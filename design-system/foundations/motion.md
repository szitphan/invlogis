---
type: design-foundations
status: approved
updated: 2026-11-03
links:
  - design-system/foundations/README.md
  - design-system/tokens.json

---

# Foundations · Chuyển động

> Một phần của [[design-system/foundations/README.md|Foundations]]. Giữ số mục cũ (10.x) để các DEC và spec trích "foundations mục 10…" vẫn tra được. Giá trị máy đọc: `design-system/tokens.json` (json thắng).

## 10. Chuyển động (DEC-139, DEC-333, DEC-336)

DEC-333 thay hai phần của DEC-139: số 700 và luật một đường cong. Mã `mt…` là mục trên trang review Chuyển động.

### 10.1 Token

| Token | Giá trị | Dùng cho |
|---|---|---|
| `duration/fast` | 125ms | Hover, nhấn, đổi màu, Switch, chevron; menu, chọn, popover, tooltip; toast lúc ra |
| `duration/medium` | 300ms | Dialog, sheet, ngăn kéo, toast lúc vào; gạch chân tab; bề rộng menu thu gọn; thời gian chờ spinner |
| `duration/slow` | 500ms | Một chiều của vòng lặp: skeleton (cả vòng 1000) |
| `duration/exit` | 200ms | Dialog, sheet, ngăn kéo lúc ra |
| `easing/standard` | cubic-bezier(0.24, 1, 0.4, 1) | Vào, đổi trạng thái. Không bounce, không spring |
| `easing/exit` | cubic-bezier(0.4, 0, 1, 1) | Ra (ease-in của Tailwind) |

Vòng lặp và thanh giờ dùng `linear`, không qua token đường cong. Ngoại lệ duy nhất: con trỏ nhập giả trong preview dùng `steps(1)` vì nó phải bật tắt, không mờ dần.

Token Component: `spinner/period` 1000, nằm trong sổ `components/_token-ledger.json` chờ đợt 2, không phải bậc Foundation. Trong lúc chờ, CSS ghi `calc(var(--duration-slow) * 2)`.

### 10.2 Luật ghi code

- **Không số trần (mt03).** `transition`, `animation` luôn đi qua `var(--duration-*)`; số trần sẽ vẫn chạy khi người dùng bật giảm chuyển động. Máy dò: `python3 _scripts/ds-token-usage.py --check`, dòng WARN "chuyển động số trần".
- Transition theo từng thuộc tính (background, color, opacity, transform, box-shadow), không dùng `all`.
- **Không khoá thao tác (mt17).** Không chuyển động nào chặn bấm; bấm tiếp trong lúc chạy thì chạy lệnh mới ngay.

### 10.3 Theo loại phần tử

| Phần tử | Vào | Ra | Hình | Mã |
|---|---|---|---|---|
| Hover, nhấn | `duration/fast` + `easing/standard` | như vào | Đổi màu | mt04 |
| Vòng focus | Hiện ngay | Mất ngay | Không transition cho `outline` | mt04 |
| Menu, chọn, popover, tooltip | `duration/fast` + `easing/standard` | `duration/fast` + `easing/exit` | Trượt 4. Tooltip chờ 300 mới hiện | mt05 |
| Dialog | `duration/medium` + `easing/standard` | `duration/exit` + `easing/exit` | Phóng 95 | mt06 |
| Sheet, ngăn kéo | `duration/medium` + `easing/standard` | `duration/exit` + `easing/exit` | Trượt. Sheet kéo được thì đi theo ngón tay | mt06, mt14 |
| Lớp phủ | Theo khối nó đỡ | Theo khối nó đỡ | Chỉ mờ dần, bán kính blur giữ nguyên | mt18 |
| Toast | `duration/medium` + `easing/standard` | `duration/fast` + `easing/exit` | Vào trượt 8 + mờ dần; ra chỉ mờ. Thanh giờ `linear` | mt07 |
| Tab | `duration/medium` + `easing/standard` | | Gạch chân trượt, nội dung mờ dần | mt11 |
| Menu thu gọn 240 ↔ 64 | `duration/medium` + `easing/standard` | như vào | Chạy bề rộng, không lò xo (DEC-139 cấm) | mt12 |
| Chevron nhóm menu | `duration/fast` + `easing/standard` | như vào | Xoay | mt12 |

