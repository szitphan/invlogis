---
type: design-component
status: draft
updated: 2026-10-26
links:
  - design/v2/architecture.md
  - design/v2/foundations.md
  - design/v2/tokens.json
  - design/v2/components/README.md
  - design/v2/components/l1/text-field.md
  - _workspace/decisions.md
---

# Base / OTP Field

> L1 · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma `Base / OTP Field` (6528:26324, đặt sẵn mode Platform =
> Mobile, trang DS · Components · L0–L3), L0 `.field / Code Cell` (6528:26230), `.field / Code Hint` (6528:26231), khung tài liệu
> `Tài liệu · OTP Field` (6529:26258, chỉ khối Mobile) · DEC-244 · cùng họ [Text Field](text-field.md) (`Base / Text Field / Mobile`)

Ô nhập mã xác thực 6 chữ số của app, mỗi ô một ký tự, không mang ngữ cảnh (không nói mã gì, gửi tới đâu, hết hạn sau bao
lâu). Chỉ có cấu tạo app: web đặt lại mật khẩu bằng link nên chưa dùng ô mã, khung tài liệu chỉ có khối Mobile. Nền, viền, chữ
lấy token `field/*` của ô nhập app nên đặt cạnh Base / Text Field / Mobile nhìn đồng bộ. Phần **Web** ngắn, phần **Mobile** tả
đầy đủ.

## Web

> Không có khối Web trên Figma: component chưa dựng cho web.

### Tổng quan

- **Chưa dùng trên web:** đặt lại mật khẩu bằng link, không nhập mã. Token `otp/cell-width` có giá trị Web 40 để dành, chưa
  có màn nào dùng và chưa dựng khối Web.

### Thuộc tính

Không đặt Base / OTP Field trên web. Thuộc tính của component: xem phần Mobile.

## Mobile

> Khối Mobile trên Figma đặt mode Platform = Mobile; mọi số dưới đây là giá trị mode Mobile.

### Tổng quan

- **6 ô cố định:** mỗi ô một chữ số (BR-account-access-009); nhập xong tự nhảy sang ô kế, xoá thì lùi về ô trước.
- **Dán mã:** dán cả mã vào ô đầu thì rải đủ 6 ô; bàn phím số; bật gợi ý tự điền mã một lần của hệ điều hành.
- **Tự kiểm:** đủ 6 số thì cha tự kiểm tra, không có nút Xác nhận trong component.
- **State:** Default · Focus · Error · Disabled; mỗi State đặt sẵn nội dung đại diện, chỉnh từng ô qua panel (State, Content,
  Digit).
- **Cỡ app:** ô 48 × 52, bo 12 (DEC-259), khoảng giữa ô 8; hàng ô rộng 328 canh giữa khung rộng 361.
- **Chỉ có ở app:** web không dùng ô mã; app không có Hover.
- **Mã sai:** cha xoá hết ô (về Default · Empty), đưa focus về ô 1, hiện chữ lỗi ở dòng dưới (Has Hint, Type=Error).
- **Đang kiểm tra, hết hiệu lực:** dùng Disabled. Đang kiểm tra = ô tắt có số + chữ ở dòng dưới; hết hiệu lực = ô tắt trống +
  dòng lỗi. Không có vòng quay. Chữ số của ô tắt vẫn đậm (`field/fg/value`).
- **Gửi lại:** đếm ngược "Gửi lại sau n giây" và nút Gửi lại là Base / Button đặt NGOÀI component, do cha cập nhật chữ nút.

### Cấu tạo

Hình phóng 2× trên Figma: State=Focus (ô 1–3 đã có số, ô 4 có con trỏ, hai ô còn trống, dòng gợi ý). Nhãn đỏ: kích thước ·
tím: khoảng · xanh: nội dung (màu, chữ); số đọc từ biến theo mode Mobile.

