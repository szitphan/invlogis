#!/usr/bin/env python3
"""DS v2 — sinh design-system/tokens.css từ design-system/tokens.json (nguồn duy nhất).

  python3 _scripts/ds-v2-tokens.py           # ghi tokens.css + in bảng tương phản
  python3 _scripts/ds-v2-tokens.py --check   # không ghi; exit 1 nếu tokens.css lệch json hoặc cặp chữ/nền dưới ngưỡng

Tên CSS = '--' + tên token thay '/' bằng '-' (neutral/100 → --neutral-100, color/bg/primary → --color-bg-primary).
Màu theo khách: collection Brand, mỗi chế độ một dải; đặt data-brand="<slug>" trên thẻ gốc (mặc định than-chi).
Bóng: màu mỗi lớp đi qua biến Semantic `color/shadow/*`; `shadow/*`, `shadow/*-border` khai trong khối Semantic Light và Dark để khung
data-theme lồng trong trang khác chế độ tính lại đúng (DEC-327, BL-348); `blur` trong json sinh --backdrop-blur-*.
Vòng focus là outline, khe trong suốt: không có token khe (DEC-327).
Màu thương hiệu: collection Brand Invlogis sinh --invlogis-*, --innvie-* cho logo, trang giới thiệu (DEC-326); không dùng trong
component sản phẩm (DEC-261, ds-token-usage.py cờ brandleak). --check so thêm với design/brand/invlogis/brand-tokens.css.
Quyết định: _workspace/decisions.md DEC-115, DEC-116, DEC-129…139, DEC-167, DEC-168, DEC-241, DEC-333.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "design-system/tokens.json"
OUT = ROOT / "design-system/tokens.css"
BRAND_CSS = ROOT / "design/brand/invlogis/brand-tokens.css"
WEIGHT = {"Regular": 400, "Medium": 500, "Semi Bold": 600, "Bold": 700}

# Cặp chữ/nền phải đạt ngưỡng (WCAG 2.2: chữ thường 4.5, chữ gợi ý/icon tắt chỉ báo cáo).
PAIRS = [
    ("color/text/primary", "color/bg/primary", 4.5),
    ("color/text/tertiary", "color/bg/primary", 4.5),
    ("color/text/tertiary", "color/bg/secondary", 4.5),
    ("color/text/tertiary_strong", "color/bg/selected", 4.5),
    ("color/text/tertiary_strong", "color/bg/primary_hover", 4.5),
    ("color/text/inverse", "color/action/primary", 4.5),
    ("color/text/inverse", "color/text/error/primary", 4.5),
    ("color/text/error/primary", "color/bg/error/primary", 4.5),
    ("color/text/primary", "color/action/secondary", 4.5),
    ("color/text/disabled", "color/bg/primary", 0),
    ("color/text/placeholder", "color/bg/primary", 4.5),
    ("color/text/secondary", "color/bg/primary", 4.5),
    ("color/text/tertiary_strong", "color/bg/pressed", 4.5),
] + [(f"color/text/{k}/primary", f"color/bg/{k}/primary", 4.5) for k in ("success", "warning", "error", "info")] \
  + [("color/text/white", f"color/bg/{k}/solid", 4.5) for k in ("success", "warning", "error", "info")] \
  + [(f"color/utility/{c}/{fg}", f"color/utility/{c}/{bg}", 4.5)  # cặp chữ/nền chip (bậc riêng: neutral 600/100, orange 800/100; DEC-311, DEC-320)
     for c, fg, bg in (("neutral", 600, 100), ("blue", 700, 50), ("teal", 700, 50), ("purple", 700, 50), ("yellow", 700, 50),
                       ("green", 700, 50), ("red", 700, 50), ("orange", 800, 100))] \
  + [("color/fg/white", f"color/file-type/{k}", 4.5) for k in ("pdf", "doc", "xls", "csv", "img", "zip", "vid")]  # nhãn File type icon (DEC-335 ms02)


def css_name(token: str) -> str:
    return "--" + token.replace("/", "-")


def px(v) -> str:
    return "0" if v == 0 else f"{v}px"


def load():
    return json.loads(SRC.read_text(encoding="utf-8"))


def resolve_color(doc, token, mode="Light"):
    prim = doc["collections"]["Primitives"]["color"]
    sem = doc["collections"]["Semantic"]["color"]
    if token in sem:
        return resolve_color(doc, sem[token][mode], mode)
    return prim[token]


def lum(hexv):
    h = hexv.lstrip("#")[:6]
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def contrast(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def ref_or_value(v, kind):
    """Giá trị Platform/Semantic: tên token → var(), số → px, chuỗi khác giữ nguyên."""
    if isinstance(v, (int, float)):
        return px(v) if kind == "px" else str(v)
    if v.endswith("%"):
        return v
    return f"var({css_name(v)})"


def shadow_decls(doc, mode):
    """--shadow-*, --shadow-*-border của một chế độ. border là tên token, hoặc {Light, Dark} khi khác nhau (None = trong suốt)."""
    out = ["  --shadow-none: none;"]
    for k, v in doc["effectStyles"].items():
        layers = ", ".join(f"{s['x']}px {s['y']}px {s['blur']}px {s['spread']}px var({css_name(s['var'])})" for s in v["shadows"])
        out.append(f"  {css_name(k)}: {layers};")
        border = v.get("border")
        if isinstance(border, dict):
            out.append(f"  {css_name(k)}-border: " + (f"var({css_name(border[mode])});" if border[mode] else "transparent;"))
        elif border:
            out.append(f"  {css_name(k)}-border: var({css_name(border)});")
    return out


def build(doc) -> str:
    c = doc["collections"]
    L = ["/* DS v2 tokens — FILE SINH RA từ design-system/tokens.json bằng _scripts/ds-v2-tokens.py. KHÔNG sửa tay. */",
         f"/* version {doc['version']} · {doc['updated']} */", "", ":root {", "  /* Fonts (DEC-121) */"]
    for k, v in doc["fonts"].items():
        L.append(f"  --font-{k}: {v};")
    L.append("  /* Primitives — component không dùng trực tiếp (DEC-115) */")
    for k, v in c["Primitives"]["color"].items():
        L.append(f"  {css_name(k)}: {v};")
    for k, v in c["Primitives"]["number"].items():
        L.append(f"  {css_name(k)}: {px(v)};")
    L.append("}")
    L.append("")
    L.append("/* Semantic — Light (mặc định) */")
    L.append(":root, [data-theme=\"light\"] {")
    for k, v in c["Semantic"]["color"].items():
        L.append(f"  {css_name(k)}: var({css_name(v['Light'])});")
    L += shadow_decls(doc, "Light")
    L.append("}")
    L.append(f"/* Semantic — Dark: {c['Semantic']['darkNote']} */")
    L.append("[data-theme=\"dark\"] {")
    for k, v in c["Semantic"]["color"].items():
        L.append(f"  {css_name(k)}: var({css_name(v['Dark'])});")
    L += shadow_decls(doc, "Dark")
    L.append("}")
    L.append("")
    for mode, sel in (("Web", ":root, [data-platform=\"web\"]"), ("Mobile", c["Platform"]["cssModeSelector"])):
        L.append(f"/* Platform — {mode} (DEC-114, DEC-132…138) */")
        L.append(sel + " {")
        for k, v in c["Platform"]["vars"].items():
            val = v[mode]
            if k == "type/label/style":
                L.append(f"  --type-label-weight: {WEIGHT[val]};")
                continue
            unit = "raw" if "OPACITY" in v.get("scopes", []) or k == "grid/columns" else "px"
            L.append(f"  {css_name(k)}: {ref_or_value(val, unit)};")
        L.append("}")
        L.append("")
    b = c.get("Brand")
    if b:
        for i, mode in enumerate(b["modes"]):
            slug = b["modeSlugs"][mode]
            sel = b["cssModeSelector"].replace("{slug}", slug)
            L.append(f"/* Brand — {mode} ({b['hue'][mode]}) · DEC-167, DEC-168 */")
            L.append((":root, " if i == 0 else "") + sel + " {")
            for k, v in b["color"].items():
                L.append(f"  {css_name(k)}: {v[mode]};")
            L.append("}")
        L.append("")
    bi = c.get("Brand Invlogis")
    if bi:
        L.append("/* Brand Invlogis — logo, trang giới thiệu, tài liệu; KHÔNG dùng trong component sản phẩm (DEC-261, DEC-326) */")
        L.append(":root {")
        for k, v in bi["color"].items():
            L.append(f"  {css_name(k)}: {v['Value']};")
        L.append("}")
        L.append("")
    comp = c.get("Component")
    if comp:
        # Khai lại ở nơi đặt data-theme để token Component tính lại theo Semantic sáng/tối.
        L.append("/* Component — màu trạng thái của component (DEC-174; nút: DEC-176, DEC-197) */")
        L.append(":root, [data-theme=\"light\"], [data-theme=\"dark\"] {")
        for k, v in comp["color"].items():
            L.append(f"  {css_name(k)}: var({css_name(v['Value'])});")
        L.append("}")
        L.append("")
    L.append(":root {")
    L.append("  /* Làm mờ nền (DEC-258) */")
    for k, v in doc.get("blur", {}).items():
        L.append(f"  {css_name(k)}: {px(v['value'])};")
    L.append("  /* Chuyển động (DEC-139) */")
    for k, v in doc["motion"].items():
        L.append(f"  {css_name(k)}: {v};")
    L.append("  /* Breakpoint (DEC-324) chỉ để tra, media query ghi số trực tiếp */")
    for k, v in doc["breakpoints"].items():
        L.append(f"  --bp-{k}: {px(v)};")
    L.append("}")
    L.append("@media (prefers-reduced-motion: reduce) {")
    # DEC-333 (mt13): mọi duration về 0, tự theo tokens.json nên token mới không lọt
    durs = " ".join(f"--{k.replace('/', '-')}: 0ms;" for k in doc["motion"] if k.startswith("duration"))
    L.append(f"  :root {{ {durs} }}")
    L.append("}")
    L.append("")
    L.append("/* Preset chuyển động (DEC-336): chỉ dùng biến thời gian nên giảm chuyển động tự về 0 */")
    decls = lambda d: " ".join(f"{k}: {v};" for k, v in d.items())
    ease = lambda e: e if e == "linear" else f"var({css_name(e)})"
    for name, p in doc.get("motionPresets", {}).items():
        dur = f"var({css_name(p['duration'])})"
        if p.get("multiply"):
            dur = f"calc({dur} * {p['multiply']})"
        if p.get("keyframes"):
            L.append(f"@keyframes inv-{name} {{ " + " ".join(f"{at} {{ {decls(d)} }}" for at, d in p["keyframes"].items()) + " }")
            L.append(f".anim-{name} {{ {decls(p.get('base', {}))} animation: inv-{name} {dur} {ease(p['easing'])} both; }}".replace("{  ", "{ "))
        elif p.get("exitDuration"):
            prop = p["transition"]
            L.append(f".anim-{name} {{ {decls(p.get('closed', {}))} transition: {prop} var({css_name(p['exitDuration'])}) {ease(p['exitEasing'])}; }}")
            L.append(f".anim-{name}[data-open=\"true\"] {{ {decls(p.get('open', {}))} transition: {prop} {dur} {ease(p['easing'])}; }}")
            L.append(f".anim-{name} > * {{ overflow: hidden; min-height: 0; }}")
        else:
            L.append(f".anim-{name} {{ transition: {p['transition']} {dur} {ease(p['easing'])}; }}")
    L.append("")
    L.append("/* Kiểu chữ (DEC-132, DEC-133) — tên lớp = tên text style Figma */")
    for k, v in doc["textStyles"].items():
        role = v["size"].split("/")[1]
        fam = {"Cal Sans": "var(--font-title)", "Inter": "var(--font-body)", "JetBrains Mono": "var(--font-code)"}[v["family"]]
        weight = "var(--type-label-weight)" if v.get("styleVar") else WEIGHT[v["style"]]
        rule = f".{k.replace('/', '-')} {{ font: {weight} var(--type-{role}-size)/var(--type-{role}-line-height) {fam};"
        if v["family"] == "Cal Sans":
            rule += " font-synthesis: none;"
        if v.get("case") == "UPPER":
            rule += " text-transform: uppercase;"
        if v.get("letterSpacingPercent"):
            rule += f" letter-spacing: {v['letterSpacingPercent'] / 100}em;"
        L.append(rule + " }")
    L += ["", "/* Số đều bề rộng: cột số, tiền, giờ, đếm, KPI (DEC-322) */", ".num { font-variant-numeric: tabular-nums; }", "",
          "/* Nội dung dài (DEC-322) */",
          ".prose { font: 400 var(--type-body-size)/var(--type-body-line-height) var(--font-body); color: var(--color-text-tertiary); max-width: var(--width-paragraph-max); }",
          ".prose h1 { font: 400 var(--type-display-size)/var(--type-display-line-height) var(--font-title); font-synthesis: none; color: var(--color-text-primary); }",
          ".prose h2 { font: 400 var(--type-title-1-size)/var(--type-title-1-line-height) var(--font-title); font-synthesis: none; color: var(--color-text-primary); }",
          ".prose h3 { font: 400 var(--type-title-2-size)/var(--type-title-2-line-height) var(--font-title); font-synthesis: none; color: var(--color-text-primary); }",
          ".prose h4 { font: 400 var(--type-title-3-size)/var(--type-title-3-line-height) var(--font-title); font-synthesis: none; color: var(--color-text-primary); }",
          ".prose p { margin: 0; } .prose p + p { margin-top: 1em; }",
          ".prose strong { color: var(--color-text-primary); }",
          ".prose hr { border: 0; border-top: 1px solid var(--color-border-secondary); }",
          ".prose blockquote { margin: 0; font: 500 var(--type-title-2-size)/var(--type-title-2-line-height) var(--font-body); color: var(--color-text-primary); }",
          ".prose code { font: 700 var(--type-body-size)/var(--type-body-line-height) var(--font-code); background: var(--color-bg-secondary); box-shadow: inset 0 0 0 1px var(--color-border-secondary); border-radius: 6px; padding: 0 4px; }"]
    return "\n".join(L) + "\n"


def report(doc):
    rows, bad = [], []
    for fg, bg, need in PAIRS:
        r = contrast(resolve_color(doc, fg), resolve_color(doc, bg))
        ok = r >= need
        rows.append(f"  {r:5.2f}:1  {'OK ' if ok else 'LOW'} (cần {need or 'báo cáo'})  {fg} trên {bg}")
        if not ok:
            bad.append(fg)
    return rows, bad


def brand_report(doc):
    """Mỗi dải: chữ trắng trên 800, bậc 700 trên nền trắng, 800 trên 50 — cần ≥ 4.5."""
    b = doc["collections"].get("Brand")
    rows, bad = [], []
    if not b:
        return rows, bad
    for mode in b["modes"]:
        v = {k.split("/")[-1]: x[mode] for k, x in b["color"].items()}
        r = (contrast("#FFFFFF", v["800"]), contrast(v["700"], "#FFFFFF"), contrast(v["800"], v["50"]))
        low = min(r) < 4.5
        rows.append(f"  {mode:11} trắng/800 {r[0]:5.2f} · 700/trắng {r[1]:5.2f} · 800/50 {r[2]:5.2f}{'  LOW' if low else ''}")
        if low:
            bad.append(mode)
    return rows, bad


def brand_css_diff(doc):
    """Bộ --brand-c-* của brand-tokens.css phải cùng giá trị collection Brand Invlogis; innvie/* không có bản ở đó."""
    if not BRAND_CSS.exists():
        return [f"thiếu {BRAND_CSS.relative_to(ROOT)}"]
    have = {m[0]: m[1].upper() for m in re.findall(r"--brand-c-([\w-]+):\s*(#[0-9A-Fa-f]{6})", BRAND_CSS.read_text(encoding="utf-8"))}
    out = []
    for k, v in doc["collections"]["Brand Invlogis"]["color"].items():
        if k.startswith("invlogis/"):
            n = k.split("/")[1].replace("_", "-")
            if have.get(n) != v["Value"].upper():
                out.append(f"{k} {v['Value']} ≠ --brand-c-{n} {have.get(n)}")
    return out


def main():
    doc = load()
    css = build(doc)
    rows, bad = report(doc)
    print("Tương phản (Light):")
    print("\n".join(rows))
    brows, bbad = brand_report(doc)
    if brows:
        print("Tương phản dải màu khách:")
        print("\n".join(brows))
    bad = bad + bbad
    bdiff = brand_css_diff(doc)
    print("brand-tokens.css:", "LỆCH " + "; ".join(bdiff) if bdiff else "khớp collection Brand Invlogis")
    bad = bad + bdiff
    if "--check" in sys.argv:
        stale = not OUT.exists() or OUT.read_text(encoding="utf-8") != css
        print("tokens.css:", "LỆCH json — chạy lại không có --check" if stale else "khớp json")
        sys.exit(1 if stale or bad else 0)
    OUT.write_text(css, encoding="utf-8")
    print(f"Đã ghi {OUT.relative_to(ROOT)} ({css.count(chr(10))} dòng)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
