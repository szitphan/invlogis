#!/usr/bin/env node
/*
 * bruno-runner.mjs — runner dùng chung cho /api-test (mọi feature). 2 chế độ, tự phát hiện theo --dir:
 *
 * A) TABLE (giữ nguyên hành vi cũ — API bên thứ 3 / bảng own-API kiểu cũ)
 *    Bảng `test/api/api-tests.md` (giữa <!-- TC:START --> / <!-- TC:END -->) là SOURCE OF TRUTH.
 *      gen → bruno/{provider|own}/{TC}.bru + bruno.json + _setup/login.bru (khi có cột Auth=session).
 *            KHÔNG đụng bruno/environments/ + bruno/.env.
 *      run → gen → bru run --env <env> --reporter-json → ghi ✅/❌/⏳ + thời điểm vào bảng + dòng Lịch sử chạy.
 *    Cột: 3rd-party: TC | Provider | Method | Path | Headers | Body | HTTP | Assert | Kết quả | Lần chạy
 *         own API:   TC | Method | Path | Auth  | Body | HTTP | Assert | Kết quả | Lần chạy
 *    `--tc` luôn kèm `_setup` (login) khi bảng có Auth=session (bản cũ bỏ sót → TC session rớt giả).
 *
 * B) OWN-API (test case **Target:** api trong test/testcases/testcases-*.md)
 *      gen → test/api/bruno-api/ dạng OpenCollection YAML giống transport-erp/bruno (bảng 3rd-party vẫn ở bruno/):
 *            opencollection.yml · environments/{dev,sit,local}.yml (từ qa/config/envs.json) ·
 *            NNN-{CHK}/folder.yml + chuỗi 3 bước đăng nhập theo vai (01-login → 02-select-working-context →
 *            03-working-context-facility, kênh Mobile/Web + platform theo qa/config/roles.json) + từng bước TC.
 *            Bắt id từ response vào biến (bru.setVar) cho bước sau; assert status + body + errorCode.
 *            Bước tuỳ chọn IgasSimulator (in-use / pumped) — host/khoá qua IGAS_SIM_BASE / IGAS_SIM_KEY.
 *      run → bru (cục bộ: qa/node_modules/.bin/bru hoặc PATH; KHÔNG tải mạng) chạy từng thư mục TC →
 *            phân loại PASS/FAIL_APP/FAIL_DATA/FAIL_OUTDATE/FAIL_DOC/PENDING (testgen-core) → run-history.json,
 *            {feature}-api-index.md, docs/{feature}/test/results/latest.json. Chưa có bru → PENDING "bru chưa cài".
 *
 *    Grammar test case (Target api):
 *      Action:    [vai: <role>] GET|POST|PUT|PATCH|DELETE /api/...   (path có thể chứa {{bien}})
 *                 Giả lập bơm in-use {{authorizationCode}}  ·  Giả lập bơm pumped {{authorizationCode}} 48.5 lít
 *      Test Data: body JSON (được dùng {{bien}}) hoặc —
 *      Expected:  mỗi dòng/`;` 1 ý: `HTTP 201` · `HTTP 2xx` · `errorCode = "FuelDispensing.X"` ·
 *                 `body.data.status = "pending"` (op: = != > >= < <= contains exists không rỗng) ·
 *                 `lưu data.id → fuelDispensingId` (bắt biến cho bước sau)
 *      **Data:** key → biến {{data_<key>}} lấy từ test/api/testdata.json ("@data.<key>"); rỗng → PENDING.
 *
 * "Môi trường giấy" (100% connection-refused) → ⏳ PENDING, KHÔNG FAIL giả, exit 0.
 * Tự phát hiện có cả bảng + own: own-API chỉ chạy khi --env có trong qa/config/envs.json, không thì in 1 dòng bỏ qua;
 * exit code chỉ tính các chế độ đã chạy.
 * BẢO MẬT: secret CHỈ ở qa/.env hoặc bruno-api/.env / bruno/.env (gitignored) qua {{process.env.*}}. Report JSON (có token đã
 * resolve) bị XOÁ ngay sau khi parse. Không in Authorization/token.
 *
 * Dùng:
 *   node .claude/scripts/bruno-runner.mjs gen --dir docs/{feature}/test        [--mode own|table]
 *   node .claude/scripts/bruno-runner.mjs run --dir docs/{feature}/test        [--env dev|sit|local] [--tc CHK-…,CHK-…]
 *   node .claude/scripts/bruno-runner.mjs run --dir docs/{feature}/test/api    [--env mock|sandbox|prod|local|staging]
 *        [--tc TC-01,TC-03] [--provider paygate] [--allow-prod]          (chế độ bảng, như cũ)
 */

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

import {
  addUniqueReason,
  classifyResult,
  cleanValue,
  dataFingerprint,
  findRepoRoot,
  isDash,
  isProdEnvName,
  loadChecklistIndex,
  loadDotEnv,
  loadQaConfig,
  loadRunHistory,
  loadTestcaseDir,
  normalizeVietnamese,
  readNormalizedResults,
  readinessReasons,
  requireSlug,
  resolveDataKeys,
  resolveRole,
  saveRunHistory,
  tcOracle,
  tcTarget,
  today,
  updateRunHistory,
  writeNormalizedResults,
  writeTestData,
} from './testgen-core.mjs';

class CliError extends Error {}
const fail = (message) => { throw new CliError(message); };

// ---------- args ----------
export function parseArgs(argvRaw) {
  const argv = argvRaw.slice(2);
  const mode = argv[0] && !argv[0].startsWith('--') ? argv[0] : 'run';
  const flag = (name, def = null) => {
    const i = argv.indexOf(`--${name}`);
    return i >= 0 ? (argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : true) : def;
  };
  const tc = flag('tc');
  return {
    mode,
    dir: flag('dir'),
    env: flag('env'),
    tc: tc && tc !== true ? String(tc).split(',').map((s) => s.trim()).filter(Boolean) : null,
    provider: flag('provider') ? String(flag('provider')).toLowerCase() : null,
    allowProd: argv.includes('--allow-prod'),
    kind: flag('mode'),
  };
}

// =====================================================================================================
// A) TABLE MODE (giữ hành vi cũ)
// =====================================================================================================

function readTable(TABLE_FILE) {
  const md = fs.readFileSync(TABLE_FILE, 'utf8');
  const start = md.indexOf('<!-- TC:START -->');
  const end = md.indexOf('<!-- TC:END -->');
  if (start < 0 || end < 0) throw new Error('Không thấy marker TC:START/END trong api-tests.md');
  const block = md.slice(start, end).split('\n').filter((l) => l.trim().startsWith('|'));
  const header = block[0].split('|').slice(1, -1).map((c) => c.trim().toLowerCase());
  const hasProvider = header.includes('provider');
  const hasAuth = header.includes('auth');
  const idx = (name) => header.indexOf(name);

  const rows = [];
  for (const line of block.slice(2)) {
    const cells = line.split('|').slice(1, -1).map((c) => c.trim());
    if (!cells.length || !/^TC-\d+/i.test(cells[0])) continue;
    rows.push({
      tc: cells[0].toUpperCase(),
      provider: hasProvider ? (cells[idx('provider')] || 'own').toLowerCase() : 'own',
      auth: hasAuth ? (cells[idx('auth')] || 'public').toLowerCase() : null,
      method: (cells[idx('method')] || '').toUpperCase(),
      pathRaw: cells[idx('path')] || '',
      headers: hasProvider ? (cells[idx('headers')] || '—') : '—',
      body: cells[idx('body')] || '—',
      http: cells[idx('http')] || '',
      assert: cells[idx('assert')] || '—',
    });
  }
  return { rows, hasProvider, hasAuth };
}

