import sys
# Sinh page.json cho /figma-component sidebar-navigation --html (vòng 1 Brainstorm)
# Chạy: python3 design-system/components/_work/sidebar-navigation/build.py && python3 _scripts/ds-component-page.py sidebar-navigation
import json
from pathlib import Path

OUT = Path(__file__).parent / "page.json"

# ---------- icon (Lucide, nét 2) ----------
P = {
 "home": '<path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 "gauge": '<path d="M12 14l4-4"/><path d="M3.3 19a10 10 0 1 1 17.4 0"/>',
 "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L4 12l8-8z" transform="scale(.9) translate(1 1)"/>',
 "alert": '<path d="M12 3l9.5 17h-19z"/><path d="M12 10v4M12 17h.01"/>',
 "file": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 13h6M9 17h4"/>',
 "clip": '<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4h6v3H9zM9 12h6M9 16h4"/>',
 "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.2"/>',
 "box": '<path d="M21 8l-9-5-9 5v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
 "check2": '<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4h6v3H9zM9 14l2 2 4-4"/>',
 "wallet": '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M16 15h2"/>',
 "coins": '<circle cx="9" cy="9" r="6"/><path d="M15.5 9.5a6 6 0 1 1-6 6"/>',
 "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 "fuel": '<path d="M4 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16M3 21h12M4 10h10"/><path d="M14 8h2a2 2 0 0 1 2 2v6a1.5 1.5 0 0 0 3 0V8l-3-3"/>',
 "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21c1-4 4-6 7-6s6 2 7 6M16 3a4 4 0 0 1 0 8M22 21c-.5-2.5-2-4.3-4-5.2"/>',
 "book": '<path d="M4 4h10a4 4 0 0 1 4 4v13H8a4 4 0 0 1-4-4z"/><path d="M4 17a4 4 0 0 1 4-4h10"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
 "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h8"/>',
 "anchor": '<circle cx="12" cy="5" r="2"/><path d="M12 7v14M5 13a7 7 0 0 0 14 0M8 11h8"/>',
 "tree": '<rect x="9" y="3" width="6" height="5" rx="1"/><rect x="3" y="16" width="6" height="5" rx="1"/><rect x="15" y="16" width="6" height="5" rx="1"/><path d="M12 8v4M6 16v-4h12v4"/>',
 "receipt": '<path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
 "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17h.01"/>',
 "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1-2.8 2.8-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21h-4v-.2a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1-2.8-2.8.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3v-4h.2a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.8l-.1-.1 2.8-2.8.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3h4v.2a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1 2.8 2.8-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1h.2v4h-.2a1.7 1.7 0 0 0-1.5 1z"/>',
 "ud": '<path d="M7 15l5 5 5-5M7 9l5-5 5 5"/>',
 "cd": '<path d="M6 9l6 6 6-6"/>',
 "cr": '<path d="M9 6l6 6-6 6"/>',
 "cl": '<path d="M15 18l-6-6 6-6"/>',
 "check": '<path d="M5 12l5 5 9-10"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
 "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8"/><path d="M10 21h4"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "out": '<path d="M14 4h6v6M20 4l-9 9"/><path d="M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "panel": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
}
def ic(k, s=20):
    return (f'<svg class="i" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[k]}</svg>')

# ---------- dữ liệu nghiệp vụ (PRD Mục 6, DEC-079; SRS cũ: Cơ cấu tổ chức tr.197, UC00.00.06) ----------
STATES = [("default", "Nhiều chi nhánh, nhiều cơ sở"), ("open", "Đang mở bộ chọn"), ("one", "1 chi nhánh, 1 cơ sở"),
          ("all", "Tất cả cơ sở"), ("collapsed", "Menu thu gọn"), ("switching", "Đang chuyển phạm vi"),
          ("confirm", "Đổi khi form chưa lưu"), ("long", "Chữ dài")]
SK = [k for k, _ in STATES]

def sv(default, **over):
    """Chữ đổi theo trạng thái: mỗi trạng thái một span (data-show state:…)."""
    return "".join(f'<span data-show="state:{k}">{over.get(k, default)}</span>' for k in SK)

BR = sv("CN Hồ Chí Minh", long="CN Bà Rịa – Vũng Tàu (Cái Mép – Thị Vải)")
FAC_X = sv("Xưởng Cát Lái", all="Tất cả xưởng", switching="Xưởng Sóng Thần",
           long="Xưởng sửa chữa container lạnh KCN Phú Mỹ 3")

MOD = {
 "dpvt": {"name": "Điều phối vận tải", "icon": "route", "t": "blue", "fac": None},
 "qlpt": {"name": "Quản lý phương tiện", "icon": "truck", "t": "teal", "fac": None},
 "bdsc": {"name": "Bảo dưỡng sửa chữa", "icon": "wrench", "t": "amber", "fac": "Xưởng",
          "list": ["Xưởng Cát Lái", "Xưởng Sóng Thần", "Xưởng Tân Vạn"]},
 "dau": {"name": "Quản lý dầu", "icon": "fuel", "t": "green", "fac": "Cây dầu", "outside": True,
         "list": ["Cây dầu Cát Lái", "Cây dầu Phú Hữu"]},
 "ns": {"name": "Nhân sự", "icon": "users", "t": "violet", "fac": None},
 "dm": {"name": "Danh mục", "icon": "book", "t": "gray", "fac": None, "company": True},
 "qt": {"name": "Quản trị hệ thống", "icon": "shield", "t": "gray", "fac": None, "company": True},
}
BRANCHES = [("CN Hồ Chí Minh", "TP. Hồ Chí Minh", "Dùng gần nhất"), ("CN Hải Phòng", "Hải Phòng", ""),
            ("CN Hà Nội", "Hà Nội", ""), ("CN Đà Nẵng", "Đà Nẵng", "")]

MENU = {
 "bdsc": [("Tổng quan", "Tổng quan", [("gauge", "Dashboard xưởng", None)]),
          ("Sửa chữa", "wrench", [("alert", "Sự cố phương tiện", "3"), ("file", "Báo giá sửa chữa", None),
                                  ("clip", "Lệnh sửa chữa", "12"), ("cal", "Lịch nhắc", None)]),
          ("Kho và mua hàng", "box", [("cart", "Mua hàng", None), ("box", "Nhập xuất kho", None), ("check2", "Kiểm kê", None)]),
          ("Thanh toán", "wallet", [("wallet", "Thanh toán mua hàng và bồi thường", None), ("coins", "Thu tiền dịch vụ", None)])],
 "dpvt": [("Tổng quan", "Tổng quan", [("gauge", "Bảng điều phối", None)]),
          ("Vận hành", "route", [("file", "Hồ sơ dịch vụ (JobID)", "5"), ("anchor", "Điều phối cảng bãi", None),
                                 ("truck", "Lệnh vận tải", "18")]),
          ("Theo dõi", "tree", [("tree", "Quy trình liên nghiệp vụ", None), ("receipt", "Công nợ, hoá đơn tạm", None)])],
}

def tile(mk, s=32):
    m = MOD[mk]
    return f'<span class="mt t-{m["t"]}" style="width:{s}px;height:{s}px">{ic(m["icon"], 20 if s >= 32 else 16)}</span>'

def line2(mk, branch=False):
    m = MOD[mk]
    if m.get("company"):
        return '<span>Toàn công ty</span>'
    if not m["fac"]:
        return BR if branch else '<span>Không chia cơ sở</span>'
    fac = FAC_X if mk == "bdsc" else sv(m["list"][0])
    return f'{BR}<span class="dot">·</span>{fac}' if branch else fac

# ---------- thẻ phạm vi ----------
def scope_card(mk):
    m = MOD[mk]
    fac = m["fac"]
    # D2a: 2 dòng
    a = (f'<button class="sc" data-show="D2:a" aria-haspopup="dialog">{tile(mk)}<span class="st"><span class="s1">{m["name"]}</span>'
         f'<span class="s2">{line2(mk)}</span></span><span class="ud">{ic("ud", 16)}</span></button>')
    # D2b: 3 hàng có nhãn
    rows = [("Chi nhánh", BR, "building"), ("Module", m["name"], m["icon"])]
    if fac:
        rows.append((fac, FAC_X if mk == "bdsc" else sv(m["list"][0]), "pin"))
    b = ('<div class="sc3" data-show="D2:b">' + "".join(
        f'<button class="r"><span class="rk">{k}</span><span class="rv">{ic(i, 16)}<span class="tx">{v}</span></span><span class="ud">{ic("cd", 16)}</span></button>'
        for k, v, i in rows) + '</div>')
    # D2c: thẻ module + ô chọn cơ sở riêng
    c = (f'<div data-show="D2:c" class="scc"><button class="sc">{tile(mk)}<span class="st"><span class="s1">{m["name"]}</span>'
         f'</span><span class="ud">{ic("ud", 16)}</span></button>'
         + (f'<button class="fsel">{ic("pin", 16)}<span class="tx">{FAC_X if mk == "bdsc" else sv(m["list"][0])}</span>{ic("cd", 16)}</button>' if fac else "")
         + '</div>')
    # thu gọn: chỉ ô module
    mini_ = f'<button class="scm" aria-label="Phạm vi: {m["name"]}">{tile(mk, 36)}</button>'
    return f'<div class="scw" data-cmp>{a}{b}{c}{mini_}</div>'

def astryx_footer(mk):
    m = MOD[mk]
    fac = (f'<div class="af2">{ic("pin", 16)}<span class="tx">{FAC_X if mk == "bdsc" else sv(m["list"][0])}</span><span class="ud">{ic("cd", 16)}</span></div>'
           if m["fac"] else '<div class="af2 muted">Không chia cơ sở</div>')
    return (f'<div class="af" data-show="D1:b" data-cmp><div class="af1">{tile(mk)}<span class="s1">{m["name"]}</span></div>'
            f'<i class="hr"></i>{fac}</div>')

def bottom_card(mk):
    m = MOD[mk]
    return (f'<button class="sc bot" data-show="D1:d" data-cmp>{tile(mk)}<span class="st"><span class="s1">{m["name"]}</span>'
            f'<span class="s2">{line2(mk)}</span></span><span class="ud">{ic("ud", 16)}</span></button>')

# ---------- menu ----------
def nav(mk, active):
    out = []
    for gi, (g, gicon, items) in enumerate(MENU[mk]):
        if gi:
            out.append('<i class="dv" data-show="D5:c"></i>')
        if g != "Tổng quan":
            out.append(f'<div class="gt" data-show="D5:a">{g}</div>')
            out.append(f'<div class="it par" data-show="D5:b">{ic(gicon)}<span class="t">{g}</span>{ic("cd", 16)}</div>')
        for i, label, badge in items:
            on = " on" if label == active else ""
            lab = sv(label, long="Thanh toán mua hàng và bồi thường hàng hoá dịch vụ") if label.startswith("Thanh toán mua") else label
            out.append(f'<a class="it{on}{" ch" if g != "Tổng quan" else ""}" title="{label}">{ic(i)}<span class="t">{lab}</span>'
                       + (f'<span class="bd">{badge}</span>' if badge else "") + '</a>')
    return "".join(out)

def sidebar(mk, active):
    return (f'<aside class="sb">'
            f'<div class="lg"><span class="lt"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span><span class="lnw"><span class="ln">Delta Logistics</span><span class="lnb" data-show="D1:a">{BR}</span><span class="lnb" data-show="D1:d">{BR}</span></span>'
            f'<button class="ib" aria-label="Thu gọn menu">{ic("panel", 20)}</button></div>'
            f'<div data-show="D1:a">{scope_card(mk)}</div>'
            f'<nav class="nv">{nav(mk, active)}</nav>'
            f'<div class="ft"><a class="it">{ic("help")}<span class="t">Hướng dẫn sử dụng</span></a>'
            f'{astryx_footer(mk)}{bottom_card(mk)}</div></aside>')

def rail(mk):
    order = ["dpvt", "qlpt", "bdsc", "dau", "ns", "dm", "qt"]
    return ('<div class="rail" data-show="D3:b" data-cmp><span class="lt"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span><i class="hr" style="width:28px"></i>'
            + "".join(f'<button class="rb{" on" if k == mk else ""}" title="{MOD[k]["name"]}">{tile(k, 36)}</button>' for k in order)
            + '</div>')

# ---------- bộ chọn phạm vi ----------
def opt(icon_html, label, sub="", on=False, radio=False, cls=""):
    mark = (f'<span class="rd{" on" if on else ""}"></span>' if radio else (f'<span class="ck">{ic("check", 16)}</span>' if on else ""))
    return (f'<div class="op{" on" if on else ""} {cls}">{icon_html}<span class="ot"><span class="o1">{label}</span>'
            + (f'<span class="o2">{sub}</span>' if sub else "") + f'</span>{mark}</div>')

def fac_list(mk, radio=False):
    m = MOD[mk]
    if not m["fac"]:
        return f'<div class="nofac">{ic("layers", 20)}<b>{m["name"]} không chia cơ sở</b><span>Dữ liệu xem theo cả chi nhánh.</span></div>'
    unit = m["fac"].lower()
    rows = [opt(f'<span class="oi">{ic("layers", 18)}</span>', f'Tất cả {unit}', f'{len(m["list"])} {unit} · xem tổng hợp', radio=radio, cls="sys")]
    if m.get("outside"):
        rows.append(opt(f'<span class="oi">{ic("out", 18)}</span>', 'Ngoài cơ sở', 'Cây dầu đối tác, hoá đơn lẻ', radio=radio, cls="sys"))
    rows.append('<i class="hr"></i>')
    for i, f in enumerate(m["list"]):
        rows.append(opt(f'<span class="oi">{ic("pin", 18)}</span>', f, "", on=(i == 0), radio=radio))
    return "".join(rows)

def mod_list(cur, radio=False):
    out = []
    for k, m in MOD.items():
        sub = "Cấp công ty" if m.get("company") else (f'{len(m["list"])} {m["fac"].lower()}' if m["fac"] else "Không chia cơ sở")
        out.append(opt(tile(k, 28), m["name"], sub, on=(k == cur), radio=radio))
    return "".join(out)

def branch_list(radio=False):
    rows = [opt(f'<span class="oi">{ic("building", 18)}</span>', "Delta Logistics (công ty mẹ)", "Toàn tổ chức · có quyền xem tổng", radio=radio, cls="sys"), '<i class="hr"></i>']
    for i, (b, city, tag) in enumerate(BRANCHES):
        rows.append(opt(f'<span class="oi">{ic("pin", 18)}</span>', b, city + (f" · {tag}" if tag else ""), on=(i == 0), radio=radio))
    return "".join(rows)

