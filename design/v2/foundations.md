---
type: design-foundations
status: draft
updated: 2026-10-26
links:
  - design/v2/architecture.md
  - design/v2/tokens.json
  - design/v2/tokens.css
  - _workspace/decisions.md
---

# Design System v2 — nền tảng (Foundations)

> Kết quả vòng 2/6, chốt 16–17/10/2026 trên trang phỏng vấn https://claude.ai/artifact/D5KS1PPdUih9dsajBo48vU
> (DEC-119…139); bổ sung 19/10 từ phần khoảng cách, màu theo khách và vòng 4 (DEC-164…170, DEC-173, DEC-176,
> DEC-179, DEC-192…194, DEC-196); 20/10 nền đặt, thẻ, chip, avatar, dòng danh sách, thanh tiến độ, ô mã (DEC-231…246). File này là **luật dùng**. Giá trị máy đọc nằm ở `design/v2/tokens.json`; `tokens.css` sinh ra từ
> json bằng `python3 _scripts/ds-v2-tokens.py`. Bảng trong file này lệch json thì **json thắng**.
> Trên Figma: trang `🎨 DS · Foundations` (collection 0–8 theo mục 2; text style `type/*`; effect style `elev/*`).

## 0. Trạng thái từng mục

Component chỉ coi một mục là chuẩn khi mục đó `approved`; mục chưa duyệt vẫn dùng được nhưng trang review ghi "chưa duyệt".
Đổi bằng `python3 _scripts/ds-foundation-status.py set <mã> <trạng thái>` (dashboard và trang duyệt foundations gọi lệnh này).

<!-- foundation-status -->
| Mã | Mục | Ở đâu | Trạng thái | Ngày | Ghi chú |
|---|---|---|---|---|---|
| color | Màu | mục 3 | draft | 2026-10-28 |  |
| type | Chữ | mục 4 | draft | 2026-10-28 |  |
| radius | Bo góc | mục 5 | draft | 2026-10-28 |  |
| space | Khoảng cách | mục 6 | draft | 2026-10-28 |  |
| grid | Lưới, độ rộng, breakpoint | mục 7 | draft | 2026-10-28 |  |
| elevation | Lớp nổi, làm mờ nền | mục 8 | draft | 2026-10-28 |  |
| touch-focus | Vùng chạm và focus | mục 9 | draft | 2026-10-28 |  |
| motion | Chuyển động | mục 10 | draft | 2026-10-28 |  |
| icon | Icon | mục 11 · `design/v2/icons.md` | draft | 2026-10-28 |  |
<!-- /foundation-status -->

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
| Gốc | `0. Primitives` | Value | `neutral/900`, `space/16`, `radius/12` | Chỉ token tầng trên trỏ tới; ẩn khỏi bảng chọn |
| Nghĩa | `1. Semantic` | Light, Dark | `color/text/secondary` | Component, màn |
| Nền tảng | `2. Platform · Radius` · `3. Platform · Spacing & Layout` · `4. Platform · Typography` · `5. Platform · Sizes` · `6. Platform · Component sizes` | Web, Mobile | `radius/card`, `layout/screen-inset`, `type/body/size`, `control/height/md`, `chip/height` | Component, màn |
| Theo khách | `7. Brand` | 8 dải | `color/brand/800` | Component, màn, theo vai mục 3.5 |
| Component | `8. Component` | Value | `button/bg/primary`, `button/fg/danger` (DEC-174, DEC-197), `avatar/bg` (DEC-201), `tooltip/bg` (DEC-206) | Component nhiều trạng thái |

- Platform tách 5 collection theo loại số đo, cùng mode Web/Mobile (DEC-257). Figma không lồng collection trong
  collection nên "Platform" chỉ là tiền tố tên; khung màn đặt mode Web hoặc Mobile cho **cả 5** collection. Trong
  `tokens.json` Platform vẫn là một nhóm, bảng chia sang 5 collection ở khoá `figma.collections`.

- Component và màn **không gắn Primitives, không ghi mã màu trần**. Cần màu mới thì thêm token nghĩa.
- Màn đặt chế độ `Platform` một lần ở khung màn (Web hoặc Mobile); chữ, bo góc, khoảng cách bên trong tự đổi.
  Trong code: `data-platform="mobile"` trên khung trang (mặc định là web), `data-theme="dark"` cho chế độ tối.
- **Không dùng nền trang xám nữa (DEC-258)**, cả web và app: nền trang trắng, thẻ trắng có viền `color/border/default`.
  Collection Context (DEC-241) đã bỏ; khe focus là token Semantic `color/focus/gap`. `color/bg/muted` giữ cho khối phụ trong
  thẻ và ô nhập app. `color/bg/canvas` trỏ về trắng, chỉ giữ để không gãy tham chiếu cũ.
