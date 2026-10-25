import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { fold, parseJunit, mapAction, mapExpected, parseDotenv, buildEnvArgs } from '../maestro-gen.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const GEN = path.join(HERE, '..', 'maestro-gen.mjs');
const FIX = path.join(HERE, 'fixtures', 'maestro');

function setup() {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'maestro-'));
  fs.cpSync(FIX, root, { recursive: true });
  return { root, dir: path.join(root, 'docs/fuel-demo/test') };
}
const cli = (args, env = {}) => spawnSync('node', [GEN, ...args], { encoding: 'utf8', env: { ...process.env, ...env } });

test('fold bỏ dấu', () => assert.equal(fold('Đăng nhập Vai'), 'dang nhap vai'));

test('mapAction: bấm / nhập / id / secret / unknown', () => {
  const ctx = { sub: (f) => `S/${f}`, role: '' };
  assert.match(mapAction('Bấm "Cấp dầu"', ctx).lines[0], /tapOn: "Cấp dầu"/);
  assert.match(mapAction('bam "fuel.list-btn"', ctx).lines[0], /id: "fuel.list-btn"/);
  const inp = mapAction('Nhập "ENV: QA_X" vào "Số lít"', ctx).lines;
  assert.equal(inp[1], '- inputText: "${QA_X}"');
  assert.ok(mapAction('Nhập "abc123" vào "Mật khẩu"', ctx).skip);
  assert.ok(mapAction('Lắc điện thoại', ctx).skip);
  assert.match(mapAction('Chờ "Đang bơm" hiện', ctx).lines[0], /timeout: 25000/);
  assert.match(mapAction('Chờ "Danh sách" hiện', ctx).lines[0], /timeout: 30000/);
});

test('mapExpected: visible / not visible / ghi chú', () => {
  const r = mapExpected('Hiện "A"\nKhông hiện "B"\nMàn đẹp');
  assert.deepEqual(r.lines.slice(0, 2), ['- assertVisible: "A"', '- assertNotVisible: "B"']);
  assert.match(r.lines[2], /^# \[chưa tự kiểm\]/);
  assert.equal(r.asserts, 2);
});

test('gen --dry-run không ghi file', () => {
  const { root, dir } = setup();
  const r = cli(['gen', '--dir', dir, '--root', root, '--dry-run']);
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stdout, /2 flow, skip 2/);
  assert.ok(!fs.existsSync(path.join(dir, 'mobile')));
});

