---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://github.com/untitleduico/react (styles/theme.css)
  - https://www.untitledui.com/react/docs/dark-mode
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Color variables, node 6472-97620)
---

# 02 — Colors · Semantic (text / border / fg / bg / alpha / utility / component)

> Light/Dark ghi **alias**, không ghi hex (hex ở `01-colors-primitives.md`).
> Nguồn: S2 (theme.css) + S1 (Figma "Color variables", frame 6472-97620 — 4 section
> Text/Border/Foreground/Background). Cột "Cách dùng" lấy mô tả từ S1; token S2-only ghi chú
> "không có trong bảng tài liệu Figma". Lệch S1↔S2 đánh dấu `⚠ lệch`.

## 1. Alpha + Base (S2)

| Token | Light | Dark | Cách dùng | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `--color-alpha-white` | `rgb(255 255 255)` | `rgb(12 14 18)` | Nền/viền trắng, bị đảo ngược ở dark | S2 | comment: "These will be inverted in dark mode." |
| `--color-alpha-black` | `rgb(0 0 0)` | `rgb(255 255 255)` | Nền/viền đen, bị đảo ngược ở dark | S2 | |
| `--color-transparent` | `rgb(0 0 0 / 0)` | (giữ nguyên) | Trong suốt | S2 | không bị ghi đè ở dark |

### Alpha colors (S1) — 20 biến

S1 có **20 biến alpha theo bậc 10%** (S2 chỉ có 2 biến `--color-alpha-white`/`--color-alpha-black` dạng màu đặc, alpha áp khi dùng):

- `alpha-white-10…100` (10): Light = white X% · Dark = neutral-950 X%
- `alpha-black-10…100` (10): Light = black X% · Dark = white X%

⚠ Lệch S1↔S2: S2 = 2 biến màu đặc (đảo ngược ở dark); S1 = 20 biến theo mức %. Đủ 20 biến trong `tokens.untitled.json` (collection `0. Primitives / Alpha (S1)`).

## 2. Utility colors (S2)

14 thang: `blue, brand, neutral, red, yellow, green, orange, indigo, fuchsia, pink, purple, sky,
slate, emerald, amber`. Mỗi thang có bậc 50–700 (brand thêm hậu tố `_alt`; neutral 50–900).

**Quy tắc flip dark mode** (áp dụng đều cho mọi thang):

- Light: `--color-utility-<hue>-50 = --color-<hue>-50` (tăng dần theo bậc).
- Dark: đảo ngược — `utility-50 → <hue>-950`, `utility-100 → <hue>-900`, …, `utility-600 → <hue>-400`, `utility-700 → <hue>-300`; bậc giữa `500 → 500`.
- Hậu tố `_alt` (brand): light = brand cùng bậc; dark = `neutral` cùng bậc (nền xám thay vì tím).

Ví dụ (`neutral`, `brand`):

| Token | Light | Dark | Token | Light | Dark |
|---|---|---|---|---|---|
| `utility-neutral-50` | neutral.50 | neutral.900 | `utility-brand-50` | brand.50 | brand.950 |
| `utility-neutral-100` | neutral.100 | neutral.800 | `utility-brand-100` | brand.100 | brand.900 |
| `utility-neutral-200` | neutral.200 | neutral.700 | `utility-brand-200` | brand.200 | brand.800 |
| `utility-neutral-300` | neutral.300 | neutral.700 | `utility-brand-300` | brand.300 | brand.700 |
| `utility-neutral-400` | neutral.400 | neutral.600 | `utility-brand-400` | brand.400 | brand.600 |
| `utility-neutral-500` | neutral.500 | neutral.500 | `utility-brand-500` | brand.500 | brand.500 |
| `utility-neutral-600` | neutral.600 | neutral.400 | `utility-brand-600` | brand.600 | brand.400 |
| `utility-neutral-700` | neutral.700 | neutral.300 | `utility-brand-700` | brand.700 | brand.300 |
| `utility-neutral-800` | neutral.800 | neutral.200 | `utility-brand-800` | brand.800 | brand.200 |
| `utility-neutral-900` | neutral.900 | neutral.100 | `utility-brand-900` | brand.900 | brand.100 |

