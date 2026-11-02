#!/usr/bin/env python3
"""SPEC trang review Chuyển động: thang thời gian, đường cong, chuyển động theo component, giảm chuyển động. Dựng: python3 _scripts/foundation_review/build.py motion"""
import collections
import glob
import json
import os
import re

import kit
from kit import ROOT, icon, panes, rows

OK, DIFF, GAP, OWN = "st-ok", "st-diff", "st-gap", "st-own"
LAB = {OK: "Giống", DIFF: "Khác có lý do", GAP: "Mình thiếu", OWN: "Chỉ mình có"}


def st(s, note=""):
    return f'<span class="{s}">{LAB[s]}</span>' + (f'<br><span class="small muted">{note}</span>' if note else "")


# ---------- đếm thật: Untitled ----------
UDIR = ROOT / "design/_ref/untitled-ui/react/components"
_u = []
for r, _, fs in os.walk(UDIR):
    for f in fs:
        if f.endswith((".tsx", ".ts", ".css")) and ".demo." not in f and ".story" not in f:
            _u.append((os.path.relpath(os.path.join(r, f), UDIR), open(os.path.join(r, f), encoding="utf-8", errors="ignore").read()))
UT = "\n".join(x for _, x in _u)
U_FILES = len(_u)
U_DUR = collections.Counter(re.findall(r"\bduration-(\d+)\b", UT))
U_EASE = collections.Counter(re.findall(r"\bease-(linear|in-out|out|in)\b", UT))
U_ANIM = collections.Counter(re.findall(r"animate-(in|out|spin|caret-blink|marquee)\b", UT))
U_DUR_TOTAL = sum(U_DUR.values())
U_EASE_TOTAL = sum(U_EASE.values())
U_SLIDE05 = len(re.findall(r"slide-(?:in-from|out-to)-(?:top|bottom|left|right)-0\.5", UT))
U_SLIDEFULL = len(re.findall(r"slide-(?:in-from|out-to)-right[^-]", UT))
U_ZOOM = len(re.findall(r"zoom-(?:in|out)-95", UT))
U_ALL = len(re.findall(r"\btransition-all\b", UT))
U_INH = len(re.findall(r"\btransition-inherit", UT))
U_REDUCE = len(re.findall(r"motion-reduce:|motion-safe:|prefers-reduced", UT))
U_REDUCE_FILES = sorted({p for p, x in _u if re.search(r"motion-reduce:|motion-safe:|prefers-reduced", x)})
U_SKEL = sum(1 for p, x in _u if re.search(r"skeleton", x + p, flags=re.I))
U_MOTION_LIB = sum(1 for _, x in _u if re.search(r'from "motion', x))
U_THEME = (ROOT / "design/_ref/untitled-ui/raw/theme.css").read_text()
U_THEME_DUR = len(re.findall(r"--(?:duration|ease)[\w-]*\s*:", U_THEME))
U_THEME_ANIM = len(re.findall(r"--animate-[\w-]+\s*:", U_THEME))

# ---------- đếm thật: của mình ----------
PAGES = sorted(glob.glob(str(ROOT / "design-system/components/_work/*/page.json")))
page_txt = {p.split("/")[-2]: open(p, encoding="utf-8").read() for p in PAGES}
USE = re.compile(r"(transition|animation)\s*:\s*([^;}\"\\]{1,80})")
use_all = collections.Counter()
use_page = collections.defaultdict(collections.Counter)
for name, s in page_txt.items():
    for k, v in USE.findall(s):
        use_all[(k, v.strip())] += 1
        use_page[name][(k, v.strip())] += 1
USE_TOTAL = sum(use_all.values())
USE_VAR = sum(n for (_, v), n in use_all.items() if "var(--duration" in v)
USE_RAW = USE_TOTAL - USE_VAR
ALLP = " ".join(page_txt.values())
VAR_DUR = collections.Counter(re.findall(r"var\(--(duration-\w+)\)", ALLP))
VAR_EASE = len(re.findall(r"var\(--easing-\w+\)", ALLP))
P_RM = sum(1 for s in page_txt.values() if "prefers-reduced" in s)
P_MOVE = len(use_page)
SPECS = glob.glob(str(ROOT / "design-system/components/base/*.md")) + glob.glob(str(ROOT / "design-system/components/application/*.md"))
SPEC_TOK = sum(1 for p in SPECS if re.search(r"duration/|easing/|--duration|--easing", open(p, encoding="utf-8").read()))
SPEC_N = len(SPECS)
TJ = json.loads((ROOT / "design-system/tokens.json").read_text())["motion"]
F_TOKENS = len(TJ)
TOK_FAST, TOK_MED, TOK_SLOW = (int(TJ[f"duration/{k}"][:-2]) for k in ("fast", "medium", "slow"))
n_raw = lambda k, v: use_all[(k, v)]


# ---------- đường cong: đo đạt bao nhiêu % sau bao nhiêu % thời gian ----------
def t_at(c, p):
    x1, y1, x2, y2 = c
    lo, hi = 0.0, 1.0
    for _ in range(60):
        s = (lo + hi) / 2
        y = 3 * (1 - s) ** 2 * s * y1 + 3 * (1 - s) * s * s * y2 + s ** 3
        lo, hi = (s, hi) if y < p else (lo, s)
    return 3 * (1 - s) ** 2 * s * x1 + 3 * (1 - s) * s * s * x2 + s ** 3


STD = tuple(float(x) for x in re.findall(r"[\d.]+", TJ["easing/standard"]))
EOUT, EIN, EIO = (0, 0, .2, 1), (.4, 0, 1, 1), (.4, 0, .2, 1)
ms90 = lambda d, c=STD: round(d * t_at(c, .9))
M90 = {d: ms90(d) for d in (TOK_FAST, TOK_MED, TOK_SLOW)}
STD_50 = round(t_at(STD, .5) * 100)
STD_90 = round(t_at(STD, .9) * 100)

# ---------- splash: logo Delta thật ----------
_vb = re.search(r'viewBox="[\d. ]+ ([\d.]+) ([\d.]+)"', (ROOT / "design/brand/delta/logo/delta-primary.svg").read_text())
DELTA_RATIO = float(_vb.group(1)) / float(_vb.group(2))
APP_W, APP_M = 393, 16
LOGO_W = APP_W - 2 * APP_M
LOGO_H = round(LOGO_W / DELTA_RATIO)
PEAK = LOGO_W * 1.15
OVER = (PEAK - APP_W) / 2
CAP = APP_W / LOGO_W
SPLASH_MS = 900 + 1000 + 900 + 600
_lg_n = [0]


def delta_logo():
    _lg_n[0] += 1
    out = []
    for name, cls in (("primary", "lg-l"), ("reverse", "lg-d")):
        x = re.sub(r"<\?xml[^>]*>", "", (ROOT / f"design/brand/delta/logo/delta-{name}.svg").read_text())
        pre = f"{cls}{_lg_n[0]}"
        x = re.sub(r'id="([^"]+)"', lambda m: f'id="{pre}{m.group(1)}"', x)
        x = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{pre}{m.group(1)})", x)
        out.append(x.replace("<svg ", f'<svg class="{cls}" ', 1))
    return "".join(out)


vn = lambda x: str(x).replace(".", ",")
code = lambda x: f"<code>{x}</code>"

# ---------- bảng đối chiếu ----------
DUR_ROWS = [
    ("<code>duration-50</code>", "n:50 ms", f"n:{U_DUR['50']}", "không có", st(DIFF, "Tag; không cần bậc riêng, dùng <code>duration/fast</code>")),
    ("<code>duration-75</code>", "n:75 ms", f"n:{U_DUR['75']}", "không có", st(DIFF, "Thanh tiến độ; mình chạy đều theo số phần trăm")),
    ("<code>duration-100</code>", "n:100 ms", f"n:{U_DUR['100']}", "<code>duration/fast</code> 125 ms", st(DIFF, "Cùng vai hover, đổi màu; DEC-139 giữ 125")),
    ("<code>duration-150</code>", "n:150 ms", f"n:{U_DUR['150']}", "<code>duration/fast</code> 125 ms", st(DIFF, "Menu, công tắc; mục mt05")),
    ("<code>duration-200</code>", "n:200 ms", f"n:{U_DUR['200']}", "không có bậc", st(DIFF, "Lúc đóng modal; mục mt06")),
    ("<code>duration-300</code>", "n:300 ms", f"n:{U_DUR['300']}", "<code>duration/medium</code> 300 ms", st(OK, "Modal, slideout mở ra")),
    ("<code>duration-500</code>", "n:500 ms", f"n:{U_DUR['500']}", "không có bậc", st(DIFF, "Slideout đóng; chậm hơn lúc mở, không lấy")),
    ("không có", "—", "n:—", "<code>duration/slow</code> 700 ms", st(OWN, "Vòng lặp; mục mt01")),
]
EASE_ROWS = [
    ("<code>ease-linear</code>", "linear", f"n:{U_EASE['linear']}", "chưa có luật", st(GAP, "Mục mt02: mình cần cho vòng lặp, thanh giờ")),
    ("<code>ease-out</code>", "cubic-bezier(0, 0, 0.2, 1)", f"n:{U_EASE['out']}", "<code>easing/standard</code>", st(DIFF, "Một đường cong, DEC-139")),
    ("<code>ease-in</code>", "cubic-bezier(0.4, 0, 1, 1)", f"n:{U_EASE['in']}", "<code>easing/standard</code>", st(DIFF, "Một đường cong, DEC-139")),
    ("<code>ease-in-out</code>", "cubic-bezier(0.4, 0, 0.2, 1)", f"n:{U_EASE['in-out']}", "<code>easing/standard</code>", st(DIFF, "Một đường cong, DEC-139")),
    ("không có", "—", "n:—", "<code>easing/standard</code> cubic-bezier(0.24, 1, 0.4, 1)", st(OWN, "Giữ từ Astryx")),
]
ANIM_ROWS = [
    ("<code>animate-in</code>, <code>animate-out</code> + <code>fade-*</code>", "mờ dần", f"n:{U_ANIM['in'] + U_ANIM['out']}", "chưa có luật hình chuyển động", st(GAP, "Mục mt05, mt06")),
    ("<code>zoom-in-95</code>, <code>zoom-out-95</code>", "phóng 95% ↔ 100%, chỉ modal", f"n:{U_ZOOM}", "chưa có luật", st(GAP, "Mục mt06")),
    ("<code>slide-in-from-*-0.5</code>", "trượt 2 px, menu", f"n:{U_SLIDE05}", "chưa có luật", st(GAP, "Mục mt05")),
    ("<code>slide-in-from-right</code>", "trượt hết bề rộng, slideout", f"n:{U_SLIDEFULL}", "chưa có luật", st(GAP, "Mục mt06")),
    ("<code>animate-spin</code>", "1 s, linear", f"n:{U_ANIM['spin']}", f"Số trần: 1 s ở {n_raw('animation', 'fsp 1s linear infinite')} chỗ, .8 s ở {n_raw('animation', 'spn .8s linear infinite')} chỗ", st(OK, "Cùng 1 s, chưa qua token; mục mt09")),
    ("<code>animate-caret-blink</code>", "1 s", f"n:{U_ANIM['caret-blink']}", f"Số trần 1 s ở {n_raw('animation', 'car 1s steps(1) infinite')} chỗ", st(OK, "Con trỏ giả trong màn mẫu")),
    ("<code>animate-marquee</code>", "60 s, chữ chạy", f"n:{U_ANIM['marquee']}", "không có", st(GAP, "Không lấy: chỉ trang trí màn rỗng")),
    ("Thư viện <code>motion</code>, kiểu lò xo", "damping 26, stiffness 220", f"n:{U_MOTION_LIB} file", "không có", st(DIFF, "DEC-139: không bounce, không spring")),
    ("Thư viện <code>sonner</code> cho toast", "khai trong package.json, 0 component trong ref", "n:0", "Spec <code>design-system/components/base/alert-notification.md</code>", st(DIFF, "Mục mt07")),
    (f"Skeleton", "không có", f"n:{U_SKEL} file", "Nhắc trong <code>design-system/foundations/motion.md</code>, chưa có spec", st(OWN, "Mục mt08")),
    ("<code>transition</code>, <code>transition-colors</code>, <code>transition-shadow</code>", "mọi thuộc tính hoặc theo nhóm", "n:—", "Theo từng thuộc tính", st(DIFF, "Foundation cấm <code>all</code>")),
    ("<code>transition-all</code>", "mọi thuộc tính", f"n:{U_ALL}", "cấm", st(DIFF, "Ô nhập của họ dùng, mình không lấy")),
    ("<code>transition-inherit-all</code>", "con kế thừa cha", f"n:{U_INH}", "không có", st(DIFF, "Tiện ích riêng của Tailwind, Angular và Flutter không cần")),
    ("<code>motion-reduce:animate-none</code>", f"chỉ {len(U_REDUCE_FILES)} file: màn rỗng", f"n:{U_REDUCE}", "<code>design-system/tokens.css</code> đưa mọi thời gian về 0", st(DIFF, "Mình rộng hơn nhưng số trần lọt ra; mục mt13")),
]
_all = [r[-1] for r in DUR_ROWS + EASE_ROWS + ANIM_ROWS]
CNT = {s: sum(1 for c in _all if f'class="{s}"' in c) for s in LAB}
TOTAL = len(_all)

