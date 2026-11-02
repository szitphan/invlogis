#!/usr/bin/env python3
"""SPEC trang review Foundations · Misc icons. Dựng: python3 _scripts/foundation_review/build.py misc

Phạm vi: icon đặc biệt ngoài Lucide, tài liệu ở design-system/foundations/icon-sets.md, mã misc-icon (DEC-331, DEC-332). Không gồm Phương tiện (trang vehicle) và Featured icon (DEC-329).
Số đếm nghiệp vụ tính lúc dựng từ docs/, không gõ tay. Số về bộ trên Figma đọc bằng figma_read ngày 02/11.
"""
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402

ROOT = kit.ROOT
sys.path.insert(0, str(ROOT / "design-system/components/_work/error-page"))
import illos  # noqa: E402

UR = ROOT / "design/_ref/untitled-ui/react/components"
ICONS = ROOT / "design-system/icons"
I = kit.icon


# ---------- đếm thật ----------
_DOCS = [p.read_text(errors="ignore") for p in (ROOT / "docs").rglob("*.md")]
_SPECS = [p.read_text(errors="ignore") for d in ("base", "application") for p in (ROOT / "design-system/components" / d).glob("*.md")]


def dn(rx):
    r = re.compile(rx)
    return sum(1 for x in _DOCS if r.search(x))


def sn(rx):
    r = re.compile(rx)
    return sum(1 for x in _SPECS if r.search(x))


N_PDF, N_XLS, N_IMG, N_DOC, N_CSV, N_ZIP, N_VID = (dn(x) for x in (r"\bPDF\b", r"\bXLSX?\b|Excel", r"\bJPE?G\b|\bPNG\b", r"\bDOCX?\b|\.docx?", r"\bCSV\b", r"\.zip|\bZIP\b", r"\bMP4\b|[Vv]ideo"))
N_QR, N_BAR, N_RATE, N_BANK, N_CARD, N_MISA, N_ZALO, N_SOCIAL, N_CONNECT = (dn(x) for x in (
    r"mã QR|[Qq]uét QR|QR tờ khai", r"mã vạch", r"đánh giá sao|chấm sao|xếp hạng sao", r"[Nn]gân hàng", r"thẻ tín dụng|credit card|Visa", r"MISA", r"Zalo", r"Facebook|LinkedIn|YouTube", r"màn (kết nối|tích hợp)|Kết nối / Tích hợp"))
S_FILE, S_BANK, S_APP, S_CHECK, S_PAY = (sn(x) for x in ("File type icon", "Bank logo", "App logo", "Check icon", "Payment method icon"))
N_PAY_SVG = len(list((ICONS / "payment").glob("*.svg")))
N_SOC_SVG = len(list((ICONS / "social").glob("*.svg")))
_fu = re.search(r"\| Icon loại tệp / ảnh nhỏ \|[^|]*icon `([^`]+)`", (ROOT / "design-system/components/application/field-upload.md").read_text())
FU_ICON_COLOR = _fu.group(1) if _fu else "màu xám"


