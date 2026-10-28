#!/usr/bin/env python3
"""DS v2 — sinh bộ bàn giao cho dev (Angular web + Flutter app) vào design/v2/handoff/.

  python3 _scripts/ds-v2-handoff.py           # ghi toàn bộ handoff/
  python3 _scripts/ds-v2-handoff.py --check   # không ghi; exit 1 nếu handoff/ lệch nguồn

Nguồn (sửa ở đây, KHÔNG sửa handoff/):
  design/v2/tokens.json                      token (tên = tên biến Figma)
  design/v2/components/l*/*.md               spec component (dòng meta + bảng Thuộc tính khối Web / Mobile)
  design/v2/components/platform-names.json   tên component bên Angular / Flutter (tay viết)
  design/v2/crosswalk.md                     Control type của BA → mã component
  design/v2/icons.md, design/v2/icons/*.svg  icon

Sinh ra:
  handoff/tokens/*.tokens.json   chuẩn DTCG ($value/$type), 1 file/collection/mode — cho Style Dictionary, Tokens Studio
  handoff/web/tokens.css         bản chép design/v2/tokens.css (sinh bởi ds-v2-tokens.py)
  handoff/web/_tokens.scss       biến SCSS trỏ biến CSS, cho Angular
  handoff/flutter/invlogis_tokens.g.dart   hằng + ThemeExtension cho Flutter
  handoff/components/registry.json         bảng nối: mã ↔ Figma ↔ spec ↔ Angular ↔ Flutter
  handoff/components/{id}.json             thuộc tính từng component theo nền tảng
  handoff/crosswalk.json, handoff/icons.json
Cấu trúc: _workspace/decisions.md DEC-255.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V2 = ROOT / "design/v2"
OUT = V2 / "handoff"
SRC = V2 / "tokens.json"
NAMES = V2 / "components/platform-names.json"
CROSSWALK = V2 / "crosswalk.md"
WEIGHT = {"Regular": 400, "Medium": 500, "Semi Bold": 600, "Bold": 700}
GEN = "GENERATED — không sửa tay. Nguồn: design/v2/ · sinh bởi _scripts/ds-v2-handoff.py"


def slug(s):
    s = s.lower()
    for a, b in (("à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ", "a"), ("è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ", "e"), ("ì|í|ị|ỉ|ĩ", "i"),
                 ("ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ", "o"), ("ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ", "u"), ("ỳ|ý|ỵ|ỷ|ỹ", "y"), ("đ", "d")):
        s = re.sub(a, b, s)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


# ---------- token ----------

def load():
    return json.loads(SRC.read_text(encoding="utf-8"))


def collections(doc):
    c = doc["collections"]
    return {
        "Primitives": {**c["Primitives"]["color"], **c["Primitives"]["number"]},
        "Semantic": c["Semantic"]["color"],
        "Platform": c["Platform"]["vars"],
        "Brand": c["Brand"]["color"],
        "Component": c["Component"]["color"],
    }


def owner(cols, name):
    """Collection chứa token `name` (thứ tự ưu tiên như Figma: tầng thấp trước)."""
    for col in ("Primitives", "Brand", "Semantic", "Component", "Platform"):
        if name in cols[col]:
            return col
    return None


def dtcg_alias(name):
    return "{" + name.replace("/", ".") + "}"


def dtcg_value(cols, raw, kind):
    if isinstance(raw, str) and owner(cols, raw):
        return dtcg_alias(raw)
    if kind == "color":
        return raw
    if isinstance(raw, (int, float)):
        return f"{raw}px"
    return raw


def put(tree, name, node):
    cur = tree
    parts = name.split("/")
    for p in parts[:-1]:
        cur = cur.setdefault(p, {})
        if "$value" in cur:
            raise SystemExit(f"DTCG: '{name}' đè lên token '{p}' (nhóm trùng tên token)")
    cur[parts[-1]] = node


def build_dtcg(doc):
    c = doc["collections"]
    cols = collections(doc)
    files = {}

    def ext(v):
        e = {}
        if v.get("scopes"):
            e["com.figma.scopes"] = v["scopes"]
        refs = {k: v[k] for k in ("hig", "m3", "atlassian") if k in v}
        if refs:
            e["invlogis.refs"] = refs
        return e

    def token(v_raw, kind, meta):
        n = {"$type": kind, "$value": dtcg_value(cols, v_raw, kind)}
        if isinstance(meta, dict) and meta.get("use"):
            n["$description"] = meta["use"]
        if isinstance(meta, dict):
            e = ext(meta)
            if e:
                n["$extensions"] = e
        return n

    prim = {}
    for k, v in c["Primitives"]["color"].items():
        put(prim, k, {"$type": "color", "$value": v})
    for k, v in c["Primitives"]["number"].items():
        put(prim, k, {"$type": "dimension", "$value": f"{v}px"})
    files["primitives"] = prim

    def by_mode(col, key, kind, slugs=None):
        for mode in c[col]["modes"]:
            tree = {}
            for k, v in c[col][key].items():
                raw = v[mode]
                if k == "type/label/style":
                    put(tree, "type/label/weight", {"$type": "fontWeight", "$value": WEIGHT[raw]})
                    continue
                put(tree, k, token(raw, kind, v))
            files[f"{col.lower()}.{(slugs or {}).get(mode, slug(mode))}"] = tree

    by_mode("Semantic", "color", "color")
    by_mode("Platform", "vars", "dimension")
    by_mode("Brand", "color", "color", c["Brand"]["modeSlugs"])
    by_mode("Component", "color", "color", {"Value": "default"})

    ts = {}
    for k, v in doc["textStyles"].items():
        put(ts, k, {"$type": "typography", "$value": {
            "fontFamily": v["family"],
            "fontWeight": "{type.label.weight}" if v.get("styleVar") else WEIGHT[v["style"]],
            "fontSize": dtcg_alias(v["size"]),
            "lineHeight": dtcg_alias(v["lineHeight"]),
            "letterSpacing": f"{v.get('letterSpacingPercent', 0) / 100}em",
        }, **({"$description": v["use"]} if v.get("use") else {}),
            **({"$extensions": {"invlogis.textCase": v["case"]}} if v.get("case") else {})})
    for k, v in doc["effectStyles"].items():
        put(ts, k, {"$type": "shadow", "$value": [
            {"color": s["color"] + f"{round(s['alpha'] * 255):02X}", "offsetX": f"{s['x']}px", "offsetY": f"{s['y']}px",
             "blur": f"{s['blur']}px", "spread": f"{s['spread']}px"} for s in v["shadows"]],
            **({"$description": v["use"]} if v.get("use") else {})})
    for k, v in doc["motion"].items():
        put(ts, f"motion/{k}", {"$type": "duration" if k.startswith("duration") else "cubicBezier",
                                "$value": v if k.startswith("duration") else
                                [float(x) for x in re.findall(r"[\d.]+", v)]})
    for k, v in doc.get("blur", {}).items():
        put(ts, k, {"$type": "dimension", "$value": f"{v['value']}px", "$description": v["use"]})
    files["styles"] = ts

    manifest = {
        "$description": "Chỉ mục bộ token DTCG của DS v2. Mỗi collection Figma = 1 nhóm file, mỗi mode = 1 file. "
                        "Ghép: primitives + styles + 1 file mỗi collection theo mode đang dùng.",
        "generator": GEN,
        "version": doc["version"],
        "collections": {
            "Primitives": ["primitives.tokens.json"],
            **{col: [f"{col.lower()}.{s}.tokens.json" for s in
                     [(c[col].get("modeSlugs") or {}).get(m, "default" if m == "Value" else slug(m)) for m in c[col]["modes"]]]
               for col in ("Semantic", "Platform", "Brand", "Component")},
            "Styles": ["styles.tokens.json"],
        },
        "modes": {col: c[col]["modes"] for col in ("Semantic", "Platform", "Brand", "Component")},
    }
    files["$manifest"] = manifest
    return files


def build_scss(doc):
    cols = collections(doc)
    L = [f"// {GEN}", "// Biến SCSS trỏ biến CSS — giá trị đổi theo data-theme / data-platform / data-brand / data-context.",
         "// Dùng trong Angular: @use 'design/v2/handoff/web/tokens' as t;  → color: t.$color-text-primary;", ""]
    seen = set()
    for col in ("Primitives", "Semantic", "Platform", "Brand", "Component"):
        L.append(f"// {col}")
        for k in cols[col]:
            name = "type-label-weight" if k == "type/label/style" else k.replace("/", "-")
            if name in seen:
                continue
            seen.add(name)
            L.append(f"${name}: var(--{name});")
        L.append("")
    return "\n".join(L)


# ---------- Flutter ----------

DART_RESERVED = {"default", "switch", "class", "new", "is", "in", "do", "if", "for", "var", "final", "const", "null"}


def ident(name, drop=("color/",)):
    for d in drop:
        if name.startswith(d):
            name = name[len(d):]
    parts = [p for p in re.split(r"[/\-_.]", name) if p]
    s = parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])
    if s[0].isdigit():
        s = "v" + s
    if s in DART_RESERVED:
        s += "Value"
    return s


def dart_color(hex_):
    h = hex_.lstrip("#").upper()
    if len(h) == 6:
        h = "FF" + h
    else:
        h = h[6:8] + h[:6]
    return f"Color(0x{h})"


def build_dart(doc):
    c = doc["collections"]
    cols = collections(doc)
    sem, brand, comp = cols["Semantic"], cols["Brand"], cols["Component"]
    P = c["Primitives"]
    L = [f"// {GEN}", "// ignore_for_file: constant_identifier_names, lines_longer_than_80_chars", "",
         "import 'package:flutter/material.dart';", ""]

    # Primitives
    L.append("/// Primitives — giá trị gốc. Màn hình KHÔNG dùng trực tiếp; đi qua [InvColors], [InvSpacing]...")
    L.append("abstract final class InvPrimitives {")
    for k, v in P["color"].items():
        L.append(f"  static const Color {ident(k)} = {dart_color(v)};")
    for k, v in P["number"].items():
        L.append(f"  static const double {ident(k)} = {float(v)};")
    L.append("}")
    L.append("")

    def prim_ref(raw):
        if raw in P["color"]:
            return f"InvPrimitives.{ident(raw)}"
        if isinstance(raw, str) and raw.startswith("#"):
            return dart_color(raw)
        raise SystemExit(f"Dart: không giải được màu '{raw}'")

    def ext_class(cls, fields, doc_line, ctor_body):
        """ThemeExtension có copyWith + lerp. fields: list (tên, kiểu, mô tả)."""
        out = [f"/// {doc_line}", "@immutable", f"class {cls} extends ThemeExtension<{cls}> {{", f"  const {cls}({{"]
        out += [f"    required this.{f},".replace(f"this.{f},", f"this.{f},") for f, _, _ in fields]
        out.append("  });")
        out.append("")
        for f, t, d in fields:
            if d:
                out.append(f"  /// {d}")
            out.append(f"  final {t} {f};")
        out.append("")
        out += ctor_body
        out.append("  @override")
        out.append(f"  {cls} copyWith({{" + ", ".join(f"{t}? {f}" for f, t, _ in fields) + "}) =>")
        out.append(f"      {cls}(" + ", ".join(f"{f}: {f} ?? this.{f}" for f, _, _ in fields) + ");")
        out.append("")
        out.append("  @override")
        out.append(f"  {cls} lerp(covariant ThemeExtension<{cls}>? other, double t) {{")
        out.append(f"    if (other is! {cls}) return this;")
        lerp = []
        for f, t, _ in fields:
            if t == "Color":
                lerp.append(f"{f}: Color.lerp({f}, other.{f}, t)!")
            elif t == "double":
                lerp.append(f"{f}: lerpDouble({f}, other.{f}, t)")
            else:
                lerp.append(f"{f}: t < 0.5 ? {f} : other.{f}")
        out.append(f"    return {cls}(" + ", ".join(lerp) + ");")
        out.append("  }")
        out.append("}")
        out.append("")
        return out

    # Semantic
    fields = [(ident(k), "Color", v.get("use", "")) for k, v in sem.items()]
    body = []
    for mode in c["Semantic"]["modes"]:
        body.append(f"  static const {mode.lower()} = InvColors(")
        body += [f"    {ident(k)}: {prim_ref(v[mode])}," for k, v in sem.items()]
        body.append("  );")
        body.append("")
    L += ext_class("InvColors", fields, f"Semantic — màu theo vai trò, mode {' | '.join(c['Semantic']['modes'])}. "
                   f"{c['Semantic'].get('darkNote', '')}", body)

    # Brand
    fields = [(ident(k), "Color", v.get("use", "")) for k, v in brand.items()]
    body = []
    for mode in c["Brand"]["modes"]:
        body.append(f"  /// {mode} ({c['Brand']['hue'][mode]})")
        body.append(f"  static const {ident(c['Brand']['modeSlugs'][mode])} = InvBrandColors(")
        body += [f"    {ident(k)}: {dart_color(v[mode])}," for k, v in brand.items()]
        body.append("  );")
        body.append("")
    body.append("  static const all = <String, InvBrandColors>{")
    body += [f"    '{s}': {ident(s)}," for s in c["Brand"]["modeSlugs"].values()]
    body.append("  };")
    body.append("")
    L += ext_class("InvBrandColors", fields, "Brand — dải màu theo khách (tenant). Chọn theo slug khách: InvBrandColors.all[slug].", body)

    # Component: tính từ Semantic + Brand lúc chạy (đổi theo sáng/tối và theo khách)
    def resolve_expr(raw, local):
        if raw in sem:
            return f"s.{ident(raw)}"
        if raw in brand:
            return f"b.{ident(raw)}"
        if raw in local:
            return ident(raw)
        return prim_ref(raw)

    def ordered(table, mode):
        done, order = set(), []

        def visit(k):
            if k in done:
                return
            ref = table[k][mode]
            if ref in table:
                visit(ref)
            done.add(k)
            order.append(k)
        for k in table:
            visit(k)
        return order

    fields = [(ident(k), "Color", v.get("use", "")) for k, v in comp.items()]
    body = ["  /// Tính từ Semantic (sáng/tối) + Brand (khách) đang dùng.",
            "  factory InvComponentColors.from(InvColors s, InvBrandColors b) {"]
    for k in ordered(comp, "Value"):
        body.append(f"    final {ident(k)} = {resolve_expr(comp[k]['Value'], comp)};")
    body.append("    return InvComponentColors(" + ", ".join(f"{f}: {f}" for f, _, _ in fields) + ");")
    body.append("  }")
    body.append("")
    L += ext_class("InvComponentColors", fields, "Component — màu theo phần của component (DEC-174).", body)

    # Platform
    pv = cols["Platform"]
    fields = []
    for k, v in pv.items():
        if k == "type/label/style":
            fields.append(("typeLabelWeight", "FontWeight", v.get("use", "")))
        else:
            fields.append((ident(k), "double", v.get("use", "")))
    body = []
    for mode in c["Platform"]["modes"]:
        body.append(f"  static const {mode.lower()} = InvPlatform(")
        for k, v in pv.items():
            raw = v[mode]
            if k == "type/label/style":
                body.append(f"    typeLabelWeight: FontWeight.w{WEIGHT[raw]},")
            elif isinstance(raw, str):
                body.append(f"    {ident(k)}: InvPrimitives.{ident(raw)},")
            else:
                body.append(f"    {ident(k)}: {float(raw)},")
        body.append("  );")
        body.append("")
    L += ext_class("InvPlatform", fields, "Platform — số đo theo nền tảng. App dùng InvPlatform.mobile.", body)

    # Typography
    fam = {"Cal Sans": "CalSans", "Inter": "Inter", "JetBrains Mono": "JetBrainsMono"}
    L.append("/// Kiểu chữ — dựng từ [InvPlatform] để cỡ chữ đúng nền tảng.")
    L.append("abstract final class InvTypography {")
    for k, v in doc["textStyles"].items():
        role = v["size"].split("/")[1]
        w = "p.typeLabelWeight" if v.get("styleVar") else f"FontWeight.w{WEIGHT[v['style']]}"
        ls = v.get("letterSpacingPercent")
        extra = f", letterSpacing: p.{ident(v['size'])} * {ls / 100}" if ls else ""
        L.append(f"  /// {v.get('use', '')}" + (" · viết hoa: dùng .toUpperCase() ở chữ" if v.get("case") == "UPPER" else ""))
        L.append(f"  static TextStyle {ident(k.replace('type/', ''))}(InvPlatform p) => TextStyle(fontFamily: '{fam[v['family']]}', "
                 f"fontWeight: {w}, fontSize: p.{ident(v['size'])}, height: p.{ident(v['lineHeight'])} / p.{ident(v['size'])}{extra});")
    L.append("}")
    L.append("")

    # Elevation, motion
    L.append("/// Đổ bóng (effect style Figma).")
    L.append("abstract final class InvElevation {")
    for k, v in doc["effectStyles"].items():
        shadows = ", ".join(
            f"BoxShadow(color: {dart_color(s['color'] + format(round(s['alpha'] * 255), '02X'))}, offset: Offset({float(s['x'])}, {float(s['y'])}), "
            f"blurRadius: {float(s['blur'])}, spreadRadius: {float(s['spread'])})" for s in v["shadows"])
        L.append(f"  /// {v.get('use', '')}")
        L.append(f"  static const List<BoxShadow> {ident(k)} = [{shadows}];")
    L.append("}")
    L.append("")
    L.append("/// Làm mờ nền (DEC-258): dùng với BackdropFilter(filter: ImageFilter.blur(sigmaX: v, sigmaY: v)).")
    L.append("abstract final class InvBlur {")
    for k, v in doc.get("blur", {}).items():
        L.append(f"  /// {v['use']}")
        L.append(f"  static const double {ident(k)} = {float(v['value'])};")
    L.append("}")
    L.append("")
    L.append("abstract final class InvMotion {")
    for k, v in doc["motion"].items():
        if k.startswith("duration"):
            L.append(f"  static const Duration {ident(k)} = Duration(milliseconds: {int(v.replace('ms', ''))});")
        else:
            a = ", ".join(re.findall(r"[\d.]+", v))
            L.append(f"  static const Curve {ident(k)} = Cubic({a});")
    L.append("}")
    L.append("")

    # Helper
    L += [
        "/// Gắn DS v2 vào ThemeData. Đổi khách: truyền brand khác.",
        "ThemeData invTheme({Brightness brightness = Brightness.light, InvBrandColors brand = InvBrandColors.thanChi}) {",
        "  final s = brightness == Brightness.dark ? InvColors.dark : InvColors.light;",
        "  return ThemeData(",
        "    brightness: brightness,",
        "    fontFamily: 'Inter',",
        "    scaffoldBackgroundColor: s.bgCanvas,",
        "    extensions: [s, brand, InvComponentColors.from(s, brand), InvPlatform.mobile],",
        "  );",
        "}",
        "",
        "extension InvThemeX on BuildContext {",
        "  InvColors get invColors => Theme.of(this).extension<InvColors>()!;",
        "  InvBrandColors get invBrand => Theme.of(this).extension<InvBrandColors>()!;",
        "  InvComponentColors get invComponent => Theme.of(this).extension<InvComponentColors>()!;",
        "  InvPlatform get invPlatform => Theme.of(this).extension<InvPlatform>()!;",
        "}",
        "",
    ]
    text = "\n".join(L)
    # lerpDouble nằm trong dart:ui
    return text.replace("import 'package:flutter/material.dart';", "import 'dart:ui' show lerpDouble;\n\nimport 'package:flutter/material.dart';")


# ---------- component ----------

def md_table(lines, start):
    rows = []
    i = start
    while i < len(lines) and not lines[i].startswith("|"):
        if lines[i].startswith("#"):
            return rows
        i += 1
    head = [h.strip() for h in lines[i].strip("|\n").split("|")]
    i += 2
    while i < len(lines) and lines[i].startswith("|"):
        cells = [x.strip() for x in lines[i].strip().strip("|").split("|")]
        rows.append(dict(zip(head, cells)))
        i += 1
    return rows


def parse_component(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = next(l[2:].strip() for l in lines if l.startswith("# "))
    meta = " ".join(l.lstrip("> ").strip() for l in lines if l.startswith(">"))
    first_meta = meta.split("\n")[0]
    level = re.match(r"(L\d)", first_meta)
    version = re.search(r"phiên bản ([\d.]+)", meta)
    status = re.search(r"phiên bản [\d.]+ · ([^·]+) ·", meta)
    figma = re.findall(r"`(Base / [^`]+)` \((\d+:\d+)", meta)
    doc_frame = re.search(r"khung tài liệu `[^`]+` \((\d+:\d+)", meta)
    decs = sorted(set(re.findall(r"DEC-\d+", meta)), key=lambda x: int(x[4:]))
    fm_status = re.search(r"^status:\s*(\S+)", text, re.M)

    platforms = {}
    section = "Chung"
    for i, l in enumerate(lines):
        if l.startswith("## "):
            h = l[3:].strip()
            section = "web" if h.startswith("Web") else "mobile" if h.startswith("Mobile") else h
        if l.startswith("### Thuộc tính") and section in ("web", "mobile"):
            rows = md_table(lines, i + 1)
            if not rows:
                # Khối Mobile hay ghi "Như web; khác: …" thay cho bảng → kế thừa web, giữ câu khác biệt.
                note = next((x.strip() for x in lines[i + 1:] if x.strip() and not x.startswith("#")), "")
                platforms[section] = {"props": platforms.get("web", {}).get("props", []), "sameAsWeb": True, "note": note}
                continue
            platforms[section] = {"props": [{
                "name": r.get("Thuộc tính", ""), "kind": r.get("Loại", ""),
                "default": r.get("Mặc định", ""),
                "values": [v.strip() for v in re.split(r" · ", r.get("Giá trị", "")) if v.strip()],
            } for r in rows]}
    tokens = sorted(set(re.findall(r"`((?:control|radius|space|type|icon|focus|touch|layout|chip|avatar|tooltip|"
                                    r"list-row|card|field|progress|otp|button|status-chip|tab|nav|color)/[a-z0-9/\-*]+)`", text)))
    name = title
    cid = f"{(level.group(1) if level else 'L1').lower()}.{slug(re.sub(r'^Base / ', '', name))}"
    return {
        "id": cid,
        "name": name,
        "level": level.group(1) if level else None,
        "version": version.group(1) if version else None,
        "status": (status.group(1).strip() if status else None) or (fm_status.group(1) if fm_status else None),
        "spec": str(path.relative_to(ROOT)),
        "figma": {"components": [{"name": n, "nodeId": nid} for n, nid in figma], "docFrame": doc_frame.group(1) if doc_frame else None},
        "decisions": decs,
        "platforms": platforms,
        "tokens": tokens,
    }


def build_components():
    names = json.loads(NAMES.read_text(encoding="utf-8")) if NAMES.exists() else {"components": {}}
    comps = [parse_component(p) for p in sorted(V2.glob("components/l*/*.md"))]
    reg, per = [], {}
    for comp in comps:
        n = names["components"].get(comp["id"], {})
        comp["platforms"].setdefault("web", {}).update({k: v for k, v in n.get("web", {}).items()})
        comp["platforms"].setdefault("mobile", {}).update({k: v for k, v in n.get("mobile", {}).items()})
        per[comp["id"]] = {"$generator": GEN, **comp}
        reg.append({
            "id": comp["id"], "name": comp["name"], "level": comp["level"], "version": comp["version"], "status": comp["status"],
            "figmaNodeId": comp["figma"]["components"][0]["nodeId"] if comp["figma"]["components"] else None,
            "spec": comp["spec"],
            "angular": n.get("web", {}).get("selector"),
            "flutter": n.get("mobile", {}).get("widget"),
            "namesStatus": n.get("status", "chưa đặt"),
        })
    registry = {"$generator": GEN, "$description": "Bảng nối mã component ↔ Figma ↔ spec ↔ Angular ↔ Flutter. "
                "Tên Angular/Flutter tay viết ở design/v2/components/platform-names.json.",
                "prefix": names.get("prefix", {}), "components": reg}
    unknown = sorted(set(names["components"]) - {c["id"] for c in comps})
    return registry, per, unknown


def build_crosswalk(ids):
    if not CROSSWALK.exists():
        return {"rows": []}, []
    lines = CROSSWALK.read_text(encoding="utf-8").splitlines()
    i = next(k for k, l in enumerate(lines) if l.startswith("| Control type"))
    rows = md_table(lines, i)
    out, bad = [], []
    for r in rows:
        cid = r.get("Mã component", "").strip("` ")
        ok = cid in ids
        if cid and cid != "—" and not ok:
            bad.append(cid)
        out.append({"controlType": r.get("Control type (BA)", ""), "when": r.get("Khi nào", ""),
                    "component": cid if ok else None, "gap": None if ok else r.get("Ghi chú", "") or "chưa có trong DS v2"})
    return {"$generator": GEN, "rows": out}, bad


def build_icons():
    text = (V2 / "icons.md").read_text(encoding="utf-8")
    lib = re.search(r"\*\*Lucide\*\*.*?bản \*\*([\d.]+)\*\*", text)
    meanings = []
    part = text.split("## 7.")[1] if "## 7." in text else ""
    for m, icon, rest in re.findall(r"^\| ([^|`]+?) \| `icon/([a-z0-9\-]+)`([^|]*)\|", part, re.M):
        meanings.append({"meaning": m.strip(), "icon": icon, "custom": "tự vẽ" in rest})
    custom = sorted({p.stem.replace("-fill", "") for p in (V2 / "icons").glob("*.svg")})
    return {
        "$generator": GEN,
        "library": {"name": "lucide", "version": lib.group(1) if lib else None,
                    "angular": "lucide-angular", "flutter": "lucide_icons_flutter (tên snake → LucideIcons.camelCase)"},
        "custom": [{"name": n, "svg": f"design/v2/icons/{n}.svg",
                    "svgFill": f"design/v2/icons/{n}-fill.svg" if (V2 / f"icons/{n}-fill.svg").exists() else None} for n in custom],
        "meanings": meanings,
    }


# ---------- main ----------

def render():
    doc = load()
    files = {}
    for name, tree in build_dtcg(doc).items():
        fn = "index.json" if name == "$manifest" else f"{name}.tokens.json"
        files[f"tokens/{fn}"] = json.dumps(tree, ensure_ascii=False, indent=2) + "\n"
    css = V2 / "tokens.css"
    files["web/tokens.css"] = css.read_text(encoding="utf-8")
    files["web/_tokens.scss"] = build_scss(doc)
    files["flutter/invlogis_tokens.g.dart"] = build_dart(doc)
    registry, per, unknown = build_components()
    files["components/registry.json"] = json.dumps(registry, ensure_ascii=False, indent=2) + "\n"
    for cid, data in per.items():
        files[f"components/{cid}.json"] = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    cw, bad = build_crosswalk(set(per))
    files["crosswalk.json"] = json.dumps(cw, ensure_ascii=False, indent=2) + "\n"
    files["icons.json"] = json.dumps(build_icons(), ensure_ascii=False, indent=2) + "\n"
    return files, unknown, bad, registry


def main():
    files, unknown, bad, registry = render()
    warn = []
    if unknown:
        warn.append(f"platform-names.json có mã không có spec: {', '.join(unknown)}")
    if bad:
        warn.append(f"crosswalk.md trỏ mã không có spec: {', '.join(bad)}")
    css_names = {}
    for col, table in collections(load()).items():
        for k in table:
            css_names.setdefault(k.replace("/", "-"), []).append(f"{col} {k}")
    for n, srcs in css_names.items():
        if len(srcs) > 1:
            warn.append(f"trùng tên biến CSS --{n}: {' · '.join(srcs)} (cái sau đè cái trước)")
    names = json.loads(NAMES.read_text(encoding="utf-8"))["components"] if NAMES.exists() else {}
    missing = [c["id"] for c in registry["components"]
               if not c["flutter"] or (not c["angular"] and not names.get(c["id"], {}).get("web", {}).get("note"))]
    if missing:
        warn.append(f"chưa đặt tên Angular/Flutter: {', '.join(missing)}")
    if "--check" in sys.argv:
        stale = [p for p, t in files.items() if not (OUT / p).exists() or (OUT / p).read_text(encoding="utf-8") != t]
        extra = [str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file() and str(p.relative_to(OUT)) not in files
                 and p.name != "README.md"] if OUT.exists() else []
        print(f"handoff/: {'LỆCH ' + str(len(stale)) + ' file' if stale else 'khớp nguồn'}" + (f" · thừa {len(extra)} file" if extra else ""))
        for p in stale[:20]:
            print("  ~", p)
        for w in warn:
            print("  ⚠", w)
        sys.exit(1 if stale or extra or bad else 0)
    if OUT.exists():
        for sub in ("tokens", "web", "flutter", "components"):
            shutil.rmtree(OUT / sub, ignore_errors=True)
    for p, t in files.items():
        f = OUT / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(t, encoding="utf-8")
    print(f"Đã ghi {len(files)} file vào {OUT.relative_to(ROOT)}/ · {len(registry['components'])} component")
    for w in warn:
        print("  ⚠", w)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
