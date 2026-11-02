---
type: design-component
status: draft
updated: 2026-11-02
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/foundations/icon-sets.md
  - design-system/tokens.json
  - _workspace/decisions.md
---

# QR code

> Base · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma: `QR code` `7171:1775` · DEC-335 ms08 · chưa có trang duyệt

Hiện một mã QR để người khác quét. Nhóm A: một bộ cho web và app, cùng số. Theo `shared-assets/qr-code.tsx` của Untitled, bỏ
phần trang trí của màn giới thiệu.

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Một chỗ dùng duy nhất:** biên bản giao nhận. Không có màn dùng nào khác; màn khác cần mã thì mở lại quyết định.
- **Mã thật do code sinh** từ nội dung truyền vào. Không vẽ tay trong sản phẩm. Figma dùng hình mẫu không quét được, chỉ để xem bố cục.
- **Chỉ hiện mã ra.** Quét mã vào là màn camera, dùng 3 icon Lucide theo [icon-sets.md](../../foundations/icon-sets.md), không dùng component này.

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Khung MD | lề `space/md`, mã `size/9xl` | lề 8, mã 96 |
| Khung LG | lề `space/lg`, mã `size/10xl` | lề 12, mã 128 |
| Nền khung | `color/bg/primary`, khung khoá mode Light | trắng cố định, không đổi theo chế độ |
| Mô-đun mã | `color/fg/primary`, khung khoá mode Light | #171717 |

**Khoá mode Light là bắt buộc:** ở Dark `color/fg/primary` là trắng, mã sẽ trắng trên trắng. Code đặt `data-theme="light"` trên
khung; Figma đặt mode Semantic = Light trên khung.

### Biến thể

`Size` = MD · LG.

### Trạng thái

| Trạng thái | Cách hiện |
|---|---|
| Có nội dung | Mã |
| Chưa có nội dung | Không hiện component; màn chứa nó tự ghi lý do |

Không có rê chuột, bấm, tắt.

### Kích thước

MD 96, LG 128 là cỡ mã, chưa tính lề. Không co giãn theo màn và không đổi theo Platform. Chữ dài: không áp, component không có chữ.

### Nên và không nên

- Nên: giữ nền trắng ở cả chế độ Tối.
- Không nên: đặt logo giữa mã, đổi màu mã theo màu khách, dùng làm trang trí.

### Trợ năng — chấm theo WCAG 2.2

- 1.1.1: khung mang `role="img"` và tên nói mã dùng để làm gì, vd "Mã QR biên bản giao nhận".
- 1.4.11: mô-đun trên nền 17,93:1 ở mọi chế độ, ngưỡng 3:1.
- 1.4.1: không truyền nghĩa bằng màu.

### Thuộc tính

`Value` (nội dung mã, bắt buộc) · VARIANT `Size` · `Label` (tên cho trình đọc màn hình).

### Thành phần lồng

Không có.

### Được dùng trong

Biên bản giao nhận. Tài liệu `docs/_research/2026-10-02-electronic-delivery-record.md` ghi đây là lớp thêm khi khách xác nhận,
chưa vào phạm vi.

### Token

`space/md` · `space/lg` · `size/9xl` · `size/10xl` · `color/bg/primary` · `color/fg/primary`. Không thêm token.

### Kiểm máy

Chưa chạy, chưa có trang `_work`. Figma Size MD, LG: mã 96, 128, khung ngoài có lề 112, 152, khoá mode Light. Chưa quét thử mã thật ở cỡ 96 trên máy in và màn hình thật.

### Chuyển động

Không có.

## Mobile

> Mode Platform = Mobile, cùng component, cùng số.

### Tổng quan · Cấu tạo · Biến thể · Trạng thái · Kích thước · Nên và không nên · Trợ năng · Thuộc tính · Thành phần lồng · Token

Như Web.

### Được dùng trong

Biên bản giao nhận khi mở trên app.

### Kiểm máy

Như Web, chưa chạy.

## Đối chiếu Astryx

Astryx không có component hiện mã QR.

| Untitled (`shared-assets/qr-code.tsx`) | Bản này | Vì sao |
|---|---|---|
| Cỡ `md` 96 lề 8, `lg` 128 lề 12 | Giữ nguyên | DEC-335 ms08 |
| 4 góc khung và lớp sáng dần màu thương hiệu | Bỏ | Trang trí của màn giới thiệu, không cần trên biên bản |

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