- Dark: bản nháp theo quy tắc đảo bậc, đã đo và chỉnh, xem mục 3.6 (DEC-257). Brand chưa có giá trị Dark.
- Tên CSS = `--` + tên token thay `/` bằng `-`: `color/bg/surface` → `var(--color-bg-surface)`. Biến Figma có code syntax WEB đúng tên này.

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

Thêm: `white` #FFFFFF, `alpha/neutral-950-50` (#0A0A0A độ mờ 50%, cho nền mờ sau dialog, sheet).

### 3.2 Luật dùng bậc

- Chữ theo sắc (blue, teal, purple, yellow, green, red, orange) trên nền trắng, và nền đặc có chữ trắng, dùng bậc 700 trở lên.
  Xám dùng qua token nghĩa (chữ phụ neutral/500, chip xám neutral/600).
- Bậc 400 chỉ cho chữ gợi ý trong ô và icon tắt (2,52:1), không dùng cho nội dung.
- Chip: nền bậc 50, chữ và icon bậc 700; riêng chip xám nền neutral/100, chữ neutral/600 (DEC-130). Kiểu chip
  (nền nhạt + icon, hay chấm + chữ) chốt luật ở vòng 4 (DEC-126).
- Màu khách đi qua dải riêng của khách và chỉ vào các vai ở mục 3.5 (DEC-167…169); chip trạng thái không đổi
  theo khách; ô logo luôn đúng màu logo khách.

### 3.3 Token nghĩa (DEC-131, DEC-258)

Tên dạng `color/{nhóm}/{vai}`. Cột **Dùng cho** viết theo cách Untitled UI: vai của token + component đang dùng.
Ánh xạ sang Apple HIG, Material 3, Atlassian chỉ để review, nằm ở `design/v2/_review/token-mapping.md` (DEC-258).
Giá trị Dark: mục 3.6. Trạng thái (`color/status/*`) có 8 vai × 4 nhóm (DEC-258): `-text 700 · -icon 600 · -bg 50 ·
-bg-strong 100 · -solid 700 · -solid-hover 800 · -border 700 · -border-subtle 300`.

