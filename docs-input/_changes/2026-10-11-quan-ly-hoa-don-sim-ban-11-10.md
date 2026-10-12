# Thay đổi: SOLUTIONS FOR INVOICE MANAGEMENT (SIM) — bản 11/10/2026

> Bản cũ: nhận 2026-10-11 (`SIM_Oct 10 2026.pdf`, 16 trang, ngày 10/10/2026) · Bản mới: nhận 2026-10-11 (`SIM_Oct 11 2026.pdf`, 19 trang, ngày 11/10/2026) · Tài liệu: [quan-ly-hoa-don-sim.md](../sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md)

## Tóm tắt nghiệp vụ

- **Mới — AI02 Tạo JobID nghiệp vụ từ chứng từ (mục 2.3).** CS/Điều vận gán trước mã khách (DK05), số báo giá/hợp đồng, loại JobID rồi tải bộ chứng từ định danh lô hàng lên → AI02 (Google Document AI + bộ lọc Regex nội bộ, kiểm số container theo ISO 6346) đổ dữ liệu vào **JobID nháp** → người tạo rà, bổ sung, sửa và bấm duyệt mới phát hành JobID chính thức. Trường độ tin cậy thấp để trống (không đoán). Chỗ người sửa so với AI được lưu riêng để cải tiến bộ luật. Tài liệu nhỏ (1–3 trang, < 5MB) trả kết quả ngay, P95 ≤ 10 giây; tài liệu lớn chạy nền, nhận yêu cầu ≤ 1 giây, xong P95 ≤ 60 giây. Chặn xử lý lặp theo loại JobID + DK05 + tệp. JobID không có chứng từ định danh vẫn tạo thủ công (mục 2.3.4). ⚠ Chạm trực tiếp bước 0 "Tạo và duyệt JobID" của brainstorm Điều phối.
- **Mới — Sổ phụ ngân hàng chặn tạo JobID khi nợ xấu (mục 2.1.2).** Biến động số dư qua webhook → xác định DK05, số hóa đơn, bảng kê nợ phải thu → **cảnh báo nợ quá hạn và chặn tạo JobID nếu nợ xấu**. Bản cũ chỉ nói "dùng để duyệt hay từ chối JobID". Khớp với điểm rẽ DP-01 của brainstorm.
- **AI01 thiết kế lại hẳn (mục 2.2, trước là 2.1).** Bản cũ: nhân viên upload hóa đơn và tự phân loại 2 bước rồi AI quét. Bản mới: Delta **chi trước** mọi khoản, hóa đơn về sau; AI01 nhận từ 2 nguồn — Misa API Gateway (đọc XML, không gọi Google) và upload thủ công của **nhân viên hiện trường/lái xe** (chụp ảnh/PDF, đọc qua Google Document AI) — rồi tự khớp 1-1 với giao dịch ngân hàng (tiền bằng nhau, MST/tên NCC ≈ tài khoản nhận, ngày lập ±3 ngày) để gán JobID + nhân viên. Bỏ bước người upload tự phân loại. Bỏ câu "YCTT phải lấy hóa đơn từ danh mục AI01, không upload lên YCTT như hiện nay". Thêm kiểm va chạm: hóa đơn gắn vào YCTT đang chờ duyệt / đã duyệt / đã thanh toán thì luồng khác dùng lại bị chặn và báo người upload.
- **API Banking viết lại thành 5 bước (mục 2.1, trước là 2.2).** Nội dung chuyển tiền tự sinh: Mã nhân viên - Số JobID - Số vận đơn/Booking - Tên chi phí - Tên khách hàng; QR động không chèn được nội dung → ghép theo mã FT. Kiểm QR còn hiệu lực ≥ 3 phút. Tự chọn tài khoản nguồn theo pháp nhân (Delta HN, Delta HCM, Delta Vận tải). Hạn mức đồng chủ tài khoản (15 triệu/lệnh, 50 triệu/ngày; 10 triệu/lệnh, 30 triệu/ngày) nay nêu cả ở mục 2.1.4, giống mục 3.1.4. Đồng bộ ngược sang MISA AMIS khi nhận webhook thành công.
- **Bỏ khỏi bản mới** (không rõ là bỏ hẳn hay chỉ rút gọn — ⚠ hỏi lại khách):
  - "Ngay khi thực hiện API Banking với ngân hàng đầu tiên thì bắt buộc phải chuyển tiền về ngân hàng này để chi trả toàn bộ hóa đơn trả hộ."
  - "Sau đó chỉ cho phép lập UNC từ một quy trình nghiệp vụ"; tham chiếu "Quy trình 5.4".
  - Đăng ký đồng chủ tài khoản duyệt theo **Mã phí** với hạn mức khác nhau (nay hạn mức theo cấp quản lý).
  - Mong muốn ngân hàng cấp **1 gói API cho cả 3 pháp nhân**.
  - Lưu đồ "Quản lý hóa đơn đầu vào" và lưu đồ "Thanh toán hóa đơn" 6 bước (nay viết bằng chữ).
