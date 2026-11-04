---
type: design-foundations
status: approved
updated: 2026-11-03
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Bo góc

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (5.x) để các DEC và spec trích "foundations mục 5…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 5. Bo góc (DEC-165, DEC-315, DEC-328)

Ba tầng như khoảng cách (DEC-315): **primitive** theo px `radius/0 · 2 · 4 · 6 · 8 · 10 · 12 · 16 · 20 · 24 · 9999` (collection
`0. Primitives`, chỉ Semantic trỏ tới) → **thang Semantic Untitled** trong `2. Platform · Radius`:

| `radius/…` | none | xxs | xs | sm | md | lg | xl | 2xl | 3xl | 4xl | full |
|---|---|---|---|---|---|---|---|---|---|---|---|
| px | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 16 | 20 | 24 | tròn hẳn |

→ **token theo vai** (bảng dưới, trỏ thang Semantic) và token component còn lại (đang gộp về token chung, DEC-319). Component
và token component không trỏ primitive `radius/<px>`.

**Web và App đã gộp một bộ (DEC-328).** Mọi vai cùng số trên hai nền, không còn vai nào khác nhau. Cấu trúc Platform giữ
nguyên: collection vẫn có hai mode Web, Mobile, hai mode bằng nhau, để đổi lại sau này không phải đổi cách gắn biến.

| Token | Web = App | Trỏ | Dùng cho |
|---|---|---|---|
| `radius/control` | 8 | `radius/md` | Nút, tab chip, ô tìm. App bỏ viên thuốc |
| `radius/field` | 8 | `radius/md` | Ô nhập, ô chọn |
| `radius/inner` | 8 | `radius/md` | Khối phụ trong thẻ, ảnh nhỏ, ô icon vuông, Featured icon vuông |
| `radius/card` | 12 | `radius/xl` | Thẻ, nhóm có viền, khối trong trang, bảng |
| `radius/overlay` | 20 | `radius/3xl` | Hộp thoại, hộp thoại tìm, mọi sheet (sheet chỉ bo hai góc trên) |
| `radius/menu` | 10 | `radius/lg` | Menu thả, popover danh sách, menu tài khoản |
| `radius/menu-item` | 6 | `radius/sm` | Mục trong menu |
| `radius/badge` | 6 | `radius/sm` | Badge vuông cho nhãn phân loại (không phải trạng thái) |

Pill, avatar tròn, vòng icon gọi thẳng `radius/full`. Thang đủ 11 bậc của Untitled nên 20 có sẵn là `radius/3xl`, không thêm bậc.

Đã bỏ (DEC-328): `radius/tab` (gộp vào `radius/control`; ô hình, ảnh nhỏ sang `radius/inner`), `radius/chip` (không ai gọi),
`chip/count-radius` (Badge SM, MD gọi `radius/xxs` 2), `upload/sheet-radius` (gọi `radius/overlay`). Badge LG, Avatar XL
không mượn `radius/menu` nữa mà gọi `radius/md`, nhìn vẫn 8.

Từ DEC-315 tên theo cỡ (`radius/md`, CSS `--radius-md`) là tầng Semantic, primitive đổi sang tên theo px (`--radius-8`); token theo vai
(`--radius-card`…) giữ tên.

**Luật lồng góc và lề đều (DEC-165).** R là bo khung ngoài, r là bo khối bên trong, lề là khoảng từ mép khung tới mép khối.

1. Khung có khối hình ở góc (ô icon, avatar, nút, ô nhập, khối phụ, công tắc) thì lề 4 phía bằng nhau, đo tới khối cao
   nhất trong dòng. Chữ không có góc để khớp, chỉ cần lề đều.
2. Khung lớn (thẻ, nhóm có viền) **tách xa**: bo không quá lề (thẻ 12 dưới lề 16, cả web và app). Khối bên trong khi đó
   chỉ đối diện cạnh thẳng nên giữ hình gì cũng được: ô icon tròn, avatar tròn, nút 8, ô nhập 8.
3. Khung ôm sát một khối (dòng đang chọn, chip, ô tìm) **đồng tâm**: R = r + lề. Hình tròn, viên thuốc có r = cao ÷ 2 nên
   R = cao ÷ 2 + lề, ôm sát thì khung cũng thành viên thuốc. Ví dụ: dòng đang chọn có ô vuông bo 8, lề 8 thì bo 16.
4. Lồng nhiều lớp thì áp từng lớp.
5. Máy đo: mỗi khối có hình nằm gần góc khung đạt khi lề ≥ R, hoặc hai lề của góc chênh ≤ 1 và R = r + lề ± 1.
   Mẫu và ma trận 15 trường hợp: Figma section Câu 12b (6246:14279).

### 5.1 Bảng đồng tâm theo số mới

| Khung | R | lề | r | R = r + lề |
|---|---|---|---|---|
| Menu thả, menu tài khoản, menu breadcrumbs | 10 `radius/menu` | 4 `space/xs` | 6 `radius/menu-item` | 6 + 4 = 10 |
| Badge MD có ô đếm | 6 `radius/badge` | 4 `space/xs` | 2 `radius/xxs` | 2 + 4 = 6 |
| Badge SM có ô đếm | 6 `radius/badge` | 3 `chip/count-inset` | 2 `radius/xxs` | 2 + 3 = 5, trong sai số ±1 |
| Badge LG có ô đếm | 8 `radius/md` | 4 `space/xs` | 4 `radius/xs` | 4 + 4 = 8 |
| Thẻ phạm vi Sidebar thu gọn | 8 `radius/md` | 4 `space/xs` | 4 `radius/xs` | 4 + 4 = 8 |

