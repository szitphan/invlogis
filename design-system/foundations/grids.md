---
type: design-foundations
status: approved
updated: 2026-11-03
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Lưới, độ rộng, breakpoint

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (7.x) để các DEC và spec trích "foundations mục 7…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 7. Lưới, độ rộng, breakpoint (DEC-324, DEC-038, DEC-039)

| Màn | Cột | Rãnh | Lề | Rộng tối đa |
|---|---|---|---|---|
| Web ≥ 1024 | 12 | 32 | 32 | 1280 gồm cả lề cho màn chi tiết, form; màn bảng trải hết |
| Tablet 768–1023 | 6 | 32 | 32 | — |
| App (khung 393) | 4 | 16 | 16 | Không chặn, trải đủ bề rộng máy |

- **Vùng tính lưới web:** vùng sau menu trái, 12 cột giữ nguyên ở mọi khung web.
- **Rộng tối đa 1280** đã gồm lề 32 hai bên, nội dung còn 1216, cột 72 như Untitled. Giới hạn chỉ chạm tới khi màn đủ rộng cho menu cộng 1280.
- **Khối cấp màn canh đúng cột**, cách nhau theo rãnh `grid/gutter`. Thẻ, dòng trong một khối dùng `layout/list-gap`.
- Màn chi tiết web chia **8 cột nội dung + 4 cột thông tin** như Jira (DEC-127).
- Viền 1px của thẻ nằm trong khung, không cộng vào lề (Figma stroke Inside; CSS `box-shadow: inset 0 0 0 1px`).
- App bỏ hẳn đường K, không có luật canh chữ theo cột (DEC-341 sp11, `spacing.md` mục 6). Lưới app chỉ canh khối.

### Khung vẽ và khung kiểm

| Nền tảng | Vẽ | Kiểm thêm |
|---|---|---|
| Web | 1920, menu mở | 1280 và 1024 cho mỗi kiểu bố cục; mobile web 393 cho màn đại diện (user chốt 15/10) |
| App | 393 | Máy 320: chữ dài, nút, bảng thẻ |

Khung kiểm web đổi 1440 thành 1280 và 1024 vì đó là chỗ dễ vỡ nhất; `figma-screen` đã đổi theo.

### Độ rộng

Một giá trị dùng chung cho web và app, trùng cả tên lẫn số với Untitled (`width/*` trong Primitives):

| Token | Giá trị | Dùng cho |
|---|---|---|
| `width/xxs` | 320 | Popover, menu thả rộng, Tooltip Supporting, ô nhập web |
| `width/xs` | 384 | Dialog xác nhận, drawer thường |
| `width/sm` | 480 | Chưa có vai cố định |
| `width/md` | 560 | Dialog form, form 1 cột |
| `width/lg` | 640 | Chưa có vai cố định |
| `width/xl` | 768 | Chưa có vai cố định |
| `width/2xl` | 1024 | Drawer rộng |
| `width/3xl` | 1280 | Khung nội dung tối đa web |
| `width/4xl`, `5xl`, `6xl` | 1440 · 1600 · 1920 | Chưa có vai cố định |

- **Khối rộng từ `width/xs` trở lên** không vượt quá bề rộng màn trừ hai lề: `max-width: calc(100% - 2 * var(--grid-margin))`.
- **Đoạn văn tối đa** `width/paragraph-max` trỏ `width/md` 560, vì chữ thân của mình cỡ 14 (Untitled 720 cho chữ 16). Lớp `.prose` đọc biến này.
- **Số riêng** không mượn bậc trùng số: `vehicle/q-lg-w` 480, `header-nav/account-menu-width` 256, `command-search/width` 600 giữ ở token component.
- **Ô nhập, thanh tiến độ trên app** (`field/width-default`, `progress/width-default`) trải theo màn trừ lề; 361 chỉ là kết quả trên khung 393.

### Container và token lưới

| Token | Web | App | Ghi chú |
|---|---|---|---|
| `container/padding-mobile` | 16 | 16 | Tên Untitled |
| `container/padding-desktop` | 32 | 32 | Tên Untitled, áp từ 768 |
| `container/max-width-desktop` | `width/3xl` | không đọc | Tên Untitled |
| `grid/columns` | 12 | 4 | Tablet 6 cột ghi ở `grid.tablet` của `tokens.json` |
| `grid/gutter` | `space/32` | `space/16` | Rãnh cấp màn |
| `grid/margin` | `container/padding-desktop` | `container/padding-mobile` | Component và màn đọc token này làm lề màn |

Figma: ba token `grid/*` đi kèm layout guide style.

### Khung cuộn có thanh dính

Khung cuộn đặt `scroll-padding` = chiều cao thanh dính + 4, để phần tử nhận focus không nằm dưới thanh (WCAG 2.4.11, DEC-339). Không thêm token, số tính từ token của thanh: web `header-nav/height` 44 + 4 = 48; cộng thêm cao tiêu đề bảng dính nếu có. Chân màn app có nút dính thì đặt `scroll-padding-bottom` theo cùng cách.

### Breakpoint

xxs 320 · xs 600 · sm 640 · md 768 · lg 1024 · xl 1280 · 2xl 1536. Biến `--bp-*` chỉ để tra, media query ghi số trực tiếp.

**Mốc thiết kế chỉ có ba:** 768 (lên bố cục web, thu menu) · 1024 (lên 12 cột) · 1280 (mở menu). Bốn mốc còn lại giữ cho code. Từ 768 tới 1279 menu trái thu còn 64 (cột icon), bấm thì bung đè lên nội dung.
