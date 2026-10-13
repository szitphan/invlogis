#!/usr/bin/env python3
"""Sổ đối chiếu nguồn — kiểm từng MỤC của tài liệu khách đã được xử lý chưa.

Mỗi nguồn trong docs-input/ có 1 sổ `docs-input/_coverage/{slug}.md`:

    # Sổ đối chiếu: {tên tài liệu} (SRC-xx)

    > Nguồn: `sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md`
    > Bản: 12/10/2026 (nhận 2026-10-12)

    | Mục | Kết quả | Ở đâu | Ghi chú |
    |---|---|---|---|
    | 2.2 Tạo JobID nghiệp vụ (AI01) | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7 | |
    | 2.2.1 Kiến trúc tích hợp Google Document AI | | | |
    | 3.1 Trích xuất mã QR để thanh toán | ➡ payables | | |

Kết quả (ký tự đầu ô): ✅ đã đưa vào · ➡ {feature} · ➖ ngoài phạm vi (Ghi chú bắt buộc ghi lý do) ·
⏳ chờ khách (OQ-n) · ⬜ chưa xử lý · 🔄 đổi ở bản mới, cần rà lại. Ô trống = theo mục cha (mục có số là
tiền tố, vd 2.2 của 2.2.1; mục không số theo dòng có kết quả gần nhất phía trên).

Dùng:
  source-coverage.py <feature>     mục còn mở của các nguồn feature trỏ tới + mục giao cho feature
  source-coverage.py --source SRC-07|<đường dẫn nguồn>   mục còn mở của 1 nguồn
  source-coverage.py --all         tổng quan mọi sổ
Exit 1 khi còn mục mở (⬜/🔄/➡ chưa tiếp nhận) hoặc sổ sai (✅ trỏ file không có, ➖ thiếu lý do).
"""
import glob, os, re, sys, unicodedata

ROOT = os.environ.get("INTAKE_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT = "docs-input"
COV_DIR = f"{INPUT}/_coverage"
MARKS = ("✅", "➡", "➖", "⏳", "⬜", "🔄")
OPEN = ("⬜", "🔄")
NUM = re.compile(r"^((?:\d+\.)*\d+|[IVX]+)\.?\s+(.*)$")
SCRATCH = re.compile(r"(^|/)zz-")

nfc = lambda s: unicodedata.normalize("NFC", s)


def rd(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return nfc(f.read())


def cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def norm_title(s):
    s = re.sub(r"[`*_]", "", nfc(s)).lower()
    s = re.sub(r"\(.*?\)", "", s)
    return re.sub(r"[^\w]+", " ", s).strip()


def split_num(muc):
    m = NUM.match(muc.strip())
    return (m.group(1), m.group(2)) if m else ("", muc.strip())


def mark_of(cell):
    cell = cell.strip()
    for m in MARKS:
        if cell.startswith(m):
            return m
    return ""


def target_of(cell):
    """➡ payables / ➡ feature khác: payables → payables."""
    m = re.match(r"➡\s*(?:feature khác:)?\s*`?([a-z0-9-]+)`?", cell.strip())
    return m.group(1) if m else ""


def load(path, txt=None):
    """Đọc 1 sổ → dict(path, source, version, title, rows[{muc, num, mark, eff, target, where, note, i}])."""
    txt = rd(path) if txt is None else txt
    src = re.search(r"^> Nguồn:\s*`([^`]+)`", txt, re.M)
    ver = re.search(r"^> Bản:.*?\(nhận (\d{4}-\d{2}-\d{2})\)", txt, re.M)
    title = re.search(r"^# (.*)$", txt, re.M)
    rows, lines = [], txt.split("\n")
    for i, ln in enumerate(lines):
        if not ln.startswith("|") or ln.startswith("| Mục |") or re.match(r"^\|\s*-", ln):
            continue
        c = cells(ln) + ["", "", "", ""]
        num, _ = split_num(c[0])
        rows.append(dict(muc=c[0], num=num, raw=c[1], mark=mark_of(c[1]), target=target_of(c[1]),
                         where=c[2], note=c[3], i=i))
    # kết quả hiệu lực: ô trống theo mục cha
    for k, r in enumerate(rows):
        if r["mark"]:
            r["eff"], r["eff_target"] = r["mark"], r["target"]
            continue
        parent = None
        if r["num"] and "." in r["num"]:
            for p in reversed(rows[:k]):
                if p["num"] and r["num"].startswith(p["num"] + ".") and p.get("eff"):
                    parent = p
                    break
        if not parent:
            parent = next((p for p in reversed(rows[:k]) if p.get("eff")), None)
        r["eff"] = parent["eff"] if parent else "⬜"
        r["eff_target"] = parent["eff_target"] if parent else ""
    return dict(path=path, source=src.group(1) if src else "", version=ver.group(1) if ver else "",
                title=title.group(1) if title else path, rows=rows, lines=lines)


def all_ledgers():
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, COV_DIR, "*.md"))):
        rel = nfc(os.path.relpath(f, ROOT))
        led = load(rel)
        if led["source"]:
            out[led["source"]] = led
    return out


def feature_exists(slug):
    return bool(slug) and os.path.isdir(os.path.join(ROOT, "docs", slug)) and not SCRATCH.search(slug)