test('gen sinh flow, config, index; skip đúng lý do', () => {
  const { root, dir } = setup();
  const r = cli(['gen', '--dir', dir, '--root', root]);
  assert.equal(r.status, 0, r.stderr);
  const f1 = fs.readFileSync(path.join(dir, 'mobile/maestro/flows/flow-a/chk-fuel-demo-001.yaml'), 'utf8');
  assert.match(f1, /appId: \$\{APP_ID\}/);
  assert.match(f1, /name: "CHK-fuel-demo-001: /);
  assert.match(f1, /  - FR-fuel-demo-R001/);
  assert.match(f1, /  - mob/);
  assert.match(f1, /launchApp/);
  assert.match(f1, /login-as-role\.yaml\n\s+env:\n\s+ROLE: "requester-mobile"/);
  assert.match(f1, /file: (\.\.\/)+qa\/mobile\/subflows\/igas-simulate-pump\.yaml/);
  assert.match(f1, /STAGE: both/);
  assert.match(f1, /assertNotVisible: "Lỗi"/);
  assert.match(f1, /timeout: 25000/);
  const f2 = fs.readFileSync(path.join(dir, 'mobile/maestro/flows/flow-a/chk-fuel-demo-002.yaml'), 'utf8');
  assert.match(f2, /ROLE: "approver"/);
  assert.match(f2, /inputText: "\$\{QA_LITERS\}"/);
  assert.ok(!fs.existsSync(path.join(dir, 'mobile/maestro/flows/flow-a/chk-fuel-demo-003.yaml')));
  assert.ok(!fs.existsSync(path.join(dir, 'mobile/maestro/flows/flow-a/chk-fuel-demo-004.yaml')));
  assert.ok(fs.existsSync(path.join(dir, 'mobile/maestro/config.yaml')));
  const idx = fs.readFileSync(path.join(dir, 'mobile/fuel-demo-mobile-index.md'), 'utf8');
  assert.match(idx, /\| Scope \| File \| Tests \| Kết quả gần nhất \|/);
  assert.match(idx, /\| CHK-ID \| Flow \| Codegen \| Kết quả gần nhất \|/);
  assert.match(idx, /\| CHK-ID \| Lý do \|/);
  assert.match(idx, /CHK-fuel-demo-003 \| bước 1: không map được/);
  assert.match(idx, /CHK-fuel-demo-005 \| Auto=No/);
  assert.ok(!/CHK-fuel-demo-004/.test(idx));
});

test('run không có maestro -> PENDING "maestro chưa cài"', () => {
  const { root, dir } = setup();
  const r = cli(['run', '--dir', dir, '--root', root], { MAESTRO_BIN: '/nonexistent/maestro' });
  assert.equal(r.status, 0, r.stderr);
  const res = JSON.parse(fs.readFileSync(path.join(dir, 'results/latest.json'), 'utf8'));
  assert.equal(res.length, 2);
  assert.ok(res.every((x) => x.status === 'PENDING' && x.note === 'maestro chưa cài' && x.target === 'mob'));
});

test('run với maestro giả: parse JUnit PASS / FAIL_APP / FAIL_DOC', () => {
  const { root, dir } = setup();
  const fake = path.join(root, 'fake-maestro.sh');
  fs.writeFileSync(fake, `#!/bin/sh
[ "$1" = "--version" ] && echo 1.0 && exit 0
OUT=""; FLOW="$2"
while [ $# -gt 0 ]; do [ "$1" = "--output" ] && OUT="$2"; shift; done
case "$FLOW" in
 *001.yaml) echo '<testsuite><testcase id="a" name="a"/></testsuite>' > "$OUT";;
 *) echo '<testsuite><testcase id="b" name="b"><failure>Assertion is false: "Số lít hợp lệ" is visible</failure></testcase></testsuite>' > "$OUT"; exit 1;;
esac
`, { mode: 0o755 });
  const r = cli(['run', '--dir', dir, '--root', root, '--env', 'dev', '--build', 'b1'], { MAESTRO_BIN: fake });
  assert.equal(r.status, 0, r.stderr);
  const res = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(dir, 'results/latest.json'), 'utf8')).map((x) => [x.chk, x]));
  assert.equal(res['CHK-fuel-demo-001'].status, 'PASS');
  assert.equal(res['CHK-fuel-demo-001'].build, 'b1');
  assert.equal(res['CHK-fuel-demo-002'].status, 'FAIL_APP');
  const idx = fs.readFileSync(path.join(dir, 'mobile/fuel-demo-mobile-index.md'), 'utf8');
  assert.match(idx, /PASS/);
});

test('run (maestro giả): core.classifyResult → FAIL_DOC (đáp án tái lập) / FAIL_DATA (đăng nhập); latest.json qua core', () => {
  const { root, dir } = setup();
  const tcFile = path.join(dir, 'testcases', 'testcases-flow-a.md');
  fs.writeFileSync(tcFile, fs.readFileSync(tcFile, 'utf8').replace('CHK-fuel-demo-002 — Verify nhập số lít', 'CHK-fuel-demo-002 — Verify nhập số lít [đáp án: tái lập]'));
  // Kết quả kênh khác có sẵn phải được giữ (merge theo chk+target của core).
  fs.mkdirSync(path.join(dir, 'results'), { recursive: true });
  fs.writeFileSync(path.join(dir, 'results', 'latest.json'), JSON.stringify([{ chk: 'CHK-fuel-demo-002', target: 'api', status: 'PASS', env: 'dev', build: '', at: '2026-10-01T00:00:00.000Z', note: '' }]));
  const fake = path.join(root, 'fake-maestro.sh');
  fs.writeFileSync(fake, `#!/bin/sh
[ "$1" = "--version" ] && echo 1.0 && exit 0
OUT=""; FLOW="$2"
while [ $# -gt 0 ]; do [ "$1" = "--output" ] && OUT="$2"; shift; done
case "$FLOW" in
 *001.yaml) echo '<testsuite><testcase id="a" name="a"><failure>Unable to launch app app.test (launchApp)</failure></testcase></testsuite>' > "$OUT"; exit 1;;
 *) echo '<testsuite><testcase id="b" name="b"><failure>Assertion is false: "Số lít hợp lệ" is visible</failure></testcase></testsuite>' > "$OUT"; exit 1;;
esac
`, { mode: 0o755 });
  const r = cli(['run', '--dir', dir, '--root', root, '--env', 'dev'], { MAESTRO_BIN: fake });
  assert.equal(r.status, 0, r.stderr);
  const list = JSON.parse(fs.readFileSync(path.join(dir, 'results/latest.json'), 'utf8'));
  const mob = Object.fromEntries(list.filter((x) => x.target === 'mob').map((x) => [x.chk, x]));
  assert.equal(mob['CHK-fuel-demo-002'].status, 'FAIL_DOC');
  assert.equal(mob['CHK-fuel-demo-001'].status, 'FAIL_DATA');
  assert.ok(list.some((x) => x.chk === 'CHK-fuel-demo-002' && x.target === 'api' && x.status === 'PASS'), 'giữ kết quả api');
  assert.deepEqual(list.map((x) => `${x.chk}|${x.target}`), [...list.map((x) => `${x.chk}|${x.target}`)].sort(), 'core sort chk rồi target');
});

