#!/usr/bin/env python3
"""Ghép các phần của 1 feature thành bộ file đích (staging/{feature}/_final/, cùng cây với docs/_reverse/{feature}/).

- Đánh lại mã tạm (FR-a001, OQ-b3 …) thành mã chính thức (FR-{feature}-001, OQ-7 …), liên tục qua các phần
  theo thứ tự phần a → b → c và thứ tự xuất hiện; sửa mọi chỗ tham chiếu, kể cả dạng khoảng `FR-a001..a005`.
- Ghép từng Mục của spec/gaps/flows/states/erd; feature nhiều phần thì mỗi phần 1 tiêu đề con.
- Sinh frontmatter, Mục 0, reverse-sources.md, use case index.

Usage: python3 _workspace/reverse-run/assemble.py <feature> [--date YYYY-MM-DD]
"""
import argparse
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
PLAN = json.loads((ROOT / "docs/_reverse/reverse-plan.json").read_text(encoding="utf-8"))

SPEC_SECTIONS = [("1", "1. Scope"), ("2", "2. Actors & Stakeholders"), ("3", "3. Functional Requirements (FR)"),
                 ("4", "4. Non-Functional Requirements (NFR)"), ("5", "5. Business Rules"), ("6", "6. Error Matrix"),
                 ("7", "7. Success Criteria"), ("8", "8. Data Entities"), ("9", "9. Flows"), ("10", "10. Screens"),
                 ("11", "11. Constraints, Dependencies & Assumptions"), ("12", "12. Open Questions")]
SPEC_NOTE = {"8": "(tóm tắt — chi tiết ở `srs/{f}-reverse-erd.md`)", "9": "(tóm tắt — chi tiết ở `srs/{f}-reverse-flows.md`)",
             "12": None}
GAP_SECTIONS = [("1", "1. Open Questions"), ("2", "2. Gaps (nguồn thiếu hẳn)"), ("3", "3. Conflicts (nguồn mâu thuẫn)"),
                ("4", "4. Inferred assumptions (suy đoán cần verify)"), ("5", "5. Ứng viên tham số (cho /srs)")]
ISSUES_REL = "docs/_product/legacy-issues.md"


def main_checkout():
    """Đường dẫn checkout main (sổ vấn đề là file dùng chung, chỉ sửa trên main)."""
    import subprocess
    r = subprocess.run(["git", "-C", str(ROOT), "worktree", "list", "--porcelain"], capture_output=True, text=True)
    first = next((l.split(" ", 1)[1] for l in r.stdout.split("\n") if l.startswith("worktree ")), None)
    return Path(first) if first else ROOT


def issues_for(slug):
    """Dòng sổ vấn đề gắn feature (cột Feature có `slug` hoặc `*`) → bảng cho reverse-gaps Mục 6."""
    p = main_checkout() / ISSUES_REL
    if not p.exists():
        return f"<!-- không đọc được {ISSUES_REL} trên main -->"
    rows = []
    for line in p.read_text(encoding="utf-8").split("\n"):
        if not line.startswith("| ISS-"):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 6 and (f"`{slug}`" in c[3] or "`*`" in c[3]):
            rows.append(f"| {c[0]} | {c[1]} | {c[4]} | {c[5]} |")
    if not rows:
        return "Không có vấn đề nào trong sổ gắn với feature này."
    return "\n".join([f"> Chép từ [`{ISSUES_REL}`](../../_product/legacy-issues.md). Mỗi vấn đề cần quyết định trong brainstorm của feature.",
                      "", "| Mã | Vấn đề | Xử lý ở | Trạng thái |", "|---|---|---|---|"] + rows)

