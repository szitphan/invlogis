#!/usr/bin/env python3
"""Sinh 3 ứng dụng mẫu + board hướng C. Cần _build.py chạy trước."""
import base64,os,re
H=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(H,'../../fonts')
def b64(n): return base64.b64encode(open(os.path.join(F,n),'rb').read()).decode()
def logo(n):
    s=open(os.path.join(H,n)).read(); return re.sub(r'<\?xml[^>]*\?>','',s).strip()
def inline(n,w=None,h=None,style=''):
    s=logo(n)
    if w: s=re.sub(r'width="\d+" height="\d+"',f'width="{w}"' + (f' height="{h}"' if h else ''),s,1)
    return s
FONTS=f"""@font-face{{font-family:Lexend;font-weight:300;src:url(data:font/ttf;base64,{b64('Lexend-300.ttf')})}}
@font-face{{font-family:Lexend;font-weight:400;src:url(data:font/ttf;base64,{b64('Lexend-400.ttf')})}}
@font-face{{font-family:Lexend;font-weight:600;src:url(data:font/ttf;base64,{b64('Lexend-600.ttf')})}}
@font-face{{font-family:'Geist Mono';font-weight:400;src:url(data:font/ttf;base64,{b64('GeistMono-400.ttf')})}}"""
NOISE="data:image/svg+xml;utf8,"+"%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E"
BASE=f"""{FONTS}
:root{{--cobalt:#1a23d1;--deep:#0f14b3;--ink:#0f1433;--paper:#fbf9f5;--smoke:#a2b5cd;--violet:#7a4dff;--coral:#ff6b5e;--amber:#ffa24d}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:Lexend,sans-serif;-webkit-font-smoothing:antialiased}}
.mono{{font-family:'Geist Mono',monospace}}
.silk{{position:absolute;inset:0;overflow:hidden;background:#0d1180}}
.silk b{{position:absolute;border-radius:50%;filter:blur(var(--bl,50px))}}
.silk::after{{content:'';position:absolute;inset:0;background:url("{NOISE}");opacity:.42;mix-blend-mode:overlay}}
"""
def silk(variant=0):
    if variant==0:   # rộng, ngang
        L=[('#2f4dff',-10,-20,90,60,-18,70),('#7a4dff',45,-30,70,50,-30,60),('#ff6b5e',20,40,80,22,-32,45),('#ffa24d',50,58,55,10,-34,30),('#0a0d62',-15,60,70,60,0,80)]
    elif variant==1: # dọc
        L=[('#2f4dff',-20,-5,110,40,-35,70),('#7a4dff',20,25,90,26,-38,55),('#ff6b5e',-10,55,100,18,-36,45),('#ffa24d',30,70,60,8,-38,30),('#0a0d62',-20,85,110,40,0,80)]
    else:            # nhỏ (di động)
        L=[('#2f4dff',-30,-10,140,36,-30,60),('#7a4dff',-10,30,120,22,-34,50),('#ff6b5e',-20,52,140,16,-32,45),('#0a0d62',-30,78,150,40,0,70)]
    s=''.join(f'<b style="background:{c};left:{x}%;top:{y}%;width:{w}%;height:{h}%;transform:rotate({r}deg);--bl:{bl}px"></b>' for c,x,y,w,h,r,bl in L)
    return f'<div class="silk">{s}</div>'

def chips(items,cls=''):
    return ''.join(f'<span class="chip {cls}">[{t}]</span>' for t in items)
CHIPCSS="""
.chip{font-family:'Geist Mono',monospace;font-size:var(--cs,22px);color:#fff;border:1px solid rgba(255,255,255,.55);border-radius:999px;padding:.35em .9em;background:rgba(255,255,255,.1);backdrop-filter:blur(10px);white-space:nowrap}
.hair{height:1px;background:rgba(255,255,255,.4)}
"""
# ---------- converge graphic: chips -> hairline curves -> solid dot -> record card
def converge(W,H,labels,dotx,doty,x0,cs,color='rgba(255,255,255,.7)'):
    n=len(labels); gap=H/(n+1); out=''
    for i,l in enumerate(labels):
        y=gap*(i+1); out+=f'<path d="M{x0+ 0} {y} C {x0+W*.35} {y}, {dotx-W*.25} {doty}, {dotx} {doty}" stroke="{color}" stroke-width="1.5" fill="none"/>'
    return out
