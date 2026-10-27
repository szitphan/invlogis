---
type: design-component
status: draft
updated: 2026-10-27
links:
  - design/v2/vehicles.md
  - design/_lab/tyre-mapping.html
  - docs/vehicle-management/brainstorms/vehicle-management.md
  - _workspace/decisions.md
---

# Tyre Layout · Tyre Slot

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Tyre Layout` (6808:16848) và
> `Tyre Slot` (6808:16502), trang DS · Application components, Section `Tyre layout` 6809:17018, Demo 6809:17026 ·
> DEC-266, DEC-275

Sơ đồ lốp nhìn từ trên theo **cấu hình trục** (`design/v2/vehicles.md` mục 3) và vị trí lốp có trạng thái. Một
component cho web và app.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Dùng ở: hồ sơ phương tiện (tab Lốp), ghi thay lốp, báo hỏng lốp trên app lái xe.
- Đầu xe hướng lên, **bên lái bên trái**; trục lái ở trước, trục tải dồn về sau; mooc có chốt kéo thay cabin.
- Số trên lốp = số thứ tự vị trí trong file lốp của khách. Bấm một lốp → xem lịch sử, ghi thay (hành vi do màn quyết).

### Cấu tạo — Tyre Layout

| Phần | Nội dung | Token |
|---|---|---|
| Khung | 200 rộng, cao theo số trục (170–388) | — |
| `Body` | thân xe 70 rộng | `color/bg/muted` · `color/border/default` |
| `Cab` / `Kingpin` | dải "Đầu xe" (xe) hoặc chấm "chốt kéo" (mooc) | `color/border/default` · `color/text/tertiary` |
| `Axle n` | đường trục 78 × 3 + chữ "trục n" | `color/text/tertiary` · `type/caption` |
| `Tyre n` | instance Tyre Slot 16 × 30, cách thân 6; lốp kép ngoài lệch thêm 19 | — |
| Dự phòng | Tyre Slot Spare dưới thân + "dự phòng" | — |
| Nhãn bên | "bên lái" trái, "bên phụ" phải | `type/caption` |

### Biến thể — Tyre Layout

`Layout`: tractor-6x4 · tractor-4x2 · truck-4x2 · truck-6x4 · truck-6x2 · truck-8x4 · truck-5ax · trailer-2ax ·
trailer-3ax · forklift-diesel · forklift-elec (11). Nhóm hình chọn sơ đồ mặc định theo `vehicles.json` →
`tyre_layout`; tên xe đổi được (`tyre_override`).

### Biến thể — Tyre Slot

| Kind | Nền mặc định |
|---|---|
| Steer — lốp lái | `color/text/secondary` |
| Load — lốp tải | `color/bg/inverse` |
| Spare — dự phòng | vòng tròn 26, viền đứt `color/text/secondary` |

| State | Khác gì |
|---|---|
| Default | theo Kind |
| Selected | nền `color/status/info-solid`, viền ngoài 3 `color/border/focus` |
| Warning | nền `color/status/warning-solid` — đến hạn km / ngày, mòn |
| Error | nền `color/status/danger-border` — hỏng, cần thay |
| Empty | không nền, viền đứt `color/border/strong`, số `color/text/tertiary` — chưa lắp |

15 biến thể. Chữ số `type/chip-sm-strong`, `color/text/inverse`.

### Nên và không nên

- Nên: luôn kèm danh sách / chú giải bằng chữ cho lốp Warning, Error (demo: cột chi tiết bên phải).
- Không nên: dựa vào màu để báo trạng thái; sửa số lốp khác file của khách khi khách chưa chốt (OQ-6…13).

### Trợ năng — chấm theo WCAG 2.2

- 1.4.1: trạng thái lốp có chữ ở danh sách đi kèm. 2.5.8: vùng chạm lốp 16 × 30 < 24 × 24 ở web — nới vùng chạm
  vô hình 24 × 32 khi code; app phóng sơ đồ ≥ 1,5 lần hoặc chọn từ danh sách.
- Tên truy cập lốp: "Vị trí n, lốp lái/tải, bên lái/phụ, trục m, trạng thái".

### Thuộc tính

Tyre Slot: TEXT `Number` · VARIANT `Kind`, `State`. Tyre Layout: VARIANT `Layout` · đưa ra panel `Tyre 1…n`.

### Được dùng trong

Demo `Lốp xe / Web` (đầu kéo 6x4 + cột chi tiết), `Lốp xe / Mobile` (mooc 3 giàn).

### Kiểm máy

27/10: kiểm tên fail 0. Đã sửa: Selected trùng màu lốp tải; cột chi tiết demo cao cố định. Còn: forklift-elec lốp 3
giữa trục che chữ "trục 2". Dark: chưa điền giá trị Dark.

## Mobile

> Mode Platform = Mobile, cùng component. Trên app phóng sơ đồ hoặc dùng danh sách vị trí để chọn (vùng chạm).

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
