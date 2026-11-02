#!/usr/bin/env python3
"""SPEC trang review Foundations · Khoảng cách. Số đếm đọc từ tokens.json, tokens.untitled.json, token-usage.json, _token-ledger.json."""
import json
import re

import kit

ROOT = kit.ROOT
TJ = json.loads((ROOT / "design-system/tokens.json").read_text())
VARS = TJ["collections"]["Platform"]["vars"]
PRIM = {k: v for k, v in TJ["collections"]["Primitives"]["number"].items() if k.startswith("space/")}
USAGE = {t["name"]: t for t in json.loads((ROOT / "design-system/_review/token-usage.json").read_text())["tokens"]}
FIND = json.loads((ROOT / "design-system/_review/token-usage.json").read_text())["findings"]
LEDGER = json.loads((ROOT / "design-system/components/_token-ledger.json").read_text())["size"]["tokens"]
UNT = {c["name"]: c["variables"] for c in json.loads((ROOT / "design/_ref/untitled-ui/tokens.untitled.json").read_text())["collections"]}


def rem_px(x):
    return int(round(float(str(x).replace("rem", "")) * 16))


UP = [(v["name"].replace("--", ""), rem_px(list(v["values"].values())[0])) for v in UNT["0. Primitives / Spacing (S1)"]]
US = [(v["name"].replace("--", ""), rem_px(list(v["values"].values())[0])) for v in UNT["3. Spacing / Semantic (S1)"]]
MINE_PX = set(PRIM.values())
UNT_PX = {p for _, p in UP}
COMMON = sorted(MINE_PX & UNT_PX)
MISSING = sorted(UNT_PX - MINE_PX)
ONLY = sorted(MINE_PX - UNT_PX)
assert (len(UP), len(US), len(COMMON), len(MISSING), ONLY) == (32, 17, 17, 15, [10, 14])


def uses(name):
    t = USAGE.get(name) or {}
    return len(set(t.get("direct", [])) | set(t.get("via", [])))


# token vai trò trỏ thẳng primitive
ROLE_PRIM = [k for k, x in VARS.items() if not k.startswith(("space/", "size/", "chip/", "container/", "grid/")) and any(isinstance(x.get(m), str) and re.fullmatch(r"space/\d+", x[m]) for m in ("Web", "Mobile"))]
PRIM_CALLS = [f for f in FIND if f["kind"] == "prim"]
SCALE = {int(v["Web"].split("/")[1]): k.split("/")[1] for k, v in VARS.items() if k.startswith("space/") and isinstance(v.get("Web"), str)}
assert len(ROLE_PRIM) == 19 and len(SCALE) == 17

# phân loại 59 token Component chờ đợt 2
PENDING = {k: v for k, v in LEDGER.items() if v.get("status") == "pending-round-2"}
GROUPS = {
    "le": ["chip/count-inset", "chip/padding-x-sm", "chip/padding-x-lg", "chip/padding-x-icon-lg", "upload/required-gap", "upload/meta-offset", "command-search/highlight-padding-x",
           "avatar/group-overlap/sm", "avatar/group-overlap/md", "avatar/group-overlap/lg", "field/edge-inset", "field/text-inset", "field/content-gap", "field/hint-inset",
           "table/cell-padding-y", "table/cell-padding-x", "notification/action-gap"],
    "co": ["chip/height-sm", "chip/height-lg", "avatar/size/md", "avatar/size/xxl", "avatar/status-size/md", "avatar/status-size/xl", "avatar/edit-size/xl", "avatar/icon-size/sm",
           "avatar/edit-icon-size/lg", "avatar/spinner-size/xxl", "upload/app-tap-min-height", "otp/cell-width", "table/row-min-height", "header-nav/height"],
    "rong": ["avatar-label/width", "tooltip/max-width", "upload/compact-text-min-width", "field/width-default", "field/label-max-width", "progress/width-default",
             "header-nav/account-menu-width", "breadcrumbs/current-max-width", "breadcrumbs/menu-min-width", "command-search/width"],
    "chu": ["chip/font-size-sm", "chip/line-height-sm", "chip/count-font-size", "chip/count-line-height", "avatar-label/subtitle-size", "avatar-label/subtitle-line-height", "help-sheet/title-line-height", "upload/action-font-size"],
    "bo": [],  # DEC-328: chip/count-radius → radius/xxs, upload/sheet-radius → radius/overlay
    "khac": ["upload/disabled-opacity", "upload/divider-width", "field/border-width"],
}
assert sorted(sum(GROUPS.values(), [])) == sorted(PENDING), "phân loại sổ gộp lệch sổ"
N_LE, N_CO, N_RONG = len(GROUPS["le"]), len(GROUPS["co"]), len(GROUPS["rong"])
N_DO = N_LE + N_CO + N_RONG
assert (len(PENDING), N_DO) == (52, 41)  # DEC-334 đã quyết 5 token vehicle/q-*

OK, DIFF, GAP, OWN = ('<span class="st-ok">Giống</span>', '<span class="st-diff">Khác có lý do</span>', '<span class="st-gap">Mình thiếu</span>', '<span class="st-own">Chỉ mình có</span>')


def code(s):
    return f"<code>{s}</code>"


def orig(k):
    o = PENDING[k]["original"]
    a, b = o.get("Web"), o.get("Mobile")
    fix = lambda x: f"<code>{x}</code>" if isinstance(x, str) else str(x).replace("-", "−")
    return fix(a) if a == b else f"{fix(a)} · {fix(b)}"


# ---------- hàng bảng đối chiếu ----------
prim_rows = []
for name, px in UP:
    if px in MINE_PX:
        t = f"space-{px}"
        prim_rows.append([code(name), f"n:{px}", code(f"space/{px}"), OK, f"n:{uses(t)}", "Đặt tên theo px (<code>DEC-135</code>)" if px else ""])
    else:
        prim_rows.append([code(name), f"n:{px}", "—", GAP, "n:0", "Không token nào cần; số rộng lớn đi qua <code>width/*</code>" if px >= 320 else "Không token nào cần"])
prim_rows.insert(5, ["—", "n:—", code("space/10"), OWN, f"n:{uses('space-10')}", "Chỉ 2 token lề Badge gọi. Untitled viết <code>px-2.5</code> trong code nhưng không đưa vào 32 bậc Figma"])
sem_rows = []
for name, px in US:
    k = name.split("-", 1)[1]
    sem_rows.append([code(name), f"n:{px}", code(f"space/{k}"), code(f"size/{k}"), OK, f"n:{uses('space-' + k)}", f"n:{uses('size-' + k)}"])

layout_rows = [
    [code("grid/margin"), "n:32", "n:16", "<code>container-padding-desktop</code> 32 · <code>container-padding-mobile</code> 16", OK, "Không gộp được: 32 trên khung app 393 chỉ còn 329 cho nội dung. DEC-324 đã đổi tên, số giữ 32 · 16"],
    [code("container/max-width-desktop"), "n:1280", "—", "<code>container-max-width-desktop</code> 1280", OK, "DEC-324: giống Untitled, app không chặn rộng"],
    [code("layout/card-padding"), "n:16", "n:16", "Không có biến; <code>slideout-menu</code> viết <code>px-4 md:px-6</code> = 16 · 24", OWN, "Đã một số. Mục sp05"],
    [code("layout/title-gap"), "n:16", "n:16", "Không có biến", OWN, "Đã một số"],
    [code("layout/list-gap"), "n:8", "n:12", "Không có biến", OWN, "Gộp được về 12. Mục sp04"],
    [code("form/field-gap"), "n:16", "n:12", "Không có biến", OWN, "Gộp được về 16. Mục sp04"],
    [code("layout/section-gap"), "n:32", "n:24", "Không có biến", OWN, "Giữ tách: 32 bằng rãnh lưới web, 24 cho màn hẹp"],
    [code("layout/empty-padding"), "n:80", "n:64", "Không có biến", OWN, "Giữ tách theo <code>DEC-259</code>; 0 component gọi, chỉ màn trống dùng"],
]