def converge_html(w,h,labels,cs=22,rec=''):
    n=len(labels); chipw=cs*9; dotx=w*.80; doty=h/2; gap=h/(n+1)
    svg=f'<svg width="{w}" height="{h}" style="position:absolute;inset:0">'
    for i,l in enumerate(labels):
        y=gap*(i+1); x0=chipw+10
        svg+=f'<path d="M{x0} {y} C {x0+(dotx-x0)*.55} {y}, {dotx-(dotx-x0)*.45} {doty}, {dotx} {doty}" stroke="rgba(255,255,255,.75)" stroke-width="1.5" fill="none"/>'
    svg+=f'<circle cx="{dotx}" cy="{doty}" r="{cs*1.1}" fill="#fff"/><circle cx="{dotx}" cy="{doty}" r="{cs*2.1}" fill="none" stroke="rgba(255,255,255,.5)" stroke-width="1"/></svg>'
    cs_html=''.join(f'<span class="chip" style="position:absolute;left:0;top:{gap*(i+1)}px;transform:translateY(-50%);--cs:{cs}px">[{l}]</span>' for i,l in enumerate(labels))
    return f'<div style="position:relative;width:{w}px;height:{h}px">{svg}{cs_html}</div>'

# ---------- deck cover
deck=f"""<!doctype html><html lang="vi"><meta charset="utf-8"><title>Invlogis · bìa deck (C)</title><style>{BASE}{CHIPCSS}
body{{width:1920px;height:1080px;position:relative;overflow:hidden;background:#0d1180;color:#fff}}
.in{{position:absolute;inset:0;padding:84px 100px}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.lab{{font-family:'Geist Mono',monospace;font-size:20px;letter-spacing:.04em;color:rgba(255,255,255,.85)}}
h1{{font-weight:300;font-size:108px;line-height:1.06;letter-spacing:-.035em;position:absolute;left:100px;top:300px;width:1060px}}
h1 em{{font-style:normal;font-weight:600}}
.sub{{position:absolute;left:100px;top:660px;width:760px;font-size:30px;line-height:1.5;font-weight:300;color:rgba(255,255,255,.92)}}
.bot{{position:absolute;left:100px;right:100px;bottom:76px;display:flex;justify-content:space-between;align-items:flex-end}}
.frame{{position:absolute;right:100px;top:210px;width:640px;height:660px;border:1px solid rgba(255,255,255,.5);border-radius:36px;background:rgba(255,255,255,.07);backdrop-filter:blur(14px)}}
.frame .tag{{position:absolute;left:28px;top:22px}}
.hair2{{position:absolute;left:100px;right:100px;bottom:150px;height:1px;background:rgba(255,255,255,.4)}}
</style><body>{silk(0)}
<div class="in"><div class="top">{inline('_logo-reverse-bare.svg',300)}<span class="lab">[ 2026 · BẢN GIỚI THIỆU ]</span></div></div>
<h1>Mọi chứng từ,<br><em>một hồ sơ</em> đúng mốc.</h1>
<p class="sub">Invlogis đọc Booking Note, eDO, EIR, phiếu cân và tờ khai có QR của Việt Nam, rồi đưa thẳng vào hồ sơ lô hàng. Chúng tôi giúp bạn bớt nhập lại.</p>
<div class="frame"><span class="lab tag">[ CHỨNG TỪ → HỒ SƠ ]</span><div style="position:absolute;left:34px;top:90px">{converge_html(572,520,['Booking Note','eDO','EIR','Phiếu cân','Tờ khai QR'],20)}</div></div>
<div class="hair2"></div>
<div class="bot"><span class="lab">invlogis.com</span><span class="lab">by innvie</span></div>
</body></html>"""
open(os.path.join(H,'deck-cover.html'),'w').write(deck)

# ---------- social post
soc=f"""<!doctype html><html lang="vi"><meta charset="utf-8"><title>Invlogis · bài mạng xã hội (C)</title><style>{BASE}{CHIPCSS}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#0d1180;color:#fff}}
.lab{{font-family:'Geist Mono',monospace;font-size:20px;letter-spacing:.04em;color:rgba(255,255,255,.88)}}
.top{{position:absolute;left:72px;right:72px;top:72px;display:flex;justify-content:space-between;align-items:center}}
h1{{position:absolute;left:72px;top:250px;width:900px;font-weight:300;font-size:104px;line-height:1.05;letter-spacing:-.035em}}
h1 em{{font-style:normal;font-weight:600}}
.card{{position:absolute;left:72px;right:72px;top:700px;height:420px;border:1px solid rgba(255,255,255,.55);border-radius:40px;background:rgba(255,255,255,.08);backdrop-filter:blur(14px)}}
.bot{{position:absolute;left:72px;right:72px;bottom:72px;display:flex;justify-content:space-between;align-items:center}}
.pill{{border:1px solid rgba(255,255,255,.6);border-radius:999px;padding:12px 26px;font-size:22px;font-weight:300}}
</style><body>{silk(1)}
<div class="top">{inline('_logo-reverse-bare.svg',250)}<span class="lab">[ RA MẮT ]</span></div>
<h1>Đọc xong chứng từ, <em>vào thẳng hồ sơ.</em></h1>
<div class="card"><span class="lab" style="position:absolute;left:32px;top:26px">[ ĐÃ ĐỌC · 5 / 5 ]</span><div style="position:absolute;left:36px;top:70px">{converge_html(900,320,['Booking Note','eDO','EIR','Phiếu cân','Tờ khai QR'],17)}</div></div>
<div class="bot"><span class="pill">Đặt lịch xem thử →</span><span class="lab">by innvie</span></div>
</body></html>"""
open(os.path.join(H,'social-post.html'),'w').write(soc)

