#!/usr/bin/env python3
"""SPEC trang review Padding component: lề trong và khoảng theo dạng nội dung (chữ, icon, chấm, ô đếm, ảnh, nút), đo trên Figma.
Dựng: python3 _scripts/foundation_review/build.py padding
Số đo đọc ngày 02/11/2026 từ file FifpyOMpZk9OP8qyNzbRVJ, trang DS · Base components và DS · Application components (chỉ đọc)."""
import kit
from kit import icon, panes, rows

OK, DIFF, GAP, OWN, NOTE = "st-ok", "st-diff", "st-gap", "st-own", "st-note"
LAB = {OK: "Giống", DIFF: "Khác có lý do", GAP: "Lệch, cần chọn", OWN: "Chỉ mình có", NOTE: "Khác, chưa rõ lý do"}


def c(s):
    return f"<code>{s}</code>"


FLAG = '<span class="pd-flag">đo khác</span>'
REF = "design/_ref/untitled-ui/react/components"

# ---------- Đo liên kết: số trường lề, khoảng trên biến thể mặc định, không tính lớp trong instance ----------
# bare: số trần khác 0 · prim: gắn thẳng primitive · sem: gắn thang Semantic · role: gắn token vai · orph: biến treo
AUDIT = [
    ("Base", "Button", 0, 0, 54, 60, 0), ("Base", "Tooltip", 12, 0, 126, 0, 0), ("Base", "Badge", 120, 2, 182, 60, 0),
    ("Base", "Tag", 70, 0, 0, 0, 0), ("Base", "_Tag count", 2, 4, 0, 0, 0), ("Base", "_Tag close X", 4, 8, 0, 0, 0),
    ("Base", "Avatar label", 0, 0, 3, 0, 0), ("Base", "Input", 23, 0, 226, 0, 0), ("Base", "Select", 0, 0, 152, 0, 0),
    ("Base", "Multi-select", 3, 4, 22, 0, 0), ("Base", "Dropdown item", 0, 0, 0, 7, 28), ("Base", "Select item", 0, 0, 4, 3, 12),
    ("Base", "_Multi-select item", 0, 0, 0, 3, 12), ("Base", "Dropdown heading", 0, 0, 4, 2, 4), ("Base", "Dropdown trigger", 0, 0, 12, 3, 0),
    ("Base", "Radio label", 0, 0, 6, 0, 0), ("Base", "Radio group item", 76, 0, 44, 96, 0), ("Base", "Checkbox label", 0, 0, 12, 0, 12),
    ("Base", "Checkbox group item", 76, 0, 44, 96, 0), ("Base", "Toggle label", 0, 4, 4, 0, 0),
    ("App", "_Tab chip", 0, 0, 0, 3, 0), ("App", "Breadcrumbs", 24, 0, 22, 0, 0), ("App", "_Header bell", 0, 0, 8, 0, 0),
    ("App", "_Search result", 2, 0, 3, 2, 0), ("App", "_Nav item", 0, 0, 20, 0, 0), ("App", "_Nav button", 0, 0, 4, 0, 0),
    ("App", "_Scope option", 0, 0, 5, 0, 0), ("App", "_Nav account card", 0, 0, 5, 0, 0), ("App", "_Button group item", 0, 0, 0, 2, 0),
    ("App", "Alert", 48, 0, 60, 0, 0), ("App", "Notification", 28, 0, 42, 0, 0), ("App", "_File row", 6, 0, 48, 6, 0),
    ("App", "Vehicle Card", 14, 0, 0, 0, 0), ("App", "Vehicle Card / Mobile", 14, 0, 0, 0, 0), ("App", "Vehicle Option Card", 14, 0, 0, 0, 0),
    ("App", "Vehicle Option Card / Mobile", 14, 0, 0, 0, 0), ("App", "Card header", 0, 6, 33, 0, 12), ("App", "Section header", 0, 0, 48, 0, 0),
]
N_BARE, N_PRIM, N_SEM, N_ROLE, N_ORPH = (sum(a[i] for a in AUDIT) for i in (2, 3, 4, 5, 6))
N_FIELD = N_BARE + N_PRIM + N_SEM + N_ROLE + N_ORPH
assert N_ORPH == 80 and len(AUDIT) == 38

MEASURED = {
    "Base": ["Button", "Close button", "Utility button", "Tooltip", "Help icon", "Badge", "Tag", "_Tag count", "_Tag close X", "_Tag checkbox", "Avatar label",
             "Input", "_Input field", "Tags input", "Textarea", "Select", "Multi-select", "_Multi-select item", "Select item", "Dropdown item", "Dropdown heading",
             "Dropdown trigger", "Dropdown search", "Dropdown menu", "Radio label", "Radio group item", "Checkbox label", "Checkbox group item", "Toggle label"],
    "App": ["_Tab chip", "_Header tab", "_Header action", "_Header bell", "_Search result", "Breadcrumbs", "_Nav item", "_Nav button", "_Nav tenant switch", "_Nav heading",
            "_Nav account card", "_Nav featured card", "_Module tile", "_Scope option", "_Button group item", "_Section toggle", "Card header", "Section header", "Alert",
            "Notification", "_File row", "Vehicle Card", "Vehicle Card / Mobile", "Vehicle Option Card", "Vehicle Option Card / Mobile", "Combo Text",
            "SegmentedControl", "SegmentedControl / SegmentedControlItem"],
}
N_SETS = sum(len(v) for v in MEASURED.values())
assert N_SETS == 57

# ---------- Bảng đo chính ----------
# nhóm, component, cỡ, dạng, trái, phải, icon→chữ, trên dưới, token, Untitled, trạng thái, ghi chú
R = [
    ("Nút", "Button · Web", "SM · MD · LG (28 · 32 · 40)", "Chỉ chữ", "10 · 12 · 16", "10 · 12 · 16", "—", "cao cố định", f"Ngoài {c('control/padding-x-icon/sm')} + bọc chữ {c('space/xs')}", "<code>px-3 + px-0.5</code> 14 ở cỡ 36", GAP, "SM 10, token ghi 8: mục pd00"),
    ("Nút", "Button · Web", "SM · MD · LG", "Icon trái + chữ", "6 · 8 · 12", "10 · 12 · 16", "8 (4 + 4)", "cao cố định", f"{c('control/padding-x-icon/sm')}, {c('space/xs')}", "<code>gap-1 + px-0.5</code> = 6, cỡ lg 8", GAP, "token icon → chữ ghi 6: mục pd01"),
    ("Nút", "Button · Web", "SM · MD · LG", "Chữ + icon phải", "10 · 12 · 16", "6 · 8 · 12", "8 (4 + 4)", "cao cố định", "như trên", "như trên", GAP, "đối xứng với icon trái"),
    ("Nút", "Button · App", "SM · MD · LG (36 · 44 · 52)", "Chỉ chữ", "12 · 16 · 24", "12 · 16 · 24", "—", "cao cố định", f"{c('control/padding-x-icon/sm')} mode Mobile + {c('space/xs')}", "không có bản app", OWN, "khớp token, DEC-163"),
    ("Nút", "Button · App", "SM · MD · LG", "Icon + chữ", "8 · 12 · 20", "12 · 16 · 24", "8 (4 + 4)", "cao cố định", "như trên", "không có bản app", OWN, "khớp token"),
    ("Nút", "Button", "SM · MD · LG", "Chỉ icon", "vuông 28 · 32 · 40", "vuông", "—", "cao = rộng", "cao, rộng cố định, lề 0", "<code>data-icon-only:p-2</code>, vuông", OK, "icon 16 · 16 · 20"),
    ("Nút", "Button Link Gray", "SM · MD · LG", "Icon + chữ", "0", "0", "6 web · 8 app", "0", c("control/icon-gap"), "<code>gap-1</code> 4, cỡ lg 6", GAP, "khác Button cùng dạng: mục pd01"),
    ("Nút", "Close · Utility · Help", "SM · MD · LG", "Chỉ icon", "vuông 28 · 32 · 40 · 24", "vuông", "—", "cao = rộng", "cao, rộng cố định", "<code>close-button.tsx</code> vuông", OK, ""),
    ("Nút", "_Button group item", "SM 28", "Chỉ chữ", "8", "8", "—", "cao cố định", c("control/padding-x/sm"), "<code>px-3.5</code> 14, icon <code>pl-3</code>", GAP, "cạnh Button SM lề 10: mục pd00"),
    ("Chip", "Badge", "SM · MD · LG", "Chỉ chữ", f"8 · 10 · 12 {FLAG}", "8 · 10 · 12", "—", "cao cố định", f"{c('chip/padding-x-sm')} · {c('chip/padding-x-md')} · {c('chip/padding-x-lg')}", "<code>px-2 · px-2.5 · px-3</code>", OK, "Đã chốt 02/11. Đo trái 6 · 8 · 10 vì Figma tắt chấm chưa đổi lề"),
    ("Chip", "Badge", "SM · MD · LG", "Chấm + chữ", "6 · 8 · 10", "8 · 10 · 12", "4", "cao cố định", f"{c('space/sm')} · {c('space/md')} · {c('chip/padding-x-icon-lg')}; {c('space/xs')}", "<code>pl-1.5 · pl-2 · pl-2.5</code>, gap 4 · 6 · 6", DIFF, "User chốt chấm → chữ 4, khung chấm đã về 0"),
    ("Chip", "Badge", "SM · MD · LG", "Icon + chữ", "6 · 8 · 10", "8 · 10 · 12", "4", "cao cố định", "như chấm", "<code>pl-1.5 · pl-2 · pl-2.5</code>, gap 2 · 4 · 4", DIFF, "Icon 14"),
    ("Chip", "Badge", "SM · MD · LG", "Có ô đếm", "6 · 8 · 10", "3 · 4 · 4", "4", "ô cách đều", f"{c('chip/count-inset')}, {c('space/xs')}; ô đếm 6 số trần", "Badge của họ không có ô đếm", OWN, "Ô đếm xem mục pd08"),
    ("Chip", "Badge", "SM · MD · LG", "Chỉ số (Count Only)", f"8 · 10 · 12 {FLAG}", "8 · 10 · 12", "—", "cao cố định", f"{c('space/xxs')} theo tài liệu", "không có", OWN, "Đo khung bọc đệm 4, tài liệu 2, nên trái đang 10 · 12 · 14"),
    ("Chip", "Badge Type Dot", "SM · MD · LG", "Chấm + chữ", "0", "0", "4", "cao cố định", c("space/xs"), "không có", OWN, ""),
    ("Chip", "Tag", "SM · MD · LG", "Chỉ chữ", "6 · 8 · 10", "6 · 8 · 10", "—", "cao cố định", "số trần 3 + 3 · 3 + 5 · 4 + 6", "<code>px-2 · px-2.25 · px-2.5</code> 8 · 9 · 10", GAP, "mục pd06"),
    ("Chip", "Tag", "SM · MD · LG", "Chấm + chữ", "6 · 8 · 10", "6 · 8 · 10", "4 · 6 · 6", "cao cố định", "số trần, khung bọc", "<code>pl-1.5 · pl-1.75 · pl-2.25</code>, gap 4 · 5 · 6", GAP, "mục pd07"),
    ("Chip", "_Tag count", "SM · MD · LG", "Ô đếm", "4 · 5 · 6", "4 · 5 · 6", "—", "cao 18", f"{c('space/4')}, số trần 5, {c('space/6')}", "<code>px-1 · px-1.25 · px-1.5</code>", OK, "Số giống, cách gắn sai: mục pd13"),
    ("Chip", "_Header bell Count", "—", "Ô đếm", "4", "4", "—", "cao 16", c("space/xs"), "không có", OWN, "mục pd08"),
    ("Ô nhập", "Input · Web", "SM · MD · LG", "Chỉ chữ", "12 (8 + 4)", "12 (8 + 4)", "—", "cao cố định", f"{c('space/md')}, {c('space/xs')}", "<code>px-3</code> 12, cỡ lg 14", OK, ""),
    ("Ô nhập", "Input · Web", "SM · MD · LG", "Icon trái + chữ", "8", "12", "8 (4 + 4)", "cao cố định", "như trên, icon 14", "<code>left-3</code> 12, <code>pl-9</code> 36: icon → chữ 8", DIFF, "Phía icon 8 theo DEC-196"),
    ("Ô nhập", "Input · App", "LG 52", "Icon + chữ", "16", "16", "16", "cao cố định", c("space/xl"), "không có bản app", OWN, "DEC-341 mục sp06"),
    ("Ô nhập", "Select · Web", "SM · MD · LG", "Chữ + chevron", "12 (8 + 4)", "8", "8 (4 + 4)", "cao cố định", f"{c('space/md')}, {c('space/xs')}", "<code>px-3 py-2 gap-2</code>", DIFF, "Icon trái 16, ở Input là 14"),
    ("Ô nhập", "Select · App", "LG 52", "Chữ + chevron", "16", "16", "16", "cao cố định", c("space/xl"), "không có bản app", OWN, ""),
    ("Ô nhập", "Multi-select · Web", "SM · MD (28 · 34)", "Chữ + chevron", "8 (4 + 4)", "8", "4", "2 · 4", f"{c('space/xs')}, {c('space/md')}; trên dưới {c('space/2')}, {c('space/4')}", "<code>pl-3 pr-2.5</code>, <code>px-3</code>, <code>px-3.5</code>, <code>gap-2</code>", GAP, "Lề và cao lệch Select: mục pd10"),
    ("Ô nhập", "Tags input", "SM · MD · LG (30 · 32 · 40)", "Chữ", "12 (8 + 4)", "12", "4", "4", f"{c('space/md')}, {c('space/xs')}", "<code>gap-1.5</code>, cỡ khác <code>gap-2</code>", GAP, "SM cao 30: mục pd10"),
    ("Ô nhập", "Textarea", "—", "Chữ", "12 (8 + 4)", "12", "—", "12 (8 + 4)", f"{c('space/md')}, {c('space/xs')}", "<code>px-3.5 py-3</code> 14 · 12", DIFF, ""),
    ("Dòng", "Dropdown item · Web", "—", "Icon, chấm, ô chọn + chữ", "8", "8", "12", "8", "<code>list-row/padding-x</code> treo; <code>layout/list-gap</code>", "<code>px-2.5 py-2</code>, icon <code>mr-2</code> 8", GAP, "mục pd03, pd04"),
    ("Dòng", "Dropdown item · App", "—", "Icon + chữ", "12", "12", "12", "12", "như trên, mode Mobile", "không có bản app", OWN, "mục pd03, pd04"),
    ("Dòng", "Select item", "Simple · Supporting · Rich", "Icon + chữ + dấu chọn", "8", "8", "12", "8", "như Dropdown item", "<code>p-2 pr-2.5 gap-2</code>", GAP, "mục pd03, pd04"),
    ("Dòng", "_Multi-select item", "—", "Ô chọn + chữ", "8", "8", "12", "8", "như Dropdown item", "<code>p-2 pr-2.5 gap-2</code>, như Select item", GAP, "mục pd03, pd04"),
    ("Dòng", "_Nav item", "—", "Icon + chữ + số", "8", "8", "8", "8", c("space/md"), "<code>p-2</code>", OK, ""),
    ("Dòng", "_Search result", "—", "Icon + chữ", "16", "16", "12", "6 số trần", f"{c('space/xl')}, {c('space/lg')}", "không có", OWN, "mục pd12"),
    ("Dòng", "_File row", "—", "Ảnh, loại tệp + chữ + nút xoá", "12", "8", "12", "12", c("space/lg"), "<code>p-4 gap-3</code> 16 · 12", DIFF, "Nút xoá 32 tự có đệm"),
    ("Thẻ", "Radio, Checkbox group item", "Icon simple", "Icon + chữ + ô chọn", "16", "16", "12", "16", f"{c('layout/card-padding')}, {c('space/lg')}", "ref không có thẻ chọn", OWN, ""),
    ("Thẻ", "Radio, Checkbox group item", "Radio button, Checkbox", "Ô chọn + chữ", "16", "16", "8 số trần", "16", c("layout/card-padding"), "ref không có", OWN, "mục pd12"),
    ("Thẻ", "Radio, Checkbox group item", "Icon card, phần đầu", "Icon + chữ + ô chọn", "12", "20", "12", "12", "số trần", "ref không có", GAP, "mục pd11"),
    ("Thẻ", "Vehicle Card", "Web · Mobile", "Ảnh + chữ", "16 · 16", "ảnh sát phải", "12", "16 · 12", "số trần", "riêng Invlogis", OWN, "mục pd11, pd12"),
    ("Thẻ", "Vehicle Card, chân thẻ", "Web · Mobile", "Icon + chữ", "16", "16", "6", "10", "số trần", "riêng Invlogis", GAP, "mục pd11"),
    ("Thẻ", "Vehicle Option Card", "Web · Mobile", "Ảnh + chữ + radio", "16", "16", "12", "12", "số trần", "riêng Invlogis", OWN, "Radio trong thẻ: mục pd05"),
    ("Thẻ", "Radio label", "SM · MD", "Radio + chữ", "0", "0", "8 · 12", "0", f"{c('space/md')} · {c('space/lg')}", "<code>gap-2 · gap-3</code>", OK, "Ruột radio: mục pd05"),
    ("Thẻ", "Checkbox, Toggle label", "SM · MD", "Ô + chữ", "0", "0", "8 · 12", "0", f"{c('space/md')} · {c('space/lg')}", "<code>gap-2 · gap-3</code>", OK, ""),
    ("Thẻ", "Avatar label", "SM · MD · LG", "Ảnh + chữ", "0", "0", "8", "0", c("space/md"), "<code>gap-2</code>", OK, ""),
    ("Thông báo", "Alert · Notification", "—", "Icon + chữ + nút đóng", "12", "12", "12", "12", c("space/lg"), "ref không có", OWN, "DEC-286. Trong khối còn số trần: mục pd12"),
    ("Thông báo", "Tooltip", "Short · Supporting", "Chữ", "8 · 12", "8 · 12", "—", "4 · 8", f"{c('space/md')}, {c('space/xs')}, {c('space/lg')}", "<code>px-3 py-2</code>, có mô tả <code>py-3</code>", DIFF, "mục pd14"),
    ("Điều hướng", "_Tab chip · App", "—", "Chữ + số", "16", "16", "nhãn → số 8", "cao cố định", "<code>tab/padding-x</code>, <code>tab/gap</code>", "<code>py-2 px-2.5 gap-1</code>", GAP, "Tài liệu ghi 6: mục pd09"),
    ("Điều hướng", "_Header tab, Tab item", "—", "Chữ", "0", "0", "—", "cao cố định", "lề 0; giữa tab <code>space/2xl</code>", "<code>px-0.5 pb-2.5</code>, cách <code>gap-3</code>", DIFF, "Không dùng <code>tab/padding-x</code> web"),
    ("Điều hướng", "Breadcrumbs", "Text · Button", "Chữ + vạch chia", "0 · 8", "0 · 8", "4", "0", f"{c('space/md')}, {c('space/xs')}, 4 số trần", "ref không có", OWN, "mục pd12"),
    ("Điều hướng", "_Nav button · _Header action", "—", "Chỉ icon", "vuông 36 · 44", "vuông", "—", "cao = rộng", c("space/md"), "<code>nav-button.tsx</code> vuông", OK, ""),
    ("Điều hướng", "SegmentedControl (Astryx cũ)", "SM · MD · LG", "Chỉ icon", "8 · 12 · 12", "8 · 12 · 12", "4", "0", "<code>Spacing/2</code>, thư viện cũ", "ref không có", GAP, "32 × 24 · 40 × 28 · 40 × 32, không vuông: mục pd15"),
]
ST_N = {k: sum(1 for r in R if r[10] == k) for k in LAB}
FAMS = list(dict.fromkeys(r[0] for r in R))


