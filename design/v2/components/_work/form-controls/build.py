#!/usr/bin/env python3
"""Sinh page.json cho Form control: Checkbox · Radio · Toggle · Textarea — brainstorm gọn (28/10).
Chạy: python3 design/v2/components/_work/form-controls/build.py && python3 _scripts/ds-component-page.py form-controls
Biến thể đã chốt: trang Chốt biến thể Base (VQDsMrBW37W3QWVTPN79qC, db variants/checkbox v2, radio v1, toggle v1, textarea v6, 26/10)
+ DEC-265 (chữ nhãn theo Size), DEC-278/281/283 (group item), DEC-280 (Checkbox nhóm A, Checkbox label nhóm B).
Điểm cần quyết từ trang Duyệt Base components (41DSsnEhvrQfZ1sggELNtq), chưa trả lời: C3, L9, R3, L14, L5 + chiều cao Textarea.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import ic, tok_css, BASE_CSS, write  # noqa: E402

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


def gitem(ctrl, title, sub, price=None, on=False, st="", attrs=""):
    p = f'<span class="gp">{price}</span>' if price else ""
    return (f'<label class="gi{" on" if on else ""} {st}" {attrs}><span class="gic">{ic("truck", 18)}</span>'
            f'<span class="lt"><span class="lb">{title}</span><span class="hn">{sub}</span></span>{p}{ctrl}</label>')


def ta(value="", st="", ph="Nhập lý do huỷ…", counter=None, resize=True, err=None, hint=None, label="Lý do", req=True, attrs=""):
    body = f'<span class="tv">{value}</span>' if value else f'<span class="tph">{ph}</span>'
    lock = f'<span class="lk">{ic("lock", 14)}</span>' if st == "ro" else ""
    rz = '<i class="rz"></i>' if resize and st not in ("d", "ro") else ""
    foot = ""
    if err:
        foot = f'<span class="msg err"><span class="ei">{ic("err", 14)}</span>{err}</span>'
    elif hint:
        foot = f'<span class="msg">{hint}</span>'
    cnt = f'<span class="cnt">{counter}</span>' if counter else ""
    r = '<span class="req">*</span>' if req else ""
    return (f'<div class="taf" {attrs}><span class="flb">{label}{r}</span><div class="ta {st}">{body}{lock}{rz}</div>'
            f'<div class="fft">{foot}<span class="sp"></span>{cnt}</div></div>')


CSS = tok_css() + BASE_CSS + """
/* ===== Checkbox ===== */
.cb{position:relative;display:inline-grid;place-items:center;flex:none;width:16px;height:16px;border-radius:4px;border:1px solid var(--field-border-default);
 background:var(--color-bg-surface);color:var(--color-text-inverse);transition:background var(--duration-fast)}