| Phần | Token | Giá trị app |
|---|---|---|
| Hàng ô | khoảng giữa ô `space/gap-sm`; canh giữa trong `field/width-default` | 8 giữa ô; 6 × 48 + 5 × 8 = 328 trong khung 361 |
| Ô (L0 `.field / Code Cell`) | rộng `otp/cell-width`; cao `control/height/lg`; bo `radius/field`; nền `field/bg/app`; viền `field/border-width` + `field/border/default` | 48 × 52; bo 12; #F2F4F7; viền 1 #5F6B7A |
| Chữ số | thuộc tính Digit; `type/title-3` (Cal Sans); màu `field/fg/value`, cả khi Disabled | 17/22; #121826 |
| Con trỏ | thanh `field/border-width-active` × `type/title-3/line-height`; màu `field/border/active`; chỉ State Focus · Content Empty | 2 × 22; #262626 |
| Dòng dưới (L0 `.field / Code Hint`) | canh giữa, cách hàng ô `space/gap-xs`; `type/caption`; Helper `field/fg/helper`, Error `field/fg/error`; bật bằng Has Hint | 13/18; cách 4; #5F6B7A · #B42318 |
| Viền và nền theo State | Focus 2px `field/border/active` · Error 2px `field/border/error` · Disabled 1px `field/border/disabled`, nền `field/bg/disabled` | 2px #262626 · 2px #B42318 · 1px #E3E6EC, nền #F2F4F7 |

### Biến thể

Field: State × 4 = 4 biến thể. Ô (L0): State 4 × Content 2 = 8. Dòng dưới (L0): Type 2. Mỗi State đặt sẵn nội dung đại diện;
chỉnh từng ô qua panel (State, Content, Digit).

| Biến thể của Field | Nội dung đại diện |
|---|---|
| Default | 6 ô trống, dòng dưới (chữ gợi ý) |
| Focus | 3 số, con trỏ ô 4 |
| Error | viền đỏ 2px + chữ lỗi |
| Disabled | ô tắt, nền và viền nhạt |

Lưới trên Figma: Field × State · Ô (L0) State × Content (Focus · Empty có con trỏ) · Dòng dưới Type Helper, Error.

### Trạng thái

Bốn State của Field, mỗi State đặt sẵn nội dung đại diện. Đang kiểm tra và hết hiệu lực không có State riêng: dùng Disabled
và chỉnh ô, dòng dưới qua panel.

| Trường hợp | Trông thế nào |
|---|---|
| Default | 6 ô trống, dòng dưới |
| Focus | 3 số, con trỏ ô 4 (viền 2px than chì + con trỏ; khi có bàn phím ngoài hoặc công cụ trợ năng) |
| Error | viền đỏ 2px + chữ lỗi ở dòng dưới |
| Disabled | ô tắt, nền và viền nhạt |
| Đang kiểm tra | Disabled · Filled, số vẫn đậm |
| Hết hiệu lực | Disabled + dòng lỗi |

App không dùng Hover.

### Kích thước

Một cỡ. Ô cao 52 khớp Base / Text Field / Mobile và Base / Button LG (`control/height/lg`, DEC-173).

| Phần | Rộng | Cao | Bo | Ghi chú |
|---|---|---|---|---|
| Ô | 48 | 52 | 12 | `otp/cell-width` · `control/height/lg` · `radius/field` |
| Hàng ô | 328 | 52 | — | 6 ô, khoảng giữa `space/gap-sm` = 8 |
| Khung (Field) | 361 | 74 | — | có dòng dưới; `field/width-default` |
| Dòng dưới | 361 | 18 | — | `type/caption` 13/18, cách hàng ô 4 |

### Nên và không nên

1. **Nên:** cho dán cả mã và tự điền mã một lần; tự kiểm khi đủ 6 ô, không cần nút xác nhận. **Không nên:** bắt gõ từng ô
   rồi bấm thêm một nút xác nhận.
2. **Nên:** báo lỗi bằng chữ ở dòng dưới kèm viền đỏ; cha xoá mã sai và đưa focus về ô 1. **Không nên:** chỉ đổi màu viền,
   không có chữ báo lỗi hay cách sửa.

### Trợ năng — chấm theo WCAG 2.2

