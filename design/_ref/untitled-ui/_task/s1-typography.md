# S1 Typography — trang Typography, frame 1023-36826; đọc panel khi chọn text mẫu (_Type scale base)
Font specimen ghi: Inter. Display dùng biến `Font family/font-family-display`, Text dùng `Font family/font-family-body` (giá trị biến chưa thấy trong panel; specimen = Inter).
Cỡ / dòng gắn biến `Font size/<tên>` và `Line height/<tên>`; paragraph spacing cũng gắn `Font size/<tên>` (= bằng cỡ chữ).
Độ đậm: Regular 400 · Medium (chưa xác nhận số; theo tên 500) · Semibold 600 (style "Semi Bold") · Bold 700.
| style | px (cỡ/dòng, từ panel Text styles) | letter-spacing |
|---|---|---|
| Display 2xl | 72/90 | -2% |
| Display xl | 60/72 | -2% |
| Display lg | 48/60 | -2% |
| Display md | 36/44 | -2% |
| Display sm | 30/38 | 0% |
| Display xs | 24/32 | 0% |
| Text xl | 20/30 | 0% |
| Text lg | 18/28 | 0% |
| Text md | 16/24 | 0% |
| Text sm | 14/20 | 0% |
| Text xs | 12/18 | 0% |
-2% × cỡ: 2xl −1.44px, xl −1.2px, lg −0.96px, md −0.72px (khớp mô tả repo ở spec mục 7).
Màu chữ mẫu: text-primary (900) = #171717 (= Tailwind neutral-900).

## Notes and documentation — trang Typography (node chứa 7436-524568), luật dùng (diễn giải)
- "Display" dành cho cỡ lớn/heading (H1–H6), không cho đoạn văn dài. "Text" dùng cho phần lớn chữ thông tin: body, label, UI element, cỡ nhỏ. Ví dụ ghép: tiêu đề Display md + đoạn Text xl + đoạn Text lg.
- Base font size = cỡ mặc định cho đoạn văn, label, menu, list; khuyến nghị 16px (Text md).
- Line height: body 1.5–2× cỡ chữ (vd 16 → 24). Chữ càng lớn line-height càng nhỏ: display ~1.2–1.25× (vd 60 → ~72). Thang đã thử trên nhiều dự án.
- Letter spacing: dùng cùng một typeface cho display và body thì nên siết tracking ở display (vd −2%) để dễ đọc ở cỡ lớn; đừng quá tay. Figma chỉ cho % hoặc px trong text style, không giống CSS → khi bàn giao nên đổi sang px hoặc tốt nhất rem/em (vd −0.2em); Dev Mode tự đổi sang rem/em. Variables Figma chưa hỗ trợ rem/em/% → line-height và letter-spacing động khó làm.
- Chọn font: bỏ qua phần lớn font mới; chọn font có ≥5 độ đậm (light, regular, medium, semibold, bold + italic); sans-serif trung tính là lựa chọn an toàn; xem font các công ty thiết kế tốt đang dùng (vd Stripe dùng Söhne). Tối đa 2 font, tốt nhất 1 font nhiều độ đậm.
- Đổi text style: quản lý bằng biến typography (single source of truth: font family, weight, size, line height) trong collection 6. Typography. Ảnh panel: Groups Font family 2, Font weight 8, Font size 11 (… tổng 32); font-family-display = Inter, font-family-body = Inter; font weight: regular, regular-italic, medium, medium-italic, semibold, … (8 biến); font size text-xs 12, text-sm 14, text-md 16, text-lg 18, text-xl 20, display-xs 24, display-sm 30, display-md 36, display-lg 48, …
- Cảnh báo của chính Untitled UI: biến typography (ra mắt 4/2024) làm chậm file khi sửa/thêm mode; họ khuyên tạm detach biến typography khỏi text style cho tới khi Figma sửa lỗi; v4.0 có 2 bản (dùng variables / dùng styles).
- Danh sách font gợi ý (chỉ ghi tên): miễn phí Inter, DM Sans, Work Sans, Space Grotesk, …; trả phí Suisse Int'l, Helvetica Neue, Graphik, Aeonik, Untitled Sans, Euclid Circular A, Neue Montreal, GT America, … (phần cuối danh sách không đọc hết — không phải token).
Đếm biến 6. Typography: Font family 2 + Font weight 8 + Font size 11 = 21; còn 11 → đoán là Line height 11 (chưa thấy trực tiếp, đánh dấu ?).
