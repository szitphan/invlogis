---
name: status
description: Dùng khi cần xem trạng thái tài liệu kèm phụ thuộc upstream/downstream, hoặc chuyển status (draft → in-review → approved…) có kiểm luồng hợp lệ. `/status` · `/status <file|feature|folder> <status-mới> [lý do]` · `/status restore <file>` · `/status impact <file>`.
allowed-tools: Read, Bash, AskUserQuestion
user-invocable: true
argument-hint: "[<prefix>] | <file|feature|folder> <draft|in-review|revisions|approved|shipped> [lý do] | restore <file|folder> | impact <file>"
---

# /status — xem và chuyển trạng thái tài liệu

## Goal

Chuyển status theo đúng `.claude/rules/status-lifecycle.md`, kèm cảnh báo khi chốt (approved/shipped) một
tài liệu mà upstream của nó chưa chốt. Cho BA thấy status lan theo phụ thuộc `links:` thế nào.

Engine tất định: `.claude/skills/status/engine/status.py` (Python stdlib). Mọi kiểm luồng/ghi frontmatter
do engine làm — skill KHÔNG tự Edit dòng `status:` bằng tay.

## Constraints

**Hard rules**
- Mọi chuyển status đi qua `status.py apply|restore`. Bảng chuyển hợp lệ nằm ở `TRANSITIONS` trong engine,
  phải khớp rule `status-lifecycle.md` — sửa một bên thì sửa cả hai.
- `stale` KHÔNG đặt tay (chỉ hook `post-edit-stale.sh` đặt). Thoát stale: `restore` (về `status_prev`) khi
  review thấy không cần sửa, hoặc `apply revisions` khi cần sửa.
- Approval gate (`approval-gate.md`): chạy `--dry-run` trước → in diff (L2) → user Y → chạy thật. Đổi hàng
  loạt: 1 lần duyệt cho cả lô, nhưng vẫn in đủ diff (diff >50 dòng thì hỏi xem full hay tóm tắt).
- Exit 3 (upstream chưa approved/shipped) → hỏi user qua AskUserQuestion, nêu rõ upstream nào đang ở status
  gì. Chỉ thêm `--confirm-upstream` khi user đồng ý. KHÔNG tự thêm cờ này.
- Chạy engine với `CLAUDE_CHANGELOG_AUTHOR` = handle trong memory `user-identity` (`ba-conventions.md`
  Mục 1). Engine tự gọi `auto-changelog.sh` để ghi `_workspace/changelog.md` (hook là writer duy nhất;
  hook tự bỏ qua `docs/_shared/` theo contract của nó).
- Đổi status KHÔNG đổi `updated:` (không phải đổi nội dung) và KHÔNG kích hoạt lan stale xuống downstream.
- Không tham số có ý nghĩa → chạy `report` (read-only, không cần approval).

**Pitfalls**
- `report` là bằng chứng cấu trúc (theo `links:`). Kết luận "downstream có thật sự lỗi thời không" phải đọc
  prose 2 đầu — engine chỉ chỉ ra chỗ cần đọc.
- Doc có lifecycle riêng (`type: change-request`, `meeting`) → engine refuse, route `/cr` hoặc `/meet`.
- Doc bị stale TRƯỚC khi hook lưu `status_prev` → `restore` báo lỗi; hỏi user status đích, rồi dùng
  `apply revisions` hoặc sửa tay.
- Phạm vi quét: `docs/**` + `design/**` có `status:`. `_workspace/` (backlog, changelog, log máy) và
  `docs/exports|inbox|_reverse` không thuộc lifecycle.

## Approach

1. **Phân tích lệnh:**
   - `/status` hoặc `/status <prefix>` → `report`.
   - `/status impact <file>` → `impact`.
   - `/status <target...> <status> [lý do]` → `apply`. Target = file, folder, hoặc tên feature trần.
   - `/status restore <target...>` → `restore`.
2. **Read-only** (`report`, `impact`): chạy engine, in nguyên bảng, thêm 2-3 câu diễn giải các cờ ⚠/🟠/❌
   bằng từ nghiệp vụ. Xong.
3. **Ghi** (`apply`, `restore`):
   a. Chạy `--dry-run`. Exit 1 → in lý do ❌ + luồng hợp lệ, dừng. Exit 3 → hỏi user (Hard rules).
   b. L2: in diff từ dry-run + 1 câu tóm tắt ("Chuyển 7 doc `_shared` từ draft sang in-review, lý do …").
      Thiếu lý do khi chuyển sang `revisions`/`approved` → hỏi 1 câu (lý do là tùy chọn, user được bỏ qua).
   c. User Y → chạy thật (bỏ `--dry-run`, thêm `--confirm-upstream` nếu đã xác nhận ở a).
   d. In kết quả + gợi ý bước tiếp engine in ra.

```bash
E=.claude/skills/status/engine/status.py
python3 $E report [docs/_research]
python3 $E impact docs/_shared/system-overview.md
CLAUDE_CHANGELOG_AUTHOR=@handle python3 $E apply in-review docs/_shared --reason "gửi PO review" --dry-run
CLAUDE_CHANGELOG_AUTHOR=@handle python3 $E apply approved payment --confirm-upstream
CLAUDE_CHANGELOG_AUTHOR=@handle python3 $E restore docs/payment/userstories/payment-story-index.md
```

Exit code: `0` OK · `1` chuyển không hợp lệ / không tìm thấy · `3` cần user xác nhận upstream.

## References

- @.claude/rules/status-lifecycle.md
- @.claude/rules/approval-gate.md
- @.claude/rules/changelog.md
- @.claude/rules/ba-conventions.md
- Hook liên quan: `.claude/hooks/post-edit-stale.sh` (đặt `stale` + `status_prev`), `.claude/hooks/status-transition.sh` (gợi ý khi status đổi qua Edit tay)
