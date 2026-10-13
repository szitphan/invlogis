---
type: meeting
status: stale
status_prev: draft
status_changed: 2026-10-12
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-12
links:
  - docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Ghi nhận trả lời — Câu hỏi cần xác nhận, Điều phối (vòng 1)

> Ngày nhận: 2026-10-10 | Người trả lời: anh Nghĩa (Delta), bằng văn bản | Bộ câu hỏi gửi ngày 2026-10-06, 24 câu

Khách không bấm chọn phương án mà viết toàn bộ vào ô "Ý kiến thêm" (thư trả lời ghi "Đã trả lời 0/24"). Đội đối chiếu từng câu với các phương án trong deck; cột "Phương án" là cách đội hiểu.

## Quyết định

| Câu | Mã | Câu hỏi | Phương án | Quyết định của Delta | Ghi chú |
|---|---|---|---|---|---|
| 1 | OQ-16 | Chi nhánh khác làm việc cho một JobID | A (đúng đề xuất) | Theo 2 trường hợp giao dịch nội bộ trong SOP. Tạo JobID trái tuyến (TH1) hoặc giao việc trái tuyến (TH2) là dấu hiệu để phần mềm tự ghi nhận giao dịch nội bộ và tự hạch toán | Yêu cầu mới: tự nhận diện + tự hạch toán |
| 2 | OQ-4 | Chia lợi nhuận giữa chi nhánh | C | Chia theo tỷ lệ lãi gộp, 50/50 | Phải chốt bảng kê công nợ phải thu, phải trả rồi mới hạch toán nội bộ |
| 3 | OQ-12 | CBT và đường sắt dùng tạm SOP 18/9 | Không chọn A/B | CBT và đường sắt không có giao nhận tại cảng (CBT thuê ngoài toàn bộ) nên không đi qua Điều phối. Mỗi loại JobID có giao diện riêng, kéo theo Yêu cầu vận tải và Lệnh vận tải riêng | Chi tiết chờ quy trình điều vận |
| 5 | OQ-18 | Quản lý vỏ container | Ngoài phạm vi | Giai đoạn 1 chưa có quản lý container. Chi phí sửa chữa container ghi trên Lệnh vận tải, ở chức năng Điều vận | |
| 7 | OQ-21 | Cảng, depot làm nhiều nhất | Bỏ câu hỏi | Không thống kê được (HCM); lấy số thật khi phần mềm chạy | Không cài sẵn thứ tự ưu tiên cảng |
| 8 | OQ-25 | Lý do CS chuyển việc làm Lệnh nâng vỏ | A, rút gọn | Nút đổi tên thành "Chuyển việc". Chỉ 2 lý do: (1) Hết giờ làm việc, (2) Khác, tự ghi. Bắt buộc nhập lý do | |
| 9 | OQ-26 | Lịch trực ngoài giờ | A | Cán bộ quản lý hiện trường giao việc trực ngoài giờ | Yêu cầu mới: quy trình bàn giao việc khi bắt đầu và kết thúc ca trực |
| 10 | OQ-27 | Gộp giao việc Lệnh hạ vỏ rỗng | B (ngược đề xuất) | Lệnh hạ rỗng chỉ có ở hàng nhập FCL. Gộp theo vận đơn + nơi hạ chỉ khi JobID có 1 container; nhiều container thì làm từng container vì khách nhận hàng khác ngày | |
| 12 | OQ-20 | Ký nhận hàng trên điện thoại lái xe | Cả điện tử và giấy (xác nhận 12/10) | Làm cả 2 để khách chuyển đổi dần | Yêu cầu mới: phần mềm tự gửi email biên bản cho CS và khách ngay khi lái xe xác nhận biên bản khách đã ký (chống giao lận) |
| 13 | OQ-34 | Quá mốc do kẹt xe, sự cố đường | Ngoài phần mềm | Xử lý ngoài phần mềm | Không thêm nhóm nguyên nhân |
| 14 | OQ-29 | Bằng chứng khách đồng ý chi ngoài định mức | Ngoài phần mềm | Giải quyết ngoài phần mềm, rồi ghi nhận và chi trả ở Quy trình CCDV (chi phí mua ngoài) hoặc thanh toán không hoá đơn (Quy trình quản lý quỹ và thanh toán) | Không làm luồng riêng để phần mềm không cồng kềnh |
| 15 | OQ-28 | Ai xác nhận nhận tiền hoàn nâng vỏ | Ngoài phần mềm | Khoản này đã nằm trong dư nợ tạm ứng 2 của nhân viên nghiệp vụ, lái xe; cá nhân tự xử lý | Bỏ theo dõi khoản chờ hoàn |
| 16 | OQ-30 | Đơn giá đường sắt xác định lần đầu | Không chọn A/B/C | Giai đoạn 1: CS làm đơn giá bằng tay. Giai đoạn 2: báo giá trên phân hệ Sales, liên thông dữ liệu | |
| 23 | OQ-11 | CBT xuất hoá đơn cho bên thứ ba | A (đúng đề xuất) | Chấp nhận lệch về hình thức; báo cáo quản trị phản ánh đúng thực tế giao dịch | |
| 24 | OQ-8 | 4 quy trình theo ý kiến Trasas | Đóng | Ý kiến Trasas không làm thay đổi SOP | |

