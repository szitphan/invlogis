#!/usr/bin/env node
// hardened v3 — parse/readiness/testdata/history/classify/results dùng chung qua testgen-core.mjs
//
//   node .claude/scripts/playwright-gen.mjs gen --dir docs/{feature}/test [--feature slug] [--base url] [--dry-run]
//   node .claude/scripts/playwright-gen.mjs run --dir docs/{feature}/test [--env dev|sit|local] [--headed]
//        [--tc CHK-...] [--retry-failed] [--base url] [--allow-prod --confirm-prod <origin>[,<origin-api>]]
//
// gen tạo symlink e2e/node_modules -> qa/node_modules (gitignored) để spec resolve '@playwright/test'.
// run dùng qa/node_modules/.bin/playwright, rồi `npx --no-install playwright`; không có → PENDING "chưa cài: cd qa && npm install"
// (exit 0, không tải mạng). Cổng origin chặn CẢ web base lẫn API base (QA_API_BASE / envs.json apiBase);
// auth.setup.ts tự từ chối gửi mật khẩu tới origin API không có trong envs.json non-prod / .allowed-origins.
//
// Chỉ codegen TC có **Target:** web (hoặc thiếu Target). TC mob/api thuộc maestro-gen / bruno-runner.
// **Role:** {slug} → project Playwright `setup` (auth.setup.ts) đăng nhập 3 bước BE theo vai (qa/config/roles.json,
// bí mật qua biến môi trường ở qa/.env) rồi ghi storageState có khoá localStorage của FE.
// Import file này an toàn (không chạy lệnh) — dispatch chỉ khi chạy trực tiếp.
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

import {
  CHK_PATTERN,
  QUOTED_CAPTURE,
  addUniqueReason,
  checkOriginGate,
  classifyFailure,
  classifyResult,
  cleanValue,
  dataFingerprint,
  dataKeySlug,
  detectDataGaps,
  escapeRegExp,
  extractAllQuoted,

  findRepoRoot,
  firstQuotedCapture,
  inlineComment,
  isDash,
  isProdEnvName,
  isValidSlug,
  knownNonProdOrigins,
  loadAllowedOrigins,
  loadChecklistIndex,
  loadDotEnv,
  loadQaConfig,
  loadRunHistory,
  loadTestcaseDir,
  normalizeVietnamese,
  parsePreconditions,
  parseTestcasesFile,
  readinessReasons,
  requireSlug as coreRequireSlug,
  resolveDataKeys,
  resolveRole,
  safeOrigin,
  saveRunHistory,
  tcOracle,
  tcTarget,
  today,
  tsString,
  updateRunHistory,
  writeNormalizedResults,
  writeTestData,
} from './testgen-core.mjs';

class CliError extends Error {}

function fail(message) {
  throw new CliError(message);
}

function requireSlug(value, label) {
  try {
    return coreRequireSlug(value, label);
  } catch (err) {
    return fail(err.message);
  }
}

function parseArgs(argv) {
  const cmd = argv[2];
  const opts = { headed: false };

  for (let i = 3; i < argv.length; i += 1) {
    const arg = argv[i];

    if (arg === '--dir') opts.dir = argv[++i];
    else if (arg === '--feature') opts.feature = argv[++i];
    else if (arg === '--headed') opts.headed = true;
    else if (arg === '--tc') opts.tc = argv[++i];
    else if (arg === '--base') opts.base = argv[++i];
    else if (arg === '--env') opts.env = argv[++i];
    else if (arg === '--allow-prod') opts.allowProd = true;
    else if (arg === '--confirm-prod') opts.confirmProd = argv[++i];
    else if (arg === '--dry-run') opts.dryRun = true;
    else if (arg === '--retry-failed') opts.retryFailed = true;
  }

  return { cmd, opts };
}

// ---------------------------------------------------------------- nhận diện nhãn trong Action

function containsKeyword(text, keywords) {
  const group = keywords.map(escapeRegExp).join('|');
  return new RegExp(`(?:^|[\\s(])(?:${group})(?=\\s|$|[:(])`, 'i').test(String(text ?? ''));
}

function extractExplicitLabel(text, keywords) {
  const source = String(text ?? '');
  const group = keywords.map(escapeRegExp).join('|');

  // Grammar: nút "Đăng nhập" · field "Email" · link "Quên mật khẩu?" · nút có accessible name: "Đăng nhập"
  // Quote ở vị trí khác (vd `"Đăng nhập" nút`) không được dùng.
  const labelAfterRole = source.match(
    new RegExp(
      `(?:^|[\\s(])(?:${group})\\s+`
      + '(?:(?:có|co)\\s+)?'
      + '(?:accessible\\s+name\\s*:\\s*)?'
      + QUOTED_CAPTURE,
      'i',
    ),
  );

  const directLabel = firstQuotedCapture(labelAfterRole);
  if (directLabel) return directLabel;
  if (!containsKeyword(source, keywords)) return null;

  const accessibleName = source.match(new RegExp(`accessible\\s+name\\s*:\\s*${QUOTED_CAPTURE}`, 'i'));
  return firstQuotedCapture(accessibleName);
}

function looksLikeSecretLabel(label, action) {
  const combined = normalizeVietnamese(`${label ?? ''} ${action ?? ''}`);
  return /\b(password|passphrase|mat khau|secret|token|api key|otp|pin)\b/i.test(combined);
}

function looksLikeSecretLiteral(value) {
  const cleaned = cleanValue(value);
  const normalized = normalizeVietnamese(cleaned);
  return (
    /^\*{3,}$/.test(cleaned)
    || /^\[?\s*(?:secret|redacted|masked)\s*\]?$/i.test(cleaned)
    || /\b(?:secret|redacted|masked)\b/i.test(normalized)
  );
}

// Biểu thức đọc data. KHÔNG hard-code literal vào script:
// - value thường → DATA("<key>", <default>): lúc CHẠY override qua testdata.json; value test-case = DEFAULT.
// - ENV:VAR → process.env (secret, không vào testdata.json).
// - thiếu/secret-literal → incomplete (không bịa).
function dataToExpression(testData, action, label, tcId, stepId = '') {
  const value = cleanValue(testData);

  if (!value || isDash(value)) {
    return { expression: '', complete: false, reason: `Test Data trống cho field ${JSON.stringify(label)}` };
  }

  const envMatch = value.match(/^ENV\s*:\s*([A-Za-z_][A-Za-z0-9_]*)$/);
  if (envMatch) {
    return { expression: `process.env[${tsString(envMatch[1])}]`, complete: true, reason: '', envKey: envMatch[1] };
  }

  if (looksLikeSecretLabel(label, action) || looksLikeSecretLiteral(value)) {
    return {
      expression: '',
      complete: false,
      reason:
        `Test Data nhạy cảm phải khai báo dạng ENV: VAR cho field ${JSON.stringify(label)}; `
        + 'không nhúng secret literal',
    };
  }

  // Key gồm STEP để 2 field khác nhau trong cùng TC không đụng key nhau.
  const key = stepId
    ? `${dataKeySlug(tcId)}.${dataKeySlug(stepId)}.${dataKeySlug(label)}`
    : `${dataKeySlug(tcId)}.${dataKeySlug(label)}`;
  return {
    expression: `DATA(${tsString(key)}, ${tsString(value)})`,
    complete: true,
    reason: '',
    envKey: '',
    dataKey: key,
    dataDefault: value,
  };
}

function mappingResult({
  code = '',
  complete = true,
  reason = '',
  executable = false,
  assertion = false,
  dataKey = '',
  dataDefault = '',
  envKey = '',
} = {}) {
  return { code, complete, reason, executable, assertion, dataKey, dataDefault, envKey };
}

function cleanUrlToken(value) {
  return String(value ?? '').trim().replace(/[)\]};,.]+$/g, '');
}

