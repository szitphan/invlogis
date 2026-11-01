---
type: design-component
status: stale
status_prev: draft
updated: 2026-10-27
links:
  - design-system/foundations/misc-icon.md
  - design-system/components/application/combo-slots.md
  - design/_lab/lab-combo.html
  - _workspace/decisions.md
---

# Combo Figure

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Combo Figure` (6806:16351), trang
> DS · Application components, Section `Combo figure` 6807:110447, Demo 6807:110455 · lồng `Vehicle Image`
> (6777:1914) View S · DEC-266, DEC-267, DEC-274

Tổ hợp **hình ghép tỉ lệ thật** (cách A, `design-system/foundations/misc-icon.md` mục 5.4) từ ảnh mặt ngang: nhìn là biết dài ngắn,
mấy container, mooc gì. Một component cho web và app.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng ở: chi tiết Lệnh (trên Combo Slots), form xếp tổ hợp (xem trước, cập nhật theo lựa chọn), thẻ Lệnh app (SM).
- Hình chỉ để **nhận dạng**; trạng thái vị trí container, số container, lỗi cấu hình đọc ở **Combo Slots đặt ngay
  dưới**. Không dùng Combo Figure một mình khi cần trạng thái.
- Đầu xe bên phải, đáy bánh thẳng hàng; đặt trên nền `color/bg/secondary` có lề.

### Cấu tạo (số đo ghép, nguồn lab-combo)

| Phần | Cách đặt |
|---|---|
| `Trailer` | Vehicle Image S theo Config: 1×20 → mooc 20ft · Empty, 1×20 Center, 2×20 → 40ft 3 giàn · 1×40 → 40ft 2 giàn · 1×45 → 45ft; đáy = đáy khung |
| `Tractor` | Vehicle Image S `tractor-2ax`; mâm kéo (19% chiều dài từ đuôi) cách đầu mooc 1 m; đáy = đáy khung |
| `Box 1`, `Box 2` | box-20 / box-40 / reefer-45; đáy container = mặt trên ảnh mooc; 2×20: cách đầu mooc 0,15 m, khe 0,08 m; 1×20: giữa mooc |

### Biến thể

| Trục | Giá trị |
|---|---|
| Config | No Trailer · Empty · 1×20 · 1×20 Center · 2×20 · 1×40 · 1×45 |
| Scale | MD 16 px/m (`size/xl`: chi tiết, form) · SM 8 px/m (`size/md`: thẻ app, cột danh sách) |

14 biến thể; tổ hợp dài nhất (1×45) ≈ 297 × 80 ở MD.

### Đổi phần

`Tractor`, `Trailer`, `Box 1`, `Box 2` là Vehicle Image đưa ra panel: đổi nhóm đầu kéo (đầu dài, 1 cầu), đổi container
sang lạnh. Đầu kéo khác Hino có mâm 25–26% (MAZ, Chenglong): lệch ≤ 0,5 m, chấp nhận ở cỡ UI.

### Nên và không nên

- Nên: luôn kèm Combo Slots (web) hoặc danh sách container (app).
- Không nên: kéo giãn méo hình; trộn MD và SM trong cùng một danh sách.

### Trợ năng — chấm theo WCAG 2.2

- 1.1.1: hình trang trí khi Combo Slots / chữ đi kèm (`alt=""`); đứng riêng thì `alt` = câu Combo Text.

### Thuộc tính

VARIANT `Config`, `Scale` · đưa ra panel: `Tractor`, `Trailer`, `Box 1`, `Box 2`.

### Được dùng trong

Demo `Chi tiết lệnh / Web` (A + Combo Slots), `Lệnh của tôi / Mobile` (A SM + Container Slot).

### Kiểm máy

27/10: kiểm tên fail 0. Ảnh Vehicle Image S theo tỉ lệ thật (container 40/45, lạnh đã sửa chiều cao 27/10). Kiểm mất
hình: chưa chạy. Dark: chưa điền giá trị Dark.

## Mobile

> Mode Platform = Mobile, cùng component; thẻ app dùng Scale SM.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
