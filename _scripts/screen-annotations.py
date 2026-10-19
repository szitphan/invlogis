#!/usr/bin/env python3
"""Thẻ Spec cạnh màn trên Figma: nội dung lấy từ bảng 5 cột + use case + user story + Jira, ghim theo từng dòng.

Vì sao: dev đọc màn trên Figma cần biết từng phần tử làm gì và màn thuộc use case, story, ticket nào mà không
phải mở tài liệu. Bảng 5 cột (`screens/{flow}.md`) là nguồn; thẻ Spec trên Figma là bản máy sinh, không sửa tay
(DEC-188). Quy ước: `.claude/rules/screen-source.md` › Thẻ Spec trên Figma.

  python3 _scripts/screen-annotations.py build <feature> <flow-slug>            # tóm tắt nội dung từng thẻ
  python3 _scripts/screen-annotations.py build <feature> <flow-slug> --json     # JSON cho bước vẽ
  python3 _scripts/screen-annotations.py match <feature> <flow-slug> <tree.json>          # ghép dòng ↔ phần tử
  python3 _scripts/screen-annotations.py match <feature> <flow-slug> <tree.json> --write  # ghi vào mốc Figma
  python3 _scripts/screen-annotations.py mark <feature> "<screenId>[ · <State>]" <n> --absent "<lý do>"
  python3 _scripts/screen-annotations.py mark <feature> "<screenId>[ · <State>]" <n> --node <nodeId>

Ba trạng thái của một row trên thẻ Spec: đã ghim (có nodeId) · chưa ghim (máy chưa ghép được — phải xử lý trước khi
chốt flow) · không có trên màn (BA xác nhận phần tử có điều kiện, không xuất hiện ở màn mẫu: `mark --absent`, mốc ghi
`absent: "<lý do>"`). `mark --node` ghim tay khi không đổi tên layer được (mốc ghi `manual: true`, match không ghi đè).

tree.json: {"<nodeId frame>": [{id, name, txt?, x, y, w, h, d}, …]} — các lớp con của từng frame theo thứ tự lớp
(cha trước con, anh em từ dưới lên trên; toạ độ trong frame, d = độ sâu), đọc từ Figma. Hai lớp cùng điểm → lấy lớp
nằm trên cùng. match chỉ đề xuất: dòng không ghép được → `null`, báo để đổi tên layer cho khớp
cột Items (đúng luật đặt tên layer theo việc nó làm của /figma-screen) rồi chạy lại.

Exit: 0 xong · 1 còn dòng chưa ghép được (match) · 2 thiếu dữ liệu.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_SCORE = 60
GENERIC_CONTROL = {"label", "button", "text", "icon", "link", "image"}   # tên lớp chung chung bên trong component
DECOR = re.compile(r"^(scrim|overlay|backdrop|mờ|khe|chấm)\b")          # lớp nền phủ / trang trí, không phải phần tử
REQ_RE = re.compile(r"\b((?:FR|NFR|BR|E)-[a-z0-9]+(?:-[a-z0-9]+)*?)-(\d{3})((?:\s*,\s*-\d{3})*)")
SHARED_RE = re.compile(r"\b(CMP-\d{2}|GR-\d{2})\b")
SID_RE = re.compile(r"(\d+\.\d+) · (web|mob)")


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def clean(s):
    return re.sub(r"\*\*|`", "", s).strip()


def node_id(url):
    m = re.search(r"node-id=(\d+)-(\d+)", url or "")
    return f"{m.group(1)}:{m.group(2)}" if m else None


def parse_screens(text):
    """screens/{flow}.md → tên flow + danh sách khối (màn chính và trạng thái), mỗi khối có bảng 5 cột."""
    flow_name = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), "")
    blocks, cur = [], None
    for line in text.splitlines():
        m = re.match(r"^## Screen:\s*(\S+)\s+—\s+(.+)$", line)
        s = re.match(r"^### Trạng thái:\s*(.+?)\s+—\s+(.+)$", line)
        if m:
            cur = {"slug": m.group(1), "name": m.group(2).strip(), "state": None, "items": []}
            blocks.append(cur)
            main = cur
            continue
        if s and blocks:
            cur = {"slug": main["slug"], "name": s.group(2).strip(), "state": s.group(1).strip(), "items": [],
                   "screenId": main.get("screenId"), "parent": main}
            blocks.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("- **screenId:**"):
            cur["screenId"] = line.split(":**", 1)[1].strip()
        elif line.startswith("- **Figma:**"):
            u = re.search(r"\((https?://[^)]+)\)", line)
            cur["nodeId"] = node_id(u.group(1) if u else "")
        elif line.startswith("- **Mô tả:**"):
            cur["desc"] = line.split(":**", 1)[1].strip()
        elif re.match(r"^\|\s*\d+\s*\|", line):
            c = split_row(line)
            if len(c) >= 5:
                bullets = [clean(b).lstrip("•").strip() for b in re.split(r"<br\s*/?>", c[4]) if clean(b).strip("• ")]
                cur["items"].append({"n": int(c[0]), "items": clean(c[1]), "control": clean(c[2]),
                                     "data": clean(c[3]), "bullets": bullets, "raw": c[4]})
    for b in blocks:
        b.pop("parent", None)
    return flow_name, blocks


def codes(text):
    req, err = [], []
    for m in REQ_RE.finditer(text):
        prefix, first, more = m.group(1), m.group(2), m.group(3)
        for num in [first] + re.findall(r"-(\d{3})", more):
            cid = f"{prefix}-{num}"
            (err if cid.startswith("E-") else req).append(cid)
    shared = SHARED_RE.findall(text)
    uniq = lambda xs: list(dict.fromkeys(xs))
    return {"req": uniq(req), "err": uniq(err), "shared": uniq(shared)}


def table_rows(text, start_re):
    lines = text.splitlines()
    i = next((k for k, l in enumerate(lines) if re.search(start_re, l)), None)
    if i is None:
        return []
    while i < len(lines) and not lines[i].lstrip().startswith("|"):
        i += 1
    head, rows = None, []
    for l in lines[i:]:
        if not l.lstrip().startswith("|"):
            break
        c = split_row(l)
        if head is None:
            head = c
        elif set("".join(c)) <= set("-: "):
            continue
        else:
            rows.append(dict(zip(head, c)))
    return rows


def screen_nums(cell):
    nums = set()
    for a, b, c, d in re.findall(r"\[(\d+)\.(\d+)\]\s*[–-]\s*\[(\d+)\.(\d+)\]", cell):
        if a == c:
            nums |= {f"{a}.{k}" for k in range(int(b), int(d) + 1)}
    nums |= set(re.findall(r"\[(\d+\.\d+)\]", cell))
    return nums


def use_cases(feature):
    d = ROOT / f"docs/{feature}/usecases"
    out = []
    for r in table_rows(read(d / f"{feature}-usecase-index.md"), r"^\| # \| Slug"):
        m = re.search(r"\[(uc-[a-z0-9-]+)\]", r.get("Slug", ""))
        if not m:
            continue
        slug = m.group(1)
        title = next((l.split(":", 1)[1].strip() for l in read(d / f"{slug}.md").splitlines()
                      if l.startswith("# Use Case:")), "")
        out.append({"id": "UC-" + slug[3:], "name": title, "nums": screen_nums(r.get("Screens", ""))})
    return out


def user_stories(feature):
    out = []
    for p in sorted((ROOT / f"docs/{feature}/userstories").glob("us-*.md")):
        t = read(p)
        sec = re.search(r"^## UI / Screen References.*?$(.*?)(?=^## )", t, re.S | re.M)
        body = sec.group(1) if sec else ""
        nums = {m.group(1) for m in SID_RE.finditer(body)} | set(re.findall(r"\[(\d+\.\d+)\]", body))
        title = next((l[2:].strip() for l in t.splitlines() if l.startswith("# ")), "")
        out.append({"id": "US-" + p.stem.split("-")[1], "title": title, "path": str(p.relative_to(ROOT)), "nums": nums})
    return out


def jira_map():
    """sync-state.yaml (rule atlassian-sync Mục 3) → {vault_path: (key, url)}; đọc theo dòng, không cần PyYAML."""
    t = read(ROOT / ".claude/state/atlassian/sync-state.yaml")
    out, vp, in_jira = {}, None, False
    for line in t.splitlines():
        m = re.match(r"^\s*-?\s*vault_path:\s*(\S+)", line)
        if m:
            vp, in_jira = m.group(1), False
            continue
        if re.match(r"^\s+jira:\s*$", line):
            in_jira = True
            continue
        if re.match(r"^\s+confluence:\s*$", line):
            in_jira = False
        if in_jira and vp:
            k = re.match(r"^\s+remote_id:\s*(\S+)", line)
            u = re.match(r"^\s+remote_url:\s*(\S+)", line)
            if k:
                out.setdefault(vp, {})["key"] = k.group(1)
            if u:
                out.setdefault(vp, {})["url"] = u.group(1)
    return out


def baseline(feature):
    p = ROOT / f".claude/state/figma/{feature}.json"
    return p, (json.loads(read(p)) if p.exists() else {})


def build(feature, flow):
    text = read(ROOT / f"docs/{feature}/screens/{flow}.md")
    if not text:
        return None, [f"thiếu docs/{feature}/screens/{flow}.md"]
    flow_name, blocks = parse_screens(text)
    ucs, uss, jira = use_cases(feature), user_stories(feature), jira_map()
    _, base = baseline(feature)
    problems, frames = [], []
    for b in blocks:
        sid = b.get("screenId", "")
        num = sid.split(" · ")[0] if sid else ""
        scr = base.get("screens", {}).get(sid, {})
        rows_map = (scr.get("frame_rows", {}).get(b["state"], {}) if b["state"] else scr.get("rows", {}))
        if not b.get("nodeId"):
            problems.append(f"{sid} {b['state'] or ''}: thiếu dòng **Figma:** có node-id — bỏ qua khối này")
            continue
        alltext = " ".join(i["raw"] for i in b["items"])
        us_here = [u for u in uss if num in u["nums"]]
        frames.append({
            "nodeId": b["nodeId"], "screenId": sid, "slug": b["slug"], "state": b["state"],
            "title": f"{sid} · {b['slug']}" + (f" · {b['state']}" if b["state"] else "") + f" — {b['name']}",
            "desc": b.get("desc", "") if not b["state"] else "",
            "uc": [{"id": u["id"], "name": u["name"]} for u in ucs if num in u["nums"]],
            "us": [dict({"id": u["id"], "title": u["title"]}, **({"jira": jira[u["path"]]} if u["path"] in jira else {}))
                   for u in us_here],
            "codes": codes(alltext),
            "items": [{"n": i["n"], "title": i["items"], "sub": f"{i['control']} · {i['data']}", "bullets": i["bullets"],
                       "target": (rows_map.get(str(i["n"])) or {}).get("nodeId"),
                       "also": (rows_map.get(str(i["n"])) or {}).get("also", []),
                       "absent": (rows_map.get(str(i["n"])) or {}).get("absent"),
                       "manual": bool((rows_map.get(str(i["n"])) or {}).get("manual"))} for i in b["items"]],
        })
    return {"feature": feature, "flow": flow, "flow_name": flow_name, "frames": frames}, problems


def norm(s):
    s = unicodedata.normalize("NFC", s or "").lower()
    s = re.sub(r"[›»\"“”'‘’().,:;!?·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def variants(items):
    noparen = re.sub(r"\(.*?\)", "", items).strip()
    quoted = re.findall(r"[“\"]([^”\"]+)[”\"]", items)
    alts = [a.strip() for a in re.split(r"\s+/\s+", noparen) if a.strip()]
    return list(dict.fromkeys([items, noparen] + quoted + alts)), alts if len(alts) > 1 else []


def score(node, vs, control):
    name, txt = norm(node.get("name")), norm(node.get("txt"))
    if DECOR.match(name):
        return 0
    best = 0
    for v in vs:
        nv = norm(v)
        if not nv:
            continue
        if name == nv:
            best = max(best, 100)
        elif txt and txt == nv:
            best = max(best, 90)
        elif len(nv) >= 4 and nv in name:
            best = max(best, 70)
        elif len(name) >= 4 and name in nv:
            best = max(best, 60)
        else:
            a, b = set(nv.split()), set(name.split())
            if a and b and len(a & b) / len(a | b) >= 0.5:
                best = max(best, 50)
    c = norm(control)
    if c and c == name and not txt and c not in GENERIC_CONTROL:   # khớp theo loại control: chỉ lớp khung, không lớp chữ
        best = max(best, 65)
    return best


def match(feature, flow, tree):
    plan, problems = build(feature, flow)
    if plan is None:
        return None, problems
    result = {}
    for fr in plan["frames"]:
        nodes = tree.get(fr["nodeId"], [])
        if not nodes:
            problems.append(f"{fr['title']}: tree.json không có lớp con của frame {fr['nodeId']}")
            continue
        rows = {}
        for it in fr["items"]:
            if it.get("manual") and it.get("target"):      # ghim tay (mark --node): giữ nguyên
                rows[str(it["n"])] = {"nodeId": it["target"], "text": it["title"], "score": 100, "manual": True}
                continue
            vs, alts = variants(it["title"])
            control = it["sub"].split(" · ")[0]
            # hoà điểm → lấy lớp nằm trên cùng (đứng sau trong thứ tự lớp): sheet, popup đè lên màn nền
            scored = sorted(((score(n, vs, control), k, n) for k, n in enumerate(nodes)), key=lambda t: (-t[0], -t[1]))
            top = scored[0][0] if scored else 0
            if top < MIN_SCORE:
                rows[str(it["n"])] = {"nodeId": None, "text": it["title"], "score": top}
                if it.get("absent"):
                    rows[str(it["n"])]["absent"] = it["absent"]
                continue
            if alts:   # "Thu hồi / Xoá" → mỗi vế một phần tử
                ids = []
                for a in alts:
                    s2 = sorted(((score(n, [a], ""), k, n) for k, n in enumerate(nodes)), key=lambda t: (-t[0], -t[1]))
                    if s2 and s2[0][0] >= MIN_SCORE:
                        ids.append(s2[0][2]["id"])
                rows[str(it["n"])] = {"nodeId": ids[0] if ids else None, "also": ids[1:], "text": it["title"], "score": top}
            else:
                rows[str(it["n"])] = {"nodeId": scored[0][2]["id"], "text": it["title"], "score": top,
                                      "layer": scored[0][2].get("name")}
        result[fr["nodeId"]] = {"title": fr["title"], "screenId": fr["screenId"], "state": fr["state"], "rows": rows}
    return result, problems


def write_baseline(feature, result):
    p, base = baseline(feature)
    if not base:
        return f"thiếu mốc {p.relative_to(ROOT)} — chạy /figma-sync trước"
    for fid, r in result.items():
        scr = base.setdefault("screens", {}).setdefault(r["screenId"], {})
        old = (scr.get("frame_rows", {}).get(r["state"], {}) if r["state"] else scr.get("rows", {}))
        clean_rows = {}
        for n, row in r["rows"].items():
            prev = old.get(n, {})
            if prev.get("manual"):                       # ghim tay: match không ghi đè
                clean_rows[n] = prev
                continue
            new = {k: v for k, v in row.items() if k in ("nodeId", "also", "text")}
            if not new["nodeId"] and prev.get("absent"):   # BA đã xác nhận không có trên màn
                new["absent"] = prev["absent"]
            clean_rows[n] = new
        if r["state"]:
            scr.setdefault("frame_rows", {})[r["state"]] = clean_rows
        else:
            scr["rows"] = clean_rows
        scr["level"] = "row"
    p.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return None


def opt(name):
    if name in sys.argv:
        k = sys.argv.index(name)
        return sys.argv[k + 1] if k + 1 < len(sys.argv) else None
    return None


def mark(feature, target, n):
    """Đặt tay trạng thái một row: --absent "<lý do>" (không có trên màn) hoặc --node <nodeId> (ghim tay)."""
    absent, node = opt("--absent"), opt("--node")
    if bool(absent) == bool(node):
        return "cần đúng một trong hai: --absent \"<lý do>\" hoặc --node <nodeId>"
    parts = [x.strip() for x in target.split(" · ")]
    if len(parts) < 2:
        return f"đích '{target}' phải dạng '<số> · <web|mob>[ · <State>]'"
    sid, state = " · ".join(parts[:2]), (" · ".join(parts[2:]) or None)
    p, base = baseline(feature)
    if not base:
        return f"thiếu mốc {p.relative_to(ROOT)} — chạy match --write trước"
    scr = base.setdefault("screens", {}).setdefault(sid, {})
    rows = scr.setdefault("frame_rows", {}).setdefault(state, {}) if state else scr.setdefault("rows", {})
    row = rows.get(str(n), {"text": ""})
    if absent:
        row = {"nodeId": None, "text": row.get("text", ""), "absent": absent}
    else:
        row = {"nodeId": node, "text": row.get("text", ""), "manual": True}
    rows[str(n)] = row
    scr["level"] = "row"
    p.write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{target} #{n}: " + (f"không có trên màn — {absent}" if absent else f"ghim tay vào {node}"))
    return None


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    for v in (opt("--absent"), opt("--node")):
        if v in a:
            a.remove(v)
    if len(a) >= 4 and a[0] == "mark":
        err = mark(a[1], a[2], a[3])
        if err:
            print("⚠ " + err)
            return 2
        return 0
    if len(a) < 3 or a[0] not in ("build", "match") or (a[0] == "match" and len(a) < 4):
        print(__doc__)
        return 2
    mode, feature, flow = a[:3]
    if mode == "build":
        plan, problems = build(feature, flow)
        if plan is None:
            print("\n".join("⚠ " + p for p in problems))
            return 2
        if "--json" in sys.argv:
            print(json.dumps({**plan, "problems": problems}, ensure_ascii=False, indent=1))
            return 0
        print(f"Thẻ Spec {feature} · {flow} ({plan['flow_name']}): {len(plan['frames'])} frame")
        for f in plan["frames"]:
            c = f["codes"]
            pinned = sum(1 for i in f["items"] if i["target"])
            print(f"- {f['title']} · {len(f['items'])} dòng ({pinned} đã ghim) · UC {', '.join(u['id'] for u in f['uc']) or '—'}"
                  f" · US {', '.join(u['id'] for u in f['us']) or '—'} · {len(c['req'])} yêu cầu, {len(c['err'])} lỗi, {len(c['shared'])} dùng chung")
        for p in problems:
            print("  ⚠ " + p)
        return 0
    tree = json.loads(Path(a[3]).read_text(encoding="utf-8"))
    result, problems = match(feature, flow, tree)
    if result is None:
        print("\n".join("⚠ " + p for p in problems))
        return 2
    miss = 0
    for fid, r in result.items():
        ok = sum(1 for row in r["rows"].values() if row["nodeId"])
        gone = sum(1 for row in r["rows"].values() if not row["nodeId"] and row.get("absent"))
        miss += len(r["rows"]) - ok - gone
        print(f"- {r['title']}: ghép {ok}/{len(r['rows'])}" + (f" · {gone} không có trên màn" if gone else ""))
        for n, row in r["rows"].items():
            if not row["nodeId"] and not row.get("absent"):
                print(f"    #{n} {row['text']}: chưa ghép được — đổi tên layer cho khớp cột Items, hoặc mark --absent / --node")
    for p in problems:
        print("  ⚠ " + p)
    if "--write" in sys.argv:
        err = write_baseline(feature, result)
        print("⚠ " + err if err else "Đã ghi bản đồ dòng ↔ phần tử vào mốc Figma.")
        if err:
            return 2
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
