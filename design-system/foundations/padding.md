---
type: design-foundations
status: approved
updated: 2026-11-03
links:
  - design-system/foundations/README.md
  - design-system/foundations/spacing.md
  - design-system/tokens.json
  - design/_ref/untitled-ui/react/components
---

# Foundations · Auto layout component

> Một phần của [[design-system/foundations/README.md|Foundations]], tách khỏi [[design-system/foundations/spacing.md|Khoảng cách]] (DEC-342). Giá trị máy đọc: `design-system/tokens.json` (json thắng). **Đang duyệt:** các số dưới đây là hiện trạng, chưa phải luật đã chốt.

## Phạm vi

- **Thuộc mục này:** 5 phần auto layout bên trong một component: padding (lề trong theo chữ, icon, chấm, ô đếm, ảnh, nút), flow, resizing, alignment, gap.
- **Thuộc Khoảng cách (`space`, đã duyệt):** thang `space/*`, cao control, lề màn, khoảng giữa các khối, lề thẻ `layout/*`.
- **Trang duyệt:** https://claude.ai/artifact/G49c2ML6q3GSBaCWnuJct6. Nguồn số đo và lý do từng mục (`pd00`…`pd15`, `al00`…`al08`) nằm trên trang, dựng từ `_scripts/foundation_review/padding.py`.

## Bộ số đã chốt (DEC-346)

Bản tổng hợp so với Untitled: https://claude.ai/artifact/G6xPZL4sgGd1YczWiRfkho.

Hai bảng so sánh bên dưới ghi số **trước khi áp**, giữ làm hồ sơ đối chiếu.

| Nhóm | Phía chữ | Phía icon, chấm | Icon, chấm → chữ | Token |
|---|---|---|---|---|
| Button Web SM · MD · LG | 10 · 12 · 16 | 8 · 10 · 14 | 6 | `control/padding-x-icon/*` + `control/label-inset` 2; khoảng `space/xs` + bọc 2 |
| Button App SM · MD · LG | 12 · 16 · 24 | 8 · 12 · 20 | 8 | `control/padding-x-icon/*` + `control/label-inset` 4 |
| Badge SM · MD · LG | 8 · 10 · 12 | 6 · 8 · 10 | 4 | Đã chốt ở DEC-341 |
| Tag SM · MD · LG | 8 · 10 · 12 | 6 · 8 · 10 | 4 | Khung ngoài trái `space/sm`, `space/md`, `space/md-lg`, phải `space/xs`, khoảng `space/xxs`; Label wrap trái `space/xxs`, phải `space/xs`, `space/sm`, `space/md` |
| Ô đếm SM, MD · LG | 4 · 6 | — | — | `space/xs` · `space/sm` |
| Input, Select, Multi-select Web | 12 | 8 | 8 | Multi-select chưa có chip: cao `control/height/*` |
| Dòng menu Web · App | 8 · 12 | 8 · 12 | 8 | `list-row/padding-x`, `list-row/padding-y`, `space/md` |
| Radio ô 16 · 20 | — | chấm 6 · 8 | — | `size/sm`, `size/md`, lề 0 |
| Thẻ Icon card | 16 | 16 | 12 | `layout/card-padding`, `space/lg` |
| Tab chip App | 16 | 12 | nhãn → số 6 | `space/sm` |

**Luật:**

- Nút Web và chip: phía icon lùi 2 so với phía chữ, như Untitled. Ô nhập Web lùi 4. App giữ số đang có.
- Chữ co giãn trong dòng dùng Fill, cắt 1 dòng. Không dùng kiểu `TRUNCATE` của Figma.
- Không dùng khung rỗng làm khoảng cách.
- Ô chọn canh trên với dòng đầu của nhãn, ở cả Web và App.
- Nhãn → ô → gợi ý 6 (`space/sm`). Dòng trong menu Web cách 2 (`space/xxs`), App 0.
- Lề và gap của component gắn thang Semantic. Số ngoài thang ghi ở bảng ngoại lệ của [[design-system/foundations/spacing.md|Khoảng cách]].

Trên Figma: section `Auto layout component` trong nhóm `Spacing, radius & grids`, trang `DS · Foundations` (node 7268:1619).

**Chốt thêm (DEC-347):**

