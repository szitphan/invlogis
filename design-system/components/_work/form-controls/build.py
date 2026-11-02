#!/usr/bin/env python3
"""Sinh page.json cho Form control: Checkbox · Radio · Toggle · Textarea — brainstorm gọn (28/10).
Chạy: python3 design-system/components/_work/form-controls/build.py && python3 _scripts/ds-component-page.py form-controls
Biến thể đã chốt: trang Chốt biến thể Base (VQDsMrBW37W3QWVTPN79qC, db variants/checkbox v2, radio v1, toggle v1, textarea v6, 26/10)
+ DEC-265 (chữ nhãn theo Size), DEC-278/281/283 (group item), DEC-280 (Checkbox nhóm A, Checkbox label nhóm B).
Điểm cần quyết từ trang Duyệt Base components (41DSsnEhvrQfZ1sggELNtq), chưa trả lời: C3, L9, R3, L14, L5 + chiều cao Textarea.
"""
import base64
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import P, ic, tok_css, BASE_CSS, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"

CHK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
IND = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M6 12h12"/></svg>'


def cb(val="off", size="sm", st=""):
    inner = CHK if val == "on" else IND if val == "ind" else ""
    return f'<span class="cb {size} {val} {st}" role="checkbox" aria-checked="{ {"on": "true", "off": "false", "ind": "mixed"}[val]}">{inner}</span>'


def rd(val="off", size="sm", st=""):
    return f'<span class="rd {size} {val} {st}" role="radio" aria-checked="{"true" if val == "on" else "false"}"></span>'


def tg(val="off", size="sm", st=""):
    return f'<span class="tgl {size} {val} {st}" role="switch" aria-checked="{"true" if val == "on" else "false"}"><i></i></span>'


def lab(ctrl, label, hint=None, size="sm", st="", attrs="", cls=""):
    h = f'<span class="hn">{hint}</span>' if hint else ""
    return f'<label class="cl {size} {st} {cls}" {attrs}>{ctrl}<span class="lt"><span class="lb">{label}</span>{h}</span></label>'


P.update({
    "map-pin": '<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8.5a3.5 3.5 0 0 0 0-7h-9a3.5 3.5 0 0 1 0-7H16"/>',
    "box": '<path d="M21 8l-9-5-9 5v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
    "inbox": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.5 5h13L22 12v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6z"/>',
})

# ----- Group item (Figma Radio group item 6658:170777 · Checkbox group item 6812:111499) -----
# Type: Radio button|Checkbox (ô chọn trái) · Icon simple · Icon card · Avatar · Payment icon · Payment logo · Vehicle (ô chọn phải)


IMG = {k: base64.b64encode((Path(__file__).parent / "assets" / f).read_bytes()).decode() for k, f in {
    "an": "avatar-an.jpg", "duc": "avatar-duc.jpg", "hoa": "avatar-hoa.jpg",
    "pi-vcb": "pay-icon-vcb.jpg", "pi-tcb": "pay-icon-tcb.jpg", "pi-mb": "pay-icon-mb.jpg",
    "pl-vcb": "pay-logo-vcb.png", "pl-tcb": "pay-logo-tcb.png", "pl-mb": "pay-logo-mb.png",
    "tractor": "vehicle-tractor.png", "truck": "vehicle-truck.png"}.items()}  # ảnh thật từ Figma, xem assets/SOURCE.txt
IMG_CSS = "".join(f'.im-{k}{{background-image:url(data:image/{"png" if k.startswith(("pl", "tr")) else "jpeg"};base64,{v})}}' for k, v in IMG.items())


def lead(typ, k=None):
    if typ == "icon":
        return f'<span class="lead fi32">{ic(k or "inbox", 16)}</span>'
    if typ == "avatar":
        return f'<span class="lead av32 im-{k or "an"}" role="img" aria-label="Ảnh lái xe"></span>'
    if typ == "picon":
        return f'<span class="lead pic im-pi-{k or "vcb"}" aria-hidden="true"></span>'
    if typ == "plogo":
        return f'<span class="lead plogo im-pl-{k or "vcb"}" aria-hidden="true"></span>'
    if typ == "veh":
        return f'<span class="lead veh im-{k or "tractor"}" aria-hidden="true"></span>'
    return ""


TYPES = [("ctl", "Radio button"), ("icon", "Icon simple"), ("card", "Icon card"), ("avatar", "Avatar"),
         ("picon", "Payment icon"), ("plogo", "Payment logo"), ("veh", "Vehicle")]
PH = {"t": "Tiêu đề lựa chọn", "s": "4 chuyến/tuần", "d": "Mô tả ngắn cho lựa chọn này.", "p": "4.500.000 ₫", "b": "Ưu đãi"}


def gx(typ, kind="radio", on=False, st="", mob=False, t=PH["t"], s=PH["s"], d=PH["d"], k=None, price=PH["p"], badge=PH["b"], attrs=""):
    """kind = radio | check · st = '' | h | f | d"""
    size = "md" if mob else "sm"
    c = (rd if kind == "radio" else cb)("on" if on else "off", size, "d" if st == "d" else "")
    ctl = f'<span class="ctl">{c}</span>'
    cls = f'gx{" m" if mob else ""}{" on" if on else ""} {st}'
    if typ == "card":
        bdg = f'<span class="bdg"><i></i>{badge}</span>'
        pr = (f'<span class="prw">{bdg}<span class="pr"><b>{price}</b><span>/chuyến</span></span></span>' if mob else
              f'<span class="prw"><span class="pr"><b>{price}</b><span>/chuyến</span></span><span class="sp"></span>{bdg}</span>')
        return (f'<label class="{cls} card" {attrs}><span class="hd">{lead("icon", k)}<span class="tt">{t}</span>{ctl}</span>'
                f'<span class="bd2">{pr}<span class="ds">{d}</span></span></label>')
    txt = f'<span class="tx"><span class="tr"><span class="tt">{t}</span>{f"<span class=sd>· {s}</span>" if s else ""}</span><span class="ds">{d}</span></span>'
    if typ == "ctl":
        return f'<label class="{cls}" {attrs}>{ctl}{txt}</label>'
    return f'<label class="{cls}" {attrs}>{lead(typ, k)}{txt}{ctl}</label>'


GST = [("", "Default"), ("h", "Hover"), ("f", "Focus"), ("d", "Disabled")]


def gx_matrix(kind, mob=False):
    out = ""
    for typ, tn in TYPES:
        tn = "Checkbox" if (typ == "ctl" and kind == "check") else tn
        cells = "".join(f'<div class="gcell"><div class="vl">Checked={"True" if on else "False"} · {sn}</div>{gx(typ, kind, on, st, mob)}</div>'
                        for on in (False, True) for st, sn in GST)
        out += f'<div><div class="vh">Type={tn}</div><div class="ggrid{" m" if mob else ""}">{cells}</div></div>'
    return out


# Nội dung ngữ cảnh cho set Radio group / Checkbox group (Figma 6814:843 · 6814:1350)
GROUPS = [
    ("ctl", "Radio button", [("Giao tiêu chuẩn", "2–3 ngày", "Xe ghép tuyến, cước thấp nhất.", None, None),
                             ("Giao nhanh", "trong ngày", "Xe riêng, ưu tiên điều phối.", None, None),
                             ("Hẹn giờ giao", "theo lịch", "Chọn khung giờ nhận hàng tại kho.", None, None)]),
    ("icon", "Icon simple", [("Chuyến một chiều", "1 điểm giao", "Xe chạy rỗng khi quay đầu.", "arrow-r", None),
                             ("Chuyến hai chiều", "có hàng về", "Ghép hàng chiều về, giảm cước.", "map-pin", None),
                             ("Chuyến nhiều điểm", "tối đa 5 điểm", "Gom nhiều điểm trên một tuyến.", "route", None)]),
    ("card", "Icon card", [("Container 20'", "3.200.000 ₫", "Hàng nặng, thể tích nhỏ.", "box", "Tiết kiệm"),
                           ("Container 40'", "4.500.000 ₫", "Phổ biến nhất cho hàng xuất khẩu.", "box", "Phổ biến"),
                           ("Container 45'", "5.100.000 ₫", "Hàng nhẹ, cần nhiều thể tích.", "truck", "Hàng cồng kềnh")]),
    ("avatar", "Avatar", [("Nguyễn Văn An", "29C-123.45", "Lái xe đầu kéo · 8 năm", "an", None),
                          ("Trần Minh Đức", "51D-678.90", "Lái xe đầu kéo · 5 năm", "duc", None),
                          ("Lê Thị Hoa", "15C-246.80", "Lái xe tải nhẹ · 3 năm", "hoa", None)]),
    ("picon", "Payment icon", [("Vietcombank", "**** 4821", "Tài khoản thu cước chính", "vcb", None),
                               ("Techcombank", "**** 0937", "Tài khoản chi tạm ứng", "tcb", None),
                               ("MB Bank", "**** 1150", "Tài khoản dự phòng", "mb", None)]),
    ("veh", "Vehicle", [("Đầu kéo 29C-123.45", "cách kho 3 km", "Sẵn sàng nhận chuyến", "tractor", None),
                        ("Xe tải 29H-456.78", "bảo dưỡng", "Đang bảo dưỡng, xong lúc 14:00", "truck", "d"),
                        ("Đầu kéo 51D-678.90", "cách kho 12 km", "Sẵn sàng nhận chuyến", "tractor", None)]),
    ("plogo", "Payment logo", [("Vietcombank", "**** 4821", "Tài khoản thu cước chính", "vcb", None),
                               ("Techcombank", "**** 0937", "Tài khoản chi tạm ứng", "tcb", None),
                               ("MB Bank", "**** 1150", "Tài khoản dự phòng", "mb", None)]),
]


def group(kind, typ, items, mob=False):
    out = ""
    for i, (t, s, d, k, x) in enumerate(items):
        on = i == 0 or (kind == "check" and i == 2 and typ != "veh")
        st = "d" if x == "d" else ""
        if typ == "card":
            out += gx(typ, kind, on, st, mob, t=t, d=d, k=k, price=s, badge=x)
        else:
            out += gx(typ, kind, on, st, mob, t=t, s=s, d=d, k=k)
    role = "radiogroup" if kind == "radio" else "group"
    return f'<div class="gset" role="{role}">{out}</div>'


