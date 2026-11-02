#!/usr/bin/env python3
"""SPEC trang review Effect styles: lớp nổi, bóng, vòng focus, làm mờ nền. Dựng: python3 _scripts/foundation_review/build.py effect"""
import collections
import glob
import re

import kit
from kit import ROOT, cr, icon, panes, rows

OK, DIFF, GAP, OWN = "st-ok", "st-diff", "st-gap", "st-own"
LAB = {OK: "Giống", DIFF: "Khác có lý do", GAP: "Mình thiếu", OWN: "Chỉ mình có"}


def st(s, note=""):
    return f'<span class="{s}">{LAB[s]}</span>' + (f'<br><span class="small muted">{note}</span>' if note else "")


# ---------- đếm thật ----------
PAGES = sorted(glob.glob(str(ROOT / "design-system/components/_work/*/page.json")))
SPECS = sorted(glob.glob(str(ROOT / "design-system/components/base/*.md")) + glob.glob(str(ROOT / "design-system/components/application/*.md")))
page_txt = {p: open(p, encoding="utf-8").read() for p in PAGES}
spec_txt = "\n".join(open(p, encoding="utf-8").read() for p in SPECS)
css_use = collections.Counter()
for s in page_txt.values():
    css_use.update(re.findall(r"var\(--(elev-[123]|blur-\w+)\)", s))
spec_use = collections.Counter(re.findall(r"elev/[123]", spec_txt))
BLUR_IN_PAGES = sum(s.count("backdrop-filter") for s in page_txt.values())
BLUR_IN_SPECS = len(re.findall(r"blur/|backdrop", spec_txt))
FOCUS_OUTLINE = sum(1 for s in page_txt.values() if re.search(r"outline:[^;\"]{0,40}solid var\(--(color-focus-ring|focus-color)\)", s))
FOCUS_SHADOW = sum(1 for s in page_txt.values() if "0 0 0 2px var(--color-focus-gap),0 0 0 4px var(--color-focus-ring)" in s)

# ---------- bảng đối chiếu: trạng thái đếm thẳng từ dữ liệu, KPI không gõ tay ----------
SHADOW_ROWS = [
    ("<code>shadow-xs</code>", "0 1 2 · đen 5%", "n:27", "<code>elev/1</code> 0 1 2 · #101828 6%", st(DIFF, "cùng hình, đậm hơn 1%; DEC-125")),
    ("<code>shadow-sm</code>", "0 1 3 · 10% + 0 1 2 −1 · 10%", "n:2", "không có", st(GAP, "không ai cần: Untitled chỉ dùng ở tab, công tắc")),
    ("<code>shadow-md</code>", "0 4 6 −1 · 10% + 0 2 4 −2 · 6%", "n:3", "<code>elev/2</code> 0 4 12 · 10% + 0 1 3 · 6%", st(DIFF, "cùng độ cao 4, nhoè rộng hơn; DEC-137")),
    ("<code>shadow-lg</code>", "0 12 16 −4 · 8% + 0 4 6 −2 · 3% + 0 2 2 −1 · 4%", "n:9", "không có bậc này; vai menu do <code>elev/2</code> gánh", st(GAP, "Untitled đặt menu, popover ở bậc này")),
    ("<code>shadow-xl</code>", "0 20 24 −4 · 8% + 0 8 8 −4 · 3% + 0 3 3 −1.5 · 4%", "n:5", "<code>elev/3</code> 0 16 40 · 16% + 0 4 12 · 10%", st(DIFF, "cùng vai dialog, sheet; mình đậm và rộng hơn")),
    ("<code>shadow-2xl</code>", "0 24 48 −12 · 18% + 0 4 4 −2 · 4%", "n:1", "không có", st(GAP, "Untitled chỉ dùng ở ảnh hồ sơ")),
    ("<code>shadow-3xl</code>", "0 32 64 −12 · 14% + 0 5 5 −2.5 · 4%", "n:0", "không có", st(GAP, "không component Untitled nào dùng")),
    ("<code>shadow-xs-skeuomorphic</code>", "viền trong 1px 18% + nét −2px 5% + xs", "n:11", "không có, nút phẳng", st(GAP, "mục ef12")),
    ("không có", "—", "n:—", "<code>elev/0</code> phẳng", st(OWN, "ô nhập, khối phụ trong thẻ")),
    ("<code>ring-secondary_alt</code> ghi tay ở từng component", "viền 1px đen 10%", "n:—", "<code>elev/1-border</code>, <code>elev/2-border</code> → <code>color/border/secondary</code>", st(OWN, "viền đi cùng bậc, không ghi tay")),
]
LAYER_ROWS = [
    ("shadow-xs", 1, 0, 1, 2, "0", "shadow-xs", "5%"), ("shadow-sm", 1, 0, 1, 2, "−1", "shadow-sm_02", "10%"), ("shadow-sm", 2, 0, 1, 3, "0", "shadow-sm_01", "10%"),
    ("shadow-md", 1, 0, 2, 4, "−2", "shadow-md_02", "6%"), ("shadow-md", 2, 0, 4, 6, "−1", "shadow-md_01", "10%"),
    ("shadow-lg", 1, 0, 2, 2, "−1", "shadow-lg_03", "4%"), ("shadow-lg", 2, 0, 4, 6, "−2", "shadow-lg_02", "3%"), ("shadow-lg", 3, 0, 12, 16, "−4", "shadow-lg_01", "8%"),
    ("shadow-xl", 1, 0, 3, 3, "−1.5", "shadow-xl_03", "4%"), ("shadow-xl", 2, 0, 8, 8, "−4", "shadow-xl_02", "3%"), ("shadow-xl", 3, 0, 20, 24, "−4", "shadow-xl_01", "8%"),
    ("shadow-2xl", 1, 0, 4, 4, "−2", "shadow-2xl_02", "4%"), ("shadow-2xl", 2, 0, 24, 48, "−12", "shadow-2xl_01", "18%"),
    ("shadow-3xl", 1, 0, 5, 5, "−2.5", "shadow-3xl_02", "4%"), ("shadow-3xl", 2, 0, 32, 64, "−12", "shadow-3xl_01", "14%"),
]
OUR_LAYERS = [
    ("elev/1", 1, 0, 1, 2, "0", "color/shadow/sm", "#101828 6%", "#000 40%"),
    ("elev/2", 1, 0, 4, 12, "0", "color/shadow/md", "#101828 10%", "#000 50%"),
    ("elev/2", 2, 0, 1, 3, "0", "color/shadow/md-soft", "#101828 6%", "#000 40%"),
    ("elev/3", 1, 0, 16, 40, "0", "color/shadow/lg", "#101828 16%", "#000 60%"),
    ("elev/3", 2, 0, 4, 12, "0", "color/shadow/md", "#101828 10%", "#000 50%"),
]
FOCUS_ROWS = [
    ("<code>focus-ring</code>", "vòng 4 + khe 2 · brand-500 #9E77ED", "<code>color/focus/ring</code> than chì #262626, Tối #E5E5E5", st(DIFF, "DEC-170: một màu cho mọi khách, không trùng sắc với lỗi")),
    ("<code>focus-ring-error</code>", "vòng 4 + khe 2 · red-500 #EF4444", "<code>color/focus/ring_error</code> #B42318, Tối #FFA19C", st(DIFF, "DEC-198, DEC-320: đỏ đậm hơn")),
    ("<code>focus-ring-shadow-xs</code>", "vòng + khe + xs", "vòng là lớp riêng, bóng của thẻ giữ nguyên", st(DIFF, "không cần style gộp")),
    ("<code>focus-ring-shadow-sm</code>", "vòng + khe + sm (lớp 2 spread 0, lệch nội bộ so với shadow-sm)", "như trên", st(DIFF, "không cần style gộp")),
    ("<code>focus-ring-error-shadow-xs</code>", "vòng đỏ + khe + xs", "như trên, màu <code>color/focus/ring_error</code>", st(DIFF, "không cần style gộp")),
    ("<code>focus-ring-shadow-xs-skeuomorphic</code>", "vòng + khe + xs + 2 lớp trong", "không có", st(GAP, "đi theo mục ef12")),
    ("<code>focus-ring-error-shadow-xs-skeuomorphic</code>", "như trên, vòng đỏ", "không có", st(GAP, "đi theo mục ef12")),
    ("code: <code>outline-2</code>", "dày 2, 51 chỗ", "<code>focus/width</code> 2", st(OK)),
    ("code: <code>outline-offset-2</code>", "cách 2, 76 chỗ", "<code>focus/offset</code> 2", st(OK)),
    ("code ô nhập: <code>ring-2 ring-brand</code>", "viền 2px, không quầng, 11 chỗ", "viền 2px <code>color/focus/ring</code> (DEC-321)", st(DIFF, "cùng cách, khác màu")),
    ("không có", "khe trong suốt bằng outline", "<code>color/focus/gap</code> = nền trang", st(OWN, "DEC-258; mục ef08")),
    ("không có", "—", "<code>--focus-color</code> trỏ <code>color/focus/ring</code>", st(OWN, "trùng, chỉ badge-avatar dùng; mục ef07")),
]
BLUR_ROWS = [
    ("<code>backdrop-blur-sm</code>", "n:8", "n:0", "<code>blur/sm</code> 8", st(OK, "khác tên")),
    ("<code>backdrop-blur-md</code>", "n:16", "n:1", "<code>blur/md</code> 16", st(OK, "khác tên")),
    ("<code>backdrop-blur-lg</code>", "n:24", "n:0", "<code>blur/lg</code> 24", st(OK, "khác tên")),
    ("<code>backdrop-blur-xl</code>", "n:40", "n:0", "<code>blur/xl</code> 40", st(OK, "khác tên; mục 8.1 ghi không dùng")),
    ("<code>bg-overlay/70</code> + <code>backdrop-blur-[6px]</code> ở modal", "n:6", "n:4", "<code>color/bg/overlay</code> 50%, chưa có blur", st(DIFF, "mục ef09")),
]
OTHER_ROWS = [
    ("<code>Avatar inner shadow</code>, <code>Avatar icon</code>", "chỉ có tên trong panel Figma, ref chưa đọc số", "không có", st(GAP, "ref thiếu số; thuộc Avatar, không thuộc foundation")),
    ("5 style Portfolio mockups", "ref chưa đọc số; bản code dùng tên khác <code>shadow-modern-mockup-*</code>", "không có", st(GAP, "bóng cho ảnh marketing, không lấy (tinh thần DEC-320)")),
]
_all = [r[-1] for r in SHADOW_ROWS + FOCUS_ROWS + BLUR_ROWS + OTHER_ROWS]
CNT = {s: sum(1 for c in _all if f'class="{s}"' in c) for s in LAB}
TOTAL = len(_all)
# Mỗi lớp Untitled chỉ biết Tối trong code: theme.css không ghi đè bóng ở Tối.
theme = (ROOT / "design/_ref/untitled-ui/raw/theme.css").read_text()
DARK_START = theme.find(".dark-mode")
DARK_OVERRIDE = len(re.findall(r"--shadow-\w+\s*:", theme[DARK_START:])) if DARK_START >= 0 else -1

