#!/usr/bin/env python3
"""Ba phương án icon app tránh bị đọc thành ⓘ (review R3, mức Cao 1).
Hệ toạ độ "vùng nhìn thấy" 0..1024 (= ô iOS = vùng 72dp của Android).
Chạy: python3 _src/icons.py  → _src/icon-a|b|c.svg, _src/android-fg-*.svg, _src/android-bg-*.svg"""
import math, pathlib
SRC = pathlib.Path(__file__).resolve().parent
K = math.tan(math.radians(14))

def poly(pts): return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"
def grad(i, stops, x1, y1, x2, y2):
    return (f'<linearGradient id="{i}" gradientUnits="userSpaceOnUse" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + "</linearGradient>")
BLUR = '<filter id="bl" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="40"/></filter>'

def i_upright(cx, top, h, sw):
    """i lụa thẳng: chấm + thân, đầu cắt 14° (y xuống)"""
    r = sw * K; hd = sw * 0.88; gap = sw * 0.36; x0 = cx - sw / 2; bot = top + h
    st_top = top + hd + r + gap + r
    stem = [(x0, bot), (x0 + sw, bot), (x0 + sw, st_top - r / 2), (x0, st_top + r / 2)]
    db = st_top - gap
    dot = [(x0, db + r / 2), (x0 + sw, db - r / 2), (x0 + sw, db - r / 2 - hd), (x0, db + r / 2 - hd)]
    return stem, dot

def ribbon(cx, top, sw, P, n=40):
    """thân i là dải lụa: thẳng xuống rồi vắt cong ra ngoài khung theo bezier P (4 điểm), bề rộng sw"""
    def bz(t):
        a, b, c, d = P
        return tuple((1-t)**3*a[k] + 3*(1-t)**2*t*b[k] + 3*(1-t)*t*t*c[k] + t**3*d[k] for k in (0, 1))
    pts = [bz(i / n) for i in range(n + 1)]; L, R = [], []
    for i, p in enumerate(pts):
        q = pts[min(i + 1, n)]; o = pts[max(i - 1, 0)]
        dx, dy = q[0] - o[0], q[1] - o[1]; m = math.hypot(dx, dy); nx, ny = -dy / m, dx / m
        L.append((p[0] - nx * sw / 2, p[1] - ny * sw / 2)); R.append((p[0] + nx * sw / 2, p[1] + ny * sw / 2))
    r = sw * K
    # đầu trên cắt 14°: mép trái thấp hơn, mép phải cao hơn
    L[0] = (L[0][0], L[0][1] + r / 2); R[0] = (R[0][0], R[0][1] - r / 2)
    # L/R theo hướng đi xuống: L là mép phải hình (nx âm) → sắp lại
    a, b = (L, R) if L[0][0] < R[0][0] else (R, L)
    return a + b[::-1]

# ---------- A · Giấy: i lụa màu trên nền giấy ấm, lệch trái, vệt khói lụa chéo
def icon_a(fg_only=False, bg_only=False):
    stem, dot = i_upright(430, 200, 640, 150)
    defs = (grad("as", [(0, "#3A4EE3"), (1, "#1B2491")], 0, 330, 0, 840) + grad("ad", [(0, "#5A6CF0"), (1, "#3D51E6")], 0, 200, 0, 330)
            + grad("ab", [(0, "#FFFFFF"), (1, "#F1EEE7")], 0, 0, 1024, 1024) + BLUR)
    bg = ('<rect x="-400" y="-400" width="1824" height="1824" fill="url(#ab)"/>'
          '<g filter="url(#bl)"><path d="M380 1200C520 900 760 760 1300 520L1300 760C900 900 700 1050 640 1300Z" fill="#C9D1FF" opacity=".75"/>'
          '<path d="M560 1250C700 980 900 860 1300 700L1300 820C1000 960 820 1100 760 1300Z" fill="#E7A9CF" opacity=".35"/></g>')
    fg = f'<path fill="url(#as)" d="{poly(stem)}"/><path fill="url(#ad)" d="{poly(dot)}"/>'
    return defs, ("" if fg_only else bg), ("" if bg_only else fg)

# ---------- B · Lụa vắt: i lớn lệch phải, thân thành dải lụa vắt cong ra khỏi khung
def icon_b(fg_only=False, bg_only=False):
    sw = 190; cx = 560; r = sw * K
    band = ribbon(cx, 0, sw, [(cx, 450), (cx, 760), (cx + 40, 980), (cx + 520, 1260)])
    db = 450 - 66; hd = 166; x0 = cx - sw / 2
    dot = [(x0, db + r / 2), (x0 + sw, db - r / 2), (x0 + sw, db - r / 2 - hd), (x0, db + r / 2 - hd)]
    defs = (grad("bt", [(0, "#4C5FEE"), (.55, "#2F43DB"), (1, "#141C70")], 0, 0, 1024, 1024)
            + grad("bs", [(0, "#FFFFFF"), (.45, "#DDE3FF"), (1, "#9AA8FF")], 0, 450, 400, 1200)
            + grad("bd", [(0, "#F4F6FF"), (1, "#C4CDFF")], 0, 190, 0, 390) + BLUR)
    bg = ('<rect x="-400" y="-400" width="1824" height="1824" fill="url(#bt)"/>'
          '<g filter="url(#bl)" opacity=".55"><path d="M-100 720C150 600 330 660 520 420C640 270 820 160 1200 60L1200 260C900 360 760 520 600 720C400 960 120 920 -100 1020Z" fill="#7C8FFF"/>'
          '<path d="M-100 240C120 260 300 90 480 -100L680 -100C500 120 340 360 -100 420Z" fill="#B7A6FF" opacity=".5"/></g>')
    fg = (f'<path fill="url(#bs)" d="{poly(band)}"/><path fill="url(#bd)" d="{poly(dot)}"/>'
          # vệt sáng mảnh dọc thân: gợi mặt lụa bóng
          f'<path d="M{x0+38:.0f} 470 L{x0+60:.0f} 465 C{x0+60:.0f} 780 {x0+110:.0f} 960 {x0+430:.0f} 1160 L{x0+380:.0f} 1170 C{x0+70:.0f} 980 {x0+38:.0f} 790 {x0+38:.0f} 470Z" fill="#fff" opacity=".35"/>')
    return defs, ("" if fg_only else bg), ("" if bg_only else fg)

# ---------- C · Nền lụa: gradient lụa nhiều sắc (neo xanh), i lụa mực-cobalt, không trắng phẳng
def icon_c(fg_only=False, bg_only=False):
    stem, dot = i_upright(512, 196, 632, 150)
    defs = (grad("cb", [(0, "#E6EAF8"), (.45, "#AEB9FF"), (1, "#6F82FF")], 0, 0, 1024, 1024)
            + grad("cs", [(0, "#1B2491"), (1, "#0E1442")], 0, 330, 0, 830) + grad("cd", [(0, "#2F43DB"), (1, "#2F43DB")], 0, 0, 0, 1) + BLUR)
    bg = ('<rect x="-400" y="-400" width="1824" height="1824" fill="url(#cb)"/>'
          '<g filter="url(#bl)"><path d="M-200 900C200 700 500 820 800 520C950 380 1100 330 1300 260L1300 520C1000 620 900 760 700 960C450 1200 100 1150 -200 1200Z" fill="#7B55FF" opacity=".45"/>'
          '<path d="M-200 380C150 420 420 220 640 -100L860 -100C650 200 420 520 -200 560Z" fill="#FFFFFF" opacity=".6"/>'
          '<path d="M600 1300C760 1100 980 1000 1300 940L1300 1100C1050 1150 900 1220 820 1300Z" fill="#E24C9A" opacity=".35"/></g>')
    fg = f'<path fill="url(#cs)" d="{poly(stem)}"/><path fill="url(#cd)" d="{poly(dot)}"/>'
    return defs, ("" if fg_only else bg), ("" if bg_only else fg)

def full(fn):
    d, bg, fg = fn(); return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs>{d}</defs>{bg}{fg}</svg>'
def android(fn, layer):
    """432×432 (108dp): vùng nhìn thấy 72dp = ô 288 ở giữa → toạ độ icon × 288/1024, dịch 72"""
    d, bg, fg = fn(fg_only=(layer == "fg"), bg_only=(layer == "bg"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432"><defs>{d}</defs>'
            f'<g transform="translate(72 72) scale({288/1024:.5f})">{bg}{fg}</g></svg>')

if __name__ == "__main__":
    for k, fn in (("a", icon_a), ("b", icon_b), ("c", icon_c)):
        (SRC / f"icon-{k}.svg").write_text(full(fn))
        (SRC / f"android-fg-{k}.svg").write_text(android(fn, "fg"))
        (SRC / f"android-bg-{k}.svg").write_text(android(fn, "bg"))
    print("ok")
