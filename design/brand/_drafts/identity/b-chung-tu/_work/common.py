import base64, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build
from build import ROOT, FONTS, symbol, svg, lockup, innvie, sheet_path, INK, MUTE

def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
def fonts_css():
    out=""
    for w in (400,500,600):
        out+=f"@font-face{{font-family:'Manrope';font-weight:{w};src:url(data:font/ttf;base64,{b64(FONTS/f'Manrope-{w}.ttf')}) format('truetype')}}\n"
    out+=f"@font-face{{font-family:'JetBrains Mono';font-weight:500;src:url(data:font/ttf;base64,{b64(FONTS/'JetBrainsMono-500.ttf')}) format('truetype')}}\n"
    return out

def inline(svgtxt, style=""):
    t = re.sub(r'\s(width|height)="[^"]+"', '', svgtxt, count=2)
    return t.replace("<svg ", f'<svg style="{style}" ', 1)

def sym_inline(p, mode="color", small=False, style="width:100%;height:100%"):
    d,b = symbol(p, mode, small); return inline(svg(64,64,b,d), style)

NOISE = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .9 0'/></filter>"
         "<rect width='300' height='300' filter='url(%23n)'/></svg>")

CSS = """
:root{--ink:#12163F;--ink2:#0B0E2B;--cobalt:#3B4EF2;--violet:#5B47F5;--mist:#9AA8CC;--paper:#F7F6F2;--white:#fff;--fog:#ECEEF6;--line:#D5D9EA;--mute:#5B6190}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Manrope',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;overflow:hidden}
.mono{font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.02em}
.abs{position:absolute}
.silk{position:absolute;overflow:hidden;isolation:isolate}
.silk .b{position:absolute;border-radius:50%;filter:blur(var(--bl,46px))}
.silk .grain{position:absolute;inset:0;background:url("NOISE");opacity:.32;mix-blend-mode:soft-light;z-index:5;pointer-events:none}
.chip{display:inline-flex;align-items:center;font-family:'JetBrains Mono',monospace;font-weight:500;letter-spacing:.02em;border:1px solid rgba(18,22,63,.28);border-radius:999px;color:var(--ink);background:rgba(255,255,255,.7)}
.chip.glass{background:rgba(255,255,255,.2);border-color:rgba(255,255,255,.55);color:#fff;backdrop-filter:blur(14px)}
.doc{position:absolute;filter:drop-shadow(0 22px 40px rgba(18,22,63,.28)) drop-shadow(0 2px 6px rgba(18,22,63,.12))}
.doc>svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.doc .in{position:absolute;inset:0}
.doc .row{display:flex;justify-content:space-between;align-items:baseline}
.doc .k{font-family:'JetBrains Mono',monospace;font-weight:500;color:var(--mute);text-transform:uppercase;letter-spacing:.04em}
.doc .v{font-weight:500;color:var(--ink)}
.doc .hit .v{color:var(--cobalt)}
.doc .hit{position:relative}
.doc .hit:before{content:"";position:absolute;left:-6px;right:-6px;top:-4px;bottom:-4px;border:1px solid rgba(59,78,242,.55);border-radius:5px;background:rgba(59,78,242,.07)}
.beam{position:absolute;pointer-events:none;transform-origin:center;z-index:4}
"""
def css(): return CSS.replace("NOISE", NOISE)

def silk(x,y,w,h,radius=0,theme="vivid",extra="",inner=""):
    """Nền lụa: các vệt mờ có hướng (cùng góc -38° với vệt quét) + hạt nhiễu."""
    if theme=="vivid":
        base="linear-gradient(140deg,#0E1250 0%,#2A3CD8 45%,#3B4EF2 100%)"
        bl=[("#8B5CF6",.95,.10,.55,.30,-38),("#F062B4",.85,.45,.50,.22,-38),("#FF8F63",.9,.70,.46,.18,-38),("#FFC774",.7,.88,.30,.10,-38),("#7AA7FF",.9,.02,.62,.18,-38),("#0B0E2B",.7,.30,.60,.16,-38)]
    elif theme=="deep":
        base="linear-gradient(170deg,#0B0E2B 0%,#1B2290 55%,#3B4EF2 120%)"
        bl=[("#5B47F5",.9,.15,.7,.28,-38),("#C15BD6",.55,.62,.5,.18,-38),("#FF8F63",.5,.86,.4,.10,-38),("#7AA7FF",.7,.38,.7,.14,-38)]
    s=f'<div class="silk" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{radius}px;background:{base};{extra}">'
    for col,op,cy,lw,lh,ang in bl:
        # cy: vị trí dọc (tỉ lệ), lw/lh: bề rộng/cao theo tỉ lệ cạnh dài
        L=max(w,h)
        s+=f'<div class="b" style="background:{col};opacity:{op};width:{L*1.5:.0f}px;height:{lh*L:.0f}px;left:{-0.25*L:.0f}px;top:{cy*h-lh*L/2:.0f}px;transform:rotate({ang}deg)"></div>'
    s+='<div class="grain"></div>'+inner+'</div>'
    return s

