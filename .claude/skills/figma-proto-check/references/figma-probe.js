// figma-probe.js — đo 1 frame Figma cùng khuôn với _scripts/proto-probe.js (/figma-proto-check).
//
// Chạy bằng Figma MCP chính thức `use_figma` (Plugin API thật — có fontWeight, textDecoration;
// figma_read của reqwise KHÔNG trả hai thứ này, xem .claude/rules/ui-review.md Mục 2).
// Read-only: không sửa node nào; tự chuyển sang trang chứa frame. Trước khi gọi: nạp skill figma:figma-use, skillNames "figma-use".
//
// Cách dùng: thay __FRAME_ID__ bằng node id (frame màn/state, hoặc main component/variant khi chạy
// --before), dán cả file vào `code`. MỘT frame mỗi lần gọi — use_figma cắt kết quả > 20 KB.
// Kết quả lưu nguyên văn ra _workspace/proto-check/{feature}/figma-{screen}[--{state}].json;
// proto-figma-diff.py tự giải nén dạng gọn này.
//
// Dạng gọn: n = [{k:"t"|"b", p:<chỉ số cha>, r:[x,y,w,h], ...}], c = bảng component.
// Node nằm trong instance không giữ id thật (sửa ở main component), chỉ giữ `in` = chỉ số instance gốc.

const FRAME_ID = "__FRAME_ID__";

const hex = (p) => {
  if (!p || p.type !== "SOLID" || p.visible === false || (p.opacity ?? 1) === 0) return null;
  const c = p.color; const h = (v) => Math.round(v * 255).toString(16).padStart(2, "0");
  const o = p.opacity ?? 1;
  return "#" + h(c.r) + h(c.g) + h(c.b) + (o < 0.999 ? h(o) : "");
};
const firstPaint = (arr) => (Array.isArray(arr) ? arr.map(hex).find(Boolean) || null : null);

const comps = [], compKey = new Map(), compOfInst = new Map();
async function compIdx(inst) {
  if (compOfInst.has(inst.id)) return compOfInst.get(inst.id);
  let idx = null;
  try {
    const mc = await inst.getMainComponentAsync();
    if (mc) {
      const set = mc.parent && mc.parent.type === "COMPONENT_SET" ? mc.parent : null;
      let pg = mc; while (pg && pg.type !== "PAGE") pg = pg.parent;
      const key = (set || mc).id + "|" + (set ? mc.name : "");
      if (!compKey.has(key)) {
        compKey.set(key, comps.length);
        comps.push({ name: set ? set.name : mc.name, variant: set ? mc.name : undefined, id: (set || mc).id, page: pg ? pg.name.trim() : undefined });
      }
      idx = compKey.get(key);
    }
  } catch (e) { /* để trống: script coi như khung tự dựng */ }
  compOfInst.set(inst.id, idx);
  return idx;
}

