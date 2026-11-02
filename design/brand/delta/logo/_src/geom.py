"""Hình học logo Delta, đo trên PNG nhúng trong IMG_7946 1.svg (900x248). Toạ độ = px ảnh gốc."""
import math
BLACK="#1E1915"; GREEN="#0A9849"
TOP,BASE=111.6,241.4
def rp(pts,r=1.6):
    """Đa giác bo góc nhỏ. pts: (x,y) hoặc (x,y,r)."""
    n=len(pts);d=""
    for i,p in enumerate(pts):
        a=pts[i-1];c=pts[(i+1)%n];rr=p[2] if len(p)>2 else r
        def tow(q):
            dx,dy=q[0]-p[0],q[1]-p[1];L=math.hypot(dx,dy);k=min(rr,L/2)/L;return p[0]+dx*k,p[1]+dy*k
        s=tow(a);e=tow(c)
        d+=("M" if i==0 else "L")+f"{s[0]:.2f} {s[1]:.2f}Q{p[0]:.2f} {p[1]:.2f} {e[0]:.2f} {e[1]:.2f}"
    return d+"Z"
# D: viền ngoài + lỗ
D_OUT=f"M10.6 {TOP}H128C152 {TOP} 175.5 124 175.5 152V200C175.5 229 152 {BASE} 128 {BASE}H10.6Q9 {BASE} 9 {BASE-1.6}V{TOP+1.6}Q9 {TOP} 10.6 {TOP}Z"
D_IN="M57.5 152.5H116C125 152.5 130 157 130 165V187C130 195 125 199.5 116 199.5H57.5Q55.5 199.5 55.5 197.5V154.5Q55.5 152.5 57.5 152.5Z"
D=D_OUT+D_IN
# E+L liền khối, có thanh xanh trong hốc
EL=rp([(183,TOP),(277,TOP),(311.5,150.5,0.8),(229.5,150.5,0.8),(229.5,200,0.8),(326,200,0.8),(326,TOP),(375,TOP),(375,200,0.8),(459,200),(459,BASE),(183,BASE)])
BAR=(229.5,156,90.5,37.5)
T=rp([(427,TOP),(581.5,TOP),(581.5,152.5),(529.5,152.5,0.8),(529.5,BASE),(481,BASE),(481,152.5,0.8),(427,152.5)])
s=0.5253
def L(y):return 616.3-(y-TOP)*s
def R(y):return 678.7+(y-TOP)*s
NO=221
A=rp([(L(TOP),TOP,3),(R(TOP),TOP,3),(R(BASE),BASE),(R(BASE)-52.5,BASE),(R(BASE)-52.5-(BASE-NO)*s,NO,1),(L(BASE)+52.5+(BASE-NO)*s,NO,1),(L(BASE)+52.5,BASE),(L(BASE),BASE)])
A+="M648.3 151.2L665.3 184H631.4Z"
WORD=[D,EL,T,A]
WX0,WX1=9,746.5
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
_f=TTFont('/System/Library/Fonts/Supplemental/STIXGeneralBol.otf');_gs=_f.getGlyphSet()
_g=_gs[_f.getBestCmap()[ord('R')]];_b=BoundsPen(_gs);_g.draw(_b)
def r_path(x0,y0,x1,y1):
    bx0,by0,bx1,by1=_b.bounds;sx=(x1-x0)/(bx1-bx0);sy=(y1-y0)/(by1-by0)
    p=SVGPathPen(_gs);_g.draw(TransformPen(p,(sx,0,0,-sy,x0-bx0*sx,y1+by0*sy)));return p.getCommands()
RC=(820.5,85.5);RO=72.5;RW=8.5
def ring(cx=RC[0],cy=RC[1],ro=RO,w=RW):
    ri=ro-w
    c=lambda r,sw:f"M{cx-r:.2f} {cy:.2f}A{r:.2f} {r:.2f} 0 1 {sw} {cx+r:.2f} {cy:.2f}A{r:.2f} {r:.2f} 0 1 {sw} {cx-r:.2f} {cy:.2f}Z"
    return c(ro,1)+c(ri,0)
