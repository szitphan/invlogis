---
type: design-foundations
status: draft
updated: 2026-10-19
links:
  - design/v2/architecture.md
  - design/v2/tokens.json
  - design/v2/tokens.css
  - _workspace/decisions.md
---

# Design System v2 — nền tảng (Foundations)

> Kết quả vòng 2/6, chốt 16–17/10/2026 trên trang phỏng vấn https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU
> (DEC-119…139); bổ sung 19/10 từ phần khoảng cách, màu theo khách và vòng 4 (DEC-164…170, DEC-173, DEC-176,
> DEC-179, DEC-192…194, DEC-196). File này là **luật dùng**. Giá trị máy đọc nằm ở `design/v2/tokens.json`; `tokens.css` sinh ra từ
> json bằng `python3 _scripts/ds-v2-tokens.py`. Bảng trong file này lệch json thì **json thắng**.
> Trên Figma: trang `🎨 DS · Foundations` (collection Primitives, Semantic, Platform; text style `type/*`; effect style `elev/*`).

## 1. Nguồn tham chiếu (DEC-128, DEC-129)

| Nền tảng | Nguồn chính | Dùng để |
|---|---|---|
| App iOS, Android | Apple Human Interface Guidelines, Material Design 3 | Thang chữ app, vùng chạm, bo góc, lớp nổi |
| Web | Atlassian Design System (hệ dựng ra Jira, DEC-127) | Thang chữ web, khoảng cách, cao control, bảng |
| Web thích ứng | Material 3 (window size classes) | Cách đổi bố cục theo bề rộng (xét khi làm bản tablet) |
| Trợ năng | WCAG 2.2 | Tương phản, vùng chạm, vòng focus |
| Đối chiếu | Tailwind CSS, Ant Design | Chỉ để so; dev quen thang của Tailwind |

Số của các hệ lấy từ trang gốc ngày 16/10/2026 (bảng nguồn trên trang phỏng vấn).

## 2. Cấu trúc token (DEC-114, DEC-115, DEC-116)

| Tầng | Collection Figma | Chế độ | Ví dụ | Ai được gắn |
|---|---|---|---|---|
| Gốc | `Primitives` | Value | `neutral/900`, `space/16`, `radius/12` | Chỉ token tầng trên trỏ tới; ẩn khỏi bảng chọn |
| Nghĩa | `Semantic` | Light, Dark | `color/text/secondary` | Component, màn |
| Nền tảng | `Platform` | Web, Mobile | `radius/card`, `type/body/size`, `layout/screen-inset` | Component, màn |
| Component | `Component` | Value | `button/bg/primary`, `button/fg/danger` (DEC-174, DEC-197), `avatar/bg` (DEC-201), `tooltip/bg` (DEC-206) | Component nhiều trạng thái |
| Theo khách | `Brand` | 8 dải | `color/brand/800` | Component, màn, theo vai mục 3.5 |

- Component và màn **không gắn Primitives, không ghi mã màu trần**. Cần màu mới thì thêm token nghĩa.
- Màn đặt chế độ `Platform` một lần ở khung màn (Web hoặc Mobile); chữ, bo góc, khoảng cách bên trong tự đổi.
  Trong code: `data-platform="mobile"` trên khung trang (mặc định là web), `data-theme="dark"` cho chế độ tối.
- Dark đang là bản sao của Light; giá trị tối điền và kiểm ở vòng sau (DEC-116).
- Tên CSS = `--` + tên token thay `/` bằng `-`: `color/bg/canvas` → `var(--color-bg-canvas)`. Biến Figma có code syntax WEB đúng tên này.

## 3. Màu

### 3.1 Bảng gốc (DEC-130)

11 bậc tên 50–950, tính bằng OKLCH để sáng đều theo mắt. Các mốc giữ đúng giá trị đã duyệt: neutral/100 nền,
300 viền ô nhập, 400 chữ gợi ý, 500 chữ phụ, 900 chữ; mỗi sắc chip nền bậc 50, chữ bậc 700.
Nút chính là than chì #262626 (DEC-119). Màu theo khách là thang riêng 11 bậc của từng khách, xem mục 3.5
(DEC-167, DEC-168).

| Sắc | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Xám lạnh `neutral` | #F9FAFC | #F2F4F7 | #E3E6EC | #D0D5DD | #98A2B3 | #5F6B7A | #495363 | #374050 | #232C3A | #121826 | #070C16 |
| Xanh dương `blue` | #E7EFFD | #D3E2FE | #B5CFFF | #93B9FF | #6C9EFE | #4982F7 | #3468D7 | #1F4FB8 | #163F98 | #0D2F7A | #051F5C |
| Xanh ngọc `teal` | #E2F5F4 | #C6EDEB | #A9DDD9 | #8AC9C5 | #67B3AD | #449D95 | #2B847C | #0B6B64 | #015751 | #01433E | #002F2C |
| Tím `purple` | #EFEAFE | #E3DBFE | #D0C4FF | #B9AAFE | #9E8CFE | #836BFF | #6A50E4 | #5536C4 | #4429A3 | #341C82 | #250F63 |
| Vàng `yellow` | #FFF3DC | #FEE4B6 | #F2D099 | #E3B87A | #D19D59 | #BF8239 | #A56A21 | #8A5300 | #704303 | #573301 | #3F2300 |
| Xanh lá `green` | #E8F5EC | #D3EDDB | #B3E0C1 | #93CFA6 | #6FBB89 | #4CA66D | #348D57 | #1B7542 | #105F34 | #054A26 | #013519 |
| Đỏ `red` | #FDECEC | #FDDBDB | #FFC1BF | #FFA19C | #FC7970 | #F05547 | #D23C2E | #B42318 | #94170E | #760B05 | #580100 |
| Cam `orange` | #FFF7ED | #FBEAD7 | #FFD3AB | #FFB782 | #FE9356 | #F96E34 | #DE5626 | #C2410C | #A03201 | #7E2500 | #5C1901 |
| Than chì `charcoal` | | | | | | | | | #3B3B3B | #262626 | #171717 |

