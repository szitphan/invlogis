---
name: run-task
description: Dùng khi muốn giao cho AI tự chạy một chuỗi bước tài liệu cho 1 feature trong worktree riêng — bạn duyệt run card 1 lần, AI tự chạy skill + gate + reviewer, chỉ dừng khi cần bạn quyết, xong thì đưa vào backlog chờ duyệt. `/run-task <feature> "<mục tiêu>" [--bg]` · `/run-task resume <card>`.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Skill, Agent, AskUserQuestion, EnterWorktree, ExitWorktree, PushNotification
user-invocable: true
argument-hint: "<feature> \"<mục tiêu>\" [--bg] | resume <đường-dẫn-card>"
---

# /run-task — giao việc cho AI chạy một mình trong worktree

## Goal

Biến 1 mục tiêu cấp feature (vd "viết SRS + use case + user story cho service-delivery từ brainstorm đã chốt")
thành **1 lần chạy có kiểm soát**: người dùng duyệt kế hoạch 1 lần (Cửa 1), AI tự làm trong worktree
`feat/<feature>`, tự kiểm, tự sửa, chỉ gọi người khi thật sự cần (Cửa 2), xong thì đẩy vào backlog chờ duyệt
land (Cửa 3). Người dùng rảnh tay làm feature khác trong lúc đó.

Run card `docs/<feature>/_runs/<YYYY-MM-DD>-<slug>.md` (khung `_templates/run-card.md`) là **kế hoạch +
trạng thái + báo cáo** của lần chạy. Mọi thứ tiếp tục được từ card — không phụ thuộc trí nhớ phiên.

## Constraints

### Hard rules

- **Không chạy khi card chưa duyệt.** `approved:` trống = chỉ được soạn/sửa card. Duyệt = người dùng trả lời
  Y cho bản trình Cửa 1 trong lượt này; KHÔNG suy ra duyệt từ câu khác ("ok chạy đi" cho việc khác).
- **Chế độ chạy chỉ hợp lệ trong worktree `feat/<feature>` + card đã duyệt** (`approval-gate.md` mục Chế độ
  chạy). Ở `main` → không bao giờ bỏ L1/L2.
- **Không đoán quyết định nghiệp vụ.** Skill con muốn hỏi người dùng (AskUserQuestion, câu hỏi phỏng vấn,
  "chọn 1 trong 3 phương án", confirm upstream) → tra card Mục 2 "Quyết định chốt sẵn" + nguồn đầu vào; có
  thì dùng và ghi nguồn vào Bằng chứng; không có → Cửa 2. Không có ngoại lệ "chuyện nhỏ".
- **Skill phỏng vấn không chạy tự động**: `/brainstorm`, `/deck`, `/discover`, phần phỏng vấn của
  `/urd` `/brd` `/prd-epic`, bước chọn phương án của `/figma-screen` — chỉ được đưa vào card khi mọi câu
  đã có ở Mục 2. Không chắc → để bước đó cho người dùng làm tay, ghi "ngoài phạm vi".
- **Vùng ghi = `docs/<feature>/**`** (hook `worktree-guard.sh` chặn). Cần sửa chỗ khác → ghi card Mục 7,
  bước sau phụ thuộc thì dừng ở Cửa 2. KHÔNG tìm đường vòng (Bash `sed`/`cat >` ra ngoài vùng cũng cấm).
- **Commit được trong worktree, KHÔNG BAO GIỜ commit/land/push trên main.** Land chỉ theo
  `.claude/rules/worktree.md` Mục 4 (người dùng duyệt task 🔍).
- **Báo cáo trung thực**: gate FAIL ghi FAIL kèm output; bước bỏ ghi ⏭ + lý do; reviewer finding chưa xử lý
  ghi rõ. Không gộp "PASS" (in 4 mức như `saas-layer.md` Mục 6).

### Pitfalls

- Card quá to (>8 bước, nhiều tầng tài liệu) → chạy lâu, khó review. Tách 2 card nối tiếp.
- Điều kiện Xong kiểu `manual` hoặc "đã viết xong" → không kiểm được. Mỗi dòng phải là `exists:`/`grep:`
  trỏ vào output thật (mã FR, file story…).
