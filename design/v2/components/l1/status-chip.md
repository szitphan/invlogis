---
type: design-component
status: draft
updated: 2026-10-20
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - _workspace/decisions.md
---

# Base / Status Chip

> L1 · phiên bản 0.2.0 · Nháp · người phụ trách @szitphan · Figma `Base / Status Chip` (6385:630, 32 biến thể, trang
> DS · Components · L0–L3), L0 `.chip / Dot` (6441:83989), khung tài liệu `Tài liệu · Status Chip` (6473:84011, khối Web
> 6473:84018, khối Mobile 6473:84025) · DEC-130, DEC-180, DEC-200, DEC-213, DEC-239 (Size SM, chữ SM `type/chip-sm*`,
> nhãn tối đa 160, 3 icon gợi ý) · đi cùng [Tooltip](tooltip.md)

Một component cho cả web và app, không có biến thể Platform. Cao chip và cỡ chữ đọc từ biến collection Platform: khung
chứa (màn, thẻ) đặt mode Web hoặc Mobile thì chip tự đổi cỡ. Phần **Web** và phần **Mobile** dưới đây mỗi phần tự đứng
được: đọc phần của nền tảng mình làm là đủ. Màu (collection Semantic, `color/chip/*`) giống nhau ở hai nền tảng. Nền thật
của chip là trắng `color/bg/surface` (bảng, thẻ, đầu trang).

## Web

> Khối Web trên Figma đặt mode Platform = Web; mọi số dưới đây là giá trị mode Web.

### Tổng quan

- **Soft:** nền nhạt + icon: trạng thái chính của bản ghi (bảng, thẻ, đầu trang chi tiết). Mỗi bản ghi chỉ một chip
  Soft (DEC-180).
- **Dot:** chấm + chữ: trạng thái phụ và chỗ dày chữ (lịch sử, dòng thời gian). Không có icon.
- **Tone:** 8 sắc cố định (Gray · Blue · Teal · Purple · Yellow · Green · Red · Orange), không đổi theo khách; nghĩa từng
  sắc gán ở L2, nhãn lấy nguyên văn từ `docs/{feature}/srs/{feature}-states.md`.
- **Cỡ web:** MD 24 mặc định khi kéo ra: bảng, đầu trang chi tiết, dòng nhãn – trạng thái (Base / Status Row) · SM 16:
  chip ở đầu thẻ bản ghi (Base / Record Card). Hai cỡ cùng lề, icon, cỡ chữ 12/16 (SM dùng text style riêng `type/chip-sm-strong` · `type/chip-sm`); chỉ khác cao.
- **Icon:** chỉ Soft; chọn theo nghĩa trạng thái (xong, chờ, lỗi…), đổi bằng thuộc tính Icon; gợi ý sẵn 4 icon: `icon/circle-check` (xong) · `icon/clock` (chờ) ·
  `icon/triangle-alert` (cảnh báo) · `icon/circle-x` (lỗi, huỷ). Dot dùng chấm L0 `.chip / Dot`.
- **Chỉ có ở web:** chữ bị cắt "…" hiện đủ khi rê chuột (Base / Tooltip); trang chi tiết vẫn có chữ đủ.
- **Chữ trên chip:** 1–3 từ, viết hoa chữ đầu, đúng nhãn trong states.md; nhãn tối đa 160 (`chip/label-max-width`), dài hơn cắt "…", không xuống dòng.
- **Không bấm được:** chip chỉ hiển thị, không có State. Cần lọc hoặc chọn thì dùng tab chip hoặc ô chọn, không dùng
  Status Chip.

### Cấu tạo

Hình phóng 2× trên Figma: Soft · Blue · MD (trái) và Dot · Blue · MD (phải), chữ mặc định "Trạng thái". SM đổi cao (16) và dùng text style riêng 12/16.

