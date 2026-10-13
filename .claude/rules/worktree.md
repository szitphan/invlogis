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
_scripts/wt.sh land <feature>   # từ checkout chính: squash vào index của main — người dùng tự commit
_scripts/wt.sh drop <feature>   # xoá worktree + branch; từ chối nếu còn file chưa land
_scripts/wt.sh list             # worktree nào còn commit / file chưa land
```

- Land luôn là **squash** (giữ lịch sử `main` gọn, không kéo lịch sử nháp vào). Sync chiều main → feature
  dùng merge thường.
- Script **không commit, không push**. Commit thủ công; push do người dùng (`block-push.sh`).
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

## Tóm tắt 1 dòng

> **1 feature = 1 worktree `feat/<slug>` · chỉ sửa `docs/<slug>/**`, đồ dùng chung sửa trên main rồi sync ·
> land = squash, người dùng commit · log ghi theo mảnh, file tổng là file sinh ra.**
