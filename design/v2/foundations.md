---
type: design-foundations
status: draft
updated: 2026-10-17
links:
  - design/v2/architecture.md
  - design/v2/tokens.json
  - design/v2/tokens.css
  - _workspace/decisions.md
---

# Design System v2 — nền tảng (Foundations)

> Kết quả vòng 2/6, chốt 16–17/10/2026 trên trang phỏng vấn https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU
> (DEC-119…139). File này là **luật dùng**. Giá trị máy đọc nằm ở `design/v2/tokens.json`; `tokens.css` sinh ra từ
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
| Component | `Component` (vòng 4) | 1 | `button/bg/primary` | Component nhiều trạng thái |

- Component và màn **không gắn Primitives, không ghi mã màu trần**. Cần màu mới thì thêm token nghĩa.
- Màn đặt chế độ `Platform` một lần ở khung màn (Web hoặc Mobile); chữ, bo góc, khoảng cách bên trong tự đổi.
  Trong code: `data-platform="mobile"` trên khung trang (mặc định là web), `data-theme="dark"` cho chế độ tối.
- Dark đang là bản sao của Light; giá trị tối điền và kiểm ở vòng sau (DEC-116).
- Tên CSS = `--` + tên token thay `/` bằng `-`: `color/bg/canvas` → `var(--color-bg-canvas)`. Biến Figma có code syntax WEB đúng tên này.

## 3. Màu

### 3.1 Bảng gốc (DEC-130)

11 bậc tên 50–950, tính bằng OKLCH để sáng đều theo mắt. Các mốc giữ đúng giá trị đã duyệt: neutral/100 nền,
300 viền ô nhập, 400 chữ gợi ý, 500 chữ phụ, 900 chữ; mỗi sắc chip nền bậc 50, chữ bậc 700.
Màu nhấn là than chì #262626 (DEC-119), không có bảng 11 bậc.

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
- Màu khách chỉ tô ô logo, không vào token (DEC-041, DEC-119).

### 3.3 Token nghĩa (DEC-131)

Tên dạng `color/{nhóm}/{vai}`. Cột HIG, Material 3, Atlassian để dev iOS, Android, web map sang hệ họ quen.
Material 3 không có vai thành công, cảnh báo, thông tin: mình tự thêm (`color/status/*`).

| Token | Trỏ tới | Dùng cho | Apple HIG | Material 3 | Atlassian |
|---|---|---|---|---|---|
| `color/bg/canvas` | `neutral/100` | Nền trang chủ mobile, vùng ngoài thẻ | systemGroupedBackground | surface-container-low | `elevation.surface.sunken` |
| `color/bg/surface` | `white` | Thẻ, bảng, màn danh sách | secondarySystemGroupedBackground | surface-container-lowest | `elevation.surface` |
| `color/bg/muted` | `neutral/100` | Ô nhập mobile, khối phụ trong thẻ | tertiarySystemFill | surface-container-highest | `color.background.input` |
| `color/bg/hover` | `neutral/50` | Rê chuột dòng bảng, mục menu | — (iOS không có hover) | lớp trạng thái on-surface 8% | `color.background.neutral.subtle.hovered` |
| `color/bg/selected` | `neutral/100` | Dòng, mục đang chọn (kèm vạch than chì) | systemFill | secondary-container | `color.background.selected` |
| `color/bg/inverse` | `neutral/900` | Toast, tooltip | — | inverse-surface | `color.background.inverse.subtle` |
| `color/text/primary` | `neutral/900` | Chữ chính | label | on-surface | `color.text` |
| `color/text/secondary` | `neutral/500` | Chữ phụ, nhãn trường | secondaryLabel | on-surface-variant | `color.text.subtle` |
| `color/text/tertiary` | `neutral/400` | Gợi ý trong ô, chữ tắt; không dùng cho nội dung | tertiaryLabel · placeholderText | on-surface 38% (tắt) | `color.text.subtlest` |
| `color/text/inverse` | `white` | Chữ trên nền đậm, chữ nút chính | — | inverse-on-surface · on-primary | `color.text.inverse` |
| `color/icon/primary` | `neutral/700` | Icon đi cùng chữ chính | label | on-surface | `color.icon` |
| `color/icon/secondary` | `neutral/500` | Chevron, icon trong ô tìm | secondaryLabel | on-surface-variant | `color.icon.subtle` |
| `color/border/default` | `neutral/200` | Viền thẻ, kẻ bảng | separator | outline-variant | `color.border` |
| `color/border/strong` | `neutral/300` | Viền ô nhập web | opaqueSeparator | outline | `color.border.input` |
| `color/border/focus` | `charcoal/900` | Vòng focus 2px | tint (vòng focus bàn phím) | secondary (vòng focus) | `color.border.focused` |
| `color/action/primary` | `charcoal/900` | Nút chính, tab chip đang chọn | tintColor · accentColor | primary | `color.background.brand.bold` |
| `color/action/primary-hover` | `charcoal/800` | Rê chuột nút chính | — | primary + lớp on-primary 8% | `color.background.brand.bold.hovered` |
| `color/action/primary-pressed` | `charcoal/950` | Đang bấm nút chính | — (hệ thống tự làm tối) | primary + lớp on-primary 10% | `color.background.brand.bold.pressed` |
| `color/action/secondary` | `neutral/100` | Nút phụ | secondarySystemFill | secondary-container | `color.background.neutral` |
| `color/action/secondary-hover` | `neutral/200` | Rê chuột nút phụ | — | secondary-container + lớp 8% | `color.background.neutral.hovered` |
| `color/action/danger` | `red/700` | Nút xoá, huỷ lệnh | systemRed | error | `color.background.danger.bold` |
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
  Thêm `type/caption-caps` cho ngoại lệ viết hoa (mục 4.3).
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

