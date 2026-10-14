#!/usr/bin/env python3
"""
Build 1 SRS tổng cho NHIỀU feature (chương theo feature). Nguồn vẫn là SRS từng feature —
script chỉ GỘP lúc xuất, không đổi cách viết.

Usage: python3 _scripts/build-srs-book.py --format md|html|pdf|docx [--features a,b,c] [--out <path>]

Bố cục:
  Phần I   Chung     — project-profile, system-overview, definitions, operating-environment,
                       tenant-parameters, UI Common (gộp Phụ lục A của mọi spec, mỗi CMP/GR 1 lần)
  Phần II  Feature   — mỗi feature 1 chương: spec (bỏ Phụ lục A + Mục Open Questions),
                       ERD, Flows, States, Userflow, Use cases
  Phần III Tổng hợp  — Open Questions theo feature, ma trận truy vết (usecase-index), feature chưa có SRS

Feature = mọi docs/*/srs/*-spec.md (bỏ zz-*, _*). --features đặt thứ tự + lọc; mặc định A→Z.
Render (mermaid, ảnh, pandoc, Chrome, verify) dùng lại build-export.py.
"""

import argparse
import importlib.util
import re
import shutil
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _viewer_wrapper import (  # noqa: E402
    build_viewer_html,
    demote_headings,
    doc_path,
    find_index_file,
    inline_local_images,
    list_glob,
    read_optional,
    render_md_offline,
    sanitize_embedded,
    strip_frontmatter,
)

_spec = importlib.util.spec_from_file_location("build_export", HERE / "build-export.py")
bx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bx)

UI_BEGIN = re.compile(r"<!-- ui-common:begin.*?-->", re.S)
UI_BLOCK = re.compile(r"<!-- ui-common:begin.*?-->(.*?)<!-- ui-common:end -->", re.S)
OQ_HEAD = re.compile(r"^##\s*\d*\.?\s*(open questions|câu hỏi mở)", re.I)
ITEM_HEAD = re.compile(r"^####\s+((?:CMP|GR)-\d+)\b", re.M)


def fm_field(text: str, key: str) -> str:
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return ""
    f = re.search(rf"^{key}:\s*(.+)$", m.group(1), re.M)
    return f.group(1).strip() if f else ""