USE_ROWS = [(f"<code>{k}: {v.replace('var(--duration-fast)', 'var(--duration-fast)')}</code>", f"n:{n}",
             ", ".join(sorted(p for p, c in use_page.items() if (k, v) in c)),
             '<span class="st-ok">qua biến</span>' if "var(--duration" in v else '<span class="st-gap">số trần</span>')
            for (k, v), n in use_all.most_common()]

# ---------- atom xem thử ----------
LINES = [("LVT-2026-0412", "Cát Lái → KCN Long Hậu", "tp-b", "Đang chạy"), ("LVT-2026-0411", "ICD Phước Long → Bình Dương", "tp-g", "Hoàn thành"),
         ("LVT-2026-0409", "Hiệp Phước → Đồng Nai", "tp-y", "Chờ duyệt"), ("LVT-2026-0407", "Cát Lái → Tân Vạn", "tp-g", "Hoàn thành"),
         ("LVT-2026-0403", "Phú Hữu → Sóng Thần", "tp-b", "Đang chạy"), ("LVT-2026-0398", "Tân Cảng → Biên Hoà", "tp-y", "Chờ duyệt")]


def lines(idx=(0, 1, 2, 3)):
    return "".join(f'<div class="mt-line" style="--i:{n}"><span class="type-code">{LINES[i][0]}</span><span class="type-body mt-grow">{LINES[i][1]}</span><span class="tp-chip {LINES[i][2]}">{LINES[i][3]}</span></div>' for n, i in enumerate(idx))


def stage(inner, label="Phát", mode="cycle", hold=1400, style="", cls="", cap=""):
    c = f'<span class="type-caption tp-sub">{cap}</span>' if cap else ""
    s = f' style="{style}"' if style else ""
    return (f'<div class="mt-st {cls}" data-mode="{mode}" data-hold="{hold}"{s}><div class="mt-ctl"><button class="tp-btn sec mt-play" type="button"><span class="type-label">{label}</span></button>{c}</div>{inner}</div>')


def scene(inner, h=200, idx=(0, 1, 2, 3)):
    return f'<div class="mt-scene" style="height:{h}px"><div class="mt-lines">{lines(idx)}</div>{inner}</div>'


SCRIM = '<div class="mt-scrim mt-a"></div>'
DLG = ('<div class="mt-center"><div class="tp-dlg mt-a mt-zoom"><div class="type-title-3">Duyệt lệnh LVT-2026-0412?</div><div class="type-body tp-sub">Lệnh gửi tới tài xế Nguyễn Văn Hoà ngay sau khi duyệt.</div>'
       '<div class="tp-acts"><span class="tp-btn sec"><span class="type-label">Để sau</span></span><span class="tp-btn"><span class="type-label">Duyệt lệnh</span></span></div></div></div>')
SHEET = ('<div class="tp-dlg tp-sheet mt-a mt-sheet"><div class="type-title-3">Kết thúc chuyến LVT-2026-0412?</div><div class="type-body tp-sub">Bạn sẽ không sửa được số km sau khi kết thúc.</div>'
         '<span class="tp-btn wide"><span class="type-label">Kết thúc chuyến</span></span></div>')
DRAWER = '<div class="mt-a mt-drawer"><div class="type-title-3">Bộ lọc lệnh</div><div class="type-body tp-sub">Trạng thái, tuyến, tài xế.</div></div>'
MENU = (f'<div class="tp-menu mt-a mt-menu"><span>{icon("pencil")}<span class="type-body">Sửa lệnh</span></span><span>{icon("copy")}<span class="type-body">Nhân bản</span></span>'
        f'<span class="tp-err">{icon("trash-2")}<span class="type-body">Huỷ lệnh</span></span></div>')
TIP = '<div class="mt-tip mt-a"><span class="type-caption">Cước đã gồm phụ phí nâng hạ</span></div>'


def toast(cls=""):
    return (f'<div class="mt-a mt-toast {cls}"><span class="mt-ok">{icon("circle-check")}</span><div class="mt-grow"><div class="type-heading">Đã duyệt lệnh LVT-2026-0412</div><div class="type-caption tp-sub">Tài xế đã nhận thông báo.</div></div><i class="mt-timer"></i></div>')


def race(rows_):
    out = ""
    for lab, d, e, read in rows_:
        val = f'<span class="type-code" data-read="{read}"></span>' if read else (f'<span class="type-code">{d}</span>' if not d.startswith("var(") else '<span></span>')
        out += f'<div class="mt-row" style="--d:{d};--e:{e}"><span class="type-caption">{lab}</span><div class="mt-track"><i class="mt-dot"></i></div>{val}</div>'
    return out


T_FAST, T_MED, T_SLOW = "var(--duration-fast)", "var(--duration-medium)", "var(--duration-slow)"
E_STD = "var(--easing-standard)"


def sk_rows(n=3):
    return "".join('<div class="mt-skrow"><i class="mt-sk" style="width:30%"></i><i class="mt-sk" style="width:55%"></i><i class="mt-sk" style="width:15%"></i></div>' for _ in range(n))


def curve_svg():
    w, h = 300, 150
    path = lambda c, st_, dash="": (f'<path d="M0 {h} C{c[0]*w:.1f} {h-c[1]*h:.1f} {c[2]*w:.1f} {h-c[3]*h:.1f} {w} 0" fill="none" stroke="currentColor" stroke-width="2" style="{st_}" {dash}/>')
    y90 = h * .1
    return (f'<svg viewBox="-2 -2 {w+4} {h+4}" class="mt-svg" role="img" aria-label="So sánh tiến độ theo thời gian của các đường cong">'
            f'<line x1="0" x2="{w}" y1="{y90}" y2="{y90}" stroke="currentColor" stroke-dasharray="3 4" style="color:var(--color-border-primary)"/>'
            f'<line x1="0" x2="{w}" y1="{h}" y2="{h}" stroke="currentColor" style="color:var(--color-border-primary)"/>'
            + path(STD, "color:var(--color-fg-primary)") + path(EOUT, "color:var(--color-utility-blue-500)", 'stroke-dasharray="6 4"')
            + path(EIN, "color:var(--color-utility-yellow-500)", 'stroke-dasharray="2 4"') + f'<line x1="0" y1="{h}" x2="{w}" y2="0" stroke="currentColor" style="color:var(--color-fg-quaternary)"/></svg>')


# ---------- xem thử từng mục ----------
def pv_scale(m, p):
    return stage(f'<div class="type-caption tp-sub">Của mình, đọc từ biến thật</div>{race([("duration/fast", T_FAST, E_STD, "--duration-fast"), ("duration/medium", T_MED, E_STD, "--duration-medium"), ("duration/slow", T_SLOW, E_STD, "--duration-slow")])}'
                 f'<div class="type-caption tp-sub">Untitled, số Tailwind</div>{race([("duration-100", "100ms", "linear", ""), ("duration-150", "150ms", "cubic-bezier(0,0,.2,1)", ""), ("duration-300", "300ms", "cubic-bezier(0,0,.2,1)", "")])}', mode="replay")


def pv_slow(m, p):
    return ('<div class="mt-2">'
            + stage(scene(SCRIM + DLG, 220), label="Hộp xác nhận 300", style=f"--d:{T_MED}", cap="<code>duration/medium</code>")
            + stage(scene(SCRIM + DLG, 220), label="Hộp xác nhận 700", style=f"--d:{T_SLOW}", cap="<code>duration/slow</code>, không nên")
            + "</div>" + stage(f'<div class="mt-sks">{sk_rows(2)}</div>', label="Vòng lặp 700, chạy 5 giây", mode="loop", cap="Hợp vai nhất của <code>duration/slow</code>: một chiều 700, cả vòng 1400"))


def pv_ease(m, p):
    tbl = rows(["Đường cong", "Đạt 50%", "Đạt 90%", "90% của 300 ms"],
               [["<b>easing/standard</b> (nét liền đậm)", f"n:{round(t_at(STD, .5)*100)}% thời gian", f"n:{STD_90}% thời gian", f"n:{ms90(300)} ms"],
                ["Tailwind <code>ease-out</code> (gạch dài)", f"n:{round(t_at(EOUT, .5)*100)}%", f"n:{round(t_at(EOUT, .9)*100)}%", f"n:{ms90(300, EOUT)} ms"],
                ["Tailwind <code>ease-in</code> (chấm)", f"n:{round(t_at(EIN, .5)*100)}%", f"n:{round(t_at(EIN, .9)*100)}%", f"n:{ms90(300, EIN)} ms"],
                ["<code>linear</code> (nét mảnh)", "n:50%", "n:90%", "n:270 ms"]])
    return (f'{curve_svg()}{tbl}'
            + stage(race([("easing/standard", T_MED, E_STD, ""), ("Tailwind ease-out", T_MED, "cubic-bezier(0,0,.2,1)", ""), ("Tailwind ease-in", T_MED, "cubic-bezier(.4,0,1,1)", ""), ("linear", T_MED, "linear", "")]), mode="replay")
            + '<div class="mt-2">' + stage(f'<div class="mt-sks">{sk_rows(1)}</div>', label="Vòng lặp linear", mode="loop", cap="Đều, không giật")
            + stage(f'<div class="mt-sks">{sk_rows(1)}</div>', label="Vòng lặp đường cong chuẩn", mode="loop", style=f"--eloop:{E_STD}", cap="Lao nhanh rồi đứng") + "</div>")


def pv_raw(m, p):
    cv = f'<span class="mt-cv">{icon("chevron-down")}</span><span class="type-label">Vận hành</span>'
    return ('<div class="mt-2">' + stage(f'<div class="mt-navrow">{cv}</div>', label="Số trần hiện tại", mode="toggle", style="--d:150ms;--e:ease", cap="<code>transform .15s</code>, đường cong mặc định")
            + stage(f'<div class="mt-navrow">{cv}</div>', label="Qua biến", mode="toggle", style=f"--d:{T_FAST};--e:{E_STD}", cap="<code>duration/fast</code> + <code>easing/standard</code>") + "</div>"
            + f'<p class="type-caption tp-sub">Bật giảm chuyển động: bản qua biến về 0, bản số trần vẫn chạy. Đang đọc từ máy bạn: <code data-read="--duration-fast"></code>.</p>')


