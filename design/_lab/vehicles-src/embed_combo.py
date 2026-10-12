"""Nhúng ảnh xe (WebP base64) thẳng vào lab-combo.html để file tự chạy, không cần assets/.
Chạy lại được: thay khối giữa 2 marker IMGS:begin / IMGS:end.
Chạy: python3 design/_lab/vehicles-src/embed_combo.py"""
import base64, io, json, pathlib, re
from PIL import Image

lab = pathlib.Path(__file__).resolve().parent.parent
src = lab / "lab-combo.html"
b_ai = lab / "assets" / "vehicles" / "b-ai"
html = src.read_text(encoding="utf-8")

TR = ["t02", "n05", "n06", "n08", "n09"]
MO = ["n01", "t01", "n03", "n04"]
CT = ["t06", "c40", "c45", "t07"]
names = [f"{k}-s" for k in TR + MO + CT] + [f"{k}-top" for k in TR + MO + CT]

imgs = {}
for n in names:
    f = b_ai / f"{n}.png"
    if not f.exists():
        print("thiếu ảnh:", n); continue
    im = Image.open(f).convert("RGBA")
    im.thumbnail((900, 600) if n.endswith("-s") else (300, 700), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "WEBP", quality=82, method=6)
    imgs[n] = "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()

block = "<!-- IMGS:begin (máy sinh bởi vehicles-src/embed_combo.py) -->\n<script>window.IMGS=" + json.dumps(imgs) + ";</script>\n<!-- IMGS:end -->\n"
if "<!-- IMGS:begin" in html:
    out = re.sub(r"<!-- IMGS:begin.*?<!-- IMGS:end -->\n", lambda m: block, html, flags=re.S)
else:
    out = html.replace("<script>\n/* ===================== Dữ liệu", block + "<script>\n/* ===================== Dữ liệu", 1)
assert out != html or "<!-- IMGS:begin" in html, "không tìm thấy chỗ chèn ảnh"
src.write_text(out, encoding="utf-8")
print(f"{src.name}: {len(imgs)}/{len(names)} ảnh nhúng, {src.stat().st_size // 1024} KB")
