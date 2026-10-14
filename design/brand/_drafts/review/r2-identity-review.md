---
type: brand-review
reviewer: R2 (độc lập)
status: draft
updated: 2026-10-14
---

# R2 · Chấm 3 hướng nhận diện Invlogis

Đã xem: brief Mục 2, 6–9; competitor-audit A–C, F; ảnh gu ElevenLabs; board, favicon 16/32, deck, social, splash, palette, type của A, B, C. Đo thêm bằng `contrast.py` (chữ trắng trên vùng sáng gradient) và render ký hiệu 24px (ảnh trong `/tmp/r2`).

## 1. Bảng điểm (1–5)

| # | Tiêu chí | A Lụa | B Chứng từ | C Hội tụ |
|---|---|---|---|---|
| 1 | Khớp brief (tính cách, gu mảnh/lụa/UI tinh tế) | 4 | 4 | 3 |
| 2 | Nhận ra + nhớ | 2 | 3 | 4 |
| 3 | Rõ ở 16px | 2 | 2 | 5 |
| 4 | Đơn sắc | 3 | 4 | 4 |
| 5 | Khác đối thủ / không na ná ElevenLabs | 3 | 3 | 3 |
| 6 | Tránh điều cấm | 3 | 2 | 3 |
| 7 | Tay nghề | 3 | 3 | 4 |
| 8 | Hệ innvie đi kèm | 4 | 2 | 5 |
| 9 | Tương phản + dấu tiếng Việt | 4 | 4 | 3 |
| | **Tổng /45** | **28** | **27** | **34** |

Lý do ngắn:
1. A đúng gu chữ mảnh, giấy ấm, lụa nhưng "mềm"; B đúng chất kỹ sư, thiếu độ bay bổng ở logo; C táo bạo nhưng chữ đậm 600, lệch gu "chữ mảnh" và kém "điềm tĩnh".
2. Chỉ C có hình nhớ được sau một lần nhìn; A nhìn là chữ thường, B nhìn là icon giấy.
3. C đọc rõ ở 16/24px; A đổi sang hình khác hẳn ở favicon; B thành icon "sửa tài liệu" nhoè.
4. A mất hẳn nếp lụa khi đơn sắc, còn lại chữ "i" mảnh; B, C giữ nguyên hình.
5. A gần ElevenLabs nhất về cơ chế chữ + gradient; C dùng vệt san hô/cam chéo trên nền xanh rực rất gần ảnh ref; B khác nhất ElevenLabs nhưng hình giấy-gạch-chéo là ngôn ngữ phổ thông, trừ CargoWise chưa va (không thấy vạch ngang xếp lệch).
6. Xem từng hướng bên dưới.
7. C cân nhất; A chi tiết "v" gần như không thấy; B có lỗi I/l và chữ bị cắt trong mẫu.
8. C: chữ "v" lặp lại thành họ ký hiệu rất rõ. A: tốt (cùng nét). B: logo innvie chỉ là một biểu tượng tờ giấy trống, đúng là icon tài liệu phổ thông.
9. C: chữ trắng nhỏ trên san hô trượt (xem Mục 2).

## 2. Đo bổ sung: chữ trắng trên vùng sáng nhất của gradient chiến dịch

| Màu (hướng) | Trắng trên màu | Kết luận |
|---|---|---|
| `#97A6FF` periwinkle (A) | 2.28:1 | trượt |
| `#C4CDFF` (A) | 1.55:1 | trượt |
| `#FF7A59` san hô (A, C) | 2.57:1 | trượt |
| `#FFB547` hổ phách (A) | 1.76:1 | trượt |
| `#E24C9A` hồng (A) | 3.66:1 | chỉ chữ lớn |
| `#7B55FF` tím (A) | 4.58:1 | đạt |
| `#F062B4` hồng (B) | 2.95:1 | trượt |
| `#FF8F63` cam (B) | 2.24:1 | trượt |
| `#FFC774` vàng (B) | 1.54:1 | trượt |
| `#7AA7FF` cuối vệt (B) | 2.39:1 | trượt |
| `#ff6b5e` / `#ffa24d` (C) | 2.79 / 1.99:1 | trượt |