def main_table():
    head = "".join(f"<th>{h}</th>" for h in ["Component", "Cỡ", "Dạng", "Lề trái", "Lề phải", "Icon, chấm → chữ", "Trên dưới", "Token hay số trần", "Untitled", "Trạng thái"])
    body = []
    for r in R:
        note = f'<br><span class="small muted">{r[11]}</span>' if r[11] else ""
        body.append(f'<tr data-c="{r[0]}"><td><b>{r[1]}</b></td><td>{r[2]}</td><td>{r[3]}</td><td class="n">{r[4]}</td><td class="n">{r[5]}</td><td class="n">{r[6]}</td><td class="n">{r[7]}</td>'
                    f'<td class="small">{r[8]}</td><td class="small">{r[9]}</td><td><span class="{r[10]}">{LAB[r[10]]}</span>{note}</td></tr>')
    btns = '<button data-f="all" aria-pressed="true">Tất cả</button>' + "".join(f'<button data-f="{f}" aria-pressed="false">{f}</button>' for f in FAMS)
    return f'<div class="pd-fb">{btns}</div><div class="tw"><table class="cmp pd-main"><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


# ---------- Sơ đồ đúng tỉ lệ, dựng từ biến thật ----------
def P(v):  # lề
    return f'<span class="pd-s pd-p" style="width:calc({v}*var(--z))"><b></b></span>'


def W(v):  # khung bọc có đệm
    return f'<span class="pd-s pd-w" style="width:calc({v}*var(--z))"><b></b></span>'


def G(v):  # khoảng giữa
    return f'<span class="pd-s pd-g" style="width:calc({v}*var(--z))"><b></b></span>'


def I(name="plus", s="16px"):
    return f'<span class="pd-i" style="width:calc({s}*var(--z));height:calc({s}*var(--z))">{icon(name, "pd-ic")}</span>'


def D(s="6px"):
    return f'<span class="pd-d" style="width:calc({s}*var(--z));height:calc({s}*var(--z))"></span>'


def T(s="Nhãn nút", fs="var(--font-size-sm)"):
    return f'<span class="pd-t" style="--fs:{fs}">{s}</span>'


def C(s="12", pad="6px", h="16px"):
    return f'<span class="pd-c" style="height:calc({h}*var(--z))">{P(pad)}<span class="pd-t" style="--fs:var(--font-size-xs)">{s}</span>{P(pad)}</span>'


def box(parts, h, z=2, r="var(--radius-control)", tone="sec", cap="", w=None):
    wd = f"width:calc({w}*var(--z));" if w else ""
    return (f'<div class="pd-fig"><div class="pd-a" style="--z:{z}"><div class="pd-box {tone}" style="{wd}height:calc({h}*var(--z));border-radius:calc({r}*var(--z))">{"".join(parts)}</div></div>'
            + (f'<div class="small pd-cap">{cap}</div>' if cap else "") + "</div>")


H_S, H_M, H_L = "var(--control-height-sm)", "var(--control-height-md)", "var(--control-height-lg)"
PI_S, PI_M, PI_L = "var(--control-padding-x-icon-sm)", "var(--control-padding-x-icon-md)", "var(--control-padding-x-icon-lg)"
XS = "var(--space-xs)"
C_S, C_M, C_L = "var(--chip-height-sm)", "var(--size-3xl)", "var(--chip-height-lg)"
RF = "var(--radius-full)"


def btn(pi=PI_M, h=H_M, wrap=XS, gap=XS, cap="", z=2, icon_on=True):
    parts = [P(pi)] + ([I(), G(gap)] if icon_on else []) + [W(wrap), T(), W(wrap), P(pi)]
    return box(parts, h, z=z, cap=cap)


def badge(left, right, h=C_M, dot=True, gap=XS, cap="", z=3, tone="chip", fs="var(--font-size-xs)", label="Đang chạy"):
    parts = [P(left)] + ([D(), G(gap)] if dot else []) + [T(label, fs), P(right)]
    return box(parts, h, z=z, r=RF, tone=tone, cap=cap)


def duo(a, b):
    return f'<div class="pd-duo"><div><div class="pd-h">Đang có</div>{a}</div><div><div class="pd-h">Đề xuất</div>{b}</div></div>'


def P4(html):
    return panes(html, modes=("light", "dark"), platforms=("web", "mobile"))


LEGEND = ('<div class="pd-leg"><span><i class="pd-p"></i>Lề của khung ngoài</span><span><i class="pd-w"></i>Đệm của khung bọc bên trong (dễ bị ẩn)</span>'
          '<span><i class="pd-g"></i>Khoảng giữa hai phần tử</span><span class="muted">Số dưới mỗi vùng đọc từ trình duyệt, chia lại cho độ phóng; đổi Web, App thì số đổi theo biến.</span></div>')

HERO = LEGEND + P4(
    '<div class="pd-g2">'
    + btn(PI_S, H_S, cap="Button SM, icon trái", icon_on=True)
    + btn(PI_M, H_M, cap="Button MD, icon trái")
    + btn(PI_L, H_L, cap="Button LG, icon trái")
    + btn(PI_M, H_M, cap="Button MD, chỉ chữ", icon_on=False)
    + box([P("calc((var(--control-height-md) - 16px)/2)"), I(), P("calc((var(--control-height-md) - 16px)/2)")], H_M, cap="Button MD, chỉ icon: vuông")
    + badge("var(--space-md)", "var(--chip-padding-x-md)", cap="Badge MD, chấm + chữ: trái 8 < phải 10")
    + badge("var(--chip-padding-x-md)", "var(--chip-padding-x-md)", dot=False, cap="Badge MD, chỉ chữ: hai bên 10 (đã chốt)")
    + box([P("var(--space-md)"), D(), G(XS), T("Đang chạy", "var(--font-size-xs)"), G(XS), C(), P(XS)], C_M, z=3, r=RF, tone="chip", cap="Badge MD, có ô đếm")
    + box([P("3px"), W("5px"), T("Nhãn", "var(--font-size-xs)"), W("5px"), P("3px")], C_M, z=3, r="var(--radius-sm)", cap="Tag MD, chỉ chữ: 3 + 5 số trần")
    + box([P("var(--space-md)"), I("search"), G(XS), W(XS), T("Nhập nội dung"), W(XS), P("var(--space-md)")], H_M, cap="Input Web MD, icon trái")
    + box([P("var(--control-padding-x-sm)"), I(), G("var(--layout-list-gap)"), T("Xem chi tiết"), P("var(--control-padding-x-sm)")], "calc(var(--control-padding-x-sm)*2 + 20px)", cap="Dropdown item: icon → chữ 12")
    + "</div>")

