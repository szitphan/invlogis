---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/tooltip.md
  - design-system-antd/components/tag.md
---

# Sidebar — `nz-sider` + `nz-menu` (inline)

> **Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.**
>
> Bộ thử AntD. shadcnuikit.com **không có** trang `components/sidebar` (404 ngày 07/11); chỉ có block
> `blocks/dashboard-ui/sidebar-layouts` (1 mẫu "Sidebar Layout 1", không có registry JSON công khai). Nguồn ví dụ dùng
> thay: **ui.shadcn.com** registry `r/styles/new-york-v4/sidebar-01…16.json` (16 block) + `sidebar.json` (lớp class gốc,
> đọc mã 07/11) + mô tả Sidebar Layout 1 của shadcnuikit. Thuộc tính theo **API ng-zorro 22.x**
> (`nz-layout` · `nz-sider` · `ul nz-menu nzMode="inline"` · `nz-submenu` · `nz-menu-group`).
> Một kiểu duy nhất: **nền sáng xám nhạt, mục bo 8, mục đang chọn nền nhạt + chữ Medium** (không viền xanh 3px của AntD).

## 1. Đề xuất Dùng / Không dùng

| Mã | Ví dụ | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| sb-01 | Nhóm theo mục có tiêu đề | `nz-menu-group nzTitle` | **Dùng** | Menu điều phối chia nhóm Vận hành · Tài chính · Hệ thống |
| sb-02 | Tiêu đề nhóm bấm thu/mở cả nhóm | `nz-menu-group` (ng-zorro không thu nhóm) | Không dùng | Menu chỉ 8 mục, thu cả nhóm thừa; ng-zorro không có sẵn |
| sb-03 | Mục con luôn mở | `nz-submenu nzOpen` cố định | Không dùng | Trùng sb-05; luôn mở làm dài menu |
| sb-04 | Sidebar nổi (bo, bóng, tách mép) | — | Không dùng | Trang trí, tốn 16px ngang trên màn điều phối dày dữ liệu |
| sb-05 | Mục con thu/mở | `nz-submenu` inline | **Dùng** | Cước & đối soát (Bảng cước, Đối soát), Báo cáo (Sản lượng, Doanh thu, Chi phí) |
| sb-06 | Mục con bung dạng dropdown | `nzMode="vertical"` | Không dùng | Khi thu gọn ng-zorro tự bung mục con dạng popup — không cần kiểu riêng khi mở rộng |
| sb-07 | Thu gọn còn icon + đầu workspace + chân người dùng | `nzCollapsible` · `nzInlineCollapsed` | **Dùng** | Điều phối viên cần rộng màn cho bảng/bản đồ; đầu chọn chi nhánh, chân tài khoản |
| sb-08 | Sidebar inset + menu phụ dưới (Hỗ trợ, Góp ý) | — | Không dùng | Inset là trang trí; Hỗ trợ đưa vào menu tài khoản ở chân |
| sb-09 | 2 sidebar lồng (thanh icon + danh sách hộp thư) | — | Không dùng | Kiểu ứng dụng mail; điều phối dùng bảng/bản đồ ở nội dung |
| sb-10 | Sidebar trong popover | `nz-popover` | Không dùng | Không có nhu cầu |
| sb-11 | Cây thư mục | `nz-tree` | Không dùng | Thuộc component Tree, không phải điều hướng |
| sb-12 | Sidebar có lịch | `nz-calendar` | Không dùng | Lịch xe/tài xế nằm ở màn Điều phối, không ở sidebar |
| sb-13 | Sidebar trong hộp thoại (Cài đặt) | `nz-modal` + `nz-menu` | Không dùng (để sau) | Cài đặt mở thành trang riêng; cân nhắc lại khi vẽ màn Cài đặt |
| sb-14 | Sidebar bên phải | `nz-sider` phải | Không dùng | Panel chi tiết bên phải là Drawer/khung chi tiết, không phải menu |
| sb-15 | Sidebar trái + phải | — | Không dùng | Như sb-14 |
| sb-16 | Header dính trên, sidebar dưới header | `nz-header` + `nz-sider` | Không dùng | Khung trang (layout) quyết ở màn; sidebar cao hết trang theo layout-1 |
| layout-1 | shadcnuikit Sidebar Layout 1 — sidebar full cao + header + nội dung | `nz-layout` > `nz-sider` + `nz-layout` | **Dùng** | Khung chuẩn web điều phối Invlogis |
| badge | Số đếm cạnh mục (`SidebarMenuBadge`) | nội dung tự thêm trong `nz-menu-item` | **Dùng** | Số lệnh chờ xử lý cạnh Lệnh vận tải, Điều phối — dùng Tag số đếm |

