# Approval Gate Convention‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

> Mọi skill phải tuân thủ rule này khi write/edit file. Mục đích: human-in-the-loop (HITL) thống nhất — không skill nào tự ý ghi file mà không qua approval.

## 3 levels‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| Level | Bắt buộc khi | Cơ chế |
|-------|--------------|--------|
| **L1 Plan** | Trước mọi tool `Write` / `Edit` / batch tạo ≥1 file | In bảng plan; user confirm Y/n/select |
| **L2 Diff** | Khi `Edit` 1 file đã tồn tại (kể cả khi skill tự vào update mode do file đã có, không cần flag) | Hiển thị unified diff; user confirm Y/n/edit-prompt |
| **L3 Iterate** | Output sáng tạo: ASCII wireframe, mermaid diagram, prose draft | Render trong chat → loop refine; max 3 vòng |

## L1 — Plan preview‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

**Format chuẩn** (skill in ra trước khi ghi):

```
[/skill-name] Sẽ thực hiện:
  # | path                              | action  | summary
  1 | docs/payment/payment-urd.md               | create  | URD draft, 3 user types, 5 needs
  2 | docs/payment/payment-brd.md               | create  | BRD draft, 4 objectives, 3 risks
  3 | docs/payment/srs/payment-spec.md          | update  | thêm 2 FR, sửa NFR perf

Apply? (Y/n/select):
```

**User response:**
- `Y` / `<enter>` / `yes` / `ok` → proceed tất cả.
- `n` / `no` / `abort` → huỷ toàn bộ, không ghi gì.
- `select skip 2,3` → chạy item 1, bỏ 2 và 3.
- `select only 1` → chỉ chạy item 1.
- Bất kỳ free text khác → treat như request thay đổi plan, skill phải re-plan.

**Rules:**
- L1 **bắt buộc** ngay cả khi chỉ tạo 1 file.
- Bảng plan tối đa 1 dòng/file. Summary ngắn (≤50 ký tự).
- Skill KHÔNG được skip L1 với cớ "user đã confirm trong skill khác".

## L2 — Diff confirm‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

**Khi nào:** edit file đã tồn tại (cả khi skill tự vào update mode vì file đã có, hoặc apply patch trong /cr).

**Format:**

```
[/skill-name] Diff cho docs/payment/payment-urd.md:

--- a/docs/payment/payment-urd.md
+++ b/docs/payment/payment-urd.md
@@ -12,7 +12,8 @@
 ## 3. User Needs
 
-1. Khách thanh toán < 30s
+1. Khách thanh toán < 30s qua Momo/VNPay
+2. Có save card cho lần sau
 
Apply? (Y/n/edit-prompt):
```

**User response:**
- `Y` → apply diff.
- `n` → huỷ edit này (giữ file cũ).
- `edit-prompt: <text>` → quay lại bước synthesize với feedback `<text>`, tạo diff mới.

**Rules:**
- Diff phải là unified format với ≥3 dòng context.
- Nếu diff > 50 dòng: skill cảnh báo "diff lớn, có muốn xem full hay summary?" trước khi in.
- L2 chạy SAU L1 (L1 list path + action `update`, L2 mới show diff khi user đã Y ở L1).

## L3 — Iterate refine‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

**Khi nào:** output sáng tạo **render được trong chat** cần feedback nhiều vòng. Tiêu biểu:
- ASCII wireframe (`/wireframe-ascii`) — monospace render OK
- ASCII flow diagram trong brainstorm — monospace render OK
- Prose draft dài (vd executive summary BRD)

**KHÔNG áp L3 cho mermaid** (`/sequence`, `/erd`) — chat chỉ in source code mermaid, không render diagram. User nhìn text raw không review được. Mermaid skills đi thẳng L1 → Write → user review từ rendered file (IDE/Obsidian/GitHub preview) → gọi lại skill, skill tự vào update mode.

**Format:**

```
[/skill-name] Phiên bản 1:

<output render trong chat>

Đồng ý / Sửa: <mô tả thay đổi> / Hủy:
```

**User response:**
- `Đồng ý` / `ok` / `approve` / `Y` → tiếp đến L1 (plan write).‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
- `Sửa: ...` / free text → skill regenerate v2 với feedback.
- `Hủy` / `cancel` / `n` → abort.

**Rules:**
- Max 3 vòng iterate. Vòng 3 (v3) là vòng ép chốt — nếu user vẫn `Sửa:`, skill thông báo "đã đạt max 3 vòng, em chốt v3 và đi tiếp L1; anh edit file manually sau nếu cần."
- Mỗi vòng số hiệu rõ ràng: `Phiên bản 1`, `Phiên bản 2`, `Phiên bản 3`.
- L3 chạy TRƯỚC L1.

## Soft gate vs Hard gate

Approval gate ≠ readiness gate. Hai khái niệm khác nhau:

| | Approval gate (rule này) | Readiness gate (chain rule) |
|---|---|---|
| Hỏi gì | "Apply những thay đổi này không?" | "Có đủ upstream để chạy skill này không?" |
| Khi nào | Trước mỗi write/edit | Bắt đầu skill, kiểm tra prerequisite |
| Default | L1 luôn chạy | **Soft** — warn nếu thiếu, vẫn proceed |