# ---------- Untitled làm base: số đọc từ mã nguồn, máy kiểm từng lớp ở đúng dòng khi dựng trang ----------
# nhóm, component Untitled, cỡ + cao, phía chữ, phía icon/chấm, icon/chấm → chữ, trên dưới, cách tính, nguồn [(file, dòng, chuỗi)],
# component mình cùng cao, phía chữ, phía icon/chấm, icon/chấm → chữ, trên dưới. "—" = không có hoặc cao cố định, không so.
BTN, BDG, TAG = "base/buttons/button.tsx", "base/badges/badges.tsx", "base/tags/tags.tsx"
INP, SEL, DRP = "base/input/input.tsx", "base/select/select-shared.tsx", "base/dropdown/dropdown.tsx"
ITM, TIP, TAB = "base/select/select-item.tsx", "base/tooltip/tooltip.tsx", "application/tabs/tabs.tsx"
BW = (BTN, 227, 'data-text className={cx("transition-inherit-all", !noTextPadding && "px-0.5")}')
UB = [
    ("Nút", "Button xs", "cao 32", "12", "10", "6", "6", "<code>px-2.5</code> 10 + bọc chữ <code>px-0.5</code> 2; <code>gap-1</code> 4 + 2", [(BTN, 26, "gap-1 rounded-lg px-2.5 py-1.5"), BW], "Button Web MD · 32", "12", "8", "8", "—"),
    ("Nút", "Button sm", "cao 36", "14", "12", "6", "8", "<code>px-3</code> 12 + 2; <code>gap-1</code> 4 + 2", [(BTN, 34, "gap-1 rounded-lg px-3 py-2"), BW], "Button App SM · 36", "12", "8", "8", "—"),
    ("Nút", "Button md", "cao 40", "16", "14", "6", "10", "<code>px-3.5</code> 14 + 2; <code>gap-1</code> 4 + 2", [(BTN, 41, "gap-1 rounded-lg px-3.5 py-2.5"), BW], "Button Web LG · 40", "16", "12", "8", "—"),
    ("Nút", "Button lg", "cao 44", "18", "16", "8", "10", "<code>px-4</code> 16 + 2; <code>gap-1.5</code> 6 + 2", [(BTN, 47, "gap-1.5 rounded-lg px-4 py-2.5"), BW], "Button App MD · 44", "16", "12", "8", "—"),
    ("Nút", "Button xl", "cao 48", "20", "18", "8", "12", "<code>px-4.5</code> 18 + 2; <code>gap-1.5</code> 6 + 2", [(BTN, 51, "gap-1.5 rounded-lg px-4.5 py-3"), BW], "Button App LG · 52, gần nhất", "24", "20", "8", "—"),
    ("Nút", "Button chỉ icon", "cao 32 · 40", "—", "8 · 10", "—", "8 · 10", "<code>data-icon-only:p-2</code>, <code>p-2.5</code>, vuông", [(BTN, 26, "data-icon-only:p-2"), (BTN, 41, "data-icon-only:p-2.5")], "Button Web MD · LG", "—", "8 · 10", "—", "8 · 10"),
    ("Nút", "Button link", "xs đến md · lg, xl", "0", "0", "4 · 6", "0", "Link không có bọc chữ (<code>noTextPadding = isLinkType</code>)", [(BTN, 30, 'linkRoot: "gap-1'), (BTN, 48, 'linkRoot: "gap-1.5'), (BTN, 195, "noTextPadding = isLinkType")], "Button Link Gray Web · App", "0", "0", "6 · 8", "0"),
    ("Nút", "Button group", "cao 36 · 40 · 44", "14 · 16 · 18", "12 · 14 · 16", "6 · 6 · 8", "8 · 10 · 10", "<code>data-icon-leading:pl-3</code>, <code>pl-3.5</code>, <code>pl-4</code>", [("base/button-group/button-group.tsx", 29, "gap-1.5 px-3.5 py-2"), ("base/button-group/button-group.tsx", 33, "gap-1.5 px-4 py-2.5"), ("base/button-group/button-group.tsx", 37, "gap-2 px-4.5 py-2.5")], "_Button group item SM · 28", "8", "—", "—", "—"),
    ("Chip", "Badge Pill, có chấm", "cao 22 · 24 · 28", "8 · 10 · 12", "6 · 8 · 10", "4 · 6 · 6", "2 · 2 · 4", "<code>pl-1.5 pr-2</code>, <code>pl-2 pr-2.5</code>, <code>pl-2.5 pr-3</code>", [(BDG, 172, "gap-1 py-0.5 pl-1.5 pr-2"), (BDG, 173, "gap-1.5 py-0.5 pl-2 pr-2.5"), (BDG, 174, "gap-1.5 py-1 pl-2.5 pr-3")], "Badge có chấm", "8 · 10 · 12", "6 · 8 · 10", "4 · 4 · 4", "—"),
    ("Chip", "Badge Pill, có icon", "cao 22 · 24 · 28", "8 · 10 · 12", "6 · 8 · 10", "2 · 4 · 4", "2 · 2 · 4", "<code>gap-0.5</code>, <code>gap-1</code>, <code>gap-1</code>", [(BDG, 224, "gap-0.5 py-0.5 pr-2 pl-1.5"), (BDG, 228, "gap-1 py-0.5 pr-2.5 pl-2"), (BDG, 232, "gap-1 py-1 pr-3 pl-2.5")], "Badge có icon", "8 · 10 · 12", "6 · 8 · 10", "4 · 4 · 4", "—"),
    ("Chip", "Badge Pill, chỉ chữ", "cao 22 · 24 · 28", "8 · 10 · 12", "—", "—", "2 · 2 · 4", "<code>px-2</code>, <code>px-2.5</code>, <code>px-3</code>", [(BDG, 134, "py-0.5 px-2 text-xs"), (BDG, 135, "py-0.5 px-2.5 text-sm"), (BDG, 136, "py-1 px-3 text-sm")], "Badge chỉ chữ (đã chốt)", "8 · 10 · 12", "—", "—", "—"),
    ("Chip", "Badge Color, chỉ chữ", "cao 22 · 24 · 28", "6 · 8 · 10", "—", "—", "2 · 2 · 4", "Untitled có bộ số riêng cho Badge bo góc", [(BDG, 139, "py-0.5 px-1.5 text-xs"), (BDG, 140, "py-0.5 px-2 text-sm"), (BDG, 141, "py-1 px-2.5 text-sm")], "Badge Color, dùng chung bộ Pill", "8 · 10 · 12", "—", "—", "—"),
    ("Chip", "Tag", "SM · MD · LG", "8 · 9 · 10", "6 · 7 · 9", "4 · 5 · 6", "3 · 2 · 4", "<code>px-2</code> <code>pl-1.5</code>, <code>px-2.25</code> <code>pl-1.75</code>, <code>px-2.5</code> <code>pl-2.25</code>", [(TAG, 96, "px-2 py-0.75"), (TAG, 99, "withDot: \"pl-1.5\""), (TAG, 103, "gap-1"), (TAG, 108, "px-2.25 py-0.5"), (TAG, 111, "withDot: \"pl-1.75\""), (TAG, 115, "gap-1.25"), (TAG, 120, "px-2.5 py-1"), (TAG, 123, "withDot: \"pl-2.25\""), (TAG, 127, "gap-1.5")], "Tag", "6 · 8 · 10", "6 · 8 · 10", "4 · 6 · 6", "—"),
    ("Chip", "Ô đếm trong Tag", "SM · MD · LG", "4 · 5 · 6", "—", "—", "—", "<code>px-1</code>, <code>px-1.25</code>, <code>px-1.5</code>; Badge của họ không có ô đếm", [(TAG, 104, "count: \"px-1"), (TAG, 116, "count: \"px-1.25"), (TAG, 128, "count: \"px-1.5")], "_Tag count", "4 · 5 · 6", "—", "—", "—"),
    ("Ô nhập", "Input", "cao 36 · 40 · 44", "12 · 12 · 14", "12 · 12 · 14", "8 · 8 · 8", "8 · 8 · 10", "Icon → chữ = <code>pl-9</code> 36 − <code>left-3</code> 12 − icon 16; <code>pl-10</code> 40 − 12 − 20; <code>pl-10.5</code> 42 − 14 − 20", [(INP, 77, 'px-3 py-2 text-sm", hasLeadingIcon && "pl-9"'), (INP, 78, "left-3 size-4"), (INP, 83, 'hasLeadingIcon && "pl-10"'), (INP, 84, "left-3 size-5"), (INP, 89, 'px-3.5 py-2.5 text-md", hasLeadingIcon && "pl-10.5"'), (INP, 90, "left-3.5 size-5")], "Input Web · 28 · 32 · 40", "12 · 12 · 12", "8 · 8 · 8", "8 · 8 · 8", "—"),
    ("Ô nhập", "Select", "cao 36 · 40 · 44", "12 · 12 · 14", "10 · 12 · 14", "8 · 8 · 8", "8 · 8 · 10", "Phía icon là chevron: <code>pl-3 pr-2.5</code>, <code>px-3</code>, <code>px-3.5</code>", [(SEL, 41, "py-2 pl-3 pr-2.5 gap-2"), (SEL, 47, "py-2 px-3 gap-2"), (SEL, 48, "py-2.5 px-3.5 gap-2")], "Select Web · 28 · 32 · 40", "12 · 12 · 12", "8 · 8 · 8", "8 · 8 · 8", "—"),
    ("Ô nhập", "Multi-select", "cao 36 · 40 · 44", "12 · 12 · 14", "10 · 12 · 14", "8 · 8 · 8", "8 · 8 · 10", "Dùng chung <code>sizes</code> với Select", [("base/select/multi-select.tsx", 234, "sizes[size].root"), (SEL, 41, "py-2 pl-3 pr-2.5 gap-2")], "Multi-select Web · 28 · 34", "8 · 8", "8 · 8", "4 · 4", "2 · 4"),
    ("Ô nhập", "Tags input, đã có tag", "SM · MD · LG", "8 · 8 · 10", "—", "tag cách 6", "6 · 8 · 10", "<code>py-1.5 pl-2</code>, <code>pl-2</code>, <code>pl-2.5</code>", [("base/input/input-tags.tsx", 197, 'py-1.5 pl-2'), ("base/input/input-tags.tsx", 201, '!isEmpty && "pl-2"'), ("base/input/input-tags.tsx", 205, '!isEmpty && "pl-2.5"'), ("base/input/input-tags.tsx", 234, "flex flex-wrap gap-1.5")], "Tags input", "12", "—", "tag cách 4", "4"),
    ("Ô nhập", "Textarea", "SM · MD", "12 · 14", "—", "—", "12 · 12", "<code>p-3</code>, <code>px-3.5 py-3</code>", [("base/textarea/textarea.tsx", 37, "p-3 text-sm"), ("base/textarea/textarea.tsx", 38, "px-3.5 py-3 text-md")], "Textarea", "12 · 12", "—", "—", "12 · 12"),
    ("Dòng", "Dropdown item", "một cỡ", "10", "10", "8", "8", "Dòng <code>px-2.5 py-2</code>, icon <code>mr-2</code>; khung ngoài dòng <code>px-1.5</code> thêm 6", [(DRP, 94, "rounded-md px-2.5 py-2"), (DRP, 109, "mr-2 size-4"), (DRP, 85, "px-1.5 py-px")], "Dropdown item Web", "8", "8", "12", "8"),
    ("Dòng", "Select item", "SM · MD", "10", "8", "8", "8", "<code>p-2 pr-2.5 gap-2</code>; khung ngoài dòng <code>px-1</code>, <code>px-1.5</code>", [(ITM, 16, "p-2 pr-2.5 gap-2"), (ITM, 23, "p-2 pr-2.5 gap-2"), (ITM, 83, 'size === "sm" ? "px-1" : "px-1.5"')], "Select item", "8", "8", "12", "8"),
    ("Dòng", "Dòng Multi-select", "SM · MD", "10", "8", "8", "8", "Dùng lại Select item", [("base/select/multi-select.tsx", 24, "import { SelectItem }"), (ITM, 16, "p-2 pr-2.5 gap-2")], "_Multi-select item", "8", "8", "12", "8"),
    ("Dòng", "Nav item", "một cỡ", "8", "8", "8", "8", "<code>p-2</code>, icon <code>mr-2</code>", [("application/app-navigation/base-components/nav-item.tsx", 119, '"group/item p-2"'), ("application/app-navigation/base-components/nav-item.tsx", 61, "mr-2 size-5")], "_Nav item", "8", "8", "8", "8"),
    ("Dòng", "File row", "một cỡ", "16", "16", "12", "16", "<code>p-4 gap-3</code>", [("application/file-upload/file-upload-base.tsx", 267, "flex gap-3 rounded-xl bg-primary p-4")], "_File row", "8", "12", "12", "12"),
    ("Ô chọn", "Radio, Checkbox, Toggle kèm chữ", "SM · MD", "—", "—", "8 · 12", "—", "<code>gap-2</code>, <code>gap-3</code>", [("base/radio-buttons/radio-buttons.tsx", 69, "gap-2"), ("base/radio-buttons/radio-buttons.tsx", 75, "gap-3"), ("base/checkbox/checkbox.tsx", 79, "gap-2"), ("base/checkbox/checkbox.tsx", 85, "gap-3"), ("base/toggle/toggle.tsx", 87, "gap-2"), ("base/toggle/toggle.tsx", 93, "gap-3")], "Radio, Checkbox, Toggle label", "—", "—", "8 · 12", "—"),
    ("Ô chọn", "Chấm Radio trong ô 16 · 20", "SM · MD", "—", "6 · 8", "—", "—", "<code>size-1.5</code>, <code>size-2</code>, cố định", [("base/radio-buttons/radio-buttons.tsx", 45, 'size-1.5 rounded-full'), ("base/radio-buttons/radio-buttons.tsx", 45, 'size === "md" && "size-2"')], "Chấm Radio App", "—", "4", "—", "—"),
    ("Ô chọn", "Avatar kèm chữ", "một cỡ", "—", "—", "8", "—", "<code>gap-2</code>", [("base/avatar/avatar-label-group.tsx", 28, "items-center gap-2")], "Avatar label", "—", "—", "8", "—"),
    ("Thông báo", "Tooltip ngắn · có mô tả", "hai dạng", "12 · 12", "—", "—", "8 · 12", "<code>px-3</code>; <code>py-2</code>, có mô tả <code>py-3</code>", [(TIP, 71, "bg-primary-solid px-3"), (TIP, 72, 'description ? "py-3" : "py-2"')], "Tooltip Short · Supporting", "8 · 12", "—", "—", "4 · 8"),
    ("Điều hướng", "Tab dạng nút", "SM", "12", "12", "6", "8", "<code>py-2 px-2.5</code> + bọc chữ <code>px-0.5</code>; <code>gap-1</code> 4 + 2", [(TAB, 56, "py-2 px-2.5"), (TAB, 55, "gap-1"), (TAB, 196, 'type !== "line" && "px-0.5"')], "_Tab chip App · 36", "16", "12", "8", "—"),
    ("Điều hướng", "Tab gạch dưới", "SM", "2", "2", "—", "pb 10", "<code>px-0.5 pb-2.5 pt-0</code>, các tab cách <code>gap-3</code> 12", [(TAB, 60, "px-0.5 pb-2.5 pt-0"), (TAB, 80, "gap-3")], "_Header tab, Tab item", "0", "0", "—", "—"),
]
UB_FILES = {}
for _r in UB:
    for _f, _l, _t in _r[8]:
        _ls = UB_FILES.setdefault(_f, (kit.ROOT / REF / _f).read_text(encoding="utf-8").splitlines())
        assert _t in _ls[_l - 1], f"Untitled đổi nguồn: {_f}:{_l} không còn {_t!r}"
UB_N = sum(1 for _r in UB for _i in range(3, 7) if _r[_i] != "—" and _r[_i + 7] != "—")
UB_OK = sum(1 for _r in UB for _i in range(3, 7) if _r[_i] != "—" and _r[_i] == _r[_i + 7])
UB_FAMS = list(dict.fromkeys(r[0] for r in UB))


def _ub_cell(u, o):
    if u == "—" and o == "—":
        return '<td class="n muted">—</td>'
    cls = "ub-na" if "—" in (u, o) else ("ub-ok" if u == o else "ub-no")
    return f'<td class="n"><span class="ub-u">{u}</span><span class="ub-o {cls}">{o}</span></td>'


def base_table():
    head = "".join(f"<th>{h}</th>" for h in ["Untitled", "Cỡ", "Phía chữ", "Phía icon, chấm", "Icon, chấm → chữ", "Trên dưới", "Mình so với", "Cách tính, dòng nguồn"])
    body = []
    for r in UB:
        src = "<br>".join(f"<code>{f}:{l}</code>" for f, l in sorted({(f, l) for f, l, _ in r[8]}))
        cells = "".join(_ub_cell(r[i], r[i + 7]) for i in range(3, 7))
        body.append(f'<tr data-c="{r[0]}"><td><b>{r[1]}</b></td><td>{r[2]}</td>{cells}<td class="small">{r[9]}</td><td class="small">{r[7]}<br><span class="muted">{src}</span></td></tr>')
    btns = '<button data-f="all" aria-pressed="true">Tất cả</button>' + "".join(f'<button data-f="{f}" aria-pressed="false">{f}</button>' for f in UB_FAMS)
    legend = ('<div class="pd-leg"><span><span class="ub-u">12</span> Số Untitled</span><span><span class="ub-o ub-ok">12</span> Mình bằng</span><span><span class="ub-o ub-no">8</span> Mình khác</span>'
              '<span><span class="ub-o ub-na">8</span> Một bên không có, không so</span></div>')
    return f'<div id="ub-base"></div>{legend}<div class="pd-fb ub-fb">{btns}</div><div class="tw"><table class="cmp pd-main ub-main"><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def _pair(title, u, o, note=""):
    n = f'<div class="small muted">{note}</div>' if note else ""
    return f'<div class="ub-pair"><h4>{title}</h4><div class="pd-h">Untitled</div>{u}<div class="pd-h">Mình</div>{o}{n}</div>'


FS14, FS12 = "14px", "12px"
UB_PAIRS = ('<div class="ub-grid">'
            + _pair("Button cao 32, icon + chữ", box([P("10px"), I(), G("4px"), W("2px"), T("Nhãn nút", FS14), W("2px"), P("10px")], "32px"), box([P("8px"), I(), G("4px"), W("4px"), T("Nhãn nút", FS14), W("4px"), P("8px")], "32px"), "Tổng độ rộng bằng nhau: 10 + 4 + 2 = 8 + 4 + 4")
            + _pair("Button cao 40, icon + chữ", box([P("14px"), I(s="20px"), G("4px"), W("2px"), T("Nhãn nút", FS14), W("2px"), P("14px")], "40px"), box([P("12px"), I(s="20px"), G("4px"), W("4px"), T("Nhãn nút", FS14), W("4px"), P("12px")], "40px"), "Chữ cách mép đều 16")
            + _pair("Badge cao 24, chấm + chữ", box([P("8px"), D(), G("6px"), T("Đang chạy", FS14), P("10px")], "24px", z=3, r=RF, tone="chip"), box([P("8px"), D(), G("4px"), T("Đang chạy", FS12), P("10px")], "24px", z=3, r=RF, tone="chip"), "Mình chữ 12, chấm → chữ 4 đã chốt; Untitled chữ 14")
            + _pair("Tag MD, chấm + chữ", box([P("7px"), D(), G("5px"), T("Nhãn", FS14), P("9px")], "24px", z=3, r="6px"), box([P("3px"), W("5px"), D(), W("1px"), W("5px"), T("Nhãn", FS12), W("5px"), P("3px")], "24px", z=3, r="6px"), "Mình còn khung bọc đệm ẩn: mục pd07")
            + _pair("Input cao 40, icon + chữ", box([P("12px"), I("search", "20px"), G("8px"), T("Nhập nội dung", "16px"), P("12px")], "40px"), box([P("8px"), I("search", "14px"), G("4px"), W("4px"), T("Nhập nội dung", FS14), W("4px"), P("8px")], "40px"), "Untitled phía icon không lùi")
            + _pair("Select cao 40, chữ + chevron", box([P("12px"), T("Chọn một mục", "16px"), G("8px"), I("chevron-down"), P("12px")], "40px"), box([P("8px"), W("4px"), T("Chọn một mục", FS14), W("4px"), G("4px"), I("chevron-down"), P("8px")], "40px"))
            + _pair("Dropdown item, icon + chữ", box([P("10px"), I(), G("8px"), T("Xem chi tiết", FS14), P("10px")], "36px"), box([P("8px"), I(), G("12px"), T("Xem chi tiết", FS14), P("8px")], "36px"), "Mục pd03, pd04")
            + _pair("Select item, icon + chữ", box([P("8px"), I(), G("8px"), T("Xem chi tiết", FS14), P("10px")], "36px"), box([P("8px"), I(), G("12px"), T("Xem chi tiết", FS14), P("8px")], "36px"), "Mục pd03")
            + _pair("Nav item, icon + chữ", box([P("8px"), I(s="20px"), G("8px"), T("Lệnh vận tải", "16px"), P("8px")], "40px"), box([P("8px"), I(s="20px"), G("8px"), T("Lệnh vận tải", FS14), P("8px")], "40px"), "Khớp")
            + "</div>")
