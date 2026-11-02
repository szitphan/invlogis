#!/usr/bin/env python3
"""Sinh page.json cho Tooltip (+ Help icon; app dùng Help sheet, DEC-280) — brainstorm gọn (28/10).
Chạy: python3 design-system/components/_work/tooltip/build.py && python3 _scripts/ds-component-page.py tooltip
Biến thể đã chốt: trang Chốt biến thể Base (VQDsMrBW37W3QWVTPN79qC, db variants/tooltip v1, 26/10): Arrow 6 × Type 2 + Help icon, chỉ web.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import ic, tok_css, BASE_CSS, write, P  # noqa: E402

P.setdefault("copy", '<rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>')
P.setdefault("print", '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>')

OUT = Path(__file__).parent / "page.json"


def tip(text, arrow="top", title=None, cls="", attrs=""):
    """arrow = top | bottom | left | right | bl | br | none — phía có mũi tên (tooltip nằm ngược phía)."""
    body = f"<b>{title}</b><span>{text}</span>" if title else f"<span>{text}</span>"
    return f'<span class="tt a-{arrow}{" sup" if title else ""} {cls}" role="tooltip" {attrs}>{body}</span>'


def help_icon(label="Giải thích", attrs=""):
    return (f'<button class="hi" aria-label="{label}" {attrs}><span class="q">{ic("help", 16)}</span>'
            f'<span class="i2">{ic("info", 16)}</span></button>')


CSS = tok_css() + """
.tt{position:relative;display:inline-flex;flex-direction:column;gap:2px;max-width:var(--tooltip-max-width);padding:var(--space-xs) var(--space-md);
 border-radius:var(--radius-md);background:var(--color-bg-primary_solid);color:var(--color-text-inverse);font:600 12px/16px var(--font-body);text-align:left;
 box-shadow:var(--shadow-xs)}
