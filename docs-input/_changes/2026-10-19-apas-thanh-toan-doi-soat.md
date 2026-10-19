# Thay đổi: Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ

> Bản cũ: nhận 2026-10-12 (`SIM_Oct 12 2026.pdf`, tên "Solutions for Invoice Management (SIM)") · Bản mới: nhận 2026-10-19 (`Phân hệ APAS_October 17 2026.pdf`) · Tài liệu: [apas-thanh-toan-doi-soat.md](../sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md)

## Tóm tắt nghiệp vụ

- **Đổi tên và mở rộng phạm vi:** SIM (quản lý hóa đơn) thành **APAS** (Automated Payment & Account Reconciliation System). Thêm đoạn giới thiệu: APAS nối Delta MIS, cổng thanh toán ngân hàng và MISA AMIS; hóa đơn lỗi được cô lập ở tài khoản ngoại bảng để tra soát qua **phê duyệt ba cấp**.
- **Mục 2.2 "Tạo JobID nghiệp vụ (AI01)" và 2.3 "Công tác chuẩn bị" bị thay bằng 2.2 "Khai thác và số hóa tài liệu trung tâm (DIS)":** một hạ tầng thu thập chứng từ dùng chung. DIS nhận từ Zalo OA, Telegram, WeChat, Gmail và tệp tải lên. Mỗi chứng từ chỉ gọi Google Document AI **một lần**, rồi ra **3 kết quả**: danh mục lô hàng cho Điều phối, JobID nháp điền sẵn 90% cho CS, dữ liệu hóa đơn đầu vào cho IIP. Có kiểm số container ISO 6346, bẫy lỗi chứng từ không xác định được đích (không tạo JobID), và **chặn ảnh mờ ngay trên App** (khóa nút "Gửi").
  - Bản mới không nhắc luồng tạo JobID thủ công (2.2.4 cũ), các ngưỡng thời gian đọc ≤10s/≤60s, hạn mức gọi AI/ngày và quy tắc kiểm trùng JobID nháp của bản 12/10. **User chốt 2026-10-19:** DIS là giải pháp quét AI OCR mới, không bỏ luồng thủ công. Vẫn cần luồng tạo JobID thủ công khi AI đọc lỗi, và để sửa những trường AI đọc chưa đúng. Phần này đang dùng ở `service-delivery` Mục 5.1 bước 0.
- **Mục 2.2.5 mới — làm việc với đại lý Google (HVN Group)** theo hợp đồng 29042026-HVN/DELTA ký 29/4/2026: bật GCP trả sau theo lượng dùng, cấu hình processor Document AI, mở Gmail API + Pub/Sub, đặt hạn mức gọi API theo ngày và cảnh báo ngân sách ở **50%, 80%, 90%**. Đây là việc chuẩn bị hạ tầng, không phải yêu cầu phần mềm.
- **3.1 đổi tên "Thanh toán qua luồng API Banking (PAB)"**, nội dung QR và hạn mức đồng chủ tài khoản giữ như bản 12/10 (cán bộ quản lý nghiệp vụ ≤15 triệu/lệnh, ≤50 triệu/ngày; quản lý hiện trường ≤10 triệu/lệnh, ≤30 triệu/ngày).
- **3.2 đổi tên SII**, thêm một luật: chỉ cho phát hành hóa đơn thay thế khi **Mẫu 04/SS-HĐĐT** đã ký số và gửi Cục thuế thành công.
- **3.3 IIP viết lại:**
  - IIP không tự gọi OCR nữa, chỉ nhận dữ liệu đã tách từ meInvoice (XML) và DIS (JSON).
  - Định danh 2 lớp: lớp pháp lý và lớp quản trị (mã nhân viên, mã phí cấp 2, JobID).
  - Kiểm trùng (MST + ký hiệu + số hóa đơn) đưa lên **trước** bước đối chiếu.
  - Khớp 1-1 thêm điều kiện **ngày hóa đơn và ngày chi lệch không quá 3 ngày**, kèm bảng ánh xạ MST/tên với tài khoản ngân hàng.
  - Khớp gộp N-1 và tách 1-N phải đúng tuyệt đối (sai số 0 VND). Lệch 1 VND thì vào hàng chờ tra soát 24 giờ.
  - Có 3 trường hợp: (1) đã chi qua API Banking, (2) chi tiền cá nhân, phải duyệt ba cấp Cán bộ quản lý → Kế toán → Ban giám đốc, (3) hóa đơn vô chủ từ meInvoice.
