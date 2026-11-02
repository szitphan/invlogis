#!/usr/bin/env python3
"""Bộ dựng dùng chung cho họ form của DS v2 (Input · Tag · Select · Multiselect · Dropdown) — vòng 1 Brainstorm.

Mỗi component có build.py riêng trong _work/{slug}/ và import file này. Hình vẽ tự do (chưa gắn token, vòng 3 mới đối
chiếu foundation), màu than chì theo DEC-260 F3, cỡ control web 28 · 32 · 40 (F7), ô app theo DEC-207 / DEC-259.

Quy ước trạng thái: phần tử có class is-hover / is-focus / is-open / is-dis / is-err / is-ro / is-filled vẽ trạng thái cố
định (bảng biến thể, hình nhỏ). Phần tử mang data-live nhận trạng thái theo Bảng chọn của màn (.pv[data-state=…]).
"""
import json
import sys
from pathlib import Path

# ---------- icon (Lucide, nét 2) ----------
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
from pvkit import tok_css_nested  # noqa: E402

P = {
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "chevup": '<path d="M18 15l-6-6-6 6"/>',
    "chevr": '<path d="M9 6l6 6-6 6"/>',
    "check": '<path d="M5 12l5 5 9-10"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/>',
    "err": '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "clip": '<path d="M21 11l-9 9a5 5 0 0 1-7-7l9-9a3.5 3.5 0 0 1 5 5l-9 9a2 2 0 0 1-3-3l8-8"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
    "pin": '<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z"/>',
    "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/>',
    "copy": '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
    "trash": '<path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14"/>',
    "dl": '<path d="M12 4v11M7 10l5 5 5-5"/><path d="M4 19h16"/>',
    "more": '<circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>',
    "out": '<path d="M15 4h4a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-4M10 16l4-4-4-4M14 12H4"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1.2l2-1.5-2-3.4-2.3.9a7 7 0 0 0-2-1.2L14 3h-4l-.6 2.6a7 7 0 0 0-2 1.2l-2.3-.9-2 3.4 2 1.5a7 7 0 0 0 0 2.4l-2 1.5 2 3.4 2.3-.9a7 7 0 0 0 2 1.2L10 21h4l.6-2.6a7 7 0 0 0 2-1.2l2.3.9 2-3.4-2-1.5c.1-.4.1-.8.1-1.2z"/>',
    "filter": '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
    "eyeoff": '<path d="M3 3l18 18M10.6 6.1A10 10 0 0 1 12 6c6.5 0 10 6 10 6a17 17 0 0 1-3.3 3.9M6.6 6.6A17 17 0 0 0 2 12s3.5 6 10 6a9.7 9.7 0 0 0 4-.9"/>',
    "send": '<path d="M4 12l16-8-6 16-3-7z"/>',
    "print": '<path d="M7 9V3h10v6M7 17H4v-7h16v7h-3"/><rect x="7" y="14" width="10" height="7"/>',
    "route": '<circle cx="6" cy="19" r="2"/><circle cx="18" cy="5" r="2"/><path d="M8 19h8a3 3 0 0 0 0-6H8a3 3 0 0 1 0-6h8"/>',
}


def ic(k, s=16, cls="i"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[k]}</svg>')


# ---------- dữ liệu mẫu cố định (logistics) ----------
DRIVERS = [("Trần Văn Bình", "TB", "#E7EFFD", "#1F4FB8"), ("Lê Thị Hoa", "LH", "#FDECEC", "#B42318"),
           ("Phạm Quốc Dũng", "PD", "#E8F5EC", "#1B7542"), ("Nguyễn Minh Khoa", "NK", "#F3EEFF", "#6A50E4"),
           ("Võ Thành Tâm", "VT", "#FFF4E5", "#B54708")]


def av(i, s=20):
    n, t, bg, fg = DRIVERS[i % len(DRIVERS)]
    return f'<span class="av" style="width:{s}px;height:{s}px;background:{bg};color:{fg};font-size:{max(8, s // 2 - 1)}px">{t}</span>'


DOT = {"gray": "#737373", "blue": "#2E6BE6", "green": "#17B26A", "yellow": "#F79009", "red": "#F04438", "purple": "#7A5AF8"}


def dot(c):
    return f'<span class="dot" style="background:{DOT[c]}"></span>'


FLAG = {"VN": ("#DA251D", "#FFCD00"), "CN": ("#DE2910", "#FFDE00"), "KH": ("#032EA1", "#E00025"), "LA": ("#CE1126", "#002868")}