.tt.sup{padding:8px 12px;max-width:280px}.tt.sup b{font:600 12px/16px var(--font-body)}.tt.sup span{font-weight:400;opacity:.86}
.tt::after{content:"";position:absolute;width:0;height:0;border:var(--size-xs) solid transparent}
/* mũi tên — tên theo phía của mũi tên trên tooltip */
.tt.a-bottom::after{top:100%;left:50%;margin-left:calc(var(--size-xs) * -1);border-top-color:var(--tt-arrow,var(--color-bg-primary_solid))}
.tt.a-top::after{bottom:100%;left:50%;margin-left:calc(var(--size-xs) * -1);border-bottom-color:var(--tt-arrow,var(--color-bg-primary_solid))}
.tt.a-left::after{right:100%;top:50%;margin-top:calc(var(--size-xs) * -1);border-right-color:var(--tt-arrow,var(--color-bg-primary_solid))}
.tt.a-right::after{left:100%;top:50%;margin-top:calc(var(--size-xs) * -1);border-left-color:var(--tt-arrow,var(--color-bg-primary_solid))}
.tt.a-bl::after{top:100%;left:12px;border-top-color:var(--tt-arrow,var(--color-bg-primary_solid))}
.tt.a-br::after{top:100%;right:12px;border-top-color:var(--tt-arrow,var(--color-bg-primary_solid))}
.tt.a-none::after{display:none}
/* D1 nền: a tối (bg/primary_solid) · b trắng + viền + bóng */
[data-D1=b] .tt{background:var(--color-bg-primary);color:var(--color-text-primary);box-shadow:0 0 0 1px var(--color-border-secondary),var(--shadow-xs);--tt-arrow:var(--color-bg-primary)}
[data-D1=b] .tt.sup span{color:var(--color-text-tertiary);opacity:1}
/* D2 mũi tên: a có · b không */
[data-D2=b] .tt::after{display:none}
/* D3 icon trợ giúp: a "?" · b "i" */
.hi{display:inline-grid;place-items:center;width:16px;height:16px;padding:0;border:0;background:none;color:var(--color-fg-tertiary);cursor:help;position:relative;vertical-align:-3px}
.hi::after{content:"";position:absolute;inset:-4px}
.hi:hover,.hi.on{color:var(--color-fg-secondary)}
.hi .q{display:grid}.hi .i2{display:none}
[data-D3=b] .hi .i2{display:grid}[data-D3=b] .hi .q{display:none}
/* D4 tooltip có tiêu đề: a tiêu đề + mô tả · b chỉ một đoạn */
[data-D4=b] .tt.sup b{display:none}[data-D4=b] .tt.sup span{font-weight:600;opacity:1}
[data-D4=b][data-D1=b] .tt.sup span,[data-D4=b] [data-D1=b] .tt.sup span{color:var(--color-text-primary)}
/* đặt tooltip quanh điểm neo */
.anc{position:relative;display:inline-flex;align-items:center}
.anc>.tt{position:absolute;z-index:4;white-space:normal;width:max-content}
.anc>.tt.p-top{bottom:calc(100% + var(--space-xs) + var(--size-xs));left:50%;transform:translateX(-50%)}
.anc>.tt.p-bottom{top:calc(100% + var(--space-xs) + var(--size-xs));left:50%;transform:translateX(-50%)}
.anc>.tt.p-right{left:calc(100% + var(--space-xs) + var(--size-xs));top:50%;transform:translateY(-50%)}
.anc>.tt.p-left{right:calc(100% + var(--space-xs) + var(--size-xs));top:50%;transform:translateY(-50%)}
.anc>.tt.p-tl{bottom:calc(100% + var(--space-xs) + var(--size-xs));left:-6px}
.anc>.tt.p-tr{bottom:calc(100% + var(--space-xs) + var(--size-xs));right:-6px}
/* Help sheet (app) */
.scrim{position:absolute;inset:0;background:var(--color-bg-overlay);z-index:5}
.sheet{position:absolute;left:0;right:0;bottom:0;z-index:6;background:var(--color-bg-primary);border-radius:var(--radius-overlay) var(--radius-overlay) 0 0;padding:8px 20px 28px}
.sheet .grab{width:36px;height:4px;border-radius:2px;background:var(--color-border-primary);margin:4px auto 16px}
.sheet b{display:block;font:600 17px/24px var(--font-body);margin-bottom:8px}
.sheet p{margin:0 0 20px;color:var(--color-text-tertiary_strong);font-size:15px;line-height:22px}
.sheet .ok{width:100%;height:var(--control-height-md);border:0;border-radius:var(--radius-control);background:var(--color-action-secondary);color:var(--color-text-primary);font:600 15px/20px var(--font-body)}
.mf .hi{width:24px;height:24px}.mf .hi svg{width:16px;height:16px}.mf .hi::after{inset:-10px}
"""

SCREEN = BASE_CSS + """
.cell{display:grid;place-items:center;height:120px;overflow:visible;border:1px dashed var(--color-border-secondary);border-radius:var(--radius-md);background:var(--color-bg-secondary)}
.cell .anc>.tt{white-space:nowrap}
.cell.tall{height:168px}
.dotx{width:24px;height:24px;border-radius:6px;background:var(--color-bg-primary);border:1px solid var(--color-border-primary)}
/* màn demo */
.ib{display:inline-grid;place-items:center;width:32px;height:32px;border-radius:var(--radius-control);border:1px solid var(--color-border-secondary);background:var(--color-bg-primary);color:var(--color-fg-tertiary)}
.ib.on{background:var(--color-bg-primary_hover);color:var(--color-fg-secondary)}
.fld{display:flex;flex-direction:column;gap:6px;max-width:320px}
.fld .lb{display:flex;align-items:center;gap:4px;font:500 13px/18px var(--font-body);color:var(--color-text-tertiary_strong)}
.fld .in{height:32px;border:1px solid var(--color-border-input);border-radius:var(--radius-field);padding:0 10px;display:flex;align-items:center;background:var(--color-bg-primary)}
.fld .hint{font-size:12px;line-height:16px;color:var(--color-text-tertiary)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px 24px;max-width:700px}
.toolbar{display:flex;gap:8px;align-items:center;padding:0 24px 12px}
.trunc{max-width:180px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:inline-block;vertical-align:middle}
/* khung tĩnh cho bảng biến thể mobile */
.mfr{position:relative;height:440px;overflow:hidden;background:var(--color-bg-primary)}
/* màn chi tiết */
.dh{display:flex;align-items:center;gap:8px;margin-bottom:16px}.dh .mono{font:600 18px/24px var(--font-code)}
.kv{display:grid;grid-template-columns:160px 1fr;gap:10px 16px;max-width:640px;font-size:14px;line-height:20px}.kv dt{color:var(--color-text-tertiary)}.kv dd{margin:0;min-width:0}
.trunc.w320{max-width:320px}
.mf{padding:16px;display:flex;flex-direction:column;gap:16px}
.mf .lb{display:flex;align-items:center;gap:6px;font:500 13px/18px var(--font-body);color:var(--color-text-tertiary)}
.mf .in{height:52px;border-radius:var(--radius-field);background:var(--color-bg-primary);display:flex;align-items:center;padding:0 16px;font-size:16px}
/* nhãn, lưới của bảng biến thể + khung khối preview */
.vl6{margin-bottom:6px}.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.r48{gap:48px;align-items:flex-start}.vgt{align-items:flex-start}
.pvp{padding:16px}.mf0{padding:0}.mb14{margin-bottom:14px}.m0{margin:0}
"""

# ---------- Bảng biến thể ----------
ARROWS = [("top", "Top", "p-bottom"), ("bottom", "Bottom", "p-top"), ("left", "Left", "p-right"), ("right", "Right", "p-left"),
          ("bl", "Bottom Left", "p-tl"), ("br", "Bottom Right", "p-tr")]


def cell(arrow, label, pos, title=None):
    t = tip("Tải trọng cho phép" if not title else "Tính cả vỏ container và hàng.", arrow, title, cls=pos)
    return f'<div><div class="vl vl6">Arrow={label}</div><div class="cell{" tall" if title else ""}"><span class="anc"><span class="dotx"></span>{t}</span></div></div>'


VAR_WEB = f"""<div class="vt">
<div><div class="vh">Type=Short × Arrow <small>đặt quanh điểm neo, cách 4 + mũi tên 4</small></div>
 <div class="g4">{"".join(cell(a, l, p) for a, l, p in ARROWS)}
 <div><div class="vl vl6">Arrow=None</div><div class="cell">{tip("Tải trọng cho phép theo đăng kiểm", "none")}</div></div></div></div>
