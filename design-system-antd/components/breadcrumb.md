---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/select.md
---

# Breadcrumb — `nz-breadcrumb`

> **Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.**
> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/breadcrumb** (6 ví dụ, registry `breadcrumb1…6`, đọc mã 07/11);
> thuộc tính theo **API ng-zorro 22.x**. Breadcrumb chỉ dùng ở **web điều phối** (đầu trang chi tiết, trang cấp sâu);
> app tài xế không dùng (điều hướng bằng nút Quay lại trên thanh đầu).

## 0. Đề xuất Dùng / Không dùng

| Mã | Ví dụ | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| web-01 | Chữ + chevron, mục cuối là trang hiện tại | `nz-breadcrumb` + `nzSeparator` (chevron) | **Dùng** | Đầu trang chi tiết: "Điều phối › Lệnh vận tải › LV-0912" |
| web-02 | Rút gọn "…" mở menu các cấp giữa | `nz-breadcrumb-item` + `nz-dropdown` | **Dùng** | Đường dẫn ≥ 4 cấp (Khách hàng › công ty › hợp đồng › phụ lục › bảng giá) hoặc màn hẹp |
| web-03 | Cấp đầu là icon nhà + chevron | `nz-breadcrumb-item` + `nz-icon` | **Dùng** | Cấp "Tổng quan" thành icon để tiết kiệm chỗ khi cột chi tiết hẹp |
| web-04 | Icon nhà + dấu "/" | `nzSeparator="/"` (mặc định ng-zorro) | **Dùng** (phương án) | "/" là mặc định ng-zorro, dev không phải ghi đè. Chỉ chọn **một** dấu ngăn cho cả sản phẩm — xem ghi chú |
| web-05 | Icon nhà + dấu "·" | `nzSeparator="·"` | Không dùng | Dấu chấm giữa đọc như phân cách thông tin, không như đường dẫn; trùng web-04 |
| web-06 | Đường dẫn trong khung viền + bóng | — (tự dựng) | Không dùng | Trang trí; breadcrumb nằm sẵn trong đầu trang, thêm khung là viền thừa |

**Ghi chú dấu ngăn:** Figma dựng cả Chevron và Gạch chéo. Đề xuất **Chevron** làm mặc định (đúng kit shadcn, đồng bộ
chevron ở Select / Button); nếu user chọn "/" thì giữ mặc định ng-zorro và bỏ ghi đè `nzSeparator`.

