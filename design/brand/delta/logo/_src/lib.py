import re,geom as g
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
INK,GREEN=g.BLACK,g.GREEN;TILE="#1B7B46";WHITE="#FFFFFF"
import pathlib
ROOT=str(pathlib.Path(__file__).resolve().parents[5])
FONTS=ROOT+"/design/brand/_drafts/fonts/"
def text_path(txt,font,size,x,y,track=0,anchor="start",width=None):
    f=TTFont(FONTS+font);gs=f.getGlyphSet();cm=f.getBestCmap();upm=f['head'].unitsPerEm;k=size/upm;hm=f['hmtx']
    adv=[hm[cm[ord(c)]][0]*k for c in txt]
    if width is not None:track=(width-sum(adv))/(len(txt)-1)
    tot=sum(adv)+track*(len(txt)-1);cx=x-(tot if anchor=="end" else 0);d=""
    for c,a in zip(txt,adv):
        p=SVGPathPen(gs);gs[cm[ord(c)]].draw(TransformPen(p,(k,0,0,-k,cx,y)));d+=p.getCommands();cx+=a+track
    return d,tot
def rnd(d):return re.sub(r"\d+\.\d{3,}",lambda m:f"{float(m.group()):.2f}",d)
def P(d,fill,er=True):return f'<path fill="{fill}"'+(' fill-rule="evenodd"' if er else '')+f' d="{rnd(d)}"/>'
def R(x,y,w,h,fill):return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{fill}"/>'
def reg(kind,fg):
    if kind=="orig":
        return P(g.ring(),fg)+P(g.r_path(777,41,868,131),fg,False)
    if kind=="small":
        ro=24.5;cx,cy=750,g.TOP+ro;w=4.6;s=ro/g.RO
        rx0=cx-(820.5-777)*s;rx1=cx+(868-820.5)*s;ry0=cy-(85.5-41)*s;ry1=cy+(131-85.5)*s
        return P(g.ring(cx,cy,ro,w),fg)+P(g.r_path(rx0,ry0,rx1,ry1),fg,False)
    return ""
REGBOX=dict(orig=(9,13,893,g.BASE),small=(9,g.TOP,774.5,g.BASE),none=(9,g.TOP,746.5,g.BASE))
def word(fg,ac,kind="small"):
    return P("".join(g.WORD),fg)+R(*g.BAR,ac)+reg(kind,fg)
def svg(inner,x0,y0,x1,y1,pad=0,title="Logo Delta",attrs=""):
    vb=f"{x0-pad:g} {y0-pad:g} {x1-x0+2*pad:g} {y1-y0+2*pad:g}"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{title}"{attrs}><title>{title}</title>{inner}</svg>'
# ---- ký hiệu: (inner(fg,ac), bbox)
def sym_d(fg,ac):
    return P(g.D_OUT+g.D_IN,fg)+R(55.5,158,68.5,36,ac)
SYMS={"d":(sym_d,(9,g.TOP,175.5,g.BASE))}
# Δ: dáng theo độ dốc chữ A, hốc + thanh như chữ E
def sym_tri(fg,ac):
    s=g.s;L=lambda y:g.L(y);Rr=lambda y:g.R(y)
    o=g.rp([(L(g.TOP),g.TOP,3),(Rr(g.TOP),g.TOP,3),(Rr(g.BASE),g.BASE),(L(g.BASE),g.BASE)])
    # hốc: chữ nhật cùng tinh thần chữ E
    return P(o+"M604 172H692.6V212H604Z",fg)+R(604,177.5,82.6,29,ac)
SYMS["tri"]=(sym_tri,(g.L(g.BASE),g.TOP,g.R(g.BASE),g.BASE))
# Δ lụa logo cũ, đo từ ảnh 167x111
def sym_swoosh(fg,ac):
    return P("M74.5 0L29 86C25.5 93 27 100.5 34 101.2L146.5 105.2L143 111H0Z",ac)
SYMS["swoosh"]=(sym_swoosh,(0,0,146.5,111))
def sym_inner_scaled(k,fg,ac,cx,cy,w):
    """đặt ký hiệu k, rộng w, tâm (cx,cy)"""
    fn,(a,b,c,d)=SYMS[k];sc=w/(c-a)
    return f'<g transform="translate({cx-sc*(a+c)/2:.2f} {cy-sc*(b+d)/2:.2f}) scale({sc:.4f})">{fn(fg,ac)}</g>'
def fg_ac(name):
    return dict(primary=(INK,GREEN),reverse=(WHITE,GREEN),black=("#000000","#000000"),white=(WHITE,WHITE))[name]
def symbol_svg(k,name="primary"):
    if k=="tile":
        return svg(f'<rect width="100" height="100" rx="22" fill="{TILE}"/>'+f'<g transform="translate(16.6 25.6) scale(0.4)"><path fill="#fff" fill-rule="evenodd" transform="translate(-9 -{g.TOP})" d="{rnd(g.D_OUT+g.D_IN)}"/></g>',0,0,100,100,title="Ký hiệu Delta")
    fg,ac=fg_ac(name);fn,bb=SYMS[k]
    if k=="swoosh" and name in("primary","reverse"):ac=GREEN
    return svg(fn(fg,ac),*bb,title="Ký hiệu Delta")
