#!/usr/bin/env python3
"""Sinh nền gradient lụa + hoạ tiết chứng từ + khung thiết bị cho Invlogis (hướng A · Lụa).
  python3 generate.py            # dựng tất cả (HTML + PNG + đo tương phản + sheet)
  python3 generate.py --only bg  # chỉ nền (bg | doc | dev | sheet)
  python3 generate.py --grain 0.5 --angle -31   # tham số hoá hạt + góc vệt
Không gọi API ảnh. Cần Chrome + Pillow (render.py)."""
import argparse, base64, json, pathlib, subprocess, sys, colorsys
from PIL import Image
HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parent / "_tools"
PNG = HERE/"png"; SC = HERE/"_scenes"
SIZES = {"1920x1080":(1920,1080),"1080x1350":(1080,1350),"1080x1080":(1080,1080),"1500x500":(1500,500),"2560x1440":(2560,1440)}
ap = argparse.ArgumentParser(); ap.add_argument("--only"); ap.add_argument("--grain",type=float,default=.42); ap.add_argument("--angle",type=float,default=-31)
OPT = ap.parse_args()

INK="#0E1442"; NIGHT="#0B1033"; DEEP="#17206F"; COB="#2F43DB"; PERI="#97A6FF"; PERI2="#C4CDFF"; SMOKE="#E6EAF8"; PAPER="#FAF8F4"
VIO="#7B55FF"; MAG="#E24C9A"; PEACH="#FFD3C0"; AMB="#FFB547"; AZ="#35B8F0"; LAV="#B79CFF"

# Mỗi blob: (u, v, dài, dày, màu, độ đục, mờ). u: 0 = phía chữ → 1 = phía xa. v: 0..1 ngang. Dài/dày theo sqrt(w*h).
# zone_mode: "white" chữ trắng (nền phải tối) hoặc "ink" chữ mực (nền phải sáng).
BG = {
 "n1-chamdem":  dict(name="Chàm đêm",        kind="neo", mode="white", base=NIGHT, blobs=[(.80,.30,1.3,.34,COB,.85,70),(.92,.62,1.1,.22,PERI,.45,60),(.70,.46,1.5,.05,PERI2,.40,22),(.55,.80,1.2,.2,DEEP,.9,70)]),
 "n2-cobalt":   dict(name="Cobalt lụa",      kind="neo", mode="white", base=COB,   blobs=[(.25,.85,1.3,.30,DEEP,.8,70),(.85,.25,1.3,.30,PERI,.70,70),(.78,.55,1.6,.04,PERI2,.55,18),(.95,.80,1.0,.2,VIO,.45,60)]),
 "n3-chamtim":  dict(name="Chàm–tím",        kind="neo", mode="white", base=DEEP,  blobs=[(.82,.35,1.4,.32,VIO,.75,70),(.95,.70,1.0,.22,COB,.9,60),(.72,.55,1.5,.045,LAV,.40,20),(.35,.15,1.2,.25,NIGHT,.8,70)]),
 "n4-periwinkle":dict(name="Periwinkle sáng",kind="neo", mode="ink",   base=PERI2, blobs=[(.80,.30,1.3,.32,COB,.55,70),(.90,.65,1.1,.24,PERI,.8,60),(.75,.50,1.5,.04,"#FFFFFF",.65,18),(.10,.20,1.2,.3,"#FFFFFF",.6,80)]),
 "n5-giay-lua": dict(name="Giấy lụa",        kind="neo", mode="ink",   base=PAPER, blobs=[(.80,.30,1.4,.30,PERI,.55,70),(.92,.62,1.1,.22,COB,.35,60),(.70,.50,1.5,.04,"#FFFFFF",.9,18),(.30,.85,1.3,.25,SMOKE,.9,70)]),
 "n6-muc-cobalt":dict(name="Mực → cobalt",   kind="neo", mode="white", base=INK,   blobs=[(.88,.45,1.8,.40,COB,.95,80),(.95,.30,1.2,.18,PERI,.35,60),(.80,.58,1.6,.045,PERI2,.35,20),(.40,.90,1.2,.2,DEEP,.85,70)]),
 "r1-tim-hong": dict(name="Rực · Cobalt–tím–hồng", kind="rực", mode="white", base=DEEP, blobs=[(.55,.85,1.4,.30,COB,.9,70),(.82,.32,1.4,.30,VIO,.85,70),(.96,.52,1.0,.20,MAG,.85,60),(.98,.30,.8,.10,PEACH,.55,45),(.74,.45,1.6,.04,LAV,.5,18)]),
 "r2-lam-tim":  dict(name="Rực · Cobalt–lam–tím",   kind="rực", mode="white", base=COB,  blobs=[(.30,.85,1.3,.30,NIGHT,.75,70),(.82,.25,1.3,.28,AZ,.80,70),(.92,.62,1.1,.24,VIO,.85,60),(.76,.45,1.6,.04,PERI2,.55,18)]),
 "r3-nang":     dict(name="Rực · Cobalt–đào–hổ phách",kind="rực", mode="white", base=COB, blobs=[(.28,.85,1.3,.30,DEEP,.85,70),(.80,.30,1.3,.30,PERI,.7,70),(.97,.60,.9,.22,PEACH,.8,55),(.99,.40,.6,.10,AMB,.7,40),(.76,.48,1.6,.04,PERI2,.5,18)]),
}
def zone(w,h):  # vùng đặt chữ an toàn, tỉ lệ (x0,y0,x1,y1)
    if w/h>=2.5: return (.05,.18,.50,.82)
    if w>h: return (.06,.20,.52,.80)
    return (.08,.56,.92,.92)
