---
paths:
  - "docs/**/*.md"
  - ".claude/hooks/**"
---

# Status Lifecycle‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## Doc statuses‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

```
draft → in-review → revisions → approved → shipped
                       ↑           ↓
                       └───────────┘
```

| Status | Meaning |
|--------|---------|
| `draft` | Initial creation, work in progress, not yet shared |
| `in-review` | Sent for review (stakeholders or `@reviewer-agents`) |
| `revisions` | Reviewer flagged issues, doc needs rework |
| `approved` | Reviewer accepted, frozen for development |
| `shipped` | Feature delivered to production |
| `stale` | __Cross-cutting__ (ngoài luồng tuyến tính): upstream đổi làm doc này có thể lỗi thời. **Set bởi hook `post-edit-stale.sh`** (reverse-graph scan `links:`), hook lưu status cũ vào `status_prev`. Không phải bước tiến; review upstream (đọc prose, hoặc `/cr` nếu cần sửa) rồi thoát: không cần sửa → `/status restore` (về `status_prev`); cần sửa → `/status <doc> revisions`. `/jira --push` HARD GATE khi gặp `stale`. |

Loops:
- `in-review → revisions → in-review` is a normal review cycle
- After enough cycles, `revisions → approved`‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
- `stale` phủ lên bất kỳ status nào (draft/approved/shipped) khi upstream đổi — status gốc giữ ở `status_prev`, chỉ đánh dấu cần review lại.

## Chuyển hợp lệ (thực thi bởi `/status`)

Đổi status qua `/status` — engine `.claude/skills/status/engine/status.py` (bảng `TRANSITIONS` phải khớp bảng này).

| Từ | Được sang |
|---|---|
| `draft` | `in-review` |
| `in-review` | `revisions`, `approved`, `draft` (rút lại) |
| `revisions` | `in-review`, `approved`, `draft` |
| `approved` | `shipped`, `revisions` (mở lại) |
| `shipped` | `revisions` |
| `stale` | `revisions`, hoặc `restore` về `status_prev` |

- Sang `approved`/`shipped` khi có upstream (doc trong `links:` có status) chưa `approved`/`shipped` → **cảnh báo + hỏi user**, user đồng ý mới chuyển (không chặn cứng).
- Đổi status không đổi `updated:` và không lan stale xuống downstream (không phải đổi nội dung).
- Ngoài lifecycle: `_workspace/` (backlog, changelog, log máy), `docs/exports|inbox|_reverse`, doc có lifecycle riêng (CR, meeting).
- Giới hạn hiện tại của hook stale: chỉ lan **1 tầng**; sửa file trong `docs/_shared/` hoặc ngoài `docs/` (vd `design/`) **không** lan. `/status impact <file>` cho thấy đủ các tầng + tầng nào hook không tự đánh.

## Transitions trigger automation‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| Transition | Action |
|------------|--------|
| `* → in-review` | (future) Notify reviewer agent specified in frontmatter `reviewers:` |
| `* → approved` | Xem trạng thái tổng hợp qua `/dashboard` (KHÔNG có file `docs/feature-list.md` — đã bỏ) |
| `* → shipped` | (future) Trigger `@gap-analyst` for cross-doc consistency check |

## Other doc types‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

### Meeting‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
```
captured → processed
```
- `captured` = raw notes
- `processed` = decisions/blockers/action items structured into tables within the meeting note itself (no separate files — see `feedback_meet_consolidated`)

## Frontmatter format‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

```yaml
---
status: draft               # required
status_prev: approved       # chỉ có khi status = stale — hook post-edit-stale.sh ghi, /status restore xoá
status_changed: 2026-05-09  # optional, /status ghi khi chuyển
status_reason: "Awaiting input from client on payment provider"   # optional, /status ghi khi có lý do
---
```


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