| Phần | Token | Giá trị web |
|---|---|---|
| Nền | chỉ Soft: `color/chip/{tone}/bg` (bậc 50) | Dot không nền (nền là chỗ đặt) |
| Icon | chỉ Soft: thuộc tính Icon (mặc định `icon/circle-check`; gợi ý sẵn thêm `icon/clock`, `icon/triangle-alert`, `icon/circle-x`); `icon/size/chip`; màu `color/chip/{tone}/fg` | 14 |
| Chữ Soft | thuộc tính Label; MD `type/caption-strong`, SM `type/chip-sm-strong` (`chip/font-size-sm`, `chip/line-height-sm`); màu `color/chip/{tone}/fg` | 12/16 Semi Bold |
| Chữ Dot | thuộc tính Label; MD `type/caption`, SM `type/chip-sm`; màu `color/text/primary` | 12/16 Regular |
| Chấm | chỉ Dot: L0 `.chip / Dot`, `chip/dot-size`; màu `color/chip/{tone}/fg` (Tone chấm theo Tone chip) | 8 |
| Cao | `chip/height` (MD) · `chip/height-sm` (SM); rộng ôm nội dung | 24 · 16 |
| Lề Soft | phía icon `chip/padding-x-icon`, phía chữ `chip/padding-x` | 8 · 12 |
| Icon → chữ | `chip/icon-gap` | 4 |
| Chấm → chữ | `chip/dot-gap`; Dot không lề | 6 |
| Bo | `radius/chip` | tròn hẳn (9999) |
| Nhãn | `chip/label-max-width`; một dòng, dài hơn cắt "…" | tối đa 160 |
| Không có | vòng focus, vùng chạm, State | chip không bấm |

### Biến thể

Type × Tone ở Size MD (lưới 2 × 8 trên Figma). 32 biến thể = Type 2 × Tone 8 × Size 2.

### Trạng thái

Không có trạng thái tương tác: chip chỉ hiển thị, không bấm — không Hover, Pressed, Focus, Disabled (DEC-200). Hai cách
hiện chữ:

| Cách | Trông thế nào |
|---|---|
| Chữ vừa | rộng ôm chữ |
| Nhãn dài | nhãn rộng tối đa 160 (`chip/label-max-width`, bọc trong `Label wrap`): chip ôm chữ tới 160 rồi cắt "…" một dòng; rê chuột hiện đủ (Base / Tooltip) |

Lưới trên Figma: Soft · Dot × MD · SM × Chữ vừa · Nhãn dài (mẫu "Chờ xác nhận bổ sung chứng từ gốc" cắt ở 160).

### Kích thước

| Size | Cao | Lề Soft (icon · chữ) | Icon | Chữ | Dùng khi |
|---|---|---|---|---|---|
| MD | 24 | 8 · 12 | 14 | 12/16 (`type/caption-strong` · `type/caption`) | mặc định: bảng, đầu trang chi tiết, Base / Status Row |
| SM | 16 | 8 · 12 | 14 | 12/16 (`type/chip-sm-strong` · `type/chip-sm`) | đầu thẻ bản ghi (Base / Record Card) |

Bo tròn hẳn ở mọi cỡ. Cần cỡ khác thì thêm biến thể ở component gốc, không đè.

### Nên và không nên

1. **Nên:** một chip Soft cho trạng thái chính, trạng thái phụ dùng Dot. **Không nên:** hai chip Soft cạnh nhau — không
   thấy đâu là trạng thái chính của bản ghi.
2. **Nên:** chữ ngắn 1–3 từ, viết hoa chữ đầu, đúng nhãn trong states.md. **Không nên:** viết hoa toàn bộ, hoặc chỉ có
   chấm không chữ (L0 `.chip / Dot` dùng riêng) — người không phân biệt màu không hiểu.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | Chữ Soft trên nền chip từ 4,88 (Orange) đến 7,06 (Gray) · chữ Dot 17,73 trên trắng |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | Chấm Dot trên trắng từ 5,18 (Orange) · nền Soft 1,06–1,18 trên trắng là trang trí: chip không bấm, chữ đủ để nhận ra |
