// node --test .claude/scripts/__tests__/testgen-core.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import * as core from '../testgen-core.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(HERE, 'fixtures', 'testgen', 'repo');
const TEST_DIR = path.join(FIX, 'docs', 'fuel-demo', 'test');
const TC_FILE = path.join(TEST_DIR, 'testcases', 'testcases-flow-a.md');
const KG_BUILD = path.resolve(HERE, '..', '..', 'skills', 'kg', 'engine', 'kg-build.mjs');

const tmp = () => fs.mkdtempSync(path.join(os.tmpdir(), 'testgen-core-'));
const tcs = () => core.parseTestcasesFile(fs.readFileSync(TC_FILE, 'utf8'));
const byChk = (list, n) => list.find((t) => t.chk === `CHK-fuel-demo-${n}`);

test('parse: Target/Role/Data + Preconditions nhiều dòng', () => {
  const list = tcs();
  assert.equal(list.length, 8);
  const tc1 = byChk(list, '001');
  assert.equal(tc1.target, 'web');
  assert.equal(tc1.role, 'approver');
  assert.equal(tc1.data, 'phieu-cho-duyet');
  assert.equal(tc1.preconditions, 'ROLE: approver\nDATA: phieu-cho-duyet');
  assert.equal(tc1.steps.length, 6);
  assert.equal(tc1.steps[2].testData, '01/10/2026');
  assert.deepEqual(tc1.parseErrors, []);

  const tc3 = byChk(list, '003');
  assert.equal(tc3.target, '', 'thiếu Target → chuỗi rỗng (không undefined)');
  assert.equal(core.tcTarget(tc3), 'web', 'thiếu Target → mặc định web');
  assert.equal(core.tcTarget(byChk(list, '002')), 'api');
  assert.equal(core.tcTarget(byChk(list, '005')), 'mob');
});

test('parse: Target sai giá trị → parseError', () => {
  const md = '---\n**STT:** 1\n**Checklist:** CHK-x-001 — a\n**Auto:** Yes\n**Target:** desktop\n**Preconditions:** —\n**Step:** 1\n**Action:** a\n**Expected:** b\n**Test Data:** —\n';
  const [tc] = core.parseTestcasesFile(md);
  assert.match(tc.parseErrors.join(';'), /Target không hợp lệ/);
});

test('preconditions: chỉ ROLE:/DATA: hoặc — thì KHÔNG setup-required', () => {
  assert.equal(core.parsePreconditions('—').setupRequired, false);
  const rd = core.parsePreconditions('ROLE: approver\nDATA: a, b');
  assert.equal(rd.setupRequired, false);
  assert.equal(rd.onlyRoleData, true);
  assert.deepEqual(rd.roles, ['approver']);
  assert.deepEqual(rd.dataKeys, ['a', 'b']);
  assert.equal(core.parsePreconditions('Có phiếu (dựng: tạo; nguồn: FR-x-001)').setupRequired, true);
  assert.equal(core.parsePreconditions('ROLE: x\nCó phiếu đã duyệt').setupRequired, true);
  const tbd = core.parsePreconditions('TBD (cần BA cấp)');
  assert.equal(tbd.tbd, true);
  assert.equal(tbd.setupRequired, false);
});

test('readiness: role/data resolve, setup-required, role lạ', () => {
  const list = tcs();
  const roles = { approver: {}, 'requester-mobile': {} };
  assert.deepEqual(core.readinessReasons(byChk(list, '001'), { roles }), []);
  assert.deepEqual(core.resolveDataKeys(byChk(list, '001')), ['phieu-cho-duyet']);
  const r4 = core.readinessReasons(byChk(list, '004'), { roles });
  assert.ok(r4.some((r) => /Auto không phải Yes/.test(r)));
  assert.ok(r4.some((r) => /setup-required/.test(r)));
  const r1 = core.readinessReasons(byChk(list, '001'), { roles: { other: {} } });
  assert.ok(r1.some((r) => /Role "approver" không có/.test(r)));
  // Role suy từ dòng ROLE: khi thiếu field
  assert.equal(core.resolveRole({ role: '', preconditions: 'ROLE: finance' }), 'finance');
});

