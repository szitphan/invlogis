---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/input.md
---

# Select — `nz-select`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/select** (15 ví dụ, registry `select1…15`) và
> **/components/combobox** (12 ví dụ, `combobox1…12`); thuộc tính theo **API ng-zorro 22.x**. Ở ng-zorro select và
> combobox là **một** `nz-select` (combobox = `nzShowSearch`), nên mọi ô chọn dùng **một kiểu ô**: giống Input — nền xám,
> không viền. Lựa chọn giữ/bỏ: trang claude.ai/artifact/3eRLKXBhZLRfpBS1rcJ6Bx tab Select (user bấm 06/11): theo cột
> đề xuất, **giữ thêm** `tags`, Không nền, web-03, web-13, cbx-08.
> Bo góc theo Input (chốt 07/11 bo kit): ô dùng `input/radius` = `radius/lg` 10, menu `radius/base` 8, mục `radius/sm` 6.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzSize` | `Cỡ` (variant) | sm · default · lg | 32 · 36 · 40, như Input |
| `nzBorderless` | `Kiểu` (variant) | Nền xám · Không nền | Không nền: chọn tại chỗ trong ô bảng (giữ 06/11) |
| `nzStatus` / `nzOpen` / `nzDisabled` | `Trạng thái` (variant) | Chờ chọn · Đã chọn · Mở · Lỗi · Cảnh báo · Đã tắt | Mở = vòng 3px như Focus của Input |
| `nzPlaceHolder` / giá trị | `Gợi ý` · `Chữ` (text) | | Hai lớp chữ tách như Input |
| `nzPrefix` (dev kiểm có trong 22.x) | `Icon đầu` (boolean) + `Icon đầu · chọn` (swap) | | Icon loại dữ liệu: đồng hồ, xe, địa điểm |
| `nzAllowClear` | `Nút xoá` (boolean) | | ⓧ cạnh mũi tên, chỉ khi đã chọn |
| `nzSuffixIcon` | — | chevron-down 16, mờ 50% | Luôn có, không tắt |
| `nzMode="multiple"` · `"tags"` | **Component riêng `Multiselect`** (user chốt 07/11) | Chế độ Chọn nhiều · Thẻ tự gõ × Trạng thái | Thẻ đã chọn: nhãn 20 nền trắng trên ô xám; Mở có menu dính dưới ô |
| `nzOpen` | `Trạng thái` = Mở | | **Biến thể Mở chứa instance `Menu` dính dưới ô** (đặt tuyệt đối, rộng theo ô, exposed) — chọn Mở là thấy menu, sửa Ô tìm / Chân menu / Loại / Thanh cuộn / từng mục ngay trên instance (user yêu cầu 07/11) |
| `nz-form-control nzExtra` / `nzErrorTip` | `Dòng gợi ý` (boolean) + `Dòng gợi ý · chữ` (text) | | Chữ 12 dưới ô, cách 6; Lỗi chữ đỏ (web-05, web-06) |
| `nzCustomContent` 2 dòng | `Dòng phụ` (boolean) + `Dòng phụ · chữ` (text) | | Dòng 12 mờ dưới tên, ô tự cao 52 (web-13, đi cùng `Icon đầu` = Ảnh 20) |
| `nzShowSearch` · `nzServerSearch` · `nzLoading` | Set `Select menu`: `Ô tìm` (boolean) · `Loại` = Đang tải | | Tìm gõ ngay trong ô (cbx) hoặc ô tìm đầu menu (web-14) |
| `nz-option-group nzLabel` | `Select mục` Loại = Tiêu đề nhóm | | Chữ 12 mờ |
| `nz-option nzDisabled` | `Select mục` Loại = Khoá | | Mờ 50%, có thể kèm icon ổ khoá (cbx-07) |
| `nzCustomContent` | `Select mục`: `Đầu` (boolean + swap) · `Mô tả` (boolean + text) | | Chấm trạng thái, icon, ảnh 20 · dòng mô tả 12 |
| `nzDropdownRender` | `Select menu`: `Chân menu` (boolean) | | Nút "Thêm mới" cuối menu (web-15) |
| `nzVirtualScroll` | — | | Danh sách > 100 mục (cbx-08), hình không khác |

**Không dùng:** web-08 (nhãn nổi trên mép ô — ô xám không có mép) · cbx-02 (menu rộng bằng ô là mặc định) ·
cbx-04 (= Nhóm + Tìm) · cbx-05 (= web-10) · cbx-06 (= web-11) · cbx-12 (= web-15).

## 2. Ô chọn

Theo Input (Mục 2–3 của `input.md`): cao `height/sm` 32 · `input/height/base` 36 · `height/lg` 40, padding ngang
`input/padding-x` 12, nền `color/input-bg`, bo `input/radius`, chữ 14 Geist Regular, gợi ý `color/input-placeholder`.
Mũi tên: `select/arrow-size` 16, mờ `select/arrow-opacity` 50%, cách chữ 8.

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Chờ chọn | Chữ gợi ý mờ | `color/input-placeholder` |
| Đã chọn | Chữ đậm màu | `color/text` |
| Mở | Vòng 3px ngoài ô + menu xổ dưới, cách 4 | `focus/width` · `color/focus-ring` |
| Lỗi | Viền 1px đỏ + vòng đỏ 20% | `color/error` |
| Cảnh báo | Viền 1px vàng + vòng vàng 20% | `color/warning` |
| Đã tắt | Mờ 50% | `opacity/disabled` |

**Multiselect** (`nzMode="multiple"` / `"tags"`): ô cao tối thiểu 36, padding 4 · 6, thẻ cách 4, xuống dòng khi đầy
(ô cao dần; bo `textarea/radius` khi > 1 hàng). Thẻ: cao `tag/height` 20, bo `tag/radius`, nền `color/body-bg`, chữ 12
Medium, nút x 12 mờ 60%. Thẻ tự gõ: chữ gợi ý "Gõ rồi Enter…" sau thẻ cuối.

## 3. Menu xổ — `Select menu` + `Select mục`

| Phần | Giá trị | Token |
|---|---|---|
| Khung | nền `color/popover-bg`, viền 1px `color/border-base`, bo 8, bóng `shadow/base`, padding 4, rộng ≥ 128 (mặc định = ô) | `select/dropdown-radius` = `radius/base` · `select/dropdown-padding` 4 |
| Mục | padding 6 · 8, phải 32 (chừa ✓), bo 6, chữ 14 | `select/item-padding-y` 6 · `select/item-padding-x` 8 · `select/item-radius` = `radius/sm` |
| Rê chuột | nền xám nhạt | `color/item-hover-bg` |
| Đã chọn | nền xám nhạt + ✓ 16 bên phải | `color/item-active-bg` |
| Khoá | mờ 50% | `opacity/disabled` |
| Tiêu đề nhóm | chữ 12 `color/text-secondary`, padding 6 · 8 | |
| Mô tả | chữ 12 `color/text-secondary`, dưới tên cách 2 | |
| Đầu mục | icon 16 `color/text-secondary` · chấm 8 màu trạng thái · ảnh 20 bo 6 — cách chữ 8 | |
| Ô tìm đầu menu | icon tìm + chữ, cao 36, vạch dưới 1px `color/border-split` | |
| Chân menu | vạch trên 1px, nút ghost "+ Thêm …" | |
| Đang tải | vòng xoay 14 + "Đang tìm…" giữa, padding 16 | |

## 4. Ví dụ đã chốt (duyệt 07/11, trang claude.ai/artifact/A6qSRpB5F19i7iQtnfDXPW)

Mẫu ghép không còn là component riêng: mọi thẻ trong khung `Ví dụ đã chốt` là instance `Select` (Mở → menu lồng đã đặt mục) / `Multiselect` + `Label`. web-02 "Rộng theo nội dung" = đặt instance Hug (không cần thuộc tính).

## 4.0 Bảng cũ

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| web-01 | Chữ gợi ý, rộng hết ô | `nzPlaceHolder` | Ô chọn chuẩn trong form: "Chọn loại xe" |
| web-02 | Rộng theo nội dung | `nz-select` không đặt rộng | Bộ lọc thanh công cụ: "Trạng thái: Tất cả" |
| web-03 | Chữ gợi ý + menu mở | `nzPlaceHolder` + `nzOpen` | Chọn tuyến — hình menu mở (giữ 06/11, khác web-01 ở chỗ hiện menu) |
| web-04 | Icon đầu ô | `nzPrefix` (dev kiểm) | Khung giờ giao, ca làm — icon đồng hồ |
| web-05 | Dòng gợi ý dưới ô | `nz-form-control nzExtra` | "Xe được gán theo đội của tài xế" |
| web-06 | Báo lỗi | `nzStatus="error"` + `nzErrorTip` | Thiếu loại hàng |
| web-07 | Nhóm có tiêu đề | `nz-option-group` | Xe theo đội, điểm giao theo tỉnh |
| web-09 | Mục có chấm màu trạng thái | `nzCustomContent` | Lọc trạng thái lệnh |
| web-10 | Mục có icon | `nzCustomContent` | Loại phương tiện: đầu kéo, xe tải, mooc |
| web-11 | Mục có mô tả, ô chỉ hiện tên | `nzCustomContent` + `nzLabel` | Loại dịch vụ, loại hàng |
| web-12 | Ảnh 20 + tiêu đề nhóm | `nz-option-group` + `nzCustomContent` | Tài xế, người phụ trách |
| web-13 | Ô 2 dòng: ảnh 24 + tên + SĐT | `nzCustomContent` (cả ô) | Chọn tài xế khi cần thấy SĐT ngay trên ô (giữ 06/11; ô cao 48 — dùng riêng, không đặt cạnh ô 36) |
| web-14 | Ô tìm đầu menu | `nzShowSearch` | Danh sách dài: xe, tài xế, khách hàng |
| web-15 | Tìm + "Thêm mới" cuối menu | `nzShowSearch` + `nzDropdownRender` | Chọn khách hàng — "+ Thêm khách mới" |
| cbx-01 | Gõ tìm ngay trong ô | `nzShowSearch` | Ô chọn có tìm |
| cbx-03 | Chọn nhiều, thẻ trong ô | `nzMode="multiple"` | Lọc nhiều tuyến, nhiều khách |
| cbx-07 | Mục khoá có ổ khoá | `nzDisabled` + `nzCustomContent` | Xe đang bảo dưỡng, tài xế nghỉ |
| cbx-08 | Danh sách dài | `nzVirtualScroll` | 63 tỉnh/thành, > 100 xe (giữ 06/11) — Select menu `Thanh cuộn` |
| cbx-09 | Tìm trên máy chủ, đang tải | `nzServerSearch` + `nzLoading` | Gõ tên khách/biển số |
| cbx-10 | Nút xoá trong ô | `nzAllowClear` | Bộ lọc không bắt buộc |
| cbx-11 | Nhóm "Gần đây" lên đầu | `nz-option-group` + `nzCustomContent` | Tuyến/khách điều phối hằng ngày |
| tags | Thẻ tự gõ | `nzMode="tags"` | Giữ 06/11 — đề xuất cũ bỏ vì dễ sinh dữ liệu bẩn; chỉ dùng cho nhãn tự do (ghi chú đơn), không dùng cho danh mục |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Select** (`55:4005`) — nhân bản từ trang Input rồi đổi (dựng 07/11, chờ duyệt):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Select` (tài liệu) | `55:4358` | Đầu trang · Playground **Light** `55:4366` / **Dark** `55:4383` (cỡ, 6 trạng thái, Không nền, chọn nhiều, thẻ tự gõ, menu) · `Ví dụ đã chốt` `55:4400` (22 thẻ) · `Mapping` `55:4466` (10 thuộc tính + 10 token) |
| Section Components | `55:4006` | Set `Select` `55:4007` = Kiểu (2) × Cỡ (3) × Trạng thái (6) = **36**, ma trận như Input · Set `Select mục` `63:620` (5 Loại) · Set `Select menu` `64:657` (Danh sách · Đang tải) · `Select thẻ` `64:661` · Set `Multiselect` `64:723` (đổi tên từ Select nhiều 07/11) = Chế độ (2) × Trạng thái (3) · `Select đầu/Chấm trạng thái` `63:567` (khung 16, chấm 8) · `Select đầu/Ảnh 20` `63:568` |
| Section Mẫu ghép cũ — chờ xoá | `55:4336` | (giữ, chưa xoá) 22 component `Select mẫu ghép/{mã} …` (`65:1600`…`65:1621`) |
| Icons (trang Button) | `55:3981` clock · `55:3988` truck · `55:3994` package · `55:3998` lock · `55:4004` user-plus | lucide 16 |
| Biến mới (collection size) | `select/arrow-size` · `arrow-opacity` · `dropdown-padding` · `dropdown-radius` · `dropdown-min-width` · `item-padding-y` · `item-padding-x` · `item-padding-right` · `item-radius` | `VariableID:62:2…62:10` |

