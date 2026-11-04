#!/usr/bin/env python3
"""Trang tổng rà vòng 3 Base: gom check.json của `_work/*-r3` thành design-system/_review/base-round3.html."""
import base64
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "design-system/components/_work"
PAGES = [
    ("buttons", "Buttons", "1wixQRN8c2E82MPpE71P7B", "Đã chọn 21/21 ở vòng 3 ngày 03/11 (DEC-350), đang lên Figma"),
    ("input", "Input", "Gcs113jUv5yyBNcwDATwMW", "Chưa chọn ở vòng 1"),
    ("select", "Select", "8ycXiy95xh9K6s5ENxRwJP", "Đã chốt vòng 1 ngày 03/11, chờ duyệt preview vòng 2"),
    ("multiselect", "Multiselect", "8WqvmUroMKH47EQK5x98Ah", "Chưa chọn ở vòng 1"),
    ("tag", "Tag", "GyXxqzWvZxcbZNFykECwqp", "Chưa chọn ở vòng 1"),
    ("form-controls", "Form controls", "U48emkhw58kHTWihJvtjyd", "48 lựa chọn vòng 3 trong db"),
    ("badge-avatar", "Badge · Avatar", "DKYwhnuHNw6bu7eGVta99T", "Đã qua vòng 3, 29/10"),
    ("tooltip", "Tooltip", "7WSaeZiGKB6bF3yqYoGtsb", "Đã duyệt vòng 3 ngày 03/11 (DEC-353), khớp Figma"),
    ("alert-notification", "Alert · Notification", "GJo88HcRNTYG3Wtj1e7nwN", "Bản 4 ráp theo foundations đã duyệt, duyệt vòng 2 ngày 03/11"),
]
KINDS = [
    ("moved", "Foundation đổi số", "#B42318", "Số trên trang hoặc số đã duyệt khác foundation hiện tại."),
    ("renamed", "Token đổi tên", "#7A5AF8", "Token đã duyệt không còn, phải trỏ sang tên mới."),
    ("unbuilt", "Token đã duyệt chưa có", "#DC6803", "Đã chọn tạo token mới nhưng thang vẫn chưa có."),
    ("pending", "Đã duyệt, trang chưa áp", "#0BA5EC", "Lựa chọn vẫn đúng, chỉ là hình trên trang chưa theo."),
    ("exception", "Ngoại lệ đã duyệt", "#737373", "Đã đồng ý lệch luật, ghi lại để soát."),
    ("open", "Chưa từng quyết", "#0036B5", "Lệch foundation và chưa có lựa chọn nào."),
]
GROUPS = [("color", "Màu"), ("typo", "Chữ"), ("spacing", "Khoảng cách, cỡ"), ("radius", "Bo góc"), ("icon", "Icon"), ("effect", "Hiệu ứng"), ("grid", "Lưới, rộng")]
RULES = [
    ("Buttons", "control/padding-x-icon/*, control/label-inset", "Luật nút Web: phía icon lùi 2 so với phía chữ (DEC-344)"),
    ("Tag", "chip/padding-x-sm · md · lg", "Tag đang ghi số riêng, chưa gắn token lề (padding.md)"),
    ("Badge · Avatar", "chip/padding-x-md", "Badge cỡ MD chưa gắn token lề (padding.md, DEC-341)"),
]
e = html.escape
data, moved = [], {}
for slug, name, url, ap in PAGES:
    c = json.loads((WORK / f"{slug}-r3/check.json").read_text())
    g = [r for r in c["rows"] if r.get("gap") and r["gap"] != "none"]
    groups = {}
    for r in g:
        groups[r.get("group")] = groups.get(r.get("group"), 0) + 1
        if r.get("isVar") and r["gap"] == "moved" and r["theme"] == "Light":
            k = (r["part"].replace("Token ", ""), r["platform"], str(r["value"]), str((r.get("to") or {}).get("value")))
            moved.setdefault(k, []).append(name)
    sp = WORK / f"{slug}-r3/state.json"  # không ghi đè: state giữ vòng đã duyệt của từng trang
    if not sp.exists():
        sp.write_text(json.dumps({"round": "foundation", "artifact_url": f"https://claude.ai/artifact/{url}",
                                  "source": f"design-system/components/_work/{slug}", "approved": {"foundation": None}, "figma": {}}, ensure_ascii=False, indent=1))
    st = json.loads(sp.read_text())
    locked = st.get("locked") or []
    if (st.get("approved") or {}).get("foundation"):  # đã chốt vòng 3: không còn dòng cần quyết
        c["open"] = 0
    data.append(dict(slug=slug, name=name, url=f"https://claude.ai/artifact/{url}", ap=ap, rows=len(c["rows"]), open=c["open"], gaps=c["gaps"],
                     total=len(g), groups=groups, ignored=len(c.get("ignored") or []), locked=locked))