- **3.3.3 Hóa đơn vô chủ chia 2 nhóm:**
  - Nhóm 1 là lỗi đối soát: kế toán gán mã FT, hóa đơn quay về danh mục chờ thanh toán của nhân viên.
  - Nhóm 2 là hóa đơn xuất nhầm MST: kế toán từ chối, hoặc chấp nhận để tạo Yêu cầu thanh toán theo Quy trình 5.3.
  - ⚠ Nhóm 2 ghi "Yêu cầu thanh toán có hóa đơn (Quy trình 5.3)", nhưng theo SOP Quản lý quỹ & Thanh toán thì thanh toán có hóa đơn là Quy trình 5.2 (5.3 là thanh toán không hóa đơn). Cần hỏi khách.
  - Bản 12/10 thì gom "Trường hợp 2" vào vô chủ và hoàn tiền qua kế toán tổng hợp.
- **3.3.4 mới — thanh toán hóa đơn không có mã FT:** nhân viên kê JobID và nhóm phí, duyệt 3 bước. Hóa đơn kê theo JobID kế toán thì tự tạo Yêu cầu thanh toán. Hóa đơn kê theo JobID nghiệp vụ thì chuyển vào JobID đó.
  - Mục này gọi "Quy trình 5.2 thuộc Quy trình quản lý quỹ và thanh toán", còn mục 3.2 gọi Quy trình 5.2 là "Quy trình cung cấp dịch vụ tổng quát". Hai chỗ không lệch nhau: Delta đánh số quy trình riêng trong từng SOP (SOP Quản lý quỹ & Thanh toán 06/10: 5.2 = Thanh toán có hóa đơn, `sop/quan-ly-quy-thanh-toan`; SOP CCDV: 5.2 = Cung cấp dịch vụ). Rà ngày 2026-10-19.
- **3.4 mới — gộp nội dung kê khai thuế tự động (ATR)** từ tài liệu riêng SRC-25 (`sop/sim-ke-khai-thue-tu-dong`, bản 12/10). Nội dung gồm tờ khai GTGT, TNCN, nhà thầu, nộp qua MISA eSign và T-VAN, kế hoạch triển khai. Mốc kế hoạch là upload hóa đơn và chốt lương trước ngày 12, IIP đẩy dữ liệu sang AMIS trước ngày 15.
- **Mục IV rủi ro:** nội dung giữ nguyên. Riêng 4.2 nêu rõ hàng đợi ký số, thử lại sau 1, 5, 15 phút; quá 5 lần thì chuyển "Ký số lỗi".
- **Phụ lục 5.1 đổi quy tắc:** các nhóm chi phí hàng bán khác (02), quản lý chung (01), đầu tư (04), khác (05) chuyển từ "không cần phân loại bước 2" sang **"phân loại theo JobID kế toán"**. Nhóm trả hộ (03) và trả hộ xuất lại hóa đơn (02) ghi rõ "JobID nghiệp vụ".
- **Phụ lục 5.2 chi phí API Banking:** không đổi số liệu.

## Đổi số mục

