// Xuất dữ liệu một component set DS v2 để sinh phần máy của tài liệu (DEC-118, DEC-183).
// Chạy bằng use_figma (Plugin API), CHỈ ĐỌC. Cách dùng: thay SET_ID, gửi toàn văn làm `code`,
// lưu kết quả JSON vào file rồi chạy: python3 _scripts/ds-v2-component-doc.py <file.json> <file.md>
// Kết quả: tên, mô tả, thuộc tính, trục biến thể, số biến thể, token theo phần:
//   colors  — gom theo các trục KHÔNG phải Size (vd Type × State): nền, viền, chữ, icon, vòng focus.
//   metrics — gom theo các trục còn lại trừ State (vd Content × Size): cao, rộng, lề, khoảng cách, bo.
//   text    — text style của từng lớp chữ.
const SET_ID = '<componentSetId>';

const cache = {};
async function vn(id) { if (!id) return null; if (!(id in cache)) { const v = await figma.variables.getVariableByIdAsync(id); cache[id] = v ? v.name : id; } return cache[id]; }
async function paintVar(ps) { if (!Array.isArray(ps) || !ps.length) return null; const p = ps.find(q => q.visible !== false); if (!p) return null; const b = p.boundVariables && p.boundVariables.color; return b ? await vn(b.id) : (p.type === 'SOLID' ? 'raw' : p.type); }
async function numVar(n, k) { const b = n.boundVariables && n.boundVariables[k]; const e = Array.isArray(b) ? b[0] : b; if (e && e.id) return await vn(e.id); const x = n[k]; return x === figma.mixed ? 'mixed' : (typeof x === 'number' ? Math.round(x * 10) / 10 : null); }
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
const colors = {}, metrics = {}, text = {};
for (const v of set.children) {
  const p = v.variantProperties;
  const ck = colorKeys.map(a => p[a]).join(' · '), mk = metricKeys.map(a => p[a]).join(' · ');
  if (!colors[ck]) {
    const t = v.findOne(n => n.type === 'TEXT'); const ic = v.findOne(n => n.type === 'INSTANCE');
    let iconColor = null; if (ic) { const vec = ic.findOne(n => Array.isArray(n.strokes) && n.strokes.length || Array.isArray(n.fills) && n.fills.length); if (vec) iconColor = await paintVar(vec.strokes && vec.strokes.length ? vec.strokes : vec.fills); }
    colors[ck] = { bg: await paintVar(v.fills), border: await paintVar(v.strokes), text: t ? await paintVar(t.fills) : null, icon: iconColor, effect: await effectVars(v) };
  }
  if (!metrics[mk]) {
    const m = {}; for (const k of ['height', 'width', 'paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom', 'itemSpacing', 'topLeftRadius']) m[k] = await numVar(v, k);
    if (v.primaryAxisSizingMode === 'AUTO') m.width = 'ôm nội dung';
    const ic = v.findOne(n => n.type === 'INSTANCE'); if (ic) m.icon = await numVar(ic, 'width');
    metrics[mk] = m;
  }
  for (const t of v.findAll(n => n.type === 'TEXT')) { if (!text[t.name]) { const s = typeof t.textStyleId === 'string' && t.textStyleId ? await figma.getStyleByIdAsync(t.textStyleId) : null; text[t.name] = s ? s.name : 'raw'; } }
}
return { name: set.name, id: set.id, key: set.key, description: set.description, variants: set.children.length, axes, colorKeys, metricKeys, props, colors, metrics, text };
