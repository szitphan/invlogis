---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/input.md
---

# Checkbox — `nz-checkbox`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/checkbox** (13 ví dụ, registry `checkbox1…13`, đọc mã 06/11);
> thuộc tính theo **API ng-zorro**. Token theo `token-mapping.md` Mục 7.4: ô 16, bo 4, viền `color/border-base`, bóng
> `shadow/xs`; đã chọn nền màu chính + ✓ trắng; tắt mờ 50%. Web shadcnuikit vẽ ô chưa chọn nền xám không viền, bo 5 —
> bộ thử **theo token** (ô trắng có viền), như hình trên trang duyệt (user "duyệt hết" 06/11).
> Lựa chọn giữ/bỏ: trang duyệt component tab Checkbox (06/11): theo cột đề xuất, **giữ thêm** `card`, web-03, web-04,
> web-10; **bỏ** web-02 (đổi màu indigo), web-11 (thẻ tô xanh).

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `ngModel` | `Chọn` (variant) | Chưa chọn · Đã chọn | Đã chọn: nền `color/primary`, ✓ 14 `color/primary-foreground` |
| `nzIndeterminate` | `Chọn` = Một phần | gạch 8 × 2 | Ô "chọn tất cả" khi chỉ chọn một phần mục con (đầu bảng, web-12) |
| `nzDisabled` | `Trạng thái` = Đã tắt | mờ 50% | Mờ cả ô và nhãn |
| focus bàn phím (`:focus-visible`) | `Trạng thái` = Focus | vòng 3px | Viền ô chưa chọn đổi `color/ring` |
| form không hợp lệ (`nz-form-control`) | `Trạng thái` = Lỗi | viền đỏ + vòng đỏ 20% | ng-zorro **không có** `nzStatus` cho checkbox — dev viết CSS khi control invalid |
| nội dung `<label nz-checkbox>` | `Nhãn` (text) · `Có nhãn` (boolean) | | Tắt nhãn khi ô đứng một mình (đầu bảng, thẻ, danh sách) |
| nhãn phụ · mô tả (tự ghép) | `Nhãn phụ` + `Nhãn phụ · chữ` · `Mô tả` + `Mô tả · chữ` | boolean + text | Nhãn phụ 14 mờ trong ngoặc; mô tả 12 mờ dưới nhãn |
| `nz-checkbox-group` | — (mẫu ghép `group`, web-05, web-06) | dọc gap 8 (thưa 12) · ngang gap 16 | Không thành set riêng |
| `nz-checkbox-wrapper` + thẻ (tự ghép) | Set riêng `Checkbox thẻ` | Vị trí ô Trái · Phải × Chưa chọn · Đã chọn · Đã tắt | Cả thẻ bấm được; `Ảnh` (boolean) cho web-10 |
| — (tự dựng) | Set riêng `Checkbox tròn` | Chưa chọn · Đã chọn | Chỉ web-04 (danh sách việc cần làm) |

**Không dùng:** web-02 (đổi màu ô chọn theo chỗ — bộ thử chỉ một màu chính) · web-11 (thẻ tô xanh — xanh nằm ngoài
màu chính; dùng thẻ web-09 viền màu chính).

## 2. Ô chọn

| Phần | Giá trị | Token |
|---|---|---|
| Ô | 16 × 16, bo 4, viền 1px, bóng xs, nền trắng | `checkbox/size` · `radius/checkbox` · `color/border-base` · `shadow/xs` · `color/body-bg` |
| Dấu ✓ | lucide check 14, màu chữ trên nền chính | `checkbox/check-size` · `color/primary-foreground` |
| Gạch (Một phần) | 8 × 2, giữa ô | `checkbox/indeterminate-width` · `checkbox/indeterminate-height` |
| Ô ↔ nhãn | cách 8; ô lệch xuống 2 để giữa dòng chữ 20 | `checkbox/gap` = `spacing/xs` |
| Nhãn | 14/20 Geist Regular | `text/base/regular` · `color/text` |
| Nhãn phụ | 14/20, mờ, cách nhãn 4 | `color/text-secondary` |
| Mô tả | 12/16, mờ, ngay dưới nhãn | `text/sm/regular` · `color/text-secondary` |

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Thường | Chưa chọn: ô trắng viền xám · Đã chọn / Một phần: nền + viền màu chính | `color/border-base` · `color/primary` |
| Focus | Vòng 3px ngoài ô (cách 0), viền ô chưa chọn đậm hơn | `focus/width` · `color/focus-ring` · `color/ring` |
| Lỗi | Viền 1px đỏ + vòng đỏ 20% (cả khi đã chọn) | `color/error` · `color/focus-error-ring` |
| Đã tắt | Mờ 50% cả ô và nhãn | `opacity/disabled` |

Không vẽ trạng thái rê chuột: shadcn không đổi ô khi rê; AntD đổi viền sang màu chính — dev giữ mặc định shadcn (không đổi).

## 3. Thẻ chọn — `Checkbox thẻ`

| Phần | Giá trị | Token |
|---|---|---|
| Khung | rộng 240 (kéo dãn được), padding 12, bo 10, viền 1px, nền trắng | `checkbox/card-padding` · `radius/lg` · `color/border-base` · `color/body-bg` |
| Đã chọn | viền 2px màu chính (CSS: viền 1px + `box-shadow 0 0 0 1px`) | `color/primary` |
| Ô | instance `Checkbox` tắt nhãn, đặt Trái hoặc Phải | |
| Ảnh (web-10) | tròn 28, nền xám, chữ tắt 12 SemiBold | `color/bg-base` · `text/sm/semibold` |
| Nhãn phụ | 12 mờ (nhỏ hơn bản ô thường, theo web-09) | `text/sm/regular` |
| Đã tắt | mờ 50% | `opacity/disabled` |