def layout(w,h): return "L" if w>h else "P"

FONTS = """@font-face{font-family:Lexend;font-weight:300;src:url(%(f)s/Lexend-300.ttf)}
@font-face{font-family:Lexend;font-weight:400;src:url(%(f)s/Lexend-400.ttf)}
@font-face{font-family:'Be Vietnam Pro';font-weight:400;src:url(%(f)s/BeVietnamPro-400.ttf)}
@font-face{font-family:'Be Vietnam Pro';font-weight:500;src:url(%(f)s/BeVietnamPro-500.ttf)}
@font-face{font-family:'JetBrains Mono';font-weight:400;src:url(%(f)s/JetBrainsMono-400.ttf)}
@font-face{font-family:'JetBrains Mono';font-weight:500;src:url(%(f)s/JetBrainsMono-500.ttf)}""" % dict(f="../../fonts")
NOISE = "data:image/svg+xml;base64," + base64.b64encode(b'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .6 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>').decode()
NOISE_D = NOISE.replace("dmlld","dmlld")  # (giữ nguyên; hạt sáng soft-light + hạt tối bên dưới)
NOISE_DARK = "data:image/svg+xml;base64," + base64.b64encode(b'<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="7" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>').decode()

def bg_layer(key,w,h,grain=None,angle=None):
    """Trả về <div> nền (position:absolute; inset:0) — vệt elip có hướng, mờ, phủ hạt."""
    grain = OPT.grain if grain is None else grain; angle = OPT.angle if angle is None else angle
    b = BG[key]; S=(w*h)**.5; lay=layout(w,h); out=[]
    for (u,v,ln,th,col,op,bl) in b["blobs"]:
        if u>.5: u=.45+.55*u
        if th<.06: ln*=.62; bl*=1.5; op*=.85
        if lay=="L": cx,cy = u*w, v*h
        else: cx,cy = v*w, (1-u)*h
        L,T = ln*S, th*S
        out.append(f'<i style="position:absolute;left:{cx-L/2:.0f}px;top:{cy-T/2:.0f}px;width:{L:.0f}px;height:{T:.0f}px;border-radius:50%;background:{col};opacity:{op};filter:blur({bl*S/1080:.1f}px);transform:rotate({angle}deg)"></i>')
    return (f'<div class="bg" style="position:absolute;inset:0;overflow:hidden;background:{b["base"]}">{"".join(out)}'
            f'<div style="position:absolute;inset:0;background:url({NOISE_DARK});mix-blend-mode:multiply;opacity:{grain*.55:.2f}"></div>'
            f'<div style="position:absolute;inset:0;background:url({NOISE});mix-blend-mode:soft-light;opacity:{grain*1.7:.2f}"></div></div>')

