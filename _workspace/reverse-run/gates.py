#!/usr/bin/env python3
"""Kiểm máy bộ reverse đã ghép (staging/{feature}/_final/) trước khi trình L1.

Báo từng nhóm riêng, không gộp "PASS":
  FILE    đủ file, không rỗng
  MỤC     spec đủ Mục 0–12; gaps đủ Mục 1–5; use case đủ mục a–h
  MÃ      không còn mã tạm (FR-a001, OQ-b3); mã chính thức đúng dạng
  NGUỒN   mọi dòng bảng spec Mục 2–7 có ô Nguồn đọc được (SRS Web/SRS Mobile/Thay đổi …) + ô Nhãn
  OQ      mỗi OQ có "Nguồn khách:"
  SAAS    ứng viên tham số không mang tiền tố P-
  FLOW    mỗi flow có đủ sequenceDiagram + flowchart
  MERMAID mọi khối mermaid biên dịch được (.claude/scripts/mermaid-verify.mjs)

Usage: python3 _workspace/reverse-run/gates.py <feature> [--dir <thư mục bộ file>] [--no-mermaid]
Exit 1 nếu có nhóm FAIL.
"""
import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = Path(__file__).resolve().parent
READABLE = re.compile(r"SRS (Web|Mobile) tr\.\d+|Thay đổi CHG-\d+ \(")
TEMP = re.compile(r"\b(FR|NFR|BR|E)-[a-z]\d{3}\b|\bSC-[a-z]\d{2}\b|\bOQ-[a-z]\d+\b")
FENCE = re.compile(r"```mermaid\n(.*?)```", re.S)


