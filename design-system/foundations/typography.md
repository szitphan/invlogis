---
type: design-foundations
status: draft
updated: 2026-11-01
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Chữ

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (4.x) để các DEC và spec trích "foundations mục 4…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 4. Chữ

Một bộ cho web và app, không tách mode (DEC-322). Component có khối Mobile tự chọn vai phù hợp.

### 4.1 Font (DEC-121)

Tiêu đề từ 18 trở lên **Cal Sans** (một độ đậm), chữ thường **Inter**, mã **JetBrains Mono**.

### 4.2 Hai tầng: thang cỡ và vai (DEC-322)

**Tầng 1: thang cỡ.** Biến `font-size/*`, `line-height/*`, tên và số theo Untitled UI v8. `line-height/xs-tight` 16 là bậc riêng cho dòng đơn dày.

| Bậc | Cỡ / dòng | Giãn |
|---|---|---|
| `display-2xl` | 72 / 90 | −2% |
| `display-xl` | 60 / 72 | −2% |
| `display-lg` | 48 / 60 | −2% |
| `display-md` | 36 / 44 | −2% |
| `display-sm` | 30 / 38 | 0 |
| `display-xs` | 24 / 32 | 0 |
| `xl` | 20 / 30 | 0 |
| `lg` | 18 / 28 | 0 |
| `md` | 16 / 24 | 0 |
| `sm` | 14 / 20 | 0 |
| `xs` | 12 / 18 (`xs-tight` 16) | 0 |

**Tầng 2: text style theo vai.** Tên `type/{vai}`, cỡ và dòng trỏ về thang. Component chỉ dùng tầng này.

| Style | Font | Nét | Cỡ / dòng | Bậc | Dùng cho |
|---|---|---|---|---|---|
| `type/display-2xl` | Cal Sans | 400 | 72 / 90 | `display-2xl` | Số rất lớn, màn giới thiệu |
| `type/display-xl` | Cal Sans | 400 | 60 / 72 | `display-xl` | Số rất lớn, màn giới thiệu |
| `type/display-lg` | Cal Sans | 400 | 48 / 60 | `display-lg` | Số lớn, màn giới thiệu |
| `type/display-md` | Cal Sans | 400 | 36 / 44 | `display-md` | Số lớn trên màn rộng |
| `type/display` | Cal Sans | 400 | 30 / 38 | `display-sm` | Số lớn, màn giới thiệu |
| `type/title-1` | Cal Sans | 400 | 24 / 32 | `display-xs` | Tiêu đề màn |
| `type/title-2` | Cal Sans | 400 | 20 / 30 | `xl` | Tiêu đề dialog, sheet, khối lớn |
| `type/title-3` | Cal Sans | 400 | 18 / 28 | `lg` | Tiêu đề khối, thẻ |
| `type/body-lg` | Inter | 400 | 16 / 24 | `md` | Chữ 16, chưa có chỗ dùng trong màn vận hành |
| `type/body-lg-medium` | Inter | 500 | 16 / 24 | `md` | Như trên, nét 500 |
| `type/body-lg-strong` | Inter | 600 | 16 / 24 | `md` | Như trên, nét 600 |
| `type/heading` | Inter | 600 | 14 / 20 | `sm` | Tiêu đề khối nhỏ, biển số, tiêu đề thông báo |
| `type/body` | Inter | 400 | 14 / 20 | `sm` | Chữ đọc, giá trị, trên cả web và app |
| `type/label` | Inter | 500 | 14 / 20 | `sm` | Nút, nhãn, tab |
| `type/caption` | Inter | 400 | 12 / 16 | `xs`, `xs-tight` | Thông tin phụ, thời gian, dòng đơn |
| `type/caption-strong` | Inter | 600 | 12 / 16 | `xs`, `xs-tight` | Chữ chip trạng thái Soft (DEC-200) |
| `type/caption-caps` | Inter | 500 | 12 / 16 | `xs`, `xs-tight` | Tên cột bảng, nhãn nhóm menu, tiêu đề nhóm nhỏ |
| `type/hint` | Inter | 400 | 12 / 18 | `xs` | Gợi ý dưới ô, chữ lỗi, dòng phụ nhiều dòng (DEC-306) |
| `type/chip-sm` | Inter | 400 | 12 / 18 | `xs` | Chữ chip, badge, tag cỡ SM (DEC-261) |
| `type/chip-sm-strong` | Inter | 600 | 12 / 18 | `xs` | Chữ chip đã chọn cỡ SM (DEC-261) |
| `type/code` | JetBrains Mono | 400 | 12 / 16 | `xs`, `xs-tight` | Mã lệnh, mã chứng từ |
| `type/prose-quote` | Inter | 500 | 20 / 30 | `xl` | Trích dẫn trong `.prose`, không nghiêng |
| `type/prose-code` | JetBrains Mono | 700 | 14 / 20 | `sm` | Mã trong dòng của `.prose` |

