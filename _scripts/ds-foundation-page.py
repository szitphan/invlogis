#!/usr/bin/env python3
"""Trang duyệt trạng thái các mục foundations DS v2 → design-system/_review/foundations-status.html (publish thành artifact).

  python3 _scripts/ds-foundation-page.py

Mỗi mục: xem thử dựng bằng design-system/tokens.css (Light/Dark, Web/Mobile), trạng thái hiện tại trong repo, nút chọn trạng
thái mới + ghi chú → lưu kho trang (collection "status", doc = mã mục). Claude đọc về rồi áp bằng
`ds-foundation-status.py apply` (L1), ghi nhãn Figma. Nguồn trạng thái vẫn là bảng trong foundations.md.
"""
import base64
import html
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "design-system/_review/foundations-status.html"
E = html.escape

spec = importlib.util.spec_from_file_location("dfs", ROOT / "_scripts/ds-foundation-status.py")
dfs = importlib.util.module_from_spec(spec); spec.loader.exec_module(dfs)
ROWS = dfs.read()[3]
TK = json.loads((ROOT / "design-system/tokens.json").read_text())
CSS = (ROOT / "design-system/tokens.css").read_text()
MARK = (ROOT / "design/brand/innvie-v1/mark-color.svg").read_text()
MARK = re.sub(r"<\?xml[^>]*>", "", MARK)


def sem_colors(prefix):
    return [k for k in TK["collections"]["Semantic"]["color"] if k.startswith(prefix)]


def v(name):
    return "--" + name.replace("/", "-")


def sw(name):
    return (f'<div class="sw"><i style="background:var({v(name)})"></i><b>{E(name.split("/", 2)[-1])}</b>'
            f'<code data-css="{v(name)}"></code></div>')


def color():
    groups = [("Nền", "color/bg/"), ("Chữ", "color/text/"), ("Icon", "color/icon/"), ("Viền", "color/border/"),
              ("Trạng thái", "color/status/")]
    h = "".join(f'<h4>{g}</h4><div class="swg">{"".join(sw(n) for n in sem_colors(p))}</div>' for g, p in groups)
    pairs = [("color/text/primary", "color/bg/primary"), ("color/text/tertiary", "color/bg/primary"),
             ("color/text/tertiary_strong", "color/bg/secondary"), ("color/text/tertiary", "color/bg/secondary"),
             ("color/text/disabled", "color/bg/primary")]
    h += '<h4>Tương phản đo trên trang</h4><div class="cg">' + "".join(
        f'<div class="ct" style="background:var({v(b)});color:var({v(a)})" data-fg="{v(a)}" data-bg="{v(b)}">'
        f'<span>Lệnh vận tải LVT-2026-0412</span><small>{E(a.split("/")[-1])} / {E(b.split("/")[-1])} · <b class="cr"></b></small></div>'
        for a, b in pairs if a in TK["collections"]["Semantic"]["color"] and b in TK["collections"]["Semantic"]["color"]) + "</div>"
    return h


def typo():
    out = []
    for name, st in TK["textStyles"].items():
        size, lh = v(st["size"]), v(st["lineHeight"])
        fam = "var(--font-title)" if st["family"] == "Cal Sans" else "var(--font-code)" if "Mono" in st["family"] else "var(--font-body)"
        w = {"Regular": 400, "Medium": 500, "Semi Bold": 600, "Bold": 700}.get(st["style"], 400)
        up = "text-transform:uppercase;" if st.get("case") == "UPPER" else ""
        out.append(f'<div class="ty"><div class="tyl"><b>{E(name)}</b><small>{E(st["family"])} {E(st["style"])} · '
                   f'<span data-css="{size}"></span>/<span data-css="{lh}"></span></small></div>'
                   f'<div style="font-family:{fam};font-size:var({size});line-height:var({lh});font-weight:{w};{up}">'
                   f'Điều phối vận tải Cát Lái → Sóng Thần</div></div>')
    return "".join(out)


def radius():
    names = ["control", "field", "card", "inner", "overlay", "chip", "menu", "menu-item", "badge", "tab"]
    return '<div class="rg">' + "".join(
        f'<div class="rd"><i style="border-radius:var(--radius-{n})"></i><b>radius/{n}</b><code data-css="--radius-{n}"></code></div>'
        for n in names) + "</div>"


