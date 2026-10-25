// testgen-core.mjs — thư viện dùng chung cho 3 máy sinh test (import-safe: KHÔNG side effect lúc import).
//
//   playwright-gen.mjs (web, Target web) · bruno-runner.mjs (API, Target api) · maestro-gen.mjs (app, Target mob)
//
// Hợp đồng định dạng: BRIEF đợt 1 + .claude/rules/test-trace.md. Mọi hàm ở đây là pure hoặc chỉ đọc/ghi
// đúng file được truyền vào; KHÔNG process.exit (lỗi = throw Error để caller tự xử).
//
// ── API XUẤT (giữ ổn định — maestro-gen/bruno-runner/playwright-gen import theo tên) ─────────────────────
// Hằng:       FIELD_PATTERN, CHK_PATTERN, SLUG_PATTERN, QUOTED_CAPTURE, CHECKLIST_LINE_PATTERN,
//             TARGETS ('web'|'mob'|'api'), RESULT_STATUSES, DOC_SUSPECT_ORACLES
// Chuỗi:      cleanValue, appendValue, normalizeVietnamese, isDash, hasTBD, escapeRegExp, tsString,
//             inlineComment, addUniqueReason, addParseError, isValidSlug, requireSlug (throw),
//             firstQuotedCapture, extractQuoted, extractAllQuoted, dataKeySlug, today, nowIso
// Test case:  splitTestcaseBlocks(md), parseTestcasesFile(md) → [tc]
//               tc = { stt, category, subcategory, checklist, ref, priority, title, description, auto,
//                      target ('' khi thiếu), role, data, preconditions, steps:[{n,action,expected,testData}],
//                      chk, retired, parseErrors }
//             normalizeTarget(v) → 'web'|'mob'|'api'|'' · tcTarget(tc) → mặc định 'web'
//             parsePreconditions(text) → { empty, tbd, onlyRoleData, setupRequired, roles[], dataKeys[], lines[] }
//             resolveRole(tc) → slug|'' (field Role, else dòng ROLE: trong Preconditions)
//             resolveDataKeys(tc) → [key] (field Data ∪ dòng DATA:)
//             readinessReasons(tc, { roles }) → [lý do chưa sẵn sàng chung cho mọi target]
//             loadTestcaseDir(tcDir) → { files, entries:[{scope, file, tc}] } (gắn lỗi CHK trùng toàn workspace)
// Checklist:  parseChecklistLine(line) → null | { priority, auto, chk, refs[], text, channels[], channel, oracle,
//                                               oracleKind, oracleCode }
//             parseChecklistFile(md), loadChecklistIndex(testDir) → Map(chkLower → item)
//             oracleKind(label) → 'srs'|'chg'|'reverse'|'code'|'legacy-uc'|'other'|''
//             tcOracle(tc, index?) → { label, kind } (checklist index trước, rồi tail [đáp án: …] trong Checklist)
//             isDocSuspectOracle(labelOrKind) → bool (UC cũ / tái lập)
// Testdata:   mergeTestData(existing, defaultsMap) → object (giữ giá trị user), writeTestData(dir, defaultsMap),
//             detectDataGaps(dir) → { stillDefault[], missing[], defaults, current }, dataFingerprint(obj),
//             readJsonSafe(path, fallback)
// Lịch sử:    loadRunHistory(dir), saveRunHistory(dir, h), updateRunHistory(h, Map|obj chk→status, fingerprint)
// Phân loại:  classifyFailure(errorText) → 'data'|'app' (marker @data-step/@assert-step trước, wording sau)
//             classifyResult({ status:'PASS'|'FAIL'|'PENDING', kind, oracle, prev, fingerprint })
//               → { status: PASS|FAIL_APP|FAIL_DATA|FAIL_OUTDATE|FAIL_DOC|PENDING, note }
//               FAIL_DOC = rớt ở assertion nghiệp vụ (kind 'app') VÀ nhãn đáp án là `UC cũ`/`tái lập`.
// Kết quả:    resultsPath(testDir), readNormalizedResults(testDir), makeResultEntry({...}),
//             writeNormalizedResults(testDir, entries) — merge theo (chk, target), ghi
//             {testDir}/results/latest.json = [{chk, target, status, env, build, at, note}]
// Cổng:       safeOrigin, isLocalOrigin, loadAllowedOrigins(dir), isProdEnvName(name),
//             findRepoRoot(startDir), loadQaConfig(repoRoot) → { qaDir, envs, roles, found },
//             knownNonProdOrigins(envs) → Set, checkOriginGate({ origin, allowlist, allowProd, confirmProd })
//               → { ok, prod, message }
// Env:        loadDotEnv(path) → object (không ghi process.env), loadEnvLayers(paths[]) (file sau đè file trước)
// ────────────────────────────────────────────────────────────────────────────────────────────────────────────

import fs from 'node:fs';
import path from 'node:path';

