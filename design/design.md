---
version: 1
name: Astryx
source: "Figma — Astryx Library (Community) · fileKey FifpyOMpZk9OP8qyNzbRVJ"
source-url: "https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/Astryx-Library--Community---Community-"
extracted: 2026-09-27
default-theme: neutral-light
themes: [neutral-light, neutral-dark]   # chỉ dùng Neutral; 6 theme phụ của thư viện nằm ngoài phạm vi
locale: vi-VN                           # định dạng ngày giờ, số, tiền: mục Content & Formatting
primary-device: desktop-web             # chỉ để đề xuất; vẫn hỏi user khi chọn device

colors:            # Mode "Neutral Light" (mặc định). Dark ở khối colors-dark.
  # Core
  accent: "#262626"
  accent-muted: "#f1f1f1"
  on-accent: "#ffffff"
  neutral: "#0000000f"            # đen 6% — nền nút Secondary
  background-surface: "#ffffff"
  background-body: "#f1f1f1"
  background-muted: "#f1f1f1"
  background-inverted: "#0a1317"
  overlay: "#00000080"            # scrim 50%
  overlay-hover: "#0000000d"      # 5%
  overlay-pressed: "#0000001a"    # 10%
  # Text
  text-primary: "#171717"
  text-secondary: "#737373"
  text-disabled: "#a3a3a3"
  text-accent: "#262626"
  text-on-dark: "#ffffff"
  text-on-light: "#171717"
  # Icon
  icon-accent: "#262626"
  icon-primary: "#171717"
  icon-secondary: "#737373"
  icon-disabled: "#a3a3a3"
  # Surface
  surface-card: "#ffffff"
  surface-popover: "#ffffff"
  # Status
  success: "#007004"
  success-muted: "#c5e5c0"
  on-success: "#ffffff"
  error: "#a50c25"
  error-muted: "#facecb"
  on-error: "#ffffff"
  error-inverted: "#aa071e"
  warning: "#745b00"
  warning-muted: "#f8da9d"
  on-warning: "#171717"
  # Border
  border-default: "#00000014"     # đen 8% — divider, hairline
  border-emphasized: "#d4d4d4"    # viền input, card
  # Effects
  skeleton: "#ebebeb"
  elevation-shadow: "#0000001a"
  elevation-shadow-strong: "#0000001a"
  shadow: "#0000001a"             # đen 10% — bóng cột dính khi cuộn ngang Table (code: --color-shadow)
  tint-hover: "#000000"           # chỉ để trộn color-mix, không tô trực tiếp (xem Effects)
  track: "#ccd3db"
  # Component-level (màu "vivid" cho Badge đặc & ProgressBar)
  badge-info-bg: "#0074e2"
  badge-success-bg: "#198100"
  badge-warning-bg: "#ffce2f"
  badge-error-bg: "#e33f4a"
  badge-on-vivid: "#ffffff"
  progress-accent: "#0074e2"
  progress-success: "#198100"
  progress-warning: "#ffce2f"
  progress-error: "#e33f4a"
  input-ring-focus: "#f1f1f1"
  input-ring-hover: "#d4d4d44d"
  input-ring-success: "#1981004d"
  input-ring-warning: "#ffce2f4d"
  input-ring-error: "#e33f4a4d"
  # Categorical (10 họ màu × bg/border/icon/text) — cho tag, biểu đồ, không mang nghĩa trạng thái
  blue-bg: "#c4ddfb"
  blue-border: "#b1c9e7"
  blue-icon: "#00458c"
  blue-text: "#00458c"
  cyan-bg: "#a3e0ef"
  cyan-border: "#91d3e3"
  cyan-icon: "#00505f"
  cyan-text: "#00505f"
  gray-bg: "#e5e5e5"
  gray-border: "#d4d4d4"
  gray-icon: "#525252"
  gray-text: "#262626"
  green-bg: "#c5e5c0"
  green-border: "#b2d1ac"
  green-icon: "#0c5700"
  green-text: "#0c5700"
  orange-bg: "#fad0b5"
  orange-border: "#e6bda2"
  orange-icon: "#6e3500"
  orange-text: "#6e3500"
  pink-bg: "#fccadc"
  pink-border: "#e7b7c8"
  pink-icon: "#83004b"
  pink-text: "#83004b"
  purple-bg: "#eccef3"
  purple-border: "#d8bbdf"
  purple-icon: "#700084"
  purple-text: "#700084"
  red-bg: "#facecb"
  red-border: "#e6bab8"
  red-icon: "#89001a"
  red-text: "#89001a"
  teal-bg: "#a5e3d6"
  teal-border: "#94d6c8"
  teal-icon: "#005348"
  teal-text: "#005348"
  yellow-bg: "#f8da9d"
  yellow-border: "#e4c279"
  yellow-icon: "#584400"
  yellow-text: "#584400"
  # Syntax (CodeBlock)
  syntax-keyword: "#700084"
  syntax-string: "#005600"
  syntax-comment: "#737373"
  syntax-number: "#6e3500"
  syntax-function: "#00458c"
  syntax-type: "#700084"
  syntax-variable: "#171717"
  syntax-operator: "#737373"
  syntax-constant: "#6e3500"
  syntax-tag: "#89001a"
  syntax-attribute: "#584400"
  syntax-property: "#005348"
  syntax-punctuation: "#a3a3a3"

colors-dark:       # Mode "Neutral Dark". Alpha theo code Neutral (neutralTheme.ts). (*) = alpha lấy bằng Light, chưa xác minh.
  accent: "#ebebeb"
  accent-muted: "#262626"
  on-accent: "#171717"
  neutral: "#ffffff1a"            # trắng 10%
  background-surface: "#262626"
  background-body: "#1b1b1b"
  background-muted: "#1b1b1b"
  background-inverted: "#ffffff"
  overlay: "#000000cc"            # đen 80%
  overlay-hover: "#ffffff0d"
  overlay-pressed: "#ffffff1a"
  text-primary: "#fafafa"
  text-secondary: "#a3a3a3"
  text-disabled: "#525252"
  text-accent: "#ebebeb"
  text-on-dark: "#ffffff"
  text-on-light: "#171717"
  icon-accent: "#ebebeb"
  icon-primary: "#fafafa"
  icon-secondary: "#a3a3a3"
  icon-disabled: "#525252"
  surface-card: "#1b1b1b"
  surface-popover: "#1b1b1b"
  success: "#9fe59b"
  success-muted: "#84c9803d"      # alpha 24% (code Neutral)
  on-success: "#171717"
  error: "#ffc6c1"
  error-muted: "#ff9e973d"        # alpha 24%
  on-error: "#171717"
  error-inverted: "#e3193b"
  warning: "#fdcf4f"
  warning-muted: "#deb4333d"      # alpha 24%
  on-warning: "#171717"
  border-default: "#ffffff1a"     # trắng 10%
  border-emphasized: "#525252"
  skeleton: "#525252"
  shadow: "#0000004d"             # đen 30% (code Neutral)
  tint-hover: "#ffffff"
  track: "#5a5e66"
  badge-info-bg: "#6d9cfe"
  badge-success-bg: "#64af4c"
  badge-warning-bg: "#ffce2f"
  badge-error-bg: "#ff705d"
  badge-on-vivid: "#171717"
  input-ring-focus: "#262626"
  input-ring-hover: "#5252524d"   # (*)
  blue-bg: "#9eb7ff"
  blue-text: "#c7d3ff"
  green-bg: "#84c980"
  green-text: "#9fe59b"
  red-bg: "#ff9e97"
  red-text: "#ffc6c1"
  yellow-bg: "#deb433"
  yellow-text: "#fdcf4f"
  gray-bg: "#ffffff"
  gray-text: "#e5e5e5"
  # Các họ categorical còn lại (cyan/orange/pink/purple/teal) và border/icon: xem design-tokens.css

typography:
  font-body: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
  font-heading: "'Cal Sans', Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"   # chỉ có Regular
  font-code: "'JetBrains Mono', ui-monospace, 'SF Mono', Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace"
  display-1:  { fontFamily: Cal Sans, fontSize: 42px, fontWeight: 400, lineHeight: 52px, letterSpacing: 0 }
  display-2:  { fontFamily: Cal Sans, fontSize: 35px, fontWeight: 400, lineHeight: 44px, letterSpacing: 0 }
  display-3:  { fontFamily: Cal Sans, fontSize: 29px, fontWeight: 400, lineHeight: 36px, letterSpacing: 0 }
  heading-1:  { fontFamily: Cal Sans, fontSize: 24px, fontWeight: 400, lineHeight: 32px, letterSpacing: 0 }
  heading-2:  { fontFamily: Cal Sans, fontSize: 20px, fontWeight: 400, lineHeight: 28px, letterSpacing: 0 }
  heading-3:  { fontFamily: Cal Sans, fontSize: 17px, fontWeight: 400, lineHeight: 24px, letterSpacing: 0 }
  heading-4:  { fontFamily: Inter, fontSize: 14px, fontWeight: 700, lineHeight: 20px, letterSpacing: 0 }
  heading-5:  { fontFamily: Inter, fontSize: 12px, fontWeight: 600, lineHeight: 20px, letterSpacing: 0 }
  heading-6:  { fontFamily: Inter, fontSize: 10px, fontWeight: 600, lineHeight: 16px, letterSpacing: 0 }
  large:      { fontFamily: Inter, fontSize: 17px, fontWeight: 600, lineHeight: 24px, letterSpacing: 0 }
  body:       { fontFamily: Inter, fontSize: 14px, fontWeight: 400, lineHeight: 20px, letterSpacing: 0 }
  label:      { fontFamily: Inter, fontSize: 14px, fontWeight: 500, lineHeight: 20px, letterSpacing: 0 }
  supporting: { fontFamily: Inter, fontSize: 12px, fontWeight: 400, lineHeight: 20px, letterSpacing: 0 }
  code:       { fontFamily: JetBrains Mono, fontSize: 14px, fontWeight: 400, lineHeight: 20px, letterSpacing: 0 }

font-size-scale: { 4xs: 6px, 3xs: 7px, 2xs: 8px, xs: 10px, sm: 12px, base: 14px, lg: 17px, xl: 20px, 2xl: 24px, 3xl: 29px, 4xl: 35px, 5xl: 42px }

rounded:
  none: 0px          # theme Neutral cố định 0, không scale (neutralTheme.ts); Figma sửa từ 4 → 0 ngày 01/10/2026
  inner: 6px
  element: 10px
  container: 12px
  page: 28px
  full: 9999px

spacing:             # Base 4px. Khóa = bậc Astryx (Spacing/<bậc>)
  "0": 0px
  half: 2px
  "1": 4px
  1-half: 6px
  "2": 8px
  "3": 12px
  "4": 16px
  "5": 20px
  "6": 24px
  "7": 28px
  "8": 32px
  "9": 36px
  "10": 40px
  "11": 44px
  "12": 48px

size:
  element-sm: 28px
  element-md: 32px
  element-lg: 36px
  border-width: 1px

elevation:
  none: "none"
  # Giá trị theo code Neutral (neutralTheme.ts). Figma: effect style Elevation/* gắn biến Effects/Elevation <Bậc> 1/2/Ring (Light/Dark).
  low: "0 2px 4px #0000000d, 0 4px 8px #0000001a"
  medium: "0 2px 4px #0000000d, 0 4px 12px #0000001a"
  high: "0 4px 6px #0000001a, 0 12px 24px #00000026"
  ring-focus: "inset 0 0 0 3px {colors.input-ring-focus}"
  ring-hover: "inset 0 0 0 3px {colors.input-ring-hover}"
  ring-success: "inset 0 0 0 3px {colors.input-ring-success}"
  ring-warning: "inset 0 0 0 3px {colors.input-ring-warning}"
  ring-error: "inset 0 0 0 3px {colors.input-ring-error}"

elevation-dark:    # Mode Dark: bóng đậm hơn + viền trong trắng mờ (code Neutral).
  low: "0 2px 4px #00000040, 0 4px 8px #00000066, inset 0 0 0 1px #ffffff14"
  medium: "0 2px 4px #00000059, 0 4px 12px #00000080, inset 0 0 0 1px #ffffff1f"
  high: "0 4px 6px #00000080, 0 12px 24px #000000b3, inset 0 0 0 1px #ffffff26"

motion:              # theme Neutral: {fast: 125, medium: 300, slow: 700, ratio: 0.75}; min = base×0.75, max = base÷0.75, làm tròn 5ms
  duration-fast-min: 95ms
  duration-fast: 125ms
  duration-fast-max: 165ms
  duration-medium-min: 225ms
  duration-medium: 300ms
  duration-medium-max: 400ms
  duration-slow-min: 525ms
  duration-slow: 700ms
  duration-slow-max: 935ms
  ease-standard: "cubic-bezier(0.24, 1, 0.4, 1)"

components:
  button-primary:     { backgroundColor: "{colors.accent}", textColor: "{colors.on-accent}", typography: "{typography.label}", rounded: "{rounded.element}", height: "{size.element-md}", padding: "0 12px", gap: 8px }
  button-secondary:   { backgroundColor: "{colors.neutral}", textColor: "{colors.text-primary}", typography: "{typography.label}", rounded: "{rounded.element}", height: "{size.element-md}", padding: "0 12px" }
  button-ghost:       { backgroundColor: "transparent", textColor: "{colors.text-primary}", typography: "{typography.label}", rounded: "{rounded.element}", height: "{size.element-md}", padding: "0 12px" }
  button-destructive: { backgroundColor: "{colors.error-muted}", textColor: "{colors.error}", typography: "{typography.label}", rounded: "{rounded.element}", height: "{size.element-md}", padding: "0 12px" }
  button-hover:       { overlay: "{colors.overlay-hover}" }
  button-pressed:     { overlay: "{colors.overlay-pressed}" }
  button-focused:     { outline: "2px solid {colors.accent}", outlineOffset: 3px }   # code: --focus-outline-*; Figma: stroke 2px ngoài, không offset
  button-disabled:    { opacity: 0.5 }
  text-input:         { backgroundColor: "{colors.background-surface}", border: "1px solid {colors.border-emphasized}", rounded: "{rounded.element}", height: "{size.element-md}", labelTypography: "{typography.label}", valueTypography: "{typography.body}", helperTypography: "{typography.supporting}", labelGap: 4px, focusedBorder: "1px solid {colors.accent}", focusedRing: "{elevation.ring-focus}" }
  card:               { backgroundColor: "{colors.surface-card}", border: "1px solid {colors.border-emphasized}", rounded: "{rounded.container}", padding: { none: 0, compact: 4px, default: 12px, spacious: 20px } }
  badge:              { rounded: "{rounded.full}", height: 20px, padding: "0 8px", gap: 4px, typography: "{typography.supporting}" }
  dialog:             { backgroundColor: "{colors.surface-popover}", rounded: "{rounded.container}", shadow: "{elevation.high}", width: 400px }
  toast:              { backgroundColor: "{colors.background-inverted}", textColor: "{colors.on-accent}", rounded: "{rounded.container}", padding: 12px, gap: 12px, width: 360px, shadow: "{elevation.medium}" }
  banner:             { backgroundColor: "{colors.background-surface}", rounded: "{rounded.container}" }
  table-cell:         { backgroundColor: "{colors.background-surface}", density: { compact: "28px · 4px 8px", balanced: "36px · 8px 12px", spacious: "44px · 12px 16px" } }
  tab:                { height: "{size.element-md}", selectedIndicator: "{colors.icon-accent}", selectedWeight: 600, defaultText: "{colors.text-secondary}" }
  divider:            { subtle: "{colors.border-default}", strong: "{colors.border-emphasized}", thickness: 1px }
  overlay-scrim:      { dark: "{colors.overlay}" }
---
# Astryx — Design System

> Tài liệu này được trích từ file Figma **Astryx Library (Community)**, gồm biến (variables),
> text/effect style, 111 component set và 33 màn mẫu trên trang *Templates*. Đây là **nguồn chuẩn
> duy nhất** cho mọi skill vẽ màn trong workspace (xem `.claude/rules/design-system.md`).
> Bản CSS của cùng bộ token nằm ở `design/design-tokens.css`.

## Overview