def groups(kind, mob=False):
    return "".join(f'<div><div class="vh">Type={"Checkbox" if (typ == "ctl" and kind == "check") else tn}</div>{group(kind, typ, items, mob)}</div>'
                   for typ, tn, items in GROUPS)


def ta(value="", st="", ph="Nhập lý do huỷ…", counter=None, resize=True, err=None, hint=None, label="Lý do", req=True, attrs="",
       help_=False, cnt_err=False, rz_all=False):
    body = f'<span class="tv">{value}</span>' if value else f'<span class="tph">{ph}</span>'
    lock = f'<span class="lk">{ic("lock", 14)}</span>' if st == "ro" else ""
    rz = '<i class="rz"></i>' if resize and (rz_all or st not in ("d", "ro")) else ""
    foot = ""
    if err:
        foot = f'<span class="msg err"><span class="ei">{ic("err", 14)}</span>{err}</span>'
    elif hint:
        foot = f'<span class="msg">{hint}</span>'
    cnt = f'<span class="cnt{" err" if cnt_err else ""}">{counter}</span>' if counter else ""
    r = '<span class="req">*</span>' if req else ""
    h = f'<span class="hi">{ic("help", 14)}</span>' if help_ else ""
    return (f'<div class="taf" {attrs}><span class="flb">{label}{r}{h}</span><div class="ta {st}">{body}{lock}{rz}</div>'
            f'<div class="fft">{foot}<span class="sp"></span>{cnt}</div></div>')


SCREEN_CSS = """
.vh.xh{font-size:15px}.vh.xt{margin-top:16px}.row.xr40{align-items:flex-start;gap:40px;flex-wrap:wrap}.row.xr32{align-items:flex-start;gap:32px;flex-wrap:wrap}
.vl.xpt{padding-top:2px}.vl.xmb{margin-bottom:6px}.vl.xm18{margin:18px 0 8px}.vl.xm8{margin:8px 0 2px}.xg4{display:grid;grid-template-columns:repeat(4,1fr);gap:20px 24px}
.ggrid{display:grid;grid-template-columns:repeat(2,560px);gap:12px 24px}.ggrid.m{grid-template-columns:1fr}
.gcell{display:flex;flex-direction:column;gap:6px}
.gsets{display:grid;grid-template-columns:repeat(2,560px);gap:28px 24px;align-items:start}.gsets.m{grid-template-columns:1fr}
.lmx{display:grid;gap:14px 16px;align-items:start}
.mlist{background:var(--color-bg-primary)}
.mrow{display:flex;align-items:center;gap:12px;padding:12px 16px;min-height:56px;border-bottom:1px solid var(--color-border-secondary)}
.mrow .lt{flex:1;min-width:0;display:flex;flex-direction:column}.mrow .lb{font:500 15px/20px var(--font-body)}.mrow .hn{font-size:13px;line-height:18px;color:var(--color-text-tertiary)}
[data-D2=a] .mrow>.cb,[data-D2=a] .mrow>.rd,[data-D2=a] .mrow>.tgl{order:3}
.mrow>.cb,.mrow>.rd{width:20px;height:20px}.mrow>.cb svg{width:14px;height:14px}.mrow>.rd.on::after{width:8px;height:8px}
[data-D3=b] .mrow.p{background:transparent}
.mrow.p{background:var(--color-bg-selected)}
.mrow .tag{font:600 12px/18px var(--font-body);padding:0 8px;border-radius:999px;background:var(--color-utility-red-50);color:var(--color-utility-red-700)}
.msec{font:600 13px/18px var(--font-body);color:var(--color-text-tertiary);padding:16px 16px 6px}
/* Màn web */
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px;max-width:960px}
.stack{display:flex;flex-direction:column;gap:12px}
.box{padding:20px}
.foot{display:flex;gap:8px;justify-content:flex-end;padding:16px 20px;border-top:1px solid var(--color-border-secondary)}
.bt{height:var(--control-height-md);padding:0 var(--control-padding-x-md);border-radius:var(--radius-control);font:600 14px var(--font-body);border:1px solid var(--color-border-primary);background:var(--color-bg-primary);color:var(--color-text-primary);cursor:pointer}
.bt.dz{background:var(--color-bg-error-solid);border-color:transparent;color:var(--color-text-inverse)}
.bt.full{width:100%;height:52px;border-radius:var(--radius-control)}
.bt.pri{background:var(--color-action-primary);color:var(--color-text-inverse);border-color:transparent}
.lockbar{display:flex;gap:8px;align-items:center;padding:8px 12px;border-radius:var(--radius-md);background:var(--color-bg-secondary);color:var(--color-text-tertiary_strong);font-size:13px;margin-bottom:12px}
.tbl td:first-child,.tbl th:first-child{width:44px;padding-right:0}
.selbar{display:flex;align-items:center;gap:12px;padding:8px 16px;background:var(--color-bg-selected);border-radius:var(--radius-md);margin-bottom:8px;font-size:13px}
.vcol{display:flex;flex-direction:column;gap:10px}
"""

