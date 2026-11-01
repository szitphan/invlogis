---
type: design-component
status: stale
status_prev: approved
updated: 2026-10-29
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/foundations/icon.md
  - design-system/tokens.json
  - design-system/components/_work/badge-avatar/page.json
  - design-system/components/base/avatar.md
  - _workspace/decisions.md
---

# Badge

> Base · phiên bản 0.1.0 · Đã duyệt · người phụ trách @szitphan · Figma: Section `Badges` (6657:165305) trang DS · Base
> components — set `Badge` 6657:165736 (288 biến thể: 6 Type × 8 Color × 3 Size × Count No/Yes) · DEC-277, DEC-303, DEC-309, DEC-310, DEC-311 · thay tài liệu cũ
> `l1/status-chip.md` (đã bỏ, DEC-312) · trang duyệt https://claude.ai/artifact/GcxVBfcfm4imkYbQstd9h2 · ảnh mốc
> `_work/badge-avatar/preview-web.png`, `preview-mobile.png`

Nhãn **chỉ đọc** cho trạng thái, phân loại, số đếm. Luôn có chữ, không dựa vào màu. Nhóm A (DEC-279): một bộ, cùng số đo
web và app. Badge **không có nút X** — chip lọc bỏ được dùng component Tag (DEC-284, DEC-303).

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

| Type | Hình | Dùng cho |
|---|---|---|
| **Pill Color** | bo tròn hẳn `radius/full`, nền màu sắc | Trạng thái (cột Trạng thái của bảng, đầu trang chi tiết) |
| **Pill Outline** | Pill Color + viền 1 màu sắc 200 | Trạng thái cần tách khỏi nền xám (dòng đang chọn / hover) |
| **Badge Color** | bo `radius/badge` 6 (LG `radius/menu` 8), nền màu sắc | Nhãn phụ, số liệu |
| **Badge Outline** | Badge Color + viền 1 màu sắc 200 (như Pill Outline) | Như Badge Color, trên nền không trắng |
| **Badge Modern** | nền trắng, viền xám `color/border/primary`, chữ `color/text/primary`; chỉ chấm / icon mang màu | **Phân loại** (cột Loại: hàng lạnh, quá khổ…) |
| **Dot** | không nền, không viền, không lề; chấm màu + chữ thường `color/text/primary` | Trạng thái phụ, chỗ dày chữ (lịch sử, dòng thời gian) — từ kiểu Dot của Status chip (DEC-310) |

- **Color:** Gray · Blue · Green · Yellow · Red · Teal · Purple · Orange — token `color/chip/{màu}/bg`, `/fg`.
  **Teal / tím / cam chỉ dùng cho phân loại** ở dạng Badge Modern, không dùng cho trạng thái (DEC-303).
- **Size:** SM 22 · MD 24 · LG 28. SM không dùng cho trạng thái chính.
- **Count** là trục biến thể No / Yes (DEC-310): có ô đếm thì lề phải khác (3 · 4 · 4), nên không làm công tắc được. Số trong ô sửa ở thuộc tính chữ **Count value**.
- **Phần thêm là boolean** (đổi Type / Color / Size / Count không mất override): Has Label · Has Dot (mặc định bật) · Has Icon
  Leading + Icon Leading · Count Only. Không dùng badge chỉ có chữ: luôn có Dot hoặc Icon Leading
  (tắt Dot khi bật icon). Bảng danh sách dùng **Icon Leading** cho cột Trạng thái (góp ý 29/10).
- **Icon trạng thái / phân loại:** bộ icon badge trong `design-system/foundations/icon.md` mục 7 (navigation đang thực hiện,
  triangle-alert trễ, hourglass chờ xử lý, circle-check hoàn thành, clock chờ duyệt…).

### Số đo

| Phần | SM | MD | LG | Token |
|---|---|---|---|---|
| Cao | 22 | 24 | 28 | `chip/height-sm` · `size/3xl` · `chip/height-lg` |
| Cấu tạo | hàng phẳng | | | Chấm / icon / chữ / ô đếm là con trực tiếp, căn giữa dọc (DEC-310) |
| Lề phía chấm / icon | 6 | 8 | 10 | `space/sm` · `space/md` · `chip/padding-x-icon-lg` (Dot: 0) |
| Lề phía chữ | 10 | 12 | 14 | `chip/padding-x-sm` · `space/lg` · `chip/padding-x-lg` (Dot: 0) |
| **Count Only** (chỉ có số): đệm trái khung số | 4 | 4 | 4 | `space/xs` (= lề phía chữ − lề phía chấm/icon) → số cách đều hai bên 10 · 12 · 14 |
| Lề phải khi **có ô đếm** | 3 | 4 | 4 | `chip/count-inset` · `space/xs` — ô đếm cách đều trên, dưới, phải; bo ô đếm đồng tâm với badge |
| Icon → chữ → ô đếm | 4 | 4 | 4 | `space/xs` |
| Chấm → chữ | 6 | 6 | 6 | `space/sm` = `space/xs` + đệm phải khung chấm `space/xxs` 2 |
| Chữ nhãn | 12/18 · 600 | 12/16 · 600 | như MD | SM `type/chip-sm-strong`; MD, LG `type/caption-strong`; màu `color/chip/{tone}/fg`. Dot: 400, `color/text/primary` (DEC-310, thay phần chữ của DEC-277) |
| Khung chữ rộng tối đa | 160 | 160 | 160 | `size/11xl`, dài hơn cắt "…" một dòng |
| Chấm | 6 × 6 | 6 × 6 | 6 × 6 | `size/sm`; màu `color/chip/{tone}/fg` |
| Icon Leading | 14 | 14 | 14 | `icon/size/chip`; màu `color/chip/{tone}/fg`; nét 2.5 trên khung 24 (ngoại lệ DEC-300, DEC-309) |
| Ô đếm — cao | 16 | 16 | 20 | `size/xl` · `size/xl` · `size/2xl` |
| Ô đếm — đệm ngang | 6 | 6 | 6 | — |
| Ô đếm và Count Only — chữ | 12/16 · 400 | 12/16 · 400 | 12/16 · 400 | `chip/count-font-size` / `chip/count-line-height` — **không đậm**, cố định cả web và app (DEC-303, DEC-304) |
| Ô đếm — bo (Badge Color / Outline / Modern) | 3 | 3 | 4 | `chip/count-radius` · `radius/xs` |
| Ô đếm — bo (Pill) | tròn | tròn | tròn | `radius/full` |
| Ô đếm — nền | trắng (Modern, Dot: `color/bg/secondary`) | | | `color/bg/primary` · `color/bg/secondary` |
| Viền Outline / Modern | 1 | 1 | 1 | Pill Outline, Badge Outline: màu sắc 200 · Modern: `color/border/primary` |

