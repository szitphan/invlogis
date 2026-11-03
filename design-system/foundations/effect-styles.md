---
type: design-foundations
status: draft
updated: 2026-11-02
links:
  - design-system/foundations/README.md
  - design-system/tokens.json
  - design/_ref/untitled-ui/05-effects.md

---

# Foundations · Lớp nổi, làm mờ nền

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (8.x) để các DEC và spec trích "foundations mục 8…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng). Nguồn số: `design/_ref/untitled-ui/05-effects.md` mục 1.

## 8. Lớp nổi (DEC-327, thay phần số của DEC-125, DEC-137)

Tên và số theo đúng thang Untitled, 7 bậc, kể cả spread âm. Không có tầng vai riêng: vai tra ở bảng dưới. Tên CSS = tên token (`shadow/lg` → `--shadow-lg`).

| Style | Lớp (x y nhoè spread · biến màu · Sáng) |
|---|---|
| `shadow/none` | Không bóng; chỉ có ở code (`--shadow-none`), không có style Figma |
| `shadow/xs` | 0 1 2 0 · `color/shadow/xs` · 5% |
| `shadow/sm` | 0 1 3 0 · `sm_01` · 10% + 0 1 2 −1 · `sm_02` · 10% |
| `shadow/md` | 0 4 6 −1 · `md_01` · 10% + 0 2 4 −2 · `md_02` · 6% |
| `shadow/lg` | 0 12 16 −4 · `lg_01` · 8% + 0 4 6 −2 · `lg_02` · 3% + 0 2 2 −1 · `lg_03` · 4% |
| `shadow/xl` | 0 20 24 −4 · `xl_01` · 8% + 0 8 8 −4 · `xl_02` · 3% + 0 3 3 −1,5 · `xl_03` · 4% |
| `shadow/2xl` | 0 24 48 −12 · `2xl_01` · 18% + 0 4 4 −2 · `2xl_02` · 4% |
| `shadow/3xl` | 0 32 64 −12 · `3xl_01` · 14% + 0 5 5 −2,5 · `3xl_02` · 4% |

### Bảng tra vai

| Vai | Bóng | Viền | Nền mặt | Dùng cho |
|---|---|---|---|---|
| Phẳng | `shadow/none` | — | `color/bg/primary` | Ô nhập, khối phụ trong thẻ |
| Thẻ | `shadow/xs` | `shadow/xs-border` | `color/bg/primary` | Thẻ; Tối giữ cả bóng và viền |
| Menu | `shadow/lg` | `shadow/lg-border` | `color/bg/primary_alt` | Menu thả, popover, gợi ý ô tìm, menu tầng ẩn, menu tài khoản |
| Lớp phủ | `shadow/xl` | `shadow/xl-border` | `color/bg/primary_alt` | Dialog, sheet, toast |
| Marker bản đồ | `shadow/sm` | giữ viền của component | theo component | Nhãn, chấm, cụm trên bản đồ (DEC-334 vh17); nổi trên ảnh nền bản đồ, thấp hơn menu; bóng trên từng chấm chưa đo giá khi nhiều xe |

`shadow/md`, `2xl`, `3xl` có sẵn để tra cùng Untitled, chưa gán vai. Cần dùng thì thêm dòng vào bảng này trước.

Đổi từ tên cũ: `elev/0` → `shadow/none`, `elev/1` → `shadow/xs`, `elev/2` → `shadow/lg`, `elev/3` → `shadow/xl`. Số đổi theo: menu cao 4 → 12, dialog cao 16 nhoè 40 → cao 20 nhoè 24, màu đen thay #101828.

### Viền đi kèm

| Token | Sáng | Tối |
|---|---|---|
| `shadow/xs-border` | `color/border/secondary` | `color/border/secondary` |
| `shadow/lg-border` | `color/border/secondary` | `color/border/secondary` |
| `shadow/xl-border` | trong suốt | `color/border/secondary` |

