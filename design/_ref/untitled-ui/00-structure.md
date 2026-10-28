---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/
  - https://github.com/untitleduico/react (styles/theme.css)
  - https://www.untitledui.com/react/docs/introduction
  - https://www.untitledui.com/react/docs/theming
---

# 00 — Cấu trúc, collection, mode, quy ước đặt tên

> Phạm vi: S1 (Figma — cấu trúc trang, collection, quy ước đặt tên, hướng dẫn dùng kit) +
> S2 (repo React) + S3 (docs web).

## 1. Cấu trúc trang file Figma (S1 — Pages panel)

Thứ tự trang đọc từ Pages panel (DOM):

- `❖ Getting started`
- `❖ Variables`
- `❖ FOUNDATIONS` → Colors, Typography, Logos, Icons, Misc icons, Effect styles, Spacing radius & grids
- `❖ BASE COMPONENTS` → Avatars, Badges, Button groups, Buttons, Checkboxes, Dropdowns, Inputs, Progress indicators, Radio groups, Select, Sliders, Tags, Text editors, Toggles, Tooltips, Video players (16; spec liệt kê 15, thiếu Video players)
- `❖ SHARED ASSETS` → Background elements, Banners, Email templates, Log in and sign up pages, Miscellaneous assets, Portfolio mockups, 404 pages
- `❖ APPLICATION EXAMPLES` (you can move to a separate file) → Dashboards 01/02, Informational pages 01/02, Settings pages 01/02
- `❖ APPLICATION COMPONENTS` → Activity feeds, Alerts & notifications, Application navigation, Breadcrumbs, Calendars, Card headers, Charts, Code snippets, Color pickers, Command menus, Content dividers, Date pickers, Empty states, File upload, Filters, Inline CTAs, Loading indicators, Messaging, Metrics, Modals, Page headers, Pagination, Progress steps, Section footers, Section headers, Slideout menus, Tables, Tabs, Tree views (29)
- `❖ MARKETING WEBSITE EXAMPLES` (you can move to a separate file) → About, Blog posts, Blogs, Contact, FAQ, Landing, Legal, Log in, Pricing, Sign up, Team, 404 pages
- `❖ MARKETING WEBSITE COMPONENTS` → Blog sections, Careers section, Contact sections, Content, CTA sections, FAQ sections, Footers, Header navigation, Header sections, Features sections, Metrics sections, Newsletter CTA sections, Pricing sections, Social proof sections, Team sections, Testimonial sections
- `❖ UTILITY` → Design annotations, Thumbnail

Trang Getting started có 5 frame: Welcome to Untitled UI · Getting up and running · Split up the file into multiple libraries · How to master variants · How to master Auto Layout.

## 2. Quy ước đặt tên (S1)

- `❖ NHÓM` (in hoa) = trang phân cách nhóm; trang con bắt đầu bằng `↳ `.
- Mỗi trang Foundations có frame tài liệu + frame `Notes and documentation (you can delete this)`.
- Component nội bộ/ẩn đặt tiền tố `_` (vd `_Shadow card`, `_Type scale base`, `_Container`, `_Dot`, `_Swatch base`).
- Header chung: component `Design system header` / `Design system footer`, nhãn `Foundations → <trang>`.
- Primitive màu đặt tên theo token (`neutral-300`, `brand-600`) thay vì hex rời.

## 3. Collections / nhóm biến (S1 — panel Variables)

| Collection (S1) | Số biến | Mode | Nội dung |
|---|---|---|---|
| `_Primitives` | 343 | — | Colors 311 + Spacing 32 (xem ghi chú dưới) |
| `1. Color modes` | 274 | Light mode, … | Colors 100 · Effects 23 · Component colors 174 |
| `2. Radius` | 11 | Light | radius-none…full |
| `3. Spacing` | 17 | Light | spacing-none…11xl |
| `4. Widths` | 12 | Light | width-xxs…6xl + paragraph-max-width |
| `5. Containers` | 3 | Light | container-padding-mobile/desktop + max-width |
| `6. Typography` | 32 | Light | Font family 2 · Font weight 8 · Font size 11 · (Line height 11 — chưa đọc) |

Groups trong `1. Color modes` (274) đọc từ ảnh panel ở trang Effect styles (cập nhật hơn):

- **Colors 100** → Text 21 · Border 8 · Foreground 19 · Background (bị che, `?`)
- **Effects 23** → các biến màu bóng (shadow-xs 5%, shadow-sm_01 10%, … — khớp giá trị đọc ở card)
- **Component colors 174** → màu riêng của từng component

