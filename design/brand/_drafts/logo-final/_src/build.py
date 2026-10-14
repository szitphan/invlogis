#!/usr/bin/env python3
"""Dựng bộ logo Invlogis × innvie bản hoàn thiện (hướng A · Lụa, chữ v vẽ lại — DEC-072, v gradient phương án 1 — DEC-073).
Mọi chữ đổi thành nét vector (không thẻ <text>). Chạy: python3 _src/build.py
Nguồn font: _src/LexendVF.ttf (OFL, trục wght), _src/BeVietnamPro-*.ttf (OFL)."""
import pathlib, math, io, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen

SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC.parent
WGHT = 340            # Lexend 340: nét thân 87/1000 em (Light 300 = 75, Regular 400 = 103)
TRACK = 20            # +20/1000 em
K = math.tan(math.radians(14))   # góc cắt nếp gấp 14°

# --- màu (giữ bảng A · Lụa) ---
INK = "#0E1442"; COBALT = "#2F43DB"; NIGHT = "#0B1033"; PAPER = "#FAF8F4"; SMOKE = "#E6EAF8"; SLATE = "#4A5380"
LIGHT_STEM = [(0, "#3A4EE3"), (1, "#1B2491")]      # thân i trên nền sáng
LIGHT_DOT = [(0, "#5A6CF0"), (1, "#3D51E6")]       # nếp gấp (mặt sau lụa, sáng hơn)
DARK_STEM = [(0, "#A3B0FF"), (1, "#5B6EF5")]       # trên nền tối
DARK_DOT = [(0, "#D6DCFF"), (1, "#AEB9FF")]

# ---------------------------------------------------------------- font
_fonts = {}
def font(path, wght=None):
    key = (path, wght)
    if key in _fonts: return _fonts[key]
    p = str(SRC / path); tt = TTFont(p)
    hbf = hb.Font(hb.Face(hb.Blob.from_file_path(p)))
    if wght and "fvar" in tt:
        hbf.set_variations({"wght": wght})
        tt = instancer.instantiateVariableFont(tt, {"wght": wght})
    _fonts[key] = (tt, tt.getGlyphSet(), hbf); return _fonts[key]
LEX = lambda: font("LexendVF.ttf", WGHT)

def shape(fk, text, tracking=0):
    tt, gs, hbf = fk; upm = tt["head"].unitsPerEm
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(hbf, buf)
    order = tt.getGlyphOrder(); x = 0; out = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        out.append(dict(cl=info.cluster, g=order[info.codepoint], x=x + pos.x_offset, y=pos.y_offset, adv=pos.x_advance))
        x += pos.x_advance + tracking * upm / 1000
    return out, x - tracking * upm / 1000

class Box:
    def __init__(s): s.b = None
    def add(s, b):
        if b is None: return
        s.b = b if s.b is None else (min(s.b[0], b[0]), min(s.b[1], b[1]), max(s.b[2], b[2]), max(s.b[3], b[3]))
    def pts(s, pts): s.add((min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts)))

def glyph_d(gs, g, dx, base, sc=1.0, dy=0, box=None):
    """glyph → path d ở hệ y-xuống; gốc chữ tại (dx, base)"""
    t = (sc, 0, 0, -sc, dx, base - dy * sc)
    pen = SVGPathPen(gs); gs[g].draw(TransformPen(pen, t))
    if box is not None:
        bp = BoundsPen(gs); gs[g].draw(TransformPen(bp, t)); box.add(bp.bounds)
    return pen.getCommands()

def poly_d(pts): return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "Z"
def xf(pts, dx, base, sc=1.0): return [(dx + x * sc, base - y * sc) for x, y in pts]

# ---------------------------------------------------------------- hình học
def i_metrics():
    tt, gs, _ = LEX(); cm = tt.getBestCmap()
    bp = BoundsPen(gs); gs[cm[0x131]].draw(bp); x0, _, x1, T = bp.bounds
    rp = RecordingPen(); gs[cm[ord("i")]].draw(rp)
    ys = [pt[1] for op, a in rp.value for pt in a if pt[1] > T + 1]
    return dict(x0=x0, S=x1 - x0, T=T, yc=(min(ys) + max(ys)) / 2)

