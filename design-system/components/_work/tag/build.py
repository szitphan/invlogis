#!/usr/bin/env python3
"""Sinh page.json cho Tag (vòng 1 Brainstorm).
Chạy: python3 design-system/components/_work/tag/build.py && python3 _scripts/ds-component-page.py tag
Đầu vào đã chốt: thẻ Tag trên trang Chốt biến thể Base (artifact VQDsMrBW37W3QWVTPN79qC, db variants/tag v2, 26/10):
Leading None · Dot · Avatar · Checkbox · Flag × Size SM MD LG × State Default · Hover · Focus · Disabled × Trailing None · Count · X Close.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_forms"))
from kit import CSS, SCREEN_CSS, av, cb, dot, flag, ic, mini, vg, vg_row, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"


def tag(label, lead=None, trail=None, size="md", st="", count=None, on=False, live=False, long=None):
    """lead: None | ('dot', màu) | ('avatar', i) | 'checkbox' | ('flag', mã). trail: None | 'count' | 'x'."""
    L = ""
    if isinstance(lead, tuple) and lead[0] == "dot":
        L = dot(lead[1])
    elif isinstance(lead, tuple) and lead[0] == "avatar":
        L = av(lead[1], 16)
    elif lead == "checkbox":
        L = cb(on)
    elif isinstance(lead, tuple) and lead[0] == "flag":
        L = flag(lead[1]).replace('width="18" height="13"', 'width="16" height="12"')
    T = ""
    if trail == "count":
        T = f'<span class="ct">{count}</span>'
    elif trail == "x":
        T = f'<button class="x touch-target" aria-label="Bỏ {label}">{ic("x", 12, "i xi")}</button>'
    lab = f'<span class="tl nl">{label}</span>'
    if long:
        lab += f'<span class="tl" data-show="state:long">{long}</span>'
    cls = f'tg t-{size} {st}{" on" if on else ""}{" ck" if lead == "checkbox" else ""}'
    return f'<span class="{cls}"{" data-cmp" if not live else " data-cmp data-live"}>{L}{lab}{T}</span>'


CSS_TAG = r"""
.pv[data-state=long] [data-live] .nl{display:none}
.pv[data-state=hover] [data-live].tg{background:var(--color-bg-primary_hover);border-color:var(--color-border-input)}
.pv[data-state=focus] [data-live].tg{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.pv[data-state=disabled] [data-live].tg{opacity:.5}
.tg.t-sm .cbx{width:12px;height:12px}.tg.t-lg .cbx{width:16px;height:16px}
.tg.t-lg .av{width:20px!important;height:20px!important}
.tg.ck{cursor:pointer}
/* D1 bo */
.pv[data-D1=b] .tg{border-radius:999px}
.pv[data-D1=b] .tg.t-sm{padding:0 8px}.pv[data-D1=b] .tg .ct{border-radius:999px}
/* D2 tag checkbox đã chọn */
.pv[data-D2=b] .tg.ck.on{border-color:var(--color-accent-border);background:var(--color-bg-selected);color:var(--color-text-primary)}
/* D3 count */
.pv[data-D3=b] .tg .ct{background:none;padding:0;color:var(--color-text-tertiary);font-weight:500}
.pv[data-D3=b] .tg .ct::before{content:"·";margin-right:4px}
/* D4 nút x */
.pv[data-D4=b] .tg .x{background:var(--color-bg-tertiary);border-radius:50%;padding:2px;color:var(--color-text-tertiary)}
/* D5 app chạm */
.pv[data-platform=mobile][data-D5=b] :is(.tg.ck,.tg:has(.x)){--th:32px;padding:0 12px;font-size:14px;gap:6px}
.pv[data-platform=mobile][data-D5=b] .tg .x{padding:4px;margin-right:-6px}
.pv[data-platform=mobile][data-D5=a] .tg .x{position:relative}

/* D6 nền */
.pv[data-D6=b] .tg{background:var(--color-bg-tertiary);border-color:transparent}
.pv[data-D6=b] .tg .ct{background:var(--color-bg-primary)}
.pv[data-D6=b] .tg.is-hover{background:var(--color-border-secondary)}
.tags{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.hscroll{display:flex;gap:8px;overflow:auto;padding-bottom:2px}.hscroll .tg{flex:none;max-width:none}
.tg.mw140{max-width:140px}
"""

# ---------- điểm cần quyết ----------
def m(over, inner, w=420, plat="web"):
    base = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "state": "x"}
    return mini(over and {**base, **over} or base, inner, w, plat)


def row(*t):
    return '<div class="tags">' + "".join(t) + "</div>"


SET = row(tag("Hàng lạnh", ("dot", "blue")), tag("Khách: Delta Logistics", trail="x"), tag("Đang chạy", "checkbox", "count", count=12, on=True),
          tag("Trần Văn Bình", ("avatar", 0), "x"), tag("Campuchia", ("flag", "KH")))
CK = row(tag("Đang chạy", "checkbox", "count", count=12, on=True), tag("Chờ xe", "checkbox", "count", count=5), tag("Trễ hẹn", "checkbox", "count", count=3, on=True))
CNT = row(tag("Đang chạy", trail="count", count=12), tag("Chờ xe", "checkbox", "count", count=5, on=True), tag("Hoàn tất", trail="count", count=128))
XS = row(tag("Khách: Delta Logistics", trail="x"), tag("Cảng: Cát Lái", trail="x", st="is-hover"), tag("Trần Văn Bình", ("avatar", 0), "x"))
APP = row(tag("Đang chạy", "checkbox", "count", count=12, on=True), tag("Chờ xe", "checkbox", "count", count=5), tag("Cát Lái", trail="x"))

decisions = [
 {"id": "D1", "title": "Bo góc",
  "why": "Status Chip (DEC-200) đã là hình viên thuốc. Tag là nhãn người dùng gắn, lọc, xoá được — nếu cùng hình viên thuốc thì dễ nhầm với trạng thái nghiệp vụ.",
  "source": "DEC-200 Status Chip · Untitled tags rounded-md",
  "options": [
   {"label": "Bo 6 (Untitled)", "desc": "Tách hẳn với Status Chip; nhìn ra ngay là thứ bấm/xoá được.", "rec": True, "preview": m({"D1": "a"}, SET), "ideas": ["I1", "I3", "I6"]},
   {"label": "Viên thuốc (Astryx Token)", "desc": "Mềm, quen trên app; trùng hình với Status Chip.", "preview": m({"D1": "b"}, SET), "ideas": ["I2", "I4", "I7"]}],
  "untitled": m({"D1": "a"}, SET), "astryx": m({"D1": "b"}, SET), "astryxNote": "Token bo tròn hoàn toàn"},
 {"id": "D2", "title": "Tag có ô chọn — lúc đã chọn",
  "why": "Leading Checkbox dùng làm bộ lọc nhanh (Đang chạy 12 · Chờ xe 5). Chỉ đổi ô tick thì nhóm tag đã chọn khó thấy khi lướt.",
  "source": "variants/tag Leading Checkbox",
  "options": [
   {"label": "Chỉ đổi ô tick", "desc": "Đúng Untitled; tag nhìn giống nhau, phải soi ô tick.", "preview": m({"D2": "a"}, CK), "ideas": ["I1"]},
   {"label": "Ô tick + viền đậm + nền nhạt", "desc": "Đã chọn nổi lên cả khi nhìn lướt; không dựa riêng vào màu (có ô tick).", "rec": True, "preview": m({"D2": "b"}, CK), "ideas": ["I5", "I8"]}],
  "untitled": m({"D2": "a"}, CK), "astryx": m({"D2": "b"}, CK), "astryxNote": "MultiSelector Labels"},
 {"id": "D3", "title": "Số đếm (Count)",
  "why": "Trailing Count cho tag lọc. Số cần đọc được nhưng không lấn nhãn.",
  "source": "variants/tag Trailing Count",
  "options": [
   {"label": "Số trong ô nền xám (Untitled)", "desc": "Tách rõ nhãn và số; tag rộng hơn 6–8px.", "rec": True, "preview": m({"D3": "a"}, CNT), "ideas": ["I1", "I5"]},
   {"label": "Số chữ phụ sau dấu ·", "desc": "Gọn; số lẫn vào nhãn khi nhãn có số (Kho 3 · 12).", "preview": m({"D3": "b"}, CNT), "ideas": ["I4"]}],
  "untitled": m({"D3": "a"}, CNT), "astryx": m({"D3": "b"}, CNT), "astryxNote": "Astryx Token không có count"},
 {"id": "D4", "title": "Nút xoá ×",
  "why": "Trailing X Close bỏ một điều kiện lọc hoặc một người khỏi danh sách.",
  "source": "variants/tag Trailing X Close",
  "options": [
   {"label": "× trơn, hiện nền khi rê", "desc": "Nhẹ, không lấn nhãn.", "rec": True, "preview": m({"D4": "a"}, XS), "ideas": ["I1", "I3"]},
   {"label": "× trong vòng tròn nền xám", "desc": "Luôn thấy là nút; nặng khi có nhiều tag.", "preview": m({"D4": "b"}, XS), "ideas": ["I2", "I7"]}],
  "untitled": m({"D4": "a"}, XS), "astryx": m({"D4": "b"}, XS)},
 {"id": "D5", "title": "App: cỡ tag và vùng chạm",
  "why": "Tag MD cao 24, nút × 16 — dưới vùng chạm 44 (foundations Mục 9). Trang chốt biến thể ghi mobile “same”.",
  "source": "foundations Mục 9 · variants/tag mobile same",
  "options": [
   {"label": "Giữ cỡ web, nới vùng chạm vô hình", "desc": "Hàng tag gọn như web; tag sát nhau dễ bấm nhầm.", "preview": m({"D5": "a"}, APP, 360, "mobile"), "ideas": ["I1"]},
   {"label": "App cao 32, chữ 14, × lớn hơn", "desc": "Bấm chắc tay ngoài hiện trường; hàng lọc cuộn ngang.", "rec": True, "preview": m({"D5": "b"}, APP, 360, "mobile"), "ideas": ["I7", "I8"]}],
  "untitled": m({"D5": "a"}, APP, 360, "mobile"), "astryx": m({"D5": "b"}, APP, 360, "mobile")},
 {"id": "D6", "title": "Nền tag",
  "why": "Tag nằm trong ô Input Tags, trong bảng, trên thẻ app. Nền trắng có viền đọc rõ trên nền trắng; nền xám nhẹ hơn khi tag dày đặc.",
  "source": "Untitled tags · DEC-258 (nền trang trắng)",
  "options": [
   {"label": "Trắng + viền (Untitled)", "desc": "Rõ là phần tử bấm được; hợp nền trắng của DS v2.", "rec": True, "preview": m({"D6": "a"}, SET), "ideas": ["I1", "I6"]},
   {"label": "Xám nhạt, không viền", "desc": "Nhẹ trong bảng nhiều tag; trên thẻ xám (bg/secondary) thì mất ranh giới.", "preview": m({"D6": "b"}, SET), "ideas": ["I2", "I4"]}],
  "untitled": m({"D6": "a"}, SET), "astryx": m({"D6": "b"}, SET)},
]

ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/react/components/tags", "title": "Untitled UI — Tags",
  "why": "Bo 6, viền, 3 cỡ; đầu tag có checkbox/dot/avatar/cờ, cuối có số đếm nền xám hoặc ×.", "pv": SET},
 {"id": "I2", "source": "Material 3", "url": "https://m3.material.io/components/chips/overview", "title": "Material 3 — Input & filter chips",
  "why": "Chip lọc viên thuốc, đã chọn có dấu ✓ và nền nhấn; chip nhập có × tròn.", "pv": CK},
 {"id": "I3", "source": "Atlassian", "url": "https://atlassian.design/components/tag/examples", "title": "Atlassian — Tag",
  "why": "Tag vuông nhỏ, × trơn chỉ nổi khi rê; tag có avatar cho người.", "pv": XS},
 {"id": "I4", "source": "Ant Design", "url": "https://ant.design/components/tag", "title": "Ant Design — Tag / CheckableTag",
  "why": "Tag nền xám không viền, CheckableTag đổi nền khi chọn; số đếm là chữ thường.", "pv": CNT},
 {"id": "I5", "source": "Linear", "url": "https://linear.app/docs/filters", "title": "Linear — thanh lọc",
  "why": "Điều kiện lọc là tag có số đếm, tag đã chọn viền đậm — lướt là thấy đang lọc gì.", "pv": CK},
 {"id": "I6", "source": "GitHub Primer", "url": "https://primer.style/components/label", "title": "Primer — Label / Token",
  "why": "Token viền mảnh nền trắng, có avatar người dùng, × khi rê.", "pv": XS},
 {"id": "I7", "source": "Apple HIG", "url": "https://developer.apple.com/design/human-interface-guidelines/buttons", "title": "Apple HIG — nút cỡ chạm",
  "why": "Phần tử bấm trên iOS ≥ 44pt — tag lọc app cao hơn, × lớn hơn.", "pv": APP, "plat": "mobile"},
 {"id": "I8", "source": "Grab Driver", "url": "https://www.grab.com/vn/driver/", "title": "Ứng dụng tài xế — lọc cuốc",
  "why": "Bộ lọc là hàng tag cao cuộn ngang, đã chọn đổi nền rõ — dùng một tay khi đứng xe.", "pv": APP, "plat": "mobile"},
]
for i in ideas:
    plat = i.pop("plat", "web")
    i["preview"] = m(None, i.pop("pv"), 380 if plat == "web" else 340, plat)

REC = {d["id"]: chr(97 + next(k for k, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC},
           {"id": "untitled", "label": "Untitled UI", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a"}},
           {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "b", "D2": "b", "D3": "b", "D4": "b", "D5": "b", "D6": "b"}}]
for i in ideas:
    pk = {**REC}
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pk[d["id"]] = chr(97 + k)
    presets.append({"id": i["id"], "label": f'{i["id"]} · {i["source"]}', "pick": pk})

# ---------- màn ----------
ORDERS = [("LVT-2026-0412", "Delta Logistics", "Cát Lái → Sóng Thần", [tag("Hàng lạnh", ("dot", "blue"), size="sm"), tag("Dễ vỡ", ("dot", "yellow"), size="sm")], "Đang chạy", "ok"),
          ("LVT-2026-0415", "Tân Cảng Logistics", "Cát Lái → Phnom Penh", [tag("Campuchia", ("flag", "KH"), size="sm"), tag("Tạm nhập tái xuất", size="sm")], "Chờ xe", "wa"),
          ("LVT-2026-0419", "An Phát Trading", "ICD Phước Long → Bình Dương", [tag("Hàng nguy hiểm loại 3", ("dot", "red"), size="sm"), tag("+2", size="sm")], "Trễ hẹn", "er"),
          ("LVT-2026-0421", "Delta Logistics", "Hiệp Phước → Long An", [tag("Giao giờ hành chính", size="sm")], "Đang chạy", "ok")]
TABLE = ('<div class="tb"><table><tr><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Nhãn hàng</th><th>Trạng thái</th></tr>'
         + "".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td>{c}</td><td><div class="tags">{"".join(t)}</div></td><td><span class="chip {k}">{s}</span></td></tr>'
                   for a, b, c, t, s, k in ORDERS) + "</table></div>")
S_LIST = ('<div class="pad"><div class="bar">'
          + tag("Đang chạy", "checkbox", "count", count=12, on=True) + tag("Chờ xe", "checkbox", "count", count=5) + tag("Trễ hẹn", "checkbox", "count", count=3, on=True)
          + '<span style="width:1px;height:20px;background:var(--color-border-secondary);margin:0 4px"></span>'
          + tag("Khách: Delta Logistics", trail="x", live=True, long="Khách: Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics chi nhánh Cát Lái")
          + tag("Cảng: Cát Lái", trail="x") + '<button class="bt ghost" style="height:24px;font-size:12.5px">Xoá lọc</button></div>'
          + TABLE + "</div>")
S_DRIVER = ('<div class="pad"><div class="grid2"><div class="card"><div class="h">Lái xe phụ trách tuyến</div><div class="tags">'
            + tag("Trần Văn Bình", ("avatar", 0), "x", size="lg") + tag("Lê Thị Hoa", ("avatar", 1), "x", size="lg")
            + tag("Phạm Quốc Dũng", ("avatar", 2), "x", size="lg", live=True, long="Phạm Quốc Dũng (lái xe dự phòng ca đêm, tuyến Cát Lái – Phnom Penh)")
            + '<button class="bt" style="height:28px;font-size:12.5px">' + ic("plus", 14) + 'Thêm lái xe</button></div></div>'
            '<div class="card"><div class="h">Nước đi qua</div><div class="tags">'
            + tag("Việt Nam", ("flag", "VN"), size="lg") + tag("Campuchia", ("flag", "KH"), "x", size="lg") + tag("Lào", ("flag", "LA"), "x", size="lg", st="is-dis")
            + '</div><div class="hn" style="color:var(--color-text-tertiary);font-size:12.5px">Lào tạm ngưng nhận hàng quá cảnh — không bỏ được.</div></div>'
            '<div class="card span2"><div class="h">Nhãn của tuyến</div><div class="tags">'
            + "".join(tag(t, ("dot", c)) for t, c in (("Hàng lạnh", "blue"), ("Dễ vỡ", "yellow"), ("Hàng nguy hiểm loại 3", "red"), ("Ưu tiên", "purple"), ("Giao giờ hành chính", "gray")))
            + "</div></div></div></div>")
MCARD = lambda code, route, tags, s, k: (f'<div class="mcard"><div style="display:flex;justify-content:space-between;align-items:center"><b class="mono" style="font-size:14px">{code}</b>'
                                         f'<span class="chip {k}">{s}</span></div><span class="s">{route}</span><div class="tags">{"".join(tags)}</div></div>')
S_APP = ('<div class="mpad"><div class="hscroll">'
         + tag("Đang chạy", "checkbox", "count", count=12, on=True, live=True, long="Đang chạy trên tuyến quốc tế")
         + tag("Chờ xe", "checkbox", "count", count=5) + tag("Trễ hẹn", "checkbox", "count", count=3) + tag("Hoàn tất", "checkbox", "count", count=128) + '</div>'
         + "".join(MCARD(a, c, t, s, k) for a, b, c, t, s, k in ORDERS[:3]) + "</div>")

STS = [("Default", ""), ("Hover", "is-hover"), ("Focus", "is-focus"), ("Disabled", "is-dis")]
LEADS = [("None", None), ("Dot", ("dot", "blue")), ("Avatar", ("avatar", 0)), ("Checkbox", "checkbox"), ("Flag", ("flag", "VN"))]
LAB = {"None": "Hàng lạnh", "Dot": "Hàng lạnh", "Avatar": "Trần Văn Bình", "Checkbox": "Đang chạy", "Flag": "Việt Nam"}


def g(plat):
    rows = []
    for size in ("SM", "MD", "LG"):
        cells = []
        for ln, ld in LEADS:
            cells.append((ln, '<div class="tags" style="flex-direction:column;align-items:flex-start">'
                          + "".join(tag(LAB[ln], ld, tr, size.lower(), count=12, on=ln == "Checkbox") for tr in (None, "count", "x")) + "</div>"))
        rows.append(vg_row(f"Size {size} · Leading × Trailing", cells, 5 if plat == "web" else 2, "mỗi ô: Trailing None · Count · X Close"))
    rows.append(vg_row("State", [(n, tag("Hàng lạnh", ("dot", "blue"), "x", st=s)) for n, s in STS], 4 if plat == "web" else 2))
    rows.append(vg_row("Checkbox — chưa chọn / đã chọn", [("Chưa chọn", tag("Chờ xe", "checkbox", "count", count=5)), ("Đã chọn", tag("Đang chạy", "checkbox", "count", count=12, on=True))], 2))
    rows.append(vg_row("Chữ dài — 1 dòng, cắt …, rộng tối đa 200", [("Nhãn dài + ×", tag("Khách: Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics", trail="x")),
                                                                    ("Tên người dài", tag("Nguyễn Thị Phương Thảo Nguyên", ("avatar", 3), "x"))], 2, "DEC-261"))
    return vg(rows)


screens = [
 {"id": "list-web", "name": "Danh sách lệnh", "device": "web", "title": "Lệnh vận tải", "crumb": "Điều phối",
  "note": "Hàng lọc (Checkbox + Count, X Close) và nhãn trong bảng (Dot, Flag). Tag “Khách: Delta Logistics” nhận trạng thái ở Bảng chọn.", "html": S_LIST},
 {"id": "route-web", "name": "Hồ sơ tuyến", "device": "web", "title": "Tuyến Cát Lái – Phnom Penh", "crumb": "Tuyến", "nav": "Điều phối",
  "note": "Tag Avatar (lái xe), Flag (nước đi qua), Dot (nhãn) — cỡ LG.", "html": S_DRIVER},
 {"id": "list-app", "name": "Danh sách lệnh", "device": "mobile", "title": "Lệnh của tôi", "nav": "Lệnh", "note": "Hàng lọc cuộn ngang + nhãn trên thẻ.", "html": S_APP},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "shell": "none", "note": "Leading 5 × Trailing 3 × Size 3, State 4, chữ dài.", "html": g("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Cùng bộ trên app — D5 đổi cỡ app.", "html": g("mobile")},
]

page = {
 "component": "Tag", "slug": "tag", "title": "Tag Review",
 "subtitle": "Base component · vòng 1 Brainstorm — biến thể đã chốt (Leading 5 · Size 3 · State 4 · Trailing 3). Trang này chỉ hỏi chi tiết hình.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Bo <mark>rounded-md</mark> (6), viền gray-300, 3 cỡ sm 22 · md 24 · lg 28; đầu có checkbox, dot, avatar, cờ; cuối có số đếm nền xám hoặc nút ×.",
               "source": "design/_ref/untitled-ui/react/components/base/tags/"},
  "astryx": {"summary": "Token — tag có thể xoá, 11 màu categorical, bo tròn hoàn toàn, một cỡ, không có số đếm.", "source": "design/design.md › Token · Feedback & Status"},
  "usage": ["Điều phối · danh sách lệnh · hàng lọc nhanh", "Lệnh vận tải · nhãn hàng (lạnh, nguy hiểm, dễ vỡ)", "Tuyến quốc tế · nước đi qua (cờ)", "Ô Input Type Tags, Multiselect Hiển thị Tags"],
  "platform": "Nhóm A — một bộ, cỡ theo Platform. D5 hỏi cỡ app vì vùng chạm."},
 "css": CSS + CSS_TAG, "cssScreen": SCREEN_CSS,
 "states": [{"key": "default", "label": "Mặc định"}, {"key": "hover", "label": "Hover"}, {"key": "focus", "label": "Focus"},
            {"key": "disabled", "label": "Tắt"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": "[data-live].tg", "state": "focus", "toggle": True}],
 "protoHint": "bấm vào tag đang thử để focus",
}

write(OUT, page, decisions)
