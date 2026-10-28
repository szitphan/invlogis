#!/usr/bin/env python3
"""Đối chiếu giá trị của bản preview HTML (vẽ tự do) với foundation DS v2 — gate vòng 3 của
/figma-component --html.

Đầu vào: design/v2/components/_work/{slug}/page.json, khoá "values" (preview khai từng giá trị nó dùng):
  {"id": "tag.height.web.md", "part": "Container", "prop": "height", "platform": "Web", "size": "MD",
   "value": 24, "control": false, "interactive": true}
  {"part": "Label", "prop": "color", "role": "text", "value": "#404040", "on": "#FFFFFF"}
  role: text (cần 4,5:1; large=true → 3:1; hint=true → chỉ báo) · icon | border | fill (cần 3:1, phần mang nghĩa)
        · decorative (viền, nền trang trí — không đo tương phản)

Xếp mỗi giá trị vào 4 nhóm:
  ok        ✅ trùng token
  near      ↔  gần một token (đề xuất kéo về)
  new       ＋ không có token gần — cần token mới hoặc sửa preview
  conflict  ⛔ vi phạm luật đã chốt (tương phản, cao control, vùng chạm, focus, nút có bóng)

Dùng:
  python3 _scripts/ds-foundation-check.py design/v2/components/_work/tag            # in báo cáo
  python3 _scripts/ds-foundation-check.py design/v2/components/_work/tag --write    # ghi check.json
Dòng ⛔/＋ coi là đã quyết khi answers.json (dump từ db của artifact) có doc "foundation-{id}" có choice.
Exit 1 khi còn dòng ⛔ hoặc ＋ chưa quyết; 0 khi qua; 2 khi lỗi đầu vào.
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "design/v2/tokens.json"

CAT_LABEL = {"ok": "✅ Khớp", "near": "↔ Lệch nhỏ", "new": "＋ Cần token mới", "conflict": "⛔ Xung đột luật"}

COLOR_PROPS = {"color", "fill", "background", "bg", "border-color", "text-color", "icon-color", "stroke"}
POOLS = {
    # prop -> (scope Figma của biến Platform, có dùng thang primitive không)
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
               "focus-offset": {2: "focus/offset"}}
WEIGHTS = {400: "Regular", 500: "Medium", 600: "Semi Bold", 700: "Bold"}


def die(msg):
    print(f"ds-foundation-check: {msg}", file=sys.stderr)
    sys.exit(2)


# ---------- token index ----------

def load_tokens():
    d = json.loads(TOKENS.read_text())
    c = d["collections"]
    prim_color = dict(c["Primitives"]["color"])
    prim_num = dict(c["Primitives"]["number"])
    sem = c["Semantic"]["color"]
    comp = c["Component"]["color"]

    def color_of(ref, mode="Light", depth=0):
        if depth > 6 or ref is None:
            return None
        if isinstance(ref, dict):
            return color_of(ref.get(mode) or ref.get("Value"), mode, depth + 1)
        ref = str(ref).strip()
        if ref.startswith("#"):
            return ref.upper()[:7]
        if ref in prim_color:
            return color_of(prim_color[ref], mode, depth + 1)
        if ref in sem:
            return color_of(sem[ref], mode, depth + 1)
        if ref in comp:
            return color_of(comp[ref], mode, depth + 1)
        return None

    colors = {}  # hex -> [token names] (Semantic + Component, Light)
    for name, v in list(sem.items()) + list(comp.items()):
        hx = color_of(v, "Light")
        if hx:
            colors.setdefault(hx, []).append(name)
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

    plat = {"Web": [], "Mobile": []}  # (name, value, scopes)
    for name, v in c["Platform"]["vars"].items():
        for mode in ("Web", "Mobile"):
            n = num_of(v.get(mode))
            if n is not None:
                plat[mode].append((name, n, v.get("scopes") or []))
    return {"colors": colors, "prim_hex": prim_hex, "prim_num": prim_num, "plat": plat,
            "effects": set((d.get("effectStyles") or {}).keys()), "color_of": color_of}


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
    if not isinstance(v, str) or not v.strip().startswith("#") or len(v.strip()) not in (4, 7):
        return None
    return "#" + "".join(c * 2 for c in v.strip()[1:]).upper() if len(v.strip()) == 4 else v.strip().upper()


def check_color(row, tk):
    hx = norm_hex(row.get("value"))
    if not hx:
        ref = tk["color_of"](row.get("value"))
        if ref:
            hx = ref
        else:
            return "new", [], None, f"không đọc được màu `{row.get('value')}` (ghi #RRGGBB hoặc tên token)"
    if hx in tk["colors"]:
        return "ok", tk["colors"][hx], None, ""
    best = min(tk["colors"], key=lambda k: delta_e(hx, k))
    de = delta_e(hx, best)
    if de <= 5:
        return "near", [], f"{' / '.join(tk['colors'][best][:3])} ({best})", f"ΔE {de:.1f}"
    note = f"gần nhất {tk['colors'][best][0]} ({best}), ΔE {de:.1f}"
    if hx in tk["prim_hex"]:
        note = f"trùng primitive {tk['prim_hex'][hx][0]} nhưng chưa có token nghĩa; " + note
    return "new", [], None, note


# ---------- số ----------

def check_num(row, tk):
    prop = row["prop"]
    platform = row.get("platform") or "Web"
    try:
        val = float(row["value"])
    except (TypeError, ValueError):
        return "new", [], None, f"giá trị không phải số: `{row.get('value')}`"
    if prop == "font-weight":
        if int(val) in WEIGHTS:
            return "ok", [WEIGHTS[int(val)]], None, ""
        best = min(WEIGHTS, key=lambda w: abs(w - val))
        return "near", [], f"{best} ({WEIGHTS[best]})", ""
    scope, prim = POOLS.get(prop, ("WIDTH_HEIGHT", "space"))
    pool = {}
    modes = ["Web", "Mobile"] if platform == "Both" else [platform]
    for mode in modes:
        for name, n, scopes in tk["plat"].get(mode, []):
            if scope and scope in scopes:
                pool.setdefault(n, []).append(name)
    if prim:
        for name, n in tk["prim_num"].items():
            if name.startswith(prim + "/") and n < 9999:
                pool.setdefault(n, []).append(name)
    for n, label in FIXED_EXTRA.get(prop, {}).items():
        pool.setdefault(n, []).append(label)
    if not pool:
        return "new", [], None, "không có thang token cho thuộc tính này"
    if val in pool:
        return "ok", pool[val][:4], None, ""
    best = min(pool, key=lambda n: abs(n - val))
    diff = abs(best - val)
    if diff <= 2 or diff <= best * 0.1:
        return "near", [], f"{fmt(best)} ({pool[best][0]})", f"lệch {fmt(val - best)}"
    return "new", [], None, f"gần nhất {fmt(best)} ({pool[best][0]})"


def fmt(n):
    return str(int(n)) if float(n).is_integer() else f"{n:.1f}"


def plat_value(tk, mode, name):
    for n_name, n, _ in tk["plat"].get(mode, []):
        if n_name == name:
            return n
    return None


# ---------- luật ----------

def rules(row, tk):
    """Trả về list (luật, chi tiết) bị vi phạm."""
    out = []
    prop = row["prop"]
    platform = row.get("platform") or "Web"
    modes = ["Web", "Mobile"] if platform == "Both" else [platform]
    if prop in COLOR_PROPS and row.get("on") and row.get("role") != "decorative":
        fg, bg = norm_hex(row.get("value")) or tk["color_of"](row.get("value")), \
            norm_hex(row.get("on")) or tk["color_of"](row.get("on"))
        if fg and bg:
            r = contrast(fg, bg)
            role = row.get("role", "text")
            need = 3.0 if role in ("border", "icon", "fill") or row.get("large") else 4.5
            if r < need and not row.get("hint"):
                out.append(("Tương phản (foundations Mục 3.4, WCAG 1.4.3/1.4.11)",
                            f"{r:.2f}:1 < {need}:1 ({role} trên {bg})"))
            row["_contrast"] = round(r, 2)
    if prop in ("height", "min-height") and row.get("control"):
        for mode in modes:
            allowed = {plat_value(tk, mode, f"control/height/{s}") for s in ("sm", "md", "lg")}
            try:
                v = float(row["value"])
            except (TypeError, ValueError):
                continue
            if v not in allowed:
                out.append(("Cao control (DEC-173)",
                            f"{mode}: {fmt(v)} không thuộc {sorted(int(a) for a in allowed if a)}"))
    if prop in ("height", "min-height", "size", "hit-area") and row.get("interactive"):
        for mode in modes:
            need = plat_value(tk, mode, "touch/min") or (44 if mode == "Mobile" else 24)
            try:
                v = float(row.get("hitArea") or row["value"])
            except (TypeError, ValueError):
                continue
            if v < need:
                out.append(("Vùng chạm (foundations Mục 9, DEC-138)",
                            f"{mode}: {fmt(v)} < {fmt(need)} — thêm vùng bấm vô hình (khai hitArea)"))
    if prop == "focus-width" and float(row.get("value", 0)) != 2:
        out.append(("Vòng focus 2px (foundations Mục 9)", f"{row['value']}px"))
    if prop == "focus-offset" and float(row.get("value", 0)) != 2:
        out.append(("Khe focus 2px (DEC-241)", f"{row['value']}px"))
    if prop == "shadow" and row.get("control") and row.get("value") not in (None, "", "none"):
        out.append(("Nút phẳng, không bóng (DEC-260)", str(row.get("value"))))
    return out


def check_row(row, tk):
    prop = row.get("prop")
    if prop in COLOR_PROPS:
        cat, tokens, suggest, note = check_color(row, tk)
    elif prop == "shadow":
        v = row.get("value")
        if v in (None, "", "none"):
            cat, tokens, suggest, note = "ok", ["không bóng"], None, ""
        elif v in tk["effects"]:
            cat, tokens, suggest, note = "ok", [v], None, ""
        else:
            cat, tokens, suggest, note = "new", [], None, f"bóng tự do `{v}` — chọn elev/1…3 hoặc thêm effect style"
    else:
        cat, tokens, suggest, note = check_num(row, tk)
    broken = rules(row, tk)
    out = {
        "id": row.get("id") or ".".join(str(x) for x in (row.get("part"), prop, row.get("platform") or "Web",
                                                            row.get("size") or "") if x).lower().replace(" ", "-"),
        "part": row.get("part"), "prop": prop, "platform": row.get("platform") or "Web",
        "size": row.get("size") or "", "state": row.get("state") or "", "value": row.get("value"),
        "cat": "conflict" if broken else cat, "tokens": tokens, "suggest": suggest,
        "rules": [f"{r}: {d}" for r, d in broken], "note": note,
    }
    if "_contrast" in row:
        out["contrast"] = row["_contrast"]
    return out


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
    tk = load_tokens()
    rows = [check_row(dict(v), tk) for v in values]
    seen = {}
    for r in rows:  # id trùng → thêm hậu tố
        if r["id"] in seen:
            seen[r["id"]] += 1
            r["id"] = f"{r['id']}-{seen[r['id']]}"
        else:
            seen[r["id"]] = 1

    answers_path = page_path.parent / "answers.json"
    answers = json.loads(answers_path.read_text()) if answers_path.exists() else {}
    for r in rows:
        a = answers.get(f"foundation-{r['id']}") or {}
        r["decided"] = a.get("choice") is not None
    counts = {k: sum(1 for r in rows if r["cat"] == k) for k in CAT_LABEL}
    open_rows = [r for r in rows if r["cat"] in ("conflict", "new") and not r["decided"]]

    print(f"Đối chiếu foundation — {page.get('component', page_path.parent.name)} · {len(rows)} giá trị")
    print(" · ".join(f"{CAT_LABEL[k]} {counts[k]}" for k in CAT_LABEL))
    for k in ("conflict", "new", "near"):
        sub = [r for r in rows if r["cat"] == k]
        if not sub:
            continue
        print(f"\n{CAT_LABEL[k]}")
        for r in sub:
            where = " · ".join(x for x in (r["part"], r["prop"], r["platform"], r["size"], r["state"]) if x)
            extra = "; ".join(r["rules"]) or (f"đề xuất {r['suggest']}" if r["suggest"] else "") or r["note"]
            done = " [đã quyết]" if r["decided"] else ""
            print(f"  - {r['id']}: {where} = {r['value']} — {extra}{done}")
    print(f"\nCòn chưa quyết (⛔ + ＋): {len(open_rows)}")

    if "--write" in sys.argv:
        out = page_path.parent / "check.json"
        out.write_text(json.dumps({"tokens_version": json.loads(TOKENS.read_text()).get("version"),
                                   "counts": counts, "rows": rows}, ensure_ascii=False, indent=1))
        print(f"Đã ghi {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    sys.exit(1 if open_rows else 0)


if __name__ == "__main__":
    main()
