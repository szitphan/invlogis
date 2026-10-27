---
type: design-component
status: draft
updated: 2026-10-27
links:
  - design/v2/vehicles.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - _workspace/decisions.md
---

# Container Slot

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Container Slot` (6797:15876), trang
> DS · Application components, Section `Container slot` 6798:15913, Demo 6798:15921 · Badge (6657:165736) ·
> DEC-267, DEC-271

Một vị trí container trên mooc trong sơ đồ khe (cách B của tổ hợp, `design/v2/vehicles.md` mục 5). Mang cỡ, số
container, trạng thái vị trí (độc lập trạng thái Lệnh, `transport-dispatch` F11), lạnh, và mã Lệnh khác khi ghép hàng.
Một component cho web và app.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng trong Combo Slots (chi tiết Lệnh, form xếp tổ hợp, thẻ Lệnh app, popup bản đồ). Đứng riêng khi cần nói về một
  container (danh sách container của Lệnh).
- Khối cha chia bề ngang: **20 = 1 phần, 40/45 = 2 phần**; 1×20 trên mooc 40 đặt giữa, hai bên để trống.
- Số container hiển thị `AAAA 123456 7` (4 chữ · 6 số · chữ số kiểm); nhập thì kiểm chữ số cuối ISO 6346 (F10).

### Cấu tạo

| Phần | Nội dung | Token |
|---|---|---|
| Ô | lề 10 × 8, khoảng 4, rộng FILL | `color/bg/surface` · `color/border/default` · `radius/inner` |
| `Top` | `Size label` ("20'", "45' · lạnh") + `Order` ("· LVT-0450", ẩn mặc định) | `type/caption` · `color/text/secondary` / `tertiary` |
| `Number` | số container | `type/code` · `color/text/primary` |
| `Chips` | Badge `Status` (Pill Color SM) + Badge `Reefer` (Teal, "Lạnh -18 °C"); xuống hàng khi hẹp | Badge |

### Biến thể

| State | Nhãn | Badge | Khác gì |
|---|---|---|---|
| No Number | Chưa có số | Gray | viền đứt `color/border/strong`; chữ "Chưa có số" thay số |
| Empty | Vỏ rỗng | Blue | — |
| Loading | Đang đóng | Yellow | có hàng, chưa niêm chì |
| Loaded | Có hàng | Green | đã niêm chì |
| Swapping | Đang đổi vỏ | Orange | số cũ gạch ngang + "chờ số mới" |
| Held | Kiểm hoá | Purple | hải quan giữ, tổ hợp chờ |
| Dropped | Đã hạ | Gray | nền trong suốt, viền đứt, số màu tertiary; container còn thuộc Lệnh |

| Density | Khi nào |
|---|---|
| Default | chi tiết Lệnh, form, thẻ app |
| Compact | không có chip trạng thái (cột danh sách mở rộng, popup bản đồ); chip Lạnh chỉ hiện khi bật Reefer |

14 biến thể. Màu Badge là đề xuất (DEC-271), lab chỉ có màu cho 4 trạng thái đầu.

### Nên và không nên

- Nên: luôn có chữ trạng thái (không chỉ màu); giữ số cũ khi đổi vỏ để đối chiếu.
- Không nên: dùng màu trạng thái Lệnh cho vị trí container; tự co cỡ chữ số container.

### Trợ năng — chấm theo WCAG 2.2

- 1.4.1: trạng thái có chữ; Swapping có chữ "chờ số mới" ngoài gạch ngang. Tên truy cập = "Size label, Number, Status".
- Số container đọc từng nhóm (trình đọc màn hình): đặt `aria-label` dạng "T G H U 123456 7" khi cần.

### Thuộc tính

TEXT `Size label` · `Number` · `Order` · BOOLEAN `Has Order` · `Reefer` · VARIANT `State`, `Density` · đưa ra panel:
`Status`, `Reefer` (đổi nhiệt độ).

### Thành phần lồng

Badge ×2 (Pill Color SM, tắt X Close / Count / Icon).

### Được dùng trong

Demo `Chi tiết lệnh / Web` (2×20 ghép 2 Lệnh), `Lệnh của tôi / Mobile` (45' lạnh). Sẽ dùng trong Combo Slots.

### Kiểm máy

27/10: kiểm tên fail 0. Đã sửa: hàng khe cao cố định cắt ô; Compact còn hàng chip rỗng. Kiểm mất hình: chưa chạy.
Dark: chưa điền giá trị Dark.

## Mobile

> Mode Platform = Mobile, cùng component và số đo. Trên thẻ Lệnh app thường đặt một khe một hàng (FILL).

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