UB_VIEW = LEGEND.replace("đổi Web, App thì số đổi theo biến.", "số Mình là số đo Figma.") + panes(UB_PAIRS, modes=("light",), platforms=("web",))

# ---------- Mục chọn ----------
ITEMS = []


def item(**k):
    ITEMS.append(k)


item(id="pd00", grp="Nút", title="Button Web SM: chữ cách mép 10, token ghi 8",
     why=(f"Đo set <b>Button</b> trên Figma (6657:163467): lớp ngoài {c('control/padding-x-icon/sm')} 6 cộng lớp bọc <b>Text padding</b> {c('space/xs')} 4, nên chữ cách mép <mark>10</mark>. "
          f"Bảng trong {c('design-system/foundations/spacing.md')} ghi {c('control/padding-x/sm')} Web 8, nguyên văn: \"Lề trái phải trong nút theo cỡ\". MD 12, LG 16 và cả ba cỡ App đều khớp, chỉ riêng <mark>SM Web</mark> lệch. "
          "Set <b>_Button group item</b> cùng cao 28 đang gắn đúng token nên lề 8; hai món đặt cạnh nhau ở Section header thấy lệch 2."),
     untitled=f"<code>px-3</code> + <code>px-0.5</code> = 14 ở cỡ 36; <code>px-2.5</code> + 2 = 12 ở cỡ 32. Nguồn {c(REF + '/base/buttons/button.tsx')}. Không có cỡ 28.",
     ours=f"{c('control/padding-x/sm')} Web 8, chỉ <b>_Button group item</b> dùng. Button thật 10.",
     astryx="Button SM 28 lề <code>0 12px</code> (<code>design/design.md</code> dòng 312).",
     tokens=[("control/padding-x/sm", "Web 10 · App 12", "Trỏ space/md-lg ở Web; App không đổi")],
     pv=P4(duo(btn(PI_S, H_S, icon_on=False, cap="Button SM: lớp ngoài + bọc chữ") + box([P("var(--control-padding-x-sm)"), T("Nhãn"), P("var(--control-padding-x-sm)")], H_S, cap="Group item SM: theo token"),
               btn(PI_S, H_S, icon_on=False, cap="Button SM giữ nguyên") + box([P("var(--pd-sm-new)"), T("Nhãn"), P("var(--pd-sm-new)")], H_S, cap="Group item SM: Web 10, App không đổi"))),
     opts=[("token10", "Đổi token Web SM thành 10 theo Figma: nút không đổi, Button group item rộng thêm 4", True),
           ("wrap2", "Giữ token 8: bọc chữ SM còn 2, nút SM hẹp đi 4, icon → chữ còn 6", False),
           ("keep", "Giữ cả hai, ghi ngoại lệ vào bảng spacing", False)])

item(id="pd01", grp="Nút", title="Icon → chữ của nút: đo 8, token Web ghi 6, Link Gray 6",
     why=(f"Button có khoảng {c('space/xs')} 4 cộng bọc chữ 4 nên icon → chữ <mark>8</mark> ở cả Web và App. {c('control/icon-gap')} ghi Web 6, App 8, nên Web lệch 2. "
          f"Button Link Gray không có lớp bọc, gắn thẳng {c('control/icon-gap')}, nên đang <mark>6</mark> trên Web: cùng là nút, hai số khác nhau. Input, Select, _Nav item, Avatar label đều 8."),
     untitled=f"<code>gap-1</code> + <code>px-0.5</code> = 6, cỡ lg <code>gap-1.5</code> + 2 = 8. Link: <code>gap-1</code>, lg <code>gap-1.5</code>. {c(REF + '/base/buttons/button.tsx')}.",
     ours=f"{c('control/icon-gap')} Web 6, App 8 (DEC-161).",
     astryx="Icon – nhãn trong nút 8px (<code>design/design.md</code> dòng 494).",
     tokens=[("control/padding-x-icon/sm", "Web 8 · 10 · 14", "Lớp ngoài của nút Web, cả 3 cỡ; cần thêm bậc Semantic 14 vì thang chưa có"),
             ("control/label-inset", "Web 2 · App 4", "Token mới cho bọc chữ của nút, thay space/xs")],
     note="Sửa đề xuất sau khi có base Untitled: bản trước đề xuất đổi token lên 8. Nay đề xuất đưa Figma về đúng token Web 6, vì đúng số Untitled ở các cỡ 32, 36, 40. Độ rộng nút không đổi: chỉ chữ 8 + 4 thành 10 + 2; có icon 8 + 4 + 4 thành 10 + 4 + 2.",
     pv=P4(duo(box([P("8px"), I(), G("4px"), W("4px"), T(), W("4px"), P("8px")], "32px", cap="Button Web MD: icon → chữ 4 + 4, phía icon 8"),
               box([P("10px"), I(), G("4px"), W("2px"), T(), W("2px"), P("10px")], "32px", cap="Như Untitled xs: icon → chữ 4 + 2, phía icon 10, chữ vẫn cách mép 12"))),
     opts=[("six", "Đưa nút Web về 6 như Untitled: phía icon 8 · 10 · 14, bọc chữ 2, chữ cách mép và độ rộng nút không đổi; App giữ 8", True),
           ("eight", "Đổi control/icon-gap Web thành 8: một số cho Web và App, khác Untitled, Link Gray rộng thêm 2", False),
           ("keep", "Giữ nguyên, ghi Link Gray là ngoại lệ", False)])

item(id="pd02", grp="Quy luật", title="Lề phía icon nhỏ hơn lề phía chữ: lùi bao nhiêu?",
     why=("Câu hỏi: quy luật \"phía icon = phía chữ − 2\" có đồng đều không. <mark>Không đồng đều</mark>: Button lùi 4 ở mọi cỡ, Web 6 và 10, 8 và 12, 12 và 16; App 8 và 12, 12 và 16, 20 và 24. "
          "Badge lùi 2 (6 và 8, 8 và 10, 10 và 12). Input, Select Web lùi 4 (8 và 12). Tag không lùi (6 và 6). "
          f"Token {c('control/padding-x-icon/sm')} ghi \"lùi một bậc thang\", đo được thì lùi hai bậc ở Button."),
     untitled=f"Lùi 2 ở cả Button và Badge. Trích {c('design/_ref/untitled-ui/04-spacing-radius-grid.md')}: \"Button có icon: padding trái giảm 2px (16→14) vì icon có ~2px khung đệm → cân bằng thị giác\". Input của họ không lùi (<code>left-3</code>, <code>px-3</code>).",
     ours=f"{c('control/padding-x-icon/sm')} · md · lg; Badge {c('chip/padding-x-sm')} và lề phía chấm theo DEC-341.",
     astryx="Không có luật này: Button lề <code>0 12px</code> hai bên.",
     note="Icon Lucide nét 2,25 có khoảng thở trong khung 24, nên bù quang học 2 đến 4 đều nhìn cân. Số lùi là chọn kiểu, không phải lỗi; cần ghi ra để component sau làm theo.",
     pv=P4(duo(btn(PI_M, H_M, cap="Button MD: 8 và 12, lùi 4") + badge("var(--space-md)", "var(--chip-padding-x-md)", cap="Badge MD: 8 và 10, lùi 2"),
               box([P("10px"), I(), G(XS), W("2px"), T(), W("2px"), P("10px")], "32px", cap="Button Web MD lùi 2 như Untitled: 10 và 12") + badge("var(--space-md)", "var(--chip-padding-x-md)", cap="Badge không đổi"))),
     opts=[("two", "Nút Web, chip lùi 2 như Untitled; ô nhập Web giữ lùi 4; App giữ số đang có. Đi cùng pd01 thì độ rộng nút không đổi", True),
           ("group", "Ghi luật theo nhóm: nút, ô nhập lùi 4; chip lùi 2; không đổi số nào", False),
           ("none", "Không ghi luật, để từng component tự quyết", False)])

item(id="pd03", grp="Dòng menu", title="Dòng menu: icon → chữ 12 do mượn token khoảng cách giữa thẻ",
     why=(f"<b>Dropdown item</b>, <b>Select item</b>, <b>_Multi-select item</b>, <b>Dropdown heading</b>, <b>Dropdown trigger</b> gắn itemSpacing vào {c('layout/list-gap')}, nghĩa trong token là \"Giữa các thẻ, dòng trong danh sách\". "
          f"DEC-341 mục sp04 nâng token đó Web từ 8 lên 12 cho danh sách thẻ, nên <mark>icon → chữ trong menu Web bị kéo từ 8 thành 12</mark>, không ai chọn việc này. Bằng chứng số cũ: biến <code>zz-old/layout/list-gap</code> trên Figma Web 8, App 12."),
     untitled=f"Icon <code>mr-2</code> 8 ({c(REF + '/base/dropdown/dropdown.tsx')}); <code>gap-2</code> 8 ({c(REF + '/base/select/select-item.tsx')}).",
     ours=f"{c('layout/list-gap')} 12 Web và App. _Nav item cùng dạng dòng dùng {c('space/md')} 8.",
     astryx="<code>List / .ListItem</code> nằm trong file Figma cũ, chưa đo riêng; lề dòng không ghi trong <code>design/design.md</code>.",
     pv=P4(duo(box([P("var(--control-padding-x-sm)"), I(), G("var(--layout-list-gap)"), T("Xem chi tiết"), P("var(--control-padding-x-sm)")], "calc(var(--control-padding-x-sm)*2 + 20px)", cap="Icon → chữ 12"),
               box([P("var(--control-padding-x-sm)"), I(), G("var(--space-md)"), T("Xem chi tiết"), P("var(--control-padding-x-sm)")], "calc(var(--control-padding-x-sm)*2 + 20px)", cap="Icon → chữ 8, như _Nav item"))),
     opts=[("eight", "Gắn lại space/md: icon → chữ 8 ở Web và App, chữ trong menu dịch trái 4", True),
           ("split", "Web 8, App 12: thêm lại token list-row/gap theo chế độ, Web như trước DEC-341", False),
           ("keep", "Giữ 12, chấp nhận menu thoáng hơn Untitled", False)])

item(id="pd04", grp="Dòng menu", title="Biến treo: dòng menu, thẻ đang gắn biến không còn trong bảng",
     why=(f"<mark>{N_ORPH} trường</mark> lề, khoảng ở Dropdown item 28, Select item 12, _Multi-select item 12, Dropdown heading 4, Checkbox label 12, Card header 12 gắn <code>list-row/padding-x</code>, <code>list-row/padding-y</code>, <code>list-row/text-gap</code>, <code>card/action-gap</code>. "
          f"Các biến này <b>không còn trong danh sách biến của collection</b> và không có trong {c('design-system/tokens.json')}, nhưng Figma vẫn đọc ra số, còn trỏ thẳng primitive (<code>space/8</code> và <code>space/12</code>). Dev đọc token sẽ không tìm thấy."),
     untitled=f"Không dùng token theo vai cho dòng; <code>px-2.5 py-2</code> ghi thẳng trong {c(REF + '/base/dropdown/dropdown.tsx')}.",
     ours=f"Không có trong {c('design-system/tokens.json')}; bản lưu trên Figma mang tên <code>zz-old/list-row/*</code>. DEC-279: component dùng chung thì số đo theo mode Platform.",
     astryx="Không dùng tên này.",
     tokens=[("list-row/padding-x", "Web 8 · App 12", "Trỏ space/md, space/lg; dòng menu, dòng chọn"), ("list-row/padding-y", "Web 8 · App 12", "Trỏ space/md, space/lg"),
             ("card/action-gap", "Web 8 · App 12", "Trỏ space/md, space/lg; DEC-162 app cách 12")],
     note="Dropdown item không có trục Platform nên cần token đổi theo mode, không gán thẳng theo khối được như ô nhập ở DEC-341. <code>list-row/text-gap</code> 2 thì gắn thẳng thang <code>space/xxs</code>.",
     pv=P4(box([P("var(--control-padding-x-sm)"), I(), G("var(--space-md)"), T("Xem chi tiết"), P("var(--control-padding-x-sm)")], "calc(var(--control-padding-x-sm)*2 + 20px)", cap="Số Web 8, App 12 dựng từ biến cùng giá trị")),
     opts=[("restore", "Khôi phục 3 token vai vào tokens.json, trỏ thang Semantic, gắn lại đúng tên: nhìn không đổi", True),
           ("direct", "Gắn thẳng space/md, thêm trục Platform cho 3 set dòng: tăng gấp đôi biến thể", False),
           ("later", "Để tới đợt sync component mới gắn lại", False)])

item(id="pd05", grp="Ô chọn", title="Radio: chấm đi theo lề, sang App chấm teo còn 4",
     why=(f"Ruột radio không đặt cỡ chấm mà đặt lề. <b>Radio</b> MD và Radio trong <b>Vehicle Option Card</b> gắn {c('control/padding-x-icon/sm')} Web 6, App 8: ô 20 trừ 16 còn <mark>chấm 4</mark> trên App, Web 8. "
          "Radio SM gắn <code>card/radio-on-ring</code> (biến treo) Web 5, App 6: ô 16 trừ 12 còn chấm 4 trên App, Web 6. Đo ở Radio group item Platform Mobile: lề 6. Ngoài ra Radio đang mượn token lề nút, đổi nút sẽ đổi radio."),
     untitled=f"Chấm <code>size-1.5</code> 6 trong ô 16, <code>size-2</code> 8 trong ô 20, cố định. {c(REF + '/base/radio-buttons/radio-buttons.tsx')}.",
     ours=f"{c('control/padding-x-icon/sm')} cho Radio MD; <code>card/radio-on-ring</code> treo cho Radio SM.",
     astryx="Chưa đo set Radio Astryx ở lượt này.",
     pv=P4(duo('<div class="pd-rd"><span class="o s"><i style="width:calc(16px - 2*var(--pd-on-sm));height:calc(16px - 2*var(--pd-on-sm))"></i></span><span class="o m"><i style="width:calc(20px - 2*var(--control-padding-x-icon-sm));height:calc(20px - 2*var(--control-padding-x-icon-sm))"></i></span><span class="small muted">Chấm theo lề, đổi theo Web, App</span></div>',
               '<div class="pd-rd"><span class="o s"><i style="width:var(--size-sm);height:var(--size-sm)"></i></span><span class="o m"><i style="width:var(--size-md);height:var(--size-md)"></i></span><span class="small muted">Chấm cố định 6 và 8</span></div>')),
     opts=[("fixed", "Chấm cố định 6 và 8 bằng size/sm, size/md, lề 0, căn giữa: Web không đổi, App chấm to lại như Web", True),
           ("token", "Thêm token vai radio/dot-inset 5 và 6, cùng số cho Web và App", False),
           ("keep", "Giữ cách cũ, chấp nhận App chấm 4", False)])

