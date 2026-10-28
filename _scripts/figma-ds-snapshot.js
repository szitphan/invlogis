// Ảnh chụp DS v2 trên Figma để so với repo (_scripts/ds-v2-sync-check.py). CHỈ ĐỌC.
// Chạy bằng use_figma (Plugin API), 2 kiểu gọi (use_figma không cho loadAllPagesAsync, mỗi lần gọi chỉ đổi trang 1 lần):
//   PAGE_ID = ''        → mã băm biến theo collection + danh sách trang DS (varhash, pages) — vài KB
//   COLLECTION = '<tên>' (PAGE_ID = '') → giá trị từng biến của 1 collection (khi sync-check báo collection đó lệch)
//   PAGE_ID = '<id>'    → component + Section của trang đó (gọi song song mỗi trang một lần)
// Lưu từng kết quả JSON vào thư mục nháp rồi gộp: python3 _scripts/ds-v2-sync-check.py --merge <out.json> <part1.json> …
// → .claude/state/figma/ds-v2-snapshot.json, rồi: python3 _scripts/ds-v2-sync-check.py --figma <file>
// Lấy:
//   varhash    — {collection: {n, h, modes}}: băm các dòng `tên=giá trị` (alias đã giải); sync-check băm tokens.json cùng cách
//   variables  — (chỉ khi COLLECTION) {collection, name, modes}; collection 1 mode thì giải thêm theo Light/Dark để so màu
//   Kết quả biến đầy đủ của cả file > 48 KB (giới hạn use_figma) nên không chụp hết một lần.
//   components — COMPONENT_SET + COMPONENT đứng riêng trên các trang DS (tên trang bắt đầu "DS ·" hoặc chứa "FOUNDATIONS"):
//                id, tên, trang, Section chứa, dòng "Trạng thái: …" đầu mô tả
//   sections   — Section trên các trang đó + chữ của nhãn trạng thái (frame/text tên "Nhãn trạng thái" nằm thẳng trong Section — không dùng tên "Trạng thái": trùng Section con khu demo state)
const PAGE_RE = /DS ·|FOUNDATIONS/;
const PAGE_ID = '';
const COLLECTION = '';

if (!PAGE_ID) {
  const hex = c => '#' + [c.r, c.g, c.b].map(x => Math.round(x * 255).toString(16).padStart(2, '0')).join('').toUpperCase()
    + (c.a !== undefined ? Math.round(c.a * 255).toString(16).padStart(2, '0').toUpperCase() : 'FF');
  const cols = await figma.variables.getLocalVariableCollectionsAsync();
  const colById = Object.fromEntries(cols.map(c => [c.id, c]));
  const vars = await figma.variables.getLocalVariablesAsync();
  const varById = Object.fromEntries(vars.map(v => [v.id, v]));
  const modeFor = (col, name) => (col.modes.find(x => x.name === name) || col.modes.find(x => x.modeId === col.defaultModeId)).modeId;
  function val(v, mode, k = 0) {
    const col = colById[v.variableCollectionId]; const raw = v.valuesByMode[modeFor(col, mode)];
    if (raw && raw.type === 'VARIABLE_ALIAS') { const t = varById[raw.id]; return t && k < 8 ? val(t, mode, k + 1) : null; }
    return raw && typeof raw === 'object' && 'r' in raw ? hex(raw) : raw;
  }
  const taken = new Date().toISOString().slice(0, 10);
  if (COLLECTION) {
    const col = cols.find(c => c.name === COLLECTION);
    const names = col.modes.length === 1 ? [col.modes[0].name, 'Light', 'Dark'] : col.modes.map(m => m.name);
    const variables = vars.filter(v => v.variableCollectionId === col.id)
      .map(v => ({ collection: col.name, name: v.name, modes: Object.fromEntries(names.map(m => [m, val(v, m)])) }));
    return { fileKey: figma.fileKey, taken, variables };
  }
  const norm = x => x == null ? 'null' : typeof x === 'number' ? (Math.round(x * 100) / 100).toString() : String(x).toUpperCase();
  const h = s => { let a = 5381; for (const ch of s) a = ((a * 33) ^ ch.codePointAt(0)) >>> 0; return a.toString(36); };
  const varhash = {};
  for (const col of cols) {
    const lines = vars.filter(v => v.variableCollectionId === col.id).map(v => v.name + '=' + (col.modes.length === 1
      ? norm(val(v, col.modes[0].name))
      : col.modes.map(m => m.name).sort().map(m => m + ':' + norm(val(v, m))).join(','))).sort();
    varhash[col.name] = { n: lines.length, h: h(lines.join('\n')), modes: col.modes.map(m => m.name) };
  }
  const pages = figma.root.children.filter(p => PAGE_RE.test(p.name)).map(p => ({ id: p.id, name: p.name.trim() }));
  return { fileKey: figma.fileKey, taken, varhash, pages };
}
const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);
const components = [], sections = [];
const secOf = n => { for (let x = n.parent; x && x.type !== 'PAGE'; x = x.parent) if (x.type === 'SECTION') return x; return null; };
for (const s of page.findAllWithCriteria({ types: ['SECTION'] })) {
  const badge = s.children.find(c => c.name === 'Nhãn trạng thái');
  let text = null;
  if (badge) { const t = badge.type === 'TEXT' ? badge : (badge.findOne ? badge.findOne(n => n.type === 'TEXT') : null); text = t ? t.characters : null; }
  sections.push({ id: s.id, name: s.name, page: page.name.trim(), badge: text });
}
for (const n of page.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] })) {
  if (n.type === 'COMPONENT' && n.parent && n.parent.type === 'COMPONENT_SET') continue;
  const d = (n.description || '').split('\n')[0]; const m = d.match(/^Trạng thái:\s*(.+)$/);
  const sec = secOf(n);
  components.push({ id: n.id, name: n.name, type: n.type, page: page.name.trim(), section: sec ? sec.id : null,
    sectionName: sec ? sec.name : null, status: m ? m[1].trim() : null });
}
return { page: page.name.trim(), components, sections };