def search(ph):
    return f'<div class="se">{ic("search", 16)}<span>{ph}</span></div>'

def popover(mk):
    m = MOD[mk]
    unit = (m["fac"] or "cơ sở").lower()
    a = (f'<div class="pa" data-show="D4:a">'
         f'<div class="ph"><span class="phk">{ic("building", 16)}Chi nhánh</span><b>{BR}</b><button class="lk">Đổi chi nhánh</button></div>'
         f'<div class="pcols"><div class="pc"><div class="pt">Module</div>'
         f'<div data-show="D3:a">{mod_list(mk)}</div>'
         f'<div data-show="D3:b" class="hint">Đổi module ở thanh icon bên trái.</div>'
         f'<div data-show="D3:c" class="hint">Bấm logo để về Trang chủ và chọn module khác.</div></div>'
         f'<div class="pc"><div class="pt">{m["fac"] or "Cơ sở"} · {m["name"]}</div>'
         + (search(f"Tìm {unit}…") if m["fac"] else "") + f'{fac_list(mk)}</div></div></div>')
    b = (f'<div class="pb" data-show="D4:b"><div class="pbs"><div class="pt">Chi nhánh</div>'
         f'<div class="op sel">{ic("building", 18)}<span class="ot"><span class="o1">{BR}</span></span>{ic("cr", 16)}</div>'
         f'<div data-show="D3:a"><div class="pt">Module</div>{mod_list(mk, radio=True)}</div>'
         + (f'<div class="pt">{m["fac"]}</div>{fac_list(mk, radio=True)}' if m["fac"] else "")
         + '</div><div class="pf"><button class="bt">Huỷ</button><button class="bt pri">Áp dụng</button></div></div>')
    c = (f'<div class="pcm" data-show="D4:c"><div class="mh"><b>Đổi phạm vi làm việc</b><button class="ib">{ic("x", 18)}</button></div>'
         f'<div class="mcols"><div class="pc"><div class="pt">1 · Chi nhánh</div>{search("Tìm chi nhánh, tỉnh thành…")}{branch_list()}</div>'
         f'<div class="pc"><div class="pt">2 · Module</div>{mod_list(mk)}</div>'
         f'<div class="pc"><div class="pt">3 · {m["fac"] or "Cơ sở"}</div>{fac_list(mk)}</div></div>'
         f'<div class="pf"><span class="pfh">Đang chọn: {m["name"]} · CN Hồ Chí Minh</span><button class="bt">Huỷ</button><button class="bt pri">Chọn</button></div></div>')
    return f'<div class="scrim" data-show="state:open D4:c"></div><div class="pop" data-show="state:open" data-cmp>{a}{b}{c}</div>'

# ---------- thanh trên ----------
def topbar(mk, crumb, page):
    m = MOD[mk]
    fac = (f'<span class="sl">/</span><button class="bc">{ic("pin", 16)}<span class="tx">{FAC_X if mk == "bdsc" else sv(m["list"][0])}</span>{ic("ud", 14)}</button>' if m["fac"] else "")
    bcs = (f'<div class="bcs" data-show="D1:c" data-cmp><button class="bc">{ic("building", 16)}<span class="tx">{BR}</span>{ic("ud", 14)}</button>'
           f'<span class="sl">/</span><button class="bc">{tile(mk, 22)}<span class="tx">{m["name"]}</span>{ic("ud", 14)}</button>{fac}</div>')
    return (f'<header class="tb"><div class="cr" data-show="D1:a">{crumb} <span class="sl">/</span> <b>{page}</b></div>'
            f'<div class="cr" data-show="D1:b">{crumb} <span class="sl">/</span> <b>{page}</b></div>'
            f'<div class="cr" data-show="D1:d">{crumb} <span class="sl">/</span> <b>{page}</b></div>{bcs}'
            f'<span class="sp"></span>'
            f'<button class="brb" data-show="D1:b" data-cmp>{ic("pin", 16)}<span class="tx">{BR}</span>{ic("cd", 16)}</button>'
            f'<div class="tse">{ic("search", 16)}<span>Tìm lệnh, xe, phụ tùng…</span><kbd>⌘K</kbd></div>'
            f'<button class="ib" aria-label="Thông báo">{ic("bell", 20)}<i class="nd"></i></button><span class="av">NA</span></header>')

def skel(n=6):
    return ('<div class="sk" data-show="state:switching"><div class="sb1" style="width:240px;height:28px"></div>'
            + "".join('<div class="sb1" style="height:44px"></div>' for _ in range(n)) + '</div>')

def web(mk, active, crumb, page, body, extra=""):
    return (f'<div class="app">{rail(mk)}{sidebar(mk, active)}<div class="mn">{topbar(mk, crumb, page)}'
            f'<main class="ct"><div class="real">{body}</div>{skel()}</main></div>{popover(mk)}{extra}</div>')

# ---------- nội dung màn ----------
RO = [("LSC-2026-0318", "51C-123.45", "Thay má phanh trục 2", "Trần Văn Bình", "Đang sửa", "info"),
      ("LSC-2026-0317", "51D-678.90", "Bảo dưỡng định kỳ 40.000 km", "Lê Minh Châu", "Chờ phụ tùng", "warn"),
      ("LSC-2026-0316", "15C-246.80", "Kiểm tra máy lạnh container", "Phạm Quốc Huy", "Chờ duyệt báo giá", "warn"),
      ("LSC-2026-0315", "51C-135.79", "Thay lốp trục 3 (2 lốp)", "Trần Văn Bình", "Hoàn tất", "ok"),
      ("LSC-2026-0314", "50H-112.23", "Sửa đèn hậu, dây điện mooc", "Ngô Thanh Tâm", "Hoàn tất", "ok")]
def chip(t, tone):
    return f'<span class="chip {tone}">{t}</span>'

B_LIST = ('<div class="ph1"><div><h1>Lệnh sửa chữa</h1><p class="sub">12 lệnh đang mở tại ' + FAC_X + '</p></div>'
          '<button class="bt pri">' + ic("plus", 16) + 'Tạo lệnh</button></div>'
          '<div class="tbl"><table><tr><th>Mã lệnh</th><th>Xe</th><th>Hạng mục</th><th>Thợ phụ trách</th><th>Trạng thái</th></tr>'
          + "".join(f'<tr><td class="mono">{a}</td><td class="mono">{b}</td><td>{c}</td><td>{d}</td><td>{chip(e, t)}</td></tr>' for a, b, c, d, e, t in RO)
          + '</table></div>')

B_DASH = ('<div class="ph1"><div><h1>Bảng điều phối</h1><p class="sub">Hôm nay · ' + BR + '</p></div></div>'
          '<div class="kpis">' + "".join(f'<div class="kpi"><span>{k}</span><b>{v}</b></div>' for k, v in
                                         [("Lệnh đang chạy", "18"), ("Chờ gán xe", "4"), ("JobID mở", "5"), ("Xe sẵn sàng", "26")]) + '</div>'
          '<div class="tbl"><table><tr><th>Mã lệnh</th><th>Tuyến</th><th>Xe</th><th>Lái xe</th><th>Trạng thái</th></tr>'
          + "".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td class="mono">{c}</td><td>{d}</td><td>{chip(e, t)}</td></tr>' for a, b, c, d, e, t in
                    [("LVT-2026-0412", "Cát Lái → Sóng Thần", "51C-123.45", "Trần Văn Bình", "Đang chạy", "info"),
                     ("LVT-2026-0413", "Cát Lái → Tân Vạn", "51D-678.90", "Lê Minh Châu", "Đang chạy", "info"),
                     ("LVT-2026-0414", "Phú Hữu → VSIP 2", "—", "—", "Chờ gán xe", "warn"),
                     ("LVT-2026-0410", "Cái Mép → Sóng Thần", "15C-246.80", "Phạm Quốc Huy", "Hoàn tất", "ok")])
          + '</table></div>')

def fld(l, v, ph=False):
    return f'<label class="fl"><span>{l}</span><span class="in{" ph" if ph else ""}">{v}</span></label>'
B_FORM = ('<div class="form"><h1>Tạo lệnh sửa chữa</h1><p class="sub">Lệnh mới tự gắn ' + BR + ' · ' + FAC_X + '</p>'
          '<div class="card">' + fld("Xe", "51C-123.45 · Đầu kéo Hyundai Xcient") + fld("Hạng mục", "Thay má phanh trục 2")
          + fld("Thợ phụ trách", "Trần Văn Bình") + fld("Ghi chú", "Xe báo phanh kêu khi xuống dốc cầu Phú Mỹ") + '</div>'
          '<div class="fa"><button class="bt">Huỷ</button><button class="bt pri">Lưu lệnh</button></div></div>')

CONFIRM = ('<div class="scrim" data-show="state:confirm"></div><div class="dlg" data-show="state:confirm" role="dialog">'
           '<span class="fi">' + ic("alert", 20) + '</span><b>Rời trang khi chưa lưu?</b>'
           '<p>Chuyển sang Xưởng Sóng Thần sẽ bỏ lệnh sửa chữa đang tạo. Dữ liệu đã nhập không được giữ lại.</p>'
           '<div class="fa"><button class="bt">Ở lại</button><button class="bt pri">Rời trang và chuyển</button></div></div>')

# ---------- mobile ----------
SHORT = [("alert", "Sự cố", "3"), ("file", "Báo giá", ""), ("clip", "Lệnh sửa chữa", "12"), ("cal", "Lịch nhắc", ""),
         ("cart", "Mua hàng", ""), ("box", "Nhập xuất kho", ""), ("check2", "Kiểm kê", ""), ("wallet", "Thanh toán", "")]
TODO = [("Duyệt báo giá BG-2026-0211", "Xe 15C-246.80 · 18.450.000 ₫"), ("Nhận phụ tùng PO-2026-0098", "4 mã · Nhà cung cấp Minh Phát"),
        ("Lịch bảo dưỡng 51D-678.90", "Đến hạn 30/10")]

def m_card(mk="bdsc"):
    m = MOD[mk]
    return (f'<button class="msc" data-cmp>{tile(mk, 36)}<span class="st"><span class="s1">{m["name"]}</span>'
            f'<span class="s2">{line2(mk, True)}</span></span><span class="ud">{ic("ud", 18)}</span></button>')

def tabs(active="home", menu=False):
    t = [("home", "Trang chủ"), ("cal", "Lịch nhắc"), ("bell", "Thông báo"), ("user", "Tài khoản")]
    if menu:
        t.append(("menu", "Menu"))
    return (f'<nav class="mtabs{" five" if menu else ""}">' + "".join(
        f'<span class="mtab{" on" if k == active else ""}" aria-label="{l}">{ic(k, 24)}</span>' for k, l in t) + '</nav>')

def m_nav(mk="bdsc"):
    out = []
    for g, _, items in MENU[mk]:
        if g != "Tổng quan":
            out.append(f'<div class="gt">{g}</div>')
        for i, l, b in items:
            out.append(f'<a class="mit">{ic(i)}<span class="t">{l}</span>' + (f'<span class="bd">{b}</span>' if b else "") + f'{ic("cr", 16)}</a>')
    return "".join(out)

def m_sheet(mk="bdsc"):
    m = MOD[mk]
    return ('<div class="mscrim" data-show="state:open D7:a"></div>'
            f'<div class="sheet" data-show="state:open D7:a" data-cmp><i class="hdl"></i><div class="shh"><b>Phạm vi làm việc</b>{ic("x", 22)}</div>'
            f'<div class="shb"><div class="pt">Chi nhánh</div><div class="op sel big">{ic("building", 20)}<span class="ot"><span class="o1">{BR}</span></span>{ic("cr", 18)}</div>'
            f'<div class="pt">Module</div>{mod_list(mk, radio=True)}<div class="pt">{m["fac"]}</div>{fac_list(mk, radio=True)}</div>'
            '<div class="shf"><button class="cta">Áp dụng</button></div></div>')

def m_drawer(mk="bdsc"):
    return ('<div class="mscrim" data-show="state:open D7:b"></div>'
            f'<div class="drw" data-show="state:open D7:b" data-cmp><div class="lg"><span class="lt"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span><span class="ln">Delta Logistics</span>{ic("x", 22)}</div>'
            f'{m_card(mk)}<div class="mnv">{m_nav(mk)}</div></div>')

def home_body():
    return ('<div class="mpad"><div class="sect">Lối tắt</div><div class="sgrid">'
            + "".join(f'<div class="sg"><span class="sgi">{ic(i, 22)}{f"<i class=sgb>{b}</i>" if b else ""}</span><span>{l}</span></div>' for i, l, b in SHORT)
            + '</div><div class="sect">Việc cần làm</div><div class="mlist">'
            + "".join(f'<div class="mrow"><span class="b">{a}</span><span class="sub">{b}</span>{ic("cr", 18)}</div>' for a, b in TODO)
            + '</div></div>')

def m_home():
    head_a = (f'<div data-show="D7:a"><div class="mh1"><span class="av lg">NA</span><div class="hi"><span>Xin chào,</span><b>Nguyễn Văn An</b></div>'
              f'<button class="mib">{ic("search", 22)}</button><button class="mib">{ic("bell", 22)}<i class="nd"></i></button></div>'
              f'<div class="mpx">{m_card()}</div></div>')
    head_b = (f'<div data-show="D7:b"><div class="mbar"><button class="mib">{ic("menu", 24)}</button><b>Trang chủ</b><span class="sp"></span>'
              f'<button class="mib">{ic("bell", 22)}<i class="nd"></i></button></div>'
              f'<div class="mctx">{tile("bdsc", 20)}<span class="tx">Bảo dưỡng sửa chữa · {FAC_X}</span></div></div>')
    head_c = (f'<div data-show="D7:c"><div class="mh1"><span class="av lg">NA</span><div class="hi"><span>Xin chào,</span><b>Nguyễn Văn An</b></div>'
              f'<button class="mib">{ic("bell", 22)}<i class="nd"></i></button></div>'
              f'<div class="mctx">{tile("bdsc", 20)}<span class="tx">Bảo dưỡng sửa chữa · {FAC_X}</span></div></div>')
    menu_c = (f'<div class="mmenu" data-show="state:open D7:c"><div class="mbar"><b>Menu</b></div><div class="mpx">{m_card()}</div>'
              f'<div class="mnv">{m_nav()}</div></div>')
    return (f'<div class="phone"><div class="mst"><span>9:41</span><span>●●● 5G ▮</span></div>{head_a}{head_b}{head_c}'
            f'<div class="msc-body"><div class="real">{home_body()}</div>{skel(4)}</div>'
            f'<div data-show="D7:a">{tabs()}</div><div data-show="D7:b">{tabs()}</div><div data-show="D7:c">{tabs("home", True)}</div>'
            f'{menu_c}{m_sheet()}{m_drawer()}</div>')