def flag(code):
    a, b = FLAG[code]
    return (f'<svg class="flag" viewBox="0 0 20 14" width="18" height="13" role="img" aria-label="{code}">'
            f'<rect width="20" height="14" rx="2" fill="{a}"/><circle cx="10" cy="7" r="3" fill="{b}"/></svg>')


def cb(on=False, ind=False):
    k = "check" if on else ("minus" if ind else None)
    return f'<span class="cbx{" on" if (on or ind) else ""}">{ic(k, 12) if k else ""}</span>'


# ---------- CSS chung ----------
CSS = r"""
.pv{position:relative;
 
 color:var(--color-text-primary);font:14px/20px Inter,system-ui,sans-serif}
.pv[data-theme=dark]{
 }
.i{flex:none;display:block}
button{font:inherit;color:inherit}
/* ---- field ---- */
.f{display:flex;flex-direction:column;gap:6px;min-width:0;position:relative}
.lb{font:500 14px/20px Inter;color:var(--color-text-secondary);display:flex;gap:4px;align-items:center}
.lb .req{color:var(--color-text-error-primary)}
.lb .hi{color:var(--color-fg-tertiary);display:inline-flex}
.hn{font-size:12.5px;line-height:18px;color:var(--color-text-tertiary)}
.fe{font-size:12.5px;line-height:18px;color:var(--color-text-error-primary);display:flex;gap:6px;align-items:center}
/* ---- ô control (input, select trigger, multiselect) ---- */
.ctl{--h:32px;display:flex;align-items:center;gap:8px;min-height:var(--h);box-sizing:border-box;border:1px solid var(--color-border-input);border-radius:8px;background:var(--color-bg-primary);
 padding:0 12px;color:var(--color-text-primary);font:400 14px/20px Inter;min-width:0;position:relative;cursor:text}
.ctl.s-sm{--h:28px;font-size:13px;padding:0 10px;gap:6px}.ctl.s-lg{--h:40px;font-size:15px;padding:0 14px}
.ctl .v{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ctl .ph{flex:1;min-width:0;color:var(--color-text-placeholder);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ctl .ic{color:var(--color-fg-tertiary);display:inline-flex;flex:none}
.ctl .sub{color:var(--color-text-tertiary);white-space:nowrap}
.ctl.is-hover{border-color:var(--color-border-input_hover)}
.ctl.is-focus,.ctl.is-open{border-color:var(--color-focus-ring);box-shadow:inset 0 0 0 1px var(--color-focus-ring)}
.ctl.is-dis{background:var(--color-bg-disabled);color:var(--color-text-disabled);cursor:not-allowed}.ctl.is-dis .ic,.ctl.is-dis .v{color:var(--color-text-disabled)}
.ctl.is-err{border-color:var(--color-border-error)}.ctl.is-err.is-focus{box-shadow:inset 0 0 0 1px var(--color-focus-ring_error)}
.ctl.is-ro{background:var(--color-bg-secondary);border-color:var(--color-border-secondary);cursor:default}
.ctl .eic{color:var(--color-fg-error-primary);display:inline-flex}
/* trạng thái theo Bảng chọn (phần tử data-live) */
.pv[data-state=hover] [data-live]>.ctl{border-color:var(--color-border-input_hover)}
.pv[data-state=focus] [data-live]>.ctl,.pv[data-state=open] [data-live]>.ctl{border-color:var(--color-focus-ring);box-shadow:inset 0 0 0 1px var(--color-focus-ring)}
.pv[data-state=disabled] [data-live]>.ctl{background:var(--color-bg-disabled);color:var(--color-text-disabled)}
.pv[data-state=error] [data-live]>.ctl{border-color:var(--color-border-error)}
.pv[data-state=readonly] [data-live]>.ctl{background:var(--color-bg-secondary);border-color:var(--color-border-secondary)}
/* addon chữ đầu/cuối, nút cuối */
.ad{align-self:stretch;display:flex;align-items:center;color:var(--color-text-tertiary);white-space:nowrap;flex:none}
.ad.l{margin-left:-12px;padding:0 10px 0 12px;border-right:1px solid var(--color-border-primary);border-radius:7px 0 0 7px}
.ad.r{margin-right:-12px;padding:0 12px 0 10px;border-left:1px solid var(--color-border-primary);border-radius:0 7px 7px 0}
.ad.dd{gap:4px;color:var(--color-text-primary)}
.ab{align-self:stretch;margin:-1px -13px -1px 0;padding:0 12px;border:1px solid var(--color-border-primary);border-radius:0 8px 8px 0;background:var(--color-bg-primary);display:flex;align-items:center;gap:6px;font:600 13px Inter;color:var(--color-text-secondary);white-space:nowrap}
/* ---- tag ---- */
.tg{--th:24px;display:inline-flex;align-items:center;gap:4px;height:var(--th);box-sizing:border-box;padding:0 8px;border:1px solid var(--color-border-primary);border-radius:6px;background:var(--color-bg-primary);color:var(--color-text-secondary);font:500 12px/18px Inter;white-space:nowrap;max-width:200px;vertical-align:middle}
.tg.t-sm{--th:22px;padding:0 6px;font-size:12px}.tg.t-lg{--th:28px;padding:0 10px;font-size:13.5px;gap:6px}
.tg .tl{min-width:0;overflow:hidden;text-overflow:ellipsis}
.tg .ct{font-weight:600;font-size:11.5px;line-height:16px;background:var(--color-utility-neutral-100);color:var(--color-text-secondary);border-radius:3px;padding:0 5px;margin-left:2px}
.tg .x{display:inline-flex;color:var(--color-fg-tertiary);border-radius:3px;margin-right:-3px;padding:1px;border:0;background:none;cursor:pointer}
.tg .x:hover{background:var(--color-bg-primary_hover);color:var(--color-fg-tertiary)}
.tg .av{width:16px!important;height:16px!important;font-size:8px!important}
.tg.is-hover{background:var(--color-bg-primary_hover);border-color:var(--color-border-input)}
.tg.is-focus{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.tg.is-dis{opacity:.5}
.dot{width:6px;height:6px;border-radius:50%;flex:none;display:inline-block}
.av{border-radius:50%;display:inline-grid;place-items:center;font-weight:600;flex:none}
.flag{flex:none;display:block;border-radius:2px}
.cbx{width:14px;height:14px;border:1px solid var(--color-border-input);border-radius:4px;display:inline-grid;place-items:center;flex:none;background:var(--color-bg-primary);box-sizing:border-box}
.cbx.on{background:var(--color-accent-solid);border-color:var(--color-accent-solid);color:var(--color-text-inverse)}
.mi .cbx,.ro .cbx{width:16px;height:16px}
/* ---- menu (popover) ---- */
.mn{border:1px solid var(--color-border-secondary);border-radius:8px;background:var(--color-bg-primary_alt);box-shadow:var(--shadow-lg);padding:4px;display:flex;flex-direction:column;gap:1px;min-width:200px;box-sizing:border-box;max-height:320px;overflow:auto}
.mi{min-height:36px;display:flex;align-items:center;gap:8px;padding:0 8px;border-radius:6px;font:500 14px/20px Inter;color:var(--color-text-primary);cursor:pointer;box-sizing:border-box}
.mi .ml{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mi .ms{color:var(--color-text-tertiary);font-weight:400;margin-left:6px}
.mi .ic{color:var(--color-fg-tertiary);display:inline-flex}
.mi .ck{color:var(--color-text-primary);display:inline-flex;margin-left:auto}
.mi.hov,.mi:hover{background:var(--color-bg-primary_hover)}
.mi.sel{font-weight:600}
.mi.dis{color:var(--color-text-disabled);cursor:not-allowed}.mi.dis .ic{color:var(--color-text-disabled)}.mi.dis:hover{background:none}
.mi.dang{color:var(--color-text-error-primary)}.mi.dang .ic{color:var(--color-text-error-primary)}
.mh{padding:8px 8px 4px;font:600 12px/18px Inter;color:var(--color-text-tertiary)}
.mdv{height:1px;background:var(--color-border-secondary);margin:4px -4px}
.msr{display:flex;align-items:center;gap:8px;height:36px;padding:0 8px;border-bottom:1px solid var(--color-border-secondary);margin:-4px -4px 4px;color:var(--color-fg-tertiary)}
.mem{padding:20px 12px;text-align:center;color:var(--color-text-tertiary);font-size:13px}
.mem b{display:block;color:var(--color-text-primary);font-weight:600;margin-bottom:2px}
.kbd{margin-left:auto;font:500 11px/16px Inter;color:var(--color-text-tertiary);border:1px solid var(--color-border-secondary);border-radius:4px;padding:0 4px}
.scb{position:absolute;right:3px;top:8px;width:4px;height:60px;border-radius:2px;background:var(--color-bg-quaternary)}
/* option nhiều thông tin */
.ro{display:flex;gap:10px;align-items:flex-start;padding:8px;border-radius:6px;cursor:pointer}
.ro.hov,.ro:hover{background:var(--color-bg-primary_hover)}
.ro .ri{width:32px;height:32px;border-radius:8px;background:var(--color-bg-tertiary);display:grid;place-items:center;color:var(--color-fg-tertiary);flex:none}
.ro .rm{flex:1;min-width:0}
.ro .r1{display:flex;gap:6px;align-items:center;font:600 14px/20px Inter;min-width:0}
.ro .r1 .code{font:600 13px/20px "JetBrains Mono",ui-monospace,monospace;white-space:nowrap;flex:none}
.ro .r2{font-size:12.5px;line-height:18px;color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ro .rr{margin-left:auto;text-align:right;font-size:12.5px;color:var(--color-text-tertiary);white-space:nowrap}
.ro .ck{color:var(--color-text-primary);display:inline-flex;align-self:center}
.chip{display:inline-flex;align-items:center;gap:4px;font:500 11.5px/16px Inter;padding:2px 8px;border-radius:999px;background:var(--color-utility-neutral-100);color:var(--color-text-secondary);white-space:nowrap}
.chip.ok{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.chip.wa{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}.chip.er{background:var(--color-utility-red-50);color:var(--color-utility-red-700)}
.pv[data-theme=dark] .chip.ok{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.pv[data-theme=dark] .chip.wa{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}.pv[data-theme=dark] .chip.er{background:var(--color-utility-red-50);color:var(--color-utility-red-700)}
/* ---- mobile ---- */
.m .ctl{--h:48px;border-radius:var(--radius-field);padding:0 16px;font-size:16px}
.m .lb{font-size:14px}
.sht{position:absolute;left:0;right:0;bottom:0;z-index:9;background:var(--color-bg-primary_alt);border-radius:var(--radius-overlay) var(--radius-overlay) 0 0;padding:8px 0 24px;display:flex;flex-direction:column;max-height:78%;border:1px solid var(--shadow-xl-border);box-shadow:var(--shadow-xl)}
.sht .hd{width:36px;height:4px;border-radius:2px;background:var(--color-bg-quaternary);align-self:center;margin-bottom:8px;flex:none}
.sht .sh-t{font:600 17px/24px Inter;padding:4px 16px 8px;display:flex;align-items:center;justify-content:space-between}
.sht .sh-b{overflow:auto;padding:0 8px}
.sht .mi{min-height:52px;font-size:16px;padding:0 12px;border-radius:10px}
.sht .ro{padding:10px 12px}
.sht .sh-f{padding:12px 16px 0;border-top:1px solid var(--color-border-secondary);display:flex;gap:8px}
.sht .msr{margin:0 16px 8px;border:1px solid var(--color-border-primary);border-radius:var(--radius-control);height:44px;padding:0 12px}
.scr{position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));z-index:8}
.bt{height:32px;padding:0 12px;border:1px solid var(--color-border-primary);border-radius:8px;background:var(--color-bg-primary);display:inline-flex;align-items:center;justify-content:center;gap:6px;font:600 13.5px/18px Inter;white-space:nowrap;cursor:pointer;color:var(--color-text-primary)}
.bt.pri{background:var(--color-action-primary);color:var(--color-text-inverse);border-color:var(--color-action-primary)}
.bt.big{height:48px;border-radius:var(--radius-control);font-size:15px;flex:1}
.bt.ic-only{width:32px;padding:0}
.bt.ghost{border-color:transparent;background:none}
/* ---- bảng biến thể (màn Biến thể) ---- */
.vg{padding:20px 24px 32px;display:flex;flex-direction:column;gap:20px;background:var(--color-bg-primary)}
.vg h3{margin:0;font:600 15px/22px Inter;display:flex;gap:8px;align-items:baseline}
.vg h3 small{font:400 12.5px Inter;color:var(--color-text-tertiary)}
.vgr{display:grid;gap:14px 18px;align-items:start}
.vgc{display:flex;flex-direction:column;gap:6px;min-width:0}
.vgc>.tg,.vgc>.bt{align-self:flex-start}
.vgc>.cap{font:500 11.5px/16px Inter;color:var(--color-text-tertiary);letter-spacing:.2px}
.vgs{border-top:1px solid var(--color-border-secondary);padding-top:16px;display:flex;flex-direction:column;gap:12px}
.pv[data-platform=mobile] .vg{padding:12px 16px 96px;gap:16px}
"""