CSS = tok_css() + """
/* ===== Checkbox ===== */
.cb{position:relative;display:inline-grid;place-items:center;flex:none;width:16px;height:16px;border-radius:4px;border:1px solid var(--color-border-input);
 background:var(--color-bg-primary);color:var(--color-text-inverse);transition:background var(--duration-fast) var(--easing-standard)}
.cb.md{width:20px;height:20px;border-radius:6px}
.cb svg{width:12px;height:12px}.cb.md svg{width:14px;height:14px}
.cb.on,.cb.ind{background:var(--color-action-primary);border-color:var(--color-action-primary)}
.cb.h{background:var(--color-bg-primary_hover);border-color:var(--color-text-primary)}.cb.on.h,.cb.ind.h{background:var(--color-action-primary-hover);border-color:var(--color-action-primary-hover)}
.cb.p{background:var(--color-bg-selected);border-color:var(--color-text-primary)}.cb.on.p,.cb.ind.p{background:var(--color-action-primary-pressed)}
.cb.f,.rd.f,.tgl.f{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.cb.d,.rd.d{background:var(--color-bg-disabled);border-color:var(--color-border-disabled);color:var(--color-text-disabled)}
/* ===== Radio ===== */
.rd{position:relative;display:inline-block;flex:none;width:16px;height:16px;border-radius:50%;border:1px solid var(--color-border-input);background:var(--color-bg-primary)}
.rd.md{width:20px;height:20px}
.rd.on{background:var(--color-action-primary);border-color:var(--color-action-primary)}
.rd.on::after{content:"";position:absolute;inset:0;margin:auto;width:6px;height:6px;border-radius:50%;background:var(--color-text-inverse)}
.rd.md.on::after{width:8px;height:8px}
.rd.h{background:var(--color-bg-primary_hover);border-color:var(--color-text-primary)}.rd.on.h{background:var(--color-action-primary-hover)}
.rd.p{background:var(--color-bg-selected);border-color:var(--color-text-primary)}.rd.on.p{background:var(--color-action-primary-pressed)}
.cb.d.on,.cb.d.ind,.rd.d.on{background:var(--color-text-disabled);border-color:var(--color-text-disabled);color:var(--color-text-inverse)}
.rd.d.on::after{background:var(--color-text-inverse)}
/* ===== Toggle — D1 rãnh khi tắt ===== */
.tgl{--tw:36px;--th:20px;--k:16px;position:relative;display:inline-block;flex:none;width:var(--tw);height:var(--th);border-radius:999px;background:var(--tg-off);transition:background var(--duration-fast) var(--easing-standard)}
.tgl.md{--tw:44px;--th:24px;--k:20px}
.tgl i{position:absolute;top:2px;left:2px;width:var(--k);height:var(--k);border-radius:50%;background:var(--color-fg-white);box-shadow:var(--shadow-sm);transition:transform var(--duration-fast) var(--easing-standard)}
.tgl.on i{transform:translateX(calc(var(--tw) - var(--th)))}
.tgl.on{background:var(--color-action-primary)}.tgl.on.h{background:var(--color-action-primary-hover)}.tgl.on.p{background:var(--color-action-primary-pressed)}
.pv,.op{--tg-off:var(--color-border-input);--tg-off-h:var(--color-fg-tertiary)}
[data-D1=b]{--tg-off:var(--color-bg-quaternary);--tg-off-h:var(--color-bg-quaternary_hover)}
[data-D1=b] .tgl:not(.on){box-shadow:inset 0 0 0 1px var(--color-border-input)}
[data-D1=c]{--tg-off:var(--color-bg-quaternary_hover);--tg-off-h:var(--color-fg-quaternary)}
.pv[data-theme=dark],.pv[data-theme=dark] .op{--tg-off:var(--color-border-input);--tg-off-h:var(--color-fg-tertiary)}
.pv[data-theme=dark] [data-D1=b],.pv[data-theme=dark][data-D1=b]{--tg-off:var(--color-bg-quaternary)}
.pv[data-theme=dark] [data-D1=c],.pv[data-theme=dark][data-D1=c]{--tg-off:var(--color-bg-quaternary_hover)}
.tgl.h:not(.on){background:var(--tg-off-h)}.tgl.p:not(.on){background:var(--tg-off-h)}
.tgl.p i{width:calc(var(--k) + 4px)}.tgl.on.p i{transform:translateX(calc(var(--tw) - var(--th) - 4px))}
.tgl.d{opacity:.5}
/* ===== Nhãn kèm (DEC-265): SM nhãn label + gợi ý caption · MD nhãn label + gợi ý body ===== */
.cl{display:inline-flex;gap:8px;align-items:flex-start;cursor:pointer;max-width:360px}
.cl.md{gap:12px}
.cl>.cb,.cl>.rd{margin-top:2px}.cl>.tgl{margin-top:0}
.cl .lt{display:flex;flex-direction:column;min-width:0}
.cl .lb{font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-primary)}
.cl .hn{font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary)}
.cl.md .hn{font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.cl.dis .lb,.cl.dis .hn{color:var(--color-text-disabled)}
/* Checkbox label bản Mobile (Figma Platform=Mobile): chữ trái, ô chọn phải, rộng 361, không Hover */
.clm{display:flex;align-items:center;gap:16px;padding:8px;width:100%;max-width:361px;cursor:pointer}
.clm .lt{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.clm .lb{font:500 15px/20px var(--font-body);color:var(--color-text-primary)}.clm .hn{font:400 14px/20px var(--font-body);color:var(--color-text-tertiary)}
.clm.dis .lb,.clm.dis .hn{color:var(--color-text-disabled)}
/* Toggle (khung SM 36×24 bọc _Toggle base 36×20) */
.tgw{display:inline-flex;align-items:center;height:24px}
/* Group item (Radio / Checkbox group item, DEC-278/283) — Web 560 · Mobile 361 */
.gx{position:relative;display:flex;align-items:flex-start;gap:12px;padding:16px;width:560px;max-width:100%;border:1px solid var(--color-border-secondary);
 border-radius:var(--radius-card);background:var(--color-bg-primary);cursor:pointer;color:var(--color-text-primary)}
.gx.m{width:100%;gap:8px}
.gx.on{border-color:var(--color-action-primary);box-shadow:inset 0 0 0 1px var(--color-action-primary)}
.gx.h{background:var(--color-bg-primary_hover)}
.gx.f{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.gx.d{background:var(--color-bg-secondary);cursor:not-allowed}.gx.d .tt,.gx.d .sd,.gx.d .ds,.gx.d .pr b,.gx.d .pr span{color:var(--color-text-disabled)}.gx.d .lead{opacity:.5}
.gx .tx{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.gx .tr{display:flex;gap:4px;align-items:baseline;min-width:0}
.gx .tt{font:500 14px/20px var(--font-body);white-space:nowrap}
.gx .sd,.gx .ds{font:400 12px/16px var(--font-body);color:var(--color-text-tertiary)}
.gx .sd{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.gx.m .tt{font-size:15px}.gx.m .sd,.gx.m .ds{font-size:13px;line-height:18px}
.gx .ctl{flex:none;display:flex;align-items:center;height:20px}
.gx .lead{flex:none;align-self:center}
.fi32{width:32px;height:32px;border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);display:grid;place-items:center;color:var(--color-fg-secondary);background:var(--color-bg-primary)}
.av32{width:32px;height:32px;border-radius:50%;background:var(--color-bg-secondary) center/cover;box-shadow:inset 0 0 0 1px var(--color-border-secondary)}
.pic{width:32px;height:32px;border-radius:var(--radius-md);background:var(--color-bg-primary) center/cover;box-shadow:inset 0 0 0 1px var(--color-border-secondary)}
.plogo{width:72px;height:32px;background:center/contain no-repeat}
.veh{width:56px;height:32px;background:center/contain no-repeat}
.gx.card{flex-direction:column;align-items:stretch;gap:0;padding:0}
.gx.card .hd{display:flex;align-items:center;gap:12px;padding:12px 20px 12px 12px;border-bottom:1px solid var(--color-border-secondary)}
.gx.card .hd .tt{flex:1}
.gx.card .bd2{display:flex;flex-direction:column;gap:4px;padding:16px}
.gx.card .prw{display:flex;align-items:center;gap:8px}
.gx.m.card .prw{flex-direction:column;align-items:flex-start;gap:16px}
.gx .pr{display:inline-flex;align-items:baseline;gap:4px}.gx .pr b{font:600 20px/28px var(--font-body)}.gx .pr span{font-size:14px;color:var(--color-text-tertiary)}
.bdg{display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px;border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);
 background:var(--color-bg-primary);font:600 12px/18px var(--font-body);color:var(--color-text-primary);white-space:nowrap}
.bdg i{width:6px;height:6px;border-radius:50%;background:currentColor}
.gset{display:flex;flex-direction:column;gap:12px}
/* ===== Textarea ===== */
.taf{display:flex;flex-direction:column;gap:6px;width:100%;max-width:var(--field-width-default)}
.taf.w{max-width:480px}
.flb{font:500 13px/18px var(--font-body);color:var(--color-text-tertiary)}.flb .req{color:var(--color-text-error-primary);margin-left:2px}
.ta{position:relative;min-height:calc(5 * var(--type-body-line-height) + 2 * var(--field-edge-inset) + 2px);padding:var(--field-edge-inset) 10px;
 border:var(--field-border-width) solid var(--color-border-input);border-radius:var(--radius-field);background:var(--color-bg-primary);
 font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body);color:var(--color-text-primary);white-space:pre-wrap;overflow:hidden}
[data-D6=b] .ta{min-height:168px}
.ta .tph{color:var(--color-text-placeholder)}
.ta .rz{position:absolute;right:3px;bottom:3px;width:8px;height:8px;background:linear-gradient(135deg,transparent 45%,var(--color-fg-quaternary) 45% 55%,transparent 55% 70%,var(--color-fg-quaternary) 70% 80%,transparent 80%)}
/* D4 hover · read only */
.ta.h{border-color:var(--color-text-primary)}
[data-D4=b] .ta.h{border-color:var(--color-border-input);background:var(--color-bg-primary_hover)}
.ta.f{border-width:var(--size-xxs);border-color:var(--color-focus-ring);padding:calc(var(--field-edge-inset) - 1px) 9px}
.ta.e{border-width:var(--size-xxs);border-color:var(--color-border-error);padding:calc(var(--field-edge-inset) - 1px) 9px}
[data-D5=b] .ta.e{border-width:1px;padding:var(--field-edge-inset) 10px}
.ta.d{background:var(--color-bg-disabled);border-color:var(--color-border-disabled);color:var(--color-text-disabled)}.ta.d .tph{color:var(--color-text-disabled)}
.ta.ro{background:var(--color-bg-secondary);border-color:var(--color-border-disabled)}
.ta .lk{position:absolute;right:10px;top:10px;color:var(--color-fg-quaternary);display:none}
[data-D4=b] .ta .lk{display:block}
.fft{display:flex;gap:8px;align-items:flex-start;min-height:16px}
.msg{font:400 12px/16px var(--font-body);color:var(--color-text-tertiary);display:flex;gap:4px;align-items:flex-start}
.msg.err{color:var(--color-text-error-primary)}
.msg .ei{display:none}[data-D5=a] .msg .ei{display:inline-flex;margin-top:1px}
.cnt{font:400 12px/16px var(--font-body);color:var(--color-text-tertiary);font-variant-numeric:tabular-nums;white-space:nowrap}
.cnt.err{color:var(--color-text-error-primary)}
.flb .hi{display:inline-flex;vertical-align:-2px;margin-left:4px;color:var(--color-fg-tertiary)}
/* App */
.pv[data-platform=mobile] .flb{font-size:13px;color:var(--color-text-tertiary)}
.pv[data-platform=mobile] .ta{background:var(--color-bg-primary);border-color:transparent;border-radius:var(--radius-field);padding:14px 16px;
 min-height:calc(5 * var(--type-body-line-height) + 28px)}
[data-D6=b] .pv[data-platform=mobile] .ta,.pv[data-platform=mobile][data-D6=b] .ta{min-height:168px}
.pv[data-platform=mobile] .ta.f,.pv[data-platform=mobile] .ta.e{padding:12px 14px}
.pv[data-platform=mobile] .ta.f{border-color:var(--color-focus-ring)}.pv[data-platform=mobile] .ta.e{border-color:var(--color-border-error)}
.pv[data-platform=mobile] .taf{max-width:none}
"""

ST = [("", "Default"), ("h", "Hover"), ("f", "Focus"), ("d", "Disabled")]
ST_T = [("", "Default"), ("h", "Hover"), ("p", "Pressed"), ("f", "Focus"), ("d", "Disabled")]


def mtx(fn, vals, states, sizes=("sm", "md")):
    cols = len(states)
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n in states)
    rows = ""
    for z in sizes:
        for v, vn in vals:
            rows += f'<div class="vl">{z.upper()} · {vn}</div>' + "".join(f"<div>{fn(v, z, s)}</div>" for s, _ in states)
    return f'<div class="vgrid" style="grid-template-columns:120px repeat({cols},64px)">{head}{rows}</div>'


# Textarea theo Figma 6658:187203: hàng 1 = mặc định (Nhãn, Hint) · hàng 2 = bật Required + Help icon + Counter
TA_ST = [("", "Placeholder"), ("h", "Hover"), ("f", "Focus"), ("", "Filled"), ("d", "Disabled"), ("e", "Error"), ("ro", "Read Only")]
TA_V1 = "Nội dung đã nhập, có thể xuống nhiều dòng."
TA_V2 = "Giao trước 10h, gọi thủ kho trước 15 phút."


def ta_grid():
    r1 = r2 = ""
    for st, n in TA_ST:
        v1 = "" if n in ("Placeholder", "Hover") else TA_V1
        v2 = "" if n in ("Placeholder", "Hover") else TA_V2
        e = st == "e"
        r1 += (f'<div><div class="vl xmb">State={n}</div>'
               f'{ta(v1, st, ph="Nhập nội dung", label="Nhãn", req=False, err="Nói rõ sai gì và cách sửa" if e else None, hint=None if e else "Gợi ý nội dung cần nhập", rz_all=True)}</div>')
        r2 += (f'<div>{ta(v2, st, ph="Nhập nội dung", label="Ghi chú giao hàng", req=True, help_=True, counter="512/500" if e else "37/500", cnt_err=e, err="Bớt 12 ký tự để gửi được." if e else None, hint=None if e else "Gợi ý nội dung cần nhập", rz_all=True)}</div>')
    g = 'class="xg4"'
    return (f'<div {g}>{r1}</div><div class="vl xm18">Mẫu bật Required + Help icon + Counter (Error = vượt giới hạn)</div><div {g}>{r2}</div>')


LB, HN = "Nhãn lựa chọn", "Mô tả ngắn giải thích lựa chọn này."


def lab_mtx(fn, vals, states, sizes=("sm", "md")):
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n in states)
    rows = ""
    for z in sizes:
        for v, vn in vals:
            rows += f'<div class="vl xpt">{z.upper()} · {vn}</div>'
            for s, _ in states:
                rows += lab(fn(v, z, s), LB, HN, z, cls="dis" if s == "d" else "")
    return f'<div class="lmx" style="grid-template-columns:96px repeat({len(states)},minmax(0,1fr))">{head}{rows}</div>'


