#!/usr/bin/env python3
"""Command menu — vòng 1 Brainstorm (04/11). Chạy: python3 design-system/components/_work/command-menu/build.py && python3 _scripts/ds-component-page.py command-menu
Nguồn: Untitled command-menus (ô tìm lớn, kết quả nhóm, phím tắt, chân gợi ý phím) · Header navigation đã dựng: `_Header search panel`
(Figma 6904:20446, token command-search/*, header-navigation.md mục Tìm tính năng) — look 600 đã duyệt giữ nguyên.
Mọi số qua token foundation (user 04/11). Nhóm C: chỉ web; app dùng màn tìm (cmd_app).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
import blocks as B  # noqa: E402
from blocks import (ALL_CSS, CSS_SCREEN, OPT_CMD, CMD_NESTED, CMD_RECENT, CMD_RES, cmd_app, cmd_menu, m_factory, mcard, rec_of,  # noqa: E402
                    section_header, table, tabs, vg, vg_row, write, ORDERS)

B.ACTIVE.add("command-menu")
OUT = Path(__file__).parent / "page.json"

CMD_LONG = [("Bản ghi", [("truck", "<mark>LVT-2026-04</mark>12 · Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics chi nhánh Cát Lái",
                               "Cát Lái → Khu công nghiệp Sóng Thần, Dĩ An, Bình Dương · container lạnh 40 feet · giao giờ hành chính", "Đang chạy", "Lệnh")]),
            ("Tính năng", [("file", "Xuất báo cáo đối soát cước theo tuyến và theo khách hàng tháng 10/2026", "Báo cáo", "", "Tính năng")])]
NESTED_CTX = "Gán xe · LVT-2026-0412"


def arch(shared):
    if shared:
        return ('<div class="arch"><div class="bx hl"><b>Command menu</b><small>component gốc · Content = Results · Recent · Loading · Empty · Nested</small></div>'
                '<span class="ar">↳ lồng instance</span><div class="ln"><div class="bx">Header navigation<small>nút Tìm · ⌘K</small></div>'
                '<div class="bx">Bảng · thao tác nhanh<small>“Gán xe”, “Đổi lái xe”</small></div></div></div>')
    return ('<div class="arch"><div class="ln"><div class="bx">Header navigation<small>giữ _Header search panel riêng</small></div>'
            '<div class="bx hl"><b>Command menu</b><small>component mới cho thao tác trong màn</small></div></div>'
            '<span class="ar">Hai bộ cùng hình — sửa phải sửa hai nơi</span></div>')


ARCH_CSS = (".arch{display:flex;flex-direction:column;gap:var(--space-md);font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body)}"
            ".arch .bx{border:1px solid var(--color-border-primary);border-radius:var(--radius-md);padding:var(--space-md) var(--space-lg);background:var(--color-bg-primary)}"
            ".arch .bx.hl{border-color:var(--color-fg-primary);box-shadow:inset 0 0 0 1px var(--color-fg-primary)}"
            ".arch .bx b{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body)}"
            ".arch .bx small{display:block;color:var(--color-text-tertiary)}.arch .ln{display:flex;gap:var(--space-md)}.arch .ar{color:var(--color-text-tertiary)}"
            ".cmbox{position:relative;height:var(--width-md);border:1px solid var(--color-border-secondary);border-radius:var(--radius-xl);overflow:hidden}")


def ov(inner, h=None):
    return f'<div class="cm-ov" style="position:static;padding:var(--space-xl);{f"height:{h};" if h else ""}">{inner}</div>'


R = ov(cmd_menu())
decisions = [
 {"id": "D1", "title": "Quan hệ với hộp tìm ⌘K của Header navigation",
  "why": "Header navigation đã dựng `_Header search panel` (Figma 6904:20446, token `command-search/*`). Command menu của Untitled chính là hộp đó. Giữ hai bộ thì lệch hình theo thời gian.",
  "source": "header-navigation.md mục Tìm tính năng (D2 B, D3 C) · DEC-292 luật lồng · Untitled command-menus",
  "options": [{"label": "Nâng thành component dùng chung", "desc": "Command menu là gốc; Header nav lồng instance. Đổi tên `_Header search panel` → `Command menu`.", "rec": True},
              {"label": "Giữ riêng", "desc": "Command menu mới chỉ cho thao tác trong màn."}]},
 {"id": "D2", "title": "Chân hộp",
  "why": "Người dùng mới không biết đi bằng phím. Chân gợi ý phím cao ~36 nhưng dạy cách dùng.",
  "source": "Untitled command-menus footer · header-navigation.md (chân `bg/secondary` `type/caption`)",
  "options": [{"label": "Có gợi ý phím", "desc": "↑ ↓ di chuyển · ↵ mở · Tab đổi phạm vi · Esc đóng.", "rec": True},
              {"label": "Không chân", "desc": "Chỉ gợi ý Esc trong ô nhập."}]},
 {"id": "D3", "title": "Cách xếp kết quả",
  "why": "Kết quả trộn lệnh, xe, lái xe, thao tác. Nhóm theo loại dễ quét; danh sách phẳng xếp theo độ khớp, mục tốt nhất luôn ở đầu.",
  "source": "Untitled command-menus (grouped) · header-navigation.md nhãn nhóm `type/caption-caps`",
  "options": [{"label": "Nhóm theo loại", "desc": "Nhãn nhóm viết hoa, trạng thái bên phải.", "rec": True},
              {"label": "Phẳng + nhãn loại", "desc": "Loại ghi bên phải dòng."}]},
 {"id": "D4", "title": "Lọc phạm vi",
  "why": "Gõ “51C” ra cả xe, lệnh có xe đó, lái xe lái xe đó. Lọc nhanh theo loại giúp thu hẹp; tiền tố gõ nhanh hơn nhưng phải nhớ.",
  "source": "Ý tưởng cộng đồng: Linear / Raycast (tiền tố), Vercel (chip phạm vi)",
  "options": [{"label": "Chip dưới ô tìm", "desc": "Tất cả · Lệnh · Xe · Lái xe · Thao tác; Tab đổi chip.", "rec": True},
              {"label": "Tiền tố gõ", "desc": "# lệnh · @ lái xe · / thao tác — gợi ý ở chân."},
              {"label": "Không lọc", "desc": "Chỉ một danh sách."}]},
 {"id": "D5", "title": "Khung xem trước bên phải",
  "why": "Điều phối hay chỉ cần liếc trạng thái, lái xe, giờ hẹn của lệnh mà không mở. Khung xem trước làm hộp rộng 920, đổi look 600 đã duyệt ở Header nav.",
  "source": "Ý tưởng cộng đồng: Raycast / Superhuman preview · memory: không tự đổi look đã duyệt",
  "options": [{"label": "Có xem trước", "desc": "Rộng `command-search/width` + `width/xxs`; khung `bg/secondary_alt`."},
              {"label": "Không — giữ 600", "desc": "Mở lệnh để xem chi tiết.", "rec": True}]},
 {"id": "D6", "title": "Thao tác nhiều bước (Gán xe → chọn xe)",
  "why": "Thao tác như “Gán xe cho lệnh…” cần bước 2 chọn xe ngay trong hộp. Phải cho thấy đang ở bước nào và quay lại được.",
  "source": "Ý tưởng cộng đồng: Raycast / Linear (chip ngữ cảnh), cmdk pages",
  "options": [{"label": "Chip ngữ cảnh trong ô", "desc": "Chip “Gán xe · LVT-…” trước chữ gõ; Backspace xoá chip = quay lại.", "rec": True},
              {"label": "Dòng tiêu đề có ←", "desc": "Hàng trên ô: ← + tên thao tác + “Bước 2/2”."}]},
 {"id": "D7", "title": "Đang tải",
  "why": "Tìm toàn cục gọi API (chưa có trong SRS). Mỗi lần gõ mà kết quả nháy trắng thì khó đọc.",
  "source": "Untitled loading indicator · motion.md 10.3",
  "options": [{"label": "Khung xương", "desc": "5 dòng xương thay kết quả."},
              {"label": "Giữ kết quả cũ mờ + vòng quay", "desc": "Vòng quay 16 trong ô nhập, danh sách cũ mờ 50%.", "rec": True}]},
 {"id": "D8", "title": "Trên app",
  "why": "App không có phím tắt; tìm là màn riêng. Toàn màn có bàn phím chiếm nửa dưới; bottom sheet giữ ngữ cảnh nhưng thấp.",
  "source": "DEC-279 nhóm C · design.md M2 ô tìm luôn hiện",
  "options": [{"label": "Màn tìm toàn màn", "desc": "Ô tìm + Huỷ, chip phạm vi, kết quả dòng 40.", "rec": True},
              {"label": "Bottom sheet cao", "desc": "Sheet từ `space/7xl`, nền mờ phía trên."}]},
]
AT = {'D1': ('list-web', '.cmd', 'recent', 'hộp tìm ⌘K'), 'D2': ('list-web', '.cm-f', 'cmd', 'chân hộp'), 'D3': ('list-web', '.cm-b', 'cmd', 'danh sách kết quả'), 'D4': ('list-web', '.cm-sc, .cm-f', 'cmd', 'dưới ô tìm / chân hộp'), 'D5': ('list-web', '.cmd', 'cmd', 'cạnh phải hộp'), 'D6': ('nested-web', '.cm-in, .cm-nh', None, 'ô tìm bước 2'), 'D7': ('list-web', '.cm-in', 'loading', 'ô tìm + danh sách'), 'D8': ('search-app', '.cma', None, 'màn tìm app')}
for d in decisions:
    sc, sel, st, note = AT[d['id']]
    d["at"] = {"screen": sc, "sel": sel, "note": note, **({"state": st} if st else {})}
REC = rec_of(decisions)
m = m_factory(REC)
APPBOX = f'<div class="cmbox">{cmd_app()}</div>'
PV = {"D1": (None, 440, "web"), "D2": (R, 660, "web"), "D3": (R, 660, "web"), "D4": (R, 660, "web"), "D5": (R, 980, "web"),
      "D6": (ov(cmd_menu("51C", CMD_NESTED, ctx=NESTED_CTX)), 660, "web"), "D7": (ov(cmd_menu(mode="loading")), 660, "web"), "D8": (APPBOX, 360, "mobile")}
UNT = {"D1": "a", "D2": "a", "D3": "a", "D4": "c", "D5": "b", "D6": "a", "D7": "b", "D8": "a"}
AST = {"D1": "b", "D2": "a", "D3": "a", "D4": "c", "D5": "b", "D6": "b", "D7": "b", "D8": "a"}
NOTE = {k: "Astryx không có Command menu — cột này là hộp tìm ⌘K đã duyệt ở Header nav" for k in UNT}
for d in decisions:
    h, w, plat = PV[d["id"]]
    for k, o in enumerate(d["options"]):
        o["preview"] = m({d["id"]: chr(97 + k)}, h if h else arch(k == 0), w, plat)
    d["untitled"] = m({d["id"]: UNT[d["id"]]}, h if h else arch(True), w, plat)
    d["astryx"] = m({d["id"]: AST[d["id"]]}, h if h else arch(False), w, plat)
    d["astryxNote"] = NOTE[d["id"]]
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC}, {"id": "untitled", "label": "Untitled UI", "pick": UNT}, {"id": "astryx", "label": "Astryx hiện tại", "pick": AST}]

# ---------- màn ----------
LAYERS = [("recent", cmd_menu("", CMD_RECENT, "recent")), ("cmd", cmd_menu()), ("loading", cmd_menu(mode="loading")),
          ("nores", cmd_menu("bảo hiểm", mode="empty")), ("nested", cmd_menu("51C", CMD_NESTED, ctx=NESTED_CTX)), ("long", cmd_menu(groups=CMD_LONG))]
S_LIST = ('<div class="pad" style="min-height:760px">'
          + section_header("Lệnh trong tuần", "Tuần 45 · 128 lệnh", [("Tìm nhanh ⌘K", "search", "sec", "open"), ("Tạo lệnh", "plus", "pri")], tabs([("Tất cả", 128), ("Đang chạy", 12), ("Chờ xe", 5), ("Trễ hẹn", 3)]))
          + table(hide="")
          + "".join(f'<div class="cm-ov" data-show="state:{st}">{h}</div>' for st, h in LAYERS) + "</div>")

S_DISPATCH = ('<div class="pad" style="min-height:760px"><div class="grid2">'
              + "".join(f'<div class="cc" style="padding:var(--space-2xl)">{mcard(a, c, f"{b} · {d}", s)}</div>' for a, b, c, d, s in ORDERS[:4])
              + '</div><div class="cm-ov">' + cmd_menu("51C", CMD_NESTED, ctx=NESTED_CTX) + "</div></div>")

APP_LAYERS = [("recent", cmd_app("", CMD_RECENT)), ("nores", cmd_app("51C-999", mode="empty")), ("long", cmd_app(groups=CMD_LONG))]
S_APP = ('<div class="mpad" style="min-height:640px">'
         + '<div data-hide="recent nores long">' + cmd_app() + "</div>"
         + "".join(f'<div data-show="state:{st}">{h}</div>' for st, h in APP_LAYERS) + "</div>")


def var_rows(plat):
    if plat == "mobile":
        return [vg_row("Bottom sheet tìm (D8 B) · Results", [("Đang gõ “lệnh”", f'<div class="cmbox">{cmd_app()}</div>')], 1, "sheet từ space/7xl, nền mờ phía trên"),
                vg_row("Recent — chưa gõ", [("Dùng gần đây", f'<div class="cmbox">{cmd_app("", CMD_RECENT)}</div>')], 1, ""),
                vg_row("Empty", [("Không thấy", f'<div class="cmbox">{cmd_app("51C-999", mode="empty")}</div>')], 1, "")]
    return [
        vg_row("Content", [("Results", ov(cmd_menu())), ("Recent — chưa gõ", ov(cmd_menu("", CMD_RECENT, "recent"))),
                           ("Loading — khung xương (D7 A)", ov(cmd_menu(mode="loading"))), ("Empty", ov(cmd_menu("bảo hiểm", mode="empty"))),
                           ("Nested — bước 2, chip ngữ cảnh trong ô (D6 A)", ov(cmd_menu("51C", CMD_NESTED, ctx=NESTED_CTX))), ("Chữ dài", ov(cmd_menu(groups=CMD_LONG)))], 2, "D3 · D6 · D7"),
        vg_row("Dòng kết quả", [("Bản ghi + trạng thái", ov(cmd_menu("0412", [("Bản ghi", CMD_RES[2][1][:1])]))),
                                ("Người (avatar)", ov(cmd_menu("Bình", [("Bản ghi", [(("av", 0), "Trần Văn <mark>Bình</mark>", "Lái xe · 0903 xxx 128", "Đang chạy", "Bản ghi")])]))),
                                ("Hành động + phím tắt", ov(cmd_menu("tạo", [("Hành động", CMD_RES[1][1][:1])])))], 3, "dòng: thường · rê · đang chọn (nền bg/selected + vạch trái focus/ring)"),
        vg_row("Phạm vi (D4 A)", [("Chip “Bản ghi” đang chọn", ov(cmd_menu("51C", [("Bản ghi", CMD_NESTED[0][1])], scope=3)))], 1, "D4"),
    ]


def variants(plat):
    return vg(var_rows(plat))


screens = [
 {"id": "list-web", "name": "Danh sách lệnh + ⌘K", "device": "web", "width": 1280, "title": "Lệnh vận tải", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Bấm “Tìm nhanh ⌘K” → Recent; bấm ô tìm → kết quả; bấm “Gán xe cho lệnh…” → bước 2. Đang tải / Không thấy / Chữ dài ở Bảng chọn.", "html": S_LIST},
 {"id": "nested-web", "name": "Gán xe nhanh — bước 2", "device": "web", "width": 1280, "title": "Điều phối", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Thao tác nhiều bước (D6) mở sẵn.", "html": S_DISPATCH},
 {"id": "search-app", "name": "Tìm trên app", "device": "mobile", "title": "Tìm", "nav": "Lệnh", "tabs": False, "note": "D8 toàn màn / bottom sheet. Recent / Không thấy / Chữ dài ở Bảng chọn.", "html": S_APP},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none", "note": "6 Content, 3 kiểu dòng, phạm vi.", "html": variants("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Màn tìm app.", "html": variants("mobile")},
]

PICK = {**REC, "D1": "b", "D6": "a", "D7": "a", "D8": "b"}  # user chốt 04/11 07:27; D6 B bỏ theo góp ý cmw1trb3w
PA = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())
preview = {
 "version": 1, "pick": PICK,
 "changes": "Bản 04/11 theo tổ hợp anh chốt: Command menu là component RIÊNG (D1 B) nhưng cùng giao diện hộp tìm ⌘K đã duyệt ở Header nav; có chân gợi ý phím, "
            "nhóm theo loại, chip phạm vi, không khung xem trước; nhiều bước = CHIP NGỮ CẢNH trong ô (D6 A — bỏ dòng tiêu đề ← theo góp ý); đang tải = KHUNG XƯƠNG (D7 A); app = BOTTOM SHEET cao (D8 B).",
 "blocks": [
  {"title": "Web", "platform": "web", "note": "6 Content (Results, Recent, Loading khung xương, Empty, Nested có ←, chữ dài) · 3 kiểu dòng · chip phạm vi",
   "html": f'<div class="pv pvp" {PA} data-platform="web" data-state="x">{variants("web")}</div>'},
  {"title": "Mobile (app)", "platform": "mobile", "note": "Bottom sheet cao: nền mờ, tay nắm, ô tìm + Huỷ, chip phạm vi, kết quả dòng 40",
   "frames": [f'<div class="pv pvp" {PA} data-platform="mobile" data-state="x">{vg([r])}</div>' for r in var_rows("mobile")]},
 ],
}
VALUES = [
 # Hộp — theo _Header search panel đã duyệt (header-navigation.md › Cấu tạo)
 {"part": "Hộp", "prop": "width", "value": 600, "platform": "Web", "sel": ".cmd"},
 {"part": "Hộp", "prop": "radius", "value": 20, "platform": "Web", "sel": ".cmd", "cssProp": "border-radius"},
 {"part": "Hộp", "prop": "top", "value": 96, "platform": "Web", "sel": ".cm-ov", "cssProp": "padding-top"},
 {"part": "Hộp · viền", "prop": "border-width", "value": 1, "role": "decorative", "platform": "Web", "sel": ".cmd", "cssProp": "box-shadow", "tpl": "var(--shadow-xl),0 0 0 $ var(--shadow-xl-border)"},
 {"part": "Con trỏ", "prop": "margin-left", "value": 1, "role": "decorative", "sel": ".caret"},
 {"part": "Ô nhập", "prop": "height", "value": 52, "platform": "Web", "sel": ".cm-in"},
 {"part": "Ô nhập", "prop": "padding-x", "value": 16, "platform": "Web", "sel": ".cm-in", "cssProp": "padding", "tpl": "0 $"},
 {"part": "Ô nhập · chữ", "prop": "font-size", "value": 18, "platform": "Web", "sel": ".cm-q,.cm-ph", "cssProp": "font", "tpl": "400 $/var(--type-title-3-line-height) var(--font-body)"},
 {"part": "Ô nhập · chữ", "prop": "color", "role": "text", "value": "#171717", "on": "#FFFFFF", "sel": ".cm-q,.cm-ph"},
 {"part": "Ô nhập · gợi ý", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "sel": ".cm-ph"},
 {"part": "Ô nhập · vạch dưới", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".cm-in", "cssProp": "border-bottom", "tpl": "$ solid var(--color-border-secondary)"},
 {"part": "Con trỏ", "prop": "width", "value": 1, "role": "decorative", "sel": ".caret"},
 {"part": "Nhãn nhóm", "prop": "font-size", "value": 12, "sel": ".cm-g", "cssProp": "font", "tpl": "500 $/var(--type-caption-line-height) var(--font-body)"},
 {"part": "Nhãn nhóm", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "sel": ".cm-g"},
 {"part": "Dòng", "prop": "height", "value": 40, "platform": "Web", "sel": ".cm-i", "cssProp": "min-height", "interactive": True, "hitArea": 40},
 {"part": "Dòng", "prop": "padding-x", "value": 16, "platform": "Web", "sel": ".cm-i", "cssProp": "padding", "tpl": "var(--space-xs) $"},
 {"part": "Dòng", "prop": "gap", "value": 8, "sel": ".cm-i"},
 {"part": "Dòng đang chọn", "prop": "color", "role": "fill", "value": "#F5F5F5", "on": "#FFFFFF", "state": "Selected", "sel": ".cm-i.on", "cssProp": "background"},
 {"part": "Dòng đang chọn · vạch", "prop": "color", "role": "border", "value": "#262626", "on": "#F5F5F5", "state": "Selected", "noOverride": "vạch trái vẽ bằng box-shadow inset focus/width", "at": ".cm-i.on"},
 {"part": "Ô icon", "prop": "size", "value": 28, "sel": ".cm-ic", "cssProp": ["width", "height"]},
 {"part": "Ô icon", "prop": "radius", "value": 8, "sel": ".cm-ic", "cssProp": "border-radius"},
 {"part": "Ô icon", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".cm-ic", "cssProp": "box-shadow", "tpl": "inset 0 0 0 $ var(--color-border-secondary)"},
 {"part": "Ô icon · nét icon", "prop": "stroke-width", "value": 2, "sel": ".cm-ic svg", "noOverride": "nét 2 trên khung 24 — mảnh hơn DEC-329 (2.25 cho icon ≤ 16), user chốt qua góp ý 04/11"},
 {"part": "Ô icon", "prop": "color", "role": "icon", "value": "#404040", "on": "#FFFFFF", "sel": ".cm-ic"},
 {"part": "Chữ chính", "prop": "font-size", "value": 14, "sel": ".cm-tx b", "cssProp": "font", "tpl": "500 $/var(--type-label-line-height) var(--font-body)"},
 {"part": "Chữ phụ", "prop": "font-size", "value": 12, "sel": ".cm-tx small", "cssProp": "font", "tpl": "400 $/var(--type-caption-line-height) var(--font-body)"},
 {"part": "Chữ phụ", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "sel": ".cm-tx small"},
 {"part": "Chữ khớp", "prop": "color", "role": "fill", "value": "#FEF0C7", "on": "#FFFFFF", "sel": ".cm-tx mark", "cssProp": "background", "noOverride": "nền warning/secondary — khai để đo", "at": ".cm-tx mark"},
 {"part": "Chân hộp", "prop": "padding-y", "value": 8, "sel": ".cm-f", "cssProp": "padding", "tpl": "$ var(--space-xl)"},
 {"part": "Chân hộp", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".cm-f", "cssProp": "border-top", "tpl": "$ solid var(--color-border-secondary)"},
 {"part": "Chân hộp · chữ", "prop": "color", "role": "text", "value": "#737373", "on": "#FAFAFA", "sel": ".cm-f"},
 {"part": "Chip phạm vi", "prop": "height", "value": 28, "platform": "Web", "sel": ".cm-chip", "interactive": True, "hitArea": 28, "control": True},
 {"part": "Hàng chip phạm vi", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".cm-sc", "cssProp": "border-bottom", "tpl": "$ solid var(--color-border-secondary)"},
 {"part": "Chip ngữ cảnh bước 2", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".cm-ctx", "cssProp": "box-shadow", "tpl": "inset 0 0 0 $ var(--color-border-primary)"},
 {"part": "Chip ngữ cảnh bước 2", "prop": "height", "value": 28, "sel": ".cm-ctx"},
 {"part": "Khung xương", "prop": "height", "value": 48, "sel": ".cm-skr", "cssProp": "min-height"},
 {"part": "Không có kết quả · icon", "prop": "size", "value": 48, "sel": ".cm-ei", "cssProp": ["width", "height"]},
 {"part": "Không có kết quả", "prop": "padding-y", "value": 24, "sel": ".cm-em", "cssProp": "padding", "tpl": "$ var(--space-xl)"},
 # App — bottom sheet
 {"part": "Sheet app", "prop": "top", "value": 64, "platform": "Mobile", "sel": ".pv[data-platform=mobile][data-D8=b] .cma"},
 {"part": "Sheet app · tay nắm", "prop": "width", "value": 32, "platform": "Mobile", "sel": ".pv[data-platform=mobile][data-D8=b] .cma-hd"},
 {"part": "Ô tìm app", "prop": "height", "value": 42, "platform": "Mobile", "sel": ".cma-in", "interactive": True, "hitArea": 44, "control": True},
 {"part": "Ô icon app", "prop": "size", "value": 40, "platform": "Mobile", "sel": ".cma-i .cm-ic", "cssProp": ["width", "height"]},
 {"part": "Ô icon app · icon", "prop": "size", "value": 20, "platform": "Mobile", "noOverride": "icon/size/lg 20 — không thu về 16 như icon app thường (góp ý 04/11)", "at": ".cma-i .cm-ic svg"},
 {"part": "Dòng app", "prop": "height", "value": 52, "platform": "Mobile", "sel": ".cma-i", "cssProp": "min-height", "interactive": True, "hitArea": 52},
 {"part": "Chip app", "prop": "border-width", "value": 1, "role": "decorative", "platform": "Mobile", "sel": ".cma .cm-chip", "cssProp": "border", "tpl": "$ solid var(--color-border-primary)"},
 {"part": "Hàng chip app", "prop": "border-width", "value": 1, "role": "decorative", "platform": "Mobile", "sel": ".cma .cm-sc", "cssProp": "border-bottom", "tpl": "$ solid var(--color-border-secondary)"},
]

page = {
 "component": "Command menu", "slug": "command-menu", "title": "Command menu Review",
 "subtitle": "Application component · vòng 2 Preview (04/11) — component riêng, cùng giao diện hộp tìm ⌘K đã duyệt ở Header navigation; màn demo khoá theo tổ hợp, bảng biến thể Web/Mobile.",
 "round": "preview", "preview": preview, "values": VALUES, "tokenFamilies": ["command-search", "control", "featured-icon"],
 "refs": {
  "untitled": {"summary": "Hộp giữa màn, ô tìm lớn, kết quả <mark>nhóm theo loại</mark> có icon, phím tắt bên phải, <mark>chân gợi ý phím</mark>; trạng thái rỗng có icon.",
               "source": "untitledui.com/components/command-menus"},
  "astryx": {"summary": "Astryx không có Command menu. Hộp tìm ⌘K mới dựng ở Header navigation: rộng 600, cách đỉnh 96, bo overlay 20, ô nhập 52 chữ title-3, nhóm caption-caps, dòng 40, chọn = bg/selected + vạch trái 2.",
             "source": "design-system/components/application/header-navigation.md · Figma 6904:20446"},
  "usage": ["Header navigation: Tìm tính năng ⌘K (lệnh, xe, lái xe, tính năng)", "Điều phối: thao tác nhanh “Gán xe”, “Đổi lái xe” không rời màn",
            "App lái xe: màn tìm lệnh, địa điểm"],
  "platform": "Nhóm C: chỉ web. App dùng màn tìm riêng (D8). Tìm toàn cục cần API — chưa có trong SRS (header-navigation.md D3 C)."},
 "css": B.CSS_CMD + OPT_CMD, "cssScreen": B.CSS_BASE + B.CSS_TABS + B.CSS_CH + B.CSS_SH + B.CSS_ES + ARCH_CSS + CSS_SCREEN,
 "states": [{"key": "default", "label": "Đóng"}, {"key": "recent", "label": "Mở · chưa gõ"}, {"key": "cmd", "label": "Có kết quả"}, {"key": "loading", "label": "Đang tải"},
            {"key": "nores", "label": "Không thấy"}, {"key": "nested", "label": "Bước 2 · Gán xe"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": [], "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": "[data-js=open]", "state": "recent"}, {"sel": ".m-recent .cm-in", "state": "cmd"}, {"sel": "[data-js=nest]", "state": "nested"},
           {"sel": ".cm-i:not([data-js])", "close": True}],
 "protoLayers": [".cmd"],
 "protoHint": "bấm Tìm nhanh ⌘K → bấm ô tìm → bấm “Gán xe cho lệnh…”; Esc hoặc bấm ra ngoài để đóng",
}
write(OUT, page, decisions)
