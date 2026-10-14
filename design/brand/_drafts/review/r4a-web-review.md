# R4a — Review landing page Invlogis (việc 3.2)

Phạm vi: `design/brand/_drafts/m3/web/` (VI + EN, site.css, site.js, 3 ảnh preview, 2 og-image). Đã đọc toàn bộ HTML, JS, preview 1440 VI/EN, mobile 390 EN, og VI/EN. Không tự render 360px (chỉ xem preview 390 và soát media query max-width 480/560).

## Điểm

| Vai | Điểm | Một câu |
|---|---|---|
| A. Giám đốc vận tải container | **6,5/10** | Câu chuyện đúng hướng, giọng không sáo, nhưng vấn đề còn ở mức "chung", thiếu nỗi đau tiền bạc (phạt lưu cont/lưu vỏ) và bằng chứng chỉ là một con số ẩn danh. |
| B. Brand guardian | **8/10** | Bám giọng, bảng màu, quy tắc chữ trên gradient, ẩn danh Delta. Trừ điểm vì còn lỗi kỹ thuật nhỏ (href `##`), "Transparent" song ngữ lặp, và dải ra mắt đầy placeholder. |

## A. Góc nhìn giám đốc

Điều làm tôi muốn xem tiếp:
- H1 "Khai mở cách vận hành mới." đúng DEC-072, nhưng H1 không nói sản phẩm làm gì. Câu phụ ngay dưới ("đọc Booking Note, eDO, EIR, phiếu cân vào thẳng hồ sơ lô hàng. Bạn kiểm tra, bấm lưu") mới là câu bán hàng. Tôi chỉ hiểu nhờ câu này.
- Demo EIR có ô `[kiểm lại]` ở số seal: đây là chi tiết đáng tin nhất trên trang. "Không có hộp đen" hợp với giá trị Minh bạch.
- Dòng "AI đọc chứng từ là điểm mạnh nhất, nhưng không phải tất cả" và "AI agent là hướng đi, chưa phải tính năng đang bán" khiến tôi tin hơn hẳn các trang AI thông thường. Câu chuyện AI **đáng tin**.

Điều khiến tôi do dự:
1. **Vấn đề còn chung chung.** 4 thẻ eDO / EIR / ePort / Excel-Zalo nói "nhập tay", nhưng người trong nghề đau ở chỗ khác: quá hạn lưu cont/lưu vỏ bị hãng tàu phạt, cược cont, đổi lệnh, xe chờ ở cổng Cát Lái, chứng từ giấy về chậm sau khi xe đã giao. Brand-strategy đã có "5 vấn đề khách đầu tiên xác nhận" (nhập lại, giao việc qua Zalo, phạt lưu cont/lưu vỏ, giấy về chậm, chi phí chưa hạch toán). Trang chỉ dùng được ~2,5/5, và **bỏ phần đau nhất (tiền phạt)**. README cũng tự nhận (câu hỏi mở 4) là mô tả ở "mức chung".
2. **Thẻ ePort yếu nhất:** "Mỗi cảng một cổng, một cách làm; thông tin đi qua lại giữa các màn bằng tay." Không nói Cát Lái / Hải Phòng, không nói việc cụ thể (đặt lịch lấy/trả cont, thanh toán phí, tra trạng thái). Người đọc không thấy mình. Khi chưa có nội dung đã kiểm với khách, nên rút còn 1 câu chắc chắn hoặc bỏ thẻ này.
3. **Thẻ eDO:** "hạn lưu bãi" nhập tay trước khi điều xe: cần BA/khách xác nhận cụm từ (người trong nghề hay nói "hạn lệnh", "free time/DET-DEM", "hạn trả vỏ"). Dùng sai thuật ngữ là mất uy tín ngay.
4. **Bằng chứng mỏng.** Một con số ẩn danh `~110.000 lô/năm` + hai placeholder. Với giám đốc quy mô 10.000–200.000 lô, tôi muốn biết: bao lâu thì xong một lô chứng từ, tỷ lệ phải sửa tay. Hai chỗ này đang là `[chờ: …]`. Trang vẫn ổn khi chưa có, nhưng **không được đăng** với placeholder.
5. **Không có "bước tiếp theo" ngoài demo:** không nói demo mang lại gì ("gửi vài chứng từ mẫu" tốt), nhưng thiếu: bao lâu triển khai, có cần đổi quy trình không, dữ liệu cũ thế nào. Một dòng "Nền tảng đã chạy thật…" ở hero là tốt nhưng chưa trả lời "liệu có hợp công ty tôi?" (đội xe, chi nhánh, 10.000–200.000 lô). Form có ô số lô hàng nhưng trang không nói đối tượng phù hợp.
6. **Lợi ích định lượng vắng mặt** (chủ ý, tránh bịa số). Chấp nhận, nhưng khi đo được phải thêm ngay; hiện trang đọc hơi "mô tả tính năng" hơn "kết quả".
7. Module "Điều vận… nhận biết sớm việc sắp trễ hạn lưu container": đây là điểm bán mạnh nhất mà lại chìm trong thẻ nhỏ. Nên nâng lên (xem Should fix).