def m_list():
    rows = "".join(f'<div class="mrow"><span class="b mono">{a}</span>{chip(e, t)}<span class="sub">{b} · {c}</span></div>' for a, b, c, d, e, t in RO)
    return (f'<div class="phone"><div class="mst"><span>9:41</span><span>●●● 5G ▮</span></div>'
            f'<div class="mbar"><button class="mib">{ic("cl", 24)}</button><span class="sp"></span><button class="mib">{ic("search", 22)}</button></div>'
            f'<div class="mtt"><h2>Lệnh sửa chữa</h2><button class="mctx in" data-cmp>{ic("pin", 16)}<span class="tx">{FAC_X}</span>{ic("cd", 16)}</button></div>'
            f'<div class="msc-body"><div class="real"><div class="mlist">{rows}</div></div>{skel(4)}</div>'
            f'<div class="mfoot"><button class="cta">Tạo lệnh sửa chữa</button></div></div>')

# ---------- CSS ----------
CSS = r"""
.pv{position:relative;
 
 
 
 color:var(--color-text-primary);font:14px/20px Inter,system-ui,sans-serif;background:var(--color-bg-primary)}
.pv[data-theme=dark]{
 
 
 }
.pv *{box-sizing:border-box}.pv button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer;text-align:left}
.pv a{color:inherit;text-decoration:none}.i{flex:none}
.mono{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:13px}
.tx,.s1,.s2,.o1,.o2,.t{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.hr{display:block;height:1px;background:var(--color-border-secondary);margin:6px 0}
.mt{display:inline-grid;place-items:center;border-radius:8px;flex:none}
.t-blue{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}.t-teal{background:var(--color-utility-teal-50);color:var(--color-utility-teal-700)}.t-amber{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}
.t-green{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.t-violet{background:var(--color-utility-purple-50);color:var(--color-utility-purple-700)}.t-gray{background:var(--color-utility-neutral-100);color:var(--color-utility-neutral-600)}
.lt{width:28px;height:28px;border-radius:8px;background:none;color:var(--color-text-white);font:700 13px/28px Inter,system-ui,sans-serif;text-align:center;flex:none}
.ib{width:32px;height:32px;border-radius:8px;display:inline-grid;place-items:center;color:var(--color-text-tertiary);position:relative;flex:none}.ib:hover{background:var(--color-bg-primary_hover)}
.nd{position:absolute;top:6px;right:7px;width:8px;height:8px;border-radius:9px;background:var(--color-fg-error-primary);border:2px solid var(--color-bg-primary)}
.av{width:32px;height:32px;border-radius:99px;background:var(--color-accent-bg);color:var(--color-accent-fg);display:grid;place-items:center;font:600 12px Inter,system-ui,sans-serif;flex:none}.av.lg{width:44px;height:44px;font-size:15px}
.bt{height:36px!important;padding:0 14px!important;flex:none;white-space:nowrap;border-radius:8px;border:1px solid var(--color-border-primary)!important;background:var(--color-bg-primary)!important;font:600 14px Inter,system-ui,sans-serif!important;display:inline-flex;align-items:center;gap:6px;box-shadow:var(--elev-1)}
.bt.pri{background:var(--color-action-primary)!important;color:var(--color-text-inverse)!important;border-color:var(--color-action-primary)!important}
.lk{font:600 13px Inter,system-ui,sans-serif!important;color:var(--color-text-primary)!important;text-decoration:underline;text-underline-offset:3px;margin-left:auto}
.chip{display:inline-block;font:500 12px/18px Inter,system-ui,sans-serif;padding:1px 8px;border-radius:999px;white-space:nowrap}.chip.ok{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.chip.warn{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}.chip.info{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}
/* ---- web ---- */
.app{display:flex;height:800px;width:100%;position:relative;overflow:hidden;background:var(--color-bg-primary)}
.rail{width:60px;flex:none;border-right:1px solid var(--color-border-secondary);display:flex;flex-direction:column;align-items:center;gap:6px;padding:14px 0;background:var(--color-bg-secondary)}
.rb{padding:2px;border-radius:10px}.rb.on{box-shadow:0 0 0 2px var(--color-accent-solid)}
.sb{width:240px;flex:none;border-right:1px solid var(--color-border-secondary);display:flex;flex-direction:column;padding:12px;background:var(--color-bg-primary);min-height:0}
.lnw{display:flex;flex-direction:column;flex:1;min-width:0}.lnb{font:12px/16px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pv[data-D3=b] .sb .lg .lt{display:none}
.lg{display:flex;align-items:center;gap:8px;min-height:36px;padding:0 0 0 4px;margin-bottom:12px}.ln{font:600 14px/24px Inter,system-ui,sans-serif;flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.scw{margin-bottom:12px}
.sc{display:flex;align-items:center;gap:10px;width:100%;padding:8px;border:1px solid var(--color-border-secondary)!important;border-radius:10px;box-shadow:var(--elev-1);background:var(--color-bg-primary)}.sc:hover{background:var(--color-bg-primary_hover)}
.st{display:flex;flex-direction:column;min-width:0;flex:1}.s1{font:600 14px/20px Inter,system-ui,sans-serif}.s2{font:12px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);display:flex;min-width:0}.s2>span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.s2 .dot{flex:none;padding:0 4px}.ud{color:var(--color-text-tertiary);display:grid;place-items:center;flex:none}
.sc3{border:1px solid var(--color-border-secondary);border-radius:10px;overflow:hidden;box-shadow:var(--elev-1)}
.sc3 .r{display:grid;grid-template-columns:1fr auto;grid-template-rows:auto auto;width:100%;padding:6px 10px;border-top:1px solid var(--color-border-secondary)}.sc3 .r:first-child{border-top:0}.sc3 .r:hover{background:var(--color-bg-primary_hover)}
.rk{font:600 11px/16px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);text-transform:uppercase;letter-spacing:.3px}.rv{display:flex;align-items:center;gap:6px;font:600 13px/20px Inter,system-ui,sans-serif;min-width:0;grid-column:1}.rv .i{color:var(--color-text-tertiary)}
.sc3 .ud{grid-row:1/span 2;grid-column:2}
.scc{display:flex;flex-direction:column;gap:6px}.fsel{display:flex;align-items:center;gap:6px;height:32px;padding:0 10px;border:1px solid var(--color-border-input)!important;border-radius:8px;font:500 13px Inter,system-ui,sans-serif!important;color:var(--color-text-secondary)!important;width:100%}.fsel .tx{flex:1}
.scm{display:none}
.nv{display:flex;flex-direction:column;gap:2px;overflow:auto;min-height:0;flex:1}
.gt{font:600 12px/16px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);text-transform:uppercase;letter-spacing:.4px;padding:16px 10px 6px}
.dv{display:block;height:1px;background:var(--color-border-secondary);margin:8px 10px}
.it{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:8px;color:var(--color-text-secondary);font:500 14px/20px Inter,system-ui,sans-serif;flex:none;cursor:pointer}
.it .i{color:var(--color-text-tertiary)}.it .t{flex:1}.it:hover{background:var(--color-bg-primary_hover)}
.it.par{color:var(--color-text-primary);font-weight:600;margin-top:4px}
.pv[data-D5=b] .it.ch{padding-left:40px}.pv[data-D5=b] .it.ch>.i{display:none}
.it.on{background:var(--color-bg-selected);color:var(--color-text-primary);font-weight:600}.it.on .i{color:var(--color-text-primary)}
.pv[data-D6=b] .it.on{background:var(--color-bg-primary_solid);color:var(--color-text-inverse)}.pv[data-D6=b] .it.on .i{color:var(--color-text-inverse)}.pv[data-D6=b] .it.on .bd{background:transparent;color:var(--color-text-inverse);border-color:var(--color-bg-overlay)}
.pv[data-D6=c] .it.on{background:transparent;box-shadow:inset 3px 0 0 var(--color-accent-solid);border-radius:0 8px 8px 0}
.bd{font:500 12px/18px Inter,system-ui,sans-serif;padding:0 8px;border-radius:999px;background:var(--color-utility-neutral-100);border:1px solid var(--color-border-secondary);color:var(--color-text-secondary);flex:none}
.ft{margin-top:8px;display:flex;flex-direction:column;gap:8px;padding-top:4px}
.af{border:1px solid var(--color-border-secondary);border-radius:12px;padding:8px}.af1{display:flex;align-items:center;gap:10px}.af .hr{margin:8px 0}
.af2{display:flex;align-items:center;gap:6px;font:500 13px Inter,system-ui,sans-serif;color:var(--color-text-secondary);padding:0 4px}.af2 .tx{flex:1}.af2.muted{color:var(--color-text-tertiary)}
.sc.bot{margin-top:0}
/* thu gọn */
.pv[data-state=collapsed] .sb{width:64px;padding:12px 10px}
.pv[data-state=collapsed] .ln,.pv[data-state=collapsed] .lg .ib,.pv[data-state=collapsed] .gt,.pv[data-state=collapsed] .it .t,.pv[data-state=collapsed] .it .bd,
.pv[data-state=collapsed] .it.par,.pv[data-state=collapsed] .scw>div,.pv[data-state=collapsed] .scw>.sc,.pv[data-state=collapsed] .af,.pv[data-state=collapsed] .sc.bot{display:none!important}
.pv[data-state=collapsed] .scm{display:grid;place-items:center;width:100%;padding:4px 0}
.pv[data-state=collapsed] .lg{justify-content:center;padding:0}
.pv[data-state=collapsed] .it{justify-content:center;padding:0;width:44px;margin:0 auto}.pv[data-state=collapsed] .it.ch{padding:0}.pv[data-state=collapsed] .it.ch>.i{display:block}
.pv[data-state=one] .ud,.pv[data-state=one] .brb .i:last-child,.pv[data-state=one] .bc .i:last-child{visibility:hidden}.pv[data-state=one] .sc,.pv[data-state=one] .sc3 .r{cursor:default;background:var(--color-bg-primary)}
/* main */
.mn{flex:1;min-width:0;display:flex;flex-direction:column}
.tb{height:56px;flex:none;border-bottom:1px solid var(--color-border-secondary);display:flex;align-items:center;gap:12px;padding:0 24px}
.cr{font-size:14px;color:var(--color-text-tertiary);white-space:nowrap}.cr b{color:var(--color-text-primary);font-weight:600}.sl{color:var(--color-fg-quaternary);padding:0 2px}.sp{flex:1}
.bcs{display:flex;align-items:center;gap:2px;min-width:0}.bc{display:flex;align-items:center;gap:6px;height:32px;padding:0 8px;border-radius:8px;font:600 14px Inter,system-ui,sans-serif!important;max-width:240px}.bc:hover{background:var(--color-bg-primary_hover)}.bc .i{color:var(--color-text-tertiary)}
.brb{display:flex;align-items:center;gap:6px;height:32px;padding:0 10px;border-radius:8px;font:500 14px Inter,system-ui,sans-serif!important;max-width:240px}.brb:hover{background:var(--color-bg-primary_hover)}.brb .i{color:var(--color-text-tertiary)}
.tse{display:flex;align-items:center;gap:8px;width:260px;height:36px;border:1px solid var(--color-border-input);border-radius:8px;padding:0 10px;color:var(--color-text-tertiary);font-size:14px}.tse kbd{margin-left:auto;font:500 12px Inter,system-ui,sans-serif;border:1px solid var(--color-border-secondary);border-radius:4px;padding:0 4px}
.ct{flex:1;overflow:hidden;padding:24px;position:relative}
.ph1{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:20px}.pv h1{font:600 24px/32px Inter,system-ui,sans-serif;margin:0}.pv h2{font:600 24px/32px Inter,system-ui,sans-serif;margin:0}
.sub{margin:2px 0 0;color:var(--color-text-tertiary);display:flex;gap:4px}.sub>span{white-space:nowrap}
.tbl{border:1px solid var(--color-border-secondary);border-radius:12px;overflow:hidden}.pv table{width:100%;border-collapse:collapse}
.pv td,.pv th{padding:12px 16px;border-bottom:1px solid var(--color-border-secondary);text-align:left;font-size:14px}.pv tr:last-child td{border-bottom:0}.pv th{color:var(--color-text-tertiary);font:500 12px/18px Inter,system-ui,sans-serif;background:var(--color-bg-secondary)}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}.kpi{border:1px solid var(--color-border-secondary);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:4px;color:var(--color-text-tertiary)}.kpi b{font:600 28px/36px Inter,system-ui,sans-serif;color:var(--color-text-primary)}
.form{max-width:720px;margin:0 auto;display:flex;flex-direction:column;gap:6px}.card{border:1px solid var(--color-border-secondary);border-radius:12px;padding:20px;display:flex;flex-direction:column;gap:16px;margin-top:14px}
.fl{display:flex;flex-direction:column;gap:6px;font:500 14px Inter,system-ui,sans-serif;color:var(--color-text-secondary)}.in{height:40px;border:1px solid var(--color-border-input);border-radius:8px;padding:0 12px;display:flex;align-items:center;color:var(--color-text-primary);font-weight:400}
.fa{display:flex;justify-content:flex-end;gap:12px;margin-top:16px}
.sk{display:flex;flex-direction:column;gap:12px}.sb1{background:var(--color-bg-tertiary);border-radius:8px}
.pv[data-state=switching] .real{display:none}
/* bộ chọn */
.scrim{position:absolute;inset:0;background:var(--color-bg-overlay);z-index:20}
.pop{position:absolute;z-index:30;background:var(--color-bg-primary_alt);border-radius:12px;box-shadow:var(--elev-2);left:12px;top:104px;width:540px}
.pv[data-D1=b] .pop,.pv[data-D1=d] .pop{top:auto;bottom:84px}
.pv[data-D1=c] .pop{left:250px;top:52px}
.pv[data-D3=b] .pop{left:72px}
.pv[data-D3=b][data-D1=c] .pop{left:310px}
.pv[data-D4=b] .pop{width:320px}
.pv[data-D4=c] .pop{left:50%!important;top:50%!important;bottom:auto!important;transform:translate(-50%,-50%);width:960px}
.ph{display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--color-border-secondary);font-size:14px;min-width:0}.ph b{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.phk{display:flex;align-items:center;gap:6px;color:var(--color-text-tertiary);flex:none}
.pcols{display:grid;grid-template-columns:1fr 1fr}.pcols .pc+.pc{border-left:1px solid var(--color-border-secondary)}
.pc{padding:8px;display:flex;flex-direction:column;gap:2px;min-width:0}
.pt{font:600 12px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);padding:8px 8px 4px}
.op{display:flex;align-items:center;gap:10px;padding:8px;border-radius:8px;cursor:pointer;min-width:0}.op:hover{background:var(--color-bg-primary_hover)}.op.on{background:var(--color-bg-selected)}
.ot{display:flex;flex-direction:column;flex:1;min-width:0}.o1{font:500 14px/20px Inter,system-ui,sans-serif}.o2{font:12px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary)}
.oi{width:28px;height:28px;border-radius:8px;display:grid;place-items:center;color:var(--color-text-tertiary);background:var(--color-bg-tertiary);flex:none}
.ck{color:var(--color-text-primary);display:grid;place-items:center}
.rd{width:18px;height:18px;border-radius:99px;border:1.5px solid var(--color-border-input);flex:none}.rd.on{border:5px solid var(--color-accent-solid)}
.op.sel{border:1px solid var(--color-border-secondary);margin:0 4px}
.se{display:flex;align-items:center;gap:8px;height:32px;border:1px solid var(--color-border-input);border-radius:8px;padding:0 10px;color:var(--color-text-tertiary);margin:4px 4px 6px}
.hint{font-size:13px;color:var(--color-text-tertiary);padding:8px}
.nofac{display:flex;flex-direction:column;align-items:center;text-align:center;gap:4px;padding:28px 12px;color:var(--color-text-tertiary)}.nofac b{color:var(--color-text-primary);font-weight:600}
.pb{padding:4px 4px 0}.pbs{max-height:520px;overflow:auto}.pb .pc{padding:0}
.pf{display:flex;align-items:center;justify-content:flex-end;gap:8px;padding:12px 16px;border-top:1px solid var(--color-border-secondary);margin-top:4px}.pfh{margin-right:auto;color:var(--color-text-tertiary);font-size:13px}
.mh{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--color-border-secondary);font:600 17px/24px Inter,system-ui,sans-serif}
.mcols{display:grid;grid-template-columns:1fr 1fr 1fr}.mcols .pc+.pc{border-left:1px solid var(--color-border-secondary)}
.dlg{position:absolute;z-index:30;left:50%;top:50%;transform:translate(-50%,-50%);width:420px;background:var(--color-bg-primary_alt);border-radius:12px;box-shadow:var(--elev-3);padding:20px;display:flex;flex-direction:column;gap:8px}
.dlg b{font:600 18px/28px Inter,system-ui,sans-serif}.dlg p{margin:0;color:var(--color-text-tertiary)}.fi{width:40px;height:40px;border-radius:99px;background:var(--color-bg-warning-primary);color:var(--color-text-warning-primary);display:grid;place-items:center;margin-bottom:8px}
/* ---- mobile ---- */
.phone{width:393px;height:800px;position:relative;overflow:hidden;display:flex;flex-direction:column;background:var(--color-bg-primary);margin:0 auto}
.mst{height:44px;flex:none;display:flex;justify-content:space-between;align-items:center;padding:0 24px;font:600 15px Inter,system-ui,sans-serif}
.mh1{display:flex;align-items:center;gap:12px;padding:8px 16px}.hi{display:flex;flex-direction:column;flex:1;line-height:22px}.hi span{color:var(--color-text-tertiary);font-size:14px}.hi b{font:600 18px/26px Inter,system-ui,sans-serif}
.mib{width:44px;height:44px;display:grid;place-items:center;border-radius:12px;position:relative;color:var(--color-text-secondary)}
.mib .nd{top:10px;right:11px}
.mpx{padding:4px 16px 8px}
.msc{display:flex;align-items:center;gap:12px;width:100%;padding:10px 12px;border:1px solid var(--color-border-secondary)!important;border-radius:14px;min-height:60px;background:var(--color-bg-primary)}
.mbar{height:52px;flex:none;display:flex;align-items:center;gap:4px;padding:0 6px}.mbar b{font:600 17px/24px Inter,system-ui,sans-serif;padding-left:4px}
.mctx{display:flex;align-items:center;gap:8px;padding:0 16px 10px;font:500 13px Inter,system-ui,sans-serif;color:var(--color-text-secondary);min-width:0}.mctx .tx{display:flex}.mctx .tx>span{overflow:hidden;text-overflow:ellipsis}
.mctx.in{padding:6px 10px;margin-top:6px;border:1px solid var(--color-border-input)!important;border-radius:999px;height:32px;max-width:100%}
.mtt{padding:0 16px 12px}
.msc-body{flex:1;overflow:hidden;position:relative}.msc-body .sk{padding:16px}
.mpad{padding:8px 16px;display:flex;flex-direction:column;gap:10px}.sect{font:600 15px/22px Inter,system-ui,sans-serif;margin-top:6px}
.sgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px 8px}.sg{display:flex;flex-direction:column;align-items:center;gap:6px;font:500 12px/16px Inter,system-ui,sans-serif;text-align:center;color:var(--color-text-secondary)}
.sgi{width:52px;height:52px;border-radius:14px;background:var(--color-bg-tertiary);display:grid;place-items:center;color:var(--color-text-primary);position:relative}
.sgb{position:absolute;top:-4px;right:-6px;font:600 11px/18px Inter,system-ui,sans-serif;font-style:normal;background:var(--color-bg-error-solid);color:var(--color-text-white);border-radius:99px;padding:0 6px}
.mlist{border-top:1px solid var(--color-border-secondary)}.mrow{display:grid;grid-template-columns:1fr auto;gap:2px 8px;padding:14px 16px;border-bottom:1px solid var(--color-border-secondary);align-items:center}
.mpad .mlist{border:1px solid var(--color-border-secondary);border-radius:14px;overflow:hidden}.mpad .mrow:last-child{border-bottom:0}
.mrow .b{font:600 15px/22px Inter,system-ui,sans-serif}.mrow .sub{grid-column:1;font-size:13px;color:var(--color-text-tertiary)}.mrow>.i{grid-row:1/span 2;grid-column:2;color:var(--color-text-tertiary)}
.mtabs{height:64px;flex:none;border-top:1px solid var(--color-border-secondary);display:grid;grid-template-columns:repeat(4,1fr);background:var(--color-bg-primary)}.mtabs.five{grid-template-columns:repeat(5,1fr)}
.mtab{display:grid;place-items:center;color:var(--color-text-tertiary)}.mtab.on{color:var(--color-text-primary)}
.pv[data-D7=c][data-state=open] .mtabs.five .mtab:first-child{color:var(--color-text-tertiary)}.pv[data-D7=c][data-state=open] .mtabs.five .mtab:last-child{color:var(--color-text-primary)}
.mfoot{padding:12px 16px 24px;border-top:1px solid var(--color-border-secondary)}
.cta{width:100%;height:52px;border-radius:14px!important;background:var(--color-action-primary)!important;color:var(--color-text-inverse)!important;font:600 16px Inter,system-ui,sans-serif!important;text-align:center!important}
.mscrim{position:absolute;inset:0;background:var(--color-bg-overlay);z-index:20}
.sheet{position:absolute;left:0;right:0;bottom:0;z-index:30;background:var(--color-bg-primary);border-radius:20px 20px 0 0;max-height:86%;display:flex;flex-direction:column}
.hdl{display:block;width:36px;height:4px;border-radius:9px;background:var(--color-bg-quaternary);margin:8px auto 0}
.shh{display:flex;justify-content:space-between;align-items:center;padding:10px 16px 6px;font:600 18px/26px Inter,system-ui,sans-serif}
.shb{overflow:hidden;padding:0 8px;flex:1}.shb .op{padding:10px 8px;min-height:48px}.op.big{min-height:52px}
.shf{padding:12px 16px 24px;border-top:1px solid var(--color-border-secondary)}
.drw{position:absolute;left:0;top:0;bottom:0;width:316px;z-index:30;background:var(--color-bg-primary_alt);padding:52px 12px 12px;display:flex;flex-direction:column;gap:8px;box-shadow:var(--elev-3)}
.drw .lg{margin-bottom:4px}
.mnv{display:flex;flex-direction:column;overflow:hidden}.mnv .gt{padding:14px 12px 6px}
.mit{display:flex;align-items:center;gap:12px;min-height:48px;padding:0 12px;border-radius:10px;font:500 15px/22px Inter,system-ui,sans-serif;color:var(--color-text-secondary)}.mit .t{flex:1}.mit>.i{color:var(--color-text-tertiary)}
.mmenu{position:absolute;left:0;right:0;top:44px;bottom:64px;z-index:15;background:var(--color-bg-primary);display:flex;flex-direction:column;padding-bottom:8px}.mmenu .mnv{padding:0 4px}
[data-cmp]{cursor:pointer}
"""