| Token | Trỏ tới (Light) | Dùng cho |
|---|---|---|
| `color/bg/canvas` | `white` | Không dùng nữa (DEC-258): nền trang trắng như bg/surface; giữ token để không gãy tham chiếu cũ. |
| `color/bg/surface` | `white` | Nền trang và nền mọi thẻ, bảng, sheet. Dùng ở: Card, Record Card, Summary Card, List Item. |
| `color/bg/muted` | `neutral/50` | Nền khối phụ trong thẻ, ô nhập app. Dùng ở: khối tóm tắt trong Card, Text Field (app), OTP Field. |
| `color/bg/hover` | `neutral/50` | Nền khi rê chuột lên thứ nền trắng. Dùng ở: dòng bảng, mục menu, List Item (web). |
| `color/bg/selected` | `neutral/100` | Nền mục đang chọn khi khách không có màu riêng. Dùng ở: List Item đang chọn, mục menu đang chọn. |
| `color/bg/inverse` | `neutral/900` | Nền tối tương phản cao. Dùng ở: Tooltip, toast trung tính. |
| `color/text/primary` | `neutral/900` | Tiêu đề, giá trị chính. Dùng ở: tiêu đề Card, giá trị trong Record Card, chữ Text Field đã nhập. |
| `color/text/secondary` | `neutral/500` | Chữ phụ: nhãn trường (web = app), mô tả, thời gian. Dùng ở: nhãn Text Field, nhãn dòng Record Card, Status Row. |
| `color/text/secondary-strong` | `neutral/600` | Chữ phụ trên nền nhấn (hover, đang chọn) để giữ ≥ 4,5:1 (DEC-289). Dùng ở: dòng phụ thẻ phạm vi khi Hover/Open, dòng chọn Hover/Selected của Scope dialog. |
| `color/text/tertiary` | `neutral/400` | Chữ tắt; không dùng cho nội dung, không dùng cho chữ gợi ý (2,52:1 — chữ gợi ý dùng `text/secondary`, DEC-207). Dùng ở: nút Disabled. |
| `color/text/inverse` | `white` | Chữ trên nền đậm. Dùng ở: chữ nút Primary, chữ Tooltip. |
| `color/icon/primary` | `neutral/700` | Icon đi cùng chữ chính. Dùng ở: icon dòng Record Card, icon List Item. |
| `color/icon/secondary` | `neutral/500` | Icon phụ: chevron, icon trong ô. Dùng ở: icon Text Field, chevron List Item. |
| `color/border/default` | `neutral/200` | Viền dùng nhiều nhất: viền thẻ, kẻ bảng, vạch chia. Dùng ở: Card, Record Card, List Item (vạch chia). |
| `color/border/strong` | `neutral/300` | Viền tách khối đậm hơn mặc định. Dùng ở: viền nút Secondary, chip viền. |
| `color/border/input` | `neutral/500` | Viền tương phản cao (≥ 3:1) cho thứ người dùng nhập hoặc chọn. Dùng ở: Text Field, OTP Field, radio Selectable Card. |
| `color/border/focus` | `charcoal/900` | Vòng focus 2px và viền ô đang gõ; than chì cho mọi khách (DEC-170). Dùng ở: .focus / Ring, Text Field đang gõ. |
| `color/border/danger` | `red/700` | Viền lỗi. Dùng ở: Text Field lỗi, OTP Field lỗi. |
| `color/action/primary` | `charcoal/900` | Nền hành động chính. Dùng ở: nút Primary, tab chip đang chọn. |
| `color/action/primary-hover` | `charcoal/800` | Nền nút Primary khi rê chuột. |
| `color/action/primary-pressed` | `charcoal/950` | Nền nút Primary khi bấm. |
| `color/action/secondary` | `neutral/100` | Nền hành động phụ và nền xám của trạng thái tắt. Dùng ở: nút Secondary, nút Disabled. |
| `color/action/secondary-hover` | `neutral/200` | Nền nút Secondary khi rê chuột. |
| `color/action/danger` | `red/700` | Chữ, icon hành động phá huỷ. Dùng ở: nút Danger (xoá, huỷ lệnh). |
| `color/action/danger-subtle` | `red/50` | Nền nhạt của nút Danger. |
| `color/status/success-text` | `green/700` | Thành công · Chữ trạng thái: chữ dưới ô, chữ trong banner. |
| `color/status/success-icon` | `green/600` | Thành công · Icon trạng thái. |
| `color/status/success-bg` | `green/50` | Thành công · Nền nhạt: banner, thanh thông báo. |
| `color/status/success-bg-strong` | `green/100` | Thành công · Nền vòng Featured icon. |
| `color/status/success-solid` | `green/700` | Thành công · Nền đặc chữ trắng: toast, huy hiệu đếm. |
| `color/status/success-solid-hover` | `green/800` | Thành công · Nền đặc khi rê chuột. |
| `color/status/success-border` | `green/700` | Thành công · Viền trạng thái. |
| `color/status/success-border-subtle` | `green/300` | Thành công · Viền nhạt quanh banner. |
| `color/status/warning-text` | `yellow/700` | Cảnh báo · Chữ trạng thái: chữ dưới ô, chữ trong banner. |
| `color/status/warning-icon` | `yellow/600` | Cảnh báo · Icon trạng thái. |
| `color/status/warning-bg` | `yellow/50` | Cảnh báo · Nền nhạt: banner, thanh thông báo. |
| `color/status/warning-bg-strong` | `yellow/100` | Cảnh báo · Nền vòng Featured icon. |
| `color/status/warning-solid` | `yellow/700` | Cảnh báo · Nền đặc chữ trắng: toast, huy hiệu đếm. |
| `color/status/warning-solid-hover` | `yellow/800` | Cảnh báo · Nền đặc khi rê chuột. |
| `color/status/warning-border` | `yellow/700` | Cảnh báo · Viền trạng thái. |
| `color/status/warning-border-subtle` | `yellow/300` | Cảnh báo · Viền nhạt quanh banner. |
| `color/status/danger-text` | `red/700` | Lỗi · Chữ trạng thái: chữ dưới ô, chữ trong banner. |
| `color/status/danger-icon` | `red/600` | Lỗi · Icon trạng thái. |
| `color/status/danger-bg` | `red/50` | Lỗi · Nền nhạt: banner, thanh thông báo. |
| `color/status/danger-bg-strong` | `red/100` | Lỗi · Nền vòng Featured icon. |
| `color/status/danger-solid` | `red/700` | Lỗi · Nền đặc chữ trắng: toast, huy hiệu đếm. |
| `color/status/danger-solid-hover` | `red/800` | Lỗi · Nền đặc khi rê chuột. |
| `color/status/danger-border` | `red/700` | Lỗi · Viền trạng thái. |
| `color/status/danger-border-subtle` | `red/300` | Lỗi · Viền nhạt quanh banner. |
| `color/status/info-text` | `blue/700` | Thông tin · Chữ trạng thái: chữ dưới ô, chữ trong banner. |
| `color/status/info-icon` | `blue/600` | Thông tin · Icon trạng thái. |
| `color/status/info-bg` | `blue/50` | Thông tin · Nền nhạt: banner, thanh thông báo. |
| `color/status/info-bg-strong` | `blue/100` | Thông tin · Nền vòng Featured icon. |
| `color/status/info-solid` | `blue/700` | Thông tin · Nền đặc chữ trắng: toast, huy hiệu đếm. |
| `color/status/info-solid-hover` | `blue/800` | Thông tin · Nền đặc khi rê chuột. |
| `color/status/info-border` | `blue/700` | Thông tin · Viền trạng thái. |
| `color/status/info-border-subtle` | `blue/300` | Thông tin · Viền nhạt quanh banner. |
| `color/chip/gray/bg` | `neutral/100` | Chip trạng thái gray: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/gray/fg` | `neutral/600` | Chip trạng thái gray: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/blue/bg` | `blue/50` | Chip trạng thái blue: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/blue/fg` | `blue/700` | Chip trạng thái blue: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/teal/bg` | `teal/50` | Chip trạng thái teal: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/teal/fg` | `teal/700` | Chip trạng thái teal: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/purple/bg` | `purple/50` | Chip trạng thái purple: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/purple/fg` | `purple/700` | Chip trạng thái purple: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/yellow/bg` | `yellow/50` | Chip trạng thái yellow: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/yellow/fg` | `yellow/700` | Chip trạng thái yellow: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/green/bg` | `green/50` | Chip trạng thái green: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/green/fg` | `green/700` | Chip trạng thái green: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/red/bg` | `red/50` | Chip trạng thái red: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/red/fg` | `red/700` | Chip trạng thái red: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/chip/orange/bg` | `orange/100` (DEC-311) | Chip trạng thái orange: nền. Dùng ở: Status Chip, Status Row. |
| `color/chip/orange/fg` | `orange/800` (DEC-311) | Chip trạng thái orange: chữ, icon. Dùng ở: Status Chip, Status Row. |
| `color/overlay/scrim` | `alpha/neutral-950-50` | Lớp phủ sau dialog, sheet. |
| `color/shadow/sm` | `alpha/shadow-6` | Màu bóng, đổi theo sáng/tối. Dùng trong: elev/1. |
| `color/shadow/md` | `alpha/shadow-10` | Màu bóng, đổi theo sáng/tối. Dùng trong: elev/2 lớp 1, elev/3 lớp 2. |
| `color/shadow/md-soft` | `alpha/shadow-6` | Màu bóng, đổi theo sáng/tối. Dùng trong: elev/2 lớp 2. |
| `color/shadow/lg` | `alpha/shadow-16` | Màu bóng, đổi theo sáng/tối. Dùng trong: elev/3 lớp 1. |
| `color/focus/gap` | `white` | Khe 2px giữa control và vòng focus, trùng nền trang (DEC-258, thay collection Context). Dùng ở: .focus / Ring, ruột nút Ghost, Outline. |

