#!/usr/bin/env python3
"""Xếp khu màn của một Section flow thành ma trận màn × case (cột = màn, hàng = case).

Vì sao: khu màn trên Figma phải cho đọc được ngay frame nào thuộc luồng chính, frame nào là lỗi hay tình
huống biên, giống userflow. Case đã có sẵn ở userflow Mục 1 (màu node), nên việc xếp là việc máy: script
đọc userflow + danh sách frame của Section flow, tính cột, hàng, toạ độ từng frame, title cột, thanh hàng.
Quy ước: `design/setup-figma.md` › *Bố cục trong Section flow* (DEC-185).

  python3 _scripts/flow-matrix.py plan  <feature> <flow-slug> <frames.json>          # in bảng + JSON kế hoạch
  python3 _scripts/flow-matrix.py plan  <feature> <flow-slug> <frames.json> --json   # chỉ JSON (cho bước vẽ)
  python3 _scripts/flow-matrix.py check <feature> <flow-slug> <frames.json>          # exit 0 đúng chỗ · 1 lệch · 2 thiếu dữ liệu

frames.json: con trực tiếp của Section flow, mỗi phần tử {id, name, x, y, w, h, tag?} (toạ độ trong section;
lấy từ `get_metadata` của Section flow hoặc `figma_read get_page_model`).

Cách xếp:
  * Cột = màn có số (`[#]` userflow Mục 2), thứ tự theo cột "Màn hình gồm" của userflow Mục 3 (thứ tự đi),
    màn không có ở đó thì theo số. Bề rộng cột = frame rộng nhất của cột (ô Responsive tính 1440 + 100 + 393).
  * Hàng: Luồng chính · Đang tải · Lỗi · Tình huống biên · Responsive. Hàng trống cả flow thì bỏ.
    - Tên state Loading / `<Khối> loading` / Submitting → Đang tải.
    - Còn lại theo màu node của frame trong userflow Mục 1 (`class … happy|error|edge`); node tìm theo nhãn
      `[n]` (frame chính) hoặc `[n] · <State>` (frame state).
    - Không có node → cột Hàng của bảng từ vựng tên state trong `design/setup-figma.md`.
    - Đuôi `1440` / `393` → Responsive.
  * Trong một ô nhiều frame → xếp dọc cách 100px theo thứ tự node trong userflow; ô Responsive xếp ngang.
  * Frame `Ghi chú … · <nodeId>` đặt ngay dưới frame có nodeId đó, cách 100px. Riêng thẻ Spec
    `Ghi chú · Spec · <nodeId>` đặt bên phải frame đó, cách 40px, cùng mép trên (cột rộng thêm phần thẻ, ô cao bằng
    phần cao hơn giữa frame và thẻ); lớp ghim `Ghi chú · Ghim · <nodeId>` dời cùng frame (giữ nguyên độ lệch).
  * Title cột (text `Cột · <screenId>`) rộng bằng cột + khoảng trống tới cột kế, chừa 40px. Title xuống nhiều
    dòng (cột mobile hẹp) thì thanh hàng đầu lùi xuống, cách đáy title cao nhất 40px: chiều cao đo từ text đã
    có trên Figma, chưa có thì ước theo số ký tự — vẽ title trước, đọc lại, chạy plan lần nữa.
  * Kế hoạch có `id` của title, thanh hàng đã có (để dời, không tạo trùng) và `remove_titles` (title cũ
    `Group title ·`, title/thanh hàng không còn dùng) để xoá.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROWS = ["Luồng chính", "Đang tải", "Lỗi", "Tình huống biên", "Responsive"]
CLS_ROW = {"happy": "Luồng chính", "error": "Lỗi", "edge": "Tình huống biên"}
DOT = {"Luồng chính": "#28A745", "Đang tải": "#8C8C8C", "Lỗi": "#DC3545", "Tình huống biên": "#FFC107", "Responsive": "#8C8C8C"}
LOADING = re.compile(r"(^|\s)(loading|submitting)$", re.I)
NUM = re.compile(r"^\d+\.\d+$")

# Khoảng cách (px) — đồng bộ với bảng vị trí trong design/setup-figma.md
COL_GAP = 400          # mép phải userflow → cột đầu, cột → cột
TITLE_Y = 320          # title cột
BAR_Y = 472            # thanh hàng đầu tiên
BAR_H = 120
BAR_TO_FRAME = 80      # đáy thanh hàng → frame đầu của hàng
CELL_GAP = 100         # frame → frame trong một ô
ROW_GAP = 300          # đáy frame thấp nhất của hàng → thanh hàng kế
PAD = 200              # đệm phải, đệm dưới section
TITLE_GAP = 40         # title cột được tràn sang khoảng trống giữa hai cột, chừa 40px trước cột kế
TITLE_TO_BAR = 40      # title xuống nhiều dòng thì thanh hàng đầu lùi xuống, cách đáy title cao nhất 40px
TITLE_LINE = 68        # Inter 64, line height 67,2 — chỉ để ước khi title chưa có trên Figma
TITLE_CHAR = 0.58 * 64 # bề rộng trung bình một ký tự ở cỡ 64 — chỉ để ước
SPEC_GAP = 40          # mép phải frame → thẻ Spec


def read(p):
    return p.read_text(encoding="utf-8") if p.exists() else ""


def table_rows(text, start_re):
    """Bảng markdown đầu tiên sau dòng khớp start_re → list[dict theo header]."""
    lines = text.splitlines()
    i = next((k for k, l in enumerate(lines) if re.search(start_re, l)), None)
    if i is None:
        return []
    while i < len(lines) and not lines[i].lstrip().startswith("|"):
        i += 1
    rows, head = [], None
    for l in lines[i:]:
        if not l.lstrip().startswith("|"):
            break
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if head is None:
            head = cells
        elif set("".join(cells)) <= set("-: "):
            continue
        else:
            rows.append(dict(zip(head, cells)))
    return rows


def vocab_rows(setup_text):
    """Bảng từ vựng tên state (cột Tên, Hàng) → ({tên: hàng}, [(regex mẫu, hàng)]) cho tên có `<…>`."""
    exact, patterns = {}, []
    for r in table_rows(setup_text, r"Bảng từ vựng tên state"):
        row = r.get("Hàng", "").strip()
        if row not in ROWS:
            continue
        cell = r.get("Tên", "")
        m = re.search(r"`([^`]+)`", cell)
        name = (m.group(1) if m else cell).strip()
        if "<" in name:
            parts = re.split(r"<[^>]+>", name)
            patterns.append((re.compile("^" + ".+".join(re.escape(p) for p in parts) + "$", re.I), row))
        elif name:
            exact[name] = row
    return exact, patterns


def vocab_row(vocab, state):
    exact, patterns = vocab
    if state in exact:
        return exact[state]
    return next((row for rx, row in patterns if rx.match(state)), None)


def mermaid_block(text, flow):
    m = re.search(r"^### Flow:\s*" + re.escape(flow) + r"\s*$", text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    b = re.search(r"```mermaid\n(.*?)```", rest, re.S)
    return b.group(1) if b else ""


NODE_RE = re.compile(r'\b([A-Za-z_][\w]*)\s*(?:\(\[|\[\[|\[|\{|\(\()"((?:[^"\\]|\\.)*)"')


def userflow_nodes(block):
    nodes, order = {}, []
    for m in NODE_RE.finditer(block):
        nid, label = m.group(1), m.group(2).replace("<br/>", " ").replace("<br>", " ")
        if nid not in nodes:
            nodes[nid] = {"label": label, "cls": None}
            order.append(nid)
    for m in re.finditer(r"^\s*class\s+([\w,]+)\s+(\w+)", block, re.M):
        for nid in m.group(1).split(","):
            if nid in nodes:
                nodes[nid]["cls"] = m.group(2)
    return [dict(id=k, **nodes[k]) for k in order]


def parse_frame(name):
    parts = [p.strip() for p in name.split(" · ")]
    if len(parts) < 3 or not NUM.match(parts[0]) or parts[1] not in ("web", "mob"):
        return None
    return {"num": parts[0], "dev": parts[1], "slug": parts[2], "state": " · ".join(parts[3:]) or None}


def find_node(nodes, num, state):
    head = f"[{num}]"
    for i, n in enumerate(nodes):
        lab = n["label"].strip()
        if not lab.startswith(head):
            continue
        rest = lab[len(head):]
        if state is None and not rest.lstrip().startswith("·"):
            return i, n
        if state and rest.lstrip().startswith("·"):
            after = rest.lstrip()[1:].lstrip()
            if after == state or after.startswith(state + " "):
                return i, n
    return None, None


def flow_order(userflow_text, flow, screens):
    rows = table_rows(userflow_text, r"^## 3\. ")
    cell = ""
    for r in rows:
        if r.get("Flow-slug", "").strip("`") == flow:
            cell = next((v for k, v in r.items() if k.startswith("Màn")), "")
    slugs = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", cell)
    by_slug = {s["slug"]: s["num"] for s in screens.values()}
    seen = []
    for s in slugs:
        if s in by_slug and by_slug[s] not in seen:
            seen.append(by_slug[s])
    return seen


def plan(feature, flow, frames, setup_text=None, userflow_text=None):
    uf_path = ROOT / f"docs/{feature}/srs/{feature}-userflow.md"
    userflow_text = userflow_text if userflow_text is not None else read(uf_path)
    setup_text = setup_text if setup_text is not None else read(ROOT / "design/setup-figma.md")
    problems = []
    if not userflow_text:
        return None, [f"thiếu {uf_path.relative_to(ROOT)}"]
    vocab = vocab_rows(setup_text)
    if not vocab[0] and not vocab[1]:
        problems.append("design/setup-figma.md: bảng từ vựng tên state chưa có cột Hàng")
    nodes = userflow_nodes(mermaid_block(userflow_text, flow))
    if not nodes:
        problems.append(f"userflow Mục 1 không có khối mermaid cho flow {flow}")
    m2 = {r.get("[#]", ""): r for r in table_rows(userflow_text, r"^## 2\. ")}

    uflow = next((f for f in frames if f["name"].startswith("Userflow")), None)
    screens, notes, cells, leftovers, specs, pins = {}, [], {}, [], {}, {}
    for f in frames:
        name = f["name"]
        if name.startswith("Ghi chú · Spec · "):
            specs[name.rsplit(" · ", 1)[1].strip()] = f
            continue
        if name.startswith("Ghi chú · Ghim · "):      # lớp ghim là group, không phải frame
            pins[name.rsplit(" · ", 1)[1].strip()] = f
            continue
        if f.get("tag") not in (None, "frame", "FRAME", "instance", "INSTANCE"):
            continue
        if name.startswith("Userflow"):
            continue
        if name.startswith(("Ghi chú", "Note")):
            notes.append(f)
            continue
        p = parse_frame(name)
        if not p:
            leftovers.append(f)
            continue
        screens.setdefault(p["num"], {"num": p["num"], "dev": p["dev"], "slug": p["slug"]})
        state = p["state"]
        if state in ("1440", "393"):
            row, rank, why = "Responsive", (0 if state == "1440" else 1), "đuôi " + state
        elif state and LOADING.search(state):
            row, rank, why = "Đang tải", 0, "state đang tải"
        else:
            idx, node = find_node(nodes, p["num"], state)
            if node and node["cls"] in CLS_ROW:
                row, rank, why = CLS_ROW[node["cls"]], idx, f"userflow {node['id']} {node['cls']}"
            elif state and vocab_row(vocab, state):
                row, rank, why = vocab_row(vocab, state), 999, "bảng từ vựng"
            elif not state:
                row, rank, why = "Luồng chính", 999, "frame chính, không có node — mặc định"
                problems.append(f"{name}: không có node [{p['num']}] trong userflow — tạm xếp Luồng chính")
            else:
                row, rank, why = None, 999, "chưa xếp được"
                problems.append(f"{name}: state '{state}' không có node trong userflow và không có trong bảng từ vựng")
        cells.setdefault((p["num"], row), []).append({**f, "rank": rank, "why": why, "state": state})

    order = flow_order(userflow_text, flow, screens)
    nums = order + sorted([n for n in screens if n not in order], key=lambda s: tuple(int(x) for x in s.split(".")))
    rows_used = [r for r in ROWS if any(k[1] == r for k in cells)]

    # bề rộng cột (frame + thẻ Spec nếu có)
    def iw(i):
        s = specs.get(i["id"])
        return i["w"] + (SPEC_GAP + s["w"] if s else 0)

    def ih(i):
        s = specs.get(i["id"])
        return max(i["h"], s["h"]) if s else i["h"]

    widths = {}
    for n in nums:
        w = 0
        for (cn, r), items in cells.items():
            if cn != n:
                continue
            w = max(w, sum(iw(i) for i in items) + CELL_GAP * (len(items) - 1)) if r == "Responsive" else max([w] + [iw(i) for i in items])
        widths[n] = w
    x0 = (uflow["x"] + uflow["w"] + COL_GAP) if uflow else 200
    cols, x = [], x0
    for n in nums:
        s = screens[n]
        name_vi = m2.get(n, {}).get("Màn hình", "")
        cols.append({"num": n, "x": x, "w": widths[n],
                     "title": f"{n} · {s['dev']} · {s['slug']}" + (f" — {name_vi}" if name_vi else "")})
        x += widths[n] + COL_GAP
    right = cols[-1]["x"] + cols[-1]["w"] if cols else x0

    # title cột: đo thật nếu đã có text `Cột · <screenId>` trên Figma, chưa có thì ước theo số ký tự
    named = {f["name"]: f for f in frames}
    titles = []
    for i, c in enumerate(cols):
        s = screens[c["num"]]
        tname = f"Cột · {c['num']} · {s['dev']}"
        tw = c["w"] + (COL_GAP if i < len(cols) - 1 else PAD) - TITLE_GAP
        cur = named.get(tname)
        th = cur["h"] if cur else TITLE_LINE * max(1, -(-int(len(c["title"]) * TITLE_CHAR) // int(tw)))
        titles.append({"name": tname, "id": cur["id"] if cur else None, "text": c["title"], "x": c["x"],
                       "y": TITLE_Y, "w": tw, "h": th, "measured": bool(cur), "col": c["num"]})
    bar_y = max(BAR_Y, TITLE_Y + max([t["h"] for t in titles] + [0]) + TITLE_TO_BAR)

    placed, bars, y = [], [], bar_y
    note_by_target = {}
    for nt in notes:
        tid = nt["name"].split(" · ")[-1].strip()
        note_by_target.setdefault(tid, []).append(nt)
    for r in rows_used:
        bname = f"Hàng · {r}"
        bars.append({"name": bname, "id": named[bname]["id"] if bname in named else None, "row": r,
                     "x": x0, "y": y, "w": right - x0, "h": BAR_H, "dot": DOT[r]})
        top = y + BAR_H + BAR_TO_FRAME
        bottom = top
        for c in cols:
            items = sorted(cells.get((c["num"], r), []), key=lambda i: (i["rank"], i["name"]))
            cx, cy = c["x"], top
            for it in items:
                placed.append({"id": it["id"], "name": it["name"], "col": c["num"], "row": r, "x": cx, "y": cy,
                               "w": it["w"], "h": it["h"], "why": it["why"]})
                sp, pg = specs.pop(it["id"], None), pins.pop(it["id"], None)
                if sp:
                    placed.append({"id": sp["id"], "name": sp["name"], "col": c["num"], "row": r, "x": cx + it["w"] + SPEC_GAP,
                                   "y": cy, "w": sp["w"], "h": sp["h"], "why": "thẻ Spec của " + it["id"]})
                if pg:
                    placed.append({"id": pg["id"], "name": pg["name"], "col": c["num"], "row": r, "x": pg["x"] + cx - it["x"],
                                   "y": pg["y"] + cy - it["y"], "w": pg["w"], "h": pg["h"], "why": "lớp ghim của " + it["id"]})
                h_eff = max(it["h"], sp["h"]) if sp else it["h"]          # ô cao bằng phần cao hơn giữa frame và thẻ
                w_eff = it["w"] + (SPEC_GAP + sp["w"] if sp else 0)
                if r == "Responsive":
                    cx += w_eff + CELL_GAP
                    bottom = max(bottom, cy + h_eff)
                    continue
                cy += h_eff
                for nt in note_by_target.pop(it["id"], []):
                    placed.append({"id": nt["id"], "name": nt["name"], "col": c["num"], "row": r, "x": cx,
                                   "y": cy + CELL_GAP, "w": nt["w"], "h": nt["h"], "why": "ghi chú của " + it["id"]})
                    cy += CELL_GAP + nt["h"]
                bottom = max(bottom, cy)
                cy += CELL_GAP
        y = bottom + ROW_GAP
    for tid, f in list(specs.items()) + list(pins.items()):
        problems.append(f"{f['name']}: không tìm thấy frame {tid} — giữ nguyên chỗ")
    for tid, nts in note_by_target.items():
        for nt in nts:
            problems.append(f"{nt['name']}: không tìm thấy frame {tid} — giữ nguyên chỗ")
    for f in leftovers:
        if f.get("tag") in (None, "frame", "FRAME"):
            problems.append(f"{f['name']}: tên không theo luật Tên frame — giữ nguyên chỗ")

    old_titles = [f["id"] for f in frames if f.get("tag") in ("text", "TEXT") and f["name"].startswith("Group title")]
    keep = {t["name"] for t in titles} | {b["name"] for b in bars}
    old_titles += [f["id"] for f in frames if f["name"].startswith(("Cột · ", "Hàng · ")) and f["name"] not in keep]
    content_bottom = max([p["y"] + p["h"] for p in placed] + [uflow["y"] + uflow["h"] if uflow else 0])
    section = {"w": right + PAD, "h": content_bottom + PAD}
    return {"feature": feature, "flow": flow, "columns": cols, "rows": rows_used, "bars": bars,
            "titles": titles, "frames": placed, "remove_titles": old_titles, "section": section}, problems


def print_plan(pl, problems):
    print(f"Ma trận {pl['feature']} · {pl['flow']}: {len(pl['columns'])} cột × {len(pl['rows'])} hàng, "
          f"section {int(pl['section']['w'])}×{int(pl['section']['h'])}")
    head = "| Hàng | " + " | ".join(c["num"] for c in pl["columns"]) + " |"
    print(head)
    print("|" + "---|" * (len(pl["columns"]) + 1))
    for r in pl["rows"]:
        cells = []
        for c in pl["columns"]:
            items = [p for p in pl["frames"] if p["row"] == r and p["col"] == c["num"] and not p["name"].startswith(("Ghi chú", "Note"))]
            cells.append(" · ".join((p["name"].split(" · ")[3] if len(p["name"].split(" · ")) > 3 else "chính") for p in items) or "")
        print(f"| {r} | " + " | ".join(cells) + " |")
    for p in problems:
        print("  ⚠ " + p)


def check(pl, frames, tol=1.0):
    cur = {f["id"]: f for f in frames}
    off = []
    for p in pl["frames"]:
        f = cur.get(p["id"])
        if f and (abs(f["x"] - p["x"]) > tol or abs(f["y"] - p["y"]) > tol):
            off.append(f"{p['name']}: đang ({int(f['x'])}, {int(f['y'])}) · đúng ({int(p['x'])}, {int(p['y'])}) [{p['row']}]")
    for t in pl["titles"] + pl["bars"]:
        f = cur.get(t["id"]) if t["id"] else None
        if not f:
            off.append(f"{t['name']}: chưa có trên Figma")
        elif abs(f["x"] - t["x"]) > tol or abs(f["y"] - t["y"]) > tol:
            off.append(f"{t['name']}: đang ({int(f['x'])}, {int(f['y'])}) · đúng ({int(t['x'])}, {int(t['y'])})")
    for i in pl["remove_titles"]:
        off.append(f"{cur[i]['name'] if i in cur else i}: title cũ còn trên Figma, cần xoá")
    return off


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if len(a) != 4 or a[0] not in ("plan", "check"):
        print(__doc__)
        return 2
    mode, feature, flow, fpath = a
    frames = json.loads(Path(fpath).read_text(encoding="utf-8"))
    if isinstance(frames, dict):
        frames = frames.get(flow, {}).get("children", frames.get("children", []))
    pl, problems = plan(feature, flow, frames)
    if pl is None:
        print("\n".join("⚠ " + p for p in problems))
        return 2
    if mode == "plan":
        if "--json" in sys.argv:
            print(json.dumps({**pl, "problems": problems}, ensure_ascii=False, indent=1))
        else:
            print_plan(pl, problems)
        return 0
    off = check(pl, frames)
    print_plan(pl, problems)
    if off:
        print(f"Lệch chỗ {len(off)} frame:")
        print("\n".join("  " + o for o in off))
        return 1
    print("Đúng chỗ: mọi frame nằm đúng cột, đúng hàng.")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
