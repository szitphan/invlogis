#!/usr/bin/env python3
"""Sinh page.json cho Tooltip (+ Help icon; app dùng Help sheet, DEC-280) — brainstorm gọn (28/10).
Chạy: python3 design/v2/components/_work/tooltip/build.py && python3 _scripts/ds-component-page.py tooltip
Biến thể đã chốt: trang Chốt biến thể Base (VQDsMrBW37W3QWVTPN79qC, db variants/tooltip v1, 26/10): Arrow 6 × Type 2 + Help icon, chỉ web.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import ic, tok_css, BASE_CSS, write  # noqa: E402

OUT = Path(__file__).parent / "page.json"


def tip(text, arrow="top", title=None, cls="", attrs=""):
    """arrow = top | bottom | left | right | bl | br | none — phía có mũi tên (tooltip nằm ngược phía)."""
    body = f"<b>{title}</b><span>{text}</span>" if title else f"<span>{text}</span>"
    return f'<span class="tt a-{arrow}{" sup" if title else ""} {cls}" role="tooltip" {attrs}>{body}</span>'


def help_icon(label="Giải thích", attrs=""):
    return (f'<button class="hi" aria-label="{label}" {attrs}><span class="q">{ic("help", 16)}</span>'
            f'<span class="i2">{ic("info", 16)}</span></button>')


CSS = tok_css() + BASE_CSS + """
.tt{position:relative;display:inline-flex;flex-direction:column;gap:2px;max-width:var(--tooltip-max-width);padding:var(--tooltip-padding-y) var(--tooltip-padding-x);
 border-radius:var(--tooltip-radius);background:var(--tooltip-bg);color:var(--tooltip-fg);font:600 12px/16px var(--font-body);text-align:left;
 box-shadow:0 4px 12px var(--color-shadow-md)}
