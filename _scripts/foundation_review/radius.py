#!/usr/bin/env python3
"""SPEC trang review Foundations · Bo góc. Số đọc từ tokens.css, token-usage.json, _token-ledger.json lúc dựng; không gõ tay."""
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402

ROOT = kit.ROOT
USAGE = json.loads((ROOT / "design-system/_review/token-usage.json").read_text())
LEDGER = json.loads((ROOT / "design-system/components/_token-ledger.json").read_text())["size"]["tokens"]


# ---------- đọc token từ tokens.css theo nền tảng ----------
def _block(sel):
    m = re.search(re.escape(sel) + r"\s*\{(.*?)\n\}", kit.TCSS, flags=re.S)
    return dict(re.findall(r"(--[\w-]+):\s*([^;]+);", m.group(1)))


_ROOT = {}
for _m in re.finditer(r"^:root \{(.*?)^\}", kit.TCSS, flags=re.S | re.M):
    _ROOT.update(re.findall(r"(--[\w-]+):\s*([^;]+);", _m.group(1)))
_PLAT = {"web": _block(':root, [data-platform="web"]'), "mobile": _block('[data-platform="mobile"]')}


def px(expr, plat):
    """Giá trị px của 'var(--x)', '--x' hoặc '12px' theo nền tảng."""
    expr = str(expr).strip()
    m = re.fullmatch(r"var\((--[\w-]+)\)", expr)
    if m:
        expr = m.group(1)
    if expr.startswith("--"):
        raw = _PLAT[plat].get(expr, _ROOT.get(expr))
        if raw is None:
            raise SystemExit(f"Không có token {expr} ({plat})")
        return px(raw, plat)
    return float(expr.replace("px", "") or 0)


def n(x):
    return f"{x:g}".replace(".", ",")


def shown(token, plat):
    x = px(f"--radius-{token}", plat)
    return "tròn hẳn" if x >= 9999 else n(x)


def used_by(css_name):
    return [c["slug"] for c in USAGE["components"] if css_name in c.get("used", [])]


SCALE = [("none", "0", "0"), ("xxs", "0.125rem", "2"), ("xs", "0.25rem", "4"), ("sm", "0.375rem", "6"), ("md", "0.5rem", "8"), ("lg", "0.625rem", "10"),
         ("xl", "0.75rem", "12"), ("2xl", "1rem", "16"), ("3xl", "1.25rem", "20"), ("4xl", "1.5rem", "24"), ("full", "9999px", "tròn hẳn")]
ROLES = ["control", "field", "card", "inner", "overlay", "tab", "chip", "menu", "menu-item", "badge"]
SPLIT = [r for r in ROLES if px(f"--radius-{r}", "web") != px(f"--radius-{r}", "mobile")]
SAME_SCALE = sum(1 for k, _, v in SCALE if shown(k, "web") == v and shown(k, "mobile") == v)


# ---------- máy đo lồng góc: đúng câu trong design-system/foundations/radius.md mục 5 luật 5 ----------
def rule(R, lx, ly, r):
    """Đạt khi lề ≥ R (cả hai phía), hoặc hai lề chênh ≤ 1 và R = r + lề ± 1. Khối chỉ tính là gần góc khi cả hai lề < 2R."""
    if lx >= 2 * R or ly >= 2 * R:
        return "far"
    if lx >= R and ly >= R:
        return "pass"
    return "pass" if abs(lx - ly) <= 1 and abs(R - (r + min(lx, ly))) <= 1 else "fail"


# name, nguồn, nền tảng, khung R, lề ngang, lề trên, bo khối, cao khối, cao khung (None = theo nội dung), sửa theo đề xuất {khoá: giá trị}, mục
CASES = [
    ("Nút trong thẻ", "thẻ trên màn chi tiết web", "web", "--radius-card", "--layout-card-padding", "--layout-card-padding", "--radius-control", "--control-height-md", None, None, ""),
    ("Nút trong thẻ", "thẻ Lệnh app", "mobile", "--radius-card", "--layout-card-padding", "--layout-card-padding", "--radius-control", "--control-height-md", None, None, ""),
    ("Ô nhập trong thẻ", "biểu mẫu web", "web", "--radius-card", "--layout-card-padding", "--layout-card-padding", "--radius-field", "--control-height-md", None, None, ""),
    ("Ô nhập trong thẻ", "biểu mẫu app", "mobile", "--radius-card", "--layout-card-padding", "--layout-card-padding", "--radius-field", "--control-height-lg", None, None, ""),
    ("Khối phụ trong thẻ", "Combo Slots trong thẻ Lệnh", "mobile", "--radius-card", "--layout-card-padding", "--layout-card-padding", "--radius-inner", "--size-7xl", None, None, ""),
    ("Ảnh nhỏ trong dòng tệp", "field-upload, dòng tệp web", "web", "--radius-card", "--space-lg", "--space-lg", "--radius-tab", "--control-height-lg", None, {"r": "--radius-inner"}, "rd09"),
    ("Badge trên Vehicle Card", "vehicle-card, ghim cách góc 12", "web", "--radius-card", "--space-lg", "--space-lg", "--radius-full", "--chip-height-sm", None, None, ""),
    ("Badge trên Vehicle Card", "vehicle-card bản app", "mobile", "--radius-card", "--space-lg", "--space-lg", "--radius-full", "--chip-height-sm", None, {"lx": "--space-xl", "ly": "--space-xl"}, "rd06"),
    ("Vòng icon trong ô bấm tải lên", "field-upload bản app", "mobile", "--radius-card", "--space-lg", "--space-lg", "--radius-full", "--featured-icon-size", None, {"lx": "--space-xl", "ly": "--space-xl"}, "rd06"),
    ("Khe Container trong khối mooc", "combo-slots lề 8 + container-slot", "web", "--radius-inner", "--space-md", "--space-md", "--radius-inner", "--size-7xl", None, None, ""),
    ("Khe Container trong khối mooc", "combo-slots Compact trên app", "mobile", "--radius-inner", "--space-md", "--space-md", "--radius-inner", "--size-7xl", None, {"lx": "--space-lg", "ly": "--space-lg"}, "rd06"),
    ("Vòng icon trong thông báo", "alert-notification, web = app", "web", "--radius-xl", "--space-lg", "--space-lg", "--radius-full", "--size-4xl", None, None, ""),
    ("Icon trong Alert", "alert-notification, web = app", "web", "--radius-lg", "--space-lg", "--space-lg", "--radius-sm", "--size-2xl", None, None, ""),
    ("Ô module trong thẻ phạm vi", "sidebar-navigation, Collapsed False", "web", "--radius-lg", "--space-md", "10px", "--radius-control", "--size-4xl", None, {"R": "--radius-md", "r": "--radius-inner"}, "rd07"),
    ("Ô module khi menu thu gọn", "sidebar-navigation, Collapsed True", "web", "--radius-control", "--space-xs", "--space-xs", "--radius-control", "--size-4xl", None, {"R": "--radius-md", "r": "--radius-xs"}, "rd07"),
    ("Mục trong menu thả", "header-navigation, menu tầng ẩn", "web", "--radius-menu", "--space-xs", "--space-xs", "--radius-menu-item", "--control-height-md", None, None, "rd05"),
    ("Mục trong menu breadcrumbs", "breadcrumbs, menu tầng ẩn", "web", "--radius-lg", "--space-xs", "--space-xs", "--radius-sm", "--control-height-ml", None, None, ""),
    ("Mục trong menu tài khoản", "header-navigation, bo radius/card", "web", "--radius-card", "--control-icon-gap", "--control-icon-gap", "--radius-menu-item", "--control-height-md", None, {"R": "--radius-menu", "lx": "--space-xs", "ly": "--space-xs"}, "rd05"),
    ("Ô đếm trong Badge SM", "badge, lề 3 · bo 3", "web", "--radius-badge", "--chip-count-inset", "--chip-count-inset", "--chip-count-radius", "--size-xl", None, {"r": "--radius-xxs"}, "rd08"),
    ("Ô đếm trong Badge MD", "badge, lề 4 · bo 3", "web", "--radius-badge", "--space-xs", "--space-xs", "--chip-count-radius", "--size-xl", None, {"r": "--radius-xxs"}, "rd08"),
    ("Ô đếm trong Badge LG", "badge, lề 4 · bo 4", "web", "--radius-menu", "--space-xs", "--space-xs", "--radius-xs", "--size-2xl", None, {"R": "--radius-md"}, "rd05"),
    ("Nút lọc trong ô tìm", "DEC-196, app, ôm sát lề 4", "mobile", "--radius-full", "--space-xs", "--space-xs", "--radius-full", "44px", "--control-height-lg", None, ""),
    ("Nút trong hộp thoại", "hộp xác nhận web, lề 20", "web", "--radius-overlay", "--space-2xl", "--space-2xl", "--radius-control", "--control-height-md", None, None, ""),
    ("Ô nhập trong sheet, sau tiêu đề", "sheet app, cách mép trên 62", "mobile", "--radius-overlay", "--space-2xl", "62px", "--radius-field", "--control-height-lg", None, None, ""),
    ("Avatar đầu sheet tài khoản", "header-navigation; lề trên chưa ghi, tạm lấy 24 như sheet upload", "mobile", "--radius-card", "--space-lg", "24px", "--radius-full", "--size-4xl", None, {"R": "--radius-overlay"}, "rd04"),
]


