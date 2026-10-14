"""Dựng app-icon-options.html → ../app-icon-options.png (1600×1000)"""
import pathlib, subprocess
from PIL import Image, ImageDraw
H = pathlib.Path(__file__).parent; D = H / "_icons"; D.mkdir(exist_ok=True)
RENDER = H.parents[1] / "_tools/render.py"
def mask(im, kind, size):
    S = 4096; m = Image.new("L", (S, S), 0); d = ImageDraw.Draw(m)
    (d.rounded_rectangle((0, 0, S-1, S-1), radius=int(S*.2237), fill=255) if kind == "ios" else d.ellipse((0, 0, S-1, S-1), fill=255))
    o = im.convert("RGBA"); o.putalpha(m.resize((1024, 1024), Image.LANCZOS)); return o.resize((size, size), Image.LANCZOS)
for k in "abc":
    subprocess.run(["python3", str(RENDER), str(H/f"icon-{k}.svg"), str(D/f"full-{k}.png"), "--size", "1024x1024"], check=True, capture_output=True)
    im = Image.open(D/f"full-{k}.png")
    for kind in ("ios", "and"):
        for sz in (180, 48): mask(im, kind, sz).save(D/f"{kind}-{k}-{sz}.png")
f = Image.open(H.parent/"favicon-32.png").convert("RGBA")
for sz, fs in ((32, 18), (64, 36)):  # favicon trong vòng tròn trắng kiểu kết quả tìm kiếm
    c = Image.new("RGBA", (sz, sz), (0, 0, 0, 0)); ImageDraw.Draw(c).ellipse((0, 0, sz-1, sz-1), fill=(255,)*4, outline=(218, 220, 224, 255))
    c.alpha_composite(f.resize((fs, fs), Image.LANCZOS), ((sz-fs)//2, (sz-fs)//2)); c.save(D/f"fav-circle-{sz}.png")
O = [("a", "A · Giấy", "i lụa màu trên nền giấy ấm, vệt khói lụa chéo.",
      "Trượt: trong mặt nạ tròn Android là chữ i xanh giữa vòng tròn trắng, trùng đúng hình ⓘ."),
     ("b", "B · Lụa vắt ra ngoài", "i lớn lệch phải; thân thành dải lụa sáng vắt cong ra khỏi khung, nền lụa cobalt.",
      "Đề xuất. Hình bị cắt ở mép, không có viền chữ i nhỏ giữa ô nên không đọc thành ⓘ; thấy ngay chất lụa; 48px vẫn ra chữ i."),
     ("c", "C · Nền lụa", "i mực-cobalt trên nền gradient lụa periwinkle, tím, hồng.",
      "Đỡ hơn A nhờ nền nhiều sắc, nhưng vẫn là chữ i nhỏ đứng giữa vòng tròn → còn nguy cơ ⓘ; nền nhạt chìm trên hình nền sáng.")]
cards = ""
for k, t, d, v in O:
    rec = k == "b"
    cards += f'''<div class="card{' rec' if rec else ''}"><div class="hd"><span class="t">{t}</span>{'<span class="badge">Đề xuất</span>' if rec else ''}</div>
<div class="pair"><div><img src="_icons/ios-{k}-180.png" width="180"><div class="cap">iOS 180</div></div><div><img src="_icons/and-{k}-180.png" width="180"><div class="cap">Android tròn 180</div></div></div>
<div class="walls"><div class="wall l"><img src="_icons/ios-{k}-48.png" width="48"><img src="_icons/and-{k}-48.png" width="48"><span>48 · nền sáng</span></div>
<div class="wall d"><img src="_icons/ios-{k}-48.png" width="48"><img src="_icons/and-{k}-48.png" width="48"><span>48 · nền tối</span></div></div>
<p class="d">{d}</p><p class="v">{v}</p></div>'''
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:BVP;src:url(BeVietnamPro-400.ttf)}}@font-face{{font-family:BVP;font-weight:500;src:url(BeVietnamPro-500.ttf)}}
@font-face{{font-family:Lex;src:url(LexendVF.ttf);font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}body{{width:1600px;height:1000px;background:#FAF8F4;font-family:BVP;color:#0E1442;padding:34px 56px}}
.eb{{font:400 14px Lex;letter-spacing:.14em;text-transform:uppercase;color:#2F43DB}}h1{{font:300 40px/1.15 Lex;margin:8px 0 4px}}.sub{{font-size:16px;color:#4A5380;margin-bottom:20px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.card{{background:#fff;border:1px solid #E1E4F0;border-radius:22px;padding:20px 24px;height:600px}}.card.rec{{border:1.5px solid #2F43DB;box-shadow:0 0 0 5px #E6EAF8}}
.hd{{display:flex;align-items:center}}.t{{font:400 21px Lex}}.badge{{margin-left:auto;font:500 13px BVP;color:#fff;background:#2F43DB;border-radius:99px;padding:5px 12px}}
.pair{{display:flex;gap:22px;justify-content:center;margin:18px 0 10px}}.cap{{font-size:12px;color:#8B93B8;text-align:center;margin-top:4px}}
.walls{{display:flex;gap:12px}}.wall{{flex:1;border-radius:14px;padding:14px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}}.wall span{{font-size:12px;width:100%}}
.wall.l{{background:linear-gradient(135deg,#F3EFE6,#DCE3F5)}}.wall.l span{{color:#4A5380}}.wall.d{{background:linear-gradient(135deg,#1d1f2b,#0B1033)}}.wall.d span{{color:#C4CDFF}}
.d{{font-size:15px;line-height:1.5;margin:16px 0 8px}}.v{{font-size:15px;line-height:1.5;color:#4A5380}}.rec .v{{color:#2F43DB;font-weight:500}}
.fav{{margin-top:18px;display:flex;align-items:center;gap:18px;font-size:14px;color:#4A5380}}.fav img{{display:block}}
</style></head><body><div class="eb">Invlogis · icon ứng dụng · sửa theo R3 (mức Cao 1)</div>
<h1>Ba phương án icon tránh bị đọc thành ⓘ</h1>
<div class="sub">Mỗi phương án thử bo góc iOS và mặt nạ tròn Android, ở cỡ 180 và 48, trên hình nền sáng lẫn tối.</div>
<div class="grid">{cards}</div>
<div class="fav"><img src="_icons/fav-circle-64.png" width="64"><img src="_icons/fav-circle-32.png" width="32">
<span><b style="font-weight:500;color:#0E1442">Favicon:</b> khi bị đặt vào vòng tròn trắng (kết quả tìm kiếm Google) thì vẫn là chữ i xanh trong vòng tròn, có nguy cơ thấp giống ⓘ. Được giữ lại vì favicon thường không có viền và chấm cắt 14° khác chấm tròn của ⓘ. Theo dõi khi lên thật.</span></div>
</body></html>'''
(H / "app-icon-options.html").write_text(html)
