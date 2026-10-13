---
name: queue
description: Dùng khi muốn xem việc đang chờ bạn trong repo — feature chờ duyệt land, lần chạy AI bị chặn cần trả lời, run card chờ duyệt, việc AI đang chạy — rồi chọn 1 việc để xử lý ngay. `/queue` · `/queue <số>`.
allowed-tools: Read, Edit, Bash, Glob, Grep, Skill, AskUserQuestion
user-invocable: true
argument-hint: "[<số thứ tự trong bảng>]"
---

# /queue — việc đang chờ bạn

## Goal

Một chỗ duy nhất trả lời "giờ tôi nên xử lý gì?" khi nhiều feature chạy song song. Hiện 4 làn từ
`_scripts/queue.py` (nguồn số liệu duy nhất — cùng nguồn với dòng "Chờ bạn" của session-init và làn
"Chờ bạn" của `/dashboard`), người dùng chọn 1 việc, skill dẫn đúng luồng xử lý việc đó.

## Constraints

### Hard rules

- **Số liệu từ `queue.py`, không tự đếm lại** bằng prompt (2 lần chạy phải ra cùng bảng).
- **Hiện xong thì chờ người dùng chọn.** Không tự chọn việc "rõ ràng nhất", không tự land, không tự trả lời
  câu hỏi chặn thay người dùng.
- **Land chỉ khi người dùng nói rõ duyệt** đúng task 🔍 đang xem (`.claude/rules/worktree.md` Mục 4). "ok",
  "được" sau phần review = duyệt; trước khi review xong = chưa.
- Commit trên main chỉ ở bước land đã duyệt; message tóm tắt feature, kèm attribution theo hướng dẫn phiên.

### Pitfalls

- Task `🔍 ⚠ có commit mới sau khi báo ready` → review phải dựa trên bản HIỆN TẠI của branch, nói rõ phần
  đổi sau ready (`git log <sha ready>..feat/x`); đề xuất AI báo ready lại sau khi người dùng xem.
- Worktree "làm tay" (không run card) ở làn ⚙ là việc người dùng tự làm — chỉ hiển thị, không gợi ý chạy.

## Approach

1. `python3 _scripts/queue.py` → in nguyên bảng (đã đánh số). Không có gì → "Không có việc nào chờ bạn." + số
   task backlog mở (`--summary` của intake-sync) rồi dừng.
2. Có `<số>` trong args → đi thẳng bước 3 với việc đó; không có → hỏi "Chọn số nào?" và dừng lượt.
3. Dẫn luồng theo làn:

| Làn | Làm gì |
|---|---|
| 🔍 Chờ duyệt land | **Review**: đọc run card Mục 9 (nếu có), `git log --oneline main..feat/x`, `git diff --stat main...feat/x`, mở 2–3 file thay đổi chính tóm tắt bằng lời nghiệp vụ; nêu gate/finding còn lại, Mục 7 "Cần sửa trên main", điểm cần soi. Hỏi: `duyệt` · `sửa: …` · `để sau`. **duyệt** → (run có vẽ Figma: chuyển các frame từ trang nháp `_run/<slug>` sang trang chính theo `/figma-screen` Bước 3, xoá trang nháp, rồi `/figma-sync`; người dùng muốn đổi bố cục → coi như `sửa`) → `_scripts/wt.sh land <slug>` → in `git diff --cached --stat` → commit → `_scripts/wt.sh drop <slug>` → báo task tự ✅. **sửa** → `_scripts/wt.sh unready <slug>`, ghi yêu cầu vào run card Mục 6 (hoặc báo người dùng mở worktree nếu không có card), gợi ý `/run-task resume`. |
| ⛔ Chặn, chờ trả lời | Đọc run card Mục 6, hỏi từng câu (AskUserQuestion, phương án gợi ý của card làm lựa chọn). Ghi trả lời vào Mục 6 + chép thành dòng D-n ở Mục 2 (nguồn "bạn chốt {ngày}") qua L2 bảng Trước → Sau, `run_state: running`, commit trong worktree (`git -C <worktree> …`). Hỏi chạy tiếp ngay (fg/bg) → `Skill(run-task, "resume <card>")`. |
| 📝 Card chờ duyệt | In card Mục 1–5 bằng lời nghiệp vụ (như Cửa 1 của `/run-task`). `Y` → set `approved` + `run_state: running`, commit, `Skill(run-task, "resume <card>")`. `sửa: …` → sửa card (L2) rồi trình lại. `bỏ` → `run_state: cancelled`. |
| ⚙ Đang chạy | Chỉ xem: bước ✅/tổng, dòng Nhật ký cuối, worktree còn bao nhiêu file chưa commit. Không can thiệp. |

## Output

Bảng 4 làn + kết quả của việc đã chọn (đã land / đã trả lời và chạy tiếp / card đã duyệt).

## References

- @.claude/rules/worktree.md (Mục 4 duyệt land) · @.claude/rules/approval-gate.md
- `_scripts/queue.py` · `_scripts/wt.sh` · `/run-task` · `/dashboard` (làn "Chờ bạn")
