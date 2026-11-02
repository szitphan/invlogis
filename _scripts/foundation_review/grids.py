#!/usr/bin/env python3
"""SPEC trang review Foundations · Lưới, độ rộng, breakpoint. Dựng: python3 _scripts/foundation_review/build.py grids"""
import json
import re

import kit

TJ = json.loads((kit.ROOT / "design-system/tokens.json").read_text())
GRID = TJ["grid"]
BP = TJ["breakpoints"]
G_WEB = GRID["web"]["gutter"]      # 32
G_TAB = GRID["tablet"]["gutter"]   # 24
G_APP = GRID["mobile"]["gutter"]   # 16
M_WEB = 32                         # layout/screen-inset Web = space/32
MENU, MENU_S = 240, 64             # design-system/components/application/sidebar-navigation.md
V_GUT, V_TAB, V_APP = "var(--grid-gutter)", "var(--space-3xl)", "var(--space-xl)"


def num(x):
    s = f"{x:.2f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def col(w, menu, cols, gut, mar):
    return (w - menu - 2 * mar - (cols - 1) * gut) / cols


def span(c, n, gut):
    return n * c + (n - 1) * gut


def st(k):
    return {"ok": '<span class="st-ok">Giống</span>', "diff": '<span class="st-diff">Khác có lý do</span>',
            "gap": '<span class="st-gap">Mình thiếu</span>', "own": '<span class="st-own">Chỉ mình có</span>'}[k]


def fr(w, menu, cols, gut, mar, s, cap, v_gut=V_GUT, v_mar=V_GUT, kpi=None, ghost=0):
    """Khung thu nhỏ theo tỉ lệ s: menu + cột phủ. Số cột suy ra tính cùng công thức trong ref Untitled."""
    c = col(w, menu, cols, gut, mar)
    k = ""
    if kpi:
        k = (f'<div class="gr-fk" style="left:calc((var(--m) + {v_mar})*var(--s));right:calc({v_mar}*var(--s));column-gap:calc({kpi}*var(--s))">'
             "<b></b><b></b><b></b></div>")
    return (f'<figure class="gr-fig"><div class="gr-fr" style="--s:{s};--m:{menu}px;width:calc({w}px*var(--s))">'
            f'<div class="gr-fm" style="width:calc(var(--m)*var(--s))"></div>'
            f'<div class="gr-fc" style="left:calc((var(--m) + {v_mar})*var(--s));right:calc({v_mar}*var(--s));grid-template-columns:repeat({cols},minmax(0,1fr));column-gap:calc({v_gut}*var(--s))">' + "<i></i>" * cols + "</div>" + (f'<div class="gr-fm gr-gh" style="width:calc({ghost}px*var(--s))"></div>' if ghost else "") + f"{k}</div>"
            f"<figcaption>{cap}<br><span class=\"tp-num\">{cols} cột, cột {num(c)}, rãnh {gut}, lề {mar}</span></figcaption></figure>")


def row(*figs, fit=False):
    return f'<div class="gr-x"><div class="gr-row{" gr-fit" if fit else ""}">' + "".join(figs) + "</div></div>"


def pane(html_):
    return kit.panes(html_, modes=("light",))


def appf(w, inner, cap, cols_css="repeat(4,minmax(0,1fr))", gap=V_APP, n=4):
    return (f'<figure class="gr-fig"><div class="tp-f gr-app" data-platform="mobile" style="width:{w}px">'
            f'<div class="gr-ovl" style="left:var(--layout-screen-inset);right:var(--layout-screen-inset);grid-template-columns:{cols_css};column-gap:{gap}">' + "<i></i>" * n + f"</div>{inner}</div><figcaption>{cap}</figcaption></figure>")


ORDER_CARD = ('<div class="tp-card"><div class="tp-top"><span class="type-code tp-sub">LVT-2026-0412</span><span class="tp-chip tp-b">Đang chạy</span></div>'
              '<div class="type-title-3">Cát Lái → KCN Long Hậu</div><div class="type-body tp-sub">51C-482.15 · Nguyễn Văn Hoà</div></div>')
APP_BAR = '<div class="tp-appbar"><div style="flex:1;min-width:0"><div class="type-title-2">Lệnh của tôi</div></div></div>'
FIXED_FIELD = '<div class="tp-fld"><span class="type-label">Mã container</span><div class="tp-inp" style="width:var(--field-width-default)"><span class="type-body">TCLU 482915-3</span></div></div>'
FILL_FIELD = '<div class="tp-fld"><span class="type-label">Mã container</span><div class="tp-inp"><span class="type-body">TCLU 482915-3</span></div></div>'

# ───────────── màn mẫu: phủ lưới, khung đúng dự án ─────────────
_RE_F = re.compile(r'<div class="tp-f( tp-prop)? (tp-web|tp-webs|tp-webc|tp-app)" data-platform="\w+">')


def overlay_html(body):
    """Chèn lớp cột vào từng khung .tp-f, vị trí theo lề thật; web 12 hoặc 6 cột đổi theo khung chọn ở thanh trên."""
    seen = {"n": 0}

    def rep(m):
        kind = m.group(2)
        head = m.group(0)
        if kind == "tp-webs":
            seen["n"] += 1
            head = head.replace("tp-webs", "tp-webs gr-detail" if seen["n"] == 1 else "tp-webs gr-form")
        if kind == "tp-app":
            st_ = "left:var(--gr-ovm);right:var(--gr-ovm);grid-template-columns:repeat(4,minmax(0,1fr));column-gap:var(--gr-ovg)"
            n = 4
        else:
            left = "calc(var(--gr-menu) + var(--gr-ovm))" if kind == "tp-web" else "var(--gr-ovm)"
            st_ = f"left:{left};right:var(--gr-ovm);grid-template-columns:repeat(var(--gr-cols),minmax(0,1fr));column-gap:var(--gr-ovg)"
            n = 12
        return head + f'<div class="tp-gridov" style="{st_}">' + "<i></i>" * n + "</div>"

    body = _RE_F.sub(rep, body)
    # trang này đổi được khung ở thanh trên, nên nhãn nói theo đó
    return body.replace("(rộng 393)", "(khung chọn ở thanh trên, mặc định 393)").replace("· danh sách, có menu nổi", "· danh sách có menu, khung chọn ở thanh trên").replace("· chi tiết, biểu mẫu, hộp xác nhận", "· chi tiết 8/4, biểu mẫu, hộp xác nhận, rộng bằng vùng sau menu")


# ───────────── bảng đối chiếu ─────────────
R = lambda *c: list(c)
CMP = [
    R("Width", "<code>width-xxs</code>", "n:320", "<code>width/xs</code>", "n:320", st("diff"), "Cùng số, khác tên, lệch một bậc"),
    R("Width", "<code>width-xs</code>", "n:384", "<code>width/sm</code>", "n:400", st("diff"), "400 lấy từ slideout thật của Untitled (<code>max-w-100</code> trong <code>design/_ref/untitled-ui/react/components/application/slideout-menus/slideout-menu.tsx</code>)"),
    R("Width", "<code>width-sm</code>", "n:480", "—", "n:—", st("gap"), "Chưa component nào cần"),
    R("Width", "<code>width-md</code>", "n:560", "<code>width/md</code>", "n:560", st("ok"), "Bậc duy nhất trùng cả tên lẫn số"),
    R("Width", "<code>width-lg</code>", "n:640", "—", "n:—", st("gap"), "<code>width/lg</code> của mình lại là 720"),
    R("Width", "<code>width-xl</code>", "n:768", "—", "n:—", st("gap"), "<code>width/xl</code> của mình lại là 960"),
    R("Width", "<code>width-2xl</code>", "n:1024", "—", "n:—", st("gap"), "<code>width/2xl</code> của mình lại là 1280"),
    R("Width", "<code>width-3xl</code>", "n:1280", "<code>width/2xl</code>", "n:1280", st("diff"), "Cùng số, khác tên"),
    R("Width", "<code>width-4xl</code>", "n:1440", "—", "n:—", st("gap"), "Khung thiết bị, không phải độ rộng khối"),
    R("Width", "<code>width-5xl</code>", "n:1600", "—", "n:—", st("gap"), "Không dùng"),
    R("Width", "<code>width-6xl</code>", "n:1920", "—", "n:—", st("gap"), "Không dùng"),
    R("Width", "<code>paragraph-max-width</code>", "n:720", "<code>width/lg</code>", "n:720", st("diff"), "Cùng số, gộp vai với dialog lớn. Lớp <code>.prose</code> lại ghi 72ch"),
    R("Width", "—", "n:—", "<code>width/xl</code>", "n:960", st("own"), "Drawer rộng, hộp thoại phạm vi (<code>design-system/components/application/sidebar-navigation.md</code>)"),
    R("Container", "<code>container-padding-mobile</code>", "n:16", "<code>layout/screen-inset</code> App", "n:16", st("diff"), "Cùng số, khác tên; mình một token hai chế độ"),
    R("Container", "<code>container-padding-desktop</code>", "n:32", "<code>layout/screen-inset</code> Web", "n:32", st("diff"), "Cùng số, khác tên (DEC-259)"),
    R("Container", "<code>container-max-width-desktop</code>", "n:1280", "<code>layout/content-max-width</code> Web", "n:1280", st("diff"), "Cùng số, ghi số trần thay vì trỏ thang"),
    R("Container", "—", "n:—", "<code>layout/content-max-width</code> App", "n:393", st("own"), "Untitled không chặn rộng trên điện thoại; xem mục gr04"),
    R("Grid", "Desktop", "n:12 · 32 · 32", "Web ≥ 1024", "n:12 · 32 · 32", st("ok"), "Khung Untitled 1280 không có menu; mình tính sau menu"),
    R("Grid", "Tablet 768", "n:6 · 32 · 32", "Tablet 768–1023", "n:6 · 24 · 24", st("diff"), "DEC-257 chọn, DEC-259 mục GR2 chọn giữ; đo thấy lệch 8 với lề, xem mục gr08"),
    R("Grid", "Mobile 375", "n:4 · 16 · 16", "App 393", "n:4 · 16 · 16", st("diff"), "Cùng cột, rãnh, lề; khung 393 thay 375"),
    R("Grid", "Cột auto 12/6/5/3/2", "n:rãnh ?", "—", "n:—", st("gap"), "Ref chưa đọc rãnh, chỉ có tên"),
    R("Grid", "—", "n:—", "Chi tiết 8 + 4 cột (DEC-127)", "n:8/4", st("own"), "Mẫu màn chi tiết như Jira"),
    R("Grid", "—", "n:—", "<code>grid/columns</code>", "n:12", st("own"), "Một giá trị, đọc trên app vẫn ra 12; xem mục gr09"),
    R("Grid", "—", "n:—", "<code>grid/gutter</code>", "n:32", st("own"), "Một giá trị, đọc trên app vẫn ra 32; xem mục gr09"),
    R("Breakpoint", "<code>--breakpoint-xxs</code>", "n:320", "<code>--bp-xxs</code>", "n:320", st("ok"), "Khai trong <code>design/_ref/untitled-ui/raw/theme.css</code>"),
    R("Breakpoint", "<code>--breakpoint-xs</code>", "n:600", "<code>--bp-xs</code>", "n:600", st("ok"), "Untitled ghi “This must match the breakpoint in Sonner”: mốc của thư viện thông báo"),
    R("Breakpoint", "sm", "n:640", "<code>--bp-sm</code>", "n:640", st("ok"), "Mặc định Tailwind v4, Untitled không khai lại"),
    R("Breakpoint", "md", "n:768", "<code>--bp-md</code>", "n:768", st("ok"), "Lề đổi ở đây: <code>px-4 md:px-8</code>; mình đổi sang menu, lưới 6 cột"),
    R("Breakpoint", "lg", "n:1024", "<code>--bp-lg</code>", "n:1024", st("ok"), "Mình đổi 6 → 12 cột"),
    R("Breakpoint", "xl", "n:1280", "<code>--bp-xl</code>", "n:1280", st("ok"), "Mình mở menu 240 (DEC-039)"),
    R("Breakpoint", "2xl", "n:1536", "<code>--bp-2xl</code>", "n:1536", st("ok"), "Mặc định Tailwind v4"),
]
_c = lambda k: sum(1 for r in CMP if st(k) == r[5])
N_OK, N_DIFF, N_GAP, N_OWN = _c("ok"), _c("diff"), _c("gap"), _c("own")
N_U = N_OK + N_DIFF + N_GAP

