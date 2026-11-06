---
type: design-system-component
status: draft
updated: 2026-11-07
links:
  - design-system-antd/foundations/foundations.md
  - design-system-antd/token-mapping.md
  - design-system-antd/components/button.md
---

# Input — `nz-input`

> Bộ thử AntD. Giao diện theo **shadcnuikit.com/components/input** (25 ví dụ, đọc registry `input1…25`);
> thuộc tính theo **API ng-zorro 22.x**. Mọi con số là token trong `token-mapping.md` Mục 7.2.
> Lựa chọn giữ/bỏ: trang claude.ai/artifact/3eRLKXBhZLRfpBS1rcJ6Bx tab Input — dựng theo cột đề xuất + 4 điểm chốt
> 06/11 tối; 07/11 user giữ thêm 6 mẫu web-07, 12, 18, 19, 24, 25 (Mục 5).
> **Bo góc chốt 07/11: theo kit shadcn** — ô `input/radius` = `radius/lg` 10, ô nhiều dòng `textarea/radius` = `radius/lg` 10,
> nút 8. Bỏ bo pill. Vòng focus bo 13 (= 10 + 3).
> Mẫu ghép duyệt 07/11 (claude.ai/artifact/A6qSRpB5F19i7iQtnfDXPW). **Cấu trúc theo kit shadcn Input Group** (user review 07/11):
> set gốc nhỏ + **khe** bật tắt; chi tiết bên trong (icon, chữ tiền tố/đơn vị, Kbd, nút, chọn, tag, nhãn trong ô, độ mạnh)
> là **component con** `Input / Addon`, `Input / Khối`. Bỏ trục `Type` 468 biến thể đã dựng thử trước đó.

## 1. Thuộc tính

| ng-zorro | Figma property | Giá trị dùng | Ghi chú |
|---|---|---|---|
| `nz-input-group` addon / `nzPrefix` / `nzSuffix` | Khe `Đầu 1` · `Đầu 2` · `Cuối 1` · `Cuối 2` (boolean) — mỗi khe là exposed instance `Input / Addon` | Mục 1.1 | Thay `Icon đầu/cuối`, `Đơn vị`, `Phần đầu` cũ |
| khối trên/dưới trong ô | Khe `Khối trên` · `Khối dưới` (boolean) — exposed instance `Input / Khối` | Nhãn · Đếm · Độ mạnh | Nhãn trong ô (web-25), độ mạnh (web-20) |
| `nzSize` | `Cỡ` (variant) | sm · default · lg | 32 · 36 · 40 |
| `nzBorderless` | `Kiểu` (variant) | Nền xám · Không nền | Không nền: sửa tại chỗ trong ô bảng |
| `nzStatus` + class `success` | `Trạng thái` (variant) | Chờ nhập · Đã nhập · Focus · Lỗi · Cảnh báo · Hợp lệ · Đã tắt | `success` không có trong ng-zorro → class riêng |
| `disabled` | `Trạng thái` = Đã tắt | true | Mờ `opacity/disabled` 50% |
| `placeholder` / `value` | `Placeholder` (text, hiện ở Chờ nhập) · `Chữ` (text, giá trị) | | Ở cấp 1 `Input`: chỉnh trong `Input / Body` lồng bên trong (exposed) |
| `nz-form-control nzExtra` / `nzErrorTip` | `Dòng gợi ý` (boolean) + `Dòng gợi ý · chữ` (text) | | Chữ 12 dưới ô, cách 6; trạng thái Lỗi chữ đỏ (web-03, web-12, web-21) |

### 1.1 Component con

| Component | Biến thể (`Loại`) | Thuộc tính | Dùng cho |
|---|---|---|---|
| `Input / Addon` | Icon · Chữ · Kbd · Spinner · Nút · Tooltip · Chọn · Tag · Chép · Đã chép | `Chữ` (text) · `Icon` (swap, cho Loại Icon) · `Icon nút` (swap, cho Loại Nút: xoá, mắt…) · Tag lồng exposed | Icon tìm, "https://", "VNĐ"/"km"/"24 kết quả"/"14/50", Ctrl K, nút xoá/mắt, ⓘ, "VN +84 ⌄"/"Mã lệnh ⌄", tag trong ô, chép → dấu tích (prototype bấm → Đã chép → 1,5 s về) |
| `Input / Khối` | Nhãn · Đếm · Độ mạnh | `Chữ` · `Chữ phải` (text) | Nhãn trong ô (Khối trên), "0/280 ký tự · 52% đã dùng", thanh 4 vạch (Khối dưới) |