def space():
    names = [f"space/gap-{x}" for x in ("xs", "sm", "md", "lg", "xl", "2xl")] + [f"space/inset-{x}" for x in ("xs", "sm", "md", "lg", "xl")]
    names += ["grid/margin", "layout/card-padding", "layout/list-gap", "layout/section-gap", "layout/title-gap"]
    return '<div class="sp">' + "".join(
        f'<div class="spr"><b>{n}</b><i style="width:var({v(n)})"></i><code data-css="{v(n)}"></code></div>' for n in names) + "</div>" + \
        '<h4>Cao control</h4><div class="ctl">' + "".join(
            f'<span style="height:var(--control-height-{s});padding:0 var(--control-padding-x-{s})">control {s} · <code data-css="--control-height-{s}"></code></span>'
            for s in ("sm", "md", "lg")) + "</div>"


def grid():
    g = TK["grid"]["web"]
    cols = "".join("<i></i>" for _ in range(g["columns"]))
    bps = " · ".join(f"{k} {x}" for k, x in TK["breakpoints"].items())
    widths = "".join(f'<div class="wd"><i style="width:min(100%,calc(var(--width-{w}) / 3))"></i><b>width/{w}</b>'
                     f'<code data-css="--width-{w}"></code></div>' for w in ("xs", "sm", "md", "lg", "xl", "2xl"))
    return (f'<p class="muted">Web: {g["columns"]} cột, gutter {g["gutter"]}, lề <code>grid/margin</code>, rộng tối đa '
            f'{g["maxWidth"]} ({E(g["maxWidthApplies"])}); chi tiết chia {g["detailSplit"]}. Breakpoint: {bps}.</p>'
            f'<div class="gr" style="gap:calc({g["gutter"]}px / 3);padding:0 calc(var(--grid-margin) / 3)">{cols}</div>'
            f'<h4>Độ rộng khung (thu 1/3)</h4>{widths}')


def elevation():
    cards = "".join(f'<div class="el" style="box-shadow:var(--shadow-{n});border:1px solid var(--shadow-{n}-border, transparent)">shadow/{n}</div>'
                    for n in ("xs", "sm", "md", "lg", "xl", "2xl", "3xl"))
    blurs = "".join(f'<div class="bl"><div class="blbg"></div><div class="blf" style="backdrop-filter:blur(var(--backdrop-blur-{b}))">backdrop-blur/{b} · '
                    f'<code data-css="--backdrop-blur-{b}"></code></div></div>' for b in ("sm", "md", "lg", "xl"))
    return f'<div class="elg">{cards}</div><h4>Làm mờ nền</h4><div class="blg">{blurs}</div>'


def touch():
    return ('<div class="tf"><button class="fb">Nút có vòng focus</button><span class="muted">vòng <code data-css="--focus-width"></code> · '
            'cách <code data-css="--focus-offset"></code> · màu <code>color/focus/ring</code></span></div>'
            '<div class="tf"><span class="hit"><i></i></span><span class="muted">vùng chạm tối thiểu <code data-css="--touch-min"></code> '
            '(icon 16 vẫn bấm được cả ô)</span></div>')


def motion():
    return '<div class="mo">' + "".join(
        f'<div class="mor"><b>duration/{d}</b><code data-css="--duration-{d}"></code><span class="track"><i style="transition-duration:var(--duration-{d});'
        f'transition-timing-function:var(--easing-standard)"></i></span></div>' for d in ("fast", "medium", "slow")) + \
        '<button class="mob" type="button">Chạy thử</button> <span class="muted">easing <code data-css="--easing-standard"></code></span></div>'


def icon():
    files = sorted(p for p in (ROOT / "design-system/icons").glob("*.svg") if not p.stem.endswith("-fill"))[:8]
    svgs = []
    for p in files:
        s = re.sub(r"<\?xml[^>]*>", "", p.read_text())
        s = re.sub(r'\s(width|height)="[^"]*"', "", s, count=2)
        svgs.append((p.stem, s))
    rows = "".join(
        f'<div class="icr"><b>{sz}px</b>' + "".join(f'<span class="ic" style="width:{sz}px;height:{sz}px;--sw:{2.25 if sz <= 16 else 2}" title="{E(n)}">{s}</span>'
                                                    for n, s in svgs) + f'<small class="muted">nét {round(2 * sz / 24, 2)} hiển thị</small></div>'
        for sz in (14, 16, 20, 24))
    return (f'<p class="muted">Lucide 1.58 + icon nghiệp vụ (DEC-145) · nét 2 trên khung 24 · cỡ theo nền tảng: '
            f'<code>icon/size/sm</code> <span data-css="--icon-size-sm"></span> · <code>md</code> <span data-css="--icon-size-md"></span> · '
            f'<code>lg</code> <span data-css="--icon-size-lg"></span></p>{rows}')