def problems(led):
    """Dòng sai cách ghi: ✅ không trỏ được file có thật, ➖ thiếu lý do, ➡ thiếu tên feature."""
    out = []
    for r in led["rows"]:
        if r["mark"] == "✅":
            paths = re.findall(r"`([^`]+\.(?:md|html|puml|bpmn|svg))`", r["where"])
            if not paths:
                out.append((r, "✅ nhưng cột Ở đâu không có đường dẫn"))
            for p in paths:
                if not os.path.exists(os.path.join(ROOT, p)):
                    out.append((r, f"✅ trỏ file không có: {p}"))
        elif r["mark"] == "➖" and not r["note"]:
            out.append((r, "➖ thiếu lý do ở cột Ghi chú"))
        elif r["mark"] == "➡" and not r["target"]:
            out.append((r, "➡ thiếu tên feature"))
    return out


def summary(led):
    """(đã xử lý, tổng, còn mở, ➡ tới feature chưa có)."""
    rows = led["rows"]
    pending_feat = sorted({r["eff_target"] for r in rows if r["eff"] == "➡" and not feature_exists(r["eff_target"])})
    opened = [r for r in rows if r["eff"] in OPEN or (r["eff"] == "➡" and not feature_exists(r["eff_target"]))]
    return len(rows) - len(opened), len(rows), opened, pending_feat


def registered(skip_out=False):
    """Đường dẫn nguồn trong sổ nguồn; skip_out=True bỏ nguồn ➖ (không phải nguồn nghiệp vụ)."""
    reg = f"{INPUT}/README.md"
    if not os.path.exists(os.path.join(ROOT, reg)):
        return []
    rows = re.findall(r"^\| SRC-\d+ \| `([^`]+)` \|[^|]*\| ([^|]*)\|", rd(reg), re.M)
    return [p for p, feed in rows if not (skip_out and feed.strip().startswith("➖"))]


def sources_of_feature(feature):
    """Nguồn trong sổ nguồn mà doc của feature trỏ tới (bỏ link ảnh, link _changes)."""
    known, txt = registered(), ""
    for md in glob.glob(os.path.join(ROOT, "docs", feature, "**", "*.md"), recursive=True):
        txt += rd(os.path.relpath(md, ROOT))
    return {p for p in known if f"{INPUT}/{p}" in txt}


def show(led, rows, label):
    print(f"\n## {led['title']}  ({led['path']}, bản nhận {led['version'] or '?'})")
    print(f"   {label}")
    for r in rows:
        tag = r["eff"] + (f" {r['eff_target']}" if r["eff_target"] else "")
        own = "" if r["mark"] else " (theo mục cha)"
        print(f"   - {tag}{own}  {r['muc']}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    leds = all_ledgers()
    bad = 0
    if args[0] == "--all":
        for src, led in leds.items():
            done, total, opened, pend = summary(led)
            probs = problems(led)
            bad += len(opened) + len(probs)
            print(f"{'✅' if not opened and not probs else '🟡'} {done}/{total}  {src}"
                  + (f"  · ➡ feature chưa có: {', '.join(pend)}" if pend else "")
                  + (f"  · {len(probs)} dòng ghi sai" if probs else ""))
        missing = [p for p in registered(skip_out=True) if p not in leds]
        if missing:
            print(f"\nChưa có sổ: {len(missing)} nguồn — " + ", ".join(missing))
        sys.exit(1 if bad else 0)

    if args[0] == "--source":
        key = args[1] if len(args) > 1 else ""
        if key.startswith("SRC-"):
            reg = rd(f"{INPUT}/README.md")
            m = re.search(rf"^\| {re.escape(key)} \| `([^`]+)`", reg, re.M)
            key = m.group(1) if m else key
        key = key.replace(f"{INPUT}/", "")
        led = leds.get(key)
        if not led:
            print(f"Chưa có sổ đối chiếu cho {key} — lập `{COV_DIR}/{{slug}}.md` (rule source-coverage.md).")
            sys.exit(1)
        _, _, opened, _ = summary(led)
        probs = problems(led)
        if opened:
            show(led, opened, f"{len(opened)} mục còn mở")
        for r, why in probs:
            print(f"   ✗ {r['muc']}: {why}")
        if not opened and not probs:
            print(f"✅ {key}: mọi mục đã xử lý")
        sys.exit(1 if opened or probs else 0)

    feature = args[0]
    srcs = sources_of_feature(feature)
    active = set(registered(skip_out=True))
    no_ledger = sorted(s for s in srcs if s not in leds and s in active)
    for src, led in leds.items():
        _, _, opened, _ = summary(led)
        mine = [r for r in led["rows"] if r["eff"] == "➡" and r["eff_target"] == feature]
        rows = (opened if src in srcs else []) + mine
        probs = problems(led) if src in srcs else []
        if rows:
            bad += len(rows)
            n_open = len([r for r in rows if r["eff"] in OPEN])
            label = [f"{n_open} mục ⬜/🔄"] if n_open else []
            if len(rows) - n_open - len(mine):
                label.append(f"{len(rows) - n_open - len(mine)} mục ➡ feature chưa có thư mục")
            if mine:
                label.append(f"{len(mine)} mục giao cho {feature} (đưa vào rồi đổi ➡ thành ✅ + Ở đâu)")
            show(led, sorted(rows, key=lambda r: r["i"]), " · ".join(label))
        for r, why in probs:
            bad += 1
            print(f"   ✗ {r['muc']}: {why}")
    if no_ledger:
        bad += len(no_ledger)
        print(f"\n## Nguồn {feature} trỏ tới nhưng chưa có sổ đối chiếu")
        for s in no_ledger:
            print(f"   - {s}")
    if not bad:
        print(f"✅ {feature}: mọi mục nguồn đã xử lý ({len(srcs)} nguồn trỏ tới)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
