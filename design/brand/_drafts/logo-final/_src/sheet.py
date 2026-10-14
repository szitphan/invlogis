"""Dựng logo-sheet.html (1600×2000) → render ra ../logo-sheet.png"""
import pathlib
H = pathlib.Path(__file__).parent
def img(f, h=None, w=None, cls=""):
    st = (f"height:{h}px;" if h else "") + (f"width:{w}px;" if w else "")
    return f'<img class="{cls}" src="../{f}" style="{st}">'
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:BVP;src:url(BeVietnamPro-400.ttf)}}@font-face{{font-family:BVP;font-weight:500;src:url(BeVietnamPro-500.ttf)}}
@font-face{{font-family:Lex;src:url(LexendVF.ttf);font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}body{{width:1600px;height:2000px;background:#FAF8F4;font-family:BVP;color:#0E1442;padding:44px 56px}}
.eb{{font:400 14px Lex;letter-spacing:.14em;text-transform:uppercase;color:#2F43DB}}h1{{font:300 40px/1.15 Lex;margin:8px 0 4px}}
.sub{{font-size:16px;color:#4A5380}}h2{{font:400 13px Lex;letter-spacing:.14em;text-transform:uppercase;color:#4A5380;margin:26px 0 12px}}
.g{{display:grid;gap:16px}}.c{{border:1px solid #E1E4F0;border-radius:20px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;padding:18px}}
.c .l{{position:absolute;left:16px;bottom:10px;font-size:12px;color:#8B93B8}}.dark{{background:#0B1033;border-color:#0B1033}}.dark .l{{color:#8B93B8}}
.cob{{background:#2F43DB;border-color:#2F43DB}}.cob .l{{color:#C4CDFF}}.smoke{{background:#E6EAF8;border-color:#E6EAF8}}
.row{{display:flex;align-items:flex-end;gap:22px}}.cap{{font-size:12px;color:#8B93B8;text-align:center;margin-top:6px}}
.px img{{image-rendering:pixelated}}
.safe{{position:relative;padding:0}}.safe .box{{position:absolute;border:1px dashed #2F43DB}}
</style></head><body>
<div class="eb">Invlogis × innvie · logo hoàn thiện · hướng A · Lụa (DEC-072)</div>
<h1>Bộ logo invlogis</h1>
<div class="sub">Lexend 340, chữ thường; chữ v chuyển màu mực → cobalt (phương án 1, DEC-073); chữ i đầu là dải lụa: thân cắt 14°, chấm là nếp gấp mặt sau.</div>

<h2>01 · Logo chính</h2>
<div class="g" style="grid-template-columns:1.15fr 1fr;height:260px">
 <div class="c">{img("invlogis-primary.svg", w=560)}<span class="l">invlogis-primary.svg · nền sáng</span></div>
 <div class="c dark">{img("invlogis-reverse.svg", w=480)}<span class="l">invlogis-reverse.svg · nền tối</span></div>
</div>

<h2>02 · Đơn sắc, ký hiệu, lockup</h2>
<div class="g" style="grid-template-columns:repeat(4,1fr);height:190px">
 <div class="c">{img("invlogis-mono-black.svg", w=280)}<span class="l">mono-black</span></div>
 <div class="c">{img("invlogis-symbol.svg", h=120)}<span class="l">symbol (có thêm -mono, -reverse)</span></div>
 <div class="c cob">{img("invlogis-mono-white.svg", w=280)}<span class="l">mono-white</span></div>
 <div class="c dark">{img("invlogis-symbol-reverse.svg", h=120)}<span class="l">symbol-reverse</span></div>
</div>
<div class="g" style="grid-template-columns:1fr 1fr 1fr;height:290px;margin-top:16px">
 <div class="c">{img("invlogis-by-innvie.svg", w=330)}<span class="l">invlogis-by-innvie</span></div>
 <div class="c">{img("invlogis-stacked.svg", h=210)}<span class="l">invlogis-stacked</span></div>
 <div class="c">{img("invlogis-tagline.svg", w=300)}<div style="height:18px"></div>{img("invlogis-tagline-en.svg", w=230)}<span class="l">tagline (Việt · Anh)</span></div>
</div>
<div class="g" style="grid-template-columns:1fr 1fr 1fr;height:150px;margin-top:16px">
 <div class="c">{img("innvie-logo.svg", w=230)}<span class="l">innvie-logo</span></div>
 <div class="c">{img("innvie-logo-mono.svg", w=230)}<span class="l">innvie-logo-mono</span></div>
 <div class="c dark">{img("invlogis-by-innvie-reverse.svg", w=300)}<span class="l">by-innvie trên nền tối</span></div>
</div>

<h2>03 · Thử cỡ nhỏ (kích thước thật) và phóng to điểm ảnh</h2>
<div class="g" style="grid-template-columns:1.25fr 1fr;height:250px">
 <div class="c" style="align-items:flex-start;padding-left:36px"><div class="row" style="gap:36px">
   <div>{img("invlogis-primary.svg", h=32)}<div class="cap">32px</div></div>
   <div>{img("invlogis-primary.svg", h=24)}<div class="cap">24px</div></div>
   <div>{img("invlogis-primary.svg", h=16)}<div class="cap">16px</div></div>
   <div>{img("invlogis-mono-black.svg", h=24)}<div class="cap">đơn sắc 24</div></div>
   <div>{img("invlogis-mono-black.svg", h=16)}<div class="cap">đơn sắc 16</div></div></div>
   <div class="row" style="gap:36px;margin-top:26px">
   <div>{img("favicon-16.png", h=16)}<div class="cap">16</div></div>
   <div>{img("favicon.svg", h=24)}<div class="cap">24</div></div>
   <div>{img("favicon-32.png", h=32)}<div class="cap">32</div></div>
   <div>{img("favicon-48.png", h=48)}<div class="cap">48</div></div>
   <div style="background:#202124;padding:8px;border-radius:8px">{img("favicon-16.png", h=16)} {img("favicon-32.png", h=32)}</div><div class="cap" style="align-self:center">tab tối (PNG)</div></div>
   <span class="l">trái → phải: logo chữ 32/24/16px · favicon 16/24/32/48</span></div>
 <div class="c px"><div class="row" style="gap:28px">
   <div>{img("favicon-16.png", h=128)}<div class="cap">favicon-16 ×8</div></div>
   <div>{img("favicon-32.png", h=128)}<div class="cap">favicon-32 ×4</div></div>
   <div style="background:#202124;padding:6px;border-radius:10px">{img("favicon-32.png", h=116)}</div></div><span class="l">phóng to: đọc ra chữ i, không thành ô vuông, không hai vạch</span></div>
</div>

<h2>04 · Icon ứng dụng</h2>
<div class="g" style="grid-template-columns:1fr 1fr 1fr 1fr;height:240px">
 <div class="c smoke"><img src="_icons/ios-b-180.png" style="height:180px"><span class="l">app-icon-1024 (iOS bo góc) · phương án B</span></div>
 <div class="c smoke"><div class="row">{img("apple-touch-icon-180.png", h=90)}{img("apple-touch-icon-180.png", h=60)}{img("apple-touch-icon-180.png", h=40)}</div><span class="l">apple-touch-icon 90/60/40</span></div>
 <div class="c smoke"><img src="_icons/and-b-180.png" style="height:180px"><span class="l">android · nền + lớp trước · mặt nạ tròn</span></div>
 <div class="c smoke"><div style="width:180px;height:180px;position:relative;background:repeating-conic-gradient(#dfe3f3 0 25%,#fff 0 50%) 0 0/20px 20px;border-radius:12px">{img("android-foreground-432.png", h=180)}<div style="position:absolute;left:35px;top:35px;width:110px;height:110px;border:1px dashed #2F43DB;border-radius:50%"></div></div><span class="l">lớp trước · vòng an toàn 66dp</span></div>
</div>

<h2>05 · Vùng an toàn và nền</h2>
<div class="g" style="grid-template-columns:1.2fr 1fr 1fr 1fr;height:150px">
 <div class="c"><div style="position:relative;padding:23px;border:1px dashed #2F43DB;margin-bottom:14px">{img("invlogis-primary.svg", h=44)}</div><span class="l">khoảng trống ≥ 1 x (chiều cao chữ x) mỗi phía</span></div>
 <div class="c" style="background:#FAF8F4">{img("invlogis-primary.svg", w=240)}<span class="l">giấy ấm #FAF8F4</span></div>
 <div class="c smoke">{img("invlogis-primary.svg", w=240)}<span class="l">xanh khói #E6EAF8</span></div>
 <div class="c" style="background:#17206F;border-color:#17206F">{img("invlogis-reverse.svg", w=240)}<span class="l" style="color:#C4CDFF">chàm đậm #17206F</span></div>
</div>
</body></html>'''
html = html.replace('class="ios"', 'style="height:180px;border-radius:40px"')
(H / "logo-sheet.html").write_text(html)