def logo():
    """Logo thật từ tệp SVG, đổi theo nút Light/Dark của trang; dùng <img> vì các SVG trùng id gradient."""
    def img(path, h):
        b = base64.b64encode((ROOT / path).read_bytes()).decode()
        return f'<img src="data:image/svg+xml;base64,{b}" alt="" style="height:{h}px;width:auto;max-width:100%;display:block">'
    inv, dl = "design/brand/invlogis/logo/invlogis", "design/brand/delta/logo/delta"

    def cell(light, dark, h):
        return f'<span class="lgl">{img(light, h)}</span><span class="lgd">{img(dark, h)}</span>'
    rows = "".join(
        f'<h4>{E(name)}</h4><div style="display:flex;flex-wrap:wrap;gap:24px;align-items:center">'
        + "".join(cell(f"{base}-primary.svg", f"{base}-reverse.svg", h) for h in (24, 40, 64))
        + cell(f"{sym}.svg", f"{sym}-reverse.svg", 24) + "</div>"
        for name, base, sym in (("Invlogis · logo ngang 24, 40, 64 · ký hiệu 24", inv, inv + "-symbol-small"),
                                ("Khách (Delta) · logo ngang 24, 40, 64 · ký hiệu 24", dl, dl + "-symbol")))
    return ('<style>.lgd{display:none}[data-theme="dark"] .lgl{display:none}[data-theme="dark"] .lgd{display:inline}</style>'
            '<p class="muted">Trục Size theo thang <code>size/*</code>: <code>size/3xl</code> 24 · <code>size/5xl</code> 40 · '
            '<code>size/7xl</code> 64 (DEC-326). Cao tối thiểu 20.</p>' + rows)


PREVIEW = ROOT / "design-system/_review/foundations/previews"
FIGMA_NODE = "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ?node-id="


def _shot(p, cls, alt):
    if not p.exists():
        return f'<p class="muted {cls}">Chưa có ảnh.</p>'
    return (f'<img class="{cls}" src="data:image/png;base64,{base64.b64encode(p.read_bytes()).decode()}" alt="{E(alt)}" loading="lazy" '
            'style="width:100%;height:auto;border:1px solid #E2E8F0;border-radius:8px">')


def shot_note(key, doc):
    """Ảnh không tự làm mới: so phiên bản lúc chụp với phiên bản hiện tại của mục (DEC-337)."""
    m = json.loads((PREVIEW / "previews.json").read_text(encoding="utf-8"))
    cur = (subprocess.run([sys.executable, str(ROOT / "_scripts/ds-deps.py"), "fversion", key], capture_output=True, text=True, cwd=ROOT).stdout.split()[1])
    note = (f"Ảnh chụp từ Figma ngày {m['taken']}, đổi theo nút Light/Dark ở trên; bấm tên để mở đúng khu. Luật: <code>design-system/foundations/{doc}</code>.")
    if m["versions"].get(key) != cur:
        note = f"<b>⚠ Tài liệu đã đổi sau ngày chụp, ảnh có thể cũ.</b> {note}"
    return note


def shots(items):
    """Ảnh chụp từng khu trên Figma (Sáng, Tối), lưu ở _review/foundations/previews: 2 mục này không dựng được từ tokens.css."""
    out = ['<style>.shd{display:none}[data-theme="dark"] .shd{display:block}.shl{display:block}[data-theme="dark"] .shl{display:none}</style>']
    for name, f, node in items:
        link = f'<a href="{FIGMA_NODE}{node.replace(":", "-")}">{E(name)}</a>'
        out.append(f'<h4>{link}</h4>{_shot(PREVIEW / f"{f}.png", "shl", name)}{_shot(PREVIEW / f"{f}-dark.png", "shd", name + " · Dark")}')
    return "".join(out)


def misc_icon():
    return ('<p class="muted">' + shot_note("misc-icon", "icon-sets.md") + '</p>'
            + shots((("Featured icon", "misc-featured", "6732:186017"), ("File type icon", "misc-file-type", "6732:186018"),
                     ("Huy hiệu, QR, _Dot, Play", "misc-badges", "6732:186019"), ("Payment", "misc-payment", "6732:186020"),
                     ("Cờ quốc gia", "misc-flag", "6732:186021"), ("Ngân hàng Việt Nam", "misc-bank", "6732:186022"),
                     ("App tích hợp", "misc-app", "6732:186023"))))


