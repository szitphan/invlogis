---
type: brand-review
status: draft
updated: 2026-10-14
links:
  - design/brand/brand-brief.md
  - design/brand/_drafts/review/r2-identity-review.md
---

# R3 · Review độc lập Đợt 2 (logo, hệ thống, hình ảnh) — hướng A · Lụa

Người review: R3 (khác agent làm). Đã mở ảnh thật, đọc mã, chạy `render.py` cho brand-guideline.

## 1. Kết luận ngắn

- **Chọn chữ v: phương án 3** (Lexend nguyên bản, mọi chi tiết lụa dồn về chữ i). Logo tốt, đã sửa gần hết lỗi R2.
- **Chưa chuyển sang `design/brand/invlogis/` được**: `brand.yml` và `brand-guideline.html` trỏ tên file logo không tồn tại, nên trang quy chuẩn đang hiện bản nháp cũ (chữ v có gradient mà founder đã chê).
- Icon ứng dụng (Android tròn, iOS) có nguy cơ bị đọc thành biểu tượng "thông tin" ⓘ.

## 2. Điểm ba phương án chữ v (1–5)

| PA | Mô tả | Giữ nhịp với n, l | Đọc ở cỡ nhỏ | Đơn sắc | Rủi ro vấp mắt | Điểm |
|---|---|---|---|---|---|---|
| 1 Gradient nhẹ | v tô dải cobalt từ đầu cánh xuống đáy | Kém: v là vùng màu khác giữa các chữ mực, mắt dừng ở v | Đạt | Mất hết ý (tự thừa nhận) | Cao: đúng lỗi "chi tiết ở v" founder chê | **2** |
| 2 Nếp gấp | cắt chéo 14° ở đầu hai cánh | Khá ở cỡ lớn; ở 48px trở xuống thành mất nét, cạnh n và l thấy lệch | Vết cắt biến mất, thành v thường | Giữ | Trung: lệch nhẹ ở "nvl" | **3** |
| 3 Nguyên bản + dồn lụa về i | v Lexend gốc, cùng màu mực | Tốt: ba chữ n-v-l đều nét 87/1000 em, không vấp | Tốt (16px vẫn thấy "invlogis") | Giữ nguyên | Thấp | **4,5** |

**Chọn PA3.** Mất "chi tiết riêng ở chữ v" trong brief Mục 8-A, nhưng i lụa đã là chi tiết riêng; đúng ý founder chê chữ v.

## 3. Bảng kiểm theo mục

| Mục | Kết quả | Ghi chú |
|---|---|---|
| R2: ký hiệu "ii" | Đạt (có 1 chỗ lọt) | Ký hiệu chỉ một chữ i. Nhưng `logo-sheet.png` mục 02 đặt `symbol-mono` cạnh `symbol-reverse` thành hai i liền nhau, vi phạm Cấm số 5 của chính `logo-spec.md` |
| R2: favicon là khối vuông | Đạt | 16/32/48 là chữ i có chấm tách, thấy rõ ở kích thước thật; 16px đọc ra "i" (chấm 2 điểm ảnh) |
| R2: ký hiệu nặng hơn chữ | Đạt | Thân i rộng đúng nét chữ, cùng độ đậm |
| Chữ v không vấp mắt | Đạt | PA3 |
| SVG không thẻ `<text>` | Đạt | `grep -c "<text"` toàn `logo-final/*.svg` = 0 |
| Favicon.svg chế độ tối | Đạt | `prefers-color-scheme` đổi sang periwinkle; PNG ≥3:1 cả hai tab |
| Icon Android/iOS giống ⓘ | **Cần sửa** | Xem mục 5-Cao-1 |
| `logo-motion.html` | Đạt | Tổng ~1,9 giây (<2,5s), CSS thuần, có `prefers-reduced-motion` (mờ dần 200ms); dùng `forwards`/`both` nên khung cuối trùng logo tĩnh |
| `logo-spec.md` nội dung | Đạt, có mâu thuẫn với guideline | Xem mục 5-Cao-2, Trung-2 |
| `brand-tokens.css` ↔ `.json` | Đạt | Mọi giá trị màu, chữ, bo, khoảng cách khớp; json không có ~15 token dẫn xuất (focus-ring, vùng chữ, tag-*, line). Có bản tối cả hai (`data-theme` + `prefers-color-scheme`) |
| `brand.yml` định dạng | Đạt định dạng, **trượt đường dẫn** | Cùng khoá (`name/colors/logo/mark/fonts`) với `innvie/brand.yml`; đường dẫn logo sai |
| `brand-guideline.html` đủ mục | Đạt nội dung | 10 mục: giới thiệu, logo, màu, chữ, gradient, chi tiết, hình ảnh, giọng văn, kiến trúc, ứng dụng; tiếng Việt đủ dấu; khẩu hiệu DEC-072 đúng |
| Guideline dùng logo bản cuối | **Cần sửa** | Hiện bản tạm (xem Cao-2) |
| `contrast-report.md` | Đạt | Bảng đo đủ, cặp trượt ghi CẤM; vùng cấm chữ 56–70% hợp lý |
| Visuals: tránh điều cấm | Đạt | Không xe tải, container, địa cầu, mạch điện, robot, ảnh người |
| Visuals: vùng chữ đạt tương phản | Đạt | `_contrast.json` đo p99.5, README ghi min 5,5:1; nền sáng dùng chữ mực |
| Visuals: na ná ElevenLabs | Chấp nhận được | Gradient hạt + nhãn mono `[eDO]` gần gu ref, nhưng nền xanh chàm/cobalt, thẻ chứng từ Việt Nam và logo chữ i lụa tạo khác biệt; không có vệt san hô chéo như hướng C cũ |
| Visuals: tay nghề khung thiết bị | **Cần sửa** | Xem Trung-3 |
| Nhất quán chéo: màu | Đạt | Cobalt `#2F43DB`, chàm `#0E1442`/`#0B1033`, giấy `#FAF8F4` giống nhau ở logo-spec, tokens, yml, guideline, visuals |
| Nhất quán chéo: font | Đạt có lưu ý | Tokens/yml ghi Lexend 300; logo dựng ở 340 (có giải thích). Hợp lý, nhưng guideline mục Chữ nên nói rõ "logo 340, chữ trên tài liệu 300" |
| Nhất quán chéo: logo | **Cần sửa** | Guideline đang dùng bản khác với `logo-final` |

