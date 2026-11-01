#!/usr/bin/env python3
"""Sinh page.json cho Buttons (Button · Close button · Utility button) — brainstorm gọn (28/10).
Chạy: python3 design-system/components/_work/buttons/build.py && python3 _scripts/ds-component-page.py buttons
Biến thể đã chốt: trang Chốt biến thể Base (artifact VQDsMrBW37W3QWVTPN79qC, db variants/button v11, 26/10).
Điểm cần quyết lấy từ trang Duyệt Base components (41DSsnEhvrQfZ1sggELNtq) còn chưa trả lời: C4, C5, C7, T1.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import ic, tok_css, BASE_CSS, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"

SPIN = '<span class="spn" aria-hidden="true"></span>'


def bt(label="Lưu", h="pri", size="md", st="", icon=None, lead=None, trail=None, dz=False, extra="", attrs=""):
    """h = pri | sec | ter | lkg ; st = h | p | f | d | ld ; icon='only' → nút chỉ icon."""
    cls = f"bt {h} {size} {st}" + (" dz" if dz else "") + (" io" if icon else "") + (f" {extra}" if extra else "")
    if icon:
        inner = (SPIN if st == "ld" else ic(icon, 20 if size == "lg" else 16))
        return f'<button class="{cls}" aria-label="{label}" {attrs}>{inner}</button>'
    inner = ""
    if st == "ld":
        inner += SPIN
    elif lead:
        inner += ic(lead, 16 if size != "lg" else 20)
    inner += f"<span class=tx>{label}</span>"
    if trail:
        inner += ic(trail, 16 if size != "lg" else 20)
    return f'<button class="{cls}" {attrs}>{inner}</button>'


def close(size="md", st=""):
    return f'<button class="cx {size} {st}" aria-label="Đóng">{ic("x", 20 if size == "lg" else 16)}</button>'


def util(icon, st="", label="", h="", size=""):
    """h = '' (bản A: có viền) | 'sec' | 'ter' (bản B theo Figma) ; size = '' | 'sm'."""
    return f'<button class="ut {h} {size} {st}" aria-label="{label}">{ic(icon, 16)}</button>'


H = [("pri", "Primary"), ("sec", "Secondary"), ("ter", "Tertiary"), ("lkg", "Link Gray")]
ST = [("", "Default"), ("h", "Hover"), ("p", "Pressed"), ("f", "Focus"), ("d", "Disabled"), ("ld", "Loading")]

# ---------- CSS ----------
CSS = tok_css() + BASE_CSS + """
.bt{display:inline-flex;align-items:center;justify-content:center;gap:var(--control-icon-gap);height:var(--control-height-md);
 padding:0 var(--control-padding-x-md);border-radius:var(--radius-control);border:1px solid transparent;position:relative;cursor:pointer;
 font:600 var(--type-label-size)/var(--type-label-line-height) var(--font-body);white-space:nowrap;max-width:240px;min-width:0;
 transition:background var(--duration-fast)}
