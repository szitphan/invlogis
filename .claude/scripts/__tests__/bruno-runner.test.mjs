// node --test .claude/scripts/__tests__/bruno-runner.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

import * as br from '../bruno-runner.mjs';
import { parseTestcasesFile } from '../testgen-core.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.resolve(HERE, '..', 'bruno-runner.mjs');
const FIX = path.join(HERE, 'fixtures', 'testgen');
const FAKE_BRU = path.join(FIX, 'reports', 'bruno-fake.mjs');

function copy(name) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'brgen-'));
  fs.cpSync(path.join(FIX, name), dir, { recursive: true });
  return dir;
}
const cli = (args, opts = {}) => spawnSync(process.execPath, [SCRIPT, ...args], { encoding: 'utf8', ...opts });
const roles = JSON.parse(fs.readFileSync(path.join(FIX, 'repo', 'qa', 'config', 'roles.json'), 'utf8'));
const tcList = () => parseTestcasesFile(fs.readFileSync(path.join(FIX, 'repo', 'docs', 'fuel-demo', 'test', 'testcases', 'testcases-flow-a.md'), 'utf8'));

// Silence console during in-process runOwn calls.
function quiet(fn) {
  const { log, error } = console;
  console.log = () => {};
  console.error = () => {};
  try { return fn(); } finally { console.log = log; console.error = error; }
}

test('import an toàn (không exit, không in)', () => {
  const r = spawnSync(process.execPath, ['--input-type=module', '-e', `import(${JSON.stringify(SCRIPT)}).then(() => console.log('OK'))`], { encoding: 'utf8' });
  assert.equal(r.status, 0, r.stderr);
  assert.equal(r.stdout.trim(), 'OK');
});

test('parseApiAction: METHOD path, tiền tố vai, IgasSimulator', () => {
  assert.deepEqual(br.parseApiAction('POST /api/x/{{id}}/submit'), { role: '', kind: 'http', method: 'POST', path: '/api/x/{{id}}/submit' });
  assert.equal(br.parseApiAction('[vai: approver] GET /api/a').role, 'approver');
  const pumped = br.parseApiAction('Giả lập bơm pumped {{authorizationCode}} 48,5 lít');
  assert.equal(pumped.kind, 'igas');
  assert.equal(pumped.igasAction, 'pumped');
  assert.equal(pumped.code, '{{authorizationCode}}');
  assert.equal(pumped.liters, 48.5);
  assert.equal(br.parseApiAction('Giả lập bơm in-use "123456"').code, '123456');
  assert.ok(br.parseApiAction('Gọi API tạo phiếu').error);
  assert.ok(br.parseApiAction('POST api/no-slash').error);
});

test('parseApiExpected: status, 2xx, errorCode, body, capture, exists, unmapped', () => {
  const e = br.parseApiExpected('HTTP 201\nbody.data.status = "draft"; errorCode = "X.Y"\nlưu data.id → fuelDispensingId\ndata.items[0].code tồn tại\nThành công');
  assert.equal(e.hasStatus, true);
  assert.deepEqual(e.assertions[0], { expression: 'res.status', operator: 'eq', value: '201' });
  assert.deepEqual(e.assertions[1], { expression: 'res.body.data.status', operator: 'eq', value: '"draft"' });
  assert.deepEqual(e.assertions[2], { expression: 'res.body.errorCode', operator: 'eq', value: '"X.Y"' });
  assert.deepEqual(e.captures, [{ path: 'data.id', name: 'fuelDispensingId' }]);
  assert.equal(e.assertions[3].operator, 'isDefined');
  assert.deepEqual(e.unmapped, ['Thành công']);
  const r = br.parseApiExpected('HTTP 2xx; data.version >= 2');
  assert.deepEqual(r.assertions.map((a) => a.operator), ['gte', 'lte', 'gte']);
  assert.equal(r.assertions[2].value, '2');
});

