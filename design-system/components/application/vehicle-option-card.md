---
type: design-component
status: stale
status_prev: draft
updated: 2026-11-02
links:
  - design-system/foundations/vehicle.md
  - design-system/components/application/vehicle-thumb.md
  - design-system/components/application/vehicle-card.md
  - _workspace/decisions.md
---

# Vehicle Option Card

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Vehicle Option Card` (6794:14809) và
> `Vehicle Option Card / Mobile` (6794:14992), trang DS · Application components, Section `Vehicle option card`
> 6795:15459, Demo 6795:15468 · lồng `Vehicle Thumb` (6787:12415), Badge (6657:165736), Radio (6657:167122) ·
> DEC-237, DEC-270, DEC-334

Dòng chọn một phương tiện trong danh sách: ảnh thu nhỏ, biển số, trạng thái + tải trọng · lái xe, Radio bên phải.
Hai component vì app không có Hover.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng ở: form xếp xe cho Lệnh, drawer / popover chọn đầu kéo, mooc, xe tải. Chọn một (Radio); cả dòng bấm được.
- Xem nhiều thông tin (ODO, vị trí, tuyến) thì dùng Vehicle Card.
- Xe không khả dụng vẫn hiện, ở State **Disabled** (không chọn được), Badge ghi trạng thái, Meta ghi chỗ + hạn
  ("Xưởng Đình Vũ · tới 30/10"); không làm mờ ảnh (DEC-269).

### Cấu tạo

| Phần | Nội dung | Token |
|---|---|---|
| Dòng | lề 16 × 12, khoảng 12, viền dưới 1; trải theo khối chứa, không có rộng cố định (DEC-334 vh07); phẳng, không bóng (vh06) | `color/bg/primary` · `color/border/secondary` |
| Ảnh `Thumb` | Vehicle Thumb SM 48 (đổi Group trên panel) | `size/6xl` |
| Biển số `Plate` | 1 dòng, cắt "…" | `type/heading` · `color/text/primary` |
| Dòng phụ `Sub` | Badge `Status` (Pill Color SM) + `Meta` (tải trọng · lái xe), khoảng 8; Meta tối thiểu 140, không đủ chỗ thì xuống dưới Badge ở mọi nền tảng, 1 dòng cắt "…" | `type/caption` · `color/text/tertiary` |
| Chọn | Radio MD của Base, Checked theo Selected | Radio |

### Biến thể

| Trục | Giá trị | Khác gì |
|---|---|---|
| Selected | False · True | True: nền `color/bg/selected`, Radio Checked |
| State | Default · Hover · Pressed · Focus · Disabled | Hover nền `color/bg/primary_hover` · Pressed nền `color/bg/secondary` · Focus vòng ngoài 2 cách 2 `color/focus/ring` (DEC-339) · Disabled chữ `color/text/disabled`, Radio Disabled; Disabled chỉ đi với Selected = False |

9 biến thể.

### Trạng thái nội dung

| Ca | Cách đặt |
|---|---|
| Sẵn sàng | Status "Sẵn sàng hoạt động" (Green) |
| Đang chạy Lệnh khác | Status "Đang hoạt động" (Blue) — vẫn chọn được; cảnh báo trùng Lệnh do form quyết |
| Chưa gán lái xe | Meta "15 tấn · Chưa gán lái xe" |
| Không khả dụng | State Disabled, Status "Đang sửa chữa" (Yellow) / "Đang tạm giữ" (Gray), Meta chỗ + hạn |
| Không cần trạng thái | tắt Has Status |

Màu Badge theo DEC-269 (đề xuất, chưa chốt).

### Kích thước

Cao theo nội dung. Trong drawer `width/xs` 384 (lề drawer 24 × 2 là giả định, chưa có spec drawer): 336 − lề 32 − ảnh 48 −
Radio 20 − 2 khoảng 12 = 212, nhỏ hơn Badge 132 + 8 + Meta 140 = 280, nên dòng phụ luôn xuống hàng. Chữ không mất, dòng cao thêm.

### Nên và không nên

- Nên: sắp xe khả dụng lên trên, Disabled xuống cuối; một Size ảnh trong một danh sách.
- Không nên: ẩn xe không khả dụng (người điều phối cần biết vì sao không có xe); thêm nút trong dòng.

### Trợ năng — chấm theo WCAG 2.2

- Nhóm là radiogroup, mỗi dòng là radio; tên truy cập = "Plate, Status, Meta". 2.5.8 Vùng chạm: dòng ≥ 72 cao.
- 2.4.7 Focus: vòng ngoài 2 cách 2 `color/focus/ring`, cùng một vòng với nút (DEC-339). 1.4.1: trạng thái có chữ; Disabled có lý do bằng chữ ở Meta.

### Thuộc tính

TEXT `Plate` · `Meta` · BOOLEAN `Has Status` · VARIANT `Selected`, `State` · đưa ra panel: `Thumb`, `Status`.

### Thành phần lồng

Vehicle Thumb (SM) · Badge (Pill Color SM, tắt X Close / Count / Icon) · Radio (Size MD).

### Được dùng trong

Demo `Xếp xe cho lệnh / Web`, `Chọn đầu kéo / Mobile`.

### Kiểm máy

27/10: kiểm tên fail 0 · 0 màu gõ tay. Chữ dài ở 420 và 320: biển số, Meta cắt "…", Badge giữ nguyên. Kiểm mất hình:
chưa chạy. 02/11: spec theo DEC-334, Figma chưa sync.

### Dark

Nền ô ảnh và nét bao theo Vehicle Thumb. Dòng phẳng ở cả hai chế độ. Phần còn lại chưa có số đo Dark.

## Mobile

>
> Component `Vehicle Option Card / Mobile`, mode Platform = Mobile. Giống Web, khác: trải theo màn; không có Hover
> (State Default · Pressed · Disabled, 5 biến thể; app không vẽ Focus, DEC-339); dòng phụ thường xuống hàng (Badge trên, Meta dưới) nên dòng
> cao ≈ 91.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