# Token đổi số nếu theo khuyến nghị: mọi ca đều tính lại qua đây, không chỉ ca có sửa riêng.
AFTER = {"--radius-menu": "--radius-lg", "--upload-sheet-radius": "--radius-overlay", "--chip-count-radius": "--radius-xxs"}


def calc(c, fix=False):
    name, src, plat, R, lx, ly, r, h, fh, f, ref = c
    if fix:
        f = f or {}
        R, lx, ly, r = f.get("R", R), f.get("lx", lx), f.get("ly", ly), f.get("r", r)
        R, lx, ly, r = (AFTER.get(x, x) for x in (R, lx, ly, r))
    hv = px(h, plat)
    rv = min(px(r, plat), hv / 2)
    lxv, lyv = px(lx, plat), px(ly, plat)
    frame_h = px(fh, plat) if fh else hv + 2 * lyv
    Rv = min(px(R, plat), frame_h / 2)
    return dict(R=Rv, lx=lxv, ly=lyv, r=rv, h=hv, st=rule(Rv, lxv, lyv, rv), Rt=R, lxt=lx, lyt=ly, rt=r)


RES = [calc(c) for c in CASES]
RES_FIX = [calc(c, True) for c in CASES]
MEASURED = sum(1 for x in RES if x["st"] != "far")
FAILS = sum(1 for x in RES if x["st"] == "fail")
FAILS_FIX = sum(1 for x in RES_FIX if x["st"] == "fail")
PLATNAME = {"web": "Web", "mobile": "App"}


def _css(expr):
    return f"var({expr})" if str(expr).startswith("--") else expr


def _bw(c):
    """Bề ngang khối theo hình thật: khối tròn, vuông rộng bằng cao; Badge và ô đếm rộng vừa nhãn."""
    if c[0].startswith(("Vòng icon", "Avatar", "Ô module", "Ảnh nhỏ", "Icon trong")):
        return f"width:{_css(c[7])};"
    if c[0].startswith("Badge"):
        return "width:80px;"
    if c[0].startswith("Ô đếm"):
        return "width:28px;"
    return ""


def frame(c, res, width="100%"):
    """Khung đo dựng bằng biến thật; JS đọc lại số trên trình duyệt và so với số dựng trang."""
    fh = c[8]
    h = f"height:{_css(fh)};" if fh else ""
    return (f'<div class="nf" data-platform="{c[2]}" data-exp="{res["st"]}" style="width:{width};{h}border-radius:{_css(res["Rt"])};padding:{_css(res["lyt"])} {_css(res["lxt"])} {_css(res["lyt"])} {_css(res["lxt"])}">'
            f'<div class="nb" style="height:{_css(c[7])};{_bw(c)}border-radius:{_css(res["rt"])}"></div></div>')


def case_card(i):
    c, x = CASES[i], RES[i]
    lab = {"pass": ('<span class="st-ok">Đạt</span>'), "fail": ('<span class="st-gap">Không đạt</span>'), "far": ('<span class="muted">Ngoài vùng góc</span>')}[x["st"]]
    how = f'R {n(x["R"])} · lề {n(x["lx"])}' + (f'/{n(x["ly"])}' if x["lx"] != x["ly"] else "") + f' · r {n(x["r"])}'
    ref = f' <a class="small" href="#{c[10]}">{c[10]}</a>' if c[10] else ""
    return (f'<div class="nc"><div class="nh"><b>{c[0]}</b><span class="tagp">{PLATNAME[c[2]]}</span></div>{frame(c, x)}'
            f'<div class="small nm" data-m>{how}</div><div class="small">{lab}{ref}</div><div class="small muted">{c[1]}</div></div>')


def group_cards(idx):
    return '<div class="ng">' + "".join(case_card(i) for i in idx) + "</div>"


def find(name, plat):
    return next(i for i, c in enumerate(CASES) if c[0] == name and c[2] == plat)


def before_after(i, label_fix):
    c = CASES[i]
    a, b = RES[i], RES_FIX[i]
    def one(x, lab):
        tag = '<span class="st-ok">Đạt</span>' if x["st"] == "pass" else ('<span class="st-gap">Không đạt</span>' if x["st"] == "fail" else '<span class="muted">Ngoài vùng góc</span>')
        return (f'<div class="pane" data-theme="light" data-platform="{c[2]}"><span class="lab">{lab}</span>{frame(c, x)}'
                f'<div class="small nm">R {n(x["R"])} · lề {n(x["lx"])}{"/" + n(x["ly"]) if x["lx"] != x["ly"] else ""} · r {n(x["r"])}</div><div class="small">{tag}</div></div>')
    return f'<div class="small" style="font-weight:600;margin:6px 0 4px">{c[0]} · {PLATNAME[c[2]]}</div><div class="pvw">{one(a, "Hiện tại")}{one(b, label_fix)}</div>'


# ---------- xem thử dựng từ atom thật ----------
def mini(title="LVT-2026-0412"):
    return (f'<div class="tp-card"><div class="tp-top"><span class="type-code">{title}</span><span class="tp-chip tp-b">Đang chạy</span></div>'
            '<div class="tp-fld"><span class="type-label">Mã container</span><div class="tp-inp"><span class="type-body">TCLU 482915-3</span></div></div>'
            '<div class="ibox type-caption">Cát Lái → KCN Long Hậu · 51C-482.15</div>'
            '<span class="tp-btn wide"><span class="type-label">Duyệt lệnh</span></span></div>')


def opts_grid(cols, body=mini, cls="pv4"):
    """Mỗi cột: (nhãn, nền tảng, đè biến)."""
    cells = "".join(f'<div class="pane" data-theme="light" data-platform="{p}" style="{o}"><span class="lab">{l}</span>{body()}</div>' for l, p, o in cols)
    return f'<div class="{cls}">{cells}</div>'


def sheet(rad, title, lab, note):
    return (f'<div class="pane" data-theme="light" data-platform="mobile"><span class="lab">{lab}</span><div class="shw"><div class="she" style="border-radius:{rad} {rad} 0 0">'
            f'<div class="grb"></div><div class="type-title-3">{title}</div><div class="type-body tp-sub">{note}</div><span class="tp-btn wide"><span class="type-label">Đã hiểu</span></span></div></div></div>')


# ---------- Corner smoothing: công thức góc liền mạch của Figma, dựng thành đường SVG ----------
def squircle(w, h, R, xi):
    p = min((1 + xi) * R, min(w, h) / 2)
    arc_m = 90 * (1 - xi)
    L = math.sin(math.radians(arc_m / 2)) * R * math.sqrt(2)
    alpha = (90 - arc_m) / 2
    p3p4 = R * math.tan(math.radians(alpha / 2))
    beta = 45 * xi
    cc = p3p4 * math.cos(math.radians(beta))
    d = cc * math.tan(math.radians(beta))
    b = (p - L - cc - d) / 3
    a = 2 * b
    f = lambda v: f"{v:.3f}"
    seg = [
        f"M{f(w - p)} 0", f"c{f(a)} 0 {f(a + b)} 0 {f(a + b + cc)} {f(d)}", f"a{R} {R} 0 0 1 {f(L)} {f(L)}", f"c{f(d)} {f(cc)} {f(d)} {f(b + cc)} {f(d)} {f(a + b + cc)}",
        f"L{w} {f(h - p)}", f"c0 {f(a)} 0 {f(a + b)} {f(-d)} {f(a + b + cc)}", f"a{R} {R} 0 0 1 {f(-L)} {f(L)}", f"c{f(-cc)} {f(d)} {f(-(b + cc))} {f(d)} {f(-(a + b + cc))} {f(d)}",
        f"L{f(p)} {h}", f"c{f(-a)} 0 {f(-(a + b))} 0 {f(-(a + b + cc))} {f(-d)}", f"a{R} {R} 0 0 1 {f(-L)} {f(-L)}", f"c{f(-d)} {f(-cc)} {f(-d)} {f(-(b + cc))} {f(-d)} {f(-(a + b + cc))}",
        f"L0 {f(p)}", f"c0 {f(-a)} 0 {f(-(a + b))} {f(d)} {f(-(a + b + cc))}", f"a{R} {R} 0 0 1 {f(L)} {f(-L)}", f"c{f(cc)} {f(-d)} {f(b + cc)} {f(-d)} {f(a + b + cc)} {f(-d)}", "Z",
    ]
    return " ".join(seg), dict(a=a, b=b, c=cc, d=d, L=L, p=p)