### 3.4 Tương phản đo được (Light)

Máy đo mỗi lần chạy `python3 _scripts/ds-v2-tokens.py --check`; dưới 4,5:1 thì script báo lỗi (trừ chữ gợi ý, chỉ báo cáo).

| Tương phản | Cặp chữ trên nền |
|---|---|
| 17.93:1 | `color/text/primary` trên `color/bg/surface` |
| 17.93:1 | `color/text/primary` trên `color/bg/canvas` |
| 4.74:1 | `color/text/secondary` trên `color/bg/surface` |
| 4.74:1 | `color/text/secondary` trên `color/bg/canvas` |
| 4.54:1 | `color/text/secondary` trên `color/bg/muted` |
| 7.17:1 | `color/text/secondary-strong` trên `color/bg/selected` |
| 7.49:1 | `color/text/secondary-strong` trên `color/bg/hover` |
| 15.13:1 | `color/text/inverse` trên `color/action/primary` |
| 6.57:1 | `color/text/inverse` trên `color/action/danger` |
| 5.76:1 | `color/action/danger` trên `color/action/danger-subtle` |
| 16.44:1 | `color/text/primary` trên `color/action/secondary` |
| 2.52:1 | `color/text/tertiary` trên `color/bg/surface` (chỉ báo cáo: chữ gợi ý, chữ tắt) |
| 5.10:1 | `color/status/success-text` trên `color/status/success-bg` |
| 5.76:1 | `color/status/warning-text` trên `color/status/warning-bg` |
| 5.76:1 | `color/status/danger-text` trên `color/status/danger-bg` |
| 6.33:1 | `color/status/info-text` trên `color/status/info-bg` |
| 7.17:1 | `color/chip/gray/fg` trên `color/chip/gray/bg` |
| 6.33:1 | `color/chip/blue/fg` trên `color/chip/blue/bg` |
| 5.63:1 | `color/chip/teal/fg` trên `color/chip/teal/bg` |
| 6.59:1 | `color/chip/purple/fg` trên `color/chip/purple/bg` |
| 5.76:1 | `color/chip/yellow/fg` trên `color/chip/yellow/bg` |
| 5.10:1 | `color/chip/green/fg` trên `color/chip/green/bg` |
| 5.76:1 | `color/chip/red/fg` trên `color/chip/red/bg` |
| 6.05:1 | `color/chip/orange/fg` trên `color/chip/orange/bg` (DEC-311) |