.cb.md{width:20px;height:20px;border-radius:6px}
.cb svg{width:12px;height:12px}.cb.md svg{width:14px;height:14px}
.cb.on,.cb.ind{background:var(--color-action-primary);border-color:var(--color-action-primary)}
.cb.h{background:var(--color-bg-hover);border-color:var(--color-text-primary)}.cb.on.h,.cb.ind.h{background:var(--color-action-primary-hover);border-color:var(--color-action-primary-hover)}
.cb.p{background:var(--color-bg-selected);border-color:var(--color-text-primary)}.cb.on.p,.cb.ind.p{background:var(--color-action-primary-pressed)}
.cb.f,.rd.f,.tgl.f{outline:var(--focus-width) solid var(--color-border-focus);outline-offset:var(--focus-offset)}
.cb.d,.rd.d{background:var(--field-bg-disabled);border-color:var(--field-border-disabled);color:var(--color-text-tertiary)}
/* ===== Radio ===== */
.rd{position:relative;display:inline-block;flex:none;width:16px;height:16px;border-radius:50%;border:1px solid var(--field-border-default);background:var(--color-bg-surface)}
.rd.md{width:20px;height:20px}
.rd.on{background:var(--color-action-primary);border-color:var(--color-action-primary)}
.rd.on::after{content:"";position:absolute;inset:0;margin:auto;width:6px;height:6px;border-radius:50%;background:var(--color-text-inverse)}
.rd.md.on::after{width:8px;height:8px}
.rd.h{background:var(--color-bg-hover);border-color:var(--color-text-primary)}.rd.on.h{background:var(--color-action-primary-hover)}
.rd.p{background:var(--color-bg-selected);border-color:var(--color-text-primary)}.rd.on.p{background:var(--color-action-primary-pressed)}
.rd.d.on::after{background:var(--color-text-tertiary)}
/* ===== Toggle — D1 rãnh khi tắt ===== */
.tgl{--tw:36px;--th:20px;--k:16px;position:relative;display:inline-block;flex:none;width:var(--tw);height:var(--th);border-radius:999px;background:var(--tg-off);transition:background var(--duration-fast)}
.tgl.md{--tw:44px;--th:24px;--k:20px}
.tgl i{position:absolute;top:2px;left:2px;width:var(--k);height:var(--k);border-radius:50%;background:#fff;box-shadow:0 1px 3px var(--color-shadow-md);transition:transform var(--duration-fast)}
.tgl.on i{transform:translateX(calc(var(--tw) - var(--th)))}
.tgl.on{background:var(--color-action-primary)}.tgl.on.h{background:var(--color-action-primary-hover)}.tgl.on.p{background:var(--color-action-primary-pressed)}
.pv,.op{--tg-off:var(--neutral-500);--tg-off-h:var(--neutral-600)}
[data-D1=b]{--tg-off:var(--neutral-200);--tg-off-h:var(--neutral-300)}
[data-D1=b] .tgl:not(.on){box-shadow:inset 0 0 0 1px var(--field-border-default)}
[data-D1=c]{--tg-off:var(--neutral-300);--tg-off-h:var(--neutral-400)}
.pv[data-theme=dark],.pv[data-theme=dark] .op{--tg-off:var(--neutral-500);--tg-off-h:var(--neutral-400)}
.pv[data-theme=dark] [data-D1=b],.pv[data-theme=dark][data-D1=b]{--tg-off:var(--neutral-800)}
.pv[data-theme=dark] [data-D1=c],.pv[data-theme=dark][data-D1=c]{--tg-off:var(--neutral-700)}
.tgl.h:not(.on){background:var(--tg-off-h)}.tgl.p:not(.on){background:var(--tg-off-h)}
.tgl.p i{width:calc(var(--k) + 4px)}.tgl.on.p i{transform:translateX(calc(var(--tw) - var(--th) - 4px))}
.tgl.d{opacity:.5}
/* ===== Nhãn kèm (DEC-265): SM nhãn label + gợi ý caption · MD nhãn label + gợi ý body ===== */
.cl{display:inline-flex;gap:8px;align-items:flex-start;cursor:pointer;max-width:360px}
.cl.md{gap:12px}
.cl>.cb,.cl>.rd{margin-top:2px}.cl>.tgl{margin-top:0}
.cl .lt{display:flex;flex-direction:column;min-width:0}
.cl .lb{font:var(--type-label-weight) var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-primary)}
.cl .hn{font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-secondary)}
.cl.md .hn{font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.cl.dis .lb,.cl.dis .hn{color:var(--color-text-tertiary)}
/* Group item (Radio / Checkbox group, DEC-278/283) */
.gi{display:flex;align-items:flex-start;gap:12px;padding:14px 16px;border:1px solid var(--color-border-default);border-radius:var(--radius-card);background:var(--color-bg-surface);cursor:pointer;max-width:560px}
.gi.on{border-color:var(--color-action-primary);box-shadow:inset 0 0 0 1px var(--color-action-primary)}
.gi .gic{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;background:var(--color-bg-selected);color:var(--color-icon-primary);flex:none}
.gi .lt{flex:1;min-width:0;display:flex;flex-direction:column}.gi .lb{font:600 14px/20px var(--font-body)}.gi .hn{font-size:12px;line-height:16px;color:var(--color-text-secondary)}
.gi .gp{font:600 14px/20px var(--font-body);white-space:nowrap}
.gi>.rd,.gi>.cb{margin-top:2px}
/* ===== Textarea ===== */
.taf{display:flex;flex-direction:column;gap:6px;width:100%;max-width:var(--field-width-default)}
.taf.w{max-width:480px}
.flb{font:500 13px/18px var(--font-body);color:var(--field-fg-label-web)}.flb .req{color:var(--color-status-danger-text);margin-left:2px}
.ta{position:relative;min-height:calc(5 * var(--type-body-line-height) + 2 * var(--field-edge-inset) + 2px);padding:var(--field-edge-inset) 10px;
 border:var(--field-border-width) solid var(--field-border-default);border-radius:var(--radius-field);background:var(--field-bg-web);
 font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body);color:var(--field-fg-value);white-space:pre-wrap;overflow:hidden}
