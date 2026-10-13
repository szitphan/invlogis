---
paths:
  - "_scripts/wt.sh"
  - "_scripts/logbook.py"
  - "_workspace/**"
---

# Worktree — chạy song song nhiều feature không giẫm chân nhau

> Mỗi feature chạy trong 1 git worktree riêng (thư mục + branch riêng), land vào `main` bằng squash.
> File dùng chung chỉ sửa trên `main`; log toàn vault ghi theo mảnh nên không bao giờ xung đột.

## 1. Vòng đời 1 feature

```bash
_scripts/wt.sh new  <feature>   # ../invlogis-wt/<feature> trên branch feat/<feature>, tách từ main
# mở phiên Claude TẠI thư mục worktree đó, làm việc, commit trong worktree
_scripts/wt.sh sync <feature>   # (tuỳ) kéo main mới nhất vào khi main có thay đổi dùng chung cần dùng
_scripts/wt.sh ready <feature> "<tóm tắt>"   # báo xong → backlog có task 🔍 chờ duyệt (Mục 4)
# ── chỉ sau khi người dùng duyệt task 🔍 ──
_scripts/wt.sh land <feature>   # từ checkout chính: squash vào index của main
_scripts/wt.sh drop <feature>   # xoá worktree + branch; từ chối nếu còn file chưa land
_scripts/wt.sh list             # worktree nào còn commit / file chưa land
```

- Land luôn là **squash** (giữ lịch sử `main` gọn, không kéo lịch sử nháp vào). Sync chiều main → feature
  dùng merge thường.
- Script **không commit, không push**. Commit do người dùng hoặc Claude sau khi người dùng duyệt (Mục 4);
  push luôn do người dùng (`block-push.sh`).
- Worktree tạo từ commit `main` gần nhất — thay đổi chưa commit ở `main` KHÔNG đi theo. Commit `main` trước.
- Slug worktree = slug feature (`docs/{feature}/`). Việc không gắn feature (sửa skill, đợt dọn) dùng slug
  mô tả việc, vd `skill-figma-screen`.

## 2. Ai được sửa gì

| Vùng | Trong worktree feature | Trên `main` |
|---|---|---|
| `docs/{feature}/**` của chính feature đó | ✅ | ✅ |
| `docs/{feature-khác}/**` | ❌ — mở worktree của feature kia | ✅ |
| `docs/_shared/**`, `docs/_product/**`, `design/**` | ❌ | ✅ |
| `.claude/**`, `CLAUDE.md`, `AGENTS.md`, `_scripts/**`, `_templates/**` | ❌ | ✅ |
| `_workspace/backlog.md`, `docs-input/README.md` | ❌ (hook tự chạy `--dry-run`) | ✅ (hook ghi) |
| `_workspace/decisions.md` | ❌ — ghi vào doc feature, chép sang sổ sau khi land | ✅ |
| `docs/_shared/dashboard*.html` | ❌ | ✅ — dựng lại sau land |
| Log mảnh `_workspace/{changelog,staleness}.d/` | ✅ (hook tự ghi) | ✅ |

Feature cần sửa vùng ❌ → dừng, ghi vào báo cáo/task "cần sửa trên main: …". Sửa trên `main`, commit,
rồi `wt.sh sync <feature>`. KHÔNG sửa tạm trong worktree "rồi tính sau" — đó chính là xung đột khi land.

> Ngoại lệ: hook `post-edit-stale.sh` có thể đánh `status: stale` doc downstream ở feature khác. Đây là
> thay đổi frontmatter 2 dòng, merge thường tự gộp được; nếu land báo xung đột ở đó thì giữ bản `stale`.

## 3. File sinh ra (không commit)

| File | Nguồn | Dựng lại khi |
|---|---|---|
| `_workspace/changelog.md` | `_workspace/changelog.d/*.md` | mỗi lần hook ghi, mở phiên, sync/land |
| `_workspace/staleness.md` | `_workspace/staleness.d/*.md` | như trên |
| `_workspace/kg/graph*.json` | `docs/**` | lazy — `kg-query` tự build khi thiếu hoặc có `.dirty` |

- Mảnh tên `{YYYY-MM-DD}--{branch}.md`, mỗi dòng 1 sự kiện. 2 branch không bao giờ ghi chung 1 mảnh →
  land chỉ là thêm file. `0000-history.md` = log trước khi tách mảnh (2026-10-13).
- Đọc log vẫn đọc file tổng như trước (`grep "docs/{feature}/" _workspace/changelog.md`). Thiếu hoặc nghi cũ →
  `python3 _scripts/logbook.py build`.
- KHÔNG sửa tay file tổng (lần dựng sau ghi đè) và không sửa tay mảnh (writer duy nhất là hook).

## 4. Duyệt land qua backlog

Land là cửa duyệt cuối của 1 feature — **không bao giờ tự chạy**. Đi qua backlog để người dùng chọn lúc nào xem:

1. **Báo xong** — làm xong trong worktree, commit hết, chạy `_scripts/wt.sh ready <feature> "<tóm tắt 1 dòng>"`.
   Máy ghi dấu ready + SHA lúc báo vào git config của branch; `intake-sync` sinh task
   `🔍 chờ duyệt | Duyệt + land feat/<feature> — <tóm tắt>`, Xong khi `!branch:feat/<feature>`.
   Commit trung gian KHÔNG sinh task — chỉ `ready` mới sinh.
2. **Review** — người dùng chọn task ("review BL-NNN"). Claude trình trong chat, KHÔNG chạy lệnh ghi nào:
   commit (`git log main..feat/x`), file đổi (`git diff --stat main...feat/x`), kết quả gate/test đã chạy,
   điểm cần người soi (quyết định nghiệp vụ mới, câu hỏi mở, chỗ đụng vùng ❌ Mục 2 nếu có).
3. **Duyệt** — người dùng nói rõ "duyệt"/"land". Claude chạy `wt.sh land` → in `git diff --cached --stat` →
   commit (message tóm tắt feature) → `wt.sh drop`. Task tự ✅ khi branch mất. Người dùng bảo "sửa: …" →
   `wt.sh unready`, sửa trong worktree, `ready` lại.

| Trạng thái task | Nghĩa |
|---|---|
| `🔍 chờ duyệt` | Đang chờ người dùng review, nội dung đúng bản đã báo |
| `🔍 ⚠ có commit mới sau khi báo ready` | Worktree đổi sau khi báo — review phải xem bản mới hoặc `ready` lại |
| `⬜ đang sửa lại` | Đã `unready`, quay lại làm |
| `✅` | Đã land + drop |

- Không có task 🔍 tương ứng hoặc người dùng chưa nói duyệt → KHÔNG land, kể cả khi được nhờ "làm nốt".
- Dashboard (BL-088) gom task 🔍 thành làn "Chờ bạn".

## Tóm tắt 1 dòng

> **1 feature = 1 worktree `feat/<slug>` · chỉ sửa `docs/<slug>/**`, đồ dùng chung sửa trên main rồi sync ·
> xong thì `ready` → task 🔍 trong backlog → người dùng review + duyệt → mới land (squash) + drop ·
> log ghi theo mảnh, file tổng là file sinh ra.**