# ───────────── số cột theo khung ─────────────
_rows = []
for w, menu, cols, g, m, lab in [(1440, MENU, 12, G_WEB, M_WEB, "Web, menu mở"), (1280, MENU, 12, G_WEB, M_WEB, "Web chuẩn, menu mở"), (1024, MENU_S, 12, G_WEB, M_WEB, "Web, menu thu gọn"),
                                 (768, MENU_S, 6, G_TAB, G_TAB, "Tablet theo <code>design-system/foundations/grids.md</code>"), (768, MENU_S, 6, G_WEB, M_WEB, "Tablet nếu chọn 32 như Untitled"),
                                 (393, 0, 4, G_APP, G_APP, "App, khung chuẩn"), (375, 0, 4, G_APP, G_APP, "App, máy thử, khung Untitled"), (320, 0, 4, G_APP, G_APP, "App, máy thử nhỏ nhất")]:
    c = col(w, menu, cols, g, m)
    sp = f"{num(span(c, 8, g))} + {num(span(c, 4, g))}" if cols == 12 else "—"
    _rows.append(R(lab, f"n:{w}", f"n:{menu or '—'}", f"n:{w - menu}", f"n:{cols}", f"n:{g}", f"n:{m}", f"n:{num(c)}", f"n:{sp}"))
COLS_TBL = kit.rows(["Khung", "Rộng", "Menu", "Vùng nội dung", "Cột", "Rãnh", "Lề", "Rộng cột", "Chi tiết 8 + 4"], _rows)

_c1040 = {g: col(1040, 0, 12, g, M_WEB) for g in (32, 24, 16)}
FRAMES_TBL = kit.rows(["Nơi ghi", "Web", "App", "Ghi chú"], [
    R("Màn mẫu của kit (<code>_scripts/foundation_review/kit.py</code>)", "1280, menu 240; chi tiết, biểu mẫu 680", "393", "Khung và menu 240 đã đúng (DEC-039). Trang này đặt vùng sau menu 1040 và thêm nút chọn khung ở thanh trên"),
    R("Ref Untitled (<code>design/_ref/untitled-ui/04-spacing-radius-grid.md</code>)", "1280, trong MacBook 1440", "375", "Khung lưới không có menu trái"),
    R("<code>design-system/foundations/grids.md</code>", "Không nêu khung vẽ", "393", "Chỉ ghi “App (khung 393)”, <mark>web chưa có khung chuẩn</mark>"),
    R("<code>design-system/components/application/header-navigation.md</code>", "1280", "—", "“1280 − menu 240 = 1040 ở màn chuẩn”"),
    R("<code>design/design.md</code> (bản cũ)", "1920, 1440", "393", "Bảng mốc 12/10, trước DS v2. Đổi từ 375 sang 393 ngày 06/10/2026"),
    R("<code>field/width-default</code>, <code>progress/width-default</code> App", "320", "361", "361 = 393 − 2 × 16, viết cứng theo khung 393"),
    R("<code>--bp-xxs</code>", "—", "320", "Mốc có trong token. Ba component đã kiểm chữ dài ở 320 (<code>design-system/components/application/vehicle-card.md</code>, <code>design-system/components/application/vehicle-option-card.md</code>, <code>design-system/components/application/combo-text.md</code>), foundations chưa ghi thành luật"),
])

REF_GAP = kit.rows(["Phần của Untitled", "Tình trạng trong ref", "Ảnh hưởng tới trang này"], [
    R("Rãnh của lưới cột auto 12/6/5/3/2", "<code>design/_ref/untitled-ui/README.md</code> ghi “giá trị rãnh chưa đọc”", "Mục gr07 không có số Untitled để so rãnh trong khối"),
    R("Lưới dạng token", "<code>tokens.untitled.json</code> không có mục grid nào; ba khung đọc bằng mắt từ thước đỏ Figma, cột “suy ra” là số tính tay", "Rộng cột Untitled 72 · 90,7 · 73,75 là số tính, không phải số đọc"),
    R("Bảng breakpoint đủ", "Repo chỉ khai 320 và 600; 5 mốc còn lại ref ghi “default Tailwind v4”. Figma không có collection breakpoint", "Không có nguồn nói mốc nào Untitled dùng để thiết kế"),
    R("Bề rộng hộp thoại", "<code>modal.tsx</code> để <code>w-full</code>, nơi dùng tự đặt; ref không có ví dụ màn. Chỉ slideout có số 400", "Vai dialog 400 · 560 · 720 của mình không có số Untitled để so"),
    R("Mẫu màn, luật khi đổi khung", "<code>react/</code> chỉ có component, không có trang; ref không nói menu, cột thay đổi ở mốc nào", "Luật menu 64, 240 và 6, 12 cột là của mình (DEC-039, DEC-257)"),
    R("Tên layout guide style Figma", "Chưa đọc tên, chỉ đọc số", "Mục gr09 chưa biết nên đặt tên style lưới giống họ thế nào"),
])

PROPOSAL = kit.rows(["Nhóm", "Bây giờ", "Sau khi chọn theo khuyến nghị"], [
    R("Độ rộng", "<code>width/xs 320 · sm 400 · md 560 · lg 720 · xl 960 · 2xl 1280</code>", "<code>width/xxs</code> 320, <code>width/md</code> 560, <code>width/3xl</code> 1280 đúng Untitled; <code>width/overlay-sm</code> 400, <code>width/overlay-lg</code> 960 tên riêng; <code>width/paragraph-max</code> trỏ 560. Không thêm bậc; 480, 256, 600 ở token Component"),
    R("Container", "<code>layout/screen-inset</code>, <code>layout/content-max-width</code> (1280 · 393)", "<code>container/padding</code> 32 · 16, <code>container/max-width</code> trỏ <code>width/3xl</code>, tính cả lề, app không chặn"),
    R("Lưới web", "12 cột, rãnh 32, lề 32, không nói tính từ đâu", "Giữ số (DEC-259), <mark>tính trong vùng sau menu</mark>, khối cấp màn canh đúng cột"),
    R("Lưới tablet", "6 cột, rãnh 24, lề 24, không có biến nào ra 24", "6 cột, rãnh 32, lề 32 như Untitled và như web"),
    R("Token lưới", "<code>--grid-columns</code> 12, <code>--grid-gutter</code> 32 cho mọi nền tảng", "<code>grid/columns</code> 12 · 4, <code>grid/gutter</code> trỏ <code>space/4xl</code> · <code>space/xl</code>"),
    R("Khung", "Web chưa nêu, app 393", "Vẽ web 1280, menu 240, thử thêm 1024. Vẽ app 393, thử thêm 320"),
    R("App co giãn", "Ô nhập, thanh tiến độ rộng cứng 361", "App trải theo màn, 361 chỉ là kết quả trên khung 393"),
    R("Breakpoint", "7 mốc, không nói mốc nào quan trọng", "Giữ 7 mốc cho code, khai <mark>3 mốc thiết kế</mark> 768 · 1024 · 1280"),
])