# ---------- ô xem trước nhỏ ----------
BASE = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}
def mini(attrs, inner, w=260, h=None, state="default"):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    hh = f"height:{h}px;overflow:hidden;" if h else ""
    return f'<div class="pv" {a} data-state="{state}" style="position:relative;{hh}max-width:{w}px;border:1px solid var(--color-border-secondary);border-radius:10px">{inner}</div>'
def m(over, inner, **kw):
    return mini({**BASE, **over}, inner, **kw)

SB = sidebar("bdsc", "Lệnh sửa chữa")
def sbm(over, h=300, state="default"):
    return m(over, SB, w=242, h=h, state=state)
def topm(over):
    return m(over, f'<div style="width:620px">{topbar("bdsc", "Sửa chữa", "Lệnh sửa chữa")}</div>', w=640)
def popm(over, w=560, h=380):
    return m({**over, "D1": "a"}, f'<div class="app" style="height:{h}px;width:{w}px"><div class="pop" data-show="state:open" style="left:8px;top:8px;transform:none">'
             + popover("bdsc").split('<div class="pop" data-show="state:open" data-cmp>')[1], w=w, h=h, state="open")
def mob(over, state="open"):
    return m(over, m_home(), w=393, h=620, state=state)

decisions = [
 {"id": "D1", "title": "Chỗ đặt phạm vi (chi nhánh · module · cơ sở)",
  "why": "Hiện ba cấp nằm hai nơi: chi nhánh ở thanh trên (FR-account-access-012), module + cơ sở ở chân menu (CMP-11). Người dùng phải nhìn hai góc màn mới biết <mark>đang làm ở đâu</mark> — dễ thao tác nhầm xưởng, nhầm chi nhánh.",
  "source": "SRS cũ tr.197–198 (Công ty → Chi nhánh → Cơ sở; đổi chi nhánh \"chưa có UI\") · CMP-11 · design.md Khung trang",
  "options": [
   {"label": "Gộp ở đầu menu", "desc": "Một thẻ phạm vi ngay dưới logo, thay nút chi nhánh ở thanh trên. Nhìn một chỗ biết cả ba cấp.", "rec": True, "preview": sbm({"D1": "a"}, 220), "ideas": ["I3", "I4", "I12"]},
   {"label": "Tách như hiện tại", "desc": "Chi nhánh ở thanh trên, module + cơ sở ở chân menu. Giữ look Astryx đã duyệt.", "preview": topm({"D1": "b"}), "ideas": ["I7"]},
   {"label": "Đường dẫn trên thanh trên", "desc": "Chi nhánh / Module / Cơ sở là ba đoạn của đường dẫn, mỗi đoạn mở danh sách riêng. Menu chỉ còn mục.", "preview": topm({"D1": "c"}), "ideas": ["I1", "I2"]},
   {"label": "Gộp ở chân menu", "desc": "Một thẻ ở đáy menu như thẻ tài khoản của Untitled; mở lên trên.", "preview": m({"D1": "d"}, SB, w=242, h=170, state="default").replace('max-width:242px', 'max-width:242px;display:flex;flex-direction:column;justify-content:flex-end'), "ideas": ["I8"]}],
  "untitled": sbm({"D1": "d"}, 0).replace("height:0px;", "") if False else m({"D1": "d"}, f'<div style="padding:8px">{bottom_card("bdsc")}</div>', w=242),
  "untitledNote": "NavAccountCard ở chân menu, popover \"Switch account\" mở lên",
  "astryx": topm({"D1": "b"}), "astryxNote": "Thanh trên: nút chi nhánh · chân menu: thẻ module + cơ sở"},
 {"id": "D2", "title": "Cấu tạo thẻ phạm vi",
  "why": "Thẻ phải đọc được <mark>ba cấp trong 240px</mark>, cấp nào đổi được thì có dấu bấm. Áp cho D1 = gộp (đầu hoặc chân menu).",
  "source": "UC00.00.06 (module có / không chia cơ sở) · DEC-106 (dòng chi nhánh ở app)",
  "options": [
   {"label": "2 dòng, một nút", "desc": "Ô màu module + tên module; dòng dưới là cơ sở. Chi nhánh nằm dưới tên đơn vị (Công ty → Chi nhánh). Bấm cả thẻ mở bộ chọn.", "rec": True, "preview": sbm({"D2": "a"}, 130), "ideas": ["I3", "I4"]},
   {"label": "3 hàng có nhãn", "desc": "Chi nhánh / Module / Cơ sở mỗi hàng một nút, bấm hàng nào mở đúng cấp đó. Rõ nhất, cao gấp đôi.", "preview": sbm({"D2": "b"}, 190)},
   {"label": "Thẻ module + ô cơ sở", "desc": "Thẻ module (kèm chi nhánh) và ô chọn cơ sở riêng bên dưới — đổi cơ sở 1 chạm, việc làm nhiều nhất ở xưởng, cây dầu.", "preview": sbm({"D2": "c"}, 170), "ideas": ["I9"]}],
  "untitled": m({"D1": "d"}, f'<div style="padding:8px">{bottom_card("bdsc")}</div>', w=242), "untitledNote": "Avatar + tên + email, chevron lên xuống",
  "astryx": m({"D1": "b"}, f'<div style="padding:8px">{astryx_footer("bdsc")}</div>', w=242), "astryxNote": "Thẻ chân menu: module, vạch, cơ sở"},
 {"id": "D3", "title": "Đổi module ở đâu",
  "why": "Theo SRS cũ người dùng về Home chọn thẻ module rồi mới vào; người làm cả xưởng lẫn cây dầu phải qua Home mỗi lần đổi. 7 module (DEC-079), mỗi người thường có 1–3.",
  "source": "UC00.00.06 › Home (lưới thẻ module, không có sidebar) · PRD Mục 6",
  "options": [
   {"label": "Trong bộ chọn phạm vi", "desc": "Danh sách module có quyền nằm trong cùng bộ chọn với chi nhánh, cơ sở.", "rec": True, "preview": popm({"D3": "a"}, 560, 330), "ideas": ["I4", "I9"]},
   {"label": "Thanh icon module bên trái", "desc": "Cột 60px cố định các module, đổi 1 chạm; menu bên cạnh là mục của module đang chọn.", "preview": m({"D3": "b"}, f'<div class="app" style="height:300px;width:300px">{rail("bdsc")}{SB}</div>', w=302, h=300), "ideas": ["I5", "I6"]},
   {"label": "Về Trang chủ", "desc": "Bấm logo về Home, chọn thẻ module như SRS cũ. Bộ chọn chỉ còn chi nhánh, cơ sở.", "preview": popm({"D3": "c"}, 560, 260)}],
  "untitled": m({"D3": "b"}, f'<div class="app" style="height:300px;width:300px">{rail("bdsc")}{SB}</div>', w=302, h=300), "untitledNote": "Sidebar dual-tier / slim: rail + panel",
  "astryx": popm({"D3": "c"}, 560, 260), "astryxNote": "Về Home chọn thẻ module (UC00.00.06)"},
 {"id": "D4", "title": "Bộ chọn mở ra trông thế nào",
  "why": "Phải có: tìm (GR-09: theo tên chi nhánh, tỉnh thành), \"Tất cả cơ sở\" khi có quyền, \"Ngoài cơ sở\" cho module dầu, công ty mẹ khi có quyền toàn tổ chức (BR-account-access-013), nhớ lần dùng gần nhất (BR-015).",
  "source": "UC00.00.06 mục 3.2 Modal Chọn cơ sở · FR-account-access-011 · SRS cũ tr.199 Ngoài cơ sở",
  "options": [
   {"label": "Popover 2 cột", "desc": "Đầu: chi nhánh + Đổi. Trái module, phải cơ sở của module. Chọn là chuyển ngay, không nút Áp dụng.", "rec": True, "preview": popm({"D4": "a"}), "ideas": ["I4", "I11"]},
   {"label": "Popover 1 cột có Áp dụng", "desc": "Ba nhóm xếp dọc có nút tròn, chọn xong bấm Áp dụng. Hẹp, cuộn dài khi nhiều module.", "preview": popm({"D4": "b"}, 340, 560), "ideas": ["I7", "I8"]},
   {"label": "Hộp thoại 3 cột", "desc": "Hộp thoại giữa màn: Chi nhánh | Module | Cơ sở, có tìm từng cột, nút Chọn. Giống modal Chọn cơ sở cũ, dùng lại cho lúc đăng nhập.", "preview": m({"D4": "c"}, f'<div class="app" style="height:520px;width:900px">{popover("bdsc")}</div>', w=900, h=520, state="open"), "ideas": ["I10"]}],
  "untitled": popm({"D4": "b"}, 340, 560), "untitledNote": "Popover tài khoản: danh sách có nút tròn",
  "astryx": m({"D4": "c"}, f'<div class="app" style="height:520px;width:900px">{popover("bdsc")}</div>', w=900, h=520, state="open"), "astryxNote": "Modal Chọn cơ sở (SRS cũ 3.2) + cửa sổ chọn chi nhánh"},
 {"id": "D5", "title": "Nhóm mục menu",
  "why": "Bảo dưỡng sửa chữa có 10 mục — cần nhóm để lướt. Mục menu là feature (UC khai vị trí).",
  "source": "CMP-11 #3–4 (mục cấp 1 có submenu) · design.md .Nhóm menu",
  "options": [
   {"label": "Nhãn nhóm chữ hoa", "desc": "Nhóm có tiêu đề nhỏ, mọi mục luôn hiện. Như Astryx, Untitled.", "rec": True, "preview": sbm({"D5": "a"}, 300), "ideas": ["I12", "I3"]},
   {"label": "Mục cha thu gọn được", "desc": "Nhóm là mục cha có mũi tên, mục con thụt vào. Gọn khi nhiều module con.", "preview": sbm({"D5": "b"}, 300)},
   {"label": "Vạch chia, không nhãn", "desc": "Chỉ vạch mảnh giữa các nhóm. Gọn nhất, mất tên nhóm.", "preview": sbm({"D5": "c"}, 300)}],
  "untitled": sbm({"D5": "a"}, 300), "untitledNote": "sidebar-sections-subheadings",
  "astryx": sbm({"D5": "a"}, 300), "astryxNote": ".Nhóm menu chữ hoa"},
 {"id": "D6", "title": "Mục đang chọn",
  "why": "Chỉ 1 mục active (CMP-11 #5). Than chì là màu hành động chính (DEC-260 F3) — dùng cho mục đang chọn thì có còn phân biệt với nút Primary?",
  "source": "CMP-11 #5 · DEC-260",
  "options": [
   {"label": "Nền xám, chữ đậm", "desc": "Như Astryx, Untitled. Nhẹ, không tranh với nút chính.", "rec": True, "preview": sbm({"D6": "a"}, 250), "ideas": ["I3", "I12"]},
   {"label": "Nền than chì", "desc": "Nổi nhất, thấy ngay đang ở đâu; tranh với nút Tạo lệnh.", "preview": sbm({"D6": "b"}, 250), "ideas": ["I6"]},
   {"label": "Vạch trái", "desc": "Vạch 3px bên trái, không nền. CMP-11 hiện ghi \"không vạch\".", "preview": sbm({"D6": "c"}, 250)}],
  "untitled": sbm({"D6": "a"}, 250), "untitledNote": "bg-active, chữ secondary_hover",
  "astryx": sbm({"D6": "a"}, 250), "astryxNote": "nền muted, không vạch"},
 {"id": "D7", "title": "App: phạm vi và menu ở đâu",
  "why": "App có thanh tab dưới 4 tab icon (Trang chủ · Lịch nhắc · Thông báo · Tài khoản, MSC-08) và dòng chi nhánh dưới lời chào (DEC-106). Chưa có chỗ đổi module, cơ sở.",
  "source": "CMP-11 Mobile — Bottom Navigation · DEC-106 · design.md m11 Đầu màn",
  "options": [
   {"label": "Thẻ phạm vi ở Trang chủ + sheet", "desc": "Giữ tab dưới. Thẻ phạm vi (như web) dưới lời chào, chạm mở sheet chọn chi nhánh · module · cơ sở. Mục của module thành Lối tắt.", "rec": True, "preview": mob({"D7": "a"}), "ideas": ["I11", "I9"]},
   {"label": "Ngăn kéo trái", "desc": "Nút ☰ mở ngăn kéo chứa thẻ phạm vi + toàn bộ menu như web. Như Untitled, Notion app.", "preview": mob({"D7": "b"}), "ideas": ["I10"]},
   {"label": "Tab thứ 5 \"Menu\"", "desc": "Thêm tab Menu: màn đầy đủ thẻ phạm vi + mục. Dòng phạm vi ở Trang chủ chỉ để đọc.", "preview": mob({"D7": "c"})}],
  "untitled": mob({"D7": "b"}), "untitledNote": "MobileNavigationHeader: ☰ mở ngăn kéo",
  "astryx": mob({"D7": "c"}, state="default").replace('data-D7="c"', 'data-D7="c"'), "astryxNote": "Tab dưới 4 icon + dòng chi nhánh (DEC-106)"},
]

