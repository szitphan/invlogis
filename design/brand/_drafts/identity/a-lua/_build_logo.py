#!/usr/bin/env python3
"""Dựng logo hướng A · Lụa (nét vector, không phụ thuộc font). Chạy: python3 _build_logo.py"""
import uharfbuzz as hb, pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
HERE = pathlib.Path(__file__).parent
FONT = str(HERE.parents[1] / "fonts/Lexend-300.ttf")
FONT4 = str(HERE.parents[1] / "fonts/Lexend-400.ttf")
INK="#0E1442"; COBALT="#2F43DB"; LIGHT="#97A6FF"; DEEP="#17206F"
XH=533; ASC=744; STEM=75

def shape(fontpath, text, tracking):
    tt=TTFont(fontpath); blob=hb.Blob.from_file_path(fontpath); font=hb.Font(hb.Face(blob))
    buf=hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(font,buf)
    gs=tt.getGlyphSet(); order=tt.getGlyphOrder(); x=0; out=[]
    for ch,info,pos in zip(text,buf.glyph_infos,buf.glyph_positions):
        out.append((ch,order[info.codepoint],x+pos.x_offset,pos.x_advance)); x+=pos.x_advance+tracking
    return tt,gs,out,x-tracking

def clip_right(poly,p,q):
    # giữ phần nằm bên phải đường p->q (hướng lên: p ở dưới, q ở trên)
    def side(pt): return (q[0]-p[0])*(pt[1]-p[1])-(q[1]-p[1])*(pt[0]-p[0])
    res=[]
    for i in range(len(poly)):
        a,b=poly[i],poly[(i+1)%len(poly)]; sa,sb=side(a),side(b)
        ina,inb=sa<=0,sb<=0
        if ina: res.append(a)
        if ina!=inb:
            t=sa/(sa-sb); res.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
    return res
def d_of(poly): return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in poly)+"Z"

_vn=[0]
def v_group(adv,fill,rfill,dx):
    """chữ v tự dựng: cánh phải là một dải lụa vắt lên cánh trái; khe mảnh (mask) ở chỗ chồng; đầu hai cánh cắt chéo như nếp gấp ở chấm i."""
    w=80; xl,xr=15,adv-15; cx=(xl+xr)/2; rise=18
    left=[(xl,XH-rise),(xl+w,XH),(cx+w/2,0),(cx-w/2,0)]
    right=[(xr-w,XH-rise),(xr,XH),(cx+w/2+6,0),(cx-w/2+6,0)]
    _vn[0]+=1; mid=f"vm{_vn[0]}"
    return (f'<g transform="translate({dx:.1f} 0)"><mask id="{mid}" maskUnits="userSpaceOnUse" x="-200" y="-300" width="1200" height="1200">'
            f'<rect x="-200" y="-300" width="1200" height="1200" fill="#fff"/><path d="{d_of(right)}" fill="#000" stroke="#000" stroke-width="26" stroke-linejoin="miter"/></mask>'
            f'<path d="{d_of(left)}" fill="{fill}" mask="url(#{mid})"/><path d="{d_of(right)}" fill="{rfill}"/></g>')

def i_path(adv, dotcolor=None):
    cx=adv/2; x0=cx-STEM/2; x1=cx+STEM/2
    stem=[(x0,0),(x1,0),(x1,XH),(x0,XH)]
    dot=[(x0,ASC-100),(x1,ASC-100+17),(x1,ASC+17),(x0,ASC)]  # chấm hình bình hành nghiêng
    dot=[(x0,640),(x1,662),(x1,744),(x0,722)]
    return d_of(stem), d_of(dot)

def glyph_d(gs,name,dx):
    from fontTools.pens.transformPen import TransformPen
    pen=SVGPathPen(gs); gs[name].draw(TransformPen(pen,(1,0,0,1,dx,0))); return pen.getCommands()

