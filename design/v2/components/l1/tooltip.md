---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
  - design/v2/components/l1/button.md
  - design/v2/components/l1/avatar.md
---

# Base / Tooltip

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Tooltip` (6405:2455, trang L1 · Base), khung
> tài liệu 6417:21363 (hình nên / không nên, cấu tạo phóng 2×) · DEC-206 · đã gắn sẵn trong [Button](button.md), [Avatar](avatar.md) (bật `Tooltip`)

## Khi dùng

Nhãn ngắn nổi lên khi rê chuột hoặc focus vào một đối tượng, **chỉ trên web** (điện thoại không có rê chuột).

- **Nút chỉ có icon:** tên hành động ("Thêm lệnh", "Tải tệp lên"). Bắt buộc cho Button Icon Only trên web.
- **Avatar đứng một mình:** tên người ("Nguyễn An"), kèm trạng thái nếu có chấm ("Nguyễn An · Đang bận").
- **Chữ bị cắt:** toàn văn của ô bảng, tên dài bị "…".
- **Placement:** phía tooltip nằm so với đối tượng. Mặc định **Top**; gần mép trên màn thì Bottom; đối tượng ở cột
  trái, phải sát mép thì Right, Left. Mũi tên chỉ vào giữa đối tượng.

Không dùng tooltip cho thông tin người dùng cần đọc mới làm tiếp được (lỗi, hướng dẫn nhập): dùng chữ phụ dưới ô hoặc
thông báo. Không đặt nút, link trong tooltip.

## Nên và không nên

Hình minh hoạ ở khung tài liệu cạnh component trên Figma.

1. **Nên:** tooltip 1–4 từ, nói đúng hành động của nút icon. **Không nên:** lặp lại đúng chữ đã hiện trên nút có chữ.
2. **Nên:** tooltip một dòng, ngắn. **Không nên:** đoạn hướng dẫn dài trong tooltip; quá 240 thì tự xuống dòng, nhưng
   đã cần xuống dòng thì nên đưa ra chữ phụ.

## Trạng thái

Không có trạng thái riêng. Hiện khi rê chuột hoặc khi focus bằng bàn phím; ẩn khi rời đi, khi bấm Esc. Rê chuột từ đối tượng sang tooltip thì tooltip vẫn hiện.

## Chữ

Viết hoa chữ đầu, không chấm cuối câu. Tên hành động là động từ như nhãn nút ("Xoá lệnh"); tên người viết đủ họ tên.

## Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | Kết quả |
|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ chữ trắng trên `bg/inverse`: 17,73 |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ đóng được (Esc), rê lên được (không tắt khi chuột chuyển sang tooltip), giữ nguyên tới khi rời đi |
| 2.1.1 Bàn phím | ✓ hiện khi focus bằng Tab, không chỉ khi rê chuột |
| 4.1.2 Tên, vai trò | ✓ đối tượng nối tới tooltip bằng `aria-describedby`; nút Icon Only vẫn phải có `aria-label` riêng |
| 1.3.3 Đặc tính giác quan | ✓ không dùng cho thông tin bắt buộc; mobile không có tooltip nên nội dung đó phải có chỗ khác |
| **Điểm** | **5/5 đạt** |

## Dùng ở đâu

Nút icon ở đầu màn, thanh công cụ, hàng bảng (web); Avatar, Avatar Group; ô bảng bị cắt chữ.

## Tên trong code

`<Tooltip content="Thêm lệnh" placement="top|bottom|left|right"><Button iconOnly … /></Tooltip>`; biến CSS
`--tooltip-*` (nền, chữ, lề, bo, rộng tối đa, mũi tên, khoảng cách).

## Phần phụ (máy không đọc)

| Phần | Số đo | Token |
|---|---|---|
| Mũi tên | 8 × 4 (Left, Right xoay thành 4 × 8) | `tooltip/arrow-w`, `tooltip/arrow-h`, màu `tooltip/bg` |
| Khoảng cách tới đối tượng | 4 | `tooltip/offset` |

## Cấu tạo, thuộc tính, token

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Tooltip` (6405:2455) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Text | Chữ | Thêm lệnh | — |
| Placement | Biến thể | Top | Top · Bottom · Left · Right |

4 biến thể · trục Placement.

### Màu theo phần (token)

| Nền | Chữ |
|---|---|
| `tooltip/bg` | `tooltip/fg` |

### Số đo theo phần (token)

| Placement | Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Bo | Rộng tối đa |
|---|---|---|---|---|---|---|---|---|
| Top | 28 | ôm nội dung | `tooltip/padding-x` | `tooltip/padding-x` | `tooltip/padding-y` | `tooltip/padding-y` | `tooltip/radius` | `tooltip/max-width` |
| Bottom | 28 | ôm nội dung | `tooltip/padding-x` | `tooltip/padding-x` | `tooltip/padding-y` | `tooltip/padding-y` | `tooltip/radius` | `tooltip/max-width` |
| Left | 24 | ôm nội dung | `tooltip/padding-x` | `tooltip/padding-x` | `tooltip/padding-y` | `tooltip/padding-y` | `tooltip/radius` | `tooltip/max-width` |
| Right | 24 | ôm nội dung | `tooltip/padding-x` | `tooltip/padding-x` | `tooltip/padding-y` | `tooltip/padding-y` | `tooltip/radius` | `tooltip/max-width` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Thêm lệnh | `type/caption` |

<!-- auto:end -->