pending_summary = [
    ["Lề, khoảng giữa", f"n:{N_LE}", "Trang này, sp01 · sp06 · sp07"],
    ["Cao, cỡ khối", f"n:{N_CO}", "Trang này, sp06 · sp08"],
    ["Rộng", f"n:{N_RONG}", "Trang này, sp09; bậc <code>width/*</code> quyết ở trang Lưới"],
    ["Cỡ chữ, cao dòng", f"n:{len(GROUPS['chu'])}", "Thuộc Chữ (<code>DEC-322</code>), không xét ở đây"],
    ["Bo góc", f"n:{len(GROUPS['bo'])}", "Thuộc trang Bo góc"],
    ["Nét viền, độ mờ", f"n:{len(GROUPS['khac'])}", "Thuộc Effect và Touch-focus; không phải khoảng cách"],
    ["<b>Tổng</b>", f"n:<b>{len(PENDING)}</b>", "Khớp <code>design-system/components/_token-ledger.json</code>"],
]

doc_rows = [
    ["“Mọi số trên thang 4”", "Sai: còn 42 (nút app), 22 (chip), 10, 14, 3", "Viết lại: thang 4 là mặc định; ngoại lệ ghi tên và công thức"],
    ["Mục Tab: “nhãn → số đếm 6 (<code>space/6</code>)”", "Gọi primitive trong luật", "Đổi thành <code>space/sm</code>"],
    ["Ghi chú sổ <code>chip/height-sm</code>: “16 = một dòng chữ 12/16”", "Số hiện tại 22 (<code>DEC-259</code>)", "Sửa ghi chú trong <code>tokens.json</code> khi áp"],
    ["“K3 64”, “K2b 48” trong luật (K1–K4, K2b là các đường canh dọc trên app, đo từ mép trái màn; chi tiết ở sp11)", "Lưới app đã thay đường K (<code>DEC-259</code>), con số vẫn đúng ở mọi máy vì đo từ mép trái", "Giữ số, thêm công thức theo sp11; riêng “phải 345” chỉ đúng ở khung 393"],
]


# ---------- xem thử ----------
def bar(label, css, extra=""):
    return (f'<div class="sp-r"><span class="sp-l">{label}</span><span class="sp-t"><i class="sp-b {extra}" style="width:{css}"></i></span><span class="sp-n" data-m></span></div>')


def cols(cells, platform="web"):
    """cells: [(nhãn, html)] hoặc [(nhãn, html, platform)]; mỗi ô một pane biến đọc đúng nền tảng."""
    out = []
    for c in cells:
        p = c[2] if len(c) > 2 else platform
        out.append(f'<div class="pane" data-theme="light" data-platform="{p}"><span class="lab">{kit.E(c[0])}</span><div class="sp-scroll">{c[1]}</div></div>')
    cls = "pv3" if len(out) == 3 else "pvw"
    return f'<div class="{cls}">{"".join(out)}</div>'


def pv_scale():
    h = "".join(bar(code(f"space/{p}"), f"var(--space-{p})", "sp-own" if p == 10 else "") for p in sorted(MINE_PX))
    miss = "".join(f'<span class="sp-miss">{p}</span>' for p in MISSING)
    return kit.panes(f'{h}<div class="type-caption tp-sub" style="margin-top:var(--space-lg)">15 bậc Untitled mình không có, 0 token cần tới:</div><div class="sp-misses">{miss}</div>', modes=("light",))


def badge(pad, h, text="Đang chạy"):
    return f'<span class="sp-badge" style="height:{h};padding:0 {pad}">{text}</span>'


def pv_badge():
    sets = [("Giữ 10 · 12 · 14 (DEC-310)", "var(--chip-padding-x-sm)", "var(--space-lg)", "var(--chip-padding-x-lg)"),
            ("Theo Untitled 8 · 10 · 12", "var(--space-md)", "var(--chip-padding-x-sm)", "var(--space-lg)"),
            ("Làm tròn về thang 8 · 12 · 16", "var(--space-md)", "var(--space-lg)", "var(--space-xl)")]
    cells = []
    for lab, a, b, c in sets:
        cells.append((lab, f'<div class="sp-stack">{badge(a, "var(--chip-height-sm)")}{badge(b, "var(--size-3xl)")}{badge(c, "var(--chip-height-lg)")}</div>'))
    return cols(cells)


def pv_alias(mode, platform):
    if platform == "web":
        return bar(code("layout/screen-inset"), "var(--grid-margin)") + bar(code("space/4xl"), "var(--space-4xl)") + bar(code("control/padding-x/md"), "var(--control-padding-x-md)") + bar(code("space/lg"), "var(--space-lg)")
    return bar(code("layout/screen-inset"), "var(--grid-margin)") + bar(code("space/xl"), "var(--space-xl)") + bar(code("control/padding-x/md"), "var(--control-padding-x-md)") + bar(code("space/xl"), "var(--space-xl)")


def app_card(inset):
    return (f'<div class="sp-frame" style="--i:{inset}"><div class="sp-in">'
            '<div class="tp-card"><div class="tp-top"><span class="type-code tp-sub">LVT-2026-0412</span><span class="tp-chip tp-b">Đang chạy</span></div>'
            '<div class="type-title-3">Cảng Cát Lái → KCN Long Hậu, Cần Giuộc, Long An</div><div class="type-body tp-sub">51C-482.15 · mooc 51R-091.44 · Nguyễn Văn Hoà</div></div>'
            '<div class="sp-mw type-caption tp-sub">Nội dung rộng <span class="sp-n" data-mw></span></div>'
            '<span class="tp-btn wide"><span class="type-label">Bắt đầu chuyến</span></span></div></div>')


def form(gap):
    f = lambda lab, val: f'<div class="tp-fld"><span class="type-label">{lab}</span><div class="tp-inp"><span class="type-body">{val}</span></div></div>'
    return (f'<div class="sp-form" style="--g:{gap}"><div class="type-heading sp-gt">Hàng hoá</div>{f("Mã container", "TCLU 482915-3")}{f("Điểm giao", "KCN Long Hậu, Long An")}{f("Số seal", "VN0482915")}</div>')


def file_rows(gap):
    r = lambda a, b: f'<div class="tp-card"><div class="type-body">{a}</div><div class="type-caption tp-sub">{b}</div></div>'
    return f'<div class="sp-list" style="--g:{gap}">{r("phieu-can-LVT-2026-0412.pdf", "2,4 MB · tải lên 14:30")}{r("anh-niem-phong-cong-B.jpg", "1,1 MB · tải lên 14:32")}</div>'


def card_pad(pad):
    return (f'<div class="tp-card" style="padding:{pad}"><div class="type-title-3">Thông tin chuyến</div><dl class="tp-kv"><dt><span class="type-caption">Tuyến</span></dt><dd><div class="type-body">Cát Lái → KCN Long Hậu</div></dd>'
            '<dt><span class="type-caption">Xe · mooc</span></dt><dd><div class="type-body">51C-482.15 · 51R-091.44</div></dd></dl></div>')


