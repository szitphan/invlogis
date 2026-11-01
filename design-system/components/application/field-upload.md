---
type: design-component
status: stale
status_prev: in-review
updated: 2026-10-29
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/foundations/icon.md
  - design-system/tokens.json
  - design-system/components/_work/field-upload/page.json
  - design-system/components/_work/field-upload/check.json
  - _workspace/decisions.md
---

# Field Upload

> Application · phiên bản 0.1.0 · Đang review · người phụ trách @szitphan · Figma: trang DS · Application components —
> Section `Field upload` 6975:226270 · `Field Upload` 6975:230197 · `_File row` 6975:226434 · `_Upload sheet` 6975:230317 ·
> `Demo · Field upload` 6978:232794 · DEC-306, DEC-307 · trang duyệt https://claude.ai/artifact/WeUYH8u8bXXTs9dsP7sT4u ·
> ảnh mốc `_work/field-upload/preview-web.png`, `preview-mobile.png`

Ô tải tệp trong form: nhãn, vùng chọn tệp, danh sách tệp đã chọn, gợi ý và lỗi. Nhóm B: web và app khác cấu tạo vùng
chọn (web kéo thả, app bấm mở sheet chọn nguồn), dùng chung dòng tệp. Mọi số đọc từ mode Platform của khung chứa.

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Nhãn trên khung** cả web lẫn app (D1 a), dấu `*` khi bắt buộc.
- **Vùng chọn tệp** — ba kiểu, chọn theo màn (D2, user giữ cả ba):
  - **Full** — Featured icon + "Bấm để tải lên hoặc kéo thả" + dòng định dạng, dung lượng. Form chỉ có một ô tải, màn nhập chứng từ.
  - **Compact** — một hàng: Featured gọn + chữ + nút Chọn tệp; vẫn kéo thả được. Form nhiều trường.
  - **Button only** — chỉ nút Chọn tệp; không kéo thả. Chỗ hẹp, bảng.
- **Ô nhận đúng 1 tệp**: có tệp rồi thì dòng tệp **thay chỗ** vùng chọn (D3 b); muốn đổi thì xoá rồi chọn lại.
- **Dòng tệp**: icon loại tệp (File type icon) hoặc ảnh nhỏ, tên, dòng phụ (dung lượng · định dạng hoặc trạng thái). Đang tải: **nền tiến
  độ chạy sau dòng** (D4 b), dòng không đổi cao. Nút xoá thùng rác **góc trên phải**, lỗi có link **Thử lại dưới tên** (D5 a).
- Viền vùng chọn **nét liền 1px**; đang kéo tệp vào đổi viền đậm 2px (D8 a).

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Field · khung | khoảng cách nhãn – vùng – gợi ý `control/icon-gap` | 6 |
| Nhãn | `type/label`, `color/text/tertiary_strong` | 14/20 nét 500 |
| Dấu bắt buộc `*` | `color/text/error/primary`, cách nhãn `upload/required-gap` | 3 |
| Gợi ý | `type/hint`, `color/text/tertiary` | 12/18 |
| Chữ lỗi | `type/hint`, `color/text/error/primary`; icon `icon/size/sm` dịch xuống `space/xxs`, cách chữ `control/icon-gap` | icon 14, lệch 2 |
| Vùng chọn · khung | nền `color/bg/primary`, viền `field/border-width` `color/border/primary`, bo `radius/card` | 1px, bo 12 |
| Vùng Full | lề `space/xl` trên dưới · `space/3xl` hai bên, khoảng dòng `field/text-inset` | 16 · 24, 4 |
| Vùng Compact | lề và khoảng cách `space/lg`; chữ rộng tối thiểu `upload/compact-text-min-width` | 12; 150 |
| Featured icon | khung `control/height/lg`, bo `radius/tab`, viền `color/border/disabled`, icon `icon/size/lg` `color/text/tertiary_strong`, khoảng dưới `space/md` | 40, bo 8, icon 20, 8 |
| Featured icon gọn (Compact) | khung `control/height/ml`, icon `icon/size/ml` | 36, icon 18 |
| Chữ vùng chọn | `type/body`, `color/text/tertiary`; link "Bấm để tải lên" `color/text/primary` nét 600, gạch chân cách `space/xxs` | 14/20, 2 |
| Dòng định dạng, dung lượng | `type/hint`, `color/text/tertiary` | 12/18 |
| Nút Chọn tệp | cao `control/height/md`, lề `space/lg`, bo `radius/tab`, viền `color/border/primary`, chữ `upload/action-font-size` nét 600 dòng `type/body/line-height`, icon `icon/size/md` | 32, 12, bo 8, chữ 13/20, icon 16 |
| Danh sách tệp | khoảng giữa dòng `layout/list-gap` | 8 (app 12) |
| Dòng tệp · khung | lề `space/lg` (trên dưới, trái), `field/edge-inset` (phải); khoảng `space/lg`; bo `radius/card`; viền `color/border/disabled`; nền `color/bg/primary` | 12 · 12 · 8, bo 12 |
| Nền tiến độ | `color/bg/disabled`, rộng theo % | — |
| Icon loại tệp / ảnh nhỏ | khung `control/height/lg`; ảnh nhỏ bo `radius/tab`, icon `color/fg/quaternary` | 40, bo 8 |
| Tên tệp | `type/body` nét 500, `color/text/primary`; cắt giữa, giữ đuôi tệp | 14/20 |
| Dòng phụ | `type/hint`, `color/text/tertiary`, cách tên `upload/meta-offset`, khoảng `field/edge-inset`; vạch chia `upload/divider-width` × `size/lg` màu `color/border/primary` | 12/18; vạch 1 × 12 |
| Trạng thái Đang tải | `color/text/tertiary_strong` (DEC-307), icon `icon/size/sm`, khoảng `field/text-inset` | "Đang tải 64%" |
| Trạng thái Xong / Lỗi | `color/text/success/primary` · `color/text/error/primary` | — |
| Link Thử lại | chữ `upload/action-font-size` nét 600 dòng `type/hint/line-height`, `color/text/error/primary`, cách tên `space/sm`; vùng bấm vô hình `touch/min` | 14/18, 6; bấm 24 |
| Nút xoá | `Button` Ghost icon: khung `control/height/md`, bo `radius/tab`, icon `icon/size/md` `color/fg/quaternary`; lệch `space/sm` · `space/xxs` | 32, icon 16, lệch 6 · 2 |
| Vòng focus | `focus/width`, cách `focus/width`, màu `color/focus/ring` | 2, cách 2 |