<div><div class="vh">Type=Supporting <small>tiêu đề + mô tả, rộng tối đa 320</small></div>
 <div class="g4">
 {cell("bottom", "Bottom", "p-top", "Tổng trọng lượng")}{cell("top", "Top", "p-bottom", "Tổng trọng lượng")}
 <div><div class="vl vl6">Arrow=None</div><div class="cell tall">{tip("Tính cả vỏ container và hàng.", "none", "Tổng trọng lượng")}</div></div></div></div>
<div class="row r48">
 <div><div class="vh">Help icon <small>16, vùng di chuột 24</small></div><div class="vg">{help_icon()}<span class="hi on">{ic("help", 16)}</span><span class="vl">Default · Hover</span></div></div>
 <div><div class="vh">Chữ dài <small>xuống dòng, tối đa 240 / 320</small></div>
  <div class="vg vgt">{tip("Phí nâng hạ tính theo biểu phí của cảng tại ngày hạ container, chưa gồm VAT và phụ phí ngoài giờ.", "none")}
  {tip("Lệnh chỉ chuyển sang Hoàn tất khi đủ biên bản giao container có chữ ký của khách và ảnh chụp seal sau khi hạ bãi.", "none", "Vì sao chưa hoàn tất được?")}</div></div>
</div>
</div>"""

# ---------- Màn demo ----------
FORM = f"""<div class="pg">
<div class="sec-t" style="margin-bottom:14px">Thông tin hàng</div>
<div class="grid2">
 <div class="fld"><span class="lb">Số container</span><div class="in">TGHU 881234-5</div></div>
 <div class="fld"><span class="lb">Tổng trọng lượng (kg) <span class="anc" data-cmp>{help_icon("Giải thích tổng trọng lượng", 'data-js="tip"')}
  <span data-show="state:tip">{tip("Tính cả vỏ container và hàng. Không vượt tải trọng cho phép của xe.", "bl", "Tổng trọng lượng", cls="p-tl")}</span>
  <span data-show="state:long">{tip("Tổng trọng lượng = trọng lượng hàng + vỏ container (tare ghi trên cửa container). Lệnh bị chặn khi vượt tải trọng cho phép của tổ hợp đầu kéo – mooc theo đăng kiểm còn hiệu lực.", "bl", "Tổng trọng lượng", cls="p-tl")}</span></span></span>
  <div class="in">26.480</div><span class="hint">Vỏ 3.800 + hàng 22.680</span></div>
 <div class="fld"><span class="lb">Nhiệt độ cài đặt (°C) {help_icon("Giải thích nhiệt độ")}</span><div class="in">-18</div></div>
 <div class="fld"><span class="lb">Seal</span><div class="in">VN-2026-118845</div></div>
