---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Base / Status Chip

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Status Chip` (6385:630, trang L1 · Base), khung
> tài liệu cạnh component (hình nên / không nên, cấu tạo phóng 2×) · DEC-130, DEC-180, DEC-200

## Khi dùng

- **Soft** (nền nhạt + icon): trạng thái chính của bản ghi, ở bảng web, thẻ, đầu trang chi tiết. Mỗi bản ghi chỉ một chip
  Soft.
- **Dot** (chấm + chữ): trạng thái phụ (thanh toán, đồng bộ, GPS) và chỗ dày chữ (lịch sử, dòng thời gian).
- **Tone:** 8 sắc cố định, không đổi theo khách. Nghĩa của từng sắc gán ở L2, nhãn lấy nguyên văn từ
  `docs/{feature}/srs/{feature}-states.md`.
- **Icon:** chọn theo nghĩa trạng thái (xong, chờ, lỗi…). Dot không có icon.
- Chip không bấm được. Cần lọc hoặc chọn thì dùng tab chip hoặc ô chọn, không dùng Status Chip.

## Nên và không nên

Hình minh hoạ ở khung tài liệu cạnh component trên Figma.

1. **Nên:** một chip Soft cho trạng thái chính, trạng thái phụ dùng Dot. **Không nên:** hai, ba chip Soft cạnh nhau trên
   một thẻ.
2. **Nên:** chữ ngắn, viết hoa chữ đầu ("Đang vận chuyển"). **Không nên:** viết hoa toàn bộ, hoặc chỉ có màu không có chữ.

## Trạng thái

Chip chỉ hiển thị, không có Hover, Pressed, Focus, Disabled. Biến thể là Type (Soft, Dot) × Tone (8 sắc), cỡ app 26, web
24 (`chip/height`, DEC-200).

## Chữ trên chip

1–3 từ, viết hoa chữ đầu, đúng nhãn trong `states.md`. Chữ dài thì cắt bằng "…" và hiện đủ khi rê chuột (web) hoặc ở trang
chi tiết.

## Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | Kết quả |
|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ chữ Soft trên nền chip từ 4,88 (Orange) đến 7,06 (Gray); chữ Dot 17,73 |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ chấm Dot trên trắng từ 5,18; nền Soft 1,06–1,18 là trang trí, chữ đủ để đọc |
| 1.4.1 Không chỉ dùng màu | ✓ luôn có chữ; Soft thêm icon |
| 1.4.12 Giãn chữ | Lưu ý: chữ bị cắt "…" phải có chỗ xem đủ (tooltip web, trang chi tiết) |
| 4.1.2 Tên, vai trò | Chip là chữ thường, không phải nút; icon đặt `aria-hidden` |
| **Điểm** | **4/5 đạt** · 1 lưu ý: chỗ xem đủ chữ bị cắt |

## Dùng ở đâu

Thẻ lệnh, bảng web, đầu trang chi tiết, dòng lịch sử (màn mẫu Câu 8d); sau này là mọi component L2 có trạng thái.

## Tên trong code

`<StatusChip variant="soft|dot" tone="gray|blue|teal|purple|yellow|green|red|orange" icon={…}>Đang vận chuyển</StatusChip>`;
biến CSS `--color-chip-{tone}-bg|fg` (màu), `--chip-*` (cao, lề, khoảng, chấm), `--radius-chip`, `--icon-size-chip`.

## Cấu tạo, thuộc tính, token

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Status Chip` (6385:630) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Label | Chữ | Trạng thái | — |
| Icon | Đổi component | icon/circle-check · Size=14 | — |
| Type | Biến thể | Soft | Soft · Dot |
| Tone | Biến thể | Gray | Gray · Blue · Teal · Purple · Yellow · Green · Red · Orange |

16 biến thể · trục Type × Tone.

### Màu theo phần (token)

| Type | Tone | Nền | Chữ | Icon |
|---|---|---|---|---|
| Soft | Gray | `color/chip/gray/bg` | `color/chip/gray/fg` | `color/chip/gray/fg` |
| Soft | Blue | `color/chip/blue/bg` | `color/chip/blue/fg` | `color/chip/blue/fg` |
| Soft | Teal | `color/chip/teal/bg` | `color/chip/teal/fg` | `color/chip/teal/fg` |
| Soft | Purple | `color/chip/purple/bg` | `color/chip/purple/fg` | `color/chip/purple/fg` |
| Soft | Yellow | `color/chip/yellow/bg` | `color/chip/yellow/fg` | `color/chip/yellow/fg` |
| Soft | Green | `color/chip/green/bg` | `color/chip/green/fg` | `color/chip/green/fg` |
| Soft | Red | `color/chip/red/bg` | `color/chip/red/fg` | `color/chip/red/fg` |
| Soft | Orange | `color/chip/orange/bg` | `color/chip/orange/fg` | `color/chip/orange/fg` |
| Dot | Gray | trong suốt | `color/text/primary` | `color/chip/gray/fg` |
| Dot | Blue | trong suốt | `color/text/primary` | `color/chip/blue/fg` |
| Dot | Teal | trong suốt | `color/text/primary` | `color/chip/teal/fg` |
| Dot | Purple | trong suốt | `color/text/primary` | `color/chip/purple/fg` |
| Dot | Yellow | trong suốt | `color/text/primary` | `color/chip/yellow/fg` |
| Dot | Green | trong suốt | `color/text/primary` | `color/chip/green/fg` |
| Dot | Red | trong suốt | `color/text/primary` | `color/chip/red/fg` |
| Dot | Orange | trong suốt | `color/text/primary` | `color/chip/orange/fg` |

### Số đo theo phần (token)

| Type | Cao | Rộng | Lề trái | Lề phải | Khoảng giữa | Bo | Cỡ icon |
|---|---|---|---|---|---|---|---|
| Soft | `chip/height` | ôm nội dung | `chip/padding-x-icon` | `chip/padding-x` | `chip/icon-gap` | `radius/chip` | `icon/size/chip` |
| Dot | `chip/height` | ôm nội dung | 0 | 0 | `chip/dot-gap` | 0 | `chip/dot-size` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label (Soft) | `type/caption-strong` |
| Label (Dot) | `type/caption` |

<!-- auto:end -->
