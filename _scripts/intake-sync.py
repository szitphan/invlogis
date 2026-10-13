#!/usr/bin/env python3
"""Đồng bộ sổ nguồn docs-input/README.md + backlog _workspace/backlog.md.

Chạy tự động qua hook (SessionStart, UserPromptSubmit, PostToolUse Write|Edit). Việc làm:
  1. Quét docs-input/ → nguồn mới tự vào sổ (⬜ chưa feed) + tự sinh task "feed".
     Nguồn bị đổi tên/chuyển chỗ (cùng nội dung) → tự cập nhật đường dẫn trong sổ.
  2. Quét docs/**/*.md → cột "Dùng ở" của sổ.
  3. Cột Feed theo sổ đối chiếu từng mục `docs-input/_coverage/{slug}.md` (source-coverage.py):
     ⬜ chưa feed · 🟡 đối chiếu n/m · ✅ đối chiếu m/m · ➖ (người ghi, không đụng). ✅ chỉ khi không còn
     mục ⬜/🔄 và mọi ➡ trỏ feature đã có thư mục. Nguồn ✅ cũ chưa có sổ → 🟡.
     Nguồn thay bản mới (dòng `> Phiên bản: … (nhận D)` mới hơn dòng `> Bản:` của sổ) → đọc bảng
     "Tổng quan thay đổi" của báo cáo _changes: Thêm mới/Sửa → mục 🔄, Bỏ → ➖ "bỏ ở bản mới"; tạo
     task rà lại. ➡ tới feature chưa có thư mục → task "Lập feature".
  4. Branch worktree đã báo sẵn sàng (`_scripts/wt.sh ready`) → task "🔍 chờ duyệt" land; có commit mới
     sau khi báo → "🔍 ⚠"; branch bị drop → task tự đóng (.claude/rules/worktree.md Mục 4).
  5. Chấm điều kiện "Xong khi" của từng task → tự đóng task, ghi ngày + bằng chứng.

Cú pháp "Xong khi" (nhiều điều kiện nối bằng `&&`, thêm `!` phía trước để phủ định):
  exists:<glob>                 có ít nhất 1 file khớp glob (tính từ gốc repo)
  grep:<glob>:<regex>           có file khớp glob chứa regex
  fed:<đường dẫn trong docs-input>   nguồn đó đang ✅ trong sổ
  branch:<tên branch>           branch local còn tồn tại (dùng `!branch:feat/x` → đóng khi đã drop)
  manual                        chỉ đóng bằng tay (đổi Trạng thái thành ✅)

Tuỳ chọn: --quiet (chỉ in khi có thay đổi) · --summary (in task đang mở) · --dry-run.
"""
import glob, hashlib, importlib.util, json, os, re, subprocess, sys, unicodedata
from datetime import date

ROOT = os.environ.get("INTAKE_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    "source_coverage", os.path.join(os.path.dirname(os.path.abspath(__file__)), "source-coverage.py"))
cov = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cov)
INPUT = "docs-input"
REG = f"{INPUT}/README.md"
STATE = f"{INPUT}/.intake-state.json"
BACKLOG = "_workspace/backlog.md"
TODAY = date.today().isoformat()
SKIP_REF = re.compile(r"^_workspace/")
# Feature nháp/test (folder bắt đầu "zz-") KHÔNG được làm bằng chứng đóng task hay feed nguồn.
SCRATCH = re.compile(r"(^|/)zz-")
GROUPS = {"sop": "SOP & giải pháp", "danh-muc": "Danh mục", "tich-hop": "Tích hợp ngoài",
          "chung-tu-mau": "Chứng từ mẫu", "du-lieu-mau": "Dữ liệu mẫu", "ui-common": "UI common",
          "srs-cu": "SRS cũ"}
IMG = re.compile(r"\.(png|jpe?g|gif|svg|webp)$", re.I)

nfc = lambda s: unicodedata.normalize("NFC", s)
args = set(sys.argv[1:])
QUIET, DRY = "--quiet" in args, "--dry-run" in args
log = []


