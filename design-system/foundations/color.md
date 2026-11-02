---
type: design-foundations
status: approved
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Màu

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (3.x) để các DEC và spec trích "foundations mục 3…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 3. Màu

### 3.1 Bảng gốc (DEC-130)

11 bậc tên 50–950, tính bằng OKLCH để sáng đều theo mắt. Các mốc giữ đúng giá trị đã duyệt: neutral/100 nền,
300 viền ô nhập, 400 chữ gợi ý, 500 chữ phụ, 900 chữ; mỗi sắc chip nền bậc 50, chữ bậc 700.
Nút chính là than chì #262626 (DEC-119). Màu theo khách là thang riêng 11 bậc của từng khách, xem mục 3.5
(DEC-167, DEC-168).

| Sắc | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Xám trung tính `neutral` (Untitled v8, DEC-260) | #FAFAFA | #F5F5F5 | #E5E5E5 | #D4D4D4 | #A3A3A3 | #737373 | #525252 | #404040 | #262626 | #171717 | #0A0A0A |
| Xanh dương `blue` | #E7EFFD | #D3E2FE | #B5CFFF | #93B9FF | #6C9EFE | #4982F7 | #3468D7 | #1F4FB8 | #163F98 | #0D2F7A | #051F5C |
| Xanh ngọc `teal` | #E2F5F4 | #C6EDEB | #A9DDD9 | #8AC9C5 | #67B3AD | #449D95 | #2B847C | #0B6B64 | #015751 | #01433E | #002F2C |
| Tím `purple` | #EFEAFE | #E3DBFE | #D0C4FF | #B9AAFE | #9E8CFE | #836BFF | #6A50E4 | #5536C4 | #4429A3 | #341C82 | #250F63 |
| Vàng `yellow` | #FFF3DC | #FEE4B6 | #F2D099 | #E3B87A | #D19D59 | #BF8239 | #A56A21 | #8A5300 | #704303 | #573301 | #3F2300 |
| Xanh lá `green` | #E8F5EC | #D3EDDB | #B3E0C1 | #93CFA6 | #6FBB89 | #4CA66D | #348D57 | #1B7542 | #105F34 | #054A26 | #013519 |
| Đỏ `red` | #FDECEC | #FDDBDB | #FFC1BF | #FFA19C | #FC7970 | #F05547 | #D23C2E | #B42318 | #94170E | #760B05 | #580100 |
| Cam `orange` | #FFF7ED | #FBEAD7 | #FFD3AB | #FFB782 | #FE9356 | #F96E34 | #DE5626 | #C2410C | #A03201 | #7E2500 | #5C1901 |
| Than chì `charcoal` | | | | | | | | | #3B3B3B | #262626 | #171717 |

Thang nền tối `dark/0…4` (DEC-316, chỉ cho Dark): `dark/0` **#191919** nền trang · `dark/1` #202020 mặt nổi · `dark/2` #232323 khối phụ, rê chuột · `dark/3` #2B2B2B đang chọn, nút phụ, tắt · `dark/4` #2E2E2E viền.

Thêm: `white` #FFFFFF, `black` #000000, 20 bậc alpha theo Untitled `alpha/white/10…100` và `alpha/black/10…100` (DEC-320); 7 bậc thấp cho màu bóng `alpha/black/3`, `4`, `5`, `6`, `8`, `14`, `18` (DEC-327); riêng của mình: `alpha/neutral-950-35` (#0A0A0A 35%, lớp phủ có làm mờ), `alpha/neutral-950-50` (#0A0A0A 50%, đường lùi và lớp tối trên ảnh), `alpha/dark-0-70` (#191919 70%, thanh mờ ở Dark); `file-type/pdf` #B42318, `doc` #1F4FB8, `xls` #1B7542, `csv` #1B7542, `img` #6A50E4, `zip` #525252, `vid` #B54708 (màu nhận diện loại tệp, DEC-335).

### 3.2 Luật dùng bậc

- Chữ theo sắc (blue, teal, purple, yellow, green, red, orange) trên nền trắng, và nền đặc có chữ trắng, dùng bậc 700 trở lên.
  Xám dùng qua token nghĩa (chữ phụ neutral/500, chip xám neutral/600).
- Bậc 400 chỉ cho chữ gợi ý trong ô và icon tắt (2,52:1), không dùng cho nội dung.
- Chip: nền bậc 50, chữ và icon bậc 700; riêng chip xám nền neutral/100, chữ neutral/600 (DEC-130). Kiểu chip
  (nền nhạt + icon, hay chấm + chữ) chốt luật ở vòng 4 (DEC-126).
- Màu khách đi qua dải riêng của khách và chỉ vào các vai ở mục 3.5 (DEC-167…169); chip trạng thái không đổi
  theo khách; ô chữ cái đầu của khách đúng màu `P-mau-logo`, logo thật không tô ô (mục 3.5).

### 3.3 Token nghĩa (DEC-131, DEC-258, DEC-316, DEC-320)

Tên và mục đích theo Untitled UI v8, dùng `/` thay `-` cho cấp nhóm, giữ `_` cho hậu tố trạng thái (`bg/primary_hover`) vì file bàn giao DTCG không cho một tên vừa là token vừa là nhóm (DEC-320). Giá trị giữ của mình, trừ nhóm Icon. Component gắn thẳng các token này (DEC-318). Web và app dùng chung một bộ màu (DEC-316). Bảng tên cũ → mới: `components/_token-ledger.json` mục `colorRename`.

