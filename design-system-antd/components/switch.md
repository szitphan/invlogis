---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/checkbox.md
---

# Switch — `nz-switch`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/switch** (10 ví dụ, registry `switch1…10`); thuộc tính theo
> **API ng-zorro 22.x**. Lựa chọn giữ/bỏ: trang claude.ai/artifact/3eRLKXBhZLRfpBS1rcJ6Bx tab Switch (user duyệt 06/11,
> theo cột đề xuất). Cỡ theo hình trên trang duyệt (user "duyệt hết" 07/11): **rãnh 32×18, nhỏ 24×14, nút tròn
> trắng**; bật = màu chính; đã tắt mờ 50%. Không dùng cỡ web 44×20 nút dài của shadcnuikit.
> Switch dùng cho tuỳ chọn **có hiệu lực ngay** (không cần bấm Lưu). Tuỳ chọn trong form có nút Lưu → dùng Checkbox.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `ngModel` | `Giá trị` (variant) | Bật · Tắt | Bật: rãnh màu chính, nút sang phải |
| `nzSize` | `Cỡ` (variant) | default · sm | 32×18 · 24×14. sm: bật/tắt từng dòng trong bảng, thẻ cài đặt (web-10) |
| `nzLoading` | `Trạng thái` = Đang lưu | | Bật/tắt có gọi máy chủ: mờ 60%, vòng xoay trong nút, không bấm được |
| `nzDisabled` | `Trạng thái` = Đã tắt | | Mờ 50% |
| (focus bàn phím) | `Trạng thái` = Focus | | Vòng 3px ngoài rãnh, như Input |
| `nzControl` | — | | Dev: tự đổi giá trị sau khi máy chủ trả lời (đi cùng Đang lưu) |
| `nz-switch` + `<label>` | Set `Switch dòng`: `Vị trí` (variant) · `Nhãn` · `Mô tả` (boolean) + `Mô tả · chữ` · `Công tắc` (instance lồng, đã expose) | Trái · Phải | Bấm vào nhãn cũng bật/tắt |

**Không dùng:** `text` (`nzCheckedChildren`/`nzUnCheckedChildren` — chữ trong nút khó đọc, khó dịch; dùng nhãn cạnh như
web-05) · web-02 (đổi màu — một màu chính cho mọi control) · web-03 (vuông, lẫn với Checkbox) · web-04 (rãnh mảnh
Material) · web-06 (icon tối/sáng — chưa làm theme tối cho app vận hành) · web-07, web-08 (thực chất là thanh chuyển 2
lựa chọn, đã bỏ 06/11) · web-09 (chữ OFF/ON trong nút).

## 2. Công tắc

| Phần | Giá trị | Token |
|---|---|---|
| Rãnh default | 32 × 18, bo tròn, bóng `shadow/xs` | `switch/width` · `switch/height` · `switch/radius` = `radius/full` |
| Rãnh sm | 24 × 14 | `switch/width-sm` · `switch/height-sm` |
| Nút tròn | 14 (sm 10), cách mép rãnh 2, bóng 0 1 2 đen 20% | `switch/handle-size` · `switch/handle-size-sm` · `switch/padding` = `spacing/2` |
| Rãnh Tắt | xám nhạt (Dark: trắng 10%) | `switch/track-bg` → `color/border-base` |
| Rãnh Bật | màu chính | `switch/track-checked-bg` → `color/primary` |
| Nút Tắt | trắng (Dark: sáng) | `switch/handle-bg` → Light `color/body-bg` · Dark `color/text` |
| Nút Bật | trắng (Dark: tối, nằm trên rãnh sáng) | `switch/handle-checked-bg` → Light `color/body-bg` · Dark `color/primary-foreground` |

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Thường | như trên | |
| Focus | Vòng 3px ngoài rãnh (lệch -3, rộng +6) | `focus/width` · `color/focus-ring` |
| Đang lưu | Cả công tắc mờ 60% + vòng xoay 10 (sm 8) trong nút, màu `color/text-secondary` | `switch/loading-opacity` · `switch/spinner-size` · `switch/spinner-size-sm` |
| Đã tắt | Mờ 50% | `opacity/disabled` |