.bt .tx{overflow:hidden;text-overflow:ellipsis;min-width:0}
.bt svg{flex:none}
.bt.sm{height:var(--control-height-sm);padding:0 var(--control-padding-x-sm)}
.bt.lg{height:var(--control-height-lg);padding:0 var(--control-padding-x-lg)}
.bt.io{width:var(--control-height-md);padding:0}.bt.io.sm{width:var(--control-height-sm)}.bt.io.lg{width:var(--control-height-lg)}
/* Primary */
.bt.pri{background:var(--color-action-primary);color:var(--color-text-inverse)}
.bt.pri.h{background:var(--color-action-primary-hover)}.bt.pri.p{background:var(--color-action-primary-pressed)}
/* Secondary — D1: a viền + nền trắng (Untitled) · b nền xám đậm · c nền xám nhạt phẳng (lượt 1 / Astryx) */
.bt.sec{background:var(--color-action-secondary);color:var(--color-text-primary)}
.bt.sec.h{background:var(--color-action-secondary-hover)}.bt.sec.p{background:var(--color-action-secondary-pressed)}
[data-D1=a] .bt.sec{background:var(--color-bg-primary);border-color:var(--color-border-primary);box-shadow:0 1px 2px var(--color-shadow-sm)}
[data-D1=a] .bt.sec.h{background:var(--color-bg-primary_hover)}[data-D1=a] .bt.sec.p{background:var(--color-bg-selected)}
[data-D1=b] .bt.sec{background:var(--color-action-secondary-hover)}
[data-D1=b] .bt.sec.h{background:var(--color-action-secondary-pressed)}[data-D1=b] .bt.sec.p{background:var(--color-action-secondary-pressed)}
/* Tertiary + Link Gray */
.bt.ter{background:transparent;color:var(--color-text-tertiary_strong)}
.bt.ter.h{background:var(--color-bg-selected);color:var(--color-text-primary)}.bt.ter.p{background:var(--color-action-secondary-hover);color:var(--color-text-primary)}
.bt.lkg{background:none;height:auto;padding:0;border-radius:var(--radius-sm);color:var(--color-text-tertiary_strong)}
.bt.lkg.h,.bt.lkg.p{color:var(--color-text-primary)}.bt.lkg.h .tx,.bt.lkg.p .tx{text-decoration:underline;text-underline-offset:4px}
/* Destructive — D2: a nền trắng viền đỏ nhạt, bấm red/50 · b nền đỏ nhạt (lượt 1), bấm red/200 */
.bt.dz.pri{background:var(--color-bg-error-solid);color:var(--color-text-inverse)}
.bt.dz.pri.h,.bt.dz.pri.p{background:var(--color-bg-error-solid_hover)}
.bt.dz.sec{color:var(--color-text-error-primary)}
[data-D2=a] .bt.dz.sec{background:var(--color-bg-primary);border-color:var(--color-border-error_subtle);box-shadow:none}
[data-D2=a] .bt.dz.sec.h{background:var(--color-bg-error-primary)}[data-D2=a] .bt.dz.sec.p{background:var(--color-bg-error-secondary)}
[data-D2=b] .bt.dz.sec{background:var(--color-bg-error-primary);border-color:transparent;box-shadow:none}
[data-D2=b] .bt.dz.sec.h{background:var(--color-bg-error-primary_hover)}[data-D2=b] .bt.dz.sec.p{background:var(--color-bg-error-primary_pressed)}
.bt.dz.ter{color:var(--color-text-error-primary)}.bt.dz.ter.h{background:var(--color-bg-error-primary);color:var(--color-text-error-primary)}
.bt.dz.ter.p{background:var(--color-bg-error-secondary);color:var(--color-text-error-primary)}
/* Disabled + Loading (DEC-277: tải trông như tắt + spinner) */
.bt.d,.bt.ld{background:var(--color-bg-disabled)!important;color:var(--color-text-disabled)!important;border-color:transparent!important;box-shadow:none!important;cursor:not-allowed}
.bt.ter.d,.bt.lkg.d,.bt.ter.ld,.bt.lkg.ld{background:transparent!important}
.spn{width:16px;height:16px;border-radius:50%;border:2px solid currentColor;border-right-color:transparent;animation:spn .8s linear infinite;flex:none}
@keyframes spn{to{transform:rotate(360deg)}}
/* Focus — D3: a vòng than chì 2px cách 2 (lượt 1) · b vòng xanh brand */
.bt.f,.cx.f,.ut.f{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.bt.dz.f{outline-color:var(--color-focus-ring_error)}
[data-D3=b] .bt.f:not(.dz),[data-D3=b] .cx.f,[data-D3=b] .ut.f{outline-color:var(--color-fg-info-primary)}
.pv[data-theme=dark] [data-D3=b] .bt.f:not(.dz),.pv[data-theme=dark][data-D3=b] .bt.f:not(.dz){outline-color:var(--color-fg-info-primary)}
/* Close button + Utility button */
.cx{display:inline-grid;place-items:center;width:var(--control-height-md);height:var(--control-height-md);border-radius:var(--radius-control);
 border:0;background:transparent;color:var(--color-fg-quaternary);cursor:pointer;position:relative}
.cx.sm{width:var(--control-height-sm);height:var(--control-height-sm)}.cx.lg{width:var(--control-height-lg);height:var(--control-height-lg)}
.cx.h{background:var(--color-bg-selected);color:var(--color-fg-secondary)}.cx.p{background:var(--color-action-secondary-hover)}
.cx.d,.ut.d{color:var(--color-text-disabled);cursor:not-allowed}
.ut{display:inline-grid;place-items:center;width:var(--control-height-md);height:var(--control-height-md);border-radius:var(--radius-control);
 border:1px solid var(--color-border-secondary);background:var(--color-bg-primary);color:var(--color-fg-quaternary);cursor:pointer;position:relative}
.ut.h{background:var(--color-bg-primary_hover);color:var(--color-fg-secondary)}.ut.p{background:var(--color-bg-selected)}
/* App: vùng chạm — D4: a thêm vùng chạm 44 vô hình cho nút < 44 · b không thêm, app chỉ dùng MD/LG */
[data-platform=mobile][data-D4=a] .bt.io::after,[data-platform=mobile][data-D4=a] .cx::after,[data-platform=mobile][data-D4=a] .ut::after,
[data-platform=mobile][data-D4=a] .bt.sm::after{content:"";position:absolute;left:50%;top:50%;min-width:44px;min-height:44px;width:100%;height:100%;transform:translate(-50%,-50%)}
[data-platform=mobile] .showhit .bt.io::after,[data-platform=mobile].showhit .bt.io::after,[data-platform=mobile] .showhit .cx::after,[data-platform=mobile].showhit .cx::after,[data-platform=mobile] .showhit .ut::after,[data-platform=mobile].showhit .ut::after,[data-platform=mobile] .showhit .bt.sm::after,[data-platform=mobile].showhit .bt.sm::after{outline:1px dashed var(--color-fg-info-primary);border-radius:4px}

[data-platform=mobile][data-D4=b] .no-sm{opacity:.35}
[data-platform=mobile][data-D4=b] .no-sm::before{content:"không dùng trên app";position:absolute;font:500 10px/12px var(--font-body);color:var(--color-text-error-primary);transform:translateY(-22px)}
.hitnote{font-size:12px;line-height:16px;color:var(--color-text-tertiary)}
[data-D4=a] .hitnote.b,[data-D4=b] .hitnote.a{display:none}
/* ===================== Bản B — theo Figma (Section Buttons 6657:163199, đo 29/10) ===================== */
/* đệm ngang web SM 6 · MD 8 · LG 12, khe icon 4 (Link Gray 6); app MD 12 · LG 20; chữ 500 */
[data-V=b] .bt{gap:var(--space-4);padding:0 var(--space-8);font-weight:500}
[data-V=b] .bt.sm{padding:0 var(--space-6)}[data-V=b] .bt.lg{padding:0 var(--space-12)}
[data-V=b] .bt.io{padding:0}
[data-V=b] .bt.lkg{gap:var(--space-6);padding:0}
[data-V=b][data-platform=mobile] .bt,[data-platform=mobile] [data-V=b] .bt{padding:0 var(--space-12)}
[data-V=b][data-platform=mobile] .bt.lg,[data-platform=mobile] [data-V=b] .bt.lg{padding:0 var(--space-20)}
[data-V=b][data-platform=mobile] .bt.io,[data-platform=mobile] [data-V=b] .bt.io,[data-V=b] .bt.lkg{padding:0}
/* Tertiary: chữ đậm như Secondary, Hover neutral/50, Pressed neutral/200 */
[data-V=b] .bt.ter{color:var(--color-text-primary)}
[data-V=b] .bt.ter.h{background:var(--color-bg-primary_hover)}[data-V=b] .bt.ter.p{background:var(--color-bg-pressed)}
[data-V=b] .bt.dz.ter{color:var(--color-text-error-primary)}
[data-V=b] .bt.dz.ter.h{background:var(--color-bg-error-primary)}[data-V=b] .bt.dz.ter.p{background:var(--color-bg-error-primary_hover)}
/* Link Gray: Hover/Pressed chỉ đậm chữ, không gạch chân */
[data-V=b] .bt.lkg.h .tx,[data-V=b] .bt.lkg.p .tx{text-decoration:none}
[data-V=b] .bt.lkg.ld{color:var(--color-text-tertiary_strong)!important}
/* Close button: nền trong, Hover neutral/50, Pressed neutral/200; icon neutral/500 → 700 */
[data-V=b] .cx{color:var(--color-fg-quaternary_hover)}
[data-V=b] .cx.h{background:var(--color-bg-primary_hover);color:var(--color-fg-secondary)}[data-V=b] .cx.p{background:var(--color-bg-pressed);color:var(--color-fg-secondary)}
/* Utility button: Hierarchy Secondary (nền xám phẳng) | Tertiary (nền trong), Size SM 28 | MD 32, không viền */
[data-V=b] .ut{border-color:transparent;background:transparent;color:var(--color-fg-quaternary_hover)}
[data-V=b] .ut.sm{width:var(--control-height-sm);height:var(--control-height-sm)}
[data-V=b] .ut.sec{background:var(--color-action-secondary)}[data-V=b] .ut.sec.h{background:var(--color-action-secondary-hover);color:var(--color-fg-secondary)}[data-V=b] .ut.sec.p{background:var(--color-action-secondary-pressed);color:var(--color-fg-secondary)}
[data-V=b] .ut.h{background:var(--color-bg-primary_hover);color:var(--color-fg-secondary)}[data-V=b] .ut.p{background:var(--color-bg-pressed);color:var(--color-fg-secondary)}
[data-V=b] .ut.d{color:var(--color-fg-disabled)}
/* Has Tooltip (mặc định bật): nút chỉ icon, Close, Utility hiện tooltip tên nút khi Hover / Focus */
[data-V=b] .bt.io.h::before,[data-V=b] .bt.io.f::before,[data-V=b] .cx.h::before,[data-V=b] .cx.f::before,[data-V=b] .ut.h::before,[data-V=b] .ut.f::before{
 content:attr(aria-label);position:absolute;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);white-space:nowrap;
 background:var(--color-bg-primary_solid);color:var(--color-text-inverse);font:500 12px/16px var(--font-body);padding:4px 8px;border-radius:var(--radius-md);pointer-events:none;z-index:3}