Cách ghép các kiểu ô (thay trục Type cũ): **Search** = Đầu 1 Icon + Cuối Nút (xoá) · **Password** = Cuối Nút (`Icon nút` = eye) + Khối dưới Độ mạnh ·
**Copy** = Cuối Chép · **Số/đơn vị/đếm** = Cuối Chữ · **Tiền tố/mã quốc gia** = Đầu Chữ / Chọn · **Nhãn** = Đầu Tag · **Nhãn trong ô** = Khối trên Nhãn.
**Thẻ ngân hàng** và **Khoảng Từ–Đến** là nhiều ô Input thật → chỉ là ví dụ ghép trong tài liệu, không nằm trong set.

**Không dùng:** `nzAddOnBefore`/`nzAddOnAfter` dạng khối rời (thay bằng chữ trong ô) · nhãn nổi.
Hover: ô nền xám **không đổi khi rê chuột** (giống web) → không có trạng thái Hover.

## 2. Cỡ

| Cỡ | ng-zorro | Cao | Padding ngang | Chữ | Dùng khi |
|---|---|---|---|---|---|
| sm | `nzSize="small"` | `height/sm` 32 | `input/padding-x` 12 | 14 | Ô lọc trong bảng, cạnh nút sm |
| default | `nzSize="default"` | `input/height/base` 36 | 12 | 14 | Web điều phối |
| lg | `nzSize="large"` | `height/lg` 40 | 12 | 14 (mobile 16) | Form mobile tài xế, đăng nhập |

Chung: bo `input/radius` = `radius/lg` 10 · nền `color/input-bg` #f2f2f2 · không viền (`color/input-border` trong suốt) · không bóng ·
icon 16, cách chữ 8 · chữ Geist Regular, placeholder `color/input-placeholder`.

## 3. Trạng thái

