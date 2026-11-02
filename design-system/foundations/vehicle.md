---
type: design-foundations
feature: ds-v2
status: draft
updated: 2026-11-02
links:
  - design-system/foundations/README.md
  - design-system/handoff/vehicles.json
  - design-system/assets/vehicles
  - design/_lab/vehicles-final.html
  - design/_lab/lab-combo.html
  - design/_lab/tyre-mapping.html
---

# Foundations · Phương tiện (DEC-266, DEC-267, DEC-334)

Ảnh phương tiện, khung và cỡ, sơ đồ lốp, marker bản đồ, và quy ước tổ hợp đầu kéo – mooc – container.
Chuẩn hoá từ lab 09–12/10 (`design/_lab/vehicles-final.html`, `lab-combo.html`, `tyre-mapping.html`),
phỏng vấn 27/10, trang review 02/11 (DEC-334). Dữ liệu máy đọc: `design-system/handoff/vehicles.json`.
Ảnh: `design-system/assets/vehicles/` (Mục 2.6).

## 1. Nhóm hình — khoá ảnh `[Lõi]`

Ảnh khoá theo **nhóm hình chung** (loại × số trục × cỡ dài), không theo tên xe của khách.

| Phần | Tầng | Ai làm |
|---|---|---|
| Nhóm hình | `[Lõi]` | Mọi khách dùng chung |
| Bảng gán tên xe → nhóm | `[Riêng Delta]`, dữ liệu mẫu trong `vehicles.json` → `tenants.delta` (39 tên, SRS cũ LG) | **Đội sản phẩm tự gán khi đưa khách lên; khách không sửa, không có màn cấu hình cho khách** (DEC-334 vh10) |

Bảng gán là dữ liệu danh mục, không có mã `P-…` (`.claude/rules/saas-layer.md` Mục 4). Tên chưa gán về `unknown`.

| Họ | Mã nhóm | Tên | Ảnh mặc định | Kiểu dáng phụ (Style) | Sơ đồ lốp mặc định |
|---|---|---|---|---|---|
| Đầu kéo | `tractor-1ax` | Đầu kéo 1 cầu sau | n05 | — | `tractor-4x2` |
| Đầu kéo | `tractor-2ax` | Đầu kéo 2 cầu sau, cabin bằng | t02 | Alt 1 = n09 | `tractor-6x4` |
| Đầu kéo | `tractor-2ax-long` | Đầu kéo 2 cầu sau, đầu dài | n08 | Alt 1 = n06 | `tractor-6x4` |
| Xe tải | `truck-2ax-s` | Xe tải 2 trục nhỏ (≤ 5,5 m) | g-truck-s | Alt 1 = g-kia | `truck-4x2` |
| Xe tải | `truck-2ax-m` | Xe tải 2 trục vừa (6–7,5 m) | t03 | Alt 1 = n17 · Alt 2 = n29 | `truck-4x2` |
| Xe tải | `truck-2ax-l` | Xe tải 2 trục dài (9–10 m) | g-truck-l | Alt 1 = n12 · Alt 2 = n25 · Alt 3 = n27 | `truck-4x2` |
| Xe tải | `truck-3ax` | Xe tải 3 trục | n26 | Alt 1 = n10 | `truck-6x4` |
| Xe tải | `truck-4ax` | Xe tải 4 trục | n28 | — | `truck-8x4` |
| Mooc | `trailer-20` | Mooc 20ft | n01 | — | `trailer-2ax` |
| Mooc | `trailer-40-2ax` | Mooc 40ft 2 giàn | t01 | — | `trailer-2ax` |
| Mooc | `trailer-40-3ax` | Mooc 40ft 3 giàn | n03 | — | `trailer-3ax` |
| Mooc | `trailer-40-flat` | Mooc sàn 40ft | g-mooc-san | — | `trailer-2ax` |
| Mooc | `trailer-45` | Mooc 45ft | n04 | — | `trailer-3ax` |
| Container | `box-20` · `box-40` · `box-45` | Container 20 · 40 · 45ft | t06 · c40 · c45 | — | không lốp |
| Container | `reefer-45` | Container lạnh 45ft | t07 | — | không lốp |
| Thiết bị | `forklift-diesel` · `forklift-elec` | Xe nâng diesel · điện | t04 · t05 | — | cùng tên |
| Thiết bị | `genset` · `fuel-station` | Máy phát điện · Trạm bơm dầu | t08 · t09 | — | không lốp |
| Khác | `unknown` | Chưa xác định (mã PT 00) | ô trống | — | không hiện |

