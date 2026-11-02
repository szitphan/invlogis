#!/usr/bin/env python3
"""Đối chiếu giá trị của bản preview HTML (vẽ tự do) với foundation DS v2 — gate vòng 3 của
/figma-component --html.

Đầu vào: design-system/components/_work/{slug}/page.json
  "css"       CSS của component — bị chấm toàn bộ: mọi px / mã màu trần phải có dòng trong "values".
  "cssScreen" CSS của khung màn mẫu (bảng, lưới, chữ giữ chỗ) — không chấm, không lên Figma.
  "tokenFamilies" (tuỳ chọn) tiền tố token riêng component được dùng, vd ["nav", "tab"]. Mặc định: các từ
               của slug + tên phần.
  "values"    mỗi giá trị preview dùng, gắn với chỗ nó nằm trong CSS:
  {"id": "tag.height.web.md", "part": "Container", "prop": "height", "platform": "Web", "size": "MD",
   "value": 24, "sel": ".tg", "control": false, "interactive": true}
  {"part": "Label", "prop": "color", "role": "text", "value": "#404040", "on": "#FFFFFF", "sel": ".tg b"}
  {"part": "Nền", "prop": "color", "cssProp": "--fg2", "sel": ".pv", "role": "text", "value": "#525252"}
  {"part": "Nền", "prop": "color", "cssProp": "--fg2", "sel": ".pv[data-theme=dark]", "theme": "Dark", …}
  sel     bộ chọn CSS y như trong "css" (bắt buộc — preview "Theo foundation" ghi đè đúng chỗ này); list khi
          cùng giá trị nằm ở nhiều rule (vd [".sbx.hv", ".sbx:hover"])
  cssProp thuộc tính CSS thật khi khác prop (biến cục bộ "--fg2", "padding-left"…); có thể là list
  tpl     khuôn giá trị khi thuộc tính ghép nhiều phần, $ = giá trị token: "inset 0 -2px 0 $"
  token   token mong muốn khi nhiều token trùng giá trị (vd "type/caption/size" thay "type/code/size")
  noOverride  lý do không ghi đè được trên preview (vd độ dày vạch vẽ bằng box-shadow) — thay cho sel
  tokenRole   khi role = decorative mà vẫn cần kiểm token đúng nghĩa (đường kẻ → border)
  "cssIgnore" (khoá trang) [{"sel", "props": [...], "why"}] — khai báo không hiện trên hình ở tổ hợp đã chốt mà máy
              không tự thấy (bị rule khác ghi đè ở mọi chỗ dùng). Bắt buộc có why; trang review in ra để user soát.
  role    text (cần 4,5:1; large=true → 3:1; hint=true → chỉ báo) · icon | border | fill (3:1, phần mang nghĩa)
          · decorative (không đo tương phản). Role còn dùng để kiểm token đúng nghĩa (chữ không gắn token nền).
  theme   Light (mặc định) | Dark — màu Dark so với bảng màu Dark.

Xếp mỗi giá trị vào 5 nhóm:
  ok          ✅ trùng token đúng nghĩa (thang chung space/ radius/ type/ control/… hoặc token mang tên component)
  near        ↔  gần token, hoặc trùng số nhưng token khác nghĩa / chỉ có Primitive (component không gắn Primitive)
  new         ＋ không có token gần — cần token mới hoặc sửa preview
  conflict    ⛔ vi phạm luật đã chốt (tương phản, cao control, vùng chạm, focus, nút có bóng)
  undeclared  ⛔ giá trị trần trong "css" (hoặc style inline trong data-cmp / bảng biến thể) chưa khai — sửa page.json

Mỗi dòng ra kèm "bind" (token gắn được khi khớp), "to" (đích khi kéo về token có sẵn: token, giá trị, biến CSS),
"visible" (đổi có nhìn thấy không: ΔE > 2, lệch > 2px, đổi cỡ/độ đậm chữ) và "resolved" (kết quả theo
answers.json) — trang review dùng để vẽ preview "Theo foundation", vòng 4 dùng để ghi spec.

Dùng:
  python3 _scripts/ds-foundation-check.py design-system/components/_work/tag            # in báo cáo
  python3 _scripts/ds-foundation-check.py design-system/components/_work/tag --write    # ghi check.json
  python3 _scripts/ds-foundation-check.py design-system/components/_work/tag --bind     # đề xuất sel cho dòng thiếu
  python3 _scripts/ds-foundation-check.py design-system/components/_work/tag --bind --write-bind  # ghi sel chắc chắn
  python3 _scripts/ds-foundation-check.py design-system/components/_work/tag --declare   # gắn sel theo phần đã học + khai
                                                                               # tự động giá trị trần còn lại ("auto")
Dòng coi là đã quyết khi answers.json (dump từ db của artifact) có doc "foundation-{id}" có choice.
Phải quyết: ⛔ ＋ và ↔ nhìn thấy; ↔ không nhìn thấy mà chưa chọn → tự kéo về token. ⛔ Chưa khai và dòng
thiếu sel không quyết bằng lựa chọn — sửa page.json.
Exit 1 khi còn việc chưa xong; 0 khi qua; 2 khi lỗi đầu vào.
"""
import json
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "design-system/tokens.json"

CAT_LABEL = {"ok": "✅ Khớp", "near": "↔ Lệch nhỏ", "new": "＋ Cần token mới", "conflict": "⛔ Xung đột luật",
             "undeclared": "⛔ Chưa khai"}

COLOR_PROPS = {"color", "fill", "background", "bg", "border-color", "text-color", "icon-color", "stroke"}
POOLS = {
    # prop -> (scope Figma của biến Platform, thang primitive cùng loại)
    "padding": ("GAP", "space"), "padding-x": ("GAP", "space"), "padding-y": ("GAP", "space"),
    "padding-top": ("GAP", "space"), "padding-bottom": ("GAP", "space"), "padding-left": ("GAP", "space"),
    "padding-right": ("GAP", "space"), "gap": ("GAP", "space"), "margin": ("GAP", "space"),
    "radius": ("CORNER_RADIUS", "radius"),
    "font-size": ("FONT_SIZE", None), "line-height": ("LINE_HEIGHT", None),
    "height": ("WIDTH_HEIGHT", "space"), "width": ("WIDTH_HEIGHT", "space"), "min-height": ("WIDTH_HEIGHT", "space"),
    "min-width": ("WIDTH_HEIGHT", "space"), "max-width": ("WIDTH_HEIGHT", "space"), "size": ("WIDTH_HEIGHT", "space"),
    "icon-size": ("WIDTH_HEIGHT", "space"),
    "border-width": ("STROKE_FLOAT", None), "focus-width": ("STROKE_FLOAT", None), "focus-offset": (None, None),
}
FIXED_EXTRA = {"border-width": {1: "viền 1px (mặc định)", 2: "viền 2px (đang gõ, focus)"},
               "focus-offset": {2: "focus/offset"}, "focus-width": {2: "focus/width"}}
WEIGHTS = {400: "Regular", 500: "Medium", 600: "Semi Bold", 700: "Bold"}
# Tiền tố token Platform dùng chung cho mọi component (thang, không mang tên component)
GENERIC_NUM = {"radius", "space", "layout", "form", "touch", "control", "focus", "type", "icon", "width"}
# Thang chung hợp từng loại thuộc tính (chiều rộng không lấy token cỡ icon, v.v.)
PROP_FAMILIES = {
    "width": {"width", "layout", "form"}, "min-width": {"width", "layout", "form"}, "max-width": {"width", "layout", "form"},
    "height": {"control", "touch", "layout", "form"}, "min-height": {"control", "touch", "layout", "form"},
    "size": {"control", "icon", "touch"}, "icon-size": {"icon"},
    "padding": {"space", "control", "layout", "form"}, "gap": {"space", "control", "layout", "form"},
    "margin": {"space", "layout", "form"}, "radius": {"radius"}, "font-size": {"type"}, "line-height": {"type"},
}
ROLE_WORDS = {
    "text": {"text", "fg", "label", "on"},
    "icon": {"icon", "fg", "text"},
    "border": {"border", "line", "stroke", "focus", "ring", "divider"},
    "fill": {"bg", "surface", "fill", "action", "overlay", "track", "bar", "solid", "selected", "hover", "pressed",
             "muted", "badge"},
}
ROLE_LABEL = {"text": "chữ", "icon": "icon", "border": "viền", "fill": "nền"}
# prop khai → thuộc tính CSS ghi đè ở preview "Theo foundation"
CSS_PROPS = {"padding-x": ["padding-left", "padding-right"], "padding-y": ["padding-top", "padding-bottom"],
             "radius": ["border-radius"], "size": ["width", "height"], "icon-size": ["width", "height"],
             "bg": ["background"], "text-color": ["color"], "icon-color": ["color"],
             "focus-width": ["outline-width"], "focus-offset": ["outline-offset"], "shadow": ["box-shadow"]}