Viền cần 3:1 (WCAG 1.4.11): `color/border/input` 4.74:1 trên `color/bg/surface`, 4.54:1 cạnh `color/bg/muted` (ô nhập app).

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

### 3.6 Chế độ tối (DEC-257)

Bản nháp lấy quy tắc đảo bậc của Untitled UI rồi đo lại bằng script: mỗi token Semantic trỏ sang bậc đối xứng
**50↔950, 100↔900, 200↔800, 300↔700, 400↔600, 500 giữ**; `white` → `neutral/950`. Ba ngoại lệ:

| Ngoại lệ | Dark | Lý do |
|---|---|---|
| `color/text/secondary`, `color/icon/secondary`, `color/border/input` | `neutral/400` | Giữ 500 chỉ đạt 3,61:1 trên nền 950; 400 đạt 7,6:1 |
| `color/action/primary` · `-hover` · `-pressed`, `color/text/inverse`, `color/border/focus` | nút sáng `neutral/50` · 200 · 300, chữ `neutral/950`, vòng focus `neutral/50` | Than chì không có bậc đảo; nút than chì trên nền tối không thấy |
| Nền: `bg/surface` (và `bg/canvas`, `focus/gap`) · `bg/muted` · `bg/hover` · `bg/selected` · `action/secondary` (+hover) | 950 · 900 · 900 · 800 · 800 (700) | Đảo thẳng thì surface (trắng) và hover (50) cùng 950, rê chuột không thấy |

Chip và trạng thái đảo thẳng (nền 950, chữ 300), đạt 6,9–7,9:1. Màu khách (Brand) ở Dark theo quy ước `_alt`:
vai cần chuyển xám thì chuyển xám (chờ điền). Giá trị máy đọc: `tokens.json` › Semantic › Dark.

## 4. Chữ

### 4.1 Font (DEC-121)

Tiêu đề **Cal Sans** (một độ đậm), chữ thường **Inter**, mã **JetBrains Mono**.

### 4.2 Thang 10 vai (DEC-132, DEC-306)

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
| `hint` | Inter | 400 | 12.5 / 18 | 12.5 / 18 | Gợi ý dưới ô, chữ lỗi, dòng phụ file (DEC-306) |
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

## 5. Bo góc (DEC-122, DEC-134, DEC-165, DEC-259)

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `radius/control` | 8 | tròn hẳn | Nút, tab chip, ô tìm |
| `radius/field` | 8 | 12 | Ô nhập, ô chọn (app 14 → 12, DEC-259) |
| `radius/card` | 12 | 16 | Thẻ, nhóm có viền, khối trong trang, bảng (app 20 → 16, DEC-165) |
| `radius/inner` | 8 | 12 | Khối phụ trong thẻ, ảnh nhỏ (app 14 → 12) |
| `radius/overlay` | 16 | 24 | Dialog, popover; đầu sheet trên app (web 12 → 16, app 28 → 24, DEC-259) |
| `radius/menu` · `radius/menu-item` | 8 · 6 | 8 · 6 | Menu thả · mục trong menu (như Untitled) |
| `radius/badge` | 6 | 6 | Badge vuông cho nhãn phân loại (không phải trạng thái) |
| `radius/tab` | 8 | tròn hẳn | Tab kiểu nút; tab gạch không bo |
| `radius/chip` | tròn hẳn | tròn hẳn | Chip trạng thái, avatar |

Bảng gốc đặt tên theo cỡ như Untitled UI (DEC-259): `radius/none 0 · xxs 2 · xs 4 · sm 6 · md 8 · lg 10 · xl 12 · 2xl 16 ·
3xl 20 · 4xl 24 · full`. Bỏ 14 và 28 (app theo thang Untitled). Tên CSS đổi theo: `--radius-8` → `--radius-md`; token theo vai
(`--radius-card`…) giữ tên. iOS dùng góc liền mạch; có bật "Corner smoothing" trên Figma hay không thì chưa chốt (mục 13).

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

## 6. Khoảng cách (DEC-135, DEC-164, DEC-166, DEC-173, DEC-192, DEC-194, DEC-196, DEC-232, DEC-234, DEC-239, DEC-242, DEC-243, DEC-244)

- Bảng gốc thang 4, 13 bậc, tên theo px: `space/0 · 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64`.
- Lề trong component: `space/inset-xs · sm · md · lg · xl` = 4 · 8 · 12 · 16 · 24.
- Khoảng giữa phần tử: `space/gap-xs · sm · md · lg · xl · 2xl` = 4 · 8 · 12 · 16 · 24 · 32.

