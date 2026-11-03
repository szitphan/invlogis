# Soát màn Fleetio, nhóm repair đợt đầu (12 frame)

Section 7221:239423 và 7224:242319. Chiều cao frame không đổi nên không phải dời nhóm ảnh gốc.

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.1 issues-list 7218:222540 | Khớp | Không cần sửa | Dòng #9 (BSA104TRNS, thu hồi, Đã xử lý) chỉ thấy nửa trong ảnh nên không vẽ. Nút "..." cạnh Tự động hoá không vẽ |
| 1.2 issue-open 7221:225993 | Đã sửa | Thêm tiêu đề nhóm "Tất cả trường". Phiếu kiểm tra #125988723: tách badge đỏ "Không đạt" khỏi dòng chữ | Các dòng dưới "Người phụ trách" ảnh bị cắt |
| 1.3 issue-resolved 7221:226558 | Đã sửa | Thêm "Tất cả trường" | Không |
| 2.1 wo-list 7218:223490 | Đã sửa | Bỏ cột "Tổng chi phí" (ảnh không có). Thêm cột "Ngày bắt đầu dự kiến", "Ngày hoàn tất dự kiến" (giá trị —). Cột Người phụ trách dời cuối. Chỉnh độ rộng cột để tiêu đề không bị cắt | Người phụ trách #1, #4 là ảnh đại diện, đọc không ra tên nên ghi —. Dòng #6 đến #9 bị popup che nên bỏ. Dòng #4 cột Đầu việc: ảnh thấp nét, chưa chắc tên đầu việc thứ hai |
| Calendar 7221:239454 | Khớp | Không cần sửa | Nút "Lưu thay đổi" ảnh có viền cam, bản vẽ để nút thường |
| Resource Scheduler 7221:240174 | Đã sửa | Thêm xe BSA108TRNS, BSA109TRNS. Lịch nhỏ: thêm ngày 1 đến 5/12 tháng sau (hàng 29-30 gộp, hàng 6 màu nhạt) | Ô chọn tháng/năm và ô hôm nay tô vàng của lịch nhỏ chưa vẽ |
| 2.2 wo-edit 7221:228404 | Đã sửa | Bốn ô ngày (bắt đầu dự kiến, bắt đầu thực tế, hoàn thành dự kiến, hoàn thành thực tế) điền 02/11/2026 20:37 (ảnh 11/02/2026 8:37pm). Thêm ô số lệnh "100" cạnh tiêu đề | Ảnh chỉ tới "Dùng số đồng hồ bắt đầu"; các khối Sự cố, Dòng việc, Tổng hợp chi phí bên dưới không có trong ảnh nên không đối chiếu được. Chữ xám của bốn ô ngày trong ảnh có thể là placeholder chứ không phải giá trị thật (đã điền theo gợi ý của brief) |
| 2.3 wo-detail 7221:227136 | Đã sửa | Thêm "Tất cả trường" | Phần dưới dòng "Dòng việc" ảnh bị cắt |
| 3.1 service-entry 7221:227793 | Đã sửa | "2 nguồn" sửa thành "1 nguồn". Thêm "Tất cả trường". Thêm hai dòng tổng hợp thấy rõ trong ảnh: Tạm tính + 1.700.000 ₫, Công 500.000 ₫ | Các dòng tổng hợp còn lại (phụ tùng, tổng) ảnh bị cắt nên chưa vẽ. Nhãn nhỏ cạnh tên đầu việc và nút Collapse chưa vẽ |
| 4.1 faults 7221:224463 | Đã sửa | Thêm dòng thiếu BSA105TRNS / P0401 (Đã xử lý, #13) | Dòng thứ 9 trở đi bị popup che nên bỏ |
| 5.1 service-tasks 7221:225010 | Đã sửa | Thêm cột Mô tả và Mã lý do sửa chữa mặc định (—). Đổi dòng 8 sang A/C Expansion Valve. Thêm 3 dòng: Receiver Dryer, System Evacuate & Recharge, System Test (đúng thứ tự ảnh). Chỉnh độ rộng cột | Dòng 12 trở đi bị cắt. Cột "Mã cụm mặc định" ảnh bị cắt ở "Default Assem…" |
| 6.1 warranty-new 7221:229320 | Đã sửa | Ngày bắt đầu điền 02/11/2026. Thêm ô chọn đơn vị thời hạn "Năm" | Ô "Standard Warranty" ảnh có nền xanh nhạt khi chọn, bản vẽ không tô. Panel "Added Warranties" bản vẽ là thẻ, ảnh là panel phẳng |

Radio và checkbox: đã soát, đúng loại. Am/pm đổi 24h: đã soát ngày giờ trên các màn, đúng. Layout audit 6.1 chỉ báo lỗi trong Sidebar/Header (không đụng).

Loại lỗi lặp lại: thiếu dòng hoặc cột mà ảnh thấy rõ (4 màn), thiếu tiêu đề "Tất cả trường" (4 màn), ô ngày để trống dù ảnh có giá trị (2 màn).