Thuộc tính Select: `Gợi ý` · `Chữ` · `Icon đầu` + `Icon đầu · chọn` · `Nút xoá` + `Nút xoá · icon`. Mũi tên là lớp cố định
(chevron-down, gắn `select/arrow-opacity`). Select mục: `Chữ` · `Đầu` + `Đầu · chọn` (gợi ý: icon xe, chấm, ảnh 20) ·
`Mô tả` + `Mô tả · chữ`. Select menu: `Ô tìm` + `Ô tìm · chữ` · `Chân menu` + `Chân menu · chữ`.

Menu trong mẫu ghép là **khung ghép** cùng token với `Select menu` (nền, viền, bo, bóng, padding), bên trong là instance
`Select mục` — vì instance không thêm/bớt được mục. Chỉ cbx-09 (đang tải) dùng thẳng instance `Select menu`.
Chưa xong: ảnh 20 khi đặt vào ô `Icon đầu` đang co về 16 (ô icon 16) — sửa khi duyệt nếu cần đúng 20.

Cập nhật 07/11 (áp trang duyệt mẫu ghép): mỗi biến thể Select = khung dọc (`Ô` + `Dòng gợi ý` + `Menu` khi Mở); `Ô` cao tối thiểu = biến cao (minHeight), hug khi bật `Dòng phụ`
(khối chữ có `Đệm trên/dưới` 8 ẩn hiện theo `Dòng phụ`). Select menu: `Thanh cuộn` (boolean) + Danh sách 8 mục (4 mục cuối ẩn sẵn, bật trên instance).
Sửa lỗi cũ: biến thể Nền xám · sm ở cột Cảnh báo bị đặt tên trùng "Mở" → đã đổi đúng tên. Bảng Mapping trên Figma thêm 5 dòng (`95:30994`…`95:31014`).