DECIDED = kit.rows(["Quyết định", "Nội dung còn hiệu lực"], [
    R("DEC-259 mục GR1", "Web 12 cột, rãnh 32, lề 32; rộng tối đa 1280 cho màn chi tiết, form, màn bảng trải hết. Rãnh, lề web cũ 24 của DEC-136 đã thay bằng dòng này"),
    R("DEC-259 mục GR3", "App 4 cột, rãnh 16, lề 16, thay đường canh K1–K4 (các đường căn mép cũ của app, đo từ mép màn)"),
    R("DEC-259 mục GR5, DEC-038", "Breakpoint theo mốc có sẵn 640 · 768 · 1024 · 1280 · 1536, thêm 320 và 600"),
    R("DEC-039", "Từ 768 tới 1279 menu thu 64, bấm thì bung 240 đè lên nội dung; từ 1280 menu 240"),
    R("DEC-127", "Màn chi tiết web chia 8 cột nội dung + 4 cột thông tin"),
    R("DEC-257 mục P3", "Tablet 6 cột. Phần rãnh 24 xem gr08"),
    R("DEC-314", "Token theo vai trỏ vào thang, không ghi số trần"),
    R("DEC-320, DEC-322", "Tên theo Untitled, số giữ của mình khi có lý do, không thêm token không ai dùng"),
])

# ───────────── xem thử từng mục ─────────────
def bars(rows_, scale=".45"):
    out = []
    for lab, expr, cls in rows_:
        out.append(f'<div class="gr-bar"><span class="gr-bl">{lab}</span><div class="gr-bb {cls}" style="width:calc({expr}*{scale})"></div></div>')
    return "".join(out)


PV_NAMES = pane('<div class="gr-2"><div><div class="type-label">Bây giờ, đọc từ biến thật</div>' + bars([
    ("<code>width/xs</code>", "var(--width-xs)", ""), ("<code>width/sm</code>", "var(--width-sm)", ""), ("<code>width/md</code>", "var(--width-md)", ""),
    ("<code>width/lg</code>", "var(--width-lg)", ""), ("<code>width/xl</code>", "var(--width-xl)", ""), ("<code>width/2xl</code>", "var(--width-2xl)", "")], ".3")
    + '</div><div><div class="type-label">Cùng tên ở Untitled, số khác</div>' + bars([
        ("<code>width-xs</code>", "384px", "u"), ("<code>width-sm</code>", "480px", "u"), ("<code>width-md</code>", "560px", "u"),
        ("<code>width-lg</code>", "640px", "u"), ("<code>width-xl</code>", "768px", "u"), ("<code>width-2xl</code>", "1024px", "u")], ".3") + "</div></div>")

PV_MISSING = pane(bars([
    ("320", "var(--width-xs)", ""), ("400", "var(--width-sm)", ""), ("480 · thêm", "480px", "u"), ("560", "var(--width-md)", ""), ("640 · thêm", "640px", "u"),
    ("720", "var(--width-lg)", ""), ("768", "768px", "u"), ("960", "var(--width-xl)", ""), ("1024", "1024px", "u"), ("1280", "var(--width-2xl)", ""), ("1440", "1440px", "u"), ("1600", "1600px", "u"), ("1920", "1920px", "u")], ".42")
    + '<p class="small muted" style="margin:8px 0">Xanh đậm: mình có. Nhạt, viền đứt: chỉ Untitled có. Dưới đây: ba token Component treo.</p>' + bars([
        ("<code>header-nav/account-menu-width</code>", "var(--header-nav-account-menu-width)", ""), ("<code>vehicle/q-lg-w</code>", "var(--vehicle-q-lg-w)", ""), ("<code>command-search/width</code>", "var(--command-search-width)", "")], ".42"))

_PARA = "Tài xế nhận container tại cổng B của cảng Cát Lái, kiểm tra niêm phong và số seal trước khi rời cảng, chụp ảnh tình trạng vỏ, rồi báo về điều vận nếu số seal khác lệnh. Khi tới KCN Long Hậu, tài xế chờ thủ kho xác nhận, nhập số km thực tế và gửi biên bản giao nhận ngay trên ứng dụng để kế toán chốt cước trong ngày."
PV_PARA = pane("".join(
    f'<div class="gr-pb"><div class="type-label">{lab} <span class="gr-lc tp-num"></span></div><p class="type-body gr-para" style="max-width:{w}">{_PARA}</p></div>'
    for lab, w in [("<code>width/lg</code> 720, luật đang ghi ·", "var(--width-lg)"), ("<code>.prose</code> 72ch, lớp đang chạy ·", "72ch"), ("<code>width/md</code> 560 ·", "var(--width-md)")]))


def _inset(m, p):
    return ('<div class="gr-ins" style="padding:0 var(--layout-screen-inset)"><div class="gr-insc"></div></div>'
            '<p class="small" style="margin:6px 0 0"><code>layout/screen-inset</code> đọc được: <b class="tp-num" data-read="--layout-screen-inset"></b> · '
            '<code>layout/content-max-width</code>: <b class="tp-num" data-read="--layout-content-max-width"></b></p>')


PV_CONT = kit.panes(_inset, modes=("light",), platforms=("web", "mobile"))

PV_MOBMAX = pane(row(
    appf(430, f'<div style="max-width:var(--layout-content-max-width);margin:0 auto;box-shadow:0 0 0 1px var(--color-border-secondary)">{APP_BAR}<div class="tp-pad">{ORDER_CARD}</div></div>', "430, đang chặn 393: thừa hai dải trống"),
    appf(430, f'{APP_BAR}<div class="tp-pad">{ORDER_CARD}</div>', "430, không chặn: trải đủ màn"),
))

_inc = col(1600, MENU, 12, G_WEB, M_WEB)
PV_MAX = pane(row(
    '<figure class="gr-fig"><div class="gr-fr" style="--s:.3;--m:240px;width:calc(1600px*var(--s))"><div class="gr-fm" style="width:calc(var(--m)*var(--s))"></div>'
    '<div class="gr-cb" style="left:calc((var(--m) + (1360px - var(--width-2xl))/2)*var(--s));width:calc(var(--width-2xl)*var(--s));padding:0 calc(var(--grid-gutter)*var(--s))"><div class="gr-fc2" style="column-gap:calc(var(--grid-gutter)*var(--s))">' + "<i></i>" * 12 + f'</div></div></div><figcaption>Tính cả lề, như Untitled: nội dung 1216, cột {num(col(1280, 0, 12, 32, 32))}</figcaption></figure>',
    '<figure class="gr-fig"><div class="gr-fr" style="--s:.3;--m:240px;width:calc(1600px*var(--s))"><div class="gr-fm" style="width:calc(var(--m)*var(--s))"></div>'
    '<div class="gr-cb" style="left:calc((var(--m) + (1360px - var(--width-2xl) - 2*var(--grid-gutter))/2)*var(--s));width:calc((var(--width-2xl) + 2*var(--grid-gutter))*var(--s));padding:0 calc(var(--grid-gutter)*var(--s))"><div class="gr-fc2" style="column-gap:calc(var(--grid-gutter)*var(--s))">' + "<i></i>" * 12 + f'</div></div></div><figcaption>Không tính lề: nội dung 1280, cột {num(col(1344, 0, 12, 32, 32))}</figcaption></figure>',
))

PV_SCOPE = pane(row(
    fr(1280, MENU, 12, 32, 32, ".4", "Tính sau menu"),
    fr(1280, 0, 12, 32, 32, ".4", "Tính từ mép màn: menu 240 che vừa 2 cột, nội dung sát menu", ghost=MENU),
))

PV_KPI = pane(row(
    fr(1280, MENU, 12, 32, 32, ".4", "Ba khối KPI rãnh 32: mép khối trùng mép cột", kpi="var(--grid-gutter)"),
    fr(1280, MENU, 12, 32, 32, ".4", "Ba khối KPI rãnh 12: mép giữa lệch cột", kpi="var(--space-lg)"),
))

PV_TAB = pane(row(
    fr(768, MENU_S, 6, 24, 24, ".5", "Theo <code>design-system/foundations/grids.md</code>", v_gut=V_TAB, v_mar=V_TAB),
    fr(768, MENU_S, 6, 32, 32, ".5", "Như Untitled và như web"),
))

PV_TOK = pane(row(
    appf(393, f'{APP_BAR}<div class="tp-pad">{ORDER_CARD}</div>', "Đọc biến hiện tại trên app: 12 cột, rãnh 32", "repeat(var(--grid-columns),minmax(0,1fr))", "var(--grid-gutter)", 12),
    appf(393, f'{APP_BAR}<div class="tp-pad">{ORDER_CARD}</div>', "Sau khi đổi: 4 cột, rãnh 16"),
))


def _merge(m, p):
    rows_ = "".join(f'<div class="gr-bar"><span class="gr-bl"><code>width/{n}</code> <b class="tp-num" data-read="--width-{n}"></b></span><div class="gr-bb" style="width:calc(var(--width-{n})*.14)"></div></div>' for n in ("xs", "sm", "md", "lg", "xl", "2xl"))
    return (rows_ + '<p class="small" style="margin:8px 0 0">Khác theo nền tảng: lề <b class="tp-num" data-read="--layout-screen-inset"></b>, '
            'rộng tối đa <b class="tp-num" data-read="--layout-content-max-width"></b></p>')


