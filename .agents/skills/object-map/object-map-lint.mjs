#!/usr/bin/env node
// object-map-lint.mjs — Kiểm bản đồ đối tượng ORCA (output /object-map) TRƯỚC khi báo xong.
//
// VÌ SAO CÓ FILE NÀY: object map là 4 bảng tham chiếu chéo nhau (đối tượng ↔ quan hệ ↔ hành động ↔
// thuộc tính) + 1 sơ đồ vẽ lại bảng quan hệ. Lỗi hay gặp đều "trông vẫn ổn" khi đọc lướt: hành động
// gắn vào đối tượng chưa khai, vai trò không có trong Actor Registry, dòng suy luận không có câu hỏi
// mở đi kèm, sơ đồ Mục 0 lệch bảng Mục 2 sau khi sửa tay. Máy kiểm được hết các lỗi này; phần
// nghiệp vụ (quan hệ có đúng đời thực không) thì KHÔNG — báo cáo luôn ghi rõ mức đó chưa được kiểm.
//
// Dùng:
//   node object-map-lint.mjs <file.md>                       → exit 0 pass, 1 có error, 2 không đọc được
//   node object-map-lint.mjs <file.md> --write-diagram       → sinh lại Mục 0 từ bảng Mục 2 rồi kiểm
//   node object-map-lint.mjs <file.md> --project <map.md>    → chế độ feature: đối chiếu bản đồ cấp dự án
//   node object-map-lint.mjs <file.md> --definitions <file>  → nguồn Actor Registry (mặc định docs/_shared/definitions.md)
//   node object-map-lint.mjs <file.md> --states <glob-dir>   → thư mục quét *-states.md cho R8 (mặc định docs)
//
// File dưới docs/{feature}/ mà không truyền --project → tự lấy docs/_shared/object-map.md nếu có.

