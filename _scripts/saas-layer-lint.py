#!/usr/bin/env python3
"""Gate nhãn tầng SaaS (rule .claude/rules/saas-layer.md).

Dùng: python3 _scripts/saas-layer-lint.py <file.md> [...] [--registry docs/_product/tenant-parameters.md]
Exit 1 khi có FAIL. WARN không chặn.
"""
import re, sys, pathlib

LAYER = re.compile(r"\[(Lõi|Cấu hình|Gói: [^\]]+|Riêng [^\]]+)\]")
PCODE = re.compile(r"\bP-[a-z0-9]+(?:-[a-z0-9]+)*\b")
# Dòng tính năng brainstorm: "- A1 [SOP+] ..." / "- B3b [SOP to-be] ..."
CAP_LINE = re.compile(r"^- [A-Z]\d+[a-z]? \[(SOP to-be|SOP\+|Mới)\]")
# Dòng bảng FR/BR (SRS, reverse-spec): "| FR-x-001 |"
REQ_ROW = re.compile(r"^\|\s*(FR|BR)-[a-z0-9-]+-\d{2,3}\s*\|")
# Con số chính sách: tiền, thời lượng, giờ trong ngày, tỷ lệ, ngày trong tháng
POLICY_NUM = re.compile(
    r"\d[\d.,]*\s*(₫|đ\b|đồng|triệu|nghìn|giờ|phút|ngày\b|tuần|tháng|%)"
    r"|\b\d{1,2}h\d{0,2}\b|\b\d+/\d+\b|ngày \d{1,2}\b")
DEFAULT_REG = "docs/_product/tenant-parameters.md"

def load_registry(path):
    p = pathlib.Path(path)
    if not p.exists():
        return None, []
    text = p.read_text(encoding="utf8")
    codes = set(re.findall(r"^\|\s*(P-[a-z0-9-]+)\s*\|", text, re.M))
    terms = []
    m = re.search(r"^tenant_terms:\s*\[(.*?)\]", text, re.M)
    if m:
        terms = [t.strip() for t in m.group(1).split(",") if t.strip()]
    return codes, terms

def strip_code(line):
    # bỏ chú thích giá trị khách đi sau mã P: "`P-x` (Delta: 5.000.000 ₫)" là cách ghi đúng
    line = re.sub(r"`?P-[a-z0-9-]+`?\s*\([^)]*\)", "", line)
    # bỏ phần trong backtick để không bắt số trong mã/đường dẫn
    return re.sub(r"`[^`]*`", "", line)

def lint(path, codes, terms):
    fails, warns, checked = [], [], 0
    in_fence = False
    for n, line in enumerate(pathlib.Path(path).read_text(encoding="utf8").splitlines(), 1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        is_target = CAP_LINE.match(line) or REQ_ROW.match(line)
        if is_target:
            checked += 1
            if not LAYER.search(line):
                fails.append((n, "thiếu nhãn tầng", line[:100]))
        for code in PCODE.findall(line):
            if codes is not None and code not in codes:
                fails.append((n, f"mã {code} không có trong bảng tham số", line[:100]))
        tags = [t for t in LAYER.findall(line)]
        if is_target and tags and all(t in ("Lõi", "Cấu hình") or t.startswith("Gói") for t in tags):
            body = strip_code(line)
            if POLICY_NUM.search(body) and not PCODE.search(line):
                warns.append((n, "có con số chính sách nhưng không qua mã P", line[:100]))
            hit = [t for t in terms if t in body]
            if hit and "Lõi" in tags:
                warns.append((n, f"dòng [Lõi] có tên riêng khách: {', '.join(hit)}", line[:100]))
    return checked, fails, warns

def main(argv):
    reg = DEFAULT_REG
    if "--registry" in argv:
        i = argv.index("--registry"); reg = argv[i + 1]; argv = argv[:i] + argv[i + 2:]
    files = [a for a in argv if not a.startswith("-")]
    if not files:
        print(__doc__); return 2
    codes, terms = load_registry(reg)
    if codes is None:
        print(f"⚠ Chưa có bảng tham số {reg} — bỏ qua kiểm mã P")
    total_fail = 0
    for f in files:
        checked, fails, warns = lint(f, codes, terms)
        print(f"\n== {f}")
        print(f"  Có nhãn tầng ......... {'FAIL' if any('nhãn' in x[1] for x in fails) else 'PASS'} ({checked} dòng quy tắc)")
        print(f"  Mã tham số ........... {'FAIL' if any('mã P-' in x[1] or 'không có trong' in x[1] for x in fails) else ('SKIPPED' if codes is None else 'PASS')}")
        print(f"  Số trần / tên riêng .. {len(warns)} cảnh báo")
        print(f"  Đúng tầng ............ chưa được máy kiểm — soi theo 3 câu hỏi (rule saas-layer Mục 3)")
        for n, msg, txt in fails:
            print(f"  FAIL {f}:{n} {msg} | {txt}")
        for n, msg, txt in warns:
            print(f"  WARN {f}:{n} {msg} | {txt}")
        total_fail += len(fails)
        if checked == 0:
            print("  ⚠ Không thấy dòng quy tắc nào (dòng tính năng brainstorm hoặc FR/BR) — kiểm định dạng file")
    return 1 if total_fail else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