PV_MERGE = kit.panes(_merge, modes=("light",), platforms=("web", "mobile"))

PV_WEBF = pane(row(
    fr(1024, MENU_S, 12, 32, 32, ".27", "1024, menu 64"),
    fr(1280, MENU, 12, 32, 32, ".27", "1280, menu 240"),
    fr(1920, MENU, 12, 32, 32, ".27", "1920 trải hết, bản bảng"),
))

PV_APPF = pane(row(*[appf(w, f'{APP_BAR}<div class="tp-pad">{ORDER_CARD}</div>', f"{w} · cột {num(col(w, 0, 4, 16, 16))}") for w in (393, 375, 320)], fit=True))

PV_FILL = pane('<div class="type-label">Bây giờ: rộng cứng <code>field/width-default</code> App</div>' + row(*[appf(w, f'<div class="tp-pad">{FIXED_FIELD}</div>', f"{w}") for w in (393, 375, 320)], fit=True)
               + '<div class="type-label" style="margin-top:12px">Sau khi đổi: trải theo màn trừ lề</div>' + row(*[appf(w, f'<div class="tp-pad">{FILL_FIELD}</div>', f"{w}") for w in (393, 375, 320)], fit=True))

_nav = lambda ic, x, on="": f'<div class="tp-nav {on}">{kit.icon(ic)}<span class="type-label">{x}</span></div>'
_tr = lambda code, r, m, c, x: f'<tr><td><div class="type-code">{code}</div></td><td><div class="type-body">{r}</div></td><td><span class="type-body tp-num">{m}</span></td><td><span class="tp-chip {c}">{x}</span></td></tr>'
_sw_btn = "".join(f'<button data-w="{w}" aria-pressed="{"true" if w == 1280 else "false"}">{w}</button>' for w in (1440, 1280, 1024, 768, 393, 375, 320))
PV_BP = pane(
    '<div class="gr-sw" id="grSw"><div class="gr-swb"><span><span class="tp-lab">Bề rộng khung</span><span class="tp-seg">' + _sw_btn + '</span></span>'
    '<input type="range" min="320" max="1440" value="1280" aria-label="Kéo đổi bề rộng khung">'
    '<span><span class="tp-lab">Tablet</span><span class="tp-seg" data-tab><button data-t="24" aria-pressed="false">Rãnh, lề 24</button><button data-t="32" aria-pressed="true">Rãnh, lề 32</button></span></span></div>'
    '<div class="gr-read" data-out></div><div class="gr-stage"><div class="tp-f gr-sf" data-platform="web"><aside class="tp-side gr-side">'
    f'<div class="tp-logo">{kit.mini_mark()}<span class="type-title-3 gr-hide">Invlogis</span></div>'
    + _nav("truck", "Lệnh vận tải", "on") + _nav("container", "Phương tiện") + _nav("users", "Tài xế") + _nav("fuel", "Nhiên liệu")
    + '</aside><div class="tp-main gr-main"><div class="tp-top"><div class="type-title-1">Lệnh vận tải</div>'
    f'<span class="tp-btn">{kit.icon("plus")}<span class="type-label">Tạo lệnh</span></span></div>'
    '<div class="tp-kpis gr-k"><div class="tp-card"><div class="type-caption tp-sub">Đang chạy</div><div class="type-title-1 tp-num">128</div></div><div class="tp-card"><div class="type-caption tp-sub">Chờ duyệt</div><div class="type-title-1 tp-num">16</div></div><div class="tp-card"><div class="type-caption tp-sub">Doanh thu</div><div class="type-title-1 tp-num">412 tr ₫</div></div></div>'
    '<div class="tp-card gr-tbl"><table class="tp-tb"><tbody>' + _tr("LVT-2026-0412", "Cát Lái → KCN Long Hậu", "1.250.000 ₫", "tp-b", "Đang chạy") + _tr("LVT-2026-0411", "ICD Phước Long → Bình Dương", "2.480.000 ₫", "tp-g", "Hoàn thành") + _tr("LVT-2026-0409", "Cảng Hiệp Phước → Đồng Nai", "980.000 ₫", "tp-y", "Chờ duyệt")
    + f'</tbody></table></div><div class="gr-cards">{ORDER_CARD}{ORDER_CARD.replace("LVT-2026-0412", "LVT-2026-0411").replace("Cát Lái → KCN Long Hậu", "ICD Phước Long → Bình Dương").replace("51C-482.15 · Nguyễn Văn Hoà", "51D-120.77 · Trần Quốc Việt")}</div></div>'
    f'<div class="gr-tabs">{kit.icon("truck", "tp-ic-lg")}{kit.icon("container", "tp-ic-lg")}{kit.icon("bell", "tp-ic-lg")}{kit.icon("settings", "tp-ic-lg")}</div>'
    '<div class="gr-ovl gr-live" data-ov>' + "<i></i>" * 12 + "</div></div></div></div>")

# ───────────── CSS, JS riêng trang ─────────────
CSS = r"""
.rv{--s:1;--m:0px}
#tpWrap{--gr-web:var(--width-2xl);--gr-menu:240px;--gr-app:393px;--gr-cols:12}
.tp-f{--gr-ovm:var(--layout-screen-inset);--gr-ovg:var(--grid-gutter)}
#tpWrap .tp-f.tp-app{width:var(--gr-app);--gr-ovg:var(--space-xl)}
#tpWrap .tp-web{width:var(--gr-web);grid-template-columns:var(--gr-menu) minmax(0,1fr)}
#tpWrap .tp-webs,#tpWrap .tp-webc{width:calc(var(--gr-web) - var(--gr-menu))}
#tpWrap .tp-dlg:not(.tp-sheet){width:var(--width-sm)}
#tpWrap .tp-card:has(.tp-tb){overflow-x:auto}
#tpWrap .gr-detail .tp-main{grid-template-columns:repeat(var(--gr-cols),minmax(0,1fr));column-gap:var(--grid-gutter);align-items:start}
#tpWrap .gr-detail .tp-top{grid-column:1/-1}
#tpWrap .gr-detail .tp-card:nth-of-type(2){grid-column:span 8}
#tpWrap .gr-detail .tp-card:nth-of-type(3){grid-column:span 4}
#tpWrap[data-webf="768"] .gr-detail .tp-card{grid-column:1/-1!important}
#tpWrap .gr-form .tp-card{max-width:var(--width-md)}
#tpWrap .tp-f:not(.tp-app) .tp-gridov i:nth-child(n+7){display:var(--gr-i7,block)}
#tpWrap[data-webf="768"]{--gr-i7:none;--gr-cols:6}
#tpWrap[data-webf="768"] .tp-f:not(.tp-prop):not(.tp-app){--gr-ovm:var(--space-3xl);--gr-ovg:var(--space-3xl)}
#tpWrap[data-menu="64"] .tp-side .type-label,#tpWrap[data-menu="64"] .tp-side .type-caption-caps,#tpWrap[data-menu="64"] .tp-logo span{display:none}
.gr-x{overflow-x:auto;padding-bottom:4px}.gr-row{display:flex;gap:var(--space-xl);align-items:flex-start;width:max-content}
.gr-fit{zoom:.85}
.gr-fig{margin:0;min-width:0}.gr-fig figcaption{font:500 12px/16px Inter,sans-serif;color:var(--color-text-tertiary);margin-top:6px;max-width:100%}
.gr-fr{position:relative;height:var(--size-10xl);background:var(--color-bg-secondary);border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);overflow:hidden}
.gr-fm{position:absolute;left:0;top:0;bottom:0;background:var(--color-bg-tertiary);border-right:1px solid var(--color-border-secondary)}
.gr-gh{z-index:2;opacity:.85}
.gr-fc,.gr-ovl{position:absolute;top:0;bottom:0;display:grid;pointer-events:none}
.gr-fc i,.gr-ovl i,.gr-fc2 i{background:color-mix(in srgb,var(--color-utility-red-500) 16%,transparent);display:block;height:100%}
.gr-ovl{z-index:3}.gr-fk{position:absolute;top:var(--space-2xl);bottom:var(--space-2xl);display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
.gr-fk b{background:var(--color-bg-primary);border:1px solid var(--color-border-primary);border-radius:var(--radius-xs)}
.gr-cb{position:absolute;top:0;bottom:0;background:var(--color-bg-primary);box-sizing:border-box}.gr-fc2{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));height:100%}
.gr-app{min-height:0}
.gr-bar{display:flex;align-items:center;gap:var(--space-md);margin:var(--space-xs) 0}.gr-bl{flex:none;width:var(--size-10xl);overflow-wrap:anywhere;font-size:12px;line-height:16px}
.gr-bb{height:var(--space-xl);min-width:2px;background:var(--color-utility-blue-500);border-radius:var(--radius-xxs)}.gr-bb.u{background:var(--color-utility-blue-100);outline:1px dashed var(--color-utility-blue-500);outline-offset:-1px}
.gr-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-xl)}@media(max-width:820px){.gr-2{grid-template-columns:minmax(0,1fr)}}
.gr-pb{margin-bottom:var(--space-lg)}.gr-para{margin:var(--space-xs) 0 0;color:var(--color-text-secondary)}.gr-lc{color:var(--color-text-secondary)}
.gr-ins{height:var(--size-8xl);background:var(--color-utility-red-50);border:1px solid var(--color-border-secondary);border-radius:var(--radius-sm)}.gr-insc{height:100%;background:var(--color-bg-tertiary)}
.gr-swb{display:flex;flex-wrap:wrap;gap:var(--space-md) var(--space-xl);align-items:center}.gr-swb input{flex:1;min-width:var(--size-11xl);accent-color:var(--color-utility-blue-500)}
.gr-read{margin:var(--space-md) 0;font:500 13px/18px Inter,sans-serif;font-variant-numeric:tabular-nums}
.gr-read b{font-weight:700}.gr-stage{overflow:hidden;background:var(--color-bg-secondary);border-radius:var(--radius-md)}
.gr-sf{transform-origin:0 0;display:grid;min-height:var(--size-11xl)}.gr-main{align-content:start}.gr-sf .tp-card:has(.tp-tb){overflow-x:auto}
.gr-tabs{display:none;justify-content:space-around;padding:var(--space-lg) var(--layout-screen-inset);border-top:1px solid var(--color-border-secondary);color:var(--color-fg-secondary)}
.gr-cards{display:none;gap:var(--layout-list-gap)}
.gr-sf[data-mode="app"]{display:flex;flex-direction:column}.gr-sf[data-mode="app"] .gr-side,.gr-sf[data-mode="app"] .gr-k,.gr-sf[data-mode="app"] .gr-tbl{display:none}
.gr-sf[data-mode="app"] .gr-cards{display:grid}.gr-sf[data-mode="app"] .gr-tabs{display:flex}
.gr-sf[data-menu="64"] .gr-side .type-label,.gr-sf[data-menu="64"] .gr-hide{display:none}
"""