- 22 nhóm. Mã nhóm ≤ 16 ký tự để làm giá trị thuộc tính Figma (DEC-264).
- **Kiểu dáng phụ** là ảnh theo hãng đã có từ lab, giữ logo hãng (chốt 09/10, giữ 27/10). Không sinh thêm.
- Một tên xe được đổi sơ đồ lốp khác mặc định của nhóm (vd Delta AC990 → `truck-6x2`): `tyre_override`.
- Thêm nhóm mới = thêm ảnh theo quy chuẩn Mục 2; gọi API sinh ảnh phải báo kế hoạch + chi phí trước.

## 2. Mặt cắt, khung, cỡ

### 2.1 Ba mặt cắt

| View | File | Định nghĩa | Dùng ở |
|---|---|---|---|
| `Q` | `{ảnh}-q.png` | 3/4 trước ~35°, đầu xe sang **phải** | Thẻ, ảnh thu nhỏ, chọn loại, đầu trang chi tiết |
| `S` | `{ảnh}-s.png` | Ngang vuông góc, đầu xe sang phải, bánh tròn | Tổ hợp (hình ghép A), so sánh, dàn xe |
| `Top` | `{ảnh}-top.png` | Nhìn thẳng từ trên, đầu xe hướng **lên** | Marker bản đồ |

Cần quay trái thì lật ngang (`scaleX(-1)`), chấp nhận logo ngược ở cỡ UI. Ảnh nền trong suốt, không bóng.
"Đầu" của vật không phải xe: mooc = chốt kéo · container = cửa · lạnh = cụm máy lạnh · máy phát = bảng điều khiển.

### 2.2 Hai chế độ hiển thị

| Chế độ | Dùng ở | Cách lấp |
|---|---|---|
| **Vừa khung** | Ảnh thu nhỏ, thẻ, ô chọn loại | Mọi nhóm chung một khung, căn đáy bánh. Ô vuông: xe dài cắt lấy **đầu xe, tràn mép phải**; mooc lấy **cụm bánh, tràn mép trái**; thiết bị gọn lấy cả (`thumb_crop` = head · wheels · whole) |
| **Tỉ lệ thật** | Tổ hợp, so sánh, dàn xe | Theo px/m từ `size_m`, căn đáy bánh, không cắt |

### 2.3 Khung và cỡ

Foundation chỉ chốt **tỉ lệ khung ảnh `Q` là 16:10**. Số đo cỡ ảnh của thẻ thuộc tầng Component của Vehicle Card
(DEC-334 vh01); bảng dưới là để tra.

| Chỗ dùng | Cỡ | Token (`tokens.json` → Platform) |
|---|---|---|
| Vehicle Thumb XS · SM · MD | 32 · 48 · 64 vuông, bo 8 cả 3 cỡ | `size/4xl` · `size/6xl` · `size/7xl` · `radius/inner` |
| Vehicle Card web | 160 × 100 | `size/11xl` × `vehicle/q-sm-h` |
| Vehicle Card app | 140 × 88 | `vehicle/card-media-app-w` × `vehicle/card-media-app-h` |
| Đầu trang chi tiết phương tiện | rộng tối đa 480, app trải theo màn, cao theo 16:10 (DEC-334 vh02) | `vehicle/q-lg-w` |