function roleOf(name, cname) {
  const s = (cname || "") + " " + name;
  if (/checkbox/i.test(s)) return "checkbox";
  if (/radio/i.test(s)) return "radio";
  if (/(text ?field|input|ô nhập|ô mật khẩu|textarea|select|combobox)/i.test(s)) return "input";
  if (/button/i.test(cname || "") || /^nút/i.test(name)) return "button"; // "Nút gửi lại link" là nút, không phải link
  if (/\blink\b/i.test(s)) return "link";
  if (/button|nút/i.test(s)) return "button";
  if (/^icon|\/icon|icon\//i.test(s)) return "icon";
  return undefined;
}

const frame = await figma.getNodeByIdAsync(FRAME_ID);
if (!frame) return { error: "không thấy node " + FRAME_ID };
// Frame ở trang khác trang đang mở → chuyển trang (absoluteRenderBounds cần trang đã nạp).
let pg = frame; while (pg && pg.type !== "PAGE") pg = pg.parent;
if (pg && figma.currentPage !== pg) await figma.setCurrentPageAsync(pg);
const shadowOf = (node) => {
  const e = "effects" in node && Array.isArray(node.effects) ? node.effects.find((x) => x.type === "DROP_SHADOW" && x.visible !== false) : null;
  if (!e) return null;
  const c = e.color, h = (v) => Math.round(v * 255).toString(16).padStart(2, "0");
  return ["#" + h(c.r) + h(c.g) + h(c.b) + (c.a < 0.999 ? h(c.a) : ""), e.offset.x, e.offset.y, e.radius, e.spread || 0];
};
// Icon = instance nhỏ (≤ 48px), không có chữ, bên trong là hình vẽ. Lấy màu nét/màu tô đầu tiên.
const iconInfo = (node) => {
  const b = node.absoluteBoundingBox;
  if (!b || b.width > 48 || b.height > 48) return null;
  if (node.findOne((x) => x.type === "TEXT")) return null;
  const v = node.findOne((x) => (x.type === "VECTOR" || x.type === "BOOLEAN_OPERATION" || x.type === "ELLIPSE" || x.type === "LINE") && x.visible !== false);
  if (!v) return null;
  return { col: firstPaint(v.strokes) || firstPaint(v.fills) };
};
const F = frame.absoluteBoundingBox;
const R = (b) => b ? [Math.round(b.x - F.x), Math.round(b.y - F.y), Math.round(b.width), Math.round(b.height)] : null;
const n = [];

async function walk(node, parent, instIdx, cIdx) {
  if (node.visible === false) return;
  if (node !== frame && !node.absoluteRenderBounds && node.type !== "FRAME" && node.type !== "INSTANCE") return;
  const inside = instIdx !== undefined;
  if (node.type === "TEXT") {
    const segs = node.getStyledTextSegments(["fontName", "fontWeight", "fontSize", "textDecoration", "fills", "lineHeight", "letterSpacing", "textCase"]);
    const s = segs[0];
    const lh = s.lineHeight.unit === "PIXELS" ? s.lineHeight.value : s.lineHeight.unit === "PERCENT" ? Math.round(s.fontSize * s.lineHeight.value) / 100 : undefined;
    const box = R(node.absoluteBoundingBox), rb = R(node.absoluteRenderBounds) || box;
    const t = { k: "t", p: parent, r: [rb[0], box[1], rb[2], box[3]], t: node.characters.replace(/\s+/g, " ").trim(),
      f: s.fontName.family, s: s.fontSize, w: s.fontWeight, lh, col: hex(s.fills && s.fills[0]) || undefined };
    if (s.textDecoration !== "NONE") t.dec = s.textDecoration;
    if (s.textCase === "UPPER") t.up = 1;
    if (node.textAlignHorizontal !== "LEFT") t.al = node.textAlignHorizontal;
    const ls = s.letterSpacing.unit === "PIXELS" ? s.letterSpacing.value : s.fontSize * s.letterSpacing.value / 100;
    if (Math.abs(ls) > 0.05) t.ls = Math.round(ls * 100) / 100;
    if (segs.length > 1) t.seg = segs.map((g) => [g.characters, g.fontWeight, hex(g.fills && g.fills[0]), g.textDecoration]);
    if (inside) { t.in = instIdx; t.c = cIdx; } else t.id = node.id;
    n.push(t);
    return;
  }
  if (node.type === "VECTOR" || node.type === "BOOLEAN_OPERATION" || node.type === "STAR" || node.type === "POLYGON") return;
  const isInst = node.type === "INSTANCE" && node !== frame;
  const myC = isInst ? await compIdx(node) : cIdx;
  const ico = isInst ? iconInfo(node) : null;
  if (ico) {
    // Icon: ghi 1 dòng rồi dừng, không đi vào hình vẽ bên trong.
    const b = { k: "b", p: parent, r: R(node.absoluteBoundingBox), role: "icon", ic: myC !== null ? comps[myC].name : node.name, id: node.id };
    if (ico.col) b.icol = ico.col;
    if (myC !== null) b.c = myC;
    if (cIdx !== null && cIdx !== undefined) b.pc = cIdx;
    if (inside) b.in = instIdx;
    n.push(b);
    return;
  }
  const hasImg = "fills" in node && Array.isArray(node.fills) && node.fills.some((f) => f.type === "IMAGE" && f.visible !== false);
  const sh = shadowOf(node);
  const fill = "fills" in node ? firstPaint(node.fills) : null;
  const stroke = "strokes" in node ? firstPaint(node.strokes) : null;
  const auto = "layoutMode" in node && node.layoutMode !== "NONE";
  const role = roleOf(node.name, isInst && myC !== null ? comps[myC].name : undefined);
  // Trong instance chỉ giữ khung có nền/viền hoặc là control; khung bố cục thuần bỏ cho gọn.
  const keep = node === frame || isInst || fill || stroke || hasImg || sh || (!inside && auto) || (inside && role);
  let me = parent;
  if (keep) {
    const b = { k: "b", p: parent, r: R(node.absoluteBoundingBox) };
    if (role) b.role = role;
    if (hasImg) b.role = "image";
    if (sh) b.sh = sh;
    if (fill) b.fill = fill;
    if (stroke) { b.st = stroke; if (typeof node.strokeWeight === "number") b.sw = node.strokeWeight; }
    const rad = typeof node.cornerRadius === "number" ? node.cornerRadius : ("topLeftRadius" in node ? node.topLeftRadius : 0);
    if (rad) b.rad = rad;
    if (auto) {
      const pad = [node.paddingTop, node.paddingRight, node.paddingBottom, node.paddingLeft];
      if (pad.some((v) => v)) b.pad = pad;
      if (node.itemSpacing) b.gap = node.itemSpacing;
      b.dir = node.layoutMode === "VERTICAL" ? "V" : "H";
    }
    if (isInst || node === frame || !inside) { b.id = node.id; b.nm = node.name; }
    if (isInst && myC !== null) b.c = myC;
    if (inside && !isInst) { b.in = instIdx; b.c = cIdx; }
    if (isInst) b.root = 1;
    me = n.length;
    n.push(b);
  }
  const nextInst = isInst ? me : instIdx;
  if ("children" in node) for (const ch of node.children) await walk(ch, me, nextInst, myC);
}
await walk(frame, null, undefined, null);
return { frameId: frame.id, name: frame.name, root: [Math.round(F.width), Math.round(F.height)], c: comps, n };