Thêm: `white` #FFFFFF, `alpha/neutral-950-50` (#070C16 độ mờ 50%, cho nền mờ sau dialog, sheet).

### 3.2 Luật dùng bậc

- Chữ theo sắc (blue, teal, purple, yellow, green, red, orange) trên nền trắng, và nền đặc có chữ trắng, dùng bậc 700 trở lên.
  Xám dùng qua token nghĩa (chữ phụ neutral/500, chip xám neutral/600).
- Bậc 400 chỉ cho chữ gợi ý trong ô và icon tắt (2,58:1), không dùng cho nội dung.
- Chip: nền bậc 50, chữ và icon bậc 700; riêng chip xám nền neutral/100, chữ neutral/600 (DEC-130). Kiểu chip
  (nền nhạt + icon, hay chấm + chữ) chốt luật ở vòng 4 (DEC-126).
- Màu khách đi qua dải riêng của khách và chỉ vào các vai ở mục 3.5 (DEC-167…169); chip trạng thái không đổi
  theo khách; ô logo luôn đúng màu logo khách.

### 3.3 Token nghĩa (DEC-131)

Tên dạng `color/{nhóm}/{vai}`. Cột HIG, Material 3, Atlassian để dev iOS, Android, web map sang hệ họ quen.
Material 3 không có vai thành công, cảnh báo, thông tin: mình tự thêm (`color/status/*`).