def lua_i(x0, S, T, yc, hdot=None):
    """chữ i lụa (y-lên, gốc baseline): thân có đầu cắt 14°, chấm là mảnh lụa gấp, cạnh song song."""
    r = S * K; h = hdot or S * 1.38
    stem = [(x0, 0), (x0 + S, 0), (x0 + S, T + r / 2), (x0, T - r / 2)]
    dot = [(x0, yc - h / 2 - r / 2), (x0 + S, yc - h / 2 + r / 2), (x0 + S, yc + h / 2 + r / 2), (x0, yc + h / 2 - r / 2)]
    return stem, dot

def v_poly(cut=False):
    """chữ v Lexend (đa giác 8 điểm). cut=True: đầu hai cánh cắt 14° song song nếp chấm i."""
    tt, gs, _ = LEX(); cm = tt.getBestCmap()
    rp = RecordingPen(); gs[cm[ord("v")]].draw(rp)
    P = [a[0] for op, a in rp.value if op in ("moveTo", "lineTo")]
    if not cut: return P
    # P: 0 đáy trái, 1 đỉnh ngoài cánh trái, 2 đỉnh trong cánh trái, 3,4 khe giữa, 5 đỉnh trong cánh phải, 6 đỉnh ngoài cánh phải, 7 đáy phải
    def inter(a, b, p, slope):  # giao đoạn a-b với đường y = p.y + slope*(x-p.x)
        (ax, ay), (bx, by) = a, b
        f = lambda t: (ay + t * (by - ay)) - (p[1] + slope * (ax + t * (bx - ax) - p[0]))
        t = f(0) / (f(0) - f(1)); return (ax + t * (bx - ax), ay + t * (by - ay))
    Q = list(P)
    Q[1] = inter(P[0], P[1], P[2], K)      # cánh trái: giữ góc trong, hạ góc ngoài
    Q[5] = inter(P[4], P[5], P[6], K)      # cánh phải: giữ góc ngoài, hạ góc trong
    return Q

def grad(gid, stops, x1, y1, x2, y2):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}">{s}</linearGradient>'

_gid = [0]
def lua_i_svg(stem, dot, dx, base, sc, scheme, cls=""):
    """scheme: 'light' | 'dark' | màu đặc '#xxxxxx' | (màu thân, màu chấm)"""
    S_ = xf(stem, dx, base, sc); D_ = xf(dot, dx, base, sc)
    c = f' class="{cls}"' if cls else ""
    if scheme in ("light", "dark"):
        _gid[0] += 1; n = _gid[0]
        st, dt = (LIGHT_STEM, LIGHT_DOT) if scheme == "light" else (DARK_STEM, DARK_DOT)
        top = min(p[1] for p in S_); bot = max(p[1] for p in S_); xl = min(p[0] for p in S_); xr = max(p[0] for p in S_)
        dtop = min(p[1] for p in D_); dbot = max(p[1] for p in D_)
        defs = grad(f"s{n}", st, xr, top, xl, bot) + grad(f"d{n}", dt, xl, dtop, xr, dbot)
        return (defs, f'<path{c} data-part="stem" fill="url(#s{n})" d="{poly_d(S_)}"/><path{c} data-part="dot" fill="url(#d{n})" d="{poly_d(D_)}"/>', S_ + D_)
    sf, df = scheme if isinstance(scheme, tuple) else (scheme, scheme)
    return ("", f'<path{c} data-part="stem" fill="{sf}" d="{poly_d(S_)}"/><path{c} data-part="dot" fill="{df}" d="{poly_d(D_)}"/>', S_ + D_)

