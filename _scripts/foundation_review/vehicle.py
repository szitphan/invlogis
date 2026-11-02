#!/usr/bin/env python3
"""SPEC trang review Foundations · Phương tiện. Dựng: python3 _scripts/foundation_review/build.py vehicle

Ảnh là ảnh thật trong design-system/assets/vehicles/: thu nhỏ bằng PIL, nén WebP, nhúng base64 một lần qua lớp CSS `.vi-<tên>`.
Số đếm (ảnh, nhóm, trạng thái component) đọc lúc dựng; tương phản tính từ tokens.css, không chép tay.
"""
import base64
import io
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402
from PIL import Image  # noqa: E402

ROOT = kit.ROOT
A = ROOT / "design-system/assets/vehicles"
V = json.loads((ROOT / "design-system/handoff/vehicles.json").read_text())
GROUPS = {g["key"]: g for g in V["groups"]}
DELTA = V["tenants"]["delta"]["vehicles"]
SLUGS = ["vehicle-thumb", "vehicle-card", "vehicle-option-card", "tyre-layout", "map-marker", "combo-figure", "combo-slots", "combo-text", "container-slot"]
APP = ROOT / "design-system/components/application"
STALE = sum(1 for s in SLUGS if re.search(r"^status: stale", (APP / f"{s}.md").read_text(), flags=re.M))
APPROVED = sum(1 for s in SLUGS if re.search(r"^status(_prev)?: approved", (APP / f"{s}.md").read_text(), flags=re.M))
PNG = len(list(A.glob("*.png")))
NO_TOP = [g["key"] for g in V["groups"] if g["image"] and "top" not in g["views"]]
NO_TOP_NAMES = sum(1 for x in DELTA if x["group"] in NO_TOP)
NO_TOP_TRUCK = sum(1 for x in DELTA if x["group"] in NO_TOP and x["group"].startswith("truck"))
ALT_NAMES = sum(1 for x in DELTA if x["style"] != "Default")
Q_TOKENS = sorted(set(re.findall(r"--(vehicle-q-[\w-]+):", kit.TCSS)))


# ---------- tương phản từ tokens.css ----------
def _block(sel):
    i = kit.TCSS.index(sel)
    return dict(re.findall(r"(--[\w-]+):\s*([^;]+);", kit.TCSS[i:kit.TCSS.index("\n}", i)]))


_R, _L, _D, _W = _block(":root {"), _block(':root, [data-theme="light"]'), _block('[data-theme="dark"]'), _block(':root, [data-platform="web"]')


def tok(name, mode):
    m = _L if mode == "light" else _D
    x = "--" + name.replace("/", "-")
    x = m.get(x) or _W.get(x) or _R.get(x)
    while x and x.startswith("var("):
        k = x[4:-1].split(",")[0].strip()
        x = m.get(k) or _W.get(k) or _R.get(k)
    return x


def _lum(h):
    h = h.lstrip("#")[:6]
    f = lambda x: x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4
    r = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return .2126 * f(r[0]) + .7152 * f(r[1]) + .0722 * f(r[2])


def ratio(a, b):
    x, y = _lum(a), _lum(b)
    return (max(x, y) + .05) / (min(x, y) + .05)


def rtag(a, b, minimum=3.0):
    r = ratio(a, b)
    return f'<span class="vh-r {"ok" if r >= minimum else "bad"}">{f"{r:.2f}".replace(".", ",")}:1</span>'


# màu bản đồ giả lập, lấy từ design/_lab/lab-map.html (.mp.light, .mp.dark); nhà cung cấp thật có thể khác
LAND = {"light": "#eef0f3", "dark": "#15171b"}
ROAD = {"light": "#ffffff", "dark": "#262930"}


# ---------- ảnh ----------
_SHEET = {}


def _emb(name, w):
    if name in _SHEET:
        return
    im = Image.open(A / f"{name}.png").convert("RGBA")
    ow, oh = im.size
    if ow > w:
        im = im.resize((w, max(1, round(oh * w / ow))), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "WEBP", quality=72, method=5)
    _SHEET[name] = (ow, oh, base64.b64encode(b.getvalue()).decode())


for n in ("t02", "n05", "t03", "g-truck-l", "n26", "n03", "t01", "n01", "t06", "c40", "t07", "t04", "t08"):
    _emb(f"{n}-q", 480 if n == "t02" else 300)
for n, m in (("t02", 7), ("n01", 6.4), ("t01", 12.4), ("n03", 12.4), ("n04", 13.9), ("t06", 6.06), ("c40", 12.19), ("c45", 13.72), ("t07", 13.7)):
    _emb(f"{n}-s", int(m * 32))
for n in ("t02", "n05", "t01", "n03", "n01", "t03"):
    _emb(f"{n}-top", 56 if n in ("t02", "t03", "n05") else 44)
for n in ("c45", "t07"):
    _emb(f"{n}-top", 56)
IMG_CSS = "".join(f".vi-{k}{{background-image:url(data:image/webp;base64,{b});aspect-ratio:{w}/{h}}}" for k, (w, h, b) in _SHEET.items())


def vi(name, style=""):
    return f'<i class="vi vi-{name}" role="img" aria-label="{name}" style="{style}"></i>'


# ---------- component dựng từ biến ----------
def thumb(image, crop, size="sm"):
    cell = {"xs": "--size-4xl", "sm": "--size-6xl", "md": "--size-7xl"}[size]
    place = {"head": "height:86%;bottom:4%;right:0", "wheels": "height:50%;bottom:12%;left:0", "whole": "height:80%;bottom:8%;left:50%;transform:translateX(-50%)"}[crop]
    return f'<span class="vh-th vh-th-{size}" style="width:var({cell});height:var({cell})">{vi(image + "-q", "position:absolute;" + place)}</span>'


def chip(cls, text):
    return f'<span class="tp-chip {cls}">{text}</span>'


def card(plate="51C-482.15", model="Hino 700 · đầu kéo 2 cầu", odo="182.450 km · 41%", loc="Cảng Cát Lái", driver="Nguyễn Văn Hoà", route="Cát Lái → Long Hậu", status=("tp-b", "Đang hoạt động"), img="t02-q", w="100%", mh="var(--vehicle-q-sm-h)", mw="var(--size-11xl)"):
    return (f'<div class="tp-card vh-card" style="width:{w};max-width:100%"><div class="vh-cbody"><div class="vh-ctext"><div class="type-heading vh-1">{plate}</div><div class="type-body tp-sub vh-1">{model}</div>'
            f'<div class="vh-ln type-caption tp-sub">{kit.icon("gauge", "tp-ic-md vh-ic")}<span>{odo}</span></div><div class="vh-ln type-caption tp-sub">{kit.icon("map-pin", "tp-ic-md vh-ic")}<span>{loc}</span></div></div>'
            f'<div class="vh-media" style="width:{mw};height:{mh}">{vi(img, "position:absolute;right:0;bottom:0;height:125%")}</div><span class="vh-badge">{chip(*status)}</span></div>'
            f'<div class="vh-cfoot type-caption tp-sub"><span class="vh-ln">{kit.icon("user-round", "tp-ic-md vh-ic")}<span>{driver}</span></span><span class="vh-ln">{kit.icon("route", "tp-ic-md vh-ic")}<span>{route}</span></span></div></div>')


def option(plate, meta, img, crop, status, selected=False, disabled=False, w="100%"):
    dot = '<span class="vh-rd on"></span>' if selected else '<span class="vh-rd"></span>'
    return (f'<div class="vh-opt{" sel" if selected else ""}{" dis" if disabled else ""}" style="width:{w};max-width:100%">{thumb(img, crop, "sm")}<div style="flex:1;min-width:0"><div class="type-heading vh-1">{plate}</div>'
            f'<div class="vh-sub">{chip(*status)}<span class="type-caption tp-sub vh-1 vh-meta">{meta}</span></div></div>{dot}</div>')


def slot(size, number, status_cls, status, reefer=None, cls=""):
    rf = chip("tp-b", reefer) if reefer else ""
    return f'<div class="vh-slot {cls}"><div class="type-caption tp-sub">{size}</div><div class="type-code vh-1">{number}</div><div class="vh-sub">{chip(status_cls, status)}{rf}</div></div>'


def combo(cfg, s="--size-xl"):
    """Combo Figure theo design-system/components/application/combo-figure.md: mâm kéo 19% từ đuôi, cách đầu mooc 1 m, đáy thẳng hàng."""
    tr, lt = ("t02-s", 7.0)
    cfgs = {"none": (None, 0, []), "empty": ("n03-s", 12.4, []), "1x20": ("n01-s", 6.4, [("t06-s", 6.06, "mid")]), "2x20": ("n03-s", 12.4, [("t06-s", 6.06, 0.15), ("t06-s", 6.06, 6.29)]),
            "1x40": ("t01-s", 12.4, [("c40-s", 12.19, 0.15)]), "1x45": ("n04-s", 13.9, [("c45-s", 13.72, 0.1)]), "1x45r": ("n04-s", 13.9, [("t07-s", 13.7, 0.1)]), "1x20c": ("n03-s", 12.4, [("t06-s", 6.06, "mid")])}
    mooc, lm, boxes = cfgs[cfg]
    left_tr = max(0.0, lm - .19 * lt - 1)
    total = left_tr + lt
    parts = []
    if mooc:
        parts.append(vi(mooc, f"position:absolute;left:0;bottom:0;width:calc(var(--vh-s) * {lm})"))
        for img, l, off in boxes:
            x = (lm - l) / 2 if off == "mid" else (lm - l - off)
            parts.append(vi(img, f"position:absolute;left:calc(var(--vh-s) * {x:.2f});bottom:calc(var(--vh-s) * 1.5);width:calc(var(--vh-s) * {l})"))
    parts.append(vi(tr, f"position:absolute;left:calc(var(--vh-s) * {left_tr:.2f});bottom:0;width:calc(var(--vh-s) * {lt})"))
    h = 4.5 if boxes else 3.9
    return f'<div class="vh-combo" style="--vh-s:var({s});width:calc(var(--vh-s) * {total:.2f});height:calc(var(--vh-s) * {h})">{"".join(parts)}</div>'


def dot(state):
    return f'<span class="vh-dot vh-st-{state}"></span>'


def label(text, sub=""):
    return f'<span class="vh-lbl type-caption-strong">{text}{f" · {sub}" if sub else ""}</span>'


def marker(x, y, state, plate, rot=0, kind="vehicle", s=8, sub=""):
    f = "t02-top" if kind != "trailer" else "t01-top"
    fig = ""
    if kind == "combo":
        fig = (vi("t01-top", f"position:absolute;left:50%;top:{round(6 * s)}px;width:{2.5 * s}px;margin-left:{-1.25 * s}px") + vi("t02-top", f"position:absolute;left:50%;top:0;width:{2.5 * s}px;margin-left:{-1.25 * s}px"))
        hh = round((7 + 12.4 - 1) * s)
    else:
        fig = vi(f, f"position:absolute;left:50%;top:0;width:{2.5 * s}px;margin-left:{-1.25 * s}px")
        hh = round((7 if kind == "vehicle" else 12.4) * s)
    op = "opacity:.5;" if state == "off" else ""
    return (f'<span class="vh-mk" style="left:{x}%;top:{y}%"><span class="vh-mkf" style="width:{round(2.5 * s) + 12}px;height:{hh}px;transform:rotate({rot}deg);{op}">{fig}</span>'
            f'<span class="vh-dot vh-st-{state}" style="position:absolute;left:50%;top:-4px"></span>{label(plate, sub)}</span>')


def dotm(x, y, state, plate, sub=""):
    return f'<span class="vh-mk vh-dm" style="left:{x}%;top:{y}%">{dot(state)}{label(plate, sub)}</span>'