| Token | Trỏ tới | Dùng cho | Apple HIG | Material 3 | Atlassian |
|---|---|---|---|---|---|
| `color/bg/canvas` | `neutral/100` | Nền trang chủ mobile, vùng ngoài thẻ | systemGroupedBackground | surface-container-low | `elevation.surface.sunken` |
| `color/bg/surface` | `white` | Thẻ, bảng, màn danh sách | secondarySystemGroupedBackground | surface-container-lowest | `elevation.surface` |
| `color/bg/muted` | `neutral/100` | Ô nhập mobile, khối phụ trong thẻ | tertiarySystemFill | surface-container-highest | `color.background.input` |
| `color/bg/hover` | `neutral/50` | Rê chuột dòng bảng, mục menu | — (iOS không có hover) | lớp trạng thái on-surface 8% | `color.background.neutral.subtle.hovered` |
| `color/bg/selected` | `neutral/100` | Dòng, mục đang chọn (kèm vạch than chì); khách có màu thì theo dải, mục 3.5 | systemFill | secondary-container | `color.background.selected` |
| `color/bg/inverse` | `neutral/900` | Toast, tooltip | — | inverse-surface | `color.background.inverse.subtle` |
| `color/text/primary` | `neutral/900` | Chữ chính | label | on-surface | `color.text` |
| `color/text/secondary` | `neutral/500` | Chữ phụ, nhãn trường | secondaryLabel | on-surface-variant | `color.text.subtle` |
| `color/text/tertiary` | `neutral/400` | Gợi ý trong ô, chữ tắt; không dùng cho nội dung | tertiaryLabel · placeholderText | on-surface 38% (tắt) | `color.text.subtlest` |
| `color/text/inverse` | `white` | Chữ trên nền đậm, chữ nút chính | — | inverse-on-surface · on-primary | `color.text.inverse` |
| `color/icon/primary` | `neutral/700` | Icon đi cùng chữ chính | label | on-surface | `color.icon` |
| `color/icon/secondary` | `neutral/500` | Chevron, icon trong ô tìm | secondaryLabel | on-surface-variant | `color.icon.subtle` |
| `color/border/default` | `neutral/200` | Viền thẻ, kẻ bảng | separator | outline-variant | `color.border` |
| `color/border/strong` | `neutral/300` | Viền tách khối đậm hơn mặc định; ô nhập dùng `color/border/input` | opaqueSeparator | outline | `color.border.bold` |
| `color/border/input` | `neutral/500` | Viền ô nhập web và app, viền radio chưa chọn (DEC-179) | separator (đậm) | outline | `color.border.input` |
| `color/border/focus` | `charcoal/900` | Vòng focus 2px, viền ô đang gõ 2px; than chì cho mọi khách (DEC-170) | tint (vòng focus bàn phím) | secondary (vòng focus) | `color.border.focused` |
| `color/action/primary` | `charcoal/900` | Nút chính, tab chip đang chọn | tintColor · accentColor | primary | `color.background.brand.bold` |
| `color/action/primary-hover` | `charcoal/800` | Rê chuột nút chính | — | primary + lớp on-primary 8% | `color.background.brand.bold.hovered` |
| `color/action/primary-pressed` | `charcoal/950` | Đang bấm nút chính | — (hệ thống tự làm tối) | primary + lớp on-primary 10% | `color.background.brand.bold.pressed` |
| `color/action/secondary` | `neutral/100` | Nút phụ | secondarySystemFill | secondary-container | `color.background.neutral` |
| `color/action/secondary-hover` | `neutral/200` | Rê chuột nút phụ | — | secondary-container + lớp 8% | `color.background.neutral.hovered` |
| `color/action/danger` | `red/700` | Chữ, icon nút Danger: xoá, huỷ lệnh (DEC-176) | systemRed | error | `color.text.danger` |
| `color/action/danger-subtle` | `red/50` | Nền nút Danger: nền đỏ nhạt, chữ đỏ (DEC-176) | systemRed (nhạt) | error-container | `color.background.danger` |
| `color/status/success-bg` | `green/50` | Thông báo thành công: nền | systemGreen | — (không có, tự thêm) | `color.background.success` |
| `color/status/success-fg` | `green/700` | Thông báo thành công: chữ, icon | systemGreen | — (không có, tự thêm) | `color.text.success` |
| `color/status/warning-bg` | `yellow/50` | Cảnh báo: nền | systemOrange · systemYellow | — (không có, tự thêm) | `color.background.warning` |
| `color/status/warning-fg` | `yellow/700` | Cảnh báo: chữ, icon | systemOrange · systemYellow | — (không có, tự thêm) | `color.text.warning` |
| `color/status/danger-bg` | `red/50` | Lỗi: nền | systemRed | error-container · on-error-container | `color.background.danger` |
| `color/status/danger-fg` | `red/700` | Lỗi: chữ, icon | systemRed | error-container · on-error-container | `color.text.danger` |
| `color/status/info-bg` | `blue/50` | Thông tin: nền | systemBlue | — (không có, tự thêm) | `color.background.information` |
| `color/status/info-fg` | `blue/700` | Thông tin: chữ, icon | systemBlue | — (không có, tự thêm) | `color.text.information` |
| `color/chip/gray/bg` | `neutral/100` | Chip trạng thái gray: nền | systemGray | — (dùng tertiary hoặc tự thêm) | `color.background.accent.gray.subtler` |
| `color/chip/gray/fg` | `neutral/600` | Chip trạng thái gray: chữ, icon | systemGray | — | `color.text.accent.gray` |
| `color/chip/blue/bg` | `blue/50` | Chip trạng thái blue: nền | systemBlue | — (dùng tertiary hoặc tự thêm) | `color.background.accent.blue.subtler` |
| `color/chip/blue/fg` | `blue/700` | Chip trạng thái blue: chữ, icon | systemBlue | — | `color.text.accent.blue` |
| `color/chip/teal/bg` | `teal/50` | Chip trạng thái teal: nền | systemTeal | — (dùng tertiary hoặc tự thêm) | `color.background.accent.teal.subtler` |
| `color/chip/teal/fg` | `teal/700` | Chip trạng thái teal: chữ, icon | systemTeal | — | `color.text.accent.teal` |
| `color/chip/purple/bg` | `purple/50` | Chip trạng thái purple: nền | systemPurple | — (dùng tertiary hoặc tự thêm) | `color.background.accent.purple.subtler` |
| `color/chip/purple/fg` | `purple/700` | Chip trạng thái purple: chữ, icon | systemPurple | — | `color.text.accent.purple` |
| `color/chip/yellow/bg` | `yellow/50` | Chip trạng thái yellow: nền | systemYellow | — (dùng tertiary hoặc tự thêm) | `color.background.accent.yellow.subtler` |
| `color/chip/yellow/fg` | `yellow/700` | Chip trạng thái yellow: chữ, icon | systemYellow | — | `color.text.accent.yellow` |
| `color/chip/green/bg` | `green/50` | Chip trạng thái green: nền | systemGreen | — (dùng tertiary hoặc tự thêm) | `color.background.accent.green.subtler` |
| `color/chip/green/fg` | `green/700` | Chip trạng thái green: chữ, icon | systemGreen | — | `color.text.accent.green` |
| `color/chip/red/bg` | `red/50` | Chip trạng thái red: nền | systemRed | — (dùng tertiary hoặc tự thêm) | `color.background.accent.red.subtler` |
| `color/chip/red/fg` | `red/700` | Chip trạng thái red: chữ, icon | systemRed | — | `color.text.accent.red` |
| `color/chip/orange/bg` | `orange/50` | Chip trạng thái orange: nền | systemOrange | — (dùng tertiary hoặc tự thêm) | `color.background.accent.orange.subtler` |
| `color/chip/orange/fg` | `orange/700` | Chip trạng thái orange: chữ, icon | systemOrange | — | `color.text.accent.orange` |
| `color/overlay/scrim` | `alpha/neutral-950-50` | Nền mờ sau dialog, sheet | — (hệ thống tự làm mờ) | scrim | `color.blanket` |

### 3.4 Tương phản đo được (Light)

