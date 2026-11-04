"""Bộ dựng chung cho 5 component Application khung nội dung (vòng 1 Brainstorm, 04/11):
Tabs · Card header · Section header · Empty state · Command menu — mỗi component một trang `_work/{slug}/`.

Luật (user 04/11): mọi số đo / màu / chữ đi qua token foundation đã chốt trong design-system/tokens.css
(type/* theo vai — Cal Sans 400 cho tiêu đề ≥ 18, Inter 600 heading, 500 label; radius control 8 · card 12 · overlay 20 ·
menu 10 · menu-item 6 · badge 6; control web 28/32/36/40 · app 36/42/52; icon 12/14/16/20; featured icon 40/48/56;
shadow xs…xl; duration/easing). Không mã màu trần.

CSS mỗi component chia hai lớp:
  CSS_<X>  = hình theo phương án ĐỀ XUẤT (trang khác dùng component này làm ngữ cảnh sẽ thấy đúng bản đề xuất)
  OPT_<X>  = luật đổi theo điểm cần quyết D1…Dn của trang <X> (chỉ trang <X> nạp)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "_forms"))
from kit import P, ic, mini, mshow_css, vg, vg_row  # noqa: E402,F401
from pvkit import tok_css_nested  # noqa: E402

P.update({
    "inbox": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.5 5.1L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.5-6.9A2 2 0 0 0 16.8 4H7.2a2 2 0 0 0-1.7 1.1z"/>',
    "file": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M9 13h6M9 17h4"/>',
    "alert": '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/>',
    "refresh": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "arrowr": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrowl": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "chevl": '<path d="M15 6l-6 6 6 6"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "wifioff": '<path d="M2 2l20 20M8.5 16.5a5 5 0 0 1 7 0M5 13a10 10 0 0 1 5.2-2.8M19 13a10 10 0 0 0-2.3-1.7M2 8.8a15 15 0 0 1 4.2-2.7M22 8.8A15 15 0 0 0 11 5"/><path d="M12 20h.01"/>',
    "checkc": '<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21c1-4 3.5-6 7-6s6 2 7 6M16 4a4 4 0 0 1 0 8M22 21c-.5-2.5-1.8-4.3-3.5-5.2"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    "ret": '<path d="M9 10l-5 5 5 5"/><path d="M20 4v7a4 4 0 0 1-4 4H4"/>',
    "spin": '<path d="M21 12a9 9 0 1 1-6.2-8.6"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "fuel": '<path d="M3 22h12M4 9h10M14 22V4a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v18"/><path d="M14 13h2a2 2 0 0 1 2 2v2a2 2 0 0 0 4 0V9l-3-3"/>',
})

ACTIVE = set()  # component đang review trên trang — gắn data-cmp (Góp ý trỏ đúng phần)


def cm(name):
    return " data-cmp" if name in ACTIVE else ""


# ---------- phần nhỏ dùng chung (hình đề xuất của component Base đã/đang dựng) ----------
def lt(normal, long):
    return f'<span class="nl">{normal}</span><span data-show="state:long">{long}</span>'


def bt(label, kind="sec", icon=None, js=None, size=""):
    i = ic(icon, 14 if size == "sm" else 16) if icon else ""
    j = f' data-js="{js}"' if js else ""
    return f'<button class="bt {kind} {size}"{j}>{i}<span class="tx">{label}</span></button>'


def ibt(icon, label, kind="ter", js=None, size=""):
    j = f' data-js="{js}"' if js else ""
    return f'<button class="bt io {kind} {size}" aria-label="{label}"{j}>{ic(icon, 14 if size == "sm" else 16)}</button>'


TONE = {"Đang chạy": "green", "Sẵn sàng": "green", "Hoàn tất": "gray", "Đã giao": "green", "Chờ xe": "yellow", "Chờ ký": "yellow",
        "1 chờ ký": "yellow", "Trễ hẹn": "red", "Bảo dưỡng": "yellow", "Nháp": "gray", "Mới": "blue"}


def pill(t, tone=None):
    tone = tone or TONE.get(t, "gray")
    return f'<span class="pill t-{tone}"><i></i>{t}</span>'


def cnt(n):
    return f'<span class="cntb">{n}</span>'


def kbd(k):
    return f'<span class="kbd">{k}</span>'


AV = [("TB", "blue"), ("LH", "red"), ("PD", "green"), ("NK", "purple"), ("VT", "orange")]


def av(i, cls=""):
    t, tone = AV[i % len(AV)]
    return f'<span class="av t-{tone} {cls}">{t}</span>'


def sk(w="60%", h="sm"):
    return f'<span class="sk {h}" style="width:{w}"></span>'


# ---------- dữ liệu mẫu cố định ----------
ORDERS = [("LVT-2026-0412", "Delta Logistics", "Cát Lái → Sóng Thần", "Trần Văn Bình", "Đang chạy"),
          ("LVT-2026-0415", "Tân Cảng Logistics", "Cát Lái → Phnom Penh", "Lê Thị Hoa", "Chờ xe"),
          ("LVT-2026-0419", "An Phát Trading", "ICD Phước Long → Bình Dương", "Phạm Quốc Dũng", "Trễ hẹn"),
          ("LVT-2026-0421", "Delta Logistics", "Hiệp Phước → Long An", "Nguyễn Minh Khoa", "Đang chạy"),
          ("LVT-2026-0423", "Minh Long Food", "Cát Lái → Tân Uyên", "Võ Thành Tâm", "Hoàn tất")]
DOCS = [("Phiếu giao nhận container (EIR)", "Cảng Cát Lái · 08:12"), ("Biên bản giao hàng", "Chờ khách ký"),
        ("Hoá đơn cầu đường", "VETC · 3 trạm"), ("Ảnh niêm phong", "2 ảnh · lái xe gửi")]


def table(rows=ORDERS, hide="empty nores error noperm offline loading"):
    h = f' data-hide="{hide}"' if hide else ""
    return (f'<div class="tw"{h}><table class="tbl"><tr><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Lái xe</th><th>Trạng thái</th></tr>'
            + "".join(f'<tr><td class="code">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{pill(s)}</td></tr>' for a, b, c, d, s in rows)
            + "</table></div>")


def table_loading():
    return ('<div class="tw" data-show="state:loading"><table class="tbl"><tr><th>Mã lệnh</th><th>Khách hàng</th><th>Tuyến</th><th>Lái xe</th><th>Trạng thái</th></tr>'
            + "".join(f'<tr><td>{sk("70%")}</td><td>{sk("60%")}</td><td>{sk("80%")}</td><td>{sk("55%")}</td><td>{sk("50%")}</td></tr>' for _ in range(4))
            + "</table></div>")


def kv(pairs):
    return '<dl class="kv">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in pairs) + "</dl>"


def doc_list(docs=DOCS):
    return "".join(f'<div class="doc"><span class="di">{ic("file", 16)}</span><span class="dn"><b>{a}</b><small>{b}</small></span>{ibt("dl", "Tải " + a)}</div>' for a, b in docs)


def mcard(code, route, sub, st):
    return (f'<div class="mcard"><div class="mc1"><b class="code">{code}</b>{pill(st)}</div>'
            f'<span class="mc2">{route}</span><span class="mc3">{sub}</span></div>')


# ======================================================================
# TABS
# ======================================================================
def tabs(items, sel=0, size="sm", kind="line", js=None, st=None, ovf=None, full=False, icons=False, aria="Trạng thái", icon_only=False):
    """items: [(nhãn, số đếm|None, icon|None)] · kind: line | seg | vert · ovf: số tab hiện khi gom “Thêm” (D6 B)."""
    st = st or {}
    out = []
    for k, it in enumerate(items):
        lab, n = it[0], it[1]
        icn = it[2] if len(it) > 2 else None
        ii = f'<span class="ti">{ic(icn, 16)}</span>' if icn else ""
        c = cnt(n) if n is not None else ""
        j = f' data-js="{js[k]}"' if js and k < len(js) and js[k] else ""
        cls = "tab" + (" io" if icon_only else "") + (" on" if k == sel else "") + (f" {st[k]}" if k in st else "") + (" ovx" if ovf is not None and k >= ovf else "")
        dis = " disabled" if "is-dis" in st.get(k, "") else ""
        lb = f'<span class="sr">{lab}</span>' if icon_only else f'<span class="tl">{lab}</span>'
        tt = f' title="{lab}"' if icon_only else ""
        out.append(f'<button class="{cls}" role="tab" aria-selected="{str(k == sel).lower()}"{tt}{j}{dis}>{ii}{lb}{c}</button>')
    more = ""
    if ovf is not None:
        rest = len(items) - ovf
        PICK = ' data-js="tpick"'
        menu = "".join(f'<button class="tmi" role="menuitem"{PICK if k == ovf else ""}><span>{it[0]}</span>{cnt(it[1]) if it[1] is not None else ""}</button>'
                       for k, it in enumerate(items) if k >= ovf)
        more = (f'<span class="tfadel"></span>{ibt("chevl", "Tab trước", "sec", js="tprev", size="sm").replace("bt io", "bt io tnavl")}'
                f'<span class="tfade"></span>{ibt("chevr", "Tab tiếp", "sec", js="tnext", size="sm").replace("bt io", "bt io tnav")}'
                f'<button class="tab tmore" data-js="tmore" aria-haspopup="menu"><span class="tl">Thêm</span>{cnt(rest)}{ic("chev", 14)}</button>'
                f'<div class="tmenu" role="menu" aria-label="Tab khác">{menu}</div>')
    lab, n = items[sel][0], items[sel][1]
    sel_html = f'<div class="tsel"><span>{lab}{f" · {n}" if n is not None else ""}</span>{ic("chev", 16)}</div>'
    w = "tbw" + (" ovf" if ovf is not None else "") + (" wi" if icons else "") + (f" k-{kind}")
    return (f'<div class="{w}"{cm("tabs")}><div class="tbs {kind} t-{size}{" full" if full else ""}" role="tablist" aria-label="{aria}">'
            f'{"".join(out)}</div>{more}{sel_html}</div>')


CSS_TABS = r"""
.tbw{min-width:0;position:relative;display:flex;align-items:flex-end}
.tbs{display:flex;min-width:0;position:relative;overflow-x:auto;scrollbar-width:none;flex:1}
.tbs::-webkit-scrollbar{display:none}
.tab{border:0;background:none;display:inline-flex;align-items:center;gap:var(--space-md);flex:none;position:relative;cursor:pointer;
 font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-tertiary);white-space:nowrap;
 transition:color var(--duration-fast) var(--easing-standard),background var(--duration-fast) var(--easing-standard),border-color var(--duration-fast) var(--easing-standard)}
.tab .ti{display:none;color:inherit}
.tbw.wi .tab .ti{display:inline-flex}
.tab.io .ti{display:inline-flex}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.tbs.seg .tab.io{width:var(--control-height-sm);padding:0;justify-content:center}
.tbs.line .tab.io{padding-left:var(--space-xs);padding-right:var(--space-xs)}
.tab:hover,.tab.is-hover{color:var(--color-text-secondary)}
.tab.on{color:var(--color-text-primary)}
.tab.is-focus{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:calc(-1 * var(--focus-width));border-radius:var(--radius-xs)}
.tab.is-dis,.tab[disabled]{color:var(--color-text-disabled);cursor:not-allowed}
.cntb{display:inline-flex;align-items:center;height:var(--chip-height-sm);padding:0 var(--space-md);border-radius:var(--radius-full);
 background:var(--color-bg-tertiary);color:var(--color-text-secondary);font:400 var(--chip-count-font-size)/var(--chip-count-line-height) var(--font-body);font-variant-numeric:tabular-nums}
