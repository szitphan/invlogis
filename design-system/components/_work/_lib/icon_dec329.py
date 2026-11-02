"""Áp DEC-329 (trang review Icon) lên một page dict của _work: một bộ cỡ icon web và app, nét theo cỡ, màu icon phụ.

build.py gọi apply(page) ngay trước khi ghi page.json, nên chạy lại build vẫn ra cùng kết quả. Cờ page["iconDec329"]
giữ để không áp hai lần: các phép đổi cỡ trên app không chạy lặp được (20 → 16 rồi 16 → 14).
Không đụng snaps, reviews, cmtChanges (bản ghi lịch sử) và cột so sánh untitled, astryx (bản của nơi khác).
"""
import re

SKIP = {"snaps", "reviews", "cmtChanges", "untitled", "astryx"}
# app: sm 16 → 14, md 20 → 16, lg 24 → 20; cỡ lẻ 22 về bậc gần nhất 20
APP = {24: 20, 22: 20, 20: 16, 16: 14}
# khối cỡ cố định, không theo icon/size/*: Featured icon, ảnh nhỏ, Avatar, hình minh hoạ, thẻ tải lên
FIXED_PARENT = re.compile(r"(?:^|\s)(fi|fr|ph|th|fa|fup|fadd|av|pei|ep-feat|ep-ill\w*|ep-illo)(?:\s|$)")
# icon trang trí, disabled giữ quaternary: dấu ngăn, chấm ngăn, tay nắm, khoá ô chỉ đọc, rãnh công tắc
KEEP_QUATERNARY = re.compile(r"\.sep\b|\.sl\b|\.ep-dot\b|\.rz\b|\.lk\b|\[data-D1=c\]|dis|:disabled")
TOK = {"sm": "14px", "md": "16px", "lg": "20px", "chip": "14px"}
SVG = re.compile(r"<svg\b[^>]*>")


def _stroke(s):
    def one(m):
        tag = m.group(0)
        w = re.search(r'(?<![-\w])width="(\d+(?:\.\d+)?)"', tag)
        sw = re.search(r'\bstroke-width="([\d.]+)"', tag)
        if not (w and sw) or sw.group(1) not in ("2", "2.25", "2.5"):
            return tag
        new = "2.25" if float(w.group(1)) <= 16 else "2"
        return tag[:sw.start(1)] + new + tag[sw.end(1):]
    return SVG.sub(one, s)


def _resize(tag, size):
    return re.sub(r'(?<![-\w])(width|height)="\d+(?:\.\d+)?"', lambda m: f'{m.group(1)}="{size}"', tag, count=2)


def _no18(s):
    return SVG.sub(lambda m: _resize(m.group(0), 20) if re.search(r'(?<![-\w])width="18"', m.group(0)) else m.group(0), s)


def _app(s):
    """Thu cỡ icon trên màn app. Chạy TRƯỚC _no18 để 18 → 20 không bị thu tiếp thành 16."""
    out, pos = [], 0
    for m in SVG.finditer(s):
        tag = m.group(0)
        w = re.search(r'(?<![-\w])width="(\d+)"', tag)
        if w and int(w.group(1)) in APP:
            parent = re.search(r'<[a-z0-9]+\b[^<>]*>\s*$', s[max(0, m.start() - 200):m.start()])
            cls = re.search(r'class="([^"]*)"', parent.group(0)) if parent else None
            if not (cls and FIXED_PARENT.search(cls.group(1))):
                out += [s[pos:m.start()], _resize(tag, APP[int(w.group(1))])]
                pos = m.end()
    return "".join(out) + s[pos:]


def _tokens(s):
    if "--icon-size-sm" not in s:
        return s
    s = re.sub(r"--icon-size-(xs|ml):\s*[^;]+;\s*", "", s)
    s = re.sub(r"--featured-icon-size-(md|compact|xl):\s*[^;]+;\s*", "", s)
    for k, v in TOK.items():
        s = re.sub(rf"--icon-size-{k}:\s*[^;]+;", f"--icon-size-{k}: {v};", s)
    s = re.sub(r"(--icon-size-sm: 14px;)", r"--icon-size-xs: 12px; \1", s)
    return re.sub(r"(--featured-icon-size:\s*[^;]+;)", r"\1 --featured-icon-size-md: 40px; --featured-icon-size-compact: 36px; --featured-icon-size-xl: 56px;", s)


def _quaternary(s):
    if "var(--color-fg-quaternary)" not in s:
        return s

    def one(m):
        if KEEP_QUATERNARY.search(m.group(1)):
            return m.group(0)
        return m.group(1) + "{" + m.group(2).replace("var(--color-fg-quaternary)", "var(--color-fg-tertiary)") + "}"
    return re.sub(r"([^{}<>]{1,200})\{([^{}]*var\(--color-fg-quaternary\)[^{}]*)\}", one, s)


def _text(s):
    s = _tokens(s)
    s = _quaternary(s)
    s = s.replace("var(--icon-size-ml)", "var(--icon-size-lg)").replace("icon/size/ml", "icon/size/lg")
    s = s.replace(".mf .hi svg{width:20px;height:20px}", ".mf .hi svg{width:16px;height:16px}")
    if "<svg" in s:
        s = _stroke(_no18(s))
    return s


def _walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in SKIP:
                continue
            if isinstance(v, str):
                o[k] = _text(v)
            else:
                _walk(v)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str):
                o[i] = _text(v)
            else:
                _walk(v)


def _app_scope(page):
    for sc in page.get("screens") or []:
        if sc.get("device") in ("mobile", "app") and isinstance(sc.get("html"), str):
            sc["html"] = _app(sc["html"])
    pv = page.get("preview")
    for b in (pv.get("blocks") or []) if isinstance(pv, dict) else []:
        if b.get("platform") != "mobile":
            continue
        if isinstance(b.get("html"), str):
            b["html"] = _app(b["html"])
        if isinstance(b.get("frames"), list):
            b["frames"] = [_app(f) if isinstance(f, str) else f for f in b["frames"]]


def apply(page):
    if page.get("iconDec329"):
        return page
    _app_scope(page)
    _walk(page)
    page["iconDec329"] = True
    return page
