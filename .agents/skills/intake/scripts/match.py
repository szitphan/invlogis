#!/usr/bin/env python3
"""Tìm tài liệu cũ trong docs-input/ mà tài liệu mới có thể là PHIÊN BẢN CẬP NHẬT.

Dùng:  python3 match.py <file .md mới> [--root docs-input] [--top 5]

Chấm 2 điểm cho mỗi .md đã có (bỏ README, _changes/, thư mục ẩn, chính nó):
  - tên:   độ giống tên file/tiêu đề sau khi bỏ ngày, số phiên bản, dấu (0..1)
  - nội dung: tỷ lệ cụm 5 từ dùng chung, tính trên tài liệu NHỎ hơn (0..1)
Gợi ý: nội dung ≥ 0.35 hoặc (tên ≥ 0.75 và nội dung ≥ 0.10) → rất có thể là bản cập nhật.
Kết quả chỉ để ĐỀ XUẤT — luôn hỏi user xác nhận.
"""
import argparse, difflib, glob, os, re, unicodedata

WORD = re.compile(r"[^\W_]+", re.U)


def strip_acc(s):
    s = unicodedata.normalize("NFD", s.lower()).replace("đ", "d")
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def name_key(s):
    s = strip_acc(os.path.splitext(os.path.basename(s))[0])
    s = re.sub(r"\d{4}[-_.]?\d{2}[-_.]?\d{2}|\d{1,2}[-_.]\d{1,2}[-_.]\d{2,4}", " ", s)   # ngày
    s = re.sub(r"\b(v|ver|version|ban|rev|r)\s*\d+(\.\d+)*\b|\b(final|sua|moi|new|update|cap nhat|copy)\b|\(\d+\)", " ", s)
    return " ".join(WORD.findall(s))


def title(md):
    m = re.search(r"^# (.+)$", md, re.M)
    return m.group(1) if m else ""


def body_words(md):
    md = re.sub(r"^> Nguồn:.*$", "", md, flags=re.M)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)|<!--.*?-->|<br>", " ", md, flags=re.S)
    return WORD.findall(unicodedata.normalize("NFC", md).lower())


def shingles(w, n=5):
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("new")
    ap.add_argument("--root", default="docs-input")
    ap.add_argument("--top", type=int, default=5)
    a = ap.parse_args()
    new = open(a.new, encoding="utf-8").read()
    src_line = re.search(r"^> Nguồn: \[`([^`]+)`", new, re.M)
    keys_new = [name_key(a.new), name_key(title(new))] + ([name_key(src_line.group(1))] if src_line else [])
    sh_new = shingles(body_words(new))
    res = []
    for p in glob.glob(os.path.join(a.root, "**/*.md"), recursive=True):
        rel = os.path.relpath(p, a.root)
        if (rel == "README.md" or rel.startswith("_") or "/." in "/" + rel
                or os.path.abspath(p) == os.path.abspath(a.new)):
            continue
        old = open(p, encoding="utf-8").read()
        keys_old = [name_key(p), name_key(title(old))]
        nm = max(difflib.SequenceMatcher(None, x, y).ratio() for x in keys_new for y in keys_old if x and y) \
            if any(keys_new) and any(keys_old) else 0
        sh_old = shingles(body_words(old))
        ct = len(sh_new & sh_old) / min(len(sh_new), len(sh_old)) if sh_new and sh_old else 0
        res.append((ct, nm, rel))
    res.sort(key=lambda x: (-(x[0] + 0.5 * x[1])))
    print("| Nội dung | Tên | Tài liệu cũ | Gợi ý |\n|---|---|---|---|")
    for ct, nm, rel in res[:a.top]:
        hint = "rất có thể là bản cũ" if ct >= 0.35 or (nm >= 0.75 and ct >= 0.10) else \
               "liên quan, kiểm tra" if ct >= 0.10 or nm >= 0.6 else "—"
        print(f"| {ct:.2f} | {nm:.2f} | `{rel}` | {hint} |")


if __name__ == "__main__":
    main()
