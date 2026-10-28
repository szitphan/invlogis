---
type: design-reference
status: draft
updated: 2026-10-26
links:
  - https://www.figma.com/design/QERVV4a2Fpa1FmsZ5LGW3S/ (Colors, node 5225-371288)
  - https://github.com/untitleduico/react (styles/theme.css, .storybook/colors.css)
  - https://www.untitledui.com/react/docs/theming
---

# 01 — Colors · Primitives (dải màu × bậc)

> Hex chỉ nằm ở file này (theo spec). Các file 02 trở đi chỉ ghi alias.
> Nguồn: S1 (Figma frame Colors, đọc nhãn trên canvas — hex + nhãn WCAG) · S2 (repo).
> Figma v8 dùng **màu Tailwind CSS v4.1** (ghi trên frame Colors) để đồng bộ design–code;
> Brand vẫn là **tím Untitled** (không phải dải Tailwind). Nhãn WCAG 2.2 in trên từng ô.

## 1. Base

| Token | Hex (S1) | Nhãn WCAG (S1) | Ghi chú |
|---|---|---|---|
| White | #FFFFFF | AAA 21.00 | |
| Black | #000000 | AAA 21.00 | |
| Transparent | #FFFFFF 0% | — | trong suốt; repo khai `--color-transparent = rgb(0 0 0 / 0)` |

## 2. 27 dải màu × bậc (50–950)