Dialog, sheet, ngăn kéo: **thôi chặn bấm ngay khi bắt đầu đóng**, lớp phủ còn đang mờ cũng không chặn (mt06).

### 10.4 Vòng lặp

| Thứ | Chu kỳ | Đường cong | Luật | Mã |
|---|---|---|---|---|
| Skeleton | `duration/slow` một chiều, cả vòng 1000 | `linear` | Nhấp nháy opacity 100 ↔ 45, không vệt sáng. Dừng sau 5 giây (10 lượt một chiều); tải lâu hơn thì thêm chữ | mt08 |
| Spinner | `spinner/period` 1000 | `linear` | Chờ `duration/medium` mới hiện để thao tác xong nhanh không bị nháy. Chạy quá 5 giây song song nội dung khác (WCAG 2.2.2) thì chuyển sang thanh tiến độ hoặc chữ | mt09 |

**Không chấm nhấp nháy (mt16).** Danh sách, bảng, bản đồ: chấm trạng thái đứng yên + nhãn.

### 10.5 Đổi dữ liệu trong bảng, danh sách (mt17)

Dòng hiện lần lượt, **chặn tổng 300** (`duration/medium`) tính từ dòng đầu bắt đầu đến dòng cuối xong, dù bảng bao nhiêu dòng. Đề xuất cách chia: mỗi dòng mờ dần `duration/fast`, các dòng lệch nhau (300 − 125) ÷ (số dòng − 1); dòng ngoài khung nhìn hiện ngay. Bật giảm chuyển động thì hiện ngay.

### 10.6 Splash (mt10)

Kịch bản 4 nhịp giữ theo `design/design.md` (DEC-037); bốn số của nó là số riêng, không qua token. Nhịp phóng bị chặn theo màn: **min(115%, rộng màn ÷ rộng logo)**.

| Nơi | Rộng màn | Rộng logo Delta | Phóng |
|---|---|---|---|
| App | 393 | 361 | 108,9% |
| App | 320 | 288 | 111,1% |
| Web | | | 115% |

Logo app đổi cỡ (`foundations/logo.md`, DEC-326) thì mức chặn đổi theo công thức.

### 10.7 Giảm chuyển động (mt13)

Người dùng bật `prefers-reduced-motion` thì mọi `duration/*` về 0, kể cả token mới: `tokens.css` sinh lớp này từ `tokens.json`; preview `.pv` mang lớp riêng vì `.pv` ghi đè `:root`.

- Spinner dừng + chữ "Đang tải…".
- Skeleton đứng yên.
- Code không chờ `transitionend`: thời gian 0 không phát sự kiện, chờ sẽ treo.

### 10.8 Trợ năng (mt15)

| WCAG | Mức | Cam kết |
|---|---|---|
| 2.2.2 Tạm dừng, dừng, ẩn | A, bắt buộc | Thứ tự động chạy quá 5 giây song song nội dung khác phải dừng được, trừ pha tải không thao tác được |
| 2.3.1 Ba lần chớp | A, bắt buộc | Không gì chớp quá 3 lần mỗi giây. Nhanh nhất trong bộ này: 1 lần mỗi giây |
| 2.3.3 Chuyển động khi tương tác | AAA, làm luôn | Qua luật giảm chuyển động ở 10.7 |

### 10.9 App Flutter (mt14)

- Một bộ số với web, sinh ra `InvMotion` trong `design-system/handoff/flutter/`.
- Chuyển màn giữ mặc định của nền tảng.
- Giảm chuyển động: đọc cả `MediaQueryData.disableAnimations` và `AccessibilityFeatures.reduceMotion`; một cờ không đủ cho cả hai hệ điều hành.

