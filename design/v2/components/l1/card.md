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
  - design/v2/components/l1/selectable-card.md
  - design/v2/components/l1/record-card.md
  - design/v2/components/l1/summary-card.md
---

# Base / Card

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / Card` (6457:22918, 136 biến thể, trang DS · Components ·
> L0–L3, Section `Card · L1 · Component Base` 6444:24203), L0 kèm theo `.card / Check` (6426:82241), `.card / Heading` (set 6575:28555, State Default · Disabled),
> `.card / Media` (6507:208231) · khung tài liệu `Tài liệu · Card` (6562:213228, khối Web 6562:213235, khối Mobile 6562:213242) ·
> DEC-234 (Base / Card), DEC-237 (Dashed, Has Check, `.card / Media`), DEC-238 (màu nhấn, rê), DEC-233 (luật lồng), DEC-241 (Context, bỏ ở DEC-258), DEC-247 (Hover thẻ, Disabled giữ viền, Heading Disabled) ·
> theo Astryx `Card` 43:108295 + `ClickableCard` 2611:21423

Một component cho cả web và app, không có biến thể Platform: bo thẻ, cỡ chữ của nội dung mặc định đọc từ biến collection Platform,
khung chứa đặt mode Web hoặc Mobile thì thẻ tự đổi. Màu (collection Component, tiền tố `card/`) giống nhau ở hai nền tảng. Một thẻ =
**khung** (nền, viền, bo, lề, bóng, tick chọn, vòng focus) + **Slot Content** nhận mọi phần. Component không biết nghiệp vụ: chữ mẫu
Title, Subtitle. Mọi ô mẫu nền trắng: nền trang web và app đều trắng (DEC-258).

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Khung thẻ:** nền, viền, bo, lề, bóng, tick chọn, vòng focus; nội dung đặt trong Slot `Content` (mặc định `.card / Heading`:
  Title + Subtitle).
- **Tone Surface:** nền trắng, viền 1px, mặc định; đặt trên nền trang trắng (mặc định của mọi màn, DEC-258).
- **Tone Muted:** nền xám `card/choice/bg`, không viền, không bóng (chỉ Elevation None); đặt trên nền trắng, không đặt trên khối `color/bg/muted`.
- **Tone Dashed:** nền trắng, viền đứt 1px nét 4/4; thẻ của đối tượng chưa tồn tại hoặc đã huỷ (DEC-237).
- **Content (Slot):** nhận chữ, ảnh, component; các phần cách `space/gap-md` 12; Slot không cắt nội dung để vòng focus của nút bên
  trong còn nguyên.
- **Padding:** None 0 · Compact 12 · Default 16 · Spacious 24.
- **Elevation:** None · Low (`elev/1`, mặc định) · Med (`elev/2`) · High (`elev/3`); Pressed, Disabled bỏ bóng.
- **Chỉ có ở web:** State Hover (Surface, Muted, Dashed) và Selected Hover (Muted).
- **Luật:**
  - Muted chỉ trên nền trắng: trên khối `color/bg/muted` thẻ xám mất ranh giới; ở đó dùng Surface.
  - Selected Hover, Selected Pressed, Selected Focus chỉ có ở Muted; Surface chỉ có Selected (viền 2px + tick).
  - Dashed không có Selected, Disabled: khi chọn thì chuyển sang Surface Selected viền đặc.
  - Has Check: tắt tick khi góc trên phải đã có nhãn khác (vd ghim của thẻ L2).
  - Đổi chữ qua thuộc tính: Title, Subtitle của `.card / Heading` sửa ở panel.

### Cấu tạo

Hình phóng 2× trên Figma: Tone Surface · State Selected · Padding Default · Elevation Low, rộng 200, Slot Content mặc định
`.card / Heading`; nền ô trắng (DEC-258).

| Phần | Token | Giá trị web |
|---|---|---|
| Khung thẻ | `card/bg/default` · `card/border/default` · `card/border-width` | nền trắng · viền 1px neutral/200 |
| Bo | `radius/card` | 12 |
| Lề | `layout/card-padding` (Default) · `card/padding-compact` · `card/padding-spacious` · `card/padding-none` | 16 · 12 · 24 · 0 |
| Bóng | effect style `elev/1` · `elev/2` · `elev/3` | Low 0 1 2 · Med 0 4 12 + 0 1 3 · High 0 16 40 + 0 4 12 |
| Viền chọn | `card/border-width-selected` · `card/border/selected` | 2px · brand/800 #262626 |
| Slot Content | `space/gap-md` | các phần cách 12, không cắt |
| Tick chọn | L0 `.card / Check`: `card/check-size` · `card/check-ring` · `card/check/bg` · `card/check/fg` · `card/check/border` | 20 · viền trắng 2 · lệch −6 ra ngoài góc trên phải |
| Chữ mặc định | L0 `.card / Heading`: `type/heading` · `type/caption`; `color/text/primary` · `color/text/secondary` | Title 14/20 · Subtitle 12/16 |
| Vòng focus | L0 `.focus / Ring`: `focus/width` · `focus/offset` · `color/border/focus` · `focus/gap` | 2 · 2 · khe = nền trang trắng (DEC-258) |

### Biến thể

State × Padding × Elevation × Tone = 136 biến thể: Surface 96 (6 State × 4 Padding × 4 Elevation) · Muted 36 (9 State × 4 Padding,
chỉ Elevation None) · Dashed 4 (Padding None, Elevation None, State Default · Hover · Pressed · Focus). Thêm Boolean Has Check (tick
của Surface Selected). Dashed chỉ có Padding None vì dùng làm Khung thẻ, lề do thẻ cha đặt.

### Trạng thái

| State | Surface | Muted | Dashed |
|---|---|---|---|
| Default | nền trắng, viền 1px, bóng theo Elevation | nền `card/choice/bg` | nền trắng, viền đứt |
| Hover (web) | nền `card/bg/hover`, chữ phụ `card/fg/secondary-hover` | nền `card/choice/bg-hover` | nền `card/bg/hover`, giữ viền đứt |
| Pressed | nền `card/bg/pressed` (neutral/300), viền `card/border/pressed`, chữ phụ `card/fg/secondary-pressed`, bỏ bóng | nền `card/choice/bg-pressed` | nền `card/bg/pressed`, viền nhấn đứt |
| Focus | vòng 2 cách 2 (`.focus / Ring`), khe theo `focus/gap` | như Surface, khe trùng nền ô | như Surface |
| Selected | viền 2px `card/border/selected` + tick `.card / Check` | nền trắng, viền 1px, không tick | không có (chọn → Surface Selected) |
| Selected Hover · Pressed · Focus | — | nền `card/bg/hover` · `card/bg/pressed` · trắng + vòng; cùng viền chọn 1px | — |
| Disabled | nền `card/disabled/bg`, viền 1px `card/border/default`, bỏ bóng | nền `card/disabled/bg`, viền 1px `card/border/default` | không có |

- Chữ trong Slot không tự xám khi Disabled: `.card / Heading` có State Disabled (Title, Subtitle màu `card/disabled/fg`, DEC-174), thẻ Disabled dùng sẵn; nội dung khác tự đặt màu Disabled hoặc dùng State Disabled của component con. Viền Disabled `card/border/default` 1,13:1 trên nền Disabled.
- Khe focus `color/focus/gap` = nền trang trắng (DEC-258).

### Kích thước

Rộng theo chỗ đặt (Fill hoặc cố định); cao ôm nội dung. Cao đo với `.card / Heading`, viền 1px:

| Padding | Token | Web | Cao với Heading |
|---|---|---|---|
| None | `card/padding-none` | 0 | 38 |
| Compact | `card/padding-compact` | 12 | 62 |
| Default | `layout/card-padding` | 16 | 70 (mặc định) |
| Spacious | `card/padding-spacious` | 24 | 86 |

Selected cao thêm 2 (viền 2px). Mọi cao ≥ `touch/min` 24 (WCAG 2.5.8).

### Nên và không nên

1. **Nên:** Muted trên nền trắng (sheet, form): thẻ xám tách khỏi nền. **Không nên:** Muted trên khối `color/bg/muted`: thẻ trùng nền,
   mất ranh giới; ở đó dùng Surface.
2. **Nên:** đang chọn có viền 2px và tick góc trên phải, không chỉ dựa vào màu viền. **Không nên:** tắt Has Check khi góc trên phải
   không có nhãn khác: chọn chỉ còn viền.

### L0 của họ thẻ

- **`.card / Check`:** tick đang chọn, vòng 20 (`card/check-size`) nền `card/check/bg`, viền trắng 2 (`card/check-ring`,
  `card/check/border`), icon check 14 màu `card/check/fg`; Absolute ở góc trên phải, lệch −6 ra ngoài thẻ; chỉ ở Surface Selected, bật
  tắt bằng Has Check; không dùng riêng.
- **`.card / Heading`:** nội dung mặc định của Slot Content: Title (`type/heading` 14/20, `color/text/primary`) + Subtitle
  (`type/caption` 12/16, `color/text/secondary`), sát nhau; Has Subtitle bật tắt; State Default · Disabled (Disabled: Title, Subtitle màu `card/disabled/fg`); thay được bằng phần khác.
- **`.card / Media`:** ảnh nhỏ trong thẻ, Size SM 48 (`card/media-size-sm`, thẻ chọn) · MD 64 (`card/media-size`, đầu Record Card);
  bo `radius/inner` 8; ô chờ có icon máy ảnh 24. Tone Muted (nền `card/lead/bg`, đặt trên thẻ trắng) · Surface (nền trắng, đặt trên
  thẻ xám Muted, đang nhấn hoặc Disabled). **Ngoại lệ luật lồng (e):** lớp `Ảnh` là nội dung, thẻ L2 thay paint của lớp `Ảnh` bằng ảnh
  thật (cắt vừa khung) rồi ẩn icon; không đổi bo, cỡ (DEC-237). Chỉ dùng qua Has Media của Record Card và Selectable Card.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Nội dung mặc định `.card / Heading`: Title 17,73 trên trắng · 16,09 khi rê · 12,03 khi nhấn · 16,09 trên Muted · 14,18 Muted rê. Subtitle 5,43 · rê 7,06 và nhấn 5,27 (chữ phụ neutral/600) · Muted 4,92 · Muted rê 6,22 |
| 1.4.3 ngoại lệ — Disabled | ✓ | `card/disabled/fg` 2,34 trên nền Disabled: được miễn; chữ trong Slot không tự xám |
| 1.4.1 Dùng màu | ✓ | Surface Selected có tick + viền 2px; Muted Selected đổi nền trắng và hiện viền 1px; thẻ chọn một dùng thêm radio (Selectable Card) |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ! | viền chọn, tick, vòng focus 15,13 trên nền trắng. Ranh giới thẻ: viền 1,25 trên trắng · Muted trên trắng 1,10 · viền đứt 1,47; nội dung trong thẻ gánh việc nhận ra |
| 2.4.7 Focus thấy được (AA) · 2.4.13 (AAA) | ✓ | vòng 2 cách 2, 15,13:1; khe `focus/gap` |
| 2.5.8 Kích thước đích (AA, ≥ 24) | ✓ | thẻ thấp nhất 38 (Padding None) |
| 4.1.2 Tên, vai trò | ✓ | thẻ bấm được là `button` hoặc `link` có tên; chọn thì `aria-pressed` / `aria-selected`; nút trong Slot là đích riêng, không lồng `button` trong `button` |
| 2.1.1 Bàn phím | ✓ | Enter, Space; thứ tự Tab theo thứ tự đọc |
| 2.3.3 Chuyển động | ✓ | không có hiệu ứng chuyển động |
| **Điểm web** | | **9/9 đạt** (! = đạt có điều kiện) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Tone | Biến thể | Surface | Surface · Muted · Dashed |
| State | Biến thể | Default | Default · Hover · Pressed · Focus · Selected · Disabled · Selected Hover · Selected Pressed · Selected Focus (ba cái cuối chỉ Muted) |
| Padding | Biến thể | Default | Default · Compact · Spacious · None (Dashed chỉ None) |
| Elevation | Biến thể | Low | Low · None · Med · High (Muted, Dashed chỉ None) |
| Has Check | Bật tắt | bật | tick của Surface Selected |
| Content | Slot | `.card / Heading` | nhận mọi phần (chữ, ảnh, component); không cắt |

### Thành phần lồng

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Tick chọn | `.card / Check` · L0 | chỉ ở Surface Selected | Has Check |
| Vòng focus | `.focus / Ring` · L0 | Tone Default; State Focus, Selected Focus; bo theo `radius/card` | — |
| Nội dung mặc định | `.card / Heading` · L0 (trong Slot Content) | Title, Subtitle, Has Subtitle; thay được bằng phần khác | Content (Slot) |
| Icon tick | icon check 14 (trong `.card / Check`) | cố định | — |

Base / Card không chứa L1 nào; ngược lại các thẻ L1 chứa Base / Card (dưới).

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components · L0–L3: 16 instance trong 3 component cha, đều ở lớp "Khung thẻ" (bỏ instance trong
khung tài liệu và khung so sánh `So sánh · mất hình`).

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Record Card (5 biến thể) | lớp Khung thẻ | Surface · Padding None · Elevation Low · State theo State của thẻ |
| Base / Summary Card | lớp Khung thẻ | Surface · Padding None · Elevation Low · Default |
| Base / Selectable Card (10 biến thể) | lớp Khung thẻ | Muted · Padding None · Elevation None · chưa chọn = State tương ứng; đã chọn = Selected, Selected Hover · Pressed · Focus; Disabled = Disabled |

**Cách ráp "Khung thẻ" (DEC-234):** Khung thẻ là instance Base / Card đặt Absolute, giãn hai chiều phủ kín thẻ cha, nằm dưới cùng, Slot
Content để trống. Nội dung thẻ là con trực tiếp của khuôn L1 cha, vì phần nằm trong Slot của instance lồng không gắn được Has… hay Slot
riêng của cha. Cha tự đặt lề, khoảng (Khung thẻ Padding None); nền, viền, bo, bóng, tick, vòng focus lấy từ Base / Card, cha không đè.
Hình minh hoạ trên Figma: Selectable Card, nhãn `Khung thẻ = Base / Card · Muted · Padding None · Elevation None → tài liệu này`.

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | Web |
|---|---|---|
| Bo | `radius/card` | 12 |
| Lề Default | `layout/card-padding` | 16 |
| Lề Compact · Spacious · None | `card/padding-compact` · `card/padding-spacious` · `card/padding-none` | 12 · 24 · 0 |
| Viền · viền chọn | `card/border-width` · `card/border-width-selected` | 1 · 2 |
| Khoảng trong Slot | `space/gap-md` | 12 |
| Tick | `card/check-size` · `card/check-ring` | 20 · 2 |
| Bóng | `elev/1` · `elev/2` · `elev/3` (effect style) | Low · Med · High |
| Chữ Title · Subtitle | `type/heading` · `type/caption` | 14/20 · 12/16 |
| Vòng focus | `focus/width` · `focus/offset` | 2 · 2 |
| Ảnh nhỏ (`.card / Media`) | `card/media-size-sm` · `card/media-size` · `radius/inner` | 48 · 64 · 8 |
| Vùng chạm | `touch/min` | 24 ✓ (thẻ thấp nhất 38) |

Màu (collection Component, một bộ cho web và app; bỏ tiền tố `card/`):

| Phần | Token | Giá trị |
|---|---|---|
| Nền · Default, rê, nhấn | `bg/default` · `bg/hover` · `bg/pressed` | trắng · neutral/100 · neutral/300 |
| Viền · thường, nhấn, chọn, đứt | `border/default` · `border/pressed` · `border/selected` · `border/dashed` | neutral/200 · neutral/400 · brand/800 · neutral/300 |
| Nền Muted · thường, rê, nhấn | `choice/bg` · `choice/bg-hover` · `choice/bg-pressed` | neutral/100 · neutral/200 · neutral/300 |
| Disabled · nền, chữ, viền | `disabled/bg` · `disabled/fg` · `border/default` | neutral/100 · neutral/400 · neutral/200 |
| Chữ phụ · khi rê, khi nhấn | `fg/secondary-hover` · `fg/secondary-pressed` | neutral/600 · neutral/600 |
| Tick · nền, icon, viền | `check/bg` · `check/fg` · `check/ring` | brand/800 · trắng · trắng |
| Vòng focus · vòng, khe | `color/border/focus` · `focus/gap` | #262626 · = nền trang trắng (DEC-258) |

Nền rê, nhấn dùng cho Surface, Dashed và Muted đã chọn. Tên trong code: `<Card tone="surface|muted|dashed" padding elevation state
selected disabled hasCheck>{content}</Card>`; biến CSS `--card-*`, `--radius-card`, `--focus-gap`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6562:213228 ngày 20/10 (ngưỡng 1,1:1), sau lần sửa cuối.

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 43 ô, 43 mẫu (khối Web; cả khung 82 ô, 82 mẫu) | luật A: 0 lỗi, ô nào cũng có nền riêng và viền mảnh |
| ✕ Mất hình (cố ý) | Cảnh · Không nên 1 | cảnh "Không nên": Muted trên khối `color/bg/muted` 1:1 — đúng điều cảnh muốn chỉ ra |
| Sát ngưỡng | Surface · Hover, Surface · Disabled, Dashed · Hover | nền #F2F4F7 trên ô trắng 1,10:1; viền 1,25 (Surface) / viền đứt 1,47 (Dashed), số tính lại theo nền trắng (DEC-258), chưa chạy lại máy. Disabled có viền từ 20/10; Hover `card/bg/hover` = neutral/100 từ 20/10 |
| ⚠ Nền chìm | Muted · Selected; Muted · đã chọn · Default, Hover, Focus | thẻ trắng trên ô trắng; hình giữ nhờ viền chọn 15,13:1 |
| Sát ngưỡng | 45 mẫu lớp ngoài (cả khung); 10 mẫu lớp con ("Ảnh" của `.card / Media`, "Khung thẻ" của Selectable) | 1,10:1: Muted trên trắng, ô ảnh chờ; Surface · Hover nền neutral/100 trên thẻ trắng 1,10:1 (hết cờ "Giống Default" của bản #F9FAFC 1,04:1) |

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Các kiểu, Content, Padding, Elevation, luật:** như web (cùng cấu tạo, cùng thuộc tính).
- **Khác web:** không Hover, không Selected Hover; bo 16; Title 15/20, Subtitle 13/18; thẻ bấm được cao ≥ 44 (`touch/min`).

### Cấu tạo

Hình phóng 2× trên Figma: như web, mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Khung thẻ | `card/bg/default` · `card/border/default` · `card/border-width` | nền trắng · viền 1px |
| Bo | `radius/card` | 16 |
| Lề | `layout/card-padding` · `card/padding-compact` · `card/padding-spacious` · `card/padding-none` | 16 · 12 · 24 · 0 |
| Bóng | `elev/1` · `elev/2` · `elev/3` | như web |
| Viền chọn | `card/border-width-selected` · `card/border/selected` | 2px · brand/800 |
| Slot Content | `space/gap-md` | 12 |
| Tick chọn | `.card / Check`: `card/check-size` · `card/check-ring` | 20 · 2 |
| Chữ mặc định | `.card / Heading`: `type/heading` · `type/caption` | Title 15/20 · Subtitle 13/18 |
| Vòng focus | `.focus / Ring` | 2 · 2 (khi có bàn phím ngoài hoặc trợ năng) |

### Biến thể

Như web: 136 biến thể; Hover, Selected Hover có trong set nhưng app không dùng.

### Trạng thái

Như web, trừ Hover và Selected Hover. Focus: "khi điều hướng bằng bàn phím ngoài hoặc trợ năng".

### Kích thước

| Padding | Token | Mobile | Cao với Heading |
|---|---|---|---|
| None | `card/padding-none` | 0 | 40 |
| Compact | `card/padding-compact` | 12 | 64 |
| Default | `layout/card-padding` | 16 | 72 (mặc định) |
| Spacious | `card/padding-spacious` | 24 | 88 |

Padding None cao 40 < `touch/min` 44: thẻ bấm được dùng Padding None cần thêm vùng chạm vô hình (Khung thẻ trong thẻ L1 có lề riêng
nên đủ cao).

### Nên và không nên

Như web (cùng hai cặp, mode Mobile).

### L0 của họ thẻ

Như web; `.card / Heading` 15/20 · 13/18; `.card / Media` bo `radius/inner` 12 (`radius/xl`, DEC-259), cỡ 48 · 64 như web.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Title 17,73 trên trắng · 12,03 khi nhấn · 16,09 trên Muted. Subtitle 5,43 · nhấn 5,27 (neutral/600) · Muted 4,92 |
| 1.4.3 ngoại lệ — Disabled | ✓ | 2,34: được miễn |
| 1.4.1 Dùng màu | ✓ | như web |
| 1.4.11 Tương phản ngoài chữ (AA) | ! | như web |
| 2.4.7 · 2.4.13 | ✓ | focus khi có bàn phím ngoài hoặc công cụ trợ năng |
| 2.5.8 (≥ 24) · 2.5.5 (≥ 44) | ! | Padding Default cao 72 ✓; Padding None cao 40 < 44, cần vùng chạm vô hình khi thẻ bấm được |
| 4.1.2 Tên, vai trò | ✓ | nhãn trợ năng (như aria-label); thẻ chọn báo "đã chọn"; nút trong Slot là đích riêng |
| 2.1.1 Bàn phím | ✓ | khi có bàn phím ngoài: Enter, Space; theo thứ tự focus |
| 2.3.3 Chuyển động | ✓ | không có hiệu ứng chuyển động |
| **Điểm app** | | **9/9 đạt** (! = đạt có điều kiện) |

### Thuộc tính

Như web (cùng bảng); app không dùng Hover, Selected Hover.

### Thành phần lồng

Như web (cùng bảng).

### Được dùng trong

Như web (cùng ba component cha, cùng cách ráp Khung thẻ).

### Token

Số đo (collection Platform, mode Mobile): bo `radius/card` 16 (`radius/2xl`) · lề `layout/card-padding` 16 · `card/padding-compact` 12 ·
`card/padding-spacious` 24 · `card/padding-none` 0 · viền 1 · viền chọn 2 · `space/gap-md` 12 · tick 20 · 2 · chữ `type/heading` 15/20 ·
`type/caption` 13/18 · vòng focus 2 · 2 · ảnh nhỏ 48 · 64 · `radius/inner` 12 (`radius/xl`) · `touch/min` 44 (Padding None 40: !).

Màu: như web, bỏ các màu rê (`bg/hover`, `choice/bg-hover`, `fg/secondary-hover`) vì app không dùng Hover.

### Kiểm máy

Cùng lần chạy ở khối Web:

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 39 ô, 39 mẫu (khối Mobile) | luật A: 0 lỗi |
| Sát ngưỡng | Trạng thái · Surface · Disabled | nền #F2F4F7 trên ô trắng 1,10:1; viền 1,25:1 (số tính lại theo nền trắng (DEC-258), chưa chạy lại máy) |
| ✕ Mất hình (cố ý) | Cảnh · Không nên 1 | cảnh "Không nên": Muted trên khối `color/bg/muted` |
| ⚠ Nền chìm | Muted · Selected; Muted · đã chọn · Default, Focus | thẻ trắng trên ô trắng; giữ nhờ viền chọn 15,13:1 |
| Sát ngưỡng | 22 mẫu lớp ngoài; 5 mẫu lớp con | 1,10:1 (app không đặt Hover, không có cờ Hover; mọi Pressed đạt ≥ 1,34) |

## Đối chiếu Astryx

Nguồn: `Card` (43:108295: Padding none · compact · default · spacious × Elevation none · low · med · high, 16 biến thể),
`ClickableCard` (2611:21423: State Rest · Hover · Pressed · Focused · Disabled × Elevation, 20 biến thể), trang Astryx · Library (chỉ đọc).

| | Astryx | DS v2 | Vì sao |
|---|---|---|---|
| Khớp | Slot nội dung; Padding 4 mức; Elevation 4 mức; nền trắng viền 1, bo 12; State Hover · Pressed · Focus · Disabled của ClickableCard | giữ nguyên cấu tạo | — |
| Lệch | hai set Card (tĩnh) và ClickableCard (bấm được) | một set Base / Card, State Default thay Rest, Focus thay Focused | một khung cho thẻ tĩnh và thẻ bấm được (DEC-234) |
| Lệch | không có chọn | State Selected: viền 2px + tick `.card / Check`; Has Check | thẻ bản ghi cần đánh dấu đang chọn, không chỉ dựa vào màu (DEC-234, DEC-237) |
| Lệch | Padding compact 4, spacious 20 | Compact 12, Spacious 24 (biến `card/padding-*`) | thang DS v2 (DEC-234) |
| Lệch | bóng của Astryx | effect style `elev/1 · 2 · 3`; Pressed, Disabled bỏ bóng | dùng bóng DS v2 đã có (DEC-234) |
| Lệch | một kiểu nền | trục Tone Surface · Muted · Dashed | thẻ chọn nền xám không viền (Selectable), thẻ đối tượng chưa tồn tại viền đứt (DEC-234, DEC-237) |
| Lệch | bo 12 mọi nền tảng | bo `radius/card` web 12, app 16 | thang bo theo Platform |
| Chưa làm | Density | — | chưa chốt (architecture) |

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
