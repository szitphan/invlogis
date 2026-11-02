// Xuất dữ liệu một component set DS v2 để sinh phần máy của tài liệu (DEC-118, DEC-183).
// Chạy bằng use_figma (Plugin API), CHỈ ĐỌC. Cách dùng: thay SET_ID, gửi toàn văn làm `code`,
// lưu kết quả JSON vào file rồi chạy: python3 _scripts/ds-v2-component-doc.py <file.json> <file.md>
// Kết quả: tên, mô tả, thuộc tính, trục biến thể, số biến thể, token theo phần:
//   colors  — gom theo các trục KHÔNG phải Size (vd Type × State): nền, viền, chữ, icon, vòng focus.
//   metrics — gom theo các trục còn lại trừ State (vd Content × Size): cao, rộng, lề, khoảng cách, bo.
//   text    — text style của từng lớp chữ (tách theo biến thể nếu mỗi biến thể một style).
// Bỏ qua lớp đang ẩn (thuộc tính bật/tắt như Status, Edit) và lớp đặt tự do (ABSOLUTE: lớp phủ, huy hiệu).
// Vòng focus (DEC-213): nay là instance L0 `.focus / Ring` — nhận diện bằng TÊN MAIN COMPONENT (không theo tên lớp), đọc
//   màu, dày ở hình con có bóng/nét; không đi vào instance L1 lồng (vòng của nút trong
//   chân thẻ không phải của thẻ), chỉ đi vào instance đặt tự do (vd "Khung thẻ"). Bản cũ (lớp con "Vòng focus" hoặc bóng
//   lan 0-blur trên chính biến thể) vẫn đọc được. Bóng nổi (shadow/*) ra cột riêng `shadow`, không lẫn vào vòng focus.
// Thuộc tính Slot không có defaultValue → `default: null`; thuộc tính Slot, Instance swap kèm `preferred` (tên component được nhận).
const SET_ID = '<componentSetId>';

