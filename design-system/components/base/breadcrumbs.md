---
type: design-component
status: stale
status_prev: draft
updated: 2026-10-28
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/tokens.json
  - design-system/components/application/header-navigation.md
  - design-system/components/_work/header-navigation/page.json
  - _workspace/decisions.md
---

# Breadcrumbs

> Base · phiên bản 0.3.0 · Nháp · người phụ trách @szitphan · Figma: trang DS · Application components — `Breadcrumbs`
> 6901:20705 — biến thể gốc Type=Text, Collapsed=False 6768:190544 (nâng cấp tại chỗ từ `_Header breadcrumb`: gộp bằng
> `use_figma` combineAsVariants để giữ id, 51 instance giữ chữ); bộ Astryx cũ đổi tên `Astryx / Breadcrumbs` 44:14946 ·
> DEC-290 · trang duyệt https://claude.ai/artifact/Ua29VuBKRsRys51EYujU3P

Đường dẫn từ trang gốc tới trang hiện tại. Chỉ web (trang Application: breadcrumb mobile = web); dưới 768 thanh trên thay
bằng hàng "← cấp trên" (xem `application/header-navigation.md` mục Mobile). Một bộ, ba Type theo Untitled; sản phẩm dùng
**Type Text** ở thanh trên (D6 A), Button và Text Line có trong bộ cho chỗ khác cần.

## Web

> Khối Web đặt mode Platform = Web.

### Tổng quan

- Thứ tự: icon Nhà (tên đọc "Trang chủ") · tầng 1 · … · tầng cuối · **trang hiện tại** (đậm, không bấm được,
  `aria-current="page"`). Phân cách là chevron phải.
- **Đường dẫn dài** (D7 A): từ 4 tầng trở lên giữ tầng đầu + tầng cuối + trang hiện tại, gom các tầng giữa thành nút
  "…". Bấm "…" mở menu liệt kê các tầng ẩn theo thứ tự.
- Mỗi mục 1 dòng: tầng cha cắt "…" sau 160, trang hiện tại cắt sau 240 (`tooltip/max-width`), tooltip đủ chữ. Thanh thiếu
  chỗ thì đường dẫn co trước các phần khác.

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Khung | auto layout ngang, khoảng `space/xxs` 2, căn giữa dọc | ôm nội dung, co được |
| Mục (tầng cha) | `type/label` 14/20 nét 500, `color/text/tertiary`; hover `color/text/primary` | tối đa 160 |
| Trang hiện tại | text style `type/heading` (14/20 600), `color/text/primary`; Type Text: khung giãn theo chỗ còn lại, tối đa 240 — thiếu chỗ thì co và cắt trước | tối đa 240 |
| Nhà | icon `home` 16 `color/fg/quaternary` | vùng bấm 24 |
| Phân cách | icon `chevron-right` 14 `color/border/primary`, ô 16 | — |
| Nút "…" | icon `dots` 16, rộng 24; mở: nền `color/bg/selected` bo `radius/sm` | vùng bấm 24 |
| Menu tầng ẩn | `Dropdown menu`: rộng tối thiểu 240, bo `radius/lg`, lề 4, bóng `elev/3`; mục cao 36 lề `space/lg` bo `radius/sm` | cách nút 8 |
| Type Button | mục cao 28, lề ngang `space/md`, bo `radius/sm`; hover nền `color/bg/primary_hover`; trang hiện tại nền `color/bg/secondary` | ô phân cách 12 |
| Type Text Line | mục cao 36; trang hiện tại vạch dưới 2 `color/focus/ring`; hover vạch `color/border/primary` | — |
| Vòng focus | `focus/width` 2 cách `focus/offset` 2 `color/focus/ring`, bo `radius/sm` | — |

### Biến thể

- `Breadcrumbs`: Type = Text · Button · Text Line × Collapsed = False · True (6 biến thể). Số tầng bằng bật tắt:
  1 tầng = tắt `Has Parent`; 2 tầng = mặc định; 3 tầng = bật `Has Root`; ≥ 4 tầng = Collapsed=True + `Has Root`
  (Root · … · Parent · Current). `Has Home` tắt khi không cần icon nhà.
- Hover / Focus / "…" đang mở không là biến thể: vẽ minh hoạ ở khung tài liệu và trang duyệt; code làm theo bảng Cấu tạo.

### Trạng thái

Default · Hover · Focus (bàn phím) · Current · "…" đang mở · Chữ dài (cắt + tooltip).

### Kích thước

Một cỡ (14/20). Type Button 28, Text Line 36, Text 20.

### Nên và không nên

- Nên: một đường dẫn mỗi màn, ở thanh trên.
- Nên: tên tầng đúng tên mục menu / tiêu đề màn đích.
- Không: đặt trang hiện tại thành link.
- Không: dùng đường dẫn thay tab hay bước (Progress steps).

### Trợ năng — chấm theo WCAG 2.2

- 1.4.3: mục `text/tertiary` 4,74:1, hiện tại `text/primary` 17,7:1 trên nền trắng.
- 1.3.1 / 4.1.2: `nav aria-label="Đường dẫn"` chứa danh sách có thứ tự; trang hiện tại `aria-current="page"`; Nhà có tên
  "Trang chủ"; "…" là nút `aria-expanded`, tên "Hiện các tầng ẩn".
- 2.4.7 / 2.4.11: vòng focus trên mọi mục bấm được.
- 2.5.8: Type Text cao 20 nhưng mục cách nhau đủ để vòng tròn 24 quanh tâm không chồng; Nhà và "…" vùng bấm 24.
- 1.4.13: tooltip chữ bị cắt hiện cả khi focus, Esc đóng.

### Thuộc tính

`Breadcrumbs`: `Root`, `Parent`, `Current` (TEXT), `Has Home`, `Has Root`, `Has Parent` (BOOLEAN), Type, Collapsed
(VARIANT). Giữ tên thuộc tính cũ của `_Header breadcrumb` để instance không mất chữ.

### Thành phần lồng

`Dropdown menu` (menu tầng ẩn, ghép ở chỗ dùng), `Tooltip`, icon `icon/house`, `icon/chevron-right`, `icon/ellipsis` (cỡ 16).

### Được dùng trong

`Header navigation` (Platform Web, trái thanh) · `Page header` (khi màn không có thanh trên, ít dùng).

### Token

Đối chiếu chung với Header navigation: `_work/header-navigation/check.json`.

### Kiểm máy

28/10: layout_audit 0 lỗi; a11y_audit 0 fail 0 review; auditDesignSystem 0,99 (khoảng cách 4 đều — có từ bản cũ, giữ).

## Mobile

Không có. Dưới 768 thanh trên dùng hàng "← {cấp trên}" thay đường dẫn (D8 A).

## Đối chiếu Astryx

| Astryx (`Breadcrumbs`) | Bản này | Vì sao |
|---|---|---|
| Chevron / Slash | Chỉ Chevron | Trang Application chọn Chevron |
| Cắt "…" sau 240 từng mục | Gom tầng giữa thành "…", cắt từng mục 160 / 240 | Đường dẫn sâu không đẩy ô tìm (D7 A) |
| Không có icon Nhà | Có Nhà | Trang Application chọn Home |

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