import { readFileSync, writeFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import path from 'node:path';

const argv = process.argv.slice(2);
const flag = (n) => { const i = argv.indexOf('--' + n); return i >= 0 ? argv[i + 1] : null; };
const FILE = argv.find((a, i) => !a.startsWith('--') && (i === 0 || !argv[i - 1].startsWith('--') || argv[i - 1] === '--write-diagram'));
const WRITE_DIAGRAM = argv.includes('--write-diagram');

if (!FILE || !existsSync(FILE)) { console.error(`KHÔNG ĐỌC ĐƯỢC: ${FILE || '(thiếu đường dẫn file)'}`); process.exit(2); }

const ROOT = findRoot(path.resolve(FILE));
const DEFS = flag('definitions') || path.join(ROOT, 'docs/_shared/definitions.md');
const STATES_DIR = flag('states') || path.join(ROOT, 'docs');
const isFeatureFile = /docs\/(?!_)[^/]+\/[^/]+-object-map\.md$/.test(path.resolve(FILE).replace(/\\/g, '/'));
let PROJECT = flag('project');
if (!PROJECT && isFeatureFile) {
  const p = path.join(ROOT, 'docs/_shared/object-map.md');
  if (existsSync(p)) PROJECT = p;
}

const BEGIN = '<!-- object-map:diagram:begin -->';
const END = '<!-- object-map:diagram:end -->';
const CARDINALITY = /^(1|n)\s*[–-]\s*(1|n)$/;
const NAV = /^(2 chiều|không|.+\s*→\s*.+)$/;
const SHOW_VALUES = ['Thẻ', 'Danh sách', 'Chi tiết'];
const CREATE_VERB = /^(Tạo|Lập|Gửi|Thêm|Đề xuất|Nhập|Khai báo)\b/i;
const END_VERB = /(Thu hồi|Huỷ|Hủy|Xoá|Xóa|Đóng|Từ chối|Chốt|Hoàn thành|Ngừng|Kết thúc|Lưu trữ)/i;
const OBJ_CODE = /^OBJ-[a-z0-9]+(?:-[a-z0-9]+)*$/;
const UNSURE = /🟡/;

// ───────────────────────── parse ─────────────────────────

function findRoot(p) {
  let d = path.dirname(p);
  while (d !== path.dirname(d)) { if (existsSync(path.join(d, 'docs'))) return d; d = path.dirname(d); }
  return process.cwd();
}

const strip = (s) => s.replace(/\[\[[^\]|]*\|([^\]]*)\]\]/g, '$1').replace(/\[\[([^\]]*)\]\]/g, '$1')
  .replace(/`/g, '').replace(/\*\*/g, '').trim();

// Trả mọi bảng markdown: {header:[...], rows:[{cells, ln}]}. Ô có `\|` (wikilink alias) được giữ nguyên.
function parseTables(text) {
  const lines = text.split(/\r?\n/);
  const tables = [];
  const split = (l) => l.trim().replace(/^\||\|$/g, '').split(/(?<!\\)\|/).map(c => c.replace(/\\\|/g, '|').trim());
  for (let i = 0; i < lines.length - 1; i++) {
    if (!/^\s*\|/.test(lines[i]) || !/^\s*\|[\s:|-]+\|\s*$/.test(lines[i + 1])) continue;
    const header = split(lines[i]).map(strip);
    const rows = [];
    let j = i + 2;
    for (; j < lines.length && /^\s*\|/.test(lines[j]); j++) rows.push({ cells: split(lines[j]), ln: j + 1 });
    tables.push({ header, rows, ln: i + 1 });
    i = j - 1;
  }
  return tables;
}

// Tìm bảng theo bộ cột bắt buộc. Map row → object theo tên cột.
function pick(tables, required) {
  const t = tables.find(t => required.every(c => t.header.includes(c)));
  if (!t) return null;
  return {
    ln: t.ln,
    rows: t.rows.map(r => {
      const o = { _ln: r.ln, _raw: r.cells.join(' | ') };
      t.header.forEach((h, k) => { o[h] = r.cells[k] ?? ''; });
      return o;
    }),
  };
}

function parseMap(file) {
  const text = readFileSync(file, 'utf8');
  const tables = parseTables(text);
  return {
    text,
    roles: pick(tables, ['Vai trò', 'Thuộc actor', 'Nguồn']),
    objects: pick(tables, ['Mã', 'Tên', 'Định nghĩa', 'Nguồn']),
    rels: pick(tables, ['Từ', 'Quan hệ', 'Tới', 'Bản số', 'Đi được từ màn chi tiết', 'Nguồn']),
    ctas: pick(tables, ['Đối tượng', 'Hành động', 'Vai trò', 'Kênh', 'Đổi trạng thái', 'Nguồn']),
    attrs: pick(tables, ['Đối tượng', 'Thuộc tính', 'Loại nghiệp vụ', 'Hiện ở', 'Lọc / Sắp', 'Nguồn']),
    oqs: pick(tables, ['#', 'Câu hỏi', 'Liên quan']),
  };
}

function actorRegistry(file) {
  if (!existsSync(file)) return null;
  const text = readFileSync(file, 'utf8');
  const idx = text.search(/^## Actor Registry/m);
  if (idx < 0) return null;
  const t = pick(parseTables(text.slice(idx)), ['Canonical']);
  return t ? new Set(t.rows.map(r => strip(r['Canonical']))) : null;
}

function stateNames(dir) {
  const names = new Set();
  let found = 0;
  const walk = (d) => {
    for (const f of readdirSync(d)) {
      const p = path.join(d, f);
      if (f === 'node_modules' || f.startsWith('.')) continue;
      if (statSync(p).isDirectory()) walk(p);
      else if (/-states\.md$/.test(f)) {
        found++;
        const t = readFileSync(p, 'utf8');
        for (const m of t.matchAll(/state\s+"([^"]+)"\s+as\s+(\w+)/g)) { names.add(m[1].trim()); names.add(m[2]); }
        for (const m of t.matchAll(/^\s*([\wÀ-ỹ]+)\s*-->\s*([\wÀ-ỹ]+)/gm)) { names.add(m[1]); names.add(m[2]); }
        for (const t2 of parseTables(t)) for (const r of t2.rows) r.cells.forEach(c => names.add(strip(c)));
      }
    }
  };
  if (existsSync(dir)) walk(dir);
  return found ? names : null;
}

// ───────────────────────── checks ─────────────────────────

const me = parseMap(FILE);
const proj = PROJECT ? parseMap(PROJECT) : null;
const issues = { 'Cấu trúc': [], 'Tham chiếu': [], 'Ngữ pháp ORCA': [] };
const add = (level, sev, ln, msg) => issues[level].push({ sev, ln, msg });

// Cấu trúc: đủ bảng
const NEED = { roles: 'Vai trò nghiệp vụ', objects: 'Mục 1 Đối tượng', rels: 'Mục 2 Quan hệ', ctas: 'Mục 3 Hành động theo vai trò', attrs: 'Mục 4 Thuộc tính', oqs: 'Mục 5 Câu hỏi mở' };
for (const [k, label] of Object.entries(NEED)) if (!me[k]) add('Cấu trúc', 'error', 0, `Thiếu bảng "${label}" (header cột chưa đúng mẫu template)`);
const rows = (k) => (me[k] ? me[k].rows : []);
const prow = (k) => (proj && proj[k] ? proj[k].rows : []);

// Đối tượng: khai ở file này + cấp dự án
const objByName = new Map(), objByCode = new Map();
for (const r of prow('objects')) { const n = strip(r['Tên']), c = strip(r['Mã']); objByName.set(n, { code: c, scope: 'project' }); objByCode.set(c, n); }
for (const r of rows('objects')) {
  const n = strip(r['Tên']), c = strip(r['Mã']);
  if (!OBJ_CODE.test(c)) add('Cấu trúc', 'error', r._ln, `Mã "${c}" sai mẫu — phải là OBJ-{slug} kebab-case ASCII (vd OBJ-lenh-sua-chua)`);
  if (objByName.get(n)?.scope === 'project') add('Tham chiếu', 'error', r._ln, `"${n}" đã khai ở bản đồ cấp dự án — file feature chỉ tham chiếu, không khai lại`);
  else if (objByName.has(n)) add('Cấu trúc', 'error', r._ln, `Tên đối tượng "${n}" bị khai 2 lần`);
  if (objByCode.has(c) && objByName.get(objByCode.get(c))?.scope !== 'project') add('Cấu trúc', 'error', r._ln, `Mã "${c}" bị dùng 2 lần`);
  objByName.set(n, { code: c, scope: 'self' }); objByCode.set(c, n);
}
const resolveObj = (cell) => { const v = strip(cell); if (objByName.has(v)) return v; if (objByCode.has(v)) return objByCode.get(v); return null; };

// Vai trò
const registry = actorRegistry(DEFS);
const roleSet = new Set([...prow('roles'), ...rows('roles')].map(r => strip(r['Vai trò'])));
if (!registry) add('Tham chiếu', 'warn', 0, `Không đọc được Actor Registry ở ${path.relative(ROOT, DEFS)} — R2 chỉ kiểm vai trò ↔ bảng Vai trò, chưa kiểm actor`);
for (const r of rows('roles')) {
  const a = strip(r['Thuộc actor']);
  if (registry && !UNSURE.test(a) && !registry.has(a)) add('Tham chiếu', 'error', r._ln, `R2: actor "${a}" của vai trò "${strip(r['Vai trò'])}" không có trong Actor Registry (dùng đúng tên Canonical)`);
}

// R9: 🟡 phải trỏ OQ tồn tại
const oqIds = new Set([...rows('oqs'), ...prow('oqs')].map(r => strip(r['#'])));
for (const k of ['roles', 'objects', 'rels', 'ctas', 'attrs']) for (const r of rows(k)) {
  if (!UNSURE.test(r._raw)) continue;
  const refs = [...r._raw.matchAll(/OQ-\d+/g)].map(m => m[0]);
  if (!refs.length) add('Tham chiếu', 'error', r._ln, `R9: dòng có 🟡 nhưng không trỏ câu hỏi mở nào — ghi "🟡 Suy luận · OQ-n" ở cột Nguồn`);
  for (const id of refs) if (!oqIds.has(id)) add('Tham chiếu', 'error', r._ln, `R9: ${id} không có trong bảng Câu hỏi mở`);
}

// R1: tham chiếu đối tượng ở bảng 2/3/4
const checkObj = (cell, ln, where) => { const o = resolveObj(cell); if (!o) add('Tham chiếu', 'error', ln, `R1: "${strip(cell)}" ở ${where} chưa được khai ở Mục 1${proj ? ' (cả bản đồ cấp dự án)' : ''}`); return o; };

const relAll = [];
for (const r of rows('rels')) {
  const a = checkObj(r['Từ'], r._ln, 'Mục 2 cột Từ'), b = checkObj(r['Tới'], r._ln, 'Mục 2 cột Tới');
  const card = strip(r['Bản số']), nav = strip(r['Đi được từ màn chi tiết']);
  if (!CARDINALITY.test(card)) add('Cấu trúc', 'error', r._ln, `Bản số "${card}" không hợp lệ — dùng 1–1 / 1–n / n–1 / n–n`);
  if (!NAV.test(nav)) add('Cấu trúc', 'error', r._ln, `Cột "Đi được từ màn chi tiết" = "${nav}" — dùng "2 chiều", "không" hoặc "{Từ} → {Tới}"`);
  else if (nav === 'không') add('Ngữ pháp ORCA', 'warn', r._ln, `R6: quan hệ ${strip(r['Từ'])} — ${strip(r['Tới'])} không đi được từ màn chi tiết theo chiều nào — người dùng không lần theo được`);
  if (a && b) relAll.push({ a, b, label: strip(r['Quan hệ']), card, ln: r._ln });
}
for (const r of prow('rels')) { const a = resolveObj(r['Từ']), b = resolveObj(r['Tới']); if (a && b) relAll.push({ a, b }); }

const ctaByObj = new Map();
for (const r of rows('ctas')) {
  const o = checkObj(r['Đối tượng'], r._ln, 'Mục 3');
  const role = strip(r['Vai trò']);
  if (!UNSURE.test(role) && !roleSet.has(role)) add('Tham chiếu', 'error', r._ln, `R2: vai trò "${role}" chưa khai ở bảng Vai trò nghiệp vụ`);
  if (o) (ctaByObj.get(o) || ctaByObj.set(o, []).get(o)).push(strip(r['Hành động']));
}
for (const r of prow('ctas')) { const o = resolveObj(r['Đối tượng']); if (o) (ctaByObj.get(o) || ctaByObj.set(o, []).get(o)).push(strip(r['Hành động'])); }

const cardAttr = new Set(), anyAttr = new Set();
for (const r of rows('attrs')) {
  const o = checkObj(r['Đối tượng'], r._ln, 'Mục 4');
  const show = strip(r['Hiện ở']).split(/\s*[·,]\s*/).filter(Boolean);
  const bad = show.filter(s => !SHOW_VALUES.includes(s));
  if (bad.length) add('Cấu trúc', 'error', r._ln, `Cột "Hiện ở" có giá trị lạ: ${bad.join(', ')} — chỉ dùng Thẻ / Danh sách / Chi tiết, ngăn bằng " · "`);
  if (o) { anyAttr.add(o); if (show.includes('Thẻ')) cardAttr.add(o); }
}
for (const r of prow('attrs')) { const o = resolveObj(r['Đối tượng']); if (o) { anyAttr.add(o); if (strip(r['Hiện ở']).includes('Thẻ')) cardAttr.add(o); } }

// R4 / R5 / R7 — chỉ xét đối tượng khai ở file này
const mine = rows('objects').map(r => ({ n: strip(r['Tên']), ln: r._ln }));
for (const { n, ln } of mine) {
  if (!relAll.some(e => e.a === n || e.b === n)) add('Ngữ pháp ORCA', 'warn', ln, `R4: "${n}" không có quan hệ nào — đối tượng mồ côi`);
  const acts = ctaByObj.get(n) || [];
  if (acts.some(a => CREATE_VERB.test(a)) && !acts.some(a => END_VERB.test(a))) add('Ngữ pháp ORCA', 'warn', ln, `R5: "${n}" có hành động tạo (${acts.filter(a => CREATE_VERB.test(a)).join(', ')}) nhưng không có hành động kết thúc (Thu hồi / Huỷ / Xoá / Đóng…)`);
  if (!cardAttr.has(n)) add('Ngữ pháp ORCA', 'warn', ln, `R7: "${n}" chưa có thuộc tính nào hiện ở Thẻ — không biết thẻ đối tượng hiện gì`);
}

// R8 — trạng thái khớp states.md (warn: tên trạng thái có thể viết khác giữa 2 nơi)
const states = stateNames(STATES_DIR);
if (!states) add('Tham chiếu', 'info', 0, 'R8: SKIPPED — chưa có file *-states.md nào để đối chiếu trạng thái');
else for (const r of rows('ctas')) {
  const v = strip(r['Đổi trạng thái']);
  if (!v || v === '—' || UNSURE.test(v)) continue;
  v.split('→').flatMap(s => s.split('/')).map(s => s.trim()).filter(s => s && s !== '—').forEach(s => {
    if (!states.has(s)) add('Tham chiếu', 'warn', r._ln, `R8: trạng thái "${s}" không thấy trong file *-states.md nào — kiểm lại tên, hoặc bổ sung /state`);
  });
}

// R10 — Mục 0 khớp Mục 2
const nodeId = (name) => (objByName.get(name)?.code || name).replace(/-/g, '_');
function buildDiagram() {
  const used = new Set();
  rows('rels').forEach(r => { const a = resolveObj(r['Từ']), b = resolveObj(r['Tới']); if (a) used.add(a); if (b) used.add(b); });
  rows('objects').forEach(r => used.add(strip(r['Tên'])));
  const out = ['```mermaid', 'flowchart LR'];
  for (const n of used) {
    const fromProject = objByName.get(n)?.scope === 'project';
    out.push(`  ${nodeId(n)}["${n}"]${fromProject ? ':::project' : ''}`);
  }
  for (const r of rows('rels')) {
    const a = resolveObj(r['Từ']), b = resolveObj(r['Tới']);
    if (a && b) out.push(`  ${nodeId(a)} -->|"${strip(r['Quan hệ'])} · ${strip(r['Bản số'])}"| ${nodeId(b)}`);
  }
  if ([...used].some(n => objByName.get(n)?.scope === 'project')) out.push('  classDef project stroke-dasharray: 4 3');
  out.push('```');
  return out.join('\n');
}
const expected = buildDiagram();
let text = me.text;
const bi = text.indexOf(BEGIN), ei = text.indexOf(END);
if (bi < 0 || ei < bi) add('Cấu trúc', 'error', 0, `Thiếu cặp marker ${BEGIN} / ${END} cho Mục 0`);
else {
  const current = text.slice(bi + BEGIN.length, ei).trim();
  if (current !== expected) {
    if (WRITE_DIAGRAM) { text = text.slice(0, bi + BEGIN.length) + '\n' + expected + '\n' + text.slice(ei); writeFileSync(FILE, text); console.log('Mục 0: đã sinh lại sơ đồ từ bảng Mục 2'); }
    else add('Ngữ pháp ORCA', 'error', 0, 'R10: sơ đồ Mục 0 lệch bảng Mục 2 — chạy lại với --write-diagram (KHÔNG sửa tay sơ đồ)');
  }
}

