# R4b — Review văn phòng phẩm Invlogis (task 3.4)

Phạm vi: `design/brand/_drafts/m3/stationery/` (README, 5 PDF, 8 DOCX, 2 HTML danh thiếp, 2 chữ ký email, phong bì, `_src/`, `assets/`). Đối chiếu: `brand-brief.md` Mục 2, 9; `invlogis/logo/logo-spec.md` Mục 2–3; `invlogis/brand-tokens.css`; `guideline/brand-guideline.html`.

Cách kiểm: SVG logo so hash với `invlogis/logo/`; PDF render bằng PyMuPDF rồi đọc bằng mắt; DOCX đọc bằng python-docx; contrast bằng `_tools/contrast.py`. Chưa mở DOCX trong Word/LibreOffice (README đã nêu). Không dựng lại được PNG logo từ SVG (Chrome headless không chạy trong phiên này), nên các PNG dẫn xuất chưa đối chiếu được.

## Bảng kết quả

| # | Hạng mục | Kết quả | File | Bằng chứng |
|---|---|---|---|---|
| 1 | Logo đúng bản đã duyệt | PASS (SVG) | `assets/logo/*.svg`, `email-signature/logo-by-innvie-email.png` | 6/6 SVG trùng SHA-256 với `invlogis/logo/` (`innvie-logo`, `invlogis-by-innvie`, `-reverse`, `invlogis-primary`, `invlogis-reverse`, `invlogis-mono-black`). PNG dẫn xuất không có bản duyệt để so hash, xem Nên sửa. |
| 2 | Vùng an toàn và cỡ tối thiểu | FAIL | `letterhead/letterhead.pdf`, `quotation/*`, `contract/*`, `email-signature/signature-*.html`, `envelope/envelope-dl.pdf` | Cỡ tối thiểu đạt: card 41 mm (≥12 mm), letterhead 13 mm, email 150 px ≈ 56 px cao (≥48), envelope ~16 mm. Vùng an toàn KHÔNG đạt: đường kẻ tiêu đề cách đáy logo ~1,6 mm (1 x ≈ 6,8 mm) ở letterhead/contract/quotation; chữ "Khai mở…" cách logo email ~0,4 x (cần ≥0,5 x); địa chỉ envelope cách logo ~5,6 mm (1 x ≈ 8 mm). Card mặt trước đạt (logo cách mép 7 mm, tagline ở đáy). |
| 3 | Biến thể đúng theo nền | PASS | `business-card/card.print.html` (front), `_src/build_docs.py` (header), `email-signature/*.html` | Mặt trước card (nền tối) dùng `invlogis-by-innvie-reverse.png`; letterhead, báo giá, hợp đồng, email, envelope (nền sáng) dùng bản primary. |
| 4 | Màu từ token + tương phản ≥4,5:1 | FAIL (màu) / PASS (tương phản) | `_src/build_docs.py`, `_src/doc.css`, `_src/build_print.py` | Tương phản: slate/paper 6,97; cobalt/paper 6,72; mực/vàng placeholder 15,70; trắng/chàm đêm 18,48; slate/trắng 7,39; cobalt/trắng 7,13; mực/khói 14,61 (tất cả ≥4,5). Màu: `#FFF1D6` (17 lần, nền placeholder) và `#C9CFE6` (3 lần, đường kẻ) KHÔNG có trong `brand-tokens.css`. Các màu còn lại (`#0E1442`, `#4A5380`, `#2F43DB`, `#FAF8F4`, `#7B55FF`, `#0B1033`, `#E6EAF8`, `#FFFFFF`) đều là token. |
| 5 | Dấu tiếng Việt | PASS | Mọi PDF/PNG preview | Đã xem: card (mặt trước/sau), letterhead, báo giá, hợp đồng, envelope, chữ ký VI. "ệ, ự, ậ, ữ, ạ, ỷ" hiển thị đúng, không có ô vuông. Chữ ký email dùng Arial (không tải font). |
| 6 | Card 90×55, tràn 3 mm, dấu cắt, safe zone | PASS | `business-card/business-card-print.pdf`, `_src/build_print.py` | Mặt in 112×77 mm (đo 111,8×76,9 mm); mặt cắt 90×55 đặt tại x=11…101, y=11…66; nền và dải gradient tràn 3 mm (face 96×61); dấu cắt đen 0,1 mm nằm ngoài tràn lề (2–7 mm). Nội dung cách mép cắt ≥6 mm (logo 7 mm, tagline ~6 mm). Thiếu TrimBox/BleedBox trong PDF (xem Nên sửa). |
| 7 | Thông tin chưa biết là `[chờ: …]` | PASS | Tất cả DOCX/PDF/HTML | 44 `[chờ` trong hợp đồng, 50 trong báo giá, 11 trong giấy tiêu đề; card, email và envelope cũng vậy. Không có tên pháp nhân, MST, SĐT, email, domain, địa chỉ bịa. Tên "Invlogis by innvie" chỉ là thương hiệu (xem Nên sửa về OQ2). |
| 8 | Hợp đồng: mọi thân điều khoản có `[Cần luật sư duyệt]` | FAIL | `contract/hop-dong-template.docx` | 24 mục đánh số có cờ (đúng). Nhưng câu kết "Hợp đồng lập thành [chờ] bản có giá trị như nhau…" (đoạn cuối trước chữ ký) KHÔNG có cờ, và bảng "Điều 1. Các bên" (9 dòng thông tin, có "theo [chờ: giấy ủy quyền]") cũng không có cờ. |
| 9 | Báo giá/hợp đồng formal; chữ ký và giấy tiêu đề theo kiến trúc "by innvie" | PASS | `_src/build_content.py`, `letterhead/`, `quotation/`, `contract/` | Xưng "Quý công ty", "BÊN A/BÊN B", "ĐẠI DIỆN…". Lockup "by innvie" ở header mọi giấy tờ, innvie chỉ đứng ở "(Invlogis by innvie)" và footer. Không có chữ ký riêng cho innvie. |
| 10 | Chữ ký email: bảng, inline, ≤600 px, không web font, logo `<img>` URL tuyệt đối | PASS | `email-signature/signature-vi.html`, `signature-en.html` | `<table role=presentation width=600>`, mọi style inline, không `<style>`/`@font-face`, Arial. `<img src="https://[chờ: domain]/brand/email/logo-by-innvie-email.png" width=150 alt=…>`. (Khoảng cách dưới logo: xem mục 2.) |
| 11 | Không có "Delta", không có ảnh stock | PASS | Toàn thư mục | Grep "delta" và "unsplash/pexels/shutterstock" không ra kết quả. Ảnh nền `bg-n1-chamdem_1920x1080.jpg` có SHA-256 trùng `design/brand/invlogis/backgrounds/` (ảnh nền thương hiệu, không phải stock). |
| 12 | README: danh sách file, thông số in, cách sửa | FAIL (nhỏ) | `README.md`, `_src/` | README đủ mục: danh sách file, danh thiếp 90×55/3 mm/dấu cắt, giấy tiêu đề A4, DL 220×110, cách sửa DOCX, lệnh dựng lại, câu hỏi mở. Sai một chỗ: README ghi "`_src/` dựng lại toàn bộ", nhưng `envelope-dl.pdf` không có script nào trong `_src/` sinh ra. README cũng ghi "chữ tối thiểu in 7 pt" nhưng nhãn T/E/W mặt sau là 6,5 pt. |

