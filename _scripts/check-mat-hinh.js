// _scripts/check-mat-hinh.js — kiểm "mất hình" khung tài liệu component DS v2 (khuôn: design/v2/components/README.md, Mục 9).
// Mục đích: mỗi hình mẫu phải đọc được trên nền thật của ô chứa nó; bắt ô thiếu nền, thân mẫu chìm vào nền ô, khe vòng focus lộ, Hover/Pressed giống Default.
// Cách dùng: thay __FRAME_ID__ (dòng `const FRAME_ID`) bằng ID khung `Tài liệu · {Tên}`, gửi toàn văn làm `code` — qua figma_write nếu proxy chạy được các hàm Plugin API dưới đây (getNodeByIdAsync, variables…), không thì use_figma. CHỈ ĐỌC, không sửa node.
// Đầu ra: { soO, soMau, soCo, co[], satNguong[], soCoLopCon, coLopCon[], satNguongLopCon[], tomTatLop, bang[] } — chép kết quả vào mục `### Kiểm máy` của md (mỗi khối Web / Mobile).
// Quy ước: mỗi ô mẫu là FRAME tên bắt đầu "Ô mẫu · "; khối nền tảng tên "Khối · Web" / "Khối · Mobile".
// Mẫu = instance nằm trong ô mà giữa nó và ô không có instance nào khác (không tính phần lồng bên trong).
// Luật (ngưỡng LIMIT = 1,1:1, tương phản WCAG):
//  A  Ô mẫu có nền riêng; ô khác nền khối (≥ 1,005:1) hoặc có viền.
//  B  Nền thân mẫu so với nền ô < LIMIT:
//       ✕ MẤT HÌNH  — không còn gì giữ hình (không viền ≥ LIMIT, không vòng focus)
//       ⚠ NỀN CHÌM  — nền chìm nhưng viền hoặc vòng focus còn giữ hình
//     Thân không có fill (Ghost, Outline…) → "không nền", không cờ (đúng thiết kế, nền là ô chứa).
//  C  Vòng focus: màu khe (bóng lan nhỏ nhất) khác nền ô (> 1,01:1) → KHE LỘ.
//  D  Cùng lưới, cùng Type: nền Hover / Pressed so với Default < LIMIT → GIỐNG DEFAULT.
// Mở rộng (đầu ra cũ giữ nguyên, chỉ THÊM khoá mới):
//  Mẫu mà lớp ngoài không có nền (Tooltip: nền ở lớp `Bóng`; Text Field: nền ở khung `Field`) →
//  đo thêm lớp con ĐẦU TIÊN (thứ tự cây, bỏ chữ/vector, bỏ lớp ẩn) có nền SOLID. Kết quả ghi ở:
//    bang[]        mọi mẫu, thêm cột lopDo (= "nền đo ở lớp": "(lớp ngoài)" | tên lớp con | "—"),
//                  nenDo, tpDo, vienDo (đo ở lớp đó)
//    coLopCon[]    cờ luật B (và D khi cả Default lẫn Hover/Pressed đo ở lớp con) áp cho lớp con (tách khỏi co[] để co[]/soCo giữ như cũ)
//    soCoLopCon, satNguongLopCon, tomTatLop ({tên lớp đo: số mẫu})
const FRAME_ID = '__FRAME_ID__';
const LIMIT = 1.1;
const fr = await figma.getNodeByIdAsync(FRAME_ID);
let pg = fr; while (pg.type !== 'PAGE') pg = pg.parent; await figma.setCurrentPageAsync(pg);
const lin = c => c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
const L = c => 0.2126 * lin(c.r) + 0.7152 * lin(c.g) + 0.0722 * lin(c.b);
const ratio = (a, b) => { const x = L(a), y = L(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
const r2 = x => Math.round(x * 100) / 100;
const over = (top, a, base) => ({ r: top.r * a + base.r * (1 - a), g: top.g * a + base.g * (1 - a), b: top.b * a + base.b * (1 - a) });
const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, '0')).join('');
async function paintColor(p, consumer) {
  let c = p.color, a = 1; const b = p.boundVariables && p.boundVariables.color;
  if (b) { const v = await figma.variables.getVariableByIdAsync(b.id); const r = v.resolveForConsumer(consumer).value; c = r; a = r.a === undefined ? 1 : r.a; }
  return { c: { r: c.r, g: c.g, b: c.b }, a: a * (p.opacity === undefined ? 1 : p.opacity) };
}
async function surface(node, below) {
  let col = below, has = false;
  if (Array.isArray(node.fills)) for (const p of node.fills) { if (p.visible === false || p.type !== 'SOLID') continue; const { c, a } = await paintColor(p, node); col = over(c, a, col); has = true; }
  return { col, has };
}
async function bgOf(node) {
  const chain = []; for (let x = node; x && x.type !== 'PAGE'; x = x.parent) chain.unshift(x);
  let col = { r: 1, g: 1, b: 1 };
  for (const x of chain) { if (x.type === 'SECTION') continue; col = (await surface(x, col)).col; }
  return col;
}
const blockOf = n => { for (let x = n; x; x = x.parent) if (x.name && x.name.startsWith('Khối · ')) return x.name.slice(7); return '?'; };
const topLevel = (n, cell) => { for (let x = n.parent; x && x !== cell; x = x.parent) if (x.type === 'INSTANCE') return false; return true; };
const BOX = ['FRAME', 'RECTANGLE', 'INSTANCE', 'COMPONENT', 'ELLIPSE'];
const coNen = n => Array.isArray(n.fills) && n.fills.some(p => p.visible !== false && p.type === 'SOLID' && (p.opacity === undefined || p.opacity > 0));
const hienThi = (n, goc) => { for (let x = n; x && x !== goc; x = x.parent) if (x.visible === false) return false; return true; };
const cells = fr.findAll(n => n.type === 'FRAME' && n.name.startsWith('Ô mẫu · '));
const flags = [], flagsLop = [], rows = [], groups = {};
for (const cell of cells) {
  const khoi = blockOf(cell);
  const parentBg = await bgOf(cell.parent);
  const s = await surface(cell, parentBg); const cellBg = s.col;
  const hasStroke = Array.isArray(cell.strokes) && cell.strokes.some(p => p.visible !== false);
  if (!s.has) flags.push({ khoi, o: cell.name, luat: 'A', muc: '✕', loi: 'ô không có nền riêng' });
  else if (ratio(cellBg, parentBg) < 1.005 && !hasStroke) flags.push({ khoi, o: cell.name, luat: 'A', muc: '✕', loi: 'ô trùng nền khối, không viền' });
  const insts = cell.findAll(n => n.type === 'INSTANCE' && topLevel(n, cell));
  for (const inst of insts) {
    const pr = inst.componentProperties || {};
    const type = pr.Type ? pr.Type.value : '', state = pr.State ? pr.State.value : '';
    const body = await surface(inst, cellBg);
    const r = { khoi, o: cell.name, mau: inst.name + (type ? ' · ' + type : '') + (state ? ' · ' + state : ''), nenO: hex(cellBg), nenThan: body.has ? hex(body.col) : 'không nền', tp: r2(ratio(body.col, cellBg)) };
    const st = (inst.strokes || []).filter(p => p.visible !== false && p.type === 'SOLID');
    if (st.length) { const { c } = await paintColor(st[0], inst); r.vien = r2(ratio(c, cellBg)); }
    // --- đo thêm ở lớp con đầu tiên có nền khi lớp ngoài không có nền ---
    let lop = null, bodyDo = body;
    r.lopDo = body.has ? '(lớp ngoài)' : '—'; r.nenDo = r.nenThan; r.tpDo = body.has ? r.tp : null;
    if (!body.has) {
      lop = inst.findAll(n => n !== inst && BOX.includes(n.type) && coNen(n) && hienThi(n, inst))[0] || null;
      if (lop) {
        bodyDo = await surface(lop, cellBg);
        r.lopDo = lop.name; r.nenDo = hex(bodyDo.col); r.tpDo = r2(ratio(bodyDo.col, cellBg));
        const st2 = (lop.strokes || []).filter(p => p.visible !== false && p.type === 'SOLID');
        if (st2.length) { const { c } = await paintColor(st2[0], lop); r.vienDo = r2(ratio(c, cellBg)); }
      }
    }
    const ring = inst.findOne(n => n.name === 'Vòng focus' && n.visible !== false);
    if (ring) {
      const rect = ring.type === 'INSTANCE' ? ring.findOne(n => (n.effects || []).length) : ring;
      const sh = (rect && rect.effects || []).filter(e => e.type === 'DROP_SHADOW' && e.visible !== false).sort((a, b) => a.spread - b.spread);
      const col = async e => { let c = e.color; if (e.boundVariables && e.boundVariables.color) { const v = await figma.variables.getVariableByIdAsync(e.boundVariables.color.id); c = v.resolveForConsumer(rect).value; } return c; };
      if (sh.length) { const gap = await col(sh[0]); r.khe = hex(gap); const g = ratio(gap, cellBg);
        if (sh.length > 1) r.vong = r2(ratio(await col(sh[sh.length - 1]), cellBg));
        if (g > 1.01) flags.push({ khoi, o: cell.name, luat: 'C', muc: '✕', loi: `KHE LỘ: khe vòng focus ${hex(gap)} trên nền ô ${r.nenO} (${r2(g)}:1)` }); }
    }
    if (body.has && r.tp < LIMIT) {
      const holds = (r.vien && r.vien >= LIMIT) ? `viền ${r.vien}:1` : (r.vong && r.vong >= 3) ? `vòng focus ${r.vong}:1` : null;
      flags.push({ khoi, o: cell.name, luat: 'B', muc: holds ? '⚠' : '✕', loi: `${holds ? 'NỀN CHÌM' : 'MẤT HÌNH'}: nền thân ${r.nenThan} trên nền ô ${r.nenO} = ${r.tp}:1${holds ? ', hình giữ nhờ ' + holds : ', không viền, không vòng'}` });
    }
    if (lop && bodyDo.has && r.tpDo < LIMIT) {
      const holds2 = (r.vienDo && r.vienDo >= LIMIT) ? `viền ${r.vienDo}:1` : (r.vong && r.vong >= 3) ? `vòng focus ${r.vong}:1` : null;
      flagsLop.push({ khoi, o: cell.name, luat: 'B', lop: lop.name, muc: holds2 ? '⚠' : '✕', loi: `${holds2 ? 'NỀN CHÌM' : 'MẤT HÌNH'} (lớp "${lop.name}"): nền ${r.nenDo} trên nền ô ${r.nenO} = ${r.tpDo}:1${holds2 ? ', hình giữ nhờ ' + holds2 : ', không viền, không vòng'}` });
    }
    rows.push(r);
    const key = khoi + '|' + (cell.parent && cell.parent.parent ? cell.parent.parent.id : '') + '|' + type;
    groups[key] = groups[key] || {}; groups[key][state] = { col: body.col, colDo: bodyDo.col, lop: lop ? lop.name : null, o: cell.name, khoi };
  }
}
for (const g of Object.values(groups)) {
  if (!g.Default) continue;
  for (const s of ['Hover', 'Pressed']) if (g[s]) { const q = ratio(g[s].col, g.Default.col); if (q < LIMIT) flags.push({ khoi: g[s].khoi, o: g[s].o, luat: 'D', muc: '✕', loi: `GIỐNG DEFAULT: ${s} ${hex(g[s].col)} so với Default ${hex(g.Default.col)} = ${r2(q)}:1` }); }
}
// luật D áp cho lớp con (chỉ khi cả Default lẫn Hover/Pressed đều đo ở lớp con)
for (const g of Object.values(groups)) {
  if (!g.Default || !g.Default.lop) continue;
  for (const s of ['Hover', 'Pressed']) if (g[s] && g[s].lop) { const q = ratio(g[s].colDo, g.Default.colDo); if (q < LIMIT) flagsLop.push({ khoi: g[s].khoi, o: g[s].o, luat: 'D', lop: g[s].lop, muc: '✕', loi: `GIỐNG DEFAULT (lớp "${g[s].lop}"): ${s} ${hex(g[s].colDo)} so với Default ${hex(g.Default.colDo)} = ${r2(q)}:1` }); }
}
const sat = rows.filter(r => r.nenThan !== 'không nền' && r.tp >= LIMIT && r.tp < 1.15).map(r => `${r.khoi} · ${r.mau}: ${r.tp}:1`);
const satLop = rows.filter(r => r.lopDo !== '(lớp ngoài)' && r.lopDo !== '—' && r.tpDo >= LIMIT && r.tpDo < 1.15).map(r => `${r.khoi} · ${r.mau} [${r.lopDo}]: ${r.tpDo}:1`);
const tomTatLop = {}; rows.forEach(r => { tomTatLop[r.lopDo] = (tomTatLop[r.lopDo] || 0) + 1; });
return { soO: cells.length, soMau: rows.length, soCo: flags.length, co: flags, satNguong: sat,
  soCoLopCon: flagsLop.length, coLopCon: flagsLop, satNguongLopCon: satLop, tomTatLop, bang: rows };
