# Task C — ghép toàn bộ dữ liệu Figma (S1) vào file output, hoàn tất bàn giao

Đọc trước: `_task/spec.md` (mục 5, 6, 8), rồi TẤT CẢ file `_task/s1-*.md` + `_task/s1-semantic.tsv` + `_task/compare-report.txt`.
Thư mục: `design/_ref/untitled-ui/` (đường dẫn tương đối trong repo). Chỉ sửa file trong thư mục này. Không commit.
Không đọc Figma. Không bịa: chỗ nào s1-*.md ghi `?`/"chưa đọc" thì giữ `?` + lý do.
Mục `## Luật dùng` trong mỗi file là phần đội cần nhất: viết luật dạng gạch đầu dòng ngắn, mỗi luật ghi nguồn (S1 + node-id nếu có / S2 / S3). Diễn giải bằng lời của bạn, không chép đoạn dài.

## 1. SỬA LỖI do task B
- `01-colors-primitives.md`: XOÁ khối "⚠ Lệch lớn S1↔S2 … brand #7f56d9 vs Tailwind v4.1". Sự thật (s1-colors.md): Figma Brand = tím Untitled, KHỚP repo (50 #F9F5FF … 600 #7F56D9 … 950 #2C1C5F). Các dải còn lại = màu Tailwind. Chỉ ghi lệch nếu so từng hex thấy khác (vd repo có bậc 25 cho brand, Figma không có → ghi chú).
- `README.md`: theme.css hiện **753 dòng** (spec cũ ghi 834) — sửa chỗ ghi 834.

## 2. Ghép S1 vào từng file
- `00-structure.md`: cấu trúc trang file Figma (s1-structure.md), quy ước đặt tên (❖ nhóm, ↳ trang con, tiền tố `_` cho component nội bộ, Notes "you can delete this"), collections + số biến + nhóm (s1-panel.md, s1-effects.md: Color modes 274 = Colors 100 [Text 21, Border 8, Foreground 19, Background ?] + Effects 23 + Component colors 174; _Primitives 343 = Colors 311 + Spacing 32), Getting started (cách dùng kit, tách library, biến là nguồn sự thật), HƯỚNG DẪN ĐỔI MÀU BRAND (s1-colors.md mục ★).
- `01-colors-primitives.md`: bảng đầy đủ 27 dải (Base, Brand, 17 sắc, 9 xám) × bậc: cột `Dải | Bậc | Hex (S1) | Nhãn WCAG (S1) | Hex S2/Tailwind (nếu file đang có) | Ghi chú`. Ghi chú Neutral = xám mặc định; mô tả dải; nhãn WCAG A/AA/AAA; lỗi nhãn Lime-50 "AAA 4.82". Gradients (s1-colors.md). Luật dùng màu (neutral/brand/accent/feedback, 8–12 sắc xám, WCAG 2.2 cấp A/AA/AAA, ≥4.5:1).
- `02-colors-semantic.md`: thêm Alpha colors S1 (20 biến) và Utility colors S1 (118) so với S2 (134): lệch tên error/warning/success vs red/yellow/green, S2 thừa amber + emerald, lỗi tên "utility-brand_alt". Giữ nguyên phần task B đã làm (kiểm lại các ô ⚠).
- `03-typography.md`: s1-typography.md — font Inter (display + body), letter-spacing −2% cho Display 2xl–md, 0% còn lại, độ đậm 400/500/600/700, biến typography, luật dùng (Display vs Text, base 16px, line-height, tracking, chọn font, cảnh báo biến typography).
- `04-spacing-radius-grid.md`: s1-spacing.md — spacing primitives 32 bậc, spacing semantic 17, widths 11 + paragraph-max-width, containers 3, radius 11 (so với S3 radius 10 → ghi lệch nếu khác), grid desktop/tablet/mobile, luật dùng (soft grid 4px, bội số 8, ngoại lệ button lg, padding icon, 45–85 ký tự, 720px).
- `05-effects.md`: s1-effects.md — bảng shadow từng lớp (x,y,blur,spread,màu,độ mờ) đủ 15 lớp, focus ring 7 style, backdrop blur 4; so với S2 shadow (đánh dấu ⚠ lệch từng lớp nếu khác); ghi lệch nội bộ focus-ring-shadow-sm; màu bóng là biến (Dark chưa đọc → `?`). Luật dùng skeuomorphic/focus ring.
- `06-icons.md`: s1-icons.md — icon 24px, stroke 2px, 20 danh mục (đếm lại theo danh sách tên), đặt tên, mô tả từ khoá, Featured icon (Size/Color/Type), Misc icons, Logos; luật dùng icon.
- `tokens.untitled.json`: thêm collection/biến S1 còn thiếu với `src:["S1"]` (hoặc thêm "S1" vào src nếu đã có): primitives màu S1 (hex), alpha S1, utility S1, spacing/widths/containers/radius S1, shadow/focus/blur S1, text style S1. Lệch → `"mismatch": true` + `"s1": {...}`. Sau đó cập nhật `_task/verify_tokens.py` để vẫn kiểm được phần S2 (378 biến S2 phải còn nguyên) và in thêm số biến S1. Chạy, phải PASS.

## 3. README.md (theo spec mục 6)
- Bảng độ phủ: `Trang | Khối | Số dòng token đã lấy | Số dòng thấy trên Figma | Đủ?` — điền số thật từ s1-*.md cho mọi khối.
- Đối chiếu S1↔S2: tổng số chỗ lệch (liệt kê ngắn từng chỗ).
- Mẫu ngẫu nhiên 10 token: để mục `## Kiểm mẫu ngẫu nhiên` với bảng trống 10 dòng `Token | Giá trị file | Đọc lại Figma | Khớp?` và ghi "điền bởi phiên Claude" (Claude sẽ điền).
- Khối không đọc được / chưa đọc: shadow ở Dark mode, stop gradient Linear 02–33, skeuemorphic-gradient-border, tên Type 2–4 của Featured icon, giá trị biến Line height (6. Typography), How to master variants/Auto Layout (hướng dẫn Figma, không có token).
- Frontmatter mọi .md: `updated: 2026-10-26`, `links:` có link Figma.

Khi xong in ra: danh sách file đã sửa, số biến S1 trong json, tổng số lệch S1↔S2, kết quả verify.