function extractExplicitUrl(text) {
  const match = String(text ?? '').match(/(?:https?:\/\/[^\s"“”'‘’«»,]+|\/(?!\/)[^\s"“”'‘’«»,]+)/i);
  const token = cleanUrlToken(match?.[0]);
  return token || null;
}

function explicitPathname(url) {
  try {
    if (/^https?:\/\//i.test(url)) return new URL(url).pathname;
    if (url.startsWith('/') && !url.startsWith('//')) return new URL(url, 'http://playwright.local').pathname;
  } catch {
    return null;
  }
  return null;
}

function todo(reason, label, original) {
  return mappingResult({
    code: `  // TODO: ${reason}. ${label}: ${tsString(inlineComment(original))}`,
    complete: false,
    reason,
  });
}

// Dựng dòng code có data; data.envKey → test.fixme khi thiếu ENV.
function withData(data, buildLine) {
  if (!data.complete) {
    return mappingResult({ code: `  // TODO: ${inlineComment(data.reason)}.`, complete: false, reason: data.reason });
  }
  const lines = [];
  if (data.envKey) {
    lines.push(`  test.fixme(!process.env[${tsString(data.envKey)}], ${tsString(`Thiếu ENV: ${data.envKey}`)});`);
  }
  lines.push(buildLine(data.expression));
  return mappingResult({
    code: lines.join('\n'),
    complete: true,
    executable: true,
    dataKey: data.dataKey || '',
    dataDefault: data.dataDefault || '',
    envKey: data.envKey || '',
  });
}

// ---------------------------------------------------------------- Action → code

function actionToCode(action, testData = '', tcId = '', stepId = '') {
  const original = cleanValue(action);
  const normalized = normalizeVietnamese(original);

  if (!original || isDash(original)) {
    return mappingResult({ code: '  // TODO: Action trống — không sinh locator.', complete: false, reason: 'Action trống' });
  }

  if (/\b(?:roi|sau do|and then|then)\b/i.test(normalized)) {
    return todo('Action ghép nhiều thao tác — tách thành từng Step', 'Action', original);
  }

  const gotoSignal = /\b(?:truy cap|mo|vao|navigate|open|go to)\b/i.test(normalized);
  if (gotoSignal) {
    const explicitUrl = extractExplicitUrl(original);
    if (explicitUrl) {
      return mappingResult({
        code: `  await page.goto(${tsString(explicitUrl)}); /*@data-step*/`,
        complete: true,
        executable: true,
      });
    }
  }

  const quotes = extractAllQuoted(original);
  const isClick = /\b(?:click|nhan|bam)\b/i.test(normalized);

  // ng-zorro: bấm nút "A" trong dòng chứa "Z" (nz-table)
  if (isClick && /\btrong dong (?:chua|co)\b/.test(normalized)) {
    const button = extractExplicitLabel(original, ['nút', 'button']) || quotes[0];
    const rowQuoted = quotes.length >= 2 ? quotes[quotes.length - 1] : null;
    if (!button) return todo('Bấm nút trong dòng thiếu nhãn nút quoted', 'Action', original);
    const rowValue = rowQuoted || testData;
    const data = dataToExpression(rowValue, original, `dong ${button}`, tcId, stepId);
    if (!data.complete) return todo('Thiếu text nhận diện dòng (quoted hoặc Test Data)', 'Action', original);
    return withData(data, (expr) => `  await ROW_ACTION(page, ${expr}, ${tsString(button)}); /*@data-step*/`);
  }

  // ng-zorro: xác nhận hộp thoại ["Đồng ý"]
  if (/\b(?:xac nhan|dong y)\s+(?:hop thoai|modal|popup|dialog)\b/.test(normalized)) {
    const ok = quotes[0];
    return mappingResult({
      code: `  await CONFIRM_DIALOG(page${ok ? `, ${tsString(ok)}` : ''});`,
      complete: true,
      executable: true,
    });
  }

  // ng-zorro: chọn ngày "dd/MM/yyyy" trong "Y" | chọn ngày "Y" (+ Test Data)
  if (/^\s*chon ngay\b/.test(normalized)) {
    let label;
    let value;
    if (quotes.length >= 2) {
      [value, label] = [quotes[0], quotes[quotes.length - 1]];
    } else if (quotes.length === 1) {
      [label, value] = [quotes[0], testData];
    }
    if (!label) return todo('Chọn ngày thiếu nhãn ô ngày quoted', 'Action', original);
    const data = dataToExpression(value, original, label, tcId, stepId);
    return withData(data, (expr) => `  await PICK_DATE(page, ${tsString(label)}, ${expr}); /*@data-step*/`);
  }

  // ng-zorro: chọn "X" trong "Y" (nz-select, option trong overlay) | chọn trong "Y" (+ Test Data)
  if (/^\s*chon\b/.test(normalized) && /\b(?:trong|tai|o|cho)\b/.test(normalized)) {
    let label;
    let value;
    if (quotes.length >= 2) {
      [value, label] = [quotes[0], quotes[quotes.length - 1]];
    } else if (quotes.length === 1) {
      [label, value] = [quotes[0], testData];
    }
    if (!label) return todo('Chọn thiếu nhãn ô chọn quoted', 'Action', original);
    const data = dataToExpression(value, original, label, tcId, stepId);
    return withData(data, (expr) => `  await SELECT_IN(page, ${tsString(label)}, ${expr}); /*@data-step*/`);
  }

  const isInput = /\b(?:nhap|dien|fill|type)\b/i.test(normalized);
  const isObservation = /\b(?:quan sat|kiem tra|xac nhan|verify|observe)\b/i.test(normalized);
  const hasButton = containsKeyword(original, ['nút', 'button']);
  const hasLink = containsKeyword(original, ['link', 'liên kết']);
  const hasField = containsKeyword(original, ['field', 'trường', 'ô']);

  if (isClick && hasButton) {
    const label = extractExplicitLabel(original, ['nút', 'button']);
    if (!label) return todo('Click nút chưa có nhãn quoted/accessibility rõ ràng', 'Action', original);
    return mappingResult({
      code: `  await page.getByRole('button', { name: ${tsString(label)}, exact: true }).click();`,
      complete: true,
      executable: true,
    });
  }

  if (isClick && hasLink) {
    const label = extractExplicitLabel(original, ['link', 'liên kết']);
    if (!label) return todo('Click link chưa có nhãn quoted/accessibility rõ ràng', 'Action', original);
    return mappingResult({
      code: `  await page.getByRole('link', { name: ${tsString(label)}, exact: true }).click();`,
      complete: true,
      executable: true,
    });
  }

  if (isClick) {
    return mappingResult({
      code: `  // TODO: Click target chưa xác định role + nhãn — không bịa locator. Action: ${tsString(inlineComment(original))}`,
      complete: false,
      reason: 'Click target chưa có role và nhãn rõ ràng',
    });
  }

  if (isInput && hasField) {
    const label = extractExplicitLabel(original, ['field', 'trường', 'ô']);
    if (!label) {
      return mappingResult({
        code: `  // TODO: Field nhập chưa có nhãn quoted/accessibility rõ ràng. Action: ${tsString(inlineComment(original))}`,
        complete: false,
        reason: 'Field nhập thiếu nhãn quoted hoặc accessible name',
      });
    }
    const data = dataToExpression(testData, original, label, tcId, stepId);
    // FIELD(): getByLabel → getByPlaceholder → khối .label-item (FE ng-zorro). Marker /*@data-step*/
    // để `run` phân loại fail ở bước nhập data = nghi-data 🟡.
    return withData(data, (expr) => `  await (await FIELD(page, ${tsString(label)})).fill(${expr}); /*@data-step*/`);
  }

  if (isInput) {
    return mappingResult({
      code:
        '  // TODO: Input target chưa theo grammar field "X" hoặc '
        + `accessible name: "X". Action: ${tsString(inlineComment(original))}`,
      complete: false,
      reason: 'Input target thiếu grammar field/accessible name rõ ràng',
    });
  }

  if (isObservation) {
    return mappingResult({
      code: `  // TODO: Quan sát/kiểm tra không phải executable action. Action: ${tsString(inlineComment(original))}`,
      complete: false,
      reason: 'Action chỉ mô tả quan sát, không có thao tác executable',
    });
  }

  return mappingResult({
    code: `  // TODO: Chưa map action an toàn — không bịa locator. Action: ${tsString(inlineComment(original))}`,
    complete: false,
    reason: 'Action chưa map được an toàn',
  });
}

// ---------------------------------------------------------------- Expected → assertion

function expectedToCode(expected) {
  const original = cleanValue(expected);
  const normalized = normalizeVietnamese(original);

  if (!original || isDash(original)) return mappingResult({ code: '', complete: true, assertion: false });

  const isNegative = /\b(?:khong hien thi|khong hien|khong xuat hien|bi an|hidden|not visible|does not appear|is not displayed)\b/i
    .test(normalized);
  const isRedirect = /\b(?:redirect|chuyen huong|tohaveurl|url)\b/i.test(normalized);

  if (isRedirect) {
    const explicitUrl = extractExplicitUrl(original);
    if (!explicitUrl) return todo('Expected redirect chưa nêu URL/route đích rõ ràng', 'Expected', original);
    const pathname = explicitPathname(explicitUrl);
    if (!pathname) return todo('URL redirect không parse được pathname', 'Expected', original);
    const exactPathPattern = `^${escapeRegExp(pathname)}$`;
    return mappingResult({
      code:
        '  await expect(page).toHaveURL('
        + `(url) => new RegExp(${tsString(exactPathPattern)}).test(url.pathname)`
        + '); /*@assert-step*/',
      complete: true,
      assertion: true,
    });
  }

  const texts = extractAllQuoted(original);
  const isToast = /\btoast\b|\bthong bao (?:hien|xuat hien|hien thi)\b/.test(normalized);
  const isVisible = /\b(?:hien thi|hien ra|hien|render|xuat hien|visible|appear|display|displayed)\b/i.test(normalized);

  if (isToast && !isNegative) {
    if (!texts.length) return todo('Expected toast thiếu text quoted', 'Expected', original);
    return mappingResult({
      code: texts.map((t) => `  await EXPECT_TOAST(page, ${tsString(t)}); /*@assert-step*/`).join('\n'),
      complete: true,
      assertion: true,
    });
  }

  if (isNegative && texts.length) {
    return mappingResult({
      code: texts
        .map((t) => `  await expect(page.getByText(${tsString(t)}, { exact: true })).toBeHidden(); /*@assert-step*/`)
        .join('\n'),
      complete: true,
      assertion: true,
    });
  }

  if (isNegative) return todo('Expected không hiển thị thiếu text/nhãn quoted', 'Expected', original);

  if (isVisible && texts.length) {
    // Nhiều chuỗi quoted → assert TẤT CẢ (bản cũ chỉ assert chuỗi đầu).
    return mappingResult({
      code: texts
        .map((t) => `  await expect(page.getByText(${tsString(t)}, { exact: true })).toBeVisible(); /*@assert-step*/`)
        .join('\n'),
      complete: true,
      assertion: true,
    });
  }

  if (isVisible) return todo('Expected hiển thị thiếu text/nhãn quoted', 'Expected', original);

  return mappingResult({
    code: `  // TODO: Chưa map assertion an toàn. Expected: ${tsString(inlineComment(original))}`,
    complete: false,
    reason: 'Expected chưa map được thành assertion an toàn',
  });
}

// ---------------------------------------------------------------- readiness

function analyzeTestcase(tc, opts = {}) {
  const stepMappings = [];
  const dataEntries = [];
  const envKeys = [];
  let hasAssertion = false;

  if (!tc || typeof tc !== 'object') {
    return {
      ready: false,
      reason: 'test case không hợp lệ',
      reasons: ['test case không hợp lệ'],
      stepMappings,
      dataEntries,
      envKeys,
      hasAssertion: false,
    };
  }

  const reasons = readinessReasons(tc, opts);
  const target = tcTarget(tc);
  if (target !== 'web') addUniqueReason(reasons, `Target=${target} — không phải web (máy sinh khác lo)`);

  const steps = Array.isArray(tc.steps) ? tc.steps : [];
  for (const step of steps) {
    const stepNo = cleanValue(step?.n) || '?';
    const action = actionToCode(step?.action, step?.testData, tc?.chk || cleanValue(tc?.stt), stepNo);
    const expected = expectedToCode(step?.expected);

    if (action.dataKey) dataEntries.push({ key: action.dataKey, default: action.dataDefault });
    if (action.envKey && !envKeys.includes(action.envKey)) envKeys.push(action.envKey);

    stepMappings.push({ step, action, expected });

    if (!action.complete || !action.executable) {
      addUniqueReason(reasons, `Step ${stepNo}: ${action.reason || 'Action không executable'}`);
    }
    if (!expected.complete) addUniqueReason(reasons, `Step ${stepNo}: ${expected.reason || 'Expected chưa map được'}`);
    if (expected.assertion) hasAssertion = true;
  }

  // Dữ liệu tiền đề có tên (**Data:** / DATA:) → entry "@data.<key>" trong testdata.json (default rỗng).
  for (const key of resolveDataKeys(tc)) dataEntries.push({ key: `@data.${key}`, default: '' });

  if (!hasAssertion) addUniqueReason(reasons, 'test case không có assertion map được');

  return {
    ready: reasons.length === 0,
    reason: reasons[0] || '',
    reasons,
    stepMappings,
    dataEntries,
    envKeys,
    hasAssertion,
    role: resolveRole(tc),
    dataKeys: resolveDataKeys(tc),
  };
}

function isCodegenReady(tc, opts = {}) {
  const analysis = analyzeTestcase(tc, opts);
  return { ready: analysis.ready, reason: analysis.reason };
}

function tcToSpec(tc, opts = {}) {
  const testId = tc?.chk || `TC-${cleanValue(tc?.stt) || 'UNKNOWN'}`;
  const title = cleanValue(tc?.title);
  const testTitle = title ? `${testId}: ${title}` : testId;
  const analysis = analyzeTestcase(tc, opts);
  const lines = [`test(${tsString(testTitle)}, async ({ page }) => {`];

  if (!analysis.ready) lines.push(`  test.fixme(true, ${tsString(analysis.reasons.join('; '))});`);

  for (const key of analysis.dataKeys || []) {
    lines.push(
      `  test.fixme(!HAS_DATA(${tsString(key)}), `
      + `${tsString(`Thiếu dữ liệu tiền đề "${key}" — điền "@data.${key}" trong testdata.json`)});`,
    );
  }

  const pre = parsePreconditions(tc?.preconditions);
  if (!pre.empty && !pre.onlyRoleData) {
    lines.push('  // TODO: Preconditions cần fixture/state setup riêng; không coi comment này là setup.');
  }

  for (const mapping of analysis.stepMappings) {
    if (mapping.action.code) lines.push(mapping.action.code);
    if (mapping.expected.code) lines.push(mapping.expected.code);
  }

  lines.push('});');

  const body = lines.join('\n');
  const role = analysis.role;
  if (!role || opts.wrapRole === false) return body;

  // Đăng nhập sẵn theo vai: storageState do project `setup` (auth.setup.ts) ghi.
  return [
    'test.describe(() => {',
    `  test.use({ storageState: ${tsString(`.auth/${role}.json`)} });`,
    ...body.split('\n').map((l) => `  ${l}`),
    '});',
  ].join('\n');
}

function toEnvKey(feature) {
  return String(feature || 'APP').toUpperCase().replace(/[^A-Z0-9_]/g, '_');
}

function safeScopeFilename(scope) {
  if (!isValidSlug(scope)) throw new Error(`scope slug không hợp lệ: ${JSON.stringify(scope)}`);
  return scope;
}

function collectCodegenReport(tcDir, opts = {}) {
  let loaded;
  try {
    loaded = loadTestcaseDir(tcDir);
  } catch (err) {
    fail(err.message);
  }
  const report = { generated: [], skipped: [], otherTarget: [], files: loaded.files };

  for (const { scope, tc } of loaded.entries) {
    const chk = tc.chk || `TC-${tc.stt || 'UNKNOWN'}`;
    const target = tcTarget(tc);

    if (target !== 'web') {
      report.otherTarget.push({ scope, chk, target });
      continue;
    }

    const readiness = isCodegenReady(tc, opts);
    if (readiness.ready) report.generated.push({ scope, chk, title: tc.title || '', role: resolveRole(tc), tc });
    else report.skipped.push({ scope, chk, reason: readiness.reason });
  }

  return report;
}

// ---------------------------------------------------------------- ghi file

function cleanupRunArtifacts(e2eDir) {
  fs.rmSync(path.join(e2eDir, 'report.json'), { force: true });
  fs.rmSync(path.join(e2eDir, 'test-results'), { recursive: true, force: true });
  fs.rmSync(path.join(e2eDir, 'playwright-report'), { recursive: true, force: true });
}

function ensureE2EGitignore(e2eDir) {
  const gitignorePath = path.join(e2eDir, '.gitignore');
  // `node_modules` KHÔNG có dấu `/`: là symlink (file với git) nên mẫu `node_modules/` không khớp.
  const required = ['.env', '.auth/', 'report.json', 'test-results/', 'playwright-report/', 'node_modules'];
  const existing = fs.existsSync(gitignorePath) ? fs.readFileSync(gitignorePath, 'utf8') : '';
  const existingEntries = new Set(existing.split(/\r?\n/).map((line) => line.trim()).filter(Boolean));
  const additions = required.filter((entry) => !existingEntries.has(entry));
  if (!additions.length) return;
  const prefix = existing && !existing.endsWith('\n') ? '\n' : '';
  fs.writeFileSync(gitignorePath, `${existing}${prefix}${additions.join('\n')}\n`, 'utf8');
}

// Spec/config import '@playwright/test' nhưng gói cài ở qa/node_modules → symlink tương đối
// e2e/node_modules -> <repoRoot>/qa/node_modules để Node/TS resolve được (link treo khi chưa `npm install` cũng được).
// Đã có thư mục node_modules thật → giữ nguyên, không xoá.
function ensureQaNodeModulesLink(e2eDir, qaDir) {
  const link = path.join(e2eDir, 'node_modules');
  const target = path.relative(e2eDir, path.join(qaDir, 'node_modules'));
  let st = null;
  try { st = fs.lstatSync(link); } catch { st = null; }
  if (st && !st.isSymbolicLink()) return { link, target, status: 'kept-dir' };
  if (st) {
    if (fs.readlinkSync(link) === target) return { link, target, status: 'ok' };
    fs.unlinkSync(link);
  }
  fs.symlinkSync(target, link, 'dir');
  return { link, target, status: 'created' };
}

// Runner cục bộ, KHÔNG tải mạng: qa/node_modules/.bin/playwright > npx --no-install playwright > null.
function resolvePlaywrightRunner(repoRoot, e2eDir, env = process.env) {
  const local = path.join(repoRoot, 'qa', 'node_modules', '.bin', 'playwright');
  if (fs.existsSync(local)) return { bin: local, args: [], label: path.relative(repoRoot, local) };
  const probe = spawnSync('npx', ['--no-install', 'playwright', '--version'], { cwd: e2eDir, encoding: 'utf8', env });
  if (!probe.error && probe.status === 0) return { bin: 'npx', args: ['--no-install', 'playwright'], label: 'npx --no-install playwright' };
  return null;
}

function writeConfig(e2eDir, feature, base, { useSetup = false } = {}) {
  const envKey = `${toEnvKey(feature)}_BASE`;
  const fallbackBase = base || 'http://localhost:3000';
  const projects = useSetup
    ? `  projects: [
    { name: 'setup', testMatch: /auth\\.setup\\.ts$/ },
    { name: 'chromium', testMatch: /specs\\/.*\\.spec\\.ts$/, dependencies: ['setup'] },
  ],
`
    : `  projects: [
    { name: 'chromium', testMatch: /specs\\/.*\\.spec\\.ts$/ },
  ],
`;

  const config = `import { defineConfig } from '@playwright/test';

// AUTO-GENERATED bởi playwright-gen.mjs — KHÔNG sửa tay.
// baseURL: ${envKey} > QA_WEB_BASE (qa/.env hoặc qa/config/envs.json theo QA_ENV) > mặc định.
export default defineConfig({
  testDir: '.',
  use: {
    baseURL: process.env[${tsString(envKey)}] || process.env.QA_WEB_BASE || ${tsString(fallbackBase)},
    trace: 'on-first-retry',
  },
${projects}  reporter: [
    ['json', { outputFile: 'report.json' }],
    ['list'],
  ],
});
`;
  fs.writeFileSync(path.join(e2eDir, 'playwright.config.ts'), config, 'utf8');
}

function writeEnvExample(e2eDir, feature, { envKeys = [], roles = [], roleConfig = null } = {}) {
  const envKey = toEnvKey(feature);
  const lines = [
    '# Copy thành .env (gitignored). Không commit secrets. Biến dùng chung (QA_*) để ở qa/.env.',
    `${envKey}_BASE=`,
    '',
    '# Môi trường QA (qa/config/envs.json): dev|sit|local — prod bị từ chối.',
    'QA_ENV=',
    'QA_TENANT_ID=',
    'QA_WEB_BASE=',
    'QA_API_BASE=',
  ];

  if (roles.length) {
    lines.push('', '# Tài khoản theo vai (qa/config/roles.json) — test case dùng **Role:**');
    for (const role of roles) {
      const cfg = roleConfig?.[role];
      if (!cfg) {
        lines.push(`# ${role}: chưa có trong qa/config/roles.json`);
        continue;
      }
      lines.push(`# ${role} (${cfg.channel || '?'}/${cfg.audience || '?'})`);
      for (const k of ['userEnv', 'passEnv', 'orgUnitEnv', 'facilityEnv']) if (cfg[k]) lines.push(`${cfg[k]}=`);
    }
  }

  lines.push('', '# Biến ENV mà Test Data của test case dùng (Test Data: ENV: VAR):');
  if (envKeys.length) for (const k of [...envKeys].sort()) lines.push(`${k}=`);
  else lines.push('# (chưa có test case nào dùng ENV: VAR)');

  fs.writeFileSync(path.join(e2eDir, '.env.example'), `${lines.join('\n')}\n`, 'utf8');
}

// support.ts: helper tự chứa (chỉ cần @playwright/test) cho locator fallback + ng-zorro.
function writeSupport(e2eDir) {
  const contents = `// AUTO-GENERATED bởi playwright-gen.mjs — KHÔNG sửa tay (regen ghi đè).
// Helper cho FE Angular + ng-zorro (transport-erp-fe): locator fallback, nz-select, nz-date-picker,
// nz-table, modal xác nhận, toast (NzMessage role=status|alert), runtime-config.
import { expect, type Locator, type Page } from '@playwright/test';
import TESTDATA from './testdata.json';

const TD: Record<string, unknown> = (TESTDATA as Record<string, unknown>) || {};

// DATA(key, default): giá trị trong testdata.json nếu có, else default (data giả-định từ test-case).
export const DATA = (k: string, d: string): string =>
  (Object.prototype.hasOwnProperty.call(TD, k) ? String(TD[k]) : d);

// Dữ liệu tiền đề có tên (**Data:** key) — có khi testdata.json["@data.<key>"] không rỗng.
export const HAS_DATA = (key: string): boolean => {
  const v = TD[\`@data.\${key}\`];
  return v !== undefined && v !== null && String(v) !== '';
};

const q = (s: string) => JSON.stringify(s);

async function firstPresent(candidates: Locator[]): Promise<Locator> {
  for (const c of candidates) {
    if (await c.count()) return c.first();
  }
  return candidates[0];
}

// Ô nhập theo nhãn: getByLabel → getByPlaceholder → khối <div><div class="label-item">X</div>…<input></div>.
export async function FIELD(page: Page, label: string): Promise<Locator> {
  return firstPresent([
    page.getByLabel(label, { exact: true }),
    page.getByPlaceholder(label, { exact: true }),
    page.locator(\`div:has(> .label-item:text-is(\${q(label)})) :is(input, textarea)\`),
  ]);
}

async function selectBox(page: Page, label: string): Promise<Locator> {
  return firstPresent([
    page.locator(\`div:has(> .label-item:text-is(\${q(label)})) nz-select\`),
    page.locator('nz-select').filter({ has: page.locator('.ant-select-selection-placeholder', { hasText: label }) }),
    page.getByLabel(label, { exact: true }),
  ]);
}

// chọn "X" trong "Y": mở nz-select rồi bấm option trong overlay CDK.
export async function SELECT_IN(page: Page, label: string, option: string): Promise<void> {
  const box = await selectBox(page, label);
  await box.click();
  const search = box.locator('input.ant-select-selection-search-input');
  if (await search.count()) await search.first().fill(option).catch(() => {});
  const opt = page.locator('.cdk-overlay-container .ant-select-item-option').filter({ hasText: option }).first();
  await opt.waitFor({ state: 'visible' });
  await opt.click();
}

// chọn ngày: gõ vào input của nz-date-picker rồi Enter (định dạng theo FE, thường dd/MM/yyyy).
export async function PICK_DATE(page: Page, label: string, value: string): Promise<void> {
  const input = await firstPresent([
    page.locator(\`div:has(> .label-item:text-is(\${q(label)})) nz-date-picker input\`),
    page.locator(\`div:has(> .label-item:text-is(\${q(label)})) nz-range-picker input\`),
    page.getByLabel(label, { exact: true }),
    page.getByPlaceholder(label, { exact: true }),
  ]);
  await input.click();
  await input.fill(value);
  await input.press('Enter');
  await page.locator('.cdk-overlay-container .ant-picker-dropdown').first()
    .waitFor({ state: 'hidden' }).catch(() => {});
}

// bấm nút "A" trong dòng chứa "Z" (nz-table).
export async function ROW_ACTION(page: Page, rowText: string, action: string): Promise<void> {
  const row = page.locator('nz-table tbody tr, .ant-table-tbody tr').filter({ hasText: rowText }).first();
  await row.waitFor({ state: 'visible' });
  const btn = row.getByRole('button', { name: action });
  if (await btn.count()) await btn.first().click();
  else await row.getByText(action, { exact: true }).first().click();
}

// xác nhận hộp thoại: nút okText (nếu có) hoặc nút cuối của modal đang mở.
export async function CONFIRM_DIALOG(page: Page, okText?: string): Promise<void> {
  const modal = page.locator('.ant-modal-wrap:visible .ant-modal, .ant-modal-confirm').last();
  await modal.waitFor({ state: 'visible' });
  const ok = okText ? modal.getByRole('button', { name: okText }) : modal.locator('.ant-modal-footer button, .ant-modal-confirm-btns button').last();
  await ok.first().click();
  await modal.waitFor({ state: 'hidden' }).catch(() => {});
}

// toast hiện "…": NzMessage, nội dung role=status (thành công) | role=alert (lỗi).
export async function EXPECT_TOAST(page: Page, text: string): Promise<void> {
  const toast = page.locator('.ant-message [role="status"], .ant-message [role="alert"], [role="alert"], [role="status"]')
    .filter({ hasText: text });
  await expect(toast.first()).toBeVisible();
}

// Chặn assets/runtime-config.js của FE để trỏ API về môi trường đang test (QA_API_BASE).
export async function ROUTE_RUNTIME_CONFIG(page: Page): Promise<void> {
  const api = (process.env.QA_API_BASE || '').replace(/\\/+$/, '');
  if (!api) return;
  const body = 'window.__TRANSPORT_ERP_CONFIG__ = ' + JSON.stringify({
    apiUrl: \`\${api}/api/\`,
    notificationSocketUrl: \`\${api}/hubs/notifications\`,
    processesSocketUrl: \`\${api}/hubs/processes\`,
  }) + ';';
  await page.route('**/assets/runtime-config.js', (route) =>
    route.fulfill({ status: 200, contentType: 'application/javascript', body }));
}
`;
  fs.writeFileSync(path.join(e2eDir, 'support.ts'), contents, 'utf8');
}

// auth.setup.ts: đăng nhập 3 bước BE theo vai → .auth/{role}.json (storageState có khoá localStorage FE).
// Nguồn: transport-erp/bruno/00-auth/*, Identity LoginRequest/LoginResponse, transport-erp-fe
// constants/storage.constant.ts, services/auth.service.ts, features/login/login.component.ts.
function writeAuthSetup(e2eDir, roles, qaRel) {
  const p = path.join(e2eDir, 'auth.setup.ts');
  if (!roles.length) {
    fs.rmSync(p, { force: true });
    return;
  }
  const contents = `// AUTO-GENERATED bởi playwright-gen.mjs — KHÔNG sửa tay (regen ghi đè).
// Đăng nhập 3 bước BE theo vai rồi ghi storageState (.auth/<role>.json, gitignored):
//   1) POST /api/identity/v1/auth/login {username,password,deviceIdentifier,deviceName,platform,channel,rememberMe}
//   2) nextStep = workingContextSelectionRequired → POST /api/identity/v1/auth/working-organization-unit
//   3) có facility (biến facilityEnv) → POST /api/identity/v1/working-contexts/facility → workingContextId
// Vai: qa/config/roles.json · môi trường: qa/config/envs.json (QA_ENV) · bí mật: biến môi trường (qa/.env).
import { test as setup } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

const QA_DIR = path.resolve(process.cwd(), process.env.QA_DIR || ${tsString(qaRel)});
const ROLES: string[] = ${JSON.stringify(roles)};

// Khoá localStorage của FE (StorageKey trong transport-erp-fe/src/app/constants/storage.constant.ts).
const SK = {
  ACCESS_TOKEN: 'access_token',
  REFRESH_TOKEN: 'refresh_token',
  DEVICE_IDENTIFIER: 'device_identifier',
  CURRENT_MODULE_CODE: 'current_module_code',
  CURRENT_FACILITY_CONTEXT: 'current_facility_context',
  WORKING_CONTEXT_ID: 'working_context_id',
  CURRENT_WORKING_ORGANIZATION_UNIT_ID: 'current_working_organization_unit_id',
  LANGUAGE: 'language',
};

function readJson(file: string): any {
  return JSON.parse(fs.readFileSync(path.join(QA_DIR, 'config', file), 'utf8'));
}

function loadQaEnvFile(): void {
  const p = path.join(QA_DIR, '.env');
  if (!fs.existsSync(p)) return;
  for (const line of fs.readFileSync(p, 'utf8').split(/\\r?\\n/)) {
    const m = line.match(/^\\s*([A-Za-z_][A-Za-z0-9_]*)\\s*=\\s*(.*)\\s*$/);
    if (m && process.env[m[1]] === undefined) process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
  }
}

// Cổng origin API: CHỈ gửi mật khẩu tới origin non-prod khai trong qa/config/envs.json (apiBase/webBase của env
// không tên prod) hoặc file .allowed-origins (cạnh playwright.config.ts), hoặc host cục bộ. Không có cờ vượt.
function safeOrigin(url: string): string {
  try { const u = new URL(url); return \`\${u.protocol}//\${u.host}\`; } catch { return ''; }
}

function isLocalOrigin(origin: string): boolean {
  return /^(https?:\\/\\/)?(localhost|127\\.0\\.0\\.1|\\[::1\\]|[^/]*\\.(local|test|localhost))(:\\d+)?$/i.test(origin);
}

function allowedApiOrigins(envs: any): Set<string> {
  const set = new Set<string>();
  for (const [name, cfg] of Object.entries<any>(envs || {})) {
    if (name.startsWith('_') || /^(prod|production|live|prd)$/i.test(name) || !cfg || typeof cfg !== 'object') continue;
    for (const k of ['apiBase', 'webBase']) {
      const o = safeOrigin(String(cfg[k] || ''));
      if (o) set.add(o);
    }
  }
  const f = path.resolve(process.cwd(), '.allowed-origins');
  if (fs.existsSync(f)) {
    for (const raw of fs.readFileSync(f, 'utf8').split(/\\r?\\n/)) {
      const line = raw.trim();
      if (!line || line.startsWith('#')) continue;
      set.add(safeOrigin(line) || line);
    }
  }
  return set;
}

async function post(url: string, headers: Record<string, string>, body: unknown): Promise<any> {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...headers },
    body: JSON.stringify(body),
  });
  const text = await res.text();
  let json: any = {};
  try { json = text ? JSON.parse(text) : {}; } catch { json = { raw: text.slice(0, 200) }; }
  if (!res.ok || json?.isSuccess === false) {
    // KHÔNG in token; errorCode/message đủ để phân loại (sai tài khoản = nghi-data).
    throw new Error(\`POST \${new URL(url).pathname} -> \${res.status} \${json?.errorCode || ''} \${json?.message || ''}\`.trim());
  }
  return json?.data ?? json;
}

for (const role of ROLES) {
  setup(\`login \${role}\`, async () => {
    loadQaEnvFile();
    const envName = process.env.QA_ENV || 'dev';
    if (/^(prod|production|live|prd)$/i.test(envName)) throw new Error('QA không được chạy trên prod.');
    const envs = readJson('envs.json');
    const env = envs[envName];
    if (!env) throw new Error(\`Môi trường "\${envName}" không có trong qa/config/envs.json\`);
    const roles = readJson('roles.json');
    const cfg = roles[role];
    if (!cfg) throw new Error(\`Vai "\${role}" không có trong qa/config/roles.json\`);

    const apiBase = String(process.env.QA_API_BASE || env.apiBase || '').replace(/\\/+$/, '');
    const webBase = process.env.QA_WEB_BASE || (env.webBaseEnv && process.env[env.webBaseEnv]) || env.webBase;
    const tenantId = process.env[env.tenantIdEnv || 'QA_TENANT_ID'] || '';
    const user = process.env[cfg.userEnv];
    const pass = process.env[cfg.passEnv];
    setup.skip(!apiBase || !webBase || !tenantId, 'Thiếu QA_API_BASE/QA_WEB_BASE/QA_TENANT_ID (qa/.env)');
    setup.skip(!user || !pass, \`Thiếu \${cfg.userEnv} / \${cfg.passEnv} trong qa/.env\`);

    const apiOrigin = safeOrigin(apiBase);
    if (!apiOrigin || (!isLocalOrigin(apiOrigin) && !allowedApiOrigins(envs).has(apiOrigin))) {
      throw new Error(\`Từ chối gửi thông tin đăng nhập tới API \${apiOrigin || '(không hợp lệ)'} — origin chưa khai non-prod trong qa/config/envs.json hoặc .allowed-origins\`);
    }

    const idn = \`\${apiBase}/api/identity/v1\`;
    const base = { 'X-Tenant-Id': tenantId };
    const mobile = String(cfg.channel).toLowerCase() === 'mobile';
    const deviceIdentifier = \`qa-playwright-\${role}\`;
    const moduleCode = process.env.QA_MODULE_CODE || cfg.moduleCode || 'fuel';

    const l1 = await post(\`\${idn}/auth/login\`, base, {
      username: user,
      password: pass,
      deviceIdentifier,
      deviceName: 'QA Playwright',
      platform: cfg.platform || (mobile ? 'Android' : 'Web'),
      channel: mobile ? 'Mobile' : 'Web',
      rememberMe: false,
    });

    let accessToken: string = l1.accessToken;
    let refreshToken: string = l1.refreshToken;
    let ouId: string | undefined = l1.currentContext?.workingOrganizationUnitId;
    const step = String(l1.nextStep || '').toLowerCase();

    if (step === 'workingcontextselectionrequired' || step === '2') {
      const options: any[] = l1.workingContextOptions || [];
      const wanted = cfg.orgUnitEnv ? process.env[cfg.orgUnitEnv] : undefined;
      const opt = (wanted && options.find((o) => String(o.workingOrganizationUnitId) === wanted)) || options[0];
      if (!l1.continuationToken || !opt) throw new Error('Login cần chọn đơn vị nhưng thiếu continuationToken/workingContextOptions');
      const l2 = await post(\`\${idn}/auth/working-organization-unit\`, base, {
        temporaryToken: l1.continuationToken,
        workingOrganizationUnitId: String(opt.workingOrganizationUnitId),
      });
      accessToken = l2.accessToken;
      refreshToken = l2.refreshToken;
      ouId = l2.currentContext?.workingOrganizationUnitId ?? String(opt.workingOrganizationUnitId);
    } else if (step && step !== 'authenticated' && step !== '3') {
      throw new Error(\`nextStep không hỗ trợ: \${l1.nextStep} (vd đổi mật khẩu lần đầu) — kiểm tài khoản seed\`);
    }
    if (!accessToken) throw new Error('Không nhận được accessToken');

    const facilityId = cfg.facilityEnv ? process.env[cfg.facilityEnv] : undefined;
    let workingContextId: string | undefined;
    if (facilityId) {
      const l3 = await post(
        \`\${idn}/working-contexts/facility\`,
        { ...base, Authorization: \`Bearer \${accessToken}\` },
        { moduleCode, facilityId: Number(facilityId) },
      );
      workingContextId = l3.workingContextId;
    }

    const ls = [
      { name: SK.ACCESS_TOKEN, value: accessToken },
      { name: SK.REFRESH_TOKEN, value: refreshToken || '' },
      { name: SK.DEVICE_IDENTIFIER, value: deviceIdentifier },
      { name: SK.CURRENT_MODULE_CODE, value: moduleCode },
      { name: SK.LANGUAGE, value: process.env.QA_LANGUAGE || 'vi' },
    ];
    if (ouId) ls.push({ name: SK.CURRENT_WORKING_ORGANIZATION_UNIT_ID, value: String(ouId) });
    if (workingContextId && facilityId) {
      ls.push({ name: SK.WORKING_CONTEXT_ID, value: workingContextId });
      ls.push({
        name: SK.CURRENT_FACILITY_CONTEXT,
        value: JSON.stringify({ selectionType: 'selected', facilityCount: 1, executionFacilityId: String(facilityId) }),
      });
    }

    const state = { cookies: [], origins: [{ origin: new URL(webBase).origin, localStorage: ls }] };
    fs.mkdirSync('.auth', { recursive: true });
    fs.writeFileSync(path.join('.auth', \`\${role}.json\`), JSON.stringify(state, null, 2));
  });
}
`;
  fs.writeFileSync(p, contents, 'utf8');
}

function writeIndex(e2eDir, feature, report) {
  const day = today();
  const generatedByScope = new Map();
  for (const item of report.generated) {
    if (!generatedByScope.has(item.scope)) generatedByScope.set(item.scope, []);
    generatedByScope.get(item.scope).push(item);
  }

  const specRows = [...generatedByScope.entries()]
    .sort(([left], [right]) => left.localeCompare(right))
    .map(([scope, tests]) => {
      const spec = `specs/${safeScopeFilename(scope)}.spec.ts`;
      return `| ${scope} | [${spec}](${spec}) | ${tests.length} | — | ${day} |`;
    })
    .join('\n');

  const testRows = report.generated
    .slice()
    .sort((a, b) => a.chk.localeCompare(b.chk))
    .map((item) => {
      const spec = `specs/${safeScopeFilename(item.scope)}.spec.ts`;
      return `| ${item.chk} | ${item.scope} | [${spec}](${spec}) | Generated | — | — |`;
    })
    .join('\n');

  const skippedRows = report.skipped
    .slice()
    .sort((a, b) => `${a.scope}:${a.chk}`.localeCompare(`${b.scope}:${b.chk}`))
    .map((item) => `| ${item.scope} | ${item.chk} | ${item.reason} |`)
    .join('\n');

  const otherCounts = {};
  for (const item of report.otherTarget || []) otherCounts[item.target] = (otherCounts[item.target] || 0) + 1;
  const otherLine = Object.keys(otherCounts).length
    ? Object.entries(otherCounts).map(([t, n]) => `${t}: ${n}`).join(' · ')
    : 'không có';

  const index = `---
type: e2e-index
feature: ${feature}
status: draft
updated: ${day}
links:
  - docs/${feature}/test/testcases/${feature}-testcase-index.md
---

# Playwright E2E — ${feature}

> Specs auto-gen từ test cases (**Target:** web hoặc thiếu Target). Sửa nghiệp vụ ở \`/test-cases\` rồi regen — không sửa \`.spec.ts\` tay.
> TC kênh khác (không sinh ở đây): ${otherLine}.

## Specs

| Scope | File | Tests | Kết quả gần nhất | Updated |
|-------|------|-------|------------------|---------|
${specRows || '| — | — | 0 | — | — |'}

## Test cases

| CHK-ID | Scope | Spec | Codegen | Kết quả gần nhất | Chạy lúc |
|--------|-------|------|---------|------------------|----------|
${testRows || '| — | — | — | — | — | — |'}

## Skipped (không codegen — manual/TBD/retired/mapping chưa an toàn)

| Scope | CHK-ID | Lý do |
|-------|--------|-------|
${skippedRows || '| — | — | — |'}
`;

  fs.writeFileSync(path.join(e2eDir, `${feature}-e2e-index.md`), index, 'utf8');
}

function resolveFeature(opts, dir) {
  return requireSlug(opts.feature || path.basename(path.dirname(dir)), 'feature');
}

function gen(opts) {
  if (!opts.dir) fail('thiếu --dir');

  const dir = path.resolve(opts.dir);
  const tcDir = path.join(dir, 'testcases');
  if (!fs.existsSync(tcDir) || !fs.statSync(tcDir).isDirectory()) fail(`không có ${tcDir} — chạy /test-cases trước`);

  const repoRoot = findRepoRoot(dir);
  const qa = loadQaConfig(repoRoot);
  const analyzeOpts = { roles: qa.roles || undefined };

  const report = collectCodegenReport(tcDir, analyzeOpts);
  if (!report.files.length) fail(`không có testcases-*.md trong ${tcDir}`);

  const feature = resolveFeature(opts, dir);
  const e2eDir = path.join(dir, 'e2e');
  const specsDir = path.join(e2eDir, 'specs');

  const byScope = new Map();
  const scopeDataDefaults = new Map();
  const dataKeyConflicts = [];
  const envKeys = new Set();
  const roles = new Set();

  for (const item of report.generated) {
    if (!byScope.has(item.scope)) byScope.set(item.scope, []);
    byScope.get(item.scope).push(item.tc);
    if (item.role) roles.add(item.role);
  }

  if (opts.dryRun) {
    console.log(
      `DRY-RUN: sẽ gen ${report.generated.length} test trong ${byScope.size} spec; `
      + `skip ${report.skipped.length}; kênh khác ${report.otherTarget.length}. Chưa ghi file.`,
    );
    for (const [scope, tests] of byScope.entries()) {
      console.log(`   • specs/${safeScopeFilename(scope)}.spec.ts — ${tests.length} test`);
    }
    if (roles.size) console.log(`   • auth.setup.ts — vai: ${[...roles].sort().join(', ')}`);
    for (const skipped of report.skipped) console.log(`   ⏭  ${skipped.scope} · ${skipped.chk} · ${skipped.reason}`);
    return {
      dryRun: true,
      generated: report.generated.length,
      skipped: report.skipped.length,
      otherTarget: report.otherTarget.length,
    };
  }

  fs.mkdirSync(specsDir, { recursive: true });
  cleanupRunArtifacts(e2eDir);
  ensureE2EGitignore(e2eDir);
  const nodeModulesLink = ensureQaNodeModulesLink(e2eDir, qa.qaDir);

  for (const sourceFile of report.files) {
    const scope = sourceFile.replace(/^testcases-/i, '').replace(/\.md$/i, '');
    requireSlug(scope, `scope từ ${sourceFile}`);
    const specPath = path.join(specsDir, `${safeScopeFilename(scope)}.spec.ts`);
    const ready = byScope.get(scope) || [];

    if (!ready.length) {
      if (fs.existsSync(specPath)) fs.unlinkSync(specPath);
      continue;
    }

    for (const tc of ready) {
      const analysis = analyzeTestcase(tc, analyzeOpts);
      for (const k of analysis.envKeys || []) envKeys.add(k);
      for (const e of analysis.dataEntries || []) {
        if (!scopeDataDefaults.has(e.key)) {
          scopeDataDefaults.set(e.key, e.default);
        } else if (scopeDataDefaults.get(e.key) !== e.default) {
          dataKeyConflicts.push({ key: e.key, kept: scopeDataDefaults.get(e.key), dropped: e.default });
        }
      }
    }

    const body = [
      "import { test, expect } from '@playwright/test';",
      "import { DATA, HAS_DATA, FIELD, SELECT_IN, PICK_DATE, ROW_ACTION, CONFIRM_DIALOG, EXPECT_TOAST, ROUTE_RUNTIME_CONFIG } from '../support';",
      '',
      `// AUTO-GENERATED bởi playwright-gen.mjs từ testcases-${scope}.md — KHÔNG sửa tay (regen sẽ ghi đè).`,
      '// Trace: mỗi test() title bắt đầu bằng CHK-ID.',
      '// Test data TÁCH khỏi script: sửa ../testdata.json để khớp môi trường, KHÔNG sửa file này.',
      '// DATA(key, default): dùng giá trị trong testdata.json nếu có, else default (data giả-định từ test-case).',
      '',
      `test.describe(${tsString(scope)}, () => {`,
      '  test.beforeEach(async ({ page }) => { await ROUTE_RUNTIME_CONFIG(page); });',
      '',
      ...ready.map((tc) => tcToSpec(tc, analyzeOpts).split('\n').map((line) => `  ${line}`).join('\n')),
      '});',
      '',
    ].join('\n');

    fs.writeFileSync(specPath, body, 'utf8');
  }

  const roleList = [...roles].sort();
  const qaRel = path.relative(e2eDir, qa.qaDir) || '.';
  writeSupport(e2eDir);
  writeAuthSetup(e2eDir, roleList, qaRel);
  writeConfig(e2eDir, feature, opts.base, { useSetup: roleList.length > 0 });
  writeEnvExample(e2eDir, feature, { envKeys: [...envKeys], roles: roleList, roleConfig: qa.roles });
  try {
    writeTestData(e2eDir, scopeDataDefaults);
  } catch (err) {
    fail(err.message);
  }
  writeIndex(e2eDir, feature, report);

  console.log(
    `✅ gen: ${report.generated.length} test trong ${byScope.size} spec; skip ${report.skipped.length}`
    + (report.otherTarget.length ? `; ${report.otherTarget.length} TC kênh khác (mob/api) bỏ qua` : ''),
  );
  if (roleList.length) console.log(`   🔑 auth.setup.ts: đăng nhập sẵn vai ${roleList.join(', ')}`);
  for (const skipped of report.skipped) console.log(`   ⏭  ${skipped.scope} · ${skipped.chk} · ${skipped.reason}`);
  for (const c of dataKeyConflicts) {
    console.warn(
      `   ⚠ data key trùng "${c.key}": giữ default ${JSON.stringify(c.kept)}, bỏ ${JSON.stringify(c.dropped)} — `
      + '2 field khác nhau đang đọc chung 1 entry testdata.json. Đổi nhãn field trong test-case cho khác nhau.',
    );
  }

  return {
    gen: [...byScope.entries()].map(([scope, tests]) => ({
      scope,
      file: `specs/${safeScopeFilename(scope)}.spec.ts`,
      count: tests.length,
    })),
    skip: report.skipped,
    otherTarget: report.otherTarget,
    roles: roleList,
    envKeys: [...envKeys].sort(),
    dataKeyConflicts,
    nodeModulesLink,
  };
}

// ---------------------------------------------------------------- report Playwright

function resultErrorText(result) {
  const parts = [];
  if (result?.error) {
    if (typeof result.error === 'string') parts.push(result.error);
    else parts.push(result.error.message || '', result.error.stack || '', result.error.snippet || '');
  }
  for (const error of result?.errors || []) {
    if (typeof error === 'string') parts.push(error);
    else parts.push(error?.message || '', error?.stack || '');
  }
  return parts.filter(Boolean).join('\n');
}

function isNavigationUnavailableResult(result) {
  const text = resultErrorText(result);
  if (!text) return false;
  const hasNavigationContext = /(?:page\.goto|navigation|navigate|navigating|browser has been closed while navigating)/i.test(text);
  const hasNetworkFailure = /(?:ECONNREFUSED|ECONNRESET|ENOTFOUND|EAI_AGAIN|ERR_CONNECTION_REFUSED|ERR_CONNECTION_RESET|ERR_CONNECTION_CLOSED|ERR_NAME_NOT_RESOLVED|Failed to connect|connect ECONNREFUSED)/i.test(text);
  return hasNavigationContext && hasNetworkFailure;
}

function isNavigationUnavailableTest(test) {
  const results = Array.isArray(test?.results) ? test.results : [];
  const failedResults = results.filter((result) => (
    ['failed', 'timedOut', 'interrupted'].includes(result?.status)
    || Boolean(result?.error)
    || (Array.isArray(result?.errors) && result.errors.length > 0)
  ));
  return failedResults.length > 0 && failedResults.every(isNavigationUnavailableResult);
}

function getReportStatus(test) {
  const status = String(test?.status || '');
  if (status === 'expected' || status === 'flaky') return 'PASS';
  if (status === 'skipped') return 'PENDING';
  if (status === 'unexpected') return isNavigationUnavailableTest(test) ? 'PENDING' : 'FAIL';
  return 'PENDING';
}

function mergeAggregatedStatus(previous, next) {
  const rank = { PASS: 1, PENDING: 2, FAIL: 3 };
  if (!previous) return next;
  return rank[next] > rank[previous] ? next : previous;
}

function parsePlaywrightReport(reportPath) {
  const results = new Map();
  const errorTexts = new Map();
  const setupFailures = [];

  if (!fs.existsSync(reportPath)) {
    return { results, errorTexts, setupFailures, stats: {}, reportFound: false, reportValid: false, error: 'report.json không tồn tại' };
  }

  let report;
  try {
    report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
  } catch {
    return { results, errorTexts, setupFailures, stats: {}, reportFound: true, reportValid: false, error: 'report.json không phải JSON hợp lệ' };
  }

  if (!report || !Array.isArray(report.suites)) {
    return {
      results, errorTexts, setupFailures, stats: report?.stats || {}, reportFound: true, reportValid: false,
      error: 'report.json không đúng schema Playwright JSON reporter',
    };
  }

  const canonicalKeys = new Map();
  const mergeResult = (chk, status, errorText) => {
    const normalizedKey = chk.toLowerCase();
    const canonical = canonicalKeys.get(normalizedKey) || chk;
    canonicalKeys.set(normalizedKey, canonical);
    results.set(canonical, mergeAggregatedStatus(results.get(canonical), status));
    if (status === 'FAIL' && errorText && !errorTexts.has(canonical)) errorTexts.set(canonical, errorText);
  };

  function walkSuite(suite) {
    for (const spec of suite?.specs || []) {
      const title = String(spec?.title || '');
      const chkMatch = title.match(/\bCHK-[a-z0-9][a-z0-9-]*-\d{3,}\b/i);

      if (!chkMatch) {
        const login = title.match(/^login\s+([a-z0-9-]+)$/i);
        if (login) {
          for (const t of spec?.tests || []) {
            if (getReportStatus(t) === 'FAIL') setupFailures.push(login[1]);
          }
        }
        continue;
      }

      for (const playwrightTest of spec?.tests || []) {
        const status = getReportStatus(playwrightTest);
        const attempts = Array.isArray(playwrightTest?.results) ? playwrightTest.results : [];
        // Status tổng hợp đúng nằm ở test.status; error text lấy từ các attempt.
        if (!attempts.length) {
          mergeResult(chkMatch[0], status);
          continue;
        }
        for (const attempt of attempts) mergeResult(chkMatch[0], status, resultErrorText(attempt));
      }
    }
    for (const child of suite?.suites || []) walkSuite(child);
  }

  for (const suite of report.suites) walkSuite(suite);

  return {
    results, errorTexts, setupFailures, stats: report.stats || {}, reportFound: true, reportValid: true, error: '',
  };
}

function summarizeResults(results) {
  const summary = { passed: 0, failed: 0, pending: 0 };
  for (const status of results.values()) {
    if (status === 'PASS') summary.passed += 1;
    else if (status === 'FAIL') summary.failed += 1;
    else summary.pending += 1;
  }
  return summary;
}

function updateIndexResults(e2eDir, feature, results) {
  const indexPath = path.join(e2eDir, `${feature}-e2e-index.md`);
  if (!fs.existsSync(indexPath)) return;

  const day = today();
  const perScope = new Map();
  const normalizedResults = new Map([...results.entries()].map(([chk, status]) => [chk.toLowerCase(), status]));
  const lines = fs.readFileSync(indexPath, 'utf8').split('\n');

  const updatedLines = lines.map((line) => {
    if (!/^\|\s*CHK-[a-z0-9][a-z0-9-]*-\d{3,}\s*\|/i.test(line)) return line;
    const cells = line.split('|').map((cell) => cell.trim());
    const chk = cells[1];
    const scope = cells[2];
    const status = normalizedResults.get(chk.toLowerCase());
    if (!status) return line;
    if (!perScope.has(scope)) perScope.set(scope, []);
    perScope.get(scope).push(status);
    cells[5] = status;
    cells[6] = day;
    return `| ${cells.slice(1, -1).join(' | ')} |`;
  });

  const finalLines = updatedLines.map((line) => {
    if (!/^\|\s*[^|]+\s*\|\s*\[specs\/[^|]+\]\([^)]*\)\s*\|/i.test(line)) return line;
    const cells = line.split('|').map((cell) => cell.trim());
    const statuses = perScope.get(cells[1]);
    if (!statuses?.length) return line;
    const pass = statuses.filter((s) => s === 'PASS').length;
    const failCount = statuses.filter((s) => s === 'FAIL').length;
    const pending = statuses.filter((s) => s === 'PENDING').length;
    cells[4] = [pass ? `PASS ${pass}` : '', failCount ? `FAIL ${failCount}` : '', pending ? `PENDING ${pending}` : '']
      .filter(Boolean).join(', ');
    cells[5] = day;
    return `| ${cells.slice(1, -1).join(' | ')} |`;
  });

  fs.writeFileSync(indexPath, `${finalLines.join('\n')}\n`, 'utf8');
}

// Phân loại mỗi kết quả (core.classifyResult) + gom data cần bổ sung. opts.oracles: Map(chkLower → {label, kind}).
function buildRunReport(e2eDir, feature, parsed, history, opts = {}) {
  const gaps = detectDataGaps(e2eDir);
  const fingerprint = dataFingerprint(gaps.current);
  const stillDefaultKeys = new Set(gaps.stillDefault.map((d) => d.key));
  const oracles = opts.oracles instanceof Map ? opts.oracles : new Map();

  const rows = [];
  for (const [chk, status] of parsed.results.entries()) {
    const kind = status === 'FAIL' ? classifyFailure(parsed.errorTexts.get(chk) || '') : '';
    const oracle = oracles.get(chk.toLowerCase()) || null;
    const r = classifyResult({ status, kind, oracle, prev: history[chk], fingerprint });
    rows.push({ chk, status, category: r.status, note: r.note, oracle: oracle?.label || '' });
  }
  rows.sort((a, b) => a.chk.localeCompare(b.chk));

  return { rows, gaps, fingerprint, stillDefaultKeys };
}

const ICON = {
  PASS: '✅', FAIL_APP: '🔴', FAIL_DATA: '🟡', FAIL_OUTDATE: '🟠', FAIL_DOC: '🟣', PENDING: '⏳', FAIL: '❌',
};
const LABEL = {
  PASS: 'Đậu',
  FAIL_APP: 'Nghi app bug',
  FAIL_DATA: 'Nghi data',
  FAIL_OUTDATE: 'Nghi data outdate',
  FAIL_DOC: 'Nghi lệch tài liệu',
  PENDING: 'Chờ (chưa chạy được)',
  FAIL: 'Rớt',
};

function writeRunReport(e2eDir, feature, report, summary, origin) {
  const day = today();
  const countBy = (cat) => report.rows.filter((r) => r.category === cat).length;
  const lines = [];

  lines.push(`# Kết quả chạy Playwright — ${feature}`);
  lines.push('');
  lines.push(`> Chạy: ${day} · Môi trường: \`${origin || '(local/không rõ)'}\``);
  lines.push('>');
  lines.push(
    `> ✅ ${summary.passed} đậu · 🔴 ${countBy('FAIL_APP')} nghi app bug · 🟣 ${countBy('FAIL_DOC')} nghi lệch tài liệu · `
    + `🟡 ${countBy('FAIL_DATA')} nghi data · 🟠 ${countBy('FAIL_OUTDATE')} nghi data outdate · ⏳ ${summary.pending} chờ`,
  );
  lines.push('');
  lines.push('Report này KHÔNG tự sửa gì. Đọc mục "Data cần bổ sung", cấp data thật vào '
    + '`e2e/testdata.json` (secret để `e2e/.env` hoặc `qa/.env`), rồi chạy lại phần chưa đậu:');
  lines.push('');
  lines.push('```');
  lines.push(`node .claude/scripts/playwright-gen.mjs run --dir docs/${feature}/test --retry-failed`);
  lines.push('```');
  lines.push('');
  lines.push('🟣 nghi lệch tài liệu = rớt ở assertion trong khi đáp án là `UC cũ` / `tái lập` (chưa chốt) → mở OQ ở doc BA, chưa báo dev.');
  lines.push('');
  lines.push('## Kết quả từng case');
  lines.push('');
  lines.push('| CHK-ID | Kết quả | Đáp án | Ghi chú |');
  lines.push('|---|---|---|---|');
  for (const r of report.rows) {
    lines.push(`| ${r.chk} | ${ICON[r.category] || ''} ${LABEL[r.category] || r.category} | ${r.oracle || '—'} | ${r.note} |`);
  }
  lines.push('');

  const outdateChks = report.rows.filter((r) => r.category === 'FAIL_OUTDATE').map((r) => r.chk);
  const hasDataWork = report.gaps.stillDefault.length || report.gaps.missing.length || outdateChks.length;
  lines.push('## Data cần bổ sung / kiểm lại');
  lines.push('');
  if (!hasDataWork) {
    lines.push('_Không có data nào còn giá-trị-giả hoặc thiếu. Nếu vẫn rớt, nghi app bug (xem cột trên)._');
  } else {
    lines.push('| Key data | Giá trị hiện tại | Vấn đề | Cấp vào đâu |');
    lines.push('|---|---|---|---|');
    for (const d of report.gaps.stillDefault) {
      const issue = d.key.startsWith('@data.') ? 'dữ liệu tiền đề chưa điền' : 'còn giá-trị-giả (mẫu từ test-case)';
      lines.push(`| \`${d.key}\` | \`${d.value}\` | ${issue} | \`e2e/testdata.json\` |`);
    }
    for (const k of report.gaps.missing) lines.push(`| \`${k}\` | _(thiếu)_ | chưa có trong testdata.json | \`e2e/testdata.json\` |`);
    if (outdateChks.length) {
      lines.push(`| _(data dùng chung)_ | — | ${outdateChks.join(', ')} từng PASS nay fail bước data → nghi outdate | kiểm \`e2e/testdata.json\` |`);
    }
    lines.push('');
    lines.push('> Secret (mật khẩu/token) KHÔNG điền vào testdata.json — khai `ENV: VAR` ở test-case, '
      + 'value để `e2e/.env` / `qa/.env`. Nếu data thật khác data giả và muốn ghi ngược vào test-case, chạy lại `/playwright-gen` sẽ hỏi.');
  }
  lines.push('');

  fs.writeFileSync(path.join(e2eDir, 'run-report.md'), lines.join('\n'), 'utf8');
}

function loadOracles(dir) {
  const oracles = new Map();
  const tcDir = path.join(dir, 'testcases');
  if (!fs.existsSync(tcDir)) return oracles;
  const index = loadChecklistIndex(dir);
  try {
    for (const { tc } of loadTestcaseDir(tcDir).entries) {
      if (tc.chk) oracles.set(tc.chk.toLowerCase(), tcOracle(tc, index));
    }
  } catch { /* scope lỗi → bỏ qua nhãn đáp án, vẫn phân loại được */ }
  return oracles;
}

const NOT_INSTALLED_NOTE = 'chưa cài: cd qa && npm install';

// Không có Playwright cục bộ → KHÔNG tải mạng; ghi PENDING cho các TC web đã sinh (theo --tc / --retry-failed nếu có).
function pendingNotInstalled(dir, feature, qa, qaEnv, env, opts, retryFilter) {
  const report = collectCodegenReport(path.join(dir, 'testcases'), { roles: qa.roles || undefined });
  let chks = [...new Set(report.generated.map((g) => g.chk).filter(Boolean))];
  if (opts.tc) chks = chks.filter((c) => c.toLowerCase().includes(String(opts.tc).toLowerCase()));
  else if (retryFilter) chks = chks.filter((c) => new RegExp(`^(?:${retryFilter})$`).test(c));
  const at = new Date().toISOString();
  writeNormalizedResults(dir, chks.map((chk) => ({
    chk, target: 'web', status: 'PENDING', env: qaEnv, build: env.QA_BUILD || '', at, note: NOT_INSTALLED_NOTE,
  })));
  console.log(`⏳ Playwright ${NOT_INSTALLED_NOTE} (không thấy qa/node_modules/.bin/playwright, npx --no-install cũng không có) — ${chks.length} TC web ghi PENDING.`);
  console.log(`🧾 Kết quả chuẩn hoá: ${path.join('docs', feature, 'test', 'results', 'latest.json')}`);
  process.exitCode = 0;
  return { passed: 0, failed: 0, pending: chks.length, notInstalled: true };
}

function run(opts) {
  if (!opts.dir) fail('thiếu --dir');

  const dir = path.resolve(opts.dir);
  const feature = resolveFeature(opts, dir);
  const e2eDir = path.join(dir, 'e2e');
  const configPath = path.join(e2eDir, 'playwright.config.ts');
  const reportPath = path.join(e2eDir, 'report.json');

  if (!fs.existsSync(configPath)) fail('chưa gen — chạy `gen` trước');

  // --retry-failed: đọc run-history → chạy lại CHỈ case chưa-PASS vòng trước.
  let retryFilter = '';
  if (opts.retryFailed) {
    const history = loadRunHistory(e2eDir);
    const notPassed = Object.keys(history).filter((chk) => history[chk]?.lastStatus !== 'PASS');
    if (!notPassed.length) {
      console.log('✅ --retry-failed: không có case nào chưa-PASS ở vòng trước — không cần chạy lại.');
      return { passed: 0, failed: 0, pending: 0 };
    }
    retryFilter = notPassed.map((c) => escapeRegExp(c)).join('|');
    console.log(`↻ --retry-failed: chạy lại ${notPassed.length} case chưa-PASS: ${notPassed.join(', ')}`);
  }

  const repoRoot = findRepoRoot(dir);
  const qa = loadQaConfig(repoRoot);
  const env = {
    ...process.env,
    ...loadDotEnv(path.join(qa.qaDir, '.env')),
    ...loadDotEnv(path.join(e2eDir, '.env')),
  };

  const qaEnv = opts.env || env.QA_ENV || 'dev';
  if (isProdEnvName(qaEnv) && !opts.allowProd) {
    fail(`QA_ENV=${qaEnv} là production — từ chối (cần --allow-prod --confirm-prod <origin>).`);
  }
  env.QA_ENV = qaEnv;
  const envCfg = qa.envs?.[qaEnv];
  if (envCfg) {
    if (!env.QA_API_BASE && envCfg.apiBase) env.QA_API_BASE = envCfg.apiBase;
    const webBase = (envCfg.webBaseEnv && env[envCfg.webBaseEnv]) || envCfg.webBase;
    if (!env.QA_WEB_BASE && webBase) env.QA_WEB_BASE = webBase;
  }
  env.QA_DIR = env.QA_DIR || qa.qaDir;

  const featureBaseKey = `${toEnvKey(feature)}_BASE`;
  if (opts.base) env[featureBaseKey] = opts.base;

  // ── PRODUCTION SAFETY GATE ── baseURL cuối: --base > {FEATURE}_BASE > QA_WEB_BASE.
  const baseUrl = opts.base || env[featureBaseKey] || env.QA_WEB_BASE || '';
  const origin = safeOrigin(baseUrl);
  const allowlist = new Set([...loadAllowedOrigins(e2eDir), ...knownNonProdOrigins(qa.envs)]);
  // --confirm-prod nhận 1 hoặc nhiều origin (phẩy) — mỗi origin web/API phải được xác nhận riêng.
  const confirmed = String(opts.confirmProd || '').split(',').map((s) => s.trim()).filter(Boolean);
  const gateOrigin = (o, label) => {
    const gate = checkOriginGate({ origin: o, allowlist, allowProd: opts.allowProd, confirmProd: confirmed.includes(o) ? o : '' });
    if (!gate.ok) fail(`[${label}] ${gate.message.replace('file .allowed-origins', `${path.join(e2eDir, '.allowed-origins')}`)}`);
    if (gate.prod) console.log(`⚠️  [${label}] ${gate.message}`);
  };
  gateOrigin(origin, 'web');
  // API (QA_API_BASE / env.apiBase): FE bị trỏ về đây (ROUTE_RUNTIME_CONFIG) và auth.setup.ts gửi mật khẩu tới đây.
  if (env.QA_API_BASE) {
    const apiOrigin = safeOrigin(env.QA_API_BASE);
    if (!apiOrigin) fail(`[api] QA_API_BASE không phải URL hợp lệ`);
    gateOrigin(apiOrigin, 'api');
  }

  const runner = resolvePlaywrightRunner(repoRoot, e2eDir, env);
  if (!runner) return pendingNotInstalled(dir, feature, qa, qaEnv, env, opts, retryFilter);

  cleanupRunArtifacts(e2eDir);

  const args = [...runner.args, 'test', '--config', 'playwright.config.ts'];
  if (opts.headed) args.push('--headed');
  if (opts.tc) args.push('-g', opts.tc);
  else if (retryFilter) args.push('-g', retryFilter);

  const execution = spawnSync(runner.bin, args, { cwd: e2eDir, encoding: 'utf8', env });
  const runnerExitCode = (typeof execution.status === 'number' && execution.status >= 0) ? execution.status : 1;

  let parsed;
  let summary;
  let reportError = '';
  let runReportSummary = null;

  try {
    parsed = parsePlaywrightReport(reportPath);

    if (!parsed.reportValid) {
      summary = { passed: 0, failed: 1, pending: 0 };
      reportError = parsed.error;
    } else {
      summary = summarizeResults(parsed.results);
      const reportedTotal = Number(parsed.stats?.total || 0);
      const summarizedTotal = summary.passed + summary.failed + summary.pending;

      if (reportedTotal > 0 && summarizedTotal === 0) {
        summary.failed = 1;
        reportError = 'report có test nhưng không có CHK-ID/status parse được';
      } else if (runnerExitCode !== 0 && summarizedTotal === 0) {
        summary.failed = 1;
        reportError = 'runner lỗi trước khi tạo kết quả test';
      }

      updateIndexResults(e2eDir, feature, parsed.results);

      const history = loadRunHistory(e2eDir);
      const runReport = buildRunReport(e2eDir, feature, parsed, history, { oracles: loadOracles(dir) });
      writeRunReport(e2eDir, feature, runReport, summary, origin);
      saveRunHistory(e2eDir, updateRunHistory(history, parsed.results, runReport.fingerprint));

      const at = new Date().toISOString();
      writeNormalizedResults(dir, runReport.rows.map((r) => ({
        chk: r.chk,
        target: 'web',
        status: r.category,
        env: qaEnv || origin,
        build: env.QA_BUILD || '',
        at,
        note: r.note,
      })));
      runReportSummary = runReport;
    }
  } finally {
    cleanupRunArtifacts(e2eDir);
  }

  if (parsed?.setupFailures?.length) {
    console.log(`🔑 Đăng nhập vai lỗi: ${[...new Set(parsed.setupFailures)].join(', ')} → TC phụ thuộc bị skip (PENDING). Kiểm tài khoản trong qa/.env.`);
  }

  const navigationPending = parsed?.reportValid
    ? [...parsed.results.values()].filter((status) => status === 'PENDING').length
    : 0;
  if (navigationPending > 0) {
    console.log(`⏳ ${navigationPending} test PENDING/skipped; lỗi navigation được phân loại riêng theo từng test.`);
  }
  if (reportError) console.error(`❌ Runner/report error: ${reportError}`);

  const finalExitCode = runnerExitCode !== 0 ? runnerExitCode : summary.failed > 0 ? 1 : 0;
  process.exitCode = finalExitCode;

  if (runReportSummary) {
    const cnt = (cat) => runReportSummary.rows.filter((r) => r.category === cat).length;
    console.log(
      `Run: ✅${summary.passed} 🔴${cnt('FAIL_APP')} nghi-app 🟣${cnt('FAIL_DOC')} nghi-tài-liệu `
      + `🟡${cnt('FAIL_DATA')} nghi-data 🟠${cnt('FAIL_OUTDATE')} nghi-outdate ⏳${summary.pending} (exit ${finalExitCode})`,
    );
    const dataWork = runReportSummary.gaps.stillDefault.length + runReportSummary.gaps.missing.length;
    if (dataWork > 0 || cnt('FAIL_DATA') > 0 || cnt('FAIL_OUTDATE') > 0) {
      console.log(
        `📄 Xem ${path.join('docs', feature, 'test', 'e2e', 'run-report.md')} — có ${dataWork} data cần bổ sung. `
        + 'Cấp data thật vào testdata.json rồi chạy lại với --retry-failed.',
      );
    }
    console.log(`🧾 Kết quả chuẩn hoá: ${path.join('docs', feature, 'test', 'results', 'latest.json')}`);
  } else {
    console.log(`Run: ✅${summary.passed} ❌${summary.failed} ⏳${summary.pending} (exit ${finalExitCode})`);
  }

  return summary;
}

// ---------------------------------------------------------------- CLI (chỉ khi chạy trực tiếp)

const isMain = Boolean(process.argv[1]) && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMain) {
  const { cmd, opts } = parseArgs(process.argv);
  try {
    if (cmd === 'gen') gen(opts);
    else if (cmd === 'run') run(opts);
    else if (cmd !== '--selftest') fail(`lệnh không hợp lệ: ${cmd || '(trống)'}. Dùng: gen | run`);
  } catch (err) {
    console.error(`❌ playwright-gen: ${err instanceof CliError ? err.message : (err?.stack || err)}`);
    process.exit(1);
  }
}

export {
  CliError,
  parseArgs,
  parseTestcasesFile,
  analyzeTestcase,
  isCodegenReady,
  actionToCode,
  expectedToCode,
  tcToSpec,
  dataToExpression,
  writeTestData,
  classifyFailure,
  detectDataGaps,
  dataFingerprint,
  buildRunReport,
  writeRunReport,
  parsePlaywrightReport,
  collectCodegenReport,
  gen,
  run,
  CHK_PATTERN,
};