[data-D6=b] .ta{min-height:168px}
.ta .tph{color:var(--field-fg-placeholder)}
.ta .rz{position:absolute;right:3px;bottom:3px;width:8px;height:8px;background:linear-gradient(135deg,transparent 45%,var(--color-icon-secondary) 45% 55%,transparent 55% 70%,var(--color-icon-secondary) 70% 80%,transparent 80%)}
/* D4 hover · read only */
.ta.h{border-color:var(--color-text-primary)}
[data-D4=b] .ta.h{border-color:var(--field-border-default);background:var(--field-bg-hover)}
.ta.f{border-width:var(--field-border-width-active);border-color:var(--field-border-active);padding:calc(var(--field-edge-inset) - 1px) 9px}
.ta.e{border-width:var(--field-border-width-active);border-color:var(--field-border-error);padding:calc(var(--field-edge-inset) - 1px) 9px}
[data-D5=b] .ta.e{border-width:1px;padding:var(--field-edge-inset) 10px}
.ta.d{background:var(--field-bg-disabled);border-color:var(--field-border-disabled);color:var(--field-fg-disabled)}.ta.d .tph{color:var(--field-fg-disabled)}
.ta.ro{background:var(--field-bg-readonly);border-color:var(--field-border-disabled)}
.ta .lk{position:absolute;right:10px;top:10px;color:var(--color-icon-secondary);display:none}
[data-D4=b] .ta .lk{display:block}
.fft{display:flex;gap:8px;align-items:flex-start;min-height:16px}
.msg{font:400 12px/16px var(--font-body);color:var(--field-fg-helper);display:flex;gap:4px;align-items:flex-start}
.msg.err{color:var(--field-fg-error)}
.msg .ei{display:none;margin-top:1px}[data-D5=a] .msg .ei{display:inline-flex}
.cnt{font:400 12px/16px var(--font-body);color:var(--color-text-secondary);font-variant-numeric:tabular-nums;white-space:nowrap}
/* App */
.pv[data-platform=mobile] .flb{font-size:13px;color:var(--field-fg-label-app)}
.pv[data-platform=mobile] .ta{background:var(--field-bg-app);border-color:transparent;border-radius:16px;padding:14px 16px;
 min-height:calc(5 * var(--type-body-line-height) + 28px)}
