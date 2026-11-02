#!/usr/bin/env python3
"""Quan hệ component DS v2 + đánh stale khi con lồng trong nó hoặc foundation nó dùng đổi (DEC-292, DEC-302).
Nguồn: design-system/components/_deps.json · rule .claude/rules/ds-stale.md

  python3 _scripts/ds-deps.py tree                 # cây: cha dùng con nào (role, tạm) + foundation mỗi component dùng
  python3 _scripts/ds-deps.py version <slug>       # phiên bản hiện tại của 1 component
  python3 _scripts/ds-deps.py fversion [<mã>]      # phiên bản hiện tại của 1 / các mục foundation
  python3 _scripts/ds-deps.py impact <slug|f:mã>   # đổi con/mục này thì component nào bị ảnh hưởng (qua KG, bắc cầu)
  python3 _scripts/ds-deps.py inherited <child>    # quyết định chốt sẵn từ cha (brainstorm con hiện làm mặc định)
  python3 _scripts/ds-deps.py scan [--write]       # dò mọi component (md + _work) + foundation nó dùng → _deps.json
  python3 _scripts/ds-deps.py baseline [<slug>…]   # lấy phiên bản hiện tại làm mốc "đã dựng theo" (mặc định: component chưa có mốc)
  python3 _scripts/ds-deps.py synced <slug>        # đã sync xong: ghi mốc mới, trả status cũ, gỡ cờ stale
  python3 _scripts/ds-deps.py check [--write] [--backlog]
      so mốc `built` với phiên bản hiện tại của con + foundation; seed lệch → `kg impact` lấy mọi cha bắc cầu.
      --write: md `status: stale` + `status_prev`, page.kit ⚠, log _workspace/staleness.md · --backlog: task "Sync …".

Phiên bản component = 10 ký tự sha1 phần quyết định hình dạng: _work/<slug> (answers brainstorm + css + values) nếu có,
không thì file md (bỏ dòng updated/status/status_prev). Chưa có gì → "chua-dung".
Phiên bản foundation = sha1 mục tương ứng trong foundations.md (cột "Ở đâu") + icons.md (mục icon) + các dòng tokens.css
có tiền tố của mục (FPREFIX). Có nhắc logo.md (hoặc màn mẫu trong page.json ghi "logo") thì tính là dùng mục logo (DEC-326).
"""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMP = ROOT / "design-system/components"
REG = COMP / "_deps.json"
FDIR = ROOT / "design-system/foundations"
FMD = FDIR / "README.md"  # bảng trạng thái; mục N nằm ở file riêng (DEC-317)
ICONS = ROOT / "design-system/foundations/icon.md"
TCSS = ROOT / "design-system/tokens.css"
KGQ = ROOT / ".claude/skills/kg/engine/kg-query.mjs"
TODAY = date.today().isoformat()
WORK_SKIP = {"_forms", "_lib"}

FFILE = {k: "design-system/foundations/" + f for k, f in {"color": "color.md", "type": "typography.md", "radius": "radius.md", "space": "spacing.md", "grid": "grids.md", "elevation": "effect-styles.md", "touch-focus": "touch-focus.md", "motion": "motion.md", "icon": "icon.md", "misc-icon": "icon-sets.md", "vehicle": "vehicle.md", "logo": "logo.md"}.items()}

# DEC-331, DEC-332: hai mục không có FPREFIX vì biến của chúng còn trỏ tiếp sang màu, cỡ (FPREFIX chặn dò ngược);
# tính phiên bản theo FTOKEN + file riêng, nhận component dùng theo biến hoặc tên trong spec
FTOKEN = {"misc-icon": ("featured-icon-", "color-file-type-", "file-type-"), "vehicle": ("vehicle-", "color-vehicle-")}
FDOC = {"misc-icon": "icon-sets.md", "vehicle": "vehicle.md"}
FTEXT = {"misc-icon": re.compile(r"Featured [Ii]con|featured-icon|File type icon|`Flag`|Bank logo|App logo|QR code|icon-sets\.md"),
         "vehicle": re.compile(r"vehicle\.md|vehicles\.json|Vehicle Image|Tyre Layout|Map Marker")}

# DEC-337: instance đo trên Figma (_scripts/figma-ds-uses.js), bắt component dùng mà spec không nhắc tên
FIGMA_USES = COMP / "_figma-uses.json"


