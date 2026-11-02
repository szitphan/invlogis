#!/usr/bin/env python3
"""Token ↔ component DS v2 — mỗi token đang được component nào dùng, token nào lẻ/thừa, component nào tự đặt giá trị
ngoài hệ token. Trang review định kỳ để đưa DS về nhất quán.

  python3 _scripts/ds-token-usage.py            # quét → design-system/_review/token-usage.json + token-usage.html
  python3 _scripts/ds-token-usage.py --summary  # chỉ in số liệu, không ghi file
  python3 _scripts/ds-token-usage.py --check    # gate: exit 1 khi token Component trỏ thẳng Primitive

Nguồn (chỉ đọc): design-system/tokens.css (định nghĩa + tầng theo khối selector), danh sách component của ds-deps.py
(universe: md trong components/{base,application,l1} + _work/<slug>/page.json). Component dùng token khi:
  - css trong page.json gọi var(--x) (bỏ khối token chép nguyên từ tokens.css), hoặc
  - md gọi var(--x) / ghi tên token kiểu `color/bg/secondary`.
Dùng gián tiếp = token nằm trong chuỗi var() của token component dùng (vd tooltip → --tooltip-bg → --color-bg-primary_solid).

Tầng theo 10 collection Figma (tokens.json › figma.collections; architecture.md mục 7, DEC-313):
  primitive  0. Primitives + fonts
  semantic   1. Semantic + 2.–5. Platform (Radius, Spacing & Layout, Typography, Sizes) + text style, shadow, motion, grid…
  brand      7. Brand (component dùng theo vai, foundations mục 3.5)
  component  6. Platform · Component sizes — chỉ được trỏ Semantic hoặc Brand (8. Component màu đã bỏ, DEC-318)
Token có trong tokens.css mà không có trong tokens.json → xếp theo tiền tố tên.

Cờ (mỗi cờ = 1 mục trong tab "Cần xử lý", id ổn định để giữ quyết định qua các lần quét):
  skip       token tầng Component (6.) trỏ thẳng Primitive — vi phạm DEC-313 (gate --check: FAIL)
  compraw    token tầng Component ghi số trần (gom theo giá trị) — chờ chọn token Semantic
  unused     token semantic/component chưa component nào dùng (trực tiếp hay gián tiếp)
  single     token semantic chỉ 1 component dùng → token riêng lẻ, cân nhắc gộp
  prim       css/md của component gọi thẳng primitive màu — trái DEC-115
  alias      component tự đặt biến cục bộ (--fg2, --line…) thay cho token hệ thống
  unknown    component gọi tên token không có trong tokens.css
  literal    màu hex/rgb viết trần trong css component
  dup        2+ token semantic cùng nhóm có giá trị giống hệt ở mọi chế độ (Light/Dark, Web/Mobile)
  stale-name tên màu cũ còn trong md, css, page.json sau DEC-318, DEC-320 (bảng đổi tên: components/_token-ledger.json)
  brandleak  css/md của component gọi --invlogis-*, --innvie-* — trái DEC-261 (gate --check: WARN)
  rawmotion  transition, animation trong page.json ghi số giây trần, không qua --duration-* — trái DEC-333 mt03, lọt luật giảm chuyển động (gate --check: WARN)
  role       cùng một vai (phần tử × thuộc tính × trạng thái) mà dùng 2+ token, hoặc lệch luật có căn cứ trong color.md, DEC-321
Trang có phạm vi Màu (mặc định) và Tất cả: mỗi mục mang cờ color; unused, dup màu có thêm sub (keep/suspect, intent/real) + lý do.
Vai suy từ selector qua bảng _ROLE_SRC; không suy được thì vào danh sách "chưa rõ vai", không kết luận. Chỉ quét HTML, CSS, md.
Quyết định user chọn trên trang nằm ở kho của artifact (collection "decisions", doc = id mục); Claude đọc về rồi áp (L1/L2).
"""
import html
import importlib.util
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TCSS = ROOT / "design-system/tokens.css"
TJSON = ROOT / "design-system/tokens.json"
OUT_J = ROOT / "design-system/_review/token-usage.json"
OUT_H = ROOT / "design-system/_review/token-usage.html"
MARK = re.sub(r"<\?xml[^>]*>", "", (ROOT / "design/brand/innvie-v1/mark-color.svg").read_text())
TODAY = date.today().isoformat()

_spec = importlib.util.spec_from_file_location("dd", ROOT / "_scripts/ds-deps.py")
dd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dd)

PAL = re.compile(r"((neutral|blue|teal|purple|yellow|green|red|orange|charcoal|alpha|dark)-[\w-]+|white|black)$")
PRIM_DIM = re.compile(r"(space-\d+|radius-\d+)$")
GROUPS = [  # (mã, tên, tiền tố) — thứ tự = thứ tự hiển thị; khớp các mục foundations/
    ("color", "Màu", ("color-",)),
    ("type", "Chữ", ("type-", "font-")),
    ("radius", "Bo góc", ("radius-",)),
    ("space", "Khoảng cách, bố cục", ("space-", "layout-")),
    ("grid", "Lưới, độ rộng", ("grid-", "container-", "width-", "bp-")),
    ("elevation", "Lớp nổi, làm mờ", ("shadow-", "backdrop-blur-")),
    ("touch-focus", "Vùng chạm, focus", ("touch-", "focus-")),
    ("motion", "Chuyển động", ("duration-", "ease-")),
    ("icon", "Icon", ("icon-",)),
    ("logo", "Logo, màu thương hiệu", ("invlogis-", "innvie-")),
]
BRAND_ONLY = ("invlogis-", "innvie-")  # 9. Brand · Invlogis: có trong tokens.css cho trang giới thiệu, component không được gọi (DEC-261, DEC-326)
RETIRED = ("card-", "list-row-")  # token đã bỏ (DEC-312), còn chép trong kit dump của trang _work cũ
OTHER = [("shadow-", "effectStyles"), ("backdrop-blur-", "blur"), ("duration-", "motion"), ("easing-", "motion"), ("grid-", "grid"),
         ("bp-", "breakpoints")]
CTXS = [("light", "web"), ("dark", "web"), ("light", "mobile"), ("dark", "mobile")]


# ── tokens.css ──────────────────────────────────────────────────────────────
def parse_tokens():
    toks, sel = {}, None
    for line in TCSS.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        cls = re.match(r"\.(type-[\w-]+)\s*\{(.*)\}", s)
        if cls:  # text style = token nhóm Chữ, tham chiếu size/line-height
            n, body = cls.groups()
            toks[n] = {"defs": [(".class", body)], "refs": set(re.findall(r"var\(--([\w-]+)", body)), "style": True}
            continue
        if s.endswith("{") and not s.startswith("--"):
            sel = s[:-1].strip()
            continue
        if s == "}":
            continue
        m = re.match(r"--([\w-]+)\s*:\s*(.*?);", s)
        if m and sel and not sel.startswith("@media"):
            n, v = m.groups()
            t = toks.setdefault(n, {"defs": [], "refs": set()})
            t["defs"].append((sel, v))
            t["refs"] |= set(re.findall(r"var\(--([\w-]+)", v))
    src = json_index()
    for n, t in toks.items():
        j = src.get(n)
        t["tier"], t["coll"], t["jname"], t["jval"] = (j["tier"], j["coll"], j["name"], j["val"]) if j else (tier(n), "", "", None)
        if not j and not t.get("style"):
            t["coll"] = next((c for pre, c in OTHER if n.startswith(pre)), "tokens.css")
        t["group"] = group(n)
    return toks


def css(name):
    return name.replace("/", "-").replace(".", "-")


def json_index():
    """css name → tầng + collection + tên/giá trị gốc trong tokens.json."""
    d = json.loads(TJSON.read_text())
    C, out = d["collections"], {}

    def put(name, tier_, coll, val):
        out[css(name)] = {"tier": tier_, "coll": coll, "name": name, "val": val}
    FP = d["figma"]["collections"]["Platform"]  # tên collection Figma → tiền tố
    pcoll = lambda k: next((c for c, pre in FP.items() if k.startswith(tuple(pre))), "Platform")
    for kind_ in ("color", "number"):
        for k, v in C["Primitives"].get(kind_, {}).items():
            put(k, "primitive", "0. Primitives", v)
    for k, v in d.get("fonts", {}).items():
        put("font/" + k, "primitive", "fonts", v)
    for k, v in C["Semantic"]["color"].items():
        put(k, "semantic", "1. Semantic", {m: v.get(m) for m in ("Light", "Dark")})
    for k, v in C["Platform"]["vars"].items():
        c = pcoll(k)
        put(k, "component" if c.startswith("6.") else "semantic", c, {m: v.get(m) for m in ("Web", "Mobile")})
    for k, v in C["Brand"]["color"].items():
        put(k, "brand", "7. Brand", v.get("Than chì") if isinstance(v, dict) else v)
    for k, v in C.get("Brand Invlogis", {}).get("color", {}).items():
        put(k, "brand", "9. Brand · Invlogis", v.get("Value"))
    # 8. Component (màu riêng component) đã bỏ — DEC-318: component gắn thẳng token Semantic
    return out


def tier(n):
    if PAL.match(n) or PRIM_DIM.match(n):
        return "primitive"
    if any(n.startswith(p) for _, _, ps in GROUPS for p in ps):
        return "semantic"
    return "component"


def group(n):
    if PAL.match(n):
        return "color"
    for k, _, ps in GROUPS:
        if any(n.startswith(p) for p in ps):
            return k
    return "c:" + n.split("-")[0]


def applies(sel, theme, plat):
    if sel == '[data-theme="dark"]':
        return theme == "dark"
    if sel == '[data-platform="mobile"]':
        return plat == "mobile"
    if sel.startswith("[data-brand"):
        return False  # brand phụ — mặc định Than chì
    return True


def resolve(toks, n, theme, plat, seen=()):
    t = toks.get(n)
    if not t or n in seen:
        return None
    if t.get("style"):
        return "." + n
    val = None
    for sel, v in t["defs"]:
        if applies(sel, theme, plat):
            val = v
    if val is None:
        return None
    return re.sub(r"var\(--([\w-]+)(?:,[^()]*)?\)",
                  lambda m: resolve(toks, m.group(1), theme, plat, seen + (n,)) or m.group(0), val)


def kind(v):
    v = (v or "").strip()
    if v.startswith(".type-"):
        return "style"
    if re.fullmatch(r"#[0-9a-fA-F]{3,8}|rgba?\([^)]*\)|transparent", v):
        return "color"
    if re.fullmatch(r"-?\d+(\.\d+)?px", v):
        return "dim"
    if "px" in v and re.search(r"#|rgba?\(", v):
        return "shadow"
    return "other"


# ── component ───────────────────────────────────────────────────────────────
MOTION_DECL = re.compile(r"(?:transition|animation)(?:-[a-z]+)?\s*:\s*([^;{}\"'<>]+)")
MOTION_TIME = re.compile(r"(?<![\w.-])(?:\d+\.?\d*|\.\d+)(?:ms|s)\b")
MOTION_SKIP = {"snaps", "reviews", "cmtChanges"}  # lịch sử vòng trước, giữ nguyên để so


def raw_motion(page):
    """DEC-333 mt03: số giây trần trong khai báo chuyển động; 0s không tính, biến trong var() không tính."""
    hits = Counter()
    for k, v in page.items():
        if k in MOTION_SKIP:
            continue
        for txt in walk_strings([v]):
            for m in MOTION_DECL.finditer(txt):
                bare = re.sub(r"var\([^()]*\)", "", m.group(1))
                if any(float(t.rstrip("ms")) for t in MOTION_TIME.findall(bare)):
                    hits[m.group(0).strip()] += 1
    return hits


def scan_component(slug, toks):
    names, local, lits, lits_html, bare = set(), {}, Counter(), Counter(), 0
    pj = dd.COMP / "_work" / slug / "page.json"
    if pj.exists():
        p = json.loads(pj.read_text())
        c = p.get("css") or ""
        c = re.sub(r"--([\w-]+)\s*:\s*[^;{}]*;?", lambda m: "" if m.group(1) in toks or m.group(1).startswith(RETIRED) else m.group(0), c)
        # đọc thẳng từng chuỗi; quét trên json.dumps sẽ dính dấu \ của style=\"--p:48\" thành giá trị rác "48\"
        extra = list(walk_strings([p.get(k) for k in ("cssScreen", "preview", "proto")]))
        for txt in [c] + extra:
            for m in re.finditer(r"--([\w-]+)\s*:\s*([^;{}\"'<>]*)", txt):
                if m.group(1) not in toks and not m.group(1).startswith(RETIRED) and m.group(2).strip():  # token đã bỏ chép sẵn trong kit
                    local.setdefault(m.group(1), m.group(2).strip())
        names |= set(re.findall(r"var\(--([\w-]+)", c))
        for txt in walk_strings([p.get(k) for k in ("preview", "proto")]):  # màu gắn inline trong HTML preview cũng là chỗ dùng
            names |= {n for n in re.findall(r"var\(--([\w-]+)", txt) if n.startswith("color-")}
            for st in re.findall(r"style=[\"']([^\"']*)", txt):
                for h in re.findall(HEX, re.sub(r"var\(--[\w-]+\)", "", st)):
                    lits_html[h.lower().replace(" ", "")] += 1
        names |= {n for n in re.findall(r"var\(--([\w-]+)", p.get("cssScreen") or "") if n.startswith("color-") and n not in toks}
        body = re.sub(r"var\(--[\w-]+(?:,[^()]*(?:\([^()]*\))?[^()]*)?\)", "", c)
        for h in re.findall(HEX, body):
            lits[h.lower().replace(" ", "")] += 1
        bare = sum(1 for v in p.get("values") or [] if isinstance(v, dict) and not v.get("token"))
    m = dd.md_of(slug)
    if m:
        s = m.read_text(encoding="utf-8")
        names |= set(re.findall(r"var\(--([\w-]+)", s))
        names |= {expand(t.replace("/", "-"), slug, toks) for t in MD_TOKEN.findall(s)}
    used = sorted(n for n in names if n in toks)
    unknown = sorted(n for n in names if n not in toks and n not in local
                     and not re.match(r"icon-(?!size|stroke)", n) and not n.endswith("-md"))
    return {"used": used, "unknown": unknown, "local": local, "literals": dict(lits), "literalsHtml": dict(lits_html), "bare": bare,
            "src": dd.rel(m) if m else dd.rel(pj)}


def expand(n, slug, toks):
    """md hay viết tắt: `text/tertiary` = color-text-secondary, `bg/default` trong card = card-bg-default."""
    if n in toks:
        return n
    for c in (f"color-{n}", f"{slug}-{n}", f"{slug.split('-')[0]}-{n}"):
        if c in toks:
            return c
    tail = [t for t in toks if t.endswith("-" + n)]
    return tail[0] if len(tail) == 1 else n


def closure(toks, n, seen=None):
    seen = set() if seen is None else seen
    for r in toks.get(n, {}).get("refs", ()):
        if r not in seen:
            seen.add(r)
            closure(toks, r, seen)
    return seen


def hex_index(toks):
    """giá trị Light/Web → token: ưu tiên semantic (component nên gọi), rồi primitive."""
    idx = defaultdict(list)
    for n, t in toks.items():
        if t["tier"] == "component" or t.get("style") or n.startswith(BRAND_ONLY):
            continue
        v = (resolve(toks, n, "light", "web") or "").lower().replace(" ", "")
        if v:
            idx[v].append(n)
    for v in idx:
        idx[v].sort(key=lambda n: (toks[n]["tier"] != "semantic", len(n)))
    return idx


# ── phần Màu: quét CSS, tên cũ, vai ─────────────────────────────────────────
MD_TOKEN = re.compile(r"`([a-z][a-z0-9-]*(?:/[a-z0-9_-]+)+)`")
_CMT = re.compile(r"/\*.*?\*/", re.S)
GATE = re.compile(r"\[data-(D\d+|V)=[\"']?(\w+)[\"']?\]")
HEX = r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)"
PAGE_SKIP = ("reviews", "snaps", "cmtSnap", "cmtChanges", "refs", "kit", "dsStale")  # nhật ký, không phải nguồn dựng


def css_blocks(c):
    """[(selector, body)] — bỏ comment, @keyframes, @font-face; @media/@supports trải phẳng."""
    c, out, i = _CMT.sub("", c or ""), [], 0
    while True:
        j = c.find("{", i)
        if j < 0:
            return out
        pre, depth, k = c[i:j].strip().rsplit("}", 1)[-1].strip(), 1, j + 1
        while k < len(c) and depth:
            depth += {"{": 1, "}": -1}.get(c[k], 0)
            k += 1
        body = c[j + 1:k - 1]
        if pre.startswith(("@media", "@supports", "@container", "@layer")):
            out += css_blocks(body)
        elif not pre.startswith("@") and pre:
            out.append((pre, body))
        i = k


def decls(body):
    """[(prop, value)] — tách theo ; ngoài ngoặc, bỏ !important."""
    out, cur, depth = [], "", 0
    for ch in body + ";":
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == ";" and depth <= 0:
            if ":" in cur:
                p, v = cur.split(":", 1)
                out.append((p.strip(), v.replace("!important", "").strip()))
            cur = ""
        else:
            cur += ch
    return out


def split_sel(s):
    out, cur, depth = [], "", 0
    for ch in s:
        depth += ch in "([" 
        depth -= ch in ")]"
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return [x for x in out + [cur.strip()] if x]


def walk_strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from walk_strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk_strings(v)


def page_pick(p, slug):
    """Phương án đã chọn của trang brainstorm: preview.pick (đã chốt) → preset Đề xuất (chưa chốt)."""
    pick = (p.get("preview") or {}).get("pick")
    if pick:
        return pick, "chốt"
    rec = next((x.get("pick") for x in p.get("presets") or [] if x.get("id") == "rec"), None)
    return rec or {}, "đề xuất" if rec else "không rõ"


def gate_on(sel, pick):
    return all(pick.get(k, v) == v for k, v in GATE.findall(sel))


