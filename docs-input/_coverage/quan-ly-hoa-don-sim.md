# Sổ đối chiếu: Solutions for Invoice Management — SIM (SRC-07)

> Nguồn: `sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md`
> Bản: 12/10/2026 (nhận 2026-10-12)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| I. Đặt vấn đề | ➖ | | giới thiệu tài liệu |
| 2.1 Luồng thanh toán tự động qua API Banking | ➡ payment-on-behalf |  |  |
| 2.2 Tạo JobID nghiệp vụ (AI01) | ⬜ | | AI đọc chứng từ có ở `docs/service-delivery/brainstorms/service-delivery.md` Mục 5.1 bước 0; còn JobID Nháp, kiểm trùng (loại + DK05 + file), AI để trống trường độ tin cậy thấp, thời gian đọc ≤10s/≤60s, hạn mức gọi AI/ngày, CS phụ trách = CS của DK05, chặn tạo khi nợ xấu |
| 2.2.4 Luồng tạo JobID thủ công | ⬜ | | chưa có |
| 2.3 Công tác chuẩn bị | ➖ | | kế hoạch chuẩn bị triển khai với ngân hàng, MISA, không phải yêu cầu |
| 3.1 Trích xuất mã QR động và tĩnh để thanh toán | ➡ payment-on-behalf |  | QR ≥3 lần/15 phút, đồng chủ tài khoản 15tr/50tr, 10tr/30tr |
| 3.2 Phát hành và điều chỉnh hóa đơn tự động (MISA meInvoice) | ➡ debt-management |  | lệch SOP tổng quát 4.10 |
| 3.3 Thu thập, định danh hóa đơn đầu vào và thanh toán tự động (IIP) | ⬜ | | A9 có một phần; lệch A9 vs IIP; pháp nhân Delta Vận tải (SIM) vs Delta Hải Phòng (VIS-SIM) |
| 3.3.5 Hóa đơn vô chủ | ⬜ | | luồng hoàn tiền chi cá nhân, chưa có |
| 4.1 Rủi ro xử lý mã QR động | ➡ payment-on-behalf | | |
| 4.2 Rủi ro nghẽn chữ ký số và Cục thuế từ chối cấp mã | ➡ debt-management | | |
| 4.3 Rủi ro mất đồng bộ trạng thái thanh toán Delta MIS – MISA AMIS | ➡ debt-management | | |
| 5.1 Hướng dẫn phân loại hóa đơn | ⬜ | | nhóm mã phí 02xx/0201/03xx; tạm ứng tiền mặt (E2) trái với SIM bỏ quỹ tạm ứng |
| 5.2 Chi phí thực hiện kết nối API Banking | ➖ | | báo giá ngân hàng, không phải yêu cầu |
