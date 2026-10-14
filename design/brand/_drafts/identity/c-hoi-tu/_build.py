#!/usr/bin/env python3
"""Sinh bộ logo hướng C · Hội tụ. Chạy: python3 _build.py  (cần fontTools, uharfbuzz)"""
import uharfbuzz as hb, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE=os.path.dirname(os.path.abspath(__file__)); FONTS=os.path.join(HERE,'../../fonts')
COBALT='#1a23d1'; DEEP='#0f14b3'; VIOLET='#7a4dff'; CORAL='#ff6b5e'; AMBER='#ffa24d'; INK='#0f1433'

def shape(fontfile,text,size,tracking=0):
    tt=TTFont(fontfile); upm=tt['head'].unitsPerEm; s=size/upm
    face=hb.Face(hb.Blob.from_file_path(fontfile)); f=hb.Font(face)
    b=hb.Buffer(); b.add_str(text); b.guess_segment_properties(); hb.shape(f,b)
    gs=tt.getGlyphSet(); order=tt.getGlyphOrder(); x=0; out=[]
    for ch,i,p in zip(text,b.glyph_infos,b.glyph_positions):
        pen=SVGPathPen(gs); gs[order[i.codepoint]].draw(TransformPen(pen,(s,0,0,-s,p.x_offset*s,0)))
        out.append((ch,pen.getCommands(),x*s,p.x_advance*s)); x+=p.x_advance+tracking*upm/1000
    return out,(x-tracking*upm/1000)*s

# --- ký hiệu 1000x1000: 3 nét chụm về chấm đặc ---
VX,VY,VR=500,730,150          # chấm hội tụ
def arms(three=True):
    a=[('L',(150,150),(VX,VY),9),('R',(850,150),(VX,VY),9)]
    return a
def symbol_elems(uid,mode='color',three=False,sw=178,dotcol=None):
    """mode: color | mono(c) | rev"""
    if mode=='color':
        gl=f'<linearGradient id="{uid}l" gradientUnits="userSpaceOnUse" x1="120" y1="120" x2="500" y2="700"><stop offset="0" stop-color="{VIOLET}"/><stop offset="1" stop-color="{COBALT}"/></linearGradient>'
        gr=f'<linearGradient id="{uid}r" gradientUnits="userSpaceOnUse" x1="880" y1="120" x2="500" y2="700"><stop offset="0" stop-color="{CORAL}"/><stop offset=".72" stop-color="{COBALT}"/></linearGradient>'
        gc=f'<linearGradient id="{uid}c" gradientUnits="userSpaceOnUse" x1="500" y1="60" x2="500" y2="700"><stop offset="0" stop-color="#4f7bff"/><stop offset="1" stop-color="{COBALT}"/></linearGradient>'
        cl,cr,cc,dc=f'url(#{uid}l)',f'url(#{uid}r)',f'url(#{uid}c)',DEEP; defs=gl+gr+gc
    elif mode=='rev':
        gl=f'<linearGradient id="{uid}l" gradientUnits="userSpaceOnUse" x1="120" y1="120" x2="500" y2="700"><stop offset="0" stop-color="#b9a6ff"/><stop offset="1" stop-color="#ffffff"/></linearGradient>'
        gr=f'<linearGradient id="{uid}r" gradientUnits="userSpaceOnUse" x1="880" y1="120" x2="500" y2="700"><stop offset="0" stop-color="#ff9a8a"/><stop offset=".72" stop-color="#ffffff"/></linearGradient>'
        cl,cr,cc,dc=f'url(#{uid}l)',f'url(#{uid}r)','#c7d4ff','#ffffff'; defs=gl+gr
    else:
        cl=cr=cc=dc=mode; defs=''
    e=f'<defs>{defs}</defs>'
    if three: e+=f'<path d="M500 60 V{VY}" stroke="{cc}" stroke-width="{sw*0.62:.0f}" stroke-linecap="round" fill="none"/>'
    e+=f'<path d="M165 165 L{VX} {VY}" stroke="{cl}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>'
    e+=f'<path d="M835 165 L{VX} {VY}" stroke="{cr}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>'
    e+=f'<circle cx="{VX}" cy="{VY}" r="{VR}" fill="{dc}"/>'
    return e
SYM_BOX=(40,0,960,900)

