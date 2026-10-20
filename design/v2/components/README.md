---
type: design-component-guide
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
  - _scripts/check-mat-hinh.js
  - _scripts/ds-v2-component-doc.py
  - _scripts/figma-component-export.js
---

# Khuôn tài liệu component DS v2

> Khuôn cho tài liệu của mọi component L1 (và L2 về sau): một khung `Tài liệu · {Tên}` trên Figma + một md, Web | Mobile
> dàn ngang. User duyệt 20/10/2026. Mẫu đã duyệt: `Base / Button` ([l1/button.md](l1/button.md) và khung
> `Tài liệu · Button` trong Section `Button · Tài liệu`, trang `DS · Components · L0–L3`, file `FifpyOMpZk9OP8qyNzbRVJ`).
> Quyết định: DEC-245 (khuôn), DEC-233 (luật lồng), DEC-241 (Context).
> Căn cứ: [architecture.md](../architecture.md) Mục 4 (luật lắp), Mục 9 (DEC-118, DEC-183). Skill `/figma-component` đọc file này.

Áp cho component khác: làm đúng thứ tự dưới đây, không hỏi lại trừ mục "Hỏi user khi" ở cuối.

## 1. Đặt khung

- Khung nằm trong Section `{Tên} · Tài liệu` của hàng component trên trang ma trận, cột Tài liệu (đọc x của Section hiện
  có, không tự dời cột).
- Thay khung tài liệu có sẵn: dựng khung mới tên `Tài liệu · {Tên}` (vd `Tài liệu · Button`), tạm đặt cạnh khung cũ; xong
  và kiểm máy đạt thì xoá khung cũ (trước khi xoá kiểm: không có component chính nằm trong khung cũ, không có prototype /
  hyperlink trỏ vào), đưa khung mới về (80, 80) trong Section, thu Section vừa khung: rộng = 80 + rộng khung + 80, cao =
  80 + cao khung + 80, đỉnh Section bằng đỉnh các Section cùng hàng.
- KHÔNG nới cao lấn hàng dưới (khoảng giữa hai hàng 240). Quá cao thì rút ô, cắt hình minh hoạ (Mục 8), không đẩy hàng dưới.
- Không đụng hàng khác, không đổi component.

## 2. Kích thước và nền

| Lớp | Bố cục | Rộng | Lề trong | Khoảng | Nền | Viền | Bo |
|---|---|---|---|---|---|---|---|
| Khung | dọc | 4256 (= 64·2 + 2040·2 + 48) | 64 | 40 | `color/bg/surface` | `color/border/default` 1 | 24 |
| Hàng hai khối | ngang | đầy | 0 | 48 | không | không | — |
| Khối Web / Mobile | dọc, đặt mode Platform = Web / Mobile (explicit variable mode của khối) | 2040 | 40 | 44 | `color/bg/surface` (trắng; user chốt 20/10) | `color/border/default` 1 (tách hai khối) | 24 |

Khung và hai khối đều nền trắng. Ranh giới ô mẫu trên nền trắng nhờ viền mảnh của ô (Mục 4), không nhờ nền khối.

- Đầu khung: dòng nhỏ `L1 · BASE · TÀI LIỆU COMPONENT` (Inter Semi Bold 12, `color/text/secondary`) · tên (Cal Sans
  Regular 48, `color/text/primary`) · dòng meta (Inter 16/24: phiên bản, trạng thái, người phụ trách, ID Figma, DEC, đường
  dẫn md) · 1 câu giới thiệu (Inter 16/24, `color/text/primary`): một component hay hai, khối nào đặt mode nào, luật nền ô.
- Đầu khối: tên nền tảng (Inter Semi Bold 32/40) + chip `Platform = Web|Mobile` (nền `color/bg/surface`, viền
  `color/border/strong`, bo 999, lề 4 × 12, chữ Semi Bold 13) + 1 câu nêu điểm khác của nền tảng (Inter 15/22).