def clm(val, st=""):
    d = st == "d"
    return f'<label class="clm{" dis" if d else ""}"><span class="lt"><span class="lb">{LB}</span><span class="hn">{HN}</span></span>{cb(val, "sm", st)}</label>'


CB_V = [("off", "False"), ("on", "True"), ("ind", "Indet.")]
TG_WRAP = lambda v, z, s: f'<span class="tgw">{tg(v, z, s)}</span>' if z == "sm" else tg(v, z, s)

VAR_WEB = f"""<div class="vt">
<div class="row xr40">
 <div><div class="vh">Checkbox <small>Size × Checked × State · 16 / 20</small></div>{mtx(cb, CB_V, ST)}</div>
 <div><div class="vh">Radio <small>Size × Checked × State</small></div>{mtx(rd, [("off", "False"), ("on", "True")], ST)}</div>
</div>
<div class="row xr40">
 <div><div class="vh">Toggle <small>SM khung 36×24 · MD 44×24 — D1 đổi rãnh tắt</small></div>{mtx(TG_WRAP, [("off", "False"), ("on", "True")], ST_T)}</div>
 <div><div class="vh">_Toggle base <small>36×20 · 44×24, phần con của Toggle và Toggle label</small></div>{mtx(tg, [("off", "False"), ("on", "True")], ST_T)}</div>
</div>
<div><div class="vh">Checkbox label <small>Platform=Web · Size × Checked × State (DEC-265)</small></div>{lab_mtx(cb, CB_V, ST)}</div>
<div><div class="vh">Radio label <small>Size × Checked × State</small></div>{lab_mtx(rd, [("off", "False"), ("on", "True")], ST)}</div>
<div><div class="vh">Toggle label <small>Size × Checked × State, có Pressed</small></div>{lab_mtx(tg, [("off", "False"), ("on", "True")], ST_T)}</div>
<div><div class="vh">Textarea <small>7 State · Label, Required, Help icon, Hint, Counter, Resize bật tắt · D4 D5 D6</small></div>{ta_grid()}</div>
<div><div class="vh">Chữ dài <small>nhãn xuống dòng; tên lựa chọn dài cắt phần phụ; Textarea tự giãn rồi cuộn</small></div>
 <div class="row xr32">
 {lab(tg("on"), "Tự động gửi SMS cho lái xe và khách hàng mỗi khi lệnh đổi giờ lấy hàng hoặc đổi điểm giao", "Áp dụng cho mọi lệnh của khách hàng hợp đồng năm, kể cả lệnh đã điều xe.")}
 {gx("icon", "radio", True, t="Chuyến nhiều điểm giao trong nội thành", s="tối đa 5 điểm, gom hàng nhiều kho", d="Gom nhiều điểm giao trên một tuyến, tính cước theo km thực chạy.", k="route")}
 {ta("Khách hàng báo huỷ vì tàu đổi lịch cập cảng sang ngày 31/10; container đã được cấp lệnh giao hàng nhưng chưa đóng phí lưu bãi. Đề nghị giữ booking, hoàn phí nâng hạ đã thu và báo lại bộ phận chứng từ để huỷ tờ khai.", "f", counter="236/500")}</div></div>
</div>"""

VAR_APP = f"""<div class="vt">
<div><div class="vh">Checkbox label <small>Platform=Mobile · MD · không Hover</small></div>
{"".join(f'<div class="vl xm8">Checked={vn} · {sn}</div>{clm(v, s)}' for v, vn in CB_V for s, sn in [("", "Default"), ("f", "Focus"), ("d", "Disabled")])}</div>
<div><div class="vh">Ô chọn trong dòng app <small>D2 vị trí · D3 Pressed</small></div>
<div class="mlist">
 <div class="mrow">{cb("on", "md")}<span class="lt"><span class="lb">Kiểm tra lốp</span><span class="hn">Áp suất, vết nứt</span></span></div>
 <div class="mrow p">{cb("off", "md", "p")}<span class="lt"><span class="lb">Kiểm tra đèn</span><span class="hn">Pressed (D3)</span></span></div>
 <div class="mrow">{rd("on", "md")}<span class="lt"><span class="lb">Kẹt xe</span></span></div>
 <div class="mrow">{tg("off", "md")}<span class="lt"><span class="lb">Chia sẻ vị trí</span><span class="hn">Rãnh tắt theo D1</span></span></div></div></div>
<div><div class="vh">Textarea <small>bản app theo mode Platform</small></div>
{ta("", "", "Mô tả sự cố…", counter="0/300", label="Ghi chú", req=False, help_=True)}
{ta("Lốp sau bên phải mòn, cần thay trước chuyến chiều.", "f", counter="52/300", label="Ghi chú", req=False)}
{ta("", "e", "Mô tả sự cố…", counter="0/300", label="Ghi chú", err="Nhập mô tả sự cố (tối thiểu 10 ký tự).")}</div>
</div>"""

ITEM_WEB = f"""<div class="vt">
<div class="vh xh">Radio group item <small>Platform=Web · 7 Type × Checked × State · 560 (DEC-278, DEC-283)</small></div>{gx_matrix("radio")}
<div class="vh xh xt">Checkbox group item <small>Platform=Web · cùng 7 Type, Type=Checkbox thay Radio button</small></div>{gx_matrix("check")}
</div>"""
ITEM_APP = f"""<div class="vt">
<div class="vh xh">Radio group item <small>Mobile · 361</small></div>{gx_matrix("radio", True)}
<div class="vh xh xt">Checkbox group item <small>Mobile · 361</small></div>{gx_matrix("check", True)}
</div>"""
GROUP_WEB = f"""<div class="vt">
<div class="vh xh">Radio group <small>Platform=Web · 7 Type, ví dụ ngữ cảnh vận tải</small></div><div class="gsets">{groups("radio")}</div>
<div class="vh xh xt">Checkbox group <small>Platform=Web · chọn nhiều</small></div><div class="gsets">{groups("check")}</div>
</div>"""
GROUP_APP = f"""<div class="vt">
<div class="vh xh">Radio group <small>Mobile</small></div><div class="gsets m">{groups("radio", True)}</div>
<div class="vh xh xt">Checkbox group <small>Mobile</small></div><div class="gsets m">{groups("check", True)}</div>
</div>"""

# ---------- Màn demo theo Figma (Demo · Radio groups 6819:112294 · Toggles 6819:112304 · Textarea 6819:112292 · Checkboxes 6819:112295) ----------
STATES = ["default", "filled", "error", "saving", "long"]


def by_state(m):
    """m = {state: html}; trạng thái không có bản riêng dùng bản 'default'."""
    return "".join(f'<div data-show="state:{s}">{m.get(s, m["default"])}</div>' for s in STATES)


def btn(label, kind="", attrs=""):
    return f'<button class="bt {kind}" {attrs}>{label}</button>'


DCSS = """
.dpg{padding:24px 32px;max-width:1040px}.dpg .bc{font-size:12px;color:var(--color-text-tertiary)}.dpg h1{font:600 24px/32px var(--font-display, var(--font-body));margin:4px 0 4px}
.dpg .sub{font-size:13px;color:var(--color-text-tertiary);margin-bottom:20px}
.dcard{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);background:var(--color-bg-primary);padding:20px}
.dcard .ct{font:600 16px/24px var(--font-body)}.dcard .ch{font-size:12px;line-height:16px;color:var(--color-text-tertiary);margin-bottom:12px}
.fld{margin-bottom:20px}.fld .lg{font:600 14px/20px var(--font-body);margin-bottom:8px}.fld .ctx{font-size:12px;color:var(--color-text-tertiary)}
.fld .ctxv{font-size:14px;margin-top:4px}
.ferr{font-size:13px;color:var(--color-text-error-primary);margin-top:6px}
.hrow{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.hrow .gx{width:auto}
.acts{display:flex;justify-content:flex-end;gap:8px}
.bt.sm{height:32px;padding:0 12px;font-size:13px}.bt.ghost{border-color:transparent;background:transparent}
.tlist>*{padding:12px 0;border-bottom:1px solid var(--color-border-secondary)}.tlist>*:last-child{border-bottom:0}
.tlist .cl{display:flex;max-width:none;justify-content:space-between;flex-direction:row-reverse;width:100%}
.tstat{display:flex;gap:6px;align-items:center;font-size:12px;color:var(--color-text-tertiary);margin-top:6px}
.tstat.err{color:var(--color-text-error-primary)}
.spin{width:12px;height:12px;border:2px solid var(--color-border-secondary);border-top-color:var(--color-text-primary);border-radius:50%}
.overlay{position:relative;background:var(--color-bg-secondary);min-height:560px;padding:24px 32px}
.overlay::after{content:"";position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg))}
.dlg{position:absolute;z-index:2;left:50%;top:120px;transform:translateX(-50%);width:560px;background:var(--color-bg-primary_alt);border-radius:var(--radius-overlay);padding:24px;border:1px solid var(--shadow-xl-border);box-shadow:var(--shadow-xl)}
.dlg h3{font:600 18px/28px var(--font-body);margin:0}.dlg .ds{font-size:13px;color:var(--color-text-tertiary);margin:4px 0 16px}
.dlg .taf{max-width:none}
.chip{display:inline-flex;height:22px;align-items:center;padding:0 8px;border-radius:999px;font:600 12px/16px var(--font-body)}
.chip.y{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}.chip.b{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}.chip.g{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}
.selhd{display:flex;align-items:center;gap:8px;padding:10px 16px;background:var(--color-bg-secondary);font-size:12px;font-weight:600}
.tbl tr.sel td{background:var(--color-bg-selected)}
.side{display:grid;grid-template-columns:1fr 320px;gap:24px;align-items:start}
.mpad{padding:16px}.mh{font:600 20px/28px var(--font-body);margin:8px 0 4px}.msub{font-size:14px;color:var(--color-text-tertiary);margin-bottom:16px}
.mstack{display:flex;flex-direction:column;gap:12px}
.mbtns{display:flex;flex-direction:column;gap:8px;padding:16px}
.bt.pill{height:48px;border-radius:var(--radius-control);width:100%;font-size:15px}
.bt.dis{background:var(--color-bg-disabled);color:var(--color-text-disabled);border-color:transparent}
.bt.sec{background:var(--color-action-secondary);color:var(--color-text-primary);border-color:transparent}
.mgrp{background:var(--color-bg-secondary);padding:12px 16px}.mgt{font:600 12px/18px var(--font-body);color:var(--color-text-tertiary);letter-spacing:.3px;margin-bottom:8px}
.mcard{background:var(--color-bg-primary);border-radius:var(--radius-card);padding:0 12px}
.mcard>*{border-bottom:1px solid var(--color-border-secondary)}.mcard>*:last-child{border-bottom:0}
.mcard .clm{max-width:none;padding:12px 0}
.ordc{display:flex;gap:12px;align-items:center;border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);padding:12px;margin-bottom:16px}
.dpg .stack .cl{max-width:none}.dpg .tbl td,.dpg .tbl th,.overlay .tbl td,.overlay .tbl th{white-space:nowrap}
.ordc b{font-size:14px}.ordc span{font-size:12px;color:var(--color-text-tertiary)}
"""

