#!/usr/bin/env python3
"""SPEC trang review Foundations · Logo. Dựng: python3 _scripts/foundation_review/build.py logo

Logo là đồ hoạ thật: SVG đọc từ design/brand/invlogis/logo/, gom thành sprite <symbol> (id đổi tiền tố lgs-), ảnh PNG nhúng base64 một lần qua lớp CSS.
Tương phản tính ở đây từ mã màu trong file, không chép tay.
"""
import base64
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kit  # noqa: E402
from PIL import Image  # noqa: E402

ROOT = kit.ROOT
LG = ROOT / "design/brand/invlogis/logo"
DELTA = ROOT / "design/brand/delta/logo/delta-primary.svg"
DELTA_REV = ROOT / "design/brand/delta/logo/delta-reverse.svg"
INNVIE_REV = ROOT / "design/brand/innvie/innvie-logo-reverse.svg"
SVG_COUNT = len(list(LG.glob("*.svg")))


# ---------- đo ----------
def _lum(h):
    h = h.lstrip("#")
    r = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda x: x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4
    return .2126 * f(r[0]) + .7152 * f(r[1]) + .0722 * f(r[2])


def ratio(a, b):
    x, y = sorted((_lum(a), _lum(b)), reverse=True)
    return (x + .05) / (y + .05)


def rs(a, b):
    return f"{ratio(a, b):.2f}".replace(".", ",") + ":1"


TOK = kit.TCSS
BG_LIGHT = re.search(r"--white:\s*(#\w+)", TOK).group(1)
BG_DARK = re.search(r"--dark-0:\s*(#\w+)", TOK).group(1)
_dsvg = DELTA.read_text()
DELTA_INK = re.search(r'fill="(#[0-9A-Fa-f]{6})"', _dsvg).group(1)
DW, DH = [float(x) for x in re.search(r'viewBox="\S+ \S+ (\S+) (\S+)"', _dsvg).groups()]
DELTA_TILE = re.search(r"\| P-mau-logo \|.*?\| (#[0-9A-Fa-f]{6}) \(user chốt", (ROOT / "docs/_product/tenant-parameters.md").read_text()).group(1)


# ---------- sprite SVG ----------
SOURCES = {
    "primary": "invlogis-primary.svg", "reverse": "invlogis-reverse.svg", "mono-black": "invlogis-mono-black.svg", "mono-white": "invlogis-mono-white.svg",
    "stacked": "invlogis-stacked.svg", "by": "invlogis-by-innvie.svg", "by-rev": "invlogis-by-innvie-reverse.svg", "tagline": "invlogis-tagline.svg", "tagline-en": "invlogis-tagline-en.svg",
    "sym": "invlogis-symbol.svg", "sym-rev": "invlogis-symbol-reverse.svg", "sym-mono": "invlogis-symbol-mono.svg", "innvie": "innvie-logo.svg", "innvie-mono": "innvie-logo-mono.svg",
}
VB, _sprite = {}, []


def _add(key, text):
    text = re.sub(r"<\?xml[^>]*>", "", text)
    vb = re.search(r'viewBox="([^"]+)"', text).group(1)
    inner = re.search(r"<svg[^>]*>(.*)</svg>", text, flags=re.S).group(1)
    inner = re.sub(r'id="([^"]+)"', lambda m: f'id="lgs-{key}-{m.group(1)}"', inner)
    inner = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#lgs-{key}-{m.group(1)})", inner)
    VB[key] = vb
    _sprite.append(f'<symbol id="lgs-{key}" viewBox="{vb}">{inner}</symbol>')


for k, f in SOURCES.items():
    _add(k, (LG / f).read_text())
_add("innvie-rev", INNVIE_REV.read_text())
# bản favicon: bỏ <style> của file (lớp .s .d và media query sẽ lan ra cả trang), tô thẳng đúng màu file ghi
_fav = (LG / "favicon.svg").read_text()
_fp = re.findall(r'<path class="(\w)" d="([^"]+)"', _fav)
_stops = re.findall(r'stop-color="(#\w+)"', _fav)
FAV_S, FAV_D = _stops[0], _stops[2]
FAVD_S, FAVD_D = re.search(r"\.s\{fill:(#\w+)\}\.d\{fill:(#\w+)\}", _fav).groups()
_fsvg = lambda s, d: f'<svg viewBox="0 0 32 32">' + "".join(f'<path fill="{s if c == "s" else d}" d="{p}"/>' for c, p in _fp) + "</svg>"
_add("fav", _fsvg(FAV_S, FAV_D))
_add("fav-rev", _fsvg(FAVD_S, FAVD_D))
SPRITE = '<svg aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden">' + "".join(_sprite) + "</svg>"


def use(key, h=24, label="", cls=""):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    # khung ngoài bắt đầu từ 0 0: <use> đặt symbol tại gốc toạ độ, viewBox lệch gốc sẽ cắt mất mép trái
    w0, h0 = VB[key].split()[2:]
    return f'<svg class="lg-svg {cls}" {a} viewBox="0 0 {w0} {h0}" style="height:{h}px;width:auto"><use href="#lgs-{key}" width="{w0}" height="{h0}"/></svg>'


def duo(light, dark, h=24, label=""):
    """Bản đúng theo chế độ: mỗi khung chỉ hiện một bản."""
    return use(light, h, label, "lg-l") + use(dark, h, label, "lg-d")


word = lambda h=24, label="Logo Invlogis": duo("primary", "reverse", h, label)
fav = lambda h=24, label="Ký hiệu Invlogis": duo("fav", "fav-rev", h, label)


def delta(h=24, mode="auto"):
    """mode: raw = tệp thật không xử lý · auto = Tối hiện delta-reverse.svg."""
    w = round(h * DW / DH)
    box = f'style="height:{h}px;width:{w}px"'
    if mode == "raw":
        return f'<span class="lg-delta" role="img" aria-label="Logo Delta" {box}></span>'
    return f'<span class="lg-delta lg-l" role="img" aria-label="Logo Delta" {box}></span><span class="lg-delta lg-whitesim lg-d" role="img" aria-label="Logo Delta, bản nền tối" {box}></span>'


def tile(ch="D", h=24, color=None):
    bg = color or DELTA_TILE
    return f'<span class="lg-tile" style="height:{h}px;width:{h}px;background:{bg};font-size:{round(h * .5)}px">{ch}</span>'


def b64(p):
    return base64.b64encode(p.read_bytes()).decode()


def lab(x):
    return f'<span class="lg-cap">{x}</span>'


CSS = f"""
.lg-svg{{display:block;flex:none}}
[data-theme="dark"] .lg-l{{display:none}}[data-theme="light"] .lg-d{{display:none}}
.lg-delta{{display:block;flex:none;background:url(data:image/svg+xml;base64,{b64(DELTA)}) left center/contain no-repeat}}
.lg-whitesim{{background-image:url(data:image/svg+xml;base64,{b64(DELTA_REV)})}}
.lg-tile{{display:inline-flex;align-items:center;justify-content:center;flex:none;border-radius:var(--radius-control);color:var(--white);font-weight:600;font-family:var(--font-body)}}
.lg-cap{{display:block;font:500 11px/15px Inter,sans-serif;color:var(--color-text-tertiary);margin-top:4px}}
.rv .lg-cap code{{font-size:10.5px;line-height:14px}}
.lg-r{{display:flex;flex-wrap:wrap;align-items:flex-end;gap:14px 20px}}.lg-rc{{display:flex;flex-wrap:wrap;align-items:center;gap:12px 18px}}
.lg-st{{display:grid;gap:12px}}.lg-c22{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}.lg-c2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}}
.lg-cell{{border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);padding:10px;min-width:0;background:var(--color-bg-primary)}}
.lg-plate{{display:inline-flex;align-items:center;background:var(--white);padding:var(--space-sm) var(--space-md);border-radius:var(--radius-control)}}
.lg-hscroll{{overflow-x:auto;padding-bottom:4px}}
.lg-g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(204px,1fr));gap:10px;margin:10px 0}}
.lg-v{{background:#fff;border:1px solid #E2E8F0;border-radius:12px;overflow:hidden;display:flex;flex-direction:column;min-width:0}}
.lg-vb{{height:110px;display:flex;align-items:center;justify-content:center;padding:14px;min-width:0}}.lg-vb svg{{max-width:100%}}
.lg-vt{{padding:7px 10px;font-size:12px;line-height:17px;border-top:1px solid #EEF2F6}}.lg-vt b{{display:block}}
.lg-side{{width:240px;max-width:100%;border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);padding:var(--space-lg);display:grid;gap:var(--space-xs);background:var(--color-bg-primary);flex:none}}
.lg-side.slim{{width:64px;justify-items:center;padding:var(--space-lg) 10px}}
.tp-f{{--d-logo:28px}}
.lg-head{{display:flex;align-items:center;gap:var(--space-md);min-height:var(--control-height-md);margin-bottom:var(--space-lg);min-width:0}}
.lg-head .nm{{min-width:0;flex:1}}.lg-trunc{{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.lg-fr{{width:393px;flex:none;border:1px solid var(--color-border-secondary);border-radius:var(--radius-card);overflow:hidden;background:var(--color-bg-primary);display:flex;flex-direction:column}}
.lg-bar{{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-lg) var(--grid-margin);border-bottom:1px solid var(--color-border-secondary)}}
.lg-spl{{height:340px;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}}
.lg-foot{{position:absolute;left:0;right:0;bottom:var(--space-3xl);display:flex;align-items:center;justify-content:center;gap:var(--space-sm);color:var(--color-text-secondary)}}
.lg-mini{{border:1px solid var(--color-border-secondary);border-radius:var(--radius-md);overflow:hidden;background:var(--color-bg-primary);min-width:0}}
.lg-mini .hd{{display:flex;align-items:center;gap:var(--space-md);padding:var(--space-md) var(--space-lg);border-bottom:1px solid var(--color-border-secondary);min-height:44px}}
.lg-mini .bd{{padding:var(--space-md) var(--space-lg)}}.lg-sk{{display:block;height:8px;border-radius:4px;background:var(--color-bg-tertiary);margin:6px 0}}
.lg-clear{{display:inline-block;outline:1px dashed var(--color-text-tertiary);padding:var(--pad);position:relative}}.lg-clear>span{{display:block;outline:1px solid var(--color-accent-solid)}}
.lg-tab{{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px;border-radius:9px 9px 0 0;font:12px Inter,sans-serif}}
.lg-ico{{width:60px;height:60px;border-radius:22.4%;background:url(data:image/png;base64,{b64(LG / "apple-touch-icon-180.png")}) center/cover;flex:none}}
.lg-and{{width:72px;height:72px;overflow:hidden;position:relative;flex:none;background:url(data:image/png;base64,{b64(LG / "android-background-432.png")}) center/108px}}
.lg-and i{{position:absolute;inset:0;background:url(data:image/png;base64,{b64(LG / "android-foreground-432.png")}) center/108px}}
.lg-sw{{display:grid;grid-template-columns:repeat(auto-fill,minmax(92px,1fr));gap:6px}}.lg-sw div{{height:44px;border-radius:8px;border:1px solid #E2E8F0;padding:4px 6px;font:500 10.5px/13px Inter,sans-serif;display:flex;align-items:flex-end}}
.lg-tt{{width:100%;border-collapse:collapse;font-size:12.5px}}.lg-tt th,.lg-tt td{{text-align:left;padding:5px 8px;border-bottom:1px solid var(--color-border-secondary)}}.lg-tt .add td{{background:var(--color-bg-secondary);font-weight:600}}
"""

