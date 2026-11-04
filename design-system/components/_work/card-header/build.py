#!/usr/bin/env python3
"""Card header — vòng 1 Brainstorm (04/11). Chạy: python3 design-system/components/_work/card-header/build.py && python3 _scripts/ds-component-page.py card-header
Nguồn: Untitled card-headers (title + badge + supporting text + actions + divider; leading featured icon / avatar) ·
Astryx P7 “khối H3 có hành động” · memory: tiêu đề khối nằm trong thẻ. Mọi số qua token foundation (user 04/11).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
import blocks as B  # noqa: E402
from blocks import (ALL_CSS, CSS_SCREEN, OPT_CH, ORDERS, bt, card, card_header, doc_list, empty, ibt, kv, lt, m_factory, pill,  # noqa: E402
                    rec_of, sk, table, tabs, vg, vg_row, write, ic)

B.ACTIVE.add("card-header")
OUT = Path(__file__).parent / "page.json"


def body(x, rows=3):
    return (f'<div data-hide="loading" style="display:flex;flex-direction:column;gap:var(--space-lg)">{x}</div>'
            f'<div data-show="state:loading" style="display:flex;flex-direction:column;gap:var(--space-lg)">'
            + "".join(sk(w) for w in ("70%", "55%", "80%", "40%")[:rows]) + "</div>")


TRIP = kv([("Khách hàng", "Delta Logistics"), ("Tuyến", "Cát Lái → Sóng Thần"), ("Container", '<span class="code">TGHU 812345-6 · 40 feet</span>'), ("Giờ hẹn", "14:00 · 04/11/2026")])
CH_FULL = card(card_header("Thông tin chuyến", pill("Đang chạy"), "Cập nhật 08:45 bởi Điều phối ca sáng", lead=("fi", "truck")), TRIP)
CH_COUNT = card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "Cảng Cát Lái và lái xe gửi", count=4, primary=("Tải lên", "dl")), doc_list(B.DOCS[:2]))
CH_COL = card(card_header("Lịch sử thay đổi", "", "23 sự kiện", lead=("fi", "clock"), collapse=True, primary=("Xuất", "dl")),
              '<div class="feed"><div>' + ic("clock", 16) + '<span>Gán xe 51C-404.12<small>07:30 · Điều phối ca sáng</small></span></div></div>', "clp")
CH_TBL = card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app", count=3, primary=("Thêm", "plus")),
              table([("CP-0412-01", "Nâng hạ", "Cát Lái", "Trần Văn Bình", "Chờ ký")][:1], hide=""), "tbl")
CH_APP = card(card_header("Thông tin chuyến", pill("Đang chạy"), "Cập nhật 08:45", lead=("fi", "truck"), link="Sửa"),
              kv([("Tuyến", "Cát Lái → Sóng Thần"), ("Giờ hẹn", "14:00")]))

decisions = [
 {"id": "D1", "title": "Cấu tạo",
  "why": "Màn chi tiết (P7) có 4–8 thẻ. Đầu thẻ đầy đủ (tiêu đề `type/title-3` 18 Cal Sans + phụ đề + gạch) rõ ràng nhưng cao ~73px; bản gọn (heading 14) đọc nhanh khi thẻ nhiều.",
  "source": "Untitled card-headers · Astryx P7 khối H3 · typography.md (Cal Sans chỉ từ 18)",
  "options": [{"label": "Đầy đủ (Untitled)", "desc": "Tiêu đề 18, phụ đề, gạch dưới; lề `space/3xl` × `space/2xl`.", "rec": True},
              {"label": "Gọn", "desc": "Tiêu đề `type/heading` 14, không phụ đề, không gạch, lề `space/2xl`."}]},
 {"id": "D2", "title": "Hành động bên phải",
  "why": "Đầu thẻ đặt thao tác của riêng khối. Nhiều nút làm hàng đầu rối; chỉ ⋯ thì giấu thao tác hay dùng.",
  "source": "Untitled card-headers (Button + Dropdown icon) · Astryx P7",
  "options": [{"label": "Nút phụ SM + ⋯", "desc": "Một thao tác chính hiện chữ (Secondary SM 28), còn lại vào ⋯.", "rec": True},
              {"label": "Chỉ ⋯", "desc": "Gọn nhất."},
              {"label": "Liên kết “Xem tất cả →”", "desc": "Cho thẻ tóm tắt dẫn sang màn khác."}]},
 {"id": "D3", "title": "Phần đầu (leading)",
  "why": "Thẻ tổng quan, thẻ người (lái xe, khách) có thể kèm icon/ảnh để quét nhanh. Trên màn nhiều thẻ, icon nào cũng có thì mất tác dụng.",
  "source": "Untitled card-headers (Featured icon / Avatar) · icon-sets.md Featured icon `featured-icon/size-md` 40",
  "options": [{"label": "Featured icon 40 (tuỳ chọn)", "desc": "Ô icon viền + `shadow/xs`; thẻ người dùng Avatar 40.", "rec": True},
              {"label": "Icon trần 20", "desc": "Icon `icon/size/lg` cạnh tiêu đề, không ô."},
              {"label": "Không dùng", "desc": "Đầu thẻ chỉ có chữ."}]},
 {"id": "D4", "title": "Số đếm cạnh tiêu đề",
  "why": "“Chứng từ 4”, “Chi phí 3” — số giúp biết khối có gì trước khi đọc. Badge trạng thái cũng nằm cạnh tiêu đề, hai khối xám liền nhau dễ rối.",
  "source": "Badge Pill Color SM (`chip/*`, DEC-303) · Untitled card header badge",
  "options": [{"label": "Viên số xám", "desc": "Cùng viên đếm của Tabs.", "rec": True},
              {"label": "Chữ xám “· 4”", "desc": "Nhẹ, không thêm khối."}]},
 {"id": "D5", "title": "Nút thu gọn",
  "why": "Rail phải P7 (Ghi chú, Lịch sử) cần thu gọn. Chevron trái gắn với tiêu đề (như cây thư mục); chevron phải gom cùng hành động.",
  "source": "design.md P7 rail Collapsible · motion.md 10.3 (xoay `duration/medium`)",
  "options": [{"label": "Bên phải, sau hành động", "desc": "Utility SM, xoay −90° khi gọn.", "rec": True},
              {"label": "Bên trái tiêu đề", "desc": "Bấm cả hàng tiêu đề để thu gọn."}]},
 {"id": "D6", "title": "Thẻ chứa bảng",
  "why": "Bảng chi phí, bảng chuyến nằm trong thẻ. Đầu thẻ trắng + gạch rồi tới hàng tên cột xám: ba tầng. Đầu thẻ nền xám gộp thành thanh bảng.",
  "source": "Untitled table card header · Table `table/*` token",
  "options": [{"label": "Đầu thẻ trắng + gạch, bảng liền", "desc": "Cùng hình mọi thẻ.", "rec": True},
              {"label": "Đầu thẻ nền xám như thanh bảng", "desc": "`bg/secondary`, bỏ phụ đề."}]},
 {"id": "D7", "title": "Trên app",
  "why": "Màn 393 không chứa nổi nút chữ + ⋯ cạnh tiêu đề 18. Lái xe bấm một tay: vùng chạm ≥ `touch/min` 44.",
  "source": "touch-focus.md · DEC-096 thẻ mobile",
  "options": [{"label": "Giữ phụ đề, hành động vào ⋯", "desc": "⋯ vùng chạm 44, mở bottom sheet.", "rec": True},
              {"label": "Bỏ phụ đề, hành động là chữ", "desc": "Chữ “Sửa” bên phải, thấy ngay."}]},
]
AT = {'D1': ('detail-web', '.chd', None, 'thẻ Thông tin chuyến'), 'D2': ('detail-web', '.chd .act', None, 'bên phải đầu thẻ'), 'D3': ('detail-web', '.ch-ld', None, 'ô icon trước tiêu đề'), 'D4': ('detail-web', '.ch-nb, .ch-nt', None, 'thẻ Chứng từ'), 'D5': ('detail-web', '.cc.clp .chd', None, 'thẻ Lịch sử thay đổi'), 'D6': ('detail-web', '.cc.tbl .chd', None, 'thẻ Chi phí phát sinh'), 'D7': ('detail-app', '.chd', None, 'đầu thẻ app')}
for d in decisions:
    sc, sel, st, note = AT[d['id']]
    d["at"] = {"screen": sc, "sel": sel, "note": note, **({"state": st} if st else {})}
REC = rec_of(decisions)
m = m_factory(REC)
PV = {"D1": (CH_FULL, 520, "web"), "D2": (CH_FULL, 520, "web"), "D3": (CH_FULL, 520, "web"), "D4": (CH_COUNT, 520, "web"),
      "D5": (CH_COL, 520, "web"), "D6": (CH_TBL, 640, "web"), "D7": (CH_APP, 360, "mobile")}
UNT = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}
AST = {"D1": "b", "D2": "a", "D3": "c", "D4": "b", "D5": "b", "D6": "b", "D7": "b"}
NOTE = {"D1": "Khối H3 + hành động, không gạch", "D2": "Nút Tertiary bên phải", "D3": "Không icon", "D4": "Số trong tiêu đề",
        "D5": "Collapsible chevron trái", "D6": "Bảng trong Card không đầu", "D7": "Thẻ mobile: tiêu đề + chữ hành động"}
for d in decisions:
    h, w, plat = PV[d["id"]]
    for k, o in enumerate(d["options"]):
        o["preview"] = m({d["id"]: chr(97 + k)}, h, w, plat)
    d["untitled"] = m({d["id"]: UNT[d["id"]]}, h, w, plat)
    d["astryx"] = m({d["id"]: AST[d["id"]]}, h, w, plat)
    d["astryxNote"] = NOTE[d["id"]]
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC}, {"id": "untitled", "label": "Untitled UI", "pick": UNT}, {"id": "astryx", "label": "Astryx hiện tại", "pick": AST}]

# ---------- màn ----------
FEED = ('<div class="feed">' + "".join(f'<div>{ic(i, 16)}<span>{t}<small>{s}</small></span></div>' for i, t, s in
                                       (("truck", "Gán xe 51C-404.12 · mooc 51R-118.07", "07:30 · Điều phối ca sáng"),
                                        ("file", "Lái xe gửi Phiếu giao nhận (EIR)", "08:12 · Trần Văn Bình"),
                                        ("clock", "Đổi giờ hẹn 13:00 → 14:00", "08:40 · Khách Delta Logistics"))) + "</div>")
COSTS = [("CP-0412-01", "Nâng hạ container", "Cảng Cát Lái", "450.000 ₫", "Chờ ký"), ("CP-0412-02", "Cầu đường", "VETC · 3 trạm", "185.000 ₫", "Đã giao"),
         ("CP-0412-03", "Lưu bãi", "ICD Sóng Thần", "320.000 ₫", "Chờ ký")]
COST_TBL = ('<div class="tw" data-hide="loading"><table class="tbl"><tr><th>Mã</th><th>Khoản</th><th>Nơi phát sinh</th><th>Số tiền</th><th>Trạng thái</th></tr>'
            + "".join(f'<tr><td class="code">{a}</td><td>{b}</td><td>{c}</td><td class="num">{d}</td><td>{pill(s)}</td></tr>' for a, b, c, d, s in COSTS) + "</table></div>"
            + '<div data-show="state:loading" style="padding:var(--space-3xl);display:flex;flex-direction:column;gap:var(--space-lg)">' + sk("90%") + sk("70%") + sk("80%") + "</div>")
S_DETAIL = ('<div class="pad"><div class="grid2">'
            + card(card_header(lt("Thông tin chuyến", "Thông tin chuyến hàng lạnh tạm nhập tái xuất qua cửa khẩu Mộc Bài"), pill("Đang chạy"),
                               lt("Cập nhật 08:45 bởi Điều phối ca sáng", "Cập nhật 08:45 bởi Điều phối ca sáng chi nhánh Cát Lái — đã gửi khách xác nhận giờ hẹn mới"),
                               lead=("fi", "truck")), body(TRIP, 4))
            + card(card_header("Lái xe và xe", "", "Gán lúc 07:30", lead=("av", 0), primary=("Đổi xe", "truck")),
                   body(kv([("Lái xe", "Trần Văn Bình · 0903 xxx 128"), ("Đầu kéo", '<span class="code">51C-404.12</span>'), ("Mooc", '<span class="code">51R-118.07</span>')]), 3))
            + card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "Cảng Cát Lái và lái xe gửi", lead=("fi", "file"), count=4, primary=("Tải lên", "dl")), body(doc_list(), 4))
            + card(card_header("Lịch sử thay đổi", "", "23 sự kiện", lead=("fi", "clock"), collapse=True, primary=("Xuất", "dl")), body(FEED, 3), "clp")
            + '<div class="span2">' + card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app · chờ kế toán duyệt", lead=("fi", "fuel"), count=3, primary=("Thêm chi phí", "plus")), COST_TBL, "tbl") + "</div>"
            + "</div></div>")

KPI = lambda v, s: f'<div class="kpi"><b>{v}</b><small>{s}</small></div>'
BARS = '<div class="bars">' + "".join(f'<i style="height:{h}%"{" class=on" if k == 5 else ""}></i>' for k, h in enumerate((40, 62, 55, 80, 66, 92, 48))) + "</div>"
S_DASH = ('<div class="pad"><div class="grid3">'
          + card(card_header("Chuyến hôm nay", "", "Cập nhật 08:45", acts=tabs([("Ngày", None), ("Tuần", None), ("Tháng", None)], kind="seg")), body(KPI("42", "+6 so với hôm qua") + BARS, 2))
          + card(card_header("Xe đang chạy", "", "31/48 xe", acts='<a class="lnk">Xem bản đồ' + ic("arrowr", 14) + "</a>"), body(KPI("31", "17 xe chờ lệnh"), 2))
          + card(card_header("Chi phí tháng", "", "Tháng 10/2026", acts=bt("Tháng 10", "sec", "calendar", size="sm") + ibt("more", "Thêm", size="sm")), body(KPI("1,82 tỷ ₫", "92% kế hoạch"), 2))
          + '<div class="span2">' + card(card_header("Cảnh báo cần xử lý", pill("3 trễ hẹn", "red"), "Sắp xếp theo mức khẩn", count=7, primary=("Xem tất cả", "arrowr")),
                                        table(ORDERS[:3], hide="loading") + '<div data-show="state:loading" style="padding:var(--space-3xl)">' + sk("80%") + "</div>", "tbl") + "</div>"
          + card(card_header("Chi phí chờ duyệt", "", "Kế toán", lead=("fi", "fuel"), primary=("Duyệt", "checkc")),
                 empty("Không còn chi phí chờ duyệt", "Mọi chi phí lái xe gửi đã được duyệt.", "checkc", "sm", None, None, "ok", "card"))
          + "</div></div>")

S_APP = ('<div class="mpad">'
         + card(card_header(lt("Thông tin chuyến", "Thông tin chuyến tạm nhập tái xuất qua Mộc Bài"), pill("Đang chạy"), "Cập nhật 08:45", lead=("fi", "truck"), link="Sửa"),
                body(kv([("Tuyến", "Cát Lái → Sóng Thần"), ("Container", '<span class="code">TGHU 812345-6</span>'), ("Giờ hẹn", "14:00")]), 3))
         + card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "4 chứng từ", lead=("fi", "file"), count=4, link="Tải lên"), body(doc_list(), 3))
         + card(card_header("Lịch sử", "", "23 sự kiện", collapse=True, link="Xem"), body(FEED, 3), "clp")
         + "</div>")
S_HOME = ('<div class="mpad">'
          + card(card_header("Chuyến hôm nay", "", "2 chuyến · 1 đang chạy", link="Xem tất cả"),
                 body('<div class="mcard"><div class="mc1"><b class="code">LVT-2026-0412</b>' + pill("Đang chạy") + '</div><span class="mc2">Cát Lái → Sóng Thần</span></div>', 2))
          + card(card_header("Chi phí đã gửi", "", "Tháng 11", count=3, link="Thêm"), body(kv([("Chờ duyệt", "2 khoản · 770.000 ₫"), ("Đã duyệt", "1 khoản · 185.000 ₫")]), 2))
          + card(card_header("Thông báo", "", "", lead=("fi", "bell")), empty("Chưa có thông báo", "Điều phối gửi lệnh mới sẽ hiện ở đây.", "bell", "sm", None, None, "", "card"))
          + "</div>")


# ---------- bảng biến thể ----------
def variants(plat):
    web = plat == "web"
    c2, c3 = (2, 3) if web else (1, 1)
    SB = '<div class="sk" style="width:60%"></div>'
    rows = [
        vg_row("Phần đầu", [("Không leading", card(card_header("Thông tin chuyến", pill("Đang chạy"), "Cập nhật 08:45"), SB)),
                            ("Featured icon 40", card(card_header("Thông tin chuyến", pill("Đang chạy"), "Cập nhật 08:45", lead=("fi", "truck")), SB)),
                            ("Avatar 40", card(card_header("Trần Văn Bình", pill("Đang chạy"), "Lái xe · 0903 xxx 128", lead=("av", 0), primary=("Gọi", "bell")), SB))], c3, "D3"),
        vg_row("Hành động", [("Nút phụ + ⋯ (theo D2)", card(card_header("Chứng từ", "", "4 chứng từ", primary=("Tải lên", "dl")), SB)),
                             ("Segmented", card(card_header("Chuyến", "", "7 ngày", acts=tabs([("Ngày", None), ("Tuần", None), ("Tháng", None)], kind="seg")), SB)),
                             ("Chọn kỳ + ⋯", card(card_header("Chi phí", "", "Tháng 10", acts=bt("Tháng 10", "sec", "calendar", size="sm") + ibt("more", "Thêm", size="sm")), SB)),
                             ("Hai nút", card(card_header("Đề nghị thanh toán", "", "Chờ bạn duyệt", acts=bt("Từ chối", "sec", None, size="sm") + bt("Duyệt", "pri", None, size="sm")), SB)),
                             ("Không hành động", card(card_header("Ghi chú", "", "Từ khách"), SB))], c3, "D2"),
        vg_row("Tiêu đề", [("Badge + số đếm", card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "4 chứng từ", count=4), SB)),
                           ("Không phụ đề", card(card_header("Lộ trình"), SB)),
                           ("Chữ dài — xuống dòng", card(card_header("Thông tin chuyến hàng lạnh tạm nhập tái xuất qua cửa khẩu Mộc Bài", pill("Đang chạy"),
                                                                     "Cập nhật 08:45 bởi Điều phối ca sáng chi nhánh Cát Lái").replace("<h3>", '<h3 style="white-space:normal">'), SB))], c3, "D4"),
        vg_row("Thu gọn", [("Mở", card(card_header("Lịch sử thay đổi", "", "23 sự kiện", collapse=True), SB, "clp")),
                           ("Đã gọn", card(card_header("Lịch sử thay đổi", "", "23 sự kiện", collapse=True), SB, "clp is-col"))], c2, "D5"),
        vg_row("Thẻ chứa bảng", [("Bảng 2 dòng", card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app", count=3, primary=("Thêm", "plus")),
                                                    table(ORDERS[:2], hide=""), "tbl"))], 1, "D6"),
        vg_row("Thân thẻ rỗng / đang tải", [("Rỗng", card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app", primary=("Thêm", "plus")),
                                                           empty("Chưa có chi phí", "Chi phí lái xe gửi sẽ hiện ở đây.", "inbox", "sm", ("Thêm chi phí", "plus"), None, "", "card"))),
                                            ("Đang tải", card(card_header("Chứng từ", "", "Đang tải…", count=None), sk("70%") + sk("50%")))], c2, ""),
    ]
    return vg(rows)


screens = [
 {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "title": "LVT-2026-0412", "crumb": "Lệnh vận tải", "nav": "Điều phối",
  "note": "6 thẻ: featured icon, avatar, số đếm, thu gọn (bấm chevron thẻ Lịch sử), thẻ chứa bảng. Đang tải / Thu gọn / Chữ dài ở Bảng chọn.", "html": S_DETAIL},
 {"id": "dash-web", "name": "Tổng quan điều phối", "device": "web", "width": 1280, "title": "Tổng quan", "crumb": "Điều phối", "nav": "Tổng quan",
  "note": "Thẻ KPI: segmented, liên kết, chọn kỳ; thẻ bảng cảnh báo; thẻ rỗng “đã xong”.", "html": S_DASH},
 {"id": "detail-app", "name": "Chi tiết chuyến", "device": "mobile", "title": "LVT-2026-0412", "nav": "Lệnh", "back": True, "note": "Card header app (D7).", "html": S_APP},
 {"id": "home-app", "name": "Trang chủ lái xe", "device": "mobile", "title": "Chào anh Bình", "nav": "Trang chủ", "note": "Thẻ tóm tắt dẫn sang màn khác.", "html": S_HOME},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none", "note": "Phần đầu, hành động, tiêu đề, thu gọn, bảng, rỗng/đang tải.", "html": variants("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app — hành động theo D7.", "html": variants("mobile")},
]

EXTRA = (".cc.is-col .cc-b,.cc.is-col .ch-dv{display:none}.cc.is-col .ch-col svg,.cc.is-col .ch-coll svg{transform:rotate(-90deg)}"
         ".num{font-variant-numeric:tabular-nums}")
page = {
 "component": "Card header", "slug": "card-header", "title": "Card header Review",
 "subtitle": "Application component · vòng 1 Brainstorm (04/11) — 7 điểm cần quyết, 4 màn demo, bảng biến thể web/app. Số đo, chữ, màu theo foundation đã chốt.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Tiêu đề <mark>text-lg 18</mark> + Badge, phụ đề text-sm, hành động phải (Button, Dropdown icon), <mark>gạch dưới</mark>; phần đầu Featured icon hoặc Avatar; lề px-6 pt-5.",
               "source": "untitledui.com/components/card-headers"},
  "astryx": {"summary": "Khối H3 + hành động nằm trong thẻ (P7), không gạch; rail phải Collapsible chevron trái; thẻ mobile tiêu đề + chữ hành động.",
             "source": "design/design.md › P7, M4 · DEC-096"},
  "usage": ["Chi tiết lệnh (P7): Thông tin chuyến, Lái xe và xe, Chứng từ, Chi phí, Lịch sử", "Tổng quan điều phối: thẻ KPI, thẻ cảnh báo",
            "App lái xe: thẻ chuyến, chứng từ, chi phí đã gửi"],
  "platform": "Nhóm A: một bộ, số đo theo mode Platform (lề thẻ `layout/card-padding` app 16); D7 đổi hành động trên app."},
 "css": ALL_CSS + OPT_CH + EXTRA, "cssScreen": CSS_SCREEN,
 "states": [{"key": "default", "label": "Có dữ liệu"}, {"key": "loading", "label": "Đang tải"}, {"key": "collapsed", "label": "Thu gọn"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": [], "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": ".cc.clp .ch-col, .cc.clp .ch-coll", "state": "collapsed", "toggle": True}],
 "protoHint": "bấm chevron của thẻ Lịch sử để thu gọn / mở",
}
write(OUT, page, decisions)