def smooth_dev(R, xi):
    """Độ lệch lớn nhất (px) giữa góc liền mạch và góc tròn thường, lấy mẫu trên đoạn cong đầu vào của góc phải trên."""
    _, g = squircle(400, 400, R, xi)
    a, b, cc, d, p = g["a"], g["b"], g["c"], g["d"], g["p"]
    x0 = p  # khoảng cách tới mép phải khi bắt đầu đoạn cong
    P = [(0, 0), (a, 0), (a + b, 0), (a + b + cc, d)]
    worst = 0
    for i in range(201):
        t = i / 200
        mt = 1 - t
        x = mt**3 * P[0][0] + 3 * mt**2 * t * P[1][0] + 3 * mt * t**2 * P[2][0] + t**3 * P[3][0]
        y = mt**3 * P[0][1] + 3 * mt**2 * t * P[1][1] + 3 * mt * t**2 * P[2][1] + t**3 * P[3][1]
        dx = x0 - x  # tới mép phải
        if dx < R:  # trong ô góc: mép góc tròn thường cách mép trên một đoạn theo cung
            yr = R - math.sqrt(max(0, R**2 - (R - dx) ** 2))
            worst = max(worst, abs(y - yr))
        else:
            worst = max(worst, y)
    return worst


DEV16, DEV24 = smooth_dev(16, 0.6), smooth_dev(24, 0.6)


def smooth_svg(w, h, R, smooth, zoom=1):
    d, _ = squircle(w, h, R, 0.6)
    shape = f'<path d="{d}" style="fill:var(--color-bg-secondary);stroke:var(--color-border-primary)"/>' if smooth else f'<rect x="0" y="0" width="{w}" height="{h}" rx="{R}" style="fill:var(--color-bg-secondary);stroke:var(--color-border-primary)"/>'
    return f'<svg class="sm" viewBox="-1 -1 {w + 2} {h + 2}" aria-hidden="true">{shape}</svg>'


def smooth_zoom(R):
    w = R * 3
    d, _ = squircle(300, 300, R, 0.6)
    return (f'<svg class="sm" viewBox="0 0 {w} {w}" aria-hidden="true"><g transform="translate(0,0)"><rect x="0" y="0" width="300" height="300" rx="{R}" style="fill:none;stroke:var(--color-text-tertiary);stroke-width:.2;stroke-dasharray:.8 .6"/>'
            f'<path d="{d}" style="fill:none;stroke:var(--color-action-primary);stroke-width:.3"/></g></svg>')


# ---------- bảng đối chiếu ----------
def scale_viz():
    cells = "".join(f'<div class="sc"><div class="sq" style="border-radius:var(--radius-{k})"></div><code>radius/{k}</code><span class="small muted">{v}</span></div>' for k, _, v in SCALE)
    return f'<div class="scw">{cells}</div>'


def scale_rows():
    out = []
    for k, rem, v in SCALE:
        comps = used_by(f"radius-{k}")
        via = [r for r in ROLES if any(re.search(rf"--radius-{r}:\s*var\(--radius-{k}\)", b) for b in (kit.TCSS,))]
        vp = ", ".join(f"<code>radius/{r}</code>" for r in via) or "—"
        prim = "9999" if k == "full" else ("0" if k == "none" else v)
        out.append([f"<code>radius-{k}</code>", f"n:{v if k == 'full' else rem + ' · ' + v}", f"<code>radius/{k}</code>", f"n:{v}", f"<code>radius/{prim}</code>",
                    f"n:{len(comps)}", vp, '<span class="st-ok">Giống</span>'])
    return out


U_USE = {
    "control": ("<code>rounded-lg</code> = 8", "base/buttons/button.tsx", "Web giống, app khác có lý do"),
    "field": ("<code>rounded-lg</code> = 8", "base/input/input.tsx", "Web giống, app khác có lý do"),
    "card": ("<code>rounded-xl</code> = 12", "application/table/table.tsx", "Web giống, app khác có lý do"),
    "inner": ("không có vai riêng", "—", "Chỉ mình có"),
    "overlay": ("<code>sm:rounded-2xl</code> = 16, màn nhỏ <code>rounded-xl</code> = 12", "application/modals/modal.tsx", "Web giống, app ngược hướng"),
    "tab": ("<code>rounded-md</code> = 6 trong khung, khung <code>rounded-lg</code> = 8", "application/tabs/tabs.tsx", "Khác có lý do"),
    "chip": ("<code>rounded-full</code>", "base/badges/badges.tsx", "Giống"),
    "menu": ("<code>rounded-lg</code> = 8", "base/dropdown/dropdown.tsx", "Giống, đang rớt máy đo"),
    "menu-item": ("<code>rounded-md</code> = 6", "base/dropdown/dropdown.tsx", "Giống"),
    "badge": ("<code>rounded-md</code> = 6, LG <code>rounded-lg</code> = 8", "base/badges/badges.tsx", "Giống"),
}


def role_rows():
    out = []
    for r in ROLES:
        comps = used_by(f"radius-{r}")
        uses, f, st = U_USE[r]
        cls = "st-ok" if st.startswith("Giống") else ("st-own" if st.startswith("Chỉ") else "st-diff")
        diff = '<span class="st-diff">khác</span>' if r in SPLIT else '<span class="muted">bằng nhau</span>'
        out.append([f"<code>radius/{r}</code>", f"n:{shown(r, 'web')}", f"n:{shown(r, 'mobile')}", diff, f"n:{len(comps)}", ", ".join(comps) or "—", uses, f'<span class="small muted">{f}</span>', f'<span class="{cls}">{st}</span>'])
    return out


def ledger_rows():
    out = []
    for k, x in LEDGER.items():
        if "radius" not in k:
            continue
        o = x["original"]["Web"]
        rep = x.get("replacement")
        st = '<span class="st-ok">Đã gộp 01/11</span>' if x.get("status") == "merged" else '<span class="st-gap">Chờ đợt 2</span>'
        rep_h = f"<code>{rep}</code> = {n(px('--' + rep.replace('/', '-'), 'web'))}" if rep else f"chưa có; <a href='#{'rd08' if 'chip' in k else 'rd04'}'>{'rd08' if 'chip' in k else 'rd04'}</a>"
        out.append([f"<code>{k}</code>", f"{o}", rep_h, x["use"], st])
    return out


merged_n = sum(1 for k, x in LEDGER.items() if "radius" in k and x.get("status") == "merged")
pending_n = sum(1 for k, x in LEDGER.items() if "radius" in k and x.get("status") != "merged")
skip_radius = [f for f in USAGE["findings"] if f["kind"] == "skip" and "radius" in json.dumps(f)]
skip_all = [f for f in USAGE["findings"] if f["kind"] == "skip"]
compraw_radius = [f for f in USAGE["findings"] if f["kind"] == "compraw" and "radius" in json.dumps(f)]
dups = [f for f in USAGE["findings"] if f["kind"] == "dup" and f.get("group") == "radius"]
assert len(ROLES) == 10 and not skip_radius and len(compraw_radius) == 2 and len(dups) == 5

CMPRAW_ROWS = [
    ["<code>skip</code> (token còn trỏ thẳng thang chữ, đệm)", f"n:{len(skip_radius)}", f"Cả {len(skip_all)} mục <code>skip</code> trong sổ đều về chữ và đệm, không mục nào về bo góc."],
    ["<code>compraw--3</code> (số 3 lệch thang)", "n:1", "<code>chip/count-radius</code> bo 3; cùng nhóm có <code>chip/count-inset</code> và <code>upload/required-gap</code> không phải bo góc. Mục <a href='#rd08'>rd08</a>."],
    ["<code>compraw--28</code> (số 28 lệch thang)", "n:1", "<code>upload/sheet-radius</code> bo 28; ba token còn lại của nhóm là cỡ khối. Sổ gợi ý gần <code>3xl (24) · 4xl (32)</code> theo thang khoảng cách; theo thang bo góc, 24 là <code>radius/4xl</code>. Mục <a href='#rd04'>rd04</a>."],
    ["<code>vehicle/thumb-radius-md</code>", "n:0", "Không còn là token: sổ ghi đã gộp về <code>radius/lg</code> ngày 01/11. Tên chỉ còn trong danh sách đã xử lý của <code>token-usage.json</code> (<code>unused--vehicle-thumb-radius-md</code>). Vehicle Thumb gọi thẳng <code>radius/sm</code> · <code>radius/md</code> · <code>radius/lg</code>, cỡ 32 · 48 · 64. Không cần quyết."],
]