| Dải | Bậc | Hex (S1) | Nhãn WCAG (S1) | Hex S2/Tailwind | Ghi chú |
|---|---|---|---|---|---|
| Brand | 50 | #F9F5FF | AA 6.15 | khớp repo |  |
| Brand | 100 | #F4EBFF | AA 5.72 | khớp repo |  |
| Brand | 200 | #E9D7FE | AA 4.92 | khớp repo |  |
| Brand | 300 | #D6BBFB | 3.89 | khớp repo |  |
| Brand | 400 | #B692F6 | 2.49 | khớp repo |  |
| Brand | 500 | #9E77ED | 3.32 | khớp repo |  |
| Brand | 600 | #7F56D9 | AA 4.95 | khớp repo | bậc mặc định • |
| Brand | 700 | #6941C6 | AA 6.61 | khớp repo |  |
| Brand | 800 | #53389E | AAA 8.65 | khớp repo |  |
| Brand | 900 | #42307D | AAA 10.76 | khớp repo |  |
| Brand | 950 | #2C1C5F | AAA 14.59 | khớp repo |  |
| Red | 50 | #FEF2F2 | AA 5.91 | khớp Tailwind |  |
| Red | 100 | #FEE2E2 | AA 5.29 | khớp Tailwind |  |
| Red | 200 | #FECACA | 4.47 | khớp Tailwind |  |
| Red | 300 | #FCA5A5 | 3.40 | khớp Tailwind |  |
| Red | 400 | #F87171 | 2.76 | khớp Tailwind |  |
| Red | 500 | #EF4444 | 3.76 | khớp Tailwind | bậc mặc định • |
| Red | 600 | #DC2626 | AA 4.82 | khớp Tailwind |  |
| Red | 700 | #B91C1C | AA 6.47 | khớp Tailwind |  |
| Red | 800 | #991B1B | AAA 8.31 | khớp Tailwind |  |
| Red | 900 | #7F1D1D | AAA 10.01 | khớp Tailwind |  |
| Red | 950 | #450A0A | AAA 16.14 | khớp Tailwind |  |
| Orange | 50 | #FFF7ED | AA 4.87 | khớp Tailwind |  |
| Orange | 100 | #FFEDD5 | AA 4.51 | khớp Tailwind |  |
| Orange | 200 | #FED7AA | 3.82 | khớp Tailwind |  |
| Orange | 300 | #FDBA74 | 3.07 | khớp Tailwind |  |
| Orange | 400 | #FB923C | 2.26 | khớp Tailwind |  |
| Orange | 500 | #F97316 | 2.80 | khớp Tailwind | bậc mặc định • |
| Orange | 600 | #EA580C | 3.55 | khớp Tailwind |  |
| Orange | 700 | #C2410C | AA 5.17 | khớp Tailwind |  |
| Orange | 800 | #9A3412 | AAA 7.30 | khớp Tailwind |  |
| Orange | 900 | #7C2D12 | AAA 9.37 | khớp Tailwind |  |
| Orange | 950 | #431407 | AAA 15.65 | khớp Tailwind |  |
| Amber | 50 | #FFFBEB | AA 4.84 | khớp Tailwind |  |
| Amber | 100 | #FEF3C7 | AA 4.50 | khớp Tailwind |  |
| Amber | 200 | #FDE68A | 4.03 | khớp Tailwind |  |
| Amber | 300 | #FCD34D | 3.48 | khớp Tailwind |  |
| Amber | 400 | #FBBF24 | 1.66 | khớp Tailwind |  |
| Amber | 500 | #F59E0B | 2.14 | khớp Tailwind | bậc mặc định • |
| Amber | 600 | #D97706 | 3.18 | khớp Tailwind |  |
| Amber | 700 | #B45309 | AA 5.02 | khớp Tailwind |  |
| Amber | 800 | #92400E | AAA 7.09 | khớp Tailwind |  |
| Amber | 900 | #78350F | AAA 9.07 | khớp Tailwind |  |
| Amber | 950 | #451A03 | AAA 14.97 | khớp Tailwind |  |
| Yellow | 50 | #FEFCE8 | AA 4.75 | khớp Tailwind |  |
| Yellow | 100 | #FEF9C3 | AA 4.58 | khớp Tailwind |  |
| Yellow | 200 | #FEF08A | 4.23 | khớp Tailwind |  |
| Yellow | 300 | #FDE047 | 3.73 | khớp Tailwind |  |
| Yellow | 400 | #FACC15 | 1.53 | khớp Tailwind |  |
| Yellow | 500 | #EAB308 | 1.91 | khớp Tailwind | bậc mặc định • |
| Yellow | 600 | #CA8A04 | 2.93 | khớp Tailwind |  |
| Yellow | 700 | #A16207 | AA 4.92 | khớp Tailwind |  |
| Yellow | 800 | #854D0E | AA 6.85 | khớp Tailwind |  |
| Yellow | 900 | #713F12 | AAA 8.67 | khớp Tailwind |  |
| Yellow | 950 | #422006 | AAA 14.57 | khớp Tailwind |  |
| Lime | 50 | #F7FEE7 | AAA 4.82 ⚠ | khớp Tailwind | lỗi nhãn: 4.82 < 7 nhưng ghi AAA |
| Lime | 100 | #ECFCCB | AA 4.60 | khớp Tailwind |  |
| Lime | 200 | #D9F99D | 4.27 | khớp Tailwind |  |
| Lime | 300 | #BEF264 | 3.82 | khớp Tailwind |  |
| Lime | 400 | #A3E635 | 1.50 | khớp Tailwind |  |
| Lime | 500 | #84CC16 | 1.97 | khớp Tailwind | bậc mặc định • |
| Lime | 600 | #65A30D | 3.08 | khớp Tailwind |  |
| Lime | 700 | #4D7C0F | AA 4.99 | khớp Tailwind |  |
| Lime | 800 | #3F6212 | AAA 7.07 | khớp Tailwind |  |
| Lime | 900 | #365314 | AAA 8.73 | khớp Tailwind |  |
| Lime | 950 | #1A2E05 | AAA 14.61 | khớp Tailwind |  |
| Green | 50 | #F0FDF4 | AA 4.79 | khớp Tailwind |  |
| Green | 100 | #DCFCE7 | AA 4.56 | khớp Tailwind |  |
| Green | 200 | #BBF7D0 | 3.78 | khớp Tailwind |  |
| Green | 300 | #86EFAC | 3.57 | khớp Tailwind |  |
| Green | 400 | #4ADE80 | 1.74 | khớp Tailwind |  |
| Green | 500 | #22C55E | 2.27 | khớp Tailwind | bậc mặc định • |
| Green | 600 | #16A34A | 3.29 | khớp Tailwind |  |
| Green | 700 | #15803D | AA 5.01 | khớp Tailwind |  |
| Green | 800 | #166534 | AAA 7.13 | khớp Tailwind |  |
| Green | 900 | #14532D | AAA 9.11 | khớp Tailwind |  |
| Green | 950 | #052E16 | AAA 14.90 | khớp Tailwind |  |
| Emerald | 50 | #ECFDF5 | AA 5.20 | khớp Tailwind |  |
| Emerald | 100 | #D1FAE5 | AA 4.83 | khớp Tailwind |  |
| Emerald | 200 | #A7F3D0 | 4.27 | khớp Tailwind |  |
| Emerald | 300 | #6EE7B7 | 3.59 | khớp Tailwind |  |
| Emerald | 400 | #34D399 | 1.92 | khớp Tailwind |  |
| Emerald | 500 | #10B981 | 2.53 | khớp Tailwind | bậc mặc định • |
| Emerald | 600 | #059669 | 3.76 | khớp Tailwind |  |
| Emerald | 700 | #047857 | AA 5.48 | khớp Tailwind |  |
| Emerald | 800 | #065F46 | AAA 7.68 | khớp Tailwind |  |
| Emerald | 900 | #064E3B | AAA 9.71 | khớp Tailwind |  |
| Emerald | 950 | #022C22 | AAA 15.15 | khớp Tailwind |  |
| Teal | 50 | #F0FDFA | AA 5.24 | khớp Tailwind |  |
| Teal | 100 | #CCFBF1 | AA 4.85 | khớp Tailwind |  |
| Teal | 200 | #99F6E4 | 4.34 | khớp Tailwind |  |
| Teal | 300 | #5EEAD4 | 3.69 | khớp Tailwind |  |
| Teal | 400 | #2DD4BF | 1.86 | khớp Tailwind |  |
| Teal | 500 | #14B8A6 | 2.48 | khớp Tailwind | bậc mặc định • |
| Teal | 600 | #0D9488 | 3.74 | khớp Tailwind |  |
| Teal | 700 | #0F766E | AA 5.47 | khớp Tailwind |  |
| Teal | 800 | #115E59 | AAA 7.58 | khớp Tailwind |  |
| Teal | 900 | #134E4A | AAA 9.47 | khớp Tailwind |  |
| Teal | 950 | #042F2E | AAA 14.47 | khớp Tailwind |  |
| Cyan | 50 | #ECFEFF | AA 5.15 | khớp Tailwind |  |
| Cyan | 100 | #CFFAFE | AA 4.78 | khớp Tailwind |  |
| Cyan | 200 | #A5F3FC | 4.29 | khớp Tailwind |  |
| Cyan | 300 | #67E8F9 | 3.69 | khớp Tailwind |  |
| Cyan | 400 | #22D3EE | 1.80 | khớp Tailwind |  |
| Cyan | 500 | #06B6D4 | 2.42 | khớp Tailwind | bậc mặc định • |
| Cyan | 600 | #0891B2 | 3.68 | khớp Tailwind |  |
| Cyan | 700 | #0E7490 | AA 5.35 | khớp Tailwind |  |
| Cyan | 800 | #155E75 | AAA 7.26 | khớp Tailwind |  |
| Cyan | 900 | #164E63 | AAA 9.11 | khớp Tailwind |  |
| Cyan | 950 | #083344 | AAA 13.39 | khớp Tailwind |  |
| Sky | 50 | #F0F9FF | AA 5.56 | khớp Tailwind |  |
| Sky | 100 | #E0F2FE | AA 5.17 | khớp Tailwind |  |
| Sky | 200 | #BAE6FD | 4.47 | khớp Tailwind |  |
| Sky | 300 | #7DD3FC | 3.55 | khớp Tailwind |  |
| Sky | 400 | #38BDF8 | 2.14 | khớp Tailwind |  |
| Sky | 500 | #0EA5E9 | 2.77 | khớp Tailwind | bậc mặc định • |
| Sky | 600 | #0284C7 | 4.09 | khớp Tailwind |  |
| Sky | 700 | #0369A1 | AA 5.93 | khớp Tailwind |  |
| Sky | 800 | #075985 | AAA 7.56 | khớp Tailwind |  |
| Sky | 900 | #0C4A6E | AAA 9.45 | khớp Tailwind |  |
| Sky | 950 | #082F49 | AAA 13.87 | khớp Tailwind |  |
| Blue | 50 | #EFF6FF | AA 6.15 | khớp Tailwind |  |
| Blue | 100 | #DBEAFE | AA 5.49 | khớp Tailwind |  |
| Blue | 200 | #BFDBFE | AA 4.71 | khớp Tailwind |  |
| Blue | 300 | #93C5FD | 3.71 | khớp Tailwind |  |
| Blue | 400 | #60A5FA | 2.54 | khớp Tailwind |  |
| Blue | 500 | #3B82F6 | 3.67 | khớp Tailwind | bậc mặc định • |
| Blue | 600 | #2563EB | AA 5.16 | khớp Tailwind |  |
| Blue | 700 | #1D4ED8 | AA 6.70 | khớp Tailwind |  |
| Blue | 800 | #1E40AF | AAA 8.72 | khớp Tailwind |  |
| Blue | 900 | #1E3A8A | AAA 10.35 | khớp Tailwind |  |
| Blue | 950 | #172554 | AAA 14.69 | khớp Tailwind |  |
| Indigo | 50 | #EEF2FF | AA 7.06 | khớp Tailwind |  |
| Indigo | 100 | #E0E7FF | AA 6.41 | khớp Tailwind |  |
| Indigo | 200 | #C7D2FE | AA 5.29 | khớp Tailwind |  |
| Indigo | 300 | #A5B4FC | 3.96 | khớp Tailwind |  |
| Indigo | 400 | #818CF8 | 2.98 | khớp Tailwind |  |
| Indigo | 500 | #6366F1 | 4.46 | khớp Tailwind | bậc mặc định • |
| Indigo | 600 | #4F46E5 | AA 6.28 | khớp Tailwind |  |
| Indigo | 700 | #4338CA | AAA 7.90 | khớp Tailwind |  |
| Indigo | 800 | #3730A3 | AAA 9.93 | khớp Tailwind |  |
| Indigo | 900 | #312E81 | AAA 11.42 | khớp Tailwind |  |
| Indigo | 950 | #1E1B4B | AAA 15.98 | khớp Tailwind |  |
| Violet | 50 | #F5F3FF | AA 6.47 | khớp Tailwind |  |
| Violet | 100 | #EDE9FE | AA 5.98 | khớp Tailwind |  |
| Violet | 200 | #DDD6FE | AA 5.11 | khớp Tailwind |  |
| Violet | 300 | #C4B5FD | 3.84 | khớp Tailwind |  |
| Violet | 400 | #A78BFA | 2.72 | khớp Tailwind |  |
| Violet | 500 | #8B5CF6 | 4.23 | khớp Tailwind | bậc mặc định • |
| Violet | 600 | #7C3AED | AA 5.69 | khớp Tailwind |  |
| Violet | 700 | #6D28D9 | AAA 7.10 | khớp Tailwind |  |
| Violet | 800 | #5B21B6 | AAA 8.98 | khớp Tailwind |  |
| Violet | 900 | #4C1D95 | AAA 10.95 | khớp Tailwind |  |
| Violet | 950 | #2E1065 | AAA 15.23 | khớp Tailwind |  |
| Purple | 50 | #FAF5FF | AA 6.50 | khớp Tailwind |  |
| Purple | 100 | #F3E8FF | AA 5.91 | khớp Tailwind |  |
| Purple | 200 | #E9D5FF | AA 5.12 | khớp Tailwind |  |
| Purple | 300 | #D8B4FE | 3.95 | khớp Tailwind |  |
| Purple | 400 | #C084FC | 2.64 | khớp Tailwind |  |
| Purple | 500 | #A855F7 | 3.95 | khớp Tailwind | bậc mặc định • |
| Purple | 600 | #9333EA | AA 5.38 | khớp Tailwind |  |
| Purple | 700 | #7E22CE | AA 6.98 | khớp Tailwind |  |
| Purple | 800 | #6B21A8 | AAA 8.72 | khớp Tailwind |  |
| Purple | 900 | #581C87 | AAA 10.87 | khớp Tailwind |  |
| Purple | 950 | #3B0764 | AAA 14.99 | khớp Tailwind |  |
| Fuchsia | 50 | #FDF4FF | AA 5.88 | khớp Tailwind |  |
| Fuchsia | 100 | #FAE8FF | AA 5.43 | khớp Tailwind |  |
| Fuchsia | 200 | #F5D0FE | AA 4.61 | khớp Tailwind |  |
| Fuchsia | 300 | #F0ABFC | 3.59 | khớp Tailwind |  |
| Fuchsia | 400 | #E879F9 | 2.46 | khớp Tailwind |  |
| Fuchsia | 500 | #D946EF | 3.45 | khớp Tailwind | bậc mặc định • |
| Fuchsia | 600 | #C026D3 | AA 4.70 | khớp Tailwind |  |
| Fuchsia | 700 | #A21CAF | AA 6.32 | khớp Tailwind |  |
| Fuchsia | 800 | #86198F | AAA 8.23 | khớp Tailwind |  |
| Fuchsia | 900 | #701A75 | AAA 10.03 | khớp Tailwind |  |
| Fuchsia | 950 | #4A044E | AAA 14.80 | khớp Tailwind |  |
| Pink | 50 | #FDF2F8 | AA 5.52 | khớp Tailwind |  |
| Pink | 100 | #FCE7F3 | AA 5.12 | khớp Tailwind |  |
| Pink | 200 | #FBCFE8 | 4.36 | khớp Tailwind |  |
| Pink | 300 | #F9A8D4 | 3.32 | khớp Tailwind |  |
| Pink | 400 | #F472B6 | 2.64 | khớp Tailwind |  |
| Pink | 500 | #EC4899 | 3.52 | khớp Tailwind | bậc mặc định • |
| Pink | 600 | #DB2777 | AA 4.59 | khớp Tailwind |  |
| Pink | 700 | #BE185D | AA 6.03 | khớp Tailwind |  |
| Pink | 800 | #9D174D | AAA 7.88 | khớp Tailwind |  |
| Pink | 900 | #831843 | AAA 9.64 | khớp Tailwind |  |
| Pink | 950 | #500724 | AAA 15.03 | khớp Tailwind |  |
| Rose | 50 | #FFF1F2 | AA 5.72 | khớp Tailwind |  |
| Rose | 100 | #FFE4E6 | AA 5.23 | khớp Tailwind |  |
| Rose | 200 | #FECDD3 | 4.45 | khớp Tailwind |  |
| Rose | 300 | #FDA4AF | 3.32 | khớp Tailwind |  |
| Rose | 400 | #FB7185 | 2.69 | khớp Tailwind |  |
| Rose | 500 | #F43F5E | 3.67 | khớp Tailwind | bậc mặc định • |
| Rose | 600 | #E11D48 | AA 4.69 | khớp Tailwind |  |
| Rose | 700 | #BE123C | AA 6.28 | khớp Tailwind |  |
| Rose | 800 | #9F1239 | AAA 8.01 | khớp Tailwind |  |
| Rose | 900 | #881337 | AAA 9.56 | khớp Tailwind |  |
| Rose | 950 | #4C0519 | AAA 15.63 | khớp Tailwind |  |
| Slate | 50 | #F8FAFC | AAA 7.24 | khớp Tailwind |  |
| Slate | 100 | #F1F5F9 | AA 6.91 | khớp Tailwind |  |
| Slate | 200 | #E2E8F0 | AA 6.14 | khớp Tailwind |  |
| Slate | 300 | #CBD5E1 | AA 5.10 | khớp Tailwind |  |
| Slate | 400 | #94A3B8 | 2.56 | khớp Tailwind |  |
| Slate | 500 | #64748B | AA 4.75 | khớp Tailwind | bậc mặc định • |
| Slate | 600 | #475569 | AAA 7.57 | khớp Tailwind |  |
| Slate | 700 | #334155 | AAA 10.35 | khớp Tailwind |  |
| Slate | 800 | #1E293B | AAA 14.62 | khớp Tailwind |  |
| Slate | 900 | #0F172A | AAA 17.85 | khớp Tailwind |  |
| Slate | 950 | #020617 | AAA 20.17 | khớp Tailwind |  |
| Gray | 50 | #F9FAFB | AAA 7.23 | khớp Tailwind |  |
| Gray | 100 | #F3F4F6 | AA 6.86 | khớp Tailwind |  |
| Gray | 200 | #E5E7EB | AA 6.10 | khớp Tailwind |  |
| Gray | 300 | #D1D5DB | AA 5.12 | khớp Tailwind |  |
| Gray | 400 | #9CA3AF | 2.53 | khớp Tailwind |  |
| Gray | 500 | #6B7280 | AA 4.83 | khớp Tailwind | bậc mặc định • |
| Gray | 600 | #4B5563 | AAA 7.55 | khớp Tailwind |  |
| Gray | 700 | #374151 | AAA 10.30 | khớp Tailwind |  |
| Gray | 800 | #1F2937 | AAA 14.67 | khớp Tailwind |  |
| Gray | 900 | #111827 | AAA 17.73 | khớp Tailwind |  |
| Gray | 950 | #030712 | AAA 20.13 | khớp Tailwind |  |
| Zinc | 50 | #FAFAFA | AAA 7.40 | khớp Tailwind |  |
| Zinc | 100 | #F4F4F5 | AAA 7.03 | khớp Tailwind |  |
| Zinc | 200 | #E4E4E7 | AA 6.09 | khớp Tailwind |  |
| Zinc | 300 | #D4D4D8 | AA 5.22 | khớp Tailwind |  |
| Zinc | 400 | #A1A1AA | 2.56 | khớp Tailwind |  |
| Zinc | 500 | #71717A | AA 4.83 | khớp Tailwind | bậc mặc định • |
| Zinc | 600 | #52525B | AAA 7.72 | khớp Tailwind |  |
| Zinc | 700 | #3F3F46 | AAA 10.44 | khớp Tailwind |  |
| Zinc | 800 | #27272A | AAA 14.89 | khớp Tailwind |  |
| Zinc | 900 | #18181B | AAA 17.71 | khớp Tailwind |  |
| Zinc | 950 | #09090B | AAA 19.89 | khớp Tailwind |  |
| Neutral | 50 | #FAFAFA | AAA 7.48 | khớp Tailwind | Default gray |
| Neutral | 100 | #F5F5F5 | AAA 7.16 | khớp Tailwind | Default gray |
| Neutral | 200 | #E5E5E5 | AA 6.20 | khớp Tailwind | Default gray |
| Neutral | 300 | #D4D4D4 | AA 5.27 | khớp Tailwind | Default gray |
| Neutral | 400 | #A3A3A3 | 2.52 | khớp Tailwind | Default gray |
| Neutral | 500 | #737373 | AA 4.74 | khớp Tailwind | Default gray, bậc mặc định • |
| Neutral | 600 | #525252 | AAA 7.81 | khớp Tailwind | Default gray |
| Neutral | 700 | #404040 | AAA 10.36 | khớp Tailwind | Default gray |
| Neutral | 800 | #262626 | AAA 15.13 | khớp Tailwind | Default gray |
| Neutral | 900 | #171717 | AAA 17.92 | khớp Tailwind | Default gray |
| Neutral | 950 | #0A0A0A | AAA 19.79 | khớp Tailwind | Default gray |
| Stone | 50 | #FAFAF9 | AAA 7.30 | khớp Tailwind |  |
| Stone | 100 | #F5F5F4 | AA 6.99 | khớp Tailwind |  |
| Stone | 200 | #E7E5E4 | AA 6.07 | khớp Tailwind |  |
| Stone | 300 | #D6D3D1 | AA 5.12 | khớp Tailwind |  |
| Stone | 400 | #A8A29E | 2.52 | khớp Tailwind |  |
| Stone | 500 | #78716C | AA 4.79 | khớp Tailwind | bậc mặc định • |
| Stone | 600 | #57534E | AAA 7.62 | khớp Tailwind |  |
| Stone | 700 | #44403C | AAA 10.27 | khớp Tailwind |  |
| Stone | 800 | #292524 | AAA 15.16 | khớp Tailwind |  |
| Stone | 900 | #1C1917 | AAA 17.48 | khớp Tailwind |  |
| Stone | 950 | #0C0A09 | AAA 19.75 | khớp Tailwind |  |
| Taupe | 50 | #FBFAF9 | AAA 7.55 | — (không có trong repo) |  |
| Taupe | 100 | #F3F1F1 | AAA 7.00 | — (không có trong repo) |  |
| Taupe | 200 | #E8E4E3 | AA 6.24 | — (không có trong repo) |  |
| Taupe | 300 | #D8D2D0 | AA 5.27 | — (không có trong repo) |  |
| Taupe | 400 | #ABA09C | 3.09 | — (không có trong repo) |  |
| Taupe | 500 | #7C6D67 | AA 4.95 | — (không có trong repo) | bậc mặc định • |
| Taupe | 600 | #5B4F4B | AAA 7.88 | — (không có trong repo) |  |
| Taupe | 700 | #473C39 | AAA 10.64 | — (không có trong repo) |  |
| Taupe | 800 | #2B2422 | AAA 15.23 | — (không có trong repo) |  |
| Taupe | 900 | #1D1816 | AAA 17.58 | — (không có trong repo) |  |
| Taupe | 950 | #0C0A09 | AAA 19.75 | — (không có trong repo) |  |
| Mauve | 50 | #FAFAFA | AAA 7.70 | — (không có trong repo) |  |
| Mauve | 100 | #F3F1F3 | AAA 7.16 | — (không có trong repo) |  |
| Mauve | 200 | #E7E4E7 | AA 6.37 | — (không có trong repo) |  |
| Mauve | 300 | #D7D0D7 | AA 5.32 | — (không có trong repo) |  |
| Mauve | 400 | #A89EA9 | 3.11 | — (không có trong repo) |  |
| Mauve | 500 | #79697B | AA 5.09 | — (không có trong repo) | bậc mặc định • |
| Mauve | 600 | #594C5B | AAA 8.04 | — (không có trong repo) |  |
| Mauve | 700 | #463947 | AAA 10.84 | — (không có trong repo) |  |
| Mauve | 800 | #2A212C | AAA 15.52 | — (không có trong repo) |  |
| Mauve | 900 | #1D161E | AAA 17.71 | — (không có trong repo) |  |
| Mauve | 950 | #0C090C | AAA 19.81 | — (không có trong repo) |  |
| Mist | 50 | #F9FBFB | AAA 7.71 | — (không có trong repo) |  |
| Mist | 100 | #F1F3F3 | AA 6.62 | — (không có trong repo) |  |
| Mist | 200 | #E3E7E8 | AA 5.92 | — (không có trong repo) |  |
| Mist | 300 | #D0D6D8 | AA 5.02 | — (không có trong repo) |  |
| Mist | 400 | #9CA8AB | 3.02 | — (không có trong repo) |  |
| Mist | 500 | #67787C | AA 4.61 | — (không có trong repo) | bậc mặc định • |
| Mist | 600 | #4B585B | AAA 7.37 | — (không có trong repo) |  |
| Mist | 700 | #394447 | AAA 10.03 | — (không có trong repo) |  |
| Mist | 800 | #22292B | AAA 14.78 | — (không có trong repo) |  |
| Mist | 900 | #161B1D | AAA 17.37 | — (không có trong repo) |  |
| Mist | 950 | #090B0C | AAA 19.72 | — (không có trong repo) |  |
| Olive | 50 | #FBFBF9 | AA 6.66 | — (không có trong repo) |  |
| Olive | 100 | #F4F4F0 | AA 6.25 | — (không có trong repo) |  |
| Olive | 200 | #E8E8E3 | AA 5.61 | — (không có trong repo) |  |
| Olive | 300 | #D8D8D0 | AA 4.81 | — (không có trong repo) |  |
| Olive | 400 | #ABAB9C | 2.96 | — (không có trong repo) |  |
| Olive | 500 | #7C7C67 | 4.25 | — (không có trong repo) | bậc mặc định • |
| Olive | 600 | #5B5B4B | AA 6.90 | — (không có trong repo) |  |
| Olive | 700 | #474739 | AAA 9.42 | — (không có trong repo) |  |
| Olive | 800 | #2B2B22 | AAA 14.27 | — (không có trong repo) |  |
| Olive | 900 | #1D1D16 | AAA 16.94 | — (không có trong repo) |  |
| Olive | 950 | #0C0C09 | AAA 19.58 | — (không có trong repo) |  |