def vehicle():
    d = json.loads((ROOT / "design-system/handoff/vehicles.json").read_text(encoding="utf-8"))
    return (f'<p class="muted">{len(d["groups"])} nhóm hình · {len(d["views"])} mặt cắt · {len(d["tyre_layouts"])} sơ đồ lốp (DEC-266, DEC-267). '
            + shot_note("vehicle", "vehicle.md") + '</p>'
            + shots((("Images", "vehicle-images", "6779:2091"), ("Frames", "vehicle-frames", "6779:2092"),
                     ("Tyres", "vehicle-tyres", "6779:2093"), ("Markers", "vehicle-markers", "6779:2094"))))


SECTIONS = {"color": color, "type": typo, "radius": radius, "space": space, "grid": grid, "elevation": elevation,
            "touch-focus": touch, "motion": motion, "icon": icon, "misc-icon": misc_icon, "vehicle": vehicle, "logo": logo}
LBL = dfs.LABEL
ORDER = list(dfs.STATUSES)


def section(r):
    body = SECTIONS[r["key"]]()
    nxt = sorted(dfs.FLOW.get(r["status"], ()), key=ORDER.index)
    btns = "".join(f'<button type="button" data-k="{r["key"]}" data-to="{t}">{E(LBL[t])}</button>' for t in nxt)
    return (f'<section class="sec" id="{r["key"]}"><header><div><h2>{E(r["name"])}</h2>'
            f'<small class="muted">foundations.md {E(r["where"])} · cập nhật {E(r["date"])}</small></div>'
            f'<span class="st st-{r["status"]}">Trong repo: {E(LBL[r["status"]])}</span></header>'
            f'<div class="pvw">{body}</div>'
            f'<div class="pick"><span>Đổi trạng thái:</span>{btns}<span class="saved" data-saved="{r["key"]}"></span>'
            f'<textarea data-note="{r["key"]}" placeholder="Ghi chú (vd cần sửa gì trước khi duyệt)"></textarea></div></section>')