- Select item dạng Supporting: nhãn Fill, cắt 1 dòng, chữ phụ nằm cuối dòng.
- Card header: giữ tiêu đề Hug, tối đa 300, để Badge sát tiêu đề. Thẻ hẹp hơn 300 thì màn phải tự giới hạn chữ tiêu đề.
- Badge dùng cách của Tag: khung chữ đệm 2, không cần trục `Leading`.

**Ngoài phạm vi (DEC-348):** 57 set Astryx cũ trên 2 trang DS không xoá và không tính khi rà. Trong phạm vi vẫn có `Khung trang/*`, `Device/*`, `Kbd`.

**Còn mở:**

- Chữ nhãn Input, Select tối đa 264 là số trần trên Figma, vì Figma không gắn biến vào chiều rộng tối đa của chữ và chữ Hug không tự co. Khi code, nhãn co theo ô.
- `list-row/min-height` và `card/border-width*` còn gắn biến đã xoá: thuộc BL-389.
- Multi-select Platform Mobile giữ nguyên số đo. Select menu, `_Multi-select menu` chưa đổi gap dòng.
- Khi component Base hoàn thiện, đi lại toàn bộ mục này một lượt (user 03/11).

## Padding so với Untitled UI v8

Số đọc từ mã nguồn `design/_ref/untitled-ui/react/components/`, đổi lớp Tailwind ra px. Mỗi ô ghi `Untitled / mình`; `—` là một bên không có hoặc cao cố định. Untitled không có cỡ 28 và không có bản App, nên hàng Button App chỉ là so gần.