> Tổng 27 dải × 11 = 297 + Base 3 = 300 màu. Thứ tự dải xám trên canvas: Slate, Gray, Zinc,
> Neutral, Stone, Taupe, Mauve, Mist, Olive (9 xám; spec ghi "8" nhưng liệt kê 9).
> Mô tả: các dải sắc "Can be swapped with the default brand color"; các dải xám "Can be swapped
> with the default gray color". Neutral = "Default gray".

## 3. So S2 (repo)

- **Brand**: khớp 100% repo `theme.css` (`--color-brand-50…950`). Repo còn có **bậc 25**
  (`#fcfaff`, chỉ trong `.storybook/colors.css`, không có trong theme.css) — Figma không có bậc 25.
- **17 sắc + 5 xám chuẩn** (Slate/Gray/Zinc/Neutral/Stone): Figma khớp Tailwind v4.1 mặc định;
  repo không khai lại (tham chiếu `--color-<hue>-*` Tailwind native). Đã so từng hex = 0 lệch.
- **4 xám Untitled** (Taupe/Mauve/Mist/Olive): không có trong repo/`.storybook/colors.css` (chỉ có ở Figma).

## 4. Gradients (S1 — frame 1525-272676)

- **Neutral gradients** (14 style): tuyến tính giữa 2 primitive, vd `Neutral/600 -> 500 (90deg)`.
  Dùng cho nền, thêm chiều sâu/kết cấu nhẹ.
