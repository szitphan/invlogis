# S1 Icons — trang Icons (frame danh mục mỗi cái có mode "1. Color modes: Light mode")
20 frame danh mục (layer panel): Weather, Maps & travel, Files, Time, Editor, Communication, Images, Media & devices, Users, Shapes, Alerts & feedback, General, Finance & eCommerce, Arrows, Development, Education, Security, Charts, Layout (+ Notes). ⚠ Notes ghi "19 categories" nhưng trang có 20 frame danh mục (đếm: Weather, Maps & travel, Files, Time, Editor, Communication, Images, Media & devices, Users, Shapes, Alerts & feedback, General, Finance & eCommerce, Arrows, Development, Education, Security, Charts, Layout = 19 → khớp; danh sách trên có 19 tên).
Mẫu icon `activity` (General): component 24×24; lớp vector "Icon" 20×18 lệch top 3 left 2; nét (stroke) 2px, căn giữa (center), màu #000000 trong master (đổi màu khi dùng). Description của component chứa từ khóa tìm kiếm: "activity, heartbeat, heart rate, exercise, pulse".
Tên icon: kebab-case, biến thể đánh số `-01`, `-02` (vd edit-01…05, building-01…08, check-circle-broken), hậu tố hình dạng `-circle`, `-square`, `-hexagon`, `-octagon`, `-broken`.
Thư viện: Untitled UI Icons (line), 4.600+ icon cho bản PRO, 4 style (line, duocolor, duotone, solid); file Figma dùng bộ line; thay icon mặc định từ v2.8. Free: 1.100+ (theo docs S3 — xem 06-icons.md).

## Notes and documentation — trang Icons (node 6721-165473), luật dùng (diễn giải)
- Icon tăng tốc thao tác khi dễ nhận ra; đặc biệt có ích trong UI dày thông tin (dashboard, SaaS); sidebar nav là ví dụ điển hình.
- Dùng icon "phổ quát" (home, menu, search, edit, heart/star, bookmark, share, download, settings, lock, upload, close, filter, link, log out) — không sáng tạo lại; chức năng trước, đẹp sau.
- Icon không thay chữ: nav chỉ có icon khó học; nếu chật chỗ thì dùng nav 2 tầng mở khi hover + tooltip. Mặc định ghép icon + nhãn; chỉ bỏ nhãn với icon phổ quát (search, help, delete, edit, save, link).
- KHÔNG phóng to icon quá cỡ thiết kế: icon Untitled UI mặc định 24px, thiết kế để dùng 16–32px; ở 48px nét thành 4px, thô. Muốn nhấn mạnh → đặt icon trong khối lớn hơn (featured icon 48px).
- Chọn một thư viện icon từ đầu và giữ nguyên; đủ lớn, nhất quán, hợp brand; trộn thư viện tạo nợ thiết kế.
- "Made for Figma": cấu trúc layer nhất quán để khi swap instance Figma giữ override (màu fill, độ mờ fill, màu nét, độ dày nét). Duotone: layer "Icon" (stroke brand-700, 2px) + layer "Fill" (brand-700, opacity 12%). Mỗi tên layer chỉ có một layer trùng tên.
- Tránh boolean group cho icon: khi export SVG bị chuyển outline → file ~4× (4KB vs 1KB), không sửa được stroke width; icon single-path giữ SVG tối ưu và stroke chỉnh được.

## Misc icons (trang Misc icons, 1025-31781) — chỉ cấu trúc
Component set trên trang: Integration icon, Country flag icons, Folder icon, File type icon, Ratings badge, Emoji, _Dot, Cursor, Check item text, App icons, Check icon, Star icon, Payment method icon, Featured icon outline, Featured icon, Social icon.
Featured icon: biến thể `Size=sm|md|lg|xl` × `Color=Brand|Gray|Error|Warning|Success` (thứ tự hàng: brand, gray, error, warning, success) × `Type=Light|…`. Nhìn canvas có 4 nhóm Type: (1) Light — vòng tròn nền nhạt, icon màu; (2) vòng tròn đặc màu + vòng sáng ngoài; (3) vuông bo góc đặc màu; (4) vuông nền trắng viền (2 hàng, không màu) — tên Type 2–4 chưa đọc (?). Icon mẫu check-circle; sm = khung chứa icon 16px lệch 8px (khối 32). Thuộc tính component: Icon swap, Gradient mask (true).
File type icon: nhiều biến thể theo đuôi file (pdf, doc, img…) và kiểu — chưa đếm.

## Logos (trang Logos, 1083-118533) — chỉ cấu trúc
Frame: Company logo (component Logo, Logomark — logo Untitled UI), Placeholder company logos (component Company logo; nền sáng và "Dark background" mode Dark), Placeholder press logos (Press logo), Notes and documentation (6721-165132).
Notes (diễn giải): 90 logo công ty giả lưu thành color style dạng ảnh (Color styles → Avatar company logo) để đổi fill nhanh cho avatar/shape; logo hư cấu, dùng thương mại được, font lấy từ Google Fonts/Fontshare. Căn logo cho cân thị giác: đặt mỗi logo trong frame (⌘⌥G), cho các frame cùng cao (gợi ý 48px), dùng ruler căn đỉnh/baseline/x-height, chỉnh từng 1px tới khi trông đều; frame giữ khi export SVG. Có link tải thêm 100+ logo trên Figma Community.