// ---------------------------------------------------------------- hằng

export const FIELD_PATTERN = /^\s*\*\*(STT|Category|Sub-Category|Checklist|Ref|Priority|Title|Description|Auto|Target|Role|Data|Preconditions|Step|Action|Expected|Test Data):\*\*\s*(.*)$/i;
export const CHK_PATTERN = /\bCHK-[a-z0-9][a-z0-9-]*-\d{3,}\b/gi;
export const SLUG_PATTERN = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
export const QUOTED_CAPTURE = "(?:\"([^\"\\n]+)\"|“([^”\\n]+)”|'([^'\\n]+)'|‘([^’\\n]+)’|«([^»\\n]+)»)";
// ĐẦU dòng checklist = đúng regex KG (kg-build.mjs, test_checklist_item). Phần đuôi (@kênh, [đáp án: …])
// nằm trong nhóm nội dung (.+) nên KG vẫn đọc được; core tách đuôi ra sau.
export const CHECKLIST_LINE_PATTERN = /^\s*\[([1-4])\]\s*\[(Yes|No)\]\s*(CHK-[a-z0-9][a-z0-9-]*-\d{3,})\s*→\s*(—|[^·]+?)\s*·\s*(.+)$/i;
export const TARGETS = ['web', 'mob', 'api'];
export const RESULT_STATUSES = ['PASS', 'FAIL_APP', 'FAIL_DATA', 'FAIL_OUTDATE', 'FAIL_DOC', 'PENDING'];
export const DOC_SUSPECT_ORACLES = ['reverse', 'legacy-uc'];

// ---------------------------------------------------------------- chuỗi

export function cleanValue(value) {
  return String(value ?? '')
    .replace(/\r\n/g, '\n')
    .replace(/\r/g, '\n')
    .replace(/[ \t]+\n/g, '\n')
    .trim();
}

export function appendValue(previous, continuation) {
  const next = String(continuation ?? '').trimEnd();
  if (!previous) return next.trim();
  if (!next) return previous;
  return `${previous}\n${next}`.trim();
}

