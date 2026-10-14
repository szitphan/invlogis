def symbol(p="s", mode="color", small=False):
    """(defs, body) trong hệ toạ độ 64x64. mode: color | mono | reverse"""
    if mode == "color": stroke, g = INK, ("#5B47F5", "#2F5BFF", "#3BB4FF")
    elif mode == "mono": stroke, g = "currentColor", None
    else: stroke, g = "#FFFFFF", ("#9A8CFF", "#7B98FF", "#6FD0FF")
    beamfill = f"url(#{p}g)" if g else stroke
    if small:
        sw, x, y, w, h, r, c = 4.8, 13, 4, 38, 54, 6, 13
        cx, cy, ang, half, th, gap = 34, 36, -38, 31, 12, 3.2
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
    body.append(f'<g mask="url(#{p}mk)"><path d="{sp}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>{fold}</g>')
    body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{beamfill}" stroke-width="{th}" stroke-linecap="round"/>')
    if not small:   # sợi chỉ mảnh phía chưa đọc: độ chính xác
        o = 7.6; sx, sy = -nx*o, -ny*o
        body.append(f'<line x1="{x1+ux*14+sx:.1f}" y1="{y1+uy*14+sy:.1f}" x2="{x2-ux*3+sx:.1f}" y2="{y2-uy*3+sy:.1f}" stroke="{beamfill}" stroke-width="1.3" stroke-linecap="round" opacity="{1 if mode=="mono" else .8}"/>')
    return "".join(defs), "".join(body)