| Tiêu chí | KQ | Số đo, ghi chú |
|---|---|---|
| 1.4.3 Tương phản chữ (AA, ≥ 4,5) | ✓ | chữ số trên nền ô 16,09 · dòng gợi ý trên trắng 5,43 · chữ lỗi 6,57 |
| 1.4.3 — Disabled | ✓ | 16,09 trên nền ô tắt: đạt AA, không cần ngoại lệ |
| 1.4.11 Tương phản ngoài chữ (AA, ≥ 3) | ✓ | viền nghỉ 4,92 trên nền ô · viền focus 13,73 · viền lỗi 5,97 |
| 2.4.7 Focus thấy được · 2.4.13 | ✓ | viền 2px than chì + con trỏ; ghi "focus khi có bàn phím ngoài hoặc công cụ trợ năng" |
| 2.5.8 · 2.5.5 Kích thước đích | ✓ | ô 48 × 52 ≥ 44 |
| 4.1.2 Tên, vai trò | ✓ | nhóm có nhãn "Mã xác thực"; mỗi ô nhãn "Chữ số k trên 6"; ô lỗi đặt trạng thái không hợp lệ, dòng lỗi nối với ô bằng nhãn mô tả |
| 3.3.1 Nhận biết lỗi · 3.3.3 Gợi ý sửa | ✓ | lỗi có viền dày và chữ; chữ lỗi nói cách sửa (do L2 đặt) |
| 1.4.1 Không chỉ dùng màu | ✓ | lỗi có viền dày 2px và chữ, không chỉ đổi màu |
| 3.3.8 Xác thực dễ tiếp cận (AA) | ! | phải cho dán mã và bật tự điền mã một lần (code); nếu không, nhập mã là bài thử trí nhớ |
| 2.1.1 Bàn phím | ! | khi có bàn phím ngoài: số điền ô, Backspace lùi ô, thứ tự focus trái → phải (code) |
| 2.3.3 Chuyển động | ✓ | con trỏ nhấp nháy theo hệ điều hành |
| **Điểm app** | | **10/10 đạt** (2 !: 3.3.8, 2.1.1 cần code) |

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| State | Biến thể | Default | Default · Focus · Error · Disabled |
| Has Hint | Bật tắt | bật | tắt khi không cần chữ gợi ý hay lỗi |
| Ô 1 … Ô 6 | Instance lồng | Digit 4 · 8 · 2 · 9 · 1 · 5 | `.field / Code Cell`: State, Content, Digit (đưa ra panel) |
| Hint | Instance lồng | Type=Helper | `.field / Code Hint`: Type Helper · Error, Helper text, Error text (đưa ra panel) |

4 biến thể · trục State · 1 thuộc tính bật tắt · 7 instance lồng đưa ra panel (6 ô, dòng dưới). Chữ số là thuộc tính Digit của
từng ô.

### Thành phần lồng

Lồng bằng instance của L0 thuộc họ field; đưa ra panel để chỉnh từng ô và dòng dưới. Không lồng L1 khác.

| Phần | Component · tầng | Cấu hình được phép | Đưa ra panel |
|---|---|---|---|
| Ô nhập số | `.field / Code Cell` · L0 | State × Content, Digit; đúng 6 ô | 6 ô |
| Dòng gợi ý, lỗi | `.field / Code Hint` · L0 | Type Helper · Error; canh giữa | Hint + Has Hint |

`.field / Hint` (đã duyệt cho Text Field) không đổi: dòng dưới của OTP canh giữa nên có L0 riêng (DEC-244).

### Được dùng trong

Kiểm trên Figma 20/10, trang DS · Components · L0–L3 (không tính khung tài liệu): chưa có component cha dùng. Màn dùng dự kiến
(chưa vẽ lại trên DS v2): account-access 3.4 · mob · otp-entry (flow 3): Default → Focus; mã sai → Error; hết hiệu lực →
Disabled + dòng lỗi.

### Token

Số đo (collection Platform, mode Mobile):

| Phần | Token | Mobile |
|---|---|---|
| Ô · rộng | `otp/cell-width` | 48 |
| Ô · cao | `control/height/lg` | 52 |
| Ô · bo | `radius/field` → `radius/xl` | 12 |
| Khoảng giữa ô | `space/gap-sm` | 8 |
| Ô → dòng dưới | `space/gap-xs` | 4 |
| Rộng khung | `field/width-default` | 361 |
| Viền nghỉ | `field/border-width` | 1 |
| Viền focus, lỗi | `field/border-width-active` | 2 |
| Chữ số | `type/title-3` | 17/22 |
| Con trỏ | `field/border-width-active` × `type/title-3/line-height` | 2 × 22 |
| Chữ dòng dưới | `type/caption` | 13/18 |