| 1.4.1 Không chỉ dùng màu (A) | ✓ | Luôn có chữ; Soft thêm icon theo nghĩa |
| 1.4.12 Giãn chữ (AA) | ! | Chữ bị cắt "…" phải có chỗ xem đủ: rê chuột, trang chi tiết |
| 1.4.13 Nội dung hiện khi rê (AA) | ! | Hiện chữ đủ bằng Base / Tooltip: Esc đóng được, rê lên tooltip không tắt |
| 4.1.2 Tên, vai trò (A) | ✓ | Chip là chữ thường, không phải nút; icon đặt `aria-hidden` |
| Không áp dụng | — | 2.1.1, 2.4.7, 2.5.8: chip không bấm, không nhận focus |
| **Điểm web** | | **6/6 đạt** (! = đạt có điều kiện) · lưu ý: chỗ xem đủ chữ bị cắt |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Type | Biến thể | Soft | Soft · Dot |
| Tone | Biến thể | Gray | Gray · Blue · Teal · Purple · Yellow · Green · Red · Orange |
| Size | Biến thể | MD | MD 24 · SM 16 |
| Label | Chữ | Trạng thái | nhãn chip, 1–3 từ, đúng states.md; tối đa 160 (`chip/label-max-width`), dài hơn cắt "…" |
| Icon | Đổi component | icon/circle-check · Size=14 | chỉ hiện ở Soft; chọn sẵn `icon/circle-check`; gợi ý sẵn (preferred) thêm `icon/clock`, `icon/triangle-alert`, `icon/circle-x` (mọi icon DS · Icons đổi được) |

### Thành phần lồng

Không lồng L1 nào; chip là L1 được lồng trong component khác (xem Được dùng trong).

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Chấm | `.chip / Dot` · L0 | Tone theo Tone chip (8 biến thể); chỉ ở Type=Dot; cỡ `chip/dot-size` 8 | — (đổi Tone của chip) |
| Icon | `icon/*` · DS · Icons | đổi bằng Icon; chọn sẵn `icon/circle-check`, gợi ý sẵn thêm `icon/clock`, `icon/triangle-alert`, `icon/circle-x`; cỡ `icon/size/chip` 14; màu theo Tone; chỉ ở Type=Soft | Icon |

### Được dùng trong

Kiểm `getInstancesAsync()` trên Figma 20/10, trang DS · Components: bỏ instance trong khung tài liệu, khung so sánh
(Section 6467:83070) và component đã xoá (`.card / Row`, `.card / Header`, `Base / Vertical Card`, `Base / Horizontal
Card`). Avatar không chứa chip. Slot `End Content` của Base / List Item gợi ý chip nhưng chưa đặt sẵn chip nào.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Record Card | Đầu thẻ, cuối hàng (bật Has Trailing; Trailing đổi component), cách tên 12, canh giữa dọc | Size=SM (16, chữ 12/16 `type/chip-sm-strong`) · Soft · Gray · chữ mẫu "Status"; Trailing chọn sẵn Base / Status Chip, Base / Button; Type, Tone, chữ đổi ở panel (instance lộ ra); không đè cỡ. Thẻ Pressed nền `card/bg/pressed` #D0D5DD: nền chip Gray 1,34:1 trên đó |
| Base / Status Row | Bên phải dòng (canh hai đầu, cách nhãn ≥ 16), canh giữa dọc | Size=MD (24) · Soft · Gray · chữ mẫu "Status"; Type, Tone, chữ đổi ở panel (instance lộ ra). Status Row là giá trị chọn sẵn của Slot Rows ở Record Card |
| Base / List Item | Slot `End Content` (tối đa 2 phần, cách `list-row/gap`) | gợi ý (preferred) cùng Base / Button, icon; đặt chip Size=MD, Soft hoặc Dot; ví dụ trong [List Item](list-item.md) |

### Token

Số đo (collection Platform, mode Web):