def page(w,h,body,extra_css=""):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:{w}px;height:{h}px;overflow:hidden;background:#fff}}
body{{font-family:'Be Vietnam Pro',sans-serif;position:relative;-webkit-font-smoothing:antialiased}}{extra_css}</style></head><body>{body}</body></html>'''

def render(html_name, out, w, h, scale=1):
    subprocess.run([sys.executable, str(TOOLS/"render.py"), str(SC/html_name), str(out), "--size", f"{w}x{h}", "--scale", str(scale)], check=True, capture_output=True)

# ---------- đo tương phản ----------
def lum(c):
    c=[x/255 for x in c]; c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def ratio(a,b):
    l1,l2=sorted([lum(a),lum(b)],reverse=True); return (l1+.05)/(l2+.05)
def hexc(c): return "#%02X%02X%02X"%tuple(c)
def measure(png, key, w, h):
    im=Image.open(png).convert("RGB"); x0,y0,x1,y1=zone(w,h)
    reg=im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))).resize((120,int(120*(y1-y0)*h/((x1-x0)*w))+1))
    px=sorted(reg.getdata(), key=lum); n=len(px); mode=BG[key]["mode"]
    worst = px[int(n*.995)] if mode=="white" else px[int(n*.005)]   # điểm sáng nhất / tối nhất (p99.5)
    fg = (255,255,255) if mode=="white" else (14,20,66)
    r = ratio(fg,worst)
    # gọi contrast.py để đối chiếu cùng công thức
    t = subprocess.run([sys.executable,str(TOOLS/"contrast.py"),hexc(fg),hexc(worst)],capture_output=True,text=True).stdout.strip()
    return dict(worst=hexc(worst), fg=hexc(fg), ratio=round(r,2), line=t)

# ---------- 1. nền ----------
def build_bg():
    res={}
    for key,b in BG.items():
        res[key]=dict(name=b["name"],kind=b["kind"],mode=b["mode"],sizes={})
        for sz,(w,h) in SIZES.items():
            fn=f"bg-{key}.html".replace(".html",f"_{sz}.html")
            (SC/fn).write_text(page(w,h,bg_layer(key,w,h)))
            out=PNG/f"bg-{key}_{sz}.png"; render(fn,out,w,h)
            res[key]["sizes"][sz]=measure(out,key,w,h)
        print("bg",key,{s:v["ratio"] for s,v in res[key]["sizes"].items()})
    (HERE/"_contrast.json").write_text(json.dumps(res,ensure_ascii=False,indent=1))
    build_gradients_html(res)

def build_gradients_html(res):
    cards=[]
    for key,r in res.items():
        mn=min(v["ratio"] for v in r["sizes"].values())
        cards.append(f'''<div class="card" data-k="{key}" data-mode="{r["mode"]}" data-min="{mn}"><img loading="lazy" src="png/bg-{key}_1920x1080.png"><b>{r["name"]}</b><span>{r["kind"]} · chữ {"trắng" if r["mode"]=="white" else "mực"} · min {mn}:1</span></div>''')
    data=json.dumps({k:{"name":v["name"],"mode":v["mode"],"sizes":{s:{"ratio":x["ratio"],"worst":x["worst"]} for s,x in v["sizes"].items()}} for k,v in res.items()},ensure_ascii=False)
    zones=json.dumps({s:zone(*wh) for s,wh in SIZES.items()})
    html=f'''<!doctype html><html lang="vi"><meta charset="utf-8"><title>Invlogis · Nền gradient lụa</title><style>{FONTS.replace("../../fonts","../fonts")}