# 1 · Radio · web: Tạo đề nghị thanh toán hộ
PAYS = [("Chuyển khoản", "Chuyển tiền vào tài khoản của bên nhận, đính kèm uỷ nhiệm chi làm chứng từ."),
        ("Tiền mặt", "Kế toán hoặc lái xe chi trực tiếp, cần phiếu chi có chữ ký người nhận."),
        ("Bù trừ công nợ", "Trừ vào khoản phải thu của khách hàng ở kỳ đối soát tiếp theo.")]
FEES = [("Phí cầu đường", "Vé BOT, trạm thu phí phát sinh trên tuyến."), ("Phí nâng hạ container", "Nâng, hạ container tại cảng hoặc depot."),
        ("Phí lưu bãi", "Lưu container, lưu xe quá thời gian miễn phí.")]


def pay_form(err=False):
    pays = "".join(lab(rd("on" if (i == 0 and not err) else "off"), t, h, attrs='data-cmp data-js="pick"') for i, (t, h) in enumerate(PAYS))
    fees = "".join(gx("icon", "radio", i == 1, t=t, s="4 chuyến/tuần", d=d, attrs="data-cmp") for i, (t, d) in enumerate(FEES))
    e = '<div class="ferr">Chọn một hình thức thanh toán.</div>' if err else ""
    return (f'<div class="dpg"><div class="bc">Thanh toán hộ  /  Tạo đề nghị</div><h1>Tạo đề nghị thanh toán hộ</h1><div style="height:16px"></div>'
            f'<div class="dcard"><div class="fld"><div class="ctx">Lệnh vận tải</div><div class="ctxv">LVT-2026-10-0142 · Xe 51C-123.45 · Lái xe Nguyễn Văn Hùng · Cảng Cát Lái → KCN Sóng Thần</div></div>'
            f'<div class="fld" role="radiogroup"><div class="lg">Hình thức thanh toán</div><div class="stack">{pays}</div>{e}</div>'
            f'<div class="fld" role="radiogroup"><div class="lg">Loại phí</div><div class="hrow">{fees}</div></div>'
            f'<div class="acts">{btn("Huỷ", "sm ghost")}{btn("Gửi đề nghị", "sm pri", "data-js=submit")}</div></div></div>')


PAY = by_state({"default": pay_form(), "error": pay_form(True)})

# 2 · Radio + Textarea · app: Lý do huỷ chuyến
REAS = [("Khách hàng huỷ đơn", "Khách báo không còn nhu cầu vận chuyển."), ("Xe gặp sự cố", "Hỏng hóc, tai nạn hoặc xe chưa đủ điều kiện lưu thông."),
        ("Lái xe không thể nhận chuyến", "Ốm, việc gia đình hoặc đã hết giờ lái cho phép."), ("Hàng chưa sẵn sàng", "Cảng hoặc kho chưa giao được container theo lịch."),
        ("Lý do khác", "Ghi rõ lý do ở bước tiếp theo.")]


def cancel_app(other=False):
    rs = "".join(lab(rd("on" if (other and i == 4) else "off", "md"), t, h, "md", attrs="data-cmp") for i, (t, h) in enumerate(REAS))
    t = ta("Khách đổi kho nhận hàng sang KCN Tân Tạo, cần tạo chuyến mới.", "f", label="Mô tả lý do", attrs="data-cmp") if other else ""
    b = btn("Xác nhận huỷ chuyến", "pill dz") if other else btn("Xác nhận huỷ chuyến", "pill dis")
    return (f'<div class="mpad"><div class="mh">Lý do huỷ chuyến</div><div class="msub">Chuyến CH-2026-10-0088 · Xe 51C-123.45</div>'
            f'<div class="mstack" role="radiogroup">{rs}</div><div style="margin-top:16px">{t}</div></div><div class="mbtns">{b}{btn("Quay lại", "pill sec")}</div>')


CANCEL_APP = by_state({"default": cancel_app(), "filled": cancel_app(True)})

# 3 · Toggle · web: Cấu hình tham số khách
PARAMS = [("Cho phép tạm ứng dưới ngưỡng", "Đề nghị tạm ứng dưới ngưỡng được duyệt tự động; trên ngưỡng vẫn chờ kế toán duyệt.", "on"),
          ("Nhắc lịch bảo dưỡng trước hạn", "Gửi thông báo cho đội xe và lái xe khi đầu kéo sắp đến hạn bảo dưỡng.", "on"),
          ("Tự động đối soát sao kê", "Khớp giao dịch sao kê ngân hàng với phiếu chi mỗi ngày; giao dịch lệch chuyển kế toán xử lý.", "off"),
          ("Bắt buộc ảnh chứng từ khi hoàn ứng", "Lái xe phải chụp hoá đơn, phiếu cân trước khi gửi đề nghị hoàn ứng.", "on"),
          ("Cho phép đổi đầu kéo giữa chuyến", "Điều độ đổi xe trên lệnh vận tải đang chạy mà không phải huỷ và cấp lệnh mới.", "off"),
          ("Xuất hoá đơn điện tử tự động", "Chưa dùng được: khách chưa kết nối nhà cung cấp hoá đơn điện tử. Liên hệ quản trị hệ thống để kết nối.", "d")]


def params(mode=""):
    rows = ""
    for i, (t, h, v) in enumerate(PARAMS):
        st, val, extra = ("d", "off", "") if v == "d" else ("", v, "")
        if i == 2 and mode == "saving":
            st, val, extra = "d", "on", '<div class="tstat"><i class="spin"></i>Đang lưu…</div>'
        if i == 2 and mode == "error":
            extra = '<div class="tstat err">' + ic("err", 14) + 'Chưa lưu được. Thử lại.</div>'
        rows += f'<div>{lab(tg(val, st=st), t, h, cls="dis" if st == "d" else "", attrs="data-cmp")}{extra}</div>'
    return (f'<div class="dpg"><div class="bc">Quản trị  /  Khách hàng  /  Delta Logistics</div><h1>Cấu hình tham số khách</h1>'
            f'<div class="sub">Bật/tắt có hiệu lực ngay cho mọi lệnh vận tải tạo sau thời điểm đổi.</div>'
            f'<div class="dcard" style="max-width:var(--width-lg)"><div class="ct">Vận hành &amp; tài chính</div><div class="ch">6 tham số · thay đổi được ghi vào nhật ký cấu hình</div>'
            f'<div class="tlist">{rows}</div></div></div>')


PARAM = by_state({"default": params(), "saving": params("saving"), "error": params("error")})

# 4 · Toggle · app: Cài đặt thông báo (D2: công tắc bên phải)
NOTIF = [("Lệnh vận tải mới", "Báo ngay khi điều độ giao lệnh vận tải cho bạn.", "on"), ("Nhắc giờ nhận hàng", "Nhắc trước giờ hẹn nhận hàng tại kho để bạn kịp xuất phát.", "on"),
         ("Kết quả tạm ứng", "Báo khi kế toán duyệt hoặc từ chối đề nghị tạm ứng của bạn.", "on"), ("Hạn đăng kiểm, bảo hiểm xe", "Nhắc khi giấy tờ của đầu kéo, rơ-moóc bạn đang lái sắp hết hạn.", "off")]
NOTIF_APP = (f'<div class="mpad" style="padding-bottom:4px"><div class="mh">Cài đặt thông báo</div><div class="msub">Đổi có hiệu lực ngay trên máy này.</div></div>'
             f'<div class="mgrp"><div class="mgt">CHUYẾN &amp; CHI PHÍ</div><div class="mcard">'
             + "".join(f'<label class="clm" data-cmp><span class="lt"><span class="lb">{t}</span><span class="hn">{h}</span></span>{tg(v, "md")}</label>' for t, h, v in NOTIF)
             + '</div></div>')

# 5 · Textarea · web: Từ chối hoá đơn (dialog)
INV = [("HD-2026-00128", "Công ty TNHH Vận tải Minh Phát", "LVT-2026-10-0412", "12.450.000 ₫"), ("HD-2026-00131", "Kho bãi Tân Cảng Sóng Thần", "LVT-2026-10-0418", "3.200.000 ₫"),
       ("HD-2026-00135", "Trạm dầu Petrolimex Bình Dương", "LVT-2026-10-0421", "8.760.000 ₫")]