Chuyển động: nút trượt 0,2 s ease-out (Figma prototype: bấm Thường/Focus → đổi sang biến thể ngược giá trị, Smart animate).

## 3. Switch dòng (nhãn + mô tả)

| Vị trí | Bố cục | Dùng cho |
|---|---|---|
| Trái | Công tắc trước, cách chữ 8 (`spacing/xs`); nhãn 14 Regular | Một tuỳ chọn đứng riêng (web-01), trạng thái tài xế (web-05) |
| Phải | Chữ trước (giãn hết chiều ngang), công tắc bên phải, cách 12 (`spacing/sm`); nhãn 14 Medium | Trang cài đặt (label), thẻ cài đặt (web-10) |

Công tắc nằm trong ô cao 20 (`line-height/base`) để thẳng hàng dòng nhãn đầu tiên. Mô tả: chữ 12
`color/text-secondary`, dưới nhãn cách 2. Nhãn phụ trong ngoặc (web-10) là đoạn chữ 12 mờ trong cùng lớp `Nhãn`.

## 4. Mẫu ghép

| Mã | Ví dụ | ng-zorro | Dùng ở Invlogis |
|---|---|---|---|
| label | Nhãn + mô tả, công tắc phải | `nz-switch` + label tự ghép | Trang cài đặt: "Tự giao lệnh — Gán xe gần nhất khi có đơn" |
| web-01 | Công tắc + nhãn bên phải | `nz-switch` + label | "Nhận thông báo đơn mới" |
| web-05 | Nhãn đổi theo trạng thái | `nz-switch` + nhãn động | App tài xế: "Sẵn sàng nhận lệnh" (Bật) / "Đang nghỉ" (Tắt) — nhãn Medium, chữ đổi theo giá trị |
| web-10 | Thẻ cài đặt, công tắc nhỏ bên phải | `nz-switch nzSize="small"` + thẻ | Thông báo tự động: "Tự gửi SMS (cho khách) — Tự gửi SMS khi giao xong" |

Thẻ web-10: viền 1px `color/border-base`, bo `radius/lg` 10, padding 12 (`spacing/sm`), nền `color/body-bg`, các thẻ cách 8.

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Switch** (`67:3165`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Switch` (tài liệu) | `67:4982` | Đầu trang · Playground **Light** / **Dark** (Giá trị × Cỡ, 4 trạng thái × Bật/Tắt, Switch dòng) · `Ví dụ đã chốt` (4 thẻ) · `Mapping` (8 thuộc tính + 12 token) |
| Section Components | `67:3210` | Set `Switch` `67:3211` = Giá trị (2) × Cỡ (2) × Trạng thái (4) = **16**, ma trận cột Trạng thái, hàng Giá trị → Cỡ · Set `Switch dòng` `67:3505` (Vị trí Trái · Phải) |
| Section Mẫu ghép | `67:3639` | `Switch mẫu ghép/label …` `67:3640` · `web-01 …` `67:3648` · `web-05 …` `67:3656` · `web-10 …` `67:3672` |
| Biến mới — color | `switch/track-bg` · `track-checked-bg` · `handle-bg` · `handle-checked-bg` | `VariableID:67:3150…67:3153` (alias, Light/Dark) |
| Biến mới — size | `switch/width` · `height` · `width-sm` · `height-sm` · `handle-size` · `handle-size-sm` · `padding` · `radius` · `loading-opacity` · `spinner-size` · `spinner-size-sm` | `VariableID:67:3154…67:3164` |

Vòng xoay dùng icon `loader-circle` (`14:24`, trang Button). Bóng nút (0 1 2 đen 20%) là hiệu ứng trần — chưa có
effect style tương ứng (`shadow/xs` chỉ 5%).