SCREEN_CSS = r"""
.pad{padding:16px 24px 24px;display:flex;flex-direction:column;gap:16px}.mpad{padding:8px 16px 96px;display:flex;flex-direction:column;gap:16px}
table{width:100%;border-collapse:collapse}td,th{padding:10px 16px;border-bottom:1px solid var(--color-border-secondary);text-align:left;font-size:13px;vertical-align:middle}th{color:var(--color-text-tertiary);font-weight:500;background:var(--color-bg-secondary);white-space:nowrap}
.tb{border:1px solid var(--color-border-secondary);border-radius:12px;overflow:visible}
.tb tr:last-child td{border-bottom:0}
.card{border:1px solid var(--color-border-secondary);border-radius:12px;padding:16px 20px;display:flex;flex-direction:column;gap:16px;background:var(--color-bg-primary)}
.card .h{font:600 15px/22px Inter;display:flex;justify-content:space-between;align-items:center}
.grid2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px 20px}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px 20px}
.span2{grid-column:span 2}
.form{max-width:760px}
.acts{display:flex;justify-content:flex-end;gap:8px}
.bar{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.mono{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12.5px}
.mcard{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);padding:12px 14px;display:flex;flex-direction:column;gap:6px;background:var(--color-bg-primary)}
.mcard b{font-size:15px}.mcard .s{color:var(--color-text-tertiary);font-size:13px}
.mfoot{position:absolute;left:0;right:0;bottom:0;padding:12px 16px 28px;background:var(--color-bg-primary);border-top:1px solid var(--color-border-secondary);display:flex;gap:8px;z-index:5}
.anchor{position:relative}
.pop{position:absolute;z-index:20;top:calc(100% + 4px);left:0}
.pop.r{left:auto;right:0}
.pv[data-platform=mobile] .grid2,.pv[data-platform=mobile] .grid3{grid-template-columns:1fr}
.pv[data-platform=mobile] .span2{grid-column:auto}
"""