- **Brand gradients** (7): như trên với primitive Brand (vd `600 -> 500 (90deg)`). Theo màu brand,
  dùng cho phần tử tương tác.
- **Linear gradients 01…33** (thiếu 23, 28 trong danh sách): 2 stop hex cố định, không gắn biến,
  vd `Linear/01` #A5C0EE → #FBC5EC. Nhiều màu cho nền, làm vật thể nổi bật. Stop 02–33: chưa đọc.
- **Mesh gradients**: là ẢNH (fill Image "01.png"…), không phải token. Tạo bằng công cụ Mesh.
- **skeuemorphic-gradient-border**: chưa đọc giá trị.

## 5. Luật dùng màu

| # | Luật | Nguồn |
|---|---|---|
| 1 | Hệ màu tối giản cần: neutral, brand, accent và màu phản hồi (xanh = thành công, đỏ = lỗi), nhất là khi có form | S1 |
| 2 | Neutral = nền tảng (chữ, form field, nền, divider thường là xám); Brand = mọi phần tử tương tác (button, link, input) | S1 |
| 3 | Accent = màu phụ gây chú ý/hỗ trợ brand, hợp cho label và badge; Feedback: error = lỗi/destructive, warning = hành động nguy hiểm/on-hold, success = tích cực | S1 |
| 4 | Nếu primary là xanh lá thì chọn sắc khác cho success (tránh nhầm) | S1 |
| 5 | Dùng 8–12 sắc mỗi màu (không cần 50); sinh bằng generator Tailwind (uicolors.app, tailwindshades.com, tints.dev, tailcolor.com) | S1 |
| 6 | WCAG 2.2: A <4.5:1 (không cho chữ); AA ≥4.5:1 (mặc định cho chữ/button/form); AAA ≥7:1 (nice-to-have). Giữ ≥4.5:1 cho phần tử quan trọng | S1 |
| 7 | Đặt tên theo token (`neutral-300`, `brand-600`), không dùng hex rời; nhất quán (vd luôn neutral-300 cho viền input field, neutral-200 cho divider) | S1 |
| 8 | Quản lý màu bằng variables (primitives = nguồn sự thật), không dùng color styles | S1 |

## 6. Ghi chú

- ⚠ **Lỗi nhãn Lime-50**: Figma ghi "AAA 4.82" nhưng 4.82 < 7 → nhãn AAA có vẻ sai trong file gốc.
- Bậc mặc định (chấm trắng • trên ô): Brand = 600; 26 dải còn lại = 500.
- Lịch sử: v5.0 xám hơi xanh (B2B/SaaS); v6.0 xám flat; v8.0 chuyển toàn bộ sang Tailwind,
  xám mặc định = neutral (khử bão hoà hoàn toàn). React bỏ 436 biến màu thừa: theme 65KB → 45KB.
- `_Primitives` → Colors = 311 trên Figma nhưng đọc được 300; 11 biến chưa giải thích (xem `00-structure.md`).
