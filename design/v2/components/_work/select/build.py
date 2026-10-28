#!/usr/bin/env python3
"""Sinh page.json cho Select (vòng 1 Brainstorm).
Chạy: python3 design/v2/components/_work/select/build.py && python3 _scripts/ds-component-page.py select
Đầu vào đã chốt: thẻ Select trên trang Chốt biến thể Base (artifact VQDsMrBW37W3QWVTPN79qC, db variants/select v7, 26/10):
Type Default · Icon Leading · Avatar Leading · Dot Leading · Searchable · Native × Size SM MD LG × State 7 · Menu item 5 ·
Kèm theo Empty · Scrollbar · Bottom Sheet · mobile split. Ghi chú user: thiếu option nhiều thông tin (mã lệnh SC, xe + lái xe,
icon loại SC; nhân viên: mã NV, chức vụ) → điểm D2, D3.
Focus của ô theo Input D1 (chốt một lần cho cả họ form) — không hỏi lại ở đây.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_forms"))
from kit import CSS, SCREEN_CSS, av, dot, ic, mini, vg, vg_row, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"

# ---------- dữ liệu mẫu ----------
VEH = [  # biển số, loại xe, lái xe, trạng thái, tông
    ("51C-482.19", "Đầu kéo Hino 2 trục", "Trần Văn Bình", "Sẵn sàng", "ok"),
    ("51C-517.03", "Đầu kéo Hyundai Xcient", "Lê Thị Hoa", "Sẵn sàng", "ok"),
    ("51D-220.84", "Xe tải 8 tấn Isuzu", "Phạm Quốc Dũng", "Đang chạy", "wa"),
    ("61C-093.55", "Đầu kéo Hino 3 trục", "Nguyễn Minh Khoa", "Đang sửa", "er"),
    ("51C-604.71", "Đầu kéo Howo 2 trục", "Võ Thành Tâm", "Sẵn sàng", "ok"),
]
LSC = [("LSC-0930", "Thay lốp trục 2", "51C-482.19 · Gara Tân Thuận", "wrench", "Đang sửa", "wa"),
       ("LSC-0941", "Bảo dưỡng 40.000 km", "61C-093.55 · Xưởng Delta Bình Dương", "gear", "Chờ duyệt", ""),
       ("LSC-0952", "Sửa hệ thống phanh hơi", "51D-220.84 · Gara Hưng Thịnh", "wrench", "Hoàn tất", "ok")]
STAFF = [("NV-0142", "Trần Văn Bình", "Lái xe hạng FC · Đội 2", 0), ("NV-0217", "Lê Thị Hoa", "Điều phối viên · Kho Sóng Thần", 1),
         ("NV-0305", "Phạm Quốc Dũng", "Kỹ thuật viên · Xưởng Bình Dương", 2), ("NV-0388", "Nguyễn Minh Khoa", "Trưởng xưởng · Xưởng Bình Dương", 3)]
PORTS = ["Cảng Cát Lái", "Cảng Hiệp Phước", "ICD Phước Long", "ICD Sóng Thần", "Cảng Cái Mép (TCIT)", "Cảng Tân Vũ"]


# ---------- phần tử ----------
def lead_html(lead):
    if not lead:
        return ""
    k, v = lead
    if k == "icon":
        return f'<span class="ic">{ic(v)}</span>'
    if k == "avatar":
        return av(v, 22)
    if k == "dot":
        return dot(v)
    return ""


def trig(val=None, ph="Chọn…", lead=None, size="md", st="", search=False, rich=None, long=None, native=False):
    """Ô chọn. rich = (dòng 1, dòng 2) cho option nhiều thông tin."""
    L = lead_html(lead)
    if search:
        L = f'<span class="ic">{ic("search")}</span>'
    if rich:
        body = f'<div class="rv nl"><div class="rv1">{rich[0]}</div><div class="rv2">{rich[1]}</div></div>'
    else:
        body = f'<span class="v nl">{val}</span>' if val else f'<span class="ph nl">{ph}</span>'
    if long:
        body += f'<span class="v" data-show="state:long">{long}</span>'
    if search:
        body += '<span class="v tp" data-show="D5:a state:open">51C<i class="caret"></i></span><span class="v tp" data-show="D5:a state:empty">51Z<i class="caret"></i></span>'
    chev = ic("chev", 14 if native else 16)
    return f'<div class="ctl sel s-{size} {st}{" rich" if rich else ""}{" nat" if native else ""}">{L}{body}<span class="ic chev">{chev}</span></div>'


def field(label, c, req=False, hint=None, err=None, live=False, mob=False, extra=""):
    lb = f'<div class="lb">{label}{"<span class=req>*</span>" if req else ""}</div>' if label else ""
    foot = ""
    if err and not live:
        foot = f'<div class="fe">{ic("err", 14)}{err}</div>'
    elif hint:
        foot = f'<div class="hn{" nh" if live else ""}">{hint}</div>'
    if live and err:
        foot = f'<div class="fe" data-show="state:error">{ic("err", 14)}{err}</div>' + foot
    return f'<div class="f anchor{" m" if mob else ""}" data-cmp{" data-live" if live else ""}>{lb}{c}{foot}{extra}</div>'


def mi(label, sup=None, lead=None, sel=False, dis=False, hov=False):
    cls = "mi" + (" sel" if sel else "") + (" dis" if dis else "") + (" hov" if hov else "")
    s = f'<span class="ms">{sup}</span>' if sup else ""
    return (f'<div class="{cls}"><span class="rd{" on" if sel else ""}"></span>{lead_html(lead)}<span class="ml">{label}{s}</span>'
            f'<span class="ck">{ic("check") if sel else ""}</span></div>')


def ro(code, title, meta, icon=None, chip=None, tone="", sel=False, hov=False, avatar=None):
    ri = av(avatar, 32) if avatar is not None else f'<span class="ri">{ic(icon or "truck", 18)}</span>'
    ch = f'<span class="rr"><span class="chip {tone}">{chip}</span></span>' if chip else ""
    return (f'<div class="ro{" sel" if sel else ""}{" hov" if hov else ""}"><span class="rd{" on" if sel else ""}"></span>{ri}<div class="rm">'
            f'<div class="r1"><span class="code">{code}</span><span class="rt">{title}</span></div><div class="r2">{meta}</div></div>{ch}'
            f'<span class="ck">{ic("check") if sel else ""}</span></div>')


def menu(items, search=False, scroll=False, w=None):
    sr = f'<div class="msr" data-show="D5:b">{ic("search")}<span>Tìm biển số, lái xe…</span></div>' if search else ""
    sb = '<span class="scb"></span>' if scroll else ""
    st = f' style="width:{w}px"' if w else ""
    return f'<div class="mn"{st}>{sr}{"".join(items)}{sb}</div>'


def veh_ro(i, sel=False, hov=False):
    p, t, d, s, k = VEH[i]
    return ro(p, t, f"Lái xe: {d}", "truck", s, k, sel, hov)


VEH_MENU = [veh_ro(0, sel=True), veh_ro(1, hov=True), veh_ro(2), veh_ro(3), veh_ro(4)]
EMPTY = f'<div class="mem"><b>Không tìm thấy xe “51Z”</b>Thử biển số khác hoặc bỏ bớt ký tự.</div>'

# ---------- CSS ----------
CSS_SEL = r"""
.ctl.sel{cursor:pointer}
.ctl.sel .chev{margin-left:auto;color:var(--fg3)}
.pv[data-state=open] [data-live] .chev{transform:rotate(180deg)}
.pv[data-state=long] [data-live] .nl{display:none}
.pv[data-state=error] [data-live] .nh{display:none}
.pv[data-state=open][data-D5=a] [data-live]>.ctl:has(.tp) .nl,.pv[data-state=empty][data-D5=a] [data-live]>.ctl:has(.tp) .nl{display:none}
.pv[data-state=empty] [data-live]>.ctl{border-color:var(--focus);box-shadow:inset 0 0 0 1px var(--focus)}
.caret{display:inline-block;width:1px;height:16px;background:var(--fg);margin-left:1px;vertical-align:-3px}
.ctl .rv{flex:1;min-width:0}
.rv1,.rv2{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rv1{font-weight:500}.rv2{font-size:12.5px;line-height:16px;color:var(--fg3)}
.pv[data-D3=a] .rv2{display:none}
.pv[data-D3=b] .ctl.rich{padding-top:5px;padding-bottom:5px}
.pv[data-D3=b] .m .ctl.rich{padding-top:8px;padding-bottom:8px}
.ctl.nat{background:var(--bg2)}
.pop{min-width:100%}
.pv[data-D7=a] .pop{width:100%}
.pv[data-D7=b] .pop{width:max-content;max-width:480px}
.pop .mn{width:100%}
/* D1 dấu đã chọn */
.rd{display:none;width:16px;height:16px;border:1px solid var(--line2);border-radius:50%;flex:none;box-sizing:border-box}
.rd.on{border:5px solid var(--solid)}
.pv[data-D1=c] .rd{display:inline-block}.pv[data-D1=c] .mi .ck,.pv[data-D1=c] .ro .ck{display:none}
.pv[data-D1=b] .mi.sel,.pv[data-D1=b] .ro.sel{background:var(--sel)}
.pv[data-D1=c] .ro .rd{align-self:center}
/* D2 option nhiều thông tin */
.ro .rt{font-weight:500;color:var(--fg2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.pv[data-D2=a] .ro .ri,.pv[data-D2=a] .ro .rr,.pv[data-D2=a] .ro .av{display:none}
.pv[data-D2=b] .ro{align-items:center;padding:6px 8px}
.pv[data-D2=b] .ro .ri,.pv[data-D2=b] .ro .av{display:none}
.pv[data-D2=b] .ro .rm{display:flex;align-items:center;gap:12px}
.pv[data-D2=b] .ro .r1{flex:none;max-width:60%}
.pv[data-D2=b] .ro .r2{margin-left:auto;flex:1;text-align:right;min-width:0}
.pv[data-D2=b] .ro .rr{display:none}
.pv[data-D2=c] .ro .rr{align-self:center}
/* D4 chữ phụ */
.mi .ml .ms{font-weight:400}
.pv[data-D4=b] .mi:has(.ms){padding-top:6px;padding-bottom:6px}
.pv[data-D4=b] .mi .ml{white-space:normal}
.pv[data-D4=b] .mi .ms{display:block;margin:0;font-size:12.5px;line-height:16px}
/* app */
.fs{position:absolute;inset:0;background:var(--bg);z-index:9;display:flex;flex-direction:column}
.fs .fs-h{height:52px;display:flex;align-items:center;gap:8px;padding:44px 16px 0;box-sizing:content-box;font:600 17px Inter}
.fs .msr{margin:8px 16px;border:1px solid var(--line2);border-radius:12px;height:44px;padding:0 12px}
.fs .fs-b{flex:1;overflow:auto;padding:0 8px}
.fs .ro{padding:12px}
.whl{display:flex;flex-direction:column;align-items:center;padding:8px 0 16px;font:400 18px/40px Inter;color:var(--fg4)}
.whl .on{color:var(--fg);font-weight:500;background:var(--muted);border-radius:10px;width:calc(100% - 32px);text-align:center}
.mn.vgm{box-shadow:var(--shadow);max-height:none}
.sht.static,.fs.static{position:relative;border-radius:16px;max-height:none;box-shadow:none;border:1px solid var(--line)}
.fs.static .fs-h{padding-top:0}
"""


def m(over, inner, w=440, plat="web"):
    base = {"D1": "a", "D2": "c", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a", "state": "x"}
    return mini({**base, **(over or {})}, inner, w, plat)


def stack(*h):
    return '<div style="display:flex;flex-direction:column;gap:8px">' + "".join(h) + "</div>"


P_SEL = stack(field("Mức ưu tiên", trig("Cao", lead=("dot", "red"), st="is-open")), menu([mi("Khẩn", lead=("dot", "red")), mi("Cao", lead=("dot", "yellow"), sel=True), mi("Thường", lead=("dot", "gray"), hov=True), mi("Thấp", lead=("dot", "gray"), dis=True)]))
P_RICH = stack(field("Xe", trig(search=True, st="is-open", ph="Chọn xe")), menu([veh_ro(0, sel=True), veh_ro(1, hov=True), veh_ro(3)]))
P_SC = stack(menu([ro(*LSC[0][:4], LSC[0][4], LSC[0][5], sel=True), ro(*LSC[1][:4], LSC[1][4], LSC[1][5], hov=True)]),
             menu([ro(c, n, r, chip=None, avatar=a, sel=i == 0) for i, (c, n, r, a) in enumerate(STAFF[:2])]))
P_TRIG = stack(field("Xe", trig(rich=("51C-482.19 · Đầu kéo Hino 2 trục", "Lái xe: Trần Văn Bình"))),
               field("Lệnh sửa chữa", trig(rich=("LSC-0930 · Thay lốp trục 2", "51C-482.19 · Gara Tân Thuận"))))
P_SUP = menu([mi("Cảng Cát Lái", "Quận Thủ Đức, TP.HCM", sel=True), mi("Cảng Hiệp Phước", "Nhà Bè, TP.HCM", hov=True), mi("ICD Phước Long", "Thủ Đức, TP.HCM"), mi("Cảng Cái Mép (TCIT)", "Phú Mỹ, Bà Rịa – Vũng Tàu")])
P_SRCH = stack(field("Xe", trig(search=True, st="is-open", ph="Chọn xe").replace('data-show="D5:a state:open"', 'data-show="D5:a"')), menu([veh_ro(0), veh_ro(1, hov=True)], search=True))
SHEET = ('<div class="sht static"><i class="hd"></i><div class="sh-t">Chọn xe<span class="ic">' + ic("x", 20) + '</span></div>'
         '<div class="msr">' + ic("search") + '<span>Tìm biển số, lái xe…</span></div><div class="sh-b">' + veh_ro(0, sel=True) + veh_ro(1) + veh_ro(2) + "</div></div>")
FULL = ('<div class="fs static"><div class="fs-h">' + ic("chevr", 20).replace("M9 6l6 6-6 6", "M15 18l-6-6 6-6") + 'Chọn xe</div><div class="msr">' + ic("search")
        + '<span>Tìm biển số, lái xe…</span></div><div class="fs-b">' + veh_ro(0, sel=True) + veh_ro(1) + veh_ro(2) + "</div></div>")
WHEEL = ('<div class="sht static"><i class="hd"></i><div class="sh-t">Chọn xe<b style="font-size:15px">Xong</b></div><div class="whl">'
         '<span>51C-604.71</span><span class="on">51C-482.19</span><span>51C-517.03</span></div></div>')
WH = {"a": SHEET, "b": FULL, "c": WHEEL}
P_W = stack(field("Lệnh sửa chữa", trig("LSC-0930 · Thay lốp trục 2", st="is-open")),
            '<div class="mn" style="width:300px">' + "".join(mi(f"{c} · {n}", sel=i == 0) for i, (c, n, *_r) in enumerate(LSC)) + "</div>")

decisions = [
 {"id": "D1", "title": "Option đã chọn đánh dấu thế nào",
  "why": "Menu Item Selected đã chốt. Untitled: dấu ✓ bên phải. Có thêm nền nhạt thì dễ tìm lại lựa chọn trong danh sách dài.",
  "source": "variants/select Menu item Selected",
  "options": [
   {"label": "✓ bên phải (Untitled)", "desc": "Gọn; danh sách dài phải dò ✓.", "preview": m({"D1": "a"}, P_SEL), "ideas": ["I1", "I2"]},
   {"label": "Nền nhạt + ✓ bên phải", "desc": "Thấy ngay khi mở menu; nền chọn trùng nền rê chuột — chữ đậm để phân biệt.", "rec": True, "preview": m({"D1": "b"}, P_SEL), "ideas": ["I4", "I6"]},
   {"label": "Nút radio bên trái", "desc": "Rõ là chọn một; thêm cột trái, hợp bottom sheet app.", "preview": m({"D1": "c"}, P_SEL), "ideas": ["I3", "I7"]}],
  "untitled": m({"D1": "a"}, P_SEL), "astryx": m({"D1": "c"}, P_SEL), "astryxNote": "Selector mobile = RadioListItem"},
 {"id": "D2", "title": "Option nhiều thông tin (xe, lệnh sửa chữa, nhân viên)",
  "why": "User ghi ở trang chốt biến thể: thiếu case mỗi option 3–4 trường — mã lệnh SC, tên xe và lái xe, icon loại SC; nhân viên: mã NV, chức vụ. Chọn sai xe hoặc sai lệnh là lỗi nghiệp vụ, nên option phải đủ để phân biệt mà không mở chi tiết.",
  "source": "variants/select (ghi chú user 26/10) · LSC-0930 ở cross-process-flow-spec",
  "options": [
   {"label": "2 dòng: mã + tên / thông tin phụ", "desc": "Gọn, đọc từ trên xuống; không có icon loại, không có trạng thái.", "preview": m({"D2": "a"}, P_RICH), "ideas": ["I2", "I5"]},
   {"label": "1 dòng: mã + tên bên trái, phụ canh phải", "desc": "Menu ngắn, so được cột; menu phải rộng (D7) và dễ cắt chữ.", "preview": m({"D2": "b", "D7": "b"}, P_RICH), "ideas": ["I4"]},
   {"label": "Icon loại + 2 dòng + chip trạng thái", "desc": "Đủ 4 trường user nêu; thấy ngay xe đang sửa, đang chạy. Option cao 52.", "rec": True, "preview": m({"D2": "c"}, P_RICH), "ideas": ["I1", "I8"]}],
  "untitled": m({"D2": "a"}, P_RICH), "untitledNote": "Untitled: supporting text cùng dòng — không có mẫu 3–4 trường",
  "astryx": m({"D2": "c"}, P_SC), "astryxNote": "ComplexSelector (popup tự dựng) — đây là lệnh SC + nhân viên"},
 {"id": "D3", "title": "Ô sau khi chọn option nhiều thông tin",
  "why": "Chọn xong, ô hiện gì: chỉ dòng chính, hay giữ cả dòng phụ (lái xe, gara) để người duyệt khỏi mở lại menu.",
  "source": "variants/select State Filled",
  "options": [
   {"label": "1 dòng: mã + tên", "desc": "Ô giữ cao 32 như mọi ô khác trong form.", "rec": True, "preview": m({"D3": "a"}, P_TRIG), "ideas": ["I2", "I4"]},
   {"label": "2 dòng như option (ô cao ~44)", "desc": "Đủ thông tin; ô lệch chiều cao với ô bên cạnh trong lưới form.", "preview": m({"D3": "b"}, P_TRIG), "ideas": ["I8"]}],
  "untitled": m({"D3": "a"}, P_TRIG), "astryx": m({"D3": "a"}, P_TRIG)},
 {"id": "D4", "title": "Chữ phụ (Supporting) trong option",
  "why": "Menu item Supporting đã chốt — vd cảng kèm quận/tỉnh.",
  "source": "variants/select Menu item Supporting",
  "options": [
   {"label": "Cùng dòng, chữ xám (Untitled)", "desc": "Menu đều 36; tên dài thì chữ phụ bị cắt trước.", "rec": True, "preview": m({"D4": "a"}, P_SUP), "ideas": ["I1"]},
   {"label": "Dòng thứ hai", "desc": "Không mất chữ phụ; menu cao gần gấp đôi.", "preview": m({"D4": "b"}, P_SUP), "ideas": ["I3", "I6"]}],
  "untitled": m({"D4": "a"}, P_SUP), "astryx": m({"D4": "b"}, P_SUP)},
 {"id": "D5", "title": "Select có tìm (Searchable): gõ ở đâu",
  "why": "Danh sách xe, cảng, khách dài hàng trăm dòng. Gõ thẳng trong ô (combobox) nhanh; ô tìm đầu menu thì ô giữ nguyên giá trị đang chọn.",
  "source": "variants/select Type Searchable",
  "options": [
   {"label": "Gõ thẳng trong ô (Untitled combobox)", "desc": "Một chỗ để nhìn; giá trị cũ biến mất khi đang gõ.", "rec": True, "preview": m({"D5": "a"}, P_SRCH), "ideas": ["I1", "I2"]},
   {"label": "Ô tìm đầu menu", "desc": "Giữ giá trị cũ trong ô; thêm một hàng trong menu, giống bottom sheet app.", "preview": m({"D5": "b"}, P_SRCH), "ideas": ["I3", "I5"]}],
  "untitled": m({"D5": "a"}, P_SRCH), "astryx": m({"D5": "b"}, P_SRCH), "astryxNote": "Typeahead tách riêng"},
 {"id": "D6", "title": "App: mở Select ra gì",
  "why": "Trang chốt biến thể ghi mobile “split” (khác cấu tạo) và có Kèm theo Bottom Sheet. Danh sách xe có tìm và option nhiều thông tin.",
  "source": "variants/select mobile split · design.md BottomSheet .Content · Chọn một",
  "options": [
   {"label": "Bottom sheet: tìm + danh sách, chọn là đóng", "desc": "Giữ ngữ cảnh form phía sau; sheet cao tối đa ~78% màn.", "rec": True, "preview": m({"D6": "a"}, SHEET, 360, "mobile"), "ideas": ["I3", "I7"]},
   {"label": "Màn riêng toàn màn", "desc": "Hợp danh sách rất dài, có tìm; mất ngữ cảnh form.", "preview": m({"D6": "b"}, FULL, 360, "mobile"), "ideas": ["I8"]},
   {"label": "Bánh xe gốc của máy (Native)", "desc": "Quen tay; chỉ hiện được 1 dòng chữ, không có tìm, không có chip.", "preview": m({"D6": "c"}, WHEEL, 360, "mobile"), "ideas": ["I7"]}],
  "untitled": m({"D6": "a"}, SHEET, 360, "mobile"), "astryx": m({"D6": "a"}, SHEET, 360, "mobile"), "astryxNote": "Selector presentation=adaptive"},
 {"id": "D7", "title": "Bề rộng menu",
  "why": "Ô Select nằm trong lưới 2 cột (~320px). Option nhiều thông tin có thể rộng hơn ô.",
  "source": "Untitled select popover",
  "options": [
   {"label": "Bằng ô", "desc": "Thẳng mép, gọn; chữ dài bị cắt …", "rec": True, "preview": m({"D7": "a"}, P_W.replace('style="width:300px"', "")), "ideas": ["I1", "I2"]},
   {"label": "Theo nội dung, tối thiểu bằng ô, tối đa 480", "desc": "Đọc đủ tên; menu lấn sang cột bên.", "preview": m({"D7": "b"}, P_W.replace('style="width:300px"', "")), "ideas": ["I4", "I6"]}],
  "untitled": m({"D7": "a"}, P_W), "astryx": m({"D7": "b"}, P_W)},
]
# Hình D7: menu đặt trong .pop để nhận luật bề rộng
for d in decisions:
    if d["id"] == "D7":
        for o in d["options"]:
            o["preview"] = o["preview"].replace('<div class="mn"', '<div class="anchor" style="height:150px;width:240px"><div class="pop"><div class="mn"', 1)[:-6] + "</div></div></div>"

ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/react/components/select", "title": "Untitled UI — Select / Combobox",
  "why": "6 Type, ✓ phải, chữ phụ cùng dòng, combobox gõ trong ô; menu bằng ô.", "pv": P_SEL},
 {"id": "I2", "source": "shadcn/ui", "url": "https://ui.shadcn.com/docs/components/combobox", "title": "shadcn/ui — Combobox",
  "why": "Popover có ô tìm (Command), ✓ đặt cạnh option; mẫu 2 dòng cho người dùng.", "pv": P_RICH},
 {"id": "I3", "source": "Material 3", "url": "https://m3.material.io/components/menus/overview", "title": "Material 3 — Menu / exposed dropdown",
  "why": "Trên điện thoại mở bottom sheet có radio; chữ phụ xuống dòng.", "pv": SHEET, "plat": "mobile"},
 {"id": "I4", "source": "Linear", "url": "https://linear.app/docs/assigning-issues", "title": "Linear — chọn người phụ trách",
  "why": "Option 1 dòng: avatar + tên trái, thông tin phụ canh phải; menu rộng theo nội dung.", "pv": P_SC},
 {"id": "I5", "source": "Atlassian", "url": "https://atlassian.design/components/select/examples", "title": "Atlassian — Select",
  "why": "Async select tìm theo nhiều trường, option có mô tả 2 dòng; ô tìm nằm trong menu.", "pv": P_SRCH},
 {"id": "I6", "source": "Stripe Dashboard", "url": "https://docs.stripe.com/dashboard/basics", "title": "Stripe Dashboard — chọn khách",
  "why": "Option đã chọn nền nhạt; tên + email 2 dòng; menu rộng hơn ô.", "pv": P_SUP},
 {"id": "I7", "source": "Apple HIG", "url": "https://developer.apple.com/design/human-interface-guidelines/pickers", "title": "Apple HIG — Pickers",
  "why": "Danh sách ngắn dùng bánh xe/menu gốc; dài thì danh sách có tìm trong sheet.", "pv": WHEEL, "plat": "mobile"},
 {"id": "I8", "source": "Samsara", "url": "https://www.samsara.com/products/telematics/fleet-management", "title": "Samsara — chọn xe trong phần mềm đội xe",
  "why": "Chọn xe hiện ảnh/icon loại, biển số, lái xe và trạng thái trực tuyến — tránh gán nhầm xe đang sửa.", "pv": P_RICH},
]
for i in ideas:
    plat = i.pop("plat", "web")
    i["preview"] = m(None, i.pop("pv"), 400 if plat == "web" else 340, plat)

REC = {d["id"]: chr(97 + next(k for k, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC},
           {"id": "untitled", "label": "Untitled UI", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
           {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "c", "D2": "c", "D3": "a", "D4": "b", "D5": "b", "D6": "a", "D7": "b"}}]
for i in ideas:
    pk = {**REC}
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pk[d["id"]] = chr(97 + k)
    presets.append({"id": i["id"], "label": f'{i["id"]} · {i["source"]}', "pick": pk})

# ---------- màn ----------
LIVE_POP = (f'<div class="pop" data-show="state:open">{menu(VEH_MENU, search=True, scroll=True)}</div>'
            f'<div class="pop" data-show="state:empty">{menu([EMPTY], search=True)}</div>')
LIVE = field("Xe", trig(search=True, rich=("51C-482.19 · Đầu kéo Hino 2 trục", "Lái xe: Trần Văn Bình"),
                        long="51C-482.19 · Đầu kéo Hino 2 trục 6x4 kéo sơ mi rơ moóc 40 feet (đăng kiểm đến 12/2026)"),
             req=True, hint="Chỉ hiện xe còn hạn đăng kiểm.", err="Xe đang sửa (LSC-0930) — chọn xe khác.", live=True, extra=LIVE_POP)
S_ASSIGN = ('<div class="pad"><div class="card form"><div class="h">Phân công cho lệnh LVT-2026-0412<span class="chip wa">Chờ xe</span></div><div class="grid2">'
            + LIVE
            + field("Lái xe", trig("Trần Văn Bình", lead=("avatar", 0)), req=True)
            + field("Mức ưu tiên", trig("Cao", lead=("dot", "yellow")))
            + field("Cảng lấy hàng", trig("Cảng Cát Lái", lead=("icon", "pin")))
            + field("Rơ moóc", trig(None, "Chọn rơ moóc"), hint="Lệnh 40 feet cần rơ moóc 40.")
            + field("Ca làm việc", trig("Ca ngày (06:00 – 18:00)", native=True), hint="Native — dùng bộ chọn của trình duyệt.")
            + '</div><div class="acts"><button class="bt">Huỷ</button><button class="bt pri">Phân công</button></div></div></div>')
S_REPAIR = ('<div class="pad"><div class="grid2"><div class="card"><div class="h">Phiếu nghiệm thu sửa chữa</div>'
            + field("Lệnh sửa chữa", trig(rich=("LSC-0930 · Thay lốp trục 2", "51C-482.19 · Gara Tân Thuận")), req=True)
            + field("Người nghiệm thu", trig(st="is-open", ph="Chọn nhân viên"), req=True,
                    extra='<div class="pop">' + menu([ro(c, n, r, avatar=a, sel=i == 2, hov=i == 1) for i, (c, n, r, a) in enumerate(STAFF)]) + "</div>")
            + '<div style="height:210px"></div></div><div class="card"><div class="h">Gợi ý cách đọc</div>'
            '<div class="hn" style="font-size:13px;color:var(--fg3)">Option nhân viên: mã NV + tên ở dòng 1, chức vụ · nơi làm ở dòng 2, avatar bên trái. '
            'Option lệnh sửa chữa: icon loại, mã LSC + nội dung, xe · gara, chip trạng thái.</div>'
            + menu([ro(*LSC[0][:4], LSC[0][4], LSC[0][5]), ro(*LSC[1][:4], LSC[1][4], LSC[1][5]), ro(*LSC[2][:4], LSC[2][4], LSC[2][5])]).replace('class="mn"', 'class="mn vgm"', 1)
            + "</div></div></div>")
M_LIVE = field("Xe", trig(search=False, rich=("51C-482.19 · Đầu kéo Hino 2 trục", "Lái xe: Trần Văn Bình"),
                          long="51C-482.19 · Đầu kéo Hino 2 trục 6x4 kéo sơ mi rơ moóc 40 feet"),
               req=True, err="Xe đang sửa (LSC-0930) — chọn xe khác.", hint="Chạm để đổi xe.", live=True, mob=True)
OPEN_M = ('<div data-show="state:open"><div class="scr"></div>'
          '<div data-show="D6:a">' + SHEET.replace("sht static", "sht") + '</div>'
          '<div data-show="D6:b">' + FULL.replace("fs static", "fs") + '</div>'
          '<div data-show="D6:c">' + WHEEL.replace("sht static", "sht") + '</div></div>'
          '<div data-show="state:empty"><div class="scr"></div><div class="sht"><i class="hd"></i><div class="sh-t">Chọn xe</div>'
          '<div class="msr">' + ic("search") + '<span style="color:var(--fg)">51Z</span></div>' + EMPTY + '</div></div>')
S_APP = ('<div class="mpad"><div class="mcard"><b>LVT-2026-0412</b><span class="s">Cát Lái → Sóng Thần · 40HC</span></div>'
         + M_LIVE + field("Rơ moóc", trig("51R-118.40 · Moóc 40 feet", lead=None), mob=True)
         + field("Ca làm việc", trig("Ca ngày (06:00 – 18:00)"), mob=True)
         + '</div><div class="mfoot"><button class="bt pri big">Nhận xe</button></div>' + OPEN_M)

TYPES = [("Default", dict(val="Cảng Cát Lái")), ("Icon Leading", dict(val="Cảng Cát Lái", lead=("icon", "pin"))),
         ("Avatar Leading", dict(val="Trần Văn Bình", lead=("avatar", 0))), ("Dot Leading", dict(val="Cao", lead=("dot", "yellow"))),
         ("Searchable", dict(search=True, val="51C-482.19")), ("Native", dict(val="Ca ngày (06:00 – 18:00)", native=True))]
STATES_V = [("Placeholder", "", None), ("Hover", "is-hover", None), ("Focus", "is-focus", None), ("Open", "is-open", "v"),
            ("Filled", "", "v"), ("Disabled", "is-dis", "v"), ("Error", "is-err", "v")]


def g(plat):
    n = 3 if plat == "web" else 1
    mob = plat == "mobile"
    B = []
    B.append(vg_row("Type", [(t, field(None, trig(**kw), mob=mob)) for t, kw in TYPES], n, "Size MD · Filled"))
    if not mob:
        B.append(vg_row("Size", [(s, field(None, trig("Cảng Cát Lái", lead=("icon", "pin"), size=s.lower()))) for s in ("SM", "MD", "LG")], 3, "28 · 32 · 40"))
    B.append(vg_row("State", [(nm, field(None, trig("Cảng Cát Lái" if v else None, "Chọn cảng", st=st), err="Chưa chọn cảng." if st == "is-err" else None, mob=mob))
                              for nm, st, v in STATES_V], 4 if not mob else 1))
    B.append(vg_row("Menu item", [("Default", menu([mi("Cảng Hiệp Phước")])), ("Hover", menu([mi("Cảng Hiệp Phước", hov=True)])),
                                  ("Selected", menu([mi("Cảng Cát Lái", sel=True)])), ("Disabled", menu([mi("Cảng Tân Vũ", dis=True)])),
                                  ("Supporting", menu([mi("Cảng Cát Lái", "Thủ Đức, TP.HCM")]))], 5 if not mob else 1))
    B.append(vg_row("Option nhiều thông tin (D2)", [("Xe", menu([veh_ro(0, sel=True), veh_ro(3)])),
                                                    ("Lệnh sửa chữa", menu([ro(*LSC[0][:4], LSC[0][4], LSC[0][5], sel=True), ro(*LSC[1][:4], LSC[1][4], LSC[1][5])])),
                                                    ("Nhân viên", menu([ro(c, nm, r, avatar=a, sel=i == 0) for i, (c, nm, r, a) in enumerate(STAFF[:2])]))], n))
    kem = [("Empty", menu([EMPTY], search=True)), ("Scrollbar", menu([mi(p, sel=i == 0) for i, p in enumerate(PORTS)], scroll=True).replace('class="mn"', 'class="mn" style="max-height:180px;position:relative"', 1))]
    if mob:
        kem.append(("Bottom Sheet", SHEET))
    B.append(vg_row("Kèm theo", kem, n))
    B.append(vg_row("Chữ dài — 1 dòng, cắt …", [("Giá trị dài", field("Cảng lấy hàng", trig("Cảng Container Quốc tế Cái Mép – Thị Vải (TCIT), Phú Mỹ, Bà Rịa – Vũng Tàu"), mob=mob)),
                                                 ("Option dài", menu([mi("Cảng Container Quốc tế Cái Mép – Thị Vải (TCIT)", "Phú Mỹ, Bà Rịa – Vũng Tàu")]))], 2 if not mob else 1, "DEC-261"))
    return vg(B)


screens = [
 {"id": "assign-web", "name": "Phân công xe", "device": "web", "title": "Phân công xe", "crumb": "Điều phối", "nav": "Điều phối",
  "note": "Ô Xe = Searchable + option nhiều thông tin; bấm ô để mở menu. Trạng thái Mở / Tìm không ra / Lỗi chọn ở Bảng chọn.", "html": S_ASSIGN},
 {"id": "repair-web", "name": "Nghiệm thu sửa chữa", "device": "web", "title": "Nghiệm thu sửa chữa", "crumb": "Bảo dưỡng", "nav": "Chứng từ",
  "note": "Option nhân viên (mã NV, chức vụ) và lệnh sửa chữa (icon loại, mã LSC, xe · gara, trạng thái) — theo ghi chú user.", "html": S_REPAIR},
 {"id": "pick-app", "name": "Nhận xe", "device": "mobile", "title": "Nhận xe cho lệnh", "back": True, "tabs": False,
  "note": "Bấm ô Xe để mở — D6 đổi sheet / màn riêng / bánh xe.", "html": S_APP},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "shell": "none", "note": "Type 6, Size 3, State 7, Menu item 5, option nhiều thông tin, Kèm theo.", "html": g("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app (cao 48) + Bottom Sheet.", "html": g("mobile")},
]

page = {
 "component": "Select", "slug": "select", "title": "Select Review",
 "subtitle": "Base component · vòng 1 Brainstorm — biến thể đã chốt (Type 6 · Size 3 · State 7 · Menu item 5 · Empty, Scrollbar, Bottom Sheet). Ô focus theo Input D1. Trang này hỏi chi tiết hình + option nhiều thông tin.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Select 6 Type (icon, avatar, dot đầu, searchable combobox, native); menu bo 8, mục bo 6 cao 40, ✓ bên phải, chữ phụ cùng dòng. Không có mẫu option 3–4 trường.",
               "source": "design/_ref/untitled-ui/react/components/base/select/"},
  "astryx": {"summary": "Selector (danh sách) + ComplexSelector (popup tự dựng cho lưới ca, ma trận); app = BottomSheet .Content · Chọn một (RadioListItem).",
             "source": "design/design.md › Form Controls · ComplexSelector"},
  "usage": ["Điều phối · phân công xe, lái xe, rơ moóc", "Bảo dưỡng · lệnh sửa chữa LSC, người nghiệm thu", "Mọi form: cảng, kho, khách, mức ưu tiên, ca"],
  "platform": "Nhóm B — trang chốt ghi mobile “split”: web menu nổi, app mở sheet / màn riêng (D6)."},
 "css": CSS + CSS_SEL, "cssScreen": SCREEN_CSS,
 "states": [{"key": "default", "label": "Đã chọn"}, {"key": "hover", "label": "Hover"}, {"key": "focus", "label": "Focus"}, {"key": "open", "label": "Mở"},
            {"key": "empty", "label": "Tìm không ra"}, {"key": "error", "label": "Lỗi"}, {"key": "disabled", "label": "Tắt"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": "[data-live]>.ctl", "state": "open", "toggle": True}, {"sel": "[data-live] .pop .ro,.sht .ro,.fs .ro,.whl span", "close": True}],
 "protoLayers": ".pop,.sht,.fs",
 "protoHint": "bấm ô Xe để mở, bấm một xe để chọn và đóng",
}

write(OUT, page, decisions)