item(id="pd06", grp="Chip", title="Tag cùng cao với Badge nhưng lề chữ nhỏ hơn 2",
     why=(f"Tag SM, MD, LG cao 22, 24, 28 như Badge. Lề phía chữ của Tag <mark>6 · 8 · 10</mark>, Badge đã chốt <mark>8 · 10 · 12</mark> (DEC-341). Lề phía chấm thì hai bên đã bằng nhau 6 · 8 · 10. Đặt cạnh nhau trên thanh lọc thấy Tag chật hơn. "
          "Số của Tag là tổng hai lớp số trần: ngoài 3, 3, 4 cộng Label wrap 3, 5, 6."),
     untitled=f"Tag <code>px-2 · px-2.25 · px-2.5</code> 8 · 9 · 10. Badge 8 · 10 · 12. {c(REF + '/base/tags/tags.tsx')}.",
     ours=f"Set Tag 6657:167999, toàn số trần: 70 trường, không gắn biến nào. Badge theo {c('design-system/components/base/badge.md')}.",
     astryx="Badge cao 20 lề <code>0 8px</code> (<code>design/design.md</code> dòng 322).",
     tokens=[("chip/padding-x-sm · md · lg", "8 · 10 · 12", "Dùng lại token Badge cho Tag")],
     pv=P4(duo(box([P("3px"), W("3px"), T("Nhãn", "var(--font-size-xs)"), W("3px"), P("3px")], C_S, z=3, r="var(--radius-sm)", cap="Tag SM: 6"),
               box([P("var(--chip-padding-x-sm)"), T("Nhãn", "var(--font-size-xs)"), P("var(--chip-padding-x-sm)")], C_S, z=3, r="var(--radius-sm)", cap="Tag SM: 8, cùng Badge"))),
     opts=[("badge", "Tag theo Badge, lề chữ 8 · 10 · 12, dùng chung token: mỗi Tag rộng thêm 4", True),
           ("untitled", "Theo Untitled 8 · 9 · 10: thêm số 9 ngoài thang", False),
           ("keep", "Giữ 6 · 8 · 10, gắn token cho đúng số", False)])

item(id="pd07", grp="Chip", title="Tag còn khung bọc đệm ẩn, chấm → chữ 4 · 6 · 6",
     why=("Đây là cùng loại lỗi vừa bắt ở Badge. <b>Dot wrap</b>, <b>Checkbox wrap</b>, <b>Avatar wrap</b>, <b>Flag wrap</b> của Tag có đệm phải 1 ở SM, MD, cộng đệm trái Label wrap 3, 5, 6, thành chấm → chữ <mark>4 · 6 · 6</mark>. "
          "Thân Tag đặt itemSpacing 0, mọi khoảng nằm trong khung bọc nên không gắn được token. Badge đã chốt chấm → chữ 4, khung chấm 0 (DEC-341 phần bổ sung)."),
     untitled=f"<code>gap-1 · gap-1.25 · gap-1.5</code> 4 · 5 · 6, không khung bọc đệm. {c(REF + '/base/tags/tags.tsx')}.",
     ours=f"Set Tag 6657:167999: Dot wrap trái 3 phải 1, trái 5 phải 1, trái 6 phải 0; Close wrap trái 2. Chưa gắn {c('space/xs')}.",
     astryx="Badge gap 4 (<code>design/design.md</code> dòng 322).",
     tokens=[("space/xs", "4", "itemSpacing thân Tag, chấm → chữ 3 cỡ")],
     pv=P4(duo(box([P("3px"), W("5px"), D(), W("1px"), W("5px"), T("Nhãn", "var(--font-size-xs)"), W("5px"), P("3px")], C_M, z=3, r="var(--radius-sm)", cap="Tag MD: nhiều lớp đệm"),
               box([P("var(--space-md)"), D(), G(XS), T("Nhãn", "var(--font-size-xs)"), P("var(--chip-padding-x-md)")], C_M, z=3, r="var(--radius-sm)", cap="Tag MD: hàng phẳng, chấm → chữ 4"))),
     opts=[("flat", "Dựng Tag thành hàng phẳng như Badge: bỏ đệm khung bọc, chấm → chữ 4 ở cả 3 cỡ", True),
           ("gap", "Phẳng nhưng giữ 4 · 6 · 6 bằng space/xs, space/sm", False),
           ("keep", "Giữ khung bọc, gắn token vào từng khung", False)])

item(id="pd08", grp="Chip", title="Ô đếm: ba bộ số cho cùng một ô",
     why=(f"Ô đếm trong <b>Badge</b> đệm ngang <mark>6 · 6 · 6</mark> số trần, {c('design-system/components/base/badge.md')} ghi token \"—\". <b>_Tag count</b> <mark>4 · 5 · 6</mark>. Số trên chuông <b>_Header bell</b> <mark>4</mark>. "
          "Chữ trong ô đều 12. Ô đếm trong Badge SM vì vậy rộng hơn trong Tag SM dù chữ như nhau."),
     untitled=f"Tag <code>px-1 · px-1.25 · px-1.5</code>; Badge không có ô đếm. {c(REF + '/base/tags/tags.tsx')}.",
     ours=f"Badge đệm trần 6; _Tag count {c('space/4')}, trần 5, {c('space/6')}; _Header bell {c('space/xs')}.",
     astryx="Không có ô đếm riêng.",
     pv=P4(duo('<div class="pd-g2">' + box([C("12", "6px")], "16px", z=3, r="var(--radius-xxs)", tone="chip", cap="Badge SM") + box([C("12", "4px")], "18px", z=3, r="var(--radius-xxs)", tone="chip", cap="Tag SM") + "</div>",
               '<div class="pd-g2">' + box([C("12", "var(--space-xs)")], "16px", z=3, r="var(--radius-xxs)", tone="chip", cap="Mọi ô SM, MD: 4") + box([C("12", "var(--space-sm)")], "20px", z=3, r="var(--radius-xxs)", tone="chip", cap="Mọi ô LG: 6") + "</div>")),
     opts=[("one", "Một luật: SM, MD đệm space/xs 4, LG đệm space/sm 6; Tag MD 5 về 4, Badge SM, MD hẹp đi 4", True),
           ("untitled", "Theo Untitled 4 · 5 · 6: ghi 5 vào bảng ngoại lệ, Badge đổi theo", False),
           ("bind", "Giữ số từng nơi, chỉ gắn token: Badge space/sm, Tag như cũ", False)])

item(id="pd09", grp="Điều hướng", title="Tab chip: nhãn → số đếm đo 8, tài liệu ghi 6",
     why=(f"<b>_Tab chip</b> gắn itemSpacing vào <code>tab/gap</code> 8, token này nghĩa \"Giữa 2 tab\". {c('design-system/foundations/spacing.md')} ghi \"nhãn → số đếm 6 (<code>space/sm</code>)\", DEC-161 cũng chốt \"nhãn → số đếm giữ 6\". "
          "Vậy Figma đang sai so với quyết định, và token bị mượn sai vai: đổi khoảng giữa tab sẽ đổi luôn trong tab."),
     untitled=f"<code>gap-1</code> 4, chữ <code>gap-1.5</code> 6 với số. {c(REF + '/application/tabs/tabs.tsx')}.",
     ours=f"<code>tab/gap</code> 8; {c('space/sm')} 6 theo DEC-161.",
     astryx="SegmentedControl gap 4.",
     pv=P4(duo(box([P("var(--tab-padding-x)"), T("Đang chạy"), G("var(--tab-gap)"), T("12", "var(--font-size-xs)"), P("var(--tab-padding-x)")], "36px", r="var(--radius-control)", cap="Theo tab/gap"),
               box([P("var(--tab-padding-x)"), T("Đang chạy"), G("var(--space-sm)"), T("12", "var(--font-size-xs)"), P("var(--tab-padding-x)")], "36px", r="var(--radius-control)", cap="Theo DEC-161"))),
     opts=[("six", "Gắn lại space/sm 6 đúng DEC-161: tab có số hẹp đi 2", True),
           ("eight", "Giữ 8, sửa tài liệu và DEC-161, gắn space/md thay tab/gap", False)])

item(id="pd10", grp="Ô nhập", title="Multi-select, Tags input: lề và cao lệch ô nhập cùng cỡ",
     why=(f"Input, Select Web chữ cách mép <mark>12</mark>; <b>Multi-select</b> Web lớp ngoài 4 + lớp ô 4 = <mark>8</mark>, trong khi Tags input cùng họ vẫn 12. Cao: Multi-select MD <mark>34</mark> (đệm {c('space/4')} × 2 + 24 + viền), Tags input SM <mark>30</mark>, trong khi {c('control/height/md')} 32, {c('control/height/sm')} 28. "
          "Xếp Select và Multi-select cùng hàng trên form sẽ lệch đường chữ 4 và lệch cao 2. Multi-select Platform Mobile đo cao 30, chưa rõ đây là ô thật hay lớp mở sheet, xem giới hạn cuối trang."),
     untitled=f"Dùng chung <code>sizes</code> với Select: <code>py-2 pl-3 pr-2.5 gap-2</code>, <code>py-2 px-3 gap-2</code>, <code>py-2.5 px-3.5 gap-2</code> ({c(REF + '/base/select/select-shared.tsx')}).",
     ours=f"Multi-select: {c('space/xs')} + {c('space/xs')}, trên dưới {c('space/2')}, {c('space/4')}.",
     astryx="Ô nhập cao theo <code>size.element-md</code>; không có Multi-select riêng được đo.",
     pv=P4(duo(box([P(XS), W(XS), T("Chọn trạng thái"), P("var(--space-md)")], "34px", cap="Multi-select MD: 8, cao 34") + box([P("var(--space-md)"), W(XS), T("Chọn trạng thái"), W(XS), P("var(--space-md)")], H_M, cap="Select MD: 12, cao 32"),
               box([P("var(--space-md)"), W(XS), T("Chọn trạng thái"), W(XS), P("var(--space-md)")], H_M, cap="Cả hai: 12, cao theo control/height"))),
     opts=[("align", "Khi chưa có chip: lề 12, cao đúng control/height như Select; có chip thì cao theo nội dung", True),
           ("edge", "Giữ lề 8 để chip sát mép, chỉ sửa cao", False),
           ("keep", "Giữ nguyên", False)])

item(id="pd11", grp="Thẻ", title="Phần đầu thẻ Icon card lề 12 và 20; chân Vehicle Card trên dưới 10",
     why=(f"Radio, Checkbox group item Type <b>Icon card</b>: phần đầu lề trái <mark>12</mark>, phải <mark>20</mark>, trên dưới 12; phần thân ngay dưới lề <mark>16</mark> hai bên. Mép trái icon và mép trái giá không thẳng hàng, lệch 4; ô chọn bên phải cũng lệch 4. "
          f"<b>Vehicle Card</b> chân thẻ trên dưới <mark>10</mark>, thân trên 16, dưới 12, đều số trần; 10 chưa có vai ngoài {c('space/md-lg')} (thêm cho Badge theo DEC-341). DEC-341 chốt lề thẻ 16."),
     untitled="Ref không có thẻ chọn kiểu Icon card, không có Vehicle Card.",
     untitled_none="Ref Untitled không có hai component này",
     ours=f"{c('layout/card-padding')} 16 là lề thẻ; Icon card, Vehicle Card chưa gắn.",
     astryx="Thẻ <code>default: 12px</code>, <code>spacious</code> 20 (<code>design/design.md</code> dòng 494).",
     pv=P4(duo(box([P("12px"), I("truck"), G("12px"), T("Gói vận chuyển"), P("20px")], "60px", r="var(--radius-card)", cap="Phần đầu: 12 và 20") + box([P("16px"), T("1.250.000 ₫"), P("16px")], "60px", r="var(--radius-card)", cap="Phần thân: 16"),
               box([P("var(--layout-card-padding)"), I("truck"), G("var(--space-lg)"), T("Gói vận chuyển"), P("var(--layout-card-padding)")], "60px", r="var(--radius-card)", cap="Phần đầu: 16") + box([P("var(--layout-card-padding)"), T("1.250.000 ₫"), P("var(--layout-card-padding)")], "60px", r="var(--radius-card)", cap="Phần thân: 16"))),
     opts=[("card16", "Phần đầu Icon card lề 16 hai bên theo layout/card-padding; chân Vehicle Card trên dưới space/lg 12, thẻ cao thêm 4", True),
           ("bind", "Giữ số đang vẽ, chỉ gắn token; 12 và 20 ghi ngoại lệ", False)])

item(id="pd12", grp="Gắn token", title=f"{N_BARE} trường lề, khoảng còn số trần",
     why=(f"Trong {N_FIELD} trường đo được, <mark>{N_BARE}</mark> là số trần: Badge 120 (toàn bộ là đệm ô đếm 6), Radio group item 76, Checkbox group item 76, Tag 70, Alert 48, Notification 28, Breadcrumbs 24, Input 23, Vehicle Card và Option Card mỗi bản 14. "
          "Đa số trùng thang (2, 4, 8, 12, 16), đổi được không đổi hình. Ngoài thang: 3, 5 và 1 ở Tag, 10 ở Notification Progress, −1 ở Tooltip (mũi tên chồng khối, giữ). DEC-341 mục sp07 yêu cầu số lề trần đi theo bảng."),
     untitled=f"Mọi lề là bậc thang Tailwind, kể cả nửa bậc <code>px-1.25</code>. {c(REF + '/base/tags/tags.tsx')}.",
     ours=f"Luật: {c('design-system/foundations/spacing.md')} \"số lệch thang phải có tên và lý do hoặc công thức trong bảng ngoại lệ\".",
     astryx="Biến <code>Spacing/*</code>, lề thẻ theo <code>{spacing.3}</code>.",
     pv_none="Việc gắn biến không đổi hình; số đo từng set nằm ở bảng Gắn token phía trên.",
     opts=[("sweep", "Một lượt gắn hết số trùng thang, số ngoài thang ghi bảng ngoại lệ: nhìn không đổi", True),
           ("sync", "Gắn dần khi mỗi component tới lượt sync", False)])

item(id="pd13", grp="Gắn token", title=f"{N_PRIM} trường gắn thẳng primitive",
     why=(f"User đã chốt mọi token vai trỏ thang Semantic, không trỏ primitive; trong {c('design-system/tokens.json')} điều này đã đúng. Trên layer còn <mark>{N_PRIM}</mark> trường gắn thẳng: _Tag close X {c('space/2')} 8, Card header {c('space/20')} 6, _Tag count {c('space/4')}, {c('space/6')} 4, Multi-select {c('space/2')}, {c('space/4')} 4, Toggle label {c('space/2')} 4, Badge {c('space/2')} 2. "
          "Các nơi này đổi tên được không đổi số."),
     untitled=f"Component gọi lớp Semantic. {c('design/_ref/untitled-ui/04-spacing-radius-grid.md')}: \"Thang giới hạn, suy từ primitive, dùng cho gap/padding/margin trong component\".",
     ours=f"{c('design-system/foundations/spacing.md')}: \"Component còn gọi Primitive sửa khi sync\" (DEC-341 mục sp02).",
     astryx="Không phân lớp này.",
     pv_none="Đổi biến gắn, số và hình giữ nguyên, không có gì để xem thử.",
     opts=[("now", "Đổi ngay sang thang Semantic cùng số: space/xxs, space/xs, space/sm, space/2xl", True),
           ("sync", "Giữ theo DEC-341: sửa khi từng component sync", False)])