def cluster(x, y, n, size="md"):
    return f'<span class="vh-cl vh-cl-{size} type-caption-strong" style="left:{x}%;top:{y}%">{n}</span>'


def mapbox(inner, h=240):
    return (f'<div class="vh-map" style="height:{h}px"><i class="vh-rd1"></i><i class="vh-rd2"></i><i class="vh-rd3"></i><i class="vh-park"></i>{inner}</div>')


AX = {"tractor-6x4": [("s", 1), ("l", 2), ("l", 2)], "tractor-4x2": [("s", 1), ("l", 2)], "trailer-3ax": [("l", 2), ("l", 2), ("l", 2)], "truck-6x2": [("s", 1), ("s", 1), ("l", 2)]}


def tyre_layout(key, states=None, scale=1.0):
    """Sơ đồ lốp nhìn từ trên: thân 70, lốp 16×30 cách thân 6, lốp kép ngoài lệch thêm 19 (tyre-layout.md)."""
    states = states or {}
    axes = AX[key]
    H = 58 + 62 * len(axes) + 44
    out, n = [], 0
    for i, (kind, per) in enumerate(axes):
        y = 44 + 62 * i
        out.append(f'<i class="vh-ax" style="top:{y + 14}px"></i>')
        for side in ("L", "R"):
            for k in range(per):
                n += 1
                base = 65 - 6 - 16 - 19 * k if side == "L" else 135 + 6 + 19 * k
                out.append(f'<span class="vh-ty vh-ty-{kind} vh-ty-{states.get(n, "d")} type-chip-sm-strong" style="left:{base}px;top:{y}px">{n}</span>')
    n += 1
    out.append(f'<span class="vh-ty-spare type-chip-sm-strong" style="top:{H - 34}px">{n}</span>')
    cab = '<span class="vh-cab type-hint">Đầu xe</span>' if not key.startswith("trailer") else '<span class="vh-kp"></span>'
    return f'<div class="vh-tyre" style="height:{H}px;zoom:{scale}"><span class="vh-body" style="height:{H - 44}px"></span>{cab}{"".join(out)}</div>'


def ba(a, b, la="Hiện tại", lb="Đề xuất", one=False):
    return f'<div class="vh-ba{" vh-ba1" if one else ""}"><div class="vh-cur"><div class="vh-cap">{la}</div>{a}</div><div class="vh-prop"><div class="vh-cap">{lb}</div>{b}</div></div>'


def plain_panes(fn, **kw):
    return kit.panes(fn, **kw)


# ---------- màn thật ----------
def overlay(_body):
    logo = kit.mini_mark()
    nav = lambda ic, x, on="": f'<div class="tp-nav {on}">{kit.icon(ic)}<span class="type-label">{x}</span></div>'
    row = lambda img, crop, plate, typ, st, drv, loc: (f'<tr><td><div class="vh-rowc">{thumb(img, crop, "xs")}<div><div class="type-code">{plate}</div><div class="type-caption tp-sub">{typ}</div></div></div></td><td><span class="type-body">{drv}</span></td><td><span class="type-caption tp-sub">{loc}</span></td><td>{chip(*st)}</td></tr>')
    table = ("<table class='tp-tb'><thead><tr><th><span class='type-caption-caps'>Phương tiện</span></th><th><span class='type-caption-caps'>Lái xe</span></th><th><span class='type-caption-caps'>Vị trí</span></th><th><span class='type-caption-caps'>Trạng thái</span></th></tr></thead><tbody>"
             + row("t02", "head", "51C-482.15", "Đầu kéo 2 cầu sau", ("tp-b", "Đang hoạt động"), "Nguyễn Văn Hoà", "Cảng Cát Lái")
             + row("t03", "head", "51D-120.77", "Xe tải 2 trục vừa", ("tp-g", "Sẵn sàng hoạt động"), "Trần Quốc Việt", "Kho Tân Vạn")
             + row("n03", "wheels", "51R-091.44", "Mooc 40ft 3 giàn", ("tp-y", "Đang sửa chữa"), "Chưa gán lái xe", "Xưởng Đình Vũ · tới 30/10")
             + "</tbody></table>")
    web = (f'<div class="tp-f tp-prop tp-web" data-platform="web"><aside class="tp-side"><div class="tp-logo">{logo}</div><div class="type-caption-caps tp-grp">Vận hành</div>{nav("clipboard-list", "Lệnh vận tải")}{nav("truck", "Phương tiện", "on")}{nav("map", "Theo dõi đội xe")}{nav("user-round", "Lái xe")}</aside>'
           f'<div class="tp-main"><div class="tp-top"><div><div class="type-title-1">Phương tiện</div><div class="type-body tp-sub">Đội xe, mooc, thiết bị của công ty.</div></div><span class="tp-btn">{kit.icon("plus")}<span class="type-label">Thêm phương tiện</span></span></div>'
           f'<div class="vh-g3">{card()}{card(plate="51D-120.77", model="Xe tải Isuzu 7 tấn", odo="96.210 km · 73%", loc="Kho Tân Vạn", driver="Trần Quốc Việt", route="Tân Vạn → Long Thành", status=("tp-g", "Sẵn sàng hoạt động"), img="t03-q")}{card(plate="50H-338.02", model="Đầu kéo 1 cầu sau", odo="240.120 km · 18%", loc="Xưởng Đình Vũ · tới 30/10", driver="Chưa gán lái xe", route="—", status=("tp-y", "Đang sửa chữa"), img="n05-q")}</div>'
           f'<div class="tp-card">{table}</div></div></div>')
    combo_det = (f'<div class="tp-f tp-prop tp-webs" data-platform="web"><div class="tp-main"><div class="tp-top"><div><div class="type-code tp-sub">LVT-2026-0412</div><div class="type-title-1">Chi tiết lệnh vận tải</div></div>{chip("tp-b", "Đang chạy")}</div>'
                 f'<div class="tp-card"><div class="type-title-3">Tổ hợp</div><div class="vh-figbox">{combo("2x20")}</div><div class="vh-slots">{slot("20&#39;", "TCLU 482915 3", "tp-g", "Có hàng")}{slot("20&#39; · LVT-0450", "MSKU 104422 7", "tp-b", "Vỏ rỗng")}</div></div></div></div>')
    form = (f'<div class="tp-f tp-prop tp-webs" data-platform="web"><div class="tp-main"><div class="type-title-1">Chọn đầu kéo</div><div class="tp-card" style="padding:0;gap:0">{option("51C-482.15", "Đầu kéo 2 cầu · Nguyễn Văn Hoà", "t02", "head", ("tp-g", "Sẵn sàng hoạt động"), selected=True)}{option("50H-338.02", "Đầu kéo 1 cầu · Chưa gán lái xe", "n05", "head", ("tp-b", "Đang hoạt động"))}{option("51C-771.09", "Xưởng Đình Vũ · tới 30/10", "t02", "head", ("tp-y", "Đang sửa chữa"), disabled=True)}</div></div></div>')
    mp = (f'<div class="tp-f tp-prop tp-webs" data-platform="web"><div class="tp-main"><div class="type-title-1">Theo dõi đội xe</div>'
          + mapbox(marker(30, 12, "mov", "51C-482.15", 35) + dotm(62, 26, "stop", "51D-120.77") + dotm(74, 52, "idle", "50H-338.02") + dotm(46, 74, "off", "51C-771.09", "10:40") + dotm(18, 72, "alert", "51F-908.31") + cluster(88, 16, 24), 360) + "</div></div>")
    app_list = f'<div class="tp-f tp-prop tp-app" data-platform="mobile"><div class="tp-appbar"><div class="type-title-2" style="flex:1">Đội xe</div></div><div class="tp-pad">{card()}{card(plate="51D-120.77", model="Xe tải Isuzu 7 tấn", odo="96.210 km · 73%", loc="Kho Tân Vạn", driver="Trần Quốc Việt", route="Tân Vạn → Long Thành", status=("tp-g", "Sẵn sàng hoạt động"), img="t03-q")}</div></div>'
    app_cmd = f'<div class="tp-f tp-prop tp-app" data-platform="mobile"><div class="tp-appbar"><div style="flex:1"><div class="type-title-2">Lệnh của tôi</div><div class="type-caption tp-sub">LVT-2026-0412</div></div></div><div class="tp-pad"><div class="tp-card"><div class="type-title-3">Cát Lái → KCN Long Hậu</div><div class="vh-figbox">{combo("1x40", "--size-md")}</div>{slot("40&#39;", "TCLU 482915 3", "tp-g", "Có hàng")}</div><div class="tp-card"><div class="type-title-3">Lốp xe</div><div style="display:flex;justify-content:center">{tyre_layout("tractor-6x4", {4: "w", 7: "e", 2: "sel"})}</div><div class="type-caption tp-sub">Vị trí 4 đến hạn thay. Vị trí 7 hỏng, cần thay.</div></div></div></div>'
    app_map = ('<div class="tp-f tp-prop tp-app" data-platform="mobile"><div class="tp-appbar"><div class="type-title-2" style="flex:1">Theo dõi đội xe</div></div><div class="tp-pad">'
               + mapbox(dotm(26, 18, "mov", "51C-482.15") + dotm(64, 34, "idle", "50H-338.02") + dotm(22, 66, "stop", "51D-120.77") + cluster(78, 72, 12), 300) + card() + "</div></div>")
    return (f'<div class="tp-h">Web <small>· màn mẫu danh sách đội xe, khung 1280, menu 240</small></div><div class="tp-scroll"><div class="tp-row">{web}</div></div>'
            f'<div class="tp-h">Web <small>· màn mẫu chi tiết Lệnh, biểu mẫu chọn xe, bản đồ</small></div><div class="tp-scroll"><div class="tp-row">{combo_det}{form}{mp}</div></div>'
            f'<div class="tp-h">App <small>· đội xe, thẻ Lệnh và sơ đồ lốp, bản đồ (rộng 393)</small></div><div class="tp-scroll"><div class="tp-row">{app_list}{app_cmd}{app_map}</div></div>')