# Thuộc tính CSS không chấm (bố cục, chuyển động — không phải giá trị foundation)
IGNORE_CSS = re.compile(r"^(transform|transition.*|animation.*|z-index|opacity|flex.*|grid.*|order|top|left|right|"
                        r"bottom|inset.*|position|content|cursor|filter|backdrop-filter|aspect-ratio|overflow.*|"
                        r"display|white-space|text-overflow|text-align|vertical-align|letter-spacing|mask.*|"
                        r"clip-path|pointer-events|user-select|object-fit|place-.*|align-.*|justify-.*|"
                        r"scroll.*|will-change|visibility|box-sizing|list-style.*|word-.*|font-family|"
                        r"font-variant.*|font-feature.*|text-decoration.*|text-transform|outline-style|"
                        r"border-style|border-collapse|background-(image|repeat|position|size|clip)|"
                        r"stroke-(linecap|linejoin|dasharray)|appearance|resize|caret-color|accent-color)$")
RAW_PX = re.compile(r"(?<![\w.#-])(-?\d*\.?\d+)px")
RAW_HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")
RAW_RGB = re.compile(r"rgba?\([^)]*\)")


def die(msg):
    print(f"ds-foundation-check: {msg}", file=sys.stderr)
    sys.exit(2)


def css_var(name):
    return "var(--" + name.replace("/", "-") + ")"


def words(s):
    return {w for w in re.split(r"[^a-z0-9]+", str(s or "").lower()) if w}


# ---------- token index ----------

def load_tokens():
    d = json.loads(TOKENS.read_text())
    c = d["collections"]
    prim_color = dict(c["Primitives"]["color"])
    prim_num = dict(c["Primitives"]["number"])
    sem = c["Semantic"]["color"]
    comp = c.get("Component", {}).get("color", {})

    def color_of(ref, mode="Light", depth=0):
        if depth > 6 or ref is None:
            return None
        if isinstance(ref, dict):
            return color_of(ref.get(mode) or ref.get("Value") or ref.get("Light"), mode, depth + 1)
        ref = str(ref).strip()
        if ref.startswith("#"):
            return ref.upper()[:7]
        for coll in (prim_color, sem, comp):
            if ref in coll:
                return color_of(coll[ref], mode, depth + 1)
        return None

    colors = {"Light": {}, "Dark": {}}  # theme -> hex -> [(name, collection)]
    for coll_name, coll in (("Semantic", sem), ("Component", comp)):
        for name, v in coll.items():
            for theme in ("Light", "Dark"):
                hx = color_of(v, theme)
                if hx:
                    colors[theme].setdefault(hx, []).append((name, coll_name))
    prim_hex = {}
    for name, v in prim_color.items():
        hx = color_of(v)
        if hx:
            prim_hex.setdefault(hx, []).append(name)

    def num_of(ref):
        if isinstance(ref, (int, float)):
            return ref
        if isinstance(ref, str) and ref in prim_num:
            return prim_num[ref]
        return None

    plat = {}  # name -> {"Web": n, "Mobile": n, "scopes": [...]}
    for name, v in c["Platform"]["vars"].items():
        plat[name] = {"Web": num_of(v.get("Web")), "Mobile": num_of(v.get("Mobile")), "scopes": v.get("scopes") or []}
    effects = {}
    for name, e in (d.get("effectStyles") or {}).items():
        parts = [f"{s.get('x', 0)}px {s.get('y', 0)}px {s.get('blur', 0)}px {s.get('spread', 0)}px "
                 f"{css_var(s['var']) if s.get('var') else s.get('color')}" for s in e.get("shadows") or []]
        effects[name] = ", ".join(parts) or "none"
    return {"colors": colors, "prim_hex": prim_hex, "prim_num": prim_num, "plat": plat, "effects": effects,
            "color_of": color_of, "version": d.get("version")}


# ---------- màu ----------