test('checklist: đầu dòng khớp regex KG, đuôi @kênh + [đáp án] tách đúng (2 thứ tự)', () => {
  const kg = fs.readFileSync(KG_BUILD, 'utf8');
  assert.ok(kg.includes(core.CHECKLIST_LINE_PATTERN.source), 'CHECKLIST_LINE_PATTERN phải trùng nguyên văn regex trong kg-build.mjs');

  const a = core.parseChecklistLine('[1] [Yes] CHK-fuel-demo-002 → FR-fuel-demo-R002, AC:FU-FD-AC-002 · Tạo phiếu trả 201 @api [đáp án: code FU-FD-AC-002]');
  assert.equal(a.chk, 'CHK-fuel-demo-002');
  assert.deepEqual(a.refs, ['FR-fuel-demo-R002', 'AC:FU-FD-AC-002']);
  assert.equal(a.text, 'Tạo phiếu trả 201');
  assert.equal(a.channel, 'api');
  assert.equal(a.oracleKind, 'code');
  assert.equal(a.oracleCode, 'FU-FD-AC-002');

  const b = core.parseChecklistLine('[2] [Yes] CHK-x-006 → — · Sai kênh bị chặn [đáp án: tái lập] @api');
  assert.equal(b.channel, 'api');
  assert.equal(b.oracleKind, 'reverse');
  assert.deepEqual(b.refs, []);

  const c = core.parseChecklistLine('[2] [No] CHK-x-004 → FR-x-004 · Tra cứu thủ công');
  assert.equal(c.channel, 'web', 'thiếu kênh → mặc định @web');
  assert.equal(c.oracle, '');
  assert.equal(core.parseChecklistLine('- [ ] không phải checklist'), null);

  for (const [label, kind] of [['SRS', 'srs'], ['CHG-12', 'chg'], ['tái lập', 'reverse'], ['UC cũ', 'legacy-uc'], ['code FU-FD-AC-1', 'code']]) {
    assert.equal(core.oracleKind(label), kind, label);
  }
  assert.equal(core.isDocSuspectOracle('UC cũ'), true);
  assert.equal(core.isDocSuspectOracle('tái lập'), true);
  assert.equal(core.isDocSuspectOracle('code FU-FD-AC-002'), false);
});

test('checklist index + tcOracle (index trước, đuôi Checklist sau)', () => {
  const index = core.loadChecklistIndex(TEST_DIR);
  assert.equal(index.size, 7);
  const list = tcs();
  assert.equal(core.tcOracle(byChk(list, '003'), index).kind, 'legacy-uc');
  const fromTail = core.tcOracle({ chk: 'CHK-z-001', checklist: 'CHK-z-001 — X [đáp án: UC cũ]' }, new Map());
  assert.equal(fromTail.kind, 'legacy-uc');
});

test('classifyFailure + classifyResult (FAIL_DOC chỉ khi assertion rớt và đáp án UC cũ / tái lập)', () => {
  assert.equal(core.classifyFailure('x /*@assert-step*/'), 'app');
  assert.equal(core.classifyFailure('x /*@data-step*/'), 'data');
  assert.equal(core.classifyFailure('locator.fill: Timeout waiting for'), 'data');
  assert.equal(core.classifyFailure(''), 'app');

  assert.equal(core.classifyResult({ status: 'PASS' }).status, 'PASS');
  assert.equal(core.classifyResult({ status: 'PENDING' }).status, 'PENDING');
  assert.equal(core.classifyResult({ status: 'FAIL', kind: 'data' }).status, 'FAIL_DATA');
  assert.equal(core.classifyResult({
    status: 'FAIL', kind: 'data', prev: { lastPass: '2026-10-01', passFingerprint: 'k=v' }, fingerprint: 'k=v',
  }).status, 'FAIL_OUTDATE');
  assert.equal(core.classifyResult({ status: 'FAIL', kind: 'app', oracle: 'UC cũ' }).status, 'FAIL_DOC');
  assert.equal(core.classifyResult({ status: 'FAIL', kind: 'app', oracle: { label: 'tái lập', kind: 'reverse' } }).status, 'FAIL_DOC');
  assert.equal(core.classifyResult({ status: 'FAIL', kind: 'app', oracle: 'code FU-FD-AC-002' }).status, 'FAIL_APP');
  assert.equal(core.classifyResult({ status: 'FAIL', kind: 'data', oracle: 'UC cũ' }).status, 'FAIL_DATA', 'rớt bước data vẫn là nghi data');
});