# ---------------------------------------------------------------- chữ
def word(text, dx=0, base=0, sc=1.0, fill=INK, first_i=None, vmode="plain", vfill=None, tracking=TRACK, fk=None, wrap_letters=False):
    """first_i: None (i Lexend) | scheme cho chữ i lụa đầu tiên. vmode: plain | grad | cut."""
    fk = fk or LEX(); tt, gs, _ = fk; items, W = shape(fk, text, tracking)
    defs, parts, box = [], [], Box(); m = i_metrics() if fk is LEX() else None
    done_i = False
    for k, it in enumerate(items):
        ch = text[it["cl"]]; gx = dx + it["x"] * sc
        if ch == "i" and first_i is not None and not done_i and m:
            done_i = True
            st, dt = lua_i(m["x0"], m["S"], m["T"], m["yc"] + 4)
            d_, p_, pts = lua_i_svg(st, dt, gx, base, sc, first_i, "lt" if wrap_letters else "")
            defs.append(d_); parts.append(p_.replace('class="lt"', 'class="ii"')); box.pts(pts); continue
        if ch == "v" and m and vmode in ("grad", "cut"):
            poly = xf(v_poly(cut=(vmode == "cut")), gx, base, sc); box.pts(poly)
            f = vfill or fill
            if vmode == "grad" and not f.startswith("#000"):   # nền sáng: mực → cobalt; nền tối: trắng → periwinkle
                _gid[0] += 1; n = _gid[0]; top = min(p[1] for p in poly); bot = max(p[1] for p in poly)
                defs.append(grad(f"v{n}", [(0, fill), (1, COBALT if fill == INK else "#A3B0FF")], 0, top, 0, bot)); f = f"url(#v{n})"
            parts.append(f'<path{LT if wrap_letters else ""} fill="{f}" d="{poly_d(poly)}"/>'); continue
        d = glyph_d(gs, it["g"], gx, base, sc, it["y"], box)
        if d: parts.append(f'<path{LT if wrap_letters else ""} fill="{fill}" d="{d}"/>')
    return "".join(defs), "".join(parts), W * sc, box.b

def svg(content, box, pad=0, defs="", bg=None, extra_attr=""):
    x0, y0, x1, y1 = box; x0 -= pad; y0 -= pad; x1 += pad; y1 += pad
    b = f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1-x0:.1f}" height="{y1-y0:.1f}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.1f} {y0:.1f} {x1-x0:.1f} {y1-y0:.1f}"{extra_attr}>'
            f'{"<defs>"+defs+"</defs>" if defs else ""}{b}{content}</svg>')

def union(*bs):
    B = Box(); [B.add(b) for b in bs]; return B.b

# ---------------------------------------------------------------- biến thể
LT = ' class="lt"'
BASE = 800   # baseline ở hệ chữ (1000 upm), y-xuống

def wordmark(scheme="color", vmode=None, wrap=False):
    """vmode mặc định: gradient (phương án 1, DEC-073) cho bản màu; bản đơn sắc giữ v một màu."""
    if vmode is None: vmode = "plain" if scheme in ("black", "white") else "grad"
    if scheme == "color":   fill, fi = INK, "light"
    elif scheme == "reverse": fill, fi = "#FFFFFF", "dark"
    elif scheme == "black": fill, fi = "#000000", "#000000"
    elif scheme == "white": fill, fi = "#FFFFFF", "#FFFFFF"
    elif scheme == "ink":   fill, fi = INK, INK
    return word("invlogis", 0, BASE, 1, fill, fi, vmode, wrap_letters=wrap)

def innvie(fill=INK, dot=COBALT, sc=1.0, dx=0, base=BASE):
    return word("innvie", dx, base, sc, fill, (fill, dot), "plain")

def text_line(fontfile, text, dx, base, size, fill, wght=None, tracking=0):
    fk = font(fontfile, wght); tt, gs, _ = fk; upm = tt["head"].unitsPerEm; sc = size / upm
    items, W = shape(fk, text, tracking); box = Box(); parts = []
    for it in items:
        d = glyph_d(gs, it["g"], dx + it["x"] * sc, base, sc, it["y"], box)
        if d: parts.append(d)
    return f'<path fill="{fill}" d="{" ".join(parts)}"/>', W * sc, box.b

def lockup_by(scheme="color"):
    d, p, W, b = wordmark(scheme)
    col = {"color": (INK, COBALT, SLATE), "reverse": ("#FFFFFF", "#AEB9FF", "#C4CDFF"), "black": ("#000",) * 3, "white": ("#FFF",) * 3}[scheme]
    sc = 0.30; base2 = b[3] + 60 + 0.76 * 1000 * sc     # dưới đuôi g một khoảng, cỡ 30% chữ chính
    dI, pI, wI, bI = innvie(col[0], col[1], sc, 0, base2)
    pb, wb, bb = text_line("LexendVF.ttf", "by", 0, base2, 1000 * sc, col[2], WGHT)
    gap = 0.26 * 1000 * sc
    # căn phải theo cạnh phải chữ s
    xI = b[2] - bI[2]; xb = xI + bI[0] - gap - bb[2]
    pI = f'<g transform="translate({xI:.1f} 0)">{pI}</g>'; pb = f'<g transform="translate({xb:.1f} 0)">{pb}</g>'
    box = union(b, (bI[0] + xI, bI[1], bI[2] + xI, bI[3]), (bb[0] + xb, bb[1], bb[2] + xb, bb[3]))
    return svg(p + pb + pI, box, 0, d + dI)

