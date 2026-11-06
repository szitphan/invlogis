---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/button.md
  - design-system-antd/components/tooltip.md
  - design-system-antd/components/input.md
---

# Kbd — thẻ `<kbd>` + CSS riêng (ng-zorro không có)

> Dựng tạm theo đề xuất 07/11 — chưa qua trang chọn biến thể, user duyệt sau.
> Nguồn ví dụ: `shadcnuikit.com/components/kbd` trả 404 (trang và registry `kbd1.json`) nên dùng
> **ui.shadcn.com/docs/components/kbd** (mã nguồn thành phần + 5 ví dụ: Group, Button, Tooltip, Input Group, RTL).
> ng-zorro 22.x không có component Kbd: dùng thẻ HTML `<kbd class="inv-kbd">` và `<kbd class="inv-kbd-group">` bọc nhiều phím,
> CSS lấy từ token `kbd/*` (Mục 3). Không có thuộc tính Angular để map.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| — (thẻ `<kbd>`) | `Nền` (variant) | Sáng · Tối | Tối khi nằm trong Tooltip hoặc nút đậm |
| — | `Loại` (variant) | Chữ · Ký hiệu | Chữ ôm nội dung (Ctrl, Enter); Ký hiệu ô vuông 20 (⌘ ⇧ ⌥ ↵ ← →) |
| nội dung thẻ | `Phím` (text, mặc định Ctrl) · `Ký hiệu` (text, mặc định ⌘) | 2 lớp chữ riêng vì mặc định mỗi loại khác nhau | |
| `<kbd class="inv-kbd-group">` | set `Kbd group`: `Nền` · `Số phím` | Sáng · Tối × 2 phím · 3 phím | Gồm instance Kbd, cách nhau `kbd/gap` 4 |

Không có trạng thái (hover, focus, disabled): Kbd chỉ hiển thị, không bấm được, không nhận focus.

## 2. Kiểu dáng

| Phần | Giá trị | Token |
|---|---|---|
| Khung | cao 20, rộng tối thiểu 20, padding ngang 4, bo 6 | `kbd/height` · `kbd/min-width` · `kbd/padding-x` · `kbd/radius` |
| Nền sáng | xám nhạt, không viền | `kbd/bg` = `color/input-bg` |
| Chữ sáng | Geist Medium 12/16 | `kbd/fg` = `color/text-secondary` · `text/sm/medium` |
| Nền tối | `color/primary-foreground` 20% | `kbd/on-dark-bg` |
| Chữ tối | `color/primary-foreground` | `kbd/on-dark-fg` |
| Tổ hợp | cách 4 | `kbd/gap` |

Kiểu dáng đồng bộ trang Button: phím tắt trong nút cũ là chữ trần `⌘P` Geist Medium 12 `color/text-secondary` (mẫu web-07); Kbd thêm nền xám để thành "phím".
Kbd trên nền xám của Input (`color/input-bg`) phải đổi nền sang `color/body-bg` (mẫu kbd-03), nếu không hộp chìm vào ô.

## 3. Token (đề xuất — chưa ghi vào token-mapping)

Đã tạo trong file Figma: `kbd/height` 20 · `kbd/min-width` 20 · `kbd/padding-x` 4 · `kbd/gap` 4 · `kbd/radius` (alias `radius/sm`) ·
`kbd/bg` · `kbd/fg` · `kbd/on-dark-bg` · `kbd/on-dark-fg`.
`kbd/on-dark-bg` ghi thẳng màu có alpha 20% (Light #fafafa, Dark #171717) vì opacity của paint không đi theo instance.
Mục 7.11 đề xuất ở phần báo cáo (main thread ghi vào token-mapping.md).

## 4. Ví dụ — đề xuất Dùng / Không dùng

| Mã | Ví dụ | ng-zorro | Đề xuất | Lý do / dùng ở Invlogis |
|---|---|---|---|---|
| kbd-01 | Phím chữ và ký hiệu (Ctrl, Esc, ⌘, ⇧, ↵) | thẻ `<kbd>` | Dùng | Khối cơ bản; hiển thị Ctrl trên Windows, ⌘ trên Mac theo hệ điều hành |
| kbd-02 | Tổ hợp phím (KbdGroup) | `<kbd>` lồng nhau | Dùng | Bảng phím tắt cho điều phối viên: Ctrl K tìm lệnh, Ctrl Shift E xuất Excel |
| kbd-03 | Trong ô tìm (Input Group) | `nz-input-group` + `<kbd>` | Dùng | Ô tìm toàn cục "Tìm lệnh, xe, khách hàng…" gợi ý Ctrl K |
| kbd-04 | Trong tooltip | `nz-tooltip` + `<kbd>` | Dùng | Nút icon có phím tắt: "Tìm kiếm  Ctrl K" (Nền Tối). Tooltip hiện chưa có slot, đề xuất thêm |
| kbd-05 | Trong menu (dòng phím tắt bên phải) | `nz-dropdown` + `<kbd>` | Dùng | Menu thao tác lệnh vận tải: Tạo, Sao chép, In, Xuất |
| kbd-06 | Trong nút đậm (Nền Tối) | `nz-button` + `<kbd>` | Dùng | "Lưu lệnh ⌘↵"; thay slot chữ trần ở Button khi cần nền |
| kbd-07 | Trong nút viền "In ⌘P" (Button của kit) | `nz-button` + `<kbd>` | Không dùng | Trùng web-07 đã có ở trang Button; người dùng vận tải ít dùng phím tắt, để sau |
| kbd-08 | RTL | — | Không dùng | Sản phẩm chỉ tiếng Việt, không có ngôn ngữ phải-sang-trái |
| kbd-09 | Kbd trang trí trong tiêu đề, badge | — | Không dùng | Không phục vụ nghiệp vụ; nhầm với phím tắt thật |

## 5. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Kbd** (`71:6414`) — dựng 07/11, chờ duyệt:

| Khối | Node | Nội dung |
|---|---|---|
| Section Components | `71:6424` | set `Kbd` `71:6434` (4 biến thể: Nền × Loại) · set `Kbd group` `71:6843` (4: Nền × Số phím) |
| Section Mẫu ghép | `71:8965` | kbd-01 `71:8966` · kbd-02 `71:8989` · kbd-03 `71:9013` · kbd-04 `71:9030` · kbd-05 `71:9044` · kbd-06 `71:9075` |
| Khung tài liệu | `71:17001` | Playground Light `71:17009` + Dark `71:17028` · Ví dụ đã chốt · Mapping |

Mẫu kbd-03 dùng instance Input (Nền xám, default, Chờ nhập) và đặt Kbd group đè lên bên phải (Input chưa có slot phím tắt).
Mẫu kbd-04 vẽ lại bubble tooltip (cùng token với Tooltip) vì Tooltip chưa có chỗ gắn Kbd; nút icon bên dưới là instance Button.
Mẫu kbd-06 hoán đổi `Icon phải · chọn` của Button sang Kbd Nền Tối · Ký hiệu.
