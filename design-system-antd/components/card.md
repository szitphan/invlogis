---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/button.md
  - design-system-antd/components/tag.md
  - design-system-antd/components/input.md
---

# Card — `nz-card`

> **Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.**
> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/card** (9 ví dụ, registry `card1…9`, đọc mã 07/11) và
> khung `Card` của shadcn v4 (`CardHeader` · `CardTitle` · `CardDescription` · `CardAction` · `CardContent` · `CardFooter`);
> thuộc tính theo **API ng-zorro 22.x**. Token đã chốt (token-mapping Mục 8.2 #7): **bo 14, padding 24, không bóng**.
> Card dùng cả **web điều phối** (thẻ KPI, thẻ lệnh trong bảng điều khiển, form ngắn) và **app tài xế** (thẻ nhận lệnh, thẻ thông tin).

## 0. Đề xuất Dùng / Không dùng

| Mã | Ví dụ | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| web-01 | Tiêu đề + mô tả + 1 nút toàn chiều rộng ở chân | `nz-card` + `nzTitle` + nút trong thân | **Dùng** | Thẻ việc cần làm một bước: "Chốt cước tháng 11/2026" — nút "Chốt cước kỳ" |
| web-02 | Thẻ form (đăng nhập) | `nz-card` + `nz-form` | **Dùng** | Form ngắn đứng riêng: thêm xe vào đội, đổi mật khẩu, đăng nhập |
| web-03 | Ảnh bìa trên đầu + nút đọc thêm | `nzCover` | Không dùng | Kiểu blog/trang giới thiệu; nghiệp vụ không có ảnh bìa (ảnh chứng từ xem ở Upload/Image) |
| web-04 | Nút "…" ở đầu card mở menu | `nzExtra` + `nz-dropdown` | **Dùng** | Thẻ lệnh vận tải, thẻ tài xế: menu Sửa · Huỷ lệnh · Xem lịch sử |
| web-05 | Tab trong card | `nzTabList` (thẻ có tab) | Không dùng (đợt này) | Chi tiết lệnh có tab nhưng dùng Tabs trên trang, không lồng trong card. Xét lại khi dựng Tabs |
| web-06 | Ghi chú cuộc họp + dãy avatar ở chân | `nz-card` + `nz-avatar-group` | Không dùng | Trùng cấu trúc web-01; dãy avatar chưa có nghiệp vụ (chưa dựng Avatar) |
| web-07 | Thông báo + 2 nút căn phải ở chân (cookie) | `nz-card` + nút cuối thân | **Dùng** | Thẻ xác nhận trên app tài xế: "Nhận lệnh LVT-…?" — Từ chối / Nhận lệnh |
| web-08 | Ô tìm + trạng thái rỗng trong card | `nz-card` + `nz-input` + `nz-empty` | **Dùng** | Danh sách trong card chưa có dữ liệu: "Tài xế trong đội" rỗng → Mời tài xế |
| web-09 | Hồ sơ có banner màu + avatar đè | `nzCover` + `nz-card-meta` | Không dùng | Trang trí kiểu mạng xã hội; thông tin tài xế làm ở inv-02 không banner |

Mẫu nghiệp vụ thêm (không có trong kit):

| Mã | Mẫu | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| inv-01 | Thẻ KPI chuyến hôm nay (cỡ small) — số lớn + Tag xu hướng + ghi chú | `nz-card nzSize="small"` + `nz-statistic` | Bảng điều khiển điều phối: chuyến hôm nay, giao đúng giờ, chuyến trễ |
| inv-02 | Thẻ thông tin tài xế — tag trạng thái, dòng nhãn/giá trị, chân Gọi + Giao lệnh | `nz-card` + `nzExtra` + `nz-descriptions` (hoặc dòng tự dựng) | Panel bên phải khi chọn tài xế; màn chi tiết tài xế trên app |

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzTitle` | `Tiêu đề` (text) · `Đầu card` (boolean) | chuỗi / TemplateRef | Tắt `Đầu card` = card không có đầu |
| — (mô tả dưới tiêu đề) | `Mô tả` (text) · `Hiện mô tả` (boolean) | | ng-zorro không có: viết trong template `nzTitle` (tiêu đề + dòng mô tả) |
| `nzExtra` | `Nút đầu card` (boolean) | TemplateRef | Mặc định nút Ghost `icon-sm` icon `ellipsis` mở menu; đổi icon trên instance lồng |
| thân (`ng-content`) | `Hiện nội dung` (boolean) · `Nội dung · chọn` (instance swap) | | Đổi khe sang component `Card khe/…` (Mục 3) |
| `nzActions` | `Chân card` (boolean) · `Chân · chọn` (instance swap) | | **Không dùng `nzActions`** (AntD chia ô đều có vạch dọc). Chân = `ng-template`/`div` cuối thân, nút căn phải cách 8 |
| `nzSize` | `Cỡ` (variant) | default · small | small: padding 16, khoảng giữa phần 16, tiêu đề 14 |
| `nzHoverable` | `Trạng thái` = Rê chuột · Focus | | Card bấm được: Rê chuột đổi viền `color/input-hover-border`, không đổ bóng; Focus vòng 3px |
| `nzLoading` | `Trạng thái` = Đang tải | | 3 thanh skeleton thay thân, đầu + chân giữ nguyên |
| `nzBordered` | — | `true` (mặc định) | Không dựng biến thể không viền: nền trang trắng, card không viền sẽ mất khung |
| `nzCover` · `nzType="inner"` · `nz-card-grid` · `nz-card-meta` | — | | Không dựng (web-03, web-05, web-09 Không dùng) |

## 2. Cấu trúc và kích thước

Khung: auto-layout dọc, rộng theo chỗ đặt (Figma 320), cao theo nội dung. Nền `color/component-bg`, viền 1px
`color/border-base`, bo `card/radius` (= `radius/xl` 14), **không bóng**.

| Phần | default | small | Ghi chú |
|---|---|---|---|
| Padding 4 cạnh | `card/padding` 24 | `card/padding-sm` 16 | shadcn `py-6` + `px-6` mỗi phần |
| Khoảng giữa đầu ↔ thân ↔ chân | `card/gap` 24 | `card/gap-sm` 16 | shadcn `gap-6` / `gap-4` |
| Tiêu đề | `text/lg/semibold` 16/24, `color/heading` | `text/base/semibold` 14/20 | |
| Mô tả | `text/base/regular` 14/20, `color/text-secondary` | như default | cách tiêu đề `card/header-gap` 6 |
| Nút đầu card | Button Ghost `icon-sm` 32 | như default | căn trên, cách khối chữ 8 |
| Chân | nút cách nhau `card/footer-gap` 8, căn phải | như default | Một nút chính thì kéo toàn chiều rộng (web-01) |

Đầu card **không có vạch kẻ dưới** (AntD có `border-bottom` + nền đầu riêng) — đầu dính liền thân như shadcn.

| Trạng thái | Viền | Khác |
|---|---|---|
| Thường | `color/border-base` | |
| Rê chuột | `color/input-hover-border` #a1a1a1 (Dark trắng 30%) | Chỉ card `nzHoverable`. Không bóng (AntD đổ bóng) — theo chốt 8.1 #3 "viền hover" |
| Focus | như Rê chuột + vòng `focus/width` 3 `color/focus-ring` ngoài khung 3px, bo `radius/2xl` 18 | Card bấm được bằng bàn phím |
| Đang tải | `color/border-base` | Thân thay bằng 3 thanh cao 16, bo `radius/sm`, nền `color/item-hover-bg`, cách 8 (rộng 100% · 100% · 60%) |

## 3. Set phụ — khe nội dung

Card chứa nội dung bất kỳ nên thân và chân là **khe** (instance swap). Mẫu ghép tạo component `Card khe/{mã} …` rồi
đổi vào `Nội dung · chọn` / `Chân · chọn`.

| Component | Nội dung |
|---|---|
| `Card khe/Nội dung` | Đoạn chữ mặc định (`text/base/regular`) |
| `Card khe/Chân 2 nút` | Button Outline "Huỷ" + Button Default "Lưu", căn phải, cách 8 |
| `Card khe/web-01 …` · `web-02 …` · `web-04 …` · `web-07 …` · `web-08 …` · `inv-01 …` · `inv-02 …` | Khe riêng của từng mẫu ghép (Mục 4) |

Dòng nhãn/giá trị (web-04, inv-02): nhãn `text/base/regular` `color/text-secondary` rộng 96, giá trị `text/base/medium`,
cách 8, các dòng cách 12.

## 4. Mẫu ghép

| Mã | Mẫu | Ghép từ |
|---|---|---|
| web-01 | Chốt cước tháng 11/2026 — mô tả + nút "Chốt cước kỳ" toàn chiều rộng | Card (không thân, không nút đầu) + Button Default |
| web-02 | Thêm xe vào đội — 2 trường Biển số xe, Tải trọng; chân Huỷ / Thêm xe | Card + 2 Input Nền xám default + Button |
| web-04 | Lệnh LVT-2611-018 — Cát Lái → KCN Sóng Thần; tag Đang chạy + Container 40ft; Tài xế · Xe · mooc · Giờ giao | Card + nút đầu "…" + Tag Tô nhạt Đang xử lý + Tag Viền |
| web-07 | Nhận lệnh LVT-2611-021? — Từ chối / Nhận lệnh | Card (không thân) + Button Outline + Default |
| web-08 | Tài xế trong đội — ô tìm có icon + trạng thái rỗng + "Mời tài xế" | Card + Input (Icon đầu) + icon `user-plus` trong khung 40 + Button |
| inv-01 | Chuyến hôm nay — 128 + ↑ 9,3% + "so với 117 chuyến hôm qua · 9 chuyến trễ" | Card small + `heading/2` + Tag xu hướng Tăng |
| inv-02 | Nguyễn Văn Hùng — Sẵn sàng · Bằng FC; Điện thoại, Xe đang lái, Hạn bằng lái, Số chuyến; chân Gọi / Giao lệnh | Card + nút đầu "…" + Tag + Button Outline (icon phone) + Default, 2 nút chia đều |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Card** (`71:5865`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Card` (tài liệu) | `71:13551` | Đầu trang · Playground Light / Dark (3 nhóm) · `Ví dụ đã chốt` (7 thẻ) · `Mapping` (10 thuộc tính + 10 token) |
| Section Components | `71:5871` | Set `Card` `71:6730` = Cỡ (2) × Trạng thái (4) = **8** · hàng instance bật/tắt phần · `Card khe/Nội dung` `71:6459` · `Card khe/Chân 2 nút` `71:6461` · 9 khe mẫu ghép |
| Section Mẫu ghép | `71:5872` | 7 component `Card mẫu ghép/{mã} …` |
| Section Icons | `71:5873` | `icon/ellipsis` `71:5884` · `icon/phone` `71:5887` · `icon/calendar` `71:5879` · `icon/route` `71:5898` · `icon/user` `71:5902` · `icon/refresh-cw` `71:5893` — lucide 16, nét 1.33, màu `color/text` |

Thuộc tính set `Card`: `Tiêu đề` · `Mô tả` (text) · `Đầu card` · `Hiện mô tả` · `Nút đầu card` · `Hiện nội dung` ·
`Chân card` (boolean) · `Nội dung · chọn` · `Chân · chọn` (instance swap).

Biến mới (size, alias): `card/padding-sm` → `spacing/md` 16 · `card/gap` → `spacing/lg` 24 · `card/gap-sm` → `spacing/md` 16 ·
`card/header-gap` → `spacing/6` 6 · `card/footer-gap` → `spacing/xs` 8. Dùng lại: `card/radius`, `card/padding`.

## 6. Ghi chú cho dev

- `@card-radius` 2 → 14; `@card-shadow` (hover) → không bóng, thay bằng CSS đổi `border-color` khi `.ant-card-hoverable:hover`.
- AntD đầu card cao `@card-head-height` 48, có `border-bottom` và padding riêng: bộ thử bỏ vạch, đầu là khối chữ thường
  trong thân (padding 24 chung), khoảng đầu ↔ thân 24. Dev ghi đè `.ant-card-head` (bỏ border, min-height, padding).
- Padding AntD `@card-padding-base` 24 — 1:1. Cỡ small AntD 12 → bộ thử 16 (`@card-padding-base-sm` — tên cần kiểm).
- Chân: không dùng `nzActions` (ô chia đều có vạch dọc, nền xám nhạt). Đặt nút trong `div` cuối thân, `justify-content: flex-end`, `gap: 8px`.
- Mô tả dưới tiêu đề: template `nzTitle` gồm 2 dòng (tiêu đề 16 SemiBold + mô tả 14 màu phụ, cách 6).
- Skeleton khi `nzLoading`: AntD tự vẽ `nz-skeleton` — chỉnh màu thanh về `color/item-hover-bg`, bo 6.