| Untitled | Cỡ | Mình so với | Phía chữ | Phía icon, chấm | Icon, chấm → chữ | Trên dưới |
|---|---|---|---|---|---|---|
| Button xs | cao 32 | Button Web MD · 32 | 12 / 12 | 10 / 8 | 6 / 8 | 6 / — |
| Button sm | cao 36 | Button App SM · 36 | 14 / 12 | 12 / 8 | 6 / 8 | 8 / — |
| Button md | cao 40 | Button Web LG · 40 | 16 / 16 | 14 / 12 | 6 / 8 | 10 / — |
| Button lg | cao 44 | Button App MD · 44 | 18 / 16 | 16 / 12 | 8 / 8 | 10 / — |
| Button xl | cao 48 | Button App LG · 52, gần nhất | 20 / 24 | 18 / 20 | 8 / 8 | 12 / — |
| Button chỉ icon | cao 32 · 40 | Button Web MD · LG | — / — | 8 · 10 / 8 · 10 | — / — | 8 · 10 / 8 · 10 |
| Button link | xs đến md · lg, xl | Button Link Gray Web · App | 0 / 0 | 0 / 0 | 4 · 6 / 6 · 8 | 0 / 0 |
| Button group | cao 36 · 40 · 44 | _Button group item SM · 28 | 14 · 16 · 18 / 8 | 12 · 14 · 16 / — | 6 · 6 · 8 / — | 8 · 10 · 10 / — |
| Badge Pill, có chấm | cao 22 · 24 · 28 | Badge có chấm | 8 · 10 · 12 / 8 · 10 · 12 | 6 · 8 · 10 / 6 · 8 · 10 | 4 · 6 · 6 / 4 · 4 · 4 | 2 · 2 · 4 / — |
| Badge Pill, có icon | cao 22 · 24 · 28 | Badge có icon | 8 · 10 · 12 / 8 · 10 · 12 | 6 · 8 · 10 / 6 · 8 · 10 | 2 · 4 · 4 / 4 · 4 · 4 | 2 · 2 · 4 / — |
| Badge Pill, chỉ chữ | cao 22 · 24 · 28 | Badge chỉ chữ (đã chốt) | 8 · 10 · 12 / 8 · 10 · 12 | — / — | — / — | 2 · 2 · 4 / — |
| Badge Color, chỉ chữ | cao 22 · 24 · 28 | Badge Color, dùng chung bộ Pill | 6 · 8 · 10 / 8 · 10 · 12 | — / — | — / — | 2 · 2 · 4 / — |
| Tag | SM · MD · LG | Tag | 8 · 9 · 10 / 6 · 8 · 10 | 6 · 7 · 9 / 6 · 8 · 10 | 4 · 5 · 6 / 4 · 6 · 6 | 3 · 2 · 4 / — |
| Ô đếm trong Tag | SM · MD · LG | _Tag count | 4 · 5 · 6 / 4 · 5 · 6 | — / — | — / — | — / — |
| Input | cao 36 · 40 · 44 | Input Web · 28 · 32 · 40 | 12 · 12 · 14 / 12 · 12 · 12 | 12 · 12 · 14 / 8 · 8 · 8 | 8 · 8 · 8 / 8 · 8 · 8 | 8 · 8 · 10 / — |
| Select | cao 36 · 40 · 44 | Select Web · 28 · 32 · 40 | 12 · 12 · 14 / 12 · 12 · 12 | 10 · 12 · 14 / 8 · 8 · 8 | 8 · 8 · 8 / 8 · 8 · 8 | 8 · 8 · 10 / — |
| Multi-select | cao 36 · 40 · 44 | Multi-select Web · 28 · 34 | 12 · 12 · 14 / 8 · 8 | 10 · 12 · 14 / 8 · 8 | 8 · 8 · 8 / 4 · 4 | 8 · 8 · 10 / 2 · 4 |
| Tags input, đã có tag | SM · MD · LG | Tags input | 8 · 8 · 10 / 12 | — / — | tag cách 6 / tag cách 4 | 6 · 8 · 10 / 4 |
| Textarea | SM · MD | Textarea | 12 · 14 / 12 · 12 | — / — | — / — | 12 · 12 / 12 · 12 |
| Dropdown item | một cỡ | Dropdown item Web | 10 / 8 | 10 / 8 | 8 / 12 | 8 / 8 |
| Select item | SM · MD | Select item | 10 / 8 | 8 / 8 | 8 / 12 | 8 / 8 |
| Dòng Multi-select | SM · MD | _Multi-select item | 10 / 8 | 8 / 8 | 8 / 12 | 8 / 8 |
| Nav item | một cỡ | _Nav item | 8 / 8 | 8 / 8 | 8 / 8 | 8 / 8 |
| File row | một cỡ | _File row | 16 / 8 | 16 / 12 | 12 / 12 | 16 / 12 |
| Radio, Checkbox, Toggle kèm chữ | SM · MD | Radio, Checkbox, Toggle label | — / — | — / — | 8 · 12 / 8 · 12 | — / — |
| Chấm Radio trong ô 16 · 20 | SM · MD | Chấm Radio App | — / — | 6 · 8 / 4 | — / — | — / — |
| Avatar kèm chữ | một cỡ | Avatar label | — / — | — / — | 8 / 8 | — / — |
| Tooltip ngắn · có mô tả | hai dạng | Tooltip Short · Supporting | 12 · 12 / 8 · 12 | — / — | — / — | 8 · 12 / 4 · 8 |
| Tab dạng nút | SM | _Tab chip App · 36 | 12 / 16 | 12 / 12 | 6 / 8 | 8 / — |
| Tab gạch dưới | SM | _Header tab, Tab item | 2 / 0 | 2 / 0 | — / — | pb 10 / — |

Khớp 31/79 số so được, đếm ngày 02/11/2026.

Ref đã lưu không có Alert, Notification, Breadcrumbs, thẻ chọn, Vehicle.

## Flow, resizing, alignment, gap so với Untitled UI v8

Đo ngày 02/11/2026 trên 53 set, tối đa 80 biến thể mỗi set, không tính lớp trong instance. Chưa đo 4 component đơn: Dropdown search, _Nav heading, _Nav account card, _Nav featured card.

