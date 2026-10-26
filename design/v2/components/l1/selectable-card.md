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
  - design/v2/components/l1/card.md
  - design/v2/components/l1/avatar.md
  - design/v2/components/l1/status-row.md
---

# Base / Selectable Card

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Selectable Card` (6442:85947, 10 biến thể, trang DS ·
> Components · L0–L3, Section `Card · L1 · Component Base` 6444:24203) · khung tài liệu `Tài liệu · Selectable Card` (6562:215835, khối
> Web 6562:215842, khối Mobile 6562:215917) · DEC-236 (đổi tên từ Choice Card, Selected × State, Has Avatar, Has Media, Has Body),
> DEC-237 (`.card / Media`), DEC-238 (màu nhấn, rê, Disabled); giữ nhìn đã duyệt DEC-184, DEC-196 · theo Astryx `SelectableCard`
> 2611:21422 · ráp từ [Card](card.md), [Avatar](avatar.md), [Status Row](status-row.md)

Một component cho cả web và app, không có biến thể Platform: radio, chữ, khoảng đọc từ biến collection Platform, khung chứa đặt mode
Web hoặc Mobile thì thẻ tự đổi. Màu một bộ cho hai nền tảng; nền, viền, bo, vòng focus của thẻ lấy từ lớp "Khung thẻ" (Base / Card
Tone Muted). Một thẻ = **radio · [ảnh nhỏ] · cột chữ (Title + Description, Body tuỳ chọn) · vòng icon hoặc avatar**. Thẻ chọn đặt trên
nền trắng (sheet, form) nên ô mẫu nền `color/bg/surface`, trừ cảnh "Không nên". Chữ mẫu trung tính: Title, Description, Label, Value.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Khi dùng:** chọn một trong vài phương án có mô tả (nhóm thẻ chọn trong sheet, form); mỗi thẻ là một radio.
- **Cấu tạo:** radio · [ảnh nhỏ] · cột chữ (Title + Description, Body tuỳ chọn) · vòng icon hoặc avatar cuối thẻ.
- **Selected:** false — nền xám, không viền; true — nền trắng, viền 1px, radio tô kín; không tick góc (radio đã là dấu chọn).
- **Khung thẻ:** Base / Card Tone Muted, Padding None, Elevation None; thẻ chỉ đặt trên nền trắng.
- **Has Icon:** vòng icon 36 cuối thẻ (mặc định bật). **Has Avatar:** Base / Avatar MD 36 ở chỗ vòng icon (tắt). **Has Media:**
  `.card / Media` SM 48 giữa radio và chữ (tắt). **Has Body + Slot Body:** tối đa 3 dòng phụ dưới tên, `.card / Row` hoặc
  Base / Status Row, cách 8 (tắt).
- **Chỉ có ở web:** State Hover (cả Selected false và true).
- **Luật:**
  - Đầu thẻ một phần: bật Has Avatar hoặc Has Media thì tắt Has Icon; thẻ chỉ có một trong ba (vòng icon, avatar, ảnh nhỏ). Figma
    không tự tắt, quy ước nằm ở tài liệu (mô tả component có ghi).
  - Chọn một: trong nhóm chỉ một thẻ Selected = true; chọn thẻ khác thì thẻ cũ về false.
  - Nền trắng: thẻ xám trên khối `color/bg/muted` mất ranh giới; không đặt thẻ chọn trên khối xám. Nền trang trắng (DEC-258).
  - Body chỉ nhận `.card / Row`, Base / Status Row: Slot khoá bằng preferred values (`allowPreferredValuesOnly`), tối đa 3.
  - Đổi chữ qua thuộc tính: Title, Description của `.card / Name` đã đưa ra panel.

### Cấu tạo

Hình phóng 2× trên Figma: Selected=false · State=Default, Has Icon bật, rộng 260; nền ô trắng. Nhãn xám đậm chỉ Khung thẻ (L1 lồng,
không lặp token của nó).

| Phần | Token | Giá trị web |
|---|---|---|
| Khung thẻ | **Base / Card · Muted · Padding None · Elevation None → xem tài liệu Card** | nền, viền chọn, bo, vòng focus lấy từ Khung thẻ |
| Lề | `layout/card-padding` | 16 bốn phía |
| Khoảng giữa các phần | `space/gap-md` | 12 |
| Radio | L0 `.card / Radio`: `card/radio-size` · `card/radio-ring` · `card/radio-on-ring` · `card/radio/border` · `card/radio/on` | 16 · viền 1,5 neutral/500 · chọn viền 5 brand/800 |
| Tên | L0 `.card / Name`: `type/label` · `type/caption` · `card/choice-text-gap` | Title 14/20 Medium · Description 12/16 · cách 2 |
| Cột chữ, Slot Body | `space/inset-sm` | Body cách tên 8, các dòng cách 8; tối đa 3 |
| Vòng icon | L0 `.card / Icon Circle`: `card/lead-size` · `card/lead/bg` · `color/bg/surface` | 36 · icon 20; nền trắng khi thẻ xám, xám khi thẻ đã chọn |
| Ảnh nhỏ | L0 `.card / Media`: `card/media-size-sm` · `radius/inner` | 48 · bo 8; Tone Surface khi thẻ xám, Muted khi thẻ trắng |
| Avatar | **Base / Avatar · MD · Initials → xem tài liệu Avatar** | ở chỗ vòng icon; bật Has Avatar |

### Biến thể

Selected (false · true) × State (Default · Hover · Pressed · Focus · Disabled) = 10 biến thể. Bốn Boolean bật tắt phần: Has Icon (mặc
định bật), Has Avatar, Has Media, Has Body (mặc định tắt); Slot Body tối đa 3. Mẫu trên Figma (Selected=false · Default): mặc định ·
Has Media · Has Avatar · Has Body · không icon · không Description.

### Trạng thái

| State | Selected=false | Selected=true |
|---|---|---|
| Default | Khung thẻ Muted Default: nền `card/choice/bg`; radio Off; vòng icon nền trắng | Khung thẻ Selected: nền trắng, viền 1px `card/border/selected`; radio On; vòng icon `card/lead/bg` |
| Hover (web) | nền `card/choice/bg-hover`; chữ phụ `card/fg/secondary-hover` | Selected Hover: nền `card/bg/hover`; chữ phụ `card/fg/secondary-hover` |
| Pressed | nền `card/choice/bg-pressed` (neutral/300); chữ phụ `card/fg/secondary-pressed`; vòng icon trắng | Selected Pressed: nền `card/bg/pressed`; vòng icon, ảnh nhỏ Tone Surface (trắng) để không chìm |
| Focus | vòng 2 cách 2 bao cả thẻ (từ Khung thẻ) | Selected Focus: nền trắng + vòng |
| Disabled | Khung thẻ Disabled; chữ `card/disabled/fg`; radio Off Disabled (viền `color/border/default`); ruột radio, vòng icon trắng `card/disabled/lead-bg` | như chưa chọn; radio On Disabled (viền `card/disabled/fg`) |

### Kích thước

Rộng theo chỗ đặt (mặc định 361), cột chữ giãn; cao ôm phần cao nhất cộng lề 16 hai đầu. Đo trên instance trong khối mode Web:

| Cấu hình | Cao (Web) |
|---|---|
| Không Description (cao theo vòng icon 36) | 68 |
| Mặc định: Title + Description | 70 |
| Has Avatar (avatar 36) | 70 |
| Has Media (ảnh 48) | 80 |
| Has Body · 2 dòng `.card / Row` | 134 |
| Mỗi dòng Body thêm | 32 (dòng 24 + khoảng 8) |

Cả thẻ là đích bấm; thấp nhất 68 ≥ `touch/min` 24 ✓.

### Nên và không nên

1. **Nên:** đầu thẻ một phần: bật Has Media thì tắt Has Icon. **Không nên:** bật Has Media mà vẫn để Has Icon: hai hình ở hai đầu
   thẻ tranh nhau.
2. **Nên:** thẻ chọn trên nền trắng (sheet, form). **Không nên:** thẻ chọn trên khối `color/bg/muted`: thẻ chưa chọn trùng nền, mất ranh giới.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Title 16,09 trên nền xám · 14,18 rê · 12,03 nhấn · 17,73 đã chọn. Description 4,92 nền xám · 6,22 rê và 5,27 nhấn (neutral/600) · 5,43 đã chọn · 7,06 đã chọn rê |
| 1.4.3 ngoại lệ — Disabled | ✓ | `card/disabled/fg` 2,34 trên nền Disabled: được miễn |
| 1.4.1 Dùng màu | ✓ | đã chọn: radio tô kín + viền thẻ + nền trắng, không chỉ đổi màu |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ! | viền radio 4,92 trên nền xám (4,34 rê, 3,68 nhấn) · radio chọn 15,13 (10,26 trên nền nhấn) · viền chọn, vòng focus 15,13. Ranh giới thẻ xám trên trắng 1,10: radio và chữ gánh việc nhận ra |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | vòng 2 cách 2 bao cả thẻ, 15,13:1 (từ Khung thẻ) |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | cả thẻ là đích bấm, thấp nhất 68 |
| 4.1.2 Tên, vai trò | ✓ | nhóm là `radiogroup` có tên; mỗi thẻ `role="radio"`, `aria-checked`; tên = Title, mô tả = Description |
| 2.1.1 Bàn phím | ✓ | Tab vào nhóm, phím mũi tên đổi lựa chọn, Space chọn (mẫu radio group) |
| 2.3.3 Chuyển động | ✓ | không có hiệu ứng chuyển động |
| **Điểm web** | | **9/9 đạt** (! = đạt có điều kiện) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Selected | Biến thể | false | false · true |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Disabled |
| Has Icon | Bật tắt | bật | vòng icon cuối thẻ |
| Has Avatar | Bật tắt | tắt | Base / Avatar MD ở chỗ vòng icon |
| Has Media | Bật tắt | tắt | `.card / Media` SM giữa radio và chữ |
| Has Body | Bật tắt | tắt | hiện Slot Body |
| Body | Slot | 2 × `.card / Row` | tối đa 3; chỉ nhận `.card / Row`, Base / Status Row; cách 8 |
| Title · Description · Has Description | Chữ, bật tắt (của Name, đưa ra panel) | Title · Description · bật | tên phương án, mô tả một ý |
| Vòng icon · Ảnh nhỏ · Avatar | Instance lồng (đưa ra panel) | — | đổi icon, ảnh, chữ cái avatar |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Khung thẻ | `Base / Card` · L1 → xem [tài liệu Card](card.md) | Muted · Padding None · Elevation None; State theo bảng Trạng thái | — |
| Radio | `.card / Radio` · L0 | Off · On · Off Disabled · On Disabled theo Selected, State | — |
| Ảnh nhỏ | `.card / Media` · L0 | SM; Tone Surface khi thẻ xám, Muted khi thẻ trắng; lớp Ảnh thay ảnh thật (ngoại lệ luật e, DEC-237) | Has Media · Ảnh nhỏ |
| Tên | `.card / Name` · L0 | Default · Disabled | Title · Description · Has Description |
| Dòng phụ | Slot Body: `.card / Row` · L0 (Type Icon Text, Label Value, Label, Total); `Base / Status Row` · L1 → xem [tài liệu Status Row](status-row.md) | tối đa 3, cách 8 (preferred values khoá) | Has Body · Body |
| Vòng icon | `.card / Icon Circle` · L0 | Tone Surface · Muted · Disabled theo nền thẻ; icon 20 | Has Icon · Vòng icon |
| Avatar | `Base / Avatar` · L1 → xem [tài liệu Avatar](avatar.md) | MD 36 | Has Avatar · Avatar |

Đưa ra panel (`isExposedInstance`, kiểm 20/10): Name, Vòng icon, Ảnh nhỏ, Avatar.

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components · L0–L3: chưa có component cha dùng (chỉ có instance trong khung tài liệu và khung so
sánh 20/10). Dự kiến: thẻ chọn phương án của L2, vd Vehicle / Option Card (Has Media + Body), chờ user chọn mẫu lab m4 (DEC-237).

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Lề | `layout/card-padding` | 16 |
| Khoảng giữa các phần | `space/gap-md` | 12 |
| Radio · viền · viền khi chọn | `card/radio-size` · `card/radio-ring` · `card/radio-on-ring` | 16 · 1,5 · 5 |
| Title · Description | `type/label` · `type/caption` | 14/20 Medium · 12/16 |
| Title – Description | `card/choice-text-gap` | 2 |
| Body: cách tên, giữa dòng | `space/inset-sm` | 8 |
| Dòng Body (`.card / Row`) | `card/row-min-height` · `card/row-icon-cell` · `space/gap-sm` | 24 · 24 · 8 |
| Vòng icon | `card/lead-size` | 36 · icon 20 |
| Ảnh nhỏ | `card/media-size-sm` · `radius/inner` | 48 · 8 |
| Avatar | Base / Avatar · MD → xem tài liệu Avatar | 36 |
| Khung thẻ (bo, viền, vòng focus) | Base / Card → xem tài liệu Card | — |
| Vùng chạm | `touch/min` | 24 ✓ (thấp nhất 68) |

Màu (collection Component, một bộ cho web và app; bỏ tiền tố `card/`). Nền, viền của thẻ thuộc Khung thẻ (luật g: không lặp token của
L1 lồng):

| Phần | Token | Giá trị |
|---|---|---|
| Nền, viền thẻ | Khung thẻ = Base / Card Muted → xem tài liệu Card | — |
| Radio · viền, chọn | `radio/border` · `radio/on` | neutral/500 · brand/800 |
| Radio, vòng icon · ruột trắng | `color/bg/surface` · `disabled/lead-bg` | trắng · trắng (Disabled) |
| Vòng icon thẻ đã chọn | `lead/bg` | neutral/100 |
| Chữ · Title, Description | `color/text/primary` · `color/text/secondary` | neutral/900 · neutral/500 |
| Chữ phụ · khi rê, khi nhấn | `fg/secondary-hover` · `fg/secondary-pressed` | neutral/600 · neutral/600 |
| Disabled · chữ, viền radio | `disabled/fg` · `color/border/default` | neutral/400 · neutral/200 |
| Icon trong vòng | `color/icon/primary` | neutral/700 |

Tên trong code: `<SelectableCard name value title description selected disabled media avatar icon>{body}</SelectableCard>` trong
`<RadioGroup>`; biến CSS `--card-radio-*`, `--card-choice-*`, `--card-lead-*`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6562:215835 ngày 20/10 (ngưỡng 1,1:1; ô mẫu nền trắng), sau lần sửa cuối. Lớp ngoài của thẻ không
có nền (nền ở lớp con "Khung thẻ") nên script đo ở lớp con cho cả 38 mẫu.

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 20 ô, 20 mẫu (khối Web; cả khung 38 ô, 38 mẫu) | luật A: 0 lỗi |
| Sát ngưỡng (lớp "Khung thẻ") | Trạng thái · Selected=true · Hover | `card/bg/hover` = neutral/100 (#F2F4F7) so với Selected Default trắng 1,10:1: đạt, hết cờ "Giống Default" của bản #F9FAFC 1,04:1 (20/10). Cờ lớp ngoài Hover, Pressed "GIỐNG DEFAULT" 1:1 là báo nhầm (nền nằm ở lớp con "Khung thẻ") |
| ✕ Mất hình (cố ý, lớp "Khung thẻ") | Cảnh · Không nên 2 | cảnh "Không nên": thẻ chưa chọn trên khối `color/bg/muted` 1:1 |
| ⚠ Nền chìm (lớp "Khung thẻ") | Selected=true · Default, Hover, Focus | thẻ trắng trên ô trắng; giữ nhờ viền chọn 15,13:1 |
| Cờ ngoài (lớp ngoài) | Selected=true · Hover, Pressed | "GIỐNG DEFAULT" là báo nhầm: lớp ngoài không fill ở mọi State; số đúng ở lớp "Khung thẻ" (Pressed #D0D5DD = 1,47:1 so với trắng) |
| Sát ngưỡng (lớp "Khung thẻ") | 13 mẫu | 1,10:1: thẻ chưa chọn #F2F4F7 trên trắng; giữ nhờ radio và chữ |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Khi dùng, cấu tạo, Has…, luật:** như web.
- **Khác web:** không Hover; radio 20 (viền 1,5, khi chọn viền 6); Title 15/20 Semi Bold, Description 13/18, cách 4; bo thẻ 16 (từ
  Khung thẻ).

### Cấu tạo

Hình phóng 2× trên Figma: như web, mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Khung thẻ | **Base / Card · Muted · Padding None · Elevation None → xem tài liệu Card** | — |
| Lề · khoảng | `layout/card-padding` · `space/gap-md` | 16 · 12 |
| Radio | `card/radio-size` · `card/radio-ring` · `card/radio-on-ring` | 20 · 1,5 · 6 |
| Tên | `type/label` · `type/caption` · `card/choice-text-gap` | Title 15/20 Semi Bold · Description 13/18 · cách 4 |
| Cột chữ, Slot Body | `space/inset-sm` | 8 |
| Vòng icon · ảnh nhỏ | `card/lead-size` · `card/media-size-sm` · `radius/inner` | 36 · 48 · bo 12 (DEC-259) |
| Avatar | **Base / Avatar · MD → xem tài liệu Avatar** | 36 |

### Biến thể

Như web: 10 biến thể; Hover có trong set nhưng app không dùng.

### Trạng thái

Như web, trừ Hover. Focus: "khi điều hướng bằng bàn phím ngoài hoặc trợ năng".

### Kích thước

| Cấu hình | Cao (Mobile) |
|---|---|
| Không Description (cao theo vòng icon 36) | 68 |
| Mặc định: Title + Description | 74 |
| Has Avatar (avatar 36) | 74 |
| Has Media (ảnh 48) | 80 |
| Has Body · 2 dòng `.card / Row` | 138 |
| Mỗi dòng Body thêm | 32 |

Thấp nhất 68 ≥ `touch/min` 44 ✓ (WCAG 2.5.5).

### Nên và không nên

Như web (cùng hai cặp, mode Mobile).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Title 16,09 trên nền xám · 12,03 nhấn · 17,73 đã chọn. Description 4,92 nền xám · 5,27 nhấn (neutral/600) · 5,43 đã chọn |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn |
| 1.4.1 Dùng màu | ✓ | như web |
| 1.4.11 Tương phản ngoài chữ (AA) | ! | viền radio 4,92 (3,68 nhấn) · radio chọn 15,13 · viền chọn, vòng focus 15,13; ranh giới thẻ 1,10 |
| 2.4.7 · 2.4.13 | ✓ | khi có bàn phím ngoài hoặc công cụ trợ năng |
| 2.5.8 (≥ 24) · 2.5.5 (≥ 44) | ✓ | thấp nhất 68 |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng (như aria-label) = Title; báo "đã chọn, 1 trên n" |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: mũi tên đổi lựa chọn, Space chọn; theo thứ tự focus |
| 2.3.3 Chuyển động | ✓ | không có hiệu ứng chuyển động |
| **Điểm app** | | **9/9 đạt** (! = đạt có điều kiện) |

### Thuộc tính

Như web (cùng bảng); app không dùng Hover.

### Thành phần lồng

Như web (cùng bảng).

### Được dùng trong

Chưa có component cha dùng (L2 chưa dựng).

### Token

Số đo (collection Platform, mode Mobile): lề 16 · khoảng 12 · radio 20 · viền 1,5 · viền khi chọn 6 · chữ `type/label` 15/20 Semi Bold ·
`type/caption` 13/18 · `card/choice-text-gap` 4 · `space/inset-sm` 8 · dòng Body 24 · vòng icon 36 · ảnh nhỏ 48, bo 12 · avatar 36 ·
`touch/min` 44 ✓ (thấp nhất 68).

Màu: như web, bỏ màu rê (`fg/secondary-hover`) vì app không dùng Hover.

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 18 ô, 18 mẫu (khối Mobile) | luật A: 0 lỗi |
| ✕ Mất hình (cố ý, lớp "Khung thẻ") | Cảnh · Không nên 2 | cảnh "Không nên": thẻ chưa chọn trên khối `color/bg/muted` |
| ⚠ Nền chìm (lớp "Khung thẻ") | Selected=true · Default, Focus | thẻ trắng trên ô trắng; giữ nhờ viền chọn 15,13:1 |
| Cờ ngoài (lớp ngoài) | Selected=true · Pressed | "GIỐNG DEFAULT" là báo nhầm như phần Web |
| Sát ngưỡng (lớp "Khung thẻ") | 13 mẫu | 1,10:1, thẻ chưa chọn trên trắng (app không đặt Hover, không có cờ Hover) |

## Đối chiếu Astryx

Nguồn: `SelectableCard` (2611:21422: Selected false · true × State rest · hover · disabled × Elevation none · low · med · high, 24 biến
thể, lề 12, nền trắng viền 1), trang Astryx · Library (chỉ đọc).

| | Astryx | DS v2 | Vì sao |
|---|---|---|---|
| Khớp | trục Selected false · true × State; radio là dấu chọn; bo 12 (web) | giữ nguyên | — |
| Lệch | State rest · hover · disabled | thêm Pressed, Focus (Default thay rest) | app cần Pressed, bàn phím cần Focus (DEC-236) |
| Lệch | trục Elevation | không có; luôn Elevation None qua Khung thẻ Base / Card Muted | thẻ chọn nền xám không bóng (DEC-184, DEC-236) |
| Lệch | chưa chọn nền trắng viền 1 | chưa chọn nền xám `card/choice/bg` không viền; đã chọn nền trắng viền 1 | giữ nhìn đã duyệt (DEC-184, DEC-196) |
| Lệch | lề 12 | lề 16 (`layout/card-padding`) | thang thẻ DS v2 |
| Lệch | nội dung tự do | Has Icon · Has Avatar · Has Media · Has Body + Slot Body (≤ 3, khoá preferred values) | thẻ chọn cần ảnh và thân nhiều dòng (DEC-236) |

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
