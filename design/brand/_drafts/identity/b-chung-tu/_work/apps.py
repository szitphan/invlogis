import subprocess
from common import *
R = ROOT; T = str(R.parents[1]/"_tools"/"render.py")
def render(html, png, w, h, scale=1): subprocess.run(["python3",T,str(html),str(png),"--size",f"{w}x{h}","--scale",str(scale)],check=True,capture_output=True)

# ---------- app icon 1024 ----------
d,b = symbol("ai","reverse",small=True)
icon = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024"><defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B0E2B"/><stop offset=".6" stop-color="#1A2294"/><stop offset="1" stop-color="#3B4EF2"/></linearGradient>
<radialGradient id="gl" cx=".68" cy=".3" r=".5"><stop offset="0" stop-color="#8B5CF6" stop-opacity=".75"/><stop offset="1" stop-color="#8B5CF6" stop-opacity="0"/></radialGradient>
<radialGradient id="gl2" cx=".25" cy=".95" r=".5"><stop offset="0" stop-color="#F062B4" stop-opacity=".45"/><stop offset="1" stop-color="#F062B4" stop-opacity="0"/></radialGradient>
<filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .8 0"/></filter>
<defs>{d}</defs></defs>
<rect width="1024" height="1024" fill="url(#bg)"/><rect width="1024" height="1024" fill="url(#gl)"/><rect width="1024" height="1024" fill="url(#gl2)"/>
<rect width="1024" height="1024" filter="url(#nz)" opacity=".16" style="mix-blend-mode:soft-light"/>
<g transform="translate(172 172) scale(11)">{b}</g></svg>'''
(R/"_work"/"icon.svg").write_text(icon)
subprocess.run(["python3",T,str(R/"_work"/"icon.svg"),str(R/"app-icon-1024.png"),"--size","1024x1024"],check=True,capture_output=True)

HEAD = lambda mode,h: inline(lockup(mode,"hd"+mode[0]), f"height:{h}px;width:auto;display:block")

# ---------- deck cover 1920x1080 ----------
doc_edo = dict(label="eDO",title="Lệnh giao hàng điện tử",idtxt="EDO-2610-048213",rows=[("Số vận đơn","HDMU-SGN-48213"),("Số cont","TCLU 482913-7"),("Cảng dỡ","Cát Lái"),("Hạn lấy","18/10/2026")])
doc_eir = dict(label="EIR",title="Phiếu giao nhận container",idtxt="EIR-CL-771204",rows=[("Cont / Seal","MSKU 719045-3"),("Tình trạng","Nguyên vẹn"),("Giờ qua cổng","09:42")])
doc_bn  = dict(label="Booking Note",title="Phiếu đặt chỗ",idtxt="BKG-HPH-30918",rows=[("Tàu / Chuyến","EVER LUCID 0417E"),("Cut-off","16/10 · 17:00"),("Loại cont","40HC")])
px,py,pw,ph = 1010,56,854,968
inner = (doc(40,90,290,-9,**doc_bn,k=.95,z=1,hits=())
         + doc(500,150,320,7,**doc_eir,k=1,z=1)
         + doc(190,170,380,-3,**doc_edo,k=1.1,z=2,hits=(0,1),note="ĐÃ ĐỌC 4/4 TRƯỜNG · KHỚP BOOKING")
         + beam(420,440,1100,26,-38,z=4)
         + '<div class="chip glass" style="position:absolute;left:60px;bottom:64px;font-size:14px;padding:7px 14px">[ đang đọc chứng từ ]</div>'
         + '<div class="chip glass" style="position:absolute;right:56px;bottom:64px;font-size:14px;padding:7px 14px">12/12 trường · 0 nhập lại</div>')
body = (silk(px,py,pw,ph,36,"vivid",inner=inner)
 + f'<div class="abs" style="left:96px;top:84px">{HEAD("color",54)}</div>'
 + '<div class="abs mono" style="left:96px;top:260px;font-size:15px;color:var(--mute)">[ GIỚI THIỆU SẢN PHẨM ]</div>'
 + '<div class="abs" style="left:96px;top:310px;width:800px;font-size:88px;line-height:1.06;font-weight:500;letter-spacing:-.025em;word-spacing:.04em">Mọi lô hàng bắt đầu từ một tờ giấy được <span style="color:var(--cobalt)">đọc đúng.</span></div>'
 + '<div class="abs" style="left:96px;top:700px;width:600px;text-wrap:balance;font-size:27px;line-height:1.5;color:var(--mute);font-weight:400">Invlogis đọc eDO, EIR, Booking Note vào thẳng hồ sơ. Bớt nhập lại, đúng mốc, minh bạch.</div>'
 + '<div class="abs" style="left:96px;right:960px;top:916px;height:1px;background:var(--line)"></div>'
 + '<div class="abs mono" style="left:96px;top:944px;font-size:15px;color:var(--mute)">10.2026</div><div class="abs mono" style="left:300px;top:944px;font-size:15px;color:var(--mute)">by innvie</div>'
 + ''.join(f'<div class="abs" style="{p}width:14px;height:14px;border:solid var(--line);{bd}"></div>' for p,bd in [("left:56px;top:56px;","border-width:1px 0 0 1px;"),("left:928px;top:56px;","border-width:1px 1px 0 0;"),("left:56px;top:1010px;","border-width:0 0 1px 1px;"),("left:928px;top:1010px;","border-width:0 1px 1px 0;")]))
page(R/"deck-cover.html","Invlogis · deck cover",1920,1080,body,"#FAFAF7"); render(R/"deck-cover.html",R/"deck-cover.png",1920,1080)

# ---------- social 1080x1350 ----------
sw_,sh_ = 1080,1350
inner = (doc(60,20,290,-8,**doc_bn,k=.82,z=1)
         + doc(700,40,290,8,**doc_eir,k=.82,z=1)
         + doc(370,-26,340,-2,**doc_edo,k=.95,z=2,hits=(0,1),note="ĐÃ ĐỌC 4/4 TRƯỜNG")
         + beam(540,250,1500,24,-38)
         + '<div class="chip glass" style="z-index:9;position:absolute;left:56px;bottom:50px;font-size:16px;padding:8px 16px">[eDO]</div><div class="chip glass" style="z-index:9;position:absolute;left:150px;bottom:50px;font-size:16px;padding:8px 16px">[EIR]</div><div class="chip glass" style="z-index:9;position:absolute;left:236px;bottom:50px;font-size:16px;padding:8px 16px">[Booking Note]</div>'
         + '<div class="mono abs" style="z-index:9;right:56px;bottom:58px;font-size:15px;color:rgba(255,255,255,.92)">~110.000 lô/năm đã chạy thật</div>')
body = (f'<div class="abs" style="left:72px;top:68px">{HEAD("color",50)}</div>'
 + '<div class="chip abs" style="right:72px;top:74px;font-size:15px;padding:7px 14px">[ 10.2026 ]</div>'
 + '<div class="abs" style="left:72px;top:210px;width:900px;font-size:104px;line-height:1.02;font-weight:500;letter-spacing:-.03em;word-spacing:.04em">Bớt nhập lại.<br>Đúng mốc.<br><span style="color:var(--cobalt)">Minh bạch.</span></div>'
 + '<div class="abs" style="left:72px;top:610px;width:820px;font-size:30px;line-height:1.45;color:var(--mute)">Chúng tôi đọc chứng từ cảng Việt Nam, từ eDO đến phiếu cân, vào thẳng hồ sơ lô hàng của bạn.</div>'
 + silk(0,750,sw_,600,0,"vivid",inner=inner)
 + '<div class="abs" style="left:0;right:0;top:750px;height:1px;background:rgba(18,22,63,.2);z-index:9"></div>')
page(R/"social-post.html","Invlogis · social post",sw_,sh_,body,"#FAFAF7"); render(R/"social-post.html",R/"social-post.png",sw_,sh_)

# ---------- splash 390x844 ----------
sw_,sh_=390,844
inner = (doc(-60,520,190,-10,**doc_bn,k=.55,z=1,fill=.22)
         + doc(250,500,190,9,**doc_eir,k=.55,z=1,fill=.22)
         + beam(195,190,700,12,-38,z=3)
         + f'<div class="abs" style="left:{195-66}px;top:300px;width:132px;height:132px;z-index:6">{sym_inline("sp","reverse")}</div>'
         + '<div class="abs" style="left:0;right:0;top:458px;text-align:center;z-index:6;font-size:40px;font-weight:500;letter-spacing:-.03em;color:#fff">Invlogis</div>'
         + '<div class="chip glass abs" style="left:50%;transform:translateX(-50%);top:536px;font-size:11px;padding:6px 12px;z-index:6;white-space:nowrap">[ đang đọc chứng từ ]</div>'
         + '<div class="abs mono" style="left:0;right:0;bottom:44px;text-align:center;z-index:6;font-size:11px;color:rgba(255,255,255,.88)">Được phát triển bởi innvie</div>')
body = silk(0,0,sw_,sh_,0,"deep",inner=inner)
page(R/"splash-mobile.html","Invlogis · splash",sw_,sh_,body,"#0B0E2B"); render(R/"splash-mobile.html",R/"splash-mobile.png",sw_,sh_,2)
print("apps ok")
