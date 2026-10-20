---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
  - design/v2/components/l1/avatar.md
---

# Base / Avatar Group

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Avatar Group` (6408:82080, trang DS ·
> Components · L0–L3), khung tài liệu `Tài liệu · Avatar Group` (6474:90239, khối Web 6474:90246, khối Mobile
> 6474:90374) · L0 `.avatar-group / Overflow` 6442:84546 · DEC-205, DEC-242 (lùi đè biến âm, avatar đầu nằm trên, State Focus) · ráp từ L1 [Avatar](avatar.md)

Một component cho cả web và app, không có biến thể Platform. Mỗi "Avatar n" là khung viền trắng 2 lồng **trực tiếp**
instance `Base / Avatar` (đưa ra panel) — không còn L0 `.avatar-group / Item` (xoá 20/10). Cỡ, viền, lùi đè đọc từ biến
collection Platform, cùng số ở hai mode; chữ "+n" đổi theo mode. Phần **Web** và phần **Mobile** mỗi phần tự đứng được.
Token của avatar con thuộc [Avatar](avatar.md), không lặp ở đây.

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Dùng khi:** nhiều người cùng gắn với một bản ghi, chỗ hẹp: người phụ trách, người đã xem, nhóm thành viên.
- **Count:** hiện tối đa **4** avatar (2 · 3 · 4). Nhiều hơn thì 4 avatar đầu + ô **"+n"**, n = số còn lại (6 người →
  4 avatar + "+2") (DEC-205).
- **Overflow:** bật tắt ô "+n"; chữ ở `Text` của instance con. Ô "+n" bấm được thì mở danh sách đủ người; Focus: vòng `.focus / Ring` bao riêng ô "+n".
- **Cỡ web:** SM 28 hàng bảng · MD 40 dòng danh sách, thẻ · LG 52 đầu trang, sheet (cao nhóm = cỡ avatar 24 · 36 · 48 +
  2 × viền 2). Kéo ra mặc định SM.
- **Chữ "+n" web:** SM 12/16 · MD 14/20 Medium · LG 17/24.
- **Chỉ có ở web:** Tooltip từng avatar con: rê chuột hoặc focus thấy tên ("Họ tên"), bật ở instance con.
- **Ráp từ L1:** mỗi "Avatar n" là khung viền trắng lồng trực tiếp instance Base / Avatar, đưa ra panel để đổi ảnh, chữ
  viết tắt, icon, Status.
- **Lùi đè:** avatar sau lùi vào đè avatar trước ¼ đường kính: khoảng giữa là biến âm `avatar/group-overlap/*` = −6 · −8 ·
  −12 (SM · MD · LG). Avatar đầu nằm trên (đảo thứ tự lớp, `itemReverseZIndex`) nên chấm trạng thái của avatar không bị che.
- **Không đè** cỡ, nền, viền của avatar con; không bật Edit trong nhóm. Ô "+n": dấu cộng và số, không khoảng trắng ("+3").

### Cấu tạo

Hình phóng 2× trên Figma: Size MD · Count 3 · bật Overflow.

| Phần | Token | Giá trị web |
|---|---|---|
| Avatar con | **Base / Avatar · cỡ theo Size → xem [tài liệu Avatar](avatar.md)** (L1 lồng, không lặp token); đổi Content, Initials, Icon, Status, Tooltip trên instance con | SM 24 · MD 36 · LG 48 |
| Khung viền "Avatar n" | khung thường, không phải L0: lề `avatar/ring` bốn phía, nền `color/bg/surface`, bo `radius/chip` | 2 |
| Lùi đè | khoảng giữa = `avatar/group-overlap/*` (biến âm, gắn vào `itemSpacing`); avatar đầu nằm trên avatar sau (`itemReverseZIndex`) | −6 · −8 · −12 |
| Cao nhóm | `avatar/size/*` + 2 × `avatar/ring`; rộng ôm nội dung | 28 · 40 · 52 |
| Bo | `radius/chip` | tròn hẳn (9999) |
| Ô +n | L0 `.avatar-group / Overflow`, bật bằng Overflow; cỡ `avatar/size/*`, nền `avatar/overflow/bg`, viền `avatar/ring`; chữ `avatar/overflow/fg` `type/caption-strong` · `label` · `title-3`; chữ ở Text (instance lồng); State=Focus: `.focus / Ring` bao riêng ô tròn (ô bấm được ở web), nền vòng `avatar/overflow/bg` | 24 · 36 · 48; chữ 12/16 · 14/20 Medium · 17/24 |

### Biến thể

Count × Overflow (Size MD): Overflow bật · Overflow tắt · đổi avatar con trên instance (Avatar 1 = Icon, Avatar 2 bật
Status Busy). 18 biến thể = Size 3 × Count 3 × State 2 (Default, Focus).

### Trạng thái

Có hai State: Default và Focus. Avatar con giữ trạng thái của [Avatar](avatar.md): Status; Tooltip "Họ tên" khi rê chuột;
avatar con không có Focus riêng.

| State | Trông thế nào |
|---|---|
| Default | như hình Cấu tạo |
| Focus (web) | chỉ ô "+n" là phần bấm được: vòng `.focus / Ring` (khe `focus/gap`, vòng `color/border/focus`) bao riêng ô tròn; chọn State=Focus ở instance con `.avatar-group / Overflow` |
| Focus (nhóm) | State=Focus của Base / Avatar Group: vòng bao cả nhóm, đặt cuối danh sách con để nằm dưới avatar — dùng cho app (xem phần Mobile) |

Trên Figma vòng "+n" bị avatar trước che vài px ở cung trái (đảo thứ tự lớp để chấm Status không bị che); khi lập trình
nâng `z-index` của phần tử đang focus. Không có Hover, Pressed.

### Kích thước

| Size | Cao nhóm | Avatar con | Lùi đè | Rộng Count 4 + ô +n | Chữ "+n" | Dùng khi |
|---|---|---|---|---|---|---|
| SM | 28 | 24 | −6 | 116 | 12/16 | hàng bảng |
| MD | 40 | 36 | −8 | 168 | 14/20 Medium | dòng danh sách, thẻ |
| LG | 52 | 48 | −12 | 212 | 17/24 | đầu trang, sheet |

Mọi cỡ ≥ `touch/min` 24.

### Nên và không nên

1. **Nên:** 6 người → 4 avatar + "+2", gọn trong một dòng. **Không nên:** tắt "+n" khi còn người (người xem tưởng chỉ có
   4 người).
2. **Nên:** rê chuột lên từng avatar con thấy tên (bật Tooltip ở instance con). **Không nên:** không có cách nào biết tên
   (không tooltip, bấm "+n" không mở danh sách).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | "+n" `avatar/overflow/fg` trên `avatar/overflow/bg`: 4,92 · chữ viết tắt như Avatar ≥ 8,30 |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ! | nền ô "+n" so với nền trắng 1,10: ô nhận ra nhờ chữ "+n" (như nền nút Secondary); avatar con giữ hình nhờ nền 1,19 hoặc ảnh |
| 1.1.1 Nội dung không phải chữ | ✓ | cả nhóm một `aria-label` liệt kê tên ("Họ tên, Họ tên và 2 người khác"); từng avatar ẩn khỏi trình đọc |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ | Tooltip avatar con: Esc đóng được, rê lên tooltip không tắt (xem [Tooltip](tooltip.md)) |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ! | State Focus ở ô "+n" (web chỉ ô này bấm được): vòng `.focus / Ring` 2 cách 2 (khe `focus/gap`), bao riêng ô tròn. Trên Figma vòng bị avatar trước che vài px cung trái (đảo thứ tự lớp) → khi lập trình nâng `z-index` phần tử đang focus |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | ô "+n" SM 24 (kèm viền 28) · MD 36 · LG 48 |
| 4.1.2 Tên, vai trò | ✓ | ô "+n" là nút có tên ("Xem thêm 2 người") |
| 2.1.1 Bàn phím | ✓ | Tab tới ô "+n"; Enter, Space mở danh sách |
| **Điểm web** | | **8/8 đạt** (2 có điều kiện !) · lưu ý: nâng `z-index` phần tử đang focus khi lập trình |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Size | Biến thể | SM | SM 28 · MD 40 · LG 52 (cao nhóm) |
| Count | Biến thể | 2 | 2 · 3 · 4 avatar |
| State | Biến thể | Default | Default · Focus (web: Focus ở ô "+n", chọn State của instance con Overflow) |
| Overflow | Bật tắt | bật | ô "+n" cuối nhóm |
| Avatar 1–4 › Base / Avatar | Instance lồng | Image, Initials xen kẽ | Content, Initials, Icon, Status, Tooltip; không bật Edit |
| Overflow › Text | Instance lồng | +3 | "+n", n = số người còn lại |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Avatar 1–4 | **Base / Avatar · L1 → xem [tài liệu Avatar](avatar.md)** | cỡ theo Size nhóm (SM 24 · MD 36 · LG 48); Content Image · Initials · Icon; Status, Tooltip được bật; không bật Edit; không đè cỡ, nền, viền | Content, Initials, Icon, Status, Tooltip (instance lồng) |
| Khung "Avatar n" | khung thường (không phải L0) | lề `avatar/ring` 2, nền `color/bg/surface`, bo `radius/chip`; không sửa | — |
| Ô +n | `.avatar-group / Overflow` · L0 | Size theo nhóm; State Default · Focus (Focus chọn ở instance con); bật bằng Overflow | Text (chữ "+n") |
| Vòng focus | `.focus / Ring` · L0 | chỉ khi State=Focus; bao riêng ô "+n" (web); Tone Default | — |

### Được dùng trong

Kiểm `getInstancesAsync` 20/10 trên toàn file: chỉ có instance trong khung tài liệu (đã lọc bỏ). **Chưa có component cha
dùng.**

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | SM | MD | LG |
|---|---|---|---|---|
| Avatar con | `avatar/size/*` | 24 | 36 | 48 |
| Viền | `avatar/ring` | 2 | 2 | 2 |
| Vòng focus | `focus/width` · `focus/offset` · khe `focus/gap` | 2 · 2 | 2 · 2 | 2 · 2 |
| Cao nhóm | `avatar/size/*` + 2 × `avatar/ring` | 28 | 40 | 52 |
| Lùi đè (khoảng giữa) | `avatar/group-overlap/*` (biến âm, gắn `itemSpacing`) | −6 | −8 | −12 |
| Rộng Count 4 + ô +n | ôm nội dung | 116 | 168 | 212 |
| Ô +n | `avatar/size/*` | 24 | 36 | 48 |
| Chữ +n | `type/caption-strong` · `label` · `title-3` | 12/16 | 14/20 Medium | 17/24 |
| Bo | `radius/chip` | tròn | tròn | tròn |
| Vùng chạm (cả nhóm) | `touch/min` | 24 ✓ | 24 ✓ | 24 ✓ |

Màu (collection Component, một bộ cho web và app):

| Phần | Token | Giá trị |
|---|---|---|
| Viền khung "Avatar n", viền ô +n | `color/bg/surface` | = white · #FFFFFF |
| Nền ô +n | `avatar/overflow/bg` | = color/bg/muted · #F2F4F7 |
| Chữ ô +n | `avatar/overflow/fg` | = color/text/secondary · #5F6B7A |
| Avatar con | Base / Avatar → xem [tài liệu Avatar](avatar.md) | — |

Tên trong code: `<AvatarGroup size="sm|md|lg" max={4} people={[{ name, src, status }]} />` — tự tính "+n" khi
`people.length > max`; biến CSS `--avatar-ring`, `--avatar-group-overlap-*` (giá trị âm, dùng cho `margin-left`/`gap` của avatar sau), `--avatar-overflow-*`,
`--focus-*`; phần tử đang focus nâng `z-index`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6474:90239 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 23 ô, 23 mẫu (khối Web; thêm ô Focus ở lưới Trạng thái) | 0 lỗi A: ô nào cũng có nền thật trắng và viền mảnh |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có |
| ⚠ Nền chìm | — | không có; gốc instance nhóm "không nền" (viền trắng nằm ở khung con) nên máy không chấm viền trắng trên ô trắng — viền chỉ để tách avatar, hình nhóm giữ nhờ nền avatar 1,19 và ảnh |
| Sát ngưỡng | — | không có |
| Lớp con (mở rộng script) | 23 cờ lớp "Avatar 1" | 22 ✕ MẤT HÌNH: khung viền trắng `avatar/ring` trắng trên ô trắng — viền trắng chỉ để tách avatar, hình giữ nhờ ảnh, nền avatar 1,19; 1 ⚠ NỀN CHÌM Count 3 · Focus: giữ hình nhờ vòng focus 15,13:1 |

Không có ô nền xám.

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Dùng khi, Count, Overflow, Ráp từ L1, Lùi đè, Không đè:** như phần Web.
- **Cỡ app:** SM 28 · MD 40 · LG 52 (cao nhóm = cỡ avatar 24 · 36 · 48 + 2 × viền 2). Kéo ra mặc định SM.
- **Chữ "+n" app:** SM 13/18 · MD 15/20 Semi Bold · LG 17/22.
- **Khác web:** không Tooltip; bấm vào cả nhóm mở danh sách đủ người; cả nhóm là một vùng bấm ≥ `touch/min` 44 (SM 28,
  MD 40 thêm vùng chạm vô hình). Focus (khi có bàn phím ngoài hoặc trợ năng): vòng `.focus / Ring` bao cả nhóm.

### Cấu tạo

Hình phóng 2× trên Figma: Size MD · Count 3 · bật Overflow; viền chấm tím = vùng chạm của cả nhóm.

| Phần | Token | Giá trị app |
|---|---|---|
| Avatar con | **Base / Avatar · cỡ theo Size → xem [tài liệu Avatar](avatar.md)**; đổi Content, Initials, Icon, Status trên instance con | SM 24 · MD 36 · LG 48 |
| Khung viền "Avatar n" | khung thường: lề `avatar/ring`, nền `color/bg/surface`, bo `radius/chip` | 2 |
| Lùi đè | `avatar/group-overlap/*` (biến âm, gắn `itemSpacing`); avatar đầu nằm trên avatar sau (`itemReverseZIndex`) | −6 · −8 · −12 |
| Cao nhóm | `avatar/size/*` + 2 × `avatar/ring` | 28 · 40 · 52 |
| Ô +n | L0 `.avatar-group / Overflow`; chữ `type/caption-strong` · `label` · `title-3` | 24 · 36 · 48; chữ 13/18 · 15/20 Semi Bold · 17/22 |
| Vùng chạm | `touch/min` | 44: cả nhóm là một vùng bấm; SM +8/phía, MD +2/phía vùng chạm vô hình |
| Vòng focus | State=Focus của nhóm: `.focus / Ring` bao cả nhóm, đặt cuối danh sách con để nằm dưới avatar | khe `focus/gap`, vòng 2 · 2 |

### Biến thể

Như web; 18 biến thể dùng chung (Size 3 × Count 3 × State 2).

### Trạng thái

Có hai State: Default và Focus. App không dùng Hover, không Tooltip. Avatar con giữ Status của Avatar, không có Focus riêng.

| State | Trông thế nào |
|---|---|
| Default | như hình Cấu tạo |
| Focus | khi điều hướng bằng bàn phím ngoài hoặc trợ năng: cả nhóm là vùng bấm; State=Focus của nhóm, vòng `.focus / Ring` bao cả nhóm, đặt cuối danh sách con để nằm dưới avatar (không bị che) |

Chưa có Pressed.

### Kích thước

| Size | Cao nhóm | Avatar con | Lùi đè | Chữ "+n" | Vùng chạm | Dùng khi |
|---|---|---|---|---|---|---|
| SM | 28 | 24 | −6 | 13/18 | +8/phía → 44 | chỗ dày |
| MD | 40 | 36 | −8 | 15/20 Semi Bold | +2/phía → 44 | dòng danh sách, thẻ |
| LG | 52 | 48 | −12 | 17/22 | đủ | đầu trang, sheet |

### Nên và không nên

1. **Nên:** 6 người → 4 avatar + "+2". **Không nên:** tắt "+n" khi còn người.
2. **Nên:** cả nhóm là một vùng bấm ≥ 44, mở danh sách đủ tên. **Không nên:** nhóm không bấm được trên app (không có cách
   nào biết tên).

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | "+n" 4,92 · chữ viết tắt như Avatar ≥ 8,30 |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ! | nền ô "+n" so với nền trắng 1,10: nhận ra nhờ chữ "+n" |
| 1.1.1 Nội dung không phải chữ | ✓ | cả nhóm một nhãn trợ năng liệt kê tên ("Họ tên, Họ tên và 2 người khác") |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | khi điều hướng bằng bàn phím ngoài hoặc trợ năng: State Focus bao cả nhóm — vòng `.focus / Ring` 2 cách 2 (khe `focus/gap`) đặt cuối danh sách con nên nằm dưới avatar, không bị che |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | cả nhóm là vùng bấm: SM 28 · MD 40 · LG 52 |
| 2.5.5 Kích thước đích (AAA, ≥ 44) | ! | SM 28, MD 40: code thêm vùng chạm vô hình 44 (+8, +2/phía); LG 52 đạt |
| 4.1.2 Tên, vai trò | ✓ | cả nhóm là nút có nhãn trợ năng, bấm mở danh sách |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Enter, Space mở danh sách; theo thứ tự focus |
| **Điểm app** | | **8/8 đạt** (2 có điều kiện !) |

### Thuộc tính

Như web (thêm thuộc tính State: Default · Focus, app: Focus bao cả nhóm); khác: Tooltip của avatar con không dùng trên app.

### Thành phần lồng

Như web; avatar con không bật Tooltip trên app. Vòng focus (`.focus / Ring` · L0) chỉ khi State=Focus của nhóm, bao cả nhóm.

### Được dùng trong

Chưa có component cha dùng (kiểm 20/10).

### Token

Số đo (collection Platform, mode Mobile):

| Phần | Token | SM | MD | LG |
|---|---|---|---|---|
| Avatar con | `avatar/size/*` | 24 | 36 | 48 |
| Viền | `avatar/ring` | 2 | 2 | 2 |
| Vòng focus | `focus/width` · `focus/offset` · khe `focus/gap` | 2 · 2 | 2 · 2 | 2 · 2 |
| Cao nhóm | `avatar/size/*` + 2 × `avatar/ring` | 28 | 40 | 52 |
| Lùi đè (khoảng giữa) | `avatar/group-overlap/*` (biến âm, gắn `itemSpacing`) | −6 | −8 | −12 |
| Rộng Count 4 + ô +n | ôm nội dung | 116 | 168 | 212 |
| Ô +n | `avatar/size/*` | 24 | 36 | 48 |
| Chữ +n | `type/caption-strong` · `label` · `title-3` | 13/18 | 15/20 Semi Bold | 17/22 |
| Bo | `radius/chip` | tròn | tròn | tròn |
| Vùng chạm (cả nhóm) | `touch/min` | 44: +8/phía | 44: +2/phía | 44 ✓ |

Màu: như bảng màu phần Web.

Tên trong code: cùng component `AvatarGroup` với web; cả nhóm bấm được, bắt buộc nhãn trợ năng.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6474:90239 ngày 20/10.

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 22 ô, 22 mẫu (khối Mobile; thêm ô Focus ở lưới Trạng thái) | 0 lỗi A |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có |
| ⚠ Nền chìm | — | không có (gốc instance "không nền", như web) |
| Sát ngưỡng | — | không có |
| Lớp con (mở rộng script) | 22 cờ lớp "Avatar 1" | như khối Web: 21 ✕ khung viền trắng `avatar/ring` trắng trên ô trắng; 1 ⚠ Count 3 · Focus giữ hình nhờ vòng focus 15,13:1 |

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Avatar Group` (6408:82080) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Overflow | Bật tắt | bật | — |
| Size | Biến thể | SM | SM · MD · LG |
| Count | Biến thể | 2 | 2 · 3 · 4 |
| State | Biến thể | Default | Default · Focus |

18 biến thể · trục Size × Count × State.

### Màu theo phần (token)

| State | Nền | Vòng focus |
|---|---|---|
| Default | `color/bg/surface` | — |
| Focus | `color/bg/surface` | `color/border/focus · dày 2 · khe focus/gap · 2` |

### Số đo theo phần (token)

| Size | Cao | Rộng | Lề trái | Lề phải | Lề trên | Lề dưới | Khoảng giữa | Bo |
|---|---|---|---|---|---|---|---|---|
| SM | 28 | ôm nội dung | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/group-overlap/sm` | `radius/chip` |
| MD | 40 | ôm nội dung | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/group-overlap/md` | `radius/chip` |
| LG | 52 | ôm nội dung | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/ring` | `avatar/group-overlap/lg` | `radius/chip` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Initials (SM) | `type/caption-strong` |
| Initials (MD) | `type/label` |
| Initials (LG) | `type/title-3` |
| Số còn lại (SM) | `type/caption-strong` |
| Số còn lại (MD) | `type/label` |
| Số còn lại (LG) | `type/title-3` |

<!-- auto:end -->