MISUSE = [
    ["<code>radius/menu</code>", "Badge LG, Avatar XL", "Mượn vai menu để lấy số 8. Đổi bo menu thì Badge và Avatar đổi theo.", "<code>radius/md</code>", "<a href='#rd05'>rd05</a>"],
    ["<code>radius/tab</code>", "Featured icon, ảnh nhỏ, nút Chọn tệp, nút xoá (field-upload web); ô icon kết quả tìm (header-navigation)", "Không có tab nào. Nếu gọi trên app sẽ thành tròn hẳn.", "<code>radius/control</code> cho nút, <code>radius/inner</code> cho ảnh, ô icon và Featured icon vuông", "<a href='#rd09'>rd09</a>"],
    ["<code>radius/control</code>", "Logo 28 và ô module (sidebar-navigation)", "Ô hình, không phải nút. Nếu sidebar có bản app, logo sẽ thành tròn hẳn.", "<code>radius/inner</code>; ô module thu gọn ngoại lệ <code>radius/xs</code> (rd07)", "<a href='#rd09'>rd09</a>"],
    ["<code>radius/card</code>", "Menu tài khoản, hộp thoại tìm, sheet tài khoản (header-navigation)", "Lớp nổi mà đi vai thẻ: hộp thoại tìm 12 trong khi hộp xác nhận 16.", "<code>radius/overlay</code> cho hộp thoại, sheet; menu tài khoản gọi <code>radius/menu</code>, lề 4 (<a href='#rd05'>rd05</a>)", "<a href='#rd04'>rd04</a>"],
    ["<code>radius/badge</code>", "Thanh kéo Help sheet (tooltip)", "Hai sheet khác gọi <code>radius/xxs</code> cho cùng thanh kéo. Thanh cao 4 nên 2 và 6 nhìn như nhau.", "<code>radius/xxs</code>", "<a href='#rd09'>rd09</a>"],
    ["<code>radius/control</code> và <code>radius/field</code>", "Ô tìm", "<code>design-system/foundations/radius.md</code> xếp ô tìm vào control; sidebar-navigation gọi <code>radius/field</code>. Web cùng 8, app 12 và tròn hẳn.", "<code>radius/control</code> theo bảng foundation (DEC-196 đo nút lọc trên ô viên thuốc)", "<a href='#rd09'>rd09</a>"],
]

ROLE_AFTER = [
    ["<code>radius/control</code>", "8 · tròn hẳn", "Giữ tách. Nút, tab, ô tìm."],
    ["<code>radius/field</code>", "8 · 12", "Giữ tách. Ô nhập, ô chọn."],
    ["<code>radius/card</code>", "12 · 16", "Giữ tách. Chỉ cho thẻ, nhóm có viền, bảng."],
    ["<code>radius/inner</code>", "8 · 12", "Giữ tách. Thêm ảnh nhỏ, ô icon, logo."],
    ["<code>radius/overlay</code>", "16 · 24", "Giữ tách. Mọi hộp thoại và mọi sheet, kể cả upload 28, tài khoản 16."],
    ["<code>radius/menu</code>", "8 → 10", "Trỏ <code>radius/lg</code>; menu tài khoản gọi vai này, lề 6 → 4; Badge LG và Avatar XL chuyển sang <code>radius/md</code>."],
    ["<code>radius/menu-item</code> · <code>radius/badge</code>", "6", "Giữ. Một số, hai vai."],
    ["<code>radius/tab</code>", "bỏ", "Gộp vào <code>radius/control</code>."],
    ["<code>radius/chip</code>", "bỏ", "Không component nào gọi; Pill dùng <code>radius/full</code>."],
    ["<code>chip/count-radius</code>", "3 → 2", "Bỏ token, Badge SM và MD gọi <code>radius/xxs</code>."],
    ["<code>upload/sheet-radius</code>", "28 → 24", "Bỏ token, gọi <code>radius/overlay</code>."],
]

# ---------- đè biến để thử gộp ----------
M_WEB = "--radius-control:var(--radius-md);--radius-tab:var(--radius-md);--radius-field:var(--radius-md);--radius-card:var(--radius-xl);--radius-inner:var(--radius-md);--radius-overlay:var(--radius-2xl)"
M_APP = "--radius-control:var(--radius-full);--radius-tab:var(--radius-full);--radius-field:var(--radius-xl);--radius-card:var(--radius-2xl);--radius-inner:var(--radius-xl);--radius-overlay:var(--radius-4xl)"

CSS = f"""
#tpWrap[data-merge=web] .tp-f{{{M_WEB}}}
#tpWrap[data-merge=app] .tp-f{{{M_APP}}}
[data-tags="on"] .tp-menu[data-tag]{{position:absolute}}
.ibox{{background:var(--color-bg-secondary);border-radius:var(--radius-inner);padding:var(--space-md) var(--space-lg);color:var(--color-text-tertiary)}}
.pv4{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}}
.scw{{display:grid;grid-template-columns:repeat(auto-fill,minmax(88px,1fr));gap:10px;background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:14px;margin:10px 0}}
.sc{{display:grid;gap:4px;justify-items:start;min-width:0}}.sc code{{white-space:nowrap}}
.sq{{width:56px;height:56px;background:color-mix(in srgb,#00A2FF 18%,#fff);border:2px solid #0036B5}}
.ng{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin:8px 0 14px}}
.nc{{background:#fff;border:1px solid #E2E8F0;border-radius:12px;padding:10px 12px;display:grid;gap:6px;align-content:start;min-width:0}}
.nh{{display:flex;justify-content:space-between;gap:6px;align-items:flex-start;font-size:13px;line-height:18px}}.tagp{{font:600 10.5px/16px Inter;background:#EEF2F8;border-radius:5px;padding:0 5px;flex:none}}
.nf{{background:var(--color-bg-primary);box-shadow:inset 0 0 0 1px var(--color-border-primary);overflow:hidden;box-sizing:border-box}}
.nb{{background:color-mix(in srgb,#00A2FF 22%,#fff);box-shadow:inset 0 0 0 1px #0036B5;width:100%;max-width:100%}}
.nm{{font-variant-numeric:tabular-nums;color:#475569}}
.shw{{background:var(--color-bg-overlay);padding:24px 0 0;border-radius:10px 10px 0 0;overflow:hidden}}
.she{{background:var(--color-bg-primary);padding:var(--space-md) var(--space-2xl) var(--space-3xl);display:grid;gap:var(--space-md)}}
.grb{{width:36px;height:var(--size-xs);background:var(--color-bg-quaternary);border-radius:var(--radius-xxs);justify-self:center;margin-bottom:var(--space-md)}}
.sm{{display:block;width:100%;height:auto;max-height:190px}}
@media(max-width:820px){{.pv4{{grid-template-columns:minmax(0,1fr)}}}}
"""

JS = r"""
// Máy đo lồng góc đọc lại trên trình duyệt, đúng luật radius.md mục 5 luật 5; lệch với số dựng trang thì báo lỗi lúc build.
function rdRule(R,lx,ly,r){if(lx>=2*R||ly>=2*R)return'far';if(lx>=R&&ly>=R)return'pass';return Math.abs(lx-ly)<=1&&Math.abs(R-(r+Math.min(lx,ly)))<=1?'pass':'fail'}
function rdMeasure(){$$('.nf').forEach(f=>{const b=f.querySelector('.nb');if(!b)return;const fr=f.getBoundingClientRect(),br=b.getBoundingClientRect();const c=getComputedStyle(f),i=getComputedStyle(b);const R=Math.min(parseFloat(c.borderTopLeftRadius),fr.height/2),r=Math.min(parseFloat(i.borderTopLeftRadius),br.height/2);const lx=Math.round(br.left-fr.left),ly=Math.round(br.top-fr.top);const st=rdRule(R,lx,ly,r);if(st!==f.dataset.exp&&fr.width>0)errs.push('lồng góc lệch: '+f.dataset.exp+' dựng, đo được '+st+' R'+R+' lề '+lx+'/'+ly+' r'+r)})}
window.afterToggle=rdMeasure;
// Thử gộp trên màn thật: nút riêng của trang, không đổi token.
(function(){const bar=$('#tpBar');if(!bar)return;const w=document.createElement('span');w.innerHTML='<span class="tp-lab">Thử gộp Web · App</span><span class="tp-seg" id="rdMerge"><button data-v="off" aria-pressed="true">Giữ tách</button><button data-v="web" aria-pressed="false">Cả hai theo Web</button><button data-v="app" aria-pressed="false">Cả hai theo App</button></span>';bar.appendChild(w);const s=w.querySelector('#rdMerge');s.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;s.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));$('#tpWrap').setAttribute('data-merge',b.dataset.v);tag()})})();
"""