> Đủ 134 token utility nằm trong `tokens.untitled.json`; bảng trên là mẫu, quy tắc giống nhau.

### Utility colors (S1) — 118 biến (so S2 134)

S1 có **118 biến utility**; S2 có **134**. Chênh 16 = `amber` (8) + `emerald` (8) — S2 có, S1 không.

⚠ Lệch tên S1↔S2:

- S1 đặt `utility-error/-warning/-success` (màu red/yellow/green) ↔ S2 đặt `utility-red/-yellow/-green`.
- S2 có thêm `utility-amber` + `utility-emerald` (16 biến) mà S1 không có.

Thành phần 118 biến S1 (frame 6487-347428):

- `utility-neutral-50…900` (10) — Dark: 50→900 … 900→100 (200/300 cùng →700)
- `utility-brand-50…900` (10) + `_alt` (10) — Dark đảo 50→950…900→100; `_alt` dark = neutral xám. ⚠ Figma ghi lỗi tên **"utility-brand_alt"** cho dòng 300_alt (thiếu số bậc).
- `utility-error/warning/success-50…700` (8 × 3 = 24, màu red/yellow/green) — Dark đảo 50→950…700→300 (500→500)
- `utility-orange/-sky/-blue/-indigo/-purple/-fuchsia/-pink/-slate-50…700` (8 × 8 = 64) — cùng quy tắc đảo

Đủ 118 biến trong `tokens.untitled.json` (collection `1. Color modes / Utility (S1)`).

## 3. Text colors (23) — S1 node 6472-97625

| Token | Light | Dark | Cách dùng | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `text-primary` | neutral.900 | neutral.50 | Chữ chính, vd tiêu đề trang | S1 · S2 | |
| `text-secondary` | neutral.700 | neutral.300 | Chữ phụ: nhãn, tiêu đề mục | S1 · S2 | |
| `text-tertiary` | neutral.600 | neutral.400 | Chữ hỗ trợ, đoạn văn | S1 · S2 | |
| `text-quaternary` | neutral.500 | neutral.400 | Chữ nhạt, tương phản thấp, vd tiêu đề cột footer | S1 · S2 | |
| `text-placeholder` | neutral.500 | neutral.500 | Placeholder của input field; neutral-500 tương phản/khả dụng tốt hơn 400 | S1 · S2 | ⚠ lệch (dark): S1=neutral-400, S2=neutral.500 |
| `text-brand-primary` | brand.900 | neutral.50 | Chữ brand chính cho heading (card trong pricing page header) | S1 · S2 | |
| `text-brand-secondary` | brand.700 | neutral.300 | Chữ brand cho buttons, chữ nhấn, highlight, subheading (blog post cards) | S1 · S2 | |
| `text-brand-secondary_hover` | brand.800 | neutral.200 | text-brand-secondary khi hover (brand buttons) | S1 · S2 | |
| `text-brand-tertiary` | brand.600 | neutral.400 | Chữ brand nhạt hơn cho nhấn/highlight (số trong metric cards) | S1 · S2 | |
| `text-brand-tertiary_alt` | brand.600 | neutral.50 | Biến thể tertiary sáng hơn ở dark mode (link buttons) | S1 · S2 | |
| `text-error-primary` | red.600 | red.400 | Chữ trạng thái lỗi mặc định (lỗi input field) | S1 · S2 | |
| `text-warning-primary` | yellow.600 | yellow.400 | Chữ cảnh báo mặc định | S1 · S2 | |
| `text-success-primary` | green.600 | green.400 | Chữ thành công mặc định | S1 · S2 | |
| `text-white` | white | white | Luôn trắng, mọi chế độ | S1 · S2 | S1 ghi `text-white`, S2 ghi `white` — không tính lệch |
| `text-primary_on-brand` | white | neutral.50 | Chữ chính trên nền brand đặc (CTA sections) | S1 · S2 | |
| `text-secondary_on-brand` | brand.200 | neutral.300 | Chữ phụ trên nền brand đặc (CTA sections) | S1 · S2 | |
| `text-tertiary_on-brand` | brand.200 | neutral.400 | Chữ cấp 3 trên nền brand đặc (CTA sections) | S1 · S2 | |
| `text-quaternary_on-brand` | brand.300 | neutral.400 | Chữ cấp 4 trên nền brand đặc (footers) | S1 · S2 | |
| `text-secondary_hover` | neutral.800 | neutral.200 | text-secondary khi hover | S1 · S2 | |
| `text-tertiary_hover` | neutral.700 | neutral.300 | text-tertiary khi hover | S1 · S2 | |
| `text-editor-icon-fg` | neutral.400 | neutral.400 | Icon trình soạn thảo | S2 | không có trong bảng tài liệu Figma |
| `text-editor-icon-fg_active` | neutral.500 | white | Icon editor đang bật | S2 | không có trong bảng tài liệu Figma |
| `text-error-primary_hover` | red.700 | red.300 | Chữ lỗi khi hover | S2 | không có trong bảng tài liệu Figma |