Màu (collection Component, tiền tố `field/`, dùng chung với Base / Text Field / Mobile, không thêm token màu mới):

| Phần | Token | Trỏ tới · mã |
|---|---|---|
| Nền ô | `bg/app` | `color/bg/muted` → neutral/100 · #F2F4F7 |
| Nền ô tắt | `bg/disabled` | `button/bg/disabled` → `color/action/secondary` · #F2F4F7 |
| Viền nghỉ | `border/default` | `color/border/input` → neutral/500 · #5F6B7A |
| Viền focus | `border/active` | `color/border/focus` → charcoal/900 · #262626 |
| Viền lỗi | `border/error` | `color/border/danger` → red/700 · #B42318 |
| Viền tắt | `border/disabled` | `color/border/default` → neutral/200 · #E3E6EC |
| Chữ số (kể cả tắt) | `fg/value` | `color/text/primary` → neutral/900 · #121826 |
| Gợi ý | `fg/helper` | `color/text/secondary` → neutral/500 · #5F6B7A |
| Chữ lỗi | `fg/error` | `color/status/danger-text` → red/700 · #B42318 |

Code: biến CSS `--otp-cell-width`, `--field-*`, `--control-height-lg`.

### Kiểm máy

Chạy `check-mat-hinh.js` trên khung 6529:26258 ngày 20/10 (ngưỡng 1,1:1, tương phản WCAG; mỗi ô mẫu đặt trên nền thật).

| Mức | Ô mẫu | Kết quả |
|---|---|---|
| Khung | 25 ô, 26 mẫu (khối Mobile) | luật A: 0 lỗi, ô nào cũng có nền trắng `color/bg/surface` và viền mảnh |
| ✕ Mất hình · Khe lộ · Giống Default | — | không có, 0 cờ |
| Sát ngưỡng | `.field / Code Cell` (8 mẫu), lớp "Ô 1" của Base / OTP Field (15 mẫu) | nền ô #F2F4F7 trên ô trắng = 1,10 (chính xác 1,0998); hình giữ nhờ viền 4,92 · 13,73 · 5,97 · 1,25 |

## Nguồn cấu tạo

Nền, viền, chữ và bo của ô lấy từ ô nhập app của DS v2 (`Base / Text Field / Mobile`, DEC-184): ô 48 × 52 viền 1px, focus 2px.

## Phần máy (chung Web và Mobile)

Tên token giống nhau ở hai nền tảng; số theo mode xem bảng Token của phần Mobile (component chỉ đặt sẵn mode Mobile). Chữ số và
dòng dưới nằm ở instance L0 lồng nên bộ xuất không đọc được màu của ô; màu xem bảng Token.

<!-- auto:begin -->
<!-- Máy sinh từ Figma `Base / OTP Field` (6528:26324) ngày 2026-10-20 bằng _scripts/ds-v2-component-doc.py. Không sửa tay: sửa trên Figma rồi xuất lại. -->

### Thuộc tính

| Thuộc tính | Loại | Mặc định | Giá trị |
|---|---|---|---|
| Has Hint | Bật tắt | bật | — |
| State | Biến thể | Default | Default · Focus · Error · Disabled |

4 biến thể · trục State.

### Màu theo phần (token)

| State | Chữ |
|---|---|
| Default | `field/fg/helper` |
| Focus | `field/fg/helper` |
| Error | `field/fg/error` |
| Disabled | `field/fg/helper` |

### Số đo theo phần (token)

| Cao | Rộng | Khoảng giữa |
|---|---|---|
| 74 | `field/width-default` | `space/gap-xs` |

### Kiểu chữ

| Lớp chữ | Text style |
|---|---|
| Helper | `type/caption` |
| Digit | `type/title-3` |
| Error text | `type/caption` |

<!-- auto:end -->
