#!/usr/bin/env python3
"""Status engine cho /status — đọc lifecycle + phụ thuộc `links:`, kiểm và ghi chuyển trạng thái.

Lệnh:
  report [<path-prefix>]                 bảng status + upstream + cờ cảnh báo
  impact <path>                          cây downstream (mọi tầng) kèm status
  apply <new> <path|prefix>... [--reason "..."] [--confirm-upstream] [--dry-run]
  restore <path|prefix>... [--dry-run]   stale → status_prev

Exit code: 0 OK · 1 chuyển không hợp lệ / lỗi · 3 cần user xác nhận (upstream chưa ổn định).
Luật nguồn: .claude/rules/status-lifecycle.md (bảng TRANSITIONS dưới phải khớp rule).
"""
import argparse
import difflib
import hashlib
import os
import re
import subprocess
import sys
from datetime import date

ROOT = os.environ.get("PROJECT_PATH") or os.getcwd()
SCAN_DIRS = ["docs", "design"]
EXCLUDE = ("docs/exports/", "docs/inbox/", "docs/_reverse/")
# Loại doc có lifecycle riêng — hiện trong report nhưng không kiểm theo bảng dưới.
OWN_LIFECYCLE = {"change-request", "meeting"}

LIFECYCLE = ["draft", "in-review", "revisions", "approved", "shipped"]
STABLE = {"approved", "shipped"}
# Chuyển hợp lệ (đồng bộ với status-lifecycle.md Mục "Transitions").
# `stale` KHÔNG đặt tay — chỉ hook post-edit-stale.sh đặt; thoát bằng `restore` hoặc sang `revisions`.
TRANSITIONS = {
    "draft": {"in-review"},
    "in-review": {"revisions", "approved", "draft"},
    "revisions": {"in-review", "approved", "draft"},
    "approved": {"shipped", "revisions"},
    "shipped": {"revisions"},
    "stale": {"revisions"},
}
SUGGEST = {
    "in-review": "chờ reviewer (người/stakeholder) duyệt",
    "approved": "/gap {feature}",
    "shipped": "/gap --product (re-verify cross-feature)",
    "revisions": "xử lý review findings rồi chạy lại skill sinh doc hoặc /cr",
}


# ---------- đọc vault ----------

def rel(p):
    return os.path.relpath(os.path.abspath(p), ROOT)


def split_frontmatter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], i
    return None, None


def parse_doc(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        text = f.read()
    fm, _ = split_frontmatter(text)
    if fm is None:
        return None
    d = {"path": path, "links": []}
    in_links = False
    for line in fm:
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            in_links = key == "links" and val == ""
            if key == "links" and val.startswith("["):
                d["links"] = [x.strip().strip("'\"") for x in val.strip("[]").split(",") if x.strip()]
            elif key != "links":
                d[key] = val.strip("'\"")
            continue
        if in_links:
            m = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if m:
                d["links"].append(m.group(1).strip("'\""))
    return d if "status" in d else None


def load_docs():
    docs = {}
    for base in SCAN_DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, base)):
            for fn in files:
                if not fn.endswith(".md"):
                    continue
                p = rel(os.path.join(dirpath, fn))
                if p.startswith(EXCLUDE):
                    continue
                d = parse_doc(p)
                if d:
                    docs[p] = d
    return docs


def downstream_map(docs):
    down = {p: [] for p in docs}
    for p, d in docs.items():
        for u in d["links"]:
            if u in down:
                down[u].append(p)
    return down


def stale_causes():
    """downstream path → (ngày, upstream) lần đánh stale gần nhất, từ _workspace/staleness.md."""
    causes = {}
    log = os.path.join(ROOT, "_workspace/staleness.md")
    if not os.path.exists(log):
        return causes
    for line in open(log, encoding="utf-8"):
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and re.match(r"\d{4}-\d{2}-\d{2}", cells[0]):
            causes[cells[2]] = (cells[0], cells[1])
    return causes


