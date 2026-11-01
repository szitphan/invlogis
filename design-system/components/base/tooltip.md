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
  - design-system/components/_work/tooltip/page.json
  - _workspace/decisions.md
---

# Tooltip · Help icon

> Base · phiên bản 0.1.0 · Đã duyệt · người phụ trách @szitphan · Figma: Section `Tooltips` (6657:165303) trang DS · Base
> components — `Tooltip` 6657:165642 · `Help icon` 6657:166386 · `Help sheet` 6823:408 · DEC-206, DEC-280, DEC-300, DEC-301 ·
> thay tài liệu cũ `l1/tooltip.md` (đã bỏ, DEC-312) · trang duyệt
> https://claude.ai/artifact/3W2p5p8gWLhKDsx7NKfJji · ảnh mốc `_work/tooltip/preview-web.png`, `preview-mobile.png`

Hai component và một mẫu app: **Tooltip** (nhãn nổi khi rê chuột hoặc focus, chỉ web), **Help icon** (dấu ? sau nhãn ô
nhập để mở giải thích) và **Help sheet** (app không có rê chuột: chạm Help icon mở sheet, DEC-280). Nhóm C (DEC-279):
Tooltip chỉ có ở web; Help icon có ở cả hai, khác hành vi. Tài liệu `l1/tooltip.md` cũ đã bỏ (DEC-312).

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Type Short** — 1–4 từ, một dòng: tên hành động của nút chỉ có icon ("Xuất Excel"), tên người của avatar, toàn văn
  chữ bị cắt "…" (tên khách, địa chỉ giao).
