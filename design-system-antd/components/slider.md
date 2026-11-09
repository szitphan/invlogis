---
type: design-system-component
status: draft
updated: 2026-11-09
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/switch.md
  - design-system-antd/components/tooltip.md
  - design-system-antd/components/input.md
---

# Slider — `nz-slider`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/slider** (13 ví dụ, đo computed style 08/11): rãnh 8 bo tròn,
> đoạn chọn màu chính, núm viên thuốc 24 × 16 nền sáng, vòng 1px đen 10%, bóng `shadow-md`. Thuộc tính theo
> **API ng-zorro 22.x**. Lựa chọn giữ/bỏ: trang claude.ai/artifact/WaFyJqqdCqEHArsgVHBqKQ (DEC-420).
> Figma kit shadcn chỉ xem được, chưa đối chiếu.
> Slider dùng khi người dùng **ước lượng** trong một dải (bán kính, tải trọng, khoảng giá) và thấy được vị trí trong dải.
> Cần con số chính xác → luôn kèm ô số (Loại `Khoảng có ô số`) hoặc dùng Input số thay Slider.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzRange` | `Kiểu` (variant) | Một giá trị · Khoảng | Khoảng: 2 núm, đoạn chọn nằm giữa |
| `ngModel` | — | | Vị trí núm cố định theo biến thể: Một giá trị 60 %, Khoảng 25–75 % |
| `nzMin` · `nzMax` · `nzStep` | — | | Theo nghiệp vụ |
| `nzTooltipVisible` · `nzTipFormatter` | `Trạng thái` = Rê/Kéo · lớp `Tooltip giá trị` (instance `Tooltip/Base`, đã expose → sửa `Nhãn · chữ`) | `default` | Tooltip chỉ hiện khi rê/kéo. `nzTipFormatter` định dạng số: "60", "7.500.000 ₫" |
| `nzTooltipPlacement` | — | `top` | Giữ mặc định, tooltip phía trên núm |
| `nzDisabled` | `Trạng thái` = Đã tắt | | Cả thanh mờ 50 % |
| (focus bàn phím) | `Trạng thái` = Focus | | Vòng 3px quanh núm như Input; ←/→ đổi một bước |
| `nzMarks` | Khe `Mốc` (boolean) + instance `_Slider/Element/Hàng mốc` | Vạch · Nhãn | Vạch: vạch + nhãn cách quãng (web-03). Nhãn: 3 chữ, không vạch (web-02) |
| (nhãn tự ghép) | Khe `Đầu dòng` (boolean) + instance `_Slider/Element/Đầu dòng` | Một nhãn · Hai nhãn | Phía trên rãnh. Một nhãn (web-10) · Hai nhãn hai đầu (web-06) |
| (output tự ghép) | Khe `Giá trị` (boolean) + `Giá trị · chữ` | | Bên phải thanh, cùng hàng (web-04) |
| (icon tự ghép) | Khe `Icon đầu` · `Icon cuối` (boolean) + instance swap | | Hai bên rãnh (web-05) |
| `nzDots` · `nzVertical` · `nzReverse` · `nzIncluded` | — | | Giữ mặc định, không dựng thanh đứng |

**Không dùng:** web-07 (emoji hai đầu), web-09 (emoji theo giá trị) — trang trí, đánh giá dùng `nz-rate` ·
web-08 (nút − / + hai bên) — ô số đã chỉnh từng bước · web-11, web-12 (thanh đứng), web-13 (bộ chỉnh âm) — chưa có màn cần.

## 2. Thanh trượt

| Phần | Giá trị | Token |
|---|---|---|
| Rãnh | Cao 8, bo tròn, rộng theo cha (set vẽ 240) | `slider/rail-height` · `slider/radius` = `radius/full` |
| Nền rãnh | Xám nhạt như rãnh Switch tắt (Dark: trắng 10 %) | `slider/rail-bg` → `switch/track-bg` |
| Đoạn chọn | Màu chính, từ đầu rãnh tới núm (Khoảng: giữa 2 núm) | `slider/track-bg` → `color/primary` |
| Núm | Viên thuốc 24 × 16, nền sáng cả 2 mode, vòng 1px đen 10 %, bóng `shadow/base` | `slider/handle-width` · `slider/handle-size` · `slider/handle-bg` · `slider/handle-border` · `slider/handle-border-width` |

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Thường | như trên | |
| Rê/Kéo | Quầng 4px quanh núm đang kéo + tooltip giá trị phía trên núm (Tooltip Trên · Một dòng, mũi tên cách mép núm 4) | `slider/handle-ring-width` · `color/focus-ring` · `slider/tooltip-offset` |
| Focus | Vòng 3px quanh núm | `focus/width` · `color/focus-ring` |
| Đã tắt | Mờ 50 % | `opacity/disabled` |

Kiểu Khoảng: quầng/focus/tooltip đặt ở **núm cuối** (núm đang thao tác).

Bố cục: khung thanh **cao bằng rãnh (8)**, núm nằm tràn ra ngoài, không cắt clip. Mọi khoảng cách phần trên và dưới đều
tính **từ mép rãnh**, không tính từ núm.

## 3. Phần đi kèm

| Phần | Giá trị | Token |
|---|---|---|
| Vạch mốc (`Hàng mốc` Vạch) | Ô mốc rộng 20, vạch 1 × 4 (Phụ 1 × 2), màu chữ phụ 70 % | `slider/mark-cell` · `slider/mark-color` · `slider/mark-opacity` |
| Rãnh → vạch | 12, tính từ mép dưới rãnh | `slider/mark-gap` → `spacing/sm` |
| Vạch → nhãn | 8; nhãn 12, màu chữ phụ | `spacing/xs` · `slider/mark-color` |
| Hàng nhãn dưới rãnh (`Hàng mốc` Nhãn) | Cách rãnh 16, 3 chữ dàn đều | `slider/label-gap` → `spacing/md` |
| Nhãn trên rãnh (`Đầu dòng`) | Một nhãn: 14 Medium · Hai nhãn: 12 Medium màu phụ, dàn 2 đầu. Cách rãnh 12 | `slider/mark-gap` |
| Số giá trị (`Giá trị`) | 14 Medium, bên phải thanh, cách 8 | `spacing/xs` |
| Icon hai đầu | Cỡ 20, màu chữ phụ, cách rãnh 16 | `slider/icon-size` · `slider/icon-gap` |

AntD vẽ mốc bằng chấm tròn trên rãnh — bộ thử theo shadcn (vạch dưới rãnh), dev ẩn chấm (`nzDots` = false) và style
lại `.ant-slider-mark`.

## 4. Mẫu dùng (L2)

| Loại | Ghép từ | Dùng ở Invlogis |
|---|---|---|
| `Khoảng có ô số` | `Slider/Base` Khoảng + khe `Đầu dòng` + 2 instance Input đơn vị ₫ | Lọc lệnh, bảng giá theo khoảng cước; gõ ô số thì thanh nhảy theo và ngược lại |
| `Có số giá trị` | `Slider/Base` Một giá trị + khe `Đầu dòng` + khe `Giá trị` | Bán kính tìm xe quanh điểm nhận |
| `Có vạch mốc` | `Slider/Base` Một giá trị + khe `Đầu dòng` + khe `Mốc` Vạch | Lọc xe theo tải trọng hàng |

Trạng thái L2: Thường · Rê/Kéo · Đã tắt. Giới hạn dải (min/max/bước) của từng mẫu là **ví dụ minh hoạ**, không phải tham số
sản phẩm — khi đưa vào SRS thì min/max/bước đi qua mã `P-…` theo `.claude/rules/saas-layer.md`.

## 5. Cấu trúc 3 tầng (dựng lại 09/11 — /ds-antd-component; DEC-420, DEC-421; duyệt claude.ai/artifact/UBxrfatCB6apcTFZXLLKLS)

File `ElvhTYV3unixPkXky2oKIY`, trang **Slider** `71:6016`.

| Tầng | Set | Node | Biến thể |
|---|---|---|---|
| L0 (section `352:273`, khoá) | `_Slider/Element/Núm` | `352:279` | Trạng thái Thường · Rê/Kéo · Focus = 3 |
| L0 | `_Slider/Element/Mốc` | `352:288` | Mức Chính · Phụ = 2; `Nhãn · chữ` |
| L0 | `_Slider/Element/Hàng mốc` | `352:330` | Loại Vạch (9 mốc) · Nhãn (3 chữ) = 2 |
| L0 | `_Slider/Element/Đầu dòng` | `352:336` | Loại Một nhãn · Hai nhãn = 2; `Nhãn · chữ` · `Nhãn phải · chữ` |
| L1 (section `353:2621`) | `Slider/Base` | `353:2622` | Kiểu Một giá trị · Khoảng × Trạng thái Thường · Rê/Kéo · Focus · Đã tắt = 8; khe `Đầu dòng` · `Mốc` · `Icon đầu` · `Icon cuối` · `Giá trị` (mặc định tắt) |
| L2 (section `354:1830`) | `Slider` | `354:1831` | Loại `Khoảng có ô số` · `Có số giá trị` · `Có vạch mốc` × Thường · Rê/Kéo · Đã tắt = 9 |
| Tài liệu | Documentation | `354:2147` | Mô tả · Playground 7 case (Light \| Dark) · Thuộc tính 9 dòng + token 10 dòng |

Tooltip giá trị là instance `Tooltip/Base` `322:240` (Trên · Một dòng), đã expose. Ô số là instance `Input/Base` Nền xám · default.
Kiểm gắn token 09/11: 94/94 giá trị có biến, 19/19 chữ có text style.

## 6. Biến

| Nhóm | Biến | Node |
|---|---|---|
| color | `slider/rail-bg` · `track-bg` · `handle-bg` · `handle-border` · `mark-color` | `VariableID:71:6017…71:6021` |
| size | `slider/rail-height` · `handle-size` · `handle-border-width` · `radius` · `handle-ring-width` · `mark-gap` · `tooltip-offset` | `VariableID:71:6022…71:6028` |
| size (thêm 09/11) | `slider/handle-width` · `mark-cell` · `label-gap` · `icon-size` · `icon-gap` | `VariableID:350:1145…350:1149` |
| size (thêm 09/11) | `slider/mark-opacity` 70 % | `VariableID:365:7778` |