export function normalizeVietnamese(value) {
  return String(value ?? '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'D')
    .toLowerCase();
}

export function isDash(value) {
  return /^(?:—|–|-|n\/a|na)$/i.test(cleanValue(value));
}

export function hasTBD(value) {
  return /\bTBD\b/i.test(String(value ?? ''));
}

export function escapeRegExp(value) {
  return String(value ?? '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

export function tsString(value) {
  return JSON.stringify(String(value ?? ''));
}

export function inlineComment(value) {
  return String(value ?? '')
    .replace(/[\r\n\u2028\u2029]+/g, ' ')
    .replace(/\*\//g, '*∕')
    .trim();
}

export function addUniqueReason(reasons, reason) {
  const value = cleanValue(reason);
  if (value && !reasons.includes(value)) reasons.push(value);
}

export function addParseError(tc, reason) {
  if (!Array.isArray(tc.parseErrors)) tc.parseErrors = [];
  addUniqueReason(tc.parseErrors, reason);
}

export function isValidSlug(value) {
  return SLUG_PATTERN.test(String(value ?? ''));
}

export function requireSlug(value, label) {
  const slug = String(value ?? '');
  if (!isValidSlug(slug)) {
    throw new Error(
      `${label} không hợp lệ: chỉ chấp nhận kebab-case chữ thường ([a-z0-9]+, phân cách bằng dấu "-")`,
    );
  }
  return slug;
}

export function firstQuotedCapture(match) {
  if (!match) return null;
  for (const capture of match.slice(1)) {
    if (capture?.trim()) return capture.trim();
  }
  return null;
}

export function extractQuoted(text) {
  const match = String(text ?? '').match(new RegExp(QUOTED_CAPTURE));
  return firstQuotedCapture(match);
}

export function extractAllQuoted(text) {
  const out = [];
  for (const match of String(text ?? '').matchAll(new RegExp(QUOTED_CAPTURE, 'g'))) {
    const value = firstQuotedCapture(match);
    if (value && !out.includes(value)) out.push(value);
  }
  return out;
}

// Chuẩn hoá 1 mảnh key ổn định (testdata.json): CHK-ID + step + nhãn field.
export function dataKeySlug(s) {
  return String(s || 'value')
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/đ/g, 'd').replace(/Đ/g, 'D')
    .toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'value';
}

export function today() {
  return new Date().toISOString().slice(0, 10);
}

export function nowIso() {
  return new Date().toISOString();
}

// ---------------------------------------------------------------- test case

const MULTILINE_FIELD_NAMES = ['description', 'preconditions', 'action', 'expected', 'test data'];

export function splitTestcaseBlocks(md) {
  const source = String(md ?? '').replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  const lines = source.split('\n');
  const blocks = [];
  let current = [];
  let activeMultiline = false;

  const flush = () => {
    const block = current.join('\n').trim();
    if (block) blocks.push(block);
    current = [];
    activeMultiline = false;
  };

  for (let index = 0; index < lines.length; index += 1) {
    const rawLine = lines[index];

    // Escape cho trường hợp mơ hồ: `\---` luôn là nội dung literal "---".
    const escapedDelimiter = rawLine.match(/^(\s*)\\---\s*$/);
    if (escapedDelimiter) {
      current.push(`${escapedDelimiter[1]}---`);
      continue;
    }

    if (/^\s*---\s*$/.test(rawLine)) {
      let nextNonEmpty = '';
      for (let lookahead = index + 1; lookahead < lines.length; lookahead += 1) {
        if (lines[lookahead].trim()) {
          nextNonEmpty = lines[lookahead];
          break;
        }
      }
      const nextField = nextNonEmpty.match(FIELD_PATTERN);
      const nextStartsTestcase = nextField?.[1]?.toLowerCase() === 'stt';
      const atEnd = !nextNonEmpty;

      // Đang ở multiline: "---" là nội dung trừ khi nó mở testcase mới hoặc là delimiter cuối file.
      if (!current.length || !activeMultiline || nextStartsTestcase || atEnd) flush();
      else current.push(rawLine);
      continue;
    }

    const fieldMatch = rawLine.match(FIELD_PATTERN);
    if (fieldMatch) {
      activeMultiline = MULTILINE_FIELD_NAMES.includes(fieldMatch[1].toLowerCase());
    }
    current.push(rawLine);
  }

  flush();
  return blocks;
}

const FIELD_MAP = new Map([
  ['stt', 'stt'],
  ['category', 'category'],
  ['sub-category', 'subcategory'],
  ['checklist', 'checklist'],
  ['ref', 'ref'],
  ['priority', 'priority'],
  ['title', 'title'],
  ['description', 'description'],
  ['auto', 'auto'],
  ['target', 'target'],
  ['role', 'role'],
  ['data', 'data'],
  ['preconditions', 'preconditions'],
  ['step', 'step'],
  ['action', 'action'],
  ['expected', 'expected'],
  ['test data', 'testData'],
]);
const MULTILINE_FIELDS = new Set(['description', 'preconditions', 'action', 'expected', 'testData']);
const STEP_FIELDS = new Set(['action', 'expected', 'testData']);

export function normalizeTarget(value) {
  const v = normalizeVietnamese(cleanValue(value)).replace(/^@/, '');
  if (!v || isDash(v)) return '';
  if (/^(web|playwright|browser)$/.test(v)) return 'web';
  if (/^(mob|mobile|app|maestro)$/.test(v)) return 'mob';
  if (/^(api|bruno|be|backend)$/.test(v)) return 'api';
  return v;
}

export function parseTestcasesFile(md) {
  const blocks = splitTestcaseBlocks(md);
  const testcases = [];

  for (const block of blocks) {
    const hasStt = /^\s*\*\*STT:\*\*/im.test(block);
    const hasChecklist = /^\s*\*\*Checklist:\*\*/im.test(block);
    if (!hasStt || !hasChecklist) continue;

    const tc = {
      stt: '',
      category: '',
      subcategory: '',
      checklist: '',
      ref: '',
      priority: '',
      title: '',
      description: '',
      auto: '',
      target: '',
      role: '',
      data: '',
      preconditions: '',
      steps: [],
      chk: null,
      retired: false,
      parseErrors: [],
    };

    const seenTopLevelFields = new Set();
    let activeTarget = null;
    let currentStep = null;
    let currentStepFields = null;

    for (const rawLine of block.split('\n')) {
      const fieldMatch = rawLine.match(FIELD_PATTERN);

      if (fieldMatch) {
        const fieldName = fieldMatch[1].toLowerCase();
        const value = fieldMatch[2] ?? '';
        const mapped = FIELD_MAP.get(fieldName);
        activeTarget = null;

        if (mapped === 'step') {
          currentStep = { n: cleanValue(value), action: '', expected: '', testData: '' };
          currentStepFields = new Set();
          tc.steps.push(currentStep);
          continue;
        }

        if (STEP_FIELDS.has(mapped)) {
          if (!currentStep || !currentStepFields) {
            addParseError(tc, `${fieldMatch[1]} xuất hiện trước Step`);
            continue;
          }
          if (currentStepFields.has(mapped)) {
            addParseError(tc, `field ${fieldMatch[1]} bị lặp trong step ${currentStep.n || '?'}`);
            continue;
          }
          currentStepFields.add(mapped);
          currentStep[mapped] = cleanValue(value);
          activeTarget = { object: currentStep, key: mapped };
          continue;
        }

        if (!mapped) continue;

        if (seenTopLevelFields.has(mapped)) {
          addParseError(tc, `field ${fieldMatch[1]} bị lặp`);
          continue;
        }

        seenTopLevelFields.add(mapped);
        tc[mapped] = cleanValue(value);
        if (MULTILINE_FIELDS.has(mapped)) activeTarget = { object: tc, key: mapped };
        continue;
      }

      if (!activeTarget) continue;

      const continuation = rawLine.trim();
      if (!continuation) {
        if (activeTarget.object[activeTarget.key]) {
          activeTarget.object[activeTarget.key] = `${activeTarget.object[activeTarget.key]}\n`;
        }
        continue;
      }
      activeTarget.object[activeTarget.key] = appendValue(activeTarget.object[activeTarget.key], continuation);
    }

    tc.description = cleanValue(tc.description);
    tc.preconditions = cleanValue(tc.preconditions);
    tc.role = cleanValue(tc.role);
    tc.data = cleanValue(tc.data);

    const rawTarget = cleanValue(tc.target);
    tc.target = normalizeTarget(rawTarget);
    if (rawTarget && !isDash(rawTarget) && !TARGETS.includes(tc.target)) {
      addParseError(tc, `Target không hợp lệ: ${JSON.stringify(rawTarget)} (chỉ web|mob|api)`);
    }

    for (const step of tc.steps) {
      step.n = cleanValue(step.n);
      step.action = cleanValue(step.action);
      step.expected = cleanValue(step.expected);
      step.testData = cleanValue(step.testData);
    }

    const checklist = cleanValue(tc.checklist);
    const chkMatches = [...checklist.matchAll(CHK_PATTERN)].map((match) => match[0]);
    if (chkMatches.length === 1) {
      tc.chk = chkMatches[0];
    } else if (chkMatches.length > 1) {
      tc.chk = chkMatches[0];
      addParseError(tc, 'Checklist chứa nhiều CHK-ID');
    }

    tc.retired = Boolean(
      tc.chk
      && new RegExp(`${escapeRegExp(tc.chk)}\\s*\\(\\s*retired\\s*\\)`, 'i').test(checklist),
    );

    testcases.push(tc);
  }

  const chkGroups = new Map();
  for (const tc of testcases) {
    if (!tc.chk) continue;
    const key = tc.chk.toLowerCase();
    if (!chkGroups.has(key)) chkGroups.set(key, []);
    chkGroups.get(key).push(tc);
  }
  for (const duplicates of chkGroups.values()) {
    if (duplicates.length < 2) continue;
    for (const tc of duplicates) addParseError(tc, `CHK-ID trùng: ${tc.chk}`);
  }

  return testcases;
}

export function tcTarget(tc) {
  return normalizeTarget(tc?.target) || 'web';
}

export function parsePreconditions(text) {
  const value = cleanValue(text);
  const result = {
    empty: !value || isDash(value),
    tbd: hasTBD(value),
    onlyRoleData: false,
    setupRequired: false,
    roles: [],
    dataKeys: [],
    lines: [],
  };
  if (result.empty) return result;

  const lines = value.split('\n').map((l) => l.trim().replace(/^[-*•]\s+/, '')).filter(Boolean);
  result.lines = lines;
  let allRoleData = true;

  for (const line of lines) {
    if (isDash(line)) continue;
    const m = line.match(/^(ROLE|DATA)\s*:\s*(.+)$/i);
    if (!m) {
      allRoleData = false;
      continue;
    }
    const items = m[2].split(',').map((s) => s.trim()).filter(Boolean);
    const bucket = m[1].toUpperCase() === 'ROLE' ? result.roles : result.dataKeys;
    for (const item of items) if (!bucket.includes(item)) bucket.push(item);
  }

  result.onlyRoleData = allRoleData;
  result.setupRequired = !result.tbd && !allRoleData;
  return result;
}

export function resolveRole(tc) {
  const field = cleanValue(tc?.role);
  if (field && !isDash(field)) return field;
  return parsePreconditions(tc?.preconditions).roles[0] || '';
}

export function resolveDataKeys(tc) {
  const keys = [];
  const field = cleanValue(tc?.data);
  if (field && !isDash(field)) {
    for (const k of field.split(',').map((s) => s.trim()).filter(Boolean)) if (!keys.includes(k)) keys.push(k);
  }
  for (const k of parsePreconditions(tc?.preconditions).dataKeys) if (!keys.includes(k)) keys.push(k);
  return keys;
}

// Lý do chưa sẵn sàng dùng chung cho mọi target (không gồm mapping từng step — việc riêng của generator).
// opts.roles: object roles.json (khi có) để kiểm Role tồn tại.
export function readinessReasons(tc, opts = {}) {
  const reasons = [];
  if (!tc || typeof tc !== 'object') return ['test case không hợp lệ'];

  for (const parseError of tc.parseErrors || []) addUniqueReason(reasons, parseError);
  if (!tc.chk) addUniqueReason(reasons, 'thiếu CHK-ID — chạy /test-cases update để ổn định trace');
  if (cleanValue(tc.auto).toLowerCase() !== 'yes') addUniqueReason(reasons, 'Auto không phải Yes (manual/chưa-ready)');
  if (tc.retired) addUniqueReason(reasons, 'retired');

  const pre = parsePreconditions(tc.preconditions);
  if (pre.tbd) {
    addUniqueReason(reasons, 'Preconditions TBD (not-ready)');
  } else if (pre.setupRequired) {
    // Preconditions có state (kể cả `(dựng: ...)`) = setup-required → KHÔNG auto-run (tránh FAIL giả).
    // Chỉ gồm ROLE:/DATA: hoặc — thì engine tự lo (đăng nhập theo vai, dữ liệu có tên) → không chặn.
    addUniqueReason(reasons, 'setup-required — cần dựng state trước (fixture/seed), KHÔNG auto-run tránh FAIL giả');
  }

  const role = resolveRole(tc);
  if (role && opts.roles && typeof opts.roles === 'object' && !Object.prototype.hasOwnProperty.call(opts.roles, role)) {
    addUniqueReason(reasons, `Role "${role}" không có trong qa/config/roles.json`);
  }

  const steps = Array.isArray(tc.steps) ? tc.steps : [];
  if (!steps.length) addUniqueReason(reasons, 'không có step');
  for (const step of steps) {
    const stepNo = cleanValue(step?.n) || '?';
    if (hasTBD(step?.expected)) addUniqueReason(reasons, `Expected TBD (step ${stepNo})`);
    if (hasTBD(step?.testData)) addUniqueReason(reasons, `Test Data TBD (step ${stepNo})`);
  }
  return reasons;
}

// Đọc mọi testcases-*.md trong tcDir; gắn lỗi CHK trùng toàn workspace (giữa các file).
export function loadTestcaseDir(tcDir) {
  const files = fs.readdirSync(tcDir)
    .filter((file) => /^testcases-.*\.md$/i.test(file))
    .sort((a, b) => a.localeCompare(b));
  const entries = [];

  for (const file of files) {
    const scope = file.replace(/^testcases-/i, '').replace(/\.md$/i, '');
    requireSlug(scope, `scope từ ${file}`);
    for (const tc of parseTestcasesFile(fs.readFileSync(path.join(tcDir, file), 'utf8'))) {
      entries.push({ scope, file, tc });
    }
  }

  const groups = new Map();
  for (const entry of entries) {
    if (!entry.tc.chk) continue;
    const key = entry.tc.chk.toLowerCase();
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(entry);
  }
  for (const dup of groups.values()) {
    if (dup.length < 2) continue;
    for (const entry of dup) addParseError(entry.tc, `CHK-ID trùng trong workspace: ${entry.tc.chk}`);
  }
  return { files, entries };
}

// ---------------------------------------------------------------- checklist

export function oracleKind(label) {
  const v = normalizeVietnamese(cleanValue(label));
  if (!v) return '';
  if (/^srs\b/.test(v)) return 'srs';
  if (/^chg-/.test(v)) return 'chg';
  if (/^tai lap\b/.test(v)) return 'reverse';
  if (/^code\b/.test(v)) return 'code';
  if (/^uc cu\b/.test(v)) return 'legacy-uc';
  return 'other';
}

export function isDocSuspectOracle(labelOrKind) {
  const v = String(labelOrKind ?? '');
  const kind = DOC_SUSPECT_ORACLES.includes(v) ? v : oracleKind(v);
  return DOC_SUSPECT_ORACLES.includes(kind);
}

// Tách đuôi `@web|@mob|@api` và `[đáp án: …]` khỏi nội dung (cả 2 thứ tự).
function splitChecklistTail(text) {
  let rest = String(text ?? '').trim();
  const channels = [];
  let oracle = '';
  for (let guard = 0; guard < 8; guard += 1) {
    const o = rest.match(/\s*\[\s*đáp án\s*:\s*([^\]]+)\]\s*$/iu)
      || rest.match(/\s*\[\s*dap an\s*:\s*([^\]]+)\]\s*$/i);
    if (o) {
      if (!oracle) oracle = o[1].trim();
      rest = rest.slice(0, o.index).trim();
      continue;
    }
    const c = rest.match(/(?:^|\s)@(web|mob|api)\s*$/i);
    if (c) {
      channels.unshift(c[1].toLowerCase());
      rest = rest.slice(0, c.index).trim();
      continue;
    }
    break;
  }
  return { text: rest, channels: [...new Set(channels)], oracle };
}

export function parseChecklistLine(line) {
  const m = String(line ?? '').match(CHECKLIST_LINE_PATTERN);
  if (!m) return null;
  const refs = m[4].trim() === '—'
    ? []
    : m[4].split(',').map((s) => s.trim()).filter(Boolean);
  const tail = splitChecklistTail(m[5]);
  const kind = oracleKind(tail.oracle);
  const codeMatch = kind === 'code' ? tail.oracle.match(/[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-AC-\d+/) : null;
  return {
    priority: m[1],
    auto: m[2],
    chk: m[3],
    refs,
    text: tail.text,
    channels: tail.channels,
    channel: tail.channels[0] || 'web',
    oracle: tail.oracle,
    oracleKind: kind,
    oracleCode: codeMatch ? codeMatch[0] : '',
  };
}

export function parseChecklistFile(md) {
  const items = [];
  for (const line of String(md ?? '').split(/\r?\n/)) {
    const item = parseChecklistLine(line);
    if (item) items.push(item);
  }
  return items;
}

// testDir = docs/{feature}/test → đọc test/checklist/*.md. Không có thư mục → Map rỗng.
export function loadChecklistIndex(testDir) {
  const index = new Map();
  const dir = path.join(testDir, 'checklist');
  if (!fs.existsSync(dir) || !fs.statSync(dir).isDirectory()) return index;
  for (const file of fs.readdirSync(dir).filter((f) => f.endsWith('.md')).sort()) {
    for (const item of parseChecklistFile(fs.readFileSync(path.join(dir, file), 'utf8'))) {
      index.set(item.chk.toLowerCase(), { ...item, file });
    }
  }
  return index;
}

export function tcOracle(tc, index) {
  if (tc?.chk && index instanceof Map) {
    const item = index.get(tc.chk.toLowerCase());
    if (item?.oracle) return { label: item.oracle, kind: item.oracleKind };
  }
  const tail = splitChecklistTail(cleanValue(tc?.checklist).replace(/\n/g, ' '));
  return { label: tail.oracle, kind: oracleKind(tail.oracle) };
}

// ---------------------------------------------------------------- testdata

export function readJsonSafe(p, fallback) {
  try {
    if (!fs.existsSync(p)) return fallback;
    const v = JSON.parse(fs.readFileSync(p, 'utf8'));
    return v ?? fallback;
  } catch {
    return fallback;
  }
}

function toEntries(mapOrObj) {
  if (mapOrObj instanceof Map) return [...mapOrObj.entries()];
  return Object.entries(mapOrObj || {});
}

// Giữ giá trị user đã sửa; key mới lấy default; key user tự thêm giữ lại; sort key.
export function mergeTestData(existing, defaults) {
  const merged = {};
  const ex = existing || {};
  for (const [key, def] of toEntries(defaults)) {
    merged[key] = Object.prototype.hasOwnProperty.call(ex, key) ? ex[key] : def;
  }
  for (const [key, val] of Object.entries(ex)) if (!(key in merged)) merged[key] = val;
  const sorted = {};
  for (const key of Object.keys(merged).sort()) sorted[key] = merged[key];
  return sorted;
}

// Ghi testdata.json (merge) + testdata.defaults.json (máy đọc). testdata.json JSON lỗi → sao lưu .bak + throw.
export function writeTestData(dir, dataDefaults) {
  const p = path.join(dir, 'testdata.json');
  let existing = {};
  if (fs.existsSync(p)) {
    const raw = fs.readFileSync(p, 'utf8');
    try {
      existing = JSON.parse(raw) || {};
    } catch (err) {
      const bak = `${p}.bak`;
      try { fs.writeFileSync(bak, raw, 'utf8'); } catch { /* best-effort */ }
      throw new Error(
        `testdata.json không đọc được (JSON lỗi: ${err.message}). `
        + `Đã sao lưu bản hiện tại vào ${path.relative(process.cwd(), bak)}. `
        + `Sửa lại cú pháp JSON trong ${path.relative(process.cwd(), p)} rồi chạy lại — `
        + 'KHÔNG tự ghi đè để tránh mất data thật anh đã điền.',
      );
    }
  }
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(p, `${JSON.stringify(mergeTestData(existing, dataDefaults), null, 2)}\n`, 'utf8');

  const defaults = {};
  for (const [key, def] of toEntries(dataDefaults).sort(([a], [b]) => a.localeCompare(b))) defaults[key] = def;
  fs.writeFileSync(path.join(dir, 'testdata.defaults.json'), `${JSON.stringify(defaults, null, 2)}\n`, 'utf8');
}

export function detectDataGaps(dir) {
  const stillDefault = [];
  const missing = [];
  const dp = path.join(dir, 'testdata.defaults.json');
  const tp = path.join(dir, 'testdata.json');
  if (!fs.existsSync(dp)) return { stillDefault, missing, defaults: {}, current: {} };
  const defaults = readJsonSafe(dp, {}) || {};
  const current = readJsonSafe(tp, {}) || {};
  for (const [key, def] of Object.entries(defaults)) {
    if (!Object.prototype.hasOwnProperty.call(current, key)) missing.push(key);
    else if (current[key] === def) stillDefault.push({ key, value: def });
  }
  return { stillDefault, missing, defaults, current };
}

export function dataFingerprint(current) {
  const keys = Object.keys(current || {}).sort();
  return keys.map((k) => `${k}=${current[k]}`).join('|');
}

// ---------------------------------------------------------------- lịch sử chạy

export function loadRunHistory(dir) {
  return readJsonSafe(path.join(dir, 'run-history.json'), {}) || {};
}

export function saveRunHistory(dir, history) {
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'run-history.json'), `${JSON.stringify(history, null, 2)}\n`, 'utf8');
}