- Chữ tài liệu: Inter, KHÔNG gắn biến cỡ chữ Platform (để chữ tài liệu không đổi theo mode). Màu chữ gắn biến Semantic:
  tiêu đề `color/text/primary`, chữ thường `color/text/secondary`, chữ trong bảng `color/icon/primary`.
- Tiêu đề mục: Inter Semi Bold 22/28; câu dưới tiêu đề Inter 14/20; khoảng trong mục 16.

## 3. Lưới bên trong khối

Rộng nội dung 1960 = 3 cột × 620 + 2 khoảng × 50. "Đôi" = 1290 (2 cột + 1 khoảng). Mỗi hàng là frame ngang
`Hàng · A | B`, khoảng 50, các mục rộng cố định.

| Hàng | Nội dung | Cột |
|---|---|---|
| R1 | Tổng quan | đủ rộng, chia 3 cột chữ 620: (a) các kiểu/biến thể chính · (b) Content, cỡ của nền tảng, "Chỉ có ở web" / "Khác web" · (c) luật chung (thứ tự, chữ, hành vi) |
| R2 | Cấu tạo | đủ rộng: hình phóng 780 × 372 + danh sách phần 3 cột |
| R3 | Biến thể · Kích thước | đôi · cột 3 |
| R4 | Trạng thái · Nên và không nên | đôi · cột 3 |
| R5 | Thuộc tính · Token số đo · Token màu | 3 cột |
| R6 | Trợ năng · Được dùng trong · Thành phần lồng | 3 cột |

**Ô Cấu tạo của component rộng.** Component có bề rộng mẫu lớn hơn 360 (thẻ Record Card, Summary Card trên lưới 620) thì mục
**Cấu tạo** (R2) chiếm **hai cột = 1290**, không dùng ô 780 × 372 mặc định: ô hình phóng rộng 1290, danh sách phần chuyển sang
cột còn lại của hàng hoặc xuống dưới hình theo 3 cột. Hình phóng vẫn `rescale(2)` sau khi đặt chữ, nhãn xếp tầng theo Mục 5, đủ
chỗ cho các nhãn mọc sang hai phía. Component rộng ≤ 360 giữ ô 780 × 372. Lý do: thẻ 361 phóng 2× là 722, cộng hai tầng nhãn mỗi
phía vượt 780; ô hẹp làm nhãn đè nhau hoặc bị cắt (Record Card, ô 1290 × 904 mobile và web).

Mục không áp dụng cho component (vd không có Nên/không nên) → giữ ô cột, 1 dòng "Không có — {lý do}". Mục quá dài so
với hàng → đổi chỗ giữa các ô cột 3 cho cân hàng, giữ thứ tự đọc trái → phải, trên → dưới. Md theo đúng thứ tự này.

Web và Mobile có CÙNG bộ mục, cùng vị trí; nội dung khác đúng chỗ khác (cỡ, vùng chạm, Hover, Tooltip, số trợ năng).
Mobile bỏ cột Hover ở lưới Trạng thái và bảng màu, ghi 1 câu "app không dùng Hover".

Component chỉ dùng ở một nền tảng: khung chỉ một khối (vd `Base / OTP Field`: khối Mobile), md vẫn có hai phần, phần nền tảng
không dùng ghi ngắn lý do và token để dành; component chỉ web (`Base / Tooltip`) có khối Mobile ngắn nói nội dung đi đâu trên app.

## 4. Luật nền ô mẫu (chống mất hình)

- Mọi hình component mẫu (biến thể, trạng thái, kích thước, cảnh nên/không nên, hình "được dùng trong") nằm trong một
  **ô mẫu**: FRAME tên bắt đầu `Ô mẫu · ` (vd `Ô mẫu · Primary · Hover`, `Ô mẫu · Biến thể · Ghost · Label`,
  `Ô mẫu · Kích thước · Primary · Label · SM`, `Ô mẫu · Cảnh · Nên`).