- Upstream đang `stale`/`draft` mà card coi là chốt → Ready check phải nêu, người dùng quyết chạy hay không.
- Sửa lại card giữa chừng để "hợp thức hoá" việc đã làm khác kế hoạch → cấm. Kế hoạch đổi = Cửa 2.

## Inputs

- `<feature>` — slug có `docs/<feature>/`. Không có → dừng, gợi ý `/brainstorm`.
- `"<mục tiêu>"` — kết quả muốn có.
- `--bg` — chạy ở terminal riêng tại worktree (phiên chính rảnh). Mặc định fg (phiên hiện tại vào worktree).
- `resume <card>` — chạy tiếp card `blocked` (đã trả lời Mục 6) hoặc `running` bị ngắt.
- Không tham số → chạy `/queue` để chọn.

## Approach

### A. Cửa 1 — Ready check + card (phiên chính, cùng người dùng)

1. **Đọc trạng thái feature**: `ls docs/<feature>/**`, status từng doc, `python3 _scripts/queue.py --json`
   (feature đã có run đang chạy/chặn → báo, không mở card thứ 2 cùng worktree), `git` worktree đã có chưa.
2. **Ready check** (soft gate — báo, người dùng quyết):
   - Upstream cần cho mục tiêu có chưa, status gì (stale/draft nêu rõ).
   - Câu hỏi mở còn treo trong brainstorm/SRS liên quan mục tiêu → liệt kê; đề xuất người dùng chốt ngay
     (vào Mục 2) hoặc đưa ra ngoài phạm vi.
   - Chuỗi bước theo luồng chính trong `CLAUDE.md`; mỗi bước đọc SKILL.md tương ứng để biết: câu skill sẽ
     hỏi (→ Mục 2), gate skill tự chạy, output path, reviewer phù hợp (`agent-conventions.md`).
3. **Soạn card** từ `_templates/run-card.md`: Mục 1–5 đủ, Mục 3 mỗi bước 1 dòng, Mục 4 điều kiện máy kiểm
   (thử ngay `python3 _scripts/queue.py check "<cond>"` — phải đang ❌, nếu ✅ sẵn thì điều kiện vô nghĩa).
4. **Trình Cửa 1** bằng lời nghiệp vụ (`ba-conventions.md` Mục 5): mục tiêu, các bước, quyết định chốt sẵn,
   điều kiện Xong, khi nào sẽ dừng hỏi, fg/bg. Hỏi: `Y` chạy · `để sau` lưu card planned · `sửa: …` · `n`.
   Câu Mục 2 còn trống → hỏi luôn ở đây (AskUserQuestion), không để lúc chạy mới hỏi.
5. **Y** → `_scripts/wt.sh new <feature>` nếu chưa có (main phải sạch phần liên quan — `wt.sh` cảnh báo) →
   ghi card vào `.claude/worktrees/<feature>/docs/<feature>/_runs/…` với `run_state: running`,
   `approved: <hôm nay>` → commit card trong worktree (`git -C <wt> commit -m "<feature>: run card …"`).
   **để sau** → ghi card `run_state: planned`, `approved:` trống (vào làn 📝 của `/queue`).

### B. Vào worktree

- **fg**: `EnterWorktree(path: "<abs>/.claude/worktrees/<feature>")` rồi chạy C trong phiên này.
- **bg**: KHÔNG dùng agent nền (`Agent`) — đã thử 2026-10-13: agent khởi từ gốc repo bị từ chối
  `EnterWorktree`; agent `isolation: "worktree"` bị khoá trong worktree riêng của nó, không ghi được vào
  worktree feature. Thay vào đó in cho người dùng 1 lệnh để mở terminal mới tại worktree:
  `cd <abs worktree> && claude "/run-task resume <card path tương đối>"` — phiên mới đó chạy C–E như fg.
  Phiên chính trả lại cho người dùng ngay; tiến độ xem qua `/queue` (card ⚙ / ⛔ / 🔍).