ideas = [
 {"id": "I1", "source": "Vercel", "url": "https://vercel.com/docs/dashboard-features",
  "title": "Đường dẫn Team / Project có nút lên xuống", "why": "Mỗi đoạn đường dẫn là một bộ chọn — đổi team hay project ngay trên thanh trên, menu bên dưới giữ nguyên.",
  "preview": topm({"D1": "c"})},
 {"id": "I2", "source": "Supabase", "url": "https://supabase.com/docs/guides/platform",
  "title": "Tổ chức / Dự án / Nhánh trên thanh trên", "why": "Ba cấp lồng nhau giống Công ty → Chi nhánh → Cơ sở; cấp không áp dụng thì đoạn đó biến mất.",
  "preview": m({"D1": "c"}, f'<div style="width:620px">{topbar("dpvt", "Vận hành", "Lệnh vận tải")}</div>', w=640)},
 {"id": "I3", "source": "Linear", "url": "https://linear.app/docs/conceptual-model",
  "title": "Tên workspace góc trên trái", "why": "Một nút ở đầu sidebar là \"tôi đang ở đâu\"; mục đang chọn nền xám nhạt, nhóm có nhãn nhỏ.",
  "preview": sbm({"D1": "a", "D2": "a"}, 200)},
 {"id": "I4", "source": "shadcn/ui · Sidebar 07", "url": "https://www.shadcnblocks.com/block/sidebar7",
  "title": "Team switcher đầu sidebar", "why": "Logo + tên + gói, chevron lên xuống; dropdown có dấu ✓ cho mục đang dùng. Mẫu phổ biến nhất của app SaaS.",
  "preview": popm({"D4": "a"}, 560, 300)},
 {"id": "I5", "source": "shadcn.io · Sidebar dual panel", "url": "https://www.shadcn.io/blocks/sidebar-dual-panel",
  "title": "Rail icon + panel mục", "why": "Cột icon hẹp đổi không gian làm việc 1 chạm như Slack, panel rộng là mục của không gian đó.",
  "preview": m({"D3": "b"}, f'<div class="app" style="height:280px;width:300px">{rail("bdsc")}{SB}</div>', w=302, h=280)},
 {"id": "I6", "source": "Dribbble · Sidebar logistics", "url": "https://dribbble.com/devdesign-studio/collections/6431427-Sidebar-Navigation",
  "title": "Sidebar freight dashboard, mục chọn nền đậm", "why": "Bộ sidebar cho dashboard vận tải: mục đang chọn tô đậm, rail module bên trái.",
  "preview": sbm({"D6": "b"}, 220)},
 {"id": "I7", "source": "Odoo · Đa công ty", "url": "https://www.odoo.com/documentation/17.0/applications/general/companies/multi_company.html",
  "title": "Bộ chọn công ty trên thanh trên", "why": "ERP đa chi nhánh: chọn công ty ở góc thanh trên, xem gộp nhiều công ty bằng ô đánh dấu — gần cách Astryx đặt chi nhánh.",
  "preview": topm({"D1": "b"})},
 {"id": "I8", "source": "Stripe · Nhiều tài khoản", "url": "https://docs.stripe.com/get-started/account/multiple-accounts",
  "title": "Đổi tài khoản trong menu góc", "why": "Danh sách tài khoản có nút tròn trong một menu; tài khoản đang dùng luôn hiện tên ở góc.",
  "preview": popm({"D4": "b"}, 340, 420)},
 {"id": "I9", "source": "Shopify admin · Địa điểm", "url": "https://help.shopify.com/en/manual/locations",
  "title": "Chọn địa điểm kho riêng với cửa hàng", "why": "Cửa hàng là cấp trên, địa điểm (kho) đổi thường xuyên và có \"Tất cả địa điểm\" — như cơ sở với \"Tất cả xưởng\".",
  "preview": sbm({"D2": "c"}, 170)},
 {"id": "I10", "source": "Google Cloud · Chọn dự án", "url": "https://cloud.google.com/resource-manager/docs/creating-managing-projects",
  "title": "Hộp thoại chọn dự án có tìm", "why": "Hộp thoại lớn duyệt tổ chức → thư mục → dự án, có tìm và \"gần đây\" — hợp khi danh sách dài.",
  "preview": m({"D4": "c"}, f'<div class="app" style="height:520px;width:900px">{popover("bdsc")}</div>', w=900, h=520, state="open")},
 {"id": "I11", "source": "Material 3 · Bottom sheet", "url": "https://m3.material.io/components/bottom-sheets/overview",
  "title": "Bottom sheet chọn trên app", "why": "Sheet mở từ dưới, nằm trong tầm ngón cái; giữ thanh tab dưới thay vì ngăn kéo.",
  "preview": mob({"D7": "a"})},
 {"id": "I12", "source": "21st.dev · Sidebar showcase", "url": "https://21st.dev/@ruixenui/components/sidebar-showcase",
  "title": "Team switcher + nhóm có nhãn + số đếm", "why": "Switcher trên cùng, nhóm Main / Work có nhãn, số đếm dạng pill bên phải mục.",
  "preview": sbm({"D5": "a"}, 300)},
]

presets = [
 {"id": "rec", "label": "Đề xuất", "pick": {d["id"]: chr(97 + next(i for i, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}},
 {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "d", "D2": "a", "D3": "b", "D4": "b", "D5": "a", "D6": "a", "D7": "b"}},
 {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "b", "D2": "a", "D3": "c", "D4": "c", "D5": "a", "D6": "a", "D7": "c"}},
]
for i in ideas:
    pick = dict(BASE)
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pick[d["id"]] = chr(97 + k)
    pr = {"id": i["id"], "label": f'Ý tưởng {i["id"]} · {i["source"].split(" ·")[0]}', "pick": pick}
    if i["id"] in ("I10", "I11"):
        pr["screen"] = 3
    presets.append(pr)