**Tỉ lệ thật px/m là hằng số**, không phải token (DEC-334 vh03): `vehicles.json` → `scale_px_per_m`. Đây là số nhân với
`size_m`, không phải cỡ; không mượn `size/*`.

| Tên | px/m | Dùng |
|---|---|---|
| `sm` | 8 | Hình ghép trong cột danh sách, thẻ app (Combo Figure 1×45 ≈ 149) |
| `md` | 16 | Khối chi tiết, form (Combo Figure 1×45 ≈ 297) |
| `lg` | 40 | Trang tài liệu, dàn xe |

### 2.4 Sửa ảnh 27/10

- `c40-s`, `c45-s`, `t07-s` cao hơn thật (+50…102%) → nén dọc về 2,59 / 2,9 m (xử lý cục bộ, không gọi API).
  Bản gốc ở `design-system/assets/vehicles/_orig/`.
- **Lỗi còn mở:** `c40-top`, `c45-top`, `t07-top`, `t06-top` không phải ảnh nhìn thẳng từ trên (c45 nghiêng
  phối cảnh, t07 chụp mặt đầu cụm máy lạnh). Marker container dùng hình vẽ khối tới khi sinh lại (BL-264, cần duyệt
  chi phí API).

### 2.5 Nền ô và nét bao (DEC-334 vh08)

Ảnh trong suốt nên một nền không cứu được cả hai chế độ: Sáng thì container trắng tan, Tối thì lốp đen tan. Đo trên
21 ảnh `Q`, tỉ lệ điểm ảnh dưới 1,5:1 so với nền: Sáng `#FAFAFA` trung bình 34%; Tối `#232323` trung bình 32%, đổi
`#404040` còn 26%.

| | Sáng | Tối |
|---|---|---|
| Nền ô ảnh | `color/bg/secondary` | `color/bg/quaternary` |
| Nét bao 0,6 theo hình (drop-shadow trên ảnh trong suốt) | `color/fg/quaternary` | `color/fg/tertiary` |

**Chưa đo hiệu năng** nét bao trong danh sách dài, chưa kiểm trên Flutter.

### 2.6 Ảnh bàn giao (DEC-334 vh09)

Nguồn duy nhất: `design-system/assets/vehicles/{ảnh}-{view}.png` · bản gốc trước khi sửa ở `_orig/`.

- **Ảnh chưa nén**, file lớn nhất 935 KB. **Dev phải nén khi tích hợp.** Đo 02/11 bằng PIL, WebP chất lượng 80 theo cỡ
  dùng (Q rộng 960, S 448, Top 120): 1,19 MB trên 44,2 MB của 76 file đang dùng.
- `g-truck-s.png` không có trong `vehicles.json`, giữ cùng thư mục, chưa dùng.

### 2.7 Icon xe hay ảnh (DEC-334 vh11)

| Chỗ | Dùng |
|---|---|
| Menu, nhãn, chip (≤ 20) | Icon xe: `icon/tractor-unit`, `icon/container-truck` (`design-system/foundations/icon.md`) |
| Dòng dữ liệu (≥ 32) | `Vehicle Thumb` |

Icon phụ đi kèm chữ trên thẻ xe (`gauge`, `map-pin`, `user-round`, `route`) dùng `color/fg/tertiary`, theo DEC-329.

## 3. Sơ đồ lốp `[Lõi]`

Khoá theo **cấu hình trục**, nhìn từ trên, đầu xe hướng lên; nguồn 11 kiểu trong file lốp của khách
(`tyre-mapping.html`). Giữ cả kiểu 5 trục cho khách khác dù Delta chưa có xe.

