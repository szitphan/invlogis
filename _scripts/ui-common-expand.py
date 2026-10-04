#!/usr/bin/env python3
"""Sinh Phụ lục A (UI Common Rules & Components) cho SRS spec — chép NGUYÊN VĂN từ nguồn.

Nguồn: design/ui-common/screen-patterns.md (CMP), design/ui-common/conventions.md (GR + E-common),
design/design.md (mục được CMP/GR trỏ tới qua dòng `- **design.md:** A; B`).
Mã lấy từ spec (ngoài vùng phụ lục): CMP-NN, GR-NN, E-common-NNN.

  python3 _scripts/ui-common-expand.py <spec.md>           # in khối phụ lục ra stdout
  python3 _scripts/ui-common-expand.py <spec.md> --write   # thay khối giữa 2 marker trong spec
  python3 _scripts/ui-common-expand.py <spec.md> --check   # exit 0 khớp · 1 cũ · 2 thiếu marker

Rule: .claude/rules/ui-common-rules-components.md Mục 12.
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SP = ROOT / "design/ui-common/screen-patterns.md"
CV = ROOT / "design/ui-common/conventions.md"
DS = ROOT / "design/design.md"
BEGIN = "<!-- ui-common:begin"
END = "<!-- ui-common:end -->"
HEADING = "## Phụ lục A — UI Common Rules & Components áp dụng"


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def strip_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:]
    return text


def sections(text, level):
    """{heading_text: (line_no, body)} cho heading đúng `level` (#*level); body tới heading cùng/cao hơn."""
    lines = text.split("\n")
    out, cur, start, buf = {}, None, 0, []
    pat = re.compile(r"^(#{1,6}) (.*)$")
    for i, line in enumerate(lines, 1):
        m = pat.match(line)
        if m and len(m.group(1)) <= level:
            if cur is not None:
                out[cur] = (start, "\n".join(buf).strip("\n"))
            cur = m.group(2).strip() if len(m.group(1)) == level else None
            start, buf = i, []
            continue
        if cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = (start, "\n".join(buf).strip("\n"))
    return {k: (ln, re.sub(r"(\n\s*-{3,}\s*)+$", "", b)) for k, (ln, b) in out.items()}


def demote(body, by):
    return re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + by) + " ", body, flags=re.M)


def codes_in(text):
    cmp_ = sorted(set(re.findall(r"\bCMP-(\d{2})\b", text)))
    gr = sorted(set(re.findall(r"\bGR-(\d{2})\b", text)))
    err = sorted(set(re.findall(r"\bE-common-(\d{3})\b", text)))
    return cmp_, gr, err


def outside_block(spec):
    i, j = spec.find(BEGIN), spec.find(END)
    return spec if i == -1 or j == -1 else spec[:i] + spec[j + len(END):]


def design_refs(body):
    m = re.search(r"^- \*\*design\.md:\*\*\s*(.+)$", body, flags=re.M)
    if not m or m.group(1).strip() in ("—", "-"):
        return []
    return [x.strip() for x in m.group(1).split(";") if x.strip()]


def build(spec_path):
    spec = read(spec_path)
    cmp_, gr, err = codes_in(outside_block(spec))
    sp, cv, ds = (read(p) for p in (SP, CV, DS))
    if not sp or not cv:
        return None, "Chưa có UI Common Rules & Components (design/ui-common/screen-patterns.md / conventions.md)"

    sp_secs = {k.split(" ")[0]: v for k, v in sections(sp, 2).items() if k.startswith("CMP-")}
    cv_secs = {k.split(" ")[0]: v for k, v in sections(cv, 3).items() if k.startswith("GR-")}
    ds_secs = sections(ds, 3)
    rel_img = "../../../design/ui-common/images/"  # spec ở docs/{feature}/srs/

    out, missing, wanted = [], [], []

    def add_refs(body):
        for ref in design_refs(body):
            if ref not in wanted:
                wanted.append(ref)

    if cmp_:
        out.append("### A.1 Component dùng chung (CMP)\n")
        for n in cmp_:
            key = f"CMP-{n}"
            if key not in sp_secs:
                missing.append(key)
                continue
            line, body = sp_secs[key]
            title = next(k for k in sections(sp, 2) if k.startswith(key))
            body = body.replace("](images/", "](" + rel_img)
            out.append(f"#### {title}\n\n_Nguồn: `design/ui-common/screen-patterns.md:{line}`_\n\n{demote(body, 2)}\n")
            add_refs(body)
    if gr:
        out.append("### A.2 Quy tắc giao diện chung (GR)\n")
        for n in gr:
            key = f"GR-{n}"
            if key not in cv_secs:
                missing.append(key)
                continue
            line, body = cv_secs[key]
            title = next(k for k in sections(cv, 3) if k.startswith(key))
            out.append(f"#### {title}\n\n_Nguồn: `design/ui-common/conventions.md:{line}`_\n\n{demote(body, 1)}\n")
            add_refs(body)
    if wanted:
        out.append("### A.3 Chi tiết từ design system\n")
        for ref in wanted:
            hit = next((k for k in ds_secs if k.startswith(ref)), None)
            if not hit:
                missing.append(f"design.md › {ref}")
                continue
            line, body = ds_secs[hit]
            out.append(f"#### {hit}\n\n_Nguồn: `design/design.md:{line}`_\n\n{demote(body, 2)}\n")
    if err:
        rows = {}
        for row in cv.split("\n"):
            m = re.match(r"^\| (E-common-(\d{3})) \|(.*)$", row)
            if m:
                rows[m.group(2)] = row
        out.append("### A.4 Lỗi dùng chung (E-common)\n")
        out.append("| Mã lỗi | Loại (GR-15) | Khi nào | Câu hiển thị | Quy tắc |\n|---|---|---|---|---|")
        for n in err:
            if n in rows:
                out.append(rows[n])
            else:
                missing.append(f"E-common-{n}")
        out.append("")

    if not out:
        out.append("_Feature chưa gọi CMP/GR/E-common nào._\n")
    if missing:
        out.append("> Không tìm thấy trong nguồn: " + ", ".join(missing) + "\n")

    body = "\n".join(out).rstrip() + "\n"
    head = (f"{BEGIN} — máy sinh bởi _scripts/ui-common-expand.py, KHÔNG sửa tay; "
            f"sửa ở nguồn rồi chạy lại. Sinh {date.today().isoformat()} -->")
    return f"{head}\n\n{body}\n{END}", missing


def body_of(block):
    return block.split("\n", 1)[1] if block else ""


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    spec_path = Path(args[0])
    mode = args[1] if len(args) > 1 else ""
    block, info = build(spec_path)
    if block is None:
        print(info)
        return 2
    spec = read(spec_path)
    i, j = spec.find(BEGIN), spec.find(END)

    if mode == "--check":
        if i == -1 or j == -1:
            print("Thiếu Phụ lục A (marker ui-common) — chạy lại với --write")
            return 2
        current = spec[i:j + len(END)]
        if body_of(current) == body_of(block):
            print("Phụ lục A khớp nguồn.")
            return 0
        print("Phụ lục A đã CŨ so với nguồn (screen-patterns / conventions / design.md) — chạy lại với --write")
        return 1

    if mode == "--write":
        if i != -1 and j != -1:
            new = spec[:i] + block + spec[j + len(END):]
        else:
            new = spec.rstrip("\n") + f"\n\n{HEADING}\n\n{block}\n"
        spec_path.write_text(new, encoding="utf-8")
        print(f"Đã ghi Phụ lục A vào {spec_path}" + (f" — thiếu: {', '.join(info)}" if info else ""))
        return 0

    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
