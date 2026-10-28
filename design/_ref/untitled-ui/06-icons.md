---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Icons, Misc icons, Logos)
  - https://www.untitledui.com/react/docs/icons
---

# 06 — Icons

> Nguồn: S1 (Figma — Icons, Misc icons, Logos) + S3 (docs icons). S2 dùng package `@untitledui/icons` (không có file icon trong repo).

## 1. Thư viện

| Thuộc tính | Giá trị | Nguồn |
|---|---|---|
| Thư viện Figma | Untitled UI Icons (line) | S1 |
| PRO | 4.600+ icon × 4 styles (line, solid, duocolor, duotone); file Figma dùng bộ **line** | S1 · S3 |
| Free (package) | `@untitledui/icons` — MIT, 1.100+ icon kiểu line | S3 |
| Đổi icon mặc định | từ v2.8 | S1 |

## 2. Đặc tả kỹ thuật (S1)

- Grid **24×24** (component 24×24); nét **stroke 2px**, căn giữa (center).
- Mẫu `activity` (General): vector "Icon" 20×18 lệch top 3 left 2; màu #000000 trong master (đổi màu khi dùng).
- Description của component chứa từ khóa tìm kiếm (vd activity: "activity, heartbeat, heart rate, exercise, pulse").

## 3. Cách đặt tên (S1 + S3)

- S1 (Figma): **kebab-case**; biến thể đánh số `-01`, `-02` (vd `edit-01…05`, `building-01…08`, `check-circle-broken`); hậu tố hình dạng `-circle`, `-square`, `-hexagon`, `-octagon`, `-broken`.
- S3 (package React): **PascalCase** + hậu tố số (`Home01`, `Settings01`, `User01`, `Bell01`).

## 4. Danh mục (S1 — đếm lại theo danh sách tên = 19)

Weather · Maps & travel · Files · Time · Editor · Communication · Images · Media & devices · Users · Shapes · Alerts & feedback · General · Finance & eCommerce · Arrows · Development · Education · Security · Charts · Layout.

> ⚠ Notes ghi "19 categories" — đếm lại danh sách tên = **19** (đúng). (Ban đầu đếm nhầm "20 frame danh mục" gồm cả khối Notes.)

## 5. Featured icon (S1 — Misc icons)

Component set: `Featured icon outline`, `Featured icon`. Biến thể:

- **Size** = sm | md | lg | xl
- **Color** = Brand | Gray | Error | Warning | Success (thứ tự hàng: brand, gray, error, warning, success)
- **Type** = Light | … (4 nhóm Type trên canvas): (1) Light — vòng tròn nền nhạt + icon màu; (2) vòng tròn đặc màu + vòng sáng ngoài; (3) vuông bo góc đặc màu; (4) vuông nền trắng viền (2 hàng, không màu). Tên Type 2–4 **chưa đọc → `?`**.
- Icon mẫu `check-circle`; sm = khung chứa icon 16px lệch 8px (khối 32). Thuộc tính: Icon swap, Gradient mask (true).

## 6. Misc icons (S1 — trang Misc icons, 1025-31781) — cấu trúc

Integration icon, Country flag icons, Folder icon, File type icon, Ratings badge, Emoji, _Dot, Cursor, Check item text, App icons, Check icon, Star icon, Payment method icon, Featured icon outline, Featured icon, Social icon.
File type icon: nhiều biến thể theo đuôi file (pdf, doc, img…) và kiểu — chưa đếm.

## 7. Logos (S1 — trang Logos, 1083-118533) — cấu trúc

- `Company logo` (component Logo, Logomark — logo Untitled UI)
- `Placeholder company logos` (component Company logo; nền sáng và "Dark background" mode Dark)
- `Placeholder press logos` (Press logo)
- Notes (6721-165132): 90 logo công ty giả lưu thành color style dạng ảnh (Color styles → Avatar company logo) để đổi fill nhanh cho avatar/shape; logo hư cấu, dùng thương mại được, font từ Google Fonts/Fontshare. Căn logo cân thị giác: đặt mỗi logo trong frame (⌘⌥G), các frame cùng cao (gợi ý 48px), dùng ruler căn đỉnh/baseline/x-height, chỉnh từng 1px. Có link tải thêm 100+ logo trên Figma Community.

## 8. Luật dùng

| # | Luật | Nguồn |
|---|---|---|
| 1 | Icon tăng tốc thao tác khi dễ nhận ra; đặc biệt hữu ích trong UI dày thông tin (dashboard, SaaS); sidebar nav là ví dụ điển hình | S1 |
| 2 | Dùng icon "phổ quát" (home, menu, search, edit, heart/star, bookmark, share, download, settings, lock, upload, close, filter, link, log out) — không sáng tạo lại; chức năng trước, đẹp sau | S1 |
| 3 | Icon không thay chữ: nav chỉ có icon khó học; nếu chật chỗ thì dùng nav 2 tầng mở khi hover + tooltip. Mặc định ghép icon + nhãn; chỉ bỏ nhãn với icon phổ quát (search, help, delete, edit, save, link) | S1 |
| 4 | KHÔNG phóng to icon quá cỡ thiết kế: mặc định 24px, thiết kế để dùng 16–32px; ở 48px nét thành 4px, thô. Muốn nhấn mạnh → đặt icon trong khối lớn hơn (featured icon 48px) | S1 |
| 5 | Chọn một thư viện icon từ đầu và giữ nguyên; đủ lớn, nhất quán, hợp brand; trộn thư viện tạo nợ thiết kế | S1 |
| 6 | "Made for Figma": cấu trúc layer nhất quán để swap instance giữ override (màu fill, độ mờ, màu nét, độ dày nét). Duotone: layer "Icon" (stroke brand-700 2px) + layer "Fill" (brand-700, opacity 12%) | S1 |
| 7 | Tránh boolean group cho icon: khi export SVG bị outline → file ~4× (4KB vs 1KB), không sửa được stroke width; icon single-path giữ SVG tối ưu + stroke chỉnh được | S1 |
| 8 | Đổi màu bằng class text (vd `text-brand-600`), cỡ bằng `size-*`, nét bằng `strokeWidth`; icon trang trí đặt `aria-hidden="true"` | S3 |

## 9. Ghi chú

- Số icon chính xác từng style + tên Type 2–4 của Featured icon: S1 chưa đọc.
- Logo: chỉ ghi cấu trúc (theo spec) — xem mục 7.