Máy đo mỗi lần chạy `python3 _scripts/ds-v2-tokens.py --check`; dưới 4,5:1 thì script báo lỗi (trừ chữ gợi ý, chỉ báo cáo).

| Tương phản | Cặp chữ trên nền |
|---|---|
| 17.73:1 | `color/text/primary` trên `color/bg/surface` |
| 16.09:1 | `color/text/primary` trên `color/bg/canvas` |
| 5.43:1 | `color/text/secondary` trên `color/bg/surface` |
| 4.92:1 | `color/text/secondary` trên `color/bg/canvas` |
| 4.92:1 | `color/text/secondary` trên `color/bg/muted` |
| 15.13:1 | `color/text/inverse` trên `color/action/primary` |
| 6.57:1 | `color/text/inverse` trên `color/action/danger` |
| 5.76:1 | `color/action/danger` trên `color/action/danger-subtle` (nút Danger) |
| 16.09:1 | `color/text/primary` trên `color/action/secondary` |
| 2.58:1 | `color/text/tertiary` trên `color/bg/surface` (chỉ báo cáo: chữ gợi ý, chữ tắt) |
| 5.10:1 | `color/status/success-fg` trên `color/status/success-bg` |
| 5.76:1 | `color/status/warning-fg` trên `color/status/warning-bg` |
| 5.76:1 | `color/status/danger-fg` trên `color/status/danger-bg` |
| 6.33:1 | `color/status/info-fg` trên `color/status/info-bg` |
| 7.06:1 | `color/chip/gray/fg` trên `color/chip/gray/bg` |
| 6.33:1 | `color/chip/blue/fg` trên `color/chip/blue/bg` |
| 5.63:1 | `color/chip/teal/fg` trên `color/chip/teal/bg` |
| 6.59:1 | `color/chip/purple/fg` trên `color/chip/purple/bg` |
| 5.76:1 | `color/chip/yellow/fg` trên `color/chip/yellow/bg` |
| 5.10:1 | `color/chip/green/fg` trên `color/chip/green/bg` |
| 5.76:1 | `color/chip/red/fg` trên `color/chip/red/bg` |
| 4.88:1 | `color/chip/orange/fg` trên `color/chip/orange/bg` |

Viền cần 3:1 (WCAG 1.4.11): `color/border/input` 5.43:1 trên `color/bg/surface`, 4.92:1 cạnh `color/bg/muted` (ô app nền xám).

### 3.5 Màu theo khách (DEC-167, DEC-168, DEC-169, DEC-170)

- Mỗi khách một dải 11 bậc `color/brand/50…950`, là thang riêng, không thay bảng gốc mục 3.1. Có 8 dải dựng sẵn;
  màu logo khách gán vào dải gần sắc nhất, lệch quá 30° thì dùng dải Than chì. Khách không khai màu dùng dải Than chì,
  nhìn giữ như bản đã duyệt (DEC-168).
- Một cách áp cho mọi khách, kiểu chạm nhẹ; không có tham số theo khách (DEC-167, DEC-169).
- Nút chính giữ `color/action/primary` than chì (DEC-119). Vòng focus và viền ô đang gõ giữ `color/border/focus` than chì
  (DEC-170). Chip trạng thái giữ 8 sắc cố định (DEC-130). Ô logo luôn đúng màu logo khách (`P-mau-logo`), không lấy từ dải.

| Bậc của dải | Vai trên màn |
|---|---|
| `color/brand/800` | Công tắc bật, ô chọn, radio và viền chỗ đang chọn, gạch tab đang chọn, thanh tiến độ, chữ và icon avatar |
| `color/brand/900` | Rê chuột trên phần mang màu khách |
| `color/brand/950` | Đang bấm phần mang màu khách |
| `color/brand/700` | Chữ liên kết, mã chứng từ |
| `color/brand/100` | Nền mục menu đang chọn, nền avatar |
| `color/brand/50` | Nền dòng bảng đang chọn |

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
Figma. Chế độ Dark của dải chờ DEC-116.

## 4. Chữ

### 4.1 Font (DEC-121)

Tiêu đề **Cal Sans** (một độ đậm), chữ thường **Inter**, mã **JetBrains Mono**.

### 4.2 Thang 9 vai (DEC-132)

| Vai | Font | Độ đậm | Web cỡ / dòng | App cỡ / dòng | Dùng cho |
|---|---|---|---|---|---|
| `display` | Cal Sans | 400 | 32 / 40 | 34 / 40 | Số lớn, màn giới thiệu |
| `title-1` | Cal Sans | 400 | 24 / 32 | 28 / 34 | Tiêu đề màn |
| `title-2` | Cal Sans | 400 | 20 / 28 | 22 / 28 | Tiêu đề dialog, sheet, khối lớn |
| `title-3` | Cal Sans | 400 | 17 / 24 | 17 / 22 | Tiêu đề khối, thẻ |
| `heading` | Inter | 600 | 14 / 20 | 15 / 20 | Tiêu đề nhóm nhỏ |
| `body` | Inter | 400 | 14 / 20 | 15 / 22 | Chữ đọc, giá trị |
| `label` | Inter | 500 web · 600 app | 14 / 20 | 15 / 20 | Nút, nhãn, tab |
| `caption` | Inter | 400 | 12 / 16 | 13 / 18 | Thông tin phụ, thời gian |
| `code` | JetBrains Mono | 400 | 12 / 16 | 13 / 18 | Mã lệnh, mã chứng từ |

