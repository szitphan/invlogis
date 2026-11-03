---
type: research
feature: fleetio-srs
status: draft
updated: 2026-11-02
---

# Phát hiện của reviewer, bộ SRS Fleetio

Bốn reviewer chỉ đọc (BA, QA, kỹ thuật, UX) ngày 02/11/2026. Reviewer không xác minh lại trên Fleetio. Phần lớn phát hiện còn mở vì bộ này mô tả Fleetio, còn nhiều yêu cầu chỉ có nghĩa khi viết SRS thật của Invlogis.

## Đã sửa

Nhãn bằng chứng reset nhắc · Overdue của sự cố · chuyển trạng thái nhắc, mục lỗi, tồn kho, Automation · ERD mục lỗi nhiều sự cố · luồng vùng vào, ra · nhãn tầng FR bật module, giới hạn gói · tồn âm tách Fleetio và đề xuất · Capacity Alert tách Fleetio và đề xuất · NFR cách ly khách, dữ liệu gửi AI, đường đọc gộp · OQ bị bỏ sót và OQ mới · tham chiếu UC-03, OQ-7, EUP · sai số màn và mô tả màn nhắc.

Sơ đồ userflow cả 6 nhóm (vẽ lại khi đưa lên Figma ngày 02/11/2026): thêm cạnh Reopen và nhánh Closed, đủ mã lỗi trên sơ đồ, số 1.1b thành 1.4 và 2.0 thành 2.3.

## Còn mở, nên làm khi chuyển thành SRS Invlogis

| Nhóm | Việc | Nguồn |
|---|---|---|
| Kiểm thử | FR P0 đổi demo sang test kèm điều kiện nghiệm thu; tách "Quan sát Fleetio" và "Acceptance Invlogis"; Success Criteria có công thức đo; tách FR ghép (FR-repair-012, 013) | QA 1, 8, 9, 11 |
| Lỗi | Gộp lỗi lệch tiền một mã; thêm cột "Invlogis kỳ vọng"; chuyển bug Fleetio sang Mục 11; thêm lỗi Out of Sequence, thiếu điều kiện hoàn thành, mở lại bị khoá; flows dẫn đủ mã lỗi | QA 2–7 |
| Bảo mật | Truy cập hỗ trợ của innvie; sandbox không chép dữ liệu thật; API, SAML, MCP, webhook, xuất dữ liệu, chống vòng lặp Automation; dữ liệu cá nhân lái xe | Kỹ thuật 1–5 |
| Tầng | "Gói: Khách lớn" chưa có; phiếu dầu nên `[Lõi] [Cấu hình]` cho khách đổ ngoài; Capacity Alert ra khỏi Giám sát; nhắc giấy tờ tách khỏi gói xưởng; số chính sách cần mã `P-…`; `saas-core-vs-tenant.md` dòng 122 và 203 đặt tên gói lệch | Kỹ thuật 6–8 |
| ERD | Service Entry nối đầu việc; bộ lịch có thực thể lịch; giấy tờ của người; người nộp phiếu; sự cố gắn dòng việc; phụ tùng trên lệnh nối PART; đánh giá nhiều lần; Group, Watcher, Comment | Kỹ thuật 9, 10 |
| Khả thi | Đo GPS điện thoại ở bãi trước khi lấy chống kiểm khống; phiếu offline nộp muộn gặp luật Out of Sequence; chuyển endpoint, tên trường khỏi FR sang ghi chú bằng chứng; xem điều khoản Fleetio về việc ghi API nội bộ | Kỹ thuật 11, 12 |
| Màn | Cấp số, block cho form sự cố, danh sách đơn, danh sách xe, form xe, hộp gán, hộp nhận; bảng lỗi cho 2.2, 2.3; trạng thái rỗng, đang tải, lỗi; thêm Mục 3 cho 3 userflow; cột Data type lẫn ràng buộc | UX 1–12 |
| Truy vết | Actor không khớp Mục 2; FR, BR chưa có UC; hạ nhãn `Chạy` xuống mức thật ở FR-015, Flow nhắc, bản đồ; trạng thái giấy tờ | BA 9, 12–15 |