item(id="pd14", grp="Thông báo", title="Tooltip ngắn 8 × 4, Untitled 12 × 8",
     why=(f"Tooltip Short lề ngang <mark>8</mark>, dọc <mark>4</mark>; Supporting 12 và 8 (DEC-206, {c('design-system/components/base/tooltip.md')}). Untitled cao hơn hẳn. Web điều vận dày dữ liệu, tooltip thường nằm trên ô bảng và nút icon, nên gọn là có lợi; app không có hover. Mở mục này để bạn thấy khác biệt, không có lỗi."),
     untitled=f"<code>px-3</code>, <code>py-2</code>, có mô tả <code>py-3</code>. {c(REF + '/base/tooltip/tooltip.tsx')}.",
     ours=f"{c('space/md')} × {c('space/xs')}; {c('space/lg')} × {c('space/md')}.",
     astryx="Tooltip Astryx chưa đo ở lượt này.",
     pv=P4(duo(box([P("var(--space-md)"), T("Sửa lệnh", "var(--font-size-xs)"), P("var(--space-md)")], "24px", cap="Short: 8 × 4"),
               box([P("var(--space-lg)"), T("Sửa lệnh", "var(--font-size-xs)"), P("var(--space-lg)")], "32px", cap="Nếu theo Untitled: 12 × 8"))),
     opts=[("keep", "Giữ 8 × 4 cho web dày dữ liệu", True), ("untitled", "Theo Untitled 12 × 8: tooltip cao thêm 8", False)])

item(id="pd15", grp="Điều hướng", title="SegmentedControl thư viện cũ: chỉ icon không vuông",
     why=("Mọi nút chỉ icon của bộ mới đều vuông (28, 32, 40, 36, 44, 24). Riêng <b>SegmentedControl</b> Content Icon Only đo <mark>32 × 24 · 40 × 28 · 40 × 32</mark>, lề 8 · 12 · 12 và còn dùng <code>Spacing/2</code>, <code>Spacing/3</code> của thư viện Astryx. "
          "Set này nằm trên trang DS · Application components nhưng bộ mới chưa dựng Segmented. _Button group item chỉ có bản chữ, chưa có bản chỉ icon."),
     untitled=f"Button group chỉ icon <code>data-icon-only:px-2.5</code> trên cỡ 36, gần vuông. {c(REF + '/base/button-group/button-group.tsx')}.",
     ours=f"Chưa có tài liệu trong {c('design-system/components/README.md')} cho Segmented.",
     astryx="SegmentedControl 43:250616 chính là bản đo được.",
     pv=P4(duo(box([P("var(--space-md)"), I(), P("var(--space-md)")], "24px", cap="Hiện tại SM 32 × 24"),
               box([P("var(--space-xs)"), I(), P("var(--space-xs)")], "24px", cap="Vuông SM 24 × 24"))),
     opts=[("later", "Không sửa set cũ; khi cần Segmented thì dựng theo _Button group item, chỉ icon vuông", True),
           ("square", "Sửa set cũ thành vuông ngay", False)])

# ---------- Auto layout còn lại: flow, resizing, alignment, gap. Đo 02/11, 53 set, tối đa 80 biến thể mỗi set, không tính lớp trong instance ----------
# phần, component, Untitled, mình, trạng thái, ghi chú, nguồn [(file, dòng, chuỗi)]
CHK, RAD, TOG = "base/checkbox/checkbox.tsx", "base/radio-buttons/radio-buttons.tsx", "base/toggle/toggle.tsx"
TGI, MSL, TXA = "base/input/input-tags.tsx", "base/select/multi-select.tsx", "base/textarea/textarea.tsx"
FUP, NAVI, AVL = "application/file-upload/file-upload-base.tsx", "application/app-navigation/base-components/nav-item.tsx", "base/avatar/avatar-label-group.tsx"
N_GAP_BARE = 365  # Tooltip 12, Radio 104, Checkbox 104, Breadcrumbs 15, Segmented 18, Vehicle 28 + 14 + 27 + 15, Combo 4, Notification 8, Alert 16
AL = [
    ("Flow", "Mọi set", "—", "Không có khung nào có từ 2 phần tử hiện mà thiếu auto layout", OK, "Đếm trên 53 set", []),
    ("Flow", "Button", "Ngang, <code>inline-flex</code>", "Ngang", OK, "", [(BTN, 13, "inline-flex")]),
    ("Flow", "Input, Select: nhãn, ô, gợi ý", "Dọc, <code>flex-col</code>", "Dọc", OK, "", [(INP, 221, "flex-col"), ("base/select/select.tsx", 123, "flex-col")]),
    ("Flow", "Chữ trong Radio, Checkbox", "Dọc, <code>flex-col</code>", "Dọc", OK, "", [(CHK, 115, "flex-col"), (RAD, 104, "flex-col")]),
    ("Flow", "Tags input", "Xuống hàng, <code>flex-wrap</code>", "Xuống hàng", OK, "", [(TGI, 230, "flex-wrap"), (TGI, 234, "flex-wrap")]),
    ("Flow", "Select item: nhãn + mô tả", "Xuống hàng khi chật, <code>flex-wrap</code>", "2 hàng cố định Line 1, Line 2", NOTE, "Chưa có mục chọn, đề xuất giữ", [(ITM, 112, "flex-wrap")]),
    ("Flow", "Lớp đè: vòng focus, viền, thanh tiến độ", "Ngoài luồng, <code>before:absolute</code>", "Ngoài luồng", OK, "Focus ring, Border, Resize handle, Timer, Progress, Status", [(BTN, 13, "before:absolute")]),
    ("Flow", "_Nav item, Vehicle Card: khung rỗng", "Lùi bằng lề, <code>pl-10</code>", "Khung rỗng <code>Indent</code>, <code>Gap</code>", GAP, "Mục al00", [(NAVI, 119, "pl-10")]),
    ("Resizing", "Button", "Rộng và cao theo nội dung, <code>h-max</code>", "Rộng theo nội dung, cao cố định", DIFF, "Cao đi theo token control", [(BTN, 13, "h-max")]),
    ("Resizing", "Input, Select", "Chiếm hết chiều ngang, <code>w-full</code>", "Rộng cố định, cao theo nội dung", DIFF, "Instance đặt Fill khi đưa vào màn", [(INP, 102, "w-full"), ("base/select/select.tsx", 53, "w-full")]),
    ("Resizing", "Dropdown item: nhãn", "Giãn và cắt, <code>grow truncate</code>", "Fill, cắt 1 dòng", OK, "", [(DRP, 111, "grow truncate")]),
    ("Resizing", "Avatar label", "<code>min-w-0 flex-1</code>, cắt", "Fill, cắt 1 dòng", OK, "", [(AVL, 28, "min-w-0 flex-1"), (AVL, 32, "truncate")]),
    ("Resizing", "Select item: nhãn", "<code>min-w-0 flex-1</code>, <code>truncate</code>", "Hug. Thử rộng 240: chữ dài 760, tràn khỏi dòng", GAP, "Mục al01", [(ITM, 112, "min-w-0 flex-1"), (ITM, 113, "truncate")]),
    ("Resizing", "_Search result: tiêu đề, đường dẫn", "Ref không có", "Hug. Thử rộng 240: chữ dài 760 và 647, tràn", GAP, "Mục al01", []),
    ("Resizing", "Card header: tiêu đề", "Ref không có", "Hug, tối đa 300. Thử rộng 240: tràn, mô tả bị ép còn 18", GAP, "Mục al01", []),
    ("Resizing", "_Multi-select item: nhãn", "Dùng Select item, <code>truncate</code>", "Xuống 5 dòng, dòng cao 116", GAP, "Mục al02", [(MSL, 24, "import { SelectItem }"), (ITM, 113, "truncate")]),
    ("Resizing", "Badge, Tag, _Tab chip: nhãn", "Badge rộng theo chữ, <code>size-max</code>, không cắt", "Hug, tối đa 160 rồi cắt. Đã thử: đúng", NOTE, "Chưa có mục chọn, đề xuất giữ", [(BDG, 80, "size-max")]),
    ("Resizing", "Tooltip", "Tối đa 320, <code>max-w-xs</code>", "Short 240, Supporting 320", DIFF, "Mục al03", [(TIP, 71, "max-w-xs")]),
    ("Resizing", "Input, Select: hàng nhãn", "Không giới hạn", "Tối đa 320, ô App rộng được 361", GAP, "Mục al03", []),
    ("Resizing", "_Nav item, _Nav tenant switch: nhãn", "<code>flex-1</code>, <code>truncate</code>", "Cắt được, nhưng dùng kiểu cũ <code>TRUNCATE</code>", GAP, "Mục al04", [(NAVI, 79, "flex-1"), (NAVI, 80, "truncate")]),
    ("Alignment", "Button", "Giữa hai trục, <code>items-center justify-center</code>", "Giữa hai trục", OK, "", [(BTN, 13, "items-center justify-center")]),
    ("Alignment", "Radio, Toggle, Checkbox Web", "Canh trên, <code>items-start</code>", "Canh trên", OK, "", [(RAD, 87, "items-start"), (CHK, 97, "items-start"), (TOG, 117, "items-start")]),
    ("Alignment", "Checkbox App", "Canh trên, <code>items-start</code>", "Canh giữa", GAP, "Mục al05", [(CHK, 97, "items-start")]),
    ("Alignment", "Select item, Dropdown item", "Canh giữa dọc, <code>items-center</code>", "Canh giữa dọc", OK, "", [(ITM, 89, "items-center"), (DRP, 94, "items-center")]),
    ("Alignment", "Input, Select: khối dọc", "Canh trái, <code>items-start</code>", "Canh trái", OK, "", [(INP, 221, "items-start")]),
    ("Alignment", "Avatar label", "Canh giữa dọc, <code>items-center</code>", "Canh giữa dọc", OK, "", [(AVL, 28, "items-center")]),
    ("Alignment", "_File row", "Canh trên, <code>flex</code> mặc định", "Canh trên", OK, "", [(FUP, 267, "relative flex gap-3")]),
    ("Alignment", "Chữ trong mọi set", "Canh trái, <code>text-left</code>", "Canh trái", OK, "Nút căn giữa bằng khung, không bằng chữ", [("base/select/select.tsx", 61, "text-left")]),
    ("Gap", "Nhãn → ô → gợi ý", "6, <code>gap-1.5</code>", "4", GAP, "Mục al06", [(INP, 221, "gap-1.5"), ("base/select/select.tsx", 123, "gap-1.5"), (TGI, 211, "gap-1.5"), (MSL, 211, "gap-1.5"), (TXA, 100, "gap-1.5")]),
    ("Gap", "Dòng trong menu", "2, mỗi dòng <code>py-px</code>", "0, nền hover hai dòng chạm nhau", GAP, "Mục al07", [(DRP, 85, "py-px"), (ITM, 83, "py-px")]),
    ("Gap", "Chip trong Tags input", "6, <code>gap-1.5</code>", "4", NOTE, "Chưa có mục chọn, đề xuất giữ", [(TGI, 234, "gap-1.5")]),
    ("Gap", "Nhãn → gợi ý trong Radio, Checkbox", "SM 0, MD 2, <code>gap-0.5</code>", "SM 0, MD 2", OK, "", [(RAD, 76, "gap-0.5"), (CHK, 86, "gap-0.5")]),
    ("Gap", "Tooltip: tiêu đề → mô tả", "4, <code>gap-1</code>", "4", OK, "", [(TIP, 71, "gap-1")]),
    ("Gap", "_File row: dòng thông tin", "8 và 4, <code>gap-2</code>, <code>gap-1</code>", "8 và 4", OK, "", [(FUP, 280, "gap-2"), (FUP, 285, "gap-1")]),
    ("Gap", "_File row: tên → thông tin", "2, <code>mt-0.5</code>", "1, ngoài thang", GAP, "Mục al08", [(FUP, 280, "mt-0.5")]),
    ("Gap", "Tab gạch dưới: giữa các tab", "12, <code>gap-3</code>", "20", NOTE, "Chưa có mục chọn, đề xuất giữ", [(TAB, 80, "gap-3")]),
    ("Gap", "Gắn biến", "Không dùng token theo vai", f"{N_GAP_BARE} gap số trần", GAP, "Mục al08, cùng nhóm pd12", []),
]
for _r in AL:
    for _f, _l, _t in _r[6]:
        _ls = UB_FILES.setdefault(_f, (kit.ROOT / REF / _f).read_text(encoding="utf-8").splitlines())
        assert _t in _ls[_l - 1], f"Untitled đổi nguồn: {_f}:{_l} không còn {_t!r}"
AL_N = {k: sum(1 for r in AL if r[4] == k) for k in LAB}
AL_FAMS = list(dict.fromkeys(r[0] for r in AL))


def al_table():
    head = "".join(f"<th>{h}</th>" for h in ["Phần", "Component", "Untitled", "Mình", "Trạng thái", "Dòng nguồn"])
    body = []
    for r in AL:
        src = "<br>".join(f"<code>{f}:{l}</code>" for f, l in sorted({(f, l) for f, l, _ in r[6]})) or '<span class="muted">—</span>'
        note = f'<br><span class="small muted">{r[5]}</span>' if r[5] else ""
        body.append(f'<tr data-c="{r[0]}"><td>{r[0]}</td><td><b>{r[1]}</b></td><td class="small">{r[2]}</td><td class="small">{r[3]}</td><td><span class="{r[4]}">{LAB[r[4]]}</span>{note}</td><td class="small muted">{src}</td></tr>')
    btns = '<button data-f="all" aria-pressed="true">Tất cả</button>' + "".join(f'<button data-f="{f}" aria-pressed="false">{f}</button>' for f in AL_FAMS)
    return f'<div class="pd-fb">{btns}</div><div class="tw"><table class="cmp pd-main al-main"><thead><tr>{head}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def _row(w, text, cut=False, over=False, h=36):
    cls = "al-cut" if cut else ("al-over" if over else "")
    return f'<div class="al-row" style="width:{w}px;min-height:{h}px"><span class="al-ic"></span><span class="al-tx {cls}">{text}</span></div>'


LONG_TX = "Cảng Cát Lái, cổng B, kho lạnh số 3, tuyến Long An"
# ---------- Bảng phụ ----------

item(id="al00", grp="Flow", title="Khung rỗng làm khoảng cách: Indent trong _Nav item, Gap trong Vehicle Card",
     why=("<b>_Nav item</b> dạng Child có một khung rỗng tên <code>Indent</code> để lùi chữ; <b>Vehicle Card</b> có khung rỗng tên <code>Gap</code> đặt giữa hai phần tử. Mỗi cái đo được trên 4 biến thể. "
          "Khung rỗng là khoảng cách không gắn được vào lề hay gap, dev đọc Figma sẽ dựng thêm một thẻ thừa. <code>Indicator</code> của <b>_Header tab</b> cũng rỗng ở trạng thái thường nhưng là gạch chân khi chọn, không tính."),
     untitled=f"Mục con lùi bằng lề: <code>py-2 pr-3 pl-10</code> ({c(REF + '/application/app-navigation/base-components/nav-item.tsx')}), không có khung rỗng.",
     ours=f"<code>Indent</code> set 6768:192076, <code>Gap</code> set 6791:13702, {c('design-system/components/application/vehicle-card.md')}.",
     pv_none="Nhìn không đổi, chỉ đổi cách dựng lớp.",
     astryx="Không đối chiếu ở mục này.",
     opts=[("replace", "Bỏ khung rỗng: Indent thành lề trái, Gap thành khoảng của khung cha; nhìn không đổi", True),
           ("keep", "Giữ nguyên", False)])