[data-platform=mobile] [data-V=b] .bt.io.f::before,[data-V=b][data-platform=mobile] .bt.io.f::before{display:none}
.vnote{font-size:12px;line-height:16px;color:var(--color-text-tertiary);margin:0 0 4px}
/* Màn demo */
.ph{display:flex;align-items:flex-start;gap:16px;padding:4px 24px 16px}
.ph .t{flex:1;min-width:0}.ph .code{font:600 22px/30px var(--font-body)}
.acts{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}
.kv{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:16px 24px}
.kv dt{font-size:12px;line-height:16px;color:var(--color-text-tertiary)}.kv dd{margin:2px 0 0;font-weight:500}
.foot{display:flex;gap:8px;padding:16px 24px;border-top:1px solid var(--color-border-secondary)}
.form{display:grid;grid-template-columns:1fr 1fr;gap:16px;max-width:720px}
.fld label{display:block;font:500 13px/18px var(--font-body);color:var(--color-text-tertiary_strong);margin-bottom:6px}
.fld .in{height:var(--control-height-md);border:1px solid var(--color-border-input);border-radius:var(--radius-field);padding:0 10px;display:flex;align-items:center;background:var(--color-bg-primary)}
.scrim{position:absolute;inset:0;background:var(--color-bg-overlay);display:grid;place-items:center;z-index:5}
.dlg{width:440px;background:var(--color-bg-primary);border-radius:var(--radius-overlay);box-shadow:0 12px 32px var(--color-shadow-lg);overflow:hidden}
.dlg .hd{display:flex;gap:12px;align-items:flex-start;padding:20px 20px 0}.dlg .hd b{font:600 16px/24px var(--font-body);display:block}
.dlg .bd{padding:8px 20px 20px 20px;color:var(--color-text-tertiary)}
.dlg .ft{display:flex;gap:8px;justify-content:flex-end;padding:16px 20px;border-top:1px solid var(--color-border-secondary)}
.fi{width:40px;height:40px;border-radius:999px;background:var(--color-bg-error-primary);color:var(--color-fg-error-primary);display:grid;place-items:center;flex:none}
.mcard{margin:12px 16px;padding:16px}
.mcard .r{display:flex;justify-content:space-between;padding:6px 0;font-size:14px}
.mbar{position:absolute;left:0;right:0;bottom:64px;padding:12px 16px;background:var(--color-bg-primary);border-top:1px solid var(--color-border-secondary);display:flex;gap:8px}
.mbar .bt{flex:1;max-width:none}
.wrap-rel{position:relative;min-height:100%}
"""

# ---------- Bảng biến thể Web ----------
def matrix(dz=False, sizes=("md",)):
    hs = H if not dz else [("pri", "Primary"), ("sec", "Secondary"), ("ter", "Tertiary")]
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{n}</div>' for _, n in ST)
    rows = ""
    for h, n in hs:
        rows += f'<div class="vl">{n}</div>' + "".join(
            f'<div>{bt("Huỷ lệnh" if dz else "Điều xe", h, "md", s, dz=dz)}</div>' for s, _ in ST)
    return f'<div class="vgrid" style="grid-template-columns:96px repeat(6,max-content)">{head}{rows}</div>'


def sizes_row():
    out = ""
    for s, lab in (("sm", "SM"), ("md", "MD"), ("lg", "LG")):
        out += (f'<div class="vl">{lab}</div><div>{bt("Điều xe", "pri", s)}</div><div>{bt("Xuất PDF", "sec", s, lead="dl")}</div>'
                f'<div>{bt("Thêm điểm", "ter", s, lead="plus")}</div><div>{bt("Tiếp tục", "pri", s, trail="arrow-r")}</div>'
                f'<div>{bt("Thêm", "sec", s, icon="plus")}</div><div>{bt("Khác", "ter", s, icon="more")}</div>')
    head = '<div class="vl"></div>' + "".join(f'<div class="vl">{x}</div>' for x in
                                              ("Icon=Default", "Leading", "Leading", "Trailing", "Only · Secondary", "Only · Tertiary"))
    return f'<div class="vgrid" style="grid-template-columns:40px repeat(6,max-content)">{head}{out}</div>'


VAR_WEB = f"""<div class="vt">
<p class="vnote" data-show="V:b">Bản B theo Figma: số đo, chữ 500, Tertiary, Link Gray, Close, Utility và tooltip khi Hover lấy đúng như Figma. Màu Secondary (D1), Destructive Secondary (D2), vòng focus (D3), vùng chạm app (D4) vẫn đổi theo D1–D4 — Figma hiện đang là D1 = C, D2 = B, D3 = A.</p>
<div><div class="vh">Hierarchy × State <small>Size=MD · Icon=Default · Destructive=False</small></div>{matrix()}</div>
<div><div class="vh">Destructive × State <small>Huỷ, xoá, từ chối — chỉ dùng cho hành động phá huỷ</small></div>{matrix(dz=True)}</div>
<div><div class="vh">Size × Icon <small>web 28 · 32 · 40</small></div>{sizes_row()}</div>
<div class="row" style="align-items:flex-start;gap:48px">
 <div><div class="vh">Close button <small>Size × State</small></div>
  <div class="vgrid" style="grid-template-columns:40px repeat(5,max-content)"><div class="vl"></div>{"".join(f'<div class="vl">{n}</div>' for _, n in ST[:5])}
  {"".join(f'<div class="vl">{z.upper()}</div>' + "".join(f"<div>{close(z, s)}</div>" for s, _ in ST[:5]) for z in ("sm", "md", "lg"))}</div></div>
 <div><div class="vh">Utility button <small data-show="V:a">nút icon có viền trong thanh công cụ</small><small data-show="V:b">Hierarchy Secondary | Tertiary × Size SM | MD (Figma)</small></div>
  <div data-show="V:a"><div class="vg">{util("filter", "", "Lọc")}{util("filter", "h", "Lọc")}{util("filter", "p", "Lọc")}{util("filter", "f", "Lọc")}{util("filter", "d", "Lọc")}</div>
  <div class="vg" style="margin-top:10px">{util("dl", "", "Tải")}{util("edit", "", "Sửa")}{util("trash", "", "Xoá")}{util("settings", "", "Cài đặt")}</div></div>
  <div data-show="V:b"><div class="vgrid" style="grid-template-columns:104px repeat(5,max-content);row-gap:28px"><div class="vl"></div>{"".join(f'<div class="vl">{n}</div>' for _, n in ST[:5])}
  {"".join(f'<div class="vl">{hn} · {z.upper() or "MD"}</div>' + "".join(f'<div>{util("filter", s, "Lọc", h, z)}</div>' for s, _ in ST[:5]) for h, hn in (("sec", "Secondary"), ("ter", "Tertiary")) for z in ("sm", ""))}</div></div></div>