| Phần | Component | Untitled | Mình | Trạng thái |
|---|---|---|---|---|
| Flow | Mọi set | — | Không có khung nào có từ 2 phần tử hiện mà thiếu auto layout | Giống |
| Flow | Button | Ngang, `inline-flex` | Ngang | Giống |
| Flow | Input, Select: nhãn, ô, gợi ý | Dọc, `flex-col` | Dọc | Giống |
| Flow | Chữ trong Radio, Checkbox | Dọc, `flex-col` | Dọc | Giống |
| Flow | Tags input | Xuống hàng, `flex-wrap` | Xuống hàng | Giống |
| Flow | Select item: nhãn + mô tả | Xuống hàng khi chật, `flex-wrap` | 2 hàng cố định Line 1, Line 2 | Khác, chưa rõ lý do |
| Flow | Lớp đè: vòng focus, viền, thanh tiến độ | Ngoài luồng, `before:absolute` | Ngoài luồng | Giống |
| Flow | _Nav item, Vehicle Card: khung rỗng | Lùi bằng lề, `pl-10` | Khung rỗng `Indent`, `Gap` | Lệch, cần chọn |
| Resizing | Button | Rộng và cao theo nội dung, `h-max` | Rộng theo nội dung, cao cố định | Khác có lý do |
| Resizing | Input, Select | Chiếm hết chiều ngang, `w-full` | Rộng cố định, cao theo nội dung | Khác có lý do |
| Resizing | Dropdown item: nhãn | Giãn và cắt, `grow truncate` | Fill, cắt 1 dòng | Giống |
| Resizing | Avatar label | `min-w-0 flex-1`, cắt | Fill, cắt 1 dòng | Giống |
| Resizing | Select item: nhãn | `min-w-0 flex-1`, `truncate` | Hug. Thử rộng 240: chữ dài 760, tràn khỏi dòng | Lệch, cần chọn |
| Resizing | _Search result: tiêu đề, đường dẫn | Ref không có | Hug. Thử rộng 240: chữ dài 760 và 647, tràn | Lệch, cần chọn |
| Resizing | Card header: tiêu đề | Ref không có | Hug, tối đa 300. Thử rộng 240: tràn, mô tả bị ép còn 18 | Lệch, cần chọn |
| Resizing | _Multi-select item: nhãn | Dùng Select item, `truncate` | Xuống 5 dòng, dòng cao 116 | Lệch, cần chọn |
| Resizing | Badge, Tag, _Tab chip: nhãn | Badge rộng theo chữ, `size-max`, không cắt | Hug, tối đa 160 rồi cắt. Đã thử: đúng | Khác, chưa rõ lý do |
| Resizing | Tooltip | Tối đa 320, `max-w-xs` | Short 240, Supporting 320 | Khác có lý do |
| Resizing | Input, Select: hàng nhãn | Không giới hạn | Tối đa 320, ô App rộng được 361 | Lệch, cần chọn |
| Resizing | _Nav item, _Nav tenant switch: nhãn | `flex-1`, `truncate` | Cắt được, nhưng dùng kiểu cũ `TRUNCATE` | Lệch, cần chọn |
| Alignment | Button | Giữa hai trục, `items-center justify-center` | Giữa hai trục | Giống |
| Alignment | Radio, Toggle, Checkbox Web | Canh trên, `items-start` | Canh trên | Giống |
| Alignment | Checkbox App | Canh trên, `items-start` | Canh giữa | Lệch, cần chọn |
| Alignment | Select item, Dropdown item | Canh giữa dọc, `items-center` | Canh giữa dọc | Giống |
| Alignment | Input, Select: khối dọc | Canh trái, `items-start` | Canh trái | Giống |
| Alignment | Avatar label | Canh giữa dọc, `items-center` | Canh giữa dọc | Giống |
| Alignment | _File row | Canh trên, `flex` mặc định | Canh trên | Giống |
| Alignment | Chữ trong mọi set | Canh trái, `text-left` | Canh trái | Giống |
| Gap | Nhãn → ô → gợi ý | 6, `gap-1.5` | 4 | Lệch, cần chọn |
| Gap | Dòng trong menu | 2, mỗi dòng `py-px` | 0, nền hover hai dòng chạm nhau | Lệch, cần chọn |
| Gap | Chip trong Tags input | 6, `gap-1.5` | 4 | Khác, chưa rõ lý do |
| Gap | Nhãn → gợi ý trong Radio, Checkbox | SM 0, MD 2, `gap-0.5` | SM 0, MD 2 | Giống |
| Gap | Tooltip: tiêu đề → mô tả | 4, `gap-1` | 4 | Giống |
| Gap | _File row: dòng thông tin | 8 và 4, `gap-2`, `gap-1` | 8 và 4 | Giống |
| Gap | _File row: tên → thông tin | 2, `mt-0.5` | 1, ngoài thang | Lệch, cần chọn |
| Gap | Tab gạch dưới: giữa các tab | 12, `gap-3` | 20 | Khác, chưa rõ lý do |
| Gap | Gắn biến | Không dùng token theo vai | 365 gap số trần | Lệch, cần chọn |
