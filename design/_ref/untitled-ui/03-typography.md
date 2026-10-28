---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Typography, frame 1023-36826)
  - https://github.com/untitleduico/react (styles/theme.css, styles/typography.css)
  - https://www.untitledui.com/react/docs/typography
---

# 03 — Typography

> Cỡ/dòng/độ đậm/letter-spacing. Nguồn: S1 (Figma) + S2 (theme.css + typography.css) + S3 (docs).

## 1. Font family

- **Inter** cho cả body và display (S1 specimen + S2). Được Rasmus Andersson thiết kế, miễn phí, 9 độ đậm + italic + variable font.
- Biến Figma (S1): `Font family/font-family-display` = Inter · `Font family/font-family-body` = Inter.

| Token | Giá trị | Nguồn |
|---|---|---|
| `--font-body` | `var(--font-inter, "Inter"), -apple-system, "Segoe UI", Roboto, Arial, sans-serif` | S2 |
| `--font-display` | `var(--font-inter, "Inter"), -apple-system, "Segoe UI", Roboto, Arial, sans-serif` | S2 |
| `--font-mono` | `ui-monospace, "Roboto Mono", SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace` | S2 |

## 2. Text scale (cỡ / dòng / letter-spacing)

`--spacing = 0.25rem = 4px` (Tailwind default) → mọi cỡ = `calc(var(--spacing) * N)`.

Letter-spacing (S1, panel khi chọn `_Type scale base`): Display **2xl–md = −2%**, các cỡ còn lại **0%**.

| Style | Cỡ (px) | Line-height (px) | Letter-spacing (S1) | Độ đậm (×4) | So S2 |
|---|---|---|---|---|---|
| Display 2xl | 72 | 90 | −2% (−1.44px) | Regular/Medium/Semibold/Bold | khớp |
| Display xl | 60 | 72 | −2% (−1.2px) | Regular/Medium/Semibold/Bold | khớp |
| Display lg | 48 | 60 | −2% (−0.96px) | Regular/Medium/Semibold/Bold | khớp |
| Display md | 36 | 44 | −2% (−0.72px) | Regular/Medium/Semibold/Bold | khớp |
| Display sm | 30 | 38 | 0% | Regular/Medium/Semibold/Bold | khớp |
| Display xs | 24 | 32 | 0% | Regular/Medium/Semibold/Bold | khớp |
| Text xl | 20 | 30 | 0% | Regular/Medium/Semibold/Bold | khớp |
| Text lg | 18 | 28 | 0% | Regular/Medium/Semibold/Bold | khớp |
| Text md | 16 | 24 | 0% | Regular/Medium/Semibold/Bold | khớp |
| Text sm | 14 | 20 | 0% | Regular/Medium/Semibold/Bold | khớp |
| Text xs | 12 | 18 | 0% | Regular/Medium/Semibold/Bold | khớp |

> 11 cỡ × 4 độ đậm = 44 text style (S1 panel Properties). Cỡ/dòng khớp 100% S2.
> Cỡ/dòng gắn biến `Font size/<tên>` + `Line height/<tên>`; paragraph spacing cũng gắn `Font size/<tên>` (= cỡ chữ).

## 3. Font weight

| Độ đậm | Giá trị | Nguồn |
|---|---|---|
| Regular | 400 | S1 |
| Medium | 500 (S1 panel: Text lg/Medium weight 500) | S1 |
| Semibold | 600 (style "Semi Bold") | S1 |
| Bold | 700 | S1 |

S2: theme.css không khai token `--font-weight-*` (dùng weight utility Tailwind). Trong typography.css: headings `600`, blockquote `500`, inline code `700`, `h1 strong` `900` → `h4 strong` `700`.

## 4. Biến typography (S1 — collection 6. Typography, 32 biến)

| Nhóm | Số biến | Giá trị |
|---|---|---|
| Font family | 2 | `font-family-display` = Inter · `font-family-body` = Inter |
| Font weight | 8 | regular, regular-italic, medium, medium-italic, semibold, … |
| Font size | 11 | text-xs 12, text-sm 14, text-md 16, text-lg 18, text-xl 20, display-xs 24, display-sm 30, display-md 36, display-lg 48, … |
| Line height | 11 (`?` — chưa đọc trực tiếp, đoán từ 32 − 21) | — |

> Biến typography là single source of truth: font family, weight, size, line height.
> ⚠ Cảnh báo của chính Untitled UI: biến typography (ra mắt 4/2024) làm chậm file khi sửa/thêm mode;
> họ khuyên tạm **detach biến typography khỏi text style** cho tới khi Figma sửa lỗi. v4.0 có 2 bản (dùng variables / dùng styles).

## 5. Typography styles (`.prose`) — S2 typography.css + S3 docs

Kiểu prose cho nội dung dài (article/docs), extends `@tailwindcss/typography`. Ánh xạ heading → display/text:

| Element | Cỡ dùng | Weight |
|---|---|---|
| `h1` | `--text-display-sm` (30/38) | 600 |
| `h2` | `--text-display-xs` (24/32) | 600 |
| `h3` | `--text-xl` (20/30) | 600 |
| `h4` | `--text-lg` (18/28) | 600 |
| `blockquote p` | `--text-xl` | 500 · italic |
| `code` (inline) | 0.875rem / 1.25rem | 700 |

Màu prose trỏ về semantic (S2): body/lead/links/captions → `text-tertiary`; headings/bold/quotes → `text-primary`; hr/td-borders → `border-secondary`; th-borders → `border-primary`; quote-borders → `fg-brand-primary_alt`; pre-bg → `bg-primary`.

## 6. Luật dùng

| # | Luật | Nguồn |
|---|---|---|
| 1 | Body & display dùng chung font **Inter** | S1 · S2 |
| 2 | "Display" dành cho cỡ lớn/heading (H1–H6), không cho đoạn dài; "Text" cho body, label, UI element, cỡ nhỏ | S1 |
| 3 | Base font size = 16px (Text md) — cỡ mặc định cho đoạn, label, menu, list | S1 |
| 4 | Line-height: body 1.5–2× cỡ (vd 16→24); chữ càng lớn line-height càng nhỏ, display ~1.2–1.25× (vd 60→~72) | S1 |
| 5 | Letter-spacing âm −2% cho display (2xl–md) để dễ đọc ở cỡ lớn; đừng quá tay | S1 |
| 6 | Figma chỉ cho %/px trong text style (không như CSS) → bàn giao nên đổi sang px hoặc rem/em (vd −0.2em) | S1 |
| 7 | Chọn font có ≥5 độ đậm (light/regular/medium/semibold/bold + italic); sans-serif trung tính là an toàn; tối đa 2 font, tốt nhất 1 font nhiều độ đậm | S1 |
| 8 | Letter-spacing âm trong S2 chỉ từ `display-md` (→ 2xl), tăng dần −0.72 → −1.44px | S2 |
| 9 | Inline code: bg `--color-bg-secondary` + ring 1px `--color-border-secondary`, radius 6px, weight 700 | S2 |

## 7. Ghi chú

- Màu chữ mẫu (S1): `text-primary (900)` = #171717 (= Tailwind neutral-900).
- Medium = 500 đã xác nhận trên panel S1 (kiểm mẫu README #10).
- `--text-*--line-height` dùng hậu tố kép `--line-height` (Tailwind v4 convention).
- Đủ 44 text style S1 trong `tokens.untitled.json` (collection `6. Typography / Text styles (S1)`).