def rd(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return nfc(f.read())


def wr(p, s):
    if DRY:
        return
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
        f.write(s)


def sha(p):
    with open(os.path.join(ROOT, p), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:12]


def cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def row(vals):
    return "| " + " | ".join(vals) + " |"


def unq(s):
    return s.strip().strip("`")


# ---------- 1. nguồn trong docs-input ----------
SKIP_DIRS = ("images", "source")  # ảnh đi kèm + bản gốc (docx/pdf/xlsx) của tài liệu đã chuyển sang .md


def list_sources():
    """Tài liệu = mọi file trừ README/state, trừ images/ + source/ (đi kèm tài liệu) và thư mục `_*`/`.*`
    (vd `_changes/` báo cáo thay đổi phiên bản, `.staging/` của /intake)."""
    out = []
    for dp, dns, fns in os.walk(os.path.join(ROOT, INPUT)):
        dns[:] = [d for d in dns if not d.startswith((".", "_")) and d not in SKIP_DIRS]
        for fn in fns:
            rel = nfc(os.path.relpath(os.path.join(dp, fn), os.path.join(ROOT, INPUT)))
            if fn.startswith(".") or rel in ("README.md",):
                continue
            out.append(rel)
    return sorted(out)


def list_originals():
    """{hash bản gốc trong <doc>/source/: đường dẫn .md của tài liệu đó} — để nhận ra file thô đã được
    /intake chuyển sang .md (file thô biến mất khỏi chỗ cũ, bản sao nằm trong source/)."""
    out = {}
    for src_dir in glob.glob(os.path.join(ROOT, INPUT, "**", "source"), recursive=True):
        doc_dir = os.path.dirname(src_dir)
        mds = sorted(glob.glob(os.path.join(doc_dir, "*.md")))
        own = os.path.join(doc_dir, os.path.basename(doc_dir) + ".md")
        md = own if os.path.exists(own) else (mds[0] if mds else None)
        if not md:
            continue
        for fn in os.listdir(src_dir):
            if not fn.startswith(".") and os.path.isfile(os.path.join(src_dir, fn)):
                rel = nfc(os.path.relpath(os.path.join(src_dir, fn), ROOT))
                out[sha(rel)] = nfc(os.path.relpath(md, os.path.join(ROOT, INPUT)))
    return out


REG_HEAD = ["Mã", "File", "Nhóm", "Feed brainstorm", "Dùng ở (tự động)", "Việc mở (tự động)", "Ngày nhận", "Ghi chú"]


def load_registry():
    rows, pre, post = [], [], []
    if not os.path.exists(os.path.join(ROOT, REG)):
        return rows, pre, post
    part = "pre"
    for ln in rd(REG).split("\n"):
        if part == "pre":
            if ln.startswith("| Mã |"):
                part = "tab"
                continue
            pre.append(ln)
        elif part == "tab":
            if ln.startswith("|---") or ln.startswith("| ---"):
                continue
            if ln.startswith("| SRC-"):
                c = cells(ln)
                rows.append(dict(zip(REG_HEAD, c + [""] * (len(REG_HEAD) - len(c)))))
                continue
            part = "post"
            post.append(ln)
        else:
            post.append(ln)
    return rows, pre, post


# ---------- 2. tham chiếu trong docs/ ----------
def scan_refs(paths):
    refs = {p: [] for p in paths}
    mds = glob.glob(os.path.join(ROOT, "docs/**/*.md"), recursive=True) + \
          glob.glob(os.path.join(ROOT, "design/**/*.md"), recursive=True)
    for md in sorted(mds):
        rel = nfc(os.path.relpath(md, ROOT))
        if SKIP_REF.search(rel) or SCRATCH.search(rel):
            continue
        txt = rd(rel)
        for p in paths:
            if f"{INPUT}/{p}" in txt:
                refs[p].append(rel)
    return refs


VERSION = re.compile(r"^> Phiên bản:.*?\(nhận (\d{4}-\d{2}-\d{2})\)", re.M)


def version_since(p):
    """Ngày nhận bản hiện hành (dòng `> Phiên bản:` đầu tiên do /intake ghi khi thay bản mới), hoặc None.
    Mới hơn dòng `> Bản:` của sổ đối chiếu → sổ còn theo bản cũ, phải mở lại mục (reopen)."""
    full = f"{INPUT}/{p}"
    if not p.endswith(".md") or not os.path.exists(os.path.join(ROOT, full)):
        return None
    m = VERSION.search(rd(full))
    return m.group(1) if m else None


CHANGES_LINK = re.compile(r"^> Phiên bản:.*?\(nhận (\d{4}-\d{2}-\d{2})\).*?\]\(([^)]*_changes/[^)]+\.md)\)", re.M)


def change_overview(p, since):
    """{'Thêm mới': [...], 'Sửa': [...], 'Bỏ': [...]} từ bảng "Tổng quan thay đổi" của báo cáo bản `since`,
    hoặc None khi không tìm được báo cáo/bảng."""
    m = next((m for m in CHANGES_LINK.finditer(rd(f"{INPUT}/{p}")) if m.group(1) == since), None)
    if not m:
        return None
    rep_path = os.path.normpath(os.path.join(os.path.dirname(f"{INPUT}/{p}"), m.group(2)))
    if not os.path.exists(os.path.join(ROOT, rep_path)):
        return None
    part = rd(rep_path).split("## Tổng quan thay đổi", 1)
    if len(part) < 2:
        return None
    out = {}
    for ln in part[1].split("\n## ")[0].split("\n"):
        c = cells(ln) if ln.startswith("|") else []
        if len(c) >= 3 and c[0] in ("Thêm mới", "Sửa", "Bỏ"):
            out[c[0]] = [x.strip() for x in c[2].split("; ") if x.strip()]
    return out or None


def reopen(led, p, since, code, new_tasks):
    """Nguồn có bản mới chưa đối chiếu: mở lại mục theo bảng Tổng quan thay đổi, ghi lại sổ, tạo task."""
    ov = change_overview(p, since)
    lines, rows = led["lines"], led["rows"]
    doc_title = cov.norm_title(re.sub(r"^#\s*", "", next((l for l in rd(f"{INPUT}/{p}").split("\n")
                                                           if l.startswith("# ")), "")))

    def find(item):
        num, title = cov.split_num(item.rstrip("."))
        t = cov.norm_title(title)
        return next((r for r in rows if cov.norm_title(cov.split_num(r["muc"])[1]) == t), None) or \
            (next((r for r in rows if num and r["num"] == num), None))

    def setrow(r, mark, note):
        c = cells(lines[r["i"]]) + ["", "", "", ""]
        was = f" (trước: {c[1]})" if c[1] and c[1] != mark else ""
        c[1], c[3] = mark, (note + was + (" · " + c[3] if c[3] else "")).strip()
        lines[r["i"]] = "| " + " | ".join(c[:4]) + " |"

    added, n = [], 0
    if ov is None:
        log.append(f"⚠ {code}: bản {since} không có bảng 'Tổng quan thay đổi' — mở lại mọi mục đã xử lý")
        for r in rows:
            if r["mark"] and r["mark"] not in ("⬜", "➖"):
                setrow(r, "🔄", f"bản {since}: rà lại")
                n += 1
    else:
        for kind, mark in (("Thêm mới", "🔄"), ("Sửa", "🔄"), ("Bỏ", "➖")):
            for item in ov.get(kind, []):
                t = cov.norm_title(cov.split_num(item.rstrip("."))[1])
                if t in ("mục lục", doc_title) or not t:
                    continue
                r = find(item)
                note = f"bỏ ở bản {since}" if kind == "Bỏ" else f"{kind.lower()} ở bản {since}"
                if r:
                    if kind == "Bỏ" and r["mark"] == "➖":
                        continue
                    setrow(r, mark, note)
                    n += 1
                elif kind != "Bỏ":
                    num, title = cov.split_num(item)
                    added.append(f"| {(num + ' ' + title) if num else title} | 🔄 | | {note} |")
                    n += 1
    last = max([r["i"] for r in rows], default=None)
    if added and last is not None:
        lines[last + 1:last + 1] = added
    txt = "\n".join(lines)
    lab = re.search(rf"^> Phiên bản:\s*(.*?)\s*\(nhận {since}\)", rd(f"{INPUT}/{p}"), re.M)
    txt = re.sub(r"^> Bản:.*$", f"> Bản: {lab.group(1) if lab else since} (nhận {since})", txt, count=1, flags=re.M)
    wr(led["path"], txt)
    log.append(f"🔄 {code}: bản {since} mở lại {n} mục trong `{led['path']}`")
    new_tasks.append((f"Rà lại {code} theo bản {since}", f"`{INPUT}/{p}`", f"`!grep:{led['path']}:🔄`"))
    return cov.load(led["path"], txt)  # dry-run không ghi file → tính trên nội dung trong bộ nhớ


# ---------- 3. backlog ----------
BL_HEAD = ["ID", "Việc", "Nguồn", "Xong khi", "Trạng thái", "Tạo", "Xong", "Bằng chứng"]


def load_backlog():
    if not os.path.exists(os.path.join(ROOT, BACKLOG)):
        return [], ""
    txt = rd(BACKLOG)
    items = []
    for ln in txt.split("\n"):
        if re.match(r"^\| BL-\d+", ln):
            c = cells(ln)
            items.append(dict(zip(BL_HEAD, c + [""] * (len(BL_HEAD) - len(c)))))
    head = txt.split("\n## ")[0]
    return items, head


def git(*a):
    try:
        r = subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def ready_branches():
    """Branch đã chạy `wt.sh ready`: [(branch, sha lúc báo, sha hiện tại, tóm tắt, ngày báo)]."""
    out = git("config", "--get-regexp", r"^branch\..*\.wtready$") or ""
    res = []
    for ln in out.splitlines():
        key, _, ready_sha = ln.partition(" ")
        br = key[len("branch."):-len(".wtready")]
        head = git("rev-parse", "--verify", "-q", f"refs/heads/{br}")
        if not head:
            continue
        summ = (git("config", "--get", f"branch.{br}.wtsummary") or "").replace("|", "/")
        at = git("config", "--get", f"branch.{br}.wtreadyat") or TODAY
        res.append((br, ready_sha.strip(), head, summ, at))
    return res


def check(cond, fed):
    """Trả (đúng/sai, bằng chứng)."""
    cond = unq(cond)
    if not cond or cond == "manual":
        return False, ""
    ev = []
    for part in [c.strip() for c in cond.split("&&")]:
        neg = part.startswith("!")
        part = part.lstrip("!").strip("` ")
        kind, _, arg = part.partition(":")
        ok, hit = False, ""
        if kind == "exists":
            m = [f for f in sorted(glob.glob(os.path.join(ROOT, arg), recursive=True))
                 if not SCRATCH.search(nfc(os.path.relpath(f, ROOT)))]
            ok, hit = bool(m), (nfc(os.path.relpath(m[0], ROOT)) if m else "")
        elif kind == "grep":
            g, _, rx = arg.partition(":")
            for f in sorted(glob.glob(os.path.join(ROOT, g), recursive=True)):
                if SCRATCH.search(nfc(os.path.relpath(f, ROOT))):
                    continue
                try:
                    if re.search(rx, rd(os.path.relpath(f, ROOT))):
                        ok, hit = True, nfc(os.path.relpath(f, ROOT))
                        break
                except (UnicodeDecodeError, IsADirectoryError):
                    pass
        elif kind == "fed":
            ok = fed.get(arg, False)
            hit = f"sổ nguồn: {arg} ✅"
        elif kind == "branch":
            ok = git("rev-parse", "--verify", "-q", f"refs/heads/{arg}") is not None
            hit = arg
        else:
            return False, ""
        if neg:
            ok, hit = not ok, f"không còn `{arg}`"
        if not ok:
            return False, ""
        ev.append(f"`{hit}`" if not hit.startswith(("sổ", "không")) else hit)
    return True, " · ".join(ev)


def main():
    os.chdir(ROOT)
    srcs = list_sources()
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    hashes = {p: sha(f"{INPUT}/{p}") for p in srcs}
    rows, pre, post = load_registry()

    # đổi tên / chuyển chỗ: dòng sổ mất file + file mới cùng hash
    renames, merged = {}, {}
    known = {unq(r["File"]) for r in rows}
    fresh = [p for p in srcs if p not in known]
    originals = list_originals()
    for r in list(rows):
        p = unq(r["File"])
        if p not in hashes:
            h = state.get(p)
            new = next((q for q in fresh if hashes[q] == h), None) if h else None
            conv = originals.get(h) if h and not new else None  # file thô đã được /intake chuyển sang .md
            owner = next((x for x in rows if x is not r and unq(x["File"]) == conv), None) if conv else None
            if owner:  # là bản cập nhật của tài liệu đã có → gộp vào mã cũ
                rows.remove(r)
                merged[p] = (conv, owner["Mã"])
                log.append(f"⤳ {r['Mã']} ({p}) là bản cập nhật của {owner['Mã']} — gộp vào `{conv}`")
            elif new or conv:
                new = new or conv
                r["File"] = f"`{new}`"
                renames[p] = new
                if r["Nhóm"] == "Chưa phân loại" and "/" in new:
                    r["Nhóm"] = GROUPS.get(new.split("/")[0], r["Nhóm"])
                if new in fresh:
                    fresh.remove(new)
                log.append(f"↪ đổi chỗ nguồn {r['Mã']}: {p} → {new}")
            elif not r["Ghi chú"].startswith("❌"):
                r["Ghi chú"] = "❌ không thấy file — " + r["Ghi chú"]
                log.append(f"❌ {r['Mã']} không thấy file {p}")
    nxt = max([int(r["Mã"][4:]) for r in rows] + [0]) + 1
    for p in fresh:
        top = p.split("/")[0] if "/" in p else ""
        rows.append(dict(zip(REG_HEAD, [f"SRC-{nxt:02d}", f"`{p}`", GROUPS.get(top, "Chưa phân loại"),
                                        "⬜ chưa feed", "", "", TODAY, ""])))
        log.append(f"+ nguồn mới SRC-{nxt:02d}: {p}")
        nxt += 1

    # tham chiếu
    refs = scan_refs([unq(r["File"]) for r in rows])
    for r in rows:
        r["Dùng ở (tự động)"] = "<br>".join(f"`{u}`" for u in refs.get(unq(r["File"]), [])) or "—"

    # feed theo sổ đối chiếu từng mục
    leds = cov.all_ledgers()
    new_tasks = []  # (việc, nguồn, xong khi)
    for r in rows:
        p = unq(r["File"])
        led = leds.get(p)
        if led:
            since = version_since(p)
            if since and led["version"] and since > led["version"]:
                led = reopen(led, p, since, r["Mã"], new_tasks)
            done, total, opened, pend = cov.summary(led)
            for f in pend:
                new_tasks.append((f"Lập feature {f} (nhận mục từ {r['Mã']})", f"`{p}`",
                                  f"`exists:docs/{f}/brainstorms/*.md`"))
            bad = len(cov.problems(led))
            new = f"✅ đối chiếu {done}/{total}" if not opened and not bad else \
                f"🟡 đối chiếu {done}/{total}" + (f", {bad} dòng ghi sai" if bad else "")
        elif r["Feed brainstorm"].startswith("➖"):
            continue
        elif r["Feed brainstorm"].startswith(("✅", "🟡")):
            new = "🟡 chưa có sổ đối chiếu"
        else:
            new = "⬜ chưa feed"
        if r["Feed brainstorm"] != new:
            log.append(f"{new[0]} {r['Mã']} {new[2:]} ({p})")
            r["Feed brainstorm"] = new
    fed = {unq(r["File"]): r["Feed brainstorm"].startswith("✅") for r in rows}

    # backlog
    items, head = load_backlog()
    for i in items:  # nguồn đổi chỗ → đổi đường dẫn trong task theo
        for old, new in renames.items():
            for k in ("Nguồn", "Xong khi"):
                i[k] = i[k].replace(old, new)
            if f"`{new}`" in i["Nguồn"] and "/" in new:  # đã xếp chỗ → bỏ vế "xếp nhóm" khỏi tên task
                i["Việc"] = i["Việc"].replace("Xếp nhóm + đặt tên, rồi đọc và feed", "Đọc và feed")
        for old, (new, code) in merged.items():  # bản cập nhật đã gộp → task feed của nó thừa
            if unq(i["Xong khi"]) == f"fed:{old}" and not i["Trạng thái"].startswith("✅"):
                i["Trạng thái"], i["Xong"] = "✅", TODAY
                i["Bằng chứng"] = f"bản cập nhật, đã gộp vào {code} (`{new}`)"
                log.append(f"✅ {i['ID']} đóng — gộp vào {code}")
            for k in ("Nguồn", "Xong khi"):
                i[k] = i[k].replace(old, new)
    is_open = lambda i: not i["Trạng thái"].startswith("✅")
    have_feed_task = {unq(i["Xong khi"])[4:] for i in items if unq(i["Xong khi"]).startswith("fed:") and is_open(i)}
    bn = max([int(i["ID"][3:]) for i in items] + [0]) + 1
    for r in rows:
        p = unq(r["File"])
        st = r["Feed brainstorm"]
        if st.startswith(("⬜", "🟡")) and p not in have_feed_task and p in hashes:
            if st.startswith("⬜"):
                verb = "Xếp nhóm + đặt tên, rồi đọc và feed" if r["Nhóm"] == "Chưa phân loại" else "Đọc và feed"
                what = f"{verb} {r['Mã']} vào brainstorm/feature (lập sổ đối chiếu)"
            elif p in leds:
                what = f"Hoàn tất sổ đối chiếu {r['Mã']} (còn mục chưa xử lý)"
            else:
                what = f"Lập sổ đối chiếu {r['Mã']} (bản cũ tính feed theo cả file)"
            new_tasks.append((what, f"`{p}`", f"`fed:{p}`"))
    have = {(i["Việc"], unq(i["Xong khi"])) for i in items if is_open(i)}
    have_cond = {unq(i["Xong khi"]) for i in items if is_open(i)}
    for what, src, cond in new_tasks:
        if (what, unq(cond)) in have or unq(cond) in have_cond:
            continue
        items.append(dict(zip(BL_HEAD, [f"BL-{bn:03d}", what, src, cond, "⬜", TODAY, "", ""])))
        have_cond.add(unq(cond))
        log.append(f"+ task BL-{bn:03d}: {what}")
        bn += 1
    # task duyệt land: 1 task / branch đã báo ready, đóng khi branch bị drop
    by_cond = {unq(i["Xong khi"]): i for i in items if is_open(i)}
    ready = ready_branches()
    ready_conds = {f"!branch:{r[0]}" for r in ready}
    for cond, i in by_cond.items():  # đã rút ready (wt.sh unready) → không còn chờ duyệt
        if (cond.startswith("!branch:") and cond not in ready_conds and i["Trạng thái"].startswith("🔍")
                and git("rev-parse", "--verify", "-q", f"refs/heads/{cond[8:]}")):  # branch đã drop → để check() đóng
            i["Trạng thái"] = "⬜ đang sửa lại"
            log.append(f"~ {i['ID']}: ⬜ đang sửa lại")
    for br, ready_sha, head, summ, at in ready:
        cond = f"!branch:{br}"
        st = "🔍 chờ duyệt" if head == ready_sha else "🔍 ⚠ có commit mới sau khi báo ready"
        what = f"Duyệt + land `{br}`" + (f" — {summ}" if summ else "")
        i = by_cond.get(cond)
        if i is None:
            items.append(dict(zip(BL_HEAD, [f"BL-{bn:03d}", what, f"`{br}`", f"`{cond}`", st, at, "", ""])))
            log.append(f"+ task BL-{bn:03d}: {what} ({st})")
            bn += 1
        elif (i["Trạng thái"], i["Việc"]) != (st, what):
            i["Trạng thái"], i["Việc"] = st, what
            log.append(f"~ {i['ID']}: {st}")

    for i in items:
        if i["Trạng thái"].startswith("✅"):
            continue
        ok, ev = check(i["Xong khi"], fed)
        if ok:
            i["Trạng thái"], i["Xong"], i["Bằng chứng"] = "✅", TODAY, ev
            log.append(f"✅ {i['ID']} xong — {i['Việc']}")

    # task "Chốt giao diện Figma {feature} · {flow}" user đóng tay mà flow chưa approved → nhắc chạy --done
    # (rule .claude/rules/screen-source.md Mục 6). In mỗi lượt tới khi điều kiện thoả.
    remind = []
    for i in items:
        m = re.match(r"Chốt giao diện Figma\s+(\S+)\s+·\s+(\S+)", i["Việc"])
        if m and i["Trạng thái"].startswith("✅") and not check(i["Xong khi"], fed)[0]:
            remind.append(f"{i['ID']} chốt tay — chạy /figma-sync {m.group(1)} --done --flow {m.group(2)}")

    # cột "Việc mở" của sổ
    open_items = [i for i in items if not i["Trạng thái"].startswith("✅")]
    for r in rows:
        p = unq(r["File"])
        ids = [i["ID"] for i in open_items
               if any(p.startswith(unq(s)) for s in re.findall(r"`([^`]+)`", i["Nguồn"]))]
        r["Việc mở (tự động)"] = ", ".join(ids) or "—"

    # ghi sổ
    if not pre:
        pre = ["# Sổ đăng ký nguồn — docs-input", "",
               "> Cột *tự động* do `_scripts/intake-sync.py` ghi lại mỗi lần chạy; các cột khác sửa tay được.", ""]
    reg = "\n".join(pre) + "\n" + row(REG_HEAD) + "\n|" + "---|" * len(REG_HEAD) + "\n" + \
          "\n".join(row([r[h] for h in REG_HEAD]) for r in rows) + "\n" + "\n".join(post).rstrip() + "\n"
    if not os.path.exists(REG) or rd(REG) != reg:
        wr(REG, reg)

    # ghi backlog
    if not head:
        head = "---\ntype: backlog\nstatus: draft\nupdated: " + TODAY + "\nlinks:\n  - docs-input/README.md\n---\n\n# Backlog\n"
    head = re.sub(r"^updated: .*$", f"updated: {TODAY}", head, count=1, flags=re.M) if log else head
    tab = lambda xs: row(BL_HEAD) + "\n|" + "---|" * len(BL_HEAD) + "\n" + "\n".join(row([x[h] for h in BL_HEAD]) for x in xs)
    done = [i for i in items if i["Trạng thái"].startswith("✅")]
    bl = head.rstrip() + "\n\n## Đang mở\n\n" + (tab(open_items) if open_items else "_Không còn task mở._") + \
         "\n\n## Đã xong\n\n" + (tab(done) if done else "_Chưa có._") + "\n"
    if not os.path.exists(BACKLOG) or rd(BACKLOG) != bl:
        wr(BACKLOG, bl)

    if not DRY:
        json.dump({unq(r["File"]): hashes.get(unq(r["File"])) for r in rows if unq(r["File"]) in hashes},
                  open(STATE, "w"), ensure_ascii=False, indent=0)

    if log:
        print("[intake-sync] " + "\n[intake-sync] ".join(log))
    elif not QUIET:
        print("[intake-sync] không có thay đổi")
    for r in remind:
        print(f"[figma-sync] {r}")
    if "--summary" in args:
        print(f"  Backlog: {len(open_items)} task mở · {len(done)} đã xong ({BACKLOG})")
        for i in open_items[:5]:
            print(f"   {i['Trạng thái']} {i['ID']} {i['Việc']}")
        if len(open_items) > 5:
            print(f"   … còn {len(open_items) - 5} task")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # hook không được làm hỏng phiên làm việc
        print(f"[intake-sync] lỗi: {e}", file=sys.stderr)
        sys.exit(0)