</div>
<div><div class="vh">Chữ dài <small>1 dòng, cắt "…", rộng tối đa 240</small></div>
 <div class="vg">{bt("Xác nhận hoàn tất giao container cho khách hàng Cát Lái", "pri")}{bt("Xuất bảng kê chi phí chuyến theo tháng", "sec", lead="dl")}</div></div>
</div>"""

# ---------- Bảng biến thể App ----------
VAR_APP = f"""<div class="vt showhit">
<div><div class="vh">Size <small>app 36 · 42 · 52, bo tròn hẳn</small></div>
 <div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start">
 <span class="no-sm" style="position:relative">{bt("Gọi điều phối", "sec", "sm", lead="send")}</span>{bt("Gọi điều phối", "sec", "md", lead="send")}{bt("Nhận chuyến", "pri", "lg")}</div></div>
<div><div class="vh">Hierarchy <small>Size=LG</small></div>
 <div style="display:flex;flex-direction:column;gap:10px">{bt("Nhận chuyến", "pri", "lg", extra="full")}{bt("Xem lộ trình", "sec", "lg", extra="full")}{bt("Báo sự cố", "ter", "lg")}{bt("Từ chối chuyến", "sec", "lg", dz=True)}</div></div>
<div><div class="vh">State <small data-show="V:a">Pressed thay Hover trên app</small><small data-show="V:b">Figma Platform = Mobile: Default · Pressed · Disabled · Loading</small></div>
 <div class="vg">{bt("Lưu", "pri", "md")}{bt("Lưu", "pri", "md", "p")}<span data-show="V:a">{bt("Lưu", "pri", "md", "f")}</span>{bt("Lưu", "pri", "md", "d")}{bt("Đang lưu", "pri", "md", "ld")}</div></div>