## Còn mở

| Câu | Mã | Delta trả lời | Còn thiếu | Ai trả lời | Hạn |
|---|---|---|---|---|---|
| 4 | OQ-9 | Sẽ làm rõ thông tin định danh hàng đường sắt và các loại hàng khác trong tài liệu về JobID | Tài liệu JobID | Delta | chưa hẹn |
| 6 | OQ-17 | ~110.000 lô hàng/năm (= số Lệnh vận tải); ~50.000 tờ khai/năm (= số JobID J01–J06); Delta HN, VT, BN, HD (HD sẽ giải thể do sáp nhập tỉnh) gấp 3–4 lần Delta HCM về sản lượng và doanh thu; tăng 2 con số mỗi năm | Số người theo chi nhánh. Đã rõ 12/10: VT là chi nhánh Vận Tải, HD là Hải Dương, không có chi nhánh Hải Phòng | Delta | chưa hẹn |
| 11 | OQ-19 | Hàng nhập: số ngày miễn phí lưu container có trên Giấy báo hàng đến. Hàng xuất: CS nhập thời gian miễn phí lưu vỏ để đóng hàng, đã bổ sung vào SOP | Số booking, tàu khi đặt xe; bản SOP đã bổ sung | Delta | chưa hẹn |
| 12 | OQ-20 | (xem Quyết định) | Phía khách ai ký, khách nào bắt đóng dấu. Đã rõ 12/10: "làm cả 2" là ký điện tử + biên bản giấy | Delta | chưa hẹn |
| 17 | OQ-32 | Giải quyết trong quy trình điều vận (chưa viết) | Quy trình điều vận | Delta | chưa hẹn |
| 18 | OQ-33 | Phí lưu ca xe ghi nhận lên Lệnh vận tải; phí chạy máy phát sẽ phát triển giải pháp | Phần mềm có tự tính phí lưu ca xe không; giải pháp phí máy phát | Delta | chưa hẹn |
| 19 | OQ-6 | Khi lập bảng kê nợ phải thu, phần mềm xác định hoá đơn trả hộ đã ghi trên JobID mà khách không xác nhận thanh toán; sẽ phát triển quy trình xử lý | Quy trình xử lý | Delta | chưa hẹn |
| 20 | OQ-23 | Delta đánh giá cao hướng lấy hoá đơn từ MISA, có thể thay thế Quy trình thanh toán trả hoá đơn; sẽ xem xét kỹ | MISA lấy được hoá đơn đầu vào không; hoá đơn trả hộ mang mã số thuế của ai | Delta | chưa hẹn |
| 21 | OQ-31 | Sẽ làm rõ luồng dữ liệu cho CCDV, QTĐP, QTĐV và các bút toán đối ứng | Bảng loại phí theo địa điểm và cách hạch toán | Delta | chưa hẹn |
| 22 | OQ-10 | Sẽ làm rõ khi viết SOP cho chức năng điều vận | SOP điều vận | Delta | chưa hẹn |
| 24 | OQ-1, OQ-3, OQ-5, OQ-7 | Các quy trình đang hoàn thiện, gửi dần | Quy trình điều vận; phụ lục JobID, định mức, bảng kê; Quy trình quản lý quỹ và thanh toán | Delta | chưa hẹn |
| 24 | OQ-22, OQ-24 | Mã QR tĩnh và động theo một chuẩn duy nhất | Mẫu QR tờ khai, Lệnh giao vỏ điện tử; bãi nào phát hành | Delta | chưa hẹn |

## Việc tiếp theo

| Việc | Ai | Theo dõi |
|---|---|---|
| Cập nhật brainstorm Điều phối theo quyết định trên (cột Trả lời ở Mục 11; phạm vi CBT/đường sắt; B4, B5, E3, E8; bỏ luồng duyệt chi ngoài định mức và theo dõi tiền hoàn; "Chuyển việc"; 6 đề xuất mới) — chờ review | @szitphan | BL-040 |
| Hỏi lại Delta 2 điểm chưa rõ (chi nhánh "VT"; "làm cả 2" ở câu ký nhận) và các câu còn mở ở bảng trên | @szitphan | BL-041 |