## 4. Border colors (8) — S1 node 6483-314735

| Token | Light | Dark | Cách dùng | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `border-primary` | neutral.300 | neutral.700 | Viền tương phản cao: input fields, button groups, checkboxes | S1 · S2 | |
| `border-secondary` | neutral.200 | neutral.800 | Viền tương phản vừa; viền DÙNG NHIỀU NHẤT, mặc định cho phần lớn component (file uploaders, cards/tables, content dividers) | S1 · S2 | |
| `border-secondary_alt` | `rgb(0 0 0 / 0.1)` | neutral.800 | Biến thể alpha của secondary; chỉ dùng cho menu nổi (input dropdowns, notifications) để mép dưới sắc hơn | S1 · S2 | S1 ghi light `#000000 10%` |
| `border-tertiary` | neutral.100 | neutral.800 | Viền tương phản thấp: divider rất nhạt, trục line/bar chart | S1 · S2 | |
| `border-brand` | brand.500 | brand.400 | Viền brand mặc định, trạng thái active (input fields) | S1 · S2 | |
| `border-brand_alt` | brand.600 | neutral.700 | Viền brand chuyển sang xám ở dark mode (banner, footer kiểu brand) | S1 · S2 | |
| `border-error` | red.500 | red.400 | Viền lỗi mặc định (input fields, file uploaders) | S1 · S2 | |
| `border-error_subtle` | red.300 | red.500 | Viền lỗi nhạt hơn (input field lỗi) | S1 · S2 | |

## 5. Foreground colors (19) — S1 node 6485-339301 · icon / phần tử "mực"