- Ô mẫu có **nền thật nơi component sống** + LUÔN có viền 1 `color/border/default` + bo 12, canh giữa,
  `clipsContent = false` (để vòng focus không bị cắt). Nền ô KHÔNG bao giờ trong suốt (không "mượn" nền khối). Ô nền
  trắng trên khối trắng vẫn giữ viền để thấy ranh giới; ô nền xám (vd Outline) vẫn nền xám.
- Thẻ Nên / Không nên không có nền (viền xanh / đỏ 2); cảnh bên trong là ô mẫu nền thật có viền.
- Bảng nền thật (thêm dòng khi gặp component mới, lấy từ mục "Khi dùng" của md):

| Component / kiểu | Nền ô |
|---|---|
| Mặc định (nút, chip, ô nhập web, dòng, thẻ trong sheet) | `color/bg/surface` (trắng) |
| Button Outline ("nút phụ trên nền xám") | `color/bg/canvas` (#F2F4F7) |
| Thẻ đặt trên nền màn app | `color/bg/canvas` |
| Thẻ Surface, Dashed, Record Card, Summary Card (Web và Mobile) | `color/bg/canvas`, Context = Canvas |
| Thẻ Muted, Selectable Card | `color/bg/surface` |
| Ô nhập app (`field/bg/app` xám) | `color/bg/surface` |

- **Ô mẫu của thẻ** (mọi component ráp trên Base / Card: Card, Selectable, Record, Summary, Status Row khi cảnh có thẻ) có nền
  `color/bg/canvas` cả **Web và Mobile**, đặt Variable mode `Context = Canvas` cho ô, không chỉ ở Mobile. Ngoại lệ: thẻ Muted và
  thẻ chọn một (Selectable) đặt trên nền trắng `color/bg/surface` (Muted mất ranh giới trên nền xám). Lý do: thẻ trắng đặt trên
  nền màn xám cả ở web lẫn app; đặt ô trắng thì không chứng minh được ranh giới thẻ (1,10:1 trên xám) và khe vòng focus
  (`focus/gap`) không theo Context.
- Cỡ ô: đều nhau trong một lưới. Cao ô = cao mẫu lớn nhất + 2 × 12 (Button MD: web 56, app 66; lưới Kích thước:
  web 56, app 76). Ô trống (tổ hợp không có) tên `Ô trống · …`, không nền, viền chấm 4/4, chữ "không có" 12
  `color/text/tertiary`.
- Đầu cột: tên Semi Bold 13 + ghi chú nền ô 11/14 (vd "trên xám bg/canvas"); `primaryAxisSizingMode = AUTO` (không thì
  ghi chú bị cắt). Đầu hàng rộng 110 (lưới Kích thước 96).
- Mobile: mẫu thấp hơn `touch/min` thì bọc trong khung `Vùng chạm · touch/min` viền chấm tím 3/3, ngoài nút, bo tròn,
  rộng = max(rộng nút, 44), cao 44.
- **Nền xám → mode Context** (collection `Context`: Surface | Canvas): khung hoặc ô nền xám (`color/bg/canvas`) đặt
  Variable mode Context = Canvas; nền trắng (`color/bg/surface`) giữ mặc định Surface. Khe vòng focus (`focus/gap`) và ruột
  nút Outline / Ghost khi Focus tự theo nền; thẻ trắng nằm trên nền xám đã tự đặt lại Surface cho nút bên trong (Slot
  Content và Footer), không cần làm gì thêm. Tài liệu component có vòng focus ghi: "khe focus theo `focus/gap`, đặt
  Context=Canvas khi nằm trên nền xám".

## 5. Mẫu Cấu tạo (bắt buộc; mẫu: mục Cấu tạo của khung `Tài liệu · Button`)

- Ô hình phóng 780 × 372: nền thật (`color/bg/surface`), viền 1, bo 16, không auto layout. Instance mẫu mặc định
  (thường MD · Default, Content giàu phần nhất) tạo trong ô RỒI phóng 2× (`rescale(2)`, sau khi đặt override chữ). Đặt
  x = 150, y = 150.
- Nhãn số: khung ngang lề 2 × 6, bo 4, chữ Inter Semi Bold 11/14 trắng. Nội dung `{phần} · {token} = {số theo mode}`
  (vd `cao · control/height/md = 32`; bo tròn ghi `tròn hẳn (9999)`).
- Màu nhãn và đường kẻ (cùng màu, nét 1):

| Màu | Hex | Dùng cho |
|---|---|---|
| Đỏ | #E5484D | kích thước (cao, rộng), bo |
| Tím | #7C3AED | lề, khoảng cách, viền, vùng chạm |
| Xanh | #2563EB | nội dung: icon, chữ (text style, màu chữ) |
| Xám đậm | #374050 | component L1 lồng: `Base / X · cỡ · kiểu → xem tài liệu X` — KHÔNG ghi token của nó (Mục 8, luật g) |

- Đường kẻ: từ nhãn thẳng đứng tới phần. Lề và khoảng: thước ngang đúng bề rộng (nét 1 + 2 vạch đầu cao 7) đặt sát mép
  trên/dưới mẫu, đường kẻ đi từ giữa thước. Cao: thước đứng cách mép phải 16, nhãn bên phải. Bo: đường kẻ tới điểm 45°
  của góc (x = phải − r(1 − 0,707), y = trên + r(1 − 0,707)).
- Xếp tầng nhãn không cắt nhau: nhãn mọc sang phải từ đường kẻ của nó; trên và dưới mỗi phía 3 tầng cách 36; đích càng
  bên phải thì tầng càng gần mẫu. Không tô màu đè lên mẫu (làm sai hình đã duyệt).
- Danh sách phần bên phải: 3 cột, mỗi phần tiêu đề Semi Bold 14/20 + 1–3 dòng 13/18: token + số theo mode. Phần là L1
  lồng thì chỉ ghi `Base / X · cỡ · kiểu → xem tài liệu X` + cách bật (thuộc tính nào). Câu dưới tiêu đề mục nói rõ mẫu
  nào phóng, nghĩa các màu nhãn, "số đọc từ biến theo mode {Web|Mobile}".

## 6. Bảng

- Khung dọc nền `color/bg/surface`, viền 1 `color/border/default`, bo 12, `clipsContent = true`. Hàng đầu nền
  `color/bg/canvas`, chữ Semi Bold 13; hàng sau viền trên 1. Ô lề 8–9 × 10–12. Cột đầu Medium 13, cột khác 12–13/18,
  màu `color/icon/primary`. Tổng rộng cột = rộng mục (620 hoặc 1290).
- Cột kết quả trợ năng: ✓ `color/status/success-fg`, ✕ `color/status/danger-fg`, ! `color/status/warning-fg`.
- Bảng màu: mỗi ô có mẫu màu 14 × 14 (bo 4, viền `color/border/strong`, fill gắn chính biến đó) + tên token bỏ tiền tố
  component; không nền → ô mẫu viền chấm + "không nền".

## 7. Số liệu — chỉ đọc từ biến

- Mọi con số in ra đọc từ giá trị của biến theo mode của khối đã đặt (cách đọc: Mục 11), không gõ tay, không lấy từ trí nhớ.
- Bảng Token · số đo: cột SM · MD · LG (hoặc trục cỡ của component), dòng: cao, lề, lề phía icon, khoảng, cỡ icon, bo,
  chữ (cỡ/dòng, nét), vòng focus, vùng chạm (`touch/min`, ghi "+n/phía" khi thiếu).
- Màu lấy từ collection Component, ghi một lần "một bộ màu cho web và app" nếu không có mode màu theo nền tảng.
- Trợ năng: tương phản tính bằng công thức WCAG trên mã màu token; giữ số đã chấm trong md cũ nếu màu không đổi. Mỗi
  khối chỉ chấm tiêu chí áp cho nền tảng, điểm ghi riêng "Điểm web: n/m", "Điểm app: n/m" (! = đạt có điều kiện, tính
  là đạt):
  - Web: 1.4.3 (+ ngoại lệ Disabled), 1.4.11, 2.4.7 · 2.4.13, 2.5.8 (≥ 24), 4.1.2 (`aria-label`, `aria-busy`), 2.1.1
    (Enter, Space, thứ tự Tab), 1.4.13 nếu có tooltip/nội dung hiện khi rê, 2.3.3. Không chấm 2.5.5.
  - Mobile (user chấp nhận 20/10): 1.4.3 (+ ngoại lệ), 1.4.11, 2.4.7 · 2.4.13 ghi "focus khi có bàn phím ngoài hoặc công
    cụ trợ năng", 2.5.8, 2.5.5 (≥ 44: thiếu thì "!" + code thêm vùng chạm vô hình), 4.1.2 ghi "nhãn trợ năng (như
    aria-label)", 2.1.1 ghi "khi có bàn phím ngoài: Enter, Space; theo thứ tự focus", 2.3.3. Không chấm 1.4.13 khi app
    không có tooltip. Trạng thái Focus của app mô tả "khi điều hướng bằng bàn phím ngoài hoặc trợ năng".

## 8. Luật lồng, Thành phần lồng và Được dùng trong

### Luật lồng

Nguồn: user chốt 20/10, ghi ở DEC-233 (sửa DEC-213 thành "L1 ráp từ L0 và L1 khác").
[architecture.md](../architecture.md) Mục 4 "Luật lắp" mới có dòng "L1 chứa L0 của mình, L1 khác, icon"; bảy luật a–g dưới đây là
phần chi tiết, áp cho mọi component:

| | Luật |
|---|---|
| a | Tầng theo vai trò, không theo chỗ dùng: component dùng riêng được (Button, Status Chip, Avatar, Tooltip, Text Field) luôn là L1, kể cả khi nằm trong component khác. L0 chỉ cho phần không dùng riêng và thuộc một họ |
| b | Lồng bằng instance của component gốc (`Base / Button`…), không sao chép, không tạo bản `.card / Button` |
| c | L0 KHÔNG BAO GIỜ chứa L1. Vùng chứa L1 trong component cha là Slot của chính L1 cha (vd chân thẻ = Slot `Footer` của Record Card, canh phải, cách 8, preferred values = Base / Button) |
| d | Cha khoá cấu hình được phép bằng preferred values (Slot / instance swap) và đưa thuộc tính của instance lồng ra panel (expose nested instance); ghi cấu hình được phép trong tài liệu cha (bảng Thành phần lồng, dưới) |
| e | Token của component lồng giữ nguyên; cha chỉ quyết khoảng cách quanh nó. Cần cỡ mới → thêm biến thể ở component gốc, không ghi đè |
| f | Phụ thuộc một chiều, không vòng: L0 → L1 → L2; L1 được chứa L1 khác |
| g | Ma trận: hàng của cha có dòng "Dùng lại: …" trỏ sang hàng component gốc, không vẽ lại. Tài liệu cha, mục Cấu tạo: nhãn chỉ vào phần lồng ghi `Base / Button · SM · Secondary → xem tài liệu Button`, không lặp token của nó |

### Thành phần lồng

- Bảng `Phần | Component · tầng | Cấu hình được phép | Đưa ra panel`. Liệt kê L0 lồng, icon (instance swap), L1 lồng
  (ghi `Base / X · L1 → xem tài liệu X`, không lặp token). Cấu hình được phép lấy từ preferred values, biến thể đang
  dùng; "Đưa ra panel" = thuộc tính của component + instance lồng có `isExposedInstance = true`.

### Được dùng trong

- Tìm trên trang ma trận mọi instance có `mainComponent.parent.id = {set}`; với mỗi instance lấy component cha
  (COMPONENT / COMPONENT_SET gần nhất), chỗ đặt (tên Slot / lớp), cấu hình (biến thể, chữ). Đọc thêm
  `componentPropertyDefinitions` của cha: Slot / instance swap có preferred value là component này cũng ghi. Bảng
  `Component cha | Chỗ đặt | Cấu hình dùng`, số cỡ theo mode của khối. Không có cha nào → "Chưa có component cha dùng".
- Hình minh hoạ: instance cha đặt trong ô mẫu nền thật của cha (thẻ: `color/bg/canvas`), cắt (`clipsContent`) chỉ còn
  vùng chứa component này, nhãn xám đậm `Base / X · cỡ · kiểu → tài liệu này` + câu cha quyết gì (canh, khoảng cách).
- Instance trong khung tài liệu không tính là "được dùng" (lọc bỏ instance nằm trong frame tên `Tài liệu · …`).
- Chỉ ghi component cha còn tồn tại; cha đã xoá (vd 4 kiểu dòng của hàng List Row, xoá 20/10) thì bỏ dòng. Không ghi
  "Dùng ở đâu" theo màn mẫu khi chưa kiểm trên Figma.

## 9. Kiểm máy "mất hình" (bắt buộc trước khi chụp ảnh trình)

Script: [`_scripts/check-mat-hinh.js`](../../../_scripts/check-mat-hinh.js) (chỉ đọc, không sửa node).

- **Cách chạy:** đọc file, thay `__FRAME_ID__` (dòng `const FRAME_ID`) bằng ID khung `Tài liệu · {Tên}`, gửi toàn văn làm
  `code`. Script viết bằng Plugin API gốc (`getNodeByIdAsync`, `setCurrentPageAsync`, `variables…resolveForConsumer`,
  `findAll`): chạy qua `figma_write` nếu proxy hỗ trợ các hàm đó (thử trước bằng một lệnh đọc nhỏ), không được thì
  `use_figma` (chỉ đọc). Ghi vào báo cáo đường nào đã dùng.
- **Nhận diện:** khối qua tên `Khối · Web` / `Khối · Mobile`, ô qua tiền tố `Ô mẫu · `. Mẫu = instance nằm trong ô mà giữa
  nó và ô không có instance nào khác.
- **Đầu ra:** `{ soO, soMau, soCo, co[], satNguong[], soCoLopCon, coLopCon[], satNguongLopCon[], tomTatLop, bang[] }`.
  Mỗi cờ `{ khoi, o, luat, muc, loi }`; `bang[]` là mọi mẫu kèm nền ô, nền thân, tương phản, viền, khe và vòng focus.

Luật, ngưỡng 1,1:1 tương phản WCAG:

| Luật | Kiểm | Cờ |
|---|---|---|
| A | Ô mẫu có nền riêng, khác nền khối hoặc có viền | ✕ lỗi khung → sửa khung |
| B | Nền thân mẫu so với nền ô < 1,1 | ✕ MẤT HÌNH nếu không còn viền ≥ 1,1 và không có vòng focus ≥ 3; ⚠ NỀN CHÌM nếu viền/vòng còn giữ hình. Thân không fill (Ghost, Outline) → "không nền", không cờ |
| C | Khe vòng focus (bóng lan nhỏ nhất) khác nền ô (> 1,01) | ✕ KHE LỘ |
| D | Cùng lưới, cùng Type: Hover / Pressed so với Default < 1,1 | ✕ GIỐNG DEFAULT |

- **Lớp con:** mẫu mà lớp ngoài không có nền (Tooltip: nền ở lớp `Bóng`; Text Field: nền ở khung `Field`) → script đo thêm
  lớp con ĐẦU TIÊN (thứ tự cây, bỏ chữ / vector / lớp ẩn) có nền SOLID. Cờ B và D của lớp con nằm ở `coLopCon[]` (tách
  khỏi `co[]`), sát ngưỡng ở `satNguongLopCon[]`, `tomTatLop` đếm mẫu theo lớp đo. Ghi trong md dạng "⚠ Nền chìm (lớp
  "{tên lớp}")".