JS = r"""
// khung theo bề rộng: đọc mốc và rãnh từ biến thật
function grVar(n){return parseFloat(getComputedStyle(document.documentElement).getPropertyValue(n))}
function grRule(w,tab){const g=grVar('--grid-gutter');
 if(w<grVar('--bp-md'))return{app:1,menu:0,cols:4,gut:16,mar:16,bp:'dưới 768, bố cục app'};
 if(w<grVar('--bp-lg'))return{menu:64,cols:6,gut:tab,mar:tab,bp:'768–1023, 6 cột, menu thu gọn'};
 if(w<grVar('--bp-xl'))return{menu:64,cols:12,gut:g,mar:g,bp:'1024–1279, 12 cột, menu thu gọn'};
 return{menu:240,cols:12,gut:g,mar:g,bp:'từ 1280, 12 cột, menu mở'}}
// thanh trên màn mẫu: chọn khung web, khung app
(function(){const bar=$('#tpBar'),W=$('#tpWrap');if(!bar)return;
 const seg=(lab,k,vals,on)=>{const s=document.createElement('span');s.innerHTML='<span class="tp-lab">'+lab+'</span><span class="tp-seg" data-gr="'+k+'">'+vals.map(v=>'<button data-v="'+v+'" aria-pressed="'+(v===on)+'">'+v+'</button>').join('')+'</span>';bar.appendChild(s);
  s.querySelector('.tp-seg').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;s.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));k==='web'?web(+b.dataset.v):W.style.setProperty('--gr-app',b.dataset.v+'px')})};
 function web(w){const r=grRule(w,grVar('--grid-gutter'));W.style.setProperty('--gr-web',w+'px');W.style.setProperty('--gr-menu',r.menu+'px');W.dataset.menu=r.menu;W.dataset.webf=w;tag()}
 seg('Khung web','web',[1440,1280,1024,768],1280);seg('Khung app','app',[393,375,320],393);
 const on=$('#tpBar [data-k="gridov"] [data-v="on"]');if(on)on.click()})();
// xem thử đổi bề rộng khung
(function(){const R=$('#grSw');if(!R)return;const F=R.querySelector('.gr-sf'),St=R.querySelector('.gr-stage'),O=R.querySelector('[data-ov]'),Out=R.querySelector('[data-out]'),Rg=R.querySelector('input[type=range]');let cur=1280,tab=32;
 const fmt=x=>String(Math.round(x*100)/100).replace('.',',');
 function apply(){const r=grRule(cur,tab),s=Math.min(1,(St.clientWidth||1060)/cur);
  F.style.width=cur+'px';F.style.transform='scale('+s+')';F.dataset.mode=r.app?'app':'web';F.dataset.menu=r.menu;F.setAttribute('data-platform',r.app?'mobile':'web');
  F.style.gridTemplateColumns=r.app?'':r.menu+'px minmax(0,1fr)';
  const inset=parseFloat(getComputedStyle(F).getPropertyValue('--layout-screen-inset'));
  O.style.cssText='left:'+(r.menu+r.mar)+'px;right:'+r.mar+'px;grid-template-columns:repeat('+r.cols+',minmax(0,1fr));column-gap:'+r.gut+'px';
  [...O.children].forEach((i,n)=>{i.style.display=n<r.cols?'block':'none'});
  St.style.height=Math.ceil(F.offsetHeight*s)+'px';
  const c=(cur-r.menu-2*r.mar-(r.cols-1)*r.gut)/r.cols;
  Out.innerHTML='<b>'+cur+'</b> · '+r.bp+' · menu <b>'+(r.menu||'không')+'</b> · <b>'+r.cols+'</b> cột, rộng <b>'+fmt(c)+'</b> · rãnh <b>'+r.gut+'</b> · lề lưới <b>'+r.mar+'</b> · lề biến <code>layout/screen-inset</code> đọc được <b>'+inset+'</b>'+(inset!==r.mar?' <mark>lệch lưới</mark>':'')+(cur!==1280&&s<1?' · thu nhỏ '+Math.round(s*100)+'%':'');
  R.querySelectorAll('[data-w]').forEach(b=>b.setAttribute('aria-pressed',String(+b.dataset.w===cur)));Rg.value=cur}
 R.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;if(b.dataset.w){cur=+b.dataset.w;apply()}if(b.dataset.t){tab=+b.dataset.t;R.querySelectorAll('[data-t]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));apply()}});
 Rg.addEventListener('input',()=>{cur=+Rg.value;apply()});addEventListener('resize',apply);window.grApply=apply})();
// đọc biến, đếm ký tự dòng đầu trên trang
function grMeasure(){$$('[data-read]').forEach(e=>{e.textContent=getComputedStyle(e).getPropertyValue(e.dataset.read).trim()});
 $$('.gr-para').forEach(p=>{const n=p.firstChild,r=document.createRange();let top=null,c=0;for(let i=0;i<n.length;i++){r.setStart(n,i);r.setEnd(n,i+1);const b=r.getClientRects();if(!b.length)continue;if(top===null)top=b[0].top;else if(b[0].top>top+2)break;c++}
  const l=p.parentElement.querySelector('.gr-lc');if(l)l.textContent=Math.round(p.getBoundingClientRect().width)+'px, dòng đầu '+c+' ký tự'});
 if(window.grApply)grApply()}
window.afterToggle=grMeasure;
"""