const slug = (s) => s.replace(/^\//, '').split('?')[0].replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-|-$/g, '') || 'root';

function assertBody(http, assert) {
  const lines = [`  res.status: eq ${http}`];
  if (assert && assert !== '—') {
    for (const pair of assert.split(';').map((x) => x.trim())) {
      const m = pair.match(/^([\w.]+)=(.+)$/);
      if (m) lines.push(`  res.body.${m[1]}: eq ${m[2]}`);
      // prose không match dotpath=value → ghi nguyên văn để người review biết còn assertion cần kiểm tay.
      else lines.push(`  # kiểm thủ công: ${pair}`);
    }
  }
  return lines.join('\n');
}

function emitBru(r, seq, ownBaseVar) {
  const m = r.method.toLowerCase();
  const hasBody = r.body && r.body !== '—' && m !== 'get';
  const useBearer = r.provider !== 'own';
  const L = [];
  L.push('meta {');
  L.push(`  name: ${r.tc} ${r.method} ${r.pathRaw}${r.auth === 'session' ? ' [session]' : ''}`);
  L.push('  type: http');
  L.push(`  seq: ${seq}`);
  L.push('}');
  L.push('');
  const urlVar = useBearer ? `{{${r.provider.toUpperCase()}_BASE}}` : `{{${ownBaseVar}}}`;
  L.push(`${m} {`);
  L.push(`  url: ${urlVar}${r.pathRaw}`);
  if (hasBody) L.push('  body: json');
  if (useBearer) L.push('  auth: bearer');
  L.push('}');
  if (useBearer) {
    L.push('', 'auth:bearer {', `  token: {{process.env.${r.provider.toUpperCase()}_KEY}}`, '}');
  }
  if (r.headers && r.headers !== '—') {
    L.push('', 'headers {');
    for (const h of r.headers.split(';')) {
      const i = h.indexOf(':');
      if (i < 0) continue;
      L.push(`  ${h.slice(0, i).trim()}: ${h.slice(i + 1).trim()}`);
    }
    L.push('}');
  }
  if (hasBody) {
    let bodyText = r.body;
    try { bodyText = JSON.stringify(JSON.parse(r.body), null, 2); } catch { /* keep raw */ }
    L.push('', 'body:json {');
    for (const bl of bodyText.split('\n')) L.push(`  ${bl}`);
    L.push('}');
  }
  L.push('', 'assert {');
  // .bru KHÔNG cho comment `#` ngoài block → ghi chú session sống trong assert{}.
  if (r.auth === 'session') L.push('  # Auth=session: cần _setup/login.bru chạy trước (cookie jar). Chạy cả suite, đừng chạy lẻ.');
  L.push(assertBody(r.http, r.assert));
  L.push('}', '');
  return L.join('\n');
}

function loginBru(ownBaseVar) {
  return [
    'meta {', '  name: _setup login (seed account)', '  type: http', '  seq: 0', '}', '',
    'post {', `  url: {{${ownBaseVar}}}/auth/login`, '  body: json', '}', '',
    'body:json {', '  {', '    "email": "{{process.env.SEED_EMAIL}}",', '    "password": "{{process.env.SEED_PASSWORD}}"', '  }', '}', '',
    'assert {',
    '  res.status: eq 200',
    '  # Cookie-session: Bruno cookie jar giữ session sau request này cho các TC Auth=session trong cùng run.',
    '  # Nếu backend dùng JWT thay cookie: thêm vars:post-response { authToken: res.body.token } + auth:bearer ở TC session.',
    '}', '',
  ].join('\n');
}

// Feature slug = segment ngay sau "docs/" (vd docs/authentication/test/api -> authentication).
function deriveFeature(HERE) {
  const parts = HERE.split(path.sep);
  const i = parts.lastIndexOf('docs');
  return (i >= 0 && parts[i + 1]) ? parts[i + 1] : 'api';
}

export function genTable(layout) {
  const { apiDir: HERE, tableFile: TABLE_FILE, tableBrunoDir: BRUNO_DIR } = layout;
  const { rows, hasAuth } = readTable(TABLE_FILE);
  fs.mkdirSync(BRUNO_DIR, { recursive: true });

  const feature = deriveFeature(HERE);
  const ownBaseVar = `${feature.toUpperCase().replace(/[^A-Z0-9]+/g, '_')}_BASE`;

  const bjson = path.join(BRUNO_DIR, 'bruno.json');
  if (!fs.existsSync(bjson)) {
    fs.writeFileSync(bjson, `${JSON.stringify({ version: '1', name: `${feature}-api-tests`, type: 'collection', ignore: ['node_modules', '.git'] }, null, 2)}\n`);
  }

  for (const p of [...new Set(rows.map((r) => r.provider))]) {
    const dir = path.join(BRUNO_DIR, p);
    if (fs.existsSync(dir)) for (const f of fs.readdirSync(dir)) if (f.endsWith('.bru')) fs.rmSync(path.join(dir, f));
    fs.mkdirSync(dir, { recursive: true });
  }

  const hasSession = hasAuth && rows.some((r) => r.auth === 'session');
  if (hasSession) {
    fs.rmSync(path.join(BRUNO_DIR, '_setup'), { recursive: true, force: true });
    fs.mkdirSync(path.join(BRUNO_DIR, '_setup'), { recursive: true });
    fs.writeFileSync(path.join(BRUNO_DIR, '_setup', 'login.bru'), loginBru(ownBaseVar));
  }

  const filemap = {};
  for (const r of rows) {
    if (!r.http) continue; // multi-step/side-effect không có HTTP code → ngoài suite auto
    const seq = parseInt(r.tc.replace(/\D/g, ''), 10) || 0;
    const fname = `${r.tc}-${r.method.toLowerCase()}-${slug(r.pathRaw)}.bru`;
    const fp = path.join(BRUNO_DIR, r.provider, fname);
    fs.writeFileSync(fp, emitBru(r, seq, ownBaseVar));
    filemap[r.tc] = fp;
  }
  const manual = rows.filter((r) => !r.http);
  return { rows, filemap, manual, hasSession, BRUNO_DIR, TABLE_FILE };
}

// Chọn target chạy cho bảng. `--tc` luôn kèm `_setup` khi có Auth=session.
export function tableTargets({ filemap, hasSession, BRUNO_DIR }, tcFilter, providerFilter) {
  if (tcFilter) {
    const wanted = tcFilter.map((s) => s.toUpperCase());
    const picked = wanted.map((tc) => filemap[tc]).filter(Boolean).map((fp) => path.relative(BRUNO_DIR, fp));
    if (!picked.length) return [];
    return hasSession ? ['_setup', ...picked] : picked;
  }
  if (providerFilter) return hasSession ? ['_setup', providerFilter] : [providerFilter];
  return hasSession
    ? ['_setup', ...new Set(Object.values(filemap).map((fp) => path.relative(BRUNO_DIR, path.dirname(fp))))]
    : ['.'];
}

// ---------- report parse (dùng chung 2 chế độ) ----------
export function flattenReport(json) {
  const items = [];
  const dig = (node) => {
    if (Array.isArray(node)) { node.forEach(dig); return; }
    if (node && typeof node === 'object') {
      if (node.request || node.response || node.assertionResults || node.runtimeError !== undefined || node.suitename) {
        items.push(node);
      }
      if (Array.isArray(node.results)) node.results.forEach(dig);
      if (Array.isArray(node.iterations)) node.iterations.forEach(dig);
    }
  };
  dig(json);
  return items;
}

export function classify(item) {
  const name = item.suitename || item.test?.filename || item.request?.name || (item.request?.url || '');
  const tcMatch = String(name).match(/TC-\d+/i);
  const tc = tcMatch ? tcMatch[0].toUpperCase() : null;
  const status = item.response?.status ?? '';
  const reasons = [];
  let pass = true;
  let connectionRefused = false;
  if (item.error || item.runtimeError) {
    pass = false;
    const msg = String(item.error || item.runtimeError);
    reasons.push(msg.split('\n')[0].slice(0, 80));
    if (/ECONNREFUSED|connection refused|ENOTFOUND|ETIMEDOUT|EAI_AGAIN/i.test(msg)) connectionRefused = true;
  }
  for (const a of (item.assertionResults || [])) {
    if (a.status === 'fail') { pass = false; reasons.push(`assert ${a.lhsExpr} ${a.operator} ${a.rhsExpr}`.slice(0, 80)); }
  }
  for (const t of (item.testResults || [])) {
    if (t.status === 'fail') { pass = false; reasons.push(`test: ${t.description}`.slice(0, 80)); }
  }
  if (!item.assertionResults?.length && !item.testResults?.length && !status && !item.error && !item.runtimeError) {
    pass = false; connectionRefused = true; reasons.push('không có response (connection refused — mock/backend chưa chạy?)');
  }
  return { tc, status, pass, connectionRefused, reason: reasons.join('; ') };
}

// 100% item connection-refused → env chưa sẵn sàng, không phải kết quả test thật.
export function derivePending(resultsMap) {
  const entries = Object.values(resultsMap);
  if (!entries.length) return false;
  return entries.every((r) => r.connectionRefused);
}

// ---------- tìm bru cục bộ (không tải mạng) ----------
export function resolveBru(repoRoot, env = process.env) {
  const candidates = [];
  if (env.BRU_BIN) candidates.push(env.BRU_BIN);
  if (repoRoot) candidates.push(path.join(repoRoot, 'qa', 'node_modules', '.bin', 'bru'));
  candidates.push('bru');
  for (const bin of candidates) {
    if (bin !== 'bru' && !fs.existsSync(bin)) continue;
    const r = spawnSync(bin, ['--version'], { encoding: 'utf8', env });
    if (!r.error && r.status === 0) return { bin, version: String(r.stdout || '').trim() };
  }
  return null;
}

let reportCounter = 0;
function runBru(bruCmd, cwd, target, envName, envVars = {}, spawnEnv = process.env) {
  const reportFile = path.join(os.tmpdir(), `.bruno-report-${process.pid}-${Date.now()}-${reportCounter++}.json`);
  const args = [...bruCmd.args, 'run', target, '-r', '--env', envName, '--reporter-json', reportFile];
  for (const [k, v] of Object.entries(envVars)) args.push('--env-var', `${k}=${v}`);
  const res = spawnSync(bruCmd.bin, args, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'], env: spawnEnv });
  let items = [];
  if (fs.existsSync(reportFile)) {
    try { items = flattenReport(JSON.parse(fs.readFileSync(reportFile, 'utf8'))); } catch { /* coi như 0 item */ }
    fs.rmSync(reportFile, { force: true }); // KHÔNG giữ — có thể chứa token/cookie đã resolve
  }
  return { items, launchErr: res.error, code: res.status, stderr: res.stderr };
}

function ts() {
  const d = new Date();
  const p = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}`;
}

function writeback(TABLE_FILE, resultsMap, when, pending, envName) {
  let md = fs.readFileSync(TABLE_FILE, 'utf8');
  const lines = md.split('\n');
  let inBlock = false;
  for (let i = 0; i < lines.length; i += 1) {
    if (lines[i].includes('<!-- TC:START -->')) { inBlock = true; continue; }
    if (lines[i].includes('<!-- TC:END -->')) { inBlock = false; continue; }
    if (!inBlock || !lines[i].trim().startsWith('|')) continue;
    const cells = lines[i].split('|');
    const tc = cells[1] && cells[1].trim().toUpperCase();
    if (!tc || !resultsMap[tc]) continue;
    const r = resultsMap[tc];
    const mark = pending ? '⏳ PENDING' : (r.pass ? '✅ PASS' : '❌ FAIL');
    cells[cells.length - 3] = ` ${mark} `;
    cells[cells.length - 2] = ` ${when} `;
    lines[i] = cells.join('|');
  }
  md = lines.join('\n');
  const pass = Object.values(resultsMap).filter((r) => r.pass).length;
  const total = Object.values(resultsMap).length;
  const histLine = pending
    ? `- ${when} | ⏳ env chưa sẵn sàng (connection refused toàn bộ ${total} case) — chưa phải kết quả test thật`
    : `- ${when} | ${pass}/${total} pass | ${total - pass} fail | env=${envName}`;
  const anchor = '## Lịch sử chạy';
  if (md.includes(anchor)) md = md.replace(anchor, `${anchor}\n\n${histLine}`);
  fs.writeFileSync(TABLE_FILE, md);
}

// Bảng: phân loại sơ bộ (401/403 = nghi data tài khoản; còn lại = nghi app) + lịch sử chạy.
export function classifyTableResult(r, prev, fingerprint) {
  if (r.connectionRefused) return { status: 'PENDING', note: 'connection refused' };
  if (r.pass) return { status: 'PASS', note: '' };
  const kind = /^(401|403)$/.test(String(r.status)) ? 'data' : 'app';
  return classifyResult({ status: 'FAIL', kind, prev, fingerprint });
}

function npxBru() {
  return { bin: 'npx', args: ['--yes', '@usebruno/cli'] };
}

export function runTable(layout, args) {
  const ENV = args.env || 'mock';
  if (ENV === 'prod' && !args.allowProd) {
    console.error('✋ Từ chối chạy --env prod khi thiếu --allow-prod (production thật, có thể tạo data/tốn quota).');
    return 2;
  }
  const g = genTable(layout);
  if (g.manual.length) console.log(`Bỏ qua khỏi suite auto (multi-step/side-effect, test thủ công): ${g.manual.map((r) => r.tc).join(', ')}`);

  const targets = tableTargets(g, args.tc, args.provider);
  if (!targets.length) { console.error('Không TC nào khớp --tc'); return 2; }

  // bru cục bộ trước; không có thì npx như bản cũ (cần mạng lần đầu).
  const local = resolveBru(layout.repoRoot);
  const bruCmd = local ? { bin: local.bin, args: [] } : npxBru();

  const all = [];
  let anyLaunchErr = null;
  let anyStderr = '';
  for (const t of targets) {
    const { items, launchErr, stderr } = runBru(bruCmd, g.BRUNO_DIR, t, ENV);
    if (launchErr) anyLaunchErr = launchErr;
    if (stderr) anyStderr += stderr;
    all.push(...items);
  }
  if (anyLaunchErr) {
    console.error('Không gọi được Bruno CLI:', anyLaunchErr.message);
    console.error('→ bru chưa cài: `npm i -g @usebruno/cli` hoặc `cd qa && npm install` (npx cần mạng lần đầu).');
    return 1;
  }
  if (!all.length) {
    console.error(`Bruno CLI không trả report nào. stderr:\n${(anyStderr || '(rỗng)').slice(0, 600)}`);
    return 1;
  }

  const resultsMap = {};
  for (const it of all) {
    const c = classify(it);
    if (c.tc) resultsMap[c.tc] = c;
  }
  const pending = derivePending(resultsMap);
  const when = ts();
  writeback(g.TABLE_FILE, resultsMap, when, pending, ENV);

  const history = loadRunHistory(layout.apiDir);
  const fingerprint = `env=${ENV}`;
  const statusMap = {};
  const entries = Object.entries(resultsMap).sort();
  console.log(`\n=== api-test (Bruno, env=${ENV}, dir=${path.relative(process.cwd(), layout.apiDir)}) ===`);
  if (pending) {
    console.log('⏳ Môi trường chưa sẵn sàng — 100% request connection-refused. Đây KHÔNG phải kết quả test (chưa có backend/mock chạy).');
    for (const [tc] of entries) console.log(`⏳ ${tc}  PENDING`);
    console.log('\nĐã ghi ⏳ PENDING vào api-tests.md (không ghi đè PASS/FAIL giả).');
    return 0;
  }
  let pass = 0;
  for (const [tc, r] of entries) {
    const c = classifyTableResult(r, history[tc], fingerprint);
    statusMap[tc] = c.status === 'PASS' ? 'PASS' : c.status === 'PENDING' ? 'PENDING' : 'FAIL';
    if (r.pass) pass += 1;
    console.log(`${r.pass ? '✅' : '❌'} ${tc}  HTTP ${r.status || '-'}${r.pass ? '' : `  ← ${r.reason}  [${c.status}]`}`);
  }
  saveRunHistory(layout.apiDir, updateRunHistory(history, statusMap, fingerprint));
  console.log(`\n${pass}/${entries.length} pass | ${entries.length - pass} fail`);
  console.log('Đã ghi kết quả vào api-tests.md (cột Kết quả/Lần chạy + Lịch sử chạy) + run-history.json.');
  return entries.length - pass;
}

// =====================================================================================================
// B) OWN-API MODE (OpenCollection YAML)
// =====================================================================================================

const HTTP_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'];

export function dataVarName(key) {
  return `data_${String(key).replace(/[^A-Za-z0-9]+/g, '_').replace(/^_+|_+$/g, '')}`;
}

// Action → { role?, kind:'http'|'igas', method, path, igasAction, code, liters } | { error }
export function parseApiAction(action) {
  let text = cleanValue(action).replace(/\n+/g, ' ');
  let role = '';
  const rolePrefix = text.match(/^\s*[[(]\s*(?:vai|vai trò|vai tro|role)\s*:?\s*([a-z0-9][a-z0-9-]*)\s*[\])]\s*/i);
  if (rolePrefix) {
    role = rolePrefix[1].toLowerCase();
    text = text.slice(rolePrefix[0].length);
  }

  const http = text.match(/^\s*(GET|POST|PUT|PATCH|DELETE)\s+(\S+)/i);
  if (http) {
    const method = http[1].toUpperCase();
    const p = http[2].replace(/[),;.]+$/, '');
    if (!/^(\/|\{\{)/.test(p)) return { role, error: `Path phải bắt đầu bằng "/" hoặc {{bien}}: ${p}` };
    return { role, kind: 'http', method, path: p };
  }

  const n = normalizeVietnamese(text);
  const igas = n.match(/^\s*gia lap (?:bom|igas)\s+(in-use|in use|dang bom|pumped|da bom|bom xong)\b/);
  if (igas) {
    const igasAction = /in-use|in use|dang bom/.test(igas[1]) ? 'in-use' : 'pumped';
    const codeMatch = text.match(/\{\{\s*([A-Za-z_][\w.]*)\s*\}\}/) || text.match(/["“]([^"”]+)["”]/);
    if (!codeMatch) return { role, error: 'Giả lập bơm thiếu mã lệnh ({{bien}} hoặc "mã")' };
    const code = codeMatch[0].startsWith('{{') ? `{{${codeMatch[1]}}}` : codeMatch[1];
    const litersMatch = n.match(/(\d+(?:[.,]\d+)?)\s*(?:lit|l)\b/);
    return {
      role,
      kind: 'igas',
      igasAction,
      code,
      liters: litersMatch ? Number(litersMatch[1].replace(',', '.')) : null,
    };
  }

  return { role, error: 'Action API chưa theo grammar: "[vai: x] METHOD /path" hoặc "Giả lập bơm in-use|pumped {{ma}}"' };
}

const OPS = [
  [/^(?:==|=|là|la)$/i, 'eq'],
  [/^!=$/, 'neq'],
  [/^>=$/, 'gte'],
  [/^<=$/, 'lte'],
  [/^>$/, 'gt'],
  [/^<$/, 'lt'],
  [/^(?:chứa|chua|contains)$/i, 'contains'],
];

function assertionValue(raw) {
  const v = String(raw ?? '').trim();
  const quoted = v.match(/^["“'](.*)["”']$/);
  if (quoted) return `"${quoted[1]}"`;
  if (/^-?\d+(?:\.\d+)?$/.test(v) || /^(true|false|null)$/i.test(v)) return v.toLowerCase() === v ? v : v.toLowerCase();
  return `"${v}"`;
}

// Expected → { assertions:[{expression, operator, value}], captures:[{path, name}], unmapped:[], hasStatus }
export function parseApiExpected(expected) {
  const out = { assertions: [], captures: [], unmapped: [], hasStatus: false };
  const parts = cleanValue(expected).split(/\n|;/).map((s) => s.trim().replace(/^[-*•]\s+/, '')).filter(Boolean);

  for (const part of parts) {
    if (isDash(part)) continue;

    const st = part.match(/^(?:HTTP|status|mã HTTP|ma HTTP|trả về|tra ve)?\s*:?\s*([1-5])(\d\d|xx)\b/i);
    if (st && /^(?:HTTP|status|mã|ma|trả|tra|\d)/i.test(part)) {
      if (st[2].toLowerCase() === 'xx') {
        out.assertions.push({ expression: 'res.status', operator: 'gte', value: `${st[1]}00` });
        out.assertions.push({ expression: 'res.status', operator: 'lte', value: `${st[1]}99` });
      } else {
        out.assertions.push({ expression: 'res.status', operator: 'eq', value: `${st[1]}${st[2]}` });
      }
      out.hasStatus = true;
      continue;
    }

    const ec = part.match(/^errorCode\s*(?:=|==|:|là|la)\s*["“']?([^"”'\s]+)["”']?\s*$/i);
    if (ec) {
      out.assertions.push({ expression: 'res.body.errorCode', operator: 'eq', value: `"${ec[1]}"` });
      continue;
    }

    const cap = part.match(/^(?:lưu|luu|capture|save|ghi nhớ|ghi nho)\s+(?:res\.)?(?:body\.)?([A-Za-z_][\w.[\]]*)\s*(?:→|->|=>|vào|vao|as|thành|thanh)\s*([A-Za-z_]\w*)\s*$/i);
    if (cap) {
      out.captures.push({ path: cap[1], name: cap[2] });
      continue;
    }

    const exists = part.match(/^(?:res\.)?(?:body\.)?([A-Za-z_][\w.[\]]*)\s+(tồn tại|ton tai|exists|không rỗng|khong rong|not empty)\s*$/i);
    if (exists) {
      const op = /rỗng|rong|empty/i.test(exists[2]) ? 'isNotEmpty' : 'isDefined';
      out.assertions.push({ expression: `res.body.${exists[1]}`, operator: op, value: '' });
      continue;
    }

    const bodyCmp = part.match(/^(?:res\.)?body\.([A-Za-z_][\w.[\]]*)\s*(==|!=|>=|<=|=|>|<|chứa|chua|contains|là|la)\s*(.+)$/i)
      || part.match(/^((?:data|isSuccess|errors?|message|meta)(?:[.[][\w.[\]]*)?)\s*(==|!=|>=|<=|=|>|<|chứa|chua|contains)\s*(.+)$/);
    if (bodyCmp) {
      const op = OPS.find(([re]) => re.test(bodyCmp[2]))?.[1] || 'eq';
      out.assertions.push({ expression: `res.body.${bodyCmp[1]}`, operator: op, value: assertionValue(bodyCmp[3]) });
      continue;
    }

    out.unmapped.push(part);
  }
  return out;
}

function bodyIsJson(text) {
  try {
    JSON.parse(String(text).replace(/\{\{\s*[^}]+\s*\}\}/g, '0'));
    return true;
  } catch {
    return false;
  }
}

// TC → kế hoạch request (pure). opts: { roles, oracle, platformOverride }
export function planApiTestcase(tc, opts = {}) {
  const reasons = readinessReasons(tc, { roles: opts.roles || undefined });
  const target = tcTarget(tc);
  if (target !== 'api') addUniqueReason(reasons, `Target=${target} — không phải api`);

  const tcRole = resolveRole(tc);
  const dataKeys = resolveDataKeys(tc);
  const requests = [];
  const roleCfg = (r) => (opts.roles && opts.roles[r]) || null;
  let currentRole = '';
  let usesIgas = false;
  let assertionCount = 0;
  const rolesUsed = [];

  const pushAuth = (role) => {
    const cfg = roleCfg(role);
    if (opts.roles && !cfg) {
      addUniqueReason(reasons, `Role "${role}" không có trong qa/config/roles.json`);
      return;
    }
    requests.push({ kind: 'auth-login', role, cfg });
    requests.push({ kind: 'auth-select', role, cfg });
    if (cfg?.facilityEnv) requests.push({ kind: 'auth-facility', role, cfg });
    if (!rolesUsed.includes(role)) rolesUsed.push(role);
    currentRole = role;
  };

  for (const step of tc.steps || []) {
    const stepNo = cleanValue(step.n) || '?';
    const act = parseApiAction(step.action);
    if (act.error) {
      addUniqueReason(reasons, `Step ${stepNo}: ${act.error}`);
      continue;
    }
    const exp = parseApiExpected(step.expected);
    if (exp.unmapped.length) addUniqueReason(reasons, `Step ${stepNo}: Expected chưa map được: ${exp.unmapped.join(' | ')}`);

    if (act.kind === 'http') {
      const role = act.role || currentRole || tcRole;
      if (!role) addUniqueReason(reasons, `Step ${stepNo}: API cần **Role:** (hoặc tiền tố [vai: x]) để đăng nhập`);
      else if (role !== currentRole) pushAuth(role);
      if (!exp.hasStatus) addUniqueReason(reasons, `Step ${stepNo}: Expected thiếu HTTP status (vd "HTTP 201")`);
      const td = cleanValue(step.testData);
      let body = '';
      if (td && !isDash(td)) {
        if (act.method === 'GET') addUniqueReason(reasons, `Step ${stepNo}: GET không nhận body (Test Data)`);
        else if (/^ENV\s*:/i.test(td)) addUniqueReason(reasons, `Step ${stepNo}: Test Data ENV: không dùng làm body — đặt {{process.env.X}} trong JSON`);
        else if (!bodyIsJson(td)) addUniqueReason(reasons, `Step ${stepNo}: Test Data phải là JSON body`);
        else body = td;
      }
      requests.push({ kind: 'http', step: stepNo, method: act.method, path: act.path, body, ...exp });
    } else {
      usesIgas = true;
      let liters = act.liters;
      const td = cleanValue(step.testData);
      if (act.igasAction === 'pumped' && liters == null && td && !isDash(td) && /^\d+(?:[.,]\d+)?$/.test(td)) {
        liters = Number(td.replace(',', '.'));
      }
      if (act.igasAction === 'pumped' && (liters == null || !(liters > 0))) {
        addUniqueReason(reasons, `Step ${stepNo}: Giả lập pumped cần số lít > 0 (trong Action hoặc Test Data)`);
      }
      if (!exp.hasStatus) exp.assertions.unshift({ expression: 'res.status', operator: 'eq', value: '200' });
      requests.push({ kind: 'igas', step: stepNo, igasAction: act.igasAction, code: act.code, liters, ...exp });
    }
    assertionCount += exp.assertions.length;
  }

  if (!requests.some((r) => r.kind === 'http' || r.kind === 'igas')) addUniqueReason(reasons, 'không có bước API map được');
  if (!assertionCount) addUniqueReason(reasons, 'test case không có assertion map được');

  return {
    ready: reasons.length === 0,
    reasons,
    requests,
    roles: rolesUsed,
    dataKeys,
    dataVars: dataKeys.map(dataVarName),
    usesIgas,
    oracle: opts.oracle || null,
  };
}

// ---------- YAML emit (OpenCollection, khớp transport-erp/bruno) ----------

const yq = (s) => `'${String(s ?? '').replace(/'/g, "''")}'`;
const block = (text, indent) => String(text).split('\n').map((l) => (l ? `${' '.repeat(indent)}${l}` : '')).join('\n');
const SETTINGS = ['settings:', '  encodeUrl: true', '  timeout: 0', '  followRedirects: true', '  maxRedirects: 5'];
const READ_PATH_JS = [
  'function readPath(source, p) {',
  "  return String(p).replace(/\\[(\\d+)\\]/g, '.$1').split('.').filter(Boolean)",
  '    .reduce((value, key) => (value == null ? undefined : value[key]), source);',
  '}',
].join('\n');