.tt.sup{padding:8px 12px;max-width:280px}.tt.sup b{font:600 12px/16px var(--font-body)}.tt.sup span{font-weight:400;opacity:.86}
.tt::after{content:"";position:absolute;width:0;height:0;border:var(--tooltip-arrow-h) solid transparent}
/* mũi tên — tên theo phía của mũi tên trên tooltip */
.tt.a-bottom::after{top:100%;left:50%;margin-left:calc(var(--tooltip-arrow-h) * -1);border-top-color:var(--tt-arrow,var(--tooltip-bg))}
.tt.a-top::after{bottom:100%;left:50%;margin-left:calc(var(--tooltip-arrow-h) * -1);border-bottom-color:var(--tt-arrow,var(--tooltip-bg))}
.tt.a-left::after{right:100%;top:50%;margin-top:calc(var(--tooltip-arrow-h) * -1);border-right-color:var(--tt-arrow,var(--tooltip-bg))}
.tt.a-right::after{left:100%;top:50%;margin-top:calc(var(--tooltip-arrow-h) * -1);border-left-color:var(--tt-arrow,var(--tooltip-bg))}
.tt.a-bl::after{top:100%;left:12px;border-top-color:var(--tt-arrow,var(--tooltip-bg))}
.tt.a-br::after{top:100%;right:12px;border-top-color:var(--tt-arrow,var(--tooltip-bg))}
.tt.a-none::after{display:none}
/* D1 nền: a tối (bg/inverse) · b trắng + viền + bóng */
[data-D1=b] .tt{background:var(--color-bg-surface);color:var(--color-text-primary);box-shadow:0 0 0 1px var(--color-border-default),0 8px 20px var(--color-shadow-md);--tt-arrow:var(--color-bg-surface)}
[data-D1=b] .tt.sup span{color:var(--color-text-secondary);opacity:1}
/* D2 mũi tên: a có · b không */
[data-D2=b] .tt::after{display:none}
/* D3 icon trợ giúp: a "?" · b "i" */
.hi{display:inline-grid;place-items:center;width:16px;height:16px;padding:0;border:0;background:none;color:var(--color-icon-secondary);cursor:help;position:relative;vertical-align:-3px}
.hi::after{content:"";position:absolute;inset:-4px}
.hi:hover,.hi.on{color:var(--color-icon-primary)}
.hi .q{display:grid}.hi .i2{display:none}
[data-D3=b] .hi .i2{display:grid}[data-D3=b] .hi .q{display:none}
/* D4 tooltip có tiêu đề: a tiêu đề + mô tả · b chỉ một đoạn */
[data-D4=b] .tt.sup b{display:none}[data-D4=b] .tt.sup span{font-weight:600;opacity:1}
[data-D4=b][data-D1=b] .tt.sup span,[data-D4=b] [data-D1=b] .tt.sup span{color:var(--color-text-primary)}
/* đặt tooltip quanh điểm neo */
.anc{position:relative;display:inline-flex;align-items:center}
.anc>.tt{position:absolute;z-index:4;white-space:normal;width:max-content}
.anc>.tt.p-top{bottom:calc(100% + var(--tooltip-offset) + var(--tooltip-arrow-h));left:50%;transform:translateX(-50%)}
.anc>.tt.p-bottom{top:calc(100% + var(--tooltip-offset) + var(--tooltip-arrow-h));left:50%;transform:translateX(-50%)}
.anc>.tt.p-right{left:calc(100% + var(--tooltip-offset) + var(--tooltip-arrow-h));top:50%;transform:translateY(-50%)}
.anc>.tt.p-left{right:calc(100% + var(--tooltip-offset) + var(--tooltip-arrow-h));top:50%;transform:translateY(-50%)}
.anc>.tt.p-tl{bottom:calc(100% + var(--tooltip-offset) + var(--tooltip-arrow-h));left:-6px}
.anc>.tt.p-tr{bottom:calc(100% + var(--tooltip-offset) + var(--tooltip-arrow-h));right:-6px}
.cell{display:grid;place-items:center;height:120px;overflow:visible;border:1px dashed var(--color-border-default);border-radius:var(--radius-md);background:var(--color-bg-muted)}
.cell .anc>.tt{white-space:nowrap}
.dotx{width:24px;height:24px;border-radius:6px;background:var(--color-bg-surface);border:1px solid var(--color-border-strong)}
/* màn demo */
.ib{display:inline-grid;place-items:center;width:32px;height:32px;border-radius:var(--radius-control);border:1px solid var(--color-border-default);background:var(--color-bg-surface);color:var(--color-icon-secondary)}
.ib.on{background:var(--color-bg-hover);color:var(--color-icon-primary)}
.fld{display:flex;flex-direction:column;gap:6px;max-width:320px}
.fld .lb{display:flex;align-items:center;gap:4px;font:500 13px/18px var(--font-body);color:var(--color-text-secondary-strong)}
.fld .in{height:32px;border:1px solid var(--field-border-default);border-radius:var(--radius-field);padding:0 10px;display:flex;align-items:center;background:var(--field-bg-web)}
.fld .hint{font-size:12px;line-height:16px;color:var(--color-text-secondary)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px 24px;max-width:700px}
.toolbar{display:flex;gap:8px;align-items:center;padding:0 24px 12px}
.trunc{max-width:180px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:inline-block;vertical-align:middle}
/* Help sheet (app) */
.scrim{position:absolute;inset:0;background:var(--color-overlay-scrim);z-index:5}
.sheet{position:absolute;left:0;right:0;bottom:0;z-index:6;background:var(--color-bg-surface);border-radius:28px 28px 0 0;padding:8px 20px 28px}
.sheet .grab{width:36px;height:4px;border-radius:2px;background:var(--color-border-strong);margin:4px auto 16px}
.sheet b{display:block;font:600 17px/24px var(--font-body);margin-bottom:8px}
.sheet p{margin:0 0 20px;color:var(--color-text-secondary-strong);font-size:15px;line-height:22px}
.sheet .ok{width:100%;height:52px;border:0;border-radius:999px;background:var(--button-bg-primary);color:var(--button-fg-primary);font:600 15px var(--font-body)}
.mf{padding:16px;display:flex;flex-direction:column;gap:16px}
.mf .lb{display:flex;align-items:center;gap:6px;font:500 13px/18px var(--font-body);color:var(--color-text-secondary)}
.mf .in{height:52px;border-radius:16px;background:var(--field-bg-app);display:flex;align-items:center;padding:0 16px;font-size:16px}
.mf .hi{width:24px;height:24px}.mf .hi svg{width:20px;height:20px}.mf .hi::after{inset:-10px}
"""

# ---------- Bảng biến thể ----------
ARROWS = [("top", "Top", "p-bottom"), ("bottom", "Bottom", "p-top"), ("left", "Left", "p-right"), ("right", "Right", "p-left"),
          ("bl", "Bottom Left", "p-tl"), ("br", "Bottom Right", "p-tr")]


def cell(arrow, label, pos, title=None):
    t = tip("Tải trọng cho phép" if not title else "Tính cả vỏ container và hàng.", arrow, title, cls=pos)
    return f'<div><div class="vl" style="margin-bottom:6px">Arrow={label}</div><div class="cell"><span class="anc"><span class="dotx"></span>{t}</span></div></div>'


VAR_WEB = f"""<div class="vt">
<div><div class="vh">Type=Short × Arrow <small>đặt quanh điểm neo, cách 4 + mũi tên 4</small></div>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{"".join(cell(a, l, p) for a, l, p in ARROWS)}
 <div><div class="vl" style="margin-bottom:6px">Arrow=None</div><div class="cell">{tip("Tải trọng cho phép theo đăng kiểm", "none")}</div></div></div></div>