Quá lời / sáo: không có "hàng đầu", "toàn diện", "giải pháp đột phá". "Đi trước về AI" trong giá trị Đổi mới hơi tự khen nhưng được chặn bằng "mỗi bước đều có cơ sở". Chấp nhận.

## B. Góc nhìn brand guardian

Đúng:
- Giọng "chúng tôi – bạn" nhất quán, câu ngắn, tính từ ít. Điều khoản Mục 7 "Avoid" (ảnh stock, sáo rỗng ngành, xanh công nghệ đại trà) không vi phạm. Không ảnh người, không container giả.
- DEC-060: không có chữ "Delta" ở bất cứ file nào (grep html/js/css/md: 0). Cách gọi "một doanh nghiệp vận tải container" khớp.
- Số `110.000`: `brand-strategy.md` (dòng 126, 204, 239, 257) **cho phép** dùng ẩn danh, kèm phạm vi, và cấm gắn vào riêng phần AI. Trang tuân thủ: hero ghi "Nền tảng đã chạy tại một doanh nghiệp…", mục Bằng chứng ghi "Một doanh nghiệp vận tải container đang vận hành trên nền tảng này." Không gắn vào AI. Đúng. Lưu ý duy nhất: README câu hỏi mở 6 hỏi "được phép công khai chưa?"; strategy nói được với điều kiện ẩn danh, nên đóng câu hỏi này, nhưng founder vẫn nên xác nhận lần cuối vì Delta chưa đồng ý (BL-056).
- Không có số bịa nào khác (20/11/2026, HDMU 7305 2214, SL 0458213 là dữ liệu minh hoạ, được gắn nhãn "mẫu · dữ liệu minh hoạ"). Ngày 20/11/2026 nằm sau hạn bàn giao ~13/11: hơi lạ nhưng vô hại.
- Logo: dùng đúng cặp primary/reverse theo nền, lockup "by innvie" chỉ ở chân trang (đúng kiến trúc thương hiệu: innvie là chữ ký nhỏ). Hero dùng nền n6, vision n3, chữ trắng ở vùng tối: khớp quy tắc 0–56% trắng, 56–70% trống, 70–100% mực. Xem preview: hero và vision không có chữ lọt vào vùng sáng; thẻ demo kính tối nằm ở vùng sáng và đọc được.
- Mục 9: chỉ chạm điểm chạm thương hiệu, không sửa design.md. Đúng.

Chưa đúng / cần chỉnh:
1. **Dải ra mắt r1** ở đầu trang chứa `[chờ: ngày ra mắt]` hiển thị công khai. Hợp với bản nháp, nhưng đây là thứ đầu tiên người ta thấy. Cần cờ rõ để gỡ trước khi đăng.
2. **Giá trị song ngữ cạnh nhau ("Transparent / Minh bạch")** ở trang VI: nhãn tiếng Anh phía trên chữ Việt đọc như thừa. Tiếng Anh là tên giá trị chính thức trong brief? Brief dùng "Minh bạch · Đáng tin cậy · Đổi mới". Trang EN hiển thị "Minh bạch" ngược lại cũng thế (preview EN: "Minh bạch" nhỏ phía trên "Transparent"). Giữ một ngôn ngữ mỗi trang.
3. **Gradient text:** hero H1 và vision đều trắng thuần: an toàn. Không thấy chữ mực nào dùng ở vùng 70–100% nên chưa kiểm được nhánh đó; không có lỗi.
4. Thương hiệu dùng "lụa" mạnh ở hero, vision, AI card, nhưng các dải còn lại (vấn đề, giá trị, bằng chứng) khá phẳng/trắng-ngà, nên sau hero trang bớt "gu ElevenLabs", nghiêng sang trang SaaS chuẩn. Không vi phạm, chỉ là cơ hội.
5. Số lớn `~110.000` kiểu chữ mảnh xanh cobalt: đẹp, đúng gu, nhưng tilde "~" ở cỡ lớn trông như lỗi. Dùng "khoảng 110.000".