### 10.10 Lớp phủ làm mờ trên app (mt18)

Đo trên Android cấu hình trung bình trước khi vào app. Dưới 50 khung mỗi giây thì lùi `color/bg/overlay_solid`. **Ngưỡng 50 là đề xuất, chưa có số đo**. 35% + `backdrop-blur/lg` ở DEC-327 giữ nguyên cho web và máy đủ khoẻ.

### 10.11 Animation bổ sung (DEC-336)

Mã `an…` là mục trên trang review Animation bổ sung. Không thêm bậc thời gian: mốc giữ 1000 và 1500 ghi bằng bội của `duration/slow`.

**Preset.** Nguồn: `motionPresets` trong `design-system/tokens.json`. Web dùng lớp `.anim-{tên}` trong `tokens.css`; app dùng `InvMotionPreset.{tên}` trong `design-system/handoff/flutter/`, chỉ gồm thời gian và đường cong, hình chạy dựng bằng widget. Không tự viết `@keyframes` cho những việc preset đã có.

| Preset | Hình | Thời gian | Đường cong | Mã |
|---|---|---|---|---|
| `fade-in` | Mờ dần | `duration/fast` | `easing/standard` | an07, an11 |
| `pop` | Phóng 0 → 100 | `duration/medium` | `easing/standard` | an02 |
| `draw` | Vẽ nét | `duration/medium` | `easing/standard` | an02 |
| `swap` | Mờ dần + phóng 95 → 100 | `duration/fast` | `easing/standard` | an05 |
| `flash` | Tô `color/utility/blue/50` giữ 1000, phai 500 | `duration/slow` × 3 | `linear` | an06, an08 |
| `expand` | Chiều cao, bật bằng `data-open="true"` | Mở `duration/medium`, đóng `duration/exit` | `easing/standard`, `easing/exit` | an08, an10, an16 |
| `glide` | Vị trí | `duration/medium` | `easing/standard` | an12 |
| `grow` | Cột mọc từ đáy | `duration/medium` | `easing/standard` | an17 |

**Theo việc.** Luật dưới đây chỉ gồm thứ preset không tự nói được.