.tab.on .cntb{background:var(--color-bg-selected);color:var(--color-text-primary)}
/* line (Underline) — web */
.tbs.line{gap:var(--space-lg)}
.tbs.line::after{content:"";position:sticky;left:0;right:0}
.tbw.k-line::before{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--color-border-secondary)}
.tbs.line .tab{padding:0 var(--space-xxs) var(--space-md);border-bottom:var(--focus-width) solid transparent}
.tbs.line .tab.on{border-bottom-color:var(--color-fg-primary)}
.tbs.line.t-md .tab{font:500 var(--type-body-lg-size)/var(--type-body-lg-line-height) var(--font-body)}
.tbs.line.full{width:100%}.tbs.line.full .tab{flex:1;justify-content:center}
/* seg (Button border) — chuyển chế độ xem */
.tbw.k-seg{display:inline-flex;max-width:100%}
.tbs.seg{display:inline-flex;flex:none;gap:var(--space-xs);padding:var(--space-xs);border-radius:var(--radius-lg);background:var(--color-bg-secondary_alt);box-shadow:inset 0 0 0 1px var(--color-border-secondary)}
.tbs.seg .tab{height:var(--control-height-sm);padding:0 var(--tab-padding-x);border-radius:var(--radius-control)}
.tbs.seg.t-md .tab{height:var(--control-height-md);padding:0 var(--control-padding-x-md)}
.tbs.seg .tab.on{background:var(--color-bg-primary_alt);box-shadow:var(--shadow-sm)}
.tbs.seg.full{display:flex;flex:1}.tbw.k-seg:has(.full){display:flex}.tbs.seg.full .tab{flex:1;justify-content:center}
/* vert (Line dọc) */
.tbw.k-vert{display:block}
.tbs.vert{flex-direction:column;gap:var(--space-md);overflow:visible}
.tbs.vert .tab{padding:var(--space-xxs) var(--space-lg) var(--space-xxs) var(--space-md);border-left:var(--focus-width) solid transparent;justify-content:flex-start}
.tbs.vert .tab.on{border-left-color:var(--color-fg-primary)}
.tbs.vert .tab .cntb{margin-left:auto}
/* tràn ngang — đề xuất: cuộn + mép mờ + nút › */
.tfade{position:absolute;right:var(--control-height-sm);top:0;bottom:1px;width:var(--space-6xl);pointer-events:none;background:linear-gradient(to right,transparent,var(--color-bg-primary))}
.tnav{position:absolute;right:0;top:calc(50% - var(--control-height-sm) / 2 - var(--space-xs))}
.tbw.ovf .tbs{padding-right:calc(var(--control-height-sm) + var(--space-6xl))}
.tmore{display:none!important}
.tbw.ovf{z-index:5}
.tfadel{display:none;position:absolute;left:var(--control-height-sm);top:0;bottom:1px;width:var(--space-6xl);pointer-events:none;background:linear-gradient(to left,transparent,var(--color-bg-primary))}
.tnavl{display:none!important;position:absolute;left:0;top:calc(50% - var(--control-height-sm) / 2 - var(--space-xs))}
.tmenu{display:none;position:absolute;right:0;top:calc(100% + var(--space-xs));z-index:20;min-width:calc(var(--width-xxs) * .7);padding:var(--space-xs);background:var(--color-bg-primary_alt);border-radius:var(--radius-menu);box-shadow:var(--shadow-lg),0 0 0 1px var(--shadow-lg-border)}
.tmi{display:flex;align-items:center;justify-content:space-between;gap:var(--space-md);width:100%;min-height:var(--control-height-ml);padding:0 var(--space-md);border:0;background:none;border-radius:var(--radius-menu-item);font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-secondary);cursor:pointer;text-align:left}
.tmi:hover,.tmi:first-child{background:var(--color-bg-primary_hover);color:var(--color-text-primary)}
/* đã bấm › (đề xuất D6 A, cả C): cuộn tới cuối — 5 tab đầu ra khỏi khung, hiện ‹ + mép mờ trái */
.pv[data-state=scrolled] .tbw.ovf .tbs .tab:not(.ovx){display:none}
.pv[data-state=scrolled] .tbw.ovf .tfade,.pv[data-state=scrolled] .tbw.ovf .tnav{display:none}
.pv[data-state=scrolled] .tbw.ovf .tfadel{display:block}
.pv[data-state=scrolled] .tbw.ovf .tnavl{display:inline-flex!important}
.pv[data-state=scrolled] .tbw.ovf .tbs{padding-left:calc(var(--control-height-sm) + var(--space-6xl));padding-right:0}
.tsel{display:none}
/* app — đề xuất: chip cuộn ngang (Lab DEC-096) */
.pv[data-platform=mobile] .tbw.k-line::before{display:none}
.pv[data-platform=mobile] .tbs.line{gap:var(--space-md);margin:0 calc(-1 * var(--container-padding-mobile));padding:0 var(--container-padding-mobile)}
.pv[data-platform=mobile] .tbs.line .tab{height:var(--control-height-sm);padding:0 var(--control-padding-x-sm);border:1px solid var(--color-border-primary);border-radius:var(--radius-full);color:var(--color-text-secondary)}
.pv[data-platform=mobile] .tbs.line .tab::after{content:"";position:absolute;left:0;right:0;top:calc((var(--control-height-sm) - var(--touch-min)) / 2);height:var(--touch-min)}
.pv[data-platform=mobile] .tbs.line .tab.on{background:var(--color-accent-solid);border-color:var(--color-accent-solid);color:var(--color-text-inverse)}
.pv[data-platform=mobile] .tbs.line .tab.on .cntb{background:var(--color-bg-primary);color:var(--color-text-primary)}
.pv[data-platform=mobile] .tbs.line .tab.on .ti{color:inherit}
.pv[data-platform=mobile] .tfade,.pv[data-platform=mobile] .tnav{display:none}
.pv[data-platform=mobile] .tbw.ovf .tbs{padding-right:var(--container-padding-mobile)}
.pv[data-platform=mobile] .tbs.seg .tab{height:var(--control-height-sm)}
"""

OPT_TABS = r"""
/* D1 kiểu chính web: a Underline · b Button gray · c Button border */
.pv:not([data-platform=mobile])[data-D1=b] .tbw.k-line::before{display:none}
.pv:not([data-platform=mobile])[data-D1=b] .tbs.line{gap:var(--space-xs)}
.pv:not([data-platform=mobile])[data-D1=b] .tbs.line .tab{height:var(--control-height-ml);padding:0 var(--tab-padding-x);border:0;border-radius:var(--radius-control)}
.pv:not([data-platform=mobile])[data-D1=b] .tbs.line .tab.on,.pv:not([data-platform=mobile])[data-D1=b] .tbs.line .tab.is-hover{background:var(--color-bg-primary_hover)}
.pv:not([data-platform=mobile])[data-D1=c] .tbw.k-line::before{display:none}
.pv:not([data-platform=mobile])[data-D1=c] .tbs.line{flex:none;gap:var(--space-xs);padding:var(--space-xs);border-radius:var(--radius-lg);background:var(--color-bg-secondary_alt);box-shadow:inset 0 0 0 1px var(--color-border-secondary)}
.pv:not([data-platform=mobile])[data-D1=c] .tbs.line .tab{height:var(--control-height-sm);padding:0 var(--tab-padding-x);border:0;border-radius:var(--radius-control)}
.pv:not([data-platform=mobile])[data-D1=c] .tbs.line .tab.on{background:var(--color-bg-primary_alt);box-shadow:var(--shadow-sm)}
/* D2 kiểu phụ (chuyển chế độ xem): a Button border · b Button minimal · c dùng Underline SM */
.pv[data-D2=b] .tbs.seg{background:var(--color-bg-secondary_alt);gap:var(--space-xxs);padding:0;box-shadow:inset 0 0 0 1px var(--color-border-secondary)}
.pv[data-D2=b] .tbs.seg .tab.on{background:var(--color-bg-primary_alt);box-shadow:var(--shadow-xs),inset 0 0 0 1px var(--color-border-primary)}
.pv[data-D2=c] .tbs.seg{background:none;box-shadow:none;padding:0;gap:var(--space-lg);border-radius:0}
.pv[data-D2=c] .tbs.seg .tab{height:auto;padding:0 var(--space-xxs) var(--space-md);border-radius:0;border-bottom:var(--focus-width) solid transparent}
.pv[data-D2=c] .tbs.seg .tab.on{background:none;box-shadow:none;border-bottom-color:var(--color-fg-primary)}
/* D3 số đếm: a viên xám · b chữ thường */
.pv[data-D3=b] .cntb{background:none!important;padding:0;height:auto;color:var(--color-text-tertiary)}
.pv[data-D3=b] .tab.on .cntb{color:var(--color-text-secondary)}
.pv[data-platform=mobile][data-D3=b] .tbs.line .tab.on .cntb{color:inherit}
/* D4 icon trước nhãn: a không · b có */
.pv[data-D4=b] .tab .ti{display:inline-flex}
/* D5 cỡ: a SM + MD · b chỉ SM */
.pv[data-D5=b] .tbs.line.t-md .tab{font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body)}
.pv[data-D5=b] .tbs.seg.t-md .tab{height:var(--control-height-sm);padding:0 var(--tab-padding-x)}
/* D6 tràn ngang: a cuộn + mép mờ + › · b gom “Thêm” · c cuộn trơn */
.pv[data-D6=b] .tbw.ovf .tab.ovx,.pv[data-D6=b] .tbw.ovf .tfade,.pv[data-D6=b] .tbw.ovf .tnav,.pv[data-D6=c] .tbw.ovf .tfade,.pv[data-D6=c] .tbw.ovf .tnav{display:none!important}
.pv[data-D6=b] .tbw.ovf .tmore,.pv[data-D6=b] .tbw.ovf .tmore{display:inline-flex!important}
.pv:not([data-platform=mobile])[data-D6=b] .tbw.ovf .tbs{padding-right:0;flex:none}
.pv:not([data-platform=mobile])[data-D6=b] .tbw.ovf .tmore{padding:0 var(--space-xxs) var(--space-md);border-bottom:var(--focus-width) solid transparent}
.pv:not([data-platform=mobile])[data-D6=c] .tbw.ovf .tbs{padding-right:0}
.pv[data-platform=mobile][data-D6=b] .tbw.ovf .tmore{display:none!important}
.pv[data-D6=b][data-state=more] .tbw.ovf .tmenu{display:block}
.pv[data-D6=b][data-state=more] .tbw.ovf .tmore{color:var(--color-text-primary)}
.pv[data-D6=b][data-state=more] .tbw.ovf .tmore svg:last-child{transform:rotate(180deg)}
.pv[data-D6=b][data-state=scrolled] .tbw.ovf .tbs .tab:not(.ovx){display:inline-flex}
.pv[data-D6=b][data-state=scrolled] .tbw.ovf .tfadel,.pv[data-D6=b][data-state=scrolled] .tbw.ovf .tnavl,.pv[data-D6=c][data-state=scrolled] .tbw.ovf .tfadel,.pv[data-D6=c][data-state=scrolled] .tbw.ovf .tnavl{display:none!important}
.pv[data-D6=b][data-state=scrolled] .tbw.ovf .tbs,.pv[data-D6=c][data-state=scrolled] .tbw.ovf .tbs{padding-left:0}
/* D7 app: a Underline cuộn · b Chip (đề xuất) · c ô Select */
.pv[data-platform=mobile][data-D7=a] .tbw.k-line::before{display:block}
.pv[data-platform=mobile][data-D7=a] .tbs.line{gap:var(--space-2xl)}
.pv[data-platform=mobile][data-D7=a] .tbs.line .tab{height:auto;padding:0 var(--space-xxs) var(--space-md);border:0;border-bottom:var(--focus-width) solid transparent;border-radius:0;color:var(--color-text-tertiary)}
.pv[data-platform=mobile][data-D7=a] .tbs.line .tab.on{background:none;color:var(--color-text-primary);border-bottom-color:var(--color-fg-primary)}
.pv[data-platform=mobile][data-D7=a] .tbs.line .tab.on .cntb{background:var(--color-bg-selected)}
.pv[data-platform=mobile][data-D7=c] .tbw.k-line .tbs{display:none}
.pv[data-platform=mobile][data-D7=c] .tbw.k-line .tsel{display:flex;flex:1;align-items:center;justify-content:space-between;height:var(--control-height-md);padding:0 var(--control-padding-x-md);
 border:1px solid var(--color-border-primary);border-radius:var(--radius-field);background:var(--color-bg-primary);font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body)}