def pv_table(mode, platform):
    td = 'style="padding:var(--table-cell-padding-y) var(--table-cell-padding-x)"'
    return (f'<table class="sp-tb"><tr><td {td}><span class="type-code">LVT-0412</span></td><td {td}><span class="type-body">Cát Lái → Long Hậu</span></td></tr>'
            f'<tr><td {td}><span class="type-code">LVT-0411</span></td><td {td}><span class="type-body">Phước Long → Bình Dương</span></td></tr></table>'
            + bar(code("table/cell-padding-y"), "var(--table-cell-padding-y)") + bar(code("table/cell-padding-x"), "var(--table-cell-padding-x)") + bar(code("field/edge-inset"), "var(--field-edge-inset)"))


def pv_gap():
    lab = lambda g: f'<span class="type-label">Mã container</span><span class="type-label tp-err" style="margin-left:{g}">*</span>'
    return cols([("Dấu bắt buộc cách nhãn 3 (đang dùng)", lab("var(--upload-required-gap)") + bar(code("upload/required-gap"), "var(--upload-required-gap)")),
                 ("Dấu bắt buộc cách nhãn 2 (đề xuất)", lab("var(--space-xxs)") + bar(code("space/xxs"), "var(--space-xxs)"))])


def pv_sizes():
    rows = [("chip/height-sm", "chip-height-sm"), ("size/2xl", "size-2xl"), ("chip/height-lg", "chip-height-lg"), ("size/3xl", "size-3xl"), ("avatar/size/md", "avatar-size-md"), ("size/4xl", "size-4xl"), ("table/row-min-height", "table-row-min-height"), ("size/6xl", "size-6xl"), ("avatar/size/xxl", "avatar-size-xxl"), ("size/8xl", "size-8xl")]
    return kit.panes("".join(bar(code(a) if a.startswith("size") else a, f"var(--{b})", "" if a.startswith("size") else "sp-own") for a, b in rows), modes=("light",))


def pv_width():
    a = '<div class="sp-frame375"><div class="sp-in2"><div class="tp-inp" style="width:var(--field-width-default)"><span class="type-body">Rộng theo màn, máy thử 375</span></div></div></div>'
    b = '<div class="sp-frame375"><div class="sp-in2"><div class="tp-inp" style="width:100%"><span class="type-body">Rộng đầy vùng nội dung: 343</span></div></div></div>'
    bars = bar("rộng 240 đang rải 5 token", "var(--avatar-label-width)", "sp-own") + bar(code("size/11xl"), "var(--size-11xl)") + bar("150 của vùng kéo thả", "var(--upload-compact-text-min-width)", "sp-own")
    return cols([("Ô nhập app đang dùng, trên máy thử 375", a, "mobile"), ("Đề xuất, trên máy thử 375", b, "mobile")]) + f'<div style="margin-top:var(--space-md)">{kit.panes(bars, modes=("light",))}</div>'


def pv_control():
    b = lambda h, t: f'<span class="sp-ctl" style="height:{h}"><span class="tp-btn wide" style="height:100%"><span class="type-label">{t}</span></span><span class="sp-n" data-mh></span></span>'
    return cols([("Giữ 42, vùng bấm vô hình đủ 44 (DEC-138)", b("var(--control-height-md)", "Xác nhận giao") , "mobile"),
                 ("Đổi thành 44, bằng touch/min", b("var(--touch-min)", "Xác nhận giao"), "mobile")])


def pv_k():
    inset, pad = "var(--grid-margin)", "var(--layout-card-padding)"
    icon, gap = "var(--size-xl)", "var(--space-xl)"
    k = [("K1", inset), ("K2", f"calc({inset} + {pad})"), ("K2b", f"calc({inset} + {pad} + {pad})"),
         ("K3", f"calc({inset} + {pad} + {icon} + {gap})"), ("K4", f"calc({inset} + {pad} + {pad} + {icon} + {gap})")]
    rows = "".join(f'<div class="sp-kr"><i class="sp-b" style="width:{c}"></i><span class="type-caption">{n}</span><span class="sp-n" data-m></span></div>' for n, c in k)
    cells = "".join("<i></i>" for _ in range(4))
    return kit.panes(f'<div class="sp-k"><div class="sp-kgrid">{cells}</div><div class="sp-kbars">{rows}</div></div>'
                     '<div class="type-caption tp-sub" style="margin-top:var(--space-md)">Khung 393, nền xám là 4 cột lưới app rãnh 16. Mọi đường K rơi trong cột 1.</div>', modes=("light",), platforms=("mobile",))


