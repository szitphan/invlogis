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
  semantic   1. Semantic + 2.–5. Platform (Radius, Spacing & Layout, Typography, Sizes) + text style, elev, motion, grid…
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
Quyết định user chọn trên trang nằm ở kho của artifact (collection "decisions", doc = id mục); Claude đọc về rồi áp (L1/L2).
"""
import html
import importlib.util
import json
import re
import sys
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

PAL = re.compile(r"((neutral|blue|teal|purple|yellow|green|red|orange|charcoal|alpha)-[\w-]+|white|black)$")
PRIM_DIM = re.compile(r"(space-\d+|radius-\d+)$")
GROUPS = [  # (mã, tên, tiền tố) — thứ tự = thứ tự hiển thị; khớp 9 mục foundations/
    ("color", "Màu", ("color-",)),
    ("type", "Chữ", ("type-", "font-")),
    ("radius", "Bo góc", ("radius-",)),
    ("space", "Khoảng cách, bố cục", ("space-", "layout-")),
    ("grid", "Lưới, độ rộng", ("grid-", "width-", "bp-")),
    ("elevation", "Lớp nổi, làm mờ", ("elev-", "blur-")),
    ("touch-focus", "Vùng chạm, focus", ("touch-", "focus-")),
    ("motion", "Chuyển động", ("duration-", "ease-")),
    ("icon", "Icon", ("icon-",)),
]
RETIRED = ("card-", "list-row-")  # token đã bỏ (DEC-312), còn chép trong kit dump của trang _work cũ
OTHER = [("elev-", "effectStyles"), ("blur-", "blur"), ("duration-", "motion"), ("easing-", "motion"), ("grid-", "grid"),
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
def scan_component(slug, toks):
    names, local, lits, bare = set(), {}, Counter(), 0
    pj = dd.COMP / "_work" / slug / "page.json"
    if pj.exists():
        p = json.loads(pj.read_text())
        c = p.get("css") or ""
        c = re.sub(r"--([\w-]+)\s*:\s*[^;{}]*;?", lambda m: "" if m.group(1) in toks or m.group(1).startswith(RETIRED) else m.group(0), c)
        extra = json.dumps([p.get(k) for k in ("cssScreen", "preview", "proto")], ensure_ascii=False)
        for m in re.finditer(r"--([\w-]+)\s*:\s*([^;{}\"]*)", c + "\n" + extra):
            if m.group(1) not in toks and not m.group(1).startswith(RETIRED):  # token đã bỏ chép sẵn trong kit
                local.setdefault(m.group(1), m.group(2).strip())
        names |= set(re.findall(r"var\(--([\w-]+)", c))
        body = re.sub(r"var\(--[\w-]+(?:,[^()]*(?:\([^()]*\))?[^()]*)?\)", "", c)
        for h in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)", body):
            lits[h.lower().replace(" ", "")] += 1
        bare = sum(1 for v in p.get("values") or [] if isinstance(v, dict) and not v.get("token"))
    m = dd.md_of(slug)
    if m:
        s = m.read_text(encoding="utf-8")
        names |= set(re.findall(r"var\(--([\w-]+)", s))
        names |= {expand(t.replace("/", "-"), slug, toks) for t in re.findall(r"`([a-z][a-z0-9-]*(?:/[a-z0-9-]+)+)`", s)}
    used = sorted(n for n in names if n in toks)
    unknown = sorted(n for n in names if n not in toks and n not in local
                     and not re.match(r"icon-(?!size|stroke)", n) and not n.endswith("-md"))
    return {"used": used, "unknown": unknown, "local": local, "literals": dict(lits), "bare": bare,
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
        if t["tier"] == "component" or t.get("style"):
            continue
        v = (resolve(toks, n, "light", "web") or "").lower().replace(" ", "")
        if v:
            idx[v].append(n)
    for v in idx:
        idx[v].sort(key=lambda n: (toks[n]["tier"] != "semantic", len(n)))
    return idx


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

    def F(fid, kind_, title, **kw):
        findings.append({"id": fid, "kind": kind_, "title": title, **kw})

    tok_rows = []
    for n, t in toks.items():
        vals = {f"{a}-{b}": resolve(toks, n, a, b) for a, b in CTXS}
        users = sorted(direct[n] | via[n])
        tok_rows.append({"name": n, "tier": t["tier"], "group": t["group"], "kind": kind(vals["light-web"]),
                         "raw": t["defs"][0][1] if t["defs"] else "", "refs": sorted(t["refs"]),
                         "vals": vals, "direct": sorted(direct[n]), "via": sorted(via[n] - direct[n]),
                         "style": bool(t.get("style")), "coll": t["coll"], "jname": t["jname"],
                         "refBy": sorted(x for x, u in toks.items() if n in u["refs"]),
                         "rawVal": bool(not t["refs"] and t["tier"] != "primitive" and not t.get("style"))})
        if t["tier"] == "primitive":
            continue
        if not users:
            F(f"unused--{n}", "unused", n, token=n, tier=t["tier"], group=t["group"])
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
            F("dup--" + "--".join(sorted(ns))[:120], "dup", " = ".join(sorted(ns)), tokens=sorted(ns), group=g, value=vs[0],
              comps=sorted({c for n in ns for c in direct[n] | via[n]}))
    for s, c in comps.items():
        for n in c["used"]:
            if toks[n]["tier"] == "primitive" and not n.startswith("font-"):
                alt = [x for x in hidx.get((resolve(toks, n, "light", "web") or "").lower(), []) if toks[x]["tier"] == "semantic"]
                F(f"prim--{s}--{n}", "prim", f"{s} gọi {n}", comp=s, prim=n, where=c["src"], alt=alt[:3])
        for a, v in c["local"].items():
            refs = re.findall(r"var\(--([\w-]+)", v)
            F(f"alias--{s}--{a}", "alias", f"{s}: --{a}", comp=s, alias=a, value=v, maps=[r for r in refs if r in toks])
        for n in c["unknown"]:
            F(f"unknown--{s}--{n}", "unknown", f"{s} gọi {n}", comp=s, token=n, where=c["src"])
        for h, k in sorted(c["literals"].items(), key=lambda x: -x[1]):
            F(f"literal--{s}--{re.sub(r'[^a-z0-9]+', '-', h)}", "literal", f"{s}: {h}", comp=s, value=h, count=k,
              alt=hidx.get(h, [])[:3])
    comp_rows = []
    for s, c in sorted(comps.items()):
        g = Counter(toks[n]["group"] for n in c["used"])
        comp_rows.append({"slug": s, "group": c["group"], "src": c["src"], "used": c["used"], "unknown": c["unknown"],
                          "local": c["local"], "literals": c["literals"], "bare": c["bare"], "byGroup": dict(g),
                          "issues": sum(1 for f in findings if f.get("comp") == s)})
    counts = Counter(f["kind"] for f in findings)
    tiers = Counter(r["tier"] for r in tok_rows if not r["style"])
    tiers["style"] = sum(1 for r in tok_rows if r["style"])
    used_f = sum(1 for r in tok_rows if r["tier"] != "primitive" and not r["style"] and (r["direct"] or r["via"]))
    stats = {"tokens": dict(tiers), "styles": sum(1 for r in tok_rows if r["style"]), "components": len(comps),
             "usedPct": round(100 * used_f / max(1, tiers["semantic"] + tiers["component"])), "findings": dict(counts)}
    spec, bundles = specimens(toks, findings)
    return {"date": TODAY, "groups": [[k, n] for k, n, _ in GROUPS], "stats": stats, "tokens": tok_rows,
            "components": comp_rows, "findings": findings, "specimens": spec, "bundles": bundles, "ladder": LADDER_NAME}


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
    hist.append({"date": TODAY, **data["stats"]["findings"], "total": len(cur)})
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
.item{border-top:1px solid #EEF2F6;padding:10px 16px;display:grid;grid-template-columns:1fr auto;gap:6px 16px}
.item .act{display:flex;gap:4px;flex-wrap:wrap;justify-content:flex-end}
.item .act button{border:1px solid #CBD5E1;background:#fff;border-radius:999px;padding:3px 10px;font:600 12px Inter;cursor:pointer}
.item .act button[aria-pressed=true]{background:#0036B5;color:#fff;border-color:#0036B5}
.item textarea{grid-column:1/-1;min-height:34px;border:1px solid #CBD5E1;border-radius:8px;padding:6px 8px;font:12px Inter;display:none}
.item.open textarea{display:block}.item.done{background:#F6FEF9}
.saved{font-size:11px;color:#067647}.hide{display:none!important}
.hist{display:flex;gap:4px;align-items:flex-end;height:40px}.hist i{display:block;width:14px;background:#0036B5;border-radius:2px 2px 0 0}
@media (max-width:700px){.wrap{padding:12px}.band{padding:16px}.item{grid-template-columns:1fr}.item .act{justify-content:flex-start}
.hidem{display:none}.cards{grid-template-columns:1fr}}
"""

