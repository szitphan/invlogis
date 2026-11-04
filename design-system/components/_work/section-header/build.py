#!/usr/bin/env python3
"""Section header — vòng 1 Brainstorm (04/11). Chạy: python3 design-system/components/_work/section-header/build.py && python3 _scripts/ds-component-page.py section-header
Nguồn: Untitled section-headers (title + supporting text + actions / tabs / search + divider; settings layout cột trái) ·
Astryx tiêu đề H2 + hành động · Page header của Header navigation. Mọi số qua token foundation (user 04/11).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
import blocks as B  # noqa: E402
from blocks import (ALL_CSS, CSS_SCREEN, OPT_SH, ORDERS, doc_list, empty, fsec, kv, lt, m_factory, mcard, pill, rec_of,  # noqa: E402
                    section_header, sk, table, table_loading, tabs, vg, vg_row, write)

B.ACTIVE.add("section-header")
OUT = Path(__file__).parent / "page.json"

ACT = [("Xuất file", "dl"), ("Tạo lệnh", "plus", "pri")]
ST = [("Tất cả", 128), ("Đang chạy", 12), ("Chờ xe", 5), ("Trễ hẹn", 3), ("Hoàn tất", None)]
SH_ACT = section_header("Chứng từ của lệnh", "4 chứng từ · 1 chờ ký", [("Tải lên", "dl"), ("Thêm chứng từ", "plus", "pri")])
SH_TABS = section_header("Lệnh trong tuần", "Tuần 45 · 128 lệnh", ACT, tabs(ST[:4]))
SH_Q = section_header("Lệnh trong tuần", "Tuần 45 · 128 lệnh", ACT, tabs(ST[:4]), search="Tìm mã lệnh, khách, lái xe…")
SH_CNT = section_header("Lệnh trong tuần", "Tuần 45 · cập nhật 08:45", ACT, count=128)


def field(a, b):
    return f'<label class="fld"><span>{a}</span><span class="inp">{b}</span></label>'


FORM = (fsec("Giờ làm việc", "Áp cho mọi chi nhánh của Delta Logistics", field("Giờ chốt sổ hằng ngày", "17:30") + field("Ca đêm bắt đầu", "22:00"))
        + fsec("Tạm ứng cho lái xe", "Mức tạm ứng tự duyệt, vượt mức cần kế toán duyệt", field("Ngưỡng tạm ứng", "P-nguong-tam-ung · 5.000.000 ₫")))
SH_APP = section_header("Chuyến hôm nay", "Giờ hẹn 14:00 · 2 điểm giao", [("Báo sự cố", "alert"), ("Gọi điều phối", "bell")])

decisions = [
 {"id": "D1", "title": "Gạch dưới",
  "why": "Section header chia các phần trong một trang (khác tiêu đề trang). Gạch dưới tách phần rõ, nhưng chồng với viền bảng/thẻ ngay dưới thành hai đường.",
  "source": "Untitled section-headers (divider) · Astryx H2 không gạch",
  "options": [{"label": "Có gạch (Untitled)", "desc": "`border/secondary` 1, cách nội dung `space/2xl`.", "rec": True},
              {"label": "Không gạch", "desc": "Chỉ khoảng `layout/section-gap`."}]},
 {"id": "D2", "title": "Đặt Tabs ở đâu",
  "why": "Danh sách có tab trạng thái ngay dưới tiêu đề phần. Hàng riêng dễ đọc; cùng hàng thấp hơn nhưng chật khi có nút và ô tìm.",
  "source": "Untitled section-headers (with tabs) · design.md M2",
  "options": [{"label": "Hàng riêng, thay gạch dưới", "desc": "Nền 1 của Tabs làm đường tách.", "rec": True},
              {"label": "Cùng hàng tiêu đề", "desc": "Thấp hơn ~40; nhiều tab phải cuộn."}]},
 {"id": "D3", "title": "Ô tìm",
  "why": "Danh sách lớn cần ô tìm ngay đầu phần. Đặt trong đầu phần gọn; hàng công cụ riêng có chỗ cho Lọc, Cột, Xuất mà không chen nút chính.",
  "source": "Untitled section-headers (search) · Table toolbar",
  "options": [{"label": "Trong đầu phần, bên phải", "desc": "Ô `control/height/md` rộng `width/xxs` 320 trước nút.", "rec": True},
              {"label": "Hàng công cụ riêng", "desc": "Ô tìm + Lọc dưới tiêu đề, nút chính giữ trên."}]},
 {"id": "D4", "title": "Cỡ",
  "why": "Trong trang có hai tầng: phần lớn (danh sách, chứng từ) và nhóm trong form cài đặt. Cùng cỡ thì form 8 nhóm trông như 8 trang.",
  "source": "Untitled (text-lg / text-sm semibold) · typography.md `type/title-3` 18 · `type/heading` 14",
  "options": [{"label": "Hai cỡ: MD 18 · SM 14", "desc": "MD Cal Sans 18 cho phần trang; SM Inter 600 14 cho nhóm form.", "rec": True},
              {"label": "Một cỡ 18", "desc": "Mọi tiêu đề phần cùng cỡ."}]},
 {"id": "D5", "title": "Bố cục form cài đặt",
  "why": "Màn cài đặt tham số khách (P5) có nhiều nhóm. Untitled đặt tiêu đề nhóm ở cột trái 280–320; tiêu đề trên dễ đọc khi màn hẹp.",
  "source": "Untitled settings pages · design.md P5 · grids.md",
  "options": [{"label": "Tiêu đề trên", "desc": "Nhóm xếp dọc, cách `space/3xl`, gạch giữa nhóm.", "rec": True},
              {"label": "Cột trái `width/xxs`", "desc": "Tiêu đề + mô tả bên trái, ô nhập bên phải."}]},
 {"id": "D6", "title": "Số đếm",
  "why": "“128 lệnh” cho biết quy mô danh sách. Trong phụ đề thì nhẹ; viên số cạnh tiêu đề nổi hơn nhưng lặp với số trên Tabs.",
  "source": "Untitled section header badge · Badge Pill Color SM",
  "options": [{"label": "Trong phụ đề", "desc": "“Tuần 45 · 128 lệnh”.", "rec": True},
              {"label": "Viên số cạnh tiêu đề", "desc": "Cùng viên đếm của Tabs."}]},
 {"id": "D7", "title": "Trên app",
  "why": "Màn 393 không chứa nổi 2 nút có chữ. Lái xe cần thao tác chính (Báo sự cố) thấy ngay, không chui vào ⋯.",
  "source": "touch-focus.md `touch/min` 44 · DEC-096",
  "options": [{"label": "Hành động vào ⋯", "desc": "Một nút 44, mở bottom sheet.", "rec": True},
              {"label": "Nút icon (≤ 2)", "desc": "Icon 44 viền, có nhãn trợ năng."},
              {"label": "Chữ hành động", "desc": "Chữ thao tác cuối bên phải."}]},
]
AT = {'D1': ('detail-web', '.shd', None, 'phần Thông tin chuyến'), 'D2': ('list-web', '.shd.has-tabs', None, 'đầu phần Lệnh trong tuần'), 'D3': ('list-web', '.sh-q, .sh-tool', None, 'ô tìm'), 'D4': ('settings-web', '.fsec .shd', None, 'nhóm Giờ làm việc'), 'D5': ('settings-web', '.fsec', None, 'các nhóm form'), 'D6': ('list-web', '.sh-m', None, 'tiêu đề + phụ đề'), 'D7': ('home-app', '.shd', None, 'đầu phần Chuyến hôm nay')}
for d in decisions:
    sc, sel, st, note = AT[d['id']]
    d["at"] = {"screen": sc, "sel": sel, "note": note, **({"state": st} if st else {})}
REC = rec_of(decisions)
m = m_factory(REC)
PV = {"D1": (SH_ACT + '<div style="height:12px"></div>' + doc_list(B.DOCS[:1]), 640, "web"), "D2": (SH_TABS, 760, "web"), "D3": (SH_Q, 860, "web"),
      "D4": (section_header("Tham số vận hành", "Áp cho Delta Logistics", [("Lưu", None, "pri")]) + '<div style="height:20px"></div>' + FORM, 720, "web"),
      "D5": (FORM, 760, "web"), "D6": (SH_CNT, 680, "web"), "D7": (SH_APP, 360, "mobile")}
UNT = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "b", "D6": "b", "D7": "a"}
AST = {"D1": "b", "D2": "a", "D3": "b", "D4": "b", "D5": "a", "D6": "a", "D7": "c"}
NOTE = {"D1": "H2 không gạch", "D2": "Tabs dưới tiêu đề", "D3": "Thanh công cụ bảng riêng", "D4": "Một cỡ H2", "D5": "Nhãn trên ô",
        "D6": "Trong phụ đề", "D7": "Chữ hành động"}
for d in decisions:
    h, w, plat = PV[d["id"]]
    for k, o in enumerate(d["options"]):
        o["preview"] = m({d["id"]: chr(97 + k)}, h, w, plat)
    d["untitled"] = m({d["id"]: UNT[d["id"]]}, h, w, plat)
    d["astryx"] = m({d["id"]: AST[d["id"]]}, h, w, plat)
    d["astryxNote"] = NOTE[d["id"]]
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC}, {"id": "untitled", "label": "Untitled UI", "pick": UNT}, {"id": "astryx", "label": "Astryx hiện tại", "pick": AST}]

# ---------- màn ----------
NORES = ('<div class="tw" data-show="state:nores">' + empty("Không tìm thấy “Hưng Thịnh”", "Không có lệnh nào của khách, lái xe hay tuyến khớp. Thử mã lệnh đầy đủ.",
                                                        "search", "md", None, ("Xoá tìm kiếm", None), "search", "card") + "</div>")
S_LIST = ('<div class="pad">'
          + section_header(lt("Lệnh trong tuần", "Lệnh vận tải trong tuần 45 của chi nhánh Cát Lái và tuyến quốc tế Campuchia"),
                           lt("Tuần 45 · 128 lệnh · cập nhật 08:45", "Tuần 45 (03/11 – 09/11) · 128 lệnh · cập nhật 08:45 bởi Điều phối ca sáng"),
                           ACT, tabs(ST), search="Tìm mã lệnh, khách, lái xe…", count=128)
          + table(hide="nores loading") + table_loading() + NORES + "</div>")

COSTS = '<div class="tw"><table class="tbl"><tr><th>Khoản</th><th>Nơi phát sinh</th><th>Số tiền</th><th>Trạng thái</th></tr>' + "".join(
    f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{pill(s)}</td></tr>" for a, b, c, s in
    (("Nâng hạ container", "Cảng Cát Lái", "450.000 ₫", "Chờ ký"), ("Cầu đường", "VETC · 3 trạm", "185.000 ₫", "Đã giao"))) + "</table></div>"
S_DETAIL = ('<div class="pad">'
            + section_header("Thông tin chuyến", "Cập nhật 08:45 bởi Điều phối ca sáng", [("Sửa", "edit")])
            + kv([("Khách hàng", "Delta Logistics"), ("Tuyến", "Cát Lái → Sóng Thần"), ("Container", '<span class="code">TGHU 812345-6 · 40 feet</span>'), ("Giờ hẹn", "14:00 · 04/11/2026")])
            + section_header("Chứng từ", "4 chứng từ · 1 chờ ký", [("Tải lên", "dl"), ("Yêu cầu khách ký", "file", "pri")], count=4)
            + '<div data-hide="loading">' + doc_list() + '</div><div data-show="state:loading" style="display:flex;flex-direction:column;gap:12px">' + sk("60%") + sk("50%") + "</div>"
            + section_header("Chi phí phát sinh", "2 khoản · 635.000 ₫", [("Thêm chi phí", "plus")], count=2)
            + COSTS + "</div>")

S_SET = ('<div class="pad" style="max-width:calc(var(--width-2xl) + var(--space-4xl))">'
         + section_header("Tham số vận hành", "Áp cho mọi chi nhánh của Delta Logistics · thay đổi có hiệu lực từ ca sau", [("Khôi phục mặc định", "refresh"), ("Lưu thay đổi", None, "pri")])
         + FORM
         + fsec("Thông báo cho khách", "Gửi khi lệnh đổi trạng thái", field("Kênh gửi", "Email + Zalo OA") + field("Gửi khi trễ hẹn quá", "30 phút"))
         + "</div>")

S_APP = ('<div class="mpad">'
         + section_header(lt("Chuyến hôm nay", "Chuyến hàng lạnh Cát Lái → Sóng Thần ca chiều"), "Giờ hẹn 14:00 · 2 điểm giao", [("Báo sự cố", "alert"), ("Gọi điều phối", "bell")])
         + mcard("LVT-2026-0412", "Cát Lái → Sóng Thần", "Delta Logistics · 14:00", "Đang chạy")
         + '<div style="height:var(--space-lg)"></div>'
         + section_header("Lệnh sắp tới", "3 lệnh · tuần này", [("Xem tất cả", "arrowr")])
         + "".join(mcard(a, c, b, s) for a, b, c, d, s in ORDERS[1:4]) + "</div>")
S_APP_DOC = ('<div class="mpad">'
             + section_header("Chứng từ", "4 chứng từ · 1 chờ ký", [("Chụp chứng từ", "file")], count=4) + doc_list()
             + '<div style="height:var(--space-lg)"></div>'
             + section_header("Chi phí đã gửi", "Chưa có khoản nào", [("Thêm chi phí", "plus")])
             + empty("Chưa có chi phí", "Chụp hoá đơn cầu đường, nâng hạ để gửi điều phối.", "inbox", "sm", ("Thêm chi phí", "plus"), None, "", "card") + "</div>")


def variants(plat):
    web = plat == "web"
    c2 = 2 if web else 1
    rows = [
        vg_row("Cơ bản", [("Chỉ tiêu đề", section_header("Chứng từ")), ("+ phụ đề", section_header("Chứng từ", "4 chứng từ · 1 chờ ký")),
                          ("+ hành động", SH_ACT), ("+ một nút chính", section_header("Lệnh sắp tới", "3 lệnh", [("Tạo lệnh", "plus", "pri")]))], c2, "D1"),
        vg_row("Kèm Tabs / ô tìm", [("Tabs", SH_TABS), ("Tabs + ô tìm", SH_Q)], 1, "D2 · D3"),
        vg_row("Số đếm", [("Viên số (D6 B)", SH_CNT)], 1, "D6"),
        vg_row("Cỡ SM — nhóm trong form", [("SM", section_header("Tạm ứng cho lái xe", "Mức tạm ứng tự duyệt", size="sm")),
                                           ("SM + hành động", section_header("Người nhận thông báo", "3 người", [("Thêm", "plus")], size="sm"))], c2, "D4"),
        vg_row("Chữ dài", [("Tiêu đề, phụ đề dài — xuống dòng", section_header("Lệnh vận tải trong tuần 45 của chi nhánh Cát Lái và tuyến quốc tế Campuchia",
                                                                                "Tuần 45 (03/11 – 09/11) · 128 lệnh · cập nhật 08:45 bởi Điều phối ca sáng", ACT).replace("<h2>", '<h2 style="white-space:normal">'))], 1, ""),
    ]
    if web:
        rows.append(vg_row("Form cài đặt", [("2 nhóm", FORM)], 1, "D5"))
    return vg(rows)


screens = [
 {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "width": 1280, "title": "Lệnh vận tải", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Section header đủ phần: phụ đề, số đếm, ô tìm, 2 nút, Tabs. Tìm không ra / Đang tải / Chữ dài ở Bảng chọn.", "html": S_LIST},
 {"id": "detail-web", "name": "Chi tiết lệnh · chia phần", "device": "web", "width": 1280, "title": "LVT-2026-0412", "crumb": "Lệnh vận tải", "nav": "Điều phối",
  "note": "3 phần không thẻ: Thông tin, Chứng từ, Chi phí — gạch dưới (D1) chồng viền bảng.", "html": S_DETAIL},
 {"id": "settings-web", "name": "Cài đặt tham số", "device": "web", "width": 1280, "title": "Cài đặt", "crumb": "Quản trị", "nav": "Tổng quan",
  "note": "Section header MD đầu trang + nhóm SM (D4, D5).", "html": S_SET},
 {"id": "home-app", "name": "Trang chủ lái xe", "device": "mobile", "title": "Chào anh Bình", "nav": "Trang chủ", "note": "Hành động app theo D7.", "html": S_APP},
 {"id": "doc-app", "name": "Chứng từ chuyến", "device": "mobile", "title": "LVT-2026-0412", "nav": "Lệnh", "back": True, "note": "Hai phần + rỗng.", "html": S_APP_DOC},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none", "note": "Cơ bản, Tabs, ô tìm, số đếm, SM, chữ dài, form.", "html": variants("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app — hành động theo D7.", "html": variants("mobile")},
]

page = {
 "component": "Section header", "slug": "section-header", "title": "Section header Review",
 "subtitle": "Application component · vòng 1 Brainstorm (04/11) — 7 điểm cần quyết, 5 màn demo, bảng biến thể web/app. Số đo, chữ, màu theo foundation đã chốt.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Tiêu đề <mark>text-lg 18</mark>, phụ đề text-sm, hành động phải (nút, ô tìm, Dropdown), biến thể kèm <mark>Tabs</mark>, <mark>gạch dưới</mark>; trang cài đặt đặt tiêu đề nhóm <mark>cột trái</mark>.",
               "source": "untitledui.com/components/section-headers · settings pages"},
  "astryx": {"summary": "Tiêu đề H2 + hành động, không gạch; thanh công cụ bảng (tìm, lọc) là hàng riêng; form nhãn trên ô.",
             "source": "design/design.md › P1, P5, P7"},
  "usage": ["Danh sách lệnh, xe, lái xe: đầu phần có ô tìm + Tabs", "Chi tiết lệnh không thẻ: chia phần Thông tin / Chứng từ / Chi phí",
            "Cài đặt tham số khách (P5): nhóm form", "App lái xe: trang chủ, chứng từ chuyến"],
  "platform": "Nhóm A: một bộ, số đo theo mode Platform; D7 đổi hành động trên app."},
 "css": ALL_CSS + OPT_SH, "cssScreen": CSS_SCREEN,
 "states": [{"key": "default", "label": "Có dữ liệu"}, {"key": "loading", "label": "Đang tải"}, {"key": "nores", "label": "Tìm không ra"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": [], "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": ".sh-q", "state": "nores", "toggle": True}],
 "protoHint": "bấm ô tìm để xem kết quả tìm không ra",
}
write(OUT, page, decisions)