// ───────────────────────── report ─────────────────────────

let errors = 0;
console.log(`object-map-lint: ${path.relative(process.cwd(), FILE)}${proj ? `  (đối chiếu ${path.relative(process.cwd(), PROJECT)})` : ''}`);
console.log(`  ${mine.length} đối tượng · ${rows('rels').length} quan hệ · ${rows('ctas').length} hành động · ${rows('attrs').length} thuộc tính · ${rows('oqs').length} câu hỏi mở`);
for (const [level, list] of Object.entries(issues)) {
  const e = list.filter(i => i.sev === 'error').length, w = list.filter(i => i.sev === 'warn').length;
  errors += e;
  console.log(`\n[${level}] ${e ? `FAIL — ${e} lỗi` : 'PASS'}${w ? `, ${w} cảnh báo` : ''}`);
  for (const i of list) console.log(`  ${i.sev === 'error' ? '✗' : i.sev === 'warn' ? '!' : '·'} ${i.ln ? `dòng ${i.ln}: ` : ''}${i.msg}`);
}
console.log('\n[Nghiệp vụ] CHƯA KIỂM BẰNG MÁY — quan hệ, quyền và thuộc tính có đúng đời thực không phải đối chiếu nguồn/người dùng.');
process.exit(errors ? 1 : 0);
