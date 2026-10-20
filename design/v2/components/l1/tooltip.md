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
  - design/v2/components/l1/avatar-group.md
---

# Base / Tooltip

> L1 · phiên bản 0.2.0 · Nháp · người phụ trách @szitphan · Figma `Base / Tooltip` (6405:2455, trang DS · Components ·
> L0–L3), L0 `.tooltip / Arrow` (6442:84443), khung tài liệu `Tài liệu · Tooltip` (6467:84315) · DEC-206, DEC-213, DEC-245, DEC-246 ·
> lồng sẵn trong [Button](button.md), [Avatar](avatar.md) (bật `Tooltip`)

Một component, **chỉ dùng trên web** (DEC-206): nhãn ngắn nổi lên khi rê chuột hoặc focus vào một đối tượng. Lề, bo,
mũi tên, khoảng cách, cỡ chữ đọc từ biến collection Platform; màu (collection Component) một bộ duy nhất. Phần **Web**
tả đầy đủ component. Phần **Mobile** ngắn: app không dùng Tooltip, phần đó nói nội dung tooltip đi đâu trên app. Mỗi
phần tự đứng được.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Nút chỉ có icon:** tên hành động ("Thêm", "Tải tệp lên"). Bắt buộc cho Button Icon Only trên web: bật thuộc tính
  Tooltip của Button.
- **Avatar đứng một mình:** tên người, kèm trạng thái nếu có chấm. Bật thuộc tính Tooltip của Avatar (Avatar Group, cột
  người phụ trách trong bảng).
- **Chữ bị cắt:** toàn văn của ô bảng, tên dài bị "…".
- **Không dùng** cho thông tin phải đọc mới làm tiếp được (lỗi, hướng dẫn nhập): dùng chữ phụ dưới ô hoặc thông báo.
  Không đặt nút, link trong tooltip.
- **Content:** một đoạn chữ (thuộc tính Text) trên bóng nền tối, mũi tên chỉ vào giữa đối tượng. Không icon, không nút.
- **Cỡ web:** chữ `type/caption` 12/16; lề 8 × 4; bo 8; rộng ôm chữ, tối đa 240 rồi xuống dòng; mũi tên 8 × 4; cách đối
  tượng 4 (DEC-206).
