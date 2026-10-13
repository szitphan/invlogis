---
name: figma-audit
description: Dùng khi cần rà nhất quán NHIỀU màn đã vẽ trên Figma của 1 feature — token, chữ, khoảng cách, bo góc, biến thể nút, icon (kể cả icon thay trong instance), khối tự dựng, mã bản ghi dọc luồng → báo cáo sai lệch theo mức Cao/Trung/Thấp, sửa theo mục user chọn. Vẽ màn mới thì dùng `/figma-screen`.
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_write
user-invocable: true
argument-hint: "<feature> [--flow <flow-slug>] [--page <trang Figma>]"
---

# /figma-audit — rà nhất quán nhiều màn đã vẽ

`/figma-screen` tự kiểm **từng màn** lúc vẽ. Skill này kiểm **giữa các màn** sau khi đã vẽ: cùng một
vai trò, cùng một nút, cùng một icon có giống nhau ở mọi màn không, và dữ liệu mẫu có đi đúng một bản
ghi dọc luồng không. Chỉ đọc và báo; sửa chỉ khi user chọn mục.

Đọc cổng kết nối trong `../reqwise-diagram-rules.md` § 5 trước: `figma_status` trước mọi thứ, đúng
một cửa sổ, cửa sổ bị throttle thì nhờ user đưa Figma lên trước.

## Bước 1 — chọn màn

1. No-arg → picker feature (feature có `srs/{feature}-userflow.md`). Feature chưa có → refuse + route
   `/user-flow` (nhóm B, `feature-bootstrap.md`).
2. Đọc userflow Mục 2 (số màn, slug, thiết bị, flow) và Mục 3. `--flow` → chỉ màn của flow đó.
3. `figma_read get_page_model` trên trang chứa màn (trang hỏi user nếu chưa biết; nhớ trong
   `screens/{feature}-screen-index.md` hoặc wireframe index nếu có link Figma). Lấy artboard có tên
   theo quy ước `{[#]} · {web|mob} · {slug}[ · {Trạng thái}]` (`naming-conventions.md` mục *Màn hình &
   flow*) và slug thuộc feature.
4. Báo trước khi đọc: `{n} màn khớp · {m} màn trong userflow chưa có frame · {k} frame tên sai quy ước
   (bỏ qua)`. Frame tên sai quy ước KHÔNG đoán — liệt kê để user đổi tên hoặc bỏ.

## Bước 2 — đọc cây node

`figma_write` gom nhiều artboard một lần, **tối đa ~12 artboard/lần** (tránh timeout 30s):

```js
const ids = [/* nodeId artboard */]; const out = [];
for (const id of ids) out.push(await figma.getDesignContext({ nodeId: id, depth: 20, detail: "full" }));
return out;
```

Kết quả lớn được lưu thành file trong `tool-results/` — dùng thẳng đường dẫn đó làm đầu vào bước 3,
KHÔNG đọc file vào ngữ cảnh. Kết quả nhỏ trả inline → ghi ra scratchpad rồi dùng.

## Bước 3 — máy đo (lớp 1, A6 trong `ui-review.md`)

```bash
python3 _scripts/figma-audit.py <batch1> <batch2> ... \
  --userflow docs/{feature}/srs/{feature}-userflow.md --design design/design.md --out <scratch>/r.md
```

| Mã | Kiểm | Mức |
|---|---|---|
| K1 | Màu / cỡ chữ / bo góc / khoảng cách / padding không gắn token (chỉ node tự dựng) | màu Cao · chữ, bo Trung · khoảng cách Thấp |
| K2 | Cùng tên layer (vai trò) mà khác giá trị giữa các màn, so trong cùng thiết bị | Trung |
| K3 | > 1 nút Primary trong một nhóm · cùng nhãn nút khác biến thể/cỡ giữa các màn | Cao · Trung |
| K4 | Icon: cỡ ngoài 12/14/16/18/20/24 · nét ≠ cỡ × 1.8/24 (chip × 2/24) gom theo cỡ · màu nét không gắn token · sai icon theo hành động của `design.md` · cùng nhãn khác icon · icon mặc định thư viện đang hiện · vector tự vẽ | Cao (cỡ) · Trung |
| K5 | Khung tự dựng trùng tên component đang dùng (nghi tách rời / dựng lại) | Trung |
| K6 | Mã bản ghi chỉ có ở 1 màn trong khi các màn khác cùng flow dùng mã cùng loại khác | Thấp |

