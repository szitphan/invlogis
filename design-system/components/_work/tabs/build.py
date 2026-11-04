#!/usr/bin/env python3
"""Tabs — vòng 1 Brainstorm (04/11). Chạy: python3 design-system/components/_work/tabs/build.py && python3 _scripts/ds-component-page.py tabs
Nguồn: Untitled tabs.tsx (5 kiểu ngang, 2 kiểu dọc, sm · md, icon, badge, fullWidth; mobile → NativeSelect) · Astryx Tabs gạch chân ·
DEC-096 tab chip trạng thái app · token tab/* (tab-padding-x, tab-gap). Mọi số qua token foundation (user 04/11).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
import blocks as B  # noqa: E402
from blocks import (ALL_CSS, CSS_SCREEN, OPT_TABS, bt, card, card_header, empty, ibt, lt, m_factory, mcard, pill, rec_of,  # noqa: E402
                    section_header, table, table_loading, tabs, vg, vg_row, write, ORDERS, kv, doc_list)

B.ACTIVE.add("tabs")
OUT = Path(__file__).parent / "page.json"

STATUS = [("Tất cả", 128, "list"), ("Đang chạy", 12, "truck"), ("Chờ xe", 5, "clock"), ("Trễ hẹn", 3, "alert"), ("Hoàn tất", None, "checkc")]
STATUS0 = [("Tất cả", 128, "list"), ("Đang chạy", 12, "truck"), ("Chờ xe", 5, "clock"), ("Trễ hẹn", 0, "alert"), ("Hoàn tất", None, "checkc")]
DETAIL = [("Tổng quan", None, "grid"), ("Chứng từ", 4, "file"), ("Chi phí", None, "fuel"), ("Lịch sử", 23, "clock")]
VIEW = [("Bảng", None, "list"), ("Bản đồ", None, "map"), ("Lịch", None, "calendar")]
MANY = [("Tất cả", 128), ("Nháp", 4), ("Chờ duyệt", 7), ("Chờ xe", 5), ("Đang chạy", 12), ("Trễ hẹn", 3), ("Chờ chứng từ", 9), ("Đối soát", 6), ("Hoàn tất", 86), ("Đã huỷ", 2)]
SETTINGS = [("Thông tin công ty", None, "shield"), ("Người dùng", 14, "users"), ("Tham số vận hành", None, "layers"), ("Thông báo", None, "bell"), ("Tích hợp", 3, "grid")]
APP = [("Tất cả", 8, "list"), ("Đang chạy", 2, "truck"), ("Chờ nhận", 1, "clock"), ("Hoàn tất", 5, "checkc")]

decisions = [
 {"id": "D1", "title": "Kiểu chính trên web",
  "why": "Tabs chia nội dung trong một màn (chi tiết lệnh) và lọc danh sách theo trạng thái. Cần một kiểu chính dùng khắp nơi; kiểu khung xám nổi hợp ít lựa chọn hơn.",
  "source": "tabs.tsx: underline · button-gray · button-border · Astryx Tabs gạch chân · DEC-260 F3 than chì (gạch chọn `color/fg/primary`)",
  "options": [
   {"label": "Underline", "desc": "Gạch 2 dưới tab chọn, nền 1 `border/secondary` cả hàng; chữ `type/label`.", "rec": True},
   {"label": "Button gray", "desc": "Tab chọn nền `bg/primary_hover`, cao `control/height/ml` 36, bo `radius/control`."},
   {"label": "Button border", "desc": "Khay `bg/secondary_alt`, tab chọn nền trắng + `shadow/sm` — kiểu segmented."}]},
 {"id": "D2", "title": "Kiểu phụ — chuyển chế độ xem (Bảng · Bản đồ · Lịch)",
  "why": "Cùng một màn hay có thêm bộ chuyển nhỏ (xem bảng / bản đồ, ngày / tuần). Nếu dùng cùng kiểu với tab chính thì hai hàng tab chồng nhau khó phân biệt.",
  "source": "tabs.tsx button-border · button-minimal",
  "options": [
   {"label": "Button border (segmented)", "desc": "Khay xám viền, tab chọn nổi trắng.", "rec": True},
   {"label": "Button minimal", "desc": "Khay xám liền, tab chọn viền `border/primary` + `shadow/xs`."},
   {"label": "Không có kiểu phụ", "desc": "Dùng Underline cỡ SM cho cả việc này."}]},
 {"id": "D3", "title": "Số đếm trên tab",
  "why": "Tab trạng thái lệnh luôn có số (12 đang chạy, 3 trễ hẹn). Viên số rõ nhưng thêm 5–10 khối xám trên một hàng.",
  "source": "tabs.tsx Badge pill · Badge Pill Color SM (`chip/height-sm` 22, chữ `chip/count-*` 12/16 không đậm, DEC-303)",
  "options": [
   {"label": "Viên số xám", "desc": "Tab chọn viên `bg/selected`, chữ đậm hơn.", "rec": True},
   {"label": "Số chữ thường", "desc": "Số `text/tertiary` cạnh nhãn, không nền."}]},
 {"id": "D4", "title": "Icon trước nhãn",
  "why": "Icon giúp nhận ra tab nhanh trên màn chi tiết, nhưng 5 tab trạng thái có icon thành rối, và icon trạng thái dễ lẫn với Badge.",
  "source": "tabs.tsx icon (`*:data-icon:size-4`) · icon.md cỡ `icon/size/md` 16, màu `fg/quaternary`",
  "options": [
   {"label": "Không icon", "desc": "Chỉ nhãn (+ số). Icon chỉ bật riêng khi màn cần.", "rec": True},
   {"label": "Có icon", "desc": "Icon 16 trước nhãn ở mọi tab."}]},
 {"id": "D5", "title": "Cỡ",
  "why": "Untitled có sm (14) và md (16). Màn vận hành đặc chữ 14; tab 16 chỉ hợp màn ít nội dung (cài đặt, trang giới thiệu).",
  "source": "tabs.tsx sizes · typography.md `type/label` 14 · `type/body-lg-medium` 16",
  "options": [
   {"label": "SM + MD", "desc": "SM `type/label` cho màn vận hành, MD `type/body-lg-medium` cho màn rộng.", "rec": True},
   {"label": "Chỉ SM", "desc": "Một cỡ, ít biến thể."}]},
 {"id": "D6", "title": "Tab tràn ngang (10 trạng thái đối soát)",
  "why": "Danh sách đối soát có 10 trạng thái, màn 1280 không chứa hết. Cuộn trơn thì người dùng không biết còn tab ẩn.",
  "source": "tabs.tsx (cuộn, không chỉ báo) · ý tưởng cộng đồng: GitHub / Linear gom “More”",
  "options": [
   {"label": "Cuộn + mép mờ + nút ›", "desc": "Mép phải mờ `space/6xl`, nút Utility SM cuộn tiếp.", "rec": True},
   {"label": "Gom vào “Thêm ▾”", "desc": "Hiện 5 tab đầu, còn lại trong menu; số đếm tổng trên nút."},
   {"label": "Cuộn trơn (Untitled)", "desc": "Không chỉ báo."}]},
 {"id": "D7", "title": "Trên app",
  "why": "Untitled đổi Tabs → Select trên mobile. Lab mobile đã duyệt (DEC-096) dùng chip có đếm cuộn ngang. Lái xe cần thấy ngay số lệnh từng trạng thái.",
  "source": "DEC-096 · DEC-279 nhóm B · tabs.demo.tsx NativeSelect · touch-focus `touch/min` 44",
  "options": [
   {"label": "Underline cuộn ngang", "desc": "Cùng hình web."},
   {"label": "Chip cuộn ngang (Lab)", "desc": "Cao `control/height/sm` 36 (vùng chạm 44), chọn nền `accent/solid`.", "rec": True},
   {"label": "Ô Select (Untitled)", "desc": "Một ô chọn mở sheet; không thấy số các tab khác."}]},
 {"id": "D8", "title": "Tabs dọc (màn cài đặt)",
  "why": "Cài đặt có 5–8 nhóm, đặt dọc bên trái. Cần một kiểu dọc khác Sidebar để không lẫn với điều hướng chính.",
  "source": "tabs.tsx vertical: line · button-gray",
  "options": [
   {"label": "Line", "desc": "Vạch 2 bên trái tab chọn.", "rec": True},
   {"label": "Button gray", "desc": "Nền `bg/primary_hover`, cao 36 — giống mục Sidebar."}]},
]
AT = {'D1': ('list-web', '.tbw.k-line', None, 'hàng tab trạng thái'), 'D2': ('detail-web', '.tbw.k-seg', None, 'Bảng · Bản đồ trong thẻ Lộ trình'), 'D3': ('list-web', '.tbw.k-line .cntb', None, 'số trên tab'), 'D4': ('detail-web', '.tbw.k-line', None, 'Tổng quan · Chứng từ · Chi phí · Lịch sử'), 'D5': ('variants-web', '.tbs.line.t-md', None, 'hàng “Underline · cỡ”'), 'D6': ('many-web', '.tbw.ovf', None, '10 tab đối soát — bấm › hoặc Thêm để thử'), 'D7': ('list-app', '.tbw.k-line', None, 'tab trạng thái app'), 'D8': ('settings-web', '.tbw.k-vert', None, 'cột trái')}
for d in decisions:
    sc, sel, st, note = AT[d['id']]
    d["at"] = {"screen": sc, "sel": sel, "note": note, **({"state": st} if st else {})}
REC = rec_of(decisions)
m = m_factory(REC)
PV = {"D1": (tabs(STATUS[:4]), 560, "web"), "D2": (tabs(VIEW, kind="seg"), 420, "web"), "D3": (tabs(STATUS[:4]), 560, "web"),
      "D4": (tabs(DETAIL), 560, "web"), "D5": (tabs(STATUS[:4], size="md") + '<div style="height:12px"></div>' + tabs(STATUS[:4]), 600, "web"),
      "D6": (tabs(MANY, ovf=5), 720, "web"), "D7": (tabs(APP), 360, "mobile"), "D8": (tabs(SETTINGS, kind="vert"), 300, "web")}
UNT = {"D1": "a", "D2": "a", "D3": "a", "D4": "b", "D5": "a", "D6": "c", "D7": "c", "D8": "a"}
AST = {"D1": "a", "D2": "c", "D3": "b", "D4": "a", "D5": "b", "D6": "c", "D7": "b", "D8": "b"}
for d in decisions:
    h, w, plat = PV[d["id"]]
    for k, o in enumerate(d["options"]):
        o["preview"] = m({d["id"]: chr(97 + k)}, h, w, plat)
    d["untitled"] = m({d["id"]: UNT[d["id"]]}, h, w, plat)
    d["astryx"] = m({d["id"]: AST[d["id"]]}, h, w, plat)
    d["astryxNote"] = {"D1": "Tabs gạch chân accent", "D2": "Không có kiểu phụ", "D3": "Số trong ngoặc", "D4": "Không icon", "D5": "Một cỡ 14",
                       "D6": "Cuộn trơn", "D7": "Tab chip (DEC-096)", "D8": "Nav trái nền xám (P5)"}[d["id"]]

presets = [{"id": "rec", "label": "Đề xuất", "pick": REC}, {"id": "untitled", "label": "Untitled UI", "pick": UNT}, {"id": "astryx", "label": "Astryx hiện tại", "pick": AST}]

# ---------- màn ----------
EMPTY_TAB = ('<div class="tw" data-show="state:nores">' + empty("Không có lệnh trễ hẹn", "Tuần 45 chưa có lệnh nào trễ giờ hẹn. Đổi tuần hoặc xem tab khác.",
                                                         "search", "md", None, ("Xem tất cả lệnh", None), "search", "card") + "</div>")
TAB_LONG = [("Tất cả", 128, "list"), ("Đang chạy", 12, "truck"), (lt("Chờ xe", "Chờ xe đầu kéo và mooc phù hợp"), 5, "clock"), ("Trễ hẹn", 3, "alert"), ("Hoàn tất", None, "checkc")]
S_LIST = ('<div class="pad">'
          + section_header("Lệnh trong tuần", "Tuần 45 · cập nhật 08:45", [("Xuất file", "dl"), ("Tạo lệnh", "plus", "pri")],
                           f'<div data-hide="nores">{tabs(TAB_LONG, 0, js=[None, None, None, "late", None])}</div>'
                           f'<div data-show="state:nores">{tabs(STATUS0, 3, js=["all"])}</div>')
          + table() + table_loading() + EMPTY_TAB + "</div>")

ROUTE = '<div class="bars">' + "".join(f'<i style="height:{h}%"{" class=on" if k == 4 else ""}></i>' for k, h in enumerate((40, 62, 55, 80, 92, 70, 48))) + "</div>"
S_DETAIL = ('<div class="pad">' + tabs(DETAIL, 0, size="md", icons=False)
            + '<div class="grid2">'
            + card(card_header("Thông tin chuyến", pill("Đang chạy"), "Cập nhật 08:45"),
                   kv([("Khách hàng", "Delta Logistics"), ("Tuyến", "Cát Lái → Sóng Thần"), ("Container", '<span class="code">TGHU 812345-6 · 40 feet</span>'), ("Giờ hẹn", "14:00 · 04/11/2026")]))
            + card(card_header("Lộ trình", "", "Cập nhật vị trí 2 phút trước", acts=tabs(VIEW[:2], kind="seg")),
                   '<div data-hide="loading">' + kv([("Đã chạy", "18,4 km / 31 km"), ("Dự kiến tới", "13:40"), ("Dừng", "1 lần · trạm cân Linh Xuân")]) + "</div>")
            + card(card_header("Sản lượng chuyến theo ngày", "", "7 ngày gần nhất", acts=tabs([("Ngày", None), ("Tuần", None), ("Tháng", None)], kind="seg")), ROUTE)
            + card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "4 chứng từ", primary=("Tải lên", "dl")), doc_list())
            + "</div></div>")

S_MANY = ('<div class="pad">' + section_header("Đối soát cước", "Tháng 10/2026 · 270 chuyến", [("Xuất bảng kê", "dl"), ("Chốt kỳ", "checkc", "pri")],
                                               f'<div data-hide="picked">{tabs(MANY, 0, ovf=5)}</div>'
                                               f'<div data-show="state:picked">{tabs(MANY[:4] + [MANY[5], MANY[4]] + MANY[6:], 4, ovf=5)}</div>')
          + table([(f"DS-2610-{k:03d}", c, r, d, s) for k, (a, c, r, d, s) in enumerate(ORDERS, 41)]) + "</div>")

FORM = ('<div class="fsec-b">' + "".join(f'<label class="fld"><span>{a}</span><span class="inp">{b}</span></label>' for a, b in
                                         (("Giờ chốt sổ hằng ngày", "17:30"), ("Ngưỡng tạm ứng", "P-nguong-tam-ung · 5.000.000 ₫"), ("Thời gian chờ tối đa tại cảng", "4 giờ"))) + "</div>")
S_SETTINGS = ('<div class="pad"><div class="split"><div>' + tabs(SETTINGS, 2, kind="vert", icons=True, aria="Nhóm cài đặt") + "</div><div>"
              + section_header("Tham số vận hành", "Áp cho mọi chi nhánh của Delta Logistics", [("Khôi phục mặc định", "refresh"), ("Lưu", None, "pri")])
              + '<div style="height:var(--space-3xl)"></div>' + FORM + "</div></div></div>")

S_APP = ('<div class="mpad">'
         + f'<div data-hide="nores">{tabs(APP, 0, js=[None, None, "late", None])}</div>'
         + f'<div data-show="state:nores">{tabs([("Tất cả", 8), ("Đang chạy", 2), ("Chờ nhận", 0), ("Hoàn tất", 5)], 2, js=["all"])}</div>'
         + '<div data-hide="nores loading" style="display:flex;flex-direction:column;gap:var(--layout-list-gap)">'
         + "".join(mcard(a, c, f"{b} · {d}", s) for a, b, c, d, s in ORDERS[:4]) + "</div>"
         + '<div data-show="state:loading" style="display:flex;flex-direction:column;gap:var(--layout-list-gap)">' + "".join('<div class="mcard"><span class="sk" style="width:50%"></span><span class="sk xs" style="width:80%"></span></div>' for _ in range(3)) + "</div>"
         + '<div data-show="state:nores">' + empty("Không có lệnh chờ nhận", "Bạn đã nhận hết lệnh được giao.", "inbox", "md", None, ("Xem tất cả", None), "search") + "</div></div>")
S_APP_DETAIL = ('<div class="mpad">' + tabs([("Tổng quan", None), ("Chứng từ", 4), ("Chi phí", None), ("Lịch sử", 23)], 0)
                + card(card_header("Lộ trình", "", "Cập nhật 2 phút trước"), tabs([("Hôm nay", None), ("Tuần này", None)], kind="seg", full=True)
                       + kv([("Đã chạy", "18,4 / 31 km"), ("Dự kiến tới", "13:40")]))
                + card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "4 chứng từ"), doc_list()) + "</div>")


# ---------- bảng biến thể ----------
def var_rows(plat):
    web = plat == "web"
    st = {1: "is-hover", 2: "is-focus", 3: "is-dis"}
    rows = [
        vg_row("Underline · một cỡ SM (D5 B)", [("SM · type/label 14 · icon 16", tabs(STATUS[:4]))], 1, "D1 · D4 · D5"),
        vg_row("Trạng thái từng tab", [("Chọn · Hover · Focus · Disabled", tabs(STATUS[:4], 0, st=st)),
                                       ("Segmented · cùng trạng thái", tabs(VIEW + [("Tuyến", None, "route")], 0, kind="seg", st=st))], 2 if web else 1, "Focus: vòng `focus/ring` 2 bên trong tab"),
        vg_row("Nội dung tab", [("Icon + số đếm", tabs(DETAIL)), ("Icon, không số đếm", tabs([(a, None, i) for a, _, i in DETAIL])),
                               ("Số lớn · 999+", tabs([("Tất cả", "1.284"), ("Chờ đối soát", "999+"), ("Lỗi", 0)])),
                               ("Full width", tabs(VIEW, full=True))], 2 if web else 1, "D3 · D4"),
        vg_row("Kiểu phụ — segmented", [("SM · có icon", tabs(VIEW, kind="seg")),
                                        ("2 lựa chọn + icon", tabs([("Bảng", None, "list"), ("Bản đồ", None, "map")], kind="seg", icons=True)),
                                        ("Chỉ icon (nhãn ẩn cho trình đọc màn hình, hiện khi rê)", tabs(VIEW, kind="seg", icon_only=True, aria="Chế độ xem")),
                                        ("Underline chỉ icon", tabs(VIEW, icon_only=True, aria="Chế độ xem")),
                                        ("Full width", tabs([("Hôm nay", None), ("Tuần này", None), ("Tháng này", None)], kind="seg", full=True))], 2 if web else 1, "D2"),
        vg_row("Tràn ngang — cuộn trơn (D6 C)", [("10 tab · cuộn ngang, không mép mờ, không nút", tabs(MANY, 0, ovf=5))], 1, "D6"),
        vg_row("Chữ dài", [("Nhãn dài — không cắt, tab giãn theo chữ", tabs([("Chờ chứng từ gốc từ hãng tàu", 9), ("Đã đối soát với khách", 41), ("Lệch", 2)]))], 1, "nhãn tab không xuống dòng"),
    ]
    if web:
        rows.append(vg_row("Dọc", [("Line · có icon", tabs(SETTINGS, 2, kind="vert", icons=True)), ("Line · không icon", tabs(SETTINGS, 0, kind="vert")),
                                   ("Trạng thái", tabs(SETTINGS, 2, kind="vert", st={0: "is-hover", 1: "is-focus", 4: "is-dis"}))], 3, "D8"))
    return rows


def variants(plat):
    return vg(var_rows(plat))


screens = [
 {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "width": 1280, "title": "Lệnh vận tải", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Tabs trạng thái dưới Section header. Bấm “Trễ hẹn” → tab không có dữ liệu; “Tất cả” để quay lại. Đang tải / Chữ dài ở Bảng chọn.", "html": S_LIST},
 {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "title": "LVT-2026-0412", "crumb": "Lệnh vận tải", "nav": "Điều phối",
  "note": "Tabs nội dung cỡ MD + Tabs phụ (segmented) trong đầu thẻ Lộ trình, Sản lượng.", "html": S_DETAIL},
 {"id": "many-web", "name": "Đối soát · 10 tab", "device": "web", "width": 1280, "title": "Đối soát", "crumb": "Kế toán", "nav": "Báo cáo",
  "note": "10 trạng thái — đã chốt D6 C: cuộn ngang trơn, không mép mờ, không nút", "html": S_MANY},
 {"id": "settings-web", "name": "Cài đặt · Tabs dọc", "device": "web", "width": 1280, "title": "Cài đặt", "crumb": "Quản trị", "nav": "Tổng quan",
  "note": "Tabs dọc trái (D8) + Section header + form.", "html": S_SETTINGS},
 {"id": "list-app", "name": "Lệnh của tôi", "device": "mobile", "title": "Lệnh của tôi", "nav": "Lệnh",
  "note": "Tabs app (D7). Bấm “Chờ nhận” → tab rỗng.", "html": S_APP},
 {"id": "detail-app", "name": "Chi tiết chuyến", "device": "mobile", "title": "LVT-2026-0412", "nav": "Lệnh", "back": True,
  "note": "Tabs nội dung + segmented full width trong thẻ.", "html": S_APP_DETAIL},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none", "note": "Kiểu, cỡ, trạng thái, nội dung, segmented, tràn, chữ dài, dọc.", "html": variants("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app — đổi theo D7.", "html": variants("mobile")},
]

VALUES = [
 # Underline — web
 {"part": "Tab list · Underline", "prop": "gap", "value": 12, "platform": "Web", "sel": ".tbs.line"},
 {"part": "Tab · Underline", "prop": "padding-bottom", "value": 8, "platform": "Web", "sel": ".tbs.line .tab", "cssProp": "padding", "tpl": "0 var(--space-xxs) $"},
 {"part": "Tab · Underline", "prop": "padding-x", "value": 2, "platform": "Web", "sel": ".tbs.line .tab", "cssProp": "padding", "tpl": "0 $ var(--space-md)"},
 {"part": "Tab · Underline", "prop": "gap", "value": 8, "platform": "Web", "sel": ".tab"},
 {"part": "Tab · Underline", "prop": "height", "value": 28, "platform": "Web", "size": "SM", "noOverride": "cao = dòng chữ 20 + lề dưới 8, không khai riêng", "interactive": True, "hitArea": 28},
 {"part": "Nhãn tab", "prop": "font-size", "value": 14, "platform": "Web", "size": "SM", "sel": ".tab", "cssProp": "font", "tpl": "500 $/var(--type-label-line-height) var(--font-body)"},
 {"part": "Vạch chọn", "prop": "height", "value": 2, "platform": "Web", "sel": ".tbs.line .tab", "cssProp": "border-bottom", "tpl": "$ solid transparent"},
 {"part": "Vạch chọn", "prop": "color", "role": "border", "value": "#171717", "on": "#FFFFFF", "sel": ".tbs.line .tab.on", "cssProp": "border-bottom-color"},
 {"part": "Đường nền hàng tab", "prop": "height", "value": 1, "platform": "Web", "sel": ".tbw.k-line::before", "role": "decorative"},
 {"part": "Đường nền hàng tab", "prop": "color", "role": "decorative", "tokenRole": "border", "value": "#E5E5E5", "sel": ".tbw.k-line::before", "cssProp": "background"},
 {"part": "Nhãn tab", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "state": "Default", "sel": ".tab"},
 {"part": "Nhãn tab", "prop": "color", "role": "text", "value": "#404040", "on": "#FFFFFF", "state": "Hover", "sel": [".tab:hover", ".tab.is-hover"]},
 {"part": "Nhãn tab", "prop": "color", "role": "text", "value": "#171717", "on": "#FFFFFF", "state": "Selected", "sel": ".tab.on"},
 {"part": "Nhãn tab", "prop": "color", "role": "text", "hint": True, "value": "#A3A3A3", "on": "#FFFFFF", "state": "Disabled", "sel": [".tab.is-dis", ".tab[disabled]"]},
 {"part": "Vòng focus", "prop": "outline-width", "value": 2, "state": "Focus", "sel": ".tab.is-focus", "cssProp": "outline", "tpl": "$ solid var(--color-focus-ring)"},
 {"part": "Icon tab", "prop": "size", "value": 16, "platform": "Web", "noOverride": "cỡ icon vẽ bằng svg width/height 16 (icon/size/md)"},
 {"part": "Icon tab", "prop": "color", "role": "icon", "value": "#737373", "on": "#FFFFFF", "state": "Default", "noOverride": "icon lấy màu chữ của tab (currentColor) — đổi cùng chữ theo trạng thái"},
 {"part": "Icon tab", "prop": "color", "role": "icon", "value": "#171717", "on": "#FFFFFF", "state": "Selected", "noOverride": "icon lấy màu chữ của tab (currentColor)"},
 # Số đếm (Badge Pill Color SM)
 {"part": "Số đếm", "prop": "height", "value": 22, "sel": ".cntb"},
 {"part": "Số đếm", "prop": "padding-x", "value": 8, "sel": ".cntb", "cssProp": "padding", "tpl": "0 $"},
 {"part": "Số đếm", "prop": "font-size", "value": 12, "sel": ".cntb", "cssProp": "font", "tpl": "400 $/var(--chip-count-line-height) var(--font-body)"},
 {"part": "Số đếm", "prop": "color", "role": "decorative", "value": "#F5F5F5", "on": "#FFFFFF", "state": "Default", "sel": ".cntb", "cssProp": "background"},
 {"part": "Số đếm", "prop": "color", "role": "text", "value": "#404040", "on": "#F5F5F5", "state": "Default", "sel": ".cntb"},
 {"part": "Số đếm", "prop": "color", "role": "decorative", "value": "#F5F5F5", "on": "#FFFFFF", "state": "Selected", "sel": ".tab.on .cntb", "cssProp": "background"},
 {"part": "Số đếm", "prop": "color", "role": "text", "value": "#171717", "on": "#F5F5F5", "state": "Selected", "sel": ".tab.on .cntb"},
 # Segmented (Button border)
 {"part": "Khay segmented", "prop": "padding", "value": 4, "sel": ".tbs.seg"},
 {"part": "Khay segmented", "prop": "radius", "value": 10, "sel": ".tbs.seg", "cssProp": "border-radius"},
 {"part": "Khay segmented", "prop": "color", "role": "decorative", "value": "#FAFAFA", "on": "#FFFFFF", "sel": ".tbs.seg", "cssProp": "background"},
 {"part": "Khay segmented", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".tbs.seg", "cssProp": "box-shadow", "tpl": "inset 0 0 0 $ var(--color-border-secondary)"},
 {"part": "Tab segmented", "prop": "height", "value": 28, "platform": "Web", "size": "SM", "sel": ".tbs.seg .tab", "interactive": True, "hitArea": 28, "control": True},
 {"part": "Tab segmented", "prop": "padding-x", "value": 8, "size": "SM", "sel": ".tbs.seg .tab", "cssProp": "padding", "tpl": "0 $"},
 {"part": "Tab segmented", "prop": "radius", "value": 8, "sel": ".tbs.seg .tab", "cssProp": "border-radius"},
 {"part": "Tab segmented", "prop": "color", "role": "fill", "value": "#FFFFFF", "on": "#FAFAFA", "state": "Selected", "sel": ".tbs.seg .tab.on", "cssProp": "background"},
 {"part": "Tab segmented chỉ icon", "prop": "width", "value": 28, "platform": "Web", "sel": ".tbs.seg .tab.io", "interactive": True, "hitArea": 28, "control": True},
 {"part": "Nhãn ẩn (trình đọc màn hình)", "prop": "width", "value": 1, "role": "decorative", "sel": ".sr"},
 {"part": "Nhãn ẩn (trình đọc màn hình)", "prop": "height", "value": 1, "role": "decorative", "sel": ".sr"},
 # Dọc
 {"part": "Tab dọc", "prop": "gap", "value": 8, "platform": "Web", "sel": ".tbs.vert"},
 {"part": "Tab dọc · vạch chọn", "prop": "width", "value": 2, "platform": "Web", "sel": ".tbs.vert .tab", "cssProp": "border-left", "tpl": "$ solid transparent"},
 {"part": "Tab dọc", "prop": "padding-x", "value": 12, "platform": "Web", "sel": ".tbs.vert .tab", "cssProp": "padding", "tpl": "var(--space-xxs) $ var(--space-xxs) var(--space-md)"},
 # Tràn ngang
 {"part": "Menu Thêm", "prop": "border-width", "value": 1, "role": "decorative", "platform": "Web", "sel": ".tmenu", "cssProp": "box-shadow", "tpl": "var(--shadow-lg),0 0 0 $ var(--shadow-lg-border)"},
 {"part": "Menu Thêm · dòng", "prop": "height", "value": 36, "platform": "Web", "sel": ".tmi", "cssProp": "min-height", "interactive": True, "hitArea": 36},
 # App — chip
 {"part": "Chip tab", "prop": "height", "value": 36, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .tbs.line .tab", "interactive": True, "hitArea": 44, "control": True},
 {"part": "Chip tab", "prop": "padding-x", "value": 12, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .tbs.line .tab", "cssProp": "padding", "tpl": "0 $"},
 {"part": "Chip tab", "prop": "gap", "value": 8, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .tbs.line"},
 {"part": "Chip tab", "prop": "color", "role": "border", "value": "#D4D4D4", "on": "#FFFFFF", "platform": "Mobile", "state": "Default", "sel": ".pv[data-platform=mobile] .tbs.line .tab", "cssProp": "border-color"},
 {"part": "Chip tab", "prop": "color", "role": "text", "value": "#404040", "on": "#FFFFFF", "platform": "Mobile", "state": "Default", "sel": ".pv[data-platform=mobile] .tbs.line .tab"},
 {"part": "Chip tab", "prop": "color", "role": "fill", "value": "#262626", "on": "#FFFFFF", "platform": "Mobile", "state": "Selected", "sel": ".pv[data-platform=mobile] .tbs.line .tab.on", "cssProp": "background"},
 {"part": "Chip tab", "prop": "color", "role": "text", "value": "#FFFFFF", "on": "#262626", "platform": "Mobile", "state": "Selected", "sel": ".pv[data-platform=mobile] .tbs.line .tab.on"},
]
PICK = {**REC, "D4": "b", "D5": "b", "D6": "c"}  # user chốt lại 06:53 04/11
PA = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())
preview = {
 "version": 1, "pick": PICK,
 "changes": "Bản 04/11 theo tổ hợp anh chốt: Underline, segmented Button border cho chuyển chế độ xem, viên số xám, CÓ icon 16 trước nhãn (D4 B), "
            "MỘT cỡ SM 14 (D5 B), tràn ngang CUỘN TRƠN không mép mờ / không nút (D6 C), app chip cuộn ngang, tab dọc Line.",
 "blocks": [
  {"title": "Web", "platform": "web",
   "note": "Underline một cỡ SM 14 có icon 16 · trạng thái Chọn/Hover/Focus/Disabled · icon + số, không số, số lớn, full width · segmented SM/2 lựa chọn/full width · tràn 10 tab cuộn trơn · chữ dài · dọc Line",
   "html": f'<div class="pv pvp" {PA} data-platform="web" data-state="x">{variants("web")}</div>'},
  {"title": "Mobile (app)", "platform": "mobile",
   "note": "Chip cao control/height/sm 36 (vùng chạm 44) · chọn nền accent/solid · số trên chip chọn nền trắng · segmented full width · tràn = cuộn ngang",
   "frames": [f'<div class="pv pvp" {PA} data-platform="mobile" data-state="x">{vg([r])}</div>' for r in var_rows("mobile")]},
 ],
}

page = {
 "component": "Tabs", "slug": "tabs", "title": "Tabs Review",
 "subtitle": "Application component · vòng 2 Preview (04/11) — tổ hợp đã chốt, màn demo khoá theo lựa chọn, bảng biến thể Web/Mobile. Số đo, chữ, màu theo foundation đã chốt.",
 "round": "preview", "preview": preview, "values": VALUES, "tokenFamilies": ["tab", "chip", "control", "focus"],
 "refs": {
  "untitled": {"summary": "Ngang 5 kiểu: <mark>underline</mark>, button-brand, <mark>button-gray</mark>, <mark>button-border</mark>, button-minimal; dọc: line, button-gray. Cỡ sm 14 · md 16, icon 16, Badge pill đếm, fullWidth. Mobile: <mark>NativeSelect</mark> thay hàng tab.",
               "source": "design/_ref/untitled-ui/react/components/application/tabs/tabs.tsx · tabs.demo.tsx"},
  "astryx": {"summary": "Tabs gạch chân accent, một cỡ 14, số trong ngoặc; app dùng tab chip trạng thái có đếm (Lab DEC-096); cài đặt dùng nav trái nền xám (P5).",
             "source": "design/design.md › Tabs, M2, P5 · DEC-096"},
  "usage": ["Điều phối · danh sách lệnh: tab trạng thái có đếm", "Chi tiết lệnh (P7): tab nội dung Tổng quan · Chứng từ · Chi phí · Lịch sử",
            "Kế toán · đối soát: 10 trạng thái (tràn)", "Cài đặt tham số khách (P5): tab dọc", "App lái xe: tab trạng thái lệnh"],
  "platform": "Nhóm B nếu D7 khác Underline (đổi cấu tạo trên app → trục Platform). Số đo theo mode Platform: control/height/sm web 28 · app 36."},
 "css": B.CSS_TABS + OPT_TABS, "cssScreen": B.CSS_BASE + B.CSS_CH + B.CSS_SH + B.CSS_ES + B.CSS_CMD + CSS_SCREEN,
 "states": [{"key": "default", "label": "Có dữ liệu"}, {"key": "loading", "label": "Đang tải"}, {"key": "nores", "label": "Tab không có dữ liệu"}, {"key": "long", "label": "Chữ dài"},
            {"key": "scrolled", "label": "Tràn · đã bấm ›"}, {"key": "more", "label": "Tràn · mở Thêm"}, {"key": "picked", "label": "Tràn · đã chọn tab trong Thêm"}],
 "ideas": [], "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": "[data-js=late]", "state": "nores"}, {"sel": "[data-js=all]", "state": "default"},
           {"sel": "[data-js=tnext]", "state": "scrolled"}, {"sel": "[data-js=tprev]", "state": "default"},
           {"sel": "[data-js=tmore]", "state": "more", "toggle": True}, {"sel": "[data-js=tpick]", "state": "picked"}],
 "protoLayers": [".tmenu"],
 "protoHint": "bấm tab Trễ hẹn / Chờ nhận; màn Đối soát: bấm › rồi ‹ (D6 A), hoặc chọn D6 B rồi bấm Thêm → Trễ hẹn",
}
write(OUT, page, decisions)