def find_cycles(docs):
    cycles, seen = [], set()
    for a, d in docs.items():
        for b in d["links"]:
            if b in docs and a in docs[b]["links"]:
                key = tuple(sorted((a, b)))
                if key not in seen:
                    seen.add(key)
                    cycles.append(key)
    return cycles


def transitive_down(start, down):
    out, stack = {}, [(start, 0)]
    while stack:
        node, depth = stack.pop()
        for c in down.get(node, []):
            if c not in out and c != start:
                out[c] = depth + 1
                stack.append((c, depth + 1))
    return out


def resolve_targets(args, docs):
    res = []
    for a in args:
        a = rel(a) if os.path.exists(os.path.join(ROOT, a)) else a.rstrip("/")
        hits = [p for p in docs if p == a or p.startswith(a + "/")]
        if not hits:
            hits = [p for p in docs if f"/{a}/" in f"/{p}"]  # tên feature trần, vd `payment`
        if not hits:
            print(f"KHÔNG TÌM THẤY doc có status khớp `{a}`", file=sys.stderr)
            sys.exit(1)
        res += [h for h in sorted(hits) if h not in res]
    return res


# ---------- report ----------

def short(p):
    return p.replace("docs/", "").replace(".md", "")


def cmd_report(prefix):
    docs = load_docs()
    down = downstream_map(docs)
    causes = stale_causes()
    sel = sorted(p for p in docs if not prefix or p.startswith(prefix.rstrip("/")))
    print("## Status & phụ thuộc\n")
    print("| Doc | Status | Upstream (status) | Downstream | Cờ |")
    print("|---|---|---|---|---|")
    flags_all = []
    for p in sel:
        d = docs[p]
        st = d["status"]
        ups, flags = [], []
        for u in d["links"]:
            if u in docs:
                ups.append(f"{short(u)} ({docs[u]['status']})")
                if st in STABLE and docs[u]["status"] not in STABLE:
                    flags.append(f"⚠ {st} nhưng upstream `{short(u)}` còn {docs[u]['status']}")
            elif not os.path.exists(os.path.join(ROOT, u)):
                ups.append(f"{u} (❌ không tồn tại)")
                flags.append(f"❌ link hỏng `{u}`")
        n_ext = sum(1 for u in d["links"] if u not in docs and os.path.exists(os.path.join(ROOT, u)))
        if n_ext:
            ups.append(f"+{n_ext} nguồn ngoài lifecycle")
        if st == "stale":
            c = causes.get(p)
            prev = d.get("status_prev", "?")
            flags.append(f"🟠 stale (trước đó: {prev})" + (f" — do `{short(c[1])}` đổi {c[0]}" if c else ""))
            indirect = [x for x, dep in transitive_down(p, down).items() if dep >= 1 and docs[x]["status"] != "stale"]
            if indirect:
                flags.append("↳ ảnh hưởng gián tiếp: " + ", ".join(f"`{short(x)}`" for x in sorted(indirect)))
        if d.get("type") in OWN_LIFECYCLE:
            flags.append("lifecycle riêng")
        n_down = len(down.get(p, []))
        print(f"| `{short(p)}` | {st} | {'<br>'.join(ups) or '—'} | {n_down or '—'} | {'<br>'.join(flags) or '✓'} |")
        flags_all += flags
    cyc = [c for c in find_cycles(docs) if not prefix or any(x.startswith(prefix) for x in c)]
    if cyc:
        print("\n### Vòng phụ thuộc (2 doc trỏ nhau — không rõ bên nào là nguồn, nên bỏ 1 chiều link)\n")
        for a, b in cyc:
            print(f"- `{short(a)}` ⇄ `{short(b)}`")
    counts = {}
    for p in sel:
        counts[docs[p]["status"]] = counts.get(docs[p]["status"], 0) + 1
    print("\n**Tổng:** " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print("\n_Ghi chú: `docs-input/`, `design/design.md`… không có status → tính là “nguồn ngoài lifecycle”; "
          "`_workspace/` (backlog/changelog/log máy) không thuộc lifecycle._")


def cmd_impact(target):
    docs = load_docs()
    down = downstream_map(docs)
    t = resolve_targets([target], docs)[0]
    tree = transitive_down(t, down)
    print(f"## Ảnh hưởng nếu `{short(t)}` ({docs[t]['status']}) thay đổi\n")
    if not tree:
        print("Không có doc nào phụ thuộc (không ai khai file này trong `links:`).")
        return
    print("| Tầng | Doc | Status | Hook tự đánh stale? |")
    print("|---|---|---|---|")
    hook_skips = "/_shared/" in f"/{t}" or not t.startswith("docs/")
    for p, dep in sorted(tree.items(), key=lambda x: (x[1], x[0])):
        auto = "có" if dep == 1 and not hook_skips else ("KHÔNG — tầng 2+ hook không lan" if dep > 1 else "KHÔNG — hook bỏ qua upstream ở `_shared/`/ngoài `docs/`")
        print(f"| {dep} | `{short(p)}` | {docs[p]['status']} | {auto} |")


# ---------- ghi ----------

def set_fm(text, updates, removes=()):
    fm, end = split_frontmatter(text)
    lines = text.split("\n")
    body_fm = list(fm)
    for k in removes:
        body_fm = [l for l in body_fm if not re.match(rf"^{k}:", l)]
    for k, v in updates.items():
        idx = next((i for i, l in enumerate(body_fm) if re.match(rf"^{k}:", l)), None)
        new = f"{k}: {v}"
        if idx is not None:
            body_fm[idx] = new
        else:
            st = next(i for i, l in enumerate(body_fm) if l.startswith("status:"))
            # chèn ngay sau status/status_* để nhóm lại
            pos = st + 1
            while pos < len(body_fm) and body_fm[pos].startswith("status_"):
                pos += 1
            body_fm.insert(pos, new)
    return "\n".join([lines[0]] + body_fm + lines[end:])


def quote(s):
    return '"' + s.replace('"', "'") + '"'


def write_doc(path, old, new, note, dry):
    diff = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), f"a/{path}", f"b/{path}", n=3))
    print(diff)
    if dry:
        return
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(new)
    # status-transition.sh state: giữ đồng bộ để hook không báo chuyển trễ ở lần Edit sau
    h = hashlib.sha1((path + "\n").encode()).hexdigest()[:16]
    sd = os.path.join(ROOT, "_workspace/.status-state")
    os.makedirs(sd, exist_ok=True)
    m = re.search(r"^status:\s*(\S+)", new, re.M)
    with open(os.path.join(sd, h), "w") as f:
        f.write(m.group(1) + "\n")
    # changelog: tái dùng hook writer duy nhất (nó tự bỏ qua _shared/ theo contract của nó)
    env = dict(os.environ, CLAUDE_SKILL_NAME="/status", CLAUDE_CHANGELOG_NOTE=note, PROJECT_PATH=ROOT)
    subprocess.run([os.path.join(ROOT, ".claude/hooks/auto-changelog.sh"), path], env=env, cwd=ROOT)


