# Sổ đối chiếu: Quy trình cung cấp dịch vụ tổng quát (SRC-03)

> Nguồn: `sop/sop-cung-cap-dich-vu-tong-quat.md`
> Bản: 24/9/2026 (nhận 2026-10-01)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1. Mục đích | ➖ | | giới thiệu tài liệu |
| 2. Phạm vi áp dụng | ➖ | | giới thiệu tài liệu |
| 3. Tài liệu tham chiếu | ➖ | | danh sách tài liệu, không phải yêu cầu |
| 4.1 Sơ đồ quy trình cung cấp dịch vụ tổng quát | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 5.1 | |
| 4.2.1 Bảng mã JobID nghiệp vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B8, Mục 5.3 |  |
| 4.2.2 Luồng luân chuyển JobID nghiệp vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` DP-02, B12 |  |
| 4.2.3 Duyệt JobID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` DP-01, Mục 6.3 | |
| 4.2.4 Yêu cầu vận tải | ✅ | `docs/shipment-coordination/brainstorms/shipment-coordination.md` Mục 6.3 | |
| 4.2.5 Job ID nghiệp vụ và Yêu cầu vận tải | ✅ | `docs/shipment-coordination/brainstorms/shipment-coordination.md` Mục 5.1, 6.3 | |
| 4.2.6 Phạm vi dịch vụ của Job ID nghiệp vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B9, OQ-66 |  |
| 4.2.7 Kê khai nhu cầu mua ngoài dịch vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E12 | duyệt, thanh toán nhà cung cấp ➡ debt-management |
| 4.2.8 Ghi nhận doanh thu dịch vụ lên JobID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E16 | duyệt doanh thu ở Quy trình 5.4 ➡ debt-management |
| 4.2.9 Ghi nhận doanh thu trả hộ lên JobID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E9 | |
| 4.2.10 Ủy quyền thanh toán JobID | ✅ | `docs/shipment-coordination/brainstorms/shipment-coordination.md` B2, Mục 5.1 bước 3 | |
| 4.2.11 Thông tin viết hóa đơn trả hộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B11, DP-20 |  |
| 4.3 Mua ngoài dịch vụ | ➡ debt-management |  | nhà cung cấp, phân loại, quy trình mua ngoài; kê khai trên JobID (4.2.7) ở lại service-delivery |
| 4.3.5 Phương thức thanh toán chi phí mua ngoài (mã phí 02xx) | ➡ debt-management |  | nhóm mã phí 02xx/0201/03xx |
| 4.4 Hạch toán nội bộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7, DP-13, OQ-4, OQ-16 | |
| 4.4.2 Các trường hợp hạch toán nội bộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7 | TH1, TH2 khớp B7; thêm câu chi nhánh làm toàn bộ dịch vụ phải tự tạo JobID |
| 4.5 Lệch pha giữa kỳ thanh toán và kỳ hạch toán | ➡ debt-management |  | kỳ ghi chi phí về muộn |
| 4.5.3 Ghi nhận doanh thu và chi phí | ➡ debt-management |  |  |
| 4.5.3.4 Trạng thái của JobID nghiệp vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 6.3 | |
| 4.6 Chi phí không hóa đơn | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E14<br>`docs/shipment-coordination/brainstorms/shipment-coordination.md` B20 | Quyết định giao Lệnh hằng tháng cho lái xe ➡ transport-dispatch (BL mới); định mức theo địa điểm ➡ location-catalog; Quyết định phân công công việc hằng tháng ➡ fund-payments |
| 4.7 Hàng đường sắt | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B9; `docs/transport-dispatch/brainstorms/transport-dispatch.md` D6, D7, E3 | khoá mục hải quan, nâng hạ ở ga; doanh thu đường sắt, J11 ở transport-dispatch |
| 4.8 Hàng CBT | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` D10, D11 | thủ tục cửa khẩu sau khi lập Lệnh ➡ transport-dispatch (BL mới); nguồn không có VAT 0% |
| 4.9.1 Thủ tục chuyên ngành | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B9, Mục 5.3 |  |
| 4.9.2 Thủ tục hải quan | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B9, E13, Mục 5.3 |  |
| 4.9.3 Kỳ lập báo cáo nội bộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` E18 | lệch kỳ báo cáo và kỳ thanh toán ➡ debt-management |
| 4.9.4 Nợ quá hạn | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B13, DP-01, OQ-67 | đổi Mục 6.3 từ "không duyệt ngoại lệ" sang có gia hạn đã duyệt (DEC-227) |
| 4.9.5 Hạn mức tín dụng | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` DP-01 | |
| 4.9.6 Chi phí dở dang | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` DP-01 |  |
| 4.10 Giải pháp phát hành hóa đơn | ✅ | `docs/invoice-management/brainstorms/invoice-management.md` C1, OQ-1 | lệch với SIM (SIM ghi QT 5.2, SOP ghi 5.4) |
| 5.1 Quy trình tạo JobID | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 5.1 bước 0, A11, B10, OQ-66<br>`docs/shipment-coordination/brainstorms/shipment-coordination.md` B15, B18 | danh mục lô hàng ở Điều phối A12; dashboard tổng là màn riêng |
| 5.2 Quy trình cung cấp dịch vụ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` Mục 5.1 bước 8, B12, E16, E17 |  |
| 5.3 Quy trình quản lý nợ phải trả | ➡ debt-management |  |  |
| 5.4 Quy trình quản lý nợ phải thu | ➡ debt-management |  |  |
| 5.5 Quy trình hạch toán nội bộ | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` B7 | |
| 6.1 Bảng thông tin JobID | ⏳ | | phụ lục trống, OQ-5 ở service-delivery |
| 6.2 Bảng kê doanh thu trên JobID | ⏳ | | OQ-5 |
| 6.3 Bảng kê chi phí trên JobID | ⏳ | | OQ-5 |