### 5.2 Máy đo sau số mới

Tính lại 25 ca của trang review Bo góc trên `tokens.css` 0.26.0 (luật 5): **22 đạt · 2 rớt · 1 ngoài vùng góc**.

| Ca | Nền | R | Lề | r | Kết quả | Nguồn |
|---|---|---|---|---|---|---|
| Nút trong thẻ | Web | 12 | 16 | 8 | Đạt | thẻ trên màn chi tiết web |
| Nút trong thẻ | App | 12 | 16 | 8 | Đạt | thẻ Lệnh app |
| Ô nhập trong thẻ | Web | 12 | 16 | 8 | Đạt | biểu mẫu web |
| Ô nhập trong thẻ | App | 12 | 16 | 8 | Đạt | biểu mẫu app |
| Khối phụ trong thẻ | App | 12 | 16 | 8 | Đạt | Combo Slots trong thẻ Lệnh |
| Ảnh nhỏ trong dòng tệp | Web | 12 | 12 | 8 | Đạt | field-upload, dòng tệp, `radius/inner` |
| Badge trên Vehicle Card | Web | 12 | 12 | 11 | Đạt | vehicle-card, ghim cách góc 12 |
| Badge trên Vehicle Card | App | 12 | 12 | 11 | Đạt | vehicle-card bản app |
| Vòng icon trong ô bấm tải lên | App | 12 | 12 | 24 | Đạt | field-upload bản app |
| Khe Container trong khối mooc | Web | 8 | 8 | 8 | Đạt | combo-slots lề 8 + container-slot |
| Khe Container trong khối mooc | App | 8 | 8 | 8 | Đạt | combo-slots Compact trên app |
| Vòng icon trong thông báo | Web | 12 | 12 | 16 | Đạt | alert-notification, web = app |
| Icon trong Alert | Web | 10 | 12 | 6 | Đạt | alert-notification, web = app |
| Ô module trong thẻ phạm vi | Web | 8 | 8 / 10 | 8 | Đạt | sidebar-navigation, dạng mở |
| Ô module khi menu thu gọn | Web | 8 | 4 | 4 | Đạt | sidebar-navigation, dạng thu gọn (ngoại lệ `radius/xs`) |
| Mục trong menu thả | Web | 10 | 4 | 6 | Đạt | header-navigation, menu tầng ẩn |
| Mục trong menu breadcrumbs | Web | 10 | 4 | 6 | Đạt | breadcrumbs, menu tầng ẩn |
| Mục trong menu tài khoản | Web | 10 | 4 | 6 | Đạt | header-navigation, `radius/menu`, lề `space/xs` |
| Ô đếm trong Badge SM | Web | 6 | 3 | 2 | Đạt | badge, lề 3, `radius/xxs` |
| Ô đếm trong Badge MD | Web | 6 | 4 | 2 | Đạt | badge, lề 4, `radius/xxs` |
| Ô đếm trong Badge LG | Web | 8 | 4 | 4 | Đạt | badge, lề 4, khung `radius/md` |
| Nút lọc trong ô tìm | App | 8 | 4 | 8 | **Rớt** | DEC-196, ô tìm app `radius/control`, nút chưa có spec, tính theo r = `radius/control` |
| Nút trong hộp thoại | Web | 20 | 20 | 8 | Đạt | hộp xác nhận web, lề 20 |
| Ô nhập trong sheet, sau tiêu đề | App | 20 | 20 / 62 | 8 | Ngoài vùng góc | sheet app, cách mép trên 62 |
| Avatar đầu sheet tài khoản | App | 20 | 12 / 24 | 16 | **Rớt** | header-navigation, `radius/overlay`; lề trên chưa ghi, tạm lấy 24 |

Hai ca còn rớt, chưa có quyết định:

- **Nút lọc trong ô tìm trên app.** Ca mới do bỏ viên thuốc: DEC-196 đo trên ô tìm tròn hẳn; nay ô tìm R 8, lề 4 thì nút lọc phải r 4 (`radius/xs`) mới đồng tâm. Nút lọc chưa có spec component nên chưa đổi.
- **Avatar đầu sheet tài khoản.** Rớt cả trước và sau đổi (R 16 → 20, lề ngang 12); lề trên chưa ghi trong spec.

**Ba ca trên app rớt ở số cũ, nay đạt không đổi lề (DEC-328):** Badge trên Vehicle Card (R 12, cách góc 12), vòng icon trong ô bấm
tải lên (R 12, lề 12), khe Container trong khối mooc (R 8, lề 8). `upload/app-tap-min-height` giữ 72, lề ô bấm giữ `space/lg` 12.

### 5.3 Ngoại lệ

- **Ô module khi Sidebar thu gọn gọi `radius/xs` 4, không gọi `radius/inner`** (DEC-328). Ô 32 trong khung 40, lề 4: nếu r 8 thì
  cần R 12, mà khung thu gọn là 8. Dạng mở và hộp thoại vẫn `radius/inner` 8.

### 5.4 Corner smoothing (DEC-328)

Góc liền mạch 60% cho **thẻ và sheet trên App**. Không có token, vì Figma không gắn biến được cho thuộc tính này.

| Nơi | Cách làm |
|---|---|
| Figma | Nhập tay Corner smoothing 60% từng khung thẻ, sheet trên App |
| Flutter (`docs/_shared/system-overview.md`) | `RoundedSuperellipseBorder` đặt một chỗ ở theme (vd `CardThemeData.shape`). Tài liệu chưa ghi bản Flutter dự án dùng; dev kiểm bản đó có widget này |
| Web | Góc thường. CSS `corner-shape` chưa Baseline |
