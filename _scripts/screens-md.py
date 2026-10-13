#!/usr/bin/env python3
"""Bảng mô tả màn (5 cột) sau khi đã có Figma: chuyển sang screens/{flow}.md + sinh Phụ lục B cho SRS.

Vì sao: khi giao diện đã vẽ trên Figma, khung wireframe (HTML/ASCII) hết vai trò — hình là Figma, nhưng
bảng 5 cột vẫn là hợp đồng BA ↔ design (Figma không chứa validation, mã lỗi). Bảng được chép NGUYÊN VĂN
bằng máy sang .md để `/figma-sync` sửa từng row, và để SRS nhúng được (Phụ lục B). Rule:
.claude/rules/screen-source.md.

  python3 _scripts/screens-md.py migrate <feature> <flow-slug>            # in bản .md ra stdout + đếm row
  python3 _scripts/screens-md.py migrate <feature> <flow-slug> --write    # ghi screens/{flow}.md + dòng index
  python3 _scripts/screens-md.py appendix <feature>                       # in Phụ lục B ra stdout
  python3 _scripts/screens-md.py appendix <feature> --write               # thay khối giữa 2 marker trong spec
  python3 _scripts/screens-md.py appendix <feature> --check               # exit 0 khớp · 1 cũ/thiếu ảnh · 2 thiếu marker

migrate KHÔNG xoá file wireframe nguồn — `/figma-sync` xoá sau khi user duyệt L1 (git rm).
appendix chỉ lấy flow có Status `approved` trong screens/{feature}-screen-index.md.
"""
import re
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN = "<!-- screens:begin"
END = "<!-- screens:end -->"
HEADING = "## Phụ lục B — Màn hình (giao diện Figma + bảng mô tả)"
HEAD5 = "| # | Items | Control type | Data type | Description |\n|---|---|---|---|---|"
INDEX_HEAD = ["#", "Flow", "File", "Thiết bị", "Màn", "Figma", "Status", "Updated"]
TODAY = date.today().isoformat()


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def table_after(text, heading_re):
    """Bảng markdown đầu tiên sau heading khớp regex → list dict theo tên cột."""
    m = re.search(heading_re, text, re.M)
    if not m:
        return []
    rows, head = [], None
    for line in text[m.end():].split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            if head is not None and s:
                break
            continue
        cells = split_row(s)
        if head is None:
            head = cells
        elif re.fullmatch(r"[-:\s|]+", s):
            continue
        else:
            rows.append(dict(zip(head, cells)))
    return rows


def split_row(line):
    cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [c.strip() for c in cells]


def device_tag(text):
    return "mob" if re.search(r"mob|393|375", text, re.I) else "web"


# ---------- đọc nguồn ----------

