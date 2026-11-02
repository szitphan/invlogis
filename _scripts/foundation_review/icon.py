#!/usr/bin/env python3
"""SPEC trang review Foundations · Icon. Dựng: python3 _scripts/foundation_review/build.py icon. Luật viết: BRIEF.md cùng thư mục."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402

ROOT = kit.ROOT
OWN_DIR = ROOT / "design-system/icons"
ICON_MD = (ROOT / "design-system/foundations/icon.md").read_text(encoding="utf-8")
THEME = (ROOT / "design/_ref/untitled-ui/react/styles/theme.css").read_text(encoding="utf-8")

# Đường vẽ thật lấy từ @untitledui/icons@0.0.23 (bản miễn phí, dist/*.mjs), chỉ để so hình với Lucide.
UU = {
    "truck": ("Truck01", "M14 7h2.337c.245 0 .367 0 .482.028a1 1 0 0 1 .29.12c.1.061.187.148.36.32l4.062 4.063c.173.173.26.26.322.36.054.09.095.188.12.29.027.115.027.237.027.482V15.5c0 .466 0 .699-.076.883a1 1 0 0 1-.541.54c-.184.077-.417.077-.883.077m-5 0H14m0 0V7.2c0-1.12 0-1.68-.218-2.108a2 2 0 0 0-.874-.874C12.48 4 11.92 4 10.8 4H5.2c-1.12 0-1.68 0-2.108.218a2 2 0 0 0-.874.874C2 5.52 2 6.08 2 7.2V15a2 2 0 0 0 2 2m10 0h-4m0 0a3 3 0 1 1-6 0m6 0a3 3 0 1 0-6 0m16.5.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0Z"),
    "house": ("Home01", "M3 10.565c0-.574 0-.861.074-1.126a2 2 0 0 1 .318-.65c.163-.22.39-.397.843-.75l6.783-5.275c.351-.273.527-.41.72-.462a1 1 0 0 1 .523 0c.194.052.37.189.721.462l6.783 5.275c.453.353.68.53.843.75.145.195.252.416.318.65.074.265.074.552.074 1.126V17.8c0 1.12 0 1.68-.218 2.108a2 2 0 0 1-.874.874C19.48 21 18.92 21 17.8 21H6.2c-1.12 0-1.68 0-2.108-.218a2 2 0 0 1-.874-.874C3 19.48 3 18.92 3 17.8v-7.235Z"),
    "pencil": ("Edit01", "M2.876 18.116c.046-.414.069-.62.131-.814a2 2 0 0 1 .234-.485c.111-.17.259-.317.553-.61L17 3a2.828 2.828 0 1 1 4 4L7.794 20.206c-.294.294-.442.442-.611.553a2 2 0 0 1-.485.233c-.193.063-.4.086-.814.132L2.5 21.5l.376-3.384Z"),
    "trash-2": ("Trash01", "M16 6v-.8c0-1.12 0-1.68-.218-2.108a2 2 0 0 0-.874-.874C14.48 2 13.92 2 12.8 2h-1.6c-1.12 0-1.68 0-2.108.218a2 2 0 0 0-.874.874C8 3.52 8 4.08 8 5.2V6m2 5.5v5m4-5v5M3 6h18m-2 0v11.2c0 1.68 0 2.52-.327 3.162a3 3 0 0 1-1.311 1.311C16.72 22 15.88 22 14.2 22H9.8c-1.68 0-2.52 0-3.162-.327a3 3 0 0 1-1.311-1.311C5 19.72 5 18.88 5 17.2V6"),
    "bell": ("Bell01", "M9.354 21c.705.622 1.632 1 2.646 1s1.94-.378 2.646-1M18 8A6 6 0 1 0 6 8c0 3.09-.78 5.206-1.65 6.605-.735 1.18-1.102 1.771-1.089 1.936.015.182.054.252.2.36.133.099.732.099 1.928.099H18.61c1.196 0 1.795 0 1.927-.098.147-.11.186-.179.2-.361.014-.165-.353-.755-1.088-1.936C18.78 13.206 18 11.09 18 8Z"),
    "search": ("SearchMd", "m21 21-4.35-4.35M19 11a8 8 0 1 1-16 0 8 8 0 0 1 16 0Z"),
    "list-filter": ("FilterLines", "M6 12h12M3 6h18M9 18h6"),
    "map-pin": ("MarkerPin01", "M12 13a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12 22c4-4 8-7.582 8-12a8 8 0 1 0-16 0c0 4.418 4 8 8 12Z"),
    "package": ("Package", "M20.5 7.278 12 12m0 0L3.5 7.278M12 12v9.5m9-5.441V7.942c0-.343 0-.514-.05-.667a1 1 0 0 0-.215-.364c-.109-.119-.258-.202-.558-.368l-7.4-4.111c-.284-.158-.425-.237-.575-.267a1 1 0 0 0-.403 0c-.15.03-.292.11-.576.267l-7.4 4.11c-.3.167-.45.25-.558.369a1 1 0 0 0-.215.364C3 7.428 3 7.599 3 7.942v8.117c0 .342 0 .514.05.666a1 1 0 0 0 .215.364c.109.119.258.202.558.368l7.4 4.111c.284.158.425.237.576.268.133.027.27.027.402 0 .15-.031.292-.11.576-.268l7.4-4.11c.3-.167.45-.25.558-.369a.999.999 0 0 0 .215-.364c.05-.152.05-.324.05-.666ZM16.5 9.5l-9-5"),
}


def _dim(px):
    return f"var({px})" if isinstance(px, str) else f"{px}px"


def L(name, px=16, cls=""):
    """Icon Lucide thật qua kit.icon; px = số hoặc tên biến CSS."""
    return kit.icon(name, "x").replace('class="tp-ic x"', f'class="tp-ic {cls}" style="--ic:{_dim(px)}"', 1)


def O(name, px=16, cls=""):
    """SVG thật đọc từ design-system/icons/, chèn inline."""
    s = (OWN_DIR / f"{name}.svg").read_text(encoding="utf-8")
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"\s+", " ", s).strip().replace("<svg ", '<svg aria-hidden="true" ', 1)
    return f'<span class="tp-ic {cls}" style="--ic:{_dim(px)}">{s}</span>'


def I(name, px=16, cls=""):
    return O(name, px, cls) if (OWN_DIR / f"{name}.svg").exists() else L(name, px, cls)


def U(key, px=24):
    d = UU[key][1]
    return (f'<span class="tp-ic" style="--ic:{_dim(px)}"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></svg></span>')


def uu_svg(rel):
    """SVG thật trong file .tsx của Untitled: bỏ cú pháp React, giữ hình."""
    s = (ROOT / "design/_ref/untitled-ui/react/components/foundations" / rel).read_text(encoding="utf-8")
    s = re.search(r"<svg.*?</svg>", s, flags=re.S).group(0)
    s = s.replace("{...props}", "")
    s = re.sub(r'\s*className="[^"]*"', "", s)
    for a, b in (("fillRule", "fill-rule"), ("clipRule", "clip-rule"), ("strokeWidth", "stroke-width"), ("strokeLinecap", "stroke-linecap"), ("strokeLinejoin", "stroke-linejoin")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s)


COUNT = {"ok": 0, "diff": 0, "gap": 0, "own": 0}


def st(k):
    COUNT[k] += 1
    return f'<span class="st-{k}">' + {"ok": "Giống", "diff": "Khác có lý do", "gap": "Mình thiếu", "own": "Chỉ mình có"}[k] + "</span>"


def jump(*ids):
    return " ".join(f'<a href="#{i}">{i}</a>' for i in ids)


H = ["Mục", "Untitled UI v8", "Mình", "Trạng thái", "Mục chọn"]

# ---------- Bảng đối chiếu ----------
LIB_ROWS = [
    ["Bộ nền", "Untitled UI Icons. Bản miễn phí <code>@untitledui/icons</code> 1.181 file icon, MIT. PRO 4.600+ icon", "Lucide 1.58.0, ISC (DEC-141, DEC-156). Kho Figma 1.694 icon", st("diff"), jump("ic00")],
    ["Kiểu nét", "line · solid · duocolor · duotone (3 kiểu sau chỉ có ở PRO)", "Viền + bản tô tự vẽ cho 9 icon", st("diff"), jump("ic07")],
    ["Danh mục", "19 nhóm trong file Figma", "3 nhóm trong <code>icon.md</code> mục 7, 6 nhóm trên Figma (DEC-262)", st("diff"), jump("ic13")],
    ["Đặt tên", "Figma kebab-case có số <code>edit-01</code>; React <code>Home01</code>", "<code>icon/&lt;tên Lucide&gt;</code>, map thẳng sang code (DEC-147)", st("diff"), ""],
    ["Khung", "24×24", "24×24", st("ok"), ""],
    ["Nét trên khung 24", "2, căn giữa", "2 (DEC-300)", st("ok"), jump("ic01")],
    ["Bù nét cỡ nhỏ", "<code>stroke-[2.25px]</code> ở cỡ 16: 33 chỗ trong <code>base</code>, <code>application</code>", "Không bù. Riêng Badge 2.5 (DEC-309)", st("diff"), jump("ic01")],
    ["Đầu nét, góc nét", "Bo tròn", "Bo tròn, cả 7 icon tự vẽ", st("ok"), jump("ic09")],
    ["Cấu trúc lớp", "Một lớp vector, tránh boolean group, đổi instance giữ màu", "Một lớp <code>Vector</code> (DEC-202)", st("ok"), ""],
    ["Đổi màu", "Lớp chữ, <code>currentColor</code>", "<code>currentColor</code>, gắn <code>color/fg/*</code>", st("ok"), jump("ic12")],
]
SIZE_ROWS = [
    ["n:12", "<code>size-3</code>, 18 lần trong code", "Chưa có token. Preview DS v2: 7 component vẽ cỡ 12", st("gap"), jump("ic03")],
    ["n:14", "<code>size-3.5</code>, 12 lần", "<code>icon/size/sm</code> web · <code>icon/size/chip</code>", st("ok"), jump("ic04")],
    ["n:16", "<code>size-4</code>, 75 lần, cỡ phổ biến nhất", "<code>icon/size/md</code> web · <code>icon/size/sm</code> app", st("ok"), jump("ic02")],
    ["n:18", "Không có", "<code>icon/size/ml</code> (DEC-306)", st("own"), jump("ic04")],
    ["n:20", "<code>size-5</code>, 42 lần", "<code>icon/size/lg</code> web · <code>icon/size/md</code> app", st("ok"), jump("ic02")],
    ["n:24", "<code>size-6</code>, 12 lần. Khung gốc", "<code>icon/size/lg</code> app", st("ok"), jump("ic02")],
    ["n:28", "<code>size-7</code>, 9 lần. Chỉ Featured xl", "Không có, luật không phóng quá 24 (DEC-258)", st("diff"), jump("ic11")],
]
FEATURED_ROWS = [
    ["Kiểu light", "Tròn, nền nhạt, icon màu. <code>theme=\"light\"</code>", "Khối tròn, nền nhạt (<code>icon.md</code> mục 3.1)", st("ok"), jump("ic10")],
    ["Kiểu modern", "Vuông bo, nền trắng, viền, chỉ màu xám. Dùng thật ở Empty state và File upload", "Upload web vuông bo 8, có viền. <code>icon.md</code> mục 3.1 đã sửa về <code>radius/inner</code> 8 (DEC-328)", st("diff"), jump("ic10")],
    ["Kiểu dark", "Vuông, nền đặc, icon trắng", "Không có", st("gap"), jump("ic10")],
    ["Kiểu gradient", "Hai lớp tròn", "Không có", st("gap"), jump("ic10")],
    ["Kiểu modern-neue", "Bóng nhiều lớp, chỉ màu xám", "Không có", st("gap"), jump("ic10")],
    ["Kiểu outline", "Hai vòng viền mờ, không nền", "Không có", st("gap"), jump("ic10")],
    ["Cỡ sm", "Khối 32, icon 16, nét 2.25", "Không có", st("gap"), jump("ic11")],
    ["Cỡ md", "Khối 40, icon 20", "Upload Full web 40/20, đang mượn <code>control/height/lg</code>", st("ok"), jump("ic11")],
    ["Cỡ lg", "Khối 48, icon 24", "<code>featured-icon/size</code> 48, icon 24", st("ok"), jump("ic11")],
    ["Cỡ xl", "Khối 56, icon 28", "Không có", st("gap"), jump("ic11")],
    ["Cỡ 36", "Không có", "Featured gọn 36, icon 18 (Upload Compact)", st("own"), jump("ic11")],
    ["Sắc brand", "Có", "Không có vai brand trong Semantic (DEC-320)", st("diff"), ""],
    ["Sắc gray · error · warning · success", "4 sắc", "4 sắc, đọc <code>color/bg/*</code> + <code>color/fg/*</code>", st("ok"), jump("ic10")],
    ["Sắc info", "Không có", "<code>color/fg/info-primary</code> + <code>color/bg/info-secondary</code>", st("own"), jump("ic10")],
    ["Token riêng cho Featured", "<code>featured-icon-light-fg-*</code>, 5 token", "Dùng chung <code>color/fg/*</code>", st("diff"), jump("ic10")],
]


def css_pairs(text, ns):
    """Tên fg → bậc màu Sáng, Tối theo thứ tự xuất hiện trong file css."""
    o = {}
    for n, v_ in re.findall(rf"--color-(fg-[\w-]+):\s*var\(--{ns}([\w-]+)\)", text):
        o.setdefault(n, []).append(v_)
    return o


def fg_rows():
    u, m = css_pairs(THEME, "color-"), css_pairs(kit.TCSS, "")
    rows = []
    for n in sorted(set(u) | set(m)):
        a, b = u.get(n), m.get(n)
        code = "color/fg/" + n[3:]
        if a and b:
            k = "ok" if a[:2] == b[:2] else "diff"
            rows.append([f"<code>{n}</code>", f"{a[0]} · {a[-1]}", f"<code>{code}</code>: {b[0]} · {b[-1]}", st(k), jump("ic12") if n == "fg-quaternary" else ""])
        elif a:
            rows.append([f"<code>{n}</code>", f"{a[0]} · {a[-1]}", "Không có vai brand (DEC-320)", st("gap"), ""])
        else:
            rows.append([f"<code>{n}</code>", "Không có", f"<code>{code}</code>: {b[0]} · {b[-1]}", st("own"), ""])
    return rows


FG_ROWS = fg_rows()
EXTRA_ROWS = [
    ["Payment icons", "56 icon. Không có MoMo, VNPay, Napas", "Không có", st("gap"), jump("ic16")],
    ["Social icons", "22 icon. Không có Zalo", "Không có", st("gap"), jump("ic16")],
    ["Integration icons", "16 icon: công cụ AI, framework", "Không có", st("gap"), jump("ic16")],
    ["File type icon", "<code>@untitledui/file-icons</code>, dùng trong File upload", "Upload nhắc tới, chưa có nguồn. Bảng nghĩa có <code>file-text</code>, <code>file-spreadsheet</code>", st("gap"), jump("ic16")],
    ["Icon phương tiện", "Không có", "<code>design-system/foundations/vehicle.md</code>, trang riêng, ngoài phạm vi trang này", st("own"), ""],
]
RULE_ROWS = [
    ["Icon phổ quát, không sáng tạo lại", "Luật 2", "Bảng nghĩa, tra chứ không tự chọn (DEC-146)", st("ok"), jump("ic14")],
    ["Icon không thay chữ, mặc định icon + nhãn", "Luật 3", "Chưa ghi trong <code>icon.md</code>", st("gap"), jump("ic17")],
    ["Không phóng icon, nhấn mạnh bằng Featured", "Luật 4, thiết kế cho 16–32", "Không quá 24 app, 20 web (DEC-258)", st("ok"), jump("ic11")],
    ["Giữ một thư viện", "Luật 5", "DEC-141, DEC-145", st("ok"), jump("ic00")],
    ["Icon trang trí ẩn khỏi trình đọc màn hình", "<code>aria-hidden=\"true\"</code>", "Chưa ghi trong <code>icon.md</code>", st("gap"), jump("ic17")],
]

# ---------- Bảng icon đủ cỡ ----------
SAMPLE = ["plus", "search", "chevron-down", "triangle-alert", "map-pin", "clipboard-list", "container", "tractor-unit", "semi-trailer", "container-truck", "container-seal", "toll-booth", "container-ship", "eir"]
SIZES = [(12, "1,00"), (14, "1,17"), (16, "1,33"), (18, "1,50"), (20, "1,67"), (24, "2,00")]


def size_table(mode, platform):
    head = "".join(f"<th>{s}<small>nét {n}</small></th>" for s, n in SIZES)
    body = "".join(f"<tr><td><span class=\"type-caption\">{n}</span>" + (' <span class="own">tự vẽ</span>' if (OWN_DIR / f"{n}.svg").exists() else "") + "</td>"
                   + "".join(f"<td>{I(n, s)}</td>" for s, _ in SIZES) + "</tr>" for n in SAMPLE)
    return f'<table class="szt"><thead><tr><th></th>{head}</tr></thead><tbody>{body}</tbody></table>'


# ---------- Bảng nghĩa đọc từ icon.md ----------
def meaning_groups():
    out = []
    for block in re.split(r"^### ", ICON_MD, flags=re.M)[1:]:
        title = block.split("\n")[0].strip()
        rows = re.findall(r"^\| ([^|]+?) \| `icon/([a-z0-9-]+)`", block, flags=re.M)
        if rows:
            out.append((title, rows))
    return out


GROUPS = meaning_groups()
ALL_ROWS = [r for _, rs in GROUPS for r in rs]
UNIQUE = len({n for _, n in ALL_ROWS})
DUP_ICONS = {"pencil", "check"}
DUP_MEAN = {"Công ty, đối tác", "Đối tác, hợp đồng"}


def meaning_html():
    parts = []
    for title, rows in GROUPS:
        cells = []
        for m, n in rows:
            flag = ' class="mi dup"' if n in DUP_ICONS or m in DUP_MEAN else ' class="mi"'
            own = '<span class="own">tự vẽ</span>' if (OWN_DIR / f"{n}.svg").exists() else ""
            cells.append(f'<div{flag}>{I(n, 20)}<span class="type-caption">{kit.E(m)}</span><code>{n}</code>{own}</div>')
        parts.append(f'<div class="type-label" style="margin:var(--space-lg) 0 var(--space-md)">{kit.E(title)} · {len(rows)} dòng</div><div class="mg">{"".join(cells)}</div>')
    return "".join(parts)


# ---------- Xem thử ----------
def lab(x):
    return f'<div class="type-caption tp-sub" style="margin:var(--space-md) 0 var(--space-xs)">{x}</div>'


def pv_lib(mode, platform):
    head = '<div class="pair h"><span class="type-caption tp-sub">Lucide</span><span class="type-caption tp-sub">Untitled</span><span></span></div>'
    rows = "".join(f'<div class="pair">{L(k, 24)}{U(k, 24)}<code>{k} · {UU[k][0]}</code></div>' for k in UU)
    return head + rows


def pv_stroke(mode, platform):
    def row(n):
        return (f'<tr><td>{L(n, 14)}</td><td class="sw">{L(n, 14)}</td><td>{L(n, 16)}</td><td class="sw">{L(n, 16)}</td><td>{I(n, 20)}</td><td class="sw">{I(n, 20)}</td></tr>')
    body = "".join(row(n) for n in ("search", "map-pin", "file-text", "wrench"))
    body += f'<tr><td>{O("tractor-unit", 14)}</td><td class="sw">{O("tractor-unit", 14)}</td><td>{O("tractor-unit", 16)}</td><td class="sw">{O("tractor-unit", 16)}</td><td>{O("tractor-unit", 20)}</td><td class="sw">{O("tractor-unit", 20)}</td></tr>'
    return ('<table class="szt"><thead><tr><th>14 · nét 2</th><th>14 · nét 2,25</th><th>16 · nét 2</th><th>16 · nét 2,25</th><th>20 · nét 2</th><th>20 · nét 2,25</th></tr></thead>'
            f"<tbody>{body}</tbody></table>"
            f'<div class="tp-btn sec" style="margin-top:var(--space-md)">{L("plus", 14)}<span class="type-label">Thêm điểm giao, nét 2</span></div> '
            f'<div class="tp-btn sec sw" style="margin-top:var(--space-md)">{L("plus", 14)}<span class="type-label">Thêm điểm giao, nét 2,25</span></div>')


def size_block(mode, platform):
    return (f'<div class="tp-btn sec">{kit.icon("plus", "tp-ic-sm")}<span class="type-label">Tạo lệnh</span></div>'
            f'<div class="tp-inp" style="margin-top:var(--space-md)"><span class="tp-fg2">{kit.icon("search", "tp-ic-sm")}</span><span class="type-body tp-ph" style="flex:1">Tìm mã lệnh, biển số</span><span class="tp-fg2">{kit.icon("chevron-down", "tp-ic-sm")}</span></div>'
            f'<div class="rowi"><span class="tp-fg2">{kit.icon("clipboard-list", "tp-ic-md")}</span><span class="type-body" style="flex:1">LVT-2026-0412 · Cát Lái → Long Hậu</span><span class="tp-fg2">{kit.icon("ellipsis", "tp-ic-md")}</span></div>'
            f'<div class="rowi"><span class="tp-fg2">{kit.icon("map-pin", "tp-ic-md")}</span><span class="type-body" style="flex:1">Cảng Cát Lái, cổng B</span></div>'
            f'<div class="rowi"><span class="tp-fg2">{kit.icon("bell", "tp-ic-lg")}</span><span class="tp-fg2">{kit.icon("house", "tp-ic-lg")}</span><span class="type-caption tp-sub">Cỡ lg: thanh trên, tab app</span></div>')


def pv_scale():
    a = kit.panes(size_block, modes=("light", "dark"), platforms=("web", "mobile"))
    merged = lambda m, p: f'<div style="--icon-size-sm:16px;--icon-size-md:20px;--icon-size-lg:24px">{size_block(m, p)}</div>'
    b = kit.panes(merged, modes=("light",), platforms=("web", "mobile"))
    return lab("Đang dùng: web 14 · 16 · 20, app 16 · 20 · 24") + a + lab("Gộp theo Untitled 16 · 20 · 24 cho cả hai") + b


def pv_12(mode, platform):
    return (f'<table class="tp-tb"><thead><tr><th><span class="type-caption-caps" style="display:inline-flex;gap:var(--space-xs);align-items:center">Mã lệnh {L("arrow-up-down", 12)}</span></th><th><span class="type-caption-caps" style="display:inline-flex;gap:var(--space-xs);align-items:center">Cước {L("arrow-up-down", 14)}</span></th></tr></thead>'
            f'<tbody><tr><td><span class="type-code">LVT-2026-0412</span></td><td><span class="type-body">1.250.000 ₫</span></td></tr></tbody></table>'
            + lab("Cùng hàng chữ 12/16: icon 12 bên trái, 14 bên phải")
            + f'<span class="tp-chip tp-b">Cát Lái {L("x", 12)}</span> <span class="tp-chip tp-b">Cát Lái {L("x", 14)}</span>')


def pv_odd(mode, platform):
    def f(px, ic):
        return f'<span class="fi" style="width:36px;height:36px;border-radius:var(--radius-inner);box-shadow:inset 0 0 0 1px var(--color-border-primary);color:var(--color-fg-secondary)">{L("cloud-upload", ic)}</span>'
    return (f'<div class="ir">{f(36, 16)}{f(36, 18)}{f(36, 20)}</div>' + lab("Khối 36 với icon 16 · 18 · 20")
            + f'<div class="ir"><span class="tp-btn sec">{L("rotate-cw", 16)}<span class="type-label">Thử lại</span></span><span class="tp-btn sec">{L("rotate-cw", 18)}<span class="type-label">Thử lại</span></span><span class="tp-btn sec">{L("rotate-cw", 20)}<span class="type-label">Thử lại</span></span></div>'
            + lab("Nút với icon 16 · 18 · 20")
            + f'<span class="tp-chip tp-b" style="gap:var(--space-xs)">{kit.icon("truck", "tp-ic-chip")}Đã giao lái xe</span>')


def pv_alias(mode, platform):
    r = []
    for tok, sz, label in (("--icon-size-md", "--size-xl", "icon/size/md ↔ size/xl"), ("--icon-size-lg", "--size-2xl", "icon/size/lg ↔ size/2xl")):
        r.append(f'<div class="rowi"><span class="tp-ic" style="--ic:var({tok})">{kit.icon("container", "x")[kit.icon("container", "x").find("<svg"):-7]}</span>'
                 f'<span class="tp-ic" style="--ic:var({sz})">{kit.icon("container", "x")[kit.icon("container", "x").find("<svg"):-7]}</span><span class="type-caption tp-sub">{label}</span></div>')
    return "".join(r)


def pv_pair(mode, platform):
    rows = [("type-title-3", "Thông tin chuyến", "--icon-size-lg", "route"), ("type-body", "Cảng Cát Lái, cổng B", "--icon-size-md", "map-pin"),
            ("type-label", "Tạo lệnh vận tải", "--icon-size-sm", "plus"), ("type-caption", "51C-482.15 · Nguyễn Văn Hoà", "--icon-size-sm", "tractor-unit"),
            ("type-hint", "Cước thấp hơn định mức của tuyến", "--icon-size-sm", "circle-alert")]
    out = []
    for cls, txt, var, ic in rows:
        out.append(f'<div class="pr"><span class="tp-fg2 vis">{I(ic, var)}</span><span class="{cls}" data-m>{txt}</span><code>{var[2:]}</code></div>')
    return "".join(out)


FILL7 = ["tractor-unit", "semi-trailer", "container-truck", "container-seal", "toll-booth", "container-ship", "eir"]


def pv_fill(mode, platform):
    a = "".join(f'<tr><td><span class="type-caption">{n}</span></td><td>{O(n, 24)}</td><td>{O(n + "-fill", 24)}</td><td>{O(n, 16)}</td><td>{O(n + "-fill", 16)}</td></tr>' for n in FILL7)
    b = "".join(f'<tr><td><span class="type-caption">{n}</span></td><td>{L(n, 24)}</td><td>{O(n + "-fill", 24)}</td><td>{L(n, 16)}</td><td>{O(n + "-fill", 16)}</td></tr>' for n in ("triangle-alert", "circle-alert"))
    return f'<table class="szt"><thead><tr><th></th><th>Viền 24</th><th>Tô 24</th><th>Viền 16</th><th>Tô 16</th></tr></thead><tbody>{a}{b}</tbody></table>'


def pv_on(mode, platform):
    rows = []
    for n, m, fg in (("star", "Yêu thích", "color-fg-warning-primary"), ("pin", "Ghim", "color-fg-primary"), ("flag", "Đánh dấu", "color-fg-primary")):
        rows.append(f'<tr><td><span class="type-caption">{m}</span></td><td>{L(n, 20)}</td><td style="color:var(--{fg})">{L(n, 20)}</td><td style="color:var(--{fg})" class="fillon">{L(n, 20)}</td></tr>')
    return f'<table class="szt"><thead><tr><th></th><th>Tắt</th><th>Bật, chỉ đổi màu</th><th>Bật, tô bằng fill</th></tr></thead><tbody>{"".join(rows)}</tbody></table>'


def pv_own(mode, platform):
    pairs = [("truck", "container-truck"), ("container", "semi-trailer"), ("ship", "container-ship"), ("file-text", "eir"), ("lock", "container-seal"), ("warehouse", "toll-booth")]
    body = ""
    for a, b in pairs:
        body += f'<tr><td>{I(a, 24)}</td><td>{I(b, 24)}</td><td>{I(a, 20)}</td><td>{I(b, 20)}</td><td>{I(a, 16)}</td><td>{I(b, 16)}</td><td>{I(a, 14)}</td><td>{I(b, 14)}</td></tr>'
    return (lab("L là Lucide, V là tự vẽ, số là cỡ") + '<table class="szt"><thead><tr><th>L 24</th><th>V 24</th><th>L 20</th><th>V 20</th><th>L 16</th><th>V 16</th><th>L 14</th><th>V 14</th></tr></thead>'
            f"<tbody>{body}</tbody></table>")


TONES = [("gray", "color-bg-tertiary", "color-fg-secondary", "circle-dashed", "Chưa có dữ liệu"),
         ("success", "color-bg-success-secondary", "color-fg-success-primary", "circle-check", "Hoàn thành"),
         ("warning", "color-bg-warning-secondary", "color-fg-warning-primary", "triangle-alert", "Cảnh báo"),
         ("error", "color-bg-error-secondary", "color-fg-error-primary", "circle-alert", "Lỗi"),
         ("info", "color-bg-info-secondary", "color-fg-info-primary", "info", "Thông tin")]


def fi(bg, fg, ic, box=48, px=24, shape="var(--radius-full)", extra=""):
    return f'<span class="fi" style="width:{box}px;height:{box}px;border-radius:{shape};background:var(--{bg});color:var(--{fg});{extra}">{L(ic, px)}</span>'


def tok(n):
    return n.replace("color-bg-", "color/bg/").replace("color-fg-", "color/fg/")


def pv_featured(mode, platform):
    light = "".join(f'<div class="fic">{fi(b, f, i)}<span class="type-caption tp-sub">{n}</span>{kit.cr(tok(f), tok(b), 3)}</div>' for _, b, f, i, n in TONES)
    modern = "".join(f'<div class="fic">{fi("color-bg-primary", "color-fg-secondary", i, shape="var(--radius-inner)", extra="box-shadow:inset 0 0 0 1px var(--color-border-primary)")}<span class="type-caption tp-sub">{n}</span></div>'
                     for i, n in (("cloud-upload", "Tải tệp lên"), ("search-x", "Không có kết quả")))
    solid = "".join(f'<div class="fic">{fi(b, "color-fg-white", i, shape="var(--radius-inner)")}<span class="type-caption tp-sub">{n}</span>{kit.cr("color/fg/white", tok(b), 3)}</div>'
                    for b, i, n in (("color-bg-success-solid", "circle-check", "Solid thành công"), ("color-bg-error-solid", "circle-alert", "Solid lỗi")))
    return lab("Kiểu light: tròn, nền nhạt") + f'<div class="ir">{light}</div>' + lab("Kiểu modern: vuông, viền xám, bo <code>radius/inner</code>") + f'<div class="ir">{modern}</div>' + lab("Kiểu dark của Untitled: nền đặc") + f'<div class="ir">{solid}</div>'


def pv_fsize(mode, platform):
    b, f = "color-bg-tertiary", "color-fg-secondary"
    untitled = "".join(f'<div class="fic">{fi(b, f, "container", bx, ic)}<span class="type-caption tp-sub">{bx}/{ic}</span></div>' for bx, ic in ((32, 16), (40, 20), (48, 24), (56, 28)))
    ours = "".join(f'<div class="fic">{fi(b, f, "container", bx, ic)}<span class="type-caption tp-sub">{bx}/{ic} {w}</span></div>' for bx, ic, w in ((36, 18, "Upload Compact"), (40, 20, "Upload Full web"), (48, 24, "Màn trống, app")))
    return lab("Untitled: bốn cỡ") + f'<div class="ir">{untitled}</div>' + lab("Mình đang dùng: ba cỡ") + f'<div class="ir">{ours}</div>'


def pv_color(mode, platform):
    rows = [("color/fg/primary", "Icon đang chọn, đi cùng chữ chính", "pin"), ("color/fg/secondary", "Icon mặc định", "map-pin"), ("color/fg/tertiary", "Đậm hơn một bậc, để so", "chevron-down"),
            ("color/fg/quaternary", "Icon phụ, đang dùng cho chevron, ô tìm, Help", "search"), ("color/fg/disabled", "Icon tắt, không cần đạt ngưỡng", "lock"),
            ("color/fg/error-primary", "Lỗi", "circle-alert"), ("color/fg/warning-primary", "Cảnh báo", "triangle-alert"), ("color/fg/success-primary", "Thành công", "circle-check"), ("color/fg/info-primary", "Thông tin", "info")]
    out = "".join(f'<div class="rowi"><span style="color:var({kit.v(t)})">{L(i, 20)}</span><span class="type-caption" style="flex:1"><code>{t}</code> {d}</span>'
                  + ("" if "disabled" in t else kit.cr(t, "color/bg/primary", 3)) + "</div>" for t, d, i in rows)
    field = (f'<div class="tp-inp" style="margin-top:var(--space-md)"><span style="color:var(--color-fg-quaternary)">{L("search", "--icon-size-md")}</span><span class="type-body tp-ph" style="flex:1">Ô tìm, icon quaternary</span></div>'
             f'<div class="tp-inp" style="margin-top:var(--space-sm)"><span style="color:var(--color-fg-tertiary)">{L("search", "--icon-size-md")}</span><span class="type-body tp-ph" style="flex:1">Ô tìm, icon tertiary</span></div>')
    return out + field


def pv_cat(mode, platform):
    def col(title, items):
        return f'<div class="catc"><div class="type-label">{title}</div><div class="ir" style="margin-top:var(--space-sm)">{"".join(I(n, 20) for n in items)}</div></div>'
    three = col("Hành động · 57", ["plus", "pencil", "search", "bell", "arrow-left", "house"]) + col("Đối tượng · 56", ["clipboard-list", "tractor-unit", "file-text", "receipt", "users", "wallet"]) + col("Trạng thái · 27", ["clock", "circle-check", "triangle-alert", "lock", "inbox", "wifi-off"])
    six = (col("Điều hướng", ["arrow-left", "chevron-right", "house", "menu"]) + col("Hành động", ["plus", "pencil", "search", "bell"]) + col("Trạng thái", ["clock", "circle-check", "triangle-alert", "wifi-off"])
           + col("Tệp và chứng từ", ["file-text", "eir", "receipt", "stamp"]) + col("Vận tải và địa điểm", ["tractor-unit", "container", "map-pin", "route"]) + col("Người, tài chính và khác", ["users", "wallet", "landmark", "handshake"]))
    return lab("<code>icon.md</code> mục 7: 3 nhóm") + f'<div class="cat">{three}</div>' + lab("Figma, DEC-262: 6 nhóm") + f'<div class="cat">{six}</div>'


def pv_dup(mode, platform):
    rows = [("Đã lập", "pencil", "file-pen", "Trùng với Sửa"), ("Lái xe đã nhận", "check", "user-check", "Trùng với Duyệt"), ("Công ty", "building", "building", "Tách nghĩa khỏi Đối tác"),
            ("Đối tác, hợp đồng", "handshake", "handshake", "Một nghĩa, một icon"), ("Tải lên", "upload", "cloud-upload", "Chưa có dòng, upload đang là Xuất file")]
    tr = "".join(f'<tr><td><span class="type-caption">{m}</span></td><td>{L(a, 20)}</td><td>{L(b, 20)}</td><td><span class="type-caption tp-sub">{w}</span></td></tr>' for m, a, b, w in rows)
    return f'<table class="szt left"><thead><tr><th>Nghĩa</th><th>Đang</th><th>Đề xuất</th><th></th></tr></thead><tbody>{tr}</tbody></table>'


def pv_screen(mode, platform):
    rows = [("Sửa, trên 13 màn Figma", "pen-line", "pencil"), ("Tuỳ chỉnh cột, Figma", "columns-3", "sliders-vertical"), ("Bộ lọc, <code>icon.md</code> mục 8", "funnel", "list-filter")]
    tr = "".join(f'<tr><td><span class="type-caption">{m}</span></td><td>{L(a, 20)}</td><td>{L(b, 20)}</td></tr>' for m, a, b in rows)
    return f'<table class="szt left"><thead><tr><th>Chỗ dùng</th><th>Đang</th><th>Theo bảng nghĩa</th></tr></thead><tbody>{tr}</tbody></table>'


VISA = uu_svg("payment-icons/visa-icon.tsx")


def pv_pay(mode, platform):
    a = "".join(f'<div class="fic">{L(n, 20)}<span class="type-caption tp-sub">{m}</span></div>' for n, m in (("banknote", "Tiền mặt"), ("landmark", "Ngân hàng"), ("credit-card", "Thẻ"), ("wallet", "Ví, quỹ"), ("hand-coins", "Tạm ứng")))
    return lab("Đang đủ trong bảng nghĩa") + f'<div class="ir">{a}</div>' + lab("Mẫu Payment icon của Untitled: logo Visa trong thẻ 34×24") + VISA


def pv_rule(mode, platform):
    nav = lambda x, ic, on="": f'<div class="tp-nav {on}">{I(ic, "--icon-size-md")}<span class="type-label">{x}</span></div>'
    only = lambda ic, on="": f'<div class="tp-nav {on}" style="width:max-content">{I(ic, "--icon-size-md")}</div>'
    return (lab("Icon + nhãn") + nav("Lệnh vận tải", "clipboard-list", "on") + nav("Đầu kéo", "tractor-unit") + nav("Trạm thu phí", "toll-booth")
            + lab("Chỉ có icon: icon nghiệp vụ khó đoán") + f'<div class="ir">{only("clipboard-list", "on")}{only("tractor-unit")}{only("toll-booth")}</div>'
            + lab("Chỉ có icon vẫn ổn với icon phổ quát") + f'<div class="ir">{only("search")}{only("bell")}{only("settings")}</div>')


# ---------- Phần lệch tài liệu ----------
DRIFT = kit.rows(["Ở đâu", "Đang ghi", "Thực tế"], [
    ["<code>icon.md</code> đầu file, mục 9, mục 10", "Nét 2 cho mọi icon, kể cả trong chip", "Badge dùng nét 2.5 (DEC-309, DEC-310); mục 2 cùng file đã ghi ngoại lệ"],
    ["<code>icon.md</code> đầu file", "Bốn cỡ <code>sm · md · lg · chip</code>", "Năm cỡ, thiếu <code>icon/size/ml</code> (DEC-306)"],
    ["<code>icon.md</code> mục 3", "Lý do tách cỡ theo nền tảng lấy từ DEC-143: chữ đọc app to hơn web", "DEC-322 đã đưa chữ đọc app về 14/20, bằng web"],
    ["<code>icon.md</code> mục 3.1, mục 5", "Tên <code>color/status/*-bg-strong</code>, <code>color/chip/{sắc}/fg</code>", "Đã thay bằng <code>color/bg/*</code>, <code>color/fg/*</code>, <code>color/utility/*</code> (DEC-320)"],
    ["<code>icon.md</code> mục 3.1", "Featured 48/24, vuông bo <code>radius/inner</code> 8 (DEC-328, trước ghi 14)", "Upload Full web 40/20 bo 8, Upload Compact 36/18 (<code>design-system/components/application/field-upload.md</code>)"],
    ["<code>icon.md</code> mục 3.1, <code>design-system/components/application/header-navigation.md</code>", "Featured icon chờ BL-253", "BL-253 đã đóng dạng Bỏ ngày 30/10, Featured icon chưa có component"],
    ["<code>icon.md</code> mục 10", "Màu icon ở chế độ Tối chưa xong (DEC-116)", "<code>color/fg/*</code> đã có giá trị Tối, đóng được"],
    ["<code>icon.md</code> mục 9", "Biến thể có Size=18", "Tài liệu ghi Figma chưa có; <code>_scripts/ds-v2-icons.py</code> vẫn sinh 5 biến thể"],
    ["<code>design-system/handoff/icons.json</code>", "Trỏ bản viền <code>circle-alert.svg</code>, <code>triangle-alert.svg</code> trong thư mục icon tự vẽ", "Hai file không tồn tại, bản viền của hai icon này lấy từ Lucide"],
    ["16 file trong <code>design-system/icons/</code>", "Chú thích đầu file ghi 1.8 (DEC-142): 7 bản viền, 9 bản tô", "DEC-300 đã thay bằng nét 2; 5 bản tô còn 13 chỗ <code>stroke-width=\"1.8\"</code> thật"],
    ["<code>_workspace/decisions.md</code>", "DEC-262 và DEC-304 mỗi mã có hai dòng khác nội dung", "Trích mã bị nhập nhằng, trang này ghi rõ dòng nào"],
])

CLOSED = kit.rows(["Mã", "Đã chốt"], [
    ["DEC-141, DEC-156", "Lucide bản 1.58.0 cho cả web và app, không trộn bộ khác."],
    ["DEC-300", "Nét 2 trên khung 24, co theo cỡ."],
    ["DEC-309, DEC-310", "Icon trong Badge cỡ 14, nét 2.5."],
    ["DEC-144", "Tab và mục menu đang chọn giữ icon viền, nhận ra bằng nền và màu."],
    ["DEC-145, DEC-154", "Bảy icon nghiệp vụ tự vẽ theo lưới và nét Lucide; cảng là tàu container."],
    ["DEC-146", "Mỗi nghĩa đúng một icon, tra bảng chứ không tự chọn."],
    ["DEC-147, DEC-202", "Trên Figma mỗi icon là component set, mỗi cỡ một lớp nét <code>Vector</code>."],
    ["DEC-258", "Không phóng icon, nhấn mạnh bằng Featured icon."],
    ["DEC-306", "Thang có thêm cỡ 18 cho 3 chỗ dùng."],
    ["DEC-320", "<code>fg/*</code> theo Untitled; nguyên văn: \"<code>fg/quaternary</code> chấp nhận 2,52:1\"."],
    ["DEC-322", "Chữ một bộ cho web và app, chữ đọc app 14/20."],
])

PROPOSAL = kit.rows(["Mục", "Sẽ xảy ra", "Màn đổi không"], [
    ["ic00, ic01, ic02, ic04, ic09, ic12", "Giữ Lucide, nét 2 không bù, hai cột cỡ web, app, cỡ 14 và 18, <code>color/fg/quaternary</code> như DEC-320. Sổ quyết định ghi lại lý do tách cỡ", "Không"],
    ["ic03", "Thêm <code>icon/size/xs</code>: web 12, app 14", "Không, thêm cỡ mới"],
    ["ic05", "<code>icon/size/*</code> trỏ vào <code>size/*</code>, 14 và 18 giữ số trần", "Không"],
    ["ic06, ic17", "Ghi vào <code>icon.md</code>: bảng ghép cỡ chữ, luật nhãn, luật <code>aria-hidden</code>", "Không"],
    ["ic07", "Bỏ 7 bản tô nghiệp vụ theo DEC-262, giữ 2 bản tô cảnh báo và lỗi", "Có, chỗ đang dùng bản tô nghiệp vụ"],
    ["ic08", "Star, pin, flag bật bằng fill trên chính path Lucide", "Thêm mới"],
    ["ic10, ic11", "Featured còn 2 kiểu, 3 cỡ 48, 40, 36 có token riêng. Vuông bo <code>radius/inner</code>", "Web không đổi, vẫn 40 và 8. App: tài liệu 14 → 8, chưa có khối vuông nào trên app"],
    ["ic13, ic14, ic15", "Bảng nghĩa theo 6 nhóm Figma, sửa 3 chỗ trùng nghĩa, máy kiểm icon ngoài bảng khi rà màn", "Có, 2 icon chip"],
    ["ic16", "Không lấy Payment, Social, Integration của Untitled", "Không"],
])

# ---------- Số đếm ----------
SECTIONS = [
    dict(title="Bảng icon mẫu đủ các cỡ", intro="Mỗi icon vẽ thật ở 6 cỡ, Lucide qua lucide-static 1.58.0, icon tự vẽ đọc từ <code>design-system/icons/</code>. Nét trong đầu cột là số điểm ảnh thật theo DEC-300, không phải thuộc tính đặt riêng từng cỡ. Hãy nhìn hàng tự vẽ ở cột 12 và 14: chi tiết bắt đầu dính nhau.",
         html=kit.panes(size_table, modes=("light", "dark"))),
    dict(title="Bảng đối chiếu thư viện và kỹ thuật — Untitled ↔ mình", intro="Nguồn: <code>design/_ref/untitled-ui/06-icons.md</code>, code React của Untitled. Số lần <code>size-*</code> và <code>stroke-[…]</code> đếm trong <code>base</code> và <code>application</code>, <mark>đã bỏ file story và demo</mark>, vẫn gồm vài phần tử không phải icon.", html=kit.rows(H, LIB_ROWS)),
    dict(title="Bảng đối chiếu thang cỡ — Untitled ↔ mình", intro="Untitled không có token cỡ icon, chỉ có lớp <code>size-*</code>. Hướng dẫn của họ nêu ba cỡ chuẩn 16, 20, 24.", html=kit.rows(["Cỡ", "Untitled UI v8", "Mình", "Trạng thái", "Mục chọn"], SIZE_ROWS)),
    dict(title="Bảng đối chiếu Featured icon — Untitled ↔ mình", intro="Nguồn: <code>design/_ref/untitled-ui/react/components/foundations/featured-icon/featured-icon.tsx</code>. Trong code component của Untitled chỉ có kiểu <code>modern</code> màu xám được dùng.", html=kit.rows(H, FEATURED_ROWS)),
    dict(title="Bảng đối chiếu màu icon — Untitled ↔ mình", intro="So bậc màu trong thang, cột giá trị ghi Sáng · Tối. Ba dòng Khác có lý do chỉ lệch ở Tối: mình lấy bậc sáng hơn của dải (DEC-316). Đọc thẳng từ <code>design/_ref/untitled-ui/react/styles/theme.css</code> và <code>design-system/tokens.css</code>.", html=kit.rows(["Token Untitled", "Untitled", "Mình", "Trạng thái", "Mục chọn"], FG_ROWS)),
    dict(title="Bảng đối chiếu bộ phụ và luật dùng — Untitled ↔ mình", html=kit.rows(H, EXTRA_ROWS + RULE_ROWS)),
    dict(title=f"Bảng nghĩa: {len(ALL_ROWS)} dòng, {UNIQUE} icon", intro="Đọc từ <code>design-system/foundations/icon.md</code> mục 7, đã kiểm cả 138 tên đều có trong lucide-static 1.58.0 hoặc <code>design-system/icons/</code>. Ô viền cam là chỗ trùng nghĩa, xem mục ic14. Nhóm Hành động và Đối tượng theo tài liệu, chưa phải 6 nhóm trên Figma.",
         html=kit.panes(meaning_html(), modes=("light",))),
    dict(title="Chỗ tài liệu đang lệch nhau", intro="Không cần chọn. Bạn chốt xong, mình sửa các dòng này cùng lượt.", html=DRIFT),
    dict(title="Đã chốt, không mở lại", intro="Các quyết định đang hiệu lực. Mục nào muốn mở lại sẽ viết rõ \"Mở lại DEC-x:\" ở phương án.", html=CLOSED),
    dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", html=PROPOSAL),
]

# ---------- Mục chọn ----------
ITEMS = [
    dict(id="ic00", grp="Thư viện", title="Giữ Lucide hay đổi sang Untitled Icons?",
         why=f"Mình đang có <mark>{UNIQUE} icon trong bảng nghĩa</mark> và màn đã duyệt đều theo tên Lucide (DEC-141, DEC-156). Đã quét 1.181 file icon miễn phí của Untitled: <mark>không có tên nào chứa</mark> forklift, warehouse, fuel, ship, road, gauge, barcode, stamp, factory. Các nghĩa đó đang có sẵn trong Lucide. Trang này không có bằng chứng mới để mở lại DEC-141, mục chỉ để bạn thấy hai bộ cạnh nhau.",
         untitled="<code>@untitledui/icons</code> 0.0.23, MIT, 1.181 file. Nét 2, khung 24, có số thứ tự kiểu <code>Truck01</code>.",
         ours="Lucide 1.58.0, <code>design-system/foundations/icon.md</code> mục 1. Web và app chung một bộ.",
         astryx="Cũng dùng Lucide, <code>design/design.md</code> mục Iconography. Nên đã có lịch sử màn cùng tên.",
         pv=kit.panes(pv_lib, modes=("light", "dark")),
         opts=[("keep", "Giữ Lucide 1.58.0, không đổi màn nào", True), ("uu", "Mở lại DEC-141: đổi sang Untitled, vẽ thêm các icon vận tải còn thiếu và đổi tên mọi instance", False)]),
    dict(id="ic01", grp="Độ dày nét", title="Icon cỡ 16 trở xuống có bù nét như Untitled không?",
         why="DEC-300 chốt nét 2 trên khung 24 cho mọi icon, ở cỡ 14 còn <mark>1,17px</mark>. Untitled tự nâng lên <code>2.25</code> ở cỡ 16 tại <mark>33 chỗ</mark> trong code, tức 1,5px. Số đó chưa nằm trong dữ kiện lúc chốt nên mới đưa ra hỏi. Trang này chưa có phản ánh nào từ người dùng về nét mảnh, và Badge đã có ngoại lệ 2.5 (DEC-309). Khuyến nghị giữ.",
         untitled="<code>*:data-icon:stroke-[2.25px]</code> ở nút sm, Featured sm. Nét 2 ở các cỡ còn lại.",
         ours="<code>strokeWidth={2}</code> (DEC-300), ngoại lệ Badge 2.5. <code>icon.md</code> mục 2.",
         astryx="Nét 1.8 trên khung 24, chip nét 2. DEC-142 đã bị DEC-300 thay.",
         pv=kit.panes(pv_stroke, modes=("light", "dark")),
         opts=[("keep", "Giữ nét 2 mọi cỡ, Badge vẫn 2.5, không đổi màn nào", True), ("comp", "Mở lại DEC-300: nét 2,25 cho cỡ 14 và 16, sửa biến thể trên Figma, bỏ ngoại lệ Badge", False)]),
    dict(id="ic02", grp="Thang cỡ", title="Thang cỡ gộp một bộ hay giữ hai cột Web, App?",
         why="Lý do tách của DEC-143 là chữ đọc app 15 to hơn web. <mark>DEC-322 đã đưa chữ app về 14/20</mark>, nên lý do đó hết hiệu lực và phải hỏi lại. Lý do còn lại là <mark>cao control</mark> vẫn khác: <code>control/height/md</code> web 32, app 42, và app lái xe dùng ngoài trời, ngón tay to. Gộp 16 · 20 · 24 cho web khiến icon hàng bảng từ 16 lên 20, nút 28 chật.",
         untitled="Không có token, lớp <code>size-4</code>, <code>size-5</code>, <code>size-6</code>. Một bộ cho mọi màn, nút sm 16, nút md trở lên 20.",
         ours="<code>icon/size/sm</code> 14 · 16, <code>icon/size/md</code> 16 · 20, <code>icon/size/lg</code> 20 · 24 (DEC-143).",
         astryx="Web cỡ 16 mặc định, 14 trong nút, 18 hiếm. Không có cột app riêng.",
         note="Phụ thuộc sp10 (nút MD app cao 42 trên trang Khoảng cách): chọn giữ 42 hay đổi 44 thì app vẫn cao hơn web 32, khuyến nghị ở đây không đổi.",
         pv=pv_scale(),
         opts=[("keep", "Giữ hai cột, ghi lại lý do là cao control và dùng ngoài trời, không đổi màn nào", True), ("merge16", "Mở lại DEC-143: gộp 16 · 20 · 24, mọi icon web to thêm 2–4px", False), ("merge14", "Mở lại DEC-143: gộp 14 · 16 · 20, mọi icon app nhỏ đi 2–4px, thanh tab còn 20", False)]),
    dict(id="ic03", grp="Thang cỡ", title="Có thêm token cho cỡ 12 không?",
         why="<code>icon.md</code> ghi cỡ 12 là dự phòng, chưa có token. Đo trên DS v2: <mark>7 component đang vẽ icon 12 trong preview</mark> <code>_work/*/page.json</code>, đều là số trần: xoá trong tag, ô chọn nhiều, ô nhập, dòng tệp (<code>tag</code>, <code>multiselect</code>, <code>input</code>, <code>field-upload</code>); dấu tick ô chọn trong <code>tag</code>, <code>multiselect</code>, <code>form-controls</code>; mũi tên bước số <code>input</code>; máy ảnh Avatar <code>badge-avatar</code> (Avatar hiện theo DEC-303); chevron, dấu ngăn, ghim chi nhánh <code>header-navigation</code>. File md chỉ ghi số ở vài dòng, chưa dùng token. Nguồn phụ: báo cáo <code>docs/reports/figma-audit/2026-10-13-cross-process-flow-figma-audit.md</code> đếm 114 icon cỡ 12 trên 41 màn, nhưng đó là file Figma cũ v0.3, không lấy làm bằng chứng chính. Token này có người dùng ngay nên giữ khuyến nghị thêm.",
         untitled="<code>size-3</code>, 18 lần trong code. Không có tên token.",
         ours="Không có. <code>icon/size/sm</code> 14 là bậc nhỏ nhất, preview ghi 12 trần. Biến thể Figma <code>Size=12</code> đã có (DEC-147).",
         astryx="<code>Icon</code> cỡ xsm 12, nằm trong bộ 4 cỡ của thư viện.",
         tokens=[("icon/size/xs", "12 · 14", "Web: xoá tag, dấu tick, dấu ngăn, mũi tên bước số. App: bằng <code>icon/size/chip</code>, chưa kiểm app từng component")],
         pv=kit.panes(pv_12, modes=("light", "dark")),
         opts=[("add", "Thêm icon/size/xs: web 12, app 14", True), ("up", "Không thêm, icon 12 trong 7 component lên 14 khi sync", False)]),
    dict(id="ic04", grp="Thang cỡ", title="Hai cỡ lẻ 18 và chip 14 giữ hay bỏ?",
         why="<code>icon/size/ml</code> 18 chỉ có <mark>1 component</mark> dùng (<code>field-upload</code>), nhưng <mark>DEC-306 mới chốt ba ngày trước</mark>. Số dùng trên màn có hai nguồn lệch nhau: DEC-306 ghi 102 chỗ (câu đó gộp cả tổ hợp chữ 12.5/18), báo cáo file Figma cũ v0.3 ngày 13/10 đếm 106 icon cỡ 18; chưa đo trên file mới. <code>icon/size/chip</code> 14 chỉ Badge dùng, cần riêng vì Badge giữ 14 trên app trong khi <code>icon/size/sm</code> app là 16 (DEC-310). Không có bằng chứng mới để mở lại.",
         untitled="Không có 18. 14 là <code>size-3.5</code>, 12 lần trong code.",
         ours="<code>icon/size/ml</code> 18 · 18 (DEC-306), <code>icon/size/chip</code> 14 · 14 (DEC-310). Số dùng ở <code>design-system/_review/token-usage.json</code>.",
         astryx="18 ghi là hiếm, icon đứng riêng cần nổi hơn chữ 14. 14 cho chip trạng thái.",
         pv=kit.panes(pv_odd, modes=("light", "dark")),
         opts=[("keep", "Giữ cả hai, ghi rõ 18 chỉ cho 3 chỗ của DEC-306, không mở chỗ mới", True), ("drop18", "Mở lại DEC-306: bỏ 18, Upload Compact và nút lớn app chuyển sang 20, phải sửa field-upload", False)]),
    dict(id="ic05", grp="Thang cỡ", title="Token cỡ icon có trỏ vào thang size/* không?",
         why="DEC-314 chốt <mark>token theo vai trỏ vào thang</mark>, nhưng cả 5 token <code>icon/size/*</code> đang là số trần. Năm giá trị đang có (14, 16, 18, 20, 24) thì 16, 20, 24 có bậc sẵn; <mark>14 và 18 không có bậc</mark> trên thang <code>size/*</code>. Thêm hai bậc đó sẽ làm nhiễu thang chung vốn theo Untitled. Nhìn màn không đổi, chỉ đổi cách khai báo.",
         untitled="Untitled không có token cỡ icon để đối chiếu, dùng thẳng <code>size-4</code> của Tailwind, cùng thang với khoảng cách.",
         ours="<code>--icon-size-md: 16px</code> trong <code>design-system/tokens.css</code>. Thang <code>size/xl</code> 16, <code>size/2xl</code> 20, <code>size/3xl</code> 24.",
         astryx="Cỡ icon ghi bằng số trong tài liệu, không có token.",
         tokens=[("icon/size/md", "size/xl · size/2xl", "Trỏ vào thang, web 16, app 20"), ("icon/size/lg", "size/2xl · size/3xl", "Trỏ vào thang, web 20, app 24"), ("icon/size/sm", "14 · size/xl", "Web giữ số trần 14 vì thang không có bậc này"), ("icon/size/xs", "size/lg · 14", "Chỉ khi chọn thêm ở ic03: web 12 có sẵn <code>size/lg</code>, app số trần 14")],
         pv=kit.panes(pv_alias, platforms=("web", "mobile"), modes=("light",)),
         opts=[("alias", "Trỏ 16, 20, 24 vào size/*, giữ 14 và 18 số trần có ghi lý do, màn không đổi", True), ("addstep", "Thêm bậc 14 và 18 vào thang size/*, thang chung lệch Untitled", False), ("raw", "Giữ toàn bộ số trần", False)]),
    dict(id="ic06", grp="Thang cỡ", title="Có ghi bảng ghép cỡ icon với cỡ chữ không?",
         why="Hiện <code>icon.md</code> chỉ ghi chỗ dùng, chưa nói icon nào đi với chữ nào. Sau DEC-322 chữ web và app bằng nhau, nên <mark>mỗi bên một tỉ lệ khác</mark>: chữ 14 đi với icon 16 trên web, 20 trên app. Đề xuất luật đo được: <mark>icon không cao hơn dòng chữ cạnh nó</mark>, để icon không đẩy hàng cao lên. Chữ 14/20 ôm vừa cả 16 và 20; <code>type/hint</code> 12/18 đi với 14 hoặc 16 đều không đội dòng.",
         untitled="Không ghi thành luật. Nút cỡ sm chữ 14 icon 16, cỡ md chữ 14 icon 20. Chung lớp <code>size-*</code>.",
         ours="<code>icon.md</code> mục 3 ghi theo chỗ dùng. Upload ghi lệch tay 2px cho chữ lỗi: <code>design-system/components/application/field-upload.md</code>.",
         astryx="Chỉ ghi cỡ 14 trong nút có chữ, 16 mặc định. Màu theo chữ cạnh nó.",
         pv=kit.panes(pv_pair, modes=("light", "dark"), platforms=("web", "mobile")),
         opts=[("rule", "Ghi bảng ghép và luật icon không cao hơn dòng chữ vào icon.md", True), ("no", "Không ghi, mỗi component tự chọn cỡ", False)]),
    dict(id="ic07", grp="Nét đặc", title="Bản tô của 7 icon nghiệp vụ còn giữ không?",
         why="Hai nguồn đang cãi nhau. <mark>DEC-262 (dòng về icon tự vẽ, 27/10)</mark> trích lời bạn: \"bỏ luôn biến thể đặc\". Nhưng <code>icon.md</code> mục 4, mục 6 vẫn ghi \"có bản tô\", <code>design-system/handoff/icons.json</code> còn trỏ file, và 7 file <code>-fill</code> vẫn trên đĩa. 5 trong số đó còn <mark>13 chỗ nét 1.8</mark>, sai DEC-300. Riêng cảnh báo, lỗi thì DEC-141 cần bản tô. Lượt này chưa đọc Figma nên chưa biết trên đó đã xoá chưa.",
         untitled="Bản miễn phí chỉ có line. Solid, duotone thuộc PRO, nhập riêng <code>@untitledui-pro/icons/solid</code>.",
         ours="9 file <code>-fill</code> trong <code>design-system/icons/</code>. DEC-144: tab, menu đang chọn không tô.",
         astryx="Lucide nét, không tô.",
         pv=kit.panes(pv_fill, modes=("light", "dark")),
         opts=[("drop7", "Bỏ 7 bản tô nghiệp vụ theo DEC-262, giữ 2 bản tô cảnh báo và lỗi, sửa tài liệu và handoff", True), ("keep9", "Mở lại DEC-262: giữ cả 9, vẽ lại 5 bản còn nét 1.8 về nét 2", False)]),
    dict(id="ic08", grp="Nét đặc", title="Trạng thái bật của yêu thích, ghim, đánh dấu vẽ thế nào?",
         why="<code>icon.md</code> mục 10 đang để mở. DEC-141 muốn tô cho trạng thái bật nhưng bảng nghĩa chưa có bản tô cho <code>star</code>, <code>pin</code>, <code>flag</code>. Tô bằng <mark>fill trên chính path Lucide</mark> không cần vẽ file mới và không đi ngược DEC-262, vì đây không phải biến thể đặc của icon nghiệp vụ. Chỉ đổi màu thì người mù màu và ảnh đen trắng không phân biệt được bật với tắt.",
         untitled="Trong bản miễn phí chỉ có line. Star icon riêng thuộc <code>Misc icons</code>, <code>rating-stars.tsx</code> dùng hình tô.",
         ours="Chưa có. <code>Fill=On</code> chỉ có ở 9 icon. <code>icon.md</code> mục 4, mục 10.",
         astryx="Không có quy định trạng thái bật.",
         pv=kit.panes(pv_on, modes=("light", "dark")),
         opts=[("fill", "Thêm Fill=On cho 3 icon bằng fill trên path Lucide", True), ("color", "Chỉ đổi màu, không tô", False)]),
    dict(id="ic09", grp="Nét đặc", title="Icon tự vẽ có đạt cùng ngôn ngữ nét với Lucide không?",
         why="Đo trong file: cả 7 bản viền đều <mark>nét 2, đầu nét và góc bo tròn</mark>, khung 24, giống Lucide. Khác ở độ dày chi tiết: <code>container-truck</code> <mark>10 phần tử</mark>, <code>tractor-unit</code> 8, trong khi <code>truck</code> của Lucide chỉ 5. Ở cỡ 14 các nét bánh và thùng dính lại; <code>semi-trailer</code> và <code>toll-booth</code> hình thấp nên trông nhẹ hơn icon Lucide cùng cỡ. Không icon chip nào là icon tự vẽ, nên chặn cỡ dưới 16 không làm hỏng màn nào đã biết.",
         untitled="Không có icon vận tải tương ứng. Chỉ có <code>Truck01</code>, <code>Container</code>, <code>Anchor</code>.",
         ours="7 file viền trong <code>design-system/icons/</code>, DEC-145, DEC-149…155 qua <code>icon.md</code> mục 6.",
         astryx="Không có icon nghiệp vụ tự vẽ.",
         pv=kit.panes(pv_own, modes=("light", "dark")),
         opts=[("min16", "Giữ nguyên 7 hình, ghi luật icon tự vẽ không dùng dưới 16", True), ("redraw", "Vẽ lại container-truck và tractor-unit bớt chi tiết để dùng được ở 14", False), ("none", "Không đặt giới hạn", False)]),
    dict(id="ic10", grp="Featured icon", title="Featured icon lấy những kiểu nền nào?",
         why="Untitled có 6 kiểu nhưng code component của họ <mark>chỉ dùng <code>modern</code></mark>. Mình cần đúng hai việc: báo kết quả có màu (màn trống, màn kết quả, đầu hộp thoại) và ô tải lên trung tính. Kiểu light hợp việc thứ nhất, modern hợp việc thứ hai. Nền đặc gây chú ý quá mức trên màn điều vận dày dữ liệu. Góc vuông chốt <mark><code>radius/inner</code>: 8 cả web và app (<code>DEC-328</code>)</mark>. Upload web thật đang bo 8 nên số không đổi. <code>icon.md</code> mục 3.1 từng ghi 14 là lệch tài liệu, không phải số trên màn; 14 cũng không có trong thang (DEC-315). Đã sửa cùng DEC-328.",
         untitled="<code>light</code>, <code>gradient</code>, <code>dark</code>, <code>modern</code>, <code>modern-neue</code>, <code>outline</code> × brand, gray, error, warning, success.",
         ours="<code>icon.md</code> mục 3.1 (DEC-258) ghi tròn hoặc vuông bo <code>radius/inner</code> 8 (DEC-328, trước ghi 14). Chưa có component vì BL-253 đã bỏ. Upload tự dựng, web bo 8: <code>design-system/components/application/field-upload.md</code>.",
         astryx="Không có Featured icon. Thẻ bản ghi mobile có icon tròn 36, không thành thang.",
         note="Tỉ lệ đo ngay trên trang, ngưỡng 3:1 của đồ hoạ. Cả 5 sắc kiểu light đều đạt ở Sáng và Tối, thấp nhất là thành công trên nền Sáng. Trang Bo góc đã chốt rd09 (<code>DEC-328</code>): Upload gọi <code>radius/inner</code> như mục này.",
         pv=kit.panes(pv_featured, modes=("light", "dark"), platforms=("web", "mobile")),
         opts=[("two", "Hai kiểu: light tròn 5 sắc, modern vuông xám bo radius/inner, Upload web giữ 8", True), ("three", "Thêm kiểu dark nền đặc cho kết quả quan trọng", False), ("one", "Chỉ light, Upload đổi sang tròn", False)]),
    dict(id="ic11", grp="Featured icon", title="Featured icon cần mấy cỡ?",
         why="Chỗ dùng thật có <mark>ba cỡ</mark>: 48/24 ở màn trống, màn kết quả, ô tải lên app; <mark>40/20 ở Upload Full web</mark> (<code>design-system/components/application/field-upload.md</code>, <code>design-system/components/_work/field-upload/check.json</code>); 36/18 ở Upload Compact. Khối 40 mượn <code>control/height/lg</code>, thành 52 nếu gọi trên app. Khối 36 mượn <code>control/height/ml</code>, thành 42 trên app, và DEC-304 đã huỷ chỗ dùng gốc của token đó. Câu cần hỏi riêng là <mark>có giữ 40 không</mark>: <code>icon.md</code> mục 3.1 chỉ ghi 48. Untitled có 32 và 56, màn của mình chưa cần; luật không phóng quá 24 (DEC-258) cũng loại 56/28.",
         untitled="<code>sm</code> 32/16 · <code>md</code> 40/20 · <code>lg</code> 48/24 · <code>xl</code> 56/28. Dùng thật: sm ở ô tìm, md ở File upload, lg và xl ở Empty state.",
         ours="<code>featured-icon/size</code> 48. Khối 40 qua <code>control/height/lg</code>, khối 36 qua <code>control/height/ml</code>, icon <code>icon/size/lg</code>, <code>icon/size/ml</code>.",
         astryx="Không có. Avatar 36, 48 có cùng số nhưng khác vai.",
         tokens=[("featured-icon/size-md", "40", "Upload Full web, icon 20, cùng số với <code>md</code> của Untitled"), ("featured-icon/size-compact", "36", "Upload Compact, icon 18. Không đặt <code>size-sm</code> vì <code>sm</code> của Untitled là 32")],
         pv=kit.panes(pv_fsize, modes=("light", "dark")),
         opts=[("three", "Giữ ba cỡ 48, 40, 36, thêm token riêng, ngừng mượn control/height, Upload không đổi hình", True), ("no40", "Bỏ 40: Upload Full web đổi từ 40/20 lên 48/24, ô cao thêm 8", False), ("no36", "Bỏ 36: Upload Compact đổi từ 36/18 lên 40/20, ô cao thêm 4", False), ("uu", "Bốn cỡ theo Untitled 32, 40, 48, 56, Upload Compact đổi sang 40/20", False)]),
    dict(id="ic12", grp="Màu", title="Icon phụ dùng color/fg/quaternary: giữ theo DEC-320 hay mở lại?",
         why="Foundation Màu đã duyệt ngày 01/11, DEC-320 ghi nguyên văn: \"<code>fg/quaternary</code> chấp nhận 2,52:1\" và đã bỏ phương án giữ 500. Bậc này có <mark>14 component</mark> dùng trực tiếp, gồm chevron ô chọn, icon ô tìm, Help. Đo lại trên trang: Sáng 2,52:1 đúng số đã chấp nhận; <mark>Tối 2,25:1</mark> là số DEC-320 không ghi. App ngoài nắng chưa có số đo. Hai điều đó chưa đủ làm bằng chứng mới, nên khuyến nghị giữ. Chờ phản ánh từ thử thực tế rồi mới mở lại.",
         untitled="<code>fg-quaternary</code>: \"icons in buttons, help icons and icons used in input fields\". Sáng neutral-400, Tối neutral-600.",
         ours="<code>icon.md</code> mục 5: mặc định <code>color/fg/secondary</code>, icon phụ <code>color/fg/quaternary</code>. Số dùng: <code>design-system/_review/token-usage.json</code>.",
         astryx="Icon phụ dùng <code>icon-secondary</code> #737373 trên nền Sáng, đạt 3:1.",
         note="Nhãn đỏ ở dòng <code>color/fg/quaternary</code> (2,52:1 và 2,25:1, ngưỡng 3:1) là cố ý để lộ số đo, DEC-320 đã chấp nhận số Sáng.",
         pv=kit.panes(pv_color, modes=("light", "dark"), platforms=("web",)),
         opts=[("keep", "Giữ color/fg/quaternary như DEC-320, không đổi màn nào", True), ("rule", "Giữ token, đổi luật: icon phụ mang nghĩa sang color/fg/tertiary, 14 component đậm hơn một bậc", False), ("raise", "Mở lại DEC-320: nâng color/fg/quaternary lên bậc 500, trùng bậc với quaternary_hover", False)]),
    dict(id="ic13", grp="Danh mục", title="Bảng nghĩa chia nhóm theo cách nào?",
         why="Tài liệu và Figma đang <mark>chia khác nhau</mark>: <code>icon.md</code> mục 7 có 3 nhóm (DEC-146), Figma có 6 nhóm (DEC-262). Người tra trong Figma và AI tra tài liệu không thấy cùng một thứ tự. Chia 19 nhóm như Untitled không hợp: Weather, Education, Editor không có icon nào của mình, mà 140 dòng chia 19 nhóm thì nhóm nào cũng lẻ tẻ.",
         untitled="19 nhóm: Weather, Maps &amp; travel, Files, Time, Editor, Communication, Images, Media &amp; devices, Users, Shapes, Alerts &amp; feedback, General, Finance &amp; eCommerce, Arrows, Development, Education, Security, Charts, Layout. Nguồn <code>06-icons.md</code> mục 4.",
         ours="<code>icon.md</code> mục 7: Hành động 57, Đối tượng 56, Trạng thái 27. Figma: 6 nhóm, chưa đếm lại từng nhóm ở lượt này.",
         astryx="Một danh sách icon theo hành động, không chia nhóm, <code>design/design.md</code>.",
         pv=kit.panes(pv_cat, modes=("light",)),
         opts=[("six", "Tài liệu chia theo 6 nhóm Figma, một thứ tự cho cả hai nơi", True), ("three", "Giữ 3 nhóm, đổi Figma về 3 nhóm", False), ("untitled", "Chia lại theo 19 nhóm của Untitled", False)]),
    dict(id="ic14", grp="Nghĩa", title="Sửa những chỗ một icon hai nghĩa, một nghĩa hai icon?",
         why="DEC-146 quy định <mark>mỗi nghĩa đúng một icon</mark>. Quét 140 dòng ra: <code>pencil</code> vừa là Sửa vừa là Đã lập, <code>check</code> vừa là Duyệt vừa là Lái xe đã nhận, chữ <mark>đối tác</mark> nằm ở cả <code>building</code> và <code>handshake</code>. Ngoài ra chưa có dòng Tải lên trong khi <code>upload</code> đang mang nghĩa Xuất file. Hai icon chip thuộc DEC-029 đã duyệt nên phải hỏi trước khi đổi.",
         untitled="Không có bảng nghĩa. File upload dùng <code>UploadCloud02</code>, hình đám mây, tách hẳn với xuất file.",
         ours="<code>icon.md</code> mục 7, 140 dòng, 138 icon. Bản máy đọc: <code>design-system/handoff/icons.json</code>.",
         astryx="Xuất file <code>upload</code>, Duyệt <code>check</code>, trong danh sách hành động của <code>design/design.md</code>.",
         pv=kit.panes(pv_dup, modes=("light", "dark")),
         opts=[("fix", "Đổi 2 icon chip sang file-pen, user-check, tách nghĩa đối tác, thêm dòng Tải lên", True), ("soft", "Cho phép một icon hai nghĩa khi khác nhóm, chỉ tách đối tác và thêm Tải lên", False), ("keep", "Giữ nguyên bảng", False)]),
    dict(id="ic15", grp="Nghĩa", title="Icon dùng sai trên màn xử lý lúc nào?",
         why="Báo cáo <code>docs/reports/figma-audit/2026-10-13-cross-process-flow-figma-audit.md</code> (41 màn, file v0.3): <code>pen-line</code> trên <mark>13 màn</mark> trong khi bảng nghĩa là <code>pencil</code>; nút Tuỳ chỉnh cột dùng <code>columns-3</code> thay <code>sliders-vertical</code>. <code>icon.md</code> mục 10 còn nêu <code>funnel</code> nhưng báo cáo này không thấy, chỉ có <code>funnel-x</code> hợp lệ. Số này từ file Figma cũ, lượt này không đọc Figma nên chưa có số mới. Màn mẫu trên đầu trang đã sửa 5 tên icon cho khớp bảng nghĩa; riêng Phương tiện dùng <code>container</code> vì bảng chưa có dòng nghĩa này.",
         untitled="Luật 2 của <code>06-icons.md</code>: dùng icon phổ quát. Không có máy kiểm.",
         ours="<code>icon.md</code> mục 8, mục 10: gộp ở vòng 6. <code>_scripts/figma-name-lint.js</code> chưa đối chiếu bảng nghĩa.",
         astryx="<code>/figma-audit</code> so với danh sách của <code>design/design.md</code>, như báo cáo trên.",
         pv=kit.panes(pv_screen, modes=("light", "dark")),
         opts=[("audit", "Thêm kiểm icon ngoài bảng nghĩa vào /figma-audit, sửa màn khi dựng lại ở vòng 6 (đợt đổi instance sang bộ mới)", True), ("now", "Sửa ngay 41 màn cũ trước khi có DS mới", False), ("doc", "Chỉ cập nhật danh sách trong tài liệu, không có máy kiểm", False)]),
    dict(id="ic16", grp="Bộ phụ", title="Lấy Payment, Social, Integration icons của Untitled không?",
         why="Ba bộ gồm <mark>56 + 22 + 16 logo thương hiệu</mark>. Payment không có MoMo, VNPay, Napas; Social không có Zalo; Integration là công cụ AI và framework. Không màn logistics nào cần chúng. Thanh toán trong nghiệp vụ đã đủ bằng <code>banknote</code>, <code>landmark</code>, <code>credit-card</code>, <code>wallet</code>, <code>hand-coins</code>. Khi cần logo ngân hàng Việt Nam thì đó là ảnh thương hiệu, thuộc trang Logo.",
         untitled="<code>foundations/payment-icons</code>, <code>social-icons</code>, <code>integration-icons</code>. Dùng thật ở <code>input-payment.tsx</code>, <code>dropdown-integration.tsx</code>.",
         ours="Không có. <code>icon.md</code> mục 7 có các nghĩa thanh toán bằng icon Lucide.",
         astryx="Không có bộ logo thương hiệu trong <code>design/design.md</code>.",
         note="Riêng File type icon: <code>design-system/components/application/field-upload.md</code> nhắc \"File type icon (Misc icons)\" nhưng <code>design-system/foundations/vehicle.md</code> chỉ nói về phương tiện. Đề xuất tạm cho tới khi có bộ riêng: dùng <code>file-text</code>, <code>file-spreadsheet</code>. Icon phương tiện xem ở <code>vehicle.md</code>, ngoài phạm vi trang này.",
         pv=kit.panes(pv_pay, modes=("light", "dark")),
         opts=[("no", "Không lấy cả ba, logo đối tác Việt Nam thêm riêng ở trang Logo khi có màn cần", True), ("pay", "Lấy Payment và Social, chịu chi phí 78 component ít khi dùng", False)]),
    dict(id="ic17", grp="Luật dùng", title="Thêm luật về nhãn và trình đọc màn hình?",
         why="<code>06-icons.md</code> mục 8 có hai luật <code>icon.md</code> chưa ghi: <mark>icon không thay chữ</mark> trừ icon phổ quát, và <mark>icon trang trí đặt <code>aria-hidden</code></mark>. App lái xe và màn điều vận có nhiều icon nghiệp vụ tự vẽ, người mới không đoán được nếu thiếu nhãn. Nút chỉ có icon đã có Tooltip (<code>design-system/components/base/tooltip.md</code>), luật chỉ cần trỏ về đó.",
         untitled="Luật 3: mặc định icon + nhãn, chỉ bỏ nhãn với search, help, delete, edit, save, link. <code>aria-hidden=\"true\"</code> cho icon trang trí.",
         ours="Chưa có trong <code>icon.md</code>. <code>design-system/foundations/touch-focus.md</code> lo vùng chạm.",
         astryx="Menu thu gọn 64 chỉ còn icon, không kèm luật tên truy cập. <code>design/design.md</code>.",
         pv=kit.panes(pv_rule, modes=("light", "dark"), platforms=("web", "mobile")),
         opts=[("add", "Thêm 3 câu: mặc định có nhãn, nút chỉ icon phải có tên truy cập và Tooltip, icon trang trí đặt aria-hidden", True), ("aria", "Chỉ thêm luật aria-hidden và tên truy cập", False)]),
]

SPEC = dict(
    slug="icon", short="phần Icon",
    title="Foundations · Icon — đúng nghĩa và đúng cỡ chưa?",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
    lead=f"Trang này giúp bạn chốt thư viện, thang cỡ, nét, Featured icon, màu và bảng nghĩa. Kết luận chính: <b>nền đã đúng</b> (Lucide, khung 24, nét 2), việc cần làm là dọn. <mark>Lý do tách cỡ Web, App đã hết hạn sau DEC-322</mark>, 3 chỗ trùng nghĩa, bản tô lệch DEC-262, Featured đang dùng 3 cỡ mà chưa có token riêng. Trang này <mark>chưa sửa token nào</mark>.",
    kpis=[(str(COUNT["ok"]), "mục giống Untitled", "ok"), (str(COUNT["diff"]), "khác có lý do", ""), (str(COUNT["gap"]), "Untitled có, mình không có (đa số không cần lấy)", "bad"), (str(COUNT["own"]), "chỉ mình có", ""),
          (f"{len(ALL_ROWS)} / {UNIQUE}", "dòng nghĩa / icon trong bảng", ""), ("3", "chỗ trùng nghĩa", "bad"), ("13", "chỗ còn nét 1.8 trong bản tô", "bad")],
    tag_kind="icon",
    screens=dict(intro="Màn dựng bằng token thật, icon Lucide thật. Bật <b>Nhãn số đo</b> để đọc cỡ và nét của từng icon, số nét là số trên khung 24 (DEC-300). Trang không đề xuất đổi cỡ nên không có nút so bộ giá trị. Icon trên màn mẫu đã theo bảng nghĩa.",
                 logo_svg=None, gridov=False, overlay_html=None),
    sections=SECTIONS,
    items=ITEMS,
    final="Khi bạn chốt: mình cập nhật <code>design-system/tokens.json</code> → sinh <code>design-system/tokens.css</code> + handoff → sửa <code>design-system/foundations/icon.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>icon = approved</b> (<code>ds-foundation-status.py set icon approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). Trang này còn thêm: dọn các dòng ở bảng \"Chỗ tài liệu đang lệch nhau\", sửa <code>_scripts/ds-v2-handoff.py</code> nếu bỏ bản tô.",
    css=r"""
