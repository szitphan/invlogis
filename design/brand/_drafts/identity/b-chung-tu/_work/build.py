import math, re, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOLS = ROOT.parents[1] / "_tools"; FONTS = ROOT.parents[1] / "fonts"
W = ROOT / "_work"
INK = "#12163F"; MUTE = "#5B6190"

def wm(text, wght=500, tracking=-10, fill=INK, name=None):
    f = FONTS / f"Manrope-{wght}.ttf"; nm = name or re.sub(r'\W','',text); out = W / f"wm-{nm}-{wght}-{abs(tracking)}.svg"
    subprocess.run(["python3", TOOLS/"wordmark.py", f, text, out, "--size","200","--tracking",str(tracking),"--fill",fill,"--wght",str(wght)], check=True, capture_output=True)
    s = out.read_text()
    vb = [float(x) for x in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    d = re.search(r' d="([^"]+)"', s).group(1)
    return vb, d   # viewBox x,y,w,h ; baseline at y=0 in path space

def sheet_path(x, y, w, h, r, c):
    return (f"M{x} {y+r} Q{x} {y} {x+r} {y} L{x+w-c} {y} L{x+w} {y+c} L{x+w} {y+h-r} "
            f"Q{x+w} {y+h} {x+w-r} {y+h} L{x+r} {y+h} Q{x} {y+h} {x} {y+h-r} Z")

def symbol(p="s", mode="color", small=False):
    """(defs, body) trong hệ toạ độ 64x64. mode: color | mono | reverse"""
    if mode == "color": stroke, g = INK, ("#5B47F5", "#3B4EF2", "#7AA7FF")
    elif mode == "mono": stroke, g = "currentColor", None
    else: stroke, g = "#FFFFFF", ("#A99CFF", "#8294FF", "#A6C4FF")
    beamfill = f"url(#{p}g)" if g else stroke
    if small:
        sw, x, y, w, h, r, c = 5, 10, 3, 44, 58, 7, 14
        cx, cy, ang, half, th, gap = 33, 35, -38, 31, 12.5, 2.6
    else:
        sw, x, y, w, h, r, c = 2.6, 22, 12, 34, 48, 5, 10
        cx, cy, ang, half, th, gap = 38, 36, -38, 29, 5.4, 2.4
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a)
    x1, y1, x2, y2 = cx-ux*half, cy-uy*half, cx+ux*half, cy+uy*half
    nx, ny = uy, -ux
    if nx > 0: nx, ny = -nx, -ny            # pháp tuyến hướng lên-trái (phần đã đọc)
    defs = []; body = []
    if g:
        defs.append(f'<linearGradient id="{p}g" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}">'
                    f'<stop offset="0" stop-color="{g[0]}"/><stop offset=".55" stop-color="{g[1]}"/><stop offset="1" stop-color="{g[2]}"/></linearGradient>')
    sp = sheet_path(x, y, w, h, r, c)
    def knock(pid, extra=""):
        return (f'<mask id="{pid}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="84" height="84"><rect x="-10" y="-10" width="84" height="84" fill="#fff"/>{extra}</mask>')
    defs.append(knock(f"{p}mk", f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#000" stroke-width="{th+2*gap:.1f}" stroke-linecap="round"/>'))
    op = 1 if mode == "mono" else .5
    if not small:
        bx, by = 9, 7
        defs.append(knock(f"{p}bk", f'<path d="{sp}" fill="#000" stroke="#000" stroke-width="{sw+3.6:.1f}" stroke-linejoin="round"/>'))
        body.append(f'<g mask="url(#{p}bk)"><g transform="rotate(-7 26 31)"><rect x="{bx}" y="{by}" width="{w}" height="{h}" rx="{r}" fill="none" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/></g></g>')
        if g:   # ánh sáng đổ lên phần đã đọc
            defs.append(f'<clipPath id="{p}cl"><path d="{sp}"/></clipPath>')
            defs.append(f'<linearGradient id="{p}h" gradientUnits="userSpaceOnUse" x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx+nx*30:.1f}" y2="{cy+ny*30:.1f}">'
                        f'<stop offset="0" stop-color="{g[1]}" stop-opacity=".38"/><stop offset="1" stop-color="{g[0]}" stop-opacity="0"/></linearGradient>')
            L = 46; e = 8
            pts = [(x1-ux*e,y1-uy*e),(x2+ux*e,y2+uy*e),(x2+ux*e+nx*L,y2+uy*e+ny*L),(x1-ux*e+nx*L,y1-uy*e+ny*L)]
            body.append(f'<g clip-path="url(#{p}cl)"><polygon points="{" ".join(f"{u:.1f},{v:.1f}" for u,v in pts)}" fill="url(#{p}h)"/></g>')
    fold = f'<path d="M{x+w-c} {y} V{y+c} H{x+w}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'
    body.append(f'<g mask="url(#{p}mk)"><path d="{sp}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>{"" if small else fold}</g>')
    body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{beamfill}" stroke-width="{th}" stroke-linecap="round"/>')
    if not small:   # sợi chỉ mảnh phía chưa đọc: độ chính xác
        o = 7.6; sx, sy = -nx*o, -ny*o
        body.append(f'<line x1="{x1+ux*17+sx:.1f}" y1="{y1+uy*17+sy:.1f}" x2="{x2-ux*12+sx:.1f}" y2="{y2-uy*12+sy:.1f}" stroke="{beamfill}" stroke-width="1.3" stroke-linecap="round" opacity="{1 if mode=="mono" else .8}"/>')
    return "".join(defs), "".join(body)

def svg(w, h, inner, defs="", bg=None, extra=""):
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}"{extra}><defs>{defs}</defs>{r}{inner}</svg>'

def lockup(mode="color", p="l", by=False):
    fill = {"color": INK, "mono": "currentColor", "reverse": "#FFFFFF"}[mode]
    defs, body = symbol(p, mode)
    vb, d = wm("Invlogis", fill=fill)
    s = 0.215                         # cỡ chữ: cao chữ hoa = 144*s
    cap = 144*s; base = 32 + cap/2 + 1
    tx = 64 + 12
    inner = body + f'<g transform="translate({tx} {base:.1f}) scale({s})"><path fill="{fill}" d="{d}"/></g>'
    width = tx + vb[2]*s + 2
    H = 64
    if by:
        vb2, d2 = wm("by innvie", wght=500, tracking=0, fill=(MUTE if mode=="color" else fill), name="byinnvie")
        s2 = 0.085
        inner += f'<g transform="translate({tx+1.5} {base+22:.1f}) scale({s2})" opacity="{1 if mode=="color" else .8}"><path d="{d2}" fill="{(MUTE if mode=="color" else fill)}"/></g>'
        H = 76
    return svg(round(width,1), H, inner, defs)

def innvie(mode="color", p="i"):
    fill = {"color": INK, "mono": "currentColor", "reverse": "#FFFFFF"}[mode]
    sw = 2.6
    sp = sheet_path(14, 8, 34, 48, 5, 10)
    mark = (f'<path d="{sp}" fill="none" stroke="{fill}" stroke-width="{sw}" stroke-linejoin="round"/>'
            f'<path d="M38 8 V18 H48" fill="none" stroke="{fill}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>')
    vb, d = wm("innvie", fill=fill)
    s = 0.19; x_h = 144*s*0.78
    base = 32 + 144*s/2 + 1
    tx = 64
    inner = mark + f'<g transform="translate({tx} {base:.1f}) scale({s})"><path fill="{fill}" d="{d}"/></g>'
    return svg(round(tx+vb[2]*s+2,1), 64, inner)

if __name__ == "__main__":
    out = ROOT
    d, b = symbol("s"); (out/"invlogis-symbol.svg").write_text(svg(64,64,b,d))
    (out/"invlogis-logo.svg").write_text(lockup("color","l"))
    (out/"invlogis-by-innvie.svg").write_text(lockup("color","b",by=True))
    (out/"invlogis-logo-mono.svg").write_text(lockup("mono","m").replace('<svg ','<svg color="#12163F" ',1))
    (out/"invlogis-logo-reverse.svg").write_text(lockup("reverse","r"))
    (out/"innvie-logo.svg").write_text(innvie())
    d, b = symbol("f", small=True); (W/"sym-small.svg").write_text(svg(64,64,b,d))
    d, b = symbol("m", "mono", small=True); (W/"sym-small-mono.svg").write_text(svg(64,64,b,d,extra=' color="#12163F"'))
    d, b = symbol("mm", "mono"); (W/"sym-mono.svg").write_text(svg(64,64,b,d,extra=' color="#12163F"'))
    print("ok")