Icon được đọc **kể cả bên trong instance** (icon thay qua thuộc tính/override). Node ẩn bị bỏ qua.
Sửa ngưỡng/luật trong script → chạy 2 fixture: `_scripts/fixtures/figma-audit/pass.json` (exit 0,
0 mục) và `fail.json` (exit 1, đủ K1–K6).

## Bước 4 — báo cáo (L1)

Ghi `docs/reports/figma-audit/{YYYY-MM-DD}-{feature}-figma-audit.md` (frontmatter `type:
figma-audit-report`, `feature`, `figma`, `updated`) qua L1. Trong chat in tóm tắt:

```
Đã rà {n} màn ({flow…}) · Cao {a} · Trung {b} · Thấp {c}
Cao: <liệt kê>
Trung đáng chú ý: <tối đa 5, gộp theo nguyên nhân>
Máy KHÔNG kiểm: nghiệp vụ/nhãn đúng sai, thẩm mỹ, thứ bậc thị giác (@visual-reviewer khi vẽ)
```

Diễn giải: một mục K4 nét "244 icon 14px để nét 1.2" là **một nguyên nhân** (icon resize không đặt lại
nét), nêu đúng như vậy, không đếm thành 244 lỗi. K6 là gợi ý soát dữ liệu mẫu, có thể đúng (mã trong
ô tìm, bản ghi trước đó).

## Bước 5 — sửa theo mục user chọn

1. Hỏi user chọn mục (AskUserQuestion, multiSelect) — KHÔNG tự sửa.
2. Mỗi mục: bảng **Trước → Sau** (node, giá trị cũ, giá trị mới, token gắn) — L2 theo memory dự án.
   Mục làm đổi giao diện đã duyệt (biến thể nút, icon, khoảng cách nhìn thấy được) → nói rõ "đổi giao
   diện đã duyệt" và chờ user đồng ý riêng.
3. Sửa bằng `figma_write` (`modify`, `setInstanceProperties`, gắn biến). Sửa trong **component nguồn**
   khi lỗi nằm ở component dự án (vd nét icon trong component) thay vì vá từng instance; component thư
   viện ngoài (Astryx) → chỉ báo, không sửa.
4. Sau khi sửa: đọc lại đúng các artboard bị chạm, chạy lại script, báo số mục còn lại. Màn đã sửa →
   gợi ý `/figma-sync {feature}` để đồng bộ tài liệu.

## Constraints

* Chỉ đọc cho tới khi user chọn mục; mọi ghi file qua L1/L2 (`approval-gate.md`).
* Không đoán frame tên sai quy ước; không đoán nhãn nghiệp vụ — K6 chỉ gợi ý soát.
* Báo tách mức, không in một chữ PASS; mục máy không kiểm luôn ghi ra (`diagram-correctness.md` Mục 2).
* Kết quả `figma-audit.py` là nguồn; không tự thêm/bớt mục ngoài script vào bảng máy đo — nhận xét của
  AI ghi riêng dưới mục "Diễn giải".

## References

- @.claude/rules/approval-gate.md
- @.claude/rules/ui-review.md (A6 — lớp 1)
- @.claude/rules/naming-conventions.md (mục *Màn hình & flow* — tên frame)
- @.claude/rules/design-system.md (`design/design.md` — Iconography, Tên trong Figma)
- @.claude/rules/feature-bootstrap.md (nhóm B)
- `_scripts/figma-audit.py` + `_scripts/fixtures/figma-audit/`