class DescTable(HTMLParser):
    """Lấy bảng .wf-desc-table: hàng header 'Screen N: [x.y] (· State) Tên' + các row 5 ô."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_table = 0
        self.groups = []          # [(header_text, [[5 ô]])]
        self.row = None
        self.cell = None
        self.header_row = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table" and "wf-desc-table" in (a.get("class") or ""):
            self.in_table += 1
        if not self.in_table:
            return
        if tag == "tr":
            self.close_row()
            self.row = []
            self.header_row = "wf-desc-screen-header" in (a.get("class") or "")
        elif tag in ("td", "th"):
            self.close_cell()
            self.cell = []
        elif tag == "br" and self.cell is not None:
            self.cell.append("<br>")

    def handle_endtag(self, tag):
        if not self.in_table:
            return
        if tag in ("td", "th"):
            self.close_cell()
        elif tag == "tr":
            self.close_row()
        elif tag == "table":
            self.close_row()
            self.in_table -= 1

    def handle_data(self, data):
        if self.in_table and self.cell is not None:
            self.cell.append(data)

    def close_cell(self):
        if self.cell is not None and self.row is not None:
            txt = re.sub(r"\s*\n\s*", " ", "".join(self.cell)).strip()
            self.row.append(txt.replace("|", "\\|"))
        self.cell = None

    def close_row(self):
        self.close_cell()
        if self.row is None:
            return
        if self.header_row and self.row:
            self.groups.append((self.row[0], []))
        elif len(self.row) == 5 and self.row[0] != "#" and self.groups:
            self.groups[-1][1].append(self.row)
        self.row, self.header_row = None, False


def parse_html(path):
    """→ [(num, state|None, title, rows)]"""
    p = DescTable()
    p.feed(read(path))
    p.close_row()
    out = []
    for head, rows in p.groups:
        m = re.match(r"Screen\s+\d+\s*:\s*\[([\d.]+)\]\s*(?:·\s*(.+?)\s{1,}(?=\S))?(.*)$", head)
        if not m:
            raise SystemExit(f"Không đọc được hàng tiêu đề màn: {head!r}")
        num, state, title = m.group(1), m.group(2), m.group(3).strip()
        if state:  # 'Load error Dòng quy trình…' — tách tên state tiếng Anh khỏi tên Việt
            sm = re.match(r"((?:[A-Z][a-z]+)(?:\s+[a-z]+)*)\s+(.*)$", state + " " + title)
            if sm:
                state, title = sm.group(1), sm.group(2)
        out.append((num, state, title, rows))
    return out


def parse_ascii(path, by_slug):
    out = []
    text = read(path)
    for m in re.finditer(r"^##\s+Screen:\s*([^—:\n]+?)\s*(?:[—:-]\s*(.*))?$", text, re.M):
        slug, title = m.group(1).strip(), (m.group(2) or "").strip()
        nxt = re.search(r"^##\s", text[m.end():], re.M)
        body = text[m.end(): m.end() + nxt.start()] if nxt else text[m.end():]
        rows = [split_row(l) for l in body.split("\n")
                if l.strip().startswith("|") and not re.fullmatch(r"[-:\s|]+", l.strip())]
        rows = [r for r in rows if len(r) == 5 and r[0] != "#"]
        info = by_slug.get(slug)
        if not info:
            raise SystemExit(f"Slug '{slug}' trong {path.name} không có ở userflow Mục 2")
        out.append((info["[#]"], None, title or info["Màn hình"], rows))
    return out


# ---------- migrate ----------

def figma_links(fdir, flow):
    """screenId (kể cả '· State') → url, từ cột Figma của index wireframe cũ hoặc index screens."""
    links = {}
    for idx in list(fdir.glob("html-wireframe/*-wireframe-html-index.md")) + \
            list(fdir.glob("ascii-wireframe/*-wireframe-index.md")) + list(fdir.glob("screens/*-screen-index.md")):
        for m in re.finditer(r"\[([\d.]+ · (?:web|mob)(?: · [^\]]+)?)\]\((https://www\.figma\.com/[^)]+)\)", read(idx)):
            links.setdefault(m.group(1), m.group(2))
    return links


def migrate(feature, flow, write):
    fdir = ROOT / "docs" / feature
    uf = read(fdir / "srs" / f"{feature}-userflow.md")
    if not uf:
        raise SystemExit(f"Thiếu docs/{feature}/srs/{feature}-userflow.md")
    screens = table_after(uf, r"^## 2\.")
    by_num = {r["[#]"]: r for r in screens}
    by_slug = {r["Slug"]: r for r in screens}
    flows = {r["Flow-slug"]: r for r in table_after(uf, r"^## 3\. ")}
    if flow not in flows:
        raise SystemExit(f"Flow '{flow}' không có ở userflow Mục 3. Có: {', '.join(flows)}")
    dev = device_tag(flows[flow].get("Thiết bị", ""))

    html_src = fdir / "html-wireframe" / f"{flow}.html"
    ascii_src = fdir / "ascii-wireframe" / f"{flow}.md"
    if html_src.exists():
        src, groups = html_src, parse_html(html_src)
    elif ascii_src.exists():
        src, groups = ascii_src, parse_ascii(ascii_src, by_slug)
    else:
        raise SystemExit(f"Không có wireframe nguồn cho flow '{flow}' (html-wireframe/ hoặc ascii-wireframe/)")

    links = figma_links(fdir, flow)
    # gom state về dưới màn chính, giữ thứ tự xuất hiện màn chính
    order, blocks = [], {}
    for num, state, title, rows in groups:
        if num not in blocks:
            order.append(num)
            blocks[num] = {"title": None, "rows": None, "states": []}
        if state:
            blocks[num]["states"].append((state, title, rows))
        else:
            blocks[num]["title"], blocks[num]["rows"] = title, rows

    out = [f"# {flows[flow].get('Tên flow', flow)}", "",
           f"> Flow `{flow}` · thiết bị `{dev}` · bảng chép từ `{src.relative_to(ROOT)}` ngày {TODAY}. "
           "Giao diện là frame Figma; bảng 5 cột là hợp đồng — sửa qua `/figma-sync` hoặc `/cr`.", ""]
    count = []
    for num in order:
        b = blocks[num]
        info = by_num.get(num, {})
        slug = info.get("Slug", f"screen-{num}")
        sid = f"{num} · {dev}"
        title = b["title"] or info.get("Màn hình", "")
        out += [f"## Screen: {slug} — {title}", "", f"- **screenId:** {sid}",
                f"- **Figma:** " + (f"[{sid}]({links[sid]})" if sid in links else "chưa gắn"), ""]
        if b["rows"] is not None:
            out += [HEAD5] + [f"| {' | '.join(r)} |" for r in b["rows"]] + [""]
        else:
            out += ["_Không có bảng màn chính trong nguồn — chỉ có trạng thái._", ""]
        count.append((sid, len(b["rows"] or [])))
        for state, stitle, rows in b["states"]:
            ssid = f"{sid} · {state}"
            out += [f"### Trạng thái: {state} — {stitle}", "",
                    f"- **Figma:** " + (f"[{ssid}]({links[ssid]})" if ssid in links else "chưa gắn"), "",
                    HEAD5] + [f"| {' | '.join(r)} |" for r in rows] + [""]
            count.append((ssid, len(rows)))
    md = "\n".join(out).rstrip() + "\n"

    src_rows = sum(len(g[3]) for g in groups)
    dst_rows = sum(n for _, n in count)
    report = [f"Nguồn: {src.relative_to(ROOT)} · {len(groups)} khối màn/trạng thái · {src_rows} row",
              f"Đích:  docs/{feature}/screens/{flow}.md · {dst_rows} row " + ("✓ khớp" if src_rows == dst_rows else "✗ LỆCH")]
    report += [f"  {sid}: {n} row" for sid, n in count]
    missing = [sid for sid, _ in count if sid not in links]
    if missing:
        report.append(f"Chưa có link Figma: {', '.join(missing)}")

    if not write:
        print(md)
        print("\n".join(report), file=sys.stderr)
        return 0 if src_rows == dst_rows else 1
    if src_rows != dst_rows:
        print("\n".join(report), file=sys.stderr)
        return 1
    sdir = fdir / "screens"
    sdir.mkdir(exist_ok=True)
    (sdir / f"{flow}.md").write_text(md, encoding="utf-8")
    upsert_index(feature, flow, flows[flow], [sid for sid, _ in count if sid.count(" · ") == 1], links)
    print("\n".join(report))
    return 0


def upsert_index(feature, flow, flow_row, sids, links):
    idx = ROOT / "docs" / feature / "screens" / f"{feature}-screen-index.md"
    text = read(idx)
    if not text:
        text = (f"---\ntype: screen-index\nfeature: {feature}\nstatus: draft\nupdated: {TODAY}\nlinks:\n"
                f"  - docs/{feature}/srs/{feature}-userflow.md\n  - docs/{feature}/srs/{feature}-spec.md\n---\n\n"
                f"# {feature} — Màn hình (Figma + bảng mô tả)\n\n## Flows\n\n"
                f"| {' | '.join(INDEX_HEAD)} |\n|{'---|' * len(INDEX_HEAD)}\n")
    rows = table_after(text, r"^## Flows")
    figma = " · ".join(f"[{s}]({links[s]})" for s in sids if s in links) or "chưa gắn"
    new = {"Flow": flow_row.get("Tên flow", flow), "File": f"[{flow}.md]({flow}.md)",
           "Thiết bị": flow_row.get("Thiết bị", ""), "Màn": " → ".join(sids), "Figma": figma,
           "Status": "draft", "Updated": TODAY}
    hit = next((r for r in rows if f"({flow}.md)" in r.get("File", "")), None)
    if hit:
        hit.update({k: v for k, v in new.items() if k != "Status"})
    else:
        rows.append({"#": str(len(rows) + 1), **new})
    tbl = f"| {' | '.join(INDEX_HEAD)} |\n|{'---|' * len(INDEX_HEAD)}\n" + \
        "".join(f"| {' | '.join(r.get(h, '') for h in INDEX_HEAD)} |\n" for r in rows)
    m = re.search(r"^## Flows\s*\n\s*\n?(\|.*\n)+", text, re.M)
    text = text[:m.start()] + "## Flows\n\n" + tbl + text[m.end():] if m else text.rstrip() + "\n\n## Flows\n\n" + tbl
    text = re.sub(r"^updated: .*$", f"updated: {TODAY}", text, count=1, flags=re.M)
    idx.write_text(text, encoding="utf-8")


# ---------- appendix ----------

def build_appendix(feature):
    sdir = ROOT / "docs" / feature / "screens"
    idx = read(sdir / f"{feature}-screen-index.md")
    if not idx:
        return None, [f"Chưa có docs/{feature}/screens/{feature}-screen-index.md — chạy /figma-sync trước"]
    parts, problems = [], []
    for r in table_after(idx, r"^## Flows"):
        if r.get("Status", "").strip() != "approved":
            continue
        fm = re.search(r"\(([^)]+\.md)\)", r.get("File", ""))
        if not fm:
            continue
        body = read(sdir / fm.group(1))
        for img in re.findall(r"!\[[^\]]*\]\((images/[^)]+)\)", body):
            if not (sdir / img).exists():
                problems.append(f"thiếu ảnh {img}")
        if "](images/" not in body:
            problems.append(f"flow {fm.group(1)} đã approved nhưng chưa có ảnh Figma")
        body = re.sub(r"^# .*\n", "", body, count=1)
        body = re.sub(r"^(#{2,5}) ", lambda m: "#" * (len(m.group(1)) + 2) + " ", body, flags=re.M)
        body = body.replace("](images/", "](../screens/images/")
        parts.append(f"### B.{len(parts) + 1} {r.get('Flow', '')}\n\n_Nguồn: docs/{feature}/screens/{fm.group(1)}_\n\n{body.strip()}\n")
    if not parts:
        return None, ["Chưa có flow nào ở trạng thái approved trong screen-index"]
    head = (f"{BEGIN} — máy sinh bởi _scripts/screens-md.py, KHÔNG sửa tay; sửa screens/*.md "
            f"(qua /figma-sync) rồi chạy lại. Sinh {TODAY} -->")
    return f"{head}\n\n" + "\n".join(parts) + f"\n{END}", problems


def appendix(feature, mode):
    spec_path = ROOT / "docs" / feature / "srs" / f"{feature}-spec.md"
    spec = read(spec_path)
    if not spec:
        print(f"Thiếu {spec_path.relative_to(ROOT)}")
        return 2
    block, problems = build_appendix(feature)
    if block is None:
        print("; ".join(problems))
        return 2
    i, j = spec.find(BEGIN), spec.find(END)
    body = lambda b: b.split("\n", 1)[1] if b else ""
    if mode == "--check":
        if i == -1 or j == -1:
            print("Thiếu Phụ lục B (marker screens) — chạy lại với --write")
            return 2
        if problems:
            print("Phụ lục B: " + "; ".join(problems))
            return 1
        if body(spec[i:j + len(END)]) == body(block):
            print("Phụ lục B khớp screens/.")
            return 0
        print("Phụ lục B đã CŨ so với screens/ — chạy lại với --write")
        return 1
    if mode == "--write":
        if i != -1 and j != -1:
            new = spec[:i] + block + spec[j + len(END):]
        else:
            new = spec.rstrip("\n") + f"\n\n{HEADING}\n\n{block}\n"
        spec_path.write_text(new, encoding="utf-8")
        print(f"Đã ghi Phụ lục B vào {spec_path.relative_to(ROOT)}" + (f" — cảnh báo: {'; '.join(problems)}" if problems else ""))
        return 0
    print(block)
    if problems:
        print("Cảnh báo: " + "; ".join(problems), file=sys.stderr)
    return 0


def main():
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == "migrate":
        return migrate(a[1], a[2], "--write" in a)
    if len(a) >= 2 and a[0] == "appendix":
        return appendix(a[1], a[2] if len(a) > 2 else "")
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