| Mục cũ (12/10) | Mục mới (17/10) |
|---|---|
| 2.2 Tạo JobID nghiệp vụ (AI01) | 2.2 Khai thác và số hóa tài liệu trung tâm (DIS) — thay nội dung |
| 2.3 Công tác chuẩn bị | bỏ (một phần sang 2.2.5) |
| 3.1 Trích xuất mã QR động & tĩnh để thanh toán | 3.1 Thanh toán qua luồng API Banking (PAB) |
| 3.2 Phát hành và điều chỉnh hóa đơn tự động (Misa meInvoice) | 3.2 Phát hành và điều chỉnh hóa đơn tự động (SII) |
| 3.3 Thu thập & định danh hóa đơn đầu vào và làm thanh toán tự động (IIP) | 3.3 Tự động đối soát hóa đơn đầu vào và thanh toán (IIP) |
| 3.3.2 Sơ đồ kiến trúc hệ thống | 3.3.1 Sơ đồ kiến trúc hệ thống |
| 3.3.4 Quy trình nghiệp vụ & Logic xử lý chi tiết | 3.3.2 Quy trình xử lý dữ liệu và logic nghiệp vụ |
| 3.3.5 Hóa đơn vô chủ | 3.3.3 Quản lý hóa đơn vô chủ |
| — | 3.3.4 Quy trình thanh toán hóa đơn không có mã FT (mới) |
| SRC-25 (tài liệu riêng) | 3.4 Tự động kê khai & nộp báo cáo thuế hàng tháng (ATR) |
| 4.1–4.3 (đề mục) | 4.1–4.3 (gạch đầu dòng trong mục IV, nội dung giữ nguyên) |

## Tài liệu đang dùng nguồn này

- `docs/service-delivery/brainstorms/service-delivery.md` — Mục 5.1 bước 0 (AI đọc chứng từ, JobID nháp) dựa trên 2.2 AI01 cũ: nay là DIS, cần rà lại.
- `docs/transport-dispatch/brainstorms/transport-dispatch.md` — phần IIP / hóa đơn trả hộ của lái xe (A9, điểm giao VIS ↔ SIM): rà theo 3.3 mới (3 trường hợp, duyệt ba cấp).
- `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md`, `docs/meetings/decks/2026-10-15-oq-vis-deck.md` — trích SRC-07 làm nguồn câu hỏi (7.000 hóa đơn trả hộ/tháng, UNC qua MB/VCB/TPBank): số liệu không đổi, chỉ đổi đường dẫn.
- `docs-input/_coverage/sim-ke-khai-thue-tu-dong.md` (SRC-25) — nội dung nay nằm trong 3.4.

## Chi tiết

Theo `diff.py`. Phần lớn khác biệt ở mục lục và cách chép sơ đồ là do cách chuyển, không phải thay đổi nghiệp vụ. Thay đổi thật đã tóm ở trên. Các mục mới (2.2.x DIS, 2.2.5.x, 3.3.4, 3.4.x) có toàn văn trong tài liệu.

## Tổng quan thay đổi

| Loại | Số mục | Mục |
|---|---|---|
| Thêm mới | 13 | 2.2. Khai thác và số hóa tài liệu trung tâm (DIS); 2.2.1. Giới hạn phạm vi thông tin (scope of data flow); 2.2.2. Kiến trúc luồng dữ liệu tập trung (data pipeline); 2.2.3. Logic xử lý theo đối tượng đầu vào và định tuyến đầu ra; 2.2.4. Ma trận điều phối danh mục đầu ra của DIS Engine; 2.2.5. Hạ tầng đám mây và Nội dung làm việc với Đại lý Google (HVN Group); 3.3.4. Quy trình thanh toán hóa đơn không có mã FT (trả bằng tiền cá nhân); 3.4. Tự động kê khai & nộp báo cáo thuế hàng tháng (ATR); 3.4.1. Luồng dữ liệu đối soát & Kết nối thuế toàn diện; 3.4.2. Quy trình tự động hóa & Kê khai các loại thuế hàng tháng; 3.4.3. Quy trình nộp tờ khai thuế tự động lên Cục thuế; 3.4.4. Kế hoạch triển khai; I. Đặt vấn đề |
| Bỏ | 3 | 2.2. Tạo JobID nghiệp vụ (AI01); 2.2.4. Luồng tạo JobID thủ công; 2.3. Công tác chuẩn bị |
| Sửa | 6 | 3.1. Thanh toán qua luồng API Banking (PAB); 3.2. Phát hành và điều chỉnh hóa đơn tự động (SII); 3.3. Tự động đối soát hóa đơn đầu vào và thanh toán (IIP); 3.3.3. Quản lý hóa đơn vô chủ; 4.2. Rủi ro nghẽn chữ ký số và Cục thuế từ chối cấp mã; 5.1. Hướng dẫn phân loại hóa đơn |
| Giữ nguyên | 6 | 2.1 (2.1.1–2.1.4); 4.1; 4.3; 5.2 |