const cache = {};
async function vn(id) { if (!id) return null; if (!(id in cache)) { const v = await figma.variables.getVariableByIdAsync(id); cache[id] = v ? v.name : id; } return cache[id]; }
async function paintVar(ps) { if (!Array.isArray(ps) || !ps.length) return null; const p = ps.find(q => q.visible !== false); if (!p) return null; const b = p.boundVariables && p.boundVariables.color; return b ? await vn(b.id) : (p.type === 'SOLID' ? 'raw' : p.type); }
async function numVar(n, k) { const b = n.boundVariables && n.boundVariables[k]; const e = Array.isArray(b) ? b[0] : b; if (e && e.id) return await vn(e.id); const x = n[k]; return x === figma.mixed ? 'mixed' : (typeof x === 'number' ? Math.round(x * 10) / 10 : null); }
function findVis(root, pred) { const st = [...(root.children || [])]; while (st.length) { const n = st.shift(); if (n.visible === false || n.layoutPositioning === 'ABSOLUTE') continue; if (pred(n)) return n; if ('children' in n && n.type !== 'INSTANCE') st.push(...n.children); } return null; }
// Lớp hiện thật: chính nó và mọi lớp cha tới biến thể đều đang hiện (bỏ chữ trong Tooltip đang tắt).
function shown(n, root) { for (let x = n; x && x !== root; x = x.parent) if (x.visible === false) return false; return true; }
// Thân: biến thể không có nền, viền riêng (Tooltip: khung "Bóng" + mũi tên) thì lấy khung con đầu tiên có nền.
function bodyOf(v) { const has = ps => Array.isArray(ps) && ps.some(q => q.visible !== false); if (has(v.fills) || has(v.strokes)) return v; return findVis(v, n => n.type === 'FRAME' && has(n.fills)) || v; }
// Icon là instance không phải component Base / … hay lớp L0 (.…), vd avatar con trong Avatar Group không tính là icon.
// Instance vòng focus (`.focus / Ring`, kể cả khi lớp tên "Vòng focus") không phải icon: ringIds gom id theo từng biến thể.
const ringIds = new Set();
const isIcon = n => n.type === 'INSTANCE' && !/^(Base \/|\.)/.test(n.name) && n.name !== 'Vòng focus' && !ringIds.has(n.id);
const RING_NAME = '.focus / Ring';
const isRingEffect = e => e.type === 'DROP_SHADOW' && !e.radius && !(e.offset && (e.offset.x || e.offset.y));
async function effectList(n, pred) { const out = []; for (const e of n.effects || []) { if (e.visible === false || !pred(e)) continue; const b = e.boundVariables && e.boundVariables.color; out.push((b ? await vn(b.id) : 'raw') + (e.spread ? ' · lan ' + e.spread : '')); } return out.length ? out.join(' + ') : null; }
// Bóng nổi: tên effect style (shadow/xs…) nếu có, không thì "raw". Bóng viền focus kiểu cũ (0 blur, 0 lệch) không tính.
async function shadowOf(n) { if (!(n.effects || []).some(e => e.visible !== false && (e.type === 'DROP_SHADOW' || e.type === 'INNER_SHADOW') && !isRingEffect(e))) return null; const st = typeof n.effectStyleId === 'string' && n.effectStyleId ? await figma.getStyleByIdAsync(n.effectStyleId) : null; return st ? st.name : 'raw'; }
async function mainName(n) { const m = await n.getMainComponentAsync(); return m ? (m.parent && m.parent.type === 'COMPONENT_SET' ? m.parent.name : m.name) : null; }
// Instance `.focus / Ring` đang hiện trong biến thể (null nếu không có). Không đi vào instance L1 lồng; đi vào instance đặt tự do.
async function findRing(root) {
  const st = [...(root.children || [])];
  while (st.length) {
    const n = st.shift(); if (n.visible === false) continue;
    if (n.type === 'INSTANCE') { if (await mainName(n) === RING_NAME) return n; if (n.layoutPositioning !== 'ABSOLUTE') continue; }
    if ('children' in n) st.push(...n.children);
  }
  return null;
}
// Đọc vòng: hình con ĐẦU TIÊN có bóng (hoặc nét). Bóng tên biến chứa "gap" = khe (bản cũ, token đã bỏ DEC-327); bóng còn lại = vòng, dày = lan − lan của khe
// (hoặc biến gắn vào spread). Không bóng thì lấy nét: màu = biến của nét, dày = strokeWeight.
async function ringOf(r) {
  const all = [r, ...r.findAll(n => n.visible !== false)];
  const withFx = all.find(n => (n.effects || []).some(e => e.visible !== false && e.type !== 'LAYER_BLUR' && e.type !== 'BACKGROUND_BLUR'));
  let color = null, width = null, gap = null;
  if (withFx) {
    const fx = [];
    for (const e of withFx.effects) { if (e.visible === false || e.type === 'LAYER_BLUR' || e.type === 'BACKGROUND_BLUR') continue; const bc = e.boundVariables && e.boundVariables.color, bs = e.boundVariables && e.boundVariables.spread; fx.push({ name: bc ? await vn(bc.id) : 'raw', spread: e.spread || 0, spreadVar: bs ? await vn(bs.id) : null }); }
    const g = fx.find(x => /(^|\/)gap$/.test(x.name)), rg = fx.filter(x => x !== g).sort((a, b) => b.spread - a.spread)[0];
    if (g) gap = g.name + (g.spreadVar ? ' · ' + g.spreadVar : g.spread ? ' · ' + g.spread : '');
    if (rg) { color = rg.name; width = rg.spreadVar || (rg.spread ? Math.round((rg.spread - (g ? g.spread : 0)) * 10) / 10 : null); }
  } else {
    const withStroke = all.find(n => Array.isArray(n.strokes) && n.strokes.some(q => q.visible !== false));
    if (withStroke) { color = await paintVar(withStroke.strokes); width = await numVar(withStroke, 'strokeWeight'); }
    const gapNode = all.find(n => Array.isArray(n.fills) && n.fills.some(q => q.visible !== false && q.boundVariables && q.boundVariables.color));
    if (gapNode) { const nm = await paintVar(gapNode.fills); if (/(^|\/)gap$/.test(nm || '')) gap = nm; }
  }
  if (!color && !gap) return null;
  return [color, width != null ? 'dày ' + width : null, gap ? 'khe ' + gap : null].filter(Boolean).join(' · ');
}
// Tên component được nhận (preferred values của Slot, Instance swap): key → tên, tra trên trang của set (DS v2 gom L0 · L1 trên một trang).
let keyNames = null;
async function preferredNames(list) {
  if (!Array.isArray(list) || !list.length) return null;
  if (!keyNames) { keyNames = {}; for (const c of figma.currentPage.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] })) if (!(c.type === 'COMPONENT' && c.parent && c.parent.type === 'COMPONENT_SET')) keyNames[c.key] = c.name; }
  return list.map(x => keyNames[x.key] || String(x.key).slice(0, 8));
}