def wordmark_svg(name="primary",kind="small"):
    fg,ac=fg_ac(name);return svg(word(fg,ac,kind),*REGBOX[kind])
def stacked_svg(k,name="primary",kind="small"):
    fg,ac=fg_ac(name);x0,y0,x1,y1=REGBOX[kind];cx=(9+746.5)/2
    h=205;sw={"d":215,"tri":320,"swoosh":270,"tile":0}.get(k,265)
    return svg(f'<g transform="translate(0 {h})">{word(fg,ac,kind)}</g>'+sym_inner_scaled(k,fg,ac if k!="swoosh" or name in("black","white") else GREEN,cx,g.TOP+85,sw),x0,g.TOP-22,x1,y1+h)
def intl_svg(name="primary",kind="small"):
    fg,ac=fg_ac(name);d,_=text_path("International","Montserrat-700.ttf",70,9,322,width=737.5)
    x0,y0,x1,y1=REGBOX[kind];return svg(word(fg,ac,kind)+P(d,fg,False),x0,y0,x1,326,title="Logo Delta International")
INV=open(ROOT+"/design/brand/invlogis/logo/invlogis-primary.svg").read()
INVR=open(ROOT+"/design/brand/invlogis/logo/invlogis-reverse.svg").read()
def inv_g(rev,x,y,h,suf):
    s=INVR if rev else INV;vb=list(map(float,re.search(r'viewBox="([^"]+)"',s).group(1).split()));inner=re.sub(r"^<svg[^>]*>|</svg>\s*$","",s.strip())
    ids=set(re.findall(r'id="([^"]+)"',inner))
    for i in ids:inner=inner.replace(f'id="{i}"',f'id="{i}{suf}"').replace(f'url(#{i})',f'url(#{i}{suf})')
    k=h/vb[3];return f'<g transform="translate({x-vb[0]*k:.2f} {y-vb[1]*k:.2f}) scale({k:.4f})">{inner}</g>',vb[2]*k
def on_inv_svg(rev=False,kind="small",suf="i"):
    fg,ac=fg_ac("reverse" if rev else "primary");x0,y0,x1,y1=REGBOX[kind]
    logo,w=inv_g(rev,0,0,0.0001,suf);h=62;w=h*3677.9/1032.6;lx=746.5-w;lg,_=inv_g(rev,lx,272,h,suf)
    d,_t=text_path("Vận hành trên","Lexend-400.ttf",34,lx-14,272+40,anchor="end")
    return svg(word(fg,ac,kind)+P(d,"#B8B8B8" if rev else "#5C5C5C",False)+lg,x0,y0,x1,272+h,title="Logo Delta, vận hành trên invlogis")
def app_icon(k,bg="ink",size=None):
    bgc={"ink":INK,"white":WHITE,"green":TILE}[bg]
    fg,ac={"ink":(WHITE,GREEN),"white":(INK,GREEN),"green":(WHITE,WHITE)}[bg]
    if k=="swoosh":
        ac=GREEN if bg!="green" else WHITE
    if k=="tile":fg,ac=(WHITE,WHITE)
    w={"d":560,"tri":640,"swoosh":640,"tile":560}[k];kk="d" if k=="tile" else k
    fn=sym_inner_scaled(kk,fg,ac,512,512,w)
    if k=="tile":
        a,b,c,d=SYMS["d"][1];sc=w/(c-a);fn=f'<g transform="translate({512-sc*(a+c)/2:.2f} {512-sc*(b+d)/2:.2f}) scale({sc:.4f})"><path fill="#fff" fill-rule="evenodd" d="{rnd(g.D_OUT+g.D_IN)}"/></g>';bgc=TILE
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" role="img" aria-label="Icon app Delta"><rect width="1024" height="1024" fill="{bgc}"/>{fn}</svg>'
# favicon cho D: vẽ khớp lưới 32
FAV_D="M3 5H21C26 5 30 8.5 30 13.5V18.5C30 23.5 26 27 21 27H3Z M10 11.5H19.5C21.8 11.5 23 12.7 23 14.5V17.5C23 19.3 21.8 20.5 19.5 20.5H10Z"
def favicon(k="d",dark=False):
    fg=WHITE if dark else INK
    if k=="d":
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path fill="{fg}" fill-rule="evenodd" d="{FAV_D}"/><rect x="10" y="13.5" width="11" height="5" fill="{g.GREEN}"/></svg>'
    if k=="tile":return symbol_svg("tile")
    if k=="swoosh":return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path fill="{g.GREEN}" d="M18 2L1 29H31V24.5L10.5 24Q9 23.8 9.8 22.5L20.5 5Z"/></svg>'
    fn,bb=SYMS["tri"];return svg(fn(fg,g.GREEN),*bb)