CSS = IMG_CSS + r"""
.vi{display:block;background-size:contain;background-repeat:no-repeat;background-position:center bottom;filter:var(--vh-contour)}
.pane,.vh-cur,.vh-prop,.tp-f{--vh-rxs:var(--radius-sm);--vh-rsm:var(--radius-md);--vh-rmd:var(--radius-lg);--vh-ibg:var(--color-bg-secondary);--vh-contour:none;--vh-sic:var(--color-text-disabled);--vh-cshadow:none;--vh-cbd:var(--color-border-secondary);
 --vh-stop:var(--color-text-disabled);--vh-off:var(--color-border-primary);--vh-alert:var(--color-border-error);--vh-tnum:var(--color-text-inverse);--vh-tsel:var(--color-bg-info-solid);--vh-terr:var(--color-border-error);--vh-tsteer:var(--color-text-tertiary);--vh-lshadow:none}
.vh-prop,.tp-f.tp-prop{--vh-rxs:var(--radius-inner);--vh-rsm:var(--radius-inner);--vh-rmd:var(--radius-inner);--vh-sic:var(--color-fg-tertiary);--vh-cshadow:var(--shadow-xs);--vh-cbd:var(--shadow-xs-border);
 --vh-stop:var(--color-fg-tertiary);--vh-off:var(--color-fg-quaternary);--vh-alert:var(--color-bg-error-solid);--vh-tnum:var(--color-text-white);--vh-terr:var(--color-bg-error-solid);--vh-tsteer:var(--color-fg-tertiary);--vh-lshadow:var(--shadow-sm);
 --vh-contour:drop-shadow(0 0 .6px var(--vh-ctc));--vh-ctc:var(--color-fg-quaternary)}
[data-theme="dark"] .vh-prop,[data-theme="dark"] .tp-f.tp-prop{--vh-ibg:var(--color-bg-quaternary);--vh-ctc:var(--color-fg-tertiary)}
[data-theme="dark"]{--vh-land:#15171b;--vh-zone:#1c1f24;--vh-parkc:#15211a;--vh-road:#262930;--vh-case:#1d1f24}
[data-theme="light"],:root{--vh-land:#eef0f3;--vh-zone:#e3e5ea;--vh-parkc:#dfece3;--vh-road:#ffffff;--vh-case:#dadde3}
.vh-r{font:600 10.5px/14px "JetBrains Mono";padding:1px 5px;border-radius:5px;white-space:nowrap}.vh-r.ok{background:#DCFCE7;color:#14532D}.vh-r.bad{background:#FEE2E2;color:#7F1D1D}
.vh-ba{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-xl)}.vh-cap{font:600 11px/14px Inter;color:var(--color-text-tertiary);margin-bottom:6px}
.vh-ba1{grid-template-columns:minmax(0,1fr)}.vh-1{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vh-th{position:relative;display:inline-block;overflow:hidden;background:var(--vh-ibg);flex:none}.vh-th-xs{border-radius:var(--vh-rxs)}.vh-th-sm{border-radius:var(--vh-rsm)}.vh-th-md{border-radius:var(--vh-rmd)}
.tp-card.vh-card{padding:0;gap:0;overflow:hidden;box-shadow:var(--vh-cshadow);border-color:var(--vh-cbd);position:relative}
.vh-cbody{display:flex;gap:var(--space-lg);padding:var(--space-xl) 0 var(--space-lg) var(--space-xl);position:relative}.vh-ctext{flex:1;min-width:0;display:grid;gap:2px;align-content:start;padding-top:22px}
.vh-media{position:relative;overflow:hidden;flex:none;align-self:flex-end}.vh-badge{position:absolute;right:var(--space-lg);top:var(--space-lg)}
.vh-cfoot{display:flex;flex-wrap:wrap;gap:4px var(--space-lg);padding:var(--space-md) var(--space-xl);border-top:1px solid var(--color-border-secondary)}
.vh-ln{display:flex;gap:var(--space-xs);align-items:flex-start;min-width:0}.vh-ic{color:var(--vh-sic)}
.vh-g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--grid-gutter)}
.vh-rowc{display:flex;gap:var(--space-lg);align-items:center}
.vh-opt{display:flex;align-items:center;gap:var(--space-lg);padding:var(--space-lg) var(--space-xl);border-bottom:1px solid var(--color-border-secondary);background:var(--color-bg-primary)}.vh-opt.sel{background:var(--color-bg-selected)}.vh-opt.dis .type-heading{color:var(--color-text-disabled)}
.vh-sub{display:flex;flex-wrap:wrap;gap:var(--space-xs) var(--space-md);align-items:center;margin-top:2px}.vh-meta{min-width:0;flex:1 1 140px}
.vh-rd{width:20px;height:20px;border-radius:50%;border:1px solid var(--color-border-primary);flex:none;background:var(--color-bg-primary)}.vh-rd.on{border:6px solid var(--color-action-primary)}
.vh-slots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-md)}.vh-slot{border:1px solid var(--color-border-secondary);border-radius:var(--radius-inner);padding:var(--space-md) 10px;display:grid;gap:var(--space-xs);min-width:0;background:var(--color-bg-primary)}
.vh-combo{position:relative;flex:none}.vh-figbox{background:var(--vh-ibg);border-radius:var(--radius-inner);padding:var(--space-lg);display:flex;justify-content:center;overflow:hidden}
.vh-map{position:relative;overflow:hidden;background:var(--vh-land);border-radius:var(--radius-inner);min-width:0}.vh-map>i{position:absolute;display:block}
.vh-rd1{left:-10%;right:-10%;top:42%;height:14px;background:var(--vh-road);box-shadow:0 0 0 1px var(--vh-case);transform:rotate(-14deg)}.vh-rd2{top:-20%;bottom:-20%;left:38%;width:10px;background:var(--vh-road);box-shadow:0 0 0 1px var(--vh-case);transform:rotate(18deg)}.vh-rd3{top:-20%;bottom:-20%;left:72%;width:7px;background:var(--vh-road);box-shadow:0 0 0 1px var(--vh-case);transform:rotate(-8deg)}.vh-park{left:4%;top:62%;width:24%;height:26%;background:var(--vh-parkc);border-radius:10px}
.vh-mk{position:absolute;display:inline-flex;flex-direction:column;align-items:center;gap:4px;transform:translateX(-50%)}.vh-mkf{position:relative;display:block;transform-origin:50% 50%}.vh-mk .vh-dot{margin-left:-6px}.vh-dm .vh-dot{margin-left:0}
.vh-dot{display:block;width:var(--space-lg);height:var(--space-lg);border-radius:50%;border:2px solid var(--color-fg-white);box-sizing:border-box;flex:none;box-shadow:var(--vh-lshadow)}
.vh-st-mov{background:var(--color-bg-success-solid)}.vh-st-stop{background:var(--vh-stop)}.vh-st-idle{background:var(--color-bg-warning-solid)}.vh-st-off{background:var(--vh-off)}.vh-st-alert{background:var(--vh-alert)}.vh-st-sel{background:var(--color-bg-info-solid);outline:2px solid var(--color-focus-ring);outline-offset:1px}
.vh-lbl{background:var(--color-bg-primary);color:var(--color-text-primary);border:1px solid var(--color-border-secondary);border-radius:var(--radius-sm);padding:2px 6px;white-space:nowrap;box-shadow:var(--vh-lshadow)}
.vh-cl{position:absolute;transform:translateX(-50%);display:grid;place-items:center;border-radius:50%;background:var(--color-bg-primary_solid);color:var(--color-text-inverse);box-shadow:var(--vh-lshadow)}.vh-cl-md{width:36px;height:36px}
.vh-tyre{position:relative;width:200px;flex:none}.vh-body{position:absolute;left:65px;top:0;width:70px;background:var(--color-bg-secondary);border:1px solid var(--color-border-secondary);border-radius:var(--radius-sm)}
.vh-cab{position:absolute;left:66px;top:1px;width:68px;height:24px;background:var(--color-border-secondary);display:grid;place-items:center;color:var(--color-text-tertiary);border-radius:var(--radius-sm) var(--radius-sm) 0 0}.vh-kp{position:absolute;left:96px;top:10px;width:8px;height:8px;border-radius:50%;background:var(--color-fg-quaternary)}
.vh-ax{position:absolute;left:61px;width:78px;height:3px;background:var(--color-fg-quaternary)}
.vh-ty{position:absolute;width:var(--size-xl);height:30px;border-radius:var(--radius-xxs);display:grid;place-items:center;color:var(--vh-tnum)}.vh-ty-s{background:var(--vh-tsteer)}.vh-ty-l{background:var(--color-bg-primary_solid)}.vh-ty-d{color:var(--color-text-inverse)}
.vh-ty-w{background:var(--color-bg-warning-solid)}.vh-ty-e{background:var(--vh-terr)}.vh-ty-sel{background:var(--vh-tsel);outline:3px solid var(--color-focus-ring);outline-offset:0}
.vh-ty-spare{position:absolute;left:87px;width:26px;height:26px;border-radius:50%;border:1px dashed var(--color-text-tertiary);display:grid;place-items:center;color:var(--color-text-tertiary)}
.vh-tree{display:grid;gap:2px}.vh-tree>span{display:flex;justify-content:space-between;gap:var(--space-md);padding:var(--space-xs) var(--space-md);border-radius:var(--radius-sm)}.vh-tree .on{background:var(--color-bg-selected);font-weight:600}
.vh-frame{border:1px dashed var(--color-border-primary);border-radius:var(--radius-inner);position:relative;overflow:hidden;background:var(--color-bg-secondary)}.vh-over{outline:2px solid var(--color-border-error);outline-offset:-2px}
.vh-scale{display:flex;align-items:flex-end;gap:var(--space-lg);flex-wrap:wrap}.vh-col{display:grid;gap:var(--space-md);justify-items:start;min-width:0}
.vh-g17{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:var(--space-md)}.vh-case{border:1px solid var(--color-border-secondary);border-radius:var(--radius-inner);padding:var(--space-md);display:grid;gap:var(--space-xs);min-width:0;background:var(--color-bg-primary)}.vh-case .vh-combo{justify-self:start}
.vh-hbar{height:10px;border-radius:99px;background:var(--color-bg-tertiary);overflow:hidden}.vh-hbar i{display:block;height:100%;background:var(--color-fg-tertiary)}
@media(max-width:820px){.vh-ba{grid-template-columns:minmax(0,1fr)}.vh-slots{grid-template-columns:minmax(0,1fr)}}
"""

# ---------- bảng ----------
_st = {"ok": '<span class="st-ok">Giống</span>', "diff": '<span class="st-diff">Khác có lý do</span>', "gap": '<span class="st-gap">Mình thiếu</span>', "own": '<span class="st-own">Chỉ mình có</span>'}
CMP = [
    ("Ô ảnh vuông 32 · 48 · 64", "<code>Avatar</code> <code>size-8</code>, <code>size-12</code>, <code>size-16</code>; còn 24, 40, 56", "<code>size/4xl</code>, <code>size/6xl</code>, <code>size/7xl</code>", "ok", "Ba bậc trùng số; không cần 24, 40, 56"),
    ("Cách lấp ô ảnh", "<code>object-cover</code>: một luật", "<code>thumb_crop</code> head · wheels · whole", "diff", "Xe dài cắt giữa thì mất nhận dạng"),
    ("Nền ô ảnh", "<code>bg-tertiary</code>", "<code>color/bg/secondary</code>", "diff", "Xem <b>vh08</b>"),
    ("Bo ô vuông", "<code>rounded-md</code> 8, mọi cỡ", "<code>radius/sm</code> 6 · <code>radius/md</code> 8 · <code>radius/lg</code> 10", "diff", "Xem <b>vh04</b>"),
    ("Nét bao ảnh", "<code>contrastBorder</code>: <code>outline-[0.5px]</code> <code>outline-black/16</code>", "Không có", "gap", "Ảnh container trắng tan vào nền; xem <b>vh08</b>"),
    ("Ảnh lỗi", "<code>onError</code> về chữ cái hoặc placeholder", "Ô nền trống", "ok", "Cùng cách lùi về ô rỗng"),
    ("Chấm trạng thái trên ảnh", "<code>AvatarOnlineIndicator</code> <code>size-1.5</code>…<code>size-5</code>", "Chấm 12, viền trắng 2 (<code>Map Marker</code>)", "diff", "Mình cần 6 trạng thái, họ chỉ bật tắt"),
    ("Thẻ có ảnh", "Ref không có Card riêng", "<code>Vehicle Card</code> mẫu 7", "own", "DEC-269"),
    ("Dòng chọn có Radio", "<code>radio-buttons</code>, <code>Radio group item</code>", "<code>Vehicle Option Card</code>", "diff", "Thêm ảnh, Badge; DEC-270"),
    ("Khoá ảnh theo nhóm", "Không có", "22 nhóm, <code>design-system/handoff/vehicles.json</code>", "own", "DEC-266"),
    ("3 mặt cắt", "Không có", "Q (3/4 trước) · S (ngang) · Top (từ trên)", "own", "DEC-266"),
    ("Thang tỉ lệ thật px/m", "Không có", "8 · 16 · 40, mượn <code>size/*</code>", "own", "Xem <b>vh03</b>"),
    ("Khung ảnh 3/4", "Không có", f"{len(Q_TOKENS)} token <code>vehicle/q-*</code>", "own", "Xem <b>vh01</b>, <b>vh02</b>"),
    ("Sơ đồ lốp", "Không có", "<code>Tyre Layout</code>, <code>Tyre Slot</code>, 11 kiểu", "own", "DEC-275"),
    ("Marker bản đồ", "Không có; <code>charts-base.tsx</code> chỉ có chấm biểu đồ", "<code>Map Marker</code>, <code>Map Dot</code>, <code>Map Cluster</code>, <code>Map Pin</code>", "own", "DEC-276"),
    ("Tổ hợp đầu kéo – mooc – container", "Không có", "<code>Combo Figure</code>, <code>Combo Slots</code>, <code>Combo Text</code>, <code>Container Slot</code>", "own", "DEC-267"),
    ("Tên “Misc icons”", "16 nhóm: cờ, file type, thanh toán, featured…", "<code>misc-icon.md</code> chứa phương tiện", "diff", "Trùng tên, khác nội dung; xem <b>vh00</b>"),
]
_cnt = Counter(c[3] for c in CMP)
CMP_TBL = kit.rows(["Thứ so", "Untitled UI v8", "Mình", "Trạng thái", "Ghi chú"], [[a, b, c, _st[s], d] for a, b, c, s, d in CMP])