def title_of(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", strip_frontmatter(text), re.M)
    return m.group(1).strip() if m else fallback


def discover(vault: Path, wanted: list) -> tuple:
    """Trả (features có spec theo thứ tự, features chưa có spec)."""
    docs = vault / "docs"
    all_dirs = sorted(d.name for d in docs.iterdir()
                      if d.is_dir() and not d.name.startswith(("_", "zz-"))
                      and d.name not in {"exports", "meetings", "reports", "inbox", "cr", "userguide"})
    with_spec = [f for f in all_dirs if doc_path(docs / f, "srs/spec.md").is_file()]
    if wanted:
        bad = [f for f in wanted if f not in all_dirs]
        if bad:
            sys.exit(f"❌ Feature không tồn tại: {', '.join(bad)}. Có: {', '.join(all_dirs)}")
        order = wanted
    else:
        order = all_dirs
    return [f for f in order if f in with_spec], [f for f in order if f not in with_spec]


def split_spec(spec: str) -> tuple:
    """Tách spec → (thân không Phụ lục A + không Mục OQ, khối Phụ lục A, Mục OQ)."""
    body = strip_frontmatter(spec)
    ui = ""
    m = UI_BLOCK.search(body)
    if m:
        ui = m.group(1)
        # bỏ cả heading "## Phụ lục A …" đứng ngay trước marker
        start = body.rfind("\n## ", 0, m.start())
        head = body[start:m.start()] if start != -1 else ""
        cut_from = start if start != -1 and "Phụ lục A" in head.split("\n", 2)[1] else m.start()
        body = body[:cut_from] + body[m.end():]
    oq = ""
    parts = re.split(r"\n(?=##\s)", body)
    keep = []
    for p in parts:
        if OQ_HEAD.match(p.lstrip()):
            oq = p
        else:
            keep.append(p)
    return "\n".join(keep), ui, oq


def merge_ui_common(blocks: list) -> str:
    """Gộp Phụ lục A của nhiều spec: mỗi CMP-/GR- 1 lần, xếp theo mã."""
    items = {}
    for blk in blocks:
        heads = list(ITEM_HEAD.finditer(blk))
        for i, h in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(blk)
            chunk = blk[h.start():end]
            # cắt heading cấp 3 (A.2 …) lọt vào cuối chunk
            chunk = re.split(r"\n(?=###\s)", chunk)[0]
            items.setdefault(h.group(1), chunk.strip())

    def key(k):
        kind, n = k.split("-")
        return (0 if kind == "CMP" else 1, int(n))

    cmp_ = [items[k] for k in sorted(items, key=key) if k.startswith("CMP")]
    gr = [items[k] for k in sorted(items, key=key) if k.startswith("GR")]
    out = []
    if cmp_:
        out.append("### Component dùng chung (CMP)\n\n" + "\n\n".join(cmp_))
    if gr:
        out.append("### Quy tắc giao diện chung (GR)\n\n" + "\n\n".join(gr))
    return "\n\n".join(out) if out else "_Chưa spec nào dùng UI Common._"


def prefix_anchors(md: str, feature: str) -> str:
    """Anchor sec-*/uc-* của từng chương → tiền tố feature, link không nhảy nhầm chương."""
    md = re.sub(r'id="((?:sec|uc)-[^"]+)"', rf'id="{feature}--\1"', md)
    return re.sub(r"\]\(#((?:sec|uc)-[^)]+)\)", rf"](#{feature}--\1)", md)


def chapter(n: int, feature: str, vault: Path) -> tuple:
    """Trả (md chương, ui block, oq, trace, srs_dir, title, status, updated)."""
    fdir = vault / "docs" / feature
    spec_raw = read_optional(doc_path(fdir, "srs/spec.md"))
    body, ui, oq = split_spec(spec_raw)
    title = title_of(spec_raw, feature).replace(" — Software Requirements Specification", "")
    # anchor đứng riêng trước heading: nằm TRONG heading thì mục lục pandoc (PDF/DOCX) mất link
    parts = [f'<a id="sec-spec"></a>\n\n## Chương {n}. {title}\n\n> Feature `{feature}` · '
             f'status `{fm_field(spec_raw, "status")}` · cập nhật {fm_field(spec_raw, "updated")}',
             "### Đặc tả yêu cầu\n\n" + demote_headings(body, 2)]
    for name, anc, label in [("erd.md", "sec-erd", "ERD"), ("flows.md", "sec-flows", "Flows"),
                             ("states.md", "sec-states", "States"), ("userflow.md", "sec-userflow", "Userflow")]:
        txt = read_optional(doc_path(fdir, f"srs/{name}"))
        if txt:
            parts.append(f'### <a id="{anc}"></a>{label}\n\n' + demote_headings(strip_frontmatter(txt), 2))
    ucs = list_glob(fdir / "usecases", "uc-*.md")
    if ucs:
        uc_md = [f'#### <a id="uc-{f.stem}"></a>{title_of(read_optional(f), f.stem)}\n\n'
                 + demote_headings(re.sub(r"\A\s*#\s+[^\n]+\n+", "", strip_frontmatter(read_optional(f))), 3)
                 for f in ucs]
        parts.append('### <a id="sec-functions"></a>Use cases\n\n' + "\n\n".join(uc_md))
    idx = find_index_file(fdir / "usecases")
    trace = demote_headings(strip_frontmatter(read_optional(idx)), 2) if idx else ""
    md = sanitize_embedded("\n\n".join(parts), fdir)
    return (prefix_anchors(md, feature), ui, oq, trace, fdir / "srs", title,
            fm_field(spec_raw, "status"), fm_field(spec_raw, "updated"))


def shared_section(path: Path, heading: str) -> str:
    txt = read_optional(path)
    if not txt:
        return ""
    return f"## {heading}\n\n" + demote_headings(strip_frontmatter(txt), 1)


def compose(vault: Path, features: list, missing: list, project: str) -> dict:
    today = date.today().isoformat()
    chapters = [chapter(i, f, vault) for i, f in enumerate(features, 1)]

    status_rows = "\n".join(f"| {i} | {c[5]} | `{f}` | `{c[6]}` | {c[7]} |"
                            for i, (f, c) in enumerate(zip(features, chapters), 1))
    cover = f"""<div class="cover">

# {project} — Software Requirements Specification

## Bản tổng hợp {len(features)} feature

**Ngày xuất:** {today}

| Chương | Feature | Slug | Status | Cập nhật |
|---|---|---|---|---|
{status_rows}

</div>
"""
    shared = vault / "docs" / "_shared"
    part1 = ["# Phần I — Chung"]
    for p, h in [(shared / "project-profile.md", "1. Giới thiệu & phạm vi"),
                 (shared / "system-overview.md", "2. Tổng quan hệ thống"),
                 (shared / "definitions.md", "3. Định nghĩa thuật ngữ"),
                 (shared / "operating-environment.md", "4. Môi trường vận hành"),
                 (vault / "docs" / "_product" / "tenant-parameters.md", "5. Tham số theo khách (P-…)")]:
        s = shared_section(p, h)
        if s:
            part1.append(sanitize_embedded(s, shared))
    ui_md = merge_ui_common([c[1] for c in chapters if c[1]])
    part1_ui = "## 6. UI Common Rules & Components\n\n" + ui_md

    part3 = ["# Phần III — Tổng hợp", "## Open Questions theo feature"]
    for f, c in zip(features, chapters):
        if c[2]:
            part3.append(f"### {c[5]} (`{f}`)\n\n" + demote_headings(re.sub(r"\A\s*##[^\n]*\n", "", c[2]), 2))
    part3.append("## Ma trận truy vết")
    for f, c in zip(features, chapters):
        part3.append(f"### {c[5]} (`{f}`)\n\n" + (c[3] or "_Chưa có usecase-index._"))
    part3.append("## Feature chưa có SRS\n\n" + ("\n".join(f"- `{f}`" for f in missing)
                                                  if missing else "_Không có._"))

    front = f"""---
type: export-srs-book
scope: project
features: [{', '.join(features)}]
status: generated
updated: {today}
---

{cover}
"""
    # Ảnh xử lý theo từng thư mục gốc (srs/ của feature, _shared) → trả các khúc kèm base_dir.
    first_srs = chapters[0][4] if chapters else shared
    segments = [(front + "\n\n".join(part1), shared), (part1_ui, first_srs)]
    segments.append(("# Phần II — Theo feature", shared))
    for f, c in zip(features, chapters):
        segments.append((c[0], c[4]))
    segments.append(("\n\n".join(part3), shared))
    return {"today": today, "segments": segments, "features": features}


def project_name(vault: Path) -> str:
    prof = read_optional(vault / "docs" / "_shared" / "project-profile.md")
    m = re.search(r"^\*\*(?:Tên dự án|Project)\*\*:\s*(.+)$", prof, re.M)
    return m.group(1).strip() if m else vault.name.title()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--format", default="md", choices=["md", "html", "pdf", "docx"])
    ap.add_argument("--features", default="")
    ap.add_argument("--out", default=None)
    ap.add_argument("--vault", default=".")
    args = ap.parse_args()
    vault = Path(args.vault).resolve()

    missing_tools = bx.check_tools({"md": [], "html": [], "pdf": ["mmdc", "pandoc"],
                                    "docx": ["mmdc", "pandoc"]}[args.format])
    chrome = bx.find_chrome()
    if args.format == "pdf" and not chrome:
        missing_tools.append("chrome")
    if missing_tools:
        print(f"❌ Format `{args.format}` cần tools: {', '.join(missing_tools)}", file=sys.stderr)
        print("Install:\n" + bx.install_hints(missing_tools), file=sys.stderr)
        sys.exit(2)

    wanted = [f.strip() for f in args.features.split(",") if f.strip()]
    features, missing = discover(vault, wanted)
    if not features:
        sys.exit("❌ Chưa feature nào có srs/{feature}-spec.md — chạy /srs trước.")
    print(f"→ {len(features)} feature có SRS: {', '.join(features)}")
    if missing:
        print(f"   Chưa có SRS (chỉ liệt kê ở Phần III): {', '.join(missing)}")

    project = project_name(vault)
    book = compose(vault, features, missing, project)
    today, segments = book["today"], book["segments"]
    exports_dir = vault / "docs" / "exports"
    exports_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", vault.name.lower()).strip("-")
    base = f"{today}-srs-{slug}"
    title = f"{project} — SRS"

    if args.format == "md":
        out = Path(args.out) if args.out else exports_dir / f"{base}.md"
        out.write_text("\n\n".join(s for s, _ in segments), encoding="utf-8")
        print(f"✅ Markdown: {out}")
        return

    # Frontmatter chỉ có nghĩa ở bản .md; HTML/PDF/DOCX render nó thành heading rác.
    segments[0] = (strip_frontmatter(segments[0][0]), segments[0][1])

    if args.format == "html":
        md = "\n\n".join(inline_local_images(s, d) for s, d in segments)
        tmp = exports_dir / f"_tmp-svg-{base}"
        try:
            html_body, mres = render_md_offline(md, tmp)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        html = build_viewer_html(title=title, subtitle=f"{len(features)} feature", date=today,
                                 md_content="", offline=True, prerendered_html=html_body,
                                 regen_cmd="python3 _scripts/build-srs-book.py --format html")
        out = Path(args.out) if args.out else exports_dir / f"{base}.html"
        out.write_text(html, encoding="utf-8")
        fail = sum(1 for _, ok, _ in mres if not ok)
        print(f"✅ HTML (offline): {out} ({out.stat().st_size // 1024} KB) · mermaid {len(mres) - fail} OK, {fail} lỗi")
        warns = bx.verify_html(out, chrome)
        print("   ⚠ " + "\n   ⚠ ".join(warns) if warns else "   ✓ Verify: DOM load OK, không console error.")
        return

    assets_root = exports_dir / "assets" / base
    parts, img_fail = [], 0
    for i, (s, d) in enumerate(segments):
        # mỗi khúc 1 thư mục con → ảnh trùng tên giữa các feature không đè nhau
        s2, res = bx.prerender_local_images(s, assets_root / f"part-{i:02d}", d, chrome)
        img_fail += sum(1 for _, ok, _ in res if not ok)
        parts.append(s2)
    md, mres = bx.prerender_mermaid("\n\n".join(parts), assets_root / "mermaid")
    # prerender_* trả path tương đối với assets_dir.parent.parent = exports/assets/ (assets_root
    # lồng thêm 1 cấp) → md tạm đặt ở exports/assets/ để pandoc --resource-path khớp.
    tmp_md = exports_dir / "assets" / f"_tmp-{base}.md"
    tmp_md.write_text(md, encoding="utf-8")
    try:
        out = Path(args.out) if args.out else exports_dir / f"{base}.{args.format}"
        rc = (bx.md_to_pdf_via_chrome(tmp_md, out, chrome, title=title) if args.format == "pdf"
              else bx.pandoc_to_docx(tmp_md, out))
        if rc != 0:
            sys.exit(rc)
        mfail = sum(1 for _, ok, _ in mres if not ok)
        print(f"✅ {args.format.upper()}: {out} ({out.stat().st_size // 1024} KB) · "
              f"mermaid {len(mres) - mfail} OK, {mfail} lỗi · ảnh lỗi {img_fail}")
        warns = bx.verify_pdf(out) if args.format == "pdf" else bx.verify_docx(out)
        print("   ⚠ " + "\n   ⚠ ".join(warns) if warns else f"   ✓ Verify: {args.format.upper()} không rỗng/hỏng.")
    finally:
        tmp_md.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
