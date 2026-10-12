"""Tạo bản HTML tự chứa để gửi người khác: nhúng ảnh xe (nén WebP) vào file.
Chạy: python3 design/_lab/vehicles-src/build_share.py design/_lab/tyre-mapping.html
Ra:   cùng thư mục, thêm hậu tố -share.html (vd tyre-mapping-share.html)."""
import base64, io, json, pathlib, re, sys
from PIL import Image

src = pathlib.Path(sys.argv[1]).resolve()
lab = src.parent
html = src.read_text(encoding="utf-8")
keys = sorted(set(re.findall(r'"([a-z0-9-]+)",(?:\d+|"none"|"\?"),"(?:ok|ask|none)"', html)) - {"—"})
imgs = {}
for k in keys:
    f = lab / "assets" / "vehicles" / "b-ai" / f"{k}-q.png"
    if not f.exists():
        print("thiếu ảnh:", k); continue
    im = Image.open(f).convert("RGBA"); im.thumbnail((360, 200), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "WEBP", quality=82, method=6)
    imgs[k] = "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
inject = "<script>window.IMGS=" + json.dumps(imgs) + ";</script>\n"
out = html.replace("<script>\nconst L=", inject + "<script>\nconst L=", 1)
assert out != html, "không tìm thấy chỗ chèn ảnh"
dst = src.with_name(src.stem + "-share.html")
dst.write_text(out, encoding="utf-8")
print(f"{dst.name}: {len(imgs)} ảnh nhúng, {dst.stat().st_size//1024} KB")