# ---------- atom xem thử ----------
BTN = lambda x, c="", st_="": f'<span class="tp-btn {c}" style="{st_}"><span class="type-label">{x}</span></span>'
BEHIND = ('<div class="ef-behind">'
          '<div class="ef-line"><span class="type-code">LVT-2026-0412</span><span class="type-body">Cát Lái → KCN Long Hậu</span><span class="tp-chip tp-b">Đang chạy</span></div>'
          '<div class="ef-line"><span class="type-code">LVT-2026-0411</span><span class="type-body">ICD Phước Long → Bình Dương</span><span class="tp-chip tp-g">Hoàn thành</span></div>'
          '<div class="ef-line"><span class="type-code">LVT-2026-0409</span><span class="type-body">Hiệp Phước → Đồng Nai</span><span class="tp-chip tp-y">Chờ duyệt</span></div>'
          '<div class="ef-line"><span class="type-code">LVT-2026-0407</span><span class="type-body">Cát Lái → Tân Vạn</span><span class="tp-chip tp-g">Hoàn thành</span></div>'
          '<div class="ef-line"><span class="type-code">LVT-2026-0403</span><span class="type-body">Phú Hữu → Sóng Thần</span><span class="tp-chip tp-b">Đang chạy</span></div></div>')
cap = lambda x: f'<div class="ef-cap">{x}</div>'
tile = lambda name, sub, style="": (f'<div class="ef-tile" style="{style}"><div class="type-label">{name}</div><div class="type-caption tp-sub">{sub}</div></div>')
elevs = lambda n: f"box-shadow:var(--elev-{n})"
DLG = ('<div class="tp-dlg ef-dlg" style="{s}"><div class="type-title-3">Duyệt lệnh LVT-2026-0412?</div>'
       '<div class="type-body tp-sub">Lệnh gửi tới tài xế Nguyễn Văn Hoà ngay sau khi duyệt.</div></div>')
scene = lambda inner, scrim="", label="": (cap(label) if label else "") + f'<div class="ef-scene">{BEHIND}<div class="tp-scrim c" style="{scrim}">{inner}</div></div>'
SCRIM35 = "background:color-mix(in srgb,var(--neutral-950) 35%,transparent);backdrop-filter:blur(var(--blur-lg))"
SCRIM70 = "background:color-mix(in srgb,var(--neutral-950) 70%,transparent);backdrop-filter:blur(6px)"
U_XS = "0 1px 2px rgba(0,0,0,.05)"
U_MD = "0 4px 6px -1px rgba(0,0,0,.1),0 2px 4px -2px rgba(0,0,0,.06)"
U_LG = "0 12px 16px -4px rgba(0,0,0,.08),0 4px 6px -2px rgba(0,0,0,.03),0 2px 2px -1px rgba(0,0,0,.04)"
U_XL = "0 20px 24px -4px rgba(0,0,0,.08),0 8px 8px -4px rgba(0,0,0,.03),0 3px 3px -1.5px rgba(0,0,0,.04)"
U_SKEU = "inset 0 0 0 1px rgba(0,0,0,.18),inset 0 -2px 0 0 rgba(0,0,0,.05),0 1px 2px rgba(0,0,0,.05)"
TOAST = lambda m="": (f'<div class="ef-toast" {m}><span class="ef-ok">{icon("circle-check")}</span><div style="min-width:0"><div class="type-label">Đã duyệt lệnh LVT-2026-0412</div>'
                      '<div class="type-caption tp-sub">Tài xế Nguyễn Văn Hoà đã nhận thông báo lúc 14:32.</div></div></div>')


def focus_states(mode=None, plat=None):
    return (f'<div class="ef-focus"><div class="ef-fgrp"><span class="tp-btn ef-ring"><span class="type-label">Duyệt lệnh</span></span>'
            f'<span class="tp-btn sec ef-ring"><span class="type-label">Để sau</span></span><span class="tp-btn ef-danger ef-ring ef-ring-err"><span class="type-label">Huỷ lệnh</span></span></div>'
            f'<div class="tp-fld"><span class="type-label">Mã container</span><div class="tp-inp ef-inp-f"><span class="type-body">TCLU 482915-3</span></div></div>'
            f'<div class="tp-fld"><span class="type-label">Cước dự kiến</span><div class="tp-inp ef-inp-fe"><span class="type-body tp-num">12.500</span></div><div class="type-hint tp-err">Cước thấp hơn định mức của tuyến.</div></div></div>')