// Cập nhật CHỈ case vừa chạy (retry chỉ chạy 1 phần → giữ phần cũ). status 'PASS' ghi mốc + fingerprint lúc PASS.
export function updateRunHistory(history, results, fingerprint) {
  const h = history || {};
  for (const [chk, status] of toEntries(results)) {
    const prev = h[chk] || {};
    const pass = status === 'PASS';
    h[chk] = {
      lastStatus: status,
      lastRun: today(),
      fingerprint,
      lastPass: pass ? today() : (prev.lastPass || ''),
      passFingerprint: pass ? fingerprint : (prev.passFingerprint || ''),
    };
  }
  return h;
}

// ---------------------------------------------------------------- phân loại

// 'data' (nghi-data: fail ở bước nhập data/navigation/auth) | 'app' (assertion nghiệp vụ). Chỉ là NGHI.
export function classifyFailure(errorText) {
  const text = String(errorText || '');
  if (!text) return 'app';
  const hasDataMarker = text.includes('@data-step');
  const hasAssertMarker = text.includes('@assert-step');
  if (hasAssertMarker && !hasDataMarker) return 'app';
  if (hasDataMarker && !hasAssertMarker) return 'data';
  if (/\bexpect\(|toBeVisible|toBeHidden|toHaveURL|toHaveText|Expected:.*Received:/s.test(text)) return 'app';
  if (/locator\.fill|getByLabel|getByRole|getByPlaceholder|page\.goto|Timeout.*waiting for|không t[oồ]n t[aạ]i|sai m[aậ]t kh[aẩ]u|invalid credential|user not found|unauthor/i.test(text)) {
    return 'data';
  }
  return 'app';
}

// status thô PASS|FAIL|PENDING (+ kind data/app, nhãn đáp án, lịch sử) → trạng thái chuẩn hoá.
export function classifyResult({ status, kind = 'app', oracle = '', prev = null, fingerprint = '' } = {}) {
  const raw = String(status || '').toUpperCase();
  if (raw === 'PASS') return { status: 'PASS', note: '' };
  if (raw !== 'FAIL') return { status: 'PENDING', note: 'chưa chạy được (env/skip/setup-required)' };

  if (kind === 'data') {
    if (prev && prev.lastPass && prev.passFingerprint && prev.passFingerprint === fingerprint) {
      return {
        status: 'FAIL_OUTDATE',
        note: `từng PASS (${prev.lastPass}) với cùng data — data có thể đã outdate (vd account bị đổi)`,
      };
    }
    return { status: 'FAIL_DATA', note: 'fail ở bước nhập data/navigation/auth — kiểm data test trước khi báo dev' };
  }

  const label = typeof oracle === 'object' && oracle ? (oracle.label || oracle.kind || '') : String(oracle || '');
  if (label && isDocSuspectOracle(label)) {
    return {
      status: 'FAIL_DOC',
      note: `rớt ở assertion nhưng đáp án là "${label}" (chưa chốt) — nghi lệch tài liệu → OQ, chưa báo dev`,
    };
  }
  return { status: 'FAIL_APP', note: 'fail ở assertion nghiệp vụ — nghi app bug, cần dev xem' };
}

// ---------------------------------------------------------------- kết quả chuẩn hoá

export function resultsPath(testDir) {
  return path.join(testDir, 'results', 'latest.json');
}

export function readNormalizedResults(testDir) {
  const v = readJsonSafe(resultsPath(testDir), []);
  return Array.isArray(v) ? v : [];
}

export function makeResultEntry({ chk, target, status, env = '', build = '', at = '', note = '' } = {}) {
  const st = RESULT_STATUSES.includes(status) ? status : 'PENDING';
  return {
    chk: String(chk || ''),
    target: normalizeTarget(target) || 'web',
    status: st,
    env: String(env || ''),
    build: String(build || ''),
    at: at || nowIso(),
    note: String(note || ''),
  };
}

// Merge theo (chk, target): entry mới thay entry cũ cùng khoá, khoá khác giữ nguyên. Sort chk rồi target.
export function writeNormalizedResults(testDir, entries) {
  const current = readNormalizedResults(testDir);
  const key = (e) => `${String(e.chk).toLowerCase()}|${e.target}`;
  const map = new Map(current.map((e) => [key(e), e]));
  for (const raw of entries || []) {
    const e = makeResultEntry(raw);
    if (!e.chk) continue;
    map.set(key(e), e);
  }
  const out = [...map.values()].sort((a, b) => (
    a.chk.localeCompare(b.chk) || String(a.target).localeCompare(String(b.target))
  ));
  const p = resultsPath(testDir);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, `${JSON.stringify(out, null, 2)}\n`, 'utf8');
  return out;
}