.pv[data-platform=mobile][data-D7=c] .tbw.k-line::before{display:none}
/* D8 Tabs dọc: a Line · b Button gray */
.pv[data-D8=b] .tbs.vert{gap:var(--space-xxs)}
.pv[data-D8=b] .tbs.vert .tab{height:var(--control-height-ml);padding:0 var(--space-lg);border-left:0;border-radius:var(--radius-control)}
.pv[data-D8=b] .tbs.vert .tab.on{background:var(--color-bg-primary_hover)}
"""


# ======================================================================
# CARD HEADER
# ======================================================================
def card_header(title, badge="", sub="", lead=None, acts=None, primary=("Sửa", "edit"), link="Xem tất cả", collapse=False, count=None):
    """lead: ('fi', icon) | ('av', i) · acts: None = 3 kiểu theo D2 (nút + ⋯ / ⋯ / liên kết) · chuỗi = hành động cố định."""
    ld = ""
    if lead and lead[0] == "fi":
        ld = f'<span class="ch-ld fi f40"><span class="fii">{ic(lead[1], 20)}</span><span class="fib">{ic(lead[1], 20)}</span></span>'
    elif lead and lead[0] == "av":
        ld = f'<span class="ch-ld">{av(lead[1], "a40")}</span>'
    n = (f'<span class="ch-nb">{cnt(count)}</span><span class="ch-nt">· {count}</span>') if count is not None else ""
    if acts is None:
        a = (f'<div class="act act-a">{bt(primary[0], "sec", primary[1], size="sm")}{ibt("more", "Thêm thao tác", size="sm")}</div>'
             f'<div class="act act-b">{ibt("more", "Thêm thao tác", size="sm")}</div>'
             f'<div class="act act-c"><a class="lnk">{link}{ic("arrowr", 14)}</a></div>'
             f'<div class="act act-m"><a class="lnk">{link if link != "Xem tất cả" else primary[0]}</a></div>')
    else:
        a = f'<div class="act fix">{acts}</div>'
    col = ""
    if collapse:
        col = ibt("chev", "Thu gọn", size="sm").replace("bt io", "bt io ch-col")
    coll = ibt("chev", "Thu gọn", size="sm").replace("bt io", "bt io ch-coll") if collapse else ""
    s = f'<p class="ch-s">{sub}</p>' if sub else ""
    return (f'<div class="chd"{cm("card-header")}>{coll}{ld}<div class="ch-m"><div class="ch-t"><h3>{title}</h3>{n}{badge}</div>{s}</div>'
            f'{a}{col}</div><div class="ch-dv"></div>')


def card(header, body, cls=""):
    return f'<div class="cc {cls}">{header}<div class="cc-b">{body}</div></div>'


CSS_CH = r"""
.cc{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);background:var(--color-bg-primary);min-width:0;box-shadow:var(--shadow-xs)}
.cc-b{padding:var(--space-2xl) var(--space-3xl) var(--space-3xl);display:flex;flex-direction:column;gap:var(--space-lg)}
.cc.tbl .cc-b{padding:0}
.chd{display:flex;gap:var(--space-xl);align-items:flex-start;padding:var(--space-2xl) var(--space-3xl)}
.ch-m{flex:1;min-width:0;display:flex;flex-direction:column;gap:var(--space-xs)}
.ch-t{display:flex;align-items:center;gap:var(--space-md);min-width:0}
.ch-t h3{margin:0;font:400 var(--type-title-3-size)/var(--type-title-3-line-height) var(--font-title);font-synthesis:none;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.pv[data-state=long] .ch-t h3{white-space:normal}
.ch-s{margin:0;color:var(--color-text-tertiary);font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.ch-ld{flex:none;display:inline-flex}
.ch-nt{display:none;color:var(--color-text-tertiary);font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.act{display:none;gap:var(--space-md);align-items:center;flex:none}
.act-a,.act.fix{display:flex}
.ch-dv{height:1px;background:var(--color-border-secondary)}
.ch-col,.ch-coll{flex:none}.ch-coll{display:none!important}
.ch-col svg,.ch-coll svg{transition:transform var(--duration-medium) var(--easing-standard)}
.pv[data-state=collapsed] .cc.clp .cc-b,.pv[data-state=collapsed] .cc.clp .ch-dv{display:none}
.pv[data-state=collapsed] .cc.clp .ch-col svg,.pv[data-state=collapsed] .cc.clp .ch-coll svg{transform:rotate(-90deg)}
.pv[data-state=loading] [data-live] .act .bt{opacity:.5;pointer-events:none}
/* app — đề xuất: giữ phụ đề, hành động vào ⋯ */
.pv[data-platform=mobile] .chd{padding:var(--layout-card-padding);gap:var(--space-lg)}
.pv[data-platform=mobile] .cc-b{padding:var(--space-lg) var(--layout-card-padding) var(--layout-card-padding)}
.pv[data-platform=mobile] .cc.tbl .cc-b{padding:0}
.pv[data-platform=mobile] .act{display:none!important}
.pv[data-platform=mobile] .act-b{display:flex!important}
.pv[data-platform=mobile] .act .bt.io{width:var(--touch-min);height:var(--touch-min);margin:calc(var(--space-md) * -1) calc(var(--space-lg) * -1) calc(var(--space-md) * -1) 0}
"""

OPT_CH = r"""
/* D1 cấu tạo: a đầy đủ · b gọn (tiêu đề heading 14, không phụ đề, không gạch) */
.pv[data-D1=b] .chd{padding:var(--space-xl) var(--space-2xl) 0;align-items:center}
.pv[data-D1=b] .ch-t h3{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body)}
.pv[data-D1=b] .ch-s,.pv[data-D1=b] .ch-dv{display:none}
.pv[data-D1=b] .cc-b{padding:var(--space-lg) var(--space-2xl) var(--space-xl)}
.pv[data-D1=b] .cc.tbl .cc-b{padding:var(--space-lg) 0 0}
.pv[data-D1=b] .ch-ld.fi{width:var(--featured-icon-size-compact);height:var(--featured-icon-size-compact)}
/* D2 hành động: a nút phụ + ⋯ · b chỉ ⋯ · c liên kết */
.pv:not([data-platform=mobile])[data-D2=b] .act-a,.pv:not([data-platform=mobile])[data-D2=c] .act-a{display:none}
.pv:not([data-platform=mobile])[data-D2=b] .act-b,.pv:not([data-platform=mobile])[data-D2=c] .act-c{display:flex}
/* D3 leading: a featured icon 40 · b icon trần 20 · c không dùng */
.pv[data-D3=b] .ch-ld.fi{width:auto;height:auto;background:none;box-shadow:none;align-self:center}
.pv[data-D3=b] .ch-ld .av{width:var(--size-2xl);height:var(--size-2xl);font-size:var(--font-size-xs)}
.pv[data-D3=c] .ch-ld{display:none}
/* D4 số đếm cạnh tiêu đề: a viên số · b chữ xám */
.pv[data-D4=b] .ch-nb{display:none}
.pv[data-D4=b] .ch-nt{display:inline}
/* D5 nút thu gọn: a bên phải · b bên trái tiêu đề */
.pv[data-D5=b] .ch-col{display:none!important}
.pv[data-D5=b] .ch-coll{display:inline-flex!important;margin-left:calc(var(--space-md) * -1)}
/* D6 thẻ chứa bảng: a đầu thẻ + gạch, bảng liền · b đầu thẻ nền xám như thanh bảng */
.pv[data-D6=b] .cc.tbl .chd{background:var(--color-bg-secondary);border-radius:var(--radius-card) var(--radius-card) 0 0;padding-top:var(--space-xl);padding-bottom:var(--space-xl)}
.pv[data-D6=b] .cc.tbl .ch-s{display:none}
/* D7 app: a giữ phụ đề, ⋯ · b bỏ phụ đề, hành động là chữ */
.pv[data-platform=mobile][data-D7=b] .act-b{display:none!important}
.pv[data-platform=mobile][data-D7=b] .act-m,.pv[data-platform=mobile][data-D7=b] .act.fix{display:flex!important}
.pv[data-platform=mobile][data-D7=b] .ch-s{display:none}
.pv[data-platform=mobile][data-D7=b] .chd{align-items:center}
.pv[data-platform=mobile][data-D7=b] .act-m .lnk{min-height:var(--touch-min)}
"""


# ======================================================================
# SECTION HEADER
# ======================================================================
def section_header(title, sub="", actions=(), tab_html="", search=None, size="md", count=None, tools=""):
    """actions: [(nhãn, icon, kind)] · search: chữ gợi ý ô tìm · size: md (phần trang) | sm (nhóm trong form)."""
    web = "".join(bt(a[0], a[2] if len(a) > 2 else "sec", a[1], a[3] if len(a) > 3 else None) for a in actions)
    q = (f'<label class="sh-q">{ic("search", 14)}<span>{search}</span></label>' if search else "")
    icons = "".join(ibt(a[1] or "checkc", a[0], "sec") for a in actions[:2])
    txt = f'<a class="lnk">{actions[-1][0]}</a>' if actions else ""
    n = (f'<span class="sh-nb">{cnt(count)}</span>') if count is not None else ""
    inline = f'<div class="sh-tin">{tab_html}</div>' if tab_html else ""
    below = f'<div class="sh-tbl">{tab_html}</div>' if tab_html else ""
    tool = (f'<div class="sh-tool"><label class="sh-q2">{ic("search", 14)}<span>{search}</span></label>{bt("Lọc", "sec", "filter")}{tools}</div>' if search else "")
    mob = (f'<div class="sh-am">{ibt("more", "Thao tác")}</div><div class="sh-ai">{icons}</div><div class="sh-at">{txt}</div>' if actions else "")
    return (f'<div class="shd s-{size}{" has-tabs" if tab_html else ""}{" has-q" if search else ""}"{cm("section-header")}><div class="sh-r"><div class="sh-m"><div class="sh-t"><h2>{title}</h2>{n}</div>'
            f'{f"<p>{sub}</p>" if sub else ""}</div>{inline}<div class="sh-a">{q}{web}</div>{mob}</div>{tool}{below}<div class="sh-dv"></div></div>')


def fsec(title, sub, body, actions=()):
    return f'<section class="fsec"><div class="fsec-h">{section_header(title, sub, actions, size="sm")}</div><div class="fsec-b">{body}</div></section>'


CSS_SH = r"""
.shd{display:flex;flex-direction:column;gap:var(--space-2xl);min-width:0}
.sh-r{display:flex;gap:var(--space-xl);align-items:flex-start}
.sh-m{flex:1;min-width:0;display:flex;flex-direction:column;gap:var(--space-xs)}
.sh-t{display:flex;align-items:center;gap:var(--space-md);min-width:0}
.sh-t h2{margin:0;font:400 var(--type-title-3-size)/var(--type-title-3-line-height) var(--font-title);font-synthesis:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.pv[data-state=long] .sh-t h2{white-space:normal}
.sh-m p{margin:0;color:var(--color-text-tertiary);font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.sh-a{display:flex;gap:var(--space-lg);align-items:center;flex:none}
.sh-q,.sh-q2{display:flex;align-items:center;gap:var(--space-md);height:var(--control-height-md);padding:0 var(--control-padding-x-md);width:var(--width-xxs);max-width:100%;
 border:1px solid var(--color-border-primary);border-radius:var(--radius-field);background:var(--color-bg-primary);box-shadow:var(--shadow-xs);color:var(--color-fg-quaternary);
 font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.sh-q span,.sh-q2 span{color:var(--color-text-placeholder);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sh-tool{display:none;gap:var(--space-lg);align-items:center}
.sh-am,.sh-ai,.sh-at{display:none}
.sh-dv{height:1px;background:var(--color-border-secondary)}
.sh-tin{display:none}
.shd.has-tabs .sh-dv{display:none}
.shd.s-sm{gap:var(--space-xl)}
.shd.s-sm .sh-t h2{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body)}
.shd.s-sm .sh-dv{display:none}
.fsec{display:flex;flex-direction:column;gap:var(--space-2xl);padding-bottom:var(--space-3xl);border-bottom:1px solid var(--color-border-secondary)}
.fsec:last-child{border-bottom:0}
.fsec-b{display:flex;flex-direction:column;gap:var(--form-field-gap,var(--space-xl));min-width:0}
/* app — đề xuất: hành động vào ⋯ */
.pv[data-platform=mobile] .sh-a,.pv[data-platform=mobile] .sh-tool{display:none!important}
.pv[data-platform=mobile] .sh-am{display:flex}
.pv[data-platform=mobile] .sh-am .bt,.pv[data-platform=mobile] .sh-ai .bt{width:var(--touch-min);height:var(--touch-min)}
.pv[data-platform=mobile] .sh-am .bt{margin:calc(var(--space-md) * -1) calc(var(--space-lg) * -1) calc(var(--space-md) * -1) 0;border-color:transparent;background:none;box-shadow:none}
.pv[data-platform=mobile] .shd{gap:var(--space-lg)}
"""

OPT_SH = r"""
/* D1 gạch dưới: a có · b không */
.pv[data-D1=b] .sh-dv{display:none}
/* D2 Tabs: a hàng riêng · b cùng hàng tiêu đề */
.pv:not([data-platform=mobile])[data-D2=b] .sh-tbl{display:none}
.pv:not([data-platform=mobile])[data-D2=b] .sh-tin{display:block;align-self:flex-end;min-width:0;flex:none;max-width:50%}
.pv:not([data-platform=mobile])[data-D2=b] .shd.has-tabs .sh-r{align-items:flex-end}
.pv:not([data-platform=mobile])[data-D2=b] .shd.has-tabs .sh-dv{display:block;margin-top:calc(var(--space-2xl) * -1)}
.pv:not([data-platform=mobile])[data-D2=b] .sh-tin .tbw::before{display:none}
.pv[data-D1=b][data-D2=b] .shd.has-tabs .sh-dv{display:none}
/* D3 ô tìm: a trong đầu phần · b hàng công cụ riêng (ô tìm + Lọc) */
.pv:not([data-platform=mobile])[data-D3=b] .sh-q{display:none}
.pv:not([data-platform=mobile])[data-D3=b] .shd.has-q .sh-tool{display:flex}
/* D4 cỡ: a hai cỡ (MD title-3 · SM heading) · b một cỡ */
.pv[data-D4=b] .shd.s-sm .sh-t h2{font:400 var(--type-title-3-size)/var(--type-title-3-line-height) var(--font-title)}
.pv[data-D4=b] .shd.s-sm .sh-dv{display:block}
/* D5 form cài đặt: a tiêu đề trên · b cột trái */
.pv:not([data-platform=mobile])[data-D5=b] .fsec{display:grid;grid-template-columns:var(--width-xxs) minmax(0,1fr);gap:var(--space-4xl)}
/* D6 số đếm: a trong phụ đề · b viên số cạnh tiêu đề */
.sh-nb{display:none}
.pv[data-D6=b] .sh-nb{display:inline-flex}
.pv[data-D6=b] .sh-m p .cnt-in{display:none}
/* D7 app: a ⋯ · b nút icon (≤ 2) · c chữ hành động */
.pv[data-platform=mobile][data-D7=b] .sh-am,.pv[data-platform=mobile][data-D7=c] .sh-am{display:none}
.pv[data-platform=mobile][data-D7=b] .sh-ai{display:flex;gap:var(--space-md)}
.pv[data-platform=mobile][data-D7=c] .sh-at{display:flex;align-items:center;min-height:var(--touch-min)}
"""


# ======================================================================
# EMPTY STATE
# ======================================================================
ILLO = ('<svg class="es-ill" viewBox="0 0 120 80" width="120" height="80" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round">'
        '<rect x="14" y="30" width="56" height="30" rx="3" fill="var(--color-bg-secondary)"/><path d="M70 38h18l10 10v12H70z" fill="var(--color-bg-secondary)"/>'
        '<path d="M76 40h10l7 8H76z" fill="var(--color-bg-primary)"/><circle cx="30" cy="62" r="6" fill="var(--color-bg-primary)"/><circle cx="84" cy="62" r="6" fill="var(--color-bg-primary)"/>'
        '<path d="M6 68h108" stroke-dasharray="3 4"/><path d="M26 18l6 6M44 12v8M60 18l-6 6" stroke-linecap="round"/></svg>')


def empty(title, desc, icon="inbox", size="md", primary=None, secondary=None, kind="", ctx="", link=None):
    """kind: '' rỗng · search · err · ok · lock · off · ctx: card (trong thẻ/bảng) · page (cả màn) · menu."""
    a = ""
    if primary or secondary or link:
        a = ('<div class="es-ac">' + (bt(secondary[0], "sec", secondary[1]) if secondary else "")
             + (bt(primary[0], "pri", primary[1]) if primary else "") + (f'<a class="lnk">{link}</a>' if link else "") + "</div>")
    fi = {"sm": "f40", "md": "f48", "lg": "f56"}[size]
    return (f'<div class="es es-{size} k-{kind or "none"} c-{ctx or "none"}"{cm("empty-state")}><div class="es-hd"><span class="es-pat"></span><span class="es-grd"></span>'
            f'<span class="fi {fi}"><span class="fii">{ic(icon, 20)}</span></span>{ILLO}</div>'
            f'<div class="es-tx"><b class="es-t">{title}</b><p class="es-d">{desc}</p></div>{a}</div>')


CSS_ES = r"""
.fi{display:grid;place-items:center;flex:none;position:relative;z-index:1;background:var(--color-bg-primary);color:var(--color-fg-secondary);
 border-radius:var(--radius-lg);box-shadow:var(--shadow-xs),inset 0 0 0 1px var(--color-border-primary)}
.fi .fib{display:none}
.fi.f40{width:var(--featured-icon-size-md);height:var(--featured-icon-size-md);border-radius:var(--radius-md)}
.fi.f48{width:var(--featured-icon-size);height:var(--featured-icon-size)}
.fi.f56{width:var(--featured-icon-size-xl);height:var(--featured-icon-size-xl);border-radius:var(--radius-xl)}
.es{display:flex;flex-direction:column;align-items:center;text-align:center;gap:var(--space-xl);padding:var(--space-5xl) var(--space-3xl);position:relative;overflow:hidden}
.es-hd{position:relative;display:grid;place-items:center}
.es-pat,.es-grd{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);pointer-events:none}
.es-pat{width:calc(var(--featured-icon-size) * 7);height:calc(var(--featured-icon-size) * 7);border-radius:var(--radius-full);
 background:repeating-radial-gradient(circle,transparent 0 calc(var(--space-3xl) - 1px),var(--color-border-secondary) calc(var(--space-3xl) - 1px) var(--space-3xl));
 -webkit-mask:radial-gradient(circle,#000 10%,transparent 62%);mask:radial-gradient(circle,#000 10%,transparent 62%)}
.es-grd{display:none;width:calc(var(--featured-icon-size) * 7);height:calc(var(--featured-icon-size) * 5);
 background-image:linear-gradient(var(--color-border-secondary) 1px,transparent 1px),linear-gradient(90deg,var(--color-border-secondary) 1px,transparent 1px);
 background-size:var(--space-3xl) var(--space-3xl);background-position:center;-webkit-mask:radial-gradient(ellipse,#000 10%,transparent 65%);mask:radial-gradient(ellipse,#000 10%,transparent 65%)}
.es-ill{display:none;color:var(--color-fg-quaternary)}
.es-tx{display:flex;flex-direction:column;gap:var(--space-xs);max-width:var(--width-xs);position:relative;z-index:1}
.es-t{font:600 var(--type-body-lg-size)/var(--type-body-lg-line-height) var(--font-body);color:var(--color-text-primary)}
.es-d{margin:0;font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body);color:var(--color-text-tertiary)}
.es-ac{display:flex;gap:var(--space-lg);position:relative;z-index:1;margin-top:var(--space-md);align-items:center;flex-wrap:wrap;justify-content:center}
.es-ac .lnk{flex-basis:100%;justify-content:center}
.es.es-sm{padding:var(--space-3xl) var(--space-xl);gap:var(--space-lg)}
.es.es-sm .es-pat{width:calc(var(--featured-icon-size-md) * 5);height:calc(var(--featured-icon-size-md) * 5)}
.es.es-sm .es-t{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body)}
.es.es-sm .es-ac{margin-top:var(--space-xs)}
.es.es-sm .bt{height:var(--control-height-sm);padding:0 var(--control-padding-x-sm)}
.es.es-lg{padding:var(--layout-empty-padding) var(--space-3xl)}
.es.es-lg .es-t{font:400 var(--type-title-2-size)/var(--type-title-2-line-height) var(--font-title);font-synthesis:none}
.es.es-lg .es-d{font:400 var(--type-body-lg-size)/var(--type-body-lg-line-height) var(--font-body)}
.es.es-lg .bt{height:var(--control-height-lg);padding:0 var(--control-padding-x-lg)}
.es.c-menu{padding:var(--space-3xl) var(--space-xl)}
.es.c-menu .es-pat{display:none}
/* thử (góp ý 04/11): featured icon nền xám, không viền — tròn hoặc vuông bo */
.es.fs-gray .fi{background:var(--color-bg-tertiary);box-shadow:none;color:var(--color-fg-secondary)}
.es.fs-gray.fs-round .fi{border-radius:var(--radius-full)}
.es.fs-gray.k-err .fi{color:var(--color-fg-error-primary)}
/* đề xuất: icon xám, chỉ lỗi màu đỏ */
.es.k-err .fi{color:var(--color-fg-error-primary)}
/* app */
.pv[data-platform=mobile] .es{padding:var(--space-6xl) var(--space-3xl)}
.pv[data-platform=mobile] .es.es-sm{padding:var(--space-3xl) var(--space-xl)}
.pv[data-platform=mobile] .es-ac{flex-direction:column-reverse;align-self:stretch;gap:var(--space-md)}
.pv[data-platform=mobile] .es-ac .bt{height:var(--control-height-lg);width:100%}
.pv[data-platform=mobile] .es.es-sm .es-ac .bt{height:var(--control-height-md)}
"""

OPT_ES = r"""
/* D1 hình đầu: a icon + nền · b chỉ icon · c minh hoạ */
.pv[data-D1=b] .es-pat,.pv[data-D1=b] .es-grd{display:none!important}
.pv[data-D1=c] .es-pat,.pv[data-D1=c] .es-grd,.pv[data-D1=c] .es .fi{display:none!important}
.pv[data-D1=c] .es-ill{display:block}
.pv[data-D1=c] .es.es-sm .es-ill{width:calc(var(--featured-icon-size) * 1.75);height:var(--featured-icon-size)}
/* D2 nền: a vòng tròn · b lưới ô vuông */
.pv[data-D2=b] .es-pat{display:none}
.pv[data-D2=b] .es-grd{display:block}
.pv[data-D1=b][data-D2=b] .es-grd{display:none}
/* D3 màu icon: a xám, lỗi đỏ · b xám hết · c màu theo loại */
.pv[data-D3=b] .es.k-err .fi{color:var(--color-fg-secondary)}
.pv[data-D3=c] .es.k-ok .fi{color:var(--color-fg-success-primary);background:var(--color-bg-success-secondary);box-shadow:none}
.pv[data-D3=c] .es.k-err .fi{background:var(--color-bg-error-secondary);box-shadow:none}
.pv[data-D3=c] .es.k-lock .fi,.pv[data-D3=c] .es.k-off .fi{color:var(--color-fg-warning-primary);background:var(--color-bg-warning-secondary);box-shadow:none}
.pv[data-D3=c] .es.k-search .fi,.pv[data-D3=c] .es.k-none .fi{color:var(--color-fg-secondary);background:var(--color-bg-secondary);box-shadow:none}
/* D4 nút: a phụ + chính · b chỉ phụ · c chỉ chính */
.pv[data-D4=b] .es-ac .bt.pri{display:none}
.pv[data-D4=c] .es-ac .bt.sec:has(+ .bt.pri){display:none}
/* D5 cỡ: a SM · MD · LG · b SM · MD (LG dùng MD) */
.pv[data-D5=b] .es.es-lg{padding:var(--space-5xl) var(--space-3xl)}
.pv[data-D5=b] .es.es-lg .es-t{font:600 var(--type-body-lg-size)/var(--type-body-lg-line-height) var(--font-body)}
.pv[data-D5=b] .es.es-lg .es-d{font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.pv[data-D5=b] .es.es-lg .fi{width:var(--featured-icon-size);height:var(--featured-icon-size);border-radius:var(--radius-lg)}
.pv[data-D5=b] .es.es-lg .bt{height:var(--control-height-md);padding:0 var(--control-padding-x-md)}
/* D6 SM trong thẻ: a canh giữa · b canh trái ngang */
.pv:not([data-platform=mobile])[data-D6=b] .es.es-sm.c-card{display:grid;grid-template-columns:auto minmax(0,1fr);grid-template-areas:"hd tx" "hd ac";text-align:left;justify-items:start;column-gap:var(--space-xl);row-gap:var(--space-md)}
.pv:not([data-platform=mobile])[data-D6=b] .es.es-sm.c-card .es-hd{grid-area:hd;align-self:start}
.pv:not([data-platform=mobile])[data-D6=b] .es.es-sm.c-card .es-tx{grid-area:tx}
.pv:not([data-platform=mobile])[data-D6=b] .es.es-sm.c-card .es-ac{grid-area:ac;margin-top:0}
.pv:not([data-platform=mobile])[data-D6=b] .es.es-sm.c-card .es-pat{display:none}
/* D7 app cả màn: a nút trong khối · b nút cố định đáy */
.pv[data-platform=mobile][data-D7=b] .es.c-page{padding-bottom:calc(var(--control-height-lg) * 2 + var(--space-6xl))}
.pv[data-platform=mobile][data-D7=b] .es.c-page{position:static}
.pv[data-platform=mobile][data-D7=b] .es.c-page .es-ac{position:absolute;left:var(--container-padding-mobile);right:var(--container-padding-mobile);bottom:calc(var(--space-9xl) - var(--space-md));z-index:6}
"""


# ======================================================================
# COMMAND MENU
# ======================================================================
CMD_RES = [  # theo _Header search panel đã duyệt (header-navigation.md): Tính năng · Hành động · Bản ghi
    ("Tính năng", [("truck", "<mark>Lệnh</mark> vận tải", "Điều phối vận tải › Danh sách", "", "Tính năng"),
                   ("wrench", "<mark>Lệnh</mark> sửa chữa", "Bảo dưỡng sửa chữa › Danh sách", "", "Tính năng"),
                   ("card", "<mark>Lệnh</mark> chi tạm ứng", "Quỹ & thanh toán", "", "Tính năng")]),
    ("Hành động", [("plus", "Tạo <mark>lệnh</mark> vận tải", "Mở form tạo mới", "⌘N", "Hành động"),
                   ("truck", "Gán xe cho <mark>lệnh</mark>…", "Chọn lệnh rồi chọn xe", "", "Hành động")]),
    ("Bản ghi", [("file", "LVT-2026-0412", "Cát Lái → Sóng Thần", "Đang chạy", "Bản ghi"),
                 ("file", "LVT-2026-0415", "Cát Lái → Phnom Penh", "Chờ xe", "Bản ghi")]),
]
CMD_RECENT = [("Dùng gần đây", [("truck", "Lệnh vận tải", "Điều phối vận tải › Danh sách", "", "Tính năng"),
                                ("file", "LVT-2026-0412", "Cát Lái → Sóng Thần · Đang chạy", "", "Bản ghi"),
                                (("av", 0), "Trần Văn Bình", "Lái xe · 0903 xxx 128", "", "Bản ghi"),
                                ("chart", "Báo cáo chuyến theo tuyến", "Báo cáo › Vận tải", "", "Tính năng"),
                                ("plus", "Tạo lệnh vận tải", "Mở form tạo mới", "⌘N", "Hành động")])]
CMD_NESTED = [("Xe sẵn sàng gần Cát Lái", [("box", "51C-404.12", "Đầu kéo Hino 700 · cách 2,1 km", "Sẵn sàng", "Xe"),
                                           ("box", "51C-388.40", "Đầu kéo Hyundai Xcient · cách 4,8 km", "Sẵn sàng", "Xe"),
                                           ("box", "51D-102.77", "Đầu kéo Hino 700 · bảo dưỡng tới 16:00", "Bảo dưỡng", "Xe")])]
SCOPES = ["Tất cả", "Tính năng", "Hành động", "Bản ghi"]


def _cm_rows(groups):
    rows, first = [], True
    for g, items in groups:
        rows.append(f'<div class="cm-g">{g}</div>')
        for icon, t, s, r, kind in items:
            lead = av(icon[1], "a28") if isinstance(icon, tuple) else f'<span class="cm-ic">{ic(icon, 16)}</span>'
            rr = kbd(r) if r.startswith("⌘") else ""
            if r and not r.startswith("⌘"):
                s = f"{s} · {r}"
            js = ' data-js="nest"' if t.startswith("Gán xe") else ""
            rows.append(f'<div class="cm-i{" on" if first else ""}"{js}>{lead}<span class="cm-tx"><b>{t}</b><small>{s}</small></span>'
                        f'<span class="cm-k">{kind}</span><span class="cm-r">{rr}</span><span class="cm-en">{ic("ret", 14)}</span></div>')
            first = False
    return "".join(rows)


def cmd_menu(query="lệnh", groups=CMD_RES, mode="results", ctx=None, live=False, scope=0):
    """mode: results · recent · empty · loading · nested."""
    spin = f'<span class="cm-spin">{ic("spin", 16)}</span>'
    q = (f'<span class="cm-q">{query}<i class="caret"></i></span>' if query else '<span class="cm-ph">Tìm lệnh, xe, lái xe hoặc thao tác…</span>')
    chip_ctx = f'<span class="cm-ctx">{ic("truck", 14)}{ctx}{ic("x", 12)}</span>' if ctx else ""
    nh = (f'<div class="cm-nh">{ibt("arrowl", "Quay lại", size="sm")}<b>{ctx}</b><span>Bước 2/2 · chọn xe</span></div>' if ctx else "")
    sc = '<div class="cm-sc">' + "".join(f'<span class="cm-chip{" on" if k == scope else ""}">{s}</span>' for k, s in enumerate(SCOPES)) + "</div>"
    body = _cm_rows(groups)
    if mode == "empty":
        body = (f'<div class="cm-em"><span class="cm-ei">{ic("search", 20)}</span><b>Không có tính năng “{query}”</b>'
                '<span>Thử một từ khác. Màn bạn không có quyền sẽ không hiện ở đây.</span></div>')
    skel = '<div class="cm-sk">' + "".join(f'<div class="cm-skr"><span class="sk sq"></span><span class="cm-tx">{sk("55%")}{sk("80%", "xs")}</span></div>' for _ in range(5)) + "</div>"
    prev = ('<aside class="cm-pv"><div class="cm-pv-h"><b class="code">LVT-2026-0412</b>' + pill("Đang chạy") + '</div>'
            + kv([("Khách", "Delta Logistics"), ("Tuyến", "Cát Lái → Sóng Thần"), ("Lái xe", "Trần Văn Bình"), ("Xe", "51C-404.12"), ("Giờ hẹn", "14:00 hôm nay")])
            + f'<div class="cm-pv-a">{bt("Mở lệnh", "sec", None, size="sm")}{bt("Gọi lái xe", "sec", None, size="sm")}</div></aside>')
    foot = (f'<div class="cm-f"><span>{kbd("↑")}{kbd("↓")} chọn</span><span>{kbd("↵")} mở</span>'
            f'<span class="cm-f-tab">{kbd("Tab")} đổi phạm vi</span><span class="cm-f-px"># bản ghi · / hành động</span><span class="sp"></span><span>Chỉ hiện tính năng bạn có quyền</span></div>')
    d = " data-live" if live else ""
    return (f'<div class="cmd m-{mode}{" nested" if ctx else ""}" role="dialog" aria-label="Tìm nhanh"{cm("command-menu")}{d}>{nh}'
            f'<div class="cm-in">{ic("search", 20)}{chip_ctx}{q}{spin}{kbd("Esc")}</div>{sc}'
            f'<div class="cm-mid"><div class="cm-b">{skel}<div class="cm-list">{body}</div></div>{prev}</div>{foot}</div>')


def cmd_app(query="lệnh", groups=CMD_RES, mode="results"):
    rows = []
    for g, items in groups:
        rows.append(f'<div class="cm-g">{g}</div>')
        for icon, t, s, r, kind in items:
            lead = av(icon[1], "a40") if isinstance(icon, tuple) else f'<span class="cm-ic pei">{ic(icon, 20)}</span>'  # pei: giữ icon 20, không quy đổi app
            rows.append(f'<div class="cma-i">{lead}<span class="cm-tx"><b>{t}</b><small>{s}</small></span>{pill(r) if r and not r.startswith("⌘") else ""}</div>')
    body = "".join(rows)
    if mode == "empty":
        body = (f'<div class="cm-em"><span class="cm-ei">{ic("search", 20)}</span><b>Không tìm thấy “{query}”</b>'
                '<span>Thử biển số xe hoặc mã lệnh đầy đủ.</span></div>')
    q = f'<span class="cm-q">{query}</span>' if query else '<span class="cm-ph">Tìm lệnh, xe, địa điểm…</span>'
    sc = '<div class="cm-sc">' + "".join(f'<span class="cm-chip{" on" if k == 0 else ""}">{s}</span>' for k, s in enumerate(SCOPES[:4])) + "</div>"
    return (f'<div class="cma-scr"></div><div class="cma"{cm("command-menu")}><span class="cma-hd"></span><div class="cma-top"><div class="cma-in">{ic("search", 20)}{q}'
            f'{ic("x", 16) if query else ""}</div><a class="lnk">Huỷ</a></div>{sc}<div class="cma-b">{body}</div></div>')


CSS_CMD = r"""
.cm-ov{position:absolute;inset:0;z-index:30;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));display:flex;justify-content:center;align-items:flex-start;padding-top:var(--space-9xl)}
.cmd{width:var(--command-search-width);max-width:calc(100% - var(--space-4xl));background:var(--color-bg-primary_alt);border-radius:var(--radius-overlay);text-align:left;
 box-shadow:var(--shadow-xl),0 0 0 1px var(--shadow-xl-border);overflow:hidden;display:flex;flex-direction:column}
.cm-nh{display:none}
.cm-in{height:calc(var(--control-height-lg) + var(--space-lg));display:flex;align-items:center;gap:var(--space-lg);padding:0 var(--space-xl);border-bottom:1px solid var(--color-border-secondary);color:var(--color-fg-quaternary)}
.cm-q,.cm-ph{flex:1;min-width:0;font:400 var(--type-title-3-size)/var(--type-title-3-line-height) var(--font-body);color:var(--color-text-primary);white-space:nowrap;overflow:hidden}
.cm-ph{color:var(--color-text-tertiary)}
.caret{display:inline-block;width:1px;height:var(--type-title-3-line-height);background:var(--color-text-primary);vertical-align:bottom;margin-left:1px}
.cm-ctx{display:inline-flex;align-items:center;gap:var(--space-xs);height:var(--chip-height-lg);padding:0 var(--space-md);border-radius:var(--radius-badge);background:var(--color-bg-secondary);
 box-shadow:inset 0 0 0 1px var(--color-border-primary);color:var(--color-text-primary);font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);white-space:nowrap;flex:none}
.cm-spin{display:none;color:var(--color-fg-quaternary);animation:cmspin 1s linear infinite}
@keyframes cmspin{to{transform:rotate(360deg)}}
.cm-sc{display:flex;gap:var(--space-xs);padding:var(--space-md) var(--space-lg);border-bottom:1px solid var(--color-border-secondary);overflow-x:auto;scrollbar-width:none}
.cm-chip{display:inline-flex;align-items:center;height:var(--control-height-sm);padding:0 var(--control-padding-x-sm);border-radius:var(--radius-control);white-space:nowrap;cursor:pointer;
 font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-tertiary)}
.cm-chip.on{background:var(--color-bg-selected);color:var(--color-text-primary)}
.cm-mid{display:flex;min-height:0}
.cm-b{flex:1;min-width:0;padding:0 0 var(--space-md);max-height:calc(var(--control-height-lg) * 9);overflow:auto;display:flex;flex-direction:column}
.cm-list{display:flex;flex-direction:column}
.cm-g{padding:var(--space-lg) var(--space-xl) var(--space-xs);font:500 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);text-transform:uppercase;color:var(--color-text-tertiary)}
.cm-i{display:flex;align-items:center;gap:var(--space-md);min-height:var(--control-height-lg);padding:var(--space-xs) var(--space-xl);cursor:pointer;
 transition:background var(--duration-fast) var(--easing-standard)}
.cm-i:hover{background:var(--color-bg-primary_hover)}
.cm-i.on{background:var(--color-bg-selected);box-shadow:inset var(--focus-width) 0 0 var(--color-focus-ring)}
.cm-ic{width:var(--control-height-sm);height:var(--control-height-sm);border-radius:var(--radius-inner);display:grid;place-items:center;flex:none;color:var(--color-text-secondary);box-shadow:inset 0 0 0 1px var(--color-border-secondary)}
.cm-ic svg{stroke-width:2}
.cm-tx{flex:1;min-width:0;display:flex;flex-direction:column}
.cm-tx b{font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cm-tx small{font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pv[data-state=long] .cm-tx b,.pv[data-state=long] .cm-tx small{white-space:normal}
.cm-tx mark{background:var(--color-bg-warning-secondary);color:inherit;border-radius:var(--radius-xxs);padding:0 var(--command-search-highlight-padding-x)}
.cm-k{display:none;font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary);flex:none}
.cm-r{flex:none;display:flex;align-items:center}
.cm-en{display:none;color:var(--color-fg-quaternary)}
.cm-i.on .cm-en{display:inline-flex}
.cm-sk{display:none;flex-direction:column;gap:var(--space-xs)}
.cm-skr{display:flex;align-items:center;gap:var(--space-md);min-height:calc(var(--control-height-lg) + var(--space-md));padding:0 var(--space-lg)}
.cm-skr .cm-tx{gap:var(--space-sm)}
.cm-pv{display:none}
.cm-f{display:flex;gap:var(--space-lg);align-items:center;padding:var(--space-md) var(--space-xl);border-top:1px solid var(--color-border-secondary);background:var(--color-bg-secondary);
 font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary)}
.cm-f>span{display:inline-flex;align-items:center;gap:var(--space-xs)}
.cm-f .sp{flex:1}
.cm-f-px{display:none!important}
.cm-ei{width:var(--featured-icon-size);height:var(--featured-icon-size);border-radius:var(--radius-full);display:grid;place-items:center;background:var(--color-bg-tertiary);color:var(--color-text-secondary)}
.cm-em{display:flex;flex-direction:column;align-items:center;gap:var(--space-xs);padding:var(--space-3xl) var(--space-xl);text-align:center;color:var(--color-text-tertiary);font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.cm-em b{color:var(--color-text-primary);font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body);margin-top:var(--space-md)}
.cm-em span{font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body)}
/* loading — đề xuất: giữ kết quả cũ mờ + vòng quay trong ô nhập */
.cmd.m-loading .cm-spin{display:inline-flex}
.cmd.m-loading .cm-list{opacity:.5}
/* app — đề xuất: màn tìm toàn màn */
.cma-scr{display:none}
.cma{position:absolute;inset:0;z-index:20;background:var(--color-bg-primary);display:flex;flex-direction:column}
.cma-hd{display:none}
.cma-top{display:flex;align-items:center;gap:var(--space-lg);padding:var(--space-md) var(--container-padding-mobile)}
.cma-in{flex:1;display:flex;align-items:center;gap:var(--space-md);height:var(--control-height-md);padding:0 var(--control-padding-x-sm);border-radius:var(--radius-field);background:var(--color-bg-secondary);color:var(--color-fg-quaternary)}
.cma-in .cm-q,.cma-in .cm-ph{font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.cma .cm-sc{padding:0 var(--container-padding-mobile) var(--space-md);border-bottom:1px solid var(--color-border-secondary)}
.cma .cm-chip{height:var(--control-height-sm);border:1px solid var(--color-border-primary);border-radius:var(--radius-full)}
.cma .cm-chip.on{background:var(--color-accent-solid);border-color:var(--color-accent-solid);color:var(--color-text-inverse)}
.cma-b{flex:1;overflow:auto;padding:0 var(--space-md) var(--space-6xl)}
.cma-i{display:flex;align-items:center;gap:var(--space-lg);min-height:var(--control-height-lg);padding:var(--space-md);border-radius:var(--radius-menu-item)}
.cma-i .cm-ic{width:var(--featured-icon-size-md);height:var(--featured-icon-size-md)}
"""

OPT_CMD = r"""
/* D2 chân hộp: a có gợi ý phím · b không */
.pv[data-D2=b] .cm-f{display:none}
/* D3 xếp kết quả: a nhóm theo loại · b phẳng + nhãn loại */
.pv[data-D3=b] .cm-g{display:none}
.pv[data-D3=b] .cm-k{display:inline}
.pv[data-D3=b] .cm-r{display:none}
.pv[data-D3=b] .cmd .cm-b{padding-top:var(--space-xs)}
/* D4 phạm vi: a chip dưới ô · b tiền tố gõ (#, @, /) · c không */
.pv[data-D4=b] .cmd .cm-sc,.pv[data-D4=c] .cmd .cm-sc,.pv[data-D4=b] .cm-f-tab,.pv[data-D4=c] .cm-f-tab{display:none!important}
.pv[data-D4=b] .cm-f-px{display:inline-flex!important}
/* D5 khung xem trước: a có · b không */
.pv:not([data-platform=mobile])[data-D5=a] .cmd{width:calc(var(--command-search-width) + var(--width-xxs))}
.pv[data-D5=a] .cmd.m-results .cm-pv{display:flex;flex-direction:column;gap:var(--space-xl);width:var(--width-xxs);flex:none;padding:var(--space-xl);border-left:1px solid var(--color-border-secondary);background:var(--color-bg-secondary_alt)}
.pv[data-D5=a] .cm-pv-h{display:flex;justify-content:space-between;align-items:center}
.pv[data-D5=a] .cm-pv .kv{grid-template-columns:auto minmax(0,1fr)}
.pv[data-D5=a] .cm-pv-a{display:flex;gap:var(--space-md);margin-top:auto}
/* D6 lệnh nhiều bước: a chip ngữ cảnh trong ô · b dòng tiêu đề có ← */
.pv[data-D6=b] .cmd.nested .cm-ctx{display:none}
.pv[data-D6=b] .cmd.nested .cm-nh{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-md) var(--space-lg);border-bottom:1px solid var(--color-border-secondary)}
.pv[data-D6=b] .cm-nh b{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body)}
.pv[data-D6=b] .cm-nh span{margin-left:auto;font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary)}
/* D7 đang tải: a khung xương · b giữ kết quả cũ mờ + vòng quay */
.pv[data-D7=a] .cmd.m-loading .cm-list{display:none}
.pv[data-D7=a] .cmd.m-loading .cm-sk{display:flex}
.pv[data-D7=a] .cmd.m-loading .cm-spin{display:none}
/* D8 app: a toàn màn · b bottom sheet cao */
.pv[data-platform=mobile][data-D8=b] .cma-scr{display:block;position:absolute;inset:0;z-index:19;background:var(--color-bg-overlay)}
.pv[data-platform=mobile][data-D8=b] .cma{top:var(--space-7xl);border-radius:var(--radius-overlay) var(--radius-overlay) 0 0;box-shadow:var(--shadow-xl)}
.pv[data-platform=mobile][data-D8=b] .cma-hd{display:block;width:var(--space-4xl);height:var(--space-xs);border-radius:var(--radius-full);background:var(--color-bg-quaternary);margin:var(--space-md) auto 0}
"""


# ======================================================================
# CSS chung: nút, badge, avatar, kbd, bảng, khung biến thể, màn
# ======================================================================
CSS_BASE = r"""
.pv{position:relative;font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body);color:var(--color-text-primary)}
.pv *{box-sizing:border-box}
.i{flex:none;display:block}
button{font:inherit;color:inherit}
.bt{height:var(--control-height-md);padding:0 var(--control-padding-x-md);border:1px solid transparent;border-radius:var(--radius-control);display:inline-flex;align-items:center;justify-content:center;
 gap:var(--control-icon-gap);font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);white-space:nowrap;cursor:pointer;flex:none;
 transition:background var(--duration-fast) var(--easing-standard)}