## 5. Bo góc (DEC-122, DEC-134)

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `radius/control` | 8 | tròn hẳn | Nút, tab chip, ô tìm |
| `radius/field` | 8 | 14 | Ô nhập, ô chọn |
| `radius/card` | 12 | 20 | Thẻ, khối trong trang, bảng |
| `radius/inner` | 8 | 14 | Khối phụ trong thẻ, ảnh nhỏ |
| `radius/overlay` | 12 | 28 | Dialog, popover; đầu sheet trên app |
| `radius/chip` | tròn hẳn | tròn hẳn | Chip trạng thái, avatar |

Bảng gốc: `radius/0 · 4 · 6 · 8 · 12 · 14 · 16 · 20 · 28 · full`. iOS dùng góc liền mạch; có bật "Corner smoothing"
trên Figma hay không thì chưa chốt (mục 13).

## 6. Khoảng cách (DEC-135)

- Bảng gốc thang 4, 13 bậc, tên theo px: `space/0 · 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64`.
- Lề trong component: `space/inset-xs · sm · md · lg · xl` = 4 · 8 · 12 · 16 · 24.
- Khoảng giữa phần tử: `space/gap-xs · sm · md · lg · xl · 2xl` = 4 · 8 · 12 · 16 · 24 · 32.

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `layout/screen-inset` | 24 | 16 | Lề màn |
| `layout/card-padding` | 16 | 14 | Lề trong thẻ (app 14 nằm ngoài thang, giữ theo DEC-135) |
| `layout/list-gap` | 8 | 12 | Giữa các thẻ, dòng trong danh sách |
| `layout/section-gap` | 32 | 24 | Giữa các khối lớn |
| `touch/min` | 24 | 44 | Vùng chạm tối thiểu (web: WCAG 2.2 AA 24; app: DEC-138) |
| `focus/width` | 2 | 2 | Độ dày vòng focus |
| `focus/offset` | 2 | 2 | Khoảng cách vòng focus tới mép control |

Lề thẻ app 14 nằm ngoài thang; giữ vì thẻ app đã duyệt dùng 14 (DEC-135). Không thêm số lẻ khác ngoài thang.

## 7. Lưới, đường canh, breakpoint (DEC-136, DEC-038, DEC-039)

- **App 393:** lề màn 16; ba đường canh cố định: **K1 16** mép nội dung màn · **K2 30** mép chữ trong thẻ (16 + lề thẻ 14) ·
  **K3 76** mép chữ sau icon trong thẻ. Mọi khối canh theo một trong ba đường này.
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
- **Focus:** vòng 2px, cách mép 2px, màu `color/border/focus` (than chì).

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

## 12. Luật gắn token khi vẽ và code

1. Fill, viền, chữ gắn biến `Semantic`; bo góc, khoảng cách, lề gắn biến `Platform`. Không mã màu, không số trần.
2. Chữ dùng text style `type/*`; không chỉnh cỡ tay. Cần cỡ không có trong thang thì hỏi, không tự thêm.
3. Khung màn đặt chế độ `Platform` (Web hoặc Mobile) một lần.
4. Thẻ dùng `elev/1` + viền `color/border/default`; menu nổi `elev/2`; dialog, sheet, toast `elev/3`.
5. Sửa token: sửa `tokens.json` → chạy script sinh `tokens.css` → cập nhật biến Figma cùng lượt.

## 13. Còn mở

- Giá trị chế độ Dark (DEC-116).
- Có bật Corner smoothing (góc liền mạch kiểu iOS) cho thẻ, sheet trên app không.
- Cao control theo cỡ (nút, ô nhập web 32, app 52 / 42) chuyển thành token Component ở vòng 4.
- Quyền publish thư viện của gói Figma (DEC-110).
- Việc còn mở của icon: `design/v2/icons.md` mục 10.
