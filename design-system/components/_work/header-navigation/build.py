# Sinh page.json cho /figma-component header-navigation --html (vòng 1 Brainstorm)
# Gồm 2 component: Header navigation (thanh trên web) + Breadcrumbs (phần lồng trong thanh trên / đầu trang).
# Chạy: python3 design-system/components/_work/header-navigation/build.py && python3 _scripts/ds-component-page.py header-navigation
# Nguồn chốt biến thể: trang Application (https://claude.ai/artifact/L3pzcVoU11rCka42c9tHoS) thẻ headernav + breadcrumb,
# đã xác nhận 27/10: Layout Simple + Secondary Nav · Height 56 · Border Bottom · Search, Bell, Account, Help, Breadcrumbs;
# Breadcrumbs Type Text / Text Line / Button · Chevron · Home, Ellipsis, Current · Default / Hover / Focus · chỉ web.
import json
from pathlib import Path
from bs4 import BeautifulSoup

OUT = Path(__file__).parent / "page.json"

# ---------- icon (Lucide, nét 2) ----------
P = {
 "home": '<path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h8"/>',
 "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 "file": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 13h6M9 17h4"/>',
 "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21c1-4 4-6 7-6s6 2 7 6M16 3a4 4 0 0 1 0 8M22 21c-.5-2.5-2-4.3-4-5.2"/>',
 "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "wallet": '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18M16 15h2"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
 "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17h.01"/>',
 "cr": '<path d="M9 6l6 6-6 6"/>',
 "cd": '<path d="M6 9l6 6 6-6"/>',
 "ud": '<path d="M8 9l4-4 4 4M8 15l4 4 4-4"/>',
 "left": '<path d="M15 6l-6 6 6 6"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "out": '<path d="M15 4h4a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-4M10 17l5-5-5-5M15 12H3"/>',
 "dots": '<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
 "enter": '<path d="M20 5v7a3 3 0 0 1-3 3H5M9 11l-4 4 4 4"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin": '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "chev2": '<path d="M7 15l5 5 5-5M7 9l5-5 5 5"/>',
}

def ic(k, s=18):
    return (f'<svg class="i" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[k]}</svg>')


# ---------- hiện khi MỘT trong các điều kiện đúng (kit chỉ có data-show = AND) ----------
ANY = set()
def A(*conds):
    v = " ".join(conds); ANY.add(v)
    return f' data-any="{v}"'

def any_css():
    out = []
    for v in sorted(ANY):
        k = v.split()[0].split(":")[0]
        nots = "".join(f':not([data-{k}="{c.split(":")[1]}"])' for c in v.split())
        out.append(f'.pv{nots} [data-any="{v}"]')
    return ",".join(out) + "{display:none!important}" if out else ""

def resolve(html, pick, state):
    """Bỏ nhánh data-show / data-any không khớp tổ hợp — ô xem trước nhỏ nằm trong .pv không mang thuộc tính của kit."""
    ok = lambda c: state == c[6:] if c.startswith("state:") else pick.get(c.split(":")[0]) == c.split(":")[1]
    soup = BeautifulSoup(html, "html.parser")
    for attr, test in (("data-show", all), ("data-any", any)):
        for el in soup.find_all(attrs={attr: True}):
            if el.decomposed:
                continue
            if test(ok(c) for c in el[attr].split()):
                del el[attr]
            else:
                el.decompose()
    return str(soup)

# ---------- trạng thái ----------
STATES = [("default", "Mặc định"), ("search", "Đang tìm tính năng"), ("noresult", "Tìm không thấy"),
          ("notif", "Mở thông báo"), ("account", "Mở menu tài khoản"), ("zero", "Không có thông báo"),
          ("long", "Chữ dài · đường dẫn sâu")]
SK = [k for k, _ in STATES]

def sv(default, **over):
    """Chữ đổi theo trạng thái."""
    return "".join(f'<span data-show="state:{k}">{over.get(k, default)}</span>' for k in SK)

NAME = sv("Nguyễn Anh", long="Nguyễn Thị Phương Thảo")
NAME_FULL = sv("Nguyễn Văn Anh", long="Nguyễn Thị Phương Thảo")
ROLE = sv("Điều độ viên · CN Hồ Chí Minh", long="Trưởng phòng Điều phối vận tải · CN Bà Rịa – Vũng Tàu")
INIT = sv("NA", long="PT")

# ---------- breadcrumb ----------
def crumb(items, cur, deep=None):
    """items: các tầng trên; cur: trang hiện tại. deep: đường dẫn dài dùng ở state long (D7 xử lý)."""
    def one(path, last, extra=""):
        sep = f'<span class="sep">{ic("cr", 14)}</span>'
        home = f'<a class="ci hm" aria-label="Trang chủ">{ic("home", 16)}</a>'
        mid = []
        n = len(path)
        for i, t in enumerate(path):
            hide = A("D7:b", "D7:c") if (n > 2 and 0 < i < n - 1) else ""
            sib = f'<span class="sib" data-show="D7:c">{ic("cd", 12)}</span>'
            mid.append(f'<span class="cw"{hide}>{sep}<a class="ci">{t}{sib}</a></span>')
        ell = (f'<span class="cw" data-show="D7:a">{sep}<button class="ci el" aria-label="Hiện các tầng ẩn">{ic("dots", 16)}</button></span>'
               if n > 2 else "")
        # thứ tự: nhà · tầng 1 · … · tầng giữa · tầng cuối · hiện tại
        body = mid[0] + ell + "".join(mid[1:]) if mid else ""
        return (f'<nav class="bc" aria-label="Đường dẫn" data-cmp{extra}>{home}{body}{sep}'
                f'<span class="ci cur" aria-current="page">{last}</span></nav>')
    if deep:
        return (f'<span{A("state:default", "state:search", "state:noresult", "state:notif", "state:account", "state:zero")}>{one(items, cur)}</span>'
                f'<span data-show="state:long">{one(deep[0], deep[1])}</span>')
    return one(items, cur)

# ---------- các phần của thanh trên ----------
def search_box():
    return (f'<div class="sbx"{A("D2:a", "D2:c")} data-cmp>{ic("search", 16)}<span class="ph">Tìm tính năng, màn…</span>'
            f'<span class="q q1">lệnh</span><span class="q q2">bảo hiểm</span><kbd>⌘K</kbd></div>'
            f'<button class="ib" data-show="D2:b" aria-label="Tìm tính năng (⌘K)" data-cmp>{ic("search", 20)}</button>')

def bell():
    return (f'<button class="ib bell" aria-label="Thông báo" data-cmp>{ic("bell", 20)}'
            f'<i class="nd" data-show="D5:a"></i><b class="nc"{A("D5:b", "D5:c")}>{sv("3", long="9+")}</b></button>')

def account():
    return (f'<button class="acc" aria-label="Tài khoản" data-cmp><span class="av">{INIT}</span>'
            f'<span class="nm"{A("D4:a", "D4:c")}><span class="n1">{NAME}</span>'
            f'<span class="n2" data-show="D4:c">{ROLE}</span></span>'
            f'<span class="cv"{A("D4:a", "D4:c")}>{ic("cd", 16)}</span></button>')

def palette():
    def row(icon, t, sub, k="", on=False):
        return (f'<div class="pr{" on" if on else ""}"><span class="pi">{ic(icon, 16)}</span><span class="pt"><span class="pt1">{t}</span>'
                f'<span class="ps">{sub}</span></span>{f"<kbd>{k}</kbd>" if k else ""}'
                f'{ic("enter", 14) if on else ""}</div>')
    hit = '<mark>Lệnh</mark>'
    res = (f'<div class="pg">Tính năng</div>'
           + row("route", f"{hit} vận tải", "Điều phối vận tải › Danh sách", on=True)
           + row("file", f"{hit} sửa chữa", "Bảo dưỡng sửa chữa › Danh sách")
           + row("wallet", f"{hit} chi tạm ứng", "Quỹ & thanh toán")
           + f'<div' + A("D3:b", "D3:c") + '><div class="pg">Hành động</div>'
           + row("plus", f"Tạo {hit.lower()} vận tải", "Mở form tạo mới", "N")
           + row("plus", f"Tạo {hit.lower()} sửa chữa", "Mở form tạo mới")
           + '</div><div data-show="D3:c"><div class="pg">Bản ghi</div>'
           + row("route", "LVT-2026-0412", "Cát Lái → Sóng Thần · Đang chạy")
           + '</div>')
    empty = ('<div class="pe" data-show="state:noresult"><b>Không có tính năng “bảo hiểm”</b>'
             '<span>Thử từ khác, hoặc tính năng chưa được cấp quyền cho tài khoản này.</span></div>')
    return (f'<div class="pal"{A("state:search", "state:noresult")} role="dialog" aria-label="Tìm tính năng">'
            f'<div class="pin" data-show="D2:b">{ic("search", 18)}<span>lệnh</span><kbd>Esc</kbd></div>'
            f'<div data-show="state:search">{res}</div>{empty}'
            f'<div class="pf"><span><kbd>↑</kbd><kbd>↓</kbd> chọn</span><span><kbd>↵</kbd> mở</span>'
            f'<span>Chỉ hiện tính năng bạn có quyền</span></div></div>'
            f'<div class="scr" data-show="D2:b"{A("state:search", "state:noresult")}></div>')

def acc_menu(n=None, r=None, i=None, show=' data-show="state:account"', cls="am"):
    def it(icon, t, extra="", cls=""):
        return f'<div class="mi {cls}">{ic(icon, 16)}<span>{t}</span>{extra}</div>'
    return (f'<div class="{cls}"{show} role="menu">'
            f'<div class="mh"><span class="av lg">{i or INIT}</span><div><b>{n or NAME_FULL}</b><span>{r or ROLE}</span></div></div>'
            + it("user", "Thông tin cá nhân") + it("key", "Đổi mật khẩu")
            + it("globe", "Ngôn ngữ", '<span class="mv" style="display:inline-flex;align-items:center;gap:var(--space-xs)"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" style="flex:none"><circle cx="12" cy="12" r="12" fill="#DA251D"/><path d="M12 5.2l1.6 4.9h5.1l-4.1 3 1.6 4.9-4.2-3-4.2 3 1.6-4.9-4.1-3h5.1z" fill="#FFCD00"/></svg>Tiếng Việt</span>')
            + '<div class="msep"></div>' + it("out", "Đăng xuất", cls="dng") + '</div>')

def notif_panel():
    def n(t, code, meta, unread=True):
        return (f'<div class="nr{" un" if unread else ""}"><i class="ud"></i><div><div>{t}</div><b class="mono">{code}</b>'
                f'<span class="ps">{meta}</span></div></div>')
    return (f'<div class="np" data-show="state:notif"><div class="nh"><b>Thông báo</b><span class="lk">Đánh dấu là đã đọc</span></div>'
            f'<div class="ntab"><span class="on">Cần xử lý <b>3</b></span><span>Tất cả</span></div>'
            + n("Chờ bạn duyệt lệnh vận tải", "LVT-2026-0418", "Trần Văn Bình · Điều phối vận tải · 5 phút")
            + n("Chờ bạn duyệt đề nghị tạm ứng", "TU-2026-0211", "Lê Minh Châu · Quỹ & thanh toán · 1 giờ")
            + n("Lệnh vận tải vừa bị từ chối", "LVT-2026-0402", "Phạm Quốc Huy · hôm qua", False) + '</div>')

def header(path, cur, deep=None, tabs=None):
    sec = ""
    if tabs:
        sec = ('<div class="hd2" data-cmp>' + "".join(f'<span class="tb{" on" if i == 0 else ""}">{t}</span>' for i, t in enumerate(tabs))
               + '</div>')
    return (f'<header class="hd" data-cmp>'
            f'<div class="hl" data-show="D1:a">{crumb(path, cur, deep)}</div>'
            f'<span class="sp"></span>{search_box()}'
            f'<button class="ib" aria-label="Trợ giúp">{ic("help", 20)}</button>{bell()}{account()}</header>{sec}'
            f'{palette()}{acc_menu()}{notif_panel()}')

# ---------- menu trái (theo bản sidebar đã duyệt 28/10: nhóm chữ hoa, mục chọn nền xám, thẻ phạm vi ở chân) ----------
MENU = [(None, [("grid", "Tổng quan", "")]),
        ("Vận tải", [("route", "Lệnh vận tải", "12"), ("truck", "Bảng điều phối", ""), ("map", "Theo dõi chuyến", "")]),
        ("Danh mục", [("users", "Khách hàng", ""), ("map", "Tuyến đường", "")]),
        ("Tài chính", [("wallet", "Chi phí chuyến", "")])]