</div></div>"""

TABLE = f"""<div class="toolbar"><span class="sec-t" style="margin:0">48 lệnh</span><span class="sp"></span>
<span class="anc"><span class="ib">{ic("filter", 16)}</span></span>
<span class="anc" data-cmp><span class="ib" data-js="tip">{ic("dl", 16)}</span><span data-show="state:tip">{tip("Xuất Excel", "top", cls="p-bottom")}</span><span data-show="state:long">{tip("Xuất Excel (tối đa 5.000 dòng theo bộ lọc hiện tại)", "top", cls="p-bottom")}</span></span>
<span class="anc"><span class="ib">{ic("settings", 16)}</span></span></div>
<div style="padding:0 24px"><table class="tbl card" style="overflow:visible"><tr><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Xe</th></tr>
<tr><td class="mono">LVT-2026-0412</td><td><span class="anc" data-cmp><span class="trunc">Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics</span>
<span data-show="state:tip">{tip("Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics", "top", cls="p-bottom")}</span></span></td><td>Cát Lái → ICD Sóng Thần</td><td>51C-123.45</td></tr>
<tr><td class="mono">LVT-2026-0413</td><td><span class="trunc">Công ty CP Thép Hoà Phát Dung Quất</span></td><td>Hiệp Phước → VSIP 2</td><td>51D-678.90</td></tr>
<tr><td class="mono">LVT-2026-0414</td><td><span class="trunc">Vinamilk</span></td><td>Cát Lái → Long Hậu</td><td>Chưa điều</td></tr></table></div>"""

APP = f"""<div style="position:relative;height:100%">
<div class="mf">
 <div><div class="lb">Tổng trọng lượng (kg) {help_icon("Giải thích tổng trọng lượng", 'data-js="sheet"')}</div><div class="in">26.480</div></div>
 <div><div class="lb">Số seal</div><div class="in">VN-2026-118845</div></div>
</div>
<div data-show="state:tip"><div class="scrim"></div><div class="sheet" data-cmp role="dialog" aria-label="Tổng trọng lượng"><div class="grab"></div><b>Tổng trọng lượng</b>
<p>Tính cả vỏ container và hàng. Không vượt tải trọng cho phép của xe.</p><button class="ok" data-js="ok">Đã hiểu</button></div></div>
<div data-show="state:long"><div class="scrim"></div><div class="sheet" data-cmp role="dialog"><div class="grab"></div><b>Tổng trọng lượng</b>
<p>Tổng trọng lượng = trọng lượng hàng + vỏ container (tare ghi trên cửa container). Lệnh bị chặn khi vượt tải trọng cho phép của tổ hợp đầu kéo – mooc theo đăng kiểm còn hiệu lực.</p><button class="ok">Đã hiểu</button></div></div>
</div>"""


def mini(attrs, inner, h=96):
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    return f'<div class="op" {a} style="padding:16px;display:flex;gap:28px;align-items:center;justify-content:center;min-height:{h}px">{inner}</div>'


def demo_pair(attrs):
    return mini(attrs, f'<span class="anc" style="margin-top:56px"><span class="ib">{ic("dl", 16)}</span>{tip("Xuất Excel", "bottom", cls="p-top")}</span>'
                       f'<span class="anc" style="margin:56px 0 0 90px">{help_icon()}{tip("Tính cả vỏ và hàng.", "bottom", "Tổng trọng lượng", cls="p-top")}</span>', 120)


DETAIL = f"""<div class="pg">
<div class="dh"><span class="mono">LVT-2026-0412</span>
 <span class="anc" data-cmp><button class="ib" aria-label="Sao chép mã lệnh" data-js="tip">{ic("copy", 16)}</button>
  <span data-show="state:tip">{tip("Sao chép mã lệnh", "top", cls="p-bottom")}</span></span>
 <span class="sp"></span>
 <span class="anc"><button class="ib" aria-label="In lệnh">{ic("print", 16)}</button></span></div>