_SETS = (ROOT / "design-system/foundations/icon-sets.md").read_text()
_SEC = {m.group(1).strip(): [x for x in m.group(2).splitlines() if x.strip()] for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", _SETS, flags=re.S | re.M)}
SET_NAMES = ("File type icon", "Check icon", "Payment method icon", "Flag", "Bank logo", "App logo")
THIN = [n for n in SET_NAMES if len(_SEC.get(n, [])) <= 1]


# ---------- đồ hoạ ----------
def asset(kind, name, w, h):
    p = ICONS / kind / f"{name}.svg"
    if not p.exists():
        return f'<span class="type-caption tp-sub">{name}</span>'
    s = re.sub(r"<\?xml[^>]*>", "", p.read_text())
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="ms{name}{m.group(1)}"', s)
    s = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#ms{name}{m.group(1)})", s)
    s = re.sub(r'href="#([^"]+)"', lambda m: f'href="#ms{name}{m.group(1)}"', s)
    s = re.sub(r'<svg([^>]*?)\swidth="[^"]*"', r"<svg\1", s, count=1)
    s = re.sub(r'<svg([^>]*?)\sheight="[^"]*"', r"<svg\1", s, count=1)
    return s.replace("<svg", f'<svg width="{w}" height="{h}" aria-hidden="true"', 1)


def store(export):
    """Huy hiệu thật lấy từ app-store-buttons.tsx của Untitled, đổi thuộc tính JSX sang SVG."""
    src = (UR / "base/buttons/app-store-buttons.tsx").read_text()
    i = src.index(f"export const {export}")
    m = re.search(r"<svg.*?</svg>", src[i:], flags=re.S)
    s = m.group(0)
    s = re.sub(r"\s(width|height)=\{[^}]*\}", "", s, count=2)
    s = re.sub(r"\s[a-zA-Z]+=\{[^}]*\}", "", s)
    for jsx, attr in (("colorInterpolationFilters", "color-interpolation-filters"), ("floodOpacity", "flood-opacity"), ("stopColor", "stop-color"), ("strokeMiterlimit", "stroke-miterlimit"),
                      ("strokeWidth", "stroke-width"), ("fillRule", "fill-rule"), ("clipRule", "clip-rule"), ("clipPath", "clip-path"), ("stopOpacity", "stop-opacity")):
        s = s.replace(f"{jsx}=", f"{attr}=")
    s = re.sub(r"\s+", " ", s)
    return f'<span class="ms-store">{s.replace("<svg", chr(60) + "svg height=" + chr(34) + "40" + chr(34), 1)}</span>'


TAG = {"PDF": "--red-700", "DOC": "--blue-700", "XLS": "--green-700", "CSV": "--green-700", "IMG": "--purple-700", "ZIP": "--neutral-700", "VID": "--orange-700"}


def fti(label="PDF", size=40, mode="color"):
    """File type icon dựng lại theo số Figma 6657:165918: tờ giấy gập góc, nhãn đuôi. Tờ giấy trỏ biến; nhãn theo mode."""
    fill = {"color": f"var({TAG.get(label, '--neutral-700')})", "gray": "var(--color-bg-secondary_solid)"}[mode]
    tag = "" if label == "Other" else (f'<rect class="ms-tag" x="1" y="15" width="24" height="12" rx="2" style="fill:{fill}"/>'
                                       f'<text x="13" y="23.6" text-anchor="middle" style="fill:var(--color-fg-white);font:600 8px Inter,sans-serif">{label}</text>')
    return (f'<svg class="ms-ft" width="{size}" height="{size}" viewBox="0 0 32 32" aria-hidden="true"><path d="M6 1h14l6 6v24H6z" stroke-width="1.5" style="fill:var(--color-bg-primary);stroke:var(--color-border-primary)"/>'
            f'<path d="M20 1v6h6" fill="none" stroke-width="1.5" style="stroke:var(--color-border-primary)"/>{tag}</svg>')


def row(name, meta, lead, st=""):
    return (f'<div class="ms-row">{lead}<div class="ms-rt"><div class="type-body ms-nm">{name}</div><div class="type-hint tp-sub">{meta}</div>{st}</div>'
            f'<span class="tp-fg2">{I("trash-2")}</span></div>')


VN = '<svg width="{0}" height="{0}" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="12" fill="#DA251D"/><path d="M12 5.2l1.6 4.9h5.1l-4.1 3 1.6 4.9-4.2-3-4.2 3 1.6-4.9-4.1-3h5.1z" fill="#FFCD00"/></svg>'
LA = '<svg width="{0}" height="{0}" viewBox="0 0 24 24" aria-hidden="true"><defs><clipPath id="mslac{0}"><circle cx="12" cy="12" r="12"/></clipPath></defs><g clip-path="url(#mslac{0})"><path fill="#CE1126" d="M0 0h24v24H0z"/><path fill="#002868" d="M0 6h24v12H0z"/><circle cx="12" cy="12" r="4.8" fill="#fff"/></g></svg>'
TH = '<svg width="{0}" height="{0}" viewBox="0 0 24 24" aria-hidden="true"><defs><clipPath id="msthc{0}"><circle cx="12" cy="12" r="12"/></clipPath></defs><g clip-path="url(#msthc{0})"><path fill="#A51931" d="M0 0h24v24H0z"/><path fill="#fff" d="M0 4h24v16H0z"/><path fill="#2D2A4A" d="M0 8h24v8H0z"/></g></svg>'


def qr(size=96):
    """Hình QR mẫu không đọc được, chỉ để xem cỡ và khung."""
    n = 21
    rnd = random.Random(7)
    cells = []
    fin = lambda x, y: x < 7 and y < 7 or x >= n - 7 and y < 7 or x < 7 and y >= n - 7
    for y in range(n):
        for x in range(n):
            if not fin(x, y) and rnd.random() > .52:
                cells.append(f"M{x} {y}h1v1h-1z")
    for ox, oy in ((0, 0), (n - 7, 0), (0, n - 7)):
        cells.append(f"M{ox} {oy}h7v7h-7zM{ox + 1} {oy + 1}v5h5v-5zM{ox + 2} {oy + 2}h3v3h-3z")
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {n} {n}" aria-hidden="true" style="fill:var(--neutral-950);fill-rule:evenodd"><path d="{"".join(cells)}"/></svg>'


def lab(x):
    return f'<div class="type-caption tp-sub ms-l">{x}</div>'


def fig(a, b=""):
    return f'<div class="ms-fic">{a}<span class="type-caption tp-sub">{b}</span></div>'


CSS = illos.CSS + """
.ms-l{margin:var(--space-md) 0 var(--space-xs)}.ms-l:first-of-type{margin-top:0}
.ms-ir{display:flex;flex-wrap:wrap;gap:var(--space-md);align-items:center}.ms-fic{display:grid;gap:var(--space-xs);justify-items:center;text-align:center;min-width:48px}
.ms-ir .tp-chip{gap:var(--space-xs)}.ms-ft{display:block;flex:none}.ms-store{display:inline-flex;border-radius:7px;background:var(--neutral-950);box-shadow:inset 0 0 0 1px var(--color-border-primary);overflow:hidden}.ms-store svg{display:block}
.ms-row{display:flex;align-items:center;gap:var(--space-lg);padding:var(--space-lg);border:1px solid var(--color-border-disabled);border-radius:var(--radius-card);background:var(--color-bg-primary);min-width:0}
.ms-row+.ms-row{margin-top:var(--space-md)}.ms-rt{flex:1;min-width:0}.ms-nm{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ms-thumb{width:var(--size-5xl);height:var(--size-5xl);border-radius:var(--radius-inner);background:var(--color-bg-quaternary);display:flex;align-items:center;justify-content:center;flex:none;color:var(--color-fg-tertiary);position:relative;overflow:hidden}
.ms-photo{width:96px;height:72px;border-radius:var(--radius-inner);background:var(--neutral-600);position:relative;display:flex;align-items:center;justify-content:center;color:var(--color-fg-white);overflow:hidden;flex:none}
.ms-photo::before{content:"";position:absolute;inset:40% 0 0;background:var(--neutral-800)}.ms-play{position:relative;width:var(--size-4xl);height:var(--size-4xl);border-radius:var(--radius-full,999px);background:var(--color-bg-overlay_solid);display:flex;align-items:center;justify-content:center}
.ms-play.un{width:80px;height:80px;background:var(--alpha-white-30);backdrop-filter:blur(var(--backdrop-blur-sm))}.ms-play.fillp svg{fill:currentColor}
.ms-dot{display:inline-block;width:var(--size-sm);height:var(--size-sm);border-radius:50%;flex:none}.ms-dotl{display:flex;align-items:center;gap:var(--space-sm)}
.ms-cam{position:relative;width:216px;height:216px;background:var(--neutral-800);border-radius:var(--radius-card);display:flex;align-items:center;justify-content:center;color:var(--color-fg-white);overflow:hidden}
.ms-cam i{position:absolute;width:var(--size-3xl);height:var(--size-3xl);border:0 solid var(--color-fg-white)}.ms-cam .a{top:32px;left:32px;border-width:2px 0 0 2px}.ms-cam .b{top:32px;right:32px;border-width:2px 2px 0 0}.ms-cam .c{bottom:32px;left:32px;border-width:0 0 2px 2px}.ms-cam .d{bottom:32px;right:32px;border-width:0 2px 2px 0}
.ms-qrw{display:inline-block;padding:var(--space-md);background:var(--white);border-radius:var(--radius-inner);line-height:0}
.ms-tile{width:var(--size-3xl);height:var(--size-3xl);border-radius:var(--radius-inner);border:1px solid var(--color-border-secondary);display:flex;align-items:center;justify-content:center;flex:none;font:600 7px Inter,sans-serif;color:var(--color-text-tertiary)}
.ms-empty{display:grid;justify-items:center;text-align:center;gap:var(--space-sm);padding:var(--space-2xl) var(--space-lg);position:relative;overflow:hidden;border-radius:var(--radius-card)}
.ms-empty>*{position:relative}.ms-fi{width:var(--size-5xl);height:var(--size-5xl);border-radius:var(--radius-inner);display:flex;align-items:center;justify-content:center;border:1px solid var(--color-border-primary);background:var(--color-bg-primary);color:var(--color-fg-tertiary)}
.ms-grid{position:absolute;inset:0;background-image:linear-gradient(var(--color-border-secondary) 1px,transparent 1px),linear-gradient(90deg,var(--color-border-secondary) 1px,transparent 1px);background-size:24px 24px;mask-image:radial-gradient(circle at 50% 35%,#000 0,transparent 70%);-webkit-mask-image:radial-gradient(circle at 50% 35%,#000 0,transparent 70%)}
.ms-map{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:var(--space-md)}.ms-map>div{border:1px solid var(--color-border-secondary);border-radius:var(--radius-inner);padding:var(--space-md);min-width:0}
.tp-f.tp-prop .ms-tag{fill:var(--color-bg-secondary_solid)!important}
"""


# ---------- màn mẫu: thêm khối Chứng từ vào màn chi tiết thật ----------
def _doc_card(head):
    rows = (row("Phieu-can-VGM-TCLU4829153.pdf", "412 KB · PDF", fti("PDF"))
            + row("Bang-ke-cuoc-thang-10.xlsx", "86 KB · Excel", fti("XLS"))
            + row("Anh-container-cong-B-niem-phong.jpg", "2,1 MB · Ảnh", f'<span class="ms-thumb">{I("image", "tp-ic-lg")}</span>'))
    return f'<div class="tp-card"><div class="{head}">Chứng từ của lệnh</div>{rows}</div>'


def overlay(body):
    body = body.replace('<div class="tp-card"><div class="type-title-3">Ghi chú điều vận', _doc_card("type-title-3") + '<div class="tp-card"><div class="type-title-3">Ghi chú điều vận', 1)
    return body.replace('<div class="tp-card"><div class="type-heading">Ghi chú điều vận', _doc_card("type-heading") + '<div class="tp-card"><div class="type-heading">Ghi chú điều vận', 1)


# ---------- bảng đối chiếu ----------
def st(k):
    return f'<span class="st-{k}">' + {"ok": "Giống", "diff": "Khác có lý do", "gap": "Mình thiếu", "own": "Chỉ mình có"}[k] + "</span>"


CMP = [
    ("Featured icon, Featured icon outline", "Figma", "<code>Featured icon</code> 6657:163375, 4 kiểu, 4 cỡ, đã chuyển sang trang Base", "ok", "Đã chốt ở DEC-329, không xét ở trang này."),
    ("File type icon", "Figma · <code>@untitledui/file-icons</code>", "<code>File type icon</code> 6657:165918, 7 loại × 2 cỡ", "diff", "Xem ms01–ms04. Gói Untitled không có trong repo nên chưa đếm được hết loại."),
    ("Payment method icon", "Figma · <code>foundations/payment-icons</code>", f"Hai bộ: 18 logo cũ <code>Payment method icon</code> và {N_PAY_SVG} SVG Untitled", "diff", "DEC-329 đã áp. Bộ Untitled thiếu NAPAS, VietQR. Xem ms12."),
    ("Social icon", "Figma · <code>foundations/social-icons</code>", f"{N_SOC_SVG} SVG, section <code>Master · Payment, Social</code>", "ok", "DEC-329 đã áp. Figma đơn sắc đen vì nguồn <code>currentColor</code>. Không có Zalo, xem ms14."),
    ("Country flag icons", "Figma · CDN <code>images/flags</code>", "<code>Flag</code> 6706:1532, 25 nước × 2 hình × 3 cỡ", "diff", "Mình chỉ lấy nước có giao thương. Xem ms06, ms07."),
    ("Integration icon", "Figma · <code>foundations/integration-icons</code>", "<code>App logo</code> 6709:1020, 15 app × 3 cỡ", "diff", "Thay công cụ AI bằng Zalo, Excel, Viettel Post. Xem ms14."),
    ("App icons", "Figma, ref chỉ ghi tên", "Chưa rõ tương ứng", "gap", "Ref <code>06-icons.md</code> mục 6 chỉ ghi tên, chưa kết luận được."),
    ("Check icon", "Figma", "<code>Check icon</code> 6657:166083, 6 kiểu × 3 cỡ", "ok", "Có đủ nhưng chưa component nào dùng. Xem ms15."),
    ("Check item text", "Figma", "Không có", "gap", "Dòng tick + chữ của bảng giá. Xem ms18."),
    ("Star icon", "Figma · <code>rating-stars.tsx</code>", "Lucide <code>star</code> có bản tô", "diff", "DEC-329 giữ Fill=On cho star."),
    ("Ratings badge", "Figma · <code>rating-badge.tsx</code>", "Không có", "gap", "Vòng nguyệt quế, chữ mẫu \"Best Design Tool\". Xem ms09."),
    ("_Dot", "Figma · <code>dot-icon.tsx</code> 8, 10", "Chấm 6 nằm trong <code>Badge</code>", "diff", "Xem ms10."),
    ("Folder icon", "Figma", "Lucide <code>folder</code>", "gap", "Xem ms18."),
    ("Emoji", "Figma", "Không có", "gap", "Xem ms18."),
    ("Cursor", "Figma", "Không có", "gap", "Đồ vẽ mockup. Xem ms18."),
    ("Play button", "<code>play-button-icon.tsx</code> 80", "Lucide <code>play</code> mang nghĩa Bắt đầu", "gap", "Xem ms11."),
    ("QR code, khung quét", "<code>shared-assets/qr-code.tsx</code> 96, 128", "Lucide <code>qr-code</code>, <code>barcode</code>, <code>scan-line</code>", "gap", "Xem ms08."),
    ("App store buttons", "<code>base/buttons/app-store-buttons.tsx</code> 4 cửa hàng", "Không có", "gap", "Xem ms05."),
    ("Background patterns", "<code>shared-assets/background-patterns</code> 4 mẫu", "Không có", "gap", "Xem ms16."),
    ("Illustrations", "<code>shared-assets/illustrations</code> 4 hình", "<code>illos.py</code> của Error Page, đang brainstorm", "diff", "Xem ms17."),
    ("iPhone mockup, Credit card, Section divider", "<code>shared-assets</code>", "Không có", "gap", "Đồ marketing. Xem ms18."),
    ("—", "Không có", "<code>Bank logo</code> 6704:101952, 69 ngân hàng × 3 cỡ", "own", "Danh sách VietQR, xem ms13."),
    ("—", "Không có", "Phương tiện, <code>design-system/foundations/vehicle.md</code>", "own", "Mã <code>vehicle</code> theo DEC-331. Việc đổi tên file xét ở trang <code>vehicle</code> mục vh00."),
]
COUNT = {k: sum(1 for r in CMP if r[3] == k) for k in ("ok", "diff", "gap", "own")}
CMP_HTML = kit.rows(["Untitled", "Nguồn", "Mình", "Trạng thái", "Ghi chú"], [[a, b, c, st(k), d] for a, b, c, k, d in CMP])


FIGMA_ROWS = [
    ["<code>File type icon</code>", "6657:165918", "7 loại × SM 32, MD 40", f"n:{S_FILE}", "Chỉ <code>design-system/components/application/field-upload.md</code>"],
    ["<code>Check icon</code>", "6657:166083", "Gray, Success, Mono × Light, Dark × 3 cỡ", f"n:{S_CHECK}", "Không"],
    ["<code>Payment method icon</code>", "6708:100826", "18 logo × 34×24, 46×32", f"n:{S_PAY}", "<code>_Card brand</code> trong <code>Payment input</code> (mô tả trên Figma)"],
    ["Payment, Social Untitled", "7145:113000", f"{N_PAY_SVG} + {N_SOC_SVG} SVG", "n:0", "Đã áp theo DEC-329; Social đơn sắc đen vì nguồn <code>currentColor</code>"],
    ["<code>Flag</code>", "6706:1532", "25 nước × 2 hình × 3 cỡ = 150", "n:0", "Tag Flag trong trang duyệt Tag"],
    ["<code>Bank logo</code>", "6704:101952", "69 ngân hàng × 24, 32, 40", f"n:{S_BANK}", "Không"],
    ["<code>App logo</code>", "6709:1020", "15 app, 5 ô chưa có nguồn × 24, 32, 40", f"n:{S_APP}", "Không"],
]


GAP_ROWS = [
    ["File type icon", "Một câu", "7 loại, 2 cỡ, màu nhãn, khi nào hiện ảnh nhỏ (ms01–ms04)"],
    ["Check icon", "Một câu", "Biến thể, chỗ dùng; có thể bỏ theo ms15"],
    ["Payment method icon", "Số logo, cỡ, nguồn", "Quan hệ với bộ Untitled, <code>_Card brand</code> (ms12)"],
    ["Flag", "Một câu", "25 nước, hình, cỡ; câu đang ghi \"mã điện thoại, ngôn ngữ\" chờ ms06"],
    ["Bank logo", "Một câu", "3 cỡ, BIN trong mô tả, tầng dữ liệu (ms13)"],
    ["App logo", "Một câu", "15 app, 5 ô trống; màn Kết nối chưa có trong tài liệu (ms14)"],
    ["Payment, Social", "Nguồn, khung, giấy phép", "Màu Social ở Tối; câu \"Napas thêm riêng ở logo.md\" lệch vì bộ cũ đã có NAPAS (ms12, ms14)"],
]


# ---------- xem thử ----------
def pv_style(mode, platform):
    return (lab("Tờ giấy + nhãn đuôi (đang có trên Figma)") + f'<div class="ms-ir">{fti("PDF")}{fti("XLS")}{fti("DOC")}</div>'
            + lab("Icon Lucide một nét") + f'<div class="ms-ir"><span class="tp-fg2">{I("file-text", "tp-ic-lg")}</span><span class="tp-fg2">{I("file-spreadsheet", "tp-ic-lg")}</span><span class="tp-fg2">{I("file", "tp-ic-lg")}</span></div>'
            + lab("Trong dòng tệp") + row("Phieu-can-VGM-TCLU4829153.pdf", "412 KB · PDF", fti("PDF")))


def pv_color(mode, platform):
    a = "".join(fti(x, 40, "color") for x in ("PDF", "DOC", "XLS", "IMG", "ZIP"))
    b = "".join(fti(x, 40, "gray") for x in ("PDF", "DOC", "XLS", "IMG", "ZIP"))
    err = '<div class="type-hint tp-err">Tải lên không thành công</div>'
    return (lab("Một màu xám") + f'<div class="ms-ir">{b}</div>' + row("Bien-ban-giao-hang-LVT-0412.pdf", "412 KB · PDF", fti("PDF", 40, "gray"), err)
            + lab("Năm màu như Figma: đỏ PDF cạnh dòng lỗi đỏ") + f'<div class="ms-ir">{a}</div>' + row("Bien-ban-giao-hang-LVT-0412.pdf", "412 KB · PDF", fti("PDF"), err)
            + lab(f'Chữ trắng trên nhãn xám {kit.cr("color/fg/white", "color/bg/secondary_solid")}'))


def pv_set(mode, platform):
    keep = "".join(fig(fti(x), x) for x in ("PDF", "DOC", "XLS", "IMG", "VID", "Other"))
    drop = "".join(fig(fti(x), x) for x in ("CSV", "ZIP"))
    return lab("Giữ, thêm VID") + f'<div class="ms-ir">{keep}</div>' + lab("Bỏ") + f'<div class="ms-ir">{drop}</div>'


def pv_size(mode, platform):
    t = '<span class="ms-thumb">' + I("image", "tp-ic-lg") + "</span>"
    return (lab("Cỡ 32 trong bảng chứng từ, cỡ 40 trong dòng tải tệp") + f'<div class="ms-ir">{fig(fti("PDF", 32), "32")}{fig(fti("PDF", 40), "40")}</div>'
            + row("Anh-container-cong-B.jpg", "2,1 MB · Ảnh", t) + lab("Thanh dưới rộng đúng <code>control/height/lg</code> của nền tảng này")
            + f'<div style="width:var(--control-height-lg);height:4px;background:var(--color-fg-tertiary)"></div>')


def pv_store(mode, platform):
    return (lab("Bước 1 của email kích hoạt, mỗi khách một đường dẫn") + f'<div class="ms-ir">{store("AppStoreButton")}{store("GooglePlayButton")}</div>'
            + lab("Thay bằng chữ") + '<div class="type-body"><u>Tải trên App Store</u> · <u>Tải trên Google Play</u></div>')


def pv_lang(mode, platform):
    r = lambda lead, a, b: f'<div class="ms-row" style="border:0;padding:var(--space-md) 0">{lead}<span class="type-body" style="flex:1">{a}</span><span class="type-body tp-sub">{b}</span><span class="tp-fg2">{I("chevron-right")}</span></div>'
    return (lab("Hàng Ngôn ngữ: chỉ chữ") + r(I("languages"), "Ngôn ngữ", "Tiếng Việt")
            + lab("Cờ đúng chỗ: tuyến qua nước khác") + f'<div class="ms-ir"><span class="tp-chip">{VN.format(16)}<span class="type-caption">Việt Nam</span></span><span class="tp-chip">{LA.format(16)}<span class="type-caption">Lào</span></span><span class="tp-chip">{TH.format(16)}<span class="type-caption">Thái Lan</span></span></div>'
            + lab("Số điện thoại: chỉ Việt Nam, không cần chọn mã vùng") + '<div class="tp-inp"><span class="type-body tp-num">0903 482 915</span></div>'
            + lab("Cờ vẽ lại để xem thử, bản thật ở Figma 6706:1532"))


def pv_flag(mode, platform):
    sz = lambda s: "".join(f'{f.format(s)}' for f in (VN, LA, TH))
    rect = '<svg width="24" height="16" viewBox="0 0 24 16" aria-hidden="true"><rect width="24" height="16" rx="2" fill="#DA251D"/><path d="M12 3.2l1.2 3.6h3.8l-3.1 2.2 1.2 3.6-3.1-2.2-3.1 2.2 1.2-3.6L7 6.8h3.8z" fill="#FFCD00"/></svg>'
    return lab("Tròn 16, 20, 24") + f'<div class="ms-ir">{sz(16)}</div><div class="ms-ir" style="margin-top:var(--space-sm)">{sz(20)}</div><div class="ms-ir" style="margin-top:var(--space-sm)">{sz(24)}</div>' + lab("Chữ nhật 3:2") + rect


def pv_scan(mode, platform):
    cam = f'<div class="ms-cam"><i class="a"></i><i class="b"></i><i class="c"></i><i class="d"></i><span class="type-caption" style="position:absolute;bottom:8px">Đưa mã QR vào khung</span></div>'
    return (lab("Khung ngắm trên màn quét") + cam + lab("Icon Lucide đã đủ") + f'<div class="ms-ir">{fig(I("scan-line", "tp-ic-lg"), "Quét mã")}{fig(I("qr-code", "tp-ic-lg"), "Mã QR")}{fig(I("barcode", "tp-ic-lg"), "Mã vạch")}</div>'
            + lab("Hiện mã QR, hình mẫu không đọc được") + f'<span class="ms-qrw">{qr(96)}</span>')


def pv_rate(mode, platform):
    stars = "".join(f'<span style="color:var(--color-fg-warning-primary)" class="ms-sf">{I("star", "tp-ic-md")}</span>' for _ in range(4)) + f'<span class="tp-fg2">{I("star", "tp-ic-md")}</span>'
    return lab("Một dòng đánh giá nếu có ngày cần") + f'<div class="ms-ir"><span style="display:flex;gap:2px">{stars}</span><span class="type-caption tp-sub">4,0</span></div>' + lab("Đang dùng: <code>star</code> nghĩa Yêu thích") + f'<span class="tp-fg2">{I("star", "tp-ic-lg")}</span>'


def pv_dot(mode, platform):
    d = lambda t, c: f'<div class="ms-dotl"><span class="ms-dot" style="background:var(--color-{t})"></span><span class="type-caption">{c}</span></div>'
    return lab("Chấm 6, một phần dùng chung") + f'<div class="ms-ir">{d("fg-success-primary", "Hoàn thành")}{d("fg-info-primary", "Đang chạy")}{d("fg-warning-primary", "Chờ duyệt")}{d("fg-error-primary", "Quá hạn")}</div>' + lab("Trong Badge kiểu Dot, dòng thời gian") + '<div class="ms-dotl"><span class="ms-dot" style="background:var(--color-fg-info-primary)"></span><span class="type-body">Lái xe đã nhận lệnh · 14:30</span></div>'


def pv_play(mode, platform):
    a = f'<span class="ms-photo"><span class="ms-play">{I("play", "tp-ic-md")}</span></span>'
    b = f'<span class="ms-photo"><span class="ms-play fillp">{I("play", "tp-ic-md")}</span></span>'
    return (lab("Ảnh nhỏ video bằng chứng: nét, nền <code>color/bg/overlay_solid</code>") + f'<div class="ms-ir">{fig(a, "Nét")}{fig(b, "Tô")}</div>'
            + lab("Dòng tệp") + row("Video-cat-chi-TCLU4829153.mp4", "48 MB · Video", fti("VID")))


def pv_pay(mode, platform):
    a = "".join(fig(asset("payment", n, 34, 24), n) for n in ("visa", "mastercard", "jcb", "amex"))
    vn = "".join(fig(f'<span class="ms-tile" style="width:34px;height:24px">{x}</span>', x) for x in ("NAPAS", "VietQR"))
    return lab("Từ bộ Untitled, 34×24") + f'<div class="ms-ir">{a}</div>' + lab("Hai logo Việt Nam chỉ có ở bộ cũ, ô giữ chỗ") + f'<div class="ms-ir">{vn}</div>'


def pv_bank(mode, platform):
    r = lambda t, b, n: f'<div class="ms-row" style="padding:var(--space-md)"><span class="ms-tile">{t}</span><div class="ms-rt"><div class="type-body ms-nm">{n}</div><div class="type-hint tp-sub">BIN {b}</div></div></div>'
    return (lab("Ô chọn ngân hàng nhận trên form nhà cung cấp, lệnh chi") + r("VCB", "970436", "Ngân hàng TMCP Ngoại thương Việt Nam") + r("BIDV", "970418", "Ngân hàng TMCP Đầu tư và Phát triển Việt Nam")
            + lab("Ô chữ giữ chỗ logo, bản thật ở Figma 6704:101952. Số BIN ở đây là mẫu từ trí nhớ, chưa đối chiếu Figma"))


def pv_app(mode, platform):
    has = ("Zalo", "Google Maps", "Gmail", "Outlook", "Teams", "Excel", "Sheets", "Drive", "Slack", "Viettel Post")
    no = ("MISA", "VNPay", "MoMo", "ZaloPay", "GHN")
    return (lab(f"{len(has)} app có file") + '<div class="ms-ir">' + "".join(f'<span class="tp-chip"><span class="type-caption">{x}</span></span>' for x in has) + "</div>"
            + lab(f"{len(no)} ô trống, chưa có nguồn") + '<div class="ms-ir">' + "".join(f'<span class="tp-chip tp-y"><span class="type-caption">{x}</span></span>' for x in no) + "</div>"
            + lab("Social: đen như Figma") + '<div class="ms-ir" style="color:var(--neutral-950)">' + "".join(asset("social", n, 24, 24) for n in ("facebook", "linkedin", "youtube")) + "</div>"
            + lab("Social: gắn <code>color/fg/primary</code> khi đặt") + '<div class="ms-ir" style="color:var(--color-fg-primary)">' + "".join(asset("social", n, 24, 24) for n in ("facebook", "linkedin", "youtube")) + "</div>")


def pv_check(mode, platform):
    a = lambda ic, tok, x: f'<div class="ms-dotl"><span style="color:var(--color-{tok})">{I(ic, "tp-ic-md")}</span><span class="type-body">{x}</span></div>'
    return lab("Dùng Lucide, không cần bộ riêng") + a("circle-check", "fg-success-primary", "Đủ ảnh niêm phong") + a("circle-check", "fg-success-primary", "Đã có phiếu cân") + a("circle", "fg-tertiary", "Chưa có EIR")


def pv_pattern(mode, platform):
    box = lambda g: (f'<div class="ms-empty">{g}<span class="ms-fi">{I("search-x", "tp-ic-lg")}</span>'
                     '<span class="type-title-3">Không tìm thấy trang</span><span class="type-body tp-sub">Đường dẫn đã đổi hoặc lệnh đã bị xoá.</span></div>')
    return lab("Lưới mờ cho trang lỗi cả màn") + box('<span class="ms-grid"></span>') + lab("Nền phẳng cho thẻ, danh sách") + box("")


def pv_illo(mode, platform):
    em = (f'<div class="ms-empty"><span class="ms-fi">{I("clipboard-list", "tp-ic-lg")}</span><span class="type-title-3">Chưa có lệnh nào</span>'
          '<span class="type-body tp-sub">Lệnh được giao sẽ hiện ở đây.</span></div>')
    il = (f'<div class="ms-empty">{illos.idle_truck()}<span class="type-title-3">Chưa có lệnh nào</span><span class="type-body tp-sub">Lệnh được giao sẽ hiện ở đây.</span></div>')
    return lab("Featured icon + chữ") + em + lab("Hình từ <code>illos.py</code>") + il


def pv_rest(mode, platform):
    return lab("Nếu cần thư mục hồ sơ, Lucide đã có") + f'<div class="ms-ir">{fig(I("folder", "tp-ic-lg"), "folder")}{fig(I("check", "tp-ic-lg"), "check")}</div>'


def pv_map(mode, platform):
    g = lambda t, x: f'<div><div class="type-label">{t}</div><div class="type-caption tp-sub">{x}</div></div>'
    m = ('<div class="ms-map">' + g("icon-sets.md · mã misc-icon", "Featured icon, File type, Check, Payment, Flag, Bank, App, Social") + g("vehicle.md · mã vehicle", "Ảnh xe, sơ đồ lốp, marker") + g("icon.md · mã icon", "Lucide, bảng nghĩa, luật dùng") + g("logo.md · mã logo", "Logo sản phẩm, logo khách") + "</div>")
    return m + lab("Mức ghi của từng bộ trong icon-sets.md") + kit.rows(["Bộ", "Đang ghi", "Còn thiếu"], GAP_ROWS)


# ---------- mục chọn ----------
ITEMS = [
    dict(id="ms00", grp="Cấu trúc", title="icon-sets.md đã đủ các bộ chưa, phần nào còn thiếu?",
         why=f"DEC-331 đã thêm mã <code>misc-icon</code>, DEC-332 đã tách tài liệu sang <code>design-system/foundations/icon-sets.md</code>, và <code>_scripts/ds-deps.py</code> đã dò stale theo mã này. Khung đã xong. Việc còn lại là nội dung: Featured icon có bảng đủ, còn <mark>{len(THIN)}/{len(SET_NAMES)} bộ phía sau chỉ ghi một câu</mark> ({', '.join(THIN)}). Người vẽ màn đọc tài liệu chưa biết bộ có mấy loại, mấy cỡ, dùng khi nào; những điều đó hiện chỉ nằm trong mô tả component trên Figma.",
         untitled="Một trang Figma <code>Misc icons</code>, nguồn <code>06-icons.md</code> mục 6. Ref chỉ ghi cấu trúc, không có luật dùng từng bộ.",
         ours="<code>design-system/foundations/icon-sets.md</code>, mã <code>misc-icon</code>, trạng thái đọc ở <code>design-system/foundations/README.md</code>. Trang Figma <code>Misc icons</code> 6702:122238.",
         astryx="<code>design/design.md</code> không tách foundation riêng cho nhóm này.",
         note="Tài liệu Phương tiện đã đổi tên thành <code>design-system/foundations/vehicle.md</code> (<code>DEC-334</code>, trang <code>vehicle</code> mục vh00), không xét ở đây. Mục này phụ thuộc ms01–ms15: nội dung ghi theo lựa chọn ở các mục đó.",
         pv=kit.panes(pv_map, modes=("light",)),
         opts=[("fill", "Bổ sung đủ 7 bộ theo bảng trên: loại, cỡ, màu, khi nào dùng, ghi theo lựa chọn ms01–ms15", True),
               ("brief", "Giữ mỗi bộ một câu, chi tiết để trong mô tả component trên Figma", False)]),

    dict(id="ms01", grp="File type icon", title="File type icon vẽ kiểu nào?",
         why=f"Mỗi dòng tệp cần nói rõ đuôi tệp. Tài liệu nghiệp vụ nhắc <mark>PDF ở {N_PDF} file</mark>, Excel ở {N_XLS} file. Bản tờ giấy + nhãn đuôi đã có trên Figma và đọc ra chữ ở cả hai cỡ. Icon Lucide <code>file-text</code>, <code>file-spreadsheet</code> nhẹ hơn nhưng phải đọc hình mới đoán được loại, ngoài trời khó hơn.",
         untitled="<code>FileIcon</code> của <code>@untitledui/file-icons</code>, có <code>variant</code> <code>default</code>, <code>solid</code> và <code>theme</code> <code>light</code>, <code>dark</code>; <code>size-10</code> tức 40. Gói không có trong repo, chưa đếm hết kiểu.",
         ours="<code>File type icon</code> 6657:165918 trên Figma, mô tả \"theo Untitled FileIcon\". <code>design-system/foundations/icon-sets.md</code> ghi một câu về hình dạng.",
         astryx="<code>design/design.md</code> không có bộ loại tệp.",
         pv=kit.panes(pv_style, platforms=("web", "mobile")),
         opts=[("sheet", "Giữ tờ giấy + nhãn đuôi đang có trên Figma, không vẽ lại", True), ("lucide", "Đổi sang icon Lucide một nét, xoá bộ File type icon", False)]),

    dict(id="ms02", grp="File type icon", title="Nhãn đuôi tệp mang màu không?",
         why=f"Nhãn trên Figma tô <mark>5 mã màu trần</mark> và không đổi theo chế độ: PDF đỏ, DOC xanh, XLS và CSV xanh lá, IMG tím, ZIP xám. Spec <code>design-system/components/application/field-upload.md</code> lại ghi icon màu <code>{FU_ICON_COLOR}</code>, hai nơi đang lệch. Ảnh đã hiện ảnh nhỏ nên phần lớn dòng tệp là PDF: <mark>đỏ gần như mọi dòng</mark>, đứng cạnh chữ lỗi cũng đỏ. Màu loại tệp không mang nghĩa nghiệp vụ, chữ trên nhãn đã đủ phân biệt. Thang <code>color/utility/red-700</code> đảo sang màu sáng ở Tối nên chữ trắng trên nhãn sẽ hỏng nếu trỏ thẳng; <code>color/bg/secondary_solid</code> với chữ <code>color/fg/white</code> không đảo nên giữ tương phản ở cả hai chế độ, tỉ lệ đo ngay trong xem thử.",
         untitled="<code>theme</code> <code>light</code>, <code>dark</code> của <code>FileIcon</code> vẽ hai bản (<code>file-upload-base.tsx</code>). Bản <code>default</code> tô màu theo loại.",
         ours="<code>File type icon</code> trên Figma: tờ giấy đã gắn biến, nền nhãn là mã trần. <code>design-system/components/application/field-upload.md</code> ghi màu xám.",
         astryx="Luật \"không truyền nghĩa chỉ bằng màu\" ở <code>design/design.md</code>, không nói riêng về tệp.",
         note="Bấm <b>Bộ giá trị</b> ở màn mẫu đầu trang để so hai cách trên màn chi tiết lệnh. Đây là đổi hình đã vẽ trên Figma nên mình hỏi trước, không tự áp.",
         pv=kit.panes(pv_color, platforms=("web", "mobile")),
         opts=[("gray", "Một màu: nhãn color/bg/secondary_solid, chữ color/fg/white, sửa nền nhãn các biến thể trên Figma", True),
               ("color", "Giữ 5 màu nhận diện loại tệp, tách thành biến riêng không đảo theo chế độ, sửa spec Field Upload theo", False)]),

    dict(id="ms03", grp="File type icon", title="Bộ loại tệp gồm những gì?",
         why=f"Đếm trong <code>docs/</code>: <mark>PDF {N_PDF} file</mark>, Excel {N_XLS}, JPG/PNG {N_IMG}, DOC {N_DOC}, <mark>CSV {N_CSV}, ZIP {N_ZIP}</mark>. SRS cũ cho phép \"JPG, PNG, PDF\" (<code>docs/_reverse/business-partners/business-partners-reverse-spec.md</code>, NFR-business-partners-003). Video mới xuất hiện ở SOP, chưa vào <code>docs/</code> ({N_VID} file): \"nhân viên hiện trường sẽ quay video cắt chì\" (<code>docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md</code>). Đây là thiết kế to-be của khách, nên bộ cần sẵn VID.",
         untitled="<code>FileIcon type</code> theo đuôi file, kèm <code>empty</code> khi không rõ loại. Ref: \"nhiều biến thể theo đuôi file (pdf, doc, img…) — chưa đếm\".",
         ours="<code>File type icon</code>: PDF, DOC, XLS, CSV, IMG, ZIP, Other.",
         astryx="Không có.",
         note="Khách cho phép định dạng nào là cấu hình theo khách, chưa có mã P trong <code>docs/_product/tenant-parameters.md</code>. Định dạng ngoài bộ dùng Other, không vẽ thêm. Mục ms11 phụ thuộc VID ở đây.",
         pv=kit.panes(pv_set),
         opts=[("trim", "Còn PDF, DOC, XLS, IMG, VID, Other: thêm VID, bỏ CSV và ZIP vì chưa tài liệu nào cần", True),
               ("add", "Giữ cả 7 loại, thêm VID thành 8", False), ("keep", "Giữ nguyên 7 loại, chưa thêm video", False)]),

    dict(id="ms04", grp="File type icon", title="Cỡ File type icon có đổi theo nền tảng?",
         why="Figma vẽ hai cỡ cố định <mark>32 và 40</mark>. Spec Field Upload lại ghi khung <code>control/height/lg</code>, biến này là <mark>40 ở Web nhưng 52 ở App</mark>, nên trên app icon loại tệp sẽ to hơn số vẽ. Đây là đồ hoạ, không phải vùng chạm, nên không cần lớn theo ngón tay. Hai bậc <code>size/4xl</code> và <code>size/5xl</code> có đúng 32 và 40 ở mọi chế độ, cùng hướng gộp một bộ của DEC-329.",
         untitled="<code>size-10</code> tức 40 ở mọi nơi dùng (<code>file-upload-base.tsx</code>, <code>empty-state.tsx</code>).",
         ours="<code>File type icon</code> SM 32, MD 40; <code>control/height/lg</code> trong <code>design-system/components/application/field-upload.md</code>.",
         astryx="Không có.",
         pv=kit.panes(pv_size, platforms=("web", "mobile")),
         opts=[("one", "Một bộ cho web và app: size/4xl 32, size/5xl 40, sửa dòng trong spec Field Upload, không thêm token", True),
               ("ctrl", "Giữ theo control/height/lg, trên app thành 52, vẽ thêm một cỡ", False)]),

    dict(id="ms05", grp="Cửa hàng ứng dụng", title="Có cần huy hiệu App Store, Google Play?",
         why="Không có màn sản phẩm nào đặt huy hiệu. Chỗ cần thật là <mark>bước 1 của email kích hoạt tài khoản</mark>: SRS cũ ghi \"Bước 1 — Tải ứng dụng Delta Partner\" kèm \"[Link tải trên App Store]\" (<code>docs-input/srs-cu/lg-srs-export.md</code>). DEC-326 chốt <mark>mỗi khách một bản app trên store</mark>, nên đường dẫn đi theo khách. Hình huy hiệu là tài sản của Apple và Google, nên lấy nguyên bản, không vẽ lại (luật thương hiệu lấy từ trí nhớ, chưa kiểm).",
         untitled="<code>base/buttons/app-store-buttons.tsx</code> gồm Google Play, App Store, Galaxy Store, AppGallery, cỡ md 135×40, lg 149×44, viền <code>app-store-badge-border</code>.",
         ours="Không có. <code>docs/_product/tenant-parameters.md</code> có <code>P-icon-app</code> nhưng chưa có mã đường dẫn tải.",
         astryx="Không có.",
         note="Nếu chọn thêm: cần dòng mới <code>P-link-tai-app</code> trong bảng tham số, kiểu Tệp liên kết theo khách, mặc định chưa chốt. Ảnh trong xem thử lấy từ code Untitled.",
         pv=kit.panes(pv_store, modes=("light", "dark")),
         opts=[("two", "Thêm 2 huy hiệu App Store, Google Play cỡ 40, chỉ cho email kích hoạt và trang đăng nhập khi mở trên điện thoại", True),
               ("text", "Không dùng huy hiệu, email ghi link bằng chữ", False)]),

    dict(id="ms06", grp="Cờ quốc gia", title="Cờ dùng ở đâu?",
         why="Figma ghi \"Cờ cho chọn quốc gia, mã điện thoại, ngôn ngữ\". Soi từng chỗ thì chỉ một chỗ cần. <mark>Ngôn ngữ</mark>: <code>P-ngon-ngu-giao-dien</code> chỉ có Tiếng Việt, Tiếng Anh, và cờ Anh hay Mỹ đều không phải \"tiếng Anh\"; hàng này trong <code>design-system/components/application/header-navigation.md</code> vốn ghi chữ. <mark>Mã vùng</mark>: quy tắc chung ghi \"Đầu số <code>0</code> hoặc <code>84</code>\" (<code>docs-input/ui-common/web/web-common-rules.md</code>), không có số nước ngoài. <mark>Quốc gia</mark>: gói CBT (<code>docs/_product/saas-core-vs-tenant.md</code>) và Tag \"nước đi qua\" là chỗ cờ có nghĩa thật.",
         untitled="<code>Badge</code> nhận <code>flag</code> theo mã nước, tải SVG tròn từ CDN <code>images/flags</code> (<code>base/badges/badges.tsx</code>), có <code>tags.demo.tsx</code>.",
         ours="<code>Flag</code> 6706:1532; <code>design-system/foundations/icon-sets.md</code> đang ghi đúng câu trên Figma. Trang duyệt <code>design-system/components/_work/tag/page.json</code> có \"Flag (nước đi qua)\".",
         astryx="Không có cờ trong <code>design/design.md</code>.",
         pv=kit.panes(pv_lang, platforms=("web", "mobile")),
         opts=[("country", "Cờ chỉ cho quốc gia (tuyến qua nước khác, Tag). Ngôn ngữ ghi chữ, không có bộ chọn mã vùng", True),
               ("lang", "Thêm cờ vào hàng Ngôn ngữ như Figma đang ghi", False)]),

    dict(id="ms07", grp="Cờ quốc gia", title="Giữ mấy biến thể cờ?",
         why="<code>Flag</code> có 25 nước × 2 hình × 3 cỡ = <mark>150 biến thể</mark>. Untitled chỉ dùng hình tròn trong component. Tag cần cỡ nhỏ; chưa spec nào cần chữ nhật. Giữ tròn còn 75, mở thư viện nhẹ hơn. Danh sách 25 nước đã phủ đối tác châu Á, Âu, Mỹ, chưa có bằng chứng phải thêm.",
         untitled="<code>badges.tsx</code>: \"circular SVG\". Figma trang <code>Country flag icons</code>, ref chưa đếm.",
         ours="<code>Flag</code>: Country × Shape (Circle, Rectangle 3:2) × Size (SM 16, MD 20, LG 24).",
         astryx="Không có.",
         pv=kit.panes(pv_flag),
         opts=[("circle", "Giữ 25 nước, chỉ hình tròn, 3 cỡ 16, 20, 24: còn 75 biến thể", True), ("all", "Giữ nguyên 150 biến thể", False)]),

    dict(id="ms08", grp="Quét mã", title="QR, mã vạch cần đồ hoạ riêng không?",
         why=f"Nghiệp vụ là <mark>quét vào</mark>, không phải hiện mã ra: quét QR tờ khai (<code>docs/shipment-coordination/brainstorms/shipment-coordination.md</code> A2), chụp QR trả hộ (<code>docs/payment-on-behalf/brainstorms/payment-on-behalf.md</code>). QR ở {N_QR} file, mã vạch ở {N_BAR} file. <mark>Số container không đi bằng mã vạch</mark>: tài liệu chọn cách AI đọc chữ rồi kiểm theo ISO 6346 (<code>docs/_research/2026-10-02-field-document-reading.md</code>), nên màn đó là camera chụp. Hiện mã QR chỉ thấy là lớp thêm khi khách xác nhận, trong <code>docs/_research/2026-10-02-electronic-delivery-record.md</code>, chưa vào phạm vi.",
         untitled="<code>shared-assets/qr-code.tsx</code>: sinh QR bằng <code>qr-code-styling</code>, cỡ 96 và 128, có 4 góc khung và dải quét <code>GradientScan</code>.",
         ours="<code>design-system/foundations/icon.md</code>: Quét mã <code>scan-line</code>, Mã QR <code>qr-code</code>, Mã vạch <code>barcode</code>. Chưa có khung ngắm.",
         astryx="Nút Quét tròn 56, icon <code>scan-qr-code</code>, nhãn truy cập \"Quét mã QR\" (<code>design/design.md</code>). Bảng nghĩa của mình đã chốt <code>scan-line</code> theo DEC-329, không mở lại.",
         note="Khung ngắm là phần của màn quét, dựng cùng màn đó, không thành token. Ảnh tờ khai và ảnh container đi qua File type IMG hoặc ảnh nhỏ.",
         pv=kit.panes(pv_scan, platforms=("mobile",), modes=("light", "dark")),
         opts=[("frame", "Không thêm bộ QR. Dùng 3 icon Lucide, thêm 4 góc ngắm khi vẽ màn quét trên app", True),
               ("qrgen", "Thêm component hiện mã QR cỡ 96, 128 theo Untitled cho biên bản giao nhận", False)]),

    dict(id="ms09", grp="Đánh giá", title="Có cần Rating?",
         why=f"Đếm trong <code>docs/</code>: chấm sao <mark>{N_RATE} file</mark>. Sản phẩm không có màn cho khách chấm lái xe hay nhà cung cấp. <code>RatingBadge</code> của Untitled là đồ trang chủ (vòng nguyệt quế, chữ mẫu \"Best Design Tool\", \"2,000+ reviews\"). Sao đã có nghĩa <b>Yêu thích</b> trong bảng nghĩa theo DEC-329, thêm nghĩa chấm điểm sẽ lẫn.",
         untitled="<code>foundations/rating-stars.tsx</code>, <code>foundations/rating-badge.tsx</code>. Trong <code>react/components</code> không component ứng dụng nào dùng.",
         ours="Lucide <code>star</code> có bản tô, nghĩa Yêu thích.",
         astryx="Không có.",
         pv=kit.panes(pv_rate),
         opts=[("no", "Không thêm. Khi nào có màn đánh giá thì mở lại ở component đó", True), ("stars", "Thêm RatingStars sẵn 5 sao, chưa có màn dùng", False)]),

    dict(id="ms10", grp="Chấm", title="Chấm trạng thái có thành phần riêng không?",
         why="Chấm xuất hiện ở <code>Badge</code> (<code>size/sm</code> 6, DEC-310), <code>_Avatar status</code>, Tag, marker bản đồ. Spec chưa ghi phần dùng chung nào, nên đổi cỡ sau này phải sửa từng nơi (chưa mở từng component trên Figma để xác nhận). Một <mark>phần con ẩn</mark> <code>_Dot</code> giữ một cỡ, màu truyền từ cha, không thêm token. Nên giữ 6 của Badge đã duyệt, không kéo lên 8 của Untitled và Astryx để khỏi đổi bản đã chốt.",
         untitled="<code>foundations/dot-icon.tsx</code>: sm 8, md 10, dùng trong <code>tags.tsx</code>, <code>badges.tsx</code>, <code>select.demo.tsx</code>.",
         ours="<code>design-system/components/base/badge.md</code>: Chấm 6 × 6, <code>size/sm</code>, màu <code>color/chip/*</code>. Chưa có component riêng.",
         astryx="<code>status-dot</code> 8px, có <code>isPulsing</code> (<code>design/design.md</code>).",
         pv=kit.panes(pv_dot),
         opts=[("part", "Tách phần con _Dot cỡ 6, Badge, Tag, marker dùng instance, nhìn không đổi", True), ("keep", "Giữ chấm vẽ riêng trong từng component", False)]),

    dict(id="ms11", grp="Video", title="Video bằng chứng hiện nút Play thế nào?",
         why="SOP có <mark>video cắt chì, video bắt sâu</mark> (<code>docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md</code>). Điều vận xem lại trong thư viện ảnh của lệnh, nên ảnh nhỏ video phải khác ảnh chụp. Nút 80 của Untitled là cho video trang giới thiệu, quá to với ảnh nhỏ 96 × 72. Nền mờ nhẹ lên ảnh ngoài trời khó đọc, nên dùng <code>color/bg/overlay_solid</code> (DEC-327). Bản tam giác tô đẹp hơn nhưng phải thêm một ngoại lệ fill.",
         untitled="<code>foundations/play-button-icon.tsx</code>: tròn 80, <code>bg-alpha-white/30</code>, <code>backdrop-blur</code>, icon tô 20.",
         ours="Lucide <code>play</code>, nghĩa Bắt đầu trong <code>design-system/foundations/icon.md</code>. Chưa có lớp phủ video.",
         astryx="Không có.",
         note="Phụ thuộc ms03: nếu không thêm VID thì mục này chỉ áp cho ảnh nhỏ. Mở lại DEC-329 chỉ khi chọn bản tô: DEC đó giới hạn Fill=On ở <code>star</code>, <code>pin</code>, <code>flag</code> và 2 icon cảnh báo; bằng chứng mới là video trong SOP, chưa xét lúc chốt.",
         pv=kit.panes(pv_play, platforms=("web", "mobile")),
         opts=[("line", "Lớp phủ tròn 32 size/4xl, icon play nét trắng, nền overlay_solid, chỉ trên ảnh nhỏ video", True),
               ("fill", "Như trên nhưng tam giác tô, thêm play vào danh sách Fill=On của DEC-329", False)]),

    dict(id="ms12", grp="Logo đối tác", title="Hai bộ Payment trùng nhau xử lý sao?",
         why=f"DEC-329 đã áp: <mark>{N_PAY_SVG} logo</mark> ở <code>design-system/icons/payment</code> và section <code>Master · Payment, Social</code> trên Figma. Cạnh đó vẫn còn bộ cũ <code>Payment method icon</code> <mark>18 logo</mark>, có 2 logo Việt Nam <b>NAPAS, VietQR</b> mà bộ Untitled không có, và mô tả trên Figma vẫn ghi <code>_Card brand</code> của <code>Payment input</code> dùng bộ này. Xoá bộ cũ thì mất NAPAS; giữ cả hai thì có 2 logo Visa để chọn. Thẻ tín dụng trong tài liệu nghiệp vụ: {N_CARD} file, VietQR, NAPAS mới là loại gần với trả hộ.",
         untitled="<code>foundations/payment-icons</code>, dùng ở <code>base/input/input-payment.tsx</code>. Không có NAPAS, VietQR, MoMo, VNPay.",
         ours="<code>Payment method icon</code> 6708:100826, section <code>Master · Payment, Social</code> 7145:113000.",
         astryx="Không có bộ logo thanh toán.",
         note="<code>design-system/foundations/icon-sets.md</code> ghi \"Không có MoMo, VNPay, Napas, Zalo; cần thì thêm riêng ở logo.md\", lệch với bộ cũ đang có NAPAS, VietQR. Chốt mục này thì sửa câu đó. Mình đọc mô tả Figma, chưa mở instance trong <code>_Card brand</code>.",
         pv=kit.panes(pv_pay),
         opts=[("one", "Một bộ: 56 logo Untitled + NAPAS, VietQR, đổi _Card brand sang bộ này, xoá Payment method icon", True), ("both", "Giữ cả hai bộ: bộ cũ cho Payment input, bộ mới để dành", False)]),

    dict(id="ms13", grp="Logo đối tác", title="Bank logo 69 ngân hàng giữ thế nào?",
         why=f"Untitled không có bộ này. Ngân hàng xuất hiện ở <mark>{N_BANK} file</mark> tài liệu: lệnh chi trong <code>docs/payment-on-behalf/brainstorms/payment-on-behalf.md</code>, chọn ngân hàng của nhà cung cấp trong <code>docs/_reverse/business-partners/reverse-gaps.md</code>. Spec component chưa dùng ({S_BANK} spec). Danh sách theo VietQR có BIN trong mô tả biến thể, là <b>danh mục dùng chung</b> nên đúng tầng Lõi, không theo khách. DEC-326 đã để khối \"trỏ đối tác\" ở trang Logos, nên đây là đích của khối đó.",
         untitled="Không có. Gần nhất là <code>foundations/payment-icons</code>.",
         ours="<code>Bank logo</code> 6704:101952: Bank × SM 24, MD 32, LG 40, nhóm Nhà nước 4, cổ phần 33, số 4, nước ngoài 28.",
         astryx="Không có.",
         note="Chưa đếm được logo trên các màn Figma: quét cả file dễ treo plugin nên lượt này không chạy.",
         pv=kit.panes(pv_bank, platforms=("web", "mobile")),
         opts=[("keep", "Giữ 69 ngân hàng, 3 cỡ; dùng 24 trong danh sách chọn, ghi là danh mục Lõi trong icon-sets.md", True), ("top", "Rút còn 20 ngân hàng phổ biến, còn lại hiện chữ", False)]),

    dict(id="ms14", grp="Logo đối tác", title="App logo giữ những app nào?",
         why=f"Màn \"Kết nối / Tích hợp\" mà Figma nhắc tới: <mark>{N_CONNECT} file</mark> trong <code>docs/</code>. Bộ có 15 app, <mark>5 ô trống</mark> ghi \"chưa có nguồn\": MISA, VNPay, MoMo, ZaloPay, GHN. MISA lại là kết nối có thật nhất ({N_MISA} file, hoá đơn điện tử). Zalo ở {N_ZALO} file nhưng chủ yếu là cách làm cũ cần thay. Slack, Teams, Google Sheets chưa có nguồn nghiệp vụ. Social {N_SOC_SVG} logo theo DEC-329 không có Zalo, nên Zalo phải nằm ở bộ này.",
         untitled="<code>foundations/integration-icons</code> 16 logo, phần lớn công cụ AI và framework, dùng ở <code>base/dropdown/dropdown-integration.tsx</code>.",
         ours="<code>App logo</code> 6709:1020: 15 app × 24, 32, 40. Nguồn Simple Icons, Wikimedia theo ghi chú Figma.",
         astryx="Không có.",
         note=f"Đề xuất không đụng DEC-329. Mạng xã hội trong tài liệu nghiệp vụ: {N_SOCIAL} file, nên bộ Social hiện chưa có chỗ dùng; mình giữ theo DEC đã chốt. Lưu ý: Social trên Figma <b>đơn sắc đen</b> vì nguồn <code>currentColor</code>, ở Tối sẽ chìm; khi có màn dùng thì gắn <code>color/fg/primary</code> lúc đặt instance, không sửa master.",
         pv=kit.panes(pv_app),
         opts=[("real", "Giữ 10 app có file, bỏ 5 ô trống; MISA thêm khi có tệp chính thức từ đối tác", True), ("all", "Giữ 15 ô, chờ bộ logo từ đối tác", False), ("drop", "Bỏ hẳn App logo tới khi có màn Kết nối", False)]),

    dict(id="ms15", grp="Dấu tick", title="Check icon còn cần bộ riêng?",
         why=f"Bộ có 6 kiểu × 3 cỡ, <mark>{S_CHECK} spec dùng</mark>. Việc của nó là liệt kê điều kiện đã đạt, ví dụ đủ ảnh bắt buộc trước khi qua bước. Lucide <code>circle-check</code> với <code>color/fg/success-primary</code> làm được, đúng bảng nghĩa, không thêm component. Bản tô tròn xanh sẽ giống một bản tô nghiệp vụ mà DEC-329 vừa bỏ.",
         untitled="<code>Check icon</code> trong Figma Misc icons, ref chỉ ghi tên. Component React không có tên riêng.",
         ours="<code>Check icon</code> 6657:166083: Gray, Success, Mono × Light, Dark × 3 cỡ.",
         astryx="Không có bộ riêng.",
         pv=kit.panes(pv_check, platforms=("web", "mobile")),
         opts=[("lucide", "Xoá Check icon, danh sách điều kiện dùng circle-check và circle của Lucide", True), ("keep", "Giữ bộ, chờ màn cần", False)]),

    dict(id="ms16", grp="Đồ hoạ trang trí", title="Background pattern dùng ở đâu?",
         why="Untitled có 4 mẫu, nhưng trong component chỉ <code>empty-state.tsx</code> dùng. Bên mình, trang lỗi đang brainstorm khuyến nghị \"Featured icon + lưới mờ\" (<code>design-system/components/_work/error-page/page.json</code> D2). Trong thẻ, bảng dày dữ liệu hay ngoài trời, lưới mờ là nhiễu. Giữ mẫu lưới cho một chỗ và vẽ bằng <code>color/border/secondary</code> thì đổi theo Tối sẵn, không cần token mới.",
         untitled="<code>shared-assets/background-patterns</code>: <code>circle</code>, <code>square</code>, <code>grid</code>, <code>grid-check</code>, cỡ sm, md, lg.",
         ours="Chưa có. Chỉ có trong brainstorm <code>design-system/components/_work/error-page/page.json</code>.",
         astryx="<code>EmptyState</code> icon + tiêu đề + mô tả, không có nền trang trí (<code>design/design.md</code>).",
         note="Phụ thuộc D2 trang Error Page: nếu chọn \"Mã lỗi số lớn\" hoặc minh hoạ thì không cần mẫu nào, chọn \"Không dùng\" ở đây.",
         pv=kit.panes(pv_pattern, platforms=("web", "mobile")),
         opts=[("grid", "Chỉ mẫu lưới, chỉ cho trang lỗi cả màn, vẽ bằng color/border/secondary", True), ("none", "Không dùng mẫu nền nào", False), ("all", "Lấy cả 4 mẫu, dùng cả màn trống trong thẻ", False)]),

    dict(id="ms17", grp="Đồ hoạ trang trí", title="Màn trống dùng minh hoạ hay Featured icon?",
         why="Ở vùng dữ liệu rỗng, người điều vận cần biết <mark>vì sao rỗng và làm gì tiếp</mark> (<code>design/design.md</code>: \"Trạng thái rỗng nói vì sao và làm gì tiếp\"). Hình lớn chiếm chỗ trên bảng dày và sheet app 393. Bốn hình của Untitled là hộp, mây, tài liệu, thẻ, không gắn logistics. Bên mình đã có <code>design-system/components/_work/error-page/illos.py</code> vẽ riêng, có xe tải chờ, nhưng còn ở vòng brainstorm, chưa gắn token xong. Featured icon đã chốt ở DEC-329 nên làm ngay được.",
         untitled="<code>shared-assets/illustrations</code>: <code>box</code>, <code>cloud</code>, <code>documents</code>, <code>credit-card</code>, dùng trong <code>EmptyState.Illustration</code>.",
         ours="Chưa có component màn trống. <code>design-system/components/_work/error-page/illos.py</code> đang là nháp.",
         astryx="<code>EmptyState</code>: icon + tiêu đề + mô tả + hành động; Size=Compact trong khối nhỏ.",
         note="Hình minh hoạ trong xem thử lấy trực tiếp từ <code>illos.py</code>. Phụ thuộc D2 trang Error Page: trang lỗi cả màn có thể chọn khác, mục này chỉ nói về vùng dữ liệu rỗng.",
         pv=kit.panes(pv_illo, platforms=("web", "mobile")),
         opts=[("icon", "Vùng rỗng dùng Featured icon + chữ + hành động, không đưa minh hoạ vào foundation", True),
               ("illos", "Đưa bộ illos.py vào foundation, gắn token, dùng cho vùng rỗng lớn", False), ("untitled", "Lấy 4 hình của Untitled", False)]),

    dict(id="ms18", grp="Không lấy", title="Các món còn lại của Untitled có bỏ hẳn?",
         why="<code>Emoji</code>, <code>Cursor</code>, <code>Check item text</code>, <code>iPhone mockup</code>, <code>Credit card</code>, <code>Section divider</code> phục vụ trang giới thiệu, bảng giá, ảnh mockup. Không màn logistics nào cần. <code>Folder icon</code> có thể hữu ích cho hồ sơ chứng từ, nhưng Lucide <code>folder</code> đủ dùng. Ghi rõ vào tài liệu để lần sau không phải xét lại.",
         untitled="<code>06-icons.md</code> mục 6; <code>react/components/shared-assets</code>.",
         ours="Không có. Lucide <code>folder</code>, <code>check</code>.",
         astryx="Không có.",
         pv=kit.panes(pv_rest),
         opts=[("drop", "Không lấy, ghi danh sách này vào icon-sets.md kèm lý do", True), ("folder", "Không lấy, riêng Folder vẽ theo kiểu File type icon", False)]),
]


SPEC = dict(
    slug="misc", short="phần Misc icons",
    title="Foundations · Misc icons — giữ gì, bỏ gì?",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 02/11/2026",
    lead=("Trang này giúp quyết nhóm <b>icon đặc biệt ngoài Lucide</b>: nhãn tệp, cờ, logo đối tác, đồ hoạ trang trí. Kết luận chính: <mark>Figma đã có 7 bộ, tài liệu <code>icon-sets.md</code> đã có khung nhưng phần lớn chỉ một câu</mark>, gần như chưa spec nào dùng, nên việc cần làm là <b>rút gọn và ghi luật</b>, không phải thêm. "
          "Đồ marketing của Untitled (rating, mockup, 4 mẫu nền) đề xuất không lấy. Phương tiện xem ở trang riêng, Featured icon đã chốt. <mark>Chưa sửa token nào.</mark>"),
    kpis=[(str(len(CMP)), "dòng đối chiếu", ""), (str(COUNT["gap"]), "món Untitled mình không có", "bad"), (f"{len(THIN)}/{len(SET_NAMES)}", "bộ trong icon-sets.md chỉ ghi một câu", "bad"), (str(S_BANK + S_APP + S_CHECK), "spec dùng Bank, App, Check", "")],
    tag_kind=None,
    screens=dict(
        title="Xem trên màn thật",
        intro="Màn mẫu dựng bằng token thật, có thêm khối <b>Chứng từ của lệnh</b> ở màn chi tiết Web và App. Bấm <b>Bộ giá trị</b>: <b>Hiện tại</b> nhãn đuôi 5 màu như Figma, <b>Sau khi đổi</b> nhãn một màu theo ms02. Biểu tượng tệp dựng lại theo số Figma 6657:165918.",
        proposal_css=".tp-f.tp-prop{--ms-prop:1}", logo_svg=None, gridov=False, overlay_html=overlay),
    sections=[
        dict(title="Bảng đối chiếu Misc icons — Untitled ↔ mình",
             intro=(f"{len(CMP)} dòng: <b>{COUNT['ok']} giống</b> · <b>{COUNT['diff']} khác có lý do</b> · <b>{COUNT['gap']} mình thiếu</b> · <b>{COUNT['own']} chỉ mình có</b>. "
                    "Nguồn Untitled: <code>design/_ref/untitled-ui/06-icons.md</code> mục 6 (Figma, chỉ ghi cấu trúc) và <code>react/components</code>. Ref không đếm biến thể, nên dòng Figma không có số là <b>ref không ghi</b>, chưa kết luận Untitled ít."),
             html=CMP_HTML),
        dict(title="Bảy bộ đang có trên Figma",
             intro="Đọc từ trang <code>Misc icons</code> 6702:122238 và <code>.claude/state/figma/ds-v2-snapshot.json</code> ngày 02/11. Cột spec đếm trong <code>design-system/components/base</code>, <code>application</code>. Chưa đếm instance trên màn vì quét cả file dễ treo plugin.",
             html=kit.rows(["Bộ", "Mã Figma", "Biến thể", "Số spec", "Nơi dùng đọc được"], FIGMA_ROWS)),
        dict(title="Đã chốt, không mở lại",
             intro="DEC đang hiệu lực liên quan. Chỉ <code>ms11</code> phương án tô mới mở lại DEC-329, có ghi lý do tại mục đó.",
             html=kit.rows(["Mã", "Đã chốt"], [
                 ["DEC-329", "Đã áp (<code>tokens.json</code> 0.27.0): bộ Payment 56, Social 22 ở <code>design-system/icons</code> và Figma; Featured icon 4 kiểu, 4 cỡ, đã chuyển sang trang Base; Fill=On cho star, pin, flag; bảng nghĩa icon."],
                 ["DEC-331", "Misc icons có mã trạng thái riêng <code>misc-icon</code>, Phương tiện có mã <code>vehicle</code>, duyệt riêng với <code>icon</code>."],
                 ["DEC-332", "Tài liệu Misc icons ở <code>design-system/foundations/icon-sets.md</code>; <code>_scripts/ds-deps.py</code> dò stale theo mã này."],
                 ["DEC-326", "Mỗi khách một bản app trên store; trang Logos có khối trỏ đối tác; logo khách theo tham số."],
                 ["DEC-327", "<code>color/bg/overlay_solid</code> 50% cho máy yếu; nút giữ phẳng."],
                 ["DEC-328", "<code>radius/inner</code> 8, <code>radius/card</code> 12, một bộ web và app."],
                 ["DEC-324", "Web vẽ 1920, kiểm 1280 và 1024; app vẽ 393, thử 320. Xem thử trên trang theo khung này."],
                 ["DEC-310", "Chấm trong Badge kiểu Dot, chữ nét thường."],
                 ["DEC-266", "Phương tiện ở <code>design-system/foundations/vehicle.md</code>, xét ở trang <code>vehicle</code> (<code>DEC-334</code>)."],
             ])),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)",
             html=kit.rows(["Bộ", "Sau khi chốt", "Đổi gì trên Figma"], [
                 ["File type icon", "PDF, DOC, XLS, IMG, VID, Other · 32, 40 · nhãn một màu", "Thêm VID, bỏ CSV, ZIP, đổi nền nhãn sang biến"],
                 ["Flag", "25 nước, tròn, 16, 20, 24", "Bỏ 75 biến thể chữ nhật"],
                 ["Payment", "56 + NAPAS, VietQR", "Đổi <code>_Card brand</code>, xoá bộ cũ"],
                 ["Social", "22 logo theo DEC-329, đơn sắc", "Không đổi master; gắn màu khi đặt instance"],
                 ["Bank logo", "69 ngân hàng, 3 cỡ", "Không đổi"],
                 ["App logo", "10 app có file", "Bỏ 5 ô trống"],
                 ["Check icon", "Bỏ, dùng Lucide", "Xoá component set"],
                 ["Mới", "<code>_Dot</code> cỡ 6 · lớp phủ Play 32 · 2 huy hiệu store · nền lưới cho trang lỗi", "Thêm phần con, không thêm token"],
                 ["Không lấy", "Rating, QR hiện mã, Illustration, Emoji, Cursor, mockup", "Không đổi"],
             ])),
    ],
    items=ITEMS,
    final=("Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/icon-sets.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>misc-icon = approved</b> (<code>ds-foundation-status.py set misc-icon approved</code>). "
           "Component đang có bị đánh stale và sync dần (rule ds-stale). Việc riêng của trang này: theo khuyến nghị thì <b>không có token mới</b>, phần lớn là sửa bộ trên Figma; sửa ghi chú <code>File type icon</code> trong <code>design-system/components/application/field-upload.md</code>; thêm <code>P-link-tai-app</code> vào bảng tham số nếu chọn ms05."),
    css=CSS, js="",
)
