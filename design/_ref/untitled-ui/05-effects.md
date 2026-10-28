---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Effect styles — panel Properties)
  - https://github.com/untitleduico/react (styles/theme.css)
---

# 05 — Effects (shadow / focus ring / backdrop blur)

> Nguồn: S1 (Figma panel Properties — đọc từng lớp khi chọn card) + S2 (theme.css).
> Màu bóng là **biến** `Colors/Effects/Shadows/<name>_NN` (collection 1. Color modes → có thể khác ở Dark;
> giá trị Dark **chưa đọc → `?`**). Light = `#000000` + độ mờ.

## 1. Shadows (S1 — đủ 15 lớp của 7 style)

Card `_Shadow card` 256×240, radius-xl, border 1px `border-secondary_alt` (#000 10%), padding spacing-3xl, fill bg-primary.
Mọi lớp: drop shadow, "Behind transparent areas: True".

| Style | Lớp | x | y | blur | spread | Màu (biến) | Light |
|---|---|---|---|---|---|---|---|
| `shadow-xs` | 1 | 0 | 1 | 2 | 0 | `shadow-xs` | #000 5% |
| `shadow-sm` | 1 | 0 | 1 | 2 | −1 | `shadow-sm_02` | #000 10% |
| `shadow-sm` | 2 | 0 | 1 | 3 | 0 | `shadow-sm_01` | #000 10% |
| `shadow-md` | 1 | 0 | 2 | 4 | −2 | `shadow-md_02` | #000 6% |
| `shadow-md` | 2 | 0 | 4 | 6 | −1 | `shadow-md_01` | #000 10% |
| `shadow-lg` | 1 | 0 | 2 | 2 | −1 | `shadow-lg_03` | #000 4% |
| `shadow-lg` | 2 | 0 | 4 | 6 | −2 | `shadow-lg_02` | #000 3% |
| `shadow-lg` | 3 | 0 | 12 | 16 | −4 | `shadow-lg_01` | #000 8% |
| `shadow-xl` | 1 | 0 | 3 | 3 | −1.5 | `shadow-xl_03` | #000 4% |
| `shadow-xl` | 2 | 0 | 8 | 8 | −4 | `shadow-xl_02` | #000 3% |
| `shadow-xl` | 3 | 0 | 20 | 24 | −4 | `shadow-xl_01` | #000 8% |
| `shadow-2xl` | 1 | 0 | 4 | 4 | −2 | `shadow-2xl_02` | #000 4% |
| `shadow-2xl` | 2 | 0 | 24 | 48 | −12 | `shadow-2xl_01` | #000 18% |
| `shadow-3xl` | 1 | 0 | 5 | 5 | −2.5 | `shadow-3xl_02` | #000 4% |
| `shadow-3xl` | 2 | 0 | 32 | 64 | −12 | `shadow-3xl_01` | #000 14% |

**So S2 (theme.css): khớp 100%** — đã so từng lớp 15/15, không có lệch. (S2 gộp lớp thành chuỗi CSS,
vd `shadow-2xl` = `0px 24px 48px -12px rgba(0,0,0,0.18), 0px 4px 4px -2px rgba(0,0,0,0.04)`.)

Biến màu bóng (ảnh panel Variables, group Effects 23): `shadow-xs` 5%, `shadow-sm_01` 10%, `shadow-sm_02` 10%,
`shadow-md_01` 10%, `shadow-md_02` 6%, `shadow-lg_01` 8%, `lg_02` 3%, `lg_03` 4%, `xl_01` 8%, `xl_02` 3%,
`xl_03` 4%, `2xl_01` 18% (khớp giá trị đọc ở card). Dark mode giá trị chưa đọc (`?`).

## 2. Focus rings (S1 — 7 style, frame 5424-398991)

Focus ring đơn lớp cho phần tử không cần shadow (toggles, checkboxes). Phần tử cần ring + shadow (buttons)
→ ring gộp sẵn với shadow style. Ring = spread 4 màu brand ngoài + spread 2 màu bg-primary (khoảng hở trắng).

| Style | Lớp (x y blur spread · màu) |
|---|---|
| `focus-ring` | 0 0 0 4 · `focus-ring` #9E77ED (=brand-500) ; 0 0 0 2 · `bg-primary` #FFFFFF |
| `focus-ring-error` | 0 0 0 4 · `focus-ring-error` #EF4444 (=red-500) ; 0 0 0 2 · `bg-primary` #FFFFFF |
| `focus-ring-shadow-xs` | ring 4 brand + gap 2 bg-primary ; 0 1 2 0 · `shadow-xs` #000 5% |
| `focus-ring-shadow-sm` | ring 4 brand + gap 2 ; 0 1 2 0 · `shadow-sm_02` #000 10% ; 0 1 3 0 · `shadow-sm_01` #000 10% |
| `focus-ring-error-shadow-xs` | ring 4 red + gap 2 ; 0 1 2 0 · `shadow-xs` 5% |
| `focus-ring-shadow-xs-skeuomorphic` | ring 4 brand + gap 2 ; 0 1 2 0 shadow-xs 5% ; 0 −2 0 0 · `shadow-skeumorphic-inner` #000 5% ; 0 0 0 1 · `shadow-skeumorphic-inner-border` #000 18% |
| `focus-ring-error-shadow-xs-skeuomorphic` | như trên, ring red-500 |

⚠ Lệch nội bộ: `focus-ring-shadow-sm` dùng lớp `shadow-sm_02` **spread 0**, còn style `shadow-sm` độc lập dùng spread **−1**.
⚠ Tên biến có lỗi chính tả gốc "skeumorphic" (thiếu chữ o). Panel không ghi loại inner/drop cho lớp y=−2 và spread 1 (theo tên "inner" → bóng trong).
⚠ `focus-ring` dùng #9E77ED = brand-500 kiểu Untitled (không phải Tailwind violet-500 #8b5cf6).

## 3. Backdrop blurs (S1 — 4 bậc)

| Style | Blur |
|---|---|
| `backdrop-blur-sm` | 8 |
| `backdrop-blur-md` | 16 |
| `backdrop-blur-lg` | 24 |
| `backdrop-blur-xl` | 40 |

Card mẫu (sm): fill #FFFFFF 60%, viền 1px #FFFFFF 50%, radius-xl, padding spacing-4xl, cao 320, min-width 800 → kiểu glass trên ảnh nền.

## 4. Danh sách effect style trên Figma (S1 — panel Properties)

| Nhóm | Tên style | Có trong S2? |
|---|---|---|
| Shadows | `shadow-xs`, `shadow-xs-skeuomorphic`, `shadow-sm`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, `shadow-3xl` | có (theme.css) |
| Portfolio mockups | `shadow-main-centre-md`, `shadow-main-centre-lg`, `shadow-overlay-right-lg`, `shadow-overlay-left-lg`, `shadow-grid-md` | **không** (S2 dùng `shadow-modern-mockup-*`, khác tên) |
| Avatars | `Avatar inner shadow`, `Avatar icon` | **không** |
| Focus rings | `focus-ring`, `focus-ring-shadow-xs`, `focus-ring-shadow-xs-skeuomorphic`, `focus-ring-shadow-sm`, `focus-ring-error`, `focus-ring-error-shadow-xs`, `focus-ring-error-shadow-xs-skeuomorphic` | `focus-ring`/`focus-ring-error` có (dạng màu); `focus-ring-shadow-*` **không** |
| Backdrop blurs | `backdrop-blur-sm`, `-md`, `-lg`, `-xl` | **không** |

## 5. Luật dùng

| # | Luật | Nguồn |
|---|---|---|
| 1 | Thang shadow 7 bậc `xs…3xl`, độ cao tăng dần (xs=1px → 3xl=32px), mỗi bậc 2–3 lớp | S1 · S2 |
| 2 | Buttons + featured icons chuyển sang kiểu **skeuomorphic nhẹ** (v5.0; flat = v4.0): drop shadow + inner shadow + linear stroke + fill; cố tình rất nhẹ, không phá accessibility | S1 |
| 3 | Bỏ skeuomorphic dễ: effect style riêng; đổi master component (vd `shadow-xs-skeuomorphic` → `shadow-xs`) | S1 |
| 4 | Focus ring = "focus indicator" cho người không dùng chuột; Figma không gắn nhiều stroke → làm bằng box-shadow effect style; kết hợp shadow (`focus-ring-shadow-*`) để không mất bóng nâng | S1 |
| 5 | Màu effect gắn biến màu → đổi biến là shadow/focus ring tự cập nhật | S1 |
| 6 | Hạn chế Figma: không tách biến khỏi độ mờ → không alias được primitive với nhiều alpha; biến shadow là màu riêng, phải cập nhật tay. Mặc định mọi shadow dùng đen #000 + độ mờ, không phụ thuộc dải xám đang dùng | S1 |
| 7 | `shadow-xl` là bóng chuẩn cho modal/dialog | S3 upgrade |

## 6. Ghi chú

- Đủ 15 lớp bóng + 7 focus ring + 4 blur trong `tokens.untitled.json` (các collection `(S1)`).
- S2 có thêm `shadow-skeuomorphic` (viền trong 1px 0.18 + nét sáng −2px 0.05) và `shadow-xs-skeuomorphic` — S1 đọc ở focus ring, không đọc thành style shadow riêng.
- Màu mockup S2 dùng `#0a0d12` (khác bóng thường dùng black) — S1 portfolio mockups chưa đọc giá trị.