- Lỗi luật A là lỗi khung: sửa ngay, chạy lại tới khi A = 0. Cờ B–D trên nền thật là sự thật của component: KHÔNG sửa
  component, KHÔNG đổi nền ô cho đẹp, tài liệu giữ nguyên hình hiện tại; ghi vào báo cáo "Cần user quyết".
- **Không đặt hộp kết quả kiểm máy trên Figma** (user chốt 20/10). Kết quả ghi trong md: mục `### Kiểm máy` ở CUỐI mỗi
  phần `## Web` và `## Mobile` — bảng `Mức | Ô mẫu | Kết quả` gồm dòng Khung (số ô, số mẫu, số lỗi A), từng cờ ✕ / ⚠
  của nền tảng đó (cả lớp ngoài và lớp con), và dòng "Sát ngưỡng" (1,10–1,15). Mẫu: [l1/button.md](l1/button.md).

## 10. Md (`design/v2/components/l1/{tên}.md`)

```
frontmatter (type, status, updated, links)
# Base / {Tên}
> L1 · phiên bản · trạng thái · người phụ trách · Figma set ID · khung tài liệu ID · DEC
1 đoạn: một component hay hai, mode Platform, màu chung
## Web
> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.
### Tổng quan · ### Cấu tạo (bảng Phần | Token | Giá trị) · ### Biến thể · ### Trạng thái · ### Kích thước
### Nên và không nên · ### Trợ năng — chấm theo WCAG 2.2 · ### Thuộc tính · ### Thành phần lồng · ### Được dùng trong
### Token (số đo theo mode; màu trỏ Phần máy; tên trong code)
### Kiểm máy (kết quả check-mat-hinh.js cho khối Web)
## Mobile
(đúng các mục như Web, số mode Mobile, kết thúc bằng ### Kiểm máy của khối Mobile)
## Phần máy (chung Web và Mobile)
<!-- auto:begin --> … <!-- auto:end -->   ← _scripts/ds-v2-component-doc.py
```