| Token | Light | Dark | Cách dùng | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `fg-primary` | neutral.900 | white | Phần tử không phải chữ tương phản cao nhất, vd icon | S1 · S2 | |
| `fg-secondary` | neutral.700 | neutral.300 | Phần tử không phải chữ tương phản cao, vd icon | S1 · S2 | |
| `fg-secondary_hover` | neutral.800 | neutral.200 | fg-secondary khi hover | S1 · S2 | |
| `fg-tertiary` | neutral.600 | neutral.400 | Tương phản vừa, vd icon | S1 · S2 | |
| `fg-tertiary_hover` | neutral.700 | neutral.300 | fg-tertiary khi hover | S1 · S2 | |
| `fg-quaternary` | neutral.400 | neutral.600 | Tương phản thấp: icon trong buttons, help icons, icon trong input fields | S1 · S2 | ⚠ lệch (dark): S1=neutral-500, S2=neutral.600 |
| `fg-quaternary_hover` | neutral.500 | neutral.500 | fg-quaternary khi hover (help icons) | S1 · S2 | ⚠ lệch (dark): S1=neutral-400, S2=neutral.500 |
| `fg-white` | white | white | Luôn trắng, mọi chế độ | S1 · S2 | |
| `fg-brand-primary` | brand.600 | brand.500 | Màu brand chính cho featured icons, progress bars | S1 · S2 | |
| `fg-brand-primary_alt` | brand.600 | neutral.300 | Như fg-brand-primary nhưng thành xám ở dark mode (horizontal tabs active) | S1 · S2 | |
| `fg-brand-secondary` | brand.500 | brand.500 | Brand phụ: nhấn, mũi tên ở trang marketing (hero header sections) | S1 · S2 | |
| `fg-brand-secondary_alt` | brand.500 | neutral.600 | Như trên nhưng thành xám ở dark mode (brand buttons) | S1 · S2 | |
| `fg-brand-secondary_hover` | brand.600 | neutral.500 | Icon brand phụ hover | S2 | không có trong bảng tài liệu Figma |
| `fg-error-primary` | red.600 | red.500 | Lỗi chính cho featured icons | S1 · S2 | |
| `fg-error-secondary` | red.500 | red.400 | Lỗi phụ: icon trong input field lỗi, chart/icon âm của metrics item | S1 · S2 | |
| `fg-warning-primary` | yellow.600 | yellow.500 | Cảnh báo chính cho featured icons | S1 · S2 | |
| `fg-warning-secondary` | yellow.500 | yellow.400 | Cảnh báo phụ | S1 · S2 | |
| `fg-success-primary` | green.600 | green.500 | Thành công chính cho featured icons | S1 · S2 | |
| `fg-success-secondary` | green.500 | green.400 | Thành công phụ: button dots, chấm online của avatar, chart/icon metrics item | S1 · S2 | |

## 6. Background colors (28) — S1 node 6487-340429

| Token | Light | Dark | Cách dùng | Nguồn | Ghi chú |
|---|---|---|---|---|---|
| `bg-primary` | white | neutral.950 | Nền chính (trắng) cho mọi layout và component | S1 · S2 | |
| `bg-primary_alt` | white | neutral.900 | Nền trắng nhưng chuyển thành bg-secondary ở dark mode | S1 · S2 | |
| `bg-primary_hover` | neutral.50 | neutral.900 | Hover mặc định cho component nền trắng (select menu items) | S1 · S2 | |
| `bg-primary-solid` | neutral.950 | bg.secondary | Nền tối chính; ở dark mode chuyển thành bg-tertiary; dùng cho tooltips | S1 · S2 | ⚠ lệch (dark): S1=neutral-800, S2=bg.secondary (→neutral-900). Figma mô tả "dark → bg-tertiary" (=neutral-800, khớp swatch S1) |
| `bg-secondary` | neutral.50 | neutral.900 | Nền phụ tạo tương phản với nền trắng, vd nền section website | S1 · S2 | |
| `bg-secondary_alt` | neutral.50 | neutral.950 | Nền phụ chuyển thành bg-primary ở dark mode (horizontal tabs kiểu viền) | S1 · S2 | |
| `bg-secondary_hover` | neutral.100 | neutral.800 | Hover cho component nền neutral-50, vd active (navigation items, date pickers) | S1 · S2 | |
| `bg-secondary-solid` | neutral.600 | neutral.600 | Nền tối phụ, dùng cho featured icons | S1 · S2 | |
| `bg-tertiary` | neutral.100 | neutral.800 | Nền cấp 3 tạo tương phản trên nền sáng (toggles) | S1 · S2 | |
| `bg-quaternary` | neutral.200 | neutral.700 | Nền cấp 4 trên nền sáng (sliders, progress bars) | S1 · S2 | |
| `bg-overlay` | neutral.950 | neutral.800 | Nền mặc định của lớp phủ (modals) | S1 · S2 | |
| `bg-brand-primary` | brand.50 | brand.500 | Nền brand chính (check icons) | S1 · S2 | |
| `bg-brand-primary_alt` | brand.50 | bg.secondary | Nền brand chuyển thành bg-secondary ở dark mode (horizontal tabs active) | S1 · S2 | ⚠ lệch (dark): S1=neutral-800, S2=bg.secondary (→neutral-900). Figma tự mâu thuẫn giữa mô tả và swatch |
| `bg-brand-secondary` | brand.100 | brand.600 | Nền brand phụ (featured icons) | S1 · S2 | |
| `bg-brand-solid` | brand.600 | brand.600 | Nền brand đặc mặc định (toggles, messages) | S1 · S2 | |
| `bg-brand-solid_hover` | brand.700 | brand.500 | bg-brand-solid khi hover (toggles) | S1 · S2 | |
| `bg-brand-section` | brand.800 | bg.secondary | Nền section brand tối mặc định (CTA, testimonial sections); dark → bg-secondary | S1 · S2 | ⚠ lệch (dark): S1=neutral-800, S2=bg.secondary (→neutral-900). Figma tự mâu thuẫn giữa mô tả và swatch |
| `bg-brand-section_subtle` | brand.700 | neutral.950 | Nền section brand thay thế để tạo tương phản (FAQ sections); dark → bg-primary | S1 · S2 | |
| `bg-error-primary` | red.50 | red.950 | Nền lỗi chính (buttons) | S1 · S2 | |
| `bg-error-secondary` | red.100 | red.600 | Nền lỗi phụ (featured icons) | S1 · S2 | |
| `bg-error-solid` | red.600 | red.600 | Nền lỗi đặc (buttons, featured icons, metric items) | S1 · S2 | |
| `bg-error-solid_hover` | red.700 | red.500 | Nền lỗi đặc khi hover (buttons) | S1 · S2 | |
| `bg-warning-primary` | yellow.50 | yellow.950 | Nền cảnh báo chính | S1 · S2 | |
| `bg-warning-secondary` | yellow.100 | yellow.600 | Nền cảnh báo phụ (featured icons) | S1 · S2 | |
| `bg-warning-solid` | yellow.600 | yellow.600 | Nền cảnh báo đặc (featured icons) | S1 · S2 | |
| `bg-success-primary` | green.50 | green.950 | Nền thành công chính | S1 · S2 | |
| `bg-success-secondary` | green.100 | green.600 | Nền thành công phụ (featured icons) | S1 · S2 | |
| `bg-success-solid` | green.600 | green.600 | Nền thành công đặc (featured icons, metric items) | S1 · S2 | |