| Phần | Token | MD | SM |
|---|---|---|---|
| Cao | `chip/height` · `chip/height-sm` | 24 | 16 |
| Lề Soft: phía icon · phía chữ | `chip/padding-x-icon` · `chip/padding-x` | 8 · 12 | 8 · 12 |
| Icon · icon → chữ | `icon/size/chip` · `chip/icon-gap` | 14 · 4 | 14 · 4 |
| Chấm · chấm → chữ | `chip/dot-size` · `chip/dot-gap` | 8 · 6 | 8 · 6 |
| Bo | `radius/chip` | tròn (9999) | tròn (9999) |
| Chữ Soft | `type/caption-strong` (MD) · `type/chip-sm-strong` (SM) | 12/16 Semi Bold | 12/16 Semi Bold |
| Chữ Dot | `type/caption` (MD) · `type/chip-sm` (SM) | 12/16 Regular | 12/16 Regular |
| Cỡ chữ · dòng SM | `chip/font-size-sm` · `chip/line-height-sm` | — | 12 · 16 |
| Nhãn tối đa | `chip/label-max-width` | 160 | 160 |

Chip không bấm: không có vùng chạm (`touch/min`).

Màu (collection Semantic, `color/chip/*`, một bộ cho web và app; nền bậc 50, chữ bậc 700 — DEC-130):

| Tone | Nền (Soft) | Chữ, icon, chấm | Tương phản (chữ / nền chip · chấm / trắng) |
|---|---|---|---|
| Gray | `chip/gray/bg` | `chip/gray/fg` | 7,06 · 7,78 |
| Blue | `chip/blue/bg` | `chip/blue/fg` | 6,33 · 7,32 |
| Teal | `chip/teal/bg` | `chip/teal/fg` | 5,63 · 6,36 |
| Purple | `chip/purple/bg` | `chip/purple/fg` | 6,59 · 7,75 |
| Yellow | `chip/yellow/bg` | `chip/yellow/fg` | 5,76 · 6,33 |
| Green | `chip/green/bg` | `chip/green/fg` | 5,10 · 5,72 |
| Red | `chip/red/bg` | `chip/red/fg` | 5,76 · 6,57 |
| Orange | `chip/orange/bg` | `chip/orange/fg` | 4,88 · 5,18 |
| Chữ Dot | không nền | `text/primary` | 17,73 trên trắng |

Tên trong code: `<StatusChip variant="soft|dot" tone="gray|blue|teal|purple|yellow|green|red|orange" size="md|sm"
icon={…}>Đang xử lý</StatusChip>`; biến CSS `--color-chip-{tone}-bg|fg` (màu), `--chip-height`, `--chip-height-sm`,
`--chip-font-size-sm`, `--chip-line-height-sm`, `--chip-label-max-width` (160), `--chip-*` (lề, khoảng, chấm), `--radius-chip`,
`--icon-size-chip`, `--type-caption-*`. Chữ dài: nhãn đặt `max-width: var(--chip-label-max-width)`, chữ
`text-overflow: ellipsis`, kèm tooltip chữ đủ.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6473:84011 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 66 ô, 72 mẫu (cả hai khối; thêm hàng Soft · SM, Dot · SM ở lưới Trạng thái) | 0 lỗi luật A: ô nào cũng có nền thật và viền mảnh; ô Record Card nền xám `color/bg/canvas` đã đặt `Context = Canvas` |
| ✕ Mất hình | Soft · Orange (lưới Biến thể; lưới Trạng thái: Chữ vừa, Nhãn dài, cả MD và SM) trên trắng | nền chip #FFF7ED trên nền ô #FFFFFF = 1,06:1; chip không viền, không vòng |
| Sát ngưỡng | Soft · Gray 1,10 · Yellow 1,10 · Green 1,12 · Teal 1,13 · Red 1,14 trên trắng | Yellow thực 1,099 (script làm tròn trước khi so nên không gắn cờ); Blue 1,16, Purple 1,18 đạt; lớp con: Record Card · Khung thẻ 1,10 |
| Không kiểm | Khe vòng focus (C), Hover/Pressed (D) | chip không có State, không có vòng focus |

Nền Soft nhạt là look đã duyệt (DEC-130, bậc 50): giữ nguyên hình; chữ và icon đủ để nhận ra chip.

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **Soft:** nền nhạt + icon: trạng thái chính của bản ghi (thẻ, đầu trang chi tiết). Mỗi bản ghi chỉ một chip Soft
  (DEC-180).
