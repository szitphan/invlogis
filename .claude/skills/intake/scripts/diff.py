#!/usr/bin/env python3
"""So 2 phiên bản .md của cùng 1 tài liệu, theo từng mục (heading) — khung cho báo cáo thay đổi.

Dùng:  python3 diff.py <bản cũ.md> <bản mới.md> [--context 1]

In Markdown:
  - bảng tổng: mục thêm / bỏ / sửa / giữ nguyên
  - con số đổi giá trị (số có ở bản này mà không có ở bản kia, kèm dòng chứa)
  - từng mục bị sửa: các dòng bỏ (-) / thêm (+), bỏ qua dòng header "> Nguồn:" và khác biệt khoảng trắng
Claude dùng output này làm phần "Chi tiết" của báo cáo, rồi viết "Tóm tắt nghiệp vụ" lên đầu.
"""
import argparse, difflib, re, unicodedata

NUM = re.compile(r"\d[\d.,:/\-]*\d|\d")


def load(p):
    s = unicodedata.normalize("NFC", open(p, encoding="utf-8").read())
    s = re.sub(r"^> (Nguồn|Phiên bản|Lịch sử).*$", "", s, flags=re.M)
    return s


def sections(md):
    out, cur, buf = [], "(đầu tài liệu)", []
    for ln in md.splitlines():
        m = re.match(r"^(#{1,6}) (.+)$", ln)
        if m:
            out.append((cur, buf))
            cur, buf = m.group(2).strip(), []
        else:
            if ln.strip():
                buf.append(re.sub(r"\s+", " ", ln.strip()))
    out.append((cur, buf))
    return [(h, b) for h, b in out if b or h != "(đầu tài liệu)"]


def key(h):
    h = re.sub(r"^[\dIVXivx.\-)\s]+", "", h)   # bỏ số thứ tự mục để mục đổi số vẫn khớp
    return re.sub(r"[*_`]", "", h).strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("old")
    ap.add_argument("new")
    a = ap.parse_args()
    old_md, new_md = load(a.old), load(a.new)
    so, sn = sections(old_md), sections(new_md)
    ko = {key(h): (h, b) for h, b in so}
    kn = {key(h): (h, b) for h, b in sn}
    # ghép mục đổi tên nhẹ
    unmatched_new = [k for k in kn if k not in ko]
    for k in [k for k in ko if k not in kn]:
        m = difflib.get_close_matches(k, unmatched_new, n=1, cutoff=0.75)
        if m:
            kn[k] = kn.pop(m[0])
            unmatched_new.remove(m[0])
    added = [kn[k][0] for k in kn if k not in ko]
    removed = [ko[k][0] for k in ko if k not in kn]
    changed, same = [], 0
    for k in ko:
        if k in kn:
            if ko[k][1] != kn[k][1] or ko[k][0] != kn[k][0]:
                changed.append(k)
            else:
                same += 1

    print("## Tổng quan thay đổi\n")
    print("| Loại | Số mục | Mục |\n|---|---|---|")
    print(f"| Thêm mới | {len(added)} | {'; '.join(added) or '—'} |")
    print(f"| Bỏ | {len(removed)} | {'; '.join(removed) or '—'} |")
    print(f"| Sửa | {len(changed)} | {'; '.join(kn[k][0] for k in changed) or '—'} |")
    print(f"| Giữ nguyên | {same} | |")

    no = set(NUM.findall(old_md)) - set(NUM.findall(new_md))
    nn = set(NUM.findall(new_md)) - set(NUM.findall(old_md))
    if no or nn:
        print("\n## Con số thay đổi\n")
        print("| Chỉ có ở bản cũ | Chỉ có ở bản mới |\n|---|---|")
        lo, ln_ = sorted(no), sorted(nn)
        for i in range(max(len(lo), len(ln_))):
            print(f"| {lo[i] if i < len(lo) else ''} | {ln_[i] if i < len(ln_) else ''} |")

    if added:
        print("\n## Mục thêm mới\n")
        for k in kn:
            if k not in ko:
                h, b = kn[k]
                print(f"### {h}\n")
                print("\n".join(f"+ {x}" for x in b[:40]) + ("\n+ …" if len(b) > 40 else "") + "\n")
    if removed:
        print("\n## Mục bị bỏ\n")
        for k in ko:
            if k not in kn:
                h, b = ko[k]
                print(f"### {h}\n")
                print("\n".join(f"- {x}" for x in b[:40]) + ("\n- …" if len(b) > 40 else "") + "\n")
    if changed:
        print("\n## Mục bị sửa\n")
        for k in changed:
            (ho, bo), (hn, bn) = ko[k], kn[k]
            print(f"### {hn}" + (f" _(trước: {ho})_" if ho != hn else "") + "\n")
            print("```diff")
            for d in difflib.unified_diff(bo, bn, lineterm="", n=0):
                if d.startswith(("---", "+++", "@@")):
                    continue
                print(d)
            print("```\n")


if __name__ == "__main__":
    main()