| Việc | Luật | Giảm chuyển động | Mã |
|---|---|---|---|
| Dấu kết quả (thành công, thất bại) | Ba nhịp, tổng 600, chạy một lần, không nảy. Đĩa ngoài `pop`; đĩa trong `pop` trễ `duration/fast`; dấu `draw` trễ `duration/medium`. Dấu X hai nét, mỗi nét `duration/fast`, nối tiếp. Chỉ dùng cho kết quả quan trọng | Hiện ngay | an02 |
| Lỗi biểu mẫu | Đổi ngay, không chạy, không rung | Như thường | an03 |
| Nút xử lý xong | Spinner theo 10.4, xong về nhãn ngay; kết quả báo bằng toast. Nút giữ nguyên bề rộng | Spinner theo 10.7 | an04 |
| Đổi icon tại chỗ | `swap`, giữ 1000 rồi về icon gốc | Đổi ngay, vẫn giữ 1000 | an05 |
| Dòng vừa đổi | `flash`, chạy một lần. Quá 5 dòng đổi cùng lúc thì không tô, chỉ đổi chip (**số 5 là đề xuất, chưa đo**) | Giữ nền 1500 bằng bộ đếm giờ rồi tắt ngay | an06 |
| Số đổi | `fade-in`, không đếm chạy, chữ số `tabular-nums`. Số trên huy hiệu cùng luật, chuông không lắc | Đổi ngay | an07 |
| Lệnh mới từ máy chủ | Luôn báo "Có n lệnh mới", bảng không tự nhảy. Bấm thì dòng mới `expand` + `flash` | Chèn ngay, nền như dòng vừa đổi | an08 |
| Thanh tiến độ | Chạy `transform`, `duration/fast`, `linear`. Chưa biết phần trăm thì spinner | Nhảy theo mốc | an09 |
| Mở, đóng khối, xoá dòng | `expand`; chevron `duration/fast` | Đổi ngay | an10 |
| Skeleton sang nội dung, đổi trang web | `fade-in` cho vùng nội dung, menu đứng yên | Đổi ngay | an11 |
| Xe trên bản đồ | `glide` khi có điểm mới, giữa hai điểm xe đứng yên. Điểm ngoài khung nhìn hoặc xa quá thì đặt ngay | Nhảy tới điểm mới | an12 |
| Bước tiến độ lệnh | Vạch chạy `duration/medium`, chấm đổi `duration/fast` nối tiếp, tổng 425. Mở màn lần đầu thì hiện ngay | Đổi ngay | an13 |
| Quét mã | Vạch quét lặp `linear`, một lượt `duration/slow` × 2. Sau 5 giây vạch dừng, khung đứng yên, hiện gợi ý nhập tay, camera vẫn nhận mã. Nhận được mã thì sang màn sau ngay | Không có vạch, hiện gợi ý ngay | an14 |
| Kéo làm mới | Mặc định của nền tảng, không tự vẽ | Theo nền tảng | an15 |
| Dải mất mạng | `expand` đẩy nội dung, không che nút. Có mạng lại thì xanh, giữ 1000 rồi đóng. Mất mạng dưới 2 giây không báo (**số 2 giây là đề xuất**). Chữ luôn kèm icon | Đổi ngay, vẫn giữ 1000 | an16 |
| Biểu đồ | `grow` khi tải, đổi bộ lọc thì đổi ngay | Hiện ngay | an17 |

**Hướng vẽ nét theo tay viết.** Path của Lucide đi ngược chiều, nên `draw` dùng path riêng; hình tĩnh không đổi.

| Dấu | Thứ tự | Path |
|---|---|---|
| Tích | Từ nét ngắn, qua góc, sang nét dài | `M4 12l5 5L20 6` |
| X | Nét 1 từ trên trái xuống dưới phải; nét 2 từ trên phải xuống dưới trái | `M6 6l12 12`, `M18 6 6 18` |

**Giữ bằng bộ đếm giờ.** Các mốc giữ 1000, 1500 là thời gian trạng thái, phải còn khi giảm chuyển động đưa `duration/*` về 0: code đếm bằng bộ đếm giờ, không dựa vào `animationend`.

