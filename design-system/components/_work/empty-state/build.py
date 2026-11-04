#!/usr/bin/env python3
"""Empty state — vòng 1 Brainstorm (04/11). Chạy: python3 design-system/components/_work/empty-state/build.py && python3 _scripts/ds-component-page.py empty-state
Nguồn: Untitled empty-state.tsx (FeaturedIcon + BackgroundPattern circle/grid, size sm · md · lg, Title, Description, Footer Secondary + Primary) ·
Astryx EmptyState (icon + tiêu đề + mô tả + 1 nút, chưa có bản mobile) · DEC-012 lỗi mạng giữ tab. Mọi số qua token foundation (user 04/11).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
import blocks as B  # noqa: E402
from blocks import (ALL_CSS, CSS_SCREEN, OPT_ES, ORDERS, card, card_header, empty, ic, kv, m_factory, mcard, pill, rec_of,  # noqa: E402
                    section_header, sk, table, table_loading, tabs, vg, vg_row, write)

B.ACTIVE.add("empty-state")
OUT = Path(__file__).parent / "page.json"

# các loại rỗng — chữ nghiệp vụ, nút theo việc tiếp theo
K = {
 "first": ("Chưa có lệnh vận tải nào", "Tạo lệnh đầu tiên hoặc nhập danh sách lệnh từ file Excel của khách.", "truck", ("Tạo lệnh", "plus"), ("Nhập từ Excel", "dl"), ""),
 "nores": ("Không có lệnh khớp bộ lọc", "Bộ lọc “Trễ hẹn · Tuần 45 · Khách Delta” không có lệnh nào. Bỏ bớt điều kiện để xem thêm.", "search", None, ("Xoá bộ lọc", None), "search"),
 "error": ("Không tải được danh sách lệnh", "Máy chủ không phản hồi. Dữ liệu của bạn chưa bị thay đổi.", "alert", ("Thử lại", "refresh"), ("Báo lỗi", None), "err"),
 "noperm": ("Bạn chưa có quyền xem đối soát", "Đối soát cước chỉ mở cho Kế toán và Quản lý chi nhánh. Gửi yêu cầu để quản trị cấp quyền.", "lock", ("Gửi yêu cầu", None), None, "lock"),
 "offline": ("Mất kết nối mạng", "Lệnh đã tải vẫn xem được. Ảnh chứng từ sẽ tự gửi khi có mạng lại.", "wifioff", ("Thử lại", "refresh"), None, "off"),
 "done": ("Không còn chi phí chờ duyệt", "Mọi chi phí lái xe gửi trong tuần đã được duyệt.", "checkc", None, ("Xem đã duyệt", None), "ok"),
}


def es(k, size="md", ctx="", **over):
    t, d, i, p, s, kind = K[k]
    return empty(over.get("t", t), over.get("d", d), i, size, over.get("p", p), over.get("s", s), kind, ctx, over.get("link"))


ES_MD = '<div class="tw">' + es("first", ctx="card") + "</div>"
ES_ALL = '<div class="grid3">' + "".join(f'<div class="tw">{es(k, "sm", "card")}</div>' for k in ("first", "error", "done")) + "</div>"
ES_CARD = card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app", primary=("Thêm", "plus")),
               empty("Chưa có chi phí phát sinh", "Phí nâng hạ, cầu đường, lưu bãi sẽ hiện ở đây khi lái xe gửi lên.", "inbox", "sm", ("Thêm chi phí", "plus"), None, "", "card"))
ES_SIZES = '<div class="grid3">' + "".join(f'<div class="tw">{empty("Chưa có tuyến nào", "Thêm tuyến để lập bảng giá.", "layers", s, ("Thêm tuyến", "plus"), None, "", "card")}</div>' for s in ("sm", "md", "lg")) + "</div>"
ES_APP = '<div style="position:relative;min-height:440px">' + empty("Hôm nay chưa có lệnh", "Điều phối sẽ gửi lệnh mới vào đây. Bật thông báo để không bỏ lỡ.", "truck", "md", ("Bật thông báo", "bell"), ("Xem lệnh tuần sau", None), "", "page") + "</div>"

decisions = [
 {"id": "D1", "title": "Hình đầu",
  "why": "Rỗng gặp ở bảng, thẻ, cả trang, menu. Hình nặng lặp lại thành nhiễu; hình quá nhẹ người dùng tưởng lỗi tải.",
  "source": "empty-state.tsx (FeaturedIcon + BackgroundPattern) · Astryx EmptyState · icon-sets.md Featured icon 40/48/56",
  "options": [{"label": "Featured icon + nền", "desc": "Đúng Untitled, có chiều sâu, nền mờ dần.", "rec": True},
              {"label": "Chỉ featured icon", "desc": "Nhẹ, hợp ô nhỏ."},
              {"label": "Minh hoạ nét", "desc": "Thân thiện, nhưng mỗi ngữ cảnh cần một hình."}]},
 {"id": "D2", "title": "Kiểu nền (khi D1 = A)",
  "why": "Untitled có nền vòng tròn và lưới ô vuông. Vòng tròn hướng mắt về icon; lưới hợp màn dữ liệu, bảng.",
  "source": "empty-state.tsx BackgroundPattern circle · grid",
  "options": [{"label": "Vòng tròn", "desc": "Vòng cách `space/3xl`, mờ dần.", "rec": True},
              {"label": "Lưới ô vuông", "desc": "Ô `space/3xl`, mờ dần hình elip."}]},
 {"id": "D3", "title": "Màu icon theo loại",
  "why": "Có 6 loại rỗng (lần đầu, lọc không ra, lỗi, không quyền, mất mạng, đã xong). Màu giúp phân biệt lỗi với rỗng bình thường, nhưng nhiều màu làm trang ồn.",
  "source": "color.md `fg/error-primary`, `bg/success-secondary`, `bg/warning-secondary`",
  "options": [{"label": "Xám, chỉ lỗi đỏ", "desc": "Icon lỗi `fg/error-primary`, còn lại `fg/secondary`.", "rec": True},
              {"label": "Xám hết", "desc": "Chữ tiêu đề tự nói loại."},
              {"label": "Màu theo loại", "desc": "Lỗi đỏ, xong xanh, không quyền/mất mạng vàng — ô nền màu."}]},
 {"id": "D4", "title": "Nút",
  "why": "Rỗng lần đầu cần nút tạo; lọc không ra cần nút xoá lọc. Hai nút ngang nhau làm người dùng phải chọn.",
  "source": "empty-state.tsx Footer (Secondary + Primary)",
  "options": [{"label": "Phụ + Chính (Untitled)", "desc": "Nút chính việc tiếp theo, nút phụ cách khác.", "rec": True},
              {"label": "Chỉ nút phụ", "desc": "Khi nút chính đã có ở đầu trang."},
              {"label": "Chỉ nút chính", "desc": "Một việc rõ ràng."}]},
 {"id": "D5", "title": "Cỡ",
  "why": "SM trong thẻ/bảng nhỏ, MD trong bảng, LG cả trang chưa có gì (màn đầu tiên của tenant mới).",
  "source": "empty-state.tsx size sm · md · lg · typography.md (LG tiêu đề `type/title-2` Cal Sans 20)",
  "options": [{"label": "SM · MD · LG", "desc": "LG chữ 20 Cal Sans + mô tả 16, icon 56.", "rec": True},
              {"label": "SM · MD", "desc": "Cả trang dùng MD."}]},
 {"id": "D6", "title": "SM trong thẻ — canh",
  "why": "Thẻ hẹp ở rail phải hoặc thẻ thấp: khối canh giữa chiếm cao; canh trái ngang tiết kiệm chỗ.",
  "source": "Untitled empty state horizontal · Card header",
  "options": [{"label": "Canh giữa", "desc": "Như mọi cỡ.", "rec": True},
              {"label": "Canh trái, icon bên trái", "desc": "Thấp hơn ~40%."}]},
 {"id": "D7", "title": "App — nút ở màn rỗng cả trang",
  "why": "Màn app rỗng cả trang (hôm nay chưa có lệnh): nút trong khối nằm giữa màn; nút cố định đáy nằm vùng ngón cái.",
  "source": "design.md M2 (nút Tạo mới cố định đáy) · touch-focus.md",
  "options": [{"label": "Trong khối, rộng hết", "desc": "Nút `control/height/lg` 52 app.", "rec": True},
              {"label": "Cố định đáy", "desc": "Trên thanh tab, vùng ngón cái."}]},
]
AT = {'D1': ('page-web', '.es', None, 'trang Tuyến trống'), 'D2': ('page-web', '.es-hd', None, 'nền sau icon'), 'D3': ('variants-web', '.es.k-err', None, 'hàng Loại · Lỗi tải'), 'D4': ('list-web', '.es .es-ac', 'empty', 'nút dưới chữ'), 'D5': ('variants-web', '.es.es-lg', None, 'hàng Cỡ · LG'), 'D6': ('detail-web', '.es.c-card', None, 'thẻ Chi phí phát sinh'), 'D7': ('list-app', '.es .es-ac', 'empty', 'nút màn app')}
for d in decisions:
    sc, sel, st, note = AT[d['id']]
    d["at"] = {"screen": sc, "sel": sel, "note": note, **({"state": st} if st else {})}
REC = rec_of(decisions)
m = m_factory(REC)
PV = {"D1": (ES_MD, 520, "web"), "D2": (ES_MD, 520, "web"), "D3": (ES_ALL, 860, "web"), "D4": (ES_MD, 520, "web"),
      "D5": (ES_SIZES, 980, "web"), "D6": ('<div style="max-width:420px">' + ES_CARD + "</div>", 460, "web"), "D7": (ES_APP, 360, "mobile")}
UNT = {"D1": "a", "D2": "a", "D3": "b", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}
AST = {"D1": "b", "D2": "a", "D3": "b", "D4": "c", "D5": "b", "D6": "a", "D7": "a"}
NOTE = {"D1": "Icon + tiêu đề + mô tả", "D2": "Không nền", "D3": "Xám", "D4": "Một nút", "D5": "Một cỡ", "D6": "Canh giữa", "D7": "Nút kiểu web"}
for d in decisions:
    h, w, plat = PV[d["id"]]
    for k, o in enumerate(d["options"]):
        o["preview"] = m({d["id"]: chr(97 + k)}, h, w, plat)
    d["untitled"] = m({d["id"]: UNT[d["id"]]}, h, w, plat)
    d["astryx"] = m({d["id"]: AST[d["id"]]}, h, w, plat)
    d["astryxNote"] = NOTE[d["id"]]
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC}, {"id": "untitled", "label": "Untitled UI", "pick": UNT}, {"id": "astryx", "label": "Astryx hiện tại", "pick": AST}]

# ---------- màn ----------
LONG = dict(t="Không tìm thấy lệnh khớp với “Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics chi nhánh Cát Lái”",
            d="Thử tên khách ngắn hơn, mã số thuế, hoặc mã lệnh đầy đủ dạng LVT-2026-0412. Lệnh đã lưu trữ hơn 12 tháng nằm ở mục Lưu trữ.")
STATES_TBL = "".join(f'<div class="tw" data-show="state:{st}">{es(k, "md", "card")}</div>' for st, k in
                     (("empty", "first"), ("nores", "nores"), ("error", "error"), ("offline", "offline")))
STATES_TBL += f'<div class="tw" data-show="state:long">{es("nores", "md", "card", **LONG)}</div>'
S_LIST = ('<div class="pad">'
          + section_header("Lệnh trong tuần", "Tuần 45 · cập nhật 08:45", [("Xuất file", "dl"), ("Tạo lệnh", "plus", "pri")], tabs([("Tất cả", 128), ("Đang chạy", 12), ("Chờ xe", 5), ("Trễ hẹn", 3)]))
          + '<div data-hide="empty nores error offline loading long noperm">' + table(hide="") + "</div>" + table_loading() + STATES_TBL
          + f'<div class="tw" data-show="state:noperm">{es("noperm", "md", "card")}</div>' + "</div>")

S_PAGE = ('<div class="pad" style="min-height:720px;justify-content:center">'
          + '<div data-hide="noperm error offline">' + empty("Chưa có tuyến nào", "Thêm tuyến để lập bảng giá, gán định mức nhiên liệu và bắt đầu điều phối. Bạn có thể nhập cả bảng tuyến từ Excel.",
                                                           "route", "lg", ("Thêm tuyến", "plus"), ("Nhập từ Excel", "dl"), "", "page", "Xem hướng dẫn thiết lập") + "</div>"
          + '<div data-show="state:noperm">' + es("noperm", "lg", "page") + "</div>"
          + '<div data-show="state:error">' + es("error", "lg", "page", t="Không tải được danh mục tuyến") + "</div>"
          + '<div data-show="state:offline">' + es("offline", "lg", "page") + "</div>" + "</div>")

S_DETAIL = ('<div class="pad"><div class="grid3">'
            + card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app", primary=("Thêm", "plus")),
                   empty("Chưa có chi phí phát sinh", "Phí nâng hạ, cầu đường, lưu bãi sẽ hiện khi lái xe gửi lên.", "inbox", "sm", ("Thêm chi phí", "plus"), None, "", "card"))
            + card(card_header("Ghi chú cho lái xe", "", "Lái xe thấy trên app"),
                   empty("Chưa có ghi chú", "Ghi chú giờ nhận hàng, người liên hệ tại kho.", "file", "sm", None, ("Viết ghi chú", "edit"), "", "card"))
            + card(card_header("Chi phí chờ duyệt", "", "Kế toán"), es("done", "sm", "card"))
            + '<div class="span2">' + card(card_header("Sự cố trên đường", "", "Lái xe báo từ app", count=0), es("done", "sm", "card", t="Chuyến chưa có sự cố", d="Lái xe báo sự cố sẽ hiện ở đây, kèm ảnh và vị trí.", s=None)) + "</div>"
            + card(card_header("Vị trí xe", "", "GPS"), es("offline", "sm", "card", t="Mất tín hiệu GPS", d="Lần cuối 11:52 tại trạm cân Linh Xuân.", p=None, s=("Gọi lái xe", None)))
            + "</div></div>")

MENU = ('<div class="row" style="align-items:flex-start;gap:var(--space-4xl)">'
        '<div class="menu"><div class="inp" style="box-shadow:none;border:0;border-bottom:1px solid var(--color-border-secondary);border-radius:0;gap:var(--space-md);color:var(--color-fg-quaternary)">'
        + ic("search", 14) + '<span style="color:var(--color-text-primary)">51C-999</span></div>'
        + empty("Không có xe khớp “51C-999”", "Kiểm tra biển số hoặc thêm xe mới.", "search", "sm", None, None, "search", "menu", "Thêm xe mới") + "</div>"
        '<div class="notif" style="position:static"><div class="nh"><b>Thông báo</b><a class="lnk">Đánh dấu đã đọc</a></div>'
        + '<div style="padding:var(--space-md) var(--space-xl) 0">' + tabs([("Việc cần làm", 0), ("Tin chung", None)], 0) + "</div>"
        + empty("Không còn việc cần làm", "Duyệt chi phí, ký chứng từ… sẽ hiện ở đây.", "bell", "sm", None, None, "ok", "menu") + "</div></div>")
S_MENU = '<div class="pad">' + section_header("Gán xe cho lệnh LVT-2026-0412", "Chọn đầu kéo sẵn sàng gần Cát Lái") + MENU + "</div>"

APP_ST = "".join(f'<div data-show="state:{st}">{es(k, "md", "page", **ov)}</div>' for st, k, ov in
                 (("empty", "first", dict(t="Hôm nay chưa có lệnh", d="Điều phối sẽ gửi lệnh mới vào đây. Bật thông báo để không bỏ lỡ.", p=("Bật thông báo", "bell"), s=("Xem lệnh tuần sau", None))),
                  ("nores", "nores", dict(t="Không có lệnh chờ nhận", d="Bạn đã nhận hết lệnh được giao.", s=("Xem tất cả", None))),
                  ("error", "error", dict(d="Kiểm tra kết nối rồi thử lại.", s=None)), ("offline", "offline", {}),
                  ("noperm", "noperm", dict(t="Tài khoản chưa được gán xe", d="Liên hệ điều phối để được gán xe trước khi nhận lệnh.", p=("Gọi điều phối", "bell"))),
                  ("long", "nores", LONG)))
S_APP = ('<div class="mpad">' + tabs([("Tất cả", 8), ("Đang chạy", 2), ("Chờ nhận", 1), ("Hoàn tất", 5)])
         + '<div data-hide="empty nores error offline noperm long loading" style="display:flex;flex-direction:column;gap:var(--layout-list-gap)">'
         + "".join(mcard(a, c, f"{b} · {d}", s) for a, b, c, d, s in ORDERS[:3]) + "</div>"
         + '<div data-show="state:loading" style="display:flex;flex-direction:column;gap:var(--layout-list-gap)">' + "".join(f'<div class="mcard">{sk("50%")}{sk("80%", "xs")}</div>' for _ in range(3)) + "</div>"
         + APP_ST + "</div>")
S_APP_DONE = ('<div class="mpad" style="min-height:640px">' + empty("Đã giao xong chuyến hôm nay", "Bạn đã giao 2/2 chuyến. Nghỉ ngơi và kiểm tra lệnh ngày mai lúc 18:00.",
                                                                     "checkc", "md", ("Xem lệnh ngày mai", None), ("Gửi chi phí còn thiếu", "plus"), "ok", "page") + "</div>")


def var_rows(plat):
    web = plat == "web"
    c3 = 3 if web else 1
    G = lambda k, size, extra: f'<div class="tw">{es(k, size, "card")}</div>'.replace('class="es es-', f'class="es {extra} es-', 1)
    rows = [
        vg_row("Thử: featured icon nền xám (góp ý) — so với hiện tại", [
            ("Hiện tại · ô trắng viền", G("first", "md", "")),
            ("Thử · nền xám tròn", G("first", "md", "fs-gray fs-round")),
            ("Thử · nền xám vuông bo", G("first", "md", "fs-gray")),
            ("Hiện tại · lỗi", G("error", "md", "")),
            ("Thử · nền xám tròn · lỗi", G("error", "md", "fs-gray fs-round")),
            ("Thử · nền xám tròn · SM", G("first", "sm", "fs-gray fs-round"))], 3 if web else 1, "nền bg/tertiary, không viền, icon fg/secondary (lỗi fg/error-primary)"),
        vg_row("Loại", [(n, f'<div class="tw">{es(k, "md", "card")}</div>') for n, k in
                        (("Rỗng lần đầu", "first"), ("Lọc không ra", "nores"), ("Lỗi tải", "error"), ("Không có quyền", "noperm"), ("Mất mạng", "offline"), ("Đã xong hết", "done"))], c3, "D3 · D4 · icon xám, chỉ lỗi đỏ"),
        vg_row("Cỡ — hai cỡ (D5 B)", [("SM · icon 40 · heading 14 · trong thẻ, bảng nhỏ", f'<div class="tw">{es("first", "sm", "card")}</div>'),
                                      ("MD · icon 48 · 16 · bảng, cả trang", f'<div class="tw">{es("first", "md", "card")}</div>')], 2 if web else 1, "D5"),
        vg_row("Nút", [("Phụ + chính", f'<div class="tw">{es("first", "sm", "card")}</div>'), ("Một nút", f'<div class="tw">{es("error", "sm", "card", s=None)}</div>'),
                       ("Liên kết", f'<div class="tw">{es("nores", "sm", "card", s=None, link="Xoá bộ lọc")}</div>'), ("Không nút", f'<div class="tw">{es("done", "sm", "card", s=None)}</div>')],
               4 if web else 1, "D4"),
        vg_row("Ngữ cảnh", [("Trong thẻ", ES_CARD), ("Trong menu chọn", MENU.split('<div class="notif"')[0] + "</div>")], 2 if web else 1, "D6"),
        vg_row("Chữ dài", [("Tiêu đề 2 dòng, mô tả 3 dòng", f'<div class="tw">{es("nores", "md", "card", **LONG)}</div>')], 1, "rộng chữ tối đa `width/xs` 384"),
    ]
    if not web:
        rows.insert(2, vg_row("Cả màn app — nút cố định đáy (D7 B)", [("Hôm nay chưa có lệnh", '<div style="position:relative;height:520px;border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);overflow:hidden">'
            + empty("Hôm nay chưa có lệnh", "Điều phối sẽ gửi lệnh mới vào đây. Bật thông báo để không bỏ lỡ.", "truck", "md", ("Bật thông báo", "bell"), ("Xem lệnh tuần sau", None), "", "page")
            .replace('class="es-ac"', 'class="es-ac" style="bottom:var(--space-xl)"') + "</div>")], 1, "nút rộng hết, nằm vùng ngón cái"))
    return rows


def variants(plat):
    return vg(var_rows(plat))


screens = [
 {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "width": 1280, "title": "Lệnh vận tải", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Rỗng trong bảng — chọn Rỗng / Lọc không ra / Lỗi tải / Không quyền / Mất mạng / Chữ dài ở Bảng chọn.", "html": S_LIST},
 {"id": "page-web", "name": "Danh mục tuyến — trang trống", "device": "web", "width": 1280, "title": "Tuyến", "crumb": "Danh mục", "nav": "Lệnh vận tải",
  "note": "LG cả trang cho tenant mới; Không quyền / Lỗi / Mất mạng ở Bảng chọn.", "html": S_PAGE},
 {"id": "detail-web", "name": "Chi tiết lệnh · thẻ rỗng", "device": "web", "width": 1280, "title": "LVT-2026-0412", "crumb": "Lệnh vận tải", "nav": "Điều phối",
  "note": "SM trong thẻ: rỗng lần đầu, đã xong, mất GPS (D6).", "html": S_DETAIL},
 {"id": "menu-web", "name": "Menu chọn · thông báo", "device": "web", "width": 1280, "title": "Gán xe", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Rỗng trong menu chọn (có liên kết thêm mới) và panel thông báo.", "html": S_MENU},
 {"id": "list-app", "name": "Lệnh của tôi", "device": "mobile", "title": "Lệnh của tôi", "nav": "Lệnh", "note": "App cả trang: chọn trạng thái ở Bảng chọn; D7 vị trí nút.", "html": S_APP},
 {"id": "done-app", "name": "Đã xong chuyến", "device": "mobile", "title": "Hôm nay", "nav": "Trang chủ", "note": "Rỗng tích cực (đã xong) trên app.", "html": S_APP_DONE},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none", "note": "6 loại, 3 cỡ, nút, ngữ cảnh, chữ dài.", "html": variants("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app.", "html": variants("mobile")},
]

PICK = {**REC, "D1": "b", "D5": "b", "D7": "b"}  # user chốt 04/11 07:21; D1 B theo góp ý cmw1tu578 (bỏ nền)
PA = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())
preview = {
 "version": 1, "pick": PICK,
 "changes": "Bản 04/11 theo tổ hợp anh chốt: CHỈ featured icon, bỏ nền vòng tròn (góp ý), icon xám (chỉ lỗi đỏ), nút phụ + chính, HAI cỡ SM · MD (D5 B — trang trống "
            "cả màn dùng MD), SM trong thẻ canh giữa, app màn rỗng cả trang NÚT CỐ ĐỊNH ĐÁY (D7 B). Không có góp ý trên trang.",
 "blocks": [
  {"title": "Web", "platform": "web", "note": "6 loại × MD · hai cỡ SM/MD · 4 kiểu nút · trong thẻ / menu chọn · chữ dài",
   "html": f'<div class="pv pvp" {PA} data-platform="web" data-state="x">{variants("web")}</div>'},
  {"title": "Mobile (app)", "platform": "mobile", "note": "Nút xếp dọc rộng hết, cao control/height/lg 52 · màn rỗng cả trang: nút cố định đáy trên thanh tab",
   "frames": [f'<div class="pv pvp" {PA} data-platform="mobile" data-state="x">{vg([r])}</div>' for r in var_rows("mobile")]},
 ],
}
VALUES = [
 # Featured icon
 {"part": "Featured icon", "prop": "size", "value": 48, "size": "MD", "sel": ".fi.f48", "cssProp": ["width", "height"]},
 {"part": "Featured icon", "prop": "size", "value": 40, "size": "SM", "sel": ".fi.f40", "cssProp": ["width", "height"]},
 {"part": "Featured icon", "prop": "radius", "value": 10, "size": "MD", "sel": ".fi", "cssProp": "border-radius"},
 {"part": "Featured icon", "prop": "radius", "value": 8, "size": "SM", "sel": ".fi.f40", "cssProp": "border-radius"},
 {"part": "Featured icon", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".fi", "cssProp": "box-shadow", "tpl": "var(--shadow-xs),inset 0 0 0 $ var(--color-border-primary)"},
 {"part": "Featured icon · viền", "prop": "color", "role": "decorative", "tokenRole": "border", "value": "#D4D4D4", "on": "#FFFFFF", "noOverride": "viền vẽ bằng box-shadow inset", "at": ".fi"},
 {"part": "Featured icon · icon", "prop": "size", "value": 20, "noOverride": "icon svg 20 (icon/size/lg)", "at": ".fi svg"},
 {"part": "Featured icon · icon", "prop": "color", "role": "icon", "value": "#404040", "on": "#FFFFFF", "state": "Default", "sel": ".fi", "cssProp": "color"},
 {"part": "Featured icon · icon", "prop": "color", "role": "icon", "value": "#D23C2E", "on": "#FFFFFF", "state": "Lỗi", "sel": ".es.k-err .fi", "cssProp": "color"},
 # Khối MD
 {"part": "Empty state MD", "prop": "padding-y", "value": 40, "platform": "Web", "size": "MD", "sel": ".es", "cssProp": "padding", "tpl": "$ var(--space-3xl)"},
 {"part": "Empty state MD", "prop": "padding-x", "value": 24, "platform": "Web", "size": "MD", "sel": ".es", "cssProp": "padding", "tpl": "var(--space-5xl) $"},
 {"part": "Empty state MD", "prop": "gap", "value": 16, "size": "MD", "sel": ".es"},
 {"part": "Tiêu đề", "prop": "font-size", "value": 16, "size": "MD", "sel": ".es-t", "cssProp": "font", "tpl": "600 $/var(--type-body-lg-line-height) var(--font-body)"},
 {"part": "Tiêu đề", "prop": "color", "role": "text", "value": "#171717", "on": "#FFFFFF", "sel": ".es-t"},
 {"part": "Mô tả", "prop": "font-size", "value": 14, "sel": ".es-d", "cssProp": "font", "tpl": "400 $/var(--type-body-line-height) var(--font-body)"},
 {"part": "Mô tả", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "sel": ".es-d"},
 {"part": "Khối chữ", "prop": "max-width", "value": 384, "sel": ".es-tx"},
 {"part": "Khối chữ", "prop": "gap", "value": 4, "sel": ".es-tx"},
 {"part": "Hàng nút", "prop": "gap", "value": 12, "platform": "Web", "sel": ".es-ac"},
 {"part": "Hàng nút", "prop": "margin-top", "value": 8, "size": "MD", "sel": ".es-ac"},
 # Khối SM
 {"part": "Empty state SM", "prop": "padding-y", "value": 24, "size": "SM", "sel": ".es.es-sm", "cssProp": "padding", "tpl": "$ var(--space-xl)"},
 {"part": "Empty state SM", "prop": "padding-x", "value": 16, "size": "SM", "sel": ".es.es-sm", "cssProp": "padding", "tpl": "var(--space-3xl) $"},
 {"part": "Empty state SM", "prop": "gap", "value": 12, "size": "SM", "sel": ".es.es-sm"},
 {"part": "Tiêu đề", "prop": "font-size", "value": 14, "size": "SM", "sel": ".es.es-sm .es-t", "cssProp": "font", "tpl": "600 $/var(--type-heading-line-height) var(--font-body)"},
 {"part": "Nút SM", "prop": "height", "value": 28, "platform": "Web", "size": "SM", "sel": ".es.es-sm .bt", "interactive": True, "hitArea": 28, "control": True},
 # Nền vòng tròn
 # App
 {"part": "Empty state app", "prop": "padding-y", "value": 48, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .es", "cssProp": "padding", "tpl": "$ var(--space-3xl)"},
 {"part": "Nút app", "prop": "height", "value": 52, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .es-ac .bt", "interactive": True, "hitArea": 52, "control": True},
 {"part": "Hàng nút app", "prop": "gap", "value": 8, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .es-ac"},
 {"part": "Hàng nút app · cố định đáy", "prop": "bottom", "value": 88, "platform": "Mobile", "sel": ".pv[data-platform=mobile][data-D7=b] .es.c-page .es-ac", "noOverride": "= space/9xl − space/md, trên thanh tab"},
]

page = {
 "component": "Empty state", "slug": "empty-state", "title": "Empty state Review",
 "subtitle": "Application component · vòng 2 Preview (04/11) — tổ hợp đã chốt, màn demo khoá theo lựa chọn, bảng biến thể Web/Mobile. Số đo, chữ, màu theo foundation đã chốt.",
 "round": "preview", "preview": preview, "values": VALUES,
 "cssIgnore": [{"sel": ".es-pat", "props": ["-webkit-mask", "mask", "background"], "why": "nền vòng tròn đã bỏ theo góp ý (D1 B) — không hiện trên hình"},
               {"sel": ".es-grd", "props": ["-webkit-mask", "mask"], "why": "như trên — nền lưới thuộc phương án D2 B đã loại"}], "tokenFamilies": ["featured-icon", "control", "empty"],
 "refs": {
  "untitled": {"summary": "<mark>FeaturedIcon</mark> + BackgroundPattern (<mark>circle</mark> / grid), 3 cỡ <mark>sm · md · lg</mark>, Title, Description (max-w 352), Footer <mark>Secondary + Primary</mark>; biến thể có avatar quanh vòng.",
               "source": "design/_ref/untitled-ui/react/components/application/empty-state/empty-state.tsx"},
  "astryx": {"summary": "EmptyState thư viện: icon + tiêu đề + mô tả + một nút kiểu web, chưa có bản mobile; lỗi mạng ở Thông báo giữ tab + nút Thử lại (DEC-012).",
             "source": "design/design.md › M2, Notification Center · DEC-012"},
  "usage": ["Danh sách lệnh / xe / lái xe: rỗng lần đầu, lọc không ra, lỗi tải", "Tenant mới: danh mục tuyến, bảng giá chưa có gì (LG)",
            "Chi tiết lệnh: thẻ Chi phí, Ghi chú, Sự cố rỗng", "Menu chọn xe, panel thông báo", "App lái xe: hôm nay chưa có lệnh, mất mạng, đã xong"],
  "platform": "Nhóm A: một bộ, số đo theo mode Platform; app nút xếp dọc rộng hết (D7)."},
 "css": B.CSS_ES + OPT_ES, "cssScreen": B.CSS_BASE + B.CSS_TABS + B.CSS_CH + B.CSS_SH + B.CSS_CMD + CSS_SCREEN,
 "states": [{"key": "default", "label": "Có dữ liệu"}, {"key": "empty", "label": "Rỗng lần đầu"}, {"key": "nores", "label": "Lọc không ra"}, {"key": "error", "label": "Lỗi tải"},
            {"key": "noperm", "label": "Không có quyền"}, {"key": "offline", "label": "Mất mạng"}, {"key": "loading", "label": "Đang tải"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": [], "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": ".es .bt.pri", "state": "default"}],
 "protoHint": "chọn loại rỗng ở Bảng chọn; bấm nút chính để về có dữ liệu",
}
write(OUT, page, decisions)