# ---------- hình nhỏ cho phương án ----------
def mini(attrs, inner, w=440, plat="web"):
    """Hình nhỏ nằm trong .pv của kit (không mang lựa chọn) → luật ẩn data-show của kit sẽ ẩn nhầm.
    Hình nhỏ dùng data-mshow + luật ẩn riêng theo .pvm gần nhất (mshow_css)."""
    a = " ".join(f'data-{k}="{v}"' for k, v in attrs.items())
    inner = inner.replace('data-show="', 'data-mshow="')
    return f'<div class="pv pvm" data-platform="{plat}" {a} style="padding:8px;max-width:{w}px">{inner}</div>'


def mshow_css(decisions):
    sel = [f'.pvm:not([data-{d["id"]}="{chr(97 + i)}"]) [data-mshow~="{d["id"]}:{chr(97 + i)}"]'
           for d in decisions for i in range(len(d["options"]))]
    sel.append('.pvm [data-mshow*="state:"]')  # hình nhỏ không có trạng thái của Bảng chọn
    return ",".join(sel) + "{display:none!important}"


def dark_nested(css):
    """Hình nhỏ .pvm lồng trong .pv[data-theme=dark] → kế thừa biến Dark."""
    dark = css.split(".pv[data-theme=dark]{", 1)[1].split("}", 1)[0]
    return ".pv[data-theme=dark] .pv{" + dark + "}"


