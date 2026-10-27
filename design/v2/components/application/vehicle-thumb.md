---
type: design-component
status: draft
updated: 2026-10-27
links:
  - design/v2/vehicles.md
  - design/v2/handoff/vehicles.json
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Vehicle Thumb

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Vehicle Thumb` (6787:12415, trang
> DS · Application components, Section `Vehicle thumb` 6788:12444, Demo 6788:12452) · ảnh lồng `Vehicle Image`
> (6777:1914, trang DS · Foundations) · DEC-266, DEC-268

Ảnh thu nhỏ phương tiện trong ô vuông, cắt sẵn theo nhóm hình. Một component cho cả web và app: cỡ, bo, nền đọc
từ biến collection Platform và có **cùng số ở hai mode**, nên phần Mobile trỏ về phần Web.

## Web

> Khối Web đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- Dùng khi cần nhận ra **loại phương tiện** trong một chỗ nhỏ: dòng bảng, dòng danh sách, thẻ chọn, đầu thẻ bản ghi.
  Luôn đi kèm biển số hoặc mã bằng chữ; ảnh không thay chữ.
- **Group** = 22 nhóm hình chung (`design/v2/vehicles.md` mục 1). Tên xe của khách gán vào nhóm theo bảng của khách
  (`vehicles.json` → `tenants`); không có nhóm → `unknown`.
- Mỗi nhóm **cắt sẵn** phần nhận diện: đầu kéo, xe tải, container lấy đầu xe tràn mép phải; mooc lấy cụm bánh tràn
  mép trái; xe nâng, máy phát, trạm bơm lấy cả.
- Kiểu dáng phụ theo hãng: chọn trên ảnh lồng **Image → Style** (Alt 1…3), không thêm biến thể.

### Cấu tạo

| Phần | Token | Giá trị |
|---|---|---|
| Ô | `vehicle/thumb-xs` · `-sm` · `-md` | 32 · 48 · 64 |
| Bo góc | `vehicle/thumb-radius-xs` · `-sm` · `-md` | 6 · 8 · 10 |
| Nền | `color/bg/muted` | — |
| Ảnh | instance `Vehicle Image`, View = Q, cắt trong ô (clip) | đầu xe: chiều cao hình = 86% ô, đáy 96%, neo mép phải · mooc: cao hình 50% ô, đáy 88%, neo mép trái · thiết bị: vừa 84% × 80% ô, đáy 92%, căn giữa |
| Chưa xác định | viền `color/border/strong`, nét đứt 3/3, không ảnh | — |

### Biến thể

| Trục | Giá trị | Khi nào |
|---|---|---|
| Group | 22 nhóm (`tractor-1ax` … `unknown`) | theo nhóm hình của phương tiện |
| Size | XS · SM · MD | XS dòng bảng web · SM thẻ chọn, List Item · MD đầu thẻ bản ghi |

66 tổ hợp — vượt trần 30 của luật component, **ngoại lệ có chủ đích** (DEC-268): cắt sẵn từng nhóm để không ai
chọn sai cách cắt. Dev không dựng 66 biến thể: một component nhận `group` + `size`, đọc `thumb_crop` và khung hình từ
`vehicles.json`.

### Trạng thái

Ảnh tĩnh, không có trạng thái tương tác. Ảnh chưa tải xong hoặc lỗi → hiện ô nền muted trống (như `unknown` nhưng
không viền). Trạng thái chọn, rê chuột thuộc component chứa (Vehicle Option Card, List Item).

### Kích thước

Cố định theo Size; không kéo giãn. Cần cỡ khác → thêm Size ở component này, không resize instance.

### Nên và không nên

- Nên: đặt cạnh biển số / mã; dùng cùng một Size trong một danh sách.
- Không nên: dùng ảnh làm tín hiệu trạng thái (màu, mờ); đặt chữ đè lên ảnh; dùng Vehicle Image View Q trực tiếp
  trong ô nhỏ (không cắt, xe dài thành vệt mỏng).

### Trợ năng — chấm theo WCAG 2.2

- 1.1.1 Nội dung không phải chữ: ảnh trang trí khi đi kèm tên/biển số bên cạnh → `alt=""` (web), ẩn khỏi trình đọc
  màn hình (app). Đứng một mình (hiếm) → `alt` = tên nhóm hình.
- 1.4.11 Tương phản phi chữ: không áp (ảnh không mang thông tin bắt buộc).

### Thuộc tính

`Group` (VARIANT, 22) · `Size` (VARIANT, 3) · ảnh lồng `Image` đưa ra panel (đổi `Style`).

### Thành phần lồng

`Vehicle Image` (Foundations) — View = Q, Style mặc định Default.

### Được dùng trong

Demo `Danh sách phương tiện / Web` (XS) · `Chọn xe / Mobile` (SM). Sẽ dùng trong Vehicle Card, Vehicle Option Card.

### Token

`--vehicle-thumb-xs: var(--space-32)` · `--vehicle-thumb-sm: var(--space-48)` · `--vehicle-thumb-md: var(--space-64)` ·
`--vehicle-thumb-radius-xs: var(--radius-sm)` · `-sm: var(--radius-md)` · `-md: var(--radius-lg)` · nền `--color-bg-muted`.

### Kiểm máy

27/10: kiểm tên (DEC-264) fail 0 trên Section và Demo · 66/66 biến thể gắn biến cỡ, bo, nền. Chữ dài: không áp
(không có chữ). Dark: chưa điền giá trị Dark (architecture Mục 7). Kiểm mất hình `check-mat-hinh.js`: chưa chạy.

## Mobile

> Khối Mobile đặt mode Platform = Mobile. Mọi token có cùng số ở hai mode — đọc phần Web. Trên app thường dùng SM
> (dòng chọn xe) và MD (đầu thẻ); XS chỉ dùng ở bảng web.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