INV_TBL = ('<h1 style="font:600 22px/30px var(--font-body);margin:0 0 16px">Hoá đơn đầu vào chờ duyệt</h1><table class="tbl card"><tr><th>Số hoá đơn</th><th>Nhà cung cấp</th><th>Lệnh vận tải</th><th>Số tiền</th></tr>'
           + "".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td class="mono">{c}</td><td>{d}</td></tr>' for a, b, c, d in INV) + "</table>")


def reject(mode):
    ph = "Ví dụ: sai mã số thuế bên mua, thiếu số lệnh vận tải"
    if mode == "filled":
        t = ta("Sai mã số thuế bên mua, cần xuất lại.", "f", ph, counter="37/500", hint="Kế toán nhà cung cấp sẽ nhận lý do này qua email.", label="Lý do từ chối", attrs="data-cmp")
    elif mode == "error":
        t = ta("", "e", ph, err="Nhập lý do để kế toán biết cần sửa gì.", label="Lý do từ chối", attrs="data-cmp")
    else:
        t = ta("", "", ph, counter="0/500", hint="Kế toán nhà cung cấp sẽ nhận lý do này qua email.", label="Lý do từ chối", attrs="data-cmp")
    return (f'<div class="overlay">{INV_TBL}<div class="dlg" role="dialog"><h3>Từ chối hoá đơn</h3>'
            f'<div class="ds">HD-2026-00128 · Công ty TNHH Vận tải Minh Phát · 12.450.000 ₫. Hoá đơn sẽ trả về kế toán nhà cung cấp kèm lý do.</div>{t}'
            f'<div class="acts" style="margin-top:16px">{btn("Huỷ", "sm ghost")}{btn("Từ chối hoá đơn", "sm dz", "data-js=submit")}</div></div></div>')


REJECT = by_state({"default": reject("default"), "filled": reject("filled"), "error": reject("error")})

# 6 · Textarea · app: Báo sự cố
INC = "Xe 51C-123.45 xì lốp sau bên phải tại km 32 QL1A, hướng đi Bình Dương. Đã bật đèn cảnh báo và đặt biển phía sau xe."
INC_LONG = INC + " Hàng là 1 container 40HC lạnh, nhiệt độ đang giữ -18°C, máy lạnh chạy bình thường. Đã gọi điều phối nhưng chưa liên lạc được, đang chờ cứu hộ của hãng lốp; dự kiến thay xong trong 90 phút, có thể trễ giờ giao tại kho KCN VSIP 1 so với lịch hẹn ban đầu với thủ kho ca chiều, cần báo khách hàng dời giờ nhận hàng sang 16:30 hôm nay."


def incident(mode):
    hint = "Ghi rõ vị trí, tình trạng xe và hàng."
    if mode == "filled":
        t, b = ta(INC, "f", counter="115/500", hint=hint, label="Mô tả sự cố", attrs="data-cmp"), btn("Gửi báo cáo sự cố", "pill pri")
    elif mode == "long":
        t, b = ta(INC_LONG, "e", counter="512/500", cnt_err=True, err="Bớt 12 ký tự để gửi được.", label="Mô tả sự cố", attrs="data-cmp"), btn("Gửi báo cáo sự cố", "pill dis")
    else:
        t, b = ta("", "", "Mô tả vị trí, tình trạng xe và hàng", counter="0/500", hint=hint, label="Mô tả sự cố", attrs="data-cmp"), btn("Gửi báo cáo sự cố", "pill dis")
    return (f'<div class="mpad"><div class="ordc">{ic("truck", 20)}<div><b>LVT-2026-10-0412</b><br><span>Xe 51C-123.45 · Cát Lái → KCN VSIP 1</span></div></div>{t}</div>'
            f'<div class="mbtns">{b}</div>')


INCIDENT = by_state({"default": incident("default"), "filled": incident("filled"), "long": incident("long"), "error": incident("long")})

# 7 · Checkbox · web: Lệnh vận tải chọn nhiều + Quyền truy cập
ORD = [("LVT-2610-0012", "Thép Bắc Hải", "Cảng Đình Vũ → KCN Quế Võ", "15C-123.45", "Chưa gán", "y", "Chờ gán lái xe", True),
       ("LVT-2610-0013", "Sữa Đồng Xanh", "Cảng Lạch Huyện → KCN VSIP", "15C-234.56", "Chưa gán", "y", "Chờ gán lái xe", True),
       ("LVT-2610-0014", "Nhựa Tiền Phong Mới", "ICD Mỹ Đình → Phố Nối A", "29H-345.67", "Nguyễn Văn Hùng", "b", "Đang chạy", False),
       ("LVT-2610-0015", "Điện tử Hoa Sen", "Cảng Đình Vũ → KCN Bá Thiện", "15C-456.78", "Chưa gán", "y", "Chờ gán lái xe", True),
       ("LVT-2610-0016", "May mặc Sông Hồng", "KCN Yên Phong → Cảng Đình Vũ", "99H-567.89", "Trần Minh Đức", "g", "Hoàn thành", False),
       ("LVT-2610-0017", "Gạch men Á Châu", "Cảng Cái Lân → Đông Anh", "14C-678.90", "Lê Quốc Bảo", "b", "Đang chạy", False)]
PERMS = [("Xem lệnh vận tải", "Xem danh sách và chi tiết mọi lệnh của chi nhánh.", "on", ""), ("Tạo và sửa lệnh vận tải", "Tạo lệnh mới, sửa lệnh chưa giao cho lái xe.", "on", ""),
         ("Gán lái xe cho lệnh", "Chọn lái xe và đầu kéo cho lệnh đang chờ gán.", "off", ""), ("Duyệt chi phí chuyến", "Chỉ Kế toán trưởng được cấp quyền này.", "off", "d")]
BULK = (f'<div class="dpg" style="max-width:none"><h1>Lệnh vận tải</h1><div class="sub">Chi nhánh Hải Phòng · 26/10/2026</div><div class="side">'
        f'<div class="card" style="overflow:hidden"><div class="selhd"><span>Đã chọn 3 lệnh</span><span class="sp"></span>{btn("Xuất", "sm ghost")}{btn("Gán lái xe", "sm pri")}</div>'
        f'<table class="tbl"><tr><th>{cb("ind")}</th><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Xe</th><th>Lái xe</th><th>Trạng thái</th></tr>'
        + "".join(f'<tr class="{"sel" if s else ""}"><td data-cmp>{cb("on" if s else "off")}</td><td class="mono">{c}</td><td>{k}</td><td>{r}</td><td>{x}</td><td>{d}</td><td><span class="chip {cl}">{stt}</span></td></tr>'
                  for c, k, r, x, d, cl, stt, s in ORD)
        + '</table></div><div class="dcard"><div class="ct" style="font-size:14px">Quyền truy cập</div><div class="ch">Vai trò Điều phối viên · áp dụng cho chi nhánh Hải Phòng</div><div class="stack">'
        + "".join(lab(cb(v, st=st), t, h, cls="dis" if st else "", attrs="data-cmp") for t, h, v, st in PERMS) + '</div></div></div></div>')

# 8 · Checkbox · app: Kiểm tra trước chuyến
CHK6 = [("Lốp và áp suất lốp đạt chuẩn", "Không phồng, không nứt; áp suất đúng tem dán cửa."), ("Phanh và phanh tay hoạt động tốt", "Thử phanh khi xe lăn bánh chậm trong bãi."),
        ("Đèn, xi nhan và còi hoạt động", "Bật thử từng đèn, bấm còi một lần."), ("Chốt mooc và chốt container đã khoá chắc", "Kiểm 4 chốt góc và chốt mâm kéo."),
        ("Giấy tờ xe và lệnh vận tải có trên xe", "Đăng ký, đăng kiểm, bảo hiểm, lệnh LVT-2610-0014."), ("Có bình chữa cháy và tam giác cảnh báo", None)]


def checklist(n):
    rows = "".join(f'<label class="clm" data-cmp><span class="lt"><span class="lb">{t}</span>{f"<span class=hn>{h}</span>" if h else ""}</span>{cb("on" if i < n else "off")}</label>'
                   for i, (t, h) in enumerate(CHK6))
    b = btn("Xác nhận đã kiểm tra", "pill pri") if n == 6 else btn("Xác nhận đã kiểm tra", "pill dis")
    return (f'<div class="mpad" style="padding-bottom:4px"><div class="mh">Kiểm tra trước chuyến</div><div class="msub">LVT-2610-0014 · Đầu kéo 29H-345.67</div></div>'
            f'<div class="mgrp"><div class="mgt">Đã kiểm {n}/6 mục</div><div class="mcard">{rows}</div></div><div class="mbtns">{b}</div>')


CHECKLIST = by_state({"default": checklist(4), "filled": checklist(6)})



def mini(attrs, inner, platform=False):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    return f'<div class="op" {a} style="padding:16px;display:flex;gap:14px;flex-wrap:wrap;align-items:center">{inner}</div>'


def app_mini(attrs, rows):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    return f'<div class="op" {a} style="width:300px">{rows}</div>'


ROWS_D2 = (f'<div class="mlist"><div class="mrow">{cb("on", "md")}<span class="lt"><span class="lb">Kiểm tra lốp</span></span></div>'
           f'<div class="mrow">{tg("off", "md")}<span class="lt"><span class="lb">Chia sẻ vị trí</span></span></div>'
           f'<div class="mrow">{rd("on", "md")}<span class="lt"><span class="lb">Kẹt xe</span></span></div></div>')
ROWS_D3 = (f'<div class="mlist"><div class="mrow">{cb("on", "md")}<span class="lt"><span class="lb">Kiểm tra lốp</span></span></div>'
           f'<div class="mrow p">{cb("off", "md", "p")}<span class="lt"><span class="lb">Kiểm tra đèn — đang chạm</span></span></div></div>')
TOG = lambda d: mini({"D1": d}, f'{tg("off")}{tg("off", "md")}{tg("on", "md")}' + lab(tg("off"), "Chia sẻ vị trí"))

# ---------- Vòng 2 · Preview theo tổ hợp chốt 29/10 ----------
PICK = {"D1": "c", "D2": "a", "D3": "b", "D4": "a", "D5": "c", "D6": "a"}
_pa = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())
PREVIEW = {
    "version": 1, "pick": PICK,
    "changes": "Bản 29/10 theo tổ hợp chốt: rãnh Toggle tắt giữ neutral/300 (D1 = C) · app: ô chọn bên phải dòng (D2 = A), không thêm Pressed (D3 = B) · "
               "Textarea Hover đậm viền, Chỉ xem không khoá (D4 = A) · Lỗi và Focus cùng viền 2px, chỉ khác màu (D5 = C) · Textarea cao 5 dòng, tự giãn tới 10 (D6 = A). "
               "Đủ biến thể theo Figma: label, group item 7 Type, group, Textarea 2 hàng; 8 màn demo như các section Demo trên Figma.",
    "blocks": [
        {"title": "Web", "platform": "web", "note": "Checkbox · Radio · Toggle (+ _Toggle base) · 3 loại label · Textarea · Radio/Checkbox group item 7 Type · Radio/Checkbox group · chữ dài",
         "html": f'<div class="pv pvp" {_pa} data-platform="web" data-state="default">{VAR_WEB}{ITEM_WEB}{GROUP_WEB}</div>'},
        {"title": "Mobile (app)", "platform": "mobile", "note": "Checkbox label Mobile · ô chọn trong dòng (bên phải) · Textarea app · group item 361 · group",
         "frames": [f'<div class="pv pvp" {_pa} data-platform="mobile" data-state="default">{h}</div>' for h in (VAR_APP, ITEM_APP, GROUP_APP)]},
    ],
}

