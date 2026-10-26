---
type: design-component
status: draft
updated: 2026-10-26
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - design/v2/components/README.md
  - _workspace/decisions.md
  - design/v2/components/l1/status-chip.md
  - design/v2/components/l1/record-card.md
  - design/v2/components/l1/selectable-card.md
---

# Base / Status Row

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Status Row` (6458:83667, component đơn, trang DS ·
> Components · L0–L3, Section `Card · L1 · Component Base` 6444:24203), khung tài liệu `Tài liệu · Status Row` (6562:224997,
> khối Web 6562:225004, khối Mobile 6562:225025) · DEC-233 (luật lồng), DEC-235 (tách Status Row khỏi `.card / Row`), DEC-239
> (chip Size) · ráp từ L0 `.card / Row` và [Status Chip](status-chip.md); dùng trong [Record Card](record-card.md), Selectable Card

Một component cho cả web và app, không có biến thể: cao chip, cỡ chữ đọc từ biến collection Platform, khung chứa đặt mode Web
hoặc Mobile thì dòng tự đổi. Màu giống nhau ở hai nền tảng. Một dòng = **nhãn (`.card / Row` Type=Label) · chip
(`Base / Status Chip` MD)**, canh hai đầu. Dòng chỉ đọc nên không có State. Chữ mẫu Label, Status.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Khi dùng:** một dòng nhãn – trạng thái trong thẻ: Slot `Rows` của Record Card, Slot `Body` của Selectable Card. Cho trạng
  thái phụ của bản ghi khi trạng thái chính đã ở chip đầu thẻ.
- **Vì sao là L1 riêng:** chip là `Base / Status Chip` (L1, dùng riêng được); L0 không được chứa L1 (luật c, DEC-233) nên dòng có
  chip không còn là `.card / Row` Type=Status; tách thành L1 (DEC-235).
- **Cấu tạo:** `.card / Row` Type=Label (nhãn) + `Base / Status Chip` MD; canh hai đầu (space-between), cách tối thiểu 16, canh
  giữa dọc; không nền, không lề (nền và lề là của thẻ chứa).
- **Chip:** Type Soft · Dot × 8 Tone, chữ, icon đổi ở panel (instance lộ ra); giữ Size MD, không đè cỡ.
- **Nhãn:** màu phụ, rộng tối đa 120, một dòng cắt "…"; tên trạng thái để ở chip, không lặp ở nhãn.
- **Chỉ có ở web:** không có: dòng không bấm được; web và app khác cỡ chữ; chip cao 24 ở cả hai (DEC-259).
- **Rộng:** mẫu 329 (= thẻ 361 − 2 × lề 16); trong Slot tự kéo giãn theo thẻ.
- **Chữ:** khi dùng, chữ chip lấy nguyên văn trạng thái trong SRS, Tone theo bảng ánh xạ ở tài liệu Status Chip.

### Cấu tạo

Hình phóng 2× trên Figma (ô 1290 × 312, nền `color/bg/surface`): mặc định (nhãn Label, chip Soft · Gray · Status).

| Phần | Token | Giá trị web |
|---|---|---|
| Nhãn | L0 `.card / Row` Type=Label: `type/body` `color/text/secondary`; rộng tối đa `card/row-label-max` | 14/20 · 120, một dòng, cắt "…" |
| Chip | **Base / Status Chip · MD · Soft → xem tài liệu Status Chip** | không lặp token |
| Khung dòng | ngang, space-between, canh giữa dọc; khoảng tối thiểu `space/gap-lg`; cao tối thiểu `card/row-min-height` | 16 · 24; không nền, không lề |
| Rộng | mẫu; kéo giãn theo Slot (stretchChildOnInsert của Slot cha) | 329 |

### Biến thể

Component đơn: không có trục biến thể, không có State. Cấu hình qua chip lộ ra (Type Soft · Dot × 8 Tone) và chữ nhãn. Khung có
ba mẫu: Soft · Gray (mặc định) · Soft · Green · Dot · Blue.

### Trạng thái

Không có — dòng chỉ đọc, không bấm được. Trạng thái nghiệp vụ nằm ở Tone và chữ của chip (bảng ánh xạ trạng thái → sắc ở tài
liệu Status Chip).

### Kích thước

| Trường hợp | Cao | Cách tính |
|---|---|---|
| Một dòng | 24 | lớn nhất của `chip/height` 24, chữ 20, `card/row-min-height` 24 |
| Trong Slot Rows của Record Card | +8 | cách dòng khác `space/gap-sm` 8 |
| Trong Slot Body của Selectable Card | +4 | cách dòng khác `space/gap-xs` 4 (DEC-236) |
| Rộng | 329 | mẫu; kéo giãn theo Slot |
| Vùng chạm | — | không bấm được |

### Nên và không nên

1. **Nên:** nhãn ngắn một dòng, chip canh phải. **Không nên:** nhãn dài quá 120 bị cắt "…"; tên trạng thái để ở chip, không viết
   vào nhãn.
2. **Nên:** trạng thái chính ở chip đầu thẻ, Status Row cho trạng thái phụ khác; hoặc tắt chip đầu thẻ khi trạng thái nằm ở dòng.
   **Không nên:** lặp cùng một trạng thái ở chip đầu thẻ và ở Status Row.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | nhãn 5,43 trên thẻ trắng, 4,92 trên thẻ chọn xám (`card/choice/bg`); chữ chip → xem tài liệu Status Chip |
| 1.4.1 Dùng màu | ✓ | chip có chữ (Soft thêm icon), không chỉ dựa vào màu |
| 1.3.1 Thông tin và quan hệ (A) | ✓ | khi code: nhãn và chip là một cặp (`dt`/`dd` hoặc `aria-label` của dòng) |
| 4.1.2 Tên, vai trò | ✓ | không bấm được nên không role button; đọc "nhãn: trạng thái" |
| 2.3.3 Chuyển động | ✓ | không chuyển động |
| Không áp dụng | — | 1.4.11, 2.4.7, 2.4.13, 2.5.8, 2.1.1, 1.4.13: không có control |
| **Điểm web** | | **5/5 đạt** |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| (không có) | — | — | Status Row không có thuộc tính riêng |
| Nhãn | instance lộ ra | Label | chữ nhãn (Label của `.card / Row`) |
| Trạng thái | instance lộ ra | Soft · Gray · Status | Type, Tone, Label, Icon của Base / Status Chip; giữ Size MD |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Nhãn | `.card / Row` Type=Label · L0 | một dòng, rộng tối đa 120 | Nhãn |
| Trạng thái | `Base / Status Chip` · L1 → xem [tài liệu Status Chip](status-chip.md) | Size MD; Soft · Dot × 8 Tone; icon gợi ý `icon/circle-check`, `icon/clock`, `icon/triangle-alert`, `icon/circle-x` | Trạng thái |

### Được dùng trong

Kiểm 20/10: Status Row là giá trị gợi ý (preferred value, Slot khoá) của Slot ở hai component cha; chưa có instance đặt sẵn
(`findInstances` = 0 ngoài khung tài liệu). Hình trên Figma: Record Card nền trắng, dòng 3 đổi sang Status Row, cắt còn vùng dòng.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Record Card | Slot `Rows` (giá trị gợi ý, chưa đặt sẵn) | một trong tối đa 4 dòng, cách 8, rộng theo thẻ; chip MD |
| Base / Selectable Card | Slot `Body` khi Has Body bật (giá trị gợi ý) | tối đa 3 dòng, cách 4; chip MD |

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Cao tối thiểu | `card/row-min-height` | 24 |
| Khoảng tối thiểu | `space/gap-lg` | 16 |
| Nhãn rộng tối đa | `card/row-label-max` | 120 |
| Chữ nhãn | `type/body` | 14/20 |
| Cao chip | `chip/height` (của Status Chip → xem tài liệu) | 24 |
| Vùng chạm | `touch/min` | không áp (không bấm) |

Màu: nhãn `color/text/secondary` → neutral/500; không nền (nền là thẻ chứa); chip → xem tài liệu Status Chip. Một bộ màu cho web
và app.

Tên trong code: `<StatusRow label status tone type />`; biến CSS `--card-row-min-height`, `--card-row-label-max`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6562:224997 ngày 20/10 (ngưỡng 1,1:1; ô dòng nền `color/bg/surface`, ô thẻ nền
trắng theo DEC-258).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 8 ô, 8 mẫu (khối Web; cả khung 16 ô, 16 mẫu) | luật A: 0 lỗi; không cờ B, C, D |
| Sát ngưỡng (lớp "Trạng thái") | Biến thể · Soft · Gray, Cảnh · nhãn | dòng không nền, đo ở chip: nền chip Gray #F2F4F7 trên ô trắng = 1,10:1 (đã ghi ở tài liệu Status Chip, chip giữ hình nhờ chữ, icon) |
| Sát ngưỡng (lớp "Trạng thái") | Biến thể · Soft · Green | nền chip #E8F5EC trên ô trắng = 1,12:1 |
| Ranh giới (lớp "Khung thẻ") | Cảnh · trong thẻ, Được dùng trong | thẻ trắng trên ô trắng: giữ hình nhờ viền 1,25:1 (số tính lại theo nền trắng (DEC-258), chưa chạy lại máy) |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Khi dùng, vì sao là L1, cấu tạo, chip, nhãn, rộng, chữ:** như web.
- **Khác web:** chữ nhãn 15/22; cao 24 như web (chip MD 24, DEC-259).

### Cấu tạo

Hình phóng 2× trên Figma (ô 1290 × 316): như web, mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Nhãn | `.card / Row` Type=Label: `type/body`; `card/row-label-max` | 15/22 · 120 |
| Chip | **Base / Status Chip · MD · Soft → xem tài liệu Status Chip** | không lặp token |
| Khung dòng | `space/gap-lg`; `card/row-min-height` | 16 · 24 (cao thật 24, bằng chip) |

### Biến thể

Như web.

### Trạng thái

Không có (như web).

### Kích thước

| Trường hợp | Cao | Cách tính |
|---|---|---|
| Một dòng | 24 | lớn nhất của `chip/height` 24, chữ 22, `card/row-min-height` 24 |
| Trong Slot Rows của Record Card | +8 | `space/gap-sm` 8 |
| Trong Slot Body của Selectable Card | +4 | `space/gap-xs` 4 |
| Rộng | 329 | mẫu; kéo giãn theo Slot |
| Vùng chạm | — | không bấm được |

### Nên và không nên

Như web (cùng hai cặp).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | như web: nhãn 5,43 (4,92 trên thẻ chọn xám) |
| 1.4.1 Dùng màu | ✓ | chip có chữ |
| 1.3.1 Thông tin và quan hệ (A) | ✓ | nhãn trợ năng đọc "nhãn: trạng thái" |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng: không bấm được nên không role button |
| 2.3.3 Chuyển động | ✓ | không chuyển động |
| Không áp dụng | — | 1.4.11, 2.4.7, 2.4.13, 2.5.8, 2.5.5, 2.1.1: không có control |
| **Điểm app** | | **5/5 đạt** |

### Thuộc tính

Như web (cùng bảng).

### Thành phần lồng

Như web (cùng bảng).

### Được dùng trong

Như web (cùng bảng): Record Card cách 8, Selectable Card cách 4; chip MD 24 ở app.

### Token

Số đo (collection Platform, mode Mobile): cao tối thiểu `card/row-min-height` 24 (cao thật 24, bằng chip) · khoảng tối thiểu
`space/gap-lg` 16 · nhãn tối đa `card/row-label-max` 120 · chữ `type/body` 15/22 · `chip/height` 24 (của Status Chip). Màu như web.

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 8 ô, 8 mẫu (khối Mobile) | luật A: 0 lỗi; không cờ B, C, D |
| Sát ngưỡng | như web | chip Gray 1,10:1, Green 1,12:1 trên ô trắng; thẻ trắng trên ô trắng giữ hình nhờ viền 1,25:1 |

## Đối chiếu Astryx

Astryx không có dòng nhãn – trạng thái riêng (thẻ Astryx đổ mọi thứ vào Slot `Content`). Status Row là khuôn Invlogis: tách từ
`.card / Row` Type=Status cũ vì L0 không được chứa L1 (DEC-233, DEC-235); chip là `Base / Status Chip` (xem tài liệu Status Chip).

| | Astryx | DS v2 | Vì sao |
|---|---|---|---|
| Lệch | không có thành phần dòng trong thẻ | L1 `Base / Status Row` = `.card / Row` Type=Label + `Base / Status Chip` MD | dòng trạng thái lặp ở nhiều thẻ L2; L0 không chứa L1 |
| — | — | chip MD 24 giữ nguyên token của Status Chip | luật e: cha chỉ quyết khoảng cách quanh chip |

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần. Chữ chip là của L1 lồng (Status Chip), không ghi
ở đây; JSON xuất đã bỏ cột nhiễu (README Mục 13).

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Status Row` (6458:83667) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|

Component đơn, không có trục biến thể.

### Màu theo phần (token)

| Chữ |
|---|
| `color/text/secondary` |

### Số đo theo phần (token)

| Cao | Rộng | Khoảng giữa |
|---|---|---|
| 24 | 329 | `space/gap-lg` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label (Nhãn) | `type/body` |

<!-- auto:end -->