function scriptsYaml(scripts) {
  if (!scripts.length) return [];
  const L = ['  scripts:'];
  for (const s of scripts) {
    L.push(`  - type: ${s.type}`, '    code: |-', block(s.code, 6));
  }
  return L;
}

function assertionsYaml(assertions) {
  if (!assertions.length) return [];
  const L = ['  assertions:'];
  for (const a of assertions) {
    L.push(`  - expression: ${a.expression}`, `    operator: ${a.operator}`, `    value: ${yq(a.value)}`);
  }
  return L;
}

function headerYaml(headers) {
  const L = ['  headers:'];
  for (const h of headers) {
    L.push(`  - name: ${h.name}`, `    value: ${yq(h.value)}`);
    if (h.description) L.push(`    description: ${h.description}`);
  }
  return L;
}

export function renderAuthRequest(req, seq) {
  const { role, cfg } = req;
  const mobile = String(cfg?.channel || 'Web').toLowerCase() === 'mobile';
  const channel = mobile ? 'Mobile' : 'Web';
  const platform = cfg?.platform || (mobile ? 'Android' : 'Web');
  const userEnv = cfg?.userEnv || `QA_${role.toUpperCase().replace(/-/g, '_')}_USER`;
  const passEnv = cfg?.passEnv || `QA_${role.toUpperCase().replace(/-/g, '_')}_PASS`;
  const tenant = { name: 'X-Tenant-Id', value: '{{tenantId}}' };
  const corr = { name: 'X-Correlation-ID', value: '{{$guid}}', description: 'Request tracing ID' };
  const L = [];

  if (req.kind === 'auth-login') {
    L.push('info:', `  name: ${yq(`Đăng nhập ${role} (${channel})`)}`, '  type: http', `  seq: ${seq}`, '  tags:', '  - auth', '  - login');
    L.push('http:', '  method: POST', `  url: ${yq('{{baseURL}}/api/identity/v1/auth/login')}`);
    L.push(...headerYaml([{ name: 'Content-Type', value: 'application/json' }, tenant, corr]));
    L.push('  body:', '    type: json', '    data: |', block([
      '{',
      `  "username": "{{process.env.${userEnv}}}",`,
      `  "password": "{{process.env.${passEnv}}}",`,
      `  "deviceIdentifier": "qa-bruno-${role}",`,
      '  "deviceName": "QA Bruno CLI",',
      `  "platform": "${platform}",`,
      `  "channel": "${channel}",`,
      '  "rememberMe": false',
      '}',
    ].join('\n'), 6));
    L.push('runtime:');
    L.push(...scriptsYaml([
      {
        type: 'after-response',
        code: [
          'const body = res.getBody() || {};',
          'const data = body.data || body;',
          "bru.setVar('qaNextStep', String(data.nextStep == null ? '' : data.nextStep));",
          '// Đổi vai: xoá token/working context của vai trước để không chạy nhầm quyền.',
          "for (const k of ['workingContextId', 'workingOrganizationUnitId', 'temporaryToken', 'accessToken', 'refreshToken']) bru.setVar(k, '');",
          "if (data.continuationToken) bru.setVar('temporaryToken', data.continuationToken);",
          "if (data.accessToken) bru.setVar('accessToken', data.accessToken);",
          "if (data.refreshToken) bru.setVar('refreshToken', data.refreshToken);",
          `const wanted = ${cfg?.orgUnitEnv ? `bru.getProcessEnv('${cfg.orgUnitEnv}') || ''` : "''"};`,
          'const options = Array.isArray(data.workingContextOptions) ? data.workingContextOptions : [];',
          'const chosen = options.find((o) => wanted && String(o.workingOrganizationUnitId) === wanted) || options[0];',
          "if (chosen && chosen.workingOrganizationUnitId != null) bru.setVar('workingOrganizationUnitId', String(chosen.workingOrganizationUnitId));",
          'const ctx = data.currentContext && data.currentContext.workingOrganizationUnitId;',
          "if (ctx) bru.setVar('workingOrganizationUnitId', String(ctx));",
        ].join('\n'),
      },
      {
        type: 'tests',
        code: [
          "test('login trả 2xx', function () {",
          '  expect(res.getStatus()).to.be.within(200, 299);',
          '});',
          "test('login có continuationToken hoặc accessToken', function () {",
          "  expect(bru.getVar('temporaryToken') || bru.getVar('accessToken')).to.be.a('string').and.not.empty;",
          '});',
        ].join('\n'),
      },
    ]));
  } else if (req.kind === 'auth-select') {
    L.push('info:', `  name: ${yq(`Chọn đơn vị làm việc ${role}`)}`, '  type: http', `  seq: ${seq}`, '  tags:', '  - auth', '  - working-context');
    L.push('http:', '  method: POST', `  url: ${yq('{{baseURL}}/api/identity/v1/auth/working-organization-unit')}`);
    L.push(...headerYaml([{ name: 'Content-Type', value: 'application/json' }, tenant, corr]));
    L.push('  body:', '    type: json', '    data: |', block([
      '{',
      '  "temporaryToken": "{{temporaryToken}}",',
      '  "workingOrganizationUnitId": "{{workingOrganizationUnitId}}"',
      '}',
    ].join('\n'), 6));
    L.push('runtime:');
    L.push(...scriptsYaml([
      {
        type: 'before-request',
        code: [
          "const step = String(bru.getVar('qaNextStep') || '').toLowerCase();",
          "if (step !== 'workingcontextselectionrequired' && step !== '2') {",
          '  bru.runner.skipRequest();',
          '}',
        ].join('\n'),
      },
      {
        type: 'after-response',
        code: [
          'const body = res.getBody() || {};',
          'const data = body.data || body;',
          "if (data.accessToken) bru.setVar('accessToken', data.accessToken);",
          "if (data.refreshToken) bru.setVar('refreshToken', data.refreshToken);",
          "if (data.deviceId) bru.setVar('deviceId', data.deviceId);",
          "if (data.sessionId) bru.setVar('sessionId', data.sessionId);",
          'const ctx = data.currentContext && data.currentContext.workingOrganizationUnitId;',
          "if (ctx) bru.setVar('workingOrganizationUnitId', String(ctx));",
        ].join('\n'),
      },
      {
        type: 'tests',
        code: [
          "test('chọn đơn vị trả 2xx và có accessToken', function () {",
          '  expect(res.getStatus()).to.be.within(200, 299);',
          "  expect(bru.getVar('accessToken')).to.be.a('string').and.not.empty;",
          '});',
        ].join('\n'),
      },
    ]));
  } else {
    L.push('info:', `  name: ${yq(`Working context cơ sở ${role}`)}`, '  type: http', `  seq: ${seq}`, '  tags:', '  - auth', '  - working-contexts');
    L.push('http:', '  method: POST', `  url: ${yq('{{baseURL}}/api/identity/v1/working-contexts/facility')}`);
    L.push(...headerYaml([{ name: 'Content-Type', value: 'application/json' }, tenant, corr]));
    L.push('  body:', '    type: json', '    data: |', block([
      '{',
      '  "moduleCode": "{{moduleCode}}",',
      `  "facilityId": {{process.env.${cfg.facilityEnv}}}`,
      '}',
    ].join('\n'), 6));
    L.push('  auth:', '    type: bearer', `    token: ${yq('{{accessToken}}')}`);
    L.push('runtime:');
    L.push(...scriptsYaml([
      {
        type: 'before-request',
        code: [
          `if (!bru.getProcessEnv('${cfg.facilityEnv}')) {`,
          `  // Vai không khai ${cfg.facilityEnv} → không cần X-Working-Context-Id.`,
          '  bru.runner.skipRequest();',
          '}',
        ].join('\n'),
      },
      {
        type: 'after-response',
        code: [
          'const body = res.getBody() || {};',
          'const id = body.data ? body.data.workingContextId : body.workingContextId;',
          "if (typeof id === 'string' && id.length > 0) bru.setVar('workingContextId', id);",
        ].join('\n'),
      },
    ]));
    L.push(...assertionsYaml([
      { expression: 'res.status', operator: 'gte', value: '200' },
      { expression: 'res.status', operator: 'lte', value: '299' },
    ]));
  }
  L.push(...SETTINGS);
  L.push('docs: |-', block(`Máy sinh (bruno-runner own-API). Chuỗi đăng nhập 3 bước theo vai ${role} — nguồn: transport-erp/bruno/00-auth/*.`, 2));
  return `${L.join('\n')}\n`;
}