## 4. Phát hiện chi tiết

- **Guideline hiện bản logo cũ.** `brand-guideline.html` gọi `../logo-final/invlogis-logo.svg`, `-logo-reverse.svg`, `-logo-mono.svg`. Thư mục thật chỉ có `invlogis-primary.svg`, `-reverse.svg`, `-mono-black.svg`. Ảnh lỗi, trang rơi về `identity/a-lua/` (bản nháp có chữ v gradient) và hiện dải cảnh báo "Logo cuối đang hoàn thiện". Trong hero, logo đảo màu còn nằm trên một ô đen chữ nhật (lỗi nền của ảnh dự phòng).
- **`brand.yml` cùng lỗi tên file** (`logo.on-primary/on-light`, `mark.*`). `/deck` sẽ không tìm thấy logo.
- **Hai định nghĩa vùng an toàn và cỡ tối thiểu khác nhau.** Spec: x = chiều cao chữ x, chừa 1x bốn phía, màn hình cao ≥20px. Guideline: x = chiều cao chữ n (1/3 ký hiệu), logo đầy đủ ≥96px rộng, ký hiệu i ≥16px cao.
- **Icon tròn trắng trên xanh.** `android-foreground-432.png` (i trắng, mặt nạ tròn) và `app-icon-1024.png` (i trắng nền xanh vuông bo) rất giống biểu tượng "info". Cấm số 7 trong spec mô tả đúng rủi ro này nhưng icon app vẫn rơi vào.
- **Hai chữ i liền nhau trong sheet.** Mục 02 của `logo-sheet.png`.
- **Khung thiết bị.** Điện thoại che hơn nửa laptop, màn laptop cắt lệch phải; nhãn "KHE THAY ẢNH MÀN HÌNH" in trong ảnh xuất ra; nội dung UI quá nhỏ để đọc.
- **Nhãn trên thẻ chứng từ.** Chữ mono 10,5px màu `#7C84AC` trên trắng khoảng 3,7:1, dưới 4,5:1; chính contrast-report cấm `#8B93B8` làm chữ.
- **Chữ i đầu ở lockup `stacked`.** Ký hiệu lụa đứng trên chữ "invlogis" (i mực) tạo hai chữ i chồng, đọc là "i / invlogis".

## 5. Danh sách sửa

### Cao
1. **Icon ứng dụng giống ⓘ.** Sửa `logo-final/android-foreground-432.png`, `app-icon-1024.png`, `apple-touch-icon-180.png` (nguồn `_src/build.py`): dùng thân i gradient lụa (không trắng phẳng) trên nền gradient sáng/chàm, hoặc cắt chéo ký hiệu to hơn vùng an toàn; thử thu nhỏ 48px trên mặt nạ tròn.
2. **Guideline và yml trỏ tên file không tồn tại.** Sửa `system/brand-guideline.html` (mọi `src` logo, bỏ `onerror` fallback và dải cảnh báo) và `system/brand.yml` thành `invlogis-primary.svg`, `invlogis-reverse.svg`, `invlogis-symbol.svg`. Render lại và xác nhận chữ v mực, không gradient, hero không còn ô đen.
3. **Mâu thuẫn cỡ tối thiểu và định nghĩa x** giữa `logo-spec.md` và `brand-guideline.html` (mục Logo, bảng cỡ). Chọn theo spec (đo từ bản cuối) và sửa guideline.

### Trung
1. `logo-final/logo-sheet.png` (nguồn `_src/sheet.py`): tách `symbol-mono` và `symbol-reverse` khỏi nhau, tránh cảnh hai chữ i liền nhau.
2. `system/brand-guideline.html` mục Chữ: ghi "logo dựng Lexend 340, tài liệu dùng 300/400/600" để khớp `logo-spec.md`.
3. `visuals/device-frames.html` (+ `generate.py`): bỏ nhãn "khe thay ảnh" khỏi ảnh xuất; đặt điện thoại không che laptop; phóng to UI trong màn.
4. `visuals/doc-motifs.html`: nhãn nhỏ đổi `#7C84AC` → tối nhất `#5A6490` (≥4,5:1).
5. `logo-final/invlogis-stacked.svg`: thân i lụa trên cùng, hoặc i trong chữ giữ lụa và bỏ ký hiệu, để khỏi lặp.

### Thấp
1. `system/brand-tokens.json`: thêm các token dẫn xuất còn thiếu hoặc ghi chú "chỉ có ở CSS".
2. `logo-motion.md`: nêu rõ splash tối dùng `invlogis-reverse.svg` cần kiểm lại độ đậm chấm i khi gập.
3. `visuals/README.md`: bỏ mô tả "min 5,5:1" nếu có ảnh r3 đo thấp hơn; ghi theo từng nền.
4. Thử bản 16px trên viền tab tối thật trước khi chốt (`favicon-16.png` hiện đạt 3,31:1 trên `#202124`, sát ngưỡng).