Mẫu nghiệp vụ thêm: **ctx-01** Đầu trang chi tiết lệnh — breadcrumb trên tiêu đề "LV-0912 · Hà Nội → Hải Phòng", cách 8.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nz-breadcrumb-item` (nội dung) | `Nội dung` (variant) · `Nhãn` (text) | Chữ · Chỉ icon · Rút gọn | Mục Chữ bật được icon đầu: `Icon` (boolean) + `Icon · chọn` (instance swap, mặc định icon nhà) |
| Trạng thái link | `Trạng thái` (variant) | Thường · Rê chuột · Focus · Trang hiện tại | Rê chuột: chữ sang màu chính, không gạch chân, không nền. Focus: vòng focus quanh link |
| Mục cuối | `Trạng thái` = Trang hiện tại | — | Màu chữ chính, weight thường, không phải link (`aria-current="page"`). Chỉ có ở `Nội dung` = Chữ |
| `nzSeparator` | set `Breadcrumb dấu ngăn` › `Kiểu` | Chevron · Gạch chéo | Chevron 14 (đề xuất) · "/" (mặc định ng-zorro) |
| `nz-dropdown` trong mục | `Nội dung` = Rút gọn + component `Breadcrumb menu` | — | Ô "…" 20 × 20; menu mở dưới, cách 4, căn trái theo ô "…" |
| `nzAutoGenerate` · `nzRouteLabel` · `nzRouteFn` | — | `false` | Dev tự sinh từ route nếu muốn; Figma vẽ tay từng mục |

Set `Breadcrumb` (đường dẫn 3 cấp) = `Dấu ngăn` (Chevron · Gạch chéo) × `Đầu` (Chữ · Icon nhà) — đổi chữ từng mục trong
instance; thêm cấp = nhân bản 1 mục + 1 dấu ngăn.

## 2. Hình dáng

| Phần | Giá trị | Token |
|---|---|---|
| Chữ | 14/20 Geist Regular | `text/base/regular` |
| Màu mục (link) | chữ phụ #737373 (Dark #a1a1a1) | `color/text-secondary` |
| Màu rê chuột · trang hiện tại | chữ chính | `color/text` |
| Khoảng cách mục ↔ dấu ngăn | 10 web (`sm:gap-2.5`); 6 dưới 640px (`gap-1.5`) | `breadcrumb/gap` |
| Icon ↔ chữ trong mục | 6 | `breadcrumb/item-gap` → `spacing/6` |
| Dấu ngăn chevron | icon chevron-right 14, màu chữ phụ | `breadcrumb/separator-size` |
| Icon mục | 16 | `breadcrumb/icon-size` |
| Ô "…" | 20 × 20, icon ellipsis 16 | `breadcrumb/ellipsis-size` |
| Focus | vòng 3 ngoài link (-3), bo 2 | `focus/width` · `color/focus-ring` · `breadcrumb/link-radius` → `radius/xs` |
| Menu "…" | nền popover, viền, bo 8, padding 4, bóng `shadow/base`, rộng tối thiểu 128; mục = instance `Select mục` | `select/dropdown-*` · `breadcrumb/menu-min-width` → `select/dropdown-min-width` |

Không có nền, không viền, không bóng cho bản thân breadcrumb. Chữ dài: mục không cắt, dòng xuống hàng (`flex-wrap`);
đường dẫn quá 4 cấp thì gom cấp giữa vào "…" (web-02) thay vì để xuống hàng.

## 3. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| web-01 | Cơ bản | `nz-breadcrumb` | "Điều phối › Lệnh vận tải › LV-0912" |
| web-02 | Rút gọn có menu | `nz-breadcrumb-item` + `nz-dropdown` | "Khách hàng › … › Bảng giá tuyến"; menu: Công ty TNHH Minh Phát · Hợp đồng HĐ-2026-014 · Phụ lục 03 |
| web-03 | Icon Tổng quan | `nz-icon nzType="home"` | Cấp đầu = icon khi chỗ hẹp |
| web-04 | Dấu gạch chéo | `nzSeparator="/"` | Phương án dấu ngăn theo mặc định ng-zorro |
| ctx-01 | Đầu trang chi tiết lệnh | `nz-breadcrumb` + tiêu đề | Breadcrumb trên tiêu đề trang (`text/xl/medium`), cách 8 |

## 4. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Breadcrumb** (`71:6180`) — khuôn như Select (dựng tạm 07/11, chờ duyệt):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Breadcrumb` (tài liệu) | `71:9087` | Rộng 1536: đầu trang · Playground **Light** / **Dark** · `Ví dụ đã chốt` (5 thẻ) · `Mapping` (bảng thuộc tính + bảng token) |
| Section Components | `71:6199` | Set `Breadcrumb mục` `71:6250` = 10 biến thể (Chữ × 4 trạng thái, Chỉ icon × 3, Rút gọn × 3) · set `Breadcrumb dấu ngăn` `71:6266` (2) · `Breadcrumb menu` `71:6270` · set `Breadcrumb` `71:6406` (4) |
| Section Mẫu ghép | `71:7334` | `71:7335` web-01 · `71:7352` web-02 · `71:7394` web-03 · `71:7412` web-04 · `71:7428` ctx-01 |
| Section Icons | `71:6188` | `icon/house` `71:6192` · `icon/ellipsis` `71:6197` (lucide 16) |

## 5. Token

Xem `token-mapping.md` Mục 7.9 Breadcrumb. Biến mới (collection `size`): `breadcrumb/gap` 10 · `breadcrumb/item-gap` →
`spacing/6` · `breadcrumb/separator-size` 14 · `breadcrumb/icon-size` 16 · `breadcrumb/ellipsis-size` 20 ·
`breadcrumb/link-radius` → `radius/xs` · `breadcrumb/menu-min-width` → `select/dropdown-min-width`.

Cho dev (ng-zorro 22.x, `default.less` — tên biến cần kiểm): `@breadcrumb-link-color` = `@text-color-secondary`,
`@breadcrumb-last-item-color` = `@text-color`, `@breadcrumb-link-color-hover` = `@text-color` (AntD đổi màu primary),
`@breadcrumb-separator-margin` 0 10px (AntD 0 8px), `@breadcrumb-separator-color` = `@text-color-secondary`.
Chevron: `nzSeparator` = `TemplateRef` chứa `nz-icon nzType="right"` cỡ 14. Rút gọn: một `nz-breadcrumb-item` bọc
`nz-dropdown` + icon `ellipsis`, menu dùng chung style `nz-dropdown-menu` của Select.