Dialog, sheet, toast ở Tối có viền vì mặt `color/bg/primary_alt` #202020 trên lớp phủ chỉ cách 1,15:1, thêm viền #2E2E2E được 1,38:1. Sáng giữ không viền.

Trên Figma viền gắn riêng bằng biến màu. CSS đọc `--shadow-*-border`.

### Màu bóng theo chế độ

15 biến đúng tên Untitled trong Semantic (`color/shadow/xs`, `sm_01`, `sm_02`, `md_01`, `md_02`, `lg_01`, `lg_02`, `lg_03`, `xl_01`, `xl_02`, `xl_03`, `2xl_01`, `2xl_02`, `3xl_01`, `3xl_02`).

| Chế độ | Giá trị |
|---|---|
| Sáng | Đen + đúng % Untitled trong bảng mục 8 (`alpha/black/3`, `4`, `5`, `6`, `8`, `10`, `14`, `18`) |
| Tối | Lớp `_01` (tán chính) `alpha/black/60`; còn lại kể cả `xs` `alpha/black/40` |

Giá trị Tối là của mình: Untitled chưa đọc được Tối trong Figma, code của họ giữ nguyên 5–18%.

`--shadow-*`, `--shadow-*-border` khai ngay trong khối Semantic Sáng và Tối của `tokens.css`, nên khung `data-theme` lồng trong trang khác chế độ tính lại đúng, không cần vá ở trang.

Thẻ ở Tối: bóng `shadow/xs` đen 40% chỉ tạo mép 1,09:1 so với nền #191919, ranh giới do viền mang; vẫn giữ một style chung cho hai chế độ (DEC-125).

### 8.1 Làm mờ nền (DEC-258, DEC-327)

| Token | Giá trị | Áp vào | Nền đi kèm |
|---|---|---|---|
| `backdrop-blur/sm` | 8 | Đầu màn, thanh công cụ dính trên cùng khi cuộn | `color/bg/primary_blur` |
| `backdrop-blur/md` | 16 | Thanh điều hướng nổi app (DEC-160), thanh hành động nổi đáy màn | `color/bg/primary_blur` |
| `backdrop-blur/lg` | 24 | Nền sau dialog, sheet | `color/bg/overlay` |
| `backdrop-blur/xl` | 40 | Giữ cho đủ thang, chưa dùng | — |

| Token nền | Sáng | Tối |
|---|---|---|
| `color/bg/overlay` | `neutral/950` 35% | `neutral/950` 35% |
| `color/bg/overlay_solid` | `neutral/950` 50% | `neutral/950` 50% |
| `color/bg/primary_blur` | trắng 70% | `dark/0` #191919 70% |

- **Máy yếu lùi về 50%:** thiết bị không chạy được làm mờ dùng `color/bg/overlay_solid`, không blur. **Phải đo trên máy thật (Android của lái xe) trước khi vào app**; chưa có số đo.
- Lớp tối, rãnh vòng tiến độ đè lên ảnh (Avatar đang tải, ảnh đang tải lên) dùng `color/bg/overlay_solid`, không blur, vì chữ trắng trên ảnh cần đủ tương phản (DEC-321).

Web: `backdrop-filter: blur(var(--backdrop-blur-md))`. Flutter: `BackdropFilter(ImageFilter.blur(sigmaX: InvBlur.backdropBlurMd, …))`.

### Không lấy từ Untitled

- 7 style `focus-ring*`: vòng focus của mình là lớp riêng, xem `design-system/foundations/touch-focus.md` mục 9.
  Ô nhập đang gõ giữ viền + `box-shadow: inset 0 0 0 1px` (DEC-321, DEC-339): ngoại lệ của câu "Không dùng `box-shadow` để vẽ vòng" trong DEC-327, vì đây là viền ô, không phải vòng; mục 9.7.
- `shadow-xs-skeuomorphic`: nút giữ phẳng (DEC-119, DEC-327).