Token cỡ chữ ở component trỏ về thang: `chip/font-size-sm`, `chip/line-height-sm` (12/18) · `chip/count-*`, `avatar-label/subtitle-*` (12/16) · `help-sheet/title-line-height` (28) · `upload/action-font-size` (14).

### 4.3 Độ đậm (DEC-133, DEC-322)

| Chữ | Luật |
|---|---|
| Tiêu đề từ 18 | Cal Sans, một độ đậm. Không đặt `font-weight` khác 400: trình duyệt sẽ làm đậm giả, các lớp `.type-*` bật `font-synthesis: none` |
| Tiêu đề khối nhỏ (`heading` 14) | Inter 600 |
| Chữ đọc | Inter 400 |
| Nhãn, nút, tab (`label`) | Inter 500, web và app như nhau |
| Tránh | Inter 700 cho chữ đọc · Cal Sans dưới 18 · Ultralight, Thin, Light |
| Viết hoa | Chỉ tên cột bảng, nhãn nhóm menu và tiêu đề nhóm nhỏ (DEC-027): `type/caption-caps` = caption, Inter 500, viết hoa, không giãn. Tiêu đề nhóm nhỏ dùng màu `color/text/tertiary` |

### 4.4 Khung cắt (DEC-322)

Chữ nằm trong khung cắt (`overflow: hidden`, ô một dòng) phải có dòng ≥ 1,25× cỡ để không mất dấu chồng tiếng Việt. Thang giữ số Untitled: `display-md` 36/44 (1,22×), `display-xl` 60/72 (1,20×) chỉ phải nới khi thật sự đặt trong khung cắt.

### 4.5 Chữ số (DEC-322)

Cột số trong bảng, tiền, giờ, đếm, KPI dùng số đều bề rộng. CSS: lớp `.num` (`font-variant-numeric: tabular-nums`). Figma: bật OpenType "Tabular figures" trên lớp chữ. Không tạo text style riêng cho số.

### 4.6 Nội dung dài (DEC-322)

Lớp `.prose` cho đoạn dài như Help sheet, ghi chú lệnh, lý do từ chối.

| Phần tử | Style | Màu |
|---|---|---|
| `h1` | `type/display` | `color/text/primary` |
| `h2` | `type/title-1` | `color/text/primary` |
| `h3` | `type/title-2` | `color/text/primary` |
| `h4` | `type/title-3` | `color/text/primary` |
| Đoạn | `type/body`, rộng tối đa 72ch, cách đoạn bằng cỡ chữ | `color/text/tertiary` |
| Trích dẫn | `type/prose-quote` | `color/text/primary` |
| Mã trong dòng | `type/prose-code`, nền `color/bg/secondary`, viền `color/border/secondary`, bo 6 | theo chữ |
| Đường kẻ | `color/border/secondary` | — |