# ---------- bảng phụ trong mục ----------
le_tb = kit.rows(["Token", "Hiện tại", "Đề xuất", "Lý do"], [
    [code("upload/required-gap"), "n:3", "<code>space/xxs</code> 2", "Untitled <code>label.tsx</code> viết <code>gap-0.5</code> = 2; nhìn đổi 1px"],
    [code("upload/meta-offset"), "n:1", "Ngoại lệ, giữ 1", "Chỉnh quang học dòng phụ file"],
    [code("command-search/highlight-padding-x"), "n:1", "Ngoại lệ, giữ 1", "Nền chữ khớp, lớn hơn làm giãn chữ"],
    [code("chip/count-inset"), "n:3", "Ngoại lệ, giữ công thức (22 − 16) / 2", "Suy từ cao chip và cao ô đếm (<code>DEC-303</code>)"],
    ["<code>avatar/group-overlap/sm</code>, <code>md</code>, <code>lg</code>", "n:−6 · −8 · −12", "Ngoại lệ, giữ", "Số âm = ¼ đường kính; biến Figma không tính được (<code>DEC-205</code>)"],
])
co_tb = kit.rows(["Token", "Hiện tại", "Đề xuất", "Lý do"], [
    ["<code>avatar/icon-size/sm</code>, <code>avatar/edit-icon-size/lg</code>", "n:14", "Ngoại lệ, giữ 14", "Cùng số với <code>icon/size/chip</code>, <code>icon/size/sm</code> (DEC-329 đã có <code>size/14</code>), token Avatar giữ riêng"],
    [code("chip/height-sm"), "n:22", "Ngoại lệ, công thức 18 + 2 × 2", "Untitled Badge SM: chữ 18, <code>py-0.5</code>"],
    [code("chip/height-lg"), "n:28", "Ngoại lệ, công thức 20 + 2 × 4", "Untitled Badge LG: chữ 20, <code>py-1</code>"],
    [code("table/row-min-height"), "n:52", "Ngoại lệ, công thức 20 + 2 × 16", "Chữ 20 + <code>table/cell-padding-y</code> 16; đổi lề thì số đổi theo"],
    ["<code>avatar/size/md</code>", "n:36", "Ngoại lệ, giữ", "Khớp ô đầu dòng 36 (<code>DEC-164</code>); Untitled MD là 40"],
    ["<code>avatar/size/xxl</code>", "n:88", "Ngoại lệ, giữ", "Đầu trang hồ sơ (<code>DEC-203</code>); Untitled dừng ở 64"],
    ["<code>avatar/status-size/md</code>, <code>xl</code>", "n:10 · 14", "Ngoại lệ, giữ", "Untitled cũng dùng <code>size-2.5</code>, <code>size-3.5</code>"],
    ["<code>avatar/edit-size/xl</code>, <code>avatar/spinner-size/xxl</code>", "n:28", "Ngoại lệ, giữ", "Thang avatar riêng (<code>DEC-203</code>, <code>DEC-303</code>)"],
    [code("header-nav/height"), "n:44 · 56", "Ngoại lệ, giữ", "Thanh trên theo <code>DEC-305</code>"],
    [code("upload/app-tap-min-height"), "n:72", "Ngoại lệ, giữ", "Cao tối thiểu vùng bấm tải lên trên app (<code>DEC-307</code>)"],
])
rong_tb = kit.rows(["Token", "Hiện tại", "Đề xuất", "Lý do"], [
    ["<code>avatar-label/width</code>, <code>tooltip/max-width</code>, <code>breadcrumbs/current-max-width</code>, <code>breadcrumbs/menu-min-width</code>", "n:240", "Ngoại lệ, giữ 240", "<code>DEC-314</code> đã bỏ thêm bậc cho số dùng từ 2 lần; nhìn không đổi"],
    ["<code>field/width-default</code>, <code>progress/width-default</code>", "n:320 · 100%", "Đã chốt ở DEC-324: Web <code>width/xxs</code> 320, App rộng đầy", "361 = 393 − 2 × 16 chỉ là kết quả trên khung 393"],
    [code("upload/compact-text-min-width"), "n:150", "<code>size/11xl</code> 160", "Không có lý do riêng cho 150; rộng thêm 10"],
    [code("field/label-max-width"), "n:300", "320 (<code>width/xxs</code>)", "Nhãn dài cắt “…”; rộng thêm 20"],
    ["<code>header-nav/account-menu-width</code>, <code>command-search/width</code>", "n:256 · 600", "Giữ riêng theo DEC-324", "256, 600 không trùng bậc nào. Năm token <code>vehicle/q-*</code> đã quyết ở <code>DEC-334</code>"],
])
bind_tb = kit.rows(["Token", "Web", "App"], [[code(k), orig(k).split(" · ")[0], orig(k).split(" · ")[-1]] for k in ("field/edge-inset", "field/text-inset", "field/content-gap", "field/hint-inset", "table/cell-padding-y", "table/cell-padding-x", "notification/action-gap", "otp/cell-width")])
kform_tb = kit.rows(["Đường", "Px", "Công thức từ token"], [
    ["K1", "n:16", "<code>layout/screen-inset</code>"],
    ["K2", "n:32", "K1 + <code>layout/card-padding</code>"],
    ["K2b", "n:48", "K2 + <code>layout/card-padding</code> (khối phụ trong thẻ)"],
    ["K3", "n:64", "K1 + lề ô 16 + khung icon 16 + cách 16; cũng bằng K2 + ô 24 + 8, K2 + radio 20 + 12"],
    ["K4", "n:80", "K2 + lề ô 16 + khung icon 16 + cách 16; cũng bằng K2 + ô 36 + 12"],
    ["Mép phải 345", "n:345", "Máy 393 − K1 − 2 × <code>layout/card-padding</code>; máy thử 375 ra 327"],
])