test('planApiTestcase: chuỗi auth theo vai (đổi vai giữa chừng), data var, igas', () => {
  const tc = tcList().find((t) => t.chk === 'CHK-fuel-demo-002');
  const plan = br.planApiTestcase(tc, { roles });
  assert.equal(plan.ready, true, plan.reasons.join('; '));
  assert.deepEqual(plan.requests.map((r) => r.kind), [
    'auth-login', 'auth-select', 'auth-facility', 'http', 'http', 'igas', 'auth-login', 'auth-select', 'http',
  ]);
  assert.deepEqual(plan.roles, ['requester-mobile', 'approver']);
  assert.deepEqual(plan.dataVars, ['data_xe_noi_bo']);
  assert.equal(plan.usesIgas, true);

  const bad = br.planApiTestcase(tcList().find((t) => t.chk === 'CHK-fuel-demo-007'), { roles });
  assert.equal(bad.ready, false);
  const noRole = br.planApiTestcase({ ...tc, role: '', preconditions: '—' }, { roles });
  assert.ok(noRole.reasons.some((r) => /API cần \*\*Role:\*\*/.test(r)));
});

test('render: login Mobile/Android, facility skip theo env, header working context, capture', () => {
  const login = br.renderAuthRequest({ kind: 'auth-login', role: 'requester-mobile', cfg: roles['requester-mobile'] }, 1);
  assert.match(login, /"channel": "Mobile"/);
  assert.match(login, /"platform": "Android"/);
  assert.match(login, /\{\{process\.env\.QA_REQUESTER_MOBILE_PASS\}\}/);
  assert.match(login, /url: '\{\{baseURL\}\}\/api\/identity\/v1\/auth\/login'/);
  const web = br.renderAuthRequest({ kind: 'auth-login', role: 'approver', cfg: roles.approver }, 1);
  assert.match(web, /"channel": "Web"/);
  assert.match(web, /"platform": "Web"/);
  const sel = br.renderAuthRequest({ kind: 'auth-select', role: 'approver', cfg: roles.approver }, 2);
  assert.match(sel, /workingcontextselectionrequired/);
  assert.match(sel, /bru\.runner\.skipRequest\(\)/);
  const fac = br.renderAuthRequest({ kind: 'auth-facility', role: 'requester-mobile', cfg: roles['requester-mobile'] }, 3);
  assert.match(fac, /\/api\/identity\/v1\/working-contexts\/facility/);
  assert.match(fac, /getProcessEnv\('QA_REQUESTER_MOBILE_FACILITY'\)/);

  const req = br.renderRequestYaml({
    kind: 'http', step: '1', method: 'POST', path: '/api/a', body: '{"x": {{data_k}}}',
    assertions: [{ expression: 'res.status', operator: 'eq', value: '201' }], captures: [{ path: 'data.id', name: 'aId' }],
  }, 4, { chk: 'CHK-x-001', feature: 'x' });
  assert.match(req, /req\.setHeader\('X-Working-Context-Id', wc\)/);
  assert.match(req, /bru\.setVar\("aId", v0\)/);
  assert.match(req, /type: bearer/);
  assert.match(req, /value: '201'/);
});