DECIDED = kit.rows(["Quyết định", "Nội dung còn hiệu lực"], [
    ["DEC-266", "Ảnh khoá theo 22 nhóm hình; tên xe của khách là dữ liệu; ảnh hãng giữ logo; 3 mặt cắt; 2 chế độ; sơ đồ lốp theo cấu hình trục; marker theo mức phóng. Đã bỏ: khách tải ảnh riêng, xoá logo, sinh lại không logo."],
    ["DEC-267", "Tổ hợp: 7 trạng thái vị trí container, 17 ca mẫu, 3 cách thể hiện, chỗ dùng từng cách; quy tắc ghép qua <code>P-quy-tac-ghep-mooc</code>."],
    ["DEC-268", "Vehicle Thumb 22 nhóm × 3 cỡ, cắt sẵn, ngoại lệ trần 30 tổ hợp. Chỉ phần bo mở lại ở <b>vh04</b>."],
    ["DEC-269", "Vehicle Card mẫu 7: chữ trái, ảnh lấn phải, Badge ghim góc. Chỉ phần bề rộng theo DEC-324 ở <b>vh05</b>."],
    ["DEC-270", "Vehicle Option Card: xe không khả dụng vẫn hiện ở Disabled, không làm mờ ảnh."],
    ["DEC-271 … DEC-274", "Container Slot, Combo Text, Combo Slots, Combo Figure: trục biến thể và luật hiển thị."],
    ["DEC-275", "Sơ đồ lốp vẽ đúng file khách kể cả điểm chờ OQ-6…13. Chỉ màu số trên lốp ở <b>vh12</b>."],
    ["DEC-276", "4 component marker; code xoay riêng Figure, nhãn giữ thẳng. Chỉ màu và cỡ ở <b>vh14</b>, <b>vh16</b>."],
    ["DEC-324, DEC-327, DEC-328, DEC-329", "Lưới, bóng, bo, icon đã chốt toàn DS. Trang này chỉ áp vào phương tiện, không bàn lại số."],
    ["DEC-330", "Bố cục page <code>DS · Foundations</code> theo hàng và cột, Master thành Section riêng, bỏ Demo khỏi page. Khi sửa foundation phải cập nhật dòng Figma ở cuối file (Section <code>Demo · Vehicles</code>)."],
    ["DEC-331", "Phương tiện có mã trạng thái riêng <code>vehicle</code>, duyệt riêng, không theo mã <code>icon</code>."],
    ["DEC-332", "Misc icons tách sang <code>design-system/foundations/icon-sets.md</code>; <code>ds-deps.py</code> nhận component dùng <code>vehicle</code> theo biến <code>vehicle-*</code> hoặc tên trong spec."],
])


def _pv_name(m, p):
    return ('<div class="vh-ba"><div class="vh-cur"><div class="vh-cap">Hiện tại</div><div class="vh-tree type-caption">'
            '<span>icon.md<span class="tp-sub">icon</span></span><span class="on">misc-icon.md<span class="tp-sub">vehicle</span></span><span>icon-sets.md<span class="tp-sub">misc-icon</span></span><span>logo.md<span class="tp-sub">logo</span></span></div></div>'
            '<div class="vh-prop"><div class="vh-cap">Đề xuất</div><div class="vh-tree type-caption"><span>icon.md<span class="tp-sub">icon</span></span><span class="on">vehicle.md<span class="tp-sub">vehicle</span></span><span>icon-sets.md<span class="tp-sub">misc-icon</span></span><span>logo.md<span class="tp-sub">logo</span></span></div></div></div>')


def _pv_q(m, p):
    used = lambda n, w, h, on: f'<div class="vh-col"><div class="vh-frame" style="width:calc({w}px / 3);height:calc({h}px / 3)"></div><span class="type-hint tp-sub">{n}<br>{w}×{h}{" · dùng" if on else " · 0 chỗ dùng"}</span></div>'
    return f'<div class="vh-scale">{used("q-sm", 160, 100, True)}{used("q-md", 240, 150, False)}{used("q-lg", 480, 300, False)}</div><div class="type-hint tp-sub" style="margin-top:8px">Hình thu 1/3. Card app 140×88 chưa có token nào.</div>'


def _pv_hero(m, p):
    if p == "mobile":
        return ba(f'<div class="vh-frame vh-over" style="width:100%;height:150px">{vi("t02-q", "position:absolute;left:0;bottom:0;width:var(--vehicle-q-lg-w)")}</div><div class="type-hint tp-sub">480 trên khung 393: tràn, mất đầu xe</div>',
                  f'<div class="vh-frame" style="width:100%;aspect-ratio:16/10">{vi("t02-q", "position:absolute;right:4%;bottom:4%;width:92%")}</div><div class="type-hint tp-sub">Rộng theo khung, tỉ lệ 16:10</div>')
    return ba(f'<div class="vh-frame" style="width:100%;max-width:var(--vehicle-q-lg-w);aspect-ratio:16/10">{vi("t02-q", "position:absolute;right:4%;bottom:4%;width:92%")}</div>',
              f'<div class="vh-frame" style="width:100%;max-width:var(--vehicle-q-lg-w);aspect-ratio:16/10">{vi("t02-q", "position:absolute;right:4%;bottom:4%;width:92%")}</div>')


def _pv_scale(m, p):
    return (f'<div class="vh-col"><span class="type-hint tp-sub">8 px/m, cột danh sách</span>{combo("1x45", "--size-md")}<span class="type-hint tp-sub">16 px/m, chi tiết, form</span><div style="max-width:100%;overflow:hidden">{combo("1x45", "--size-xl")}</div></div>')


def _pv_rad(m, p):
    t = lambda: "".join(f'<div class="vh-col">{thumb("t02", "head", s)}<span class="type-hint tp-sub">{n}</span></div>' for s, n in (("xs", "32"), ("sm", "48"), ("md", "64")))
    return ba(f'<div class="vh-scale">{t()}</div>', f'<div class="vh-scale">{t()}</div>', "6 · 8 · 10", "<span>radius/inner 8</span>")


def _pv_card(m, p):
    if p == "mobile":
        return ba(card(w="343px", model="Hino 700 · đầu kéo 2 cầu sau"), card(model="Hino 700 · đầu kéo 2 cầu sau", mw="140px", mh="88px"), "Cố định 343", "Trải theo màn: 361 trên 393", one=True)
    return ('<div class="vh-col" style="width:100%"><span class="type-hint tp-sub">Khi lưới 12 cột, 1280 − menu 240 − lề 32×2 = 976: 4 cột = 304</span>' + card(w="304px", status=("tp-g", "Sẵn sàng hoạt động")) + "</div>")


def _pv_card_fx(m, p):
    return ba(card(w="304px", status=("tp-g", "Sẵn sàng hoạt động")), card(w="304px", status=("tp-g", "Sẵn sàng hoạt động")), "Viền, không bóng", "shadow/xs + shadow/xs-border", one=True)


def _pv_option(m, p):
    b = lambda w: f'<div class="tp-card" style="padding:0;gap:0;width:{w};max-width:100%">{option("51C-482.15", "15 tấn · Nguyễn Văn Hoà", "t02", "head", ("tp-g", "Sẵn sàng hoạt động"), True)}{option("51R-091.44", "Xưởng Đình Vũ · tới 30/10", "n03", "wheels", ("tp-y", "Đang sửa chữa"), False, True)}</div>'
    return f'<div class="vh-col" style="width:100%"><span class="type-hint tp-sub">Drawer <code>width/xs</code> 384, trừ lề 24×2 = 336</span>{b("calc(var(--width-xs) - 2 * var(--space-3xl))")}</div>' if p == "web" else b("100%")


def _pv_bg(m, p):
    set_ = lambda: "".join(thumb(i, c, "md") for i, c in (("c40", "head"), ("t07", "head"), ("t02", "head"), ("t01", "wheels"), ("t04", "whole")))
    return ba(f'<div class="vh-scale">{set_()}</div>', f'<div class="vh-scale">{set_()}</div>')


def _pv_bg2(m, p):
    return f'<div class="vh-prop vh-scale"><div class="vh-col"><div style="background:var(--color-bg-primary);padding:8px;border-radius:8px">{vi("c40-q", "width:150px")}</div><span class="type-hint tp-sub">Trên nền thẻ, có nét bao</span></div><div class="vh-col"><div style="background:var(--color-bg-primary);padding:8px;border-radius:8px">{vi("t01-q", "width:150px")}</div><span class="type-hint tp-sub">Mooc, cùng nét bao</span></div></div>'


def _pv_src(m, p):
    bar = lambda n, w, t: f'<div class="vh-col" style="width:100%"><span class="type-caption">{n}</span><div class="vh-hbar" style="width:100%"><i style="width:{w}%"></i></div><span class="type-hint tp-sub">{t}</span></div>'
    return bar("PNG gốc, 76 file đang dùng", 100, "44,2 MB") + bar("WebP, Q rộng 960, S 448, Top 120", 2.7, "1,19 MB, đo 02/11 bằng PIL chất lượng 80")


def _pv_tenant(m, p):
    r = lambda a, b, c, d: f'<tr><td><span class="type-body">{a}</span></td><td>{thumb(b, c, "xs")}</td><td><span class="type-caption tp-sub">{d}</span></td></tr>'
    return ('<table class="tp-tb"><thead><tr><th><span class="type-caption-caps">Tên xe của khách</span></th><th></th><th><span class="type-caption-caps">Nhóm hình [Lõi]</span></th></tr></thead><tbody>'
            + r("Delta: Đầu kéo Hino 2 cầu", "t02", "head", "tractor-2ax") + r("Khách mới: Howo 6×4", "t02", "head", "tractor-2ax · Default") + r("Khách mới: Mooc 40ft", "t01", "wheels", "trailer-40-2ax") + "</tbody></table>")


def _pv_icon(m, p):
    line = lambda: f'<div class="vh-ln type-caption tp-sub">{kit.icon("gauge", "tp-ic-md vh-ic")}<span>182.450 km · 41%</span></div><div class="vh-ln type-caption tp-sub">{kit.icon("map-pin", "tp-ic-md vh-ic")}<span>Cảng Cát Lái, Thủ Đức</span></div>'
    return ba(f'{line()}<div style="margin-top:6px">{rtag(tok("color/text/disabled", m), tok("color/bg/primary", m))}</div>', f'{line()}<div style="margin-top:6px">{kit.cr("color/fg/tertiary", "color/bg/primary", 3)}</div>', "<span>color/text/disabled</span>", "<span>color/fg/tertiary</span>")


def _pv_tyre(m, p):
    st = {1: "sel", 4: "w", 7: "e"}
    return ba(tyre_layout("tractor-6x4", st), tyre_layout("tractor-6x4", st), "Số: color/text/inverse", "Số: color/text/white")