[data-D6=b] .pv[data-platform=mobile] .ta,.pv[data-platform=mobile][data-D6=b] .ta{min-height:168px}
.pv[data-platform=mobile] .ta.f,.pv[data-platform=mobile] .ta.e{padding:12px 14px}
.pv[data-platform=mobile] .ta.f{border-color:var(--field-border-active)}.pv[data-platform=mobile] .ta.e{border-color:var(--field-border-error)}
.pv[data-platform=mobile] .taf{max-width:none}
.mlist{background:var(--color-bg-surface)}
.mrow{display:flex;align-items:center;gap:12px;padding:12px 16px;min-height:56px;border-bottom:1px solid var(--color-border-default)}
.mrow .lt{flex:1;min-width:0;display:flex;flex-direction:column}.mrow .lb{font:500 15px/20px var(--font-body)}.mrow .hn{font-size:13px;line-height:18px;color:var(--color-text-secondary)}
[data-D2=a] .mrow>.cb,[data-D2=a] .mrow>.rd,[data-D2=a] .mrow>.tgl{order:3}
.mrow>.cb,.mrow>.rd{width:20px;height:20px}.mrow>.cb svg{width:14px;height:14px}.mrow>.rd.on::after{width:8px;height:8px}
[data-D3=b] .mrow.p{background:transparent}
.mrow.p{background:var(--color-bg-selected)}
.mrow .tag{font:600 12px/18px var(--font-body);padding:0 8px;border-radius:999px;background:var(--color-chip-red-bg);color:var(--color-chip-red-fg)}
.msec{font:600 13px/18px var(--font-body);color:var(--color-text-secondary);padding:16px 16px 6px}
/* Màn web */
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px;max-width:960px}
.stack{display:flex;flex-direction:column;gap:12px}
.box{padding:20px}
.foot{display:flex;gap:8px;justify-content:flex-end;padding:16px 20px;border-top:1px solid var(--color-border-default)}
.bt{height:var(--control-height-md);padding:0 var(--control-padding-x-md);border-radius:var(--radius-control);font:600 14px var(--font-body);border:1px solid var(--button-border-outline);background:var(--color-bg-surface);color:var(--color-text-primary);cursor:pointer}
.bt.dz{background:var(--color-status-danger-solid);border-color:transparent;color:var(--color-text-inverse)}
.bt.full{width:100%;height:52px;border-radius:999px}
.bt.pri{background:var(--button-bg-primary);color:var(--button-fg-primary);border-color:transparent}
.lockbar{display:flex;gap:8px;align-items:center;padding:8px 12px;border-radius:var(--radius-md);background:var(--color-bg-muted);color:var(--color-text-secondary-strong);font-size:13px;margin-bottom:12px}
.tbl td:first-child,.tbl th:first-child{width:44px;padding-right:0}
.selbar{display:flex;align-items:center;gap:12px;padding:8px 16px;background:var(--color-bg-selected);border-radius:var(--radius-md);margin-bottom:8px;font-size:13px}
.vcol{display:flex;flex-direction:column;gap:10px}
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


TA_STATES = [("", "Placeholder", ""), ("h", "Hover", ""), ("f", "Focus", "Container 40' HC bị móp cửa sau, khách từ chối nhận."),
             ("", "Filled", "Container 40' HC bị móp cửa sau, khách từ chối nhận."), ("d", "Disabled", ""),
             ("e", "Error", ""), ("ro", "Read Only", "Khách đổi lịch lấy hàng sang 30/10.")]


def ta_grid():
    out = ""
    for st, n, v in TA_STATES:
        err = "Nhập lý do huỷ (tối thiểu 10 ký tự)." if st == "e" else None
        cnt = f"{len(v)}/500" if v else "0/500"
        out += f'<div><div class="vl" style="margin-bottom:6px">State={n}</div>{ta(v, st, counter=cnt, err=err, hint=None if err else "Khách hàng nhận được lý do này.")}</div>'
    return f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px 24px">{out}</div>'