PX = lambda n: f'<img alt="" width="{n}" height="{n}" style="display:block;image-rendering:auto" src="data:image/png;base64,{b64(LG / f"favicon-{n}.png")}">'


# ---------- bảng đối chiếu: trạng thái đếm thẳng từ bảng ----------
OK, DIFF, GAP, OWN = '<span class="st-ok">Giống</span>', '<span class="st-diff">Khác có lý do</span>', '<span class="st-gap">Mình thiếu</span>', '<span class="st-own">Chỉ mình có</span>'
CMP = [
    ("<code>Company logo</code> › Logo: ký hiệu + chữ, code <code>UntitledLogo</code>", "<code>invlogis-primary.svg</code>, set Figma <code>Logo</code> (DEC-261)", OK, "Cùng vai: logo đầy đủ của sản phẩm."),
    ("<code>Company logo</code> › Logomark, code <code>UntitledLogoMinimal</code>", "<code>invlogis-symbol.svg</code> và bản nhỏ <code>favicon.svg</code>", DIFF, "Untitled một bản cho mọi cỡ. Ký hiệu của mình mảnh (rộng 1/5 cao) nên có bản dày riêng dưới 48px, xem lg03."),
    ("Đổi chế độ bằng lớp màu <code>fill-fg-primary</code>", "Hai file <code>primary</code> / <code>reverse</code>", DIFF, "Chữ i và chữ v có gradient riêng cho từng nền (DEC-073), một biến màu không thay được."),
    ("<code>Placeholder company logos</code>, nền sáng", "Set Figma <code>Company logo</code>, tên công ty giả (DEC-261)", OK, "Logo khách giữ chỗ trong mẫu."),
    ("<code>Placeholder company logos</code>, <code>Dark background</code>", "Chưa có luật logo khách trên Tối", GAP, f"Delta chữ đen trên nền Tối chỉ {rs(DELTA_INK, BG_DARK)}, xem lg08."),
    ("<code>Placeholder press logos</code> (<code>Press logo</code>)", "Không có", DIFF, "Khối báo chí phục vụ trang marketing. Sản phẩm vận hành không dùng, đề xuất bỏ (lg01)."),
    ("90 logo giả dạng color style, <code>AvatarCompanyIcon</code>", "<code>Company avatar</code> ở <code>design-system/components/base/avatar.md</code>", DIFF, "Mình có component tổ chức, không cần kho ảnh giả."),
    ("Căn nhiều logo cân thị giác: frame cùng cao, gợi ý 48px", "Chưa có luật căn; <code>Bank logo</code> có khung SM, MD, LG (DEC-281)", GAP, "Cần khi có màn liệt kê nhiều khách, ghi một câu ở <code>logo.md</code>."),
    ("Mặc định <code>h-8</code> = 32; 8 chỗ điều hướng dùng <code>h-6</code> = 24", "Đầu menu 28 (<code>control/height/sm</code>)", DIFF, "28 lấy theo cao <code>control/height/sm</code>, tức mượn vai control. lg05 đề xuất về 24, bằng Untitled."),
    ("Thanh Slim: <code>UntitledLogoMinimal</code> <code>size-6</code> = 24", "Thu gọn 64, chưa ghi dùng bản nào", GAP, "Khách có logo chữ thì bản thu gọn lấy gì, xem lg14."),
    ("Vùng trống, cỡ tối thiểu: ref không ghi", "<code>logo-spec.md</code> Mục 2: 1 x, cao ≥ 20px", OWN, "Ref Untitled mục 7 chỉ ghi cấu trúc, không kết luận được họ có luật hay không."),
    ("Đơn sắc: ref không ghi", "<code>mono-black</code>, <code>mono-white</code>, <code>symbol-mono</code>", OWN, "Cho in một màu, đóng dấu, nền cobalt."),
    ("Xếp dọc: ref không ghi", "<code>invlogis-stacked.svg</code>", OWN, "Splash, bìa dọc."),
    ("Kèm khẩu hiệu: ref không ghi", "<code>invlogis-tagline.svg</code>, <code>-tagline-en</code>", OWN, "Marketing, không vào sản phẩm (lg02)."),
    ("Chữ ký pháp nhân: không có", "<code>invlogis-by-innvie.svg</code> (+ <code>-reverse</code>), <code>innvie-logo.svg</code>", OWN, "innvie là pháp nhân, Invlogis là thương hiệu (DEC-055)."),
    ("Favicon, icon app của sản phẩm: ref không ghi", "<code>favicon.svg</code>, PNG 16/32/48, <code>app-icon-1024.png</code>, Android 432", OWN, "Component <code>App icons</code> của Untitled nằm ở Misc icons, ref chưa đọc nội dung."),
    ("Logo theo khách: không có", "<code>P-logo</code>, <code>P-mau-logo</code>", OWN, "Riêng của sản phẩm SaaS nhiều khách. Untitled là kit một thương hiệu."),
    ("Logo đối tác: <code>Integration icon</code>, <code>Payment method icon</code>, <code>Social icon</code> ở Misc icons", "Set Figma <code>Bank logo</code> (69 ngân hàng, DEC-281), <code>App logo</code>", DIFF, "Cùng chỗ với Untitled: ở nhóm Misc, không ở trang Logos."),
    ("Component code tại <code>react/components/foundations/logo</code>", "Set Figma có, file spec trong <code>design-system/components/</code> chưa có", GAP, "Xem lg06."),
]
CNT = Counter(r[2] for r in CMP)
CMP_HTML = kit.rows(["Untitled UI v8", "Mình", "Trạng thái", "Ghi chú"], [list(r) for r in CMP])
SUMMARY = f"<b>{len(CMP)} dòng</b>: {CNT[OK]} giống · {CNT[DIFF]} khác có lý do · {CNT[GAP]} mình thiếu · {CNT[OWN]} chỉ mình có."


# ---------- bộ biến thể thật ----------
def vcard(key, bg, name, when, h=44, fg="#171717"):
    return (f'<div class="lg-v"><div class="lg-vb" style="background:{bg}">{use(key, h, name)}</div>'
            f'<div class="lg-vt"><b><code>{name}</code></b><span class="muted">{when}</span></div></div>')