**Nền.** Tên theo Untitled `bg-*`; giá trị giữ của mình, nền Dark theo thang `dark/*` (DEC-316). Token riêng: `bg/selected`, `bg/pressed`, `bg/skeleton`, `bg/disabled`, `bg/quaternary_hover`, `bg/*/secondary`, `bg/error/primary_hover`, `bg/error/primary_pressed`, các nền `info`.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/bg/disabled` | `neutral/100` | `dark/3` | Nền control tắt: nút, ô nhập, ô chọn (DEC-316) |
| `color/bg/error/primary` | `red/50` | `red/950` | Nền lỗi chính (DEC-320) |
| `color/bg/error/primary_hover` | `red/100` | `red/900` | Nền nhạt nút Danger khi rê chuột. (DEC-320) |
| `color/bg/error/primary_pressed` | `red/200` | `red/800` | Nền nhạt nút Danger khi bấm. (DEC-320) |
| `color/bg/error/secondary` | `red/100` | `red/900` | Nền lỗi phụ: featured icon (DEC-320) |
| `color/bg/error/solid` | `red/700` | `red/700` | Nền lỗi đặc: nút, featured icon, số liệu (DEC-320) |
| `color/bg/error/solid_hover` | `red/800` | `red/600` | Nền lỗi đặc khi rê chuột (DEC-320) |
| `color/bg/info/primary` | `blue/50` | `blue/950` | Nền thông tin chính (DEC-320) |
| `color/bg/info/secondary` | `blue/100` | `blue/900` | Nền thông tin phụ: featured icon (DEC-320) |
| `color/bg/info/solid` | `blue/700` | `blue/700` | Nền thông tin đặc: nút, featured icon, số liệu (DEC-320) |
| `color/bg/info/solid_hover` | `blue/800` | `blue/600` | Nền thông tin đặc khi rê chuột (DEC-320) |
| `color/bg/overlay` | `alpha/neutral-950-35` | `alpha/neutral-950-35` | Nền lớp phủ sau dialog, sheet: 35% + `backdrop-blur/lg` (DEC-258, DEC-327) |
| `color/bg/overlay_solid` | `alpha/neutral-950-50` | `alpha/neutral-950-50` | Đường lùi khi máy không chạy được làm mờ; lớp tối và rãnh vòng tiến độ đè lên ảnh (DEC-321, DEC-327) |
| `color/bg/primary_blur` | `alpha/white/70` | `alpha/dark-0-70` | Nền đầu màn dính và thanh nổi app, đi cùng `backdrop-blur/*` (DEC-327) |
| `color/bg/error/overlay` | `alpha/red-700-55` | `alpha/red-700-55` | Lớp phủ đỏ trên ảnh tải lỗi, không đổi theo Light/Dark vì ảnh không đổi (DEC-321) |
| `color/bg/pressed` | `neutral/200` | `neutral/700` | Nền đang bấm của thứ nền trắng: dòng danh sách, thẻ bấm được (app không có hover); chữ phụ trên nền này dùng text/tertiary_strong (DEC-316) |
| `color/bg/primary` | `white` | `dark/0` | Nền chính cho mọi bố cục và component (DEC-320) |
| `color/bg/primary_alt` | `white` | `dark/1` | Nền trắng ở Light, sáng hơn nền trang ở Dark: menu, dialog, sheet (DEC-320) |
| `color/bg/primary_hover` | `neutral/50` | `dark/2` | Rê chuột trên component nền trắng: menu chọn, dòng bảng (DEC-320) |
| `color/bg/primary_solid` | `neutral/900` | `neutral/200` | Nền tối chính: tooltip, toast trung tính (DEC-320) |
| `color/bg/quaternary` | `neutral/200` | `neutral/700` | Nền cấp 4 trên nền sáng: thanh trượt, thanh tiến độ, thanh kéo sheet (DEC-320, DEC-321) |
| `color/bg/quaternary_hover` | `neutral/300` | `neutral/600` | Rãnh công tắc tắt; rê chuột dùng `fg/quaternary` (DEC-321) |
| `color/bg/secondary` | `neutral/50` | `dark/2` | Nền phụ tạo tương phản với nền trắng (DEC-320) |
| `color/bg/secondary_alt` | `neutral/50` | `dark/0` | Nền phụ thành nền trang ở Dark (tab kiểu viền) (DEC-320) |
| `color/bg/secondary_hover` | `neutral/100` | `dark/3` | Rê chuột trên component nền phụ (DEC-320) |
| `color/bg/secondary_solid` | `neutral/600` | `neutral/600` | Nền tối phụ: featured icon (DEC-320) |
| `color/bg/selected` | `neutral/100` | `dark/3` | Nền mục đang chọn khi khách không có màu riêng. Dùng ở: List Item đang chọn, mục menu đang chọn. |
| `color/bg/skeleton` | `neutral/100` | `dark/3` | Khối chờ tải (skeleton) (DEC-316) |
| `color/bg/success/primary` | `green/50` | `green/950` | Nền thành công chính (DEC-320) |
| `color/bg/success/secondary` | `green/100` | `green/900` | Nền thành công phụ: featured icon (DEC-320) |
| `color/bg/success/solid` | `green/700` | `green/700` | Nền thành công đặc: nút, featured icon, số liệu (DEC-320) |
| `color/bg/success/solid_hover` | `green/800` | `green/600` | Nền thành công đặc khi rê chuột (DEC-320) |
| `color/bg/tertiary` | `neutral/100` | `dark/3` | Nền cấp 3: công tắc tắt (DEC-320) |
| `color/bg/warning/primary` | `yellow/50` | `yellow/950` | Nền cảnh báo chính (DEC-320) |
| `color/bg/warning/secondary` | `yellow/100` | `yellow/900` | Nền cảnh báo phụ: featured icon (DEC-320) |
| `color/bg/warning/solid` | `yellow/700` | `yellow/700` | Nền cảnh báo đặc: nút, featured icon, số liệu (DEC-320) |
| `color/bg/warning/solid_hover` | `yellow/800` | `yellow/600` | Nền cảnh báo đặc khi rê chuột (DEC-320) |

**Chữ.** Tên theo Untitled `text-*`. `text/tertiary` là chữ hỗ trợ mặc định, giữ bậc 500 / 400. Token riêng: `text/tertiary_strong`, `text/inverse`, `text/disabled`, `text/info/primary`.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/text/disabled` | `neutral/400` | `neutral/600` | Chữ control tắt; không dùng cho nội dung (DEC-316, DEC-320) |
| `color/text/error/primary` | `red/700` | `red/300` | Chữ lỗi mặc định (DEC-320) |
| `color/text/error/primary_hover` | `red/700` | `red/300` | Chữ lỗi khi rê chuột (DEC-320) |
| `color/text/info/primary` | `blue/700` | `blue/300` | Chữ thông tin mặc định (DEC-320) |
| `color/text/inverse` | `white` | `neutral/950` | Chữ trên nền đậm. Dùng ở: chữ nút Primary, chữ Tooltip. |
| `color/text/placeholder` | `neutral/500` | `neutral/400` | Chữ gợi ý trong ô nhập |
| `color/text/primary` | `neutral/900` | `neutral/200` | Chữ chính: tiêu đề trang, giá trị chính |
| `color/text/quaternary` | `neutral/500` | `neutral/400` | Chữ nhạt, tương phản thấp (DEC-320) |
| `color/text/secondary` | `neutral/700` | `neutral/300` | Chữ phụ: nhãn, tiêu đề mục (DEC-320) |
| `color/text/secondary_hover` | `neutral/800` | `neutral/200` | Chữ phụ khi rê chuột (DEC-320) |
| `color/text/success/primary` | `green/700` | `green/300` | Chữ thành công mặc định (DEC-320) |
| `color/text/tertiary` | `neutral/500` | `neutral/400` | Chữ hỗ trợ, đoạn văn, thời gian (DEC-320); nhãn trường dùng `text/secondary` (DEC-321) |
| `color/text/tertiary_hover` | `neutral/700` | `neutral/300` | Chữ hỗ trợ khi rê chuột (DEC-320) |
| `color/text/tertiary_strong` | `neutral/600` | `neutral/300` | Chữ phụ trên nền nhấn (hover, đang chọn) để giữ ≥ 4,5:1 (DEC-289). Dùng ở: dòng phụ thẻ phạm vi khi Hover/Open, dòng chọn Hover/Selected của Scope dialog. (DEC-320) |
| `color/text/warning/primary` | `yellow/700` | `yellow/300` | Chữ cảnh báo mặc định (DEC-320) |
| `color/text/white` | `white` | `white` | Luôn trắng, mọi chế độ: chữ trên nền đặc (DEC-320) |

**Icon.** Tên **và giá trị** theo Untitled `fg-*`, quy về màu gốc của mình (user chỉ định, DEC-320). `fg/quaternary` chỉ đạt 2,52:1 trên trắng, dưới ngưỡng 3:1 cho icon mang nghĩa, nên từ DEC-329 (ic12) chỉ dùng cho icon trang trí và disabled; icon phụ mang nghĩa dùng `fg/tertiary`. Token riêng: `fg/inverse`, `fg/disabled`, `fg/info/primary`.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/fg/disabled` | `neutral/400` | `neutral/600` | Icon control tắt (DEC-316, DEC-320) |
| `color/fg/error/primary` | `red/600` | `red/400` | Icon lỗi chính: featured icon (DEC-320) |
| `color/fg/error/secondary` | `red/500` | `red/400` | Icon trong ô lỗi, chỉ số âm (DEC-320) |
| `color/fg/info/primary` | `blue/600` | `blue/400` | Icon thông tin chính: featured icon (DEC-320) |
| `color/fg/inverse` | `white` | `neutral/950` | Icon trên nền đậm đổi theo chế độ: Tooltip, nút Primary (DEC-316, DEC-320) |
| `color/fg/primary` | `neutral/900` | `white` | Icon tương phản cao nhất (DEC-320) |
| `color/fg/quaternary` | `neutral/400` | `neutral/600` | Tương phản thấp, chỉ cho icon trang trí và disabled (DEC-320, DEC-329 ic12) |
| `color/fg/quaternary_hover` | `neutral/500` | `neutral/500` | Icon tương phản thấp khi rê chuột (DEC-320) |
| `color/fg/secondary` | `neutral/700` | `neutral/300` | Phần tử không phải chữ tương phản cao: icon đi cùng chữ chính (DEC-320) |
| `color/fg/secondary_hover` | `neutral/800` | `neutral/200` | Icon khi rê chuột (DEC-320) |
| `color/fg/success/primary` | `green/600` | `green/400` | Icon thành công chính: featured icon (DEC-320) |
| `color/fg/success/secondary` | `green/500` | `green/400` | Chấm online avatar, chấm nút (DEC-320) |
| `color/fg/tertiary` | `neutral/600` | `neutral/400` | Icon tương phản vừa (DEC-320); icon phụ mang nghĩa: chevron ô chọn, icon ô tìm, Help (DEC-329 ic12) |
| `color/fg/tertiary_hover` | `neutral/700` | `neutral/300` | Icon tương phản vừa khi rê chuột (DEC-320) |
| `color/fg/warning/primary` | `yellow/600` | `yellow/400` | Icon cảnh báo chính: featured icon (DEC-320) |
| `color/fg/warning/secondary` | `yellow/500` | `yellow/400` | Cảnh báo phụ (DEC-320) |
| `color/fg/white` | `white` | `white` | Icon luôn trắng, mọi chế độ (DEC-320) |

**Viền.** Tên theo Untitled `border-*`. `border/secondary` là viền mặc định. Token riêng: `border/input` (≥ 3:1 cho ô nhập), `border/disabled`, `border/success*`, `border/warning*`, `border/info*`.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/border/disabled` | `neutral/200` | `dark/4` | Viền control tắt (DEC-316) |
| `color/border/error` | `red/700` | `red/300` | Viền lỗi mặc định: ô nhập, tải tệp (DEC-320) |
| `color/border/error_subtle` | `red/300` | `red/700` | Viền lỗi nhạt hơn (DEC-320) |
| `color/border/info` | `blue/700` | `blue/300` | Viền thông tin (DEC-320) |
| `color/border/info_subtle` | `blue/300` | `blue/700` | Viền thông tin nhạt (DEC-320) |
| `color/border/input` | `neutral/500` | `neutral/500` | Viền tương phản cao (≥ 3:1) cho thứ người dùng nhập hoặc chọn. Dùng ở: Text Field, OTP Field, radio Selectable Card, checkbox, vùng tải tệp (DEC-321). |
| `color/border/input_hover` | `neutral/700` | `neutral/300` | Viền ô nhập khi rê chuột, đậm hơn `border/input` (DEC-321) |
| `color/border/primary` | `neutral/300` | `neutral/700` | Viền tương phản cao hơn mặc định: nhóm nút, nút Secondary (DEC-320) |
| `color/border/secondary` | `neutral/200` | `dark/4` | Viền dùng nhiều nhất, mặc định cho phần lớn component (DEC-320) |
| `color/border/secondary_alt` | `alpha/black/10` | `dark/4` | Biến thể alpha của viền phụ, chỉ dùng cho menu nổi (DEC-320) |
| `color/border/success` | `green/700` | `green/300` | Viền thành công (DEC-320) |
| `color/border/success_subtle` | `green/300` | `green/700` | Viền thành công nhạt (DEC-320) |
| `color/border/tertiary` | `neutral/100` | `dark/2` | Viền tương phản thấp: vạch chia rất nhạt, trục biểu đồ (DEC-320) |
| `color/border/warning` | `yellow/700` | `yellow/300` | Viền cảnh báo (DEC-320) |
| `color/border/warning_subtle` | `yellow/300` | `yellow/700` | Viền cảnh báo nhạt (DEC-320) |

**Focus.** `focus/ring`, `focus/ring_error` theo Untitled; than chì cho mọi khách (DEC-170).

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/focus/ring` | `charcoal/900` | `neutral/200` | Vòng focus mặc định; than chì cho mọi khách (DEC-170) (DEC-320) |
| `color/focus/ring_error` | `red/700` | `red/300` | Vòng focus lỗi (DEC-320) |

**Hành động.** Token riêng của mình: nút cố định than chì, không theo màu khách (DEC-119). Untitled gọi vai này là `bg-brand-solid`; không đổi tên để tránh hiểu nhầm với `accent/*`.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/action/primary` | `charcoal/900` | `neutral/200` | Nền hành động chính. Dùng ở: nút Primary, tab chip đang chọn. |
| `color/action/primary-hover` | `charcoal/800` | `neutral/300` | Nền nút Primary khi rê chuột. |
| `color/action/primary-pressed` | `charcoal/950` | `neutral/400` | Nền nút Primary khi bấm. |
| `color/action/secondary` | `neutral/100` | `dark/3` | Nền hành động phụ và nền xám của trạng thái tắt. Dùng ở: nút Secondary, nút Disabled. |
| `color/action/secondary-hover` | `neutral/200` | `neutral/700` | Nền nút Secondary khi rê chuột. |
| `color/action/secondary-pressed` | `neutral/300` | `neutral/600` | Nền nút Secondary khi bấm; nút Outline dùng chung thang secondary khi rê, bấm. |

**Màu khách.** Đổi theo dải khách ở collection `7. Brand` (mục 3.5).

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/accent/bg` | `color/brand/100` | `color/brand/900` | Màu khách · Nền mục menu đang chọn, nền avatar (DEC-316) |
| `color/accent/bg-subtle` | `color/brand/50` | `color/brand/950` | Màu khách · Nền dòng bảng đang chọn (DEC-316) |
| `color/accent/border` | `color/brand/800` | `color/brand/300` | Màu khách · Viền chỗ đang chọn: thẻ chọn, ô chọn (DEC-316) |
| `color/accent/fg` | `color/brand/800` | `color/brand/200` | Màu khách · Chữ viết tắt, icon avatar trên nền accent/bg (DEC-316) |
| `color/accent/solid` | `color/brand/800` | `color/brand/300` | Màu khách · Công tắc bật, ô chọn, radio, gạch tab đang chọn, thanh tiến độ (DEC-316) |
| `color/accent/solid-hover` | `color/brand/900` | `color/brand/200` | Màu khách · Rê chuột trên phần mang màu khách (DEC-316) |
| `color/accent/solid-pressed` | `color/brand/950` | `color/brand/100` | Màu khách · Đang bấm phần mang màu khách (DEC-316) |
| `color/accent/text` | `color/brand/700` | `color/brand/300` | Màu khách · Chữ liên kết, mã chứng từ (DEC-316) |
| `color/accent/text-hover` | `color/brand/800` | `color/brand/200` | Màu khách · Chữ liên kết khi rê chuột (DEC-316) |

**Thang utility.** Thang theo sắc của Untitled `utility-*`, chỉ gồm các sắc có trong màu gốc của mình. Ở Dark đảo bậc. Chip dùng nền `50`, chữ `700`, viền `200`, chấm `600`; riêng xám nền `100`, chữ `600`, chấm `500`; cam nền `100`, chữ `800` (DEC-311). Biểu đồ dùng bậc `500`, thứ tự cố định: blue, teal, purple, yellow, green, red, orange, neutral.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/utility/blue/50` | `blue/50` | `blue/950` | Chip trạng thái blue: nền. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/blue/100` | `blue/100` | `blue/900` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/blue/200` | `blue/200` | `blue/800` | Chip blue: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/blue/300` | `blue/300` | `blue/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/blue/400` | `blue/400` | `blue/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/blue/500` | `blue/500` | `blue/400` | Chuỗi dữ liệu biểu đồ thứ 1 (DEC-316, DEC-320) |
| `color/utility/blue/600` | `blue/600` | `blue/400` | Chip blue: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/blue/700` | `blue/700` | `blue/300` | Chip trạng thái blue: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/green/50` | `green/50` | `green/950` | Chip trạng thái green: nền. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/green/100` | `green/100` | `green/900` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/green/200` | `green/200` | `green/800` | Chip green: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/green/300` | `green/300` | `green/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/green/400` | `green/400` | `green/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/green/500` | `green/500` | `green/400` | Chuỗi dữ liệu biểu đồ thứ 5 (DEC-316, DEC-320) |
| `color/utility/green/600` | `green/600` | `green/400` | Chip green: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/green/700` | `green/700` | `green/300` | Chip trạng thái green: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/neutral/50` | `neutral/50` | `neutral/950` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/neutral/100` | `neutral/100` | `dark/3` | Chip trạng thái gray: nền. Dùng ở: Status Chip, Status Row. Dark dùng `dark/3` để nổi trên nền #191919 (DEC-320, DEC-323) |
| `color/utility/neutral/200` | `neutral/200` | `neutral/800` | Chip gray: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/neutral/300` | `neutral/300` | `neutral/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/neutral/400` | `neutral/400` | `neutral/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/neutral/500` | `neutral/500` | `neutral/400` | Chip gray: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/neutral/600` | `neutral/600` | `neutral/400` | Chip trạng thái gray: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/neutral/700` | `neutral/700` | `neutral/300` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/orange/50` | `orange/50` | `orange/950` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/orange/100` | `orange/100` | `orange/950` | Chip trạng thái orange: nền. Dùng ở: Status Chip, Status Row. Light orange/100 (review R1, DEC-311: tách khỏi chip vàng). (DEC-320) |
| `color/utility/orange/200` | `orange/200` | `orange/800` | Chip orange: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/orange/300` | `orange/300` | `orange/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/orange/400` | `orange/400` | `orange/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/orange/500` | `orange/500` | `orange/400` | Chuỗi dữ liệu biểu đồ thứ 7 (DEC-316, DEC-320) |
| `color/utility/orange/600` | `orange/600` | `orange/400` | Chip orange: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/orange/700` | `orange/700` | `orange/300` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/orange/800` | `orange/800` | `orange/300` | Chip trạng thái orange: chữ, icon. Dùng ở: Status Chip, Status Row. Light orange/800 (review R1, DEC-311). (DEC-320) |
| `color/utility/purple/50` | `purple/50` | `purple/950` | Chip trạng thái purple: nền. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/purple/100` | `purple/100` | `purple/900` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/purple/200` | `purple/200` | `purple/800` | Chip purple: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/purple/300` | `purple/300` | `purple/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/purple/400` | `purple/400` | `purple/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/purple/500` | `purple/500` | `purple/400` | Chuỗi dữ liệu biểu đồ thứ 3 (DEC-316, DEC-320) |
| `color/utility/purple/600` | `purple/600` | `purple/400` | Chip purple: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/purple/700` | `purple/700` | `purple/300` | Chip trạng thái purple: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/red/50` | `red/50` | `red/950` | Chip trạng thái red: nền. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/red/100` | `red/100` | `red/900` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/red/200` | `red/200` | `red/800` | Chip red: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/red/300` | `red/300` | `red/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/red/400` | `red/400` | `red/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/red/500` | `red/500` | `red/400` | Chuỗi dữ liệu biểu đồ thứ 6 (DEC-316, DEC-320) |
| `color/utility/red/600` | `red/600` | `red/400` | Chip red: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/red/700` | `red/700` | `red/300` | Chip trạng thái red: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/teal/50` | `teal/50` | `teal/950` | Chip trạng thái teal: nền. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/teal/100` | `teal/100` | `teal/900` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/teal/200` | `teal/200` | `teal/800` | Chip teal: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/teal/300` | `teal/300` | `teal/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/teal/400` | `teal/400` | `teal/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/teal/500` | `teal/500` | `teal/400` | Chuỗi dữ liệu biểu đồ thứ 2 (DEC-316, DEC-320) |
| `color/utility/teal/600` | `teal/600` | `teal/400` | Chip teal: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/teal/700` | `teal/700` | `teal/300` | Chip trạng thái teal: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/yellow/50` | `yellow/50` | `yellow/950` | Chip trạng thái yellow: nền. Dùng ở: Status Chip, Status Row. (DEC-320) |
| `color/utility/yellow/100` | `yellow/100` | `yellow/900` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/yellow/200` | `yellow/200` | `yellow/800` | Chip yellow: viền Badge Outline (DEC-308) (DEC-316, DEC-320) |
| `color/utility/yellow/300` | `yellow/300` | `yellow/700` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/yellow/400` | `yellow/400` | `yellow/600` | Thang utility, đảo bậc ở Dark (DEC-320) |
| `color/utility/yellow/500` | `yellow/500` | `yellow/400` | Chuỗi dữ liệu biểu đồ thứ 4 (DEC-316, DEC-320) |
| `color/utility/yellow/600` | `yellow/600` | `yellow/400` | Chip yellow: chấm Badge Dot (DEC-310) (DEC-316, DEC-320) |
| `color/utility/yellow/700` | `yellow/700` | `yellow/300` | Chip trạng thái yellow: chữ, icon. Dùng ở: Status Chip, Status Row. (DEC-320) |

**Bóng.** Màu bóng đổ, đổi theo sáng/tối.

| Token | Light | Dark | Mục đích |
|---|---|---|---|
| `color/shadow/xs` | `alpha/black/5` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xs lớp 1 (DEC-327). |
| `color/shadow/sm_01` | `alpha/black/10` | `alpha/black/60` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/sm lớp 1 (DEC-327). |
| `color/shadow/sm_02` | `alpha/black/10` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/sm lớp 2 (DEC-327). |
| `color/shadow/md_01` | `alpha/black/10` | `alpha/black/60` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/md lớp 1 (DEC-327). |
| `color/shadow/md_02` | `alpha/black/6` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/md lớp 2 (DEC-327). |
| `color/shadow/lg_01` | `alpha/black/8` | `alpha/black/60` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/lg lớp 1 (DEC-327). |
| `color/shadow/lg_02` | `alpha/black/3` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/lg lớp 2 (DEC-327). |
| `color/shadow/lg_03` | `alpha/black/4` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/lg lớp 3 (DEC-327). |
| `color/shadow/xl_01` | `alpha/black/8` | `alpha/black/60` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xl lớp 1 (DEC-327). |
| `color/shadow/xl_02` | `alpha/black/3` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xl lớp 2 (DEC-327). |
| `color/shadow/xl_03` | `alpha/black/4` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/xl lớp 3 (DEC-327). |
| `color/shadow/2xl_01` | `alpha/black/18` | `alpha/black/60` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/2xl lớp 1 (DEC-327). |
| `color/shadow/2xl_02` | `alpha/black/4` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/2xl lớp 2 (DEC-327). |
| `color/shadow/3xl_01` | `alpha/black/14` | `alpha/black/60` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/3xl lớp 1 (DEC-327). |
| `color/shadow/3xl_02` | `alpha/black/4` | `alpha/black/40` | Màu bóng theo Untitled, đổi theo sáng/tối. Dùng trong: shadow/3xl lớp 2 (DEC-327). |

Đủ 15 biến đúng tên Untitled; Dark: lớp `_01` (tán chính) `alpha/black/60`, còn lại `alpha/black/40` (DEC-327). Lớp phủ dùng `color/bg/overlay`; vòng focus là outline, khe trong suốt, không có token khe.

**Ô nền logo đối tác** (DEC-338): `color/logo/bg`, Light và Dark đều `white`, dùng cho ô của Bank logo để logo màu không chìm trên nền Tối.

**Màu nhận diện loại tệp** (DEC-335 ms02): nền nhãn File type icon, không đảo theo chế độ, chữ `color/fg/white`. Không mang nghĩa trạng thái. Luật dùng: [icon-sets.md](icon-sets.md).

| Biến | Light | Dark |
|---|---|---|
| `color/file-type/pdf` | `file-type/pdf` | `file-type/pdf` |
| `color/file-type/doc` | `file-type/doc` | `file-type/doc` |
| `color/file-type/xls` | `file-type/xls` | `file-type/xls` |
| `color/file-type/csv` | `file-type/csv` | `file-type/csv` |
| `color/file-type/img` | `file-type/img` | `file-type/img` |
| `color/file-type/zip` | `file-type/zip` | `file-type/zip` |
| `color/file-type/vid` | `file-type/vid` | `file-type/vid` |

### 3.4 Tương phản đo được

Máy đo Light mỗi lần chạy `python3 _scripts/ds-v2-tokens.py --check`. Bảng dưới đo cả Dark; màu khách đo ở dải Than chì
(8 dải: mục 3.5). Chữ cần 4,5:1; viền, control, chấm cần 3:1 (WCAG 1.4.11). Chữ tắt miễn (`text/disabled` 2,52:1).

| Cặp | Cần | Light | Dark |
|---|---|---|---|
| `text/primary` trên `bg/primary` | 4.5:1 | 17,93 | 13,96 |
| `text/tertiary` trên `bg/primary` | 4.5:1 | 4,74 | 6,97 |
| `text/tertiary` trên `bg/secondary` | 4.5:1 | 4,54 | 6,23 |
| `text/tertiary` trên `bg/primary_alt` | 4.5:1 | 4,74 | 6,46 |
| `text/tertiary_strong` trên `bg/selected` | 4.5:1 | 7,17 | 9,55 |
| `text/tertiary_strong` trên `bg/pressed` | 4.5:1 | 6,20 | 6,99 |
| `text/secondary` trên `bg/primary` | 4.5:1 | 10,37 | 11,86 |
| `text/placeholder` trên `bg/primary` | 4.5:1 | 4,74 | 6,97 |
| `text/inverse` trên `action/primary` | 4.5:1 | 15,13 | 15,72 |
| `text/inverse` trên `text/error/primary` | 4.5:1 | 6,57 | 10,21 |
| `text/primary` trên `action/secondary` | 4.5:1 | 16,44 | 11,24 |
| `accent/text` trên `bg/primary` | 4.5:1 | 10,37 | 9,56 |
| `accent/fg` trên `accent/bg` | 4.5:1 | 12,69 | 12,70 |
| `text/white` trên `bg/success/solid` | 4.5:1 | 5,72 | 5,72 |
| `text/white` trên `bg/warning/solid` | 4.5:1 | 6,33 | 6,33 |
| `text/white` trên `bg/error/solid` | 4.5:1 | 6,57 | 6,57 |
| `text/white` trên `bg/info/solid` | 4.5:1 | 7,32 | 7,32 |
| `text/success/primary` trên `bg/success/primary` | 4.5:1 | 5,10 | 7,69 |
| `text/warning/primary` trên `bg/warning/primary` | 4.5:1 | 5,76 | 7,85 |
| `text/error/primary` trên `bg/error/primary` | 4.5:1 | 5,76 | 7,63 |
| `text/info/primary` trên `bg/info/primary` | 4.5:1 | 6,33 | 7,83 |
| `utility/neutral/600` trên `utility/neutral/100` | 4.5:1 | 7,17 | 5,62 |
| `utility/blue/700` trên `utility/blue/50` | 4.5:1 | 6,33 | 7,83 |
| `utility/teal/700` trên `utility/teal/50` | 4.5:1 | 5,63 | 7,79 |
| `utility/purple/700` trên `utility/purple/50` | 4.5:1 | 6,59 | 7,72 |
| `utility/yellow/700` trên `utility/yellow/50` | 4.5:1 | 5,76 | 7,85 |
| `utility/green/700` trên `utility/green/50` | 4.5:1 | 5,10 | 7,69 |
| `utility/red/700` trên `utility/red/50` | 4.5:1 | 5,76 | 7,63 |
| `utility/orange/800` trên `utility/orange/100` | 4.5:1 | 6,05 | 7,74 |
| `border/input` trên `bg/primary` | 3:1 | 4,74 | 3,71 |
| `accent/solid` trên `bg/primary` | 3:1 | 15,13 | 9,56 |
| `focus/ring` trên `bg/primary` | 3:1 | 15,13 | 13,96 |
| `utility/neutral/500` trên `bg/primary` | 3:1 | 4,74 | 6,97 |
| `utility/blue/600` trên `bg/primary` | 3:1 | 5,11 | 6,66 |
| `utility/teal/600` trên `bg/primary` | 3:1 | 4,47 | 7,22 |
| `utility/purple/600` trên `bg/primary` | 3:1 | 5,41 | 6,39 |
| `utility/yellow/600` trên `bg/primary` | 3:1 | 4,48 | 7,27 |
| `utility/green/600` trên `bg/primary` | 3:1 | 4,12 | 7,66 |
| `utility/red/600` trên `bg/primary` | 3:1 | 4,74 | 6,79 |
| `utility/orange/600` trên `bg/primary` | 3:1 | 3,84 | 7,97 |
| `fg/white` trên `file-type/pdf` | 4.5:1 | 6,57 | 6,57 |
| `fg/white` trên `file-type/doc` | 4.5:1 | 7,32 | 7,32 |
| `fg/white` trên `file-type/xls`, `csv` | 4.5:1 | 5,72 | 5,72 |
| `fg/white` trên `file-type/img` | 4.5:1 | 5,41 | 5,41 |
| `fg/white` trên `file-type/zip` | 4.5:1 | 7,81 | 7,81 |
| `fg/white` trên `file-type/vid` | 4.5:1 | 5,43 | 5,43 |

### 3.5 Màu theo khách (DEC-167, DEC-168, DEC-169, DEC-170)

- Mỗi khách một dải 11 bậc `color/brand/50…950`, là thang riêng, không thay bảng gốc mục 3.1. Có 8 dải dựng sẵn;
  màu logo khách gán vào dải gần sắc nhất, lệch quá 30° thì dùng dải Than chì. Khách không khai màu dùng dải Than chì,
  nhìn giữ như bản đã duyệt (DEC-168).
- Một cách áp cho mọi khách, kiểu chạm nhẹ; không có tham số theo khách (DEC-167, DEC-169).
- Nút chính giữ `color/action/primary` than chì (DEC-119). Vòng focus và viền ô đang gõ giữ `color/focus/ring` than chì
  (DEC-170). Chip trạng thái giữ 8 sắc cố định (DEC-130). Logo thật của khách đặt thẳng trên nền, không tô ô; `P-mau-logo` chỉ tô ô khi hiện chữ cái đầu, đúng mã khách khai, không lấy từ dải (DEC-326, [logo.md](logo.md) mục 14.4).

Vai màu khách đi qua nhóm Semantic `color/accent/*` (DEC-316); component **không trỏ thẳng** `color/brand/N`. Dark lấy bậc sáng của chính dải khách, nên dải Brand không cần chế độ Dark.

| Token | Light | Dark | Vai trên màn |
|---|---|---|---|
| `color/accent/solid` | `brand/800` | `brand/300` | Công tắc bật, ô chọn, radio, gạch tab đang chọn, thanh tiến độ |
| `color/accent/solid-hover` | `brand/900` | `brand/200` | Rê chuột trên phần mang màu khách |
| `color/accent/solid-pressed` | `brand/950` | `brand/100` | Đang bấm phần mang màu khách |
| `color/accent/text` | `brand/700` | `brand/300` | Chữ liên kết, mã chứng từ |
| `color/accent/text-hover` | `brand/800` | `brand/200` | Chữ liên kết khi rê chuột |
| `color/accent/fg` | `brand/800` | `brand/200` | Chữ viết tắt, icon avatar trên nền accent/bg |
| `color/accent/bg` | `brand/100` | `brand/900` | Nền mục menu đang chọn, nền avatar |
| `color/accent/bg-subtle` | `brand/50` | `brand/950` | Nền dòng bảng đang chọn |
| `color/accent/border` | `brand/800` | `brand/300` | Viền chỗ đang chọn: thẻ chọn, ô chọn |

Chữ, dấu tích trên `accent/solid`: `color/text/inverse` (Light trắng; Dark đen vì phần đặc ở Dark là bậc 300 sáng).

| Dải | Sắc | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Than chì | mặc định | #F5F5F5 | #EBEBEB | #D9D9D9 | #BFBFBF | #999999 | #737373 | #575757 | #404040 | #262626 | #171717 | #0A0A0A |
| Xanh lá | 154° (Delta #1B7B46) | #F0F8F2 | #DFF1E3 | #C2E3CB | #98CFA8 | #64B47F | #239857 | #027C42 | #026535 | #004F28 | #00381B | #00220E |
| Xanh ngọc | 190° | #EDF9F7 | #D9F1EF | #B6E4E0 | #81D0CA | #2DB6AF | #0A938E | #047773 | #03615D | #024C49 | #003634 | #00201F |
| Xanh dương | 255° | #F0F6FE | #E0ECFD | #C4DBF9 | #9EC2F1 | #6FA3E5 | #4081D2 | #1D67BB | #0A529F | #003F80 | #002C5E | #001A3D |
| Chàm | 272° | #F3F5FE | #E5EBFD | #CED8FA | #ADBDF2 | #889BE6 | #6478D3 | #4B5DBC | #3B4AA0 | #2C3882 | #1D2661 | #0E1442 |
| Tím | 300° | #F7F4FD | #EDE8FB | #DED3F5 | #C7B4EB | #AB90DB | #8E6AC7 | #764EAF | #613C94 | #4C2C78 | #371D59 | #220C3C |
| Đỏ đô | 18° | #FEF3F3 | #FCE5E5 | #F7CDCD | #EEABAC | #DD8285 | #C65860 | #AD3946 | #912835 | #751A27 | #560D19 | #3A010A |
| Cam đất | 45° | #FDF3EF | #FBE6DD | #F5D0C0 | #EBB096 | #DA8964 | #C26030 | #A94400 | #8A3600 | #6D2900 | #501B00 | #330D00 |

Tương phản đo trên Figma (section Màu thương hiệu theo khách 6159:49228): chữ trắng trên bậc 800 từ 9,77:1 (Xanh lá) tới
15,13:1 (Than chì); bậc 700 trên nền trắng từ 7,20:1; bậc 800 trên bậc 50 từ 9,03:1.

Trong `tokens.json`: collection `Brand`, 8 chế độ (mỗi chế độ một dải), biến `color/brand/50…950`; Figma có collection
`Brand` cùng tên chế độ. CSS: đặt `data-brand="<slug>"` trên thẻ gốc theo khách: `than-chi` (mặc định), `xanh-la`,
`xanh-ngoc`, `xanh-duong`, `cham`, `tim`, `do-do`, `cam-dat`. Bậc 200–600 chưa có vai nên ẩn khỏi bảng chọn biến trên
Figma. Dải không có chế độ Dark: Dark đi qua `color/accent/*` (DEC-316).

### 3.6 Chế độ tối (DEC-257, DEC-316)

Nền Dark là **#191919** (`dark/0`), không phải đen gần tuyệt đối: bản cũ nền #0A0A0A + chữ #F5F5F5 đạt 18,2:1, chói khi nhìn
lâu. Mặt nổi sáng dần theo thang `dark/0…4`; chữ chính `neutral/200` #E5E5E5 (14,0:1).

| Vai | Dark | Ghi chú |
|---|---|---|
| Nền trang, thẻ (`bg/primary`) | `dark/0` #191919 | |
| Mặt nổi: menu, dialog, sheet, toast (`bg/primary_alt`) | `dark/1` #202020 | bóng đổ khó thấy trên nền tối, mặt nổi sáng hơn nền |
| Khối phụ, rê chuột (`bg/secondary`, `bg/primary_hover`) | `dark/2` #232323 | |
| Đang chọn, nút phụ, tắt, chờ tải (`bg/selected`, `action/secondary`, `bg/disabled`, `bg/skeleton`, `bg/secondary_hover`) | `dark/3` #2B2B2B | |
| Viền thẻ, viền tắt, viền menu (`border/secondary`, `border/disabled`, `border/secondary_alt`) | `dark/4` #2E2E2E | |
| Đang bấm, rãnh (`bg/pressed`, `bg/quaternary`) | `neutral/700` #404040 | |
| Chữ chính, nút chính, vòng focus, nền tooltip (`text/primary`, `action/primary`, `focus/ring`, `bg/primary_solid`) | `neutral/200` #E5E5E5 | nút: rê chuột 300, bấm 400; chữ trên nút `neutral/950` |
| Chữ phụ, icon phụ, chữ gợi ý | `neutral/400` #A3A3A3 | 6,97:1 trên nền |
| Chữ phụ trên nền nhấn (`text/tertiary_strong`) | `neutral/300` #D4D4D4 | Dark "strong" là bậc sáng hơn; 400 trên nền đang bấm chỉ 4,11:1 |
| Viền ô nhập (`border/input`) | `neutral/500` #737373 | 3,71:1 — đủ 3:1, đỡ sáng hơn 400 |
| Chữ trên nền đặc trạng thái (`text/white`) | `white` | nền `status/*-solid` giữ bậc 700 ở Dark; `text/inverse` (đen) chỉ đạt 2,70–3,46:1 |

Chip và trạng thái đảo bậc (nền 950, chữ 300; viền chip 800, chấm 400). Màu khách ở Dark: mục 3.5. Giá trị máy đọc:
`tokens.json` › Semantic › Dark.
