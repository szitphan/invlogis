#!/usr/bin/env python3
"""Bản trước khi sửa + hoàn lại theo từng góp ý — tab Góp ý của trang review /figma-component --html.

  # sau mỗi góp ý sửa xong (khuyên dùng: 1 góp ý = 1 lần ghi, để hoàn lại được riêng):
  python3 _scripts/ds-snap.py change <slug> <page-truoc-khi-sua.json> <commentId>
  # hoàn lại đúng phần góp ý đó đã sửa (người dùng bấm "Hoàn lại bản trước" trên trang):
  python3 _scripts/ds-snap.py revert <slug> <commentId> [--dry]
  # cách cũ — chụp cả lượt cho nhiều góp ý (chỉ xem bản trước, không hoàn lại riêng được):
  python3 _scripts/ds-snap.py <slug> <page-truoc-khi-sua.json> <snapId> "<nhãn>" <commentId>[,...]

`change` ghi page["cmtChanges"][id] = danh sách thay đổi mịn (từng luật CSS theo bộ chọn trong css/cssScreen, html từng
màn, từng dòng values) + chụp bản trước (snaps["c-<id>"], cmtSnap). `revert` đảo từng thay đổi: chỗ hiện tại còn đúng
bản sau thì trả về bản trước; chỗ đã bị sửa tiếp → xung đột, giữ nguyên và báo (Claude xử lý tay). Góp ý đã xoá thì không
hoàn lại.
"""
import json
import re
import sys
from pathlib import Path

WORK = Path("design/v2/components/_work")


def css_rules(css):
    """[(khoá, văn bản)] theo thứ tự — luật cấp ngoài cùng (cả khối @media) là một đơn vị; khoá = bộ chọn + #lần xuất hiện."""
    out, seen, i, s = [], {}, 0, css or ""
    while i < len(s):
        j = s.find("{", i)
        if j < 0:
            break
        d, k = 1, j + 1
        while k < len(s) and d:
            d += {"{": 1, "}": -1}.get(s[k], 0)
            k += 1
        head = re.sub(r"/\*.*?\*/", "", s[i:j], flags=re.S).strip()
        lead = s[i:j][:len(s[i:j]) - len(s[i:j].lstrip())]
        n = seen.get(head, 0); seen[head] = n + 1
        out.append((f"{head}#{n}", lead + s[i:k].lstrip()))
        i = k
    return out


def val_key(v):
    return "|".join(str(v.get(x) or "") for x in ("part", "prop", "platform", "size", "state", "theme"))


def units(page):
    u = {}
    for f in ("css", "cssScreen"):
        for k, t in css_rules(page.get(f)):
            u[(f, k)] = t
    for sc in page.get("screens") or []:
        u[("screens", sc["id"])] = sc.get("html")
    for v in page.get("values") or []:
        u[("values", val_key(v))] = json.dumps(v, ensure_ascii=False, sort_keys=True)
    return u


def diff(old, cur):
    a, b = units(old), units(cur)
    return [{"field": f, "key": k, "before": a.get((f, k)), "after": b.get((f, k))}
            for (f, k) in sorted(set(a) | set(b)) if a.get((f, k)) != b.get((f, k))]


def set_unit(page, field, key, text):
    if field in ("css", "cssScreen"):
        rules = css_rules(page.get(field))
        keys = [k for k, _ in rules]
        if key in keys:
            i = keys.index(key)
            if text is None:
                rules.pop(i)
            else:
                rules[i] = (key, text)
        elif text is not None:
            rules.append((key, "\n" + text.lstrip()))
        page[field] = "".join(t for _, t in rules)
    elif field == "screens":
        for sc in page.get("screens") or []:
            if sc["id"] == key and text is not None:
                sc["html"] = text
    elif field == "values":
        vals = page.get("values") or []
        idx = [i for i, v in enumerate(vals) if val_key(v) == key]
        if text is None:
            for i in reversed(idx):
                vals.pop(i)
        elif idx:
            vals[idx[0]] = json.loads(text)
        else:
            vals.append(json.loads(text))
        page["values"] = vals


