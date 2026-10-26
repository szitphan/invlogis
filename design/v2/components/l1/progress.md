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
---

# Base / Progress

> ⚠ Đã hạ cấp (DEC-254, 26/10): thanh là L0 `.progress / Bar`; nội dung file này sẽ gộp thành mục L0 trong
> `l1/progress-card.md` khi dựng `Base / Progress Card` (BL-240).

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Progress` (6520:212428, 24 biến thể, trang DS ·
> Components · L0–L3, Section `Progress · L1 · Component Base` 6507:212370), L0 `.progress / Segment` (6520:212400), `.progress / Gap`
> (6520:212403), khung tài liệu `Tài liệu · Progress` (6522:26020, khối Web 6522:26027, khối Mobile 6522:26049) · DEC-243 ·
> thiết kế riêng, Astryx không có (xem [Đối chiếu Astryx](#đối-chiếu-astryx))

Một component cho cả web và app, không có biến thể Platform: số đo giống nhau ở hai nền tảng, chỉ rộng mặc định khác (web
320, app 361), đọc từ collection Platform. Hai kiểu: **Bar** (một phần tô trên rãnh) và **Segmented** (chia đoạn, mỗi bước một
đoạn). Phần **Web** và phần **Mobile** dưới đây mỗi phần tự đứng được. Thanh không mang chữ: chữ đi kèm do component cha đặt.
Màu (collection Component, tiền tố `progress/`) giống nhau ở hai nền tảng.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Bar:** tỉ lệ hoàn thành của một việc biết trước (tải tệp, nhập nhiều bước). Value 0 → 100 bước 10, phần tô bo tròn; Tone
  chọn ở instance lồng Fill.
- **Segmented:** tiến độ nhiều bước theo nhóm trạng thái: mỗi bước một đoạn bằng nhau, các bước cùng nhóm liền nhau, giữa
  hai nhóm khe 2. Nhóm không có bước thì không thêm đoạn.
- **Tone:** Brand · Success · Info · Warning · Danger · Neutral; nghĩa từng Tone gán ở L2 (vd nhóm "xong" = Success).
- **Size:** MD 6 mặc định khi kéo ra · SM 4 cho thẻ gọn.
- **Cỡ web:** cao 6 · 4, bo tròn hẳn, khe nhóm 2; rộng mặc định 320 (đặt vào màn thì kéo Fill theo khung).
- **Chỉ có ở web:** không có gì riêng: thanh không tương tác nên không Hover, Focus, Disabled.
- **Chữ đi kèm:** "Xong x/y bước", chú giải số theo nhóm do component cha đặt; thanh không mang chữ.
- **Màu không phải cách duy nhất báo nhóm:** luôn kèm chữ (NFR-cross-process-flow-005).
- **Chưa làm:** đang tải không xác định (Indeterminate), vì chưa có nguồn nghiệp vụ.

### Cấu tạo

Hình phóng 2× trên Figma: Segmented MD (mẫu 4 · 2 · 1 đoạn, hai khe) và Bar MD Value 60. Nhãn đỏ: kích thước, bo · tím: khe ·
xanh: nội dung (màu); số đọc từ biến theo mode Web.

| Phần | Token | Giá trị web |
|---|---|---|
| Rãnh (khung của component) | `progress/height/sm · md`; bo `radius/chip`, cắt phần tràn; rộng `progress/width-default` | cao 4 · 6; tròn hẳn; rộng 320 |
| Nền rãnh (chỉ Bar) | `progress/bg/track` → `color/border/default` | #E3E6EC; Segmented không nền |
| Phần tô (Bar) | L0 `.progress / Segment` Shape=Round, Tone Brand mặc định; rộng = Value% (ràng buộc Scale khi kéo rộng); màu `progress/fill/{tone}` | cao = cao rãnh |
| Đoạn (Segmented) | L0 `.progress / Segment` Shape=Flat, mỗi bước một đoạn, Fill container; màu theo Tone | cao = cao rãnh |
| Khe giữa nhóm | L0 `.progress / Gap`, rộng `progress/gap`, trong suốt; chỉ đặt giữa hai nhóm, không đặt giữa các bước cùng nhóm | 2 |
| Màu theo Tone | `progress/fill/brand · success · info · warning · danger · neutral` | #262626 · #1B7542 · #1F4FB8 · #8A5300 · #B42318 · #495363 |

### Biến thể

Type × Size × Value (Value chỉ cho Bar). 24 biến thể = Bar 22 (Size 2 × Value 11) + Segmented 2. Tone của phần tô Bar chọn ở
instance lồng Fill (đưa ra panel), không nhân vào biến thể. Lưới trên Figma: Bar × Tone (Size MD, Value 60) · Bar × Value (0 ·
20 · 40 · 60 · 80 · 100, còn 10 · 30 · 50 · 70 · 90) · Segmented MD, SM (mẫu 4 Success · khe · 2 Info · khe · 1 Neutral; số
đoạn và Tone tự đặt trong Slot `Segments`).

### Trạng thái

Không có State: thanh không tương tác (không Hover, Focus, Disabled). Chỉ có giá trị hiện ra theo Value (Bar) và theo nhóm
đoạn (Segmented): Value 0 chưa bắt đầu · 50 đang làm · 100 xong, trên trắng `color/bg/surface`. Đang tải không xác định
(Indeterminate) chưa có nguồn nên chưa làm.

### Kích thước

Cao đọc từ `progress/height/*`, bo `radius/chip` tròn hẳn; web và app cùng số. Rộng mặc định 320, kéo Fill theo khung.

| Size | Cao | Bo | Dùng khi |
|---|---|---|---|
| SM | 4 | tròn hẳn | thẻ gọn, dòng chữ nhỏ |
| MD | 6 | tròn hẳn | mặc định; dòng quy trình, thẻ tóm tắt |

### Nên và không nên

1. **Nên:** Segmented cho tiến độ theo bước: nhóm cùng trạng thái liền nhau, kèm chữ "Xong x/y bước". **Không nên:** chỉ
   đưa thanh, không có chữ đi kèm: nhóm chỉ phân biệt bằng màu.
2. **Nên:** Bar cho việc biết trước tỉ lệ; Tone khớp nghĩa (Success khi xong, Danger khi lỗi). **Không nên:** chồng nhiều Bar
   cho cùng một việc: dùng một Bar kèm chữ.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.1 Không chỉ dùng màu (A) | ! | nhóm đoạn phân biệt bằng màu nên cha BẮT BUỘC kèm chữ (NFR-cross-process-flow-005) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | đoạn trên nền trắng: Brand 15,13 · Success 5,72 · Info 7,32 · Warning 6,33 · Danger 6,57 · Neutral 7,78. Bar: phần tô trên rãnh 4,58–12,10; rãnh trên nền trắng 1,25 (không mang thông tin, đọc nhờ phần tô) |
| 4.1.2 Tên, vai trò, giá trị (A) | ✓ | `role="progressbar"` + `aria-valuenow`, `aria-valuemin`, `aria-valuemax` + `aria-label`; Segmented đặt `aria-valuetext` = câu tóm tắt |
| 2.3.3 Chuyển động (AAA) | ✓ | không chuyển động; đổi giá trị không hoạt hình |
| 1.4.3 · 2.4.7 · 2.5.8 · 2.1.1 | — | không áp dụng: thanh không có chữ và không tương tác |
| **Điểm web** | | **4/4 đạt** (1 !: 1.4.1 phụ thuộc chữ cha) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Type | Biến thể | Bar | Bar · Segmented |
| Size | Biến thể | MD | SM 4 · MD 6 |
| Value | Biến thể | 50 | None · 0 · 10 … 100 (chỉ Bar; Segmented = None) |
| Segments | Slot | 4 Success · khe · 2 Info · khe · 1 Neutral | chỉ Segmented; preferred `.progress / Segment`, `.progress / Gap` |
| Fill | Instance lồng | Tone Brand | Tone: Brand · Success · Info · Warning · Danger · Neutral (chỉ Bar; không đổi Size, Shape ở panel) |

Không có thuộc tính chữ hay bật tắt: chữ đi kèm do cha đặt.

### Thành phần lồng

Lồng bằng instance của L0 thuộc họ progress; Slot `Segments` khoá preferred values (Segment, Gap). Không lồng L1 khác.

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Phần tô (Bar) | `.progress / Segment` · L0 | Shape=Round; Tone tự chọn | Tone (instance lồng Fill) |
| Đoạn (Segmented) | `.progress / Segment` · L0 | Shape=Flat; Tone tự chọn; số đoạn tự thêm | Slot `Segments` |
| Khe giữa nhóm | `.progress / Gap` · L0 | chỉ đặt giữa hai nhóm | Slot `Segments` |

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components · L0–L3 (không tính khung tài liệu): chưa có component cha dùng. Dự kiến dùng ở
L2 quy trình liên phòng (thẻ quy trình trên màn chi tiết: Segmented · MD 6 rộng cố định cạnh chữ; thẻ tóm tắt quy trình:
Segmented · MD 6 · Fill khung); L2 chưa dựng.

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Cao rãnh · SM | `progress/height/sm` | 4 |
| Cao rãnh · MD | `progress/height/md` | 6 |
| Bo | `radius/chip` | tròn hẳn |
| Khe giữa nhóm | `progress/gap` | 2 |
| Rộng mặc định | `progress/width-default` | 320 |
| Rộng đoạn đặt tự do | `progress/segment-width` | 24 (trong thanh đoạn luôn Fill) |
| Cao đoạn, phần tô | = cao rãnh theo Size | SM 4 · MD 6 |
| Phần tô Bar | rộng = Value% rãnh | ràng buộc Scale |

Màu (collection Component, tiền tố `progress/`; một bộ cho web và app; Brand theo dải màu khách, DEC-167):

| Phần | Token | Trỏ tới · mã |
|---|---|---|
| Rãnh | `bg/track` | `color/border/default` → neutral/200 · #E3E6EC |
| Brand | `fill/brand` | `color/brand/800` → than chì · #262626 |
| Success | `fill/success` | `color/status/success-text` → green/700 · #1B7542 |
| Info | `fill/info` | `color/status/info-text` → blue/700 · #1F4FB8 |
| Warning | `fill/warning` | `color/status/warning-text` → yellow/700 · #8A5300 |
| Danger | `fill/danger` | `color/status/danger-text` → red/700 · #B42318 |
| Neutral | `fill/neutral` | `color/chip/gray/fg` → neutral/600 · #495363 |

Code: biến CSS `--progress-height-*`, `--progress-gap`, `--progress-width-default`, `--progress-fill-*`, `--progress-bg-track`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6522:26020 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền trắng).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 31 ô, 32 mẫu (khối Web) | luật A: 0 lỗi, ô nào cũng có nền trắng `color/bg/surface` và viền mảnh |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có, 0 cờ |
| Lớp con (lớp "Đoạn · Success") | 12 mẫu | 0 cờ; sát ngưỡng: không có |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Bar, Segmented, Tone, Size, Chữ đi kèm, Màu, Chưa làm:** như phần Web.
- **Cỡ app:** cao 6 · 4, bo tròn hẳn, khe nhóm 2; rộng mặc định 361 (đặt vào màn thì kéo Fill theo khung).
- **Khác web:** rộng mặc định 361 = 393 − 2 × 16; số đo giống web; app không dùng Hover. Thẻ quy trình dùng SM 4 rộng cố
  định (84) cạnh chữ, thẻ tóm tắt trong sheet dùng MD 6 rộng hết khung.

### Cấu tạo

Hình phóng 2× như phần Web, số đọc từ biến theo mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Rãnh (khung của component) | `progress/height/sm · md`; bo `radius/chip`; rộng `progress/width-default` | cao 4 · 6; tròn hẳn; rộng 361 |
| Nền rãnh (chỉ Bar) | `progress/bg/track` → `color/border/default` | #E3E6EC; Segmented không nền |
| Phần tô, đoạn, khe, màu theo Tone | như phần Web | khe `progress/gap` 2 |

### Biến thể

Như web; 24 biến thể dùng chung.

### Trạng thái

Như web: không có State; app không dùng Hover.

### Kích thước

| Size | Cao | Bo | Dùng khi |
|---|---|---|---|
| SM | 4 | tròn hẳn | thẻ quy trình trên màn chi tiết, rộng cố định cạnh chữ |
| MD | 6 | tròn hẳn | mặc định; thẻ tóm tắt trong sheet, Fill hết khung |

Rộng mặc định 361, kéo Fill theo khung.

### Nên và không nên

1. **Nên:** Segmented kèm chữ "Xong x/y bước". **Không nên:** chỉ đưa thanh, nhóm chỉ phân biệt bằng màu.
2. **Nên:** Bar cho việc biết trước tỉ lệ; Tone khớp nghĩa. **Không nên:** chồng nhiều Bar cho cùng một việc.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.1 Không chỉ dùng màu (A) | ! | nhóm đoạn phân biệt bằng màu nên cha BẮT BUỘC kèm chữ (NFR-cross-process-flow-005) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | như web: đoạn trên nền trắng 5,72–15,13; rãnh 1,25 (không mang thông tin) |
| 4.1.2 Tên, vai trò, giá trị (A) | ✓ | nhãn trợ năng + giá trị (now, min, max); Segmented đọc câu tóm tắt |
| 2.3.3 Chuyển động (AAA) | ✓ | không chuyển động; đổi giá trị không hoạt hình |
| 1.4.3 · 2.4.7 · 2.5.5 · 2.5.8 · 2.1.1 | — | không áp dụng: thanh không có chữ và không tương tác |
| **Điểm app** | | **4/4 đạt** (1 !: 1.4.1 phụ thuộc chữ cha) |

### Thuộc tính

Như web (cùng bảng).

### Thành phần lồng

Như web (cùng bảng).

### Được dùng trong

Chưa có component cha dùng (kiểm 20/10). Dự kiến: L2 thẻ quy trình (Segmented · SM 4, rộng cố định 84 cạnh chữ) và thẻ tóm
tắt quy trình (Segmented · MD 6, Fill khung); chưa dựng.

### Token

Số đo (collection Platform, mode Mobile): cao rãnh `progress/height/sm` 4 · `progress/height/md` 6 · bo `radius/chip` tròn hẳn ·
khe `progress/gap` 2 · rộng mặc định `progress/width-default` 361 · đoạn đặt tự do `progress/segment-width` 24. Màu: như phần
Web (một bộ). Code: cùng biến CSS với web.

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 31 ô, 32 mẫu (khối Mobile) | luật A: 0 lỗi |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có, 0 cờ |

## Đối chiếu Astryx

Astryx không có Progress hay ProgressBar; chỉ có thanh 4px trong Stepper (5055:30816). Base / Progress là thiết kế riêng theo
token DS v2 (màu đoạn dùng token, không giữ mã màu hex của mẫu cũ).

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Progress` (6520:212428) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Segments | Slot | — | nhận: .progress / Segment · .progress / Gap |
| Type | Biến thể | Bar | Bar · Segmented |
| Size | Biến thể | MD | MD · SM |
| Value | Biến thể | 50 | 50 · 0 · 10 · 20 · 30 · 40 · 60 · 70 · 80 · 90 · 100 · None |

24 biến thể · trục Type × Size × Value.

### Màu theo phần (token)

| Type | Nền |
|---|---|
| Bar | `progress/bg/track` |
| Segmented | trong suốt |

### Số đo theo phần (token)

| Size | Cao | Rộng | Bo |
|---|---|---|---|
| MD | `progress/height/md` | `progress/width-default` | `radius/chip` |
| SM | `progress/height/sm` | `progress/width-default` | `radius/chip` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|

<!-- auto:end -->