VAR_WEB = f"""<div class="vt">
<div class="row" style="align-items:flex-start;gap:40px;flex-wrap:wrap">
 <div><div class="vh">Checkbox <small>Size × Checked × State · 16 / 20</small></div>{mtx(cb, [("off", "False"), ("on", "True"), ("ind", "Indeterminate")], ST)}</div>
 <div><div class="vh">Radio <small>Size × Checked × State</small></div>{mtx(rd, [("off", "False"), ("on", "True")], ST)}</div>
 <div><div class="vh">Toggle <small>36×20 · 44×24 — D1 đổi rãnh tắt</small></div>{mtx(tg, [("off", "False"), ("on", "True")], ST_T)}</div>
</div>
<div class="row" style="align-items:flex-start;gap:40px;flex-wrap:wrap">
 <div class="vcol"><div class="vh">Checkbox label <small>SM · MD (DEC-265)</small></div>
  {lab(cb("on"), "Thông báo cho khách hàng", "Gửi email và SMS khi lệnh huỷ.")}
  {lab(cb("off", "md"), "Thông báo cho khách hàng", "Gửi email và SMS khi lệnh huỷ.", "md")}
  {lab(cb("off", st="d"), "Hoàn phí nâng hạ", "Chỉ khi container chưa hạ bãi.", st="", cls="dis")}</div>
 <div class="vcol"><div class="vh">Radio label</div>
  {lab(rd("on"), "Khách huỷ đơn", "Khách báo trước 24 giờ.")}{lab(rd("off"), "Không có xe phù hợp")}
  {lab(rd("off", "md"), "Hàng chưa sẵn sàng", "Kho báo chưa đóng xong.", "md")}</div>
 <div class="vcol"><div class="vh">Toggle label</div>
  {lab(tg("on"), "Gửi SMS cho lái xe", "Lái xe nhận tin ngay khi lệnh đổi.")}{lab(tg("off", "md"), "Tự điều xe khi có lệnh mới", "Theo xe gần nhất còn trống.", "md")}
  {lab(tg("off", st="d"), "Chia sẻ vị trí cho khách", "Chưa bật gói theo dõi.", cls="dis")}</div>
</div>
<div><div class="vh">Radio group item <small>Type=Radio button · Web 560 (DEC-278, DEC-283)</small></div>
 <div class="vcol">{gitem(rd("on"), "Đầu kéo + mooc 40'", "51C-123.45 · Trần Văn Bình · còn trống từ 08:00", "2.450.000 ₫", on=True)}
 {gitem(rd("off"), "Xe tải 15 tấn", "51D-678.90 · Lê Minh Châu · đang chạy chuyến, xong 10:30", "1.850.000 ₫")}</div></div>
<div><div class="vh">Textarea <small>State × Phần kèm (Counter, Resize) · D4 D5 D6</small></div>{ta_grid()}</div>
<div><div class="vh">Chữ dài <small>nhãn xuống dòng tối đa 2 dòng; Textarea tự giãn rồi cuộn</small></div>
 <div class="row" style="align-items:flex-start;gap:32px">
 {lab(cb("on"), "Xác nhận đã kiểm tra seal, cửa container và chụp ảnh đủ 4 góc trước khi rời cảng", "Bắt buộc với hàng xuất khẩu và hàng có giá trị cao theo hợp đồng.")}
 {ta("Khách hàng báo huỷ vì tàu đổi lịch cập cảng sang ngày 31/10; container đã được cấp lệnh giao hàng nhưng chưa đóng phí lưu bãi. Đề nghị giữ booking, hoàn phí nâng hạ đã thu và báo lại bộ phận chứng từ để huỷ tờ khai.", "f", counter="236/500")}</div></div>
</div>"""

VAR_APP = f"""<div style="padding-bottom:16px">
<div class="msec">Checkbox · vị trí theo D2</div>
<div class="mlist">
 <div class="mrow">{cb("on", "md")}<span class="lt"><span class="lb">Kiểm tra lốp</span><span class="hn">Áp suất, vết nứt</span></span></div>
 <div class="mrow p">{cb("off", "md", "p")}<span class="lt"><span class="lb">Kiểm tra đèn</span><span class="hn">Pressed (D3)</span></span></div>
 <div class="mrow">{cb("ind", "md")}<span class="lt"><span class="lb">Giấy tờ xe</span><span class="hn">2/3 mục</span></span></div></div>
<div class="msec">Radio</div>
<div class="mlist"><div class="mrow">{rd("on", "md")}<span class="lt"><span class="lb">Kẹt xe</span></span></div><div class="mrow">{rd("off", "md")}<span class="lt"><span class="lb">Xe hỏng</span></span></div></div>
<div class="msec">Toggle</div>
<div class="mlist"><div class="mrow">{tg("on", "md")}<span class="lt"><span class="lb">Nhận chuyến tự động</span></span></div>
 <div class="mrow">{tg("off", "md")}<span class="lt"><span class="lb">Chia sẻ vị trí</span><span class="hn">Rãnh tắt theo D1</span></span></div></div>
<div class="msec">Textarea</div><div style="padding:0 16px">{ta("", "", "Mô tả sự cố…", counter="0/300", label="Ghi chú")}
{ta("Lốp sau bên phải mòn, cần thay trước chuyến chiều.", "f", counter="52/300", label="Ghi chú")}</div>
</div>"""

# ---------- Màn demo web: Huỷ lệnh ----------
REASONS = ["Khách huỷ đơn", "Không có xe phù hợp", "Hàng chưa sẵn sàng", "Lý do khác"]


