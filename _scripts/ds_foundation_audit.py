"""Kiểm foundation kỹ theo 7 nhóm — nạp từ ds-foundation-check.py.

Bộ kiểm chính so từng giá trị đã khai (values) với token. Module này thêm phần nó không thấy:
  Chữ      font-family ngoài bộ font DS · tổ hợp cỡ/dòng không thuộc thang type/* · viết hoa + giãn chữ sai caption-caps
  Icon     cỡ icon ngoài thang 12/14/16/20/24 · nét sai theo cỡ (DEC-329 ic01) · khối icon nhấn mạnh khác Featured 48 / icon 24
  Hiệu ứng blur ngoài backdrop-blur/* (làm mờ nền)
  Lưới     bề rộng khung (width/max-width/min-width) ngoài width/*, breakpoint · lề nội dung khác grid/margin (chỉ khi page.json auditInset: true)
và gắn nhóm cho mọi dòng (group_of) để trang review lọc theo nhóm, báo cáo tách nhóm.
Dòng sinh ra có cat "conflict" (phải chọn: sửa theo luật / đổi luật / ngoại lệ), id ổn định "audit.{nhóm}.{khoá}".
"""
import json
import re
from pathlib import Path

GROUPS = [("typo", "Chữ"), ("color", "Màu"), ("icon", "Icon"), ("effect", "Hiệu ứng"),
          ("spacing", "Khoảng cách & cỡ"), ("radius", "Bo góc"), ("grid", "Lưới & độ rộng")]
GROUP_LABEL = dict(GROUPS)
COLOR = {"color", "fill", "background", "bg", "border-color", "text-color", "icon-color", "stroke"}
TYPO = {"font-size", "line-height", "font-weight", "letter-spacing", "font-family"}
EFFECT = {"shadow", "blur", "backdrop-blur", "opacity", "focus-width", "focus-offset"}
WIDTH = {"width", "max-width", "min-width"}
DS_FONTS = {"cal sans", "inter", "jetbrains mono"}
ICON_SIZES = {12, 14, 16, 20, 24}  # bỏ 18 (DEC-329 ic04)
STROKES = {"2", "2.25"}  # icon.md mục 2 (DEC-329): 2,25 cho cỡ 16 trở xuống, 2 cho cỡ 20, 24


def group_of(prop, part=""):
    p, part = str(prop or ""), str(part or "").lower()
    if p in COLOR:
        return "color"
    if p in TYPO:
        return "typo"
    if "radius" in p:
        return "radius"
    if p in EFFECT:
        return "effect"
    if p in ("icon-size", "stroke-width") or ("icon" in part and p in ("size", "width", "height")):
        return "icon"
    if p in WIDTH:
        return "grid"
    return "spacing"


def _px(v):
    m = re.match(r"^\s*(-?\d*\.?\d+)px\s*$", str(v))
    return float(m.group(1)) if m else None


def _n(x):
    return int(x) if float(x).is_integer() else x


def _slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:40] or "x"


def _row(group, key, part, prop, value, sel, rule, fix=None, note="", css_props=None, count=1):
    return {"id": f"audit.{group}.{key}", "part": part, "prop": prop, "platform": "", "size": "", "state": "",
            "theme": "Light", "value": value, "sel": sel, "cssProps": css_props or [prop], "tpl": None,
            "noOverride": None if sel else "kiểm cả màn, không ghi đè được", "cat": "conflict", "tokens": [],
            "bind": None, "to": None, "visible": True, "suggest": fix["token"] if fix else None,
            "rules": [rule], "note": note, "fix": fix, "group": group, "audit": True, "count": count}


def _text_pairs(d):
    """{(cỡ, cao dòng): tên style} của thang type/* cả Web và Mobile."""
    pv = d["collections"]["Platform"]["vars"]
    prim = d["collections"]["Primitives"]["number"]
    num = lambda x: prim.get(x, x) if isinstance(x, str) else x  # type/*/size trỏ thang font-size/*, line-height/* (DEC-322)
    out = {}
    for name, st in (d.get("textStyles") or {}).items():
        s, lh = pv.get(st.get("size")) or {}, pv.get(st.get("lineHeight")) or {}
        for m in ("Web", "Mobile"):
            a, b = num(s.get(m)), num(lh.get(m))
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                out.setdefault((a, b), f"{name} ({m})")
    return out