live = [d for d in data if not d["locked"]]
held = [d for d in data if d["locked"]]
total = sum(d["total"] for d in live)
need = sum(d["open"] for d in live)
kind_sum = {k: sum(d["gaps"].get(k, 0) for d in live) for k, *_ in KINDS}
top = max([d["total"] for d in live] or [1]) or 1
worst = max(live, key=lambda d: d["open"])
rows = ""
for d in data:
    bar = "".join(f'<i style="width:{d["gaps"].get(k, 0) / top * 100:.2f}%;background:{col}" title="{e(lb)}: {d["gaps"].get(k, 0)}"></i>' for k, lb, col, _ in KINDS if d["gaps"].get(k))
    if d["locked"]:
        at = "vòng 1, tab 2 và 3 khoá" if "preview" in d["locked"] else "vòng 2, tab 3 khoá"
        rows += f'<tr class="lk"><td><a href="{d["url"]}">🔒 {e(d["name"])}</a><div class="s">{e(d["ap"])}</div></td><td colspan="4" class="s">Đang ở {at}. Số dòng rà sẽ tính lại khi tới vòng 3.</td></tr>'
        continue
    rows += f'<tr><td><a href="{d["url"]}">{e(d["name"])}</a><div class="s">{e(d["ap"])}</div></td><td class="n"><b>{d["open"]}</b></td><td class="n">{d["total"]}</td><td class="n">{d["rows"]}</td><td><div class="bar">{bar}</div></td></tr>'
maxg = max([v for d in live for v in d["groups"].values()] or [1])
heat = ""
for d in live:
    cells = ""
    for k, _ in GROUPS:
        v = d["groups"].get(k, 0)
        cells += f'<td class="h" style="background:rgba(0,54,181,{v / maxg * .75:.2f});color:{"#fff" if v / maxg > .5 else "#171717"}">{v or "·"}</td>'
    heat += f'<tr><td>{e(d["name"])}</td>{cells}</tr>'
mv = "".join(f'<tr><td><code>{e(k[0])}</code></td><td>{e(k[1])}</td><td class="n">{e(k[2])}</td><td class="n"><b>{e(k[3])}</b></td><td class="s">{e(", ".join(v))}</td></tr>'
             for k, v in sorted(moved.items(), key=lambda x: (-len(x[1]), x[0][0])))