page = {
 "component": "Sidebar Navigation",
 "slug": "sidebar-navigation",
 "title": "Sidebar Navigation Review",
 "subtitle": "Application component · nhóm C (web: menu trái · app: tab dưới + thẻ phạm vi) · vòng 1 Brainstorm — gộp chọn chi nhánh, module, cơ sở",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "5 kiểu sidebar: <mark>simple</mark>, <mark>sections-subheadings</mark> (nhãn nhóm chữ hoa, 276px), dividers, <mark>slim</mark> (rail 68 + panel 256), dual-tier. Đổi không gian làm việc nằm ở <mark>NavAccountCard</mark> chân menu (popover \"Switch account\" có nút tròn). Mobile: thanh đầu 56 + nút ☰ mở ngăn kéo tối đa 296px.",
               "source": "design/_ref/untitled-ui/react/components/application/app-navigation/ (sidebar-navigation/*.tsx, base-components/nav-item.tsx, nav-account-card.tsx, mobile-header.tsx)"},
  "astryx": {"summary": "<mark>Khung trang / Menu trái</mark> 240 (thu gọn 64), mục cao 34, nhãn nhóm chữ hoa, mục chọn nền muted không vạch; <mark>.Chân menu</mark> thẻ module + cơ sở (Nhiều / Một / Không chia cơ sở / Thu gọn); chi nhánh là nút trên <mark>Thanh trên</mark> 44. App: tab dưới 4 icon + dòng chi nhánh dưới lời chào.",
             "source": "design/design.md › Khung trang dự án, bảng component 5596:129193–129536 · design/ui-common/screen-patterns.md CMP-11 · DEC-106"},
  "usage": ["Mọi màn web trong module (CMP-11) — vd service-delivery, transport-dispatch, repair-order",
            "account-access · Đổi chi nhánh trong phiên (FR-account-access-012) — hiện là nút trên thanh trên",
            "common-workspace · Home chọn module, cơ sở (UC00.00.06, PRD 7.2) — modal Chọn cơ sở",
            "organization · Công ty → Chi nhánh → Cơ sở, \"Ngoài cơ sở\" (SRS cũ tr.197–199, PRD 7.6)",
            "App: Trang chủ (m11, DEC-106) + Bottom Navigation (MSC-08)"],
  "platform": "Nhóm C (DEC-279): khác cách thao tác — web là menu trái cố định + popover; app là tab dưới + sheet (hoặc ngăn kéo, D7). Một bộ, trục Platform=Web|Mobile; phần chỉ có trên app tiền tố _."},
 "css": CSS,
 "states": [{"key": k, "label": l} for k, l in STATES],
 "ideas": ideas, "decisions": decisions, "presets": presets,
 "screens": [
  {"id": "repair-web", "name": "Lệnh sửa chữa · Bảo dưỡng sửa chữa", "device": "web", "width": 1280, "shell": "none",
   "note": "Module có cơ sở (Xưởng). Thử trạng thái: Đang mở bộ chọn, Tất cả cơ sở, Thu gọn, Chữ dài, Đang chuyển.",
   "html": web("bdsc", "Lệnh sửa chữa", "Sửa chữa", "Lệnh sửa chữa", B_LIST)},
  {"id": "dispatch-web", "name": "Bảng điều phối · Điều phối vận tải", "device": "web", "width": 1280, "shell": "none",
   "note": "Module không chia cơ sở: thẻ chỉ còn chi nhánh, cột cơ sở trong bộ chọn báo \"không chia cơ sở\".",
   "html": web("dpvt", "Bảng điều phối", "Tổng quan", "Bảng điều phối", B_DASH)},
  {"id": "form-web", "name": "Tạo lệnh sửa chữa · đổi khi chưa lưu", "device": "web", "width": 1280, "shell": "none",
   "note": "Trạng thái \"Đổi khi form chưa lưu\": đổi cơ sở giữa chừng hỏi xác nhận (GR-13, FR-account-access-012).",
   "html": web("bdsc", "Lệnh sửa chữa", "Lệnh sửa chữa", "Tạo lệnh", B_FORM, CONFIRM)},
  {"id": "home-app", "name": "Trang chủ · app", "device": "mobile", "shell": "none",
   "note": "Trạng thái \"Đang mở bộ chọn\" mở sheet / ngăn kéo / màn Menu theo D7.", "html": m_home()},
  {"id": "list-app", "name": "Lệnh sửa chữa · app", "device": "mobile", "shell": "none",
   "note": "Màn con: không có tab dưới; cơ sở đang dùng hiện dưới tiêu đề, chạm để đổi.", "html": m_list()},
 ],
 "figma": {},
}


# ================= Vòng 2 — Preview (tổ hợp user chốt 28/10) =================
ANS = json.loads((Path(__file__).parent / "answers.json").read_text())
PICK = {d["id"]: chr(97 + ANS[f"brainstorm-{d['id']}"]["choice"]) for d in decisions}
P.update({
 "logout": '<path d="M15 4h3a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-3"/><path d="M10 17l-5-5 5-5"/><path d="M5 12h11"/>',
 "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 "back": '<path d="M15 18l-6-6 6-6"/>',
})

# --- app: tab Tài khoản chứa thẻ phạm vi (D7 C + ghi chú user) ---
def m_pick_full(mk="bdsc"):
    m = MOD[mk]
    return (f'<div class="mfull" data-show="state:open" data-cmp><div class="mbar"><button class="mib" aria-label="Đóng">{ic("x", 24)}</button><b>Đổi phạm vi làm việc</b></div>'
            f'<div class="shb"><div class="pt">1 · Chi nhánh</div><div class="op sel big">{ic("building", 20)}<span class="ot"><span class="o1">{BR}</span><span class="o2">Chạm để đổi chi nhánh</span></span>{ic("cr", 18)}</div>'
            f'<div class="pt">2 · Module</div>{mod_list(mk, radio=True)}<div class="pt">3 · {m["fac"]}</div>{fac_list(mk, radio=True)}</div>'
            f'<div class="shf"><div class="pfh m">Đang chọn: {m["name"]} · {FAC_X}</div><button class="cta">Chọn</button></div></div>')

def m_row(icon, label, sub="", danger=False):
    return (f'<div class="arow{" dg" if danger else ""}">{ic(icon, 22)}<span class="ot"><span class="o1">{label}</span>'
            + (f'<span class="o2">{sub}</span>' if sub else "") + f'</span>{"" if danger else ic("cr", 18)}</div>')

def m_account(mk="bdsc"):
    m = MOD[mk]
    body = (f'<div class="apf"><span class="av lg">NA</span><div class="hi"><b>Nguyễn Văn An</b><span>Trưởng xưởng · Delta Logistics</span></div></div>'
            f'<div class="sect2">Phạm vi làm việc</div><div class="mpx0">{m_card(mk)}</div>'
            f'<div class="sect2">Chức năng · {m["name"]}</div><div class="mnv acc">{m_nav(mk)}</div>'
            f'<div class="sect2">Tài khoản</div><div class="agrp">{m_row("user", "Thông tin cá nhân")}{m_row("lock", "Đổi mật khẩu")}'
            f'{m_row("globe", "Ngôn ngữ", "Tiếng Việt")}{m_row("logout", "Đăng xuất", danger=True)}</div>')
    return (f'<div class="phone"><div class="mst"><span>9:41</span><span>●●● 5G ▮</span></div><div class="mbar"><b>Tài khoản</b></div>'
            f'<div class="msc-body"><div class="real ascr">{body}</div>{skel(4)}</div>{tabs("user")}'
            f'<div class="mscrim" data-show="state:confirm"></div><div class="sheet" data-show="state:confirm"><i class="hdl"></i>'
            f'<div class="shh"><b>Rời màn khi chưa lưu?</b></div><p class="shp">Chuyển sang Xưởng Sóng Thần sẽ bỏ báo giá đang soạn. Dữ liệu đã nhập không được giữ lại.</p>'
            f'<div class="shf two"><button class="cta sec">Ở lại</button><button class="cta">Rời màn và chuyển</button></div></div>'
            f'{m_pick_full(mk)}</div>')

def m_home2(mk="bdsc"):
    head = (f'<div class="mh1"><span class="av lg">NA</span><div class="hi"><span>Xin chào,</span><b>Nguyễn Văn An</b></div>'
            f'<button class="mib">{ic("bell", 22)}<i class="nd"></i></button></div>'
            f'<div class="mctx ro">{tile(mk, 20)}<span class="tx">{MOD[mk]["name"]}<span class="dot">·</span>{FAC_X}</span></div>')
    return (f'<div class="phone"><div class="mst"><span>9:41</span><span>●●● 5G ▮</span></div>{head}'
            f'<div class="msc-body"><div class="real">{home_body()}</div>{skel(4)}</div>{tabs("home")}{m_pick_full(mk)}</div>')

# --- web: màn chi tiết ---
B_DETAIL = ('<div class="ph1"><div><h1 class="mono" style="font-size:24px">LSC-2026-0318</h1><p class="sub">Thay má phanh trục 2 · ' + FAC_X + '</p></div>'
            '<div style="display:flex;gap:8px"><button class="bt">In lệnh</button><button class="bt pri">Hoàn tất sửa chữa</button></div></div>'
            '<div class="dgrid"><div class="card">' + fld("Xe", "51C-123.45 · Đầu kéo Hyundai Xcient") + fld("Thợ phụ trách", "Trần Văn Bình")
            + fld("Ngày nhận xe", "27/10/2026 08:15") + fld("Trạng thái", chip("Đang sửa", "info")) + '</div>'
            '<div class="tbl"><table><tr><th>Phụ tùng</th><th>Số lượng</th><th>Kho</th></tr>'
            + "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in
                      [("Má phanh trục 2 (bộ)", "1", "Kho Xưởng Cát Lái"), ("Dầu phanh DOT4 1L", "2", "Kho Xưởng Cát Lái")]) + '</table></div></div>')

page["screens"] = [
 {"id": "repair-web", "name": "Lệnh sửa chữa · danh sách", "device": "web", "width": 1280, "shell": "none",
  "note": "Thẻ phạm vi ở chân menu; bấm mở hộp thoại 3 cột. Thử: Đang mở bộ chọn, Tất cả cơ sở, Thu gọn, Chữ dài, Đang chuyển, Dark.",
  "html": web("bdsc", "Lệnh sửa chữa", "Sửa chữa", "Lệnh sửa chữa", B_LIST)},
 {"id": "detail-web", "name": "Lệnh sửa chữa · chi tiết", "device": "web", "width": 1280, "shell": "none",
  "note": "Màn chi tiết giữ nguyên menu; mục cha \"Lệnh sửa chữa\" vẫn đang chọn.",
  "html": web("bdsc", "Lệnh sửa chữa", "Lệnh sửa chữa", "LSC-2026-0318", B_DETAIL)},
 {"id": "dispatch-web", "name": "Bảng điều phối · module không chia cơ sở", "device": "web", "width": 1280, "shell": "none",
  "note": "Dòng 2 của thẻ ghi \"Không chia cơ sở\"; cột 3 của hộp thoại báo không cần chọn.",
  "html": web("dpvt", "Bảng điều phối", "Tổng quan", "Bảng điều phối", B_DASH)},
 {"id": "form-web", "name": "Tạo lệnh sửa chữa · đổi khi chưa lưu", "device": "web", "width": 1280, "shell": "none",
  "note": "Trạng thái \"Đổi khi form chưa lưu\": bấm Chọn trong hộp thoại thì hỏi xác nhận trước (GR-13).",
  "html": web("bdsc", "Lệnh sửa chữa", "Lệnh sửa chữa", "Tạo lệnh", B_FORM, CONFIRM)},
 {"id": "home-app", "name": "Trang chủ · app", "device": "mobile", "shell": "none",
  "note": "4 tab giữ nguyên. Dòng phạm vi dưới lời chào chỉ để đọc; đổi ở tab Tài khoản.", "html": m_home2()},
 {"id": "account-app", "name": "Tài khoản · app", "device": "mobile", "shell": "none",
  "note": "Thẻ phạm vi + chức năng của module nằm ở tab Tài khoản. Chạm thẻ mở màn Đổi phạm vi (bản app của hộp thoại 3 cột).", "html": m_account()},
 {"id": "list-app", "name": "Lệnh sửa chữa · app", "device": "mobile", "shell": "none",
  "note": "Màn con: không có tab dưới; cơ sở đang dùng hiện dưới tiêu đề, chạm để đổi.", "html": m_list()},
]

# --- bảng biến thể ---
def card(mk, s2, cls="", chev=True, s1=None):
    return (f'<button class="sc bot {cls}">{tile(mk)}<span class="st"><span class="s1">{s1 or MOD[mk]["name"]}</span>'
            f'<span class="s2"><span>{s2}</span></span></span>' + (f'<span class="ud">{ic("ud", 16)}</span>' if chev else "") + '</button>')
def item(icon, label, cls="", badge=None):
    return (f'<a class="it {cls}">{ic(icon)}<span class="t">{label}</span>' + (f'<span class="bd">{badge}</span>' if badge else "") + '</a>')
def mcard(mk, s2, chev=True, s1=None):
    return (f'<button class="msc">{tile(mk, 36)}<span class="st"><span class="s1">{s1 or MOD[mk]["name"]}</span><span class="s2"><span>{s2}</span></span></span>'
            + (f'<span class="ud">{ic("ud", 18)}</span>' if chev else "") + '</button>')

def cell(lab, inner, w):
    return (f'<div style="display:flex;flex-direction:column;gap:6px;width:{w}">'
            f'<div style="font:500 11px Inter,system-ui,sans-serif;color:var(--color-text-tertiary)">{lab}</div>{inner}</div>')
def row(title, cells, note=""):
    return (f'<div style="font:600 13px Inter,system-ui,sans-serif;margin:20px 0 4px">{title}</div>'
            + (f'<div style="font:12px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);margin-bottom:8px">{note}</div>' if note else '<div style="height:4px"></div>')
            + f'<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start">{"".join(cells)}</div>')
def pvwrap(inner, plat):
    a = " ".join(f'data-{k}="{x}"' for k, x in PICK.items())
    return f'<div class="pv" {a} data-state="default" data-theme="light" data-platform="{plat}" style="padding:16px">{inner}</div>'