**Checkbox tròn** (web-04): tròn 16, chưa chọn viền `color/border-base`; đã chọn nền `color/success`, ✓ 12 trắng
(`color/error-foreground` — biến trắng cố định cả 2 mode). Chỉ dùng trong danh sách việc cần làm; không đặt cạnh Radio.

## 4. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| state | Chọn / không chọn | `ngModel` | Loại hàng: Hàng nguy hiểm · Hàng lạnh |
| ind | Chọn một phần | `nzIndeterminate` | Ô "Chọn tất cả (3/10)" đầu bảng lệnh |
| disabled | Đã tắt | `nzDisabled` | Mục đã đối soát, không sửa được |
| desc | Kèm mô tả | nhãn + mô tả | Cài đặt: "Gửi SMS cho khách — Khi xe rời kho và khi giao xong" |
| group | Nhóm dọc | `nz-checkbox-group` | Lọc loại hàng: Container · Hàng rời · Hàng lạnh |
| card | Thẻ chọn ô trái | `nz-checkbox-wrapper` + thẻ | Dịch vụ cộng thêm: Bảo hiểm hàng 0,1% giá trị hàng (giữ 06/11) |
| web-01 | Đồng ý điều khoản (có link) | `nz-checkbox` + `a` | Đăng ký khách/đối tác: "Tôi đồng ý **điều khoản dịch vụ**" |
| web-03 | Danh sách kiểm tra — gạch khi xong | `nz-checkbox` + CSS | Kiểm tra xe trước chuyến: Lốp · Phanh · Giấy tờ (giữ 06/11; chữ gạch + mờ, vẫn đọc được) |
| web-04 | Ô tròn việc cần làm | tự dựng | Việc tài xế: kiểm dây chằng, chụp ảnh niêm phong (giữ 06/11) |
| web-05 | Nhóm ngang | `nz-checkbox-group` | Lọc nhanh trên thanh công cụ |
| web-06 | Nhóm dọc thưa (gap 12) | `nz-checkbox-group` | Bộ lọc bên trái danh sách, form nhiều lựa chọn |
| web-07 | Nhãn + nhãn phụ + mô tả | nhãn + mô tả | "Giao giờ hành chính (tuỳ chọn) — Chỉ giao 8:00–17:00, trừ Chủ nhật" |
| web-08 | Tick để mở ô nhập | `nz-checkbox` + `nz-input` hiện khi chọn | Tick "Có phụ phí" → ô số tiền thụt 24 dưới mô tả |
| web-09 | Thẻ — ô chọn bên phải | `nz-checkbox-wrapper` + thẻ | Bốc xếp tại kho (tuỳ chọn) |
| web-10 | Thẻ có ảnh đại diện | thẻ + `nz-avatar` | Chọn tài xế: ảnh/chữ tắt + tên + biển số, trạng thái (giữ 06/11) |
| web-12 | Cha – con, chọn một phần | `nzIndeterminate` + `nz-checkbox-group` | Phân quyền lệnh vận tải: Xem · Sửa · Xoá; chọn xe theo đội |
| web-13 | Danh sách có icon, ô bên phải | `nz-list` + `nz-checkbox` | Kênh nhận thông báo: App tài xế · SMS · Email; vạch ngăn giữa dòng |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Checkbox** (`67:3519`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Checkbox` (tài liệu) | `67:9527` | Đầu trang · Playground **Light** `67:9535` / **Dark** `67:9554` · `Ví dụ đã chốt` (17 thẻ) · `Mapping` (10 thuộc tính + 12 token) |
| Section Components | `67:3914` | Set `Checkbox` `67:3892` = Chọn (3) × Trạng thái (4) = **12** · Set `Checkbox thẻ` `67:6646` = Vị trí ô (2) × Trạng thái (3) = 6 · Set `Checkbox tròn` `67:6651` (2) |
| Section Mẫu ghép | `67:8780` | 17 component `Checkbox mẫu ghép/{mã} …` |
| Section Icons (trang này) | `67:3527` | `icon/smartphone` `67:3531` · `icon/message-square` `67:3534` · `icon/mail` `67:3538` (lucide 16) |
| Biến mới (collection size) | `VariableID:67:3520…67:3526` | `checkbox/size` 16 · `check-size` 14 · `gap` → `spacing/xs` · `indent` → `spacing/lg` · `card-padding` → `spacing/sm` · `indeterminate-width` 8 · `indeterminate-height` 2 |

Thuộc tính Checkbox: `Nhãn` · `Có nhãn` · `Nhãn phụ` + `Nhãn phụ · chữ` · `Mô tả` + `Mô tả · chữ`. Checkbox thẻ: `Nhãn` ·
`Nhãn phụ` + `· chữ` · `Mô tả` + `· chữ` · `Ảnh` + `Ảnh · chữ`. Mô tả dài: đặt instance rộng FILL, lớp `Chữ` và `Mô tả`
bên trong đổi sang FILL để xuống dòng (như mẫu `desc`, web-07, web-08).