def lockup_tagline(scheme="color", text="Khai mở cách vận hành mới."):
    d, p, W, b = wordmark(scheme)
    col = SLATE if scheme == "color" else "#C4CDFF"
    pt, wt, bt = text_line("BeVietnamPro-400.ttf", text, b[0] + 4, b[3] + 330, 210, col)
    return svg(p + pt, union(b, bt), 0, d)

def lockup_stacked():
    m = i_metrics(); st, dt = lua_i(m["x0"], m["S"], m["T"], m["yc"] + 4)
    d, p, W, b = wordmark("ink")
    sc = 1.55; cx = (b[0] + b[2]) / 2; ix = cx - (m["x0"] + m["S"] / 2) * sc
    top_base = b[1] - 230
    dS, pS, pts = lua_i_svg(st, dt, ix, top_base, sc, "light")
    B = Box(); B.pts(pts)
    return svg(pS + p, union(b, B.b), 0, dS + d)

def symbol(scheme="light", pad=40):
    m = i_metrics(); st, dt = lua_i(m["x0"], m["S"], m["T"], m["yc"] + 4)
    dS, pS, pts = lua_i_svg(st, dt, 0, BASE, 1, scheme); B = Box(); B.pts(pts)
    return svg(pS, B.b, pad, dS)

# ---------------------------------------------------------------- favicon + icon (bản tối ưu cỡ nhỏ: cùng hình, thân dày hơn)
def icon_i(cx, top, height, stem_ratio=0.30, scheme="light", ids="f"):
    """i lụa tối ưu cỡ nhỏ: thân rộng = stem_ratio × chiều cao; chấm vuông lệch 14°."""
    S = height * stem_ratio; r = S * K; hd = S * 0.88; gap = S * 0.36
    x0 = cx - S / 2; bot = top + height
    stem_top = top + hd + r + gap + r   # y-xuống
    stem = [(x0, bot), (x0 + S, bot), (x0 + S, stem_top - r / 2), (x0, stem_top + r / 2)]
    dt_b = stem_top - gap
    dot = [(x0, dt_b + r / 2), (x0 + S, dt_b - r / 2), (x0 + S, dt_b - r / 2 - hd), (x0, dt_b + r / 2 - hd)]
    return stem, dot

def favicon_svg(px=32):
    if px == 16:   # vẽ khớp lưới điểm ảnh
        stem = [(6, 15), (10, 15), (10, 8), (6, 9)]; dot = [(6, 6.5), (10, 5.5), (10, 1.5), (6, 2.5)]; vb = 16
    else:
        stem = [(11, 31), (21, 31), (21, 13.5), (11, 16)]; dot = [(11, 12.5), (21, 10), (21, 1.5), (11, 4)]; vb = 32
    css = ('<style>.s{fill:url(#fs)}.d{fill:url(#fd)}@media (prefers-color-scheme:dark){.s{fill:#A3B0FF}.d{fill:#D6DCFF}}</style>')
    # màu đặc, chọn để đạt ≥3:1 trên cả tab sáng (#FAF8F4/#FFF) lẫn tab tối (#202124)
    defs = (grad("fs", [(0, "#4F62EE"), (1, "#4F62EE")], 0, 0, 0, vb) + grad("fd", [(0, "#6577F2"), (1, "#6577F2")], 0, 0, 0, vb))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb} {vb}"><defs>{defs}</defs>{css}'
            f'<path class="s" d="{poly_d(stem)}"/><path class="d" d="{poly_d(dot)}"/></svg>')

