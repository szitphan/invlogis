# Sổ đối chiếu: Phân hệ APAS — Hệ thống tự động hóa thanh toán & Đối soát công nợ (SRC-07)

> Nguồn: `sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md`
> Bản: 17/10/2026 (nhận 2026-10-19)

Bản 17/10 (2026-10-19): đổi tên SIM thành APAS, sổ dựng lại theo số mục mới (xem `_changes/2026-10-19-apas-thanh-toan-doi-soat.md`). Mục 3.4 là nội dung SRC-25 gộp vào, giao giống sổ SRC-25 (`debt-management`).

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| I. Đặt vấn đề | ➖ | | giới thiệu tài liệu; bản 17/10 thêm đoạn mở đầu APAS (nối Delta MIS – ngân hàng – MISA AMIS, tài khoản ngoại bảng, duyệt ba cấp) — các ý này có ở 3.3 |
| 2.1 Luồng thanh toán tự động qua API Banking | ➡ payment-on-behalf | | không đổi so với bản 12/10 |
| 2.2 Khai thác và số hóa tài liệu trung tâm (DIS) | ➡ service-delivery | | thay 2.2 AI01 cũ (đang ở `service-delivery` Mục 5.1 bước 0, cần rà lại). DIS là hạ tầng dùng chung: quét 1 lần, 3 đầu ra — danh mục lô hàng (`shipment-coordination`), JobID nháp 90% (`service-delivery`), hóa đơn đầu vào sạch (IIP, `debt-management`). bản 17/10 không nhắc luồng tạo JobID thủ công; user chốt 2026-10-19: vẫn giữ luồng thủ công khi AI OCR lỗi và để sửa trường AI đọc sai (ngưỡng thời gian đọc, hạn mức gọi AI/ngày của bản 12/10 chưa có ở bản mới) |
| 2.2.1 Giới hạn phạm vi thông tin (scope of data flow) | ➡ service-delivery | | kênh vào: Zalo OA, Telegram, WeChat, Gmail Workspace, tệp tải lên App/Web; DIS không tham gia quy trình nghiệp vụ |
| 2.2.3 Logic xử lý theo đối tượng đầu vào và định tuyến đầu ra | ➡ service-delivery | | nhận diện chứng từ vận tải (B/L, Booking) theo từ khóa, ánh xạ DK05 + báo giá/hợp đồng, kiểm ISO 6346; nhận diện hóa đơn GTGT sang IIP; chặn ảnh mờ trên App (khóa nút "Gửi") |
| Luồng xử lý Hóa đơn đầu vào | ➡ debt-management | | gói dữ liệu hóa đơn đã tách (MST, ký hiệu, số, ngày, tiền trước thuế, thuế, tổng) chuyển IIP |
| 2.2.4 Ma trận điều phối danh mục đầu ra của DIS Engine | ➡ service-delivery | | bảng ví dụ 5 kênh; chứng từ lỗi (null đích) vào hàng đợi tra soát thủ công, chặn tạo JobID |
| 2.2.5 Hạ tầng đám mây và Nội dung làm việc với Đại lý Google (HVN Group) | ➖ | | việc chuẩn bị hạ tầng với đại lý theo hợp đồng 29042026-HVN/DELTA (GCP trả sau, processor, Gmail API + Pub/Sub, hạn mức API/ngày, cảnh báo ngân sách 50/80/90%), Riêng Delta, không phải yêu cầu phần mềm |
| 3.1 Thanh toán qua luồng API Banking (PAB) | ➡ payment-on-behalf | | trước là 3.1 Trích xuất mã QR; QR ≥3 phút hiệu lực, QR gốc <15 phút chặn, đồng chủ tài khoản 15tr/50tr, 10tr/30tr (không đổi) |
| 3.2 Phát hành và điều chỉnh hóa đơn tự động (SII) | ➡ debt-management | | lệch SOP tổng quát 4.10; mới ở bản 17/10: chỉ phát hành hóa đơn thay thế khi Mẫu 04/SS-HĐĐT đã ký số và gửi Cục thuế thành công |
| 3.3 Tự động đối soát hóa đơn đầu vào và thanh toán (IIP) | ➡ debt-management | | A9 (`transport-dispatch`) có một phần; lệch A9 vs IIP; pháp nhân Delta Vận tải (SIM) vs Delta Hải Phòng (VIS-SIM). Bản 17/10: đầu vào chỉ XML meInvoice + JSON DIS; định danh 2 lớp; kiểm trùng trước đối chiếu; khớp 1-1 thêm lệch ngày ≤3 ngày + bảng ánh xạ MST/tên tài khoản; N-1, 1-N sai số 0 VND, lệch vào hàng chờ 24 giờ; 3 trường hợp, chi tiền cá nhân duyệt ba cấp CBQL → Kế toán → BGĐ |
| 3.3.3 Quản lý hóa đơn vô chủ | ➡ debt-management | | trước là 3.3.5; bản 17/10 chia 2 nhóm: lỗi đối soát (kế toán gán mã FT, trả về danh mục chờ thanh toán của nhân viên) và xuất nhầm MST (từ chối hoặc chấp nhận tạo Yêu cầu thanh toán theo Quy trình 5.3); ⚠ theo SOP Quản lý quỹ & Thanh toán, có hóa đơn là Quy trình 5.2 (5.3 là không hóa đơn), cần hỏi khách |
| 3.3.4 Quy trình thanh toán hóa đơn không có mã FT (trả bằng tiền cá nhân) | ➡ debt-management | | kê JobID + nhóm phí, duyệt CBQL → Kế toán → BGĐ; JobID kế toán tự tạo Yêu cầu thanh toán, JobID nghiệp vụ chuyển vào JobID đó; "Quy trình 5.2" ở đây là Thanh toán có hóa đơn của SOP Quản lý quỹ & Thanh toán (đánh số riêng từng SOP, không lệch với 3.2) |
| 3.4 Tự động kê khai & nộp báo cáo thuế hàng tháng (ATR) | ➡ debt-management | | nội dung SRC-25 (`_coverage/sim-ke-khai-thue-tu-dong.md`) gộp vào; tờ khai 01/GTGT, 05/KK-TNCN, 01/NTNN; ký MISA eSign, nộp T-VAN MISA mTax trước ngày 20; upload hóa đơn + chốt lương trước ngày 12, IIP đẩy AMIS trước ngày 15 |
| 3.4.4 Kế hoạch triển khai | ➖ | | việc chuẩn bị với MISA, không phải yêu cầu; mốc ngày 12/15 đã ghi ở dòng 3.4 |
| IV. Rủi ro vận hành | ➡ debt-management | | 4.2 hàng đợi ký số, thử lại 1/5/15 phút, quá 5 lần "Ký số lỗi" báo kế toán; 4.3 đồng bộ ngược sang MISA AMIS ghi mã FT vào "Số chứng từ gốc" |
| 4.1 Rủi ro xử lý mã QR động | ➡ payment-on-behalf | | |
| 5.1 Hướng dẫn phân loại hóa đơn | ⬜ | | nhóm mã phí 02xx/0201/03xx; tạm ứng tiền mặt (E2) trái với bỏ quỹ tạm ứng; bản 17/10 đổi: nhóm 02 khác, 01, 04, 05 "phân loại theo JobID kế toán" (trước: không cần phân loại bước 2) |
| 5.2 Chi phí thực hiện kết nối API Banking | ➖ | | báo giá ngân hàng, không phải yêu cầu |
