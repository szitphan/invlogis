#!/usr/bin/env python3
"""Sinh page.json cho Multiselect (vòng 1 Brainstorm).
Chạy: python3 design-system/components/_work/multiselect/build.py && python3 _scripts/ds-component-page.py multiselect
Đầu vào đã chốt: thẻ Multiselect trên trang Chốt biến thể Base (artifact VQDsMrBW37W3QWVTPN79qC, db variants/multiselect v1, 26/10):
Hiển thị Tags · Count · Checkbox Menu × Size SM MD × State Placeholder · Focus · Active · Open Active · Search Empty · Disabled · mobile split.
Focus của ô theo Input D1; option nhiều thông tin theo Select D2 — không hỏi lại.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_forms"))
from kit import CSS, SCREEN_CSS, av, cb, dot, ic, mini, vg, vg_row, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"

STATUS = [("Chờ xe", "yellow", 5), ("Đang chạy", "blue", 12), ("Trễ hẹn", "red", 3), ("Hoàn tất", "green", 128), ("Đã huỷ", "gray", 9)]
ROUTES = ["Cát Lái → Sóng Thần", "Cát Lái → Phnom Penh", "Hiệp Phước → Long An", "ICD Phước Long → Bình Dương", "Cái Mép → Biên Hoà", "Tân Vũ → Hà Nội"]
CUST = ["Delta Logistics", "Tân Cảng Logistics", "An Phát Trading", "Hưng Thịnh Food", "Gemadept"]


def tg(label, x=True, lead=""):
    xx = f'<button class="x" aria-label="Bỏ {label}">{ic("x", 12)}</button>' if x else ""
    return f'<span class="tg t-sm">{lead}<span class="tl">{label}</span>{xx}</span>'


def trig(sel=(), mode="tags", ph="Chọn…", size="md", st="", lead=None, live=False, long_sel=None, label="Trạng thái"):
    """mode: tags | count. sel = danh sách nhãn đã chọn."""
    L = f'<span class="ic">{ic(lead)}</span>' if lead else ""
    if not sel:
        body = f'<span class="ph nl">{ph}</span>'
    elif mode == "tags":
        many = "".join(tg(s) for s in sel)
        body = (f'<span class="tw nl">{many}<span class="more">+{max(0, len(sel) - 2)}</span>'
                f'<span class="v tp" data-show="D3:a state:open">ch<i class="caret"></i></span>'
                f'<span class="v tp" data-show="D3:a state:empty">xyz<i class="caret"></i></span></span>')
    else:
        first = ", ".join(sel[:2]) + (f" +{len(sel) - 2}" if len(sel) > 2 else "")
        body = (f'<span class="v nl"><span data-show="D7:a">{len(sel)} đã chọn</span><span data-show="D7:b">{first}</span>'
                f'<span data-show="D7:c">{label}<span class="cn">{len(sel)}</span></span></span>')
    if long_sel:
        body += f'<span class="tw" data-show="state:long">{"".join(tg(s) for s in long_sel)}</span>'
    return f'<div class="ctl ms s-{size} m-{mode} {st}">{L}{body}<span class="ic chev">{ic("chev")}</span></div>'


def field(label, c, req=False, hint=None, live=False, mob=False, extra=""):
    lb = f'<div class="lb">{label}{"<span class=req>*</span>" if req else ""}</div>' if label else ""
    hn = f'<div class="hn">{hint}</div>' if hint else ""
    return f'<div class="f anchor{" m" if mob else ""}" data-cmp{" data-live" if live else ""}>{lb}{c}{hn}{extra}</div>'


def opt(label, on=False, hov=False, lead="", count=None, dis=False):
    ct = f'<span class="oc">{count}</span>' if count is not None else ""
    return (f'<div class="mi{" sel" if on else ""}{" hov" if hov else ""}{" dis" if dis else ""}"><span class="lcb">{cb(on)}</span>{lead}'
            f'<span class="ml">{label}</span>{ct}<span class="ck">{ic("check") if on else ""}</span></div>')


def menu(items, picked=(), search=True, foot=True, w=None):
    sr = f'<div class="msr" data-show="D3:b">{ic("search")}<span>Tìm…</span></div>' if search else ""
    grp = ""
    if picked:
        grp = (f'<div data-show="D5:b"><div class="mh">Đã chọn · {len(picked)}</div>{"".join(picked)}<div class="mdv"></div><div class="mh">Tất cả</div></div>')
    n = sum(1 for i in items if ' sel' in i[:30])
    ft = ""
    if foot:
        ft = (f'<div class="mft" data-show="D4:b"><button class="lk">Bỏ chọn tất cả</button><span class="fc">{n} đã chọn</span></div>'
              f'<div class="mft" data-show="D4:c"><button class="bt ghost">Bỏ chọn</button><button class="bt pri" style="margin-left:auto">Áp dụng ({n})</button></div>')
    st = f' style="width:{w}px"' if w else ""
    return f'<div class="mn msm"{st}>{sr}{grp}<div class="ml-all">{"".join(items)}</div>{ft}</div>'


def st_items(chosen=("Đang chạy", "Trễ hẹn"), hov="Chờ xe"):
    return [opt(n, n in chosen, n == hov, dot(c), k) for n, c, k in STATUS]


def st_picked(chosen=("Đang chạy", "Trễ hẹn")):
    return [opt(n, True, False, dot(c), k) for n, c, k in STATUS if n in chosen]


EMPTY = '<div class="mem"><b>Không có trạng thái “xyz”</b>Thử từ khác.</div>'

CSS_MS = r"""
.ctl.ms{cursor:pointer}
.ctl.ms .chev{margin-left:auto;color:var(--color-text-tertiary)}
.pv[data-state=open] [data-live] .chev{transform:rotate(180deg)}
.pv[data-state=empty] [data-live]>.ctl{border-color:var(--color-focus-ring);box-shadow:inset 0 0 0 1px var(--color-focus-ring)}
.pv[data-state=long] [data-live] .nl{display:none}
.tw{display:flex;flex-wrap:wrap;gap:4px;flex:1;min-width:0;align-items:center;padding:3px 0}
.ctl.m-tags{align-items:center}
.more{display:none;font:600 12px Inter;color:var(--color-text-secondary);background:var(--color-utility-neutral-100);border-radius:4px;padding:1px 6px}
.caret{display:inline-block;width:1px;height:16px;background:var(--color-text-primary);margin-left:1px;vertical-align:-3px}
.tp{flex:0 0 auto}
/* D1 nhiều tag */
.pv[data-D1=b] .tw{flex-wrap:nowrap;overflow:hidden}
.pv[data-D1=b] .tw .tg:nth-of-type(n+3){display:none}
.pv[data-D1=b] .tw:has(.tg:nth-of-type(3)) .more{display:inline-block}
.pv[data-D1=b] .tw .tg{flex:0 1 auto;min-width:0}
/* D2 dấu chọn */
.lcb{display:inline-flex}
.pv[data-D2=a] :is(.msm,.sht,.fs) .ck{display:none}
.pv[data-D2=b] :is(.msm,.sht,.fs) .lcb{display:none}
.pv[data-D2=b] .msm .mi.sel{background:var(--color-bg-selected)}
.oc{margin-left:auto;font:500 12.5px Inter;color:var(--color-text-tertiary)}
.mi .oc+.ck{margin-left:8px}
/* D4 chân menu */
.mft{display:flex;align-items:center;gap:8px;border-top:1px solid var(--color-border-secondary);margin:4px -4px -4px;padding:8px 12px}
.mft .lk{border:0;background:none;padding:0;font:600 13px Inter;color:var(--color-text-primary);text-decoration:underline;text-underline-offset:2px;cursor:pointer}
.mft .fc{margin-left:auto;color:var(--color-text-tertiary);font-size:12.5px}
.mft .bt{height:28px;font-size:12.5px}
/* D7 count */
.cn{display:inline-block;margin-left:6px;font:600 11.5px/16px Inter;background:var(--color-bg-primary_solid);color:var(--color-text-inverse);border-radius:999px;padding:0 6px}
/* pop */
.pop{min-width:100%}.pop .mn{width:100%}
.ctl.ms.s-sm .tg{--th:20px;font-size:11.5px}
/* app */
.sht .mi{gap:12px}.sht .mi .cbx{width:20px;height:20px}
.sht .sh-f .bt{flex:1;height:48px;border-radius:12px;font-size:15px}
.fs{position:absolute;inset:0;background:var(--color-bg-primary_alt);z-index:9;display:flex;flex-direction:column}
.fs .fs-h{height:52px;display:flex;align-items:center;gap:8px;padding:44px 16px 0;box-sizing:content-box;font:600 17px Inter}
.fs .msr{margin:8px 16px;border:1px solid var(--color-border-primary);border-radius:12px;height:44px;padding:0 12px}
.fs .fs-b{flex:1;overflow:auto;padding:0 8px}.fs .mi{min-height:52px;font-size:16px;padding:0 12px}
.fs .chips{display:flex;gap:6px;flex-wrap:wrap;padding:4px 16px 8px}
.fs .fs-f{padding:12px 16px 28px;border-top:1px solid var(--color-border-secondary)}
.sht.static,.fs.static{position:relative;border-radius:16px;max-height:none;box-shadow:none;border:1px solid var(--color-border-secondary)}
.fs.static .fs-h{padding-top:0}
.vg .msm{max-height:none}
"""


def m(over, inner, w=420, plat="web"):
    base = {"D1": "a", "D2": "a", "D3": "a", "D4": "b", "D5": "a", "D6": "a", "D7": "a", "state": "x"}
    return mini({**base, **(over or {})}, inner, w, plat)


def stack(*h):
    return '<div style="display:flex;flex-direction:column;gap:6px">' + "".join(h) + "</div>"


FOUR = ["Cát Lái → Sóng Thần", "Hiệp Phước → Long An", "Cát Lái → Phnom Penh", "Tân Vũ → Hà Nội"]
P_MANY = field("Tuyến được chạy", trig(FOUR, ph="Chọn tuyến"))
P_MENU = stack(field("Trạng thái", trig(["Đang chạy", "Trễ hẹn"], st="is-open")), menu(st_items(), foot=False))
P_SRCH = stack(field("Trạng thái", trig(["Đang chạy", "Trễ hẹn"], st="is-open").replace('data-show="D3:a state:open"', 'data-show="D3:a"')), menu(st_items()[:3], foot=False))
P_FOOT = menu(st_items())
P_GRP = menu(st_items(), st_picked(), foot=False)
P_CNT = stack(field("Trạng thái", trig(["Đang chạy", "Trễ hẹn", "Chờ xe"], "count")), field("Khách hàng", trig(["Delta Logistics", "Gemadept"], "count", label="Khách hàng")))
SHEET = ('<div class="sht static"><i class="hd"></i><div class="sh-t">Trạng thái<span class="ic">' + ic("x", 20) + '</span></div><div class="sh-b">'
         + "".join(opt(n, n in ("Đang chạy", "Trễ hẹn"), False, dot(c), k) for n, c, k in STATUS)
         + '</div><div class="sh-f"><button class="bt">Bỏ chọn</button><button class="bt pri">Áp dụng (2)</button></div></div>')
FULL = ('<div class="fs static"><div class="fs-h">' + ic("chevr", 20).replace("M9 6l6 6-6 6", "M15 18l-6-6 6-6") + 'Tuyến được chạy</div>'
        '<div class="msr">' + ic("search") + '<span>Tìm tuyến…</span></div><div class="chips">' + tg("Cát Lái → Sóng Thần") + tg("Hiệp Phước → Long An") + '</div>'
        '<div class="fs-b">' + "".join(opt(r, r in FOUR[:2]) for r in ROUTES[:5]) + '</div><div class="fs-f"><button class="bt pri big" style="width:100%">Xong (2)</button></div></div>')

decisions = [
 {"id": "D1", "title": "Hiển thị Tags: chọn nhiều thì ô xử lý sao",
  "why": "Lái xe chạy 4–6 tuyến, lệnh có 3–5 nhãn. Ô xuống dòng làm lệch lưới form; một dòng thì phải giấu bớt.",
  "source": "variants/multiselect Hiển thị Tags · DEC-261 (chữ dài)",
  "options": [
   {"label": "Xuống dòng, ô cao lên", "desc": "Thấy hết lựa chọn; ô cao không đều trong lưới 2 cột.", "preview": m({"D1": "a"}, P_MANY), "ideas": ["I1", "I3"]},
   {"label": "Một dòng: 2 tag + “+n”", "desc": "Ô giữ cao 32; muốn xem đủ phải mở menu.", "rec": True, "preview": m({"D1": "b"}, P_MANY), "ideas": ["I2", "I5"]}],
  "untitled": m({"D1": "a"}, P_MANY), "astryx": m({"D1": "b"}, P_MANY), "astryxNote": "MultiSelector Labels"},
 {"id": "D2", "title": "Dấu chọn trong menu",
  "why": "Hiển thị Checkbox Menu đã chốt. Nếu Select (chọn một) dùng ✓ phải thì chọn nhiều nên khác để người dùng biết bấm không đóng menu.",
  "source": "variants/multiselect Checkbox Menu · Select D1",
  "options": [
   {"label": "Ô checkbox bên trái", "desc": "Nói rõ “chọn được nhiều”; khác hẳn Select chọn một.", "rec": True, "preview": m({"D2": "a"}, P_MENU), "ideas": ["I1", "I4"]},
   {"label": "✓ bên phải + nền nhạt (như Select)", "desc": "Đồng bộ nhìn với Select; khó biết bấm có đóng menu không.", "preview": m({"D2": "b"}, P_MENU), "ideas": ["I2"]}],
  "untitled": m({"D2": "a"}, P_MENU), "astryx": m({"D2": "a"}, P_MENU), "astryxNote": "CheckboxListItem"},
 {"id": "D3", "title": "Gõ tìm ở đâu",
  "why": "State Search Empty đã chốt → có tìm. Gõ ngay sau các tag (combobox) hoặc ô tìm đầu menu.",
  "source": "variants/multiselect State Search Empty · Select D5",
  "options": [
   {"label": "Gõ sau các tag trong ô", "desc": "Nhanh như ô nhập tag; ô đã nhiều tag thì chỗ gõ hẹp.", "preview": m({"D3": "a"}, P_SRCH), "ideas": ["I3", "I1"]},
   {"label": "Ô tìm đầu menu", "desc": "Chỗ gõ luôn rộng; giống bottom sheet app.", "rec": True, "preview": m({"D3": "b"}, P_SRCH), "ideas": ["I2", "I5"]}],
  "untitled": m({"D3": "a"}, P_SRCH), "astryx": m({"D3": "b"}, P_SRCH)},
 {"id": "D4", "title": "Chân menu",
  "why": "Bộ lọc danh sách: chọn xong áp ngay thì danh sách nhảy sau mỗi lần tick; có nút Áp dụng thì thêm một bấm.",
  "source": "Điều phối · hàng lọc danh sách lệnh",
  "options": [
   {"label": "Không có chân, tick là áp ngay", "desc": "Nhanh nhất; danh sách tải lại mỗi lần tick.", "preview": m({"D4": "a"}, P_FOOT), "ideas": ["I1", "I3"]},
   {"label": "“Bỏ chọn tất cả” + số đã chọn", "desc": "Gỡ nhanh khi lỡ chọn nhiều; vẫn áp ngay.", "rec": True, "preview": m({"D4": "b"}, P_FOOT), "ideas": ["I5", "I2"]},
   {"label": "Bỏ chọn + Áp dụng (n)", "desc": "Chọn xong mới tải; hợp danh sách nặng, lọc theo nhiều điều kiện.", "preview": m({"D4": "c"}, P_FOOT), "ideas": ["I4", "I6"]}],
  "untitled": m({"D4": "a"}, P_FOOT), "astryx": m({"D4": "c"}, P_FOOT)},
 {"id": "D5", "title": "Mục đã chọn nằm đâu trong menu",
  "why": "Danh sách khách hàng, tuyến dài; mục đã chọn ở giữa danh sách thì khó gỡ.",
  "source": "variants/multiselect Open Active",
  "options": [
   {"label": "Giữ đúng thứ tự", "desc": "Danh sách không nhảy chỗ khi tick.", "rec": True, "preview": m({"D5": "a"}, P_GRP), "ideas": ["I1", "I4"]},
   {"label": "Nhóm “Đã chọn” lên đầu", "desc": "Gỡ nhanh; mục xuất hiện hai lần, menu dài hơn.", "preview": m({"D5": "b"}, P_GRP), "ideas": ["I6", "I5"]}],
  "untitled": m({"D5": "a"}, P_GRP), "astryx": m({"D5": "a"}, P_GRP)},
 {"id": "D6", "title": "App: mở ra gì",
  "why": "Trang chốt ghi mobile “split”. Danh sách ngắn (trạng thái) và dài có tìm (tuyến, khách) khác nhau.",
  "source": "variants/multiselect mobile split · design.md BottomSheet .Content · Chọn nhiều",
  "options": [
   {"label": "Bottom sheet checkbox + Áp dụng cố định", "desc": "Hợp danh sách ≤ 10 mục; giữ ngữ cảnh.", "rec": True, "preview": m({"D6": "a"}, SHEET, 360, "mobile"), "ideas": ["I7", "I4"]},
   {"label": "Màn riêng: tìm + chip đã chọn + Xong", "desc": "Hợp danh sách dài; mất ngữ cảnh form.", "preview": m({"D6": "b"}, FULL, 360, "mobile"), "ideas": ["I8"]}],
  "untitled": m({"D6": "a"}, SHEET, 360, "mobile"), "astryx": m({"D6": "a"}, SHEET, 360, "mobile")},
 {"id": "D7", "title": "Hiển thị Count: ô ghi gì",
  "why": "Hiển thị Count đã chốt cho hàng lọc chật chỗ. Cần đủ để biết đang lọc gì mà không mở.",
  "source": "variants/multiselect Hiển thị Count",
  "options": [
   {"label": "“3 đã chọn”", "desc": "Ngắn nhất; không biết đã chọn gì.", "preview": m({"D7": "a"}, P_CNT), "ideas": ["I1"]},
   {"label": "“Đang chạy, Trễ hẹn +1”", "desc": "Biết ngay đang lọc gì; dài, dễ bị cắt.", "rec": True, "preview": m({"D7": "b"}, P_CNT), "ideas": ["I5", "I6"]},
   {"label": "Tên trường + số tròn", "desc": "“Trạng thái ③” gọn như nút lọc; phải mở mới biết chi tiết.", "preview": m({"D7": "c"}, P_CNT), "ideas": ["I4"]}],
  "untitled": m({"D7": "a"}, P_CNT), "astryx": m({"D7": "a"}, P_CNT), "astryxNote": "MultiSelector Count"},
]

ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/react/components/multi-select", "title": "Untitled UI — Multi-select",
  "why": "Tag trong ô xuống dòng, gõ sau tag, menu checkbox trái; chế độ đếm “n selected”.", "pv": P_MANY},
 {"id": "I2", "source": "shadcn/ui", "url": "https://ui.shadcn.com/docs/components/combobox", "title": "shadcn/ui — Combobox nhiều lựa chọn",
  "why": "Ô giữ một dòng với “+n”; popover có ô tìm đầu; chân “Clear”.", "pv": P_SRCH},
 {"id": "I3", "source": "Atlassian", "url": "https://atlassian.design/components/select/examples", "title": "Atlassian — Multi select",
  "why": "Tag xuống dòng trong ô, gõ để lọc ngay sau tag, áp ngay.", "pv": P_MANY},
 {"id": "I4", "source": "Material 3", "url": "https://m3.material.io/components/chips/guidelines", "title": "Material 3 — Filter chips + sheet",
  "why": "Lọc trên điện thoại mở sheet checkbox, nút Áp dụng cố định; nút lọc có số tròn.", "pv": SHEET, "plat": "mobile"},
 {"id": "I5", "source": "Linear", "url": "https://linear.app/docs/filters", "title": "Linear — bộ lọc",
  "why": "Ô lọc ghi “Status is In Progress, Todo +1”; menu có tìm đầu, gỡ nhanh.", "pv": P_CNT},
 {"id": "I6", "source": "Airtable", "url": "https://support.airtable.com/docs/filtering-records-using-conditions", "title": "Airtable — lọc theo nhiều giá trị",
  "why": "Mục đã chọn gom đầu danh sách; Áp dụng sau khi chọn xong cho bảng lớn.", "pv": P_GRP},
 {"id": "I7", "source": "Apple HIG", "url": "https://developer.apple.com/design/human-interface-guidelines/sheets", "title": "Apple HIG — Sheets",
  "why": "Sheet cao vừa, nút xác nhận ở chân, vuốt xuống để huỷ.", "pv": SHEET, "plat": "mobile"},
 {"id": "I8", "source": "Shopee Seller", "url": "https://banhang.shopee.vn/", "title": "App bán hàng — chọn nhiều danh mục",
  "why": "Màn riêng có tìm, chip đã chọn chạy ở đầu, nút Xong cố định đáy.", "pv": FULL, "plat": "mobile"},
]
for i in ideas:
    plat = i.pop("plat", "web")
    i["preview"] = m(None, i.pop("pv"), 400 if plat == "web" else 340, plat)

REC = {d["id"]: chr(97 + next(k for k, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC},
           {"id": "untitled", "label": "Untitled UI", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a"}},
           {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "b", "D2": "a", "D3": "b", "D4": "c", "D5": "a", "D6": "a", "D7": "a"}}]
for i in ideas:
    pk = {**REC}
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pk[d["id"]] = chr(97 + k)
    presets.append({"id": i["id"], "label": f'{i["id"]} · {i["source"]}', "pick": pk})

# ---------- màn ----------
POP = (f'<div class="pop" data-show="state:open">{menu(st_items(), st_picked())}</div>'
       f'<div class="pop" data-show="state:empty">{menu([EMPTY], foot=False)}</div>')
LIVE = field(None, trig(["Đang chạy", "Trễ hẹn", "Chờ xe"], "count", "Trạng thái", lead="filter", live=True,
                        long_sel=["Đang chạy", "Trễ hẹn", "Chờ xe", "Hoàn tất", "Đã huỷ"]), live=True, extra=POP)
ORD = [("LVT-2026-0412", "Delta Logistics", "Cát Lái → Sóng Thần", "Đang chạy", "ok"), ("LVT-2026-0415", "Tân Cảng Logistics", "Cát Lái → Phnom Penh", "Chờ xe", "wa"),
       ("LVT-2026-0419", "An Phát Trading", "ICD Phước Long → Bình Dương", "Trễ hẹn", "er"), ("LVT-2026-0421", "Delta Logistics", "Hiệp Phước → Long An", "Đang chạy", "ok")]
S_LIST = ('<div class="pad"><div class="bar"><div style="width:260px">' + LIVE + '</div>'
          '<div style="width:300px">' + field(None, trig(["Delta Logistics", "Gemadept"], "tags", "Khách hàng", lead="user")) + '</div>'
          '<div style="width:220px">' + field(None, trig([], ph="Tuyến", lead="route")) + '</div></div>'
          '<div class="tb"><table><tr><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Trạng thái</th></tr>'
          + "".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td>{c}</td><td><span class="chip {k}">{s}</span></td></tr>' for a, b, c, s, k in ORD)
          + "</table></div></div>")
POP2 = (f'<div class="pop" data-show="state:open">{menu([opt(r, r in FOUR, r == ROUTES[3]) for r in ROUTES])}</div>'
        f'<div class="pop" data-show="state:empty">{menu([EMPTY.replace("trạng thái", "tuyến")], foot=False)}</div>')
LIVE2 = field("Tuyến được chạy", trig(FOUR, ph="Chọn tuyến", long_sel=ROUTES), req=True, hint="Điều phối chỉ gợi ý lái xe cho các tuyến này.", live=True, extra=POP2)
S_FORM = ('<div class="pad"><div class="card form"><div class="h">Hồ sơ lái xe · Trần Văn Bình</div><div class="grid2">'
          + '<div class="span2">' + LIVE2 + '</div>'
          + field("Hạng bằng lái", trig(["FC", "C"], ph="Chọn hạng"))
          + field("Loại xe được lái", trig(["Đầu kéo", "Xe tải 8 tấn"], ph="Chọn loại xe"))
          + field("Kho thường nhận hàng", trig([], ph="Chọn kho", st="is-dis"), hint="Chỉ trưởng đội sửa được.")
          + '</div><div class="acts"><button class="bt">Huỷ</button><button class="bt pri">Lưu</button></div></div></div>')
M_LIVE = field("Trạng thái", trig(["Đang chạy", "Trễ hẹn"], "tags", "Chọn trạng thái", long_sel=["Đang chạy", "Trễ hẹn", "Chờ xe", "Hoàn tất"]), live=True, mob=True)
OPEN_M = ('<div data-show="state:open"><div class="scr"></div><div data-show="D6:a">' + SHEET.replace("sht static", "sht") + '</div>'
          '<div data-show="D6:b">' + FULL.replace("fs static", "fs").replace("Tuyến được chạy", "Trạng thái") + '</div></div>'
          '<div data-show="state:empty"><div class="scr"></div><div class="sht"><i class="hd"></i><div class="sh-t">Trạng thái</div>'
          '<div class="msr">' + ic("search") + '<span style="color:var(--color-text-primary)">xyz</span></div>' + EMPTY + '</div></div>')
S_APP = ('<div class="mpad">' + M_LIVE + field("Khách hàng", trig(["Delta Logistics"], ph="Tất cả khách"), mob=True)
         + field("Tuyến", trig([], ph="Tất cả tuyến"), mob=True) + '</div><div class="mfoot"><button class="bt big">Xoá lọc</button><button class="bt pri big">Xem 15 lệnh</button></div>' + OPEN_M)

STV = [("Placeholder", [], ""), ("Focus", [], "is-focus"), ("Active", ["Đang chạy", "Trễ hẹn"], ""),
       ("Open Active", ["Đang chạy", "Trễ hẹn"], "is-open"), ("Search Empty", ["Đang chạy"], "is-focus"), ("Disabled", ["Đang chạy"], "is-dis")]


def g(plat):
    mob = plat == "mobile"
    n = 1 if mob else 3
    B = []
    B.append(vg_row("Hiển thị Tags · State", [(nm, field(None, trig(s, ph="Chọn trạng thái", st=st), mob=mob)) for nm, s, st in STV], n))
    B.append(vg_row("Hiển thị Count · State", [(nm, field(None, trig(s, "count", "Chọn trạng thái", st=st), mob=mob)) for nm, s, st in STV], n))
    if not mob:
        B.append(vg_row("Size", [(z, field(None, trig(["Đang chạy", "Trễ hẹn"], size=z.lower()))) for z in ("SM", "MD")] +
                        [(z + " · Count", field(None, trig(["Đang chạy", "Trễ hẹn"], "count", size=z.lower()))) for z in ("SM", "MD")], 4, "28 · 32"))
    B.append(vg_row("Checkbox Menu", [("Open Active", menu(st_items(), st_picked())), ("Search Empty", menu([EMPTY], foot=False))] +
                    ([("Bottom sheet", SHEET)] if mob else []), n if not mob else 1))
    B.append(vg_row("Chữ dài / nhiều lựa chọn", [("6 tuyến", field("Tuyến được chạy", trig(ROUTES), mob=mob)),
                                                 ("Count dài", field("Khách hàng", trig(CUST, "count", label="Khách hàng"), mob=mob))], 2 if not mob else 1, "DEC-261"))
    return vg(B)


screens = [
 {"id": "filter-web", "name": "Lọc danh sách lệnh", "device": "web", "title": "Lệnh vận tải", "crumb": "Điều phối",
  "note": "Hàng lọc: Trạng thái (Count, bấm để mở), Khách hàng (Tags). Trạng thái Mở / Tìm không ra / Chữ dài ở Bảng chọn.", "html": S_LIST},
 {"id": "driver-web", "name": "Hồ sơ lái xe", "device": "web", "title": "Hồ sơ lái xe", "crumb": "Lái xe", "nav": "Lái xe",
  "note": "Multiselect Tags trong form — ô Tuyến được chạy 4 tuyến (D1).", "html": S_FORM},
 {"id": "filter-app", "name": "Lọc lệnh", "device": "mobile", "title": "Lọc lệnh", "back": True, "tabs": False, "note": "Bấm ô Trạng thái để mở — D6 sheet / màn riêng.", "html": S_APP},
 {"id": "variants-web", "name": "Bảng biến thể", "device": "web", "shell": "none", "note": "Hiển thị Tags · Count · Checkbox Menu × State 6 × Size 2.", "html": g("web")},
 {"id": "variants-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản app + sheet.", "html": g("mobile")},
]

page = {
 "component": "Multiselect", "slug": "multiselect", "title": "Multiselect Review",
 "subtitle": "Base component · vòng 1 Brainstorm — biến thể đã chốt (Hiển thị Tags · Count · Checkbox Menu × Size SM MD × State 6). Ô focus theo Input D1, option nhiều thông tin theo Select D2.",
 "round": "brainstorm",
 "refs": {
  "untitled": {"summary": "Multi-select: tag trong ô xuống dòng, gõ sau tag, menu checkbox trái; chế độ đếm “n selected”; sm 36 · md 40.",
               "source": "design/_ref/untitled-ui/react/components/base/select/ · untitledui.com/react/components/multi-select"},
  "astryx": {"summary": "MultiSelector: Placeholder / Count / Labels / Badges; app = BottomSheet .Content · Chọn nhiều (CheckboxListItem).",
             "source": "design/design.md › Form Controls"},
  "usage": ["Điều phối · hàng lọc danh sách lệnh (trạng thái, khách, tuyến)", "Hồ sơ lái xe · tuyến được chạy, hạng bằng", "Báo cáo · chọn nhiều kho, nhiều khách"],
  "platform": "Nhóm B — mobile “split”: web menu nổi, app sheet hoặc màn riêng (D6)."},
 "css": CSS + CSS_MS, "cssScreen": SCREEN_CSS,
 "states": [{"key": "default", "label": "Đã chọn"}, {"key": "focus", "label": "Focus"}, {"key": "open", "label": "Mở"},
            {"key": "empty", "label": "Tìm không ra"}, {"key": "disabled", "label": "Tắt"}, {"key": "long", "label": "Chọn nhiều"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": "[data-live]>.ctl", "state": "open", "toggle": True}, {"sel": ".mft .bt.pri,.sh-f .bt,.fs-f .bt", "close": True}],
 "protoLayers": ".pop,.sht,.fs",
 "protoHint": "bấm ô đang thử để mở menu",
}

write(OUT, page, decisions)
