---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/button.md
---

# Tooltip — `nz-tooltip`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/tooltip** (8 ví dụ, registry `tooltip1…8`, đọc mã 06/11);
> thuộc tính theo **API ng-zorro 22.x**. Lựa chọn giữ/bỏ: trang claude.ai/artifact/3eRLKXBhZLRfpBS1rcJ6Bx tab Tooltip —
> theo cột đề xuất (user không bấm khác). Một kiểu duy nhất: **nền màu chính, có mũi tên**, chữ 12/16.
> Nội dung dài, có tiêu đề, có ảnh hoặc có nút → `nz-popover` (component khác, chưa dựng).

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzTooltipTitle` (chuỗi) | `Nhãn` (text) | chuỗi | `Nội dung` = Một dòng · chữ 12/16, không xuống dòng |
| `nzTooltipTitle` (`TemplateRef`) | `Nội dung` (variant) | Một dòng · Chỉ số | Chỉ số = danh sách tên – giá trị, rộng 180 (web-03) |
| `nzTooltipPlacement` | `Vị trí` (variant) | Trên · Dưới · Trái · Phải | = `top` · `bottom` · `left` · `right`. 8 hướng lệch góc (`topLeft`…) không vẽ, dev vẫn dùng được; ng-zorro tự lật khi sát mép |
| `nzTooltipTrigger` · `nzTooltipMouseEnterDelay` | — | `hover` · 0,15 s | Giữ mặc định ng-zorro. Nút chỉ icon trên mobile: tooltip không hiện — nút phải tự rõ nghĩa hoặc có nhãn |
| `nzTooltipArrowPointAtCenter` | — | `false` | Mũi tên giữa cạnh khi dùng 4 hướng chính |
| `nzTooltipColor` | — | **không dùng** | Một kiểu nền tối cho thống nhất |

Set phụ `Tooltip chỉ số · dòng`: thuộc tính `Tên` (text, chữ mờ 60%) · `Giá trị` (text, Medium). Mẫu Chỉ số gồm 4 dòng
instance — đổi chữ từng dòng trong instance, ẩn dòng thừa.

**Không dùng:** `corner` (8 hướng lệch góc — chỉ không vẽ) · `noarrow` / web-07 (không mũi tên) · `color` / web-08
(nền sáng, màu tuỳ chỉnh — thông tin quan trọng dùng Popover/Alert) · web-02 (tiêu đề + đoạn mô tả → `nz-popover`) ·
web-06 (ảnh xem trước — ảnh chứng từ, POD mở bằng Popover hoặc Modal xem ảnh).

## 2. Hình dáng

| Phần | Giá trị | Token |
|---|---|---|
| Nền | Màu chính (Light #171717 · Dark #e5e5e5 — tooltip đảo màu theo nền) | `color/primary` |
| Chữ | 12/16 Geist Regular, màu chữ trên nền chính | `text/sm/regular` · `color/primary-foreground` |
| Padding | 6 trên dưới · 12 hai bên | `tooltip/padding-y` · `tooltip/padding-x` |
| Bo góc | 8 | `tooltip/radius` = `radius/base` |
| Mũi tên | tam giác 10 × 5 cùng màu nền, giữa cạnh hướng về nút (kit: hình vuông 8 xoay 45°, nhô ≈ 5) | `color/primary` |
| Cách nút | 8 từ đầu mũi tên tới mép nút | `tooltip/offset` = `spacing/xs` |
| Chỉ số | rộng 180, padding 12, các dòng cách 8; tên 12 mờ 60%, giá trị 12 Medium | `tooltip/rich-width` · `tooltip/rich-padding` · `tooltip/rich-gap` |
| Bóng | không | — |

Không có trạng thái riêng: tooltip hiện khi rê / focus vào nút, ẩn khi rời. Trên Figma, nút trong mẫu ghép đặt ở
trạng thái **Hover** để đọc đúng ngữ cảnh.

## 3. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| web-01 | Tooltip cơ bản | `nz-tooltip nzTooltipTitle` | **Bắt buộc với mọi nút chỉ icon** (Button web-26): "Thêm lệnh vận tải", "Tải phiếu giao" |
| web-03 | Danh sách chỉ số | `nzTooltipTitle` = `TemplateRef` | Rê vào xe trên bản đồ / dòng lệnh: Trạng thái · Tài xế · Giờ đến dự kiến · Còn lại — xem nhanh không mở chi tiết |
| web-04 | 4 hướng | `nzTooltipPlacement` | Như `Vị trí`; ng-zorro tự lật khi sát mép |
| web-05 | Icon ⓘ cạnh nhãn | `nz-icon` + `nz-tooltip` | Cạnh nhãn ô để giải thích ("Cước tính theo km thực chạy") — thay nút ⓘ trong ô (Input web-07) |

## 4. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Tooltip** (`67:3293`) — khuôn như Select (dựng 07/11, chờ duyệt):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Tooltip` (tài liệu) | `67:3925` | Rộng 1536: đầu trang · Playground **Light** / **Dark** (mode Dark gắn trên khung) · `Ví dụ đã chốt` (4 thẻ = instance mẫu ghép) · `Mapping` (bảng thuộc tính + bảng token) |
| Section Components | `67:3294` | Set `Tooltip` `67:3374` = Vị trí (4) × Nội dung (2) = **8**, ma trận cột = Vị trí, hàng = Nội dung · component phụ `Tooltip chỉ số · dòng` `67:3295` |
| Section Mẫu ghép | `67:3539` | `67:3540` web-01 · `67:3552` web-03 · `67:3588` web-04 · `67:3625` web-05 — ghép từ instance Tooltip + instance Button (trang Button, không sửa) |

Cấu trúc biến thể: khung auto-layout (dọc với Trên/Dưới, ngang với Trái/Phải) gồm `Bubble` + `Mũi tên` (vector), nên
cỡ component = bubble + mũi tên; đặt tooltip cách nút `tooltip/offset` 8.

## 5. Token

Xem `token-mapping.md` Mục 7.8 Tooltip. Biến mới (collection `size`): `tooltip/radius` → `radius/base` ·
`tooltip/padding-x` → `spacing/sm` · `tooltip/padding-y` → `spacing/6` · `tooltip/offset` → `spacing/xs` ·
`tooltip/rich-width` 180 · `tooltip/rich-padding` → `spacing/sm` · `tooltip/rich-gap` → `spacing/xs`.

Cho dev (ng-zorro 22.x, `default.less` — tên biến cần kiểm): `@tooltip-bg` = `@primary-color`, `@tooltip-color` =
`@btn-primary-color`, `@tooltip-border-radius` 8, `@tooltip-distance` 8; padding 6 · 12 và chữ 12/16 ghi đè bằng CSS
`.ant-tooltip-inner` (AntD đặt cứng padding 6 · 8, `min-height` 32, chữ 14). Nền tối: ghi đè thêm trong theme tối.