function capturesCode(captures) {
  if (!captures.length) return '';
  return [
    'const body = res.getBody();',
    READ_PATH_JS,
    ...captures.map((c, i) => [
      `const v${i} = readPath(body, ${JSON.stringify(c.path)});`,
      `if (v${i} !== undefined && v${i} !== null) bru.setVar(${JSON.stringify(c.name)}, v${i});`,
    ].join('\n')),
  ].join('\n');
}

export function renderRequestYaml(req, seq, meta = {}) {
  const L = [];
  const tags = ['qa', meta.feature, meta.chk].filter(Boolean);

  if (req.kind === 'igas') {
    const url = `{{igasSimulatorBaseURL}}/orders/by-code/${req.code}/${req.igasAction}`;
    L.push('info:', `  name: ${yq(`${meta.chk || ''} · B${req.step} IgasSimulator ${req.igasAction}`)}`, '  type: http', `  seq: ${seq}`);
    L.push('  tags:', ...[...tags, 'igas-simulator'].map((t) => `  - ${t}`));
    L.push('http:', '  method: POST', `  url: ${yq(url)}`);
    const headers = [{ name: 'X-Simulator-Key', value: '{{igasSimulatorApiKey}}', description: 'Khoá giả lập (IGAS_SIM_KEY trong qa/.env)' }];
    if (req.igasAction === 'pumped') headers.unshift({ name: 'Content-Type', value: 'application/json' });
    L.push(...headerYaml(headers));
    if (req.igasAction === 'pumped') {
      L.push('  body:', '    type: json', '    data: |-', block(`{\n  "liters": ${req.liters},\n  "nozzleCode": null\n}`, 6));
    }
    L.push('runtime:');
    const cap = capturesCode(req.captures || []);
    L.push(...scriptsYaml(cap ? [{ type: 'after-response', code: cap }] : []));
    L.push(...assertionsYaml(req.assertions || []));
    L.push(...SETTINGS);
    L.push('docs: |-', block(`Giả lập iGAS ${req.igasAction} theo mã lệnh (Tools/IgasSimulator/0${req.igasAction === 'pumped' ? 7 : 6}-*). Khoá chỉ qua biến môi trường.`, 2));
    return `${L.join('\n')}\n`;
  }

  L.push('info:', `  name: ${yq(`${meta.chk || ''} · B${req.step} ${req.method} ${req.path}`)}`, '  type: http', `  seq: ${seq}`);
  L.push('  tags:', ...tags.map((t) => `  - ${t}`));
  L.push('http:', `  method: ${req.method}`, `  url: ${yq(`{{baseURL}}${req.path.startsWith('/') ? req.path : `/${req.path}`}`)}`);
  const headers = [
    { name: 'X-Tenant-Id', value: '{{tenantId}}' },
    { name: 'X-Correlation-ID', value: '{{$guid}}', description: 'Request tracing ID' },
  ];
  if (req.body) headers.push({ name: 'Content-Type', value: 'application/json' });
  L.push(...headerYaml(headers));
  if (req.body) L.push('  body:', '    type: json', '    data: |-', block(req.body, 6));
  L.push('  auth:', '    type: bearer', `    token: ${yq('{{accessToken}}')}`);
  L.push('runtime:');
  const scripts = [{
    type: 'before-request',
    code: [
      "const wc = bru.getVar('workingContextId');",
      "if (wc) req.setHeader('X-Working-Context-Id', wc);",
    ].join('\n'),
  }];
  const cap = capturesCode(req.captures || []);
  if (cap) scripts.push({ type: 'after-response', code: cap });
  L.push(...scriptsYaml(scripts));
  L.push(...assertionsYaml(req.assertions || []));
  L.push(...SETTINGS);
  const docLines = [
    `Máy sinh từ ${meta.source || 'testcases'} — ${meta.chk || ''} bước ${req.step}. KHÔNG sửa tay (regen ghi đè).`,
  ];
  if (meta.ref) docLines.push(`Ref: ${meta.ref}`);
  if (meta.oracle) docLines.push(`Đáp án: ${meta.oracle}`);
  L.push('docs: |-', block(docLines.join('\n'), 2));
  return `${L.join('\n')}\n`;
}