i_badge_m = find("Badge trên Vehicle Card", "mobile")
i_upload = find("Vòng icon trong ô bấm tải lên", "mobile")
i_slot_m = find("Khe Container trong khối mooc", "mobile")
i_scope = find("Ô module trong thẻ phạm vi", "web")
i_scope2 = find("Ô module khi menu thu gọn", "web")
i_menu = find("Mục trong menu thả", "web")
i_sm = find("Ô đếm trong Badge SM", "web")
i_md = find("Ô đếm trong Badge MD", "web")
i_avatar = find("Avatar đầu sheet tài khoản", "mobile")
i_acct = find("Mục trong menu tài khoản", "web")
assert RES[i_acct]["st"] == "pass" and calc(CASES[i_acct][:9] + ({"R": "--radius-menu"}, ""), True)["st"] == "fail" and RES_FIX[i_acct]["st"] == "pass"  # menu 10 mà giữ lề 6 thì rớt: 6 + 6 = 12

MATRIX = (
    '<div class="pvt">Thẻ, khung lớn: mong đợi "tách xa"</div>' + group_cards([i for i, c in enumerate(CASES) if i <= 8 or c[0].startswith("Vòng icon trong thông") or c[0].startswith("Icon trong Alert")])
    + '<div class="pvt">Khối trong khối</div>' + group_cards([i for i, c in enumerate(CASES) if c[0].startswith("Khe Container") or c[0].startswith("Ô module")])
    + '<div class="pvt">Khung ôm sát: mong đợi "đồng tâm"</div>' + group_cards([i for i, c in enumerate(CASES) if c[0].startswith(("Mục trong", "Ô đếm", "Nút lọc"))])
    + '<div class="pvt">Hộp thoại, sheet</div>' + group_cards([i for i, c in enumerate(CASES) if c[0].startswith(("Nút trong hộp", "Ô nhập trong sheet", "Avatar đầu"))])
)
assert MATRIX.count('class="nc"') == len(CASES)