### Biến thể

- `Field Upload`: Dropzone = Full · Compact · Button only × State (mục dưới) × Has Hint × Has Error.
- `_File row`: Status = Uploading · Done · Error × Lead = File type icon · Thumbnail. Phần con, dùng riêng trong danh sách tệp.

### Trạng thái

| Trạng thái | Vùng chọn | Dòng tệp |
|---|---|---|
| Mặc định | như Cấu tạo | — |
| Rê chuột | nền `color/bg/disabled`, viền `color/border/input` | nút xoá nền `color/bg/selected`, icon `color/text/primary` |
| Đang kéo tệp vào | viền `size/xxs` `color/text/primary`, nền `color/bg/primary`; icon Featured `color/text/primary` | — |
| Focus (bàn phím) | vòng focus quanh vùng / nút | vòng focus quanh nút |
| Khoá | nền `color/bg/disabled`, mờ `upload/disabled-opacity` | — |
| Lỗi | viền `color/border/error`; nút Chọn tệp viền `color/border/error` | viền `color/border/error`, dòng phụ đỏ, link Thử lại |
| Đang tải | — | nền tiến độ, dòng phụ "Đang tải n%" |

### Kích thước

Một cỡ. Rộng theo cột form; Compact cần tối thiểu chỗ cho chữ 150 cộng nút.

### Nên và không nên

- Nên: ghi định dạng và dung lượng tối đa ở dòng dưới vùng chọn ("PDF, XML · tối đa 10 MB").
- Nên: lỗi một tệp báo ở dòng tệp đó, có Thử lại; lỗi cả ô (thiếu tệp bắt buộc) báo ở chữ lỗi dưới ô.
- Không: dùng Button only khi người dùng thường kéo tệp từ máy (nhập chứng từ hàng loạt) — mất kéo thả.
- Không: giữ vùng chọn bên cạnh tệp ở ô nhận 1 tệp — dễ thay nhầm (D3).

### Trợ năng — chấm theo WCAG 2.2

- 1.4.3: chữ "Đang tải" đạt ≥ 4,5:1 trên nền tiến độ nhờ `color/text/tertiary_strong` (trước 4,35:1, DEC-307).
- 1.4.11: viền vùng chọn `color/border/primary` là trang trí; vùng nhận biết bằng icon + chữ. Viền lỗi kèm chữ lỗi, không chỉ màu.
- 2.1.1: vùng kéo thả là một nút (Enter / Space mở hộp chọn tệp); kéo thả chỉ là đường thêm.
- 2.5.8: link Thử lại có vùng bấm vô hình 24; nút xoá 32.
- 4.1.2: nút xoá đọc "Xoá {tên tệp}", Thử lại đọc "Tải lại {tên tệp}".
- 4.1.3: tiến độ đọc bằng vùng thông báo lịch sự theo mốc (bắt đầu, xong, lỗi), không đọc từng %; lỗi dùng `role="alert"`.
- 3.3.1: chữ lỗi gắn với ô bằng `aria-describedby`.
- 3.3.2 · 4.1.2: ô bắt buộc khai `aria-required="true"` (app: nhãn trợ năng "bắt buộc"); dấu `*` ẩn với trình đọc màn hình.
- 4.1.2 nút xoá khi Đang tải: tên đọc "Huỷ tải {tên tệp}"; huỷ xong báo bằng vùng thông báo lịch sự.
- 1.4.11: nền tiến độ chỉ là trang trí (`aria-hidden`), số % bắt buộc đi kèm; bỏ số % thì dải phải đạt ≥ 3:1.
- 2.3.3: icon Đang tải dừng xoay khi bật giảm chuyển động (`prefers-reduced-motion`, tuỳ chọn giảm chuyển động iOS/Android).

