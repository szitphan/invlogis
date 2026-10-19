// Xuất dữ liệu một component set DS v2 để sinh phần máy của tài liệu (DEC-118, DEC-183).
// Chạy bằng use_figma (Plugin API), CHỈ ĐỌC. Cách dùng: thay SET_ID, gửi toàn văn làm `code`,
// lưu kết quả JSON vào file rồi chạy: python3 _scripts/ds-v2-component-doc.py <file.json> <file.md>
// Kết quả: tên, mô tả, thuộc tính, trục biến thể, số biến thể, token theo phần:
//   colors  — gom theo các trục KHÔNG phải Size (vd Type × State): nền, viền, chữ, icon, vòng focus.
//   metrics — gom theo các trục còn lại trừ State (vd Content × Size): cao, rộng, lề, khoảng cách, bo.
//   text    — text style của từng lớp chữ (tách theo biến thể nếu mỗi biến thể một style).
// Bỏ qua lớp đang ẩn (thuộc tính bật/tắt như Status, Edit) và lớp đặt tự do (ABSOLUTE: lớp phủ, huy hiệu).
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
const isIcon = n => n.type === 'INSTANCE' && !/^(Base \/|\.)/.test(n.name);
async function effectVars(n) { const out = []; for (const e of n.effects || []) { if (e.visible === false) continue; const b = e.boundVariables && e.boundVariables.color; out.push((b ? await vn(b.id) : 'raw') + (e.spread ? ' · lan ' + e.spread : '')); } return out.length ? out.join(' + ') : null; }

const set = await figma.getNodeByIdAsync(SET_ID);
{ let pg = set; while (pg && pg.type !== 'PAGE') pg = pg.parent; if (pg) await figma.setCurrentPageAsync(pg); }
const defs = set.componentPropertyDefinitions;
const props = [];
for (const [k, d] of Object.entries(defs)) {
  let def = d.defaultValue;
  if (d.type === 'INSTANCE_SWAP') { const c = await figma.getNodeByIdAsync(d.defaultValue); def = c ? (c.parent && c.parent.type === 'COMPONENT_SET' ? c.parent.name + ' · ' + c.name : c.name) : d.defaultValue; }
  props.push({ name: k.split('#')[0], type: d.type, default: def, options: d.variantOptions || null });
}
const axes = props.filter(p => p.type === 'VARIANT').map(p => p.name);
const colorKeys = axes.filter(a => a !== 'Size');
const metricKeys = axes.filter(a => a !== 'State');
const colors = {}, metrics = {}, textBy = {};
for (const v of set.children) {
  const p = v.variantProperties;
  const ck = colorKeys.map(a => p[a]).join(' · '), mk = metricKeys.map(a => p[a]).join(' · ');
  if (!colors[ck]) {
    const b = bodyOf(v); const t = findVis(v, n => n.type === 'TEXT'); const ic = findVis(v, isIcon); const dot = findVis(v, n => n.type === 'ELLIPSE');
    let iconColor = null; if (ic) { const vec = ic.findOne(n => Array.isArray(n.strokes) && n.strokes.length || Array.isArray(n.fills) && n.fills.length); if (vec) iconColor = await paintVar(vec.strokes && vec.strokes.length ? vec.strokes : vec.fills); } else if (dot) iconColor = await paintVar(dot.fills);
    // Vòng focus: bóng trên chính biến thể, hoặc trên lớp con "Vòng focus" (Button, DEC-206).
    const ring = v.children.find(c => c.name === 'Vòng focus' && c.visible !== false);
    colors[ck] = { bg: await paintVar(b.fills), border: await paintVar(b.strokes), text: t ? await paintVar(t.fills) : null, icon: iconColor, effect: await effectVars(v) || (ring ? await effectVars(ring) : null) };
  }
  if (!metrics[mk]) {
    const b = bodyOf(v), m = {};
    for (const k of ['height', 'width']) m[k] = await numVar(v, k);
    for (const k of ['paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom', 'itemSpacing', 'topLeftRadius', 'maxWidth']) { m[k] = await numVar(v, k); if ((m[k] === null || m[k] === 0) && b !== v) m[k] = await numVar(b, k); }
    if (v.primaryAxisSizingMode === 'AUTO') m.width = 'ôm nội dung';
    const ic = findVis(v, n => isIcon(n) || n.type === 'ELLIPSE'); if (ic) m.icon = await numVar(ic, 'width');
    metrics[mk] = m;
  }
  for (const t of v.findAll(n => n.type === 'TEXT' && shown(n, v))) { const s = typeof t.textStyleId === 'string' && t.textStyleId ? await figma.getStyleByIdAsync(t.textStyleId) : null; (textBy[t.name] = textBy[t.name] || []).push([p, s ? s.name : 'raw']); }
}
const text = {};
for (const [name, rows] of Object.entries(textBy)) {
  if (new Set(rows.map(r => r[1])).size === 1) { text[name] = rows[0][1]; continue; }
  // style đổi theo trục nào thì tách theo trục đó (vd Label theo Type, Initials theo Size)
  const ax = axes.find(a => { const m = {}; return rows.every(([pp, st]) => (m[pp[a]] = m[pp[a]] || st) === st); });
  for (const [pp, st] of rows) text[name + ' (' + (ax ? pp[ax] : metricKeys.map(a => pp[a]).join(' · ')) + ')'] = st;
}
return { name: set.name, id: set.id, key: set.key, description: set.description, variants: set.children.length, axes, colorKeys, metricKeys, props, colors, metrics, text };