def svg(w,h,vb,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n'

def wordmark(text,size,fill,uid,mode,tracking=-10,font='Lexend-600.ttf'):
    """trả (body, width, ascent, descent) với baseline y=0. Chữ v thay bằng v tuỳ biến."""
    gl,W=shape(os.path.join(FONTS,font),text,size,tracking); s=size/1000
    body=''; 
    for ch,d,x,adv in gl:
        if ch=='v':
            # v: hai nét + chấm, cao x-height 525, rộng 15..579
            xh=525*s; x0=x+15*s; x1=x+579*s; cx=(x0+x1)/2; sw=162*s; r=112*s; vy=-r-2*s
            top=-xh+sw/2*0.0
            if mode=='color':
                g=f'<linearGradient id="{uid}wl" gradientUnits="userSpaceOnUse" x1="{x0:.1f}" y1="{-xh:.1f}" x2="{cx:.1f}" y2="{vy:.1f}"><stop offset="0" stop-color="{VIOLET}"/><stop offset="1" stop-color="{COBALT}"/></linearGradient><linearGradient id="{uid}wr" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{-xh:.1f}" x2="{cx:.1f}" y2="{vy:.1f}"><stop offset="0" stop-color="{CORAL}"/><stop offset=".75" stop-color="{COBALT}"/></linearGradient>'
                cl,cr=f'url(#{uid}wl)',f'url(#{uid}wr)'; dc=DEEP
            elif mode=='rev':
                g=f'<linearGradient id="{uid}wl" gradientUnits="userSpaceOnUse" x1="{x0:.1f}" y1="{-xh:.1f}" x2="{cx:.1f}" y2="{vy:.1f}"><stop offset="0" stop-color="#b9a6ff"/><stop offset="1" stop-color="#fff"/></linearGradient><linearGradient id="{uid}wr" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{-xh:.1f}" x2="{cx:.1f}" y2="{vy:.1f}"><stop offset="0" stop-color="#ff9a8a"/><stop offset=".75" stop-color="#fff"/></linearGradient>'
                cl,cr,dc=f'url(#{uid}wl)',f'url(#{uid}wr)','#fff'
            else: g='';cl=cr=dc=fill
            ax0=x0+sw/2; ax1=x1-sw/2; ty=-xh+sw/2
            body+=f'<defs>{g}</defs><path d="M{ax0:.1f} {ty:.1f} L{cx:.1f} {vy:.1f}" stroke="{cl}" stroke-width="{sw:.1f}" stroke-linecap="round" fill="none"/><path d="M{ax1:.1f} {ty:.1f} L{cx:.1f} {vy:.1f}" stroke="{cr}" stroke-width="{sw:.1f}" stroke-linecap="round" fill="none"/><circle cx="{cx:.1f}" cy="{vy:.1f}" r="{r:.1f}" fill="{dc}"/>'
        elif d:
            body+=f'<path transform="translate({x:.1f} 0)" d="{d}" fill="{fill}"/>'
    return body,W

def tr(x,y,b): return f'<g transform="translate({x:.1f} {y:.1f})">{b}</g>'
def symbol_scaled(h,x,y,uid,mode,three=False):
    k=h/900; return f'<g transform="translate({x:.1f} {y:.1f}) scale({k:.4f}) translate(-40 0)">{symbol_elems(uid,mode,three)}</g>'

def logo(mode,fill,uid,bg=None,three=False):
    S=200; wm,W=wordmark('invlogis',S,fill,uid,mode)
    sh=170; sx=0; gap=46
    # ký hiệu cao 190, đáy trùng baseline-0.. đặt đáy tại baseline+? 
    sym=symbol_scaled(sh,0,-sh*0.972,uid+'s',mode,three)
    sw=(960-40)/900*sh
    body=sym+tr(sw+gap,0,wm)
    tw=sw+gap+W; asc=sh; desc=64
    pad=40
    vb=f'{-pad} {-asc-pad+4} {tw+2*pad:.0f} {asc+desc+2*pad-4:.0f}'
    if bg: body=f'<rect x="{-pad}" y="{-asc-pad+4}" width="{tw+2*pad:.0f}" height="{asc+desc+2*pad-4:.0f}" fill="{bg}"/>'+body
    return body,vb,(tw+2*pad,asc+desc+2*pad-4)

def write(name,s): open(os.path.join(HERE,name),'w').write(s)

# 1. logo ngang
b,vb,(w,h)=logo('color',COBALT,'a'); write('invlogis-logo.svg',svg(round(w),round(h),vb,b,'Invlogis'))
b,vb,(w,h)=logo('#0f1433','#0f1433','m'); write('invlogis-logo-mono.svg',svg(round(w),round(h),vb,b,'Invlogis (đơn sắc)'))
b,vb,(w,h)=logo('rev','#ffffff','r',bg=INK); write('invlogis-logo-reverse.svg',svg(round(w),round(h),vb,b,'Invlogis (nền tối)'))
b,vb,(w,h)=logo('rev','#ffffff','r'); write('_logo-reverse-bare.svg',svg(round(w),round(h),vb,b,'Invlogis'))
# 2. ký hiệu
write('invlogis-symbol.svg',svg(512,512,'0 0 920 920',f'<g transform="translate(-40 40)">{symbol_elems("sy")}</g>','Ký hiệu Invlogis'))
# 3. innvie
wm,W=wordmark('innvie',200,COBALT,'iv','color')
write('innvie-logo.svg',svg(round(W+80),300,f'-40 -240 {W+80:.0f} 300',wm,'innvie'))
# 4. lockup by innvie
S=200; wm,W=wordmark('invlogis',S,COBALT,'k','color'); sh=170; sw=(960-40)/900*sh; gap=46
sym=symbol_scaled(sh,0,-sh*0.972,'ks','color')
by,bw=shape(os.path.join(FONTS,'Lexend-400.ttf'),'by innvie',56,40)
bp=''.join(f'<path transform="translate({x:.1f} 0)" d="{d}" fill="#5b6a8c"/>' for ch,d,x,a in by if d)
tw=sw+gap+W
body=sym+tr(sw+gap,0,wm)+tr(tw-bw,112,bp)
write('invlogis-by-innvie.svg',svg(round(tw+80),round(190+160+40),f'-40 -186 {tw+80:.0f} {190+160+40}',body,'Invlogis by innvie'))
# 5. favicon/app icon sources (2 nét + chấm dày)
def tile(size,rad,solid=False):
    g=symbol_elems('f','#ffffff' if solid else 'rev',three=False,sw=185 if solid else 190)
    return svg(size,size,'0 0 1000 1000',f'<defs><linearGradient id="bgf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a30e0"/><stop offset="1" stop-color="{DEEP}"/></linearGradient></defs><rect width="1000" height="1000" rx="{rad}" fill="url(#bgf)"/><g transform="translate(500 500) scale(.94) translate(-500 -478)">{g}</g>','icon')
write('_favicon.svg',tile(64,200,True))
write('_appicon.svg',tile(1024,0))