.bt.sm{height:var(--control-height-sm);padding:0 var(--control-padding-x-sm)}
.bt.io{width:var(--control-height-md);padding:0}.bt.io.sm{width:var(--control-height-sm)}
.bt.pri{background:var(--color-action-primary);color:var(--color-text-inverse)}
.bt.sec{background:var(--color-bg-primary);border-color:var(--color-border-primary);color:var(--color-text-primary);box-shadow:var(--shadow-xs)}
.bt.sec:hover{background:var(--color-bg-primary_hover)}
.bt.ter{background:transparent;color:var(--color-text-tertiary_strong)}
.bt.ter:hover{background:var(--color-bg-selected)}
.pv[data-platform=mobile] .bt{height:var(--control-height-md)}
.lnk{display:inline-flex;align-items:center;gap:var(--space-xs);font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-primary);cursor:pointer;white-space:nowrap;text-decoration:none}
.pill{display:inline-flex;align-items:center;gap:var(--space-sm);height:var(--chip-height-sm);padding:0 var(--chip-padding-x-sm);border-radius:var(--radius-full);white-space:nowrap;flex:none;
 font:600 var(--chip-font-size-sm)/var(--chip-line-height-sm) var(--font-body)}
.pill i{width:var(--space-sm);height:var(--space-sm);border-radius:var(--radius-full);background:currentColor}
.pill.t-gray{background:var(--color-utility-neutral-50);color:var(--color-utility-neutral-700)}
.pill.t-green{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}
.pill.t-yellow{background:var(--color-utility-yellow-50);color:var(--color-utility-yellow-700)}
.pill.t-red{background:var(--color-utility-red-50);color:var(--color-utility-red-700)}
.pill.t-blue{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}
.av{display:inline-grid;place-items:center;border-radius:var(--radius-full);flex:none;width:var(--control-height-md);height:var(--control-height-md);font:600 var(--type-caption-size)/1 var(--font-body)}
.av.a28{width:var(--control-height-sm);height:var(--control-height-sm)}
.av.a40{width:var(--featured-icon-size-md);height:var(--featured-icon-size-md);font:600 var(--type-heading-size)/1 var(--font-body)}
.av.t-blue{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700)}.av.t-red{background:var(--color-utility-red-50);color:var(--color-utility-red-700)}
.av.t-green{background:var(--color-utility-green-50);color:var(--color-utility-green-700)}.av.t-purple{background:var(--color-utility-purple-50);color:var(--color-utility-purple-700)}
.av.t-orange{background:var(--color-utility-orange-50);color:var(--color-utility-orange-700)}
.kbd{display:inline-flex;align-items:center;justify-content:center;min-width:var(--size-2xl);height:var(--size-2xl);padding:0 var(--space-xs);border-radius:var(--radius-xs);
 border:1px solid var(--color-border-primary);background:var(--color-bg-primary);color:var(--color-text-tertiary);font:500 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body)}
