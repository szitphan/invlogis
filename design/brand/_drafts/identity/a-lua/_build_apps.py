#!/usr/bin/env python3
"""Dựng 3 ứng dụng mẫu hướng A (HTML tự chứa) + xuất PNG. Chạy sau _build_logo.py."""
import base64, re, subprocess, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import _build_logo as L
H = pathlib.Path(__file__).parent; F = H.parents[1] / "fonts"; R = H.parents[1] / "_tools/render.py"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
def img(svg): return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
FONTS = "".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/ttf;base64,{b64(F/fn)}) format('truetype')}}"
  for fam, w, fn in [("Lexend",300,"Lexend-300.ttf"),("Lexend",400,"Lexend-400.ttf"),("Be Vietnam Pro",400,"BeVietnamPro-400.ttf"),("Be Vietnam Pro",500,"BeVietnamPro-500.ttf")])
NOISE = "data:image/svg+xml;base64," + base64.b64encode(b'<svg xmlns="http://www.w3.org/2000/svg" width="320" height="320"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>').decode()
logo_color = img(L.logo_svg()); logo_mono=img(L.logo_svg("mono"))
logo_rev = img(re.sub(r'<rect x="-300"[^>]*/>', "", L.logo_svg("reverse")))
by_rev = img(re.sub(r'<rect x="-300"[^>]*/>', "", L.logo_svg("reverse", by=True)))
by_col = img(L.logo_svg(by=True))
wm_rev = img(L.wordmark_full("#FFFFFF","#C4CDFF")); innvie_col=img(L.innvie_svg()); innvie_rev=img(L.innvie_svg("#FFFFFF","#C4CDFF"))
sym_dark = img(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {L.SW+2} {L.SH+2}"><defs>{L.sym_defs("g",[(0,"#FFFFFF"),(.5,"#C4CDFF"),(1,"#7C8FFF")])}</defs>{L.symbol_inner("url(#g)",sheen=False)}</svg>')
COMMON = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#0E1442;--deep:#17206F;--cobalt:#2F43DB;--peri:#97A6FF;--smoke:#E6EAF8;--paper:#FAF8F4;--mute:#4A5380;
--violet:#7B55FF;--magenta:#E24C9A;--coral:#FF7A59;--amber:#FFB547}
body{font-family:'Be Vietnam Pro',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.display{font-family:'Lexend',sans-serif;font-weight:300;letter-spacing:-.01em}
.silk{position:absolute;inset:0;overflow:hidden;background:linear-gradient(160deg,#0E1442 0%,#1B2AA8 45%,#2F43DB 100%)}
.silk i{position:absolute;display:block;border-radius:50%;filter:blur(var(--b,46px));transform:rotate(-31deg)}
.silk .grain{position:absolute;inset:0;background:url(%NOISE%);opacity:.28;mix-blend-mode:soft-light;filter:none;border-radius:0;transform:none}
.chip{display:inline-flex;align-items:center;font-family:'Lexend',sans-serif;font-weight:400;font-size:var(--cs,22px);letter-spacing:.02em;padding:.32em .8em;border-radius:99px;
  background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.55);color:#fff;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.chip.dk{background:rgba(255,255,255,.7);color:var(--ink);border-color:rgba(14,20,66,.18)}
.frame{border-radius:var(--r,36px);border:1px solid rgba(255,255,255,.55);padding:var(--p,10px)}
.hair{height:1px;background:currentColor;opacity:.25}
""".replace("%NOISE%", NOISE)
def streaks(extra=""):
    return ('<div class="silk">'
      '<i style="left:-20%;top:42%;width:150%;height:30%;background:linear-gradient(90deg,#2F43DB,#7B55FF 45%,#E24C9A 78%,#FF7A59);opacity:.85"></i>'
      '<i style="left:-30%;top:14%;width:140%;height:20%;background:linear-gradient(90deg,#0E1442,#97A6FF 58%,#FFD3C0);opacity:.55;--b:60px"></i>'
      '<i style="left:-10%;top:72%;width:130%;height:26%;background:linear-gradient(90deg,#17206F,#2F43DB 60%,#97A6FF);opacity:.9"></i>'
      '<i style="left:30%;top:28%;width:70%;height:12%;background:linear-gradient(90deg,transparent,#fff 60%,transparent);opacity:.45;--b:34px"></i>'
      + extra + '<div class="grain"></div></div>')
def page(w,h,body,css=""):
    return f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Invlogis · hướng A · Lụa</title><style>{COMMON}html,body{{width:{w}px;height:{h}px;overflow:hidden}}body{{position:relative}}{css}</style></head><body>{body}</body></html>'

# ---------- 1. bìa deck 1920x1080
deck = page(1920,1080, f'''
<div style="position:absolute;inset:0;background:var(--paper)"></div>
<div style="position:absolute;left:96px;top:84px"><img src="{logo_color}" style="height:62px;display:block"></div>
<div class="mono" style="position:absolute;left:96px;top:300px;width:820px">
  <div style="font-family:Lexend;font-size:20px;letter-spacing:.14em;color:var(--cobalt);text-transform:uppercase;font-weight:400">Giới thiệu nền tảng · 2026</div>
  <h1 class="display" style="font-size:104px;line-height:1.08;margin-top:34px">Chứng từ Việt,<br>vào thẳng hồ sơ.</h1>
  <p style="font-size:30px;line-height:1.5;color:var(--mute);margin-top:44px;font-weight:400;max-width:700px">Nền tảng vận hành cho doanh nghiệp giao nhận và vận tải container: điều vận, xưởng, dầu và công nợ chung một dữ liệu.</p>
</div>
<div style="position:absolute;left:96px;bottom:84px;right:1010px;display:flex;justify-content:space-between;align-items:flex-end;font-size:20px;color:var(--mute)">
  <div><div class="hair" style="width:340px;margin-bottom:18px;color:var(--ink)"></div>Đã chạy thật ở quy mô khoảng 110.000 lô hàng/năm</div>
  <div style="display:flex;align-items:center;gap:10px;font-size:18px"><span>by</span><img src="{innvie_col}" style="height:26px"></div>
</div>
<div class="frame" style="position:absolute;left:1000px;top:60px;width:864px;height:960px;border-color:rgba(14,20,66,.22);--r:44px;--p:12px">
  <div style="position:relative;width:100%;height:100%;border-radius:34px;overflow:hidden">{streaks()}
    <div style="position:absolute;left:54px;top:70px;display:flex;flex-direction:column;gap:20px;align-items:flex-start"><span class="chip" style="--cs:26px">[Booking Note]</span><span class="chip" style="margin-left:150px;--cs:26px">[eDO]</span></div>
    <div style="position:absolute;right:50px;top:330px;display:flex;flex-direction:column;gap:20px;align-items:flex-end"><span class="chip" style="--cs:26px">[Phiếu cân]</span><span class="chip" style="margin-right:120px;--cs:26px">[EIR]</span></div>
    <div style="position:absolute;left:60px;bottom:74px"><span class="chip dk" style="--cs:26px">[Tờ khai có QR] · đã đọc ✓</span></div>
  </div></div>
''')
# ---------- 2. bài social 1080x1350
social = page(1080,1350, f'''
{streaks()}
<div style="position:absolute;left:72px;top:72px;right:72px;display:flex;justify-content:space-between;align-items:center;color:#fff">
  <img src="{logo_rev}" style="height:44px">
  <span class="chip" style="--cs:19px">Ra mắt · 11/2026</span></div>
<div style="position:absolute;left:72px;top:250px;right:72px;color:#fff">
  <h1 class="display" style="font-size:98px;line-height:1.1;font-weight:300">AI đọc chứng từ,<br>bạn chỉ cần duyệt.</h1>
  <p style="font-size:30px;line-height:1.5;margin-top:34px;max-width:780px;opacity:.92">Booking Note, eDO, EIR, phiếu cân: vào thẳng hồ sơ lô hàng. Bớt nhập lại, đúng mốc, minh bạch.</p></div>
<div class="frame" style="position:absolute;left:72px;right:72px;bottom:150px;--r:36px;--p:10px;background:rgba(255,255,255,.1);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)">
  <div style="border-radius:28px;background:rgba(255,255,255,.88);padding:34px 40px;color:var(--ink)">
    <div style="display:flex;justify-content:space-between;align-items:center"><span class="chip dk" style="--cs:20px;background:#fff">[eDO]</span><span style="font-family:Lexend;font-size:19px;color:var(--cobalt);letter-spacing:.04em">Đã đọc · 4 trường</span></div>
    <div style="margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:20px 40px;font-size:24px">
      <div><div style="font-size:17px;color:var(--mute);margin-bottom:4px">Số vận đơn</div>HDMU 7305 2214</div>
      <div><div style="font-size:17px;color:var(--mute);margin-bottom:4px">Cảng dỡ</div>Cảng Cát Lát, TP. Hồ Chí Minh</div>
      <div><div style="font-size:17px;color:var(--mute);margin-bottom:4px">Hạn lấy container</div>20/11/2026</div>
      <div><div style="font-size:17px;color:var(--mute);margin-bottom:4px">Loại cont</div>40'HC · 1 container</div></div></div></div>
<div style="position:absolute;left:72px;right:72px;bottom:64px;display:flex;justify-content:space-between;color:#fff;font-size:21px;opacity:.9"><span style="display:flex;align-items:center;gap:10px"><span>by</span><img src="{innvie_rev}" style="height:26px"></span><span>Nền tảng cho giao nhận &amp; vận tải container</span></div>
''', "")
# ---------- 3. splash 390x844
splash = page(390,844, f'''
<div class="silk" style="background:linear-gradient(180deg,#0B1033 0%,#141C70 55%,#2F43DB 100%)">
 <i style="left:-40%;top:58%;width:190%;height:22%;background:linear-gradient(90deg,#2F43DB,#7B55FF 50%,#E24C9A 85%,#FF7A59);opacity:.75;--b:34px"></i>
 <i style="left:-50%;top:78%;width:170%;height:20%;background:linear-gradient(90deg,#17206F,#97A6FF 60%,#fff);opacity:.6;--b:30px"></i>
 <i style="left:-30%;top:40%;width:150%;height:9%;background:linear-gradient(90deg,transparent,#97A6FF 55%,transparent);opacity:.5;--b:26px"></i>
 <div class="grain"></div></div>
<div style="position:absolute;left:0;right:0;top:250px;display:flex;flex-direction:column;align-items:center;color:#fff">
  <img src="{sym_dark}" style="height:128px">
  <img src="{wm_rev}" style="height:44px;margin-top:34px">
  <div style="margin-top:18px;font-size:14px;letter-spacing:.04em;opacity:.8">Chứng từ vào thẳng hồ sơ</div></div>
<div style="position:absolute;left:0;right:0;bottom:46px;text-align:center;color:#fff;font-size:12.5px;opacity:.82"><span class="chip" style="--cs:12px;margin-bottom:16px">[Booking Note] · đang đọc…</span><br>Được phát triển bởi innvie</div>
''')
def main():
    out = {"deck-cover":(1920,1080,deck),"social-post":(1080,1350,social),"splash-mobile":(390,844,splash)}
    for n,(w,h,html) in out.items():
        (H/f"{n}.html").write_text(html)
        subprocess.run(["python3",str(R),str(H/f"{n}.html"),str(H/f"{n}.png"),"--size",f"{w}x{h}"+"","--scale","2" if n=="splash-mobile" else "1"],check=True,capture_output=True)

if __name__=='__main__': main(); print('apps ok')