Astryx là một design system **đơn sắc, trung tính, mật độ vừa phải**, dành cho sản phẩm dạng
công cụ/ứng dụng làm việc (bảng dữ liệu, form, cài đặt, chat AI, bảng Kanban). Theme mặc định
*Neutral* **không có màu thương hiệu**: màu nhấn `{colors.accent}` (#262626) gần như đen, nên
nút chính là khối than chì chữ trắng. Mọi độ nổi bật đến từ **tương phản sáng–tối và độ đậm chữ**,
không đến từ màu sắc.

Màu chỉ xuất hiện khi mang nghĩa: **trạng thái** (success/warning/error), **nhãn phân loại**
(10 họ categorical cho tag, badge, biểu đồ) và **tô cú pháp** trong code block. Nền trang là
`{colors.background-body}` (#f1f1f1) xám rất nhạt, trên đó đặt bề mặt trắng `{colors.background-surface}`.
Phân lớp dựa vào khác biệt hai tông nền cộng viền mảnh, và chỉ dùng bóng cho lớp nổi (dialog, toast, popover).

Chữ dùng **Cal Sans** cho tiêu đề lớn (Display, Heading 1–3), **Inter** cho phần còn lại và
**JetBrains Mono** cho code. Cỡ chữ gốc là 14px,
line-height 20px, tức là giao diện dày đặc kiểu ứng dụng chứ không thưa như trang marketing.

Thư viện được đồng bộ tự động với codebase `@astryxdesign/core`, và **code là nguồn sự thật**.
Mỗi component trong Figma tương ứng một component React cùng tên (Button, TextInput, Dialog…),
nên spec nên gọi đúng tên component.

**Đặc điểm chính:**

* Đơn sắc: `{colors.accent}` (#262626) cho nút chính, tab đang chọn, focus ring. Không có màu brand.
* Hai tông nền: `{colors.background-body}` (#f1f1f1) cho nền trang/vùng rửa (*wash*), `{colors.background-surface}` (#fff) cho nội dung.
* Nút phụ (Secondary) là **đen 6% trong suốt** (`{colors.neutral}`) chứ không phải nút viền, nên trông như "pill xám nhạt".
* Hover và pressed là **lớp phủ** `{colors.overlay-hover}` (5%) / `{colors.overlay-pressed}` (10%) đặt lên nền sẵn có, không đổi màu nền.
* Bo góc theo **vai trò** chứ không theo cỡ: phần tử tương tác `{rounded.element}` (10px), khung chứa `{rounded.container}` (12px), pill/avatar `{rounded.full}`.
* Kích thước phần tử cố định ba bậc: 28 / 32 / 36px (SM/MD/LG). **MD 32px là mặc định.**
* Dùng theme **Neutral** với hai mode Light (mặc định) và Dark. Thư viện còn 6 theme phụ (Chocolate, Butter, Stone, Y2K, Gothic, Matcha) nhưng **không dùng** trong dự án này.
* Giao diện tiếng Việt, định dạng theo `vi-VN` (xem Content & Formatting).

## Colors

Tên token trong tài liệu là dạng kebab của biến Figma. Cột "CSS Astryx" là tên biến CSS mà
trang *Foundation → Color* công bố, dùng khi đối chiếu với code `@astryxdesign/core`.

### Core — nhấn & nền

| Token | Figma | CSS Astryx | Light | Dark | Dùng cho |
| --- | --- | --- | --- | --- | --- |
| `{colors.accent}` | Core/Accent | `--color-accent` | #262626 | #ebebeb | Nền nút Primary, thanh chỉ báo tab, focus outline, phần đã tô của Slider |
| `{colors.accent-muted}` | Core/Accent Muted | `--color-accent-muted` | #f1f1f1 | #262626 | Nền nhấn nhẹ (mục đang chọn trong list/nav) |
| `{colors.on-accent}` | Core/On Accent | `--color-on-accent` | #ffffff | #171717 | Chữ/icon trên nền accent |
| `{colors.neutral}` | Core/Neutral | `--color-neutral` | #000 @6% | #fff @10% | Nền nút Secondary, chip lựa chọn, badge đếm |
| `{colors.background-surface}` | Core/Background Surface | `--color-background-surface` | #ffffff | #262626 | Bề mặt nội dung chính, input, banner |
| `{colors.background-body}` | Core/Background Body | `--color-background-body` | #f1f1f1 | #1b1b1b | Nền trang, cột Kanban, side nav, hàng nhóm trong bảng |
| `{colors.background-muted}` | Core/Background Muted | `--color-background-muted` | #f1f1f1 | #1b1b1b | Vùng phụ, code block, bong bóng chat |
| `{colors.background-inverted}` | Core/Background Inverted | — | #0a1317 | #ffffff | Bề mặt đảo màu (hiếm) |
| `{colors.overlay}` | Core/Overlay | `--color-overlay` | #000 @50% | #000 @80% | Scrim sau Dialog, Overlay trên ảnh |
| `{colors.overlay-hover}` | Core/Overlay Hover | `--color-overlay-hover` | #000 @5% | #fff @5% | Lớp phủ khi hover mọi phần tử tương tác |
| `{colors.overlay-pressed}` | Core/Overlay Pressed | `--color-overlay-pressed` | #000 @10% | #fff @10% | Lớp phủ khi nhấn; nền ToggleButton đang bật |

### Text & Icon

| Token | Light | Dark | Dùng cho |
| --- | --- | --- | --- |
| `{colors.text-primary}` | #171717 | #fafafa | Chữ chính, tiêu đề, giá trị |
| `{colors.text-secondary}` | #737373 | #a3a3a3 | Mô tả, helper, cột phụ, tab chưa chọn, placeholder |
| `{colors.text-disabled}` | #a3a3a3 | #525252 | Chữ bị vô hiệu |
| `{colors.text-accent}` | #262626 | #ebebeb | Chữ nhấn (link active) |
| `{colors.text-on-dark}` / `{colors.text-on-light}` | #fff / #171717 | cố định | Chữ trên ảnh, scrim, toast tối |
| `{colors.icon-primary}` / `-secondary` / `-disabled` / `-accent` | #171717 / #737373 / #a3a3a3 / #262626 | #fafafa / #a3a3a3 / #525252 / #ebebeb | Icon, cùng thang với chữ |

### Surface

* **Card** (`{colors.surface-card}`, #fff / dark #1b1b1b): nền Card, ClickableCard, SelectableCard.
* **Popover** (`{colors.surface-popover}`, #fff / dark #1b1b1b): Dialog, DropdownMenu, Popover, Toast sáng.

### Status: nghĩa trạng thái

| Nhóm | Đậm (chữ/icon) | Muted (nền nhạt) | On (chữ trên nền đậm) | Vivid (Badge đặc/ProgressBar) |
| --- | --- | --- | --- | --- |
| Success | `{colors.success}` #007004 | `{colors.success-muted}` #c5e5c0 | #ffffff | `{colors.badge-success-bg}` #198100 |
| Warning | `{colors.warning}` #745b00 | `{colors.warning-muted}` #f8da9d | #171717 | `{colors.badge-warning-bg}` #ffce2f |
| Error | `{colors.error}` #a50c25 | `{colors.error-muted}` #facecb | #ffffff | `{colors.badge-error-bg}` #e33f4a |
| Info | — (dùng họ Blue) | `{colors.blue-bg}` #c4ddfb | — | `{colors.badge-info-bg}` #0074e2 |

`{colors.error-inverted}` (#aa071e) dùng cho chữ lỗi trên nền đảo màu.

### Border

* **Default** (`{colors.border-default}`, đen 8%): divider *subtle*, đường kẻ giữa hàng bảng/list, viền header.
* **Emphasized** (`{colors.border-emphasized}`, #d4d4d4): viền input, viền Card, Divider *strong*.
* Độ dày duy nhất: `{size.border-width}` = 1px.

### Effects

* **Skeleton** (`{colors.skeleton}`, #ebebeb): khối giữ chỗ khi đang tải.
* **Elevation Shadow** (`{colors.elevation-shadow}`, đen 10%): biến màu bóng trong Figma. Code Neutral không dùng biến này — bóng lấy giá trị riêng từng bậc (xem `elevation`, `elevation-dark`).
* **Shadow** (`{colors.shadow}`, đen 10% / Dark 30%; Figma `Effects/Shadow`): bóng mép cột dính khi Table cuộn ngang. Không dùng cho card hay popover (đã có elevation).
* **Tint Hover** (`{colors.tint-hover}`, đen / Dark trắng; Figma `Effects/Tint Hover`): **không tô trực tiếp**. Code trộn với màu nền bằng `color-mix`: nền surface + 5% (hover checkbox/radio chưa chọn), viền emphasized + 20%, accent + 15% (hover checkbox/radio/slider đã chọn). Hover của nút vẫn dùng `overlay-hover`.
* **Track** (`{colors.track}`, #ccd3db): rãnh Slider/ProgressBar.
* **Input Ring**: vòng trong (inset 3px) theo trạng thái input: focus / hover (#d4d4d4 @30%) / success / warning / error (@30%). Ring chỉ là lớp phụ; dấu hiệu focus chính của field là **viền 1px `{colors.accent}`** (xem Accessibility). Code vẽ ring 2px, Figma 3px.

### Categorical: nhãn phân loại

Mười họ màu: **Blue, Cyan, Gray, Green, Orange, Pink, Purple, Red, Teal, Yellow**. Mỗi họ có 4 vai
trò `-bg` / `-border` / `-icon` / `-text` (giá trị ở YAML). Dùng cho **Token** (tag),
**Badge** biến thể màu, cột "Breed" trong Searchable Table, và biểu đồ. **Không** dùng họ Red/Green
để thay cho Status — ngoại lệ duy nhất: chip trạng thái nền nhạt theo bảng § Ánh xạ trạng thái nghiệp vụ. Status có token riêng và có nghĩa cố định.

### Syntax

13 token `syntax-*` (keyword, string, comment, number, function, type, variable, operator, constant,
tag, attribute, property, punctuation) chỉ dùng trong **CodeBlock / Code / Markdown**.

## Typography

### Font Family

* **Cal Sans**: `{typography.display-1…3}` và `{typography.heading-1…3}`. Font tiêu đề chỉ có **một độ đậm (Regular)**; nét vốn đã dày nên không cần bold. Dự phòng: Inter.
* **Inter**: mọi chữ còn lại (heading-4…6, body, label, supporting, large, số liệu). Stack dự phòng: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.
* Thư viện Astryx gốc dùng **Figtree**. Dự án đổi sang Cal Sans + Inter ngày 27/09/2026 vì **Figtree thiếu dấu tiếng Việt**: "ẫ" bị hiển thị thành "ã" (mất dấu mũ). Cal Sans và Inter đã được kiểm hiển thị đủ dấu.
* **JetBrains Mono**: `{typography.code}` (Code, CodeBlock, Kbd). Stack dự phòng: `ui-monospace, "SF Mono", Monaco, Consolas, monospace`.

### Hierarchy

| Token | Size | Weight | Line height | Dùng cho |
| --- | --- | --- | --- | --- |
| `{typography.display-1}` | 42px | 400 (Cal Sans) | 52px | Tiêu đề hero, trang giới thiệu |
| `{typography.display-2}` | 35px | 400 (Cal Sans) | 44px | Tiêu đề trang landing/form marketing ("Let's work together", "Payment Request") |
| `{typography.display-3}` | 29px | 400 (Cal Sans) | 36px | Tiêu đề sản phẩm ("Solstice Mug & Plate Set"), tiêu đề login split |
| `{typography.heading-1}` | 24px | 400 (Cal Sans) | 32px | Tiêu đề trang ứng dụng ("All Issues", "Settings", "#1001") |
| `{typography.heading-2}` | 20px | 400 (Cal Sans) | 28px | Tiêu đề Dialog, section lớn |
| `{typography.heading-3}` | 17px | 400 (Cal Sans) | 24px | Tiêu đề khối trong trang ("Contact Information", "Items") |
| `{typography.heading-4}` | 14px | 700 | 20px | Tiêu đề nhóm nhỏ, tên cột Kanban |
| `{typography.heading-5}` | 12px | 600 | 20px | Nhãn nhóm trong nav |
| `{typography.heading-6}` | 10px | 600 | 16px | Nhãn rất nhỏ (superheading) |
| `{typography.large}` | 17px | 600 | 24px | Tiêu đề Card, Banner, Overlay |
| `{typography.body}` | 14px | 400 | 20px | **Chữ mặc định**: đoạn văn, giá trị input, ô bảng |
| `{typography.label}` | 14px | 500 | 20px | Nhãn nút, nhãn field, mục nav, tab |
| `{typography.supporting}` | 12px | 400 | 20px | Helper text, mô tả phụ, badge, timestamp |
| `{typography.code}` | 14px | 400 | 20px | Code inline và block |

### Principles

* Display và Heading 1–3 dùng **Cal Sans** (một độ đậm, tự nó đã nổi). Heading 4–6 dùng **Inter 600–700** vì Cal Sans ở cỡ 10–14px khó đọc. Hai hệ không trộn: màn ứng dụng dùng heading-1, màn landing/form công khai dùng display.
* Không đặt Cal Sans cho chữ đọc liền mạch (đoạn văn, nhãn, ô bảng). Đó là việc của Inter.
* Chỉ có một cỡ chữ đọc chính là 14px. 12px (supporting) dành cho thông tin phụ, không dùng cho nội dung chính.
* Trọng số có 4 bậc token: 400 / 500 / 600 / 700 (`Font Weight/Normal…Bold`).
* Letter-spacing luôn bằng 0, không viết hoa toàn bộ (textCase ORIGINAL). Ngoại lệ thấy trong mẫu: badge "LIMITED EDITION", "CURRENT SESSION".

## Layout

### Spacing System

* **Base unit:** 4px. Có thêm bậc nửa: `{spacing.half}` 2px và `{spacing.1-half}` 6px.
* **Thang:** 0 · 2 · 4 · 6 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 36 · 40 · 44 · 48px (`Spacing/0…12`).
* **Trong component:** khoảng cách icon–nhãn trong nút `{spacing.2}` (8px); nhãn field → input `{spacing.1}` (4px); padding Card default `{spacing.3}` (12px), spacious `{spacing.5}` (20px); Toast padding/gap `{spacing.3}`.
* **Giữa các field trong form:** `{spacing.4}` (16px); giữa các nhóm/section: `{spacing.8}` (32px) kèm Divider.
* **Lề trang ứng dụng:** `{spacing.4}` (16px) quanh nội dung trong Shell; hàng tiêu đề trang (H1 + nút chính) cao 40px (P1).

### Grid & Container

Mọi màn mẫu dựng ở **desktop 1920×1080**. Số đo lấy từ node Figma của mẫu (01/10/2026). Đây là số
của mẫu, không phải token: màn thật giữ đúng khung, chiều cao co theo nội dung.

| Bố cục | Khung | Cột bên trong | Mẫu |
| --- | --- | --- | --- |
| Trang dữ liệu (bảng, board, explorer) | Full-width, lề 16px | Bảng rộng hết (1888px ở 1920); Kanban: cột 300px, cách 16px | P1, P8 |
| Form 1 cột | Khối 800px căn giữa, padding 24px → nội dung 752px | 2 field ngắn cạnh nhau: 368px + cách 16px | P2 |
| Form + tóm tắt | Khối 1100px căn giữa, padding 24px → 1052px | 2 cột 510px, cách 32px (form \| card tóm tắt). Bản Two-column: 2 × 518px, cách 40px | P3 |
| Chi tiết + rail | Khung 1200px (max-width) căn giữa | Cột chính 879px (padding 16px) + divider dọc 1px + rail phải 320px (padding 16px) | P7 |
| Settings · nav trái | Nav 260px (padding 16px) + nội dung max 800px (padding 32px → 736px) | *Nhãn section* 348px \| *field* 348px, cách 40px | P4 (Settings Form) |
| Settings · panel | Khung 1200px (max-width) | Sidebar 300px + nội dung 900px (padding 16px) | P4 (Settings Panels) |
| Login | Card 400px căn giữa | Nội dung 360px (bản SSO 336px) | P6 |
| Login · split | Card 1000px, padding 32px | 2 cột 452px, cách 32px (form \| ảnh) | P6 |
| Chat | Cột hội thoại 760px căn giữa | Panel tài liệu phải 640px (tùy chọn) | P12 |
| Shell | SideNav 300px · TopNav cao 48px | Nội dung dưới TopNav max 1100px | S1, S2 |

**Khung trang dự án (chốt 12/10/2026, thắng số của mẫu ở bảng trên).** Bảng trên là số đo mẫu
Astryx, giữ để tham khảo. Màn thật của dự án dựng theo bảng này (nguồn: `design/_lab/refs/notes.md`
mục "Kết quả chốt Lab ↔ DS", dòng 07–09).

| Vùng | Quy tắc |
| --- | --- |
| Menu trái | 240px, nền surface; thu gọn 64px (chỉ icon). Chân menu: thẻ module + chọn cơ sở. Thay SideNav 300px |
| Thanh trên | Cao 44px: nút thu/mở menu · đường dẫn · tìm · chuông · tài khoản. Thay TopNav 48px |
| Lề nội dung | 24px mọi phía (thay 16px) |
| Trang danh sách | Giãn hết bề rộng còn lại, không max-width |
| Form | Thân form tối đa 720px, căn giữa |
| Trang chi tiết | Tối đa 1440px, căn giữa |
| Khi màn hẹp | Theo § Responsive Behavior › Breakpoints |

### Mẫu bố cục (P = desktop)

> Luật: mẫu dưới đây là **một trong ba phương án bố cục** đề xuất cho mỗi màn — phương án A: mẫu gần
> nhất, chỉnh vùng/nội dung cho hợp màn. Hai phương án B, C đề xuất độc lập từ nhu cầu của màn (vẫn
> dùng token, component và Do's and Don'ts của file này). User chọn. Khung B/C được chọn và dùng lại
> → thêm thành mẫu mới theo Iteration Guide. Mỗi mẫu ghi node Figma để mở xem hoặc lấy instance.

| Mã | Mẫu | Khi nào dùng | Cấu trúc | Node Figma |
| --- | --- | --- | --- | --- |
| **S1** | Shell · Side Nav | Khung ứng dụng có nhiều mục điều hướng | `AppShell` Nav Layout=SideNav Only: SideNav trái (300px, nền body) + vùng nội dung trắng | 2749:8320 |
| **S2** | Shell · Top Nav | Ít mục, sản phẩm hướng người dùng cuối | TopNav cao 48px (logo · menu giữa · hành động phải) + nội dung giữa | 2749:8321 |
| **S3** | Shell · Top + Side | Ứng dụng lớn, 2 cấp điều hướng | `AppShell` Nav Layout=TopNav + SideNav | 2749:8319 |
| **P1** | Danh sách dạng bảng | Tra cứu/quản lý nhiều bản ghi | Header (H1 + nút chính phải) → thanh lọc/tìm full-width → bảng; nhóm hàng theo trạng thái (Grouped)**hoặc** phân trang dưới (Searchable) | 3340:58273 · 3340:58272 |
| **P2** | Form 1 cột | Nhập liệu tuyến tính, form công khai | Tiêu đề display + mô tả → (tùy chọn) 3 card giới thiệu → field xếp 2 cột ngắn / 1 cột dài → nút gửi | 3340:58276 |
| **P3** | Form + tóm tắt | Thanh toán, xác nhận đơn, form có ngữ cảnh | Tiêu đề + mô tả + divider → trái: form chia section H3; phải: Card tóm tắt (danh sách, tổng, Banner info) | 3340:58274 · 3340:58275 |
| **P4** | Cài đặt · nav trái | Trang cài đặt nhiều nhóm | H1 + ô tìm phải → nav dọc trái → mỗi section: nhãn+mô tả trái, field phải, nút Save riêng từng section | 3340:58279 · 3340:58277 |
| **P5** | Cài đặt trong Dialog | Cài đặt mở từ ứng dụng, không rời ngữ cảnh | Dialog lớn 2 cột: nav trái + nội dung phải có Tabs, hàng "tên · mô tả · hành động" | 3340:58278 |
| **P6** | Đăng nhập | Xác thực | Card giữa trên nền body (logo · tiêu đề · 2 input · nút chính full-width · "Or continue with" · SSO)**hoặc** split form \| ảnh | 2749:3026 · 2749:4244 · 2749:4245 · 2749:4246 |
| **P7** | Chi tiết + rail phải | Xem/xử lý một bản ghi | Back link + H1 + hàng meta (badge trạng thái, người, ngày) + hành động phải → Tabs → cột chính (các khối H3 có hành động) + rail phải (Collapsible: Notes, Customer…) | 3340:58289 |
| **P8** | Bảng Kanban | Luồng công việc theo cột trạng thái | H1 + đếm + công cụ phải → các cột nền body, mỗi cột: StatusDot + tên + đếm → card task | 3340:58280 |
| **P9** | Explorer nhiều cột | Duyệt cây phân cấp | Toolbar trên (điều hướng · SegmentedControl view · công cụ) → các cột list lồng nhau → panel chi tiết | 3340:58282 |
| **P10** | Lưới card / catalog | Thư viện, danh mục | H1 → ô tìm full-width → chip lọc + sort → section H2 + lưới card 5 cột | 3340:58284 · 3340:58287 |
| **P11** | Chi tiết sản phẩm | Trang sản phẩm/hàng hóa | Trái: ảnh lớn + lưới thumbnail; phải: tiêu đề display-3, giá, mô tả, SegmentedControl chọn biến thể, số lượng, nút chính + nút phụ full-width, Collapsible | 3340:58288 |
| **P12** | Chat AI | Trợ lý, hỏi đáp | Cột hội thoại giữa (760px) + composer dưới; (tùy chọn) panel tài liệu bên phải | 3340:58291 · 3340:58290 |
| **P13** | Tài liệu | Trang docs/hướng dẫn | Mẫu Documentation Design/Technical | 3340:58286 · 3340:58285 |
| **P14** | Gallery / hero | Trang giới thiệu có ảnh | 6 biến thể: Centered Hero, Classic, Gallery Hero, Mixed, Product, Side | 3340:58293…58297 |
| **P15** | Page Editor / IDE | Công cụ soạn thảo | Mẫu Page Editor, IDE | 3340:58283 · 3340:58281 |

Chưa có mẫu **M (mobile)**. Xem Responsive Behavior và Known Gaps.

### Mẫu bố cục (M = mobile) — spec, chưa có node Figma

> **Đề xuất (29/09/2026), mượn 3 nguyên tắc của `mobile-app-ui-design`, chưa dựng trong Figma —
> vẽ mobile vẫn phải ghi "chưa có chuẩn trong design.md — theo spec M, chưa có node Figma".**
>
> 1. **Lưới 8pt tương thích spacing 4px hiện có**: trên mobile chỉ dùng các bậc đã là số nhân của
>    8 trong thang hiện tại — `{spacing.2}` 8px · `{spacing.4}` 16px · `{spacing.6}` 24px ·
>    `{spacing.8}` 32px · `{spacing.10}` 40px · `{spacing.12}` 48px. Bỏ các bậc lẻ (2, 4, 6, 12,
>    20, 28, 36, 44px) khỏi margin/gutter mobile.
> 2. **Thumb zone**: hành động chính đặt cố định ở đáy màn (sticky bottom bar hoặc `BottomSheet`),
>    không đặt góc trên phải như các mẫu P desktop. Dùng đúng component adaptive Astryx đã có sẵn
>    (`BottomSheet`, `presentation="adaptive"` trên DropdownMenu/Selector/MultiSelector/DateTimeInput),
>    không vẽ control mới.
> 3. **Tối đa 4 cỡ chữ**: `{typography.heading-1}` (24px, tiêu đề trang) · `{typography.heading-3}`
>    (17px, tiêu đề khối) · `{typography.body}` (14px, nội dung chính) · `{typography.supporting}`
>    (12px, phụ). Bỏ display-*, heading-2/4-6, large khi vẽ mobile; label dùng lại body/supporting
>    theo ngữ cảnh.

| Mã | Mẫu | Khi nào dùng | Cấu trúc | Node Figma |
| --- | --- | --- | --- | --- |
| **M1** | Shell mobile | Khung ứng dụng trên mobile, thay S1/S2/S3 — chỉ cho 4 màn gốc | `Device / Frame` → Body cuộn cao hết vùng Content (764), nội dung chạy **dưới** `Bottom Navigation` nổi; Body chừa đệm đáy 92 (= chiều cao thanh) để mục cuối không bị che. Màn con dùng M3/M4 (ẩn thanh). Không dùng hamburger/`MobileNav` (chốt 06/10/2026) | `Example/Shell Mobile` — Templates › Shell (`5383:7822`) |
| **M2** | Danh sách mobile | Thay P1 trên màn hẹp | Header (heading-1 + icon Tìm — chạm mở ô tìm full-width thay hàng tiêu đề) → `Tabs` trạng thái có đếm (cuộn ngang khi nhiều) → mỗi bản ghi 1 `Card`: dòng 1 mã + `Badge` trạng thái, 2–3 dòng `MetadataList` (thay bảng nhiều cột; không dồn hết cột của P1) → chạm thẻ mở M4. **2 biến thể tạo mới:** (a) **Màn gốc** — trong M1, nút [+] dạng icon ở header, có `Bottom Navigation`; (b) **Màn con** — ← quay lại ở header, ẩn thanh, nút "Tạo mới" rộng hết cố định đáy (thumb zone). Trạng thái: có dữ liệu / rỗng / đang tải (`Skeleton` dạng thẻ) / lọc không ra (chốt 06/10/2026). Thẻ dùng `Card` **Elevation=none** — biến thể có bóng của thư viện không có slot Content | `Example/List Mobile` — Templates › Table: Màn gốc (`5389:46482`) · Màn con (`5390:7575`) · Rỗng (`5390:7961`) · Đang tải (`5390:8192`) · Lọc không ra (`5390:8447`) |
| **M3** | Form mobile | Thay P2/P3 trên màn hẹp | Tiêu đề heading-1 → field xếp 1 cột (bỏ 2 cột) → nút gửi cố định đáy (thumb zone) → control chọn dùng`presentation="adaptive"` (mở `BottomSheet` thay popover) | Chưa dựng |
| **M4** | Chi tiết mobile | Thay P7 trên màn hẹp | Back + heading-1 + hàng meta →`Tabs` thay rail phải (rail dời vào 1 tab riêng, theo Collapsing Strategy) → hành động chính cố định đáy | Chưa dựng |

Bảng này là **spec**, không phải mẫu đã vẽ: chưa có node Figma nào cho M1–M4. Trước khi
`figma-screen` dùng được các mã M này, phải dựng frame mẫu tương ứng trong Figma rồi điền cột
*Node Figma*.

### Whitespace Philosophy

Mật độ **vừa phải, ưu tiên ứng dụng**: hàng bảng 36px, nút 32px, chữ 14/20. Khoảng trắng lớn
chỉ có ở màn công khai (login, form liên hệ), nơi nội dung được căn giữa trên nền rộng. Trong
ứng dụng, phân tách vùng bằng **đổi tông nền** (body ↔ surface) và **divider 1px**, không bằng khoảng trống lớn.

## Elevation & Depth

| Level | Treatment | Dùng cho |
| --- | --- | --- |
| Flat | Không bóng, không viền | Nền trang, section, header |
| Hairline | 1px`{colors.border-default}` | Đường kẻ hàng, divider header/section |
| Outlined | 1px`{colors.border-emphasized}` + nền surface | Card, input, SelectableCard |
| Low | `{elevation.low}` (0 2 4 đen 5% + 0 4 8 đen 10%) | Card/Button có Elevation=low |
| Medium | `{elevation.medium}` (0 2 4 + 0 4 12) | Toast, popover, dropdown |
| High | `{elevation.high}` (0 4 6 đen 10% + 0 12 24 đen 15%) | Dialog, lớp nổi trên cùng |
| Scrim | `{colors.overlay}` đen 50% (Dark 80%) | Nền sau Dialog; Overlay trên ảnh |

Mode Dark dùng `{elevation-dark.*}`: bóng đậm hơn và thêm viền trong trắng 8/12/15% để tách lớp trên nền tối.

Button, Card, ClickableCard và SelectableCard có trục **Elevation = none/low/med/high**. Mặc định
là **none**. Chỉ nâng khi phần tử nổi trên ảnh hoặc trên nội dung đang cuộn.

## Shapes

### Border Radius Scale

| Token | Giá trị | Dùng cho (theo trang Foundation → Shape) |
| --- | --- | --- |
| `{rounded.none}` | 0px | "No rounding. Used for sections, headers, dividers." |
| `{rounded.inner}` | 6px | Góc trong của ButtonGroup, nhóm token; checkbox |
| `{rounded.element}` | 10px | Phần tử tương tác: button, input, list item, tab |
| `{rounded.container}` | 12px | Card, popover, dialog, toast, banner |
| `{rounded.page}` | 28px | Panel lớn cấp trang |
| `{rounded.full}` | 9999px | Pill, badge, avatar, status dot, nút tròn |

### Motion

Theo theme Neutral của code (`neutralTheme.ts`, `expandMotionScale.ts`). Figma không có biến thời gian;
khi ghi chú prototype hoặc spec cho dev thì dùng tên token dưới đây.

| Dải | min · chuẩn · max | Dùng cho |
| --- | --- | --- |
| `fast` | 95 · 125 · 165ms | Vi tương tác: hover, pressed, đổi màu, bật/tắt Switch |
| `medium` | 225 · 300 · 400ms | Vào/ra: Dialog, Popover, Toast, BottomSheet |
| `slow` | 525 · 700 · 935ms | Chuyển động liên tục: skeleton pulse, StatusDot pulsing |

* Một đường cong cho mọi chuyển động: `{motion.ease-standard}` = `cubic-bezier(0.24, 1, 0.4, 1)`. Không bounce, không spring.
* Transition theo từng thuộc tính (background, color, opacity, transform, box-shadow), không dùng `all`.
* Spinner của Button chờ `duration-medium-min` rồi mới hiện, để thao tác nhanh không bị nháy.
* **`prefers-reduced-motion: reduce`** → thời lượng về `0s` cho mọi component có chuyển động (code đã làm vậy). Prototype HTML phải làm như `design-tokens.css`.

### Iconography & Imagery

* Icon theo bộ **Lucide** (tên `icon/…`), 4 cỡ: xsm 12 · sm 16 · md 20 · lg 24px. Màu theo token `icon-*`.
* Avatar: 5 cỡ `xsm/sm/md/lg/xl` (20/24/36/48/128px), nội dung Image/Initials/Icon, chấm trạng thái bật bằng BOOLEAN `Status`. Avatar chữ tắt dùng nền `{colors.neutral}`.
* Ảnh trong card/product bo `{rounded.container}`, thumbnail đang chọn có viền 2px `{colors.accent}`.

## Tên trong Figma (khi vẽ bằng công cụ)

Token trong tài liệu này dùng tên kebab (`{colors.text-primary}`). Khi vẽ trên Figma phải gắn
**theo tên biến/style gốc** của Astryx. Quy tắc đổi tên:

| Loại | Trong design.md | Tên trong Figma | Ví dụ |
| --- | --- | --- | --- |
| Màu Core | `{colors.<x>}` | `Core/<X>` | `accent` → `Core/Accent`, `background-surface` → `Core/Background Surface`, `neutral` → `Core/Neutral`, `overlay-hover` → `Core/Overlay Hover` |
| Màu chữ/icon | `{colors.text-<x>}` / `{colors.icon-<x>}` | `Text/<X>` / `Icon/<X>` | `text-secondary` → `Text/Secondary`, `text-on-dark` → `Text/On Dark` |
| Surface | `{colors.surface-<x>}` | `Surface/<X>` | `surface-card` → `Surface/Card` |
| Status | `{colors.success}`, `{colors.error-muted}`… | `Status/<X>` | `error-muted` → `Status/Error Muted`, `on-warning` → `Status/On Warning` |
| Border | `{colors.border-<x>}` | `Border/<X>` | `border-emphasized` → `Border/Emphasized` |
| Effects | `skeleton`, `track`, `shadow`, `tint-hover`, `elevation-shadow` | `Effects/<X>` | `track` → `Effects/Track`; bóng elevation: `Effects/Elevation Low 1`… (chỉ dùng trong effect style) |
| Categorical | `{colors.<họ>-bg/-border/-icon/-text}` | `<Họ>/Background`, `/Border`, `/Icon`, `/Text` | `blue-bg` → `Blue/Background` |
| Text style | `{typography.display-n}` / `heading-n` | `Display/Display n` / `Heading/Heading n` | `heading-1` → `Heading/Heading 1` |
|  | `{typography.body/large/label/code/supporting}` | `Text/<X>` | `body` → `Text/Body` |
| Radius | `{rounded.<x>}` | `Radius/<X>` | `element` → `Radius/Element` |
| Spacing | `{spacing.<n>}` | `Spacing/<n>` | `spacing.4` → `Spacing/4`, `spacing.half` → `Spacing/half` |
| Size | `{size.element-sm/md/lg}` | `Element/Small/Medium/Large` |  |
| Elevation | `{elevation.low/medium/high}` | effect style`Elevation/Low/Medium/High` | ring:`Input Ring/Focus`… |

Cú pháp với reqwise `figma_write`: `fill: "$Core/Background Surface"`, `textStyle: "Heading/Heading 1"`,
`tokens: { padding: "Spacing/4", cornerRadius: "Radius/Container" }` (đã chạy thử ngày 27/09/2026).

**Mặc định của thư viện không phải mặc định của thiết kế.** Khi vừa tạo instance, component ra
biến thể đầu bảng, **không** phải cỡ MD. Luôn đặt thuộc tính tường minh:

* **Button**: mặc định là `Size=SM` và `Icon=true` (có icon đầu). Phải đặt `Size: "MD"`, `Icon: false` (trừ khi cần icon), `Label`, và `Variant` đúng vai trò.
* **TextInput, Selector, TextArea, Date/Time/NumberInput…**: mặc định `size=sm`, nên phải đặt `size: "md"`.
* **TextInput**: thuộc tính `placeholder` và `statusText` **không** đẩy xuống lớp chữ đang hiển thị, nên phải `setText` trực tiếp lên lớp chữ ("name@company.com", "Error message goes here"). Nhãn nằm trong FieldLabel con (lớp chữ `label`), cũng phải `setText`. Bật `showLabel` làm lộ dòng "Description text" dù `description=false`, nên phải ẩn lớp chữ `description`.
* **Banner**: vùng `EndArea` luôn chiếm ~100px bên phải kể cả khi trống, làm tiêu đề xuống dòng. Không có hành động cuối thì ẩn `EndArea`.
* **MetadataList / MetadataListItem**: thuộc tính `Value` (và `Label`) không đẩy xuống lớp chữ, luôn hiện chữ "Value", nên phải `setText`. Giá trị dài (địa chỉ) bị tràn vì `Value Slot` ôm theo chữ: đặt `Value Slot` là `primaryAxisSizingMode: "FIXED"` + `layoutAlign: "STRETCH"`, chữ bên trong là `layoutGrow: 1` + `textAutoResize: "HEIGHT"`.
* **Avatar**: thư viện có **2 bộ cùng tên "Avatar"**. Luôn lấy theo key trong `figma-library-keys.json` (`ef7bf337…`, `Size = xsm…xl`, TEXT `Initials`, BOOLEAN `Status`); bộ này khớp code và được `AvatarGroup`, Activity Log dùng. **Không** tìm theo tên: dễ ra bộ trưng bày `Size = Tiny…Large` (`eb5fdb28…`), bộ đó không có thuộc tính chữ tắt. Chữ tắt của Avatar chỉ đạt 4,16:1 (lỗi của thư viện).
* **Thanh Tabs** phải đặt trên nền surface (trong card/header), **không** đặt trực tiếp trên `Core/Background Body`: chữ tab chưa chọn là text-secondary, trên nền body chỉ đạt 4,2:1.
* **Banner** có nút ở `End Content`: slot mặc định cao cố định 20px sẽ cắt nút 32px, nên phải đặt slot `counterAxisSizingMode: "AUTO"` và `EndArea` `clipsContent: false`.
* **Mẫu P7 (Order Detail) có lỗi sẵn:**
  - Hàng giá trị trong khối Invoice (`ValueRow`) cố định rộng 890px, đẩy cột số tiền ra ngoài vùng hiển thị (ảnh mẫu gốc cũng không thấy số tiền). Phải đặt `ValueRow` bằng bề rộng `Value Slot` và cho ô mô tả `layoutGrow: 1`.
  - Trong rail, `Value Slot` cố định 226px nên tràn. Phải đặt `layoutGrow: 1` và resize theo phần còn lại.
  - Ba khối (ItemsCard, InvoiceCard, TimelineSection) tô bo góc 12 cứng, cần gắn `Radius/Container`.
* **Gắn text style cho chữ tô cứng phải theo độ đậm gốc**, không theo cỡ: chữ 14px đậm (tên người, số tiền) là `Heading/Heading 4`, không phải `Text/Body`. Gắn sai thì mất đậm; lượt kiểm tự động không bắt được, chỉ ảnh chụp mới lộ.
* **Thuộc tính TEXT của một component set dùng chung một giá trị mặc định cho mọi biến thể.** Sửa chữ ở một biến thể sẽ đổi luôn các biến thể khác. Biến thể cần chữ mẫu khác nhau (ví dụ Timer Elapsed/Clock) thì không gắn thuộc tính TEXT.
* **Công cụ không tạo được slot** (`type: "SLOT"`). Nội dung tự do thì dùng thuộc tính INSTANCE_SWAP cùng các component mẫu nội dung (xem BottomSheet, ComplexSelector).
* **Đổi biến thể (`Variant`) làm đổi id các lớp con** của instance (ví dụ thanh tô trong ProgressBar), nên phải đọc lại id sau khi đổi biến thể.
* **Bảng bằng TableHeaderCell/TableCell**: đặt `Density: "Balanced"`, resize từng ô theo bề rộng cột, `setText` lên chữ "Column"/"Cell". Ô chứa Badge: ẩn chữ "Cell", đặt Badge vào slot `Content`. Hàng là frame ngang `itemSpacing: 0`. Tổng bề rộng cột = bề rộng thẻ − padding − **2px viền** (quên 2px thì cột cuối tràn).
* **ProgressBar không có thuộc tính giá trị**: phần tô bị khóa ở khoảng 65% và không resize được trên instance. Muốn hiện đúng giá trị thì phải detach riêng thanh đó rồi resize `Fill` (token màu vẫn giữ). Đây là chưa có chuẩn, nên ghi vào báo cáo màn.
* **Stepper**: dùng `Stepper / Step` (bổ sung từ code, xem mục *Bổ sung từ code*). Không tự dựng từ StatusDot + Divider nữa.
* **`Core/Background Muted` cũng là #f1f1f1**: chữ secondary trên nền này chỉ đạt 4,2:1, giống nền body. Vùng có chữ phụ phải dùng nền surface + viền `Border/Default`.
* **Button State=Loading**: nhãn trong biến thể này tô `#000000` cứng (lỗi của thư viện), `auditDesignSystem` sẽ báo. Không sửa component chính.
* Còn lại: đọc `componentProperties` trả về sau khi instantiate, rồi đặt mọi trục ảnh hưởng đến hiển thị.
* **Lượt kiểm tự động không bắt được chữ mẫu còn sót.** Các lỗi trên chỉ lộ ra ở ảnh chụp, nên phải xem ảnh chụp trước khi báo xong.

## Components

Tất cả là COMPONENT_SET, có biến thể theo trục. Tên thuộc tính đúng như Figma
(để `setProperties` khi vẽ). **MD là cỡ mặc định** cho mọi control.

> **Chọn component nào, dùng thế nào:** xem `design/components.md`. File đó có Usage, Nên/Không nên và
> Examples của 99 component, dịch từ Astryx và chia theo 11 section của astryx.atmeta.com. Mục này
> chỉ giữ tên thuộc tính trong Figma.

**Định dạng example trên Figma (Block).** Mỗi example của Astryx là một frame `Block — <tên example>`
dựng từ mẫu `TPL_BLOCK` (node `2107:6322`), rộng 1320px, gồm 3 phần:

* **Header**: tên example, giữ nguyên tiếng Anh như Astryx (để tra ngược mã nguồn). Tiêu đề trang dùng Cal Sans, còn lại Inter.
* **Description**: mô tả dịch sang tiếng Việt, chỉ dịch từ Astryx, không thêm ý.
* **Preview**: bản dựng thật bằng instance của thư viện. Chữ trong preview bằng tiếng Việt, dữ liệu mẫu
  theo ngữ cảnh dự án (thiết bị, lệnh sửa chữa, kỹ thuật viên). Tên định danh code (prop, tên tệp,
  tên tool) giữ nguyên. Khi thư viện thiếu biến thể mà example cần thì dựng tạm và ghi một dòng chú
  thích ngay trong preview, ví dụ "Thư viện chưa có biến thể ghost — vẽ tạm bằng …".

Block nằm ngay dưới khung `Hướng dẫn · <Component>` của component đó, theo thứ tự example của Astryx.
Trang Chat gom mọi component trong một khung, nên Block nằm trong nhóm `Examples · <Component>`.
Component bố cục không có hình trong thư viện (Grid, Layout, ScrollableArea, Stack) vẫn có khung
hướng dẫn và Block; preview dựng bằng auto-layout + token để minh họa hành vi.

**Web và Mobile: một component, không chia hai bộ (29/09/2026).** Astryx là thư viện React cho web
(không có React Native / iOS / Android). 111 component trong `packages/core/src` chia theo chức năng,
**không** tách thư mục web/mobile. Màn nhỏ được xử lý bằng cách *cùng một component đổi cách hiển
thị* (xem *Responsive Behavior*). Vì vậy trên Figma, **không dựng component set "Mobile" song song**
cho mọi component. Thay vào đó mỗi example được bày theo **hàng ghép cặp**:

* Khung examples tên `Examples · Web | Mobile`, trên cùng là hàng nhãn cột `WEB — Desktop` (1320) |
  `MOBILE — App (375px)` (454), cách nhau 24px.
* Mỗi example là một hàng `Row · <tên example>` (auto-layout ngang). Ô trái `Web / Block — …` là
  Block gốc, ô phải `Mobile / Block — …` cùng tiêu đề. Cả hai ô đặt chiều cao **Fill** để luôn bằng nhau.
* Block vốn đã so sánh cả hai nền tảng (vd *Dialog — Adaptive presentation*) để một hàng trải hết bề
  rộng, tên `Cả hai nền tảng / Block — …`.
* Chưa áp lên file Figma nào (đã thử trên Dialog rồi hoàn tác, 29/09/2026). Khi áp, làm từng trang và qua duyệt.

Ô Mobile chứa gì, theo nhóm component:

| Nhóm | Component | Ô Mobile |
| --- | --- | --- |
| Đổi sang bottom sheet trên màn cảm ứng nhỏ | Dialog (mẫu Adaptive), DropdownMenu, MoreMenu, ContextMenu, Selector, MultiSelector, Popover (mẫu BottomSheet Alternative) | Bản **bottom-sheet** của chính component đó (instance BottomSheet thật) |
| Có bản cảm ứng riêng bên trong | DateInput, TimeInput, DateTimeInput (`TouchDateField`, `NativeDateField`, `TouchTimeField`…) | Bản cảm ứng/native picker |
| Chỉ dùng cho màn nhỏ | BottomSheet, BottomSheetSwitcher, MobileNav, MobileNavToggle; AppShell ở chế độ mobile | Có component set riêng; ô Web ghi "Không dùng trên desktop" hoặc chỉ component thay thế (vd SideNav) |
| Tự co giãn, không đổi hình | Còn lại (Button, Badge, Card, Banner…) | Ghi "Giống bản web", chỉ vẽ khi bố cục thực sự khác |

Chưa có bản mobile thì để ô giữ chỗ viền nét đứt "Chưa có bản mobile — chưa có chuẩn trong design.md",
không tự vẽ.

### Action

**`button`** · *Button* (3:12652): Variant = **Primary / Secondary / Ghost / Destructive** · Size = SM 28 / **MD 32** / LG 36 · State = Rest / Hover / Pressed / Disabled / Focused / Loading · Type = Default / Icon Only · Elevation. Padding ngang 12px, gap 8px, bo `{rounded.element}`, chữ `{typography.label}`. Có icon đầu (Icon) và vùng cuối (End Content).

* **Primary**: nền `{colors.accent}`, chữ `{colors.on-accent}`. Hành động chính của vùng.
* **Secondary**: nền `{colors.neutral}` (đen 6%), chữ `{colors.text-primary}`. Hành động phụ ("View Options", "Restock", "Sign In").
* **Ghost**: trong suốt, chỉ có chữ. Hành động nhẹ ("Cancel", "Fulfill item", "Refund", "Log out").
* **Destructive**: nền `{colors.error-muted}`, chữ `{colors.error}`. Xóa, vô hiệu hóa.
* Hover: phủ `{colors.overlay-hover}` · Pressed: phủ `{colors.overlay-pressed}` · Focused: viền ngoài 2px `{colors.accent}` · Disabled: opacity 0.5 · Loading: spinner thay nội dung.

**`toggle-button`** · *Button / ToggleButton*: dạng ghost, `isPressed` phủ overlay-pressed và chữ semibold. Dùng cho thanh công cụ, chuyển chế độ xem.

**`button-group`** · *Action / ButtonGroup*: gộp nút liền nhau, chung divider 1px, chỉ bo góc ngoài.

**`segmented-control`** · *SegmentedControl*: chọn **một giá trị** (không phải chuyển view). Text / Icon + Text / Icon Only; SM/MD/LG.

**`link`** · *Link*: Color = active/primary/secondary/inherit · Underline · External.

**`dropdown-menu`**, **`more-menu`** (nút "…"), **`context-menu-item`** (có biến thể Destructive), **`toolbar`** (slot Start/Center/End · Density Default/Compact · Variant Transparent/Section/Wash).

### Form Controls (trước đây: Data Input)

Mọi field dùng chung giải phẫu **Field**: *nhãn* (`{typography.label}`, chỉ báo Required/Optional, tooltip) → *control* → *mô tả/thông báo trạng thái* (`{typography.supporting}`). Chung trục **state** = rest / hover / focused / error / warning / success / loading / disabled và **size** = sm / md / lg.

| Component | Ghi chú |
| --- | --- |
| **TextInput** (23:57023) | Nền surface, viền`{colors.border-emphasized}`, bo 10px, cao 32 (md). Icon đầu, statusMessage. Focus: viền đổi sang `{colors.accent}` 1px + inset ring; hover/error hiện bằng inset ring 3px (error: viền `{colors.error}` kể cả khi focus). Mọi field nhập (TextArea, NumberInput, Selector, DateInput…) cùng quy tắc |
| **TextArea**, **NumberInput**, **InputGroup** | InputGroup: prefix/suffix gắn liền (đơn vị, nút) |
| **Selector** / **MultiSelector** | Dropdown chọn; MultiSelector hiển thị Placeholder / Count / Labels / Badges |
| **Typeahead**, **Tokenizer** | Gõ để gợi ý; nhập nhiều giá trị dạng token |
| **DateInput**, **TimeInput**, **DateTimeInput**, **DateRangeInput**, **Calendar** | Calendar Single/Range, 1–2 tháng |
| **Checkbox** (CheckboxInput / CheckboxList / CheckboxListItem) | Unchecked/Checked/Indeterminate, sm/md, có mô tả |
| **Radio** (RadioList / RadioListItem) | Dọc/ngang, có mô tả |
| **Switch** | Bật/tắt có hiệu lực ngay; nhãn trước/sau, có mô tả |
| **Slider** | single/range, có marks, value, status |
| **FileInput** | input hoặc dropzone |
| **PowerSearch** | Ô tìm có filter chip, đếm kết quả, popover gợi ý field/giá trị |

### Feedback & Status

**`badge`** · *Badge* (8:1063): Shape = **Pill** (cao 20, padding 0 8, bo full) / **Dot** (8px) · Variant = Neutral / Info / Success / Warning / Error (nền *vivid*) + 9 màu categorical (nền `-bg`, chữ `-text`). Chữ `{typography.supporting}`, có icon tùy chọn.

**`status-dot`** · *StatusDot*: chấm 8px, positive / warning / negative / info / neutral, `isPulsing` cho trạng thái trực tiếp.

**`banner`** · *Banner*: thông báo **bền** trong trang. Status info/success/warning/error · Container card/section · có mô tả, nút đóng, vùng nội dung, vùng hành động cuối.

**`toast`** · *Toast*: thông báo **tạm thời**. Nền `{colors.background-inverted}` (tối ở Light, sáng ở Dark), chữ `{colors.on-accent}` (đảo theo nền); type error nền `{colors.error-inverted}`, chữ trắng. 360px, bo 12, bóng medium; type default/error.

**`progress-bar`** (accent/success/warning/error/neutral; determinate/indeterminate) · **`spinner`** (sm/md/lg/xl, onMedia) · **`skeleton`** (bo none→rounded).

### Container

**Card** (padding none 0 / compact 4 / **default 12** / spacious 20 · elevation) · **ClickableCard** (cả card là vùng bấm: Rest/Hover +5% overlay + viền đậm/Pressed +10%/Focused/Disabled) · **SelectableCard** (chọn nhiều, Selected true/false) · **Collapsible** (mở/đóng khối nội dung).

### Content

**Heading** (Level 1–4) · **Text** (có truncation 1 dòng) · **Avatar** · **Token** (tag có thể xóa, 11 màu) · **Timestamp** (Relative / Auto / Date / Date Time / Time / System…) · **Code**, **CodeBlock**, **Markdown**, **Kbd** · **Thumbnail** (Image/Placeholder/Loading/Uploading) · **Citation** · **EmptyState** (icon + tiêu đề + mô tả + hành động; Default/Compact).

### Layout

**AppShell** (Nav Layout: TopNav + SideNav / SideNav Only / TopNav Only / Content Only · Variant Elevated/Wash/Surface/Section · Banner) · **Section** (section/transparent/wash) · **FormLayout** (Vertical / Horizontal / Horizontal Labels) · **Divider** (subtle/strong, ngang/dọc, có nhãn) · **AspectRatio** · **ResizeHandle**.

### Navigation

**SideNav** (Expanded/Collapsed; SideNavHeading, SideNavItem Default/Hover/Selected/Disabled, lồng cấp) · **TopNav** (TopNavItem, TopNavMenu, TopNavMegaMenu) · **MobileNav** (drawer trượt từ Start/End) + **MobileNavToggle** (hamburger) · **Tabs** (TabList sm/md/lg, có divider; Tab đang chọn: chữ primary semibold + thanh chỉ báo accent) · **Breadcrumbs** (Chevron/Slash) · **Pagination** (Pages/Count/Compact/Dots) · **OutlineItem** (mục lục 4 cấp).

### Overlay

**Dialog** (Standard 400px / Fullscreen · header có tiêu đề, phụ đề, nút đóng · footer actions · divider tùy chọn; bóng high, bo 12) · **Overlay** (nội dung trên ảnh với scrim dark/light/none) · **CommandPaletteItem** · **Toast**.

### Table & List

**TableHeaderCell** (sortable, checkbox, filter, resizable, căn phải) · **TableCell** (Density **Compact 28** / **Balanced 36** / **Spacious 44** · Default/Hovered/Selected · checkbox đầu, nút mở rộng, divider dưới/phải) · **List / ListItem** (Compact/Balanced/Spacious, slot đầu/cuối) · **Item** (hàng tổng quát: Marker · Start · Label+Description · End) · **MetadataList** (cặp nhãn–giá trị, Inline/Stacked, 1 hay nhiều cột) · **TreeList** (có/không đường dẫn) · **OverflowList** ("+3 more").

### Phân trang danh sách (theo SC-04, 29/09/2026)

Nguồn: `web-common-rules.md` SC-04 (phân trang) và 2.17 (nhóm dữ liệu). Component: **`Pagination`**
(trang Navigation) · Variant = **Pages** / Count / Compact / Dots / None · Size = md / sm ·
`Has Prev`, `Has Next`, `Show Page Size Selector` · slot `Pages`. Hướng dẫn chung của component:
`design/components.md` § Pagination.

**Theo SC-04 (đã chốt):**

| Thành phần | Quy tắc |
| --- | --- |
| Vị trí | Cuối **mọi** màn danh sách (mẫu P1 và danh sách khác), dưới nội dung nó điều khiển |
| Số bản ghi/trang | `Show Page Size Selector` = bật · lựa chọn **25 / 50 / 100** · mặc định **50** |
| Bố cục | **Trái:** ô số bản ghi/trang, chữ *"50 / trang"* · **Phải:** Trước · số trang · Sau. Không có nhãn tổng riêng — tổng số kết quả sau lọc hiện ở hàng 2 thanh công cụ (*"128 kết quả"*, § Bộ lọc nâng cao) |
| Số trang | `Variant=Pages`: trang đầu, trang hiện tại ± 1, `…`, trang cuối |
| Trước / Sau | Icon `<` / `>`; vô hiệu (Disabled) ở trang đầu / trang cuối |
| Nhóm dữ liệu | Phân trang theo **nhóm** (mỗi nhóm = 1 đơn vị). Nhóm đầu mở sẵn tối đa 10 bản ghi con; > 10 thì nút **"Xem thêm"** cuối nhóm, mỗi lần thêm 10 |

* **Khác SC-04 — nhãn tổng (chốt 12/10/2026):** SC-04 ghi nhãn *"50 bản ghi trên 1 trang"*. Bỏ nhãn
  này: ô chọn *"50 / trang"* đã nói đúng thông tin đó, đặt nhãn cạnh ô là lặp. Tổng số bản ghi sau lọc
  đã có ở thanh công cụ nên phân trang không nhắc lại. Các phần khác của SC-04 giữ nguyên.
* **Khác SC-04 (chốt 01/10/2026):** SC-04 ghi "trang hiện tại highlight màu xanh lá". Theme Neutral không có màu xanh lá
  cho điều hướng (xem Don't: không thêm màu brand), nên dùng trạng thái chọn sẵn có của `Pagination`
  (`{colors.accent}`).
* Chỉ có 1 trang thì vẫn hiện bộ chọn số bản ghi, nhưng ẩn số trang và nút Trước/Sau
  (khớp "Không nên" của components.md: không phân trang khi mọi mục vừa một trang).

**Phần SC-04 chưa nói (chốt 01/10/2026, KG-17):**

* Đổi bộ lọc, tìm kiếm, sắp xếp hoặc số bản ghi/trang → về **trang 1**.
* Mở chi tiết rồi quay lại danh sách → **giữ** trang, bộ lọc và vị trí cuộn cũ.
* Đang chuyển trang → giữ header + bảng, thay các hàng bằng `Skeleton` (không xoá trắng bảng).
* Mobile (mẫu M2): không dùng số trang; tải thêm khi cuộn tới cuối (hoặc nút "Xem thêm"), mỗi lần
  bằng số bản ghi/trang của desktop.
* Danh sách trong panel (vd Notification Center): tải 20 dòng, cuộn tới cuối tự tải tiếp, dòng
  `Skeleton` ở cuối khi đang tải; không dùng số trang.

### Quy tắc bảng danh sách (theo 2.9, 2.14, 2.16–2.20, SC-07 — 01/10/2026)

Nguồn: `web-common-rules.md`. Áp dụng cho mọi bảng danh sách (mẫu P1). Cột/trường cụ thể (cột
nào tìm, nhóm, lọc được; action nào có ở trạng thái nào) do từng UC định nghĩa.

| Quy tắc | Chuẩn |
| --- | --- |
| **Căn lề** (2.14) | Số, tiền, % → **phải** · ngày giờ → **giữa** · văn bản, trạng thái → **trái**. Tiêu đề cột căn theo dữ liệu của cột (TableHeaderCell/TableCell Align tương ứng) |
| **Tìm kiếm** (2.9) | Tìm gần đúng trên toàn bộ dữ liệu bảng. Chạy khi nhấn **Enter** hoặc click ra ngoài ô tìm; màn tìm realtime thì debounce **300ms**. Trường cố định (trạng thái, phân loại…) không tìm được → tooltip trên ô tìm liệt kê các trường đó, user dùng lọc thay thế |
| **Freeze cột** (2.16) | Chỉ khi bảng phải cuộn ngang. Cột đầu (Tên/Mã) cố định trái, cột action cố định phải; cột cố định có bóng nhẹ ở cạnh trong. Đủ rộng hiện hết cột thì không freeze |
| **Nhóm** (2.17) | Nút **Nhóm** trên toolbar, chọn **1 cột**; chọn **Xoá** để bỏ nhóm. Dòng cha = giá trị nhóm + số bản ghi ("Petrolimex (5)"). Nhóm đầu mở sẵn tối đa 10 dòng con, nhóm khác thu gọn; click dòng cha để mở/thu. > 10 dòng → **"Xem thêm"** (+10 mỗi lần). Phân trang theo nhóm (xem Phân trang) |
| **Sắp xếp** (2.18) | Click tiêu đề cột: lần 1 tăng dần ↑ → lần 2 giảm dần ↓ → lần 3 về mặc định. Mọi cột sort được; mỗi lúc chỉ **1 cột** (sort cột khác thì cột cũ reset). Chưa sort: icon mờ. Mặc định: **mới nhất trước** (thời gian tạo giảm dần) |
| **Export** (2.19) | Xuất PDF / Excel **toàn bộ** dữ liệu sau khi đã lọc, nhóm, tuỳ chỉnh cột — gồm mọi trang, không chỉ trang đang xem |
| **Lọc theo cột** (2.20) | Nhập giá trị/ID → ô tìm · chọn giá trị → dropdown · ngày giờ → chọn khoảng ngày (chỉ `dd/mm/yyyy`, không chọn giờ) · số/tiền/% → 2 ô Từ – Đến. Cách trình bày trên innvie: § Bộ lọc nâng cao |
| **Cột action** (SC-07) | Tối đa **2** icon hiện thẳng trên hàng, còn lại gom vào `⋯` (MoreMenu). Chỉ hiện action **dùng được** theo trạng thái + quyền — không hiện rồi vô hiệu. Xoá/Huỷ luôn nằm trong `⋯`; chỉ có 1 action phụ thì hiện thẳng, không dùng `⋯`. Nút icon phải có nhãn truy cập |
| **Sửa trong ô** | Theo § Sửa trong bảng: bảng danh sách click-to-edit, lưu từng ô; bảng dòng hàng trong form luôn là input, lưu cùng form. Ô đang sửa được thì click ô **không** mở chi tiết |
| **Mở chi tiết** (SC-07) | Click vùng thông tin của hàng (tên, mã, người phụ trách…) → mở chi tiết. Click vùng action **không** mở chi tiết |

### Bổ sung từ code (nằm ở trang của từng section)

Component **có trong code `@astryxdesign/core` nhưng thiếu trong thư viện Figma**. Tôi dựng lại từ
mã nguồn GitHub, **không phải bản chính thức** của Meta/Figma Librarian. Khi thư viện chính thức có
component cùng tên, chuyển sang bản chính thức.

**Vị trí (cập nhật 28/09/2026).** Các component thật sự mới đã chuyển về trang của section, trong
khung riêng có mục *Master Components · bổ sung từ code*: `Stepper`, `Stepper / Step` → Navigation ·
`AlertDialog` (trong khung Dialog), `BottomSheet` → Overlay · `AvatarGroup`, `Timer` → Content ·
`ComplexSelector` (+ `ComplexSelector / .Popover`, `.Popover Content`) → Form Controls.

**Đã bỏ bản trùng (28/09/2026).** Các component sau **thư viện đã có sẵn** (dạng component đơn,
không phải set, nên lượt so khớp đầu bị sót). Bản tôi dựng đã **xoá**, dùng bản gốc:
`Tooltip`, `HoverCard`, `Popover`, `Lightbox` (trang Overlay) · `Blockquote` (Content) ·
`Carousel` (Container) · `Navigation / TopNav`, `Navigation / TopNavHeading`,
`Navigation / .TopNavMegaMenuFeaturedCard` (Navigation). Cũng đã xoá `NavHeadingMenu`,
`NavHeadingMenu / Item` (chỉ dùng trong TopNavHeading của tôi).
Còn giữ vì đang có instance:

* `ComplexSelector / .Popover` + `ComplexSelector / .Popover Content` (đổi tên từ Popover của tôi,
  nằm cạnh ComplexSelector): là popup bên trong ComplexSelector. Vẽ popover ở màn thì dùng `Popover` gốc.
* `NavIcon` và `HoverCard / .Content · Văn bản`: trang `DS · Bổ sung từ code` đã bị xoá; quét
  01/10/2026 không còn trong file, đã gỡ khỏi `figma-library-keys.json`.

**`Stepper / Step`** (key `177748f2…`, dựng từ `packages/core/src/Stepper`, bản 0.6.3):

* Biến thể: Orientation = Horizontal / Vertical · Progress = Completed / Current / Upcoming / Disabled · Indicator = Auto / Number.
* Thuộc tính: `Label`, `Description`, `Has Description`, `Optional`.
* Hình dạng theo code (chế độ `separated`, `balanced`):
  - Thanh 4px, nền `Border/Default`, tô `Core/Accent` khi đã đạt.
  - Chỉ báo 16px: Completed là tròn đặc có check; Current là vòng 2px có chấm; Upcoming là số trên `Core/Background Muted`; Disabled là số mờ 50%.
  - Nhãn `Text/Body`, bước Current đậm 600. Mô tả `Text/Supporting`, line-height 16px, thụt 24px.
* Chữ số trong chỉ báo **không có thuộc tính**: phải `setText` lớp `Số bước` theo thứ tự bước.

**`Stepper`** (key `b681c7fa…`): Orientation = Horizontal (880px) / Vertical (280px), mỗi biến thể ghép sẵn 4 Step. Cần số bước khác thì đặt trực tiếp các `Stepper / Step` vào frame auto-layout (ngang: `layoutGrow: 1` mỗi bước).

**`AlertDialog`** (key `1fadff07…`, dựng từ `packages/core/src/AlertDialog`): hộp xác nhận hành động phá huỷ hoặc không hoàn tác được.

* Biến thể: Action = Destructive / Primary · Layout = Default (400px) / Stacked (màn ≤ 640px).
* Thuộc tính `Title`, `Description`. Nhãn hai nút sửa trực tiếp vì đã mở nested instance.
* Theo code:
  - Nền `Core/Background Surface`, `Radius/Container`, `Elevation/High`.
  - Nội dung đệm 16px: `Heading/Heading 2` + `Text/Body` màu secondary.
  - Chân đệm 16px, `[Hủy]` Ghost rồi `[Hành động]` căn phải. Ở dạng Stacked: full-width, **hành động ở trên**.
* Hành vi không vẽ được: không đóng khi bấm ra ngoài; Esc = Hủy; focus mặc định ở Hủy.
* **Dùng thay cho Dialog thường** mỗi khi xác nhận xoá, huỷ lệnh, hoặc hành động không hoàn tác (xem Do's).

**`AvatarGroup`** (key `a5863cbf…`, dựng từ `packages/core/src/AvatarGroup`): nhiều người liên quan hiển thị gọn trên một dòng.

* Biến thể Size = xsm 20 / sm 24 / md 36 / lg 48.
* Thuộc tính `Has Overflow`, `Overflow Count` ("+3"). Đổi chữ tắt trên từng Avatar vì đã mở nested instance.
* Theo code:
  - Mỗi avatar nằm trong vòng 2px `Core/Background Surface`.
  - Chồng nhau 25% cỡ avatar, avatar sau đè avatar trước.
  - Ô "+N" cao bằng cỡ + 4px, chữ `Text/Secondary` đậm 500.
* Lệch: nền ô "+N" dùng `Core/Background Muted` thay cho surface + tint neutral.
* Khi dùng trong bảng hoặc thẻ: tối đa 3–4 avatar + "+N". Luôn có tên đầy đủ ở tooltip hoặc danh sách chi tiết.

**Indicator** (code `packages/core/src/Indicator`) **không cần dựng riêng**. Đây là phần hình
trang trí của control chọn (ô checkbox, vòng radio, dấu tick trong menu), code cũng ẩn khỏi trang
tổng quan. Figma đã có nó bên trong `Checkbox`, `Radio`, `DropdownMenuCheckboxItem`, `DropdownMenuRadioItem`.

**`ComplexSelector`** (key `8298b254…`, dựng từ `packages/core/src/ComplexSelector`): khi cần một **bộ chọn riêng trong popup** (lưới ca, ma trận, khoảng thời gian) thay vì danh sách.

* Biến thể: Variant = Input / Ghost · State = Closed / Open.
* Input dùng instance `Selector` thật. Ghost là chữ `Text/Label` + chevron, không viền, nền `Core/Overlay Pressed` khi mở.
* Popup là `ComplexSelector / .Popover` (nội bộ), mở phía dưới, căn trái, cách 4px.
* Chỉ chọn trong danh sách thì dùng `Selector`.

**`Timer`** (key `ace5e29c…`, dựng từ `packages/core/src/Timer`): thời lượng **đang chạy** (thời gian dừng máy, thời gian sửa, thời gian chờ). Khác `Timestamp`, là **mốc thời điểm**.

* Biến thể: Format = Elapsed / Clock · Color = Secondary (mặc định) / Primary / Accent / Disabled.
* Chữ `Text/Supporting`. Sửa giá trị trực tiếp trên instance.
* Định dạng cố định theo code, không tự chế:
  - Elapsed: `45s` · `12m 05s` · `3h 07m` (bỏ giây từ 1 giờ).
  - Clock: `12:05` · `3:07:12`.
* Code **không dịch** h/m/s (gắn cứng trong `Timer.tsx`). **Chấp nhận** `12m 05s` trên giao diện tiếng Việt (chốt 01/10/2026); cần dạng trung tính thì chọn Format = Clock.

**`BottomSheet`** (key `1ce08702…`): bảng trượt từ đáy, **chỉ cho mobile**.

* Biến thể Height = Hug / Capped (62%) / Tall (92%), mẫu trên màn 390×844.
* Theo code: nền surface, viền 1px `Border/Default` trên và hai bên, bo 12px hai góc trên, `Elevation/High`, thanh kéo 24px có vạch 36×4px.
* Nội dung qua `Content` (instance swap). Đặt vào màn thì thêm scrim bằng `figma.overlay`.
* Mẫu nội dung có sẵn (trang Overlay, trong khung BottomSheet), rộng 390px, swap vào `Content`:
  - `BottomSheet / .Content · Hành động` (key `7735af84…`): danh sách `DropdownMenuItem`, cho DropdownMenu/MoreMenu `presentation="bottom-sheet"`.
  - `BottomSheet / .Content · Chọn một` (key `ce12a283…`): danh sách `RadioListItem`, cho Selector trên mobile.
  - `BottomSheet / .Content · Chọn nhiều` (key `646bb320…`): danh sách `CheckboxListItem`, cho MultiSelector trên mobile.
  - `BottomSheet / .Content · Mẫu` (key `acf7ddb8…`): tiêu đề Heading 2 + đoạn mô tả, đệm 16px.
* Đây là thành phần mobile đầu tiên trong hệ thống. Vẽ màn mobile vẫn phải ghi "chưa có chuẩn trong design.md" cho phần bố cục (xem Known Gaps).

**Đã đủ so với code** `@astryxdesign/core` 0.6.3 (27/09/2026): mọi component có hình trong code
đều đã có trong Figma, hoặc sẵn trong thư viện, hoặc bổ sung (nằm ở trang của section, mục *Master Components · bổ sung từ code*).
Phần còn lại là tiện ích bố cục hoặc logic, không có hình. `packages/lab` (component thử nghiệm)
chưa được đối chiếu. Stack/HStack/VStack/Grid/Center/Layer/ScrollableArea/VisuallyHidden
là tiện ích bố cục hoặc logic, không cần có trong Figma.

### Chat

ChatMessage / ChatMessageBubble (assistant/user; filled/ghost) · ChatMessageMetadata (sending→read/error) · ChatComposer (empty/typing/streaming) + ChatComposerInput, ChatComposerDrawer, ChatComposerTokenElement (@mention, /command, file) · ChatSendButton (send/stop) · ChatDictationButton · ChatToolCalls (pending/running/success/error) · ChatSystemMessage · ChatLayoutScrollButton.

## Components - innvie logis (không có trong thư viện Astryx)

Đối chiếu với `web-common-rules.md`, 5 mẫu dưới đây **không có** trong thư viện Figma/code
Astryx — ghép từ các component có sẵn. **Cả 5 đã dựng thành Figma component thật** (quyết định 29/09/2026,
xem từng mục). Mẫu ghép mới sau này (nếu có): khi vẽ, dùng đúng instance
của từng component thành phần, **không tạo Figma component mới** cho cả khối. Nếu sau này phát hiện
Astryx code (`@astryxdesign/core`) đã có sẵn khối tương đương mà chưa vẽ trong Figma, ưu tiên dùng
đúng cái đó.

### Quy ước chung của component dự án

> Rút từ 4 spec dưới (NC = Notification Center, BL = Bộ lọc nâng cao, TC = Tuỳ chỉnh cột, AL = Activity
> Log). Component mới theo các quy ước này để cả họ nhất quán; spec riêng khác quy ước thì spec riêng
> thắng và phải ghi lý do. Quy ước mới lặp lại ở ≥ 2 spec → đưa lên đây.

* **Cấu trúc họ:** `<Tên> / Trigger` (nút mở; NC gọi `Bell`) → phần tử lặp (`Item`, `Entry`) →
  `Body` (Platform × trạng thái dữ liệu) → `Panel` (vỏ). Bảng spec: Component | Key | Biến thể /
  thuộc tính | Dựng từ. (NC, AL)
* **Nút mở:** `Button` Ghost Icon Only; Desktop MD + `Tooltip`, Mobile LG trong vùng chạm 44; State
  Rest / Hover / Open; có nhãn truy cập. Trên header màn chi tiết: ngoài cùng phải, sau các nút hành
  động. (NC, AL)
* **Vỏ:** Desktop `Popover` neo dưới nút, căn phải; bề rộng theo spec từng khối (NC 380px, AL 400px),
  chưa có chuẩn chung. Mobile: chưa có quy tắc chung chọn vỏ — mỗi spec tự chốt kèm lý do (NC màn
  riêng; AL, BL `BottomSheet`); component mới thì hỏi user. Luôn ghi "Bố cục mobile chưa có chuẩn
  trong design.md — theo spec M…". Chỉ Desktop thì nói rõ (TC).
* **Trạng thái dữ liệu:** Rỗng = `EmptyState` tiêu đề + một câu hướng dẫn · Đang tải = `Skeleton`
  theo hình phần tử (bảng: giữ header) · **Lỗi mạng = `EmptyState`** icon `wifi-off` + "Không tải
  được …" + "Kiểm tra kết nối mạng rồi thử lại." + Button Secondary "Thử lại" (MD desktop, LG
  mobile), không dùng Banner. Tải thêm: 20 mục/lần, cuộn tới cuối tự tải (§ Phân trang). (NC, AL, BL)
* **Chữ dài** (kiểm ở bề rộng desktop của khối và 320px): mã định danh `Heading/Heading 4`, cùng vị
  trí, **không bao giờ cắt** · thời gian (`Timestamp`) không co · tiêu đề / tên / meta / nhãn chip 1
  dòng cắt "…" (NC cho Title 2 dòng) · nội dung người dùng cần để hành động (lý do, hành động) xuống
  dòng đủ, không cắt · phần đếm `+n` không cắt. (NC, AL, BL, TC)
* **Tông và màu:** tông theo *Ánh xạ trạng thái nghiệp vụ*, luôn kèm chữ/icon. Badge đếm/chấm dùng
  **Info** (Error không đạt AA). Chữ secondary trên nền muted chỉ ~4,2:1 → chấp nhận cho thông tin
  phụ, không đặt nội dung quan trọng trên nền muted. Nền nhấn `{colors.accent-muted}` trùng
  surface ở Dark → panel dùng `Surface/Popover`. (NC, AL)
* **Tương tác:** không đặt nút hành động nghiệp vụ (Duyệt/Từ chối) trong danh sách; bấm dòng → mở
  bản ghi (NC). Mốc lịch sử chỉ để đọc (AL).
* **Khác nguồn nghiệp vụ (SC):** mở spec bằng khối "> **Khác SC-xx gốc — chờ người phụ trách xác
  nhận:** …" kèm lý do, và thêm một mục KG ở Known Gaps. (NC, BL, TC)
* **Figma:** trang Overlay, khung `<Tên> · innvie` + khung `Trạng thái · instances` có mọi trạng
  thái, ví dụ trong màn, *Chữ dài · kiểm tra*. Nội dung khác nhau theo biến thể (icon theo Tone,
  nhãn lượt) → để sẵn trong từng biến thể + expose, không dùng thuộc tính TEXT/INSTANCE_SWAP. (NC, AL)

### Notification Center (theo SC-02, đã điều chỉnh 29/09/2026)

> **Khác SC-02 gốc — đã duyệt 01/10/2026:** bỏ mẫu một câu
> `[Module] · [Feature] — [Mã] vừa được/bị [hành động] bởi [Người]`, chuyển sang 3 dòng (hành động ·
> mã in đậm · người + module); chia thông báo theo việc người nhận phải làm; badge chuông đếm **việc
> cần xử lý**; không đưa lý do từ chối và hạn xử lý vào thông báo; mobile là màn riêng; nền chưa đọc
> dùng `{colors.accent-muted}` thay "nền xanh nhạt".

**Component Figma** (trang Overlay, khung `NotificationCenter · innvie`, node `5142:2017`; khung
`Trạng thái · instances` bày đủ mọi trạng thái và phần *Chữ dài · kiểm tra*). Bên trong dùng
instance thật của thư viện, không vẽ lại control:

| Component | Key | Biến thể / thuộc tính | Dựng từ |
| --- | --- | --- | --- |
| `Notification Center / Bell` | `1ae34e12…` | Count = 0 / 3 / 9+ · Open = No / Yes | `Button` Ghost MD Icon Only + `icon/bell`; `Badge` **Info** Pill (Info đạt AA, Error không đạt) |
| `Notification Center / Item` | `c0017367…` | Status = Unread / Read / Resolved · State = Rest / Hover · `Title`, `Code`, `Meta` (TEXT) · `Has Code` | `Badge` Info Dot (chấm chưa đọc) + Title + Code Row (mã + `Resolved Tag` `Badge` Neutral "Đã xử lý" căn phải cùng dòng, chỉ khi Resolved) + Meta Row (Meta + `Timestamp`) |
| `Notification Center / Body` | `373bfce7…` | Platform = Desktop 380 / Mobile 390 · State = Cần xử lý / Tất cả / Đã đọc hết / Rỗng / Đang tải / Lỗi mạng | Header ("Thông báo" + Ghost "Đánh dấu là đã đọc"; Mobile thêm nút ← ) → `Tabs / TabList` ("Cần xử lý" + `Badge` Neutral đếm, "Tất cả") → nhóm ngày → Item · `EmptyState` (rỗng, lỗi mạng) · `Skeleton` |
| `Notification Center / Panel` | `bd22fa41…` | Platform = Desktop / Mobile | Desktop: `Popover` gốc (tắt nút đóng, ẩn tiêu đề, padding 0) chứa Body. Mobile: **màn riêng 390×844** chứa Body Mobile |

**1. Ba nhóm thông báo** — mỗi hành động của feature phải gán vào đúng một nhóm (thêm hành động mới
chỉ cần gán nhóm, không đổi giao diện):

| Nhóm | Hành động | Người nhận cần | Hiển thị |
| --- | --- | --- | --- |
| **Cần xử lý** | Chờ duyệt, chờ ký biên bản, chờ xác nhận… | Làm một việc | Tab "Cần xử lý", được đếm trên chuông |
| **Kết quả việc của tôi** | Đã duyệt, bị từ chối, bị thu hồi | Biết kết quả | Tab "Tất cả" |
| **Để biết** | Tạo mới, cập nhật do người khác làm | Nắm thông tin | Tab "Tất cả", ưu tiên thấp |

**2. Nội dung 3 dòng** (Item):

1. **Title** — việc gì + tên feature, hành động đứng đầu; việc cần xử lý mở đầu "Chờ bạn…".
   Text/Label (chưa đọc) / Text/Body (đã đọc).
2. **Code** — mã định danh, `Heading/Heading 4` (Inter 700) để nổi khi lướt, luôn cùng một vị trí.
   Chưa có mã: tắt `Has Code`, Title ghi "một [tên feature]".
3. **Meta** — `[Người] · [Module]` (Text/Supporting, secondary) + thời gian bên phải. **Không lặp
   động từ đã có ở Title** (duyệt, từ chối, thu hồi, tạo). Riêng việc "Chờ…" giữ động từ của người gửi
   ("gửi", "lập") vì Title nói về việc của người nhận.
   **Không** ghi lý do từ chối (xem trong bản ghi). **Không** có hạn xử lý hay "quá hạn" trong thông báo.

Việc đã được giải quyết (`Status=Resolved`): thêm Badge Neutral `Đã xử lý` **cùng dòng với mã, căn phải**,
nên item không cao thêm và mã, dòng Meta giữ nguyên vị trí như các thông báo khác. Bản ghi không có mã
(`Has Code` tắt) thì dòng này chỉ còn tag, vẫn căn phải.

| Hành động | Title | Code | Meta |
| --- | --- | --- | --- |
| Chờ duyệt | Chờ bạn duyệt Đơn mua HHDV | DMH-2026-00123 | Trần Minh Khoa gửi · Xưởng |
| Chờ ký biên bản | Chờ bạn ký biên bản Phiếu nhập kho | PNK-2026-00045 | Lê Quốc Huy lập · Xưởng |
| Đã duyệt | Đơn mua HHDV đã được duyệt | DMH-2026-00118 | Nguyễn Thị Lan · Xưởng |
| Bị từ chối | Phiếu nhập kho bị từ chối | PNK-2026-00040 | Phạm Đức Anh · Xưởng |
| Thu hồi | Đơn mua HHDV đã bị thu hồi | DMH-2026-00110 | Trần Minh Khoa · Xưởng |
| Tạo mới | Có Lệnh điều xe mới | LĐX-2026-00077 | Hoàng Văn Nam · Điều vận |

Module (Xưởng / Nhân sự / Điều vận…) chỉ là thông tin phụ ở Meta, không tô màu riêng.

**3. Gộp tin cùng bản ghi**

* **Khoá gộp** = cùng mã bản ghi + cùng người nhận + **chưa đọc**. Chỉ giữ **một dòng** cho bản ghi đó.
* Dòng giữ lại hiển thị **sự kiện mới nhất** (Title, Meta, thời gian theo sự kiện mới nhất), đưa lên
  đầu danh sách, và thêm cuối Meta `· +N cập nhật khác` (N = số sự kiện cũ bị gộp).
  Ví dụ: 09:05 "Đơn mua HHDV DMH-2026-00118 bị từ chối" rồi 09:40 "…được gửi lại" rồi 10:12 "…đã được
  duyệt" → một dòng "Đơn mua HHDV đã được duyệt · DMH-2026-00118 · Nguyễn Thị Lan · Xưởng
  · +2 cập nhật khác · 10:12".
* **Không gộp** khi: tin cũ đã đọc (tin mới thành dòng mới); khác nhóm (việc Cần xử lý không bị gộp
  vào tin Để biết và ngược lại); hoặc hai việc Cần xử lý khác nhau trên cùng bản ghi (vd chờ duyệt và
  chờ ký biên bản là 2 việc, 2 dòng).
* Badge chuông và số trên tab đếm **dòng sau khi gộp**, không đếm từng sự kiện.
* Click dòng gộp → đánh dấu đã đọc cả nhóm + mở bản ghi; lịch sử chi tiết xem ở Activity Log của bản ghi
  (không mở rộng danh sách con trong panel).

**4. Hành vi**

* Mở panel: tab **Cần xử lý** khi còn việc, không còn thì **Tất cả**. Trong tab, nhóm theo ngày:
  Hôm nay / Hôm qua / Trước đó.
* Badge chuông = số việc **Cần xử lý** chưa giải quyết (tối đa "9+", ẩn khi 0). Nhãn truy cập:
  "Thông báo, N việc cần xử lý".
* Việc "Chờ…" đã được giải quyết (bởi mình hay người khác) → `Status=Resolved` (chữ mờ + "Đã xử lý"),
  rời tab Cần xử lý, badge giảm.
* Click một thông báo → đánh dấu đã đọc + mở bản ghi. **Không** đặt nút Duyệt/Từ chối trong danh sách.
* "Đánh dấu là đã đọc" chỉ hiện khi còn tin chưa đọc; không làm mất việc Cần xử lý.
* Tải thêm: 20 dòng mỗi lần, cuộn tới cuối tự tải tiếp (xem § Phân trang danh sách).
* Kênh khác (nếu hệ thống hỗ trợ): Toast khi có việc Cần xử lý mới lúc đang mở ứng dụng. Tin "Để
  biết" chỉ ở chuông.

**5. Hiển thị**

* **Desktop:** Popover 380px neo dưới chuông, căn phải.
* **Mobile: màn riêng** (bấm chuông → điều hướng sang màn "Thông báo", nút ← quay lại), không dùng
  BottomSheet: danh sách dài cần cuộn cả màn và quay lại được bằng nút back của hệ điều hành. Header:
  ← + "Thông báo" + Ghost LG "Đánh dấu là đã đọc"; Tabs size lg; cả dòng Item bấm được (cao ≥ 64px).
  Bố cục mobile chưa có chuẩn trong design.md — theo spec M2, chưa có node Figma.
* **Nền chưa đọc = `{colors.accent-muted}`** + chấm Badge Info + Title 500 (không chỉ dựa vào màu).
  Đã đọc: nền `{colors.surface-popover}`. Ở Dark, accent-muted trùng background-surface nên panel phải
  dùng `Surface/Popover`.
* Thời gian — **quy tắc riêng cho khối này, khác Relative Timestamp chung ở mục Ngày giờ**: hôm nay
  cách ≤ 5 phút → "Bây giờ"; > 5 phút → `hh:mm`; từ hôm qua → "X ngày trước".
* **Lỗi mạng** (chốt 29/09/2026, bỏ phương án Banner): `EmptyState` giữa panel — icon `wifi-off` +
  "Không tải được thông báo" + "Kiểm tra kết nối mạng rồi thử lại." + Button Secondary "Thử lại"
  (MD desktop, LG mobile). Giữ tab để người dùng vẫn chuyển được.
* **Chữ dài** (đã kiểm ở 380px và 320px):

  | Phần | Quy tắc |
  | --- | --- |
  | Title | Tối đa 2 dòng, cắt cuối bằng "…" |
  | Code | Không bao giờ cắt |
  | Meta | 1 dòng, cắt cuối bằng "…" (tên người và module dài) |
  | Timestamp | Không co, luôn hiện đủ |
  | Header mobile | Tiêu đề co lại, nút giữ nguyên (đã kiểm màn 320px) |

* Tương phản: chữ secondary (Meta, thời gian) trên nền chưa đọc chỉ ~4,2:1. Chấp nhận vì là thông tin phụ.
* Đổi trạng thái: chọn lớp `Body` trong Panel → `State`.
* **Cần nghiệp vụ xác nhận:** danh sách hành động "Chờ…" của từng feature.

### Bộ lọc nâng cao (theo SC-05 + 2.20, phương án thanh chip — 29/09/2026)

> **Khác SC-05 gốc — đã duyệt 01/10/2026:** không dùng Drawer. Bộ lọc là **thanh chip
> `PowerSearch`** ngay trên bảng: điều kiện luôn hiển thị, sửa từng điều kiện trong popover nhỏ, bảng
> cập nhật sau mỗi điều kiện được xác nhận. Lý do: drawer che bảng, giấu điều kiện sau khi đóng, bắt mở
> lại cả khối để sửa một điều kiện; thư viện đã có `PowerSearch` làm đúng việc này.

> **Thanh công cụ 2 hàng (chốt 12/10/2026, thay `PowerSearch / Trigger` 1 ô):** ô tìm và nút Bộ lọc tách
> riêng ở hàng 1, chip điều kiện xuống hàng 2. Lý do: nhóm điều khiển (tìm, lọc, cột, nhóm) luôn đứng
> yên một chỗ dù có bao nhiêu chip; chip dài không đẩy nút sang dòng khác. Popover chọn cột / sửa giá
> trị vẫn dùng của thư viện.

**Không tạo component vỏ** — dùng `PowerSearch / Popover` của thư viện
(Form Controls; hướng dẫn: `components.md` § Power Search). Chỉ thêm nội dung sửa giá trị của dự án.
Figma: trang Overlay, khung `BoLocNangCao · innvie` (node `5176:9303`), khung `Trạng thái · instances` có 3 cảnh
trên bảng (chọn cột / sửa điều kiện / không có kết quả), 3 màn mobile và *Chữ dài · kiểm tra*.

| Phần | Dùng | Ghi chú |
| --- | --- | --- |
| Thanh công cụ — hàng 1 | Ô tìm (`TextInput` có icon tìm, cao 32, giãn hết) · `Button` Secondary *"Bộ lọc"* + `Badge` Neutral đếm số điều kiện đang áp · `Button` Ghost có icon + chữ *"Tuỳ chỉnh cột"*, *"Nhóm"* | Cách nhau 8px. Placeholder nêu đúng các trường tìm được (vd *"Tìm mã Lệnh, biển số, lái xe…"*). Bấm *Bộ lọc* → `PowerSearch / Popover` Mode = Fields |
| Thanh công cụ — hàng 2 | Chip điều kiện · *"Xoá tất cả"* (Button Ghost SM) · số kết quả căn phải | Cách hàng 1 8px. Chưa có điều kiện: hàng 2 chỉ còn số kết quả |
| Chip điều kiện | `Token` SM (mobile MD) trong slot `Filters`, `Removable` bật | `Label` = `[Cột]: [giá trị 1]`, phần `+n` đặt trong `End Content` của Token (để không bị cắt); rộng tối đa 260px, nhãn 1 dòng cắt "…"; khoảng: `Ngày tạo: 01/09 – 30/09/2026`, `Tổng tiền: 1,000,000 – 10,000,000 đ`. Bấm chip → Value Editor của điều kiện đó; × trên chip → xoá điều kiện |
| Chọn cột | `PowerSearch / Popover` Mode = Fields | Danh sách cột được phép lọc (định nghĩa trong UC), thứ tự trái → phải của bảng kể cả cột ẩn, icon theo loại dữ liệu |
| Sửa giá trị | `PowerSearch / Popover` Mode = Value Editor, slot `Content` = **`Bộ lọc nâng cao / .Value Editor`** | Xem bảng dưới |
| Số kết quả | Chữ `{typography.supporting}`, màu `{colors.text-secondary}`, cuối hàng 2 | "128 kết quả" — là tổng duy nhất của danh sách (phân trang không lặp lại) |
| Không có kết quả | Bảng hiện `EmptyState` "Không có kết quả phù hợp" / "Thử bỏ bớt điều kiện lọc." + Button Secondary "Xoá bộ lọc" | **Không** có nút Tạo mới (tách khỏi "chưa có dữ liệu", xem Known Gaps 2.12) |

**`Bộ lọc nâng cao / .Value Editor`** (key `a4b66118…`, 8 biến thể Platform × Type; nội dung đặt vào Value Editor) — theo bố cục của
thư viện: [Cột] [Toán tử] [Giá trị] → chân `[Huỷ]` Secondary SM · `[Áp dụng]` Primary SM.

| Type | Khi nào (2.20) | Toán tử | Giá trị |
| --- | --- | --- | --- |
| Chọn một | Giá trị chọn, chỉ một | là / không là | `Selector` (luôn có "Không có") |
| Chọn nhiều | Giá trị chọn, nhiều | là một trong | `Selector / MultiSelector` (luôn có "Không có") |
| Khoảng ngày | Ngày/giờ | trong khoảng | `DateRangeInput`, **chỉ chọn ngày** |
| Khoảng số | Số / tiền / % | trong khoảng | 2 `NumberInput` "Từ" – "Đến" (suffix `đ` cho tiền) |

* "Áp dụng" xác nhận **một** điều kiện (thành chip), bảng tải lại ngay, về trang 1. Không có nút Áp dụng
  chung. "Xoá tất cả" xoá mọi chip, không xoá từ khoá trong ô tìm.
* Gõ vào ô tìm = tìm theo từ khoá (mã, tên…), không tạo chip.
* **Mobile** (bố cục chưa có chuẩn trong design.md — theo spec M2): ô tìm full-width + icon button Bộ lọc
  (kèm số điều kiện); chip xuống dưới ô tìm, cuộn ngang; bấm Bộ lọc hoặc chip → `BottomSheet` chứa Fields / Value Editor (bản Mobile: control
  LG xếp dọc, nút full-width, "Áp dụng" ở trên).
* **Chữ dài:** chip giữ 1 dòng — giá trị dài cắt "…", phần `+n` không cắt; nhiều chip thì thanh tự xuống
  dòng (desktop) / cuộn ngang (mobile).
* **Đang tải:** bảng giữ header, hàng thay bằng `Skeleton`; chip vẫn hiện.

### Tuỳ chỉnh cột (theo SC-06, phương án chỉnh trên bảng — 29/09/2026)

> **Khác SC-06 gốc — đã duyệt 01/10/2026:** không có panel. Ẩn / ghim / sắp xếp làm ngay
> trên **tiêu đề cột**; đổi thứ tự bằng **kéo tiêu đề cột**; bật/tắt cột ở nút **Tuỳ chỉnh cột** (Button Ghost có icon + chữ, chốt 12/10/2026)
> ở hàng 1 thanh công cụ, sau nút Bộ lọc (tham khảo column picker của Jira). Người dùng thấy kết quả ngay trên
> bảng, không có "Áp dụng"; "Đặt lại mặc định" nằm ở chân popover. Gọi là *tuỳ chỉnh* chứ không phải
> *cột ẩn* vì đây là cấu hình riêng của từng người dùng.

Figma: trang Overlay, khung `TuyChinhCot · innvie` (node `5177:7634`), khung `Trạng thái · instances` có 3 cảnh
trên bảng (menu ⋯ mở / đang kéo tiêu đề / popover Tuỳ chỉnh cột) và *Chữ dài · kiểm tra*. Ba cảnh của
Bộ lọc nâng cao cũng đặt nút này cạnh thanh lọc.

Mỗi UC tự ghi rõ: cột nào lọc được và loại dữ liệu của cột (quyết định Value Editor), cột nào bị khoá
(không ẩn, không kéo được).

Code đã có: plugin `columnSettings` của Table (ẩn/hiện, thứ tự, `isAlwaysVisible` = cột khoá, nhóm cột) và
`stickyColumns` (ghim). Figma thêm phần tương tác trên tiêu đề. **Chỉ Desktop** (mobile: bảng → `List`).

| Component | Key | Biến thể | Dựng từ |
| --- | --- | --- | --- |
| `Tuỳ chỉnh cột / Header Cell` | `8fab478b…` | State = Rest / Hover / Menu Open / Dragging · Align = Left / Right · `TableHeaderCell` exposed | `TableHeaderCell` + tay nắm `icon/grip-vertical` (hiện khi hover, trái) + `MoreMenu` Ghost SM (hiện khi hover/mở, phải). Dragging = cột nguồn đang kéo: nền `{colors.overlay-hover}`, hiện tay nắm + ⋯. Cột số/tiền chọn **Align = Right** (nhãn căn phải, dài thì "…"); không bật `Align Right` của `TableHeaderCell` trực tiếp |
| `Tuỳ chỉnh cột / Drop Indicator` | — | — | Vạch 2px `{colors.accent}` + chấm 8px ở đầu trên, cao hết bảng (tiêu đề + thân); đặt ở mép trái cột đích |
| `Tuỳ chỉnh cột / Column Menu` | `145c8a4a…` | Locked = No / Yes · Pinned = No / Yes | Bề mặt như menu của `MoreMenu` + `DropdownMenu / DropdownMenuItem`: Sắp xếp tăng dần · Sắp xếp giảm dần · Ghim bên trái / Bỏ ghim · Ẩn cột (cột khoá: vô hiệu + "Cột bắt buộc") |
| `Tuỳ chỉnh cột / Column Picker` | `93b58478…` | Part = Trigger / Popover · State (Trigger) = Rest / Hover / Open | Trigger: icon button — `Button` Secondary MD Icon Only (32, cao bằng thanh lọc) + `icon/columns-3-cog`, nhãn truy cập "Tuỳ chỉnh cột", **luôn hiện**; Hover = `Tooltip` "Tuỳ chỉnh cột" dưới nút, căn phải; Open = Pressed. Popover 280px neo dưới nút, căn phải, cách 4px: ô tìm cột + danh sách `CheckboxListItem` mọi cột theo thứ tự bảng (cột khoá: đã chọn + vô hiệu) + chân: Ghost "Đặt lại mặc định" · "n/m cột" (`Text/Supporting`, `Text/Secondary`; số cột đang hiện / tổng) |

* **Kéo cột** (tham khảo Jira, góp ý 01/10/2026): chỉ bắt đầu từ tay nắm trên tiêu đề. Bản xem trước chỉ là **khung
  hình cột** (rộng bằng cột, cao hết bảng, không có tiêu đề hay dữ liệu) đi theo con trỏ, chỉ trượt ngang:
  viền 2px `{colors.accent}`, nền `{colors.accent-muted}` 50%, không bóng. Cột nguồn giữ nguyên chỗ và nội dung tới khi
  thả, cả cột (tiêu đề + ô thân) tô nền `{colors.overlay-hover}` để biết đang kéo cột nào. `Drop Indicator` ở mép trái cột đích, cao hết bảng. Cột khác không dịch tới khi thả. Bàn phím: focus tay nắm → Space → ←/→ → Space / Esc.
* Cấu hình lưu theo từng người dùng (SC-06).
* **Chữ dài:** nhãn tiêu đề 1 dòng "…" (khi hover, tay nắm và ⋯ chiếm chỗ, nhãn co tiếp); tên cột trong
  popover xuống dòng.

### Activity Log (theo SC-08, component thật 29/09/2026)

Lịch sử thay đổi trạng thái và hành động trên **một bản ghi**, mở từ màn chi tiết. Nguồn:
`web-common-rules.md` SC-08. Code Astryx không có Timeline/Activity nên dựng riêng; cấu trúc
mỗi mốc theo `TimelineSection` của mẫu P7 (Avatar → tên đậm + nội dung → thời gian).

**Nút mở** = `Activity Log / Trigger`: góc trên phải header màn chi tiết/drawer, **ngoài cùng bên phải**,
sau các nút hành động (vd `[Từ chối] [Phê duyệt] [🕐]`). Nhãn truy cập "Lịch sử hoạt động". Khung
`Trạng thái · instances` có ví dụ *Trong màn chi tiết* cho Desktop (header P7 + panel neo dưới nút) và
Mobile (M4 + scrim + BottomSheet).

**Component Figma** (trang Overlay, khung `ActivityLog · innvie`, node `5160:3295`; khung `Trạng thái ·
instances` bày mọi trạng thái Desktop/Mobile, BottomSheet kéo lên Tall và phần *Chữ dài · kiểm tra*).

| Component | Key | Biến thể / thuộc tính | Dựng từ |
| --- | --- | --- | --- |
| `Activity Log / Trigger` | — | Platform = Desktop (MD 32) / Mobile (LG trong vùng chạm 44) · State = Rest / Hover (chỉ Desktop, có `Tooltip` "Lịch sử hoạt động") / Open (Pressed khi panel đang mở) | `Button` Ghost Icon Only + `icon/history`; `Tooltip` |
| `Activity Log / Entry` | `f4a0a7dd…` | Tone = Neutral / Success / Error · TEXT `Actor`, `Action`, `Reason` · BOOLEAN `Has Reason` · instance `Icon`, `Avatar`, `Timestamp` được expose (đổi trực tiếp) | `Avatar` chữ tắt + tên (`Heading/Heading 4`) + `Timestamp` Date Time bên phải + icon 16px + dòng hành động (`Text/Body`) + khung lý do |
| `Activity Log / Body` | `8bb34a41…` | Platform = Desktop 400 / Mobile 390 · State = Có dữ liệu / Rỗng / Đang tải / Lỗi mạng | Header "Lịch sử hoạt động" (`Heading/Heading 3`) + nút đóng (Icon Only) → danh sách Entry · `EmptyState` · `Skeleton` |
| `Activity Log / Panel` | `77e7c7d3…` | Platform = Desktop / Mobile | Desktop: `Popover` 400px neo dưới nút, căn phải. Mobile: `BottomSheet` Height=Capped, `Content` = Body Mobile |

**Nội dung (nguyên văn SC-08)** — `[feature]` điền theo từng màn (vd "kế hoạch mua dầu"):

| Hành động | Action | Icon | Tone |
| --- | --- | --- | --- |
| Tạo mới (submit) | Đã tạo mới [feature] | `icon/plus` | Neutral |
| Phê duyệt | Đã phê duyệt tạo mới [feature] | `icon/check` | Success |
| Từ chối | Đã từ chối phê duyệt [feature] + Lý do | `icon/x` | Error |
| Thu hồi | Đã huỷ tạo mới [feature] | `icon/trash-2` | Neutral |

* Icon không dùng thuộc tính INSTANCE_SWAP (giá trị mặc định dùng chung mọi Tone): mỗi Tone có icon
  mặc định (Neutral `plus`, Success `check`, Error `x`); đổi bằng cách chọn lớp `Icon` (exposed) → swap, rồi
  gán lại màu nét theo Tone nếu icon mới mất màu.
* Hành động khác: đổi `Icon`, chọn Tone theo *Ánh xạ trạng thái nghiệp vụ* (hoàn tất → Success; lỗi /
  từ chối / huỷ nghiêm trọng → Error; còn lại Neutral). Icon Neutral = `Icon/Secondary`. Luôn có chữ
  đi kèm, không chỉ màu.
* **Lý do** (chỉ khi Từ chối): khung nền `{colors.background-surface}` + viền `{colors.border-default}`,
  bo `{rounded.element}`, chữ `Lý do: [nội dung]` `Text/Body` primary. **Hiện đủ, không cắt** (khác
  Notification Center: SC-08 yêu cầu giữ lý do). Không dùng nền muted vì chữ trên đó chỉ ~4,2:1.
* **Thời gian:** `Timestamp` Date Time `dd/MM/yyyy hh:mm` (quyết định 29/09/2026; SC-08 gốc chỉ ghi ngày).
* **Thứ tự:** mới nhất trên cùng. Không nhóm theo ngày (mỗi mốc có ngày đầy đủ).
* **Không tương tác trên mốc:** không hover, không click.

**Trạng thái (Body):** Có dữ liệu · Rỗng — `EmptyState` "Chưa có hoạt động nào" / "Các thao tác trên
bản ghi này sẽ hiện ở đây." · Đang tải — `Skeleton` theo hình Entry · Lỗi mạng — `EmptyState` icon
`wifi-off` + "Không tải được lịch sử" + "Kiểm tra kết nối mạng rồi thử lại." + Button Secondary "Thử lại".
Tải thêm: 20 mốc mỗi lần, cuộn tới cuối tự tải (xem § Phân trang danh sách).

**Chữ dài:**

| Phần | Quy tắc |
| --- | --- |
| Actor (tên) | 1 dòng, cắt cuối "…" |
| Timestamp | Không co |
| Action | Xuống dòng đủ, không cắt |
| Reason | Xuống dòng đủ, không cắt |

**Mobile:** `BottomSheet` (quyết định 29/09/2026), không phải màn riêng như Notification Center — người
dùng xem lịch sử để quay lại xử lý **chính bản ghi đó**, nên giữ màn chi tiết phía sau; đúng cơ chế
Popover → bottom-sheet của Astryx và thumb zone của spec M. Mặc định Capped (62%), kéo lên Tall
(92%), cuộn bên trong; nút đóng LG trên header. Trạng thái kéo lên: dùng trực tiếp `BottomSheet`
Height=Tall + Content = Body Mobile (instance BottomSheet lồng trong Panel giữ chiều cao Capped). Bố cục mobile chưa có chuẩn trong design.md — theo spec M.


#### Phương án A + B (đã duyệt 01/10/2026)

Dựng lại từ việc người dùng cần làm, không theo hình SC-08: người tạo cần **lý do bị từ chối** để sửa; người
duyệt cần **lý do lần trước** khi phiếu được gửi lại; người xem cần biết **đang ở đâu**. Bản danh sách phẳng
ở trên (Body `State=Có dữ liệu`) giữ làm dự phòng.

| Component | Key | Biến thể / thuộc tính | Dựng từ |
| --- | --- | --- | --- |
| `Activity Log / Latest` (**A**) | `25e5dd1d…` | Platform = Desktop / Mobile × Case = Bị từ chối (Banner error) / Gửi lại sau từ chối (info) / Đã thu hồi (info) = 6 · lớp `Banner` exposed (sửa Title, Description) | `Banner` Container=section + `Button` Ghost SM "Xem lịch sử" (mở Panel): Desktop ở End Content (cuối hàng tiêu đề); Mobile ở Content Area, dưới phần chữ, thẳng lề chữ — để chữ dùng hết bề ngang |
| `Activity Log / Round` (**B**) | `4c6aa3cf…` | Result = Đang xử lý / Đã phê duyệt / Bị từ chối / Đã thu hồi · lớp chữ `Round Label` sửa trực tiếp (không dùng thuộc tính TEXT vì mặc định dùng chung mọi biến thể) · exposed `Result Badge`, `Outcome Entry`, `Older Activities` | Tiêu đề lượt (`Heading/Heading 5`, 1 dòng "…") + `Badge` → Entry kết quả → `Collapsible` "Xem n hoạt động trước" (nhãn hạ về `Text/Label` secondary) |
| `Activity Log / Body` | `8bb34a41…` | thêm State = **Theo lượt** (Desktop, Mobile) | Header → dòng "Đang chờ duyệt · đã chờ n ngày" (nền muted) → Round, lượt mới nhất trên cùng |

**Quy tắc A (Latest):**
* Đặt ngay dưới hàng meta của header màn chi tiết (P7, M4), rộng theo vùng nội dung.
* **Chỉ hiện** khi: phiếu đang bị từ chối (cho người tạo) · phiếu đã gửi lại sau khi bị từ chối (cho
  người duyệt) · phiếu đã thu hồi. Trạng thái khác → không hiện.
* Title: `[kết quả] · [người] · dd/MM/yyyy hh:mm`. Description: `Lý do: …`, **hiện đủ, không cắt**.
* Badge trạng thái trên header phải khớp Banner (vd Bị từ chối → Badge Error). Không thêm Toast/Badge khác lặp cùng thông tin.

**Quy tắc B (Round, Body Theo lượt):**
* Một lượt = từ lúc gửi tới khi có kết quả. Lượt đang xử lý hiện đủ mọi mốc, không thu gọn.
* Lượt đã kết thúc: luôn hiện mốc kết quả (lý do hiện đủ); các mốc cũ hơn nằm trong `Collapsible`, mặc định đóng.
* Dòng "Hiện tại" chỉ nêu trạng thái + thời gian chờ (không tên người duyệt — quyết định 29/09/2026), không lặp Badge vì Badge lượt đã có.
* Chữ dài: `Round Label` 1 dòng "…"; phần còn lại theo bảng *Chữ dài* ở trên.

**Chưa có chuẩn:** hành động "Gửi lại" và khái niệm "lượt" không có trong SC-08 (câu mẫu "Đã gửi lại
[feature]" là đề xuất).

Ví dụ: khung `Trạng thái · instances` → "Phương án A + B · trong màn chi tiết" (Desktop P7 + Banner +
panel theo lượt · Mobile M4 + Banner · Mobile BottomSheet theo lượt) và "Chữ dài · A + B" (752 / 320px).

### Sửa trong bảng (nhập/sửa trong ô và báo lỗi ô — 01/10/2026)

Thư viện Astryx chưa có ô bảng sửa được (`components.md` § Table chỉ có Rich Cell Content). Figma: trang
Overlay, khung `SuaTrongBang · innvie` (node `5240:9341`), khung `Trạng thái · instances` có 3 cảnh (bảng
danh sách đang sửa / lỗi ô + Tooltip / bảng dòng hàng trong form bấm Lưu có lỗi) và *Chữ dài · kiểm tra*.
**Chỉ Desktop** (mobile: bảng → `List`, sửa trong màn/BottomSheet của bản ghi).

| Component | Key | Biến thể | Dựng từ |
| --- | --- | --- | --- |
| `Sửa trong bảng / Editable Cell` | `0110de4c…` | Mode = Click: State = Rest / Hover / Editing / Saving / Error · Mode = Form: State = Rest / Focused / Error / Disabled | Ô cao 36 (Balanced), nền `Core/Background Surface`, divider dưới `Border/Default`. Rest/Hover/Saving: đệm 12/8 như `TableCell`; Hover thêm nền hover + `icon/pencil`; Saving chữ secondary + `Spinner` sm. Editing/Error/Form: `TextInput` sm (28) đệm 4, ẩn nhãn, mô tả, startIcon, statusMessage |

**Chọn kiểu theo ngữ cảnh**

| | Bảng danh sách (P1) — `Mode=Click` | Bảng dòng hàng trong form — `Mode=Form` |
| --- | --- | --- |
| Hiển thị | Ô hiện chữ; hover: nền hover + icon pencil ở cuối ô | Ô sửa được luôn là input; cột tính toán (Thành tiền…) là `TableCell` chỉ đọc |
| Mở sửa | Click ô, hoặc focus ô rồi Enter / F2. Mở ra chọn sẵn toàn bộ giá trị. Mỗi lúc chỉ 1 ô | — |
| Lưu | Từng ô: Enter / Tab / click ra ngoài → kiểm tra → lưu (State=Saving). Lưu xong không Toast. Esc → huỷ, trả giá trị cũ | Cùng nút Lưu của form. Rời trang khi còn thay đổi → confirm rời trang (Copy động) |
| Kiểm tra | Khi Enter/rời ô, theo *Nhập liệu và kiểm tra* | On Blur từng ô + On Submit mọi ô |
| Bàn phím | Tab / Shift+Tab sang ô sửa được kế tiếp; Enter lưu | Tab đi qua input theo hàng |

**Báo lỗi ô** (detached — hàng không cao lên):

* Ô lỗi: `TextInput` state=error (viền + ring error, icon `circle-x` trong ô), **ẩn statusMessage**. Câu lỗi
  trong `Tooltip` neo trên ô, hiện khi hover hoặc focus ô; `aria-describedby` trỏ tới câu lỗi.
* Câu lỗi theo *Nhập liệu và kiểm tra*, không nhắc lại tên cột khi tiêu đề cột đã rõ trừ câu bắt buộc
  ("Nhập Số lượng.").
* Bảng danh sách: giá trị sai hoặc server từ chối gắn với ô → không lưu, giữ giá trị vừa nhập, focus ở lại
  ô, Esc để bỏ. Lỗi kỹ thuật (mất mạng, 5xx) → Toast error, trả giá trị cũ.
* Bảng trong form, Submit có lỗi: `Banner` error (card) ngay trên bảng — tiêu đề "Có n ô chưa hợp lệ.",
  mô tả "Sửa các ô viền đỏ rồi lưu lại." — focus + cuộn tới ô lỗi đầu tiên, không gửi. Banner tự ẩn khi
  hết lỗi. Lỗi On Blur đơn lẻ không hiện Banner.
* Loại control trong ô: chữ → `TextInput`; số, tiền → `NumberInput` căn phải; chọn → `Selector`; ngày →
  `DateInput` — đều Size sm. Figma chỉ dựng bằng `TextInput`; ô khác thay instance cùng cỡ.
* **Chữ dài:** Rest cắt 1 dòng "…" (xem đủ ở Tooltip hoặc khi mở sửa); Editing input cuộn ngang, không
  xuống dòng. Ghi chú dài hơn 1 dòng → không sửa trong ô, mở màn/Dialog của bản ghi.
* Density: chỉ dựng Balanced (36). Bảng Compact (28) không cho sửa trong ô.

### Thanh chọn nhiều (theo Figma ERP, 12/10/2026)

> Spec, **chưa dựng Figma component**. Mẫu chuẩn: file *DELTA ERP 3.0 | CÂY DẦU | WEB*, frame
> "Tick chọn (opt1)" (`7801:9397`), thanh "Bulk action" (`7801:10228`). Ảnh: `design/_lab/refs/bulk/`.
> Dựng từ: `Checkbox` (cột đầu bảng) · `Button` Ghost (hành động trên thanh) · `Tooltip` · `MoreMenu`.

| Phần | Quy tắc |
| --- | --- |
| Khi hiện | Chọn ≥ 1 dòng; bỏ hết chọn → thanh ẩn |
| Vị trí | Nổi giữa vùng nội dung (không tính menu trái), cách đáy 32px, nằm trên bảng |
| Khung | Rộng 750px (co theo màn, chừa lề 24), cao 48, nền tối `#3C4043`, bo 8, đệm ngang 16, bóng nhẹ |
| Trái | Ô số đếm (nền `#505356`, bo 4, chữ 12) + "Đã chọn" · icon + "Chọn tất cả" |
| Giữa | Vạch đứng 24px · hành động chung: icon 20 + chữ trắng 14, cách nhau 24; rê chuột nền `#505356` bo 4 cao 28. Hành động nguy hiểm cũng chữ trắng (theo mẫu), xác nhận bằng CMP-03 |
| Phải | Vạch đứng · X (bỏ chọn, thoát chế độ chọn) |
| "Chọn tất cả" | Chọn **toàn bộ kết quả theo bộ lọc hiện tại**, không chỉ trang đang xem; số đếm hiện tổng đã chọn |
| > 3 hành động | 3 hành động đầu trên thanh, phần còn lại gom vào `MoreMenu` (⋯) |
| Bảng | Dòng chọn tô nền nhạt màu chính · đầu bảng gạch ngang khi chọn một phần · dòng không áp được hành động: checkbox khoá + Tooltip lý do |

* Màu `#3C4043` / `#505356` lấy từ mẫu ERP, **chưa có token** — khi dựng component cần đối chiếu
  `background-inverted` hoặc thêm token qua Iteration Guide.
* UC chỉ khai: danh sách hành động chung (thứ tự, cái nào nguy hiểm) và điều kiện khoá dòng.

### Device Frame (khung thiết bị mobile, 06/10/2026)

Khung nền cho mọi màn mobile (mẫu M1–M4, khung "Mobile" của component dự án, màn `-mob`). Chỉ vẽ phần
của hệ điều hành; không phải control, không có hành vi.

| Set | Biến thể / thuộc tính | Dựng từ |
| --- | --- | --- |
| `Device / Status Bar` | Tone = Default / Inverted · TEXT `Time` | Theo file app DELTA ERP 3.0 (`hH32r7V3CaQ4UepOZq5pay`, node `414:8182`): giờ SF Pro Semibold 15; glyph sóng 4 cột, wifi, pin dựng lại bằng vector, màu gắn biến; Dynamic Island 126×37 đen, cách đỉnh 11 |
| `Device / Home Indicator` | Tone = Default / Inverted | Thanh 134×5, `Radius/Full` |
| `Device / Frame` | Không biến thể · SLOT `Content` | Status Bar + Content + Home Indicator |

* **Kích thước:** mọi màn mobile dùng khung **393×852 (iPhone 14 Pro)** — đổi từ 375×812 ngày 06/10/2026.
  Status bar cao 54 có Dynamic Island ở giữa; giờ căn giữa vùng trái, cụm sóng/wifi/pin căn giữa vùng phải.
  Vùng Home indicator cao 34 (thanh cách đáy 8). Slot Content 393×764, không đè lên hai vùng an toàn.
  Các khung 390×844 dựng trước đó (BottomSheet, Notification Center, Activity Log, M4 thử) chuyển dần sang 393.
* Dynamic Island là phần cứng: đen cứng `#000` ở cả Light/Dark, không gắn biến.
* **Tone:** Default = `Text/Primary` / `Icon/Primary` (tự đổi theo mode Light/Dark). Inverted =
  `Text/On Dark` cho cả chữ và icon — dùng khi phần trên/dưới màn có nền tối, ảnh, hoặc đang mở scrim.
  Đổi tone: chọn instance Status Bar / Home Indicator trong Frame (đã expose) → Tone.
* **Nền khung:** `Core/Background Body`; màn cần nền khác thì đổi fill trên instance.
* Luôn hiện cả Status bar và Home indicator (chốt 06/10/2026); màn ảnh toàn màn hình cần ẩn thì detach.
* Giờ cố định "9:41", SF Pro Semibold 15 (font hệ thống iOS, không phải text style của dự án). Máy không
  cài SF Pro thì Figma báo thiếu font — cài SF Pro từ Apple Developer.
* Glyph ở tone Inverted gắn `Text/On Dark` vì chưa có biến `Icon/On Dark`.
* Home indicator giữ bản dự án (gắn biến), cùng số đo với file app.
* **Figma:** trang Layout, khung `Device Frame · innvie` (`5370:5589`) gồm Master Components và
  Trạng thái & ví dụ (Light · Dark · Inverted trên nền tối · Có nội dung trong slot). `Device / Status Bar`
  `5370:5625` · `Device / Home Indicator` `5370:5643` · `Device / Frame` `5371:3063`. Hai set Status Bar /
  Home Indicator có nền xám ở trang Master để thấy được bản Inverted; nền này không theo vào instance.

### Bottom Navigation (CMP-11 Mobile, 06/10/2026)

Điều hướng chính của mẫu M1 trên mobile, thay hamburger + `MobileNav`. Astryx không có component này nên
dựng thành component dự án.

| Set | Biến thể / thuộc tính | Dựng từ |
| --- | --- | --- |
| `Bottom Navigation / Tab` | State = Rest / Selected · TEXT `Label` (ẩn, làm nhãn truy cập) · INSTANCE_SWAP `Icon` · BOOLEAN `Has Badge` | Icon 24; `Badge` Info Pill |
| `Bottom Navigation / Scan` | State = Rest / Pressed | Tròn 56, nền `Core/Accent`, icon `icon/scan-qr-code` 24 `Core/On Accent`, `Elevation/Medium`; đặt giữa cột thứ 3, căn giữa dọc thanh |
| `Bottom Navigation` | Selected = Trang chủ / Lịch nhắc / Thông báo / Tài khoản | Thanh nổi: 4 Tab + Scan giữa |

* **Bố cục:** thanh nổi rộng 361 (lề 16 hai bên, khung 393), cao 64, bo `{rounded.page}`, nền `Core/Background Surface`,
  `Elevation/Medium`; nổi đè lên nội dung ở đáy slot Content của `Device / Frame` (mép dưới thanh cách vùng
  Home indicator 8), nội dung màn gốc cuộn dưới thanh và chừa đệm đáy 92 (xem M1). Chia 5 cột
  bằng nhau: **Trang chủ · Lịch nhắc · [Quét] · Thông báo · Tài khoản**; nút Quét tròn 56 **nằm trong thanh,
  căn giữa dọc** (lùi vào 4 như khối nền tab), không nhô lên — 06/10/2026, khi bỏ nhãn tab.
* **Tab — chỉ icon, không hiện chữ** (chốt 06/10/2026, sau khi so với bản icon + nhãn). Nhãn vẫn khai trong
  `Label` và ẩn đi, dùng làm nhãn truy cập cho trình đọc màn hình. Rest = `Icon/Secondary`. Selected = khối nền
  `Core/Neutral` + `Icon/Primary`, nhận ra bằng cả nền lẫn màu. Không dùng `Accent Muted` vì trùng nền thanh
  ở Dark. Cả cột bấm được (cao 64, đạt ≥ 44).
* **Khối nền đồng tâm với thanh:** khối lùi vào 4 so với mép thanh (đệm dọc của Tab `Spacing/1` = đệm ngang của
  Bar), rộng hết cột (68), cao 56, bo **24 = 28 (`{rounded.page}` của thanh) − 4**. Không có biến bán kính 24
  nên để giá trị cứng. Đổi bo hoặc đệm của thanh thì tính lại theo công thức này.
* **Màu icon khi thay icon:** icon thay qua `Icon` giữ màu gốc (`Icon/Primary`), không tự theo State → mỗi Tab
  trong thanh gắn màu icon tường minh theo State (đã gắn cho 4 biến thể). Cùng lưu ý cho `Button` Primary thay
  `Icon Source`: gắn icon `Core/On Accent`, nếu không icon tối trên nền tối.
* **Icon:** Trang chủ `icon/house` · Lịch nhắc `icon/calendar-clock` · Thông báo `icon/bell` · Tài khoản
  `icon/circle-user`.
* **Badge** trên tab Thông báo: chỉ đếm việc cần xử lý, tối đa `9+` (CMP-02), `Badge` Info.
* **Nút Quét:** chỉ icon, nhãn truy cập "Quét mã QR"; mở màn quét bằng camera.
* **Nhãn tab** (không hiện, chỉ để trình đọc màn hình): Trang chủ · Lịch nhắc · Thông báo · Tài khoản.
* **Khi nào thanh hiện, khi nào ẩn:**
  * Thanh **chỉ hiện ở 4 màn gốc** — màn đầu tiên khi chạm mỗi tab (Trang chủ, Lịch nhắc, Thông báo, Tài khoản).
  * Khi **đi sâu vào màn con** (vd từ Thông báo chạm 1 thông báo → màn chi tiết; từ Trang chủ chạm
    "Tạo mới" → form), thanh **ẩn**, nút Quét ẩn theo.
  * Màn con có nút **←** góc trên trái để quay lại; về màn gốc thì thanh hiện lại, đúng tab lúc rời đi.
  * Đáy màn con dành cho **hành động chính của màn đó**, cố định đáy (dễ chạm bằng ngón cái): form (M3) →
    nút **Gửi**/**Lưu** rộng hết màn; chi tiết (M4) → hành động chính của bản ghi (vd **Xác nhận**). Màn con
    không có hành động → đáy để trống, chỉ còn Home indicator.
  * Lý do: không có hai thanh chồng nhau ở đáy; không chạm nhầm sang tab khác khi đang nhập dở form (rời
    form có dữ liệu chưa lưu theo GR-13); nhường chỗ cho nội dung màn con.
  * Màn con cần quét (vd quét mã trong form) tự đặt nút quét riêng trong màn, không dựa vào nút Quét của thanh.
* Chạm lại tab đang chọn → cuộn danh sách về đầu (đề xuất).
* **UC phải khai báo:** feature mở từ tab nào / màn nào; quét xong đi tới màn nào.
* **Figma:** trang Layout, khung `Bottom Navigation · innvie` (`5377:5655`) gồm Master Components và
  Trạng thái & ví dụ (Trang chủ · Lịch nhắc · Thông báo badge 9+ · Tài khoản Dark · Quét đang nhấn, đặt
  trong `Device / Frame`). `Bottom Navigation / Tab` `5377:5693` · `Bottom Navigation / Scan` `5377:5715`
  · `Bottom Navigation` `5381:3341`. Tab và Scan trong thanh đã expose (bật/tắt badge, Scan Pressed).

## States

### Trạng thái giao diện: mọi màn phải có đủ

| Trạng thái | Component dùng | Mẫu tham chiếu |
| --- | --- | --- |
| **Rỗng · chưa có dữ liệu** | `EmptyState` (icon + tiêu đề + mô tả + hành động); trong cột/khối nhỏ dùng Size=Compact. Nút **+ Tạo mới** nếu user có quyền | Cột "In review" của Kanban: "Nothing in review / Items awaiting your review appear here." |
| **Rỗng · lọc/tìm không ra** | `EmptyState`: "Không tìm thấy kết quả phù hợp" + nút **Xoá bộ lọc**. **Không** có Tạo mới (2.12) | — |
| **Đang tải** | `Skeleton` giữ đúng hình khối nội dung; `Spinner` cho thao tác ngắn; Button State=Loading khi gửi; ProgressBar khi biết tiến độ | Shell Side/Top Nav: vùng nội dung skeleton |
| **Lỗi field** | Field`state=error` + status message dưới field, chữ `{colors.error}` + ring error | — |
| **Lỗi trang/khối** | `Banner` Status=error (có hành động thử lại ở End Content) | — |
| **Thành công/xác nhận** | `Toast` (tạm thời) hoặc `Banner` success (bền) | — |
| **Vô hiệu** | State=Disabled (opacity 0.5 cho nút; chữ`{colors.text-disabled}` cho field) | — |
| **Đang chọn** | TableCell/ListItem/SideNavItem State=Selected; SelectableCard Selected | — |

### Ánh xạ trạng thái nghiệp vụ

Gán mỗi trạng thái nghiệp vụ vào **một nhóm** dưới đây. **Nhãn lấy nguyên văn từ `srs/{feature}-states.md`**,
không lấy từ bảng này. Luôn có **chữ** đi kèm màu (Badge Pill có nhãn, hoặc StatusDot + nhãn).

**Chip trạng thái trong bảng, thẻ, đầu trang chi tiết (chốt 12/10/2026, giống app mobile):** `Badge`
Shape = Pill, nền **nhạt** họ categorical (`-bg` + chữ `-text`, icon `-icon`), **icon thay chấm** đứng
trước nhãn. Chữ Inter `{typography.supporting}` đậm 600, không kế thừa font tiêu đề. Nền *vivid*
(Variant Info/Success/Warning/Error) chỉ dùng cho số đếm, cảnh báo nổi bật — không dùng cho cột trạng thái.
Một feature có nhiều trạng thái "đang xử lý" thì tách họ màu để phân biệt bước (bảng dưới, cột *Họ
categorical*); icon do feature chọn theo nghĩa trạng thái và ghi trong UC.

| Nhóm | Badge Variant | StatusDot | Họ categorical (chip nền nhạt) | Ví dụ trong mẫu Astryx |
| --- | --- | --- | --- | --- |
| Chưa bắt đầu / nháp / tồn đọng | Neutral | neutral | Gray | Backlog, To-do |
| Đang xử lý | Info | info | Blue → Teal → Purple (theo thứ tự bước) | In Progress |
| Chờ / cần chú ý / chờ duyệt | Warning | warning | Yellow | Unfulfilled, In review, Needs attention |
| Hoàn tất / thành công | Success | positive | Green | Done, Paid |
| Lỗi / từ chối / hủy / nghiêm trọng | Error | negative | Red | (High priority) |

* Mức ưu tiên (Low/Medium/High) và phân loại **không** phải trạng thái. Dùng Badge màu categorical (Teal/Yellow/Red) hoặc Token.
* Trong wireframe B&W: chỉ ghi **nhãn chữ** của trạng thái (ví dụ `[Badge: Chờ duyệt]`), không tô màu.
* Hai mẫu Astryx đang lệch nhau: Grouped Table tô "Todo" màu vàng, còn Kanban tô "To-do" màu xám. **Theo bảng trên**: chưa bắt đầu = Neutral.

## Content & Formatting

Giao diện viết **tiếng Việt**, định dạng theo locale **vi-VN**. Chữ trong các mẫu Astryx là tiếng
Anh và kiểu Mỹ, chỉ để tham khảo bố cục. Khi vẽ màn, chữ và định dạng phải theo mục này.

### Chữ trên giao diện

* **Viết hoa:** chỉ viết hoa chữ đầu câu và tên riêng ("Tạo yêu cầu", "Lưu thông tin cho lần sau"). Không viết hoa từng chữ, không viết hoa toàn bộ, trừ badge nhấn mạnh.
* **Nhãn nút** là động từ + đối tượng, ngắn ("Tạo yêu cầu", "Gửi hóa đơn", "Thêm vào giỏ"). Tránh nhãn chung chung như "OK" hay "Xác nhận" khi nói rõ được hành động.
* **Vị trí nút chính:** trong form đặt **cuối form, căn trái theo cột field**; trên header trang đặt **góc phải**.
* **Thứ tự nút:** chính trước, phụ sau (từ trái sang): `[Lưu] [Hủy]` (Primary rồi Ghost). Trên header: phụ bên trái, chính ngoài cùng bên phải ("Nhập lại kho" · "Sửa").
* **Placeholder** là ví dụ định dạng ("ten@congty.vn", "0901 234 567"), không thay cho nhãn.
* **Trường bắt buộc:** dấu `*` sau nhãn (FieldLabel Indicator=Required); trường không bắt buộc ghi "(không bắt buộc)".
* **Giá trị rỗng** trong bảng theo loại trường (`web-common-rules.md` 2.10, chốt 01/10/2026):
  cột Ghi chú → để trống hẳn · ID/Mã → `N/A` · mọi cột khác → `-`.
* **Đếm** đặt cạnh tiêu đề bằng Badge Neutral nhỏ ("Bảng công việc 7", "Đang xử lý 3").
* Chữ tiếng Việt thường dài hơn tiếng Anh khoảng 20–30%. Nhãn nút, tab, cột bảng phải để chỗ co giãn, không cố định bề rộng theo chữ tiếng Anh của mẫu.

### Copy động: lỗi, xác nhận, trạng thái rỗng, toast, loading

Cấu trúc câu cho copy ĐỘNG (đổi theo tình huống, khác nhãn tĩnh ở trên) — gộp lại một chỗ theo khung
`ux-copy` (CTA / Error / Empty state / Confirmation / Loading). Giọng và nhãn nút giữ đúng như Astryx
đã dùng; các mục đánh dấu *(đã có)* chỉ gom lại từ `components.md` để nằm một chỗ, không đổi nội dung gốc.

* **Tông giọng chung:** ngôi "bạn", câu ngắn, động từ đứng đầu cho hành động, không đùa cợt, không "Vui lòng" rườm rà. Áp dụng cho mọi dòng dưới.
* **Xác nhận hành động phá hủy** (Dialog — Confirmation): tiêu đề `"<Động từ> <đối tượng>?"` + nội dung nói rõ hậu quả/có hoàn tác được không + nút ghi đúng hành động (Destructive) thay "OK"/"Hủy" chung.
  Ví dụ: "Xóa yêu cầu #1024? Yêu cầu và lịch sử xử lý sẽ mất, không thể hoàn tác." → `[Xóa yêu cầu] [Hủy]`
* **Xác nhận hành động khác** (Dialog — Confirmation, theo SC-03 `web-common-rules.md`): 4 mẫu cố định,
  ưu tiên dùng tên bản ghi nếu có, không có tên thì dùng mã, không có cả hai thì bỏ qua phần đó.
  - Thu hồi: "Thu hồi yêu cầu?" · "Bạn đang thu hồi [tên feature] **[tên/mã]**. Yêu cầu sẽ trở về trạng thái Bản nháp." → `[Thu hồi] [Hủy]`
  - Phê duyệt: "Xác nhận phê duyệt?" · "Bạn đang phê duyệt [tên feature] **[tên/mã]**." → `[Phê duyệt] [Hủy]`
  - Từ chối: "Từ chối yêu cầu?" · "Bạn đang từ chối [tên feature] **[tên/mã]**." → `[Từ chối] [Hủy]`
  - Huỷ form (có dữ liệu chưa lưu): "Huỷ bản ghi?" · "Bạn có dữ liệu chưa được lưu. Nếu rời khỏi trang, toàn bộ thông tin sẽ bị mất." → `[Huỷ] [Tiếp tục chỉnh sửa]`
  - Rời trang khi có dữ liệu chưa lưu (đóng tab, đóng trình duyệt, tải lại — theo 2.13): dùng hộp
    confirm **gốc của trình duyệt**, không vẽ Dialog. Câu: "Bạn có muốn rời trang? Dữ liệu chưa lưu sẽ mất."
    (Trình duyệt có thể thay bằng câu mặc định của nó; không vẽ màn này trong Figma.)
* **Lỗi kiểm tra trường** (cấp field, khác Banner/Toast): nói đúng trường nào sai + cách sửa, câu ngắn dưới field, không lộ mã lỗi kỹ thuật.
  Ví dụ: "Số điện thoại phải có 10 số" thay vì "Lỗi 422: invalid_format".
* **Lỗi xung đột nghiệp vụ** (Dialog — Popup Error, theo mục 2.15 Loại 2 của `web-common-rules.md`,
  khác Dialog xác nhận ở trên): dùng khi lỗi chỉ phát hiện được SAU KHI submit, do đối chiếu dữ liệu
  hoặc ràng buộc nghiệp vụ ở server (trùng mã, vượt hạn mức, xung đột dữ liệu...) — không thuộc về
  một trường cụ thể nên không báo inline được. Tiêu đề lỗi (màu error) + mô tả chi tiết + nút Đóng,
  thêm nút Thử lại nếu hành động retry được. Không tự đóng; giữ nguyên form sau khi đóng để user
  xem lại và điều chỉnh.
  Ví dụ: "Nhà cung cấp này đã tồn tại trong hệ thống." · "Lượng đặt mua vượt quá hạn mức hợp đồng." ·
  "Tên cây dầu đã được sử dụng. Vui lòng chọn tên khác."
* **Trạng thái rỗng** *(đã có khung ở components.md, thêm câu Việt)*: tiêu đề nói rõ cái gì rỗng + vì sao + CTA cụ thể.
  Ví dụ: "Chưa có đơn hàng nào. Tạo đơn đầu tiên để bắt đầu theo dõi." → `[Tạo đơn hàng]`
* **Banner** *(đã có)* — xem `components.md` § Banner: tiêu đề ngắn, dễ lướt, không kể lể nguyên nhân.
  Ví dụ: "Thanh toán thất bại" (không phải "Đã có sự cố khi xử lý khoản thanh toán gần nhất của bạn").
* **Toast** *(đã có)* — xem `components.md` § Toast: vài từ xác nhận hành động; thêm `[Hoàn tác]` nếu đảo ngược được.
  Ví dụ: "Đã lưu thay đổi" · "Đã xóa 3 mục [Hoàn tác]".
* **Đang tải/xử lý:** mẫu "Đang <động từ>…", không dùng "Loading...".
  Ví dụ: "Đang tải…" · "Đang lưu…" · "Đang xử lý…".

### Nhập liệu và kiểm tra (theo 2.1–2.3, 2.7, 2.15)

Lỗi cấp field là **Inline Error** (2.15 Loại 1): viền field chuyển error + câu lỗi dưới field
(Field `state=error`), tự ẩn khi giá trị hợp lệ. Lỗi server không gắn với field → Popup Error; lỗi
kỹ thuật → Toast error (xem Copy động).

| Quy tắc | Chuẩn |
| --- | --- |
| Khi nào kiểm | **On Blur**: rời field (click ra ngoài, sang field khác) thì kiểm và hiện lỗi field đó. **On Submit**: bấm Lưu/Gửi/Tạo mới thì kiểm **mọi** field, kể cả field chưa chạm |
| Submit có lỗi | Hiện inline error mọi field lỗi, cuộn tới field lỗi **đầu tiên**, không gửi đi, nút về trạng thái thường |
| Submit hợp lệ | Nút Loading + vô hiệu tới khi có kết quả. Server trả lỗi → hiện lỗi tương ứng, giữ nguyên form, nút về thường |
| Bắt buộc bỏ trống (Input, Select) | Nhãn có `*` (FieldLabel Indicator=Required). Câu chung: "Nhập [tên trường]." (Select: "Chọn [tên trường].") — dùng khi UC không ghi câu riêng |
| Tiêu đề (Title) | Tối đa **50** ký tự. Vượt → "Tối đa 50 ký tự." |
| Text ngắn | Tối đa **255** ký tự. Không gõ thêm được; dán vượt thì tự cắt |
| TextArea | Tối đa **1000** ký tự (hoặc theo UC), đếm ký tự góc dưới phải (`120/1000`); dán vượt thì tự cắt |
| Ngày sai định dạng | "Hãy nhập ngày tháng theo định dạng: dd/mm/yyyy" |
| Email sai định dạng | Phải có `@`. Câu lỗi: "Email không đúng định dạng." |
| Select | Single: chọn 1. Multi: giá trị hiện dạng tag trong ô. Danh sách từ server: tìm gần đúng khi gõ |

* Câu lỗi theo tông giọng của Copy động (không "Vui lòng"), không lấy nguyên văn `web-common-rules.md`.

### Ngày giờ

Dùng component **Timestamp** và chọn Format phù hợp. Giờ luôn là **24 giờ**.

| Format | Hiển thị | Dùng khi |
| --- | --- | --- |
| Date | `03/07/2026` (dd/MM/yyyy) | Ngày trong bảng, form, hạn chót |
| Date Time | `23/02/2026 09:12` | Nhật ký, lịch sử thao tác |
| Time | `09:12` | Tin nhắn trong ngày |
| Relative | `Vừa xong` · `5 phút trước` · `2 giờ trước` · `Hôm qua, 22:27` | Hoạt động gần đây (dưới 7 ngày); quá 7 ngày chuyển sang Date |
| Ngày có thứ | `Thứ Hai, 03/07/2026` | Lịch, tiêu đề nhóm theo ngày |
| Khoảng ngày | `01/07 – 15/07/2026` | DateRangeInput |

* Ngày tháng dạng ngắn trong ô hẹp (thẻ Kanban, hạn): `Hạn 08/07`.
* Không dùng tên tháng tiếng Anh ("Jul 3") và không dùng AM/PM.
* **Quy định cho dev:** tự định dạng theo bảng trên, **không dùng đầu ra `Intl` mặc định** của
  `Timestamp` (code ra `3 thg 7, 2026`, `9:12`, `bây giờ`… — lệch bảng). Ngưỡng Auto chuyển
  Relative → ngày giờ là 7 ngày, khớp bảng. Rút gọn tiền (`tr đ`, `tỷ đ`) cũng là quy ước dự án,
  không lấy từ code.

### Số và tiền tệ

Theo `web-common-rules.md` (mục 2.4, 2.5) — **đổi từ chuẩn vi-VN sang chuẩn dự án dưới đây**
(quyết định 29/09/2026), thay cho định dạng dấu chấm/phẩy trước đó.

* **Số:** dấu phẩy `,` ngăn hàng nghìn, dấu chấm `.` thập phân: `1,234,567` · `12.5`.
* **Phần trăm:** `12.5%` (không có khoảng trắng).
* **Tiền:** đơn vị **VND**, hiển thị `100,000 đ` hoặc `100,000 VND` tùy context, không có số lẻ.
  Ví dụ: `89,000 đ`. Số tiền lớn trong ô hẹp có thể rút gọn: `1.2 tr đ` · `3.5 tỷ đ` (giữ quy ước rút
  gọn của tài liệu này, xem "Còn mở"), nhưng ở màn chi tiết và tổng tiền phải ghi đủ.
* **Ngoại tệ:** `50 USD · 25,000 VND/USD`.
* **Làm tròn** (2.6, áp dụng khi hiển thị, tính toán và lưu):
  - Số học và **USD**: 2 chữ số thập phân, **làm tròn nửa lên** (Round Half Up): `12.345` → `12.35` · `123.456 USD` → `123.46 USD`.
  - **VND**: không có số lẻ, **luôn làm tròn lên** hàng đơn vị (Round Up): `123,456.10` → `123,457 đ`.
* Số tiền và số liệu **căn phải** trong bảng (TableCell Align Right); tổng tiền in đậm.
* Ô nhập tiền (NumberInput / InputGroup) đặt `đ` hoặc `VND` ở suffix và tự chèn dấu phẩy hàng nghìn khi gõ.

### Thông tin liên hệ và địa chỉ

* **Số điện thoại:** `0901 234 567`; có mã quốc gia thì `+84 901 234 567`.
* **Địa chỉ** ghi từ nhỏ đến lớn: số nhà, đường → phường/xã → tỉnh/thành phố. Form địa chỉ dùng Selector cho Tỉnh/Thành phố → Phường/Xã, còn số nhà, đường là TextInput. Không dùng ZIP code hay State như mẫu gốc.
* **Họ tên:** một trường "Họ và tên" thay cho cặp First/Last name của mẫu gốc, trừ khi nghiệp vụ yêu cầu tách.

## Accessibility

Tương phản được đo trên mode Light (dark ghi riêng):

| Cặp | Tỉ lệ | Kết luận |
| --- | --- | --- |
| text-primary / surface | 17.9 : 1 | Đạt AAA |
| text-secondary / surface | 4.74 : 1 | Đạt AA |
| text-secondary /**background-body** | **4.2 : 1** | **Chưa đạt AA** cho chữ 12–14px. Tránh dùng chữ secondary trên nền body |
| on-accent / accent (nút Primary) | 15.1 : 1 | Đạt |
| Badge Info / Success (chữ trắng) | 4.57 / 5.02 : 1 | Đạt AA |
| **Badge Error** (trắng trên #e33f4a) | **4.14 : 1** | **Chưa đạt AA** với chữ 12px |
| Badge Warning (#171717 trên #ffce2f) | 12.1 : 1 | Đạt |
| Categorical text/bg (Blue, Red, Yellow, Green) | 6.4–7.1 : 1 | Đạt |
| **border-emphasized / surface** (viền input) | **1.48 : 1** | **Chưa đạt 3:1** (WCAG 1.4.11) cho ranh giới control |
| accent / background-surface (focus outline nút,`{colors.accent}`) | 15.1 : 1 (Light) · 12.7 : 1 (Dark) | Đạt — vượt xa 3:1 (WCAG 1.4.11) |
| accent / background-surface (viền field khi focus) | 15.1 : 1 (Light) · 12.7 : 1 (Dark) | Đạt 3:1 (WCAG 1.4.11). Đây là dấu hiệu focus của field |
| input-ring-focus / background-surface (`ring-focus` inset) | 1.13 : 1 (Light) · 1.0 : 1 (Dark) | Chỉ trang trí, không tính là dấu hiệu focus (KG-11) |
| Dark: text-secondary / body | 6.8 : 1 | Đạt |

**Quyết định (27/09/2026):** ba cặp chưa đạt ở trên được **giữ nguyên theo thư viện Astryx**, không
chỉnh token. Reviewer không coi chúng là lỗi của màn. Chỉ báo lỗi khi màn **dùng sai chỗ**, ví dụ
đặt nội dung quan trọng bằng chữ secondary trên nền body (xem Don't).

* **Không truyền nghĩa chỉ bằng màu:** trạng thái luôn có nhãn chữ; StatusDot phải đi kèm chữ.
* **Focus nhìn thấy được:** nút, link, checkbox, switch có outline 2px accent (cách control một khe); field đổi viền sang accent 1px. Không được tắt, không vẽ focus chỉ bằng ring.
* **Vùng chạm:** control 28/32/36px **nhỏ hơn 44px**. Trên thiết bị cảm ứng dùng Size=LG và giãn vùng bấm (padding hàng, cả hàng bấm được).
* Nút chỉ có icon (Type=Icon Only, MoreMenu, MobileNavToggle) phải có nhãn truy cập.
* Dialog: tiêu đề rõ, có nút đóng, focus nằm trong dialog.

## Do's and Don'ts

### Do

* Đề xuất 3 phương án bố cục trước khi vẽ: 1 theo mẫu (S/P/M) có sẵn + 2 độc lập, để user chọn.
* **Mỗi nhóm hành động chỉ một nút Primary.** Các nút còn lại là Secondary hoặc Ghost.
* Dùng Destructive (nền error-muted) cho xóa/vô hiệu, và xác nhận bằng Dialog khi không hoàn tác được.
* Dùng token, không mã màu cứng. Hover/pressed dùng overlay, không tự chọn màu đậm hơn.
* Dùng MD (32px) làm cỡ mặc định. SM chỉ cho toolbar/bảng dày, LG cho màn công khai hoặc cảm ứng.
* Giới hạn chiều rộng form (khối 800px, nội dung 752px cho 1 cột — xem Grid & Container). Field ngắn ghép 2 cột (Email/Số điện thoại, Tỉnh-Thành/Phường-Xã).
* Có đủ trạng thái rỗng, đang tải, lỗi cho mọi vùng dữ liệu.
* Dùng Banner cho thông báo bền, Toast cho phản hồi tạm thời.

### Don't

* Không thêm màu brand vào theme Neutral và không dùng 6 theme phụ của thư viện.
* Không dùng họ categorical Red/Green thay cho Status, và không dùng Status cho tag phân loại.
* Không cho form trải hết bề rộng desktop 1920px.
* Không dùng bóng cho card thường. Bóng chỉ dành cho lớp nổi (dialog, toast, dropdown).
* Không dùng chữ secondary trên nền body cho nội dung quan trọng (tương phản 4.2:1).
* Không dùng SegmentedControl để chuyển trang/view (đó là việc của Tabs), và không dùng Tabs để chọn giá trị.
* Không tự tạo component mới khi đã có component tương đương trong thư viện.

## Responsive Behavior

### Breakpoints

**File Figma không định nghĩa breakpoint** (bảng mốc của dự án ở cuối mục này). Mọi màn mẫu là desktop 1920×1080, và không có mẫu
tablet/mobile. Những gì *thư viện có sẵn* cho màn nhỏ:

* `MobileNav` (drawer) + `MobileNavToggle` (hamburger) thay SideNav/TopNav.
* `SideNav` có trạng thái Collapsed.
* `Dialog` Variant=Fullscreen.
* `AppShell` Nav Layout=Content Only.

**Trong code Astryx** (kiểm repo `facebook/astryx`, nhánh main, 29/09/2026):

* **Ngưỡng "adaptive":** `(max-width: 768px) and (pointer: coarse)`, tức màn ≤ 768px *và* dùng ngón
  tay (`packages/core/src/hooks/useAdaptivePresentation.ts`). Đúng điều kiện → hiển thị
  `bottom-sheet`, ngược lại → `popover`. Tablet lớn và laptop cảm ứng vẫn giữ kiểu desktop.
* Prop `presentation` = `popover` / `bottom-sheet` / `adaptive` có ở DropdownMenu, MoreMenu,
  ContextMenu, Selector, MultiSelector. Dialog có mẫu `AdaptiveDialog` (`touchPresentation="bottom-sheet"`).
* **AppShell** chuyển sang MobileNav khi bề rộng `< mobileNav.breakpoint` (tên breakpoint lấy từ Theme,
  hỗ trợ tới `xl`, `2xl`). Theme có thể đổi cỡ chữ/khoảng cách theo bề rộng (`widthBreakpoints`).
* Ô nhập ngày giờ tự dùng picker cảm ứng/native trên thiết bị cảm ứng; trên iOS, chữ trong ô nhập
  được nâng tối thiểu 16px để tránh trình duyệt tự zoom.
* Cách bày Web | Mobile trên Figma theo các hành vi này: xem *Components* → "Web và Mobile".

**Bảng mốc của dự án (chốt 12/10/2026):** dùng nguyên bảng mặc định `DEFAULT_WIDTH_BREAKPOINTS`
của Astryx (`packages/core/src/theme/themeAdaptations.ts`), không tự đặt mốc riêng. Mỗi mốc tính từ
giá trị đó trở lên.

| Mốc | sm | md | lg | xl | 2xl |
| --- | --- | --- | --- | --- | --- |
| Từ | 640 | 768 | 1024 | 1280 | 1536 |

| Bề rộng | Khung trang | Khung vẽ Figma |
| --- | --- | --- |
| ≥ 1536 (2xl) | Menu 240 mở, thanh trên 44, lề 24 (§ Grid & Container › Khung trang dự án) | **1920** |
| 1280–1535 (xl) | Như trên; nội dung co lại, trang chi tiết ≤ 1440 vừa khít | **1440** |
| 768–1279 (md–lg) | Menu **tự thu gọn 64px** (cột icon); bấm nút thu/mở → menu 240 đè lên nội dung | không vẽ riêng |
| < 768 | `AppShell` đổi sang `MobileNav` (mặc định `mobileNav.breakpoint = 'md'`, đúng 768 vẫn là layout rộng) + Bottom Navigation; bảng → thẻ | **393** (`Device / Frame`) |

Menu, Selector chuyển bottom-sheet theo ngưỡng adaptive ở trên (≤ 768 *và* cảm ứng), độc lập với
bảng mốc.

**Quyết định (27/09/2026):** thiết bị chính để **đề xuất** là **Desktop web**, với bố cục dựng ở
khung 1920×1080 theo các mẫu P. Vẫn phải hỏi user khi chọn device theo quy ước của workspace.

### Touch Targets

Control 28/32/36px, nhỏ hơn 44px. Xem mục Accessibility.

### Collapsing Strategy (định hướng, chưa có chuẩn)

SideNav → Bottom Navigation (§ Bottom Navigation); bảng nhiều cột → List/Item; form 2 cột → 1 cột; rail phải của P7 → dời xuống dưới hoặc vào Tab. Các quy tắc này **chưa có chuẩn** trong Figma, nên khi vẽ mobile phải ghi "chưa có chuẩn trong design.md". Đã có spec cụ thể ở *Mẫu bố cục (M = mobile)* (Layout, mượn nguyên tắc lưới 8pt/thumb zone/tối đa 4 cỡ chữ từ `mobile-app-ui-design`); Figma node: M1, M2 đã dựng; M3, M4 chưa.

## Iteration Guide

1. Sửa token: sửa **khối YAML đầu file này và `design/design-tokens.css` cùng lượt**, qua approval gate.
2. Thêm mẫu bố cục: thêm dòng vào bảng *Mẫu bố cục* (mã P/M tiếp theo, node Figma, khi nào dùng).
3. Thêm component: chỉ thêm khi Astryx (code `@astryxdesign/core`) đã có. Ghi đúng tên và trục biến thể của Figma.
4. Thêm trạng thái nghiệp vụ: gán vào một nhóm trong *Ánh xạ trạng thái nghiệp vụ*, không tạo nhóm màu mới.
5. Trong văn bản, luôn tham chiếu token dạng `{colors.x}`, `{typography.x}`, `{rounded.x}`, `{spacing.x}`.
6. Known Gap mới / đóng: sửa dòng `KG-nn` ở § Known Gaps (ghi đủ chi tiết ngay tại đó); đóng thì chuyển sang "Đã quyết định" kèm ngày; mã KG không đánh số lại.
7. Dự án mới: setup file Figma theo `design/setup-figma.md` (thư viện hay bản sao) trước khi vẽ màn đầu tiên.
8. Thư viện Figma được agent đồng bộ theo code. Khi Figma đổi thì trích lại (reqwise `get_design_system_kit`, Figma MCP `get_variable_defs`) và cập nhật file này.

## Known Gaps

### Đã quyết định (27/09/2026)

* **Theme:** chỉ dùng Neutral (Light/Dark). 6 theme phụ của thư viện nằm ngoài phạm vi, không trích.
* **Alpha ở mode Dark** của `neutral`, `overlay*`, `border-default`, `input-ring-*`: chấp nhận **lấy bằng alpha của Light** (đánh dấu `*` trong YAML và có ghi chú trong CSS). Lý do là plugin chỉ trả hex không alpha, còn Figma MCP chỉ trả mode Light. *(01/10/2026: nay lấy từ code Neutral, trừ `input-ring-*` vẫn giữ `*`.)*
* **Thiết bị:** đề xuất Desktop web. Chưa có breakpoint và mẫu mobile.
* **Tương phản:** giữ nguyên ba cặp chưa đạt AA theo thư viện (xem Accessibility).
* **Định dạng:** tiếng Việt, locale vi-VN (xem Content & Formatting).
* **Font:** Cal Sans (Display, Heading 1–3) + Inter (còn lại), thay Figtree vì thiếu dấu tiếng Việt. Đã sửa 13 text style và biến `Font Family/Heading`, `Font Family/Body` trong file Figma.
* **Mẫu bố cục mobile (29/09/2026):** chốt spec M1–M4 ở *Mẫu bố cục (M = mobile)*, mượn nguyên tắc lưới 8pt/thumb zone/tối đa 4 cỡ chữ từ `mobile-app-ui-design`. Figma node chưa dựng — xem "Còn mở".

### Đã quyết định (01/10/2026)

* **KG-04:** `Effects/Shadow` = đen 10% / Dark 30%, `Effects/Tint Hover` = đen / trắng chỉ để trộn — lấy từ code Neutral, thành token `shadow`, `tint-hover` (xem Effects).
* **KG-05:** `{rounded.none}` = 0px theo code (Neutral cố định, không scale); biến Figma `Radius/None` sửa 4 → 0.
* **KG-06:** dev tự định dạng theo bảng Ngày giờ, không dùng đầu ra `Intl` mặc định của `Timestamp`.
* **KG-08:** chấp nhận Timer hiện `12m 05s`; cần dạng trung tính thì dùng Clock.
* **KG-10:** token `motion` theo Neutral + quy tắc `prefers-reduced-motion` (xem Motion).
* **KG-19 (phần số điện thoại):** giữ `+84`.
* **Alpha Dark + elevation:** lấy theo code Neutral (`neutralTheme.ts`): `neutral` và `border-default` trắng 10%, `overlay` đen 80%, `*-muted` alpha 24%; elevation đổi giá trị cả Light và Dark (thêm `elevation-dark`). Figma đã sửa theo (KG-28).
* **KG-01, KG-05, KG-07, KG-28 (Figma):** gắn lại `Font Size/*`, `Line Height/*` cho 13 text style; `Radius/None` = 0; Toast gắn biến theo code (`background-inverted` / `error-inverted`); effect style Elevation theo code + bộ Dark qua biến `Effects/Elevation *`.
* **KG-02:** quy trình áp lại sửa của dự án sau mỗi lần đồng bộ Astryx: `design/setup-figma.md` § 5.1.
* **KG-22:** giá trị rỗng theo loại trường (Ghi chú trống · ID/Mã `N/A` · còn lại `-`).
* **KG-09:** bề rộng khung/cột đo từ node Figma của mẫu, thay số ước lượng từ ảnh (xem Grid & Container).
* **KG-18, KG-19, KG-24:** kiểm tra dữ liệu nhập, câu lỗi ngày/email, giới hạn ký tự (xem *Nhập liệu và kiểm tra*); rời trang có dữ liệu chưa lưu dùng confirm gốc của trình duyệt (xem Copy động). Theo `web-common-rules.md` 2.1–2.3, 2.7, 2.13.
* **KG-20:** làm tròn số/USD 2 số lẻ nửa lên, VND luôn lên hàng đơn vị (xem Số và tiền tệ, 2.6).
* **KG-21, KG-25, KG-26, KG-27:** tìm kiếm, căn lề, freeze, nhóm, sắp xếp, export, lọc theo cột, cột action (xem *Quy tắc bảng danh sách*).
* **KG-12:** sửa trong ô bảng theo ngữ cảnh (danh sách click-to-edit, lưu từng ô; form luôn là input, lưu cùng form); lỗi ô detached: viền + icon + Tooltip, Banner khi Submit (xem § Sửa trong bảng). Figma: `Sửa trong bảng / Editable Cell`.
* **KG-23:** EmptyState tách "chưa có dữ liệu" (có Tạo mới) và "lọc không ra" (Xoá bộ lọc) (xem States).
* **KG-11:** field dùng **viền 1px `{colors.accent}` khi focus** (15.1:1) làm dấu hiệu chính, ring inset chỉ là lớp phụ — khớp code Neutral (`Field/inputStyles`) và Figma (mọi field State=Focused đã có viền `Core/Accent`). Outline focus của nút/checkbox/switch = 2px accent. Figma: vòng focus Checkbox, Switch đổi từ xanh cứng (#0D73E5, #0064E0) sang `Core/Accent` + khe `Core/Background Surface`.
* **KG-17:** phần phân trang SC-04 chưa nói thành chuẩn (về trang 1 khi đổi lọc/tìm/sort, giữ trang khi quay lại, Skeleton khi chuyển trang, tải thêm trên mobile và trong panel); trang hiện tại dùng accent thay xanh lá (xem § Phân trang danh sách).
* **KG-13:** bỏ Drawer; bộ lọc nâng cao = thanh chip `PowerSearch` (xác nhận từng điều kiện), tuỳ chỉnh cột = thao tác trên tiêu đề cột + icon button Tuỳ chỉnh cột trên thanh công cụ (xem § Bộ lọc nâng cao, § Tuỳ chỉnh cột). Khác SC-05/06 gốc, đã duyệt.
* **KG-14:** đã review 4 set `.Value Editor`, `Column Menu`, `Header Cell`, `Column Picker` (node `5176:9303`, `5177:7634`); sửa lỗi tiêu đề căn phải bị cắt sớm (Header Cell trục `Align`, biến thể Right ẩn `Align Spacer`); xoá phương án Drawer (2 khung cũ + component `Drawer`). Cột lọc được/cột khoá do từng UC ghi (xem § Tuỳ chỉnh cột).
* **KG-15:** Activity Log dùng phương án A + B (khung `ActivityLog · innvie` `5160:3295`): A = `Activity Log / Latest` (Banner kết quả gần nhất dưới header), B = Body `State=Theo lượt` + `Activity Log / Round`. Đã có đồng ý của phụ trách SC-08, xác nhận nghiệp vụ/BE ("Gửi lại", mốc lượt, thời gian chờ) và designer review (gồm tương phản Description của Banner). Body `State=Có dữ liệu` giữ làm dự phòng.
* **KG-16:** Notification Center khác SC-02 gốc, đã duyệt: nội dung 3 dòng (hành động · mã đậm · người + module), 3 nhóm (Cần xử lý / Kết quả / Để biết), badge chuông chỉ đếm việc cần xử lý, bỏ lý do từ chối và hạn xử lý, mobile là màn riêng, lỗi mạng dạng EmptyState, nền chưa đọc accent-muted. Tag "Đã xử lý" chuyển xuống dòng cuối, dưới Meta (Figma `Notification Center / Item` Status=Resolved). Danh sách hành động "Chờ…" do từng feature ghi theo bảng Hành động (xem § Notification Center).

### Đã quyết định (12/10/2026)

Chốt Lab ↔ DS (18 mục, `design/_lab/refs/notes.md` mục "Kết quả chốt Lab ↔ DS"):

* **Khung trang:** menu 240 (thu gọn 64) + chân menu module/cơ sở, thanh trên 44, lề 24, form ≤ 720,
  chi tiết ≤ 1440 (xem Grid & Container › Khung trang dự án).
* **Breakpoint (KG-03 phần mốc):** bảng mặc định Astryx; 768–1279 menu tự thu gọn 64px; < 768 MobileNav
  (xem Breakpoints).
* **Nút / ô nhập / nút phụ:** giữ theo DS — bo `{rounded.element}` 10px, nút phụ đen 6%, ô nhập nền
  trắng viền `{colors.border-emphasized}` (so 2 phương án trên Sandbox `5508:14821`).
* **Font tiêu đề:** giữ Cal Sans · **cỡ chữ** 14/12 · **bo thẻ** 12 · **căn ngày giờ** giữa — theo DS.
* **Thanh chọn nhiều:** spec mới (xem § Thanh chọn nhiều).
* **Phân trang:** bỏ nhãn tổng; ô *"50 / trang"* bên trái, số trang bên phải; tổng số ở thanh công cụ
  (KG-30 cũ "Hiển thị x–y / tổng" bỏ, không cần hỏi khách).
* **Thanh công cụ danh sách:** 2 hàng — tìm · Bộ lọc · Tuỳ chỉnh cột · Nhóm / chip · Xoá tất cả · n kết quả
  (xem § Bộ lọc nâng cao).
* **Chip trạng thái:** Badge pill nền nhạt categorical + icon thay chấm (xem § Ánh xạ trạng thái nghiệp vụ).

### Còn mở — khi vẽ gặp thì làm gì

> Mỗi mục ghi đủ chi tiết ngay tại đây (không còn file backlog riêng). Mặc định cho mọi mục: không
> bịa giá trị — hỏi user, hoặc vẽ theo quy định hiện có và ghi "chưa có chuẩn trong design.md".

**Mobile**
* KG-03 · Lưới cột, mẫu mobile (mốc breakpoint đã chốt 12/10/2026): spec M1–M4 đã có (29/09/2026). Khung nền `Device / Frame`
  393×852 (iPhone 14 Pro) đã dựng (06/10/2026, `5371:3063`); M1 (`5383:7822`) và M2 (5 khung `Example/List Mobile`) đã
  dựng; M3–M4 chưa dựng node Figma → vẽ
  mobile dùng `Device / Frame` và ghi "chưa có chuẩn trong design.md — theo spec M, chưa có node Figma".

**Component dự án chờ xác nhận / duyệt** — spec trong § Components - innvie logis là bản hiện hành
* KG-29 · EmptyState có hình minh hoạ đang thử (01/10/2026, trang 🧪 Sandbox): set `Illustration / Empty State` (`5277:1598`) Scene = Chưa có dữ liệu / Không có kết quả / Lỗi mạng / Không có quyền × Source = Tự vẽ / unDraw, 200×150, màu gắn biến `Color`; set `EmptyState / Illustrated` (`5281:48386`) bọc `EmptyState` Default rộng 480, hình trong slot Icon, 1 Button MD trong slot Actions; 4 màn ví dụ nhân bản từ 4.1 (y=4300). Cần quyết: (1) giữ nguồn Tự vẽ hay unDraw (license unDraw: thương mại, không cần ghi nguồn, cấm phân phối lại thành bộ); (2) cỡ hình 200×150, bề rộng 480; (3) câu chữ + nút cho Không có quyền / 404; (4) bóng unDraw đen 10% chưa gắn biến; (5) dùng hình ở mọi trạng thái rỗng hay chỉ khối lớn/toàn trang (Compact giữ icon); (6) ghi spec vào § Components và § States. Khi vẽ: tạm dùng `EmptyState` icon như § States; muốn dùng bản có hình thì ghi "chưa có chuẩn trong design.md — KG-29".