> ⚠ Lưu ý: 100 + 23 + 174 = 297 ≠ 274 (tổng collection). Group đếm không khớp tổng — có thể do ảnh panel
> cắt bớt hoặc đếm khác nhau giữa 2 thời điểm đọc (panel Variables ghi 274, ảnh panel ghi breakdown 297).

`_Primitives` (343) = **Colors 311 + Spacing 32**. Colors 311: 27 dải × 11 = 297 + Base 3 = 300 → còn **11 chưa giải thích** (có thể thêm 1 dải 11 bậc — `?`).

## 4. Getting started (S1 — diễn giải)

- Kit ra mắt 2021; có bản **Untitled UI React** (Tailwind CSS + React Aria) đồng bộ với Figma.
- Quy trình gợi ý: nhân bản file → thay branding (logo, biến màu, typeface) → dùng section/page example dựng sẵn → xoá phần không dùng.
- Đã refactor theo Figma mới: color variables (dark mode), spacing, radius, typography, effect variables, Auto Layout 5.0, min/max width, wrap.
- File >10.000 component/variant; Figma giới hạn 2GB/tab → nên chuyển trang example (Marketing website examples, Application examples, ~40% dung lượng) sang file riêng; xoá trang ví dụ dark mode và component không dùng.
- Font mặc định **Inter** (miễn phí, Rasmus Andersson, 9 độ đậm + italic + variable font).
- Dùng như library: Publish trong Libraries modal (⌥3), bật "Add to file" ở dự án khác; library là "nguồn sự thật". Còn có thư viện "Untitled UI Icons – PRO".
- Tách library (Split up the file into multiple libraries): gợi ý Main = styles + foundations + base components/assets; Marketing components; Application components; Page examples — bằng "move published components". Cảnh báo "ghost layers" khi move component → chạy script "Compute publish statuses of soft deleted components" định kỳ.
- How to master variants / How to master Auto Layout: hướng dẫn kỹ năng Figma chung (không chứa token).

## 5. Hướng dẫn đổi màu brand (S1 — Notes trang Colors, mục ★)

- **Biến là nguồn sự thật**: mọi biến màu (và spacing, radius) tham chiếu primitives; không dùng color styles để quản lý.
- Đổi brand: chỉ cần đổi các biến `brand` trong `_Primitives` (mở Local variables → collection `_Primitives` → sửa giá trị, vd Brand/500 `#9E77ED`) → mọi chỗ dùng tím tự cập nhật; làm cho mọi bậc một lượt. Có bài tạo palette trên blog Untitled UI.
- Đổi dải xám: tương tự — đổi biến `neutral` trong `_Primitives`, hoặc chỉnh hue/saturation trong HSL picker; có thể dùng xám Tailwind khác (Slate, Gray, Zinc…).
- Sau khi đổi màu, cập nhật biến shadow nếu cần: shadow dùng đen + alpha riêng, phải sửa tay.

## 6. Luật dùng

| # | Luật | Nguồn |
|---|---|---|
| 1 | Đổi brand = repoint biến `brand` trong `_Primitives` (không đổi từng component) | S1 (★) · S3 theming |
| 2 | Biến (variables) là nguồn sự thật; primitives tham chiếu bởi mọi biến màu/spacing/radius | S1 |
| 3 | Đủ 11 bậc brand (50–950) vì component dùng cả thang | S3 theming |
| 4 | File nặng → tách trang example sang file riêng (giới hạn 2GB/tab) | S1 |
| 5 | Dark mode = ghi đè biến trong `.dark-mode` (không có `.light-mode`) | S3 dark-mode |
| 6 | Dùng semantic color (`bg-primary`) thay palette (`bg-gray-50`) để dark tự đúng | S3 dark-mode |
| 7 | v8 bỏ palette riêng, chỉ giữ `--color-brand-*`; đổi tên `utility-error→utility-red`, `utility-gray→utility-neutral`, … | S3 upgrade |

## 7. Ghi chú chưa chắc / lệch

- `_Primitives` Colors = 311 nhưng đọc được 300 (27 dải × 11 + Base 3); 11 biến còn lại chưa giải thích.
- `6. Typography` = 32 nhưng đếm được Font family 2 + Font weight 8 + Font size 11 = 21; 11 còn lại đoán là Line height (chưa thấy trực tiếp).
- `1. Color modes` group Foreground = 19 (panel bị che), Background = `?` (bị che).
- Radius: repo (S2) không khai `--radius-*`; S1 có 11, S3 docs có 10 (thang khác) — xem `04-spacing-radius-grid.md`.
