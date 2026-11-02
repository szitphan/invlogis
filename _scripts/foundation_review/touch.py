#!/usr/bin/env python3
"""SPEC trang review Foundations · Vùng chạm và focus. Số đọc từ tokens.css, _work/*, react/ của Untitled lúc dựng; không gõ tay trừ chỗ ghi nguồn.
Dựng: python3 _scripts/foundation_review/build.py touch"""
import collections
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402
from kit import ROOT, cr, icon, panes, rows  # noqa: E402

OK, DIFF, GAP, OWN = "st-ok", "st-diff", "st-gap", "st-own"
LAB = {OK: "Giống", DIFF: "Khác có lý do", GAP: "Mình thiếu", OWN: "Chỉ mình có"}


def st(s, note=""):
    return f'<span class="{s}">{LAB[s]}</span>' + (f'<br><span class="small muted">{note}</span>' if note else "")


def n(x):
    return f"{x:g}".replace(".", ",")


# ---------- đọc token theo nền tảng ----------
def _blocks(*want):
    out = {}
    for sel, body in re.findall(r"^([^\n{}@]+)\{(.*?)^\}", kit.TCSS, flags=re.S | re.M):
        if sel.strip() in want:
            out.update(re.findall(r"(--[\w-]+):\s*([^;]+);", body))
    return out


_ROOT = _blocks(":root")
_PLAT = {"web": {**_ROOT, **_blocks(':root, [data-platform="web"]')}, "mobile": {**_ROOT, **_blocks('[data-platform="mobile"]')}}
_LIGHT = {**_ROOT, **_blocks(':root, [data-theme="light"]')}
_THEME = {"l": _LIGHT, "d": {**_LIGHT, **_blocks('[data-theme="dark"]')}}


def px(token, plat="web"):
    """Giá trị px của token dạng 'control/height/md'."""
    name = "--" + token.replace("/", "-")
    raw = _PLAT[plat].get(name)
    while raw and raw.startswith("var("):
        raw = _PLAT[plat].get(re.match(r"var\((--[\w-]+)", raw).group(1))
    if raw is None:
        raise SystemExit(f"Không có token {token} ({plat})")
    if raw.endswith("rem"):
        return float(raw[:-3]) * 16
    return float(raw.replace("px", ""))


def _hex(token, theme):
    src = _THEME[theme]
    raw = src.get("--" + token.replace("/", "-"))
    while raw and raw.startswith("var("):
        raw = src.get(re.match(r"var\((--[\w-]+)", raw).group(1))
    return raw


