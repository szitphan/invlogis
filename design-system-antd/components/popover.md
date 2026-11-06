---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/tooltip.md
  - design-system-antd/components/button.md
  - design-system-antd/components/input.md
---

# Popover — `nz-popover` · `nz-popconfirm`

> **Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.**
> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/popover** (6 ví dụ, registry `popover1…6`, đọc mã 07/11);
> thuộc tính theo **API ng-zorro 22.x**. Ví dụ xác nhận (`pc-01`) theo `nz-popconfirm` — shadcnuikit không có.
> Đồng bộ: mũi tên như **Tooltip** (10 × 5, cách nút `tooltip/offset` 8); khung như **menu Select** (nền
> `color/popover-bg`, viền `color/border-base`, bo 8, `shadow/base`).
> Chữ ngắn, một dòng, chỉ để giải thích → `nz-tooltip`. Nội dung dài, nhiều bước, cần cuộn → Modal / Drawer.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nzPopoverPlacement` | `Vị trí` (variant) | Trên · Dưới · Trái · Phải | = `top` · `bottom` · `left` · `right`. 8 hướng lệch góc không vẽ; ng-zorro tự lật khi sát mép |
| `nzPopoverTitle` | `Tiêu đề` (variant Có/Không) + `Tiêu đề` (text) | chuỗi | Chữ 14/20 Medium. Mẫu Xác nhận và Hồ sơ không dùng tiêu đề |
| `nzPopoverContent` (`TemplateRef`) | `Nội dung` › `Loại` (instance lồng, đã expose) | Đoạn văn · Biểu mẫu · Xác nhận · Hồ sơ | Loại chỉ để vẽ; dev đặt TemplateRef. Đoạn văn có thuộc tính text `Mô tả` |
| — (`.ant-popover-arrow`) | `Mũi tên` (variant) | Có · Không | ng-zorro luôn có mũi tên. **Mặc định Có** (đồng bộ Tooltip). Không = kiểu shadcn, dev ẩn bằng CSS |
| `nzPopoverTrigger` | — | `click` | Form, xác nhận, mobile luôn click. `hover` chỉ cho thẻ thông tin xem nhanh trên web |
| `nzPopoverVisible` · `nzPopoverVisibleChange` | — | — | Đóng popover sau khi Lưu / Huỷ |
| `nzPopoverOverlayClassName` | — | `popover-288` · `popover-320` | Rộng cố định qua class (AntD chỉ có rộng tối thiểu) |
| `nz-popconfirm`: `nzPopconfirmTitle` · `nzOkText` · `nzCancelText` · `nzOkDanger` · `nzIcon` | `Nội dung` › `Loại` = Xác nhận | "Huỷ lệnh" / "Không" | Nút OK = Button Destructive khi huỷ / xoá; icon `circle-alert` màu `color/warning` |

Set phụ `Popover nội dung` (variant `Loại`): Đoạn văn (chữ mờ 14/20) · Biểu mẫu (nhãn 64 + Input sm nền xám, nút
sm phải) · Xác nhận (icon 16 + câu hỏi Medium + mô tả mờ, nút Outline + Destructive sm) · Hồ sơ (ảnh đại diện 32
chữ tắt + tên + SĐT, mô tả, 2 nút sm chia đôi). Control bên trong là **instance** của Input (`47:442`) và Button
(`15:2459`), không sửa component gốc.

## 2. Hình dáng

| Phần | Giá trị | Token |
|---|---|---|
| Nền · viền | Light #fff · Dark #171717, viền 1 trong | `color/popover-bg` · `color/border-base` |
| Rộng | 288 (shadcn `w-72`); mẫu Hồ sơ, Biểu mẫu vẫn 288 trong khung mẫu ghép 320 | `popover/width` |
| Padding | 16 bốn phía | `popover/padding` = `spacing/md` |
| Tiêu đề ↔ nội dung | 8, không vạch kẻ (AntD có vạch dưới tiêu đề — bỏ) | `popover/gap` = `spacing/xs` |
| Bo góc | 8 (như menu Select) | `popover/radius` = `radius/base` |
| Bóng | `shadow-md` | `shadow/base` |
| Mũi tên | tam giác 10 × 5, nền popover, 2 cạnh viền 1 `color/border-base`; chồng 1px lên viền khung để che vạch | `color/popover-bg` · `color/border-base` |
| Cách nút | 8 từ đầu mũi tên tới mép nút | `popover/offset` = `tooltip/offset` |
| Chữ | tiêu đề 14/20 Medium `color/text`; nội dung 14/20 Regular `color/text-secondary` | `text/base/medium` · `text/base/regular` |

Không có trạng thái riêng: popover hiện khi bấm nút, ẩn khi bấm ra ngoài / Esc. Trong mẫu ghép, nút kích hoạt
đặt ở trạng thái **Hover** (như Tooltip).

## 3. Ví dụ — đề xuất Dùng / Không dùng

| Mã | Ví dụ (shadcnuikit) | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| web-01 | Form kích thước (nhãn + ô nhập) | `nz-popover` + form | **Dùng** | Sửa nhanh tại chỗ trong bảng lệnh: cước, phụ phí, lý do — không mở trang chi tiết |
| web-02 | Danh sách thông báo (chuông + badge) | `nz-popover` + list | Không dùng | Trùng component Notification Center riêng (dropdown thông báo) — dựng khi có component đó |
| web-03 | Mẹo từng bước (onboarding tour) | — (ng-zorro không có Tour) | Không dùng | Trang trí; hướng dẫn người mới không thuộc phạm vi bộ thử |
| web-04 | Chia sẻ (icon mạng xã hội + ô link sao chép) | `nz-popover` | Không dùng | Không chia sẻ mạng xã hội; link theo dõi lệnh sao chép bằng Input có nút copy |
| web-05 | Góp ý (textarea + nút gửi) | `nz-popover` + textarea | Không dùng | Trùng web-01 (form trong popover); ghi chú dài dùng Modal / Drawer |
| web-06 | Thẻ hồ sơ (ảnh, tên, mô tả, 2 nút) | `nz-popover` | **Dùng** | Thẻ tài xế khi bấm tên tài xế trong bảng lệnh / bản đồ: SĐT, lệnh đang chạy, Gọi |
| pc-01 | Xác nhận thao tác (ng-zorro) | `nz-popconfirm` | **Dùng** | Xác nhận nhẹ ngay tại nút: "Huỷ lệnh LV-0912?" — thay Modal cho thao tác một bước |

## 4. Mẫu ghép

| Mã | Ví dụ | Ghép từ | Nội dung |
|---|---|---|---|
| web-01 | Sửa nhanh cước | Button Outline sm (icon pencil phải) + Popover Dưới, Tiêu đề Có, Loại Biểu mẫu | "Sửa cước LV-0912": Cước 4.500.000 ₫ · Phụ phí 350.000 ₫ · Lý do; Huỷ / Lưu |
| pc-01 | Xác nhận huỷ lệnh | Popover Trên, Tiêu đề Không, Loại Xác nhận + Button Outline sm (icon trash-2) | "Huỷ lệnh LV-0912?" — Không / Huỷ lệnh (Destructive) |
| web-06 | Thông tin tài xế | Button Link sm + Popover Dưới, Tiêu đề Không, Loại Hồ sơ | Nguyễn Văn An · 0912 345 678 · Bằng FC · đang chạy LV-0912; Xem hồ sơ / Gọi |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Popover** (`71:6792`) — khuôn như Select (dựng 07/11, chờ duyệt):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Popover` (tài liệu) | `71:11973` | Rộng 1536: đầu trang · Playground **Light** / **Dark** (mode Dark gắn trên khung) · `Ví dụ đã chốt` (3 thẻ) · `Mapping` |
| Section Components | `71:6798` | Set `Popover` `71:7889` = Vị trí (4) × Tiêu đề (2) × Mũi tên (2) = **16**, cột = Vị trí, hàng = Mũi tên › Tiêu đề · set phụ `Popover nội dung` `71:7674` (4) |
| Section Mẫu ghép | `71:6799` | `71:11276` web-01 · `71:11362` pc-01 · `71:11406` web-06 |
| Section Icons | `71:6800` | `icon/circle-alert` `71:6805` · `icon/phone` `71:6808` · `icon/pencil` `71:6812` |