item(id="al01", grp="Resizing", title="Chữ dài tràn khỏi dòng: Select item, _Search result, Card header",
     why=("Cả ba đặt nhãn <b>Hug</b> kèm cờ cắt 1 dòng. Figma ghi rõ chữ tự rộng thì cờ cắt không có tác dụng nếu không có giới hạn. Mình <mark>đã thử bằng instance tạm rộng 240 rồi xoá</mark>: "
          "Select item chữ rộng 760 tràn khỏi dòng, _Search result 760 và 647, Card header tiêu đề tối đa 300 vẫn tràn và ép mô tả còn 18. Badge, Tag, _Tab chip có giới hạn 160 nên cắt đúng, không nằm trong mục này."),
     untitled=f"<code>min-w-0 flex-1</code> và <code>truncate</code> ({c(REF + '/base/select/select-item.tsx')}). Ref không có _Search result, Card header.",
     ours="Nhãn Hug, <code>maxLines</code> 1, không có chiều rộng tối đa trong khung cha.",
     astryx="Không đối chiếu ở mục này.",
     note="Mới thử biến thể mặc định của từng set, chưa thử Select item dạng Supporting và Rich.",
     pv=P4(duo(_row(240, LONG_TX, over=True), _row(240, LONG_TX, cut=True))),
     opts=[("fill", "Nhãn đổi sang Fill, cắt 1 dòng như Untitled; chữ ngắn nhìn không đổi", True),
           ("max", "Giữ Hug, thêm chiều rộng tối đa theo từng set", False),
           ("keep", "Giữ nguyên, ghi luật màn phải tự giới hạn chữ", False)])

item(id="al02", grp="Resizing", title="_Multi-select item xuống nhiều dòng, Select item thì cắt",
     why=("Cùng là dòng chọn trong danh sách nhưng <b>_Multi-select item</b> không bật cắt: thử rộng 240 với chữ dài, nhãn <mark>xuống 5 dòng, dòng cao 116</mark>, so với 36 lúc thường. Danh sách đang đều nhịp sẽ lệch hẳn."),
     untitled=f"Multi-select dùng lại Select item, nhãn <code>truncate whitespace-nowrap</code> ({c(REF + '/base/select/select-item.tsx')}).",
     ours=f"Nhãn Fill, cao theo nội dung, không giới hạn dòng. Set 6658:190134, {c('design-system/components/_work/multiselect')}.",
     astryx="Không đối chiếu ở mục này.",
     pv=P4(duo(_row(240, LONG_TX), _row(240, LONG_TX, cut=True))),
     opts=[("cut", "Cắt 1 dòng như Select item và Untitled", True),
           ("two", "Cho tối đa 2 dòng rồi cắt, đọc được nhiều hơn nhưng dòng cao không đều", False),
           ("keep", "Giữ xuống dòng tự do", False)])

item(id="al03", grp="Resizing", title="Giới hạn rộng: hàng nhãn ô nhập 320, Tooltip ngắn 240",
     why=("Hàng nhãn của <b>Input</b>, <b>Select</b> có tối đa 320 trong khi ô App rộng được 361: nhãn dài có thể bị giới hạn sớm hơn ô bên dưới. <b>Tooltip</b> Short tối đa 240, Supporting 320."),
     untitled=f"Tooltip một số <code>max-w-xs</code> 320 cho cả hai dạng ({c(REF + '/base/tooltip/tooltip.tsx')}). Nhãn không có giới hạn riêng ({c(REF + '/base/input/label.tsx')}).",
     ours=f"Label row tối đa 320; Tooltip Content 240 và 320, {c('design-system/components/base/tooltip.md')}.",
     pv_none="Chỉ đổi giới hạn khi chữ rất dài, chữ thường nhìn không đổi.",
     astryx="Không đối chiếu ở mục này.",
     opts=[("label", "Bỏ giới hạn hàng nhãn, cho rộng theo ô; Tooltip giữ 240 và 320", True),
           ("both", "Bỏ giới hạn hàng nhãn, Tooltip một số 320 như Untitled", False),
           ("keep", "Giữ cả hai", False)])

item(id="al04", grp="Resizing", title="Nhãn _Nav item dùng kiểu cắt cũ TRUNCATE",
     why=("<b>_Nav item</b> và <b>_Nav tenant switch</b> dùng <code>textAutoResize = TRUNCATE</code>. Tài liệu Plugin API ghi kiểu này <mark>đã lỗi thời và sẽ bị bỏ</mark>. Hiện vẫn cắt đúng; các set khác dùng cao theo nội dung kèm tối đa 1 dòng."),
     untitled=f"<code>flex-1</code>, <code>truncate</code> ({c(REF + '/application/app-navigation/base-components/nav-item.tsx')}).",
     ours=f"Label 16 và 4 biến thể đã đo, {c('design-system/components/application/sidebar-navigation.md')}.",
     pv_none="Nhìn không đổi, chỉ đổi thuộc tính chữ.",
     astryx="Không đối chiếu ở mục này.",
     opts=[("modern", "Đổi sang cao theo nội dung, tối đa 1 dòng như các set khác; nhìn không đổi", True),
           ("keep", "Để tới khi Figma bỏ hẳn", False)])

item(id="al05", grp="Alignment", title="Checkbox App canh giữa, các ô chọn còn lại canh trên",
     why=("<b>Checkbox label</b> Platform Mobile có 9 biến thể canh giữa dọc; Checkbox Web, Radio, Toggle đều canh trên. Nhãn 2 dòng trở lên thì ô chọn trên App trôi xuống giữa khối chữ, lệch khỏi dòng đầu."),
     untitled=f"<code>relative flex items-start</code> ({c(REF + '/base/checkbox/checkbox.tsx')}).",
     ours=f"Set 6658:191113, Platform=Mobile, {c('design-system/components/_work/form-controls')}.",
     astryx="Không đối chiếu ở mục này.",
     pv=P4(duo('<div class="al-ck" style="align-items:center"><i></i><span>Xác nhận đã kiểm tra niêm phong container trước khi rời cảng và ký biên bản</span></div>',
               '<div class="al-ck" style="align-items:flex-start"><i></i><span>Xác nhận đã kiểm tra niêm phong container trước khi rời cảng và ký biên bản</span></div>')),
     opts=[("top", "Canh trên như Checkbox Web, Radio, Toggle và Untitled", True),
           ("keep", "Giữ canh giữa trên App", False)])

item(id="al06", grp="Gap", title="Nhãn → ô → gợi ý: mình 4, Untitled 6",
     why=(f"<b>Input</b>, <b>Select</b>, <b>Tags input</b>, <b>Multi-select</b>, <b>Textarea</b> đều 4, gắn {c('space/xs')}. {c('design-system/foundations/spacing.md')} ghi \"ô → dòng gợi ý 4\" (DEC-184), nên đây là số đã chọn, không phải lỗi. Đổi sang 6 thì <mark>mỗi ô đủ nhãn và gợi ý cao thêm 4</mark>, form dài hơn."),
     untitled=f"<code>gap-1.5</code> 6 ở cả 5 set ({c(REF + '/base/input/input.tsx')}, {c(REF + '/base/select/select.tsx')}).",
     ours=f"{c('space/xs')} 4.",
     astryx="Không đối chiếu ở mục này.",
     pv=P4(duo('<div class="al-fd" style="gap:var(--space-xs)"><b>Mã container</b><span class="al-in">TCLU 482915-3</span><small>11 ký tự, gồm 4 chữ và 7 số</small></div>',
               '<div class="al-fd" style="gap:var(--space-sm)"><b>Mã container</b><span class="al-in">TCLU 482915-3</span><small>11 ký tự, gồm 4 chữ và 7 số</small></div>')),
     opts=[("six", "Đổi sang space/sm 6 như Untitled, form cao thêm", True),
           ("four", "Giữ 4, form gọn hơn; ghi là khác Untitled có chủ đích", False)])

item(id="al07", grp="Gap", title="Dòng menu dính nhau: mình 0, Untitled cách 2",
     why=("<b>Dropdown menu</b> đặt gap 0 giữa các dòng. Khi di chuột, nền hover và nền dòng đang chọn <mark>chạm nhau</mark>. Lề trong menu Web 4 đều bốn phía."),
     untitled=f"Mỗi dòng <code>py-px</code>, nên hai dòng cách 2; khung dòng <code>px-1.5</code> 6 ({c(REF + '/base/dropdown/dropdown.tsx')}).",
     ours=f"Set 6819:112227: Web lề 4, gap 0; Mobile lề 8, 8, 16, 8, gap 0. Dòng cùng họ với {c('design-system/components/_work/select')}.",
     astryx="Không đối chiếu ở mục này.",
     pv=P4(duo('<div class="al-mn" style="gap:0"><span class="on">Sửa lệnh</span><span class="on2">Nhân bản lệnh</span><span>Huỷ lệnh</span></div>',
               '<div class="al-mn" style="gap:var(--space-xxs)"><span class="on">Sửa lệnh</span><span class="on2">Nhân bản lệnh</span><span>Huỷ lệnh</span></div>')),
     opts=[("two", "Web gap space/xxs 2 như Untitled; menu 4 dòng cao thêm 6. App giữ 0 vì dòng cao 52", True),
           ("both", "Cả Web và App cùng gap 2", False),
           ("keep", "Giữ 0", False)])

item(id="al08", grp="Gap", title=f"{N_GAP_BARE} gap số trần và 3 số lệch thang",
     why=(f"Đếm trên biến thể đã đo: <mark>{N_GAP_BARE} gap không gắn biến</mark>, nhiều nhất ở Radio, Checkbox group item 104 mỗi set, Vehicle Card và Vehicle Option Card. Số lệch thang: <b>_File row</b> tên → thông tin 1; <b>Notification</b> 10 số trần; <b>Tooltip</b> −1 để mũi tên chồng lên khung."),
     untitled=f"<code>mt-0.5</code> 2 ở _File row ({c(REF + '/application/file-upload/file-upload-base.tsx')}). Tailwind ghi thẳng, không dùng token theo vai.",
     ours=f"Cùng nhóm với pd12, nhưng pd12 đếm trên biến thể mặc định của 38 set nên hai số không cộng được. {c('design-system/components/base/alert-notification.md')}.",
     pv_none="Gắn biến không đổi hình; chỉ _File row đổi 1 thành 2, khó thấy ở cỡ xem thử.",
     astryx="Không đối chiếu ở mục này.",
     opts=[("bind", "Gắn hết vào thang; _File row 1 thành 2, Notification 10 gắn space/md-lg; Tooltip −1 ghi ngoại lệ", True),
           ("later", "Làm khi sync từng component, không làm một đợt", False),
           ("keep", "Giữ số trần", False)])


AUDIT_ROWS = [[f"<b>{a[1]}</b>", a[0], f"n:{a[2] or '–'}", f"n:{a[3] or '–'}", f"n:{a[4] or '–'}", f"n:{a[5] or '–'}", f"n:{a[6] or '–'}"] for a in AUDIT if a[2] or a[3] or a[6]]
AUDIT_ROWS.append(["<b>Tổng 38 set</b>", "", f"n:{N_BARE}", f"n:{N_PRIM}", f"n:{N_SEM}", f"n:{N_ROLE}", f"n:{N_ORPH}"])

PROP = rows(["Nhóm", "Phía chữ", "Phía icon, chấm", "Icon, chấm → chữ", "Chỉ icon", "Mục"], [
    ["<b>Button Web</b> SM · MD · LG", "n:10 · 12 · 16", "n:8 · 10 · 14", "n:6", "vuông 28 · 32 · 40", "pd00, pd01, pd02"],
    ["<b>Button App</b> SM · MD · LG", "n:12 · 16 · 24", "n:8 · 12 · 20", "n:8", "vuông 36 · 44 · 52", "pd01, pd02"],
    ["<b>Badge</b> SM · MD · LG", "n:8 · 10 · 12", "n:6 · 8 · 10", "n:4", "—", "Đã chốt"],
    ["<b>Tag</b> SM · MD · LG", "n:8 · 10 · 12", "n:6 · 8 · 10", "n:4", "—", "pd06, pd07"],
    ["<b>Ô đếm</b> SM, MD · LG", "n:4 · 6", "—", "—", "—", "pd08"],
    ["<b>Input, Select, Multi-select Web</b>", "n:12", "n:8", "n:8", "—", "pd10"],
    ["<b>Input, Select App</b>", "n:16", "n:16", "n:16", "—", "DEC-341"],
    ["<b>Dòng menu</b> Web · App", "n:8 · 12", "n:8 · 12", "n:8", "—", "pd03, pd04"],
    ["<b>Radio</b> ô 16 · 20", "—", "—", "chấm 6 · 8", "—", "pd05"],
    ["<b>Thẻ</b>", "n:16", "n:16", "n:12", "—", "pd11"],
    ["<b>Tab chip App</b>", "n:16", "n:12", "nhãn → số 6", "—", "pd09"],
])

