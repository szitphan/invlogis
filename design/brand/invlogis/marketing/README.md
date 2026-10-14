# Marketing M3 · việc 3.3 (nháp, chờ founder duyệt)

Tài liệu 1 trang, mẫu mạng xã hội, banner ra mắt. Hướng A · Lụa. Giọng "chúng tôi – bạn". Slogan: "Khai mở cách vận hành mới." / "Open a new way to operate." (DEC-072). Không nêu tên khách (DEC-060). Bằng chứng ghi ẩn danh: "một doanh nghiệp vận tải container, khoảng 110.000 lô/năm". Số chưa có nguồn để `[chờ: …]`.

## Danh sách file

| File | Cỡ | Dùng cho |
|---|---|---|
| `one-pager/one-pager-vi.html` `.pdf` `.png` | A4 (794×1123 px) | Gửi khách, in, đính kèm email chào bán (Việt) |
| `one-pager/one-pager-en.html` `.pdf` `.png` | A4 | Bản tiếng Anh |
| `social/post-01-announce` | 1080×1350 | Giới thiệu sản phẩm (thẻ chứng từ minh hoạ + câu nêu kết quả) |
| `social/post-02-feature` | 1080×1350 | Nêu một tính năng (thẻ chứng từ minh hoạ, nền sáng) |
| `social/post-03-insight` | 1080×1080 | Nhận định, câu hỏi gợi vấn đề |
| `social/post-04-stat` | 1080×1080 | Một con số (đang để `[chờ: số]`) |
| `social/post-05-behind-the-build` | 1080×1350 | Hậu trường xây sản phẩm |
| `social/post-06-hiring` | 1080×1350 | Tuyển dụng, giới thiệu đội |
| `social/story-01-teaser`, `-02-question`, `-03-cta` | 1080×1920 | Story: giới thiệu, câu hỏi/bình chọn, kêu gọi |
| `social/cover-linkedin` | 1128×191 | Ảnh bìa trang công ty LinkedIn |
| `social/cover-facebook` | 1640×624 | Ảnh bìa Facebook |
| `social/cover-youtube-x` | 1500×500 | Ảnh bìa YouTube / X |
| `launch/launch-web-hero` | 1920×600 | Hero trang web ngày ra mắt |
| `launch/launch-email-header` | 1200×400 | Đầu email ra mắt |
| `launch/launch-social` | 1080×1350 | Bài ra mắt trên mạng xã hội |
| `launch/launch-event-backdrop` `.png` `.pdf` | 3000×2000 | Phông sân khấu / backdrop sự kiện |
| `launch/launch-countdown-story` | 1080×1920 | Story đếm ngược |
| `contact-sheet.png` | | Xem nhanh toàn bộ |
| `assets/` | | Chữ, logo, nền đã chép từ `design/brand/invlogis/` |

Nền rực r1–r3 chỉ có trong thư mục `launch/`; mọi thứ còn lại dùng nền n1, n2, n5, n6.

## Sửa và dựng lại

1. Mở file `.html`, sửa chữ ở thẻ có `data-edit` hoặc ô `[chờ: …]` (mỗi file có chú thích đầu file ghi cỡ và lệnh dựng).
2. Dựng PNG (chạy từ gốc repo): `python3 design/brand/_drafts/_tools/render.py <file>.html <file>.png --size <rộng>x<cao>`. One-pager: thêm `--scale 2`; PDF: `render.py <file>.html <file>.pdf` (không cần `--size`).
3. Đổi chữ dài thì xem lại ảnh: tiêu đề có thể xuống dòng và đè phần dưới.
4. Mọi mẫu dựa trên `assets/m3.css`; HTML mở bằng trình duyệt là xem được.

## Kiểm đã làm