| Token | Web | App | Dùng cho |
|---|---|---|---|
| `layout/screen-inset` | 32 | 16 | Lề màn (web 24 → 32 như Untitled, DEC-259) |
| `layout/empty-padding` | 80 | 64 | Lề trên dưới màn trống, màn kết quả, đăng nhập (`space/80`, `space/96` thêm ở DEC-259) |
| `layout/content-max-width` | 1280 | — | Rộng nội dung tối đa màn chi tiết, form; màn bảng trải hết (DEC-259) |
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
| `chip/height-sm` · `chip/height` · `chip/height-lg` | 22 · 24 · 28 | 22 · 24 · 28 | Cao chip SM · MD · LG theo Untitled (DEC-259; SM 16 → 22, app MD 26 → 24); SM cho chip ở đầu thẻ (DEC-239) |
| `chip/font-size-sm` · `chip/line-height-sm` · `chip/label-max-width` | 12 · 18 · 160 | 12 · 18 · 160 | Chữ chip SM cố định 12/18 cả web và app; nhãn chip tối đa 160 rồi cắt "…" (DEC-239) |
| `chip/padding-x-sm` · `chip/padding-x` · `chip/padding-x-lg` | 10 · 12 · 14 | như web | Badge: lề phía chữ SM · MD · LG (DEC-310) |
| `chip/padding-x-icon-sm` · `chip/padding-x-icon` · `chip/padding-x-icon-lg` · `chip/icon-gap` · `chip/dot-gap` · `chip/dot-extra-gap` · `chip/dot-size` | 6 · 8 · 10 · 4 · 6 · 2 · 6 | như web | Badge: lề phía chấm/icon; icon → chữ 4; chấm → chữ 6 (= 4 + 2); chấm 6 (DEC-310) |
| `table/row-min-height` · `table/cell-padding-y` · `table/cell-padding-x` | 52 · 16 · 24 | 52 · 12 · 16 | Bảng theo Untitled (DEC-259). `list-row/*` giữ 36 cho List Item trong menu, danh sách |
| `chip/count-height-sm` · `chip/count-height` · `chip/count-height-lg` · `chip/count-radius` · `chip/count-radius-lg` · `chip/count-inset` · `chip/count-inset-lg` · `chip/count-only-offset` | 16 · 16 · 20 · 3 · 4 · 3 · 4 · 4 | như web | Badge: ô đếm cao SM · MD · LG; bo ô đếm; khi có ô đếm lề phải thu về 3 (SM) · 4 (MD, LG) để ô cách đều trên, dưới, phải; Count Only đệm trái khung số 4 để số cách đều hai bên (DEC-303, DEC-310) |
| `avatar-label/width` | 240 | 240 | Avatar label: rộng mặc định, tên và dòng phụ cắt "…" (DEC-303) |
| `chip/count-font-size` · `chip/count-line-height` · `avatar-label/subtitle-size` · `avatar-label/subtitle-line-height` | 12 · 16 · 12 · 16 | 12 · 16 · 12 · 16 | Chữ số đếm Badge và dòng phụ Avatar label cố định 12/16 cả web và app — không theo `type/caption` (app 13/18) để giữ nhóm A cùng số đo (DEC-304) |
| `avatar/size/xs · sm · md · lg · xl · xxl` | 24 · 32 · 36 · 48 · 64 · 88 | 24 · 32 · 36 · 48 · 64 · 88 | Cỡ avatar thang XS–XXL (DEC-201, DEC-203; thêm SM 32 và đổi tên sm → xs, DEC-303); MD 36 khớp ô đầu dòng 36 (DEC-164); XL, XXL cho ảnh đại diện đổi được |
| `avatar/status-size/xs · sm · md · lg · xl · xxl` · `avatar/status-border` | 6 · 8 · 10 · 12 · 14 · 16 · 2 | 6 · 8 · 10 · 12 · 14 · 16 · 2 | Chấm trạng thái avatar, thêm viền trắng 2 (DEC-204); SM 8 và đổi tên theo thang XS–XXL; viền chấm Offline rỗng 2 (DEC-303) |
| `avatar/edit-size/md · lg · xl · xxl` | 20 · 24 · 28 · 32 | 20 · 24 · 28 · 32 | Nút đổi ảnh trên avatar (SM không có; DEC-203) |
| `avatar/icon-size/sm · md · lg · xl · xxl` | 14 · 20 · 24 · 24 · 24 | 14 · 20 · 24 · 24 · 24 | Icon trong avatar Content=Icon và Upload (DEC-242) |
| `avatar/edit-icon-size/md · lg · xl · xxl` | 12 · 14 · 16 · 16 | 12 · 14 · 16 · 16 | Icon camera trong nút đổi ảnh (DEC-242) |
| `avatar/spinner-size/sm · md · lg · xl · xxl` | 12 · 16 · 20 · 24 · 28 | 12 · 16 · 20 · 24 · 28 | Vòng quay Uploading (DEC-242) |
| `avatar/group-overlap/sm · md · lg` · `avatar/ring` | −6 · −8 · −12 · 2 | −6 · −8 · −12 · 2 | Avatar Group: khoảng giữa là số âm = lùi đè ¼ đường kính, gắn vào itemSpacing; viền trắng 2; bước giữa hai tâm = cỡ + 4 − lùi = 22 · 32 · 40 (DEC-205, DEC-242) |
| `tooltip/padding-x · padding-y` · `tooltip/offset` · `tooltip/max-width` | 8 · 4 · 4 · 240 | 8 · 4 · 4 · 240 | Tooltip: lề, cách đối tượng, rộng tối đa; bo `tooltip/radius` 8, mũi tên 8 × 4 (DEC-206) |
| `list-row/min-height` · `padding-x` · `padding-y` · `gap` | 36 · 8 · 8 · 8 | 52 · 12 · 12 · 12 | `Base / List Item`: cao tối thiểu, lề ngang, lề dọc, khoảng giữa các phần; thêm `text-gap` 2, `radius` 8, `value-max-width` 120, `divider-height` 1 (DEC-232) |
| `card/padding-none · compact · spacious` | 0 · 12 · 24 | 0 · 12 · 24 | Padding của `Base / Card` cạnh Default `layout/card-padding` 16 (DEC-234) |
| `card/media-size` · `card/media-size-sm` | 64 · 48 | 64 · 48 | Ảnh nhỏ `.card / Media` MD · SM (DEC-237) |
| `card/radio-size` · `card/radio-ring` · `card/radio-on-ring` | 16 · 1,5 · 5 | 20 · 1,5 · 6 | Radio của Selectable Card (DEC-184, DEC-236) |
| `progress/height/sm · md` · `progress/gap` · `progress/width-default` | 4 · 6 · 2 · 320 | 4 · 6 · 2 · 361 | `Base / Progress`: cao thanh, khe giữa nhóm đoạn, rộng mặc định (DEC-243) |
| `otp/cell-width` | 40 | 48 | Rộng một ô mã OTP; app dùng, web chưa dựng (DEC-244) |

