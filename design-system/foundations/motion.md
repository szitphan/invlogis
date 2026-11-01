---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Chuyển động

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (10.x) để các DEC và spec trích "foundations mục 10…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 10. Chuyển động (DEC-139)

Giữ như bộ cũ (`design/design.md` › Motion).

| Token | Giá trị | Dùng cho |
|---|---|---|
| `duration/fast` | 125ms | Vi tương tác: hover, pressed, đổi màu, bật/tắt Switch |
| `duration/medium` | 300ms | Vào/ra: Dialog, Popover, Toast, BottomSheet |
| `duration/slow` | 700ms | Chuyển động liên tục: skeleton pulse, chấm trạng thái nhấp nháy |
| `easing/standard` | cubic-bezier(0.24, 1, 0.4, 1) | Một đường cong cho mọi chuyển động; không bounce, không spring |

Transition theo từng thuộc tính (background, color, opacity, transform, box-shadow), không dùng `all`. Người dùng bật giảm chuyển động thì mọi thời gian về 0 (`tokens.css` đã có).