- **Dot:** chấm + chữ: trạng thái phụ và chỗ dày chữ (lịch sử, dòng thời gian). Không có icon.
- **Tone:** 8 sắc cố định (Gray · Blue · Teal · Purple · Yellow · Green · Red · Orange), không đổi theo khách; nghĩa từng
  sắc gán ở L2, nhãn lấy nguyên văn từ `docs/{feature}/srs/{feature}-states.md`.
- **Cỡ app:** MD 26 mặc định khi kéo ra: đầu trang chi tiết, dòng nhãn – trạng thái (Base / Status Row) · SM 16: chip ở đầu thẻ bản ghi (Base / Record Card). Hai cỡ cùng lề, icon; chữ MD 13/18, SM 12/16 (text style riêng `type/chip-sm-strong` · `type/chip-sm`); khác cao và cỡ chữ.
- **Icon:** chỉ Soft; chọn theo nghĩa trạng thái (xong, chờ, lỗi…), đổi bằng thuộc tính Icon; gợi ý sẵn 4 icon: `icon/circle-check` (xong) · `icon/clock` (chờ) ·
  `icon/triangle-alert` (cảnh báo) · `icon/circle-x` (lỗi, huỷ). Dot dùng chấm L0 `.chip / Dot`.
- **Khác web:** MD cao 26 (web 24), chữ 13/18 (web 12/16); SM 16, chữ SM 12/16 như web. Không rê chuột: chữ bị cắt xem đủ ở trang chi
  tiết. Chip không bấm nên không cần vùng chạm 44.
- **Chữ trên chip:** 1–3 từ, viết hoa chữ đầu, đúng nhãn trong states.md; nhãn tối đa 160 (`chip/label-max-width`), dài hơn cắt "…", không xuống dòng.
- **Không bấm được:** chip chỉ hiển thị, không có State. Cần lọc hoặc chọn thì dùng tab chip hoặc ô chọn, không dùng
  Status Chip.

### Cấu tạo

Hình phóng 2× trên Figma: Soft · Blue · MD (trái) và Dot · Blue · MD (phải), chữ mặc định "Trạng thái". SM đổi cao (16) và dùng text style riêng 12/16.

| Phần | Token | Giá trị app |
|---|---|---|
| Nền | chỉ Soft: `color/chip/{tone}/bg` (bậc 50) | Dot không nền (nền là chỗ đặt) |
| Icon | chỉ Soft: thuộc tính Icon (mặc định `icon/circle-check`; gợi ý sẵn thêm `icon/clock`, `icon/triangle-alert`, `icon/circle-x`); `icon/size/chip`; màu `color/chip/{tone}/fg` | 14 |
| Chữ Soft | thuộc tính Label; MD `type/caption-strong`, SM `type/chip-sm-strong` (`chip/font-size-sm`, `chip/line-height-sm`); màu `color/chip/{tone}/fg` | 13/18 Semi Bold (SM 12/16) |
| Chữ Dot | thuộc tính Label; MD `type/caption`, SM `type/chip-sm`; màu `color/text/primary` | 13/18 Regular (SM 12/16) |
| Chấm | chỉ Dot: L0 `.chip / Dot`, `chip/dot-size`; màu `color/chip/{tone}/fg` (Tone chấm theo Tone chip) | 8 |
| Cao | `chip/height` (MD) · `chip/height-sm` (SM); rộng ôm nội dung | 26 · 16 |
| Lề Soft | phía icon `chip/padding-x-icon`, phía chữ `chip/padding-x` | 8 · 12 |
| Icon → chữ | `chip/icon-gap` | 4 |
| Chấm → chữ | `chip/dot-gap`; Dot không lề | 6 |
| Bo | `radius/chip` | tròn hẳn (9999) |
| Nhãn | `chip/label-max-width`; một dòng, dài hơn cắt "…" | tối đa 160 |
| Không có | vòng focus, vùng chạm, State | chip không bấm |

