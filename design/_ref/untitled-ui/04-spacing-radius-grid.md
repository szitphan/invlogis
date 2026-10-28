---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Spacing, radius & grids, node 5245-372830)
  - https://github.com/untitleduico/react (styles/theme.css)
  - https://www.untitledui.com/react/docs/installation
---

# 04 — Spacing · Radius · Grid

> Nguồn: S1 (Figma) + S2 (theme.css) + S3 (docs installation).

## 1. Spacing primitives (S1 — collection `_Primitives` → Spacing, 32 bậc)

Thang spacing số theo tỉ lệ, 1 đơn vị = 0.25rem = 4px (vd 16px gấp đôi 8px nên tên là 4 và 2). Có thể sửa biến để đổi thang mặc định.

| name → px (16px base) | | name → px | | name → px |
|---|---|---|---|---|
| 0 → 0 | 2 → 8 | 5 → 20 | 32 → 128 | 120 → 480 |
| 0.5 → 2 | 3 → 12 | 6 → 24 | 40 → 160 | 140 → 560 |
| 1 → 4 | 4 → 16 | 8 → 32 | 48 → 192 | 160 → 640 |
| 1.5 → 6 | 10 → 40 | 12 → 48 | 56 → 224 | 180 → 720 |
| — | — | 16 → 64 | 64 → 256 | 192 → 768 |
| — | — | 20 → 80 | 80 → 320 | 256 → 1024 |
| — | — | 24 → 96 | 96 → 384 | 320 → 1280 · 360 → 1440 · 400 → 1600 · 480 → 1920 |

## 2. Spacing semantic (S1 — collection 3. Spacing, 17 biến)

Thang giới hạn, suy từ primitive, dùng cho gap/padding/margin trong component và thiết kế.

| Token | Giá trị | | Token | Giá trị |
|---|---|---|---|---|
| `spacing-none` | 0rem (0) | | `spacing-3xl` | 1.5rem (24) |
| `spacing-xxs` | 0.125rem (2) | | `spacing-4xl` | 2rem (32) |
| `spacing-xs` | 0.25rem (4) | | `spacing-5xl` | 2.5rem (40) |
| `spacing-sm` | 0.375rem (6) | | `spacing-6xl` | 3rem (48) |
| `spacing-md` | 0.5rem (8) | | `spacing-7xl` | 4rem (64) |
| `spacing-lg` | 0.75rem (12) | | `spacing-8xl` | 5rem (80) |
| `spacing-xl` | 1rem (16) | | `spacing-9xl` | 6rem (96) |
| `spacing-2xl` | 1.25rem (20) | | `spacing-10xl` | 8rem (128) · `spacing-11xl` 10rem (160) |

## 3. Widths (S1 — collection 4. Widths, 12 biến)

Độ rộng cố định suy từ primitive, để đặt max-width cho section nội dung chữ và page heading.

| Token | Giá trị | | Token | Giá trị |
|---|---|---|---|---|
| `width-xxs` | 20rem (320) | | `width-xl` | 48rem (768) |
| `width-xs` | 24rem (384) | | `width-2xl` | 64rem (1024) |
| `width-sm` | 30rem (480) | | `width-3xl` | 80rem (1280) |
| `width-md` | 35rem (560) | | `width-4xl` | 90rem (1440) |
| `width-lg` | 40rem (640) | | `width-5xl` | 100rem (1600) · `width-6xl` 120rem (1920) |

`paragraph-max-width` = 45rem (720) — chữ đoạn có max-width riêng để độ dài dòng tối ưu, đổi được một chỗ (thuộc collection 4. Widths theo đếm).

## 4. Containers (S1 — collection 5. Containers, 3 biến)

Chỉ dùng cho padding và max-width của container, tách khỏi width/spacing thường để đổi nhanh toàn bộ thiết kế.

| Token | Giá trị |
|---|---|
| `container-padding-mobile` | 1rem (16) |
| `container-padding-desktop` | 2rem (32) |
| `container-max-width-desktop` | 80rem (1280) |

## 5. Radius (S1 — collection 2. Radius, 11 biến)

Bo góc cho ảnh, button, mọi phần tử; hệ radius giới hạn suy từ primitive spacing.