<div><div class="vh">Type=Supporting <small>tiêu đề + mô tả, rộng tối đa 280</small></div>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">
 {cell("bottom", "Bottom", "p-top", "Tổng trọng lượng")}{cell("top", "Top", "p-bottom", "Tổng trọng lượng")}
 <div><div class="vl" style="margin-bottom:6px">Arrow=None</div><div class="cell">{tip("Tính cả vỏ container và hàng.", "none", "Tổng trọng lượng")}</div></div></div></div>
<div class="row" style="gap:48px;align-items:flex-start">
 <div><div class="vh">Help icon <small>16, vùng di chuột 24</small></div><div class="vg">{help_icon()}<span class="hi on">{ic("help", 16)}</span><span class="vl">Default · Hover</span></div></div>
 <div><div class="vh">Chữ dài <small>xuống dòng, tối đa 240 / 280</small></div>
  <div class="vg" style="align-items:flex-start">{tip("Phí nâng hạ tính theo biểu phí của cảng tại ngày hạ container, chưa gồm VAT và phụ phí ngoài giờ.", "none")}
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


page = {
    "component": "Tooltip",
    "slug": "tooltip",
    "title": "Tooltip Review",
    "subtitle": "Base component · Tooltip + Help icon · nhóm C (chỉ web; app dùng Help sheet — DEC-280)",
    "round": "brainstorm",
    "brief": True,
    "refs": {
        "untitled": {
            "summary": "Nền <mark>tối</mark> (bg-primary-solid) chữ trắng 12, có <mark>mũi tên</mark> tuỳ chọn, 2 kiểu: chỉ tiêu đề / tiêu đề + supporting text; hiện sau delay 300ms, focus bàn phím cũng mở. Help icon \"?\" 16 trong nhãn ô nhập.",
            "source": "design/_ref/untitled-ui/react/components/base/tooltip/tooltip.tsx",
        },
        "astryx": {
            "summary": "Tooltip v2 cũ (Base / Tooltip): nền đảo màu, đệm 4 × 8, bo 8, rộng tối đa 240, mũi tên 8 × 4 — đã có token `tooltip/*`.",
            "source": "design/v2/components/l1/tooltip.md · tokens.json tooltip/*",
        },
        "usage": [
            "cross-process-flow · search-process, view-process (giải thích bước, tên dài bị cắt)",
            "Header web: nút tài khoản chỉ avatar, tên ở tooltip (DEC-290)",
            "Mọi nút chỉ icon trên web (thanh công cụ bảng)",
        ],
        "platform": "Nhóm C — chỉ web. App không có hover: chạm icon \"?\" mở Help sheet (tiêu đề, nội dung, nút Đã hiểu — DEC-280). Đã chốt biến thể 26/10: Arrow 6 × Type 2 + Help icon. Brainstorm gọn: 4 điểm về hình.",
    },
    "css": CSS,
    "states": [
        {"key": "default", "label": "Chưa mở"},
        {"key": "tip", "label": "Đang hiện tooltip"},
        {"key": "long", "label": "Chữ dài"},
    ],
    "ideas": [],
    "decisions": [
        {"id": "D1", "title": "Nền tooltip",
         "why": "Tooltip nằm đè lên bảng, form. Nền <mark>tối</mark> tách khỏi nội dung ngay; nền <mark>trắng</mark> nhẹ hơn nhưng dễ lẫn với popover / menu.",
         "source": "tooltip.tsx · tokens tooltip/bg = color/bg/inverse",
         "options": [
             {"label": "Nền tối", "desc": "bg/inverse, chữ trắng — như Untitled và v2 cũ.", "rec": True, "preview": demo_pair({"D1": "a"})},
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
        {"id": "help-app", "name": "Help sheet (app)", "device": "mobile", "nav": "Lệnh", "title": "Thông tin hàng", "back": True,
         "note": "App không có tooltip: chạm ? mở Help sheet (DEC-280). Bảng chọn D1–D4 không áp ở đây.", "html": APP},
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
