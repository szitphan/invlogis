#!/usr/bin/env python3
"""Sinh page.json cho Sidebar Navigation — trang Brainstorm mới (vòng 1, làm lại theo yêu cầu user 28/10).
Chạy: python3 design-system/components/_work/sidebar-navigation-r2/build.py && python3 _scripts/ds-component-page.py sidebar-navigation-r2
Đầu vào đã chốt: thẻ Sidebar trên trang Chốt biến thể Application (artifact L3pzcVoU11rCka42c9tHoS, db variants/sidebar v10, 27/10):
Type Sections Subheadings · Sections Dividers · Dual Tier · Slim × Width 280 · 240 × Nav item Link · Collapsible · Child · Badge ×
State Default · Hover · Current · Focus × Phần kèm Logo · Search · Account · Tenant Switch · Featured Card · mobile "web".
Ghi chú user: "Cần có cả bản sub heading". Phần phạm vi làm việc (thẻ chân menu, hộp thoại 3 cột) giữ theo DEC-288/289 — không hỏi lại.
Bản cũ (đã lên Figma): _work/sidebar-navigation/.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_forms"))
from kit import CSS, ic, mini, vg, vg_row, write  # noqa: E402
from kit import P as ICONS  # noqa: E402

OUT = Path(__file__).parent / "page.json"
ICONS.update({
    "home": '<path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21c1-4 4-6 7-6s6 2 7 6"/>',
    "fuel": '<path d="M4 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16M3 21h12M14 10h2a2 2 0 0 1 2 2v4a1.5 1.5 0 0 0 3 0V8l-3-3"/><path d="M7 8h4"/>',
    "money": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/>',
    "file": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/>',
    "db": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "panel": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 4v16"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8"/><path d="M10 21h4"/>',
    "swap": '<path d="M7 4L3 8l4 4M3 8h14M17 20l4-4-4-4M21 16H7"/>',
    "alert": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
})

# ---------- dữ liệu menu ----------
GROUPS = [
    ("Vận tải", [("home", "Tổng quan", None, None), ("file", "Lệnh vận tải", 12, None), ("list", "Điều phối xe", None, None),
                 ("map", "Bản đồ xe", None, None)]),
    ("Đội xe", [("truck", "Phương tiện", None, ["Đầu kéo", "Rơ moóc", "Xe tải"]), ("users", "Lái xe", None, None),
                ("wrench", "Bảo dưỡng sửa chữa", 3, None), ("fuel", "Quản lý dầu", None, None)]),
    ("Tài chính", [("money", "Chi phí chuyến", None, None), ("card", "Công nợ", 5, None)]),
    ("Hệ thống", [("db", "Danh mục", None, None), ("gear", "Cài đặt", None, None)]),
]
CUR = "Lệnh vận tải"
MODS = [("truck", "Vận tải"), ("wrench", "Bảo dưỡng"), ("fuel", "Dầu"), ("money", "Tài chính"), ("db", "Danh mục")]


def badge(n):
    return f'<span class="nb">{n}</span>' if n else ""


def item(icon, label, n=None, children=None, cur=False, st="", open_=True, live=False, long=None):
    lab = f'<span class="nl0 lnorm">{label}</span>' + (f'<span class="nl0" data-show="state:long">{long}</span>' if long else "")
    chev = f'<span class="cv{" op" if open_ else ""}">{ic("chev", 16)}</span>' if children else ""
    fly = (f'<div class="mn fly"><div class="flh">{label}</div>' + "".join(f'<div class="mi">{c}</div>' for c in children) + "</div>") if children else ""
    head = (f'<a class="ni{" cur" if cur is True else ""} {st}"{" data-live" if live else ""} title="{label}"><span class="nic">{ic(icon, 20)}</span>'
            f'{lab}{badge(n)}{chev}<span class="tip">{label}</span>{fly}</a>')
    kids = ""
    if children:
        kids = '<div class="kids' + ("" if open_ else " shut") + '">' + "".join(
            f'<a class="ni ch{" cur" if c == "Đầu kéo" and cur == "child" else ""}"><span class="cd"></span><span class="nl0">{c}</span></a>' for c in children) + "</div>"
    return head + kids


def nav(groups=GROUPS, cur=CUR, child_cur=False, live=None, long=None):
    out = []
    for gi, (g, items) in enumerate(groups):
        out.append(f'<div class="grp"><div class="gh">{g}</div>' if gi else '<div class="grp first">')
        for icon, lab, n, kids in items:
            out.append(item(icon, lab, n, kids, cur=(lab == cur) or ("child" if child_cur and kids else False),
                            live=lab == live, long=long if lab == live else None))
        out.append("</div>")
    return "".join(out)


def head(tenant=True):
    t = '<div class="tn"><span class="tnm">Delta Logistics</span><span class="tns">Chi nhánh Hồ Chí Minh</span></div>' if tenant else ""
    return (f'<div class="sbh"><span class="lg"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span><div class="hd0"><b class="lgw">invlogis</b>{t}</div>'
            f'<button class="clp" aria-label="Thu gọn menu">{ic("panel", 18)}</button></div>')


SEARCH = f'<div class="sbs">{ic("search", 16)}<span>Tìm tính năng</span><span class="kb">⌘K</span></div>'
FEAT = (f'<div class="fc"><div class="fct">{ic("alert", 16)}<b>3 xe sắp hết hạn đăng kiểm</b></div>'
        '<span>51C-482.19 hết hạn 05/11. Lên lịch đăng kiểm để không lỡ chuyến.</span><a>Xem danh sách</a></div>')
SCOPE = (f'<div class="scope"><span class="sic">{ic("truck", 18)}</span><div class="smm"><b>Vận tải</b><span>Toàn chi nhánh</span></div>'
         f'<span class="sw">{ic("swap", 16)}</span></div>')
ACC = (f'<div class="acc"><span class="av0">NA</span><div class="smm"><b>Nguyễn Văn An</b><span>Điều phối viên</span></div>'
       f'<span class="sw">{ic("more", 16)}</span></div>')


def sidebar(kind="sub", width=280, feat=True, live=None, long=None, child_cur=False, search=True):
    """kind: sub (Sections Subheadings) · div (Sections Dividers) · dual (Dual Tier) · slim (Slim)."""
    if kind == "dual":
        rail = "".join(f'<a class="rl{" cur" if i == 0 else ""}" title="{l}">{ic(k, 20)}<span class="rlt">{l}</span></a>' for i, (k, l) in enumerate(MODS))
        g = GROUPS[:1] + [("Báo cáo", [("file", "Báo cáo chuyến", None, None), ("money", "Doanh thu tuyến", None, None)])]
        return (f'<aside class="sb dual" data-cmp style="--sbw:{width}px"><div class="rail"><span class="lg"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJmcyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSIwLjAiIHkxPSIwLjAiIHgyPSIwLjAiIHkyPSIzMi4wIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM0RjYyRUUiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iZmQiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMC4wIiB5MT0iMC4wIiB4Mj0iMC4wIiB5Mj0iMzIuMCI+PHN0b3Agb2Zmc2V0PSIwIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjNjU3N0YyIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHN0eWxlPi5ze2ZpbGw6dXJsKCNmcyl9LmR7ZmlsbDp1cmwoI2ZkKX1AbWVkaWEgKHByZWZlcnMtY29sb3Itc2NoZW1lOmRhcmspey5ze2ZpbGw6I0EzQjBGRn0uZHtmaWxsOiNENkRDRkZ9fTwvc3R5bGU+PHBhdGggY2xhc3M9InMiIGQ9Ik0xMS4wMCAzMS4wMCBMMjEuMDAgMzEuMDAgTDIxLjAwIDEzLjUwIEwxMS4wMCAxNi4wMFoiLz48cGF0aCBjbGFzcz0iZCIgZD0iTTExLjAwIDEyLjUwIEwyMS4wMCAxMC4wMCBMMjEuMDAgMS41MCBMMTEuMDAgNC4wMFoiLz48L3N2Zz4=" alt="" style="width:100%;height:100%;display:block"></span>{rail}<span class="av0 sm">NA</span></div>'
                f'<div class="pane"><div class="pnh">Vận tải<span>Chi nhánh Hồ Chí Minh</span></div>{SEARCH if search else ""}<nav class="nv">{nav(g, live=live, long=long)}</nav>'
                f'{FEAT if feat else ""}{SCOPE}</div></aside>')
    return (f'<aside class="sb k-{kind}" data-cmp style="--sbw:{width}px">{head()}{SEARCH if search else ""}'
            f'<nav class="nv">{nav(live=live, long=long, child_cur=child_cur)}</nav>{FEAT if feat else ""}{SCOPE}{ACC}</aside>')


# ---------- CSS ----------
CSS_SB = r"""
.sb{--sbw:280px;width:var(--sbw);box-sizing:border-box;height:100%;min-height:760px;border-right:1px solid var(--color-border-secondary);background:var(--color-bg-primary);display:flex;flex-direction:column;padding:12px 12px 12px;gap:8px;position:relative;flex:none}
.sbh{display:flex;align-items:center;gap:10px;padding:4px 4px 8px}
.lg{width:32px;height:32px;border-radius:8px;background:none;color:var(--color-text-inverse);display:grid;place-items:center;font:700 18px Inter;flex:none}
.hd0{display:flex;flex-direction:column;min-width:0;flex:1}
.lgw{font:700 16px/22px Inter;letter-spacing:-.2px}
.tn{display:flex;flex-direction:column;min-width:0}.tnm{display:none}.tns{font-size:12.5px;line-height:16px;color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.clp{border:0;background:none;color:var(--color-text-tertiary);width:28px;height:28px;border-radius:6px;display:grid;place-items:center;cursor:pointer}
.sbs{display:flex;align-items:center;gap:8px;height:36px;border:1px solid var(--color-border-primary);border-radius:8px;padding:0 10px;color:var(--color-text-tertiary);font-size:14px}
.sbs .kb{margin-left:auto;font:500 11px/16px Inter;color:var(--color-text-tertiary);border:1px solid var(--color-border-secondary);border-radius:4px;padding:0 4px}
.nv{flex:1;overflow:auto;display:flex;flex-direction:column;gap:4px;margin:0 -4px;padding:0 4px}
.grp{display:flex;flex-direction:column;gap:1px}
.gh{font:600 12px/18px Inter;color:var(--color-text-tertiary);padding:12px 10px 4px}
.ni{position:relative;display:flex;align-items:center;gap:10px;height:40px;padding:0 10px;border-radius:6px;color:var(--color-text-secondary);font:500 14px/20px Inter;cursor:pointer;text-decoration:none;min-width:0}
.ni .nic{color:var(--color-text-tertiary);display:inline-flex;flex:none}
.ni .nl0{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ni:hover,.ni.is-hover{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}
.ni.is-focus{box-shadow:0 0 0 2px var(--color-focus-gap),0 0 0 4px var(--color-focus-ring)}
.ni.cur{background:var(--color-bg-selected);color:var(--color-text-primary);font-weight:600}.ni.cur .nic{color:var(--color-text-primary)}
.nb{font:500 12px/18px Inter;border-radius:999px;padding:0 8px;background:var(--color-utility-neutral-100);color:var(--color-fg-tertiary);border:1px solid var(--color-border-secondary)}
.cv{color:var(--color-text-tertiary);display:inline-flex;transition:transform .15s}.cv:not(.op){transform:rotate(-90deg)}
.kids{display:flex;flex-direction:column;gap:1px}.kids.shut{display:none}
.ni.ch{height:36px;padding-left:40px;font-weight:500}
.cd{display:none}
.tip{display:none}
.fc{border:1px solid var(--color-border-secondary);border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:4px;font-size:13px;line-height:18px;color:var(--color-text-tertiary);background:var(--color-bg-secondary)}
.fct{display:flex;gap:6px;align-items:center;color:var(--color-text-primary)}.fct b{font-weight:600}.fct .i{color:var(--color-fg-warning-primary)}
.fc a{font-weight:600;color:var(--color-text-primary);text-decoration:underline;text-underline-offset:2px;margin-top:4px}
.scope,.acc{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:10px;border:1px solid var(--color-border-secondary)}
.acc{border-color:transparent;padding:6px 10px}
.sic{width:32px;height:32px;border-radius:8px;background:var(--color-bg-tertiary);display:grid;place-items:center;color:var(--color-text-secondary);flex:none}
.smm{display:flex;flex-direction:column;min-width:0;flex:1}.smm b{font:600 13.5px/18px Inter;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.smm>span{font-size:12.5px;line-height:16px;color:var(--color-text-tertiary)}
.sw{color:var(--color-text-tertiary);display:inline-flex}
.av0{width:32px;height:32px;border-radius:50%;background:var(--color-accent-bg);color:var(--color-accent-fg);display:grid;place-items:center;font:600 12px Inter;flex:none}.av0.sm{width:28px;height:28px;margin-top:auto}
/* Dividers: vạch thay nhãn nhóm */
.sb.k-div .gh{display:none}.sb.k-div .grp:not(.first){border-top:1px solid var(--color-border-secondary);padding-top:6px;margin-top:6px}
/* Dual tier */
.sb.dual{flex-direction:row;padding:0;gap:0}
.rail{width:64px;border-right:1px solid var(--color-border-secondary);display:flex;flex-direction:column;align-items:center;gap:4px;padding:12px 0}
.rail .lg{margin-bottom:8px}
.rl{width:48px;min-height:48px;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;color:var(--color-text-tertiary);cursor:pointer}
.rl.cur,.rl:hover{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}
.rlt{font:500 10.5px/14px Inter}
.pane{flex:1;min-width:0;display:flex;flex-direction:column;gap:8px;padding:12px}
.pnh{font:600 16px/22px Inter;display:flex;flex-direction:column;padding:4px 6px 4px}.pnh span{font:400 12.5px/16px Inter;color:var(--color-text-tertiary)}
/* Slim 64 */
.sb.k-slim,.pv[data-state=slim] [data-live-sb] .sb:not(.dual){--sbw:64px!important;padding:12px 8px;align-items:center}
.sb.k-slim :is(.hd0,.sbs span,.sbs .kb,.gh,.nl0,.nb,.cv,.kids,.fc,.smm,.sw,.clp),
.pv[data-state=slim] [data-live-sb] .sb:not(.dual) :is(.hd0,.sbs span,.sbs .kb,.gh,.nl0,.nb,.cv,.kids,.fc,.smm,.sw){display:none}
.sb.k-slim .ni,.pv[data-state=slim] [data-live-sb] .ni{width:44px;justify-content:center;padding:0}
.sb.k-slim .sbs,.pv[data-state=slim] [data-live-sb] .sbs{width:44px;justify-content:center;padding:0}
.sb.k-slim :is(.scope,.acc),.pv[data-state=slim] [data-live-sb] :is(.scope,.acc){padding:4px;border:0}
.sb.k-slim .grp:not(.first),.pv[data-state=slim] [data-live-sb] .grp:not(.first){border-top:1px solid var(--color-border-secondary);padding-top:6px;margin-top:6px}
.sb.k-slim .ni:has(.nb)::after,.pv[data-state=slim] [data-live-sb] .ni:has(.nb)::after{content:"";position:absolute;top:8px;right:8px;width:8px;height:8px;border-radius:50%;background:var(--color-utility-blue-600);border:2px solid var(--color-bg-primary)}
.pv[data-state=slim] [data-live-sb] .sbh{flex-direction:column}
/* trạng thái theo Bảng chọn */
.pv[data-state=hover] .ni[data-live]{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}
.pv[data-state=focus] .ni[data-live]{box-shadow:0 0 0 2px var(--color-focus-gap),0 0 0 4px var(--color-focus-ring)}
.pv[data-state=long] .ni[data-live] .lnorm{display:none}
/* D1 nhãn nhóm */
.pv[data-D1=b] .gh{text-transform:uppercase;letter-spacing:.5px;font-size:11.5px}
.pv[data-D1=c] .gh{font-size:13px;color:var(--color-text-primary);padding-top:14px}
/* D2 mục cha thu gọn: chevron trái */
.pv[data-D2=b] .ni:has(.cv){flex-direction:row}
.pv[data-D2=b] .ni:has(.cv) .cv{order:-1;margin-left:-6px;margin-right:-6px}
.pv[data-D2=c] .ni .cv{display:none}
/* D3 mục con */
.pv[data-D3=a] .kids{margin-left:20px;border-left:1px solid var(--color-border-secondary);padding-left:8px}.pv[data-D3=a] .ni.ch{padding-left:12px}
.pv[data-D3=c] .ni.ch{padding-left:20px}.pv[data-D3=c] .cd{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--color-bg-quaternary);margin:0 7px}
.pv[data-D3=c] .ni.ch.cur .cd{background:var(--color-fg-primary)}
/* D4 badge */
.pv[data-D4=b] .nb{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700);border-color:var(--color-utility-blue-700)}
.pv[data-D4=c] .nb{font-size:0;width:8px;height:8px;padding:0;border:0;background:var(--color-utility-blue-600)}
/* D5 mục đang chọn */
.pv[data-D5=b] .ni.cur{background:var(--color-bg-selected)}.pv[data-D5=b] .ni.cur::before{content:"";position:absolute;left:-12px;top:8px;bottom:8px;width:3px;border-radius:0 3px 3px 0;background:var(--color-fg-primary)}
.pv[data-D5=c] .ni.cur{background:none}
/* D6 tìm trong menu */
.pv[data-D6=b] .sb .sbs{width:36px;height:36px;padding:0;justify-content:center;position:absolute;top:16px;right:48px;border:0}
.pv[data-D6=b] .sb .sbs :is(span){display:none}
.pv[data-D6=c] .sb .sbs{display:none}
/* D7 thẻ nổi bật */
.pv[data-D7=b] .fc{background:var(--color-bg-warning-primary);border-color:var(--color-border-warning_subtle)}
.pv[data-D7=c] .fc{display:none}
/* D8 Slim: rê vào mục */
.pv[data-D8=a] .sb.k-slim .ni:hover .tip,.pv[data-D8=a] .sb.k-slim .ni.is-hover .tip,.pv[data-D8=a][data-state=slim] [data-live-sb] .ni:hover .tip{display:block;position:absolute;left:52px;top:8px;background:var(--color-bg-primary_solid);color:var(--color-text-inverse);font:500 12px/16px Inter;padding:4px 8px;border-radius:6px;white-space:nowrap;z-index:5}
.fly{display:none;position:absolute;left:52px;top:0;z-index:6;width:200px}
.flh{font:600 12px/18px Inter;color:var(--color-text-tertiary);padding:6px 8px 2px}
.pv[data-D8=b] .fly.on,.pv[data-D8=b] .sb.k-slim .ni.is-hover>.fly,
.pv[data-D8=b][data-state=slim] [data-live-sb] .ni:hover>.fly{display:flex}
.pv[data-D8=b] .sb.k-slim .ni:not(:has(.fly)):is(:hover,.is-hover) .tip,
.pv[data-D8=b][data-state=slim] [data-live-sb] .ni:not(:has(.fly)):hover .tip{display:block;position:absolute;left:52px;top:8px;background:var(--color-bg-primary_solid);color:var(--color-text-inverse);font:500 12px/16px Inter;padding:4px 8px;border-radius:6px;white-space:nowrap;z-index:5}
.sb.k-slim .nv,.pv[data-state=slim] [data-live-sb] .nv{overflow:visible}
.pv[data-theme=dark] .lg{background:none}
"""

SHELL = r"""
.shellw{display:flex;min-height:760px;background:var(--color-bg-primary);position:relative}
.mainw{flex:1;min-width:0;display:flex;flex-direction:column}
.tb0{height:44px;border-bottom:1px solid var(--color-border-secondary);display:flex;align-items:center;gap:8px;padding:0 24px;font:400 14px/20px Inter;color:var(--color-text-tertiary)}
.tb0 b{color:var(--color-text-primary);font-weight:500}.tb0 .r{margin-left:auto;display:flex;gap:4px;align-items:center}
.tb0 .ib{width:32px;height:32px;border-radius:8px;display:grid;place-items:center;color:var(--color-fg-tertiary);position:relative}
.tb0 .rc{position:absolute;top:2px;right:2px;min-width:16px;height:16px;border-radius:8px;background:var(--color-bg-error-solid);color:var(--color-text-white);font:600 10px/16px Inter;text-align:center;padding:0 4px;box-sizing:border-box}
.pt0{padding:20px 24px 8px;font:600 22px/30px Inter}
.pad{padding:8px 24px 24px;display:flex;flex-direction:column;gap:12px}
table{width:100%;border-collapse:collapse}td,th{padding:10px 14px;border-bottom:1px solid var(--color-border-secondary);text-align:left;font-size:13px}th{color:var(--color-text-tertiary);font-weight:500;background:var(--color-bg-secondary)}
.tb{border:1px solid var(--color-border-secondary);border-radius:12px;overflow:hidden}
.mono{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12.5px}
.chip.ok{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}
.tabs0{display:flex;gap:20px;border-bottom:1px solid var(--color-border-secondary);padding:0 24px}.tabs0 a{padding:10px 0;font:500 14px/20px Inter;color:var(--color-text-tertiary)}.tabs0 a.on{color:var(--color-text-primary);box-shadow:inset 0 -2px 0 var(--color-accent-solid)}
.kv{display:grid;grid-template-columns:160px 1fr;gap:10px 16px;border:1px solid var(--color-border-secondary);border-radius:12px;padding:16px;font-size:14px;margin:0}.kv dt{color:var(--color-text-tertiary)}.kv dd{margin:0}
.frm{max-width:560px;display:flex;flex-direction:column;gap:16px}.frm .row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}.frm .act{display:flex;gap:8px;justify-content:flex-end;padding-top:16px;border-top:1px solid var(--color-border-secondary)}
.dlg0{position:absolute;z-index:9;left:50%;top:180px;transform:translateX(-50%);width:400px;background:var(--color-bg-primary_alt);border-radius:12px;box-shadow:var(--elev-3);padding:20px;display:flex;flex-direction:column;gap:8px}
.dlg0 h4{margin:0;font:600 16px/24px Inter}.dlg0 p{margin:0;color:var(--color-text-tertiary);font-size:14px;line-height:20px}.dlg0 .act{display:flex;gap:8px;justify-content:flex-end;padding-top:12px}
.bt.dng{background:var(--color-bg-error-solid);border-color:var(--color-bg-error-solid);color:var(--color-text-white)}
.mweb{width:393px;height:760px;position:relative;overflow:hidden;background:var(--color-bg-primary)}
.mweb .sb{position:absolute;left:0;top:0;bottom:0;z-index:9;min-height:0;box-shadow:var(--elev-2);border-right:0}
.mtb{height:56px;display:flex;align-items:center;gap:8px;padding:0 8px;border-bottom:1px solid var(--color-border-secondary);font:600 16px/24px Inter}
"""


def m(over, inner, w=300):
    base = {"D1": "a", "D2": "a", "D3": "a", "D4": "a", "D5": "a", "D6": "a", "D7": "a", "D8": "a", "state": "x"}
    return mini({**base, **(over or {})}, inner, w)


def clip(html, h=520):
    return f'<div style="height:{h}px;overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:12px;display:flex">{html}</div>'


SB = clip(sidebar(feat=False))
SB_CH = clip(sidebar(feat=False, child_cur=True, search=False), 470)
SB_FULL = clip(sidebar(), 760)
SLIM = sidebar("slim", 64, feat=False).replace('<a class="ni" title="Điều phối xe">', '<a class="ni is-hover" title="Điều phối xe">', 1)
SLIM_PV = clip('<div style="position:relative">' + SLIM.replace('<div class="mn fly"><div class="flh">Phương tiện', '<div class="mn fly on"><div class="flh">Phương tiện', 1) + "</div>", 560)

decisions = [
 {"id": "D1", "title": "Nhãn nhóm (bản sub heading)",
  "why": "User ghi ở trang chốt biến thể: “Cần có cả bản sub heading”. DEC-288 đã chọn nhãn chữ hoa cho bản cũ — trang mới hỏi lại vì làm lại từ đầu.",
  "source": "variants/sidebar (ghi chú user) · DEC-288 D5",
  "options": [
   {"label": "Chữ thường, xám, đậm vừa (Untitled)", "desc": "Nhẹ, đọc tự nhiên tiếng Việt có dấu.", "rec": True, "preview": m({"D1": "a"}, SB), "ideas": ["I1", "I3"]},
   {"label": "Chữ HOA giãn chữ (DEC-288)", "desc": "Tách nhóm rõ khi lướt; chữ hoa tiếng Việt dấu chồng khó đọc hơn.", "preview": m({"D1": "b"}, SB), "ideas": ["I4"]},
   {"label": "Chữ đậm màu chính, cỡ 13", "desc": "Nhóm nổi như tiêu đề; lấn mục bên dưới.", "preview": m({"D1": "c"}, SB), "ideas": ["I5"]}],
  "untitled": m({"D1": "a"}, SB), "astryx": m({"D1": "b"}, SB), "astryxNote": "bản đã lên Figma (DEC-288)"},
 {"id": "D2", "title": "Mục cha thu gọn được (Collapsible)",
  "why": "Phương tiện có mục con Đầu kéo · Rơ moóc · Xe tải. Mũi tên đặt đâu, hay luôn mở.",
  "source": "variants/sidebar Nav item Collapsible",
  "options": [
   {"label": "Mũi tên bên phải, xoay khi mở", "desc": "Như Untitled; icon mục giữ thẳng cột.", "rec": True, "preview": m({"D2": "a"}, SB_CH), "ideas": ["I1", "I2"]},
   {"label": "Mũi tên bên trái", "desc": "Thấy ngay mục nào mở được; đẩy icon lệch cột.", "preview": m({"D2": "b"}, SB_CH), "ideas": ["I6"]},
   {"label": "Luôn mở, không mũi tên", "desc": "Ít bấm; menu dài khi module nhiều mục con.", "preview": m({"D2": "c"}, SB_CH), "ideas": ["I4"]}],
  "untitled": m({"D2": "a"}, SB_CH), "astryx": m({"D2": "a"}, SB_CH)},
 {"id": "D3", "title": "Mục con (Child)",
  "why": "Mục con cần thụt và cho thấy thuộc mục cha nào; mục con đang chọn phải nhận ra được.",
  "source": "variants/sidebar Nav item Child",
  "options": [
   {"label": "Thụt + đường dọc bên trái", "desc": "Thấy rõ nhóm; giống cây thư mục.", "rec": True, "preview": m({"D3": "a"}, SB_CH), "ideas": ["I2", "I3"]},
   {"label": "Chỉ thụt vào thẳng chữ mục cha (Untitled)", "desc": "Gọn nhất; mục con dễ lẫn với mục thường khi lướt.", "preview": m({"D3": "b"}, SB_CH), "ideas": ["I1"]},
   {"label": "Chấm tròn đầu mục con", "desc": "Chấm đậm ở mục đang chọn; thêm một dấu nhỏ cần học.", "preview": m({"D3": "c"}, SB_CH), "ideas": ["I7"]}],
  "untitled": m({"D3": "b"}, SB_CH), "astryx": m({"D3": "a"}, SB_CH)},
 {"id": "D4", "title": "Số đếm (Badge)",
  "why": "Lệnh vận tải 12 chờ xử lý, Bảo dưỡng 3, Công nợ 5. DEC-288 chọn xanh dương cho bản cũ.",
  "source": "variants/sidebar Nav item Badge · DEC-288",
  "options": [
   {"label": "Viên xám (Untitled)", "desc": "Nhẹ, không kéo mắt khỏi nội dung.", "preview": m({"D4": "a"}, SB), "ideas": ["I1", "I3"]},
   {"label": "Viên xanh dương (DEC-288)", "desc": "Thấy việc cần xử lý ngay; nhiều số thì menu sặc sỡ.", "rec": True, "preview": m({"D4": "b"}, SB), "ideas": ["I5", "I8"]},
   {"label": "Chỉ chấm", "desc": "Gọn; không biết bao nhiêu việc.", "preview": m({"D4": "c"}, SB), "ideas": ["I6"]}],
  "untitled": m({"D4": "a"}, SB), "astryx": m({"D4": "b"}, SB)},
 {"id": "D5", "title": "Mục đang ở (Current)",
  "why": "DEC-288 chọn nền xám chữ đậm. Có thêm vạch trái thì thấy chỗ đang ở cả khi rê chuột mục khác (rê cũng nền xám).",
  "source": "variants/sidebar State Current · DEC-288 D6",
  "options": [
   {"label": "Nền xám, chữ đậm (DEC-288)", "desc": "Đúng Untitled; trùng nền với Hover — phân biệt bằng chữ đậm.", "rec": True, "preview": m({"D5": "a"}, SB), "ideas": ["I1", "I2"]},
   {"label": "Nền xám + vạch dọc trái", "desc": "Không bao giờ lẫn Hover; thêm một nét.", "preview": m({"D5": "b"}, SB), "ideas": ["I4", "I8"]},
   {"label": "Chỉ chữ + icon đậm, không nền", "desc": "Nhẹ nhất; khó thấy khi lướt.", "preview": m({"D5": "c"}, SB), "ideas": ["I5"]}],
  "untitled": m({"D5": "a"}, SB), "astryx": m({"D5": "a"}, SB)},
 {"id": "D6", "title": "Ô tìm trong menu (Search)",
  "why": "Phần kèm Search đã chốt. Header đã có ô tìm tính năng ⌘K (DEC-290 Header) — trùng chức năng nếu để cả hai.",
  "source": "variants/sidebar Phần kèm Search · DEC-290 (Header Navigation D2)",
  "options": [
   {"label": "Ô tìm đầy đủ đầu menu", "desc": "Như Untitled; trùng ô tìm ở header.", "preview": m({"D6": "a"}, SB), "ideas": ["I1"]},
   {"label": "Nút kính lúp cạnh logo, mở ⌘K", "desc": "Gọn; cùng một ô tìm với header.", "preview": m({"D6": "b"}, SB), "ideas": ["I5", "I6"]},
   {"label": "Bỏ — chỉ tìm ở header", "desc": "Một chỗ tìm duy nhất; Phần kèm Search chỉ dùng khi màn không có header.", "rec": True, "preview": m({"D6": "c"}, SB), "ideas": ["I3"]}],
  "untitled": m({"D6": "a"}, SB), "astryx": m({"D6": "c"}, SB), "astryxNote": "bản cũ: tìm ở header"},
 {"id": "D7", "title": "Thẻ nổi bật (Featured Card)",
  "why": "Phần kèm Featured Card đã chốt. Dùng cho cảnh báo vận hành (hạn đăng kiểm, hạn mức dầu) — không quảng cáo.",
  "source": "variants/sidebar Phần kèm Featured Card",
  "options": [
   {"label": "Thẻ xám nhạt, icon cảnh báo", "desc": "Hợp nền menu; không giành chú ý với nội dung.", "rec": True, "preview": m({"D7": "a"}, SB_FULL), "ideas": ["I1"]},
   {"label": "Thẻ vàng nhạt (cảnh báo)", "desc": "Nổi rõ; dễ thành “luôn vàng” khi luôn có xe sắp hạn.", "preview": m({"D7": "b"}, SB_FULL), "ideas": ["I8"]},
   {"label": "Không dùng mặc định", "desc": "Menu gọn; cảnh báo nằm ở chuông thông báo.", "preview": m({"D7": "c"}, SB_FULL), "ideas": ["I3"]}],
  "untitled": m({"D7": "a"}, SB_FULL), "astryx": m({"D7": "c"}, SB_FULL)},
 {"id": "D8", "title": "Slim 64: rê vào mục",
  "why": "Type Slim chỉ còn icon. Rê vào cần biết tên mục; mục có con (Phương tiện) cần chỗ chọn mục con.",
  "source": "variants/sidebar Type Slim",
  "options": [
   {"label": "Tooltip tên mục", "desc": "Đơn giản; mục có con phải mở rộng menu mới chọn được.", "preview": m({"D8": "a"}, SLIM_PV, 300), "ideas": ["I1", "I2"]},
   {"label": "Menu nổi có mục con", "desc": "Chọn được mục con ngay; thêm lớp nổi.", "rec": True, "preview": m({"D8": "b"}, SLIM_PV, 300), "ideas": ["I5", "I6"]}],
  "untitled": m({"D8": "a"}, SLIM_PV, 300), "astryx": m({"D8": "a"}, SLIM_PV, 300), "astryxNote": "bản cũ Width=64 6896:206354"},
]

ideas = [
 {"id": "I1", "source": "Untitled UI", "url": "https://www.untitledui.com/react/components/sidebar-navigations", "title": "Untitled UI — Sidebar navigations",
  "why": "Bộ đủ nhất: nhóm có nhãn hoặc vạch, Dual Tier, Slim, ô tìm, thẻ nổi bật, tài khoản chân.", "pv": SB},
 {"id": "I2", "source": "shadcn/ui", "url": "https://ui.shadcn.com/docs/components/sidebar", "title": "shadcn/ui — Sidebar",
  "why": "Mục cha thu gọn mũi tên phải, mục con thụt có đường dọc, thu về icon có tooltip.", "pv": SB_CH},
 {"id": "I3", "source": "Vercel", "url": "https://vercel.com/docs/dashboard-features", "title": "Vercel Dashboard",
  "why": "Nhãn nhóm chữ thường xám, ít trang trí; tìm ở thanh trên.", "pv": SB},
 {"id": "I4", "source": "Atlassian", "url": "https://atlassian.design/components/side-navigation/examples", "title": "Atlassian — Side navigation",
  "why": "Nhãn nhóm chữ hoa nhỏ, mục đang ở có vạch trái; mục con luôn mở.", "pv": SB},
 {"id": "I5", "source": "Linear", "url": "https://linear.app/docs/conceptual-model", "title": "Linear — menu trái",
  "why": "Kính lúp cạnh tên workspace mở ⌘K; số đếm Inbox màu nhấn; thu gọn có menu nổi.", "pv": SB},
 {"id": "I6", "source": "Notion", "url": "https://www.notion.com/help/navigate-with-the-sidebar", "title": "Notion — Sidebar",
  "why": "Mũi tên trái mở trang con, chấm cho cập nhật; rê vào khi thu gọn hiện menu nổi.", "pv": SB_CH},
 {"id": "I7", "source": "Stripe Dashboard", "url": "https://docs.stripe.com/dashboard/basics", "title": "Stripe Dashboard",
  "why": "Mục con chấm tròn, mục đang ở chấm đậm; nhóm cách nhau khoảng trắng.", "pv": SB_CH},
 {"id": "I8", "source": "Samsara", "url": "https://www.samsara.com/products/telematics/fleet-management", "title": "Samsara — phần mềm đội xe",
  "why": "Số cảnh báo màu nhấn trên mục, thẻ cảnh báo vận hành (bảo dưỡng, hạn giấy tờ) trong menu.", "pv": SB_FULL},
]
for i in ideas:
    i["preview"] = m(None, i.pop("pv"), 300)

REC = {d["id"]: chr(97 + next(k for k, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}
presets = [{"id": "rec", "label": "Đề xuất", "pick": REC},
           {"id": "untitled", "label": "Untitled UI", "pick": {"D1": "a", "D2": "a", "D3": "b", "D4": "a", "D5": "a", "D6": "a", "D7": "a", "D8": "a"}},
           {"id": "astryx", "label": "Bản hiện tại (DEC-288)", "pick": {"D1": "b", "D2": "a", "D3": "a", "D4": "b", "D5": "a", "D6": "c", "D7": "c", "D8": "a"}}]
for i in ideas:
    pk = {**REC}
    for d in decisions:
        for k, o in enumerate(d["options"]):
            if i["id"] in (o.get("ideas") or []):
                pk[d["id"]] = chr(97 + k)
    presets.append({"id": i["id"], "label": f'{i["id"]} · {i["source"]}', "pick": pk})

# ---------- màn ----------
ROWS = [("LVT-2026-0412", "Delta Logistics", "Cát Lái → Sóng Thần", "51C-482.19"), ("LVT-2026-0415", "Tân Cảng Logistics", "Cát Lái → Phnom Penh", "51C-517.03"),
        ("LVT-2026-0419", "An Phát Trading", "ICD Phước Long → Bình Dương", "51D-220.84"), ("LVT-2026-0421", "Delta Logistics", "Hiệp Phước → Long An", "61C-093.55")]
TABLE = ('<div class="tb"><table><tr><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Xe</th><th>Trạng thái</th></tr>'
         + "".join(f'<tr><td class="mono">{a}</td><td>{b}</td><td>{c}</td><td class="mono">{d}</td><td><span class="chip ok">Đang chạy</span></td></tr>' for a, b, c, d in ROWS)
         + "</table></div>")


def page_shell(sb, title, crumb, body=None, over="", tabs=""):
    """Thanh trên theo Header navigation đã chốt (DEC-291, DEC-293): cao 44, đường dẫn 14/20 (cha 400, hiện tại 500),
    nút kính lúp + chuông số đỏ + avatar 32. Tìm chỉ ở header (D6 C)."""
    return (f'<div class="shellw"><div data-live-sb style="display:flex">{sb}</div><div class="mainw"><div class="tb0">{crumb} / <b>{title}</b>'
            f'<span class="r"><span class="ib">{ic("search", 18)}</span><span class="ib">{ic("bell", 18)}<span class="rc">3</span></span>'
            f'<span class="av0" style="margin-left:4px">NA</span></span></div>'
            f'<div class="pt0">{title}</div>{tabs}<div class="pad">{TABLE if body is None else body}</div></div>{over}</div>')


DETAIL = ('<dl class="kv"><dt>Khách hàng</dt><dd>Delta Logistics</dd><dt>Tuyến</dt><dd>Cát Lái → Sóng Thần</dd>'
          '<dt>Xe · Lái xe</dt><dd><span class="mono">51C-482.19</span> · Trần Minh Khoa</dd><dt>Container</dt><dd class="mono">TGHU 482190-3 · 40HC</dd>'
          '<dt>Giờ lấy hàng</dt><dd>08:30 · 29/10/2026</dd><dt>Trạng thái</dt><dd><span class="chip ok">Đang chạy</span></dd></dl>')
TABS = '<div class="tabs0"><a class="on">Tổng quan</a><a>Chặng</a><a>Chi phí</a><a>Lịch sử</a></div>'
FORM = ('<div class="frm"><div class="f"><span class="lb">Khách hàng<span class="req">*</span></span><div class="ctl"><span class="v">Delta Logistics</span></div></div>'
        '<div class="row2"><div class="f"><span class="lb">Điểm lấy</span><div class="ctl"><span class="v">Cảng Cát Lái</span></div></div>'
        '<div class="f"><span class="lb">Điểm trả</span><div class="ctl"><span class="ph">Chọn điểm trả</span></div></div></div>'
        '<div class="f"><span class="lb">Ghi chú cho lái xe</span><div class="ctl" style="--h:72px;align-items:flex-start;padding-top:6px"><span class="ph">Nhập ghi chú</span></div></div>'
        '<div class="act"><span class="bt">Huỷ</span><span class="bt pri">Tạo lệnh</span></div></div>')
CONFIRM = ('<div class="scr" style="z-index:8"></div><div class="dlg0" role="dialog"><h4>Huỷ lệnh LVT-2026-0412?</h4>'
           '<p>Lái xe Trần Minh Khoa sẽ nhận thông báo huỷ. Chi phí đã ghi của chuyến vẫn giữ.</p>'
           '<div class="act"><span class="bt">Giữ lệnh</span><span class="bt dng">Huỷ lệnh</span></div></div>')


LONG = "Lệnh vận tải nội địa và quốc tế (kể cả tạm nhập tái xuất)"
S1 = page_shell(sidebar(live="Lệnh vận tải", long=LONG), "Lệnh vận tải", "Vận tải")
S2 = page_shell(sidebar("div", 240, feat=False, live="Lệnh vận tải", long=LONG), "Lệnh vận tải", "Vận tải")
S3 = page_shell(sidebar("dual", 312, live="Lệnh vận tải", long=LONG), "Lệnh vận tải", "Vận tải")
S4 = page_shell(sidebar(live="Lệnh vận tải", long=LONG), "LVT-2026-0412", "Vận tải / Lệnh vận tải", DETAIL, tabs=TABS)
S5 = page_shell(sidebar(live="Lệnh vận tải", long=LONG), "Tạo lệnh vận tải", "Vận tải / Lệnh vận tải", FORM)
S6 = page_shell(sidebar(live="Lệnh vận tải", long=LONG), "LVT-2026-0412", "Vận tải / Lệnh vận tải", DETAIL, over=CONFIRM, tabs=TABS)


def g():
    B = []
    B.append(vg_row("Type × Width", [("Sections Subheadings · 280", clip(sidebar(feat=False), 600)), ("Sections Dividers · 240", clip(sidebar("div", 240, feat=False), 600)),
                                     ("Dual Tier", clip(sidebar("dual", 312, feat=False), 600)), ("Slim · 64", clip(sidebar("slim", 64, feat=False), 600))], 4))
    ni = lambda **kw: f'<div class="sb" style="min-height:0;border:0;padding:4px;width:260px">{item(**kw)}</div>'
    B.append(vg_row("Nav item × State", [(f"{t} · {s}", ni(icon="file", label="Lệnh vận tải", n=12 if t == "Badge" else None,
                                                           children=["Đầu kéo"] if t == "Collapsible" else None, open_=False,
                                                           cur=s == "Current", st={"Hover": "is-hover", "Focus": "is-focus"}.get(s, "")))
                                         for t in ("Link", "Collapsible", "Badge") for s in ("Default", "Hover", "Current", "Focus")], 4))
    B.append(vg_row("Child", [("Mở, mục con đang ở", clip(f'<div class="sb" style="min-height:0;border:0;width:260px">{item("truck", "Phương tiện", None, ["Đầu kéo", "Rơ moóc", "Xe tải"], cur="child")}</div>', 170)),
                              ("Thu gọn", f'<div class="sb" style="min-height:0;border:0;width:260px">{item("truck", "Phương tiện", None, ["Đầu kéo"], open_=False)}</div>')], 2))
    B.append(vg_row("Phần kèm", [("Logo + Tenant Switch", f'<div class="sb" style="min-height:0;width:280px">{head()}</div>'),
                                 ("Search — ẩn khi D6 chọn C", f'<div class="sb" style="min-height:0;width:280px">{SEARCH}</div>'),
                                 ("Featured Card", f'<div class="sb" style="min-height:0;width:280px">{FEAT}</div>'),
                                 ("Phạm vi + Account (DEC-288)", f'<div class="sb" style="min-height:0;width:280px">{SCOPE}{ACC}</div>')], 4))
    B.append(vg_row("Chữ dài — 1 dòng, cắt …", [("Tên mục dài", f'<div class="sb" style="min-height:0;width:280px">{item("file", LONG, 12)}</div>'),
                                                 ("Chi nhánh dài", f'<div class="sb" style="min-height:0;width:280px">{head().replace("Chi nhánh Hồ Chí Minh", "Chi nhánh Bà Rịa – Vũng Tàu (Cảng Cái Mép – Thị Vải)")}</div>')], 2, "DEC-261"))
    return vg(B)


screens = [
 {"id": "sub-web", "name": "Sections Subheadings · 280", "device": "web", "shell": "none",
  "note": "Bản có nhãn nhóm (sub heading). Bấm nút ▢ đầu menu để thu về Slim 64; mục Lệnh vận tải nhận Hover / Focus / Chữ dài ở Bảng chọn.", "html": S1},
 {"id": "div-web", "name": "Sections Dividers · 240", "device": "web", "shell": "none", "note": "Bản vạch ngăn, rộng 240.", "html": S2},
 {"id": "dual-web", "name": "Dual Tier", "device": "web", "shell": "none", "note": "Cột module 64 + cột trang của module.", "html": S3},
 {"id": "detail-web", "name": "Chi tiết · Lệnh vận tải", "device": "web", "shell": "none", "note": "Màn chi tiết; mục đang ở vẫn là Lệnh vận tải (cha của trang).", "html": S4},
 {"id": "form-web", "name": "Form · Tạo lệnh", "device": "web", "shell": "none", "note": "Form hẹp 560 cạnh menu 280.", "html": S5},
 {"id": "confirm-web", "name": "Hộp thoại xác nhận", "device": "web", "shell": "none", "note": "Lớp phủ che cả menu trái.", "html": S6},
]

# ---------- vòng 2: preview khoá theo tổ hợp đã chốt (answers.json, DEC-295) ----------
PICK = {"D1": "b", "D2": "a", "D3": "a", "D4": "b", "D5": "a", "D6": "c", "D7": "c", "D8": "b"}
MOB = ('<div class="mweb"><div class="mtb"><span class="bt ghost ic-only">' + ic("menu", 20) + '</span>Lệnh vận tải</div>'
       '<div class="scr"></div>' + sidebar(feat=False).replace('style="--sbw:280px"', 'style="--sbw:300px"', 1) + "</div>")
preview = {
 "version": 1, "pick": PICK,
 "changes": "Bản 28/10 theo tổ hợp chốt: nhãn nhóm chữ hoa, mũi tên phải, mục con thụt + đường dọc, số đếm xanh dương, "
            "mục đang ở nền xám chữ đậm, không ô tìm trong menu (tìm ở header), không thẻ nổi bật; Slim 64 rê vào mục có con "
            "mở menu nổi, mục khác hiện tooltip (DEC-295). Thanh trên của màn demo theo Header nav (DEC-291, DEC-293). "
            "Thêm màn chi tiết, form, hộp thoại xác nhận.",
 "blocks": [
  {"title": "Web", "platform": "web", "note": "Type × Width · Nav item × State · Child · Phần kèm · chữ dài — khoá theo tổ hợp", "html": m(PICK, g(), 1280)},
  {"title": "Mobile web (< 768)", "platform": "mobile", "note": "Khung 393 · nút menu ở thanh trên mở menu dạng ngăn kéo 300 trên lớp phủ; app dùng tab Tài khoản (DEC-288)",
   "frames": [m(PICK, MOB, 393)]},
 ]}

page = {
 "component": "Sidebar Navigation", "slug": "sidebar-navigation-r2", "title": "Sidebar Navigation Review (làm lại)",
 "subtitle": "Application component · vòng 2 Preview — biến thể đã chốt: Type 4 · Width 280/240 · Nav item 4 · State 4 · Phần kèm 5. Phạm vi làm việc giữ theo DEC-288/289. Chỉ web (app dùng tab Tài khoản, DEC-288).",
 "round": "preview", "preview": preview,
 "refs": {
  "untitled": {"summary": "4 kiểu: nhóm có nhãn, nhóm vạch ngăn, Dual Tier (cột module + cột trang), Slim 64; mục 40 bo 6, đang ở nền xám; ô tìm, thẻ nổi bật, tài khoản ở chân.",
               "source": "untitledui.com/react/components/sidebar-navigations · design/_ref/untitled-ui/react/components/application/"},
  "astryx": {"summary": "Bản đã lên Figma 28/10: nhãn nhóm chữ hoa, đang ở nền xám chữ đậm, số đếm xanh dương, thẻ phạm vi chân menu + hộp thoại 3 cột (DEC-288, DEC-289).",
             "source": "design-system/components/application/sidebar-navigation.md · _work/sidebar-navigation/"},
  "usage": ["Mọi màn web trong module (CMP-11): vận tải, điều phối, bảo dưỡng, quản lý dầu, tài chính", "Đổi chi nhánh · module · cơ sở qua thẻ phạm vi (DEC-288)"],
  "platform": "Chỉ web (variants/sidebar mobile “web”). App: tab Tài khoản (DEC-288 D7)."},
 "css": CSS + CSS_SB, "cssScreen": SHELL,
 "states": [{"key": "default", "label": "Mặc định"}, {"key": "slim", "label": "Thu gọn 64"}, {"key": "hover", "label": "Hover mục"},
            {"key": "focus", "label": "Focus mục"}, {"key": "long", "label": "Chữ dài"}],
 "ideas": ideas, "decisions": decisions, "presets": presets, "screens": screens,
 "proto": [{"sel": ".clp,[data-live-sb] .lg", "state": "slim", "toggle": True}],
 "protoHint": "bấm nút ▢ đầu menu để thu gọn / mở lại",
}

# page.json đã sửa thẳng sau build (tách css/cssScreen, khai values, kit) — chạy lại build sẽ xoá hết
import json  # noqa: E402
if OUT.exists() and "values" in json.loads(OUT.read_text()) and "--force" not in sys.argv:
    sys.exit("page.json đã có chỉnh sửa sau build (values, cssScreen, kit). Sửa thẳng page.json; ghi đè thì thêm --force.")
write(OUT, page, decisions, brief=False)
