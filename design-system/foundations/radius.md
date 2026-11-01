---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Bo góc

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (5.x) để các DEC và spec trích "foundations mục 5…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 5. Bo góc (DEC-122, DEC-134, DEC-165, DEC-259, DEC-315)

Ba tầng như khoảng cách (DEC-315): **primitive** theo px `radius/0 · 2 · 4 · 6 · 8 · 10 · 12 · 16 · 20 · 24 · 9999` (collection
`0. Primitives`, chỉ Semantic trỏ tới) → **thang Semantic Untitled** trong `2. Platform · Radius`, Web = Mobile:

| `radius/…` | none | xxs | xs | sm | md | lg | xl | 2xl | 3xl | 4xl | full |
|---|---|---|---|---|---|---|---|---|---|---|---|
| px | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 16 | 20 | 24 | tròn hẳn |

→ **token theo vai** (bảng dưới, trỏ thang Semantic) và token component còn lại (đang gộp về token chung, DEC-319). Component
và token component không trỏ primitive `radius/<px>`.


| Token | Web | App | Dùng cho |
|---|---|---|---|
| `radius/control` | 8 | tròn hẳn | Nút, tab chip, ô tìm |
| `radius/field` | 8 | 12 | Ô nhập, ô chọn (app 14 → 12, DEC-259) |
| `radius/card` | 12 | 16 | Thẻ, nhóm có viền, khối trong trang, bảng (app 20 → 16, DEC-165) |
| `radius/inner` | 8 | 12 | Khối phụ trong thẻ, ảnh nhỏ (app 14 → 12) |
| `radius/overlay` | 16 | 24 | Dialog, popover; đầu sheet trên app (web 12 → 16, app 28 → 24, DEC-259) |
| `radius/menu` · `radius/menu-item` | 8 · 6 | 8 · 6 | Menu thả · mục trong menu (như Untitled) |
| `radius/badge` | 6 | 6 | Badge vuông cho nhãn phân loại (không phải trạng thái) |
| `radius/tab` | 8 | tròn hẳn | Tab kiểu nút; tab gạch không bo |
| `radius/chip` | tròn hẳn | tròn hẳn | Chip trạng thái, avatar |

Thang theo Untitled UI (DEC-259): bỏ 14 và 28 (app theo thang Untitled). Từ DEC-315 tên theo cỡ (`radius/md`, CSS
`--radius-md`) là tầng Semantic, primitive đổi sang tên theo px (`--radius-8`); token theo vai (`--radius-card`…) giữ tên. iOS dùng góc liền mạch; có bật "Corner smoothing" trên Figma hay không thì chưa chốt (mục 13).

**Luật lồng góc và lề đều (DEC-165).** R là bo khung ngoài, r là bo khối bên trong, lề là khoảng từ mép khung tới mép khối.

1. Khung có khối hình ở góc (ô icon, avatar, nút, ô nhập, khối phụ, công tắc) thì lề 4 phía bằng nhau, đo tới khối cao
   nhất trong dòng. Chữ không có góc để khớp, chỉ cần lề đều.
2. Khung lớn (thẻ, nhóm có viền) **tách xa**: bo không quá lề (app 16 = lề 16; web 12 dưới lề 16). Khối bên trong khi đó
   chỉ đối diện cạnh thẳng nên giữ hình gì cũng được: ô icon tròn, avatar tròn, nút viên thuốc, ô nhập bo 14.
3. Khung ôm sát một khối (dòng đang chọn, chip, ô tìm) **đồng tâm**: R = r + lề. Hình tròn, viên thuốc có r = cao ÷ 2 nên
   R = cao ÷ 2 + lề, ôm sát thì khung cũng thành viên thuốc. Ví dụ: dòng đang chọn có ô vuông bo 8, lề 8 thì bo 16.
4. Lồng nhiều lớp thì áp từng lớp.
5. Máy đo: mỗi khối có hình nằm gần góc khung đạt khi lề ≥ R, hoặc hai lề của góc chênh ≤ 1 và R = r + lề ± 1.
   Mẫu và ma trận 15 trường hợp: Figma section Câu 12b (6246:14279).

