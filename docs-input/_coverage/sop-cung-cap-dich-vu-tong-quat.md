# Sổ đối chiếu: Quy trình cung cấp dịch vụ tổng quát (SRC-03)

> Nguồn: `sop/sop-cung-cap-dich-vu-tong-quat.md`
> Bản: 24/9/2026 (nhận 2026-10-01)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1. Mục đích | ➖ | | giới thiệu tài liệu |
| 2. Phạm vi áp dụng | ➖ | | giới thiệu tài liệu |
| 3. Tài liệu tham chiếu | ➖ | | danh sách tài liệu, không phải yêu cầu |
| 4.1 Sơ đồ quy trình cung cấp dịch vụ tổng quát | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 5.1 | |
| 4.2.1 Bảng mã JobID nghiệp vụ | ⬜ | | 12 loại JobID chưa ghi vào brainstorm; giao diện riêng theo loại JobID |
| 4.2.2 Luồng luân chuyển JobID nghiệp vụ | ⬜ | | đã có DP-02 (Mục 6.1); nhánh "Không có vận tải" (3 luồng) đã chốt 12/10 nhưng chưa ghi |
| 4.2.3 Duyệt JobID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` DP-01, Mục 6.3 | |
| 4.2.4 Yêu cầu vận tải | ✅ | `docs/shipment-coordination/brainstorms/shipment-coordination.md` Mục 6.3 | |
| 4.2.5 Job ID nghiệp vụ và Yêu cầu vận tải | ✅ | `docs/shipment-coordination/brainstorms/shipment-coordination.md` Mục 5.1, 6.3 | |
| 4.2.6 Phạm vi dịch vụ của Job ID nghiệp vụ | ⬜ | | đổi phạm vi sau khi tạo; chặn cứng soát thiếu chi phí, doanh thu theo phạm vi ở bước Hoàn thành (đã chốt 12/10, chưa ghi) |
| 4.2.7 Kê khai nhu cầu mua ngoài dịch vụ | ⬜ | | chưa có trong brainstorm |
| 4.2.8 Ghi nhận doanh thu dịch vụ lên JobID | ⬜ | | doanh thu bằng 0; OQ mới: Hoàn thành dịch vụ cần doanh thu "đã chuyển duyệt" hay "đã duyệt" |
| 4.2.9 Ghi nhận doanh thu trả hộ lên JobID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E9 | |
| 4.2.10 Ủy quyền thanh toán JobID | ✅ | `docs/shipment-coordination/brainstorms/shipment-coordination.md` B2, Mục 5.1 bước 3 | |
| 4.2.11 Thông tin viết hóa đơn trả hộ | ⬜ | | mục mới bản 24/9, chưa có trong brainstorm |
| 4.3 Mua ngoài dịch vụ | ➡ debt-management |  | nhà cung cấp, phân loại, quy trình mua ngoài; kê khai trên JobID (4.2.7) ở lại service-delivery |
| 4.3.5 Phương thức thanh toán chi phí mua ngoài (mã phí 02xx) | ➡ debt-management |  | nhóm mã phí 02xx/0201/03xx |
| 4.4 Hạch toán nội bộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7, DP-13, OQ-4, OQ-16 | |
| 4.4.2 Các trường hợp hạch toán nội bộ | ⬜ | | TH2 "chia sẻ JobID" chưa rõ đã phủ bởi B7 chưa |
| 4.5 Lệch pha giữa kỳ thanh toán và kỳ hạch toán | ➡ debt-management |  | kỳ ghi chi phí về muộn |
| 4.5.3 Ghi nhận doanh thu và chi phí | ➡ debt-management |  |  |
| 4.5.3.4 Trạng thái của JobID nghiệp vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 6.3 | |
| 4.6 Chi phí không hóa đơn | ⬜ | | định mức hải quan; quyết định công tác phí chưa ghi |
| 4.7 Hàng đường sắt | ⬜ | | D6, D7, E3 ở transport-dispatch; doanh thu đường sắt, JobID J11 tự sinh chưa ghi |
| 4.8 Hàng CBT | ⬜ | | D10 đã có; tiền USD, VAT 0%, DK05 chính chưa ghi |
| 4.9.1 Thủ tục chuyên ngành | ⬜ | | |
| 4.9.2 Thủ tục hải quan | ⬜ | | |
| 4.9.3 Kỳ lập báo cáo nội bộ | ⬜ | | |
| 4.9.4 Nợ quá hạn | ⬜ | | gia hạn nợ (vai Sales, BGĐ) trái với "không duyệt ngoại lệ" ghi ở Mục 6.3 |
| 4.9.5 Hạn mức tín dụng | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` DP-01 | |
| 4.9.6 Chi phí dở dang | ⬜ | | |
| 4.10 Giải pháp phát hành hóa đơn | ➡ debt-management |  | lệch với SIM (SIM ghi QT 5.2, SOP ghi 5.4) |
| 5.1 Quy trình tạo JobID | ⬜ | | khung có ở Mục 5.1 bước 0; còn tạo thủ công, khai báo giá/hợp đồng, số container thực nhận |
| 5.2 Quy trình cung cấp dịch vụ | ⬜ | | Hoàn thành dịch vụ có ở Mục 5.1 bước 8; còn nhánh không vận tải và chặn soát thiếu |
| 5.3 Quy trình quản lý nợ phải trả | ➡ debt-management |  |  |
| 5.4 Quy trình quản lý nợ phải thu | ➡ debt-management |  |  |
| 5.5 Quy trình hạch toán nội bộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7 | |
| 6.1 Bảng thông tin JobID | ⏳ | | phụ lục trống, OQ-5 ở service-delivery |
| 6.2 Bảng kê doanh thu trên JobID | ⏳ | | OQ-5 |
| 6.3 Bảng kê chi phí trên JobID | ⏳ | | OQ-5 |
