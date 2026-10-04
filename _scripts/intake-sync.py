#!/usr/bin/env python3
"""Đồng bộ sổ nguồn docs-input/README.md + backlog docs/_shared/backlog.md.

Chạy tự động qua hook (SessionStart, UserPromptSubmit, PostToolUse Write|Edit). Việc làm:
  1. Quét docs-input/ → nguồn mới tự vào sổ (⬜ chưa feed) + tự sinh task "feed".
     Nguồn bị đổi tên/chuyển chỗ (cùng nội dung) → tự cập nhật đường dẫn trong sổ.
  2. Quét docs/**/*.md → cột "Dùng ở" của sổ; doc feature (docs/{feature}/...) trỏ tới nguồn
     → tự nâng ⬜ thành ✅ (không bao giờ tự hạ ✅ do người ghi tay).
  3. Chấm điều kiện "Xong khi" của từng task → tự đóng task, ghi ngày + bằng chứng.

Cú pháp "Xong khi" (nhiều điều kiện nối bằng `&&`, thêm `!` phía trước để phủ định):
  exists:<glob>                 có ít nhất 1 file khớp glob (tính từ gốc repo)
  grep:<glob>:<regex>           có file khớp glob chứa regex
  fed:<đường dẫn trong docs-input>   nguồn đó đang ✅ trong sổ
  manual                        chỉ đóng bằng tay (đổi Trạng thái thành ✅)

Tuỳ chọn: --quiet (chỉ in khi có thay đổi) · --summary (in task đang mở) · --dry-run.
"""
import glob, hashlib, json, os, re, sys, unicodedata
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT = "docs-input"
REG = f"{INPUT}/README.md"
STATE = f"{INPUT}/.intake-state.json"
BACKLOG = "docs/_shared/backlog.md"
TODAY = date.today().isoformat()
SKIP_REF = re.compile(r"^docs/_shared/(changelog|staleness|backlog)\.md$|^docs/_shared/kg/")
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
    for md in sorted(glob.glob(os.path.join(ROOT, "docs/**/*.md"), recursive=True)):
        rel = nfc(os.path.relpath(md, ROOT))
        if SKIP_REF.search(rel):
            continue
        txt = rd(rel)
        for p in paths:
            if f"{INPUT}/{p}" in txt:
                refs[p].append(rel)
    return refs


def is_feature_doc(rel):
    parts = rel.split("/")
    return len(parts) >= 3 and not parts[1].startswith("_")


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
            m = sorted(glob.glob(os.path.join(ROOT, arg), recursive=True))
            ok, hit = bool(m), (nfc(os.path.relpath(m[0], ROOT)) if m else "")
        elif kind == "grep":
            g, _, rx = arg.partition(":")
            for f in sorted(glob.glob(os.path.join(ROOT, g), recursive=True)):
                try:
                    if re.search(rx, rd(os.path.relpath(f, ROOT))):
                        ok, hit = True, nfc(os.path.relpath(f, ROOT))
                        break
                except (UnicodeDecodeError, IsADirectoryError):
                    pass
        elif kind == "fed":
            ok = fed.get(arg, False)
            hit = f"sổ nguồn: {arg} ✅"
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

    # tham chiếu + nâng feed
    refs = scan_refs([unq(r["File"]) for r in rows])
    for r in rows:
        p = unq(r["File"])
        used = refs.get(p, [])
        r["Dùng ở (tự động)"] = "<br>".join(f"`{u}`" for u in used) or "—"
        if r["Feed brainstorm"].startswith("⬜") and any(is_feature_doc(u) for u in used):
            r["Feed brainstorm"] = "✅ đã feed"
            log.append(f"✅ {r['Mã']} đã feed ({p})")
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
    have_feed_task = {unq(i["Xong khi"])[4:] for i in items if unq(i["Xong khi"]).startswith("fed:")}
    bn = max([int(i["ID"][3:]) for i in items] + [0]) + 1
    for r in rows:
        p = unq(r["File"])
        if r["Feed brainstorm"].startswith("⬜") and p not in have_feed_task and p in hashes:
            verb = "Xếp nhóm + đặt tên, rồi đọc và feed" if r["Nhóm"] == "Chưa phân loại" else "Đọc và feed"
            items.append(dict(zip(BL_HEAD, [f"BL-{bn:03d}", f"{verb} {r['Mã']} vào brainstorm/feature",
                                            f"`{p}`", f"`fed:{p}`", "⬜", TODAY, "", ""])))
            log.append(f"+ task BL-{bn:03d}: feed {p}")
            bn += 1
    for i in items:
        if i["Trạng thái"].startswith("✅"):
            continue
        ok, ev = check(i["Xong khi"], fed)
        if ok:
            i["Trạng thái"], i["Xong"], i["Bằng chứng"] = "✅", TODAY, ev
            log.append(f"✅ {i['ID']} xong — {i['Việc']}")

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