# ── nguồn dùng chung, để không đếm một quy tắc của kit thành 5 component ─────
def _load_py(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def _rule_key(sel, body):
    return re.sub(r"\s+", "", sel) + "{" + re.sub(r"\s+", "", body) + "}"


def shared_rules():
    w = dd.COMP / "_work"
    kit = _load_py("ds_forms_kit", w / "_forms/kit.py")
    pv = _load_py("ds_pvkit", w / "_lib/pvkit.py")
    kits = {_rule_key(s, b) for s, b in css_blocks(kit.CSS)}
    chrome = {_rule_key(s, b) for s, b in css_blocks(pv.BASE_CSS)}
    return kits, chrome, getattr(kit, "CSS", "")


CHROME_RE = re.compile(r"^(\.pv|\.vt|\.vh|\.vh small|\.vl|\.vg|\.vgc|\.vgs|\.vg h3 small|\.vgc>\.cap|\.tbl\b.*|\.pg|\.vnote|\.hitnote|\.kv dt|\.foot)$")


# ── tên cũ ───────────────────────────────────────────────────────────────────
def stale_table(toks):
    """{tên cũ đầy đủ color/...: tên mới} theo _token-ledger.json (DEC-318, DEC-320). Tên vừa cũ vừa mới → ambiguous."""
    L = json.loads((dd.COMP / "_token-ledger.json").read_text())
    rn = L["colorRename"]
    ren = {**{f"color/{a}": f"color/{b}" for a, b in rn["map"].items()},
           **{f"color/{a}": f"color/{b}" for a, b in rn.get("merged", {}).items()}}
    cur = {t["jname"] for t in toks.values() if t["jname"]}

    def final(n, seen=()):
        """Token đích có thể đã đổi tên tiếp; tên đang tồn tại thì dừng."""
        return final(ren[n], seen + (n,)) if n in ren and n not in cur and n not in seen else n
    table, ambiguous = {}, sorted(a for a in ren if a in cur)
    for a in ren:
        if a not in cur:
            table[a] = final(a)
    for a, v in L["color"]["tokens"].items():  # 8. Component đã bỏ (DEC-318)
        if a not in cur and v.get("replacement"):
            table[a] = final(v["replacement"])
    return table, ambiguous


STATUS_TAIL = [("-border-subtle", "border/{tone}_subtle"), ("-solid-hover", "bg/{tone}/solid_hover"), ("-bg-strong", "bg/{tone}/secondary"),
               ("-solid", "bg/{tone}/solid"), ("-border", "border/{tone}"), ("-icon", "fg/{tone}/primary"), ("-text", "text/{tone}/primary"),
               ("-bg", "bg/{tone}/primary")]
CHIP_TAIL = {"bg": "utility/{sắc}/50 (xám, cam: 100)", "fg": "utility/{sắc}/700 (xám: 600, cam: 800)",
             "border": "utility/{sắc}/200", "dot": "utility/{sắc}/600 (xám: 500)"}


def stale_pattern(n):
    """Tên viết theo mẫu trong md (`color/chip/{tone}/fg`, `color/status/*-bg`) — ledger không có dòng khớp nguyên văn."""
    n = n.removeprefix("color/")
    if re.fullmatch(r"chip/gray/?\*?", n):
        return "color/utility/neutral/*"
    m = re.fullmatch(r"chip/(?:\{[^}]*\}|\*|[a-z]+)/?([a-z*]*)", n) or re.fullmatch(r"chip/?()", n)
    if m:
        return f"color/{CHIP_TAIL[m.group(1)]}" if m.group(1) in CHIP_TAIL else "color/utility/{sắc}/{bậc}"
    if n.startswith("status"):
        for tail, new in STATUS_TAIL:
            if n.endswith(tail):
                return "color/" + new
        return "color/{bg|text|fg|border}/{success|warning|error|info}/…"
    if re.fullmatch(r"chart/?[\w{}*]*", n):
        return "color/utility/{sắc}/500"
    if re.fullmatch(r"icon/[\w{}*-]+|icon/?", n):
        return "color/fg/…"
    return None


def stale_scan(toks, uni):
    """Tên màu cũ còn trong md (kể cả viết tắt, viết theo mẫu), css và page.json."""
    table, ambiguous = stale_table(toks)
    short = {k.removeprefix("color/"): k for k in table}
    dash = {}
    for k in table:
        d = css(k)
        if d not in toks:
            dash[d] = k
    hits = defaultdict(lambda: {"count": 0, "lines": [], "new": None, "pattern": False})

    def hit(path, old, new, line=None, pattern=False):
        h = hits[(path, old)]
        h["count"] += 1
        h["new"], h["pattern"] = new, pattern
        if line and line not in h["lines"]:
            h["lines"].append(line)
    full_re = re.compile(r"(?<![\w/-])color/[a-z][\w/{}*.-]*")
    for m in sorted((ROOT / "design-system").rglob("*.md")):
        if "/_work/" in str(m):
            continue
        path = dd.rel(m)
        for i, line in enumerate(m.read_text(encoding="utf-8").splitlines(), 1):
            for raw in full_re.findall(line):
                n = raw.rstrip(".*/-") if raw.endswith((".", "/")) else raw
                n = n.rstrip("/.")
                if n in table:
                    hit(path, n, table[n], i)
                elif re.match(r"color/(chip|status|chart|icon)(/|$)", n) and n not in {t["jname"] for t in toks.values()}:
                    new = stale_pattern(n)
                    if new:
                        hit(path, n + ("/" if raw.endswith("/") else ""), new, i, True)
            for t in re.findall(r"`([a-z][\w/{}*-]*)`", line):
                if t in short and t not in {x["jname"] for x in toks.values()}:
                    hit(path, short[t], table[short[t]], i)
                elif re.fullmatch(r"(chip/(\{[^}]*\}|\*)[\w/{}*-]*|status/[\w{}*-]+)", t):
                    new = stale_pattern(t)
                    if new:
                        hit(path, "color/" + t, new, i, True)
    w = dd.COMP / "_work"
    dash_re = re.compile(r"--([a-z][\w-]*)")
    sources = [(dd.rel(w / "_forms/kit.py"), (w / "_forms/kit.py").read_text(encoding="utf-8"))]
    for s in uni:
        pj = w / s / "page.json"
        if pj.exists():
            p = json.loads(pj.read_text())
            sources.append((dd.rel(pj), "\n".join(walk_strings({k: v for k, v in p.items() if k not in PAGE_SKIP}))))
    for path, txt in sources:
        for n in dash_re.findall(txt):
            if n in dash:
                hit(path, dash[n], table[dash[n]])
        for raw in full_re.findall(txt):
            n = raw.rstrip("/.")
            if n in table:
                hit(path, n, table[n])
    return hits, ambiguous, table


# ── quét màu từng component ─────────────────────────────────────────────────
TONES = {"ok": "thành công", "warn": "cảnh báo", "wa": "cảnh báo", "er": "lỗi", "err": "lỗi", "info": "thông tin", "dang": "nguy hiểm", "dng": "nguy hiểm",
         "dg": "nguy hiểm", "dz": "nguy hiểm", "nt": "trung tính", "up": "đang tải"}
STATE_CLS = {"h": "rê chuột", "hv": "rê chuột", "hov": "rê chuột", "hover": "rê chuột", "is-hover": "rê chuột", "p": "đang bấm", "pr": "đang bấm",
             "f": "focus", "fc": "focus", "focus": "focus", "is-focus": "focus", "typ": "focus", "d": "tắt", "dis": "tắt", "disabled": "tắt", "is-dis": "tắt",
             "ld": "đang tải", "on": "đang chọn", "cur": "đang chọn", "sel": "đang chọn", "ind": "đang chọn", "is-on": "đang chọn", "op": "đang mở", "is-open": "đang mở",
             "e": "lỗi", "error": "lỗi", "is-err": "lỗi", "ro": "chỉ đọc", "is-ro": "chỉ đọc"}
DATA_STATE = {"hover": "rê chuột", "focus": "focus", "open": "đang mở", "disabled": "tắt", "error": "lỗi", "readonly": "chỉ đọc", "empty": "focus", "search": "focus",
              "noresult": "focus", "notif": "đang mở", "account": "đang mở", "scope": "đang mở", "crumbmenu": "đang mở"}
PSEUDO = {"hover": "rê chuột", "active": "đang bấm", "focus": "focus", "focus-visible": "focus", "focus-within": "focus", "disabled": "tắt", "checked": "đang chọn"}
STATE_ORDER = ["nghỉ", "rê chuột", "đang bấm", "focus", "đang chọn", "đang mở", "tắt", "chỉ đọc", "lỗi", "đang tải"]
VARIANT_CLS = {("ctl", "sel"), ("ctl", "ms"), ("ctl", "nat")}  # .ctl.sel = ô kiểu Select, không phải "đang chọn"


def parse_selector(sel):
    """Tách một selector thành phần tử (đã bỏ trạng thái, tông), trạng thái, tông, màn."""
    states, tones, flags = set(), set(), set()
    s = GATE.sub("", sel)
    if re.search(r"\[data-theme=[\"']?dark", s):
        flags.add("dark")
    if re.search(r"\[data-platform=[\"']?mobile", s):
        flags.add("mobile")
    if re.search(r"\[data-(ck|sbr|smod)=|\[data-[bm]=", s):
        tones.add("theo phạm vi")
    for v in re.findall(r"\[data-state=[\"']?(\w+)", s):
        if v in DATA_STATE:
            states.add(DATA_STATE[v])
        else:
            flags.add("màn:" + v)
    if "[data-on]" in s:
        states.add("đang chọn")
    s = re.sub(r"\[[^\]]*\]", "", s)
    for inner in re.findall(r":(?:is|where)\(([^()]*)\)", s):
        for v in re.findall(r":([\w-]+)|\.([\w-]+)", inner):
            st = PSEUDO.get(v[0]) or STATE_CLS.get(v[1])
            if st:
                states.add(st)
    s = re.sub(r":(?:is|where|has|not)\((?:[^()]|\([^()]*\))*\)", "", s)
    pe = re.search(r"::?(before|after)\b", s)
    s = re.sub(r"::?(before|after)\b", "", s)
    for v in re.findall(r":([\w-]+)", s):
        if v in PSEUDO:
            states.add(PSEUDO[v])
    s = re.sub(r":[\w-]+", "", s)
    parts = []
    for comp in re.split(r"\s*[ >+~]\s*", s.strip()):
        if not comp:
            continue
        tag = re.match(r"^[a-z][\w]*", comp)
        cls = re.findall(r"\.([\w-]+)", comp)
        keep = [tag.group(0)] if tag else []
        for i, c in enumerate(cls):
            first = i == 0 and not tag
            m = re.fullmatch(r"[tc]-(red|blue|yellow|green|teal|amber|violet|gray|purple|orange)", c)
            if m:
                tones.add(m.group(1))
            elif first:
                keep.append("." + c)
            elif cls[0] and (cls[0], c) in VARIANT_CLS:
                keep.append("." + c)
            elif c in TONES:
                tones.add(TONES[c])
            elif c in STATE_CLS:
                if STATE_CLS[c]:
                    states.add(STATE_CLS[c])
            else:
                keep.append("." + c)
        b = "".join(keep)
        if b and b not in (".pv",):
            parts.append(b)
    base = " ".join(parts) + ("::" + pe.group(1) if pe else "")
    return {"base": base, "states": states, "tones": tones, "flags": flags}


_X = r"(?:\.[\w-]+)*"
_ROLE_SRC = [  # (phạm vi, regex trên phần tử đã chuẩn hoá, phần tử, phần, cờ) — cờ i = thuộc tính color là icon; ? = suy không chắc
    # theo component (class trùng tên nhưng khác nghĩa)
    (("header-navigation",), r"\.(mi|msi)~$", "Mục menu", "icon", "i"),
    (("header-navigation",), r"\.(mi|msi) span$", "Mục menu", "thân", ""),
    (("alert-notification",), r"\.ts~$", "Toast", "thân", ""), (("alert-notification",), r"\.al~$", "Alert", "thân", ""),
    (("alert-notification",), r"\.(ts|al) \.ds$", "Toast, Alert", "mô tả", ""), (("alert-notification",), r"\.cl$", "Nút icon", "thân", "i"),
    (("alert-notification",), r"\.lk~$", "Nút link", "thân", ""),
    (("field-upload",), r"\.ib$", "Nút icon", "thân", "i"), (("field-upload",), r"\.az \.fi$", "Featured icon", "trong vùng ảnh", "i"),
    (("field-upload",), r"\.dz~ \.fi$|\.fi$", "Featured icon", "thân", "i"),
    (("buttons",), r"\.fi$", "Featured icon", "thân", "i t=lỗi"), (("sidebar-navigation",), r"\.fi$", "Featured icon", "thân", "i t=cảnh báo"),
    (("alert-notification",), r"\.bn \.bt$", "Nút", "trong Banner", ""),
    (("header-navigation",), r"\.acc~$", "Nút tài khoản", "thân", ""),
    (("field-upload",), r"\.tov~$|\.tcap$|\.tx$", "Ảnh tải lên", "lớp phủ", ""),
    (("sidebar-navigation", "sidebar-navigation-r2"), r"\.sic$|\.mt~$|\.t-\w+$", "Ô phân hệ", "thân", ""),
    (("header-navigation", "sidebar-navigation", "sidebar-navigation-r2"), r"\.ib$", "Nút icon", "thân", "i"),
    (("sidebar-navigation",), r"\.lk$", "Nút link", "thân", ""),
    (("badge-avatar",), r"\.fb\.dt$", "Chip", "kiểu Dot", ""), (("badge-avatar",), r"\.fb\.bm$", "Chip", "kiểu Modern", ""), (("badge-avatar",), r"\.fb\.(po|bo)$", "Chip", "kiểu Outline", ""),
    (("badge-avatar",), r"\.fb~$", "Chip", "thân", ""), (("badge-avatar",), r"\.fb~ \.fi$", "Chip", "icon", "i"),
    (("badge-avatar",), r"\.fa\.more$", "Avatar", "ô +N", ""), (("badge-avatar",), r"\.fa\.co~$", "Avatar", "logo công ty", ""),
    (("badge-avatar",), r"\.fb~ \.fdot$", "Chip", "chấm", ""), (("badge-avatar",), r"\.fb~ \.fcnt$", "Chip", "ô số đếm", ""),
    (("badge-avatar",), r"\.fa~$", "Avatar", "thân", ""), (("badge-avatar",), r"\.fa \.fai$", "Avatar", "icon", "i"),
    (("badge-avatar",), r"\.fa \.fup~$", "Avatar", "nút đổi ảnh", "i"), (("badge-avatar",), r"\.fadd$", "Avatar", "nút thêm", "i"),
    (("sidebar-navigation",), r"\.bd$", "Chip số đếm", "thân", ""), (("sidebar-navigation",), r"\.it \.bd$", "Chip số đếm", "thân", ""),
    (("sidebar-navigation-r2",), r"\.nb$", "Chip số đếm", "thân", ""), (("sidebar-navigation-r2",), r"\.so \.ok$", "Mục menu", "dấu chọn", "i"),
    (("sidebar-navigation",), r"\.sc$", "Thẻ phạm vi", "thân", ""), (("sidebar-navigation-r2",), r"\.scope$", "Thẻ phạm vi", "thân", ""),
    (("sidebar-navigation",), r"\.sl$", "Breadcrumb", "dấu phân cách", "i"),
    (("sidebar-navigation",), r"\.(bc|brb)$", "Breadcrumb", "mục", ""),
    (("multiselect",), r"\.fs$", "Sheet", "thân", ""), (("multiselect",), r"\.more$", "Chip", "thân", "t=gray"), (("multiselect",), r"\.cn$", "Ô chọn nhiều", "số đã chọn", ""),
    (("error-page",), r"\.ep-search$", "Ô nhập", "thân", "? i"), (("error-page",), r"\.ep-feat$", "Featured icon", "thân", "i"),
    (("tooltip",), r"\.sheet \.ok$", "Nút", "Secondary", ""), (("tooltip",), r"\.hi$", "Icon trợ giúp", "thân", "i"),
    # nút
    (None, r"\.bt\.pri$", "Nút", "Primary", ""), (None, r"\.bt\.sec$", "Nút", "Secondary", ""), (None, r"\.bt\.ter$", "Nút", "Tertiary", ""),
    (None, r"\.bt\.lkg$", "Nút", "Link", ""), (None, r"\.bt$", "Nút", "Mặc định", ""),
    (None, r"\.(cx|ut)~$", "Nút icon", "thân", "i"), (None, r"\.tg \.x$", "Tag", "nút xoá", "i"),
    # ô nhập
    (None, r"\.ctl~ \.ph$|\.ta \.tph$|\.sph$|\.pin \.pin-ph$", "Ô nhập", "placeholder", ""),
    (None, r"\.ctl~ \.(ic|chev)$|\.ta \.lk$", "Ô nhập", "icon", "i"), (None, r"\.nb~$", "Ô nhập", "nút tăng giảm", "i"),
    (None, r"\.ad~$", "Ô nhập", "addon", ""), (None, r"\.ab~$", "Ô nhập", "nút addon", ""), (None, r"\.ctl\.nat$", "Ô nhập", "kiểu native", ""),
    (None, r"\.ctl~ \.eic$", "Ô nhập", "icon lỗi", "i"), (None, r"\.ctl~ \.sub$", "Ô nhập", "chữ phụ", ""),
    (None, r"\.ctl~ \.v$|\.sbx \.q$", "Ô nhập", "thân", ""),
    (None, r"\.ctl~$|\.ta~$|\.ob~$|\.otp \.ob$|\.fld \.in$", "Ô nhập", "thân", ""),
    (None, r"\.sbx~$|\.se$", "Ô nhập", "thân", "? p"), (None, r"\.fsel$", "Ô nhập", "thân", "?"),
    # nhãn trường
    (None, r"\.(cl|clm) \.lb$", "Ô chọn", "nhãn", ""), (None, r"\.(cl|clm) \.hn$", "Ô chọn", "mô tả", ""),
    (None, r"(\.lb|\.flb) \.req$|\.req$", "Trường nhập", "dấu bắt buộc", ""), (None, r"(\.lb|\.flb) \.hi$", "Icon trợ giúp", "thân", "i"),
    (None, r"\.lb$|\.flb$|\.fld label$", "Trường nhập", "nhãn", ""), (None, r"\.hn$", "Trường nhập", "gợi ý", ""),
    (None, r"\.fe$", "Trường nhập", "thông báo lỗi", ""), (None, r"\.msg~$", "Trường nhập", "gợi ý", ""), 
    # ô chọn
    (None, r"\.(cb|cbx)~$", "Ô chọn", "Checkbox", ""), (None, r"\.rd~$", "Ô chọn", "Radio", ""), (None, r"\.tgl~$", "Công tắc", "thân", ""),
    (None, r"\.gx~$", "Thẻ chọn", "thân", ""),
    # menu, danh sách
    (None, r"\.mi \.ms$|\.ro \.(r2|rr)$|\.(mi|msi) \.mv$|\.so \.o2$|\.o2$|\.ps$|\.mem$", "Mục menu", "chữ phụ", ""),
    (None, r"\.ro \.ri$|\.so \.oi$|\.oi$|\.pr \.pi$|\.pe \.pei$", "Mục menu", "icon trong ô", "i"),
    (None, r"\.mi \.ic$|\.pr svg$|\.(mit|mrow) \.i$", "Mục menu", "icon", "i"),
    (None, r"\.msr$", "Menu", "ô tìm", "i"),
    (None, r"\.(mi|ro) \.ck$|\.ck$", "Mục menu", "dấu chọn", "i"),
    (None, r"\.so \.o1$|\.arow \.o1$", "Mục menu", "thân", ""),
    (None, r"\.mi~$|\.ro~$|\.pr~$|\.op~$|\.so~$|\.sdi~$|\.sh-i~$|\.msi~$|\.mit~$|\.elm a$|\.sc3 \.r$", "Mục menu", "thân", ""),
    (None, r"\.mh$|\.gh$|\.gt$|\.pt$|\.sdt$|\.pfh$|\.phk$|\.pok$", "Menu", "tiêu đề nhóm", ""),
    # điều hướng
    (None, r"\.ni~ \.nic$|\.it~ \.i$", "Mục điều hướng", "icon", "i"), (None, r"\.it\.par$", "Mục điều hướng", "mục cha", ""), (None, r"\.ni~$|\.it~$", "Mục điều hướng", "thân", ""),
    (None, r"\.tb~$|\.hd2 \.tb~$|\.mtab~$", "Tab", "thân", ""),
    (None, r"\.bc \.sep$|\.mhd \.sep$", "Breadcrumb", "dấu phân cách", "i"), (None, r"\.bc \.cur$", "Breadcrumb", "mục hiện tại", ""), (None, r"\.bc \.(ci|hm|sib)~$|\.bc$", "Breadcrumb", "mục", ""),
    # lớp nổi
    (None, r"\.sht \.hd$|\.(msh|sheet) \.grab$", "Sheet", "thanh kéo", ""), (None, r"\.sht~$|\.msh$|\.sheet$", "Sheet", "thân", ""),
    (None, r"\.dlg$", "Hộp thoại", "thân", ""), (None, r"\.dlg (\.bd|p)$", "Hộp thoại", "mô tả", ""),
    (None, r"\.scr$|\.scrim$|\.mscr$|\.fa \.fscrim$", "Lớp phủ", "thân", ""),
    (None, r"\.mn$|\.am$|\.pal$|\.elm$|\.pop~$|\.pcm~$", "Menu nổi", "thân", ""),
    (None, r"\.tt~$|\.tip$", "Tooltip", "thân", ""),
    # chip, tag, avatar
    (None, r"\.chip~$", "Chip", "thân", "t=gray"), (None, r"\.bdg$", "Chip", "kiểu Modern", "?"), (None, r"\.tg \.ct$", "Tag", "ô số đếm", ""), (None, r"\.tg~$", "Tag", "thân", ""),
    (None, r"\.av$", "Avatar", "thân", ""), (None, r"\.av32$", "Avatar", "ảnh chèn", "?"), (None, r"\.bell \.nc$", "Chuông thông báo", "số đếm", ""), (None, r"\.bell \.nd$", "Chuông thông báo", "chấm", ""),
    # tiến độ, vạch, khác
    (None, r"\.(pb|bar) i$", "Thanh tiến độ", "phần đã chạy", ""), (None, r"\.pb$|\.bar$|\.fr \.fill$", "Thanh tiến độ", "rãnh", ""),
    (None, r"\.mdv$|\.msep$|\.hr$|\.dv$|\.sdv$|\.sep$", "Vạch chia", "thân", ""),
    (None, r"\.kbd$|^kbd$|\.sbs \.kb$", "Phím tắt", "thân", ""),
    (None, r"\.dz~$|\.az~$", "Vùng tải tệp", "thân", ""), (None, r"\.fr~$", "Dòng tệp", "thân", ""),
]
ROLE_TABLE = [(sc, re.compile(r"(?:^| )(?:" + rx.replace("$", "").replace("^", "").replace("~", _X) + r")$"), el, part, fl) for sc, rx, el, part, fl in _ROLE_SRC]
RAW_ROLE = [  # khớp trên selector gốc, khi trạng thái nằm trong tên class
    (re.compile(r"\.dz\.hover$"), "Vùng tải tệp", "thân", "", "đang kéo thả"),
    (re.compile(r"\.(fst\.on>i|av \.on)$"), "Avatar", "chấm trực tuyến", "", "nghỉ"),
    (re.compile(r"\.rd\.(d\.)?on::after$"), "Ô chọn", "Radio, chấm giữa", "", None),
    (re.compile(r"\.tgl i$"), "Công tắc", "núm", "", None),
    (re.compile(r"\.msg\.err$|\.cnt\.err$"), "Trường nhập", "thông báo lỗi", "", "nghỉ"),
]
SOLID_BG = re.compile(r"^color-bg-(error|success|warning|info)-solid$")
# Luật có căn cứ trong color.md hoặc DEC: thắng số đông.
ROLE_RULE = {
    ("Chip", "thân", "chữ", "nghỉ", "gray"): ("color-utility-neutral-600", "color.md 3.2, 3.4: chip xám nền utility/neutral/100, chữ utility/neutral/600"),
    ("Ô nhập", "thân", "nền", "nghỉ"): ("color-bg-primary", "DEC-316: ô nhập một kiểu nền trắng + viền, web và app"),
    ("Avatar", "thân", "nền", "nghỉ"): ("color-accent-bg", "color.md: accent/bg là nền avatar"),
    ("Avatar", "thân", "chữ", "nghỉ"): ("color-accent-fg", "color.md: accent/fg là chữ viết tắt trên avatar"),
    ("Vạch chia", "thân", "vạch", "nghỉ"): ("color-border-secondary", "color.md: border/secondary là viền mặc định"),
    ("Ô nhập", "thân", "viền", "nghỉ"): ("color-border-input", "DEC-321: viền ô nhập border/input (4,74:1)"),
    ("Ô nhập", "thân", "viền", "rê chuột"): ("color-border-input_hover", "DEC-321: ô nhập rê chuột border/input_hover"),
    ("Ô nhập", "thân", "viền", "focus"): ("color-focus-ring", "DEC-321: focus ô nhập viền 2px focus/ring"),
    ("Ô nhập", "thân", "viền", "lỗi"): ("color-border-error", "color.md: border/error là viền lỗi ô nhập"),
    ("Ô nhập", "thân", "nền", "chỉ đọc"): ("color-bg-secondary", "DEC-321: ô chỉ đọc bg/secondary"),
    ("Ô nhập", "thân", "nền", "tắt"): ("color-bg-disabled", "color.md: bg/disabled là nền control tắt"),
    ("Ô nhập", "thân", "viền", "tắt"): ("color-border-disabled", "color.md: border/disabled là viền control tắt"),
    ("Ô nhập", "thân", "chữ", "tắt"): ("color-text-disabled", "color.md: chữ control tắt"),
    ("Ô nhập", "icon", "icon", "nghỉ"): ("color-fg-quaternary", "color.md: fg/quaternary là icon trong ô nhập"),
    ("Ô nhập", "icon", "icon", "tắt"): ("color-fg-disabled", "color.md: fg/disabled là icon control tắt"),
    ("Ô nhập", "placeholder", "chữ", "nghỉ"): ("color-text-placeholder", "color.md: text/placeholder"),
    ("Trường nhập", "nhãn", "chữ", "nghỉ"): ("color-text-secondary", "DEC-321: nhãn trường text/secondary"),
    ("Trường nhập", "gợi ý", "chữ", "nghỉ"): ("color-text-tertiary", "color.md: chữ hỗ trợ text/tertiary"),
    ("Ô chọn", "Checkbox", "nền", "đang chọn"): ("color-accent-solid", "DEC-321, color.md: ô chọn accent/solid"),
    ("Ô chọn", "Radio", "nền", "đang chọn"): ("color-accent-solid", "DEC-321, color.md: radio accent/solid"),
    ("Ô chọn", "Checkbox", "viền", "đang chọn"): ("color-accent-border", "color.md: accent/border là viền ô chọn đang chọn"),
    ("Ô chọn", "Radio", "viền", "đang chọn"): ("color-accent-border", "color.md: accent/border là viền ô chọn đang chọn"),
    ("Công tắc", "thân", "nền", "đang chọn"): ("color-accent-solid", "color.md: công tắc bật accent/solid"),
    ("Thẻ chọn", "thân", "viền", "đang chọn"): ("color-accent-border", "color.md: accent/border là viền thẻ chọn"),
    ("Thanh tiến độ", "phần đã chạy", "nền", "nghỉ"): ("color-accent-solid", "DEC-321: tiến độ accent/solid"),
    ("Thanh tiến độ", "rãnh", "nền", "nghỉ"): ("color-bg-quaternary", "color.md: bg/quaternary là rãnh thanh tiến độ"),
    ("Sheet", "thanh kéo", "nền", "nghỉ"): ("color-bg-quaternary", "DEC-321: thanh kéo sheet bg/quaternary"),
    ("Sheet", "thân", "nền", "nghỉ"): ("color-bg-primary_alt", "color.md: bg/primary_alt là nền menu, dialog, sheet"),
    ("Hộp thoại", "thân", "nền", "nghỉ"): ("color-bg-primary_alt", "color.md: bg/primary_alt là nền menu, dialog, sheet"),
    ("Menu nổi", "thân", "nền", "nghỉ"): ("color-bg-primary_alt", "color.md: bg/primary_alt là nền menu, dialog, sheet"),
    ("Lớp phủ", "thân", "nền", "nghỉ"): ("color-bg-overlay", "color.md: bg/overlay là lớp phủ sau dialog, sheet"),
    ("Tooltip", "thân", "nền", "nghỉ"): ("color-bg-primary_solid", "color.md: bg/primary_solid là nền tooltip"),
    ("Mục menu", "thân", "nền", "rê chuột"): ("color-bg-primary_hover", "color.md: bg/primary_hover là rê chuột menu, dòng bảng"),
    ("Mục menu", "thân", "nền", "đang bấm"): ("color-bg-pressed", "color.md: bg/pressed là đang bấm dòng danh sách"),
    ("Mục menu", "thân", "nền", "đang chọn"): ("color-bg-selected", "color.md: bg/selected"),
    ("Mục điều hướng", "thân", "nền", "rê chuột"): ("color-bg-primary_hover", "color.md: bg/primary_hover"),
    ("Mục điều hướng", "thân", "nền", "đang chọn"): ("color-bg-selected", "color.md: bg/selected"),
    ("Avatar", "chấm trực tuyến", "nền", "nghỉ"): ("color-fg-success-secondary", "color.md: fg/success/secondary là chấm online avatar"),
    ("Nền đặc màu", "chữ trên nền", "chữ", "nghỉ"): ("color-text-white", "color.md mục 3.4: chữ trên nền đặc màu dùng text/white, Dark vẫn đạt ≥ 5,72:1"),
    ("Tab", "thân", "gạch chỉ báo", "đang chọn"): ("color-accent-solid", "DEC-321: gạch tab accent/solid"),
    ("Trường nhập", "thông báo lỗi", "chữ", "nghỉ"): ("color-text-error-primary", "color.md: chữ lỗi mặc định"),
}
FAMILY = {"chữ": ("color-text-", "color-utility-", "color-accent-"), "icon": ("color-fg-", "color-utility-", "color-accent-"),
          "nền": ("color-bg-", "color-action-", "color-utility-", "color-accent-"),
          "viền": ("color-border-", "color-focus-", "color-accent-", "color-utility-"), "vạch": ("color-border-",),
          "vòng focus": ("color-focus-",), "gạch chỉ báo": ("color-accent-", "color-border-", "color-fg-")}


def classify_role(slug, sel, base):
    for rx, el, part, fl, state in RAW_ROLE:
        if rx.search(sel):
            return el, part, fl, state
    for scope, rx, el, part, fl in ROLE_TABLE:
        if (scope is None or slug in scope) and rx.search(base):
            return el, part, fl, None
    return None


def prop_kind(prop, val):
    """Thuộc tính CSS → (loại, ghi chú). None = không xét (trang trí, bóng đổ, biến)."""
    if prop.startswith("--"):
        return None
    if prop in ("background", "background-color"):
        return None if re.search(r"gradient\(", val) else "nền"
    if prop == "color":
        return "chữ"
    if prop in ("fill", "stroke"):
        return "icon"
    if prop in ("border", "border-color"):
        return "viền"
    if re.fullmatch(r"border-(top|right|bottom|left)", prop):
        return "vạch"
    if prop in ("outline", "outline-color"):
        return "vòng focus"
    if prop == "box-shadow":
        if re.search(r"inset\s+0\s+0\s+0\s+\d", val):
            return "viền"
        if re.search(r"inset\s+-?\d+px\s+-?\d*p?x?\s*0?\s*0?\s*var", val) or re.search(r"inset\s+\d+px\s+0\s+0", val) or re.search(r"inset\s+0\s+-\d", val):
            return "gạch chỉ báo"
        if re.search(r"focus-ring", val):
            return "viền"
        return None
    return None


def color_scan(slug, p, toks, kits, chrome):
    """Mọi khai báo màu còn hiệu lực của trang: bỏ khối token chép sẵn, vỏ trang duyệt, phương án brainstorm không chọn."""
    pick, pick_src = page_pick(p, slug)
    c = p.get("css") or ""
    rows, defs, skipped = [], defaultdict(list), 0
    is_col = lambda n: n in toks and toks[n]["group"] == "color"
    for sel_all, body in css_blocks(c):
        key = _rule_key(sel_all, body)
        src = "kit" if key in kits else "page"
        if key in chrome:
            continue
        ds = decls(body)
        for sel in split_sel(sel_all):
            if not gate_on(sel, pick):
                if "var(--color" in body:
                    skipped += 1
                continue
            for prop, val in ds:
                if prop.startswith("--"):
                    n = prop[2:]
                    if n not in toks and not n.startswith(RETIRED):
                        defs[n].append({"sel": sel, "value": val, "gated": bool(GATE.search(sel))})
    for sel_all, body in css_blocks(c):
        key = _rule_key(sel_all, body)
        src = "kit" if key in kits else "page"
        if key in chrome:
            continue
        ds = [(pp, v) for pp, v in decls(body) if not pp.startswith("--")]
        bg_tok = next((m for pp, v in ds if pp in ("background", "background-color")
                       for m in [re.match(r"var\(--([\w-]+)\)", v)] if m), None)
        fg_tok = next((m for pp, v in ds if pp == "color" for m in [re.fullmatch(r"var\(--([\w-]+)\)", v)] if m), None)
        for sel in split_sel(sel_all):
            if not gate_on(sel, pick) or CHROME_RE.match(sel.strip()):
                continue
            for prop, val in ds:
                refs = re.findall(r"var\(--([\w-]+)", val)
                cols = [r for r in refs if is_col(r)]
                aliases = [r for r in refs if r not in toks]
                lits = re.findall(HEX, val)
                if not cols and not aliases and not lits:
                    continue
                kind_ = prop_kind(prop, val)
                rows.append({"sel": sel, "prop": prop, "val": val, "kind": kind_, "cols": cols, "aliases": aliases, "lits": lits, "src": src,
                             "bg": bg_tok.group(1) if bg_tok else None, "fg": fg_tok.group(1) if fg_tok else None,
                             "gated": bool(GATE.search(sel))})
    return {"rows": rows, "defs": defs, "pick": pick, "pickSrc": pick_src, "skipped": skipped}


def resolve_aliases(scan, toks):
    """Biến tự đặt: giá trị cuối cùng theo từng selector (phương án chọn đè lên gốc)."""
    out = {}
    for n, ds in scan["defs"].items():
        last = {}
        for d in ds:  # cùng selector (bỏ cổng phương án, Dark) → khai báo sau đè khai báo trước
            k = re.sub(r"\[data-theme=[\"']?dark[\"']?\]|\.pv(?![\w-])", "", GATE.sub("", d["sel"]))
            last[re.sub(r"\s+", "", k)] = d
        out[n] = list(last.values())
    return out


ALIAS_RULE = {  # biến tự đặt có quyết định rõ: đề xuất theo quyết định, không theo giá trị đang gán
    "field-bg": ("color-bg-primary", "DEC-316: bỏ field/bg/*, ô nhập một kiểu nền trắng; giá trị đang gán là bản cũ"),
    "tg-off": ("color-bg-quaternary_hover", "DEC-321: công tắc tắt bg/quaternary_hover; bản đang gán Sáng khác Tối"),
    "tg-off-h": ("color-fg-quaternary", "DEC-321: công tắc tắt khi rê chuột fg/quaternary"),
}


def alias_value_token(v):
    m = re.fullmatch(r"var\(--([\w-]+)(?:,[^()]*(?:\([^()]*\))?[^()]*)?\)", (v or "").strip())
    return m.group(1) if m else None


def alias_info(a, defs, toks, uses, allvals=(), fallback=None):
    """Phân loại một biến tự đặt: màu hay không, thay bằng token nào, hay là biến đổi theo biến thể."""
    vals = sorted({d["value"] for d in defs}) or ([f"var(--{fallback})"] if fallback else sorted(set(allvals)))
    tokens = [alias_value_token(v) for v in vals]
    is_color = any(t in toks and toks[t]["group"] == "color" for t in tokens if t) or any(re.search(HEX, v) for v in vals) or any(re.fullmatch(r"(white|black|transparent)", v) for v in vals)
    info = {"color": bool(is_color), "values": vals, "uses": uses, "defs": [{"sel": d["sel"][:80], "value": d["value"]} for d in defs][:12]}
    if not is_color:
        return info
    sem = [t for t in tokens if t and t in toks and toks[t]["tier"] in ("semantic", "brand")]
    if a in ALIAS_RULE and uses and ALIAS_RULE[a][0] in toks:
        info.update(sub="replace", suggest=ALIAS_RULE[a][0], aliasWhy=ALIAS_RULE[a][1])
    elif not defs and fallback and uses:
        info.update(sub="replace", suggest=fallback, aliasWhy="Biến chỉ được gán trong phương án không chọn; đang chạy bằng giá trị dự phòng trong var().")
    elif not uses:
        info.update(sub="dead", suggest=sem[0] if len(sem) == 1 else None)
    elif len(vals) == 1 and len(sem) == 1:
        info.update(sub="replace", suggest=sem[0])
    elif len(sem) == len(vals) and len(vals) > 1:
        info.update(sub="switch", suggest=None)
    else:
        info.update(sub="raw", suggest=None)
    return info


# ── vai ──────────────────────────────────────────────────────────────────────
def role_analysis(scans, toks, uni):
    """Gom khai báo màu theo vai (phần tử × phần × thuộc tính × trạng thái × tông). Không suy được vai → unresolved."""
    roles, unresolved, switched = {}, {}, 0
    for slug, sc in scans.items():
        file = dd.rel(dd.COMP / "_work" / slug / "page.json")
        seen = {}
        for r in sc["rows"]:
            if not r["kind"] or "dark" in parse_selector(r["sel"])["flags"]:
                continue
            ps = parse_selector(r["sel"])
            cl = classify_role(slug, r["sel"], ps["base"])
            tok = r["cols"][0] if r["cols"] else None
            if not tok and r["aliases"]:
                a = r["aliases"][0]
                vals = {alias_value_token(d["value"]) for d in sc["aliases"].get(a, [])}
                if len(vals) == 1 and next(iter(vals)) in toks:
                    tok = next(iter(vals))
                else:
                    switched += 1
                    continue
            if not tok or toks.get(tok, {}).get("group") != "color":
                continue
            if "color-mix" in r["val"]:
                continue
            kind_ = r["kind"]
            if kind_ == "vạch" and (not cl or cl[0] not in ("Ô nhập",)):
                cl = ("Vạch chia", "thân", "", None)
            if not cl:
                k = (slug, r["sel"], kind_)
                unresolved[k] = {"comp": slug, "sel": r["sel"][:90], "prop": kind_, "token": tok, "file": file}
                continue
            el, part, fl, forced = cl
            if kind_ == "chữ" and "i" in fl.split():
                kind_ = "icon"
            if kind_ == "chữ" and "p" in fl.split():
                part = "placeholder"
            if el == "Vạch chia" and kind_ == "nền":
                kind_ = "vạch"
            if kind_ == "vạch" and el == "Ô nhập":
                part = "vạch ngăn"
            state = forced or " + ".join(sorted(ps["states"], key=STATE_ORDER.index)) or "nghỉ"
            if kind_ == "vòng focus" and "focus" not in state and not tok.startswith("color-focus"):
                kind_ = "viền"
            tone = " + ".join(sorted(ps["tones"]))
            forced_tone = next((x[2:] for x in fl.split() if x.startswith("t=")), None)
            if forced_tone and not tone:
                tone = forced_tone
            place = {"comp": slug, "sel": r["sel"][:110], "file": dd.rel(dd.COMP / "_work/_forms/kit.py") if r["src"] == "kit" else file,
                     "src": r["src"], "gated": r["gated"], "mobile": "mobile" in ps["flags"], "unsure": "?" in fl.split(), "pickSrc": sc["pickSrc"]}
            key = (el, part, kind_, state, tone)
            # phương án đã chọn đè khai báo gốc cùng phần tử trong cùng component
            dk = (slug, ps["base"], kind_, state, tone, frozenset(ps["flags"]))
            prev = seen.get(dk)
            if prev and prev["gated"] and not r["gated"]:
                continue
            if prev and r["gated"] and not prev["gated"]:
                for rk, t, pl in prev["items"]:
                    roles[rk][t].remove(pl)
                prev = None
            items = prev["items"] if prev else []
            if prev:  # cùng selector, khai báo sau trong file đè khai báo trước
                for it in [x for x in items if x[2]["sel"] == r["sel"][:110]]:
                    roles[it[0]][it[1]].remove(it[2])
                    items.remove(it)
            roles.setdefault(key, defaultdict(list))[tok].append(place)
            items.append((key, tok, place))
            if r["bg"] and SOLID_BG.match(r["bg"]) and kind_ == "chữ":
                sk = ("Nền đặc màu", "chữ trên nền", "chữ", "nghỉ", "")
                sp = {**place, "bg": r["bg"]}
                roles.setdefault(sk, defaultdict(list))[tok].append(sp)
                items.append((sk, tok, sp))
            seen[dk] = {"gated": r["gated"], "items": items}
    return roles, list(unresolved.values()), switched


def _hex(v):
    v = (v or "").strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{3})", v)
    if m:
        v = "#" + "".join(c * 2 for c in m.group(1))
    m = re.fullmatch(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?", v)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (int(m.group(2), 16) / 255 if m.group(2) else 1,)
    m = re.fullmatch(r"rgba?\(([^)]*)\)", v)
    if m:
        x = [float(t.rstrip("%")) for t in re.split(r"[,\s/]+", m.group(1).strip()) if t]
        return (x[0], x[1], x[2], x[3] if len(x) > 3 else 1)
    return None


def _lum(c):
    f = lambda u: (u / 255) / 12.92 if (u / 255) <= .03928 else (((u / 255) + .055) / 1.055) ** 2.4
    return .2126 * f(c[0]) + .7152 * f(c[1]) + .0722 * f(c[2])


def contrast(a, b):
    ca, cb = _hex(a), _hex(b)
    if not ca or not cb:
        return None
    if cb[3] < 1:
        return None
    if ca[3] < 1:
        ca = tuple(ca[i] * ca[3] + cb[i] * (1 - ca[3]) for i in range(3)) + (1,)
    x, y = sorted((_lum(ca), _lum(cb)), reverse=True)
    return round((x + .05) / (y + .05), 2)


def short(n):
    return (n or "").removeprefix("color-")


def tname(toks, n):
    return (toks.get(n, {}).get("jname") or n).removeprefix("color/")


def slugify(s):
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def role_findings(roles, toks, F):
    """Cùng vai mà 2+ token, hoặc lệch luật có căn cứ → finding role--…. Trả bảng mọi vai để hiển thị."""
    table = []
    for key, by in sorted(roles.items(), key=lambda kv: kv[0]):
        el, part, prop, state, tone = key
        by = {t: ps for t, ps in by.items() if ps}
        if not by:
            continue

        def srcs(ps):  # kit tính 1 nguồn, không tính 5 component
            return len({("kit" if p["src"] == "kit" else p["comp"]) for p in ps})
        rows = sorted(({"token": t, "name": tname(toks, t), "sources": srcs(ps), "comps": sorted({p["comp"] for p in ps}), "places": ps}
                       for t, ps in by.items()), key=lambda r: (-r["sources"], -len(r["comps"]), r["name"]))
        rule = ROLE_RULE.get(key) or (ROLE_RULE.get((el, part, prop, state)) if not tone else None)
        if tone == "theo phạm vi":  # màu theo dữ liệu phân hệ của demo, không phải cùng một vai
            table.append({"key": "|".join(key), "element": el, "part": part, "prop": prop, "state": state, "tone": tone, "finding": None,
                          "tokens": [{"token": r["token"], "name": r["name"], "sources": r["sources"], "comps": r["comps"], "n": len(r["places"])} for r in rows],
                          "comps": sorted({p["comp"] for ps in by.values() for p in ps})})
            continue
        tset = set(by)
        fam = FAMILY.get(prop, ())
        wrong = [t for t in tset if fam and not t.startswith(fam)]
        dev_places = [p for t, ps in by.items() for p in ps]
        unsure = bool(dev_places) and all(p["unsure"] for p in dev_places)
        suggest, why, certain, reason = None, "", True, None
        if rule and rule[0] in toks:
            suggest, why = rule
            if tset != {suggest}:
                reason = "lệch luật" if len(tset) == 1 else "nhiều token"
                off = [p for t, ps in by.items() if t != suggest for p in ps]
                unsure = bool(off) and all(p["unsure"] for p in off)
        if not suggest:
            good = [r for r in rows if not (fam and not r["token"].startswith(fam))] or rows
            suggest = good[0]["token"]
            top = good[0]["sources"]
            tie = sum(1 for r in good if r["sources"] == top) > 1
            why = f"nhiều nguồn dùng nhất ({top} nguồn)"
            if len(tset) > 1:
                reason = "nhiều token"
                if tie:
                    certain, why = False, f"hoà {top} nguồn, phải chọn tay"
            elif wrong:
                alt = "color-fg-" + wrong[0].removeprefix("color-text-") if prop == "icon" and wrong[0].startswith("color-text-") else None
                if alt and alt in toks:
                    suggest, why, reason = alt, "color.md: icon dùng nhóm fg/*, không dùng nhóm chữ", "sai nhóm"
        if unsure:
            certain = False
        row = {"key": "|".join(key), "element": el, "part": part, "prop": prop, "state": state, "tone": tone,
               "tokens": [{"token": r["token"], "name": r["name"], "sources": r["sources"], "comps": r["comps"], "n": len(r["places"])} for r in rows],
               "comps": sorted({p["comp"] for ps in by.values() for p in ps}), "finding": None}
        table.append(row)
        if not reason:
            continue
        fid = "role--" + "--".join(slugify(x) for x in (el, part, prop, state) + ((tone,) if tone else ()))
        row["finding"] = fid
        devs = [{"token": r["token"], "name": r["name"], "comps": r["comps"], "sources": r["sources"], "n": len(r["places"]),
                 "places": [{"comp": p["comp"], "sel": p["sel"], "file": p["file"], "src": p["src"], "pickSrc": p["pickSrc"], "unsure": p["unsure"]} for p in r["places"]][:24]}
                for r in rows if r["token"] != suggest]
        keep = next((r for r in rows if r["token"] == suggest), None)
        on = "color-bg-primary"
        fg = "color-text-primary"
        if el in ("Nền đặc màu",):
            on = next((p.get("bg") for ps in by.values() for p in ps if p.get("bg")), on)
        title = " · ".join(x for x in (el, None if part == "thân" else part, None if prop == part else prop, state, tone or None) if x)
        F(fid, "role", title, color=True, element=el, part=part, prop=prop, state=state, tone=tone, reason=reason, certain=certain,
          suggest=suggest, suggestName=tname(toks, suggest), suggestComps=keep["comps"] if keep else [], suggestN=len(keep["places"]) if keep else 0,
          why=why, devs=devs, on=on, fg=fg, comps=row["comps"],
          acts=[f"Đổi về {tname(toks, suggest)}", "Giữ, có lý do…", "Thêm token mới…"],
          vals=_role_vals(toks, [suggest] + [d["token"] for d in devs], on, fg, prop))
    return table


def _role_vals(toks, names, on, fg, prop):
    out = {}
    for n in names:
        l, d = resolve(toks, n, "light", "web"), resolve(toks, n, "dark", "web")
        ol, od = resolve(toks, on, "light", "web"), resolve(toks, on, "dark", "web")
        fl, fd = resolve(toks, fg, "light", "web"), resolve(toks, fg, "dark", "web")
        out[n] = {"l": l, "d": d, "cl": contrast(fl, l) if prop == "nền" else contrast(l, ol),
                  "cd": contrast(fd, d) if prop == "nền" else contrast(d, od)}
    return out


# phân loại token thừa, token trùng
UNUSED_SUSPECT = {
    "color-accent-bg-subtle": "DEC-316 tự thêm cho dòng bảng đang chọn; bảng chưa có component nào dựng.",
    "color-accent-solid-hover": "DEC-316 tự thêm; công tắc, ô chọn đang dùng action/primary-hover thay vì token này.",
    "color-accent-solid-pressed": "DEC-316 tự thêm; công tắc, ô chọn đang dùng action/primary-pressed thay vì token này.",
    "color-accent-text": "DEC-316 tự thêm cho chữ liên kết, mã chứng từ; liên kết đang dùng text/primary, text/secondary.",
    "color-accent-text-hover": "DEC-316 tự thêm; đi đôi với accent/text, cùng chưa ai dùng.",
    "color-bg-skeleton": "DEC-316 tự thêm cho khối chờ tải; chưa component nào vẽ skeleton.",
    "color-fg-inverse": "color.md ghi dùng ở Tooltip, nút Primary, nhưng hai nơi đó đang tô icon bằng text/inverse.",
    "color-border-secondary_alt": "color.md ghi chỉ dùng cho menu nổi, nhưng menu nổi đang dùng border/secondary.",
}
DUP_REAL = {
    frozenset(("color-shadow-md-soft", "color-shadow-sm")): "Hai màu bóng giống nhau ở cả Sáng và Tối; không phải tên Untitled nên không có lý do giữ riêng theo chuẩn.",
    frozenset(("color-text-placeholder", "color-text-quaternary", "color-text-tertiary", "color-utility-neutral-500")): "text/tertiary và text/quaternary là hai bậc khác nhau theo tên, nhưng cùng một màu nên bậc này không nhạt hơn bậc kia.",
    frozenset(("color-action-secondary", "color-bg-disabled", "color-bg-secondary_hover", "color-bg-selected", "color-bg-skeleton", "color-bg-tertiary", "color-utility-neutral-100")): "color.md ghi action/secondary cũng là nền xám của trạng thái tắt, trùng đúng mục đích bg/disabled.",
    frozenset(("color-action-secondary-hover", "color-bg-pressed", "color-bg-quaternary")): "Hai vai đang bấm (action/secondary-hover cho nút Tertiary, bg/pressed cho dòng) cùng màu; nút Tertiary đang dùng cả hai tùy phương án.",
}


def classify_unused(n, t, purpose):
    if n in UNUSED_SUSPECT:
        return "suspect", UNUSED_SUSPECT[n]
    if t["tier"] == "brand":
        return "keep", "Thang 11 bậc của màu khách (DEC-167, DEC-168). Component không gọi thẳng, đi qua color/accent/* (color.md mục 3.5)."
    if n.startswith("color-utility-"):
        if "biểu đồ" in purpose:
            return "keep", "Thang utility của Untitled (DEC-320), bậc 500 để dành cho chuỗi biểu đồ; chưa có component biểu đồ."
        return "keep", "Thang utility của Untitled (DEC-320): giữ đủ bậc, chưa cần dùng."
    if "DEC-320" in purpose:
        return "keep", f"Token theo chuẩn Untitled, DEC-320 cố ý thêm: {purpose.split(' (DEC')[0]}."
    if not purpose:
        return "suspect", "Không có dòng nào trong color.md nói token này để làm gì."
    return "suspect", f"Không thuộc nhóm DEC-320 giữ sẵn: {purpose.split(' (DEC')[0]}."


def classify_dup(ns, purposes):
    fs = frozenset(ns)
    if fs in DUP_REAL:
        return "real", DUP_REAL[fs]
    fams = {n.removeprefix("color-").split("-")[0] for n in ns}
    if any(n.startswith("color-utility-") for n in ns):
        return "intent", "Có token thang utility đứng cùng token theo vai. Untitled tách hai lớp này (DEC-320), trùng giá trị là bình thường."
    if len(fams) > 1:
        return "intent", "Khác nhóm (" + ", ".join(sorted(fams)) + "): tên theo vai, trùng màu là do vai trùng, đổi một vai không kéo vai kia."
    if any(re.search(r"_(hover|pressed)$|-(hover|pressed)$", n) for n in ns):
        return "intent", "Có token trạng thái: tên theo Untitled, giữ để sau này chỉnh riêng trạng thái được."
    return "intent", "Cùng nhóm nhưng color.md ghi mục đích khác nhau cho từng token."


def color_purposes():
    """token css → cột Mục đích trong color.md."""
    md = (ROOT / "design-system/foundations/color.md").read_text(encoding="utf-8")
    return {css(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\| `(color/[^`]+)` \| [^|]+\| [^|]+\| (.*?) \|$", md, re.M)}


def stale_findings(hits, uni, F):
    by_file = defaultdict(list)
    for (path, old), h in hits.items():
        by_file[path].append({"old": old, "new": h["new"], "count": h["count"], "lines": h["lines"][:12], "pattern": h["pattern"]})
    for path, items in sorted(by_file.items()):
        items.sort(key=lambda x: x["old"])
        stem = Path(path).parent.name if path.endswith("page.json") else Path(path).stem
        comp = stem if stem in uni else None
        if comp:
            for it in items:
                short_ = lambda x: x.removeprefix("color/")
                F(f"stale-name--{comp}--{slugify(path.rsplit('.', 1)[-1])}--{slugify(it['old'])}", "stale-name", f"{it['old']} → {it['new']}", color=True, comp=comp,
                  where=path, items=[it], acts=[f"Đổi sang {short_(it['new'])}", "Giữ, có lý do…"])
        else:
            n = sum(i["count"] for i in items)
            F(f"stale-name--{slugify(path)}", "stale-name", f"{path}: {len(items)} tên cũ, {n} chỗ", color=True, where=path, items=items,
              acts=["Đổi hết sang tên mới", "Giữ, có lý do…"])


def color_matrix(comps, scans, pages, findings, toks):
    """Mỗi component một dòng tình trạng màu. Việc nhiều xếp trên."""
    r = dd.reg()
    fv = dd.fversions()
    changes = dd.direct_changes(r, fv)
    out = []
    for s, c in comps.items():
        fs = [f for f in findings if f.get("comp") == s and f.get("color")]
        alias = [f for f in fs if f["kind"] == "alias"]
        alias_todo = [f for f in alias if f.get("sub") != "switch"]
        lit = sum(f.get("count", 0) + f.get("html", 0) for f in fs if f["kind"] == "literal")
        stale = sum(i["count"] for f in fs if f["kind"] == "stale-name" for i in f["items"])
        dev = sum(1 for f in findings if f["kind"] == "role" for d in f["devs"] for p in d["places"] if p["comp"] == s)
        sc = scans.get(s)
        good = total = 0
        if sc:
            switch = {f["alias"] for f in alias if f.get("sub") == "switch"}
            for row in sc["rows"]:
                if "dark" in parse_selector(row["sel"])["flags"]:
                    continue
                col_alias = [a for a in row["aliases"] if a in c["local"] and any(f["alias"] == a for f in alias)]
                if not row["cols"] and not col_alias and not row["lits"]:
                    continue
                total += 1
                if row["cols"] and not row["lits"] and all(a in switch for a in col_alias) or (not row["cols"] and col_alias and all(a in switch for a in col_alias) and not row["lits"]):
                    good += 1
            source = "css"
        else:
            names = [n for n in c["used"] if toks[n]["group"] == "color"]
            good, total = sum(1 for n in names if toks[n]["tier"] in ("semantic", "brand")), len(names) + stale
            source = "md"
        ch = changes.get(s, [])
        col_stale = any(t == "foundation" and d == "color" for t, d, _, _ in ch)
        md = dd.md_of(s)
        status = None
        if md:
            head = md.read_text(encoding="utf-8")[:400]
            m, prev = re.search(r"^status: (.+)$", head, re.M), re.search(r"^status_prev: (.+)$", head, re.M)
            status = m.group(1) if m else None
            if prev:
                status = f"{status} (trước đó {prev.group(1)})"
        elif s in pages:
            status = "trang brainstorm, chưa có spec md"
        out.append({"slug": s, "group": c["group"], "src": c["src"], "source": source, "good": good, "total": total,
                    "pct": round(100 * good / total) if total else None, "alias": len(alias_todo), "aliasOk": len(alias) - len(alias_todo),
                    "literal": lit, "stale": stale, "role": dev, "deps": len(ch), "colorStale": col_stale, "status": status,
                    "pickSrc": scans[s]["pickSrc"] if s in scans else None,
                    "work": len(alias_todo) + lit + stale + dev})
    out.sort(key=lambda x: (-x["work"], -x["deps"], x["slug"]))
    return out


def norm_hex(h):
    m = re.fullmatch(r"#([0-9a-f]{3})", h)
    return "#" + "".join(c * 2 for c in m.group(1)) if m else h


# ── build ───────────────────────────────────────────────────────────────────
def build():
    toks = parse_tokens()
    uni = dd.universe()
    comps = {s: {**scan_component(s, toks), "group": u["group"]} for s, u in uni.items()}
    direct, via = defaultdict(set), defaultdict(set)
    for s, c in comps.items():
        for n in c["used"]:
            direct[n].add(s)
            for r in closure(toks, n):
                via[r].add(s)
    hidx = hex_index(toks)
    findings = []
    kits, chrome, _ = shared_rules()
    scans = {}
    pages = {}
    for s in uni:
        pj = dd.COMP / "_work" / s / "page.json"
        if pj.exists():
            pages[s] = json.loads(pj.read_text())
            scans[s] = color_scan(s, pages[s], toks, kits, chrome)
            scans[s]["aliases"] = resolve_aliases(scans[s], toks)
    purposes = color_purposes()

    def F(fid, kind_, title, **kw):
        findings.append({"id": fid, "kind": kind_, "title": title, **kw})

    for s, pg in pages.items():
        for decl, cnt in raw_motion(pg).items():
            F(f"rawmotion--{s}--{decl}", "rawmotion", f"{s}: {decl} ({cnt} chỗ)", comps=[s], group="motion")

    tok_rows = []
    for n, t in toks.items():
        vals = {f"{a}-{b}": resolve(toks, n, a, b) for a, b in CTXS}
        users = sorted(direct[n] | via[n])
        tok_rows.append({"name": n, "tier": t["tier"], "group": t["group"], "kind": kind(vals["light-web"]),
                         "raw": t["defs"][0][1] if t["defs"] else "", "refs": sorted(t["refs"]),
                         "vals": vals, "direct": sorted(direct[n]), "via": sorted(via[n] - direct[n]),
                         "style": bool(t.get("style")), "coll": t["coll"], "jname": t["jname"],
                         "refBy": sorted(x for x, u in toks.items() if n in u["refs"]),
                         "rawVal": bool(not t["refs"] and t["tier"] != "primitive" and not t.get("style")),
                         "c": t["group"] == "color" or kind(vals["light-web"]) == "color"})
        if n.startswith(BRAND_ONLY):  # không xét thừa/lẻ: không phải token cho component
            if direct[n]:
                F(f"brandleak--{n}", "brandleak", f"{n} ← {', '.join(sorted(direct[n]))}", token=n, comps=sorted(direct[n]), group=t["group"])
            continue
        if t["tier"] == "primitive":
            continue
        if not users:
            ex = {}
            if t["group"] == "color":
                pp = purposes.get(n, "")
                sub, why = classify_unused(n, t, pp)
                ex = {"sub": sub, "reason": why, "purpose": pp}
            F(f"unused--{n}", "unused", n, token=n, tier=t["tier"], group=t["group"], **ex)
        elif t["tier"] == "semantic" and len(users) == 1:
            F(f"single--{n}", "single", n, token=n, comps=users, group=t["group"])
    tier_checks(toks, direct, via, hidx, F)
    # trùng giá trị giữa token semantic cùng nhóm (khác tầng primitive, khác text style)
    sig = defaultdict(list)
    for r in tok_rows:
        if r["tier"] == "semantic" and not r["style"] and r["vals"]["light-web"]:
            sig[(r["group"], tuple(r["vals"][f"{a}-{b}"] for a, b in CTXS))].append(r["name"])
    for (g, vs), ns in sig.items():
        if len(ns) > 1:
            ex = {}
            if g == "color":
                sub, why = classify_dup(ns, purposes)
                ex = {"sub": sub, "reason": why, "purposes": {n: purposes.get(n, "") for n in sorted(ns)}, "valueDark": vs[1]}
            F("dup--" + "--".join(sorted(ns))[:120], "dup", " = ".join(sorted(ns)), tokens=sorted(ns), group=g, value=vs[0],
              comps=sorted({c for n in ns for c in direct[n] | via[n]}), **ex)
    for s, c in comps.items():
        for n in c["used"]:
            if toks[n]["tier"] == "primitive" and not n.startswith(("font-", "width-")):
                alt = [x for x in hidx.get((resolve(toks, n, "light", "web") or "").lower(), []) if toks[x]["tier"] == "semantic"]
                F(f"prim--{s}--{n}", "prim", f"{s} gọi {n}", comp=s, prim=n, where=c["src"], alt=alt[:3])
        for a, v in c["local"].items():
            refs = re.findall(r"var\(--([\w-]+)", v)
            pg = pages.get(s) or {}
            hay = "\n".join(walk_strings([pg.get(k) for k in ("css", "cssScreen", "preview", "proto")]))
            uses = len(re.findall(r"var\(--" + re.escape(a) + r"\b", hay))
            fb = re.search(r"var\(--" + re.escape(a) + r"\s*,\s*var\(--([\w-]+)\)\)", hay)
            info = alias_info(a, scans[s]["aliases"].get(a, []) if s in scans else [], toks, uses, [v], fb.group(1) if fb else None)
            ex = {}
            if info.get("suggest"):
                ex = {"suggestName": tname(toks, info["suggest"]), "acts": [f"Thay bằng {tname(toks, info['suggest'])}", "Đưa lên tokens.css", "Giữ, có lý do…"]}
            F(f"alias--{s}--{a}", "alias", f"{s}: --{a}", comp=s, alias=a, value=v, maps=[r for r in refs if r in toks], **info, **ex)
        for n in c["unknown"]:
            F(f"unknown--{s}--{n}", "unknown", f"{s} gọi {n}", comp=s, token=n, where=c["src"])
        for h, k in sorted(c["literals"].items(), key=lambda x: -x[1]):
            F(f"literal--{s}--{re.sub(r'[^a-z0-9]+', '-', h)}", "literal", f"{s}: {h}", comp=s, value=h, count=k,
              alt=hidx.get(norm_hex(h), [])[:3], color=True, html=c["literalsHtml"].get(h, 0))
        for h, k in sorted(c["literalsHtml"].items(), key=lambda x: -x[1]):
            if h not in c["literals"]:
                F(f"literal--{s}--{re.sub(r'[^a-z0-9]+', '-', h)}", "literal", f"{s}: {h}", comp=s, value=h, count=0, html=k,
                  alt=hidx.get(norm_hex(h), [])[:3], color=True)
    stale_hits, ambiguous, _table = stale_scan(toks, uni)
    stale_findings(stale_hits, uni, F)
    # bỏ tên cũ khỏi "token không tồn tại": đã báo đúng hơn ở stale-name, kèm tên mới
    stale_css = {css(k) for k in _table} | {css(k).removeprefix("color-") for k in _table}
    findings[:] = [f for f in findings if not (f["kind"] == "unknown" and f.get("token") in stale_css)]
    for c in comps.values():
        c["unknown"] = [n for n in c["unknown"] if n not in stale_css]
    roles, unresolved, switched = role_analysis(scans, toks, uni)
    role_table = role_findings(roles, toks, F)
    for f in findings:  # cờ phạm vi Màu
        if "color" in f:
            continue
        k = f["kind"]
        if k in ("unused", "single", "dup"):
            f["color"] = f.get("group") == "color"
        elif k == "prim":
            f["color"] = toks.get(f["prim"], {}).get("group") == "color"
        elif k == "unknown":
            f["color"] = str(f.get("token", "")).startswith(("color-", "chip-", "status-", "chart-", "surface-"))
        elif k == "skip":
            f["color"] = any(toks.get(css(x), {}).get("group") == "color" for x in f.get("prim", []))
        else:
            f["color"] = False
    matrix = color_matrix(comps, scans, pages, findings, toks)
    comp_rows = []
    for s, c in sorted(comps.items()):
        g = Counter(toks[n]["group"] for n in c["used"])
        comp_rows.append({"slug": s, "group": c["group"], "src": c["src"], "used": c["used"], "unknown": c["unknown"],
                          "local": c["local"], "literals": c["literals"], "literalsHtml": c["literalsHtml"], "bare": c["bare"], "byGroup": dict(g),
                          "issues": sum(1 for f in findings if f.get("comp") == s or s in (f.get("comps") or []) and f["kind"] == "role"),
                          "issuesColor": sum(1 for f in findings if f.get("color") and (f.get("comp") == s or (f["kind"] == "role" and s in f.get("comps", [])))
                                             and f.get("sub") not in ("keep", "intent", "switch"))})
    counts = Counter(f["kind"] for f in findings)
    tiers = Counter(r["tier"] for r in tok_rows if not r["style"])
    tiers["style"] = sum(1 for r in tok_rows if r["style"])
    used_f = sum(1 for r in tok_rows if r["tier"] != "primitive" and not r["style"] and (r["direct"] or r["via"]))
    stats = {"tokens": dict(tiers), "styles": sum(1 for r in tok_rows if r["style"]), "components": len(comps),
             "usedPct": round(100 * used_f / max(1, tiers["semantic"] + tiers["component"])), "findings": dict(counts)}
    colf = [f for f in findings if f.get("color")]
    stats["color"] = {"findings": dict(Counter(f["kind"] for f in colf)),
                      "todo": dict(Counter(f["kind"] for f in colf if f.get("sub") not in ("keep", "intent", "switch"))),
                      "noact": dict(Counter(f["kind"] for f in colf if f.get("sub") in ("keep", "intent", "switch"))),
                      "subs": {k: dict(Counter(f.get("sub") for f in colf if f["kind"] == k)) for k in ("unused", "dup", "alias")},
                      "roleCertain": sum(1 for f in colf if f["kind"] == "role" and f["certain"]), "roles": len(role_table),
                      "rolesOk": sum(1 for r in role_table if not r["finding"]), "unresolved": len(unresolved), "viaSwitch": switched,
                      "total": len(colf)}
    spec, bundles = specimens(toks, findings)
    return {"date": TODAY, "groups": [[k, n] for k, n, _ in GROUPS], "stats": stats, "tokens": tok_rows,
            "components": comp_rows, "findings": findings, "specimens": spec, "bundles": bundles, "ladder": LADDER_NAME,
            "roles": role_table, "unresolved": unresolved, "matrix": matrix, "ambiguous": [a.removeprefix("color/") for a in ambiguous]}


def tier_checks(toks, direct, via, hidx, F):
    """skip / compraw — token tầng Component (6. Component sizes, 8. Component) phải trỏ Semantic (DEC-313)."""
    sem_by_pair = defaultdict(list)  # (Web, Mobile) → token semantic Platform cùng cặp (đã giải về primitive)
    pv = lambda v: v if isinstance(v, str) else next((t["jname"] for t in toks.values()
                                                      if t["coll"] == "0. Primitives" and t["jval"] == v
                                                      and t["jname"].startswith("space/")), v)
    for n, t in toks.items():
        if t["tier"] == "semantic" and isinstance(t["jval"], dict) and "Web" in t["jval"]:
            sem_by_pair[(pv(t["jval"]["Web"]), pv(t["jval"]["Mobile"]))].append(t["jname"])
    users = lambda n: sorted(direct[n] | via[n])
    raw_by_val = defaultdict(list)
    for n, t in sorted(toks.items()):
        if t["tier"] != "component" or not t["coll"]:
            continue
        jv = t["jval"] if isinstance(t["jval"], dict) else {"Value": t["jval"]}
        raw = {m: v for m, v in jv.items() if isinstance(v, (int, float))}
        if raw:
            raw_by_val[tuple(sorted(set(raw.values())))].append(t["jname"])
        bad = sorted({v for v in jv.values() if isinstance(v, str) and toks.get(css(v), {}).get("tier") == "primitive"})
        if bad:
            if "Web" in jv:
                alt = sem_by_pair.get((pv(jv["Web"]), pv(jv["Mobile"])), [])
            else:
                alt = [toks[x]["jname"] or x for x in hidx.get((resolve(toks, css(bad[0]), "light", "web") or "").lower(), [])
                       if toks[x]["tier"] == "semantic"]
            F(f"skip--{n}", "skip", f"{t['jname']} → {', '.join(bad)}", token=n, prim=bad, alt=alt[:3], comps=users(n))
    LAD = {0: "none", 2: "xxs", 4: "xs", 6: "sm", 8: "md", 12: "lg", 16: "xl", 20: "2xl", 24: "3xl", 32: "4xl", 40: "5xl",
           48: "6xl", 64: "7xl", 80: "8xl", 96: "9xl", 128: "10xl", 160: "11xl"}

    def near(x):
        if not isinstance(x, (int, float)) or x < 0 or x < 1 and x != 0:
            return "không trỏ được (số âm / độ mờ: biến Figma không tính toán)"
        lo = max([k for k in LAD if k <= x], default=0); hi = min([k for k in LAD if k >= x], default=160)
        return " · ".join(sorted({f"{LAD[k]} ({k})" for k in (lo, hi)}, key=lambda t: int(t.split("(")[1][:-1])))
    for vs, ns in sorted(raw_by_val.items(), key=lambda kv: kv[0]):
        v = " / ".join(str(x) for x in vs)
        same = sem_by_pair.get((pv(vs[0]), pv(vs[-1])), []) if len(vs) <= 2 else []
        F(f"compraw--{v}", "compraw", f"{v} — {len(ns)} token", value=v, tokens=ns, alt=same[:3],
          near=" / ".join(near(x) for x in vs))


LADDER = [0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128, 160]
LADDER_NAME = dict(zip(LADDER, ["none", "xxs", "xs", "sm", "md", "lg", "xl", "2xl", "3xl", "4xl", "5xl", "6xl", "7xl", "8xl",
                                "9xl", "10xl", "11xl"]))


def specimens(toks, findings):
    """Dữ liệu preview cho mục skip / compraw: phần nào của component, giá trị theo mode, phương án đổi.
    live = CSS trang _work gọi var(--token) → trang dựng component thật (bundle) và khoanh selector; không có → hình mô phỏng."""
    want = set()
    for f in findings:
        if f["kind"] in ("skip", "compraw"):
            for t in f.get("tokens") or [f.get("token")]:
                if t:
                    want.add(css(t.split(" (")[0]))
    mds = [(m, m.read_text(encoding="utf-8")) for m in sorted(dd.COMP.glob("*/*.md")) if not m.parent.name.startswith("_")]
    mds += [(m, m.read_text(encoding="utf-8")) for m in sorted((ROOT / "design-system/foundations").glob("*.md"))]
    pages = {}
    for pj in sorted((dd.COMP / "_work").glob("*/page.json")):
        if pj.parent.name in dd.WORK_SKIP:
            continue
        pg = json.loads(pj.read_text())
        c = re.sub(r"--([\w-]+)\s*:\s*[^;{}]*;?", lambda m: "" if m.group(1) in toks or m.group(1).startswith(RETIRED) else m.group(0),
                   pg.get("css") or "")
        pages[pj.parent.name] = (pg, c)
    out, bundles = {}, {}
    for n in sorted(want):
        t = toks.get(n)
        if not t:
            continue
        jn = t["jname"] or n
        vals = {m: resolve(toks, n, "light", m.lower()) for m in ("Web", "Mobile")}
        num = {m: (float(re.sub(r"px$", "", v)) if v and re.fullmatch(r"-?\d+(\.\d+)?(px)?", v.strip()) else None)
               for m, v in vals.items()}
        part, src = "", ""
        for m, txt in mds:
            for line in txt.split("\n"):
                short = jn.split("/", 1)[-1]
                if line.startswith("|") and (f"`{jn}`" in line or (m.parent.name in ("base", "application") and f"`{short}`" in line)):
                    cells = [c.strip() for c in line.strip("|").split("|")]
                    # spec component: cột đầu là tên phần; foundations/vehicles: cột cuối là "dùng cho"
                    part = cells[0] if m.parent.name in ("base", "application") else cells[-1]
                    part = re.sub(r"`|\*\*", "", part)[:90]
                    if part in ("Chính component đó", "Component, màn", "Component, màn, theo vai mục 3.5"):  # bảng tầng §2, không phải tên phần
                        part = ""
                        continue
                    src = dd.rel(m)
                    break
            if part:
                break
        live = None
        for slug, (pg, c) in pages.items():
            rules = [(sel.strip(), body) for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", c) if f"var(--{n}" in body]
            if not rules:
                continue
            sels = sorted({x.strip() for sel, _ in rules for x in sel.split(",") if x.strip() and not x.strip().startswith("@")})
            props = sorted({pp.split(":")[0].strip() for _, body in rules for pp in body.split(";") if f"var(--{n}" in pp})
            if not part:
                part = next((v.get("part") for v in pg.get("values") or [] if isinstance(v, dict)
                             and (v.get("token") or "").replace("/", "-") == n), "") or ""
            live = {"comp": slug, "sels": sels[:6], "props": props}
            if slug not in bundles:
                blocks = (pg.get("preview") or {}).get("blocks") or []
                bundles[slug] = {"css": c, "html": next((b.get("html") for b in blocks if b.get("html")), "")}
            break
        if not part:
            part = part_from_name(jn)
        elif not part.lower().startswith(jn.split("/")[0].replace("-", " ")):
            part = f"{jn.split('/')[0].replace('-', ' ').capitalize()} · {part}"
        out[n] = {"jname": jn, "vals": vals, "num": num, "part": part, "src": src, "live": live,
                  "kind": spec_kind(jn)}
    return out, bundles


VI = {"size": "cỡ", "height": "cao", "width": "rộng", "radius": "bo góc", "overlap": "đè", "status": "chấm trạng thái",
      "edit": "nút đổi ảnh", "icon": "icon", "spinner": "vòng tải", "group": "nhóm", "label": "nhãn", "thumb": "ảnh nhỏ",
      "q": "khung ảnh", "default": "mặc định", "max": "tối đa", "min": "tối thiểu", "gap": "khoảng", "padding": "lề", "w": "rộng", "h": "cao"}


def part_from_name(jn):
    head, *rest = jn.split("/")
    words = [w for seg in rest for w in seg.split("-")]
    sizes = [w.upper() for w in words if w in ("xs", "sm", "md", "lg", "xl", "xxl")]
    desc = " ".join(VI.get(w, w) for w in words if w not in ("xs", "sm", "md", "lg", "xl", "xxl"))
    return f"{head.replace('-', ' ').capitalize()} · {desc}" + (f" {' '.join(sizes)}" if sizes else "") + " (theo tên token)"


def spec_kind(jn):
    k = jn.split("/")[-1] + "/" + jn
    for key, pat in (("opacity", r"opacity"), ("radius", r"radius"), ("font", r"font-size|subtitle-size"),
                     ("line", r"line-height"), ("border", r"border-width|divider-width|ring|status-border"),
                     ("overlap", r"overlap"), ("gap", r"gap|offset"), ("padding", r"padding|inset"),
                     ("width", r"width|-w$"), ("height", r"height|-h$"), ("size", r"size|thumb|scale|count-size|cell")):
        if re.search(pat, k):
            return key
    return "size"


def with_history(data):
    old = json.loads(OUT_J.read_text()) if OUT_J.exists() else {}
    prev = {f["id"] for f in old.get("findings", [])}
    cur = {f["id"] for f in data["findings"]}
    base = old.get("base_ids") if old.get("date") == TODAY else sorted(prev)  # quét lại trong ngày: so với hôm trước
    base = set(base or [])
    for f in data["findings"]:
        f["new"] = bool(base) and f["id"] not in base
    data["base_ids"] = sorted(base) if base else sorted(cur)
    data["resolved"] = sorted(base - cur)
    hist = [h for h in old.get("history", []) if h["date"] != TODAY]
    hist.append({"date": TODAY, **data["stats"]["findings"], "total": len(cur), "colorTodo": sum(data["stats"]["color"]["todo"].values())})
    data["history"] = hist[-30:]
    data["artifact"] = old.get("artifact")
    return data


# ── trang ───────────────────────────────────────────────────────────────────
PAGE_CSS = r"""
*{box-sizing:border-box}body{margin:0;font:14px/20px Inter,system-ui,sans-serif;color:#171717;background:#F5F7FB}
.band{background:#0036B5;color:#fff;padding:20px 32px;display:flex;align-items:center;gap:14px}
.band svg{width:36px;height:36px;flex:none}.band h1{margin:0;font:400 26px/32px "Cal Sans",Inter,sans-serif}.band p{margin:2px 0 0;opacity:.85}
.wrap{max-width:1240px;margin:0 auto;padding:16px 24px 80px}
h2{font:400 20px/28px "Cal Sans",Inter,sans-serif;margin:22px 0 10px;display:flex;align-items:center;gap:8px}
h2::before{content:"";width:10px;height:10px;background:#00A2FF;flex:none}
mark{background:color-mix(in srgb,#00A2FF 28%,transparent);color:inherit;padding:0 2px;border-radius:3px}
.muted{color:#64748B}.small{font-size:12px;line-height:16px}code,.mono{font:12px/16px "JetBrains Mono",monospace}
.kpis{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin:14px 0}
.kpi{background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:12px 14px;cursor:pointer;text-align:left;font:inherit;color:inherit}
.kpi b{display:block;font:400 26px/32px "Cal Sans",Inter,sans-serif}.kpi.warn b{color:#B54708}.kpi.bad b{color:#B42318}.kpi.ok b{color:#067647}
.kpi span{font-size:12px;color:#475569}
.tabs{position:sticky;top:0;z-index:6;background:#F5F7FB;display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding:10px 0;border-bottom:1px solid #E2E8F0}
.tabs button,.chipbtn{border:1px solid #CBD5E1;background:#fff;border-radius:999px;padding:6px 12px;font:600 13px Inter;cursor:pointer;color:#171717}
.tabs button[aria-pressed=true],.chipbtn[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}
.tabs .sp{flex:1}.filters{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:12px 0}
.filters select,.filters input{border:1px solid #CBD5E1;border-radius:10px;padding:6px 10px;font:13px Inter;background:#fff}
.filters input{min-width:220px}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #E2E8F0;border-radius:14px;overflow:hidden}
th,td{padding:8px 10px;border-bottom:1px solid #EEF2F6;text-align:left;vertical-align:top}
th{font:600 12px/16px Inter;color:#475569;background:#F8FAFC}
tr.g td{background:#F1F5FF;font:600 13px Inter;color:#0036B5}
.pv{width:44px;height:28px;border-radius:6px;border:1px solid #E2E8F0;display:grid;place-items:center;overflow:hidden;background:#fff}
.pv i{display:block}.pv .sw{width:100%;height:100%}.pv .bar{height:8px;background:#0036B5;border-radius:2px;max-width:40px}
.pv .rd{width:30px;height:20px;background:#E7EFFD;border:1.5px solid #0036B5}.pv .sh{width:26px;height:16px;background:#fff;border-radius:4px}
.pv .ag{font-size:14px;line-height:1}
.tg{display:inline-flex;align-items:center;border-radius:999px;padding:1px 8px;font:600 11px/18px Inter;white-space:nowrap;margin:1px 2px 1px 0}
.t-primitive{background:#F1F5F9;color:#475569}.t-semantic{background:#E7EFFD;color:#0036B5}.t-component{background:#F4F3FF;color:#5925DC}
.k-unused{background:#F1F5F9;color:#475569}.k-single{background:#FFFAEB;color:#B54708}.k-prim{background:#FEF3F2;color:#B42318}
.k-alias{background:#FEF3F2;color:#B42318}.k-unknown{background:#FEF3F2;color:#B42318}.k-literal{background:#FFF4ED;color:#C4320A}.k-dup{background:#F0F9FF;color:#026AA2}
.new{background:#00A2FF;color:#fff}
.k-compraw{background:#FFFAEB;color:#B54708}.k-skip{background:#FEF3F2;color:#B42318}
.k-role{background:#E7EFFD;color:#0036B5}.k-stale-name{background:#FFF4ED;color:#C4320A}
.scopebar{display:flex;flex-wrap:wrap;align-items:center;gap:8px;background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:10px 14px;margin:14px 0 0}
.scopebar b{font:600 13px Inter}.scopebar button{border:1px solid #CBD5E1;background:#fff;border-radius:999px;padding:6px 14px;font:600 13px Inter;cursor:pointer;color:#171717}
.scopebar button[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}.scopebar .note{flex:1 1 320px;font-size:12px;line-height:17px;color:#475569}
.lead{background:#fff;border:1px solid #E2E8F0;border-left:4px solid #0036B5;border-radius:10px;padding:10px 14px;margin:10px 0;font-size:14px;line-height:21px}
.tk{display:flex;align-items:flex-start;gap:6px;flex-wrap:wrap;margin:3px 0;font-size:12px;line-height:18px}
.tk i{flex:none;width:14px;height:14px;border-radius:4px;border:1px solid rgba(0,0,0,.14);margin-top:2px}
.tk.good code{color:#067647;font-weight:600}.tk.off code{color:#B42318;font-weight:600}
.tk .pl{color:#64748B}.place{font:11px/16px "JetBrains Mono",monospace;color:#475569;margin:1px 0 1px 20px;word-break:break-all}
.unsure{background:#FFFAEB;color:#B54708}.sure{background:#ECFDF3;color:#067647}
.rp{display:grid;grid-template-columns:repeat(4,minmax(150px,1fr));gap:8px;margin-bottom:12px}.rp h5{grid-column:1/-1;margin:0;font:600 12px/18px Inter}
.rpc{border:1px solid #E2E8F0;border-radius:10px;overflow:hidden;background:#fff}.rpc>span{display:block;padding:4px 8px;font-size:11px;line-height:15px;color:#475569;border-bottom:1px solid #EEF2F6}
.rpc.after{border-color:#067647}.rpcell{height:78px;display:flex;align-items:center;justify-content:center;gap:8px;padding:10px}
.rps{padding:6px 12px;border-radius:8px;font:500 13px/18px Inter}.rpc small{display:block;padding:4px 8px;font:11px/15px "JetBrains Mono",monospace;color:#475569;border-top:1px solid #EEF2F6}
.rpc small b.low{color:#B42318}
.mx{font-size:13px;margin-bottom:8px}.mx td,.mx th{white-space:nowrap}.mx td.num,.mx th.num{text-align:right}.mx .zero{color:#94A3B8}.mx .hot{color:#B42318;font-weight:600}
.mxwrap{overflow:auto;border-radius:14px}.pct{display:inline-block;width:64px;height:6px;background:#EEF2F6;border-radius:3px;overflow:hidden;vertical-align:middle;margin-right:6px}.pct i{display:block;height:100%;background:#067647}
.tierbar{display:flex;gap:0;margin:8px 0 4px;border-radius:10px;overflow:hidden;border:1px solid #E2E8F0;background:#fff}
.tierbar div{flex:1;padding:10px 14px;border-right:1px solid #E2E8F0}.tierbar div:last-child{border:0}
.tierbar b{font:400 22px/28px "Cal Sans",Inter,sans-serif}.tierbar .arw{flex:0 0 28px;display:grid;place-items:center;color:#94A3B8;padding:0}
.fam{background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:12px 14px;margin-bottom:10px}
.fam h3{margin:0 0 8px;font:600 14px Inter;display:flex;gap:8px;align-items:center}
.cells{display:grid;grid-template-columns:repeat(auto-fill,minmax(98px,1fr));gap:6px}
.cell{border:1px solid #E2E8F0;border-radius:10px;padding:6px;font-size:11px;line-height:14px;cursor:pointer;background:#fff;text-align:left}
.cell .sw{height:34px;border-radius:6px;margin-bottom:4px;border:1px solid rgba(0,0,0,.06)}
.cell .dm{height:34px;display:flex;align-items:center;margin-bottom:4px}.cell .dm i{display:block;height:10px;background:#0036B5;border-radius:2px;max-width:100%}
.cell .dm .rd{width:44px;height:30px;background:#E7EFFD;border:1.5px solid #0036B5}
.cell b{display:block;font:600 11px/14px "JetBrains Mono",monospace}.cell.zero{opacity:.45}.cell.badc{outline:2px solid #F04438}
.cell[aria-expanded=true]{outline:2px solid #0036B5}
.detail{background:#F8FAFC;border:1px solid #E2E8F0;border-radius:10px;padding:10px 12px;margin-top:8px;font-size:12px}
.ref.t-semantic,.ref.t-component,.ref.t-primitive{font:11px/16px "JetBrains Mono",monospace}
.warnraw{color:#B54708;font-weight:600}
.pvbtn{border:1px solid #0036B5!important;color:#0036B5!important}
.pvbox{grid-column:1/-1;background:#F8FAFC;border:1px solid #E2E8F0;border-radius:12px;padding:12px;margin-top:4px}
.sprow{margin-bottom:14px}.sprow:last-child{margin-bottom:0}
.sphead{font-size:12px;line-height:18px;margin-bottom:6px}.sphead b{font-size:13px}
.spmark{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;background:#F04438;color:#fff;font:700 11px Inter;margin-right:6px}
.opts{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px}
.opt{background:#fff;border:1px solid #E2E8F0;border-radius:10px;overflow:hidden}
.opt.cur{border-color:#0036B5}.opt h4{margin:0;padding:6px 10px;font:600 12px/16px Inter;background:#F1F5F9;display:flex;justify-content:space-between;gap:6px}
.opt.cur h4{background:#E7EFFD;color:#0036B5}.opt .delta{font-weight:500;color:#B54708}.opt .same{font-weight:500;color:#067647}
.stage{height:150px;display:grid;place-items:center;overflow:hidden;position:relative;background:repeating-conic-gradient(#fff 0 25%,#FAFBFC 0 50%) 0 0/16px 16px}
.stage.live{place-items:center;overflow:auto;padding:22px 30px;height:auto;min-height:150px;max-height:320px}
.sch{position:relative;display:inline-flex;align-items:center;justify-content:center}
.sch .box{background:#E7EFFD;border:1px solid #93B9FF}.sch .hl{background:rgba(240,68,56,.32)}
.sch .dim{position:absolute;font:600 10px/12px Inter;color:#B42318;white-space:nowrap}
body.noann .sch .hl{background:transparent}body.noann .sch .dim,body.noann .sch i{display:none}
.opt .cap{padding:6px 10px;font-size:11px;line-height:15px;color:#475569;border-top:1px solid #EEF2F6}
.cmp{display:inline-block;border:1px solid #CBD5E1;border-radius:6px;padding:0 6px;margin:1px 2px 1px 0;font:12px/18px Inter;background:#fff;cursor:pointer}
.cmp.via{border-style:dashed;color:#64748B}
.vals{font:11px/16px "JetBrains Mono",monospace;color:#475569}.vals b{color:#171717;font-weight:600}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:12px}
.card{background:#fff;border:1px solid #E2E8F0;border-radius:14px;padding:14px}
.card h3{margin:0 0 2px;font:600 15px/20px Inter;display:flex;justify-content:space-between;gap:8px}
.meter{display:flex;height:8px;border-radius:4px;overflow:hidden;background:#EEF2F6;margin:8px 0}
.meter i{display:block;height:100%}
.sec{background:#fff;border:1px solid #E2E8F0;border-radius:14px;margin-bottom:12px;overflow:hidden}
.sec>summary{padding:12px 16px;cursor:pointer;font:600 14px Inter;display:flex;gap:8px;align-items:center;list-style:none}
.sec>summary::-webkit-details-marker{display:none}.sec>summary::before{content:"▸";color:#0036B5}.sec[open]>summary::before{content:"▾"}
.sec .why{padding:0 16px 10px;color:#475569;font-size:13px}
.item{border-top:1px solid #EEF2F6;padding:10px 16px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px 16px}
.item .act{display:flex;gap:4px;flex-wrap:wrap;justify-content:flex-end;align-self:start;align-items:flex-start;align-content:flex-start;max-width:300px}
.item .act button{border:1px solid #CBD5E1;background:#fff;border-radius:999px;padding:3px 10px;font:600 12px Inter;cursor:pointer}
.item .act button[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}
.item textarea{grid-column:1/-1;min-height:34px;border:1px solid #CBD5E1;border-radius:8px;padding:6px 8px;font:12px Inter;display:none}
.item.open textarea{display:block}.item.done{background:#F6FEF9}
.saved{font-size:11px;color:#067647}.hide{display:none!important}
.hist{display:flex;gap:4px;align-items:flex-end;height:40px}.hist i{display:block;width:14px;background:#0036B5;border-radius:2px 2px 0 0}
@media (max-width:700px){.rp{grid-template-columns:repeat(2,minmax(0,1fr))}.wrap{padding:12px}.band{padding:16px}.item{grid-template-columns:1fr}.item .act{justify-content:flex-start;max-width:none}
.hidem{display:none}.cards{grid-template-columns:1fr}}
"""

PAGE_JS = r"""
const D=JSON.parse(document.getElementById("data").textContent);
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],E=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const GN=Object.fromEntries(D.groups); const gname=g=>GN[g]||(g.startsWith("c:")?"Component · "+g.slice(2):g);
let SCOPE="color";const inS=f=>SCOPE==="all"||f.color,NOACT=new Set(["keep","intent","switch"]),FX=Object.fromEntries(D.findings.map(f=>[f.id,f]));
const KN={rawmotion:"Chuyển động số trần",brandleak:"Component dùng màu thương hiệu",role:"Lệch vai","stale-name":"Tên cũ còn sót",compraw:"Component số trần",skip:"Component trỏ Primitive",unused:"Chưa dùng",single:"Lẻ — 1 component",prim:"Gọi thẳng primitive",alias:"Biến tự đặt",unknown:"Token không tồn tại",literal:"Màu viết trần",dup:"Trùng giá trị"};
const KWHY={
 role:"Cùng một <b>vai</b> (phần tử × thuộc tính × trạng thái) mà dùng <mark>2 token trở lên</mark>, hoặc lệch luật có căn cứ. Đề xuất ưu tiên luật trong <code>color.md</code>, <code>DEC-321</code>; không có luật thì lấy token nhiều nguồn dùng nhất. Kit dùng chung tính 1 nguồn.",
 "stale-name":"Tên màu đã bỏ ở <b>DEC-318</b> (bỏ tầng Component) và <b>DEC-320</b> (đổi tên theo Untitled) <mark>còn nằm trong tài liệu hoặc CSS</mark>. Tên mới lấy từ <code>components/_token-ledger.json</code>. Dev đọc md sẽ tìm không ra biến.",
 skip:"Token tầng <b>Component</b> (<code>6. Component sizes</code>) <b>trỏ thẳng Primitive</b>, trái <b>DEC-313</b>: token component chỉ được trỏ Semantic (<code>1.</code>–<code>5.</code>) hoặc Brand theo vai. Gợi ý = token Semantic cùng giá trị (màu: cùng Light; số đo: cùng cặp Web/Mobile). Không có gợi ý → cần <mark>thêm bậc Semantic</mark> hoặc đổi số.",
 compraw:"Token tầng <b>Component</b> ghi <b>số trần</b>, gom theo giá trị. Theo DEC-313 cũng phải trỏ Semantic. Gợi ý = Semantic cùng giá trị nếu có; không có → chọn bậc gần nhất hoặc thêm thang Semantic (vd <code>size/*</code> cho cỡ khối).",
 unused:"Token có trong tokens.css nhưng <b>không component nào dùng</b>, kể cả gián tiếp. Mục ở đây là <mark>nghi thừa hoặc nghi thiếu gắn</mark>; token theo chuẩn Untitled mà <code>DEC-320</code> cố ý giữ sẵn nằm ở phần không cần xử lý cuối trang.",
 single:"Token semantic <b>chỉ 1 component dùng</b>. Semantic phải dùng chung; chỉ 1 nơi dùng thường là <mark>token riêng lẻ</mark>: gộp vào token sẵn có, hoặc chuyển thành token component.",
 rawmotion:"<code>transition</code>, <code>animation</code> ghi số giây trần, không qua <code>--duration-*</code>, nên <mark>vẫn chạy khi bật giảm chuyển động</mark> (<b>DEC-333</b>).",
 brandleak:"Component gọi <b>--invlogis-*, --innvie-*</b>. Bộ này chỉ cho logo, trang giới thiệu, tài liệu (<b>DEC-261</b>); màu theo khách đi qua <code>color/accent/*</code>.",
 prim:"CSS hoặc spec của component <b>gọi thẳng primitive màu</b> (neutral-300, red-100…), trái <b>DEC-115</b>. Đổi Light/Dark hay đổi brand sẽ lệch. Nên đi qua token semantic.",
 alias:"Component <b>tự đặt biến cục bộ</b> (--fg2, --line…) thay vì gọi token hệ thống. Đây là nguồn chính của <mark>token riêng lẻ</mark>: thay bằng token hệ thống, hoặc đưa lên tokens.css nếu thật sự cần.",
 unknown:"Component <b>gọi tên token không có</b> trong tokens.css. Có thể tên cũ (l1), viết sai, hoặc token chưa tạo.",
 literal:"Màu <b>viết trần</b> (hex/rgb) trong css component, không qua token. Cột gợi ý là token có đúng giá trị đó.",
 dup:"Các token semantic <b>cùng nhóm, cùng giá trị ở cả 4 chế độ</b> (Light/Dark × Web/Mobile). Mục ở đây là <mark>nghi trùng thật</mark>; trùng do tên theo vai nằm ở phần không cần xử lý cuối trang."};
const KACT={compraw:["Trỏ Semantic cùng số","Làm tròn về bậc gần nhất…","Thêm bậc Semantic mới…","Ngoại lệ (giữ số, ghi lý do)…"],skip:["Trỏ Semantic gợi ý","Làm tròn về bậc gần nhất…","Thêm bậc Semantic mới…"],
 rawmotion:["Giữ","Đổi sang biến"],brandleak:["Giữ","Đổi sang token semantic"],unused:["Giữ","Bỏ token"],single:["Giữ","Gộp vào…","Chuyển thành token component"],prim:["Giữ","Đổi sang token semantic"],
 alias:["Thay bằng token hệ thống","Đưa lên tokens.css","Giữ (khung xem thử)"],unknown:["Sửa tên","Tạo token","Bỏ qua (spec cũ)"],
 literal:["Đổi sang token","Giữ (khung xem thử)"],dup:["Giữ cả hai","Gộp vào…"]};
KACT.role=["Giữ, có lý do…","Thêm token mới…"];KACT["stale-name"]=["Đổi sang tên mới","Giữ, có lý do…"];
const ORDER=["rawmotion","brandleak","role","stale-name","skip","compraw","prim","alias","unknown","literal","single","dup","unused"];
const TIERN={primitive:"Primitive",semantic:"Semantic",component:"Component token",brand:"Brand"};
let db=null,uid=null,curTier="semantic"; const ST={};
function kpis(){const rows=D.tokens.filter(r=>SCOPE==="all"||r.c),n=x=>rows.filter(r=>r.tier===x&&!r.style).length,st=rows.filter(r=>r.style).length;
 const k=(n,l,c,go)=>`<button class="kpi ${c}" data-go="${go}"><b>${n}</b><span>${l}</span></button>`;
 const tb=(n,l,sub,go)=>`<div role="button" data-go="${go}" style="cursor:pointer"><span class="tg t-${go==="prim"?"primitive":go==="sem"?"semantic":"component"}">${l}</span><br><b>${n}</b> <span class="small muted">${sub}</span></div>`;
 $("#tierbar").innerHTML=tb(n("primitive"),"Primitive",SCOPE==="all"?"0. Primitives · fonts":"thang màu, alpha, dark","prim")+'<div class="arw">→</div>'
  +tb(n("semantic")+st,"Semantic",SCOPE==="all"?`1. Semantic · 2.–5. Platform · ${st} text style`:"1. Semantic","sem")+'<div class="arw">→</div>'+tb(n("component"),"Component token",SCOPE==="all"?"6. Component sizes":"màu đã bỏ tầng này (DEC-318)","ctok")+tb(n("brand"),"Brand","7. Brand · theo vai §3.5","prim");
 const used=rows.filter(r=>r.tier!=="primitive"&&!r.style),pct=Math.round(100*used.filter(r=>r.direct.length||r.via.length).length/Math.max(1,used.length));
 const F=D.findings.filter(inS),todo=F.filter(f=>!NOACT.has(f.sub)),noact=F.length-todo.length,cnt=x=>todo.filter(f=>f.kind===x).length;
 const kinds=ORDER.filter(x=>SCOPE==="all"||F.some(f=>f.kind===x));
 $("#kpis").innerHTML=k(pct+"%",SCOPE==="all"?"token semantic + component đang có component dùng":"token màu đang có component dùng",pct>=80?"ok":"warn","sem")+k(D.stats.components,"component đã quét","","comps")
  +kinds.map(x=>k(cnt(x),KN[x],["role","stale-name","skip","prim","alias","unknown"].includes(x)?(cnt(x)?"bad":"ok"):(cnt(x)?"warn":"ok"),"q-"+x)).join("")
  +(noact?k(noact,"không cần xử lý: giữ sẵn, cố ý","ok","q-noact"):"");
 const h=(D.history||[]).map(x=>({date:x.date,v:SCOPE==="all"?x.total:x.colorTodo})).filter(x=>x.v!=null); $("#hist").innerHTML="";
 if(h.length>1){const mx=Math.max(...h.map(x=>x.v));
  $("#hist").innerHTML=`<span class="small muted">Tổng mục cần xử lý qua các lần quét:</span><div class="hist">${h.map(x=>`<i title="${x.date}: ${x.v}" style="height:${Math.max(3,40*x.v/mx)}px"></i>`).join("")}</div>`;}
 if(D.resolved?.length&&SCOPE==="all") $("#hist").innerHTML+=`<p class="small">✅ ${D.resolved.length} mục đã hết so với lần quét trước.</p>`;}
function pv(r){const v=`var(--${r.name})`;
 if(r.style) return `<div class="pv"><span class="ag ${r.name}">Ag</span></div>`;
 if(r.kind==="color") return `<div class="pv"><i class="sw" style="background:${v}"></i></div>`;
 if(r.kind==="shadow") return `<div class="pv" style="background:#F1F5F9"><i class="sh" style="box-shadow:${v}"></i></div>`;
 if(r.kind==="dim"&&r.group==="radius") return `<div class="pv"><i class="rd" style="border-radius:${v}"></i></div>`;
 if(r.kind==="dim") return `<div class="pv"><i class="bar" style="width:${v}"></i></div>`;
 return `<div class="pv"><span class="small muted">—</span></div>`;}
function vals(r){const v=r.vals,a=v["light-web"]||"";const d=[];
 if(v["dark-web"]!==a) d.push(`Dark <b>${E(v["dark-web"])}</b>`); if(v["light-mobile"]!==a) d.push(`Mobile <b>${E(v["light-mobile"])}</b>`);
 return `<div class="vals"><b>${E(a)}</b>${d.length?" · "+d.join(" · "):""}${r.refs.length?`<br>→ ${r.refs.map(E).join(", ")}`:""}</div>`;}
const TOK=Object.fromEntries(D.tokens.map(r=>[r.name,r]));
const fl=name=>D.findings.filter(f=>f.token===name||(f.tokens||[]).includes(name)||(f.tokens||[]).some(x=>typeof x==="string"&&x.split(" (")[0].replace(/\//g,"-")===name));
const refs=r=>r.refs.length?r.refs.map(x=>{const t=TOK[x]?.tier||"";return `<span class="tg t-${t} ref">${E(x)}</span>`}).join("")+(r.tier==="component"&&r.refs.some(x=>TOK[x]?.tier==="primitive")?'<br><span class="warnraw small">⚠ trỏ thẳng Primitive</span>':"")
 :(r.style?'<span class="small muted">text style</span>':r.rawVal&&r.tier==="component"?'<span class="warnraw small">⚠ số trần</span>':r.rawVal?'<span class="small muted">giá trị thang</span>':"");
const TDESC={semantic:"Token mang <b>nghĩa / vai trò</b>: <code>1. Semantic</code> (màu, Light/Dark) + <code>2.–5. Platform</code> (bo góc, khoảng cách, chữ, cỡ; Web/Mobile) + text style, shadow, motion, grid. Trỏ về Primitive; số trần ở tầng này là giá trị thang (vd cỡ chữ), không phải lỗi.",
 component:"Token riêng của một component: <code>6. Platform · Component sizes</code> (số đo). Tầng màu <code>8. Component</code> đã bỏ (<code>DEC-318</code>), component gắn thẳng Semantic. Chuẩn DEC-313: <b>chỉ trỏ Semantic</b> hoặc Brand theo vai; ⚠ khi trỏ thẳng Primitive hoặc ghi số trần."};
function tokens(){const g=$("#fg").value,f=$("#ff").value,c=$("#fc").value,q=$("#fq").value.trim().toLowerCase();
 $("#ttitle").textContent=TIERN[curTier]; $("#tdesc").innerHTML=TDESC[curTier];
 let rows=D.tokens.filter(r=>(SCOPE==="all"||r.c)&&r.tier===curTier&&(!g||r.group===g||(g==="comp"&&r.group.startsWith("c:")))&&(!c||r.coll===c)&&(!q||r.name.includes(q)||[...r.direct,...r.via].some(x=>x.includes(q))));
 if(f==="none") rows=rows.filter(r=>!r.direct.length&&!r.via.length);
 else if(f==="raw") rows=rows.filter(r=>r.rawVal);
 else if(f==="skipr") rows=rows.filter(r=>r.refs.some(x=>TOK[x]?.tier==="primitive"));
 else if(f) rows=rows.filter(r=>fl(r.name).some(x=>x.kind===f));
 const key=r=>{const i=D.groups.findIndex(x=>x[0]===r.group);return (i<0?99:i).toString().padStart(3,"0")+r.group};
 rows.sort((a,b)=>key(a).localeCompare(key(b)));let last="",h="";
 for(const r of rows){ if(r.group!==last){last=r.group;h+=`<tr class="g"><td colspan="6">${E(gname(r.group))}</td></tr>`;}
  const fs=fl(r.name).map(x=>`<span class="tg k-${x.kind}">${KN[x.kind]}</span>`).join("");
  h+=`<tr><td>${pv(r)}</td><td><code>--${E(r.name)}</code><br><span class="small muted">${E(r.coll)}</span> ${fs}</td>
  <td class="hidem">${vals(r)}</td><td>${refs(r)}</td><td>${r.direct.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}${r.via.map(c=>`<span class="cmp via" data-c="${c}" title="dùng gián tiếp">${E(c)}</span>`).join("")}${!r.direct.length&&!r.via.length?'<span class="muted small">—</span>':""}</td>
  <td>${r.direct.length+r.via.length||""}</td></tr>`;}
 $("#tbody").innerHTML=h||`<tr><td colspan="6" class="muted">${curTier==="component"&&SCOPE==="color"?"Không còn token màu tầng Component: DEC-318 đã bỏ, component gắn thẳng Semantic. Đổi sang phạm vi Tất cả để xem token số đo.":"Không có token khớp bộ lọc."}</td></tr>`; $("#tcount").textContent=rows.length+" token";}
function prims(){const P=D.tokens.filter(r=>(r.tier==="primitive"||r.tier==="brand")&&(SCOPE==="all"||r.c));
 const fam=r=>r.tier==="brand"?"7. Brand — tầng riêng, component dùng theo vai §3.5 (đang xem Than chì)":r.coll==="fonts"?"Font":r.name.startsWith("space-")?"Khoảng cách · space/N":r.name.startsWith("radius-")?"Bo góc · radius/N":"Màu · "+(r.name.match(/^[a-z]+/)[0]);
 const by={};P.forEach(r=>(by[fam(r)]=by[fam(r)]||[]).push(r));
 $("#prims").innerHTML=Object.entries(by).map(([n,rs])=>{const zero=rs.filter(r=>!r.refBy.length&&!r.direct.length).length;
  return `<div class="fam"><h3>${E(n)} <span class="small muted">${rs.length} token${zero?` · ${zero} chưa ai trỏ tới`:""}</span></h3><div class="cells">${rs.map(r=>{
   const sem=r.refBy.filter(x=>TOK[x]?.tier==="semantic"),cmp=r.refBy.filter(x=>TOK[x]?.tier==="component");const bad=cmp.length||r.direct.length;
   const vis=r.kind==="color"?`<div class="sw" style="background:var(--${r.name})"></div>`:r.name.startsWith("radius-")?`<div class="dm"><i class="rd" style="border-radius:var(--${r.name})"></i></div>`:r.name.startsWith("space-")?`<div class="dm"><i style="width:var(--${r.name})"></i></div>`:`<div class="dm" style="font-family:var(--${r.name});font-size:18px">Ag</div>`;
   return `<button class="cell${!r.refBy.length&&!r.direct.length?" zero":""}${bad?" badc":""}" data-p="${r.name}">${vis}<b>${E(r.name)}</b><span class="muted">${E((r.vals["light-web"]||"").slice(0,24))}</span><br>← ${sem.length}${bad?` · <span style="color:#B42318">${cmp.length+r.direct.length} gọi thẳng</span>`:""}</button>`}).join("")}</div><div class="detail hide"></div></div>`;}).join("");}
function pdetail(b){const r=TOK[b.dataset.p],box=b.closest(".fam").querySelector(".detail");const open=b.getAttribute("aria-expanded")==="true";
 b.closest(".fam").querySelectorAll(".cell").forEach(x=>x.setAttribute("aria-expanded","false"));
 if(open){box.classList.add("hide");return;} b.setAttribute("aria-expanded","true");
 const sem=r.refBy.filter(x=>TOK[x]?.tier==="semantic"),cmp=r.refBy.filter(x=>TOK[x]?.tier==="component");
 box.innerHTML=`<b>--${E(r.name)}</b> = <code>${E(r.vals["light-web"])}</code> · ${E(r.coll)}<br>
 <b>Semantic trỏ vào (${sem.length}):</b> ${sem.map(x=>`<span class="tg t-semantic ref">${E(x)}</span>`).join("")||'<span class="muted">—</span>'}<br>
 <b>Token component trỏ thẳng (${cmp.length}):</b> ${cmp.map(x=>`<span class="tg t-component ref">${E(x)}</span>`).join("")||'<span class="muted">— tốt</span>'}<br>
 <b>Component gọi thẳng trong css/spec:</b> ${r.direct.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")||'<span class="muted">— tốt</span>'}
 <br><b>Component dùng qua chuỗi:</b> ${r.via.map(c=>`<span class="cmp via" data-c="${c}">${E(c)}</span>`).join("")||'<span class="muted">—</span>'}`;box.classList.remove("hide");}
function matrix(){const pc=m=>m.pct==null?'<span class="zero">—</span>':`<span class="pct"><i style="width:${m.pct}%"></i></span>${m.pct}%`,num=(n,h)=>n?`<span class="${h?"hot":""}">${n}</span>`:'<span class="zero">0</span>';
 $("#matrix").innerHTML=`<table class="mx"><thead><tr><th>Component</th><th>% dùng đúng Semantic</th><th class="num">Biến tự đặt</th><th class="num">Màu trần</th><th class="num">Tên cũ</th><th class="num">Lệch vai</th><th class="num" title="Số mục lệch mốc built trong _deps.json: foundation hoặc component con">Lệch mốc</th><th>Trạng thái</th></tr></thead><tbody>${D.matrix.map(m=>`<tr>
 <td><span class="cmp" data-c="${E(m.slug)}">${E(m.slug)}</span> <button type="button" class="chipbtn small" data-qc="${E(m.slug)}" style="padding:1px 8px;font-size:11px">Xem việc</button></td>
 <td>${pc(m)} <span class="small muted">${m.good}/${m.total} chỗ · ${m.source==="css"?"CSS":"chỉ có md"}</span></td>
 <td class="num">${num(m.alias,1)}${m.aliasOk?` <span class="small muted">+${m.aliasOk} ổn</span>`:""}</td><td class="num">${num(m.literal,1)}</td><td class="num">${num(m.stale,1)}</td><td class="num">${num(m.role,1)}</td>
 <td class="num" title="${m.colorStale?"foundation Màu đã đổi so với lúc dựng":""}">${num(m.deps)}${m.colorStale?' <span class="small muted">gồm Màu</span>':""}</td>
 <td class="small">${E(m.status||"—")}${m.pickSrc==="đề xuất"?' <span class="tg unsure" title="Trang chưa có phương án chốt, máy đọc theo preset Đề xuất">chưa chốt phương án</span>':""}</td></tr>`).join("")}</tbody></table>`;}
function comps(){matrix();const q=$("#cq").value.trim().toLowerCase(),gs=$("#cg").value,colorOnly=SCOPE==="color",iss=c=>colorOnly?c.issuesColor:c.issues;
 const cols={color:"#0036B5",type:"#7A5AF8",radius:"#00A2FF",space:"#12B76A",grid:"#F79009",elevation:"#667085",["touch-focus"]:"#F04438",motion:"#2E90FA",icon:"#344054"};
 const isC=n=>TOK[n]?.c;
 $("#cards").innerHTML=D.components.filter(c=>(!q||c.slug.includes(q))&&(!gs||c.group===gs)).sort((a,b)=>iss(b)-iss(a)).map(c=>{
  c={...c,used:colorOnly?c.used.filter(isC):c.used,byGroup:colorOnly?Object.fromEntries(Object.entries(c.byGroup).filter(([g])=>g==="color")):c.byGroup,unknown:colorOnly?c.unknown.filter(n=>/^color-/.test(n)):c.unknown,
   local:colorOnly?Object.fromEntries(Object.entries(c.local).filter(([a])=>FX[`alias--${c.slug}--${a}`]?.color)):c.local,bare:colorOnly?0:c.bare,issues:iss(c)};
  const tot=Object.values(c.byGroup).reduce((a,b)=>a+b,0)||1;
  const meter=Object.entries(c.byGroup).map(([g,n])=>`<i title="${E(gname(g))}: ${n}" style="width:${100*n/tot}%;background:${cols[g]||"#A48AFB"}"></i>`).join("");
  const loc=Object.entries(c.local),lit=Object.entries(c.literals);
  const by={};c.used.forEach(n=>{const r=D.tokens.find(x=>x.name===n);(by[r.group]=by[r.group]||[]).push(r)});
  return `<div class="card" id="c-${c.slug}"><h3><span>${E(c.slug)}</span><span>${c.issues?`<span class="tg k-prim">${c.issues} cần xử lý</span>`:'<span class="tg" style="background:#ECFDF3;color:#067647">sạch</span>'}</span></h3>
  <div class="small muted">${E(c.group)} · <code>${E(c.src)}</code></div><div class="meter">${meter}</div>
  <div class="small"><b>${c.used.length}</b> token hệ thống${loc.length?` · <b style="color:#B42318">${loc.length}</b> biến tự đặt`:""}${lit.length?` · <b style="color:#C4320A">${lit.reduce((a,x)=>a+x[1],0)}</b> màu trần`:""}${c.unknown.length?` · <b style="color:#B42318">${c.unknown.length}</b> token không tồn tại`:""}${c.bare?` · ${c.bare} số đo chưa gắn token`:""}</div>
  <details><summary class="small" style="cursor:pointer;margin-top:6px">Xem token đang dùng</summary>${Object.entries(by).map(([g,rs])=>`<div class="small" style="margin-top:6px"><b>${E(gname(g))}</b><br>${rs.map(r=>`<span class="tg t-${r.tier}">${E(r.name)}</span>`).join("")}</div>`).join("")}
  ${loc.length?`<div class="small" style="margin-top:6px"><b>Biến tự đặt</b><br>${loc.map(([a,v])=>`<code>--${E(a)}: ${E(v)}</code>`).join("<br>")}</div>`:""}
  ${c.unknown.length?`<div class="small" style="margin-top:6px"><b>Token không tồn tại</b><br>${c.unknown.map(E).join(", ")}</div>`:""}</details></div>`;}).join("");}
const SP=D.specimens||{},BUN=D.bundles||{},LAD=D.ladder||{};
const plat=()=>$(".pvroot").getAttribute("data-platform")==="mobile"?"Mobile":"Web";
function famOf(sp){const k=sp.kind;return k==="radius"?"radius-":k==="font"?"type-":k==="line"?"type-":["padding","gap","overlap"].includes(k)?"space-":"size-";}
function semVal(r,m){const v=r.vals[m==="Web"?"light-web":"light-mobile"];const n=parseFloat(v);return /^-?\d+(\.\d+)?(px)?$/.test((v||"").trim())?n:null;}
function choices(sp){const m=plat(),cur=sp.num[m];const out=[{label:"Hiện tại",v:cur,cur:true,tok:sp.jname}];
 if(cur===null||cur===undefined) return out;
 if(sp.kind==="overlap"||sp.kind==="opacity"||cur<0) return out;
 const fam=famOf(sp);let C=D.tokens.filter(r=>r.tier==="semantic"&&r.name.startsWith(fam)&&!r.style);
 if(sp.kind==="font") C=C.filter(r=>/-size$/.test(r.name)); if(sp.kind==="line") C=C.filter(r=>/-line-height$/.test(r.name));
 const vs=C.map(r=>({r,v:semVal(r,m)})).filter(x=>x.v!==null);
 const same=vs.filter(x=>x.v===cur&&semVal(x.r,m==="Web"?"Mobile":"Web")===sp.num[m==="Web"?"Mobile":"Web"]);
 same.slice(0,2).forEach(x=>out.push({label:"Trỏ Semantic cùng số",v:x.v,tok:x.r.jname||x.r.name,same:true}));
 const lo=vs.filter(x=>x.v<cur).sort((a,b)=>b.v-a.v)[0],hi=vs.filter(x=>x.v>cur).sort((a,b)=>a.v-b.v)[0];
 if(lo) out.push({label:"Làm tròn xuống",v:lo.v,tok:lo.r.jname||lo.r.name});
 if(hi) out.push({label:"Làm tròn lên",v:hi.v,tok:hi.r.jname||hi.r.name});
 if(!same.length&&sp.kind!=="radius"&&sp.kind!=="font"&&sp.kind!=="line") out.push({label:"Thêm bậc Semantic mới",v:cur,tok:`${fam.replace(/-$/,"")}/… = ${cur}`,add:true});
 return out;}
function schematic(sp,v){const k=sp.kind,px=x=>Math.max(0,x)+"px",S=Math.min(1,130/Math.max(1,v||1));
 const lab=`<span class="dim" style="bottom:-16px">${v}${k==="opacity"?"":"px"}</span>`;
 if(k==="height") return `<div class="sch"><div class="box hl" style="width:120px;height:${px(v*Math.min(1,120/v))}"></div>${lab}</div>`;
 if(k==="width") return `<div class="sch"><div class="box hl" style="height:22px;width:${px(v*Math.min(1,180/v))}"></div>${lab}${v>180?'<span class="dim" style="top:-16px">thu nhỏ</span>':""}</div>`;
 if(k==="size") return `<div class="sch"><div class="box hl" style="width:${px(v*S)};height:${px(v*S)};border-radius:${/avatar|status|spinner|dot/.test(sp.jname)?"50%":"6px"}"></div>${lab}</div>`;
 if(k==="radius") return `<div class="sch"><div class="box" style="width:96px;height:64px;border-radius:${px(v)};position:relative;overflow:hidden"><i style="position:absolute;left:0;top:0;width:${px(Math.max(v,4))};height:${px(Math.max(v,4))};background:rgba(240,68,56,.4)"></i></div>${lab}</div>`;
 if(k==="padding") return `<div class="sch"><div class="box" style="display:flex;padding:0 ${px(v)};height:28px;align-items:center;background:linear-gradient(90deg,rgba(240,68,56,.25) ${px(v)},#E7EFFD ${px(v)},#E7EFFD calc(100% - ${px(v)}),rgba(240,68,56,.25) 0)"><span style="font:500 12px Inter">Nhãn</span></div>${lab}</div>`;
 if(k==="gap") return `<div class="sch"><div class="box" style="width:28px;height:28px"></div><div class="hl" style="width:${px(v)};height:28px"></div><div class="box" style="width:56px;height:28px"></div>${lab}</div>`;
 if(k==="font") return `<div class="sch"><span class="hl" style="font:500 ${px(v)}/1.3 Inter;padding:0 4px">Nhãn 123</span>${lab}</div>`;
 if(k==="line") return `<div class="sch"><span class="hl" style="font:400 12px/${px(v)} Inter;width:120px;display:block;padding:0 4px">Dòng một<br>Dòng hai</span>${lab}</div>`;
 if(k==="border") return `<div class="sch"><div class="box" style="width:120px;height:40px;background:#fff;border:${px(v)} solid #F04438"></div>${lab}</div>`;
 if(k==="opacity") return `<div class="sch"><div class="box" style="width:120px;height:40px;opacity:${v};display:grid;place-items:center;font:500 12px Inter">Khoá</div>${lab}</div>`;
 if(k==="overlap") return `<div class="sch">${[0,1,2].map(i=>`<div class="box ${i?"hl":""}" style="width:32px;height:32px;border-radius:50%;margin-left:${i?px(0)+";margin-left:"+v+"px":"0"};border:2px solid #fff"></div>`).join("")}${lab}</div>`;
 return `<div class="sch"><div class="box hl" style="width:${px(v)};height:${px(v)}"></div>${lab}</div>`;}
const SRC={};
function srcRoot(slug){if(SRC[slug]) return SRC[slug];const h=document.createElement("div");h.style.cssText="position:absolute;left:-99999px;top:0;width:1200px";document.body.appendChild(h);
 const r=h.attachShadow({mode:"open"});r.innerHTML=`<style>${BUN[slug].css}</style>${BUN[slug].html}`;return SRC[slug]=r;}
function liveCtx(sp){const L=sp.live,r=srcRoot(L.comp);let el=null;for(const s of L.sels){try{el=r.querySelector(s)}catch(e){} if(el) break;}
 if(!el) return null;const pv=el.closest(".pv");let ctx=el.parentElement||el;if(ctx.outerHTML.length>12000) ctx=el;
 const attrs=pv?[...pv.attributes].map(a=>`${a.name}="${E(a.value)}"`).join(" "):'class="pv"';
 return `<div ${attrs} data-platform="${plat()==="Mobile"?"mobile":"web"}" style="background:transparent">${ctx.outerHTML}</div>`;}
function liveCard(host,sp,v){const L=sp.live,html=liveCtx(sp);if(!html) return false;const r=host.attachShadow({mode:"open"});
 r.innerHTML=`<style>${BUN[L.comp].css} *{--${sp.name}:${v}${sp.kind==="opacity"?"":"px"} !important}
 .ov{position:absolute;pointer-events:none;z-index:50}.ov-a{background:rgba(240,68,56,.32)}.ov-l{background:#F04438}
 .ov-t{font:600 10px/14px Inter,sans-serif;color:#fff;background:#F04438;border-radius:7px;padding:0 5px;white-space:nowrap}
 :host(.noann) .ov{display:none}</style>${html}`;
 const els=[];L.sels.forEach(s=>{try{r.querySelectorAll(s).forEach(x=>{if(els.length<3&&x.getClientRects().length) els.push(x)})}catch(e){}});
 requestAnimationFrame(()=>annotate(r,host,els,sp,v,L.props));return true;}
function annotate(r,host,els,sp,v,props){const H=host.getBoundingClientRect(),near=(a,b)=>Math.abs(a-b)<0.6;
 const add=(cls,x,y,w,h,txt)=>{if(w<=0&&h<=0&&!txt) return;const d=document.createElement("div");d.className="ov "+cls;d.style.cssText+=`left:${x-H.left}px;top:${y-H.top}px;${w!=null?`width:${Math.max(w,1)}px;`:""}${h!=null?`height:${Math.max(h,1)}px;`:""}`;if(txt) d.textContent=txt;r.appendChild(d);};
 const has=re=>props.some(p=>re.test(p));let labelled=false;const lab=(x,y,t)=>{if(!labelled){add("ov-t",x,y,null,null,t);labelled=true;}};
 const u=sp.kind==="opacity"?"":"px";
 els.forEach(el=>{const b=el.getBoundingClientRect(),c=getComputedStyle(el);
  const sides=pre=>{const S=new Set();props.forEach(p=>{if(p===pre||p===pre+"-inline"||p===pre+"-block"){if(p!==pre+"-block"){S.add(1);S.add(3);} if(p!==pre+"-inline"){S.add(0);S.add(2);}}
    ["top","right","bottom","left"].forEach((k,n)=>{if(p===pre+"-"+k) S.add(n);});});return S;};
  if(has(/^padding/)){const P=["Top","Right","Bottom","Left"].map(k=>parseFloat(c["padding"+k])),S=sides("padding");
   if(S.has(0)&&near(P[0],v)) add("ov-a",b.left,b.top,b.width,P[0]); if(S.has(2)&&near(P[2],v)) add("ov-a",b.left,b.bottom-P[2],b.width,P[2]);
   if(S.has(3)&&near(P[3],v)) add("ov-a",b.left,b.top,P[3],b.height); if(S.has(1)&&near(P[1],v)) add("ov-a",b.right-P[1],b.top,P[1],b.height);
   lab(S.has(1)&&!S.has(3)?b.right-20:b.left,b.top-15,`lề ${v}${u}`);}
  if(has(/^margin/)){const M=["Top","Right","Bottom","Left"].map(k=>parseFloat(c["margin"+k])),S=sides("margin");
   if(v<0){if(S.has(3)) add("ov-a",b.left,b.top,-v,b.height); lab(b.left,b.top-15,`đè ${-v}${u}`);}
   else{if(S.has(0)) add("ov-a",b.left,b.top-M[0],b.width,M[0]); if(S.has(2)) add("ov-a",b.left,b.bottom,b.width,M[2]);
    if(S.has(3)) add("ov-a",b.left-M[3],b.top,M[3],b.height); if(S.has(1)) add("ov-a",b.right,b.top,M[1],b.height); lab(b.left,b.top-15,`cách ${v}${u}`);}}
  if(has(/gap$/)){const k=[...el.children].filter(x=>x.getClientRects().length).map(x=>x.getBoundingClientRect());
   for(let i=1;i<k.length;i++){const a=k[i-1],z=k[i];
    if(z.left>=a.right-0.5) add("ov-a",a.right,Math.min(a.top,z.top),z.left-a.right,Math.max(a.bottom,z.bottom)-Math.min(a.top,z.top));
    else if(z.top>=a.bottom-0.5) add("ov-a",Math.min(a.left,z.left),a.bottom,Math.max(a.right,z.right)-Math.min(a.left,z.left),z.top-a.bottom);}
   lab(b.left,b.top-15,`khoảng ${v}${u}`);}
  if(has(/(^|-)height$|^block-size/)){add("ov-l",b.right+6,b.top,1,b.height);add("ov-l",b.right+3,b.top,7,1);add("ov-l",b.right+3,b.bottom-1,7,1);lab(b.right+10,b.top+b.height/2-7,`cao ${v}${u}`);}
  if(has(/(^|-)width$|^inline-size/)){add("ov-l",b.left,b.bottom+6,b.width,1);add("ov-l",b.left,b.bottom+3,1,7);add("ov-l",b.right-1,b.bottom+3,1,7);lab(b.left+b.width/2-16,b.bottom+9,`rộng ${v}${u}`);}
  if(has(/radius/)){const rr=Math.max(4,Math.min(v,b.height/2,b.width/2));add("ov-a",b.left,b.top,rr,rr);lab(b.left-4,b.top-16,`bo ${v}${u}`);}
  if(has(/^font|line-height/)){add("ov-l",b.left,b.bottom+2,b.width,2);lab(b.left,b.bottom+5,`${sp.kind==="line"?"cao dòng":"cỡ chữ"} ${v}${u}`);}
  if(has(/^(top|left|right|bottom|inset)$/)){add("ov-l",b.left,b.top,1,b.height);lab(b.left,b.top-15,`lệch ${v}${u}`);}
  if(has(/opacity/)) lab(b.left,b.top-15,`mờ ${v}`);});
 if(!labelled&&els[0]){const b=els[0].getBoundingClientRect();lab(b.left,b.top-15,`${v}${u}`);}}
function renderSpec(box,f){const toks=(f.tokens||[f.token]).map(t=>String(t).split(" (")[0].replace(/\//g,"-")).filter(n=>SP[n]);
 box.innerHTML=toks.slice(0,4).map((n,i)=>{const sp={...SP[n],name:n};const m=plat();
  return `<div class="sprow" data-n="${n}"><div class="sphead"><span class="spmark">${i+1}</span><b>${E(sp.part||"—")}</b> · <code>${E(sp.jname)}</code> · Web ${sp.num.Web??"—"} / Mobile ${sp.num.Mobile??"—"} · đang xem <b>${m}</b>${sp.src?` · nguồn <code>${E(sp.src)}</code>`:""}${sp.live?` · <span class="tg t-component">preview thật: ${E(sp.live.comp)}</span> <span class="small muted">vùng tô đỏ = ${E(sp.live.props.join(", "))} · kích thước thật</span>`:` · <span class="small muted">hình mô phỏng (chưa có preview HTML của component)</span>`}</div>
  <div class="opts">${choices(sp).map((o,j)=>`<div class="opt ${o.cur?"cur":""}"><h4><span>${E(o.label)}</span><span class="${o.same||o.add?"same":o.cur?"":"delta"}">${o.v}${sp.kind==="opacity"?"":"px"}${!o.cur&&!o.same&&!o.add&&sp.num[m]!=null?` (${o.v>sp.num[m]?"+":""}${Math.round((o.v-sp.num[m])*10)/10})`:""}</span></h4>
   <div class="stage ${sp.live?"live":""}" data-j="${j}">${sp.live?"":schematic(sp,o.v)}</div><div class="cap"><code>${E(o.tok)}</code>${o.same?" · nhìn không đổi":o.add?" · thêm token Semantic mới, nhìn không đổi":o.cur?"":" · đổi nhìn"}</div></div>`).join("")}
  ${!choices(sp).slice(1).length?`<div class="small muted" style="padding:6px">${sp.kind==="overlap"||sp.num[m]<0?"Số âm: biến Figma không tính được −token, chỉ chọn Ngoại lệ hoặc thêm token âm riêng.":sp.kind==="opacity"?"Độ mờ: chưa có thang Semantic; chọn Ngoại lệ hoặc thêm token <code>opacity/disabled</code>.":"Không có phương án."}</div>`:""}</div></div>`;}).join("")+(toks.length>4?`<div class="small muted">… còn ${toks.length-4} token cùng giá trị, cùng cách xử lý.</div>`:"");
 box.querySelectorAll(".sprow").forEach(row=>{const n=row.dataset.n,sp={...SP[n],name:n};if(!sp.live) return;const ch=choices(sp);
  row.querySelectorAll(".stage").forEach(st=>{const h=document.createElement("div");h.style.cssText="position:relative;display:inline-block";h.classList.add("annhost");if(document.body.classList.contains("noann")) h.classList.add("noann");st.appendChild(h);if(!liveCard(h,sp,ch[+st.dataset.j].v)){st.classList.remove("live");st.innerHTML=schematic(sp,ch[+st.dataset.j].v);}});});}
const swatch=t=>`<i style="background:var(--${E(t)})"></i>`;
function placeList(ps){return ps.map(p=>`<div class="place">${E(p.comp)} · <b>${E(p.sel)}</b> · ${E(p.file)}${p.src==="kit"?" (kit dùng chung)":""}${p.unsure?' · <span class="tg unsure">cần xem</span>':""}${p.pickSrc==="đề xuất"?" · phương án chưa chốt":""}</div>`).join("");}
function roleBody(f){const un=!f.certain;
 return `<div class="small"><span class="tg ${un?"unsure":"sure"}">${un?"Cần xem, máy không chắc":"Đề xuất rõ"}</span> ${f.reason==="sai nhóm"?'<span class="tg k-literal">sai nhóm token</span>':""}${f.reason==="lệch luật"?'<span class="tg k-literal">lệch luật</span>':""} <span class="muted">Căn cứ: ${E(f.why)}</span></div>
 <div class="tk good">${swatch(f.suggest)}<code>${E(f.suggestName)}</code> <span class="pl">đề xuất · ${f.suggestN?`đang dùng ${f.suggestN} chỗ ở ${f.suggestComps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:"chưa chỗ nào dùng"}</span></div>
 ${f.devs.map(x=>`<div class="tk off">${swatch(x.token)}<code>${E(x.name)}</code> <span class="pl">lệch ${x.n} chỗ ở ${x.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}</span></div>${placeList(x.places.slice(0,6))}${x.places.length>6?`<details class="small"><summary style="cursor:pointer;margin-left:20px">Còn ${x.places.length-6} chỗ</summary>${placeList(x.places.slice(6))}</details>`:""}`).join("")}`;}
function rpCell(f,tok,theme){const V=t=>`var(--${t})`,T=V(tok);
 const ic='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg>';
 const box=`background:${V("color-bg-primary")};color:${V("color-text-primary")}`;let x="";
 if(f.prop==="nền") x=`<div class="rps" data-s="bg" style="background:${T};color:${V(f.fg)};border:1px solid ${V("color-border-secondary")}">Mẫu nền</div>`;
 else if(f.prop==="chữ") x=`<span data-s="fg" style="color:${T};font:500 14px/20px Inter">Nội dung mẫu 123</span>`;
 else if(f.prop==="icon") x=`<span data-s="fg" style="color:${T};display:inline-flex">${ic}</span><span style="color:${V("color-text-primary")};font:500 13px/18px Inter">Nhãn</span>`;
 else if(f.prop==="viền") x=`<div class="rps" data-s="bd" style="${box};border:${/focus/.test(f.state)?2:1}px solid ${T}">Ô mẫu</div>`;
 else if(f.prop==="vạch") x=`<div data-s="bd" style="width:80%;border-top:1px solid ${T}"></div>`;
 else if(f.prop==="vòng focus") x=`<div class="rps" data-s="ol" style="${box};outline:2px solid ${T};outline-offset:2px">Ô mẫu</div>`;
 else x=`<div class="rps" data-s="sh" style="${box};box-shadow:inset 0 -2px 0 ${T}">Tab mẫu</div>`;
 return `<div class="rpcell" data-theme="${theme}" data-tok="${E(tok)}" style="background:${V(f.on)}">${x}</div>`;}
function rpCap(f,tok,mode){const v=f.vals[tok]||{},c=mode==="l"?v.cl:v.cd,min=f.prop==="chữ"||f.prop==="nền"?4.5:3,exempt=/tắt/.test(f.state);
 return `<small>${E(mode==="l"?v.l:v.d)}${c?` · <b class="${c<min&&!exempt?"low":""}">${String(c).replace(".",",")}:1</b>`:""}</small>`;}
function rolePv(box,f){box.innerHTML=f.devs.map(x=>{const a=x.token,b=f.suggest,cell=(t,mode,lab,cls)=>`<div class="rpc ${cls}"><span>${lab}</span>${rpCell(f,t,mode==="l"?"light":"dark")}${rpCap(f,t,mode)}</div>`;
  return `<div class="rp"><h5>Trước <code>${E(x.name)}</code> → Sau <code>${E(f.suggestName)}</code></h5>${cell(a,"l","Trước · Sáng","")}${cell(b,"l","Sau · Sáng","after")}${cell(a,"d","Trước · Tối","")}${cell(b,"d","Sau · Tối","after")}</div>`}).join("")
  +`<div class="small muted">Dựng bằng biến thật trong tokens.css. Số là tương phản với nền đặt dưới${f.prop==="nền"?" (chữ text/primary trên nền đó)":""}; đỏ khi dưới ngưỡng ${f.prop==="chữ"||f.prop==="nền"?"4,5":"3"}:1.</div>`;}
function itemHTML(f){const s=ST[f.id]||{};const acts=f.acts||KACT[f.kind];
 let d="";
 if(f.kind==="role") d=roleBody(f);
 if(f.kind==="stale-name") d=`trong <code>${E(f.where)}</code>${f.comp?` · <span class="cmp" data-c="${f.comp}">${E(f.comp)}</span>`:""}${f.items.map(i=>`<div class="place"><b>${E(i.old)}</b> → ${E(i.new)} · ${i.count} chỗ${i.lines.length?` · dòng ${i.lines.join(", ")}`:""}${i.pattern?" · viết theo mẫu, đổi tay":""}</div>`).join("")}`;
 if(f.kind==="unused") d=`<span class="tg t-${f.tier}">${f.tier}</span> ${E(gname(f.group))}${f.reason?` · ${E(f.reason)}`:""}`;
 if(f.kind==="single") d=`chỉ <span class="cmp" data-c="${f.comps[0]}">${E(f.comps[0])}</span> dùng`;
 if(f.kind==="prim") d=`${f.comps?`ảnh hưởng ${f.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:`trong <code>${E(f.where)}</code>`}${f.alt?.length?` · gợi ý: <code>${f.alt.map(E).join(" / ")}</code>`:" · <mark>chưa có token semantic cùng giá trị</mark>"}`;
 if(f.kind==="alias"){const vs=f.values||[f.value];d=vs.slice(0,6).map(v=>`<code>--${E(f.alias)}: ${E(v)}</code>`).join(" ")+(vs.length>6?` … +${vs.length-6}`:"");
  if(f.color) d+=f.sub==="replace"?`<br>${f.aliasWhy?E(f.aliasWhy)+" ":"Chỉ trỏ một token: "}<mark>thay thẳng bằng <code>${E(f.suggestName)}</code></mark>, ${f.uses} chỗ.`:f.sub==="dead"?`<br><mark>Không chỗ nào dùng</mark>, xoá được.`:f.sub==="switch"?`<br>Đổi giá trị theo biến thể, mỗi giá trị đã là Semantic. ${f.uses} chỗ dùng. Giữ được.`:`<br><mark>Giá trị trần</mark>, chưa trỏ token.`;
  else d+=f.maps.length?` · trỏ tới <code>${f.maps.map(E).join(", ")}</code>`:" · số đo, không phải màu";}
 if(f.kind==="unknown") d=`trong <code>${E(f.where)}</code>`;
 if(f.kind==="literal") d=`<span class="pv" style="display:inline-grid;width:22px;height:16px;vertical-align:middle"><i class="sw" style="background:${E(f.value)}"></i></span> ${f.count} lần trong CSS${f.html?`, ${f.html} lần inline HTML`:""}${f.alt.length?` · gợi ý: <code>${f.alt.map(E).join(" / ")}</code>`:" · <mark>không token nào trùng giá trị</mark>"}`;
 if(f.kind==="dup") d=`giá trị <code>${E(f.value)}</code>${f.valueDark?` · Tối <code>${E(f.valueDark)}</code>`:""}${f.reason?`<br>${E(f.reason)}`:""}${f.purposes?Object.entries(f.purposes).map(([n,p])=>`<div class="place"><b>${E(n.replace(/^color-/,""))}</b>: ${E(p||"color.md chưa ghi")}</div>`).join(""):""}${f.comps.length?`dùng ở ${f.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:""}`;
 if(f.kind==="compraw") d=`${f.tokens.slice(0,6).map(x=>`<code>${E(x)}</code>`).join(", ")}${f.tokens.length>6?` … +${f.tokens.length-6}`:""}${f.alt.length?` · Semantic cùng số: <code>${f.alt.map(E).join(" / ")}</code>`:" · <mark>chưa có Semantic cùng số</mark>"}${f.near?`<br>Bậc gần nhất (thang space/size): <b>${E(f.near)}</b>`:""}`;
 if(f.kind==="skip") d=`${f.alt.length?`gợi ý: <code>${f.alt.map(E).join(" / ")}</code>`:"<mark>chưa có semantic cùng giá trị</mark>"}${f.comps.length?` · ảnh hưởng ${f.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:""}`;
 return `<div class="item${s.choice?" done":""}${s.choice&&s.choice.endsWith("…")?" open":""}" data-id="${E(f.id)}"><div><code>${E(f.title)}</code> ${f.new?'<span class="tg new">Mới</span>':""}<div class="small ${f.kind==="role"?"":"muted"}" style="margin-top:2px">${d}</div><span class="saved" data-saved></span></div>
  <div class="act">${acts.map(a=>`<button type="button" data-a="${E(a)}" aria-pressed="${s.choice===a}">${E(a)}</button>`).join("")}<button type="button" data-note-toggle title="Ghi chú">✎</button>${(f.kind==="compraw"||f.kind==="skip")?'<button type="button" class="pvbtn" data-pv>Xem preview</button>':""}${f.kind==="role"?'<button type="button" class="pvbtn" data-rp>Xem thử trước, sau</button>':""}</div>
  <textarea placeholder="Ghi chú / gộp vào token nào…">${E(s.note||"")}</textarea><div class="pvbox hide"></div></div>`;}
function fmatch(f,q){return !q||f.id.includes(q)||f.comp===q||(f.comps||[]).includes(q)||(f.title||"").toLowerCase().includes(q);}
function qlead(){const r=D.findings.filter(f=>f.kind==="role"&&inS(f)),rule=r.filter(f=>f.certain&&/DEC-|color\.md/.test(f.why)).length,st=D.findings.filter(f=>f.kind==="stale-name"&&inS(f)).length;
 const top=[...D.matrix].sort((a,b)=>b.role-a.role)[0];
 $("#qlead").innerHTML=SCOPE==="color"?`<b>Nên làm trước:</b> xử lý <mark>${rule} lệch vai có luật rõ</mark> ở tab Đồng nhất theo vai, vì đổi về đúng token là xong, không phải thêm gì. Bắt đầu từ <b>${E(top.slug)}</b> (${top.role} chỗ lệch). Sau đó đổi <mark>${st} mục tên cũ</mark> trong tài liệu.`
  :`<b>Nên làm trước:</b> ở phạm vi Màu đã duyệt. Khoảng cách, bo góc, chữ <mark>đang review ở trang riêng</mark>, đừng chọn hướng ở đây khi trang đó chưa chốt.`;}
function queue(){qlead();const fk=$("#qk").value,fq=$("#qq").value.trim().toLowerCase(),only=$("#qn").value,base=D.findings.filter(f=>inS(f)&&fmatch(f,fq));
 const pick=f=>!(only==="todo"&&ST[f.id]?.choice)&&!(only==="new"&&!f.new);
 const sec=ORDER.filter(k=>!fk||k===fk).map(k=>{const it=base.filter(f=>f.kind===k&&!NOACT.has(f.sub)&&pick(f));
  if(!it.length) return "";
  const done=it.filter(f=>ST[f.id]?.choice).length;
  return `<details class="sec" id="q-${k}" ${fk||it.length<=12?"open":""}><summary><span class="tg k-${k}">${KN[k]}</span> ${it.length} mục <span class="muted small">· đã chọn ${done}</span></summary>
  <div class="why">${KWHY[k]}</div>${it.map(itemHTML).join("")}</details>`;}).join("");
 const na=base.filter(f=>NOACT.has(f.sub)&&(!fk||f.kind===fk)&&pick(f));
 const naH=na.length?`<details class="sec" id="q-noact"><summary><span class="tg" style="background:#ECFDF3;color:#067647">Không cần xử lý</span> ${na.length} mục <span class="muted small">· ${["unused","dup","alias"].map(k=>[k,na.filter(f=>f.kind===k).length]).filter(x=>x[1]).map(([k,n])=>`${n} ${k==="unused"?"token giữ sẵn":k==="dup"?"trùng do tên theo vai":"biến theo biến thể"}`).join(" · ")}</span></summary>
  <div class="why">Máy xếp vào đây kèm lý do. Thấy sai thì vẫn chọn hướng được.</div>${na.map(itemHTML).join("")}</details>`:"";
 $("#queue").innerHTML=(sec+naH)||`<p class="muted">Không còn mục nào khớp bộ lọc.</p>`;
 const all=D.findings.filter(f=>inS(f)&&!NOACT.has(f.sub)),dn=all.filter(f=>ST[f.id]?.choice).length; $("#qcount").textContent=`${dn}/${all.length} mục đã chọn hướng xử lý`;
 const orphan=SCOPE==="all"?Object.keys(ST).filter(id=>ST[id]?.choice&&!FX[id]).length:0;$("#qorphan").textContent=orphan?`${orphan} quyết định đã lưu không còn mục tương ứng (token đã đổi tên). Vẫn giữ trong kho, không mất.`:"";}
function qkOpts(){const cnt=k=>D.findings.filter(f=>inS(f)&&f.kind===k&&!NOACT.has(f.sub)).length;const v=$("#qk").value;
 $("#qk").innerHTML=`<option value="">Mọi loại</option>${ORDER.filter(k=>SCOPE==="all"||D.findings.some(f=>f.color&&f.kind===k)).map(k=>`<option value="${k}">${KN[k]} (${cnt(k)})</option>`).join("")}`;$("#qk").value=[...$("#qk").options].some(o=>o.value===v)?v:"";}
function roles(){const el=$("#re").value,pr=$("#rp").value,st=$("#rs").value,md=$("#rm").value,q=$("#rq").value.trim().toLowerCase();
 const all=D.findings.filter(f=>f.kind==="role");
 const it=all.filter(f=>(!el||f.element===el)&&(!pr||f.prop===pr)&&(!st||f.state===st)&&(md!=="sure"||f.certain)&&(md!=="unsure"||!f.certain)&&(md!=="todo"||!ST[f.id]?.choice)&&fmatch(f,q));
 const by={};it.forEach(f=>(by[f.element]=by[f.element]||[]).push(f));
 const dev=it.reduce((a,f)=>a+f.devs.reduce((x,d)=>x+d.n,0),0);
 $("#rlist").innerHTML=Object.entries(by).sort((a,b)=>b[1].length-a[1].length).map(([k,fs])=>`<details class="sec" open><summary><span class="tg k-role">${E(k)}</span> ${fs.length} vai lệch <span class="muted small">· đã chọn ${fs.filter(f=>ST[f.id]?.choice).length}</span></summary>${fs.map(itemHTML).join("")}</details>`).join("")||'<p class="muted">Không có vai lệch khớp bộ lọc.</p>';
 $("#rcount").textContent=`${it.length} vai lệch · ${dev} chỗ cần đổi`;
 const okr=D.roles.filter(r=>!r.finding);
 $("#rok").innerHTML=`<summary><b>Các vai đã đồng nhất</b> ${okr.length} vai <span class="small muted">· một token, đúng nhóm</span></summary><div class="mxwrap"><table class="mx"><thead><tr><th>Phần tử</th><th>Thuộc tính</th><th>Trạng thái</th><th>Token</th><th class="num">Component</th></tr></thead><tbody>${okr.map(r=>`<tr><td>${E(r.element)}${r.part==="thân"?"":" · "+E(r.part)}${r.tone?` <span class="small muted">${E(r.tone)}</span>`:""}</td><td>${E(r.prop)}</td><td>${E(r.state)}</td><td>${r.tokens.map(t=>`<code>${E(t.name)}</code>`).join(", ")}</td><td class="num" title="${E(r.comps.join(", "))}">${r.comps.length}</td></tr>`).join("")}</tbody></table></div>`;
 $("#run").innerHTML=`<summary><b>Chưa rõ vai, cần xem</b> ${D.unresolved.length} selector <span class="small muted">· máy không suy được là phần tử gì nên không kết luận, không đưa vào so sánh</span></summary><div class="mxwrap"><table class="mx"><thead><tr><th>Component</th><th>Selector</th><th>Thuộc tính</th><th>Token</th></tr></thead><tbody>${D.unresolved.map(r=>`<tr><td>${E(r.comp)}</td><td><code>${E(r.sel)}</code></td><td>${E(r.prop)}</td><td><code>${E(r.token.replace(/^color-/,""))}</code></td></tr>`).join("")}</tbody></table></div>`;}
function roleOpts(){const R=D.findings.filter(f=>f.kind==="role"),u=k=>[...new Set(R.map(f=>f[k]))];
 $("#re").innerHTML=`<option value="">Mọi phần tử</option>${u("element").sort().map(x=>`<option>${E(x)}</option>`).join("")}`;
 $("#rp").innerHTML=`<option value="">Mọi thuộc tính</option>${u("prop").sort().map(x=>`<option>${E(x)}</option>`).join("")}`;
 $("#rs").innerHTML=`<option value="">Mọi trạng thái</option>${u("state").sort().map(x=>`<option>${E(x)}</option>`).join("")}`;}
async function save(id){const x={...ST[id],at:Date.now(),by:uid};try{localStorage.setItem("tku-"+id,JSON.stringify(x))}catch(e){}
 if(db) try{await db.doc("decisions/"+id).set(x)}catch(e){}
 document.querySelectorAll(`.item[data-id="${CSS.escape(id)}"] [data-saved]`).forEach(el=>{el.textContent=x.choice?"Đã lưu, Claude áp khi bạn gọi":"";});}
document.addEventListener("click",e=>{const b=e.target.closest("button");const c=e.target.closest(".cmp");
 const pc=e.target.closest(".cell[data-p]"); if(pc) return pdetail(pc);
 const tg=e.target.closest("[data-go]"); if(tg&&!b){const g=tg.dataset.go; show(g); return;}
 if(c){show("comps");$("#cq").value=c.dataset.c;comps();document.getElementById("c-"+c.dataset.c)?.scrollIntoView({block:"start"});return;}
 if(!b) return;
 if("ann" in b.dataset){const off=document.body.classList.toggle("noann");b.setAttribute("aria-pressed",String(!off));b.textContent="Ký hiệu: "+(off?"Tắt":"Bật");
  $$(".annhost").forEach(h=>h.classList.toggle("noann",off));try{localStorage.setItem("tku-ann",off?"0":"1")}catch(e){}return;}
 if(b.dataset.tab) return show(b.dataset.tab);
 if(b.dataset.scope) return setScope(b.dataset.scope);
 if(b.dataset.qc){show("queue");$("#qk").value="";$("#qq").value=b.dataset.qc;queue();return;}
 if(b.dataset.go){const g=b.dataset.go; if(g==="q-role"){show("roles");return;} if(g==="q-noact"){show("queue");$("#qk").value="";queue();const n=document.getElementById("q-noact");if(n){n.open=true;n.scrollIntoView({block:"start"});}return;} if(g.startsWith("q-")){show("queue");$("#qk").value=g.slice(2);queue();} else show(g); return;}
 if(b.dataset.m){$(".pvroot").setAttribute("data-"+b.dataset.m,b.dataset.v);$$(`[data-m="${b.dataset.m}"]`).forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
  $$(".pvbox:not(.hide)").forEach(box=>{const it=box.closest(".item");renderSpec(box,D.findings.find(x=>x.id===it.dataset.id));});return;}
 const it=b.closest(".item"); if(!it) return; const id=it.dataset.id;
 if("noteToggle" in b.dataset){it.classList.toggle("open");return;}
 if("pv" in b.dataset){const box=it.querySelector(".pvbox"),open=box.classList.toggle("hide")===false;b.textContent=open?"Ẩn preview":"Xem preview";
  if(open) renderSpec(box,D.findings.find(x=>x.id===id));return;}
 if("rp" in b.dataset){const box=it.querySelector(".pvbox"),open=box.classList.toggle("hide")===false;b.textContent=open?"Ẩn xem thử":"Xem thử trước, sau";
  if(open) rolePv(box,FX[id]);return;}
 if(b.dataset.a){ST[id]={...(ST[id]||{}),choice:ST[id]?.choice===b.dataset.a?null:b.dataset.a};
  it.querySelectorAll("[data-a]").forEach(x=>x.setAttribute("aria-pressed",String(ST[id].choice===x.dataset.a)));
  it.classList.toggle("done",!!ST[id].choice); if(b.dataset.a.endsWith("…")) it.classList.add("open"); save(id);}});
document.addEventListener("input",e=>{const t=e.target; if(t.tagName!=="TEXTAREA") return; const id=t.closest(".item").dataset.id;
 ST[id]={...(ST[id]||{}),note:t.value}; clearTimeout(t._t); t._t=setTimeout(()=>save(id),500);});
let curView="roles";
function writeHash(){try{const h=SCOPE+(curView==="roles"?"":"/"+curView);history.replaceState(null,"","#"+h)}catch(e){}}
function show(v){curView=v;$$("[data-tab]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.tab===v)));
 const view=v==="sem"||v==="ctok"?"tokens":v; if(view==="tokens"){curTier=v==="sem"?"semantic":"component";fopts();tokens();}
 if(view==="queue") queue(); if(view==="roles") roles();
 $$(".view").forEach(x=>x.classList.toggle("hide",x.id!=="v-"+view));writeHash();}
const SNOTE={color:'Đang xem <b>phần màu</b>: nhóm color, primitive màu, alpha, biến tự đặt mang giá trị màu, mã màu trần. Foundation Màu đã duyệt (<code>DEC-316</code>, <code>DEC-320</code>, <code>DEC-321</code>). <mark>Các foundation khác đang review, xem ở trang riêng</mark>; mục khoảng cách, bo góc, chữ ẩn ở đây. Trang chỉ quét HTML, CSS, md, <b>chưa đối chiếu biến gắn trên Figma</b> (<code>BL-346</code> là việc Figma).',
 all:'Đang xem <b>mọi foundation</b>. Khoảng cách, bo góc, chữ <mark>đang review ở trang riêng</mark>, mục của chúng ở đây chỉ để tham khảo. Trang chỉ quét HTML, CSS, md, <b>chưa đối chiếu biến gắn trên Figma</b> (<code>BL-346</code> là việc Figma).'};
function setScope(x){SCOPE=x==="all"?"all":"color";$$("[data-scope]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.scope===SCOPE)));$("#snote").innerHTML=SNOTE[SCOPE];
 try{localStorage.setItem("tku-scope",SCOPE)}catch(e){}
 qkOpts();kpis();prims();comps();queue();roles();if(curView==="sem"||curView==="ctok"){fopts();tokens();}writeHash();}
function fopts(){const tr=D.tokens.filter(r=>r.tier===curTier&&(SCOPE==="all"||r.c));const gs=[...new Set(tr.map(r=>r.group))];
 $("#fg").innerHTML=`<option value="">Mọi nhóm</option>${gs.map(g=>`<option value="${E(g)}">${E(gname(g))}</option>`).join("")}`;
 const cs=[...new Set(tr.map(r=>r.coll))];
 $("#fc").innerHTML=`<option value="">Mọi collection</option>${cs.map(c=>`<option>${E(c)}</option>`).join("")}`;
 $("#ff").innerHTML=`<option value="">Mọi cờ</option><option value="none">Chưa component nào dùng</option><option value="raw">⚠ Số trần</option>`
  +(curTier==="component"?`<option value="skipr">⚠ Trỏ thẳng Primitive</option>`:`${["single","dup"].map(k=>`<option value="${k}">${KN[k]}</option>`).join("")}`);}
roleOpts();
$("#cg").innerHTML=`<option value="">Mọi nhóm</option>${[...new Set(D.components.map(c=>c.group))].map(g=>`<option>${E(g)}</option>`).join("")}`;
["#fg","#fc","#ff","#fq"].forEach(s=>$(s).addEventListener("input",tokens));["#cq","#cg"].forEach(s=>$(s).addEventListener("input",comps));["#qk","#qq","#qn"].forEach(s=>$(s).addEventListener("input",queue));["#re","#rp","#rs","#rm","#rq"].forEach(s=>$(s).addEventListener("input",roles));
D.findings.forEach(f=>{try{const x=JSON.parse(localStorage.getItem("tku-"+f.id)||"null");if(x) ST[f.id]=x}catch(e){}});
try{if(localStorage.getItem("tku-ann")==="0"){document.body.classList.add("noann");const b=$("[data-ann]");b.setAttribute("aria-pressed","false");b.textContent="Ký hiệu: Tắt";}}catch(e){}
{const hp=location.hash.slice(1).split("/"),TABS=["roles","queue","prim","sem","ctok","comps"];let sc=hp.find(x=>x==="color"||x==="all");
 if(!sc){try{sc=localStorage.getItem("tku-scope")}catch(e){}}
 curView=hp.find(x=>TABS.includes(x))||"roles";setScope(sc||"color");show(curView);}
(async()=>{if(!window.claude?.use) return; const [d,u]=await Promise.all([claude.use("db"),claude.use("user")]); if(!d) return; db=d;
 try{uid=u?await u.id():null}catch(e){}
 let first=true;
 db.collection("decisions").onSnapshot(sn=>{let ch=false;const inDb=new Set(sn.docs.map(x=>x.id));
  if(first){first=false;Object.keys(ST).forEach(id=>{if(!inDb.has(id)&&(ST[id].choice||ST[id].note)) save(id);});} // lựa chọn cũ chỉ ở localStorage → đẩy lên kho
  sn.docs.forEach(x=>{const v=x.data();if(v&&(!ST[x.id]||(v.at||0)>=(ST[x.id].at||0))){ST[x.id]=v;ch=true}});
  if(ch&&!document.activeElement?.closest?.(".item")){queue();roles();}},()=>{});})();
"""


def page(data):
    E = html.escape
    st = data["stats"]
    blob = json.dumps({k: data[k] for k in ("date", "groups", "stats", "tokens", "components", "findings", "history", "resolved",
                                            "specimens", "bundles", "ladder", "roles", "unresolved", "matrix", "ambiguous")},
                      ensure_ascii=False).replace("</", "<\\/")
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DS v2 · Token ↔ Component</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cal+Sans&display=swap">
<style>{TCSS.read_text(encoding="utf-8")}{PAGE_CSS}</style></head><body>
<div class="band">{MARK}<div><h1>DS v2 — Token ↔ Component</h1>
<p>Quét {E(data["date"])} · {st["components"]} component · đưa component về đồng nhất token, làm phần Màu trước</p></div></div>
<div class="wrap pvroot" data-theme="light" data-platform="web">
<div class="scopebar"><b>Phạm vi</b><button type="button" data-scope="color" aria-pressed="true">Màu</button><button type="button" data-scope="all" aria-pressed="false">Tất cả</button><span class="note" id="snote"></span></div>
<div id="kpis" class="kpis"></div><div id="hist"></div>
<p class="small muted">Nguồn: <code>design-system/tokens.css</code> + spec md và trang brainstorm (<code>_work/*/page.json</code>) của từng component. Quét lại: <code>python3 _scripts/ds-token-usage.py</code> rồi nhờ Claude publish lên đúng link này. Mục <span class="tg new">Mới</span> = xuất hiện so với lần quét trước.</p>
<div class="tierbar" id="tierbar"></div>
<div class="tabs"><button data-tab="roles">Đồng nhất theo vai</button><button data-tab="queue">Cần xử lý</button><button data-tab="prim">Primitive</button><button data-tab="sem">Semantic</button><button data-tab="ctok">Component token</button><button data-tab="comps">Theo component</button>
<span class="sp"></span><button type="button" data-ann aria-pressed="true" title="Bật/tắt vùng tô và nhãn ký hiệu trên preview">Ký hiệu: Bật</button><span class="small muted">Xem thử:</span><button data-m="theme" data-v="light" aria-pressed="true">Light</button><button data-m="theme" data-v="dark" aria-pressed="false">Dark</button>
<button data-m="platform" data-v="web" aria-pressed="true">Web</button><button data-m="platform" data-v="mobile" aria-pressed="false">Mobile</button></div>

<section class="view" id="v-roles"><h2>Đồng nhất theo vai</h2>
<p class="small">Mỗi <b>vai</b> là một tổ hợp: phần tử (nút, ô nhập, mục menu, thẻ, chip) × thuộc tính (nền, chữ, viền, icon) × trạng thái (nghỉ, rê chuột, đang bấm, focus, tắt, đang chọn, lỗi). Cùng vai thì nên cùng token. Máy đọc CSS đang có hiệu lực: <b>bỏ phương án brainstorm không chọn</b>, bỏ vỏ trang duyệt, gộp <code>_forms/kit.py</code> thành 1 nguồn. Mỗi vai lệch có đề xuất, chỗ lệch, xem thử Sáng và Tối, nút chọn lưu về kho.</p>
<div class="filters"><select id="re"></select><select id="rp"></select><select id="rs"></select><select id="rm"><option value="">Mọi độ chắc</option><option value="sure">Đề xuất rõ</option><option value="unsure">Cần xem</option><option value="todo">Chưa chọn</option></select>
<input id="rq" placeholder="Tìm component hoặc vai…"><span id="rcount" class="small muted"></span></div>
<div id="rlist"></div><details class="sec" id="rok"></details><details class="sec" id="run"></details></section>

<section class="view hide" id="v-queue"><h2>Cần xử lý để đưa về nhất quán</h2>
<div class="lead" id="qlead"></div>
<p class="small">Mỗi mục chọn <b>một hướng xử lý</b> (bấm lại để bỏ chọn), cần thì thêm ghi chú bằng ✎. Lựa chọn được lưu trên trang; khi bạn bảo "áp quyết định token", Claude đọc về và trình L1/L2 trước khi sửa tokens.json / spec.</p>
<div class="filters"><select id="qk"></select><select id="qn"><option value="">Tất cả</option><option value="todo">Chưa chọn</option><option value="new">Mới so với lần trước</option></select>
<input id="qq" placeholder="Tìm token / component…"><span id="qcount" class="small muted"></span></div><p class="small muted" id="qorphan"></p><div id="queue"></div></section>

<section class="view hide" id="v-prim"><h2>Primitive — giá trị gốc, không mang nghĩa · Brand</h2>
<p class="small">Collection <code>0. Primitives</code> (thang màu, <code>space/N</code>, <code>radius/N</code>) và <code>fonts</code>; cuối trang là <code>7. Brand</code> (tầng riêng, theo khách). Component và token Component <b>không gọi thẳng</b> Primitive (DEC-115, DEC-313) — đi qua Semantic. Mỗi ô: số token semantic trỏ vào (<b>←</b>), viền đỏ = có component/token component gọi thẳng, mờ = chưa ai trỏ tới. Bấm ô để xem chi tiết.</p>
<div id="prims"></div></section>
<section class="view hide" id="v-tokens"><h2 id="ttitle">Semantic</h2><p class="small" id="tdesc"></p>
<div class="filters"><select id="fg"></select>
<select id="ff"></select><select id="fc"></select><input id="fq" placeholder="Tìm token hoặc component…"><span id="tcount" class="small muted"></span></div>
<p class="small muted">Ô viền liền = component gọi token trực tiếp · viền đứt = dùng gián tiếp qua token khác. Bấm tên component để xem chi tiết.</p>
<table><thead><tr><th style="width:56px"></th><th>Token</th><th class="hidem">Giá trị (Light/Web, chỉ ghi chế độ khác)</th><th>Trỏ về</th><th>Component dùng</th><th style="width:40px">#</th></tr></thead><tbody id="tbody"></tbody></table></section>

<section class="view hide" id="v-comps"><h2>Theo component</h2>
<h3 style="font:600 14px Inter;margin:6px 0">Tình trạng màu, nhiều việc xếp trên</h3>
<p class="small muted">Trang <b>chỉ quét HTML, CSS, md; chưa đối chiếu biến gắn trên Figma</b> (<code>BL-346</code> là việc Figma). <b>% dùng đúng Semantic</b> = số khai báo màu đang có hiệu lực gọi thẳng token Semantic (biến theo biến thể tính là đúng). <b>Lệch mốc</b> đọc từ <code>components/_deps.json</code>: sổ này theo dõi theo từng mục foundation và component con, không theo từng token, nên "gồm Màu" nghĩa là foundation Màu đã đổi từ lúc dựng.</p>
<div class="mxwrap" id="matrix"></div>
<h3 style="font:600 14px Inter;margin:14px 0 6px">Chi tiết từng component</h3>
<div class="filters"><input id="cq" placeholder="Tìm component…"><select id="cg"></select></div>
<p class="small muted">Thanh màu = tỷ lệ token theo nhóm foundation. Xếp component nhiều mục cần xử lý lên đầu.</p><div id="cards" class="cards"></div></section>
</div><script id="data" type="application/json">{blob}</script><script>{PAGE_JS}</script></body></html>"""


def main():
    data = build()
    st = data["stats"]
    print(f"token: {st['tokens']} · text style {st['styles']} · component {st['components']} · đang dùng {st['usedPct']}%")
    print("cần xử lý:", ", ".join(f"{k} {v}" for k, v in sorted(st["findings"].items(), key=lambda x: -x[1])))
    ct = st["color"]
    print("phần màu:", ", ".join(f"{k} {v}" for k, v in sorted(ct["todo"].items(), key=lambda x: -x[1])),
          "· không cần xử lý:", ", ".join(f"{k} {v}" for k, v in sorted(ct["noact"].items(), key=lambda x: -x[1])) or "0",
          f"· vai {ct['roles']} ({ct['rolesOk']} đã đồng nhất, {ct['unresolved']} selector chưa rõ vai)")
    if "--summary" in sys.argv:
        return
    if "--check" in sys.argv:  # gate DEC-313: FAIL khi token Component trỏ Primitive; css/md gọi Primitive chỉ WARN
        f = data["findings"]
        skip = [x["title"] for x in f if x["kind"] == "skip"]
        prim = [x["title"] for x in f if x["kind"] == "prim"]
        print(f"FAIL {len(skip)} · token Component trỏ thẳng Primitive" + "".join(f"\n  ✕ {t}" for t in skip))
        print(f"WARN {len(prim)} · css/spec component gọi thẳng Primitive" + "".join(f"\n  ! {t}" for t in prim[:40]))
        rl = [x for x in f if x["kind"] == "role"]
        sn = [x for x in f if x["kind"] == "stale-name"]
        bl = [x["title"] for x in f if x["kind"] == "brandleak"]
        print(f"WARN {len(bl)} · component gọi màu thương hiệu Invlogis (DEC-261)" + "".join(f"\n  ! {t}" for t in bl[:40]))
        rm = [x["title"] for x in f if x["kind"] == "rawmotion"]
        print(f"WARN {len(rm)} · chuyển động số trần, không qua --duration-* (DEC-333)" + "".join(f"\n  ! {t}" for t in rm[:40]))
        print(f"WARN {len(rl)} · cùng vai lệch token (phần màu)")
        print(f"WARN {len(sn)} · tên màu cũ còn sót (phần màu)")
        sys.exit(1 if skip else 0)
    data = with_history(data)
    OUT_J.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    doc = page(data)
    OUT_H.write_text(doc, encoding="utf-8")
    print(f"Đã sinh {OUT_J.relative_to(ROOT)} + {OUT_H.relative_to(ROOT)} ({len(doc) // 1024} KB)"
          + (f" · artifact {data['artifact']}" if data.get("artifact") else " · chưa publish"))


if __name__ == "__main__":
    main()
