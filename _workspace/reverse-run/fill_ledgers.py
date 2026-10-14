"""Điền sổ đối chiếu SRC-22/23: mục ⬜ → ➡ {feature} theo reverse-plan, hoặc ➖ + lý do cho phần loại ra.
Usage: python3 fill_ledgers.py <main_root> <plan.json> <out_dir>"""
import json, re, sys, collections
M, PLAN, OUT = sys.argv[1:4]
plan = json.load(open(PLAN, encoding="utf-8"))
web_map, mob_map = {}, {}
for f in plan["features"]:
    for p in f["parts"]:
        for a, b in p["web_pages"]:
            for x in range(a, b + 1):
                web_map.setdefault(x, f["slug"])        # trang dùng chung (lưu đồ danh mục) → feature đầu tiên
        for a, b in p["mobile_lines"]:
            for x in range(a, b + 1):
                mob_map.setdefault(x, f["slug"])
WEB_EX = [((10, 40), "trùng tài liệu Quy tắc giao diện chung web (SRC-20), đối chiếu ở sổ của tài liệu đó"),
          ((236, 246), "mục lục lặp lại bên trong SRS, không phải yêu cầu"), ((1, 9), "mục lục")]
MOB_EX = [((1, 702), "trùng tài liệu Quy tắc giao diện chung app (SRC-21), đối chiếu ở sổ của tài liệu đó")]
LIEN = "Liên quy trình — đã thay bằng `docs/cross-process-flow` (chỉ còn mục chưa đối chiếu riêng)"

def ex(n, table):
    return next((w for (a, b), w in table if a <= n <= b), None)

mob_src = open(f"{M}/docs-input/srs-cu/srs-mobile/srs-mobile.md", encoding="utf-8").read().split("\n")
def mob_line(title, start):
    t = title.strip()
    for i in range(start, len(mob_src)):
        if re.match(r"^#{1,6} ", mob_src[i]) and mob_src[i].lstrip("#").strip() == t:
            return i + 1
    return None

stats = {}
for name in ("lg-srs-export", "srs-mobile"):
    L = open(f"{M}/docs-input/_coverage/{name}.md", encoding="utf-8").read().split("\n")
    out, cnt, cursor, last_line, samples = [], collections.Counter(), 0, None, []
    for l in L:
        if not l.startswith("| ") or l.startswith("| Mục |"):
            out.append(l); continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        while len(c) < 4: c.append("")
        if c[1] and c[1] != "⬜":
            cnt["giữ nguyên " + c[1][:2]] += 1; out.append(l)
            if name == "srs-mobile":
                ln = mob_line(c[0], cursor)
                if ln: cursor, last_line = ln, ln
            continue
        new = None
        if name == "lg-srs-export":
            m = re.search(r"tr\. ?(\d+)", c[3]); n = int(m.group(1)) if m else None
            if n is None: cnt["không có trang"] += 1
            elif ex(n, WEB_EX): new = ("➖", "", (c[3] + " · " if c[3] else "") + ex(n, WEB_EX))
            elif 46 <= n <= 70: new = ("➖", "", (c[3] + " · ") + LIEN)
            elif n in web_map: new = (f"➡ {web_map[n]}", "", c[3])
            else: cnt["trang không thuộc feature"] += 1
        else:
            ln = mob_line(c[0], cursor) or last_line
            if ln: cursor, last_line = ln, ln
            if ln is None: cnt["không định vị được"] += 1
            elif ex(ln, MOB_EX): new = ("➖", "", (c[3] + " · " if c[3] else "") + ex(ln, MOB_EX))
            elif 861 <= ln <= 940: new = ("➖", "", (c[3] + " · " if c[3] else "") + LIEN)
            elif ln in mob_map: new = (f"➡ {mob_map[ln]}", "", c[3])
            else: cnt["dòng không thuộc feature"] += 1
        if new:
            cnt[new[0].split(" ")[0]] += 1
            row = f"| {c[0]} | {new[0]} | {new[1]} | {new[2]} |"
            if len(samples) < 400: samples.append((l, row))
            out.append(row)
        else:
            out.append(l)
    open(f"{OUT}/{name}.md", "w", encoding="utf-8").write("\n".join(out))
    stats[name] = cnt
    json.dump(samples, open(f"{OUT}/{name}.samples.json", "w"), ensure_ascii=False)
for k, v in stats.items(): print(k, dict(v))