- Mọi số trên thang 4; DEC-164 bỏ ngoại lệ lề thẻ app 14. Không thêm số lẻ ngoài thang.
- **Ô đầu dòng (DEC-164, app):** ô 24 cho icon 16 và 20, radio, ô chọn, cách chữ 8; ô 36 cho vòng icon, avatar, cách chữ 12.
  Icon đầu dòng luôn đặt giữa ô, không đặt trần. Trừ khung có nền: icon đầu khối phụ, khối tóm tắt (DEC-194), icon đầu
  ô tìm, ô nhập và radio thẻ chọn (DEC-196) chạm mép nội dung; và icon cuối dòng (mục 7, DEC-193). Cỡ ô là `card/row-icon-cell` (24) và `card/lead-size` (36); không có token `layout/lead-slot` (từng đổi thành `list-row/lead-slot/*`, bỏ cùng hàng List Row, DEC-231).
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
- **Thanh điều hướng app (DEC-160):** thanh nổi rộng 361 (393 − 2 × 16), cao `nav/height`, bo 24 (28 → 24, DEC-259), cách vùng an toàn
  `nav/offset-bottom`, lề trong `nav/padding-x`; mục lề trên dưới `nav/item-padding-y` nên nền mục đang chọn cao 56, bo
  20 = 24 − 4 (đồng tâm, DEC-165); icon 24; nút Quét mã `nav/scan-size`.

## 7. Lưới, độ rộng, breakpoint (DEC-136, DEC-259, DEC-038, DEC-039)

| Màn | Cột | Rãnh | Lề | Rộng tối đa |
|---|---|---|---|---|
| Web ≥ 1024 | 12 | 32 | 32 | 1280 cho màn chi tiết, form; màn bảng trải hết |
| Tablet 768–1023 | 6 | 24 | 24 | — (DEC-257) |
| App (khung 393) | 4 | 16 | 16 | — |

- Lưới web và app theo Untitled UI (DEC-259): web rãnh 24 → 32, lề 24 → 32; app thay **đường canh K1–K4** (DEC-164, DEC-193,
  DEC-194) bằng **4 cột rãnh 16 lề 16**. Lề màn 16 và lề thẻ 16 không đổi, nên chữ trong thẻ vẫn ở 32 tính từ mép màn.
  Viền 1px của thẻ nằm trong khung, không cộng vào lề (Figma stroke Inside; CSS `box-shadow: inset 0 0 0 1px`).
- Mục 6 còn ghi vị trí chữ dạng "K3 64", "K2b 48": đó là khoảng cách đo từ mép màn, vẫn đúng; tên K không còn là lưới.
- Màn chi tiết web chia **8 cột nội dung + 4 cột thông tin** như Jira (DEC-127).
- **Độ rộng (DEC-259):** `width/xs 320` popover, menu thả rộng · `sm 400` dialog xác nhận, drawer thường · `md 560` dialog
  form, form 1 cột · `lg 720` đoạn văn tối đa, dialog lớn · `xl 960` drawer rộng · `2xl 1280` khung nội dung tối đa web.