def hex_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = hex_rgb(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def lab(h):
    def ch(v):
        v /= 255
        return ((v + 0.055) / 1.055) ** 2.4 if v > 0.04045 else v / 12.92
    r, g, b = (ch(x) for x in hex_rgb(h))
    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
    y = (r * 0.2126 + g * 0.7152 + b * 0.0722)
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e(a, b):
    return math.dist(lab(a), lab(b))


def norm_hex(v):
    if not isinstance(v, str):
        return None
    v = v.strip()
    if not v.startswith("#") or len(v) not in (4, 7, 9):
        return None
    if len(v) == 4:
        return "#" + "".join(c * 2 for c in v[1:]).upper()
    return v.upper()[:7]


def color_role(row):
    if row.get("tokenRole") in ROLE_WORDS:  # decorative nhưng vẫn kiểm token đúng nghĩa (vd đường kẻ = token viền)
        return row["tokenRole"]
    r = row.get("role")
    if r in ROLE_WORDS:
        return r
    if r == "decorative" or not r:
        p = row.get("prop")
        return {"color": "text", "text-color": "text", "icon-color": "icon", "border-color": "border",
                "stroke": "border", "background": "fill", "bg": "fill", "fill": "fill"}.get(p) \
            if not str(row.get("cssProp") or "").startswith("--") else None
    return None


def related(prefix, fams):
    return any(w.startswith(prefix) or prefix.startswith(w) for w in fams if len(w) >= 3) if prefix else False


def color_allowed(name, coll, role, fams):
    """(được dùng, lý do không) — Semantic theo vai trò, Component chỉ khi mang tên component."""
    if coll == "Component" and not related(name.split("/")[0], fams):
        return False, f"token riêng của {name.split('/')[0]}"
    if role and not (words(name) & ROLE_WORDS[role]):
        return False, f"token không dành cho {ROLE_LABEL[role]}"
    return True, ""


def pick_name(cands, fams, part, hint=None):
    """hint = trường "token" của dòng values: token mong muốn khi nhiều token trùng số (vd type/caption thay type/code)."""
    if hint and hint in cands:
        return hint
    pw = words(part)
    return max(cands, key=lambda n: (related(n.split("/")[0], fams) * 3 + len(words(n) & pw), -len(n)))


def check_color(row, tk, fams):
    theme = row.get("theme") or "Light"
    hx = norm_hex(row.get("value")) or tk["color_of"](row.get("value"), theme)
    if not hx:
        return {"cat": "new", "note": f"không đọc được màu `{row.get('value')}` (ghi #RRGGBB hoặc tên token)"}
    role = color_role(row)
    table = tk["colors"][theme]
    allowed = {h: [n for n, cl in lst if color_allowed(n, cl, role, fams)[0]] for h, lst in table.items()}
    allowed = {h: v for h, v in allowed.items() if v}
    rolenote = "" if role or row.get("role") == "decorative" else "chưa khai role — không kiểm được token đúng nghĩa; "
    if hx in allowed:
        name = pick_name(allowed[hx], fams, row.get("part"), row.get("token"))
        return {"cat": "ok", "tokens": allowed[hx][:4], "bind": {"token": name, "css": css_var(name)},
                "note": rolenote.rstrip("; ")}
    if not allowed:
        return {"cat": "new", "note": "không có token màu nào hợp vai trò này"}
    best = min(allowed, key=lambda k: delta_e(hx, k))
    de = delta_e(hx, best)
    name = pick_name(allowed[best], fams, row.get("part"))
    to = {"token": name, "value": best, "css": css_var(name)}
    if hx in table:  # trùng màu nhưng token khác nghĩa
        others = [n for n, _ in table[hx]]
        why = color_allowed(table[hx][0][0], table[hx][0][1], role, fams)[1]
        return {"cat": "near", "to": to, "visible": de > 2,
                "note": f"{rolenote}trùng màu với {', '.join(others[:2])} nhưng {why}; token đúng nghĩa gần nhất "
                        f"{name} ({best}), ΔE {de:.1f}"}
    if de <= 5:
        return {"cat": "near", "to": to, "visible": de > 2, "note": f"{rolenote}ΔE {de:.1f}"}
    note = f"{rolenote}gần nhất {name} ({best}), ΔE {de:.1f}"
    if hx in tk["prim_hex"]:
        note = f"trùng primitive {tk['prim_hex'][hx][0]} nhưng chưa có token nghĩa; " + note
    return {"cat": "new", "to": to, "visible": True, "note": note}


# ---------- số ----------

def fmt(n):
    return str(int(n)) if float(n).is_integer() else f"{n:.1f}"


SMALL_WIDTH = 120  # bề rộng dưới mức này là cỡ phần tử (icon, chấm, nút), không phải khung → không so với width/*


def num_family(base, val=None):
    if base in ("width", "min-width", "max-width") and val is not None and val < SMALL_WIDTH:
        return {"control", "icon", "touch", "space"}
    return PROP_FAMILIES.get(base, GENERIC_NUM)


def num_pools(prop, platform, tk, fams, val=None):
    """allowed / other (Platform khác nghĩa) / prim: value -> [names]"""
    scope, prim = POOLS.get(prop, ("WIDTH_HEIGHT", "space"))
    modes = ["Web", "Mobile"] if platform == "Both" else [platform]
    allowed, other, prims = {}, {}, {}
    for name, v in tk["plat"].items():
        if scope and scope not in v["scopes"]:
            continue
        vals = {v[m] for m in modes}
        if len(vals) != 1 or None in vals:
            continue
        n = vals.pop()
        pre = name.split("/")[0]
        base = "padding" if prop.startswith("padding") else prop
        generic = num_family(base, val) & GENERIC_NUM
        (allowed if pre in generic or related(pre, fams) else other).setdefault(n, []).append(name)
    if prim:
        for name, n in tk["prim_num"].items():
            if name.startswith(prim + "/"):
                prims.setdefault(n, []).append(name)
    for n, label in FIXED_EXTRA.get(prop, {}).items():
        allowed.setdefault(n, []).append(label)
    return allowed, other, prims


def num_css(name, n):
    return css_var(name) if "/" in name and " " not in name else f"{fmt(n)}px"


def check_num(row, tk, fams):
    prop = row["prop"]
    platform = row.get("platform") or "Web"
    try:
        val = float(row["value"])
    except (TypeError, ValueError):
        return {"cat": "new", "note": f"giá trị không phải số: `{row.get('value')}`"}
    if prop == "font-weight":
        if int(val) in WEIGHTS:
            return {"cat": "ok", "tokens": [WEIGHTS[int(val)]], "bind": {"token": WEIGHTS[int(val)], "css": fmt(val)}}
        best = min(WEIGHTS, key=lambda w: abs(w - val))
        return {"cat": "near", "visible": True, "to": {"token": WEIGHTS[best], "value": best, "css": str(best)}}
    if prop == "radius" and val >= 999:
        val = 9999.0
    allowed, other, prims = num_pools(prop, platform, tk, fams, val)
    if val in allowed:
        name = pick_name(allowed[val], fams, row.get("part"), row.get("token"))
        return {"cat": "ok", "tokens": allowed[val][:4], "bind": {"token": name, "css": num_css(name, val)}}
    if not allowed:
        return {"cat": "new", "note": "không có thang token cho thuộc tính này"}
    # gợi ý kéo về: chỉ thang chung (token riêng component chỉ nhận khi khớp đúng số)
    base = "padding" if prop.startswith("padding") else prop
    generic = num_family(base, val) & GENERIC_NUM
    sug = {n: [x for x in names if x.split("/")[0] in generic or "/" not in x] for n, names in allowed.items()}
    sug = {n: v for n, v in sug.items() if v} or allowed
    best = min(sug, key=lambda n: abs(n - val))
    diff = abs(best - val)
    name = pick_name(sug[best], fams, row.get("part"))
    to = {"token": name, "value": best, "css": num_css(name, best)}
    typo = prop in ("font-size", "line-height")
    visible = diff > 0 if typo else diff > 2
    close = diff <= 2 or diff <= best * 0.1
    if diff > max(8, val * 0.25):
        # token chung gần nhất quá xa — kéo về sẽ vỡ hình, không gợi ý (user 28/10: width 16 → width/xxs 320)
        why = f"thang chung gần nhất {name} = {fmt(best)} lệch quá xa, không kéo về được"
        if val in other:
            why = f"trùng số với {', '.join(other[val][:2])} nhưng đó là token của component khác; " + why
        return {"cat": "new", "to": None, "visible": True, "note": why + " — chọn thêm token mới (giữ hình preview)"}
    cat = "near" if close else "new"
    if val in other:
        return {"cat": cat, "to": to, "visible": visible,
                "note": f"trùng số với {', '.join(other[val][:2])} nhưng đó là token của component khác; "
                        f"thang chung gần nhất {name} = {fmt(best)}"}
    if val in prims:
        return {"cat": cat, "to": to, "visible": visible,
                "note": f"chỉ có primitive {prims[val][0]} — component không gắn primitive (architecture Mục 7); "
                        f"thang chung gần nhất {name} = {fmt(best)}"}
    if close:
        return {"cat": "near", "to": to, "visible": visible, "note": f"lệch {fmt(val - best)}"}
    return {"cat": "new", "to": to, "visible": True, "note": f"thang chung gần nhất {name} = {fmt(best)}"}


# ---------- luật ----------

FIX_MAX_DE = 40  # ngưỡng ΔE gợi ý màu sửa tương phản


def plat_value(tk, mode, name):
    v = tk["plat"].get(name)
    return v[mode] if v else None


def rules(row, tk, fams):
    """list (luật, chi tiết, cách sửa | None)."""
    out = []
    prop = row["prop"]
    platform = row.get("platform") or "Web"
    modes = ["Web", "Mobile"] if platform == "Both" else [platform]
    theme = row.get("theme") or "Light"
    if prop in COLOR_PROPS and row.get("on") and row.get("role") != "decorative":
        fg = norm_hex(row.get("value")) or tk["color_of"](row.get("value"), theme)
        bg = norm_hex(row.get("on")) or tk["color_of"](row.get("on"), theme)
        if fg and bg:
            r = contrast(fg, bg)
            role = row.get("role", "text")
            need = 3.0 if role in ("border", "icon", "fill") or row.get("large") else 4.5
            row["_contrast"] = round(r, 2)
            if r < need and not row.get("hint"):
                crole = color_role(row)
                status_part = "status" in (row.get("part") or "").lower()
                cands = [(h, n) for h, lst in tk["colors"][theme].items() for n, cl in lst
                         if color_allowed(n, cl, crole, fams)[0] and contrast(h, bg) >= need
                         and (status_part or not n.startswith("color/status/"))]
                fix = None
                if cands:
                    h, n = min(cands, key=lambda x: delta_e(fg, x[0]))
                    # màu đạt chuẩn gần nhất vẫn khác hẳn (vd nền xám → xanh success, user 29/10) → không gợi ý
                    if delta_e(fg, h) <= FIX_MAX_DE:
                        fix = {"token": n, "value": h, "css": css_var(n)}
                out.append(("Tương phản (foundations Mục 3.4, WCAG 1.4.3/1.4.11)",
                            f"{r:.2f}:1 < {need}:1 ({role} trên {bg})", fix))
    if prop in ("height", "min-height") and row.get("control"):
        for mode in modes:
            names = {s: plat_value(tk, mode, f"control/height/{s}") for s in ("sm", "md", "lg")}
            try:
                v = float(row["value"])
            except (TypeError, ValueError):
                continue
            if v not in names.values():
                s, n = min(((s, n) for s, n in names.items() if n), key=lambda x: abs(x[1] - v))
                out.append(("Cao control (DEC-173)", f"{mode}: {fmt(v)} không thuộc {sorted(int(a) for a in names.values() if a)}",
                            {"token": f"control/height/{s}", "value": n, "css": css_var(f"control/height/{s}")}))
    if prop in ("height", "min-height", "size", "hit-area") and row.get("interactive"):
        for mode in modes:
            need = plat_value(tk, mode, "touch/min") or (44 if mode == "Mobile" else 24)
            try:
                v = float(row.get("hitArea") or row["value"])
            except (TypeError, ValueError):
                continue
            if v < need:
                out.append(("Vùng chạm (foundations Mục 9, DEC-138)",
                            f"{mode}: {fmt(v)} < {fmt(need)} — thêm vùng bấm vô hình (khai hitArea)", None))
    if prop == "focus-width" and float(row.get("value", 0)) != 2:
        out.append(("Vòng focus 2px (foundations Mục 9)", f"{row['value']}px", {"token": "focus/width", "value": 2, "css": "2px"}))
    if prop == "focus-offset" and float(row.get("value", 0)) != 2:
        out.append(("Khe focus 2px (DEC-241)", f"{row['value']}px", {"token": "focus/offset", "value": 2, "css": "2px"}))
    if prop == "shadow" and row.get("control") and row.get("value") not in (None, "", "none"):
        out.append(("Nút phẳng, không bóng (DEC-260)", str(row.get("value")), {"token": "không bóng", "value": "none", "css": "none"}))
    return out


def check_row(row, tk, fams):
    prop = row.get("prop")
    if prop in COLOR_PROPS:
        res = check_color(row, tk, fams)
    elif prop == "shadow":
        v = row.get("value")
        if v in (None, "", "none"):
            res = {"cat": "ok", "tokens": ["không bóng"], "bind": {"token": "không bóng", "css": "none"}}
        elif v in tk["effects"]:
            res = {"cat": "ok", "tokens": [v], "bind": {"token": v, "css": tk["effects"][v]}}
        else:
            res = {"cat": "new", "visible": True, "to": {"token": "shadow/xs", "value": "shadow/xs", "css": tk["effects"].get("shadow/xs")},
                   "note": f"bóng tự do `{v}` — chọn shadow/xs · lg · xl theo vai hoặc bậc khác trong thang shadow/*"}
    else:
        res = check_num(row, tk, fams)
    broken = rules(row, tk, fams)
    cp = row.get("cssProp") or CSS_PROPS.get(prop) or [prop]
    out = {
        "id": row.get("id") or ".".join(str(x) for x in (row.get("part"), prop, row.get("platform") or "Web",
                                                            row.get("size") or "", row.get("state") or "",
                                                            "dark" if row.get("theme") == "Dark" else "") if x
                                        ).lower().replace(" ", "-"),
        "part": row.get("part"), "prop": prop, "platform": row.get("platform") or "Web",
        "size": row.get("size") or "", "state": row.get("state") or "", "theme": row.get("theme") or "Light",
        "value": row.get("value"), "sel": row.get("sel"), "cssProps": cp if isinstance(cp, list) else [cp],
        "tpl": row.get("tpl"), "noOverride": row.get("noOverride"),
        # cách soi phần tử chỉ hiện khi tương tác: {"state": "scope", "set": {"ck": "…"}, "add": {"<sel>": "<class>"}}
        "soi": row.get("soi"),
        "at": row.get("at"),  # chỗ để soi cho dòng noOverride (không ghi đè được nhưng phải chỉ được trên hình)
        "cat": "conflict" if broken else res["cat"], "tokens": res.get("tokens", []),
        "bind": res.get("bind"), "to": res.get("to"), "visible": bool(res.get("visible")),
        "suggest": (f"{res['to']['token']} ({res['to']['value']})" if res.get("to") else None),
        "rules": [f"{r}: {d}" for r, d, _ in broken], "note": res.get("note", ""),
    }
    fixes = [f for _, _, f in broken if f]
    if broken:
        out["fix"] = fixes[0] if fixes else None
        out["visible"] = True
    if "_contrast" in row:
        out["contrast"] = row["_contrast"]
    return out


# ---------- quét CSS ----------

def norm_sel(s):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    s = re.sub(r"\s*([>+~,])\s*", r"\1", s)
    return s.replace('"', "").replace("'", "")


def parse_css(css):
    """[(selector, prop, value)] — bỏ comment, đi vào @media / @supports."""
    css = re.sub(r"/\*.*?\*/", "", css or "", flags=re.S)
    out = []

    def walk(text):
        i = 0
        while i < len(text):
            j = text.find("{", i)
            if j < 0:
                return
            head = text[i:j].strip()
            depth, k = 1, j + 1
            while k < len(text) and depth:
                depth += {"{": 1, "}": -1}.get(text[k], 0)
                k += 1
            body = text[j + 1:k - 1]
            if head.startswith("@"):
                if head.startswith(("@media", "@supports", "@container")):
                    walk(body)
            else:
                for decl in body.split(";"):
                    if ":" in decl:
                        p, v = decl.split(":", 1)
                        out.append((head, p.strip().lower(), v.strip()))
            i = k
    walk(css)
    return out


def css_family(p):
    p = p.lower()
    if p.startswith("--"):
        return p
    if p.startswith("padding"):
        return "padding"
    if p.startswith("margin"):
        return "margin"
    if "radius" in p:
        return "radius"
    if p in ("font", "font-size", "line-height", "font-weight"):
        return "font"
    if p.endswith("height"):
        return "height"
    if p.endswith("width") and not p.startswith(("border", "outline")):
        return "width"
    if p.startswith("border"):
        return "border"
    if p.startswith("outline"):
        return "outline"
    if p in ("background", "background-color", "fill"):
        return "background"
    if p in ("gap", "row-gap", "column-gap"):
        return "gap"
    if p == "box-shadow":
        return "shadow"
    return p


ROW_FAMILY = {"padding": "padding", "padding-x": "padding", "padding-y": "padding", "padding-top": "padding",
              "padding-bottom": "padding", "padding-left": "padding", "padding-right": "padding", "margin": "margin",
              "gap": "gap", "radius": "radius", "font-size": "font", "line-height": "font", "font-weight": "font",
              "height": "height", "min-height": "height", "width": "width", "min-width": "width", "max-width": "width",
              "size": "size", "icon-size": "size", "border-width": "border", "border-color": "border",
              "focus-width": "outline", "focus-offset": "outline", "color": "color", "text-color": "color",
              "icon-color": "color", "background": "background", "bg": "background", "fill": "background",
              "stroke": "stroke", "shadow": "shadow"}


def row_families(row):
    cp = row.get("cssProp")
    if cp:
        fams = {css_family(x) for x in (cp if isinstance(cp, list) else [cp])}
    else:
        fams = {ROW_FAMILY.get(row.get("prop"), css_family(row.get("prop") or ""))}
    if "size" in fams:
        fams |= {"width", "height"}
    if row.get("prop") == "icon-color":
        fams |= {"background", "stroke"}
    if row.get("prop") == "border-color":
        fams |= {"outline"}
    return fams


def raw_tokens(prop, value):
    """Giá trị trần trong một khai báo: [('px', 12.0) | ('hex', '#AABBCC') | ('rgb', 'rgba(...)')]"""
    v = re.sub(r"var\([^)]*\)", "", value)
    v = re.sub(r"url\([^)]*\)", "", v)
    out = []
    fam = css_family(prop)
    for m in RAW_PX.finditer(v):
        n = float(m.group(1))
        if n == 0 or (n == 1 and fam in ("border", "outline")):
            continue
        out.append(("px", abs(n)))
    for m in RAW_HEX.finditer(v):
        out.append(("hex", norm_hex(m.group(0)) or m.group(0).upper()))
    for m in RAW_RGB.finditer(v):
        out.append(("rgb", m.group(0)))
    return out


def sels(r):
    v = r.get("sel")
    return [norm_sel(x) for x in (v if isinstance(v, list) else [v]) if x]


def covered_keys(values):
    keys = set()
    for r in values:
      for s in sels(r):
        v = r.get("value")
        hx = norm_hex(v) if isinstance(v, str) else None
        for f in row_families(r):
            if hx:
                keys.add((s, f, hx))
            elif isinstance(v, (int, float)):
                keys.add((s, f, float(9999 if r.get("prop") == "radius" and v >= 999 else v)))
            elif isinstance(v, str):
                keys.add((s, f, v.strip()))
    return keys


def off_variant(sel, pick):
    """Rule chỉ áp cho phương án không được chốt (mọi vế của selector list đều đòi [data-Dn=x] khác pick)."""
    if not pick:
        return False
    parts = [x for x in re.split(r",(?![^\[(]*[\])])", sel) if x.strip()]

    def off(part):
        for d, o in re.findall(r"\[data-(D\d+)=\"?([a-z])\"?\]", part):
            if pick.get(d) and pick[d] != o:
                return True
        for d, o in re.findall(r":not\(\[data-(D\d+)=\"?([a-z])\"?\]\)", part):
            if pick.get(d) == o:
                return True
        return False
    return all(off(x) for x in parts)


TOKEN_VARS = None


def token_vars():
    """Tên biến CSS có trong design-system/tokens.css (var(--x) tới đây = đã qua token)."""
    global TOKEN_VARS
    if TOKEN_VARS is None:
        css = (ROOT / "design-system/tokens.css")
        TOKEN_VARS = set(re.findall(r"(--[\w-]+)\s*:", css.read_text())) if css.exists() else set()
    return TOKEN_VARS


VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def _hidden_by(attrs, pick):
    if pick is None:  # xem mọi phương án
        return False
    sh, an = attrs.get("data-show"), attrs.get("data-any")
    if sh and any(pick.get(d) and pick[d] != o for d, o in re.findall(r"(D\d+):([a-z])", sh)):
        return True
    if an:
        terms = re.findall(r"(D\d+):([a-z])", an)
        return bool(terms) and not any(pick.get(d) == o for d, o in terms)
    return False


class _Walk(HTMLParser):
    """Duyệt HTML có lồng nhau: phần tử nằm TRONG khối bị ẩn (data-show phương án đã loại) cũng bị ẩn."""
    def __init__(self, pick, platform):
        super().__init__(convert_charrefs=True)
        self.pick, self.platform, self.stack, self.els = pick, platform, [], []

    def _el(self, tag, attrs, push):
        a = {k: (v or "") for k, v in attrs}
        par = self.stack[-1] if self.stack else None
        # hình nhỏ lồng .pv.pvm mang lựa chọn riêng (data-Dn) và ẩn theo data-mshow của khung gần nhất
        loc = par["loc"] if par else None
        if "pvm" in a.get("class", "").split():
            loc = {k[5:].upper(): v for k, v in a.items() if re.fullmatch(r"data-d\d+", k, re.I)}  # parser hạ chữ thường
        hid = (par["hid"] if par else False) or _hidden_by(a, self.pick)
        if not hid and loc is not None and a.get("data-mshow"):
            hid = self.pick is not None and _hidden_by({"data-show": a["data-mshow"]}, loc)
        e = {"tag": tag, "cls": set(a.get("class", "").split()), "attrs": a, "shown": not hid,
             "platform": self.platform, "parent": par["el"] if par else None}
        self.els.append(e)
        if push:
            self.stack.append({"hid": hid, "el": e, "loc": loc})

    def handle_starttag(self, tag, attrs):
        self._el(tag, attrs, tag not in VOID_TAGS)

    def handle_startendtag(self, tag, attrs):
        self._el(tag, attrs, False)

    def handle_endtag(self, tag):
        if tag not in VOID_TAGS and self.stack:
            self.stack.pop()


def page_elements(page, pick):
    """Mọi phần tử trên màn demo + bảng biến thể, kèm cờ hiện ở tổ hợp đã chốt và nền tảng (web/mobile)."""
    pv = page.get("preview") or {}
    srcs = [(s.get("html") or "", "mobile" if s.get("device") == "mobile" else "web") for s in page.get("screens") or []]
    srcs += [(h, "mobile" if b.get("platform") == "mobile" else "web")
             for b in pv.get("blocks") or [] for h in (b.get("frames") or [b.get("html") or ""])]
    els = []
    for html, plat in srcs:
        w = _Walk(pick, plat)
        w.feed(html)
        els += w.els
    if pick:
        css_hide(page, pick, els)
    return els


def css_hide(page, pick, els):
    """Ẩn theo CSS gắn phương án: luật display:none có [data-Dn=o] đúng pick (vd .pv[data-D6=c] .sb .sbs) → phần tử
    khớp coi như không lên hình. Luật ẩn mặc định không gắn phương án (.fly{display:none}) thì bỏ qua — tương tác bật lại."""
    if not pick:
        return
    for sel, prop, val in parse_css(page.get("css") or ""):
        if prop != "display" or val.strip() != "none":
            continue
        for part in [x.strip() for x in re.split(r",(?![^\[(]*[\])])", sel) if x.strip()]:
            terms = re.findall(r"\[data-(D\d+)=\"?([a-z])\"?\]", part)
            if not terms or any(pick.get(d) != o for d, o in terms) or re.search(r":(?!not)[\w-]", part):
                continue
            rest = re.sub(r"^\.pv(\[[^\]]*\])*\s*", "", part)
            if re.search(r"\[data-(?!D\d)", part.split(" ")[0]):  # còn điều kiện trạng thái trên .pv
                continue
            for e in els:
                if e["shown"] and _chain_ok(rest, e):
                    e["shown"] = False
                    # con cháu cũng ẩn
            # lan xuống con cháu
            for e in els:
                a = e["parent"]
                while a is not None and e["shown"]:
                    if not a["shown"]:
                        e["shown"] = False
                    a = a["parent"]


def _chain_ok(part, e):
    chain = [c for c in re.split(r"\s*[>+~]\s*|\s+", re.sub(r"[^\s>+~]+\s*[+~]\s*", "", part)) if c]
    if not chain or not _compound_ok(chain[-1], e):
        return False
    a, rest = e["parent"], chain[:-1]
    while rest and a is not None:
        if _compound_ok(rest[-1], a):
            rest = rest[:-1]
        a = a["parent"]
    return not rest


def hidden_classes(page, pick):
    """Class chỉ nằm trên phần tử bị ẩn ở tổ hợp đã chốt (data-show / data-any theo điểm Dn, tính cả khối cha)."""
    if not pick:
        return set()
    els = page_elements(page, pick)
    seen = {c for e in els for c in e["cls"]}
    shown = {c for e in els if e["shown"] for c in e["cls"]}
    return seen - shown


def shown_classes(page, pick):
    """Class có trên ít nhất một phần tử đang hiện ở tổ hợp chốt — CSS cho class ngoài tập này không lên hình."""
    return {c for e in page_elements(page, pick or {}) if e["shown"] for c in e["cls"]}


def _compound_ok(comp, e):
    """So một vế đơn (tag.cls[attr="v"]) với một phần tử — bỏ :hover/::before."""
    comp = re.sub(r"::?[\w-]+(\([^)]*\))?", "", comp)
    m = re.match(r"^([a-zA-Z][\w-]*)?", comp)
    if m.group(1) and m.group(1).lower() != e["tag"]:
        return False
    if not set(re.findall(r"\.([\w-]+)", comp)) <= e["cls"]:
        return False
    for k, v in re.findall(r'\[([\w-]+)(?:=\"?([^\]"]*)\"?)?\]', comp):
        if k not in e["attrs"] or (v and e["attrs"][k] != v):
            return False
    return True


def sel_on_page(sel, els, platform=""):
    """Bộ chọn có trỏ tới ít nhất một phần tử đang hiện (đúng nền tảng) không — xét vế cuối và tổ tiên gần
    đúng theo chuỗi tổ tiên. Gate "mọi dòng sai lệch phải soi được trên màn demo hoặc bảng biến thể" (user 29/10)."""
    plat = platform.lower() if platform.lower() in ("web", "mobile") else ""
    sel = ",".join(sel) if isinstance(sel, list) else (sel or "")
    for part in [x.strip() for x in re.split(r",(?![^\[(]*[\])])", sel) if x.strip()]:
        part = re.sub(r"^\.pv(\[[^\]]*\])*\s*", "", part)
        part = re.sub(r"[^\s>+~]+\s*[+~]\s*", "", part)  # anh em (+ ~): chỉ giữ vế sau
        if not part:
            return True
        chain = [c for c in re.split(r"\s*[>+~]\s*|\s+", part) if c]
        for e in els:
            if not e["shown"] or (plat and e["platform"] != plat) or not _compound_ok(chain[-1], e):
                continue
            a, rest = e["parent"], chain[:-1]
            while rest and a is not None:  # tổ tiên khớp lần lượt (coi > như khoảng trắng)
                if _compound_ok(rest[-1], a):
                    rest = rest[:-1]
                a = a["parent"]
            if not rest:
                return True
    return False


def scan_css(page):
    """Khai báo của component còn giá trị chưa khai: số/màu trần, hoặc biến cục bộ của trang (var(--fg2)…).
    Khai báo biến cục bộ trên .pv (--fg2:#525252) là bảng màu nháp — không chấm chỗ định nghĩa, chấm chỗ dùng."""
    values = page.get("values") or []
    keys = covered_keys(values)
    fam_keys = {(s, f) for r in values for s in sels(r) for f in row_families(r)}
    shadow_ok = {s for r in values if r.get("prop") in ("shadow", "border-width") or r.get("tpl") for s in sels(r)}
    pick = (page.get("preview") or {}).get("pick") or {}
    tv = token_vars()
    out = []
    # cascade: cùng bộ chọn (bỏ tiền tố phương án đã chốt) + cùng thuộc tính → chỉ khai báo thắng còn hiện trên hình
    win = {}
    for n, (sel, prop, val) in enumerate(parse_css(page.get("css") or "")):
        for part in [x.strip() for x in re.split(r",(?![^\[(]*[\])])", sel) if x.strip()]:
            chosen = [d for d, o in re.findall(r"\[data-(D\d+)=\"?([a-z])\"?\]", part) if pick.get(d) == o]
            eff = norm_sel(re.sub(r"\.pv\[data-D\d+=\"?[a-z]\"?\]\s*", "", part)) if chosen else norm_sel(part)
            fam = css_family(prop)
            k = (eff, fam) if fam == "font" else (eff, fam, prop)
            pr = (1 if chosen else 0, n)
            if k not in win or pr >= win[k]:
                win[k] = pr
    live = {v for v in win.values()}
    hid = hidden_classes(page, pick)

    live_cls = shown_classes(page, pick) if pick else None

    def dead_part(part):
        last = re.split(r"[\s>+~]+", re.sub(r"\[[^\]]*\]|::?[\w-]+(\([^)]*\))?", "", part.strip()))[-1]
        cls = set(re.findall(r"\.([\w-]+)", last))
        # mọi class trong bộ chọn (kể cả tổ tiên) phải có trên hình — không thì là CSS của phương án không dựng
        every = set(re.findall(r"\.([\w-]+)", re.sub(r"\[[^\]]*\]|::?[\w-]+(\([^)]*\))?", "", part)))
        return bool(cls & hid) or (live_cls is not None and bool(every - live_cls - {"pv"}))
    for n, (sel, prop, val) in enumerate(parse_css(page.get("css") or "")):
        if not any(pr[1] == n for pr in live):
            continue
        if IGNORE_CSS.match(prop) or prop.startswith("--") or off_variant(sel, pick):
            continue
        if all(dead_part(x) for x in re.split(r",(?![^\[(]*[\])])", sel) if x.strip()):
            continue
        if any(norm_sel(ig.get("sel")) == norm_sel(sel) and (not ig.get("props") or prop in ig["props"])
               for ig in page.get("cssIgnore") or []):
            continue
        s, fam = norm_sel(sel), css_family(prop)
        if fam == "shadow" and s in shadow_ok:
            continue
        local = [v for v in re.findall(r"var\((--[\w-]+)", val) if v not in tv]
        if local and (s, fam) not in fam_keys and (s, "size") not in fam_keys:
            out.append({"sel": sel, "prop": prop, "value": val, "raw": f"var({local[0]})"})
            continue
        for kind, x in raw_tokens(prop, val):
            k = float(9999 if fam == "radius" and kind == "px" and x >= 999 else x) if kind == "px" else x
            if kind == "rgb" or (s, fam, k) not in keys:
                out.append({"sel": sel, "prop": prop, "value": val, "raw": f"{fmt(x)}px" if kind == "px" else x})
    return out


class InlineScan(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self, whole):
        super().__init__()
        self.stack, self.whole, self.hits = [], whole, []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        inside = (self.stack[-1] if self.stack else self.whole)
        if "data-frame" in a:
            inside = False
        if "data-cmp" in a:
            inside = True
        st = a.get("style") or ""
        if inside and st:
            for decl in st.split(";"):
                if ":" in decl:
                    p, v = decl.split(":", 1)
                    if not IGNORE_CSS.match(p.strip().lower()) and raw_tokens(p.strip(), v):
                        cls = "." + ".".join((a.get("class") or "").split()) if a.get("class") else ""
                        self.hits.append({"sel": f"(inline) <{tag}{cls}>", "prop": p.strip(), "value": v.strip(),
                                          "raw": "style inline"})
        if tag not in self.VOID:
            self.stack.append(inside)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID and self.stack:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag not in self.VOID and self.stack:
            self.stack.pop()


def scan_inline(page):
    hits = []
    docs = [(s.get("html") or "", False, f"màn {s.get('name') or s.get('id')}") for s in page.get("screens") or []]
    pv = page.get("preview") or {}
    for b in pv.get("blocks") or []:
        for h in (b.get("frames") or [b.get("html") or ""]):
            # bảng có đánh dấu data-cmp → chỉ quét trong data-cmp; chưa đánh dấu → quét cả bảng
            docs.append((h, "data-cmp" not in h, f"bảng biến thể {b.get('title')}"))
    for dm in pv.get("demos") or []:
        docs.append((dm.get("html") or "", False, f"demo {dm.get('name')}"))
    for html, whole, where in docs:
        p = InlineScan(whole)
        p.feed(html)
        for h in p.hits:
            h["where"] = where
            hits.append(h)
    return hits


# ---------- gắn sel ----------

def bind_sel(page):
    """Đề xuất sel cho dòng values thiếu: khai báo cùng họ thuộc tính chứa đúng giá trị."""
    decls = parse_css(page.get("css") or "")
    local = {}
    for sel, prop, val in decls:  # biến cục bộ: .pv (Light) trước, rồi khai báo đầu tiên ở bộ chọn khác
        if prop.startswith("--") and norm_sel(sel) == ".pv":
            local.setdefault(prop, val.strip())
    for sel, prop, val in decls:
        if prop.startswith("--") and "dark" not in sel:
            local.setdefault(prop, val.strip())

    def res(v, k=0):
        return re.sub(r"var\((--[\w-]+)[^)]*\)", lambda m: res(local[m.group(1)], k + 1) if m.group(1) in local and k < 6
                      else m.group(0), v)
    decls = [(sel, prop, res(val)) for sel, prop, val in decls if not prop.startswith("--")]
    sure, unsure = [], []
    for i, r in enumerate(page.get("values") or []):
        if r.get("sel") or r.get("noOverride"):
            continue
        v = r.get("value")
        hx = norm_hex(v) if isinstance(v, str) else None
        fams = row_families(r)
        cands = []
        for sel, prop, val in decls:
            if css_family(prop) not in fams or IGNORE_CSS.match(prop):
                continue
            raws = raw_tokens(prop, val)
            if (hx and ("hex", hx) in raws) or (isinstance(v, (int, float)) and ("px", float(v)) in raws):
                if r.get("cssProp") and prop not in ([r["cssProp"]] if isinstance(r["cssProp"], str) else r["cssProp"]):
                    continue
                cands.append(sel)
        cands = list(dict.fromkeys(cands))
        plat = (r.get("platform") or "").lower()
        if len(cands) > 1 and plat in ("web", "mobile"):
            narrowed = [c for c in cands if f"platform={plat}" in c.replace('"', "")] or \
                       [c for c in cands if "platform=" not in c]
            cands = narrowed or cands
        if len(cands) > 1:  # .pv là chữ gốc của cả trang — chỉ chọn khi không còn chỗ cụ thể hơn
            cands = [c for c in cands if norm_sel(c) != ".pv"] or cands
        if len(cands) > 1 and r.get("theme") == "Dark":
            cands = [c for c in cands if "dark" in c] or cands
        elif len(cands) > 1:
            cands = [c for c in cands if "dark" not in c] or cands
        (sure if len(cands) == 1 else unsure).append((i, r, cands))
    return sure, unsure


def declare(page):
    """--declare: (1) gắn sel cho dòng values thiếu khi ứng viên trùng bộ chọn đã gắn cho cùng phần (học từ dòng chắc chắn);
    (2) khai một dòng values cho mỗi giá trị trần còn lại trong css (tên phần lấy theo bộ chọn đã học, không có thì
    dùng chính bộ chọn). Biến cục bộ var(--x) giải theo khai báo trên .pv (Light). Trả (số dòng gắn, số dòng khai)."""
    from collections import Counter, defaultdict
    vals = page.setdefault("values", [])
    bound = 0
    for _ in range(3):
        learn = defaultdict(Counter)
        for r in vals:
            for x in sels(r):
                learn[r.get("part")][x] += 1
        sure, unsure = bind_sel(page)
        n0 = bound
        for i, r, cands in sure:
            vals[i]["sel"] = cands[0]; bound += 1
        for i, r, cands in unsure:
            hit = [c for c in cands if norm_sel(c) in learn.get(r.get("part"), {})]
            if len(hit) == 1:
                vals[i]["sel"] = hit[0]; bound += 1
        if bound == n0:
            break
    part_of = defaultdict(Counter)
    for r in vals:
        for x in sels(r):
            part_of[x][r.get("part")] += 1
    local = {}
    decl = parse_css(page.get("css") or "")
    for sel, prop, val in decl:  # ưu tiên khai báo trên .pv (Light), rồi tới khai báo đầu tiên ở bộ chọn khác (biến theo tông)
        if norm_sel(sel) == ".pv" and prop.startswith("--"):
            local.setdefault(prop, val.strip())
    for sel, prop, val in decl:
        if prop.startswith("--") and "dark" not in sel:
            local.setdefault(prop, val.strip())

    def res(v, k=0):
        m = re.search(r"var\((--[\w-]+)", v)
        return res(local[m.group(1)], k + 1) if m and m.group(1) in local and k < 6 else v
    added = 0
    for h in scan_css(page):
        sel, prop = h["sel"], h["prop"].lower()
        ns = norm_sel(sel)
        part = part_of[ns].most_common(1)[0][0] if part_of.get(ns) else ns
        plat = "Mobile" if "platform=mobile" in sel.replace('"', "") else "Web" if "platform=web" in sel.replace('"', "") else "Both"
        base = {"part": part, "sel": sel, "platform": plat, "auto": True}
        if "dark" in sel:
            base["theme"] = "Dark"
        fam = css_family(prop)
        new = []
        if fam == "shadow":
            new.append({**base, "prop": "shadow", "value": res(h["value"])})
        elif h["raw"].startswith("var("):
            v = res(h["value"])
            hx = re.search(r"#[0-9a-fA-F]{3,8}", v)
            if hx:
                rp = {"background": "background", "border": "border-color", "outline": "border-color"}.get(fam, "color")
                new.append({**base, "prop": rp, "cssProp": prop, "value": norm_hex(hx.group(0)) or hx.group(0)})
            else:
                for kind, x in raw_tokens(prop, v):
                    new.append({**base, "prop": prop, "value": x})
        else:
            x = h["raw"]
            if x.endswith("px"):
                n = float(x[:-2]); n = int(n) if n == int(n) else n
                if fam == "radius":
                    rp, n = "radius", (9999 if n >= 999 else n)
                elif fam == "font":
                    nums = [float(m) for m in re.findall(r"(-?\d*\.?\d+)px", h["value"])]
                    rp = "line-height" if prop == "font" and len(nums) > 1 and float(n) == nums[1] else \
                        ("font-size" if prop == "font" else prop)
                else:
                    rp = prop
                new.append({**base, "prop": rp, "value": n} | ({"cssProp": prop} if rp != prop else {}))
            elif x.startswith("#"):
                rp = {"background": "background", "border": "border-color", "outline": "border-color"}.get(fam, "color")
                new.append({**base, "prop": rp, "cssProp": prop, "value": x})
        for r in new:
            key = (norm_sel(r["sel"]), r["prop"], str(r["value"]), r.get("theme"))
            if not any((norm_sel(str(v.get("sel") or "")), v.get("prop"), str(v.get("value")), v.get("theme")) == key for v in vals):
                vals.append(r); added += 1
    return bound, added


# ---------- main ----------

def resolve(r, a):
    """Kết quả cuối của một dòng theo lựa chọn — vòng 4 ghi spec theo đây."""
    ch = a.get("choice")
    cat = r["cat"]
    if cat == "ok":
        return {"kind": "token", **(r.get("bind") or {})}
    if cat == "near":
        if ch == 1:
            return {"kind": "new-token", "value": r["value"]}
        if ch == 0 or not r["visible"]:
            return {"kind": "token", **(r.get("to") or {}), "auto": ch is None}
    if cat == "new":
        if ch == 0:
            return {"kind": "new-token", "value": r["value"]}
        if ch == 1:
            return {"kind": "token", **(r.get("to") or {})}
    if cat == "conflict":
        if ch == 0:
            return {"kind": "fix", **(r.get("fix") or {"value": None})}
        if ch == 1:
            return {"kind": "rule-change", "value": r["value"]}
        if ch == 2:
            return {"kind": "exception", "value": r["value"]}
    return {"kind": "pending"}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        die("thiếu đường dẫn _work/{slug} hoặc page.json")
    p = Path(args[0])
    page_path = p / "page.json" if p.is_dir() else p
    if not page_path.exists():
        die(f"không thấy {page_path}")
    page = json.loads(page_path.read_text())
    values = page.get("values") or []
    if not values:
        die("page.json chưa có khoá values — preview phải khai giá trị nó dùng")

    if "--declare" in sys.argv:
        before = json.dumps(page, ensure_ascii=False)
        nb = na = 0
        for _ in range(3):  # khai xong có thể lộ thêm chỗ học được
            b_, a_ = declare(page); nb += b_; na += a_
            if not a_ and not b_:
                break
        # đặt lại tên phần cho dòng auto còn mang tên bộ chọn: cùng bộ chọn (bỏ tiền tố .pv[data-…]) hoặc cùng class chủ
        def core(x):
            return norm_sel(re.sub(r"\.pv(\[[^\]]*\])+\s*", "", x.split(",")[0]))

        def subj(x):
            return re.split(r"[\s>+~]+", re.sub(r"::?[\w-]+(\([^)]*\))?", "", core(x)))[-1]
        names = {}
        for v in page["values"]:
            if not v.get("auto") and v.get("sel") and not str(v.get("part") or ".").startswith((".", ":")):
                for x in sels(v):
                    names.setdefault(core(x), v["part"]); names.setdefault("~" + subj(x), v["part"])
        ren = 0
        for v in page["values"]:
            if v.get("auto") and str(v.get("part") or ".").startswith((".", ":", "(")):
                x = str(v.get("sel") or "")
                nm = names.get(core(x)) or names.get("~" + subj(x))
                if nm:
                    v["part"] = nm; ren += 1
        if ren:
            print(f"--declare: đặt tên phần cho {ren} dòng auto")
        man = covered_keys([v for v in page["values"] if not v.get("auto")])
        keep = [v for v in page["values"] if not v.get("auto") or not (covered_keys([v]) <= man)]
        nd = len(page["values"]) - len(keep); page["values"] = keep
        if nd:
            print(f"--declare: bỏ {nd} dòng auto trùng dòng gốc đã gắn sel")
        print(f"--declare: gắn sel {nb} dòng · khai thêm {na} dòng (đánh dấu \"auto\": true — soát tên phần, role)")
        if json.dumps(page, ensure_ascii=False) != before:
            page_path.write_text(json.dumps(page, ensure_ascii=False, indent=1))
            print(f"Đã ghi {page_path.name}")
        sys.exit(0)

    if "--bind" in sys.argv:
        sure, unsure = bind_sel(page)
        print(f"Gắn sel — {len(sure)} chắc chắn · {len(unsure)} cần chọn tay")
        for i, r, c in unsure:
            print(f"  ? values[{i}] {r.get('part')} · {r.get('prop')} = {r.get('value')}: "
                  f"{' | '.join(c) if c else 'không thấy trong css'}")
        if "--write-bind" in sys.argv:
            for i, r, c in sure:
                page["values"][i]["sel"] = c[0]
            page_path.write_text(json.dumps(page, ensure_ascii=False, indent=1))
            print(f"Đã ghi sel cho {len(sure)} dòng vào {page_path.name}")
        sys.exit(0)

    tk = load_tokens()
    # token riêng component: theo slug + tokenFamilies của trang + tên phần của chính dòng đó
    fams = words(page.get("slug")) | {str(x).lower() for x in page.get("tokenFamilies") or []}
    rows = [check_row(dict(v), tk, fams | words(v.get("part"))) for v in values]
    seen = {}
    for r in rows:  # id trùng → thêm hậu tố
        if r["id"] in seen:
            seen[r["id"]] += 1
            r["id"] = f"{r['id']}-{seen[r['id']]}"
        else:
            seen[r["id"]] = 1
    bad_ig = [ig for ig in page.get("cssIgnore") or [] if not (ig.get("why") or "").strip()]
    if bad_ig:
        die(f"cssIgnore thiếu lý do (why): {', '.join(str(ig.get('sel')) for ig in bad_ig)}")
    undeclared = scan_css(page) + scan_inline(page)
    for n, u in enumerate(undeclared, 1):
        rows.append({"id": f"css.{n}", "part": u.get("where") or u["sel"], "prop": u["prop"], "platform": "",
                     "size": "", "state": "", "theme": "", "value": u["raw"], "sel": u["sel"], "cssProps": [u["prop"]],
                     "cat": "undeclared", "tokens": [], "bind": None, "to": None, "visible": True, "suggest": None,
                     "rules": [], "note": f"`{u['prop']}: {u['value']}` — "
                                          + ("chuyển vào css rồi khai values" if u["raw"] == "style inline"
                                             else "khai một dòng values (sel này), hoặc dời sang cssScreen nếu là khung màn")})

    # kiểm kỹ 7 nhóm (chữ, màu, icon, hiệu ứng, khoảng cách, bo góc, lưới) — _scripts/ds_foundation_audit.py
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import ds_foundation_audit as fa
    for r in rows:
        r.setdefault("group", fa.group_of(r.get("prop"), r.get("part")))
    pick0 = (page.get("preview") or {}).get("pick") or {}
    els = page_elements(page, pick0 or {})
    # dòng values chỉ trỏ vào phần tử nằm trong khối ẩn ở tổ hợp chốt (phương án đã loại)
    # → không phải giá trị của component đã chốt, bỏ khỏi đối chiếu
    if pick0:
        els_all = page_elements(page, None)
        def _off_pick(r):
            sl = ",".join(r["sel"]) if isinstance(r.get("sel"), list) else (r.get("sel") or "")
            return bool(sl) and r["cat"] != "undeclared" and not sel_on_page(sl, els, r.get("platform") or "") \
                and sel_on_page(sl, els_all, r.get("platform") or "")
        dropped = [r for r in rows if _off_pick(r)]
        rows = [r for r in rows if not _off_pick(r)]
        if dropped:
            print(f"Bỏ {len(dropped)} dòng chỉ thuộc phương án đã loại: " + ", ".join(r["id"] for r in dropped[:8])
                  + (" …" if len(dropped) > 8 else ""))
    # dòng kiểm thêm chỉ trỏ vào phương án đã loại (ẩn ở tổ hợp chốt) → không phải sai lệch của component
    rows += [r for r in fa.audit(page, parse_css, TOKENS) if not r.get("sel") or sel_on_page(r["sel"], els)]
    # mọi dòng còn lại phải soi được trên hình (user 29/10) — dòng không trỏ tới phần tử nào đang hiện
    off_page = [r for r in rows if r["cat"] != "undeclared" and (r.get("sel") or r.get("at"))
                and not sel_on_page(r.get("at") or r["sel"], els, r.get("platform") or "")]
    # dòng phải quyết mà không chỉ được chỗ nào trên hình (noOverride thiếu at) → user không nhìn được
    off_page += [r for r in rows if (r["cat"] in ("conflict", "new") or (r["cat"] == "near" and r["visible"]))
                 and not r.get("sel") and not r.get("at")]
    for r in off_page:
        r["offPage"] = True

    answers_path = page_path.parent / "answers.json"
    answers = json.loads(answers_path.read_text()) if answers_path.exists() else {}
    for r in rows:
        a = answers.get(f"foundation-{r['id']}") or {}
        r["decided"] = a.get("choice") is not None
        r["must"] = r["cat"] in ("conflict", "new") or (r["cat"] == "near" and r["visible"])
        if r["cat"] != "undeclared":
            r["resolved"] = resolve(r, a)
    counts = {k: sum(1 for r in rows if r["cat"] == k) for k in CAT_LABEL}
    no_sel = [r for r in rows if r["cat"] != "undeclared" and not r.get("sel") and not r.get("noOverride")]
    open_rows = [r for r in rows if r["must"] and not r["decided"] and r["cat"] != "undeclared"]
    open_rows += [r for r in rows if r["cat"] == "undeclared"]

    groups = fa.summary(rows)
    print(f"Đối chiếu foundation — {page.get('component', page_path.parent.name)} · {len(values)} giá trị khai")
    print(" · ".join(f"{CAT_LABEL[k]} {counts[k]}" for k in CAT_LABEL))
    print("Theo nhóm: " + " · ".join(f"{g['label']} {g['total']} (chờ chọn {g['open']}"
                                    + (f", kiểm thêm {g['audit']}" if g["audit"] else "") + ")" for g in groups.values()))
    for k in ("undeclared", "conflict", "new", "near"):
        sub = [r for r in rows if r["cat"] == k]
        if not sub:
            continue
        print(f"\n{CAT_LABEL[k]}")
        for r in sub:
            where = " · ".join(x for x in (r["part"], r["prop"], r["platform"], r["size"], r["state"]) if x)
            extra = "; ".join(r["rules"]) or r["note"] or (f"đề xuất {r['suggest']}" if r["suggest"] else "")
            tag = " [đã quyết]" if r["decided"] else (" [phải chọn]" if r["must"] and k != "undeclared" else "")
            print(f"  - {r['id']}: {where} = {r['value']} — {extra}{tag}")
    if no_sel:
        print(f"\nThiếu sel (preview Theo foundation không ghi đè được): {len(no_sel)} — chạy --bind")
    if off_page:
        print(f"\nKhông soi được trên hình: {len(off_page)} — sel không trỏ tới phần tử nào đang hiện ở màn demo hay bảng"
              " biến thể (sai nền tảng, chỉ có ở phương án đã loại, hoặc thiếu ô biến thể). Sửa platform/sel hoặc thêm ô:")
        for r in off_page:
            print(f"  - {r['id']}: {r['sel']} ({r.get('platform') or 'mọi nền tảng'})")
    print(f"\nCòn chưa xong: {len(open_rows)} (chưa khai {counts['undeclared']} · chưa quyết "
          f"{len(open_rows) - counts['undeclared']}) · thiếu sel {len(no_sel)} · không soi được {len(off_page)}")

    if "--write" in sys.argv:
        out = page_path.parent / "check.json"
        out.write_text(json.dumps({"tokens_version": tk["version"], "counts": counts, "no_sel": len(no_sel),
                                   "off_page": len(off_page),
                                   "open": len(open_rows),  # backlog đóng task khi "open": 0
                                   "ignored": page.get("cssIgnore") or [],
                                   "groups": groups,
                                   "rows": rows}, ensure_ascii=False, indent=1))
        print(f"Đã ghi {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    sys.exit(1 if open_rows or no_sel or off_page else 0)


if __name__ == "__main__":
    main()
