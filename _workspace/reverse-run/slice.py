#!/usr/bin/env python3
"""Cắt lát nguồn cho từng phần của reverse-plan.json → slices/{feature}--{part}.md

Mỗi lát gồm: đầu lát (feature, phần, cách ghi nguồn), mục lục các mục trong phần (mã + tên + trang),
dòng thay đổi CHG liên quan (chép nguyên từ ghi chép thay đổi), rồi nội dung SRS Web theo khoảng trang
và SRS Mobile theo khoảng dòng. Giữ nguyên mốc trang; link ảnh đổi thành đường dẫn từ gốc repo.

Usage: python3 _workspace/reverse-run/slice.py [feature ...]     (không tham số = mọi feature)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
PLAN = json.loads((ROOT / "docs/_reverse/reverse-plan.json").read_text(encoding="utf-8"))
SRC = PLAN["sources"]

web_txt = (ROOT / SRC["web"]["file"]).read_text(encoding="utf-8")
mob_lines = (ROOT / SRC["mobile"]["file"]).read_text(encoding="utf-8").split("\n")
chg_txt = (ROOT / SRC["changes"]["file"]).read_text(encoding="utf-8")

WEB_PAGE = {int(m.group(1)): m.start() for m in re.finditer(r"<!-- Page (\d+) -->", web_txt)}
WEB_IMG = SRC["web"]["images"]
MOB_IMG = SRC["mobile"]["images"]

# Mục lục web: các dòng "Tên mục  số-trang" trong 9 trang đầu
WEB_TOC = []
for line in web_txt[:WEB_PAGE[10]].split("\n"):
    m = re.match(r"^(.*\S)\s+(\d{1,4})$", line.strip())
    if m and not line.startswith("<!--"):
        WEB_TOC.append((int(m.group(2)), m.group(1)))


def web_pages(a, b):
    end = WEB_PAGE.get(b + 1, len(web_txt))
    return web_txt[WEB_PAGE[a]:end].replace("](images/", f"]({WEB_IMG}")


def mob_range(a, b):
    chunk = "\n".join(mob_lines[a - 1:b])
    # mốc trang mobile gần nhất phía trên dòng a, để lát mở đầu có số trang
    page = None
    for i in range(a - 1, -1, -1):
        m = re.match(r"<!-- Trang (\d+) -->", mob_lines[i])
        if m:
            page = m.group(1)
            break
    head = f"<!-- Trang {page} -->\n" if page and not chunk.lstrip().startswith("<!-- Trang") else ""
    return head + chunk.replace("](images/", f"]({MOB_IMG}")


def mob_toc(a, b):
    out, page = [], None
    for i in range(0, b):
        l = mob_lines[i]
        m = re.match(r"<!-- Trang (\d+) -->", l)
        if m:
            page = m.group(1)
        if i >= a - 1 and re.match(r"^#{2,3} ", l):
            out.append((page, l.lstrip("#").strip()))
    return out


def chg_rows(ids):
    rows = []
    hdr = next((l for l in chg_txt.split("\n") if l.startswith("| Mã | Chỗ trong SRS v2.0")), "")
    for cid in ids:
        rows += [l for l in chg_txt.split("\n") if l.startswith(f"| {cid} |")]
    return ([hdr, re.sub(r"[^|]+", "---", hdr)] + rows) if rows else []


def build(feat, part):
    w, mo = SRC["web"], SRC["mobile"]
    out = [f"# Lát nguồn: {feat['slug']} — phần {part['id']}: {part['name']}", "",
           f"> Feature: **{feat['name']}** (`{feat['slug']}`) · module: {feat.get('module', '—')}",
           f"> Nguồn: **{w['short']}** = {w['title']}, bản {w['version']} (`{w['file']}`, mốc `<!-- Page N -->`)"
           + (f" · **{mo['short']}** = {mo['title']}, bản {mo['version']} (`{mo['file']}`, mốc `<!-- Trang N -->`)"
              if part["mobile_lines"] else ""),
           "> Cách ghi nguồn: xem `_workspace/reverse-run/brief.md` Mục 4.", ""]
    out += ["## Mục lục phần (danh sách phải phủ hết)", "", "| Nguồn | Trang | Mục |", "|---|---|---|"]
    for a, b in part["web_pages"]:
        for p, t in WEB_TOC:
            if a <= p <= b:
                out.append(f"| {w['short']} | {p} | {t} |")
    for a, b in part["mobile_lines"]:
        for p, t in mob_toc(a, b):
            out.append(f"| {mo['short']} | {p} | {t} |")
    out.append("")
    if feat["changes"]:
        out += ["## Thay đổi đã chốt/đề xuất đụng tới phần này (chép từ ghi chép thay đổi — dùng cho Mục 0.3)", ""]
        out += chg_rows([c["id"] for c in feat["changes"]]) + [""]
    for a, b in part["web_pages"]:
        out += [f"## {w['short']} — trang {a}–{b}", "", web_pages(a, b), ""]
    for a, b in part["mobile_lines"]:
        out += [f"## {mo['short']} — dòng {a}–{b} của file", "", mob_range(a, b), ""]
    return "\n".join(out)


def main():
    want = set(sys.argv[1:])
    (RUN / "slices").mkdir(exist_ok=True)
    keep = {f"{f['slug']}--{p['id']}.md" for f in PLAN["features"] for p in f["parts"]}
    for old in (RUN / "slices").glob("*.md"):
        if old.name not in keep:
            old.unlink()
    for feat in PLAN["features"]:
        if want and feat["slug"] not in want:
            continue
        for part in feat["parts"]:
            p = RUN / "slices" / f"{feat['slug']}--{part['id']}.md"
            text = build(feat, part)
            p.write_text(text, encoding="utf-8")
            imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
            missing = [i for i in imgs if not (ROOT / i).exists()]
            print(f"{p.relative_to(ROOT)}  {len(text)//1000}k ký tự · {len(imgs)} ảnh"
                  + (f" · THIẾU {len(missing)} ảnh" if missing else ""))


if __name__ == "__main__":
    main()