PAGE_JS = r"""
const D=JSON.parse(document.getElementById("data").textContent);
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],E=s=>String(s??"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const GN=Object.fromEntries(D.groups); const gname=g=>GN[g]||(g.startsWith("c:")?"Component · "+g.slice(2):g);
const KN={compraw:"Component số trần",skip:"Component trỏ Primitive",unused:"Chưa dùng",single:"Lẻ — 1 component",prim:"Gọi thẳng primitive",alias:"Biến tự đặt",unknown:"Token không tồn tại",literal:"Màu viết trần",dup:"Trùng giá trị"};
const KWHY={
 skip:"Token tầng <b>Component</b> (<code>6. Component sizes</code>) <b>trỏ thẳng Primitive</b>, trái <b>DEC-313</b>: token component chỉ được trỏ Semantic (<code>1.</code>–<code>5.</code>) hoặc Brand theo vai. Gợi ý = token Semantic cùng giá trị (màu: cùng Light; số đo: cùng cặp Web/Mobile). Không có gợi ý → cần <mark>thêm bậc Semantic</mark> hoặc đổi số.",
 compraw:"Token tầng <b>Component</b> ghi <b>số trần</b>, gom theo giá trị. Theo DEC-313 cũng phải trỏ Semantic. Gợi ý = Semantic cùng giá trị nếu có; không có → chọn bậc gần nhất hoặc thêm thang Semantic (vd <code>size/*</code> cho cỡ khối).",
 unused:"Token có trong tokens.css nhưng <b>không component nào dùng</b>, kể cả gián tiếp. Hoặc chưa tới lượt component cần nó (giữ), hoặc là <mark>token thừa</mark> (bỏ).",
 single:"Token semantic <b>chỉ 1 component dùng</b>. Semantic phải dùng chung; chỉ 1 nơi dùng thường là <mark>token riêng lẻ</mark>: gộp vào token sẵn có, hoặc chuyển thành token component.",
 prim:"CSS hoặc spec của component <b>gọi thẳng primitive màu</b> (neutral-300, red-100…), trái <b>DEC-115</b>. Đổi Light/Dark hay đổi brand sẽ lệch. Nên đi qua token semantic.",
 alias:"Component <b>tự đặt biến cục bộ</b> (--fg2, --line…) thay vì gọi token hệ thống. Đây là nguồn chính của <mark>token riêng lẻ</mark>: thay bằng token hệ thống, hoặc đưa lên tokens.css nếu thật sự cần.",
 unknown:"Component <b>gọi tên token không có</b> trong tokens.css. Có thể tên cũ (l1), viết sai, hoặc token chưa tạo.",
 literal:"Màu <b>viết trần</b> (hex/rgb) trong css component, không qua token. Cột gợi ý là token có đúng giá trị đó.",
 dup:"Các token semantic <b>cùng nhóm, cùng giá trị ở cả 4 chế độ</b> (Light/Dark × Web/Mobile). Có thể cố ý (khác vai trò), hoặc <mark>gộp được</mark>."};
const KACT={compraw:["Trỏ Semantic cùng số","Làm tròn về bậc gần nhất…","Thêm bậc Semantic mới…","Ngoại lệ (giữ số, ghi lý do)…"],skip:["Trỏ Semantic gợi ý","Làm tròn về bậc gần nhất…","Thêm bậc Semantic mới…"],
 unused:["Giữ","Bỏ token"],single:["Giữ","Gộp vào…","Chuyển thành token component"],prim:["Giữ","Đổi sang token semantic"],
 alias:["Thay bằng token hệ thống","Đưa lên tokens.css","Giữ (khung xem thử)"],unknown:["Sửa tên","Tạo token","Bỏ qua (spec cũ)"],
 literal:["Đổi sang token","Giữ (khung xem thử)"],dup:["Giữ cả hai","Gộp vào…"]};
const ORDER=["skip","compraw","prim","alias","unknown","literal","single","dup","unused"];
const TIERN={primitive:"Primitive",semantic:"Semantic",component:"Component token",brand:"Brand"};
let db=null,uid=null,curTier="semantic"; const ST={};
function kpis(){const s=D.stats,f=s.findings,t=s.tokens;
 const k=(n,l,c,go)=>`<button class="kpi ${c}" data-go="${go}"><b>${n}</b><span>${l}</span></button>`;
 const tb=(n,l,sub,go)=>`<div role="button" data-go="${go}" style="cursor:pointer"><span class="tg t-${go==="prim"?"primitive":go==="sem"?"semantic":"component"}">${l}</span><br><b>${n}</b> <span class="small muted">${sub}</span></div>`;
 $("#tierbar").innerHTML=tb(t.primitive||0,"Primitive","0. Primitives · fonts","prim")+'<div class="arw">→</div>'
  +tb((t.semantic||0)+(t.style||0),"Semantic",`1. Semantic · 2.–5. Platform · ${t.style||0} text style`,"sem")+'<div class="arw">→</div>'+tb(t.component||0,"Component token","6. Component sizes · 8. Component","ctok")+tb(t.brand||0,"Brand","7. Brand · theo vai §3.5","prim");
 $("#kpis").innerHTML=k(s.usedPct+"%","token semantic + component đang có component dùng",s.usedPct>=80?"ok":"warn","sem")+k(s.components,"component đã quét","","comps")
  +ORDER.map(x=>k(f[x]||0,KN[x],["skip","prim","alias","unknown"].includes(x)?(f[x]?"bad":"ok"):(f[x]?"warn":"ok"),"q-"+x)).join("");
 const h=D.history||[]; if(h.length>1){const mx=Math.max(...h.map(x=>x.total));
  $("#hist").innerHTML=`<span class="small muted">Tổng mục cần xử lý qua các lần quét:</span><div class="hist">${h.map(x=>`<i title="${x.date}: ${x.total}" style="height:${Math.max(3,40*x.total/mx)}px"></i>`).join("")}</div>`;}
 if(D.resolved?.length) $("#hist").innerHTML+=`<p class="small">✅ ${D.resolved.length} mục đã hết so với lần quét trước.</p>`;}
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
const TDESC={semantic:"Token mang <b>nghĩa / vai trò</b>: <code>1. Semantic</code> (màu, Light/Dark) + <code>2.–5. Platform</code> (bo góc, khoảng cách, chữ, cỡ; Web/Mobile) + text style, elev, motion, grid. Trỏ về Primitive; số trần ở tầng này là giá trị thang (vd cỡ chữ), không phải lỗi.",
 component:"Token riêng của một component: <code>6. Platform · Component sizes</code> (số đo) + <code>8. Component</code> (màu trạng thái, DEC-174). Chuẩn DEC-313: <b>chỉ trỏ Semantic</b> hoặc Brand theo vai; ⚠ khi trỏ thẳng Primitive hoặc ghi số trần."};
function tokens(){const g=$("#fg").value,f=$("#ff").value,c=$("#fc").value,q=$("#fq").value.trim().toLowerCase();
 $("#ttitle").textContent=TIERN[curTier]; $("#tdesc").innerHTML=TDESC[curTier];
 let rows=D.tokens.filter(r=>r.tier===curTier&&(!g||r.group===g||(g==="comp"&&r.group.startsWith("c:")))&&(!c||r.coll===c)&&(!q||r.name.includes(q)||[...r.direct,...r.via].some(x=>x.includes(q))));
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
 $("#tbody").innerHTML=h||`<tr><td colspan="6" class="muted">Không có token khớp bộ lọc.</td></tr>`; $("#tcount").textContent=rows.length+" token";}
function prims(){const P=D.tokens.filter(r=>r.tier==="primitive"||r.tier==="brand");
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
function comps(){const q=$("#cq").value.trim().toLowerCase(),gs=$("#cg").value;
 const cols={color:"#0036B5",type:"#7A5AF8",radius:"#00A2FF",space:"#12B76A",grid:"#F79009",elevation:"#667085",["touch-focus"]:"#F04438",motion:"#2E90FA",icon:"#344054"};
 $("#cards").innerHTML=D.components.filter(c=>(!q||c.slug.includes(q))&&(!gs||c.group===gs)).sort((a,b)=>b.issues-a.issues).map(c=>{
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
function itemHTML(f){const s=ST[f.id]||{};const acts=KACT[f.kind];
 let d="";
 if(f.kind==="unused") d=`<span class="tg t-${f.tier}">${f.tier}</span> ${E(gname(f.group))}`;
 if(f.kind==="single") d=`chỉ <span class="cmp" data-c="${f.comps[0]}">${E(f.comps[0])}</span> dùng`;
 if(f.kind==="prim") d=`${f.comps?`ảnh hưởng ${f.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:`trong <code>${E(f.where)}</code>`}${f.alt?.length?` · gợi ý: <code>${f.alt.map(E).join(" / ")}</code>`:" · <mark>chưa có token semantic cùng giá trị</mark>"}`;
 if(f.kind==="alias") d=`<code>--${E(f.alias)}: ${E(f.value)}</code>${f.maps.length?` · trỏ tới <code>${f.maps.map(E).join(", ")}</code>`:" · <mark>giá trị trần</mark>"}`;
 if(f.kind==="unknown") d=`trong <code>${E(f.where)}</code>`;
 if(f.kind==="literal") d=`<span class="pv" style="display:inline-grid;width:22px;height:16px;vertical-align:middle"><i class="sw" style="background:${E(f.value)}"></i></span> ${f.count} lần${f.alt.length?` · gợi ý: <code>${f.alt.map(E).join(" / ")}</code>`:" · <mark>không token nào trùng giá trị</mark>"}`;
 if(f.kind==="dup") d=`giá trị <code>${E(f.value)}</code>${f.comps.length?` · dùng ở ${f.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:""}`;
 if(f.kind==="compraw") d=`${f.tokens.slice(0,6).map(x=>`<code>${E(x)}</code>`).join(", ")}${f.tokens.length>6?` … +${f.tokens.length-6}`:""}${f.alt.length?` · Semantic cùng số: <code>${f.alt.map(E).join(" / ")}</code>`:" · <mark>chưa có Semantic cùng số</mark>"}${f.near?`<br>Bậc gần nhất (thang space/size): <b>${E(f.near)}</b>`:""}`;
 if(f.kind==="skip") d=`${f.alt.length?`gợi ý: <code>${f.alt.map(E).join(" / ")}</code>`:"<mark>chưa có semantic cùng giá trị</mark>"}${f.comps.length?` · ảnh hưởng ${f.comps.map(c=>`<span class="cmp" data-c="${c}">${E(c)}</span>`).join("")}`:""}`;
 return `<div class="item${s.choice?" done":""}${s.choice&&s.choice.endsWith("…")?" open":""}" data-id="${E(f.id)}"><div><code>${E(f.title)}</code> ${f.new?'<span class="tg new">Mới</span>':""}<div class="small muted">${d}</div><span class="saved" data-saved></span></div>
  <div class="act">${acts.map(a=>`<button type="button" data-a="${E(a)}" aria-pressed="${s.choice===a}">${E(a)}</button>`).join("")}<button type="button" data-note-toggle title="Ghi chú">✎</button>${(f.kind==="compraw"||f.kind==="skip")?'<button type="button" class="pvbtn" data-pv>Xem preview</button>':""}</div>
  <textarea placeholder="Ghi chú / gộp vào token nào…">${E(s.note||"")}</textarea><div class="pvbox hide"></div></div>`;}
function queue(){const fk=$("#qk").value,fq=$("#qq").value.trim().toLowerCase(),only=$("#qn").value;
 $("#queue").innerHTML=ORDER.filter(k=>!fk||k===fk).map(k=>{let it=D.findings.filter(f=>f.kind===k&&(!fq||f.id.includes(fq)));
  if(only==="todo") it=it.filter(f=>!ST[f.id]?.choice); if(only==="new") it=it.filter(f=>f.new);
  if(!it.length) return "";
  const done=it.filter(f=>ST[f.id]?.choice).length;
  return `<details class="sec" id="q-${k}" ${fk||it.length<=12?"open":""}><summary><span class="tg k-${k}">${KN[k]}</span> ${it.length} mục <span class="muted small">· đã chọn ${done}</span></summary>
  <div class="why">${KWHY[k]}</div>${it.map(itemHTML).join("")}</details>`;}).join("")||`<p class="muted">Không còn mục nào khớp bộ lọc.</p>`;
 const tot=D.findings.length,dn=D.findings.filter(f=>ST[f.id]?.choice).length; $("#qcount").textContent=`${dn}/${tot} mục đã chọn hướng xử lý`;}
async function save(id){const x={...ST[id],at:Date.now(),by:uid};try{localStorage.setItem("tku-"+id,JSON.stringify(x))}catch(e){}
 if(db) try{await db.doc("decisions/"+id).set(x)}catch(e){}
 const el=document.querySelector(`.item[data-id="${CSS.escape(id)}"] [data-saved]`); if(el) el.textContent=x.choice?"Đã lưu — Claude áp khi bạn gọi":"";}
document.addEventListener("click",e=>{const b=e.target.closest("button");const c=e.target.closest(".cmp");
 const pc=e.target.closest(".cell[data-p]"); if(pc) return pdetail(pc);
 const tg=e.target.closest("[data-go]"); if(tg&&!b){const g=tg.dataset.go; show(g); return;}
 if(c){show("comps");$("#cq").value=c.dataset.c;comps();document.getElementById("c-"+c.dataset.c)?.scrollIntoView({block:"start"});return;}
 if(!b) return;
 if("ann" in b.dataset){const off=document.body.classList.toggle("noann");b.setAttribute("aria-pressed",String(!off));b.textContent="Ký hiệu: "+(off?"Tắt":"Bật");
  $$(".annhost").forEach(h=>h.classList.toggle("noann",off));try{localStorage.setItem("tku-ann",off?"0":"1")}catch(e){}return;}
 if(b.dataset.tab) return show(b.dataset.tab);
 if(b.dataset.go){const g=b.dataset.go; if(g.startsWith("q-")){show("queue");$("#qk").value=g.slice(2);queue();} else show(g); return;}
 if(b.dataset.m){$(".pvroot").setAttribute("data-"+b.dataset.m,b.dataset.v);$$(`[data-m="${b.dataset.m}"]`).forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
  $$(".pvbox:not(.hide)").forEach(box=>{const it=box.closest(".item");renderSpec(box,D.findings.find(x=>x.id===it.dataset.id));});return;}
 const it=b.closest(".item"); if(!it) return; const id=it.dataset.id;
 if("noteToggle" in b.dataset){it.classList.toggle("open");return;}
 if("pv" in b.dataset){const box=it.querySelector(".pvbox"),open=box.classList.toggle("hide")===false;b.textContent=open?"Ẩn preview":"Xem preview";
  if(open) renderSpec(box,D.findings.find(x=>x.id===id));return;}
 if(b.dataset.a){ST[id]={...(ST[id]||{}),choice:ST[id]?.choice===b.dataset.a?null:b.dataset.a};
  it.querySelectorAll("[data-a]").forEach(x=>x.setAttribute("aria-pressed",String(ST[id].choice===x.dataset.a)));
  it.classList.toggle("done",!!ST[id].choice); if(b.dataset.a.endsWith("…")) it.classList.add("open"); save(id);}});
document.addEventListener("input",e=>{const t=e.target; if(t.tagName!=="TEXTAREA") return; const id=t.closest(".item").dataset.id;
 ST[id]={...(ST[id]||{}),note:t.value}; clearTimeout(t._t); t._t=setTimeout(()=>save(id),500);});
function show(v){$$("[data-tab]").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.tab===v)));
 const view=v==="sem"||v==="ctok"?"tokens":v; if(view==="tokens"){curTier=v==="sem"?"semantic":"component";fopts();tokens();}
 $$(".view").forEach(x=>x.classList.toggle("hide",x.id!=="v-"+view));
 try{history.replaceState(null,"","#"+v)}catch(e){}}
function fopts(){const gs=[...new Set(D.tokens.filter(r=>r.tier===curTier).map(r=>r.group))];
 $("#fg").innerHTML=`<option value="">Mọi nhóm</option>${gs.map(g=>`<option value="${E(g)}">${E(gname(g))}</option>`).join("")}`;
 const cs=[...new Set(D.tokens.filter(r=>r.tier===curTier).map(r=>r.coll))];
 $("#fc").innerHTML=`<option value="">Mọi collection</option>${cs.map(c=>`<option>${E(c)}</option>`).join("")}`;
 $("#ff").innerHTML=`<option value="">Mọi cờ</option><option value="none">Chưa component nào dùng</option><option value="raw">⚠ Số trần</option>`
  +(curTier==="component"?`<option value="skipr">⚠ Trỏ thẳng Primitive</option>`:`${["single","dup"].map(k=>`<option value="${k}">${KN[k]}</option>`).join("")}`);}
$("#qk").innerHTML=`<option value="">Mọi loại</option>${ORDER.map(k=>`<option value="${k}">${KN[k]} (${D.stats.findings[k]||0})</option>`).join("")}`;
$("#cg").innerHTML=`<option value="">Mọi nhóm</option>${[...new Set(D.components.map(c=>c.group))].map(g=>`<option>${E(g)}</option>`).join("")}`;
["#fg","#fc","#ff","#fq"].forEach(s=>$(s).addEventListener("input",tokens));["#cq","#cg"].forEach(s=>$(s).addEventListener("input",comps));["#qk","#qq","#qn"].forEach(s=>$(s).addEventListener("input",queue));
D.findings.forEach(f=>{try{const x=JSON.parse(localStorage.getItem("tku-"+f.id)||"null");if(x) ST[f.id]=x}catch(e){}});
try{if(localStorage.getItem("tku-ann")==="0"){document.body.classList.add("noann");const b=$("[data-ann]");b.setAttribute("aria-pressed","false");b.textContent="Ký hiệu: Tắt";}}catch(e){}
kpis();prims();comps();queue();{const h=location.hash.slice(1);show(["prim","sem","ctok","comps","queue"].includes(h)?h:"queue");}
(async()=>{if(!window.claude?.use) return; const [d,u]=await Promise.all([claude.use("db"),claude.use("user")]); if(!d) return; db=d;
 try{uid=u?await u.id():null}catch(e){}
 let first=true;
 db.collection("decisions").onSnapshot(sn=>{let ch=false;const inDb=new Set(sn.docs.map(x=>x.id));
  if(first){first=false;Object.keys(ST).forEach(id=>{if(!inDb.has(id)&&(ST[id].choice||ST[id].note)) save(id);});} // lựa chọn cũ chỉ ở localStorage → đẩy lên kho
  sn.docs.forEach(x=>{const v=x.data();if(v&&(!ST[x.id]||(v.at||0)>=(ST[x.id].at||0))){ST[x.id]=v;ch=true}});
  if(ch&&!document.activeElement?.closest?.(".item")) queue();},()=>{});})();
"""