legend = "".join(f'<li><i style="background:{col}"></i><b>{e(lb)}</b> <span class="c">{kind_sum[k]}</span><div class="s">{e(why)}</div></li>' for k, lb, col, why in KINDS)
rules = "".join(f'<tr><td>{e(a)}</td><td><code>{e(b)}</code></td><td>{e(c)}</td></tr>' for a, b, c in RULES)
logo = base64.b64encode((ROOT / "design/brand/innvie-v1/logo-color.png").read_bytes()).decode()
page = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rà vòng 3 · Base components</title>
<link href="https://fonts.googleapis.com/css2?family=Cal+Sans&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><style>
*{{box-sizing:border-box}}body{{margin:0;font:14px/20px Inter,system-ui,sans-serif;color:#171717;background:#F7F8FA}}
.band{{background:#0036B5;color:#fff;padding:20px max(24px,calc(50% - 540px));display:flex;align-items:center;gap:16px}}.band img{{height:28px;background:#fff;border-radius:6px;padding:4px 8px}}
h1,h2{{font-family:'Cal Sans',Inter,sans-serif;font-weight:400;margin:0}}h1{{font-size:24px;line-height:32px}}h2{{font-size:18px;line-height:24px;margin-bottom:4px}}
main{{max-width:1080px;margin:auto;padding:24px}}section{{background:#fff;border:1px solid #E5E5E5;border-radius:12px;padding:20px;margin-bottom:16px;overflow-x:auto}}
.kpi{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:16px}}.kpi div{{background:#fff;border:1px solid #E5E5E5;border-radius:12px;padding:16px}}.kpi b{{display:block;font:400 28px/36px 'Cal Sans',Inter}}
table{{border-collapse:collapse;width:100%;margin-top:10px}}th,td{{padding:8px 10px;border-bottom:1px solid #EEE;text-align:left;vertical-align:middle}}th{{font-size:12px;color:#525252;font-weight:600}}
.n{{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}}.s{{font-size:12px;line-height:16px;color:#525252}}a{{color:#0036B5;font-weight:600}}
.bar{{display:flex;height:14px;min-width:220px;border-radius:4px;overflow:hidden;background:#F5F5F5}}.bar i{{display:block}}code{{font:12px/16px 'JetBrains Mono',ui-monospace,monospace;background:#F5F5F5;padding:1px 4px;border-radius:4px}}
ul.lg{{list-style:none;padding:0;margin:12px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px}}ul.lg i{{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px}}.c{{color:#525252}}
tr.lk{{background:#FAFAFA}}.h{{text-align:center;font-variant-numeric:tabular-nums}}mark{{background:#FFF1B8;padding:0 2px;border-radius:2px}}p{{margin:6px 0}}ul.n2{{margin:8px 0 0;padding-left:18px}}ul.n2 li{{margin:4px 0}}
</style></head><body><div class="band"><img src="data:image/png;base64,{logo}" alt="innvie"><h1>Rà vòng 3 · Base components</h1></div><main>
<div class="kpi"><div><b>{need}</b><span class="s">dòng cần bạn quyết</span></div><div><b>{total}</b><span class="s">dòng có gap, trên {len(live)} component đang mở</span></div><div><b>{kind_sum['moved']}</b><span class="s">dòng foundation đã đổi số</span></div><div><b>{len(held)}</b><span class="s">component đang khoá vòng 3</span></div></div>
<section><h2>Kết luận</h2><ul class="n2">
<li><mark>Trang review vẽ theo bản token nhúng cũ</mark>: khớp token chưa có nghĩa là khớp số. Trang rà này so thêm bản nhúng với <code>tokens.css</code> 0.35.0; Tooltip, Buttons, Form controls, Badge · Avatar lệch vì lý do này.</li>
<li><mark>{e(", ".join(d["name"] for d in held))} chưa đi đủ vòng trước</mark>, nên vòng 3 đang khoá. Đi lần lượt vòng 1 rồi vòng 2; số dòng của các trang này không tính vào trang tổng.</li>
<li>Trong nhóm đang mở, nhiều nhất là <mark>{e(worst['name'])}</mark> với {worst['open']} dòng cần quyết.</li></ul></section>
<section><h2>Từng component</h2><p class="s">Bấm tên để mở trang. Trên trang, nút tròn góc dưới phải mở bảng: bước 3, lọc <b>Có gap</b>, mỗi dòng có Đã duyệt, Trước → Sau, Soi và ô chọn. Lựa chọn lưu trên trang.</p>
<table><thead><tr><th>Component · nguồn đã duyệt</th><th class="n">Cần quyết</th><th class="n">Có gap</th><th class="n">Tổng dòng</th><th>Loại gap</th></tr></thead><tbody>{rows}</tbody></table><ul class="lg">{legend}</ul></section>
<section><h2>Gap nằm ở nhóm foundation nào</h2><table><thead><tr><th>Component</th>{''.join(f'<th class="h">{e(l)}</th>' for _, l in GROUPS)}</tr></thead><tbody>{heat}</tbody></table></section>
<section><h2>Số foundation đã đổi, chế độ Light</h2><p class="s">Trước là số trên trang review, Sau là <code>tokens.css</code> hiện tại. Màu Dark đổi theo DEC-316 xem trên từng trang.</p>
<table><thead><tr><th>Token</th><th>Nền tảng</th><th class="n">Trước</th><th class="n">Sau</th><th>Component dính</th></tr></thead><tbody>{mv}</tbody></table></section>
<section><h2>Luật mới chưa gắn token trên trang</h2><p class="s">Máy tìm <code>var(--…)</code> trong CSS của component, không đo hình; cần xem trên trang để biết số có đúng không.</p><table><thead><tr><th>Component</th><th>Token</th><th>Luật</th></tr></thead><tbody>{rules}</tbody></table></section>
<section><h2>Base không có trang review</h2><table><tbody><tr><td>Breadcrumbs</td><td>Spec nhắc <code>shadow/lg-border</code>, <code>text/primary</code>, <code>text/tertiary</code>: không có trong <code>tokens.json</code></td></tr><tr><td>Logo</td><td>Không lệch tên token</td></tr><tr><td>QR code</td><td>Không lệch tên token</td></tr></tbody></table></section>
<section><h2>Trang này chưa kiểm</h2><ul class="n2"><li><b>Figma:</b> chưa so với bản vẽ, snapshot từ 02/11 cũ hơn DEC-344 (BL-389).</li>
<li><b>Khung demo:</b> {sum(d['ignored'] for d in data)} giá trị thuộc khung màn demo hoặc component khác bị bỏ khỏi đối chiếu; danh sách trong <code>check.json</code> mục <code>ignored</code>.</li>
<li><b>Select:</b> 2 dòng trong bottom sheet (<code>.sht .mi</code>, <code>.rd.on</code>) Soi chưa ra phần tử; vẫn chọn được, nhưng không tô trên hình.</li>
<li><b>Lựa chọn cũ:</b> quy từ số thứ tự phương án của <code>check.json</code> gần nhất trong repo, có thể lệch nếu phương án từng đổi. Dòng nào thấy lạ thì ghi chú trên trang.</li></ul></section>
</main></body></html>"""
out = ROOT / "design-system/_review/base-round3.html"
out.write_text(page)
print(out, len(page) // 1024, "KB", "· cần quyết", need, "· gap", total, kind_sum)
for d in data:
    print(d["name"], "cần quyết", d["open"], "· gap", d["total"], "· tổng", d["rows"])
print("moved Light", len(moved))