PAGE_CSS = r"""
*{box-sizing:border-box}body{margin:0;font:14px/20px Inter,system-ui,sans-serif;color:#171717;background:#F5F7FB}
.band{background:#0036B5;color:#fff;padding:20px 32px;display:flex;align-items:center;gap:14px}
.band svg{width:36px;height:36px}.band h1{margin:0;font:400 26px/32px "Cal Sans",Inter,sans-serif}.band p{margin:2px 0 0;opacity:.85}
.wrap{max-width:1180px;margin:0 auto;padding:20px 24px 80px}
.bar{position:sticky;top:0;z-index:5;background:#F5F7FB;padding:10px 0;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.bar button,.pick button,.mob{border:1px solid #CBD5E1;background:#fff;border-radius:999px;padding:6px 12px;font:600 13px Inter;cursor:pointer}
.bar button[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}
.sum{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 16px}.sum a{text-decoration:none;color:inherit}
.st{display:inline-flex;align-items:center;gap:4px;border-radius:999px;padding:2px 10px;font:600 12px/20px Inter;white-space:nowrap}
.st-draft{background:#F1F5F9;color:#475569}.st-in-review{background:#FFFAEB;color:#B54708}.st-revisions{background:#FEF3F2;color:#B42318}.st-approved{background:#ECFDF3;color:#067647}
.sec{background:#fff;border:1px solid #E2E8F0;border-radius:16px;margin-bottom:18px;overflow:hidden}
.sec>header{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:1px solid #E2E8F0}
.sec h2{margin:0;font:400 20px/28px "Cal Sans",Inter,sans-serif}.muted{color:#64748B}
.pick{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:12px 18px;border-top:1px solid #E2E8F0;background:#FAFBFD}
.pick button[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}
.pick textarea{flex-basis:100%;min-height:44px;border:1px solid #CBD5E1;border-radius:10px;padding:8px 10px;font:13px Inter}
.saved{font-size:12px;color:#067647}
.pvw{padding:16px 18px;background:var(--color-bg-primary);color:var(--color-text-primary);font-family:var(--font-body)}
.pvw h4{margin:14px 0 8px;font:600 12px/16px Inter;text-transform:uppercase;letter-spacing:.04em;color:var(--color-text-tertiary)}
.pvw code,.pvw [data-css]{font:12px var(--font-code);color:var(--color-text-tertiary)}
.swg{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.sw{display:grid;grid-template-columns:28px 1fr;gap:2px 8px;align-items:center;font-size:12px}.sw i{grid-row:span 2;width:28px;height:28px;border-radius:8px;border:1px solid var(--color-border-tertiary,#e5e5e5)}
.cg{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px}.ct{border-radius:10px;padding:10px 12px;border:1px solid var(--color-border-tertiary,#e5e5e5);display:grid;gap:2px}
.ct small{font-size:12px}.cr.bad{color:#B42318}
.ty{display:grid;grid-template-columns:220px 1fr;gap:12px;align-items:center;padding:8px 0;border-bottom:1px dashed var(--color-border-tertiary,#e5e5e5)}
.tyl{display:grid}.tyl small{font-size:12px;color:var(--color-text-tertiary)}
.rg{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:12px}.rd{display:grid;gap:4px;font-size:12px}
.rd i{height:56px;background:var(--color-bg-secondary);border:1px solid var(--color-border-secondary,#d4d4d4)}
.sp{display:grid;gap:6px}.spr{display:grid;grid-template-columns:200px auto 1fr;gap:10px;align-items:center;font-size:12px}
.spr i{height:12px;background:var(--color-action-primary,#3468D7);border-radius:2px;display:block}
.ctl{display:flex;gap:10px;align-items:flex-end}.ctl span{display:inline-flex;align-items:center;border:1px solid var(--color-border-secondary,#d4d4d4);border-radius:var(--radius-control);font-size:13px}
.gr{display:grid;grid-template-columns:repeat(12,1fr);height:60px;background:var(--color-bg-secondary)}.gr i{background:rgba(52,104,215,.18)}
.wd{display:grid;grid-template-columns:auto 90px 60px;gap:10px;align-items:center;font-size:12px;margin:4px 0}.wd i{height:10px;background:var(--color-action-primary,#3468D7);display:block;border-radius:2px}
.elg{display:flex;gap:24px;padding:12px;background:var(--color-bg-secondary);border-radius:12px}
.el{width:160px;height:90px;background:var(--color-bg-primary);border-radius:var(--radius-card);display:grid;place-items:center;font-size:13px}
.blg{display:flex;gap:12px;flex-wrap:wrap}.bl{position:relative;width:200px;height:90px;border-radius:12px;overflow:hidden}
.blbg{position:absolute;inset:0;background:repeating-linear-gradient(45deg,#3468D7 0 12px,#FDB022 12px 24px,#fff 24px 36px)}
.blf{position:absolute;inset:18px;border-radius:10px;background:rgba(255,255,255,.35);display:grid;place-items:center;font-size:12px}
.tf{display:flex;gap:14px;align-items:center;margin:8px 0}.fb{height:36px;padding:0 14px;border-radius:var(--radius-control);border:1px solid var(--color-border-secondary,#d4d4d4);background:var(--color-bg-primary);color:inherit;font:600 13px Inter;outline:var(--focus-width) solid var(--color-focus-ring,#262626);outline-offset:var(--focus-offset)}
.hit{width:var(--touch-min);height:var(--touch-min);border:1px dashed #E11D48;display:grid;place-items:center}.hit i{width:16px;height:16px;background:var(--color-fg-secondary,#525252);border-radius:3px}
.mo{display:grid;gap:8px}.mor{display:grid;grid-template-columns:140px 70px 1fr;gap:10px;align-items:center;font-size:12px}
.track{height:12px;background:var(--color-bg-secondary);border-radius:6px;position:relative}.track i{position:absolute;left:0;top:0;width:12px;height:12px;border-radius:6px;background:var(--color-action-primary,#3468D7);transition-property:left}
.mo.run .track i{left:calc(100% - 12px)}
.icr{display:flex;gap:14px;align-items:center;margin:6px 0}.icr>b{width:44px;font-size:12px}
.ic{display:inline-grid;color:var(--color-fg-secondary,#525252)}.ic svg{width:100%;height:100%;stroke-width:var(--sw)}
"""