| Token | Giá trị | | Token | Giá trị |
|---|---|---|---|---|
| `radius-none` | 0 | | `radius-lg` | 0.625rem (10) |
| `radius-xxs` | 0.125rem (2) | | `radius-xl` | 0.75rem (12) |
| `radius-xs` | 0.25rem (4) | | `radius-2xl` | 1rem (16) |
| `radius-sm` | 0.375rem (6) | | `radius-3xl` | 1.25rem (20) |
| `radius-md` | 0.5rem (8) | | `radius-4xl` | 1.5rem (24) · `radius-full` 9999px |

⚠ Lệch S1↔S3: S1 có **11** bậc, S3 docs có **10** (không có `xxs` + `4xl`, có thêm `DEFAULT`). Thang giá trị cũng khác:
S1 `sm`=6px (S3 4px), S1 `md`=8px (S3 6px), S1 `lg`=10px (S3 8px), S1 `3xl`=20px (S3 24px). Repo (S2) không khai `--radius-*`.

## 6. Grid layouts (S1 — frame 5245-373008, đọc thước đo đỏ)

Grid tạo cấu trúc, thứ bậc, nhịp; bật/tắt bằng Shift+G.

| Grid | Khung | Lề trái/phải | Rãnh | Số cột | Vùng nội dung | Cột suy ra |
|---|---|---|---|---|---|---|
| Desktop | 1280 (trong MacBook 1440) | 32 | 32 | 12 | 1216 | (1216−11×32)/12 = 72 |
| Tablet | 768 | 32 | 32 | 6 | 704 | (704−5×32)/6 ≈ 90.7 |
| Mobile | 375 (iPhone) | 16 | 16 | 4 | 343 | (343−3×16)/4 = 73.75 |

- Lề khớp `container-padding-desktop` 32 / `container-padding-mobile` 16.
- Grid cột "auto" (layout guide styles): 12 / 6 / 5 / 3 / 2 columns — dùng chia cột bên trong khối (giá trị rãnh chưa đọc).
- Container mẫu: radius-2xl, viền 1px `border-primary` = #D4D4D4 (Tailwind neutral-300), nền `bg-primary`.

## 7. Luật dùng

| # | Luật | Nguồn |
|---|---|---|
| 1 | Hệ spacing cố định giúp nhanh, nhất quán, bớt đoán; không có hệ → giá trị lộn xộn, dev không làm đúng | S1 |
| 2 | Dùng "soft grid" 4px (không phải hard grid 8px): mọi khoảng cách chia hết cho 4 nhưng vẫn khớp lưới 8px | S1 |
| 3 | Giới hạn tập giá trị: chọn bậc định sẵn (vd 128 thay vì 124); thang 0 → 1920px | S1 |
| 4 | Chấp nhận ngoại lệ, nhất là component có chữ (Button md 40/lg 44/xl 48 cao; Button lg padding dọc 10px vì icon 20px) | S1 |
| 5 | Button có icon: padding trái giảm 2px (16→14) vì icon có ~2px khung đệm → cân bằng thị giác | S1 |
| 6 | Ưu tiên bội số 8px; dùng 4px khi cần tinh chỉnh; căn thẳng hàng dọc/ngang | S1 |
| 7 | Độ dài dòng đoạn văn lý tưởng ~45–85 ký tự (85–105 quá dài); đặt max-width toàn cục, mặc định 720px (= paragraph-max-width) | S1 |
| 8 | Base spacing = 4px (`--spacing` = 0.25rem) | S2 |
| 9 | Container tối đa 1280px | S2 |
| 10 | Mẹo Figma: đổi "Big nudge" 10→8px để Shift+mũi tên đi đúng lưới 8 | S1 |

## 8. Ghi chú

- Đủ 32 spacing primitive + 17 semantic + 12 width + 3 container + 11 radius trong `tokens.untitled.json` (các collection `(S1)`).
- Radius: repo (S2) thiếu → bản Figma v8 có 11 bậc (khác 10 bậc của docs S3).
- Breakpoint chỉ khai 2 mốc trong repo (320/600); phần còn lại dùng default Tailwind v4.