- Text style Figma tên `type/{vai}`, gắn cỡ và dòng vào biến `Platform`, nên một style dùng cho cả web và app.
  Thêm `type/caption-caps` cho ngoại lệ viết hoa (mục 4.3). Thêm `type/caption-strong` (cỡ, dòng như caption; Inter 600)
  cho chữ chip trạng thái Soft (DEC-200).
- Web gần trùng Atlassian (đọc 14, phụ 12, tiêu đề trang 24). App đọc 15, nằm giữa Material (14) và HIG (17).
- `title-2` 22 trên app là tiêu đề sheet (Material Title Large và HIG Title 2 cùng là 22). `display` cho số lớn.

### 4.3 Độ đậm theo cỡ (DEC-133)

| Chữ | Luật |
|---|---|
| Tiêu đề từ 17px (title-3 trở lên, gồm tiêu đề khối, thẻ) | Cal Sans, một độ đậm |
| Tiêu đề nhóm nhỏ (`heading` 14 web / 15 app) | Inter 600 |
| Chữ đọc | Inter 400 |
| Nhãn, nút, tab (`label`) | Inter 500 trên web, 600 trên app |
| Tránh | Inter 700 cho chữ đọc · Cal Sans dưới 17px · Ultralight, Thin, Light |
| Viết hoa | Chỉ tên cột bảng và nhãn nhóm menu (DEC-027): `type/caption-caps` = caption, Inter 500, viết hoa, giãn chữ 4% (như bản xem trước A; bộ cũ để 0; DEC-140) |

## 5. Bo góc (DEC-122, DEC-134, DEC-165)

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `radius/control` | 8 | tròn hẳn | Nút, tab chip, ô tìm |
| `radius/field` | 8 | 14 | Ô nhập, ô chọn |
| `radius/card` | 12 | 16 | Thẻ, nhóm có viền, khối trong trang, bảng (app 20 → 16, DEC-165) |
| `radius/inner` | 8 | 14 | Khối phụ trong thẻ, ảnh nhỏ |
| `radius/overlay` | 12 | 28 | Dialog, popover; đầu sheet trên app |
| `radius/chip` | tròn hẳn | tròn hẳn | Chip trạng thái, avatar |

Bảng gốc: `radius/0 · 4 · 6 · 8 · 12 · 14 · 16 · 20 · 28 · full`. iOS dùng góc liền mạch; có bật "Corner smoothing"
trên Figma hay không thì chưa chốt (mục 13).

**Luật lồng góc và lề đều (DEC-165).** R là bo khung ngoài, r là bo khối bên trong, lề là khoảng từ mép khung tới mép khối.

1. Khung có khối hình ở góc (ô icon, avatar, nút, ô nhập, khối phụ, công tắc) thì lề 4 phía bằng nhau, đo tới khối cao
   nhất trong dòng. Chữ không có góc để khớp, chỉ cần lề đều.
2. Khung lớn (thẻ, nhóm có viền) **tách xa**: bo không quá lề (app 16 = lề 16; web 12 dưới lề 16). Khối bên trong khi đó
   chỉ đối diện cạnh thẳng nên giữ hình gì cũng được: ô icon tròn, avatar tròn, nút viên thuốc, ô nhập bo 14.
3. Khung ôm sát một khối (dòng đang chọn, chip, ô tìm) **đồng tâm**: R = r + lề. Hình tròn, viên thuốc có r = cao ÷ 2 nên
   R = cao ÷ 2 + lề, ôm sát thì khung cũng thành viên thuốc. Ví dụ: dòng đang chọn có ô vuông bo 8, lề 8 thì bo 16.
4. Lồng nhiều lớp thì áp từng lớp.
5. Máy đo: mỗi khối có hình nằm gần góc khung đạt khi lề ≥ R, hoặc hai lề của góc chênh ≤ 1 và R = r + lề ± 1.
   Mẫu và ma trận 15 trường hợp: Figma section Câu 12b (6246:14279).

## 6. Khoảng cách (DEC-135, DEC-164, DEC-166, DEC-173, DEC-192, DEC-194, DEC-196)