SPEC = dict(
    slug="spacing", short="phần Khoảng cách",
    title="Foundations · Khoảng cách — đủ token chưa?",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
    lead=("Trang này giúp quyết phần khoảng cách còn lệch sau khi đã chốt thang tên theo Untitled (<code>DEC-314</code>). "
          f"<mark>17/17 bậc Semantic đã trùng</mark>, nên việc còn lại nằm ở ba chỗ: <b>token vai trò và component gọi thẳng primitive</b>, <b>{N_DO} số đo Component chờ đợt 2</b> (đợt gom thứ hai của <code>DEC-319</code>: token còn số trần hoặc web khác app, quyết trên trang review), và bộ <code>layout/*</code> còn tách web, app. "
          "<mark>Chưa sửa token nào.</mark>"),
    kpis=[("17/17", "bậc Semantic trùng Untitled", "ok"), ("17/32", "bậc Primitive trùng; mình thiếu 15, 0 token cần", ""), ("1", "bậc chỉ mình có: 10", "bad"),
          (str(len(ROLE_PRIM) + len(PRIM_CALLS)), f"chỗ gọi thẳng primitive: {len(ROLE_PRIM)} token vai, {len(PRIM_CALLS)} lượt component", "bad"), (f"{N_DO}/{len(PENDING)}", "token chờ đợt 2 là số đo", "")],
    tag_kind="spacing",
    screens=dict(
        intro=("Đè đề xuất sp04 bằng biến thật: <b>app</b> <code>form/field-gap</code> 12 → 16, thấy ở màn Báo cáo sự cố; <b>web</b> <code>layout/list-gap</code> 8 → 12, chưa màn mẫu nào dùng nên web không đổi. "
               "Bật Nhãn số đo để đọc lề, khoảng giữa từ trình duyệt. Màn mẫu đã chỉnh hai chỗ để đúng token: khoảng giữa 2 ô đọc <code>form/field-gap</code>, ô bảng đọc <code>table/cell-padding-y</code>, <code>table/cell-padding-x</code>."),
        proposal_css=".tp-f.tp-prop[data-platform=mobile]{--form-field-gap:var(--space-xl)}.tp-f.tp-prop[data-platform=web]{--layout-list-gap:var(--space-lg)}",
    ),
    sections=[
        dict(title="Bảng đối chiếu Primitive — Untitled ↔ mình",
             intro=("Untitled 32 bậc, mình 19 bậc (thêm <code>space/14</code> chỉ cho cỡ icon, DEC-329). Nguồn <code>design/_ref/untitled-ui/04-spacing-radius-grid.md</code> và <code>design-system/tokens.json</code>. Đếm theo giá trị: <mark>17 Giống · 15 Mình thiếu · 2 Chỉ mình có</mark>. Cột Component đếm component dùng trực tiếp hoặc gián tiếp, theo <code>design-system/_review/token-usage.json</code>."),
             html=kit.rows(["Untitled", "Px", "Mình", "Trạng thái", "Component", "Ghi chú"], prim_rows)),
        dict(title="Bảng đối chiếu Semantic, space/* và size/* — Untitled ↔ mình",
             intro=("<mark>17/17 Giống</mark> cả tên lẫn số (<code>DEC-314</code>, không mở lại). Thang <code>size/*</code> Chỉ mình có cả 17 bậc: Untitled không tách, mình tách để Figma giới hạn đúng phạm vi cao rộng. Bậc từ <code>space/4xl</code> trở lên chưa component nào gọi, mới màn và <code>layout/*</code> dùng."),
             html=kit.rows(["Untitled", "Px", "<code>space/*</code>", "<code>size/*</code>", "Trạng thái", "Dùng space", "Dùng size"], sem_rows)),
        dict(title="Bảng đối chiếu bố cục, containers và layout/* — Untitled ↔ mình",
             intro="Untitled chỉ có 3 biến container; phần còn lại họ viết thẳng trong component. 12 biến <code>width-*</code> của Untitled đối chiếu ở trang Lưới.",
             html=kit.rows(["Mình", "Web", "App", "Untitled", "Trạng thái", "Gộp một bộ?"], layout_rows)),
        dict(title="Sổ gộp đợt 2, 59 token chia theo vai",
             intro="Nguồn sổ theo <code>DEC-319</code>. Đề xuất từng số nằm ở sp01, sp06, sp07, sp08, sp09.",
             html=kit.rows(["Nhóm", "Số token", "Xử lý ở đâu"], pending_summary)),
        dict(title="Chỗ foundations ghi lệch tokens.json",
             intro="Không cần chọn; sửa cùng lượt áp, theo luật <code>tokens.json</code> thắng.",
             html=kit.rows(["Trong <code>design-system/foundations/spacing.md</code>", "Thực tế", "Sửa thành"], doc_rows)),
        dict(title="Đã chốt, không mở lại",
             intro="Các quyết định đang hiệu lực. Mục nào muốn đổi số đã chốt thì ghi rõ Mở lại DEC kèm bằng chứng.",
             html=kit.rows(["DEC", "Đã chốt"], [
                 [code("DEC-314"), "Thang Semantic <code>space/*</code> theo tên, số Untitled, thêm thang <code>size/*</code>; đã bỏ phương án thêm bậc cho số dùng từ 2 lần."],
                 [code("DEC-313"), "Token Component chỉ trỏ Semantic hoặc Brand, kể cả số đo."],
                 [code("DEC-319"), "Gộp số đo Component 2 đợt, giữ sổ ánh xạ; đã bỏ phương án làm tròn hết không qua duyệt."],
                 [code("DEC-259"), "Lưới web lề 32, rãnh 32, rộng tối đa 1280; app 4 cột lề 16 thay đường K; bảng lề 16 × 24."],
                 [code("DEC-164"), "Lề chứa 16 cho mọi khung có chữ canh trái; ô đầu dòng 24 và 36."],
                 [code("DEC-166"), "Form đặt trên nền trang hoặc mỗi nhóm một thẻ, thẻ web lề 24."],
                 [code("DEC-138"), "Vùng chạm app 44; nút nhìn 42 thì phần thiếu là vùng bấm vô hình."],
                 [code("DEC-173"), "Cao control web 28 · 32 · 40, app 36 · 42 · 52."],
                 [code("DEC-310"), "Badge lề phía chữ 10 · 12 · 14, phía chấm, icon 6 · 8 · 10."],
                 [code("DEC-303"), "Avatar thang XS–XXL, Avatar group lùi đè; thay <code>DEC-242</code>."],
                 [code("DEC-205"), "Avatar group lùi đè ¼ đường kính, viền trắng 2."],
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)",
             intro="Nhìn đổi rất ít: chỉ ô form app, danh sách thẻ web và vài số rộng trong component.",
             html=kit.rows(["Việc", "Số token", "Nhìn có đổi?"], [
                 ["Bỏ primitive <code>space/10</code>, thang còn 18 bậc; 10 và 14 của Badge thành ngoại lệ có ghi", "n:3", "Không"],
                 ["Trỏ 19 token vai về thang Semantic, sửa 6 lượt component gọi primitive", "n:26", "Không"],
                 ["Gộp <code>form/field-gap</code> về 16, <code>layout/list-gap</code> về 12", "n:2", "App form thoáng thêm 4 mỗi ô; web danh sách thẻ thêm 4"],
                 ["Gán thẳng 8 token web khác app theo từng khối Web, App", "n:8", "Không"],
                 ["Xử lý số trần lề, cỡ, rộng theo bảng", f"n:{7 + N_CO - 1 + N_RONG}", "Đổi ở 5 token: dấu bắt buộc −1, vùng kéo thả +10, nhãn +20, ô nhập và thanh tiến độ app rộng đầy; còn lại không. Ô bấm tải lên app giữ 72: rd06 đã đạt nhờ bo mới (DEC-328)"],
             ])),
    ],
    items=[
        dict(id="sp00", grp="Thang", title="Có thêm 15 bậc Primitive lớn của Untitled không?",
             why=(f"Untitled có 32 bậc, tới 1920; mình 19 bậc, dừng ở 160. Bậc thiếu đều từ <b>192 trở lên</b>, <mark>0 token và 0 component cần</mark>. Bậc lớn nhất đang có người dùng là <code>space/160</code>, {uses('space-160')} component. Untitled ghi “Giới hạn tập giá trị: chọn bậc định sẵn”, nên thang ngắn vẫn đúng tinh thần. Số rộng trên 160 đã có <code>width/*</code>."),
             untitled="<code>spacing-48</code> 192 … <code>spacing-480</code> 1920, 32 bậc. Gốc của <code>width-*</code>, <code>container-*</code>.",
             ours="<code>space/0</code> … <code>space/160</code>, 19 bậc. Rộng lớn: <code>width/xs</code> … <code>width/2xl</code> là số riêng.",
             astryx="Thang <code>Spacing</code> dừng ở 48, có 28, 36, 44 lẻ. Theo <code>design/design.md</code>.",
             pv=pv_scale(),
             opts=[("keep", "Không thêm; số trên 160 đi qua width/*", True), ("add", "Thêm đủ 15 bậc cho khớp 32, chưa ai dùng", False)]),
        dict(id="sp01", grp="Thang", title="Bậc 10 và 14 của Badge đặt ở đâu?",
             why=("<code>space/10</code> là bậc Chỉ mình có của khoảng cách (<code>space/14</code> cũng lệch Untitled nhưng chỉ cho cỡ icon, DEC-329 ic05). Chỉ <code>chip/padding-x-sm</code>, <code>chip/padding-x-icon-lg</code> gọi, và cả hai <mark>đang vi phạm gate</mark> <code>DEC-313</code> (token Component trỏ Primitive). <code>chip/padding-x-lg</code> ghi số trần 14. Số 10, 14 do bạn duyệt từ spec Status chip (<code>DEC-310</code>), nên khuyến nghị giữ nhìn và đổi cách ghi. Untitled nói “Chấp nhận ngoại lệ, nhất là component có chữ”, code của họ dùng <code>2.5</code> tới 47 lần."),
             untitled="<code>badges.tsx</code>: pill lề <code>px-2</code> · <code>px-2.5</code> · <code>px-3</code> = 8 · 10 · 12. Có 10 trong code, không có trong 32 bậc Figma.",
             ours="<code>chip/padding-x-sm</code> 10 · <code>space/lg</code> 12 · <code>chip/padding-x-lg</code> 14 (<code>DEC-310</code>).",
             astryx="Không có token Badge riêng; <code>design/design.md</code> ghi “Không dùng 10”.",
             tokens=[("chip/padding-x-sm", "10", "Số ghi thẳng, nhãn ngoại lệ, bỏ trỏ primitive"), ("chip/padding-x-icon-lg", "10", "Như trên"), ("chip/padding-x-lg", "14", "Giữ số, thêm nhãn ngoại lệ")],
             note="Chọn giữ thì xoá được primitive <code>space/10</code>: thang primitive còn 18 bậc, mỗi bậc khớp một bậc Semantic, trừ <code>space/14</code> chỉ cho cỡ icon. Số lẻ 10, 14, 240 ghi ngoại lệ ở token dùng nó, không thành bậc.",
             pv=pv_badge(),
             opts=[("exc", "Giữ 10 · 12 · 14 làm ngoại lệ có ghi, xoá primitive space/10, Badge không đổi", True), ("unt", "Mở lại DEC-310: đổi theo Untitled 8 · 10 · 12, mọi Badge hẹp 2px mỗi bên", False), ("round", "Mở lại DEC-310: làm tròn 8 · 12 · 16, Badge SM hẹp 2, LG rộng 2", False)]),
        dict(id="sp02", grp="Thang", title="Token vai và component đang gọi thẳng primitive",
             why=(f"Bo góc đã có ba tầng: <code>radius/control</code> trỏ <code>radius/md</code> (<code>DEC-315</code>). Khoảng cách thì <mark>{len(ROLE_PRIM)} token vai</mark> vẫn trỏ <code>space/8</code>, <code>space/32</code>: layout 6, form 1, control 7, tab 3, nav 3. Thêm <mark>{len(PRIM_CALLS)} lượt component</mark> theo <code>design-system/_review/token-usage.json</code>: <code>buttons</code> gọi space-4, 6, 8, 12, 20; <code>sidebar-navigation</code> ghi “lề đầu hộp thoại <code>space/20</code> (primitive)”. Đổi xong số không đổi, nhưng đổi thang một chỗ là theo cả hệ. Với 2 token Badge xem sp01."),
             untitled="<code>spacing-md</code> trỏ primitive <code>spacing-2</code>; component gọi Semantic hoặc Tailwind.",
             ours="<code>layout/screen-inset</code> → <code>space/32</code>, <code>space/16</code>. <code>control/padding-x/md</code> → <code>space/12</code>, <code>space/16</code>.",
             astryx="Component gọi <code>Spacing/&lt;bậc&gt;</code> trực tiếp, không có tầng vai.",
             tokens=[("layout/screen-inset", "<code>space/4xl</code> · <code>space/xl</code>", "Mẫu; 19 token còn lại đổi theo cùng giá trị"), ("control/padding-x/md", "<code>space/lg</code> · <code>space/xl</code>", "Mẫu"),
                     ("grid/margin", "32 · 16", "Lề màn, DEC-324"), ("container/max-width-desktop", "1280", "DEC-324; app không đọc")],
             note="DEC-324 đã đổi <code>layout/screen-inset</code> thành <code>grid/margin</code>, vẫn 32 · 16.",
             pv=kit.panes(pv_alias, modes=("light",), platforms=("web", "mobile")),
             opts=[("all", "Trỏ 19 token vai về thang, sửa 6 lượt component, số không đổi", True), ("role", "Chỉ trỏ token vai, component sửa khi sync", False), ("no", "Giữ như hiện tại, sửa lại gate cho phép", False)]),
        dict(id="sp03", grp="Bố cục", title="Lề màn app giữ 16 hay đổi 24?",
             why=("Hiện <code>grid/margin</code> app 16, trùng <code>container-padding-mobile</code> của Untitled. Khung app 393 có <b>361</b> cho nội dung; đổi 24 còn <b>345</b>. Máy thử 375 lần lượt 343, 327. App lái xe có tuyến, biển số dài, xuống dòng nhiều hơn. Đổi 24 thì mọi đường đo từ mép (sp11) tăng 8. Web giữ 32 (<code>DEC-259</code>). Tablet lề 24 nằm trong <code>grid.tablet</code> của <code>design-system/tokens.json</code>, chưa có biến; quyết ở trang Lưới."),
             note="DEC-324 đã đổi tên token lề màn thành <code>grid/margin</code>; số 16 quyết ở đây.",
             untitled="<code>container-padding-mobile</code> 16, <code>container-padding-desktop</code> 32. Lưới điện thoại lề 16.",
             ours="<code>layout/screen-inset</code> 32 · 16 (<code>DEC-192</code>, <code>DEC-259</code>).",
             astryx="Lề màn 16 trong <code>design/design.md</code>.",
             pv=cols([("App lề 16 (đang dùng)", app_card("var(--space-xl)"), "mobile"), ("App lề 24", app_card("var(--space-3xl)"), "mobile")], "mobile"),
             opts=[("16", "Giữ 16, 361 cho nội dung ở khung 393, không màn nào đổi", True), ("24", "Mở lại DEC-192: đổi 24, nội dung app hẹp 16, đường đo tăng 8", False)]),
        dict(id="sp04", grp="Bố cục", title="Gộp bộ layout web và app được tới đâu?",
             why=("Hướng đã chốt ở Màu, Chữ là một bộ nếu làm được (<code>DEC-316</code>, <code>DEC-322</code>), nên đây là <b>Mở lại DEC-192:</b> bằng chứng mới là hướng một bộ đó, và chỉ <code>field-upload</code> trong 26 component gọi 2 token này. Định nghĩa: <code>layout/list-gap</code> = khoảng giữa các <b>thẻ trong một danh sách</b> (<code>DEC-192</code>: web 8, app 12); khối cấp màn trên lưới theo rãnh, quyết ở gr07. Còn 5 token khác nhau. <b>Lề màn</b> không gộp được (sp03). <b>Khoảng giữa 2 ô</b> app 12 đang <mark>bằng khoảng tiêu đề nhóm → ô</mark> 12, mắt không thấy nhóm; về 16 như web thì rõ. <b>Giữa 2 thẻ</b> web 8 chật so với app 12, trong khi web dày dữ liệu bằng bảng, chỉ <code>field-upload</code> gọi. Còn <code>layout/section-gap</code>, <code>layout/empty-padding</code> theo bề ngang màn nên giữ tách."),
             untitled="Không có biến. Trong code: <code>file-upload</code> dùng <code>gap-3</code>, <code>gap-4</code>; <code>input.tsx</code> nhãn → ô <code>gap-1.5</code>.",
             ours="<code>form/field-gap</code> 16 · 12, <code>layout/list-gap</code> 8 · 12, <code>layout/section-gap</code> 32 · 24, <code>layout/empty-padding</code> 80 · 64.",
             astryx="Giữa các thẻ 12, đệm trong thẻ 16 trong <code>design/design.md</code>; một bộ.",
             tokens=[("form/field-gap", "16 cả hai", "Giữa 2 ô; app 12 → 16"), ("layout/list-gap", "12 cả hai", "Giữa 2 thẻ, dòng; web 8 → 12")],
             pv=cols([("App, giữa 2 ô 12 (đang dùng)", form("var(--form-field-gap)"), "mobile"), ("App, giữa 2 ô 16", form("var(--space-xl)"), "mobile"),
                      ("Web, giữa 2 thẻ 8 (đang dùng)", file_rows("var(--layout-list-gap)")), ("Web, giữa 2 thẻ 12", file_rows("var(--space-lg)"))]),
             opts=[("two", "Gộp 2: giữa ô 16, giữa thẻ 12; lề màn, section, empty giữ tách", True), ("four", "Gộp thêm section 24, empty 64; web khoảng giữa khối 32 → 24, màn trống 80 → 64", False), ("no", "Giữ tách cả 5 như DEC-192", False)]),
        dict(id="sp05", grp="Bố cục", title="Lề thẻ web 16 hay 24?",
             why=("<code>layout/card-padding</code> 16 cả hai từ <code>DEC-164</code>. Riêng form mỗi nhóm một thẻ thì web lề 24 (<code>DEC-166</code>), hiện gắn <code>space/3xl</code>, không có token vai. Web điều vận cần hiện nhiều: 16 giúp thẻ chi tiết thấp hơn khoảng 16 mỗi thẻ. Untitled bảng và ngăn kéo dùng 24 ở desktop. Token này trùng số với <code>layout/title-gap</code> (báo trùng trong <code>design-system/_review/token-usage.json</code>), nhưng khác vai nên giữ cả hai."),
             untitled="<code>slideout-menu.tsx</code> <code>px-4 md:px-6</code>; <code>table.tsx</code> ô <code>px-6 py-4</code>. Không có biến thẻ.",
             ours="<code>layout/card-padding</code> 16, <code>space/3xl</code> cho thẻ form web.",
             astryx="Card <code>default</code> 12, <code>spacious</code> 20; đệm thẻ màn 16.",
             pv=cols([("Thẻ web lề 16 (đang dùng)", card_pad("var(--layout-card-padding)")), ("Thẻ web lề 24", card_pad("var(--space-3xl)"))]),
             opts=[("16", "Giữ 16 cho mọi thẻ, thẻ form web gắn space/3xl như DEC-166", True), ("24", "Mở lại DEC-164: đổi thẻ web sang 24, mọi màn web thoáng và dài hơn", False)]),
        dict(id="sp06", grp="Số đo Component", title="8 token web khác app, cả hai đầu đã trên thang",
             why=("Nhóm này chờ đợt 2 chỉ vì <mark>web và app khác số</mark>, không vì lệch thang (<code>DEC-319</code>). Trên Figma mỗi component đã dựng hai khối Web, App riêng, nên mỗi khối gắn thẳng bậc của nó là đủ, không cần token đổi theo chế độ. Đổi lại CSS phải có <code>[data-platform]</code> ở component. Nếu sau này tách lại, sổ gộp vẫn còn." + bind_tb),
             untitled="Không có tầng này; <code>table.tsx</code> ghi <code>px-6 py-4</code>, <code>px-5 py-3</code> theo cỡ.",
             ours="<code>table/cell-padding-x</code>, <code>field/edge-inset</code>, <code>notification/action-gap</code>, <code>otp/cell-width</code> và 4 token khác, theo chế độ Web, Mobile.",
             astryx="Một bộ số, không chia Web, App.",
             pv=kit.panes(pv_table, modes=("light",), platforms=("web", "mobile")),
             opts=[("bind", "Gán thẳng space/*, size/* theo từng khối, bỏ 8 token, số không đổi", True), ("keep", "Giữ 8 token theo chế độ, ghi miễn trong sổ gộp", False)]),
        dict(id="sp07", grp="Số đo Component", title="Số lề trần còn lại",
             why=(f"Trong {N_LE} token lề chờ đợt 2: 3 token Badge ở sp01, 7 token ở sp06, còn <b>7 token</b> dưới đây. <code>DEC-319</code> đã loại cách làm tròn hết không qua duyệt, nên xét từng số. Chỉ một số đáng đổi, còn lại là chỉnh quang học hoặc suy từ công thức." + le_tb),
             untitled="<code>label.tsx</code> <code>gap-0.5</code>; “Chấp nhận ngoại lệ, nhất là component có chữ”.",
             ours="<code>upload/required-gap</code> 3, <code>upload/meta-offset</code> 1, <code>chip/count-inset</code> 3, <code>avatar/group-overlap/lg</code> −12.",
             astryx="Không có token tương ứng; <code>design/design.md</code> không ghi.",
             pv=pv_gap(),
             opts=[("table", "Theo bảng: dấu bắt buộc về 2, còn lại ghi ngoại lệ", True), ("keep", "Ghi ngoại lệ cả 7, kể cả số 3 của dấu bắt buộc", False)]),
        dict(id="sp08", grp="Số đo Component", title="Số cao, cỡ khối lệch thang",
             why=(f"{N_CO} token cỡ chờ đợt 2, trừ <code>otp/cell-width</code> ở sp06. Số 28 và 36 lặp nhiều, nhưng <code>DEC-314</code> đã bỏ phương án thêm bậc Semantic và <code>DEC-319</code> đã bỏ làm tròn, nên đề xuất ghi <b>ngoại lệ kèm công thức</b> khi suy được. Làm vậy đổi lề thì biết số nào đổi theo, theo luật giá trị dẫn xuất." + co_tb),
             untitled="<code>avatar.tsx</code> 24 · 32 · 40 · 48 · 56 · 64. Chấm 6 · 8 · 10 · 12 · 14 · 16. Badge 22 · 24 · 28.",
             ours="<code>chip/height-sm</code> 22, <code>avatar/size/md</code> 36, <code>table/row-min-height</code> 52, <code>size/3xl</code> 24.",
             astryx="<code>element-sm</code> 28, <code>element-md</code> 32, <code>element-lg</code> 36 trong <code>design/design.md</code>.",
             note="Dữ liệu Untitled <code>table.tsx</code> ghi dòng <code>h-14</code> và <code>h-18</code> = 56, 72, khác ghi nhận “dòng 52 như Untitled” ở <code>DEC-259</code>; 52 chỉ là chữ 20 + lề 2 × 16. Không đề xuất đổi, web dày dữ liệu hợp 52. <code>upload/app-tap-min-height</code> giữ 72: sau <code>DEC-328</code> thẻ app bo 12, lề 12 đã đạt máy đo nên rd06 không đổi lề.",
             pv=pv_sizes(),
             opts=[("table", "Theo bảng: ghi ngoại lệ, số suy được thì kèm công thức", True), ("steps", "Mở lại DEC-314: thêm bậc size/* cho số lặp 14, 28, 36", False)]),
        dict(id="sp09", grp="Số đo Component", title="Số rộng: 240 lặp 5 lần, 361 tràn ở máy thử 375",
             why=(f"{N_RONG} token rộng. <mark>240 lặp 5 token</mark>, thang <code>size/*</code> dừng ở 160 và <code>width/xxs</code> bắt đầu 320, nên 240 không có bậc; <code>DEC-314</code> đã bỏ phương án thêm bậc, nên ghi ngoại lệ như sp08. <mark>361 chỉ đúng ở khung 393</mark>: trên máy thử 375 ô nhập tràn 18 so với vùng nội dung. Sửa bằng rộng đầy thì hết phải giữ số." + rong_tb),
             untitled="Thang <code>width-xxs</code> 320 trở lên; <code>width-*</code> không có 240. Code dùng <code>w-60</code>, <code>w-64</code> cho menu.",
             ours="<code>avatar-label/width</code> 240, <code>field/width-default</code> 320 · 100%, <code>width/xxs</code> 320, <code>size/11xl</code> 160.",
             astryx="Dialog 400, toast 360 trong <code>design/design.md</code>.",
             tokens=[("width/xxs", "320", "Đã có từ DEC-324")],
             note="DEC-324: 320 mang tên <code>width/xxs</code>, <code>width/xs</code> là 384.",
             pv=pv_width(),
             opts=[("table", "Theo bảng: 240 ghi ngoại lệ, app rộng đầy, ảnh tính theo tỉ lệ", True), ("steps", "Mở lại DEC-314: thêm một bậc size/* 240, vì 5 token cùng số", False), ("keep", "Giữ nguyên mọi số, chỉ ghi ngoại lệ", False)]),
        dict(id="sp10", grp="Số đo Component", title="Nút MD app cao 42 lệch thang 4",
             why=("<code>spacing.md</code> ghi “Mọi số trên thang 4”, nhưng <code>control/height/md</code> app 42. Số 42 có chủ đích: nút nhìn 42, phần thiếu là vùng bấm vô hình đủ 44 (<code>DEC-138</code>), và <code>DEC-173</code> đã bỏ phương án 44. Trang này không có bằng chứng dùng thực tế mới, nên <b>khuyến nghị giữ</b> và sửa câu trong tài liệu. Vẫn hỏi lại vì 44 khớp thang 4, khớp <code>touch/min</code> và khớp Button LG của Untitled. Cái giá: mọi nút MD app cao thêm 2, component đã duyệt thành stale."),
             untitled="<code>button.tsx</code> xs 32 · sm 36 · md 40 · lg 44 · xl 48: <code>py</code> cộng cao dòng.",
             ours="<code>control/height/sm</code> 28 · 36, <code>control/height/md</code> 32 · 42, <code>control/height/ml</code> 36 · 42, <code>control/height/lg</code> 40 · 52.",
             astryx="<code>element-md</code> 32 cho web, không có bộ app.",
             pv=pv_control(),
             opts=[("keep", "Giữ 42, sửa câu “thang 4” trong spacing.md", True), ("44", "Mở lại DEC-173: đổi 44, nút MD app cao thêm 2", False)]),
        dict(id="sp11", grp="Đường canh", title="Đường K1–K4 suy từ token, ghi thế nào?",
             why=("K1–K4, K2b là các đường canh dọc trên app, đo từ mép trái màn (<code>DEC-164</code>). <code>DEC-259</code> đã đổi lưới app sang 4 cột, nhưng luật vẫn dùng vị trí “K3 64”, “K2b 48” trong <code>design-system/foundations/spacing.md</code>. Soát lại: <mark>mọi đường là tổng các token</mark>, không có đường lệch. Có hai điểm cần biết: chỉ K1 trùng mép cột, các đường còn lại nằm trong cột 1; “mép phải 345” chỉ đúng ở khung 393." + kform_tb),
             note="K1 ghi theo <code>grid/margin</code>, số 16 không đổi (DEC-324).",
             untitled="Không có đường canh; lưới điện thoại của họ vẽ trên khung 375, lề 16, rãnh 16, 4 cột <code>container-padding-mobile</code>.",
             ours="<code>layout/screen-inset</code> + <code>layout/card-padding</code> + lề ô, <code>size/xl</code>, <code>space/xl</code>. Cột 1 của lưới rộng 78 ở máy 393.",
             astryx="Không có đường canh; lề màn 16.",
             pv=pv_k(),
             opts=[("formula", "Giữ số đo, ghi công thức từ token vào spacing.md, không thêm token", True), ("tokens", "Thêm token layout cho từng đường K, thêm 5 token mới", False), ("drop", "Bỏ K, canh hết theo cột: chữ đầu dòng lùi về cột 2, 110", False)]),
    ],
    final=("Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/spacing.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>space = approved</b> (<code>ds-foundation-status.py set space approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). "
           "Việc riêng của trang: cập nhật sổ <code>design-system/components/_token-ledger.json</code>, xoá primitive <code>space/10</code> nếu chọn ở sp01."),
    css="""
.sp-r{display:grid;grid-template-columns:minmax(0,170px) minmax(0,1fr) 34px;gap:8px;align-items:center;margin:3px 0}
.sp-l{font-size:12px;line-height:16px;min-width:0;overflow-wrap:anywhere}
.sp-t{min-width:0;overflow:hidden}
.sp-b{display:block;height:12px;background:var(--color-action-primary);border-radius:2px}
.sp-b.sp-own{background:var(--color-utility-yellow-700)}.sp-b.sp-thin{height:4px;background:var(--color-border-primary)}
.sp-n{font:600 11px/14px "JetBrains Mono",monospace;color:var(--color-text-tertiary);text-align:right}
.sp-misses{display:flex;flex-wrap:wrap;gap:var(--space-xs);margin-top:var(--space-xs)}
.sp-miss{font:500 11px/16px "JetBrains Mono",monospace;padding:0 var(--space-sm);border:1px dashed var(--color-border-primary);border-radius:var(--radius-xs);color:var(--color-text-tertiary)}
.sp-scroll{overflow-x:auto}
.sp-stack{display:flex;flex-direction:column;align-items:flex-start;gap:var(--space-md)}
.sp-badge{display:inline-flex;align-items:center;white-space:nowrap;border-radius:var(--radius-full);background:var(--color-utility-blue-50);color:var(--color-utility-blue-700);font-size:var(--font-size-xs);font-weight:500}
.sp-frame{width:393px;box-shadow:inset 0 0 0 1px var(--color-border-secondary);border-radius:var(--radius-card);background:var(--color-bg-secondary)}
.sp-in{padding:var(--space-xl) var(--i);display:grid;gap:var(--space-lg)}
.sp-mw{display:flex;gap:var(--space-sm);align-items:center}
.sp-form{display:grid;gap:var(--g)}.sp-form .sp-gt{margin-bottom:calc(var(--space-lg) - var(--g))}
.sp-list{display:grid;gap:var(--g)}
.sp-tb{width:100%;border-collapse:collapse;margin-bottom:var(--space-md)}.sp-tb td{border-bottom:1px solid var(--color-border-secondary);vertical-align:top}
.sp-frame375{width:375px;box-shadow:inset 0 0 0 1px var(--color-border-secondary);border-radius:var(--radius-card);overflow:hidden;background:var(--color-bg-secondary)}
.sp-in2{padding:var(--space-xl) var(--grid-margin)}
.sp-ctl{display:flex;align-items:center;gap:var(--space-md);max-width:320px}
.sp-k{position:relative;width:393px;border:1px solid var(--color-border-secondary);min-height:176px;background:var(--color-bg-primary)}
.sp-kgrid{position:absolute;inset:0;padding:0 var(--grid-margin);display:grid;grid-template-columns:repeat(4,1fr);gap:var(--space-xl)}.sp-kgrid i{background:var(--color-bg-secondary);display:block}
.sp-kbars{position:relative;padding:var(--space-lg) 0;display:grid;gap:var(--space-md)}
.sp-kr{display:flex;align-items:center;gap:var(--space-md)}.sp-kr .sp-b{flex:none;border-radius:0 2px 2px 0}.sp-kr .sp-n{margin-left:auto;padding-right:var(--space-md)}
/* đưa màn mẫu về đúng token khoảng cách */
.tp-f .tp-card:has(>.tp-fld),.tp-f .tp-pad:has(>.tp-fld){gap:var(--form-field-gap)}
.tp-f .tp-card>.type-title-3+.tp-fld{margin-top:calc(var(--space-lg) - var(--form-field-gap))}
.tp-f .tp-tb td{padding:var(--table-cell-padding-y) var(--table-cell-padding-x)}.tp-f .tp-tb th{padding:var(--space-md) var(--table-cell-padding-x)}.tp-f .tp-tb td:nth-child(1) .type-code,.tp-f .tp-tb td:nth-child(3) span{white-space:nowrap}
""",
    js="""
window.afterToggle=()=>{document.querySelectorAll('[data-m]').forEach(e=>{const p=e.previousElementSibling;const t=p&&(p.querySelector&&p.querySelector('i')||p);if(!t)return;e.textContent=Math.round(t.getBoundingClientRect().width)});
document.querySelectorAll('[data-mw]').forEach(e=>{const p=e.parentElement.previousElementSibling;if(p)e.textContent=Math.round(p.getBoundingClientRect().width)});
document.querySelectorAll('[data-mh]').forEach(e=>{const p=e.previousElementSibling;if(p)e.textContent=Math.round(p.getBoundingClientRect().height)});
document.querySelectorAll('.sp-kr').forEach(r=>{const b=r.querySelector('i'),n=r.querySelector('[data-m]');if(b&&n)n.textContent=Math.round(b.getBoundingClientRect().width)})};
""",
)