def reasons(state):
    out = ""
    for k, r in enumerate(REASONS):
        on = (state == "filled" and k == 0)
        hint = {0: "Khách báo trước 24 giờ.", 3: "Ghi rõ ở ô Lý do."}.get(k)
        out += lab(rd("on" if on else "off", st="d" if state == "ro" else ""), r, hint, cls="dis" if state == "ro" else "",
                   attrs='data-cmp data-js="pick"')
    return f'<div class="stack" role="radiogroup">{out}</div>'


def cancel_form(state):
    long = state == "long"
    v = {"filled": "Khách đổi lịch lấy hàng sang 30/10, giữ booking.",
         "long": "Khách hàng báo huỷ vì tàu đổi lịch cập cảng sang ngày 31/10; container đã được cấp lệnh giao hàng nhưng chưa đóng phí lưu bãi. Đề nghị giữ booking, hoàn phí nâng hạ đã thu và báo lại bộ phận chứng từ để huỷ tờ khai.",
         "ro": "Khách đổi lịch lấy hàng sang 30/10, giữ booking."}.get(state, "")
    st = {"error": "e", "ro": "ro"}.get(state, "f" if state == "filled" else "")
    err = "Chọn lý do và nhập mô tả (tối thiểu 10 ký tự)." if state == "error" else None
    lock = '<div class="lockbar">' + ic("lock", 14) + ' Lệnh đã huỷ ngày 27/10 — chỉ xem.</div>' if state == "ro" else ""
    dis = 'cls="dis"'
    return f"""<div data-show="state:{state}"><div class="card" style="max-width:960px;margin:0 24px">
<div class="box">{lock}<div class="two"><div><div class="sec-t">Lý do huỷ<span style="color:var(--color-status-danger-text)">*</span></div>
<div class="muted" style="font-size:13px;margin-bottom:12px">Bắt buộc chọn một.</div>{reasons(state)}</div>
<div class="stack">{ta(v, st, counter=f"{len(v)}/500", err=err, hint=None if err else "Khách hàng nhận được lý do này.", label="Mô tả", attrs='data-cmp').replace('class="taf"', 'class="taf w"')}
{lab(cb("off" if state in ("default", "error") else "on", st="d" if state == "ro" else ""), "Thông báo cho khách hàng", "Gửi email và SMS khi lệnh huỷ.", cls="dis" if state == "ro" else "", attrs="data-cmp")}
{lab(tg("on" if state in ("filled", "long", "ro") else "off", st="d" if state == "ro" else ""), "Giữ booking với hãng tàu", "Không trả lại chỗ cho hãng tàu.", cls="dis" if state == "ro" else "", attrs="data-cmp")}</div></div></div>
<div class="foot"><button class="bt">Đóng</button>{"" if state == "ro" else '<button class="bt dz" data-js="submit">Huỷ lệnh</button>'}</div></div></div>""".replace(dis, "")


CANCEL = "".join(cancel_form(s) for s in ("default", "filled", "error", "long", "ro"))

# ---------- Màn demo web: bảng chọn nhiều ----------
TROWS = [("LVT-2026-0412", "Cát Lái → ICD Sóng Thần", "Trần Văn Bình", True), ("LVT-2026-0413", "Hiệp Phước → VSIP 2", "Lê Minh Châu", True),
         ("LVT-2026-0414", "Cát Lái → Long Hậu", "Chưa điều", False), ("LVT-2026-0415", "Cái Mép → Tân Uyên", "Phạm Quốc Dũng", False)]
BULK = f"""<div style="padding:0 24px">
<div class="selbar">{cb("ind")}<b>2 lệnh đã chọn</b><span class="sp"></span><button class="bt">Gán lái xe</button><button class="bt">Xuất PDF</button></div>
<table class="tbl card" style="overflow:hidden"><tr><th>{cb("ind")}</th><th>Mã lệnh</th><th>Tuyến</th><th>Lái xe</th><th>Gửi SMS</th></tr>
{"".join(f'<tr style="{"background:var(--color-bg-hover)" if s else ""}"><td>{cb("on" if s else "off")}</td><td class="mono">{c}</td><td>{r}</td><td>{d}</td><td>{tg("on" if s else "off")}</td></tr>' for c, r, d, s in TROWS)}
</table></div>"""