def _pv_touch(m, p):
    if p == "mobile":
        return f'<div style="display:flex;justify-content:center">{tyre_layout("trailer-3ax", {3: "w"}, 1.5)}</div><div class="type-hint tp-sub">Phóng 1,5 lần: lốp 24×45</div>'
    return f'<div style="display:flex;justify-content:center">{tyre_layout("trailer-3ax", {3: "w"})}</div><div class="type-hint tp-sub">Web: lốp 16×30, vùng bấm vô hình 24×32</div>'


def _pv_markers(m, p):
    mk = lambda: mapbox(dotm(20, 8, "mov", "Chạy") + dotm(68, 8, "stop", "Dừng") + dotm(20, 34, "idle", "Nổ máy") + dotm(68, 34, "off", "Mất tín hiệu", "10:40") + dotm(20, 60, "alert", "Cảnh báo") + dotm(68, 60, "sel", "Đang chọn"), 170)
    return ba(mk(), mk())


def _pv_top(m, p):
    return ba(mapbox(dotm(50, 30, "mov", "51F-120.08"), 150) + '<div class="type-hint tp-sub">Lùi về chấm ở mọi mức phóng</div>',
              '<div class="vh-map" style="height:150px"><i class="vh-rd1"></i>' + f'<span class="vh-mk" style="left:50%;top:14%"><span class="vh-mkf" style="width:24px;height:40px">{vi("t03-top", "position:absolute;left:2px;top:0;width:20px")}</span>{label("51F-120.08")}</span></div><div class="type-hint tp-sub">Mượn ảnh Top cùng họ, dài theo <code>size_m</code></div>',
              "Dùng chấm", "Mượn ảnh cùng họ")


def _pv_zoom(m, p):
    return ba(mapbox(marker(30, 4, "mov", "51C-482.15", 0, "combo", 8) + marker(70, 4, "stop", "51D-120.77", 0, "combo", 8), 240),
              mapbox(marker(26, 4, "sel", "51C-482.15", 0, "combo", 8) + marker(70, 18, "stop", "51D-120.77", 0, "combo", 4), 240), "Mọi Combo 8 px/m, dài 147", "Đang chọn 8, còn lại 4 px/m")


def _pv_label(m, p):
    mk = lambda: mapbox(dotm(26, 14, "mov", "51C-482.15") + dotm(66, 40, "stop", "51D-120.77") + cluster(28, 60, 24), 170)
    return ba(mk(), mk(), "Viền, không bóng", "<span>shadow/sm</span>")


GOLD = [("1", "Đầu kéo một mình", "none"), ("2", "Kéo mooc, không container", "empty"), ("3", "Đã xếp chỗ, chưa có số", "1x20"), ("4", "1×20 vỏ rỗng", "1x20"), ("5", "1×20 có hàng", "1x20"), ("6", "2×20 cùng Lệnh", "2x20"), ("7", "2×20 ghép 2 Lệnh", "2x20"), ("8", "1×40 có hàng", "1x40"), ("9", "1×45 lạnh", "1x45r")]


def _pv_gold(m, p):
    return '<div class="vh-g17">' + "".join(f'<div class="vh-case"><span class="type-caption-strong">{a}. {b}</span><div style="overflow:hidden">{combo(c, "--size-md")}</div></div>' for a, b, c in GOLD) + "</div>"


def _pv_status(m, p):
    r = "".join(f'<tr><td><code>{s}</code></td><td>{chip("tp-y", "stale")}</td><td><span class="type-caption tp-sub">Nháp, trước đó draft</span></td></tr>' for s in SLUGS[:3])
    return f'<table class="tp-tb"><tbody>{r}<tr><td colspan="3"><span class="type-caption tp-sub">… cùng trạng thái cho {len(SLUGS) - 3} component còn lại</span></td></tr></tbody></table>'


def _proposal():
    return kit.rows(["Việc", "Kết quả nếu chọn hết theo khuyến nghị"], [
        ["Tên", "Đổi <code>design-system/foundations/misc-icon.md</code> thành <code>vehicle.md</code>, không đổi token"],
        ["Token", "Xoá <code>vehicle/q-md-w</code>, <code>vehicle/q-md-h</code>, <code>vehicle/q-lg-h</code>; giữ <code>vehicle/q-sm-h</code>, <code>vehicle/q-lg-w</code> ở tầng Component; thêm 2 token cỡ ảnh thẻ app; px/m thành hằng số trong <code>vehicles.json</code>"],
        ["Bo, bóng, icon", "Thumb một vai <code>radius/inner</code>; thẻ <code>shadow/xs</code>; icon phụ <code>color/fg/tertiary</code>; nhãn marker <code>shadow/sm</code>"],
        ["Bề rộng", "Vehicle Card, Option Card trải theo cột; bỏ 360, 343, 420 cố định"],
        ["Ảnh", "Tối đổi nền ô sang <code>color/bg/quaternary</code>, thêm nét bao; xuất WebP vào <code>design-system/</code>; khách gán xe vào nhóm"],
        ["Lốp, bản đồ", "Số trên lốp <code>color/text/white</code>; Dừng <code>color/fg/tertiary</code>; 19 tên xe Delta thiếu Top mượn ảnh cùng họ; Combo thường 4 px/m"],
        ["Duyệt", "Sync 9 component từ dưới lên, kiểm 17 ca, rồi mới đặt approved"],
    ])