VALUES = [
 {"part": "Checkbox", "prop": "size", "value": 16, "platform": "Web", "size": "SM", "sel": ".cb", "cssProp": ["width", "height"], "control": True},
 {"part": "Checkbox", "prop": "size", "value": 20, "platform": "Web", "size": "MD", "sel": ".cb.md", "cssProp": ["width", "height"], "control": True},
 {"part": "Checkbox", "prop": "radius", "value": 4, "platform": "Web", "size": "SM", "sel": ".cb", "cssProp": "border-radius"},
 {"part": "Checkbox", "prop": "radius", "value": 6, "platform": "Web", "size": "MD", "sel": ".cb.md", "cssProp": "border-radius"},
 {"part": "Checkbox · Check", "prop": "size", "value": 12, "platform": "Web", "size": "SM", "sel": ".cb svg", "cssProp": ["width", "height"]},
 {"part": "Checkbox · Check", "prop": "size", "value": 14, "platform": "Web", "size": "MD", "sel": ".cb.md svg", "cssProp": ["width", "height"]},
 {"part": "Radio", "prop": "size", "value": 16, "platform": "Web", "size": "SM", "sel": ".rd", "cssProp": ["width", "height"], "control": True},
 {"part": "Radio", "prop": "size", "value": 20, "platform": "Web", "size": "MD", "sel": ".rd.md", "cssProp": ["width", "height"], "control": True},
 {"part": "Radio · Dot", "prop": "size", "value": 6, "platform": "Web", "size": "SM", "sel": ".rd.on::after", "cssProp": ["width", "height"]},
 {"part": "Radio · Dot", "prop": "size", "value": 8, "platform": "Web", "size": "MD", "sel": ".rd.md.on::after", "cssProp": ["width", "height"]},
 {"part": "Toggle", "prop": "width", "value": 36, "platform": "Web", "size": "SM", "sel": ".tgl", "cssProp": "--tw", "control": True},
 {"part": "Toggle", "prop": "height", "value": 20, "platform": "Web", "size": "SM", "sel": ".tgl", "cssProp": "--th", "control": True},
 {"part": "Toggle", "prop": "width", "value": 44, "platform": "Web", "size": "MD", "sel": ".tgl.md", "cssProp": "--tw", "control": True},
 {"part": "Toggle", "prop": "height", "value": 24, "platform": "Web", "size": "MD", "sel": ".tgl.md", "cssProp": "--th", "control": True},
 {"part": "Toggle · Knob", "prop": "size", "value": 16, "platform": "Web", "size": "SM", "sel": ".tgl", "cssProp": "--k"},
 {"part": "Toggle · Knob", "prop": "size", "value": 20, "platform": "Web", "size": "MD", "sel": ".tgl.md", "cssProp": "--k"},
 {"part": "Toggle · Knob", "prop": "inset", "value": 2, "platform": "Web", "sel": ".tgl i", "cssProp": ["top", "left"]},
 {"part": "Label", "prop": "gap", "value": 8, "platform": "Web", "size": "SM", "sel": ".cl"},
 {"part": "Label", "prop": "gap", "value": 12, "platform": "Web", "size": "MD", "sel": ".cl.md"},
 {"part": "Label", "prop": "max-width", "value": 360, "platform": "Web", "sel": ".cl"},
 {"part": "Checkbox label Mobile", "prop": "padding", "value": 8, "platform": "Mobile", "sel": ".clm"},
 {"part": "Checkbox label Mobile", "prop": "width", "value": 361, "platform": "Mobile", "sel": ".clm", "cssProp": "max-width"},
 {"part": "Group item", "prop": "padding", "value": 16, "platform": "Web", "sel": ".gx"},
 {"part": "Group item", "prop": "gap", "value": 12, "platform": "Web", "sel": ".gx"},
 {"part": "Group item", "prop": "width", "value": 560, "platform": "Web", "sel": ".gx"},
 {"part": "Group item", "prop": "width", "value": 361, "platform": "Mobile", "at": ".gx.m", "noOverride": True, "why": "bề rộng group item mobile = bề rộng màn trừ lề, 361 chỉ là kết quả trên khung 393 (DEC-324)"},
 {"part": "Group item", "prop": "gap", "value": 8, "platform": "Mobile", "sel": ".gx.m"},
 {"part": "Group item · Title", "prop": "font-size", "value": 14, "platform": "Web", "sel": ".gx .tt", "cssProp": "font", "tpl": "500 $/20px var(--font-body)"},
 {"part": "Group item · Title", "prop": "font-size", "value": 15, "platform": "Mobile", "sel": ".gx.m .tt"},
 {"part": "Group item · Lead icon", "prop": "size", "value": 32, "platform": "Web", "sel": ".fi32", "cssProp": ["width", "height"]},
 {"part": "Group item · Avatar", "prop": "size", "value": 32, "platform": "Web", "sel": ".av32", "cssProp": ["width", "height"]},
 {"part": "Group item · Payment logo", "prop": "width", "value": 72, "platform": "Web", "sel": ".plogo"},
 {"part": "Group item · Vehicle", "prop": "width", "value": 56, "platform": "Web", "sel": ".veh"},
 {"part": "Group item · Price", "prop": "font-size", "value": 20, "platform": "Web", "sel": ".gx .pr b", "cssProp": "font", "tpl": "600 $/28px var(--font-body)"},
 {"part": "Group item · Badge", "prop": "height", "value": 22, "platform": "Web", "sel": ".bdg"},
 {"part": "Group", "prop": "gap", "value": 12, "platform": "Web", "sel": ".gset"},
 {"part": "Textarea", "prop": "padding-x", "value": 10, "platform": "Web", "sel": ".ta", "cssProp": "padding", "tpl": "var(--field-edge-inset) $"},
 {"part": "Textarea · Label", "prop": "font-size", "value": 13, "platform": "Web", "sel": ".flb", "cssProp": "font", "tpl": "500 $/18px var(--font-body)"},
 {"part": "Textarea · Counter", "prop": "font-size", "value": 12, "platform": "Web", "sel": ".cnt", "cssProp": "font", "tpl": "400 $/16px var(--font-body)"},
 {"part": "Textarea", "prop": "radius", "value": 16, "platform": "Mobile", "sel": ".pv[data-platform=mobile] .ta", "cssProp": "border-radius"},
]