SPEC = dict(
    slug="padding", short="phần Auto layout component",
    title="Foundations · Auto layout component — padding, flow, resizing, alignment, gap",
    subtitle="Foundation riêng, tách khỏi Khoảng cách · 5 phần của auto layout · Untitled UI v8 làm base · đo trên Figma · chọn từng mục · 02/11/2026",
    lead=(f"Trang này rà đủ 5 phần auto layout của component: <b>padding</b>, <b>flow</b>, <b>resizing</b>, <b>alignment</b>, <b>gap</b>. Padding đo {N_SETS} set; bốn phần còn lại đo 53 set, <a href='#al-base'>xem bảng</a>: {AL_N[OK]} giống, {AL_N[GAP]} lệch, <b>chữ dài tràn ở 3 set</b>. "
          f"So với <a href='#ub-base'>base Untitled</a>: <b>{UB_OK}/{UB_N} số khớp</b>. Kết luận chính: nút và ô nhập ổn ở App nhưng <b>Web còn hai số lệch token</b>; <b>dòng menu bị DEC-341 kéo giãn ngoài ý muốn</b>; <b>{N_ORPH} trường gắn biến treo</b>. <mark>Chưa sửa token, Figma nào.</mark>"),
    kpis=[(f"{UB_OK}/{UB_N}", "số padding khớp Untitled", ""), (f"{AL_N[OK]}/{len(AL)}", "dòng flow, resizing, alignment, gap giống", ""), (str(N_SETS), "set đã đo", ""), (str(len(R)), "dạng trong bảng đo", ""), (str(ST_N[GAP]), "dạng lệch cần chọn", "bad"), (str(ST_N[OK]), "dạng giống Untitled", "ok"),
          (str(N_BARE), "trường số trần", "bad"), (str(N_PRIM), "trường gắn primitive", "bad"), (str(N_ORPH), "trường gắn biến treo", "bad")],
    tag_kind="spacing",
    screens=dict(
        intro=(f"Màn mẫu dựng từ biến thật. Bộ <b>Sau khi đổi</b> áp chip lề đúng {c('chip/padding-x-sm')} hai bên (đã chốt). Bật Nhãn số đo để đọc lề khung từ trình duyệt."),
        proposal_css=".tp-f.tp-prop .tp-chip{padding:0 var(--chip-padding-x-sm)}",
        logo_svg=None, gridov=False, overlay_html=None),
    sections=[
        dict(title="Base so sánh: padding của Untitled",
             intro=(f"Số Untitled đọc từ mã nguồn <code>{REF}/</code>, bản React v8, đổi lớp Tailwind ra px (1 đơn vị = 4px). Khi dựng trang, máy kiểm từng lớp còn đúng ở dòng ghi bên phải; nguồn đổi thì trang không dựng được. "
                    f"Mỗi ô: số trên là Untitled, số dưới là mình. So theo cùng cao, Untitled không có cỡ 28 và không có bản App, nên Button App chỉ là so gần. Tổng <b>{UB_OK}/{UB_N} số khớp</b>. "
                    "Ref đã lưu không có Alert, Notification, Breadcrumbs, thẻ chọn, Vehicle."),
             html=base_table()),
        dict(title="Untitled và mình đặt cạnh nhau, đúng tỉ lệ", intro="Cả hai bên dùng số px thật, không qua biến, phóng cùng tỉ lệ. Chỉ Web, vì Untitled không có bản App.", html=UB_VIEW),
        dict(title="Flow, resizing, alignment, gap so với Untitled",
             intro=(f"Đo ngày 02/11 trên 53 set, tối đa 80 biến thể mỗi set, không tính lớp trong instance. Cột Untitled đọc từ mã nguồn, máy kiểm từng lớp khi dựng. Có {AL_N[OK]} Giống · {AL_N[DIFF]} Khác có lý do · {AL_N[NOTE]} Khác, chưa rõ lý do · {AL_N[GAP]} Lệch, cần chọn. "
                    "Số thử chữ dài lấy từ instance tạm trên trang Sandbox, rộng 240, đã xoá ngay sau khi đo."),
             html='<div id="al-base"></div>' + al_table()),
        dict(title="Bảng đối chiếu theo dạng nội dung — Untitled ↔ mình",
             intro=(f"Số đo Figma ngày 02/11, Web trừ khi ghi App; \"8 + 4\" là lớp ngoài cộng khung bọc. Trạng thái: {ST_N[OK]} Giống · {ST_N[DIFF]} Khác có lý do · {ST_N[GAP]} Lệch, cần chọn · {ST_N[OWN]} Chỉ mình có. "
                    f"Nhãn <span class=\"pd-flag\">đo khác</span>: trang ghi số theo quyết định đã chốt, Figma đo ra số khác, xem section Đã chốt. Nguồn Untitled: <code>{REF}/</code>."),
             html=main_table()),
        dict(title="Sơ đồ đúng tỉ lệ từng dạng",
             intro="Mỗi khung phóng theo đúng tỉ lệ. Nhìn hai bên nút có icon và Badge có chấm: lề phía icon nhỏ hơn lề phía chữ (bù quang học). Tag, Input có vùng tím là đệm nằm trong khung bọc, nhìn trên Figma dễ bỏ sót.",
             html=HERO),
        dict(title="Gắn token: số trần, primitive, biến treo",
             intro=(f"Đếm trên biến thể mặc định, tối đa 60 biến thể mỗi set Base, 40 mỗi set Application, không tính lớp trong instance, chỉ các set đã đếm ({len(AUDIT)} set). Tổng {N_FIELD} trường; dưới đây chỉ liệt kê set có vấn đề. "
                    "Biến treo: layer còn gắn, Figma còn đọc ra số, nhưng biến không còn trong danh sách của collection."),
             html=rows(["Set", "Trang", "Số trần", "Primitive", "Thang Semantic", "Token vai", "Biến treo"], AUDIT_ROWS)),
        dict(title="Đã chốt, không mở lại",
             intro="Không thành câu hỏi. Ô Đo Figma ghi số thật lúc dựng trang; chỗ khác quyết định cần agent sửa Figma, không cần bạn chọn.",
             html=rows(["Nguồn", "Đã chốt", "Đo Figma 02/11"], [
                 ["User 02/11", "Badge <b>không chấm, không icon</b>: lề trái = phải <b>8 · 10 · 12</b>", f"{FLAG} Trái 6 · 8 · 10, phải 8 · 10 · 12: tắt <code>Has Dot</code> thì lề khung ngoài không đổi theo"],
                 ["User 02/11", "Badge <b>có chấm hoặc icon</b>: trái <b>6 · 8 · 10</b>, phải 8 · 10 · 12", "Khớp"],
                 ["DEC-341", "Chấm → chữ 4, khung chấm không đệm phải; thêm <code>space/md-lg</code> 10", "Khớp: Dot wrap rộng 6, khoảng 4"],
                 ["DEC-341 · <code>design-system/components/base/badge.md</code>", "Count Only đệm trái khung số 2 → số cách đều 8 · 10 · 12", f"{FLAG} Count only wrap đệm 4, nên trái 10 · 12 · 14"],
                 ["User 02/11", "Bỏ hẳn đường K, không còn luật chữ theo cột", "Chưa đo đường canh; trang này không dùng luật đó"],
                 ["User 02/11, DEC-341", "Mọi token vai trỏ thang Semantic, không trỏ primitive", f"Đúng trong <code>tokens.json</code>; trên layer còn {N_PRIM} trường gắn thẳng: mục pd13"],
                 ["DEC-341", "Lề thẻ 16; ô nhập gán thẳng theo khối Web, App; <code>form/field-gap</code> 16", "Khớp ở Input, Select App"],
                 ["DEC-339", "Vùng chạm bù bằng lớp <code>::after</code> dùng chung, sàn Web 24, App 44", "Không tính vào lề; đề xuất trang này không đổi cao nút"],
                 ["DEC-329", "Icon 12 · 14 · 16 · 20; icon không cao hơn dòng chữ", "Input icon 14, Select icon 16: lệch ngoài phạm vi trang, ghi lại để soi ở sync"],
                 ["DEC-328", "Bo góc một bộ cho Web và App", "Không đổi ở trang này"],
                 ["DEC-324", "Lề màn, lưới, độ rộng", "Ngoài phạm vi lề trong component"],
                 ["DEC-327, DEC-333", "Effect, chuyển động", "Không liên quan số lề"],
                 ["DEC-334, DEC-335", "Phương tiện: thẻ trải theo cột; Misc: <code>_Dot</code> cỡ 6", "Khớp: _Dot 6"],
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", intro="Số sau khi áp mọi khuyến nghị. Luật đọc được: nút Web và chip phía icon lùi 2 như Untitled; ô nhập Web lùi 4; icon → chữ 6 ở nút Web, 8 ở nút App và ô, 4 ở chip.", html=PROP),
        dict(title="Set không tìm thấy, giới hạn đo", html=(
            "<p class=\"small\"><b>Không có set đúng tên:</b> Tab công khai (chỉ có <code>_Tab chip</code>, <code>_Header tab</code>, lớp Tab item trong Section header); Header nav item (đo <code>_Header tab</code>, <code>_Header action</code>, <code>_Header bell</code>); Segmented của bộ mới (chỉ còn SegmentedControl Astryx 43:250616). "
            "<b>Ref Untitled không có:</b> Alert, Notification, Breadcrumbs, thẻ chọn, Vehicle.</p>"
            "<p class=\"small\"><b>Bốn phần còn lại chưa đo:</b> Dropdown search, _Nav heading, _Nav account card, _Nav featured card là component đơn, không phải set; set trên 80 biến thể chỉ đọc 80 biến thể đầu (Button 252, Badge 288, Input 345, Select 131, Radio và Checkbox group item 112).</p>"
            "<p class=\"small\"><b>Chưa chắc:</b> \"biến treo\" suy từ việc biến không có trong danh sách biến của collection, API vẫn đọc được; Multi-select Platform Mobile đo cao 30, chưa soi có phải lớp mở sheet. Đếm gắn token trên 38 set, 19 set còn lại chỉ đọc số. Icon wrap của Badge đang ẩn có cỡ cũ nên không tính. Số Figma có thể đổi nếu agent khác đang sửa Badge.</p>")),
    ],
    items=ITEMS,
    final=("Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/spacing.md</code> và spec component → gắn lại biến Figma từng set → ghi DEC. Component đổi số bị đánh stale và sync dần (rule ds-stale). "
           "Đổi hình đã duyệt (Tag, ô đếm, menu) chỉ làm theo mục bạn chọn."),
    css="""
.pd-fb{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}.pd-fb button{font:600 12px/18px Inter;border:1px solid #CBD5E1;border-radius:999px;padding:3px 10px;background:#fff;color:#334155;cursor:pointer}.pd-fb button[aria-pressed=true]{background:#0036B5;border-color:#0036B5;color:#fff}
.pd-main td,.pd-main th{vertical-align:top}.pd-main td.n{white-space:nowrap}
.pd-flag{display:inline-block;font:600 11px/15px Inter;color:#B42318;background:#FEE4E2;border-radius:4px;padding:0 4px;white-space:nowrap}
.pd-leg{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:12.5px;margin:8px 0}.pd-leg span{display:inline-flex;align-items:center;gap:6px}.pd-leg i{width:14px;height:14px;border-radius:3px;display:inline-block}.pd-leg .pd-p{background:#FEF0C7}.pd-leg .pd-w{background:#EBE9FE}.pd-leg .pd-g{background:#D1FADF}
.pd-g2{display:flex;flex-wrap:wrap;gap:var(--space-xl) var(--space-3xl);align-items:flex-start}
.pd-duo{display:flex;flex-wrap:wrap;gap:var(--space-lg) var(--space-3xl);align-items:flex-start}.pd-duo>div{display:grid;gap:var(--space-md);min-width:0}
.pd-h{font:600 12px/16px Inter;color:var(--color-text-tertiary)}
.ub-main td.n{min-width:64px;text-align:left}.ub-main th{text-align:left}.ub-u,.ub-o{display:block;font:600 12.5px/18px Inter;white-space:nowrap}.ub-u{color:#0036B5}.ub-o{border-radius:4px;padding:0 4px;width:max-content}.ub-ok{background:#D1FADF;color:#05603A}.ub-no{background:#FEE4E2;color:#B42318}.ub-na{background:#F1F5F9;color:#475569}.pd-leg .ub-u,.pd-leg .ub-o{display:inline-block}
.st-note{color:#475569;font-weight:600}.al-main td{vertical-align:top}.al-row{display:flex;align-items:center;gap:var(--space-md);padding:0 var(--space-md);border:1px solid var(--color-border-primary);border-radius:var(--radius-sm);background:var(--color-bg-primary);color:var(--color-text-primary);font-size:14px;overflow:visible}.al-ic{width:16px;height:16px;flex:none;border-radius:4px;background:var(--color-bg-tertiary)}.al-tx{min-width:0;flex:1;padding:6px 0}.al-tx.al-cut{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.al-tx.al-over{flex:none;white-space:nowrap;max-width:none;color:var(--color-text-error-primary)}
.al-pvw{max-width:100%;overflow:hidden}.al-ck{display:flex;gap:var(--space-md);max-width:240px;font-size:14px;line-height:20px;color:var(--color-text-primary)}.al-ck i{width:20px;height:20px;flex:none;border-radius:4px;background:var(--color-action-primary)}
.al-fd{display:grid;max-width:240px;color:var(--color-text-primary);font-size:14px}.al-fd b{font-weight:500}.al-fd small{color:var(--color-text-tertiary);font-size:12px}.al-in{border:1px solid var(--color-border-input);border-radius:var(--radius-sm);padding:6px 12px}
.al-mn{display:flex;flex-direction:column;width:200px;padding:4px;border:1px solid var(--color-border-primary);border-radius:var(--radius-md);background:var(--color-bg-primary);color:var(--color-text-primary);font-size:14px}.al-mn span{padding:8px;border-radius:var(--radius-xs)}.al-mn .on{background:var(--color-bg-tertiary)}.al-mn .on2{background:var(--color-bg-secondary)}
.ub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:var(--space-2xl)}.ub-pair{display:grid;gap:var(--space-xs);align-content:start;min-width:0;overflow-x:auto}.ub-pair h4{margin:0;font:600 13px/18px Inter}.ub-pair .pd-a{padding-bottom:32px}.ub-pair .pd-w b{margin-top:16px}
.pd-fig{display:grid;gap:2px;justify-items:start}.pd-cap{color:var(--color-text-tertiary);max-width:280px}
.pd-a{--z:2;--fs:var(--font-size-sm);--pd-on-sm:var(--space-sm);--pd-sm-new:var(--space-lg);padding-bottom:18px}
[data-platform=web] .pd-a{--pd-on-sm:5px;--pd-sm-new:var(--space-md-lg)}
.pd-box{display:inline-flex;align-items:center;position:relative;background:var(--color-bg-primary);color:var(--color-text-primary);box-shadow:inset 0 0 0 1px var(--color-border-primary)}
.pd-box.chip{background:var(--color-utility-blue-50);color:var(--color-utility-blue-700);box-shadow:none}.pd-box.link{box-shadow:none;background:transparent}
.pd-s{display:inline-block;height:100%;position:relative;flex:none}.pd-s b{position:absolute;top:100%;left:50%;transform:translateX(-50%);margin-top:3px;font:600 11px/14px Inter;color:var(--color-text-secondary)}
.pd-p{background:var(--color-utility-yellow-100)}.pd-w{background:var(--color-utility-purple-100)}.pd-g{background:var(--color-utility-green-100)}
.pd-t{font-size:calc(var(--fs)*var(--z));line-height:1.1;font-weight:500;white-space:nowrap;flex:none}
.pd-i{display:inline-flex;flex:none}.pd-ic,.pd-ic svg{width:100%;height:100%;display:block}
.pd-d{display:inline-block;border-radius:50%;background:currentColor;flex:none}
.pd-c{display:inline-flex;align-items:center;flex:none;border-radius:calc(var(--radius-xxs)*var(--z));box-shadow:inset 0 0 0 1px currentColor}
.pd-rd{display:flex;gap:var(--space-lg);align-items:center;flex-wrap:wrap;--pd-on-sm:var(--space-sm)}[data-platform=web] .pd-rd{--pd-on-sm:5px}
.pd-rd .o{display:inline-flex;align-items:center;justify-content:center;border-radius:50%;background:var(--color-action-primary)}.pd-rd .s{width:48px;height:48px;zoom:1}.pd-rd .m{width:60px;height:60px}
.pd-rd .o i{display:block;border-radius:50%;background:var(--color-text-inverse);transform:scale(3)}
""",
    js="""
window.afterToggle=()=>{document.querySelectorAll('.pd-s').forEach(s=>{const a=s.closest('.pd-a');const z=parseFloat(getComputedStyle(a).getPropertyValue('--z'))||1;const w=s.getBoundingClientRect().width/z;const b=s.querySelector('b');if(b)b.textContent=Math.round(w*10)/10})};
document.querySelectorAll('.pd-fb').forEach(g=>{const btns=g.querySelectorAll('button');const tb=g.nextElementSibling.querySelector('tbody');btns.forEach(b=>b.addEventListener('click',()=>{btns.forEach(x=>x.setAttribute('aria-pressed',x===b));const f=b.dataset.f;tb.querySelectorAll('tr').forEach(t=>{t.style.display=(f==='all'||t.dataset.c===f)?'':'none'})}))});
""",
)