export const AUTH_STEP_RE = /^\d+-auth-/;
export const IGAS_STEP_RE = /^\d+-igas-/;

export function requestFileName(req, seq) {
  const nn = String(seq).padStart(2, '0');
  if (req.kind === 'auth-login') return `${nn}-auth-${req.role}-login.yml`;
  if (req.kind === 'auth-select') return `${nn}-auth-${req.role}-select-working-context.yml`;
  if (req.kind === 'auth-facility') return `${nn}-auth-${req.role}-working-context-facility.yml`;
  if (req.kind === 'igas') return `${nn}-igas-${req.igasAction}.yml`;
  // Bước thường: NN-{method}-… — method không bao giờ là "auth"/"igas" nên không đụng AUTH_STEP_RE/IGAS_STEP_RE.
  return `${nn}-${req.method.toLowerCase()}-${slug(req.path.replace(/\{\{\s*([^}]+?)\s*\}\}/g, '$1'))}.yml`.slice(0, 120);
}

function opencollectionYaml(feature) {
  return [
    'opencollection: 1.0.0',
    '',
    'info:',
    `  name: ${yq(`${feature} — QA API (máy sinh)`)}`,
    'config:',
    '  proxy:',
    '    inherit: true',
    '    config:',
    '      protocol: http',
    '      hostname: ""',
    '      port: ""',
    '      auth:',
    '        username: ""',
    '        password: ""',
    '      bypassProxy: ""',
    '',
    'docs:',
    '  content: |',
    `    # ${feature} — QA API`,
    '',
    '    Máy sinh bởi `.claude/scripts/bruno-runner.mjs` từ test case **Target: api**. KHÔNG sửa tay —',
    '    sửa test case rồi `gen` lại. Mỗi thư mục `NNN-CHK-…` tự đăng nhập theo vai (3 bước như',
    '    `transport-erp/bruno/00-auth/`) rồi chạy các bước của TC; id bắt bằng `bru.setVar`.',
    '    Không chạy `--parallel`. Bí mật chỉ qua biến môi trường (`qa/.env`).',
    '  type: text/markdown',
    'bundled: false',
    'extensions:',
    '  bruno:',
    '    ignore:',
    '      - node_modules',
    '      - .git',
    '      - reports',
    '',
  ].join('\n');
}