def word_group(fontpath,text,fill,tracking=25,skip_first=False,custom_i=True,dotfill=None,x0=0,vfill=None):
    """trả về (chuỗi <path>, rộng) ở hệ font (y lên). skip_first: bỏ chữ đầu (dành cho ký hiệu i)."""
    tt,gs,items,total=shape(fontpath,text,tracking); parts=[]; dotfill=dotfill or fill
    start=items[1][2] if skip_first else 0
    for k,(ch,gn,x,adv) in enumerate(items):
        if skip_first and k==0: continue
        dx=x-start+x0
        if ch=="v": 
            parts.append(v_group(adv,fill,vfill or fill,dx))
        elif ch=="i" and custom_i:
            s,dd=i_path(adv); parts.append(f'<path fill="{fill}" transform="translate({dx:.1f} 0)" d="{s}"/><path fill="{dotfill}" transform="translate({dx:.1f} 0)" d="{dd}"/>')
        else:
            parts.append(f'<path fill="{fill}" d="{glyph_d(gs,gn,dx)}"/>')
    return "".join(parts), total-start+x0

# --- ký hiệu: dải lụa gấp thành chữ i (hệ toạ độ 0..~27 × 0..100, y xuống)
def sym_defs(gid,stops):
    s="".join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in stops)
    return f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="18" y1="-4" x2="0" y2="102">{s}</linearGradient>'
DOT="M0 4L14 .5L14 15.5L0 19Z"
STEMP="M0 25L14 21.5C14 41 21 58 17 96.5L3 100C7 62 0 45 0 25Z"
SHEEN="M4.5 28L7.5 27.3C8.5 48 13 62 10.5 92L8 92.6C10.5 64 5.5 48 4.5 28Z"
def symbol_inner(fill, sheen=True):
    s=f'<path d="{DOT}" fill="{fill}"/><path d="{STEMP}" fill="{fill}"/>'
    if sheen and fill.startswith("url"): s+=f'<path d="{SHEEN}" fill="#fff" opacity=".12"/>'
    return s
STOPS_LIGHTBG=[(0,LIGHT),(.45,COBALT),(1,DEEP)]
STOPS_DARKBG=[(0,"#C4CDFF"),(.5,"#6F82FF"),(1,"#3347E6")]
SW=19; SH=100

def logo_svg(variant="color", by=False):
    k=ASC/SH   # đổi đơn vị ký hiệu -> đơn vị font
    gap=120; tracking=25
    if variant=="mono": fill="#000"; sf="#000"; bg=""; defs=""
    elif variant=="reverse": fill="#FFFFFF"; sf="url(#g)"; bg='<rect x="-300" y="-1000" width="3600" height="1800" fill="#0B1033"/>'; defs=sym_defs("g",STOPS_DARKBG)
    else: fill=INK; sf="url(#g)"; bg=""; defs=sym_defs("g",STOPS_LIGHTBG)
    sym_w=SW*k
    wg,tw=word_group(FONT,"invlogis",fill,tracking,skip_first=True,x0=sym_w+gap,vfill=(COBALT if variant=="color" else None))
    W=tw; pad=0
    body=f'<g transform="scale({k:.4f})">{symbol_inner(sf)}</g>'
    # chữ: hệ font y lên → lật; baseline tại y=ASC
    body+=f'<g transform="translate(0 {ASC}) scale(1 -1)">{wg}</g>'
    extra=""; H=ASC+250; vb_y=0
    if by:
        # dòng chữ ký "by innvie" dưới chữ, căn trái với chữ n
        iw,iwid=word_group(FONT,"innvie",fill,tracking=60,custom_i=True,dotfill=fill if variant!="color" else COBALT,vfill=(COBALT if variant=="color" else None))
        sc=0.19; y=ASC+330
        sx=sym_w+gap+60
        lbl_col=fill if variant!="color" else "#55608F"
        by_g,bw=word_group(FONT,"by",lbl_col,60)
        body+=f'<g transform="translate({sx+0:.1f} {y}) scale({sc} -{sc})" opacity=".9">{by_g}</g>'
        body+=f'<g transform="translate({sx+ (bw+260)*sc:.1f} {y}) scale({sc} -{sc})">{iw}</g>'
        H=ASC+400
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {W+2*pad:.0f} {H+2*pad}"><defs>{defs}</defs>{bg}{body}</svg>'
def symbol_svg(variant="color"):
    if variant=="mono": fill="#000"; defs=""
    else: fill="url(#g)"; defs=sym_defs("g",STOPS_LIGHTBG)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 {SW+2} {SH+2}"><defs>{defs}</defs>{symbol_inner(fill)}</svg>'