### Biến thể

Type × Tone ở Size MD (lưới 2 × 8 trên Figma). 32 biến thể = Type 2 × Tone 8 × Size 2 (dùng chung với web).

### Trạng thái

Không có trạng thái tương tác: chip chỉ hiển thị, không bấm — không Pressed, Focus, Disabled (DEC-200); app không dùng
Hover. Hai cách hiện chữ:

| Cách | Trông thế nào |
|---|---|
| Chữ vừa | rộng ôm chữ |
| Nhãn dài | nhãn rộng tối đa 160 (`chip/label-max-width`, bọc trong `Label wrap`): chip ôm chữ tới 160 rồi cắt "…" một dòng; xem đủ ở trang chi tiết (app không rê chuột) |

Lưới trên Figma: Soft · Dot × MD · SM × Chữ vừa · Nhãn dài (mẫu "Chờ xác nhận bổ sung chứng từ gốc" cắt ở 160).

### Kích thước

| Size | Cao | Lề Soft (icon · chữ) | Icon | Chữ | Dùng khi |
|---|---|---|---|---|---|
| MD | 26 | 8 · 12 | 14 | 13/18 (`type/caption-strong` · `type/caption`) | mặc định: đầu trang chi tiết, Base / Status Row |
| SM | 16 | 8 · 12 | 14 | 12/16 (`type/chip-sm-strong` · `type/chip-sm`) | đầu thẻ bản ghi (Base / Record Card) |

Bo tròn hẳn ở mọi cỡ. Ở SM chữ 12/16 vừa khít chip 16, không lố khung (DEC-239).

### Nên và không nên

1. **Nên:** một chip Soft cho trạng thái chính, trạng thái phụ dùng Dot. **Không nên:** hai chip Soft cạnh nhau — không
   thấy đâu là trạng thái chính của bản ghi.
2. **Nên:** chữ ngắn 1–3 từ, viết hoa chữ đầu, đúng nhãn trong states.md. **Không nên:** viết hoa toàn bộ, hoặc chỉ có
   chấm không chữ (L0 `.chip / Dot` dùng riêng) — người không phân biệt màu không hiểu.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | cùng màu với web: chữ Soft trên nền chip từ 4,88 (Orange) đến 7,06 (Gray) · chữ Dot 17,73 trên trắng |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | Chấm Dot trên trắng từ 5,18 (Orange) · nền Soft 1,06–1,18 trên trắng là trang trí: chip không bấm, chữ đủ để nhận ra |
| 1.4.1 Không chỉ dùng màu (A) | ✓ | Luôn có chữ; Soft thêm icon theo nghĩa |
| 1.4.12 Giãn chữ (AA) | ! | Chữ bị cắt "…" xem đủ ở trang chi tiết (app không rê chuột) |
| 4.1.2 Tên, vai trò (A) | ✓ | Nhãn trợ năng (như `aria-label`) đọc chữ chip; icon ẩn khỏi trình đọc màn hình |
| Không áp dụng | — | 2.1.1, 2.4.7, 2.5.5, 2.5.8: chip không bấm · 1.4.13: app không rê chuột |
| **Điểm app** | | **5/5 đạt** (! = đạt có điều kiện) · lưu ý: chữ bị cắt xem ở trang chi tiết |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Type | Biến thể | Soft | Soft · Dot |
| Tone | Biến thể | Gray | Gray · Blue · Teal · Purple · Yellow · Green · Red · Orange |
| Size | Biến thể | MD | MD 26 · SM 16 |
| Label | Chữ | Trạng thái | nhãn chip, 1–3 từ, đúng states.md; tối đa 160 (`chip/label-max-width`), dài hơn cắt "…" |
| Icon | Đổi component | icon/circle-check · Size=14 | chỉ hiện ở Soft; chọn sẵn `icon/circle-check`; gợi ý sẵn (preferred) thêm `icon/clock`, `icon/triangle-alert`, `icon/circle-x` (mọi icon DS · Icons đổi được) |

### Thành phần lồng