def cols(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("feature")
    ap.add_argument("--dir")
    ap.add_argument("--no-mermaid", action="store_true")
    a = ap.parse_args()
    f = a.feature
    d = Path(a.dir) if a.dir else RUN / "staging" / f / "_final"
    res = {}

    files = [d / f"{f}-reverse-spec.md", d / "reverse-sources.md", d / "reverse-gaps.md",
             d / "srs" / f"{f}-reverse-flows.md", d / "srs" / f"{f}-reverse-states.md", d / "srs" / f"{f}-reverse-erd.md",
             d / "usecases" / f"{f}-reverse-usecase-index.md"]
    ucs = sorted((d / "usecases").glob("uc-*.md"))
    bad = [str(p.relative_to(d)) for p in files + ucs if not p.exists() or p.stat().st_size == 0]
    res["FILE"] = (not bad and bool(ucs), bad or ([] if ucs else ["không có use case nào"]))
    if bad:
        report(res)
        raise SystemExit(1)

    spec = files[0].read_text(encoding="utf-8")
    gaps = files[2].read_text(encoding="utf-8")
    flows = files[3].read_text(encoding="utf-8")
    alltext = "\n".join(p.read_text(encoding="utf-8") for p in files + ucs)

    miss = [f"spec Mục {n}" for n in range(0, 13) if not re.search(rf"^## {n}\. ", spec, re.M)]
    miss += [f"gaps Mục {n}" for n in range(1, 6) if not re.search(rf"^## {n}\. ", gaps, re.M)]
    for uc in ucs:
        t = uc.read_text(encoding="utf-8")
        lack = [c for c in "abcdefgh" if not re.search(rf"^#+ {c}\. ", t, re.M)]
        if lack:
            miss.append(f"{uc.name} thiếu mục {','.join(lack)}")
    miss += [f"spec Mục {m.group(1)} còn <!-- TBD -->" for m in re.finditer(r"^## (\d+)\. [^\n]*\n\n<!-- TBD -->", spec, re.M)]
    res["MỤC"] = (not [m for m in miss if "TBD" not in m], miss)

    temps = sorted(set(m.group(0) for m in TEMP.finditer(alltext)))
    wrong = sorted(set(re.findall(rf"\b(?:FR|NFR|BR|E)-(?!{re.escape(f)}-\d{{3}}\b)[a-z][a-z0-9-]*-\d+\b", alltext)))
    res["MÃ"] = (not temps and not wrong, [f"mã tạm còn sót: {', '.join(temps[:10])}"] * bool(temps)
                 + [f"mã sai dạng: {', '.join(wrong[:10])}"] * bool(wrong))

    # NGUỒN: bảng trong spec Mục 2–7 (+ 11)
    probs, sec = [], None
    for line in spec.split("\n"):
        m = re.match(r"^## (\d+)\. ", line)
        if m:
            sec, header = int(m.group(1)), None
            continue
        if sec in (2, 3, 4, 5, 6, 7, 11) and line.startswith("|"):
            c = cols(line)
            if re.match(r"^-+$", c[0].replace(":", "")):
                continue
            if header is None or "Nguồn" in c:
                header = c
                continue
            if "Nguồn" not in header:
                continue
            src = c[header.index("Nguồn")] if header.index("Nguồn") < len(c) else ""
            lab = c[header.index("Nhãn")] if "Nhãn" in header and header.index("Nhãn") < len(c) else "?"
            if not READABLE.search(src):
                probs.append(f"Mục {sec} · {c[0][:30]}: Nguồn không đọc được «{src[:40]}»")
            if not re.search(r"[✅🔵🟡]", lab):
                probs.append(f"Mục {sec} · {c[0][:30]}: thiếu Nhãn")
    res["NGUỒN"] = (not probs, probs[:15] + ([f"… và {len(probs) - 15} dòng nữa"] if len(probs) > 15 else []))

    oq = re.findall(r"^\s*- \[[ x]\] (OQ-\d+)[^\n]*$", gaps, re.M)
    no_cust = [m.group(1) for m in re.finditer(r"^\s*- \[[ x]\] (OQ-\d+)([^\n]*)$", gaps, re.M) if "Nguồn khách:" not in m.group(2)]
    res["OQ"] = (not no_cust, [f"{len(oq)} OQ, thiếu Nguồn khách: {', '.join(no_cust[:10])}"] if no_cust else [f"{len(oq)} OQ"])

    s5 = re.split(r"^## ", gaps.split("## 5.", 1)[1], flags=re.M)[0] if "## 5." in gaps else ""
    pc = re.findall(r"\bP-[a-z0-9]+(?:-[a-z0-9]+)*\b", s5)
    res["SAAS"] = (not pc, [f"tiền tố P- trong ứng viên: {', '.join(pc[:8])}"] if pc else
                   [f"{len([l for l in s5.split(chr(10)) if l.startswith('|')]) - 2} ứng viên"])

    blocks = re.split(r"^#{2,3} Flow: ", flows, flags=re.M)[1:]
    fb = []
    for b in blocks:
        name = b.split("\n", 1)[0].strip()
        nxt = re.split(r"^## Nhóm: ", b, flags=re.M)[0]
        if "sequenceDiagram" not in nxt or "flowchart" not in nxt:
            fb.append(name)
    res["FLOW"] = (bool(blocks) and not fb, [f"{len(blocks)} flow"] + [f"thiếu 1 loại sơ đồ: {n}" for n in fb])

    if a.no_mermaid:
        res["MERMAID"] = (True, ["bỏ qua (--no-mermaid)"])
    else:
        fails = []
        for p in files[3:6] + ucs:
            if "```mermaid" not in p.read_text(encoding="utf-8"):
                continue
            r = subprocess.run(["node", str(ROOT / ".claude/scripts/mermaid-verify.mjs"), "--file", str(p)],
                               capture_output=True, text=True, cwd=ROOT)
            if r.returncode:
                fails.append(f"{p.name}: {r.returncode} khối lỗi — " + " | ".join(
                    l.strip() for l in r.stdout.split("\n") if "FAIL" in l)[:300])
        res["MERMAID"] = (not fails, fails)

    report(res)
    raise SystemExit(0 if all(ok for ok, _ in res.values()) else 1)


def report(res):
    for k, (ok, notes) in res.items():
        print(f"{'PASS' if ok else 'FAIL'} {k:8s} " + ("; ".join(notes) if notes else ""))


if __name__ == "__main__":
    main()