### Trạng thái và nội dung

- **Tổ hợp hợp lệ:** Count Only chỉ dùng với Count=No và tắt Has Label (badge chỉ có số). Tắt Has Label chỉ hợp lệ khi bật
  Count Only — không dùng badge chỉ có chấm hoặc icon (trạng thái chỉ bằng màu, WCAG 1.4.1).
- **Không trộn Dot với Pill / Modern trong cùng một cột** — Dot không nền, không lề nên lạc tầng và lệch mép trái; Dot dành
  cho dòng thời gian, lịch sử, chỗ dày chữ (review 30/10).
- Outline (viền màu sắc 200) chỉ rõ trên nền không trắng; trên nền trắng dùng Color.

- Badge không bấm được, không có hover / focus. Chữ dài: khung chữ tối đa 160, cắt "…", tooltip hiện toàn văn (web).
- Trong bảng danh sách thử chữ nhãn 500 (góp ý 29/10, chưa có token chip 500) — **chưa áp** vào component; muốn đổi thì
  thêm token và ghi DEC mới thay DEC-277.

### Trợ năng

- Chữ nhãn 600 (SM 12/18, MD/LG 12/16) màu `color/chip/{tone}/fg` trên 8 nền chip đạt ≥ 4,5 : 1 ở Light (thấp nhất Green 5,10; Orange 6,05 sau DEC-311) và Dark (≥ 7,1); chữ trên Modern và Dot 17,9; số
  đếm trên ô trắng ≥ 5,18 (đo 29/10). Viền Outline / Modern và chấm màu là trang trí (badge không bấm được, chữ mang nghĩa)
  → không cần 3 : 1.
- **Số đếm và Count Only bắt buộc có nhãn ẩn** đủ ngữ cảnh: "3" → aria-label "3 lệnh chờ duyệt"; số đổi theo thời gian
  thực thì `aria-live="polite"`. Badge nằm trong tab / nút: gộp vào tên control (`aria-describedby` hoặc tên đủ) thay vì để
  badge thành phần tử riêng. App: accessibilityLabel đủ ngữ cảnh; số đổi thời gian thực — iOS announcement, Android
  `accessibilityLiveRegion="polite"`; trong tab / nút thì gộp nhãn vào control cha ("Chờ duyệt, 3 mục").
- **Chấm và Icon Leading là trang trí:** `aria-hidden="true"` (app: `accessibilityElementsHidden` /
  `importantForAccessibility="no"`); cả badge đọc thành một phần tử: nhãn rồi số đếm.
- Type Dot: chữ `text/primary` trên trắng 17,9 · `bg/secondary` 17,2 · dòng hover neutral/100 16,4 · dòng bấm giữ neutral/200
  14,2; chấm Dot màu fg trên trắng ≥ 5,18 (Orange), trên neutral/200 ≥ 4,11 — đạt 3 : 1 dù coi chấm mang nghĩa. Ô đếm
  Modern / Dot: `text/primary` trên `bg/secondary` 17,2. Orange Light nay 6,05 (DEC-311); Green 5,10 thấp nhất — đổi độ đậm chữ hoặc làm mờ thì đo lại
  (review 30/10).
- **Chữ cắt "…"**: cắt bằng CSS, DOM giữ đủ chữ để trình đọc màn hình đọc hết. Tooltip toàn văn mở cả khi focus dòng / ô
  chứa badge (hoặc `tabindex="0"` khi bị cắt), đóng bằng Esc, rê vào tooltip không tắt (WCAG 1.4.13). App: accessibilityLabel
  đủ chữ.

## Mobile

Cùng số đo Web (nhóm A). Chữ dài cắt "…", chạm giữ không mở tooltip — nội dung đầy đủ hiện ở màn chi tiết.

## Đối chiếu Astryx

- Status Chip v2 cũ (`l1/status-chip.md`, đã bỏ): bo tròn hẳn, nền nhạt, không viền, cỡ 24 → giữ làm Pill Color MD; thêm 4 Type
  theo Untitled, 3 cỡ, Icon Leading, ô đếm, Count Only. Kiểu Dot của Status Chip giữ thành Type Dot; số đo chấm/icon/lề lấy theo khung chú thích Status Chip (DEC-310).
- Bỏ X Close khỏi Badge (lượt Figma 1 có) — chip lọc dùng Tag.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
