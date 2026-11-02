---
type: design-component
status: stale
status_prev: draft
updated: 2026-11-02
links:
  - design-system/foundations/vehicle.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
  - _workspace/decisions.md
---

# Map Marker · Map Dot · Map Cluster · Map Pin

> Application · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Map Marker` (6811:17156), `Map Dot`
> (6811:17181), `Map Cluster` (6811:17188), `Map Pin` (6811:17199), trang DS · Application components, Section
> `Map marker` 6812:111364, Demo 6812:111372 · lồng `Vehicle Image` View Top (6777:1914) · DEC-266, DEC-276, DEC-334

Marker phương tiện và tổ hợp trên bản đồ theo **mức phóng** (`design-system/foundations/vehicle.md` mục 4), cụm, và ghim điểm Lấy /
Giao của Lệnh. Bốn set vì 3 Kind × 6 State × 2 mức phóng vượt trần 30 tổ hợp. Web = Mobile.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

| Mức phóng | Bản đồ | Component |
|---|---|---|
| Gần | ≥ 17 | `Map Marker` — ảnh nhìn từ trên 4 px/m, Đang chọn 8 px/m, đầu xe hướng lên, chấm trạng thái ở đầu, nhãn biển số dưới |
| Vừa | 12–16 | `Map Dot` — chấm trạng thái + nhãn |
| Xa | ≤ 11 | `Map Cluster` — tròn nền inverse + số xe |
| Mọi mức | mọi mức | `Map Pin` — điểm Lấy · Giao của Lệnh đang xem |

- Kind: **Vehicle** (xe đơn), **Combo** (đầu kéo + mooc), **Trailer** (mooc đứng riêng tại chỗ đỗ, `vehicle-telematics`
  M2).
- **Hướng chạy:** code xoay riêng `Figure` theo hướng GPS; nhãn và chấm trạng thái giữ thẳng. Figma không xoay được lớp
  trong instance nên master và demo vẽ đầu xe hướng lên.
- **Chuyển động:** preset `glide` khi có điểm GPS mới, giữa hai điểm xe đứng yên; điểm ngoài khung nhìn hoặc xa quá thì đặt ngay; giảm chuyển động thì nhảy tới điểm mới (`foundations/motion.md` mục 10.11, DEC-336).
- Marker Combo chưa vẽ container (ảnh Top container sai góc — BL-264).
- **Nhóm thiếu ảnh Top** (DEC-334 vh15, `vehicles.json` → `top_fallback`): xe tải mượn `t03-top`, dài theo `size_m` của nhóm;
  `forklift-elec`, `genset`, `fuel-station` dùng Map Dot ở mọi mức phóng.

### Cấu tạo — Map Marker

| Phần | Nội dung | Token |
|---|---|---|
| `Media` | khung bao hình, lề 6; Selected: nền `color/bg/selected`, viền 2 `color/focus/ring`, bo 8 | — |
| `Figure` | Vehicle Image Top 25% (4 px/m), Selected 50% (8 px/m); Combo: mooc nối sau mâm kéo; Offline: mờ 50% | `vehicles.json` → `marker_px_per_m` |
| `Status` | chấm vẽ riêng cỡ 12 (không dùng `_Dot`, vì instance đang ghi đè màu, [icon-sets.md](../../foundations/icon-sets.md)), viền trắng 2, góc trên phải; không mờ ở Offline | màu truyền từ cha theo State · `shadow/sm` |
| `Label` | pill biển số, lề 6 × 2, bo 6, viền 1; Offline thêm giờ cuối | `type/caption-strong` · `color/bg/primary` · `shadow/sm` |

### State và màu (dùng chung Marker và Dot)

| State | Nghĩa | Màu |
|---|---|---|
| Moving | đang chạy | `color/bg/success/solid` |
| Stopped | dừng, tắt máy | `color/fg/tertiary` |
| Idling | nổ máy không chạy (kẹt xe, nổ máy ngủ) | `color/bg/warning/solid` |
| Offline | mất tín hiệu — vị trí cuối, hình mờ, chấm không mờ, nhãn "· 10:40" | `color/fg/quaternary` |
| Alert | có sự việc (cảnh báo nhiên liệu, ngoài Lệnh…) | `color/bg/error/solid` |
| Selected | đang chọn | `color/bg/info/solid` + vòng focus |

### Biến thể

`Map Marker`: Kind (3) × State (6) = 18 · `Map Dot`: State (6) · `Map Cluster`: Size SM < 10 · MD 10–99 · LG ≥ 100 ·
`Map Pin`: Type Pickup (Lấy, `info-solid`) · Delivery (Giao, `success-solid`); chấm đáy là toạ độ.
Nhãn, chấm (Dot), cụm (Cluster) đều `shadow/sm` (DEC-334 vh17, vai Marker bản đồ).

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
định. Còn: vòng Selected lệch vài px về phía chấm. 02/11: spec theo DEC-334, Figma chưa sync. Giá của bóng trên từng chấm
khi nhiều xe: chưa đo.

### Dark

Tương phản chấm so với nền đất **giả lập** của `design/_lab/lab-map.html` (Sáng #eef0f3, Tối #15171b). **Chưa kiểm trên bản
đồ thật** (Vietmap, Google Maps).

| State | Màu | Sáng | Tối |
|---|---|---|---|
| Moving | `color/bg/success/solid` | 5,01:1 | 3,14:1 |
| Stopped | `color/fg/tertiary` | 6,84:1 | 7,11:1 |
| Idling | `color/bg/warning/solid` | 5,54:1 | 2,84:1 |
| Offline | `color/fg/quaternary` | 2,21:1 | 2,30:1 |
| Alert | `color/bg/error/solid` | 5,76:1 | 2,73:1 |
| Selected | `color/bg/info/solid` | 6,41:1 | 2,45:1 |

Offline dưới 3:1 là cố ý, luôn có giờ cuối trên nhãn. Nền đặc ở Tối dưới 3:1 dựa vào viền trắng 2 để tách khỏi nền.

## Mobile

> Mode Platform = Mobile, cùng component. App ưu tiên Dot + Cluster; Marker ảnh khi phóng gần hoặc đang chọn.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