Cấu trúc biến thể: khung auto-layout (dọc với Trên/Dưới, ngang với Trái/Phải), khoảng −1, gồm `Bubble` + `Mũi tên`
(frame 10 × 6 / 6 × 10 có 2 vector: `Nền` và `Viền`). Biến thể có mũi tên ở đầu dùng "first on top" để mũi tên đè
viền khung.

## 6. Token

Biến mới (collection `size`): `popover/width` 288 · `popover/padding` → `spacing/md` · `popover/gap` → `spacing/xs` ·
`popover/radius` → `radius/base` · `popover/offset` → `tooltip/offset`. Màu dùng lại, không thêm biến màu.

Cho dev (ng-zorro 22.x, `default.less` — tên biến cần kiểm): `@popover-bg` = `@component-background`;
`@popover-min-width` giữ, rộng đặt qua class; `@popover-padding-horizontal` 16 và padding dọc nội dung 16 (AntD 12)
ghi đè CSS `.ant-popover-inner-content`; tiêu đề bỏ `border-bottom`, `min-height` 32 → auto; `.ant-popover-inner`
thêm `border: 1px solid` `@border-color-base`, `border-radius` 8, `box-shadow` = `@box-shadow-base`;
`@popover-distance` 8; mũi tên `@popover-arrow-width` theo 10 × 5 và thêm viền. Nền tối: ghi đè thêm trong theme tối.