ITEMS = [
    dict(id="gr00", grp="Độ rộng", title="Sáu token width: năm token trùng tên Untitled mà khác số, đổi sao?",
         why=f"<b>Mở lại DEC-259 mục T4, GR4:</b> bằng chứng mới là DEC-320, DEC-322 sau đó chốt tên theo Untitled. Hiện <b>5/6</b> token mang đúng tên của Untitled nhưng khác số (chỉ <code>width/md</code> 560 trùng cả hai): <code>width/xs</code> mình 320, họ 384; <code>width/2xl</code> mình 1280, họ 1024. Người đọc Untitled rồi viết <code>width/xl</code> sẽ được 960 thay vì 768. Đổi lúc này rẻ: <code>design-system/_review/token-usage.json</code> ghi <mark>2/6 token có component dùng</mark>, là Tooltip (<code>width/xs</code>) và Sidebar navigation (<code>width/xl</code>). <b>Nói thẳng:</b> nếu chỉ dời tên theo Untitled mà giữ số thì vẫn còn <code>width/xs</code> 400 (Untitled 384) và <code>width/2xl</code> 960 (Untitled 1024), <mark>cùng tên khác số, lý do của mục chỉ đạt một phần</mark>. Muốn hết hẳn, hai số riêng phải mang tên không có ở Untitled.",
         untitled="<code>width-xxs 320 · xs 384 · sm 480 · md 560 · lg 640 · xl 768 · 2xl 1024 · 3xl 1280 · 4xl 1440 · 5xl 1600 · 6xl 1920</code>, thêm <code>paragraph-max-width</code> 720",
         ours="<code>width/xs 320 · sm 400 · md 560 · lg 720 · xl 960 · 2xl 1280</code> (DEC-259)",
         astryx="Không có thang width. <code>design/design.md</code> ghi số theo mẫu: form 800, chi tiết 1200, shell 1100.",
         tokens=[("width/xxs", "320", "Popover, menu thả rộng, Tooltip Supporting. Đổi tên từ width/xs"),
                 ("width/overlay-sm", "400", "Dialog xác nhận, drawer thường. Giữ 400 vì slideout của Untitled thật là 400; bậc width-xs của họ là 384 nên không mượn tên"),
                 ("width/md", "560", "Dialog form, form 1 cột. Không đổi"),
                 ("width/overlay-lg", "960", "Drawer rộng, hộp thoại phạm vi. Giữ 960 = 1024 − 2 × 32 vừa khít màn 1024; bậc width-2xl của họ là 1024 nên không mượn tên"),
                 ("width/3xl", "1280", "Khung nội dung tối đa. Đổi tên từ width/2xl")],
         note="Vai đoạn văn (đang là <code>width/lg</code>) tách ra mục gr02. Vai “dialog lớn” của 720 chưa component nào dùng nên bỏ theo. Phụ thuộc sp09: thang <code>size/*</code> dừng ở 160, nếu sp09 thêm bậc 240 vào thang đó thì nằm ngay dưới 320 của thang này, không đụng nhau.",
         pv=PV_NAMES,
         opts=[("d", "Tên Untitled cho số trùng (xxs 320, md 560, 3xl 1280), tên vai cho 400 và 960", True), ("a", "Dời cả 5 tên theo Untitled, giữ số; còn 2 cặp cùng tên khác số (xs, 2xl)", False), ("b", "Giữ tên cũ, thêm bảng quy đổi vào tài liệu", False), ("c", "Theo cả tên lẫn số Untitled: 400 → 384, 960 → 1024, hai cỡ hộp thoại đổi", False)]),
    dict(id="gr01", grp="Độ rộng", title="Bảy bậc Untitled mình không có, thêm bậc nào?",
         why="Mình thiếu <code>width-sm</code> 480, <code>width-lg</code> 640, <code>width-xl</code> 768, <code>width-2xl</code> 1024, <code>width-4xl</code> 1440, <code>width-5xl</code> 1600, <code>width-6xl</code> 1920. Sổ 26 component: <mark>không component nào đọc bậc thang ở các số này</mark>; 768 trở lên là bề rộng khung, đã có ở breakpoint. Nhưng có <b>3 token Component mang số rộng riêng</b> đang treo từ sp09 (ghi ở ô vàng): chỉ 480 trùng bậc Untitled, mà vai là ảnh, không phải khối nội dung. Luật chung: không mượn token vai khác vì trùng số. Tinh thần DEC-320: không thêm token không ai dùng.",
         untitled="Ref mô tả: “để đặt max-width cho section nội dung chữ và page heading”. Nguồn gốc là trang marketing; <code>max-w-container</code> mới là số component dùng.",
         ours="<code>width/sm</code> 400 nhảy thẳng lên <code>width/md</code> 560, rồi <code>width/lg</code> 720.",
         astryx="Không có thang; mỗi mẫu một số riêng.",
         tokens=[("width/sm", "480", "Chỉ khi chọn thêm 2 bậc: dialog vừa"), ("width/lg", "640", "Chỉ khi chọn thêm 2 bậc: dialog có bảng nhỏ, hộp ⌘K")],
         note="Ba token treo, số đọc từ <code>design-system/tokens.json</code>: <code>vehicle/q-lg-w</code> 480, khung ảnh 3/4 trước đầu trang chi tiết phương tiện (DEC-266), sổ dùng token chưa ghi component nào đọc · <code>header-nav/account-menu-width</code> 256, menu tài khoản, Header navigation dùng (DEC-305); Untitled có <code>w-66</code> 264 ở <code>nav-account-card.tsx</code> · <code>command-search/width</code> 600, hộp tìm ⌘K, Header navigation dùng (DEC-305); ref Untitled không có hộp tìm để so. Phụ thuộc sp09: dòng “Chờ trang Lưới” của sp09 lấy kết quả mục này.",
         pv=PV_MISSING,
         opts=[("a", "Không thêm bậc; 480, 256, 600 giữ ở token Component, ghi ngoại lệ", True), ("b", "Thêm 480 và 640; ⌘K 600 → 640 trỏ bậc, ảnh xe, menu tài khoản giữ riêng", False), ("c", "Thêm đủ 7 bậc cho khớp Untitled", False)]),
    dict(id="gr02", grp="Độ rộng", title="Đoạn văn tối đa rộng bao nhiêu với chữ 14?",
         why="<b>Mở lại DEC-259 mục T4, phần vai đoạn văn:</b> bằng chứng mới là số đếm dưới đây. Đang có <mark>hai luật lệch nhau</mark>: <code>width/lg</code> 720 ghi “Đoạn văn tối đa”, còn lớp <code>.prose</code> trong <code>design-system/tokens.css</code> ghi <code>max-width: 72ch</code>. Luật Untitled: “Độ dài dòng đoạn văn lý tưởng ~45–85 ký tự (85–105 quá dài)”, mặc định 720, nhưng chữ thân của họ cỡ 16. Chữ thân của mình 14 (<code>type/body</code>, DEC-322), nên cùng 720 thì nhiều chữ hơn. Đếm trên trang với đoạn tiếng Việt thật: <mark>720 ra 107 ký tự, 72ch ra 96, 560 ra 82</mark>, chỉ 560 lọt khoảng 45–85. Số đếm hiện ngay trong xem thử.",
         untitled="<code>paragraph-max-width</code> 45rem (720), “đổi được một chỗ”.",
         ours="<code>width/lg</code> 720 · <code>.prose</code> 72ch · <code>type/body</code> 14/20.",
         astryx="Form tối đa 720 trong khung trang dự án; không có luật riêng cho đoạn văn.",
         tokens=[("width/paragraph-max", "trỏ width/md 560", "Đoạn văn, thân form đọc nhiều. Lớp .prose đọc từ biến này")],
         pv=PV_PARA,
         opts=[("a", "Đoạn văn tối đa 560 cho chữ 14, .prose đọc từ width/paragraph-max", True), ("b", "Giữ 720 như Untitled, bỏ 72ch", False), ("c", "Giữ 72ch trong .prose, bỏ vai đoạn văn khỏi thang width", False)]),
    dict(id="gr03", grp="Container", title="Ba token container đang mang tên layout, đổi theo Untitled?",
         why="Cả ba số đã khớp Untitled (DEC-259), chỉ khác tên. Mình gộp hai lề Untitled thành một token hai chế độ, gọn hơn nên giữ. <code>layout/content-max-width</code> ghi số trần 1280 thay vì trỏ thang, trùng <code>width/2xl</code>; luật DEC-314 là token theo vai trỏ vào thang. Sổ dùng token: <mark>0/26 component</mark> đọc hai token này nên đổi tên không kéo theo màn nào.",
         untitled="<code>container-padding-mobile</code> 16, <code>container-padding-desktop</code> 32, <code>container-max-width-desktop</code> 1280, “tách khỏi width/spacing thường để đổi nhanh toàn bộ thiết kế”.",
         ours="<code>layout/screen-inset</code> Web 32, App 16 · <code>layout/content-max-width</code> Web 1280, App 393.",
         astryx="Lề 16 ở mẫu, khung trang dự án lề 24 (<code>design/design.md</code>, trước DS v2).",
         tokens=[("container/padding", "Web space/4xl 32 · App space/xl 16", "Lề màn. Thay layout/screen-inset"),
                 ("container/max-width", "trỏ width/3xl 1280", "Rộng tối đa màn chi tiết, form. Thay layout/content-max-width")],
         note="Các token <code>layout/*</code> còn lại (khe khối, lề thẻ) thuộc trang Khoảng cách, không xét ở đây.",
         pv=PV_CONT,
         opts=[("a", "Đổi sang container/padding, container/max-width, trỏ thang", True), ("b", "Giữ tên layout/*, chỉ cho max-width trỏ thang", False), ("c", "Ba token đúng tên Untitled, bỏ cách một token hai chế độ", False)]),
    dict(id="gr04", grp="Container", title="App đang chặn rộng 393, có nên bỏ?",
         why="<code>layout/content-max-width</code> App = 393 tức nội dung app không rộng quá khung vẽ. Đọc đúng biến này trên máy rộng 430 sẽ <mark>thừa hai dải trống</mark>, lái xe nhìn dữ liệu nhỏ đi mà không vì lý do gì. Untitled chỉ có <code>container-max-width-desktop</code>, không chặn điện thoại. Trong <code>design-system/foundations/grids.md</code> ô Rộng tối đa của app cũng để trống, nên token đang <mark>lệch với chính luật</mark>. 0/26 component đọc giá trị này.",
         untitled="Không có token tương ứng; chỉ <code>container-max-width-desktop</code>.",
         ours="<code>layout/content-max-width</code> App 393 · bảng lưới ghi “—”.",
         astryx="Khung mẫu 393 (<code>Device / Frame</code>), không ghi giới hạn khi chạy thật.",
         tokens=[("container/max-width", "Web width/3xl 1280 · App none", "App trải đủ màn")],
         pv=PV_MOBMAX,
         opts=[("a", "App không chặn, app trải đủ bề rộng máy", True), ("b", "Giữ chặn 393, căn giữa trên máy lớn", False)]),
    dict(id="gr05", grp="Container", title="Rộng tối đa 1280 tính cả lề hay chưa tính?",
         why=f"Tài liệu ghi “rộng tối đa 1280”, token ghi “Rộng nội dung tối đa”, nên hai người đọc ra hai kết quả. Code Untitled viết <code>mx-auto max-w-container px-4 md:px-8</code>: lề nằm trong 1280, nội dung còn 1216, cột 72, khớp bảng lưới của họ. Giới hạn chỉ chạm tới khi màn rộng từ 1520 (1280 + menu 240); màn bảng trải hết nên không bị ảnh hưởng (DEC-259).",
         untitled="<code>--max-width-container</code> 1280 trong <code>design/_ref/untitled-ui/raw/theme.css</code>, cộng padding trong khung ở <code>section-divider.tsx</code>, <code>header-navigation.tsx</code>.",
         ours="<code>layout/content-max-width</code> 1280, không nói có lề hay không.",
         astryx="Chi tiết 1200, shell 1100, không nói có lề hay không.",
         pv=PV_MAX,
         opts=[("a", "1280 gồm cả lề, nội dung 1216, cột 72 như Untitled", True), ("b", "1280 là riêng nội dung, cả khung 1344", False)]),
    dict(id="gr06", grp="Lưới", title="Lưới web tính trong vùng nào: cả màn hay sau menu?",
         why=f"Bảng Untitled vẽ khung 1280 <mark>không có menu trái</mark>, cột 72. Web mình luôn có menu: màn 1280 trừ menu 240 (DEC-039) còn vùng 1040, trừ hai lề 32 còn 976, cột <b>{num(col(1280, MENU, 12, 32, 32))}</b>, màn chi tiết 8 + 4 cột thành <b>{num(span(col(1280, MENU, 12, 32, 32), 8, 32))} + {num(span(col(1280, MENU, 12, 32, 32), 4, 32))}</b>. <code>design-system/foundations/grids.md</code> không nói tính từ đâu. Tính từ mép màn thì cột 3 bắt đầu đúng ở 240 (lề 32 + 2 cột 72 + 2 rãnh 32), menu mở chiếm vừa 2 cột. Nhưng khi đó <mark>nội dung sát viền menu, mất lề trái</mark>; và menu thu gọn 64 rơi giữa cột 1, nên mỗi lần thu mở menu nội dung lại lệch cột.",
         untitled="Khung Desktop 1280 trong MacBook 1440, lề 32, rãnh 32, <code>container-padding-desktop</code>.",
         ours="<code>grid/columns</code> 12, <code>grid/gutter</code> 32, DEC-127 chia 8 + 4, chưa nêu vùng tính.",
         astryx="Không có lưới cột; mẫu chi tiết ghi số trực tiếp: cột chính 879, rail 320.",
         pv=PV_SCOPE,
         opts=[("a", "Tính trong vùng sau menu, 12 cột giữ nguyên ở mọi khung web", True), ("b", "Tính từ mép màn: menu mở chiếm 2 cột, còn 10 cột, nội dung sát menu", False)]),
    dict(id="gr07", grp="Lưới", title="Khối cấp màn có canh đúng cột không?",
         why=f"<b>Định nghĩa:</b> khối cấp màn đặt trên lưới, cách nhau theo rãnh <code>grid/gutter</code>; thẻ trong một danh sách cách nhau theo <code>layout/list-gap</code> (DEC-192, trang Khoảng cách sp04). Bật Phủ lưới ở màn thật: ba thẻ KPI trong kit dùng rãnh 12, mép giữa <mark>không trùng cột</mark>. Đổi về rãnh 32 thì mỗi thẻ rộng 304 thay vì 317 ở vùng 1040, mất 13 mỗi thẻ. Chuyện rãnh 32 có quá thưa cho web điều vận không: đo cho thấy <b>không đáng mở lại DEC-259</b>, vì khối 8 cột gần như không đổi: rãnh 32 ra {num(span(_c1040[32], 8, 32))}, rãnh 24 ra {num(span(_c1040[24], 8, 24))}, rãnh 16 ra {num(span(_c1040[16], 8, 16))}.",
         note="Phụ thuộc sp04: nếu chọn gộp ở sp04, <code>layout/list-gap</code> thành 12 cả Web và App; định nghĩa trên không đổi.",
         untitled="Lưới cột auto 12/6/5/3/2 chia bên trong khối (“layout guide styles”); ref chưa đọc rãnh. Cạnh đó <code>container-padding-desktop</code> 32.",
         ours="<code>grid/gutter</code> 32 · <code>layout/list-gap</code> Web 8, App 12 · màn mẫu KPI dùng <code>space/lg</code> 12.",
         astryx="Hai trường cách 16, hai cột cách 32 hoặc 40, không nối với lưới.",
         pv=PV_KPI,
         opts=[("a", "Khối cấp màn canh đúng cột, rãnh 32; trong khối dùng layout/list-gap", True), ("b", "Lưới chỉ canh mép ngoài, nhóm thẻ rãnh space/lg 12", False), ("c", "Mở lại DEC-259, hạ rãnh web về 24", False)]),
    dict(id="gr08", grp="Lưới", title="Tablet rãnh 24 lề 24 không có biến nào đọc ra, đưa về 32?",
         why="<b>Mở lại DEC-259 mục GR2:</b> dòng đó ghi rõ “giữ … tablet rãnh 24”, chủ DS đã chọn giữ khi đưa web lên 32. Bằng chứng mới là đo được lệch: tablet chạy ở chế độ token Web nên <code>layout/screen-inset</code> đọc ra <mark>32, trong khi lưới ghi 24</mark>, lưới và nội dung lệch 8 mỗi bên. Chọn khung 768, bộ Hiện tại, ở thanh trên màn mẫu để thấy. Muốn giữ 24 phải thêm biến và ghi đè theo mốc, là việc hợp lệ nhưng có giá. Ở vùng 704 (768 trừ menu 64) cột còn 80 với 32 và 89,33 với 24, cả hai đủ dùng; <code>design/design.md</code> ghi 768–1279 “không vẽ riêng”.",
         untitled="Tablet 768: 6 cột, rãnh 32, lề 32. Code <code>px-4 md:px-8</code> đổi lề 16 → 32 đúng ở 768.",
         ours="<code>design-system/tokens.json</code> mục grid.tablet: 6 cột, 24, 24, không có token.",
         astryx="Mốc md 768 chỉ đổi menu; không có lưới cột.",
         pv=PV_TAB,
         opts=[("a", "Mở lại GR2: tablet 6 cột, rãnh 32, lề 32, không thêm biến", True), ("b", "Giữ 24 theo GR2, thêm token và ghi đè theo mốc 768–1023", False), ("c", "Bỏ riêng tablet, 12 cột từ 768, cột còn 24", False)]),
    dict(id="gr09", grp="Lưới", title="Token lưới một giá trị cho mọi nền tảng, đọc trên app ra sai",
         why="<code>--grid-columns</code> 12 và <code>--grid-gutter</code> 32 nằm ngoài Platform, nên trên app vẫn đọc ra <mark>12 cột, rãnh 32</mark>; số đúng 4 và 16 chỉ có trong khối <code>grid</code> của <code>design-system/tokens.json</code>, không xuất CSS. Xem thử dựng thẳng từ hai biến để thấy. <code>--grid-gutter</code> còn là số trần, chưa trỏ thang (DEC-314). 0/26 component đọc hai biến này. Chưa kiểm được file Figma có layout guide style nào: lượt này không đụng Figma.",
         untitled="Không có token lưới; dùng layout guide style trong Figma, code dựa vào <code>--spacing</code> và lớp Tailwind.",
         ours="<code>grid/columns</code> 12 · <code>grid/gutter</code> 32 · tablet, app chỉ ghi trong tokens.json.",
         astryx="Không có lưới cột.",
         tokens=[("grid/columns", "Web 12 · App 4", "Số cột màn"), ("grid/gutter", "Web space/4xl 32 · App space/xl 16", "Rãnh cột cấp màn"),
                 ("grid/margin", "trỏ container/padding", "Lề lưới, để Figma và dev đọc một chỗ")],
         pv=PV_TOK,
         opts=[("a", "Đưa 3 token vào Platform theo nền tảng, trỏ thang, thêm layout guide style Figma", True), ("b", "Bỏ token lưới, lưới chỉ ghi trong tài liệu, Figma giữ guide", False), ("c", "Giữ nguyên, ghi chú chỉ áp web", False)]),
    dict(id="gr10", grp="Lưới", title="Phần nào gộp một bộ web và app?",
         why="Hướng đã chốt: gộp một bộ khi làm được (DEC-316, DEC-322). Sáu token <code>width/*</code> <mark>bằng nhau 6/6</mark> ở Web và App, đang nằm trong collection <code>5. Platform · Sizes</code> chỉ vì cả nhóm ở đó. Cột, rãnh, lề thì không gộp được: điện thoại 393 không chứa nổi 12 cột rãnh 32.",
         untitled="<code>width-*</code> một bộ; container tách <code>-mobile</code>, <code>-desktop</code> trong cùng tên.",
         ours="<code>width/*</code> hai cột Web = App · <code>layout/screen-inset</code> 32 · 16 · lưới 12 · 4.",
         astryx="Không có token cho nhóm này.",
         pv=PV_MERGE,
         opts=[("a", "Width một giá trị dùng chung; lề, cột, rãnh vẫn theo nền tảng", True), ("b", "Giữ tất cả theo nền tảng cho đồng đều bảng biến", False)]),
    dict(id="gr11", grp="Khung và breakpoint", title="Web vẽ ở khung chuẩn nào?",
         why="Hiện <mark>chưa nơi nào chốt</mark>: Untitled 1280 trong MacBook 1440, <code>design-system/components/application/header-navigation.md</code> 1280, <code>design/design.md</code> bản cũ 1440 và 1920. <code>design-system/foundations/grids.md</code> không nêu số nào cho web, chỉ nêu app. Khung 1280 với menu 240 (DEC-039) còn vùng 1040, khó nhất cho bảng; lên màn to thì chỉ giãn ra; vẽ 1920 rồi co xuống dễ tràn. Chưa có số liệu màn hình thật của phòng điều vận Delta, cần hỏi khi có dịp.",
         untitled="Khung lưới 1280 đặt trong MacBook 1440; <code>container-max-width-desktop</code> 1280.",
         ours="<code>width/2xl</code> 1280, “1040 ở màn chuẩn”, chưa ghi vào foundations.",
         astryx="Mọi mẫu dựng 1920 × 1080.",
         pv=PV_WEBF,
         opts=[("a", "Vẽ 1280, menu mở; mỗi màn kiểm thêm 1024; màn bảng kiểm 1920", True), ("b", "Vẽ 1440 như khung thiết bị Untitled", False), ("c", "Vẽ 1920 như bảng cũ của design.md", False)]),
    dict(id="gr12", grp="Khung và breakpoint", title="App vẽ khung nào, kiểm tới bề rộng nào?",
         why=f"Đề xuất <b>không đổi khung vẽ 393</b>: <code>design/design.md</code> chuyển từ 375 sang 393 ngày 06/10/2026, các đường canh và màn đã dựng theo đó. Điều còn thiếu là <mark>chưa có luật khung kiểm nhỏ nhất</mark>: <code>--bp-xxs</code> 320 có trong token, 3 component (Vehicle card, Vehicle option card, Combo text) đã tự kiểm ở 320, nhưng foundations chưa ghi nên màn không ai kiểm. Cột: 393 ra {num(col(393, 0, 4, 16, 16))}, 375 ra {num(col(375, 0, 4, 16, 16))}, 320 ra {num(col(320, 0, 4, 16, 16))}. 375 là khung Untitled, cùng 320 chỉ dùng làm máy thử.",
         untitled="Khung lưới Mobile 375 (iPhone), <code>--breakpoint-xxs</code> 320.",
         ours="<code>--bp-xxs</code> 320 · App (khung 393) trong <code>design-system/foundations/grids.md</code>.",
         astryx="393 × 852 (<code>Device / Frame</code>).",
         pv=PV_APPF,
         opts=[("a", "Vẽ 393, mỗi màn thử thêm máy 320 (chữ dài, nút, bảng thẻ)", True), ("b", "Đổi về 375 như Untitled, vẽ lại các khung đã có", False), ("c", "Vẽ 393, không kiểm khung nhỏ", False)]),
    dict(id="gr13", grp="Khung và breakpoint", title="Ô nhập, thanh tiến độ trên app rộng cứng 361",
         why="<b>Mở lại DEC-243, phần rộng app:</b> đo lại trên máy thử. <code>field/width-default</code> và <code>progress/width-default</code> (chế độ token Mobile) = <b>361</b>, tức 393 − 2 × 16 viết thành số. Trên máy 375 nội dung chỉ còn 343, ô <mark>lấn qua lề phải 18</mark>; trên 320 nội dung còn 288, ô <mark>vượt mép màn 57</mark> và bị cắt. <code>design-system/components/_work/form-controls/page.json</code> đọc <code>field/width-default</code> 3 lần. Toast đã viết đúng cách: “rộng theo màn trừ lề 16 (361 trên khung 393)” trong <code>design-system/components/base/alert-notification.md</code>. Thanh điều hướng nổi 361 (DEC-160) cũng cần viết lại theo cách đó.",
         untitled="Component dùng <code>w-full</code>, cha quyết bề rộng.",
         ours="<code>field/width-default</code> 320 · 361 · <code>progress/width-default</code> 320 · 361 (DEC-243).",
         astryx="Thanh nổi 361 trong khung 393, cùng cách ghi số.",
         tokens=[("field/width-default", "Web 320 · App 100%", "Mặc định trải theo cha trên app"), ("progress/width-default", "Web 320 · App 100%", "Như trên")],
         note="Phụ thuộc sp09: chọn “app rộng đầy” ở sp09 là cùng việc này, chốt một nơi. Đường canh K (đường căn mép cũ của app, DEC-259 đã thay bằng lưới) bên phải 377, 361 (DEC-193) đo từ mép trái khung 393; đọc lại thành khoảng cách từ mép phải (16, 32) thì đúng mọi khung, hình không đổi.",
         pv=PV_FILL,
         opts=[("a", "App trải theo màn trừ lề; 361 chỉ là kết quả trên khung 393", True), ("b", "Giữ 361, chỉ hỗ trợ máy từ 393", False)]),
    dict(id="gr14", grp="Khung và breakpoint", title="Bảy mốc breakpoint, mốc nào là mốc thiết kế?",
         why="Bảy mốc khớp Untitled, không có gì lệch (DEC-038, DEC-259). Vấn đề là <mark>không nói mốc nào đổi bố cục</mark>. Luật hiện có chỉ dùng 3 mốc: 768 sang web và thu menu, 1024 sang 12 cột, 1280 mở menu 240 (DEC-039). 600 được thêm “như Untitled” nhưng lý do của Untitled là thư viện thông báo: “This must match the breakpoint in Sonner”. Biến <code>--bp-*</code> chỉ để tra, media query ghi số trực tiếp vì CSS không cho dùng biến trong media query. 0/26 component đọc. Kéo khung trong xem thử để đi qua từng mốc.",
         untitled="<code>--breakpoint-xxs</code> 320, <code>--breakpoint-xs</code> 600, còn lại mặc định Tailwind v4.",
         ours="<code>--bp-xxs 320 · xs 600 · sm 640 · md 768 · lg 1024 · xl 1280 · 2xl 1536</code>.",
         astryx="<code>DEFAULT_WIDTH_BREAKPOINTS</code> 640 · 768 · 1024 · 1280 · 1536, AppShell đổi MobileNav dưới 768.",
         pv=PV_BP,
         opts=[("a", "Giữ 7 mốc cho code, ghi rõ 3 mốc thiết kế 768, 1024, 1280", True), ("b", "Mở lại DEC-259 mục GR5: bỏ xxs, xs khỏi token, 320 chỉ là máy thử", False), ("c", "Thêm mốc 1440 cho màn lớn", False)]),
]

