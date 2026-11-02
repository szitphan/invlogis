---
type: design-component
status: stale
status_prev: draft
updated: 2026-11-02
links:
  - design-system/foundations/vehicle.md
  - design-system/components/application/container-slot.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - _workspace/decisions.md
---

# Combo Slots

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Combo Slots` (6804:16465), trang
> DS · Application components, Section `Combo slots` 6805:16591, Demo 6805:16599 · lồng `Container Slot`
> (6797:15876) · DEC-267, DEC-273, DEC-334

Tổ hợp dạng **sơ đồ khe** (cách B, `design-system/foundations/vehicle.md` mục 5.4): khối mooc (biển số · loại, hàng khe container) nối
khối đầu kéo, không dùng ảnh. Một component cho web và app.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng ở: chi tiết Lệnh (dưới hình ghép A), form xếp tổ hợp (từng vị trí), dòng mở rộng danh sách Lệnh, thẻ Lệnh app,
  popup bản đồ.
- Đầu xe bên **phải** (cùng hướng ảnh Vehicle Image): mooc trái — đoạn nối — đầu kéo phải.
- Banner F4 (mooc trên Lệnh khác mooc đang móc), đổi vỏ, chưa có số đặt **ngoài** component, đầu khối chứa.

### Cấu tạo

| Phần | Nội dung | Token |
|---|---|---|
| `Trailer box` | lề 8, khoảng 8; dòng `Trailer` (label) + `Trailer type` (caption); hàng `Slots` | `color/bg/secondary` · `radius/inner` |
| `Slots` | instance Container Slot (`Slot 1`, `Slot 2`), chia 20 = 1 phần, 40/45 = 2 phần; 1×20 Center có hai khoảng trống | — |
| `Hitch` | đường 16 × 2 | `color/border/primary` |
| `Tractor box` | rộng 112, lề 12 × 10; `Tractor` (label) + `Tractor type` (caption), 1 dòng cắt "…" | `color/bg/secondary` · `radius/inner` |
| `Error message` | dòng lỗi dưới, ẩn mặc định | `type/caption` · `color/text/error/primary` |

### Biến thể

| Config | Khi nào |
|---|---|
| No Trailer | đầu kéo chạy một mình — khối mooc viền đứt "Không kéo mooc" |
| Empty | kéo mooc không container — hàng khe viền đứt "Không container" |
| 1×20 | 20ft trên mooc 20ft |
| 1×20 Center | 20ft trên mooc 40/45 (đặt giữa) |
| 2×20 · 1×40 · 1×45 | theo cấu hình |

| Density | Khác gì |
|---|---|
| Default | xếp ngang; khe Container Slot Default (có chip trạng thái) |
| Compact | **xếp dọc**: dòng đầu kéo (biển số + loại cùng hàng) trên, mooc dưới; khe Container Slot Compact. Dùng ở bề rộng ≤ 400 (thẻ app trải theo màn, 361 ở khung 393) và dòng mở rộng |

14 biến thể. Bảng 17 ca: `design-system/foundations/vehicle.md` Mục 5.3.

### Lỗi

`Has Error` + `Error`: cấu hình bị chặn theo `P-quy-tac-ghep-mooc` (F10), vd "Cấu hình bị chặn: container 40ft dài hơn
mooc 20ft". Cảnh báo / Cần hỏi hiển thị ở form, không trong component.

### Nên và không nên

- Nên: đổi `Trailer type` cho khớp mooc thật (thuộc tính dùng chung mọi Config, mặc định "40ft 3 giàn").
- Không nên: dùng Default ở chỗ hẹp hơn 400 (số container bị cắt); vẽ lại khe thay vì dùng Container Slot.

### Trợ năng — chấm theo WCAG 2.2

- Đọc theo thứ tự đầu kéo → mooc → khe (thứ tự DOM, không theo vị trí trên màn). Lỗi có chữ, không chỉ màu.

### Thuộc tính

TEXT `Tractor` · `Tractor type` · `Trailer` · `Trailer type` · `Error` · BOOLEAN `Has Error` · VARIANT `Config`, `Density`
· đưa ra panel: `Slot 1`, `Slot 2` (Container Slot — State, Number, Order, Reefer).

### Thành phần lồng

Container Slot ×1–2 (Density theo cha).

### Được dùng trong

Demo `Chi tiết lệnh / Web` (banner F4 + 1×40), `Lệnh của tôi / Mobile` (2×20 Compact). Sẽ dùng trong Combo Figure.

### Kiểm máy

27/10: kiểm tên fail 0. Đã sửa: Compact xếp ngang cắt số container ở 343 → xếp dọc; chiều cao khối bị khoá sau khi đổi
hướng. Kiểm mất hình: chưa chạy. 02/11: spec theo DEC-334, Figma chưa sync.

### Dark

Chưa có số đo Dark.

## Mobile

> Mode Platform = Mobile, cùng component; thẻ app dùng Density Compact.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