def innvie_svg(fill=INK,dot=COBALT,bgrect=None):
    g,w=word_group(FONT4,"innvie",fill,tracking=30,dotfill=dot,vfill=dot)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {ASC+250}"><g transform="translate(0 {ASC}) scale(1 -1)">{g}</g></svg>'
def wordmark_full(fill=INK,dot=COBALT):
    g,w=word_group(FONT,"invlogis",fill,tracking=25,dotfill=dot,vfill=dot)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {ASC+250}"><g transform="translate(0 {ASC}) scale(1 -1)">{g}</g></svg>'
def favicon_svg(size_hint=32):
    # khối i đặc trên ô bo tròn: không nếp, không sheen — đọc được ở 16px
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="t" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4A5DF0"/><stop offset="1" stop-color="#1B2488"/></linearGradient></defs>'
            '<rect width="64" height="64" rx="15" fill="url(#t)"/>'
            '<path d="M21 10L43 6L43 25L21 29Z" fill="#fff"/><path d="M21 34L43 30L43 56L21 56Z" fill="#fff"/></svg>')
def appicon_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs>'
            '<linearGradient id="t" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5568F5"/><stop offset=".55" stop-color="#2F43DB"/><stop offset="1" stop-color="#141C70"/></linearGradient>'
            '<linearGradient id="r" gradientUnits="userSpaceOnUse" x1="640" y1="170" x2="380" y2="860"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C9D1FF"/></linearGradient>'
            '<radialGradient id="h" cx=".2" cy=".1" r=".9"><stop offset="0" stop-color="#9FB0FF" stop-opacity=".55"/><stop offset="1" stop-color="#9FB0FF" stop-opacity="0"/></radialGradient></defs>'
            '<rect width="1024" height="1024" fill="url(#t)"/><rect width="1024" height="1024" fill="url(#h)"/>'
            '<defs><filter id="bl" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="38"/></filter></defs><g filter="url(#bl)" opacity=".5"><path d="M-80 760C200 600 420 700 700 380C820 250 960 200 1100 120L1100 330C900 420 800 560 620 760C420 980 150 900 -80 1000Z" fill="#7C8FFF"/><path d="M-80 300C160 330 360 120 560 -60L760 -60C560 160 380 420 -80 480Z" fill="#A9B7FF" opacity=".7"/></g><g transform="translate(441 142) scale(7.4)"><g>'+symbol_inner("url(#r)",sheen=False)+'</g></g></svg>')

if __name__=="__main__":
    W=lambda n,s:(HERE/n).write_text(s)
    W("invlogis-logo.svg",logo_svg()); W("invlogis-logo-mono.svg",logo_svg("mono")); W("invlogis-logo-reverse.svg",logo_svg("reverse"))
    W("invlogis-by-innvie.svg",logo_svg(by=True)); W("invlogis-symbol.svg",symbol_svg()); W("invlogis-symbol-mono.svg",symbol_svg("mono"))
    W("innvie-logo.svg",innvie_svg()); W("invlogis-wordmark.svg",wordmark_full()); W("_favicon.svg",favicon_svg()); W("_appicon.svg",appicon_svg())
    print("ok")