page = {
    "component": "Checkbox · Radio · Toggle · Textarea",
    "slug": "form-controls",
    "title": "Form controls Review",
    "subtitle": "Base component · Checkbox, Radio, Toggle (+ label, _Toggle base, group item 7 Type, group), Textarea · Checkbox/Radio/Toggle/Textarea nhóm A, Checkbox label nhóm B (DEC-280)",
    "round": "foundation",
    "brief": True,
    "preview": PREVIEW,
    "values": VALUES,
    "refs": {
        "untitled": {
            "summary": "Checkbox / Radio 16 · 20, tô <mark>màu brand</mark> khi chọn, có Indeterminate; Toggle 36×20 · 44×24, rãnh tắt <mark>bg-tertiary</mark> (xám nhạt, có viền mảnh); Textarea viền 1px, focus <mark>ring-2</mark>, lỗi viền đỏ 1px + icon, có kéo giãn.",
            "source": "design/_ref/untitled-ui/react/components/base/checkbox · radio-buttons · toggle · textarea",
        },
        "astryx": {
            "summary": "Ô chọn web theo Astryx (thẻ chọn 5795:151255), ô nhập app nền muted bo 16 không viền (DEC-099); viền ô 2px khi focus và khi lỗi (DEC-207).",
            "source": "design/design.md § Mobile — chốt Lab ↔ DS mobile · DEC-099 · DEC-207",
        },
        "usage": [
            "Hộp huỷ lệnh / từ chối hoá đơn: Radio lý do + Textarea mô tả",
            "Bảng danh sách chọn nhiều: Checkbox (Indeterminate ở đầu cột) + Toggle trong dòng",
            "App lái xe: checklist trước chuyến, ghi chú sự cố, cài đặt",
        ],
        "platform": "Nhóm A (Checkbox, Radio, Toggle, Textarea — số đo theo mode Platform) + nhóm B (Checkbox label, group item: trục Platform, app ô chọn bên phải — DEC-280/283). Đã chốt biến thể 26/10 + DEC-265/278/281. Brainstorm gọn: 6 điểm còn mở từ lượt duyệt Figma 1.",
    },
    "css": CSS,
    "states": [
        {"key": "default", "label": "Chưa nhập"},
        {"key": "filled", "label": "Đã chọn / nhập"},
        {"key": "error", "label": "Lỗi"},
        {"key": "saving", "label": "Đang lưu"},
        {"key": "long", "label": "Vượt giới hạn"},
    ],
    "ideas": [],
    "decisions": [
        {"id": "D1", "title": "Rãnh Toggle khi tắt",
         "why": "Lượt 1: rãnh tắt neutral/300 trên nền trắng chỉ <b>1,5:1</b> — <mark>trông như Disabled</mark>, không đạt 3:1 cho thành phần điều khiển (WCAG 1.4.11, mục C3).",
         "source": "Trang Duyệt Base components › C3 · Figma Toggle 6658:170547 · toggle.tsx (bg-tertiary + ring)",
         "options": [
             {"label": "Rãnh xám đậm neutral/500", "desc": "4,7:1 với nền trắng; bật = than chì, tắt = xám — vẫn khác rõ.", "rec": True, "preview": TOG("a")},
             {"label": "Rãnh nhạt + viền đạt 3:1", "desc": "Như Untitled: nền neutral/200, viền neutral/500 1px.", "preview": TOG("b")},
             {"label": "Giữ neutral/300", "desc": "Như lượt 1; chấp nhận dưới 3:1.", "preview": TOG("c")},
         ],
         "untitled": mini({"D1": "b"}, tg("off", "md")), "untitledNote": "bg-tertiary + ring-0.5",
         "astryx": mini({"D1": "c"}, tg("off", "md")), "astryxNote": "lượt 1 v2"},
        {"id": "D2", "title": "Vị trí ô chọn trên app",
         "why": "Trên app, ô chọn / công tắc thường nằm <mark>bên phải dòng</mark> (iOS, Android), ngón cái dễ với. Lượt 1: Checkbox app đặt phải, Toggle app lại đặt trái — lệch nhau (mục L9).",
         "source": "Trang Duyệt Base components › L9 · DEC-280 (Checkbox label nhóm B) · Figma 6658:175924",
         "options": [
             {"label": "Mọi control bên phải dòng", "desc": "Checkbox, Radio, Toggle đều ở phải trên app; web giữ trái.", "rec": True, "platform": "mobile", "preview": app_mini({"D2": "a"}, ROWS_D2)},
             {"label": "Bên trái như web", "desc": "Một bố cục cho cả hai nền tảng.", "platform": "mobile", "preview": app_mini({"D2": "b"}, ROWS_D2)},
         ]},
        {"id": "D3", "title": "Trạng thái Pressed cho ô chọn trên app",
         "why": "App không có Hover. Radio, Checkbox chưa có Pressed (bạn không tick ở vòng 2); Toggle, Button có. Không có phản hồi khi chạm thì dòng có vẻ không bấm được (mục R3).",
         "source": "Trang Duyệt Base components › R3",
         "options": [
             {"label": "Thêm Pressed (thay Hover)", "desc": "Ô đậm viền + cả dòng nền bg/selected khi đang chạm.", "rec": True, "platform": "mobile", "preview": app_mini({"D3": "a"}, ROWS_D3)},
             {"label": "Không thêm", "desc": "Chỉ đổi khi nhả tay.", "platform": "mobile", "preview": app_mini({"D3": "b"}, ROWS_D3.replace(' p">', '">').replace('"md", "p"', '"md"'))},
         ]},
        {"id": "D4", "title": "Textarea: Hover và Chỉ xem",
         "why": "Hover tô nền hay chỉ đậm viền; ô Chỉ xem (Read Only) có cần icon khoá để khỏi nhầm với Disabled (mục L14). <b>Figma hiện tại: Hover tô nền xám, Chỉ xem không khoá</b> — gần phương án b phần Hover.",
         "source": "Trang Duyệt Base components › L14 · Figma 6658:187203",
         "options": [
             {"label": "Đậm viền; Chỉ xem không icon", "desc": "Giống Input; Chỉ xem phân biệt bằng nền muted + chữ đậm bình thường.", "rec": True,
              "preview": mini({"D4": "a"}, ta("", "h", counter="0/500", hint="Hover") + ta("Khách đổi lịch sang 30/10.", "ro", counter="25/500", hint="Chỉ xem"))},
             {"label": "Tô nền; Chỉ xem có khoá", "desc": "Hover nền bg/primary_hover; icon khoá góc phải khi chỉ xem.",
              "preview": mini({"D4": "b"}, ta("", "h", counter="0/500", hint="Hover") + ta("Khách đổi lịch sang 30/10.", "ro", counter="25/500", hint="Chỉ xem"))},
         ]},
        {"id": "D5", "title": "Phân biệt Lỗi với Focus",
         "why": "Focus và Lỗi cùng viền 2px, chỉ khác màu (than chì / đỏ) — chụp xám hoặc người mù màu khó phân biệt (mục L5, WCAG 1.4.1).",
         "source": "Trang Duyệt Base components › L5 · DEC-207",
         "options": [
             {"label": "Thêm icon lỗi trước câu lỗi", "desc": "Giữ viền 2px; câu lỗi có icon ⓘ đỏ. Áp mọi ô nhập.", "rec": True,
              "preview": mini({"D5": "a"}, ta("Khách đổi lịch", "f", counter="14/500", hint="Focus") + ta("", "e", counter="0/500", err="Nhập lý do huỷ (tối thiểu 10 ký tự)."))},
             {"label": "Viền lỗi 1px như Untitled", "desc": "Focus 2px, Lỗi 1px đỏ + icon.",
              "preview": mini({"D5": "b"}, ta("Khách đổi lịch", "f", counter="14/500", hint="Focus") + ta("", "e", counter="0/500", err="Nhập lý do huỷ (tối thiểu 10 ký tự)."))},
             {"label": "Giữ như lượt 1", "desc": "Cùng 2px, chỉ khác màu.",
              "preview": mini({"D5": "c"}, ta("Khách đổi lịch", "f", counter="14/500", hint="Focus") + ta("", "e", counter="0/500", err="Nhập lý do huỷ (tối thiểu 10 ký tự)."))},
         ]},
        {"id": "D6", "title": "Chiều cao Textarea",
         "why": "Lượt 1 cố định 168: trên app chỉ thấy ~4,5 dòng (chữ 15/22), trên web thừa chỗ. Đề xuất cao theo số dòng: 5 dòng × line-height + lề, tự giãn tới 10 dòng rồi cuộn.",
         "source": "Trang Duyệt Base components › token field/textarea-height",
         "options": [
             {"label": "5 dòng, tự giãn tới 10", "desc": "Web 5 × 20 + 18 = 118 · app 5 × 22 + 28 = 138.", "rec": True,
              "preview": mini({"D6": "a"}, ta("Container 40' HC bị móp cửa sau.", "", counter="33/500", hint="Web"))},
             {"label": "Cố định 168", "desc": "Như lượt 1, mọi nền tảng.",
              "preview": mini({"D6": "b"}, ta("Container 40' HC bị móp cửa sau.", "", counter="33/500", hint="Web"))},
         ]},
    ],
    "presets": [
        {"id": "rec", "label": "Đề xuất", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a"}},
        {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "b", "D2": "b", "D3": "b", "D4": "a", "D5": "b", "D6": "a"}},
        {"id": "astryx", "label": "Figma lượt 1", "pick": {"D1": "c", "D2": "a", "D3": "b", "D4": "a", "D5": "c", "D6": "b"}},
    ],
    "screens": [
        {"id": "var-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none",
         "note": "Theo Figma: ô chọn, _Toggle base, Checkbox/Radio/Toggle label, Textarea 2 hàng, Radio/Checkbox group item 7 Type (Radio button, Icon simple, Icon card, Avatar, Payment icon, Payment logo, Vehicle), Radio/Checkbox group. Đổi theo D1–D6 và Light/Dark.", "html": VAR_WEB.replace('</div>\n<div><div class="vh">Chữ dài', '</div>\n<div><div class="vh">Chữ dài') + ITEM_WEB + GROUP_WEB},
        {"id": "var-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Bản Mobile: Checkbox label, ô chọn trong dòng (D2/D3), Textarea, group item 7 Type 361, Radio/Checkbox group.", "html": VAR_APP + ITEM_APP + GROUP_APP},
        {"id": "pay-web", "name": "Tạo đề nghị thanh toán hộ", "device": "web", "width": 1280, "nav": "Thanh toán hộ", "title": "Tạo đề nghị",
         "note": "Figma Demo · Radio groups: Radio label + Radio group item Icon simple. Lỗi = chưa chọn hình thức thanh toán.", "html": PAY},
        {"id": "cancel-app", "name": "Lý do huỷ chuyến", "device": "mobile", "nav": "Lệnh", "title": "Huỷ chuyến", "back": True, "tabs": False,
         "note": "Figma Demo · Radio groups: chọn Lý do khác → hiện Textarea, nút huỷ bật.", "html": CANCEL_APP},
        {"id": "param-web", "name": "Cấu hình tham số khách", "device": "web", "width": 1280, "nav": "Quản trị", "title": "Cấu hình",
         "note": "Figma Demo · Toggles: Toggle label 6 tham số, 1 Disabled; Đang lưu và Lỗi lưu.", "html": PARAM},
        {"id": "notif-app", "name": "Cài đặt thông báo", "device": "mobile", "nav": "Tôi", "title": "Cài đặt", "back": True,
         "note": "Figma Demo · Toggles: công tắc bên phải dòng (D2).", "html": NOTIF_APP},
        {"id": "reject-web", "name": "Từ chối hoá đơn", "device": "web", "width": 1280, "nav": "Hoá đơn", "title": "Hoá đơn đầu vào",
         "note": "Figma Demo · Textarea: hộp thoại, Lỗi = chưa nhập lý do, Đã nhập có Counter.", "html": REJECT},
        {"id": "incident-app", "name": "Báo sự cố", "device": "mobile", "nav": "Lệnh", "title": "Báo sự cố", "back": True, "tabs": False,
         "note": "Figma Demo · Textarea: rỗng (nút tắt), đã nhập 115/500, vượt giới hạn 512/500.", "html": INCIDENT},
        {"id": "bulk-web", "name": "Lệnh vận tải · chọn nhiều", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Lệnh vận tải",
         "note": "Figma Demo · Checkboxes: Indeterminate đầu cột, thanh Đã chọn 3 lệnh; thẻ Quyền truy cập dùng Checkbox label (1 Disabled).", "html": BULK},
        {"id": "check-app", "name": "Kiểm tra trước chuyến", "device": "mobile", "nav": "Lệnh", "title": "Kiểm tra xe", "back": True, "tabs": False,
         "note": "Figma Demo · Checkboxes: Checkbox label Mobile; 4/6 nút tắt, 6/6 nút bật.", "html": CHECKLIST},
    ],
    "proto": [
        {"sel": "[data-js=pick]", "state": "filled"},
        {"sel": "[data-js=submit]", "state": "error"},
    ],
    "protoHint": "chọn trạng thái ở Bảng chọn; màn Thanh toán hộ: bấm Gửi đề nghị",
}

page["cssScreen"] = BASE_CSS + SCREEN_CSS + DCSS
page["css"] += IMG_CSS
write(OUT, page)