Readiness gate examples:
- `/userstory payment` nhưng chưa có `/usecase` → warn "Chưa có UC, em vẫn chạy" + proceed.
- `/jira push` nhưng có US `status: stale` → **refuse** (đây là exception hard gate, vì Jira là external side-effect).

## Tham chiếu trong SKILL.md

Mọi SKILL.md PHẢI có dòng:

```markdown
References:
- @.claude/rules/approval-gate.md
```

Và trong Processing steps, dùng cụm từ chuẩn:

```markdown
6. **Approval L1:** in plan preview (xem rule approval-gate.md). User Y → tiếp.
7. **Approval L2** (nếu file đã tồn tại — update mode tự động): show diff trước khi ghi.
```

## Exception — skill không cần approval gate

Chỉ skill read-only thuần (không ghi file) được miễn:

| Skill | Lý do |
|-------|-------|
| `/gap` | Read-only analysis; L1 bắt buộc cho `traceability.md` write |

> `/dashboard` KHÔNG được miễn — nó Write file HTML nên vẫn qua L1 (chỉ phần data scan là read-only).

Mọi skill khác (kể cả `/reverse-doc` tái lập từ nguồn ngoài) đều phải qua L1.

## Sub-agent KHÔNG được ghi file đích trước approval

KHÔNG có exception "Write-rồi-confirm". Nếu 1 skill dùng Task tool sub-agent để tận dụng context riêng, sub-agent phải **trả về proposed content** (không tự Write file đích) — main thread gom lại, show L1/L2, user Y rồi main thread mới Write.

Lý do bỏ mô hình "sub-agent Write thẳng rồi rollback nếu user từ chối": rollback không đáng tin. `git checkout -- file` trả về HEAD (không phải trạng thái ngay trước sub-agent) → nuốt thay đổi chưa commit; `rm` không phân biệt file vừa tạo với file untracked có sẵn; hook (changelog.md/staleness) đã kịp chạy side-effect không hoàn tác được. An toàn dữ liệu > tốc độ song song.

`/srs` đã chuyển sang mô hình tuần tự này (L1 trước mỗi Write). Không skill nào được ghi file đích trước approval với cớ "chạy sub-agent song song".

## Chế độ chạy (run mode) — 1 lần duyệt cho cả lần chạy

`/run-task` cho AI tự chạy chuỗi skill. Khi đó **run card đã duyệt thay cho L1/L2/L3 của từng skill con** —
người dùng đã duyệt kế hoạch, phạm vi ghi, quyết định nghiệp vụ và điều kiện dừng 1 lần (Cửa 1), và duyệt
kết quả 1 lần trước khi land (Cửa 3, `.claude/rules/worktree.md` Mục 4).

Hợp lệ **chỉ khi đủ cả 3** (thiếu 1 → quay về L1/L2/L3 bình thường):

1. Phiên/agent đang ở worktree branch `feat/<feature>` (KHÔNG BAO GIỜ trên `main`).
2. Có run card `docs/<feature>/_runs/*.md` với `approved:` có ngày và `run_state: running`.
3. File sắp ghi nằm trong vùng ghi `docs/<feature>/**` (hook `worktree-guard.sh` chặn bằng máy).

Trong chế độ chạy, skill con:

- **L1/L2** → không chờ Y; in tóm tắt plan/diff vào Nhật ký của card rồi ghi.
- **L3** (iterate) → thay bằng reviewer agent theo card; quá `max_rounds` → dừng.
- **Câu hỏi cho người dùng** (AskUserQuestion, phỏng vấn, chọn phương án, confirm upstream) → tra
  "Quyết định chốt sẵn" của card + tài liệu nguồn; không có → **dừng (Cửa 2)**, ghi câu hỏi vào card. KHÔNG đoán.
- Mọi gate máy (lint, diagram gate, saas-layer) vẫn chạy đủ — chế độ chạy bỏ chờ người, không bỏ kiểm.

Vì sao không phạm anti-pattern "bypass bằng env var": không có cờ nào bật được chế độ này. Điều kiện là
trạng thái kiểm được (branch + card đã duyệt + vùng ghi), mọi thay đổi nằm trên branch riêng bỏ được bằng
`wt.sh drop`, và không gì vào `main` khi người dùng chưa duyệt.

## Anti-patterns

❌ **KHÔNG** auto-pick file im lặng dù "có vẻ rõ ràng".
❌ **KHÔNG** gộp L1 + L2 thành 1 prompt ("Tạo file? Y/n" mà không show diff khi update).
❌ **KHÔNG** dùng L3 cho file write thuần (vd `/urd` text — không cần iterate, đi thẳng L1).
❌ **KHÔNG** skip L1 khi chỉ ghi 1 file ngắn.
❌ **KHÔNG** dùng env var `CLAUDE_AUTO_APPROVE` hoặc tương tự để bypass.
❌ **KHÔNG** coi chế độ chạy là hợp lệ ngoài worktree `feat/*`, khi card chưa duyệt, hoặc để ghi ngoài `docs/<feature>/**`.

## Tóm tắt 1 dòng

> **L3 (iterate nếu sáng tạo) → L1 (plan + Y/n) → L2 (diff nếu update) → Write.**‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
