---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - design/v2/components/README.md
  - _workspace/decisions.md
  - design/v2/components/l1/card.md
  - design/v2/components/l1/record-card.md
---

# Base / Summary Card

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Summary Card` (6442:85948, component đơn, trang DS ·
> Components · L0–L3, Section `Card · L1 · Component Base` 6444:24203), khung tài liệu `Tài liệu · Summary Card` (6562:223644,
> khối Web 6562:223651, khối Mobile 6562:223675) · DEC-211 (khuôn thẻ Invlogis), DEC-233 (luật lồng), DEC-234 (ráp trên Base /
> Card); giữ DEC-125, DEC-192 như đã nêu ở từng mục · ráp trên [Card](card.md); thẻ bấm được xem [Record Card](record-card.md)

Một component cho cả web và app, không có biến thể: lề, bo, cỡ chữ đọc từ biến collection Platform, khung chứa đặt mode Web
hoặc Mobile thì thẻ tự đổi. Màu giống nhau ở hai nền tảng. Một thẻ = **tiêu đề · Slot Rows (nhãn – giá trị) · đường kẻ · dòng
tổng**, ráp trên khung `Base / Card`. Thẻ chỉ đọc nên không có State. Chữ mẫu Title, Label, Value.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Khi dùng:** tóm tắt các cặp nhãn – giá trị và một dòng tổng (chi phí, số lượng, thanh toán) ở màn chi tiết, màn xác nhận,
  sheet. Chỉ đọc. Thẻ một bản ghi bấm được thì dùng [Record Card](record-card.md).
- **Ráp trên Base / Card:** lớp đầu "Khung thẻ" (`Base / Card` · State Default · Padding None · Elevation Low) đặt tuyệt đối,
  kéo giãn theo thẻ; khung lo nền, viền, bo, bóng (DEC-234).
- **Vì sao không dùng Slot Content:** nội dung trong Slot của instance lồng không gắn được Boolean hay Slot, nên tiêu đề, Slot
  `Rows`, đường kẻ, dòng tổng là con trực tiếp để giữ `Has Total` và Slot `Rows`.
- **Thứ tự cố định:** `.card / Heading` (chỉ Title) → Slot `Rows` → `.card / Divider` → dòng tổng (`.card / Row` Type=Total).
- **Rows:** Slot, 1–8 dòng `.card / Row` Type=Label Value, cách 8; chỉ nhận `.card / Row` (không nhận Status Row).
- **Has Total:** tắt cả đường kẻ lẫn dòng tổng.
- **Nhãn – giá trị:** nhãn màu phụ, rộng tối đa 120 (`card/row-label-max`), một dòng cắt "…"; giá trị canh phải, một dòng,
  cách nhãn 16.
- **Dòng tổng:** nhãn chữ chính, giá trị đậm `type/heading`; khác dòng thường ở độ đậm và đường kẻ, không ở màu.
- **Chỉ có ở web:** không có: thẻ không bấm được nên không có Hover; web và app chỉ khác bo, cỡ chữ.
- **Chữ:** tiền, số theo quy ước Content & Formatting. Đổi chữ ở panel (Heading, Dòng tổng lộ ra).
- **Rộng:** mẫu 361; dùng thật đặt Fill, cao ôm nội dung.

### Cấu tạo

Hình phóng 2× trên Figma (ô 1290 × 630, nền `color/bg/canvas`, Context = Canvas): mặc định, 3 dòng nhãn – giá trị, Has Total bật.

| Phần | Token | Giá trị web |
|---|---|---|
| Khung thẻ | **Base / Card · State Default · Padding None · Elevation Low · Tone Surface → xem tài liệu Card** | nền, viền, bo `radius/card` 12, bóng `elev/1`; không lặp token |
| Khung nội dung | lề `layout/card-padding`; khoảng `space/gap-md` | 16 · 12; rộng mẫu 361, cao ôm nội dung |
| Tiêu đề | L0 `.card / Heading`: Title `type/heading` `color/text/primary`; Subtitle tắt | 14/20, một dòng |
| Slot Rows | khoảng `space/gap-sm`; 1–8 dòng | 8 |
| `.card / Row` Label Value | cao tối thiểu `card/row-min-height`; nhãn `type/body` `color/text/secondary`, rộng tối đa `card/row-label-max`; cách giá trị `space/gap-lg`; giá trị `type/body` `color/text/primary`, canh phải | 24 · 14/20 · 120 · 16 |
| Đường kẻ | L0 `.card / Divider`: cao `card/border-width`, `color/border/default` | 1, đầy bề ngang |
| Dòng tổng | L0 `.card / Row` Type=Total: nhãn `type/body` `color/text/primary`; giá trị `type/heading`, canh phải | 14/20 |

### Biến thể

Component đơn: không có trục biến thể, không có State. Cấu hình bằng Has Total và số dòng trong Slot Rows (1–8). Khung có ba mẫu:
Has Total bật (mặc định) · Has Total tắt · 1 dòng.

### Trạng thái

Không có — thẻ chỉ đọc, không bấm được nên không có Hover, Pressed, Focus, Selected. Màn đang tải dùng khung xương thay cả thẻ.

### Kích thước

| Trường hợp | Cao | Cách tính |
|---|---|---|
| Has Total bật, 3 dòng (mặc định) | 201 | 16 + 20 + 12 + 88 + 12 + 1 + 12 + 24 + 16 (lề · tiêu đề · phần · dòng · phần · kẻ · phần · dòng tổng · lề) |
| Has Total tắt, 3 dòng | 152 | 16 + 20 + 12 + 88 + 16 |
| Mỗi dòng thêm | +32 | 24 + 8 (`card/row-min-height` + `space/gap-sm`) |
| 8 dòng, Has Total bật | 361 | 201 + 5 × 32 |
| Vùng chạm | — | không bấm được |

Cao dòng 24 vì chữ 14/20 thấp hơn `card/row-min-height`.

### Nên và không nên

1. **Nên:** nhãn ngắn một dòng, giá trị canh phải cùng đơn vị, cùng cách viết số. **Không nên:** nhãn dài quá 120 bị cắt "…",
   người đọc không biết giá trị của gì.
2. **Nên:** tắt Has Total khi các dòng chỉ liệt kê, không cộng thành một tổng. **Không nên:** bật dòng tổng khi giá trị trên nó
   không cộng được (khác đơn vị, khác loại); dòng tổng phải là kết quả của các dòng.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | tiêu đề, giá trị, dòng tổng 17,73 · nhãn 5,43 (trên nền thẻ trắng) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | không có control; viền 1,13 trên nền xám và đường kẻ 1,25 là trang trí |
| 1.4.1 Dùng màu | ✓ | dòng tổng khác ở độ đậm và đường kẻ, không dựa vào màu |
| 1.3.1 Thông tin và quan hệ (A) | ✓ | khi code: danh sách mô tả (nhãn `dt`, giá trị `dd`) hoặc bảng 2 cột; dòng tổng đánh dấu rõ |
| 4.1.2 Tên, vai trò | ✓ | không bấm được nên không role button; vùng có tên bằng tiêu đề |
| 2.3.3 Chuyển động | ✓ | không chuyển động |
| Không áp dụng | — | 2.4.7, 2.4.13, 2.5.8, 2.1.1, 1.4.13: thẻ không nhận focus, không bấm |
| **Điểm web** | | **6/6 đạt** |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Rows | Slot, 1–8 | 3 × `.card / Row` (Label Value) | chỉ `.card / Row` (khoá) |
| Has Total | Bật tắt | bật | đường kẻ + dòng tổng |
| Instance lộ ra | panel | — | Heading (Title, Has Subtitle), Dòng tổng (Label, Value) |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Khung thẻ | `Base / Card` · L1 → xem [tài liệu Card](card.md) | State Default · Padding None · Elevation Low · Tone Surface | — (không lộ) |
| Tiêu đề | `.card / Heading` · L0 | Title một dòng; Has Subtitle tắt | Heading |
| Dòng | `.card / Row` · L0 | Type=Label Value; 1–8 dòng | Slot Rows |
| Đường kẻ | `.card / Divider` · L0 | cao `card/border-width` | Has Total |
| Dòng tổng | `.card / Row` · L0 | Type=Total | Dòng tổng · Has Total |

### Được dùng trong

Chưa có component cha dùng. Kiểm `findInstances` 20/10 trên trang DS · Components · L0–L3, bỏ instance trong khung tài liệu:
không component nào chứa Summary Card. Thẻ L2 (chi phí chuyến, tóm tắt lệnh trước khi gửi, đối soát) sẽ dựng trên khuôn này
khi vẽ màn.

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Lề thẻ | `layout/card-padding` | 16 |
| Giữa các phần | `space/gap-md` | 12 |
| Giữa các dòng | `space/gap-sm` | 8 |
| Bo thẻ (khung) | `radius/card` | 12 |
| Viền · kẻ | `card/border-width` | 1 |
| Dòng | `card/row-min-height` | 24 |
| Nhãn rộng tối đa | `card/row-label-max` | 120 |
| Nhãn – giá trị | `space/gap-lg` | 16 |
| Chữ | `type/heading` · `type/body` | 14/20 · 14/20 |
| Vùng chạm | `touch/min` | không áp (không bấm) |

Màu (một bộ cho web và app): nền `card/bg/default` → white · viền `card/border/default` → neutral/200 · đường kẻ
`color/border/default` → neutral/200 · tiêu đề, giá trị, dòng tổng `color/text/primary` → neutral/900 · nhãn
`color/text/secondary` → neutral/500.

Tên trong code: `<SummaryCard title total>` với slot `rows` gồm `<SummaryRow label value />`; biến CSS `--card-*`, `--radius-card`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6562:223644 ngày 20/10 (ngưỡng 1,1:1; ô mẫu nền `color/bg/canvas`, Context = Canvas).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 7 ô, 7 mẫu (khối Web; cả khung 14 ô, 14 mẫu) | luật A: 0 lỗi; không cờ B, C, D |
| Sát ngưỡng (lớp "Khung thẻ") | mọi ô | nền thẻ #FFFFFF trên nền ô #F2F4F7 = 1,10:1; hình giữ nhờ viền 1,13:1 |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Khi dùng, ráp trên Base / Card, thứ tự, Rows, Has Total, nhãn – giá trị, dòng tổng, chữ, rộng:** như web.
- **Khác web:** bo thẻ 16; chữ 15/22 (tiêu đề 15/20); không có State ở cả hai nền tảng.

### Cấu tạo

Hình phóng 2× trên Figma: như web, mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Khung thẻ | **Base / Card · State Default · Padding None · Elevation Low → xem tài liệu Card** | bo `radius/card` 16 |
| Khung nội dung | `layout/card-padding` · `space/gap-md` | 16 · 12 |
| Tiêu đề | `.card / Heading`: `type/heading` | 15/20 |
| Slot Rows · `.card / Row` | `space/gap-sm`; `card/row-min-height`; `type/body`; `card/row-label-max`; `space/gap-lg` | 8 · 24 · 15/22 · 120 · 16 |
| Đường kẻ | `.card / Divider`: `card/border-width` | 1 |
| Dòng tổng | `.card / Row` Type=Total: giá trị `type/heading` | 15/20 |

### Biến thể

Như web.

### Trạng thái

Không có (như web).

### Kích thước

| Trường hợp | Cao | Cách tính |
|---|---|---|
| Has Total bật, 3 dòng (mặc định) | 201 | 16 + 20 + 12 + 88 + 12 + 1 + 12 + 24 + 16 (chữ 15/22 vẫn thấp hơn dòng 24) |
| Has Total tắt, 3 dòng | 152 | 16 + 20 + 12 + 88 + 16 |
| Mỗi dòng thêm | +32 | 24 + 8 |
| 8 dòng, Has Total bật | 361 | 201 + 5 × 32 |
| Vùng chạm | — | không bấm được |

### Nên và không nên

Như web (cùng hai cặp).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | như web: 17,73 · nhãn 5,43 |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | không có control |
| 1.4.1 Dùng màu | ✓ | dòng tổng khác ở độ đậm và đường kẻ |
| 1.3.1 Thông tin và quan hệ (A) | ✓ | nhãn trợ năng đọc "nhãn: giá trị" theo cặp; dòng tổng đọc rõ là tổng |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng: không bấm được nên không role button; vùng có tên bằng tiêu đề |
| 2.3.3 Chuyển động | ✓ | không chuyển động |
| Không áp dụng | — | 2.4.7, 2.4.13, 2.5.8, 2.5.5, 2.1.1: thẻ không nhận focus, không bấm |
| **Điểm app** | | **6/6 đạt** |

### Thuộc tính

Như web (cùng bảng).

### Thành phần lồng

Như web (cùng bảng).

### Được dùng trong

Chưa có component cha dùng (như web).

### Token

Số đo (collection Platform, mode Mobile): lề `layout/card-padding` 16 · giữa phần `space/gap-md` 12 · giữa dòng `space/gap-sm` 8 ·
bo `radius/card` 16 · viền, kẻ `card/border-width` 1 · dòng `card/row-min-height` 24 · nhãn tối đa `card/row-label-max` 120 ·
nhãn – giá trị `space/gap-lg` 16 · chữ `type/heading` 15/20 · `type/body` 15/22. Màu như web.

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 7 ô, 7 mẫu (khối Mobile) | luật A: 0 lỗi; không cờ B, C, D |
| Sát ngưỡng (lớp "Khung thẻ") | mọi ô | nền thẻ #FFFFFF trên nền ô #F2F4F7 = 1,10:1; giữ hình nhờ viền 1,13:1 |

## Đối chiếu Astryx

Nguồn: `Card` (43:108295), trang Astryx · Library (chỉ đọc). Astryx không có thẻ tóm tắt riêng: Summary Card là khuôn Invlogis
(DEC-211) ráp trên khung `Base / Card` theo Astryx `Card` (DEC-234).

| | Astryx | DS v2 | Vì sao |
|---|---|---|---|
| Khớp | `Card`: khung nền + viền + bo + lề, Elevation, Slot `Content` | khung `Base / Card` State Default, Elevation Low | giữ cấu tạo khung |
| Lệch | Slot `Content` nhận mọi nội dung | nội dung cố định tiêu đề → Rows → kẻ → dòng tổng, con trực tiếp của thẻ | giữ Has Total và Slot Rows riêng |
| Lệch | không có hàng nhãn – giá trị dựng sẵn | `.card / Row` Label Value (nhãn tối đa 120, giá trị canh phải) và Type=Total | thẻ tóm tắt P3 đang có (DEC-211) |
| Lệch | thẻ có thể bấm (`ClickableCard`) | không State, chỉ đọc | bấm được thì dùng Record Card |

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần. Nền, viền, bóng nằm ở lớp "Khung thẻ" (đặt tuyệt
đối) nên bộ xuất không tự đọc được (README Mục 13); JSON đã làm sạch theo Khung thẻ trước khi sinh bảng.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Summary Card` (6442:85948) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Rows | Slot | — | nhận: .card / Row |
| Has Total | Bật tắt | bật | — |

Component đơn, không có trục biến thể.

### Màu theo phần (token)

| Nền | Viền | Chữ | Bóng |
|---|---|---|---|
| `card/bg/default` | `card/border/default` | `color/text/primary` | `elev/1` |

### Số đo theo phần (token)

| Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Khoảng giữa | Bo | Viền |
|---|---|---|---|---|---|---|---|---|
| 201 | 361 | `layout/card-padding` | `layout/card-padding` | `layout/card-padding` | `layout/card-padding` | `space/gap-md` | `radius/card` | `card/border-width` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Title | `type/heading` |
| Label | `type/body` |
| Value (.card / Row) | `type/body` |
| Value (Dòng tổng) | `type/heading` |

<!-- auto:end -->