<div><div class="vh">Nút chỉ icon + vùng chạm</div>
 <div class="vg"><span class="no-sm" style="position:relative">{bt("Thêm", "sec", "sm", icon="plus")}</span>{bt("Thêm", "sec", "md", icon="plus")}{bt("Thêm", "sec", "lg", icon="plus")}{close("md")}<span data-show="V:a">{util("filter", "", "Lọc")}</span><span data-show="V:b">{util("filter", "", "Lọc", "sec")}</span></div>
 <p class="hitnote a">Khung nét đứt = vùng chạm 44 × 44 vô hình. Hình nút giữ nguyên.</p>
 <p class="hitnote b">Không thêm vùng chạm: nút SM (36) không được dùng trên app; MD 42 vẫn dưới 44.</p></div>
</div>"""
VAR_APP = VAR_APP.replace('extra="full"', "")

# ---------- Màn demo ----------
def detail_actions():
    return (f'<div class="acts">'
            f'<span>{bt("Huỷ lệnh", "ter", dz=True, attrs="data-cmp class-js")}</span>'
            f'{bt("Xuất PDF", "sec", lead="dl", attrs="data-cmp")}'
            f'<span data-hide="disabled long">{bt("Điều xe", "pri", attrs="data-cmp")}</span>'
            f'<span data-show="state:disabled">{bt("Điều xe", "pri", st="d", attrs="data-cmp")}</span>'
            f'<span data-show="state:long">{bt("Xác nhận hoàn tất giao container cho khách hàng Cát Lái", "pri", attrs="data-cmp")}</span>'
            f'{bt("Khác", "sec", icon="more", attrs="data-cmp")}</div>')


DETAIL = f"""<div class="wrap-rel">
<div class="ph"><div class="t"><div class="muted" style="font-size:12px">Lệnh vận tải</div><div class="code">LVT-2026-0412</div>
<div class="muted">Cát Lái → ICD Sóng Thần · 2 × 40' HC</div></div>{detail_actions()}</div>
<div data-show="state:disabled" style="margin:0 24px 8px;padding:10px 12px;border-radius:var(--radius-md);background:var(--color-bg-warning-primary);color:var(--color-text-warning-primary);font-size:13px">Chưa có xe sẵn sàng ở bãi Cát Lái — chưa điều xe được.</div>
<dl class="kv card" style="margin:0 24px"><div><dt>Khách hàng</dt><dd>Công ty TNHH Delta Logistics</dd></div><div><dt>Ngày lấy hàng</dt><dd>28/10/2026 · 08:00</dd></div>
<div><dt>Xe</dt><dd>Chưa điều</dd></div><div><dt>Lái xe</dt><dd>Chưa điều</dd></div></dl>
<div class="pg"><div class="row" style="margin-bottom:8px"><div class="sec-t">Điểm dừng</div><span class="sp"></span>{bt("Thêm điểm", "ter", "sm", lead="plus", attrs="data-cmp")}</div>
<table class="tbl card" style="overflow:hidden"><tr><th>#</th><th>Địa điểm</th><th>Việc</th><th>Giờ hẹn</th><th></th></tr>
<tr><td>1</td><td>Cảng Cát Lái</td><td>Lấy container</td><td>08:00</td><td style="text-align:right">{bt("Sửa", "ter", "sm", icon="edit", attrs="data-cmp")}{bt("Xoá", "ter", "sm", icon="trash", attrs="data-cmp")}</td></tr>
<tr><td>2</td><td>ICD Sóng Thần</td><td>Hạ container</td><td>11:30</td><td style="text-align:right">{bt("Sửa", "ter", "sm", icon="edit", attrs="data-cmp")}{bt("Xoá", "ter", "sm", icon="trash", attrs="data-cmp")}</td></tr></table>
<div class="row" style="margin-top:12px">{bt("Xem lịch sử thay đổi", "lkg", attrs="data-cmp")}</div></div>
<div class="scrim" data-show="state:confirm"><div class="dlg" role="dialog" aria-label="Huỷ lệnh">
 <div class="hd"><span class="fi">{ic("trash", 20)}</span><div><b>Huỷ lệnh LVT-2026-0412?</b></div><span class="sp"></span>{close("sm")}</div>
 <div class="bd" style="padding-left:72px">Lệnh chưa điều xe. Huỷ xong không khôi phục được; khách hàng nhận thông báo huỷ.</div>
 <div class="ft">{bt("Giữ lệnh", "sec", attrs="data-cmp")}{bt("Huỷ lệnh", "pri", dz=True, attrs="data-cmp")}</div></div></div>
