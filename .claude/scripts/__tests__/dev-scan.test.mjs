import test from 'node:test';
import assert from 'node:assert/strict';
import path from 'node:path';
import fs from 'node:fs';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { maskSource, composeRoute, parseControllerFile, scanBeEndpoints, scanBePermissions, scanBeAcs, scanBeTests, scanFe, parseSnapshot, collectJiraKeys, resolveTsExpr, run } from '../dev-scan.mjs';

const fx = path.join(path.dirname(fileURLToPath(import.meta.url)), 'fixtures', 'dev-scan');
const be = path.join(fx, 'be');
const fe = path.join(fx, 'fe');

test('maskSource hides comments and string contents but keeps length', () => {
  const s = 'a "{x}" // [HttpGet]\nb';
  const m = maskSource(s, 'cs');
  assert.equal(m.length, s.length);
  assert.ok(!m.includes('{') && !m.includes('Http'));
});

test('composeRoute: prefix, version, absolute override', () => {
  assert.equal(composeRoute({ prefix: 'api/m/v{version:apiVersion}', version: '1.0', classTemplate: 'items', methodTemplate: null }), '/api/m/v1/items');
  assert.equal(composeRoute({ prefix: 'api/m/v{version:apiVersion}', version: '2.0', classTemplate: 'items', methodTemplate: 'x' }), '/api/m/v2/items/x');
  assert.equal(composeRoute({ prefix: 'p', version: '1.0', classTemplate: 'items', methodTemplate: '/abs' }), '/abs');
});

test('controller endpoints, permissions, working context', () => {
  const perms = scanBePermissions(be);
  assert.equal(perms.items.length, 2);
  const map = new Map(perms.items.map((p) => [`${p.class}.${p.name}`, p]));
  const { endpoints } = scanBeEndpoints(be, map);
  assert.equal(endpoints.length, 3);
  const list = endpoints.find((e) => e.action === 'ListAsync');
  assert.equal(list.route, '/api/demo-mod/v1/items');
  assert.equal(list.operationId, 'Items_ListAsync');
  assert.deepEqual(list.permissions.map((p) => p.code), ['demo.items.view']);
  assert.equal(list.workingContext.requirement, 'NoModuleContext');
  const sub = endpoints.find((e) => e.action === 'Submit');
  assert.equal(sub.route, '/api/demo-mod/v1/items/{id:long}/submit');
  assert.equal(sub.permissionLogic, 'Or');
  assert.equal(sub.permissions.length, 2);
  const del = endpoints.find((e) => e.action === 'Remove');
  assert.equal(del.route, '/abs/{id}');
  assert.equal(del.anonymous, true);
  assert.ok(!endpoints.some((e) => e.methodTemplate === 'ghost'));
});

test('AC definitions and test tracing', () => {
  const r = scanBeAcs(be);
  assert.equal(r.totals.definedUnique, 2);
  assert.equal(r.totals.mentionedInDocsUnique, 3);
  assert.equal(r.acs.find((a) => a.id === 'DM-IT-AC-001').traced, true);
  assert.equal(r.acs.find((a) => a.id === 'DM-IT-AC-002').traced, false);
  assert.equal(r.acs[0].title, 'co phieu');
});

test('test counts', () => {
  const t = scanBeTests(be);
  assert.equal(t.totals.fact, 1);
  assert.equal(t.totals.theory, 1);
  assert.equal(t.projects[0].inlineData, 2);
});

test('FE routes resolve enums, templates, children, menu id', () => {
  const r = scanFe(fe);
  const paths = r.routes.routes.map((x) => x.fullPath);
  assert.deepEqual(paths, ['/home', '/alpha/:id', '/alpha/:id/child']);
  const alpha = r.routes.routes[1];
  assert.equal(alpha.component, 'AlphaComponent');
  assert.equal(alpha.menuId, 'ALPHA');
  assert.deepEqual(alpha.guards, ['canActivate:guard']);
  assert.equal(r.testids.totals.dataTestId, 1);
  assert.equal(r.testids.totals.ariaLabel, 1);
  assert.equal(r.testids.totals.labelItem, 1);
  assert.equal(resolveTsExpr('`${RouterPath.HOME}/x`', { enums: { RouterPath: { HOME: 'home' } }, consts: {} }).value, 'home/x');
});

test('snapshot parser', () => {
  const t = [
    '[DbContext(typeof(XDbContext))]',
    '            modelBuilder.Entity("A.B.Thing", b =>',
    '                {',
    '                    b.Property<long>("Id")',
    '                        .HasColumnType("bigint")',
    '                        .HasColumnName("id");',
    '                    b.Property<string>("Name")',
    '                        .HasMaxLength(50)',
    '                        .HasColumnName("name");',
    '                    b.HasKey("Id");',
    '                    b.ToTable("things", "dbo");',
    '                });',
  ].join('\n');
  const r = parseSnapshot(t);
  assert.equal(r.dbContext, 'XDbContext');
  assert.equal(r.entities[0].table, 'things');
  assert.equal(r.entities[0].schema, 'dbo');
  assert.equal(r.entities[0].columns[0].key, true);
  assert.equal(r.entities[0].columns[1].maxLength, 50);
});

test('jira keys aggregate', () => {
  const k = collectJiraKeys('2026-01-02T00:00:00Z\tCD-12 fix\n2026-03-01T00:00:00Z\tmerge CD-12 CD-13\n');
  assert.equal(k['CD-12'].count, 2);
  assert.equal(k['CD-12'].first, '2026-01-02T00:00:00Z');
  assert.equal(k['CD-12'].last, '2026-03-01T00:00:00Z');
  assert.equal(k['CD-13'].count, 1);
});

test('run --only be/fe writes files', () => {
  const out = fs.mkdtempSync(path.join(os.tmpdir(), 'devscan-'));
  try {
    const nonRepo = path.join(out, 'none');
    const s = run({ out, only: 'be', be });
    assert.equal(s.be.endpoints, 3);
    assert.ok(fs.existsSync(path.join(out, 'be-endpoints.json')));
    run({ out, only: 'fe', fe });
    const sum = JSON.parse(fs.readFileSync(path.join(out, 'summary.json'), 'utf8'));
    assert.equal(sum.fe.routes, 3);
    assert.equal(sum.be.endpoints, 3);
    void nonRepo;
  } finally { fs.rmSync(out, { recursive: true, force: true }); }
});

test('parseControllerFile is import-safe', () => {
  assert.deepEqual(parseControllerFile('public class Plain {}'), []);
});