.szt{border-collapse:collapse;width:100%;font-size:11px}.szt th{font:500 10.5px/14px Inter,sans-serif;color:var(--color-text-tertiary);padding:3px 4px;text-align:center;vertical-align:bottom}.szt th small{display:block;font-weight:400;font-size:9.5px}
.szt td{padding:5px 4px;text-align:center;border-top:1px solid var(--color-border-secondary);vertical-align:middle;color:var(--color-fg-secondary)}.szt td:first-child{text-align:left;color:var(--color-text-primary)}.szt td .tp-ic{vertical-align:middle}
.szt.left th{text-align:left}.szt.left td{text-align:left}
.own{display:inline-block;font:500 9.5px/13px Inter,sans-serif;border:1px solid var(--color-border-primary);border-radius:var(--radius-xs);padding:0 3px;color:var(--color-text-tertiary);margin-left:2px;white-space:nowrap}
.mg{display:grid;grid-template-columns:repeat(auto-fill,minmax(148px,1fr));gap:var(--space-sm)}
.mi{display:grid;gap:2px;justify-items:start;padding:var(--space-md);border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);color:var(--color-fg-secondary);min-width:0}.mi .type-caption{color:var(--color-text-primary)}
.mi.dup{border-color:var(--color-fg-warning-primary);box-shadow:inset 0 0 0 1px var(--color-fg-warning-primary)}.rv .mi code{font-size:10.5px;background:none;padding:0;color:var(--color-text-tertiary);overflow-wrap:anywhere}
.pair{display:grid;grid-template-columns:48px 48px minmax(0,1fr);align-items:center;padding:4px 0;border-top:1px solid var(--color-border-secondary);color:var(--color-fg-secondary)}.pair.h{border-top:0}
.sw svg{stroke-width:2.25}.fillon svg{fill:currentColor}
.rowi{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) 0;min-width:0}
.ir{display:flex;flex-wrap:wrap;gap:var(--space-md);align-items:center}
.fi{display:inline-flex;align-items:center;justify-content:center;flex:none}.fic{display:grid;gap:var(--space-xs);justify-items:center;text-align:center;max-width:96px}
.pr{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-sm) 0;border-top:1px solid var(--color-border-secondary);flex-wrap:wrap}.pr code{margin-left:auto}.pr .vis{display:inline-flex}
.cat{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:var(--space-md)}.catc{border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);padding:var(--space-md);color:var(--color-fg-secondary)}.catc .type-label{color:var(--color-text-primary)}
.tp-ic-chip{--ic:var(--icon-size-chip)}
.src a,.cmp a{color:#0036B5}
""",
    js="",
)
