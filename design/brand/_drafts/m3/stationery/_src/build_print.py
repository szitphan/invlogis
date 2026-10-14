import subprocess, pathlib, shutil
R="python3 ../../_tools/render.py"
root=pathlib.Path(__file__).resolve().parent.parent
def render(src,out,size=None,scale=1):
    cmd=["python3",str(root/"../../_tools/render.py"),str(src),str(out)]
    if size: cmd+=["--size",size,"--scale",str(scale)]
    subprocess.run(cmd,check=True,capture_output=True)

FONTS="""
@font-face{font-family:Lexend;font-weight:300;src:url(%(p)sassets/fonts/Lexend-300.ttf)}
@font-face{font-family:Lexend;font-weight:400;src:url(%(p)sassets/fonts/Lexend-400.ttf)}
@font-face{font-family:Lexend;font-weight:600;src:url(%(p)sassets/fonts/Lexend-600.ttf)}
@font-face{font-family:BVP;font-weight:300;src:url(%(p)sassets/fonts/BeVietnamPro-300.ttf)}
@font-face{font-family:BVP;font-weight:400;src:url(%(p)sassets/fonts/BeVietnamPro-400.ttf)}
@font-face{font-family:BVP;font-weight:500;src:url(%(p)sassets/fonts/BeVietnamPro-500.ttf)}
@font-face{font-family:BVP;font-weight:600;src:url(%(p)sassets/fonts/BeVietnamPro-600.ttf)}
"""
PH="background:#FFD3C0;color:#0E1442;padding:0 1px"

# ---------------- business card ----------------
def card_html(mode, p="../"):
    # mode: print (page 112x77 with marks) | preview (trim only 90x55)
    f=FONTS%{"p":p}
    front=f'''<div class="face front">
      <img class="lk" src="{p}assets/logo/invlogis-by-innvie-reverse.png">
      <div class="tag">Khai mở cách vận hành mới.</div>
    </div>'''
    back=f'''<div class="face back">
      <div class="who"><div class="nm"><span class="ph">[chờ: Họ và tên]</span></div>
        <div class="ti"><span class="ph">[chờ: Chức danh]</span></div></div>
      <div class="ct">
        <div><b>T</b><span class="ph">[chờ: số điện thoại]</span></div>
        <div><b>E</b><span class="ph">[chờ: email]</span></div>
        <div><b>W</b><span class="ph">[chờ: domain]</span></div>
        <div class="ad"><span class="ph">[chờ: địa chỉ]</span></div>
      </div>
      <div class="strip"></div>
    </div>'''
    css=f'''{f}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#fff;font-family:BVP,Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.ph{{background:#FFD3C0;color:#0E1442}}
.face{{position:relative;width:96mm;height:61mm;overflow:hidden}}
.front{{background:#0B1033 url({p}assets/bg/bg-n1-chamdem_1920x1080.jpg) center/cover}}
.front .lk{{position:absolute;left:10mm;top:17mm;width:41mm}}   /* trim x=7 mm, cao ~15 mm > 12 mm */
.front .tag{{position:absolute;left:10mm;bottom:9mm;color:#fff;font:300 7pt Lexend,Arial,sans-serif;letter-spacing:.02em}}
.back{{background:#FAF8F4;color:#0E1442}}
.back .who{{position:absolute;left:10mm;top:10mm}}
.back .nm{{font:400 11pt Lexend,Arial,sans-serif;line-height:1.2}}
.back .ti{{font:400 7pt BVP,Arial,sans-serif;color:#4A5380;margin-top:1mm}}
.back .ct{{position:absolute;left:10mm;top:27mm;font:400 7pt/1.55 BVP,Arial,sans-serif}}
.back .ct b{{display:inline-block;width:4mm;font:600 7pt BVP;color:#2F43DB}}
.back .ct .ad{{margin-left:4mm;color:#4A5380}}
.back .strip{{position:absolute;left:0;right:0;bottom:0;height:4.2mm;background:linear-gradient(115deg,#0E1442 0%,#2F43DB 55%,#7B55FF 100%)}}
.mark{{position:absolute;background:#000}}
@page{{margin:0;size:{'112mm 77mm' if mode=='print' else '90mm 55mm'}}}
.pg{{position:relative;page-break-after:always;overflow:hidden;width:{'112mm' if mode=='print' else '90mm'};height:{'77mm' if mode=='print' else '55mm'}}}
.pg .face{{position:absolute;left:{'8mm' if mode=='print' else '-3mm'};top:{'8mm' if mode=='print' else '-3mm'}}}
'''
    marks=''
    if mode=='print':
        xs=[11,101]; ys=[11,66]
        for y in ys:
            for x0 in (2,105): marks+=f'<div class="mark" style="left:{x0}mm;top:{y}mm;width:5mm;height:.1mm"></div>'
        for x in xs:
            for y0 in (2,70): marks+=f'<div class="mark" style="left:{x}mm;top:{y0}mm;width:.1mm;height:5mm"></div>'
    return f'<!doctype html><meta charset=utf-8><style>{css}</style><div class="pg">{front}{marks}</div><div class="pg">{back}{marks}</div>'

d=root/"business-card"
(d/"card.print.html").write_text(card_html("print"),encoding="utf-8")
(d/"card.preview.html").write_text(card_html("preview"),encoding="utf-8")
render(d/"card.print.html",d/"business-card-print.pdf")
# previews: render each page separately (two html with one face)
for side in ("front","back"):
    h=card_html("preview")
    parts=h.split('<div class="pg">')
    one=parts[0]+'<div class="pg">'+(parts[1] if side=="front" else parts[2])
    (d/f"_{side}.html").write_text(one,encoding="utf-8")
    render(d/f"_{side}.html",d/f"business-card-{side}.png","340x208",3)
    (d/f"_{side}.html").unlink()