- **Breakpoint:** xxs 320 · xs 600 (thêm như Untitled, DEC-259) · 640 · 768 · 1024 · 1280 · 1536. Từ 768 tới 1279 menu trái thu
  còn 64 (cột icon), bấm thì bung 240 đè lên nội dung.

## 8. Lớp nổi (DEC-125, DEC-137, DEC-234)

| Bậc | Viền | Bóng | Dùng cho |
|---|---|---|---|
| `elev/0` | — | không | Ô nhập, khối phụ trong thẻ (phẳng) |
| `elev/1` | `color/border/default` | 0 1 2 · `shadow/sm` | Thẻ (DEC-125) |
| `elev/2` | `color/border/default` | 0 4 12 · `shadow/md` + 0 1 3 · `shadow/md-soft` | Menu thả, popover, gợi ý ô tìm |
| `elev/3` | — | 0 16 40 · `shadow/lg` + 0 4 12 · `shadow/md` | Dialog, sheet, toast |

Màu bóng là biến Semantic (DEC-258), đổi theo sáng/tối như Untitled UI:

| Biến | Light | Dark |
|---|---|---|
| `color/shadow/sm` | #101828 6% | #000 40% |
| `color/shadow/md` | #101828 10% | #000 50% |
| `color/shadow/md-soft` | #101828 6% | #000 40% |
| `color/shadow/lg` | #101828 16% | #000 60% |

`elev/3` lớp 2 đổi 8% → 10% khi gom về biến `shadow/md`.

- Thẻ mặc định có viền mảnh và bóng rất nhẹ (`elev/1`). Bóng đậm chỉ cho lớp nổi tạm (`elev/2`, `elev/3`).
- `Base / Card` chọn Elevation None · Low · Med · High = không bóng · `elev/1` · `elev/2` · `elev/3`, mặc định Low; thẻ đang
  nhấn (Pressed) và Disabled bỏ bóng (DEC-234).
- Effect style Figma tên `elev/1 · 2 · 3`; viền gắn riêng bằng `color/border/default`; màu từng lớp gắn biến `color/shadow/*`.

### 8.1 Làm mờ nền (DEC-258)

| Token | Giá trị | Áp vào |
|---|---|---|
| `blur/sm` | 8 | Đầu màn, thanh công cụ dính trên cùng khi cuộn (nền trắng 70%) |
| `blur/md` | 16 | Thanh điều hướng nổi app (DEC-160), thanh hành động nổi đáy màn (nền trắng 60%) |
| `blur/lg` | 24 | Nền sau dialog, sheet: scrim 35% + blur thay scrim 50% |
| `blur/xl` | 40 | Không dùng trong app nghiệp vụ |

Web: `backdrop-filter: blur(var(--blur-md))`. Flutter: `BackdropFilter(ImageFilter.blur(sigmaX: InvBlur.blurMd, …))`.

## 9. Vùng chạm và focus (DEC-97, DEC-138, DEC-139, DEC-241)

- **App:** vùng chạm tối thiểu 44×44 cho mọi app (ưu tiên iOS). Nút nhìn: 52 ở chân màn, 42 cho nút nhỏ và nút icon;
  phần thiếu là vùng bấm vô hình quanh nút. Hai nút icon cạnh nhau cách nhau đủ để vùng bấm không chồng
  (ghi chú câu 10, trang phỏng vấn).
  Lưu ý: dưới mức 48dp Android khuyên.
- **Web:** đích bấm tối thiểu 24×24 (WCAG 2.2 AA, mục 2.5.8).
- **Focus:** vòng 2px, cách mép 2px, màu `color/border/focus` (than chì) cho mọi khách, không theo dải màu khách
  (DEC-170). Nút Danger: vòng focus màu danger (`button/focus/danger` → `color/action/danger`, DEC-198). Ô nhập
  đang gõ: viền 2px cùng màu than chì.
- **Khe focus (DEC-241, DEC-258):** khe 2px giữa control và vòng tô `color/focus/gap` = nền trang (trắng; Dark 950). Hết nền
  xám nên không còn chế độ Canvas. Vòng là L0 `.focus / Ring` dùng chung.

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

Luật icon ở `design/v2/icons.md`: Lucide 1.58.0 cho web và app; nét 2 trên khung 24 đổi theo cỡ, cả icon trong chip (DEC-300);
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
7. Nền trang luôn trắng (`color/bg/surface`), không dùng nền xám (DEC-258).

## 13. Còn mở

- Dark của Brand (quy ước `_alt`); biến Figma chưa điền Dark, chưa bỏ Context (BL-249, BL-252).
- Có bật Corner smoothing (góc liền mạch kiểu iOS) cho thẻ, sheet trên app không.
- Quyền publish thư viện của gói Figma (DEC-110).
- Việc còn mở của icon: `design/v2/icons.md` mục 10.
