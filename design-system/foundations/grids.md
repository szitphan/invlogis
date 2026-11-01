---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Lưới, độ rộng, breakpoint

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (7.x) để các DEC và spec trích "foundations mục 7…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 7. Lưới, độ rộng, breakpoint (DEC-136, DEC-259, DEC-038, DEC-039)

| Màn | Cột | Rãnh | Lề | Rộng tối đa |
|---|---|---|---|---|
| Web ≥ 1024 | 12 | 32 | 32 | 1280 cho màn chi tiết, form; màn bảng trải hết |
| Tablet 768–1023 | 6 | 24 | 24 | — (DEC-257) |
| App (khung 393) | 4 | 16 | 16 | — |

- Lưới web và app theo Untitled UI (DEC-259): web rãnh 24 → 32, lề 24 → 32; app thay **đường canh K1–K4** (DEC-164, DEC-193,
  DEC-194) bằng **4 cột rãnh 16 lề 16**. Lề màn 16 và lề thẻ 16 không đổi, nên chữ trong thẻ vẫn ở 32 tính từ mép màn.
  Viền 1px của thẻ nằm trong khung, không cộng vào lề (Figma stroke Inside; CSS `box-shadow: inset 0 0 0 1px`).
- Mục 6 còn ghi vị trí chữ dạng "K3 64", "K2b 48": đó là khoảng cách đo từ mép màn, vẫn đúng; tên K không còn là lưới.
- Màn chi tiết web chia **8 cột nội dung + 4 cột thông tin** như Jira (DEC-127).
- **Độ rộng (DEC-259):** `width/xs 320` popover, menu thả rộng · `sm 400` dialog xác nhận, drawer thường · `md 560` dialog
  form, form 1 cột · `lg 720` đoạn văn tối đa, dialog lớn · `xl 960` drawer rộng · `2xl 1280` khung nội dung tối đa web.
- **Breakpoint:** xxs 320 · xs 600 (thêm như Untitled, DEC-259) · 640 · 768 · 1024 · 1280 · 1536. Từ 768 tới 1279 menu trái thu
  còn 64 (cột icon), bấm thì bung 240 đè lên nội dung.