PAPER, NIGHT, COBALT, SMOKE = "#FAF8F4", "#0B1033", "#2F43DB", "#E6EAF8"
GALLERY = '<div class="lg-g">' + "".join([
    vcard("primary", PAPER, "invlogis-primary.svg", "Mặc định, nền sáng", 40),
    vcard("reverse", NIGHT, "invlogis-reverse.svg", "Nền tối", 40),
    vcard("mono-black", "#FFFFFF", "invlogis-mono-black.svg", "In một màu, đóng dấu", 40),
    vcard("mono-white", COBALT, "invlogis-mono-white.svg", "Nền cobalt, ảnh tối", 40),
    vcard("stacked", SMOKE, "invlogis-stacked.svg", "Splash, bìa dọc", 80),
    vcard("by", PAPER, "invlogis-by-innvie.svg", "Chân trang, hợp đồng. Cao ≥ 48", 56),
    vcard("by-rev", NIGHT, "invlogis-by-innvie-reverse.svg", "Như trên, nền tối", 56),
    vcard("tagline", PAPER, "invlogis-tagline.svg", "Bìa deck, landing. Cao ≥ 64", 64),
    vcard("tagline-en", PAPER, "invlogis-tagline-en.svg", "Bản tiếng Anh", 64),
    vcard("sym", PAPER, "invlogis-symbol.svg", "Hình đại diện. Cao ≥ 48", 72),
    vcard("sym-rev", NIGHT, "invlogis-symbol-reverse.svg", "Nền tối. Cao ≥ 48", 72),
    vcard("sym-mono", "#FFFFFF", "invlogis-symbol-mono.svg", "Đơn sắc", 72),
    vcard("fav", "#FFFFFF", "favicon.svg", "Tab trình duyệt, cỡ nhỏ", 48),
    vcard("innvie", PAPER, "innvie-logo.svg", "Chỉ pháp nhân: chữ ký, giấy tờ", 36),
    vcard("innvie-mono", "#FFFFFF", "innvie-logo-mono.svg", "Pháp nhân, đơn sắc", 36),
]) + "</div>"

_cr = lambda part, fg: (part, f"<code>{fg}</code>", f"n:{rs(fg, BG_LIGHT)}", f"n:{rs(fg, BG_DARK)}")
CONTRAST = kit.rows(["Phần", "Mã màu trong file", f"Trên nền Sáng {BG_LIGHT}", f"Trên nền Tối {BG_DARK}"], [
    _cr("Bản chính: chữ mực", "#0E1442"), _cr("Bản chính: đáy thân i", "#1B2491"), _cr("Bản chính: chấm i, điểm sáng nhất", "#5A6CF0"),
    _cr("Bản tối: chữ trắng", "#FFFFFF"), _cr("Bản tối: đáy thân i", "#5B6EF5"), _cr("Bản tối: đáy chữ v", "#A3B0FF"),
    _cr("Bản favicon: thân", FAV_S), _cr("Bản favicon: chấm", FAV_D), _cr("Favicon tối: thân", FAVD_S),
    _cr("Delta: màu chữ trong delta-primary.svg", DELTA_INK), _cr("Ô màu Delta <code>P-mau-logo</code>", DELTA_TILE),
])

SURF = kit.rows(["Điểm chạm", "Logo chính", "Invlogis có hiện?", "Tầng", "Tham số, nguồn"], [
    ["Đầu menu web, mở rộng", "Logo khách", "Không", "<code>[Lõi] [Cấu hình]</code>", "<code>P-logo</code> (Delta: <code>delta-primary.svg</code>)"],
    ["Đầu menu web, thu gọn 64", "Logo vuông của khách, thiếu thì chữ cái trên ô", "Không", "<code>[Lõi] [Cấu hình]</code>", "<code>P-logo</code>, <code>P-mau-logo</code> (Delta: " + DELTA_TILE + "), đề xuất <code>P-logo-vuong</code>"],
    ["Đầu màn chủ app 393", "Logo khách", "Không", "<code>[Lõi] [Cấu hình]</code>", "<code>P-logo</code>; chưa ghi app trong bảng tham số"],
    ["Đăng nhập, đã biết khách", "Logo khách", "Dòng nhỏ ở chân", "<code>[Lõi] [Cấu hình]</code>", "<code>P-logo</code>, đề xuất <code>P-hien-van-hanh-tren</code>"],
    ["Đăng nhập, chưa biết khách", "Invlogis", "Là logo chính", "<code>[Lõi]</code>", "Phụ thuộc <code>saas-core-vs-tenant.md</code> Mục 7 việc 3"],
    ["Splash web, app", "Logo khách", "Dòng nhỏ ở chân", "<code>[Lõi] [Cấu hình]</code>", "<code>P-logo</code>, DEC-037 (xem lg10)"],
    ["Trang lỗi 500, bảo trì", "Logo khách nếu đã biết, không thì Invlogis", "Theo cột bên", "<code>[Lõi]</code>", "<code>error-page</code>"],
    ["Email giao dịch, chứng từ in", "Logo khách", "Không", "<code>[Cấu hình]</code>", "Đề xuất mới, <code>P-logo</code> chưa ghi hai chỗ này (lg07)"],
    ["Favicon, icon app", "Invlogis", "Là logo chính", "<code>[Lõi]</code>", "xem lg11"],
    ["Màn Giới thiệu", "<code>invlogis-by-innvie.svg</code>", "Là logo chính", "<code>[Lõi]</code>", "<code>touchpoints.md</code>"],
])

BUNDLE = kit.rows(["Việc", "Bộ đề xuất", "Mục"], [
    ["Bảng trạng thái", "Thêm mã <code>logo</code>, nối vào dò stale", "lg00"],
    ["Tổ chức", "Logo sản phẩm · Logo khách · trỏ sang Bank logo. Bỏ Press logos", "lg01"],
    ["Biến thể trong sản phẩm", "<code>primary</code>, <code>reverse</code>, <code>stacked</code>, <code>by-innvie</code> + ký hiệu bản nhỏ. Còn lại ở bộ nhận diện", "lg02, lg03"],
    ["Cỡ", "Đầu menu 24, app 24, đăng nhập 40, splash 64. Tối thiểu cao 20, vùng trống 1 x (thanh điều hướng 0,5 x)", "lg04, lg05"],
    ["Token cỡ", "Không thêm: <code>size/3xl</code>, <code>size/5xl</code>, <code>size/7xl</code>", "lg05"],
    ["Component", "<code>Logo</code> và <code>Tenant logo</code>, 2 spec mới; xoá 2 bản cũ trên Figma", "lg06"],
    ["Logo khách", "Thêm <code>P-logo-nen-toi</code>, <code>P-logo-vuong</code>, <code>P-hien-van-hanh-tren</code>. <code>P-mau-logo</code> chỉ tô ô chữ cái", "lg07, lg08, lg09, lg14"],
    ["Invlogis khi có khách", "Chân đăng nhập, splash: \"Vận hành trên\" + logo chữ cao 20", "lg10"],
    ["Favicon, icon app, splash", "Favicon Invlogis chung, icon app chờ Mục 7 việc 3, splash theo chế độ", "lg11, lg12"],
    ["App 393", "Chỉ màn chủ có logo, cao 24", "lg13"],
    ["Màu thương hiệu", "Giữ ngoài <code>tokens.css</code>", "lg15"],
])


# ---------- xem thử ----------
def p_status(m, p):
    return ('<table class="lg-tt"><tr><th>Mã</th><th>Mục</th><th>Ở đâu</th><th>Trạng thái</th></tr>'
            '<tr><td>icon</td><td>Icon</td><td>icon.md (mục 11)</td><td>draft</td></tr>'
            '<tr class="add"><td>logo</td><td>Logo</td><td>logo.md (mục 12)</td><td>draft → theo lần chốt này</td></tr></table>')


def p_org(m, p):
    return ('<div class="lg-c2">'
            f'<div class="lg-cell">{word(24)}{lab("Khối 1 · Logo sản phẩm")}</div>'
            f'<div class="lg-cell"><div class="lg-rc">{delta(24)}{tile("M", 24, "#262626")}</div>{lab("Khối 2 · Logo khách: tệp thật, hoặc chữ cái trên ô")}</div>'
            f'<div class="lg-cell"><span class="type-label">Bank logo · App logo</span>{lab("Khối 3 · Đối tác: chỉ trỏ sang Misc icons")}</div></div>')


def p_variants(m, p):
    if m == "light":
        return (f'<div class="lg-c2"><div class="lg-cell">{use("primary", 28, "Logo chính")}{lab("Mặc định")}</div><div class="lg-cell">{use("fav", 28, "Ký hiệu")}{lab("Ký hiệu, bản nhỏ")}</div>'
                f'<div class="lg-cell">{use("stacked", 64, "Xếp dọc")}{lab("Xếp dọc, splash")}</div><div class="lg-cell">{use("by", 48, "By innvie")}{lab("By innvie, Giới thiệu")}</div></div>')
    return (f'<div class="lg-c2"><div class="lg-cell">{use("reverse", 28, "Logo nền tối")}{lab("Mặc định")}</div><div class="lg-cell">{use("fav-rev", 28, "Ký hiệu")}{lab("Ký hiệu, bản nhỏ")}</div>'
            f'<div class="lg-cell">{use("sym-rev", 64, "Ký hiệu nền tối")}{lab("Xếp dọc chưa có bản tối, đang thay bằng ký hiệu")}</div><div class="lg-cell">{use("by-rev", 48, "By innvie")}{lab("By innvie, Giới thiệu")}</div></div>')


def p_small(m, p):
    s, f = ("sym", "fav") if m == "light" else ("sym-rev", "fav-rev")
    row = lambda k: '<div class="lg-r">' + "".join(f'<div>{use(k, n)}{lab(str(n))}</div>' for n in (16, 20, 24, 28, 32, 48)) + "</div>"
    return f'<div class="lg-st"><div>{lab("<code>" + ("invlogis-symbol.svg" if m == "light" else "invlogis-symbol-reverse.svg") + "</code> · nét mảnh")}{row(s)}</div><div>{lab("Bản favicon · thân dày, khớp lưới điểm ảnh")}{row(f)}</div></div>'