def _lum(c):
    f = lambda x: (x / 255) / 12.92 if x / 255 <= 0.03928 else ((x / 255 + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(fg, bg, theme="l"):
    """Tỉ lệ tương phản hai token màu; nền có độ trong suốt trộn trên color/bg/primary."""
    def parse(h):
        h = h.lstrip("#")
        h = h if len(h) == 8 else h + "FF"
        return [int(h[i:i + 2], 16) for i in (0, 2, 4)], int(h[6:8], 16) / 255
    base, _ = parse(_hex("color/bg/primary", theme))
    b, a = parse(_hex(bg, theme))
    b = [b[i] * a + base[i] * (1 - a) for i in range(3)]
    f, _ = parse(_hex(fg, theme))
    x, y = _lum(f), _lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def rr(fg, bg, theme="l"):
    return n(round(ratio(fg, bg, theme), 2)) + ":1"


# ---------- đếm thật ở component của mình ----------
PAGES = sorted(glob.glob(str(ROOT / "design-system/components/_work/*/page.json")))
page_raw = {Path(p).parent.name: open(p, encoding="utf-8").read() for p in PAGES}
page_css = {}
for slug, raw in page_raw.items():
    c = json.loads(raw).get("css", "")
    page_css[slug] = c if isinstance(c, str) else json.dumps(c)
NP = len(PAGES)
TOUCH_VAR = sum(1 for s in page_raw.values() if "var(--touch-min)" in s)
BUILDS = sorted(glob.glob(str(ROOT / "design-system/components/_work/*/build.py")))
hand = []
for p in BUILDS:
    for m in re.finditer(r"::after\{[^}]*inset:(-[\d]+px(?: -?[\d]+px?)?)", open(p, encoding="utf-8").read()):
        hand.append((Path(p).parent.name, m.group(1)))
HAND_N = len(hand)
HAND_TXT = ", ".join(f"{a} <code>{b}</code>" for a, b in hand)
GAP_PAGES = [k for k, s in page_raw.items() if "--color-focus-gap" in s]  # bộ token nhúng cũ trong trang
COLOR_PAGES = [k for k, s in page_raw.items() if "var(--focus-color)" in s]
ALIAS_PAGES = [k for k, s in page_raw.items() if "var(--focus)" in s]
SHADOW_INPUT = [k for k, s in page_css.items() if re.search(r"\.ctl\.is-focus[^{]*\{[^}]*box-shadow:inset", s)]
FV_PAGES = [k for k, s in page_css.items() if ":focus-visible" in s]
OVH = {k: len(re.findall(r"overflow:\s*hidden", s)) for k, s in page_css.items()}
OVH_TOTAL = sum(OVH.values())
TOKEN_GAP_GONE = "--color-focus-gap" not in kit.TCSS
SPEC_MD = sorted(glob.glob(str(ROOT / "design-system/components/base/*.md")) + glob.glob(str(ROOT / "design-system/components/application/*.md")))
spec_text = {Path(p).stem: open(p, encoding="utf-8").read() for p in SPEC_MD}
SPEC_TOUCH = sum(1 for s in spec_text.values() if re.search(r"touch/min|[Vv]ùng (chạm|bấm)", s))


# ---------- đếm thật ở Untitled (bỏ demo, story) ----------
UREACT = ROOT / "design/_ref/untitled-ui/react/components"
_ufiles = [p for p in UREACT.rglob("*.tsx") if not re.search(r"\.(demo|story)\.tsx$", p.name)]
_ulines = [ln for p in _ufiles for ln in p.read_text(encoding="utf-8").splitlines()]


def u(pat):
    return sum(1 for ln in _ulines if re.search(pat, ln))


U_RING = u(r"outline-focus-ring")
U_O2 = u(r"outline-2")
U_OFF = u(r"(?<!-)outline-offset-2")
U_NEG = u(r"-outline-offset-2")
U_FV = u(r"focus-visible")
U_IFV = u(r"isFocusVisible")
U_HIDDEN = u(r"outline-hidden")
U_TOUCH = u(r"touch-|min-h-11|min-w-11|tap-")
U_NEG_FILES = sorted({p.parent.name for p in _ufiles if "-outline-offset" in p.read_text(encoding="utf-8")})

# ---------- số vùng chạm ----------
T_W, T_A = px("touch/min", "web"), px("touch/min", "mobile")
F_W, F_O = px("focus/width"), px("focus/offset")
RING_OUT = F_W + F_O
H = {k: (px(f"control/height/{k}", "web"), px(f"control/height/{k}", "mobile")) for k in ("sm", "md", "ml", "lg")}
IC = {k: px(f"icon/size/{k}", "mobile") for k in ("xs", "sm", "md", "lg")}
IC_OLD = {"sm": 16, "md": 20, "lg": 24}  # tokens.json 0.22.0 (commit d0c167b), trước DEC-329


def bu(h, t):
    return max(0, (t - h) / 2)


def need_gap(h, t):
    return max(0, t - h)


NONSOLID = ["color/bg/primary", "color/bg/primary_alt", "color/bg/secondary", "color/bg/tertiary", "color/bg/selected", "color/bg/primary_hover", "color/bg/quaternary",
            "color/bg/error-primary", "color/bg/warning-primary", "color/bg/success-primary", "color/bg/info-primary"]
SOLID = ["color/bg/primary_solid", "color/bg/secondary_solid", "color/bg/error-solid", "color/bg/info-solid", "color/bg/success-solid", "color/bg/warning-solid"]
MIN_NS = min(ratio("color/focus/ring", b, m) for b in NONSOLID for m in "ld")
MIN_NS_TXT = n(round(MIN_NS, 2))
RING_ON_BTN = rr("color/focus/ring", "color/action/primary")
RING_ON_PRIMARY = rr("color/focus/ring", "color/bg/primary")
RING_ON_PRIMARY_D = rr("color/focus/ring", "color/bg/primary", "d")
SEL_VS_BG = rr("color/bg/selected", "color/bg/primary")
SEL_VS_BG_D = rr("color/bg/selected", "color/bg/primary", "d")


# ---------- atom xem thử ----------
def z(ctrl, label=""):
    """Vùng chạm viền chấm quanh control; chữ đo đọc từ trình duyệt."""
    lab = f'<span class="tc-n">{label}</span>' if label else ""
    return f'<span class="tc-c">{lab}<span class="tc-z">{ctrl}</span><span class="tc-v" data-m></span></span>'


def b(text, h="md", cls="", ic=None):
    inner = (icon(ic, "tp-ic-sm") if ic else "") + f'<span class="type-label">{text}</span>'
    return f'<span class="tp-btn {cls}" style="height:var(--control-height-{h})">{inner}</span>'


def ib(name="bell", h="md", cls="", ic="tp-ic-md"):
    return f'<span class="tc-ib {cls}" style="--h:var(--control-height-{h})">{icon(name, ic)}</span>'


def bare(name="circle-question-mark", ic="tp-ic-md"):
    return f'<span class="tc-bare tp-fg2">{icon(name, ic)}</span>'


def cap(x):
    return f'<div class="type-caption tp-sub tc-cap">{x}</div>'


# ---------- xem thử từng mục ----------
def pv_names(m, p):
    return (f'<div class="tc-row">{z(b("Xem lệnh", "md"))}</div>'
            + cap('Ô chấm đọc <code>touch/min</code>, vòng đọc <code>focus/width</code>, <code>focus/offset</code> theo chế độ của khung.')
            + f'<div class="tc-row" style="margin-top:var(--space-lg)"><span class="tp-btn sec tc-f"><span class="type-label">Có vòng focus</span></span></div>')


def pv_app_min(m, p):
    return (f'<div class="tc-row">{z(b("Bắt đầu chuyến", "lg"), "Nút chân màn")}{z(b("Xem lệnh", "md"), "Nút nhỏ")}{z(b("Lọc", "sm"), "Tab chip, nút SM")}{z(ib("bell", "md"), "Nút icon")}</div>')


def pv_48(m, p):
    return (f'<div class="tc-row"><span style="--touch-min:44px">{z(b("Nhận", "md"), "Sàn 44")}</span><span style="--touch-min:44px">{z(b("Lọc", "sm"), "Sàn 44")}</span>'
            f'<span style="--touch-min:48px">{z(b("Nhận", "md"), "Sàn 48")}</span><span style="--touch-min:48px">{z(b("Lọc", "sm"), "Sàn 48")}</span></div>')


def pv_web_min(m, p):
    return (f'<div class="tc-row">{z(b("Tạo lệnh", "md"), "Nút 32")}{z(b("Sửa", "sm"), "Nút 28")}{z(bare("x", "tp-ic-sm"), "Icon xoá 14")}{z(bare("circle-question-mark"), "Help 16")}{z(bare("x", "tc-ic12"), "Icon 12")}</div>'
            + cap('Icon đứng riêng có nền trong suốt, vùng chấm là phần bù vô hình.'))


def pv_coarse(m, p):
    return (f'<div class="tc-grid3"><div>{cap("Web, chuột: sàn 24")}<span style="--touch-min:24px">{z(b("Sửa", "md"))}</span></div>'
            f'<div>{cap("Web, cảm ứng: sàn 44, nút giữ 32")}<span style="--touch-min:44px">{z(b("Sửa", "md"))}</span></div>'
            f'<div data-platform="mobile">{cap("Đổi cả chế độ Mobile: nút 42")}<span style="--touch-min:44px">{z(b("Sửa", "md"))}</span></div></div>')


def pv_icons(m, p):
    return (f'<div class="tc-row">{z(bare("map-pin", "tp-ic-sm"), "icon sm")}{z(bare("circle-question-mark", "tp-ic-md"), "icon md")}{z(bare("bell", "tp-ic-lg"), "icon lg")}'
            f'{z(ib("bell", "md", "", "tp-ic-md"), "Nút icon, md")}{z(ib("bell", "md", "", "tp-ic-lg"), "Nút icon, lg")}</div>')


def pv_hit(m, p):
    box = '<span class="tc-ctx">Biên lai cân xe</span>'
    return (f'<div class="tc-grid3">'
            f'<div>{cap("Lớp giả: dòng giữ nguyên chiều cao")}<div class="tc-line">{box}<span class="tc-pse tp-fg2">{icon("circle-question-mark")}</span></div><div class="tc-line">{box}</div></div>'
            f'<div>{cap("Bọc khung: dòng cao thêm")}<div class="tc-line"><span class="tc-wrap">{box}<span class="tc-bx tp-fg2">{icon("circle-question-mark")}</span></span></div><div class="tc-line">{box}</div></div>'
            f'<div>{cap("Lớp giả trong khung cắt: phần bù mất")}<div class="tc-clip"><span class="tc-ctx">Biên lai</span><span class="tc-pse tc-pse-r tp-fg2">{icon("circle-question-mark")}</span></div></div></div>')


def pv_gap(m, p):
    pair = lambda gap, h: (f'<span class="tc-pair" style="gap:{gap}px">' + f'<span class="tc-z tc-zo">{ib("bell", h)}</span>' * 2 + "</span>")
    pair_b = lambda gap: (f'<span class="tc-pair" style="gap:{gap}px">' + f'<span class="tc-z tc-zo">{bare("bell")}</span>' * 2 + "</span>")
    t = T_A if p == "mobile" else T_W
    h = H["sm"][1] if p == "mobile" else H["sm"][0]
    second = f'<div>{cap(f"Nút SM, gap {n(need_gap(h, t))}")}{pair(need_gap(h, t), "sm")}</div>' if need_gap(h, t) else ""
    return (f'<div class="tc-row"><div>{cap("Nút SM, gap 0")}{pair(0, "sm")}</div>{second}'
            f'<div>{cap("Icon md riêng, gap 8")}{pair_b(8)}</div></div>')


def pv_ionly(m, p):
    if p == "mobile":
        return f'<div class="tc-row">{z(ib("pencil", "sm"), "SM")}{z(ib("pencil", "md"), "MD")}{z(ib("pencil", "lg", "", "tp-ic-lg"), "LG")}</div>'
    return f'<div class="tc-row">{z(ib("pencil", "sm"), "SM")}{z(ib("pencil", "md"), "MD")}{z(ib("pencil", "ml"), "ML")}{z(ib("pencil", "lg"), "LG")}</div>'


def pv_stale(m, p):
    return (f'<div class="tc-row"><div>{cap("Chuẩn: 2 cách 2")}<span class="tc-ava tc-f">NH</span></div>'
            f'<div>{cap("avatar.md: 2 cách 4")}<span class="tc-ava tc-f" style="outline-offset:calc(var(--focus-offset) * 2)">NH</span></div></div>')


def pv_app_focus(m, p):
    return (f'<div class="tc-row"><div>{cap("Chạm tay: không có vòng")}{b("Bắt đầu chuyến", "lg")}</div>'
            f'<div>{cap("Bàn phím ngoài: vòng 2 cách 2")}{b("Bắt đầu chuyến", "lg", "tc-f")}</div>'
            f'<div>{cap("Ô đang gõ: viền 2, chạm tay cũng có")}<div class="tp-inp tc-fin" style="min-height:var(--control-height-lg)"><span class="type-body">51C-482.15</span></div></div></div>')


def _tb(row_cls="", cell_cls="", clip=True):
    return (f'<div class="tc-tbw {"tc-clipc" if clip else ""}"><table class="tc-tb"><tr class="{row_cls}"><td><span class="type-code">LVT-2026-0412</span></td><td class="{cell_cls}"><span class="type-body">1.250.000 ₫</span></td><td class="tc-end">{ib("ellipsis", "sm")}</td></tr>'
            f'<tr><td><span class="type-code">LVT-2026-0411</span></td><td><span class="type-body">2.480.000 ₫</span></td><td class="tc-end">{ib("ellipsis", "sm")}</td></tr></table></div>')


def pv_table(m, p):
    return (f'{cap("Dòng nhận focus, vòng ngoài trong khung bo: hai đầu bị cắt")}{_tb("tc-f")}'
            f'{cap("Dòng nhận focus, vòng vào trong 2")}{_tb("tc-fin")}{cap("Ô nhận focus, vòng vào trong 2")}{_tb("", "tc-fin")}')


def pv_card(m, p):
    tile = lambda bg, lbl: (f'<div class="tc-t" style="background:var(--{bg.replace("/", "-")})"><span class="tp-btn sec tc-f"><span class="type-label">{lbl}</span></span>{cr("color/focus/ring", bg, 3)}</div>')
    return (f'<div class="tc-tiles">{tile("color/bg/primary", "Nền chính")}{tile("color/bg/secondary", "Nền phụ")}{tile("color/bg/selected", "Dòng chọn")}{tile("color/bg/warning-primary", "Cảnh báo")}{tile("color/bg/error-primary", "Lỗi")}{tile("color/bg/info-primary", "Thông tin")}</div>'
            f'<div class="tc-cards"><div class="tp-card tc-f"><span class="type-label">51C-482.15</span><span class="type-caption tp-sub">Thẻ bấm được, vòng ngoài</span></div><div class="tp-card"><span class="type-label">51D-120.77</span><span class="type-caption tp-sub">Thẻ kế bên, cách <code>layout/list-gap</code></span></div></div>')


def pv_solid(m, p):
    tt = lambda bg, cls, fg, lbl: (f'<div class="tc-solid" style="background:var(--{bg.replace("/", "-")});color:var(--{fg})"><span class="type-label">{lbl}</span><span class="tc-ibs {cls}">{icon("x")}</span></div>')
    return (f'{cap("Vòng than chì giữ nguyên")}<div class="tc-solids">{tt("color/bg/primary_solid", "tc-f", "color-text-inverse", "Nền đậm")}{tt("color/bg/error-solid", "tc-f", "color-text-white", "Nền lỗi")}</div>'
            f'{cap("Vòng theo màu chữ của nền (<code>currentColor</code>)")}<div class="tc-solids">{tt("color/bg/primary_solid", "tc-fc", "color-text-inverse", "Nền đậm")}{tt("color/bg/error-solid", "tc-fc", "color-text-white", "Nền lỗi")}</div>')


def pv_clip(m, p):
    return (f'<div class="tc-grid3"><div>{cap("Khung cắt, lề 0: vòng mất")}<div class="tc-ov" style="padding:0">{b("Lưu", "md", "tc-f")}</div></div>'
            f'<div>{cap("Khung cắt, lề 4: vòng vừa đủ")}<div class="tc-ov" style="padding:var(--space-xs)">{b("Lưu", "md", "tc-f")}</div></div>'
            f'<div>{cap("Khung cắt, lề 0, vòng vào trong")}<div class="tc-ov" style="padding:0">{b("Lưu", "md", "sec tc-fin")}</div></div></div>')


def pv_menu(m, p):
    mi = lambda cls, x, ic: f'<div class="tc-mi {cls}">{icon(ic, "tp-ic-md")}<span class="type-body">{x}</span></div>'
    mn = lambda cls: f'<div class="tc-menu">{mi("", "Sửa lệnh", "pencil")}{mi(cls, "Nhân bản", "copy")}{mi("", "Huỷ lệnh", "trash-2")}</div>'
    return f'<div class="tc-grid2"><div>{cap("Vòng ngoài: đè dòng trên, dưới")}{mn("tc-f")}</div><div>{cap("Vòng vào trong 2")}{mn("tc-fin")}</div></div>'


def pv_live(m, p):
    return (f'<div class="tc-row"><div>{cap("Bấm Tab vào đây, rồi bấm chuột: vòng chỉ hiện khi dùng bàn phím")}<div class="tc-row"><button class="tp-btn tc-live"><span class="type-label">Duyệt lệnh</span></button>'
            f'<button class="tp-btn sec tc-live"><span class="type-label">Để sau</span></button><input class="tc-input" aria-label="Mã container" value="TCLU 482915-3"></div></div>'
            f'<div>{cap("Dùng <code>:focus</code>: bấm chuột cũng hiện vòng")}<button class="tp-btn sec tc-livef"><span class="type-label">Xuất file</span></button></div></div>')


def pv_input(m, p):
    fld = lambda cls, x: f'<div class="tc-fldm">{cap(x)}<div class="tp-inp {cls}"><span class="type-body">51C-482.15</span></div></div>'
    return f'<div class="tc-inputs">{fld("", "Thường")}{fld("tc-i-border", "Đổi viền 1 → 2: chữ nhích 1")}{fld("tc-i-shadow", "Viền + bóng trong 1 (đang làm)")}{fld("tc-fin", "Outline 2 vào trong 2")}</div>'


def pv_order(m, p):
    tb = lambda k, x: f'<span class="tc-o"><i>{k}</i>{x}</span>'
    return (f'<div class="tc-grid2"><div>{cap("Mỗi nút một điểm dừng")}<div class="tc-ol">{tb(1, "Tạo lệnh")}{tb(2, "Dòng 1 · Sửa")}{tb(3, "Dòng 1 · Huỷ")}{tb(4, "Dòng 2 · Sửa")}{tb(5, "Dòng 2 · Huỷ")}{tb(6, "Dòng 3 · Sửa")}{tb(7, "…")}</div></div>'
            f'<div>{cap("Bảng là một điểm dừng, mũi tên đi trong bảng")}<div class="tc-ol">{tb(1, "Tạo lệnh")}{tb(2, "Bảng: dòng đang chọn")}{tb("↑↓", "đổi dòng")}{tb("←→", "đổi ô, nút")}{tb(3, "Phân trang")}</div></div></div>')


def pv_sticky(m, p):
    head = "header-nav-height"
    rows_ = "".join(f'<div class="tc-sr {"tc-fin" if i == 1 else ""}"><span class="type-code">LVT-2026-041{i}</span></div>' for i in range(1, 6))
    return (f'<div class="tc-grid2"><div>{cap("Không bù: dòng 0411 đang focus nằm dưới thanh, không thấy vòng")}<div class="tc-scr"><div class="tc-sh" style="height:var(--{head})"><span class="type-label">Thanh trên</span></div><div style="margin-top:calc(var(--{head}) * -1)">{rows_}</div></div></div>'
            f'<div>{cap("Bù bằng <code>scroll-padding-top</code>: dòng 0411 hiện ngay dưới thanh")}<div class="tc-scr"><div class="tc-sh" style="height:var(--{head})"><span class="type-label">Thanh trên</span></div><div style="margin-top:var(--focus-offset)">{rows_}</div></div></div></div>')


def pv_trap(m, p):
    sheet = p == "mobile"
    body = (f'<div class="type-title-3">Kết thúc chuyến LVT-2026-0412?</div><div class="type-body tp-sub">Bạn sẽ không sửa được số km sau khi kết thúc.</div>'
            f'<div class="{"tc-stack" if sheet else "tp-acts"}"><span class="tp-btn sec tc-f"><span class="type-label">Để sau</span></span><span class="tp-btn"><span class="type-label">Kết thúc chuyến</span></span></div>')
    return (f'<div class="tc-trap {"b" if sheet else "c"}"><div class="tp-dlg {"tp-sheet" if sheet else "tc-dlg"}">{body}</div></div>'
            + cap("Mở: focus vào nút an toàn · Tab đi vòng trong khung · Esc đóng · đóng xong về nút đã mở."))


def pv_status(m, p):
    dot = lambda c: f'<i class="tc-dot" style="background:var(--color-{c})"></i>'
    return (f'<div class="tc-grid2"><div>{cap("Chỉ bằng màu")}<div class="tc-st">{dot("fg-success-primary")}{dot("fg-warning-primary")}{dot("fg-error-primary")}</div><div class="tc-rowsel"><span class="type-body">LVT-2026-0412</span></div></div>'
            f'<div>{cap("Có chữ hoặc dấu đi kèm")}<div class="tc-st"><span class="tp-chip tp-g">{icon("check", "tp-ic-sm")}&nbsp;Hoàn thành</span><span class="tp-chip tp-y">{icon("clock", "tp-ic-sm")}&nbsp;Chờ duyệt</span></div>'
            f'<div class="tc-rowsel">{icon("check", "tp-ic-md")}<span class="type-body">LVT-2026-0412</span></div></div></div>')


CSS = r"""
.tc-row{display:flex;flex-wrap:wrap;gap:var(--space-xl);align-items:flex-end}
.tc-c{display:inline-grid;justify-items:center;gap:var(--space-xs);min-width:0}
.tc-n{font:600 11px/14px Inter;color:var(--color-text-tertiary)}
.tc-v{font:500 10.5px/14px "JetBrains Mono",monospace;color:var(--color-text-tertiary);text-align:center;white-space:nowrap}
.tc-z{position:relative;display:inline-flex;align-items:center;justify-content:center;min-width:var(--touch-min);min-height:var(--touch-min);outline:1px dashed var(--color-utility-blue-500)}
.tc-zo{background:color-mix(in srgb,var(--color-utility-blue-500) 16%,transparent)}
.tc-ib{display:inline-flex;align-items:center;justify-content:center;width:var(--h);height:var(--h);border-radius:var(--radius-control);box-shadow:inset 0 0 0 1px var(--color-border-primary);color:var(--color-fg-secondary);background:var(--color-bg-primary)}
.tc-bare{display:inline-flex;line-height:0}
.tc-ic12{--ic:var(--icon-size-xs)}
.tc-cap{margin:var(--space-xs) 0}
.tc-f{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.tc-fin{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:calc(var(--focus-width) * -1)}
.tc-fc{outline:var(--focus-width) solid currentColor;outline-offset:var(--focus-offset)}
button.tp-btn{border:0;font:inherit;cursor:pointer}
.tc-live:focus{outline:none}.tc-live:focus-visible{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.tc-livef:focus{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}
.tc-input{height:var(--control-height-md);border:var(--field-border-width) solid var(--color-border-input);border-radius:var(--radius-field);padding:0 var(--space-lg);background:var(--color-bg-primary);color:var(--color-text-primary);font:400 14px/20px var(--font-body);width:150px;min-width:0}
.tc-input:focus{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:calc(var(--focus-width) * -1)}
.tc-grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-lg)}
.tc-grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-lg)}
.tc-line{display:flex;align-items:center;gap:var(--space-xs);border-bottom:1px solid var(--color-border-secondary);padding:var(--space-xs) 0}
.tc-ctx{font:400 13px/18px var(--font-body);min-width:0}
.tc-pse{position:relative;display:inline-flex}.tc-pse::after{content:"";position:absolute;left:50%;top:50%;width:var(--touch-min);height:var(--touch-min);transform:translate(-50%,-50%);outline:1px dashed var(--color-utility-blue-500);background:color-mix(in srgb,var(--color-utility-blue-500) 14%,transparent)}
.tc-wrap{display:flex;align-items:center;gap:var(--space-xs)}.tc-bx{display:inline-flex;align-items:center;justify-content:center;width:var(--touch-min);height:var(--touch-min);outline:1px dashed var(--color-utility-blue-500)}
.tc-clip{display:flex;align-items:center;justify-content:space-between;overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:var(--radius-control);height:var(--control-height-md);padding:0 var(--space-md)}
.tc-pair{display:inline-flex}
.tc-ava{display:inline-flex;align-items:center;justify-content:center;width:var(--size-4xl);height:var(--size-4xl);border-radius:var(--radius-full);background:var(--color-bg-tertiary);font:600 12px/16px Inter}
.tc-tbw{border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);margin-bottom:var(--space-md)}
.tc-clipc{overflow:hidden}
.tc-tb{width:100%;border-collapse:collapse}.tc-tb td{height:var(--table-row-min-height);padding:0 var(--space-lg);border-bottom:1px solid var(--color-border-secondary)}.tc-end{text-align:right}
.tc-tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:var(--space-md)}.tc-t{display:flex;flex-wrap:wrap;gap:var(--space-md);align-items:center;padding:var(--space-lg);border-radius:var(--radius-control);border:1px solid var(--color-border-secondary)}
.tc-cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--layout-list-gap);margin-top:var(--space-lg)}
.tc-solids{display:flex;flex-wrap:wrap;gap:var(--space-lg);margin-bottom:var(--space-md)}
.tc-solid{display:flex;align-items:center;gap:var(--space-lg);padding:var(--space-lg);border-radius:var(--radius-control)}
.tc-ibs{display:inline-flex;align-items:center;justify-content:center;width:var(--control-height-sm);height:var(--control-height-sm);border-radius:var(--radius-control)}
.tc-ov{overflow:hidden;border:1px dashed var(--color-border-primary);border-radius:var(--radius-control);display:inline-flex;max-width:100%}
.tc-menu{display:grid;gap:var(--space-xxs);padding:var(--space-xs);background:var(--color-bg-primary_alt);border:1px solid var(--shadow-lg-border);border-radius:var(--radius-menu);box-shadow:var(--shadow-lg)}
.tc-mi{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) var(--space-md);border-radius:var(--radius-menu-item);background:var(--color-bg-primary_alt)}
.tc-inputs{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:var(--space-lg)}
.tc-i-border{border:2px solid var(--color-focus-ring)}
.tc-i-shadow{border-color:var(--color-focus-ring);box-shadow:inset 0 0 0 1px var(--color-focus-ring)}
.tc-ol{display:grid;gap:var(--space-xs)}.tc-o{display:flex;align-items:center;gap:var(--space-md);font:400 13px/18px var(--font-body)}.tc-o i{font:600 11px/18px "JetBrains Mono",monospace;font-style:normal;min-width:24px;height:18px;padding:0 4px;text-align:center;border-radius:var(--radius-xs);background:var(--color-bg-tertiary)}
.tc-scr{position:relative;height:150px;overflow:hidden;border:1px solid var(--color-border-secondary);border-radius:var(--radius-control)}
.tc-sh{position:relative;z-index:2;display:flex;align-items:center;padding:0 var(--space-lg);background:var(--color-bg-primary_alt);border-bottom:1px solid var(--color-border-secondary)}
.tc-sr{display:flex;align-items:center;height:var(--control-height-lg);padding:0 var(--space-lg);border-bottom:1px solid var(--color-border-secondary)}
.tc-trap{display:flex;background:var(--color-bg-overlay);border-radius:var(--radius-control);min-height:190px;padding:var(--space-lg);margin-bottom:var(--space-md)}.tc-trap.c{align-items:center;justify-content:center}.tc-trap.b{align-items:flex-end;padding:var(--space-lg) 0 0}
.tc-dlg{width:100%;max-width:420px}.tc-stack{display:grid;gap:var(--space-md)}.tc-stack .tp-btn{height:var(--control-height-md)}
.tc-st{display:flex;flex-wrap:wrap;gap:var(--space-md);align-items:center;min-height:var(--chip-height-sm);margin-bottom:var(--space-md)}.tc-dot{width:10px;height:10px;border-radius:var(--radius-full);display:inline-block}
.tc-rowsel{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-md) var(--space-lg);background:var(--color-bg-selected);border-radius:var(--radius-control)}
@media(max-width:820px){.tc-grid2,.tc-grid3,.tc-cards{grid-template-columns:minmax(0,1fr)}}
"""

JS = r"""
function tcM(){document.querySelectorAll('.tc-v[data-m]').forEach(v=>{const zo=v.previousElementSibling;if(!zo)return;const c=zo.firstElementChild;if(!c)return;const a=zo.getBoundingClientRect(),b=c.getBoundingClientRect();const f=x=>String(Math.round(x*10)/10).replace('.',',');const dy=Math.max(0,(a.height-b.height)/2),dx=Math.max(0,(a.width-b.width)/2);v.textContent=f(b.width)+'×'+f(b.height)+(dy||dx?' · +'+f(dy)+'/phía':' · đủ')})}
window.afterToggle=tcM;tcM();
"""


# ---------- bảng đối chiếu ----------
CMP = [
    ("<code>focus-ring</code> (màu)", "brand-500 #9E77ED", "<code>color/focus/ring</code> than chì", DIFF, "DEC-170: một màu cho mọi khách, không trùng sắc với lỗi"),
    ("<code>focus-ring-error</code> (màu)", "red-500 #EF4444", "<code>color/focus/ring_error</code> red-700", DIFF, "DEC-198, DEC-318: đỏ đậm hơn"),
    ("Style <code>focus-ring</code>", "spread 4 + spread 2 nền: vòng nhìn 2, cách 2", "<code>outline</code> 2 cách 2, khe trong suốt", DIFF, "DEC-327: cùng hình, không tô khe"),
    ("Style <code>focus-ring-error</code>", "như trên, đỏ", "như trên, <code>color/focus/ring_error</code>", DIFF, "DEC-327"),
    ("Style <code>focus-ring-shadow-xs</code>", "vòng + bóng xs", "không có", DIFF, "DEC-327: vòng là lớp riêng, bóng giữ nguyên"),
    ("Style <code>focus-ring-shadow-sm</code>", "vòng + bóng sm", "không có", DIFF, "DEC-327"),
    ("Style <code>focus-ring-error-shadow-xs</code>", "vòng đỏ + bóng xs", "không có", DIFF, "DEC-327"),
    ("Style <code>focus-ring-shadow-xs-skeuomorphic</code>", "vòng + xs + 2 lớp trong", "không có", DIFF, "DEC-327: nút giữ phẳng"),
    ("Style <code>focus-ring-error-shadow-xs-skeuomorphic</code>", "như trên, đỏ", "không có", DIFF, "DEC-327"),
    ("Class <code>outline-2</code>", f"{U_O2} dòng, ghi thẳng trong class", "<code>focus/width</code> 2", OK, "cùng số, mình có token"),
    ("Class <code>outline-offset-2</code>", f"{U_OFF} dòng", "<code>focus/offset</code> 2", OK, "cùng số, mình có token"),
    ("Class <code>-outline-offset-2</code>", f"{U_NEG} dòng; {len(U_NEG_FILES)} thư mục: bảng, tab, menu, tag…", "chưa có luật", GAP, "mục tc10, tc14"),
    ("<code>focus-visible:</code> và <code>isFocusVisible</code>", f"{U_FV} và {U_IFV} dòng", f"luật chưa ghi; {len(FV_PAGES)}/{NP} trang <code>_work</code> dùng thật", GAP, "mục tc15"),
    ("Ô nhập <code>ring-2 ring-brand</code>", "viền 2, không quầng, theo <code>isFocusWithin</code>", "viền 2 <code>color/focus/ring</code>, bóng trong 1", DIFF, "DEC-321; cách vẽ ở mục tc16"),
    ("<code>outline-brand</code>, <code>outline-error</code> trên nút", "theo màu nút", "than chì; nút Danger đỏ", DIFF, "DEC-170, DEC-198"),
    ("Dialog của <code>react-aria-components</code>", "thư viện lo giữ focus, Esc, trả focus", "ghi rải rác trong spec", GAP, "mục tc19"),
    ("Không có token vùng chạm", f"{U_TOUCH} dòng khớp <code>touch-</code>, <code>min-h-11</code>, <code>tap-</code>", "<code>touch/min</code> Web 24, App 44", OWN, "DEC-138, WCAG 2.5.8"),
    ("Không có token dày, cách vòng", "ghi trong class", "<code>focus/width</code>, <code>focus/offset</code>", OWN, "đổi một chỗ, đọc được từ Figma"),
    ("Không có", "—", "<code>upload/app-tap-min-height</code> 72", OWN, "DEC-307, ô tải lên trên app"),
    ("<code>ButtonUtility</code> xs, sm, md, lg", "28, 36, 40, 44", f"Web {n(H['sm'][0])}, {n(H['md'][0])}, {n(H['ml'][0])}, {n(H['lg'][0])} · App {n(H['sm'][1])}, {n(H['md'][1])}, {n(H['lg'][1])}", DIFF, "web dày hơn, app cao hơn (DEC-097)"),
    ("<code>Button</code> xs…xl (tính từ lề + dòng chữ)", "32, 36, 40, 44, 48", f"Web {n(H['sm'][0])}–{n(H['lg'][0])} · App {n(H['sm'][1])}–{n(H['lg'][1])}", DIFF, "DEC-097: lái xe đeo găng"),
    ("<code>Checkbox</code> sm, md", "16, 20", "16, 20 (<code>_work/form-controls</code>)", OK, "vùng bấm tính cả nhãn"),
    ("<code>Toggle</code> sm, md", "20×36, 24×44", "20×36 (<code>_work/form-controls</code>)", DIFF, "bậc lớn hơn chưa ai cần"),
    ("<code>Table</code> dòng sm, md", "56, 72", f"<code>table/row-min-height</code> {n(px('table/row-min-height'))}", DIFF, "DEC-324 không đổi; bảng dày hơn cho điều vận"),
]
_CNT = collections.Counter(r[3] for r in CMP)
CMP_ROWS = [[r[0], r[1], r[2], st(r[3], r[4])] for r in CMP]

# ---------- bảng số vùng chạm ----------
def _row(name, h_w, h_a, note=""):
    w = "—" if h_w is None else f"+{n(bu(h_w, T_W))}"
    a = "—" if h_a is None else f"+{n(bu(h_a, T_A))}"
    gw = "—" if h_w is None else n(need_gap(h_w, T_W))
    ga = "—" if h_a is None else n(need_gap(h_a, T_A))
    return [name, f"n:{'—' if h_w is None else n(h_w)}", f"n:{w}", f"n:{gw}", f"n:{'—' if h_a is None else n(h_a)}", f"n:{a}", f"n:{ga}", note]


SIZE_ROWS = [
    _row("<code>control/height/sm</code>", H["sm"][0], H["sm"][1], "Nút trong hàng bảng (Web); tab chip, nút SM (App)"),
    _row("<code>control/height/md</code>", H["md"][0], H["md"][1], "Nút mặc định 32 · nút nhỏ 42"),
    _row("<code>control/height/ml</code>", H["ml"][0], H["ml"][1], "Nút icon thanh trên"),
    _row("<code>control/height/lg</code>", H["lg"][0], H["lg"][1], "Nút cần nổi · nút chân màn 52"),
    _row("Dòng <code>table/row-min-height</code>", px("table/row-min-height"), None, "Đủ, kể cả mục tiêu 44"),
    _row("<code>header-nav/height</code>", px("header-nav/height", "web"), px("header-nav/height", "mobile"), "Thanh, nút trong thanh tính riêng"),
    _row("Ô chọn (<code>_work/form-controls</code>)", 16, 20, "Web 16, App 20; nhãn bấm được"),
    _row("Icon đứng riêng <code>icon/size/lg</code>", IC["lg"], IC["lg"], "Sau DEC-329"),
    _row("Icon đứng riêng <code>icon/size/md</code>", IC["md"], IC["md"], "Help icon"),
    _row("Icon đứng riêng <code>icon/size/sm</code>", IC["sm"], IC["sm"], "Icon xoá"),
    _row("Icon đứng riêng <code>icon/size/xs</code>", IC["xs"], IC["xs"], "Xoá trong tag"),
]

WCAG = [
    ["2.5.8 Target Size (Minimum)", "AA", "“at least 24 by 24 CSS pixels”, trừ khi vòng tròn 24 quanh tâm không chạm đích khác; còn ngoại lệ tương đương, trong dòng chữ, do trình duyệt, bắt buộc.", f"Web {n(T_W)} đạt theo số. App {n(T_A)} vượt."],
    ["2.5.5 Target Size (Enhanced)", "AAA", "“at least 44 by 44 CSS pixels”.", f"App đạt theo số. Web không nhắm mức này."],
    ["2.4.7 Focus Visible", "AA", "“has a mode of operation where the keyboard focus indicator is visible”.", "Có vòng; chỗ bị cắt là rủi ro (tc10, tc13)."],
    ["2.4.11 Focus Not Obscured (Minimum)", "AA", "“not entirely hidden due to author-created content”.", "Chưa có luật cho thanh dính (tc18)."],
    ["2.4.13 Focus Appearance", "AAA", "Diện tích bằng viền 2 CSS px, tương phản 3:1 giữa lúc có và không focus.", f"Vòng 2, thấp nhất {MIN_NS_TXT}:1 trên nền không đặc."],
    ["2.4.3 Focus Order", "A", "Thứ tự focus giữ được nghĩa và thao tác.", "tc17"],
    ["2.1.2 No Keyboard Trap", "A", "Vào được bằng bàn phím thì ra được bằng bàn phím.", "tc19"],
    ["1.4.1 Use of Color", "A", "Màu không là cách duy nhất để truyền thông tin.", "tc20"],
    ["1.4.11 Non-text Contrast", "AA", "Thành phần giao diện và trạng thái đạt 3:1 với màu kề.", "tc11, tc12"],
]

SHARED = [
    ["<code>touch/min</code>", f"{n(T_W)} · {n(T_A)}", "Giữ tên, giữ số. Thêm đè 44 khi con trỏ thô cho web."],
    ["<code>focus/width</code>, <code>focus/offset</code>", f"{n(F_W)}, {n(F_O)}", "Giữ. Vòng vào trong tính bằng <code>focus/width</code> nhân −1, không thêm token."],
    ["<code>color/focus/ring</code>, <code>color/focus/ring_error</code>", "giữ", "Giữ màu. Nền đặc dùng màu chữ của nền, không thêm token."],
    ["Cách bù vùng chạm", "lớp giả", "Một lớp dùng chung tính từ <code>touch/min</code>, thay các số tay."],
    ["Vòng focus chỗ nào", "ngoài · trong", "Ngoài: nút, thẻ, ô chọn. Trong: dòng, ô bảng, mục menu, tab. Sidebar giữ ngoài."],
    ["Khi nào hiện", "<code>:focus-visible</code>", "Ô nhập vẫn hiện cả khi bấm chuột do trình duyệt lo."],
    ["Ô nhập", "outline 2 vào trong", "Nhìn như đang làm, không dùng bóng."],
    ["Bàn phím", "3 luật", "Thứ tự theo DOM; bảng, menu, tab một điểm dừng; dialog giữ focus trong khung và trả về."],
    ["Thanh dính", "<code>scroll-padding</code>", "Tính từ <code>header-nav/height</code> cộng phần vòng."],
    ["Trạng thái", "không chỉ màu", "Luôn có chữ hoặc dấu, dòng chọn có ô chọn."],
]

# ---------- mục chọn ----------
ITEMS = [
    dict(id="tc00", grp="Cấu trúc", title="Tên token vùng chạm và vòng focus có theo Untitled không?",
         why=f"Untitled <mark>không có token vùng chạm</mark>: quét react của họ có {U_TOUCH} dòng khớp <code>touch-</code>, <code>min-h-11</code>, <code>tap-</code>. Dày và cách vòng họ ghi thẳng class ({U_O2} và {U_OFF} dòng). "
             "Hướng đã chốt là tên theo Untitled (DEC-316), nhưng ở đây <b>không có tên nào để theo</b>, trừ màu <code>color/focus/ring</code> đã khớp. Tên hiện đang được "
             f"{SPEC_TOUCH}/{len(spec_text)} spec nhắc tới vùng chạm, đổi tên chỉ thêm việc.",
         untitled="Không có biến. Màu <code>--color-focus-ring</code>, <code>--color-focus-ring-error</code>; class <code>outline-2</code>, <code>outline-offset-2</code>.",
         ours="<code>touch/min</code>, <code>focus/width</code>, <code>focus/offset</code>, <code>color/focus/ring</code>, <code>color/focus/ring_error</code>.",
         astryx="Không có token vùng chạm; ghi chữ “vùng chạm 44” trong <code>design/design.md</code>. Focus nút: “viền ngoài 2px <code>{colors.accent}</code>”.",
         pv=panes(pv_names, platforms=("web", "mobile")),
         opts=[("keep", "Giữ tên touch/min, focus/width, focus/offset; không đổi spec nào", True),
               ("size", "Chuyển thành size/touch-min, sửa mọi spec đang nhắc", False)]),
    dict(id="tc01", grp="Vùng chạm", title=f"App: sàn {n(T_A)} có đủ cho nút {n(H['lg'][1])}, {n(H['md'][1])}, {n(H['sm'][1])}?",
         why=f"<mark>Nút chân màn {n(H['lg'][1])}</mark> dư, <b>nút nhỏ {n(H['md'][1])}</b> thiếu {n(bu(H['md'][1], T_A))} mỗi phía, nhưng còn <mark>nút SM {n(H['sm'][1])} thiếu {n(bu(H['sm'][1], T_A))} mỗi phía</mark>. "
             f"<code>design-system/foundations/touch-focus.md</code> chỉ nói 52 và 42, chưa nhắc 36 mà <code>control/height/sm</code> đang dùng cho tab chip, nút SM; Alert trên app đang đặt <code>.bt</code> cao 36 và bù tay 4. "
             f"DEC-138 chốt 44 vì “User ưu tiên iOS”, DEC-097 ghi lý do “lái xe đeo găng, bấm ngón cái ở đáy màn”. Nguồn: HIG Accessibility “44x44 pt” (đọc 02/11), WCAG 2.5.5 “44 by 44 CSS pixels”. 48dp Android: theo DEC-138, lượt này chưa kiểm lại.",
         untitled="Không có sàn. <code>ButtonUtility</code> lớn nhất <code>size-11</code> 44, nhỏ nhất 28.",
         ours=f"<code>touch/min</code> App {n(T_A)}; <code>control/height/sm</code> {n(H['sm'][1])}, <code>control/height/md</code> {n(H['md'][1])}, <code>control/height/lg</code> {n(H['lg'][1])}.",
         astryx="Nút SM 28, MD 32, LG 36 cho web; app ghi “Mobile LG trong vùng chạm 44”.",
         pv=panes(pv_app_min, platforms=("mobile",)) + '<div style="height:10px"></div>' + panes(pv_48, modes=("light",), platforms=("mobile",)),
         opts=[("keep", "Giữ sàn 44; ghi thêm nút SM 36 bù 4 mỗi phía vào foundations", True),
               ("up36", "Bỏ 36 trên app: nút SM lên 42, tab chip cao thêm 6", False),
               ("48", "Mở lại DEC-138: sàn 48. Bằng chứng mới: chưa có; chỉ chọn nếu đo thật với lái xe đeo găng", False)]),
    dict(id="tc02", grp="Vùng chạm", title=f"Web: sàn {n(T_W)} so với nút {n(H['sm'][0])}, {n(H['md'][0])} và icon đứng riêng",
         why=f"Mọi nút web từ <b>{n(H['sm'][0])}</b> trở lên đã đủ, không phải bù. Chỗ thật sự thiếu là <mark>icon đứng riêng</mark>: {n(IC['md'])} thiếu {n(bu(IC['md'], T_W))}, {n(IC['sm'])} thiếu {n(bu(IC['sm'], T_W))}, {n(IC['xs'])} thiếu {n(bu(IC['xs'], T_W))} mỗi phía. "
             "WCAG 2.5.8 mức AA: “at least 24 by 24 CSS pixels”, có ngoại lệ khoảng cách: vòng tròn 24 quanh tâm không chạm đích khác. Sàn 24 đúng cho điều vận dày dữ liệu, nút trong bảng đứng sát nhau.",
         untitled="Không có sàn; nút nhỏ nhất <code>size-7</code> 28; nút xoá trong tag là <code>TagCloseX</code>, không có phần bù.",
         ours=f"<code>touch/min</code> Web {n(T_W)}; breadcrumbs ghi “vùng bấm 24”, field-upload ghi vùng vô hình <code>touch/min</code>.",
         astryx="Nút SM 28 trong ô bảng; chưa ghi sàn web.",
         pv=panes(pv_web_min, platforms=("web",)),
         opts=[("keep", "Giữ sàn 24 AA; nút 28 trở lên không bù, icon đứng riêng bù tới 24", True),
               ("28", "Nâng sàn web lên 28: icon đứng riêng bù thêm 2 mỗi phía, cột bảng chật hơn", False),
               ("44", "Theo AAA 44 trên web: dòng và nút trong bảng phải giãn, bảng điều vận mất mật độ", False)]),
    dict(id="tc03", grp="Vùng chạm", title="Mobile web và tablet cảm ứng đang rơi vào sàn 24",
         why=f"Màn đặt chế độ <code>Platform</code> một lần; web mặc định là Web, nên <mark>mobile web 393 và tablet (DEC-095, DEC-324) đọc <code>touch/min</code> = {n(T_W)}</mark> trong khi người dùng bấm bằng ngón tay. "
             f"Cả DS chưa nói rõ chuyện này. Nút {n(H['md'][0])} bù tới 44 cần {n(bu(H['md'][0], 44))} mỗi phía và hai nút cạnh nhau phải cách {n(need_gap(H['md'][0], 44))}. "
             "<code>@media (pointer: coarse)</code> đổi được riêng vùng vô hình, không đụng mật độ; chưa kiểm trên máy thật, Figma không vẽ được điều kiện này nên chỉ ghi spec.",
         untitled="Không xử lý riêng; nút giữ số ở mọi màn. Modal, slideout đổi bố cục theo <code>sm:</code>.",
         ours=f"<code>touch/min</code> theo <code>data-platform</code>; <code>design-system/foundations/grids.md</code> kiểm mobile web 393; {sum(1 for s in page_css.values() if 'pointer:coarse' in s or 'pointer: coarse' in s)}/{NP} trang <code>_work</code> dùng <code>pointer: coarse</code>.",
         astryx="Chưa có. Có “DateInput… bản cảm ứng riêng bên trong”.",
         pv=panes(pv_coarse, platforms=("web",)),
         opts=[("coarse", "Thêm một luật CSS: con trỏ thô thì touch/min = 44, nút nhìn giữ nguyên", True),
               ("mode", "Mobile web dùng cả chế độ Mobile: nút 42, chữ, lề đổi theo app", False),
               ("none", "Để sàn 24 như hiện tại, ghi là chấp nhận", False)]),
    dict(id="tc04", grp="Vùng chạm", title="Icon app nhỏ đi theo DEC-329: phần bù đổi ở đâu?",
         why=f"DEC-329 gộp icon một bộ: md {IC_OLD['md']} → {n(IC['md'])}, lg {IC_OLD['lg']} → {n(IC['lg'])}, sm {IC_OLD['sm']} → {n(IC['sm'])} (số cũ từ <code>tokens.json</code> 0.22.0). <mark>Nút có chữ, nút icon không đổi vùng chạm</mark>: cao vẫn {n(H['md'][1])}, lề trong nút icon tăng từ {n((H['md'][1] - IC_OLD['md']) / 2)} lên {n((H['md'][1] - IC['md']) / 2)}. "
             f"Thay đổi nằm ở <b>icon đứng riêng</b>: phần bù md {n(bu(IC_OLD['md'], T_A))} → {n(bu(IC['md'], T_A))}, lg {n(bu(IC_OLD['lg'], T_A))} → {n(bu(IC['lg'], T_A))}. Help icon đang đặt hộp 24 và <code>inset:-10px</code> nên vẫn đủ 44; <code>design-system/components/base/tooltip.md</code> còn ghi cỡ 20 đã cũ.",
         untitled="<code>ButtonUtility</code>: khung 44 icon 24, khung 40 icon 20. Không có icon đứng riêng bấm được trên app.",
         ours="<code>icon/size/md</code>, <code>icon/size/lg</code> (DEC-329, không mở lại); <code>touch/min</code>.",
         astryx="Nút Ghost Icon Only Mobile LG “trong vùng chạm 44”, icon 20–24 trong bộ cũ.",
         pv=panes(pv_icons, platforms=("mobile",)),
         note="Phụ thuộc <code>icon/size/*</code> của DEC-329 đang áp song song: số trên trang đọc lúc dựng, dựng lại khi token đổi.",
         opts=[("calc", "Vùng chạm tính theo phần bấm; icon đứng riêng bù vô hình tới 44, không đổi số icon", True),
               ("btn", "Mọi icon đứng riêng trên app đổi thành nút icon 42 có nền khi nhấn", False),
               ("box", "Giữ cách hiện tại: hộp 24 rồi bù 10, ghi ngoại lệ cho từng chỗ", False)]),
    dict(id="tc05", grp="Vùng chạm", title="Bù vùng chạm bằng cách nào?",
         why=f"Spec nói “vùng bấm vô hình” ở {SPEC_TOUCH}/{len(spec_text)} file, nhưng <mark>{TOUCH_VAR}/{NP} trang <code>_work</code> dùng <code>var(--touch-min)</code></mark>; có {HAND_N} chỗ viết số tay: {HAND_TXT}. Đổi sàn thì không chỗ nào đổi theo. "
             f"Lớp giả <code>::after</code> không đổi bố cục nên dòng giữ nguyên, nhưng <b>bị khung <code>overflow:hidden</code> cắt mất</b>; {OVH_TOTAL} luật <code>overflow:hidden</code> trong css các trang <code>_work</code>, chưa soát hết chỗ nào chứa nút.",
         untitled="Không có cơ chế chung. Nút dùng lề trong để đủ cao (<code>size-11</code>, <code>py-3</code>).",
         ours="<code>design-system/components/README.md</code>: khung Figma <code>Vùng chạm · touch/min</code> viền chấm chỉ để mô tả, code tự đặt lề đệm.",
         astryx="Chỉ ghi chữ “vùng chạm 44”; “ô chừa đệm phải 52” cho nút trong ô nhập.",
         pv=panes(pv_hit, platforms=("mobile",)),
         opts=[("after", "Một lớp ::after dùng chung, tính từ touch/min trừ cao phần bấm; thay các số tay", True),
               ("pad", "Lề trong + lề âm: không cần lớp giả, nhưng dễ đẩy chữ", False),
               ("wrap", "Bọc khung đủ cao: dễ làm, dòng và hàng cao thêm", False)]),
    dict(id="tc06", grp="Vùng chạm", title="Khoảng cách giữa hai vùng chạm",
         why=f"<code>design-system/foundations/touch-focus.md</code> chỉ viết “cách nhau đủ”. Tính ra: app nút {n(H['md'][1])} cần cách <b>≥ {n(need_gap(H['md'][1], T_A))}</b>, nút {n(H['sm'][1])} cần <b>≥ {n(need_gap(H['sm'][1], T_A))}</b>, <mark>hai icon {n(IC['md'])} đứng riêng cần ≥ {n(need_gap(IC['md'], T_A))}</mark>. "
             f"<code>tab/gap</code> đang {n(px('tab/gap', 'mobile'))} vừa khít tab {n(H['sm'][1])}; <code>notification/action-gap</code> App {n(px('notification/action-gap', 'mobile'))} dư. HIG: “add about 12 points of padding around elements that include a bezel”, không viền “about 24 points”. WCAG 2.5.8 chỉ cần vùng 24 không chạm nhau. Lái xe đeo găng (DEC-097) nên chỉ “không chồng” là mức thấp nhất.",
         untitled="Không có luật về khoảng cách đích bấm; <code>gap-*</code> ghi theo từng component.",
         ours=f"<code>tab/gap</code> {n(px('tab/gap', 'mobile'))}, <code>notification/action-gap</code> {n(px('notification/action-gap', 'web'))} · {n(px('notification/action-gap', 'mobile'))}.",
         astryx="Chưa ghi luật khoảng cách đích bấm.",
         pv=panes(pv_gap, platforms=("web", "mobile"), modes=("light",)),
         opts=[("no-overlap8", "Hai vùng không chồng, và trên app cách nhau tối thiểu 8", True),
               ("no-overlap", "Chỉ cần hai vùng không chồng, tính theo công thức sàn trừ cao", False),
               ("hig12", "Theo HIG: tối thiểu 12 trên app, nhóm nút rộng thêm 4", False)]),
    dict(id="tc07", grp="Vùng chạm", title="Nút chỉ có icon: cỡ tối thiểu và tên đọc",
         why=f"Web nhỏ nhất {n(H['sm'][0])}, mặc định {n(H['md'][0])}, thanh trên {n(H['ml'][0])}; app {n(H['md'][1])} thiếu {n(bu(H['md'][1], T_A))} mỗi phía. Sau DEC-329, nút app {n(H['md'][1])} icon {n(IC['md'])} còn <mark>lề {n((H['md'][1] - IC['md']) / 2)}</mark>, icon {n(IC['lg'])} lề {n((H['md'][1] - IC['lg']) / 2)}. "
             "Không có chữ nên tên đọc là bắt buộc: DEC-329 đã có 3 luật nhãn và trình đọc màn hình. Mục này chỉ chốt cỡ và cái gì đi kèm trên từng nền tảng.",
         untitled="<code>ButtonUtility</code> xs 28, sm 36, md 40, lg 44; có sẵn thuộc tính <code>tooltip</code>, không bắt buộc.",
         ours="<code>control/height/sm</code>, <code>control/height/md</code>, <code>control/height/ml</code>; icon nút theo <code>icon/size/md</code>.",
         astryx="Button Type = Icon Only, cỡ theo Button; Desktop MD + Tooltip, Mobile LG trong vùng 44.",
         pv=panes(pv_ionly, platforms=("web", "mobile")),
         opts=[("rule", "Web từ 28, có tooltip; app 42 + bù 1; tên đọc theo DEC-329", True),
               ("web32", "Web tối thiểu 32: bỏ nút icon 28 trong hàng bảng, cột thao tác rộng thêm", False),
               ("app44", "App nhìn thấy 44: lệch với nút chữ 42 đứng cạnh", False)]),
    dict(id="tc08", grp="Vòng focus", title="Dọn các chỗ focus đang lệch token",
         why=f"DEC-327 đã bỏ khe và <code>--focus-color</code>, nhưng <mark>{len(GAP_PAGES)} trang <code>_work</code> còn khai <code>--color-focus-gap</code></mark> trong bộ token nhúng cũ ({', '.join(GAP_PAGES) or 'không còn'}), {len(COLOR_PAGES)} trang gọi <code>--focus-color</code> ({', '.join(COLOR_PAGES) or 'không còn'}), {len(ALIAS_PAGES)} trang đặt bí danh <code>--focus</code> ({', '.join(ALIAS_PAGES) or 'không còn'}). "
             f"Trong spec: <code>design-system/components/base/avatar.md</code> ghi “focus ring 2 cách 4; vùng chạm 48”, <code>design-system/components/application/field-upload.md</code> ghi “cách <code>focus/width</code>”, css ghi trần <code>2px</code>. <code>design-system/components/application/vehicle-card.md</code> dùng “viền 2” thay vòng. "
             + ("Biến khe đã rời <code>tokens.css</code>, các trang này dựng lại là hết." if TOKEN_GAP_GONE else "Biến khe còn trong <code>tokens.css</code> tới khi áp xong DEC-327."),
         untitled="Ghi thẳng class <code>outline-2</code>, <code>outline-offset-2</code> ở mọi component; khác chỉ ở ô nhập, bảng, menu.",
         ours="<code>focus/width</code>, <code>focus/offset</code>, <code>color/focus/ring</code>; xem rule ds-stale.",
         astryx="Viền ngoài 2px, không tách token.",
         pv=panes(pv_stale, platforms=("web",)),
         opts=[("sync", "Đưa mọi chỗ về focus/width, focus/offset khi sync; avatar về 2 cách 2 và vùng chạm theo touch/min", True),
               ("avatar", "Như trên nhưng giữ avatar cách 4 để vòng không đè chấm trạng thái", False)]),
    dict(id="tc09", grp="Vòng focus", title="App có cần vòng focus không?",
         why=f"Chạm tay <b>không tạo focus nhìn thấy</b>; người dùng bàn phím ngoài, Switch Control, TalkBack, VoiceOver thì có. WCAG 2.4.7 nói “any keyboard operable user interface”. Trình đọc màn hình có con trỏ riêng của hệ điều hành; <mark>chưa kiểm</mark> hành vi từng hệ và stack app vì <code>design-system/architecture.md</code> chưa ghi stack. "
             f"<code>focus/width</code> và <code>focus/offset</code> có đủ chế độ Mobile ({n(px('focus/width', 'mobile'))}, {n(px('focus/offset', 'mobile'))}). Ô đang gõ thì khác: viền 2 (DEC-170) là tín hiệu chạm tay vẫn thấy, nên giữ.",
         untitled="Chỉ có web (<code>react/components</code>), không nói về bàn phím ngoài trên điện thoại.",
         ours=f"<code>focus/width</code>; spec app của Tooltip ghi “mở sheet: focus vào tiêu đề”, chưa có luật chung. DEC-327 chỉ nói cho web.",
         astryx="Chưa ghi riêng cho app (không thấy trong <code>design/design.md</code>).",
         pv=panes(pv_app_focus, platforms=("mobile",)),
         opts=[("kbd", "App không vẽ state Focus trên Figma; code bật vòng 2 cách 2 khi có bàn phím; ô đang gõ giữ viền 2", True),
               ("all", "Vẽ đủ state Focus trên Figma cho mọi component app, thêm biến thể cần soát", False),
               ("none", "Bỏ focus/* ở chế độ Mobile, dựa hẳn vào hệ điều hành; ô đang gõ giữ viền", False)]),
    dict(id="tc10", grp="Vòng focus", title="Focus trong bảng: dòng, ô, nút trong ô",
         why=f"Vòng ngoài ló ra {n(RING_OUT)} quanh dòng. Bảng nằm trong thẻ bo <code>radius/card</code> {n(px('radius/card'))} thường có <code>overflow:hidden</code>, nên <mark>hai đầu dòng bị cắt</mark>, và dòng kế bên đè lên mép dưới. Untitled giải bằng vòng vào trong: <code>focus-visible:-outline-offset-2</code> trên cả dòng và ô, kèm <code>z-1</code>. "
             f"Nút trong ô thì khác: dòng cao {n(px('table/row-min-height'))}, nút {n(H['sm'][0])}, còn dư {n((px('table/row-min-height') - H['sm'][0]) / 2)} mỗi phía, vòng ngoài vẫn lọt.",
         untitled=f"<code>application/table</code>: dòng và ô <code>-outline-offset-2</code>; toàn bộ {U_NEG} dòng dùng vòng vào trong.",
         ours="Chưa có luật. <code>focus/offset</code> 2 ở mọi nơi.",
         astryx="“Bàn phím: focus tay nắm → Space → ←/→”; ô sửa “focus ô rồi Enter / F2”, không nói hình vòng.",
         pv=panes(pv_table, platforms=("web",)),
         opts=[("inset", "Dòng và ô tự nhận focus thì vòng vào trong 2; nút trong ô giữ vòng ngoài", True),
               ("outer", "Vòng ngoài khắp nơi, bỏ overflow:hidden khỏi thẻ bảng, góc dòng không còn được bo cắt", False),
               ("bg", "Chỉ tô nền dòng khi focus: không có vòng, dễ lẫn với dòng chọn", False)]),
    dict(id="tc11", grp="Vòng focus", title="Trên thẻ, nền phụ, nền trạng thái nhạt",
         why=f"Khe trong suốt nên vòng nằm trên nền nơi đặt (DEC-327). Đo trên mọi nền không đặc: <mark>thấp nhất {MIN_NS_TXT}:1</mark> (cần 3:1 theo WCAG 1.4.11), nền chính {RING_ON_PRIMARY} Sáng, {RING_ON_PRIMARY_D} Tối. <b>Không cần biến thể theo nền.</b> "
             f"Thẻ bấm được cách nhau <code>layout/list-gap</code> {n(px('layout/list-gap'))} · {n(px('layout/list-gap', 'mobile'))}, lớn hơn phần ló {n(RING_OUT)} nên không đè thẻ kế. Riêng <code>design-system/components/application/vehicle-card.md</code> đang ghi “viền 2”, khác phần còn lại.",
         untitled="<code>outline-focus-ring</code> tím trên mọi nền, thêm <code>outline-offset-2</code>. Thẻ bấm được chưa thấy mẫu chung (chưa kiểm hết).",
         ours="<code>color/focus/ring</code> trên <code>color/bg/secondary</code>, <code>color/bg/selected</code>, <code>color/bg/warning-primary</code>.",
         astryx="ClickableCard có Focused; Focused dùng <code>{colors.accent}</code>, đổi theo khách.",
         pv=panes(pv_card, platforms=("web",)),
         opts=[("one", "Một vòng ngoài cho mọi nền không đặc; thẻ bấm được cũng vậy, sửa spec vehicle-card", True),
               ("border", "Thẻ dùng viền 2 như vehicle-card, nút dùng vòng: hai cách vẽ", False)]),
    dict(id="tc12", grp="Vòng focus", title="Trên nền màu đặc",
         why=f"Vòng than chì trên nền đặc rớt: <code>color/bg/primary_solid</code> {rr('color/focus/ring', 'color/bg/primary_solid')} Sáng, {rr('color/focus/ring', 'color/bg/primary_solid', 'd')} Tối; <code>color/bg/error-solid</code> {rr('color/focus/ring', 'color/bg/error-solid')} Sáng. Nút Primary tự thân cũng {RING_ON_BTN}, chỉ đạt nhờ <b>khe trong suốt tách vòng khỏi nút</b>; đây là lý do nút đặc không được dùng vòng vào trong. "
             "Nhưng hiện <mark>chưa component đã duyệt nào đặt control lên nền đặc</mark>: Toast nền trắng (DEC-286), Alert nền nhạt (DEC-287), Tooltip không có phần bấm. Thêm token lúc này là token không ai dùng (tinh thần DEC-320). Một token đảo cũng không đủ: ở Tối <code>color/bg/primary_solid</code> sáng còn <code>color/bg/error-solid</code> đậm, nên một màu không đạt cả hai. <code>currentColor</code> mượn đúng màu chữ đã đạt tương phản của từng nền, không thêm gì.",
         untitled="<code>button-utility</code> bản <code>dark</code> vẫn giữ <code>outline-focus-ring</code> trên nền tối; không có màu riêng.",
         ours="<code>color/focus/ring</code>, <code>color/focus/ring_error</code>; không có bản đảo.",
         astryx="Một <code>{colors.accent}</code>, chưa ghi trường hợp nền đặc.",
         pv=panes(pv_solid, platforms=("web",)),
         tokens=[("color/focus/ring_inverse", "Sáng trắng · Tối than chì", "Chỉ khi chọn phương án thêm token: control trên nền đặc")],
         opts=[("current", "Không thêm token; ghi luật: control trên nền đặc thì vòng dùng màu chữ của nền", True),
               ("token", "Thêm color/focus/ring_inverse ngay, chưa component nào dùng", False),
               ("ban", "Cấm đặt control lên nền đặc", False)]),
    dict(id="tc13", grp="Vòng focus", title="Vòng bị overflow cắt",
         why=f"Vòng ló {n(RING_OUT)} ra ngoài phần tử. Css các trang <code>_work</code> có {OVH_TOTAL} luật <code>overflow:hidden</code>, nhiều nhất {max(OVH, key=OVH.get)} {max(OVH.values())}; số này <b>tính cả khung trình bày của trang review</b>, chưa tách được khung thật. "
             "WCAG 2.4.7 cần nhìn thấy, vòng mất là lỗi. Luật tính được từ số thật: <mark>lề khung ≥ 4 thì vòng ngoài, lề &lt; 4 thì vòng vào trong</mark>. Vùng chạm cũng dính cùng khung cắt (tc05).",
         untitled=f"Không có luật viết ra; họ dùng <code>-outline-offset-2</code> ở {len(U_NEG_FILES)} thư mục ({', '.join(U_NEG_FILES)}) và <code>focus-visible:z-1</code> để không bị đè.",
         ours="<code>focus/width</code> + <code>focus/offset</code> = 4; chưa có luật.",
         astryx="Input Ring dùng inset 3px nên không bị cắt; nút viền ngoài chưa ghi.",
         pv=panes(pv_clip, platforms=("web",)),
         opts=[("rule", "Luật: lề khung ≥ 4 thì vòng ngoài, < 4 thì vòng vào trong; thêm dòng kiểm vào đối chiếu foundation", True),
               ("clip", "Cho vòng tràn bằng overflow:clip + overflow-clip-margin 4 (chưa kiểm hết trình duyệt)", False),
               ("each", "Không ghi luật chung, xử lý theo từng component", False)]),
    dict(id="tc14", grp="Vòng focus", title="Mục menu, sidebar, tab: vòng ngoài hay trong",
         why=f"Menu lề {n(px('space/xs'))} (DEC-328), hai mục cách {n(px('space/xxs'))} ở màn mẫu (Untitled <code>py-px</code> mỗi mục cũng ra 2): vòng ngoài <mark>đè mục kế bên {n(RING_OUT - px('space/xxs'))}</mark> và chạm mép menu. Untitled đặt menu, tab vào trong (<code>-outline-offset-2</code>) nhưng <b>sidebar giữ ngoài</b> kèm <code>focus-visible:z-10</code>. Spec sidebar của mình cũng đang ghi vòng 2 cách 2. "
             f"Vòng vào trong trên nền chọn vẫn đủ: {rr('color/focus/ring', 'color/bg/selected')} Sáng, {rr('color/focus/ring', 'color/bg/selected', 'd')} Tối.",
         untitled="<code>base/dropdown</code> và <code>application/tabs</code>: <code>-outline-offset-2</code>; <code>nav-item</code>: <code>outline-offset-2</code> + <code>focus-visible:z-10</code>.",
         ours="<code>radius/menu</code>, <code>radius/menu-item</code>; <code>design-system/components/application/sidebar-navigation.md</code> “vòng 2px cách 2px”.",
         astryx="Chưa ghi hình vòng cho mục menu.",
         pv=panes(pv_menu, platforms=("web",)),
         opts=[("untitled", "Theo Untitled: menu, tab vào trong; sidebar giữ ngoài và nổi lên trên", True),
               ("allin", "Mọi mục trong danh sách vào trong, kể cả sidebar; sửa spec sidebar", False),
               ("allout", "Mọi mục giữ ngoài, tăng khoảng giữa mục lên 4, menu cao thêm", False)]),
    dict(id="tc15", grp="Vòng focus", title="Khi nào hiện: focus-visible",
         why=f"Bấm chuột mà hiện vòng là nhiễu trên màn điều vận bấm liên tục. Untitled dùng <code>focus-visible</code> {U_FV} dòng và <code>isFocusVisible</code> {U_IFV} dòng. Bên mình các trang <code>_work</code> chủ yếu dùng class tĩnh <code>.is-focus</code> để vẽ state: <mark>{len(FV_PAGES)}/{NP} trang có <code>:focus-visible</code></mark> ({', '.join(FV_PAGES) or 'không có'}). "
             "WCAG 2.4.7 chấp nhận: “User agents may optimize when the focus indicator is shown”. Ô nhập vẫn hiện khi bấm chuột vì trình duyệt coi là cần gõ. Xem thử có nút thật: bấm Tab để thử. Spec cần thêm câu cấm <code>outline:none</code> không có thay thế.",
         untitled=f"<code>focus-visible:outline-2</code>; container dùng <code>outline-hidden</code> {U_HIDDEN} dòng.",
         ours="State vẽ bằng <code>.is-focus</code>; <code>focus/width</code>. Chưa có luật khi nào hiện.",
         astryx="Button State có Focused, chưa phân biệt chuột và bàn phím.",
         pv=panes(pv_live, platforms=("web",)),
         opts=[("fv", "Mọi control dùng :focus-visible; cấm outline:none nếu không có vòng thay thế", True),
               ("f", "Dùng :focus: hiện cả khi bấm chuột, dễ làm, nhiều vòng thừa", False)]),
    dict(id="tc16", grp="Vòng focus", title="Ô nhập đang gõ: viền 2 vẽ bằng gì?",
         why=f"DEC-321 chốt “focus ô nhập viền 2px, không quầng mờ”. Cách đang làm ở {len(SHADOW_INPUT)} trang (<code>.ctl.is-focus</code>): đổi màu viền + <code>box-shadow:inset 0 0 0 1px</code>, chữ không nhích. DEC-327 lại ghi “Không dùng <code>box-shadow</code> để vẽ vòng”, nên <mark>hai câu đang chạm nhau</mark> nếu coi viền ô là vòng. "
             "Outline 2 vào trong đúng 2 cho ra <b>hình giống hệt</b>, chữ không nhích, không dùng bóng, trạng thái lỗi đổi một biến màu. Chế độ tương phản cao của Windows bỏ <code>box-shadow</code> (chưa kiểm lại lượt này).",
         untitled="<code>base/input</code>: <code>ring-2 ring-brand</code> khi <code>isFocusWithin</code>, tức là vẽ bằng bóng; họ không có câu cấm.",
         ours="<code>color/focus/ring</code>, <code>field/border-width</code> 1; <code>color/focus/ring_error</code> cho ô lỗi.",
         astryx="“viền 1px <code>{colors.accent}</code>” + inset ring 3px làm lớp phụ.",
         pv=panes(pv_input, platforms=("web", "mobile")),
         opts=[("outline", "Đổi sang outline 2 vào trong: nhìn như cũ, một cách vẽ với mọi vòng", True),
               ("shadow", "Giữ viền + bóng trong 1, ghi vào DEC-327 là ngoại lệ của ô nhập", False)]),
    dict(id="tc17", grp="Bàn phím", title="Thứ tự Tab",
         why=f"Web điều vận dày nút: bảng 50 dòng, mỗi dòng 2 nút (ví dụ để tính) là <mark>100 lần Tab</mark> mới qua được bảng. WCAG 2.4.3 cần thứ tự giữ nghĩa; không bắt mỗi nút một điểm dừng. Spec sidebar đã có mẫu: “Tab giữa 3 cột và chân hộp thoại, mũi tên lên xuống trong cột”. Bảng, menu, tab chưa có luật chung. <code>tabindex</code> dương chưa bị cấm ở đâu.",
         untitled="React Aria: <code>Table</code>, <code>Tabs</code>, <code>Menu</code> một điểm dừng, mũi tên đi bên trong (do <code>react-aria-components</code> lo, đọc từ tài liệu thư viện, chưa chạy thử).",
         ours="<code>design-system/components/application/sidebar-navigation.md</code> mục 2.1.1; chưa ở <code>design-system/foundations/touch-focus.md</code>.",
         astryx="Ô sửa trong bảng: “focus ô rồi Enter / F2”, “mỗi lúc chỉ 1 ô”.",
         pv=panes(pv_order, platforms=("web",), modes=("light", "dark")),
         opts=[("group", "Theo DOM, cấm tabindex dương; bảng, menu, tab là một điểm dừng, mũi tên đi trong đó", True),
               ("all", "Mọi phần bấm được đều một điểm dừng, đơn giản nhưng bảng dài rất mệt", False),
               ("spec", "Không ghi luật chung, từng spec tự quyết", False)]),
    dict(id="tc18", grp="Bàn phím", title="Thanh dính che focus (WCAG 2.4.11)",
         why=f"Thanh trên cao <code>header-nav/height</code> {n(px('header-nav/height'))} · {n(px('header-nav/height', 'mobile'))}, tiêu đề bảng dính, chân màn app có nút {n(H['lg'][1])}. Lùi Tab về dòng đang nằm dưới thanh thì <mark>dòng bị che hẳn</mark>: WCAG 2.4.11 AA “not entirely hidden due to author-created content”. "
             f"<code>scroll-padding-top</code> sửa được, số tính từ token: {n(px('header-nav/height'))} + {n(RING_OUT)} = {n(px('header-nav/height') + RING_OUT)} trên web (cộng cao tiêu đề bảng nếu có), không thêm token.",
         untitled_none="Không có scroll-padding toàn cục trong component; đã quét không thấy.",
         untitled="Không thấy luật cho thanh dính trong react đã quét; tài liệu Untitled không nói.",
         ours="<code>header-nav/height</code>; <code>design-system/components/application/header-navigation.md</code> chưa nói thanh dính và focus.",
         astryx="Chưa ghi.",
         pv=panes(pv_sticky, platforms=("web", "mobile"), modes=("light",)),
         opts=[("sp", "Khung cuộn đặt scroll-padding tính từ chiều cao thanh dính + 4; thêm vào luật khung trang", True),
               ("nosticky", "Không dính thanh trên: mất lối tới thao tác chung khi cuộn", False),
               ("skip", "Bỏ qua, chấp nhận lỗi AA ở màn cuộn", False)]),
    dict(id="tc19", grp="Bàn phím", title="Dialog, sheet: giữ focus trong khung",
         why="Luật đang rải theo spec và chưa khớp nhau: Tooltip app “focus vào tiêu đề, chỉ đi vòng trong sheet… đưa focus về Help icon”; hộp thoại xác nhận cũ trong <code>design/design.md</code> “focus mặc định ở Huỷ”; field-upload “giữ focus trong sheet, đóng xong focus về ô bấm”. "
             "WCAG 2.1.2 cấm bẫy không ra được, nên <mark>luôn phải có Esc hoặc nút đóng</mark>. Với thao tác không hoàn tác được của lái xe (kết thúc chuyến), focus vào nút an toàn tránh bấm Enter nhầm. Hộp hỏi nhập liệu thì focus vào ô đầu.",
         untitled="<code>application/modals/modal.tsx</code>, <code>application/slideout-menus/slideout-menu.tsx</code>: <code>react-aria-components</code> lo giữ, Esc, trả focus (chưa chạy thử); hộp có <code>outline-hidden</code>.",
         ours="Spec <code>design-system/components/base/tooltip.md</code>, <code>design-system/components/application/field-upload.md</code>; chưa có trong foundations.",
         astryx="“không đóng khi bấm ra ngoài; Esc = Huỷ; focus mặc định ở Huỷ”.",
         pv=panes(pv_trap, platforms=("web", "mobile")),
         opts=[("rule", "Một luật: vào nút an toàn hoặc ô đầu; Tab đi vòng; Esc đóng; trả focus về nút đã mở; lớp phủ không nhận focus", True),
               ("first", "Luôn vào phần bấm được đầu tiên: có thể rơi vào nút nguy hiểm", False),
               ("title", "Luôn vào tiêu đề như Tooltip app: đọc trước rồi mới chọn, thêm một lần Tab", False)]),
    dict(id="tc20", grp="Không chỉ bằng màu", title="Chỉ báo trạng thái không chỉ bằng màu",
         why=f"WCAG 1.4.1. <code>design-system/components/base/badge.md</code> đã cấm “badge chỉ có chấm hoặc icon”, nhưng cả DS chưa có câu chung. <mark>Dòng chọn <code>color/bg/selected</code> so với nền chỉ {SEL_VS_BG} Sáng, {SEL_VS_BG_D} Tối</mark>: không có ô chọn hoặc dấu thì gần như không thấy. "
             "Vòng focus đạt sẵn vì khác hình. Ô lỗi đi kèm câu chữ dưới ô. Sơ đồ lốp, marker bản đồ đã có chữ đi kèm (spec 1.4.1, DEC-329 giữ icon cảnh báo, lỗi).",
         untitled="<code>Badge</code> có <code>dot</code> kèm chữ; <code>Table</code> dòng chọn có ô chọn và <code>highlightSelectedRow</code>.",
         ours="<code>color/bg/selected</code>, Badge có Dot hoặc Icon Leading; bảng dùng Icon Leading (góp ý 29/10).",
         astryx="Badge màu + chữ; <code>Table</code> Selected tô nền, có checkbox đầu dòng.",
         pv=panes(pv_status, platforms=("web", "mobile")),
         opts=[("rule", "Ghi luật chung: mọi trạng thái có chữ hoặc dấu; dòng chọn phải có ô chọn hoặc dấu tick", True),
               ("dense", "Như trên, cho phép chấm không chữ trong bảng dày nếu có tooltip: bản chạm không đọc được", False)]),
]

SPEC = dict(
    slug="touch", short="phần Vùng chạm và focus",
    title="Foundations · Vùng chạm và focus — đủ luật chưa?",
    subtitle="Đối chiếu Untitled UI v8, WCAG 2.2, HIG · chọn từng mục · 02/11/2026",
    lead=(f"Trang này giúp quyết vùng chạm tối thiểu, cách bù, và vòng focus ở các chỗ khó. Kết luận chính: <mark>số {n(T_W)} · {n(T_A)} và vòng {n(F_W)} cách {n(F_O)} đều đứng được</mark>, thứ còn thiếu là <b>luật</b>: "
          f"phần bù đang viết tay, vòng vào trong chưa có, mobile web đang rơi vào sàn {n(T_W)}. <mark>Chưa sửa token nào.</mark>"),
    kpis=[(f"{_CNT[OK]} · {_CNT[DIFF]} · {_CNT[GAP]} · {_CNT[OWN]}", f"dòng đối chiếu: giống · khác có lý do · mình thiếu · chỉ mình có (tổng {len(CMP)})", ""),
          (f"{TOUCH_VAR}/{NP}", "trang component dùng var(--touch-min)", "bad"),
          (f"{HAND_N}", "chỗ bù vùng chạm viết số tay", "bad"),
          (f"{MIN_NS_TXT}:1", "tương phản vòng focus thấp nhất trên nền không đặc (cần 3:1)", "ok"),
          (f"{n(bu(IC['md'], T_A))}", f"phần bù mỗi phía của icon {n(IC['md'])} đứng riêng trên app, trước đây {n(bu(IC_OLD['md'], T_A))}", ""),
          (f"{len(ITEMS)}", "mục cần chọn", "")],
    tag_kind=None,
    screens=dict(
        title="Xem trên màn mẫu",
        intro=("“Sau khi đổi” vẽ thêm viền chấm xanh cho vùng chạm và vòng focus theo khuyến nghị: nút, icon bù tới <code>touch/min</code>; dòng bảng, mục menu vòng vào trong; nút chính vòng ngoài; ô nhập outline vào trong. Mọi số đọc từ biến thật, đổi Sáng Tối ngay trên màn. "
               "Màn mẫu web rộng 1280 vì khung kiểm của DEC-324 có 1280, bản vẽ thật là 1920."),
        proposal_css=(
            ".tp-f.tp-prop .tp-btn,.tp-f.tp-prop .tp-fg2{position:relative}"
            ".tp-f.tp-prop .tp-btn::after{content:\"\";position:absolute;left:0;right:0;top:50%;height:max(100%,var(--touch-min));transform:translateY(-50%);outline:1px dashed var(--color-utility-blue-500);pointer-events:none}"
            ".tp-f.tp-prop .tp-fg2::after{content:\"\";position:absolute;left:50%;top:50%;width:var(--touch-min);height:var(--touch-min);transform:translate(-50%,-50%);outline:1px dashed var(--color-utility-blue-500);pointer-events:none}"
            ".tp-f.tp-prop .tp-top .tp-btn{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}"
            ".tp-f.tp-prop .tp-tb tbody tr:first-child{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:calc(var(--focus-width) * -1)}"
            ".tp-f.tp-prop .tp-menu>span:first-child{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:calc(var(--focus-width) * -1)}"
            ".tp-f.tp-prop .tp-fld:first-child .tp-inp{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:calc(var(--focus-width) * -1)}"
            ".tp-f.tp-prop .tp-acts .tp-btn.sec,.tp-f.tp-prop .tp-sheet .tp-btn.sec{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}"
        ),
        logo_svg=None, gridov=False, overlay_html=None),
    sections=[
        dict(title="Bảng đối chiếu từng phần — Untitled ↔ mình",
             intro=f"Gồm token, 7 style focus (đã so ở trang Effect, DEC-327) và cách dùng thật trong <code>design/_ref/untitled-ui/react/components</code> (đếm lúc dựng, bỏ demo và story). Số Button tính từ lề và dòng chữ trong class, Untitled không ghi trực tiếp.",
             html=rows(["Untitled", "Số, cách dùng", "Mình", "Trạng thái"], CMP_ROWS)),
        dict(title="Số đo control ↔ sàn vùng chạm",
             intro=f"“Bù” là phần vô hình thêm mỗi phía tới sàn (Web {n(T_W)}, App {n(T_A)}). “Cách” là khoảng tối thiểu giữa hai phần tử cùng cỡ để hai vùng không chồng. Đọc từ <code>design-system/tokens.json</code> lúc dựng.",
             html=rows(["Phần tử", "Web", "Bù", "Cách", "App", "Bù", "Cách", "Ghi chú"], SIZE_ROWS)),
        dict(title="Chuẩn WCAG 2.2 đã đọc",
             intro="Câu trong ngoặc kép lấy từ w3.org/WAI/WCAG22/Understanding ngày 02/11/2026. HIG Accessibility đọc cùng ngày: “44x44 pt”, “about 12 points of padding”. Mức 48dp của Android và hành vi bàn phím ngoài trên app: <b>chưa kiểm</b> lượt này.",
             html=rows(["Tiêu chí", "Mức", "Yêu cầu", "Mình đang ở đâu"], WCAG)),
        dict(title="Đã chốt, không mở lại", intro="Các DEC đang hiệu lực mà trang chỉ áp, không hỏi lại. Chỗ nào mở lại thì mục đó ghi rõ \"Mở lại DEC-…:\".",
             html=rows(["DEC", "Đã chốt"], [
                 ["DEC-097", "Nút app cao 52 ở chân màn, 42 cho nút nhỏ và nút icon."],
                 ["DEC-138", "Vùng chạm app 44×44 cho mọi app, phần thiếu là vùng bấm vô hình."],
                 ["DEC-139", "Vòng focus 2px cách mép 2px màu than chì."],
                 ["DEC-170", "Viền ô đang gõ và vòng focus than chì cho mọi khách."],
                 ["DEC-198", "Nút Danger có vòng focus màu danger."],
                 ["DEC-321", "Focus ô nhập viền 2px, không quầng mờ."],
                 ["DEC-324", "Web vẽ 1920, kiểm 1280 và 1024, mobile web 393; app vẽ 393, thử 320."],
                 ["DEC-327", "Focus web dùng outline 2 cách 2, khe trong suốt, bỏ khe token, không thêm style focus, nút phẳng. Thay phần khe của DEC-241, DEC-258."],
                 ["DEC-328", "Bo một bộ: control 8, card 12, overlay 20."],
                 ["DEC-329", "Icon một bộ 12, 14, 16, 20; nét 2,25 từ 16 trở xuống; 3 luật nhãn."],
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", intro="Không thêm token nào. Việc chính là ghi luật vào <code>design-system/foundations/touch-focus.md</code> và đưa component về token.",
             html=rows(["Phần", "Web · App", "Việc"], SHARED)),
    ],
    items=ITEMS,
    final=("Khi bạn chốt: mình cập nhật <code>design-system/tokens.json</code> → sinh <code>design-system/tokens.css</code> + handoff → sửa <code>design-system/foundations/touch-focus.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>touch-focus = approved</b> "
           "(<code>ds-foundation-status.py set touch-focus approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). Việc riêng của trang: thêm lớp bù vùng chạm dùng chung, sửa <code>design-system/components/base/avatar.md</code>, <code>design-system/components/base/tooltip.md</code> và các trang <code>_work</code> còn gọi biến focus đã bỏ."),
    css=CSS,
    js=JS,
)