- Bảng gốc thang 4, 13 bậc, tên theo px: `space/0 · 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64`.
- Lề trong component: `space/inset-xs · sm · md · lg · xl` = 4 · 8 · 12 · 16 · 24.
- Khoảng giữa phần tử: `space/gap-xs · sm · md · lg · xl · 2xl` = 4 · 8 · 12 · 16 · 24 · 32.

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `layout/screen-inset` | 24 | 16 | Lề màn |
| `layout/card-padding` | 16 | 16 | Lề chứa: lề trong thẻ, nhóm có viền, dòng trong nhóm (app 14 → 16, DEC-164) |
| `layout/list-gap` | 8 | 12 | Giữa các thẻ, dòng trong danh sách |
| `layout/section-gap` | 32 | 24 | Giữa các khối lớn |
| `layout/title-gap` | 16 | 16 | Tiêu đề màn → nội dung |
| `form/field-gap` | 16 | 12 | Giữa 2 ô nhập trong một nhóm |
| `touch/min` | 24 | 44 | Vùng chạm tối thiểu (web: WCAG 2.2 AA 24; app: DEC-138) |
| `focus/width` | 2 | 2 | Độ dày vòng focus |
| `focus/offset` | 2 | 2 | Khoảng cách vòng focus tới mép control |
| `control/height/sm · md · lg` | 28 · 32 · 40 | 36 · 42 · 52 | Cao nút, ô nhập, ô chọn; cùng cỡ thì cùng cao (DEC-173) |
| `control/padding-x/sm · md · lg` | 8 · 12 · 16 | 12 · 16 · 24 | Lề trái phải trong nút theo cỡ (nút app 52 lề 24, DEC-163) |
| `control/padding-x-icon/sm · md · lg` | 6 · 8 · 12 | 8 · 12 · 20 | Lề phía có icon trong nút: lùi một bậc thang |
| `control/icon-gap` | 6 | 8 | Icon → chữ trong nút, tab chip (DEC-161) |
| `tab/padding-x` | 8 | 16 | Lề trái phải trong tab: web tab gạch, app tab chip |
| `tab/padding-x-icon` | 6 | 12 | Lề phía có icon trong tab: lùi một bậc thang |
| `tab/gap` | 8 | 8 | Giữa 2 tab |
| `nav/height` | — (chỉ app) | 64 | Cao thanh điều hướng nổi (DEC-160) |
| `nav/offset-bottom` | — (chỉ app) | 8 | Thanh điều hướng → vùng an toàn đáy màn |
| `nav/padding-x` | — (chỉ app) | 4 | Lề trong thanh điều hướng |
| `nav/item-padding-y` | — (chỉ app) | 4 | Lề trên dưới mục, nên nền mục đang chọn cao 56 |
| `nav/scan-size` | — (chỉ app) | 56 | Nút Quét mã giữa thanh |
| `chip/height` | 24 | 26 | Cao chip trạng thái (DEC-200) |
| `chip/padding-x` · `chip/padding-x-icon` | 12 · 8 | 12 · 8 | Lề phía chữ · phía icon của chip Soft |
| `chip/icon-gap` | 4 | 4 | Icon → chữ chip Soft |
| `chip/dot-gap` · `chip/dot-size` | 6 · 8 | 6 · 8 | Chấm → chữ, cỡ chấm của chip Dot |
| `avatar/size/sm · md · lg · xl · xxl` | 24 · 36 · 48 · 64 · 88 | 24 · 36 · 48 · 64 · 88 | Cỡ avatar (DEC-201, DEC-203); MD 36 khớp ô đầu dòng 36 (DEC-164); XL, XXL cho ảnh đại diện đổi được |
| `avatar/status-size/sm · md · lg · xl · xxl` | 6 · 10 · 12 · 14 · 16 | 6 · 10 · 12 · 14 · 16 | Chấm trạng thái avatar, thêm viền trắng 2 (DEC-204) |
| `avatar/edit-size/md · lg · xl · xxl` | 20 · 24 · 28 · 32 | 20 · 24 · 28 · 32 | Nút đổi ảnh trên avatar (SM không có; DEC-203) |
| `avatar/group-overlap/sm · md · lg` · `avatar/ring` | 6 · 8 · 12 · 2 | 6 · 8 · 12 · 2 | Avatar Group: lùi đè ¼ đường kính, viền trắng 2; bước giữa hai tâm = cỡ + 4 − lùi = 22 · 32 · 40 (DEC-205) |
| `tooltip/padding-x · padding-y` · `tooltip/offset` · `tooltip/max-width` | 8 · 4 · 4 · 240 | 8 · 4 · 4 · 240 | Tooltip: lề, cách đối tượng, rộng tối đa; bo `tooltip/radius` 8, mũi tên 8 × 4 (DEC-206) |

- Mọi số trên thang 4; DEC-164 bỏ ngoại lệ lề thẻ app 14. Không thêm số lẻ ngoài thang.
- **Ô đầu dòng (DEC-164, app):** ô 24 cho icon 16 và 20, radio, ô chọn, cách chữ 8; ô 36 cho vòng icon, avatar, cách chữ 12.
  Icon đầu dòng luôn đặt giữa ô, không đặt trần. Trừ khung có nền: icon đầu khối phụ, khối tóm tắt (DEC-194), icon đầu
  ô tìm, ô nhập và radio thẻ chọn (DEC-196) chạm mép nội dung; và icon cuối dòng (mục 7, DEC-193). Token `layout/lead-slot` thêm vào `tokens.json` khi dựng Base / List Row.
- **Form (DEC-166):** đặt trên nền trang (nhóm bằng tiêu đề nhóm, web cách nhau 32) hoặc mỗi nhóm một thẻ (web lề 24
  = `space/inset-xl`, app theo `layout/card-padding`); người vẽ chọn theo màn.
- **Tiêu đề (DEC-192):** tiêu đề màn → nội dung `layout/title-gap`; tiêu đề khối → nội dung khối 12 (`space/gap-md`).
  Tiêu đề khối đặt trong thẻ, nhóm, không đặt ngoài.