- Luật chữ trên gradient (0–56% chữ trắng, 56–70% không chữ, 70–100% chàm đêm): mọi chữ đặt trực tiếp lên nền đều lấy mẫu pixel dưới khung chữ và đạt từ 4.5:1 (Facebook, email, countdown, launch đã đổi nền hoặc dời chữ để đạt). Chữ ngoài vùng đó nằm trong chip kính.
- Logo: vùng an toàn 0,5–1 x, cỡ lớn hơn mức tối thiểu (cao ≥ 20 px, lockup "by innvie" ≥ 48 px). Nền cobalt sáng dùng `invlogis-mono-white`.
- Thẻ chứng từ ở one-pager, post-01 và bài ra mắt là thẻ dựng bằng HTML với giá trị hiển nhiên giả (`VD-0000`, `MSKU 000000-0`, `00.000 kg`) và nhãn "Dữ liệu minh hoạ" / "Sample data"; không còn ảnh chứng từ có số trông thật.
- Logo story đếm ngược đã dời xuống vùng chàm đậm ở chân.
- Đã xem từng PNG, sửa các chỗ đè chữ.
- Phần máy KHÔNG kiểm: giọng văn, đúng ý nghĩa.

## Cỡ chuẩn theo khung (px)

| Khung | Logo cao | Lề | Tiêu đề | Thân | Chân bài |
|---|---|---|---|---|---|
| 1080×1350, 1080×1080 | 56–64 | 80 | 78–100 (Lexend 300) | 32–36 | 24, "Invlogis là sản phẩm của innvie." |
| 1080×1920 (chừa 250 trên, dưới) | 64 | 80 | 100–110 | 38 | 26 |
| Banner ngang 1200–1920 | 48–64 | 64–120 | 60–92 | 26 | không |
| Phông 3000×2000 | 230 (lockup by innvie, duy nhất) | 220 | 220 | 84 (câu innvie), 52 (EN) | không |

Chân bài không gõ lại logo bằng font; chỉ dùng logo SVG hoặc câu chữ.

## Câu chữ chờ founder duyệt: dòng innvie ở phông sự kiện

- VI: "innvie, công ty đứng sau Invlogis, trong tiếng Na Uy còn có nghĩa là khánh thành và khai mở: hôm nay chúng tôi khai mở một cách vận hành mới."
- EN: "innvie, the company behind Invlogis, also means to inaugurate and to open in Norwegian: today we open a new way to operate."

## Quyết định nội dung đã áp ở vòng sửa R4a

- Mục "Vấn đề" của one-pager theo phần Vấn đề của landing page: DEM (phí lưu container), DET (phí lưu vỏ), chứng từ giấy về chậm, Excel/Zalo; tiếng Anh dùng demurrage/detention. Khối "Giá trị" thay bằng "Làm riêng cho cảng Việt" (ePort, mốc DEM/DET, 6 mẫu quy trình).
- Ô nhiên liệu bỏ khỏi one-pager vì còn nằm trong PRD OQ-13 như Nhân sự; thêm ô "Cấu hình theo khách". Khi OQ-13 chốt, thêm lại.
- Thêm dòng `[chờ: đã chạy bao lâu, kết quả đo được, nguồn]` dưới câu 110.000 lô; EN CTA đổi thành "Book a walkthrough".

## Câu hỏi mở

1. Thông tin liên hệ: email, số điện thoại, website (đang `[chờ: …]` ở one-pager, banner).
2. Ngày, địa điểm ra mắt; số ngày đếm ngược.
3. Có cho nêu "khoảng 110.000 lô/năm" ở dạng ẩn danh trong tài liệu gửi ngoài không, và khi nào được nêu tên khách (BL-056)?
4. PRD OQ-13: Nhân sự và nhiên liệu chưa đưa lên one-pager; xin founder chốt gói.
5. Nhãn "Dữ liệu minh hoạ" đã có trên mọi thẻ chứng từ; xác nhận có giữ trên bản gửi ngoài.
6. Con số cho bài `post-04-stat` và các mục `[chờ: …]` ở hậu trường, tuyển dụng.
7. Duyệt dòng innvie ở phông sự kiện (mục trên); có nêu thêm nghĩa "cống hiến" không.
9. "Xem Invlogis chạy với chứng từ của bạn": đội có cam kết demo bằng chứng từ thật của khách không (NDA, nơi lưu)?
10. Có nêu ePort, cảng cụ thể trên tài liệu bán hàng không.
8. Chưa có màn xem lãi lỗ theo lô (PRD OQ-3): các mẫu không hứa tính năng này.
