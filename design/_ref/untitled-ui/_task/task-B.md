# Task B — ghép dữ liệu S1 (Figma) đã đọc vào các file output

Đọc: `_task/spec.md` (mục 5, 6), `_task/s1-panel.md`, `_task/s1-semantic.tsv`, `_task/compare-report.txt`.
Chỉ sửa file trong `design/_ref/untitled-ui/`. Không commit. Không đọc Figma (đã có dữ liệu sẵn).

1. `02-colors-semantic.md`, bảng Text/Border/Foreground/Background:
   - Cột "Cách dùng": thay bằng mô tả trong s1-semantic.tsv (đã là lời diễn giải, giữ ≤25 từ, giữ tên component).
   - Cột Nguồn: `S1 · S2` cho token có trong cả hai, kèm node-id section (ghi trong tsv).
   - Lệch (compare-report.txt): ghi `⚠ lệch: S1=…, S2=…` ở cột Ghi chú. `text-white` (S1 ghi `text-white`, S2 `white`) KHÔNG tính là lệch — chỉ ghi chú nhẹ.
     Với bg-primary-solid: thêm ghi chú mô tả Figma nói "dark → bg-tertiary" (=neutral-800, khớp swatch S1).
     Với bg-brand-primary_alt, bg-brand-section: mô tả Figma nói "dark → bg-secondary" nhưng swatch Figma là neutral-800 trong khi bg-secondary dark = neutral-900 → ghi "Figma tự mâu thuẫn giữa mô tả và swatch".
   - Token S2 có mà S1 không có trong bảng tài liệu: fg-brand-secondary_hover, text-editor-icon-fg, text-editor-icon-fg_active, text-error-primary_hover → Ghi chú `không có trong bảng tài liệu Figma`. (Panel Variables Figma ghi group Text = 21, bảng tài liệu chỉ có 20 dòng.)
   - Mục `## Luật dùng`: thêm luật từ S1, ít nhất: border-secondary là viền mặc định của phần lớn component; border-secondary_alt chỉ cho menu nổi; text-placeholder dùng neutral-500 vì tương phản cao hơn 400; hậu tố `_on-brand` = dùng trên nền brand đặc; `_alt` = biến thể đổi hành vi ở dark mode (thường thành xám); `-solid` = nền đặc tối; fg-* chỉ cho phần tử không phải chữ (icon, chấm, thanh). Mỗi luật ghi nguồn S1 + node-id.
2. `tokens.untitled.json`: với các biến text/border/fg/bg khớp S1, điền `usage` (từ tsv) và `src` thêm "S1". Lệch thì thêm trường `"s1": {"Light":..,"Dark":..}` và `"mismatch": true`. Chạy lại `_task/verify_tokens.py` phải vẫn PASS.
3. `03-typography.md`: thêm dữ liệu text styles từ s1-panel.md (11 cỡ × 4 độ đậm = 44 style), so cỡ/dòng với S2, đánh dấu lệch nếu có.
4. `05-effects.md`: thêm danh sách tên effect style từ s1-panel.md (giá trị lớp S1 chưa đọc → `?` + "chưa đọc giá trị từng lớp trên Figma"). Liệt kê style S1 có mà S2 không (vd Portfolio mockups, Avatars, focus-ring-shadow-*, backdrop-blur-*).
5. `00-structure.md`: thêm collections + số biến từ s1-panel.md; so với S2.
6. `01-colors-primitives.md`: thêm mục S1 color styles (26 dải × 11 bậc + Base White/Black, gradient). Ghi rõ ⚠ lệch lớn: repo S2 dùng brand Untitled tím `#7f56d9` (dải untitled-*, có bậc 25) còn Figma v8 theo Tailwind v4.1 (bậc 50–950, 26 dải). Hex S1 chưa đọc.
7. README.md: cập nhật bảng độ phủ (cột "Số dòng thấy trên Figma": Text 20 (panel ghi 21), Border 8, Foreground 18, Background 28; còn lại `chưa đọc`), ghi số chỗ lệch S1↔S2 = 6 (+1 không tính: text-white), mục "Khối S1 chưa đọc": Color utility variables, Notes and documentation, Gradients (giá trị), hex primitives + nhãn WCAG, giá trị shadow/blur, Typography page notes, Spacing/radius/grids, Icons, Logos, Getting started. Ghi chú: theme.css hiện 753 dòng (spec ghi 834).

Khi xong in: file đã sửa, số token đã gắn S1, kết quả verify.
