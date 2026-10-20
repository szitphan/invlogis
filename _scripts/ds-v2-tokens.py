#!/usr/bin/env python3
"""DS v2 — sinh design/v2/tokens.css từ design/v2/tokens.json (nguồn duy nhất).

  python3 _scripts/ds-v2-tokens.py           # ghi tokens.css + in bảng tương phản
  python3 _scripts/ds-v2-tokens.py --check   # không ghi; exit 1 nếu tokens.css lệch json hoặc cặp chữ/nền dưới ngưỡng

Tên CSS = '--' + tên token thay '/' bằng '-' (neutral/100 → --neutral-100, color/bg/canvas → --color-bg-canvas).
Màu theo khách: collection Brand, mỗi chế độ một dải; đặt data-brand="<slug>" trên thẻ gốc (mặc định than-chi).
Nền đặt: collection Context (Surface | Canvas) chứa màu đổi theo nền của khung chứa (khe vòng focus `focus/gap`); đặt
data-context="canvas" trên khung nền xám, mặc định surface.
Quyết định: _workspace/decisions.md DEC-115, DEC-116, DEC-129…139, DEC-167, DEC-168, DEC-241.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "design/v2/tokens.json"
OUT = ROOT / "design/v2/tokens.css"
WEIGHT = {"Regular": 400, "Medium": 500, "Semi Bold": 600, "Bold": 700}

# Cặp chữ/nền phải đạt ngưỡng (WCAG 2.2: chữ thường 4.5, chữ gợi ý/icon tắt chỉ báo cáo).
PAIRS = [
    ("color/text/primary", "color/bg/surface", 4.5),
    ("color/text/primary", "color/bg/canvas", 4.5),
    ("color/text/secondary", "color/bg/surface", 4.5),
    ("color/text/secondary", "color/bg/canvas", 4.5),
    ("color/text/secondary", "color/bg/muted", 4.5),
    ("color/text/inverse", "color/action/primary", 4.5),
    ("color/text/inverse", "color/action/danger", 4.5),
    ("color/action/danger", "color/action/danger-subtle", 4.5),
    ("color/text/primary", "color/action/secondary", 4.5),
    ("color/text/tertiary", "color/bg/surface", 0),
] + [(f"color/status/{k}-fg", f"color/status/{k}-bg", 4.5) for k in ("success", "warning", "danger", "info")] \
  + [(f"color/chip/{c}/fg", f"color/chip/{c}/bg", 4.5)
     for c in ("gray", "blue", "teal", "purple", "yellow", "green", "red", "orange")]


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
    return f"var({css_name(v)})"


def build(doc) -> str:
    c = doc["collections"]
    L = ["/* DS v2 tokens — FILE SINH RA từ design/v2/tokens.json bằng _scripts/ds-v2-tokens.py. KHÔNG sửa tay. */",
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
    L.append("}")
    L.append(f"/* Semantic — Dark: {c['Semantic']['darkNote']} */")
    L.append("[data-theme=\"dark\"] {")
    for k, v in c["Semantic"]["color"].items():
        L.append(f"  {css_name(k)}: var({css_name(v['Dark'])});")
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
            L.append(f"  {css_name(k)}: {ref_or_value(val, 'px')};")
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
    comp = c.get("Component")
    if comp:
        # Khai lại ở nơi đặt data-theme để token Component tính lại theo Semantic sáng/tối.
        L.append("/* Component — màu trạng thái của component (DEC-174; nút: DEC-176, DEC-197) */")
        L.append(":root, [data-theme=\"light\"], [data-theme=\"dark\"] {")
        for k, v in comp["color"].items():
            L.append(f"  {css_name(k)}: var({css_name(v['Value'])});")
        L.append("}")
        L.append("")
    ctx = c.get("Context")
    if ctx:
        # Màu theo nền đặt (DEC-241). Mặc định = chế độ đầu (Surface) khai ở mọi nơi đặt data-theme như Component, để var() tính lại
        # theo Semantic sáng/tối; chế độ còn lại chỉ ghi đè trong khung mang data-context tương ứng.
        L.append("/* Context — màu theo nền đặt: khe vòng focus (DEC-241); data-context=\"canvas\" trên khung nền xám */")
        for i, mode in enumerate(ctx["modes"]):
            slug = ctx["modeSlugs"][mode]
            sel = ctx["cssModeSelector"].replace("{slug}", slug)
            L.append((":root, [data-theme=\"light\"], [data-theme=\"dark\"], " if i == 0 else "") + sel + " {")
            for k, v in ctx["color"].items():
                L.append(f"  {css_name(k)}: var({css_name(v[mode])});")
            L.append("}")
        L.append("")
    L.append(":root {")
    L.append("  /* Lớp nổi (DEC-137) */")
    L.append("  --elev-0: none;")
    for k, v in doc["effectStyles"].items():
        shadows = ", ".join(
            f"{s['x']}px {s['y']}px {s['blur']}px {s['spread']}px rgba(16, 24, 40, {s['alpha']})" for s in v["shadows"])
        L.append(f"  {css_name(k)}: {shadows};")
        if v.get("border"):
            L.append(f"  {css_name(k)}-border: var({css_name(v['border'])});")
    L.append("  /* Chuyển động, focus (DEC-139) */")
    for k, v in doc["motion"].items():
        L.append(f"  {css_name(k)}: {v};")
    L.append("  --focus-color: var(--color-border-focus);")
    L.append("  /* Lưới (DEC-136); breakpoint chỉ để tra, media query ghi số trực tiếp */")
    L.append(f"  --grid-columns: {doc['grid']['web']['columns']};")
    L.append(f"  --grid-gutter: {px(doc['grid']['web']['gutter'])};")
    for k, v in doc["breakpoints"].items():
        L.append(f"  --bp-{k}: {px(v)};")
    L.append("}")
    L.append("@media (prefers-reduced-motion: reduce) {")
    L.append("  :root { --duration-fast: 0ms; --duration-medium: 0ms; --duration-slow: 0ms; }")
    L.append("}")
    L.append("")
    L.append("/* Kiểu chữ (DEC-132, DEC-133) — tên lớp = tên text style Figma */")
    for k, v in doc["textStyles"].items():
        role = v["size"].split("/")[1]
        fam = {"Cal Sans": "var(--font-title)", "Inter": "var(--font-body)", "JetBrains Mono": "var(--font-code)"}[v["family"]]
        weight = "var(--type-label-weight)" if v.get("styleVar") else WEIGHT[v["style"]]
        rule = f".{k.replace('/', '-')} {{ font: {weight} var(--type-{role}-size)/var(--type-{role}-line-height) {fam};"
        if v.get("case") == "UPPER":
            rule += f" text-transform: uppercase; letter-spacing: {v['letterSpacingPercent'] / 100}em;"
        L.append(rule + " }")
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
    if "--check" in sys.argv:
        stale = not OUT.exists() or OUT.read_text(encoding="utf-8") != css
        print("tokens.css:", "LỆCH json — chạy lại không có --check" if stale else "khớp json")
        sys.exit(1 if stale or bad else 0)
    OUT.write_text(css, encoding="utf-8")
    print(f"Đã ghi {OUT.relative_to(ROOT)} ({css.count(chr(10))} dòng)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