def pv_hover(m, p):
    return ('<div class="mt-2">'
            + stage('<div class="mt-fakes"><span class="tp-btn mt-hv"><span class="type-label">Duyệt lệnh</span></span><span class="tp-btn sec mt-hv2"><span class="type-label">Để sau</span></span></div>', label="Giả lập rê chuột", mode="cycle", hold=800, style=f"--d:{T_FAST}", cap="Rê thật lên nút cũng chạy")
            + stage('<div class="mt-fakes"><span class="tp-btn sec mt-ring"><span class="type-label">Hiện ngay</span></span><span class="tp-btn sec mt-ring mt-ringf"><span class="type-label">Mờ dần 300</span></span></div>', label="Giả lập phím Tab", mode="cycle", hold=900, cap="Bên trái là đề xuất")
            + "</div>")


def pv_menu(m, p):
    menu = lambda lab, d, cap, e=E_STD, dx=None: stage(scene(MENU, 190), label=lab, style=f"--d:{d};--e:{e}" + (f";--dx:{dx};--ex:cubic-bezier(.4,0,1,1)" if dx else ""), hold=1000, cap=cap)
    return ('<div class="pv3">' + menu("125", T_FAST, "<code>duration/fast</code>") + menu("300", T_MED, "<code>duration/medium</code>, foundation đang ghi")
            + menu("Untitled", "150ms", "Vào 150, ra 100", "cubic-bezier(0,0,.2,1)", "100ms") + "</div>"
            + stage(f'<div class="mt-scene mt-tipscene" style="height:88px">{TIP}<span class="type-body">Cước: 1.250.000 ₫</span></div>', label="Tooltip, chờ 300 rồi hiện 125", style=f"--d:{T_FAST};--wait:300ms", cls="mt-waitin", hold=1400))


def pv_dialog(m, p):
    box = SCRIM + (DLG if p == "web" else SHEET)
    return ('<div class="mt-2">' + stage(scene(box, 250), label="Vào 300, ra 300", style=f"--d:{T_MED}", cap="Đề xuất")
            + stage(scene(box, 250), label="Vào 300, ra 125", style=f"--d:{T_MED};--dx:{T_FAST}") + "</div>"
            + stage(scene(box, 250), label="Untitled: vào 300, ra 200", style="--d:300ms;--e:cubic-bezier(0,0,.2,1);--dx:200ms;--ex:cubic-bezier(.4,0,1,1)", cap="Hai đường cong"))


def pv_toast(m, p):
    c = "" if p == "web" else "mt-toast-app"
    return ('<div class="mt-2">' + stage(scene(toast(c), 190), label="Trượt 8 + mờ dần", style=f"--d:{T_MED};--dx:{T_FAST}", hold=3000, cls="mt-timed", cap="Thanh giờ 3 giây chạy đều")
            + stage(scene(toast(c + " mt-nomove"), 190), label="Chỉ mờ dần", style=f"--d:{T_MED};--dx:{T_FAST}", hold=3000, cls="mt-timed") + "</div>")


def pv_skel(m, p):
    return ('<div class="pv3">' + stage(f'<div class="mt-sks">{sk_rows()}</div>', label="Nhấp nháy", mode="loop", cap="Chạy 5 giây rồi tĩnh")
            + stage(f'<div class="mt-sks mt-shim">{sk_rows()}</div>', label="Vệt sáng", mode="loop", cap="Tốn hơn, nhiễu trên bảng dày")
            + stage(f'<div class="mt-sks mt-static">{sk_rows()}</div>', label="Đứng yên", mode="loop", cap="Không chạy") + "</div>")


def pv_spin(m, p):
    b = f'<span class="tp-btn sec mt-spinbtn"><span class="mt-spn">{icon("loader-circle")}</span><span class="type-label">Duyệt lệnh</span></span>'
    return ('<div class="pv3">' + stage(b, label="Xong sau 200, có chờ", hold=200, style="--wait:300ms", cap="Không nháy")
            + stage(b, label="Xong sau 200, không chờ", hold=200, style="--wait:0ms", cap="Nháy một cái")
            + stage(b, label="Xong sau 2 giây, có chờ", hold=2000, style="--wait:300ms", cap="Hiện từ mili giây 300") + "</div>"
            + '<div class="mt-2">' + stage(b, label="Chu kỳ 1000", mode="loop", style="--wait:0ms;--sp:1000ms") + stage(b, label="Chu kỳ 800", mode="loop", style="--wait:0ms;--sp:800ms") + "</div>")


def pv_splash(m, p):
    frame = lambda: f'<div class="mt-splash"><i class="mt-guide"></i><div class="mt-lg">{delta_logo()}<i class="mt-sweep"></i></div></div>'
    return (stage(frame(), label="Như đang ghi: 115%", mode="replay", style=f"--w:{LOGO_W}px;--sc:1.15", cap=f"Rộng {LOGO_W} → {round(PEAK)}, vượt màn {vn(round(OVER, 1))} px mỗi bên")
            + stage(frame(), label=f"Đề xuất: chặn ở bề rộng màn", mode="replay", style=f"--w:{LOGO_W}px;--sc:{CAP:.3f}", cap=f"Delta phóng {vn(round(CAP * 100, 1))}%, logo hẹp vẫn 115%"))


def pv_tab(m, p):
    bd = lambda: ('<div class="mt-tabs"><span class="mt-tab mt-t1"><span class="type-label">Đang chạy (128)</span></span><span class="mt-tab mt-t2"><span class="type-label">Chờ duyệt (16)</span></span><i class="mt-ind"></i></div>'
                  f'<div class="mt-pa">{lines((0, 4))}</div><div class="mt-pb">{lines((2, 5))}</div>')
    return ('<div class="pv3">' + stage(bd(), label="Đổi tab", mode="toggle", style=f"--d:0ms;--dc:{T_FAST}", cap="Gạch chân nhảy, chữ đổi màu 125")
            + stage(bd(), label="Đổi tab", mode="toggle", style=f"--d:{T_FAST};--dc:{T_FAST}", cap="Gạch chân trượt 125")
            + stage(bd(), label="Đổi tab", mode="toggle", style=f"--d:{T_MED};--dc:{T_MED}", cls="mt-tabfade", cap="Trượt 300, nội dung mờ dần") + "</div>")


def pv_side(m, p):
    b = lambda: f'<div class="mt-sbw"><aside class="mt-sb"><span class="mt-cv2">{icon("clipboard-list")}</span><span class="type-label mt-sbl">Lệnh vận tải</span></aside><div class="mt-lines mt-grow">{lines((0, 1))}</div></div>'
    return ('<div class="pv3">' + stage(b(), label="Thu gọn", mode="toggle", style="--d:0ms", cap="Đổi ngay")
            + stage(b(), label="Thu gọn", mode="toggle", style=f"--d:{T_FAST}", cap="Chạy 125, bảng xếp lại nhiều lần")
            + stage(b(), label="Thu gọn", mode="toggle", style="--d:300ms;--e:cubic-bezier(.4,0,.2,1)", cap="Untitled 300") + "</div>")


def pv_reduced(m, p):
    body = lambda: scene(SCRIM + DLG, 220) + f'<div class="mt-fakes"><span class="mt-spn mt-spn-keep">{icon("loader-circle")}</span><span class="type-caption mt-rmtxt">Đang tải…</span></div><div class="mt-sks">{sk_rows(1)}</div>'
    return ('<div class="mt-2">' + stage(body(), label="Bình thường", cap="Đọc biến của máy bạn: <code data-read=\"--duration-medium\"></code>", hold=1600)
            + stage(body(), label="Giả lập giảm chuyển động", cls="mt-rm", hold=1600, cap="Mọi thời gian 0, spinner dừng, thêm chữ") + "</div>")


def pv_app(m, p):
    box = SCRIM + (DLG if p == "web" else SHEET)
    return stage(scene(box, 260), label="Mở, đóng", style=f"--d:{T_MED}", cap="Cùng <code>duration/medium</code>, cùng đường cong")


def pv_wcag(m, p):
    return (stage(f'<div class="mt-wc"><div class="mt-fakes"><span class="mt-spn mt-spn-keep">{icon("loader-circle")}</span><span class="type-caption">Spinner: 0 lần loé</span></div>'
                  f'<div class="mt-fakes"><span class="mt-dt mt-dtp"></span><span class="type-caption">Chấm: {vn(round(1000 / (TOK_SLOW * 2), 2))} lần mỗi giây</span></div>'
                  f'<div class="mt-fakes"><span class="mt-caret"></span><span class="type-caption">Con trỏ: 1 lần mỗi giây</span></div><div class="mt-sks">{sk_rows(1)}</div></div>', label="Chạy cả bộ 5 giây", mode="loop", style="--wait:0ms", cap="Dưới mốc 3 lần mỗi giây"))


def pv_dot(m, p):
    r = lambda c: "".join(f'<div class="mt-line"><span class="mt-dt {c}"></span><span class="type-code">51C-482.1{i}</span><span class="type-body mt-grow">Đang chạy · Cát Lái</span></div>' for i in range(5))
    return ('<div class="mt-2">' + stage(f'<div>{r("mt-dtp")}</div>', label="Mọi dòng nhấp nháy", mode="loop", cap="Đang ghi trong foundation")
            + stage(f'<div>{r("")}</div>', label="Đứng yên + nhãn", mode="loop", cap="Đề xuất") + "</div>")


def pv_dense(m, p):
    bd = lambda: f'<div class="mt-lines mt-la">{lines((0, 1, 2, 3))}</div><div class="mt-lines mt-lb">{lines((2, 5, 4, 3))}</div>'
    return ('<div class="pv3">' + stage(bd(), label="Lọc", mode="toggle", cap="Đổi ngay: chờ 0 ms")
            + stage(bd(), label="Lọc", mode="toggle", cls="mt-fade", cap="Mờ dần: 125 ms mỗi lần lọc")
            + stage(bd(), label="Lọc", mode="toggle", cls="mt-fade mt-stag", cap="Lần lượt: 125 + 3 × 60 = 305 ms") + "</div>")


def pv_blur(m, p):
    v = lambda lab, cls, cap: stage(scene(SCRIM + DLG, 230) + '<div class="type-caption tp-sub mt-fps">Chưa đo</div>', label=lab, mode="measure", cls=cls, hold=1200, cap=cap)
    return ('<div class="mt-stack">' + v("Mờ lớp phủ, bán kính giữ", "", "<code>backdrop-blur/lg</code> cố định")
            + v("Chạy cả bán kính blur", "mt-blurrun", "0 → 24, tốn nhất") + v("Máy yếu: không blur", "mt-solid", "<code>color/bg/overlay_solid</code>") + "</div>")


# ---------- màn thật ----------
def overlay(body):
    web = lambda t_, inner, cls="", style="": f'<div class="tp-f tp-prop mt-demo" data-platform="web">{stage(inner, label=t_, cls=cls, style=style)}</div>'
    app = lambda t_, inner, cls="", style="": f'<div class="tp-f tp-prop mt-demo mt-demoapp" data-platform="mobile">{stage(inner, label=t_, cls=cls, style=style)}</div>'
    extra = ('<div class="tp-h">Bấm để chạy <small>· menu đổi theo nút Bộ giá trị: Hiện tại 300, Sau khi đổi 125. Đọc từ biến thật, đổi được Sáng, Tối</small></div><div class="tp-scroll"><div class="tp-row">'
             + web("Mở menu", scene(MENU, 230), cls="mt-menust") + web("Mở hộp xác nhận", scene(SCRIM + DLG, 230))
             + web("Hiện toast", scene(toast(), 230), cls="mt-timed", style=f"--dx:{T_FAST}")
             + app("Mở sheet", scene(SCRIM + SHEET, 300, (0, 1, 2, 3))) + app("Hiện toast", scene(toast("mt-toast-app"), 300), cls="mt-timed", style=f"--dx:{T_FAST}") + "</div></div>")
    return extra + body