# ---------- màn thật: thêm toast, focus; hộp xác nhận có dữ liệu phía sau ----------
def overlay(body):
    a = '<div class="tp-f tp-prop tp-webc" data-platform="web"><div class="tp-scrim c">'
    b = f'<div class="tp-f tp-prop tp-webc" data-platform="web"><div class="tp-main">{BEHIND}{BEHIND}</div><div class="tp-scrim c">'
    assert a in body
    body = body.replace(a, b)
    extra = (f'<div class="tp-h">Toast <small>· web góc dưới phải, app đỉnh màn</small></div><div class="tp-scroll"><div class="tp-row">'
             f'<div class="tp-f tp-prop tp-webs" data-platform="web" style="min-height:300px"><div class="tp-main"><div class="type-title-1">Lệnh vận tải</div><div class="tp-card">{BEHIND}</div></div>{TOAST("style=position:absolute;right:24px;bottom:24px;width:400px")}</div>'
             f'<div class="tp-f tp-prop tp-app" data-platform="mobile" style="min-height:300px"><div class="tp-pad"><div class="tp-card">{BEHIND}</div></div>{TOAST("style=position:absolute;left:16px;right:16px;top:16px")}</div></div></div>'
             f'<div class="tp-h">Trạng thái focus <small>· nút chính, nút phụ, nút Danger, ô nhập đang gõ, ô nhập lỗi</small></div><div class="tp-scroll"><div class="tp-row">'
             f'<div class="tp-f tp-prop tp-webs" data-platform="web" style="min-height:0"><div class="tp-main">{focus_states()}</div></div>'
             f'<div class="tp-f tp-prop tp-app" data-platform="mobile" style="min-height:0"><div class="tp-pad">{focus_states()}</div></div></div></div>')
    return body + extra


# ---------- xem thử từng mục ----------
def pv_ladder(m, p):
    return (cap("Của mình") + '<div class="ef-tiles">' + tile("elev/1", "0 1 2", elevs(1)) + tile("elev/2", "0 4 12 + 0 1 3", elevs(2)) + tile("elev/3", "0 16 40 + 0 4 12", elevs(3)) + "</div>"
            + cap("Untitled, cùng tên nếu đặt theo họ") + '<div class="ef-tiles">' + tile("shadow-xs", "0 1 2", f"box-shadow:{U_XS}") + tile("shadow-md", "0 4 6 −1 + 0 2 4 −2", f"box-shadow:{U_MD}") + tile("shadow-xl", "0 20 24 −4 + 0 8 8 −4 + 0 3 3 −1.5", f"box-shadow:{U_XL}") + "</div>")


def pv_values(m, p):
    return (cap("Của mình (DEC-137)") + '<div class="ef-tiles">' + tile("Thẻ", "elev/1", elevs(1)) + tile("Menu", "elev/2", elevs(2)) + tile("Dialog", "elev/3", elevs(3)) + "</div>"
            + cap("Số Untitled") + '<div class="ef-tiles">' + tile("Thẻ", "shadow-xs", f"box-shadow:{U_XS}") + tile("Menu", "shadow-lg", f"box-shadow:{U_LG}") + tile("Dialog", "shadow-xl", f"box-shadow:{U_XL}") + "</div>")


def pv_color(m, p):
    if m == "dark":
        return (cap("Tối không đổi: cả hai cách đều là đen") + '<div class="ef-tiles">' + tile("Thẻ", "#000 40%", elevs(1)) + tile("Menu", "#000 50% + 40%", elevs(2)) + tile("Dialog", "#000 60% + 50%", elevs(3)) + "</div>")
    return (cap("#101828 đang dùng") + '<div class="ef-tiles">' + tile("Thẻ", "6%", elevs(1)) + tile("Menu", "10% + 6%", elevs(2)) + tile("Dialog", "16% + 10%", elevs(3)) + "</div>"
            + cap("Đen, cùng độ mờ") + '<div class="ef-tiles">' + tile("Thẻ", "6%", "box-shadow:0 1px 2px rgba(0,0,0,.06)") + tile("Menu", "10% + 6%", "box-shadow:0 4px 12px rgba(0,0,0,.10),0 1px 3px rgba(0,0,0,.06)") + tile("Dialog", "16% + 10%", "box-shadow:0 16px 40px rgba(0,0,0,.16),0 4px 12px rgba(0,0,0,.10)") + "</div>")


def pv_border(m, p):
    return (scene(DLG.format(s=""), "", "Hiện tại: <code>elev/3</code> không viền")
            + scene(DLG.format(s="border:1px solid var(--ef-elev3b)"), "", "Thêm <code>elev/3-border</code>: Tối có viền, Sáng không"))


def pv_card_dark(m, p):
    return (cap("Bóng + viền (đang dùng)") + f'<div class="tp-card">{kit.t("title-3", "Cát Lái → KCN Long Hậu")}<div class="type-body tp-sub">51C-482.15 · Nguyễn Văn Hoà</div></div>'
            + cap("Chỉ viền") + f'<div class="tp-card" style="box-shadow:none">{kit.t("title-3", "Cát Lái → KCN Long Hậu")}<div class="type-body tp-sub">51C-482.15 · Nguyễn Văn Hoà</div></div>')


MENU = lambda n: (f'<div class="tp-menu" style="position:static;width:auto;flex:1;min-width:0;box-shadow:var(--elev-{n})"><span>{icon("pencil")}<span class="type-body">Sửa lệnh</span></span><span>{icon("copy")}<span class="type-body">Nhân bản</span></span><span class="tp-err">{icon("trash-2")}<span class="type-body">Huỷ lệnh</span></span></div>')


def pv_menu(m, p):
    return f'<div class="ef-duo"><div>{cap("elev/2 theo DEC-137")}{MENU(2)}</div><div>{cap("elev/3 như spec đang ghi")}{MENU(3)}</div></div>'


def pv_focus(m, p):
    return (focus_states() + '<div class="small" style="margin-top:8px">Vòng trên khe ' + cr("color/focus/ring", "color/focus/gap", 3)
            + ' · Vòng Danger trên khe ' + cr("color/focus/ring_error", "color/focus/gap", 3) + ' · Vòng trên nền phụ ' + cr("color/focus/ring", "color/bg/secondary", 3) + "</div>")


def pv_gap(m, p):
    def surf(bg, name, tok):
        return (f'<div class="ef-surf" style="background:var({tok})"><div class="type-caption tp-sub">{name}</div><div class="ef-fgrp">'
                f'<span class="tp-btn sec ef-boxring"><span class="type-label">Khe tô màu</span></span><span class="tp-btn sec ef-ring"><span class="type-label">Khe trong suốt</span></span></div></div>')
    return surf(0, "Nền trang <code>color/bg/primary</code>", "--color-bg-primary") + surf(0, "Khối phụ <code>color/bg/secondary</code>", "--color-bg-secondary") + surf(0, "Dòng đang chọn <code>color/bg/selected</code>", "--color-bg-selected") + surf(0, "Cảnh báo <code>color/bg/warning/primary</code>", "--color-bg-warning-primary")


def pv_scrim(m, p):
    return (scene(DLG.format(s=""), "", "Hiện tại: <code>color/bg/overlay</code> 50%, không mờ")
            + scene(DLG.format(s=""), SCRIM35, "Mục 8.1: scrim 35% + <code>blur/lg</code> 24")
            + scene(DLG.format(s=""), SCRIM70, "Untitled: 70% + mờ 6"))


