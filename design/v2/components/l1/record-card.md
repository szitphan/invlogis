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
  - design/v2/components/l1/status-row.md
  - design/v2/components/l1/status-chip.md
  - design/v2/components/l1/avatar.md
  - design/v2/components/l1/button.md
---

# Base / Record Card

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Record Card` (6442:85850, trang DS · Components ·
> L0–L3, Section `Card · L1 · Component Base` 6444:24203), khung tài liệu `Tài liệu · Record Card` (6562:220123, khối Web
> 6562:220130, khối Mobile 6562:220137) · DEC-211 (khuôn thẻ Invlogis), DEC-233 (luật lồng), DEC-234 (ráp trên Base / Card),
> DEC-235 (Slot Footer, Has Avatar, Status Row), DEC-237 (Has Media), DEC-238 (màu nhấn), DEC-239 (chip SM); giữ DEC-125,
> DEC-177, DEC-192, DEC-209, DEC-210 như đã nêu ở từng mục · ráp trên [Card](card.md), lồng [Status Row](status-row.md),
> [Status Chip](status-chip.md), [Avatar](avatar.md), [Button](button.md)

Một component cho cả web và app, không có biến thể Platform: lề, bo, cỡ chữ, cỡ chip, cỡ nút đọc từ biến collection Platform,
khung chứa đặt mode Web hoặc Mobile thì thẻ tự đổi. Màu (collection Component, tiền tố `card/`) giống nhau ở hai nền tảng. Một
thẻ = **đầu thẻ · Slot Rows · khối liên quan · Slot Footer**, ráp trên khung `Base / Card`. Component không biết nghiệp vụ: chữ
mẫu Title, Subtitle, Value, Label, Status.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Khi dùng:** một bản ghi trong danh sách thẻ (mẫu M2): một thẻ = một bản ghi, chạm thẻ mở màn chi tiết. Chỉ liệt kê nhãn –
  giá trị và dòng tổng thì dùng [Summary Card](summary-card.md); chọn một trong vài phương án thì dùng Selectable Card.
- **Ráp trên Base / Card:** lớp đầu "Khung thẻ" là instance `Base / Card` (Padding None · Elevation Low · Tone Surface) đặt
  tuyệt đối, kéo giãn theo thẻ; khung lo nền, viền, bo, bóng, tick chọn và vòng focus theo State (DEC-234).
- **Vì sao không dùng Slot Content của Base / Card:** Figma không cho gắn Boolean hay Slot vào lớp nằm trong Slot của instance
  lồng. Nếu đổ nội dung vào Slot `Content` của khung, thẻ mất các `Has …` và hai Slot `Rows`, `Footer`. Nên nội dung là con trực
  tiếp của Record Card, Slot `Content` của khung để trống.
- **Thứ tự cố định:** Đầu thẻ → Slot `Rows` → `.card / Related` → Slot `Footer`; tắt phần nào thì thẻ co lại, không để chỗ trống.
- **Đầu thẻ:** [Has Media: `.card / Media` MD | Has Avatar: `Base / Avatar` MD] + `.card / Header` (vòng icon + Title, Subtitle) +
  chip cuối (Has Trailing; Trailing đổi giữa `Base / Status Chip` SM và `Base / Button`). Bật Has Media hoặc Has Avatar thì đặt
  Header Lead = None.
- **Rows:** Slot, tối đa 4, cách 8: `.card / Row` (Icon Text, Label Value) hoặc [`Base / Status Row`](status-row.md); Slot khoá,
  không nhận component khác.
- **Footer:** Slot, 1–2 `Base / Button` cỡ MD (32), canh phải, cách 8; mặc định [Phụ Ghost][Chính Secondary], chữ mặc định "Action" · "Action" (chữ L1 trung tính, đổi ở L2); không đặt Primary
  trong thẻ lặp (DEC-177, DEC-235).
- **Selected:** viền 2px than chì + tick tròn đè góc trên phải (lớp "Tick đang chọn" của khung, `Has Check` của Base / Card
  bật); chỉ dùng trong danh sách chọn nhiều.
- **Chỉ có ở web:** State Hover (nền `card/bg/hover` = neutral/100, chữ phụ neutral/600).
- **Chữ:** Title, Subtitle, Value của dòng một dòng cắt "…"; Value khối liên quan tối đa 2 dòng. Đổi chữ ở panel (instance lộ
  ra), không gõ thẳng lên lớp chữ.
- **Rộng:** mẫu 361; dùng thật đặt Fill theo màn, cao ôm nội dung.

### Cấu tạo

Hình phóng 2× trên Figma (ô 1290 × 868, nền `color/bg/canvas`, Context = Canvas): State=Default · Has Trailing bật · 3 dòng,
dòng 3 đổi sang Base / Status Row · Has Related, Has Footer bật · Has Media, Has Avatar tắt.

| Phần | Token | Giá trị web |
|---|---|---|
| Khung thẻ | **Base / Card · Padding None · Elevation Low · Tone Surface → xem tài liệu Card** (đặt tuyệt đối, Stretch) | nền, viền, bo `radius/card` 12, bóng `elev/1`, tick, vòng focus theo State; không lặp token |
| Khung nội dung | lề `layout/card-padding`; khoảng `space/gap-md` | 16 · 12; rộng mẫu 361, cao ôm nội dung |
| Đầu thẻ | L0 `.card / Header` Lead=Icon: vòng `card/lead-size`, nền `card/lead/bg`; cách chữ `space/gap-md` | 36, icon 20 · 12 |
| Title · Subtitle | L0 `.card / Heading`: `type/heading` `color/text/primary` · `type/caption` `color/text/secondary` | 14/20 · 12/16, một dòng, cắt "…" |
| Ảnh nhỏ (Has Media) | L0 `.card / Media` MD: `card/media-size`, bo `radius/inner` | 64 · 8 |
| Avatar (Has Avatar) | **Base / Avatar · MD → xem tài liệu Avatar** | không lặp token |
| Chip cuối (Has Trailing) | **Base / Status Chip · SM · Soft → xem tài liệu Status Chip**; Trailing đổi sang **Base / Button** | không lặp token |
| Slot Rows | khoảng `space/gap-sm`; tối đa 4 | 8 |
| `.card / Row` | cao tối thiểu `card/row-min-height`; ô icon `card/row-icon-cell`, icon `color/icon/secondary`; Value `type/body` `color/text/primary` | 24 · 24 (icon 16) · 14/20 |
| Dòng trạng thái | **Base / Status Row → xem tài liệu Status Row** | không lặp token |
| `.card / Related` | nền `card/related/bg`, bo `radius/inner`, lề `layout/card-padding`, khoảng icon–chữ `space/gap-lg`; Label `type/caption`, Value `type/body` | 8 · 16 · 16; Value tối đa 2 dòng |
| Slot Footer | **Base / Button · MD · Ghost + Secondary → xem tài liệu Button**; khoảng `card/action-gap` | 1–2 nút, canh phải, cách 8 |
| Tick, vòng focus | lớp của Khung thẻ → xem tài liệu Card | — |

### Biến thể

State 5 biến thể (Default · Hover · Pressed · Focus · Selected); không có trục Size, một mật độ. Phần bật tắt bằng Boolean: Has
Media, Has Avatar, Has Trailing, Has Rows, Has Related, Has Footer. Khung có ba cấu hình mẫu: Đủ phần (mặc định) · Has Avatar +
Status Row · Has Media, tắt Related và Footer.

### Trạng thái

| State | Trông thế nào |
|---|---|
| Default | nền `card/bg/default` (trắng), viền 1px `card/border/default`, bóng `elev/1` (DEC-125) |
| Hover | nền `card/bg/hover` = neutral/100 (1,10:1 so với trắng); chữ phụ `card/fg/secondary-hover` = neutral/600; chỉ web |
| Pressed | nền `card/bg/pressed` = neutral/300, viền `card/border/pressed` = neutral/400, chữ phụ `card/fg/secondary-pressed` = neutral/600, bỏ bóng (DEC-238); khối liên quan giữ nền neutral/100 nên nổi trên nền nhấn |
| Focus | vòng `.focus / Ring` của khung, dày 2 cách 2, bo vòng = bo thẻ + 4; khe theo `focus/gap` (đặt Context=Canvas khi thẻ nằm trên nền xám) |
| Selected | viền 2px `card/border/selected` (brand/800, than chì) + tick `.card / Check` 20 đè góc trên phải (Has Check của khung bật); đang chọn mà focus thì vòng focus chồng lên |

Không có Disabled.

### Kích thước

| Trường hợp | Cao | Cách tính |
|---|---|---|
| Đủ phần (mặc định, 3 dòng) | 292 | 16 + 36 + 12 + 88 + 12 + 68 + 12 + 32 + 16 (lề · đầu thẻ · phần · dòng · phần · khối liên quan · phần · nút · lề) |
| Dòng 3 là Base / Status Row | 292 | Status Row cao 24 (chip MD 24) |
| Has Media, tắt Related và Footer | 196 | 16 + 64 + 12 + 88 + 16 |
| Has Media (đủ phần) | 320 | đầu thẻ 64 (`card/media-size`) thay 36 |
| Mỗi dòng thêm | +32 | 24 + 8 (`card/row-min-height` + `space/gap-sm`), tối đa 4 dòng |
| Vùng chạm | ≥ 24 | thẻ ≥ 196; nút chân thẻ 32 (`touch/min` 24 ✓) |

Một mật độ (Density chưa dựng).

### Nên và không nên

1. **Nên:** chân thẻ [Phụ Ghost][Chính Secondary], canh phải, tối đa 2 nút. **Không nên:** nút Primary trong thẻ lặp của danh
   sách (mỗi vùng chỉ một nút chính, DEC-177).
2. **Nên:** đầu thẻ một hình đại diện: vòng icon, hoặc Has Avatar, hoặc Has Media (bật cái nào thì Header Lead=None). **Không
   nên:** bật cùng lúc ảnh nhỏ, avatar và vòng icon; chữ đầu thẻ bị đẩy hẹp.

### Trợ năng — chấm theo WCAG 2.2

Ô mẫu nền xám `color/bg/canvas`; tương phản tính bằng công thức WCAG trên mã màu token.

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Title 17,73 · chữ phụ 5,43 (rê 7,06 · nhấn 5,27 với neutral/600) · khối liên quan: Value 16,09, Label 4,92 (rê, nhấn 7,06) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | viền chọn 2px 13,73 trên nền xám · tick 15,13 · vòng focus 13,73; viền nghỉ 1,13 trên nền xám là trang trí (thẻ nhận ra nhờ nội dung và bóng) |
| 1.4.1 Dùng màu | ✓ | Selected có tick + viền dày, không chỉ đổi màu; chip có chữ |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | vòng 2px cách 2px, 13,73:1 trên nền xám |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | thẻ ≥ 196; nút chân thẻ 32 |
| 4.1.2 Tên, vai trò | ✓ | thẻ bấm được là link (tiêu đề) hoặc button; nút chân thẻ là đích riêng, không lồng button trong button; Selected: `aria-selected` hoặc checkbox |
| 2.1.1 Bàn phím | ✓ | Tab tới thẻ rồi tới nút chân thẻ; Enter mở; Space chọn (danh sách chọn nhiều) |
| 2.3.3 Chuyển động | ✓ | đổi State chỉ đổi màu, viền; không chuyển động |
| **Điểm web** | | **8/8 đạt** |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Selected |
| Has Media | Bật tắt | tắt | `.card / Media` MD ở đầu thẻ; bật thì đặt Header Lead=None |
| Has Avatar | Bật tắt | tắt | `Base / Avatar` MD ở đầu thẻ; bật thì đặt Header Lead=None |
| Has Trailing | Bật tắt | bật | chip cuối đầu thẻ |
| Trailing | Đổi instance | Base / Status Chip SM | chỉ Base / Status Chip · Base / Button |
| Has Rows | Bật tắt | bật | — |
| Rows | Slot, 1–4 | 3 × `.card / Row` | chỉ `.card / Row` · Base / Status Row (khoá) |
| Has Related | Bật tắt | bật | — |
| Has Footer | Bật tắt | bật | — |
| Footer | Slot, 1–2 | Ghost + Secondary, MD | chỉ Base / Button (khoá) |
| Instance lộ ra | panel | — | Header (Lead, Icon), Heading (Title, Subtitle), Ảnh nhỏ, Avatar, Cuối (chip), Related |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Khung thẻ | `Base / Card` · L1 → xem [tài liệu Card](card.md) | Padding None · Elevation Low · Tone Surface; State theo thẻ; Has Check bật | — (không lộ) |
| Đầu thẻ | `.card / Header` · L0 | Lead Icon · None; Icon đổi | Header |
| Tiêu đề | `.card / Heading` · L0 | Title, Subtitle một dòng | Heading |
| Ảnh nhỏ | `.card / Media` · L0 | Size MD 64 · Tone Muted | Ảnh nhỏ · Has Media |
| Avatar | `Base / Avatar` · L1 → xem [tài liệu Avatar](avatar.md) | MD; Initials · Image | Avatar · Has Avatar |
| Chip cuối | `Base / Status Chip` · L1 → xem [tài liệu Status Chip](status-chip.md) | Size SM; Soft · Dot × 8 Tone; không đè cỡ | Cuối · Has Trailing · Trailing |
| Nút đầu thẻ | `Base / Button` · L1 → xem [tài liệu Button](button.md) | qua Trailing | Trailing |
| Dòng | `.card / Row` · L0 | Icon Text · Label Value | Slot Rows |
| Dòng trạng thái | `Base / Status Row` · L1 → xem [tài liệu Status Row](status-row.md) | chip MD | Slot Rows |
| Khối liên quan | `.card / Related` · L0 | Has Icon; Value tối đa 2 dòng | Related · Has Related |
| Chân thẻ | `Base / Button` · L1 → xem [tài liệu Button](button.md) | MD; Ghost · Secondary; 1–2 nút | Slot Footer · Has Footer |
| Tick | `.card / Check` · L0 (trong khung) | chỉ State=Selected | — |
| Vòng focus | `.focus / Ring` · L0 (trong khung) | chỉ State=Focus | — |

### Được dùng trong

Chưa có component cha dùng. Kiểm `findInstances` 20/10 trên trang DS · Components · L0–L3, bỏ instance trong khung tài liệu:
không component nào chứa Record Card. Thẻ L2 (lệnh vận tải, chuyến, xe, lái xe) sẽ dựng trên khuôn này khi vẽ màn.

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Lề thẻ | `layout/card-padding` | 16 |
| Giữa các phần | `space/gap-md` | 12 |
| Giữa các dòng | `space/gap-sm` | 8 |
| Bo thẻ (khung) | `radius/card` | 12 |
| Viền · viền chọn | `card/border-width` · `card/border-width-selected` | 1 · 2 |
| Vòng icon | `card/lead-size` | 36 |
| Ảnh nhỏ | `card/media-size` | 64 |
| Dòng · ô icon | `card/row-min-height` · `card/row-icon-cell` | 24 · 24 |
| Khối liên quan | `radius/inner` · `layout/card-padding` · `space/gap-lg` | 8 · 16 · 16 |
| Chip đầu thẻ | `chip/height-sm` | 16 |
| Cách nút chân thẻ | `card/action-gap` | 8 |
| Tick | `card/check-size` · `card/check-ring` | 20 · 2 |
| Chữ | `type/heading` · `type/body` · `type/caption` | 14/20 · 14/20 · 12/16 |
| Vòng focus | `focus/width` · `focus/offset` | 2 · 2 |
| Vùng chạm | `touch/min` | 24 ✓ |

Màu (collection Component, một bộ cho web và app): `card/bg/default` → white · `card/bg/hover` → neutral/100 · `card/bg/pressed` →
neutral/300 · `card/border/default` → neutral/200 · `card/border/pressed` → neutral/400 · `card/border/selected` → brand/800 ·
`card/check/bg` → brand/800 · `card/check/fg` → white · `card/lead/bg`, `card/related/bg` → neutral/100 · `color/text/primary` →
neutral/900 · `color/text/secondary` → neutral/500 · `card/fg/secondary-hover`, `card/fg/secondary-pressed` → neutral/600 ·
`color/icon/secondary` → neutral/500 · `color/border/focus` → charcoal/900. Bảng theo State ở Phần máy.

Tên trong code: `<RecordCard state hasMedia hasAvatar hasTrailing hasRows hasRelated hasFooter>` với slot `rows`, `footer`; biến
CSS `--card-*`, `--radius-card`, `--layout-card-padding`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6562:220123 ngày 20/10 (ngưỡng 1,1:1; ô mẫu nền `color/bg/canvas`, Context = Canvas).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 12 ô, 12 mẫu (khối Web; cả khung 23 ô, 23 mẫu) | luật A: 0 lỗi, ô nào cũng có nền riêng và viền mảnh |
| ⚠ Nền chìm (lớp "Khung thẻ") | Trạng thái · Hover | nền #F2F4F7 (`card/bg/hover` = neutral/100) trên nền ô #F2F4F7 = 1:1; hình giữ nhờ viền 1,13:1 |
| Sát ngưỡng (lớp "Khung thẻ") | Trạng thái · Hover | Hover #F2F4F7 so với Default #FFFFFF = 1,10:1: đạt, hết cờ "Giống Default" của bản #F9FAFC 1,04:1 (20/10) |
| Sát ngưỡng (lớp "Khung thẻ") | mọi ô thẻ trắng (Default, Focus, Selected, biến thể, cảnh) | nền thẻ #FFFFFF trên nền ô #F2F4F7 = 1,10:1; hình giữ nhờ viền 1,13:1 và bóng |
| Cờ ngoài (lớp ngoài) | Trạng thái · Hover, Pressed | "GIỐNG DEFAULT" 1:1 là báo nhầm: lớp ngoài của thẻ không fill, nền nằm ở lớp con "Khung thẻ"; Pressed thật là 1,34:1 so với nền ô, 1,47:1 so với Default |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Khi dùng, ráp trên Base / Card, thứ tự, đầu thẻ, Rows, Footer, Selected, chữ, rộng:** như web (cùng cấu tạo, cùng thuộc
  tính).
- **Khác web:** không Hover; bo thẻ 16, bo khối phụ 14; chữ 15/22 (tiêu đề 15/20, phụ 13/18); nút chân thẻ MD 42, cách 12; chip
  đầu thẻ vẫn 16.
- **Đường K app:** chữ đầu thẻ K4 80, chữ dòng K3 64, khối liên quan K2 32 → nội dung 48 (thẻ 361 trên màn 393).

### Cấu tạo

Hình phóng 2× trên Figma: như web, mode Mobile (ô 1290 × 904).

| Phần | Token | Giá trị app |
|---|---|---|
| Khung thẻ | **Base / Card · Padding None · Elevation Low · Tone Surface → xem tài liệu Card** | bo `radius/card` 16; không lặp token |
| Khung nội dung | `layout/card-padding` · `space/gap-md` | 16 · 12 |
| Đầu thẻ | `.card / Header`: `card/lead-size`; cách chữ `space/gap-md` | 36 · 12 |
| Title · Subtitle | `type/heading` · `type/caption` | 15/20 · 13/18 |
| Ảnh nhỏ | `.card / Media` MD: `card/media-size`, bo `radius/inner` | 64 · 14 |
| Avatar · Chip cuối | **Base / Avatar · MD**; **Base / Status Chip · SM · Soft** → xem tài liệu của từng component | không lặp token |
| Slot Rows · `.card / Row` | `space/gap-sm`; `card/row-min-height`; Value `type/body` | 8 · 24 · 15/22 |
| Dòng trạng thái | **Base / Status Row → xem tài liệu Status Row** (cao 26 ở app, chip MD 26) | không lặp token |
| `.card / Related` | `card/related/bg`, `radius/inner`, `layout/card-padding` | 14 · 16; Label 13/18, Value 15/22 |
| Slot Footer | **Base / Button · MD · Ghost + Secondary → xem tài liệu Button**; `card/action-gap` | nút 42, cách 12 |

### Biến thể

Như web: 5 biến thể; Hover có trong set nhưng app không dùng.

### Trạng thái

Như web, trừ Hover. Focus: "khi điều hướng bằng bàn phím ngoài hoặc trợ năng". Không có Disabled.

### Kích thước

| Trường hợp | Cao | Cách tính |
|---|---|---|
| Đủ phần (mặc định, 3 dòng) | 308 | 16 + 38 + 12 + 88 + 12 + 72 + 12 + 42 + 16 (đầu thẻ 38 = 20 + 18; khối liên quan 72 = 16 + 18 + 22 + 16) |
| Dòng 3 là Base / Status Row | 310 | Status Row cao 26 (chip MD 26) |
| Has Media, tắt Related và Footer | 196 | 16 + 64 + 12 + 88 + 16 |
| Has Media (đủ phần) | 334 | đầu thẻ 64 thay 38 |
| Mỗi dòng thêm | +32 | 24 + 8 |
| Vùng chạm | ≥ 44 | thẻ ≥ 196 ✓; nút chân thẻ 42: thiếu 2, code thêm vùng chạm vô hình theo tài liệu Button |

### Nên và không nên

Như web (cùng hai cặp), cỡ app.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Title 17,73 · chữ phụ 5,43 (nhấn 5,27 với neutral/600) · khối liên quan Label 4,92 (nhấn 7,06) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | như web: viền chọn 13,73 · tick 15,13 · vòng focus 13,73 |
| 1.4.1 Dùng màu | ✓ | Selected có tick + viền dày |
| 2.4.7 · 2.4.13 | ✓ | focus khi có bàn phím ngoài hoặc công cụ trợ năng: vòng 2px cách 2px |
| 2.5.8 (≥ 24) · 2.5.5 (≥ 44) | ! | thẻ ≥ 196 ✓; nút chân thẻ MD 42 < 44: code thêm vùng chạm vô hình theo tài liệu Button |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng (như aria-label) gồm tiêu đề + trạng thái chip; nút chân thẻ là đích riêng; chọn thì báo "đã chọn" |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Enter, Space; theo thứ tự focus |
| 2.3.3 Chuyển động | ✓ | như web |
| **Điểm app** | | **8/8 đạt** (2.5.5 có điều kiện) |

### Thuộc tính

Như web (cùng bảng).

### Thành phần lồng

Như web (cùng bảng); nút chân thẻ cỡ MD 42 ở app.

### Được dùng trong

Chưa có component cha dùng (như web).

### Token

Số đo (collection Platform, mode Mobile): lề `layout/card-padding` 16 · giữa phần `space/gap-md` 12 · giữa dòng `space/gap-sm` 8 ·
bo `radius/card` 16 · viền 1 · 2 · `card/lead-size` 36 · `card/media-size` 64 · dòng 24 · 24 · khối liên quan `radius/inner` 14 ·
lề 16 · khoảng 16 · `chip/height-sm` 16 · `card/action-gap` 12 · tick 20 · 2 · chữ 15/20 · 15/22 · 13/18 · vòng focus 2 · 2 ·
`touch/min` 44 (thẻ ✓, nút chân thẻ xem Button). Màu: như web, bỏ nền rê và chữ phụ rê (app không Hover).

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 11 ô, 11 mẫu (khối Mobile) | luật A: 0 lỗi |
| Sát ngưỡng (lớp "Khung thẻ") | mọi ô thẻ trắng | nền thẻ #FFFFFF trên nền ô #F2F4F7 = 1,10:1; giữ hình nhờ viền 1,13:1 và bóng (app không đặt Hover, không có cờ Hover) |
| Cờ ngoài (lớp ngoài) | Trạng thái · Pressed | "GIỐNG DEFAULT" 1:1 là báo nhầm như phần Web: nền nằm ở lớp con "Khung thẻ" |

## Đối chiếu Astryx

Nguồn: `Card` (43:108295), `ClickableCard` (2611:21423), trang Astryx · Library (chỉ đọc). Astryx không có thẻ bản ghi riêng:
Record Card là khuôn Invlogis (DEC-211) ráp trên khung `Base / Card` theo Astryx `Card` + `ClickableCard` (DEC-234).

| | Astryx | DS v2 | Vì sao |
|---|---|---|---|
| Khớp | `ClickableCard`: State Rest · Hover · Pressed · Focused, Elevation none · low · med · high, khung nền + viền + bo + lề | khung `Base / Card` với State, Elevation; Record Card dùng Elevation Low | giữ cấu tạo khung |
| Lệch | Slot `Content` nhận mọi nội dung | nội dung cố định Đầu thẻ → Rows → Related → Footer, con trực tiếp của thẻ; Slot Content của khung để trống | giữ Has … và Slot riêng (Figma không gắn Boolean/Slot vào lớp trong Slot của instance lồng) |
| Lệch | Hover phủ 5%, Pressed phủ 10% + viền đậm | Hover nền neutral/100; Pressed nền neutral/300, viền neutral/400, chữ phụ neutral/600 | DEC-210, DEC-238 |
| Lệch | Focused vòng 2px màu nhấn sát thẻ | vòng `.focus / Ring` 2px cách 2px, khe theo nền | DEC-172, DEC-241 |
| Lệch | Disabled giảm độ mờ 50% | Record Card không có State Disabled (khung Base / Card có, xám không làm mờ theo DEC-174) | chưa chốt có cần Disabled cho thẻ bản ghi |
| Thêm | — | State Selected (viền 2px + tick), chip SM đầu thẻ, khối liên quan, chân thẻ 1–2 nút | thẻ bản ghi M2 cần chọn nhiều và hành động nhanh (DEC-209, DEC-211) |

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần. Nền, viền, bóng nằm ở lớp "Khung thẻ" (Base /
Card, đặt tuyệt đối) nên bộ xuất không tự đọc được (README Mục 13); bảng màu dưới đã làm sạch theo Khung thẻ của từng State.
Chữ của chip và nút là của L1 lồng, không ghi ở đây.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Record Card` (6442:85850) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Has Rows | Bật tắt | bật | — |
| Has Related | Bật tắt | bật | — |
| Has Footer | Bật tắt | bật | — |
| Rows | Slot | — | nhận: .card / Row · Base / Status Row |
| Has Trailing | Bật tắt | bật | — |
| Trailing | Đổi component | Base / Status Chip · Type=Soft, Tone=Gray, Size=SM | nhận: Base / Status Chip · Base / Button |
| Has Avatar | Bật tắt | tắt | — |
| Footer | Slot | — | nhận: Base / Button |
| Has Media | Bật tắt | tắt | — |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Selected |

5 biến thể · trục State.

### Màu theo phần (token)

| State | Nền | Viền | Chữ | Vòng focus | Bóng |
|---|---|---|---|---|---|
| Default | `card/bg/default` | `card/border/default` | `color/text/primary` | — | `elev/1` |
| Hover | `card/bg/hover` | `card/border/default` | `color/text/primary` | — | `elev/1` |
| Pressed | `card/bg/pressed` | `card/border/pressed` | `color/text/primary` | — | — |
| Focus | `card/bg/default` | `card/border/default` | `color/text/primary` | `color/border/focus · dày 2 · khe focus/gap · 2` | `elev/1` |
| Selected | `card/bg/default` | `card/border/selected · dày card/border-width-selected` | `color/text/primary` | — | `elev/1` |

### Số đo theo phần (token)

| Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Khoảng giữa | Bo | Viền |
|---|---|---|---|---|---|---|---|---|
| 292 | 361 | `layout/card-padding` | `layout/card-padding` | `layout/card-padding` | `layout/card-padding` | `space/gap-md` | `radius/card` | `card/border-width` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Title | `type/heading` |
| Subtitle | `type/caption` |
| Value (.card / Row, Related) | `type/body` |
| Label (Related) | `type/caption` |

<!-- auto:end -->