Không lồng L1 nào; chip là L1 được lồng trong component khác (xem Được dùng trong).

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Chấm | `.chip / Dot` · L0 | Tone theo Tone chip (8 biến thể); chỉ ở Type=Dot; cỡ `chip/dot-size` 8 | — (đổi Tone của chip) |
| Icon | `icon/*` · DS · Icons | đổi bằng Icon; chọn sẵn `icon/circle-check`, gợi ý sẵn thêm `icon/clock`, `icon/triangle-alert`, `icon/circle-x`; cỡ `icon/size/chip` 14; màu theo Tone; chỉ ở Type=Soft | Icon |

### Được dùng trong

Kiểm `getInstancesAsync()` trên Figma 20/10 (cùng cách lọc như phần Web). Avatar không chứa chip.

| Component cha | Chỗ đặt | Cấu hình dùng |
|---|---|---|
| Base / Record Card | Đầu thẻ, cuối hàng (bật Has Trailing; Trailing đổi component), cách tên 12, canh giữa dọc | Size=SM (16, chữ 12/16 `type/chip-sm-strong`) · Soft · Gray · chữ mẫu "Status"; Trailing chọn sẵn Base / Status Chip, Base / Button; Type, Tone, chữ đổi ở panel (instance lộ ra); không đè cỡ. Thẻ Pressed nền `card/bg/pressed` #D0D5DD: nền chip Gray 1,34:1 trên đó |
| Base / Status Row | Bên phải dòng (canh hai đầu, cách nhãn ≥ 16), canh giữa dọc | Size=MD (26) · Soft · Gray · chữ mẫu "Status"; Type, Tone, chữ đổi ở panel (instance lộ ra). Status Row là giá trị chọn sẵn của Slot Rows ở Record Card |
| Base / List Item | Slot `End Content` (tối đa 2 phần, cách `list-row/gap` 12) | gợi ý (preferred) cùng Base / Button, icon; đặt chip Size=MD (26), Soft hoặc Dot |

### Token

Số đo (collection Platform, mode Mobile):

| Phần | Token | MD | SM |
|---|---|---|---|
| Cao | `chip/height` · `chip/height-sm` | 26 | 16 |
| Lề Soft: phía icon · phía chữ | `chip/padding-x-icon` · `chip/padding-x` | 8 · 12 | 8 · 12 |
| Icon · icon → chữ | `icon/size/chip` · `chip/icon-gap` | 14 · 4 | 14 · 4 |
| Chấm · chấm → chữ | `chip/dot-size` · `chip/dot-gap` | 8 · 6 | 8 · 6 |
| Bo | `radius/chip` | tròn (9999) | tròn (9999) |
| Chữ Soft | `type/caption-strong` (MD) · `type/chip-sm-strong` (SM) | 13/18 Semi Bold | 12/16 Semi Bold |
| Chữ Dot | `type/caption` (MD) · `type/chip-sm` (SM) | 13/18 Regular | 12/16 Regular |
| Cỡ chữ · dòng SM | `chip/font-size-sm` · `chip/line-height-sm` | — | 12 · 16 |
| Nhãn tối đa | `chip/label-max-width` | 160 | 160 |

Chip không bấm: không có vùng chạm (`touch/min` 44 không áp).

Màu: cùng bảng với phần Web (collection Semantic không có mode theo nền tảng); tương phản như nhau.