function environmentYaml(name, cfg) {
  const vars = [
    ['baseURL', String(cfg.apiBase || '').replace(/\/+$/, ''), 'url'],
    ['tenantId', `{{process.env.${cfg.tenantIdEnv || 'QA_TENANT_ID'}}}`],
    ['moduleCode', cfg.moduleCode || 'fuel'],
    ['igasSimulatorBaseURL', '{{process.env.IGAS_SIM_BASE}}', 'url'],
    ['igasSimulatorApiKey', '{{process.env.IGAS_SIM_KEY}}'],
    ['temporaryToken', ''],
    ['workingOrganizationUnitId', ''],
    ['workingContextId', ''],
    ['accessToken', ''],
    ['refreshToken', ''],
    ['deviceId', ''],
    ['sessionId', ''],
    ['qaNextStep', ''],
  ];
  // dotEnvFilePath: bru đọc bruno-api/.env (gitignored) cho {{process.env.*}} bên cạnh qa/.env runner nạp sẵn.
  const L = [`name: ${name}`, 'dotEnvFilePath: .env', 'variables:'];
  for (const [n, v, type] of vars) {
    L.push(`  - name: ${n}`, `    value: ${JSON.stringify(v)}`);
    if (type) L.push(`    type: ${type}`);
  }
  return `${L.join('\n')}\n`;
}

// --dir → bố cục (testDir, apiDir, bảng, collection own).
export function detectLayout(dirArg) {
  if (!dirArg) fail('Thiếu --dir <path>. Ví dụ: --dir docs/fuel-issuing/test (hoặc docs/x/test/api cho chế độ bảng)');
  const dir = path.resolve(process.cwd(), dirArg);
  let testDir;
  let apiDir;
  if (path.basename(dir) === 'api' && path.basename(path.dirname(dir)) === 'test') {
    testDir = path.dirname(dir);
    apiDir = dir;
  } else if (fs.existsSync(path.join(dir, 'api-tests.md')) && !fs.existsSync(path.join(dir, 'testcases'))) {
    testDir = path.dirname(dir);
    apiDir = dir;
  } else {
    testDir = dir;
    apiDir = path.join(dir, 'api');
  }
  const tableFile = path.join(apiDir, 'api-tests.md');
  const hasTable = fs.existsSync(tableFile);
  const tcDir = path.join(testDir, 'testcases');
  const hasTestcases = fs.existsSync(tcDir) && fs.statSync(tcDir).isDirectory();
  const repoRoot = findRepoRoot(testDir);
  return {
    dir,
    testDir,
    apiDir,
    tableFile,
    hasTable,
    tcDir,
    hasTestcases,
    repoRoot,
    // Own-API (OpenCollection YAML) ở `bruno-api/`; bảng 3rd-party giữ `bruno/` như cũ — 2 collection tách hẳn,
    // không bao giờ dời chỗ nhau dù feature có cả hai.
    ownBrunoDir: path.join(apiDir, 'bruno-api'),
    tableBrunoDir: path.join(apiDir, 'bruno'),
    feature: deriveFeature(testDir),
  };
}

function collectOwnPlans(layout, qa) {
  const index = loadChecklistIndex(layout.testDir);
  const plans = [];
  const { entries } = loadTestcaseDir(layout.tcDir);
  for (const { scope, file, tc } of entries) {
    if (tcTarget(tc) !== 'api') continue;
    const oracle = tcOracle(tc, index);
    const plan = planApiTestcase(tc, { roles: qa.roles || undefined, oracle });
    plans.push({ scope, file, tc, chk: tc.chk || `TC-${tc.stt || 'UNKNOWN'}`, plan });
  }
  plans.sort((a, b) => a.chk.localeCompare(b.chk));
  return plans;
}

function ownFolderName(i, chk) {
  return `${String(i + 1).padStart(3, '0')}-${chk}`;
}