def cmd_apply(new, targets, reason, confirm_up, dry):
    docs = load_docs()
    paths = resolve_targets(targets, docs)
    if new == "stale":
        print("❌ `stale` không đặt tay — hook post-edit-stale.sh tự đặt khi upstream đổi.")
        sys.exit(1)
    if new not in LIFECYCLE:
        print(f"❌ status `{new}` không có trong lifecycle {LIFECYCLE}")
        sys.exit(1)
    bad, warn, ok = [], [], []
    for p in paths:
        d = docs[p]
        cur = d["status"]
        if d.get("type") in OWN_LIFECYCLE:
            bad.append(f"`{p}` — type `{d['type']}` có lifecycle riêng, dùng skill của nó (/cr, /meet)")
        elif cur == new:
            bad.append(f"`{p}` — đã ở `{cur}`")
        elif new not in TRANSITIONS.get(cur, set()):
            hint = " (thoát stale: `restore` hoặc sang `revisions`)" if cur == "stale" else ""
            bad.append(f"`{p}` — `{cur} → {new}` không hợp lệ; được phép: {sorted(TRANSITIONS.get(cur, []))}{hint}")
        else:
            unstable = [u for u in d["links"] if u in docs and docs[u]["status"] not in STABLE and u not in paths]
            if new in STABLE and unstable:
                warn.append((p, unstable))
            ok.append(p)
    for b in bad:
        print("❌ " + b)
    if warn and not confirm_up:
        print("\n⚠ Upstream chưa ổn định — cần user xác nhận (chạy lại với --confirm-upstream):")
        for p, us in warn:
            print(f"- `{p}` → {new}, nhưng upstream: " + ", ".join(f"`{u}` ({docs[u]['status']})" for u in us))
        sys.exit(3)
    if bad and not ok:
        sys.exit(1)
    today = date.today().isoformat()
    for p in ok:
        old = open(os.path.join(ROOT, p), encoding="utf-8").read()
        upd = {"status": new, "status_changed": today}
        if reason:
            upd["status_reason"] = quote(reason)
        rm = ["status_prev"] + ([] if reason else ["status_reason"])
        note = f"status {docs[p]['status']} → {new}" + (f": {reason}" if reason else "")
        write_doc(p, old, set_fm(old, upd, rm), note, dry)
    if not dry:
        print(f"\n✓ Đã chuyển {len(ok)} doc sang `{new}`.")
        sug = SUGGEST.get(new)
        if sug:
            feats = sorted({docs[p].get("feature", "") for p in ok} - {""})
            print("↳ gợi ý tiếp: " + sug.replace("{feature}", " ".join(feats) or "<feature>"))
    sys.exit(1 if bad else 0)


