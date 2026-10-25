// node --test .claude/scripts/__tests__/playwright-gen.test.mjs
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

import * as pw from '../playwright-gen.mjs';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.resolve(HERE, '..', 'playwright-gen.mjs');
const FIX = path.join(HERE, 'fixtures', 'testgen');

function copyRepo() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'pwgen-'));
  fs.cpSync(path.join(FIX, 'repo'), dir, { recursive: true });
  return dir;
}

const cli = (args, opts = {}) => spawnSync(process.execPath, [SCRIPT, ...args], { encoding: 'utf8', ...opts });

test('import an toàn: không chạy lệnh, không in, không exit', () => {
  const r = spawnSync(process.execPath, ['--input-type=module', '-e', `import(${JSON.stringify(SCRIPT)}).then(() => console.log('OK'))`, 'gen'], { encoding: 'utf8' });
  assert.equal(r.status, 0, r.stderr);
  assert.equal(r.stdout.trim(), 'OK');
});

test('CLI: lệnh lạ → exit 1', () => {
  const r = cli(['bogus']);
  assert.equal(r.status, 1);
  assert.match(r.stderr, /lệnh không hợp lệ/);
});

test('action: ng-zorro verbs + FIELD fallback', () => {
  const sel = pw.actionToCode('Chọn "Cây A" trong "Cây cấp dầu"', '—', 'CHK-x-001', '2');
  assert.equal(sel.complete, true);
  assert.match(sel.code, /SELECT_IN\(page, "Cây cấp dầu", DATA\("chk-x-001\.2\.cay-cap-dau", "Cây A"\)\)/);

  const date = pw.actionToCode('Chọn ngày "Từ ngày"', '01/10/2026', 'CHK-x-001', '3');
  assert.match(date.code, /PICK_DATE\(page, "Từ ngày", DATA\(.*"01\/10\/2026"\)\)/);
  const date2 = pw.actionToCode('Chọn ngày "02/10/2026" trong "Đến ngày"', '', 'CHK-x-001', '4');
  assert.match(date2.code, /PICK_DATE\(page, "Đến ngày", DATA\(.*"02\/10\/2026"\)\)/);

  const row = pw.actionToCode('Bấm nút "Duyệt" trong dòng chứa "PCD-1"', '—', 'CHK-x-001', '5');
  assert.match(row.code, /ROW_ACTION\(page, DATA\(.*"PCD-1"\), "Duyệt"\)/);
  const rowData = pw.actionToCode('Bấm nút "Duyệt" trong dòng chứa', 'PCD-9', 'CHK-x-001', '5');
  assert.match(rowData.code, /ROW_ACTION\(page, DATA\(.*"PCD-9"\), "Duyệt"\)/);

  const confirm = pw.actionToCode('Xác nhận hộp thoại "Đồng ý"');
  assert.equal(confirm.code.trim(), 'await CONFIRM_DIALOG(page, "Đồng ý");');
  assert.equal(pw.actionToCode('Xác nhận hộp thoại').code.trim(), 'await CONFIRM_DIALOG(page);');

  const fill = pw.actionToCode('Nhập field "Email"', 'a@b.vn', 'CHK-x-001', '1');
  assert.match(fill.code, /await \(await FIELD\(page, "Email"\)\)\.fill\(DATA\(/);
  assert.match(fill.code, /@data-step/);

  // giữ hành vi cũ
  assert.match(pw.actionToCode('Bấm nút "Lưu"').code, /getByRole\('button', \{ name: "Lưu", exact: true \}\)/);
  assert.equal(pw.actionToCode('Bấm vào đâu đó').complete, false);
  assert.equal(pw.actionToCode('Nhập field "Mật khẩu"', 'abc123').complete, false, 'secret literal bị chặn');
  const env = pw.actionToCode('Nhập field "Mật khẩu"', 'ENV: QA_PW');
  assert.equal(env.envKey, 'QA_PW');
});

test('expected: nhiều chuỗi quoted → assert TẤT CẢ; toast role=alert|status', () => {
  const multi = pw.expectedToCode('Hiển thị "Phiếu cấp dầu" và "Chờ duyệt"');
  assert.equal((multi.code.match(/toBeVisible/g) || []).length, 2);
  assert.match(multi.code, /"Chờ duyệt"/);
  const neg = pw.expectedToCode('Không hiển thị "Lỗi" hoặc "Sai"');
  assert.equal((neg.code.match(/toBeHidden/g) || []).length, 2);
  const toast = pw.expectedToCode('Toast hiện "Duyệt thành công"');
  assert.match(toast.code, /EXPECT_TOAST\(page, "Duyệt thành công"\)/);
  assert.equal(pw.expectedToCode('Toast hiện thành công').complete, false);
  assert.match(pw.expectedToCode('Chuyển hướng tới /home').code, /toHaveURL/);
});

test('gen: chỉ web/thiếu Target, auth setup theo vai, .env.example có ENV của TC, support fallback', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  const r = cli(['gen', '--dir', dir]);
  assert.equal(r.status, 0, r.stderr);
  const e2e = path.join(dir, 'e2e');

  const spec = fs.readFileSync(path.join(e2e, 'specs', 'flow-a.spec.ts'), 'utf8');
  assert.match(spec, /CHK-fuel-demo-001/);
  assert.match(spec, /CHK-fuel-demo-003/);
  assert.match(spec, /CHK-fuel-demo-008/);
  for (const other of ['002', '005', '006', '007']) assert.doesNotMatch(spec, new RegExp(`CHK-fuel-demo-${other}`));
  assert.match(spec, /test\.use\(\{ storageState: "\.auth\/approver\.json" \}\)/);
  assert.match(spec, /HAS_DATA\("phieu-cho-duyet"\)/);
  assert.match(spec, /ROUTE_RUNTIME_CONFIG/);
  assert.doesNotMatch(spec, /Preconditions cần fixture/, 'Preconditions ROLE:/DATA: không phải setup');

  const setup = fs.readFileSync(path.join(e2e, 'auth.setup.ts'), 'utf8');
  assert.match(setup, /const ROLES: string\[\] = \["approver"\]/);
  for (const key of ['access_token', 'refresh_token', 'current_working_organization_unit_id', 'working_context_id', 'current_facility_context', 'device_identifier']) {
    assert.match(setup, new RegExp(`'${key}'`));
  }
  assert.match(setup, /auth\/working-organization-unit/);
  assert.match(setup, /working-contexts\/facility/);
  assert.doesNotMatch(setup, /\$\{'\$\{'\}/);

  const config = fs.readFileSync(path.join(e2e, 'playwright.config.ts'), 'utf8');
  assert.match(config, /name: 'setup'/);
  assert.match(config, /dependencies: \['setup'\]/);

  const envEx = fs.readFileSync(path.join(e2e, '.env.example'), 'utf8');
  assert.match(envEx, /^QA_DEMO_SECRET=$/m);
  assert.match(envEx, /^QA_APPROVER_USER=$/m);
  assert.doesNotMatch(envEx, /=\S/, '.env.example chỉ có tên biến');

  const support = fs.readFileSync(path.join(e2e, 'support.ts'), 'utf8');
  assert.match(support, /getByPlaceholder\(label/);
  assert.match(support, /\.label-item:text-is/);
  assert.match(support, /role="alert"/);
  assert.match(support, /runtime-config\.js/);

  const td = JSON.parse(fs.readFileSync(path.join(e2e, 'testdata.json'), 'utf8'));
  assert.equal(td['@data.phieu-cho-duyet'], '');
  const index = fs.readFileSync(path.join(e2e, 'fuel-demo-e2e-index.md'), 'utf8');
  assert.match(index, /CHK-fuel-demo-004 \| Auto không phải Yes/);
  assert.match(index, /api: 3 · mob: 1/);
  assert.match(fs.readFileSync(path.join(e2e, '.gitignore'), 'utf8'), /^\.auth\/$/m);

  // e2e/node_modules -> qa/node_modules (symlink TƯƠNG ĐỐI, gitignore không có dấu /).
  const link = path.join(e2e, 'node_modules');
  assert.ok(fs.lstatSync(link).isSymbolicLink());
  assert.equal(fs.readlinkSync(link), path.join('..', '..', '..', '..', 'qa', 'node_modules'));
  assert.match(fs.readFileSync(path.join(e2e, '.gitignore'), 'utf8'), /^node_modules$/m);
  // gen lần 2: giữ link, không nhân đôi dòng gitignore.
  assert.equal(cli(['gen', '--dir', dir]).status, 0);
  assert.ok(fs.lstatSync(link).isSymbolicLink());
  assert.equal((fs.readFileSync(path.join(e2e, '.gitignore'), 'utf8').match(/^node_modules$/gm) || []).length, 1);
  assert.match(setup, /Từ chối gửi thông tin đăng nhập tới API/);
});

test('gen --dry-run không ghi file', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  const r = cli(['gen', '--dir', dir, '--dry-run']);
  assert.equal(r.status, 0, r.stderr);
  assert.match(r.stdout, /DRY-RUN: sẽ gen 3 test/);
  assert.equal(fs.existsSync(path.join(dir, 'e2e')), false);
});

test('run (npx giả): phân loại + FAIL_DOC + latest.json + run-report đúng lệnh retry', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  assert.equal(cli(['gen', '--dir', dir]).status, 0);

  // Playwright cục bộ (qa/node_modules/.bin/playwright) được ưu tiên — npx trong PATH không được gọi.
  const report = path.join(FIX, 'reports', 'playwright-report.json');
  const binDir = path.join(repo, 'qa', 'node_modules', '.bin');
  fs.mkdirSync(binDir, { recursive: true });
  const argsLog = path.join(repo, 'pw-args.txt');
  fs.writeFileSync(path.join(binDir, 'playwright'), `#!/bin/sh\necho "$@" > ${JSON.stringify(argsLog)}\ncp ${JSON.stringify(report)} ./report.json\nexit 1\n`, { mode: 0o755 });
  const bin = fs.mkdtempSync(path.join(os.tmpdir(), 'fake-npx-'));
  fs.writeFileSync(path.join(bin, 'npx'), '#!/bin/sh\necho npx-called >&2\nexit 3\n', { mode: 0o755 });

  const env = { ...process.env, PATH: `${bin}${path.delimiter}${process.env.PATH}`, QA_ENV: 'dev', QA_WEB_BASE: '', FUEL_DEMO_BASE: '', QA_API_BASE: '' };
  const r = cli(['run', '--dir', dir], { env });
  assert.equal(r.status, 1, `${r.stdout}\n${r.stderr}`);
  assert.match(r.stdout, /🟣1 nghi-tài-liệu/);
  assert.doesNotMatch(r.stderr, /npx-called/);
  assert.match(fs.readFileSync(argsLog, 'utf8'), /^test --config playwright\.config\.ts/);

  const latest = JSON.parse(fs.readFileSync(path.join(dir, 'results', 'latest.json'), 'utf8'));
  const st = Object.fromEntries(latest.map((e) => [e.chk, e.status]));
  assert.equal(st['CHK-fuel-demo-001'], 'PASS');
  assert.equal(st['CHK-fuel-demo-003'], 'FAIL_DOC', 'assertion rớt + đáp án UC cũ');
  assert.equal(st['CHK-fuel-demo-008'], 'PENDING');
  assert.ok(latest.every((e) => e.target === 'web' && e.env === 'dev'));

  const runReport = fs.readFileSync(path.join(dir, 'e2e', 'run-report.md'), 'utf8');
  assert.match(runReport, /run --dir docs\/fuel-demo\/test --retry-failed/);
  assert.doesNotMatch(runReport, /--dir docs\/fuel-demo --retry/);
  assert.ok(fs.existsSync(path.join(dir, 'e2e', 'run-history.json')));
  assert.equal(fs.existsSync(path.join(dir, 'e2e', 'report.json')), false, 'report.json bị dọn');
});