*{{box-sizing:border-box;margin:0}}body{{font-family:'Be Vietnam Pro',sans-serif;background:{PAPER};color:{INK};padding:32px;-webkit-font-smoothing:antialiased}}
h1{{font-family:Lexend;font-weight:300;font-size:32px}}p.s{{color:#4A5380;margin:6px 0 22px;font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.card{{cursor:pointer;background:#fff;border:1px solid #D9DEF0;border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:4px}}
.card img{{width:100%;border-radius:8px;display:block}}.card b{{font-weight:500;font-size:14px}}.card span{{font-family:'JetBrains Mono';font-size:11px;color:#4A5380}}
.card.on{{outline:2px solid {COB}}}h2{{font-family:Lexend;font-weight:300;font-size:20px;margin:28px 0 10px}}
.view{{position:relative;max-width:1100px}}.view img{{width:100%;display:block;border-radius:12px}}.zone{{position:absolute;border:1.5px dashed #fff;mix-blend-mode:difference;border-radius:6px}}
.tabs button{{font:500 12px 'JetBrains Mono';border:1px solid #C9D0EE;background:#fff;border-radius:99px;padding:6px 12px;margin:0 6px 8px 0;cursor:pointer}}.tabs button.on{{background:{COB};color:#fff;border-color:{COB}}}
#info{{font:12px 'JetBrains Mono';color:#4A5380;margin-top:8px}}label{{font-size:13px;margin-left:8px}}</style>
<h1>Nền gradient lụa · 9 nền</h1><p class="s">6 neo (cobalt/mực chàm) + 3 rực cho ra mắt. Bấm một nền để xem cỡ lớn, bật khung vùng đặt chữ.</p>
<div class="grid">{"".join(cards)}</div>
<h2 id="t">Chọn một nền</h2><div class="tabs" id="tabs"></div><label><input type="checkbox" id="z" checked> Hiện vùng đặt chữ</label>
<div class="view" id="view"><img id="big"><div class="zone" id="zn"></div></div><div id="info"></div>
<script>const D={data},Z={zones};let k="n1-chamdem",s="1920x1080";
function show(){{const d=D[k],x=d.sizes[s];document.getElementById('t').textContent=d.name;document.getElementById('big').src='png/bg-'+k+'_'+s+'.png';
const [a,b,c,e]=Z[s],z=document.getElementById('zn');z.style.cssText=`left:${{a*100}}%;top:${{b*100}}%;width:${{(c-a)*100}}%;height:${{(e-b)*100}}%;display:${{document.getElementById('z').checked?'block':'none'}}`;
document.getElementById('info').textContent=`file bg-${{k}}_${{s}}.png · chữ ${{d.mode=='white'?'trắng #FFFFFF':'mực #0E1442'}} · điểm xấu nhất trong vùng ${{x.worst}} → ${{x.ratio}}:1`;
document.querySelectorAll('.card').forEach(c=>c.classList.toggle('on',c.dataset.k==k));document.querySelectorAll('#tabs button').forEach(c=>c.classList.toggle('on',c.textContent==s))}}
document.getElementById('tabs').innerHTML=Object.keys(Z).map(q=>`<button>${{q}}</button>`).join('');
document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>{{s=b.textContent;show()}});
document.querySelectorAll('.card').forEach(c=>c.onclick=()=>{{k=c.dataset.k;show();scrollTo(0,document.getElementById('t').offsetTop)}});
document.getElementById('z').onchange=show;show()</script></html>'''
    (HERE/"gradients.html").write_text(html)

# ---------- 2. hoạ tiết chứng từ ----------
CARD_CSS = f"""
.doc{{position:absolute;width:380px;height:480px;background:linear-gradient(160deg,#FFFFFF,#F1F3FC);border:1px solid rgba(255,255,255,.75);border-radius:16px;padding:26px 26px;box-shadow:0 30px 60px -20px rgba(11,16,51,.55),0 0 0 6px rgba(255,255,255,.12);color:{INK};overflow:hidden}}
.doc .tag{{display:inline-block;font:500 12px 'JetBrains Mono';letter-spacing:.04em;border:1px solid #C3CAEA;border-radius:99px;padding:4px 11px;color:{COB};background:#fff}}
.doc .no{{font:400 11px 'JetBrains Mono';color:#6A729C;float:right;margin-top:6px}}
.doc .f{{margin-top:15px;position:relative}}.doc .f small{{display:block;font:400 10.5px 'JetBrains Mono';color:#7C84AC;letter-spacing:.06em;text-transform:uppercase}}
.doc .f em{{font-style:normal;display:inline-block;font:500 16px 'Be Vietnam Pro';padding:2px 6px;margin:2px -6px 0;border-radius:6px;transition:none}}
.doc .f.on em{{background:linear-gradient(90deg,rgba(47,67,219,.16),rgba(151,166,255,.28));box-shadow:inset 0 0 0 1px rgba(47,67,219,.35);color:{INK}}}
.doc .f.on::after{{content:attr(data-t);position:absolute;right:0;top:12px;font:400 10.5px 'JetBrains Mono';color:{COB};background:#fff;border:1px solid #C3CAEA;border-radius:99px;padding:2px 8px}}
.doc .ln{{height:7px;border-radius:4px;background:#E3E7F6;margin-top:10px}}
.doc .scan{{position:absolute;left:0;right:0;height:110px;background:linear-gradient(180deg,rgba(151,166,255,0),rgba(151,166,255,.35) 70%,rgba(47,67,219,.55) 98%,rgba(255,255,255,.9) 100%);border-bottom:1.5px solid #fff;filter:drop-shadow(0 6px 10px rgba(47,67,219,.4))}}
.doc .row{{display:flex;gap:16px}}.doc .row>*{{flex:1}}
.doc .stat{{position:absolute;left:26px;right:26px;bottom:22px;font:400 11px 'JetBrains Mono';color:{COB};display:flex;justify-content:space-between;border-top:1px solid #DDE2F4;padding-top:10px}}
"""
def F(label,val,on=False,t=""): return f'<div class="f{" on" if on else ""}" data-t="{t}"><small>{label}</small><em>{val}</em></div>'
def qr(n=15,seed=3):
    import random; r=random.Random(seed); cells=[]
    for i in range(n):
        for j in range(n):
            fin=(i<4 and j<4) or (i<4 and j>=n-4) or (i>=n-4 and j<4)
            on = (fin and (i in(0,3) or j in (0,3) or (i in (1,2) and j in (1,2)) or (i in(1,2) and j in(n-3,n-2)) or (i in (n-3,n-2) and j in (1,2)) or i in (n-4,n-1) or j in (n-4,n-1) or ((n-3<=i<=n-2) and 1<=j<=2) and False)) if fin else r.random()<.48
            if on: cells.append(f'<rect x="{j*10}" y="{i*10}" width="9" height="9" rx="1.5"/>')
    return f'<svg viewBox="0 0 {n*10} {n*10}" width="118" height="118" fill="{INK}">{"".join(cells)}</svg>'
def card(kind,x,y,rot=0,z=1,scan=None,lit=(),scale=1):
    sty=f'left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({scale});z-index:{z}'
    L=lambda i:i in lit
    if kind=="booking":
        body=f'<span class="tag">[Booking Note]</span><span class="no">BN-0412</span>'+F("Số booking","SGN2610-48213",L(0),"[ma_booking]")+F("Hãng tàu","Cảng đi · Cát Lái",L(1),"[cang]")+'<div class="row">'+F("Loại cont","40’HC × 2",L(2),"[loai]")+F("Hạn cut-off","20/11 · 17:00",L(3),"[han]")+'</div>'+'<div class="ln" style="width:92%;margin-top:26px"></div><div class="ln" style="width:70%"></div><div class="ln" style="width:81%"></div>'
        st="Booking · 4 trường"
    elif kind=="edo":
        body=f'<span class="tag">[eDO]</span><span class="no">DO-7305</span>'+F("Số vận đơn","HDMU 7305 2214",L(0),"[van_don]")+F("Cảng dỡ","Cát Lái, TP.HCM",L(1),"[cang_do]")+F("Hạn lấy container","20/11/2026",L(2),"[han_lay]")+'<div style="margin-top:22px;border:1.5px dashed #AEB7E6;border-radius:10px;height:70px;display:flex;align-items:center;justify-content:center;font:400 11px \'JetBrains Mono\';color:#7C84AC;letter-spacing:.12em">PHÊ DUYỆT HÃNG TÀU</div><div class="ln" style="width:60%;margin-top:18px"></div>'
        st="eDO · 3 trường"
    elif kind=="eir":
        sq="".join(f'<i style="width:34px;height:34px;border:1.2px solid #AEB7E6;border-radius:6px;{"background:linear-gradient(135deg,#97A6FF,#2F43DB);border-color:#2F43DB" if (n in (1,4,6)) else ""}"></i>' for n in range(8))
        body=f'<span class="tag">[EIR]</span><span class="no">EIR-2291</span>'+F("Số cont","TCLU 8841 073",L(0),"[so_cont]")+F("Số seal","VN-0057421",L(1),"[seal]")+f'<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:22px">{sq}</div><small style="display:block;margin-top:10px;font:400 10.5px \'JetBrains Mono\';color:#7C84AC;letter-spacing:.06em">TÌNH TRẠNG VỎ CONT</small><div class="ln" style="width:75%"></div>'
        st="EIR · 2 trường"
    elif kind=="can":
        body=f'<span class="tag">[Phiếu cân]</span><span class="no">VGM-0933</span>'+'<div style="margin-top:14px;font:300 54px Lexend;letter-spacing:-.02em;line-height:1">'+('<span style="background:linear-gradient(90deg,rgba(47,67,219,.16),rgba(151,166,255,.28));border-radius:8px;padding:0 6px;margin:0 -6px">'+'27.480'+'</span>' if L(0) else '27.480')+'<span style="font:400 16px \'JetBrains Mono\';color:#7C84AC"> kg</span></div>'+'<small style="font:400 10.5px \'JetBrains Mono\';color:#7C84AC;letter-spacing:.06em;margin-top:2px;display:block">TỔNG TRỌNG LƯỢNG (VGM)</small>'+'<div class="row">'+F("Tare","3.870",L(1),"[tare]")+F("Hàng","23.610",L(1),"[net]")+'</div>'+'<div class="ln" style="width:88%;margin-top:28px"></div><div class="ln" style="width:64%"></div>'
        st="Phiếu cân · 3 trường"
    else:
        body=f'<span class="tag">[Tờ khai]</span><span class="no">TK-10551</span>'+'<div style="display:flex;gap:18px;margin-top:6px;align-items:center"><div style="flex:1">'+F("Số tờ khai","10551 66420",L(0),"[so_tk]")+'</div><div style="'+('box-shadow:0 0 0 3px rgba(47,67,219,.25);' if L(1) else '')+'padding:6px;border:1px solid #D1D7F0;border-radius:10px;background:#fff">'+qr()+'</div></div>'+F("Mã HS","8708.29.90",L(2),"[ma_hs]")+F("Luồng","Xanh · thông quan",L(2),"[luong]")+'<div class="ln" style="width:80%;margin-top:22px"></div>'
        st="Tờ khai · QR đã đọc"
    sc=f'<div class="scan" style="top:{scan}px"></div>' if scan is not None else ""
    return f'<div class="doc" style="{sty}">{body}{sc}<div class="stat"><span>{st}</span><span>{"đã đọc" if lit else "chờ đọc"}</span></div></div>'

def doc_sheet():
    # tờ giấy nền Giấy ấm: 5 thẻ, mỗi thẻ 1 trạng thái (chờ đọc → AI đọc → đã đọc)
    cs=[("booking",40,60,0,1,None,()),("edo",470,60,0,1,200,(0,)),("eir",900,60,0,1,330,(0,1)),("can",1330,60,0,1,None,(0,1)),("edo",40,640,0,1,None,(0,1,2))]
    cards="".join(card(k,x,y,r,z,s,l) for k,x,y,r,z,s,l in cs)
    cards+=card("tokhai",470,640,0,1,None,(0,1,2))
    cards+=card("booking",900,640,0,1,None,(0,1,2,3))
    cards+=f'<div style="position:absolute;left:1330px;top:640px;width:380px;height:480px;border:1.5px dashed #AEB7E6;border-radius:16px;display:flex;align-items:center;justify-content:center;font:400 12px \'JetBrains Mono\';color:#7C84AC;text-align:center;padding:30px;line-height:1.7">3 trạng thái:<br>chờ đọc · vệt quét · trường sáng + nhãn [..]</div>'
    return page(1760,1200,f'<div style="position:absolute;inset:0;background:{PAPER}"></div><div style="position:absolute;left:40px;top:14px;font:300 26px Lexend;color:{INK}">Hoạ tiết chứng từ · 5 thẻ + hiệu ứng AI đọc</div>{cards}',CARD_CSS)
def doc_hero(key,w,h,name):
    lay=layout(w,h)
    if lay=="L":
        cards=card("booking",980,200,-7,1,None,(),1.1)+card("edo",1270,130,3,3,260,(0,),1.1)+card("eir",1480,330,8,2,None,(0,1),1.0)+card("tokhai",1100,540,-3,4,None,(0,1,2),1.0)
    else:
        cards=card("can",40,100,-8,2,None,(0,1),1.0)+card("edo",350,140,5,3,240,(0,),1.12)+card("booking",640,70,10,1,None,(),1.0)
    return page(w,h,bg_layer(key,w,h)+cards,CARD_CSS)

def build_doc():
    (SC/"doc-motifs.html").write_text(doc_sheet()); (HERE/"doc-motifs.html").write_text(doc_sheet().replace("../../fonts","../fonts"))
    render("doc-motifs.html",HERE/"doc-motifs.png",1760,1200)
    for key,w,h,nm in [("r1-tim-hong",1920,1080,"doc-hero-r1_1920x1080"),("n3-chamtim",1920,1080,"doc-hero-n3_1920x1080"),("r2-lam-tim",1080,1350,"doc-hero-r2_1080x1350")]:
        (SC/f"{nm}.html").write_text(doc_hero(key,w,h,nm)); render(f"{nm}.html",PNG/f"{nm}.png",w,h)
    print("doc done")

# ---------- 3. khung thiết bị ----------
DEV_CSS = f"""
.phone{{position:absolute;border-radius:62px;background:linear-gradient(145deg,#2A2F55,#0B1033 40%,#1B2160);padding:11px;box-shadow:0 50px 90px -30px rgba(5,8,30,.7),inset 0 0 0 1.5px rgba(255,255,255,.22),0 0 0 1px rgba(255,255,255,.08)}}
.phone .scr{{position:relative;width:100%;height:100%;border-radius:52px;overflow:hidden;background-size:cover;background-position:top center;background-color:{PAPER}}}
.phone .isl{{position:absolute;top:14px;left:50%;width:30%;height:3.1%;background:#05081F;border-radius:99px;transform:translateX(-50%);z-index:5}}
.lap{{position:absolute}}.lap .lid{{border-radius:22px 22px 6px 6px;background:linear-gradient(160deg,#2A2F55,#0B1033 50%,#1B2160);padding:16px 16px 18px;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.2),0 40px 80px -30px rgba(5,8,30,.65)}}
.lap .scr{{width:100%;height:100%;border-radius:8px;overflow:hidden;background-size:cover;background-position:top left;background-color:{PAPER};position:relative}}
.lap .cam{{position:absolute;top:6px;left:50%;width:6px;height:6px;border-radius:50%;background:#05081F;transform:translateX(-50%)}}
.lap .base{{height:16px;margin:0 -5%;border-radius:2px 2px 22px 22px;background:linear-gradient(180deg,#C9CFEA,#8F98C4);position:relative;box-shadow:0 22px 30px -12px rgba(5,8,30,.5)}}
.lap .base::after{{content:"";position:absolute;left:50%;top:0;width:16%;height:6px;background:rgba(14,20,66,.28);border-radius:0 0 8px 8px;transform:translateX(-50%)}}
.ui{{position:absolute;inset:0;padding:6% 6%;font-family:'Be Vietnam Pro';color:{INK};background:{PAPER}}}
.ui .hd{{font:300 1.7em Lexend;margin-top:8%}}.ui .ch{{display:inline-block;font:500 .62em 'JetBrains Mono';border:1px solid #C3CAEA;border-radius:99px;padding:.3em .8em;color:{COB};background:#fff;margin:.8em 0 .4em}}
.ui .c{{background:#fff;border:1px solid #DDE2F4;border-radius:1.2em;padding:.9em 1em;margin-top:.7em;font-size:.8em}}.ui .c small{{display:block;font:400 .72em 'JetBrains Mono';color:#7C84AC;letter-spacing:.06em}}
.ui .c b{{font-weight:500}}.ui .on{{background:linear-gradient(90deg,rgba(47,67,219,.14),rgba(151,166,255,.26));border-color:rgba(47,67,219,.35)}}
.ui .btn{{margin-top:1em;background:{COB};color:#fff;border-radius:99px;text-align:center;padding:.75em;font:500 .8em 'Be Vietnam Pro'}}
.ui .slot{{position:absolute;left:6%;right:6%;bottom:5%;font:400 .6em 'JetBrains Mono';color:#7C84AC;text-align:center;border-top:1px dashed #C3CAEA;padding-top:.8em}}
"""
def ui_phone(fs):
    return f'<div class="ui" style="font-size:{fs}px"><div class="hd">Hồ sơ lô hàng</div><span class="ch">[eDO] đã đọc · 4 trường</span><div class="c on"><small>SỐ VẬN ĐƠN</small><b>HDMU 7305 2214</b></div><div class="c on"><small>CẢNG DỠ</small><b>Cát Lái, TP.HCM</b></div><div class="c"><small>HẠN LẤY CONTAINER</small><b>20/11/2026</b></div><div class="btn">Duyệt hồ sơ</div><div class="slot">KHE THAY ẢNH MÀN HÌNH · .scr</div></div>'
def ui_lap(fs):
    return f'<div class="ui" style="font-size:{fs}px;padding:3% 4%"><div style="display:flex;gap:4%"><div style="flex:1.1"><div class="hd" style="margin-top:2%">Lô hàng · SGN2610-48213</div><span class="ch">[AI đọc] 3 chứng từ</span><div class="c on"><small>SỐ VẬN ĐƠN</small><b>HDMU 7305 2214</b></div><div class="c on"><small>SỐ CONT / SEAL</small><b>TCLU 8841 073 · VN-0057421</b></div><div class="c"><small>HẠN LẤY CONTAINER</small><b>20/11/2026</b></div></div><div style="flex:.9;padding-top:3%"><div class="c" style="margin-top:3.2em"><small>CHỨNG TỪ</small><b>Booking Note · eDO · EIR</b></div><div class="c"><small>TRẠNG THÁI</small><b>Chờ duyệt</b></div><div class="btn">Duyệt hồ sơ</div></div></div></div>'
def phone(x,y,w,h,rot=0,z=1,fs=17):
    return f'<div class="phone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{w*.15:.0f}px;padding:{max(5,w*.026):.0f}px;transform:rotate({rot}deg);z-index:{z}"><div class="scr" id="screen-phone" style="border-radius:{w*.125:.0f}px"><div class="isl"></div>{ui_phone(fs)}</div></div>'
def laptop(x,y,w,z=1,fs=15):
    sh=(w-32)*10/16
    return f'<div class="lap" style="left:{x}px;top:{y}px;width:{w}px;z-index:{z}"><div class="lid" style="position:relative"><div class="cam"></div><div class="scr" id="screen-laptop" style="height:{sh:.0f}px">{ui_lap(fs)}</div></div><div class="base"></div></div>'
def dev_scene(key,w,h,kind):
    if kind=="combo": body=laptop(120,190,1160,1,16)+phone(1170,260,360,740,3,2,17)
    elif kind=="phone": body=phone(w//2-310,130,420,880,-4,2,19)+phone(w//2+80,250,420,880,5,1,19)
    else: body=laptop(700,50,640,1,11)+phone(1270,150,190,340,4,2,8)
    return page(w,h,bg_layer(key,w,h)+body,DEV_CSS)
def build_dev():
    scenes=[("n2-cobalt",1920,1080,"combo","device-combo_1920x1080"),("r1-tim-hong",1080,1350,"phone","device-phones_1080x1350"),("n5-giay-lua",1500,500,"lap","device-laptop_1500x500")]
    for key,w,h,kind,nm in scenes:
        (SC/f"{nm}.html").write_text(dev_scene(key,w,h,kind)); render(f"{nm}.html",PNG/f"{nm}.png",w,h)
    # trang xem
    items="".join(f'<figure><img src="png/{n}.png"><figcaption>{n}.png</figcaption></figure>' for _,_,_,_,n in scenes)
    (HERE/"device-frames.html").write_text(f'''<!doctype html><html lang="vi"><meta charset="utf-8"><title>Invlogis · Khung thiết bị</title><style>{FONTS.replace("../../fonts","../fonts")}{DEV_CSS}
body{{margin:0;padding:32px;background:{PAPER};font-family:'Be Vietnam Pro';color:{INK}}}h1{{font:300 30px Lexend}}p{{color:#4A5380;font-size:14px;max-width:760px;line-height:1.6}}
figure{{margin:18px 0}}figure img{{max-width:100%;width:900px;border-radius:12px;display:block}}figcaption{{font:12px 'JetBrains Mono';color:#4A5380;margin-top:6px}}
.live{{position:relative;width:900px;height:480px;overflow:hidden;border-radius:12px;margin:18px 0}}.live .in{{position:absolute;left:0;top:0;width:1920px;height:1080px;transform:scale(.46875);transform-origin:0 0}}</style>
<h1>Khung thiết bị · điện thoại + laptop (CSS thuần)</h1><p>Thay màn hình: đặt <code>style="background-image:url(anh.png)"</code> cho phần tử <code>.scr</code> rồi xoá khối <code>.ui</code> bên trong. Bản dưới là trang sống (bấm chọn chữ được); PNG là bản xuất.</p>
<div class="live"><div class="in">{bg_layer("n2-cobalt",1920,1080)}{laptop(120,190,1160,1,16)}{phone(1170,260,360,740,3,2,17)}</div></div>{items}</html>''')
    # PNG tổng của trang xem
    (SC/"device-frames.html").write_text((HERE/"device-frames.html").read_text().replace("../fonts","../../fonts").replace('src="png/','src="../png/'))
    render("device-frames.html",HERE/"device-frames.png",1000,1900)
    print("dev done")

# ---------- 4. sheet ----------
def build_sheet():
    th=lambda f,s="": f'<img src="../png/{f}" style="width:100%;display:block;border-radius:8px;{s}">'
    bgs=list(BG.keys()); cells="".join(f'<div>{th(f"bg-{k}_1920x1080.png")}<p>{BG[k]["name"]}</p></div>' for k in bgs)
    html=page(1600,2000,f'''<div style="padding:44px 48px;background:{PAPER};height:100%">
<div style="font:300 40px Lexend">Invlogis · Bộ hình nền & hoạ tiết (hướng A · Lụa)</div>
<div style="font:400 14px 'JetBrains Mono';color:#4A5380;margin:6px 0 22px">9 nền gradient · hoạ tiết chứng từ + AI đọc · khung thiết bị · 5 cỡ xuất</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px 16px">{cells}</div>
<div style="font:300 22px Lexend;margin:26px 0 10px">Chứng từ · AI đọc · thiết bị</div>
<div style="display:flex;gap:16px;align-items:flex-start;height:400px"><img src="../png/doc-hero-r1_1920x1080.png" style="height:400px;border-radius:8px"><img src="../png/doc-hero-r2_1080x1350.png" style="height:400px;border-radius:8px"><img src="../png/device-phones_1080x1350.png" style="height:400px;border-radius:8px"></div>
<div style="display:flex;gap:16px;align-items:flex-start;height:420px;margin-top:16px"><img src="../png/device-combo_1920x1080.png" style="height:400px;border-radius:8px"><img src="../png/device-laptop_1500x500.png" style="width:440px;border-radius:8px"></div></div></div>''',
    "p{font:400 12px 'JetBrains Mono';color:#4A5380;margin-top:6px}")
    (SC/"visuals-sheet.html").write_text(html); render("visuals-sheet.html",HERE/"visuals-sheet.png",1600,2000)
    print("sheet done")

if __name__=="__main__":
    o=OPT.only
    if not o or o=="bg": build_bg()
    if not o or o=="doc": build_doc()
    if not o or o=="dev": build_dev()
    if not o or o=="sheet": build_sheet()
