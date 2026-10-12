"""Dựng trang bản chốt design/_lab/vehicles-final.html từ ảnh theo quy chuẩn (-q / -s / -top) + sizes.json.
--share: nhúng ảnh (WebP) để gửi 1 file → vehicles-final-share.html.
"""
import base64, io, json, pathlib, sys
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
SIZES = json.loads((HERE / "sizes.json").read_text(encoding="utf-8"))
LAB = HERE.parent
A = LAB / "assets" / "vehicles" / "b-ai"
SHARE = "--share" in sys.argv

# [mã PT, mã loại, tên SRS, key ảnh, kiểu sơ đồ lốp (số | None)]
NAMES = [
 ["00", "", "Phương tiện chưa xác định", None, None],
 ["01", "01", "Mooc 20ft", "n01", 8], ["02", "01", "Mooc 40ft 2 giàn", "t01", 8], ["03", "01", "Mooc 40ft 3 giàn", "n03", 9], ["04", "01", "Mooc 45ft", "n04", 9],
 ["05", "02", "Đầu kéo Maz", "n05", 2], ["06", "02", "Đầu kéo Maxxforce", "n06", 1], ["07", "02", "Đầu kéo Hino 700", "t02", 1],
 ["08", "02", "Đầu kéo Cascadia", "n08", 1], ["09", "02", "Đầu kéo Chenglong H7 385PS", "n09", 1],
 ["10", "03", "Xe tải AC990", "n10", 5], ["11", "03", "Xe tải AC820", "g-truck-l", 3], ["12", "03", "Xe tải TMT", "n12", 3],
 ["13", "03", "Xe tải Ollin 700A", "n29", 3], ["14", "03", "Xe tải Isuzu NQR75L", "t03", 3], ["15", "03", "Xe tải Ollin 450", "n29", 3],
 ["16", "03", "Xe Isuzu NQR66P", "t03", 3], ["17", "03", "Xe Hyundai HD72", "n17", 3], ["18", "03", "Xe Olin 250", "n29", 3],
 ["19", "03", "Xe Kia Frontier K165", "g-kia", 3], ["20", "03", "Xe Isuzu QKR 55H", "g-truck-s", 3], ["21", "03", "Xe Kia Frontier 140", "g-kia", 3],
 ["22", "03", "Xe Kia K2700", "g-kia", 3], ["23", "03", "Xe Isuzu NLR55", "g-truck-s", 3], ["24", "03", "Xe tải Kia K3000", "g-kia", 3],
 ["25", "03", "Xe tải Dongfeng B180", "n25", 3], ["26", "03", "Xe tải Auman C240", "n26", 4], ["27", "03", "Xe tải Chenglong M3 - 2024", "n27", 3],
 ["28", "03", "Xe tải Chenglong H5 - 2024", "n28", 6], ["29", "03", "Xe tải Ollin 700", "n29", 3], ["30", "03", "Xe tải Isuzu QKR 210", "g-truck-s", 3],
 ["31", "04", "Xe nâng Toyota 2.5T", "t04", 10], ["32", "05", "Xe nâng Komatsu FB15RL-15 1.5T", "t05", 11],
 ["33", "06", "Container thường", "t06", None], ["34", "07", "Container lạnh", "t07", None],
 ["35", "08", "Máy phát điện 25 KVA", "t08", None], ["36", "08", "Máy phát điện 44 KVA (HP)", "t08", None], ["37", "08", "Máy phát điện 45 KVA (BN)", "t08", None],
 ["38", "09", "Trạm bơm dầu", "t09", None]]
TYRE = {1: "Đầu kéo 2 cầu sau (1 dí 2 cầu tải)", 2: "Đầu kéo 1 cầu sau (1 dí 1 cầu tải)", 3: "Xe tải hai trục (1 dí 1 cầu tải)",
        4: "Xe tải ba trục (1 dí 2 cầu tải)", 5: "Xe tải ba trục (2 dí 1 cầu tải)", 6: "Xe tải bốn trục (2 dí 2 cầu tải)",
        8: "Sơ mi-Rơ mooc 2 giàn", 9: "Sơ mi-Rơ mooc 3 giàn", 10: "Xe nâng diesel", 11: "Xe nâng điện"}

keys = sorted(p.stem for p in A.glob("*.png") if p.stem.endswith(("-q", "-s", "-top")))
info, src = {}, {}
for k in keys:
    im = Image.open(A / f"{k}.png"); info[k] = round(im.height / im.width, 4)
    if SHARE:
        im = im.convert("RGBA"); im.thumbnail((900, 900), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, "WEBP", quality=80, method=6)
        src[k] = "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
    else:
        src[k] = f"assets/vehicles/b-ai/{k}.png"
data = {"names": NAMES, "tyre": TYRE, "sizes": SIZES, "aspect": info, "src": src}
tpl = (HERE / "final-template.html").read_text(encoding="utf-8")
out = LAB / ("vehicles-final-share.html" if SHARE else "vehicles-final.html")
out.write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
miss = sorted({n[3] + s for n in NAMES if n[3] for s in ("-q", "-s") if n[3] + s not in info})
print(f"{out.name}: {len(keys)} ảnh, {out.stat().st_size // 1024} KB" + (f" · thiếu: {miss}" if miss else ""))