def snap_round(cur, old, snap_id, label, ids):
    snap = {"label": label}
    for k in ("css", "cssScreen"):
        if old.get(k, "") != cur.get(k, ""):
            snap[k] = old.get(k, "")
    old_sc = {s["id"]: s["html"] for s in old.get("screens", [])}
    d = {s["id"]: old_sc[s["id"]] for s in cur.get("screens", []) if s["id"] in old_sc and old_sc[s["id"]] != s["html"]}
    if d:
        snap["screens"] = d
    for k0, s0 in (cur.get("snaps") or {}).items():  # trùng bản chụp có sẵn → chỉ lưu phần khác, nền = bản đó
        if k0 != snap_id and not s0.get("base") and s0.get("screens") == snap.get("screens"):
            snap = {"label": label, "base": k0, **{k: v for k, v in snap.items() if k in ("css", "cssScreen") and v != s0.get(k)}}
            break
    cur.setdefault("snaps", {})[snap_id] = snap
    for c in ids:
        cur.setdefault("cmtSnap", {})[c] = snap_id
    return snap, len(d)


def main():
    av = sys.argv[1:]
    if av and av[0] == "change":
        slug, before, cid = av[1:4]
        pj = WORK / slug / "page.json"
        cur, old = json.loads(pj.read_text()), json.loads(Path(before).read_text())
        ch = diff(old, cur)
        if not ch:
            sys.exit("không thấy thay đổi nào so với bản trước — đã sửa page.json chưa?")
        cur.setdefault("cmtChanges", {}).setdefault(cid, []).append({"changes": ch, "reverted": False})
        snap_round(cur, old, f"c-{cid}", "trước khi sửa góp ý này", [cid])
        pj.write_text(json.dumps(cur, ensure_ascii=False, indent=1))
        print(f"{cid}: {len(ch)} thay đổi — " + ", ".join(f"{c['field']}:{c['key'][:40]}" for c in ch[:8]) + (" …" if len(ch) > 8 else ""))
        return
    if av and av[0] == "revert":
        slug, cid = av[1:3]
        dry = "--dry" in av
        pj = WORK / slug / "page.json"
        cur = json.loads(pj.read_text())
        rounds = [r for r in (cur.get("cmtChanges") or {}).get(cid, []) if not r.get("reverted")]
        if not rounds:
            sys.exit(f"{cid}: không có thay đổi ghi theo góp ý này (lượt cũ chụp cả lượt) — hoàn lại tay theo bản trước")
        r = rounds[-1]
        now = units(cur)
        done, conflict = [], []
        for c in r["changes"]:
            if now.get((c["field"], c["key"])) == c["after"]:
                set_unit(cur, c["field"], c["key"], c["before"])
                done.append(c)
            else:
                conflict.append(c)
        if not dry:
            r["reverted"] = True
            r["conflicts"] = [f"{c['field']}:{c['key']}" for c in conflict]
            pj.write_text(json.dumps(cur, ensure_ascii=False, indent=1))
        print(json.dumps({"comment": cid, "reverted": len(done), "conflicts": [f"{c['field']}:{c['key']}" for c in conflict],
                          "dry": dry}, ensure_ascii=False, indent=1))
        sys.exit(1 if conflict else 0)
    slug, before, snap_id, label, ids = av[0:5]
    pj = WORK / slug / "page.json"
    cur, old = json.loads(pj.read_text()), json.loads(Path(before).read_text())
    snap, n = snap_round(cur, old, snap_id, label, [x.strip() for x in ids.split(",")])
    pj.write_text(json.dumps(cur, ensure_ascii=False, indent=1))
    print(f"snap {snap_id}: {', '.join(k for k in snap if k != 'label')} · {n} màn · {len(ids.split(','))} góp ý")


if __name__ == "__main__":
    main()
