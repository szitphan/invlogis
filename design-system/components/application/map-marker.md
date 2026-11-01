---
type: design-component
status: stale
status_prev: draft
updated: 2026-10-27
links:
  - design-system/foundations/misc-icon.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
  - _workspace/decisions.md
---

# Map Marker · Map Dot · Map Cluster · Map Pin

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Map Marker` (6811:17156), `Map Dot`
> (6811:17181), `Map Cluster` (6811:17188), `Map Pin` (6811:17199), trang DS · Application components, Section
> `Map marker` 6812:111364, Demo 6812:111372 · lồng `Vehicle Image` View Top (6777:1914) · DEC-266, DEC-276

Marker phương tiện và tổ hợp trên bản đồ theo **mức phóng** (`design-system/foundations/misc-icon.md` mục 4), cụm, và ghim điểm Lấy /
Giao của Lệnh. Bốn set vì 3 Kind × 6 State × 2 mức phóng vượt trần 30 tổ hợp. Web = Mobile.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

| Mức phóng | Component |
|---|---|
| Gần | `Map Marker` — ảnh nhìn từ trên 8 px/m, đầu xe hướng lên, chấm trạng thái ở đầu, nhãn biển số dưới |
| Vừa | `Map Dot` — chấm trạng thái + nhãn |
| Xa | `Map Cluster` — tròn nền inverse + số xe |
| Mọi mức | `Map Pin` — điểm Lấy · Giao của Lệnh đang xem |

- Kind: **Vehicle** (xe đơn), **Combo** (đầu kéo + mooc), **Trailer** (mooc đứng riêng tại chỗ đỗ, `vehicle-telematics`
  M2).
- **Hướng chạy:** code xoay riêng `Figure` theo hướng GPS; nhãn và chấm trạng thái giữ thẳng. Figma không xoay được lớp
  trong instance nên master và demo vẽ đầu xe hướng lên.
- Marker Combo chưa vẽ container (ảnh Top container sai góc — BL-264).

### Cấu tạo — Map Marker

| Phần | Nội dung | Token |
|---|---|---|
| `Media` | khung bao hình, lề 6; Selected: nền `color/bg/selected`, viền 2 `color/focus/ring`, bo 8 | — |
| `Figure` | Vehicle Image Top 50% (Combo: mooc nối sau mâm kéo); Offline: mờ 50% | `size/md` |
| `Status` | chấm 12 viền trắng 2, góc trên phải | màu theo State |
| `Label` | pill biển số, lề 6 × 2, bo 6, viền 1; Offline thêm giờ cuối | `type/caption-strong` · `color/bg/primary` |

### State và màu (dùng chung Marker và Dot)

| State | Nghĩa | Màu |
|---|---|---|
| Moving | đang chạy | `color/bg/success/solid` |
| Stopped | dừng, tắt máy | `color/text/disabled` |
| Idling | nổ máy không chạy (kẹt xe, nổ máy ngủ) | `color/bg/warning/solid` |
| Offline | mất tín hiệu — vị trí cuối, mờ, nhãn "· 10:40" | `color/border/primary` |
| Alert | có sự việc (cảnh báo nhiên liệu, ngoài Lệnh…) | `color/border/error` |
| Selected | đang chọn | `color/bg/info/solid` + vòng focus |

### Biến thể

`Map Marker`: Kind (3) × State (6) = 18 · `Map Dot`: State (6) · `Map Cluster`: Size SM < 10 · MD 10–99 · LG ≥ 100 ·
`Map Pin`: Type Pickup (Lấy, `info-solid`) · Delivery (Giao, `success-solid`); chấm đáy là toạ độ.

### Nên và không nên

- Nên: thu nhỏ thì chuyển Marker → Dot → Cluster; bấm marker mở thẻ (Vehicle Card) ở panel / bottom sheet.
- Không nên: dùng màu làm tín hiệu duy nhất (nhãn + chi tiết khi bấm); xoay cả nhãn theo hướng chạy.

### Trợ năng — chấm theo WCAG 2.2

- Tên truy cập marker = "biển số, trạng thái, giờ cập nhật". Danh sách xe song song với bản đồ cho người không dùng
  được bản đồ. 2.5.8: Dot 14 + nhãn ≥ 24 cao vùng chạm.

### Thuộc tính

`Map Marker`: TEXT `Name` · BOOLEAN `Has Label` · VARIANT `Kind`, `State` · đưa ra panel `Image` / `Tractor`, `Trailer`.
`Map Dot`: TEXT `Name` · VARIANT `State`. `Map Cluster`: TEXT `Count` · VARIANT `Size`. `Map Pin`: VARIANT `Type`.

### Được dùng trong

Demo `Theo dõi đội xe / Web` (đủ 3 mức, ghim Lấy/Giao), `Theo dõi đội xe / Mobile` (bottom sheet Vehicle Card / Mobile).

### Kiểm máy

27/10: kiểm tên fail 0. Đã sửa: xoay instance làm nghiêng nhãn (demo bỏ xoay, ghi luật cho code); sheet demo cao cố
định. Còn: vòng Selected lệch vài px về phía chấm. Dark: chưa điền giá trị Dark.

## Mobile

> Mode Platform = Mobile, cùng component. App ưu tiên Dot + Cluster; Marker ảnh khi phóng gần hoặc đang chọn.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