- Component có HAI component riêng cho web và app (vd Text Field / Text Field / Mobile): vẫn một md, phần Web tả
  component web, phần Mobile tả component app. Phần máy: dùng hai khối `auto:` có tên nếu `_scripts/ds-v2-component-doc.py`
  đã nhận (đọc docstring đầu script); chưa nhận thì giữ md riêng cho bản app như cũ, phần `## Mobile` trỏ sang.
- Chữ mẫu L1 trung tính (Lưu, Huỷ, Xoá, Thêm, Title, Value…), không có lệnh, chuyến, xe.
- Mục "Đối chiếu Astryx" chỉ ghi trong md, không đặt trên khung Figma (khung tài liệu và dòng Meta không nhắc Astryx).
- Frontmatter theo mẫu các md cùng thư mục: `type: design-component`, `status`, `updated`, `links`. Không `changelog`;
  lịch sử đổi ở `_workspace/changelog.md`.

## 11. Cách dựng (Figma)

**Đường chính là `figma_write` (reqwise)**; `use_figma` (Figma chính thức) chỉ khi proxy không làm được việc đó (vd đặt nội
dung vào Slot bằng `appendChild`, đọc giá trị biến theo mode nếu proxy chưa trả) và mỗi lần dùng ghi lý do vào báo cáo.
Trước lần ghi đầu của phiên đọc `figma_docs(section="api", level="cheat")` và `figma_docs(section="recipes")`; quy trình
chung và các bẫy của proxy nằm ở skill `/figma-component`, không chép lại đây.