test('parseTestcases dùng core.parseTestcasesFile (Target chuẩn hoá, block thiếu Checklist bị bỏ như core)', async () => {
  const { parseTestcases } = await import('../maestro-gen.mjs');
  const core = await import('../testgen-core.mjs');
  const md = '---\n**STT:** 1\n**Checklist:** CHK-x-001 — a\n**Target:** Mob\n**Role:** approver\n**Step:** 1\n**Action:** Mở app\n**Expected:** Hiện "A"\n---\n**STT:** 2\n**Target:** mob\n**Step:** 1\n**Action:** Mở app\n';
  const got = parseTestcases(md);
  assert.equal(got.length, core.parseTestcasesFile(md).length);
  assert.equal(got.length, 1);
  assert.equal(got[0].target, 'mob');
  assert.equal(got[0].role, 'approver');
  assert.equal(got[0].chk, 'CHK-x-001');
});

test('parseJunit', () => {
  const r = parseJunit('<testsuite><testcase name="x"/><testcase name="y"><failure message="boom"/></testcase></testsuite>');
  assert.deepEqual(r.map((x) => x.status), ['PASS', 'FAIL']);
  assert.equal(r[1].message, 'boom');
});

test('parseDotenv bỏ comment/trống, buildEnvArgs lọc APP_ID/QA_*/biến tham chiếu', () => {
  const v = parseDotenv('# c\n\nAPP_ID=x.y\nQA_ENV=dev\nQA_A_PASS="p w"\nOTHER=1\nREF=2\n');
  assert.equal(v.QA_A_PASS, 'p w');
  const a = buildEnvArgs(['REF'], v);
  assert.ok(a.includes('APP_ID=x.y') && a.includes('QA_ENV=dev') && a.includes('REF=2'));
  assert.ok(!a.some((x) => x.startsWith('OTHER=')));
});

test('run truyền -e tới maestro (không in giá trị) và từ chối prod', () => {
  const { root, dir } = setup();
  fs.mkdirSync(path.join(root, 'qa'), { recursive: true });
  fs.writeFileSync(path.join(root, 'qa/.env'), 'APP_ID=app.test\nQA_ENV=dev\nQA_SECRET_PASS=s3cr3t-value\n');
  const argsFile = path.join(root, 'args.txt');
  const fake = path.join(root, 'fake2.sh');
  fs.writeFileSync(fake, `#!/bin/sh
[ "$1" = "--version" ] && echo 1.0 && exit 0
echo "$@" >> "${argsFile}"
OUT=""; while [ $# -gt 0 ]; do [ "$1" = "--output" ] && OUT="$2"; shift; done
echo '<testsuite><testcase id="a" name="a"/></testsuite>' > "$OUT"
`, { mode: 0o755 });
  const r = cli(['run', '--dir', dir, '--root', root], { MAESTRO_BIN: fake });
  assert.equal(r.status, 0, r.stderr);
  const got = fs.readFileSync(argsFile, 'utf8');
  assert.match(got, /-e APP_ID=app\.test/);
  assert.match(got, /-e QA_SECRET_PASS=s3cr3t-value/);
  assert.ok(!r.stdout.includes('s3cr3t-value') && !r.stderr.includes('s3cr3t-value'));
  const p = cli(['run', '--dir', dir, '--root', root, '--env', 'prod'], { MAESTRO_BIN: fake });
  assert.notEqual(p.status, 0);
  assert.match(p.stderr, /prod/);
});