**Khác mẫu tham khảo.** an02 lấy từ mẫu [Finance Success & Failure Lottie Animation](https://dribbble.com/shots/27204078-Finance-Success-Failure-Lottie-Animation). Giữ ba nhịp; bỏ độ nảy (DEC-139), cung chạy quanh viền và phần lặp; không dùng file Lottie.

**Trên Figma.** Trang `DS · Foundations`, nhóm Chuyển động: khối `Preset animation` (`7152:217019`) chạy bằng keyframe, xem bằng Present hoặc Play trên timeline; bảng `Animation theo việc` (`7152:216729`). Keyframe chạy khi khung hiện ra và lặp lại trong Present, không chạy theo cú bấm; số ghi bằng chữ vì Figma không có biến thời gian. Mẫu `flash` tô bằng mã màu vì keyframe không nhận biến.

**Còn mở.** Chu kỳ GPS thật của EUP chưa có số; bản xem thử giả định 2 giây. Nếu trên 30 giây thì xem lại an12.

### 10.12 Chuyển động theo component

Chuyển động là một phần của component: **component mới vẽ cùng chuyển động của nó**, không làm riêng sau đó. `/figma-component` đọc bảng này ở Bước 1, gắn ở Bước 6, kiểm ở Bước 7, đổi trạng thái dòng ở Bước 9.

Trên Figma, đổi trạng thái dùng Smart Animate với thời gian và đường cong của token. Thứ Figma không chạy được (dòng hiện lần lượt, đếm giờ theo dữ liệu thật) thì ghi chú trong spec cho dev, không vẽ giả.

**Chưa có component: định nghĩa và vẽ cùng khi dựng**

| Component | Chuyển động phải có | Theo | Trạng thái |
|---|---|---|---|
| Dialog dùng chung | Vào 300 phóng 95, ra 200; lớp phủ chỉ mờ dần | 10.3 | ⬜ chưa có |
| Sheet, ngăn kéo dùng chung | Vào 300, ra 200, trượt; sheet kéo được đi theo ngón tay | 10.3 | ⬜ chưa có |
| Tab | Gạch chân trượt 300, nội dung mờ dần | 10.3 | ⬜ chưa có |
| Skeleton | Nhấp nháy 100 ↔ 45, một chiều 500, dừng sau 5 giây; sang nội dung `fade-in` | 10.4, an11 | ⬜ chưa có |
| Spinner độc lập | Chu kỳ 1000, chờ 300 mới hiện | 10.4 | ⬜ chưa có |
| Thanh tiến độ độc lập | Trượt 125 linear theo mốc | an09 | ⬜ chưa có |
| Khối mở rộng | `expand`, chevron 125 | an10 | ⬜ chưa có |
| Bảng, dòng bảng | Dòng hiện lần lượt chặn 300; `flash`; báo "Có n lệnh mới"; xoá dòng co lại | 10.5, an06, an08, an10 | ⬜ chưa có |
| Bước tiến độ lệnh | Vạch 300, chấm 125 nối tiếp | an13 | ⬜ chưa có |
| Dấu kết quả | Ba nhịp `pop`, `pop`, `draw`, tổng 600 | an02 | ⬜ chưa có |
| Thẻ KPI, số | `fade-in`, không đếm chạy | an07 | ⬜ chưa có |
| Biểu đồ | `grow` khi tải, đổi lọc thì đổi ngay | an17 | ⬜ chưa có |
| Màn quét mã | Vạch lặp, sau 5 giây dừng + gợi ý nhập tay | an14 | ⬜ chưa có |
| Dải mất mạng | `expand`, xanh giữ 1000 rồi đóng | an16 | ⬜ chưa có |

Stepper, SegmentedControl, Timer trên trang `DS · Base components` là bản cũ chưa dựng lại theo DS v2 nên tính là chưa có.

**Đã có component**

| Component | Chuyển động | Theo | Trạng thái |
|---|---|---|---|
| Button, Close button, Utility button, Help icon, Dropdown trigger, Select item, Dropdown item, Input | Hover, nhấn 125 | 10.3 | ✅ đã gắn |
| Toggle, Checkbox, Radio | Hover 125, bấm đổi trạng thái 125 | 10.3 | ✅ đã gắn |
| Tooltip | 125 trượt 4, chờ 300 mới hiện | 10.3 | 🟡 chưa gắn |
| Dropdown menu, Select menu, `_Select sheet`, `_Multi-select sheet` | Menu 125 trượt 4; sheet vào 300, ra 200 | 10.3 | 🟡 chưa gắn |
| Notification, Alert | Vào 300 trượt 8, ra 125 | 10.3 | 🟡 chưa gắn |
| Scope dialog | Vào 300 phóng 95, ra 200 | 10.3 | 🟡 chưa gắn |
| Sidebar navigation | 240 ↔ 64 trong 300, chevron 125 | 10.3 | 🟡 chưa gắn |
| `_Header tab` | Gạch chân trượt 300 | 10.3 | 🟡 chưa gắn |
| `_Section toggle`, Section header | `expand`, chevron 125 | an10 | 🟡 chưa gắn |
| Field Upload | Dải tiến độ trượt 125, spinner | an09 | 🟡 chưa gắn |
| Map Marker | `glide` | an12 | 🟡 chưa gắn |
