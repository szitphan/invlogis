---
type: design-component
status: draft
updated: 2026-10-26
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Base / Button

> L1 · phiên bản 0.2.0 · Nháp · người phụ trách @szitphan · Figma `Base / Button` (6373:491, trang DS · Components ·
> L0–L3), khung tài liệu `Tài liệu · Button` (6457:82802, khối Web 6457:82809, khối Mobile 6457:82816) · DEC-172…177, DEC-192,
> DEC-197…199, DEC-206, DEC-210, DEC-240 (Outline), DEC-241 (thay bởi DEC-258), DEC-259 · đi cùng [Tooltip](tooltip.md)

Một component cho cả web và app, không có biến thể Platform. Cao, lề, bo, cỡ chữ đọc từ biến collection Platform:
khung chứa (màn, thẻ) đặt mode Web hoặc Mobile thì nút tự đổi cỡ. Phần **Web** và phần **Mobile** dưới đây mỗi phần tự
đứng được: đọc phần của nền tảng mình làm là đủ. Màu (collection Component) giống nhau ở hai nền tảng.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Primary:** hành động chính của một vùng (Lưu, Gửi, Xác nhận). Mỗi vùng chỉ một nút Primary.
- **Secondary:** hành động phụ đi cùng nút chính (Huỷ, Quay lại), nút trong thẻ, sheet.
- **Ghost:** ít nhấn mạnh: thanh công cụ, đầu màn, hàng bảng; nút icon ở đầu màn.
- **Danger:** phá huỷ (Xoá). Không bao giờ là nút chính của vùng; bấm thì mở hộp xác nhận.
- **Outline:** nút phụ đặt trên khối nền `color/bg/muted` (khối phụ trong thẻ), nơi Secondary chìm vào nền. Nền trang trắng (DEC-258).
- **Content:** Label mặc định · Leading Icon khi icon giúp nhận ra nhanh (Thêm, Tải xuống) · Icon Only khi chỗ chật và
  icon quen thuộc; luôn có tên cho trình đọc màn hình và bật Tooltip.
- **Cỡ web:** MD 32 mặc định khi kéo ra (DEC-210) · SM 28 trong hàng bảng · LG 40 ở màn đăng nhập và nút cần nổi (DEC-173).
- **Chỉ có ở web:** Hover; Tooltip cho nút Icon Only (tên hành động khi rê chuột hoặc focus, nổi phía trên, cách 4; DEC-206).
- **Thứ tự (DEC-088):** chân dialog `[Phụ][Chính]` canh phải; hàng nút form trong trang `[Chính][Phụ]` canh trái.
- **Chữ trên nút:** động từ 1–3 từ, viết hoa chữ đầu, không viết hoa toàn bộ; tránh "OK", "Đồng ý" khi nói rõ được hành
  động; đang tải "Đang lưu…", "Đang gửi…". Không khoá nút gửi form: bấm khi thiếu dữ liệu thì báo lỗi ngay tại ô (DEC-177).

### Cấu tạo

Hình phóng 2× trên Figma: Primary · Leading Icon · MD · Default, cạnh đó Ghost · Icon Only · MD bật Tooltip.

| Phần | Token | Giá trị web |
|---|---|---|
| Nền | `button/bg/{type}`, Hover `-hover`, Pressed `-pressed`; Disabled `button/bg/disabled` | Ghost không nền (nền là ô chứa). Outline: Default không nền; Hover `button/bg/outline-hover` = neutral/300 #D0D5DD; Pressed `button/bg/outline-pressed` = neutral/400 #98A2B3 |
| Viền | chỉ Outline: `button/border/outline`; Disabled `button/border/outline-disabled` (alias `color/border/default`) | 1px; Disabled giữ viền, nền `button/bg/disabled` |
| Nhãn | thuộc tính Label; `type/label`; màu `button/fg/{type}` | 14/20 Medium |
| Icon | thuộc tính Icon (bộ DS · Icons); `icon/size/sm`; màu `button/fg/{type}` | 14 |
| Cao | `control/height/sm · md · lg` | 28 · 32 · 40 |
| Lề | `control/padding-x/*`; phía icon `control/padding-x-icon/*` | 8 · 12 · 16; phía icon 6 · 8 · 12 |
| Icon → chữ | `control/icon-gap` | 6 |
| Bo | `radius/control` | 8 |
| Vòng focus | L0 `.focus / Ring`: bóng lan 4 `color/border/focus` (Danger `button/focus/danger`) + lan 2 khe `color/focus/gap` (= nền trang trắng, DEC-258); `focus/width` · `focus/offset` | 2 · 2 |
| Vòng quay | L0 `.button / Spinner`, cỡ `icon/size/sm`, khi State=Loading; chữ lấy Loading Label | 14 |
| Tooltip | **Base / Tooltip · Top → xem [tài liệu Tooltip](tooltip.md)** (component L1 lồng, không lặp token) | bật bằng Tooltip |