test('gen own-API: OpenCollection YAML, environments từ envs.json, .env.example chỉ tên', () => {
  const repo = copy('repo');
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  const r = cli(['gen', '--dir', dir]);
  assert.equal(r.status, 0, r.stderr);
  const out = path.join(dir, 'api', 'bruno-api');
  assert.equal(fs.existsSync(path.join(dir, 'api', 'bruno')), false, 'own-API không ghi vào bruno/ (của bảng 3rd-party)');
  assert.match(fs.readFileSync(path.join(out, 'opencollection.yml'), 'utf8'), /^opencollection: 1\.0\.0/);
  assert.deepEqual(fs.readdirSync(path.join(out, 'environments')).sort(), ['dev.yml', 'local.yml']);
  const devEnv = fs.readFileSync(path.join(out, 'environments', 'dev.yml'), 'utf8');
  assert.match(devEnv, /value: "https:\/\/api-dev-erp\.innvie\.vn"/);
  assert.match(devEnv, /\{\{process\.env\.IGAS_SIM_KEY\}\}/);
  assert.match(devEnv, /^dotEnvFilePath: \.env$/m);
  const folders = fs.readdirSync(out).filter((f) => /^\d{3}-/.test(f)).sort();
  assert.deepEqual(folders, ['001-CHK-fuel-demo-002', '002-CHK-fuel-demo-006']);
  const files = fs.readdirSync(path.join(out, folders[0])).sort();
  assert.ok(files.includes('06-igas-pumped.yml'));
  assert.ok(files.includes('07-auth-approver-login.yml'));
  // Tên file: chỉ bước auth/igas bắt đầu bằng NN-auth- / NN-igas-; bước thường là NN-{method}-…
  for (const f of files.filter((x) => x.endsWith('.yml') && x !== 'folder.yml')) {
    const special = br.AUTH_STEP_RE.test(f) || br.IGAS_STEP_RE.test(f);
    assert.ok(special || /^\d+-(get|post|put|patch|delete)-/.test(f), f);
  }
  const login = fs.readFileSync(path.join(out, folders[0], '07-auth-approver-login.yml'), 'utf8');
  assert.match(login, /\['workingContextId', 'workingOrganizationUnitId', 'temporaryToken'/, 'đổi vai xoá cả đơn vị làm việc');
  assert.match(fs.readFileSync(path.join(dir, 'api', 'fuel-demo-api-index.md'), 'utf8'), /\]\(bruno-api\/001-CHK-fuel-demo-002\)/);
  const envEx = fs.readFileSync(path.join(out, '.env.example'), 'utf8');
  for (const k of ['QA_TENANT_ID', 'QA_REQUESTER_MOBILE_USER', 'QA_APPROVER_PASS', 'IGAS_SIM_KEY']) assert.match(envEx, new RegExp(`^${k}=$`, 'm'));
  assert.doesNotMatch(envEx, /=\S/);
  const td = JSON.parse(fs.readFileSync(path.join(dir, 'api', 'testdata.json'), 'utf8'));
  assert.deepEqual(td, { '@data.xe-noi-bo': '' });
  assert.match(fs.readFileSync(path.join(dir, 'api', 'fuel-demo-api-index.md'), 'utf8'), /CHK-fuel-demo-007/);
});

test('run own-API không có bru → PENDING "bru chưa cài", exit 0', () => {
  const repo = copy('repo');
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  const layout = br.detectLayout(dir);
  const code = quiet(() => br.runOwn(layout, { env: 'dev' }, { bru: null }));
  assert.equal(code, 0);
  const latest = JSON.parse(fs.readFileSync(path.join(dir, 'results', 'latest.json'), 'utf8'));
  const e2 = latest.find((e) => e.chk === 'CHK-fuel-demo-002');
  assert.equal(e2.status, 'PENDING');
  assert.equal(e2.target, 'api');
  assert.match(e2.note, /bru chưa cài/);
  assert.match(latest.find((e) => e.chk === 'CHK-fuel-demo-007').note, /chưa sinh/);
});