## 2. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nz-sider [nzWidth]` | — | 256 | `sidebar/width` (AntD 200) |
| `nzCollapsible` · `[(nzCollapsed)]` | `Trạng thái` (set Sidebar) | Mở rộng · Thu gọn | `nzCollapsedWidth` 48 (AntD 80) |
| `nzTrigger` | — | `null` | Bỏ thanh trigger đáy AntD; nút thu gọn = Button Ghost cỡ icon-sm, icon `panel-left`, đặt đầu header trang |
| `nzBreakpoint` | — | `lg` | Dưới 992px tự thu gọn; dưới 768px sidebar thành `nz-drawer` trái (chưa vẽ) |
| `nzTheme` | — | `light` | Không dùng sider tối của AntD; nền tối theo theme tối cả trang |
| `nz-menu nzMode` · `[nzInlineCollapsed]` | `Kiểu` (Sidebar mục) | Mở rộng · Thu gọn | `nzMode="inline"`; `nzInlineCollapsed` = `nzCollapsed` |
| `nz-menu-item [nzSelected]` · `[nzDisabled]` | `Trạng thái` (Sidebar mục) | Thường · Rê chuột · Đang chọn · Focus · Đã tắt | Đã tắt = mục không có quyền (vd Cài đặt với điều phối viên) |
| `nz-submenu [nzOpen]` | `Loại` (Sidebar mục) | Mục · Nhóm đóng · Nhóm mở · Mục con | Mũi tên phải, mở thì quay xuống; nhóm chứa mục đang chọn mở sẵn |
| `nz-menu-group nzTitle` | set `Sidebar nhóm` · `Tiêu đề` (text) | chuỗi | Thu gọn: ẩn tiêu đề, thay bằng đường chia 1px |
| `nz-icon` trong mục | `Icon` (instance swap) | 8 icon lucide 16 | Ẩn ở Mục con (shadcn không có icon cấp con) |
| Số đếm (tự thêm) | `Số đếm` (boolean) — instance Tag số đếm, đổi số qua thuộc tính lồng `Số` | số | Ẩn khi thu gọn |
| Tooltip khi thu gọn | — (instance Tooltip `67:3374`, Vị trí Phải) | tên mục | ng-zorro tự gắn tooltip cho mục cấp 1 khi `nzInlineCollapsed` |
| Đầu sidebar | set `Sidebar đầu` · `Tên workspace` · `Mô tả` | chuỗi | Bấm mở `nz-dropdown` chọn chi nhánh/workspace (dropdown chưa dựng) |
| Chân sidebar | set `Sidebar chân` · `Tên` · `Email` · `Viết tắt` | chuỗi | Bấm mở menu tài khoản: Hồ sơ · Đổi mật khẩu · Đăng xuất |

Menu nghiệp vụ web điều phối (thứ tự cố định): **Vận hành** — Tổng quan · Lệnh vận tải · Điều phối · Xe & tài xế ·
Khách hàng; **Tài chính** — Cước & đối soát (Bảng cước · Đối soát) · Báo cáo (Sản lượng · Doanh thu · Chi phí);
**Hệ thống** — Cài đặt.

## 3. Hình dáng

| Phần | Giá trị | Token |
|---|---|---|
| Nền sidebar | Light #fafafa · Dark #171717 | `color/sider-bg` |
| Viền phải | 1px | `color/sider-border` → `color/border-split` |
| Rộng | 256 mở rộng · 48 thu gọn | `sidebar/width` · `sidebar/collapsed-width` |
| Đầu / nhóm / chân | padding 8 | `sidebar/group-padding` |
| Mục | cao 32, padding 8, icon 16, cách 8, bo 8, chữ 14/20 | `sidebar/item-height` · `-padding` · `-icon-size` · `-gap` · `-radius` · `text/base/regular` |
| Khoảng giữa mục | 4 | `sidebar/menu-gap` |
| Rê chuột | nền #f5f5f5, chữ + icon `accent-foreground` | `color/sider-item-hover-bg` · `color/sider-item-active-text` |
| Đang chọn | nền #f5f5f5, chữ Medium | `color/sider-item-active-bg` · `text/base/medium` |
| Focus | vòng 3px ngoài mục (-3) | `focus/width` · `color/focus-ring` |
| Đã tắt | mờ 50% | `opacity/disabled` |
| Tiêu đề nhóm | cao 32, chữ 12/16 Medium, màu phụ | `text/sm/medium` · `color/sider-group-title` |
| Mục con | cao 28, khung lùi 14 hai bên, viền trái 1px, padding 10 ngang · 2 dọc | `sidebar/sub-item-height` · `sidebar/sub-indent` · `sidebar/sub-padding-x` |
| Đầu workspace / chân người dùng | cao 48, logo/ảnh 32 bo 10; tên 14 Medium + mô tả 12 | `sidebar/item-height-lg` · `sidebar/logo-size` · `sidebar/logo-radius` |
| Logo | nền màu chính, icon chữ trên nền chính | `color/sider-primary` · `color/sider-primary-foreground` |
| Ảnh đại diện chữ viết tắt | nền `color/border-base` (như ảnh 20 của Select) | `color/border-base` |
| Mục thu gọn | 32 × 32, chỉ icon | `sidebar/item-height` |