# ---------- bảng biến thể ----------
def vg_row(title, cells, cols=None, note=""):
    n = cols or len(cells)
    inner = "".join(f'<div class="vgc"><span class="cap">{c}</span>{h}</div>' for c, h in cells)
    return (f'<div class="vgs"><h3>{title}<small>{note}</small></h3>'
            f'<div class="vgr" style="grid-template-columns:repeat({n},minmax(0,1fr))">{inner}</div></div>')


def vg(blocks):
    return f'<div class="vg">{"".join(blocks)}</div>'


# ---------- ghi page.json ----------
def write(out, page, decisions, brief=True):
    """brief: brainstorm gọn cho Base đã chốt biến thể — chỉ điểm cần quyết, bỏ ý tưởng cộng đồng (ds-component-page.py,
    user chọn 28/10). Ý tưởng vẫn giữ trong build.py để mở lại bằng brief=False."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_lib"))
    from icon_dec329 import apply as _dec329
    _dec329(page)  # DEC-329: cỡ, nét, màu icon
    if brief:
        page["brief"] = True
        page.pop("ideas", None)
        page["presets"] = [p for p in page.get("presets", []) if p["id"] in ("rec", "untitled", "astryx")]
        for d in decisions:
            for o in d["options"]:
                o.pop("ideas", None)
    page["css"] = tok_css_nested() + page.get("css", "") + mshow_css(decisions) + dark_nested(CSS)
    Path(out).write_text(json.dumps(page, ensure_ascii=False, indent=1))
    print("ok", out, len(page.get("ideas", [])), "ý tưởng ·", len(decisions), "điểm ·",
          len(page.get("screens", [])), "màn ·", len(page.get("presets", [])), "bộ chọn")