def cmd_restore(targets, dry):
    docs = load_docs()
    paths = resolve_targets(targets, docs)
    today = date.today().isoformat()
    rc = 0
    for p in paths:
        d = docs[p]
        if d["status"] != "stale":
            if len(targets) == 1 and targets[0].rstrip("/") == p:
                print(f"❌ `{p}` không ở stale (đang `{d['status']}`)")
                rc = 1
            continue
        prev = d.get("status_prev")
        if prev not in LIFECYCLE:
            print(f"❌ `{p}` không có `status_prev` hợp lệ (bị đánh stale trước khi hook lưu status cũ) — "
                  f"chọn status đích bằng `apply <status> {p}` (chỉ cho phép `revisions`) hoặc sửa tay.")
            rc = 1
            continue
        old = open(os.path.join(ROOT, p), encoding="utf-8").read()
        new = set_fm(old, {"status": prev, "status_changed": today,
                           "status_reason": quote("đã review upstream, không cần sửa")}, ["status_prev"])
        write_doc(p, old, new, f"status stale → {prev} (restore sau review upstream)", dry)
    sys.exit(rc)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report"); r.add_argument("prefix", nargs="?")
    i = sub.add_parser("impact"); i.add_argument("path")
    a = sub.add_parser("apply"); a.add_argument("new"); a.add_argument("targets", nargs="+")
    a.add_argument("--reason"); a.add_argument("--confirm-upstream", action="store_true"); a.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("restore"); s.add_argument("targets", nargs="+"); s.add_argument("--dry-run", action="store_true")
    o = ap.parse_args()
    if o.cmd == "report":
        cmd_report(o.prefix)
    elif o.cmd == "impact":
        cmd_impact(o.path)
    elif o.cmd == "apply":
        cmd_apply(o.new, o.targets, o.reason, o.confirm_upstream, o.dry_run)
    else:
        cmd_restore(o.targets, o.dry_run)


if __name__ == "__main__":
    main()
