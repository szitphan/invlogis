#!/usr/bin/env node
// Bruno CLI giả cho test: `bru --version` | `bru run <folder> -r --env x --reporter-json <file> [--env-var k=v]`.
// Kịch bản theo tên thư mục: *CHK-fuel-demo-006* → assertion body rớt; còn lại → đậu.
import fs from 'node:fs';
const argv = process.argv.slice(2);
if (argv[0] === '--version') { console.log('9.9.9-fake'); process.exit(0); }
const folder = argv[1];
const out = argv[argv.indexOf('--reporter-json') + 1];
const files = fs.readdirSync(folder).filter((f) => f.endsWith('.yml') && f !== 'folder.yml').sort();
const fail = folder.includes('CHK-fuel-demo-006');
const results = files.map((f) => {
  const biz = !f.includes('-auth-');
  const bad = fail && biz;
  const skipped = f.includes('select-working-context') || f.includes('working-context-facility');
  return {
    test: { filename: `${folder}/${f}` },
    request: { method: 'POST', url: 'https://api-dev-erp.innvie.vn/x' },
    response: { status: bad ? 201 : 200 },
    status: skipped ? 'skipped' : (bad ? 'fail' : 'pass'),
    assertionResults: [{ lhsExpr: 'res.status', operator: 'eq', rhsExpr: '403', status: bad ? 'fail' : 'pass' }],
    testResults: [],
  };
});
fs.writeFileSync(out, JSON.stringify([{ iterationIndex: 0, results }]));
process.exit(fail ? 1 : 0);