# ---------- splash
spl=f"""<!doctype html><html lang="vi"><meta charset="utf-8"><title>Invlogis · splash (C)</title><style>{BASE}
body{{width:390px;height:844px;position:relative;overflow:hidden;background:#0d1180;color:#fff}}
.c{{position:absolute;left:0;right:0;top:300px;display:flex;flex-direction:column;align-items:center;gap:26px}}
.lab{{font-family:'Geist Mono',monospace;font-size:11px;letter-spacing:.06em;color:rgba(255,255,255,.85)}}
.ld{{width:120px;height:1px;background:rgba(255,255,255,.3);position:relative}}.ld i{{position:absolute;left:0;top:-1px;width:44px;height:3px;border-radius:2px;background:#fff}}
.foot{{position:absolute;left:0;right:0;bottom:44px;text-align:center;font-weight:300;font-size:13px;color:rgba(255,255,255,.85)}}
.foot::before{{content:'';display:block;width:40px;height:1px;background:rgba(255,255,255,.4);margin:0 auto 16px}}
</style><body>{silk(2)}
<div class="c">{inline('_logo-reverse-bare.svg',220)}<div class="ld"><i></i></div><span class="lab">[ đang mở hồ sơ… ]</span></div>
<div class="foot">Được phát triển bởi innvie</div>
</body></html>"""
open(os.path.join(H,'splash-mobile.html'),'w').write(spl)

# ---------- board
import base64 as _b
def img(n,w): 
    d=_b.b64encode(open(os.path.join(H,n),'rb').read()).decode(); return f'<img src="data:image/png;base64,{d}" style="width:{w}px;display:block;border-radius:14px;border:1px solid rgba(15,20,51,.12)">'