def sidebar(active):
    out = ['<aside class="sb"><div class="lg"><span class="lo"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span><b>invlogis</b></div>']
    for g, items in MENU:
        if g:
            out.append(f'<div class="gh">{g}</div>')
        for icon, t, n in items:
            out.append(f'<div class="it{" on" if t == active else ""}">{ic(icon, 18)}<span>{t}</span>'
                       f'{f"<b class=c>{n}</b>" if n else ""}</div>')
    out.append(f'<div class="sc"><span class="mt">{ic("route", 16)}</span><div><b>Điều phối vận tải</b>'
               f'<span>{ic("pin", 12)} CN Hồ Chí Minh</span></div>{ic("ud", 16)}</div></aside>')
    return "".join(out)

def web(active, path, cur, body, title, deep=None, tabs=None, sub=""):
    pcrumb = f'<div class="pcb" data-show="D1:b">{crumb(path, cur, deep)}</div>'
    return (f'<div class="app">{sidebar(active)}<div class="mn">{header(path, cur, deep, tabs)}'
            f'<main class="ct">{pcrumb}<div class="ph1"><div><h1>{title}</h1>{f"<p class=sub>{sub}</p>" if sub else ""}</div></div>'
            f'{body}</main></div></div>')

# ---------- nội dung màn ----------
LVT = [("LVT-2026-0412", "Cát Lái → Sóng Thần", "51C-123.45", "Trần Văn Bình", "Đang chạy", "info"),
       ("LVT-2026-0413", "Hiệp Phước → VSIP 2", "51D-678.90", "Lê Minh Châu", "Đang chạy", "info"),
       ("LVT-2026-0414", "Cát Lái → Long Hậu", "51C-246.80", "Phạm Quốc Huy", "Chờ nhận", "warn"),
       ("LVT-2026-0415", "ICD Tân Cảng Long Bình → KCN Mỹ Phước 3", "50H-112.23", "Ngô Thanh Tâm", "Chờ duyệt", "warn"),
       ("LVT-2026-0416", "Cát Lái → Tân Vạn", "51C-135.79", "Trần Văn Bình", "Hoàn thành", "ok")]

def chip(t, tone):
    return f'<span class="chip {tone}">{t}</span>'

B_LIST = ('<table class="tbl"><tr><th>Mã lệnh</th><th>Tuyến</th><th>Xe</th><th>Lái xe</th><th>Trạng thái</th></tr>'
          + "".join(f'<tr><td class="mono b">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{chip(e, f)}</td></tr>' for a, b, c, d, e, f in LVT)
          + '</table>')

def fld(l, v, ph=False):
    return f'<label class="fl"><span>{l}</span><div class="fi{" ph" if ph else ""}">{v}</div></label>'

B_DETAIL = ('<div class="cards"><div class="card"><h3>Thông tin chuyến</h3>'
            + fld("Khách hàng", "Công ty TNHH Delta Logistics") + fld("Tuyến", "Cát Lái → Sóng Thần")
            + fld("Xe · mooc", "51C-123.45 · 51R-045.67") + fld("Lái xe", "Trần Văn Bình") + '</div>'
            '<div class="card"><h3>Chi phí chuyến</h3>'
            + fld("Cước", "6.450.000 ₫") + fld("Phí cầu đường", "320.000 ₫") + fld("Nhiên liệu tạm ứng", "1.800.000 ₫") + '</div></div>')

B_FORM = ('<div class="form">' + fld("Khách hàng", "Chọn khách hàng", True) + fld("Tuyến", "Chọn tuyến", True)
          + fld("Ngày đóng hàng", "28/10/2026") + fld("Loại container", "40' HC")
          + '<div class="fa"><span class="btn">Huỷ</span><span class="btn pri">Lưu nháp</span></div></div>')

B_DASH = ('<div class="kpis">' + "".join(f'<div class="kpi"><span>{a}</span><b>{b}</b></div>' for a, b in
          [("Chuyến đang chạy", "12"), ("Chờ nhận", "4"), ("Chờ duyệt", "3"), ("Trễ hẹn", "1")]) + '</div>' + B_LIST)

# ---------- mobile web 393 ----------
def m_header(title="LVT-2026-0412", parent="Lệnh vận tải", bell_html=None):
    return (f'<header class="mhd" data-cmp>'
            f'<button class="ib" aria-label="Mở menu">{ic("menu", 22)}</button>'
            f'<div class="mt1" data-show="D8:a"><b>{title}</b></div>'
            f'<div class="mt1" data-show="D8:b"><span class="mut">…</span><span class="sep">{ic("cr", 12)}</span><b>LVT-2026-0412</b></div>'
            f'<span class="sp"></span><button class="ib" aria-label="Tìm tính năng">{ic("search", 20)}</button>{bell_html or bell()}'
            f'<button class="acc m" aria-label="Tài khoản"><span class="av sm">{INIT}</span></button></header>'
            + (f'<div class="mback" data-show="D8:a">{ic("left", 16)} {parent}</div>' if parent else ""))

def m_list():
    rows = "".join(f'<div class="mr"><b class="mono">{a}</b>{chip(e, f)}<div class="mut">{b} · {c}</div></div>' for a, b, c, d, e, f in LVT[:4])
    return (f'<div class="mweb">{m_header()}<div class="mbody">'
            f'<p class="sub" style="margin:0 0 4px">Cát Lái → Sóng Thần · Đang chạy</p>{rows}</div>'
            f'<div class="mpal"{A("state:search", "state:noresult")}>{palette_inner_mobile()}</div>'
            f'<div data-show="state:account">{m_sheet()}</div><div data-show="state:notif">{m_notif()}</div></div>')

def m_sheet(n=None, r=None, i=None):
    def it(icon, t, extra="", cls=""):
        return f'<div class="msi {cls}">{ic(icon, 20)}<span>{t}</span>{extra}</div>'
    return (f'<div class="mscr"></div><div class="msh" role="dialog" aria-label="Tài khoản"><i class="grab"></i>'
            f'<div class="mh"><span class="av lg">{i or INIT}</span><div><b>{n or NAME_FULL}</b><span>{r or ROLE}</span></div></div>'
            + it("user", "Thông tin cá nhân") + it("key", "Đổi mật khẩu")
            + it("globe", "Ngôn ngữ", '<span class="mv" style="display:inline-flex;align-items:center;gap:var(--space-xs)"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" style="flex:none"><circle cx="12" cy="12" r="12" fill="#DA251D"/><path d="M12 5.2l1.6 4.9h5.1l-4.1 3 1.6 4.9-4.2-3-4.2 3 1.6-4.9-4.1-3h5.1z" fill="#FFCD00"/></svg>Tiếng Việt</span>') + '<div class="msep"></div>'
            + it("out", "Đăng xuất", cls="dng") + '</div>')

def m_notif():
    def n(t, code, meta, unread=True):
        return (f'<div class="nr{" un" if unread else ""}"><i class="ud"></i><div><div>{t}</div><b class="mono">{code}</b>'
                f'<span class="ps">{meta}</span></div></div>')
    return (f'<div class="mnp"><div class="mhd"><button class="ib" aria-label="Quay lại">{ic("left", 22)}</button><b style="font-size:15px">Thông báo</b>'
            f'<span class="sp"></span><span class="lk">Đánh dấu là đã đọc</span></div>'
            f'<div class="ntab"><span class="on">Cần xử lý <b>3</b></span><span>Tất cả</span></div>'
            + n("Chờ bạn duyệt lệnh vận tải", "LVT-2026-0418", "Trần Văn Bình · 5 phút")
            + n("Chờ bạn duyệt đề nghị tạm ứng", "TU-2026-0211", "Lê Minh Châu · 1 giờ")
            + n("Lệnh vận tải vừa bị từ chối", "LVT-2026-0402", "Phạm Quốc Huy · hôm qua", False) + '</div>')

def palette_inner_mobile():
    return (f'<div class="pin">{ic("left", 18)}<span>lệnh</span></div>'
            f'<div data-show="state:search"><div class="pg">Tính năng</div><div class="pr on"><span class="pi">{ic("route", 16)}</span>'
            f'<span class="pt"><span class="pt1"><mark>Lệnh</mark> vận tải</span><span class="ps">Điều phối vận tải</span></span></div>'
            f'<div class="pr"><span class="pi">{ic("file", 16)}</span><span class="pt"><span class="pt1"><mark>Lệnh</mark> sửa chữa</span><span class="ps">Bảo dưỡng sửa chữa</span></span></div></div>'
            f'<div class="pe" data-show="state:noresult"><b>Không có tính năng “bảo hiểm”</b><span>Thử từ khác.</span></div>')