## 7. Component colors (20)

| Token | Light | Dark | Cách dùng | Nguồn |
|---|---|---|---|---|
| `focus-ring` | brand.500 | brand.500 | Vòng focus mặc định | S2 |
| `focus-ring-error` | red.500 | red.500 | Vòng focus lỗi | S2 |
| `featured-icon-light-fg-brand` | brand.600 | brand.200 | Icon nổi bật brand | S2 |
| `featured-icon-light-fg-error` | red.600 | red.200 | Icon nổi bật lỗi | S2 |
| `featured-icon-light-fg-warning` | yellow.600 | yellow.200 | Icon nổi bật cảnh báo | S2 |
| `featured-icon-light-fg-success` | green.600 | green.200 | Icon nổi bật thành công | S2 |
| `featured-icon-light-fg-gray` | neutral.500 | neutral.200 | Icon nổi bật xám | S2 |
| `icon-fg-brand` | brand.600 | neutral.400 | Icon brand | S2 |
| `icon-fg-brand_on-brand` | brand.200 | neutral.400 | Icon brand trên nền brand | S2 |
| `toggle-border` | neutral.300 | transparent | Viền toggle | S2 |
| `toggle-slim-border_pressed` | bg-brand-solid | transparent | Toggle slim đang bật | S2 |
| `toggle-slim-border_pressed-hover` | bg-brand-solid_hover | transparent | Toggle slim bật+hover | S2 |
| `slider-handle-bg` | white | fg-brand-primary | Nền núm slider | S2 |
| `slider-handle-border` | brand.600 | bg-primary | Viền núm slider | S2 |
| `tooltip-supporting-text` | neutral.300 | neutral.300 | Chữ phụ trong tooltip | S2 |
| `footer-button-fg` | brand.200 | neutral.300 | Nút footer | S2 |
| `footer-button-fg_hover` | white | neutral.100 | Nút footer hover | S2 |
| `screen-mockup-border` | neutral.900 | neutral.700 | Viền screen mockup | S2 |
| `app-store-badge-border` | `166 166 166 1` | white | Viền badge app store | S2 |
| `avatar-styles-bg-neutral` | `224 224 224 1` | `224 224 224 1` | Nền avatar neutral | S2 |