.sk{display:block;height:var(--space-lg);border-radius:var(--radius-xs);background:var(--color-bg-skeleton)}
.sk.xs{height:var(--space-md)}.sk.sq{width:var(--control-height-sm);height:var(--control-height-sm);border-radius:var(--radius-inner);flex:none}
.code{font:400 var(--type-code-size)/var(--type-code-line-height) var(--font-code)}
.pv[data-state=long] .nl{display:none}
.pv[data-state=empty] [data-hide~=empty],.pv[data-state=nores] [data-hide~=nores],.pv[data-state=error] [data-hide~=error],.pv[data-state=noperm] [data-hide~=noperm],
.pv[data-state=offline] [data-hide~=offline],.pv[data-state=loading] [data-hide~=loading],.pv[data-state=cmd] [data-hide~=cmd],.pv[data-state=recent] [data-hide~=recent],
.pv[data-state=nested] [data-hide~=nested],.pv[data-state=collapsed] [data-hide~=collapsed],.pv[data-state=long] [data-hide~=long],.pv[data-state=picked] [data-hide~=picked],.pv[data-state=scrolled] [data-hide~=scrolled],.pv[data-state=more] [data-hide~=more]{display:none!important}
/* bảng biến thể */
.vg{padding:var(--space-2xl) var(--space-3xl) var(--space-4xl);display:flex;flex-direction:column;gap:var(--space-3xl);background:var(--color-bg-secondary)}
.pv[data-platform=mobile] .vg{padding:var(--space-xl)}
.vgs h3{margin:0 0 var(--space-lg);font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body);display:flex;gap:var(--space-md);align-items:baseline}
.vgs h3 small{font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary)}
.vgr{display:grid;gap:var(--space-lg)}
.vgc{display:flex;flex-direction:column;gap:var(--space-md);min-width:0;padding:var(--space-lg);border:1px solid var(--color-border-secondary);border-radius:var(--radius-xl);background:var(--color-bg-primary)}
.vgc .cap{font:500 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary)}
"""

CSS_SCREEN = r"""
.pad{padding:var(--space-xl) var(--container-padding-desktop) var(--space-4xl);display:flex;flex-direction:column;gap:var(--layout-section-gap)}
.mpad{padding:var(--space-md) var(--container-padding-mobile) var(--space-9xl);display:flex;flex-direction:column;gap:var(--layout-list-gap)}
.tw{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);overflow:hidden;background:var(--color-bg-primary);box-shadow:var(--shadow-xs)}
.cc .tw{border:0;border-radius:0;box-shadow:none}
.tbl{width:100%;border-collapse:collapse;color:inherit;font:inherit}
.tbl th,.tbl td{padding:0 var(--table-cell-padding-x);height:var(--table-row-min-height);border-bottom:1px solid var(--color-border-secondary);text-align:left;vertical-align:middle;font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.tbl th{height:calc(var(--control-height-lg) + var(--space-xxs));background:var(--color-bg-secondary);color:var(--color-text-tertiary);font:500 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);text-transform:uppercase;white-space:nowrap}
.tbl tr:last-child td{border-bottom:0}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--layout-section-gap)}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--layout-section-gap)}
.span2{grid-column:span 2}
.pv[data-platform=mobile] .grid2,.pv[data-platform=mobile] .grid3{grid-template-columns:1fr}
.pv[data-platform=mobile] .span2{grid-column:auto}
.kv{display:grid;grid-template-columns:var(--space-10xl) minmax(0,1fr);gap:var(--space-md) var(--space-xl);margin:0}
.kv dt{color:var(--color-text-tertiary)}.kv dd{margin:0;min-width:0}
.doc{display:flex;align-items:center;gap:var(--space-lg);padding:var(--space-md) 0;border-bottom:1px solid var(--color-border-secondary)}
.doc:last-child{border-bottom:0}.doc .dn{flex:1;min-width:0;display:flex;flex-direction:column}.doc .dn b{font-weight:500}
.doc .dn small{color:var(--color-text-tertiary);font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body)}
.doc .di{width:var(--control-height-md);height:var(--control-height-md);border-radius:var(--radius-inner);display:grid;place-items:center;background:var(--color-bg-secondary);color:var(--color-fg-tertiary);flex:none}
.mcard{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);padding:var(--layout-card-padding);display:flex;flex-direction:column;gap:var(--space-xs);background:var(--color-bg-primary)}
.mc1{display:flex;justify-content:space-between;align-items:center}.mc1 .code{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-code)}
.mc2{font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}.mc3{color:var(--color-text-tertiary);font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body)}
.kpi{display:flex;flex-direction:column;gap:var(--space-xs)}.kpi b{font:400 var(--type-display-size)/var(--type-display-line-height) var(--font-title);font-variant-numeric:tabular-nums}
.kpi small{color:var(--color-text-tertiary)}
.bars{display:flex;align-items:flex-end;gap:var(--space-md);height:calc(var(--space-10xl) + var(--space-4xl))}
.bars i{flex:1;background:var(--color-bg-quaternary);border-radius:var(--radius-xs) var(--radius-xs) 0 0}.bars i.on{background:var(--color-fg-primary)}
.fld{display:flex;flex-direction:column;gap:var(--space-sm)}
.fld>span{font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-secondary)}
.inp{height:var(--control-height-md);padding:0 var(--control-padding-x-md);display:flex;align-items:center;border:1px solid var(--color-border-primary);border-radius:var(--radius-field);background:var(--color-bg-primary);box-shadow:var(--shadow-xs)}
.row{display:flex;align-items:center;gap:var(--space-lg)}.sp{flex:1}
.split{display:grid;grid-template-columns:calc(var(--width-xxs) * .75) minmax(0,1fr);gap:var(--space-4xl)}
.pv[data-platform=mobile] .split{grid-template-columns:1fr}
.feed{display:flex;flex-direction:column;gap:var(--space-xl)}
.feed>div{display:flex;gap:var(--space-lg)}.feed small{display:block;color:var(--color-text-tertiary);font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body)}
.notif{position:absolute;right:var(--space-3xl);top:var(--space-md);width:var(--width-xs);z-index:25;background:var(--color-bg-primary_alt);border-radius:var(--radius-menu);box-shadow:var(--shadow-lg),0 0 0 1px var(--shadow-lg-border);overflow:hidden}
.notif .nh{display:flex;align-items:center;justify-content:space-between;padding:var(--space-lg) var(--space-xl);border-bottom:1px solid var(--color-border-secondary)}
.notif .nh b{font:600 var(--type-heading-size)/var(--type-heading-line-height) var(--font-body)}
.menu{width:var(--width-xxs);background:var(--color-bg-primary_alt);border-radius:var(--radius-menu);box-shadow:var(--shadow-lg),0 0 0 1px var(--shadow-lg-border);padding:var(--space-xs)}
"""


def m_factory(rec):
    def m(over, inner, w=440, plat="web"):
        pick = {**rec, **(over or {}), "state": "x"}
        return mini(pick, inner, w, plat)
    return m


def write(out, page, decisions, brief=True):
    """page.css = token (.pv) + CSS bộ chung + CSS trang; brief: bỏ ý tưởng cộng đồng. brief=False giữ ý tưởng + bộ chọn theo ý tưởng."""
    from icon_dec329 import apply as _dec329
    _dec329(page)
    if brief:
        page["brief"] = True
        page.pop("ideas", None)
        page["presets"] = [p for p in page.get("presets", []) if p["id"] in ("rec", "untitled", "astryx")]
    page["css"] = tok_css_nested() + page.get("css", "") + mshow_css(decisions)
    old = Path(out)
    if old.exists():
        o = json.loads(old.read_text())
        for k in ("snaps", "cmtSnap", "cmtChanges", "kit"):
            if k in o and k not in page:
                page[k] = o[k]
    Path(out).write_text(json.dumps(page, ensure_ascii=False, indent=1))
    print("ok", out, len(decisions), "điểm ·", len(page.get("screens", [])), "màn")


def rec_of(decisions):
    return {d["id"]: chr(97 + next(k for k, o in enumerate(d["options"]) if o.get("rec"))) for d in decisions}


ALL_CSS = CSS_BASE + CSS_TABS + CSS_CH + CSS_SH + CSS_ES + CSS_CMD


# ======================================================================
# PAGE HEADER (04/11) — đầu trang: tiêu đề màn (type/title-1), phụ đề, hành động, trường chính của bản ghi.
# Đường dẫn nằm ở thanh trên (Header navigation, DEC-291) — Page header không lặp đường dẫn.
# ======================================================================
def page_header(title, sub="", actions=(), badge="", fields=(), meta=(), lead=None, parent=None, pager=None, keep=2, tab_html=""):
    """actions: [(nhãn, icon, kind)] — hiện `keep` nút cuối (nút chính ở cuối), còn lại vào ⋯ (D4 A).
    fields: [(nhãn, giá trị)] khối trường chính (D2 B) · meta: [chuỗi] hàng meta chữ (D2 A) · lead: ('fi', icon) | ('av', i)
    parent: tên trang cha (D3 C) · pager: (vị trí, tổng) chuyển bản ghi (D8)."""
    acts = list(actions)
    n = len(acts)
    web = "".join(bt(a[0], a[2] if len(a) > 2 else "sec", a[1]).replace('class="bt ', f'class="bt{" ovx" if k < n - keep else ""} ', 1)
                  for k, a in enumerate(acts))
    more = ibt("more", "Thao tác khác", "sec").replace("bt io", "bt io ph-more") if n > keep else ""
    ld = ""
    if lead and lead[0] == "fi":
        ld = f'<span class="ph-ld fi f48"><span class="fii">{ic(lead[1], 20)}</span></span>'
    elif lead and lead[0] == "av":
        ld = f'<span class="ph-ld">{av(lead[1], "a48")}</span>'
    par = f'<a class="ph-par">{ic("chevl", 14)}{parent}</a>' if parent else ""
    back = ibt("arrowl", "Quay lại", "sec").replace("bt io", "bt io ph-back") if parent else ""
    pg = (f'<div class="ph-pg">{ibt("chevl", "Bản ghi trước", "sec", size="sm")}<span>{pager[0]} / {pager[1]}</span>'
          f'{ibt("chevr", "Bản ghi sau", "sec", size="sm")}</div>') if pager else ""
    mt = ('<div class="ph-meta">' + "".join(f"<span>{x}</span>" for x in meta) + "</div>") if meta else ""
    kf = ('<dl class="ph-kf">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in fields) + "</dl>") if fields else ""
    s = f'<p class="ph-s">{sub}</p>' if sub else ""
    skel = f'<div class="ph-skl" data-show="state:loading">{sk("40%", "sm")}{sk("25%", "xs")}</div>'
    tabs_in = f'<div class="ph-tabs">{tab_html}</div>' if tab_html else ""
    mob = ibt("more", "Thao tác", "ter").replace("bt io", "bt io ph-am") if acts else ""
    two = " has2" if (sub or meta) else ""
    return (f'<header class="phd{" has-kf" if fields else ""}{" has-tabs" if tab_html else ""}{two}"{cm("page-header")}>{par}<div class="ph-r">{back}{ld}'
            f'<div class="ph-m"><div data-hide="loading" class="ph-mm"><div class="ph-t"><h1>{title}</h1>{badge}</div>{s}{mt}</div>{skel}</div>'
            f'{pg}<div class="ph-a">{web}{more}</div>{mob}</div>{kf}{tabs_in}</header>')


def page_sticky(title, badge="", primary=None, tab_html=""):
    """Thanh gọn dính đầu khi cuộn (D5 B) — tiêu đề nhỏ + trạng thái + nút chính; D5 C chỉ giữ hàng tab."""
    p = bt(primary[0], "pri", primary[1], size="sm") if primary else ""
    return (f'<div class="ph-st" data-show="state:scrolled"{cm("page-header")}><div class="ph-st-r"><span class="ph-st-back" aria-label="Quay lại">{ic("chevl", 20)}</span><b>{title}</b>{badge}<span class="sp"></span>{p}</div>'
            f'{f"<div class=ph-st-t>{tab_html}</div>" if tab_html else ""}</div>')


CSS_PH = r"""
.phd{display:flex;flex-direction:column;gap:var(--space-2xl);padding-bottom:var(--space-2xl);border-bottom:1px solid var(--color-border-secondary);min-width:0}
.ph-r{display:flex;gap:var(--space-xl);align-items:flex-start;min-width:0}
.ph-m{flex:1;min-width:0;display:flex;flex-direction:column}
.ph-mm{display:flex;flex-direction:column;gap:var(--space-xs);min-width:0}
.ph-t{display:flex;align-items:center;gap:var(--space-lg);min-width:0}
.ph-t h1{margin:0;font:400 var(--type-title-1-size)/var(--type-title-1-line-height) var(--font-title);font-synthesis:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}
.pv[data-state=long] .ph-t h1{white-space:normal}
.ph-s{margin:0;color:var(--color-text-tertiary);font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.ph-skl{display:flex;flex-direction:column;gap:var(--space-md);padding:var(--space-xs) 0}
.ph-skl .sk{height:var(--space-3xl)}.ph-skl .sk.xs{height:var(--space-lg)}
.ph-meta{display:none;flex-wrap:wrap;gap:var(--space-xs) var(--space-lg);color:var(--color-text-tertiary);font:400 var(--type-body-size)/var(--type-body-line-height) var(--font-body)}
.ph-meta span+span::before{content:"·";margin-right:var(--space-lg)}
.ph-kf{display:grid;grid-template-columns:repeat(auto-fill,minmax(calc(var(--width-xxs) / 2),1fr));gap:var(--space-lg) var(--space-3xl);margin:0}
.ph-kf>div{display:flex;flex-direction:column;gap:var(--space-xxs);min-width:0}
.ph-kf dt{font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary)}
.ph-kf dd{margin:0;font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-primary);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pv[data-state=long] .ph-kf dd{white-space:normal}
.ph-ld{flex:none;display:inline-flex}
/* ảnh / icon đầu tiêu đề cao bằng các dòng chữ bên phải: 1 dòng tiêu đề = title-1 line-height 32; 2 dòng (tiêu đề + phụ đề/meta) = 56 */
.phd .ph-ld.fi,.phd .ph-ld .av{width:var(--type-title-1-line-height);height:var(--type-title-1-line-height);border-radius:var(--radius-md)}
.phd .ph-ld .av{border-radius:var(--radius-full)}
.phd.has2 .ph-ld.fi,.phd.has2 .ph-ld .av{width:var(--featured-icon-size-xl);height:var(--featured-icon-size-xl)}
.phd.has2 .ph-ld.fi{border-radius:var(--radius-xl)}
.av.a48{width:var(--featured-icon-size);height:var(--featured-icon-size);font:600 var(--type-label-size)/1 var(--font-body)}
.ph-par,.ph-back{display:none!important}
.ph-par{align-items:center;gap:var(--space-xs);font:500 var(--type-label-size)/var(--type-label-line-height) var(--font-body);color:var(--color-text-tertiary);cursor:pointer}
.ph-pg{display:flex;align-items:center;gap:var(--space-md);flex:none;font:400 var(--type-caption-size)/var(--type-caption-line-height) var(--font-body);color:var(--color-text-tertiary);font-variant-numeric:tabular-nums}
.ph-a{display:flex;gap:var(--space-lg);align-items:center;flex:none}
.ph-a .bt.ovx{display:none}
.ph-am{display:none!important}
.ph-tabs{display:none}
.phd.has-tabs{padding-bottom:0;border-bottom:0}
.hn-sec{padding:0 var(--container-padding-desktop);background:var(--color-bg-primary)}
.hn-sec .tbw.k-line::before{left:calc(var(--container-padding-desktop) * -1);right:calc(var(--container-padding-desktop) * -1)}
.ph-st{position:sticky;top:0;z-index:8;margin:calc(var(--space-xl) * -1) calc(var(--container-padding-desktop) * -1) 0;padding:var(--space-lg) var(--container-padding-desktop) 0;
 background:var(--color-bg-primary);box-shadow:var(--shadow-sm);display:flex;flex-direction:column;gap:var(--space-md)}