**Tổng: 8 PASS · 4 FAIL** (mục 4 tính FAIL vì màu ngoài token; tương phản đạt).

## Must fix (xếp theo mức nghiêm trọng)

1. **Hợp đồng: thiếu cờ luật sư ở câu kết và Điều 1** (mục 8). `_src/build_content.py`: thêm ` [Cần luật sư duyệt]` vào câu "Hợp đồng lập thành…" và thêm một dòng `('Luật sư duyệt', LAW)` vào kv của Điều 1, hoặc gắn cờ vào từng dòng bên. Dựng lại DOCX và PDF.
2. **Giấy tiêu đề và báo giá còn câu hướng dẫn nằm trong thân văn bản** (mục 7/9). `letterhead.docx`: "Lời mở đầu trang trọng: … phông Be Vietnam Pro 10,5 pt, giãn dòng 1,35, căn đều hai bên." `bao-gia-template.docx`: "Tên hạng mục là mẫu, thay bằng gói dịch vụ thực tế." Đây là ghi chú của người dựng, không phải placeholder, nên rất dễ gửi nhầm. Đổi thành `[chờ: …]` hoặc xóa khỏi `build_content.py` (dòng `LH` thứ 5 và dòng báo giá "Invlogis trân trọng gửi…").
3. **Đường kẻ tiêu đề quá sát logo** (mục 2, letterhead/báo giá/hợp đồng). Khoảng cách logo→kẻ khoảng 1,6 mm, cần ≥1 x (~6,8 mm) hoặc ít nhất 0,5 x. Sửa `_src/build_docs.py` (`new_doc`): tăng khoảng cách của đoạn có viền (`para_border(hp,'bottom',…,space=6)`) hoặc tách kẻ thành mép riêng cách bảng header ≥6 mm; kiểm lại trên PDF.
4. **Phong bì DL: dải gradient 3 mm không có tràn lề, và địa chỉ sát logo** (mục 2; README đã nêu). Nếu in offset, dải sẽ bị cắt lệch thành khe trắng. Hoặc thêm tràn lề 3 mm (trang 226×116 mm, dấu cắt), hoặc bỏ dải. Đưa khối địa chỉ xuống cách logo ≥1 x (~8 mm). Envelope chưa có script trong `_src/`, nên sửa xong phải dựng lại được (xem Nên sửa).
5. **Chữ ký email: tagline sát logo và logo sát mép trái** (mục 2, mục 10). `signature-vi.html` / `-en.html`: hàng tagline `padding:0` ngay dưới ảnh; cần thêm padding-top ≥ 0,5–1 x (≈ 28–29 px với logo 56 px cao). Thêm padding-left nhẹ cho hàng logo để không dính mép cột.