- **Type Supporting** — tiêu đề đậm + một câu giải thích, mở từ Help icon cạnh nhãn ô nhập ("Tổng trọng lượng" → "Tính
  cả vỏ container và hàng."). Không dùng cho thông tin phải đọc mới làm tiếp được (lỗi, hướng dẫn bắt buộc): dùng chữ phụ
  dưới ô hoặc thông báo.
- **Nền tối** (`color/bg/primary_solid`), chữ trắng, **có mũi tên** chỉ vào đối tượng (DEC-301). Không icon, không nút, không link
  trong tooltip.
- **Placement:** mặc định Arrow=Bottom Center (tooltip nằm trên đối tượng); gần mép trên thì đổi phía; đối tượng sát mép trái /
  phải dùng Bottom Left / Bottom Right để tooltip không tràn màn. Neo vào vùng rộng (dòng bảng, ô) thì Arrow=None.
- **Hiện, ẩn:** hiện khi rê chuột hoặc focus bằng Tab; Help icon còn hiện khi bấm; ẩn khi rời đi, bấm ra ngoài hoặc Esc;
  rê từ đối tượng sang tooltip thì vẫn hiện.

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Nền, mũi tên | `color/bg/primary_solid` | #171717 (Dark #F5F5F5) |
| Bóng | `elev/1` | — |
| Chữ (Short) | `type/caption` nét 600, màu `color/text/inverse` | 12/16, trắng |
| Lề (Short) | `space/xs` × `space/md` | 4 × 8 |
| Bo | `radius/md` | 8 |
| Rộng (Short) | ôm chữ, tối đa `tooltip/max-width`, quá thì xuống dòng | 240 |
| Tiêu đề (Supporting) | `type/caption` nét 600, `color/text/inverse` | 12/16 |
| Mô tả (Supporting) | `type/caption` nét 400, `color/text/inverse` mờ 86% | 12/16 |
| Lề (Supporting) | `space/md` × `space/lg` | 8 × 12 |
| Tiêu đề → mô tả | `space/xs` | 4 |
| Rộng (Supporting) | tối đa `width/xs` | 320 |
| Mũi tên | `size/md` × `size/xs`; Bottom Left / Bottom Right cách góc 12 | 8 × 4 |
| Cách đối tượng | `space/xs` + `size/xs`; offset do chỗ đặt (instance cha / code) lo, component chỉ gồm thân + mũi tên | 4 + 4 |
| Help icon | icon `circle-question-mark` cỡ `icon/size/md`, nét 2 trên khung 24 (DEC-300); màu `color/fg/quaternary`, Hover `color/fg/secondary` | 16; vùng rê chuột 24 |

### Biến thể

- `Tooltip`: Type = Short · Supporting × Arrow = None · Top Center · Bottom Center · Bottom Left · Bottom Right · Left ·
  Right (14, chốt 26/10, trang Chốt biến thể Base). Tên trục Arrow theo vị trí mũi tên trên tooltip: Arrow=Bottom Center
  nghĩa là tooltip nằm trên đối tượng.
- `Help icon`: State = Default · Hover · Focus.

### Trạng thái

Tooltip không có State riêng, hiện theo đối tượng: Default ẩn · Hover hiện · Focus (Tab) hiện, vòng focus của đối tượng
vẫn thấy · rời đi / Esc ẩn. Help icon: Default · Hover (đổi màu icon) · Focus (vòng focus chung); đang mở giữ màu Hover.

### Kích thước

Một cỡ. Chữ dài xuống dòng: Short tối đa 240, Supporting tối đa 320; không cắt chữ trong tooltip.

### Nên và không nên

1. **Nên:** Short 1–4 từ, nói đúng hành động ("Xuất Excel"). **Không nên:** lặp lại chữ đã hiện trên nút có chữ.
2. **Nên:** Supporting một tiêu đề + một câu. **Không nên:** đoạn hướng dẫn dài phải giữ chuột để đọc — đưa ra chữ phụ dưới ô.
3. **Nên:** mỗi Help icon giải thích đúng một trường. **Không nên:** đặt Help icon cho mọi trường của form.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (≥ 4,5) | ✓ | chữ 17,93; mô tả mờ 86% 13,45 (Dark: chữ 18,16, mô tả 12,99) |
| 1.4.13 Nội dung hiện khi rê, focus | ✓ | đóng bằng Esc, rê lên tooltip được, giữ tới khi rời đi; code có vùng nối vô hình phủ khoảng hở 8 giữa đối tượng và tooltip (hoặc chờ ~100 ms rồi mới ẩn) |
| 2.1.1 Bàn phím | ✓ | hiện khi focus bằng Tab; Help icon là nút, Enter / Space mở; ô bảng có chữ bị cắt phải nhận focus (`tabindex=0`) hoặc có lối khác (trang chi tiết) |
| 4.1.2 Tên, vai trò | ✓ | đối tượng nối tooltip bằng `aria-describedby`; Help icon `aria-label` "Giải thích {tên trường}" + `aria-expanded`; nút Icon Only có `aria-label` trùng chữ tooltip Short |
| 1.4.11 Tương phản ngoài chữ | ✓ | Help icon 4,74 trên trắng · 4,54 trên #FAFAFA · 4,35 trên #F5F5F5 · Hover 10,37 · Dark 7,85 |
| 2.4.7 Focus thấy được | ✓ | Help icon Focus: vòng `color/focus/ring` dày 2 trong khung 24, 15,13 trên trắng |
| 2.5.8 Vùng bấm (≥ 24) | ✓ | Help icon vùng vô hình 24; tooltip không bấm được |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Type | Biến thể | Short | Short · Supporting |
| Arrow | Biến thể | None | None · Top Center · Bottom Center · Bottom Left · Bottom Right · Left · Right |
| Title | Chữ | Thêm | Short: tên hành động / tên người / toàn văn; Supporting: tiêu đề |
| Description | Chữ | Mô tả ngắn giải thích thêm. | chỉ hiện ở Type Supporting; Short bỏ qua giá trị này |

### Thành phần lồng

Tooltip: khung + mũi tên (phần con `.tooltip / Arrow`), không chứa component khác. Help icon: icon `circle-question-mark`.
Button và Avatar lồng Tooltip Type Short qua thuộc tính `Tooltip` (giữ như `l1/tooltip.md` (đã bỏ, DEC-312)).

### Được dùng trong

Mọi nút chỉ có icon trên web (thanh công cụ bảng, đầu màn chi tiết: "Sao chép mã lệnh") · tên khách, địa chỉ bị cắt
trong bảng và chi tiết · Header web: nút tài khoản chỉ có avatar (DEC-290) · cross-process-flow (search-process,
view-process): giải thích bước, tên dài · form có trường cần giải thích (Tổng trọng lượng, Nhiệt độ cài đặt).

### Token

Số đo ở bảng Cấu tạo; màu ở Phần máy.

### Kiểm máy

29/10 trên preview: `ds-foundation-check.py` 0 chưa khai · 0 chưa quyết (`_work/tooltip/check.json`). Figma 29/10 (Section
Tooltips): layout_audit 0 lỗi · a11y_audit 0 lỗi · kiểm tên DEC-264 0 lỗi · auditDesignSystem Tooltip 0,99, Help sheet 0,93
(tiêu đề sheet dòng 24 tách khỏi style `type/title-3`, cỡ và dòng vẫn gắn biến; bo 5 của khung set do Figma tự đặt).
Nét icon theo DEC-300 (2 trên khung 24) đã áp lên bộ icon Figma 29/10.

## Mobile

> Khối Mobile đặt mode Platform = Mobile.

### Tổng quan

- **Không có Tooltip trên app** (DEC-206): không rê chuột. Nút chỉ có icon dùng nhãn trợ năng; chữ bị cắt xem đủ ở trang
  chi tiết (bảng "Thay bằng gì" ở `l1/tooltip.md` (đã bỏ, DEC-312) phần Mobile vẫn áp).
- **Help icon → Help sheet** (DEC-280): chạm dấu ? cạnh nhãn ô mở sheet từ dưới lên gồm thanh kéo, tiêu đề (tên trường),
  nội dung giải thích và nút **Đã hiểu**. Không có nút X ở đầu sheet (DEC-301). Đóng bằng nút, chạm lớp phủ hoặc vuốt xuống.

### Cấu tạo

| Phần | Token | Giá trị (Mobile) |
|---|---|---|
| Help icon | icon `circle-question-mark` cỡ `icon/size/md`, nét 2 (DEC-300), màu `color/fg/quaternary` | 20; vùng chạm 44 (`touch/min`) |
| Lớp phủ | `color/bg/overlay` | — |
| Sheet · khung | nền `color/bg/primary`; bo trên `radius/overlay` (DEC-259); không bóng — nằm trên lớp phủ (R3) | 24 |
| Sheet · lề | trên `space/md` · ngang `space/2xl` · dưới `space/3xl` | 8 · 20 · 24 |
| Thanh kéo | `color/bg/quaternary` (DEC-321), bo `radius/badge`; cách trên `space/xs`, cách dưới `space/xl` | 36 × 4 |
| Tiêu đề | `type/title-3/size` nét 600, dòng `help-sheet/title-line-height`, `color/text/primary`, tối đa 2 dòng; cách dưới `space/md` | 18/28 |
| Nội dung | `type/body`, `color/text/tertiary_strong`; cách dưới `space/2xl` | 14/20 |
| Nút Đã hiểu | `Button` Secondary · Label · MD, rộng hết sheet (DEC-301) | 42 |

### Biến thể · Trạng thái · Kích thước

Help sheet một kiểu; sheet cao theo nội dung, **tối đa 90% màn**: quá thì phần Nội dung tự cuộn, thanh kéo, tiêu đề và nút
Đã hiểu luôn hiện (review R1, 29/10). Tiêu đề tối đa 2 dòng rồi cắt "…" (R2).

### Nên và không nên

Như Web. Thêm: **Không nên** đặt nút khác ngoài "Đã hiểu" trong Help sheet — sheet chỉ để đọc.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 2.5.8 Vùng chạm (≥ 44, DEC-138) | ✓ | Help icon vùng 44 (`touch/min` theo mode Mobile); nút Đã hiểu Figma 42, code thêm vùng vô hình tới 44 (trên dưới nút còn trống 20 / 24) |
| 4.1.2 Tên, vai trò | ✓ | Help icon "Giải thích {tên trường}"; sheet là dialog có tiêu đề |
| 2.4.3 Thứ tự focus | ✓ | mở sheet: focus vào tiêu đề, chỉ đi vòng trong sheet, lớp phủ không nhận focus; nút Back / Esc đóng và đưa focus về Help icon |
| 1.4.3 Tương phản chữ | ✓ | nội dung 7,81 (Dark 7,85) · tiêu đề 17,93 · nhãn nút 16,44 |
| 1.4.11 Tương phản ngoài chữ | — | thanh kéo 1,48 chỉ là gợi ý; đóng được bằng nút Đã hiểu hoặc chạm lớp phủ (2.5.7 đạt) |
| 1.4.4 / 1.4.10 Chữ lớn | ✓ | sheet tối đa 90% màn, nội dung tự cuộn, nút Đã hiểu luôn hiện; tiêu đề xuống 2 dòng |

### Thuộc tính · Thành phần lồng

Help sheet: lớp chữ `Title`, `Body`; lồng `Button` Secondary MD, tắt `Has Tooltip` (nhãn "Đã hiểu"). Help icon như Web.

### Được dùng trong

Form app có trường cần giải thích (Thông tin hàng: Tổng trọng lượng).

### Kiểm máy

29/10: a11y_audit Section Tooltips 0 lỗi; số tương phản đo tay từ biến Figma (Light, Dark). Help icon đổi cỡ 20 và vùng 44
theo mode Platform = Mobile của chính set (không cần biến thể riêng). Mẫu chữ dài Help sheet 6927:218493 (cao 350). Trên Figma mỗi sheet nằm trong ô mẫu nền
`color/bg/overlay` (6927:218508, 6927:218509) để thấy mép sheet. Review 29/10: R1–R4 đã sửa.

## Đối chiếu Astryx

- Tooltip v2 cũ chỉ có một kiểu chữ Regular, 4 Placement → thêm Type Supporting (tiêu đề + mô tả), Arrow 7 kiểu gồm
  Bottom Left / Bottom Right / None; chữ Short nét 600 như Untitled.
- Bóng tự do → `elev/1`. Help icon "i" (dễ nhầm icon Alert info) → dấu ?.
- App: v2 cũ chỉ ghi "không dùng" → thêm Help sheet có nút Đã hiểu Secondary (DEC-280, DEC-301).

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
