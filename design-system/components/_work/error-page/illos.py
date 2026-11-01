"""Bộ minh hoạ trang lỗi / không có dữ liệu — theo mẫu Figma Test 1209:1060 (thư mục mặt buồn).
Ngôn ngữ: nét xám than 2px đầu tròn · mảng tím xám nhạt + mặt khuất đậm hơn · đúng 1 chấm nhấn cam trong huy hiệu tròn ·
đồ vật có mặt (mắt X / chấm, miệng) · chi tiết phụ: khói lượn, vòng nhỏ, đường chấm, tia góc.
Màu qua biến CSS (--il-*) để đổi Light/Dark; SVG dùng class, không mã màu trong hình.
"""

CSS = r"""
.il{--il-badge:var(--color-bg-warning-secondary);display:block;overflow:visible;--il-st:var(--color-fg-tertiary);--il-f0:var(--color-bg-primary);--il-f1:var(--color-bg-quaternary);--il-f2:var(--color-border-primary);--il-acc:var(--color-fg-warning-primary);--il-dot:var(--color-fg-quaternary)}
.pv[data-theme=dark] .il{--il-st:var(--color-fg-tertiary);--il-f0:var(--color-bg-primary);--il-f1:var(--color-bg-quaternary);--il-f2:var(--color-border-primary);--il-acc:var(--color-fg-warning-primary);--il-dot:var(--color-fg-quaternary)}
.il *{stroke:var(--il-st);stroke-width:2;stroke-linecap:round;stroke-linejoin:round;fill:none}
.il .f0{fill:var(--il-f0)}.il .fb{fill:var(--il-badge,var(--il-f0))}.il .f1{fill:var(--il-f1)}.il .f2{fill:var(--il-f2)}
.il .k{fill:var(--il-st);stroke:none}
.il .a{stroke:var(--il-acc);stroke-width:3}.il .ka{fill:var(--il-acc);stroke:none}
.il .d{stroke:var(--il-dot);stroke-dasharray:0 4.5}
.il .t{stroke-width:1.6}
.il .w{stroke-width:2.6}
.il.line .f1,.il.line .f2,.il-line .il .f1,.il-line .il .f2{fill:var(--il-f0)}
.il.ok{--il-acc:var(--color-fg-success-primary);--il-badge:var(--color-bg-success-secondary)}.il.err{--il-acc:var(--color-fg-error-primary);--il-badge:var(--color-bg-error-secondary)}
.pv[data-theme=dark] .il.ok{--il-acc:var(--color-fg-success-primary);--il-badge:var(--color-bg-success-secondary)}.pv[data-theme=dark] .il.err{--il-acc:var(--color-fg-error-primary);--il-badge:var(--color-bg-error-secondary)}
"""


def svg(body, label, tone=""):
    return (f'<svg class="il {tone}" viewBox="0 0 128 120" width="128" height="120" role="img" aria-label="{label}">'
            f'{body}</svg>')


# ---- mảnh dùng chung ----
def xeyes(cx, cy, gap=14, r=3.2):
    out = ""
    for x in (cx - gap / 2, cx + gap / 2):
        out += f'<path class="w" d="M{x - r} {cy - r}l{2 * r} {2 * r}M{x + r} {cy - r}l{-2 * r} {2 * r}"/>'
    return out


def doteyes(cx, cy, gap=14, r=2.2):
    return "".join(f'<circle class="k" cx="{x}" cy="{cy}" r="{r}"/>' for x in (cx - gap / 2, cx + gap / 2))


def closed(cx, cy, gap=14, r=3):
    return "".join(f'<path class="w" d="M{x - r} {cy}q{r} {r * .9} {2 * r} 0"/>' for x in (cx - gap / 2, cx + gap / 2))


def frown(cx, cy, w=16):
    return f'<path class="w" d="M{cx - w / 2} {cy + 3}q{w / 2} -7 {w} 0"/>'


def flat(cx, cy, w=10):
    return f'<path class="w" d="M{cx - w / 2} {cy}h{w}"/>'


def ohh(cx, cy, r=2.6):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * 1.2}"/>'


def badge(cx, cy, inner, r=13):
    return f'<circle class="fb" cx="{cx}" cy="{cy}" r="{r}"/>{inner}'


def qmark(cx, cy):
    return (f'<path class="a" d="M{cx - 4.5} {cy - 4}a4.5 4.5 0 1 1 6.5 4c-1.4.8-2 1.6-2 3.2"/>'
            f'<circle class="ka" cx="{cx}" cy="{cy + 7.5}" r="1.9"/>')