def figma_uses(slug):
    if not FIGMA_USES.exists():
        return set()
    d = json.loads(FIGMA_USES.read_text(encoding="utf-8"))
    return {k for name, keys in d["uses"].items() if d["slugs"].get(name) == slug for k in keys}


# tiền tố biến CSS → mục foundation (biến component như --tooltip-bg được dò ngược qua var() trong tokens.css)
FPREFIX = {
    "color": ("color-", "neutral-", "blue-", "red-", "green-", "yellow-", "orange-", "purple-", "teal-", "charcoal-", "alpha-", "dark-", "file-type-"),
    "type": ("type-", "font-"),
    "radius": ("radius-",),
    "space": ("space-",),
    "grid": ("grid-", "container-", "width-", "bp-"),
    "elevation": ("shadow-", "backdrop-blur-"),
    "touch-focus": ("touch-", "focus-"),
    "motion": ("duration-", "ease-"),
    "icon": ("icon-",),
    "logo": ("invlogis-", "innvie-"),  # màu thương hiệu; logo không có biến cỡ (DEC-326), nên dò thêm theo chữ ở foundations_used
}


def reg():
    r = json.loads(REG.read_text()) if REG.exists() else {}
    r.setdefault("components", {})
    r.setdefault("inherited", {})
    return r


def save(r):
    txt = json.dumps(r, ensure_ascii=False, indent=1) + "\n"
    if not REG.exists() or REG.read_text() != txt:  # không đổi thì không chạm mtime → KG khỏi build lại
        REG.write_text(txt)


def md_of(slug):
    for p in sorted(COMP.glob(f"*/{slug}.md")):
        if not p.parent.name.startswith("_"):
            return p
    return None


def rel(p):
    return str(p.relative_to(ROOT))