TEMP3 = re.compile(r"\b(FR|NFR|BR|E)-([a-z])(\d{3})\b")
TEMP_SC = re.compile(r"\bSC-([a-z])(\d{2})\b")
TEMP_OQ = re.compile(r"\bOQ-([a-z])(\d+)\b")
FENCE = re.compile(r"^(```|~~~)")


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def split_sections(text, pat=r"^## (0\.3|\d{1,2})\b[^\n]*$"):
    """{key: body} theo tiêu đề '## N. …' (key '0.3', '1' … '12'). Nội dung trước tiêu đề đầu bị bỏ."""
    out, key, buf = {}, None, []
    for line in text.split("\n"):
        m = re.match(pat, line)
        if m:
            if key is not None:
                out[key] = "\n".join(buf).strip()
            key, buf = m.group(1), []
        elif key is not None:
            buf.append(line)
    if key is not None:
        out[key] = "\n".join(buf).strip()
    return out


def demote(text, levels=1):
    """Hạ cấp tiêu đề markdown ngoài code fence."""
    out, fence = [], False
    for line in text.split("\n"):
        if FENCE.match(line.strip()):
            fence = not fence
        if not fence and re.match(r"^#{1,5} ", line):
            line = "#" * levels + line
        out.append(line)
    return "\n".join(out)


class Renumber:
    def __init__(self, feat):
        self.f = feat
        self.maps = {"FR": {}, "NFR": {}, "BR": {}, "E": {}, "SC": {}, "OQ": {}}
        self.undefined = []

    def define(self, kind, key):
        m = self.maps[kind]
        if key not in m:
            m[key] = len(m) + 1

    def collect(self, part, spec, gaps):
        # thứ tự định nghĩa: cột đầu của dòng bảng trong spec, rồi OQ trong gaps (sau đó spec Mục 12)
        for line in spec.split("\n"):
            if line.startswith("|"):
                first = line.split("|")[1].strip() if line.count("|") > 2 else ""
                m = TEMP3.fullmatch(first)
                if m:
                    self.define(m.group(1), (m.group(2), m.group(3)))
                m = TEMP_SC.fullmatch(first)
                if m:
                    self.define("SC", (m.group(1), m.group(2)))
        for m in re.finditer(r"^\s*- \[[ x]\] (OQ-([a-z])(\d+))", gaps + "\n" + spec, re.M):
            self.define("OQ", (m.group(2), m.group(3)))

    def fmt(self, kind, key):
        m = self.maps[kind]
        if key not in m:
            self.undefined.append(f"{kind}-{key[0]}{key[1]}")
            m[key] = len(m) + 1
        n = m[key]
        if kind == "OQ":
            return f"OQ-{n}"
        if kind == "SC":
            return f"SC-{self.f}-{n:02d}"
        return f"{kind}-{self.f}-{n:03d}"

    def apply(self, text):
        def rng3(m):
            kind = m.group(1)
            a = self.fmt(kind, (m.group(2), m.group(3)))
            b = self.fmt(kind, (m.group(4) or m.group(2), m.group(5)))
            return f"{a}..{b.rsplit('-', 1)[1]}"
        text = re.sub(r"\b(FR|NFR|BR|E)-([a-z])(\d{3})\.\.([a-z])?(\d{3})\b", rng3, text)

        def rng_oq(m):
            a = self.fmt("OQ", (m.group(1), m.group(2)))
            b = self.fmt("OQ", (m.group(3) or m.group(1), m.group(4)))
            return f"{a}..{b.split('-')[1]}"
        text = re.sub(r"\bOQ-([a-z])(\d+)\.\.([a-z])?(\d+)\b", rng_oq, text)
        text = TEMP3.sub(lambda m: self.fmt(m.group(1), (m.group(2), m.group(3))), text)
        text = TEMP_SC.sub(lambda m: self.fmt("SC", (m.group(1), m.group(2))), text)
        text = TEMP_OQ.sub(lambda m: self.fmt("OQ", (m.group(1), m.group(2))), text)
        return text


def page_ranges(part):
    w = ", ".join(f"tr.{a}–{b}" for a, b in part["web_pages"])
    m = ", ".join(f"dòng {a}–{b}" for a, b in part["mobile_lines"])
    return w, m