def pv_bar(m, p):
    bar = lambda s, txt: f'<div class="ef-scene ef-short">{BEHIND}<div class="ef-bar" style="{s}"><span class="type-label">{txt}</span></div></div>'
    return (cap("Mục 8.1 hiện tại: nền trắng 70%") + bar("background:var(--alpha-white-70);backdrop-filter:blur(var(--blur-sm))", "Lệnh vận tải · 128 lệnh")
            + cap("Đề xuất: <code>color/bg/primary_blur</code> 70%") + bar("background:color-mix(in srgb,var(--color-bg-primary) 70%,transparent);backdrop-filter:blur(var(--blur-sm))", "Lệnh vận tải · 128 lệnh")
            + cap("Thanh đặc, không mờ") + bar("background:var(--color-bg-primary);border-bottom:1px solid var(--color-border-secondary)", "Lệnh vận tải · 128 lệnh"))


def pv_blur(m, p):
    one = lambda n, px: f'<div class="ef-scene ef-short">{BEHIND}<div class="ef-bar" style="inset:0;height:auto;background:color-mix(in srgb,var(--color-bg-primary) 60%,transparent);backdrop-filter:blur(var(--blur-{n}))"><span class="type-label">blur/{n} · {px}</span></div></div>'
    return '<div class="ef-tiles ef-t2">' + one("sm", 8) + one("md", 16) + one("lg", 24) + one("xl", 40) + "</div>"


def pv_skeu(m, p):
    fl = f'<div class="ef-fgrp">{BTN("Duyệt lệnh")}{BTN("Để sau", "sec")}</div>'
    sk = f'<div class="ef-fgrp">{BTN("Duyệt lệnh", "", "box-shadow:" + U_SKEU)}<span class="tp-btn sec" style="box-shadow:inset 0 0 0 1px var(--color-border-primary),inset 0 -2px 0 0 rgba(0,0,0,.05),0 1px 2px rgba(0,0,0,.05)"><span class="type-label">Để sau</span></span></div>'
    return cap("Phẳng (đang dùng)") + fl + cap("Có <code>shadow-xs-skeuomorphic</code>") + sk


CSS = """
/* lớp nổi đọc lại màu theo từng khung data-theme: tokens.css khai ở :root nên khung Tối lồng trong trang Sáng nhận màu Sáng (xem báo cáo) */
[data-theme]{--elev-1:0px 1px 2px 0px var(--color-shadow-sm);--elev-1-border:var(--color-border-secondary);--elev-2:0px 4px 12px 0px var(--color-shadow-md),0px 1px 3px 0px var(--color-shadow-md-soft);--elev-2-border:var(--color-border-secondary);--elev-3:0px 16px 40px 0px var(--color-shadow-lg),0px 4px 12px 0px var(--color-shadow-md);--focus-color:var(--color-focus-ring);--ef-elev3b:transparent}
[data-theme=dark]{--ef-elev3b:var(--color-border-secondary)}
/* kit: nhãn số đo đặt position:relative lên mọi phần tử có data-tag, làm menu, scrim rời chỗ; giữ lại absolute */
[data-tags="on"] .tp-menu,[data-tags="on"] .tp-scrim{position:absolute}
.ef-cap{font:600 11.5px/16px Inter,sans-serif;color:var(--color-text-tertiary);margin:10px 0 6px}.ef-cap:first-of-type{margin-top:0}.ef-cap code,.ef-surf code{font-size:11px;background:none;padding:0;color:inherit}
.ef-tiles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-lg);padding:var(--space-sm) var(--space-xs) var(--space-xl)}.ef-t4{grid-template-columns:repeat(4,minmax(0,1fr))}.ef-t2{grid-template-columns:repeat(2,minmax(0,1fr));padding:0}
.ef-tile{background:var(--color-bg-primary_alt);border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);padding:var(--space-lg);min-height:72px;min-width:0;overflow-wrap:anywhere}
.ef-scene{position:relative;overflow:hidden;min-height:176px;border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);background:var(--color-bg-primary)}.ef-short{min-height:96px;max-height:112px}
.ef-behind{padding:var(--space-md) var(--space-lg);display:grid;gap:var(--space-xs)}.ef-line{display:flex;align-items:center;gap:var(--space-md);min-width:0;white-space:nowrap}.ef-line .type-body{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis}
.ef-dlg{width:auto;max-width:84%;padding:var(--space-xl);gap:var(--space-sm)}
.ef-duo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-xl);padding-bottom:var(--space-3xl)}
.ef-bar{position:absolute;left:0;right:0;top:0;height:40px;display:flex;align-items:center;justify-content:center;padding:0 var(--space-lg)}
.ef-toast{display:flex;gap:var(--space-md);align-items:flex-start;background:var(--color-bg-primary_alt);border:1px solid var(--color-border-secondary);border-radius:var(--radius-xl);padding:var(--space-lg);box-shadow:var(--elev-3);z-index:2}.ef-ok{color:var(--color-fg-success-primary,var(--color-utility-green-700))}
.ef-focus{display:grid;gap:var(--space-xl);padding:var(--space-xs)}.ef-fgrp{display:flex;flex-wrap:wrap;gap:var(--space-xl);align-items:center;padding:var(--space-xs)}
.ef-ring{outline:var(--focus-width) solid var(--color-focus-ring);outline-offset:var(--focus-offset)}.ef-ring-err{outline-color:var(--color-focus-ring_error)}
.ef-danger{background:var(--color-bg-error-solid);color:var(--white)}
.tp-btn.ef-boxring{box-shadow:inset 0 0 0 1px var(--color-border-primary),0 0 0 2px var(--color-focus-gap),0 0 0 4px var(--color-focus-ring)}
.tp-inp.ef-inp-f{border-color:var(--color-focus-ring);box-shadow:inset 0 0 0 1px var(--color-focus-ring)}.tp-inp.ef-inp-fe{border-color:var(--color-focus-ring_error);box-shadow:inset 0 0 0 1px var(--color-focus-ring_error)}
.ef-surf{padding:var(--space-lg);border-radius:var(--radius-md);margin-bottom:var(--space-md)}.ef-surf .type-caption{margin-bottom:var(--space-md)}
.ef-ladder{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:10px 0}
@media(max-width:820px){.ef-tiles,.ef-t4,.ef-duo,.ef-ladder{grid-template-columns:minmax(0,1fr)}}
"""

layers_u = rows(["Style", "Lớp", "x", "y", "blur", "spread", "Biến màu", "Sáng", "Tối (Figma)", "Tối (code)"],
                [(f"<code>{a}</code>", f"n:{b}", f"n:{c}", f"n:{d}", f"n:{e}", f"n:{f}", f"<code>{g}</code>", f"đen {h}", '<span class="st-gap">? chưa đọc</span>', f"đen {h}") for a, b, c, d, e, f, g, h in LAYER_ROWS])
layers_o = rows(["Style", "Lớp", "x", "y", "blur", "spread", "Biến màu", "Sáng", "Tối"],
                [(f"<code>{a}</code>", f"n:{b}", f"n:{c}", f"n:{d}", f"n:{e}", f"n:{f}", f"<code>{g}</code>", h, i) for a, b, c, d, e, f, g, h, i in OUR_LAYERS])
skeu_tbl = rows(["Lớp của nút Untitled", "Số đo", "Biến", "Sáng", "Tối"],
                [("Viền trong", "0 0 0 1 inset", "<code>shadow-skeumorphic-inner-border</code>", "đen 18%", '<span class="st-gap">? chưa đọc</span>'),
                 ("Nét đáy trong", "0 −2 0 0 inset", "<code>shadow-skeumorphic-inner</code>", "đen 5%", '<span class="st-gap">? chưa đọc</span>'),
                 ("Bóng ngoài", "0 1 2 0", "<code>shadow-xs</code>", "đen 5%", '<span class="st-gap">? chưa đọc</span>')])