# ── phiên bản ───────────────────────────────────────────────────────────────
def version(slug):
    w = COMP / "_work" / slug
    if (w / "page.json").exists():
        p = json.loads((w / "page.json").read_text())
        a = json.loads((w / "answers.json").read_text()) if (w / "answers.json").exists() else {}
        core = {"answers": {k: v.get("choice") for k, v in a.items() if k.startswith("brainstorm-")},
                "css": p.get("css"), "values": p.get("values")}
        return hashlib.sha1(json.dumps(core, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:10]
    m = md_of(slug)
    if m:
        s = re.sub(r"^(updated|status|status_prev):.*$", "", m.read_text(encoding="utf-8"), flags=re.M)
        return hashlib.sha1(s.encode()).hexdigest()[:10]
    return "chua-dung"


def _fstatus():
    spec = importlib.util.spec_from_file_location("dfs", ROOT / "_scripts/ds-foundation-status.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.read()[3]


def _sections():
    """Mục `## N.` gộp từ mọi file foundations/*.md (DEC-317); mỗi file bắt đầu lại, phần đầu file không thuộc mục nào."""
    out = {}
    for f in sorted(FDIR.glob("*.md")):
        if f.name in ("icon.md", "vehicle.md", "icon-sets.md"):
            continue
        cur = None
        for line in f.read_text(encoding="utf-8").splitlines():
            h = re.match(r"^## (\d+)\.", line)
            if h:
                cur = h.group(1)
            elif line.startswith("## "):
                cur = None
            if cur:
                out.setdefault(cur, []).append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def _css_lines():
    return TCSS.read_text(encoding="utf-8").splitlines() if TCSS.exists() else []


def fversions():
    secs, css, out = _sections(), _css_lines(), {}
    for row in _fstatus():
        k = row["key"]
        parts = [secs.get(n, "") for n in re.findall(r"mục (\d+)", row["where"])]
        if k == "icon" and ICONS.exists():
            parts.append(re.sub(r"^updated:.*$", "", ICONS.read_text(encoding="utf-8"), flags=re.M))
        if k in FDOC and (FDIR / FDOC[k]).exists():
            parts.append(re.sub(r"^updated:.*$", "", (FDIR / FDOC[k]).read_text(encoding="utf-8"), flags=re.M))
        pre = tuple("--" + x for x in FPREFIX.get(k, FTOKEN.get(k, ())))
        parts += [l.strip() for l in css if l.strip().startswith(pre)]
        out[k] = {"name": row["name"], "status": row["status"],
                  "version": hashlib.sha1("\n".join(parts).encode()).hexdigest()[:10]}
    return out


# ── dò foundation component dùng ────────────────────────────────────────────
def _token_graph():
    g = {}
    for m in re.finditer(r"--([\w-]+)\s*:\s*([^;]*);", TCSS.read_text(encoding="utf-8") if TCSS.exists() else ""):
        g.setdefault(m.group(1), set()).update(re.findall(r"var\(--([\w-]+)", m.group(2)))
    return g


def _resolver():
    g, memo = _token_graph(), {}

    def fnd(name, seen=()):
        if name in memo:
            return memo[name]
        for k, pre in FPREFIX.items():
            if name.startswith(pre):
                memo[name] = {k}
                return memo[name]
        out = set()
        for ref in g.get(name, ()):
            if ref not in seen:
                out |= fnd(ref, seen + (name,))
        memo[name] = out
        return out
    return g, fnd


def foundations_used(slug):
    g, fnd = _resolver()
    names, text, logo_note = set(), "", ""
    pj = COMP / "_work" / slug / "page.json"
    if pj.exists():
        p = json.loads(pj.read_text())
        blob = json.dumps([p.get(k) for k in ("css", "cssScreen", "values", "preview", "proto")], ensure_ascii=False)
        # bỏ khối token chép nguyên từ tokens.css (kit dump) — định nghĩa, không phải dùng
        blob = re.sub(r"--([\w-]+)\s*:\s*[^;{}\"]*;?", lambda m: "" if m.group(1) in g else m.group(0), blob)
        names |= set(re.findall(r"var\(--([\w-]+)", blob))
        text += blob
        # màn mẫu ghi logo trong note: error-page "chỉ logo và chân trang"; Payment/Bank/App logo là logo đối tác, không phải mục này
        logo_note = " ".join(str(x.get("note", "")) for x in p.get("screens") or [] if isinstance(x, dict))
    m = md_of(slug)
    if m:
        s = m.read_text(encoding="utf-8")
        names |= set(re.findall(r"var\(--([\w-]+)", s))
        names |= {t.replace("/", "-") for t in re.findall(r"`([a-z][a-z0-9-]*(?:/[a-z0-9.-]+)+)`", s)}
        text += s
    out = set()
    for n in names:
        out |= fnd(n)
    if re.search(r"icons\.md|lucide", text, re.I):
        out.add("icon")
    if "logo.md" in text or re.search(r"(?<!Payment )(?<!Bank )(?<!App )\blogo\b", logo_note, re.I):
        out.add("logo")
    for k, rx in FTEXT.items():
        if rx.search(text) or any(n.startswith(FTOKEN[k]) for n in names):
            out.add(k)
    out |= figma_uses(slug)
    return sorted(out)


def universe():
    out = {}
    for p in sorted(COMP.glob("*/*.md")):
        if p.parent.name.startswith("_") or p.stem in out:
            continue
        out[p.stem] = {"group": p.parent.name, "file": rel(p)}
    for d in sorted((COMP / "_work").glob("*/")):
        if d.name in WORK_SKIP or d.name in out or not (d / "page.json").exists():
            continue
        out[d.name] = {"group": "_work", "file": rel(d / "page.json")}
    return out


def scan(write=False):
    r = reg()
    for slug, meta in universe().items():
        c = r["components"].setdefault(slug, {})
        c["group"], c["file"] = meta["group"], meta["file"]
        c["foundations"] = foundations_used(slug)
    r["foundations"] = {k: {"name": v["name"], "file": FFILE.get(k, "design-system/foundations/README.md")}
                        for k, v in fversions().items()}
    # giữ thứ tự khoá ổn định: components theo slug, mỗi component uses/foundations/built
    r["components"] = dict(sorted(r["components"].items()))
    if write:
        save(r)
    return r


def snapshot(slug, r, fv):
    c = r["components"].get(slug, {})
    return {"children": {u["child"]: version(u["child"]) for u in c.get("uses", [])},
            "foundations": {k: fv[k]["version"] for k in c.get("foundations", []) if k in fv}, "at": TODAY}


def baseline(slugs=None):
    r, fv = scan(), fversions()
    done = []
    for slug, c in r["components"].items():
        if (slugs and slug not in slugs) or (not slugs and c.get("built")):
            continue
        c["built"] = snapshot(slug, r, fv)
        done.append(slug)
    save(r)
    return done


# ── kiểm stale ──────────────────────────────────────────────────────────────
def parents_of(child, r):
    return [(p, u) for p, d in r["components"].items() for u in d.get("uses", []) if u["child"] == child]


def direct_changes(r, fv):
    """{slug: [(loại, dep, mốc, hiện tại)]} — chỉ so phụ thuộc trực tiếp với mốc built."""
    out = {}
    for slug, c in r["components"].items():
        b = c.get("built")
        if not b:
            continue
        ch = []
        for u in c.get("uses", []):
            old, now = b.get("children", {}).get(u["child"]), version(u["child"])
            if old and old != now:
                ch.append(("con", u["child"], old, now))
        for k in c.get("foundations", []):
            old, now = b.get("foundations", {}).get(k), fv.get(k, {}).get("version")
            if old and now and old != now:
                ch.append(("foundation", k, old, now))
        if ch:
            out[slug] = ch
    return out


def kg_refresh():
    """graph.json cũ hơn _deps.json → build lại (hook kg-refresh chỉ canh docs/)."""
    g = ROOT / "_workspace/kg/graph.json"
    if g.exists() and g.stat().st_mtime >= REG.stat().st_mtime:
        return True
    p = subprocess.run(["node", str(ROOT / ".claude/skills/kg/engine/kg-build.mjs")], cwd=ROOT, capture_output=True, text=True)
    return p.returncode == 0


def kg_ancestors(seed):
    """`kg impact` → {slug: edge-path}. None nếu KG lỗi (gọi nơi khác fallback)."""
    try:
        p = subprocess.run(["node", str(KGQ), "impact", seed, "--depth", "8", "--all"], cwd=ROOT,
                           capture_output=True, text=True, timeout=60)
    except Exception:
        return None
    if p.returncode != 0 or "KG-ERROR" in p.stdout + p.stderr:
        return None
    out = {}
    for line in p.stdout.splitlines():
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 4 and c[2] == "ds_component" and c[1].startswith("ds:"):
            out[c[1][3:]] = c[3].replace("\\|", "|")
    return out


def py_ancestors(seed, r):
    kind, name = seed.split(":", 1)
    if kind == "ds-f":
        first = [s for s, c in r["components"].items() if name in c.get("foundations", [])]
    else:
        first = [p for p, _ in parents_of(name, r)]
    out, queue = {}, [(s, f"ds:{s} → {seed}") for s in first]
    while queue:
        s, path = queue.pop(0)
        if s in out:
            continue
        out[s] = path
        queue += [(p, f"ds:{p} → {path}") for p, _ in parents_of(s, r)]
    return out


def check(write=False, backlog=False):
    r, fv = scan(write=True), fversions()  # _deps.json là sổ máy dò — luôn ghi để KG thấy cạnh mới
    kg_ok = kg_refresh()
    direct = direct_changes(r, fv)
    seeds = sorted({(f"ds-f:{d}" if t == "foundation" else f"ds:{d}") for ch in direct.values() for t, d, _, _ in ch})
    # stale = có phụ thuộc trực tiếp lệch, hoặc có con (bắc cầu) đang stale
    stale = {s: [f"{'foundation ' if t == 'foundation' else ''}{d} ({o} → {n})" for t, d, o, n in ch] for s, ch in direct.items()}
    changed = True
    while changed:
        changed = False
        for slug, c in r["components"].items():
            via = [u["child"] for u in c.get("uses", []) if u["child"] in stale]
            if via and slug not in stale:
                stale[slug] = [f"qua {v}" for v in via]
                changed = True
            elif via:
                add = [f"qua {v}" for v in via if f"qua {v}" not in stale[slug]]
                if add:
                    stale[slug] += add
    paths, notes = {}, [] if kg_ok else ["kg-build lỗi — dùng thẳng _deps.json"]
    unbound = [s for s, c in r["components"].items() if not c.get("foundations")]
    if unbound:
        notes.append(f"không gắn token foundation (CSS mã cứng) — foundation đổi không lan tới: {', '.join(unbound)}")
    nobase = [s for s, c in r["components"].items() if not c.get("built")]
    if nobase:
        notes.append(f"chưa có mốc built (chạy `baseline`): {', '.join(nobase)}")
    for seed in seeds:
        anc = kg_ancestors(seed) if kg_ok else None
        if anc is None:
            notes.append(f"KG lỗi khi impact {seed} — dùng thẳng _deps.json")
            anc = py_ancestors(seed, r)
        else:
            miss = set(py_ancestors(seed, r)) - set(anc)
            if miss:
                notes.append(f"KG thiếu {', '.join(sorted(miss))} cho {seed} — chạy `node .claude/skills/kg/engine/kg-build.mjs`")
                anc.update({s: p for s, p in py_ancestors(seed, r).items() if s in miss})
        for s, p in anc.items():
            if s in stale:
                paths.setdefault(s, []).append(p)
    out = [{"slug": s, "reasons": rs, "paths": paths.get(s, []), "file": r["components"][s].get("file")} for s, rs in sorted(stale.items())]
    if write:
        for o in out:
            mark_stale(o)
        sync_kit_flags(r, stale)
    if backlog and out:
        add_tasks(out)
    return out, notes


# ── ghi ─────────────────────────────────────────────────────────────────────
def logbook(kind, row):
    subprocess.run([sys.executable, str(ROOT / "_scripts/logbook.py"), "add", kind, row], cwd=ROOT, capture_output=True)


def mark_stale(o):
    slug, why = o["slug"], "; ".join(o["reasons"])
    m = md_of(slug)
    if m:
        s = m.read_text(encoding="utf-8")
        st = re.search(r"^status:\s*(\S+)", s, re.M)
        if st and st.group(1) != "stale":
            s = s.replace(st.group(0), f"status: stale\nstatus_prev: {st.group(1)}", 1)
            m.write_text(s, encoding="utf-8")
            author = os.environ.get("CLAUDE_CHANGELOG_AUTHOR") or "manual"
            logbook("changelog", f"| {TODAY} | ds-deps | {author} | `{rel(m)}` | stale theo {why.replace('|', '/')} |")
            log_staleness(rel(m), why)
    pj = COMP / "_work" / slug / "page.json"
    if pj.exists():
        p = json.loads(pj.read_text())
        if p.get("dsStale") != o["reasons"]:
            p["dsStale"] = o["reasons"]
            pj.write_text(json.dumps(p, ensure_ascii=False, indent=1))
            if not m:
                log_staleness(rel(pj), why)


def log_staleness(path, why):
    f = ROOT / "_workspace/staleness.md"
    if f.exists():
        with f.open("a", encoding="utf-8") as h:
            h.write(f"| {TODAY} | `design-system/components/_deps.json` | `{path}` | ds-deps: {why.replace('|', '/')} |\n")


def sync_kit_flags(r, stale):
    """page.kit của trang duyệt: con nào / mục nào làm cha stale → ⚠ trên trang."""
    fv = fversions()
    for slug in r["components"]:
        pj = COMP / "_work" / slug / "page.json"
        if not pj.exists():
            continue
        page = json.loads(pj.read_text())
        kit = page.get("kit") or {}
        b = r["components"][slug].get("built") or {}
        changed = False
        for c in kit.get("components") or []:
            now = version(c["slug"])
            old = b.get("children", {}).get(c["slug"])
            st = (bool(old) and old != now) or c["slug"] in stale
            if c.get("stale") != st or c.get("versionNow") != now:
                c["stale"], c["versionNow"] = st, now
                changed = True
        for f in kit.get("foundations") or []:
            old, now = b.get("foundations", {}).get(f["key"]), fv.get(f["key"], {}).get("version")
            st = bool(old) and old != now
            if f.get("stale") != st:
                f["stale"] = st
                changed = True
        if changed:
            pj.write_text(json.dumps(page, ensure_ascii=False, indent=1))


def done_cond(slug):
    m = md_of(slug)
    if m:
        return f"`!grep:{rel(m)}:^status: stale`"
    return f"`!grep:design-system/components/_work/{slug}/page.json:\"dsStale\": \\[`"


def add_tasks(out):
    bl = ROOT / "_workspace/backlog.md"
    s = bl.read_text(encoding="utf-8")
    n = max(int(x) for x in re.findall(r"^\| BL-(\d+)", s, re.M)) + 1
    lines = s.split("\n")
    last = max(i for i, l in enumerate(lines) if re.match(r"^\| BL-\d+ \|", l) and "| ✅ |" not in l)
    add = []
    for o in out:
        head = f"Sync {o['slug']} (DS stale)"
        if any(head in l and "| ✅ |" not in l for l in lines):
            continue
        why = "; ".join(o["reasons"]).replace("|", "/")
        add.append(f"| BL-{n:03d} | {head}: {why} — dựng lại preview/Figma, chạy lại bước 3, rồi `ds-deps.py synced {o['slug']}` "
                   f"| ds-deps (DEC-302) | {done_cond(o['slug'])} | ⬜ | {TODAY} |  |  |  |  |")
        n += 1
    if add:
        lines[last + 1:last + 1] = add
        bl.write_text("\n".join(lines), encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "_scripts/intake-sync.py")], cwd=ROOT, capture_output=True)
        print(f"Thêm {len(add)} task backlog")