def appicon_svg(transparent=False, size=1024, i_height=0.64):
    s = size; st, dt = icon_i(s / 2, s * (1 - i_height) / 2, s * i_height, 0.2)
    bg = "" if transparent else (
        '<rect width="{s}" height="{s}" fill="url(#t)"/><rect width="{s}" height="{s}" fill="url(#h)"/>'
        '<g filter="url(#bl)" opacity=".55"><path d="M-80 760C200 600 420 700 700 380C820 250 960 200 1100 120L1100 330C900 420 800 560 620 760C420 980 150 900 -80 1000Z" fill="#7C8FFF"/>'
        '<path d="M-80 300C160 330 360 120 560 -60L760 -60C560 160 380 420 -80 480Z" fill="#A9B7FF" opacity=".6"/></g>').replace("{s}", "1024")
    defs = ('<linearGradient id="t" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4C5FEE"/><stop offset=".55" stop-color="#2F43DB"/><stop offset="1" stop-color="#141C70"/></linearGradient>'
            '<radialGradient id="h" cx=".2" cy=".1" r=".9"><stop offset="0" stop-color="#9FB0FF" stop-opacity=".5"/><stop offset="1" stop-color="#9FB0FF" stop-opacity="0"/></radialGradient>'
            '<filter id="bl" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="38"/></filter>'
            + grad("is", [(0, "#FFFFFF"), (1, "#DCE2FF")], 0, 0, 0, 1024) + grad("id", [(0, "#E9EDFF"), (1, "#C4CDFF")], 0, 0, 0, 1024))
    k = 1024 / s
    stem = [(x * k, y * k) for x, y in st]; dot = [(x * k, y * k) for x, y in dt]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs>{defs}</defs>{bg}'
            f'<path fill="url(#is)" d="{poly_d(stem)}"/><path fill="url(#id)" d="{poly_d(dot)}"/></svg>')

def android_fg_svg():
    # 432×432, vùng an toàn 66% (đường kính 285) ở giữa: i cao 260 (rộng 52) nằm gọn trong vòng tròn an toàn
    st, dt = icon_i(216, 216 - 130, 260, 0.2)
    defs = grad("is", [(0, "#FFFFFF"), (1, "#DCE2FF")], 0, 86, 0, 346) + grad("id", [(0, "#E9EDFF"), (1, "#C4CDFF")], 0, 86, 0, 346)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432"><defs>{defs}</defs>'
            f'<path fill="url(#is)" d="{poly_d(st)}"/><path fill="url(#id)" d="{poly_d(dt)}"/></svg>')

# ---------------------------------------------------------------- ghi
def W(name, s): (OUT / name).write_text(s); return OUT / name

if __name__ == "__main__":
    for sch, name in [("color", "primary"), ("reverse", "reverse"), ("black", "mono-black"), ("white", "mono-white")]:
        d, p, w, b = wordmark(sch); W(f"invlogis-{name}.svg", svg(p, b, 16, d))
    W("invlogis-symbol.svg", symbol("light")); W("invlogis-symbol-mono.svg", symbol("#000000"))
    W("invlogis-symbol-reverse.svg", symbol("dark"))
    W("invlogis-by-innvie.svg", lockup_by("color")); W("invlogis-by-innvie-reverse.svg", lockup_by("reverse"))
    W("invlogis-stacked.svg", lockup_stacked())
    W("invlogis-tagline.svg", lockup_tagline()); W("invlogis-tagline-en.svg", lockup_tagline(text="Open a new way to operate."))
    d, p, w, b = innvie(); W("innvie-logo.svg", svg(p, b, 0, d))
    d, p, w, b = innvie("#000000", "#000000"); W("innvie-logo-mono.svg", svg(p, b, 0, d))
    W("favicon.svg", favicon_svg(32)); (SRC / "favicon-16.svg").write_text(favicon_svg(16))
    # icon app: xem _src/icons.py (phương án B, sửa theo R3)
    # 3 phương án v (để dựng v-options)
    for k, vm in [(1, "grad"), (2, "cut"), (3, "plain")]:
        d, p, w, b = wordmark("color", vm); (SRC / f"v{k}.svg").write_text(svg(p, b, 0, d))
        d, p, w, b = wordmark("black", vm); (SRC / f"v{k}-mono.svg").write_text(svg(p, b, 0, d))
    # bản có class cho logo động
    d, p, w, b = wordmark("color", wrap=True); (SRC / "motion-logo.svg").write_text(svg(p, b, 0, d))
    print("ok", i_metrics())