const set = await figma.getNodeByIdAsync(SET_ID);
{ let pg = set; while (pg && pg.type !== 'PAGE') pg = pg.parent; if (pg) await figma.setCurrentPageAsync(pg); }
const defs = set.componentPropertyDefinitions;
const props = [];
for (const [k, d] of Object.entries(defs)) {
  let def = d.defaultValue === undefined ? null : d.defaultValue;   // Slot không có defaultValue
  if (d.type === 'INSTANCE_SWAP') { const c = await figma.getNodeByIdAsync(d.defaultValue); def = c ? (c.parent && c.parent.type === 'COMPONENT_SET' ? c.parent.name + ' · ' + c.name : c.name) : d.defaultValue; }
  const pr = { name: k.split('#')[0], type: d.type, default: def, options: d.variantOptions || null };
  if (d.type === 'SLOT' || d.type === 'INSTANCE_SWAP') { const pf = await preferredNames(d.preferredValues); if (pf) pr.preferred = pf; }
  props.push(pr);
}
const axes = props.filter(p => p.type === 'VARIANT').map(p => p.name);
const colorKeys = axes.filter(a => a !== 'Size');
const metricKeys = axes.filter(a => a !== 'State');
const colors = {}, metrics = {}, textBy = {};
for (const v of set.children) {
  const p = v.variantProperties;
  const ck = colorKeys.map(a => p[a]).join(' · '), mk = metricKeys.map(a => p[a]).join(' · ');
  ringIds.clear(); const ringNode = await findRing(v); if (ringNode) ringIds.add(ringNode.id);
  if (!colors[ck]) {
    const b = bodyOf(v); const t = findVis(v, n => n.type === 'TEXT'); const ic = findVis(v, isIcon); const dot = findVis(v, n => n.type === 'ELLIPSE');
    let iconColor = null; if (ic) { const vec = ic.findOne(n => Array.isArray(n.strokes) && n.strokes.length || Array.isArray(n.fills) && n.fills.length); if (vec) iconColor = await paintVar(vec.strokes && vec.strokes.length ? vec.strokes : vec.fills); } else if (dot) iconColor = await paintVar(dot.fills);
    // Vòng focus: instance `.focus / Ring` (DEC-213); cũ hơn: bóng 0-blur trên chính biến thể, hoặc trên lớp con "Vòng focus" (Button, DEC-206).
    const ring = v.children.find(c => c.name === 'Vòng focus' && c.visible !== false);
    const effect = ringNode ? await ringOf(ringNode) : (await effectList(v, isRingEffect) || (ring ? await effectList(ring, () => true) : null));
    colors[ck] = { bg: await paintVar(b.fills), border: await paintVar(b.strokes), text: t ? await paintVar(t.fills) : null, icon: iconColor, effect, shadow: await shadowOf(v) || (b !== v ? await shadowOf(b) : null) };
  }
  if (!metrics[mk]) {
    const b = bodyOf(v), m = {};
    for (const k of ['height', 'width']) m[k] = await numVar(v, k);
    for (const k of ['paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom', 'itemSpacing', 'topLeftRadius', 'maxWidth', 'strokeWeight']) { m[k] = await numVar(v, k); if ((m[k] === null || m[k] === 0) && b !== v) m[k] = await numVar(b, k); }
    if (v.primaryAxisSizingMode === 'AUTO') m.width = 'ôm nội dung';
    const ic = findVis(v, n => isIcon(n) || n.type === 'ELLIPSE'); if (ic) m.icon = await numVar(ic, 'width');
    metrics[mk] = m;
  }
  for (const t of v.findAll(n => n.type === 'TEXT' && shown(n, v))) { const s = typeof t.textStyleId === 'string' && t.textStyleId ? await figma.getStyleByIdAsync(t.textStyleId) : null; (textBy[t.name] = textBy[t.name] || []).push([p, s ? s.name : 'raw', t.parent && t.parent !== v ? t.parent.name : '']); }
}
const text = {};
for (const [name, rows] of Object.entries(textBy)) {
  if (new Set(rows.map(r => r[1])).size === 1) { text[name] = rows[0][1]; continue; }
  // style đổi theo trục nào thì tách theo trục đó (vd Label theo Type, Initials theo Size)
  const ax = axes.find(a => { const m = {}; return rows.every(([pp, st]) => (m[pp[a]] = m[pp[a]] || st) === st); });
  // Component đơn (không trục): không có trục để tách → tách theo tên lớp cha của chữ (chữ ngay dưới biến thể: không nhãn), không để "()" rỗng.
  for (const [pp, st, par] of rows) { const tag = ax ? pp[ax] : (metricKeys.length ? metricKeys.map(a => pp[a]).join(' · ') : par); text[tag ? name + ' (' + tag + ')' : name] = st; }
}
return { name: set.name, id: set.id, key: set.key, description: set.description, variants: set.children.length, axes, colorKeys, metricKeys, props, colors, metrics, text };
