from common import *
import subprocess
R=ROOT
def img(src,style=""): return f'<img src="{src}" style="{style}">'
def sw(hexc,name,role,txt="#fff"): return f'<div style="flex:1;min-width:0"><div style="height:92px;border-radius:10px;background:{hexc};border:1px solid rgba(18,22,63,.12)"></div><div style="font-size:14px;font-weight:600;margin-top:10px">{name}</div><div class="mono" style="font-size:11px;color:var(--mute)">{hexc}</div><div style="font-size:12px;color:var(--mute);margin-top:2px;line-height:1.35">{role}</div></div>'
def lab(t): return f'<div class="mono" style="font-size:12px;color:var(--mute);margin-bottom:16px">[ {t} ]</div>'
def sec(x,y,w,h,body,extra=""): return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}">{body}</div>'
big = sym_inline("bg1","color",style="width:100%;height:100%")
# chú thích cấu tạo
callouts=[("Tấm sau · xoay −7°",22,60,0.17,.13),("Tấm trước · tỉ lệ A4, góc gấp",338,40,.85,.08),("Vệt quét · ánh sáng đi qua, −38°",360,230,.97,.52),("Sợi chỉ mảnh · độ chính xác",360,330,.78,.72)]
co=""
S=380
def pt(fx,fy): return (fx*S,fy*S)
for t,tx,ty,fx,fy in [("Tấm sau · xoay −7°",-190,40,.25,.2),("Tấm trước · A4, góc gấp",330,-4,.80,.24),("Vệt quét · −38°, ánh sáng đi qua",340,150,.93,.38),("Sợi chỉ mảnh",340,262,.76,.67)]:
    x,y=pt(fx,fy)
    co+=f'<div class="abs mono" style="left:{tx}px;top:{ty}px;font-size:11px;color:var(--ink);white-space:nowrap">{t}</div>'
body=""
body+=sec(72,64,900,60,inline(lockup("color","hb"),"height:60px;width:auto"))
body+=sec(1128,72,400,30,'<div class="mono" style="font-size:13px;text-align:right;color:var(--mute)">HƯỚNG B · CHỨNG TỪ</div>')
body+=sec(72,170,1000,230,'<div style="font-size:64px;line-height:1.06;font-weight:500;letter-spacing:-.025em">AI đọc chứng từ: mọi việc bắt đầu từ <span style="color:var(--cobalt)">một tờ giấy được đọc đúng.</span></div>')
body+=sec(1128,184,400,200,'<div style="font-size:16px;line-height:1.55;color:var(--mute)">Ký hiệu là hai tấm giấy tỉ lệ A4 xếp lệch, tấm trước có góc gấp, một vệt quét sáng đi chéo qua. Chính xác, chất kỹ sư, minh bạch. Vệt quét chéo −38° để không thành thanh ngang.</div>')
# hàng logo
body+=sec(72,430,1456,1,'',"background:var(--line)")
body+=sec(72,456,1456,260,
 f'<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:20px;height:100%">'
 f'<div style="border:1px solid var(--line);border-radius:18px;display:flex;align-items:center;justify-content:center;background:#fff">{inline(lockup("color","hw"),"height:88px;width:auto")}</div>'
 f'<div style="border-radius:18px;display:flex;align-items:center;justify-content:center;background:#12163F">{inline(lockup("reverse","hr"),"height:76px;width:auto")}</div>'
 f'<div style="border:1px solid var(--line);border-radius:18px;display:flex;align-items:center;justify-content:center;background:#F7F6F2;color:#12163F">{inline(lockup("mono","hm"),"height:76px;width:auto")}</div></div>')
body+=sec(72,736,1456,170,
 f'<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:20px;height:100%">'
 f'<div style="border:1px solid var(--line);border-radius:18px;display:flex;align-items:center;justify-content:center;background:#fff;gap:56px">{inline(lockup("color","hby",by=True),"height:90px;width:auto")}</div>'
 f'<div style="border:1px solid var(--line);border-radius:18px;display:flex;align-items:center;justify-content:center;background:#fff">{inline(innvie("color"),"height:70px;width:auto")}</div>'
 f'<div style="border-radius:18px;position:relative;overflow:hidden;background:linear-gradient(140deg,#0E1250,#3B4EF2)"><div class="abs" style="left:0;top:0;right:0;bottom:0;background:radial-gradient(circle at 80% 20%,#F062B4aa,transparent 55%),radial-gradient(circle at 20% 100%,#FF8F63aa,transparent 50%)"></div><div style="position:relative;display:flex;height:100%;align-items:center;justify-content:center">{inline(lockup("reverse","hr2"),"height:62px;width:auto")}</div></div></div>')
# cấu tạo + thử nhỏ
body+=sec(72,944,720,420,lab("CẤU TẠO KÝ HIỆU")+f'<div style="position:relative;height:340px"><div class="abs" style="left:230px;top:0;width:{S*.85:.0f}px;height:{S*.85:.0f}px;">{big}</div>'+
  ''.join(f'<div class="abs mono" style="left:{x}px;top:{y}px;font-size:11px;white-space:nowrap;color:var(--ink)">{t}</div>' for t,x,y in [("Tấm sau · xoay −7°",85,50),("Tấm trước · A4, bo góc",70,120),("Góc gấp",590,10),("Vệt quét −38°",540,120),("Sợi chỉ mảnh",545,215)])+'</div>')