### Biến thể

Type × Content (Size MD, Default). Icon Only chỉ có Primary, Secondary, Ghost (DEC-197). 225 biến thể = Label 90 +
Leading Icon 90 + Icon Only 45.

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | màu theo Type; Ghost, Outline không nền |
| Hover | nền `-hover` (chỉ web) |
| Pressed | nền `-pressed` |
| Focus | vòng 2 cách 2 (lớp `.focus / Ring` đặt tự do sau nút, không cắt khung); Danger vòng đỏ (DEC-198); Ghost, Outline: ruột và khe `color/focus/gap` = nền trang trắng (DEC-258) |
| Disabled | một kiểu xám, không làm mờ (DEC-174); Outline giữ viền `button/border/outline-disabled` |
| Loading | vòng quay + "Đang lưu…", giữ nguyên cỡ nút, bấm thêm không làm gì |

### Kích thước

| Size | Cao | Lề | Lề phía icon | Icon Only | Dùng khi |
|---|---|---|---|---|---|
| SM | 28 | 8 | 6 | 28 × 28 | hàng bảng |
| MD | 32 | 12 | 8 | 32 × 32 | mặc định |
| LG | 40 | 16 | 12 | 40 × 40 | màn đăng nhập, nút cần nổi |

Mọi cỡ ≥ `touch/min` 24 (WCAG 2.5.8). Bo 8 ở mọi cỡ.

### Nên và không nên

1. **Nên:** một Primary kèm một Secondary trong vùng. **Không nên:** hai Primary cạnh nhau.
2. **Nên:** Danger nền đỏ nhạt, tách khỏi nút chính, bấm thì mở xác nhận. **Không nên:** Danger đứng ở chỗ nút chính
   hoặc nền đỏ đặc.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✕ | Primary 15,13 · Secondary 16,09 · Ghost 17,73 · Outline 17,73 · Danger 5,76 (rê 5,11) · **Danger lúc bấm 4,27** — giữ vì trạng thái chỉ thoáng qua (DEC-199) |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn (control không hoạt động) |