def synced(slug):
    r, fv = scan(), fversions()
    if slug not in r["components"]:
        sys.exit(f"Không có component {slug}")
    r["components"][slug]["built"] = snapshot(slug, r, fv)
    save(r)
    m = md_of(slug)
    if m:
        s = m.read_text(encoding="utf-8")
        prev = re.search(r"^status_prev:\s*(\S+)\n?", s, re.M)
        if prev and re.search(r"^status: stale", s, re.M):
            s = re.sub(r"^status: stale$", f"status: {prev.group(1)}", s, count=1, flags=re.M).replace(prev.group(0), "", 1)
            m.write_text(s, encoding="utf-8")
            author = os.environ.get("CLAUDE_CHANGELOG_AUTHOR") or "manual"
            logbook("changelog", f"| {TODAY} | ds-deps | {author} | `{rel(m)}` | synced, status về {prev.group(1)} |")
    pj = COMP / "_work" / slug / "page.json"
    if pj.exists():
        p = json.loads(pj.read_text())
        if p.pop("dsStale", None) is not None:
            pj.write_text(json.dumps(p, ensure_ascii=False, indent=1))
    sync_kit_flags(r, {})
    print(f"Đã ghi mốc {slug}: {json.dumps(r['components'][slug]['built'], ensure_ascii=False)}")