Lưu ý: nền Rê chuột và Đang chọn cùng giá trị (#f5f5f5, như shadcn `sidebar-accent`); phân biệt bằng chữ Medium. Trên
nền #fafafa độ tương phản nền thấp — nếu user thấy khó nhận mục đang chọn thì đổi `color/sider-item-active-bg`
sang `color/border-split` (#e5e5e5), chỉ đổi alias.

## 4. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| sb-01 | Nhóm có tiêu đề + số đếm | `nz-menu-group` + `nz-menu-item nzSelected` | Nhóm Vận hành, Lệnh vận tải đang chọn (12 lệnh chờ), Điều phối (5) |
| sb-05 | Nhóm con mở và đóng | `nz-submenu` | Báo cáo mở, Doanh thu đang chọn; Cước & đối soát đóng |
| sb-07 | Thu gọn chỉ icon + tooltip | `nzCollapsed` + `nzInlineCollapsed` | Rê vào Điều phối hiện Tooltip Phải "Điều phối" |
| sb-07 | Đầu chọn workspace | khối trên `nz-menu` + `nz-dropdown` | Invlogis · Delta Logistics · Điều phối |
| sb-07 | Chân người dùng | khối dưới `nz-menu` + `nz-dropdown` | Nguyễn Văn Long · long.nv@delta.vn |
| layout-1 | Sidebar đầy đủ | `nz-layout` > `nz-sider` | Menu nghiệp vụ đầy đủ 3 nhóm |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Sidebar** (`71:7446`) — khuôn như Select (dựng 07/11, chờ duyệt):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Sidebar` (tài liệu) | `73:546` | Rộng 1536: đầu trang · Playground **Light** `73:554` / **Dark** `73:573` (mode Dark gắn trên khung) · `Ví dụ đã chốt` `73:592` (6 thẻ) · `Mapping` `73:661` |
| Section Components | `71:11969` | Set `Sidebar mục` `71:11970` = Kiểu × Loại × Trạng thái = **25** (Mở rộng: Mục · Nhóm đóng · Nhóm mở · Mục con; Thu gọn: Mục) · `Sidebar nhóm` `71:15714` (2) · `Sidebar đầu` `71:15759` (4) · `Sidebar chân` `71:15784` (4) · `Sidebar` `71:19860` (2: Mở rộng 256 × 720 · Thu gọn 48 × 720) |
| Section Mẫu ghép | `72:674` | `72:302` sb-01 · `72:401` sb-05 · `72:451` sb-07 thu gọn · `72:529` sb-07 đầu · `72:545` sb-07 chân · `72:556` layout-1 |
| Section Icons | `71:7470` | 11 icon lucide 16, stroke `color/sider-text`: chart-column · chevron-right · chevrons-up-down · clipboard-list · layout-dashboard · panel-left · receipt · route · settings · truck · users |

Set `Sidebar` ghép hoàn toàn từ instance (đầu · nhóm · mục · chân); phần `Nội dung` giãn (fill) để chân luôn dính đáy.

## 6. Token

Xem `token-mapping.md` Mục 7.15 Sidebar. Biến mới — collection `color`: `color/sider-text` → `color/text` ·
`color/sider-group-title` → `color/text-secondary` · `color/sider-item-hover-bg` → `color/item-hover-bg` ·
`color/sider-item-active-bg` → `color/item-active-bg` · `color/sider-item-active-text` → `color/accent-foreground` ·
`color/sider-border` → `color/border-split` · `color/sider-primary` → `color/primary` ·
`color/sider-primary-foreground` → `color/primary-foreground` (dùng sẵn `color/sider-bg`). Collection `size`:
`sidebar/width` 256 · `sidebar/collapsed-width` 48 · `sidebar/item-height` → `height/sm` · `sidebar/item-height-lg` 48 ·
`sidebar/sub-item-height` 28 · `sidebar/item-padding` · `sidebar/item-gap` · `sidebar/group-padding` → `spacing/xs` ·
`sidebar/menu-gap` → `spacing/xss` · `sidebar/item-radius` → `radius/base` · `sidebar/sub-indent` 14 ·
`sidebar/sub-padding-x` 10 · `sidebar/icon-size` 16 · `sidebar/logo-size` → `height/sm` · `sidebar/logo-radius` → `radius/lg`.

Cho dev (ng-zorro 22.x, `default.less` — tên biến cần kiểm): `@layout-sider-background` · `@menu-bg` = `color/sider-bg`;
`@menu-item-color` = `color/text`; `@menu-highlight-color` = `color/accent-foreground`; `@menu-item-active-bg` =
`color/item-active-bg`; `@menu-item-group-title-color` = `color/text-secondary`; `@menu-item-height` ·
`@menu-inline-toplevel-item-height` 32; `@menu-collapsed-width` 48; `@menu-icon-size` 16; `@menu-icon-margin-right` 8;
`@menu-item-padding-horizontal` 8; `nzInlineIndent` 14. CSS riêng: bo 8 cho `.ant-menu-item` / `.ant-menu-submenu-title`,
bỏ viền phải 3px của `.ant-menu-item-selected::after`, nền hover, chữ Medium khi chọn, mục con cao 28 + viền trái
danh sách con, nhóm mục cách nhau 4 (margin AntD mặc định 4 trên/dưới cần đổi thành gap 4 giữa mục).