# ---------- CSS ----------
CSS = r"""
.pv{
 
 
 font:14px/20px Inter,system-ui,sans-serif;color:var(--color-text-primary);background:var(--color-bg-primary)}
.pv[data-theme=dark]{
 
 }
.i{flex:none;display:block}
.mono{font-family:"JetBrains Mono",ui-monospace,Menlo,monospace;font-size:.92em}
.b{font-weight:600}.mut{color:var(--color-text-tertiary)}
kbd{font:500 11px/16px Inter;color:var(--color-text-tertiary);border:1px solid var(--color-border-primary);border-radius:4px;padding:0 4px;background:var(--color-bg-primary)}
mark{background:var(--color-utility-yellow-100);color:inherit;border-radius:2px;padding:0 1px}
/* khung */
.app{display:flex;min-height:720px;background:var(--color-bg-primary);position:relative}
.sb{width:240px;flex:none;border-right:1px solid var(--color-border-secondary);padding:12px;display:flex;flex-direction:column;gap:2px;background:var(--color-bg-primary)}
.sb .lg{display:flex;align-items:center;gap:8px;padding:4px 6px 14px;font:400 18px "Cal Sans",Inter}
.sb .lo{width:28px;height:28px;border-radius:8px;background:none;color:var(--color-text-white);display:grid;place-items:center;font:600 12px Inter}
.sb .gh{font:600 11px/16px Inter;letter-spacing:.05em;text-transform:uppercase;color:var(--color-text-tertiary);padding:14px 8px 4px}
.sb .it{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:8px;color:var(--color-text-secondary);font-weight:500}
.sb .it.on{background:var(--color-bg-selected);color:var(--color-text-primary);font-weight:600}
.sb .it .c{margin-left:auto;font:600 11px/18px Inter;color:var(--color-text-info-primary);background:var(--color-utility-blue-50);border-radius:999px;padding:0 7px}
.sb .sc{margin-top:auto;border:1px solid var(--color-border-secondary);border-radius:12px;padding:8px;display:flex;gap:8px;align-items:center;font-size:13px}
.sb .sc .mt{width:32px;height:32px;border-radius:8px;background:var(--color-utility-blue-50);color:var(--color-text-info-primary);display:grid;place-items:center;flex:none}
.sb .sc b{display:block;font-weight:600}.sb .sc span{display:flex;gap:4px;align-items:center;color:var(--color-text-tertiary);font-size:12px}
.sb .sc>svg:last-child{margin-left:auto;color:var(--color-text-tertiary)}
.mn{flex:1;min-width:0;display:flex;flex-direction:column;position:relative}
/* D2 b: bảng tìm là hộp thoại của cả màn — neo theo .app để lớp phủ che cả menu trái, bảng nằm giữa màn */
.pv[data-D2=b] .app>.mn{position:static}
/* thanh trên */
.hd{height:56px;display:flex;align-items:center;gap:8px;padding:0 24px;border-bottom:1px solid var(--color-border-secondary);background:var(--color-bg-primary)}
.hd2{height:44px;display:flex;align-items:flex-end;gap:20px;padding:0 24px;border-bottom:1px solid var(--color-border-secondary);background:var(--color-bg-primary)}
.hd2 .tb{padding-bottom:10px;font-weight:600;color:var(--color-text-tertiary)}.hd2 .tb.on{color:var(--color-text-primary);box-shadow:inset 0 -2px 0 var(--color-accent-solid)}
.hl{min-width:0;flex:0 1 auto;overflow:hidden}
.sp{flex:1}
.ib{width:36px;height:36px;border-radius:8px;border:0;background:transparent;color:var(--color-fg-tertiary);display:grid;place-items:center;position:relative;cursor:pointer;flex:none}
.ib:hover{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}
.bell .nd{position:absolute;top:8px;right:9px;width:8px;height:8px;border-radius:50%;background:var(--color-bg-error-solid);box-shadow:0 0 0 2px var(--color-bg-primary)}
.bell .nc{position:absolute;top:-1px;right:-3px;min-width:18px;height:18px;padding:0 5px;border-radius:999px;font:600 11px/18px Inter;
 background:var(--color-bg-info-solid);color:var(--color-text-inverse);box-shadow:0 0 0 2px var(--color-bg-primary)}
.pv[data-theme=dark] .bell .nc{color:var(--color-text-inverse)}
.pv[data-D5=c] .bell .nc,.pv[data-theme=dark] .pv[data-D5=c] .bell .nc{background:var(--color-bg-error-solid);color:var(--color-text-white)}
.pv[data-state=zero] .bell .nd,.pv[data-state=zero] .bell .nc{display:none}
.pv[data-state=notif] .bell,.pv[data-state=account] .acc{background:var(--color-bg-selected);color:var(--color-text-primary)}
.sbx{width:280px;height:36px;border:1px solid var(--color-border-input);border-radius:8px;display:flex;align-items:center;gap:8px;padding:0 8px 0 10px;color:var(--color-text-tertiary);background:var(--color-bg-primary);flex:none;margin-right:4px}
.sbx .ph{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sbx .q{display:none;flex:1;color:var(--color-text-primary)}
.pv[data-state=search] .sbx .ph,.pv[data-state=noresult] .sbx .ph{display:none}
.pv[data-state=search] .sbx .q1,.pv[data-state=noresult] .sbx .q2{display:block}
.pv[data-state=search] .sbx,.pv[data-state=noresult] .sbx{border-color:var(--color-focus-ring);box-shadow:0 0 0 1px var(--color-focus-ring)}
.pv[data-D2=c] .sbx{position:absolute;left:50%;transform:translateX(-50%);width:420px;top:10px}
.acc{display:flex;align-items:center;gap:8px;height:40px;padding:0 6px 0 4px;border:0;border-radius:10px;background:transparent;color:var(--color-text-primary);cursor:pointer;margin-left:4px;max-width:260px;font:inherit}
.acc:hover{background:var(--color-bg-primary_hover)}
.av{width:32px;height:32px;border-radius:50%;background:var(--color-accent-bg);border:1px solid var(--color-border-secondary);display:grid;place-items:center;font:600 12px Inter;color:var(--color-text-secondary);flex:none}
.av.lg{width:40px;height:40px;font-size:14px}.av.sm{width:30px;height:30px;font-size:11px}
.acc .nm{display:flex;flex-direction:column;min-width:0;text-align:left}
.acc .n1{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:160px}
.acc .n2{font-size:12px;line-height:16px;color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:180px}
.acc .cv{color:var(--color-text-tertiary)}
/* breadcrumb */
.bc{display:flex;align-items:center;gap:2px;min-width:0;font:500 14px/20px Inter;color:var(--color-text-tertiary);white-space:nowrap}
.bc .cw{display:contents}
.bc .sep{color:var(--color-fg-quaternary);display:grid;place-items:center;width:16px;flex:none}
.bc .ci{color:var(--color-text-tertiary);text-decoration:none;display:inline-flex;align-items:center;gap:2px;border:0;background:none;font:inherit;padding:0;cursor:pointer;min-width:0}
.bc .ci:hover{color:var(--color-text-primary)}
.bc .cur{color:var(--color-text-primary);font-weight:600;cursor:default}
.bc .hm{color:var(--color-text-tertiary)}
.bc .el{width:24px;justify-content:center}
.bc .sib{color:var(--color-text-tertiary);margin-left:1px}
.pv[data-D6=b] .bc .ci{height:28px;padding:0 8px;border-radius:6px}
.pv[data-D6=b] .bc .ci:hover{background:var(--color-bg-primary_hover)}
.pv[data-D6=b] .bc .cur{background:var(--color-bg-selected)}
.pv[data-D6=b] .bc .sep{width:12px}
.pv[data-D6=c] .bc .ci{height:36px;box-shadow:inset 0 -2px 0 transparent}
.pv[data-D6=c] .bc .cur{box-shadow:inset 0 -2px 0 var(--color-accent-solid)}
.pv[data-D6=c] .hd .bc{align-self:stretch}
.pv[data-D7=b] .bc .ci:not(.hm){max-width:150px}
.pv[data-D7=b] .bc .ci>span:first-child{overflow:hidden;text-overflow:ellipsis}
.pv[data-D7=b][data-state=long] .bc .ci:not(.hm):not(.cur){display:inline-block;overflow:hidden;text-overflow:ellipsis;max-width:120px}
.pcb{margin-bottom:6px}
/* nội dung */
.ct{padding:24px;background:var(--color-bg-primary);flex:1}
.ph1{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:16px}
.ph1 h1{font:400 24px/32px "Cal Sans",Inter;margin:0}
.sub{margin:2px 0 0;color:var(--color-text-tertiary)}
.tbl{width:100%;border-collapse:collapse;font-size:13px}
.tbl th{text-align:left;font-weight:500;color:var(--color-text-tertiary);background:var(--color-bg-secondary);height:40px;padding:0 12px;border-bottom:1px solid var(--color-border-secondary)}
.tbl td{height:52px;padding:0 12px;border-bottom:1px solid var(--color-border-secondary);white-space:nowrap}
.chip{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 8px;border-radius:999px;font:500 12px/18px Inter}
.chip:before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.chip.info{color:var(--color-utility-blue-700);background:var(--color-utility-blue-50)}.chip.ok{color:var(--color-utility-green-700);background:var(--color-utility-green-50)}.chip.warn{color:var(--color-utility-yellow-700);background:var(--color-utility-yellow-50)}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{border:1px solid var(--color-border-secondary);border-radius:12px;padding:16px;display:grid;gap:10px}
.card h3{margin:0;font:600 16px/24px Inter}
.fl{display:grid;gap:4px;font-size:13px}.fl>span{color:var(--color-text-secondary);font-weight:500}
.fi{height:36px;border:1px solid var(--color-border-primary);border-radius:8px;padding:0 10px;display:flex;align-items:center}
.fi.ph{color:var(--color-text-tertiary)}
.form{max-width:560px;display:grid;gap:14px}
.fa{display:flex;gap:8px;justify-content:flex-end}
.btn{height:36px;padding:0 14px;border-radius:8px;background:var(--color-action-secondary);font-weight:600;display:inline-flex;align-items:center}
.btn.pri{background:var(--color-action-primary);color:var(--color-text-inverse)}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:16px}
.kpi{border:1px solid var(--color-border-secondary);border-radius:12px;padding:12px 14px;display:grid}.kpi span{color:var(--color-text-tertiary);font-size:13px}.kpi b{font:600 24px/32px Inter}
/* bảng tìm tính năng */
.pal{position:absolute;top:52px;right:196px;width:440px;background:var(--color-bg-primary_alt);border:1px solid var(--color-border-secondary);border-radius:var(--radius-overlay);box-shadow:var(--shadow-xl);z-index:20;overflow:hidden}
.pv[data-D2=c] .pal{right:auto;left:50%;transform:translateX(-50%);width:480px}
.pv[data-D2=b] .pal{top:96px;left:50%;right:auto;transform:translateX(-50%);width:600px;z-index:31}
.scr{position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));z-index:30}
.pin{display:flex;align-items:center;gap:10px;height:52px;padding:0 16px;border-bottom:1px solid var(--color-border-secondary);font-size:16px}
.pin span{flex:1}
.pg{font:600 11px/16px Inter;letter-spacing:.05em;text-transform:uppercase;color:var(--color-text-tertiary);padding:12px 16px 4px}
.pr{display:flex;align-items:center;gap:10px;min-height:44px;padding:4px 16px;cursor:pointer}
.pr.on{background:var(--color-bg-selected)}
.pr .pi{width:28px;height:28px;border-radius:8px;border:1px solid var(--color-border-secondary);display:grid;place-items:center;color:var(--color-text-secondary);flex:none}
.pr .pt{flex:1;display:flex;flex-direction:column;min-width:0;font-weight:500}.pt1{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ps{font-size:12px;line-height:16px;color:var(--color-text-tertiary);font-weight:400}
.pr>svg{color:var(--color-text-tertiary)}
.pe{padding:28px 16px;display:grid;gap:4px;text-align:center}.pe span{color:var(--color-text-tertiary);font-size:13px}
.pf{display:flex;gap:14px;padding:8px 16px;border-top:1px solid var(--color-border-secondary);font-size:12px;color:var(--color-text-tertiary);background:var(--color-bg-secondary)}
.pf span:last-child{margin-left:auto}
/* menu tài khoản */
.am{position:absolute;top:52px;right:24px;width:280px;background:var(--color-bg-primary_alt);border:1px solid var(--color-border-secondary);border-radius:var(--radius-menu);box-shadow:var(--shadow-lg);z-index:20;padding:var(--space-xs)}
.am .mh{display:flex;gap:10px;align-items:center;padding:8px 10px 12px;border-bottom:1px solid var(--color-border-secondary);margin-bottom:6px}
.am .mh b{display:block;font-weight:600}.am .mh>div>span{display:block;font-size:12px;line-height:16px;color:var(--color-text-tertiary)}
.mi{display:flex;align-items:center;gap:10px;height:36px;padding:0 10px;border-radius:8px;color:var(--color-text-secondary);font-weight:500}
.mi span{flex:1;color:var(--color-text-primary)}.mi:hover{background:var(--color-bg-primary_hover)}
.mi .mv{flex:none;color:var(--color-text-tertiary);font-weight:400}
.mi.dng,.mi.dng span{color:var(--color-text-error-primary)}
.msep{height:1px;background:var(--color-border-secondary);margin:6px 0}
/* panel thông báo (Notification Center, chỉ minh hoạ vị trí neo) */
.np{position:absolute;top:52px;right:72px;width:380px;background:var(--color-bg-primary_alt);border:1px solid var(--color-border-secondary);border-radius:12px;box-shadow:var(--shadow-lg);z-index:20;overflow:hidden}
.np .nh{display:flex;justify-content:space-between;align-items:center;padding:12px 16px}.np .lk{font-size:13px;color:var(--color-text-secondary);font-weight:600}
.ntab{display:flex;gap:16px;padding:0 16px;border-bottom:1px solid var(--color-border-secondary);font-weight:600;color:var(--color-text-tertiary)}
.ntab span{padding-bottom:8px}.ntab .on{color:var(--color-text-primary);box-shadow:inset 0 -2px 0 var(--color-accent-solid)}
.ntab b{font:600 11px/16px Inter;background:var(--color-utility-neutral-100);border-radius:999px;padding:0 6px;color:var(--color-text-secondary)}
.nr{display:flex;gap:10px;padding:12px 16px;border-bottom:1px solid var(--color-border-secondary);font-size:13px}
.nr.un{background:var(--color-bg-info-primary)}.nr .ud{width:8px;height:8px;border-radius:50%;margin-top:6px;flex:none}
.nr.un .ud{background:var(--color-bg-info-solid)}.nr b{display:block}
/* mobile web */
.mweb{background:var(--color-bg-primary);min-height:720px;position:relative}
.mhd{height:56px;display:flex;align-items:center;gap:4px;padding:0 8px 0 4px;border-bottom:1px solid var(--color-border-secondary);background:var(--color-bg-primary)}
.mhd .mt1{display:flex;align-items:center;gap:2px;min-width:0;font-size:15px;white-space:nowrap;overflow:hidden}
.mhd .mt1 b{overflow:hidden;text-overflow:ellipsis;min-width:0}
.mhd .av{margin-left:4px}
.mhd .sep{color:var(--color-fg-quaternary)}
.mback{display:flex;align-items:center;gap:4px;height:40px;padding:0 12px;color:var(--color-text-secondary);font-weight:500;border-bottom:1px solid var(--color-border-secondary)}
.mbody{padding:16px}
.mh1{font:400 22px/28px "Cal Sans",Inter;margin:0}
.mr{display:grid;grid-template-columns:1fr auto;gap:2px 8px;padding:12px 0;border-bottom:1px solid var(--color-border-secondary);font-size:13px}
.mr .mut{grid-column:1/-1}
.mpal{position:absolute;inset:0;background:var(--color-bg-primary);z-index:30}
"""

# ---------- ô xem trước nhỏ (phương án, ý tưởng) ----------
BASE = {f"D{i}": "a" for i in range(1, 9)}