def frontmatter(kind, feat, today, extra=None):
    lines = ["---", f"type: {kind}", f"feature: {feat}"]
    if extra and "status" in extra:
        lines.append(f"status: {extra['status']}")
    lines.append(f"updated: {today}")
    if extra and "confidence" in extra:
        lines.append(f'confidence_summary: "{extra["confidence"]}"')
    if extra and extra.get("links"):
        lines.append("links:")
        lines += [f"  - {l}" for l in extra["links"]]
    lines.append("---")
    return "\n".join(lines)


def count_labels(text):
    rows = [l for l in text.split("\n") if l.startswith("|") and not re.match(r"^\|\s*-", l)]
    body = "\n".join(rows)
    return body.count("✅"), body.count("🔵"), body.count("🟡")


def merge(feat_plan, parts, key_sections, part_texts, multi):
    """Ghép từng Mục: 1 phần → giữ nguyên; nhiều phần → tiêu đề con theo phần, hạ cấp tiêu đề bên trong."""
    out = {}
    for key, _ in key_sections:
        chunks = []
        for p in parts:
            body = part_texts[p["id"]].get(key, "").strip()
            if not body:
                continue
            chunks.append(f"### {p['name']}\n\n{demote(body, 1)}" if multi else body)
        out[key] = "\n\n".join(chunks)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("feature")
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    fp = next(f for f in PLAN["features"] if f["slug"] == a.feature)
    f, today, src = fp["slug"], a.date, PLAN["sources"]
    base = RUN / "staging" / f
    parts = [p for p in fp["parts"] if (base / p["id"] / "spec.md").exists()]
    missing = [p["id"] for p in fp["parts"] if p not in parts]
    if missing:
        raise SystemExit(f"Thiếu spec.md của phần: {', '.join(missing)} — chưa ghép.")
    multi = len(parts) > 1
    rn = Renumber(f)
    raw = {}
    for p in parts:
        d = base / p["id"]
        raw[p["id"]] = {n: read(d / n) for n in ("spec.md", "gaps.md", "flows.md", "states.md", "erd.md")}
        raw[p["id"]]["index"] = read(d / "usecases/index-rows.md")
        rn.collect(p["id"], raw[p["id"]]["spec.md"], raw[p["id"]]["gaps.md"])
    for p in parts:
        for k in raw[p["id"]]:
            raw[p["id"]][k] = rn.apply(raw[p["id"]][k])

    out = base / "_final"
    if out.exists():
        shutil.rmtree(out)
    (out / "srs").mkdir(parents=True)
    (out / "usecases").mkdir()

    uses_mobile = any(p["mobile_lines"] for p in parts)
    links = [src["web"]["file"]] + ([src["mobile"]["file"]] if uses_mobile else [])
    if fp["changes"]:
        links.append(src["changes"]["file"])

    # ---- spec
    spec_parts = {p["id"]: split_sections(raw[p["id"]]["spec.md"]) for p in parts}
    merged = merge(fp, parts, [("0.3", "")] + SPEC_SECTIONS, spec_parts, multi)
    body = []
    if merged.get("0.3"):
        body += ["### 0.3 Khác biệt với thay đổi đã chốt", "", demote(merged["0.3"], 1) if multi else merged["0.3"], ""]
    for key, title in SPEC_SECTIONS:
        note = SPEC_NOTE.get(key)
        head = f"## {title}" + (f" {note.format(f=f)}" if note else "")
        content = merged.get(key) or "<!-- TBD -->"
        if key == "12":
            content = "> Danh sách đầy đủ OQ + Gap ở [`reverse-gaps.md`](./reverse-gaps.md). Dưới đây chỉ trích các OQ chặn tiến độ.\n\n" + content
        body += [head, "", content, ""]
    g, b, y = count_labels("\n".join(body))
    part_rows = []
    for p in parts:
        w, m = page_ranges(p)
        srcs = [f"{src['web']['short']} {w}"] if w else []
        if m:
            srcs.append(f"{src['mobile']['short']} {m}")
        part_rows.append(f"| {p['name']} | {'; '.join(srcs)} |")
    sec0 = ["## 0. Truy vết nguồn & độ tin cậy", "",
            f"- **Module:** {fp.get('module', '—')} (gắn tạm theo DEC-079, chốt ở PRD).",
            f"- **Nguồn:** {src['web']['title']} (bản {src['web']['version']})"
            + (f" và {src['mobile']['title']} (bản {src['mobile']['version']})" if uses_mobile else "")
            + " — chi tiết ở [`reverse-sources.md`](./reverse-sources.md).",
            "- **Câu hỏi mở / khác biệt:** xem [`reverse-gaps.md`](./reverse-gaps.md).",
            f"- **Độ tin cậy:** ✅ {g} · 🔵 {b} · 🟡 {y} (đếm trên các dòng bảng).",
            "- **Trạng thái:** tái lập từ SRS cũ, **CHƯA duyệt**. ✅ nghĩa là \"SRS cũ ghi rõ\", không có nghĩa "
            "\"hệ thống đang chạy đúng như thế\".", "",
            "| Phần | Nguồn đã đọc |", "|---|---|"] + part_rows + [""]
    spec = [frontmatter("reverse-srs", f, today, {"status": "draft", "confidence": f"✅{g} 🔵{b} 🟡{y}", "links": links}), "",
            f"# {fp['name']} (`{f}`) — SRS tái lập (reverse)", "",
            "> Trạng thái: `draft` (tái lập, chưa duyệt). Nhãn: ✅ chắc chắn · 🔵 suy đoán · 🟡 cần xác nhận.", ""] + sec0 + body
    (out / f"{f}-reverse-spec.md").write_text("\n".join(spec).rstrip() + "\n", encoding="utf-8")

    # ---- gaps
    gap_parts = {p["id"]: split_sections(raw[p["id"]]["gaps.md"], r"^## (\d)\b[^\n]*$") for p in parts}
    gm = merge(fp, parts, GAP_SECTIONS, gap_parts, multi)
    gaps = [f"# {fp['name']} (`{f}`) — Gaps & Open Questions", ""]
    for key, title in GAP_SECTIONS:
        gaps += [f"## {title}", "", gm.get(key) or "Không có.", ""]
    gaps += ["## 6. Vấn đề đội đã ghi nhận", "", issues_for(f), ""]
    (out / "reverse-gaps.md").write_text("\n".join(gaps).rstrip() + "\n", encoding="utf-8")

    # ---- sources
    rows = []
    for kind in ("web", "mobile"):
        if kind == "mobile" and not uses_mobile:
            continue
        s = src[kind]
        used = []
        for p in parts:
            w, m = page_ranges(p)
            r = w if kind == "web" else m
            if r:
                used.append(f"{p['name']}: {r}")
        enc = "OK — bảng chuyển từ PDF hay bị cắt ô" if kind == "web" else "OK"
        rows.append(f"| {s['short']} | {s['title']} — `{s['file']}` (ảnh: `{s['images']}`; bản gốc: {s['original']}) "
                    f"| pdf → md | bản {s['version']} | high | {enc} | {'<br>'.join(used)} |")
    if fp["changes"]:
        s = src["changes"]
        rows.append(f"| {s['short']} | {s['title']} — `{s['file']}` | md | 2026-10-12 | medium | OK | Mục 0.3: "
                    + "; ".join(f"{c['id']} ({c['desc']})" for c in fp["changes"]) + " |")
    sources = [f"# {fp['name']} (`{f}`) — Danh mục nguồn (provenance)", "",
               "| Nguồn | Tài liệu | Loại | Ngày | Confidence | Encoding | Phần suy ra từ đây |",
               "|---|---|---|---|---|---|---|"] + rows + ["",
               "## Ghi chú nguồn", "",
               "- SRS Web chuyển từ PDF theo bố cục trang: bảng hay bị cắt ô (chữ dồn dòng), `Cột n` là nhãn kỹ thuật. "
               "Ảnh trích lại từ PDF gốc ngày 2026-10-14 (lưu đồ hoạt động, lưu đồ trạng thái, mockup màn hình).",
               "- Hai nguồn nói khác nhau cùng 1 điểm → ghi cả hai, nhãn 🟡, Conflict ở `reverse-gaps.md`. Không tự chọn bên.",
               "- Ghi chép thay đổi là tài liệu của đội (không phải tài liệu khách), chỉ dùng để đối chiếu ở Mục 0.3."]
    (out / "reverse-sources.md").write_text("\n".join(sources) + "\n", encoding="utf-8")

    # ---- flows / states / erd
    for name, kind, title in (("flows.md", "reverse-srs-flows", "Flows"), ("states.md", "reverse-srs-states", "States"),
                              ("erd.md", "reverse-srs-erd", "ERD")):
        chunks = []
        for p in parts:
            t = raw[p["id"]][name].strip()
            t = re.sub(r"^# .*\n", "", t)  # bỏ tiêu đề cấp 1 nếu agent tự thêm
            if t:
                chunks.append(f"## Nhóm: {p['name']}\n\n{demote(t, 1)}" if multi else t)
        doc = [frontmatter(kind, f, today), "", f"# {fp['name']} (`{f}`) — {title} tái lập (reverse)", "",
               "\n\n".join(chunks) or "<!-- TBD -->"]
        (out / "srs" / f"{f}-reverse-{name.split('.')[0]}.md").write_text("\n".join(doc).rstrip() + "\n", encoding="utf-8")

    # ---- use cases
    seen, index_rows = {}, []
    for p in parts:
        ucdir = base / p["id"] / "usecases"
        rows_txt = raw[p["id"]]["index"]
        for uc in sorted(ucdir.glob("uc-*.md")) if ucdir.exists() else []:
            slug = uc.stem
            final = slug if slug not in seen else f"{slug}-{p['id']}"
            if final != slug:
                rows_txt = rows_txt.replace(f"({slug}.md)", f"({final}.md)").replace(f"[{slug}]", f"[{final}]")
            seen[final] = p["id"]
            (out / "usecases" / f"{final}.md").write_text(rn.apply(read(uc)).rstrip() + "\n", encoding="utf-8")
        index_rows += [l for l in rows_txt.split("\n") if l.startswith("|")]
    actors = sorted({l.split("|")[3].strip() for l in index_rows if l.count("|") > 4} - {""})
    idx = [frontmatter("reverse-usecase-index", f, today, {"status": "draft", "links": [f"docs/_reverse/{f}/{f}-reverse-spec.md"]}), "",
           f"# {fp['name']} (`{f}`) — Use Case Index (reverse)", "", "## Use cases", "",
           "| Slug | Title | Primary Actor | Related FR | Screens | Errors | OQ | Nguồn | Nhãn |",
           "|------|-------|---------------|-----------|---------|--------|-----|-------|------|"] + index_rows + ["",
           "## Actors", "", "| Actor |", "|---|"] + [f"| {x} |" for x in actors] + ["",
           "## Ghi chú", "",
           "* Use case **tái lập chưa duyệt** từ SRS cũ — mỗi mệnh đề mang nhãn ✅/🔵/🟡. Chạy `/usecase "
           f"{f}` (downstream) sau khi có SRS chính thức để điền truy vết đầy đủ.",
           "* Nhóm mục con cùng khuôn (vd các danh mục) viết 1 use case cho cả khuôn; khác biệt từng mục con ở bảng "
           "\"Khác biệt theo …\" trong spec Mục 3."]
    (out / "usecases" / f"{f}-reverse-usecase-index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    counts = {k: len(v) for k, v in rn.maps.items()}
    print(f"✓ {f}: ghép {len(parts)} phần → {out.relative_to(ROOT)}")
    print(f"  mã: {counts} · use case: {len(seen)} · nhãn spec ✅{g} 🔵{b} 🟡{y}")
    if rn.undefined:
        print(f"  ⚠ mã được tham chiếu nhưng không có dòng định nghĩa: {', '.join(sorted(set(rn.undefined)))}")


if __name__ == "__main__":
    main()