def beam(cx,cy,length,thick,ang=-38,z=4,core="#fff"):
    """Vệt quét: ánh sáng đi qua (nền vệt mờ + lõi sáng mảnh), KHÔNG phải thanh ngang."""
    return (f'<div class="beam" style="left:{cx-length/2}px;top:{cy-thick*3}px;width:{length}px;height:{thick*6}px;transform:rotate({ang}deg);z-index:{z}">'
            f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,transparent,rgba(122,167,255,.28) 40%,rgba(255,255,255,.55) 50%,rgba(122,167,255,.28) 60%,transparent);'
            f'-webkit-mask-image:linear-gradient(90deg,transparent,#000 18%,#000 82%,transparent);mask-image:linear-gradient(90deg,transparent,#000 18%,#000 82%,transparent);filter:blur({thick*.35}px)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:50%;height:{thick*.5}px;margin-top:-{thick*.25}px;border-radius:99px;background:linear-gradient(90deg,transparent,#8AA0FF 15%,{core} 50%,#A6C4FF 85%,transparent);box-shadow:0 0 {thick*2}px rgba(120,150,255,.9)"></div></div>')

def doc(x,y,w,rot,label,title,rows,idtxt,k=1,z=2,hits=(),note=None,fill=.94):
    """Tờ giấy tỉ lệ A4, góc gấp, viền mảnh. k: hệ số cỡ chữ."""
    h=w*1.414; r=w*.045; c=w*.14
    sp=sheet_path(1,1,w-2,h-2,r,c)
    fold=f'M{w-c-1} 1 V{c+1} H{w-1}'
    rowsh=""
    for i,(a,b) in enumerate(rows):
        cl="row hit" if i in hits else "row"
        rowsh+=f'<div class="{cl}" style="margin-top:{14*k:.0f}px;font-size:{11*k:.1f}px"><span class="k">{a}</span><span class="v" style="font-size:{14*k:.1f}px">{b}</span></div>'
    nt=f'<div class="mono" style="position:absolute;left:{w*.08}px;bottom:{w*.07}px;font-size:{10*k:.1f}px;color:var(--cobalt)">{note}</div>' if note else ""
    return (f'<div class="doc" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);z-index:{z}">'
            f'<svg viewBox="0 0 {w} {h}"><path d="{sp}" fill="rgba(255,255,255,{fill})" stroke="rgba(18,22,63,.30)" stroke-width="1"/>'
            f'<path d="{fold}" fill="rgba(122,140,255,.12)" stroke="rgba(18,22,63,.30)" stroke-width="1" stroke-linejoin="round"/></svg>'
            f'<div class="in" style="padding:{w*.08}px {w*.08}px"><div class="row"><span class="chip" style="font-size:{11*k:.1f}px;padding:{3*k:.0f}px {9*k:.0f}px">[{label}]</span></div>'
            f'<div style="margin-top:{w*.09}px;font-size:{17*k:.1f}px;font-weight:600;letter-spacing:-.01em;line-height:1.2;max-width:{w*.62}px">{title}</div>'
            f'<div class="mono" style="margin-top:{5*k}px;font-size:{10*k:.1f}px;color:var(--mute)">{idtxt}</div>'
            f'<div style="height:1px;background:rgba(18,22,63,.14);margin-top:{14*k}px"></div>{rowsh}</div>{nt}</div>')

PAGE = '<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{t}</title><style>{fonts}{css}html,body{{width:{w}px;height:{h}px;background:{bg}}}</style></head><body><div style="position:relative;width:{w}px;height:{h}px;overflow:hidden;background:{bg}">{body}</div></body></html>'
def page(path,t,w,h,body,bg="#fff"):
    pathlib.Path(path).write_text(PAGE.format(t=t,w=w,h=h,body=body,bg=bg,fonts=fonts_css(),css=css()))