ITEMS = [
    dict(id="vh00", grp="Cấu trúc", title="Đổi tên misc-icon.md thành vehicle.md không?",
         why=("Đầu file ghi “Foundations · Phương tiện”, không có icon lẻ nào. DEC-332 (02/11) đã tách Misc icons sang <code>design-system/foundations/icon-sets.md</code>, nên giờ <mark>mã <code>misc-icon</code> trỏ tới <code>icon-sets.md</code>, còn mã <code>vehicle</code> trỏ tới <code>misc-icon.md</code></mark>: tên file và tên mã vẫn chéo nhau. Misc icons của Untitled (<code>design/_ref/untitled-ui/06-icons.md</code> Mục 6) cũng là 16 nhóm khác hẳn. "
              "Figma đã đặt Section <code>Vehicles</code>, handoff là <code>vehicles.json</code>. Đo lại 02/11, không tính trang review, sổ changelog, sổ quyết định: <mark>30 dòng trong 19 file</mark> phải sửa. Đổi tên không đổi token nào. Stale đã có: <code>ds-deps.py impact f:vehicle</code> nay trả đủ 9 component (DEC-332), nên trang này không hỏi việc đó nữa."),
         untitled="<code>Misc icons</code>: Integration, Country flag, File type, Payment method, Featured icon… Không có phương tiện.",
         ours="<code>design-system/foundations/misc-icon.md</code>, <code>design-system/foundations/icon-sets.md</code>, <code>design-system/foundations/README.md</code>; DEC-331, DEC-332.",
         astryx="Không có mục riêng; chỉ thẻ “Phương tiện” trong họ thẻ m13 (<code>design/design.md</code>).",
         note="Phụ thuộc trang misc: tên file phía Misc icons nay là <code>icon-sets.md</code>, đổi tên ở đây không vướng trang đó; <code>_scripts/ds-deps.py</code> phải sửa cùng lượt vì đang ghi cứng tên file.",
         pv=kit.panes(_pv_name, modes=("light",)),
         opts=[("a", "Đổi thành vehicle.md, sửa mọi dòng dẫn và ds-deps.py cùng lượt", True), ("b", "Giữ tên misc-icon.md, ghi chú trong README", False)]),
    dict(id="vh01", grp="Cấu trúc", title="Token vehicle/q-* còn thuộc foundation, hay chuyển Component?",
         why=(f"Sổ gộp <code>design-system/components/_token-ledger.json</code> (DEC-319: gộp số đo tầng Component về token chung, đợt 2 quyết trên trang review) còn {len(Q_TOKENS)} dòng <code>pending-round-2</code>. <code>design-system/_review/token-usage.json</code> ghi <mark>cả 5 có 0 chỗ gắn</mark> (<code>direct</code> rỗng, <code>refBy</code> rỗng); chưa đọc Figma để đối chiếu. "
              "Foundation Mục 2.3 ghi 240×150 là “thẻ web”, còn DEC-269 đã chốt <mark>thẻ web 160×100, app 140×88</mark>; hai cỡ sau mới là cỡ thật, và 140×88 lại không có token. Dòng <code>size/11xl × -h</code> trong bảng foundation cũng lạc vì <code>vehicle/q-sm-w</code> đã gộp về <code>size/11xl</code>. Mở lại DEC-266 phần cỡ: dòng đó từng bỏ phương án “bớt cỡ”; bằng chứng mới là DEC-269 có sau không dùng 240×150, và số chỗ gắn bằng 0."),
         untitled="Không có mảng này; <code>Avatar</code> ghi cỡ trong component, không có token riêng.",
         ours=f"{', '.join('<code>' + t.replace('vehicle-q-', 'vehicle/q-') + '</code>' for t in Q_TOKENS)}; <code>design-system/components/application/vehicle-card.md</code> ghi <code>vehicle/q-*</code>.",
         astryx="Không có token khung ảnh xe. Ảnh trong thẻ bo <code>{rounded.container}</code>, không cố định cỡ (<code>design/design.md</code>).",
         pv=kit.panes(_pv_q, platforms=("web", "mobile"), modes=("light",)),
         tokens=[("vehicle/q-sm-h", "100", "Giữ tầng Component: cao ảnh Vehicle Card web"), ("vehicle/card-media-app-w", "140", "Mới: rộng ảnh Vehicle Card app, DEC-269"), ("vehicle/card-media-app-h", "88", "Mới: cao ảnh Vehicle Card app, DEC-269")],
         opts=[("a", "Xoá q-md-*, chuyển phần còn lại về tầng Component của Vehicle Card, foundation chỉ ghi tỉ lệ 16:10", True), ("b", "Giữ cả 5 ở foundation, sửa bảng cho đúng DEC-269", False), ("c", "Xoá hết, Vehicle Card ghi số trần trong spec", False)]),
    dict(id="vh02", grp="Cấu trúc", title="vehicle/q-lg-w 480 cho ảnh đầu trang chi tiết: giữ thế nào?",
         why=("Giá trị 480 đang <mark>giống nhau ở Web và Mobile</mark> trong <code>design-system/tokens.json</code>, trong khi app vẽ 393: rộng hơn màn 87px. DEC-324 ghi “khối từ <code>width/xs</code> không vượt màn trừ hai lề”, nên 480 trên app phải co về 361, và 300 cao thành 225. "
              "<code>design-system/foundations/grids.md</code> đã chốt “Số riêng không mượn bậc trùng số: <code>vehicle/q-lg-w</code> 480”, nên trang này không đề xuất trỏ về <code>width/sm</code>. Chưa component nào dùng 480: chưa có spec “đầu trang chi tiết phương tiện”, <code>docs/vehicle-management/brainstorms/vehicle-management.md</code> cũng không nhắc cỡ."),
         untitled="<code>width-sm</code> 480 có trong thang, không gắn với ảnh. Không có ảnh đầu trang kiểu này.",
         ours="<code>vehicle/q-lg-w</code> 480, <code>vehicle/q-lg-h</code> 300; <code>design-system/foundations/grids.md</code>.",
         astryx="Mẫu trang P11, chi tiết sản phẩm: ảnh lớn bên trái (<code>design/design.md</code>).",
         pv=kit.panes(_pv_hero, platforms=("web", "mobile")),
         opts=[("a", "Giữ q-lg-w 480 là chiều rộng tối đa, app trải theo màn, bỏ q-lg-h, dùng tỉ lệ 16:10", True), ("b", "Giữ 480×300 ở web, thêm cỡ app 361×225", False), ("c", "Bỏ cả hai, chờ có spec màn chi tiết phương tiện mới thêm", False)]),
    dict(id="vh03", grp="Cấu trúc", title="Tỉ lệ thật px/m mượn size/md, size/xl, size/5xl: có ổn không?",
         why=("Sổ gộp ghi <code>vehicle/scale-sm</code>, <code>vehicle/scale-md</code>, <code>vehicle/scale-lg</code> đã về <code>size/md</code> 8, <code>size/xl</code> 16, <code>size/5xl</code> 40. Foundation vẫn ghi “<code>size/md</code> 8 (px/m)”. <mark>Hai nghĩa dùng chung một tên</mark>: <code>size/md</code> là pixel, còn ở đây là pixel trên mét, chỉ để nhân với <code>size_m</code>. "
              "Sau này đổi thang <code>size/*</code>, hình tổ hợp sẽ co theo mà không ai để ý. Combo Figure 1×45 đo 297 ở 16 px/m (18,57 m), 149 ở 8 px/m: vừa khung app 393 khi trừ lề. Mở lại DEC-319: bằng chứng là luật thống nhất sau soát chéo trong <code>_scripts/foundation_review/BRIEF.md</code>, “không mượn token vai khác vì trùng số”, có sau đợt gộp 1."),
         untitled="Không có. Thang <code>size-*</code> của Tailwind chỉ là pixel.",
         ours="<code>size/md</code>, <code>size/xl</code>, <code>size/5xl</code>; <code>design-system/components/application/combo-figure.md</code>.",
         astryx="Không có khái niệm tỉ lệ thật.",
         pv=kit.panes(_pv_scale),
         opts=[("a", "Ghi 8 · 16 · 40 px/m làm hằng số trong vehicles.json, foundation ghi bảng; không còn là token", True), ("b", "Giữ mượn size/md, size/xl, size/5xl như đợt gộp 1", False), ("c", "Lập lại 3 token vehicle/scale-*", False)]),
    dict(id="vh04", grp="Thẻ và ô", title="Bo ô Vehicle Thumb sau DEC-328",
         why=("DEC-328 chốt bo theo <b>vai</b>: <code>radius/control</code>, <code>radius/field</code>, <code>radius/inner</code> 8, <code>radius/card</code> 12. Vehicle Thumb vẫn gọi bo theo <b>cỡ</b>: 32 bo 6, 48 bo 8, 64 bo 10. Mở lại DEC-268: dòng đó bo theo cỡ, ⚠ chưa ghi lý do (“user chọn phương án đề xuất”); bằng chứng mới là DEC-328 có sau và <code>_scripts/foundation_review/radius.py</code> mới xác nhận tên token đã gộp, chưa bàn vai. "
              "Thumb nằm trong <code>radius/card</code> 12 ở lề 16, luật lồng “lề ≥ bo ngoài” đã đạt ở mọi cỡ. Container Slot, Trailer box, Tractor box đang <code>radius/inner</code> 8, <mark>ô ảnh cùng vai nên cùng số</mark>."),
         untitled="<code>Avatar</code> khi <code>rounded=false</code>: <code>rounded-md</code> 8 ở mọi cỡ từ 24 đến 64.",
         ours="<code>radius/sm</code>, <code>radius/md</code>, <code>radius/lg</code> trong <code>design-system/components/application/vehicle-thumb.md</code>.",
         astryx="Ảnh trong thẻ <code>{rounded.container}</code> 12; ảnh đang chọn viền 2 (<code>design/design.md</code>).",
         pv=kit.panes(_pv_rad, platforms=("web", "mobile")),
         opts=[("a", "Một vai radius/inner 8 cho cả 3 cỡ", True), ("b", "Giữ 6 · 8 · 10 theo cỡ, ghi là ngoại lệ", False)]),
    dict(id="vh05", grp="Thẻ và ô", title="Vehicle Card rộng 360 và 343 đã lệch lưới DEC-324",
         why=("DEC-269 đặt thẻ web 360, app 343 (khung 375 cũ). Sau DEC-324: web 1280 trừ menu 240 và lề 32×2 còn 976, rãnh 32, nên <mark>4 cột = 304</mark>, 360 không rơi vào cột nào; 5 cột = 388. App vẽ 393, lề 16: <mark>361</mark>, spec vẫn 343 và Combo Slots Compact ghi “thẻ app 343”. "
              "Ở 304, ảnh 160 và lề 16 + 12 còn 116 cho chữ: biển số vẫn đọc được, dòng xe cắt “…”. Badge dài nhất đo 132 trong <code>design-system/components/application/vehicle-card.md</code>, nằm gọn trên vùng ảnh 160. Web 1920 có 4 cột = 517, 3 cột = 380. Mở lại DEC-269 phần bề rộng: bằng chứng mới là lưới DEC-324."),
         untitled="Không có thẻ này. Lưới <code>container-max-width-desktop</code> 1280.",
         ours="<code>design-system/components/application/vehicle-card.md</code> Mục Kích thước; DEC-269, DEC-324.",
         astryx="Thẻ Phương tiện trong họ thẻ app <code>m13</code> (<code>design/design.md</code>), chưa đo bề rộng.",
         pv=kit.panes(_pv_card, platforms=("web", "mobile")),
         opts=[("a", "Bỏ 360, 343 cố định: thẻ trải theo cột, 4 cột trên 1280, tối thiểu 304; app trải theo màn; ảnh giữ 160×100, 140×88", True), ("b", "Giữ 360 làm cỡ thẻ, lưới tự xếp bao nhiêu cột vừa", False), ("c", "Web 2 cột 472 trên 1280, ảnh to lên 240×150", False)]),
    dict(id="vh06", grp="Thẻ và ô", title="Viền, bóng của thẻ xe và ô container sau DEC-327",
         why=("DEC-327 chốt vai thẻ: <code>shadow/xs</code> kèm viền <code>shadow/xs-border</code>, ở Tối giữ cả bóng và viền. <code>vehicle-card.md</code> chỉ có <code>color/border/secondary</code>, không bóng. Container Slot nằm trong khối cha nên <mark>phẳng là đúng</mark>; Option Card là dòng nên cũng không bóng. Thay đổi thực chất chỉ ở Vehicle Card."),
         untitled="Thang có <code>shadow-xs</code>; không có thẻ xe riêng.",
         ours="<code>design-system/components/application/vehicle-card.md</code>, <code>design-system/components/application/container-slot.md</code>.",
         astryx="“Chỉ dùng bóng cho lớp nổi” (dialog, toast, popover), thẻ phẳng (<code>design/design.md</code>).",
         pv=kit.panes(_pv_card_fx),
         opts=[("a", "Vehicle Card theo DEC-327; Container Slot, Option Card giữ phẳng", True), ("b", "Cả thẻ cũng phẳng, ghi là ngoại lệ", False)]),
    dict(id="vh07", grp="Thẻ và ô", title="Vehicle Option Card rộng 420 không vừa drawer 384",
         why=("DEC-324 đổi drawer 400 thành <code>width/xs</code> 384; trừ lề 24×2 (lề giả định, chưa có spec drawer) còn <mark>336</mark>, spec vẫn ghi “rộng 420 kéo giãn”. Bên trong: 336 − lề 16×2 − ảnh 48 − Radio 20 − 2 khoảng 12 = 212, mà Badge dài nhất 132 + khoảng 8 + Meta tối thiểu 140 = 280. Nên ở drawer web <mark>dòng phụ luôn xuống hàng</mark>, không chỉ ở app như DEC-270 ghi. Chữ không mất, dòng cao thêm."),
         untitled="<code>radio-buttons</code>: dòng chọn, không có ảnh và Badge.",
         ours="<code>design-system/components/application/vehicle-option-card.md</code>; <code>width/xs</code> 384.",
         astryx="Mẫu app <code>m15</code>, thẻ chọn: icon tròn, tên, mô tả, radio (<code>design/design.md</code>).",
         pv=kit.panes(_pv_option, platforms=("web", "mobile")),
         opts=[("a", "Bỏ số 420, dòng trải theo khối chứa; xuống hàng ở mọi nền tảng khi hẹp", True), ("b", "Rút Meta tối thiểu về 72 để giữ một hàng, chấp nhận cắt tên lái xe", False)]),
    dict(id="vh08", grp="Ảnh", title="Nền ô ảnh ở Sáng và Tối: container trắng tan, lốp đen tan",
         why=("Đo trên 21 ảnh Q, tỉ lệ điểm ảnh <mark>dưới 1,5:1 so với nền ô</mark>. Sáng, nền <code>color/bg/secondary</code> #FAFAFA: lạnh 84%, container 40 66%, trung bình 34%. Tối, nền #232323: xe nâng điện 87%, mooc 57%, đầu kéo 40%, trung bình 32%. Nên 2 chế độ đều mất hình, chỉ khác loại xe. "
              "Tối đổi sang <code>color/bg/quaternary</code> #404040 còn 26%. Không có một nền nào cứu cả hai: #737373 chỉ 8% nhưng thành ô xám giữa, lạc tông trong cả 2 chế độ. Nên cần thêm <mark>nét bao theo hình ảnh</mark>, cùng ý với <code>contrastBorder</code> của Untitled. Tất cả 9 spec đang ghi “Dark: chưa điền”, nên chưa ai quyết chuyện này. Ảnh là trong suốt, không cần sinh lại."),
         untitled="<code>Avatar</code>: nền <code>bg-tertiary</code> + <code>outline-[0.5px]</code> <code>outline-black/16</code> quanh ô; không xử lý ảnh trong suốt.",
         ours="<code>color/bg/secondary</code> trong <code>design-system/components/application/vehicle-thumb.md</code>; ô chưa có token Tối riêng.",
         astryx="Không có ảnh xe ở Tối; ảnh trong thẻ đặt thẳng trên nền thẻ (<code>design/design.md</code>).",
         pv=kit.panes(_pv_bg, platforms=("web", "mobile")) + '<div style="height:10px"></div>' + kit.panes(_pv_bg2),
         note="Nét bao 0,6px dựng bằng <code>filter: drop-shadow</code> theo viền hình ảnh, màu <code>color/fg/quaternary</code> ở Sáng, <code>color/fg/tertiary</code> ở Tối. Figma có Drop shadow trên layer ảnh trong suốt nên làm được; hiệu năng trong danh sách dài chưa đo, chưa kiểm trên Flutter.",
         opts=[("a", "Sáng giữ nền; Tối đổi color/bg/quaternary; thêm nét bao theo hình ở cả hai", True), ("b", "Chỉ đổi nền Tối, không nét bao", False), ("c", "Ô luôn nền sáng cố định ở cả hai chế độ, như ảnh in", False)]),
    dict(id="vh09", grp="Ảnh", title="Ảnh giao cho dev nằm ở đâu, định dạng gì?",
         why=(f"Nguồn thật đang ở <code>design/_lab/assets/vehicles/b-ai/</code>: <b>{PNG} file PNG</b>, 47 MB cả thư mục; {PNG - 1} file có trong <code>design-system/handoff/vehicles.json</code>, dư <code>g-truck-s.png</code>. Thư mục tên <code>_lab</code> là <mark>chỗ thử nghiệm mà lại là nguồn của foundation</mark>. File lớn nhất 935 KB, trong khi ảnh hiện cao nhất 480. "
              "Đo 02/11 bằng PIL: nén WebP theo cỡ dùng (Q rộng 960, S 448, Top 120) còn <mark>1,19 MB trên 44,2 MB</mark>. Trường <code>size_m</code> ghi “ước lượng” trong handoff, chưa đo lại."),
         untitled="Ảnh placeholder ở <code>shared-assets</code>, không có quy cách handoff.",
         ours="<code>design-system/handoff/vehicles.json</code>, <code>design/_lab/assets/vehicles/b-ai/t02-q.png</code>.",
         astryx="Không có bộ ảnh xe.",
         pv=kit.panes(_pv_src, modes=("light",)),
         opts=[("a", "Giữ PNG làm bản gốc ở design/_lab, xuất WebP theo cỡ vào design-system/handoff bằng script", True), ("b", "Chuyển hẳn PNG sang design-system, dev tự nén", False), ("c", "Để nguyên, dev tự lấy từ design/_lab", False)]),
    dict(id="vh10", grp="Ảnh", title="Nguồn ảnh theo khách: tầng nào, khách mới làm gì?",
         why=(f"Theo <code>.claude/rules/saas-layer.md</code>: nhóm hình là <b>[Lõi]</b>, bảng gán tên xe là dữ liệu danh mục <b>[Riêng Delta]</b> (39 tên, {ALT_NAMES} tên dùng ảnh Alt theo hãng). Bảng gán này đang nằm trong <code>vehicles.json</code> → <code>tenants.delta</code>, một file handoff. <mark>Khách thứ hai chưa có đường nào để gán</mark>; không có nhóm thì về <code>unknown</code>, ô trống. "
              "DEC-266 đã bỏ phương án khách tải ảnh riêng, trang này giữ nguyên. Câu hở thứ hai: 22 nhóm chưa có xe bồn, xe cẩu, mooc bồn. Câu 1 của rule hỏi “có ít nhất 2 doanh nghiệp cần không”, nên nhóm mới chỉ vào lõi khi có khách thứ hai; gọi API sinh ảnh phải báo chi phí trước (Mục 1 foundation). Ảnh mặc định như <code>t02</code>, <code>n08</code> cũng mang logo hãng thật, không riêng ảnh Alt; DEC-266 đã chọn giữ logo, trang này chỉ nêu để khách mới biết."),
         untitled="Không có khái niệm nhiều khách. Tầng do <code>design-system/foundations/misc-icon.md</code> Mục 1 đặt.",
         ours="<code>tenants.delta</code> trong <code>design-system/handoff/vehicles.json</code>; <code>docs/_product/saas-core-vs-tenant.md</code>.",
         astryx="Một khách, không có tầng.",
         pv=kit.panes(_pv_tenant, modes=("light", "dark")),
         note="Không tạo mã P: đây là dữ liệu danh mục, rule Mục 4 ghi “không cần mã P”. <code>P-quy-tac-ghep-mooc</code> đã có trong <code>docs/_product/tenant-parameters.md</code>, giá trị Delta còn chờ OQ-66, OQ-67.",
         opts=[("a", "Danh mục loại phương tiện của khách có cột Nhóm hình + Kiểu dáng; Delta là dữ liệu mẫu; nhóm mới vào lõi khi có khách thứ hai", True), ("b", "Đội sản phẩm tự gán khi đưa khách lên, khách không sửa", False), ("c", "Thêm trước nhóm xe bồn, xe cẩu vào lõi để bán rộng hơn", False)]),
    dict(id="vh11", grp="Icon", title="Icon phụ trên thẻ xe và chỗ của tractor-unit, container-truck",
         why=("<code>vehicle-card.md</code> ghi icon <code>gauge</code>, <code>map-pin</code>, <code>user-round</code>, <code>route</code> cỡ 16 màu <code>color/text/disabled</code>: 2,52:1 trên nền trắng, dưới ngưỡng 3:1 của WCAG 1.4.11. DEC-329 ghi “icon phụ mang nghĩa dùng <code>color/fg/tertiary</code>”, nên đây là <mark>áp DEC-329, không phải quyết mới</mark>; <code>icon/size/md</code> 16 nằm trong dòng chữ caption 16, đúng luật icon không cao hơn dòng chữ; nét theo DEC-329 là 2,25 ở cỡ ≤ 16. "
              "Câu còn hở là ranh giới icon và ảnh: <code>tractor-unit</code>, <code>container-truck</code> đã vẽ lại theo DEC-329 để đọc được ở 14 (<code>design-system/foundations/icon.md</code>). Chưa có luật khi nào dùng icon, khi nào dùng Vehicle Thumb XS 32."),
         untitled="Gói <code>@untitledui/icons</code> không có trong ref nên chưa kiểm icon xe; <code>Avatar</code> có <code>placeholderIcon</code>.",
         ours="<code>design-system/foundations/icon.md</code>; <code>icon/size/md</code> 16; DEC-329.",
         astryx="<code>truck</code> Lucide cho trạng thái Đã giao lái xe (<code>design/design.md</code>).",
         pv=kit.panes(_pv_icon, platforms=("web", "mobile")),
         opts=[("a", "Icon phụ color/fg/tertiary; icon xe cho menu, nhãn, chip (≤ 20), Vehicle Thumb cho dòng dữ liệu (≥ 32)", True), ("b", "Chỉ đổi màu, chưa đặt ranh giới", False), ("c", "Bỏ Thumb XS, bảng web dùng icon xe", False)]),
    dict(id="vh12", grp="Sơ đồ lốp", title="Màu lốp mượn token chữ, viền; số trên lốp mất ở Tối",
         why=(f"Số lốp dùng <code>color/text/inverse</code>. Token này đổi theo chế độ: Tối thành #0A0A0A, trên nền xanh Selected chỉ {rtag(tok('color/text/inverse', 'dark'), tok('color/bg/info/solid'.replace('/', '-'), 'dark'), 4.5)}, trên Warning {rtag(tok('color/text/inverse', 'dark'), tok('color/bg/warning/solid'.replace('/', '-'), 'dark'), 4.5)}. Nền màu đặc giữ nguyên ở hai chế độ, nên chữ phải là <code>color/text/white</code>: {rtag(tok('color/text/white', 'dark'), tok('color/bg/info/solid'.replace('/', '-'), 'dark'), 4.5)} và {rtag(tok('color/text/white', 'dark'), tok('color/bg/warning/solid'.replace('/', '-'), 'dark'), 4.5)}. "
              "Thêm nữa, lốp lái tô bằng <code>color/text/tertiary</code> và Error tô bằng <code>color/border/error</code>: <mark>token chữ, viền làm nền</mark>, trái luật “không mượn token vai khác”. Error ở Tối thành hồng #FFA19C, trong khi nền lỗi đặc <code>color/bg/error/solid</code> vẫn đỏ. Mở lại DEC-275: dòng đó ghi “⚠ chưa ghi lý do chung cho bảng màu”, chưa từng xét Tối; bằng chứng mới là số đo ở trên, spec ghi “Dark: chưa điền”."),
         untitled="Không có sơ đồ lốp. Token <code>text-white</code>, <code>fg-white</code> có trong bảng màu của họ.",
         ours="<code>design-system/components/application/tyre-layout.md</code> Mục Biến thể; <code>color/bg/info/solid</code>, <code>color/bg/warning/solid</code>.",
         astryx="Không có sơ đồ lốp. Lab: <code>design/_lab/tyre-mapping.html</code>.",
         pv=kit.panes(_pv_tyre, platforms=("web", "mobile")),
                  opts=[("a", "Số trên nền trạng thái color/text/white; lốp lái color/fg/tertiary; Error color/bg/error/solid", True), ("b", "Chỉ đổi số sang color/text/white, giữ các nền", False), ("c", "Giữ nguyên, thêm ngoại lệ Tối vào spec", False)]),
    dict(id="vh13", grp="Sơ đồ lốp", title="Vùng chạm lốp 16×30 trên app",
         why=("<code>tyre-layout.md</code> tự nhận 16×30 nhỏ hơn 24×24 của WCAG 2.5.8 và ghi hai cách: nới vùng vô hình 24×32 ở web; “phóng ≥ 1,5 lần hoặc chọn từ danh sách” ở app, <mark>chưa chọn cách nào</mark>. App lái xe dùng ngoài trời. Phóng 1,5 lần thì lốp 24×45, khung 300 rộng, vừa 361. Lốp kép ngoài và trong cách nhau 3px, nên phóng vẫn dễ bấm nhầm: cần cả danh sách."),
         untitled="Không có sơ đồ lốp. <code>touch target</code> ref chưa ghi số riêng.",
         ours="<code>design-system/components/application/tyre-layout.md</code> Mục Trợ năng.",
         astryx="Vùng chạm tối thiểu 44 ở app, theo <code>design/design.md</code>.",
         note="Phụ thuộc trang touch: nếu trang đó chốt vùng chạm 44 cho app, thì lốp phóng 1,5 lần vẫn dưới ngưỡng, danh sách là đường chính.",
         pv=kit.panes(_pv_touch, platforms=("web", "mobile")),
         opts=[("a", "App phóng 1,5 lần và luôn có danh sách vị trí bên dưới; web nới vùng bấm 24×32", True), ("b", "App chỉ chọn từ danh sách, sơ đồ để xem", False)]),
    dict(id="vh14", grp="Bản đồ", title="Màu trạng thái marker: Dừng, Mất tín hiệu quá nhạt, Cảnh báo đổi màu ở Tối",
         why=(f"Đo chấm trên nền đất giả lập của <code>design/_lab/lab-map.html</code>, Sáng #eef0f3, Tối #15171b; bản đồ thật (Vietmap, Google Maps) chưa kiểm. Dừng <code>color/text/disabled</code>: Sáng {rtag(tok('color/text/disabled', 'light'), LAND['light'])}, Tối {rtag(tok('color/text/disabled', 'dark'), LAND['dark'])}. Mất tín hiệu <code>color/border/primary</code>: Sáng {rtag(tok('color/border/primary', 'light'), LAND['light'])}, Tối {rtag(tok('color/border/primary', 'dark'), LAND['dark'])}, lại còn mờ 50%; đề xuất <code>color/fg/quaternary</code> Sáng {rtag(tok('color/fg/quaternary', 'light'), LAND['light'])} vẫn dưới ngưỡng, chấp nhận vì trạng thái này cố ý nhạt và luôn có giờ cuối trên nhãn. "
              f"Cảnh báo <code>color/border/error</code> ở Tối thành hồng. Các nền đặc ở Tối thấp hơn (đang chọn {rtag(tok('color/bg/info/solid', 'dark'), LAND['dark'])}, nổ máy {rtag(tok('color/bg/warning/solid', 'dark'), LAND['dark'])}), nhưng viền trắng 2 tách chúng ra khỏi nền; ngược lại ở Sáng viền trắng không giúp gì. "
              "DEC-276 ghi Dừng là <code>text/tertiary</code>, spec lại ghi <code>color/text/disabled</code>, và DEC-276 ghi Mất tín hiệu <code>border/strong</code>, token này không còn. <mark>Spec đã lệch DEC</mark>. Mở lại DEC-276 phần màu: dòng đó “⚠ chưa ghi lý do chung cho màu”, chưa xét nền bản đồ; bằng chứng mới là số đo trên. Trạng thái cũng không dựa riêng vào màu vì có nhãn và chi tiết khi bấm (spec Mục Nên)."),
         untitled="<code>AvatarOnlineIndicator</code> chỉ online, offline; không có bản đồ.",
         ours="<code>design-system/components/application/map-marker.md</code> Mục State; DEC-276.",
         astryx="Không có marker. Lab <code>design/_lab/lab-map.html</code> dùng chấm viền trắng 2,5.",
         pv=kit.panes(_pv_markers, platforms=("web", "mobile")),
         pv_raw_ok="Màu đất, đường là giả lập bản đồ từ lab-map.html, nằm trong css trang.",
         opts=[("a", "Dừng color/fg/tertiary; Mất tín hiệu color/fg/quaternary bỏ mờ ở chấm, giữ mờ ở hình; Cảnh báo color/bg/error/solid", True), ("b", "Giữ màu theo đúng DEC-276, chỉ sửa spec cho khớp", False), ("c", "Thêm hình vào chấm: chấm rỗng cho Mất tín hiệu, dấu ! cho Cảnh báo, giữ màu spec", False)]),
    dict(id="vh15", grp="Bản đồ", title=f"{len(NO_TOP)} nhóm chưa có ảnh Top: marker gần hiện gì?",
         why=(f"Trong <code>vehicles.json</code>, {len(NO_TOP)} nhóm không có mặt cắt Top: {', '.join('<code>' + k + '</code>' for k in NO_TOP)}. Tính theo Delta: <mark>{NO_TOP_NAMES} trên {len(DELTA)} tên xe</mark>, trong đó {NO_TOP_TRUCK} là xe tải. <code>map-marker.md</code> chưa nói gì về ca này. Ngoài ra 4 ảnh Top của container sai góc (Mục 2.4 foundation; hình dưới là <code>c45-top</code>, <code>t07-top</code>): Marker Combo chưa vẽ container. "
              "BL-264 đã ghi việc sinh lại, cần duyệt chi phí API; trong lúc chờ cần một luật lùi."),
         untitled="Không có.",
         ours="<code>design-system/handoff/vehicles.json</code> trường <code>views</code>; <code>design-system/components/application/map-marker.md</code>.",
         astryx="Không có.",
         pv=kit.panes(_pv_top, platforms=("web", "mobile")) + f'<div class="vh-scale" style="margin-top:8px">{vi("c45-top", "width:40px")}{vi("t07-top", "width:40px")}<span class="small muted">Ảnh Top sai góc đang có</span></div>',
         untitled_none="Không có mảng này",
         opts=[("a", "Mượn ảnh Top cùng họ (xe tải về t03-top, dài theo size_m), thiết bị dùng chấm; sinh lại theo BL-264 khi duyệt chi phí", True), ("b", "Nhóm thiếu Top dùng Map Dot ở mọi mức phóng", False), ("c", "Sinh đủ ảnh ngay (gọi API, cần báo chi phí trước)", False)]),
    dict(id="vh16", grp="Bản đồ", title="Marker gần 8 px/m và mức phóng chưa có số",
         why=("Foundation chỉ ghi Gần, Vừa, Xa, <mark>không có số mức phóng</mark>. Tính theo công thức Web Mercator ở vĩ độ TP.HCM 10,8°: mức 20 là 0,147 m/px (6,8 px/m), mức 17 là 1,17 m/px (0,85 px/m). Nghĩa là 8 px/m chỉ đúng tỉ lệ thật ở mức 20; ở mức 17 hình to gấp 9 lần thật. "
              "Combo đầu kéo + mooc 40: (7 + 12,4 − 1) × 8 = <mark>147px</mark>, 37% bề ngang app 393. Foundation ghi Đang chọn “to hơn + viền”, spec chỉ có viền. Mở lại DEC-276 phần cỡ: bằng chứng là phép tính trên, lúc chốt chưa có. Số mức phóng đề xuất dưới đây là ước lượng của Claude, chưa thử trên Vietmap."),
         untitled="Không có.",
         ours="<code>size/md</code> 8; <code>design-system/foundations/misc-icon.md</code> Mục 4; DEC-276.",
         astryx="Không có.",
         untitled_none="Không có mảng này",
         pv=kit.panes(_pv_zoom, platforms=("web", "mobile")),
         note="Mức phóng đề xuất: Gần ≥ 17, Vừa 12–16, Xa ≤ 11. Là [Lõi], không theo khách.",
         opts=[("a", "Marker thường 4 px/m, Đang chọn 8 px/m; ghi mức phóng 17 và 12 vào foundation", True), ("b", "Giữ 8 px/m cho mọi marker, chỉ thêm số mức phóng", False), ("c", "Dài theo tỉ lệ thật của bản đồ, co giãn theo từng mức phóng", False)]),
    dict(id="vh17", grp="Bản đồ", title="Nhãn, chấm, cụm trên bản đồ có bóng không?",
         why=("Nhãn biển số dùng nền <code>color/bg/primary</code> + viền <code>color/border/secondary</code>. Ở Sáng, viền #E5E5E5 gần trùng đất #eef0f3 và đường trắng, <mark>nhãn dính vào đường</mark>. DEC-327 chỉ định vai cho thẻ, menu, dialog; marker chưa có vai. Chọn <code>shadow/sm</code>, nhỏ hơn <code>shadow/lg</code> của menu để không tranh với popup, hơn <code>shadow/xs</code> để nổi được trên ảnh nền bản đồ. Bóng trên từng chấm có giá khi nhiều xe, chưa đo."),
         untitled="<code>shadow-sm</code> trong thang 7 bậc, không gán cho marker.",
         ours="<code>shadow/sm</code>; <code>design-system/components/application/map-marker.md</code> Mục Cấu tạo.",
         astryx="Lab <code>design/_lab/lab-map.html</code>: <code>0 2px 6px</code> trên ghim.",
         pv=kit.panes(_pv_label, platforms=("web", "mobile")),
         opts=[("a", "Thêm vai marker: nhãn, chấm, cụm dùng shadow/sm", True), ("b", "Không bóng, chỉ đậm viền lên color/border/primary", False)]),
    dict(id="vh18", grp="Tổ hợp", title="17 ca mẫu đã phủ đủ chưa?",
         why=("DEC-267 chốt “Component tổ hợp phải hiển thị đúng cả 17”. Foundation Mục 5.3 liệt kê đủ, nhưng <mark>chưa có bảng kiểm</mark>: spec Combo Figure, Combo Slots chỉ ghi Config và “Kiểm mất hình: chưa chạy”. Mooc đổi Lệnh (F4), bỏ giữa đường (F5), chưa số, kiểm hoá đặt ngoài component hoặc nằm ở Container Slot, nên mỗi ca cần ghi rõ ráp từ gì. Ca 1–9 dựng được bằng Combo Figure ở dưới; ca 10–17 cần banner, trạng thái khe. Combo Figure ở app dùng 8 px/m, Compact ghi “thẻ app 343” cần đổi theo vh05. Nguồn: <code>design/_lab/lab-combo.html</code>, bản lab bạn duyệt “tương đối ok” ngày 12/10; quy tắc trong đó là đề xuất, chưa phải quy định của khách."),
         untitled="Không có.",
         ours="<code>design-system/components/application/combo-figure.md</code>, <code>design-system/components/application/combo-slots.md</code>, <code>design-system/components/application/combo-text.md</code>, <code>design-system/components/application/container-slot.md</code>.",
         astryx="Không có; từ ngành “container, mooc” chỉ ở mục ngôn ngữ (<code>design/design.md</code>).",
         untitled_none="Không có mảng này",
         pv=kit.panes(_pv_gold, modes=("light", "dark"), platforms=("web",)),
         opts=[("a", "Lập bảng 17 ca × component trong vehicle.md, dựng trên Figma khi sync", True), ("b", "Kiểm trong lượt vẽ Lệnh vận tải, không làm riêng", False)]),
    dict(id="vh19", grp="Duyệt", title="Component nào thực sự đã duyệt?",
         why=(f"DEC-268 tới DEC-276 ghi “User duyệt 27/10 (Y)”, là <b>duyệt kế hoạch dựng</b>. Trong md: <mark>{APPROVED}/{len(SLUGS)} approved</mark>, {STALE}/{len(SLUGS)} đang <code>status: stale</code>, cả 9 có <code>status_prev: draft</code>, đầu bài ghi “phiên bản 0.1.0 · Nháp”, cả 9 “Dark: chưa điền giá trị Dark”. <code>_workspace/backlog.md</code> có 27 dòng Sync cho 9 component này (đếm cả dòng đã đóng), do foundation đổi nhiều lần. "
              "Rule <code>.claude/rules/ds-stale.md</code> buộc sync từ dưới lên, nên thứ tự là Vehicle Thumb, Container Slot rồi Vehicle Card, Option Card, Combo Slots, Combo Figure; cuối cùng Map Marker dùng ảnh Top. Trường <code>uses</code> của cả 9 đang rỗng trong <code>design-system/components/_deps.json</code>, dù spec ghi lồng Badge, Radio: máy không thấy, nên sửa Badge không làm stale các thẻ này (chưa rõ do máy dò hay cách ghi md)."),
         untitled="Không có quy trình này.",
         ours="<code>design-system/components/application/vehicle-thumb.md</code> và 8 file cùng thư mục; <code>design-system/components/_deps.json</code>.",
         astryx="Thẻ Phương tiện đã dựng trên Figma cũ, nút <code>5795:151897</code> (<code>design/design.md</code>), không thuộc DS v2.",
         untitled_none="Không có quy trình này",
         pv=kit.panes(_pv_status, modes=("light",)),
         opts=[("a", "Coi cả 9 là Nháp: áp trang này, sync từ dưới lên, duyệt 1 trang riêng rồi mới approved", True), ("b", "Đặt approved theo DEC cũ, sửa dần", False)]),
]