// ---------------------------------------------------------------- cổng môi trường

// origin an toàn để log/so sánh: scheme://host[:port], BỎ credential/path/query.
export function safeOrigin(url) {
  try {
    const u = new URL(String(url));
    return `${u.protocol}//${u.host}`;
  } catch {
    return '';
  }
}

export function isLocalOrigin(origin) {
  return /^(https?:\/\/)?(localhost|127\.0\.0\.1|\[::1\]|[^/]*\.(local|test|localhost))(:\d+)?$/i.test(String(origin || ''));
}

export function loadAllowedOrigins(dir) {
  const p = path.join(dir, '.allowed-origins');
  const set = new Set();
  if (!fs.existsSync(p)) return set;
  for (const raw of fs.readFileSync(p, 'utf8').split('\n')) {
    const line = raw.trim();
    if (!line || line.startsWith('#')) continue;
    const o = safeOrigin(line) || line;
    if (o) set.add(o);
  }
  return set;
}

export function isProdEnvName(name) {
  return /^(prod|production|live|prd)$/i.test(String(name || '').trim());
}

// Đi lên từ startDir tới thư mục có qa/config hoặc .git (repo/worktree root).
export function findRepoRoot(startDir) {
  let d = path.resolve(startDir || process.cwd());
  for (;;) {
    if (fs.existsSync(path.join(d, 'qa', 'config'))) return d;
    if (fs.existsSync(path.join(d, '.git'))) return d;
    const up = path.dirname(d);
    if (up === d) return path.resolve(startDir || process.cwd());
    d = up;
  }
}

