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
  - design/v2/components/l1/avatar.md
  - design/v2/components/l1/status-chip.md
  - design/v2/components/l1/button.md
---

# Base / List Item

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / List Item` (6507:209513, trang DS · Components ·
> L0–L3, Section `List Item · L1 · Component Base` 6507:209480), khung tài liệu `Tài liệu · List Item` (6507:209648, khối Web 6507:209655,
> khối Mobile 6507:209656) · DEC-231 (bỏ hàng List Row), DEC-232 (List Item); giữ DEC-164, DEC-165, DEC-172, DEC-174 như đã nêu ở từng mục ·
> theo Astryx `List / .ListItem` + `Item` · ráp từ [Avatar](avatar.md), [Status Chip](status-chip.md), [Button](button.md)

Một component cho cả web và app, không có biến thể Platform: cao tối thiểu, lề, khoảng cách, cỡ chữ đọc từ biến collection
Platform, khung chứa đặt mode Web hoặc Mobile thì dòng tự đổi. Màu (collection Component, tiền tố `list-row/`, giữ tên theo DEC-232)
giống nhau ở hai nền tảng. Một dòng = **đầu dòng (Slot) · chữ (Label + Description) · giá trị · cuối
dòng (Slot) · dấu chọn**; kẻ dưới tuỳ chọn. Component không biết nghiệp vụ: chữ mẫu Title, Description, Value.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Khi dùng:** một dòng trong danh sách, nhóm trên nền trắng hoặc trong thẻ, sheet: dòng menu, dòng cài đặt, dòng lịch
  sử, dòng người. Bấm được (điều hướng, chọn) hoặc chỉ đọc.
- **Đầu dòng (Start Content, Slot, tối đa 1):** Base / Avatar (MD 36, hoặc Content=Icon cho icon trong vòng) hoặc icon.
- **Chữ:** Label một dòng (cắt "…") + Description một dòng tuỳ chọn.
- **Giá trị (Value):** chữ phụ canh phải, rộng tối đa 120, cắt "…". Dùng cho giá trị cài đặt, giờ.
- **Cuối dòng (End Content, Slot, tối đa 2):** Base / Status Chip, Base / Button (Ghost, Icon Only), icon (mũi tên).
- **Quy ước Slot (user chốt 20/10):** Start Content và End Content chỉ nhận Base / Avatar, Base / Status Chip, Base / Button và icon. Figma để Slot mở (`allowPreferredValuesOnly` tắt, vì icon có hàng nghìn bộ); danh sách gợi ý chỉ là gợi ý, nên quy ước này nằm ở tài liệu, không khoá bằng máy.
- **Align:** Center (mặc định, một dòng chữ) · Start (đầu, cuối, giá trị canh đỉnh: dòng nhiều chữ như lịch sử).
- **Divider:** kẻ dưới dòng, đầy bề ngang; trong thẻ, sheet thì tắt (DEC-182).
- **Chỉ có ở web:** State Hover.
- **Chữ trên dòng:** Label tên sự vật, không thêm "Xem". Description nói thêm một ý. Không viết hoa toàn bộ.
- **Đổi chữ qua thuộc tính:** sửa Label, Description, Value ở panel (thuộc tính), không gõ thẳng lên lớp chữ trong instance: gõ thẳng làm mất việc cắt "…" một dòng (đã gặp 20/10).

### Cấu tạo

Hình phóng 2× trên Figma: Align=Center · Default · Description bật, Start Content = Base / Avatar MD, Value bật, End
Content = Base / Status Chip (Soft), Divider bật.

| Phần | Token | Giá trị web |
|---|---|---|
| Khung dòng | `list-row/min-height`; lề `list-row/padding-x` · `list-row/padding-y`; bo `list-row/radius` | cao tối thiểu 36 · lề 8 · 8 · bo 8 |
| Nền | `list-row/bg/hover` (Hover) · `list-row/bg/pressed` · `list-row/bg/selected`; Default, Focus, Disabled không nền (nền là ô chứa) | neutral/100 · neutral/200 · neutral/100 (Hover đậm hơn `color/bg/hover` neutral/50: lệch DEC-210 cho dòng danh sách, user chốt 20/10) |
| Label | `type/body`; `color/text/primary` | 14/20, một dòng, cắt "…" |
| Description | `type/caption`; `color/text/secondary`; cách Label `list-row/text-gap` | 12/16, cách 2 |
| Value | L0 `.list-item / Value`; `type/body`; `color/text/secondary`; `list-row/value-max-width` | 14/20, rộng tối đa 120, canh phải |
| Khoảng giữa các phần | `list-row/gap` | 8 |
| Dấu chọn | `icon/check`; `list-row/check/fg`; `icon/size/md` | 16, chỉ State=Selected |
| Kẻ dưới | L0 `.list-item / Divider`; `list-row/divider`; `list-row/divider-height` | 1px `color/border/default` |
| Vòng focus | L0 `.focus / Ring`: bóng lan 4 `color/border/focus` + lan 2 khe `focus/gap`; bo lớp ruột `list-row/radius` | 2 · 2 · bo ruột 8, vòng ngoài bo 12 (= 8 + 2 + 2) |
| Đầu dòng | Slot `Start Content` — **Base / Avatar · MD · Content=Icon → xem tài liệu Avatar** (hoặc icon) | không lặp token của Avatar |
| Cuối dòng | Slot `End Content` — **Base / Status Chip · Soft → xem tài liệu Status Chip**; **Base / Button · MD · Ghost → xem tài liệu Button** | không lặp token |

### Biến thể

State × Align (Size, Density chưa có: một mật độ, lề 8). 12 biến thể = State 6 × Align 2.

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | không nền |
| Hover | nền `list-row/bg/hover` = neutral/100, 1,10:1 so với trắng (lệch DEC-210 cho dòng danh sách, user chốt 20/10; chỉ web) |
| Pressed | nền `list-row/bg/pressed`; chữ phụ đổi `list-row/fg/secondary-pressed` (neutral/600) |
| Focus | vòng 2 cách 2 bo 10 (lớp `.focus / Ring` đặt tự do sau dòng, không cắt khung); khe theo `focus/gap` (đặt Context=Canvas khi nằm trên nền xám) |
| Selected | nền `list-row/bg/selected` + dấu tick cuối dòng (không chỉ dựa vào màu, WCAG 1.4.1; DEC-208) |
| Disabled | chữ, icon, dấu chọn xám `list-row/fg/disabled`, không làm mờ (DEC-174); phần trong hai Slot **không** tự xám: đặt State=Disabled ở từng component con (Avatar, Button) |

### Kích thước

Một mật độ. Cao tối thiểu 36 (một dòng chữ: 20 + 2 × 8). Hai dòng chữ 54 (20 + 2 + 16 + 2 × 8). Avatar MD ở đầu dòng 52 (36
+ 2 × 8). Kẻ dưới cộng 1. Mọi cao ≥ `touch/min` 24 (WCAG 2.5.8).

### Nên và không nên

1. **Nên:** đầu dòng một phần (Avatar hoặc icon), cuối dòng tối đa hai (chip, mũi tên). **Không nên:** ba phần cuối dòng
   đẩy Label còn vài chữ.
2. **Nên:** kẻ giữa các dòng của nhóm trên nền trắng, bỏ kẻ ở dòng cuối. **Không nên:** kẻ giữa các dòng đã nằm trong thẻ
   hoặc sheet (DEC-182).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Label 17,73 (rê 16,09 · chọn 16,09 · bấm 14,18) · chữ phụ 5,43 (rê 4,92 · chọn 4,92 · bấm 6,22 với `list-row/fg/secondary-pressed`; 4,34 nếu dùng `color/text/secondary`) |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,58: được miễn (control không hoạt động) |
| 1.4.1 Dùng màu | ✓ | Selected có dấu tick; không chỉ đổi nền |
| 1.4.11 Tương phản ngoài chữ (AA) | ✓ | Tick 9,47 trên nền chọn · nền rê và nền chọn so với trắng 1,10 (tick và tên gánh việc nhận ra) · vòng focus 15,13 · kẻ dưới 1,25 (trang trí) |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | Vòng 2px cách 2px, tương phản ≥ 3:1 |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | tối thiểu 36 |
| 4.1.2 Tên, vai trò | ✓ | dòng bấm được là `link` hoặc `button`, chọn thì `aria-selected` / `aria-current`; nút trong cuối dòng là đích bấm riêng, không lồng `button` trong `button` |
| 2.1.1 Bàn phím | ✓ | Enter, Space (dòng chọn) hoặc Enter (dòng link); thứ tự Tab theo đọc |
| **Điểm web** | | **8/8 đạt** |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Disabled · Selected |
| Align | Biến thể | Center | Center · Start |
| Label | Chữ (đưa ra panel từ `.list-item / Text`) | Title | tên dòng |
| Has Description | Bật tắt (thuộc tính của `.list-item / Text`, đưa ra panel) | bật | — |
| Description | Chữ (từ `.list-item / Text`) | Description | ý phụ |
| Has Value | Bật tắt (thuộc tính của dòng, ẩn instance `.list-item / Value`) | tắt | — |
| Value | Chữ (từ `.list-item / Value`) | Value | giá trị phụ, giờ |
| Has Start Content | Bật tắt | bật | — |
| Start Content | Slot, tối đa 1; gợi ý (không khoá hẳn, vì icon có hàng nghìn): Base / Avatar, icon/circle-dashed · chevron-right · phone · plus · search | icon/circle-dashed | Base / Avatar · icon |
| Has End Content | Bật tắt | bật | — |
| End Content | Slot, tối đa 2, cách `list-row/gap`; gợi ý (không khoá hẳn): Base / Status Chip, Base / Button, icon (5 bộ) | icon/circle-dashed | Base / Status Chip · Base / Button · icon |
| Divider | Bật tắt | tắt | — |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Chữ | `.list-item / Text` · L0 | Label 1 dòng; Description 1 dòng | Label · Description · Has Description |
| Giá trị | `.list-item / Value` · L0 | rộng tối đa 120 | Value · Has Value |
| Kẻ dưới | `.list-item / Divider` · L0 | — | Divider (thuộc tính của dòng) |
| Vòng focus | `.focus / Ring` · L0 | Tone Default; chỉ ở State=Focus; bo ruột `list-row/radius` | — |
| Dấu chọn | `icon/check` · icon | chỉ ở State=Selected | — |
| Đầu dòng | `Base / Avatar` · L1 → xem [tài liệu Avatar](avatar.md); icon | MD (36) · SM (24); Content=Icon cho icon trong vòng | Start Content (Slot) |
| Cuối dòng | `Base / Status Chip` · L1 → xem [tài liệu Status Chip](status-chip.md); `Base / Button` · L1 → xem [tài liệu Button](button.md); icon | Chip Soft hoặc Dot; Button SM hoặc MD, Ghost, Icon Only | End Content (Slot) |

### Được dùng trong

Chưa có component cha dùng (L2 chưa dựng).

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Cao tối thiểu | `list-row/min-height` | 36 |
| Lề ngang · lề dọc | `list-row/padding-x` · `list-row/padding-y` | 8 · 8 |
| Khoảng giữa các phần | `list-row/gap` | 8 |
| Giữa Label và Description | `list-row/text-gap` | 2 |
| Bo | `list-row/radius` | 8 |
| Rộng tối đa Value | `list-row/value-max-width` | 120 |
| Kẻ | `list-row/divider-height` | 1 |
| Chữ | `type/body` · `type/caption` | 14/20 · 12/16 |
| Cỡ dấu chọn | `icon/size/md` | 16 |
| Vòng focus | `focus/width` · `focus/offset` · `focus/gap` (collection Context) | 2 · 2 |
| Vùng chạm | `touch/min` | 24 ✓ |

Đã bỏ khỏi `tokens.json` 0.12.0 các biến `list-row/*` không còn dùng (DEC-231): `ring-radius` (vòng focus dùng `list-row/radius`), `lead-slot/*`, `lead-margin-y`, `lead/*`, `switch/*`, `icon-stroke`.

Màu (collection Component, tiền tố `list-row/`): bảng "Màu theo phần" ở Phần máy. Tên trong code: `<ListItem label description
value start end selected disabled divider align="center|start" />`; biến CSS `--list-row-*` (giữ tên, DEC-232), `--icon-size-md`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6507:209648 ngày 20/10 (ngưỡng 1,1:1; ô mẫu đặt trên nền trắng `color/bg/surface`).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 15 ô, 20 mẫu (khối Web; cả khung 29 ô, 39 mẫu) | luật A: 0 lỗi, ô nào cũng có nền riêng và viền mảnh |
| ⚠ Nền chìm (lớp "Vòng focus") | Trạng thái · Focus (Web, Mobile) | ruột vòng trắng trùng nền ô 1:1; hình giữ nhờ vòng focus 15,13:1 |
| Sát ngưỡng (lớp "Content Row") | Trạng thái · Hover (Web), Selected (Web, Mobile) | nền #F2F4F7 = 1,10:1 (Hover dùng neutral/100); Selected giữ hình nhờ dấu tick |
| Cờ ngoài (lớp ngoài) | Web Hover, Web Pressed, Mobile Pressed | "GIỐNG DEFAULT" là báo nhầm: nền nằm ở lớp con Content Row, lớp ngoài của dòng không fill ở mọi State; số đúng ở dòng trên (Pressed neutral/200 = 1,25:1 so với ô trắng) |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Khi dùng, Slot, Value, Align, Divider:** như web (cùng cấu tạo, cùng thuộc tính).
- **Khác web:** không Hover; lề dọc 12, khoảng giữa các phần 12; cao tối thiểu 52; chữ 15 / 13; vùng chạm tối thiểu 44 (cao
  tối thiểu 52 đã đủ, dòng không cần thêm vùng chạm vô hình).
- **Đầu dòng:** Base / Avatar MD (36, hoặc Content=Icon) hoặc icon 20.
- **Cuối dòng:** tối đa 2 phần; nút trong dòng dùng Base / Button MD (42), không Tooltip (app không có).
- **Chữ trên dòng:** như web; Label một dòng, cắt "…".

### Cấu tạo

Hình phóng 2× trên Figma: như web, mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Khung dòng | `list-row/min-height`; lề `list-row/padding-x` · `list-row/padding-y`; bo `list-row/radius` | cao tối thiểu 52 · lề 12 · 12 · bo 8 |
| Nền | `list-row/bg/pressed` · `list-row/bg/selected` (Hover có trong component, không dùng) | neutral/200 · neutral/100 |
| Label | `type/body`; `color/text/primary` | 15/22, một dòng, cắt "…" |
| Description | `type/caption`; `color/text/secondary`; `list-row/text-gap` | 13/18, cách 2 |
| Value | L0 `.list-item / Value`; `type/body`; `list-row/value-max-width` | 15/22, rộng tối đa 120 |
| Khoảng giữa các phần | `list-row/gap` | 12 |
| Dấu chọn | `icon/check`; `icon/size/md` | 20 |
| Kẻ dưới | `.list-item / Divider`; `list-row/divider` | 1px |
| Vòng focus | `.focus / Ring`; bo ruột `list-row/radius` | 2 · 2 · bo ruột 8, vòng ngoài bo 12 (khi có bàn phím ngoài hoặc trợ năng) |
| Đầu dòng · Cuối dòng | Slot — **Base / Avatar · MD · Content=Icon**; **Base / Status Chip · Soft**; **Base / Button · MD · Ghost** → xem tài liệu của từng component | không lặp token |

### Biến thể

Như web: 12 biến thể; Hover có trong set nhưng app không dùng.

### Trạng thái

Như web, trừ Hover. Focus: "khi điều hướng bằng bàn phím ngoài hoặc trợ năng".

### Kích thước

Một mật độ. Cao tối thiểu 52 (một dòng chữ 22 + 2 × 12 = 46 → nâng lên 52). Hai dòng chữ 66 (22 + 2 + 18 + 2 × 12). Avatar
MD ở đầu dòng 60 (36 + 2 × 12). Kẻ dưới cộng 1. Mọi cao ≥ `touch/min` 44 (WCAG 2.5.5).

### Nên và không nên

1. **Nên:** dòng bấm được cao ≥ 52, nút trong dòng là Ghost MD. **Không nên:** đặt Primary trong dòng (DEC-177: không Primary
   trong thẻ, danh sách).
2. **Nên:** Selected có tick cuối dòng. **Không nên:** chỉ đổi nền để báo đang chọn.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | như web; chữ phụ lúc bấm 6,22 với `list-row/fg/secondary-pressed` |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,58: được miễn |
| 1.4.1 Dùng màu | ✓ | Selected có dấu tick |
| 1.4.11 Tương phản ngoài chữ (AA) | ✓ | như web |
| 2.4.7 · 2.4.13 | ✓ | focus khi có bàn phím ngoài hoặc công cụ trợ năng |
| 2.5.8 (≥ 24) · 2.5.5 (≥ 44) | ✓ | tối thiểu 52 |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng (như aria-label); dòng chọn báo "đã chọn" |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Enter, Space; theo thứ tự focus |
| **Điểm app** | | **8/8 đạt** |

### Thuộc tính

Như web (cùng bảng).

### Thành phần lồng

Như web (cùng bảng); Button trong cuối dòng cỡ MD (42) ở app.

### Được dùng trong

Chưa có component cha dùng (L2 chưa dựng).

### Token

Số đo (collection Platform, mode Mobile): cao tối thiểu `list-row/min-height` 52 · lề `list-row/padding-x` · `padding-y` 12 ·
12 · `list-row/gap` 12 · `list-row/text-gap` 2 · bo `list-row/radius` 8 · `list-row/value-max-width` 120 · kẻ 1 ·
chữ `type/body` 15/22 · `type/caption` 13/18 · `icon/size/md` 20 · `touch/min` 44 ✓.

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 14 ô, 19 mẫu (khối Mobile) | luật A: 0 lỗi |
| ⚠ Nền chìm (lớp "Vòng focus") | Trạng thái · Focus | ruột vòng trắng trùng nền ô 1:1; hình giữ nhờ vòng focus 15,13:1 |
| Sát ngưỡng (lớp "Content Row") | Trạng thái · Selected | nền #F2F4F7 = 1,10:1; giữ hình nhờ dấu tick (app không đặt Hover, không có cờ Hover) |
| Cờ ngoài (lớp ngoài) | Trạng thái · Pressed | "GIỐNG DEFAULT" là báo nhầm như phần Web: nền nằm ở lớp con Content Row |

## Đối chiếu Astryx

Nguồn: `List / .ListItem` (86:202661), `Item` (2639:51616), `List` (86:202686), trang Astryx · Library (chỉ đọc).

| | Astryx | DS v2 | Vì sao |
|---|---|---|---|
| Khớp | Label + Description (Has Description), Slot Start Content / End Content (+ Has …), Divider bật tắt 1px dưới dòng, Content Row canh giữa lề đều, nền khi rê / chọn, Align Center · Start (từ `Item`) | giữ nguyên cấu tạo | — |
| Lệch | State 4 (Default, Hovered, Selected, Disabled) | State 6, thêm Pressed và Focus | app cần Pressed, bàn phím cần Focus (DEC-172) |
| Lệch | Disabled giảm độ mờ 50% | Disabled xám `list-row/fg/disabled`, không làm mờ | DEC-174 |
| Lệch | Selected chỉ đổi nền | thêm dấu tick cuối dòng | WCAG 1.4.1; DEC-208 |
| Lệch | Density Compact · Balanced · Spacious | một mật độ = Balanced (web lề 8) | chưa chốt |
| Lệch | bo nền dòng 10 | bo 8 (`list-row/radius`) | DEC-165 |
| Lệch | chữ trần vào Slot cuối dòng | thêm L0 `.list-item / Value` (chữ giá trị / giờ) | L2 chỉ đổi chữ, swap, Slot trong danh sách chọn sẵn (luật d) |
| Lệch | Slot mở, nhận mọi thứ | Slot gợi ý (preferred) Avatar, Chip, Button, icon; quy ước ở tài liệu chỉ nhận bốn loại này | luật d: ghi cấu hình được phép ở tài liệu cha; Figma không khoá hẳn được vì icon có hàng nghìn bộ |
| Chưa làm | `Item / Marker` (Slot đầu nhất), `List` (Header + Children) | — | chờ L2 cần (Notification chấm chưa đọc; nhóm có tiêu đề) |

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần. Chữ Label, Description, Value nằm ở instance L0
lồng nên bộ xuất không đọc được màu của riêng chúng; màu xem bảng Token và bảng Màu theo phần.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / List Item` (6507:209513) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Has Value | Bật tắt | tắt | — |
| Divider | Bật tắt | tắt | — |
| Start Content | Slot | — | nhận: Base / Avatar · icon/circle-dashed · icon/chevron-right · icon/phone · icon/plus · icon/search |
| End Content | Slot | — | nhận: Base / Status Chip · Base / Button · icon/chevron-right · icon/circle-dashed · icon/plus · icon/phone · icon/search |
| Has Start Content | Bật tắt | bật | — |
| Has End Content | Bật tắt | bật | — |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Disabled · Selected |
| Align | Biến thể | Center | Center · Start |

12 biến thể · trục State × Align.

### Màu theo phần (token)

| State | Nền | Chữ | Vòng focus |
|---|---|---|---|
| Default | trong suốt | `color/text/primary` | — |
| Hover | `list-row/bg/hover` | `color/text/primary` | — |
| Pressed | `list-row/bg/pressed` | `color/text/primary` | — |
| Focus | trong suốt | `color/text/primary` | `color/border/focus · dày 2 · khe focus/gap · 2` |
| Disabled | trong suốt | `list-row/fg/disabled` | — |
| Selected | `list-row/bg/selected` | `color/text/primary` | — |

### Số đo theo phần (token)

| Cao | Rộng |
|---|---|
| 54 | 360 |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label | `type/body` |
| Description | `type/caption` |

<!-- auto:end -->