| Trạng thái | Cách thể hiện | Token |
|---|---|---|
| Chờ nhập | Placeholder mờ | `color/input-placeholder` |
| Đã nhập | Chữ đậm màu | `color/text` |
| Focus | Vòng 3px ngoài ô | `focus/width` 3 · `color/focus-ring` (#a1a1a1 50%) |
| Lỗi | Viền 1px đỏ + vòng đỏ 3px 20% · dòng báo lỗi dưới ô | `color/error` · `focus/error-color` |
| Cảnh báo | Viền 1px vàng + vòng vàng 20% | `color/warning` |
| Hợp lệ | **Nền trắng, viền 1px xanh** (như web-05) | `color/body-bg` · `color/input-success-border` = `color/success` |
| Đã tắt | Mờ 50%, không gõ được | `opacity/disabled` |

Kiểu **Không nền**: nền trong suốt; Focus/Lỗi/Cảnh báo/Hợp lệ giữ viền + vòng như trên.

## 4. Nhiều dòng — `textarea nz-input`

Nền xám, không viền, **bo `textarea/radius` = `radius/lg` 10** (chốt 07/11), padding 12, cao tối thiểu 80, `nzAutosize`.
Trạng thái như Mục 3. Đếm ký tự (`nz-textarea-count`): số `n/max` góc dưới phải, chữ 12 `color/text-secondary`.

## 5. Ví dụ đã chốt — mẫu ghép theo 4 nhóm (duyệt 07/11)

Mẫu ghép không còn là component riêng. Thẻ trong khung `Ví dụ đã chốt` là instance set Input (+ Label khi có nhãn).

| Mã | Ví dụ | Đi đâu | Dùng ở Invlogis |
|---|---|---|---|
| web-01 | Ô cơ bản | Input | |
| web-02 | Có nhãn | Label + Input | Mọi form: nhãn trên ô, cách 6 |
| web-03 | Có dòng gợi ý | `Dòng gợi ý` | "Theo đăng ký xe" |
| web-06 | Icon tìm + số kết quả | Đầu Icon + Cuối Chữ "24 kết quả" + Cuối Nút | Tìm lệnh — "24 kết quả" |
| web-07 | Tiền tố chữ + ⓘ | Đầu Chữ "https://" + Cuối Tooltip | Link webhook đối tác |
| web-08 | Chữ đơn vị | Cuối Chữ "km" | km, tấn, khối, chuyến |
| web-09 | Ô tìm + chọn trường | Đầu Icon + Cuối Chọn "Mã lệnh" | Tìm theo Mã lệnh / Biển số / Tài xế |
| web-10 | Tiền | Cuối Chữ "VNĐ" | Cước, phí phát sinh |
| web-11 | Nút chép trong ô | Cuối Chép | Link theo dõi đơn, mã lệnh |
| web-12 | Đếm ký tự dưới ô | `Dòng gợi ý` "14/50 ký tự" | Ô hẹp không đủ chỗ đếm trong ô |
| web-13 | Mật khẩu ẩn/hiện | Cuối Nút (eye) | Đăng nhập |
| web-15 | Đếm ký tự trong ô | Cuối Chữ "14/50" | Mã tham chiếu khách |
| web-16 | Nút xoá nhanh | Đầu Icon + Cuối Nút (xoá) | Ô tìm, ô lọc |
| web-17 | Mã OTP 4 ô | → component **Input OTP** (đợt tới, `nz-input-otp`); thẻ giữ hình cũ | Tài xế đăng nhập SMS |
| web-18 | SĐT + mã quốc gia | Đầu Chọn "VN +84" | SĐT tài xế |
| web-19 | Thẻ 3 ô | Ví dụ 3 ô Input (Đầu Icon thẻ) | Thẻ thanh toán cước |
| web-20 | Mật khẩu + độ mạnh | Cuối Nút (eye) + Khối dưới Độ mạnh (danh sách điều kiện bỏ khỏi ví dụ) | Đặt/đổi mật khẩu |
| web-21 | Ô có mặt nạ | Input + `Dòng gợi ý` | Biển số, số container |
| web-23 | Khoảng Từ – Đến | Ví dụ 2 ô Input + "–" | Lọc khoảng cước, tải trọng |
| web-24 | Ô + nhãn | Đầu 1/2 Tag | Mặt hàng chở, nhãn đơn |
| web-25 | Nhãn nằm trong ô | Khối trên Nhãn | Form mobile tài xế, cao 54 |

**Không dùng:** web-14 (nhãn nổi) · web-22 (giờ → `nz-time-picker`).

## 6. Figma

File `ElvhTYV3unixPkXky2oKIY`, trang **Input** (`47:2`) — khuôn như Button (dựng tạm 06/11, chờ duyệt):

| Khối | Node | Nội dung |
|---|---|---|
| Frame `Input` (tài liệu) | `40:3109` | Rộng 1536: đầu trang · Playground **Light** / **Dark** (mode Dark gắn trên khung) · `Ví dụ đã chốt` `40:3385` (lưới `40:3387`, 21 thẻ = instance Input + khe/addon; web-19, web-23 = hàng nhiều ô; web-17 còn mẫu cũ chờ Input OTP) · `Mapping` `40:3633` (bảng thuộc tính + bảng token) |
| Section Components | `47:3` | Set `Input / Body` (cấp 0) `47:442` = Kiểu (2) × Cỡ (3) × Trạng thái (7) = **42** + 6 khe; set `Input / Body / Addon` `96:31171` (10); set `Input / Body / Khối` `96:31209` (3) · Set `Textarea` `47:534` = Trạng thái (7) |
| Section Mẫu ghép cũ — chờ xoá | `40:2879` | (user giữ, chưa xoá 07/11) 21 component `Input mẫu ghép/web-NN …` ghép từ instance Input; 6 mẫu 07/11: `55:3767` web-07 · `55:3782` web-12 · `55:3796` web-18 · `55:3815` web-19 · `55:3857` web-24 · `55:3886` web-25 |
| Icons (trang Button, `14:10`) | `46:1278` search · `46:1283` circle-x · `46:1287` eye · `46:1291` map-pin · `55:3764` info · `55:3765` credit-card · `55:3766` x | lucide 16px, thêm cho Input |

Mỗi biến thể = khung dọc (gap 6): lớp `Ô` (nền, bo, padding, Focus ring giãn theo ô) gồm `Khối trên` + `Hàng` (cao = biến cao; Đầu 1 · Đầu 2 · Gợi ý · Chữ · Cuối 1 · Cuối 2) + `Khối dưới`; dưới `Ô` là `Dòng gợi ý`.
Thuộc tính Input: `Placeholder` (đổi tên từ `Gợi ý` 07/11) · `Chữ` · `Dòng gợi ý · chữ` (text) · `Dòng gợi ý` · `Đầu 1` · `Đầu 2` · `Cuối 1` · `Cuối 2` · `Khối trên` · `Khối dưới` (boolean). Khe là exposed instance → đổi Loại/chữ/icon của addon ngay ở bảng thuộc tính của instance Input.
Textarea: `Gợi ý` · `Chữ` · `Đếm ký tự` (boolean) · `Số đếm` (text).
Vòng 3px (Focus / Lỗi / Cảnh báo) = lớp `Focus ring` đặt tuyệt đối ngoài ô, như Button. Vòng cảnh báo = `color/warning` 20%
(ở Textarea để mã màu, chưa gắn biến — reqwise không gắn được biến kèm độ mờ).
Set Input, Textarea, icon, biến mới, mode Dark dựng bằng Figma MCP (plugin reqwise chưa bật lúc đầu); mẫu ghép, khung tài liệu, bảng dựng bằng reqwise.

### Đặt tên (user chốt 07/11)
L0 `_Input/Element/Addon` · `_Input/Element/Nhãn` (`136:2773`, nhãn trong ô — tách khỏi Khối 07/11; trục như Label: Kiểu Thường · Bắt buộc (*) · Tuỳ chọn ((không bắt buộc)) × Gợi ý Không · Có (ⓘ) × Trạng thái Mặc định · Đã tắt = 12; prop `Chữ`; exposed trong khe Nhãn trong ô) · `_Input/Element/Khối` (Đếm · Độ mạnh · Tag) · `_Input/Element/Điều kiện` · `_Input/Element/Độ mạnh` · `_Input/Element/Ô ghép` (+ `_icon/eye-off`) — L1 `Input/Base` (`47:442`) · `Input/Base/Nhóm` (`125:3049`, trục `Loại` = Trên 1 · dưới 2 · Ngang 2) — L2 `Input` (`116:9446`, trục `Loại` × `Trạng thái`). Textarea tách trang riêng: `Textarea/Base` (`47:534`), `Textarea` (`131:2340`). Tên component tiếng Anh, trục/giá trị tiếng Việt.

### Cấp component (user chốt 07/11) — L0 · L1 · L2
- **L0 · Element** (section riêng, khoá, tên có `_` đầu để ẩn khỏi thư viện): `_Input / Body / Addon`, `_… / Khối`, `_… / Điều kiện`, `_… / Độ mạnh`, `_… / Nhóm / Ô`, `_icon/eye-off` — cấu phần, không dùng riêng.
- Chữ mẫu L0/L1 trung tính (07/11): Nhãn "Nhãn" · Placeholder "Nhập nội dung" · Chữ "Nội dung" · Addon "Chữ" · Khối "Nhãn" · Điều kiện "Điều kiện" · Thông báo "Thông báo lỗi"; Nhóm không còn chữ/icon thẻ. Ngữ cảnh chỉ ở L2.
- **L1 · Component Base** (section `47:3`): `Input / Body`, `Textarea`, `Input / Body / Nhóm` — không mang ngữ cảnh.
- **L2 · Content Component** (section `111:829`): `Input` ma trận Type × Trạng thái — mang ngữ cảnh.

Ghi chú cũ (cấp 0/1):
- **Cấp 0 `Input / Body`** `47:442` (set gốc 42 biến thể + khe) và con `Input / Body / Addon` `96:31171`, `Input / Body / Khối` `96:31209` — section Components `47:3`.
- **Cấp 1 `Input`** `116:9446` — **ma trận Type × Trạng thái (vòng đời)**, 49 variant (user chốt 07/11), section riêng `111:829` ngay bên phải:
  Text (Chờ nhập · Đang nhập · Đã nhập · Lỗi · Đã tắt) · Search (Chờ nhập · Đang nhập · Có kết quả · Không có kết quả · Đã tắt) · Password (Chờ nhập · Đã nhập · Hiện chữ · Lỗi) ·
  Mật khẩu mới (Chờ nhập · Yếu · Trung bình · Mạnh; dòng tiêu đề trên danh sách điều kiện: "Nhập mật khẩu. Phải bao gồm:" · "Mật khẩu yếu. Phải bao gồm:" · "Mật khẩu trung bình. Phải bao gồm:" · "Mật khẩu mạnh. Phải bao gồm:"; thanh độ mạnh có số bước bằng số điều kiện (3)) · Copy (Mặc định · Đã chép) · Số (Chờ nhập · Đã nhập · Lỗi) · Đếm ký tự (Chờ nhập · Đang nhập · Gần hết · Vượt giới hạn) ·
  Tiền tố URL / Tiền tố SĐT (Chờ nhập · Đã nhập · Lỗi) · Mặt nạ (Chờ nhập · Đang nhập · Đã nhập · Lỗi) · Nhãn (tag) (Chờ nhập · Có nhãn · Đủ tối đa) ·
  Nhãn trong ô / Thẻ ngân hàng / Khoảng Từ–Đến (Chờ nhập · Đã nhập · Lỗi). Mỗi variant ghép từ `Input / Body` (exposed). OTP → Input OTP. Icon mới `icon/eye-off` `113:52763`.
  Bản 21 mẫu cũ `110:5477` chuyển sang section `Input — bản 21 mẫu (chờ xoá)`. Người vẽ màn dùng `Input`; cần kiểu mới thì ghép từ `Input / Body`.

### Ví dụ → set mẫu (07/11, user đổi ý: ví dụ bản chất là variant)
Set `Input` (cấp 1, trước tên `Input / Mẫu`) `110:5477` trong section Components: trục `Mẫu` 21 giá trị (Cơ bản · Có nhãn · Dòng gợi ý · Tìm + số kết quả · Tiền tố + ⓘ · Đơn vị · Tìm + chọn trường · Tiền · Chép · Đếm dưới ô · Mật khẩu · Đếm trong ô · Xoá nhanh · OTP · SĐT + mã quốc gia · Thẻ ngân hàng · Mật khẩu + độ mạnh · Mặt nạ · Khoảng Từ – Đến · Nhãn dưới ô · Nhãn trong ô), mỗi variant ghép từ instance Input (exposed → đổi Trạng thái/Cỡ/chữ) + addon/Label/Tag. Set Input thêm thuộc tính **`Nhãn`** (bật tắt, instance Label exposed trên ô, cách 6). Section ví dụ instance 104:527 đã bỏ (chuyển thành set).

Ghi chú so khớp (trước khi chuyển):
Section `Ví dụ — instance (copy để dùng)` `104:527` trên trang Input: 21 thẻ dựng từ Input + khe/addon, Label, Tag, so điểm ảnh với ảnh mẫu cũ:
cùng kích thước 21/21, lệch còn lại chỉ do nét chữ Geist (bản font lúc chụp ảnh cũ) và bo góc 10 thay pill (đã chốt). web-24 dùng Tag thật (chữ 400, × xám)
thay tag tạm của mẫu cũ. Chỉnh trên master khi so: icon addon màu `color/text-secondary`; `Nút`/`Chép` không đệm; `Chọn` chữ + ⌄ màu `color/text`,
thuộc tính `Vạch ngăn`; `Khối` Nhãn chữ 500; lớp `Ô` gap −6 (Khối trên + hàng = 54). Override riêng trong thẻ: web-07 gap 4, web-09 đệm phải 3 + chữ xám,
web-19/23 khối liền (bo theo vị trí, vạch 1px), web-20 thanh độ mạnh ngoài ô, web-25 lề 16.

### Bổ sung cấp 0 (07/11, rà từ cấp 1)
Cấp 1 không còn tự vẽ tại chỗ — mọi phần đều là instance cấp 0:
| Set cấp 0 | Biến thể | Dùng ở cấp 1 |
|---|---|---|
| `Input / Body / Điều kiện` `125:1794` | Đạt (✓ xanh, chữ 500) · Chưa đạt (✕ xám) · prop `Chữ` | Mật khẩu mới |
| `Input / Body / Độ mạnh` `125:1815` | Trống · Yếu (1 đỏ) · Trung bình (2 vàng) · Mạnh (3 xanh) — 3 vạch, bằng số điều kiện | Mật khẩu mới |
| `Input / Body / Nhóm / Ô` `126:16124` | Vị trí: Trên · Dưới trái · Dưới phải · Trái · Phải (Body bo góc theo vị trí, exposed) | dựng Nhóm |
| `Input / Body / Nhóm` `125:3049` | **Bố cục** (Trên 1 · dưới 2 · Ngang 2) × Trạng thái (Thường · Lỗi) — ma trận; viền + Focus ring quanh khối; prop `Thông báo` | Thẻ ngân hàng (Trên 1 · dưới 2), Khoảng Từ–Đến (Ngang 2) |
| `Input / Body / Khối` Loại=**Tag** | 5 Tag Viền, wrap, ẩn/hiện từng tag | Nhãn (tag) — đặt dưới ô |
| `icon/eye-off` `113:52763` | — | Password · Hiện chữ |
Body Focus có `Con trỏ`. Cấp 1 thêm Type **Nhiều dòng** (Textarea: Chờ nhập · Đang nhập · Đã nhập · Lỗi · Đã tắt) → 54 variant. `tag/radius` = `radius/sm` 6.

Khe `Khối trên` của Input/Base đổi tên **`Nhãn trong ô`** (instance `_Input/Element/Nhãn`, prop `Chữ`) — 07/11.
