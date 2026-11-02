#!/usr/bin/env python3
"""Dựng bộ logo Delta: python3 build.py (chạy trong _src, cần Google Chrome). Theo DEC-325."""
import base64,os,pathlib,subprocess,tempfile
import lib,geom as g
from lib import *
from PIL import Image
OUT=pathlib.Path(__file__).resolve().parents[1]
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
def w(n,s):(OUT/n).write_text(s+"\n")
w("delta-primary.svg",wordmark_svg());w("delta-reverse.svg",wordmark_svg("reverse"))
w("delta-mono-black.svg",wordmark_svg("black"));w("delta-mono-white.svg",wordmark_svg("white"))
w("delta-small.svg",wordmark_svg(kind="none"));w("delta-small-reverse.svg",wordmark_svg("reverse",kind="none"))
w("delta-original.svg",wordmark_svg(kind="orig"))
w("delta-symbol.svg",symbol_svg("d"));w("delta-symbol-reverse.svg",symbol_svg("d","reverse"));w("delta-symbol-mono.svg",symbol_svg("d","black"))
w("delta-stacked.svg",stacked_svg("d"));w("delta-stacked-reverse.svg",stacked_svg("d","reverse"))
BAR='<rect x="10" y="13.5" width="11" height="5" fill="%s"/>'%GREEN
w("favicon.svg",f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><style>.f{{fill:{INK}}}@media (prefers-color-scheme:dark){{.f{{fill:#fff}}}}</style><path class="f" fill-rule="evenodd" d="{FAV_D}"/>{BAR}</svg>')
def png(svgtxt,name,px):
    h=f'<html><body style="margin:0;background:transparent">{svgtxt.replace("<svg ",f"<svg style=display:block width={px} height={px} ",1)}</body></html>'
    with tempfile.NamedTemporaryFile("w",suffix=".html",delete=False) as t:t.write(h)
    p=str(OUT/name);subprocess.run([CH,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1",f"--window-size={max(px,500)},{px+200}","--default-background-color=00000000",f"--screenshot={p}","file://"+t.name],check=True,capture_output=True)
    Image.open(p).crop((0,0,px,px)).save(p);os.unlink(t.name)
# favicon PNG không đổi theo tab được: đặt trên ô trắng để đọc ra ở cả tab sáng lẫn tab tối
FP=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#fff"/><g transform="translate(2.4 2.4) scale(.85)"><path fill="{INK}" fill-rule="evenodd" d="{FAV_D}"/>{BAR}</g></svg>'
for z in(16,32,48):png(FP,f"favicon-{z}.png",z)
ICON=app_icon("d","white")
png(ICON,"app-icon-1024.png",1024);png(ICON,"apple-touch-icon-180.png",180)
png(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432">{sym_inner_scaled("d",INK,GREEN,216,216,216)}</svg>',"android-foreground-432.png",432)
png('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432"><rect width="432" height="432" fill="#fff"/></svg>',"android-background-432.png",432)
# trang tổng hợp
def b64(p):return "data:image/png;base64,"+base64.b64encode((OUT/p).read_bytes()).decode()
def im(n,h):return f'<img src="data:image/svg+xml;base64,{base64.b64encode((OUT/n).read_bytes()).decode()}" style="height:{h}px;display:block">'
def c(body,cap,bg="#fff",col="#64748B",sp=1):return f'<div class=c style="background:{bg};color:{col};grid-column:span {sp}"><div class=s>{body}</div><span>{cap}</span></div>'
D="#191919";Wt="#CBD5E1"
ico=f'<div style="display:flex;gap:14px;align-items:center"><img src="{b64("app-icon-1024.png")}" style="width:96px;border-radius:22%;box-shadow:0 0 0 1px #E2E8F0"><img src="{b64("apple-touch-icon-180.png")}" style="width:60px;border-radius:22%;box-shadow:0 0 0 1px #E2E8F0"></div>'
adp=f'<div style="position:relative;width:96px;height:96px;border-radius:50%;overflow:hidden;box-shadow:0 0 0 1px #E2E8F0"><img src="{b64("android-background-432.png")}" style="position:absolute;width:96px"><img src="{b64("android-foreground-432.png")}" style="position:absolute;width:96px"></div>'
fav="".join(f'<img src="{b64(f"favicon-{z}.png")}" style="width:{z}px">' for z in(16,32,48))
html=f"""<html><body style="margin:0;background:#F6F6F4;font:13px Inter,Arial;width:1600px"><style>.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:0 56px 16px}}.c{{border-radius:14px;padding:18px;box-shadow:inset 0 0 0 1px #E5E7EB;display:flex;flex-direction:column;gap:12px}}.s{{min-height:130px;display:flex;align-items:center;justify-content:center;gap:14px}}h1{{font:600 34px Arial;margin:0 56px 4px;padding-top:44px}}p{{margin:0 56px 22px;color:#475569;font-size:15px}}</style>
<h1>Bộ logo Delta</h1><p>Vẽ lại vector từ logo khách · chữ {INK} · thanh xanh {GREEN} · DEC-325</p><div class=g>
{c(im("delta-primary.svg",84),"delta-primary",sp=2)}{c(im("delta-reverse.svg",84),"delta-reverse",D,Wt,2)}
{c(im("delta-mono-black.svg",52),"delta-mono-black",sp=2)}{c(im("delta-mono-white.svg",52),"delta-mono-white",TILE,"#E5F3EB",2)}
{c(im("delta-symbol.svg",84),"delta-symbol")}{c(im("delta-symbol-reverse.svg",84),"delta-symbol-reverse",D,Wt)}{c(im("delta-symbol-mono.svg",84),"delta-symbol-mono")}{c(fav,"favicon 16, 32, 48 (PNG trên ô trắng)",D,Wt)}
{c(im("delta-stacked.svg",170),"delta-stacked",sp=2)}{c(im("delta-stacked-reverse.svg",170),"delta-stacked-reverse",D,Wt,2)}
{c(im("delta-small.svg",28),"delta-small · dưới 20px, không ®")}{c(im("delta-small-reverse.svg",28),"delta-small-reverse",D,Wt)}{c(im("delta-original.svg",84),"delta-original · ® to như gốc, in ấn",sp=2)}
{c(ico,"app-icon-1024, apple-touch-icon-180 · nền trắng",sp=2)}{c(adp,"android-foreground + background 432",sp=2)}
{c('<div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap">'+"".join(im("delta-primary.svg",z) for z in(40,32,24,20))+im("delta-small.svg",16)+'</div>',"Cỡ thật: 40, 32, 24, 20 (delta-primary) · 16 (delta-small)",sp=4)}
</div></body></html>"""
with tempfile.NamedTemporaryFile("w",suffix=".html",delete=False) as t:t.write(html)
p=str(OUT/"logo-sheet.png");subprocess.run([CH,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1","--window-size=1600,1640",f"--screenshot={p}","file://"+t.name],check=True,capture_output=True)
os.unlink(t.name)