SPEC = dict(
    slug="effect", short="phần Effect styles",
    title="Foundations · Effect styles — lớp nổi, bóng, vòng focus, làm mờ nền",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
    lead=(f"Trang này giúp quyết <b>tên, số đo và cách áp</b> của bóng, vòng focus, làm mờ nền. Kết luận chính: <mark>hình học vòng focus đã trùng Untitled</mark>, ba bậc bóng giữ được, "
          f"còn <b>làm mờ nền ghi trong <code>design-system/foundations/effect-styles.md</code> chưa component nào áp</b>. Trang chỉ đề xuất, <mark>chưa sửa token nào</mark>."),
    kpis=[(f"{CNT[OK]}/{TOTAL}", "dòng đối chiếu giống Untitled", "ok"),
          (f"{CNT[DIFF]}", "dòng khác có lý do", ""),
          (f"{CNT[GAP]}", "dòng mình thiếu, đa số chủ ý không lấy", ""),
          (f"{CNT[OWN]}", "dòng chỉ mình có", ""),
          (f"{BLUR_IN_PAGES}", "trang component có áp làm mờ nền", "bad"),
          ("1", "lỗi tokens.css: khung Tối nhận bóng Sáng", "bad")],
    tag_kind="effect",
    screens=dict(
        intro=("Bộ màn mẫu đọc <code>--elev-*</code> thật. <b>Sau khi đổi</b> áp ba thứ: <code>elev/3</code> có viền ở Tối, scrim 35% + <code>blur/lg</code> theo mục 8.1, dialog đè lên dữ liệu thật. "
               "Bật <b>Nhãn số đo</b> để đọc số lớp bóng và độ mờ trực tiếp từ trình duyệt. Chuyển Sáng/Tối để so."),
        proposal_css=(".tp-f.tp-prop{--elev-3-border:transparent;--color-bg-overlay:color-mix(in srgb,var(--neutral-950) 35%,transparent)}"
                      "[data-theme=dark] .tp-f.tp-prop{--elev-3-border:var(--color-border-secondary)}"
                      ".tp-f.tp-prop .tp-dlg{border:1px solid var(--elev-3-border)}"
                      ".tp-f.tp-prop .tp-scrim{backdrop-filter:blur(var(--blur-lg))}"),
        overlay_html=overlay),
    sections=[
        dict(title="Bảng đối chiếu từng bậc bóng — Untitled ↔ mình",
             intro=("Số Untitled từ <code>design/_ref/untitled-ui/05-effects.md</code> và <code>design/_ref/untitled-ui/raw/theme.css</code>. Cột “chỗ dùng” đếm class trong <code>design/_ref/untitled-ui/react</code>, bỏ minh hoạ và demo."),
             html=rows(["Untitled", "Lớp (x y blur spread · độ mờ)", "Chỗ dùng", "Mình", "Trạng thái"], SHADOW_ROWS)),
        dict(title="Từng lớp bóng Untitled: 15 lớp của 7 style",
             intro=(f"Ref ghi <code>?</code> cho toàn bộ giá trị Tối của Figma, nên <b>Tối theo Figma là thiếu</b>. Trong code, <code>design/_ref/untitled-ui/raw/theme.css</code> có {DARK_OVERRIDE} chỗ ghi đè <code>--shadow-*</code> ở Tối, tức giữ đen độ mờ như Sáng."),
             html=layers_u),
        dict(title="Lớp bóng của mình, màu đổi theo Sáng/Tối (DEC-258)",
             intro="Năm lớp, bốn biến màu <code>color/shadow/*</code>. Nguồn <code>design-system/tokens.json</code>, khớp <code>design-system/foundations/effect-styles.md</code>.",
             html=layers_o),
        dict(title="Lớp nổi của nút Untitled (skeuomorphic)",
             intro="Tên biến trong Figma viết thiếu chữ o, bản code v8 đã sửa thành <code>shadow-skeuomorphic</code>. Bản code không ghi đè ở Tối.",
             html=skeu_tbl),
        dict(title="Bảng đối chiếu vòng focus — Untitled ↔ mình",
             intro=("Style Figma của Untitled tả <b>vòng 4 đè khe 2</b>, nhìn ra là khe 2 + vòng 2. Code Untitled dùng <code>outline-2</code> + <code>outline-offset-2</code>. "
                    "Của mình <code>focus/width</code> 2 + <code>focus/offset</code> 2, <mark>cùng hình học</mark>; Web và App cùng số nên không có gì cần gộp."),
             html=rows(["Untitled", "Mô tả", "Mình", "Trạng thái"], FOCUS_ROWS)),
        dict(title="Bảng đối chiếu làm mờ nền và lớp phủ — Untitled ↔ mình",
             intro=("Bốn bậc Figma <code>backdrop-blur-*</code> không có trong <code>design/_ref/untitled-ui/raw/theme.css</code>. Code Untitled gần như không dùng: modal dùng mờ 6 ghi tay, slide-out không mờ. "
                    "<code>bg-overlay</code> của Untitled: Sáng neutral-950, Tối neutral-800, dùng ở 70%."),
             html=rows(["Untitled", "px / %", "Chỗ dùng", "Mình", "Trạng thái"], BLUR_ROWS)),
        dict(title="Phần Untitled còn lại", html=rows(["Untitled", "Giá trị", "Mình", "Trạng thái"], OTHER_ROWS)),
        dict(title="Số dùng thật trong component của mình",
             intro=f"Đếm trên {len(PAGES)} trang <code>design-system/components/_work/*/page.json</code> và {len(SPECS)} spec <code>components/{{base,application}}/*.md</code>.",
             html=rows(["Token", "CSS trang component", "Spec viết", "Ghi chú"], [
                 ("<code>elev/1</code>", f"n:{css_use['elev-1']}", f"n:{spec_use['elev/1']}", "Thẻ phạm vi của Sidebar, Tooltip (DEC-301)"),
                 ("<code>elev/2</code>", f"n:{css_use['elev-2']}", f"n:{spec_use['elev/2']}", "<b>Không spec nào viết</b>, CSS menu dùng; mục ef05"),
                 ("<code>elev/3</code>", f"n:{css_use['elev-3']}", f"n:{spec_use['elev/3']}", "Có ba chỗ là menu, trái DEC-137"),
                 ("Trục Elevation của thẻ", "n:0", "n:0", "<code>Base / Card</code> đã xoá theo DEC-312; không component nào đặt Med hay High, nên trang không hỏi trục này"),
                 ("<code>blur/sm</code> … <code>blur/xl</code>", f"n:{sum(v for k, v in css_use.items() if k.startswith('blur'))}", f"n:{BLUR_IN_SPECS}", "Chưa component nào áp"),
                 ("<code>color/focus/gap</code> (vòng bằng box-shadow)", f"n:{FOCUS_SHADOW} trang", "—", "Ô nhập, chọn, thẻ tag"),
                 ("outline <code>focus/width</code>, <code>focus/offset</code>", f"n:{FOCUS_OUTLINE} trang", "—", "Nút, ô chọn, avatar"),
             ])),
        dict(title="Lỗi đã thấy khi dựng trang: khung Tối nhận bóng Sáng",
             intro=("<code>design-system/tokens.css</code> khai <code>--elev-*</code> và <code>--focus-color</code> ở <code>:root</code>. Biến tính xong ở gốc rồi mới truyền xuống, nên khung <code>data-theme=\"dark\"</code> lồng trong trang Sáng "
                    "nhận <b>bóng #101828 và viền #E5E5E5</b>, đo bằng Chrome ngày 01/11/2026. App đặt theme ở thẻ gốc thì không dính; mọi trang review vẽ Sáng/Tối cạnh nhau thì dính. "
                    "Trang này đã khai lại biến theo từng khung để phần Tối đúng. Sửa <code>_scripts/ds-v2-tokens.py</code> là việc riêng, không cần chọn."),
             html=panes(lambda m, p: cap("Như đang thấy ở trang review khác") + '<div class="tp-card" style="border-color:var(--neutral-200);box-shadow:0 16px 40px 0 var(--alpha-shadow-16)"><span class="type-body">Thẻ trong khung Tối, viền sáng chói</span></div>'
                        + cap("Đúng") + '<div class="tp-card"><span class="type-body">Thẻ trong khung Tối, viền <code>color/border/secondary</code></span></div>', modes=("dark",))),
        dict(title="Đã chốt, không mở lại",
             html=rows(["Quyết định", "Nội dung"], [
                 ("DEC-125", "Thẻ có viền mảnh và bóng rất nhẹ; bóng đậm chỉ cho sheet, dialog, popover."),
                 ("DEC-137", "Lớp nổi có 4 bậc <code>elev/0</code> … <code>elev/3</code>."),
                 ("DEC-170", "Vòng focus và viền ô đang gõ than chì cho mọi khách, không theo dải màu khách."),
                 ("DEC-198", "Vòng focus nút Danger màu danger."),
                 ("DEC-258", "Thang làm mờ có 4 bậc, mỗi bậc một chỗ áp."),
                 ("DEC-301", "Tooltip dùng <code>elev/1</code>."),
                 ("DEC-312", "Component Card cũ và token <code>card/*</code> đã xoá, nên không còn trục Elevation của thẻ."),
                 ("DEC-321", "Focus ô nhập là viền 2px <code>color/focus/ring</code>, không quầng mờ, trùng cách làm của Untitled."),
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)",
             html=('<div class="ef-ladder"><div class="kpi"><b>3</b><span><code>elev/1 · 2 · 3</code> theo vai, giữ số DEC-137, không thêm thang</span></div>'
                   '<div class="kpi"><b>3</b><span>màu bóng sau khi gộp <code>color/shadow/md-soft</code></span></div><div class="kpi"><b>2 + 2</b><span><code>color/focus/ring</code>, <code>color/focus/ring_error</code> + dày 2, cách 2</span></div>'
                   '<div class="kpi"><b>4</b><span><code>backdrop-blur/sm · md · lg · xl</code></span></div><div class="kpi"><b>3</b><span>token mới: <code>elev/3-border</code>, <code>color/bg/overlay_solid</code>, <code>color/bg/primary_blur</code></span></div></div>')),
    ],
    items=[
        dict(id="ef00", grp="Cấu trúc", title="Đặt tên theo Untitled hay giữ elev/* theo vai",
             why=(f"Khoảng cách, Bo góc đã có thang tên Untitled và token vai trỏ vào (DEC-314, DEC-315), vì ở đó số trùng họ. Bóng thì <mark>tên trùng mà số khác</mark>: <code>elev/2</code> 0 4 12 so với <code>shadow-md</code> 0 4 6 −1; <code>elev/3</code> 16 40 so với <code>shadow-xl</code> 20 24. "
                  f"Người đọc Untitled rồi viết <code>shadow-md</code> sẽ được hình khác, cùng lý do đổi tên <code>width/*</code> ở trang Lưới (mục gr00). Tên CSS phải bằng tên token nên không có cách đặt tên riêng cho code. DEC-315 cũng ghi “lớp nổi đi qua style <code>elev/*</code> + <code>color/shadow/*</code>”. Hiện có {css_use['elev-1'] + css_use['elev-2'] + css_use['elev-3']} chỗ CSS và {sum(spec_use.values())} chỗ spec viết theo tên này."),
             untitled="Thang <code>shadow-xs … 3xl</code>, không có tầng vai; dialog dùng thẳng <code>shadow-xl</code>.",
             ours="<code>elev/1 · 2 · 3</code> + viền đi kèm; không có thang.",
             astryx="Ba bậc theo vai <code>Elevation/Low · Medium · High</code>, không có thang.",
             note="Bảng tra sang Untitled sẽ nằm trong <code>design-system/foundations/effect-styles.md</code>: <code>elev/1</code> gần <code>shadow-xs</code>, <code>elev/2</code> gần <code>shadow-md</code> về độ cao và giữ vai của <code>shadow-lg</code>, <code>elev/3</code> giữ vai của <code>shadow-xl</code>.",
             pv=panes(pv_ladder), pv_raw_ok="Số Untitled để thấy cùng tên khác hình",
             opts=[("elev", "Giữ elev/* theo vai, không thêm token, tài liệu có bảng tra sang Untitled", True),
                   ("two", "Thêm shadow/xs · md · xl, elev/* trỏ vào. Cái giá: shadow/md, shadow/xl trùng tên Untitled mà khác số, ai làm theo Untitled sẽ ra hình khác", False),
                   ("all", "Thêm đủ 7 bậc shadow/*. Cái giá: cùng lỗi trùng tên, thêm 4 bậc chưa ai dùng", False)]),
        dict(id="ef01", grp="Bóng", title="Số đo ba bậc: giữ của mình hay lấy số Untitled",
             why=("Hướng chốt ở Màu: giá trị giữ của mình khi có lý do (DEC-320). Lý do ở đây là DEC-125, DEC-137: bóng của mình không spread âm, tán rộng. Bóng dialog của mình đậm gấp đôi Untitled (<b>16%</b> so với <b>8%</b>), hợp màn dày dữ liệu nền trắng khi dialog đè lên bảng. "
                  "Nguồn: <code>design-system/foundations/effect-styles.md</code> mục 8. Đổi số thì mọi màn đổi nhẹ và phải chụp lại Figma. Hai phương án lấy số Untitled là mở lại DEC-137, chưa có bằng chứng mới ngoài việc theo họ."),
             untitled="<code>shadow-xs</code> 0 1 2 · 5%; <code>shadow-lg</code> 3 lớp, cao 12; <code>shadow-xl</code> 3 lớp, cao 20.",
             ours="<code>elev/1</code> 0 1 2 · 6%; <code>elev/2</code> cao 4; <code>elev/3</code> cao 16, nhoè 40.",
             astryx="<code>low</code> 0 2 4 · 5% + 0 4 8 · 10%; <code>medium</code> 0 2 4 · 5% + 0 4 12 · 10%; <code>high</code> 0 4 6 · 10% + 0 12 24 · 15%.",
             pv=panes(pv_values), pv_raw_ok="Số Untitled để so",
             opts=[("keep", "Giữ số DEC-137 cho cả ba bậc, không màn nào đổi", True),
                   ("untitled", "Lấy số Untitled xs · lg · xl, mọi thẻ, menu, dialog đổi nhẹ", False),
                   ("mix", "Lấy số Untitled riêng bậc menu, cao 12 thay cao 4", False)]),
        dict(id="ef02", grp="Bóng", title="Màu bóng: gộp biến trùng, giữ #101828 hay đổi đen",
             why=("<code>color/shadow/sm</code> và <code>color/shadow/md-soft</code> <mark>trùng cả hai chế độ</mark> (6%, Tối 40%), <code>design-system/_review/token-usage.json</code> xếp vào nhóm trùng. Untitled ghi luật “mặc định mọi shadow dùng đen #000 + độ mờ” để không lệ thuộc dải xám. "
                  "Của mình #101828 đọc gần như đen; bộ <code>alpha/black</code> (DEC-320) chỉ có bậc 10, 20… nên đổi sang đen phải thêm primitive 6%, 16%. <b>Mở lại DEC-258:</b> phần E1 chốt 4 biến; bằng chứng mới là hai biến trùng hẳn, gộp không đổi màu nào."),
             untitled="15 biến <code>shadow-xs</code> … <code>shadow-3xl_02</code>, đều đen; Tối trong Figma <code>?</code> chưa đọc.",
             ours="4 biến <code>color/shadow/sm</code>, <code>color/shadow/md</code>, <code>color/shadow/md-soft</code>, <code>color/shadow/lg</code>.",
             astryx="<code>elevation-shadow</code> đen 10%; Tối đen đậm hơn.",
             pv=panes(pv_color), pv_raw_ok="So #101828 với đen",
             opts=[("merge", "Gộp color/shadow/md-soft vào color/shadow/sm, giữ #101828, không màn nào đổi", True),
                   ("keep", "Giữ nguyên 4 biến", False),
                   ("black", "Gộp và đổi sang đen, thêm primitive alpha 6% và 16%", False)]),
        dict(id="ef03", grp="Tối", title="Dialog, sheet, toast ở Tối có thêm viền không",
             why=("Tối dựa vào mặt sáng hơn nền: <code>color/bg/primary_alt</code> #202020 trên scrim chỉ cách <b>1,15:1</b>, thêm viền #2E2E2E được <b>1,38:1</b>; bóng đen gần như chìm. "
                  "<code>elev/1</code>, <code>elev/2</code> đã có viền, riêng <code>elev/3</code> không. <code>design-system/components/base/alert-notification.md</code> đã tự ghi viền cho toast, tức <mark>spec đang lệch bảng mục 8</mark>. <b>Mở lại DEC-137:</b> DEC ghi <code>elev/3</code> chỉ có bóng, chốt trước khi có nền Tối #191919 (DEC-316); bằng chứng mới là các số đo vừa nêu. Sáng giữ không viền."),
             untitled="Modal <code>shadow-xl</code> không viền; menu <code>ring-secondary_alt</code>. Không tách Tối.",
             ours="<code>elev/3</code> viền <code>null</code> trong <code>design-system/tokens.json</code>; mặt nổi <code>color/bg/primary_alt</code>.",
             astryx="Tối thêm viền trong trắng mờ cho mọi bậc: <code>high</code> kèm inset 1px #ffffff26.",
             tokens=[("elev/3-border", "Sáng trong suốt · Tối <code>color/border/secondary</code>", "Dialog, sheet, toast")],
             note="Hai spec <code>design-system/components/base/alert-notification.md</code> và <code>design-system/components/application/sidebar-navigation.md</code> còn ghi nền <code>color/bg/primary</code> cho lớp nổi, trái <code>design-system/foundations/color.md</code> dòng 371. Sửa cùng lượt.",
             pv=panes(pv_border),
             opts=[("dark", "Thêm elev/3-border: Tối có viền, Sáng giữ nguyên", True),
                   ("both", "Thêm viền cả hai chế độ, Sáng mọi dialog có thêm viền", False),
                   ("none", "Giữ không viền, bỏ viền khỏi spec toast", False)]),
        dict(id="ef04", grp="Tối", title="Thẻ ở Tối: giữ bóng hay chỉ để viền",
             why=("Bóng <code>elev/1</code> ở Tối là đen 40%, cao 1, chỉ tạo mép <b>1,09:1</b> so với nền #191919. Ranh giới thẻ thực chất do viền mang. Bỏ bóng thì luật Tối gọn hơn; giữ thì một style chung cho hai chế độ, Figma không phải tách. "
                  "DEC-125 chốt “viền mảnh và bóng rất nhẹ”, đã bỏ phương án “Phẳng, chỉ viền”. Chọn chỉ viền ở Tối là <b>Mở lại DEC-125:</b> bằng chứng là mép 1,09:1 vừa đo."),
             untitled="Figma Tối <code>?</code> chưa đọc; code giữ <code>shadow-xs</code> đen 5%, gần như không thấy.",
             ours="<code>elev/1</code> + <code>elev/1-border</code>, màu bóng <code>color/shadow/sm</code> Tối 40%.",
             astryx="Tối dùng bóng đậm hơn và viền trong trắng mờ.",
             pv=panes(pv_card_dark),
             opts=[("keep", "Giữ bóng và viền, không đổi gì", True),
                   ("border", "Tối đặt elev/1 không bóng, chỉ còn viền", False)]),
        dict(id="ef05", grp="Áp dụng", title="Menu thả: elev/2 hay elev/3",
             why=(f"DEC-137 ghi menu dùng <code>elev/2</code>, nhưng <mark>{spec_use['elev/2']} spec viết <code>elev/2</code></mark>. Ba chỗ menu viết <code>elev/3</code>: menu tầng ẩn ở <code>design-system/components/base/breadcrumbs.md</code>, menu tầng ẩn và menu tài khoản ở <code>design-system/components/application/header-navigation.md</code>. "
                  f"CSS trang component lại dùng <code>elev-2</code> {css_use['elev-2']} chỗ. Spec và trang đang nói hai số. Phương án đổi luật là mở lại DEC-137, không có bằng chứng mới."),
             untitled="<code>shadow-lg</code> cho <code>dropdown</code>, <code>popover</code>, <code>tooltip</code>; riêng modal <code>shadow-xl</code>.",
             ours="<code>design-system/foundations/effect-styles.md</code>: <code>elev/2</code> cho menu; 3 spec ghi <code>elev/3</code>.",
             astryx="Dropdown bóng <code>medium</code>, dialog <code>high</code>.",
             pv=panes(pv_menu),
             opts=[("e2", "Sửa 3 spec về elev/2, đúng DEC-137 và CSS đang chạy", True),
                   ("e3", "Đổi luật: menu dùng elev/3, bỏ elev/2 khỏi thang", False)]),
        dict(id="ef07", grp="Focus", title="Vòng focus: có thêm 7 style của Untitled không",
             why=("Bảy style tồn tại vì Figma không gắn được nhiều nét nên Untitled phải gộp vòng với bóng. Của mình vòng là lớp riêng, bóng thẻ giữ nguyên, nên <mark>2 màu + dày 2 + cách 2 đủ phủ</mark>. Code Untitled cũng chỉ dùng outline (51 chỗ <code>focus-visible:outline-2</code>). "
                  "Thêm <code>--focus-color</code> đang trùng <code>color/focus/ring</code>, chỉ <code>design-system/components/_work/badge-avatar/page.json</code> dùng. Tương phản đo ngay dưới đây, ngưỡng 3:1."),
             untitled="7 style <code>focus-ring</code>, <code>focus-ring-error</code>, <code>focus-ring-shadow-*</code>; hai biến màu <code>--color-focus-ring</code>, <code>--color-focus-ring-error</code>.",
             ours="<code>color/focus/ring</code>, <code>color/focus/ring_error</code>, <code>focus/width</code>, <code>focus/offset</code>; ô nhập viền 2px (DEC-321).",
             astryx="Viền ngoài 2px <code>accent</code>, cách 3; ô nhập <code>ring-focus</code> inset 3px.",
             pv=panes(pv_focus, platforms=("web", "mobile")),
             opts=[("keep", "Không thêm style, bỏ --focus-color, badge-avatar trỏ color/focus/ring", True),
                   ("keepall", "Không thêm style, giữ --focus-color", False),
                   ("seven", "Thêm đủ 7 style vào Figma để tra như Untitled", False)]),
        dict(id="ef08", grp="Focus", title="Khe focus: tô màu nền trang hay để trong suốt",
             why=(f"Có hai cách đang chạy song song: <b>{FOCUS_OUTLINE} trang dùng outline</b>, khe trong suốt; <b>{FOCUS_SHADOW} trang dùng box-shadow</b>, khe tô <code>color/focus/gap</code> = nền trang (DEC-258). "
                  "<b>Mở lại DEC-258:</b> phần C5 chốt khe focus = nền trang. Bằng chứng mới: DEC-258 bỏ nền xám nhưng vẫn còn <code>color/bg/secondary</code>, dòng chọn, cảnh báo. Trên các nền đó khe tô màu <mark>hiện một vạch khác màu nền</mark>, đúng lỗi “khe lộ” của DEC-241. Figma vẫn cần vẽ vòng thành lớp riêng, khung vòng không tô nền thì cũng trong suốt."),
             untitled="Code <code>outline-offset-2</code>, khe trong suốt. Figma tô <code>bg-primary</code>.",
             ours="<code>color/focus/gap</code> Sáng trắng, Tối #191919; <code>design-system/components/_work/_forms/kit.py</code> dùng box-shadow.",
             astryx="Không có khe màu; <code>outlineOffset</code> 3, trong suốt.",
             pv=panes(pv_gap),
             opts=[("outline", "Web đổi hết sang outline, bỏ color/focus/gap, vòng Figma không tô nền", True),
                   ("keep", "Giữ color/focus/gap, chấp nhận vạch khác màu trên nền phụ", False),
                   ("code", "Code dùng outline, Figma giữ color/focus/gap để vẽ", False)]),
        dict(id="ef09", grp="Làm mờ", title="Nền sau dialog, sheet: áp đúng mục 8.1 hay giữ 50%",
             why=(f"Mục 8.1 ghi “scrim 35% + blur thay scrim 50%” cho bậc <code>blur/lg</code> (DEC-258 phần E3: mỗi bậc một chỗ áp), nhưng <code>color/bg/overlay</code> vẫn 50% và <mark>{BLUR_IN_PAGES}/{len(PAGES)} trang có <code>backdrop-filter</code></mark>. Tức quyết định chưa áp. "
                  "Đo: dialog trắng trên scrim 50% cách <b>3,74:1</b>, trên 35% còn <b>2,35:1</b> nhưng chữ phía sau đã mờ nên ít nhiễu. Chưa đo được độ mượt trên máy Android của lái xe; máy yếu cần đường lùi về 50%. Phương án giữ 50% là <b>Mở lại DEC-258:</b> phần E3; bằng chứng duy nhất là số đo trên, chưa có số về máy."),
             untitled="Modal <code>bg-overlay/70</code> + <code>backdrop-blur-[6px]</code>; slide-out <code>bg-overlay/70</code> không mờ; <code>shadow-xl</code> cho cả hai.",
             ours="<code>color/bg/overlay</code> = <code>alpha/neutral-950-50</code>; mục 8.1 ghi <code>blur/lg</code> 24 + 35%.",
             astryx="Sáng đen 50%, Tối đen 80%, không mờ.",
             tokens=[("color/bg/overlay", "<code>neutral/950</code> 35%", "Dialog, sheet"),
                     ("color/bg/overlay_solid", "<code>neutral/950</code> 50%", "Đường lùi khi máy không chạy được mờ")],
             pv=panes(pv_scrim),
             opts=[("apply", "Áp đúng DEC-258: 35% + blur/lg, máy yếu lùi về 50%; đo trên máy thật trước khi vào app", True),
                   ("solid", "Giữ 50% không mờ, sửa mục 8.1, đảo phần E3 của DEC-258", False),
                   ("u70", "Lấy cách Untitled: 70% + mờ 6, thêm một bậc blur", False)]),
        dict(id="ef10", grp="Làm mờ", title="Thanh dính, thanh nổi mờ: nền ghi trắng 70%, 60% sai ở Tối",
             why=("Mục 8.1 ghi “nền trắng 70%” cho đầu màn dính, “nền trắng 60%” cho thanh nổi app (DEC-160). Hai số không có token, và <mark>trắng 70% trên nền Tối thành mảng xám sáng #BABABA</mark>. "
                  "Hai thanh cùng một vai nên gộp về một token, độ mờ 70: nền đặc hơn thì chữ trên thanh ít nhiễu hơn so với 60. Phương án bỏ mờ là mở lại DEC-258 phần E3 cho <code>blur/sm</code>, <code>blur/md</code>."),
             untitled="Không có token. Mẫu Figma: nền trắng 60%, viền trắng 50%, trên ảnh nền; <code>backdrop-blur-sm</code>.",
             ours="<code>blur/sm</code>, <code>blur/md</code> trong <code>design-system/foundations/effect-styles.md</code>; nền ghi chữ, chưa token.",
             astryx="Không có thanh mờ, thanh đặc.",
             tokens=[("color/bg/primary_blur", "<code>color/bg/primary</code> 70%", "Đầu màn dính, thanh nổi app; Sáng trắng 70, Tối #191919 70")],
             pv=panes(pv_bar),
             opts=[("token", "Thêm color/bg/primary_blur 70%, đổi theo chế độ, dùng cho cả hai thanh", True),
                   ("solid", "Bỏ mờ ở thanh, dùng nền đặc + viền dưới", False)]),
        dict(id="ef11", grp="Làm mờ", title="Thang làm mờ: tên và số bậc",
             why=("Bốn số trùng Untitled 8 · 16 · 24 · 40. Tên khác: <code>blur/*</code> so với <code>backdrop-blur-*</code>. Hướng chốt là tên theo Untitled (DEC-320), và <mark>đổi tên lúc này không tốn gì</mark> vì 0 component dùng. "
                  "<code>blur/xl</code> mục 8.1 ghi không dùng; giữ để thang đủ như DEC-314. Phương án bỏ <code>blur/xl</code> là mở lại DEC-258 phần E3, không có bằng chứng mới."),
             untitled="<code>backdrop-blur-sm · md · lg · xl</code> trong Figma.",
             ours="<code>blur/sm</code>, <code>blur/md</code>, <code>blur/lg</code>, <code>blur/xl</code>.",
             astryx="Không có thang làm mờ.",
             tokens=[("backdrop-blur/sm", "8", "Đầu màn dính"), ("backdrop-blur/md", "16", "Thanh nổi app"), ("backdrop-blur/lg", "24", "Sau dialog, sheet"), ("backdrop-blur/xl", "40", "Giữ cho đủ thang, chưa dùng")],
             pv=panes(pv_blur),
             opts=[("rename", "Đổi tên thành backdrop-blur/*, giữ 4 bậc, số không đổi", True),
                   ("keep", "Giữ tên blur/*, ngắn hơn", False),
                   ("drop", "Giữ tên, bỏ blur/xl vì không dùng", False)]),
        dict(id="ef12", grp="Nút", title="Bóng trong kiểu skeuomorphic của nút: có lấy không",
             why=("Untitled gắn <code>shadow-xs-skeuomorphic</code> ở 4 component (11 chỗ: nút, nút tiện ích, nút mạng xã hội, Featured icon), ref ghi “cố tình rất nhẹ” và “bỏ dễ”. Nút của mình phẳng, than chì (DEC-119, DEC-320 giữ lại). "
                  "Lái xe nhìn ngoài nắng thì nét trong 5% rất khó thấy, lại thêm 2 biến màu. Vòng focus <code>-skeuomorphic</code> cũng không cần theo."),
             untitled="<code>--shadow-skeuomorphic</code>: viền trong 1px 18%, nét −2px 5%; <code>--shadow-xs-skeuomorphic</code> thêm xs.",
             ours="Nút phẳng, <code>design-system/components/_work/buttons/page.json</code>; nút phụ viền <code>color/border/primary</code>.",
             astryx="Nút phẳng, không bóng trong.",
             pv=panes(pv_skeu), pv_raw_ok="Số Untitled để so",
             opts=[("no", "Không lấy, nút giữ phẳng, không thêm token", True),
                   ("yes", "Lấy cho nút Primary, Secondary, thêm 2 biến màu, mọi nút đổi nhẹ", False)]),
    ],
    final=("Khi bạn chốt: mình cập nhật <code>design-system/tokens.json</code> → sinh <code>design-system/tokens.css</code> + handoff → sửa <code>design-system/foundations/effect-styles.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>elevation = approved</b> "
           "(<code>ds-foundation-status.py set elevation approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). Việc riêng của trang: sửa lỗi khung Tối ở <code>_scripts/ds-v2-tokens.py</code>, sửa các spec lệch, xoá dòng <code>Base / Card</code> còn sót ở mục 8 (DEC-312)."),
    css=CSS,
    js="TAG.effect.sel+=',.ef-toast';",
)