def smoke(x, y, h=18):
    return f'<path class="t" d="M{x} {y}c-4-4 4-6 0-10s4-6 0-{h - 10}"/>'


def rings(*pts):
    return "".join(f'<circle class="t" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in pts)


def burst(x, y):
    return f'<path class="t" d="M{x} {y}l-7 2M{x + 2} {y + 4}l-4 6M{x + 7} {y + 6}v7"/>'


def dots(d):
    return f'<path class="d" d="{d}"/>'


# ---- 1. 404 · không tìm thấy (sát mẫu nhất) ----
def not_found():
    b = (smoke(34, 30) + smoke(50, 24, 22) + smoke(64, 32, 16)
         + rings((96, 18, 3.2), (86, 26, 2))
         + '<path class="f2" d="M24 50l2-8a3 3 0 0 1 3-2h18l6 7h44a3 3 0 0 1 3 3v46H24z"/>'
         + '<path class="f1" d="M14 52a3 3 0 0 1 3-3h20l6 7h46a3 3 0 0 1 3 3l-6 42a3 3 0 0 1-3 2.6H23a3 3 0 0 1-3-2.6z"/>'
         + xeyes(46, 76) + frown(46, 88)
         + dots("M70 92h26M104 70v22")
         + badge(104, 50, qmark(104, 50)) + burst(8, 104))
    return svg(b, "Thư mục không tìm thấy")


# ---- 2. Không có quyền · ổ khoá ----
def forbidden():
    b = (rings((22, 22, 3), (32, 14, 2))
         + '<path class="f2" d="M40 50V38a24 24 0 0 1 48 0v12h-9V38a15 15 0 0 0-30 0v12z"/>'
         + '<rect class="f1" x="30" y="50" width="68" height="50" rx="8"/>'
         + '<path class="t" d="M30 60h68" opacity=".5"/>'
         + closed(64, 74, 18) + flat(64, 86, 12)
         + dots("M98 92h14M14 60v26")
         + badge(104, 36, '<circle class="a" cx="104" cy="36" r="6.5"/><path class="a" d="M99.5 40.5l9-9"/>')
         + burst(14, 102))
    return svg(b, "Ổ khoá không có quyền")


# ---- 3. Lỗi hệ thống · máy chủ bốc khói ----
def server_error():
    b = (smoke(44, 22) + smoke(58, 18, 20) + smoke(72, 24)
         + rings((28, 28, 2.5))
         + '<rect class="f2" x="30" y="40" width="68" height="22" rx="5"/>'
         + '<rect class="f1" x="30" y="62" width="68" height="40" rx="5"/>'
         + '<circle class="k" cx="40" cy="51" r="2"/><circle class="k" cx="48" cy="51" r="2"/><path class="t" d="M70 51h20"/>'
         + xeyes(64, 76, 16) + frown(64, 89)
         + '<path class="t" d="M38 102v6M90 102v6M30 108h68"/>'
         + dots("M98 84h16")
         + badge(106, 34, '<path class="a" d="M108 26l-6 9h6l-4 9" style="stroke-width:2.6"/>')
         + burst(16, 96))
    return svg(b, "Máy chủ gặp sự cố")


# ---- 4. Mất kết nối · đám mây + sóng wifi gạch ----
def offline():
    b = (rings((18, 24, 3), (108, 96, 2.4))
         + '<path class="f1" d="M30 74a16 16 0 0 1 4-31 22 22 0 0 1 42-6 18 18 0 0 1 22 18 12 12 0 0 1-2 24H36a12 12 0 0 1-6-5z"/>'
         + doteyes(64, 56, 16) + ohh(64, 66)
         + '<path class="t" d="M46 92a26 26 0 0 1 36 0M52 99a16 16 0 0 1 24 0"/><circle class="k" cx="64" cy="106" r="2.4"/>'
         + dots("M14 60v24")
         + badge(102, 30, '<path class="a" d="M96 24l12 12M108 24l-12 12"/>')
         + burst(18, 100))
    return svg(b, "Đám mây mất kết nối")


# ---- 5. Bảo trì · container ngủ + cờ lê ----
def maintenance():
    b = ('<path class="t" d="M72 24h6l-6 7h6M82 12h8l-8 9h8"/>'
         + '<path class="f2" d="M20 48l8-8h70l-8 8z"/>'
         + '<rect class="f1" x="20" y="48" width="70" height="46" rx="3"/>'
         + '<path class="f2" d="M90 48l8-8v46l-8 8z"/>'
         + '<path class="t" d="M30 54v34M38 54v34M72 54v34M80 54v34" opacity=".55"/>'
         + closed(55, 66, 14) + '<path class="w" d="M51 78q4 3 8 0"/>'
         + '<path class="f1" d="M104 96l6-26h4l6 26z"/><path class="t" d="M106 86h12M108 78h8M100 96h24"/>'
         + dots("M20 100h70")
         + badge(30, 24, '<path class="a" d="M34 18a5 5 0 0 0-6.5 6.5L22 30l2 2 5.5-5.5A5 5 0 0 0 36 20l-3 3-2.5-.5-.5-2.5z" style="stroke-width:2.2"/>'))
    return svg(b, "Container đang bảo trì")


# ---- 6. Không có dữ liệu · thùng hàng rỗng ----
def empty_box():
    b = (rings((96, 16, 3), (106, 26, 2)) + '<path class="t" d="M30 20l2 6M24 26l6 2M38 18l-1 6"/>'
         + '<path class="f2" d="M28 52l36-12 36 12-36 12z"/>'
         + '<path class="f1" d="M28 52v38l36 14V64z"/><path class="f2" d="M100 52v38l-36 14V64z"/>'
         + '<path class="f1" d="M28 52l-10 12 36 12 10-12zM100 52l10 12-36 12-10-12z"/>'
         + doteyes(44, 84, 12) + '<path class="w" d="M40 94q4-2 8 0"/>'
         + dots("M8 104h20M112 98h10")
         + '<path class="ka" d="M64 22l2.2 5.8L72 30l-5.8 2.2L64 38l-2.2-5.8L56 30l5.8-2.2z"/>')
    return svg(b, "Thùng hàng rỗng")


# ---- 7. Danh sách trống · bảng kẹp giấy ----
def empty_list():
    b = (rings((20, 20, 3), (110, 100, 2.4))
         + '<rect class="f1" x="30" y="22" width="60" height="82" rx="6"/>'
         + '<rect class="f2" x="46" y="16" width="28" height="12" rx="4"/>'
         + '<path class="d" d="M42 44h36M42 54h28M42 64h32"/>'
         + doteyes(60, 80, 14) + flat(60, 90, 8)
         + badge(98, 88, '<path class="a" d="M98 82v12M92 88h12"/>', 12)
         + burst(14, 100))
    return svg(b, "Danh sách trống")


# ---- 8. Chưa có lệnh · xe tải chờ ----
def idle_truck():
    b = (rings((104, 16, 3), (94, 24, 2))
         + '<rect class="f1" x="10" y="44" width="62" height="40" rx="4"/>'
         + '<path class="f2" d="M72 56h22l12 14v14H72z"/><path class="t" d="M80 60h12l8 10H80z"/>'
         + doteyes(40, 62, 14) + '<path class="w" d="M36 72q4 2 8 0"/>'
         + '<circle class="f0" cx="28" cy="88" r="8"/><circle class="f0" cx="88" cy="88" r="8"/>'
         + '<path class="t" d="M4 100h120"/>'
         + dots("M14 108h30M70 108h40")
         + '<path class="ka" d="M108 34a7 7 0 0 0-7 7c0 5 7 11 7 11s7-6 7-11a7 7 0 0 0-7-7z"/><circle class="f0" style="stroke:none" cx="108" cy="41" r="2.4"/>'
         + '<path class="d" d="M108 54v-2M100 56c-6 0-8 4-12 0"/>')
    return svg(b, "Xe tải chưa có lệnh")



def happy(cx, cy, gap=14, r=3):
    return "".join(f'<path class="w" d="M{x - r} {cy + 1}q{r} {-r * 1.1} {2 * r} 0"/>' for x in (cx - gap / 2, cx + gap / 2))


def smile(cx, cy, w=14):
    return f'<path class="w" d="M{cx - w / 2} {cy}q{w / 2} 7 {w} 0"/>'


def check(cx, cy):
    return f'<path class="a" d="M{cx - 6} {cy}l4 4.5 8-9"/>'


def bang(cx, cy):
    return f'<path class="a" d="M{cx} {cy - 7}v8"/><circle class="ka" cx="{cx}" cy="{cy + 6}" r="1.9"/>'


def sparks(*pts):
    return "".join(f'<path class="t" d="M{x} {y - 5}v10M{x - 5} {y}h10"/>' for x, y in pts)


# ---- 9. Thành công · thùng hàng đã giao ----
def success_box():
    b = (sparks((22, 26), (116, 64)) + rings((32, 14, 2.4), (74, 22, 2))
         + '<path class="f2" d="M28 50l36-12 36 12-36 12z"/>'
         + '<path class="f1" d="M28 50v40l36 14V62z"/><path class="f2" d="M100 50v40l-36 14V62z"/>'
         + '<path class="t" d="M46 44l36 12v10" opacity=".7"/>'
         + happy(45, 80, 13) + smile(45, 89, 10)
         + dots("M8 106h18M108 102h14")
         + badge(98, 30, check(98, 30)))
    return svg(b, "Thùng hàng giao thành công", "ok")


# ---- 10. Thành công · đã gửi (máy bay giấy tới đích) ----
def success_sent():
    b = (rings((18, 90, 2.4), (110, 96, 3))
         + '<path class="d" d="M14 70c14 10 26 8 36-2"/>'
         + '<path class="f1" d="M50 62l58-32-20 62-16-18z"/><path class="f2" d="M72 74l36-44-30 52z"/>'
         + '<path class="t" d="M72 74l-6 22 12-14"/>'
         + happy(70, 56, 12, 2.6) + smile(72, 64, 8)
         + sparks((24, 30))
         + badge(34, 50, check(34, 50), 12))
    return svg(b, "Đã gửi thành công", "ok")


# ---- 11. Thất bại · gửi không được (tài liệu rách) ----
def failed_doc():
    b = (smoke(84, 24, 16) + rings((22, 20, 3), (32, 30, 2))
         + '<path class="f1" d="M30 26h40l14 14v26l-8 4 6 6-8 4 6 6-6 4v12a4 4 0 0 1-4 4H34a4 4 0 0 1-4-4z"/>'
         + '<path class="f2" d="M70 26v14h14z"/>'
         + '<path class="d" d="M40 46h20M40 56h26"/>'
         + xeyes(54, 74, 14) + frown(54, 86, 14)
         + '<path class="f1" d="M92 80l8-4-4 8 8 2-6 6"/>'
         + badge(102, 46, bang(102, 46))
         + burst(14, 104))
    return svg(b, "Gửi thất bại", "err")


# ---- 12. Thất bại · hàng có sự cố (thùng bẹp, băng dính bung) ----
def failed_box():
    b = (smoke(56, 20, 16) + smoke(68, 26, 14) + rings((100, 16, 3))
         + '<path class="f2" d="M26 54l38-10 38 12-38 10z"/>'
         + '<path class="f1" d="M26 54l2 36 36 14 -2-38z"/><path class="f2" d="M102 56l-4 34-34 14 2-38z"/>'
         + '<path class="t" d="M80 66l6 10-4 6 6 8"/>'
         + xeyes(46, 76, 12) + frown(46, 88, 11)
         + '<path class="f1" d="M60 46l-14-12 6-2 12 10z"/>'
         + dots("M8 108h20M108 106h14")
         + badge(102, 36, bang(102, 36))
         + burst(10, 92))
    return svg(b, "Hàng gặp sự cố", "err")

ALL = [("s404", "404 · Không tìm thấy", not_found), ("s403", "Không có quyền", forbidden),
       ("s500", "Lỗi hệ thống", server_error), ("offline", "Mất kết nối", offline),
       ("maint", "Bảo trì", maintenance), ("box", "Rỗng · thùng hàng", empty_box),
       ("list", "Rỗng · danh sách", empty_list), ("truck", "Rỗng · chưa có lệnh", idle_truck),
       ("ok-box", "Thành công · đã giao", success_box), ("ok-sent", "Thành công · đã gửi", success_sent),
       ("fail-doc", "Thất bại · gửi không được", failed_doc), ("fail-box", "Thất bại · hàng sự cố", failed_box)]

if __name__ == "__main__":
    import sys
    cells = "".join(f'<figure style="margin:0;padding:16px;background:var(--color-bg-primary);border-radius:12px;text-align:center">'
                    f'<div style="display:flex;justify-content:center">{f()}</div><figcaption style="font:13px Inter;margin-top:8px;color:var(--color-text-tertiary)">{l}</figcaption></figure>'
                    for k, l, f in ALL)
    for theme, bg in (("light", "#F5F5F5"), ("dark", "#111")):
        html = (f'<!doctype html><meta charset=utf-8><style>{CSS}body{{margin:0;padding:24px;background:{bg}}}'
                f'.pv{{--bg:{"#fff" if theme == "light" else "#0A0A0A"}}}</style>'
                f'<div class="pv" data-theme="{theme}" style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{cells}</div>')
        open(f"{sys.argv[1]}/sheet-{theme}.html", "w").write(html)