| Mã | Tên | Trục | Lốp + dự phòng | File khách |
|---|---|---|---|---|
| `tractor-6x4` | Đầu kéo 2 cầu sau (1 dí 2 cầu tải) | 3 | 10 + 1 | Kiểu 1 |
| `tractor-4x2` | Đầu kéo 1 cầu sau (1 dí 1 cầu tải) | 2 | 6 + 1 | Kiểu 2 |
| `truck-4x2` | Xe tải hai trục (1 dí 1 cầu tải) | 2 | 6 + 1 | Kiểu 3 |
| `truck-6x4` | Xe tải ba trục (1 dí 2 cầu tải) | 3 | 10 + 1 | Kiểu 4 |
| `truck-6x2` | Xe tải ba trục (2 dí 1 cầu tải) | 3 | 8 + 1 | Kiểu 5 |
| `truck-8x4` | Xe tải bốn trục (2 dí 2 cầu tải) | 4 | 12 + 1 | Kiểu 6 |
| `truck-5ax` | Xe tải năm trục (tên trong file chưa chốt) | 5 | 16 + 1 | Kiểu 7 |
| `trailer-2ax` | Sơ mi-Rơ mooc 2 giàn | 2 | 8 + 1 | Kiểu 8 |
| `trailer-3ax` | Sơ mi-Rơ mooc 3 giàn | 3 | 12 + 1 | Kiểu 9 |
| `forklift-diesel` | Xe nâng diesel | 2 | 4 | Kiểu 10 |
| `forklift-elec` | Xe nâng điện | 2 | 3 | Kiểu 11 |

Mỗi vị trí lốp (`Tyre Slot`): **Default · Selected · Warning** (đến hạn km/ngày, mòn) **· Error** (hỏng, cần
thay) **· Empty** (chưa lắp, viền đứt). Màu theo nhóm trạng thái Semantic (`warning-*`, `error-*`), không màu riêng.
8 điểm lệch trong file lốp của khách: `docs/vehicle-management/brainstorms/vehicle-management.md` OQ-6…OQ-13.

Màu lốp không mượn token chữ, viền (DEC-334 vh12): số trên nền trạng thái `color/text/white`, lốp lái
`color/fg/tertiary`, Error `color/bg/error/solid`. Vùng chạm (vh13): app phóng 1,5 lần (lốp 24 × 45) và luôn có danh
sách vị trí bên dưới; web nới vùng bấm 24 × 32. Số đo ở `design-system/components/application/tyre-layout.md`.

## 4. Marker bản đồ

| Mức phóng | Bản đồ | Hiển thị |
|---|---|---|
| Gần | ≥ 17 | Ảnh `Top` ghép theo tổ hợp (đầu kéo + mooc + container), xoay theo hướng chạy, dài theo `size_m` |
| Vừa | 12–16 | Chấm tròn màu trạng thái + nhãn biển số |
| Xa | ≤ 11 | Cụm có số đếm (`Map Cluster`) |

`[Lõi]`, không theo khách. Mức phóng là ước lượng theo Web Mercator ở vĩ độ 10,8°, chưa thử trên Vietmap (DEC-334 vh16).
**Cỡ hình:** marker thường 4 px/m, Đang chọn 8 px/m (`vehicles.json` → `marker_px_per_m`); đầu kéo + mooc 40 dài 74 và 147.
Hình không theo tỉ lệ thật của bản đồ: 8 px/m chỉ đúng ở mức 20.

**Nhóm thiếu ảnh `Top`** (`vehicles.json` → `top_fallback`, DEC-334 vh15): xe tải mượn `t03-top`, dài theo `size_m` của
nhóm; thiết bị dùng chấm. Sinh lại ảnh theo BL-264 khi duyệt chi phí.

Nhãn, chấm, cụm dùng `shadow/sm`: vai Marker bản đồ trong `design-system/foundations/effect-styles.md` (vh17).

Loại: **Vehicle** (xe đơn) · **Combo** (đầu kéo + mooc) · **Trailer** (mooc đứng riêng tại chỗ đỗ —
`vehicle-telematics` M2). Ghim điểm Lệnh: `Map Pin` Lấy · Giao.