test('run: cổng origin từ chối host chưa khai non-prod', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  assert.equal(cli(['gen', '--dir', dir]).status, 0);
  const r = cli(['run', '--dir', dir, '--base', 'https://erp.example.com'], { env: { ...process.env, QA_ENV: 'dev' } });
  assert.equal(r.status, 1);
  assert.match(r.stderr, /CHƯA xác nhận non-prod: https:\/\/erp\.example\.com/);
  const p = cli(['run', '--dir', dir, '--env', 'prod']);
  assert.equal(p.status, 1);
  assert.match(p.stderr, /production/);
});

test('run: không có playwright cục bộ → npx --no-install; không có cả hai → PENDING "chưa cài"', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  assert.equal(cli(['gen', '--dir', dir]).status, 0);
  const report = path.join(FIX, 'reports', 'playwright-report.json');
  const baseEnv = { ...process.env, QA_ENV: 'dev', QA_WEB_BASE: '', FUEL_DEMO_BASE: '', QA_API_BASE: '' };

  // npx có playwright (--no-install --version OK) → chạy qua npx --no-install.
  const bin = fs.mkdtempSync(path.join(os.tmpdir(), 'fake-npx-'));
  const argsLog = path.join(repo, 'npx-args.txt');
  fs.writeFileSync(path.join(bin, 'npx'), `#!/bin/sh
echo "$@" >> ${JSON.stringify(argsLog)}
[ "$1" = "--no-install" ] || exit 9
[ "$3" = "--version" ] && echo "Version 1.49.1" && exit 0
cp ${JSON.stringify(report)} ./report.json
exit 1
`, { mode: 0o755 });
  const r = cli(['run', '--dir', dir], { env: { ...baseEnv, PATH: `${bin}${path.delimiter}${process.env.PATH}` } });
  assert.equal(r.status, 1, `${r.stdout}\n${r.stderr}`);
  const lines = fs.readFileSync(argsLog, 'utf8').trim().split('\n');
  assert.deepEqual(lines, ['--no-install playwright --version', '--no-install playwright test --config playwright.config.ts']);

  // Không có cả hai → PENDING, exit 0, không tải mạng.
  fs.writeFileSync(path.join(bin, 'npx'), '#!/bin/sh\nexit 1\n', { mode: 0o755 });
  fs.rmSync(path.join(dir, 'results'), { recursive: true, force: true });
  const p = cli(['run', '--dir', dir], { env: { ...baseEnv, PATH: `${bin}${path.delimiter}${process.env.PATH}` } });
  assert.equal(p.status, 0, `${p.stdout}\n${p.stderr}`);
  assert.match(p.stdout, /chưa cài: cd qa && npm install/);
  const latest = JSON.parse(fs.readFileSync(path.join(dir, 'results', 'latest.json'), 'utf8'));
  assert.ok(latest.length >= 1);
  assert.ok(latest.every((e) => e.status === 'PENDING' && e.target === 'web' && e.note === 'chưa cài: cd qa && npm install'));
});