- **Mới — Công tác chuẩn bị (mục 2.4):** việc cần làm cho đối tác outsourcing tích hợp AI01/AI02 — dự án Google Cloud, chọn bộ xử lý (Document OCR hoặc Lending/Procurement DocAI), cấp quyền, đặt hạn mức gọi theo ngày để kiểm soát chi phí.
- **Mục 3.3.3.1 thêm 1 ý:** với QR động, truy ngược Mã nhân viên + Số JobID bằng mã FT từ webhook ngân hàng.
- ⚠ **Mục lục lệch thân bài:** mục lục ghi 2.1 = AI01, 2.2 = AI02, 2.3 = API Banking (số trang lỗi "Error! Bookmark not defined."); thân bài là 2.1 = API Banking, 2.2 = AI01, 2.3 = AI02. Tài liệu trích "mục 2.x" nên dẫn theo thân bài và hỏi khách thứ tự đúng.
- ⚠ Còn nguyên từ bản trước: bảng phí có Techcombank nhưng thân bài chỉ nêu MB Bank, Vietcombank, TPBank; mục 4.1 vẫn chỉ 1 câu; mục I chưa nhắc AI02 trong mục tiêu.
- Đã giải quyết so với bản trước: các chỗ "Sẽ định nghĩa chi tiết sau", "Mô tả chi tiết", trỏ "Bước 2.1.4.6" không tồn tại — đều nằm trong phần AI01/API Banking cũ đã viết lại.
- Mục III, IV, V: nội dung không đổi (chỉ khác cách chuyển) — riêng 3.2.1.3 "qua Open API" → "qua cổng Open API" và bản mới không còn đường link sang trang MISA.

## Đổi số mục

| Bản cũ | Bản mới |
|---|---|
| 2.1. Quản lý hóa đơn đầu vào (AI01) — 2.1.1 đến 2.1.4.5 | 2.2. Quản lý hóa đơn đầu vào (AI01) — 2.2.1 đến 2.2.3 (viết lại, không tương ứng 1-1) |
| 2.2. Luồng thanh toán tự động qua API Banking | 2.1. Luồng thanh toán tự động qua API Banking |
| 2.2.1.1. Thực hiện Ủy nhiệm chi | 2.1.1. Luồng thực hiện Ủy nhiệm chi (UNC) tự động |
| 2.2.1.2. Sổ phụ ngân hàng | 2.1.2. Luồng số hóa Sổ phụ ngân hàng để quản lý công nợ |
| 2.2.2. Quy trình thanh toán qua API Banking (+ 2.2.2.1, 2.2.2.2) | 2.1.3. Quy trình thanh toán qua API Banking + 2.1.4. Rủi ro vận hành |
| — | 2.3. Tạo JobID nghiệp vụ (AI02) · 2.4. Công tác chuẩn bị |
| III, IV, V | không đổi số |

## Tài liệu đang dùng nguồn này

- `docs/dispatch-coordination/brainstorms/dispatch-coordination.md` — `links:`; **bước 0 "Tạo và duyệt JobID"** (dòng 154, 167–171), luồng AI đọc chứng từ (dòng 65, 82, 606), DP-01 nợ quá hạn (dòng 408, 427, 459, 505) → nên đối chiếu với AI02 (mục 2.3) và chặn JobID nợ xấu (mục 2.1.2). Phạm vi loại trừ "Thanh toán trả hộ" (dòng 45) không đổi.
- `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md` — ghi chú nguồn OQ-17 (7.000 HĐ trả hộ/tháng, vẫn mục 3.1) và OQ-32 (UNC qua API MB/VCB/TPBank, nay mục 3.1 và **2.1**, không còn 2.2).
- `docs/_shared/logistics-primer.html` — dòng nguồn mục trả hộ, không trích số mục → không ảnh hưởng.

## Chi tiết

`diff.py` ghép được mục theo số. Mục II đổi cấu trúc nên so theo ý (xem Tóm tắt nghiệp vụ). Các mục còn lại báo "Sửa" chỉ do khác cách chuyển (định dạng nghiêng, chữ trong sơ đồ ghi theo thứ tự đọc thay vì theo mũi tên, ảnh sơ đồ đổi tên tệp), trừ:

| Mục | Bản cũ | Bản mới |
|---|---|---|
| 3.2.1.3 | "kết nối trực tiếp qua Open API của MISA meInvoice … dịch vụ [MISA meInvoice](link misa.vn)" | "kết nối trực tiếp qua cổng Open API của MISA meInvoice … dịch vụ MISA meInvoice" |
| 3.3.3.1 | (không có) | "Đối với luồng quét mã QR động, hệ thống sử dụng cơ chế mapping số tham chiếu FT nhận từ Webhook ngân hàng với dữ liệu Cache để truy vết ngược lại Mã nhân viên và Số JobID tương ứng." |
| 3.3.3.1 | "Mã JobID: Sử dụng cấu trúc Regex…" | "Số JobID: Sử dụng cấu trúc Regex…" |