### Thuộc tính

`Label`, `Required`, `Hint`, `Has Hint`, `Error`, `Has Error`, `Dropzone`, `Accept` (dòng định dạng), `Max size`, `Multiple`
(một hay nhiều tệp — một tệp thì dòng tệp thay vùng chọn).

### Thành phần lồng

`Button` (Secondary SM cho Chọn tệp; Ghost icon cho xoá), Featured icon, File type icon (Misc icons), icon Lucide.

### Được dùng trong

Màn mẫu trên trang duyệt: Hoá đơn đầu vào (web), Chứng từ LVT-2026-0412 (web). Feature dùng: chưa gắn.

### Kiểm máy

29/10: `ds-foundation-check.py` exit 0 (153 dòng, 0 chưa khai, 0 không soi được).
30/10 Figma: layout_audit 0 lỗi chặn (dải tiến độ bị dòng bo góc cắt — cố ý); auditDesignSystem `Field Upload` 1,00 · `_File row` 0,99 ·
`_Upload sheet` 1,00; a11y_audit 1 fail = chữ nút Disabled 2,31:1 (WCAG 1.4.3 miễn cho control bị khoá); nút xoá 32 ≥ 24; kiểm tên
DEC-264 0 lỗi. Kiểm mất hình (`check-mat-hinh.js`): không áp — Section theo khuôn Map marker, chưa có khung `Tài liệu · …`.

## Mobile

> Khối Mobile đặt mode Platform = Mobile.

### Tổng quan

- Nhãn trên khung như web (D1 a).
- **Một ô bấm → sheet 3 lựa chọn** Chụp ảnh / Thư viện / Tệp (D6 a).
- Ảnh đã chụp hiện bằng **dòng tệp có ảnh nhỏ** như web (D7 b).

### Cấu tạo

Như Web; khác:

| Phần | Token | Giá trị (Mobile) |
|---|---|---|
| Nhãn | `type/caption`, `color/text/tertiary_strong` | 12/16 |
| Ô bấm tải lên | cao tối thiểu `upload/app-tap-min-height`, bo `radius/card`, lề và khoảng `space/lg`, viền `color/border/primary`, nền `color/bg/primary` | 72, bo 16, 14 |
| Featured trong ô bấm | khung `featured-icon/size`, tròn `radius/full`, nền `color/bg/disabled`, icon `icon/size/lg` (icons.md mục 3.1) | 48 / icon 24 |
| Dòng tệp | bo `radius/field`, lề phải `space/xs`; tên `type/body` | bo 12, lề 4, tên 15 |
| Nút xoá | khung `control/height/md` | 42 |
| Sheet chọn nguồn | bo `upload/sheet-radius` (lệch DEC-259, DEC-307), lề hai bên `field/edge-inset`, lề trên `space/md`, lề dưới `space/3xl`, nền `color/bg/primary`, scrim `color/bg/overlay` | bo 28 |
| Thanh kéo | `size/xs`, `radius/xxs`, nền `color/bg/quaternary` (DEC-321), cách dưới `space/lg` | 4, bo 2, rộng 36 |
| Tiêu đề sheet | `type/title-3` nét 600, cách dưới `space/sm` | 18/28, 6 |
| Mục sheet | cao `control/height/lg`, khoảng `space/lg`, `type/body`, icon `icon/size/md`, vạch `color/border/disabled` | 52, icon 20 |

### Biến thể · Trạng thái · Kích thước · Nên và không nên · Thuộc tính · Thành phần lồng

Như Web. Không có trạng thái Đang kéo tệp vào và Rê chuột.

### Trợ năng — chấm theo WCAG 2.2

2.5.8 nâng lên 44 theo DEC-138 (nút xoá 42 thêm vùng bấm vô hình; link Thử lại vùng bấm 44). Sheet giữ focus trong sheet, đóng
xong focus về ô bấm. Còn lại như Web.

### Được dùng trong

Màn mẫu trên trang duyệt: Giao hàng — ảnh tại điểm giao, Ghi chi phí — ảnh hoá đơn (app tài xế). Feature dùng: chưa gắn.

### Kiểm máy

30/10: chung lượt kiểm với Web (khối Mobile 6978:232000, mode Platform = Mobile); demo Giao hàng / Ghi chi phí layout_audit 0 lỗi.

## Còn mở

- `control/height/ml` (DEC-304) chưa có trong `tokens.json` — Featured gọn 36 đang trỏ token này.
- Figma chưa có biến thể icon `Size=18` (DEC-306) — thêm khi dựng.
- Thanh kéo sheet rộng 36 chưa có token riêng (đề xuất sheet/grabber-width); máy chỉ khớp được số với `control/height/sm`.

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