test('run: cổng origin chặn cả API base (QA_API_BASE) chưa khai non-prod', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  assert.equal(cli(['gen', '--dir', dir]).status, 0);
  const env = { ...process.env, QA_ENV: 'dev', QA_WEB_BASE: '', FUEL_DEMO_BASE: '', QA_API_BASE: 'https://api.evil.example.com' };
  const r = cli(['run', '--dir', dir], { env });
  assert.equal(r.status, 1);
  assert.match(r.stderr, /\[api\].*CHƯA xác nhận non-prod: https:\/\/api\.evil\.example\.com/);
  // Chỉ xác nhận web origin thì API vẫn bị chặn.
  const r2 = cli(['run', '--dir', dir, '--allow-prod', '--confirm-prod', 'https://web-dev.example.test'], { env });
  assert.equal(r2.status, 1);
  assert.match(r2.stderr, /\[api\]/);
});

test('auth.setup.ts (chạy thật bằng Node strip-types + @playwright/test giả qua symlink): từ chối origin API lạ', () => {
  const repo = copyRepo();
  const dir = path.join(repo, 'docs', 'fuel-demo', 'test');
  assert.equal(cli(['gen', '--dir', dir]).status, 0);
  const e2e = path.join(dir, 'e2e');
  // @playwright/test giả trong qa/node_modules — resolve được nhờ symlink e2e/node_modules.
  const pkg = path.join(repo, 'qa', 'node_modules', '@playwright', 'test');
  fs.mkdirSync(pkg, { recursive: true });
  fs.writeFileSync(path.join(pkg, 'package.json'), JSON.stringify({ name: '@playwright/test', type: 'module', main: 'index.js' }));
  fs.writeFileSync(path.join(pkg, 'index.js'), `
// Không mạng: fetch thật bị thay — tới được bước POST nghĩa là đã qua cổng origin.
globalThis.fetch = async () => { throw new Error('NO-NETWORK'); };
const queue = [];
export function test(name, fn) { queue.push([name, fn]); }
test.skip = (cond, msg) => { if (cond) throw new Error('SKIP ' + msg); };
setTimeout(async () => {
  for (const [name, fn] of queue) {
    try { await fn(); console.log('OK ' + name); } catch (e) { console.log('ERR ' + name + ': ' + e.message); }
  }
}, 0);
`);
  const env = {
    ...process.env, QA_DIR: '', QA_ENV: 'dev', QA_TENANT_ID: 't', QA_WEB_BASE: 'https://web-dev.example.test',
    QA_APPROVER_USER: 'u', QA_APPROVER_PASS: 'p', QA_APPROVER_ORG_UNIT: '',
  };
  const run = (apiBase) => spawnSync(process.execPath, ['auth.setup.ts'], { cwd: e2e, encoding: 'utf8', env: { ...env, QA_API_BASE: apiBase } });
  const bad = run('https://api.evil.example.com');
  assert.equal(bad.status, 0, bad.stderr);
  assert.match(bad.stdout, /ERR login approver: Từ chối gửi thông tin đăng nhập tới API https:\/\/api\.evil\.example\.com/);
  // Origin trong envs.json (dev apiBase) và origin khai ở .allowed-origins → qua cổng, tới bước fetch.
  assert.match(run('https://api-dev-erp.innvie.vn').stdout, /ERR login approver: NO-NETWORK/);
  fs.writeFileSync(path.join(e2e, '.allowed-origins'), '# qa\nhttps://qa-api.example.org\n');
  assert.match(run('https://qa-api.example.org').stdout, /ERR login approver: NO-NETWORK/);
});

test('buildRunReport: data-step → FAIL_DATA, outdate theo lịch sử', () => {
  const repo = copyRepo();
  const e2e = path.join(repo, 'e2e');
  fs.mkdirSync(e2e);
  fs.writeFileSync(path.join(e2e, 'testdata.defaults.json'), '{"k":"v"}');
  fs.writeFileSync(path.join(e2e, 'testdata.json'), '{"k":"real"}');
  const parsed = {
    results: new Map([['CHK-a-001', 'FAIL'], ['CHK-a-002', 'FAIL']]),
    errorTexts: new Map([['CHK-a-001', 'x /*@data-step*/'], ['CHK-a-002', 'x /*@data-step*/']]),
  };
  const history = { 'CHK-a-002': { lastPass: '2026-10-01', passFingerprint: 'k=real' } };
  const rep = pw.buildRunReport(e2e, 'x', parsed, history, {});
  assert.deepEqual(rep.rows.map((r) => r.category), ['FAIL_DATA', 'FAIL_OUTDATE']);
});