- **Form (DEC-184, DEC-192):** giữa 2 ô `form/field-gap`; ô → dòng gợi ý 4 (`space/gap-xs`); tiêu đề nhóm → ô 12; giữa 2
  nhóm ô `layout/section-gap`; form web 2 cột cách 24 (`space/gap-xl`). Chữ gợi ý, chữ lỗi dưới ô: app lùi 16 thẳng chữ
  trong ô (K2 32), web canh mép ô.
- **Nút (DEC-162, DEC-163, DEC-192):** lề `control/padding-x/*` theo cỡ, phía có icon `control/padding-x-icon/*`, icon →
  chữ `control/icon-gap`. Hai nút cạnh nhau trên app cách 12 (`space/gap-md`).
- **Tab (DEC-161, DEC-164, DEC-192):** tab chip app cao 36 (`control/height/sm`): lề `tab/padding-x`, phía icon
  `tab/padding-x-icon`, icon → nhãn `control/icon-gap`, nhãn → số đếm 6 (`space/6`), các tab cách `tab/gap`. Tab gạch web
  cao 40 (`control/height/lg`), chữ canh giữa, gạch 2 phủ hết bề ngang tab.
- **Ô có icon (DEC-192, DEC-193, DEC-196):** web phía icon 12 → 8 (icon đầu, icon cuối), icon 14 cách chữ 8. App icon đầu:
  khung icon 16 chạm mép nội dung (cách mép ô 16), chữ cách icon 16 → K3 64 (ô ở K1) hoặc K4 80 (ô đặt trong thẻ). Icon cuối
  ô theo đường K bên phải (mục 7). Nút lọc trong ô tìm giữ ôm sát (DEC-165 luật 3: lề 4, bo đồng tâm).
- **Thẻ chọn app (DEC-184, DEC-196):** lề 16; radio 20 chạm mép nội dung (cách mép thẻ 16), chữ cách radio 12 → K3 64.
- **Khối phụ trong thẻ, khối tóm tắt trong sheet (DEC-194):** nền `color/bg/muted`, bo `radius/inner`, lề
  `layout/card-padding` 16 đều 4 phía. Khối phụ trong thẻ (đặt ở K2 32) có mép nội dung trái **K2b 48**, phải 345; khối tóm
  tắt trong sheet (đặt ở K1 16) có mép nội dung K2 32. Không icon: chữ ở mép nội dung. Có icon: khung icon 16 chạm mép nội
  dung, không đặt trong ô 24; chữ cách icon 16 (khối phụ: chữ K4 80; khối tóm tắt: chữ K3 64). Lề nhìn thấy từ mép nền tới
  icon bằng lề 16.
- **Thanh điều hướng app (DEC-160):** thanh nổi rộng 361 (393 − 2 × 16), cao `nav/height`, bo 28, cách vùng an toàn
  `nav/offset-bottom`, lề trong `nav/padding-x`; mục lề trên dưới `nav/item-padding-y` nên nền mục đang chọn cao 56, bo
  24 = 28 − 4 (đồng tâm, DEC-165); icon 24; nút Quét mã `nav/scan-size`.

## 7. Lưới, đường canh, breakpoint (DEC-136, DEC-164, DEC-193, DEC-194, DEC-038, DEC-039)

- **App 393 (DEC-164):** lề màn 16; năm đường canh: **K1 16** mép nội dung màn · **K2 32** mép chữ trong thẻ, nhóm, ô nhập,
  tab đầu (16 + lề chứa 16) · **K2b 48** mép nội dung khối phụ trong thẻ và ô nhập đặt trong thẻ (32 + lề 16, DEC-194) ·
  **K3 64** mép chữ sau ô đầu dòng 24 (icon, radio) · **K4 80** mép chữ sau ô 36 (vòng icon, avatar) và chữ khối phụ có icon. Mọi chữ dòng thẻ và dòng danh sách có icon đứng ở K3; icon 20 luôn nằm trong ô 24 nên không còn chữ ở 58.
  Mọi khối canh theo một trong bốn đường. Đường K đo từ mép ngoài khung; viền 1px của thẻ nằm trong khung, không cộng
  vào lề (Figma stroke Inside; CSS `box-shadow: inset 0 0 0 1px` hoặc trừ 1px khỏi lề).
- **Đường K bên phải (DEC-193):** soi gương bên trái: **K1 phải 377** (393 − 16) mép thẻ, nhóm · **K2 phải 361**
  (377 − lề chứa 16) mép nội dung. Phần cuối dòng (giá trị, chip, công tắc, nút) chạm K2 phải. Icon cuối dòng và icon
  cuối ô nhập (mũi tên, lịch, mũi tên xuống): khung icon 16 chạm K2 phải, không đặt trong ô 24 như đầu dòng; giá trị,
  chip → khung icon 8. Mẫu: Figma Câu 8d (6288:14692).
- **Web:** 12 cột, rãnh 24, lề màn 24. Màn chi tiết chia **8 cột nội dung + 4 cột thông tin** như Jira (DEC-127).
- **Breakpoint:** 640 · 768 · 1024 · 1280 · 1536 (trùng Tailwind). Từ 768 tới 1279 menu trái thu còn 64 (cột icon),
  bấm thì bung 240 đè lên nội dung.