SPEC = dict(
    slug="grids", short="phần Lưới",
    title="Foundations · Lưới, độ rộng, breakpoint — đúng khung chưa?",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
    lead=(f"Trang này giúp quyết <b>tên độ rộng, lưới từng nền tảng và khung vẽ chuẩn</b>. Số lưới web đã khớp Untitled (DEC-259), chỗ lệch nằm ở <mark>tên width</mark>, <mark>tablet</mark> và <mark>khung app co giãn</mark>. "
          "Có 2/17 token trong nhóm được component dùng nên đổi lúc này rẻ. <mark>Chưa sửa token nào.</mark>"),
    kpis=[(f"{N_OK}/{N_U}", "dòng Untitled giống mình", "ok"), (str(N_DIFF), "khác có lý do", ""), (str(N_GAP), "mình thiếu", "bad"), (str(N_OWN), "chỉ mình có", ""), ("2/17", "token có component dùng", "")],
    tag_kind="spacing",
    screens=dict(
        intro="Lưới đỏ tính theo lề thật. Khung chuẩn: web <b>1280</b>, menu <b>240</b> (DEC-039), app <b>393</b>; chi tiết, biểu mẫu rộng 1040 là vùng sau menu. Đổi khung web, khung app ở thanh trên để xem nội dung còn khớp cột không. Khung 768 ở bộ Hiện tại: lưới ghi 24, biến đọc 32 nên thấy lệch (mục gr08).",
        proposal_css=".tp-f.tp-prop .tp-kpis{gap:var(--grid-gutter)}",
        logo_svg=None, gridov=True, overlay_html=overlay_html),
    sections=[
        dict(title="Bảng đối chiếu từng dòng — Untitled ↔ mình",
             intro=f"Đủ 12 width, 3 container, 3 khung grid, lưới auto và 7 breakpoint: {N_U} dòng của Untitled, cộng {N_OWN} dòng chỉ mình có. Giống {N_OK}, khác có lý do {N_DIFF}, mình thiếu {N_GAP}. Cột grid ghi cột · rãnh · lề. App là chế độ token App.",
             html=kit.rows(["Nhóm", "Untitled", "Số", "Mình", "Số", "Trạng thái", "Ghi chú"], CMP)),
        dict(title="Số cột, rãnh, lề từng nền tảng theo khung",
             intro="Rộng cột tính bằng công thức của ref: (vùng − 2 × lề − rãnh × (cột − 1)) ÷ cột, với số lấy từ <code>design-system/tokens.json</code>.",
             html=COLS_TBL),
        dict(title="Bề rộng màn mẫu so với khung chuẩn của dự án", intro="Khung đang ghi ở mỗi nơi. Hai mục gr11 và gr12 chốt lại.", html=FRAMES_TBL),
        dict(title="Phần Untitled còn thiếu trong ref", intro="Những chỗ dưới đây không có số để so. Trang không đoán, ghi rõ để biết khi nào cần đọc lại Figma của họ.", html=REF_GAP),
        dict(title="Đã chốt, không mở lại", intro="Trang giữ nguyên các dòng dưới. Chỗ mở lại ghi rõ câu “Mở lại DEC-x:” kèm bằng chứng, ở gr00, gr02, gr08, gr13.", html=DECIDED),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", html=PROPOSAL),
    ],
    items=ITEMS,
    final=("Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/grids.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>grid = approved</b> (<code>ds-foundation-status.py set grid approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). "
           "Việc riêng của trang: đổi tên token ở mọi nơi dùng. <code>width/*</code>: <code>design-system/components/base/tooltip.md</code>, <code>design-system/components/application/sidebar-navigation.md</code>, <code>_scripts/ds-foundation-check.py</code>. "
           "<code>layout/screen-inset</code>, <code>layout/content-max-width</code>: <code>design-system/foundations/spacing.md</code>, <code>design-system/foundations/README.md</code>, <code>design-system/architecture.md</code>, <code>_scripts/ds-foundation-page.py</code>, <code>_scripts/ds_foundation_audit.py</code>, <code>_scripts/foundation_review/kit.py</code>. "
           "<code>grid/columns</code>, <code>grid/gutter</code>: <code>_scripts/ds-v2-tokens.py</code>. Rồi dựng lại bản token nhúng trong 14 trang <code>design-system/components/_work/*/page.json</code> bằng <code>_scripts/ds-kit.py</code>."),
    css=CSS, js=JS,
)