def page(data):
    E = html.escape
    st = data["stats"]
    blob = json.dumps({k: data[k] for k in ("date", "groups", "stats", "tokens", "components", "findings", "history", "resolved",
                                            "specimens", "bundles", "ladder")},
                      ensure_ascii=False).replace("</", "<\\/")
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DS v2 · Token ↔ Component</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cal+Sans&display=swap">
<style>{TCSS.read_text(encoding="utf-8")}{PAGE_CSS}</style></head><body>
<div class="band">{MARK}<div><h1>DS v2 — Token ↔ Component</h1>
<p>Quét {E(data["date"])} · {st["components"]} component · token nào đang được dùng ở đâu, token nào lẻ, component nào tự đặt giá trị ngoài hệ</p></div></div>
<div class="wrap pvroot" data-theme="light" data-platform="web">
<div id="kpis" class="kpis"></div><div id="hist"></div>
<p class="small muted">Nguồn: <code>design-system/tokens.css</code> + spec md và trang brainstorm (<code>_work/*/page.json</code>) của từng component. Quét lại: <code>python3 _scripts/ds-token-usage.py</code> rồi nhờ Claude publish lên đúng link này. Mục <span class="tg new">Mới</span> = xuất hiện so với lần quét trước.</p>
<div class="tierbar" id="tierbar"></div>
<div class="tabs"><button data-tab="queue">Cần xử lý</button><button data-tab="prim">Primitive</button><button data-tab="sem">Semantic</button><button data-tab="ctok">Component token</button><button data-tab="comps">Theo component</button>
<span class="sp"></span><button type="button" data-ann aria-pressed="true" title="Bật/tắt vùng tô và nhãn ký hiệu trên preview">Ký hiệu: Bật</button><span class="small muted">Xem thử:</span><button data-m="theme" data-v="light" aria-pressed="true">Light</button><button data-m="theme" data-v="dark" aria-pressed="false">Dark</button>
<button data-m="platform" data-v="web" aria-pressed="true">Web</button><button data-m="platform" data-v="mobile" aria-pressed="false">Mobile</button></div>

<section class="view" id="v-queue"><h2>Cần xử lý để đưa về nhất quán</h2>
<p class="small">Mỗi mục chọn <b>một hướng xử lý</b> (bấm lại để bỏ chọn), cần thì thêm ghi chú bằng ✎. Lựa chọn được lưu trên trang; khi bạn bảo "áp quyết định token", Claude đọc về và trình L1/L2 trước khi sửa tokens.json / spec.</p>
<div class="filters"><select id="qk"></select><select id="qn"><option value="">Tất cả</option><option value="todo">Chưa chọn</option><option value="new">Mới so với lần trước</option></select>
<input id="qq" placeholder="Tìm token / component…"><span id="qcount" class="small muted"></span></div><div id="queue"></div></section>

<section class="view hide" id="v-prim"><h2>Primitive — giá trị gốc, không mang nghĩa · Brand</h2>
<p class="small">Collection <code>0. Primitives</code> (thang màu, <code>space/N</code>, <code>radius/N</code>) và <code>fonts</code>; cuối trang là <code>7. Brand</code> (tầng riêng, theo khách). Component và token Component <b>không gọi thẳng</b> Primitive (DEC-115, DEC-313) — đi qua Semantic. Mỗi ô: số token semantic trỏ vào (<b>←</b>), viền đỏ = có component/token component gọi thẳng, mờ = chưa ai trỏ tới. Bấm ô để xem chi tiết.</p>
<div id="prims"></div></section>
<section class="view hide" id="v-tokens"><h2 id="ttitle">Semantic</h2><p class="small" id="tdesc"></p>
<div class="filters"><select id="fg"></select>
<select id="ff"></select><select id="fc"></select><input id="fq" placeholder="Tìm token hoặc component…"><span id="tcount" class="small muted"></span></div>
<p class="small muted">Ô viền liền = component gọi token trực tiếp · viền đứt = dùng gián tiếp qua token khác. Bấm tên component để xem chi tiết.</p>
<table><thead><tr><th style="width:56px"></th><th>Token</th><th class="hidem">Giá trị (Light/Web, chỉ ghi chế độ khác)</th><th>Trỏ về</th><th>Component dùng</th><th style="width:40px">#</th></tr></thead><tbody id="tbody"></tbody></table></section>

<section class="view hide" id="v-comps"><h2>Theo component</h2>
<div class="filters"><input id="cq" placeholder="Tìm component…"><select id="cg"></select></div>
<p class="small muted">Thanh màu = tỷ lệ token theo nhóm foundation. Xếp component nhiều mục cần xử lý lên đầu.</p><div id="cards" class="cards"></div></section>
</div><script id="data" type="application/json">{blob}</script><script>{PAGE_JS}</script></body></html>"""


def main():
    data = build()
    st = data["stats"]
    print(f"token: {st['tokens']} · text style {st['styles']} · component {st['components']} · đang dùng {st['usedPct']}%")
    print("cần xử lý:", ", ".join(f"{k} {v}" for k, v in sorted(st["findings"].items(), key=lambda x: -x[1])))
    if "--summary" in sys.argv:
        return
    if "--check" in sys.argv:  # gate DEC-313: FAIL khi token Component trỏ Primitive; css/md gọi Primitive chỉ WARN
        f = data["findings"]
        skip = [x["title"] for x in f if x["kind"] == "skip"]
        prim = [x["title"] for x in f if x["kind"] == "prim"]
        print(f"FAIL {len(skip)} · token Component trỏ thẳng Primitive" + "".join(f"\n  ✕ {t}" for t in skip))
        print(f"WARN {len(prim)} · css/spec component gọi thẳng Primitive" + "".join(f"\n  ! {t}" for t in prim[:40]))
        sys.exit(1 if skip else 0)
    data = with_history(data)
    OUT_J.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    doc = page(data)
    OUT_H.write_text(doc, encoding="utf-8")
    print(f"Đã sinh {OUT_J.relative_to(ROOT)} + {OUT_H.relative_to(ROOT)} ({len(doc) // 1024} KB)"
          + (f" · artifact {data['artifact']}" if data.get("artifact") else " · chưa publish"))


if __name__ == "__main__":
    main()