| 1.4.11 Tương phản ngoài chữ (AA) | ✓ | Viền Outline 1,47, nền Secondary 1,10: chữ đủ để nhận ra nút · vòng focus 15,13 (Danger 6,57) |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | Vòng 2px cách 2px, tương phản ≥ 3:1. Khe vòng focus `color/focus/gap` = nền trang trắng (DEC-258). |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | SM 28 · MD 32 · LG 40 |
| 4.1.2 Tên, vai trò | ✓ | Icon Only bắt buộc `aria-label`; Loading đặt `aria-busy`, nhãn "Đang lưu…" |
| 2.1.1 Bàn phím | ✓ | Enter, Space kích hoạt; theo thứ tự Tab |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ | Tooltip hiện cả khi focus bằng bàn phím, Esc đóng được, rê lên tooltip không tắt |
| 2.3.3 Chuyển động (AAA) | ✓ | Vòng quay đứng yên khi bật giảm chuyển động |
| **Điểm web** | | **8/9 đạt** · cần cải thiện: Danger lúc bấm 4,27 (DEC-199) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Type | Biến thể | Primary | Primary · Secondary · Ghost · Danger · Outline |
| Content | Biến thể | Label | Label · Leading Icon · Icon Only (Icon Only chỉ Primary, Secondary, Ghost) |
| Size | Biến thể | MD (DEC-210) | SM 28 · MD 32 · LG 40 |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Disabled · Loading (Icon Only không có Loading) |
| Label | Chữ | Lưu | nhãn nút |
| Loading Label | Chữ | Đang lưu… | nhãn khi State=Loading |
| Icon | Đổi component | icon/plus · Size=16 | mọi icon trong ✦ DS · Icons (4 bộ chọn sẵn) |
| Tooltip | Bật tắt | tắt | bật cho Icon Only; chữ tooltip đưa ra panel |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Vòng focus | `.focus / Ring` · L0 | Tone Default; Danger dùng Tone Danger; chỉ ở State=Focus | — |
| Vòng quay | `.button / Spinner` · L0 | chỉ ở State=Loading | — |
| Icon | `icon/*` · DS · Icons | đổi bằng Icon, 4 bộ chọn sẵn; cỡ 14 | Icon |
| Tooltip | `Base / Tooltip` · L1 → xem [tài liệu Tooltip](tooltip.md) | Placement=Top, nổi trên nút cách 4 | Tooltip (bật tắt) + chữ tooltip (instance lồng đưa ra panel) |

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Record Card | Slot `Footer` (chỉ nhận Base / Button), canh phải, cách 8 | Ghost + Secondary · Label · MD (32) · Default; chưa dùng SM |
| Base / Record Card | `Trailing` ở đầu thẻ (bật Has Trailing), đổi component | mặc định Base / Status Chip; được đổi sang Base / Button |

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | SM | MD | LG |
|---|---|---|---|---|
| Cao, rộng Icon Only | `control/height/*` | 28 | 32 | 40 |
| Lề hai bên | `control/padding-x/*` | 8 | 12 | 16 |
| Lề phía icon | `control/padding-x-icon/*` | 6 | 8 | 12 |
| Icon → chữ | `control/icon-gap` | 6 | 6 | 6 |
| Cỡ icon | `icon/size/sm` | 14 | 14 | 14 |
| Bo | `radius/control` | 8 | 8 | 8 |
| Chữ | `type/label` | 14/20 Medium | 14/20 Medium | 14/20 Medium |
| Vòng focus | `focus/width` · `focus/offset` · `color/focus/gap` (= nền trang) | 2 · 2 | 2 · 2 | 2 · 2 |
| Vùng chạm | `touch/min` | 24 ✓ | 24 ✓ | 24 ✓ |