.ph-st-r{display:flex;align-items:center;gap:var(--space-lg);padding-bottom:var(--space-lg)}
.ph-st-r b{font:600 var(--type-body-lg-size)/var(--type-body-lg-line-height) var(--font-body)}
.ph-st-t .tbw.k-line::before{display:none}
.ph-st-back{display:none}
/* app: thanh gọn = ← + tiêu đề cùng dòng như thanh trên (góp ý 04/11); trong màn có thanh trên của app thì thanh trên đảm nhận */
.pv[data-platform=mobile] .ph-st-back{display:inline-flex;width:var(--touch-min);height:var(--touch-min);margin:calc(var(--space-lg) * -1) 0 calc(var(--space-lg) * -1) calc(var(--space-lg) * -1);align-items:center;justify-content:center}
.pv[data-platform=mobile] .ph-st-r b{font:600 var(--type-body-lg-size)/var(--type-body-lg-line-height) var(--font-body)}
.pv[data-platform=mobile] .sh .ph-st-r{display:none}
/* app — đề xuất: tiêu đề lớn trong nội dung, thanh trên chỉ hiện tiêu đề khi đã cuộn (D9 A) */
.pv[data-platform=mobile] .phd{gap:var(--space-lg);padding-bottom:var(--space-xl)}
.pv[data-platform=mobile] .ph-a,.pv[data-platform=mobile] .ph-pg{display:none}
.pv[data-platform=mobile] .ph-am{display:inline-flex!important;width:var(--touch-min);height:var(--touch-min);margin:calc(var(--space-md) * -1) calc(var(--space-lg) * -1) calc(var(--space-md) * -1) 0}
.pv[data-platform=mobile] .ph-kf{grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-lg)}
/* app: ảnh / icon cùng hàng tiêu đề, cao bằng dòng tiêu đề; phụ đề, meta xuống dòng thẳng mép trái với hàng tab (góp ý 04/11) */
.pv[data-platform=mobile] .ph-r{display:grid;grid-template-columns:auto minmax(0,1fr) auto;column-gap:var(--space-lg);row-gap:var(--space-xs);align-items:center}
.pv[data-platform=mobile] .ph-m,.pv[data-platform=mobile] .ph-mm{display:contents}
.pv[data-platform=mobile] .ph-ld{grid-column:1;grid-row:1}
.pv[data-platform=mobile] .ph-t{grid-column:2;grid-row:1;flex-wrap:wrap}
.pv[data-platform=mobile] .ph-r:not(:has(.ph-ld)) .ph-t{grid-column:1 / 3}
.pv[data-platform=mobile] .ph-am{grid-column:3;grid-row:1}
.pv[data-platform=mobile] .ph-s,.pv[data-platform=mobile] .ph-meta,.pv[data-platform=mobile] .ph-skl{grid-column:1 / -1}
.pv[data-platform=mobile] .phd.has2 .ph-ld.fi,.pv[data-platform=mobile] .phd.has2 .ph-ld .av{width:var(--type-title-1-line-height);height:var(--type-title-1-line-height)}
.pv[data-platform=mobile] .phd.has2 .ph-ld.fi{border-radius:var(--radius-md)}
.pv[data-platform=mobile] .ph-meta{flex-direction:column;gap:var(--space-xxs)}
.pv[data-platform=mobile] .ph-meta span+span::before{content:none}
.pv[data-platform=mobile] .ph-st{margin:calc(var(--space-md) * -1) calc(var(--container-padding-mobile) * -1) 0;padding:var(--space-md) var(--container-padding-mobile) 0}
.pv[data-platform=mobile]:not([data-state=scrolled]) .sh-bar span{visibility:hidden}
.pv[data-platform=mobile] .ph-st-r .bt{display:none}
.pv[data-platform=mobile] .ph-t{flex-wrap:wrap;row-gap:var(--space-xs)}
.pv[data-platform=mobile] .ph-t h1{white-space:normal;overflow-wrap:anywhere}
"""

OPT_PH = r"""
/* D1 cấu tạo: a Simple (title-1 24 + phụ đề + gạch) · b Gọn (title-2 20, không phụ đề, không gạch) */
.pv[data-D1=b] .ph-t h1{font:400 var(--type-title-2-size)/var(--type-title-2-line-height) var(--font-title)}
.pv[data-D1=b] .ph-s{display:none}
.pv[data-D1=b] .phd{border-bottom:0;padding-bottom:0;gap:var(--space-xl)}
/* D2 thông tin bản ghi: a hàng meta chữ · b khối trường chính · c không */
.pv[data-D2=a] .ph-kf,.pv[data-D2=c] .ph-kf{display:none}
.pv[data-D2=a] .ph-meta{display:flex}
/* D3 quay lại: a không (đường dẫn trên thanh) · b nút ← trước tiêu đề · c liên kết trang cha trên tiêu đề */
.pv[data-D3=b] .ph-back{display:inline-flex!important}
.pv[data-D3=c] .ph-par{display:inline-flex!important}
/* D4 hành động: a ≤ 2 nút + ⋯ · b hiện hết */
.pv[data-D4=b] .ph-a .bt.ovx{display:inline-flex}
.pv[data-D4=b] .ph-a .ph-more{display:none}
/* D5 khi cuộn: a cuộn mất · b thanh gọn dính đầu · c chỉ hàng tab dính */
.pv[data-D5=a] .ph-st{display:none!important}
.pv[data-D5=c] .ph-st-r{display:none}
.pv[data-D5=c] .ph-st:not(:has(.ph-st-t)){display:none!important}
/* D6 tab của trang: a nằm trong Page header · b Secondary Nav của Header navigation (đã duyệt) */
.pv[data-D6=a] .ph-tabs{display:block}
.pv[data-D6=a] .hn-sec{display:none}
.pv:not([data-D6=a]) .ph-st-t{display:none}
/* D7 ảnh / icon đầu tiêu đề: a có (tuỳ chọn) · b không */
.pv[data-D7=b] .ph-ld{display:none}
/* D8 chuyển bản ghi trước/sau: a có · b không */
.pv[data-D8=b] .ph-pg{display:none}
/* D9 app: a tiêu đề lớn trong nội dung · b chỉ tiêu đề nhỏ trên thanh */
.pv[data-platform=mobile][data-D9=b] .sh-bar span{visibility:visible!important}
.pv[data-platform=mobile][data-D9=b] .ph-t h1{font:400 var(--type-title-3-size)/var(--type-title-3-line-height) var(--font-title)}
.pv[data-platform=mobile][data-D9=b] .phd .ph-t h1{display:none}
"""