export function loadQaConfig(repoRoot) {
  const qaDir = path.join(repoRoot, 'qa');
  const envs = readJsonSafe(path.join(qaDir, 'config', 'envs.json'), null);
  const roles = readJsonSafe(path.join(qaDir, 'config', 'roles.json'), null);
  const strip = (obj) => {
    if (!obj || typeof obj !== 'object') return null;
    const out = {};
    for (const [k, v] of Object.entries(obj)) if (!k.startsWith('_')) out[k] = v;
    return out;
  };
  return { qaDir, envs: strip(envs), roles: strip(roles), found: Boolean(envs || roles) };
}

// Origin của apiBase/webBase khai trong envs.json (bỏ env tên prod) = non-prod đã khai.
export function knownNonProdOrigins(envs) {
  const set = new Set();
  for (const [name, cfg] of Object.entries(envs || {})) {
    if (isProdEnvName(name) || !cfg || typeof cfg !== 'object') continue;
    for (const k of ['apiBase', 'webBase']) {
      const o = safeOrigin(cfg[k]);
      if (o) set.add(o);
    }
  }
  return set;
}

export function checkOriginGate({ origin, allowlist, allowProd = false, confirmProd = '' } = {}) {
  const list = allowlist instanceof Set ? allowlist : new Set(allowlist || []);
  if (origin && (list.has(origin) || isLocalOrigin(origin))) return { ok: true, prod: false, message: '' };
  if (allowProd && origin && confirmProd === origin) {
    return { ok: true, prod: true, message: `Chạy trên môi trường CHƯA khai non-prod đã được cấp phép tường minh: ${origin}` };
  }
  return {
    ok: false,
    prod: false,
    message:
      `Từ chối chạy trên môi trường CHƯA xác nhận non-prod: ${origin || '(baseURL rỗng)'}\n`
      + '  • Non-prod: khai origin trong qa/config/envs.json hoặc file .allowed-origins (1 origin/dòng) rồi chạy lại.\n'
      + `  • Production (rủi ro — test có thể tạo/đổi dữ liệu thật): cần cả \`--allow-prod\` VÀ \`--confirm-prod ${origin || '<origin>'}\`.`,
  };
}

// ---------------------------------------------------------------- dotenv

export function loadDotEnv(envPath) {
  const out = {};
  if (!envPath || !fs.existsSync(envPath)) return out;
  for (const raw of fs.readFileSync(envPath, 'utf8').split('\n')) {
    const line = raw.trim();
    if (!line || line.startsWith('#')) continue;
    const eq = line.indexOf('=');
    if (eq === -1) continue;
    const key = line.slice(0, eq).trim().replace(/^export\s+/, '');
    let value = line.slice(eq + 1).trim();
    if (!/^[A-Za-z_][A-Za-z0-9_]*$/.test(key)) continue;
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    out[key] = value;
  }
  return out;
}

export function loadEnvLayers(paths) {
  const out = {};
  for (const p of paths || []) Object.assign(out, loadDotEnv(p));
  return out;
}