- Mỗi lần gọi dựng 1–2 hàng cho CẢ HAI khối (vòng lặp qua `Web` / `Mobile`); đầu script xoá mục cùng tên để chạy lại an toàn.
- Bộ hàm dùng chung đầu mỗi lần gọi: bảng biến theo tên (collection Semantic, Platform, Component, Primitives, Context), gắn
  màu / số theo tên biến (không mã hex trần ngoài màu nhãn Mục 5); hàm tạo auto layout (nền, viền, lề, khoảng, bo gắn biến);
  hàm tạo chữ (Inter, kiểu và màu gắn biến, rộng cố định + tự cao khi cần); hàm tạo ô mẫu (Mục 4).
- Đặt mode cho khối: đặt explicit variable mode `Platform` = Web / Mobile cho khung khối (và `Context` = Canvas cho khung /
  ô nền xám), tạo con SAU khi đã đặt mode.
- Đọc số theo mode của khối từ giá trị biến; không gõ tay (Mục 7).
- Lưu ý đã gặp: tạo instance trong khối (đã có mode) rồi mới đọc rộng / cao; phóng 2× (`rescale`) sau khi đặt chữ; `resize`
  đặt lại sizing nên gọi trước khi đặt `primaryAxisSizingMode = 'AUTO'`; ô có vòng focus phải `clipsContent = false`.