## Nice to have

- **Màu ngoài token:** thay `#FFF1D6` (nền placeholder) bằng token gần nhất hoặc khai báo là màu chỉ dùng cho duyệt trong `brand-tokens.css`; thay `#C9CFE6` (đường kẻ) bằng `rgba(14,20,66,0.14)` (`--brand-border`). README đã nói phải xóa nền vàng trước khi in, nên hiện chấp nhận được.
- **Envelope không dựng lại được:** thêm `_src/build_envelope.py` (hoặc sửa README) để README "dựng lại toàn bộ" đúng.
- **Nhãn T/E/W mặt sau danh thiếp 6,5 pt:** tăng lên 7 pt (`build_print.py`, `.back .ct b`) cho khớp README.
- **PDF danh thiếp không có TrimBox/BleedBox** và kích thước 111,8×76,9 mm (Chrome làm tròn): xác nhận khi duyệt bản in với nhà in, hoặc xuất PDF có TrimBox 90×55 và BleedBox 96×61.
- **PNG dẫn xuất chưa có bản duyệt để đối chiếu:** `invlogis-by-innvie-reverse.png` (danh thiếp), `invlogis-by-innvie.png` (DOCX), `logo-by-innvie-email.png` (email). Xuất lại từ SVG đã duyệt bằng `_tools/render.py`, ghi SHA vào README để lần sau kiểm được.
- **Điều khoản thương mại trong báo giá (4.1–4.5)** chưa có cờ duyệt. README nêu luật sư duyệt cho hợp đồng; nên thêm cờ "[Cần thương mại/pháp lý duyệt]" như hợp đồng.
- **OQ2 (vai trò innvie):** "(Invlogis by innvie)" trong Điều 1 hợp đồng và Bên A báo giá đang ngầm coi innvie là bên ký. Chờ founder xác nhận trước khi dùng.
- **Khẩu hiệu "Khai mở cách vận hành mới." trên danh thiếp và email:** README OQ6 cho thấy chưa chốt có đặt khẩu hiệu trên văn phòng phẩm không.
- **Email, Outlook:** nhãn "Điện thoại" bold 12 px trong cột 62 px có thể xuống dòng; kiểm trong Outlook desktop.
- **DOCX chưa mở bằng Word/LibreOffice** (README đã nêu): kiểm nhanh header logo, trang "X / Y" và độ lệch font so với PDF.
- **Card mặt trước:** tagline Lexend 300 trắng 7 pt trên ảnh nền tối, nét mảnh; cân nhắc 400 để đọc rõ khi in.

## Ghi chú

- Không ghi file nào khác ngoài báo cáo này. Ảnh PDF đã render để xem được lưu ở thư mục scratchpad của phiên, không nằm trong repo.