LONG_BR = "CN Bà Rịa – Vũng Tàu (Cái Mép – Thị Vải)"
LONG_FAC = "Xưởng sửa chữa container lạnh KCN Phú Mỹ 3"
W216 = "216px"
def grid_web():
    h = row("Thẻ phạm vi — theo loại module", [
        cell("Có cơ sở", card("bdsc", "Xưởng Cát Lái"), W216),
        cell("Đang xem tất cả", card("bdsc", "Tất cả xưởng"), W216),
        cell("Ngoài cơ sở (Quản lý dầu)", card("dau", "Ngoài cơ sở"), W216),
        cell("Không chia cơ sở", card("dpvt", "Không chia cơ sở"), W216),
        cell("Cấp công ty", card("dm", "Toàn công ty"), W216)],
        "Dòng 1 là module, dòng 2 là cơ sở. Chi nhánh nằm dưới tên đơn vị ở đầu menu.")
    h += row("Thẻ phạm vi — trạng thái", [
        cell("Rest", card("bdsc", "Xưởng Cát Lái"), W216), cell("Hover", card("bdsc", "Xưởng Cát Lái", "hv"), W216),
        cell("Focus (bàn phím)", card("bdsc", "Xưởng Cát Lái", "fc"), W216), cell("Đang mở hộp thoại", card("bdsc", "Xưởng Cát Lái", "pr"), W216),
        cell("Chỉ 1 phạm vi — không bấm được", card("bdsc", "Xưởng Cát Lái", "ro", chev=False), W216),
        cell("Chữ dài — cắt 1 dòng, tooltip đủ", card("bdsc", LONG_FAC, s1="Bảo dưỡng sửa chữa container lạnh"), W216),
        cell("Thu gọn 64", f'<div class="colx" style="width:64px;padding:0 10px"><button class="sc bot pr">{tile("bdsc")}</button></div>', "68px")])
    lg = lambda br: (f'<div class="lg" style="margin:0"><span class="lt"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span><span class="lnw"><span class="ln">Delta Logistics</span>'
                     f'<span class="lnb">{br}</span></span><button class="ib">{ic("panel", 20)}</button></div>')
    h += row("Đầu menu — đơn vị và chi nhánh", [cell("Chi nhánh", lg("CN Hồ Chí Minh"), W216), cell("Công ty mẹ (quyền xem tổng)", lg("Toàn tổ chức"), W216),
                                                 cell("Chữ dài", lg(LONG_BR), W216)])
    h += row("Mục menu", [
        cell("Rest", item("file", "Báo giá sửa chữa"), W216), cell("Hover", item("file", "Báo giá sửa chữa", "hv"), W216),
        cell("Đang chọn", item("clip", "Lệnh sửa chữa", "on"), W216), cell("Focus", item("file", "Báo giá sửa chữa", "fc"), W216),
        cell("Có số đếm", item("alert", "Sự cố phương tiện", badge="3"), W216), cell("Đang chọn + số đếm", item("clip", "Lệnh sửa chữa", "on", "12"), W216),
        cell("Chữ dài — cắt 1 dòng, tooltip", item("wallet", "Thanh toán mua hàng và bồi thường hàng hoá dịch vụ"), W216),
        cell("Nhãn nhóm", '<div class="gt" style="padding:6px 10px">Kho và mua hàng</div>', W216),
        cell("Thu gọn + tooltip", f'<div class="colx" style="position:relative;width:200px"><div class="sb" style="width:68px;border:0;padding:0 12px">{item("clip", "Lệnh sửa chữa", "on")}</div>'
             f'<span class="tip">Lệnh sửa chữa</span></div>', W216)])
    full = lambda col: (f'<div class="{"colx" if col else ""}" style="height:640px;display:flex;border:1px solid var(--color-border-secondary);border-radius:10px;overflow:hidden">'
                        f'{sidebar("bdsc", "Lệnh sửa chữa")}</div>')
    h += row("Menu đầy đủ", [cell("Mở rộng 240", full(False), "242px"), cell("Thu gọn 64", full(True), "66px")])
    h += row("Hộp thoại đổi phạm vi (3 cột)", [cell("Mặc định — module có xưởng", f'<div class="pcm static">{popover("bdsc").split("<div class=\"pcm\" data-show=\"D4:c\">")[1]}', "960px"),
                                                cell("Module không chia cơ sở", f'<div class="pcm static">{popover("dpvt").split("<div class=\"pcm\" data-show=\"D4:c\">")[1]}', "960px")],
                 "Chọn theo thứ tự 1 → 2 → 3, bấm Chọn mới chuyển. Có tìm ở cột chi nhánh. Công ty mẹ chỉ hiện khi có quyền xem tổng.")
    return pvwrap(h, "web")

def grid_mob():
    W = "361px"
    h = row("Thẻ phạm vi — tab Tài khoản", [
        cell("Có cơ sở", mcard("bdsc", "CN Hồ Chí Minh · Xưởng Cát Lái"), W), cell("Không chia cơ sở", mcard("dpvt", "CN Hồ Chí Minh"), W),
        cell("Cấp công ty", mcard("dm", "Toàn công ty"), W), cell("Chỉ 1 phạm vi — không bấm được", mcard("bdsc", "CN Hồ Chí Minh · Xưởng Cát Lái", chev=False), W),
        cell("Chữ dài", mcard("bdsc", f"{LONG_BR} · {LONG_FAC}", s1="Bảo dưỡng sửa chữa container lạnh"), W)])
    h += row("Dòng phạm vi ở Trang chủ — chỉ để đọc", [
        cell("Có cơ sở", f'<div class="mctx ro" style="padding:0">{tile("bdsc", 20)}<span class="tx">Bảo dưỡng sửa chữa<span class="dot">·</span>Xưởng Cát Lái</span></div>', W),
        cell("Chữ dài", f'<div class="mctx ro" style="padding:0">{tile("bdsc", 20)}<span class="tx">Bảo dưỡng sửa chữa<span class="dot">·</span>{LONG_FAC}</span></div>', W)])
    h += row("Thanh tab dưới (4 tab)", [cell("Trang chủ", tabs("home"), W), cell("Tài khoản", tabs("user"), W)])
    h += row("Mục chức năng (tab Tài khoản)", [cell("Rest / Pressed / số đếm", '<div class="mnv">'
             + f'<a class="mit">{ic("file")}<span class="t">Báo giá sửa chữa</span>{ic("cr", 16)}</a>'
             + f'<a class="mit pr">{ic("file")}<span class="t">Báo giá sửa chữa</span>{ic("cr", 16)}</a>'
             + f'<a class="mit">{ic("clip")}<span class="t">Lệnh sửa chữa</span><span class="bd">12</span>{ic("cr", 16)}</a></div>', W)])
    return pvwrap(h, "mobile")

CSS2 = r"""
:is(.pv[data-state=collapsed],.colx) .lnw{display:none!important}
.pv[data-state=collapsed] .sc.bot,.colx .sc.bot{display:grid!important;place-items:center;padding:4px;width:44px;margin:0 auto;border:0!important;box-shadow:none}
.pv[data-state=collapsed] .sc.bot .st,.pv[data-state=collapsed] .sc.bot .ud,.colx .sc.bot .st,.colx .sc.bot .ud{display:none}
.sc.hv{background:var(--color-bg-primary_hover)}.sc.pr{background:var(--color-bg-pressed)}.sc.fc,.it.fc{outline:2px solid var(--color-focus-ring);outline-offset:2px}.sc.ro{box-shadow:none;cursor:default}
.it.hv{background:var(--color-bg-primary_hover)}
.tip{position:absolute;left:62px;top:4px;background:var(--color-bg-primary_solid);color:var(--color-text-inverse);font:500 12px/18px Inter,system-ui,sans-serif;padding:4px 8px;border-radius:6px;white-space:nowrap}
.pcm.static{position:static;transform:none;width:960px;box-shadow:var(--elev-3);border-radius:12px;background:var(--color-bg-primary_alt)}
.mfull{position:absolute;inset:0;z-index:30;background:var(--color-bg-primary);display:flex;flex-direction:column;padding-top:44px}
.pfh.m{margin:0 0 10px;font-size:13px}
.mctx.ro .tx{color:var(--color-text-secondary)}.mctx .dot{padding:0 4px;flex:none}
.ascr{overflow:hidden;padding-bottom:12px}
.apf{display:flex;align-items:center;gap:12px;padding:4px 16px 8px}.apf .hi span{font-size:13px}
.sect2{font:600 13px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);padding:14px 16px 6px}
.mpx0{padding:0 16px}.mnv.acc{padding:0 4px}
.agrp{margin:0 16px;border:1px solid var(--color-border-secondary);border-radius:14px;overflow:hidden}
.arow{display:flex;align-items:center;gap:12px;min-height:52px;padding:0 14px;border-top:1px solid var(--color-border-secondary);color:var(--color-text-secondary)}.arow:first-child{border-top:0}.arow .o1{font:500 15px/22px Inter,system-ui,sans-serif;color:var(--color-text-primary)}
.arow.dg,.arow.dg .o1{color:var(--color-text-error-primary)}
.mit.pr{background:var(--color-bg-pressed)}
.shp{margin:0;padding:0 16px 12px;color:var(--color-text-tertiary);font-size:14px}.shf.two{display:flex;gap:8px}.cta.sec{background:var(--color-bg-primary)!important;color:var(--color-text-primary)!important;border:1px solid var(--color-border-primary)!important}
.dgrid{display:grid;grid-template-columns:360px 1fr;gap:16px;align-items:start}.dgrid .card{display:flex;flex-direction:column;gap:12px}
"""
page["css"] = CSS.replace(".pv[data-state=collapsed]", ":is(.pv[data-state=collapsed],.colx)") + CSS2
page["round"] = "preview"
page["subtitle"] = "Application component · nhóm C · vòng 2 Preview — tổ hợp đã chốt: " + " · ".join(f"{k} {v.upper()}" for k, v in PICK.items())
page["preview"] = {"version": "1", "pick": PICK,
                   "changes": "bản đầu theo lựa chọn vòng 1; D7 C sửa theo ghi chú: không thêm tab Menu, thẻ phạm vi + chức năng nằm ở tab Tài khoản",
                   "blocks": [{"title": "Web", "platform": "web", "note": "Menu 240 · thu gọn 64 · hộp thoại 960", "html": grid_web()},
                              {"title": "Mobile", "platform": "mobile", "note": "Khung 393, lề 16", "frames": [grid_mob()]}]}


# Khai giá trị preview — vòng 3 đối chiếu foundation (ds-foundation-check.py)
V = []
def v(part, prop, value, **kw):
    V.append({"part": part, "prop": prop, "value": value, **kw})
