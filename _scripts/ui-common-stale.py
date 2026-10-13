#!/usr/bin/env python3
"""Lan stale khi sửa UI Common Rules & Components (design/ui-common/).

Vì sao: hook post-edit-stale.sh chỉ lan theo `links:` trong docs/. CMP/GR sống ở
design/ui-common/ và được gọi bằng mã ("Xem CMP-09", "Theo GR-27") trong SRS, use case,
wireframe — sửa CMP không đánh dấu ai cả, nên hành vi mới (vd tooltip chip Điều kiện,
13/10/2026) lọt khỏi wireframe/Figma.

Cách làm:
  1. Băm từng mục: `## CMP-xx`, `### GR-xx` (tới heading cùng cấp kế tiếp) và từng dòng
     bảng `| E-common-NNN |`. Lưu ở _workspace/ui-common-hashes.json.
  2. So với lần trước → danh sách mã vừa đổi. Lần đầu (chưa có file băm) chỉ ghi mốc.
  3. Tìm doc gọi mã đó trong docs/ (.md và .html, trừ cr/exports/inbox/_reverse).
     - .md có `status:` → status: stale + status_prev (giống post-edit-stale.sh).
     - .html (wireframe, không có frontmatter) → chỉ ghi log + in cảnh báo.
  4. Ghi _workspace/staleness.md (cùng bảng 4 cột) + in danh sách cho người chạy.

Dùng:
  python3 _scripts/ui-common-stale.py <file đã sửa>   # hook gọi
  python3 _scripts/ui-common-stale.py --check          # chỉ in mã đổi, không ghi gì
"""
import hashlib
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = ["design/ui-common/screen-patterns.md", "design/ui-common/conventions.md"]
HASHES = os.path.join(ROOT, "_workspace", "ui-common-hashes.json")
LOG = os.path.join(ROOT, "_workspace", "staleness.md")
SKIP_DIRS = ("/cr/", "/exports/", "/inbox/", "/_reverse/")


def sections(path):
    """{mã: hash} cho 1 file nguồn."""
    out = {}
    try:
        lines = open(path, encoding="utf-8").read().split("\n")
    except FileNotFoundError:
        return out
    head = re.compile(r"^(#{2,3})\s+((?:CMP|GR)-\d+)\b")
    i = 0
    while i < len(lines):
        m = head.match(lines[i])
        if m:
            level, code = len(m.group(1)), m.group(2)
            j = i + 1
            while j < len(lines):
                h = re.match(r"^(#{1,6})\s", lines[j])
                if h and len(h.group(1)) <= level:
                    break
                j += 1
            body = "\n".join(lines[i:j]).strip()
            out[code] = hashlib.sha256(body.encode()).hexdigest()[:12]
            i = j
            continue
        e = re.match(r"^\|\s*(E-common-\d+)\s*\|", lines[i])
        if e:
            out[e.group(1)] = hashlib.sha256(lines[i].strip().encode()).hexdigest()[:12]
        i += 1
    return out


def current():
    allh = {}
    for rel in SOURCES:
        for code, h in sections(os.path.join(ROOT, rel)).items():
            allh[code] = {"hash": h, "file": rel}
    return allh


def users(codes):
    """{mã: [đường dẫn tương đối]} doc trong docs/ gọi mã."""
    pat = re.compile(r"\b(" + "|".join(re.escape(c) for c in codes) + r")\b(?!\d)")
    found = {c: [] for c in codes}
    for base, _, files in os.walk(os.path.join(ROOT, "docs")):
        rel_base = os.path.relpath(base, ROOT) + "/"
        if any(s in "/" + rel_base for s in SKIP_DIRS):
            continue
        for f in files:
            if not f.endswith((".md", ".html")):
                continue
            p = os.path.join(base, f)
            try:
                txt = open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            for c in set(pat.findall(txt)):
                found[c].append(os.path.relpath(p, ROOT))
    return found


def mark_stale(path):
    """Đánh stale 1 file .md có frontmatter status. Trả về status cũ hoặc None."""
    txt = open(path, encoding="utf-8").read()
    if not txt.startswith("---"):
        return None
    end = txt.find("\n---", 3)
    if end < 0:
        return None
    fm, rest = txt[:end], txt[end:]
    m = re.search(r"^status:\s*(\S+)\s*$", fm, re.M)
    if not m or m.group(1) in ("stale", "archived"):
        return None
    prev = m.group(1)
    fm = re.sub(r"^status_prev:.*\n?", "", fm, flags=re.M)
    fm = re.sub(r"^status:.*$", f"status: stale\nstatus_prev: {prev}", fm, count=1, flags=re.M)
    open(path, "w", encoding="utf-8").write(fm + rest)
    return prev


def log_rows(rows):
    if not rows:
        return
    if not os.path.exists(LOG) or os.path.getsize(LOG) == 0:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write("# Staleness Log\n\n> Lan truyền `status: stale` khi upstream đổi — append-only, mới nhất ở cuối.\n\n"
                    "| Ngày | Upstream đổi | Downstream bị đánh stale | Lý do |\n|---|---|---|---|\n")
    with open(LOG, "a", encoding="utf-8") as f:
        f.writelines(rows)


def main():
    check = "--check" in sys.argv
    edited = next((a for a in sys.argv[1:] if not a.startswith("--")), "")
    if edited and not any(edited.endswith(s) for s in SOURCES):
        return 0
    now = current()
    if not os.path.exists(HASHES):
        if not check:
            json.dump(now, open(HASHES, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
        print(f"ui-common-stale: ghi mốc {len(now)} mã CMP/GR/E-common (lần đầu, chưa lan stale).")
        return 0
    old = json.load(open(HASHES, encoding="utf-8"))
    changed = sorted(c for c in now if c not in old or old[c]["hash"] != now[c]["hash"])
    removed = sorted(c for c in old if c not in now)
    if not changed and not removed:
        return 0
    codes = changed + removed
    hits = users(codes)
    skill = os.environ.get("CLAUDE_SKILL_NAME", "manual")
    today = date.today().isoformat()
    rows, md_n, html = [], 0, []
    print(f"ui-common-stale: mã đổi {', '.join(changed) or '—'}" + (f" · mã bị xoá {', '.join(removed)}" if removed else ""))
    for c in codes:
        src = (now.get(c) or old.get(c))["file"]
        for rel in sorted(hits[c]):
            if rel.endswith(".html"):
                html.append((c, rel))
                rows.append(f"| {today} | `{src}` {c} | `{rel}` | gọi {c} — wireframe HTML không có status, cần rà tay (by {skill}) |\n")
                continue
            if check:
                print(f"  - {c}: {rel}")
                continue
            prev = mark_stale(os.path.join(ROOT, rel))
            if prev:
                md_n += 1
                rows.append(f"| {today} | `{src}` {c} | `{rel}` | gọi {c}, mục {c} vừa đổi (by {skill}) |\n")
    if check:
        for c, rel in html:
            print(f"  - {c}: {rel} (html)")
        return 0
    log_rows(rows)
    json.dump(now, open(HASHES, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    if md_n:
        print(f"  ↳ đánh stale {md_n} doc .md gọi các mã trên. Xem _workspace/staleness.md.")
    if html:
        print("  ↳ wireframe HTML cần rà lại (không tự đánh stale được):")
        for c, rel in sorted(set(html)):
            print(f"     - {rel} ({c})")
    if not md_n and not html:
        print("  ↳ chưa doc nào gọi các mã này.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
