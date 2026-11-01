---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/
  - https://github.com/untitleduico/react
  - https://www.untitledui.com/react/docs/
---

# Untitled UI (v8.0) — Design tokens tham chiếu

Tài liệu trích xuất Foundations của Untitled UI React để đội Invlogis so sánh với DS v2
(`design-system/`). **Chỉ trích xuất, không so sánh/đề xuất** (việc đó do phiên khác làm).

## Nguồn & ngày đọc

| Nguồn | Chi tiết | Ngày | Ghi chú |
|---|---|---|---|
| S1 | Figma `QERVV4a2Fpa1FmsZ5LGW3S` (❖ PREVIEW v8.0) | 2026-10-26 | đọc qua Chrome: cấu trúc trang, collection, quy ước, hex+WCAG, alpha/utility, spacing/width/container/radius/grid, shadow/focus/blur, text style, icon, gradients |
| S2 | Repo `untitleduico/react` @ `1d410cb8facde8d50869e7bbb5f3d048e2267466` (main) | 2026-10-26 | `styles/theme.css` (753 dòng), `styles/typography.css`, `styles/globals.css`, `.storybook/colors.css` |
| S3 | https://www.untitledui.com/react/docs/ (introduction, theming, dark-mode, typography, icons, installation, cli, rtl, upgrade) | 2026-10-26 | rút text vào `raw/docs-*.txt` |

## Phạm vi đã phủ (Đợt 1: Foundations)

| Trang | Khối | Số token đã lấy (S1) | Số thấy trên Figma | Đủ? |
|---|---|---|---|---|
| Getting started | Cấu trúc file, quy ước đặt tên, đổi brand | — (luật, file `00`) | 5 frame đọc | ✅ |
| Variables | Collections + mode | 7 collection | 7 collection | ⚠ group Background/Foreground bị che |
| Colors | Primitives (hex + WCAG) | 300 (27 dải × 11 + Base 3) | 311 (panel `_Primitives` → Colors) | ⚠ thiếu 11 |
| Colors | Semantic (text/border/fg/bg) | 74 (Text 20 + Border 8 + Foreground 18 + Background 28) | Text 21 · Border 8 · Foreground 19 · Background ? | ⚠ Background bị che |
| Colors | Alpha + Utility | 20 alpha + 118 utility | — (frame Color utility variables) | ✅ |
| Colors | Gradients | Neutral 14 · Brand 7 · Linear 01–33 (thiếu 23/28) · Mesh (ảnh) | — | ⚠ stop 02–33 chưa đọc |
| Typography | Text style (cỡ/dòng/đậm/tracking) | 44 (11 cỡ × 4 độ đậm) | 44 | ✅ |
| Logos, Icons | Thư viện, đặt tên, danh mục, featured/misc, logos | 19 danh mục · 24px · stroke 2px | — | ✅ (cấu trúc) |
| Effect styles | Shadows / Focus rings / Backdrop blurs | 15 lớp bóng · 7 focus ring · 4 blur | Shadows 8 · Focus 7 · Blur 4 (tên) | ✅ (Dark shadow `?`) |
| Spacing, radius & grids | Spacing / width / container / radius / grid | 32 primitive + 17 semantic + 12 width + 3 container + 11 radius + 3 grid | khớp panel | ✅ |

## Số biến trong `tokens.untitled.json`

- **S2** (repo theme.css light `@theme`): **378 biến** (giữ nguyên qua verify).
- **S1** (Figma): **649 biến** mang nguồn S1 (gồm 12 collection `(S1)` mới + brand/transparent/semantic đã gộp src).

| Nhóm S1 (collection) | Số biến |
|---|---|
| Primitives / Colors (S1) | 288 (+ Brand 11 đã gộp vào collection S2) |
| Primitives / Alpha (S1) | 20 |
| Color modes / Utility (S1) | 118 |
| Primitives / Spacing (S1) | 32 |
| Spacing / Semantic (S1) | 17 |
| Widths (S1) | 12 |
| Containers (S1) | 3 |
| Radius (S1) | 11 |
| Effects / Shadows (S1) | 7 style (15 lớp) |
| Effects / Focus rings (S1) | 7 |
| Effects / Backdrop blurs (S1) | 4 |
| Typography / Text styles (S1) | 44 |

## Kết quả kiểm tự động (theme.css ↔ tokens.untitled.json)

Script `_task/verify_tokens.py`:

```
KẾT QUẢ: PASS — khớp
  Tổng biến theme.css (light @theme): 378
  Tổng biến trong tokens.json (S2):    378
  Tổng biến mang nguồn S1:            649
```

Chi tiết từng nhóm: `_task/verify-report.txt`.

## Đối chiếu S1↔S2 (tổng 10 chỗ lệch)

**Màu semantic — 6 chỗ lệch giá trị (đều ở Dark):**