test('run own-API (bru giả): PASS + FAIL_DOC (đáp án tái lập), thiếu dữ liệu → PENDING, từ chối prod', () => {
  const repo = copy('repo');
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  const layout = br.detectLayout(dir);
  const saved = { ...process.env };
  Object.assign(process.env, {
    QA_TENANT_ID: 't', QA_REQUESTER_MOBILE_USER: 'u', QA_REQUESTER_MOBILE_PASS: 'p',
    QA_APPROVER_USER: 'u2', QA_APPROVER_PASS: 'p2', IGAS_SIM_BASE: 'http://sim.local', IGAS_SIM_KEY: 'k',
  });
  try {
    // Lần 1: thiếu @data.xe-noi-bo → CHK-002 PENDING
    quiet(() => br.runOwn(layout, { env: 'dev' }, { bru: { bin: FAKE_BRU, version: 'fake' } }));
    let latest = JSON.parse(fs.readFileSync(path.join(dir, 'results', 'latest.json'), 'utf8'));
    assert.equal(latest.find((e) => e.chk === 'CHK-fuel-demo-002').status, 'PENDING');
    assert.match(latest.find((e) => e.chk === 'CHK-fuel-demo-002').note, /thiếu dữ liệu tiền đề: xe-noi-bo/);

    fs.writeFileSync(path.join(dir, 'api', 'testdata.json'), JSON.stringify({ '@data.xe-noi-bo': '362387869791001' }));
    const code = quiet(() => br.runOwn(layout, { env: 'dev' }, { bru: { bin: FAKE_BRU, version: 'fake' } }));
    assert.equal(code, 1);
    latest = JSON.parse(fs.readFileSync(path.join(dir, 'results', 'latest.json'), 'utf8'));
    assert.equal(latest.find((e) => e.chk === 'CHK-fuel-demo-002').status, 'PASS');
    assert.equal(latest.find((e) => e.chk === 'CHK-fuel-demo-006').status, 'FAIL_DOC');
    const hist = JSON.parse(fs.readFileSync(path.join(dir, 'api', 'run-history.json'), 'utf8'));
    assert.equal(hist['CHK-fuel-demo-002'].lastStatus, 'PASS');
    assert.match(fs.readFileSync(path.join(dir, 'api', 'fuel-demo-api-index.md'), 'utf8'), /CHK-fuel-demo-002 .*\| PASS \|/);

    assert.equal(quiet(() => br.runOwn(layout, { env: 'prod' }, { bru: null })), 2);
    assert.equal(quiet(() => br.runOwn(layout, { env: 'staging' }, { bru: null })), 2, 'env không có trong envs.json');
  } finally {
    for (const k of Object.keys(process.env)) if (!(k in saved)) delete process.env[k];
    Object.assign(process.env, saved);
  }
});

test('aggregateTcItems: auth rớt = FAIL_DATA-kind, refused = PENDING, 403 = data', () => {
  const ok = { status: 'pass', response: { status: 200 }, assertionResults: [{ status: 'pass' }], test: { filename: 'f/04-post-a.yml' } };
  assert.equal(br.aggregateTcItems([ok]).raw, 'PASS');
  const authFail = { status: 'fail', response: { status: 401 }, assertionResults: [], testResults: [{ status: 'fail', description: 'login' }], test: { filename: 'f/01-auth-approver-login.yml' } };
  const a = br.aggregateTcItems([authFail, ok]);
  assert.equal(a.kind, 'data');
  assert.match(a.note, /vai approver/);
  const refused = { error: 'connect ECONNREFUSED', test: { filename: 'f/01-auth-approver-login.yml' } };
  assert.equal(br.aggregateTcItems([refused]).raw, 'PENDING');
  const forbidden = { status: 'fail', response: { status: 403 }, assertionResults: [{ status: 'fail', lhsExpr: 'res.status', operator: 'eq', rhsExpr: '201' }], test: { filename: 'f/04-post-a.yml' } };
  assert.equal(br.aggregateTcItems([ok, forbidden]).kind, 'data');
  const skippedOnly = { status: 'skipped', test: { filename: 'f/02-auth-x-select-working-context.yml' } };
  assert.equal(br.aggregateTcItems([skippedOnly]).raw, 'PENDING');

  // Bước thường có "auth"/"igas" trong path KHÔNG bị coi là bước đăng nhập / giả lập (neo basename ^NN-auth-).
  const pathHasAuth = { status: 'fail', response: { status: 500 }, assertionResults: [{ status: 'fail', lhsExpr: 'res.status', operator: 'eq', rhsExpr: '200' }], test: { filename: 'x-auth-y/04-post-api-identity-v1-auth-login.yml' } };
  const r1 = br.aggregateTcItems([ok, pathHasAuth]);
  assert.equal(r1.kind, 'app');
  assert.doesNotMatch(r1.note, /đăng nhập vai/);
  const pathHasIgas = { status: 'fail', response: { status: 500 }, assertionResults: [{ status: 'fail' }], test: { filename: '003-CHK-a-igas-001/05-get-api-fuel-igas-codes.yml' } };
  assert.doesNotMatch(br.aggregateTcItems([pathHasIgas]).note, /giả lập iGAS/);
  const igasFail = { status: 'fail', response: { status: 500 }, assertionResults: [{ status: 'fail' }], test: { filename: 'f/05-igas-pumped.yml' } };
  assert.match(br.aggregateTcItems([igasFail]).note, /giả lập iGAS/);
  assert.equal(br.requestFileName({ kind: 'http', method: 'POST', path: '/api/identity/v1/auth/login' }, 4), '04-post-api-identity-v1-auth-login.yml');
});