def main():
    av = sys.argv[1:]
    r = reg()
    cmd = av[0] if av else "tree"
    if cmd == "tree":
        for p, d in r["components"].items():
            if not d.get("uses") and not d.get("foundations"):
                continue
            print(f"{p}  (bản {version(p)}) · foundation: {', '.join(d.get('foundations', [])) or '—'}"
                  + ("" if d.get("built") else " · chưa có mốc"))
            for u in d.get("uses", []):
                print(f"  └ {u['child']:<22} {u['role']:<7} {'tạm' if u.get('provisional') else '   '} bản {version(u['child'])}"
                      + (f" — {u['parts']}" if u.get("parts") else ""))
        for c, items in r.get("inherited", {}).items():
            print(f"chốt sẵn cho {c}: " + "; ".join(f"{i['id']} {i['title']} ({i['from']}, {i['dec']})" for i in items))
    elif cmd == "version":
        print(version(av[1]))
    elif cmd == "fversion":
        fv = fversions()
        for k, v in fv.items():
            if len(av) < 2 or av[1] == k:
                print(f"{k:<12} {v['version']}  {v['status']:<10} {v['name']}")
    elif cmd == "impact":
        kg_refresh()
        seed = f"ds-f:{av[1][2:]}" if av[1].startswith("f:") else f"ds:{av[1]}"
        anc = kg_ancestors(seed)
        if anc is None:
            print("KG lỗi — dùng thẳng _deps.json")
            anc = py_ancestors(seed, r)
        print("\n".join(f"{s}  ·  {p}" for s, p in sorted(anc.items())) or "không component nào dùng")
    elif cmd == "inherited":
        print(json.dumps(r.get("inherited", {}).get(av[1], []), ensure_ascii=False, indent=1))
    elif cmd == "scan":
        r = scan("--write" in av)
        for s, c in r["components"].items():
            print(f"{s:<26} {c.get('group', '?'):<12} {', '.join(c.get('foundations', [])) or '—'}")
    elif cmd == "baseline":
        done = baseline(av[1:] or None)
        print(f"Ghi mốc {len(done)} component: {', '.join(done) or '—'}")
    elif cmd == "synced":
        synced(av[1])
    elif cmd == "check":
        out, notes = check("--write" in av, "--backlog" in av)
        for n in notes:
            print(f"ℹ {n}")
        for o in out:
            print(f"⚠ {o['slug']} stale: {'; '.join(o['reasons'])}")
            for p in o["paths"]:
                print(f"    KG: {p}")
        if not out:
            print("Không component nào stale")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