Màu (collection Component, tiền tố `button/`): bảng "Màu theo phần" ở [Phần máy](#phần-máy-chung-web-và-mobile).

Tên trong code: `<Button variant="primary|secondary|ghost|danger|outline" size="sm|md|lg" icon={…} iconOnly loading
tooltip="Thêm">`; biến CSS `--button-*` (màu), `--control-*` (cao, lề), `--radius-control`, `--icon-size-sm`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6457:82802 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 109 ô, 119 mẫu (cả hai khối) | 0 lỗi: ô nào cũng có nền thật và viền mảnh |
| ⚠ Nền chìm | Ghost · Focus | nền thân trắng trùng ô trắng; hình giữ nhờ vòng focus 15,13:1 |
| Sát ngưỡng | Outline · Disabled trên nền trắng | nền thân #F2F4F7 trên ô trắng 1,10:1; viền `button/border/outline-disabled` 1,25:1 (số tính lại theo nền trắng (DEC-258), chưa chạy lại máy) |
| Sát ngưỡng (lớp "Vòng focus") | Outline · Focus trên nền trắng | khe vòng focus trắng trùng nền ô (đúng thiết kế); vòng 15,13:1 (số tính lại theo nền trắng (DEC-258), chưa chạy lại máy) |
| Sát ngưỡng | Secondary (Default, Focus, Loading), mọi Disabled, Ghost Hover trên trắng | 1,10:1 · Danger 1,14:1 |

Ô mẫu Outline (15 ô, cả hai khối) nằm trên nền trắng như mọi ô (DEC-258). Hết ba điểm ✕ cũ: Outline · Hover
#D0D5DD, Pressed #98A2B3 đều khác Default; khe focus không còn lộ; Disabled có viền. Toàn khung (web + mobile): 0 ✕, 4 cờ ⚠
ở lớp ngoài và 2 cờ ⚠ ở lớp con.

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Primary:** hành động chính của một vùng (Lưu, Gửi, Xác nhận). Mỗi vùng chỉ một nút Primary.
- **Secondary:** hành động phụ đi cùng nút chính (Huỷ, Quay lại), nút trong thẻ, sheet.
- **Ghost:** ít nhấn mạnh: đầu màn, chân thẻ; nút icon ở đầu màn.
- **Danger:** phá huỷ (Xoá). Không bao giờ là nút chính của vùng; bấm thì mở hộp xác nhận.
- **Outline:** nút phụ đặt trên khối nền `color/bg/muted` (khối phụ trong thẻ), nơi Secondary chìm vào nền. Nền trang trắng (DEC-258).
- **Content:** Label mặc định · Leading Icon khi icon giúp nhận ra nhanh · Icon Only cho nút icon đầu màn; luôn có tên
  cho trình đọc màn hình (app không có Tooltip).
- **Cỡ app:** LG 52 cho nút chân màn · MD 42 cho nút trong thẻ, sheet và nút icon · SM 36 cho nút nhỏ (DEC-173).
- **Khác web:** không Hover, không Tooltip; bo tròn hẳn; chữ 15 Semi Bold; vùng chạm tối thiểu 44 — SM, MD thêm vùng
  chạm vô hình quanh nút (foundations mục 9).
- **Thứ tự (DEC-088):** chân dialog `[Phụ][Chính]` canh phải; hàng nút form trong trang `[Chính][Phụ]` canh trái.
- **Chữ trên nút:** động từ 1–3 từ, viết hoa chữ đầu, không viết hoa toàn bộ; tránh "OK", "Đồng ý" khi nói rõ được hành
  động; đang tải "Đang lưu…", "Đang gửi…". Không khoá nút gửi form: bấm khi thiếu dữ liệu thì báo lỗi ngay tại ô (DEC-177).

### Cấu tạo

Hình phóng 2× trên Figma: Primary · Leading Icon · MD · Default.

| Phần | Token | Giá trị app |
|---|---|---|
| Nền | `button/bg/{type}`, Pressed `-pressed`; Disabled `button/bg/disabled` (Hover có trong component, không dùng) | Ghost không nền (nền là ô chứa). Outline: Default không nền; Pressed `button/bg/outline-pressed` = neutral/400 #98A2B3 |
| Viền | chỉ Outline: `button/border/outline`; Disabled `button/border/outline-disabled` (alias `color/border/default`) | 1px; Disabled giữ viền, nền `button/bg/disabled` |
| Nhãn | thuộc tính Label; `type/label`; màu `button/fg/{type}` | 15/20 Semi Bold |
| Icon | thuộc tính Icon (bộ DS · Icons); `icon/size/sm`; màu `button/fg/{type}` | 16 |
| Cao | `control/height/sm · md · lg` | 36 · 42 · 52 |
| Lề | `control/padding-x/*`; phía icon `control/padding-x-icon/*` | 12 · 16 · 24; phía icon 8 · 12 · 20 |
| Icon → chữ | `control/icon-gap` | 8 |
| Bo | `radius/control` | tròn hẳn (9999) |
| Vòng focus | L0 `.focus / Ring`: bóng lan 4 `color/border/focus` (Danger `button/focus/danger`) + lan 2 khe `color/focus/gap` (= nền trang trắng, DEC-258); `focus/width` · `focus/offset` | 2 · 2 |
| Vòng quay | L0 `.button / Spinner`, cỡ `icon/size/sm`, khi State=Loading; chữ lấy Loading Label | 16 |
| Vùng chạm | `touch/min` | 44: nút thấp hơn thì code thêm vùng chạm vô hình, không đổi hình |

### Biến thể

Type × Content (Size MD, Default). Icon Only chỉ có Primary, Secondary, Ghost (DEC-197). 225 biến thể = Label 90 +
Leading Icon 90 + Icon Only 45 (dùng chung với web).

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | màu theo Type; Ghost, Outline không nền |
| Pressed | nền `-pressed`; phản hồi khi chạm |
| Focus | khi điều hướng bằng bàn phím ngoài hoặc trợ năng: vòng 2 cách 2; Danger vòng đỏ (DEC-198); Ghost, Outline: ruột và khe `color/focus/gap` = nền trang trắng (DEC-258) |
| Disabled | một kiểu xám, không làm mờ (DEC-174); Outline giữ viền `button/border/outline-disabled` |
| Loading | vòng quay + "Đang lưu…", giữ nguyên cỡ nút, bấm thêm không làm gì |

App không dùng Hover (biến thể có trong component cho web).

### Kích thước

| Size | Cao | Lề | Lề phía icon | Icon Only | Vùng chạm | Dùng khi |
|---|---|---|---|---|---|---|
| SM | 36 | 12 | 8 | 36 × 36 | thêm 4 mỗi phía → 44 | nút nhỏ |
| MD | 42 | 16 | 12 | 42 × 42 | thêm 1 mỗi phía → 44 | nút trong thẻ, sheet, nút icon |
| LG | 52 | 24 | 20 | 52 × 52 | đủ | nút chân màn |

Bo tròn hẳn ở mọi cỡ.

### Nên và không nên

1. **Nên:** một Primary kèm một Secondary trong vùng. **Không nên:** hai Primary cạnh nhau.
2. **Nên:** Danger nền đỏ nhạt, tách khỏi nút chính, bấm thì mở xác nhận. **Không nên:** Danger đứng ở chỗ nút chính
   hoặc nền đỏ đặc.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✕ | cùng màu với web: Primary 15,13 · Secondary 16,09 · Ghost 17,73 · Outline 17,73 · Danger 5,76 · **Danger lúc bấm 4,27** — giữ (DEC-199) |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn (control không hoạt động) |
| 1.4.11 Tương phản ngoài chữ (AA) | ✓ | Viền Outline 1,47, nền Secondary 1,10: chữ đủ để nhận ra nút · vòng focus 15,13 (Danger 6,57) |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | Vòng 2px cách 2px khi điều hướng bằng bàn phím ngoài, trợ năng. Khe vòng focus `color/focus/gap` = nền trang trắng (DEC-258). |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | SM 36 · MD 42 · LG 52 |
| 2.5.5 Kích thước đích (AAA, ≥ 44) | ! | SM 36, MD 42: code thêm vùng chạm vô hình 44 (foundations mục 9); LG 52 đạt |
| 4.1.2 Tên, vai trò | ✓ | Icon Only bắt buộc nhãn trợ năng (như `aria-label`); Loading báo đang bận, nhãn "Đang lưu…" |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Enter, Space kích hoạt; theo thứ tự focus |
| 2.3.3 Chuyển động (AAA) | ✓ | Vòng quay đứng yên khi bật giảm chuyển động |
| **Điểm app** | | **8/9 đạt** (! = đạt có điều kiện) · cần cải thiện: Danger lúc bấm 4,27 (DEC-199) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Type | Biến thể | Primary | Primary · Secondary · Ghost · Danger · Outline |
| Content | Biến thể | Label | Label · Leading Icon · Icon Only (Icon Only chỉ Primary, Secondary, Ghost) |
| Size | Biến thể | MD (DEC-210) | SM 36 · MD 42 · LG 52 |
| State | Biến thể | Default | Default · Pressed · Focus · Disabled · Loading; Hover có trong component, không dùng trên app |
| Label | Chữ | Lưu | nhãn nút |
| Loading Label | Chữ | Đang lưu… | nhãn khi State=Loading |
| Icon | Đổi component | icon/plus · Size=16 | mọi icon trong ✦ DS · Icons (4 bộ chọn sẵn) |
| Tooltip | Bật tắt | tắt | không dùng trên app, để tắt |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Vòng focus | `.focus / Ring` · L0 | Tone Default; Danger dùng Tone Danger; chỉ ở State=Focus | — |
| Vòng quay | `.button / Spinner` · L0 | chỉ ở State=Loading | — |
| Icon | `icon/*` · DS · Icons | đổi bằng Icon, 4 bộ chọn sẵn; cỡ 16 | Icon |
| Tooltip | `Base / Tooltip` · L1 → xem [tài liệu Tooltip](tooltip.md) | không dùng trên app | — |

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Record Card | Slot `Footer` (chỉ nhận Base / Button), canh phải, cách 8 | Ghost + Secondary · Label · MD (42) · Default; chưa dùng SM |
| Base / Record Card | `Trailing` ở đầu thẻ (bật Has Trailing), đổi component | mặc định Base / Status Chip; được đổi sang Base / Button |

### Token

Số đo (collection Platform, mode Mobile):

| Phần | Token | SM | MD | LG |
|---|---|---|---|---|
| Cao, rộng Icon Only | `control/height/*` | 36 | 42 | 52 |
| Lề hai bên | `control/padding-x/*` | 12 | 16 | 24 |
| Lề phía icon | `control/padding-x-icon/*` | 8 | 12 | 20 |
| Icon → chữ | `control/icon-gap` | 8 | 8 | 8 |
| Cỡ icon | `icon/size/sm` | 16 | 16 | 16 |
| Bo | `radius/control` | tròn | tròn | tròn |
| Chữ | `type/label` | 15/20 Semi Bold | 15/20 Semi Bold | 15/20 Semi Bold |
| Vòng focus | `focus/width` · `focus/offset` · `color/focus/gap` (= nền trang) | 2 · 2 | 2 · 2 | 2 · 2 |
| Vùng chạm | `touch/min` | 44: +4/phía | 44: +1/phía | 44 ✓ |

Màu (collection Component, tiền tố `button/`): bảng "Màu theo phần" ở [Phần máy](#phần-máy-chung-web-và-mobile); app bỏ
cột Hover.

Tên trong code: cùng component `Button` với web (`variant`, `size`, `icon`, `iconOnly`, `loading`); không dùng
`tooltip`; Icon Only bắt buộc nhãn trợ năng.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6457:82802 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 109 ô, 119 mẫu (cả hai khối) | 0 lỗi: ô nào cũng có nền thật và viền mảnh |
| ⚠ Nền chìm | Ghost · Focus | nền thân trắng trùng ô trắng; hình giữ nhờ vòng focus 15,13:1 |
| Sát ngưỡng | Outline · Disabled trên nền trắng | nền thân #F2F4F7 trên ô trắng 1,10:1; viền `button/border/outline-disabled` 1,25:1 (số tính lại theo nền trắng (DEC-258), chưa chạy lại máy) |
| Sát ngưỡng (lớp "Vòng focus") | Outline · Focus trên nền trắng | khe vòng focus trắng trùng nền ô (đúng thiết kế); vòng 15,13:1 (số tính lại theo nền trắng (DEC-258), chưa chạy lại máy) |
| Sát ngưỡng | Secondary (Default, Focus, Loading), mọi Disabled trên trắng | 1,10:1 · Danger 1,14:1 |

App không dùng Hover nên không kiểm Hover. Ô mẫu Outline nền trắng (DEC-258); Pressed #98A2B3 khác Default,
khe focus không còn lộ.

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Button` (6373:491) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Label | Chữ | Lưu | — |
| Loading Label | Chữ | Đang lưu… | — |
| Icon | Đổi component | icon/plus · Size=16 | — |
| Tooltip | Bật tắt | tắt | — |
| Type | Biến thể | Primary | Primary · Secondary · Ghost · Danger · Outline |
| Content | Biến thể | Label | Label · Leading Icon · Icon Only |
| Size | Biến thể | MD | SM · MD · LG |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Disabled · Loading |

225 biến thể · trục Type × Content × Size × State.

### Màu theo phần (token)

| Type | State | Nền | Viền | Chữ | Icon | Vòng focus |
|---|---|---|---|---|---|---|
| Primary | Default | `button/bg/primary` | — | `button/fg/primary` | `button/fg/primary` | — |
| Primary | Hover | `button/bg/primary-hover` | — | `button/fg/primary` | `button/fg/primary` | — |
| Primary | Pressed | `button/bg/primary-pressed` | — | `button/fg/primary` | `button/fg/primary` | — |
| Primary | Focus | `button/bg/primary` | — | `button/fg/primary` | `button/fg/primary` | `color/border/focus · lan 4 + focus/gap · lan 2` |
| Primary | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Primary | Loading | `button/bg/primary` | — | `button/fg/primary` | `button/fg/primary` | — |
| Secondary | Default | `button/bg/secondary` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Secondary | Hover | `button/bg/secondary-hover` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Secondary | Pressed | `button/bg/secondary-pressed` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Secondary | Focus | `button/bg/secondary` | — | `button/fg/secondary` | `button/fg/secondary` | `color/border/focus · lan 4 + focus/gap · lan 2` |
| Secondary | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Secondary | Loading | `button/bg/secondary` | — | `button/fg/secondary` | `button/fg/secondary` | — |
| Ghost | Default | trong suốt | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Ghost | Hover | `button/bg/ghost-hover` | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Ghost | Pressed | `button/bg/ghost-pressed` | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Ghost | Focus | `focus/gap` | — | `button/fg/ghost` | `button/fg/ghost` | `color/border/focus · lan 4 + focus/gap · lan 2` |
| Ghost | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Ghost | Loading | trong suốt | — | `button/fg/ghost` | `button/fg/ghost` | — |
| Danger | Default | `button/bg/danger` | — | `button/fg/danger` | `button/fg/danger` | — |
| Danger | Hover | `button/bg/danger-hover` | — | `button/fg/danger` | `button/fg/danger` | — |
| Danger | Pressed | `button/bg/danger-pressed` | — | `button/fg/danger` | `button/fg/danger` | — |
| Danger | Focus | `button/bg/danger` | — | `button/fg/danger` | `button/fg/danger` | `button/focus/danger · lan 4 + focus/gap · lan 2` |
| Danger | Disabled | `button/bg/disabled` | — | `button/fg/disabled` | `button/fg/disabled` | — |
| Danger | Loading | `button/bg/danger` | — | `button/fg/danger` | `button/fg/danger` | — |
| Outline | Default | trong suốt | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |
| Outline | Hover | `button/bg/outline-hover` | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |
| Outline | Pressed | `button/bg/outline-pressed` | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |
| Outline | Focus | `focus/gap` | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | `color/border/focus · lan 4 + focus/gap · lan 2` |
| Outline | Disabled | `button/bg/disabled` | `button/border/outline-disabled` | `button/fg/disabled` | `button/fg/disabled` | — |
| Outline | Loading | trong suốt | `button/border/outline` | `button/fg/outline` | `button/fg/outline` | — |

### Số đo theo phần (token)

| Content | Size | Cao | Rộng | Lề trái | Lề phải | Khoảng giữa | Bo | Cỡ icon |
|---|---|---|---|---|---|---|---|---|
| Label | SM | `control/height/sm` | ôm nội dung | `control/padding-x/sm` | `control/padding-x/sm` | `control/icon-gap` | `radius/control` | — |
| Label | MD | `control/height/md` | ôm nội dung | `control/padding-x/md` | `control/padding-x/md` | `control/icon-gap` | `radius/control` | — |
| Label | LG | `control/height/lg` | ôm nội dung | `control/padding-x/lg` | `control/padding-x/lg` | `control/icon-gap` | `radius/control` | — |
| Leading Icon | SM | `control/height/sm` | ôm nội dung | `control/padding-x-icon/sm` | `control/padding-x/sm` | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Leading Icon | MD | `control/height/md` | ôm nội dung | `control/padding-x-icon/md` | `control/padding-x/md` | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Leading Icon | LG | `control/height/lg` | ôm nội dung | `control/padding-x-icon/lg` | `control/padding-x/lg` | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Icon Only | SM | `control/height/sm` | `control/height/sm` | 0 | 0 | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Icon Only | MD | `control/height/md` | `control/height/md` | 0 | 0 | `control/icon-gap` | `radius/control` | `icon/size/sm` |
| Icon Only | LG | `control/height/lg` | `control/height/lg` | 0 | 0 | `control/icon-gap` | `radius/control` | `icon/size/sm` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label | `type/label` |

<!-- auto:end -->