export function genOwn(layout, { quiet = false } = {}) {
  const feature = requireSlug(layout.feature, 'feature');
  const qa = loadQaConfig(layout.repoRoot);
  const plans = collectOwnPlans(layout, qa);
  const out = layout.ownBrunoDir;

  // Dọn thư mục TC cũ (máy sinh) — giữ environments/.env/reports do người dùng thêm.
  if (fs.existsSync(out)) {
    for (const f of fs.readdirSync(out)) {
      if (/^\d{3}-CHK-/i.test(f) || /^\d{3}-TC-/i.test(f)) fs.rmSync(path.join(out, f), { recursive: true, force: true });
    }
  }
  fs.mkdirSync(path.join(out, 'environments'), { recursive: true });
  fs.writeFileSync(path.join(out, 'opencollection.yml'), opencollectionYaml(feature));
  fs.writeFileSync(path.join(out, '.gitignore'), '.env\nreports/\n.bruno-report-*\n');

  const envs = qa.envs || { dev: { apiBase: 'https://api-dev-erp.innvie.vn', tenantIdEnv: 'QA_TENANT_ID' } };
  for (const [name, cfg] of Object.entries(envs)) {
    if (isProdEnvName(name) || !cfg?.apiBase) continue;
    fs.writeFileSync(path.join(out, 'environments', `${name}.yml`), environmentYaml(name, cfg));
  }

  const envNames = new Set(['QA_ENV', 'QA_TENANT_ID']);
  const dataDefaults = new Map();
  const ready = [];
  const skipped = [];

  plans.forEach((p, i) => {
    if (!p.plan.ready) {
      skipped.push({ chk: p.chk, scope: p.scope, reason: p.plan.reasons[0] || 'chưa sẵn sàng', reasons: p.plan.reasons });
      return;
    }
    const folder = ownFolderName(ready.length, p.chk);
    const fdir = path.join(out, folder);
    fs.mkdirSync(fdir, { recursive: true });
    fs.writeFileSync(path.join(fdir, 'folder.yml'), [
      'info:',
      `  name: ${yq(`${p.chk} — ${cleanValue(p.tc.title) || p.scope}`)}`,
      '  type: folder',
      `  seq: ${ready.length + 1}`,
      'docs: |',
      block([
        `# ${p.chk}`,
        '',
        `Nguồn: testcases-${p.scope}.md · Ref: ${cleanValue(p.tc.ref) || '—'} · Đáp án: ${p.plan.oracle?.label || '—'}`,
        `Vai: ${p.plan.roles.join(', ') || '—'}${p.plan.dataKeys.length ? ` · Dữ liệu tiền đề: ${p.plan.dataKeys.join(', ')}` : ''}`,
      ].join('\n'), 2),
      '',
    ].join('\n'));

    p.plan.requests.forEach((req, j) => {
      const seq = j + 1;
      const yaml = req.kind.startsWith('auth-')
        ? renderAuthRequest(req, seq)
        : renderRequestYaml(req, seq, {
          feature, chk: p.chk, ref: cleanValue(p.tc.ref), oracle: p.plan.oracle?.label, source: `testcases-${p.scope}.md`,
        });
      fs.writeFileSync(path.join(fdir, requestFileName(req, seq)), yaml);
      if (req.cfg) for (const k of ['userEnv', 'passEnv', 'orgUnitEnv', 'facilityEnv']) if (req.cfg[k]) envNames.add(req.cfg[k]);
    });
    if (p.plan.usesIgas) { envNames.add('IGAS_SIM_BASE'); envNames.add('IGAS_SIM_KEY'); }
    for (const k of p.plan.dataKeys) dataDefaults.set(`@data.${k}`, '');
    ready.push({ ...p, folder });
  });

  fs.writeFileSync(path.join(out, '.env.example'), [
    '# Chỉ TÊN biến (giá trị để qa/.env hoặc bruno-api/.env — gitignored). Không commit bí mật.',
    ...[...envNames].sort().map((k) => `${k}=`),
    '',
  ].join('\n'));
  writeTestData(layout.apiDir, dataDefaults);
  writeApiIndex(layout, feature, ready, skipped, new Map());

  if (!quiet) {
    console.log(`gen own-API: ${ready.length} TC → ${path.relative(process.cwd(), out)}/ (OpenCollection YAML); skip ${skipped.length}`);
    for (const s of skipped) console.log(`   ⏭  ${s.scope} · ${s.chk} · ${s.reasons.join('; ')}`);
  }
  return { ready, skipped, plans, envNames: [...envNames].sort(), brunoDir: out };
}

function writeApiIndex(layout, feature, ready, skipped, results) {
  const day = today();
  const rows = ready.map((p) => {
    const r = results.get(p.chk.toLowerCase());
    const steps = p.plan.requests.filter((q) => !q.kind.startsWith('auth-')).length;
    return `| ${p.chk} | [${p.folder}](bruno-api/${p.folder}) | ${p.plan.roles.join(', ') || '—'} | ${steps} | ${p.plan.oracle?.label || '—'} | ${r ? r.status : '—'} | ${r ? r.at.slice(0, 10) : '—'} |`;
  });
  const skip = skipped.map((s) => `| ${s.scope} | ${s.chk} | ${s.reasons.join('; ')} |`);
  const md = `---
type: api-test-index
feature: ${feature}
status: draft
updated: ${day}
links:
  - docs/${feature}/test/testcases/${feature}-testcase-index.md
---

# API test (Bruno) — ${feature}

> Máy sinh từ test case **Target: api** (\`bruno-runner.mjs gen --dir docs/${feature}/test\`). Sửa test case rồi gen lại — không sửa YAML tay.
> Kết quả chuẩn hoá: \`docs/${feature}/test/results/latest.json\`.

## Test cases

| CHK-ID | Thư mục | Vai | Bước | Đáp án | Kết quả gần nhất | Chạy lúc |
|--------|---------|-----|------|--------|------------------|----------|
${rows.join('\n') || '| — | — | — | 0 | — | — | — |'}

## Skipped (không sinh — manual/TBD/grammar chưa map được)

| Scope | CHK-ID | Lý do |
|-------|--------|-------|
${skip.join('\n') || '| — | — | — |'}
`;
  fs.mkdirSync(layout.apiDir, { recursive: true });
  fs.writeFileSync(path.join(layout.apiDir, `${feature}-api-index.md`), md);
}

