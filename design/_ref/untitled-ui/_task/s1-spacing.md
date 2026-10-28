# S1 Spacing, radius & grids

## Spacing primitives (frame 6300-76782) — nằm trong collection _Primitives
Mô tả: thang spacing số theo tỉ lệ, 1 đơn vị = 0.25rem = 4px (vd 16px gấp đôi 8px nên tên là 4 và 2). Có thể sửa biến để đổi thang mặc định.
name → rem → px (16px base), 32 bậc:
0 0rem 0 · 0.5 0.125rem 2 · 1 0.25rem 4 · 1.5 0.375rem 6 · 2 0.5rem 8 · 3 0.75rem 12 · 4 1rem 16 · 5 1.25rem 20 · 6 1.5rem 24 · 8 2rem 32 · 10 2.5rem 40 · 12 3rem 48 · 16 4rem 64 · 20 5rem 80 · 24 6rem 96 · 32 8rem 128 · 40 10rem 160 · 48 12rem 192 · 56 14rem 224 · 64 16rem 256 · 80 20rem 320 · 96 24rem 384 · 120 30rem 480 · 140 35rem 560 · 160 40rem 640 · 180 45rem 720 · 192 48rem 768 · 256 64rem 1024 · 320 80rem 1280 · 360 90rem 1440 · 400 100rem 1600 · 480 120rem 1920

## Spacing (frame 5245-372881) — collection 3. Spacing (17 biến, khớp panel)
Mô tả: thang giới hạn, suy ra từ primitive, dùng cho gap, padding, margin trong component và thiết kế.
spacing-none 0rem 0 · spacing-xxs 0.125rem 2 · spacing-xs 0.25rem 4 · spacing-sm 0.375rem 6 · spacing-md 0.5rem 8 · spacing-lg 0.75rem 12 · spacing-xl 1rem 16 · spacing-2xl 1.25rem 20 · spacing-3xl 1.5rem 24 · spacing-4xl 2rem 32 · spacing-5xl 2.5rem 40 · spacing-6xl 3rem 48 · spacing-7xl 4rem 64 · spacing-8xl 5rem 80 · spacing-9xl 6rem 96 · spacing-10xl 8rem 128 · spacing-11xl 10rem 160

## Widths — collection 4. Widths (11 + paragraph-max-width = 12, khớp panel)
Mô tả: độ rộng cố định suy từ primitive, để đặt max-width cho section như nội dung chữ và page heading.
width-xxs 20rem 320 · width-xs 24rem 384 · width-sm 30rem 480 · width-md 35rem 560 · width-lg 40rem 640 · width-xl 48rem 768 · width-2xl 64rem 1024 · width-3xl 80rem 1280 · width-4xl 90rem 1440 · width-5xl 100rem 1600 · width-6xl 120rem 1920

## Containers — collection 5. Containers (3, khớp panel)
Mô tả: chỉ dùng cho padding và max-width của container, tách khỏi width/spacing thường để đổi nhanh kích thước container toàn bộ thiết kế.
container-padding-mobile 1rem 16 · container-padding-desktop 2rem 32 · container-max-width-desktop 80rem 1280

## Paragraph max-widths
Mô tả: chữ đoạn (vd blog post) có max-width riêng để độ dài dòng tối ưu cho đọc, đổi được một chỗ.
paragraph-max-width 45rem 720 (thuộc collection 4. Widths theo đếm)

## Radius (frame 5253-372274) — collection 2. Radius (11, khớp panel)
Mô tả: bo góc cho ảnh, button, mọi phần tử; hệ radius giới hạn suy từ primitive spacing.
radius-none 0 · radius-xxs 0.125rem 2 · radius-xs 0.25rem 4 · radius-sm 0.375rem 6 · radius-md 0.5rem 8 · radius-lg 0.625rem 10 · radius-xl 0.75rem 12 · radius-2xl 1rem 16 · radius-3xl 1.25rem 20 · radius-4xl 1.5rem 24 · radius-full ∞ 9999px

## Grid layouts (frame 5245-373008) — đọc thước đo đỏ trên canvas
Mô tả: grid tạo cấu trúc, thứ bậc, nhịp; bật/tắt bằng Shift+G.
| Grid | khung | lề trái/phải | rãnh | số cột | vùng nội dung | ghi chú |
|---|---|---|---|---|---|---|
| Desktop | 1280 (container trong khung MacBook 1440, padding spacing-8xl/9xl) | 32 | 32 | 12 | 1216 | cột suy ra = (1216−11×32)/12 = 72 |
| Tablet | 768 (frame width-xl) | 32 | 32 | 6 | 704 | cột suy ra = (704−5×32)/6 ≈ 90.7 |
| Mobile | 375 (iPhone) | 16 | 16 | 4 | 343 | cột suy ra = (343−3×16)/4 = 73.75 |
Số cột suy từ số thước rãnh (Desktop 13 thước = 2 lề + 11 rãnh; Tablet 7 = 2 + 5; Mobile 5 = 2 + 3). Lề khớp container-padding-desktop 32 / container-padding-mobile 16.
Grid cột "auto" (layout guide styles): 12 / 6 / 5 / 3 / 2 columns (auto) — dùng chia cột bên trong khối; giá trị rãnh chưa đọc.
Container mẫu: radius-2xl, viền 1px border-primary = #D4D4D4 (= Tailwind neutral-300), nền bg-primary.

## Notes and documentation — trang Spacing, radius & grids (node 5245-372830), luật dùng (diễn giải)
- Hệ spacing cố định giúp làm nhanh, nhất quán, bớt đoán; tạo nhịp đều. Không có hệ → giá trị lộn xộn (20/23/25/5/21/35/15px), dev không thể làm đúng.
- Dùng "soft grid" 4px (không phải hard grid 8px): mọi khoảng cách chia hết cho 4 nhưng vẫn khớp lưới 8px. Ví dụ đúng: card padding 24, avatar↔heading 16, heading↔text 2, text↔content 20, list items 12, content↔action 32, action top padding 24, button padding 12.
- Giới hạn tập giá trị: chọn bậc định sẵn (vd 128 thay vì 124) — thang từ 0 đến 1920px.
- Không phải mọi thứ đều khớp 4px; chấp nhận ngoại lệ, nhất là component có chữ. Ví dụ: Button md 40, lg 44, xl 48 cao; Button lg cần padding dọc 10px (icon 20px) — không khớp 4px nhưng chấp nhận.
- Button có icon: padding trái giảm 2px (16→14) vì icon có ~2px khung đệm → cân bằng thị giác ("optically balanced").
- Best practices: ưu tiên bội số 8px (tưởng tượng lưới 8×8); dùng 4px khi cần tinh chỉnh; căn thẳng hàng dọc và ngang; định nghĩa tập spacing riêng và dùng khắp component/layout.
- Độ dài dòng đoạn văn: lý tưởng ~45–85 ký tự (55–70 và 70–85 đều OK; 85–105 là quá dài). Đặt max-width toàn cục; Untitled UI mặc định 720px (= paragraph-max-width).
- Mẹo Figma: đổi "Big nudge" 10→8px (Preferences → Nudge amount) để Shift+mũi tên đi đúng lưới 8.