</div>""".replace("class-js", 'data-js="cancel"')

FORM = f"""<div class="pg" style="max-width:820px">
<div class="sec-t" style="margin-bottom:12px">Thông tin lệnh</div>
<div class="form"><div class="fld"><label>Khách hàng</label><div class="in">Công ty TNHH Delta Logistics</div></div>
<div class="fld"><label>Ngày lấy hàng</label><div class="in">28/10/2026</div></div>
<div class="fld"><label>Điểm lấy</label><div class="in">Cảng Cát Lái</div></div><div class="fld"><label>Điểm trả</label><div class="in">ICD Sóng Thần</div></div></div>
</div>
<div class="foot" style="max-width:820px">
<span data-hide="saving">{bt("Lưu lệnh", "pri", attrs='data-cmp data-js="save"')}</span>
<span data-show="state:saving">{bt("Đang lưu", "pri", st="ld", attrs="data-cmp")}</span>
{bt("Lưu nháp", "sec", attrs="data-cmp")}<span class="sp"></span>{bt("Bỏ thay đổi", "ter", attrs="data-cmp")}</div>"""

APP = f"""<div class="wrap-rel" style="padding-bottom:140px">
<div class="card mcard"><div class="row"><b style="font-size:16px">LVT-2026-0412</b><span class="sp"></span>{bt("Gọi điều phối", "sec", "md", icon="send", attrs="data-cmp")}</div>
<div class="muted" style="margin:4px 0 10px">Cát Lái → ICD Sóng Thần</div>
<div class="r"><span class="muted">Lấy hàng</span><b>08:00 · 28/10</b></div><div class="r"><span class="muted">Container</span><b>2 × 40' HC</b></div>
<div class="r"><span class="muted">Xe</span><b>51C-123.45</b></div></div>
<div style="padding:0 16px">{bt("Xem lộ trình", "lkg", trail="chev", attrs="data-cmp")}</div>
<div class="mbar">
<span data-hide="saving" style="display:contents">{bt("Từ chối", "sec", "lg", dz=True, attrs="data-cmp")}{bt("Nhận chuyến", "pri", "lg", attrs='data-cmp data-js="save"')}</span>
<span data-show="state:saving" style="display:contents">{bt("Từ chối", "sec", "lg", "d", dz=True)}{bt("Đang nhận", "pri", "lg", "ld", attrs="data-cmp")}</span>
</div></div>"""

page = {
    "component": "Buttons",
    "slug": "buttons",
    "title": "Buttons Review",
    "subtitle": "Base component · Button, Close button, Utility button · nhóm A (dùng chung web và app, số đo theo mode Platform)",
    "round": "brainstorm",
    "brief": True,
    "refs": {
        "untitled": {
            "summary": "Hierarchy <mark>primary · secondary · tertiary · link</mark> + biến thể destructive; 5 cỡ xs–xl, bo <mark>rounded-lg</mark>; Secondary = <mark>nền trắng + viền</mark> (ring-1) có bóng xs; Loading giữ màu nút + spinner.",
            "source": "design/_ref/untitled-ui/react/components/base/buttons/button.tsx · close-button.tsx · button-utility.tsx",
        },
        "astryx": {
            "summary": "Secondary là <mark>đen 6% trong suốt</mark> (pill xám nhạt, không viền); focus viền accent 2px cách 3; app nút tròn hẳn cao 52 / 42 (DEC-097).",
            "source": "design/design.md dòng 313–318, 364 · DEC-097",
        },
        "usage": [
            "Mọi màn: hàng hành động đầu trang, chân form, hộp xác nhận",
            "cross-process-flow · view-process (web) · nút hành động bước",
            "App lái xe · nhận chuyến / từ chối / báo sự cố",
        ],
        "platform": "Nhóm A — một bộ, cao 28·32·40 web / 36·42·52 app theo mode Platform (DEC-279). Đã chốt biến thể 26/10 (Hierarchy 4 × Destructive × Icon 4 × Size 3 × State 6) và Loading trông như Disabled (DEC-277). Đây là trang brainstorm gọn: chỉ 4 điểm còn mở từ lượt duyệt Figma 1.",
    },
    "css": CSS,
    "states": [
        {"key": "default", "label": "Mặc định"},
        {"key": "saving", "label": "Đang lưu"},
        {"key": "confirm", "label": "Hộp xác nhận huỷ"},
        {"key": "disabled", "label": "Chưa đủ điều kiện"},
        {"key": "long", "label": "Chữ dài"},
    ],
    "ideas": [],
    "decisions": [
        {"id": "V", "title": "Phiên bản để duyệt",
         "why": "<mark>Bản A</mark> = bản đang đăng trên trang (số đo theo token control/*: đệm 8·12·16, chữ 600, Tertiary chữ xám, Link Gray gạch chân khi Hover, Utility có viền). "
                "<mark>Bản B</mark> = dựng lại theo <b>component Button đang có trên Figma</b> (252 biến thể): đệm ngang <b>6·8·12</b> web, <b>12·20</b> app, khe icon 4, chữ <b>Medium 500</b>; "
                "Tertiary chữ đen, Hover neutral/50; Link Gray không gạch chân; Close và Utility nền trong, icon neutral/500; Utility có Hierarchy Secondary | Tertiary × Size SM | MD; "
                "nút chỉ icon, Close, Utility <b>hiện tooltip</b> khi Hover/Focus (Has Tooltip bật sẵn); app chỉ Default · Pressed · Disabled · Loading. "
                "Màu Secondary, Destructive Secondary, focus vẫn chọn ở D1–D3.",
         "source": "Figma Section Buttons 6657:163199 · set Button 6657:163467 · Close button 6657:164851 · Utility button 6657:164908 (đo 29/10)",
         "options": [
             {"label": "Bản A · hiện tại", "desc": "Giữ số đo theo token control/* đang có; đổi Figma theo trang này.",
              "preview": f'<div class="op" data-V="a" data-D1="c" style="padding:28px 16px 16px;display:flex;gap:8px;align-items:center">{bt("Xuất PDF", "sec", lead="dl")}{bt("Bỏ thay đổi", "ter")}{bt("Khác", "sec", st="h", icon="more")}{util("filter", "", "Lọc")}{bt("Điều xe", "pri")}</div>'},
             {"label": "Bản B · theo Figma", "desc": "Theo đúng component đang vẽ trên Figma; không phải sửa Figma phần số đo.",
              "preview": f'<div class="op" data-V="b" data-D1="c" style="padding:28px 16px 16px;display:flex;gap:8px;align-items:center">{bt("Xuất PDF", "sec", lead="dl")}{bt("Bỏ thay đổi", "ter")}{bt("Khác", "sec", st="h", icon="more")}{util("filter", "", "Lọc", "sec")}{bt("Điều xe", "pri")}</div>'},
         ]},
        {"id": "D1", "title": "Nút Secondary trên nền trắng",
         "why": "Lượt 1 trên Figma vẽ Secondary <mark>nền xám phẳng neutral/100</mark>: trên nền trắng chỉ <b>1,1:1</b>, nút gần như lẫn vào nền, đặc biệt trong bảng và chân form (mục C4 trang Duyệt Base).",
         "source": "Trang Duyệt Base components › C4 · Figma Button 6657:163467 · button.tsx secondary",
         "options": [
             {"label": "Nền trắng + viền", "desc": "Như Untitled: viền `border/primary`, bóng rất nhẹ. Rõ trên nền trắng lẫn nền xám.", "rec": True,
              "preview": f'<div class="op" data-D1="a" style="padding:16px;display:flex;gap:8px">{bt("Xuất PDF", "sec", lead="dl")}{bt("Điều xe", "pri")}</div>'},
             {"label": "Nền xám đậm hơn", "desc": "Giữ kiểu nền đặc, đổi sang neutral/200. Vẫn chỉ ~1,25:1 với nền.",
              "preview": f'<div class="op" data-D1="b" style="padding:16px;display:flex;gap:8px">{bt("Xuất PDF", "sec", lead="dl")}{bt("Điều xe", "pri")}</div>'},
             {"label": "Giữ nền xám nhạt", "desc": "Như lượt 1 và Astryx. Chấp nhận nút phụ chìm.",
              "preview": f'<div class="op" data-D1="c" style="padding:16px;display:flex;gap:8px">{bt("Xuất PDF", "sec", lead="dl")}{bt("Điều xe", "pri")}</div>'},
         ],
         "untitled": f'<div class="op" data-D1="a" style="padding:16px">{bt("Secondary", "sec")}</div>', "untitledNote": "bg-primary + ring-1 ring-primary + shadow-xs",
         "astryx": f'<div class="op" data-D1="c" style="padding:16px">{bt("Phụ", "sec")}</div>', "astryxNote": "đen 6%, không viền"},
        {"id": "D2", "title": "Nút phá huỷ phụ (Destructive Secondary)",
         "why": "Lượt 1: nền đỏ nhạt, khi bấm nền đỏ đậm lên → <mark>chữ đỏ trên nền đỏ</mark> dưới 4,5:1 (mục C5). Nút này nằm ở hộp xác nhận huỷ / từ chối hoá đơn.",
         "source": "Trang Duyệt Base components › C5 · button.tsx secondary-destructive",
         "options": [
             {"label": "Nền trắng, viền đỏ nhạt", "desc": "Như Untitled; Hover red/50, Pressed red/100 — chữ đỏ luôn đạt.", "rec": True,
              "preview": f'<div class="op" data-D2="a" style="padding:16px;display:flex;gap:8px">{bt("Từ chối", "sec", dz=True)}{bt("Từ chối", "sec", st="h", dz=True)}{bt("Từ chối", "sec", st="p", dz=True)}</div>'},
             {"label": "Giữ nền đỏ nhạt", "desc": "Như lượt 1: Default red/50 · Hover red/100 · Pressed red/200.",
              "preview": f'<div class="op" data-D2="b" style="padding:16px;display:flex;gap:8px">{bt("Từ chối", "sec", dz=True)}{bt("Từ chối", "sec", st="h", dz=True)}{bt("Từ chối", "sec", st="p", dz=True)}</div>'},
         ],
         "untitled": f'<div class="op" data-D2="a" style="padding:16px">{bt("Delete", "sec", dz=True)}</div>', "untitledNote": "bg-primary + ring-error_subtle",
         "astryx": f'<div class="op" data-D2="b" style="padding:16px">{bt("Xoá", "sec", dz=True)}</div>', "astryxNote": "nền đỏ nhạt"},
        {"id": "D3", "title": "Màu vòng focus (bàn phím)",
         "why": "Vòng focus than chì đặt quanh nút Primary cũng than chì: visual-reviewer thấy khó nhận; đo lại thì khe trắng 2px tách được (mục C7).",
         "source": "Trang Duyệt Base components › C7 · foundations focus/width, focus/offset",
         "options": [
             {"label": "Giữ than chì", "desc": "Cùng màu hành động chính; khe 2px tách vòng khỏi nút.", "rec": True,
              "preview": f'<div class="op" data-D3="a" style="padding:16px;display:flex;gap:12px">{bt("Điều xe", "pri", st="f")}{bt("Xuất PDF", "sec", st="f")}</div>'},
             {"label": "Vòng xanh brand", "desc": "blue/600 — nổi hơn trên nút tối; thêm một màu chỉ cho focus.",
              "preview": f'<div class="op" data-D3="b" style="padding:16px;display:flex;gap:12px">{bt("Điều xe", "pri", st="f")}{bt("Xuất PDF", "sec", st="f")}</div>'},
         ],
         "untitled": f'<div class="op" data-D3="b" style="padding:16px">{bt("Button", "pri", st="f")}</div>', "untitledNote": "outline-focus-ring = brand",
         "astryx": f'<div class="op" data-D3="a" style="padding:16px">{bt("Lưu", "pri", st="f")}</div>', "astryxNote": "accent #262626, cách 3"},
        {"id": "D4", "title": "Vùng chạm của nút nhỏ trên app",
         "why": "App: SM cao 36, MD 42 — đều dưới 44 (WCAG 2.5.8 / HIG). Lượt 1 đề xuất \"app chỉ dùng MD/LG\" (mục T1), nhưng MD 42 vẫn thiếu, và nút −/+ của ô số, nút X, nút icon trên thẻ vẫn nhỏ.",
         "source": "Trang Duyệt Base components › T1 · design.md Accessibility (44)",
         "options": [
             {"label": "Thêm vùng chạm 44 vô hình", "desc": "Mọi nút dưới 44 trên app có vùng bấm 44×44 bao ngoài; hình nút không đổi.", "rec": True, "platform": "mobile",
              "preview": f'<div class="op showhit" data-D4="a" data-platform="mobile" style="padding:20px;display:flex;gap:16px">{bt("Thêm", "sec", "sm", icon="plus")}{bt("Thêm", "sec", "md", icon="plus")}{close("md")}</div>'},
             {"label": "Quy định: app chỉ MD/LG", "desc": "Không thêm vùng chạm; cấm SM trên app. MD 42 vẫn dưới 44.", "platform": "mobile",
              "preview": f'<div class="op showhit" data-D4="b" data-platform="mobile" style="padding:28px 20px 20px;display:flex;gap:16px"><span class="no-sm" style="position:relative">{bt("Thêm", "sec", "sm", icon="plus")}</span>{bt("Thêm", "sec", "md", icon="plus")}{close("md")}</div>'},
         ]},
    ],
    "presets": [
        {"id": "rec", "label": "Đề xuất", "pick": {"V": "a", "D1": "a", "D2": "a", "D3": "a", "D4": "a"}},
        {"id": "untitled", "label": "Theo Untitled", "pick": {"V": "a", "D1": "a", "D2": "a", "D3": "b", "D4": "a"}},
        {"id": "figma", "label": "Bản B · Figma", "pick": {"V": "b", "D1": "c", "D2": "b", "D3": "a", "D4": "b"}},
        {"id": "astryx", "label": "Astryx hiện tại", "pick": {"V": "a", "D1": "c", "D2": "b", "D3": "a", "D4": "b"}},
    ],
    "screens": [
        {"id": "var-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none",
         "note": "Toàn bộ biến thể đã chốt 26/10, đổi theo phiên bản (V), phương án D1–D4 và Light/Dark.", "html": VAR_WEB},
        {"id": "var-app", "name": "Bảng biến thể", "device": "mobile", "shell": "none",
         "note": "Cùng component, số đo theo mode Platform = Mobile. Nét đứt = vùng chạm.", "html": VAR_APP},
        {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "LVT-2026-0412", "heading": False,
         "note": "Hàng hành động đầu trang: Tertiary đỏ (Huỷ) · Secondary · Primary · icon. Bấm Huỷ lệnh mở hộp xác nhận.", "html": DETAIL},
        {"id": "form-web", "name": "Sửa lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Sửa lệnh LVT-2026-0412",
         "note": "Chân form [Chính][Phụ] canh trái (DEC-088). Bấm Lưu lệnh để thấy Loading.", "html": FORM},
        {"id": "trip-app", "name": "Chuyến được giao", "device": "mobile", "nav": "Lệnh", "title": "Chuyến mới", "back": True,
         "note": "Chân màn 2 nút LG; bấm Nhận chuyến để thấy Loading.", "html": APP},
    ],
    "proto": [
        {"sel": "[data-js=cancel]", "state": "confirm"},
        {"sel": "[data-js=save]", "state": "saving", "toggle": True, "back": "default"},
        {"sel": ".dlg .bt, .dlg .cx", "close": True},
    ],
    "protoLayers": [".dlg"],
    "protoHint": "bấm Huỷ lệnh, Lưu lệnh, Nhận chuyến",
}

write(OUT, page)
