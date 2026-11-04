#!/usr/bin/env python3
"""Page header — vòng 1 Brainstorm (04/11), có ý tưởng cộng đồng (user: nghiên cứu thêm nguồn ngoài Untitled / Astryx).
Chạy: python3 design-system/components/_work/page-header/build.py && python3 _scripts/ds-component-page.py page-header
Nguồn: Untitled page-headers (Simple, Avatar, Banner ×2) · Astryx P7 (Back link + H1 + hàng meta + hành động) · Header navigation
(DEC-291: đường dẫn ở thanh trên, Page header không lặp; Layout Secondary Nav có hàng tab) · Primer PageHeader · Carbon for IBM
Products PageHeader · SAP Fiori Dynamic Page · Salesforce Highlights panel · Shopify Polaris Page · Atlassian Page header ·
Apple HIG large title · Material 3 top app bar · Stripe, Linear. Mọi số qua token foundation (user 04/11).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
import blocks as B  # noqa: E402
from blocks import (ALL_CSS, CSS_PH, CSS_SCREEN, OPT_PH, ORDERS, card, card_header, doc_list, empty, ic, kv, lt, m_factory, mcard,  # noqa: E402
                    page_header, page_sticky, pill, rec_of, section_header, sk, table, table_loading, tabs, vg, vg_row, write)

B.ACTIVE.add("page-header")
OUT = Path(__file__).parent / "page.json"

# ---------- dữ liệu ----------
ACT_LIST = [("Nhập từ Excel", "dl"), ("Xuất file", "dl"), ("Tạo lệnh", "plus", "pri")]
ACT_DET = [("Huỷ lệnh", "x"), ("In lệnh", "file"), ("Đổi xe", "truck"), ("Hoàn tất chuyến", "checkc", "pri")]
FIELDS = [("Khách hàng", "Delta Logistics"), ("Tuyến", "Cát Lái → Sóng Thần"), ("Lái xe", "Trần Văn Bình"),
          ("Đầu kéo · mooc", '<span class="code">51C-404.12 · 51R-118.07</span>'), ("Giờ hẹn", "14:00 · 04/11/2026")]
FIELDS_LONG = [("Khách hàng", "Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics chi nhánh Cát Lái"), ("Tuyến", "Cảng Cát Lái → KCN Sóng Thần, Dĩ An, Bình Dương"),
               ("Lái xe", "Trần Văn Bình (lái chính) · Lê Thị Hoa (phụ xe)"), ("Đầu kéo · mooc", '<span class="code">51C-404.12 · 51R-118.07</span>'), ("Giờ hẹn", "14:00 · 04/11/2026")]
META = ["Tạo 03/11 08:12 bởi Điều phối ca sáng", "Cập nhật 08:45", "Ưu tiên: Cao"]
DTABS = [("Tổng quan", None), ("Chứng từ", 4), ("Chi phí", None), ("Lịch sử", 23)]

PH_LIST = page_header("Lệnh vận tải", "Điều phối · tuần 45 · 128 lệnh", ACT_LIST)
PH_DET = page_header("LVT-2026-0412", "", ACT_DET, pill("Đang chạy"), FIELDS, META, ("fi", "truck"), "Lệnh vận tải", (3, 128))
PH_DRV = page_header("Trần Văn Bình", "Lái xe · mã NV LX-0128", [("Gọi", "bell"), ("Gán lệnh", "truck", "pri")], pill("Sẵn sàng"),
                     [("Điện thoại", "0903 xxx 128"), ("Bằng lái", "FC · hết hạn 12/2028"), ("Xe đang giữ", '<span class="code">51C-404.12</span>'), ("Chuyến tháng 10", "26 chuyến")],
                     [], ("av", 0), "Lái xe", (12, 48))
PH_APP = page_header("LVT-2026-0412", "", ACT_DET, pill("Đang chạy"), FIELDS[:4], META[:2], ("fi", "truck"), "Lệnh của tôi")

decisions = [
 {"id": "D1", "title": "Cấu tạo đầu trang",
  "why": "Mọi màn vận hành mở đầu bằng Page header. Bản đầy đủ (tiêu đề 24 + phụ đề + gạch) rõ tầng trang; bản gọn tiết kiệm chiều cao khi bảng là nội dung chính.",
  "source": "Untitled page-headers Simple · Linear (tiêu đề một dòng) · typography.md `type/title-1` 24 Cal Sans = tiêu đề màn",
  "options": [{"label": "Simple (Untitled)", "desc": "Tiêu đề `type/title-1` 24, phụ đề, hành động phải, gạch dưới.", "rec": True, "ideas": ["I1", "I8"]},
              {"label": "Gọn", "desc": "Tiêu đề `type/title-2` 20, không phụ đề, không gạch.", "ideas": ["I12"]}]},
 {"id": "D2", "title": "Thông tin bản ghi dưới tiêu đề (màn chi tiết)",
  "why": "Điều phối mở lệnh để biết ngay khách, tuyến, lái xe, xe, giờ hẹn. Hàng meta chữ gọn nhưng phải đọc cả câu; khối trường chính quét theo cột được.",
  "source": "Astryx P7 hàng meta · Salesforce Highlights panel (tối đa 7 trường) · SAP Fiori header content · Stripe",
  "options": [{"label": "Hàng meta chữ", "desc": "Người tạo · cập nhật · ưu tiên, ngăn bằng chấm.", "ideas": ["I3"]},
              {"label": "Khối trường chính", "desc": "4–6 cặp nhãn `type/caption` + giá trị `type/label`, xếp lưới.", "rec": True, "ideas": ["I5", "I6", "I11"]},
              {"label": "Không có", "desc": "Thông tin nằm trong thẻ Tổng quan."}]},
 {"id": "D3", "title": "Quay lại trang cha",
  "why": "Header navigation đã đặt đường dẫn ở thanh trên và chốt Page header không lặp đường dẫn (DEC-291). Nút ← hoặc liên kết cha vẫn tiện khi mở chi tiết từ danh sách.",
  "source": "DEC-291 · Primer (back button / parent link) · Polaris backAction · Astryx P7 Back link",
  "options": [{"label": "Không — đường dẫn trên thanh trên lo", "desc": "Giữ đúng DEC-291.", "rec": True, "ideas": ["I1"]},
              {"label": "Nút ← trước tiêu đề", "desc": "Utility MD viền, cùng hàng tiêu đề.", "ideas": ["I3", "I7"]},
              {"label": "Liên kết “‹ Lệnh vận tải” trên tiêu đề", "desc": "Lặp một tầng của đường dẫn.", "ideas": ["I8"]}]},
 {"id": "D4", "title": "Nhiều hành động",
  "why": "Chi tiết lệnh có 4–6 thao tác (Huỷ, In, Đổi xe, Hoàn tất…). Hiện hết thì hàng đầu dài và nút chính lạc.",
  "source": "Carbon PageHeader (thao tác tràn vào menu) · Primer (thu vào nút tràn khi hẹp) · Polaris (1 hành động chính)",
  "options": [{"label": "≤ 2 nút + ⋯", "desc": "Nút chính ở cuối, một nút phụ, còn lại trong ⋯.", "rec": True, "ideas": ["I3", "I4", "I7"]},
              {"label": "Hiện hết", "desc": "Mọi nút trên một hàng."}]},
 {"id": "D5", "title": "Khi cuộn",
  "why": "Chi tiết lệnh dài (chứng từ, chi phí, lịch sử). Cuộn xuống mất tiêu đề và nút chính thì phải cuộn ngược để thao tác.",
  "source": "Carbon PageHeader collapse on scroll · SAP Fiori Dynamic Page (snap on scroll) · Apple HIG large title",
  "options": [{"label": "Cuộn mất", "desc": "Đơn giản, không lớp dính."},
              {"label": "Thanh gọn dính đầu", "desc": "Tiêu đề 16 + trạng thái + nút chính + hàng tab, nền trắng `shadow/sm`.", "rec": True, "ideas": ["I4", "I5"]},
              {"label": "Chỉ hàng tab dính", "desc": "Tiêu đề cuộn mất, tab ở lại."}]},
 {"id": "D6", "title": "Tab của trang (Tổng quan · Chứng từ · Chi phí · Lịch sử)",
  "why": "Header navigation đã duyệt kiểu Secondary Nav: hàng tab ngay dưới thanh trên, nằm TRÊN tiêu đề trang. Primer, Carbon, Atlassian đặt tab trong Page header, DƯỚI tiêu đề.",
  "source": "header-navigation.md Layout = Secondary Nav · Primer PageHeader.Navigation · Carbon navigation slot · Ant Card tabList",
  "options": [{"label": "Trong Page header, dưới tiêu đề", "desc": "Đổi Header nav: bỏ Secondary Nav, tab thuộc Page header.", "ideas": ["I3", "I4", "I8"]},
              {"label": "Secondary Nav của Header nav (đã duyệt)", "desc": "Tab ở trên tiêu đề — giữ nguyên Header nav.", "rec": True}]},
 {"id": "D7", "title": "Ảnh / icon đầu tiêu đề",
  "why": "Màn chi tiết đối tượng (lái xe, xe, khách) nhận ra nhanh nhờ avatar, ảnh xe, logo. Màn danh sách không cần.",
  "source": "Untitled page-headers Avatar · icon-sets.md Featured icon 48",
  "options": [{"label": "Có, tuỳ chọn", "desc": "Avatar / Featured icon 48 cho màn chi tiết đối tượng.", "rec": True, "ideas": ["I2"]},
              {"label": "Không", "desc": "Chỉ chữ."}]},
 {"id": "D8", "title": "Chuyển bản ghi trước / sau",
  "why": "Điều phối duyệt lần lượt nhiều lệnh trong danh sách đã lọc. Nút ‹ › giữ ngữ cảnh lọc, không phải quay về danh sách.",
  "source": "Polaris Page pagination · Gmail · Linear (J/K)",
  "options": [{"label": "Có “‹ 3 / 128 ›”", "desc": "Utility SM, theo thứ tự danh sách vừa lọc.", "rec": True, "ideas": ["I7"]},
              {"label": "Không", "desc": "Quay về danh sách để mở lệnh khác."}]},
 {"id": "D9", "title": "Trên app",
  "why": "App lái xe: tiêu đề lớn đọc rõ ngoài trời, nhưng chiếm chỗ. Kiểu iOS: tiêu đề lớn trong nội dung, cuộn lên thì thu vào thanh trên.",
  "source": "Apple HIG large title · Material 3 top app bar medium/large · DEC-096 M2 (tiêu đề dòng riêng)",
  "options": [{"label": "Tiêu đề lớn, thu khi cuộn", "desc": "`type/title-1` 24 trong nội dung; thanh trên hiện tiêu đề khi đã cuộn.", "rec": True, "ideas": ["I9", "I10"]},
              {"label": "Chỉ tiêu đề nhỏ trên thanh", "desc": "Thanh 18, nội dung bắt đầu bằng thông tin."}]},
]
REC = rec_of(decisions)
m = m_factory(REC)
PV = {"D1": (PH_LIST, 900, "web"), "D2": (PH_DET, 980, "web"), "D3": (PH_DET, 980, "web"), "D4": (PH_DET, 980, "web"),
      "D5": ('<div style="position:relative;padding-top:var(--space-xl)">' + page_sticky("LVT-2026-0412", pill("Đang chạy"), ("Hoàn tất chuyến", "checkc"), tabs(DTABS)).replace('data-show="state:scrolled"', "") + "</div>", 980, "web"),
      "D6": ('<div class="hn-sec">' + tabs(DTABS) + '</div><div style="height:var(--space-xl)"></div>' + page_header("LVT-2026-0412", "", ACT_DET, pill("Đang chạy"), FIELDS[:3], tab_html=tabs(DTABS)), 980, "web"),
      "D7": (PH_DRV, 980, "web"), "D8": (PH_DET, 980, "web"), "D9": (PH_APP, 360, "mobile")}
UNT = {"D1": "a", "D2": "c", "D3": "a", "D4": "b", "D5": "a", "D6": "a", "D7": "a", "D8": "b", "D9": "b"}
AST = {"D1": "a", "D2": "a", "D3": "b", "D4": "b", "D5": "a", "D6": "a", "D7": "b", "D8": "b", "D9": "a"}
NOTE = {"D1": "H1 + hành động", "D2": "Hàng meta (P7)", "D3": "Back link (P7)", "D4": "Hiện hết", "D5": "Cuộn mất", "D6": "Tabs dưới H1 (P7)",
        "D7": "Không", "D8": "Không", "D9": "Tiêu đề 28 dòng riêng (M2)"}
AT = {"D1": ("list-web", ".phd", None, "đầu trang Lệnh vận tải"), "D2": ("detail-web", ".ph-kf, .ph-meta", None, "dưới tiêu đề"),
      "D3": ("detail-web", ".ph-r", None, "trước / trên tiêu đề"), "D4": ("detail-web", ".ph-a", None, "cụm nút phải"),
      "D5": ("detail-web", ".ph-st", "scrolled", "thanh dính khi đã cuộn"), "D6": ("detail-web", ".hn-sec, .ph-tabs", None, "hàng tab"),
      "D7": ("driver-web", ".ph-ld", None, "avatar lái xe"), "D8": ("detail-web", ".ph-pg", None, "‹ 3 / 128 ›"), "D9": ("detail-app", ".phd", None, "đầu màn app")}
for d in decisions:
    h, w, plat = PV[d["id"]]
    for k, o in enumerate(d["options"]):
        o["preview"] = m({d["id"]: chr(97 + k)}, h, w, plat)
    d["untitled"] = m({d["id"]: UNT[d["id"]]}, h, w, plat)
    d["astryx"] = m({d["id"]: AST[d["id"]]}, h, w, plat)
    d["astryxNote"] = NOTE[d["id"]]
    sc, sel, st, note = AT[d["id"]]
    d["at"] = {"screen": sc, "sel": sel, "note": note, **({"state": st} if st else {})}

# ---------- ý tưởng từ nguồn khác (vẽ lại bằng HTML, không nhúng ảnh) ----------
ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/components/page-headers", "title": "Page header · Simple",
  "why": "Tiêu đề + phụ đề + nút chính bên phải, gạch dưới; mobile nút xuống dưới tiêu đề. Khung chuẩn cho màn danh sách.", "pick": {"D1": "a", "D3": "a"}, "pv": PH_LIST},
 {"id": "I2", "source": "Untitled UI", "url": "https://www.untitledui.com/components/page-headers", "title": "Page header · Avatar",
  "why": "Avatar cùng hàng tiêu đề — hợp màn hồ sơ lái xe, khách hàng. (Kiểu Banner ảnh bìa không dùng: màn vận hành không có ảnh bìa.)", "pick": {"D7": "a"}, "pv": PH_DRV},
 {"id": "I3", "source": "GitHub Primer", "url": "https://primer.style/product/components/page-header/guidelines", "title": "PageHeader · back + trailing actions",
  "why": "Nút quay lại đứng trước tiêu đề; khi hẹp, hành động phụ thu vào nút tràn; có dòng mô tả và vùng điều hướng (tab) dưới tiêu đề.",
  "pick": {"D2": "a", "D3": "b", "D4": "a", "D6": "a"}, "pv": PH_DET},
 {"id": "I4", "source": "Carbon for IBM Products", "url": "https://cdn.jsdelivr.net/npm/@carbon/ibm-products@2.94.0/es/components/PageHeader/PageHeader.d.ts", "title": "PageHeader · thu gọn khi cuộn",
  "why": "Cuộn xuống thì phần đầu thu lại, hàng tiêu đề + tab dính đầu; thao tác không đủ chỗ thì vào menu; tag tràn vào hộp thoại.",
  "pick": {"D4": "a", "D5": "b", "D6": "a"}, "pv": '<div style="position:relative;padding-top:var(--space-xl)">' + page_sticky("LVT-2026-0412", pill("Đang chạy"), ("Hoàn tất chuyến", "checkc"), tabs(DTABS)).replace('data-show="state:scrolled"', "") + "</div>"},
 {"id": "I5", "source": "SAP Fiori", "url": "https://experience.sap.com/fiori-design-web/v1-74/dynamic-page-layout", "title": "Dynamic Page · tiêu đề + phần thông tin thu gọn",
  "why": "Tiêu đề luôn hiện; phần thông tin chính (trường, KPI) bên dưới thu lại khi cuộn hoặc khi bấm, tiêu đề tóm tắt lại thông tin đó.",
  "pick": {"D2": "b", "D5": "b"}, "pv": PH_DET},
 {"id": "I6", "source": "Salesforce", "url": "https://developer.salesforce.com/trailhead/en/lex_migration_customization/lex_migration_customization_layouts_ui", "title": "Record page · Highlights panel",
  "why": "Dưới tiêu đề bản ghi là hàng tối đa 7 trường chính (theo compact layout); màn nhỏ hiện ít trường hơn.", "pick": {"D2": "b"}, "pv": PH_DET},
 {"id": "I7", "source": "Shopify Polaris", "url": "https://shopify.dev/docs/api/app-home/latest/web-components", "title": "Page · trạng thái cạnh tiêu đề + chuyển bản ghi",
  "why": "Badge trạng thái đứng cạnh tiêu đề; một hành động chính, phần còn lại vào “Thêm thao tác”; nút ‹ › sang đơn trước/sau.",
  "pick": {"D3": "b", "D4": "a", "D8": "a"}, "pv": PH_DET},
 {"id": "I8", "source": "Atlassian", "url": "https://atlassian.design/components/page-header", "title": "Page header · bottom bar",
  "why": "Đường dẫn + tiêu đề + hành động; khe “bottom bar” dưới tiêu đề cho bộ lọc/tab của trang.", "pick": {"D1": "a", "D3": "c", "D6": "a"}, "pv": PH_LIST},
 {"id": "I9", "source": "Apple HIG", "url": "https://developer.apple.com/design/human-interface-guidelines/navigation-bars", "title": "Large title · thu vào thanh khi cuộn",
  "why": "Tiêu đề lớn trong nội dung để định hướng, cuộn lên thì thu thành tiêu đề nhỏ trên thanh điều hướng.", "pick": {"D9": "a"}, "pv": PH_APP, "plat": "mobile"},
 {"id": "I10", "source": "Material 3", "url": "https://m3.material.io/components/top-app-bar/overview", "title": "Top app bar · medium / large",
  "why": "Thanh trên có biến thể medium/large: tiêu đề hai tầng, thu về small khi cuộn; hành động là nút icon bên phải.", "pick": {"D9": "a"}, "pv": PH_APP, "plat": "mobile"},
 {"id": "I11", "source": "Stripe Dashboard", "url": "https://docs.stripe.com/dashboard/basics", "title": "Chi tiết thanh toán · số tiền + trạng thái + trường",
  "why": "Chi tiết một giao dịch mở bằng số tiền lớn + trạng thái, ngay dưới là hàng trường chính (ngày, khách, phương thức).", "pick": {"D2": "b"}, "pv": PH_DET},
 {"id": "I12", "source": "Linear", "url": "https://linear.app/docs/issues", "title": "Tiêu đề một dòng gọn",
  "why": "Tiêu đề ngắn một dòng, thuộc tính đặt ở cột phải thay vì dưới tiêu đề — tối đa chỗ cho nội dung.", "pick": {"D1": "b", "D2": "c"}, "pv": PH_LIST},
]
for i in ideas:
    plat = i.pop("plat", "web")
    w = 980 if plat == "web" else 360
    z = 0.33 if plat == "web" else 0.85
    i["preview"] = f'<div style="width:{w + 16}px;zoom:{z}">' + m(i.pop("pick"), i.pop("pv"), w, plat) + "</div>"

presets = [{"id": "rec", "label": "Đề xuất", "pick": REC}, {"id": "untitled", "label": "Untitled UI", "pick": UNT}, {"id": "astryx", "label": "Astryx hiện tại", "pick": AST}]
for i in ideas:
    pk = {**REC}
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pk[d["id"]] = chr(97 + k)
    presets.append({"id": i["id"], "label": f'{i["id"]} · {i["source"]}', "pick": pk, "screen": 6 if i["id"] in ("I9", "I10") else (2 if i["id"] == "I2" else (0 if i["id"] in ("I1", "I8", "I12") else 1))})

# ---------- màn ----------
SEC = '<div class="hn-sec">{}</div>'


def body_cards():
    return ('<div class="grid2">'
            + card(card_header("Thông tin chuyến", "", "Cập nhật 08:45"), kv([("Container", '<span class="code">TGHU 812345-6 · 40 feet</span>'), ("Hàng", "Hàng lạnh −18 °C"), ("Điểm giao", "Kho Minh Long, KCN Sóng Thần")]))
            + card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "4 chứng từ", primary=("Tải lên", "dl")), doc_list())
            + card(card_header("Chi phí phát sinh", "", "Lái xe gửi từ app", primary=("Thêm", "plus")), empty("Chưa có chi phí", "Chi phí lái xe gửi sẽ hiện ở đây.", "inbox", "sm", ("Thêm chi phí", "plus"), None, "", "card"))
            + card(card_header("Lịch sử", "", "23 sự kiện", primary=("Xuất", "dl")), kv([("08:45", "Đổi giờ hẹn 13:00 → 14:00"), ("08:12", "Lái xe gửi EIR"), ("07:30", "Gán xe 51C-404.12")]))
            + "</div>")


S_LIST = ('<div class="pad">'
          + '<div data-hide="scrolled">' + page_header(lt("Lệnh vận tải", "Lệnh vận tải chi nhánh Cát Lái và tuyến quốc tế Campuchia"),
                                                        lt("Điều phối · tuần 45 · 128 lệnh", "Điều phối · tuần 45 (03/11 – 09/11) · 128 lệnh · cập nhật 08:45 bởi Điều phối ca sáng"), ACT_LIST) + "</div>"
          + page_sticky("Lệnh vận tải", "", ("Tạo lệnh", "plus"))
          + tabs([("Tất cả", 128), ("Đang chạy", 12), ("Chờ xe", 5), ("Trễ hẹn", 3), ("Hoàn tất", None)])
          + table(hide="loading") + table_loading() + "</div>")

DET = lambda fields: page_header(lt("LVT-2026-0412", "LVT-2026-0412 · Hàng lạnh tạm nhập tái xuất qua cửa khẩu Mộc Bài"), "", ACT_DET, pill("Đang chạy"), fields, META,
                                 ("fi", "truck"), "Lệnh vận tải", (3, 128), tab_html=tabs(DTABS))
S_DETAIL = ('<div class="pad">'
            + '<div data-hide="scrolled long">' + DET(FIELDS) + "</div>"
            + '<div data-show="state:long">' + DET(FIELDS_LONG) + "</div>"
            + page_sticky("LVT-2026-0412", pill("Đang chạy"), ("Hoàn tất chuyến", "checkc"), tabs(DTABS))
            + body_cards() + "</div>")

S_DRIVER = ('<div class="pad">' + '<div data-hide="scrolled">' + PH_DRV + "</div>"
            + page_sticky("Trần Văn Bình", pill("Sẵn sàng"), ("Gán lệnh", "truck"))
            + '<div class="grid2">' + card(card_header("Chuyến gần đây", "", "Tháng 10 · 26 chuyến", primary=("Xem tất cả", "arrowr")), table(ORDERS[:3], hide="")) .replace('class="cc ', 'class="cc tbl ')
            + card(card_header("Giấy tờ", pill("1 sắp hết hạn", "yellow"), "Bằng lái, CCCD, chứng chỉ"), doc_list([("Bằng lái FC", "Hết hạn 12/2028"), ("Chứng chỉ hàng nguy hiểm", "Hết hạn 01/2027")]))
            + "</div></div>")

S_SETTINGS = ('<div class="pad" style="max-width:calc(var(--width-2xl) + var(--space-4xl))">'
              + page_header("Cài đặt tham số", "Áp cho mọi chi nhánh của Delta Logistics · có hiệu lực từ ca sau", [("Khôi phục mặc định", "refresh"), ("Lưu thay đổi", None, "pri")])
              + section_header("Giờ làm việc", "Giờ chốt sổ, ca đêm", size="sm")
              + '<label class="fld"><span>Giờ chốt sổ hằng ngày</span><span class="inp">17:30</span></label></div>')

S_APP_LIST = ('<div class="mpad">' + '<div data-hide="scrolled">' + page_header("Lệnh của tôi", "Hôm nay · 2 chuyến", [("Lọc", "filter")]) + "</div>"
              + page_sticky("Lệnh của tôi")
              + tabs([("Tất cả", 8), ("Đang chạy", 2), ("Chờ nhận", 1), ("Hoàn tất", 5)])
              + "".join(mcard(a, c, f"{b} · {d}", s) for a, b, c, d, s in ORDERS[:3]) + "</div>")
S_APP_DET = ('<div class="mpad">' + '<div data-hide="scrolled long">' + PH_APP + "</div>"
             + '<div data-show="state:long">' + page_header(lt("LVT-2026-0412", "LVT-2026-0412 · Hàng lạnh tạm nhập tái xuất"), "", ACT_DET, pill("Đang chạy"), FIELDS_LONG[:4], META[:2], ("fi", "truck")) + "</div>"
             + page_sticky("LVT-2026-0412", pill("Đang chạy"), None, tabs(DTABS))
             + tabs(DTABS)
             + card(card_header("Chứng từ", pill("1 chờ ký", "yellow"), "4 chứng từ"), doc_list()) + "</div>")


def var_rows(plat):
    one = 1
    return [
        vg_row("Màn danh sách", [("Đủ: tiêu đề · phụ đề · 3 hành động (2 nút + ⋯)", PH_LIST),
                                 ("Chỉ tiêu đề + một nút", page_header("Tuyến", "", [("Thêm tuyến", "plus", "pri")])),
                                 ("Không hành động", page_header("Báo cáo chuyến", "Tháng 10/2026"))], one, "D1 · D4"),
        vg_row("Màn chi tiết", [("Trạng thái + hàng meta + 4 hành động + tab trong Page header", page_header("LVT-2026-0412", "", ACT_DET, pill("Đang chạy"), FIELDS, META, ("fi", "truck"), tab_html=tabs(DTABS))),
                                ("Avatar + hàng meta", PH_DRV),
                                ("Không tab", PH_DET)], one, "D2 A · D6 A · D7"),
        vg_row("Thanh gọn khi cuộn", [("Tiêu đề + trạng thái + nút chính + tab", '<div style="position:relative;padding-top:var(--space-xl)">'
                                       + page_sticky("LVT-2026-0412", pill("Đang chạy"), ("Hoàn tất chuyến", "checkc"), tabs(DTABS)).replace('data-show="state:scrolled"', "") + "</div>")], one, "D5"),
        vg_row("Đang tải", [("Khung xương tiêu đề", page_header("x", "", ACT_LIST).replace('data-hide="loading" class="ph-mm"', 'class="ph-mm" style="display:none"').replace('data-show="state:loading"', ""))], one, ""),
        vg_row("Chữ dài", [("Tiêu đề, hàng meta dài — xuống dòng", page_header("LVT-2026-0412 · Hàng lạnh tạm nhập tái xuất qua cửa khẩu Mộc Bài", "", ACT_DET, pill("Đang chạy"), FIELDS_LONG,
                                                                              ["Tạo 03/11 08:12 bởi Điều phối ca sáng chi nhánh Cát Lái", "Cập nhật 08:45 bởi Nguyễn Thị Phương Thảo", "Ưu tiên: Cao"])
                                                               .replace("<h1>", '<h1 style="white-space:normal">'))], one, ""),
    ]


def variants(plat):
    return vg(var_rows(plat))


screens = [
 {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "width": 1280, "heading": False, "crumb": "Điều phối", "title": "Lệnh vận tải", "nav": "Điều phối",
  "note": "Page header màn danh sách (D1, D4). Đã cuộn / Đang tải / Chữ dài ở Bảng chọn.", "html": S_LIST},
 {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "heading": False, "crumb": "Lệnh vận tải", "title": "LVT-2026-0412", "nav": "Điều phối",
  "top": SEC.format(tabs(DTABS)), "note": "Page header chi tiết theo tổ hợp chốt: trạng thái + hàng meta (D2 A), ≤ 2 nút + ⋯ (D4), tab nằm trong Page header dưới tiêu đề (D6 A — Header nav sẽ bỏ Secondary Nav). Đã cuộn → thanh dính (D5).", "html": S_DETAIL},
 {"id": "driver-web", "name": "Hồ sơ lái xe", "device": "web", "width": 1280, "heading": False, "crumb": "Lái xe", "title": "Trần Văn Bình", "nav": "Lái xe",
  "note": "Avatar đầu tiêu đề (D7).", "html": S_DRIVER},
 {"id": "settings-web", "name": "Cài đặt tham số", "device": "web", "width": 1280, "heading": False, "crumb": "Quản trị", "title": "Cài đặt", "nav": "Tổng quan",
  "note": "Page header màn form: nút Lưu ở đầu trang.", "html": S_SETTINGS},
 {"id": "list-app", "name": "Lệnh của tôi", "device": "mobile", "title": "Lệnh của tôi", "nav": "Lệnh", "note": "Tiêu đề lớn (D9). Đã cuộn → tiêu đề lên thanh trên.", "html": S_APP_LIST},
 {"id": "detail-app", "name": "Chi tiết chuyến", "device": "mobile", "title": "LVT-2026-0412", "nav": "Lệnh", "back": True, "note": "Chi tiết app: trạng thái + 4 trường + ⋯.", "html": S_APP_DET},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none", "note": "Danh sách, chi tiết, thanh gọn, đang tải, chữ dài.", "html": variants("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app.", "html": variants("mobile")},
]

PICK = {**REC, "D2": "a", "D6": "a", "D8": "b"}  # user chốt 04/11 08:12
PA = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())
preview = {
 "version": 1, "pick": PICK,
 "changes": "Bản 04/11 theo tổ hợp anh chốt: Simple (title-1 24 + phụ đề + gạch), HÀNG META CHỮ dưới tiêu đề (D2 A), không nút quay lại, ≤ 2 nút + ⋯, "
            "thanh gọn dính khi cuộn, TAB NẰM TRONG PAGE HEADER dưới tiêu đề (D6 A — kéo theo sửa Header navigation: bỏ Secondary Nav), avatar/icon tuỳ chọn, "
            "KHÔNG chuyển bản ghi ‹ › (D8 B), app tiêu đề lớn thu khi cuộn.",
 "blocks": [
  {"title": "Web", "platform": "web", "note": "Danh sách (3 cấu hình) · chi tiết (tab trong header, avatar, không tab) · thanh gọn · đang tải · chữ dài",
   "html": f'<div class="pv pvp" {PA} data-platform="web" data-state="x">{variants("web")}</div>'},
  {"title": "Mobile (app)", "platform": "mobile", "note": "Tiêu đề lớn title-1 24 trong nội dung, hành động vào ⋯ (vùng chạm 44), hàng meta xuống dòng",
   "frames": [f'<div class="pv pvp" {PA} data-platform="mobile" data-state="x">{vg([r])}</div>' for r in var_rows("mobile")]},
 ],
}
VALUES = [
 {"part": "Page header", "prop": "gap", "value": 20, "platform": "Web", "sel": ".phd"},
 {"part": "Page header", "prop": "padding-bottom", "value": 20, "platform": "Web", "sel": ".phd"},
 {"part": "Page header · gạch dưới", "prop": "border-width", "value": 1, "role": "decorative", "sel": ".phd", "cssProp": "border-bottom", "tpl": "$ solid var(--color-border-secondary)"},
 {"part": "Page header · gạch dưới", "prop": "color", "role": "decorative", "tokenRole": "border", "value": "#E5E5E5", "on": "#FFFFFF", "noOverride": "màu trong border-bottom", "at": ".phd"},
 {"part": "Hàng tiêu đề", "prop": "gap", "value": 16, "sel": ".ph-r"},
 {"part": "Tiêu đề", "prop": "font-size", "value": 24, "sel": ".ph-t h1", "cssProp": "font", "tpl": "400 $/var(--type-title-1-line-height) var(--font-title)"},
 {"part": "Tiêu đề", "prop": "color", "role": "text", "value": "#171717", "on": "#FFFFFF", "noOverride": "kế thừa màu chữ trang", "at": ".ph-t h1"},
 {"part": "Tiêu đề + trạng thái", "prop": "gap", "value": 12, "sel": ".ph-t"},
 {"part": "Phụ đề", "prop": "font-size", "value": 14, "sel": ".ph-s", "cssProp": "font", "tpl": "400 $/var(--type-body-line-height) var(--font-body)"},
 {"part": "Phụ đề", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "sel": ".ph-s"},
 {"part": "Hàng meta", "prop": "color", "role": "text", "value": "#737373", "on": "#FFFFFF", "sel": ".ph-meta"},
 {"part": "Hàng meta", "prop": "gap-x", "value": 12, "sel": ".ph-meta", "cssProp": "gap", "tpl": "var(--space-xs) $"},
 {"part": "Cụm hành động", "prop": "gap", "value": 12, "platform": "Web", "sel": ".ph-a"},
 {"part": "Ảnh / icon đầu tiêu đề · 2 dòng", "prop": "size", "value": 56, "platform": "Web", "sel": ".phd.has2 .ph-ld.fi,.phd.has2 .ph-ld .av", "cssProp": ["width", "height"]},
 {"part": "Ảnh / icon đầu tiêu đề · 1 dòng", "prop": "size", "value": 32, "sel": ".phd .ph-ld.fi,.phd .ph-ld .av", "cssProp": ["width", "height"]},
 {"part": "Thanh gọn", "prop": "padding-top", "value": 12, "platform": "Web", "sel": ".ph-st", "cssProp": "padding", "tpl": "$ var(--container-padding-desktop) 0"},
 {"part": "Thanh gọn · tiêu đề", "prop": "font-size", "value": 16, "sel": ".ph-st-r b", "cssProp": "font", "tpl": "600 $/var(--type-body-lg-line-height) var(--font-body)"},
 {"part": "Thanh gọn · hàng", "prop": "padding-bottom", "value": 12, "sel": ".ph-st-r"},
 {"part": "Page header app", "prop": "padding-bottom", "value": 16, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .phd"},
 {"part": "Nút ⋯ app", "prop": "size", "value": 44, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .ph-am", "cssProp": ["width", "height"], "interactive": True, "hitArea": 44},
]

page = {
 "component": "Page header", "slug": "page-header", "title": "Page header Review",
 "subtitle": "Application component · vòng 2 Preview (04/11) — tổ hợp đã chốt, màn demo khoá theo lựa chọn, bảng biến thể Web/Mobile. Số đo, chữ, màu theo foundation đã chốt.",
 "round": "preview", "preview": preview, "values": VALUES, "tokenFamilies": ["page-header", "featured-icon", "control", "layout"],
 "refs": {
  "untitled": {"summary": "6 kiểu: <mark>Simple</mark>, <mark>Avatar</mark>, Banner simple, Banner centered, Banner avatar, Banner avatar centered. Đường dẫn + tiêu đề + phụ đề + nút chính phải; mobile nút xuống dưới tiêu đề. Không có tab, ô tìm, nút quay lại.",
               "source": "untitledui.com/components/page-headers"},
  "astryx": {"summary": "P7: Back link + H1 + hàng meta (badge trạng thái, người, ngày) + hành động phải → Tabs. Header navigation (đã duyệt): đường dẫn trên thanh trên, Page header không lặp (DEC-291); Layout Secondary Nav có hàng tab dưới thanh.",
             "source": "design/design.md › P7 · header-navigation.md"},
  "usage": ["Mọi màn danh sách: Lệnh vận tải, Xe, Lái xe, Khách hàng", "Màn chi tiết bản ghi (P7): lệnh, lái xe, xe", "Màn form / cài đặt: nút Lưu ở đầu",
            "App lái xe: Lệnh của tôi, Chi tiết chuyến"],
  "platform": "Nhóm B nếu D9 = A (app đổi cấu tạo: tiêu đề lớn trong nội dung + thanh Mobile header) — trục Platform. Web màn hẹp: hành động vào ⋯."},
 "css": CSS_PH + OPT_PH, "cssScreen": ALL_CSS + CSS_SCREEN,
 "states": [{"key": "default", "label": "Mặc định"}, {"key": "scrolled", "label": "Đã cuộn"}, {"key": "loading", "label": "Đang tải"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": ".ph-st", "state": "default"}],
 "protoHint": "chọn “Đã cuộn” ở Bảng chọn để xem thanh dính; bấm thanh dính để về đầu trang",
}
write(OUT, page, decisions, brief=False)