// Gom kết quả 1 thư mục TC → { raw:'PASS'|'FAIL'|'PENDING', kind, note }
export function aggregateTcItems(items) {
  const live = (items || []).filter((it) => !['skipped', 'skip'].includes(String(it.status || '').toLowerCase()) && !it.skipped);
  if (!live.length) return { raw: 'PENDING', kind: '', note: 'bru không trả kết quả cho TC này' };
  const evaluated = live.map((it) => ({ it, c: classify(it), file: String(it.test?.filename || it.suitename || it.request?.url || '') }));
  if (evaluated.every((e) => e.c.connectionRefused)) {
    return { raw: 'PENDING', kind: '', note: 'môi trường chưa sẵn sàng (connection refused)' };
  }
  const failed = evaluated.find((e) => !e.c.pass);
  if (!failed) return { raw: 'PASS', kind: '', note: '' };

  const file = failed.file;
  const status = String(failed.c.status || '');
  const where = path.basename(file) || file;
  // Phân loại theo TÊN FILE (basename) neo đầu: NN-auth-… / NN-igas-… (requestFileName). Bước thường luôn là
  // NN-{method}-… nên không bao giờ khớp — kể cả khi path chứa "auth" (vd 04-post-api-identity-v1-auth-login).
  const base = path.basename(file);
  if (AUTH_STEP_RE.test(base)) {
    const role = (base.match(/^\d+-auth-([a-z0-9-]+?)-(?:login|select-working-context|working-context-facility)\.ya?ml$/) || [])[1] || '?';
    return { raw: 'FAIL', kind: 'data', note: `đăng nhập vai ${role} lỗi (HTTP ${status || '-'}) — kiểm tài khoản/quyền trong qa/.env` };
  }
  if (IGAS_STEP_RE.test(base)) {
    if (failed.c.connectionRefused) return { raw: 'PENDING', kind: '', note: 'IgasSimulator không tới được (IGAS_SIM_BASE?)' };
    return { raw: 'FAIL', kind: 'app', note: `giả lập iGAS rớt (HTTP ${status || '-'}) ở ${where}: ${failed.c.reason}` };
  }
  if (failed.c.connectionRefused) return { raw: 'PENDING', kind: '', note: `không tới được API ở ${where}` };
  if (/^(401|403)$/.test(status)) {
    return { raw: 'FAIL', kind: 'data', note: `HTTP ${status} ở ${where} — nghi tài khoản/quyền/vai (kênh Mobile cho tạo phiếu?)` };
  }
  const usesDataVar = /\{\{data_/.test(JSON.stringify(failed.it.request || {})) || /data_/.test(String(failed.it.request?.url || ''));
  if (status === '404' && usesDataVar) {
    return { raw: 'FAIL', kind: 'data', note: `HTTP 404 ở ${where} — dữ liệu tiền đề không tồn tại trên môi trường` };
  }
  return { raw: 'FAIL', kind: 'app', note: `${where}: ${failed.c.reason || `HTTP ${status}`}` };
}

export function runOwn(layout, args, { bru } = {}) {
  const qa = loadQaConfig(layout.repoRoot);
  const g = genOwn(layout, { quiet: true });
  const feature = layout.feature;
  const spawnEnv = {
    ...process.env,
    ...loadDotEnv(path.join(qa.qaDir, '.env')),
    ...loadDotEnv(path.join(layout.ownBrunoDir, '.env')),
  };
  const envName = args.env || spawnEnv.QA_ENV || 'dev';
  if (isProdEnvName(envName)) {
    console.error(`✋ Từ chối chạy own-API trên "${envName}" — QA chỉ chạy dev/sit/local.`);
    return 2;
  }
  if (qa.envs && !qa.envs[envName]) {
    console.error(`✋ Môi trường "${envName}" không có trong qa/config/envs.json — không chạy tới host lạ.`);
    return 2;
  }

  let targets = g.ready;
  if (args.tc) {
    const wanted = new Set(args.tc.map((s) => s.toLowerCase()));
    targets = g.ready.filter((p) => wanted.has(p.chk.toLowerCase()));
    if (!targets.length) { console.error('Không TC nào khớp --tc'); return 2; }
  }

  const testdata = (() => {
    try { return JSON.parse(fs.readFileSync(path.join(layout.apiDir, 'testdata.json'), 'utf8')) || {}; } catch { return {}; }
  })();
  const fingerprint = dataFingerprint(testdata);
  const history = loadRunHistory(layout.apiDir);
  const at = new Date().toISOString();
  const build = spawnEnv.QA_BUILD || '';
  const entries = [];
  const statusMap = {};
  const bruInfo = bru === undefined ? resolveBru(layout.repoRoot, spawnEnv) : bru;

  const pending = (p, note) => entries.push({ chk: p.chk, target: 'api', status: 'PENDING', env: envName, build, at, note });

  for (const p of targets) {
    const missing = [];
    const tenantEnv = qa.envs?.[envName]?.tenantIdEnv || 'QA_TENANT_ID';
    if (!spawnEnv[tenantEnv]) missing.push(tenantEnv);
    for (const req of p.plan.requests) {
      if (req.kind === 'auth-login') for (const k of ['userEnv', 'passEnv']) if (req.cfg?.[k] && !spawnEnv[req.cfg[k]]) missing.push(req.cfg[k]);
    }
    if (p.plan.usesIgas) for (const k of ['IGAS_SIM_BASE', 'IGAS_SIM_KEY']) if (!spawnEnv[k]) missing.push(k);
    const missingData = p.plan.dataKeys.filter((k) => !String(testdata[`@data.${k}`] ?? ''));

    if (!bruInfo) { pending(p, 'bru chưa cài — `npm i -g @usebruno/cli` hoặc `cd qa && npm install` (runner không tải mạng)'); continue; }
    if (missing.length) { pending(p, `thiếu biến môi trường: ${[...new Set(missing)].join(', ')} (qa/.env)`); continue; }
    if (missingData.length) { pending(p, `thiếu dữ liệu tiền đề: ${missingData.join(', ')} (test/api/testdata.json "@data.<key>")`); continue; }

    const envVars = {};
    for (const k of p.plan.dataKeys) envVars[dataVarName(k)] = String(testdata[`@data.${k}`]);
    const { items, launchErr } = runBru({ bin: bruInfo.bin, args: [] }, layout.ownBrunoDir, p.folder, envName, envVars, spawnEnv);
    if (launchErr) { pending(p, `không gọi được bru: ${launchErr.message}`); continue; }

    const agg = aggregateTcItems(items);
    const r = classifyResult({ status: agg.raw, kind: agg.kind, oracle: p.plan.oracle, prev: history[p.chk], fingerprint });
    statusMap[p.chk] = agg.raw;
    entries.push({ chk: p.chk, target: 'api', status: r.status, env: envName, build, at, note: [agg.note, r.status === agg.raw ? '' : r.note].filter(Boolean).join(' — ') });
  }
  for (const s of g.skipped) {
    entries.push({ chk: s.chk, target: 'api', status: 'PENDING', env: envName, build, at, note: `chưa sinh: ${s.reason}` });
  }

  if (Object.keys(statusMap).length) saveRunHistory(layout.apiDir, updateRunHistory(history, statusMap, fingerprint));
  const written = writeNormalizedResults(layout.testDir, entries);
  const resMap = new Map(written.filter((e) => e.target === 'api').map((e) => [e.chk.toLowerCase(), e]));
  writeApiIndex(layout, feature, g.ready, g.skipped, resMap);

  const icon = { PASS: '✅', FAIL_APP: '🔴', FAIL_DATA: '🟡', FAIL_OUTDATE: '🟠', FAIL_DOC: '🟣', PENDING: '⏳' };
  console.log(`\n=== api-test own-API (Bruno, env=${envName}, ${bruInfo ? `bru ${bruInfo.version || ''}`.trim() : 'bru chưa cài'}) ===`);
  for (const e of entries) console.log(`${icon[e.status] || ''} ${e.chk}  ${e.status}${e.note ? `  ← ${e.note}` : ''}`);
  const count = (s) => entries.filter((e) => e.status === s).length;
  console.log(`\n✅${count('PASS')} 🔴${count('FAIL_APP')} 🟣${count('FAIL_DOC')} 🟡${count('FAIL_DATA')} 🟠${count('FAIL_OUTDATE')} ⏳${count('PENDING')}`);
  console.log(`🧾 Kết quả chuẩn hoá: ${path.relative(process.cwd(), path.join(layout.testDir, 'results', 'latest.json'))}`);
  return entries.some((e) => e.status.startsWith('FAIL_')) ? 1 : 0;
}

function ownApiAvailable(layout) {
  if (!layout.hasTestcases) return false;
  try {
    return loadTestcaseDir(layout.tcDir).entries.some((e) => tcTarget(e.tc) === 'api');
  } catch {
    return false;
  }
}

export function selectModes(layout, kind) {
  if (kind === 'own') return { own: true, table: false };
  if (kind === 'table') return { own: false, table: true };
  return { own: ownApiAvailable(layout), table: layout.hasTable };
}

// Chạy các chế độ đã chọn; exit code = max của CHỈ các chế độ thực sự chạy.
// Tự phát hiện (không --mode) + có cả bảng: own-API chỉ chạy khi env (--env > QA_ENV > dev) có trong qa/config/envs.json
// (env của bảng — mock/sandbox/… — không phải env QA) → in 1 dòng bỏ qua thay vì báo lỗi.
export function runModes(layout, args, modes, { runTableFn = runTable, runOwnFn = runOwn } = {}) {
  const codes = [];
  if (modes.table) codes.push(runTableFn(layout, args));
  if (modes.own) {
    let skip = '';
    if (!args.kind && modes.table) {
      const qa = loadQaConfig(layout.repoRoot);
      const fileEnv = loadDotEnv(path.join(qa.qaDir, '.env'));
      const envName = args.env || process.env.QA_ENV || fileEnv.QA_ENV || 'dev';
      if (qa.envs && !qa.envs[envName]) skip = envName;
    }
    if (skip) console.log(`⏭  own-API bỏ qua: env "${skip}" không có trong qa/config/envs.json (chạy riêng: --mode own --env dev|sit|local)`);
    else codes.push(runOwnFn(layout, args));
  }
  return codes.length ? Math.max(...codes) : 0;
}

// ---------- main ----------
const isMain = Boolean(process.argv[1]) && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMain) {
  const args = parseArgs(process.argv);
  try {
    const layout = detectLayout(args.dir);
    const modes = selectModes(layout, args.kind);
    if (!modes.own && !modes.table) {
      fail(`Không có gì để chạy: không thấy ${path.relative(process.cwd(), layout.tableFile)} và không có test case Target api trong ${path.relative(process.cwd(), layout.tcDir)}`);
    }
    if (args.mode === 'gen') {
      if (modes.table) {
        const { rows, manual, BRUNO_DIR } = genTable(layout);
        console.log(`gen: sinh ${rows.length - manual.length} request .bru vào ${path.relative(process.cwd(), BRUNO_DIR)}/`);
        if (manual.length) console.log(`bỏ qua (multi-step/side-effect, chạy thủ công): ${manual.map((r) => r.tc).join(', ')}`);
      }
      if (modes.own) genOwn(layout);
    } else if (args.mode === 'run') {
      process.exit(runModes(layout, args, modes));
    } else {
      console.error(`mode lạ: ${args.mode} (dùng 'gen' hoặc 'run')`);
      process.exit(2);
    }
  } catch (err) {
    console.error(`❌ bruno-runner: ${err instanceof CliError ? err.message : (err?.stack || err)}`);
    process.exit(1);
  }
}

export { CliError, readTable, emitBru, assertBody, readNormalizedResults };