test('table mode: hành vi cũ + --tc luôn kèm _setup', () => {
  const root = copy('table');
  const apiDir = path.join(root, 'docs', 'paydemo', 'test', 'api');
  const r = cli(['gen', '--dir', apiDir]);
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stdout, /gen: sinh 2 request \.bru/);
  assert.ok(fs.existsSync(path.join(apiDir, 'bruno', '_setup', 'login.bru')));
  assert.ok(fs.existsSync(path.join(apiDir, 'bruno', 'own', 'TC-01-post-auth-login.bru')));

  const layout = br.detectLayout(apiDir);
  const g = br.genTable(layout);
  assert.deepEqual(br.tableTargets(g, ['TC-02'], null), ['_setup', 'own/TC-02-get-orders.bru']);
  assert.deepEqual(br.tableTargets(g, ['TC-99'], null), []);
  assert.deepEqual(br.tableTargets(g, null, null), ['_setup', 'own']);

  const pend = { A: { connectionRefused: true }, B: { connectionRefused: true } };
  assert.equal(br.derivePending(pend), true);
  assert.equal(br.classify({ suitename: 'TC-01 x', response: { status: 200 }, assertionResults: [{ status: 'pass' }] }).pass, true);
  assert.equal(br.classifyTableResult({ pass: false, status: 403 }, null, '').status, 'FAIL_DATA');
  assert.equal(br.classifyTableResult({ pass: false, status: 500 }, null, '').status, 'FAIL_APP');
});

test('layout: own-API ở bruno-api/, bảng giữ bruno/ khi có cả 2; runModes bỏ own khi env không thuộc qa', () => {
  const repo = copy('repo');
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  const l1 = br.detectLayout(dir);
  assert.equal(l1.apiDir, path.join(dir, 'api'));
  assert.deepEqual(br.selectModes(l1), { own: true, table: false });
  fs.mkdirSync(path.join(dir, 'api'), { recursive: true });
  fs.copyFileSync(path.join(FIX, 'table', 'docs', 'paydemo', 'test', 'api', 'api-tests.md'), path.join(dir, 'api', 'api-tests.md'));
  const l2 = br.detectLayout(path.join(dir, 'api'));
  assert.equal(l2.testDir, dir);
  assert.deepEqual(br.selectModes(l2), { own: true, table: true });
  assert.equal(l2.tableBrunoDir, path.join(dir, 'api', 'bruno'), 'bảng 3rd-party không bị dời');
  assert.equal(l2.ownBrunoDir, path.join(dir, 'api', 'bruno-api'));

  const calls = [];
  const fns = { runTableFn: () => { calls.push('table'); return 0; }, runOwnFn: () => { calls.push('own'); return 1; } };
  const modes = br.selectModes(l2);
  // --env mock (env của bảng) → own bỏ qua, exit chỉ theo bảng.
  assert.equal(quiet(() => br.runModes(l2, { env: 'mock' }, modes, fns)), 0);
  assert.deepEqual(calls, ['table']);
  calls.length = 0;
  assert.equal(quiet(() => br.runModes(l2, { env: 'dev' }, modes, fns)), 1);
  assert.deepEqual(calls, ['table', 'own']);
  calls.length = 0;
  // --mode own tường minh → không bỏ qua (runOwn tự từ chối env lạ).
  assert.equal(quiet(() => br.runModes(l2, { env: 'mock', kind: 'own' }, { own: true, table: false }, fns)), 1);
  assert.deepEqual(calls, ['own']);
});