def p_clear(m, p):
    def box(h, x, note):
        pad = round(h * .52 * x, 1)
        return f'<div><span class="lg-clear" style="--pad:{pad}px"><span>{word(h, "Logo Invlogis")}</span></span>{lab(f"cao {h} · {note} = {str(pad).replace(chr(46), chr(44))}px")}</div>'
    sizes = '<div class="lg-r">' + "".join(f'<div>{word(n)}{lab(str(n) + (" · dưới tối thiểu" if n < 20 else " · tối thiểu" if n == 20 else ""))}</div>' for n in (16, 20, 24, 28, 40)) + "</div>"
    return f'<div class="lg-st"><div class="lg-r">{box(24, 1, "1 x")}{box(24, .5, "0,5 x, thanh chật")}</div>{sizes}</div>'


def p_ladder(m, p):
    r = [(24, "<code>size/3xl</code> · app, đầu menu", delta(24)), (28, "đang ghi ở Sidebar · không có bậc <code>size/*</code>", delta(28)), (40, "<code>size/5xl</code> · đăng nhập", delta(40)), (64, "<code>size/7xl</code> · splash", delta(64))]
    return '<div class="lg-r">' + "".join(f'<div>{x}{lab(f"{n}px · {t}")}</div>' for n, t, x in r) + "</div>"


def p_comp(m, p):
    return ('<div class="lg-c2">'
            f'<div class="lg-cell"><span class="type-label">Logo</span><div class="lg-rc" style="margin-top:8px">{word(24)}{fav(24)}</div>{lab("Type = Wordmark, Symbol, Stacked, By innvie · Theme theo chế độ, không còn trục chọn tay")}</div>'
            f'<div class="lg-cell"><span class="type-label">Tenant logo</span><div class="lg-rc" style="margin-top:8px">{delta(24)}{tile("D", 24)}</div>{lab("Type = Image, Square, Initial · Size theo vị trí · nền Tối đọc tham số khách")}</div></div>')


def p_surfaces(m, p):
    mini = lambda head, body, cap: f'<div><div class="lg-mini"><div class="hd">{head}</div><div class="bd">{body}</div></div>{lab(cap)}</div>'
    sk = '<span class="lg-sk" style="width:70%"></span><span class="lg-sk" style="width:45%"></span>'
    return ('<div class="lg-c22">' + mini(delta(24), sk, "Đầu menu web") + mini(delta(24), sk, "Màn chủ app")
            + mini(delta(40), '<span class="tp-btn wide"><span class="type-label">Đăng nhập</span></span>', "Đăng nhập")
            + mini(delta(24) + '<span style="flex:1"></span><span class="type-caption tp-sub" style="white-space:nowrap">LVT-0412</span>', sk, "Chứng từ in, email · đề xuất mới") + "</div>")


def p_dark(m, p):
    cell = lambda x, c: f'<div class="lg-cell" style="min-height:72px">{x}{lab(c)}</div>'
    a = cell(delta(24, "raw"), f"Tệp thật, đặt thẳng · {rs(DELTA_INK, BG_DARK if m == 'dark' else BG_LIGHT)}")
    b = cell(f'<span class="lg-plate">{delta(24, "raw")}</span>', "Ô trắng cố định")
    c = cell(f'<span class="lg-delta lg-whitesim" role="img" aria-label="Logo Delta bản nền tối" style="height:24px;width:{round(24 * DW / DH)}px"></span>' if m == "dark" else delta(24, "raw"), "Bản nền tối riêng: delta-reverse.svg" if m == "dark" else "Sáng vẫn dùng tệp chính")
    return f'<div class="lg-c2">{a}{b}{c}</div>'


def p_tile(m, p):
    cell = lambda x, c: f'<div class="lg-cell">{x}{lab(c)}</div>'
    return ('<div class="lg-c2">'
            + cell(tile("D", 24), f"Chữ cái trên ô: trắng {rs('#FFFFFF', DELTA_TILE)}")
            + cell(f'<span style="display:inline-flex;padding:6px 8px;border-radius:var(--radius-control);background:{DELTA_TILE}">{delta(24, "raw")}</span>', f"Logo chữ trên ô: chữ {rs(DELTA_INK, DELTA_TILE)}, ô xanh nuốt mảng xanh trong logo")
            + cell(delta(24), "Logo chữ đặt thẳng, ô màu không dùng") + "</div>")


def p_invl(m, p):
    k_inn, k_w, k_by = ("innvie", "primary", "by") if m == "light" else ("innvie-rev", "reverse", "by-rev")
    cell = lambda x, c: f'<div class="lg-cell"><div class="lg-rc" style="justify-content:center;min-height:84px;gap:6px"><span class="type-caption tp-sub">{x[0]}</span>{x[1]}</div>{lab(c)}</div>'
    return ('<div class="lg-c2">'
            + cell(("Vận hành trên", use(k_w, 20, "Logo Invlogis")), "Đề xuất: logo chữ cao 20, đúng tối thiểu")
            + cell(("Được phát triển bởi", use(k_inn, 26, "Logo innvie")), "DEC-037 đang ghi: innvie cao 26")
            + cell(("Vận hành trên", use(k_by, 48, "Invlogis by innvie")), "Lockup cỡ tối thiểu 48 (bản nháp ghi 72)") + "</div>")


def p_fav(m, p):
    tabbg, fg = (("#F1F3F4", "#202124") if m == "light" else ("#202124", "#E8EAED"))
    k = "fav" if m == "light" else "fav-rev"
    tab = lambda ic, t: f'<span class="lg-tab" style="background:{tabbg};color:{fg}">{ic}<span>{t}</span></span>'
    png = '<div class="lg-rc">' + "".join(f'<div>{PX(n)}{lab(str(n))}</div>' for n in (16, 32, 48)) + "</div>"
    return f'<div class="lg-st"><div class="lg-rc">{tab(PX(16), "Delta · Lệnh vận tải")}{tab(use(k, 16), "Bản SVG")}</div>{png}</div>'


def p_icon(m, p):
    tenant = tile("D", 60)
    return (f'<div class="lg-rc"><div><div class="lg-ico" role="img" aria-label="Icon app Invlogis"></div>{lab("iOS 180")}</div>'
            f'<div><div class="lg-and" style="border-radius:50%" role="img" aria-label="Icon Android mặt nạ tròn"><i></i></div>{lab("Android tròn")}</div>'
            f'<div><div class="lg-and" style="border-radius:16px" role="img" aria-label="Icon Android mặt nạ vuông bo"><i></i></div>{lab("Android vuông bo")}</div>'
            f'<div>{tenant}{lab("Icon theo khách: chữ cái, chưa có bản vẽ")}</div></div>')


def p_splash(m, p):
    foot = f'<div class="lg-foot"><span class="type-caption">Vận hành trên</span>{word(20)}</div>'
    a = f'<div class="lg-fr"><div class="lg-spl">{delta(64)}{foot}</div></div>'
    return f'<div class="lg-hscroll">{a}{lab("Splash theo chế độ · Delta cao 64 (nền Tối: delta-reverse.svg)")}</div>'


def p_splash2(m, p):
    fall = f'<div class="lg-fr"><div class="lg-spl" style="background:var(--white)"><span class="lg-delta" role="img" aria-label="Logo Delta" style="height:64px;width:{round(64 * DW / DH)}px"></span></div></div>'
    prod = f'<div class="lg-fr"><div class="lg-spl">{use("stacked" if m == "light" else "reverse", 96 if m == "light" else 40, "Logo Invlogis")}</div></div>'
    return f'<div class="lg-hscroll">{fall if m == "dark" else prod}{lab("Khách chưa nộp bản nền tối: giữ nền trắng" if m == "dark" else "Chưa biết khách: logo xếp dọc Invlogis")}</div>'


def p_app(m, p):
    home = (f'<div class="lg-fr"><div class="lg-bar">{delta(24)}<span style="flex:1"></span><span class="tp-fg2">{kit.icon("bell", "tp-ic-lg")}</span></div><div class="tp-pad"><div class="type-title-2">Chào anh Hoà</div>'
            '<div class="tp-card"><div class="tp-top"><span class="type-code tp-sub">LVT-2026-0412</span><span class="tp-chip tp-b">Đang chạy</span></div><div class="type-title-3">Cát Lái → KCN Long Hậu</div><div class="type-body tp-sub">51C-482.15 · mooc 51R-091.44</div></div></div></div>')
    return f'<div class="lg-hscroll">{home}{lab("Màn chủ · logo cao 24 (nền Tối: delta-reverse.svg). Màn con giữ tiêu đề + nút quay lại, không logo")}</div>'


