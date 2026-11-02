---
type: design-component
status: stale
status_prev: draft
updated: 2026-11-02
links:
  - design-system/foundations/vehicle.md
  - design-system/components/application/vehicle-thumb.md
  - docs/vehicle-management/brainstorms/vehicle-management.md
  - _workspace/decisions.md
---

# Vehicle Card

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Vehicle Card` (6791:13702) và
> `Vehicle Card / Mobile` (6791:13823), trang DS · Application components, Section `Vehicle card` 6792:14479,
> Demo 6792:14488 · ảnh lồng `Vehicle Image` (6777:1914) · Badge của Base (6657:165736) · DEC-266, DEC-269, DEC-334

Thẻ phương tiện theo **mẫu 7** của lab thẻ phương tiện: chữ bên trái, ảnh 3/4 trước lấn ra mép phải, trạng thái ghim
góc phải trên, chân thẻ là lái xe và tuyến đang chạy. Hai component vì ô ảnh khác cỡ: web 160 × 100, app 140 × 88.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng ở: lưới danh sách đội xe, khối tóm tắt phương tiện trong chi tiết Lệnh, chọn xe khi điều phối (dạng xem nhiều
  thông tin). Chọn trong danh sách dài dùng Vehicle Option Card.
- Cả thẻ bấm được → mở chi tiết phương tiện. Không đặt nút trong thẻ.
- Trạng thái xe theo `vehicle-management` H2, nhãn nguyên văn: Sẵn sàng hoạt động · Đang hoạt động · Đang sửa chữa ·
  Đang tạm giữ.

### Cấu tạo

| Phần | Nội dung | Token |
|---|---|---|
| Khung | nền, bóng, viền 1, bo; cắt nội dung (vai Thẻ, DEC-327) | `color/bg/primary` · `shadow/xs` · `shadow/xs-border` · `radius/card` |
| Thân | lề 16 trái/trên, 12 dưới, 0 phải (ảnh lấn mép); khoảng 12 giữa chữ và ảnh | — |
| Biển số `Plate` | 1 dòng, cắt "…" | `type/heading` · `color/text/primary` |
| Dòng xe `Model` | 1 dòng, cắt "…" | `type/body` · `color/text/tertiary` |
| ODO · nhiên liệu `Odometer` | icon `gauge` + chữ, xuống dòng | `type/caption` · `color/text/tertiary`, icon `color/fg/tertiary` |
| Vị trí `Location` | icon `map-pin` + chữ, xuống dòng; tắt bằng Has Location | như trên |
| Ảnh `Media` | 160 × 100 cắt nội dung; Vehicle Image View Q phóng 125%, neo đáy phải; có nét bao theo hình (DEC-334 vh08) | `size/11xl` × `vehicle/q-sm-h` |
| Trạng thái `Status` | Badge Pill Color SM, ghim góc phải trên cách 12, có chấm | Badge |
| Chân | viền trên 1; lề 16 × 10; icon `user-round` + Driver · icon `route` + Route (tắt bằng Has Route) | `color/border/secondary` |

### Biến thể

| Trục | Giá trị | Khác gì |
|---|---|---|
| State | Default · Hover · Pressed · Focus | Hover nền `color/bg/primary_hover` · Pressed nền `color/bg/selected` · Focus viền 2 `color/focus/ring` |

### Trạng thái nội dung

| Ca | Cách đặt |
|---|---|
| Đang chạy Lệnh | Status "Đang hoạt động", Route = tuyến của Lệnh |
| Chưa gán lái xe | Driver = "Chưa gán lái xe", tắt Has Route |
| Không khả dụng | Status "Đang sửa chữa" / "Đang tạm giữ", Location ghi chỗ + hạn ("Xưởng Đình Vũ · tới 30/10"); **không** làm mờ ảnh |
| Mooc, thiết bị không có ODO | Odometer = "—" |

Màu Badge (đề xuất, **chưa chốt** — chưa có `vehicle-management-states.md`): Sẵn sàng hoạt động Green · Đang hoạt động
Blue · Đang sửa chữa Yellow · Đang tạm giữ Gray.

### Kích thước

Trải theo cột lưới, không có rộng cố định (DEC-334 vh05, thay 360 của DEC-269): 4 cột trên web 1280 (976 − 3 rãnh 32 = 304
mỗi cột), tối thiểu 304. Cao theo nội dung (≈ 140 khi đủ dòng). Ảnh giữ 160 × 100. Ở 304: ảnh 160, lề 16 + 12 còn 116 cho
chữ, biển số đọc được, dòng xe cắt "…".

### Nên và không nên

- Nên: trạng thái luôn có chữ trong Badge; dùng đúng nhóm hình qua Image.
- Không nên: làm mờ/xám thẻ để báo không khả dụng; thêm nút vào thẻ; nhồi quá 2 dòng thông tin phụ.

### Trợ năng — chấm theo WCAG 2.2

- 2.4.7 Focus thấy được: viền 2 `color/focus/ring`. 2.5.8 Vùng chạm: cả thẻ ≥ 140 cao.
- 1.1.1: ảnh trang trí (`alt=""`), biển số và dòng xe là chữ. 1.4.1: trạng thái có chữ, không chỉ màu.
- Tên truy cập của thẻ = "Plate, Model, trạng thái".

### Thuộc tính

TEXT: `Plate` · `Model` · `Odometer` · `Location` · `Driver` · `Route` · BOOLEAN: `Has Location` · `Has Route` · VARIANT:
`State` · lồng đưa ra panel: `Image` (Vehicle Image — đổi Group / Style), `Status` (Badge — đổi Label / Color).

### Thành phần lồng

Vehicle Image (View Q) · Badge (Type Pill Color, Size SM, Has Dot, tắt X Close / Count / Icon) · icon `gauge`, `map-pin`,
`user-round`, `route` (16).

### Được dùng trong

Demo `Danh sách xe / Web`, `Đội xe / Mobile`.

### Kiểm máy

27/10: kiểm tên fail 0 trên Section và Demo · 0 màu gõ tay trong hai set. Chữ dài 360 và 320: biển số, dòng xe cắt "…",
vị trí / lái xe / tuyến xuống dòng, Badge dài nhất (Sẵn sàng hoạt động, 132) không đè chữ. Kiểm mất hình: chưa chạy.
02/11: spec theo DEC-334, Figma chưa sync; chữ dài ở 304 chưa kiểm trên Figma.

### Dark

| Phần | Sáng | Tối |
|---|---|---|
| Bóng, viền | `shadow/xs` + `shadow/xs-border` | giữ cả hai (DEC-327) |
| Icon phụ trên `color/bg/primary` | `color/fg/tertiary` 7,81:1 | `color/fg/tertiary` 6,97:1 |
| Nét bao ảnh 0,6 | `color/fg/quaternary` | `color/fg/tertiary` |

### Mục mở

- Thẻ app trên màn dưới 320: Badge xuống hàng dưới biển số, vì Badge dài nhất đo được 143 làm biển số chạm Badge khoảng 2px (user 02/11).

Hướng của user 02/11 (DEC-334 vh05), **chưa làm, đợi lượt sync component**:

> Phần ảnh dùng cho thẻ này nên reverse lại quay đầu vào trong thẻ, chỗ này đến component cân nhắc sửa component tách layer, blur nhẹ phần ảnh phương tiện sau nếu có chữ đè lên

## Mobile

> Component `Vehicle Card / Mobile`, mode Platform = Mobile. Giống Web, khác: trải theo màn (361 ở khung 393, lề 16), sàn
> 304 chỉ áp web; ô ảnh **140 × 88** (`vehicle/card-media-app-w` × `vehicle/card-media-app-h`, để Badge dài
> nhất nằm gọn trên vùng ảnh ở bề rộng 320); State chỉ Default · Pressed · Focus (không có Hover).

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