- Tham khảo cách dựng: đọc khung `Tài liệu · Button` bằng `figma_read`; tên lớp đã theo quy ước trên.

## 12. Trình duyệt

1. Chạy kiểm máy (Mục 9) sau lần sửa cuối, A = 0.
2. Chụp: toàn khung, cận Cấu tạo (mỗi khối), cận lưới Trạng thái (mỗi khối); ảnh lưu ở thư mục tạm của phiên, không vào repo.
3. Báo: ID khung, kết quả kiểm máy (A phải 0; B–D liệt kê), số đo khác giữa Web và Mobile, chỗ chưa chắc, đường ghi đã dùng
   (`figma_write` hay `use_figma`, lý do).
4. Md đề xuất trình user (có `### Kiểm máy` cuối mỗi phần, kèm bảng "khác bản cũ" khi sửa md có sẵn); ghi vào repo sau khi
   user duyệt (L1 / L2 theo `.claude/rules/approval-gate.md`).

## 13. Giới hạn script đã biết

- `figma-component-export.js` đọc thân component ở FRAME có nền; component ráp từ instance L0 (Text Field, List Item, Progress,
  OTP Field) thì cột Nền, Viền, Chữ ra trống hoặc nhầm sang cột Icon, "Cỡ icon" lấy rộng của instance L0, "Viền" luôn 1 (mặc định
  của Figma, không phải nét thật), "Rộng" ghi "ôm nội dung" cho khung dọc (AUTO là chiều cao). Khi gặp: làm sạch JSON xuất ra
  (bỏ cột nhiễu, sửa rộng theo biến thật) trước khi chạy `ds-v2-component-doc.py`, hoặc giữ khối máy lần xuất đọc được; số
  Web/Mobile luôn lấy ở bảng Token của từng phần (Mục 7).
- Slot, Instance swap: tên preferred value chỉ tra được trong cùng trang; icon ở trang `✦ DS · Icons` ra mã 8 ký tự, thay bằng tên icon
  trước khi render.
- Phần máy không có số theo mode: số Web/Mobile chỉ nằm ở bảng Token của từng phần (dựng bằng Mục 7).

## Hỏi user khi

- Nền thật của component chưa ghi trong md ("Khi dùng" không nói đặt trên nền gì).
- Kiểm máy có cờ B ✕, C, D (đó là quyết định về look đã duyệt, không tự sửa).
- Component có trục chưa có biến theo nền tảng (số không đọc được từ biến).