Trạng thái: **Moving** (chạy) · **Stopped** (dừng, `color/fg/tertiary`) · **Idling** (nổ máy không chạy) · **Offline**
(mất tín hiệu: vị trí cuối + giờ, `color/fg/quaternary`, chấm không mờ, hình mờ) · **Alert** (có sự việc,
`color/bg/error/solid`) · **Selected** (đang chọn: to hơn + viền). Số đo tương phản trên nền đất giả lập, chưa kiểm bản
đồ thật: `design-system/components/application/map-marker.md`.

## 5. Tổ hợp đầu kéo – mooc – container (DEC-267, nguồn `lab-combo`)

Tổ hợp = 1 đầu kéo + 0 hoặc 1 mooc + 0–2 container. Một Lệnh gắn một tổ hợp; đổi được giữa Lệnh (F4, F5).

### 5.1 Quy tắc ghép mooc × cấu hình `[Lõi] [Cấu hình]`

Cơ chế 4 mức là lõi: **Được ✓ · Cảnh báo ⚠ · Chặn ✕ · Cần hỏi ?**. Ma trận mức theo loại mooc là tham số
`P-quy-tac-ghep-mooc`; mặc định sản phẩm:

| Mooc | Rỗng | 1×20 | 2×20 | 1×40 | 1×45 |
|---|---|---|---|---|---|
| `trailer-20` | ✓ | ✓ | ✕ chỉ đủ 1 cont 20 | ✕ dài hơn mooc | ✕ |
| `trailer-40-2ax` | ✓ | ? khoá giữa | ⚠ kiểm VGM với tải mooc | ✓ | ✕ |
| `trailer-40-3ax` | ✓ | ✓ khoá giữa | ✓ | ✓ | ✕ |
| `trailer-45` | ✓ | ? | ? | ? | ✓ |

Ô "?" = chưa chốt (`transport-dispatch` OQ-66, OQ-67). Mooc sàn `trailer-40-flat` theo hàng `trailer-40-2ax`.

### 5.2 Trạng thái một vị trí container (độc lập trạng thái Lệnh)

| State | Nghĩa |
|---|---|
| **No Number** — Chưa có số | Đã xếp chỗ, lái xe chọn vỏ tại bãi rồi nhập số |
| **Empty** — Vỏ rỗng | Lấy vỏ về đóng hàng / trả vỏ sau rút hàng |
| **Loading** — Đang đóng | Có hàng, chưa niêm chì |
| **Loaded** — Có hàng | Đã đóng, có số chì |
| **Swapping** — Đang đổi vỏ | Vỏ hỏng sau khi lên mooc, số cũ gạch, chờ số mới (phí đổi vỏ B5) |
| **Held** — Kiểm hoá | Hải quan giữ kiểm hoá / soi chiếu, tổ hợp chờ |
| **Dropped** — Đã hạ | Container đã hạ (cắt mooc, quay cắt Q1) nhưng còn thuộc Lệnh; khe trống có ghi chú |

Cờ **Reefer** (Boolean) cộng thêm cho Empty, Loading, Loaded, Held: nhiệt độ cài + nguồn điện.
Số container kiểm chữ số cuối ISO 6346.

### 5.3 Bộ trường hợp mẫu (golden set)

13 trường hợp lab: (1) đầu kéo chạy một mình · (2) kéo mooc không container · (3) đã xếp chỗ chưa có số ·
(4) 1×20 vỏ rỗng · (5) 1×20 có hàng · (6) 2×20 cùng Lệnh · (7) 2×20 ghép 2 Lệnh · (8) 1×40 có hàng ·
(9) 1×45 lạnh · (10) F4 mooc trên Lệnh khác mooc đang móc · (11) F5 bỏ mooc giữa đường · (12) chặn 40ft trên
mooc 20ft · (13) đổi vỏ sau khi lên mooc. Thêm 27/10: (14) cắt mooc tại nhà máy · (15) quay cắt mooc đơn vị
khác · (16) kiểm hoá giữ container · (17) đang đóng hàng chưa niêm chì. Component tổ hợp phải hiển thị đúng cả 17.

