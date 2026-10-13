---
type: run-card
feature: {feature}
run_state: planned        # planned | running | blocked | review | cancelled
mode: fg                  # fg | bg
branch: feat/{feature}
worktree: .claude/worktrees/{feature}
approved:
max_rounds: 2
updated: {YYYY-MM-DD}
---
# Run: {mục tiêu 1 dòng}

## 1. Mục tiêu & phạm vi

- **Mục tiêu:** {1–2 câu — kết quả nghiệp vụ, không phải danh sách file}
- **Trong phạm vi:** {…}
- **Ngoài phạm vi:** {…}
- **Vùng ghi:** `docs/{feature}/**` (máy chặn ngoài vùng — `worktree-guard.sh`)

## 2. Đầu vào đã chốt

| Nguồn | Đường dẫn | Status |
|---|---|---|
| {brainstorm/SRS/…} | `docs/{feature}/…` | {approved/draft/stale} |

**Quyết định chốt sẵn**

| # | Câu skill sẽ hỏi | Quyết định | Ai chốt / nguồn |
|---|---|---|---|
| D1 | {…} | {…} | {bạn chốt {ngày} / DEC-xxx / meeting …} |

## 3. Các bước

| # | Bước | Skill / lệnh | Output | Gate | Reviewer | Trạng thái | Vòng | Commit | Bằng chứng |
|---|---|---|---|---|---|---|---|---|---|
| 1 | {…} | `/{skill} {feature}` | `docs/{feature}/…` | {gate của skill + lint chung} | `@{persona}` | ⬜ | 0 | | |

Trạng thái: ⬜ chưa · ⚙ đang · ✅ xong · ⛔ dừng (xem Mục 6) · ⏭ bỏ (ghi lý do ở Nhật ký)

## 4. Điều kiện Xong (máy kiểm)

- [ ] `{cond}`

## 5. Điều kiện dừng (Cửa 2)

- Cần quyết định nghiệp vụ không có ở Mục 2 (kể cả skill muốn hỏi người dùng)
- Gate FAIL hoặc finding mức cao của reviewer còn sau `max_rounds` vòng sửa
- Cần ghi ra ngoài vùng ghi (ghi vào Mục 7 rồi dừng nếu bước sau phụ thuộc)
- Upstream trong Mục 2 đổi / bị đánh `stale` trong lúc chạy

## 6. Câu hỏi chặn

| # | Bước | Câu hỏi | Vì sao không tự quyết | Phương án gợi ý | Trả lời |
|---|---|---|---|---|---|

## 7. Cần sửa trên main

| # | File | Sửa gì | Vì sao |
|---|---|---|---|

## 8. Nhật ký

- {YYYY-MM-DD HH:MM} — tạo card

## 9. Báo cáo (Cửa 3)

{tóm tắt} · {file đổi} · {gate 4 mức} · {finding reviewer} · {Điều kiện Xong} · {điểm cần soi}