body+=sec(830,944,698,420,lab("THỬ NHỎ VÀ THỬ SẮC")+
  '<div style="display:flex;gap:28px;align-items:flex-end;flex-wrap:wrap">'
  +''.join(f'<div style="text-align:center"><div style="padding:14px;border:1px solid var(--line);border-radius:12px;background:#fff">{img(f"favicon-{n}.png",f"width:{n}px;height:{n}px;display:block")}</div><div class="mono" style="font-size:11px;margin-top:6px;color:var(--mute)">{n}px</div></div>' for n in (16,32))
  +f'<div style="text-align:center"><div style="padding:14px;border:1px solid var(--line);border-radius:12px;background:#fff">{img("favicon-32.png","width:64px;height:64px;display:block;image-rendering:pixelated")}</div><div class="mono" style="font-size:11px;margin-top:6px;color:var(--mute)">32 → 64 (phóng)</div></div>'
  +f'<div style="text-align:center">{img("app-icon-1024.png","width:120px;height:120px;border-radius:27px;display:block")}<div class="mono" style="font-size:11px;margin-top:6px;color:var(--mute)">app icon</div></div>'
  +f'<div style="text-align:center"><div style="width:96px;height:96px;border:1px solid var(--line);border-radius:12px;color:#12163F;padding:12px;background:#fff">{sym_inline("bm","mono")}</div><div class="mono" style="font-size:11px;margin-top:6px;color:var(--mute)">đơn sắc</div></div>'
  +'</div>'
  +'<div style="margin-top:22px;font-size:14px;line-height:1.55;color:var(--mute);max-width:600px">Từ 32px trở xuống dùng bản rút gọn: một tấm giấy, nét dày hơn, bỏ sợi chỉ và góc gấp (chỉ còn góc cắt). Vẫn còn đủ hai thành phần: tờ giấy và vệt quét.</div>')
# màu
body+=sec(72,1396,1456,170,lab("MÀU")+'<div style="display:flex;gap:16px">'
  +sw("#12163F","Navy mực","chữ, logo, nền sâu · hue 235°")+sw("#3B4EF2","Cobalt điện","nhấn, vệt quét · hue 234°")+sw("#5B47F5","Tím chàm","đầu vệt quét · hue 247°")+sw("#9AA8CC","Xanh khói","viền, chữ phụ trên nền tối")+sw("#F7F6F2","Giấy ấm","nền ấm")+sw("#ECEEF6","Sương","nền khối")+sw("#5B6190","Xám chàm","chữ phụ · 5,9:1")+'</div>')
body+=sec(72,1596,1456,60,'<div class="silk" style="position:relative;height:44px;border-radius:12px;background:linear-gradient(90deg,#0E1250,#3B4EF2 28%,#8B5CF6 48%,#F062B4 68%,#FF8F63 86%,#FFC774)"><div class="grain"></div></div><div class="mono" style="font-size:11px;color:var(--mute);margin-top:8px">DẢI CHIẾN DỊCH · navy → cobalt → tím → hồng → cam → vàng, neo về xanh</div>')
# chữ
body+=sec(72,1690,520,250,lab("CHỮ")+'<div style="font-size:54px;font-weight:500;letter-spacing:-.025em;line-height:1">Manrope</div><div style="font-size:18px;margin-top:12px;line-height:1.5">Chữ không chân độ đậm vừa (500), chính xác. Đủ dấu: ắ ằ ẳ ẵ ặ ế ề ể ễ ệ ố ồ ổ ỗ ộ ớ ờ ở ỡ ợ ứ ừ ử ữ ự đ Đ</div><div class="mono" style="margin-top:12px;font-size:13px;color:var(--mute)">[eDO] [EIR] [Booking Note] · JetBrains Mono 500</div>')
# ứng dụng
for i,(f,w,h,x) in enumerate([("deck-cover.png",1920,1080,630),("social-post.png",1080,1350,1005),("splash-mobile.png",780,1688,1245)]):
    hh=250
    ww=int(hh*w/h)
    body+=sec(x if i<0 else [630,1100,1330][i],1690,ww,hh,img(f"{f}",f"width:{ww}px;height:{hh}px;border-radius:10px;border:1px solid var(--line);display:block"))
body+=sec(630,1958-20,900,24,'<div class="mono" style="font-size:11px;color:var(--mute)">deck-cover 1920×1080 · social-post 1080×1350 · splash-mobile 390×844</div>')
page(R/"board.html","Invlogis · Hướng B · Chứng từ",1600,2000,body,"#FAFAF7")
subprocess.run(["python3",str(R.parents[1]/"_tools"/"render.py"),str(R/"board.html"),str(R/"board.png"),"--size","1600x2000"],check=True,capture_output=True)
print("board ok")
