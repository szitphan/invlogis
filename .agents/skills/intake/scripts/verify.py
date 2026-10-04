#!/usr/bin/env python3
"""Kiểm bản .md có ĐỦ nội dung so với chữ trích thô từ file gốc không.

Dùng:  python3 verify.py <thư mục staging>          (đọc _raw.txt + {slug}.md trong thư mục)
       python3 verify.py --raw <_raw.txt> --md <file.md>

Hai phép kiểm, tất định:
  1. Con số: mọi con số (tiền, ngày, mã, số lượng) trong bản gốc phải xuất hiện trong .md, đủ số lần.
  2. Dòng chữ: mỗi dòng gốc (≥3 từ) phải có ≥70% cụm 3 từ liên tiếp xuất hiện trong .md.
Thoát mã 0 = đủ; 1 = có chỗ thiếu (in danh sách để Claude bổ sung hoặc giải thích từng chỗ).

Chữ OCR (trang scan, ảnh) nằm riêng trong _raw_ocr.txt và chỉ được báo THAM KHẢO (không làm verify
fail): Claude đã sửa chữ theo ảnh nên khác OCR là bình thường. Dò mục đó để bắt dòng bị bỏ sót thật.
"""
import argparse, collections, glob, os, re, sys, unicodedata


def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)          # ảnh
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)        # link → chữ
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"[*_`#>|~\\]", " ", s)
    return s


WORD = re.compile(r"[^\W_]+", re.U)
NUM = re.compile(r"\d[\d.,:/\-]*\d|\d")


def nums(s):
    out = []
    for m in NUM.findall(s):
        out.append(re.sub(r"[.,](?=\d{3}\b)", "", m))  # 5.000.000 ≡ 5,000,000 ≡ 5000000
    return out


def grams(words, n=3):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir", nargs="?")
    ap.add_argument("--raw")
    ap.add_argument("--md")
    ap.add_argument("--threshold", type=float, default=0.7)
    a = ap.parse_args()
    if a.dir:
        raw_p = os.path.join(a.dir, "_raw.txt")
        mds = [p for p in glob.glob(os.path.join(a.dir, "*.md")) if not os.path.basename(p).startswith("_")]
        md_p = mds[0]
    else:
        raw_p, md_p = a.raw, a.md
    raw = open(raw_p, encoding="utf-8").read()
    md = open(md_p, encoding="utf-8").read()
    mdn = norm(md)
    md_words = WORD.findall(mdn)
    md_g = grams(md_words)
    md_set = set(md_words)

    # 1. con số
    need = collections.Counter(nums(norm(raw)))
    have = collections.Counter(nums(mdn))
    miss_num = {k: v - have[k] for k, v in need.items() if have[k] < v}

    # 2. dòng chữ
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    miss_lines, total, ok = [], 0, 0
    for l in lines:
        w = WORD.findall(norm(l))
        if len(w) < 3:
            if w and not all(x in md_set for x in w):
                miss_lines.append((0.0, l))
            continue
        total += 1
        g = grams(w)
        r = len(g & md_g) / len(g)
        if r >= a.threshold:
            ok += 1
        else:
            miss_lines.append((r, l))

    cov = ok / total * 100 if total else 100.0
    print(f"Độ phủ dòng chữ: {ok}/{total} dòng ({cov:.1f}%) · ngưỡng {a.threshold:.0%} cụm 3 từ")
    print(f"Con số: {sum(need.values()) - sum(miss_num.values())}/{sum(need.values())} có mặt")
    if miss_num:
        print("\n## Con số thiếu (số lần thiếu) — kèm dòng gốc chứa nó")
        for k, v in sorted(miss_num.items(), key=lambda x: -x[1])[:60]:
            ctx = next((l for l in lines if k in "".join(nums(norm(l))) or k in l), "")
            print(f"- {k} ×{v}  ← {ctx[:140]}")
    if miss_lines:
        print(f"\n## Dòng gốc chưa thấy trong .md ({len(miss_lines)})")
        for r, l in miss_lines[:120]:
            print(f"- [{r:.0%}] {l[:160]}")
        if len(miss_lines) > 120:
            print(f"- … còn {len(miss_lines) - 120} dòng")
    ocr_p = os.path.join(os.path.dirname(raw_p), "_raw_ocr.txt")
    if os.path.exists(ocr_p):
        ol = [l.strip() for l in open(ocr_p, encoding="utf-8").read().splitlines() if len(WORD.findall(norm(l))) >= 3]
        weak = [(len(grams(WORD.findall(norm(l))) & md_g) / max(1, len(grams(WORD.findall(norm(l))))), l) for l in ol]
        weak = [x for x in weak if x[0] < 0.34]
        print(f"\nChữ OCR (tham khảo, không tính fail): {len(ol) - len(weak)}/{len(ol)} dòng khớp ≥34%")
        if weak:
            print("## Dòng OCR ít khớp — xem ảnh: sửa lỗi OCR (bình thường) hay bỏ sót?")
            for r, l in weak[:40]:
                print(f"- [{r:.0%}] {l[:140]}")
    if not miss_num and not miss_lines:
        print("✅ Đủ nội dung.")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