def mini(over, inner, state="default", w=None, pad=12, base=None, plat="web"):
    pick = {**(base or BASE), **over}
    a = " ".join(f'data-{k}="{v}"' for k, v in pick.items())
    st = f"padding:{pad}px;position:relative;" + (f"width:{w}px;" if w else "")
    return f'<div class="pv" {a} data-state="{state}" data-platform="{plat}" style="{st}">{resolve(inner, pick, state)}</div>'

P2 = (["Điều phối vận tải", "Lệnh vận tải"], "LVT-2026-0412")
P4 = (["Danh mục", "Khách hàng", "Delta Logistics", "Hợp đồng"], "HĐ-2026-07")

def bar(over, path=P2, state="default", extra=""):
    inner = (f'<div class="mn" style="min-height:{240 if state != "default" else 0}px">'
             f'{header(path[0], path[1])}{extra}</div>')
    return mini(over, inner, state=state, pad=0)

def bc_only(over, path=P4, state="default"):
    return mini(over, crumb(path[0], path[1]), state=state)

# ---------- ý tưởng cộng đồng ----------
ideas = [
 {"id": "I1", "source": "shadcn.io", "url": "https://www.shadcn.io/blocks/navbar-dashboard",
  "title": "Navbar dashboard: nút thu menu · đường dẫn · tìm · chuông chấm đỏ · avatar",
  "why": "Đúng bộ phần user đã tick, xếp một hàng: đường dẫn bên trái, mọi icon dồn phải. Gần Astryx Thanh trên nhất.",
  "preview": bar({"D1": "a", "D5": "a", "D4": "b"})},
 {"id": "I2", "source": "Tailgrids", "url": "https://tailgrids.com/blocks/horizontal-navbar",
  "title": "Ô tìm lệnh toàn cục có gợi ý phím tắt ⌘K",
  "why": "Ô tìm luôn hiện kèm ⌘K: người mới thấy ngay chỗ tìm, người quen dùng phím tắt. Hợp yêu cầu tìm tính năng.",
  "preview": bar({"D2": "a", "D1": "b"})},
 {"id": "I3", "source": "Novu", "url": "https://novu.co/changelog/commandk-palette",
  "title": "Bảng lệnh ⌘K: trang + hành động, lọc theo quyền",
  "why": "Kết quả gồm cả màn và hành động (tạo mới…), và chỉ hiện việc người dùng có quyền — khớp phân quyền theo role của mình.",
  "preview": bar({"D2": "b", "D3": "b"}, state="search")},
 {"id": "I4", "source": "ServiceNow Horizon", "url": "https://horizon.servicenow.com/workspace/app-shells/breadcrumb-app-shell",
  "title": "App shell có breadcrumb, ô tìm bung ra khi bấm",
  "why": "Ô tìm rộng ở giữa, bấm vào bung popover gợi ý gần đây. Mẫu ERP doanh nghiệp, nhiều module như mình.",
  "preview": bar({"D2": "c", "D3": "a"}, state="search")},
 {"id": "I5", "source": "21st.dev · Wensity", "url": "https://21st.dev/@wensity/components/breadcrumb",
  "title": "Breadcrumb gom tầng giữa thành “…”, bấm ra menu",
  "why": "Đường dẫn sâu (khách → hợp đồng → lệnh) không đẩy ô tìm ra khỏi thanh; giữ tầng đầu và tầng cuối.",
  "preview": bc_only({"D7": "a"})},
 {"id": "I6", "source": "21st.dev · Watermelon UI", "url": "https://21st.dev/@quantvansh/components/watermelon-compact-workspace-breadcrumb",
  "title": "Breadcrumb dạng nút, mục hiện tại có nền",
  "why": "Mỗi mục là nút cao 28 có nền khi rê: vùng bấm rõ trong thanh dày. Ứng với Type=Button của Untitled.",
  "preview": bc_only({"D6": "b"})},
 {"id": "I7", "source": "21st.dev · Oliver", "url": "https://21st.dev/@olewandowski1/components/page-header-2",
  "title": "Đường dẫn nằm trên tiêu đề trang (page header)",
  "why": "Thanh trên chỉ giữ tìm + icon; đường dẫn đi cùng tiêu đề và badge trạng thái. Untitled làm vậy.",
  "preview": mini({"D1": "b"}, f'<div class="pcb">{crumb(*P2)}</div><div class="ph1" style="margin:0"><h1>LVT-2026-0412</h1></div>')},
 {"id": "I8", "source": "saasui.design", "url": "https://www.saasui.design/blog/saas-breadcrumb-navigation-ux-patterns",
  "title": "Mỗi tầng có mũi tên mở danh sách cùng cấp",
  "why": "Nhảy ngang sang lệnh / khách khác mà không lùi lại. Có ích ở màn chi tiết, nhưng nặng tay khi dựng.",
  "preview": bc_only({"D7": "c"})},
 {"id": "I9", "source": "21st.dev · Cnippet", "url": "https://21st.dev/@cnippet.dev/components/v-breadcrumb-6",
  "title": "Nút tài khoản có tên + vai trò 2 dòng",
  "why": "Người dùng nhiều vai trò, nhiều chi nhánh thấy ngay đang đăng nhập với vai trò nào.",
  "preview": bar({"D4": "c"})},
 {"id": "I10", "source": "Zoho Desk · TMS", "url": "https://desk.zoho.com/portal/mitrefinch/en/kb/articles/general-navigation",
  "title": "Thanh trên TMS: menu tính năng mở từ header, tách khỏi thao tác của màn",
  "why": "Tách rõ việc toàn cục (tìm, thông báo, tài khoản) ở header với việc của màn ở page header. Gợi ý bảng tìm có nhóm theo module.",
  "preview": bar({"D2": "a", "D3": "a"}, state="search")},
]

# ---------- điểm cần quyết ----------
UNT = "Theo Untitled"
AST = "Astryx hiện tại"

decisions = [
 {"id": "D1", "title": "Đường dẫn (breadcrumb) nằm ở đâu",
  "why": "Bạn tick Breadcrumbs ở cả Header nav và Page header. Chỉ nên có một chỗ, nếu không màn có hai đường dẫn.",
  "source": "Trang Application: headernav (Phần kèm: Breadcrumbs) + pageheader (Phần kèm: Breadcrumbs) · Astryx Khung trang / Thanh trên 5596:129536",
  "options": [
   {"label": "Trong thanh trên, bên trái", "desc": "Như Astryx Thanh trên. Đầu trang chỉ còn tiêu đề, tiết kiệm một hàng.",
    "rec": True, "ideas": ["I1"], "preview": bar({"D1": "a"})},
   {"label": "Trên tiêu đề trang", "desc": "Như Untitled. Thanh trên chỉ có tìm + icon; đường dẫn đi với tiêu đề.",
    "ideas": ["I7", "I2"], "preview": mini({"D1": "b"}, f'<div class="pcb">{crumb(*P2)}</div><div class="ph1" style="margin:0"><h1>LVT-2026-0412</h1></div>')}],
  "untitled": mini({"D1": "b"}, f'<div class="pcb">{crumb(*P2)}</div>'), "untitledNote": "page header có breadcrumb, header không có",
  "astryx": bar({"D1": "a", "D5": "a"}), "astryxNote": "Thanh trên 44: đường dẫn trái"},
 {"id": "D2", "title": "Ô tìm tính năng trông thế nào",
  "why": "Bạn cần tìm tính năng (màn, chức năng), không phải tìm bản ghi trong một bảng. Cần chỗ tìm thấy được ngay, có phím tắt.",
  "source": "Yêu cầu lần gọi 28/10 · Untitled header-navigation.tsx (Input shortcut, max-w-70 = 280)",
  "options": [
   {"label": "Ô tìm 280 + ⌘K, kết quả rơi xuống dưới", "desc": "Luôn thấy ô tìm. Kết quả trong popover ngay dưới ô.",
    "rec": True, "ideas": ["I2", "I10"], "preview": bar({"D2": "a"}, state="search")},
   {"label": "Nút kính lúp + hộp thoại ⌘K giữa màn", "desc": "Thanh gọn nhất; bấm hoặc ⌘K mở hộp tìm lớn có nền mờ.",
    "ideas": ["I3"], "preview": bar({"D2": "b"}, state="search")},
   {"label": "Ô tìm rộng 420 giữa thanh", "desc": "Tìm là việc chính của thanh. Chiếm chỗ của đường dẫn.",
    "ideas": ["I4"], "preview": bar({"D2": "c"}, state="search")}],
  "untitled": bar({"D2": "a", "D1": "b"}), "untitledNote": "Input sm có shortcut, max 280",
  "astryx": bar({"D2": "a", "D5": "a"}), "astryxNote": "Thanh trên có ô tìm, chưa có bảng kết quả"},
 {"id": "D3", "title": "Ô tìm trả về những gì",
  "why": "Tìm tính năng thì kết quả là màn theo quyền. Thêm hành động hoặc bản ghi thì tiện hơn nhưng cần backend tìm toàn cục.",
  "source": "system-overview: menu theo phân quyền role · Novu ⌘K",
  "options": [
   {"label": "Chỉ tính năng (màn)", "desc": "Màn có quyền, nhóm theo module. Đọc từ cây menu, không cần API tìm.",
    "ideas": ["I10", "I4"], "preview": bar({"D3": "a"}, state="search")},
   {"label": "Tính năng + hành động tạo nhanh", "desc": "Thêm “Tạo lệnh vận tải”… mở thẳng form. Vẫn đọc từ cây menu + quyền tạo.",
    "rec": True, "ideas": ["I3"], "preview": bar({"D3": "b"}, state="search")},
   {"label": "Tính năng + hành động + bản ghi", "desc": "Gõ mã lệnh, biển số ra bản ghi. Cần API tìm toàn cục (chưa có trong SRS).",
    "preview": bar({"D3": "c"}, state="search")}],
  "untitled": bar({"D3": "a"}, state="search"), "untitledNote": "không có bảng kết quả, chỉ ô nhập",
  "astryx": bar({"D3": "a"}, state="search"), "astryxNote": "chưa có"},
 {"id": "D4", "title": "Nút tài khoản",
  "why": "Mở menu Thông tin cá nhân · Đổi mật khẩu · Ngôn ngữ · Đăng xuất (UC01.01–01.06, đổi ngôn ngữ ở system-overview).",
  "source": "docs/_shared/system-overview.md dòng 40, 54 · Astryx Thanh trên (avatar 36 + họ tên ≤ 160)",
  "options": [
   {"label": "Avatar + họ tên + mũi tên", "desc": "Như Astryx. Biết ngay đang đăng nhập tài khoản nào.", "rec": True,
    "preview": bar({"D4": "a"}, state="account")},
   {"label": "Chỉ avatar", "desc": "Như Untitled. Gọn, tên hiện trong menu.", "ideas": ["I1"],
    "preview": bar({"D4": "b"}, state="account")},
   {"label": "Avatar + tên + vai trò 2 dòng", "desc": "Thấy vai trò, chi nhánh. Thanh dày chữ hơn.", "ideas": ["I9"],
    "preview": bar({"D4": "c"})}],
  "untitled": bar({"D4": "b"}), "untitledNote": "DropdownAccountButton: avatar",
  "astryx": bar({"D4": "a", "D5": "a"}), "astryxNote": "avatar 36 + họ tên + chevron"},
 {"id": "D5", "title": "Chuông báo có việc",
  "why": "Chuông mở Notification Center đã duyệt. Chỉ đếm việc cần xử lý, tối đa 9+. Ở sidebar bạn ghi “số đếm màu xanh dương”.",
  "source": "design.md › Notification Center (Bell: Count 0/3/9+, Badge Info) · ghi chú duyệt sidebar 28/10",
  "options": [
   {"label": "Chấm đỏ", "desc": "Như Astryx Thanh trên. Không biết bao nhiêu việc.", "ideas": ["I1"],
    "preview": bar({"D5": "a"})},
   {"label": "Số đếm xanh dương", "desc": "Như Bell của Notification Center (Info, đạt AA). Khớp số đếm menu trái.", "rec": True,
    "preview": bar({"D5": "b"})},
   {"label": "Số đếm đỏ", "desc": "Như Untitled. Gắt, đỏ trắng 10px khó đạt AA.",
    "preview": bar({"D5": "c"})}],
  "untitled": bar({"D5": "c"}), "untitledNote": "bubble đỏ 14px chữ 10",
  "astryx": bar({"D5": "a"}), "astryxNote": "chấm đỏ"},
 {"id": "D6", "title": "Kiểu breadcrumb dùng trong sản phẩm",
  "why": "Bạn tick đủ 3 Type (Text, Text Line, Button) để dựng. Cần chọn một kiểu mặc định cho thanh trên để mọi màn giống nhau.",
  "source": "Trang Application: breadcrumb Type · Untitled: Text 20 / Text with line 36 / Button 28",
  "options": [
   {"label": "Text", "desc": "Chữ xám, mục hiện tại đậm. Nhẹ nhất.", "rec": True, "preview": bc_only({"D6": "a"})},
   {"label": "Button", "desc": "Mỗi mục là nút cao 28, có nền khi rê; mục hiện tại có nền.", "ideas": ["I6"],
    "preview": bc_only({"D6": "b"})},
   {"label": "Text Line", "desc": "Mục hiện tại gạch chân, cao 36. Dễ lẫn với tab.", "preview": bc_only({"D6": "c"})}],
  "untitled": bc_only({"D6": "a"}), "untitledNote": "Text là mặc định",
  "astryx": bc_only({"D6": "a"}), "astryxNote": "Breadcrumbs Chevron"},
 {"id": "D7", "title": "Đường dẫn dài xử lý thế nào",
  "why": "Màn chi tiết lồng sâu (Danh mục › Khách hàng › Delta Logistics › Hợp đồng › HĐ-2026-07) đẩy ô tìm ra ngoài thanh.",
  "source": "Trang Application: breadcrumb Phần kèm Ellipsis · Astryx: tên cắt “…” sau 240",
  "options": [
   {"label": "Gom tầng giữa thành “…”", "desc": "Giữ tầng đầu + tầng cuối + trang hiện tại; bấm “…” ra menu.", "rec": True,
    "ideas": ["I5"], "preview": bc_only({"D7": "a"})},
   {"label": "Hiện đủ, cắt chữ từng mục", "desc": "Như Astryx. Mỗi mục tối đa 150, cắt “…”.", "preview": bc_only({"D7": "b"}, state="long")},
   {"label": "Hiện đủ, mỗi mục mở danh sách cùng cấp", "desc": "Nhảy ngang sang hợp đồng / khách khác.", "ideas": ["I8"],
    "preview": bc_only({"D7": "c"})}],
  "untitled": bc_only({"D7": "a"}), "untitledNote": "mobile gom “…”",
  "astryx": bc_only({"D7": "b"}, state="long"), "astryxNote": "cắt “…”"},
 {"id": "D8", "title": "Mobile web (< 768)",
  "why": "Bạn chọn bản mobile “same”. Thanh 393 không đủ chỗ cho đường dẫn + ô tìm, phải đổi cấu tạo. App Delta Super App dùng Mobile header riêng, không dùng thanh này.",
  "source": "Trang Application: headernav mobile=same · Untitled MobileNavigationHeader · design.md: < 768 dùng MobileNav",
  "options": [
   {"label": "Menu + tiêu đề + icon; hàng ← cấp trên", "desc": "Đường dẫn thay bằng một nút ← về tầng trên.", "rec": True,
    "preview": mini({"D8": "a"}, m_header(), w=393, pad=0)},
   {"label": "Menu + đường dẫn rút gọn “… › trang”", "desc": "Giữ breadcrumb, chỉ hiện trang hiện tại.",
    "preview": mini({"D8": "b"}, m_header(), w=393, pad=0)}],
  "untitled": mini({"D8": "a"}, m_header(), w=393, pad=0), "untitledNote": "logo + hamburger 56",
  "astryx": mini({"D8": "a"}, m_header(), w=393, pad=0), "astryxNote": "MobileNav + MobileNavToggle"},
]

