#!/usr/bin/env python3
"""Kiểm DS v2 đồng bộ giữa repo và Figma — chạy sau MỌI lần /figma-component ghi Figma (và trước khi bàn giao dev).

Repo (luôn chạy):
  R1 status frontmatter hợp lệ (draft · in-review · approved · shipped)
  R2 dòng meta "> … · Nháp · …" của md khớp status frontmatter
  R3 _work/{slug}/state.json khớp status (approved cần round = done; round done mà md còn draft → báo)
  R4 tên token ghi trong md (`color/text/secondary`, `space/inset-md`…) có thật trong tokens.json
Figma (khi có --figma <snapshot.json>, ảnh chụp từ _scripts/figma-ds-snapshot.js qua use_figma):
  F1 node Figma md trỏ tới (`Tên` (id)) còn trên Figma và đúng tên
  F2 nhãn trạng thái trên Figma (dòng đầu mô tả set "Trạng thái: …" + nhãn "Nhãn trạng thái" trong Section) khớp md
  F3 component set trên trang DS không md nào nhắc tới (bỏ qua tên bắt đầu "_" hoặc ".": phần riêng của set khác)
  F4 biến Figma khớp tokens.json: thiếu / thừa / khác giá trị theo mode (Primitives, Semantic, Platform, Component)

Nhãn trạng thái: draft = Nháp · in-review = Đang review · approved = Đã duyệt · shipped = Đã bàn giao.
md trong l1/ (dựng trước DEC-260) mang nhãn Figma "Bản cũ — chờ dựng lại" dù status là draft.

Dùng:
  python3 _scripts/ds-v2-sync-check.py                         # chỉ phần repo
  python3 _scripts/ds-v2-sync-check.py --figma .claude/state/figma/ds-v2-snapshot.json
  python3 _scripts/ds-v2-sync-check.py --status                # in bảng trạng thái từng component
  python3 _scripts/ds-v2-sync-check.py --merge <out.json> <part.json> …   # gộp các phần ảnh chụp
F4 so theo mã băm từng collection (ảnh chụp nhỏ); collection lệch → chụp chi tiết collection đó rồi so từng biến.
Exit 1 khi có FAIL; 0 khi qua (WARN không chặn); 2 khi lỗi đầu vào.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMP = ROOT / "design/v2/components"
WORK = COMP / "_work"
TOKENS = ROOT / "design/v2/tokens.json"
LABEL = {"draft": "Nháp", "in-review": "Đang review", "approved": "Đã duyệt", "shipped": "Đã bàn giao"}
LEGACY = "Bản cũ — chờ dựng lại"
TIERS = ("base", "application", "l1")


def die(msg):
    print(f"ds-v2-sync-check: {msg}", file=sys.stderr)
    sys.exit(2)


def front(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip()
    return out


def specs():
    out = []
    for tier in TIERS:
        for f in sorted((COMP / tier).glob("*.md")):
            t = f.read_text()
            fm = front(t)
            meta = " ".join(l for l in t.splitlines()[:40] if l.startswith(">"))
            refs = re.findall(r"`([^`\n]+)`\s*\(?(\d+:\d+)", t)
            out.append({"path": f.relative_to(ROOT).as_posix(), "slug": f.stem, "tier": tier, "text": t,
                        "status": fm.get("status"), "meta": meta, "refs": refs})
    return out


def figma_label(s):
    return LEGACY if s["tier"] == "l1" else LABEL.get(s["status"], s["status"])


# ---------- token ----------

def token_index():
    d = json.loads(TOKENS.read_text())
    c = d["collections"]
    names = set()
    for coll in ("Primitives", "Semantic", "Component", "Brand", "Brand Invlogis"):
        for kind, vals in c.get(coll, {}).items():
            if isinstance(vals, dict) and kind in ("color", "number"):
                names |= set(vals)
    names |= set(c["Platform"]["vars"])
    names |= set(d.get("effectStyles") or {}) | set(d.get("textStyles") or {})
    return d, names


def prefixes(names):
    return {n.split("/")[0] for n in names}


# ---------- giá trị token theo mode (để so F4) ----------

def expected_vars(d):
    """[(collection Figma, tên, {mode: giá trị})] theo tokens.json."""
    c = d["collections"]
    fig = d.get("figma", {}).get("collections", {})
    prim_c, prim_n = c["Primitives"]["color"], c["Primitives"]["number"]

    def col(ref, mode, depth=0):
        if depth > 8 or ref is None:
            return None
        if isinstance(ref, dict):
            return col(ref.get(mode, ref.get("Value", ref.get("Light"))), mode, depth + 1)
        ref = str(ref)
        if ref.startswith("#"):
            return ref.upper()
        for coll in (prim_c, c["Semantic"]["color"], c["Component"]["color"]):
            if ref in coll:
                return col(coll[ref], mode, depth + 1)
        return None

    def num(ref):
        return prim_n.get(ref, ref) if isinstance(ref, str) else ref

    out = []
    for n, v in prim_c.items():
        out.append((fig.get("Primitives", "Primitives"), n, {"*": col(v, "Light")}))
    for n, v in prim_n.items():
        out.append((fig.get("Primitives", "Primitives"), n, {"*": v}))
    for coll in ("Semantic", "Component"):
        for n, v in c[coll]["color"].items():
            out.append((fig.get(coll, coll), n, {"Light": col(v, "Light"), "Dark": col(v, "Dark")}))
    plat = fig.get("Platform", {})
    for n, v in c["Platform"]["vars"].items():
        cname = next((k for k, pres in plat.items() if any(n.startswith(p) for p in pres)), "Platform") \
            if isinstance(plat, dict) else plat
        out.append((cname, n, {"Web": num(v.get("Web")), "Mobile": num(v.get("Mobile"))}))
    return out


def _norm(x):
    if x is None:
        return "null"
    if isinstance(x, (int, float)) and not isinstance(x, bool):
        r = round(x * 100) / 100
        return str(int(r)) if r == int(r) else repr(r)
    t = str(x).upper()
    return t + "FF" if t.startswith("#") and len(t) == 7 else t


def _b36(n):
    a, o = "0123456789abcdefghijklmnopqrstuvwxyz", ""
    while True:
        o, n = a[n % 36] + o, n // 36
        if not n:
            return o


def var_hash(rows, modes):
    """Cùng cách băm với figma-ds-snapshot.js (djb2 xor, base36) trên các dòng `tên=giá trị` đã sắp."""
    lines = []
    for n, mo in rows:
        if len(modes) == 1:
            lines.append(n + "=" + _norm(mo.get("*", mo.get("Light", mo.get("Web", mo.get("Value"))))))
        else:
            lines.append(n + "=" + ",".join(f"{k}:{_norm(mo.get(k, mo.get('*')))}" for k in sorted(modes)))
    a = 5381
    for ch in "\n".join(sorted(lines)):
        a = (((a * 33) & 0xFFFFFFFF) ^ ord(ch)) & 0xFFFFFFFF
    return _b36(a)


def same(a, b):
    if a is None or b is None:
        return a == b
    if isinstance(a, str) or isinstance(b, str):
        A, B = str(a).upper(), str(b).upper()
        if A.startswith("#") and B.startswith("#"):
            A = A if len(A) == 9 else A[:7] + ("FF" if len(A) == 7 else "")
            B = B if len(B) == 9 else B[:7] + ("FF" if len(B) == 7 else "")
        return A == B
    return abs(float(a) - float(b)) < 0.01


# ---------- main ----------

def main():
    args = sys.argv[1:]
    if args[:1] == ["--merge"]:  # gộp các phần ảnh chụp (1 phần biến + mỗi trang 1 phần)
        if len(args) < 3:
            die("--merge <out.json> <part.json> …")
        out = {"components": [], "sections": [], "variables": [], "pages": [], "varhash": {}}
        for f in args[2:]:
            part = json.loads(Path(f).read_text())
            for k in ("fileKey", "taken"):
                if part.get(k):
                    out[k] = part[k]
            for k in ("components", "sections", "variables", "pages"):
                out[k] += part.get(k) or []
            out["varhash"].update(part.get("varhash") or {})
        Path(args[1]).parent.mkdir(parents=True, exist_ok=True)
        Path(args[1]).write_text(json.dumps(out, ensure_ascii=False, indent=1))
        print(f"Đã gộp {len(args) - 2} phần → {args[1]}: {len(out['variables'])} biến · "
              f"{len(out['components'])} component · {len(out['sections'])} Section")
        sys.exit(0)
    snap = None
    if "--figma" in args:
        i = args.index("--figma")
        if i + 1 >= len(args):
            die("thiếu đường dẫn sau --figma")
        p = Path(args[i + 1])
        if not p.exists():
            die(f"không thấy {p}")
        snap = json.loads(p.read_text())
    d, tnames = token_index()
    tpre = prefixes(tnames) - {"color"} | {"color"}
    S = specs()
    fails, warns = [], []

    def F(code, msg):
        fails.append(f"{code} {msg}")

    def W(code, msg):
        warns.append(f"{code} {msg}")

    for s in S:
        st = s["status"]
        if st not in LABEL:
            F("R1", f"{s['path']}: status `{st}` không hợp lệ")
            continue
        labels_in_meta = [lb for lb in LABEL.values() if f"· {lb}" in s["meta"] or f"{lb} ·" in s["meta"]]
        if labels_in_meta and LABEL[st] not in labels_in_meta:
            F("R2", f"{s['path']}: dòng meta ghi `{labels_in_meta[0]}` nhưng status = {st} ({LABEL[st]})")
        stf = WORK / s["slug"] / "state.json"
        if stf.exists():
            rnd = json.loads(stf.read_text()).get("round")
            if st in ("approved", "shipped") and rnd != "done":
                F("R3", f"{s['path']}: status {st} nhưng _work/{s['slug']} đang ở vòng `{rnd}`")
            if rnd == "done" and st == "draft":
                W("R3", f"{s['path']}: _work/{s['slug']} đã xong vòng 5 mà md còn draft")
        body = re.sub(r"<!-- auto:begin.*?auto:end[^>]*-->", "", s["text"], flags=re.S)
        for tok in sorted(set(re.findall(r"`([a-z][a-z0-9-]*(?:/[a-z0-9.-]+)+)`", body))):
            if tok.split("/")[0] not in tpre or tok in tnames:
                continue
            if tok.startswith("icon/") and tok.split("/")[1] not in ("size",):
                continue  # tên icon Lucide (icons.md), không phải token
            if "color/" + tok in tnames:
                W("R4", f"{s['path']}: `{tok}` viết thiếu tiền tố — token là `color/{tok}`")
                continue
            F("R4", f"{s['path']}: token `{tok}` không có trong tokens.json")

    if snap:
        comps = {c["id"]: c for c in snap.get("components") or []}
        secs = {x["id"]: x for x in snap.get("sections") or []}
        referenced = set()
        for s in S:
            want = figma_label(s)
            own = []
            for name, nid in s["refs"]:
                referenced.add(nid)
                if nid in comps:
                    c = comps[nid]
                    if c["name"] != name and not c["name"].endswith(name):
                        F("F1", f"{s['path']}: `{name}` ({nid}) trên Figma tên `{c['name']}`")
                    own.append(c)
                elif nid in secs:
                    pass
                elif re.match(r"^[A-Z_.][\w .·/-]*$", name) and "Section" not in name:
                    W("F1", f"{s['path']}: không thấy `{name}` ({nid}) trong component/Section trên trang DS")
            if not own:
                W("F2", f"{s['path']}: md không trỏ tới component set nào có trên Figma — chưa kiểm được nhãn")
            for c in own[:1] + [x for x in own[1:] if x["section"] == own[0]["section"]]:
                if c["status"] != want:
                    F("F2", f"{s['path']}: `{c['name']}` mô tả ghi trạng thái `{c['status'] or '—'}`, cần `{want}`")
            sec_ids = {c["section"] for c in own if c["section"]}
            for sid in sec_ids:
                b = secs.get(sid, {}).get("badge")
                if b != want:
                    F("F2", f"{s['path']}: Section `{secs.get(sid, {}).get('name', sid)}` nhãn `{b or '—'}`, cần `{want}`")
        for c in comps.values():
            if c["type"] == "COMPONENT_SET" and c["id"] not in referenced and not c["name"].startswith(("_", ".")):
                W("F3", f"`{c['name']}` ({c['id']}, {c['page']}) không md nào nhắc tới")

        fv = {}
        for v in snap.get("variables") or []:
            fv[(v["collection"], v["name"])] = v
        exp = expected_vars(d)
        exp_keys = {(c, n) for c, n, _ in exp}
        detail = {c for c, _ in fv}
        vh = snap.get("varhash") or {}
        for cname in sorted({c for c, _, _ in exp} - detail):
            rows = [(n, mo) for c, n, mo in exp if c == cname]
            got = vh.get(cname)
            if not got:
                F("F4", f"collection `{cname}` không có trên Figma ({len(rows)} biến)")
            elif got["n"] != len(rows) or got["h"] != var_hash(rows, got["modes"]):
                F("F4", f"collection `{cname}` lệch (Figma {got['n']} biến, tokens.json {len(rows)}) — chụp chi tiết: "
                        f"figma-ds-snapshot.js với COLLECTION='{cname}', gộp lại rồi chạy lại")
        for cname, n, modes in exp:
            if cname not in detail:
                continue
            v = fv.get((cname, n))
            if not v:
                alt = [k for k in fv if k[1] == n]
                F("F4", f"biến `{n}` thiếu trong collection `{cname}`" + (f" (đang ở `{alt[0][0]}`)" if alt else ""))
                continue
            for m, val in modes.items():
                got = list(v["modes"].values()) if m == "*" else [v["modes"].get(m)]
                for g in got:
                    if val is not None and not same(val, g):
                        F("F4", f"`{n}` ({cname}{'' if m == '*' else ' · ' + m}): Figma {g} ≠ tokens.json {val}")
                        break
        known = {c for c, _, _ in exp}
        for (cname, n) in fv:
            if cname in known and (cname, n) not in exp_keys:
                W("F4", f"biến `{n}` có trên Figma (`{cname}`) nhưng không có trong tokens.json")

    if "--status" in args:
        print("| Component | Tầng | Trạng thái md | Nhãn Figma cần | Vòng _work |")
        print("|---|---|---|---|---|")
        for s in S:
            stf = WORK / s["slug"] / "state.json"
            rnd = json.loads(stf.read_text()).get("round") if stf.exists() else "—"
            print(f"| {s['slug']} | {s['tier']} | {s['status']} | {figma_label(s)} | {rnd} |")
        print()

    print(f"DS v2 sync — {len(S)} spec md" + (f" · Figma {snap.get('fileKey')} chụp {snap.get('taken')}" if snap else
                                                " · chưa có ảnh chụp Figma (chỉ kiểm repo)"))
    for code in ("R1", "R2", "R3", "R4", "F1", "F2", "F3", "F4"):
        f = [x for x in fails if x.startswith(code + " ")]
        w = [x for x in warns if x.startswith(code + " ")]
        if f or w:
            print(f"\n{code}: FAIL {len(f)} · WARN {len(w)}")
            for x in (f + w)[:40]:
                print(f"  {'✕' if x in f else '!'} {x[len(code) + 1:]}")
            if len(f + w) > 40:
                print(f"  … còn {len(f + w) - 40}")
    print(f"\nTổng: FAIL {len(fails)} · WARN {len(warns)}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