ITEMS = [
    dict(id="rd00", grp="Gộp Web · App", title="Nút và tab: 8 trên web, tròn hẳn trên app. Gộp không?",
         why=f"<code>radius/control</code> (<code>radius/md</code> ↔ <code>radius/full</code>) có {len(used_by('radius-control'))} component gọi, <code>radius/tab</code> có {len(used_by('radius-tab'))}. Lý do cũ ở DEC-122: \"Bảng web dày dữ liệu cần góc gọn; mobile giữ nút viên thuốc và thẻ bo lớn user thích\". Màu và Chữ đã về một bộ (DEC-316, DEC-322) vì không có lý do tách; ở đây lý do vẫn còn: nút web cao 32 chen trong bảng, nút app cao 42 đến 52 bấm ngoài trời. <b>Mở lại DEC-122:</b> chỉ khi chọn gộp; bằng chứng mới là Màu và Chữ đã về một bộ. Phương án tròn hẳn trùng phương án \"tròn\" DEC-122 đã bỏ.",
         untitled="<code>rounded-lg</code> = 8 cho mọi cỡ nút, không có bản app riêng (<code>base/buttons/button.tsx</code>).",
         ours="<code>radius/control</code>, <code>radius/tab</code>: Web 8, App tròn hẳn.",
         astryx="Nút web bo <code>element</code> 10; nút app bo <code>full</code>. Astryx cũng tách.",
         pv=opts_grid([("Web hiện tại", "web", ""), ("App hiện tại", "mobile", ""), ("App nếu gộp về 8", "mobile", "--radius-control:var(--radius-md);--radius-tab:var(--radius-md)"), ("Web nếu gộp tròn hẳn", "web", "--radius-control:var(--radius-full);--radius-tab:var(--radius-full)")]),
         opts=[("keep", "Giữ tách: web 8, app tròn hẳn. Không màn nào đổi", True), ("eight", "Gộp về 8: mọi nút app đổi từ viên thuốc sang góc vuông bo", False), ("full", "Gộp tròn hẳn: mọi nút web thành viên thuốc, kể cả trong bảng", False)]),
    dict(id="rd01", grp="Gộp Web · App", title="Ô nhập và khối trong thẻ: 8 trên web, 12 trên app. Gộp không?",
         why=f"<code>radius/field</code> {len(used_by('radius-field'))} component, <code>radius/inner</code> {len(used_by('radius-inner'))} component. Hai vai đang bằng nhau trên cả hai nền. Bo đi theo chiều cao: web cao {n(px('--control-height-md', 'web'))}, tỉ lệ bo trên cao {n(round(px('--radius-field', 'web') / px('--control-height-md', 'web'), 2))}; app cao {n(px('--control-height-lg', 'mobile'))}, tỉ lệ {n(round(px('--radius-field', 'mobile') / px('--control-height-lg', 'mobile'), 2))}. Gộp về 8 làm ô app 52 trông sắc hơn hẳn, tỉ lệ {n(round(8 / px('--control-height-lg', 'mobile'), 2))}; gộp về 12 làm ô web 32 gần thành viên thuốc, tỉ lệ {n(round(12 / px('--control-height-md', 'web'), 2))}. Về máy đo: gộp về 8 tự sửa ca khe Container trên app; gộp về 12 làm ca đó rớt thêm trên web. <b>Mở lại DEC-134, DEC-259:</b> chỉ khi chọn gộp; bằng chứng mới là Màu và Chữ đã về một bộ.",
         untitled="<code>rounded-lg</code> = 8, chiều cao ô một bộ (<code>base/input/input.tsx</code>). Không có vai khối trong.",
         ours="<code>radius/field</code>, <code>radius/inner</code>: Web 8, App 12 (DEC-259 đổi app 14 → 12).",
         astryx="Ô nhập web bo <code>element</code> 10; ô nhập app và khối trong thẻ <code>inner-mobile</code> 16.",
         pv=opts_grid([("Web hiện tại", "web", ""), ("App hiện tại", "mobile", ""), ("App nếu gộp về 8", "mobile", "--radius-field:var(--radius-md);--radius-inner:var(--radius-md)"), ("Web nếu gộp về 12", "web", "--radius-field:var(--radius-xl);--radius-inner:var(--radius-xl)")]),
         opts=[("keep", "Giữ tách theo chiều cao: web 8, app 12. Không màn nào đổi", True), ("eight", "Gộp về 8: mọi ô nhập và khối trong thẻ trên app bớt 4", False), ("twelve", "Gộp về 12: mọi ô nhập và khối trong thẻ trên web thêm 4", False)]),
    dict(id="rd02", grp="Gộp Web · App", title="Thẻ: 12 trên web, 16 trên app. Gộp không?",
         why=f"<code>radius/card</code> được {len(used_by('radius-card'))} component gọi, nhiều nhất trong các vai. Gộp về 12 không làm xấu máy đo, còn sửa luôn hai ca app đang rớt (Badge trên Vehicle Card, vòng icon ô bấm tải lên); gộp về 16 làm rớt thêm ba ca web (dòng tệp, Badge trên Vehicle Card, mục trong menu tài khoản). Đổi lại, trên app thẻ 12 chứa ô nhập 12 thì mất bậc ngoài lớn hơn trong, và DEC-165 đã chốt \"app thẻ và nhóm bo 16 = lề 16 đều 4 phía\". Trang đề xuất giữ, sửa hai ca rớt bằng lề ở <a href='#rd06'>rd06</a>. <b>Mở lại DEC-165:</b> chỉ khi chọn gộp; bằng chứng mới là hai ca rớt trên app. Thẻ web 16 trùng phương án \"tròn\" DEC-122 đã bỏ.",
         untitled="<code>rounded-xl</code> = 12 cho bảng, cả web lẫn màn nhỏ (<code>application/table/table.tsx</code>).",
         ours="<code>radius/card</code>: Web 12, App 16 (DEC-165 hạ app 20 → 16).",
         astryx="Web <code>container</code> 12; app <code>card-mobile</code> 22.",
         pv=opts_grid([("Web hiện tại", "web", ""), ("App hiện tại", "mobile", ""), ("App nếu gộp về 12", "mobile", "--radius-card:var(--radius-xl)"), ("Web nếu gộp về 16", "web", "--radius-card:var(--radius-2xl)")]),
         opts=[("keep", "Giữ tách: web 12, app 16. Sửa ca rớt bằng lề", True), ("twelve", "Gộp về 12: mọi thẻ app bớt 4, hai ca rớt tự hết", False), ("sixteen", "Gộp về 16: mọi thẻ web thêm 4, rớt thêm ba ca trên web", False)]),
    dict(id="rd03", grp="Gộp Web · App", title="Hộp thoại và sheet: 16 trên web, 24 trên app. Gộp không?",
         why=f"<code>radius/overlay</code> có {len(used_by('radius-overlay'))} component gọi. Trên web là hộp thoại nổi bốn góc; trên app là sheet chỉ bo hai góc trên, rộng hết màn. Hai hình khác nhau nên số không nhất thiết phải bằng. Untitled đi ngược: màn nhỏ bo ít hơn. Sheet 16 vẫn dùng được, nên đây là chọn theo nhìn, không phải theo máy đo. <b>Mở lại DEC-259:</b> chỉ khi chọn gộp; bằng chứng mới là Màu và Chữ đã về một bộ.",
         untitled="<code>sm:rounded-2xl</code> = 16, màn nhỏ <code>rounded-xl</code> = 12 (<code>application/modals/modal.tsx</code>).",
         ours="<code>radius/overlay</code>: Web 16, App 24 (DEC-259 đổi web 12 → 16, app 28 → 24).",
         astryx="Dialog <code>container</code> 12; đầu sheet app <code>page</code> 28.",
         pv='<div class="pv3">' + sheet("var(--radius-overlay)", "Kết thúc chuyến?", "App hiện tại, 24", "Bạn sẽ không sửa được số km sau khi kết thúc.") + sheet("var(--radius-2xl)", "Kết thúc chuyến?", "App nếu gộp về 16", "Bạn sẽ không sửa được số km sau khi kết thúc.") + sheet("var(--radius-xl)", "Kết thúc chuyến?", "Theo Untitled màn nhỏ, 12", "Bạn sẽ không sửa được số km sau khi kết thúc.") + "</div>",
         opts=[("keep", "Giữ tách: hộp thoại web 16, sheet app 24", True), ("sixteen", "Gộp về 16: mọi sheet app bớt 8", False)]),
    dict(id="rd04", grp="Đúng vai", title="Ba sheet trên app đang có ba bo: 24, 28, 16",
         why=f"Help sheet gọi <code>radius/overlay</code> 24 (DEC-301 đã đổi 28 → 24). Sheet tài khoản gọi <code>radius/card</code> 16. Sheet chọn nguồn file giữ <code>upload/sheet-radius</code> 28: DEC-259 đã bỏ 28 từ 26/10, nhưng 29/10 chủ DS vẫn chọn giữ 28 và bỏ phương án 24 (DEC-307, cột Bỏ: \"bo sheet 24 theo DEC-259\"); DEC-315 chỉ ghi số này còn lệch thang. <b>Mở lại DEC-307:</b> bằng chứng mới là ba sheet trên app đang có ba độ bo, và token nằm trong đợt 2 của DEC-319, tức nhóm số trần phải quyết từng số trên trang review. Avatar đầu sheet tài khoản rớt máy đo cả trước và sau khi đổi (R {n(RES[i_avatar]['R'])} → {n(RES_FIX[i_avatar]['R'])}, lề {n(RES[i_avatar]['lx'])}); lề trên chưa ghi trong spec nên ca này ghi ngoại lệ tới khi vẽ lại, avatar tròn nên mắt không thấy chạm góc.",
         untitled="Không có sheet riêng; <code>application/modals/modal.tsx</code> dùng một bo cho mọi hộp.",
         ours="<code>radius/overlay</code> 24, <code>upload/sheet-radius</code> 28, <code>radius/card</code> 16 (<code>design-system/components/application/field-upload.md</code>, <code>design-system/components/application/header-navigation.md</code>).",
         astryx="Mọi đầu sheet <code>page</code> 28 (DEC-098).",
         pv='<div class="pv3">' + sheet("var(--radius-overlay)", "Trợ giúp", "Help sheet, 24", "Số km lấy từ đồng hồ xe.") + sheet("var(--upload-sheet-radius)", "Chọn nguồn file", "Sheet upload, 28", "Máy ảnh, thư viện hoặc tệp.") + sheet("var(--radius-card)", "Nguyễn Văn Hoà", "Sheet tài khoản, 16", "Lái xe · Đội Cát Lái") + "</div>",
         opts=[("over", "Mọi sheet gọi radius/overlay: upload 28 → 24, tài khoản 16 → 24, bỏ upload/sheet-radius", True), ("keep28", "Sửa tài khoản về 24, giữ upload 28 như DEC-307", False), ("keep", "Giữ cả ba như đang vẽ", False)]),
    dict(id="rd05", grp="Lồng góc", title="Menu thả: bo 8, lề 4, mục 6 đang rớt máy đo",
         why=f"Luật ở <code>design-system/foundations/radius.md</code> mục 5: \"Khung ôm sát một khối … đồng tâm: R = r + lề\". Menu: 6 + 4 = 10, khung đang 8, lệch 2, quá sai số ±1 (DEC-165). Menu breadcrumbs trong chính DS đã dùng 10 và đạt. Đổi <code>radius/menu</code> về <code>radius/lg</code> thì {len(used_by('radius-menu'))} component chịu ảnh hưởng: header-navigation đúng vai, nhưng Badge LG và Avatar XL mượn vai này để lấy số 8, phải trỏ lại <code>radius/md</code> trước. Menu tài khoản đang đạt nhờ mượn <code>radius/card</code> (12 = 6 + 6); về đúng vai thì R {n(RES_FIX[i_menu]['R'])}, lề 6, r 6, cần 12, rớt; nên đặt lề <code>space/xs</code> 4 như mọi menu khác, đạt. Dropdown của Untitled cũng rớt máy đo này: khung 8, lề ngang 6, mục 6. <b>Mở lại DEC-259:</b> phần \"menu 8\"; bằng chứng mới là số đo trên chính luật lồng góc DEC-259 giữ, và menu breadcrumbs 10 đang đạt.",
         untitled="<code>rounded-lg</code> = 8, lề <code>px-1.5</code> = 6, mục <code>rounded-md</code> = 6 (<code>base/dropdown/dropdown.tsx</code>). Thanh tab của họ thì đồng tâm: khung <code>rounded-[10px]</code>, lề 4, tab 6.",
         ours="<code>radius/menu</code> 8, <code>radius/menu-item</code> 6, lề <code>space/xs</code> 4.",
         astryx="Không có vai menu riêng; popover <code>container</code> 12.",
         pv=before_after(i_menu, "Sau khi đổi, radius/menu = 10") + before_after(i_acct, "Sau: radius/menu 10, lề 4"),
         opts=[("lg", "radius/menu về 10; menu tài khoản gọi radius/menu, lề 6 → 4; Badge LG, Avatar XL trỏ radius/md, nhìn không đổi", True), ("item", "Giữ menu 8, hạ mục về radius/xs 4: mọi mục menu bớt 2", False), ("keep", "Giữ 8 và 6 như Untitled, ghi ngoại lệ máy đo", False)]),
    dict(id="rd06", grp="Lồng góc", title="Ba ca trên app rớt máy đo vì lề nhỏ hơn bo",
         why=f"Cùng một số: bản web đạt, sang app bo thẻ 16 và khối trong 12 lớn lên mà lề giữ 12 hoặc 8. Luật DEC-165: \"bo không quá lề\". Badge trên Vehicle Card: R 16, cách góc 12. Vòng icon ô bấm tải lên: R 16, lề 12; đổi lề thì ô cao từ 72 lên {n(px('--featured-icon-size', 'mobile') + 32)}. Khe Container trong khối mooc: R 12, lề 8. Spec <code>field-upload.md</code> cột giá trị còn ghi 14 cho ô bấm trong khi token là <code>space/lg</code> 12; trang đo theo token.",
         untitled="Không có các khối này. Thẻ tài khoản chân sidebar của họ <code>rounded-xl</code> 12, lề <code>p-3</code> 12: bo không quá lề.",
         ours="<code>radius/card</code> App 16, <code>radius/inner</code> App 12, lề <code>space/lg</code>, <code>space/md</code>.",
         astryx="Không có luật lồng góc; thẻ app 22 với lề 16 sẽ rớt.",
         note="Phụ thuộc sp08: nếu chọn sửa, thì <code>upload/app-tap-min-height</code> 72 → 80 để ô bấm tải lên đủ lề 16.",
         pv=before_after(i_badge_m, "Sau: cách góc 16") + before_after(i_upload, "Sau: lề 16") + before_after(i_slot_m, "Sau: lề 12"),
         opts=[("fix", "Nâng lề cả ba ca trên app, bản web giữ nguyên; component bị đánh stale", True), ("keep", "Giữ như đang vẽ, ghi ba ngoại lệ vào radius.md", False)]),
    dict(id="rd07", grp="Lồng góc", title="Thẻ phạm vi ở chân Sidebar rớt máy đo cả hai dạng",
         why="Sidebar đã duyệt (DEC-288, DEC-295) nên đây là <b>đổi nét đã duyệt, chỉ làm khi bạn đồng ý</b>; hai DEC đó không ghi số bo, số nằm ở spec. Dạng mở: R 10, lề 8/10, ô module bo 8. Dạng thu gọn: R 8, lề 4, ô 32 bo 8; đồng tâm cần R 12 hoặc ô bo 4. Đề xuất: dạng mở khung xuống <code>radius/md</code> 8, ô module về <code>radius/inner</code> 8 theo <a href='#rd09'>rd09</a>, lề đạt. Dạng thu gọn nếu cũng <code>radius/inner</code> 8 thì vẫn rớt (8 + 4 = 12, khung 8), nên ghi <b>ngoại lệ</b>: ô module thu gọn gọi <code>radius/xs</code> 4.",
         untitled="Thẻ tài khoản chân sidebar dùng <code>rounded-xl</code> 12 với lề 12 (<code>application/app-navigation/base-components/nav-account-card.tsx</code>).",
         ours="<code>radius/lg</code> 10 và <code>radius/control</code> 8 (<code>design-system/components/application/sidebar-navigation.md</code>).",
         astryx="Chân menu bo <code>container</code> 12, lề 8, ô icon 32.",
         pv=before_after(i_scope, "Sau: R 8") + before_after(i_scope2, "Sau: ô bo 4"),
         opts=[("fix", "Mở: khung 10 → 8, ô radius/inner. Thu gọn: ô 8 → 4, ghi ngoại lệ. Đều đạt máy đo", True), ("keep", "Giữ như đã duyệt, ghi hai ngoại lệ vào radius.md", False)]),
    dict(id="rd08", grp="Token Component", title="Ô đếm trong Badge bo 3: số lệch thang duy nhất của Base",
         why=f"<code>chip/count-radius</code> 3 chờ đợt 2 trong sổ <code>design-system/components/_token-ledger.json</code> (DEC-319). Số 3 không vô cớ: Badge 6 trừ lề 3 đúng bằng 3, <code>design-system/components/base/badge.md</code> ghi \"bo ô đếm đồng tâm với badge\" (DEC-303). Vào thang được: <code>radius/xxs</code> 2 cho SM (2 + 3 = 5) và MD (2 + 4 = 6) đều đạt trong sai số ±1. <code>radius/xs</code> 4 thì MD thành 8, rớt. DEC-314 bỏ làm tròn hàng loạt nhưng để chốt từng số trên trang review, nên mục này không mở lại DEC đó.",
         untitled="Badge của họ không có ô đếm bo vuông: phần <code>addon</code> chỉ là chữ và icon, không có nền riêng (<code>base/badges/badges.tsx</code>).",
         ours="<code>chip/count-radius</code> 3 ở SM, MD; <code>radius/xs</code> 4 ở LG.",
         astryx="Badge bo <code>full</code>, không có ô đếm bo vuông.",
         pv=before_after(i_sm, "Sau: radius/xxs 2") + before_after(i_md, "Sau: radius/xxs 2"),
         opts=[("xxs", "Bỏ chip/count-radius, SM và MD gọi radius/xxs 2; nhìn đổi 1px ở ô cao 16", True), ("keep", "Giữ 3 làm ngoại lệ ghi trong sổ, vì đúng đồng tâm tuyệt đối", False)]),
    dict(id="rd09", grp="Đúng vai", title="Mười vai có thừa không: tab trùng control, chip không ai gọi",
         why=f"Sổ <code>design-system/_review/token-usage.json</code> báo {len(dups)} nhóm trùng số. Hai nhóm là vai trỏ vào bậc thang (<code>radius/sm</code>, <code>radius/md</code>), bình thường; ba nhóm còn lại đáng xét: <code>radius/tab</code> = <code>radius/control</code> trên cả hai nền, mà {len(used_by('radius-tab'))} component gọi tab đều không phải tab (bảng \"Vai đang gọi sai chỗ\"); <code>radius/chip</code> = <code>radius/full</code> và {len(used_by('radius-chip'))} component gọi. <code>radius/field</code> = <code>radius/inner</code> cũng trùng nhưng khác nghĩa, ô nhập có thể đổi độc lập khối trong nên giữ. Cùng hướng gộp với DEC-319. <b>Mở lại DEC-134:</b> phần tên <code>radius/chip</code>, số giữ; bằng chứng là không component nào gọi. Featured icon vuông chốt <code>radius/inner</code> (Web 8, App 12): Upload web đang bo 8 theo <code>design-system/components/application/field-upload.md</code> dòng 53 (gọi <code>radius/tab</code>), còn <code>design-system/foundations/icon.md</code> mục 3.1 ghi \"vuông bo 14\" là lệch tài liệu, 14 đã bỏ từ DEC-259.",
         note="Phụ thuộc ic10: nếu chọn bỏ <code>radius/tab</code>, trang Icon theo Featured icon vuông = <code>radius/inner</code> (Web 8, App 12) thay cho số 14. Ô module Sidebar về <code>radius/inner</code> 8, dạng thu gọn là ngoại lệ <code>radius/xs</code> 4 (<a href='#rd07'>rd07</a>).",
         untitled="Không có tầng vai; component gọi thẳng <code>rounded-*</code>.",
         ours="10 vai trong <code>design-system/foundations/radius.md</code>: 6 khác Web và App, 4 bằng nhau.",
         astryx="3 vai: <code>element</code>, <code>container</code>, <code>page</code>.",
         pv=opts_grid([("Tab đang gọi radius/tab", "mobile", ""), ("Gọi radius/control, nhìn y hệt", "mobile", "--radius-tab:var(--radius-control)")], body=lambda: '<span class="tp-btn" style="border-radius:var(--radius-tab)"><span class="type-label">Tất cả lệnh</span></span> <span class="tp-chip tp-g" style="border-radius:var(--radius-full)">Hoàn thành</span>', cls="pvw"),
         opts=[("trim", "Bỏ radius/tab, radius/chip; trỏ lại các chỗ gọi sai vai. Không màn nào đổi trên web", True), ("tab", "Chỉ bỏ radius/chip, giữ radius/tab cho component Tabs sau này", False), ("keep", "Giữ đủ 10 vai", False)]),
    dict(id="rd10", grp="Còn mở", title="Corner smoothing: có bật góc liền mạch cho thẻ, sheet trên app không",
         why=f"<code>design-system/foundations/README.md</code> mục 13 còn mở câu này, <code>radius.md</code> ghi \"iOS dùng góc liền mạch\". Số đo dựng theo <a href='https://www.figma.com/blog/desperately-seeking-squircles/'>blog Figma</a>: ξ = 0,6 khớp iOS, đoạn tay nắm chia a : b theo 2/3 và 1/3. Lệch tối đa so với góc tròn thường là {n(round(DEV16, 1))}px ở R 16 và {n(round(DEV24, 1))}px ở R 24; <b>số này chỉ đúng với hình của Figma</b>, hình của Flutter và CSS chưa đo. App là Flutter (<code>docs/_shared/system-overview.md</code>): có <a href='https://api.flutter.dev/flutter/painting/RoundedSuperellipseBorder-class.html'><code>RoundedSuperellipseBorder</code></a>, đặt được một chỗ ở theme qua <a href='https://api.flutter.dev/flutter/material/CardThemeData/shape.html'><code>CardThemeData.shape</code></a>; bản Flutter dự án đang dùng chưa kiểm. Web: <a href='https://developer.mozilla.org/en-US/docs/Web/CSS/corner-shape'>MDN</a> xếp <code>corner-shape</code> vào \"Limited availability\", chưa Baseline. Figma: <a href='https://developers.figma.com/docs/plugins/api/VariableBindableNodeField/'>danh sách <code>VariableBindableNodeField</code></a> không có <code>cornerSmoothing</code>, nên không gắn được biến, phải nhập tay từng khung. Đổi lấy chưa tới nửa px thì chưa đáng.",
         untitled="<code>tokens.untitled.json</code> và <code>design/_ref/untitled-ui/04-spacing-radius-grid.md</code> không nhắc smoothing; react dùng góc CSS thường.",
         ours="Chưa bật; <code>radius/card</code> App 16, <code>radius/overlay</code> App 24.",
         astryx="Không có trong <code>design/design.md</code>.",
         pv=(f'<div class="pv3"><div class="pane" data-theme="light" data-platform="mobile"><span class="lab">R 24, góc thường</span>{smooth_svg(200, 120, 24, False)}</div>'
             f'<div class="pane" data-theme="light" data-platform="mobile"><span class="lab">R 24, liền mạch 60%</span>{smooth_svg(200, 120, 24, True)}</div>'
             f'<div class="pane" data-theme="light" data-platform="mobile"><span class="lab">Phóng to góc: nét đứt là thường</span>{smooth_zoom(24)}</div></div>'),
         opts=[("off", "Không bật, đóng câu hỏi ở mục 13; ghi rõ vào radius.md", True), ("on", "Bật 60% cho thẻ, sheet trên app: Figma nhập tay từng khung, Flutter đặt RoundedSuperellipseBorder ở theme, web giữ góc thường", False)]),
]