# ---------- CSS, JS ----------
CSS = r"""
.mt-st{--d:var(--duration-medium);--e:var(--easing-standard);--dx:var(--d);--ex:var(--e);--dloop:var(--duration-slow);--eloop:linear;--sp:1000ms;--wait:0ms;--dc:var(--duration-fast);--w:361px;--sc:1;display:grid;gap:var(--space-md);min-width:0;align-content:start}
.mt-ctl{display:flex;flex-wrap:wrap;gap:var(--space-sm) var(--space-md);align-items:center;min-width:0}
.mt-play{border:0;font:inherit;cursor:pointer;height:auto;min-height:var(--control-height-sm);padding:var(--space-xs) var(--space-lg);white-space:normal;text-align:left}
.mt-play:focus-visible{outline:2px solid var(--color-focus-ring);outline-offset:2px}
.mt-grow{flex:1;min-width:0}.mt-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-lg)}
.pv3 .mt-st{min-width:0}.pane{display:grid;gap:var(--space-lg);align-content:start}.pane>.lab{margin:0}
.mt-reset,.mt-reset *{transition:none!important;animation:none!important}
/* đua: chấm chạy trên đường, thời gian và đường cong đọc từ --d --e */
.mt-row{display:grid;grid-template-columns:128px minmax(0,1fr) 66px;gap:var(--space-md);align-items:center}
.mt-track{container-type:inline-size;height:14px;border-radius:var(--radius-full);background:var(--color-bg-secondary)}
.mt-dot{display:block;width:14px;height:14px;border-radius:var(--radius-full);background:var(--color-fg-primary);transition:transform var(--d) var(--e)}
.mt-st.go .mt-dot{transform:translateX(calc(100cqw - 14px))}
/* cảnh nền */
.mt-scene{position:relative;overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);background:var(--color-bg-primary)}
.mt-lines{padding:var(--space-md) var(--space-lg);display:grid}
.mt-line{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) 0;border-bottom:1px solid var(--color-border-secondary);min-width:0}
.mt-line .type-body{overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.mt-a{opacity:0;pointer-events:none;transition:opacity var(--dx) var(--ex),transform var(--dx) var(--ex)}
.mt-st.go .mt-a{opacity:1;transform:none;transition-duration:var(--d);transition-timing-function:var(--e)}
.mt-scrim{position:absolute;inset:0;background:var(--color-bg-overlay);backdrop-filter:blur(var(--backdrop-blur-lg));display:block}
.mt-solid .mt-scrim{background:var(--color-bg-overlay_solid);backdrop-filter:none}
.mt-blurrun .mt-scrim{backdrop-filter:blur(0);transition:opacity var(--dx) var(--ex),backdrop-filter var(--dx) var(--ex)}
.mt-st.mt-blurrun.go .mt-scrim{backdrop-filter:blur(var(--backdrop-blur-lg));transition:opacity var(--d) var(--e),backdrop-filter var(--d) var(--e)}
.mt-center{position:absolute;inset:0;display:grid;place-items:center;padding:var(--space-md);pointer-events:none}
.mt-center .tp-dlg{width:min(340px,100%);padding:var(--space-xl)}
.mt-zoom{transform:scale(.95)}
.tp-dlg.mt-sheet{position:absolute;left:0;right:0;bottom:0;opacity:1;transform:translateY(100%);padding:var(--space-xl)}
.mt-drawer{position:absolute;top:0;right:0;bottom:0;width:60%;opacity:1;transform:translateX(100%);background:var(--color-bg-primary_alt);border-left:1px solid var(--shadow-xl-border);box-shadow:var(--shadow-xl);padding:var(--space-xl)}
.mt-st .tp-menu.mt-menu{top:var(--space-lg);right:var(--space-lg);transform:translateY(-4px);width:min(200px,70%)}
.mt-st.go .tp-menu.mt-menu{transform:none}
.mt-tip{position:absolute;left:var(--space-lg);top:var(--space-sm);transform:translateY(4px);background:var(--color-bg-primary_solid,var(--color-action-primary));color:var(--color-text-inverse);padding:var(--space-xs) var(--space-md);border-radius:var(--radius-xs)}
.mt-tipscene{padding:var(--space-4xl) var(--space-lg) 0}
.mt-waitin.go .mt-tip{transition-delay:var(--wait)}
.mt-toast{position:absolute;right:var(--space-lg);bottom:var(--space-lg);width:min(320px,calc(100% - 24px));display:flex;gap:var(--space-md);align-items:flex-start;padding:var(--space-lg);background:var(--color-bg-primary_alt);border:1px solid var(--shadow-xl-border);border-radius:var(--radius-card);box-shadow:var(--shadow-xl);transform:translateY(8px);overflow:hidden}
.mt-toast-app{left:var(--space-lg);right:var(--space-lg);width:auto;bottom:var(--space-lg)}.mt-nomove{transform:none}
.mt-ok{color:var(--color-utility-green-700)}
.mt-timer{position:absolute;left:0;bottom:0;height:4px;width:100%;background:var(--color-utility-green-500);transform-origin:left;transform:scaleX(1)}
.mt-timed.go .mt-timer{transform:scaleX(0);transition:transform 3000ms linear}
/* vòng lặp */
.mt-sks{display:grid;gap:var(--space-md)}.mt-skrow{display:flex;gap:var(--space-md);align-items:center}
.mt-sk{display:block;height:12px;border-radius:var(--radius-xs);background:var(--color-bg-selected)}
.mt-st.go .mt-sk{animation:mt-pulse var(--dloop) var(--eloop) infinite alternate}
.mt-shim .mt-sk{background:linear-gradient(90deg,var(--color-bg-selected) 25%,var(--color-bg-primary) 50%,var(--color-bg-selected) 75%);background-size:200% 100%}
.mt-st.go .mt-shim .mt-sk{animation:mt-shimk calc(var(--dloop) * 2) linear infinite}
.mt-st.go .mt-static .mt-sk{animation:none}
@keyframes mt-pulse{to{opacity:.45}}@keyframes mt-shimk{from{background-position:200% 0}to{background-position:0 0}}
@keyframes mt-spin{to{transform:rotate(360deg)}}
.mt-spn{display:inline-flex;opacity:0;width:var(--icon-size-md);height:var(--icon-size-md)}.mt-st.go .mt-spn{opacity:1;transition:opacity 0s linear var(--wait);animation:mt-spin var(--sp) linear infinite}
.mt-spn-keep{opacity:1}.mt-spinbtn{width:fit-content}
.mt-rmtxt{display:none}.mt-rm .mt-rmtxt{display:inline}
.mt-st.mt-rm{--d:0ms;--dx:0ms;--dloop:0ms}.mt-st.mt-rm.go .mt-sk,.mt-st.mt-rm.go .mt-spn{animation:none}
.mt-dt{width:10px;height:10px;border-radius:var(--radius-full);background:var(--color-utility-green-500);flex:none;display:inline-block}
.mt-st.go .mt-dtp{animation:mt-pulse var(--dloop) linear infinite alternate}
.mt-caret{width:2px;height:16px;background:var(--color-fg-primary);display:inline-block}.mt-st.go .mt-caret{animation:mt-car 1s steps(1) infinite}@keyframes mt-car{50%{opacity:0}}
.mt-wc{display:grid;gap:var(--space-md);grid-template-columns:repeat(2,minmax(0,1fr));align-items:center}.mt-fakes{display:flex;flex-wrap:wrap;gap:var(--space-md);align-items:center}
/* hover, focus, chevron */
.mt-hv,.mt-hv2{transition:background var(--d) var(--e)}.mt-st.go .mt-hv,.mt-hv:hover{background:var(--color-action-primary-hover)}.mt-st.go .mt-hv2,.mt-hv2:hover{background:var(--color-bg-primary_hover)}
.mt-ring{outline:2px solid transparent;outline-offset:2px}.mt-ringf{transition:outline-color var(--duration-medium) var(--easing-standard)}.mt-st.go .mt-ring{outline-color:var(--color-focus-ring)}
.mt-navrow{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) var(--space-md);border:1px solid var(--color-border-secondary);border-radius:var(--radius-menu-item)}
.mt-cv{display:inline-flex;transform:rotate(-90deg);transition:transform var(--d) var(--e)}.mt-st.go .mt-cv{transform:none}
.mt-svg{width:100%;max-width:340px;display:block}
/* tab */
.mt-tabs{position:relative;display:flex;border-bottom:1px solid var(--color-border-secondary)}.mt-tab{flex:1;min-width:0;padding:var(--space-sm) var(--space-xs);transition:color var(--dc) var(--e)}
.mt-t2{color:var(--color-text-tertiary)}.mt-st.go .mt-t1{color:var(--color-text-tertiary)}.mt-st.go .mt-t2{color:var(--color-text-primary)}
.mt-ind{position:absolute;left:0;bottom:-1px;width:50%;height:2px;background:var(--color-action-primary);transition:transform var(--d) var(--e)}.mt-st.go .mt-ind{transform:translateX(100%)}
.mt-pb,.mt-lb{display:none}.mt-st.go .mt-pa,.mt-st.go .mt-la{display:none}.mt-st.go .mt-pb,.mt-st.go .mt-lb{display:grid}
.mt-tabfade.go .mt-pb{animation:mt-in var(--d) var(--e) both}
.mt-fade.go .mt-lb .mt-line{animation:mt-in var(--duration-fast) var(--easing-standard) both}.mt-stag.go .mt-lb .mt-line{animation-delay:calc(var(--i) * 60ms)}
@keyframes mt-in{from{opacity:0}}
/* menu thu gọn */
.mt-sbw{display:flex;overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);min-height:120px}
.mt-sb{flex:none;width:112px;display:flex;gap:var(--space-sm);align-items:flex-start;padding:var(--space-md);border-right:1px solid var(--color-border-secondary);overflow:hidden;transition:width var(--d) var(--e);box-sizing:border-box}
.mt-st.go .mt-sb{width:40px}.mt-sbl{white-space:nowrap}
/* splash, khung app 393 */
.mt-splash{position:relative;width:393px;max-width:100%;height:170px;overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);background:var(--color-bg-primary);display:grid;place-items:center}
.mt-guide{position:absolute;inset:0 16px;border-inline:1px dashed var(--color-border-error);pointer-events:none}
.mt-lg{position:relative;width:var(--w);line-height:0}.mt-lg svg{width:100%;height:auto;display:block}.mt-lg .lg-d{display:none}[data-theme="dark"] .mt-lg .lg-d{display:block}[data-theme="dark"] .mt-lg .lg-l{display:none}
.mt-sweep{position:absolute;inset:0;background:linear-gradient(100deg,transparent 40%,color-mix(in srgb,var(--color-bg-primary) 75%,transparent) 50%,transparent 60%);background-size:300% 100%;background-position:120% 0;opacity:0}
.mt-st.go .mt-lg{animation:mt-spl 3400ms both}.mt-st.go .mt-sweep{animation:mt-sw 3400ms both}
@keyframes mt-spl{0%{opacity:0;transform:translateX(-12px);animation-timing-function:var(--easing-standard)}26.47%{opacity:1;transform:none}82.35%{opacity:1;transform:none;animation-timing-function:var(--easing-standard)}100%{opacity:1;transform:scale(var(--sc))}}
@keyframes mt-sw{0%,26.47%{opacity:1;background-position:120% 0}55.88%{opacity:1;background-position:-20% 0}56%,100%{opacity:0}}
/* cỡ khung màn mẫu */
.mt-demo{width:440px;padding:var(--space-lg);min-height:0}.mt-demoapp{width:393px}
.tp-f .mt-menust{--d:var(--duration-medium)}
.pane .tw{margin:0;border-color:var(--color-border-secondary)}.pane .cmp{background:transparent;color:inherit}.pane .cmp th{background:var(--color-bg-secondary);color:var(--color-text-secondary)}.pane .cmp th,.pane .cmp td{border-color:var(--color-border-secondary)}
.pane.pane code,.tp-f code{background:var(--color-bg-secondary);color:var(--color-text-primary)}
.mt-lines{container-type:inline-size}.mt-line .type-code{white-space:nowrap}
@container (max-width:300px){.mt-line .tp-chip{display:none}}@container (max-width:180px){.mt-line .type-body{display:none}}
.mt-center{grid-template-columns:minmax(0,1fr)}.mt-center .tp-dlg{justify-self:center}.mt-center .tp-acts{flex-wrap:wrap}
.mt-st.go .mt-sbl{display:none}.mt-stack{display:grid;gap:var(--space-lg)}
@media(max-width:820px){.mt-2{grid-template-columns:minmax(0,1fr)}.mt-row{grid-template-columns:96px minmax(0,1fr) 56px}}
/* trang này tôn trọng giảm chuyển động: số trần của Untitled cũng dừng */
@media (prefers-reduced-motion: reduce){.mt-st,.mt-st *{transition-duration:0s!important;transition-delay:0s!important;animation:none!important}}
"""