<dl class="kv">
 <dt>Khách hàng</dt><dd>Công ty TNHH Giao nhận Vận tải Quốc tế Delta Logistics</dd>
 <dt>Tuyến</dt><dd>Cát Lái → ICD Sóng Thần</dd>
 <dt>Địa chỉ giao</dt><dd><span class="anc"><span class="trunc w320">Lô C3, đường số 7, KCN Sóng Thần 2, phường Dĩ An, TP. Dĩ An, Bình Dương</span>
  <span data-show="state:long">{tip("Lô C3, đường số 7, KCN Sóng Thần 2, phường Dĩ An, TP. Dĩ An, Bình Dương", "top", cls="p-bottom")}</span></span></dd>
 <dt>Xe · mooc</dt><dd>51C-123.45 · 51R-045.67</dd>
</dl></div>"""


def sheet_frame(long=False):
    body = ("Tổng trọng lượng = trọng lượng hàng + vỏ container (tare ghi trên cửa container). Lệnh bị chặn khi vượt tải trọng cho phép của tổ hợp đầu kéo – mooc theo đăng kiểm còn hiệu lực."
            if long else "Tính cả vỏ container và hàng. Không vượt tải trọng cho phép của xe.")
    return (f'<div class="mfr"><div class="mf"><div><div class="lb">Tổng trọng lượng (kg) {help_icon()}</div><div class="in">26.480</div></div></div>'
            f'<div class="scrim"></div><div class="sheet" role="dialog" aria-label="Tổng trọng lượng"><div class="grab"></div><b>Tổng trọng lượng</b>'
            f'<p>{body}</p><button class="ok">Đã hiểu</button></div></div>')


PICK = {"D1": "a", "D2": "a", "D3": "a", "D4": "a"}
_pa = " ".join(f'data-{k}="{v}"' for k, v in PICK.items())
MOB_ICON = (f'<div class="mf mf0"><div><div class="lb">Tổng trọng lượng (kg) {help_icon()}</div><div class="in">26.480</div></div>'
            f'<div><div class="lb">Nhiệt độ cài đặt (°C) <span class="hi on">{ic("help", 20)}</span></div><div class="in">-18</div></div></div>')
preview = {
    "version": 1, "pick": PICK,
    "changes": "Bản 28/10 theo tổ hợp chốt (cả 4 điểm theo đề xuất): nền tối, có mũi tên, icon trợ giúp dấu ?, tooltip Supporting có tiêu đề đậm + mô tả. "
               "Nút Đã hiểu trong Help sheet đổi sang Secondary cỡ MD (góp ý trên trang). Thêm màn chi tiết lệnh (nút chỉ icon + địa chỉ bị cắt).",
    "blocks": [
        {"title": "Web", "platform": "web", "note": "Type Short × Arrow 7 · Type Supporting · Help icon Default/Hover · chữ dài xuống dòng (tối đa 240 / 320)",
         "html": f'<div class="pv pvp" {_pa} data-platform="web" data-state="x">{VAR_WEB}</div>'},
        {"title": "Mobile (app)", "platform": "mobile",
         "note": "App không có tooltip (DEC-280): icon ? 20, vùng chạm 44, chạm mở Help sheet · tiêu đề, nội dung, nút Secondary MD 42 · chữ dài",
         "frames": [f'<div class="pv pvp" {_pa} data-platform="mobile" data-state="x">{MOB_ICON}</div>',
                    f'<div class="pv" {_pa} data-platform="mobile" data-state="x">{sheet_frame()}</div>',
                    f'<div class="pv" {_pa} data-platform="mobile" data-state="x">{sheet_frame(True)}</div>']},
    ],
}


VALUES = [
 {"part": "Tooltip Supporting", "prop": "padding-y", "value": 8, "platform": "Web", "sel": ".tt.sup", "cssProp": "padding", "tpl": "$ 12px"},
 {"part": "Tooltip Supporting", "prop": "padding-x", "value": 12, "platform": "Web", "sel": ".tt.sup", "cssProp": "padding", "tpl": "8px $"},
 {"part": "Tooltip Supporting", "prop": "max-width", "value": 280, "platform": "Web", "sel": ".tt.sup"},
 {"part": "Tooltip", "prop": "gap", "value": 2, "platform": "Web", "sel": ".tt"},
 {"part": "Help icon", "prop": "size", "value": 16, "platform": "Web", "sel": ".hi", "cssProp": ["width", "height"], "interactive": True, "hitArea": 24},
 {"part": "Help icon", "prop": "size", "value": 24, "platform": "Mobile", "sel": ".mf .hi", "cssProp": ["width", "height"], "interactive": True, "hitArea": 44},
]

page = {
    "component": "Tooltip",
    "slug": "tooltip",
    "title": "Tooltip Review",
    "subtitle": "Base component · Tooltip + Help icon · nhóm C (chỉ web; app dùng Help sheet — DEC-280)",
    "round": "preview",
    "brief": True,
    "preview": preview,
    "refs": {
        "untitled": {
            "summary": "Nền <mark>tối</mark> (bg-primary-solid) chữ trắng 12, có <mark>mũi tên</mark> tuỳ chọn, 2 kiểu: chỉ tiêu đề / tiêu đề + supporting text; hiện sau delay 300ms, focus bàn phím cũng mở. Help icon \"?\" 16 trong nhãn ô nhập.",
            "source": "design/_ref/untitled-ui/react/components/base/tooltip/tooltip.tsx",
        },
        "astryx": {
            "summary": "Tooltip v2 cũ (Base / Tooltip): nền đảo màu, đệm 4 × 8, bo 8, rộng tối đa 240, mũi tên 8 × 4 — đã có token `tooltip/*`.",
            "source": "design-system/components/l1/tooltip.md · tokens.json tooltip/*",
        },
        "usage": [
            "cross-process-flow · search-process, view-process (giải thích bước, tên dài bị cắt)",
            "Header web: nút tài khoản chỉ avatar, tên ở tooltip (DEC-290)",
            "Mọi nút chỉ icon trên web (thanh công cụ bảng)",
        ],
        "platform": "Nhóm C — chỉ web. App không có hover: chạm icon \"?\" mở Help sheet (tiêu đề, nội dung, nút Đã hiểu — DEC-280). Đã chốt biến thể 26/10: Arrow 6 × Type 2 + Help icon. Brainstorm gọn: 4 điểm về hình.",
    },
    "css": CSS, "cssScreen": SCREEN, "values": VALUES,
    "states": [
        {"key": "default", "label": "Chưa mở"},
        {"key": "tip", "label": "Đang hiện tooltip"},
        {"key": "long", "label": "Chữ dài"},
    ],
    "ideas": [],
    "decisions": [
        {"id": "D1", "title": "Nền tooltip",
         "why": "Tooltip nằm đè lên bảng, form. Nền <mark>tối</mark> tách khỏi nội dung ngay; nền <mark>trắng</mark> nhẹ hơn nhưng dễ lẫn với popover / menu.",
         "source": "tooltip.tsx · tokens color/bg/primary_solid = color/bg/primary_solid",
         "options": [
             {"label": "Nền tối", "desc": "bg/primary_solid, chữ trắng — như Untitled và v2 cũ.", "rec": True, "preview": demo_pair({"D1": "a"})},
             {"label": "Nền trắng + viền + bóng", "desc": "Hợp tooltip dài có tiêu đề; cần phân biệt với popover.", "preview": demo_pair({"D1": "b"})},
         ],
         "untitled": mini({"D1": "a"}, tip("This is a tooltip", "none")), "untitledNote": "bg-primary-solid",
         "astryx": mini({"D1": "a"}, tip("Xuất Excel", "none")), "astryxNote": "Base / Tooltip v2 cũ"},
        {"id": "D2", "title": "Mũi tên",
         "why": "Mũi tên chỉ rõ tooltip thuộc phần tử nào khi các icon nằm sát nhau (thanh công cụ). Bỏ mũi tên thì gọn hơn nhưng phải dựa vào khoảng cách.",
         "source": "Biến thể đã chốt: Arrow Top · Bottom · Left · Right · Bottom Left/Right · None",
         "options": [
             {"label": "Có mũi tên", "desc": "Mặc định có; Arrow=None cho tooltip neo vào vùng rộng.", "rec": True, "preview": demo_pair({"D2": "a"})},
             {"label": "Không mũi tên", "desc": "Chỉ dùng Arrow=None; tooltip cách điểm neo 8.", "preview": demo_pair({"D2": "b"})},
         ]},
        {"id": "D3", "title": "Icon trợ giúp trong nhãn",
         "why": "Icon đứng sau nhãn ô nhập để mở giải thích. \"?\" = hỏi cách hiểu; \"i\" = thông tin thêm — dễ nhầm với icon Alert info.",
         "source": "Biến thể đã chốt: Kèm theo › Help Icon · Input Phần kèm › Help Icon",
         "options": [
             {"label": "Dấu ? trong vòng tròn", "desc": "Như Untitled (help-circle).", "rec": True,
              "preview": mini({"D3": "a"}, f'<div class="fld"><span class="lb">Tổng trọng lượng (kg) {help_icon()}</span><div class="in">26.480</div></div>')},
             {"label": "Chữ i trong vòng tròn", "desc": "Trùng hình với icon Alert / Notification info.",
              "preview": mini({"D3": "b"}, f'<div class="fld"><span class="lb">Tổng trọng lượng (kg) {help_icon()}</span><div class="in">26.480</div></div>')},
         ]},
        {"id": "D4", "title": "Tooltip có tiêu đề (Supporting)",
         "why": "Type=Supporting dùng cho giải thích dài. Có tiêu đề đậm giúp đọc lướt; bỏ tiêu đề thì gọn nhưng đoạn dài đọc như một khối.",
         "source": "Biến thể đã chốt: Type Short · Supporting",
         "options": [
             {"label": "Tiêu đề đậm + mô tả", "desc": "Như Untitled; mô tả chữ thường, mờ hơn.", "rec": True,
              "preview": mini({"D4": "a"}, tip("Tính cả vỏ container và hàng. Không vượt tải trọng cho phép của xe.", "none", "Tổng trọng lượng"))},
             {"label": "Một đoạn chữ", "desc": "Supporting chỉ khác Short ở độ rộng tối đa.",
              "preview": mini({"D4": "b"}, tip("Tính cả vỏ container và hàng. Không vượt tải trọng cho phép của xe.", "none", "Tổng trọng lượng"))},
         ]},
    ],
    "presets": [
        {"id": "rec", "label": "Đề xuất", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a"}},
        {"id": "untitled", "label": "Theo Untitled", "pick": {"D1": "a", "D2": "a", "D3": "a", "D4": "a"}},
        {"id": "astryx", "label": "Astryx hiện tại", "pick": {"D1": "a", "D2": "a", "D3": "b", "D4": "b"}},
    ],
    "screens": [
        {"id": "var-web", "name": "Bảng biến thể", "device": "web", "width": 1280, "shell": "none",
         "note": "Toàn bộ biến thể đã chốt 26/10, đổi theo D1–D4 và Light/Dark.", "html": VAR_WEB},
        {"id": "form-web", "name": "Form thông tin hàng", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Sửa lệnh LVT-2026-0412",
         "note": "Bấm icon ? cạnh Tổng trọng lượng để mở tooltip có tiêu đề.", "html": FORM},
        {"id": "table-web", "name": "Bảng lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Lệnh vận tải",
         "note": "Tooltip cho nút chỉ icon và cho tên khách bị cắt. Bấm nút Tải.", "html": TABLE},
        {"id": "detail-web", "name": "Chi tiết lệnh", "device": "web", "width": 1280, "nav": "Lệnh vận tải", "title": "Chi tiết lệnh",
         "note": "Bấm nút sao chép cạnh mã lệnh; trạng thái Chữ dài hiện tooltip cho địa chỉ bị cắt.", "html": DETAIL},
        {"id": "help-app", "name": "Help sheet (app)", "device": "mobile", "nav": "Lệnh", "title": "Thông tin hàng", "back": True,
         "note": "App không có tooltip: chạm ? mở Help sheet (DEC-280). Chỉ D3 (icon ?) áp ở đây; nút Đã hiểu là Secondary.", "html": APP},
    ],
    "proto": [
        {"sel": "[data-js=tip]", "state": "tip", "toggle": True, "back": "default"},
        {"sel": "[data-js=sheet]", "state": "tip"},
        {"sel": "[data-js=ok]", "close": True},
    ],
    "protoLayers": [".tt", ".sheet"],
    "protoHint": "bấm icon ?, nút Tải; trên app chạm ?",
}

write(OUT, page)
