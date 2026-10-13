---
name: board
description: Đã gộp vào /dashboard (tab Luồng việc) — gõ /board hay /board sync sẽ chạy /dashboard hoặc /dashboard sync.
allowed-tools: Read, Bash, Skill
user-invocable: true
argument-hint: "publish | sync"
---

# /board — đã gộp vào /dashboard (14/10/2026)

Board kéo-thả cũ (artifact `Mct3oujnZQG9agD9EdUezq`, trang `_workspace/board/index.html`) **không còn cập nhật**.
Cùng dữ liệu và cùng 3 thao tác kéo giờ nằm ở **tab Luồng việc** của trang dashboard (link trong
`.claude/state/dashboard.json`). Lý do gộp: 2 trang có thao tác + 2 lệnh sync là thừa; user chọn gộp (hướng B, 14/10).

| Gõ | Chạy |
|---|---|
| `/board` hoặc `/board publish` | `/dashboard` (build + audit + publish trang có tab Luồng việc) |
| `/board sync` | `/dashboard sync` (áp yêu cầu `board-move` cùng các yêu cầu khác) |
| `/loop 5m /board sync` | đổi thành `/loop 5m /dashboard sync` |

## Approach

1. Báo 1 dòng: "/board đã gộp vào /dashboard (tab Luồng việc)."
2. Gọi skill `dashboard` với tham số tương ứng bảng trên (Skill tool).

## References

- @../dashboard/SKILL.md
