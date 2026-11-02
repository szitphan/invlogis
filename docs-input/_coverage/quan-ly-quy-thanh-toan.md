# Sổ đối chiếu: Quy trình quản lý quỹ & Thanh toán (SRC-31)

> Nguồn: `sop/quan-ly-quy-thanh-toan/quan-ly-quy-thanh-toan.md`
> Bản: 06/10/2026 (nhận 2026-10-19)

Phần lớn mục giao cho feature mới `fund-payments` (Quản lý quỹ và thanh toán: tạm ứng, thanh toán của nhân viên, đặt cọc, phiếu thu/chi, quỹ tiền mặt), user chốt slug ngày 2026-10-19. Nợ hóa đơn/trả hóa đơn (thanh toán hóa đơn trả hộ) giao `payment-on-behalf` giống APAS (SRC-07); thanh toán nhà cung cấp giao `debt-management` giống SOP CCDV 5.3 (SRC-03). Bản 06/10 cũ hơn APAS 17/10: khi viết brainstorm cần đối chiếu đồng chủ tài khoản (5.1.2.4, 5.2.2.5: chỉ luồng TTNHĐ) và số bước duyệt (5.2: 2 bước) với APAS 3.1 và 3.3 (duyệt ba cấp CBQL → Kế toán → BGĐ khi chi tiền cá nhân).

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1. Mục đích | ➖ | | giới thiệu tài liệu: báo cáo chi phí theo mã phí, văn phòng, nhân viên, khách hàng; lưu hóa đơn theo chế độ kế toán |
| 2. Phạm vi áp dụng | ➖ | | một câu: mọi loại chi phí ở các văn phòng chi nhánh |
| 3. Tài liệu tham chiếu | ➖ | | danh sách tài liệu; nội dung từng đính kèm có dòng riêng bên dưới |
| 4.1 Các khái niệm chung | ➡ fund-payments | | JobID; đơn vị nhận tiền trả hộ (hãng tàu, cảng, bãi) không phải nhà cung cấp; cấm số âm trên Yêu cầu thanh toán, Đề nghị tạm ứng, phiếu thu/chi |
| 4.2 Tạm ứng tiền mặt | ➡ fund-payments | | bỏ "tạm ứng chuyển khoản"; tạm ứng hóa đơn trả hộ < 5 triệu; hạn 7 ngày từ ngày duyệt Phiếu chi, cảnh báo còn 2 ngày, quá hạn khóa tạm ứng mới; gia hạn rút gọn 3 bước; 2 tiêu chí phân loại; hạn mức theo mã nhân viên; 5 trạng thái; "Dư nợ tạm ứng 1" |
| 4.3 Dư nợ tạm ứng của nhân viên | ➡ fund-payments | | 3 loại dư nợ; dư nợ 2 (TTNHĐ) là tài khoản trung gian, không sang Misa, không hạn mức; dư nợ 3 (đặt cọc) là TK 244; chuyển giao khi nghỉ việc/chuyển việc |
| 4.4 Thanh toán & Thanh toán có hóa đơn | ➡ fund-payments | | phân loại theo nhóm phí (JobID kế toán/nghiệp vụ) và theo 6 mục đích; không đối ứng tạm ứng, dư nợ 1 chuyển sang module nhân sự; 4 trạng thái Yêu cầu thanh toán |
| 4.5 Thanh toán nợ hóa đơn | ✅ | `docs/payment-on-behalf/brainstorms/payment-on-behalf.md` B1, B4, OQ-9 | hạn trả hóa đơn 3 ngày làm việc, quá hạn khóa quyền tạo TTNHĐ; duyệt trong 2 ngày cuối tháng thì khóa từ ngày làm việc đầu tháng sau; tạo từ JobID (CS, hiện trường) và Lệnh vận tải (lái xe) |
| 4.6 Thanh toán trả hóa đơn | ✅ | `docs/payment-on-behalf/brainstorms/payment-on-behalf.md` B1–B6, OQ-14 | báo cáo dư nợ 2 đầu tháng, thu hồi bằng Phiếu thu; comment 09/10: anh Nghĩa bỏ đoạn "thanh toán không hóa đơn để nhận lại số tiền này" |
| 4.7 Thanh toán không hóa đơn | ➡ fund-payments | | chi phí quản lý chung không chứng từ; chi phí định mức (COGS) ghi lên Mã nhân viên; hoa hồng khách hàng qua Mã DK05; comment 09/10: tạm ứng không hạn chế, quản lý ở module nhân sự; ⚠ chốt ranh giới với `employee-records` (BL-215) |
| 4.8 Quản lý tiền đặt cọc | ➡ fund-payments | | 5 trường hợp đặt cọc; TK 244, dư nợ 3 không hạn mức; hoàn trả nhiều lần; không đòi được thì ghi TK 811 / TK 1388 |
| 4.9 Phiếu chi và Phiếu thu | ➡ fund-payments | | phần mềm tự tạo phiếu từ Yêu cầu thanh toán/Đề nghị tạm ứng; thủ quỹ tạo tay chỉ ở tình huống đặc biệt |
| 4.10 Thanh toán nhà cung cấp | ➡ debt-management | | nhận dữ liệu từ Quy trình quản lý nợ phải trả (SRC-03 5.3); chặn thanh toán NCC qua quy trình khác; hạn trả sau tính theo cách 1/cách 2, lưu trên danh mục NCC; comment 08–09/10 về lý do tách 6 quy trình |
| 4.11 Hướng dẫn thực hiện các quy trình | ➡ fund-payments | | bảng 8 quy trình; tạm ứng hóa đơn trả hộ < 5 triệu hoặc tổng < 5 triệu/ngày |
| 4.12 Số âm trong thanh toán và tạm ứng | ➡ fund-payments | | 15 trường hợp ở Đính kèm 04 |
| 5.1 Quy trình tạm ứng tiền mặt | ➡ fund-payments | | duyệt 2 bước; chủ tài khoản chính duyệt trên ngân hàng; webhook lấy UNC; ⚠ đồng chủ tài khoản lệch APAS 3.1 (BL-215) |
| 5.2 Quy trình thanh toán có hóa đơn | ➡ fund-payments | | chọn hóa đơn từ AI01 cùng nhóm phí, tổng tiền tự cộng; comment 09/10: biên lai cũng dùng quy trình này, duyệt xong là trả tiền; ⚠ 2 bước duyệt, APAS 3.3 là 3 cấp (BL-215) |
| 5.3 Quy trình thanh toán không hóa đơn | ➡ fund-payments | | |
| 5.4 Quy trình thanh toán nợ hóa đơn | ✅ | `docs/payment-on-behalf/brainstorms/payment-on-behalf.md` A1–A11, OQ-3, OQ-4 | QR động (≥ 3 phút), QR tĩnh, tài khoản đối tác; gợi ý 3–5 cảng bãi gần lái xe; duyệt bước 1 theo giới hạn duyệt và hạn mức trên ngân hàng |
| 5.5 Quy trình thanh toán trả hóa đơn | ✅ | `docs/payment-on-behalf/brainstorms/payment-on-behalf.md` B1, B2, OQ-7, OQ-18 | |
| 5.6 Quy trình quản lý tiền đặt cọc | ➡ fund-payments | | |
| 5.7 Quy trình thanh toán nhà cung cấp | ➡ debt-management | | |
| 5.8 Quy trình Phiếu chi | ➡ fund-payments | | |
| 5.9 Quy trình Phiếu thu | ➡ fund-payments | | |
| 5.10 Quy trình quản lý quỹ tiền mặt | ➡ fund-payments | | bổ sung quỹ bằng séc hoặc API Banking |
| 6.1 Quy tắc ghi chép đối ứng | ➡ fund-payments | | ghi 1 lần, khóa sau khi ghi; sửa sai bằng phiếu thu/chi, không dùng số âm; không dùng khái niệm "Hoàn ứng" |
| 6.2 Hạn mức tạm ứng | ➡ fund-payments | | 5 mức theo chức danh (CS, hiện trường, sales, thanh tra: 0–60 triệu; CBQL 30–120 triệu; BGĐ 100–500 triệu); lái xe không có hạn mức; khi viết brainstorm cần đưa qua mã tham số P-… |
| 6.3 (trống) | ➖ | | mục không có tiêu đề và nội dung trong bản gốc |
| 6.4 Phân quyền duyệt tạm ứng & thanh toán | ➡ fund-payments | | bảng quy trình × nhóm phí, bản gốc tự ghi "dự thảo, có thể chưa nhất quán"; bảng gọi Phiếu chi/Phiếu thu là 5.7/5.8 trong khi thân bài là 5.8/5.9; 6.4.2 hạn mức duyệt còn trống (BL-215) |
| 6.5 Báo cáo | ➡ fund-payments | | 6 mẫu báo cáo (tạm ứng, có HĐ, không HĐ, TTNHĐ & TTTHĐ, đặt cọc, quỹ tiền mặt) |
| Đính kèm 01 Quản lý hóa đơn đầu vào (AI01) | ➡ invoice-management | | bản 20/06; APAS 17/10 thay AI01 bằng DIS + IIP (SRC-07 2.2, 3.3), đối chiếu khi viết IIP |
| Đính kèm 02 API Banking | ➡ payment-on-behalf | | bản 03/03; UNC, sổ phụ điện tử, lưu đồ dự kiến; bảng phí ngân hàng là báo giá, không phải yêu cầu (như SRC-07 5.2) |
| Đính kèm 03 Công tác phí | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E14 | trùng SOP tổng quát 4.6; Quyết định giao Lệnh hằng tháng ở transport-dispatch (BL-218) |
| Đính kèm 04 Thanh toán âm | ➡ fund-payments | | 15 trường hợp + giải pháp đề xuất |
| Đính kèm 05 Job ID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B8, B14, E20, E21, Mục 5.3, Mục 6.3, OQ-69 | bản 26/07; bảng mã lệch SOP 24/9 (OQ-69), thêm trạng thái Đã xuất hoá đơn, Đã đóng (Mục 6.3, DEC-228); JobID kế toán ➡ cost-catalog (dòng riêng); JobID xưởng ➡ phân hệ xưởng; JobID vận tải = Lệnh ➡ transport-dispatch |
| Đính kèm 05 — JobID kế toán (2.2, 3.2, Phụ lục 4.2, 4.4) | ➡ cost-catalog | | K01–K07 theo nhóm phí cấp 1/cấp 2 |
| Đính kèm 06 Hóa đơn trả hộ | ➖ | | trùng APAS 17/10 mục 2.1 + 3.1 (SRC-07, đã giao payment-on-behalf); bản này cũ hơn |
| Đính kèm 07 Bảng phân quyền duyệt (xlsx) | ➡ fund-payments | | bản Excel của 6.4.1, thêm mã nhóm phí 03xx |