Tên trong code: cùng component `StatusChip` với web (`variant`, `tone`, `size`, `icon`); icon ẩn khỏi trình đọc màn
hình; nhãn dài cắt "…" ở `--chip-label-max-width` (160) và trang chi tiết hiện chữ đủ.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6473:84011 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 66 ô, 72 mẫu (cả hai khối; thêm hàng Soft · SM, Dot · SM ở lưới Trạng thái) | 0 lỗi luật A; ô Record Card nền xám đã đặt `Context = Canvas` |
| ✕ Mất hình | Soft · Orange (lưới Biến thể; lưới Trạng thái: Chữ vừa, Nhãn dài, cả MD và SM) trên trắng | nền chip #FFF7ED trên nền ô #FFFFFF = 1,06:1; chip không viền, không vòng |
| Sát ngưỡng | Soft · Gray 1,10 · Yellow 1,10 · Green 1,12 · Teal 1,13 · Red 1,14 trên trắng | Yellow thực 1,099 (script làm tròn trước khi so); Blue 1,16, Purple 1,18 đạt; lớp con: Record Card · Khung thẻ 1,10 |
| Không kiểm | Khe vòng focus (C), Hover/Pressed (D) | chip không có State; app không dùng Hover |

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của từng phần.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / Status Chip` (6385:630) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Label | Chữ | Trạng thái | — |
| Icon | Đổi component | icon/circle-check · Size=14 | nhận: icon/circle-check · icon/clock · icon/triangle-alert · icon/circle-x |
| Type | Biến thể | Soft | Soft · Dot |
| Tone | Biến thể | Gray | Gray · Blue · Teal · Purple · Yellow · Green · Red · Orange |
| Size | Biến thể | MD | MD · SM |

32 biến thể · trục Type × Tone × Size.

### Màu theo phần (token)

| Type | Tone | Nền | Chữ | Icon |
|---|---|---|---|---|
| Soft | Gray | `color/chip/gray/bg` | `color/chip/gray/fg` | `color/chip/gray/fg` |
| Soft | Blue | `color/chip/blue/bg` | `color/chip/blue/fg` | `color/chip/blue/fg` |
| Soft | Teal | `color/chip/teal/bg` | `color/chip/teal/fg` | `color/chip/teal/fg` |
| Soft | Purple | `color/chip/purple/bg` | `color/chip/purple/fg` | `color/chip/purple/fg` |
| Soft | Yellow | `color/chip/yellow/bg` | `color/chip/yellow/fg` | `color/chip/yellow/fg` |
| Soft | Green | `color/chip/green/bg` | `color/chip/green/fg` | `color/chip/green/fg` |
| Soft | Red | `color/chip/red/bg` | `color/chip/red/fg` | `color/chip/red/fg` |
| Soft | Orange | `color/chip/orange/bg` | `color/chip/orange/fg` | `color/chip/orange/fg` |
| Dot | Gray | trong suốt | `color/text/primary` | `color/chip/gray/fg` |
| Dot | Blue | trong suốt | `color/text/primary` | `color/chip/blue/fg` |
| Dot | Teal | trong suốt | `color/text/primary` | `color/chip/teal/fg` |
| Dot | Purple | trong suốt | `color/text/primary` | `color/chip/purple/fg` |
| Dot | Yellow | trong suốt | `color/text/primary` | `color/chip/yellow/fg` |
| Dot | Green | trong suốt | `color/text/primary` | `color/chip/green/fg` |
| Dot | Red | trong suốt | `color/text/primary` | `color/chip/red/fg` |
| Dot | Orange | trong suốt | `color/text/primary` | `color/chip/orange/fg` |

### Số đo theo phần (token)

| Type | Size | Cao | Rộng | Lề trái | Lề phải | Khoảng giữa | Bo | Cỡ icon |
|---|---|---|---|---|---|---|---|---|
| Soft | MD | `chip/height` | ôm nội dung | `chip/padding-x-icon` | `chip/padding-x` | `chip/icon-gap` | `radius/chip` | `icon/size/chip` |
| Soft | SM | `chip/height-sm` | ôm nội dung | `chip/padding-x-icon` | `chip/padding-x` | `chip/icon-gap` | `radius/chip` | `icon/size/chip` |
| Dot | MD | `chip/height` | ôm nội dung | 0 | 0 | `chip/dot-gap` | 0 | `chip/dot-size` |
| Dot | SM | `chip/height-sm` | ôm nội dung | 0 | 0 | `chip/dot-gap` | 0 | `chip/dot-size` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Label (Soft · MD) | `type/caption-strong` |
| Label (Dot · MD) | `type/caption` |
| Label (Soft · SM) | `type/chip-sm-strong` |
| Label (Dot · SM) | `type/chip-sm` |

<!-- auto:end -->