# ---------- Màn demo app: checklist trước chuyến ----------
CHECK = [("Lốp và áp suất", "Kiểm 10 bánh", True), ("Đèn, còi, gạt mưa", None, True), ("Khoá container, chốt mooc", "Chụp ảnh 2 chốt", False),
         ("Giấy tờ xe", "Đăng kiểm, bảo hiểm, phù hiệu", False)]
APP = (f'<div class="msec">Trước chuyến LVT-2026-0412 · 2/4</div><div class="mlist">'
       + "".join(f'<label class="mrow" data-cmp>{cb("on" if on else "off", "md")}<span class="lt"><span class="lb">{t}</span>{f"<span class=hn>{h}</span>" if h else ""}</span></label>' for t, h, on in CHECK)
       + f'</div><div class="msec">Thiết lập</div><div class="mlist"><label class="mrow" data-cmp>{tg("on", "md")}<span class="lt"><span class="lb">Báo điều phối khi xong</span></span></label></div>'
       + f'<div style="padding:16px">{ta("", "", "Ghi chú tình trạng xe…", counter="0/300", label="Ghi chú", req=False, attrs="data-cmp")}</div>'
       + '<div style="padding:0 16px 16px"><button class="bt pri full">Xác nhận sẵn sàng</button></div>')


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

page = {
    "component": "Checkbox · Radio · Toggle · Textarea",
    "slug": "form-controls",
    "title": "Form controls Review",
    "subtitle": "Base component · Checkbox, Radio, Toggle (+ label, group item), Textarea · Checkbox/Radio/Toggle/Textarea nhóm A, Checkbox label nhóm B (DEC-280)",
    "round": "brainstorm",
    "brief": True,
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
        {"key": "error", "label": "Lỗi khi gửi"},
        {"key": "long", "label": "Chữ dài"},
        {"key": "ro", "label": "Chỉ xem"},
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
         "why": "Hover tô nền hay chỉ đậm viền; ô Chỉ xem (Read Only) có cần icon khoá để khỏi nhầm với Disabled (mục L14).",
         "source": "Trang Duyệt Base components › L14 · Figma 6658:187203",
         "options": [
             {"label": "Đậm viền; Chỉ xem không icon", "desc": "Giống Input; Chỉ xem phân biệt bằng nền muted + chữ đậm bình thường.", "rec": True,
              "preview": mini({"D4": "a"}, ta("", "h", counter="0/500", hint="Hover") + ta("Khách đổi lịch sang 30/10.", "ro", counter="25/500", hint="Chỉ xem"))},
             {"label": "Tô nền; Chỉ xem có khoá", "desc": "Hover nền bg/hover; icon khoá góc phải khi chỉ xem.",
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
         "note": "Toàn bộ biến thể đã chốt 26/10, đổi theo D1–D6 và Light/Dark.", "html": VAR_WEB},
        {"id": "var-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none", "note": "Cùng component trên app; D2 đổi vị trí ô chọn, D3 Pressed.", "html": VAR_APP},
        {"id": "cancel-web", "name": "Huỷ lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Huỷ lệnh LVT-2026-0412",
         "note": "Radio lý do + Textarea + Checkbox label + Toggle label. Bấm một lý do → Đã chọn; bấm Huỷ lệnh khi chưa chọn → Lỗi.", "html": CANCEL},
        {"id": "bulk-web", "name": "Chọn nhiều lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Lệnh vận tải",
         "note": "Checkbox Indeterminate ở đầu cột và thanh chọn; Toggle trong dòng.", "html": BULK},
        {"id": "check-app", "name": "Checklist trước chuyến", "device": "mobile", "nav": "Lệnh", "title": "Kiểm tra xe", "back": True,
         "note": "Ô chọn theo D2, Textarea ghi chú bản app.", "html": APP},
    ],
    "proto": [
        {"sel": "[data-js=pick]", "state": "filled"},
        {"sel": "[data-js=submit]", "state": "error"},
    ],
    "protoHint": "bấm một lý do, bấm Huỷ lệnh",
}

write(OUT, page)