def _font_short(v):
    """font: 600 12px/20px Inter → (weight, size, lh, family)."""
    m = re.match(r"^\s*(?:(\d{3}|normal|bold)\s+)?(\d*\.?\d+)px(?:/(\d*\.?\d+)px)?\s+(.+)$", v)
    if not m:
        return None
    return m.group(1), float(m.group(2)), float(m.group(3)) if m.group(3) else None, m.group(4)


_FONT_VARS = None


def _first_family(v):
    """Họ font đầu tiên; var(--font-*) đọc theo design-system/tokens.css (vd --font-body = Inter)."""
    global _FONT_VARS
    v = v.strip()
    m = re.match(r"var\((--[\w-]+)\s*(?:,(.*))?\)$", v)
    if m:
        if _FONT_VARS is None:
            css = (Path(__file__).resolve().parent.parent / "design-system/tokens.css").read_text()
            _FONT_VARS = dict(re.findall(r"(--font-[\w-]+)\s*:\s*([^;]+);", css))
        if m.group(1) in _FONT_VARS:
            v = _FONT_VARS[m.group(1)]
        elif m.group(2):
            v = m.group(2)
    return v.split(",")[0].strip().strip("'\"").lower()


def audit(page, parse_css, tokens_path):
    d = json.loads(Path(tokens_path).read_text())
    pv = d["collections"]["Platform"]["vars"]
    prim = d["collections"]["Primitives"]["number"]
    num = lambda ref: prim.get(ref, ref) if isinstance(ref, str) else ref
    rows = []
    comp = parse_css(page.get("css") or page.get("preview", {}).get("css") or "")
    screen = parse_css(page.get("cssScreen") or "")
    pairs = _text_pairs(d)

    # ---- Chữ ----
    by_sel = {}
    for sel, p, v in comp:
        by_sel.setdefault(sel, {})[p] = v
    fam_bad = {}
    for sel, p, v in comp + screen:
        fam = None
        if p == "font-family":
            fam = _first_family(v)
        elif p == "font":
            f = _font_short(v)
            fam = _first_family(f[3]) if f else None
        if fam and fam not in DS_FONTS and fam not in ("inherit", "var(--f-body)"):
            fam_bad.setdefault(fam, []).append(sel)
    for fam, sl in fam_bad.items():
        rows.append(_row("typo", f"family-{_slug(fam)}", "Font chữ", "font-family", fam, ", ".join(sl[:6]),
                         "font ngoài bộ DS (Cal Sans · Inter · JetBrains Mono, foundations mục 4.1)",
                         {"token": "font/body", "value": "Inter", "css": "'Inter', system-ui, sans-serif"},
                         css_props=["font-family"], count=len(sl)))
    combo_bad = {}
    for sel, decl in by_sel.items():
        size = _px(decl.get("font-size", "")) if "font-size" in decl else None
        lh = _px(decl.get("line-height", "")) if "line-height" in decl else None
        if "font" in decl:
            f = _font_short(decl["font"])
            if f:
                size, lh = size or f[1], lh or f[2]
        if size is None or lh is None:
            continue
        if (size, lh) not in pairs:
            combo_bad.setdefault((size, lh), []).append(sel)
    for (size, lh), sl in combo_bad.items():
        same = sorted([(k, v) for k, v in pairs.items() if k[0] == size], key=lambda x: abs(x[0][1] - lh))
        near = same[0] if same else min(pairs.items(), key=lambda x: (abs(x[0][0] - size), abs(x[0][1] - lh)))
        rows.append(_row("typo", f"combo-{_n(size)}-{_n(lh)}", "Tổ hợp chữ", "line-height", f"{_n(size)}/{_n(lh)}",
                         ", ".join(sl[:6]), f"cỡ {_n(size)} / dòng {_n(lh)} không thuộc thang type/* (foundations mục 4.2)",
                         {"token": near[1], "value": f"{_n(near[0][0])}/{_n(near[0][1])}", "css": f"{_n(near[0][1])}px"},
                         note="cùng cỡ chữ thì sửa cao dòng; khác cỡ thì chọn vai gần nhất", css_props=["line-height"],
                         count=len(sl)))
    for sel, decl in by_sel.items():
        up = decl.get("text-transform") == "uppercase"
        ls = decl.get("letter-spacing")
        if up:
            size = _px(decl.get("font-size", "")) or (_font_short(decl.get("font", "")) or (0, None))[1]
            ok_size = size in (None, 12.0, 13.0)
            ok_ls = ls is not None and re.match(r"^0?\.04em$", ls.strip())
            if not (ok_size and ok_ls):
                rows.append(_row("typo", f"caps-{_slug(sel)}", sel, "letter-spacing", ls or "0", sel,
                                 "chữ viết hoa chỉ theo type/caption-caps: cỡ caption, giãn 4% (0.04em)",
                                 {"token": "type/caption-caps", "value": "0.04em", "css": "0.04em"},
                                 css_props=["letter-spacing"]))
        elif ls and ls.strip() not in ("0", "normal", "0em"):
            rows.append(_row("typo", f"tracking-{_slug(sel)}", sel, "letter-spacing", ls, sel,
                             "giãn chữ chỉ dùng cho type/caption-caps (chữ viết hoa)",
                             {"token": "không giãn", "value": "0", "css": "0"}, css_props=["letter-spacing"]))

    # ---- Icon ----
    html = " ".join(s.get("html") or "" for s in page.get("screens") or [])
    prev = page.get("preview") or {}
    html += " " + json.dumps(prev, ensure_ascii=False).replace('\\"', '"')
    sizes, strokes = {}, {}
    for m in re.finditer(r"<svg\b[^>]*>", html):
        tag = m.group(0)
        w = re.search(r'\swidth="(\d+(?:\.\d+)?)"', tag)
        sw = re.search(r'\bstroke-width="([\d.]+)"', tag)
        if w and float(w.group(1)) not in ICON_SIZES and 'class="i"' in tag:
            sizes[float(w.group(1))] = sizes.get(float(w.group(1)), 0) + 1
        if sw and w and sw.group(1) != ("2.25" if float(w.group(1)) <= 16 else "2") and sw.group(1) in ("2", "2.25", "2.5") and 'fill="none"' in tag:
            strokes[sw.group(1)] = strokes.get(sw.group(1), 0) + 1
        elif sw and sw.group(1) not in STROKES and 'fill="none"' in tag:
            strokes[sw.group(1)] = strokes.get(sw.group(1), 0) + 1
    for w, n in sorted(sizes.items()):
        to = min(ICON_SIZES, key=lambda x: abs(x - w))
        rows.append(_row("icon", f"size-{_n(w)}", f"Icon cỡ {_n(w)} ({n} chỗ)", "icon-size", _n(w),
                         f'svg.i[width="{_n(w)}"]', "cỡ icon ngoài thang 12 · 14 · 16 · 20 · 24 (icon.md mục 3)",
                         {"token": f"icon {to}", "value": to, "css": f"{to}px"}, css_props=["width", "height"], count=n))
    for sw, n in strokes.items():
        rows.append(_row("icon", f"stroke-{_slug(sw)}", f"Nét icon {sw} ({n} chỗ)", "stroke-width", sw,
                         f'svg[stroke-width="{sw}"]', "nét icon sai: 2,25 cho cỡ 16 trở xuống, 2 cho cỡ 20, 24 (icon.md mục 2, DEC-329)",
                         {"token": "nét theo cỡ", "value": 2, "css": "2"}, css_props=["stroke-width"], count=n))
    # khối icon nhấn mạnh: khối vuông = tròn/bo, chỉ chứa một svg → Featured icon 48, icon 24 (icons.md 3.1, DEC-258)
    circ = {}
    for sel, decl in by_sel.items():
        w, h = _px(decl.get("width", "")), _px(decl.get("height", ""))
        r = decl.get("border-radius", "")
        if w and w == h and 28 <= w <= 64 and ("9999" in r or "50%" in r or "999px" in r):
            cls = re.findall(r"\.([\w-]+)", sel.split(",")[0])
            if cls:
                circ[cls[-1]] = (sel, w)
    for cls, (sel, w) in circ.items():
        # bộ chọn có lớp cha (".az .fi") → chỉ xét phần tử nằm trong lớp cha đó, không lấy nhầm ".fi" ở chỗ khác
        anc = re.findall(r"\.([\w-]+)", sel.split(",")[0])[:-1]
        iw = None
        for m in re.finditer(r'class="(?:[^"]*\s)?%s(?:\s[^"]*)?"[^>]*>\s*<svg\b[^>]*?\swidth="(\d+)"' % re.escape(cls), html):
            before = html[max(0, m.start() - 400):m.start()]
            if all(re.search(r'class="(?:[^"]*\s)?%s(?:\s[^"]*)?"' % re.escape(a), before) for a in anc):
                iw = int(m.group(1))
                break
        if iw is not None:
            if w != 48 or iw != 24:
                rows.append(_row("icon", f"featured-{_slug(cls)}", f"Khối icon .{cls} {_n(w)} / icon {iw}", "size",
                                 f"{_n(w)}/{iw}", sel, "icon nhấn mạnh đặt trong Featured icon 48, icon 24 (icons.md mục 3.1, DEC-258)",
                                 {"token": "Featured icon 48", "value": 48, "css": "48px"}, css_props=["width", "height"]))

    # ---- Hiệu ứng ----
    blurs = {num(v["value"]) for v in (d.get("blur") or {}).values()}
    for sel, p, v in comp + screen:
        if p in ("backdrop-filter", "filter"):
            for b in re.findall(r"blur\((\d*\.?\d+)px\)", v):
                if float(b) not in blurs:
                    to = min(blurs, key=lambda x: abs(x - float(b)))
                    rows.append(_row("effect", f"blur-{_slug(sel)}", sel, "backdrop-filter", f"blur({_n(float(b))}px)", sel,
                                     "làm mờ nền ngoài backdrop-blur/sm 8 · md 16 · lg 24 · xl 40 (foundations mục 8.1)",
                                     {"token": "backdrop-blur", "value": to, "css": f"blur({_n(to)}px)"}, css_props=[p]))

    # ---- Lưới & độ rộng ----
    allowed = {}
    for k, v in d["collections"]["Primitives"]["number"].items():
        if k.startswith("width/"):
            allowed.setdefault(float(v), k)
    for k, v in (d.get("breakpoints") or {}).items():
        allowed.setdefault(float(v), f"breakpoint {k}")
    side = {float(num(pv[k][m])) for k in pv if k.startswith(("sidebar/", "nav/width")) for m in ("Web", "Mobile")
            if isinstance(num(pv[k].get(m)), (int, float))}
    # độ rộng khung màn demo (lưới form, bảng mẫu) cũng thuộc khung màn — cùng cờ auditInset (user 29/10: Tooltip .grid2)
    for sel, p, v in (screen if page.get("auditInset") else []):
        if p in ("max-width",):
            x = _px(v)
            if x and x >= 200 and x not in allowed:
                to = min(allowed, key=lambda a: abs(a - x))
                rows.append(_row("grid", f"width-{_slug(sel)}-{_slug(p)}", sel, p, _n(x), sel,
                                 "khung nội dung rộng ngoài width/* · content-max-width · breakpoint (foundations mục 7)",
                                 {"token": allowed[to], "value": _n(to), "css": f"{_n(to)}px"}, css_props=[p]))
    # lề nội dung thuộc khung màn, không thuộc component — chỉ kiểm khi component dựng khung trang
    # (page.json "auditInset": true, vd app shell / page layout). User 29/10: Header nav → ngoài phạm vi.
    inset = num(pv.get("grid/margin", {}).get("Web")) if page.get("auditInset") else None
    for sel, p, v in screen:
        if (re.search(r"(^|[\s.>])(main|\.ct|content)\b", sel) or sel.strip() in (".ct", "main")) and p in ("padding", "padding-left", "padding-right"):
            vals = [_px(x) for x in v.split()]
            xs = vals[1] if p == "padding" and len(vals) >= 2 else vals[0]
            if xs is not None and inset and xs != float(inset):
                rows.append(_row("grid", f"inset-{_slug(sel)}", sel, "padding-x", _n(xs), sel,
                                 f"lề nội dung web phải bằng grid/margin {inset} (DEC-259)",
                                 {"token": "grid/margin", "value": inset,
                                  "css": f"{vals[0] if vals[0] is not None else 0}px {inset}px" if p == "padding" else f"{inset}px"},
                                 css_props=[p]))
    _ = side
    return rows


def summary(rows):
    out = {}
    for g, label in GROUPS:
        sub = [r for r in rows if r.get("group") == g]
        out[g] = {"label": label, "total": len(sub), "ok": sum(1 for r in sub if r["cat"] == "ok"),
                  "open": sum(1 for r in sub if r.get("must") and not r.get("decided")),
                  "audit": sum(1 for r in sub if r.get("audit"))}
    return out