def p_side(m, p):
    nav = lambda ic, x, on="": f'<div class="tp-nav {on}">{kit.icon(ic)}<span class="type-label">{x}</span></div>'
    items = nav("truck", "Lệnh vận tải", "on") + nav("container", "Phương tiện")
    full = f'<div class="lg-side"><div class="lg-head">{delta(24)}</div><div class="type-caption tp-sub lg-trunc" style="margin-bottom:8px">Chi nhánh Cát Lái</div>{items}</div>'
    none = (f'<div class="lg-side"><div class="lg-head">{tile("M", 24, "#262626")}<div class="nm"><span class="type-heading lg-trunc">Công ty CP Vận tải Biển Minh Long Sài Gòn</span>'
            f'<span class="type-caption tp-sub lg-trunc">Chi nhánh Hiệp Phước</span></div></div>{items}</div>')
    ic = lambda c: f'<div class="tp-nav {"on" if c == "truck" else ""}">{kit.icon(c)}</div>'
    slim = f'<div class="lg-side slim"><div class="lg-head" style="justify-content:center">{tile("D", 24)}</div>{ic("truck")}{ic("container")}</div>'
    return f'<div class="lg-hscroll"><div class="lg-rc" style="align-items:flex-start;flex-wrap:nowrap;width:max-content"><div>{full}{lab("Logo chữ, tắt tên đơn vị")}</div><div>{slim}{lab("Thu gọn")}</div></div></div><div style="margin-top:10px">{none}{lab("Chưa có logo: chữ cái + tên, dài thì cắt …")}</div>'


def p_swatch(m, p):
    pal = [("ink", "#0E1442"), ("night", "#0B1033"), ("navy", "#17206F"), ("cobalt", "#2F43DB"), ("peri", "#97A6FF"), ("peri_light", "#C4CDFF"), ("smoke", "#E6EAF8"), ("paper", "#FAF8F4"), ("slate", "#4A5380"), ("white", "#FFFFFF"), ("violet", "#7B55FF"), ("pink", "#E24C9A"), ("coral", "#FF7A59"), ("peach", "#FFD3C0"), ("amber", "#FFB547"), ("innvie", "#0036B5")]
    return '<div class="lg-sw">' + "".join(f'<div style="background:{h};color:{"#fff" if ratio(h, "#FFFFFF") > 4.5 else "#171717"}">{n}<br>{h}</div>' for n, h in pal) + "</div>"


DEMO_LOGO = use("fav", 24, "Ký hiệu Invlogis", "lg-l") + use("fav-rev", 24, "Ký hiệu Invlogis", "lg-d")
SPL = dict(modes=("light", "dark"))

