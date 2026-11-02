---
type: design-component
status: draft
updated: 2026-11-02
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/foundations/logo.md
  - design-system/tokens.json
  - design/brand/invlogis/logo/logo-spec.md
  - design/brand/delta/logo/logo-spec.md
  - docs/_product/tenant-parameters.md
  - _workspace/decisions.md
---

# Logo

> Base · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · DEC-326 (gộp set `Logo`, `Company logo` của DEC-261) · luật dùng:
> `design-system/foundations/logo.md` mục 14 · Figma: set `Logo` 6681:227878 ở DS · Foundations › Logos (Owner × Type × Theme × Size, 30 biến thể).

Một component cho logo sản phẩm và logo khách, phân biệt bằng trục `Owner`. Sau này có thêm khách, cấu trúc và biến thể như
nhau, chỉ khác tệp. Nhóm A (DEC-279): một bộ, cùng số đo web và app.

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Owner = Invlogis:** logo sản phẩm, khi chưa biết khách. **Owner = Khách:** tệp lấy từ `P-logo`, `P-logo-nen-toi`, `P-logo-vuong`.
- **Type = Logo:** logo ngang. **Type = Symbol:** ký hiệu, cho chỗ không đủ rộng. Không có xếp dọc, đơn sắc, khẩu hiệu, "by innvie"
  (foundations mục 14.2).
- Theme đổi theo chế độ của app, không theo hệ điều hành.
- Không bấm được trong spec này. Bấm về trang chủ, nếu có, do thanh chứa lo.

### Biến thể

| Trục | Giá trị | Mặc định |
|---|---|---|
| Owner | Invlogis · Khách | Invlogis |
| Type | Logo · Symbol | Logo |
| Theme | Light · Dark | Light |
| Size | 24 · 40 · 64 (Symbol chỉ 24) | 24 |

### Cấu tạo

| Phần | Token | Giá trị |
|---|---|---|
| Cao, Size 24 | `size/3xl` | 24 |
| Cao, Size 40 | `size/5xl` | 40 |
| Cao, Size 64 | `size/7xl` | 64 |
| Rộng | theo tỉ lệ tệp, không kéo méo, không cắt | — |
| Vùng trống | 1 x; trong thanh điều hướng 0,5 x (`x` ≈ 0,52 cao, foundations mục 14.3); do chỗ đặt giữ | ở cao 24: 12,5 · 6,2 |
| Ô chữ cái đầu | vuông bằng cao logo, nền `P-mau-logo`, bo `radius/md`, chữ `color/text/white` hoặc #171717 theo tương phản cao hơn | Mặc định #262626 |
| Ô trắng (Dark, khách thiếu `P-logo-nen-toi`) | nền trắng cố định, lề `space/sm`, bo `radius/md` | ở cao 24: khung 36 |

Tệp theo từng ô (tên tệp Khách lấy Delta làm ví dụ):

| Owner · Type | Light | Dark |
|---|---|---|
| Invlogis · Logo | `invlogis-primary.svg` | `invlogis-reverse.svg` |
| Invlogis · Symbol | `invlogis-symbol-small.svg` | `invlogis-symbol-small-reverse.svg` |
| Khách · Logo | `P-logo` (`delta-primary.svg`) | `P-logo-nen-toi` (`delta-reverse.svg`) |
| Khách · Symbol | `P-logo-vuong` (`delta-symbol.svg`) | `delta-symbol-reverse.svg` |

### Trạng thái dữ liệu

Không có hover, focus. Chỉ có trạng thái theo tệp khách nộp:

| Trường hợp | Hiển thị |
|---|---|
| Đủ tệp | Tệp đặt thẳng trên nền, không tô ô |
| Thiếu `P-logo` | Ô chữ cái đầu tên khách |
| Dark, thiếu `P-logo-nen-toi` | Tệp chính trên ô trắng; riêng splash thì cả màn giữ nền trắng |
| Symbol, thiếu `P-logo-vuong` | Ô chữ cái đầu |
| Tệp quá rộng cho chỗ đặt | Hạ cao, không dưới 20; không cắt |

### Kích thước

| Chỗ dùng | Type · Size |
|---|---|
| Đầu menu web, màn chủ app | Logo · 24 |
| Menu thu gọn 64, thanh trên mobile web | Symbol · 24 |
| Đăng nhập | Logo · 40 |
| Splash | Logo · 64; trên app rộng tối đa bằng màn trừ lề, Delta còn cao khoảng 61 |

Cao tối thiểu 20 ở mọi Owner.

### Nên và không nên

- **Nên** dùng instance component này, không dán SVG rời vào màn.
- **Không nên** đặt Symbol cạnh Logo: hai chữ i lụa liền nhau (`logo-spec.md` Mục 5).
- **Không nên** tô ô `P-mau-logo` sau logo thật.
- **Không nên** tự đổi logo khách sang trắng bằng code ở chế độ Tối.
- **Không nên** gắn cỡ logo vào `control/height/*`: đó là vai control, control đổi thì logo đổi theo.
- **Không nên** dùng `--invlogis-*`, `--innvie-*` trong component sản phẩm (DEC-261).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.1.1 Văn bản thay thế | ✓ | Có nghĩa: tên sản phẩm hoặc tên khách. Cạnh tên đơn vị đã hiện chữ thì để trống, tránh đọc 2 lần |
| 1.4.11 Tương phản ngoài chữ (≥ 3) | ✓ | Invlogis Symbol Light 4,87 · 3,84 trên trắng; Dark 8,55 · 13,01 trên #191919. Delta chữ 17,43 / trắng, 17,58 / Tối; thanh xanh 3,75 / trắng, 4,69 / Tối |
| 1.4.3 Tương phản chữ (ô chữ cái) | ✓ | Trắng trên #262626 15,13; trắng trên #1B7B46 5,29 |
| 1.4.1 Không chỉ dùng màu | — | Không mang nghĩa trạng thái |

### Thuộc tính

`Owner`, `Type`, `Theme`, `Size` (biến thể). `Has File` (Owner Khách, tắt thì hiện ô chữ cái), `White Plate` (Theme Dark, Owner Khách,
bật khi khách thiếu tệp nền tối), lớp chữ `Initial`.

### Được dùng trong

Sidebar navigation (đầu menu), Header navigation (khối Mobile), Error page (màn toàn trang), đăng nhập, splash, màn chủ app.

### Chuyển động

Splash: nhịp phóng tối đa min(115%, rộng màn ÷ rộng logo), Delta 108,9% trên 393, 111,1% trên 320; web giữ 115%. Bốn số của kịch bản splash là số riêng, không qua `duration/*`. Luật chung: `foundations/motion.md` (DEC-333).

## Mobile

> Khối Mobile đặt mode Platform = Mobile. Số đo như Web: `size/*` cùng giá trị ở hai mode.

- App: màn chủ, splash, đăng nhập có logo; màn con giữ tiêu đề + quay lại, không logo.
- Web trên điện thoại: mọi màn có logo, dùng Symbol 24.

## Đối chiếu Untitled

- `UntitledLogo`, `UntitledLogoMinimal` ở `react/components/foundations/logo`, đổi chế độ bằng `fill-fg-primary`. Mình giữ 2 tệp vì logo có
  gradient, không đổi màu bằng token.
- Untitled cao `h-6` = 24 ở điều hướng, `size-6` ở thanh Slim: khớp Size 24.
- Untitled không có logo theo khách: trục `Owner`, ô chữ cái, ô trắng là phần của mình.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