presets = [
 {"id": "rec", "label": "Đề xuất", "pick": {"D1": "a", "D2": "a", "D3": "b", "D4": "a", "D5": "b", "D6": "a", "D7": "a", "D8": "a"}},
 {"id": "untitled", "label": UNT, "pick": {"D1": "b", "D2": "a", "D3": "a", "D4": "b", "D5": "c", "D6": "a", "D7": "a", "D8": "a"}},
 {"id": "astryx", "label": AST, "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "b", "D8": "a"}},
]
for i in ideas:
    pick = dict(presets[0]["pick"])
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pick[d["id"]] = chr(97 + k)
    presets.append({"id": i["id"], "label": f'Ý tưởng {i["id"]} · {i["source"]}', "pick": pick})

DEEP = (["Danh mục", "Khách hàng", "Công ty TNHH Delta Logistics Việt Nam", "Hợp đồng vận chuyển"], "HĐ-2026-07-DLV-0012")

screens = [
 {"id": "list-web", "name": "Danh sách lệnh vận tải", "device": "web", "width": 1280, "shell": "none",
  "note": "Đường dẫn 2 tầng. Thử trạng thái Đang tìm, Mở thông báo, Mở menu tài khoản trong Bảng chọn › Hiển thị.",
  "html": web("Lệnh vận tải", ["Điều phối vận tải"], "Lệnh vận tải", B_LIST, "Lệnh vận tải", sub="12 lệnh đang chạy · CN Hồ Chí Minh",
              deep=DEEP)},
 {"id": "detail-web", "name": "Chi tiết lệnh · có hàng phụ (tab)", "device": "web", "width": 1280, "shell": "none",
  "note": "Layout Secondary Nav: hàng tab 44 dưới thanh trên. Đường dẫn 3 tầng.",
  "html": web("Lệnh vận tải", ["Điều phối vận tải", "Lệnh vận tải"], "LVT-2026-0412", B_DETAIL, "LVT-2026-0412",
              deep=DEEP, tabs=["Chi tiết", "Chi phí", "Chứng từ", "Lịch sử"], sub="Cát Lái → Sóng Thần · Đang chạy")},
 {"id": "form-web", "name": "Tạo lệnh vận tải (form)", "device": "web", "width": 1280, "shell": "none",
  "note": "Đường dẫn 4 tầng: thử D7 (gom “…” / cắt chữ / danh sách cùng cấp).",
  "html": web("Lệnh vận tải", ["Điều phối vận tải", "Lệnh vận tải", "Nháp"], "Tạo lệnh mới", B_FORM, "Tạo lệnh vận tải", deep=DEEP)},
 {"id": "dash-web", "name": "Tổng quan điều phối", "device": "web", "width": 1280, "shell": "none",
  "note": "Màn gốc của module: đường dẫn chỉ 1 tầng.",
  "html": web("Tổng quan", [], "Tổng quan", B_DASH, "Tổng quan", sub="Hôm nay 28/10/2026")},
 {"id": "detail-mweb", "name": "Chi tiết lệnh · mobile web", "device": "mobile", "width": 393, "shell": "none",
  "note": "< 768: thanh 56 đổi cấu tạo (D8). Ô tìm thành icon, bấm mở màn tìm.",
  "html": m_list()},
]

refs = {
 "untitled": {"summary": "Header 64 (hàng chính) + hàng phụ 64 (nút hoặc tab gạch chân). Phải: icon Cài đặt, Chuông (bubble đỏ), "
              "nút tài khoản dạng avatar. Ô tìm <mark>Input sm có phím tắt, tối đa 280</mark>. Breadcrumb: Text 20 · Text with line 36 · "
              "Button 28 · Chevron/Slash · icon nhà · mobile gom “…”.",
              "source": "design/_ref/untitled-ui/react/components/application/app-navigation/header-navigation.tsx · "
                        "base/dropdown/dropdown-account-breadcrumb.tsx · untitledui.com/components (breadcrumbs)"},
 "astryx": {"summary": "<b>Khung trang / Thanh trên</b> cao 44: đường dẫn (mục cha xám › trang đậm) · nút chi nhánh · tìm · chuông chấm đỏ · "
            "avatar 36 + họ tên cắt sau 160 + chevron, menu Thông tin tài khoản / Đăng xuất. <code>Breadcrumbs</code> Chevron/Slash. "
            "Notification Center / Bell: Count 0/3/9+, Badge Info.",
            "source": "design/design.md › Khung trang web (CMP-11) · Notification Center · Figma 5596:129536"},
 "usage": ["Mọi màn web (CMP-11): thanh trên của Khung trang — vd transport-dispatch, service-delivery, fund-payments",
           "CMP-02 In-app Notification: chuông mở Notification Center",
           "UC01.01–01.06 Tài khoản cá nhân: menu tài khoản (thông tin cá nhân, đổi mật khẩu, đăng xuất), đổi ngôn ngữ",
           "Page header (thẻ pageheader) dùng Breadcrumbs nếu D1 = trên tiêu đề"],
 "platform": "Web + mobile web (< 768). Nhóm C (DEC-279): mobile web đổi cấu tạo (menu + icon, đường dẫn thành nút ←), "
             "trục Platform=Web|Mobile. App Delta Super App không dùng — dùng Mobile header (thẻ mobileheader). "
             "Breadcrumbs chỉ web (bạn chọn).",
}

page = {
 "component": "Header navigation + Breadcrumbs",
 "slug": "header-navigation",
 "title": "Header Nav Review",
 "subtitle": "Application component · thanh trên ERP web 56 (Simple + hàng phụ tab) gồm đường dẫn, tìm tính năng, chuông, trợ giúp, tài khoản. "
             "Breadcrumbs dựng cùng vì lồng trong thanh.",
 "round": "brainstorm",
 "refs": refs,
 "css": CSS + any_css(),
 "states": [{"key": k, "label": l} for k, l in STATES],
 "ideas": ideas,
 "decisions": decisions,
 "presets": presets,
 "screens": screens,
}


# ================= Vòng 2 — Preview (28/10) =================
# Tổ hợp chốt ở Brainstorm: D1 A · D2 A · D3 B · D4 B (chỉ avatar) · D5 C (số đếm đỏ) · D6 A · D7 A · D8 A
PICK = {"D1": "a", "D2": "a", "D3": "b", "D4": "b", "D5": "c", "D6": "a", "D7": "a", "D8": "a"}

# ô nhỏ lồng .pv cần biến tối khi trang bật Dark (kit chỉ đổi data-theme của .pv ngoài)
DARK = CSS.split(".pv[data-theme=dark]{", 1)[1].split("}", 1)[0]
CSS3 = ".pv[data-theme=dark] .pv{" + DARK + "}" + r"""
.bc .cur{display:inline-block;max-width:240px;overflow:hidden;text-overflow:ellipsis;vertical-align:middle}.pv[data-D6=b] .bc .cur{line-height:28px}.pv[data-D6=c] .bc .cur{line-height:36px}
.bc .ci.hv{color:var(--color-text-primary)}.bc .ci.fc,.sbx.fc,.ib.fc,.acc.fc{outline:2px solid var(--color-focus-ring);outline-offset:2px;border-radius:6px}
.pv[data-D6=b] .bc .ci.hv{background:var(--color-bg-primary_hover)}.pv[data-D6=c] .bc .ci.hv{box-shadow:inset 0 -2px 0 var(--color-border-primary)}
.sbx.hv{border-color:var(--color-border-input_hover)}.sbx .q.on{display:block}.sbx.typ{border-color:var(--color-focus-ring);box-shadow:0 0 0 1px var(--color-focus-ring)}
.ib.hv,.acc.hv{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}.ib.op,.acc.op{background:var(--color-bg-selected);color:var(--color-text-primary)}
.ib.fc,.acc.fc{border-radius:8px}
.tw{position:relative;display:inline-flex;flex-direction:column;align-items:center;gap:6px}
.tip{background:var(--color-bg-primary_solid);color:var(--color-text-inverse);font:500 12px/18px Inter;padding:4px 8px;border-radius:6px;white-space:nowrap}
.acc.only{padding:2px;height:36px;width:36px;justify-content:center;border-radius:50%;margin:0}
.pv[data-D4=b] .hd .acc{padding:2px;width:36px;height:36px;justify-content:center;border-radius:50%}
.elw{position:relative;display:inline-flex}.bc .ci.el.op{background:var(--color-bg-selected);border-radius:6px;color:var(--color-text-primary)}
.elm{position:absolute;top:28px;left:-8px;min-width:220px;background:var(--color-bg-primary_alt);border:1px solid var(--color-border-secondary);border-radius:10px;box-shadow:var(--shadow-lg);padding:4px;z-index:5}
.elm a{display:flex;align-items:center;gap:8px;height:36px;padding:0 10px;border-radius:6px;color:var(--color-text-primary);font-weight:500;white-space:nowrap}
.elm a:hover{background:var(--color-bg-primary_hover)}
.static .pal,.static .am{position:static;transform:none}
.static{position:relative}
.ex{display:flex;flex-direction:column;gap:6px;width:max-content}
.lab{font:500 11px Inter;color:var(--color-text-tertiary)}
.mhd .acc.m{padding:0;height:36px;width:36px;justify-content:center;margin:0}
.mscr{position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));z-index:30}
.msh{position:absolute;left:0;right:0;bottom:0;background:var(--color-bg-primary_alt);border-radius:var(--radius-overlay) var(--radius-overlay) 0 0;padding:8px 8px 24px;z-index:31}
.msh .grab{display:block;width:36px;height:4px;border-radius:2px;background:var(--color-bg-quaternary);margin:0 auto 8px}
.msh .mh{display:flex;gap:12px;align-items:center;padding:8px 12px 14px;border-bottom:1px solid var(--color-border-secondary);margin-bottom:6px}
.msh .mh b{display:block}.msh .mh>div>span{display:block;font-size:13px;line-height:18px;color:var(--color-text-tertiary)}
.msi{display:flex;align-items:center;gap:12px;min-height:48px;padding:0 12px;border-radius:10px;color:var(--color-text-secondary);font:500 15px/22px Inter}
.msi span{flex:1;color:var(--color-text-primary)}.msi .mv{flex:none;color:var(--color-text-tertiary);font-weight:400}.msi.dng,.msi.dng span{color:var(--color-text-error-primary)}
.mnp{position:absolute;inset:0;background:var(--color-bg-primary);z-index:30}.mnp .lk{font-size:13px;font-weight:600;color:var(--color-text-secondary);padding-right:8px}
.mweb .pal-m{position:static}
"""
page["css"] = CSS + any_css() + CSS3

W = 1040  # 1280 − menu 240
def pvc(inner, state="default", over=None, pad=0, w=None, plat="web"):
    return mini(over or {}, inner, state=state, w=w, pad=pad, base=PICK, plat=plat)

def cell(lab, inner):
    return f'<div class="ex"><span class="lab">{lab}</span>{inner}</div>'

def row(title, cells, note=""):
    return (f'<div style="font:600 13px Inter,system-ui,sans-serif;margin:24px 0 4px">{title}</div>'
            + (f'<div style="font:12px/18px Inter,system-ui,sans-serif;color:var(--color-text-tertiary);margin-bottom:8px">{note}</div>' if note else '<div style="height:4px"></div>')
            + f'<div style="display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start">{"".join(cells)}</div>')

def hbar(path, cur, state="default", tabs=None, h=None, over=None):
    inner = f'<div class="mn" style="width:{W}px;{f"min-height:{h}px" if h else ""}">{header(path, cur, tabs=tabs)}</div>'
    return pvc(inner, state, over)

ELL = f'<button class="ci el" aria-label="Hiện các tầng ẩn">{ic("dots", 16)}</button>'
def bc(path, cur, over=None, hv=False, fc=False, open_=False, state="default"):
    h = crumb(path, cur)
    if hv: h = h.replace('<a class="ci">', '<a class="ci hv">', 1)
    if fc: h = h.replace('<a class="ci">', '<a class="ci fc">', 1)
    if open_:
        h = h.replace(ELL, f'<span class="elw"><button class="ci el op" aria-expanded="true" aria-label="Hiện các tầng ẩn">{ic("dots", 16)}</button>'
                           f'<div class="elm" role="menu">' + "".join(f'<a>{t}</a>' for t in path[1:-1]) + '</div></span>')
    return pvc(h, state, over, pad=8)

def sbx(cls="", q=None):
    t = f'<span class="q on">{q}</span>' if q else '<span class="ph">Tìm tính năng, màn…</span>'
    return pvc(f'<div class="sbx {cls}" style="margin:0">{ic("search", 16)}{t}<kbd>⌘K</kbd></div>', pad=4)

def ibtn(icon, cls="", label="", tip=None, badge=None):
    b = f'<b class="nc">{badge}</b>' if badge else ""
    btn = f'<button class="ib {"bell " if icon == "bell" else ""}{cls}" aria-label="{label}">{ic(icon, 20)}{b}</button>'
    return pvc(f'<span class="tw">{btn}<span class="tip">{tip}</span></span>' if tip else btn, pad=4)

def avbtn(cls="", tip=None, init="NA"):
    btn = f'<button class="acc only {cls}" aria-label="Tài khoản: Nguyễn Văn Anh"><span class="av">{init}</span></button>'
    return pvc(f'<span class="tw">{btn}<span class="tip">{tip}</span></span>' if tip else btn, pad=4)

def pal_static(state):
    return pvc(f'<div class="static" style="width:440px">{palette()}</div>', state, pad=4)

def pal_recent():
    def r(icon, t, sub):
        return (f'<div class="pr"><span class="pi">{ic(icon, 16)}</span><span class="pt"><span class="pt1">{t}</span><span class="ps">{sub}</span></span></div>')
    return pvc('<div class="static" style="width:440px"><div class="pal" style="position:static">'
               '<div class="pg">Dùng gần đây</div>' + r("route", "Lệnh vận tải", "Điều phối vận tải › Danh sách")
               + r("truck", "Bảng điều phối", "Điều phối vận tải") + r("wallet", "Đề nghị tạm ứng", "Quỹ & thanh toán")
               + '<div class="pf"><span><kbd>↑</kbd><kbd>↓</kbd> chọn</span><span><kbd>↵</kbd> mở</span><span>Chỉ hiện tính năng bạn có quyền</span></div></div></div>', pad=4)

def pal_long():
    return pvc('<div class="static" style="width:440px"><div class="pal" style="position:static"><div class="pg">Tính năng</div>'
               f'<div class="pr on"><span class="pi">{ic("wallet", 16)}</span><span class="pt"><span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">'
               '<mark>Thanh toán</mark> mua hàng và bồi thường hàng hoá dịch vụ vận chuyển</span>'
               '<span class="ps" style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Quỹ & thanh toán › Đề nghị thanh toán › Danh sách chờ duyệt cấp chi nhánh</span></span></div>'
               '</div></div>', "search", pad=4)

LONGN, LONGR = "Nguyễn Thị Phương Thảo", "Trưởng phòng Điều phối vận tải · CN Bà Rịa – Vũng Tàu"
P1 = ([], "Tổng quan")
P3 = (["Điều phối vận tải", "Lệnh vận tải"], "LVT-2026-0412")

def grid_web():
    h = row("Thanh trên — bố cục (1040 = 1280 − menu 240)", [
        cell("Simple · màn danh sách (đường dẫn 2 tầng)", hbar(["Điều phối vận tải"], "Lệnh vận tải")),
        cell("Secondary Nav · màn chi tiết có hàng tab 44", hbar(*P3, tabs=["Chi tiết", "Chi phí", "Chứng từ", "Lịch sử"])),
        cell("Màn gốc của module (1 tầng)", hbar(*P1))],
        "Cao 56, viền dưới. Trái: đường dẫn. Phải: ô tìm 280 · Trợ giúp · Chuông · Avatar.")
    h += row("Thanh trên — trạng thái mở", [
        cell("Đang tìm (kết quả rơi dưới ô)", hbar(*P3, state="search", h=440)),
        cell("Tìm không thấy", hbar(*P3, state="noresult", h=260)),
        cell("Mở menu tài khoản", hbar(*P3, state="account", h=320)),
        cell("Mở thông báo (Notification Center — component riêng, chỉ minh hoạ chỗ neo)", hbar(*P3, state="notif", h=400)),
        cell("Không có thông báo (ẩn số đếm)", hbar(*P3, state="zero")),
        cell("Chữ dài — đường dẫn 5 tầng gom “…”, 9+", hbar(DEEP[0], DEEP[1], state="long"))])
    h += row("Breadcrumbs — độ sâu (Type Text)", [
        cell("1 tầng", bc(*P1)), cell("2 tầng", bc(["Điều phối vận tải"], "Lệnh vận tải")), cell("3 tầng", bc(*P3)),
        cell("≥ 4 tầng: gom tầng giữa", bc(*P4)), cell("Bấm “…” mở danh sách tầng ẩn", pvc(f'<div style="height:130px">{bc(*P4, open_=True)}</div>')),
        cell("Trang hiện tại dài: cắt sau 240, tooltip đủ", bc(DEEP[0], DEEP[1]))],
        "Giữ tầng đầu + tầng cuối + trang hiện tại. Nhà là icon, có nhãn đọc màn hình “Trang chủ”.")
    types = [("Text", "a"), ("Button", "b"), ("Text Line", "c")]
    for nm, k in types:
        h += row(f"Breadcrumbs — Type {nm}" + (" (mặc định trong thanh trên)" if k == "a" else " (có trong bộ, không dùng ở thanh trên)"), [
            cell("Default", bc(*P3, over={"D6": k})), cell("Hover (mục 1)", bc(*P3, over={"D6": k}, hv=True)),
            cell("Focus bàn phím", bc(*P3, over={"D6": k}, fc=True))])
    h += row("Ô tìm tính năng (280 × 36)", [
        cell("Rest", sbx()), cell("Hover", sbx("hv")), cell("Focus · chưa gõ", sbx("typ")), cell("Đang gõ", sbx("typ", "lệnh")),
        cell("Focus bàn phím (Tab)", sbx("fc"))],
        "⌘K (Ctrl K trên Windows) nhảy vào ô. Esc đóng bảng kết quả, xoá chữ.")
    h += row("Bảng kết quả (popover 440, dưới ô tìm)", [
        cell("Mới mở — dùng gần đây", pal_recent()), cell("Có kết quả: Tính năng + Hành động", pal_static("search")),
        cell("Không có kết quả", pal_static("noresult")), cell("Chữ dài — cắt 1 dòng", pal_long())],
        "Đọc từ cây menu theo quyền + quyền tạo; không gọi API tìm. Mục đầu được chọn sẵn, ↵ mở.")
    h += row("Nút icon 36 — Trợ giúp, Chuông", [
        cell("Rest", ibtn("help", label="Trợ giúp")), cell("Hover + tooltip", ibtn("help", "hv", "Trợ giúp", "Trợ giúp")),
        cell("Focus", ibtn("help", "fc", "Trợ giúp")), cell("Đang mở", ibtn("bell", "op", "Thông báo", badge="3")),
        cell("Chuông 0", ibtn("bell", label="Thông báo")), cell("Chuông 3", ibtn("bell", label="Thông báo, 3 việc cần xử lý", badge="3")),
        cell("Chuông 9+", ibtn("bell", label="Thông báo, hơn 9 việc", badge="9+")),
        cell("Hover + tooltip", ibtn("bell", "hv", "Thông báo", "Thông báo · 3 việc cần xử lý", badge="3"))],
        "Số đếm đỏ (danger-solid) chỉ đếm việc cần xử lý, tối đa 9+. Nhãn đọc màn hình kèm số.")
    h += row("Nút tài khoản (chỉ avatar 32 trong nút 36)", [
        cell("Rest", avbtn()), cell("Hover + tooltip họ tên", avbtn("hv", "Nguyễn Văn Anh")), cell("Focus", avbtn("fc")),
        cell("Đang mở", avbtn("op"))], "Họ tên + vai trò hiện ở đầu menu, không ở thanh.")
    h += row("Menu tài khoản (280)", [
        cell("Mặc định", pvc(f'<div class="static">{acc_menu(show="")}</div>', pad=4)),
        cell("Chữ dài — họ tên, vai trò xuống dòng", pvc(f'<div class="static">{acc_menu(LONGN, LONGR, "PT", show="")}</div>', pad=4))])
    return h

def phone(inner, h=720):
    return f'<div class="mweb" style="min-height:{h}px">{inner}</div>'

def grid_mob():
    hd = lambda **k: pvc(m_header(**k), plat="mobile")
    lab = lambda t: f'<div class="lab" style="padding:16px 16px 6px">{t}</div>'
    f1 = phone(lab("Màn gốc — không có hàng ←") + hd(title="Lệnh vận tải", parent=None)
               + lab("Màn con — hàng ← về cấp trên") + hd()
               + lab("Tiêu đề dài — cắt 1 dòng") + hd(title="HĐ-2026-07-DLV-0012 · Công ty TNHH Delta Logistics Việt Nam", parent="Hợp đồng vận chuyển")
               + lab("Chuông 9+ · không có thông báo") + hd(bell_html='<button class="ib bell" aria-label="Thông báo">' + ic("bell", 20) + '<b class="nc">9+</b></button>', parent=None)
               + hd(bell_html='<button class="ib bell" aria-label="Thông báo">' + ic("bell", 20) + '</button>', parent=None))
    f2 = pvc(m_list(), "search", plat="mobile")
    f3 = pvc(m_list(), "noresult", plat="mobile")
    f4 = pvc(m_list(), "account", plat="mobile")
    f5 = pvc(m_list(), "notif", plat="mobile")
    # khung điện thoại của kit 393 có lề stage 20 mỗi bên → vùng vẽ 351; ghim bề rộng để chữ dài cắt thay vì đẩy icon ra ngoài
    return [f'<div style="width:351px;overflow:hidden">{f}</div>' for f in (f1, f2, f3, f4, f5)]

page["round"] = "preview"
page["subtitle"] = ("Application component · nhóm C · vòng 2 Preview — tổ hợp đã chốt: "
                    + " · ".join(f"{k} {v.upper()}" for k, v in PICK.items()))
page["preview"] = {"version": "1", "pick": PICK,
                   "changes": "bản đầu theo lựa chọn vòng 1 (D4 chỉ avatar, D5 số đếm đỏ); mobile web: avatar mở sheet tài khoản, chuông mở màn Thông báo",
                   "blocks": [{"title": "Web", "platform": "web", "note": "Thanh 56 · hàng tab 44 · ô tìm 280 · bảng kết quả 440 · menu tài khoản 280", "html": grid_web()},
                              {"title": "Mobile web (< 768)", "platform": "mobile", "note": "Khung 393 · thanh 56 + hàng ← 40 · tìm toàn màn · tài khoản là sheet",
                               "frames": grid_mob()}]}

# Khai giá trị preview — vòng 3 đối chiếu foundation (ds-foundation-check.py)
V = []
def v(part, prop, value, **kw):
    V.append({"part": part, "prop": prop, "value": value, **kw})
W_, M_ = {"platform": "Web"}, {"platform": "Mobile"}
v("Header", "height", 56); v("Header", "padding-x", 24, **W_); v("Header", "gap", 8, **W_); v("Header", "border-width", 1)
v("Header", "background", "#FFFFFF"); v("Header", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF")
v("Secondary nav", "height", 44, **W_); v("Secondary nav", "gap", 20, **W_); v("Secondary nav", "padding-x", 24, **W_)
v("Tab", "font-size", 14); v("Tab", "line-height", 20); v("Tab", "font-weight", 600); v("Tab", "padding-bottom", 10, **W_, interactive=True, hitArea=44)
v("Tab inactive", "color", "#737373", role="text", on="#FFFFFF"); v("Tab active", "color", "#171717", role="text", on="#FFFFFF")
v("Tab indicator", "border-width", 2); v("Tab indicator", "color", "#262626", role="border", on="#FFFFFF")
v("Breadcrumb", "font-size", 14); v("Breadcrumb", "line-height", 20); v("Breadcrumb", "font-weight", 500); v("Breadcrumb", "gap", 2)
v("Breadcrumb item", "color", "#737373", role="text", on="#FFFFFF"); v("Breadcrumb item hover", "color", "#171717", role="text", on="#FFFFFF", state="hover")
v("Breadcrumb current", "color", "#171717", role="text", on="#FFFFFF"); v("Breadcrumb current", "font-weight", 600); v("Breadcrumb current", "max-width", 240)
v("Breadcrumb separator", "icon-size", 14); v("Breadcrumb separator", "width", 16); v("Breadcrumb separator", "color", "#D4D4D4", role="decorative", on="#FFFFFF")
v("Breadcrumb home", "icon-size", 16); v("Breadcrumb ellipsis", "width", 24, interactive=True, hitArea=24)
v("Breadcrumb button", "height", 28, interactive=True, hitArea=28); v("Breadcrumb button", "padding-x", 8); v("Breadcrumb button", "radius", 6)
v("Breadcrumb button hover", "background", "#F5F5F5", state="hover"); v("Breadcrumb line", "height", 36); v("Breadcrumb line", "border-width", 2)
v("Ellipsis menu", "min-width", 220); v("Ellipsis menu", "radius", 10); v("Ellipsis menu", "padding", 4); v("Ellipsis menu", "shadow", "shadow/lg")
v("Ellipsis menu item", "height", 36, interactive=True, hitArea=36); v("Ellipsis menu item", "padding-x", 10); v("Ellipsis menu item", "radius", 6)
v("Search", "width", 280, **W_); v("Search", "height", 36, **W_, control=True, interactive=True, hitArea=36); v("Search", "radius", 8)
v("Search", "padding-left", 10); v("Search", "padding-right", 8); v("Search", "gap", 8); v("Search", "icon-size", 16)
v("Search", "border-color", "#737373", role="border", on="#FFFFFF"); v("Search hover", "border-color", "#525252", role="border", on="#FFFFFF", state="hover")
v("Search focus", "border-color", "#262626", role="border", on="#FFFFFF", state="focus")
v("Search placeholder", "color", "#737373", role="text", on="#FFFFFF"); v("Search value", "color", "#171717", role="text", on="#FFFFFF")
v("Kbd", "font-size", 11); v("Kbd", "line-height", 16); v("Kbd", "padding-x", 4); v("Kbd", "radius", 4); v("Kbd", "color", "#737373", role="text", on="#FFFFFF", hint=True)
v("Palette", "width", 440, **W_); v("Palette", "radius", 12); v("Palette", "shadow", "shadow/xl"); v("Palette", "border-color", "#E5E5E5", role="decorative", on="#FFFFFF")
v("Palette group label", "font-size", 11); v("Palette group label", "line-height", 16); v("Palette group label", "font-weight", 600)
v("Palette group label", "color", "#737373", role="text", on="#FFFFFF"); v("Palette group label", "padding-x", 16); v("Palette group label", "padding-top", 12)
v("Palette row", "min-height", 44, interactive=True, hitArea=44); v("Palette row", "padding-x", 16); v("Palette row", "gap", 10)
v("Palette row selected", "background", "#F5F5F5", state="selected"); v("Palette icon box", "size", 28); v("Palette icon box", "radius", 8)
v("Palette row title", "font-size", 14); v("Palette row title", "font-weight", 500); v("Palette row sub", "font-size", 12); v("Palette row sub", "line-height", 16)
v("Palette row sub", "color", "#737373", role="text", on="#FFFFFF"); v("Palette highlight", "background", "#FFF1B8")
v("Palette footer", "padding-x", 16); v("Palette footer", "padding-y", 8); v("Palette footer", "gap", 14); v("Palette footer", "font-size", 12)
v("Palette footer", "background", "#FAFAFA"); v("Palette footer", "color", "#737373", role="text", on="#FAFAFA")
v("Palette empty", "padding-y", 28); v("Palette empty sub", "font-size", 13); v("Palette empty sub", "color", "#737373", role="text", on="#FFFFFF")
v("Icon button", "size", 36, **W_, interactive=True, hitArea=36); v("Icon button", "radius", 8); v("Icon button", "icon-size", 20)
v("Icon button", "color", "#525252", role="icon", on="#FFFFFF"); v("Icon button hover", "background", "#F5F5F5", state="hover")
v("Icon button hover", "color", "#171717", role="icon", on="#F5F5F5", state="hover")
v("Tooltip", "font-size", 12); v("Tooltip", "line-height", 18); v("Tooltip", "padding-x", 8); v("Tooltip", "padding-y", 4); v("Tooltip", "radius", 6)
v("Tooltip", "background", "#262626"); v("Tooltip", "color", "#FFFFFF", role="text", on="#262626")
v("Bell count", "min-width", 18); v("Bell count", "height", 18); v("Bell count", "padding-x", 5); v("Bell count", "radius", 9999)
v("Bell count", "font-size", 11); v("Bell count", "line-height", 18); v("Bell count", "font-weight", 600)
v("Bell count", "background", "#B42318"); v("Bell count", "color", "#FFFFFF", role="text", on="#B42318")
v("Avatar", "size", 32); v("Avatar", "radius", 9999); v("Avatar", "font-size", 12); v("Avatar", "background", "#F5F5F5")
v("Avatar", "color", "#525252", role="text", on="#F5F5F5"); v("Avatar", "border-color", "#E5E5E5", role="decorative", on="#F5F5F5")
v("Account button", "size", 36, **W_, interactive=True, hitArea=36); v("Account button", "padding", 2)
v("Account menu", "width", 280, **W_); v("Account menu", "radius", 12); v("Account menu", "padding", 6); v("Account menu", "shadow", "shadow/lg")
v("Account menu header", "gap", 10); v("Account menu header", "padding-x", 10); v("Account menu avatar", "size", 40)
v("Account menu role", "font-size", 12); v("Account menu role", "line-height", 16); v("Account menu role", "color", "#737373", role="text", on="#FFFFFF")
v("Menu item", "height", 36, **W_, interactive=True, hitArea=36); v("Menu item", "padding-x", 10); v("Menu item", "gap", 10); v("Menu item", "radius", 8)
v("Menu item", "icon-size", 16); v("Menu item icon", "color", "#525252", role="icon", on="#FFFFFF")
v("Menu item danger", "color", "#B42318", role="text", on="#FFFFFF"); v("Menu separator", "color", "#E5E5E5", role="decorative", on="#FFFFFF")
v("Focus ring", "focus-width", 2); v("Focus ring", "focus-offset", 2); v("Focus ring", "color", "#262626", role="border", on="#FFFFFF")
v("Mobile header", "height", 56, **M_); v("Mobile header", "padding-left", 4, **M_); v("Mobile header", "padding-right", 8, **M_); v("Mobile header", "gap", 4, **M_)
v("Mobile title", "font-size", 15, **M_); v("Mobile title", "font-weight", 600, **M_)
v("Mobile icon button", "size", 36, **M_, interactive=True, hitArea=44); v("Mobile menu icon", "icon-size", 22, **M_)
v("Mobile back row", "height", 40, **M_, interactive=True, hitArea=40); v("Mobile back row", "padding-x", 12, **M_); v("Mobile back row", "gap", 4, **M_)
v("Mobile back row", "color", "#525252", role="text", on="#FFFFFF")
v("Mobile avatar", "size", 30, **M_)
v("Mobile search screen input", "height", 52, **M_); v("Mobile search screen input", "font-size", 16, **M_)
v("Account sheet", "radius", 16, **M_); v("Account sheet", "padding-bottom", 24, **M_); v("Sheet grabber", "width", 36, **M_); v("Sheet grabber", "height", 4, **M_)
v("Sheet item", "min-height", 48, **M_, interactive=True, hitArea=48); v("Sheet item", "padding-x", 12, **M_); v("Sheet item", "gap", 12, **M_)
v("Sheet item", "radius", 10, **M_); v("Sheet item", "font-size", 15, **M_); v("Sheet item", "line-height", 22, **M_); v("Sheet item", "icon-size", 20, **M_)
v("Scrim", "background", "color/bg/overlay")
page["values"] = V


# Preview bản 1 duyệt 28/10 (trong chat) → vòng 3 đối chiếu foundation
page["round"] = "foundation"

# ================= Vòng 3 — quyết định đối chiếu foundation (28/10) =================
# ⛔ ô tìm 36 → 32 (luật cao control DEC-173) · ⛔ hàng ← mobile 40: ngoại lệ cho component này
# ＋ nền chữ khớp → color/bg/warning/secondary · ＋ lề khung không kết quả → 24
# ↔ 16 dòng không chọn = kéo về token đề xuất
page["css"] += r"""
.pv{}
.hd2{height:40px}.elm{min-width:240px}
.sbx{width:300px;height:32px}kbd{font-size:12px}
.pal{width:400px;right:64px}.pg{font-size:12px}.pr{min-height:40px}.pf{gap:12px}
.pe{padding:24px 16px}.pe span{font-size:12px}
.bell .nc{min-width:20px;height:20px;padding:0 4px;font:600 12px/20px Inter}
.am{width:300px}.mhd .av.sm{width:28px;height:28px}.mpal .pin{font-size:17px}
"""
NEW = {("Search", "height"): 32, ("Palette highlight", "background"): "#FEE4B6", ("Palette empty", "padding-y"): 24,
       ("Secondary nav", "height"): 40, ("Ellipsis menu", "min-width"): 240, ("Search", "width"): 300, ("Kbd", "font-size"): 12,
       ("Palette", "width"): 400, ("Palette group label", "font-size"): 12, ("Palette row", "min-height"): 40,
       ("Palette footer", "gap"): 12, ("Palette empty sub", "font-size"): 12, ("Bell count", "min-width"): 20,
       ("Bell count", "height"): 20, ("Bell count", "padding-x"): 4, ("Bell count", "font-size"): 12, ("Bell count", "line-height"): 20,
       ("Account menu", "width"): 300, ("Mobile avatar", "size"): 28, ("Mobile search screen input", "font-size"): 17}
for x in page["values"]:
    k = (x["part"], x["prop"])
    if k in NEW:
        x["value"] = NEW[k]
        if x.get("hitArea") and isinstance(NEW[k], int) and x["prop"] in ("height", "min-height"): x["hitArea"] = NEW[k]
for x in page["values"]:
    if x["part"] == "Mobile back row" and x["prop"] == "height": x["hitArea"] = 44  # vòng 4: user đổi ý, thêm vùng bấm vô hình 44 thay ngoại lệ
page["preview"]["changes"] += "; vòng 3: ô tìm 300 × 32, bảng kết quả 400 (dòng 40), hàng tab 40, số đếm 20, menu tài khoản 300, chữ phụ 12, nền chữ khớp warning-bg-strong; hàng ← mobile hình 40, vùng bấm vô hình 44"

# ================= Vòng 5 — review Figma (28/10): 3 agent, 26 điểm gộp còn 19 =================
page["round"] = "review"
page["figma"] = {"url": "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/?node-id=6768-190542",
                 "label": "Master Header navigation (Breadcrumbs 6901:20705 · _Header search panel 6904:20446 · khung Tài liệu 6768:198301)"}
def rv(i, agent, sev, node, text, fix, look=False):
    return {"id": i, "agent": agent, "severity": sev, "node": node, "text": text, "fix": fix, "changesLook": look}
page["reviews"] = [
 rv("R1", "accessibility", "Cao", "6900:216882", "<b>2.1.4 — phím tắt một chữ “N”</b> ở dòng “Tạo lệnh vận tải”. Phím một chữ không bổ trợ trượt mức A (nhập giọng nói gõ nhầm), và đụng chữ “n” khi đang gõ trong ô tìm. Spec chưa chốt phím này (UX/UI cũng nêu).",
    "A (đề xuất): bỏ phím tắt khỏi bản mẫu (tắt <code>Has Shortcut</code>), chưa có tính năng phím tắt tạo nhanh. B: đổi thành tổ hợp <code>Alt N</code>, chỉ chạy khi focus không ở ô nhập."),
 rv("R2", "uxui-reviewer", "Cao", "6904:20446", "<b>Bảng tìm thiếu trạng thái</b>: chỉ có Results / Recent / Empty. Cây menu theo quyền tải sau đăng nhập — chưa xong hoặc lỗi thì bảng hiện “Không có tính năng…” sai, đẩy người dùng sang hướng “chưa cấp quyền”. Thiếu cả Recent rỗng (người dùng mới).",
    "Thêm <code>Content = Loading</code> (3 dòng khung chờ, giữ chân bảng), <code>Error</code> (“Chưa tải được danh sách tính năng” + nút Tải lại), <code>Recent rỗng</code> (“Gõ tên màn để tìm”). Spec ghi: cây menu chưa sẵn sàng → Loading, không Empty."),
 rv("R3", "uxui-reviewer", "Cao", "6768:198301", "<b>Chưa vẽ các lớp mở ra</b>: Mobile — màn tìm toàn trang, sheet tài khoản; Web — menu tài khoản 300, menu “…” của đường dẫn. Hiện chỉ có chữ trong spec, dev không có hình để dựng. Mobile cũng mất lối vào <b>Trợ giúp</b> (web có nút, mobile không).",
    "Vẽ thêm vào khung Tài liệu: menu tài khoản web, menu “…” mở, màn tìm mobile (chưa gõ + Empty), sheet tài khoản mobile có mục <b>Trợ giúp</b> (trước Đăng xuất). Notification Center chỉ ghi chú trỏ sang component riêng."),
 rv("R4", "visual-reviewer", "Trung", "6768:201351", "<b>Thứ tự co khi thiếu chỗ</b> (màn 1280, 1024): trang hiện tại bị cắt trước (“Danh…”), trong khi ô tìm giữ 300 và tầng cha vẫn dài. Trang hiện tại là thứ cần đọc nhất (UX/UI cũng nêu).",
    "Ghi thứ tự vào spec và dựng lại: (1) ô tìm co 300 → 240 dưới 1280, (2) gom tầng giữa thành “…” khi không đủ chỗ (không chỉ theo số tầng), (3) trang hiện tại giữ tối thiểu 120 rồi mới cắt.", True),
 rv("R5", "accessibility", "Trung", "6900:216892", "<b>1.4.3 — chữ phím tắt trên dòng đang chọn 4,35:1</b>: <code>text/tertiary</code> 12 trên <code>bg/selected</code>. Path đã đổi sang <code>secondary-strong</code>, Shortcut thì chưa.",
    "Lớp Shortcut ở <code>_Search result</code> State=Selected dùng <code>color/text/tertiary_strong</code> (~7:1). Không đổi look đáng kể."),
 rv("R6", "accessibility", "Trung", "6900:216885", "<b>2.4.7 / 1.4.11 — dòng đang chọn chỉ khác nền 1,09:1</b> (#F5F5F5 so với trắng) + icon ↵. Spec tự mâu thuẫn: ghi “vòng focus trên dòng kết quả” nhưng lại dùng mẫu combobox (focus ở ô nhập, dòng chọn qua <code>aria-activedescendant</code>).",
    "Thêm vạch trái 2px <code>color/focus/ring</code> cho dòng Selected (≥ 3:1). Spec: focus ở ô, mỗi dòng <code>role=\"option\"</code> + <code>aria-selected</code>, bỏ câu “vòng focus trên dòng”.", True),
 rv("R7", "uxui-reviewer", "Trung", "6901:20705", "<b>Collapsed chưa giữ tầng đầu</b>: biến thể Collapsed mặc định là “Nhà › … › Mục cha › Trang hiện tại” vì <code>Has Root</code> mặc định tắt — lệch D7 A (giữ tầng đầu + tầng cuối + trang hiện tại).",
    "Ở 3 biến thể Collapsed=True cho tầng đầu luôn hiện (không phụ thuộc <code>Has Root</code>)."),
 rv("R8", "accessibility", "Trung", "6901:20705", "<b>Thiếu hình trạng thái</b> Hover / Focus / Đang mở của mục đường dẫn, nút “…”, avatar, nút Trợ giúp ở khung Trạng thái (ô tìm, chuông, tab thì có). Phụ: ở chuông State=Focus, viền trắng của số đếm đè lên góc vòng focus.",
    "Thêm hàng minh hoạ Hover/Focus/Open cho đường dẫn, “…”, avatar, Trợ giúp vào khung Trạng thái. Số đếm nằm trên vòng focus mà không cắt vòng."),
 rv("R9", "accessibility", "Trung", "6900:216808", "<b>Avatar mobile vùng chạm 32</b> (luật dự án DEC-138: mobile ≥ 44; WCAG 2.5.8 vẫn đạt). Menu / Tìm / Chuông là nút 42, avatar chỉ là khung 32.",
    "Bọc avatar trong nút 42 như các nút khác (avatar vẫn 32)."),
 rv("R10", "accessibility", "Trung", "6900:216829", "<b>Hàng ← chưa có vùng bấm 44</b> như DEC-290 ghi — chỉ có chữ trong spec; lề trái 12 lệch lề 16 của thanh (thị giác cũng nêu: nhãn nhỏ, nhạt, dễ bỏ qua).",
    "A (đề xuất): tăng hàng lên 44, lề trái 16, cả hàng là liên kết “Quay lại {cấp trên}” — hết chồng lấn. B: giữ 40 + lớp Hit area 44 trong suốt.", True),
 rv("R11", "accessibility", "Trung", "", "<b>Spec trợ năng thiếu</b>: tên đọc nút mobile (Mở menu + <code>aria-expanded</code>, Tìm tính năng, hàng ←); màn tìm và sheet tài khoản là <code>dialog</code> có nhãn, giữ focus, Esc trả focus; chuông <code>aria-expanded</code> + <code>aria-controls</code>; hàng tab đổi màn nên là <code>nav</code> + liên kết <code>aria-current</code> (không dùng tablist); 2.4.11 thanh dính đầu che focus; 1.4.10 ngưỡng 768 theo bề rộng CSS (zoom 400% tự sang Mobile).",
    "Bổ sung các dòng trên vào mục Trợ năng / Kích thước của spec và mô tả component; ghi <code>scroll-padding-top</code> = cao thanh (56, 96 khi có hàng tab). Không đổi hình."),
 rv("R12", "uxui-reviewer", "Thấp", "6768:191286", "<b>API thiếu thuộc tính hay đổi</b>: số đếm chuông, chữ gợi ý ô tìm, chữ tắt avatar phải vào instance lồng; <code>Has Menu</code>, <code>Has Back</code>, <code>Back label</code> hiện cả ở Web dù chỉ Mobile dùng.",
    "Expose instance lồng (chuông, ô tìm, avatar) ra panel; mô tả thuộc tính ghi “chỉ Mobile”."),
 rv("R13", "uxui-reviewer", "Thấp", "6900:217377", "<b>Chữ trạng thái rỗng</b> nối hai ý bằng “hoặc”, không nói làm gì tiếp: “Thử từ khác, hoặc tính năng chưa được cấp quyền cho tài khoản này.”",
    "Đổi: “Thử từ khác. Nếu vẫn không thấy, tài khoản của bạn có thể chưa được cấp quyền — hỏi quản trị viên.”"),
 rv("R14", "uxui-reviewer", "Thấp", "6904:20446", "<b>Chữ khớp không tô trong bản mẫu</b> Figma, trong khi spec ghi tô nền <code>warning-bg-strong</code>.",
    "Mô phỏng trong bản mẫu Results: khung nền <code>bg/warning/secondary</code> sau chữ “Lệnh” (chỉ minh hoạ, code tô thật).", True),
 rv("R15", "uxui-reviewer", "Thấp", "6768:198301", "<b>Khung Tài liệu còn nhãn cũ</b> “_Header breadcrumb · Has Root tắt / bật” ở mục Cấu tạo.",
    "Đổi nhãn sang <code>Breadcrumbs</code>; mô tả component rút về “dùng khi nào”, số đo để spec."),
 rv("R16", "accessibility", "Thấp", "6900:216610", "<b>Breadcrumbs</b>: chevron phân cách chưa ghi <code>aria-hidden</code>; Type Text Line vạch dưới trang hiện tại trùng màu/độ dày vòng focus và vạch tab chọn — dễ nhầm “đang chọn” với “đang focus”.",
    "Spec ghi aria-hidden cho dấu phân cách; vạch Current của Text Line đổi sang <code>color/text/primary</code> 2px, focus luôn là vòng quanh mục.", True),
 rv("R17", "visual-reviewer", "Thấp", "6768:190944", "<b>Hai điểm nhấn tranh nhau</b> ở Secondary Nav: trang hiện tại (đậm) hàng 1 và tab chọn (đậm + vạch) hàng 2.",
    "Giữ nguyên (vạch dưới đã đủ tách tab với đường dẫn); hoặc tab chọn nét 500 thay 600.", True),
 rv("R18", "visual-reviewer", "Thấp", "6768:190822", "<b>Số đếm “9+”</b> rộng hơn, gần chạm avatar bên cạnh (khoảng 8).",
    "Kiểm khe giữa số “9+” và avatar; dưới 4 thì tăng khoảng Actions → Account lên 12."),
 rv("R19", "visual-reviewer", "Thấp", "6768:201351", "<b>Tầng cha bị cắt giữa từ</b> (“Quản lý vận tải đa phư…”).",
    "Giữ (ngưỡng 160 + tooltip đủ chữ); Figma không cắt theo từ được."),
]

# page.json đã được sửa thẳng sau build (tách css/cssScreen, khai sel 253 dòng, proto, ghim R-n) — chạy lại build sẽ xoá hết
import sys
if OUT.exists() and "proto" in json.loads(OUT.read_text()) and "--force" not in sys.argv:
    sys.exit("page.json đã có chỉnh sửa sau build (proto, cssScreen, sel). Sửa thẳng page.json; ghi đè thì thêm --force.")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import tok_css_nested  # noqa: E402
page["css"] = tok_css_nested() + page["css"]
from icon_dec329 import apply as _dec329  # noqa
_dec329(page)  # DEC-329: cỡ, nét, màu icon
OUT.write_text(json.dumps(page, ensure_ascii=False, indent=1))
print("ok", OUT, len(ideas), "ý tưởng", len(decisions), "điểm", len(screens), "màn")