## 8. Property color alias (S2 — tầng sinh class Tailwind)

Năm nhóm alias trỏ về semantic ở trên; là nguồn cho các class tiện ích `bg-*`, `text-*`,
`border-*`, `ring-*`, `outline-*`:

| Nhóm | Số biến | Ví dụ |
|---|---|---|
| `--background-color-*` | 30 | `--background-color-primary: var(--color-bg-primary)` |
| `--text-color-*` | 23 | `--text-color-secondary: var(--color-text-secondary)` |
| `--border-color-*` | 10 | `--border-color-brand-solid: var(--color-bg-brand-solid)` |
| `--ring-color-*` | 10 | `--ring-color-error: var(--color-border-error)` |
| `--outline-color-*` | 10 | `--outline-color-primary: var(--color-border-primary)` |

> Lưu ý: `border-color-brand-solid`/`ring-color-brand-solid`/`outline-color-brand-solid` trỏ về
> `--color-bg-brand-solid` (không phải `border-*`) — viền solid dùng màu nền brand.

## 9. Luật dùng

| # | Luật | Nguồn |
|---|---|---|
| 1 | `border-secondary` là viền mặc định của phần lớn component (code inline: `box-shadow: 0 0 0 1px var(--color-border-secondary)`) | S2 typography.css · S1 (6483-314735) |
| 2 | `border-primary` dùng cho viền bảng (`--tw-prose-th-borders`) | S2 typography.css |
| 3 | Placeholder dùng `neutral-500` (không phải 400) — giữ nguyên ở cả 2 mode | S2 |
| 4 | Trên nền brand (`_on-brand`): chữ chính = white (light) / neutral.50 (dark) | S2 |
| 5 | Dark mode: `bg-primary = neutral-950` (nền tối nhất), `fg-primary = white` | S2 |
| 6 | Focus ring mặc định = `brand-500`, lỗi = `red-500` — không đổi giữa 2 mode | S2 |
| 7 | Disabled state không có token riêng — dùng `opacity-50` | S3 upgrade |
| 8 | Nên dùng semantic class (`bg-primary`) thay palette (`bg-gray-50`) để dark tự đúng | S3 dark-mode |
| 9 | `border-secondary_alt` chỉ dùng cho menu nổi (input dropdowns, notifications) để mép dưới sắc hơn | S1 (6483-314735) |
| 10 | `text-placeholder` dùng `neutral-500` vì tương phản/khả dụng cao hơn `neutral-400` | S1 (6472-97625) |
| 11 | Hậu tố `_on-brand` = dùng trên nền brand đặc (CTA sections, footers) | S1 (6472-97625) |
| 12 | Hậu tố `_alt` = biến thể đổi hành vi ở dark mode (thường chuyển thành xám) | S1 (6472-97625 / 6485-339301 / 6487-340429) |
| 13 | Hậu tố `-solid` = nền đặc tối (tooltips, featured icons, buttons, metric items) | S1 (6487-340429) |
| 14 | `fg-*` chỉ dùng cho phần tử không phải chữ (icon, chấm, thanh); chữ thì dùng `text-*` | S1 (6485-339301) |

## 10. Ghi chú

- Đủ 246 biến `--color-*` trong `tokens.untitled.json`; bảng trên là các token semantic + component,
  phần utility ghi quy tắc thay vì 134 dòng (xem JSON).
- S1 (Figma) đã đọc: 4 section Color variables — Text 20 dòng (panel Variables ghi 21), Border 8,
  Foreground 18, Background 28. Token S2 có mà S1 không: `fg-brand-secondary_hover`,
  `text-editor-icon-fg`, `text-editor-icon-fg_active`, `text-error-primary_hover`.
- S1 (Figma) Alpha + Utility: 20 biến alpha + 118 biến utility (xem mục 1, 2) — đã gộp vào `tokens.untitled.json`.