- **Chỉ có ở web:** cả component; app không có rê chuột nên không dùng (xem [Mobile](#mobile)).
- **Placement:** mặc định Top; gần mép trên màn thì Bottom; đối tượng sát mép phải thì Left, sát mép trái thì Right.
- **Hiện, ẩn:** hiện khi rê chuột hoặc focus bằng Tab; ẩn khi rời đi hoặc bấm Esc; rê từ đối tượng sang tooltip thì
  tooltip vẫn hiện.
- **Chữ:** 1–4 từ, viết hoa chữ đầu, không chấm cuối câu; tên hành động là động từ như nhãn nút; tên người viết đủ họ
  tên. Không lặp lại đúng chữ đã hiện trên nút có chữ.

### Cấu tạo

Hình phóng 2× trên Figma: Placement=Top, chữ mặc định; bên cạnh là Base / Button · Secondary · Icon Only · MD bật
Tooltip để thấy khoảng cách tới đối tượng.

| Phần | Token | Giá trị web |
|---|---|---|
| Nền (bóng và mũi tên) | `tooltip/bg` → `color/bg/inverse` → `neutral/900` | #121826 |
| Chữ | thuộc tính Text; `type/caption`; màu `tooltip/fg` → `color/text/inverse` → `white` | 12/16 Regular, #FFFFFF |
| Lề | `tooltip/padding-x` · `tooltip/padding-y` | 8 · 4 |
| Bo | `tooltip/radius` | 8 |
| Rộng | ôm chữ, tối đa `tooltip/max-width` | tối đa 240, quá thì xuống dòng |
| Cao bóng | 2 × `tooltip/padding-y` + `type/caption` line-height | 24 một dòng, mỗi dòng thêm 16 |
| Mũi tên | L0 `.tooltip / Arrow`; `tooltip/arrow-w` × `tooltip/arrow-h`; màu `tooltip/bg` | 8 × 4 (Left, Right xoay thành 4 × 8) |
| Khoảng cách | `tooltip/offset`, từ mép đối tượng tới đầu mũi tên; component cha đặt (Button, Avatar: nổi trên). Tooltip tự canh giữa nhờ lớp `Tooltip wrap` (Button, Avatar) | 4 |

### Biến thể

Trục Placement: Top · Bottom · Left · Right (4 biến thể). Mũi tên (`.tooltip / Arrow`) đổi Direction theo Placement và
luôn chỉ vào giữa đối tượng. Trên Figma có hai hàng: tooltip đứng riêng và tooltip đặt cạnh Base / Button · Secondary ·
Icon Only · MD, cách 4.

### Trạng thái

Không có State riêng; tooltip hiện theo đối tượng.

| Đối tượng | Tooltip |
|---|---|
| Default | ẩn |
| Hover (rê chuột) | hiện |
| Focus (bằng Tab) | hiện; vòng focus của đối tượng vẫn thấy dưới tooltip |
| Rời đi, bấm Esc | ẩn |
| Rê từ đối tượng sang tooltip | vẫn hiện |

### Kích thước

Không có trục cỡ. Đo trên Figma 20/10 (Placement=Top):

| Chữ | Rộng | Cao | Số dòng |
|---|---|---|---|
| Ngắn: "Thêm" (mặc định) | 49 | 28 | 1 |
| Vừa: "Tải tệp lên" | 75 | 28 | 1 |
| Dài (toàn văn chữ bị cắt) | 240 = tối đa | 60 | 3 |

Cao gồm mũi tên 4 ở Top, Bottom; Left, Right cao 24 (một dòng).

### Nên và không nên

Hình minh hoạ ở khung tài liệu trên Figma (cảnh trên nền trắng, tooltip ghép cạnh Base / Button · Secondary · Icon Only ·
MD).

1. **Nên:** tooltip 1–4 từ, nói đúng hành động của nút chỉ có icon ("Thêm"). **Không nên:** lặp lại đúng chữ đã hiện
   trên nút có chữ (nút "Thêm" kèm tooltip "Thêm").
2. **Nên:** một dòng, ngắn ("Xoá"); đọc lướt khi rê chuột qua. **Không nên:** đoạn hướng dẫn dài trong tooltip: phải
   giữ chuột để đọc, app không thấy. Đưa ra chữ phụ.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | chữ `tooltip/fg` trên `tooltip/bg`: 17,73 |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ | đóng được (Esc), rê lên được (không tắt khi chuột chuyển sang tooltip), giữ nguyên tới khi rời đi |
| 2.1.1 Bàn phím | ✓ | hiện khi focus bằng Tab, không chỉ khi rê chuột |
| 4.1.2 Tên, vai trò | ✓ | đối tượng nối tới tooltip bằng `aria-describedby`; nút Icon Only vẫn phải có `aria-label` riêng |
| 1.3.3 Đặc tính giác quan | ✓ | không dùng cho thông tin bắt buộc; app không có tooltip nên nội dung đó phải có chỗ khác (phần Mobile) |
| **Điểm web** | | **5/5 đạt** · 2.5.8 không áp (tooltip không bấm được) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Placement | Biến thể | Top | Top · Bottom · Left · Right |
| Text | Chữ | Thêm | tên hành động, tên người, toàn văn chữ bị cắt; quá 240 tự xuống dòng |

Trong Button, Avatar: tooltip bật bằng thuộc tính `Tooltip` (Bật tắt, mặc định tắt) của cha; instance Tooltip lồng
được đưa ra panel nên sửa được chữ.

### Thành phần lồng

Tooltip ráp từ L0 `.tooltip / Arrow` và lớp của chính nó; không chứa L1 khác.

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Mũi tên | `.tooltip / Arrow` · L0 (6442:84443) | Direction theo Placement: Top → Down, Bottom → Up, Left → Right, Right → Left; cỡ 8 × 4, màu `tooltip/bg` | — |
| Bóng | khung của Tooltip (không phải component) | nền `tooltip/bg`, lề 8 × 4, bo 8, rộng tối đa 240 | — |
| Chữ | lớp chữ của Tooltip | `type/caption`, màu `tooltip/fg` | Text |

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components (bỏ instance trong khung tài liệu và instance mồ côi).

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Button | lớp `Tooltip` nổi trên nút (vị trí tuyệt đối), canh giữa, cách 4 | Placement=Top · chữ mặc định "Thêm" · bật bằng `Tooltip` (mặc định tắt) · có ở cả 225 biến thể; dùng cho Icon Only |
| Base / Avatar | lớp `Tooltip` nổi trên avatar, canh giữa, cách 4 | Placement=Top · chữ đè "Họ tên" · bật bằng `Tooltip` (mặc định tắt) · 45 biến thể |
| Base / Avatar Group | gián tiếp: trong từng Base / Avatar (instance Avatar đưa ra panel) | Tooltip từng avatar, mặc định tắt; web bật để rê chuột thấy tên ([Avatar Group](avatar-group.md), Nên 2) |

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Lề ngang | `tooltip/padding-x` | 8 |
| Lề dọc | `tooltip/padding-y` | 4 |
| Bo | `tooltip/radius` | 8 |
| Rộng | ôm chữ, tối đa `tooltip/max-width` | tối đa 240 |
| Mũi tên | `tooltip/arrow-w` × `tooltip/arrow-h` | 8 × 4 (Left, Right 4 × 8) |
| Cách đối tượng | `tooltip/offset` | 4 |
| Chữ | `type/caption` (size, line-height) | 12/16 Regular |
| Cao bóng | 2 × `tooltip/padding-y` + line-height | 24 một dòng; Top, Bottom +4 |
| Vùng chạm | — (không bấm được) | không áp |

Màu (collection Component, tiền tố `tooltip/`): `tooltip/bg` → `color/bg/inverse` → `neutral/900` #121826 (nền, mũi
tên) · `tooltip/fg` → `color/text/inverse` → `white` #FFFFFF (chữ). Một bộ màu, không đổi theo trạng thái.

Tên trong code: `<Tooltip content="Thêm" placement="top|bottom|left|right"><Button iconOnly … /></Tooltip>`; biến CSS
`--tooltip-*` (nền, chữ, lề, bo, rộng tối đa, mũi tên, khoảng cách), `--type-caption-*`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6467:84315 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 20 ô, 28 mẫu (khối Web) | luật A: 0 lỗi, ô nào cũng có nền thật `color/bg/surface` và viền mảnh |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có, 0 cờ (Button Secondary Focus: khe #FFFFFF trên ô #FFFFFF, vòng 15,13) |
| Lớp con (lớp "Bóng") | 15 mẫu | nền tooltip nằm ở lớp con `Bóng` (lớp ngoài không nền): `tooltip/bg` #121826 trên ô trắng 17,73:1, 0 cờ |
| Sát ngưỡng | 11 mẫu Base / Button · Secondary | nền #F2F4F7 trên ô trắng = 1,10 — số của Button, xem tài liệu Button |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile.

### Tổng quan

- **Không dùng trên app:** điện thoại không có rê chuột; Tooltip chỉ dùng trên web (DEC-206). Không đặt Base / Tooltip
  vào màn app.
- **Trong component cha:** Button, Avatar có thuộc tính `Tooltip`: trên app để tắt (mặc định đã tắt).
- **Biến `tooltip/*` vẫn có mode Mobile:** lề 8 × 4, bo 8, rộng tối đa 240, mũi tên 8 × 4, cách 4; chữ `type/caption`
  13/18. Chưa có màn app nào dùng.
- **Nội dung không chỉ nằm trong tooltip:** mọi thông tin web để trong tooltip phải có chỗ khác trên app (bảng dưới).
- **Focus:** app chỉ có focus khi dùng bàn phím ngoài hoặc công cụ trợ năng; khi đó trình đọc màn hình đọc nhãn trợ
  năng của đối tượng, không có tooltip.

### Thay bằng gì

Lấy từ tài liệu component đã có, không thêm cách mới.

| Trên web, tooltip dùng cho | Trên app thay bằng | Nguồn |
|---|---|---|
| Tên hành động của nút chỉ có icon | nhãn trợ năng của nút: trình đọc màn hình đọc, không hiện chữ; icon phải quen thuộc; vùng chạm ≥ `touch/min` = 44 | [Button](button.md) phần Mobile (Content, Trợ năng 4.1.2, 2.5.5) |
| Tên người khi nhiều avatar xếp chồng (Avatar Group) | bấm vào nhóm mở danh sách đủ người | [Avatar Group](avatar-group.md) · Nên và không nên 2 |
| Trạng thái của người (chấm trên avatar) | chữ ở dòng phụ, vd "Đang trực tuyến" | [Avatar](avatar.md) · Nên và không nên 2 |
| Toàn văn chữ bị cắt "…" | xem đủ ở trang chi tiết | [Status Chip](status-chip.md) · Trợ năng 1.4.12 |
| Thông tin phải đọc mới làm tiếp (lỗi, hướng dẫn) | chữ phụ dưới ô hoặc thông báo, như web; không bao giờ để trong tooltip | [Tooltip](tooltip.md) · Tổng quan (mục Không dùng) |

### Trợ năng — chấm theo WCAG 2.2

Chấm riêng cho app: chỉ các tiêu chí áp dụng khi không có tooltip.

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.3.3 Đặc tính giác quan | ✓ | nội dung web để trong tooltip có chỗ khác trên app (bảng Thay bằng gì) |
| 4.1.2 Tên, vai trò | ✓ | nút chỉ có icon có nhãn trợ năng (Button phần Mobile) |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài hoặc công cụ trợ năng: focus vào nút thì đọc nhãn trợ năng; mở danh sách, trang chi tiết bằng Enter như mọi nút (Button phần Mobile 2.1.1) |
| 1.4.13 Nội dung hiện khi rê, focus | — | không áp: app không có nội dung hiện khi rê |
| **Điểm app** | | **3/3 tiêu chí áp đạt** |

### Thuộc tính

Không đặt Base / Tooltip trên app. Thuộc tính `Tooltip` của Button, Avatar: để tắt.

### Kiểm máy

Khối Mobile không có ô mẫu (component không dùng trên app) nên script không có gì để đo: 0 ô, 0 cờ.

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của phần Web và Tổng quan của phần Mobile.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Tooltip` (6405:2455) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Text | Chữ | Thêm | — |
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
| Thêm | `type/caption` |

<!-- auto:end -->