**Bảng 17 ca × component** (DEC-334 vh18). Đây là bảng kiểm, **chưa dựng trên Figma**: dựng khi sync. Ô "chưa chốt" là
chỗ `lab-combo` chưa vẽ ca đó, quyết khi dựng.

| # | Ca | Combo Text | Combo Slots | Combo Figure | Container Slot | Đặt ngoài component |
|---|---|---|---|---|---|---|
| 1 | Đầu kéo một mình | No Trailer | No Trailer | No Trailer | — | — |
| 2 | Kéo mooc, không container | No Container | Empty | Empty | — | — |
| 3 | Đã xếp chỗ, chưa có số | One Box, "— (chưa có số)" | 1×20 | 1×20 | No Number | Banner chưa có số |
| 4 | 1×20 vỏ rỗng | One Box | 1×20 | 1×20 | Empty | — |
| 5 | 1×20 có hàng | One Box | 1×20 | 1×20 | Loaded | — |
| 6 | 2×20 cùng Lệnh | Two Boxes | 2×20 | 2×20 | ×2, theo từng khe | — |
| 7 | 2×20 ghép 2 Lệnh | Two Boxes, "· LVT-…" | 2×20 | 2×20 | ×2, Has Order | — |
| 8 | 1×40 có hàng | One Box | 1×40 | 1×40 | Loaded | — |
| 9 | 1×45 lạnh | One Box | 1×45 | 1×45, Box đổi `reefer-45` | Loaded, Reefer | — |
| 10 | F4: mooc trên Lệnh khác mooc đang móc | One Box | 1×40 | 1×40 | Empty | Banner F4 |
| 11 | F5: bỏ mooc giữa đường | One Box | 1×40 | 1×40 | Loaded | Hai chặng đầu kéo |
| 12 | Chặn 40ft trên mooc 20ft | One Box | 1×40, Has Error | chưa chốt | Loaded | Cấu hình Chặn bị gạch ở form |
| 13 | Đổi vỏ sau khi lên mooc | One Box | 1×20 | 1×20 | Swapping | Banner đổi vỏ |
| 14 | Cắt mooc tại nhà máy | chưa chốt | chưa chốt | chưa chốt | Dropped | Ghi chú khe trống |
| 15 | Quay cắt mooc đơn vị khác | chưa chốt | chưa chốt | chưa chốt | Dropped | Ghi chú khe trống |
| 16 | Kiểm hoá giữ container | One Box | theo cấu hình | theo cấu hình | Held | — |
| 17 | Đang đóng hàng, chưa niêm chì | One Box | theo cấu hình | theo cấu hình | Loading | — |

### 5.4 Ba cách thể hiện và chỗ dùng

| Cách | Component | Danh sách Lệnh (web) | Chi tiết Lệnh | Form xếp tổ hợp | Thẻ Lệnh app lái xe | Bản đồ |
|---|---|---|---|---|---|---|
| A · Hình ghép tỉ lệ thật | `Combo Figure` | — | ✓ trên (16 px/m) | ✓ xem trước | ✓ nhỏ | ảnh Top khi phóng gần |
| B · Sơ đồ khe | `Combo Slots` | khi mở rộng dòng | ✓ dưới hình | ✓ từng vị trí | danh sách container | popup |
| C · Một dòng chữ | `Combo Text` | ✓ mặc định | — | — | — | nhãn |

Form xếp tổ hợp giữ luồng lab mục 7: đầu kéo → mooc → cấu hình → từng vị trí; cấu hình Chặn bị gạch,
Cảnh báo / Cần hỏi có dấu; hình ghép cập nhật theo lựa chọn. Chi tiết Lệnh: banner F4 / đổi vỏ / chưa có số
đặt đầu khối.