W_, M_ = {"platform": "Web"}, {"platform": "Mobile"}
v("Sidebar", "width", 240, **W_); v("Sidebar collapsed", "width", 64, **W_); v("Sidebar", "padding", 12, **W_); v("Sidebar collapsed", "padding-x", 10, **W_)
v("Sidebar", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF")
v("Header", "min-height", 36, **W_); v("Header", "gap", 8, **W_); v("Header", "margin", 12, **W_)
v("Logo", "size", 28); v("Logo", "radius", 8)
v("Tenant name", "font-size", 14); v("Tenant name", "line-height", 24); v("Tenant name", "font-weight", 600); v("Tenant name", "color", "#171717", role="text", on="#FFFFFF")
v("Branch", "font-size", 12); v("Branch", "line-height", 16); v("Branch", "color", "#737373", role="text", on="#FFFFFF")
v("Collapse button", "size", 32, **W_, interactive=True, hitArea=32); v("Collapse button", "radius", 8); v("Collapse icon", "icon-size", 20)
v("Scope card", "padding", 8, **W_); v("Scope card", "gap", 10, **W_); v("Scope card", "radius", 10, **W_); v("Scope card", "height", 52, **W_, interactive=True, hitArea=52)
v("Scope card", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF"); v("Scope card", "shadow", "0 1px 2px rgba(10,13,18,.05)")
v("Scope card hover", "background", "#FAFAFA", state="hover"); v("Scope card open", "background", "#F5F5F5", state="open")
v("Module tile", "size", 32, **W_); v("Module tile", "radius", 8); v("Module tile icon", "icon-size", 20)
v("Scope title", "font-size", 14); v("Scope title", "line-height", 20); v("Scope title", "font-weight", 600); v("Scope title", "color", "#171717", role="text", on="#FFFFFF")
v("Scope subtitle", "font-size", 12); v("Scope subtitle", "line-height", 18); v("Scope subtitle", "color", "#737373", role="text", on="#FFFFFF")
v("Chevron", "icon-size", 16); v("Chevron", "color", "#737373", role="icon", on="#FFFFFF")
v("Nav", "gap", 2, **W_)
v("Nav item", "height", 36, **W_, interactive=True, hitArea=36); v("Nav item", "padding-x", 10, **W_); v("Nav item", "gap", 10, **W_); v("Nav item", "radius", 8, **W_)
v("Nav item label", "font-size", 14); v("Nav item label", "line-height", 20); v("Nav item label", "font-weight", 500); v("Nav item label", "color", "#525252", role="text", on="#FFFFFF")
v("Nav item icon", "icon-size", 20); v("Nav item icon", "color", "#737373", role="icon", on="#FFFFFF")
v("Nav item hover", "background", "#FAFAFA", state="hover")
v("Nav item active", "background", "#F5F5F5", state="active"); v("Nav item active label", "color", "#171717", role="text", on="#F5F5F5", state="active"); v("Nav item active label", "font-weight", 600, state="active")
v("Badge", "font-size", 12); v("Badge", "line-height", 18); v("Badge", "padding-x", 8); v("Badge", "radius", 9999); v("Badge", "background", "#F5F5F5")
v("Badge", "border-color", "#E5E5E5", role="decorative", on="#F5F5F5"); v("Badge", "color", "#525252", role="text", on="#F5F5F5")
v("Group label", "font-size", 12); v("Group label", "line-height", 16); v("Group label", "font-weight", 600); v("Group label", "color", "#737373", role="text", on="#FFFFFF")
v("Group label", "padding-top", 16, **W_); v("Group label", "padding-bottom", 6, **W_); v("Group label", "padding-x", 10, **W_)
v("Focus ring", "focus-width", 2); v("Focus ring", "focus-offset", 2); v("Focus ring", "color", "#171717", role="border", on="#FFFFFF")
v("Tooltip", "font-size", 12); v("Tooltip", "line-height", 18); v("Tooltip", "padding-x", 8); v("Tooltip", "padding-y", 4); v("Tooltip", "radius", 6)
v("Tooltip", "background", "#171717"); v("Tooltip", "color", "#FFFFFF", role="text", on="#171717")
v("Dialog", "width", 960, **W_); v("Dialog", "radius", 12, **W_); v("Dialog", "shadow", "elev/3")
v("Dialog header", "padding-x", 20, **W_); v("Dialog header", "padding-y", 16, **W_); v("Dialog title", "font-size", 17); v("Dialog title", "line-height", 24); v("Dialog title", "font-weight", 600)
v("Dialog column", "padding", 8, **W_); v("Column title", "font-size", 12); v("Column title", "font-weight", 600); v("Column title", "color", "#737373", role="text", on="#FFFFFF")
v("Option", "padding", 8, **W_, interactive=True, hitArea=44); v("Option", "gap", 10); v("Option", "radius", 8)
v("Option title", "font-size", 14); v("Option title", "line-height", 20); v("Option title", "font-weight", 500)
v("Option sub", "font-size", 12); v("Option sub", "line-height", 18); v("Option sub", "color", "#737373", role="text", on="#FFFFFF")
v("Option selected", "background", "#F5F5F5", state="selected"); v("Option icon box", "size", 28); v("Option icon box", "radius", 8)
v("Check", "icon-size", 16); v("Check", "color", "#171717", role="icon", on="#F5F5F5")
v("Search", "height", 32, **W_, control=True, interactive=True, hitArea=32); v("Search", "radius", 8); v("Search", "padding-x", 10); v("Search", "border-color", "#737373", role="border", on="#FFFFFF")
v("Dialog footer", "padding-x", 16, **W_); v("Dialog footer", "padding-y", 12, **W_); v("Dialog footer", "gap", 8)
v("Dialog button", "height", 40, **W_, control=True, interactive=True, hitArea=40); v("Dialog button", "radius", 8); v("Dialog button", "padding-x", 12)
v("Scrim", "background", "rgba(10,13,18,.45)")
v("Mobile scope card", "padding-x", 12, **M_); v("Mobile scope card", "padding-y", 10, **M_); v("Mobile scope card", "gap", 12, **M_); v("Mobile scope card", "radius", 14, **M_)
v("Mobile scope card", "min-height", 60, **M_, interactive=True, hitArea=60); v("Mobile module tile", "size", 36, **M_)
v("Tab bar", "height", 64, **M_); v("Tab icon", "icon-size", 24, **M_); v("Tab", "width", 98, **M_, interactive=True, hitArea=64)
v("Tab inactive", "color", "#737373", role="icon", on="#FFFFFF"); v("Tab active", "color", "#171717", role="icon", on="#FFFFFF")
v("Mobile nav item", "min-height", 48, **M_, interactive=True, hitArea=48); v("Mobile nav item", "padding-x", 12, **M_); v("Mobile nav item", "gap", 12, **M_); v("Mobile nav item", "radius", 10, **M_)
v("Mobile nav label", "font-size", 15, **M_); v("Mobile nav label", "line-height", 22, **M_)
v("Section label", "font-size", 13, **M_); v("Section label", "line-height", 18, **M_); v("Section label", "color", "#737373", role="text", on="#FFFFFF")
v("Account row", "min-height", 52, **M_, interactive=True, hitArea=52); v("Account group", "radius", 14, **M_)
v("Picker option", "min-height", 48, **M_, interactive=True, hitArea=48)
v("Picker CTA", "height", 52, **M_, control=True, interactive=True, hitArea=52); v("Picker CTA", "radius", 14, **M_)
v("Radio", "size", 18, **M_); v("Radio", "border-color", "#D4D4D4", role="border", on="#FFFFFF")
v("Home scope line", "font-size", 13, **M_); v("Home scope line", "color", "#525252", role="text", on="#FFFFFF")
for t, (fg, bg) in {"blue": ("#1F4FB8", "#E7EFFD"), "teal": ("#0B6B64", "#E2F5F4"), "amber": ("#8A5300", "#FFF3DC"),
                    "green": ("#1B7542", "#E8F5EC"), "violet": ("#5536C4", "#EFEAFE"), "gray": ("#404040", "#F0F0F0")}.items():
    v(f"Module tile {t}", "background", bg); v(f"Module tile icon {t}", "color", fg, role="icon", on=bg)
page["values"] = V


# ================= Duyệt preview bản 1 (28/10): "Chưa cần dựng bản mobile app, số đếm màu xanh dương" =================
page["css"] += ".bd{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700);border-color:transparent}.pv[data-D6=a] .it.on .bd{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}"
page["screens"] = [sc for sc in page["screens"] if sc.get("device") != "mobile"]
page["preview"]["blocks"] = [b for b in page["preview"]["blocks"] if b["platform"] != "mobile"]
page["preview"]["changes"] = "duyệt bản 1 kèm ghi chú: bỏ phần app (chưa dựng), số đếm nền xanh dương nhạt chữ xanh dương đậm"
page["subtitle"] = page["subtitle"].replace("nhóm C", "nhóm C · đợt này chỉ Web")
page["values"] = [x for x in page["values"] if x.get("platform") != "Mobile" and not x["part"].startswith(("Mobile", "Tab", "Section label", "Account", "Picker", "Radio", "Home scope"))]
for x in page["values"]:
    if x["part"] == "Badge" and x["prop"] == "background": x["value"] = "#E7EFFD"
    if x["part"] == "Badge" and x["prop"] == "color": x.update(value="#1F4FB8", on="#E7EFFD")
page["values"] = [x for x in page["values"] if not (x["part"] == "Badge" and x["prop"] == "border-color")]


# Khai đúng tên token cho 2 giá trị khai sai dạng (không phải quyết định thiết kế)
for x in page["values"]:
    if x["part"] == "Scope card" and x["prop"] == "shadow": x["value"] = "elev/1"
    if x["part"] == "Scrim": x["value"] = "color/bg/overlay"
page["round"] = "foundation"
page["css"] += ".pcm .pf .bt{height:40px!important;padding:0 12px!important}"
page["preview"]["version"] = "1"; page["preview"]["changes"] += "; vòng 3: menu thu gọn 64, hộp thoại 960, ô tìm 32 viền border/input, nút hộp thoại 40, chữ và icon kéo về token, màu ô module theo token chip"

# ---------- Vòng 5 — Review Figma (3 agent, 28/10) ----------
page["round"] = "review"
page["figma"] = {"url": "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=6768-190829",
                 "label": "Section Sidebar navigation (+ Demo 6768:204061, khung Phạm vi làm việc 6896:212951)"}
R = lambda i, ag, sev, node, look, text, fix: {"id": i, "agent": ag, "severity": sev, "node": node, "changesLook": look, "text": text, "fix": fix}
page["reviews"] = [
 R("R1", "accessibility", "Cao", "6896:205512", True, "<b>1.4.3 — dòng phụ trên nền chọn chỉ 4,35:1</b>: <code>text/tertiary</code> trên <code>bg/selected</code> (thẻ Open, dòng Selected trong hộp thoại). Trên nền trắng 4,74:1 đạt. Spec đang ghi sai \"≥ 4,5:1\".",
   "A (đề xuất): dòng phụ trên nền chọn/hover dùng chữ đậm hơn một bậc (neutral-600, ~7:1). B: làm nhạt <code>bg/selected</code> (sát ngưỡng). Cả hai đổi màu so với preview đã duyệt."),
 R("R2", "accessibility", "Cao", "6896:213729", False, "<b>2.4.7 — <code>_Scope option</code> thiếu Focus</b> (dòng chọn bằng mũi tên không có mẫu vòng focus).", "<b>Đã sửa:</b> thêm State=Focus (vòng 2px cách 2px, như thẻ)."),
 R("R3", "uxui-reviewer", "Cao", "6896:212951", False, "<b>Thiếu 2 trạng thái spec nêu</b>: \"Đổi khi chưa lưu\" (hỏi xác nhận GR-13) và \"Đang chuyển\" (vùng nội dung khung chờ, menu giữ nguyên).",
   "Thêm 2 khung vào khung tài liệu: hộp \"Rời trang khi chưa lưu?\" · Ở lại · Rời trang và chuyển; và màn đang chuyển (nút Chọn đang xử lý, nội dung khung chờ). Không đổi look."),
 R("R4", "uxui-reviewer", "Cao", "6896:205795", False, "<b>Bản Facility=None ghi \"Đang chọn: Bảo dưỡng sửa chữa\"</b> trong khi cột 2 chọn Điều phối vận tải.",
   "<b>Đã sửa</b> ở khung tài liệu và demo bằng thuộc tính <code>Selection</code>. Main component chỉ giữ được một giá trị mặc định cho mọi biến thể (giới hạn của thuộc tính TEXT)."),
 R("R5", "uxui-reviewer", "Trung", "6896:205519", False, "<b>Nút Chọn luôn bật</b>, chưa có quy tắc tắt khi chưa đổi gì hoặc module có cơ sở mà chưa chọn cơ sở; cột 3 chưa có trạng thái \"chưa chọn\".",
   "Cần quyết quy tắc: tắt Chọn khi lựa chọn trùng phạm vi hiện tại hoặc thiếu cơ sở (đề xuất). Rồi ghi spec + thêm khung."),
 R("R6", "uxui-reviewer", "Trung", "6896:206071", False, "<b>Hộp thoại thiếu rỗng / lỗi / đang tải</b>: tìm chi nhánh không ra, tải danh sách lỗi, và chọn công ty mẹ (Toàn tổ chức) thì cột 2–3 hiện gì.",
   "Rỗng giữa cột (cùng kiểu cột 3 hiện có), lỗi cột + Thử lại. Chọn công ty mẹ: cần quyết — đề xuất cột 3 báo \"Toàn tổ chức · dữ liệu cả công ty\"."),
 R("R7", "uxui-reviewer", "Trung", "6896:205519", False, "<b>Chỉ minh hoạ module Xưởng</b>; chưa có Quản lý dầu (Tất cả cây dầu, 2 cây dầu, dòng hệ thống \"Ngoài cơ sở\").", "Thêm một khung hộp thoại Quản lý dầu vào khung tài liệu. Không đổi look."),
 R("R8", "uxui-reviewer", "Trung", "6896:205467", False, "<b>Thiếu hình tooltip</b>: thẻ thu gọn (tên module · cơ sở), thẻ chữ dài (tên đủ), thẻ Read-only (\"Chỉ có một phạm vi làm việc\"); bản thu gọn chưa có Hover/Read-only trong khung tài liệu.",
   "Thêm các ô có Tooltip vào khung tài liệu; ghi tooltip Read-only vào spec. Không đổi look."),
 R("R9", "accessibility", "Trung", "6896:206071", False, "<b>Spec thiếu luật bàn phím và đọc màn hình</b>: giữ focus trong hộp thoại + thứ tự Tab (2.1.2/2.4.3), nhãn ô tìm (3.3.2), cột 3 đổi danh sách phải được báo (4.1.3), nút đóng aria-label \"Đóng\", thẻ Read-only không phải nút, thẻ thu gọn đọc đủ phạm vi (4.1.2); reflow khi zoom 400% (1.4.10).",
   "Sửa chữ trong spec mục Trợ năng (không đổi look). Reflow: dưới 768 px dùng bản app như mục Kích thước đã ghi."),
 R("R10", "accessibility", "Thấp", "6768:194161", False, "<b>Spec ghi sai/thiếu so với Figma</b>: token vòng focus là <code>color/focus/ring</code> (spec ghi text/primary); thẻ thu gọn 40 (ô 32); thuộc tính mới <code>Has Tenant Name</code>, <code>Tenant Name</code> chưa có trong mục Thuộc tính.", "Sửa spec (L2) cùng lượt với Bước 9."),
 R("R11", "visual-reviewer", "Trung", "6768:202878", True, "<b>Thẻ phạm vi và thẻ tài khoản xếp chồng cùng trọng lượng</b> ở chân menu; thẻ tài khoản cao hơn nên mắt dừng ở đó trước, dù phạm vi quyết định dữ liệu đang xem.",
   "Giữ vị trí; làm thẻ tài khoản nhẹ hơn (bỏ viền hoặc thu thấp). Hoặc giữ nguyên."),
 R("R12", "visual-reviewer", "Trung", "6768:202878", False, "<b>Phạm vi tách hai nơi</b>: chi nhánh ở đầu menu, module + cơ sở ở chân. Dòng chi nhánh không có dấu hiệu bấm được.",
   "Đã chốt ở D1 (DEC-288). Đề xuất giữ, ghi spec \"dòng chi nhánh chỉ để đọc, đổi qua thẻ phạm vi\"."),
 R("R13", "visual-reviewer", "Trung", "6768:203426", False, "<b>Bản thu gọn hiện avatar \"HP\"</b> (dễ đọc thành Hải Phòng) trong khi bản mở rộng là logo DELTA và chi nhánh HCM.", "Đổi dữ liệu demo: chữ viết tắt đúng đơn vị (DL)."),
 R("R14", "visual-reviewer", "Trung", "6896:204887", False, "<b>6 sắc ô module trùng nghĩa màu trạng thái</b> (vàng, xanh lá).", "Màu đã duyệt (DEC-288): giữ, ghi spec \"màu phân loại module, không mang nghĩa trạng thái; luôn đi cùng tên\"."),
 R("R15", "visual-reviewer", "Thấp", "6896:205515", True, "<b>Hover / Open / Selected gần giống nhau</b>; Selected chỉ hơn Hover ở dấu ✓.", "Nền selected đậm hơn một bậc hoặc vạch trái. Hoặc giữ (dấu ✓ + chữ đậm đã phân biệt)."),
 R("R16", "visual-reviewer", "Thấp", "6896:212160", True, "<b>Dòng \"Đang chọn: …\" nhỏ, xám</b>, bị hai nút lấn át.", "Tên module · chi nhánh dùng <code>text/primary</code>, nhãn \"Đang chọn\" giữ xám."),
 R("R17", "visual-reviewer", "Thấp", "6768:203426", True, "<b>Bản thu gọn</b>: ô phạm vi sát avatar cùng cỡ, mất phân nhóm giữa các mục.", "Thêm khoảng cách / vạch chia giữa nhóm khi thu gọn. Hoặc giữ."),
 R("R18", "visual-reviewer", "Thấp", "6896:206354", False, "<b>Bản Width=64 trong khung tài liệu toàn icon giữ chỗ</b>.", "Không đổi: main component mọi biến thể đều dùng icon giữ chỗ; demo 6768:203426 đã có icon thật."),
 R("R19", "máy", "Thấp", "6768:194161", False, "<b>Kiểm tên (DEC-264)</b>: giá trị Type \"Sections Subheadings\", \"Sections Dividers\" dài hơn 16 ký tự — có sẵn từ trước, đổi tên đụng mọi instance.", "Cần quyết: giữ, hoặc đổi thành \"Subheadings\" / \"Dividers\"."),
 R("R20", "accessibility", "Thấp", "6658:172078", False, "<b>Ngoài phạm vi</b>: placeholder của Base Input 2,52:1.", "Mở việc riêng cho component Base."),
]

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import tok_css_nested  # noqa: E402
page["css"] = tok_css_nested() + page["css"]
OUT.write_text(json.dumps(page, ensure_ascii=False, indent=1))
print("ok", OUT, len(ideas), "ý tưởng ·", len(decisions), "điểm ·", len(page["screens"]), "màn")
