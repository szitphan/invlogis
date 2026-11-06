---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/select.md
---

# Tag — `nz-tag` (+ số đếm `nz-badge`)

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/badge** (17 ví dụ, registry `badge1…17`, đọc mã 06/11);
> thuộc tính theo **API ng-zorro 22.x**. shadcn gọi là Badge; ở ng-zorro nhãn là `nz-tag`, số đếm và chấm trạng thái
> là `nz-badge`. Lựa chọn giữ/bỏ: trang review components-r1 tab Tag (user duyệt hết theo đề xuất 06/11).
> Token đã chốt (token-mapping Mục 8.2 #7): **pill cao 20**, padding 8, chữ 12 Medium; Info xanh `#155dfc`.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzColor` | `Màu` (variant) | Mặc định · Thành công · Đang xử lý · Cảnh báo · Lỗi | `default` · `success` · `processing` · `warning` · `error` |
| `nzColor` + `nzBordered` | `Kiểu` (variant) | Tô nhạt · Viền chấm · Viền | Xem Mục 2 |
| `nz-badge nzStatus` + `nzText` | `Kiểu` = Viền chấm | chấm theo `Màu` | Dev: nz-tag viền + span chấm, hoặc nz-badge đặt trong khung viền |
| `nzMode="closeable"` · `(nzOnClose)` | `Nút đóng` (boolean) | | Icon x 12 mờ 60%, rê chuột 100% |
| `nz-icon` trong `nz-tag` | `Icon` (boolean) + `Icon đổi` (swap) | zap · snowflake · truck · arrow-up · arrow-down | Icon 12 mờ 60%, cách chữ 4 |
| `nzMode="checkable"` · `nzChecked` | Set riêng `Tag chọn` › `Trạng thái` | Chưa chọn · Rê chuột · Đã chọn · Focus · Đã tắt | |
| `nz-badge nzCount` (`nzStandalone`) | Set riêng `Tag số đếm` › `Kiểu` | Đứng riêng · Trên ảnh | |
| `nz-tag nzColor` + icon mũi tên | Set riêng `Tag xu hướng` › `Hướng` | Tăng · Giảm | Thẻ KPI |
| nội dung | `Nhãn` (Tag, Tag chọn) · `Số` (số đếm, xu hướng) | | 1 dòng, không xuống dòng |

**Không dùng:** Đặc màu chính / web-01 (đen đặc quá nổi cho nhãn) · 11 màu đặt sẵn (lẫn với màu trạng thái; cần nhãn
phân loại thì dùng 5 màu biểu đồ) · `nzBordered="false"` (đã có Tô nhạt Mặc định) · web-04 (nhãn không là link) ·
web-05 (trùng Button web-06) · web-06 (chọn chấm màu thay icon ✓) · web-09, web-10 (thẻ đóng dùng nền xám) · web-11
(để đến Select người dùng) · web-14…17 (kiểu landing page; báo cập nhật dùng Alert/Notification).

## 2. Kiểu × Màu

Khung chung: cao `tag/height` 20, bo `tag/radius` (= `radius/sm` 6, user chốt 07/11 — bỏ pill), padding ngang `tag/padding-x` 8, khoảng cách
`tag/gap` 4, chữ `text/sm/medium` 12/16.

| Kiểu | Nền | Viền | Chữ | Chấm |
|---|---|---|---|---|
| Tô nhạt | màu 10% (Dark 20%) | không | màu đậm | — |
| Viền chấm | `color/component-bg` | 1px `color/border-base` | `color/text` | 6, màu trạng thái |
| Viền (chỉ Mặc định) | `color/component-bg` | 1px `color/border-base` | `color/text` | — |

| Màu | Nền Tô nhạt | Chữ Tô nhạt | Chấm |
|---|---|---|---|
| Mặc định (= secondary) | `color/bg-base` #f5f5f5 | `color/text` | `color/text-secondary` |
| Thành công | `tag/success-bg` #389e0d 10% · Dark #49aa19 20% | `tag/success-fg` #389e0d · Dark #6abe39 | `color/success` |
| Đang xử lý | `tag/info-bg` #155dfc 10% · Dark #2b7fff 20% | `color/info` | `color/info` |
| Cảnh báo | `tag/warning-bg` #d48806 10% · Dark #d89614 20% | `tag/warning-fg` #d48806 · Dark #e8b339 | `color/warning` |
| Lỗi (= destructive) | `color/error-bg` | `color/error` | `color/error` |

Chữ Thành công / Cảnh báo dùng tông đậm (AntD green-7, gold-7) thay `color/success` / `color/warning`: màu gốc trên
nền 10% không đủ tương phản cho chữ 12.

**Chọn kiểu nào:** Tô nhạt cho trạng thái nổi bật (cột Trạng thái trong chi tiết lệnh, thẻ). Viền chấm cho bảng dày
nhiều dòng — đỡ loè. Một màn chỉ dùng một trong hai cho cùng một loại trạng thái.

## 3. Set phụ

| Set | Biến thể | Giá trị |
|---|---|---|
| `Tag chọn` | Chưa chọn · Rê chuột · Đã chọn · Focus · Đã tắt | Chưa chọn nền `color/component-bg` không viền · Rê chuột `color/item-hover-bg` · Đã chọn `color/primary` + chữ `color/primary-foreground` · Focus vòng `focus/width` 3 `color/focus-ring` cách 3 · Đã tắt `opacity/disabled` |
| `Tag số đếm` | Đứng riêng · Trên ảnh | Nền `color/primary`, chữ 12 SemiBold `color/primary-foreground`, padding 4. Đứng riêng cao 20, rộng tối thiểu `tag/count-min-width` 20. Trên ảnh cao/rộng tối thiểu `tag/count-sm-size` 18, viền 2 `color/body-bg`, đặt góc trên phải ảnh lệch −6 |
| `Tag xu hướng` | Tăng · Giảm | Tăng = nền/chữ Thành công + arrow-up 12 · Giảm = nền/chữ Lỗi + arrow-down 12; mũi tên không mờ |

## 4. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| status | Trạng thái lệnh vận tải: Đã giao · Đang chạy · Trễ hẹn · Huỷ · Nháp | `nzColor` | Trạng thái lệnh, xe, thanh toán |
| secondary | Nền xám không viền | `nz-tag` (default ghi đè) | Loại hàng, đội xe |
| outline | Viền nền trắng | `nzBordered` | Nhãn phụ trên nền xám: Hàng lạnh, Ghép chuyến |
| destructive | Đỏ nhạt | `nzColor="error"` | Quá hạn |
| closable | Có nút xoá | `nzMode="closeable"` | Bộ lọc đang áp, email nhận thông báo |
| checkable | Bấm để chọn | `nzMode="checkable"` | Lọc nhanh: Tất cả · Container · Hàng lạnh |
| web-02 | Icon + chữ | `nz-tag` + `nz-icon` | Hoả tốc, Hàng lạnh, Đang chạy (icon xe) |
| web-03 | Số đếm tròn 20 | `nz-badge nzCount nzStandalone` | "Chờ duyệt 6" trên tab, menu |
| web-07 | Viền + chấm — chờ | `nz-badge nzStatus` + `nzText` | Trạng thái trong bảng dày: Chờ xếp xe |
| web-08 | Viền + chấm — lỗi | `nz-badge nzStatus="error"` | Trễ hẹn, Lỗi đồng bộ |
| web-12 | Tăng / giảm (%) | `nz-tag nzColor` + mũi tên | Thẻ KPI: giao đúng giờ ↑ 9,3%, chi phí nhiên liệu ↓ 1,9% |
| web-13 | Số đếm trên ảnh đại diện | `nz-badge nzCount` bọc `nz-avatar` | Ảnh tài xế + số tin chưa đọc (chat điều phối) |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Tag** (`67:3225`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Tag` (tài liệu) | `67:7347` | Đầu trang · Playground Light / Dark (5 nhóm) · `Ví dụ đã chốt` (12 thẻ) · `Mapping` (9 thuộc tính + 14 token) |
| Section Components | `67:3509` | Set `Tag` `67:3490` = Tô nhạt (5) + Viền chấm (5) + Viền (1) = **11** · Set `Tag chọn` `67:6051` (5) · Set `Tag số đếm` `67:6062` (2) · Set `Tag xu hướng` `67:6074` (2) |
| Section Mẫu ghép | `67:7149` | 12 component `Tag mẫu ghép/{mã} …` |
| Section Icons | `67:3237` | `icon/zap` `67:3240` · `icon/snowflake` `67:3256` · `icon/truck` `67:3265` · `icon/arrow-up` `67:3271` · `icon/arrow-down` `67:3277` · `icon/x` `67:3283` — lucide 12, nét 1 |

Thuộc tính set `Tag`: `Nhãn` (text) · `Icon` (boolean) + `Icon đổi` (swap, gợi ý 5 icon trên) · `Nút đóng` (boolean).
Icon có 1 lớp `Hình` — màu nét đặt theo từng biến thể nên đổi icon vẫn giữ màu chữ.

Biến mới: màu (Light/Dark) `tag/success-fg` · `tag/success-bg` · `tag/info-bg` · `tag/warning-fg` · `tag/warning-bg`;
size `tag/padding-x` (→ `spacing/xs`) · `tag/gap` (→ `spacing/xss`) · `tag/icon-size` 12 · `tag/icon-opacity` 60 ·
`tag/dot-size` 6 · `tag/count-min-width` 20 · `tag/count-sm-size` 18.

## 6. Ghi chú cho dev

- AntD tag mặc định có viền 1px và padding 7: bộ thử bỏ viền ở Tô nhạt → padding 8. Kiểu Viền giữ viền, padding 8 − 1 = 7.
- Màu trạng thái AntD tô nền `-deprecated-bg` + viền `-deprecated-border` + chữ màu gốc. Bộ thử: nền 10%, không viền,
  chữ tông 7 — dev viết CSS riêng cho `.ant-tag-success|processing|warning|error` (tên biến Less cần kiểm).
- Số đếm AntD màu đỏ (`@badge-color`); bộ thử dùng màu chính đen (web-03, web-13).
- Chấm trạng thái: AntD `@badge-status-size` 6 — 1:1.