## 8. Lớp nổi (DEC-125, DEC-137)

| Bậc | Viền | Bóng | Dùng cho |
|---|---|---|---|
| `elev/0` | — | không | Ô nhập, khối phụ trong thẻ (phẳng) |
| `elev/1` | `color/border/default` | 0 1 2 · 6% | Thẻ (DEC-125) |
| `elev/2` | `color/border/default` | 0 4 12 · 10% + 0 1 3 · 6% | Menu thả, popover, gợi ý ô tìm |
| `elev/3` | — | 0 16 40 · 16% + 0 4 12 · 8% | Dialog, sheet, toast |

- Thẻ luôn có viền mảnh và bóng rất nhẹ (`elev/1`). Bóng đậm chỉ cho lớp nổi tạm (`elev/2`, `elev/3`).
- Effect style Figma tên `elev/1 · 2 · 3`; viền gắn riêng bằng `color/border/default`.

## 9. Vùng chạm và focus (DEC-097, DEC-138, DEC-139)

- **App:** vùng chạm tối thiểu 44×44 cho mọi app (ưu tiên iOS). Nút nhìn: 52 ở chân màn, 42 cho nút nhỏ và nút icon;
  phần thiếu là vùng bấm vô hình quanh nút. Hai nút icon cạnh nhau cách nhau đủ để vùng bấm không chồng
  (ghi chú câu 10, trang phỏng vấn).
  Lưu ý: dưới mức 48dp Android khuyên.
- **Web:** đích bấm tối thiểu 24×24 (WCAG 2.2 AA, mục 2.5.8).
- **Focus:** vòng 2px, cách mép 2px, màu `color/border/focus` (than chì) cho mọi khách, không theo dải màu khách
  (DEC-170). Nút Danger: vòng focus màu danger (`button/focus/danger` → `color/action/danger`, DEC-198). Ô nhập
  đang gõ: viền 2px cùng màu than chì.

## 10. Chuyển động (DEC-139)

Giữ như bộ cũ (`design/design.md` › Motion).

| Token | Giá trị | Dùng cho |
|---|---|---|
| `duration/fast` | 125ms | Vi tương tác: hover, pressed, đổi màu, bật/tắt Switch |
| `duration/medium` | 300ms | Vào/ra: Dialog, Popover, Toast, BottomSheet |
| `duration/slow` | 700ms | Chuyển động liên tục: skeleton pulse, chấm trạng thái nhấp nháy |
| `easing/standard` | cubic-bezier(0.24, 1, 0.4, 1) | Một đường cong cho mọi chuyển động; không bounce, không spring |

Transition theo từng thuộc tính (background, color, opacity, transform, box-shadow), không dùng `all`. Người dùng bật giảm chuyển động thì mọi thời gian về 0 (`tokens.css` đã có).

## 11. Icon (DEC-141…156)

Luật icon ở `design/v2/icons.md`: Lucide 1.58.0 cho web và app; nét 1.8 trên khung 24 đổi theo cỡ, icon trong chip nét 2;
cỡ theo Platform `icon/size/sm · md · lg · chip` (web 14 · 16 · 20 · 14, app 16 · 20 · 24 · 14) — trên Figma chọn biến thể
Size theo bảng, đổi chế độ Platform không tự đổi cỡ icon; bản tô cho cảnh báo, lỗi và trạng thái bật; tab đang chọn (app)
và mục menu đang chọn (web) giữ icon viền; 7 icon nghiệp vụ tự vẽ; bảng icon theo nghĩa.

**Cấu trúc lớp trên Figma (DEC-202):** mỗi icon mỗi cỡ là **một lớp nét tên `Vector`** (bản tô thêm một lớp `Hình tô`).
Component tô màu icon bằng cách đè màu lớp `Vector`; nhờ cùng một lớp cùng tên nên đổi icon qua thuộc tính vẫn giữ màu. Icon mới
phải gộp nét thành một lớp trước khi đưa vào thư viện. Lớp `Hình tô` không theo màu khi đổi icon: trong component dùng bản viền,
cần bản tô thì gán màu lớp tô trên instance.

## 12. Luật gắn token khi vẽ và code

1. Fill, viền, chữ gắn biến `Semantic`; bo góc, khoảng cách, lề gắn biến `Platform`. Không mã màu, không số trần.
2. Chữ dùng text style `type/*`; không chỉnh cỡ tay. Cần cỡ không có trong thang thì hỏi, không tự thêm.
3. Khung màn đặt chế độ `Platform` (Web hoặc Mobile) một lần.
4. Thẻ dùng `elev/1` + viền `color/border/default`; menu nổi `elev/2`; dialog, sheet, toast `elev/3`.
5. Sửa token: sửa `tokens.json` → chạy script sinh `tokens.css` → cập nhật biến Figma cùng lượt.
6. Khối có hình đặt gần góc khung: chạy máy đo lồng góc (mục 5, DEC-165) trước khi trình màn.

## 13. Còn mở

- Giá trị chế độ Dark (DEC-116).
- Có bật Corner smoothing (góc liền mạch kiểu iOS) cho thẻ, sheet trên app không.
- Quyền publish thư viện của gói Figma (DEC-110).
- Việc còn mở của icon: `design/v2/icons.md` mục 10.