Hệ quả thấy trên mẫu: C, thẻ "[ ĐÃ ĐỌC · 5/5 ]" và chip mono 11–13px đặt thẳng trên san hô (khoảng 2.6:1). A, tiêu đề trắng đè mảng lam-xám nhạt giữa trang, phụ đề 30px chạm vùng periwinkle (ước 2.3–3:1). B an toàn nhất vì chữ nằm trên nền giấy hoặc thẻ trắng; chỉ nhãn chip trên vệt cam là rủi ro. Các palette đều tự ghi "chưa đo", nay đã đo: trượt.

## 3. Hướng A · Lụa (28/45)

Điểm mạnh
- Gu gần brief nhất: chữ Lexend Light thoáng, giấy ấm `#FAF8F4`, chip viền mảnh, thẻ eDO kính mờ; bài social đẹp, cao cấp.
- Màu cobalt ngả tím (hue ~233) né vùng azure đông đối thủ; hệ innvie cùng nét, nhất quán.
- Kỹ thuật sạch: logo vector, đủ dấu tiếng Việt, tương phản chữ thân đạt.

Sửa
- **Cao** Favicon 16/32 là khối vuông bo trắng-xanh giống ký hiệu pixel cũ mà brief bắt bỏ, không liên quan chữ "i" lụa; làm lại một ký hiệu duy nhất dùng được mọi cỡ.
- **Cao** Ký hiệu hai chữ "i" cạnh nhau (màu + đơn sắc trên board) đọc thành "ii", chính là "hai vạch dọc" brief cấm; chỉ ký hiệu một "i" và rời hai biến thể.
- **Cao** Chữ trắng trên periwinkle/san hô/hồng chưa xử lý: dùng chip kính hoặc đẩy tông gradient tối hơn ở vùng có chữ (đo ≥4.5 cho chữ nhỏ).
- Trung Nếp gập "i" mảnh 14px không nhìn ra là lụa; tăng bề dày thân hoặc lộ hẳn một nếp gấp.
- Trung Chi tiết riêng ở chữ "v" (cánh vắt) mất ở cỡ <96px; hoặc bỏ, hoặc đẩy lớn hơn.
- Thấp Chấm "i" hình bình hành nghiêng lệch nhịp so với ba chữ cái còn lại; cân lại khoảng cách i–n.

Rủi ro: na ná ElevenLabs (chữ mảnh + gradient hạt); thiếu cảm giác "đáng tin cậy, chắc"; không có hình đủ riêng để giữ khi cắt ra khỏi bối cảnh.

## 4. Hướng B · Chứng từ (27/45)

Điểm mạnh
- Thông điệp mạnh nhất trong ba: "Bớt nhập lại. Đúng mốc. Minh bạch." và bộ thẻ chứng từ nghiêng + vệt quét sáng thể hiện đúng câu chuyện "AI đọc chứng từ".
- Palette navy + cobalt có lý do rõ (né azure), nền trắng nhiều, chữ Manrope + JetBrains Mono tinh tế; đơn sắc đẹp.
- Hợp gu "chi tiết UI tinh tế": chip mono, viền mảnh, thẻ kính.

Sửa
- **Cao** Ký hiệu rơi đúng điều cấm "icon tài liệu phổ thông"; nét gạch chéo còn đọc như biểu tượng "bút sửa" hoặc "cấm/vô hiệu". Đổi hình khác (đừng giữ khung tờ giấy làm ký hiệu), hoặc dùng thẻ giấy làm minh hoạ chứ không làm logo.
- **Cao** Logo innvie là một tờ giấy trống: không phải logo, không cùng họ với chữ; vẽ lại innvie bằng chữ + chi tiết riêng.
- **Cao** Chữ "Invlogis" viết hoa chữ đầu: "I" và "l" trong Manrope gần như giống hệt ("Invlogis" đọc thành "lnvlogis"). Đổi dáng "I" (có chân/vạch) hoặc dùng chữ thường.
- Trung Ở 16–24px ký hiệu thành mảng xanh nhoè; cần bản rút gọn thực sự (một tờ + vệt dày), hiện bản 32px vẫn còn viền kép.
- Trung Nét ký hiệu đậm 5–6px nặng hơn Manrope 500; hạ độ dày hoặc tăng độ đậm chữ để đồng nhịp.
- Trung Mẫu social/deck: thẻ chứng từ bị cắt chữ ("TCLU 482…", chip "[EI"), thẻ giấy giống ảnh stock minh hoạ dạng sticker; sửa tràn chữ.
- Thấp Chip nhãn trên vệt cam: dùng nền kính đậm để vượt 4.5.