JS = r"""
(function(){
 const R=matchMedia('(prefers-reduced-motion: reduce)');
 function read(){$$('[data-read]').forEach(e=>{const v=getComputedStyle(e).getPropertyValue(e.dataset.read).trim();e.textContent=v||'chưa có'});const n=$('#mtRm');if(n)n.textContent=R.matches?'Máy bạn đang bật giảm chuyển động: mọi bản chạy trên trang hiện tĩnh, đúng luật. Muốn xem chạy thì tắt tuỳ chọn này trong hệ điều hành.':'Máy bạn đang không bật giảm chuyển động. Trang chỉ chạy khi bạn bấm, vòng lặp tự dừng sau 5 giây.'}
 read();if(R.addEventListener)R.addEventListener('change',read);
 const label=(b,t)=>{const l=b.querySelector('.type-label');if(!b.dataset.t)b.dataset.t=l.textContent;l.textContent=t||b.dataset.t};
 function replay(s){s.classList.add('mt-reset');s.classList.remove('go');void s.offsetWidth;s.classList.remove('mt-reset');void s.offsetWidth;s.classList.add('go')}
 function measure(s,ms){const f=s.querySelector('.mt-fps');if(!f)return;let n=0,last=performance.now(),worst=0;const t0=last;function tick(now){n++;worst=Math.max(worst,now-last);last=now;if(now-t0<ms)requestAnimationFrame(tick);else f.textContent='Máy này: '+Math.round(n*1000/(now-t0))+' khung mỗi giây, khung chậm nhất '+Math.round(worst)+' ms'}requestAnimationFrame(tick)}
 document.addEventListener('click',e=>{const b=e.target.closest('.mt-play');if(!b)return;const s=b.closest('.mt-st');if(!s)return;const m=s.dataset.mode,h=+s.dataset.hold||1400;clearTimeout(s._t);
  if(m==='replay'){replay(s);return}
  if(m==='toggle'){s.classList.toggle('go');return}
  if(m==='loop'){if(s.classList.contains('go')){s.classList.remove('go');label(b);return}s.classList.add('go');label(b,'Dừng');s._t=setTimeout(()=>{s.classList.remove('go');label(b)},5000);return}
  replay(s);s._t=setTimeout(()=>s.classList.remove('go'),h);if(m==='measure')measure(s,h+Math.max(400,parseFloat(getComputedStyle(s).getPropertyValue('--duration-medium'))||0))});
})();
"""

# ---------- bảng ----------
MATRIX = rows(["Chỗ dùng", "Thời gian", "Đường cong", "Thuộc tính chạy", "Giảm chuyển động"], [
    ["Hover, nhấn, đổi màu, công tắc", "<code>duration/fast</code> 125", "<code>easing/standard</code>", "<code>background</code>, <code>color</code>, <code>transform</code> của công tắc", "Đổi ngay"],
    ["Vòng focus", "Không chạy, hiện ngay", "—", "—", "Như thường"],
    ["Menu, chọn, popover, tooltip", "<code>duration/fast</code> 125; tooltip chờ 300 mới hiện", "<code>easing/standard</code>", "<code>opacity</code>, trượt 4", "Hiện ngay"],
    ["Hộp thoại", "<code>duration/medium</code> 300 cả vào, ra; thôi chặn bấm ngay khi đóng", "<code>easing/standard</code>", "<code>opacity</code>, phóng 95 → 100", "Hiện ngay"],
    ["Sheet, ngăn kéo", "<code>duration/medium</code> 300 cả vào, ra", "<code>easing/standard</code>", "<code>transform</code>; lớp phủ <code>opacity</code>", "Hiện ngay"],
    ["Toast", "Vào <code>duration/medium</code> 300, ra <code>duration/fast</code> 125", "<code>easing/standard</code>", "<code>opacity</code>, trượt 8", "Hiện ngay; thanh giờ vẫn đếm nhưng không chạy hình"],
    ["Skeleton", "<code>duration/slow</code> 700 một chiều, cả vòng 1400; tối đa 5 giây", "<code>linear</code>", "<code>opacity</code> 100 ↔ 45", "Đứng yên"],
    ["Spinner", "Vòng 1000, chờ 300 mới hiện", "<code>linear</code>", "<code>transform</code>", "Dừng, thêm chữ “Đang tải…”"],
    ["Thanh giờ, thanh tiến độ", "Bằng thời gian thật", "<code>linear</code>", "<code>transform</code>", "Đổi theo từng mốc"],
    ["Tab", "Chữ đổi màu <code>duration/fast</code>; gạch chân, nội dung đổi ngay", "<code>easing/standard</code>", "<code>color</code>", "Đổi ngay"],
    ["Bảng: lọc, sắp xếp, phân trang, thêm dòng", "Không chạy", "—", "—", "Như thường"],
    ["Menu thu gọn", "Bề rộng đổi ngay; chevron <code>duration/fast</code>", "<code>easing/standard</code>", "<code>transform</code>", "Đổi ngay"],
    ["Splash", f"Bốn nhịp 900 · 1000 · 900 · 600, tổng {vn(SPLASH_MS / 1000)} giây, số ghi trong spec Splash", "<code>easing/standard</code>", "<code>opacity</code>, <code>transform</code>", "Logo đứng yên"],
])

FINAL = ("Khi bạn chốt: mình cập nhật <code>design-system/tokens.json</code> → sinh <code>design-system/tokens.css</code> + handoff → sửa <code>design-system/foundations/motion.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>motion = approved</b> "
         "(<code>ds-foundation-status.py set motion approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). "
         "Việc riêng của trang: Figma hiện không có biến thời gian (<code>design/design.md</code> mục Motion ghi vậy, sổ biến Figma của DS cũng 0 biến <code>duration</code>), nên phần Figma chỉ là ghi tên token vào ghi chú prototype; "
         f"đổi {USE_RAW} chỗ số trần trong <code>page.json</code> sang biến; thêm luật giảm chuyển động của Flutter vào handoff; viết spec Skeleton, Spinner khi tới lượt.")