sw=lambda hexv,name,role,dark=False: f'<div style="flex:1"><div style="height:92px;background:{hexv};border-radius:12px;border:1px solid rgba(15,20,51,.12)"></div><div class="mono" style="font-size:13px;margin-top:8px">{hexv}</div><div style="font-size:13px;font-weight:600">{name}</div><div style="font-size:12px;color:#5b6a8c">{role}</div></div>'
board=f"""<!doctype html><html lang="vi"><meta charset="utf-8"><title>Invlogis · hướng C · Hội tụ</title><style>{BASE}
body{{width:1600px;height:2000px;background:#fbf9f5;color:#0f1433;padding:64px 72px;position:relative;overflow:hidden}}
.lab{{font-family:'Geist Mono',monospace;font-size:13px;letter-spacing:.05em;color:#5b6a8c;text-transform:uppercase}}
.box{{border:1px solid rgba(15,20,51,.14);border-radius:24px;position:relative;overflow:hidden}}
.box>.lab{{position:absolute;left:22px;top:18px;z-index:3}}
.row{{display:flex;gap:24px;margin-top:30px}}
h1{{font-weight:300;font-size:60px;letter-spacing:-.03em;line-height:1.05}} h1 b{{font-weight:600}}
p{{font-size:16px;line-height:1.55;font-weight:300}}
.k{{font-size:14px;line-height:1.5}} .k b{{font-weight:600}}
</style><body>
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div class="lab">Hướng C · việc 1.5 · bản nháp 14/10/2026</div><h1 style="margin-top:10px">Hội tụ — <b>nhiều nguồn, một hồ sơ</b></h1></div><div style="width:380px"><p>Hai nét từ hai phía chụm về một chấm đặc: chứng từ của cảng, hãng tàu, lái xe về một dữ liệu đã chốt. Chữ "v" của Việt và innvie lặp lại trong tên.</p></div></div>
<div class="row">
 <div class="box" style="flex:1.45;height:360px;background:#fff;display:flex;align-items:center;justify-content:center"><span class="lab">Logo chính</span>{inline('invlogis-logo.svg',760)}</div>
 <div class="box" style="flex:.55;height:360px;background:#fff;display:flex;align-items:center;justify-content:center"><span class="lab">Ký hiệu</span>{inline('invlogis-symbol.svg',230)}</div>
</div>
<div class="row">
 <div class="box" style="flex:1;height:250px;background:#fff;display:flex;align-items:center;justify-content:center"><span class="lab">by innvie</span>{inline('invlogis-by-innvie.svg',520)}</div>
 <div class="box" style="flex:.55;height:250px;background:#fff;display:flex;align-items:center;justify-content:center"><span class="lab">innvie</span>{inline('innvie-logo.svg',300)}</div>
 <div class="box" style="flex:.7;height:250px;background:#fff;display:flex;align-items:center;justify-content:center"><span class="lab">Đơn sắc</span>{inline('invlogis-logo-mono.svg',380)}</div>
</div>
<div class="row">
 <div class="box" style="flex:1;height:230px;display:flex;align-items:center;justify-content:center;background:#0f1433"><span class="lab" style="color:#a2b5cd">Đảo màu · nền mực</span>{inline('_logo-reverse-bare.svg',500)}</div>
 <div class="box" style="flex:1;height:230px;display:flex;align-items:center;justify-content:center;background:#1a23d1"><span class="lab" style="color:#c7d4ff">Đảo màu · nền cobalt</span>{inline('_logo-reverse-bare.svg',500)}</div>
 <div class="box" style="flex:.7;height:230px;background:#fff;display:flex;align-items:center;justify-content:center;gap:26px"><span class="lab">Favicon · app icon</span>
   <div style="text-align:center"><img src="data:image/png;base64,{_b.b64encode(open(os.path.join(H,'favicon-16.png'),'rb').read()).decode()}" width="16" height="16"><div class="mono" style="font-size:11px;margin-top:6px">16</div></div>
   <div style="text-align:center"><img src="data:image/png;base64,{_b.b64encode(open(os.path.join(H,'favicon-32.png'),'rb').read()).decode()}" width="32" height="32"><div class="mono" style="font-size:11px;margin-top:6px">32</div></div>
   <div style="text-align:center"><img src="data:image/png;base64,{_b.b64encode(open(os.path.join(H,'app-icon-1024.png'),'rb').read()).decode()}" width="96" height="96" style="border-radius:22px"><div class="mono" style="font-size:11px;margin-top:6px">1024</div></div></div>
</div>
<div class="row" style="align-items:flex-start">
 <div style="flex:1"><div class="lab" style="margin-bottom:12px">Màu</div>
  <div style="display:flex;gap:14px">{sw('#1a23d1','Cobalt','chủ đạo · 9.06:1 trên giấy')}{sw('#0f14b3','Cobalt sâu','chấm hội tụ')}{sw('#0f1433','Mực chàm','chữ · 17.1:1')}{sw('#fbf9f5','Giấy ấm','nền')}{sw('#a2b5cd','Xanh khói','phụ')}</div>
  <div style="height:70px;border-radius:12px;margin-top:14px;background:linear-gradient(100deg,#0a0d62 0%,#2f4dff 28%,#7a4dff 52%,#ff6b5e 78%,#ffa24d 100%)"></div><div class="mono" style="font-size:12px;margin-top:6px;color:#5b6a8c">dải chiến dịch · neo cobalt, hạt nhiễu + vệt hướng khi dùng thật</div>
  <div class="lab" style="margin:22px 0 10px">Chữ</div>
  <div style="font-weight:600;font-size:46px;letter-spacing:-.02em;line-height:1.1">invlogis <span style="font-weight:300">Việt Nam</span></div>
  <div style="font-weight:300;font-size:22px;margin-top:8px">Lexend 300/600 · đủ dấu: ắ ằ ẳ ẵ ặ ế ề ể ễ ệ ố ồ ổ ỗ ộ ớ ờ ở ỡ ợ ứ ừ ử ữ ự đ</div>
  <div class="mono" style="font-size:16px;margin-top:10px">[Booking Note] [eDO] [Phiếu cân] — Geist Mono</div></div>
 <div style="flex:1.05"><div class="lab" style="margin-bottom:12px">Ứng dụng mẫu</div>
  <div style="display:flex;gap:16px;align-items:flex-start">{img('splash-mobile.png',215)}<div style="display:flex;flex-direction:column;gap:16px">{img('deck-cover.png',520)}{img('social-post.png',260)}</div></div></div>
</div>
<div class="row" style="margin-top:26px;gap:40px"><div class="k" style="flex:1"><b>Tự kiểm.</b> 16px: V + chấm đọc rõ trên ô cobalt. Đơn sắc: giữ nguyên hình, mất gradient. Đối xứng nên không đọc thành dấu tick. Không dùng xe, container, địa cầu, mũi tên.</div><div class="k" style="flex:1"><b>Điểm yếu.</b> "V + chấm" có thể gợi ngón tay chỉ xuống hay chân đĩa; ký hiệu chỉ 2 nét (3 nét thử đều thành đinh ba hoặc mũi tên). Vệt san hô trên nền xanh rực gần gu ElevenLabs.</div></div>
</body></html>"""
open(os.path.join(H,'board.html'),'w').write(board)