## 6. Component (Application) — dựng tuần tự, mỗi cái một lượt duyệt

**Cả 9 là Nháp** (DEC-334 vh19): DEC-268…276 “user duyệt” là duyệt kế hoạch dựng. Sync từ dưới lên trong lượt riêng, duyệt 1
trang riêng rồi mới `approved`.

| # | Component | Thuộc tính chính | Ráp từ |
|---|---|---|---|
| 1 | `Vehicle Thumb` | Group (22) × Size XS 32 · SM 48 · MD 64, cắt sẵn theo nhóm (DEC-268), bo `radius/inner`; Style qua ảnh lồng | `Vehicle Image` View Q |
| 2 | `Vehicle Card` · `Vehicle Card / Mobile` | Mẫu 7: chữ trái, ảnh Q lấn phải, Badge trạng thái, chân lái xe + tuyến; State (DEC-269); trải theo cột, tối thiểu 304, `shadow/xs` (DEC-334) | `Vehicle Image` Q · Badge |
| 3 | `Vehicle Option Card` · `/ Mobile` | Dòng gọn: Thumb SM · biển số · Badge + "tải trọng · lái xe" · Radio phải; Selected × State, xe không khả dụng = Disabled (DEC-270); trải theo khối chứa (DEC-334) | `Vehicle Thumb` · Badge · Radio |
| 4 | `Container Slot` | State 7 × Density Default · Compact; Reefer, Has Order (DEC-271) | Badge |
| 5 | `Combo Text` | Config No Trailer · No Container · One Box · Two Boxes; Load luôn hiện, Boxes cắt "…", Has Types (DEC-272) | — |
| 6 | `Combo Slots` | Config No Trailer · Empty · 1×20 · 1×20 Center · 2×20 · 1×40 · 1×45 × Density (Compact xếp dọc); Has Error (DEC-273) | `Container Slot` |
| 7 | `Combo Figure` | Config 7 × Scale MD 16 · SM 8 px/m (`scale_px_per_m`); hình chỉ nhận dạng, trạng thái ở Combo Slots (DEC-274) | `Vehicle Image` View=S |
| 8 | `Tyre Layout` · `Tyre Slot` | Layout 11 · Tyre Slot Kind Steer · Load · Spare × State 5 (DEC-275) | `Tyre Slot` |
| 9 | `Map Marker` · `Map Dot` · `Map Cluster` · `Map Pin` | Marker Kind 3 × State 6 · Dot State 6 · Cluster Size 3 · Pin Type 2; xoay chỉ Figure (DEC-276) | `Vehicle Image` View=Top |

Figma (trang DS · Application components, 27/10): Vehicle Thumb 6787:12415 · Vehicle Card 6791:13702 / Mobile
6791:13823 · Vehicle Option Card 6794:14809 / Mobile 6794:14992 · Container Slot 6797:15876 · Combo Text 6801:15783 ·
Combo Slots 6804:16465 · Combo Figure 6806:16351 · Tyre Slot 6808:16502 · Tyre Layout 6808:16848 · Map Marker
6811:17156 · Map Dot 6811:17181 · Map Cluster 6811:17188 · Map Pin 6811:17199. Spec từng cái:
`design-system/components/application/*.md`.

Foundations trên Figma: Section `Vehicles` trên trang `❖ FOUNDATIONS` (khối con: Images · Frames · Tyres ·
Markers) + Section `Demo · Vehicles` (DEC-263, DEC-264). `Vehicle Image` = Group × View × Style.

Figma Section Vehicles: 6779:2086 (master `Vehicle Image` 6777:1914, 79 biến thể; View S và Top theo 16 px/m, khung Top rộng thật 2,5 m — xe nâng 1,2 m) · Demo · Vehicles 6780:1870. User duyệt 27/10. Figma chưa theo DEC-334 (biến, ảnh, 9 component): sync lượt riêng.