SPEC = dict(
    slug="logo", short="phần Logo",
    title="Foundations · Logo — khách thay ở đâu, cỡ nào?",
    subtitle="Đối chiếu Untitled UI v8 · chọn từng mục · 01/11/2026",
    lead=(f"Trang giúp chốt <b>logo Invlogis và logo khách</b> đi vào sản phẩm thế nào. Bộ nhận diện đã duyệt (DEC-074), phần còn hở nằm ở <mark>logo khách trên nền Tối</mark>: "
          f"chữ Delta chỉ đạt <b>{rs(DELTA_INK, BG_DARK)}</b>, nhìn như biến mất. Logo cũng chưa có <mark>file spec component</mark> và chưa có mã trong bảng trạng thái foundations. <mark>Chưa sửa token nào</mark>."),
    kpis=[(f"{CNT[OK] + CNT[DIFF]}/{len(CMP)}", "dòng Untitled đã có bản tương ứng", "ok"), (str(CNT[GAP]), "chỗ mình thiếu so với Untitled", "bad"),
          (str(CNT[OWN]), "thứ chỉ mình có", ""), (str(SVG_COUNT), "file SVG trong bộ logo", ""), (rs(DELTA_INK, BG_DARK), "chữ Delta trên nền Tối", "bad"), ("0", "file spec component Logo", "bad")],
    screens=dict(
        intro=("Bấm <b>Bộ giá trị</b> để đổi cỡ logo ở đầu menu web: <b>Hiện tại</b> 28 là số bảng Sidebar đang ghi; <b>Sau khi đổi</b> 24 là <code>size/3xl</code>, bằng <code>h-6</code> của Untitled (lg05). "
               "Logo ở menu là <b>file thật</b> trong <code>design/brand/invlogis/logo/</code>, tự đổi bản đảo khi sang Tối; "
               "logo khách trên từng vị trí xem ở lg13, lg14. Màn app trong màn mẫu không có logo, đúng đề xuất lg13 cho màn con."),
        proposal_css=".tp-f.tp-prop[data-platform=web]{--d-logo:var(--size-3xl)}"),
    tag_kind=None,
    sections=[
        dict(title="Bảng đối chiếu Logos — Untitled ↔ mình",
             intro=(f"{SUMMARY} Nguồn Untitled: <code>design/_ref/untitled-ui/06-icons.md</code> mục 7, <code>00-structure.md</code>, code <code>react/components/foundations/logo</code>. "
                    "Ref ghi rõ \"Logo: chỉ ghi cấu trúc\", nên dòng ghi <b>ref không ghi</b> nghĩa là chưa có nguồn, chưa kết luận Untitled không có."),
             html=SPRITE + CMP_HTML),
        dict(title="Đã chốt, không mở lại",
             intro="DEC đang hiệu lực liên quan tới logo. DEC-037 và phần tên, trục của DEC-261 được mở lại có lý do ở lg10, lg06.",
             html=kit.rows(["Mã", "Đã chốt"], [
                 ["DEC-055", "Invlogis là thương hiệu chính; innvie là pháp nhân, chỉ là chữ ký nhỏ."],
                 ["DEC-073", "Chữ v trong logo dùng gradient nhẹ theo từng nền."],
                 ["DEC-074", "Duyệt bộ logo và icon app phương án B."],
                 ["DEC-078", "File Figma \"[innvie] Invlogis Brand\" là bản thiết kế nguồn của bộ nhận diện."],
                 ["DEC-043", f"Màu ô logo Delta là {DELTA_TILE}."],
                 ["DEC-066", "Nhận diện mới chỉ vào điểm chạm sản phẩm; phần màu nhấn đã thay bởi DEC-167."],
                 ["DEC-167", "Màu khách áp kiểu chạm nhẹ, nút chính giữ than chì."],
                 ["DEC-261", "Collection <code>9. Brand · Invlogis</code> không dùng trong component sản phẩm."],
                 ["DEC-039", "Menu bung rộng 240, thu gọn 64."],
                 ["DEC-288", "App sau này có 4 tab."],
                 ["DEC-316", "Nền Tối #191919."],
             ])),
        dict(title="Bộ logo đang có",
             intro="SVG thật từ <code>design/brand/invlogis/logo/</code>, đặt đúng nền theo <code>logo-spec.md</code> Mục 3. Gồm logo sản phẩm Invlogis và logo pháp nhân innvie: Invlogis luôn đứng trước, innvie chỉ là chữ ký (DEC-055).",
             html=GALLERY),
        dict(title="Tương phản trên đúng nền của DS",
             intro=(f"<code>logo-spec.md</code> Mục 6 đo trên giấy và chàm đêm, <b>chưa đo trên nền sản phẩm</b>. Bảng dưới tính lại trên <code>color/bg/primary</code>. <b>Ngưỡng 3:1 ở đây là mình tự đặt để logo đọc được, không phải yêu cầu WCAG</b>: WCAG miễn tương phản cho logotype (theo trí nhớ, chưa kiểm lại trên bản gốc), dù <code>logo-spec.md</code> Mục 6 có dẫn 1.4.11. "
                    "Bản chính trên Tối rớt, đúng luật đã có: nền tối phải dùng bản <code>reverse</code>. Bản <code>reverse</code> đạt trên #191919. Delta không có bản tương đương."),
             html=CONTRAST),
        dict(title="Logo đứng ở đâu: bản đồ điểm chạm",
             intro="Tầng theo <code>.claude/rules/saas-layer.md</code>. <code>P-logo</code> hiện ghi 4 chỗ: góc menu, đăng nhập, splash app, splash web. Dòng in \"đề xuất\" là phần thêm.",
             html=SURF),
        dict(title="Bộ chung đề xuất (nếu chọn hết theo khuyến nghị)", html=BUNDLE),
    ],
    items=[
        dict(id="lg00", grp="Cấu trúc", title="Có đưa Logo vào bảng trạng thái foundations không?",
             why=("Bảng trong <code>design-system/foundations/README.md</code> có 9 mã; dòng <code>logo.md</code> ghi mã \"—\". Không có mã thì <b>không có lệnh duyệt</b> và không bên nào biết Logo đã chốt chưa. "
                  "<b>4 trang</b> <code>_work</code> nhắc tới logo: <code>sidebar-navigation</code>, <code>sidebar-navigation-r2</code>, <code>header-navigation</code>, <code>error-page</code>. Logo không có biến CSS nên <code>_scripts/ds-deps.py</code> <mark>không dò được</mark> component nào dùng, phải thêm luật như icon (\"có nhắc <code>logo.md</code> thì tính là dùng\")."),
             untitled="Trang <code>Logos</code> nằm trong <code>❖ FOUNDATIONS</code>, ngang hàng Colors, Typography. Kit không có bảng trạng thái.",
             ours="<code>design-system/foundations/logo.md</code> status draft, không mã. <code>FPREFIX</code> trong <code>_scripts/ds-deps.py</code> có 9 mục, không có logo.",
             astryx="<code>design/design.md</code> không có mục Logo riêng, luật rải ở Splash web và Thương hiệu theo khách.",
             pv=kit.panes(p_status, modes=("light",)),
             note="Việc phải làm khi thêm: dòng trong bảng, số mục cho <code>logo.md</code> (bảng trỏ theo \"mục N\", file đang đánh số lại từ 1), <code>FPREFIX</code>, luật dò tên file.",
             opts=[("a", "Thêm mã logo vào bảng, nối dò stale: đổi logo là đánh Sidebar, Header, Error page", True), ("b", "Thêm mã logo chỉ để theo dõi duyệt, không nối dò stale", False), ("c", "Không thêm mã, logo.md chỉ trỏ sang bộ nhận diện như hiện tại", False)]),
        dict(id="lg01", grp="Cấu trúc", title="Trang Logos chia khối thế nào?",
             why="Untitled có 3 khối: logo công ty, logo công ty giả, logo báo chí. Mình đã có <code>Logo</code>, <code>Company logo</code> (DEC-261) và <code>Bank logo</code>, <code>App logo</code> ở khu Master. Nhu cầu thật của mình là <mark>logo khách</mark>, thứ Untitled không có. Khối báo chí chỉ phục vụ marketing website, và DEC-320 cũng không thêm token marketing.",
             untitled="<code>Company logo</code> · <code>Placeholder company logos</code> · <code>Placeholder press logos</code>",
             ours="Figma: <code>Logo</code>, <code>Company logo</code> ở khu Logos; <code>Bank logo</code>, <code>App logo</code> khu Master riêng (<code>.claude/state/figma/ds-v2-snapshot.json</code>).",
             astryx="Component <code>Logo sản phẩm / Invlogis</code>, <code>Logo khách / Delta</code> nằm ở trang Application.",
             pv=kit.panes(p_org, modes=("light", "dark")),
             pv_raw_ok="Ô chữ cái dùng mặc định #262626 của P-mau-logo.",
             opts=[("a", "Ba khối: Logo sản phẩm, Logo khách, trỏ sang đối tác. Bỏ Press logos", True), ("b", "Hai khối, không nhắc đối tác trên trang Logos", False), ("c", "Giữ đủ 3 khối như Untitled, thêm khối Logo khách", False)]),
        dict(id="lg02", grp="Biến thể", title="Biến thể nào được dùng trong sản phẩm?",
             why=(f"Bộ logo có <b>{SVG_COUNT} file SVG</b>, phần lớn cho in ấn, deck, marketing. Người dựng màn thấy đủ cả sẽ dễ chọn nhầm. <code>invlogis-stacked.svg</code> <mark>chưa có bản nền tối</mark>, nên splash Tối phải dùng logo ngang."),
             untitled="Chỉ <code>Logo</code> và <code>Logomark</code>, đổi chế độ bằng <code>fill-fg-primary</code>.",
             ours="<code>design/brand/invlogis/logo/logo-spec.md</code> Mục 3 ghi từng file dùng khi nào; set Figma <code>Logo</code> trục Type × Theme.",
             astryx="Chỉ logo chữ và ô logo, <code>design/design.md</code> Menu trái.",
             pv=kit.panes(p_variants),
             note="<code>logo-spec.md</code> Mục 5 cấm: \"Đặt hai chữ i lụa cạnh nhau\". Component Logo không cho ghép ký hiệu cạnh logo chữ.",
             opts=[("a", "Sản phẩm dùng 4 biến thể: chính/đảo, ký hiệu bản nhỏ, xếp dọc, by innvie. Còn lại ở bộ nhận diện", True), ("b", "Chỉ 2 biến thể: chính/đảo và ký hiệu; splash dùng logo ngang", False), ("c", "Đưa đủ 15 file vào component Logo", False)]),
        dict(id="lg03", grp="Biến thể", title="Ký hiệu cỡ nhỏ dùng bản nào?",
             why=("<code>logo-spec.md</code> Mục 2 ghi: \"Ký hiệu <code>invlogis-symbol.svg</code> cao ≥ 48px / 8 mm. Nhỏ hơn thì dùng bản favicon (thân dày hơn, vẽ khớp lưới điểm ảnh).\" "
                  "Trong sản phẩm mọi vị trí ký hiệu đều <mark>dưới 48</mark>. Bản favicon hiện chỉ là file tab trình duyệt, <b>chưa có tên</b> trong DS, và file có <code>&lt;style&gt;</code> theo chế độ hệ điều hành chứ không theo chế độ của app."),
             untitled="Một bản <code>UntitledLogoMinimal</code>, <code>size-8</code> mặc định, <code>size-6</code> ở thanh Slim.",
             ours="<code>invlogis-symbol.svg</code> và <code>favicon.svg</code>. Bản sau chưa có file tách riêng sáng, tối.",
             astryx="Chữ cái trên ô 30, không có ký hiệu.",
             pv=kit.panes(p_small),
             opts=[("a", "Dưới 48 dùng bản favicon; tách 2 file sáng, tối theo chế độ app", True), ("b", "Dùng bản favicon nguyên file, tự đổi theo hệ điều hành", False), ("c", "Dùng ký hiệu thường ở mọi cỡ, chấp nhận nét mảnh", False)]),
        dict(id="lg04", grp="Cỡ", title="Cỡ tối thiểu và vùng trống áp vào DS thế nào?",
             why=(f"<code>logo-spec.md</code> Mục 2: logo chữ cao ≥ 20px, vùng trống 1 x, \"thanh điều hướng chật thì tối thiểu 0,5 x\"; 1 x ≈ 0,52 chiều cao logo. Ở đầu menu cao 24: 1 x = 12,5px, 0,5 x = 6,2px. "
                  "Bảng Sidebar đặt khoảng 8 giữa logo và nút thu gọn, <mark>đạt 0,5 x</mark>. Luật này hiện chỉ áp cho Invlogis; logo khách chưa có ràng buộc nào."),
             untitled="Ref không ghi vùng trống, cỡ tối thiểu; nguồn <code>06-icons.md</code> mục 7.",
             ours="<code>logo-spec.md</code>: cao ≥ 20, by innvie ≥ 48, có khẩu hiệu ≥ 64.",
             astryx="Ô logo 30, đệm 12, không ghi vùng trống.",
             pv=kit.panes(p_clear),
             opts=[("a", "Giữ số của bộ nhận diện; áp cả cho logo khách: cao ≥ 20, trống 0,5 x trong thanh điều hướng", True), ("b", "Chỉ áp cho Invlogis, logo khách tự do", False), ("c", "Luôn đòi 1 x, kể cả thanh điều hướng: đầu menu rộng thêm 6px mỗi phía", False)]),
        dict(id="lg05", grp="Cỡ", title="Có cần token cỡ logo không?",
             why=("Logo xuất hiện ở <b>4 cỡ</b>: app 24, đầu menu 28, đăng nhập 40, splash 72 (<code>design/design.md</code> Splash web). Hai cỡ có sẵn bậc: <code>size/3xl</code> 24, <code>size/5xl</code> 40. "
                  "<mark>28 và 72 không có bậc</mark> <code>size/*</code> (24 rồi 32, 64 rồi 80). Bảng Sidebar đang lấy 28 từ <code>control/height/sm</code>: trùng số nhưng là <b>vai control</b>, control đổi thì logo đổi theo. Thêm token riêng đi ngược hướng gộp của DEC-319. "
                  "Đưa về thang thì đầu menu nhỏ đi 4px, bằng <code>h-6</code> của Untitled, và splash nhỏ đi 8px."),
             untitled="Không có biến cỡ logo, chỉ lớp <code>h-6</code>, <code>h-8</code>, <code>size-6</code> trong code.",
             ours="<code>size/3xl</code>, <code>size/5xl</code>, <code>size/7xl</code> sẵn có (DEC-314). Bảng Sidebar đang gắn <code>control/height/sm</code>.",
             note="Đổi đầu menu về 24 làm Sidebar, Header lệch so với bản đã dựng, nên đây là câu hỏi đổi hình đang có, không tự áp.",
             astryx="Ô logo 30, splash 72, innvie 26: số trần.",
             pv=kit.panes(p_ladder, modes=("light", "dark")),
             tokens=[("logo/height/nav", "28", "Chỉ khi chọn thêm token: đầu menu"), ("logo/height/login", "40", "Chỉ khi chọn thêm token: đăng nhập"), ("logo/height/splash", "72", "Chỉ khi chọn thêm token: splash")],
             opts=[("a", "Không thêm token: trục Size của Logo theo thang size/*, đầu menu 28 thành 24, splash 72 thành 64", True), ("b", "Không thêm token, giữ đầu menu 28 và splash 72 làm ngoại lệ ghi lý do: số riêng của Logo, không gắn token vai khác", False), ("c", "Thêm 3 token logo/height/*, đầu menu giữ 28, splash giữ 72", False)]),
        dict(id="lg06", grp="Component", title="Component Logo trong DS đặt tên và ghi spec thế nào?",
             why=("<b>Mở lại DEC-261:</b> dòng sổ chốt set <code>Logo</code> (Type × Theme) và <code>Company logo</code>; bằng chứng mới là <code>Company avatar</code> nay đã có spec riêng nên hai tên dễ lẫn, và logo khách thật cần trục khác logo mẫu. Sổ Figma có 4 thứ: <code>Logo</code>, <code>Company logo</code>, và 2 bản cũ <code>Logo sản phẩm / Invlogis</code>, <code>Logo khách / Delta</code> ở trang Application. Trong <code>design-system/components/</code> <mark>không có file spec nào</mark>, nên Sidebar và Header tự mô tả logo trong spec của mình. "
                  "Tên <code>Company logo</code> theo Untitled nghĩa là logo mẫu, còn ở mình đây là <b>logo khách thật</b> và dễ lẫn với <code>Company avatar</code>."),
             untitled="<code>UntitledLogo</code>, <code>UntitledLogoMinimal</code> tại <code>react/components/foundations/logo</code>; 9 chỗ điều hướng dùng trực tiếp.",
             ours="Set <code>Logo</code> trục Type × Theme, <code>Company logo</code> (DEC-261). Chưa có spec, chưa có mốc trong <code>design-system/components/_deps.json</code>.",
             astryx="<code>Logo khách / Delta</code>, <code>Logo sản phẩm / Invlogis</code>: gắn cứng tên khách.",
             pv=kit.panes(p_comp),
             pv_raw_ok="Ô chữ cái dùng giá trị Delta của P-mau-logo.",
             note="Tên mới chỉ đổi khi có quyết định ở mục này; lượt review không chạm Figma.",
             opts=[("a", "Hai spec: Logo (Invlogis) và Tenant logo (đổi tên Company logo); xoá 2 bản cũ", True), ("b", "Hai spec, giữ tên Company logo theo Untitled", False), ("c", "Một component Logo gộp cả hai, trục Owner = Invlogis, Khách", False)]),
        dict(id="lg07", grp="Logo khách", title="Logo khách thay Invlogis ở những chỗ nào?",
             why=("Tầng <code>[Lõi] [Cấu hình]</code>: chỗ đặt và cơ chế đúng với mọi doanh nghiệp, tệp logo theo từng khách. <code>P-logo</code> ghi 4 chỗ: góc menu, đăng nhập, splash app, splash web. "
                  "<mark>App, email giao dịch, chứng từ in</mark> chưa được nhắc, trong khi <code>design/brand/invlogis/product/touchpoints.md</code> đặt email theo logo Invlogis. Lệnh vận tải, báo giá gửi ra ngoài là giấy tờ của khách, nên đề xuất theo logo khách."),
             untitled="Không có khái niệm logo theo khách; <code>docs-theming</code> chỉ đổi màu brand.",
             ours="<code>docs/_product/tenant-parameters.md</code> <code>P-logo</code>: tệp + tên hiển thị, mặc định chữ cái đầu trên ô. Delta: <code>design/brand/delta/logo/delta-primary.svg</code> (DEC-325).",
             astryx="Thương hiệu theo khách \"chỉ thay ô logo\": <code>design/design.md</code>.",
             pv=kit.panes(p_surfaces),
             pv_raw_ok="Màu ô là giá trị Delta của P-mau-logo, không phải token.",
             note="Nền Tối trong xem thử dùng <code>delta-reverse.svg</code> (DEC-325), Delta đã đồng ý (BL-351).",
             opts=[("a", "4 chỗ của P-logo + app, email, chứng từ in; ghi lại vào bảng tham số", True), ("b", "4 chỗ + app; email và chứng từ in giữ Invlogis", False), ("c", "Giữ đúng 4 chỗ đang ghi", False)]),
        dict(id="lg08", grp="Logo khách", title="Logo khách trên nền Tối xử lý thế nào?",
             why=(f"Đo từ tệp thật: chữ Delta {DELTA_INK}, trên nền Tối {BG_DARK} đạt <mark>{rs(DELTA_INK, BG_DARK)}</mark>, dưới xa ngưỡng 3:1 mình tự đặt để đọc được. Delta đã có bản riêng <code>delta-reverse.svg</code> (DEC-325), nhưng khách khác có logo chữ đen vẫn gặp đúng chuyện này. Nền Tối là chế độ đã chốt ở DEC-316. "
                  "Tự đảo màu làm mất mảng xanh trong logo và đổi nhận diện của khách, không nên âm thầm làm."),
             untitled="<code>Placeholder company logos</code> có khung <code>Dark background</code>: logo khác màu cho nền tối, mode Dark.",
             ours="<code>P-logo</code> chỉ một tệp. <code>design-system/foundations/logo.md</code> mục 3 chỉ nói màu ô, không nói nền Tối.",
             astryx="Chưa có chế độ Tối; ghi \"Logo nền trắng (jpg): chỉ đặt trên nền trắng\".",
             pv=kit.panes(p_dark),
             note="Tham số đề xuất: <code>P-logo-nen-toi</code>, tệp, tuỳ chọn, tầng <code>[Cấu hình]</code>, Delta: <code>delta-reverse.svg</code>. Thiếu tệp thì hiện ô trắng. Chưa thêm vào bảng tham số.",
             opts=[("a", "Thêm P-logo-nen-toi; khách chưa nộp thì đặt tệp chính trên ô trắng", True), ("b", "Luôn đặt trên ô trắng ở chế độ Tối, không thêm tham số", False), ("c", "Tự đổi logo sang đơn sắc trắng bằng code khi ở chế độ Tối", False)]),
        dict(id="lg09", grp="Logo khách", title="P-mau-logo tô ô khi nào?",
             why=(f"<code>P-mau-logo</code> ghi \"Màu nền ô logo\", Delta {DELTA_TILE} (DEC-043, không mở lại giá trị). <code>design/design.md</code> viết luật với ý chữ trên ô tự đổi trắng hoặc #171717; tệp logo thật không tự đổi được. Với logo chữ thật: chữ đen trên ô xanh chỉ <mark>{rs(DELTA_INK, DELTA_TILE)}</mark>, và mảng xanh trong logo chìm vào ô. "
                  f"Chữ cái trắng trên cùng ô đạt {rs('#FFFFFF', DELTA_TILE)}."),
             untitled="Không có; <code>AvatarCompanyIcon</code> dùng ảnh công ty, không có ô màu.",
             ours="<code>design-system/foundations/color.md</code> mục 3.5: ô logo luôn đúng màu logo khách, không lấy từ dải. Mặc định #262626.",
             astryx="Ô logo 30 màu <code>P-mau-logo</code>, chữ tự chọn trắng hoặc #171717.",
             pv=kit.panes(p_tile),
             pv_raw_ok="Mã màu là giá trị Delta của P-mau-logo, không phải token.",
             opts=[("a", "Ô màu chỉ tô khi hiện chữ cái đầu; có logo thật thì đặt thẳng trên nền", True), ("b", "Luôn tô ô, kể cả có logo chữ", False), ("c", "Bỏ P-mau-logo, ô chữ cái dùng màu color/accent/solid", False)]),
        dict(id="lg10", grp="Logo khách", title="Khi có logo khách, Invlogis xuất hiện ở đâu?",
             why=("<b>Mở lại DEC-037:</b> dòng sổ ghi \"Splash web: logo khách giữa, innvie ở chân\", còn hiệu lực; cột lý do và cột phương án đã bỏ đều \"⚠ chưa ghi\", nên chưa phương án nào từng bị bỏ. Bằng chứng mới: DEC-055 (13/10, sau một ngày) chốt Invlogis là thương hiệu chính, innvie chỉ là chữ ký nhỏ. Phần logo khách ở giữa giữ nguyên. Hiện khách thấy tên pháp nhân mà <mark>không thấy tên sản phẩm</mark>. "
                  "<code>logo-spec.md</code> Mục 4 cũng ghi lockup \"chỉ là đề xuất thay thế, founder duyệt rồi mới đổi\". Bản nháp <code>touchpoints.md</code> đề xuất lockup 72, cạnh logo khách là quá nặng. Tầng <code>[Lõi] [Cấu hình]</code>: cơ chế chung, khách lớn có thể đòi tắt."),
             untitled="Không có; kit một thương hiệu. <code>Company logo</code> không có dạng đồng thương hiệu.",
             ours="DEC-037, <code>design/brand/invlogis/product/touchpoints.md</code> (chờ quyết), <code>invlogis-by-innvie.svg</code>.",
             astryx="Chân splash: \"Được phát triển bởi\" 13px + innvie 26, thẳng chân chữ.",
             pv=kit.panes(p_invl),
             note="Tham số đề xuất: <code>P-hien-van-hanh-tren</code>, bật/tắt, tầng <code>[Cấu hình]</code>, mặc định bật, Delta: chưa chốt. innvie vẫn ở màn Giới thiệu và giấy tờ. Trích <code>logo-spec.md</code> Mục 4: innvie cao không quá 50% logo Invlogis khi đứng riêng.",
             opts=[("a", "Chân đăng nhập, splash: \"Vận hành trên\" + logo chữ Invlogis cao 20, tắt được theo khách; innvie vào màn Giới thiệu", True), ("b", "Giữ DEC-037: \"Được phát triển bởi\" + innvie", False), ("c", "Dùng lockup Invlogis by innvie cao 48 ở chân", False)]),
        dict(id="lg11", grp="Điểm chạm", title="Favicon và icon app theo ai?",
             why=("Icon app đã duyệt phương án B (DEC-074), favicon có đủ SVG + PNG 16/32/48. Câu còn hở: khách có đổi không. Với icon app, câu trả lời <mark>phụ thuộc việc chưa chốt</mark>: <code>docs/_product/saas-core-vs-tenant.md</code> Mục 7 việc 3, \"Một app chung có chọn khách, hay mỗi khách một bản app mang tên riêng\". "
                  "Với favicon: 16px không đủ cho logo chữ của khách, tab đã có tên khách ở tiêu đề. <code>logo-spec.md</code> Mục 5 cấm đặt chữ i nhỏ giữa ô trơn vì dễ đọc thành ⓘ."),
             untitled="Ref không ghi favicon. <code>App icons</code> thuộc Misc icons, ref chưa đọc.",
             ours="<code>design/brand/invlogis/logo/favicon.svg</code>, <code>app-icon-1024.png</code>, <code>android-foreground-432.png</code>.",
             astryx="Chưa có favicon, icon app thương hiệu (<code>touchpoints.md</code>: chưa có / mặc định).",
             pv=kit.panes(p_fav) + '<div style="height:10px"></div>' + kit.panes(p_icon, modes=("light", "dark")),
             pv_raw_ok="Tab trình duyệt dùng màu thật của Chrome (#F1F3F4, #202124) để thử favicon; ô chữ cái dùng giá trị Delta của P-mau-logo.",
             opts=[("a", "Favicon Invlogis cho mọi khách, tiêu đề tab mang tên khách; icon app chờ chốt Mục 7 việc 3", True), ("b", "Favicon theo khách khi khách nộp logo vuông; thiếu thì Invlogis", False), ("c", "Cả favicon và icon app đều theo khách ngay từ đầu", False)]),
        dict(id="lg12", grp="Điểm chạm", title="Splash ở chế độ Tối làm thế nào?",
             why=("<code>design/design.md</code> ghi splash \"nền trắng #FFFFFF\" cố định, chưa tính chế độ Tối. Người dùng đang ở Tối sẽ <mark>bị loé trắng</mark> mỗi lần mở app, nhất là tài xế chạy đêm. Mặt khác Delta chữ đen chỉ đọc được trên nền sáng. "
                  "Hướng dung hoà: theo chế độ khi khách có bản nền tối, chưa có thì giữ trắng. <code>invlogis-stacked.svg</code> được <code>logo-spec.md</code> ghi cho splash nhưng chưa có bản tối, nên Tối dùng logo ngang."),
             untitled="Không có splash trong ref; <code>docs-dark-mode</code> không nói tới logo.",
             ours="Chưa có spec splash trong <code>design-system/components/</code>. <code>design/brand/invlogis/product/splash-mobile-a.html</code> là bản nháp.",
             astryx="Splash web: logo khách giữa cao 72, nền trắng, chuyển động logo làm tín hiệu tải.",
             pv=kit.panes(p_splash) + '<div style="height:10px"></div>' + kit.panes(p_splash2),
             opts=[("a", "Splash theo chế độ; khách chưa có bản nền tối thì giữ nền trắng", True), ("b", "Luôn nền trắng ở mọi chế độ như design.md", False), ("c", "Luôn theo chế độ, khách chưa có bản nền tối thì hiện chữ cái trên ô", False)]),
        dict(id="lg13", grp="Điểm chạm", title="Logo trên màn app 393 đặt ở đâu?",
             why=("App lái xe dùng ngoài trời, chỗ trên đầu màn dành cho việc phải làm. Untitled đặt logo cao 24 ở mọi màn (<code>mobile-header</code>) vì đó là menu chung; DEC-288 chốt app có 4 tab nên không cần lặp logo. <mark>24 đọc được</mark>: Delta rộng 92px, trên khung 393, trừ lề 16 hai bên và icon chuông 24 vẫn còn hơn 240px. Logo khách chưa ghi vị trí app trong <code>P-logo</code>."),
             untitled="<code>mobile-header.tsx</code>: <code>UntitledLogo</code> <code>h-6</code> = 24, trái, cạnh nút mở menu.",
             ours="Màn mẫu dùng tiêu đề, không có logo. Chưa có spec header app; Header navigation chỉ ghi \"logo + hamburger 56\" (<code>design-system/components/_work/header-navigation/page.json</code>).",
             astryx="Chưa có chuẩn đặt logo ở màn M; <code>design/brand/invlogis/product/touchpoints.md</code> ghi Known Gap cho đăng nhập trên app.",
             pv=kit.panes(p_app, platforms=("mobile",)),
             opts=[("a", "Chỉ màn chủ có logo khách cao 24; màn con giữ tiêu đề + quay lại", True), ("b", "Mọi màn đều có logo như Untitled", False), ("c", "App không có logo, chỉ ở đăng nhập và splash", False)]),
        dict(id="lg14", grp="Điểm chạm", title="Logo ở Sidebar web: logo rộng và thanh thu gọn?",
             why=("<code>design-system/components/application/sidebar-navigation.md</code> ghi logo 28 và \"Đầu menu tự xuống dòng khi logo rộng\", <code>Has Tenant Name</code> tắt khi là logo chữ. "
                  f"Menu rộng 240: trừ lề 12 hai bên, nút thu gọn 32 và khoảng 8 còn 176px cho logo. Delta cao 24 rộng {round(24 * DW / DH)}px, cao 28 rộng {round(28 * DW / DH)}px, đều vừa. Còn <mark>thanh thu gọn 64 chỉ còn 44px</mark> bên trong (lề ngang 10): logo chữ không vào được, nên khung thu gọn phải có bản thay thế. Cắt logo chữ thì làm hỏng nhận diện của khách."),
             untitled="<code>sidebar-slim.tsx</code>: <code>UntitledLogoMinimal</code> <code>size-6</code>; các loại sidebar còn lại <code>UntitledLogo</code> <code>h-6</code>.",
             ours="<code>sidebar-navigation.md</code>: logo 28 (<code>control/height/sm</code>) bo <code>radius/control</code>, khoảng 8, thu gọn 64.",
             astryx="Menu trái 240, thu gọn 64 chỉ icon, ô logo 30 + tên đơn vị + module.",
             pv=kit.panes(p_side),
             pv_raw_ok="Ô chữ cái dùng giá trị của P-mau-logo: Delta và mặc định #262626.",
             note="Tham số đề xuất: <code>P-logo-vuong</code>, tệp, tuỳ chọn, tầng <code>[Cấu hình]</code>, Delta: <code>delta-symbol.svg</code>. Thiếu thì dùng chữ cái đầu trên ô. Luật chữ dài theo DEC-261: tên đơn vị một dòng, cắt \"…\".",
             opts=[("a", "Thu gọn dùng logo vuông của khách, thiếu thì chữ cái trên ô; logo rộng quá hạ cao, không dưới 20", True), ("b", "Thu gọn luôn dùng chữ cái trên ô, không thêm tham số", False), ("c", "Thu gọn cắt phần đầu logo chữ", False)]),
        dict(id="lg15", grp="Màu thương hiệu", title="Bảng màu 9. Brand · Invlogis có xuất ra CSS không?",
             why=("Collection <code>9. Brand · Invlogis</code> có <b>16 màu</b> trong <code>design-system/tokens.json</code> (15 Invlogis + 1 innvie), khớp <code>design/brand/invlogis/brand-tokens.json</code> cả 15 dòng; <code>tokens.css</code> có <mark>0 dòng</mark>. Luật DEC-261: \"không dùng trong component sản phẩm\". "
                  "Không có biến CSS thì không ai gắn nhầm. SVG logo mang sẵn mã màu, không cần biến. Gradient logo #A3B0FF cũng khác <code>peri</code> #97A6FF, nên không đổi logo bằng token."),
             untitled="Không có collection riêng; logo đổi bằng <code>fill-fg-primary</code>, brand đổi qua primitive <code>brand</code>.",
             ours="<code>design-system/foundations/logo.md</code> mục 2; bản CSS riêng tiền tố <code>--brand-</code> ở <code>design/brand/invlogis/brand-tokens.css</code>.",
             astryx="Không dùng màu thương hiệu trong sản phẩm, trừ ô logo (<code>design/design.md</code>).",
             pv=kit.panes(p_swatch, modes=("light",)),
             pv_raw_ok="Đây là chính bảng màu thương hiệu, không có biến CSS nên hiện mã màu thật.",
             opts=[("a", "Giữ như hiện tại: Figma + tokens.json, không xuất vào tokens.css", True), ("b", "Xuất vào tokens.css để trang giới thiệu dùng chung", False), ("c", "Bỏ collection khỏi DS, chỉ còn ở brand-tokens.json", False)]),
    ],
    final=("Khi bạn chốt: mình cập nhật <code>tokens.json</code> → sinh <code>tokens.css</code> + handoff → sửa <code>design-system/foundations/logo.md</code> → cập nhật biến Figma cùng lượt → ghi DEC; rồi đặt <b>logo = approved</b> (<code>ds-foundation-status.py set logo approved</code>). Component đang có bị đánh stale và sync dần (rule ds-stale). "
           "<mark>Chọn hết theo khuyến nghị thì không đổi token nào</mark>: <code>tokens.json</code>, <code>tokens.css</code>, biến Figma giữ nguyên; chỉ đổi khi chọn lg05 c hoặc lg15 b. "
           "<mark>Logo chưa có mã trong bảng trạng thái foundations</mark>, nên lệnh trên chỉ chạy được khi <b>lg00</b> chọn thêm mã; chọn không thêm thì chỉ ghi trạng thái ở đầu file <code>logo.md</code> và không có gì tự đánh stale. "
           "Thêm tham số đã chọn vào <code>docs/_product/tenant-parameters.md</code>."),
    css=CSS, js="",
)