Rủi ro: một ký hiệu "tờ giấy" dễ lẫn mọi phần mềm văn phòng/ký số; khó nhớ; ít "ấn tượng + hào hứng" cho logo (hào hứng nằm ở bài quảng bá, không nằm ở nhận diện).

## 5. Hướng C · Hội tụ (34/45)

Điểm mạnh
- Ký hiệu "V + chấm" nhớ ngay, đúng 16px, đơn sắc giữ nguyên hình, đảo màu nền tối tốt; chữ "v" trong tên lặp lại thành một hệ ký hiệu rõ.
- Ý tưởng hội tụ bám thẳng sản phẩm (nhiều chứng từ về một hồ sơ); sơ đồ năm nhãn mono nối vào một chấm là ứng dụng dễ hiểu nhất.
- Hệ innvie tốt nhất: cùng chữ "v" lặp, cùng họ chữ.

Sửa
- **Cao** Chữ trắng nhỏ (nhãn mono 11–13px, thẻ "[ ĐÃ ĐỌC ]") trên vệt san hô/hổ phách: trượt (2–2.8:1). Dựng thẻ nền tối kính đậm hoặc giảm san hô dưới khối chữ.
- **Cao** Vệt san hô-cam trên xanh rực rất gần ảnh ElevenLabs (ảnh ref, ô "Introducing Eleven V4"). Đổi cơ chế: hồng/tím mảnh hơn, bớt cam đặc, thêm hạt/hướng riêng; nếu giữ thì thu hẹp tỷ lệ cam.
- **Cao** Ký hiệu có thể đọc thành ngón tay/chân đĩa hoặc chấm dọc kiểu "địa điểm" (tự ghi trên board). Thử chấm nhỏ hơn hoặc tách khỏi đáy nét; kiểm cảm nhận với vài người ngoài.
- Trung Wordmark Lexend 600 nặng, lệch gu "chữ mảnh"; thử 400–500 và giữ "v" làm điểm nhấn.
- Trung Cobalt `#1a23d1` rất bão hoà, gần chàm điện `#371ee1` của CargoWise (hue ~236 vs ~249); đẩy sang cobalt ít chói hơn hoặc ngả tím rõ hơn.
- Thấp Chữ "v" thu nhỏ trong wordmark có màu gradient mờ ở cỡ nhỏ; ở 12–14px chuyển sang một màu.

Rủi ro: giống logo ngân hàng/viễn thông (chữ đậm, ký hiệu V); mất "điềm tĩnh"; lệch gu chữ mảnh.

## 6. Khuyến nghị

**Chọn C làm nền, ghép thêm A và B.**
- **Ký hiệu và hệ innvie: từ C** (V + chấm, thêm "v" lặp trong chữ), vì là hướng duy nhất dùng được ở 16px và nhớ được.
- **Chữ: lấy tinh thần A**: giảm độ đậm Lexend xuống 400–500 (thay 600), giãn nhẹ; tránh chữ quá nặng làm mất "chuyên gia điềm tĩnh".
- **Màu: nền giấy ấm + cobalt ngả tím của A** (hue ~233, ít chói hơn `#1a23d1`), gradient chiến dịch theo A nhưng 2/3 diện tích xanh, san hô chỉ là vệt mảnh; chữ nhỏ luôn nằm trên thẻ kính/giấy.
- **Ứng dụng: lấy từ B** thẻ chứng từ nghiêng với vệt quét sáng và thông điệp "Bớt nhập lại. Đúng mốc. Minh bạch." — dùng làm minh hoạ chiến dịch, không làm logo.

Vì sao: C thắng ở tiêu chí kỹ thuật cứng (16px, đơn sắc, hệ innvie), A thắng ở gu và tính cách, B thắng ở thông điệp. Không chọn A nguyên bản vì ký hiệu yếu và có nguy cơ "ii"; không chọn B vì ký hiệu rơi đúng điều cấm.

Việc cần làm trước khi trình founder: đo lại mọi chữ nhỏ trên gradient (≥4.5), thử C ở 12–24px + mono, và so cạnh logo với ảnh ref ElevenLabs để chắc không bị gọi là "bản xanh".