PAGE_JS = r"""
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
let db=null,uid=null; const ST={};
function hex(c){const m=c.match(/\d+(\.\d+)?/g);return m?m.slice(0,3).map(Number):[0,0,0]}
function lum(rgb){const a=rgb.map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2]}
function fill(){const pv=$(".pvroot"); const cs=getComputedStyle(pv);
  $$("[data-css]").forEach(e=>{e.textContent=cs.getPropertyValue(e.dataset.css).trim()||"—";});
  $$(".ct").forEach(e=>{const s=getComputedStyle(e);const a=lum(hex(s.color)),b=lum(hex(s.backgroundColor));const r=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
    const c=e.querySelector(".cr");c.textContent=r.toFixed(2).replace(".",",")+":1";c.classList.toggle("bad",r<4.5);});}
function mode(k,v){$(".pvroot").setAttribute("data-"+k,v);$$(`[data-m="${k}"]`).forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.v===v)));fill();}
$$("[data-m]").forEach(b=>b.onclick=()=>mode(b.dataset.m,b.dataset.v));
$$(".mob").forEach(b=>b.onclick=()=>{const m=b.closest(".mo");m.classList.toggle("run");});
function paint(){$$(".pick button").forEach(b=>b.setAttribute("aria-pressed",String(ST[b.dataset.k]?.to===b.dataset.to)));
  $$("[data-saved]").forEach(e=>{const x=ST[e.dataset.saved];e.textContent=x&&x.to?"Đã lưu: "+({"draft":"Nháp","in-review":"Đang duyệt","revisions":"Cần sửa","approved":"Đã duyệt"}[x.to])+" — Claude áp vào repo + Figma":"";});
  $$("[data-note]").forEach(t=>{if(document.activeElement!==t&&ST[t.dataset.note]) t.value=ST[t.dataset.note].note||"";});}
async function save(k){const x={...ST[k],at:Date.now(),by:uid}; try{localStorage.setItem("fst-"+k,JSON.stringify(x))}catch(e){} if(db) try{await db.doc("status/"+k).set(x)}catch(e){}}
$$(".pick button").forEach(b=>b.onclick=()=>{const k=b.dataset.k; ST[k]={...(ST[k]||{}),to:ST[k]?.to===b.dataset.to?null:b.dataset.to}; paint(); save(k);});
$$("[data-note]").forEach(t=>t.oninput=()=>{const k=t.dataset.note; ST[k]={...(ST[k]||{}),note:t.value}; clearTimeout(t._t); t._t=setTimeout(()=>save(k),500);});
$$("[data-note]").forEach(t=>{try{const x=JSON.parse(localStorage.getItem("fst-"+t.dataset.note)||"null"); if(x) ST[t.dataset.note]=x;}catch(e){}});
paint(); fill(); addEventListener("load",fill);
(async()=>{ if(!window.claude?.use) return; const [d,u]=await Promise.all([claude.use("db"),claude.use("user")]); if(!d) return; db=d;
  try{uid=u?await u.id():null}catch(e){}
  db.collection("status").onSnapshot(sn=>{sn.docs.forEach(x=>{const v=x.data(); if(v&&(!ST[x.id]||(v.at||0)>=(ST[x.id].at||0))) ST[x.id]=v;}); paint();},()=>{});})();
"""


def main():
    summ = "".join(f'<a href="#{r["key"]}"><span class="st st-{r["status"]}">{E(r["name"])} · {E(LBL[r["status"]])}</span></a>' for r in ROWS)
    doc = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Foundations DS v2 · trạng thái</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cal+Sans&display=swap">
<style>{CSS}{PAGE_CSS}</style></head><body>
<div class="band">{MARK}<div><h1>Foundations DS v2 — trạng thái từng mục</h1>
<p>Xem thử dựng bằng tokens.css thật · chọn trạng thái cho từng mục · Claude áp vào foundations.md và nhãn trên Figma</p></div></div>
<div class="wrap pvroot" data-theme="light" data-platform="web">
<div class="bar"><b>Xem thử:</b><button data-m="theme" data-v="light" aria-pressed="true">Light</button><button data-m="theme" data-v="dark" aria-pressed="false">Dark</button>
<button data-m="platform" data-v="web" aria-pressed="true">Web</button><button data-m="platform" data-v="mobile" aria-pressed="false">Mobile</button></div>
<p class="muted">Component chỉ coi một mục là chuẩn khi mục đó <b>Đã duyệt</b>. Mục chưa duyệt vẫn dùng được, trang review component ghi "chưa duyệt".</p>
<div class="sum">{summ}</div>
{"".join(section(r) for r in ROWS)}
</div><script>{PAGE_JS}</script></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    print(f"Đã sinh {OUT.relative_to(ROOT)} ({len(doc) // 1024} KB) · {len(ROWS)} mục")


if __name__ == "__main__":
    main()