### C. Vòng chạy (trong worktree)

Mỗi bước ⬜ theo thứ tự trong card Mục 3:

1. Card: bước → ⚙, Nhật ký `- {giờ} — bắt đầu bước N`.
2. Kiểm upstream Mục 2 chưa bị đánh `stale` từ lúc duyệt (grep `^status: stale`) → có thì Cửa 2.
3. Gọi skill (`Skill`, args kèm `run mode: <card path>`). Trong skill: L1/L2/L3 thay bằng card (in tóm tắt
   plan vào Nhật ký, không chờ); câu hỏi → quy tắc "Không đoán quyết định" ở trên.
4. **Gate**: gate skill tự khai + gate chung áp được: `python3 _scripts/saas-layer-lint.py` (FR/BR, nếu dự án
   SaaS), gate sơ đồ (`diagram-correctness.md`), `_scripts/status-chip-lint.py` khi có wireframe HTML.
5. **Reviewer chéo**: `Agent` persona ở cột Reviewer (vd `@senior-ba` cho SRS, `@qa-reviewer` cho AC,
   `@flow-reviewer` cho userflow). Người làm ≠ người review.
6. FAIL hoặc finding mức cao → sửa → gate + review lại. Quá `max_rounds` → Cửa 2.
7. Xong → `git add docs/<feature> && git commit -m "<feature>: <bước> (run <card slug>)"`; card: ✅, Vòng,
   SHA, Bằng chứng (đường dẫn output + kết quả gate 1 dòng). Commit card cùng lúc.

### D. Cửa 2 — dừng có chủ đích

Card: bước → ⛔, Mục 6 thêm câu hỏi (câu hỏi bằng lời nghiệp vụ, vì sao không tự quyết, 2–3 phương án gợi ý),
`run_state: blocked`, Nhật ký, commit. `PushNotification`: "⛔ <feature>: cần bạn trả lời <n> câu — /queue".
fg → `ExitWorktree(action: "keep")`. Dừng lượt.

**Resume** (`/run-task resume <card>`, thường từ `/queue`): người dùng đã trả lời → ghi vào Mục 6 cột Trả lời
+ chép quyết định vào Mục 2 (D-n mới, nguồn "bạn chốt <ngày>") qua L2 bảng Trước → Sau, `run_state:
running`, commit, rồi B → C từ bước ⛔.

### E. Cửa 3 — xong

1. Chấm từng dòng Mục 4 bằng `python3 _scripts/queue.py check`. Dòng nào ❌ → bước còn thiếu → quay C hoặc
   Cửa 2, KHÔNG báo xong.
2. Điền Mục 9: tóm tắt nghiệp vụ, `git diff --stat main...feat/<feature>`, gate 4 mức, finding reviewer đã
   xử lý / còn lại, điểm người dùng nên soi (quyết định mới suy ra, chỗ đụng Mục 7), Điều kiện Xong từng dòng.
3. `run_state: review`, commit, rồi `_scripts/wt.sh ready <feature> "<mục tiêu>"` (sinh task 🔍 trong backlog).
4. `PushNotification`: "🔍 <feature> xong <n> bước — chờ bạn duyệt land (/queue)". fg → `ExitWorktree(keep)`.

## Output

- Run card trong worktree, cập nhật sau mỗi bước; output của các skill con trong `docs/<feature>/**`.
- Commit trong `feat/<feature>` (không đụng main). Task 🔍 trong backlog khi xong.
- Báo cuối lượt: run_state, bước ✅/tổng, câu hỏi chặn hoặc lời mời review.

## References

- @.claude/rules/approval-gate.md (mục Chế độ chạy)
- @.claude/rules/worktree.md (vùng ghi Mục 2, duyệt land Mục 4)
- @.claude/rules/backlog.md · @.claude/rules/ba-conventions.md · @.claude/rules/agent-conventions.md
- @.claude/rules/saas-layer.md · @.claude/rules/diagram-correctness.md
- `_templates/run-card.md` · `_scripts/queue.py` · `_scripts/wt.sh` · `/queue`