# ---------- SPEC ----------
SPEC = dict(
    slug="motion", short="phần Chuyển động",
    title="Foundations · Chuyển động — thang có đủ, đang dùng có đúng?",
    subtitle=f"Đối chiếu Untitled UI v8 · chọn từng mục · 02/11/2026",
    lead=(f"Trang giúp chốt <b>nhanh chậm bao nhiêu, đường cong nào, component nào chạy ra sao</b>. Kết luận chính: thang 125 · 300 · 700 (DEC-139, giữ 3 dải và một đường cong) <mark>đủ, không cần thêm bậc</mark>, vì đường cong của mình rất dốc: dialog 300 đã đi được 90% sau {M90[TOK_MED]} ms. "
          f"Chỗ yếu là <mark>cách dùng</mark>: {USE_RAW}/{USE_TOTAL} chỗ ghi số trần, nên giảm chuyển động không tắt được. Trang chỉ chạy khi bạn bấm, tôn trọng giảm chuyển động của máy. <mark>Chưa sửa token nào.</mark>"),
    kpis=[(f"{CNT[OK]}/{TOTAL}", "dòng đối chiếu giống Untitled", "ok"), (f"{USE_RAW}/{USE_TOTAL}", "chỗ dùng ghi số trần, không qua token", "bad"), (f"{SPEC_TOK}/{SPEC_N}", "spec nhắc token chuyển động", "bad"),
          (f"{VAR_EASE}", "chỗ dùng easing/standard trong màn mẫu", "bad"), (f"{M90[TOK_MED]} ms", "dialog 300 đạt 90% quãng đường", ""), (f"{vn(round(OVER, 1))} px", "logo Delta vượt màn mỗi bên khi splash phóng 115%", "bad")],
    tag_kind=None,
    screens=dict(title="Xem trên màn thật",
                 intro=('<span id="mtRm"></span> Các khung đầu tiên chạy được, các khung sau là bộ màn mẫu đứng yên (danh sách, chi tiết, biểu mẫu, xác nhận) để so nền. Web rộng 1280, menu 240 (DEC-039), app 393.'),
                 proposal_css=".tp-f.tp-prop .mt-menust{--d:var(--duration-fast)}", overlay_html=overlay),
    sections=[
        dict(title="Bảng đối chiếu từng bậc — Untitled ↔ mình",
             intro=(f"Đếm trên {U_FILES} file code của Untitled (<code>design/_ref/untitled-ui/react/components</code>, bỏ demo) và {len(PAGES)} trang màn mẫu của mình. <b>Untitled không có token thời gian</b>: <code>design/_ref/untitled-ui/raw/theme.css</code> có {U_THEME_DUR} biến thời gian, đường cong và {U_THEME_ANIM} biến <code>--animate-*</code>; họ dùng thẳng số Tailwind. Vì vậy không có tên nào để đặt theo. "
                    f"Tổng {TOTAL} dòng: {CNT[OK]} Giống · {CNT[DIFF]} Khác có lý do · {CNT[GAP]} Mình thiếu · {CNT[OWN]} Chỉ mình có. Giá trị <code>ease-*</code>, <code>animate-spin</code> lấy từ tài liệu Tailwind (tailwindcss.com/docs, đọc 02/11)."),
             html=(rows(["Untitled: thời gian", "Số", "Số chỗ", "Mình", "Trạng thái"], DUR_ROWS)
                   + rows(["Untitled: đường cong", "Giá trị", "Số chỗ", "Mình", "Trạng thái"], EASE_ROWS)
                   + rows(["Untitled: hình chuyển động, thư viện", "Là gì", "Số chỗ", "Mình", "Trạng thái"], ANIM_ROWS))),
        dict(title="Chỗ dùng thật của mình",
             intro=(f"{P_MOVE}/{len(PAGES)} trang màn mẫu có chuyển động; {USE_VAR} chỗ qua biến, {USE_RAW} chỗ số trần. Biến <code>duration/medium</code>, <code>duration/slow</code>, <code>easing/standard</code> có {VAR_DUR['duration-medium']}, {VAR_DUR['duration-slow']}, {VAR_EASE} chỗ dùng. {P_RM} trang tự xử lý giảm chuyển động."),
             html=rows(["Khai báo", "Số chỗ", "Trang", ""], USE_ROWS)),
        dict(title="Đã chốt, không mở lại",
             html=rows(["Mã", "Đã chốt", "Trang này làm gì"], [
                 ["DEC-139", "Ba dải 125 · 300 · 700, một đường cong, tắt khi bật giảm chuyển động, không bounce, không spring", "Giữ số. Mở lại đúng một điểm “một đường cong” ở mục mt02, có lý do tại mục đó"],
                 ["DEC-037", "Splash web: logo khách giữa, innvie ở chân; kịch bản 4 nhịp ở <code>design/design.md</code> mục Splash web", "Giữ kịch bản, chỉ hỏi phần phóng trên app"],
                 ["DEC-326", "Splash dùng logo ngang 64, app rộng tối đa bằng màn trừ lề, Delta cao khoảng 61", f"Không đổi cỡ. Câu này không nói phóng; số 115% nằm ở <code>design/design.md</code>"],
                 ["DEC-325", "Bộ logo Delta vector ở <code>design/brand/delta/logo/delta-primary.svg</code>", "Dùng file thật trong xem thử"],
                 ["DEC-327", "Lớp phủ 35% + <code>backdrop-blur/lg</code>, <code>color/bg/overlay_solid</code> 50% cho máy yếu; toast, dialog, sheet <code>shadow/xl</code>", "Giữ. Chỉ hỏi cách chạy lúc mở, chưa có số đo máy thật"],
                 ["DEC-286, DEC-287", "Toast web dưới phải, app dưới ngay trên thanh tab; có nút tự ẩn tối thiểu 10 giây, dừng đếm khi rê, focus", "Giữ vị trí, thời gian đọc. Chỉ hỏi hình chuyển động"],
                 ["DEC-277", "Nút đang tải trông như Disabled + spinner", "Giữ. Chỉ hỏi thời gian chờ và chu kỳ"],
                 ["DEC-324, DEC-328, DEC-329", "Lưới, bo góc, icon đã chốt", "Xem thử dùng đúng: khung 1280, 393; <code>radius/overlay</code>; Lucide"],
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)",
             intro=f"Bốn token giữ nguyên, <b>không thêm bậc nào ở Foundation</b>. Một số đo riêng của component đi vào sổ <code>design-system/components/_token-ledger.json</code> (DEC-319, “đợt 2” là đợt gộp 59 token Component có số trần).",
             html=(rows(["Token", "Giá trị", "Vai"], [
                 ["<code>duration/fast</code>", f"n:{TOK_FAST} ms", "Đổi trạng thái, menu, tooltip. Đạt 90% sau " + str(M90[TOK_FAST]) + " ms"],
                 ["<code>duration/medium</code>", f"n:{TOK_MED} ms", "Dialog, sheet, toast vào. Đạt 90% sau " + str(M90[TOK_MED]) + " ms"],
                 ["<code>duration/slow</code>", f"n:{TOK_SLOW} ms", "Chỉ cho một chiều của vòng lặp, không cho vào, ra"],
                 ["<code>easing/standard</code>", "n:0.24, 1, 0.4, 1", "Mọi chuyển động có đầu có cuối"],
                 ["<code>linear</code> (từ khoá, không phải token)", "n:—", "Vòng lặp, thanh giờ, thanh tiến độ"],
             ]) + MATRIX)),
    ],
    items=[
        dict(id="mt00", grp="Thang thời gian", title="Thang 125 · 300 · 700 có cần đổi theo Untitled không",
             why=(f"Untitled dùng {len(U_DUR)} số khác nhau ({U_DUR_TOTAL} chỗ), <mark>{round(U_DUR['100'] * 100 / U_DUR_TOTAL)}% là 100 ms</mark>, không đặt thành token. Thang của mình nhìn chậm hơn trên giấy, nhưng đường cong dốc: <mark>đạt 90% quãng đường sau {M90[TOK_FAST]} ms với 125, {M90[TOK_MED]} ms với 300</mark>. "
                  f"Modal Untitled 300 với <code>ease-out</code> đạt 90% sau {ms90(300, EOUT)} ms, tức chậm hơn mình. DEC-139 ghi “đổi lúc này không làm nhìn mới hơn mà chỉ thêm việc”, số đo vẫn đồng ý với câu đó. Hai phương án còn lại đều là mở lại DEC-139, bằng chứng mới duy nhất là bảng đếm trên, không đủ để đổi nên không khuyến nghị."),
             untitled=f"Không có token. <code>duration-100</code> {U_DUR['100']} chỗ, <code>duration-150</code> {U_DUR['150']}, <code>duration-300</code> {U_DUR['300']}, <code>duration-200</code> {U_DUR['200']}.",
             ours="<code>duration/fast</code> 125, <code>duration/medium</code> 300, <code>duration/slow</code> 700 trong <code>design-system/tokens.json</code>.",
             astryx="Cùng 3 dải, thêm min, max cho mỗi dải (95 · 125 · 165, 225 · 300 · 400, 525 · 700 · 935), <code>design/design.md</code> mục Motion.",
             pv=panes(pv_scale),
             opts=[("keep", "Giữ 125 · 300 · 700, không thêm bậc", True),
                   ("tw", "Mở lại DEC-139: đổi thành 100 · 200 · 300, sửa mọi chỗ đang dùng", False),
                   ("add", "Mở lại DEC-139: thêm bậc 200 cho menu và lúc đóng", False)]),
        dict(id="mt01", grp="Thang thời gian", title="duration/slow 700 có quá chậm cho web điều vận",
             why=(f"Quá chậm nếu dùng cho mở, đóng: dialog 700 đạt 90% sau {M90[TOK_SLOW]} ms, đuôi kéo tới 700, người điều vận bấm hàng trăm lần mỗi ngày sẽ thấy lề mề. Foundation chỉ giao nó cho <b>chuyển động liên tục</b>, và hiện có <mark>{VAR_DUR['duration-slow']} chỗ dùng</mark>; skeleton đang ghi số trần 1,2 giây. "
                  "Coi 700 là <mark>một chiều của vòng lặp</mark> thì cả vòng 1400, gần với 1,2 giây đang có, và dưới <code>animate-pulse</code> 2 giây của Tailwind. Không chậm việc vì vòng lặp không chặn gì."),
             untitled="Không có bậc 700; <code>duration-500</code> chỉ ở lúc đóng slideout, 2 chỗ. Tailwind <code>animate-pulse</code> 2 giây, code Untitled không dùng.",
             ours=f"<code>duration/slow</code> 700, foundation ghi “skeleton pulse, chấm trạng thái nhấp nháy”; thực dùng <code>pl 1.2s</code> ở trang badge-avatar.",
             astryx="Slow 700 cho skeleton pulse, StatusDot pulsing, không dùng cho vào, ra.",
             pv=panes(pv_slow),
             opts=[("loop", "Giữ 700, chỉ dùng cho một chiều của vòng lặp, cấm cho vào, ra", True),
                   ("500", "Mở lại DEC-139: hạ xuống 500, vòng lặp nhanh hơn, dễ gây chú ý hơn", False),
                   ("drop", "Mở lại DEC-139: bỏ duration/slow, vòng lặp ghi số trong từng component", False)]),
        dict(id="mt02", grp="Đường cong", title="Một đường cong hay nhiều: vào, ra, đứng yên, vòng lặp",
             why=(f"Mở lại DEC-139 phần “một đường cong cho mọi chuyển động”, chỉ cho vòng lặp. Bằng chứng mới: <mark>{VAR_EASE} chỗ thật dùng <code>easing/standard</code></mark>; spinner, skeleton, con trỏ giả đang dùng <code>linear</code>, <code>ease-in-out</code>, <code>steps</code>. Đường cong chuẩn đặt vào vòng lặp thì lao rồi đứng, bấm thử bên dưới để thấy. "
                  f"Vào, ra thì một đường đủ: đạt 50% sau {STD_50}% thời gian, 90% sau {STD_90}%, nên phần tử đóng biến mất nhanh hơn <code>ease-in</code> của Untitled (90% sau {round(t_at(EIN, .9) * 100)}%). <code>linear</code> là từ khoá CSS, Flutter có <code>Curves.linear</code>, nên không cần token."),
             untitled=f"Hai đường cho vào, ra: <code>ease-out</code> {U_EASE['out']}, <code>ease-in</code> {U_EASE['in']}. Đổi màu <code>ease-linear</code> {U_EASE['linear']}, <code>ease-in-out</code> {U_EASE['in-out']}.",
             ours="<code>easing/standard</code> cubic-bezier(0.24, 1, 0.4, 1), foundation: “một đường cong cho mọi chuyển động”.",
             astryx="Một đường <code>ease-standard</code> giống hệt, không bounce, không spring; không nói vòng lặp.",
             pv=panes(pv_ease), pv_raw_ok="Số Untitled để so",
             opts=[("one", "Một đường cong cho vào, ra, đổi trạng thái; vòng lặp và thanh giờ dùng linear, không thêm token", True),
                   ("strict", "Giữ đúng một đường cong kể cả vòng lặp, không sửa DEC-139", False),
                   ("two", "Thêm easing/exit cho lúc ra, thành hai đường như Untitled, mọi component khai thêm", False)]),
        dict(id="mt03", grp="Đường cong", title="Số trần không qua token: sửa ngay hay sửa dần",
             why=(f"{USE_RAW}/{USE_TOTAL} chỗ ghi số trần ở {P_MOVE} trang màn mẫu. Nặng nhất là <code>transform .15s</code> {n_raw('transition', 'transform .15s')} chỗ ở trang sidebar-navigation-r2, không khai đường cong nên trình duyệt lấy mặc định <code>ease</code>. "
                  f"Hậu quả đo được: <mark>{USE_RAW} chỗ này vẫn chạy khi người dùng bật giảm chuyển động</mark>, vì luật đó chỉ đưa biến về 0. {SPEC_TOK}/{SPEC_N} spec nhắc token, nên dev đọc spec không biết phải dùng gì."),
             untitled=f"Không có token để lọt: dùng thẳng lớp Tailwind như <code>duration-100</code>; không có lớp kiểm.",
             ours=f"<code>design-system/components/_work/sidebar-navigation-r2/page.json</code>, trang badge-avatar, buttons, form-controls; mục 10 của <code>design-system/foundations/motion.md</code> cấm <code>all</code>.",
             astryx="Ghi “dùng tên token khi ghi chú prototype, spec”, không có máy kiểm.",
             pv=panes(pv_raw),
             opts=[("now", f"Đổi cả {USE_RAW} chỗ sang biến trong lượt chốt, thêm dò số trần vào kiểm token", True),
                   ("later", "Sửa dần khi chạm tới từng component, chưa thêm dò", False)]),
        dict(id="mt04", grp="Component", title="Hover, nhấn, focus: cái nào chạy, cái nào hiện ngay",
             why=("Hover đổi màu qua <code>duration/fast</code> đã có ở Button, Checkbox, Toggle. Chưa có luật là <b>focus</b>: người dùng bàn phím di chuyển nhanh, vòng focus chạy dần thì <mark>không biết đang đứng ở đâu</mark> trong khoảng trễ. WCAG không cấm, đây là chọn theo tác vụ: người điều vận nhập bằng Tab rất nhiều. Vòng focus web dùng outline theo DEC-327. "
                  "Nhấn: không có màu riêng thì không có gì để chạy."),
             untitled="<code>transition duration-100 ease-linear</code> trên nút, ô nhập; <code>outline-focus-ring</code> nằm chung phần tử, chưa kiểm vòng có chạy theo hay không.",
             ours=f"<code>background var(--duration-fast)</code> {n_raw('transition', 'background var(--duration-fast)')} chỗ ở buttons, form-controls; không khai đường cong.",
             astryx="Fast cho hover, pressed, đổi màu, Switch; không nói focus.",
             pv=panes(pv_hover),
             opts=[("rec", "Hover, nhấn chạy duration/fast; vòng focus hiện ngay, không chạy", True),
                   ("same", "Vòng focus chạy cùng duration/fast cho đồng bộ", False),
                   ("none", "Bỏ cả chuyển động hover trên web, đổi màu ngay, nhanh nhất", False)]),
        dict(id="mt05", grp="Component", title="Menu, chọn, popover, tooltip: 125 hay 300",
             why=(f"Foundation xếp Popover vào 300. Menu là thứ người điều vận mở nhiều nhất, 300 đạt 90% sau {M90[TOK_MED]} ms còn đuôi chạy tới 300; 125 đạt 90% sau {M90[TOK_FAST]} ms. Untitled mở 150, đóng 100, <mark>nhanh gấp đôi modal của chính họ</mark>. Đổi vai, không đổi số, nên không đụng DEC-139. "
                  "Trượt 4 thay vì 2 của Untitled, vì 2 quá nhỏ để thấy với đường cong dốc. Tooltip chờ 300 như mặc định của Untitled để rê ngang qua hàng icon không bật liên tục; con số đọc được trên <code>design/_ref/untitled-ui/react/components/base/tooltip/tooltip.tsx</code>."),
             untitled="<code>duration-150 ease-out animate-in fade-in slide-in-from-*-0.5</code>, đóng <code>duration-100 ease-in</code>. Tooltip <code>delay = 300</code>, không ghi thời gian chạy, lấy mặc định của tailwindcss-animate (chưa kiểm số).",
             ours="<code>duration/medium</code> cho Popover trong <code>design-system/foundations/motion.md</code>; <code>design-system/components/base/tooltip.md</code> chưa ghi thời gian chờ.",
             astryx="Medium 300 cho Popover, không tách menu.",
             pv=panes(pv_menu), pv_raw_ok="Số Untitled để so",
             opts=[("fast", "Menu, chọn, popover, tooltip chạy duration/fast + trượt 4; tooltip chờ 300 mới hiện", True),
                   ("med", "Giữ duration/medium như foundation đang ghi", False),
                   ("zero", "Menu hiện ngay không chạy, tooltip vẫn chờ 300", False)]),
        dict(id="mt06", grp="Component", title="Dialog, sheet, ngăn kéo: lúc đóng có nhanh hơn lúc mở không",
             why=(f"Untitled mở 300, đóng 200, còn slideout đóng 500 chậm hơn mở, nên không phải luật đáng chép. Với đường cong của mình, đóng 300 đã mất 90% sau {M90[TOK_MED]} ms, <mark>nhanh hơn đóng 200 của Untitled ({ms90(200, EIN)} ms)</mark>. Đóng 125 đạt 90% sau {M90[TOK_FAST]} ms: sheet trên app gần như biến mất đột ngột, mất cảm giác đi xuống đâu. "
                  "Thứ làm chậm việc là lớp phủ còn chặn bấm trong lúc đóng, nên luật cần là <mark>thôi chặn bấm ngay khi người dùng đóng</mark>. Hình: dialog phóng 95 → 100 + mờ dần, sheet và ngăn kéo trượt hết chiều, không mờ."),
             untitled="<code>modal.tsx</code>: <code>duration-300 ease-out animate-in zoom-in-95</code>, đóng <code>duration-200 ease-in</code>. <code>slideout-menu.tsx</code>: mở <code>duration-300</code>, đóng <code>duration-500</code>.",
             ours="<code>duration/medium</code> cho Dialog, BottomSheet trong <code>design-system/foundations/motion.md</code>; chưa có spec Dialog, chưa có luật hình.",
             astryx="Medium cho Dialog, BottomSheet, một đường cong.",
             pv=panes(pv_dialog, platforms=("web", "mobile")), pv_raw_ok="Số Untitled để so",
             opts=[("same", "Vào, ra đều duration/medium, thôi chặn bấm ngay khi đóng; dialog phóng 95, sheet trượt", True),
                   ("fastout", "Vào duration/medium, ra duration/fast", False),
                   ("untitled", "Theo Untitled: vào 300, ra 200, cần thêm bậc 200 và đường cong thứ hai", False)]),
        dict(id="mt07", grp="Component", title="Toast: trượt hay chỉ mờ",
             why=("Vị trí, thời gian đọc đã chốt ở DEC-286, DEC-287: web dưới phải, app dưới ngay trên thanh tab; không nút 3 giây, có nút tối thiểu 10 giây. Còn thiếu hình chuyển động. Trượt 8 giúp mắt bắt được vì toast hiện ở góc xa chỗ đang nhìn; lái xe nhìn nhanh ngoài trời càng cần. "
                  "Ra nhanh hơn vào, vì toast tự ẩn không phải do người dùng bấm, nó <mark>không nên kéo mắt thêm lần nữa</mark>. Thanh giờ chạy <code>linear</code> theo đúng số giây (mục mt02)."),
             untitled="Khai <code>sonner</code> trong package.json, 0 component toast trong ref; không có số để so. Chưa kiểm số mặc định của thư viện.",
             ours="Vị trí, thanh giờ trong <code>design-system/components/base/alert-notification.md</code>; chưa có số chuyển động.",
             astryx="Medium cho Toast, góc trên phải theo bản cũ; DEC-286 đã đổi vị trí.",
             pv=panes(pv_toast, platforms=("web", "mobile")),
             note="Phụ thuộc mt02: nếu chọn đúng một đường cong kể cả vòng lặp, thanh giờ vẫn phải chạy đều, cần ghi ngoại lệ riêng.",
             opts=[("slide", "Vào duration/medium trượt 8 + mờ dần, ra duration/fast chỉ mờ", True),
                   ("fade", "Chỉ mờ dần, không trượt, ít gây chú ý hơn", False)]),
        dict(id="mt08", grp="Component", title="Skeleton: nhấp nháy, vệt sáng hay đứng yên",
             why=(f"Untitled <mark>không có skeleton</mark> ({U_SKEL} file), nên đây là quyết định của mình; <code>design/design.md</code> dùng Skeleton khi chuyển trang. Bảng dày chứa hàng chục ô, vệt sáng chạy qua làm nhiễu và tốn hơn vì đổi nền liên tục; nhấp nháy opacity nhẹ hơn. "
                  "WCAG 2.2.2 áp cho thứ chạy quá 5 giây song song nội dung khác; ghi chú 4 chỉ miễn khi không thao tác được trong lúc tải. Skeleton một khối trên màn còn thao tác được thì <mark>phải dừng trước 5 giây</mark>, sau đó đứng yên và có chữ."),
             untitled_none="Untitled không có skeleton trong ref", untitled="Không có component Skeleton trong ref. Tailwind có <code>animate-pulse</code> 2 giây, code Untitled không dùng.",
             ours=f"<code>pl 1.2s ease-in-out</code> {n_raw('animation', 'pl 1.2s ease-in-out infinite')} chỗ ở trang badge-avatar; chưa có spec Skeleton.",
             astryx="Skeleton pulse dùng slow 700.",
             pv=panes(pv_skel),
             opts=[("pulse", "Nhấp nháy opacity 100 ↔ 45, duration/slow một chiều, linear; dừng sau 5 giây, tải lâu hơn thì thêm chữ", True),
                   ("shim", "Vệt sáng chạy ngang, dừng sau 5 giây", False),
                   ("static", "Khung đứng yên, không chạy, an toàn nhất, ít tín hiệu đang tải nhất", False)]),
        dict(id="mt09", grp="Component", title="Spinner: chu kỳ và thời gian chờ trước khi hiện",
             why=(f"Đang có hai số: 1 giây {n_raw('animation', 'fsp 1s linear infinite')} chỗ, 0,8 giây {n_raw('animation', 'spn .8s linear infinite')} chỗ (Button). Untitled <code>animate-spin</code> 1 giây. Chốt <mark>một số 1000</mark>. Số này là của Spinner, không thêm bậc Foundation (tinh thần DEC-314: số lẻ thì ghi ngoại lệ). "
                  "Chờ 300 trước khi hiện để thao tác xong nhanh không bị nháy; <code>design/design.md</code> ghi chờ <code>duration-medium-min</code> 225, nhưng dải min không còn ở bộ mới, nên trỏ <code>duration/medium</code>. Trạng thái Disabled của DEC-277 vẫn hiện ngay từ lúc bấm, chỉ riêng spinner chờ."),
             untitled="<code>animate-spin</code> ở Button, ô tải file, Loading indicator; không có thời gian chờ.",
             ours=f"Trang buttons <code>spn .8s</code>, badge-avatar <code>fsp 1s</code>; <code>design-system/components/base/avatar.md</code> nhắc spinner, không ghi số.",
             astryx="Spinner của Button chờ <code>duration-medium-min</code> 225 rồi mới hiện.",
             tokens=[("spinner/period", "1000 ms", "Token Component, vào sổ đợt 2; không phải bậc Foundation")],
             pv=panes(pv_spin),
             opts=[("rec", "Chu kỳ 1000, chờ duration/medium mới hiện, thêm spinner/period vào sổ Component", True),
                   ("nowait", "Chu kỳ 1000, hiện ngay khi bấm", False),
                   ("225", "Chờ 225 như Astryx, thêm lại dải min vào thang", False)]),
        dict(id="mt10", grp="Component", title="Splash: nhịp phóng 115% làm logo tràn màn app",
             why=(f"Kịch bản 4 nhịp ở <code>design/design.md</code> (DEC-037) kết bằng <mark>phóng 115%</mark>. DEC-326 đặt logo app rộng tối đa bằng màn trừ lề: Delta rộng {LOGO_W}, cao khoảng {LOGO_H} trên khung 393. Phóng 115% thành {round(PEAK)}, <mark>vượt mép màn {vn(round(OVER, 1))} px mỗi bên</mark>, cắt chữ. Hai quyết định riêng nên chưa ai thấy; DEC-326 không nói phóng. "
                  f"Tổng {vn(SPLASH_MS / 1000)} giây, dưới 5 giây và là pha tải nên hợp WCAG 2.2.2 (ghi chú 4). Bốn số là số riêng của Splash, không qua thang. Điều kiện “chỉ hiện khi tải lâu hơn <code>duration-medium-max</code> 400” trỏ vào dải đã bỏ, cần ghi lại thành 400 trong spec. Bản Flutter chưa có spec."),
             untitled_none="Untitled không có splash", untitled="Không có splash trong ref. Số gần nhất để so: <code>duration-300</code> lúc mở modal.",
             ours="<code>design/design.md</code> mục Splash web; <code>design-system/foundations/logo.md</code> mục 14: cao 64, Delta cao khoảng 61.",
             astryx="Chính là nguồn kịch bản này, chỉ cho web; app chưa có.",
             pv=panes(pv_splash), note=f"Phụ thuộc <code>design-system/foundations/logo.md</code>: nếu sau này splash app đổi cỡ logo khác 361 thì mức chặn đổi theo công thức rộng màn ÷ rộng logo. Máy thử 320: logo 288, chặn ở {vn(round(320 / 288 * 100, 1))}%.",
             opts=[("cap", f"Phóng tối đa bằng bề rộng màn: min(115%, rộng màn ÷ rộng logo), Delta {vn(round(CAP * 100, 1))}%; web giữ 115%", True),
                   ("clip", "Giữ 115% ở mọi nơi, chấp nhận mép logo bị cắt ở nhịp cuối", False),
                   ("nozoom", "App bỏ nhịp phóng, chỉ mờ dần sang màn đầu; web giữ 115%", False),
                   ("shrink", f"Mở lại DEC-326: logo app nhỏ lại còn rộng {round(APP_W / 1.15)} để đủ chỗ phóng 115%", False)]),
        dict(id="mt11", grp="Component", title="Tab: gạch chân có trượt không",
             why=("Untitled chỉ đổi màu chữ <code>duration-100</code>, <b>gạch chân không trượt</b>. Tab trong web điều vận đổi nhóm dữ liệu rất thường xuyên, trượt không mang thêm nghĩa, nội dung mờ dần thì <mark>làm chậm mắt đọc số liệu</mark> mỗi lần đổi. Chưa có spec Tab trong <code>design-system/components</code>; DEC-328 đã bỏ token bo góc riêng của tab nên luật hình đi theo khi có spec."),
             untitled="<code>tabs.tsx</code>: <code>transition duration-100 ease-linear</code> trên từng tab, không có phần tử gạch chân chạy.",
             ours="Chưa có spec Tab; không có khai báo chuyển động trong <code>page.json</code>.",
             astryx="Không nói riêng.",
             pv=panes(pv_tab),
             opts=[("color", "Chữ đổi màu duration/fast, gạch chân nhảy ngay, nội dung đổi ngay", True),
                   ("slide", "Gạch chân trượt duration/fast, nội dung đổi ngay", False),
                   ("full", "Gạch chân trượt duration/medium, nội dung mờ dần", False)]),
        dict(id="mt12", grp="Component", title="Menu thu gọn 240 ↔ 64: có chạy bề rộng không",
             why=(f"Untitled chạy 300 và dùng lò xo ở sidebar kép, DEC-139 cấm lò xo. Chạy bề rộng thì <mark>bảng bên cạnh xếp lại ở mỗi khung hình</mark>, màn dày dữ liệu càng tốn; thao tác này cũng hiếm, không cần dẫn mắt. Chevron của nhóm menu vẫn xoay bằng <code>duration/fast</code>, thay cho <code>transform .15s</code> {n_raw('transition', 'transform .15s')} chỗ đang ghi."),
             untitled="<code>sidebar-slim.tsx</code>: <code>transition duration-300</code>; panel phụ <code>type: \"spring\", damping: 26, stiffness: 220</code>.",
             ours="Rộng 240, thu gọn 64 trong <code>design-system/components/application/sidebar-navigation.md</code>; không ghi chuyển động.",
             astryx="Không nói riêng.",
             pv=panes(pv_side), pv_raw_ok="Số Untitled để so",
             opts=[("instant", "Bề rộng đổi ngay, chevron xoay duration/fast", True),
                   ("fast", "Bề rộng chạy duration/fast, bảng xếp lại trong lúc chạy", False),
                   ("u", "Theo Untitled, chạy 300", False)]),
        dict(id="mt13", grp="Giảm chuyển động", title="prefers-reduced-motion: luật đầy đủ khi người dùng bật",
             why=(f"DEC-139 chốt “tắt”, <code>design-system/tokens.css</code> đưa ba biến về 0. Thiếu ba thứ. Một: {USE_RAW} chỗ số trần lọt ra, {P_RM} trang tự xử lý. Hai: <mark>vòng lặp về 0 thì spinner đứng yên, không còn tín hiệu đang tải</mark>, cần thêm chữ. Ba: code chờ <code>transitionend</code> sẽ treo vì thời gian 0 không phát sự kiện (đặc tả CSS Transitions, ghi từ trí nhớ, chưa kiểm). "
                  "WCAG 2.3.3 không tính mờ dần, đổi màu là chuyển động, nên phương án giữ mờ dần vẫn đạt; đó là mở lại DEC-139 vì đổi “tắt” thành “giảm”, không có bằng chứng người dùng cần nên không khuyến nghị."),
             untitled=f"<code>motion-reduce:animate-none</code> chỉ ở {U_REDUCE_FILES[0] if U_REDUCE_FILES else '—'}, {U_REDUCE} chỗ; modal, spinner không xử lý.",
             ours="<code>@media (prefers-reduced-motion: reduce)</code> ở <code>design-system/tokens.css</code>; <code>design-system/components/application/field-upload.md</code> ghi icon dừng xoay.",
             astryx="Thời lượng về 0 cho mọi component; Splash: logo tĩnh, tải xong chuyển thẳng.",
             pv=panes(pv_reduced),
             note="Phụ thuộc mt03: nếu chọn sửa dần, luật này chỉ có hiệu lực ở phần đã đổi sang biến. Bạn có thể kiểm thật: bật giảm chuyển động trong hệ điều hành rồi tải lại trang, biến ở khung trái thành 0ms.",
             opts=[("rule", "Giữ về 0; spinner dừng + chữ “Đang tải…”; skeleton đứng yên; code không chờ transitionend", True),
                   ("fade", "Mở lại DEC-139: giữ mờ dần ngắn duration/fast, chỉ bỏ trượt, phóng, vòng lặp", False),
                   ("setting", "Như khuyến nghị, thêm công tắc riêng trong Cài đặt của sản phẩm", False)]),
        dict(id="mt14", grp="Nền tảng", title="App Flutter so với web: một bộ số hay hai",
             why=("<code>_scripts/ds-v2-handoff.py</code> đã sinh <code>InvMotion</code> cho Flutter từ cùng bốn token, nên <mark>một bộ số không tốn thêm việc</mark>, đúng hướng gộp ở DEC-316. Khác nhau ở chỗ tay người: sheet kéo được thì <mark>đi theo ngón tay</mark>, không chạy theo thời gian; chuyển màn giữ mặc định của nền tảng để giống ứng dụng khác trên máy. "
                  "Bẫy đã đọc: <code>MediaQueryData.disableAnimations</code> chỉ phản ánh tuỳ chọn Android, <b>iOS không bật cờ này</b>, phải đọc thêm <code>AccessibilityFeatures.reduceMotion</code> (api.flutter.dev, đọc 02/11). Theo <code>docs/_shared/operating-environment.md</code> app phải chạy mượt trên máy cấu hình trung bình; chưa có số đo chuyển động trên máy thật."),
             untitled_none="Untitled chỉ có web", untitled="Chỉ có web React, không có app; dùng <code>items-end</code> để modal thành sheet trên màn nhỏ nhưng vẫn phóng, không trượt.",
             ours="<code>InvMotion</code> sinh từ <code>design-system/tokens.json</code>; Flutter theo <code>docs/_shared/operating-environment.md</code>.",
             astryx="Một bộ số, chưa nói app riêng.",
             pv=panes(pv_app, platforms=("web", "mobile")),
             note="Phụ thuộc mt13: luật giảm chuyển động trên app phải đọc cả hai cờ trên.",
             opts=[("one", "Một bộ số; sheet theo ngón tay; chuyển màn mặc định nền tảng; đọc cả hai cờ giảm chuyển động", True),
                   ("two", "Tách số riêng cho app, cần thêm chế độ Mobile cho chuyển động", False),
                   ("native", "App bỏ token, dùng hết mặc định Material, Cupertino, hai hệ điều hành chạy khác nhau", False)]),
        dict(id="mt15", grp="Nền tảng", title="Ngưỡng WCAG: 2.2.2, 2.3.1, 2.3.3 đặt mức nào",
             why=("Nguyên văn đọc tại w3.org ngày 02/11. <b>2.3.1 (A)</b>: không gì “flashes more than three times in any one second period”. <b>2.2.2 (A)</b>: thứ chạy tự động, “lasts more than five seconds”, song song nội dung khác thì phải dừng được, trừ pha tải không thao tác được. <b>2.3.3 (AAA)</b>: “Motion animation triggered by interaction can be disabled”. "
                  f"Đo bộ đề xuất: nhanh nhất là con trỏ 1 lần mỗi giây, chấm {vn(round(1000 / (TOK_SLOW * 2), 2))} lần, splash một vệt duy nhất, <mark>đều dưới mốc 3</mark>. Rủi ro thật là 2.2.2: skeleton, chấm chạy mãi. 2.3.3 là AAA nhưng mình đã có sẵn cơ chế, làm không tốn thêm."),
             untitled=f"Không nêu. Chỉ {U_REDUCE} chỗ <code>motion-reduce:animate-none</code>, nên chưa đạt 2.3.3 ở modal.",
             ours="<code>design-system/components/application/field-upload.md</code> ghi 2.3.3; foundation chưa nêu ngưỡng.",
             astryx="Có <code>prefers-reduced-motion</code>, không nêu 2.2.2, 2.3.1.",
             pv=panes(pv_wcag),
             opts=[("all", "Bắt buộc 2.2.2, 2.3.1, làm luôn 2.3.3 qua giảm chuyển động; ghi vào foundation", True),
                   ("a", "Chỉ cam kết mức A (2.2.2, 2.3.1), 2.3.3 là tuỳ từng màn", False)]),
        dict(id="mt16", grp="Nguyên tắc", title="Chấm trạng thái nhấp nháy trên danh sách dày",
             why=("Foundation ghi <code>duration/slow</code> cho “chấm trạng thái nhấp nháy”, nhưng <mark>0 spec dùng</mark>. Danh sách xe có hàng chục dòng “Đang chạy”, nhấp nháy đồng loạt thì <b>không còn dòng nào nổi bật</b>, lại vướng 2.2.2 vì chạy mãi song song với nội dung. Trạng thái đã có màu và nhãn chữ. Đây là luật chặn trước khi có người dùng tới."),
             untitled="Không có chấm nhấp nháy; <code>Dot</code> của Badge đứng yên (theo <code>design/_ref/untitled-ui/react/components/base/badges/badges.tsx</code>).",
             ours="Một câu trong <code>design-system/foundations/motion.md</code>; <code>design-system/components/application/map-marker.md</code> không nhấp nháy.",
             astryx="StatusDot pulsing dùng slow.",
             pv=panes(pv_dot),
             opts=[("static", "Bỏ nhấp nháy ở danh sách, bảng, bản đồ; chấm đứng yên + nhãn; xoá khỏi foundation", True),
                   ("one", "Chỉ một chấm mỗi màn, cho trạng thái cần xử lý gấp, dừng sau 5 giây", False),
                   ("keep", "Giữ như foundation đang ghi", False)]),
        dict(id="mt17", grp="Nguyên tắc", title="Không làm chậm tác vụ dày dữ liệu",
             why=("Nguyên tắc này chưa có chữ nào trong foundation. Lọc, sắp xếp, phân trang là việc lặp lại liên tục ở web điều vận. Mờ dần mỗi lần lọc thêm 125 ms, lần lượt từng dòng thêm 305 ms với 4 dòng, <mark>bảng 50 dòng thì hơn 3 giây</mark> nếu không chặn. Đồng thời <b>không chuyển động nào được khoá thao tác</b>: bấm tiếp trong lúc chạy thì chạy luôn lệnh mới."),
             untitled="Không có chuyển động khi đổi dữ liệu; dòng trong <code>table.tsx</code> chỉ có <code>transition-colors</code> lúc hover.",
             ours="Chưa có luật; foundation chỉ ghi “không dùng <code>all</code>”.",
             astryx="Chỉ nói chuyển trang dùng Skeleton, không dùng splash.",
             pv=panes(pv_dense),
             opts=[("rule", "Bảng, lọc, sắp xếp, phân trang, thêm dòng không chạy; mọi chuyển động không khoá thao tác", True),
                   ("fade", "Cho mờ dần duration/fast khi đổi dữ liệu, cùng luật không khoá", False),
                   ("stag", "Cho dòng hiện lần lượt, có chặn tổng 300", False)]),
        dict(id="mt18", grp="Nguyên tắc", title="Lớp phủ làm mờ khi mở: chạy cái gì, đo trên máy nào",
             why=("DEC-327 đã chốt 35% + <code>backdrop-blur/lg</code>, máy yếu lùi <code>color/bg/overlay_solid</code>; <code>design-system/foundations/effect-styles.md</code> ghi “phải đo trên máy thật”, <mark>chưa có số đo</mark>. Làm mờ phải tính lại vùng nền mỗi khung hình, chạy cả bán kính thì tốn nhất. Mục này không mở lại DEC-327, chỉ chốt <b>phần nào được chạy</b> và điều kiện đo. "
                  "Nút Phát bên dưới đo khung hình trên chính máy đang xem, không thay được Android của lái xe. Ngưỡng 50 khung mỗi giây là đề xuất của mình, không lấy từ nguồn nào."),
             untitled="<code>modal.tsx</code>: <code>bg-overlay/70 backdrop-blur-[6px]</code>, chạy <code>fade-in</code> của cả lớp; không có đường lùi.",
             ours="<code>backdrop-blur/lg</code> 24 + <code>color/bg/overlay</code> 35%, đường lùi 50% ở <code>design-system/foundations/effect-styles.md</code>.",
             astryx="Lớp phủ đặc, không làm mờ.",
             pv=panes(pv_blur),
             note="Phụ thuộc mt14: máy đo là Android cấu hình trung bình; nếu rớt ngưỡng thì app dùng <code>color/bg/overlay_solid</code>, 35% trong DEC-327 chỉ áp cho web và máy đủ khoẻ.",
             opts=[("opacity", "Chỉ mờ dần lớp phủ, bán kính giữ nguyên; đo Android trước khi vào app, dưới 50 khung mỗi giây thì lùi lớp đặc", True),
                   ("run", "Chạy cả bán kính blur 0 → 24, đẹp hơn, tốn nhất", False),
                   ("after", "Lúc chạy dùng lớp đặc, chạy xong mới bật làm mờ, thấy nháy một nhịp", False)]),
    ],
    final=FINAL,
    css=CSS,
    js=JS,
)