## Kiểm kỹ thuật

| Mục | Kết quả |
|---|---|
| Tiếng Anh tự nhiên | Tốt. "Re-typed many times", "Already running, at real scale", "We say plainly what exists and what does not" đọc bản ngữ. Sai nhẹ: "Add-on plans" đúng nhưng "Profit-and-loss per shipment: [chờ]" còn thô; "Fix anything, then save" hợp lý. |
| Dấu tiếng Việt | Không thấy lỗi trong HTML, preview, og-image (đã xem "Khai mở cách vận hành mới" đầy đủ dấu). |
| Responsive | Preview 390 xếp 1 cột, không tràn ngang trong ảnh. Media query xuống 480/560. 360px **không tự render**, rủi ro thấp (các hàng chỉ 1 cột), nên người duyệt kiểm bằng tay trên máy thật. Trang 390px dài 10.466px: rất dài, xem Should fix. |
| Reduced-motion | `site.js` kiểm `prefers-reduced-motion` trước khi gắn animation: không JS hoặc giảm chuyển động thì hiện sẵn trạng thái cuối. CSS có khối `@media(prefers-reduced-motion:reduce)`. **Đạt.** Lưu ý: ở `play()` có `reset()` gọi 2 lần (thừa, vô hại). Animation lặp vô hạn không có nút tạm dừng; WCAG 2.2.2 yêu cầu cho chuyển động quá 5 giây tự chạy. Nên thêm nút dừng hoặc chỉ chạy 1–2 vòng. |
| Alt | Logo có alt, bản dark `alt=""` + `aria-hidden` (đúng). Demo có `role="img"` + aria-label đầy đủ, nội dung bên trong `aria-hidden`: ổn. |
| Focus | `:focus-visible` outline 2px; ô nhập có ring riêng. Có skip-link. Đạt. |
| Form label | Mọi ô có `<label>` bọc, autocomplete đúng. Đạt. Thiếu thông báo lỗi và vùng `aria-live` cho "cảm ơn" (có `focus()` vào hộp, chấp nhận). |
| Tương phản | README nêu số đo n6 11,5:1, n3 7,2:1. Chữ phụ kiểu mono nhỏ ("Bạn luôn thấy chỗ nào AI đọc…", "Xưởng, dầu, nhân sự đóng gói theo gói…") ở preview trông xám nhạt, cỡ nhỏ: nên đo lại trên nền ngà. |
| Lỗi mã | (1) `href="##lien-he"` và `href="##contact"` (hai dấu #): nút "Đặt lịch demo" ở hero, dải ra mắt, menu **không nhảy** tới form. (2) `<nav aria-label="Vấn đề">` / `"The problem"`: nhãn điều hướng đang là tên mục đầu tiên, sai. (3) Chuyển ngôn ngữ: trang VI có `<span aria-current="true">` ổn. |
| Meta/SEO | og:image đường dẫn tương đối, README đã ghi `[chờ: domain]`. og-image tốt (chữ đủ dấu, logo "iv" rõ). Chữ trong og-image-en: dòng phụ tràn 2 dòng, ổn. |
| Form | Chỉ front-end; dòng "Bản nháp: biểu mẫu chưa gửi dữ liệu đi đâu" hiển thị công khai: gỡ khi có backend. Chưa có liên kết chính sách quyền riêng tư dù có ô đồng ý. |

## Must fix (xếp hạng)

1. **Neo "Đặt lịch demo" không hoạt động.** `index.html` dòng ~46, ~63 và dải ra mắt; `en/index.html` dòng 46, 51, 63: đổi `href="##lien-he"` → `href="#lien-he"`, `href="##contact"` → `href="#contact"` (kiểm id thực tế của section form). Đây là CTA chính duy nhất của trang.
2. **Nhãn nav sai.** `index.html` dòng 44: `aria-label="Vấn đề"` → `aria-label="Điều hướng chính"`; `en/index.html` dòng 44: `"The problem"` → `"Main navigation"`.
3. **Viết lại mục "Vấn đề" cho khớp thực tế cảng Việt** (`index.html` ~dòng 88–90, `en/index.html` tương ứng): thêm thẻ/câu về phạt lưu container–lưu vỏ quá mốc và chứng từ giấy về chậm (đã có trong brand-strategy "5 vấn đề khách xác nhận"); đổi thẻ ePort sang việc cụ thể hoặc bỏ nếu BA chưa xác nhận; nhờ BA/khách đối chiếu thuật ngữ eDO ("hạn lưu bãi" → cụm người ngành dùng). README câu hỏi 4 chưa đóng thì **không đăng**.
4. **Sửa "Transparent / Minh bạch" song ngữ lẫn trang** (`index.html` khối Giá trị; `en/index.html` tương tự): mỗi trang chỉ một ngôn ngữ (VI: Minh bạch · Đáng tin cậy · Đổi mới; EN: Transparent · Reliable · Innovative).
5. **Gỡ/ẩn mọi placeholder `[chờ: …]` khỏi bản đăng**: dải ra mắt (ngày), thời lượng demo, hai ô bằng chứng, lộ trình lãi lỗ, chân trang. Thêm một lệnh kiểm `grep -c "\[chờ" ` vào checklist đăng trang. Riêng dòng "chờ: khách đồng ý nêu tên" và "chờ: số đo tỷ lệ trường AI phải sửa tay" là **ghi chú nội bộ lộ ra công khai**, phải bỏ khỏi trang kể cả khi đăng sớm.
6. **Animation lặp vô hạn, không có cách dừng** (`assets/site.js`, hàm `play`: `later(play, t + 5200)`): thêm nút "Tạm dừng" hoặc dừng sau 2 vòng (WCAG 2.2.2).

## Should fix

- Hero: thêm nhãn nhỏ (eyebrow) nói rõ sản phẩm ("Nền tảng vận hành cho giao nhận, vận tải container Việt Nam") trước H1, vì H1 một mình không nói gì. Hiện eyebrow là "AI đọc chứng từ · Điều vận · Xưởng · Công nợ": được nhưng chưa nêu đối tượng.
- Nâng điều vận "nhận biết sớm việc sắp trễ hạn lưu container" thành mục riêng hoặc thẻ lớn thứ hai cạnh AI: đây là lợi ích tiền bạc rõ nhất.
- Đổi `~110.000` thành "Khoảng 110.000" (cỡ lớn) cả VI và EN ("About 110,000").
- Thêm dòng "Phù hợp với: doanh nghiệp có đội xe, nhiều chi nhánh, 10.000–200.000 lô/năm" gần form hoặc bằng chứng (brief Mục 1).
- Đo lại tương phản chữ phụ mono nhỏ trên nền ngà/n3; không dưới 4,5:1.
- Thêm liên kết chính sách quyền riêng tư cạnh ô đồng ý; thêm thông báo lỗi cụ thể từng ô.
- Trang dài 10.466px trên mobile: xem xét gộp "Giá trị" và "Bằng chứng" hoặc thu ngắn thẻ vấn đề thành danh sách.
- Dải sau hero hơi phẳng: thêm 1 chi tiết "lụa" nhỏ (đường kẻ gradient mảnh) để giữ gu xuyên suốt, không cần ảnh mới.
- Bỏ lệnh `reset()` gọi hai lần trong `play()`.
- Ngày mẫu 20/11/2026 trong demo: đổi thành ngày quá khứ gần để không gây thắc mắc.

## Câu hỏi cho founder

1. Khẩu hiệu làm H1 (DEC-072) hay đưa "Chứng từ vào. Hồ sơ sẵn." làm H1 để nói được sản phẩm ngay? Em nghiêng về giữ DEC-072 nhưng thêm eyebrow nêu đối tượng (Should fix 1).
2. Con số 110.000 lô/năm: strategy cho phép ẩn danh, nhưng Delta chưa đồng ý (BL-056). Anh muốn công khai trên trang ngay hay chờ Delta đồng ý?
3. Có chấp nhận lộ nội dung "Xưởng, dầu, nhân sự đóng gói theo gói" (README câu hỏi 3) trước khi có bảng giá? Giám đốc sẽ hỏi giá ngay.
4. Ai kiểm thuật ngữ eDO/EIR/ePort với khách trước khi đăng (BA hay chính Delta)? Chưa có người chịu trách nhiệm.
5. Dải ra mắt r1: giữ cho tới ngày ra mắt hay chỉ bật từ ngày ra mắt (README câu hỏi 2)?
6. Form gửi về đâu, ai trả lời trong bao lâu? Cam kết thời gian phản hồi nên ghi lên trang.