1. `text-placeholder` (dark): S1=neutral-400, S2=neutral.500
2. `fg-quaternary` (dark): S1=neutral-500, S2=neutral.600
3. `fg-quaternary_hover` (dark): S1=neutral-400, S2=neutral.500
4. `bg-primary-solid` (dark): S1=neutral-800, S2=bg.secondary (→neutral-900)
5. `bg-brand-primary_alt` (dark): S1=neutral-800, S2=bg.secondary (→neutral-900)
6. `bg-brand-section` (dark): S1=neutral-800, S2=bg.secondary (→neutral-900)

**Khác tên (không tính giá trị):**

7. `text-white`: S1 ghi `text-white`, S2 ghi `white` (cùng nghĩa)

**Lệch nhóm:**

8. Alpha: S1 = 20 biến theo bậc 10% · S2 = 2 biến màu đặc
9. Utility: S1 = 118 (tên `utility-error/-warning/-success`) · S2 = 134 (tên `utility-red/-yellow/-green`, thêm `amber` + `emerald` 16 biến). ⚠ S1 lỗi tên "utility-brand_alt" (thiếu số bậc).

**Lệch bậc:**

10. Brand: repo có bậc **25** (`#fcfaff`, `.storybook/colors.css`) · Figma không có.

**Shadow S1↔S2:** 7 style `shadow-xs…3xl` (15 lớp) khớp từng giá trị x/y/blur/spread/alpha với `theme.css`; lớp bóng trong của skeuomorphic (0 −2 0 0 5%, 0 0 0 1 18%) khớp `--shadow-skeuomorphic`.

**S1↔S3:** Radius S1 = 11 bậc, S3 docs = 10 (thang khác: S1 `sm`=6px vs S3 4px…).

## Kiểm mẫu ngẫu nhiên

> Phiên Claude mở lại Figma 2026-10-26, đọc lại bằng cách khác lần đầu (panel Properties ↔ ảnh zoom). **10/10 khớp.**

| # | Token | Giá trị file | Đọc lại Figma | Cách đọc lại | Khớp? |
|---|---|---|---|---|---|
| 1 | Brand/300 | #D6BBFB · 3.89 | #D6BBFB · 3.89 | panel (fill swatch + Content nhãn) | ✅ |
| 2 | Red/400 | #F87171 · 2.76 | #F87171 · 2.76 | panel | ✅ |
| 3 | Lime/50 | #F7FEE7 · "AAA 4.82" | #F7FEE7 · "AAA 4.82" | panel (xác nhận nhãn AAA sai có thật trong file) | ✅ |
| 4 | Emerald/800 | #065F46 | #065F46 | panel | ✅ |
| 5 | Orange/600 | #EA580C | #EA580C | panel | ✅ |
| 6 | shadow-2xl | 0/4/4/−2 #000 4% + 0/24/48/−12 #000 18% | giống hệt | panel, chọn lại card | ✅ |
| 7 | radius-lg | 0.625rem · 10px | 0.625rem · 10px | ảnh zoom bảng Radius | ✅ |
| 8 | spacing-xxs | 0.125rem · 2px | 0.125rem · 2px | ảnh zoom bảng Spacing | ✅ |
| 9 | Display xl/Semibold | 600 · letter-spacing −2% | 600 · −2% | panel (text tiêu đề Notes) | ✅ |
| 10 | Text lg/Medium | Medium = 500 (lần đầu chưa xác nhận), tracking 0% | Weight 500 · 0% | panel (nhãn WCAG trên swatch dùng Text lg/Medium) | ✅ (đồng thời xác nhận Medium = 500) |

## Khối không đọc được / chưa đọc

- **Shadow ở Dark mode**: màu bóng là biến `Colors/Effects/Shadows/*_NN`; giá trị Dark chưa đọc → `?`.
- **Stop gradient Linear 02–33**: chưa đọc (chỉ đọc Linear 01 + tên/cặp màu của Neutral/Brand).
- **skeuemorphic-gradient-border**: chưa đọc giá trị.
- **Tên Type 2–4 của Featured icon**: chưa đọc (chỉ đọc Type 1 = Light).
- **Giá trị biến Line height** (collection 6. Typography): chưa đọc trực tiếp (đoán 11 biến từ 32 − 21).
- **How to master variants / Auto Layout**: hướng dẫn kỹ năng Figma chung, không chứa token.
- **`_Primitives` → Colors = 311** nhưng đọc được 300; 11 biến chưa giải thích.
- **Grid cột "auto"** (12/6/5/3/2): giá trị rãnh chưa đọc.

## Cấu trúc thư mục

```
design/_ref/untitled-ui/
├── README.md               ← file này
├── 00-structure.md
├── 01-colors-primitives.md
├── 02-colors-semantic.md
├── 03-typography.md
├── 04-spacing-radius-grid.md
├── 05-effects.md
├── 06-icons.md
├── tokens.untitled.json    378 biến (S2) + 649 nguồn S1 + radius/spacing (S3)
├── raw/                    nguyên văn theme.css, typography.css, globals.css, colors.css + docs-*.txt
└── _task/                  spec, task-A/B/C, gen/merge/verify scripts, s1-*.md
```

## Hướng dẫn chạy kiểm lại

```bash
cd design/_ref/untitled-ui
python3 _task/verify_tokens.py
```