SPEC = dict(
    slug="radius", short="phần Bo góc",
    title="Foundations · Bo góc — vai nào tách, góc nào lồng sai",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
    lead=(f"Trang giúp quyết <b>có gộp Web và App không</b> và sửa <b>{FAILS} ca lồng góc đang rớt</b>. Kết luận chính: thang 11 bậc đã trùng Untitled nên không bàn lại (DEC-315); <mark>6 vai còn tách vẫn có lý do</mark> vì bo đi theo chiều cao control, khác Màu và Chữ. Việc đáng làm là gom ba sheet về một bo và sửa lề. <mark>Chưa sửa token nào.</mark>"),
    kpis=[(f"{SAME_SCALE}/11", "bậc thang trùng Untitled", "ok"), (f"{len(SPLIT)}/10", "vai khác nhau giữa Web và App", ""), (f"{FAILS}/{MEASURED}", "ca lồng góc đo được đang rớt", "bad"),
          (f"{FAILS_FIX}", "ca còn rớt nếu theo khuyến nghị", ""), ("3", "bo khác nhau của sheet trên app", "bad"), (f"{pending_n}/{merged_n + pending_n}", "token Component về bo chờ đợt 2 (nhóm số trần DEC-319 quyết trên trang review)", "")],
    tag_kind="radius",
    screens=dict(
        title="Xem trên màn mẫu",
        intro="Bộ màn danh sách, chi tiết, biểu mẫu, xác nhận dựng từ <code>tokens.css</code> thật. <b>Bộ giá trị</b> chỉ đổi menu nổi về 10 (<a href='#rd05'>rd05</a>), vì khuyến nghị giữ tách các vai. <b>Thử gộp Web · App</b> đặt cả 6 vai về một bộ để bạn thấy mọi màn đổi thế nào trước khi trả lời <a href='#rd00'>rd00</a> đến <a href='#rd03'>rd03</a>. Bật <b>Nhãn số đo</b> để đọc bo góc từng khối.",
        proposal_css=".tp-f.tp-prop{--radius-menu:var(--radius-lg)}", logo_svg=None, gridov=False, overlay_html=None),
    sections=[
        dict(title="Bảng đối chiếu thang 11 bậc — Untitled ↔ mình", intro="Nguồn Untitled: <code>design/_ref/untitled-ui/04-spacing-radius-grid.md</code> mục 5 (Figma v8). Cột component đếm từ <code>design-system/_review/token-usage.json</code>, chỉ tính chỗ gọi thẳng; <code>radius/2xl</code>, <code>radius/4xl</code> được dùng gián tiếp qua vai. <code>radius/none</code>, <code>radius/3xl</code> chưa ai gọi, vẫn giữ vì DEC-315 đã chốt đủ thang.",
             html=scale_viz() + kit.rows(["Untitled", "rem · px", "Của mình", "px", "Primitive", "Component gọi thẳng", "Vai trỏ vào", "Trạng thái"], scale_rows())
             + '<div class="note"><b>Tên lớp trong code Untitled lệch tên Figma.</b> Code React dùng thang mặc định Tailwind, repo không khai <code>--radius-*</code>: <code>rounded-lg</code> là 8 trong khi Figma v8 gọi 8 là <code>radius-md</code>. Bảng dưới đã quy về px, không so theo tên.</div>'),
        dict(title="Bảng đối chiếu token theo vai — Untitled ↔ mình", intro=f"Untitled không có tầng vai, nên cả 10 dòng đều <b>Chỉ mình có</b> về mặt tên; cột So số px đối chiếu số họ thật sự dùng trong component (<code>design/_ref/untitled-ui/react/components</code>). {len(SPLIT)} vai khác Web và App, mục hỏi gộp ở rd00 đến rd03.",
             html=kit.rows(["Vai", "Web", "App", "Web · App", "Số comp.", "Component gọi", "Untitled dùng thật", "File", "So số px"], role_rows())),
        dict(title="Ma trận lồng góc — đo trên trình duyệt", intro=f"Luật nguyên văn ở <code>design-system/foundations/radius.md</code> mục 5, DEC-165: \"mỗi khối có hình nằm gần góc khung đạt khi lề ≥ R, hoặc hai lề của góc chênh ≤ 1 và R = r + lề ± 1\". Mỗi ô là khung dựng bằng biến thật; khối cao đúng cỡ, số đọc từ tokens.css và được đọc lại trên trình duyệt. <b>R</b> bo khung, <b>r</b> bo khối, hình tròn thì r = cao ÷ 2. Luật chưa định nghĩa \"gần góc\" bằng số, trang dùng: cả hai lề dưới 2R. Chưa đo: ảnh lấn mép Vehicle Card, vì ảnh xe nền trong suốt nên không có góc hình; hàng sheet chỉ có chữ và vạch. Kết quả: <b>{FAILS}/{MEASURED} rớt</b>, còn {FAILS_FIX} nếu theo khuyến nghị.",
             html=MATRIX),
        dict(title="Token Component về bo góc và sổ rà", intro=f"Sổ <code>design-system/components/_token-ledger.json</code> (DEC-319): {merged_n} token đã gộp, {pending_n} chờ đợt 2.",
             html=kit.rows(["Token", "Số gốc", "Thay bằng", "Dùng cho", "Trạng thái"], ledger_rows()) + kit.rows(["Sổ <code>token-usage.json</code>", "Mục về bo", "Thực tế"], CMPRAW_ROWS)),
        dict(title="Vai đang gọi sai chỗ", intro="Đọc từ spec component. Những chỗ này làm đổi một vai kéo theo khối không liên quan.",
             html=kit.rows(["Vai", "Đang gọi ở", "Vấn đề", "Nên gọi", "Mục"], MISUSE)),
        dict(title="Đã chốt, không mở lại", intro="Các DEC đang hiệu lực mà trang chỉ áp, không hỏi lại. Chỗ nào mở lại thì mục đó ghi rõ \"Mở lại DEC-…:\".",
             html=kit.rows(["DEC", "Đã chốt"], [
                 ["DEC-315", "Bo góc ba tầng: primitive theo px, thang Semantic tên Untitled, token theo vai trỏ vào thang."],
                 ["DEC-259", "Thang 11 bậc bỏ 14 và 28; mục menu 6, badge vuông 6."],
                 ["DEC-165", "Luật lồng góc và máy đo: lề ≥ R, hoặc hai lề chênh ≤ 1 và R = r + lề ± 1."],
                 ["DEC-314", "Không thêm bậc Semantic cho số lẻ; số lệch thang chốt từng số."],
                 ["DEC-319", "Token Component gộp về token chung theo 2 đợt, giữ sổ để tách lại sau."],
                 ["DEC-196", "Nút lọc trong ô tìm trên app ôm sát, lề 4, bo đồng tâm."],
                 ["DEC-266", "Vehicle Thumb bo <code>radius/sm</code> · <code>radius/md</code> · <code>radius/lg</code>; token riêng đã gộp theo DEC-319."],
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", intro="Thang giữ nguyên 11 bậc. Vai còn lại sau khi chọn:", html=kit.rows(["Token", "Web · App", "Việc"], ROLE_AFTER)),
    ],
    items=ITEMS,
    final="Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/radius.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>radius = approved</b> (<code>ds-foundation-status.py set radius approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). Việc riêng của trang: đóng dòng Corner smoothing ở <code>design-system/foundations/README.md</code> mục 13; các mục đổi nét đã duyệt (Sidebar, sheet upload) chỉ áp theo lựa chọn của bạn.",
    css=CSS, js=JS,
)