test('writeNormalizedResults: merge theo (chk, target), schema đúng', () => {
  const dir = tmp();
  core.writeNormalizedResults(dir, [
    { chk: 'CHK-a-001', target: 'web', status: 'PASS', env: 'dev' },
    { chk: 'CHK-a-001', target: 'api', status: 'FAIL_APP', env: 'dev', note: 'x' },
  ]);
  const out = core.writeNormalizedResults(dir, [
    { chk: 'CHK-a-001', target: 'web', status: 'FAIL_DOC', env: 'dev' },
    { chk: 'CHK-a-002', target: 'mob', status: 'WEIRD' },
  ]);
  assert.equal(out.length, 3);
  const file = JSON.parse(fs.readFileSync(path.join(dir, 'results', 'latest.json'), 'utf8'));
  assert.deepEqual(file, out);
  assert.deepEqual(Object.keys(file[0]).sort(), ['at', 'build', 'chk', 'env', 'note', 'status', 'target']);
  assert.equal(file.find((e) => e.target === 'web').status, 'FAIL_DOC');
  assert.equal(file.find((e) => e.target === 'api').status, 'FAIL_APP');
  assert.equal(file.find((e) => e.target === 'mob').status, 'PENDING', 'status lạ → PENDING');
});

test('testdata: merge giữ giá trị user, JSON hỏng → .bak + throw; gaps; history', () => {
  const dir = tmp();
  core.writeTestData(dir, new Map([['a', '1'], ['b', '2']]));
  fs.writeFileSync(path.join(dir, 'testdata.json'), JSON.stringify({ a: 'real', extra: 'x' }));
  core.writeTestData(dir, new Map([['a', '1'], ['b', '2'], ['c', '3']]));
  const td = JSON.parse(fs.readFileSync(path.join(dir, 'testdata.json'), 'utf8'));
  assert.deepEqual(td, { a: 'real', b: '2', c: '3', extra: 'x' });
  const gaps = core.detectDataGaps(dir);
  assert.deepEqual(gaps.stillDefault.map((d) => d.key), ['b', 'c']);
  assert.equal(core.dataFingerprint({ b: 1, a: 2 }), 'a=2|b=1');

  fs.writeFileSync(path.join(dir, 'testdata.json'), '{ broken');
  assert.throws(() => core.writeTestData(dir, new Map([['a', '1']])), /JSON lỗi/);
  assert.equal(fs.readFileSync(path.join(dir, 'testdata.json.bak'), 'utf8'), '{ broken');

  const h = core.updateRunHistory({}, new Map([['CHK-a-001', 'PASS'], ['CHK-a-002', 'FAIL']]), 'fp');
  assert.equal(h['CHK-a-001'].passFingerprint, 'fp');
  assert.equal(h['CHK-a-002'].lastPass, '');
  core.saveRunHistory(dir, h);
  assert.deepEqual(core.loadRunHistory(dir), h);
});

test('cổng môi trường + qa config + dotenv', () => {
  const qa = core.loadQaConfig(FIX);
  assert.equal(qa.found, true);
  assert.ok(!('_note' in qa.roles), 'bỏ khoá _note');
  assert.equal(qa.roles.approver.channel, 'Web');
  assert.equal(core.findRepoRoot(TEST_DIR), FIX);

  const known = core.knownNonProdOrigins(qa.envs);
  assert.ok(known.has('https://api-dev-erp.innvie.vn'));
  assert.ok(known.has('https://web-dev.example.test'));
  assert.equal(core.isProdEnvName('prod'), true);
  assert.equal(core.isProdEnvName('dev'), false);

  assert.equal(core.checkOriginGate({ origin: 'https://web-dev.example.test', allowlist: known }).ok, true);
  assert.equal(core.checkOriginGate({ origin: 'http://localhost:4200' }).ok, true);
  const refused = core.checkOriginGate({ origin: 'https://erp.example.com', allowlist: known });
  assert.equal(refused.ok, false);
  assert.match(refused.message, /CHƯA xác nhận non-prod/);
  const prod = core.checkOriginGate({ origin: 'https://erp.example.com', allowProd: true, confirmProd: 'https://erp.example.com' });
  assert.equal(prod.ok && prod.prod, true);
  assert.equal(core.safeOrigin('https://u:p@h.example.com:8443/x?token=1'), 'https://h.example.com:8443');

  const dir = tmp();
  fs.writeFileSync(path.join(dir, '.env'), '# c\nA=1\nexport B="two"\nbad-key=3\n');
  assert.deepEqual(core.loadDotEnv(path.join(dir, '.env')), { A: '1', B: 'two' });
  assert.deepEqual(core.loadDotEnv(path.join(dir, 'missing')), {});
});

test('chuỗi: extractAllQuoted, dataKeySlug, requireSlug throw (không exit)', () => {
  assert.deepEqual(core.extractAllQuoted('Hiển thị "A" và “B” và "A"'), ['A', 'B']);
  assert.equal(core.dataKeySlug('CHK-x-001'), 'chk-x-001');
  assert.equal(core.dataKeySlug('Số tiền đ'), 'so-tien-d');
  assert.throws(() => core.requireSlug('Bad_Slug', 'feature'), /không hợp lệ/);
});