SPEC = dict(
    slug="vehicle", short="phần Phương tiện",
    title="Foundations · Phương tiện — lõi Invlogis, Untitled không có",
    subtitle="Ảnh xe, sơ đồ lốp, marker bản đồ, tổ hợp · chọn từng mục · 02/11/2026",
    lead=(f"Trang này giúp quyết phần <mark>[Lõi] của Invlogis</mark>: Untitled không có mảng này, nên chỉ so khi có thứ tương đương (Avatar, ảnh, chấm trạng thái). Kết luận chính: foundation đúng về cấu trúc, nhưng <mark>đã lệch sau DEC-324, DEC-327, DEC-328, DEC-329</mark>; cả 9 component đều chưa duyệt; chế độ Tối chưa ai đụng tới. <mark>Chưa sửa token nào.</mark>"),
    kpis=[(f"{APPROVED}/{len(SLUGS)}", "component đã duyệt", "bad"), (f"{_cnt['own']}", "thứ chỉ mình có", ""), (f"{_cnt['ok']}", "giống Untitled", "ok"), (f"{_cnt['diff']}", "khác có lý do", ""), (f"{_cnt['gap']}", "mình thiếu", "bad"),
          (f"{NO_TOP_NAMES}/{len(DELTA)}", "tên xe Delta chưa có ảnh Top", "bad"), (f"{len(Q_TOKENS)}", "token vehicle/q-* có 0 chỗ gắn", "bad"), (f"{PNG}", "file PNG nguồn, 47 MB", "")],
    tag_kind="radius",
    screens=dict(title="Xem trên màn thật", intro="Màn mẫu dựng từ biến thật và ảnh thật trong repo (nhúng WebP). Bật <b>Bộ giá trị</b> để so hiện tại với đề xuất; đề xuất gồm bo, bóng, màu icon, nền ô Tối, nét bao, màu marker, số trên lốp. Bản đồ là giả lập màu từ <code>design/_lab/lab-map.html</code>.",
                 proposal_css=".tp-f.tp-prop{--vh-prop-on:1}", logo_svg=None, gridov=False, overlay_html=overlay),
    sections=[
        dict(title="Bảng đối chiếu từng mục — Untitled ↔ mình", intro=f"Đủ {len(CMP)} dòng: {_cnt['ok']} giống, {_cnt['diff']} khác có lý do, {_cnt['gap']} mình thiếu, {_cnt['own']} chỉ mình có. Ref Untitled không có phương tiện; dòng có số lấy từ <code>design/_ref/untitled-ui/react/components/base/avatar/avatar.tsx</code>.", html=CMP_TBL),
        dict(title="Đã chốt, không mở lại", intro="Trang giữ nguyên các dòng dưới. Chỗ mở lại ghi rõ câu “Mở lại DEC-x:” kèm bằng chứng, ở vh01, vh03, vh04, vh05, vh12, vh14, vh16.", html=DECIDED),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", html=_proposal()),
    ],
    items=ITEMS,
    final=("Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/misc-icon.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>vehicle = approved</b> (<code>ds-foundation-status.py set vehicle approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). "
           "Việc riêng của trang: sửa 9 spec trong <code>design-system/components/application/</code>, đổi tên file nếu chọn <b>vh00</b>, xuất WebP nếu chọn <b>vh09</b>. Gọi API sinh ảnh Top (BL-264) sẽ báo kế hoạch và chi phí riêng."),
    css=CSS, js="",
)
