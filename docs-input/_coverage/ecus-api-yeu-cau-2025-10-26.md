# Sổ đối chiếu: Kết nối API giữa phần mềm Delta và phần mềm khai hải quan Ecus — Mô tả yêu cầu (SRC-10)

> Nguồn: `tich-hop/ecus-api-yeu-cau-2025-10-26/ecus-api-yeu-cau-2025-10-26.md`
> Bản: 26/10/2025 (nhận 2026-10-02)

Cả tài liệu vào `service-delivery` Nhóm H (DEC-215, thay DEC-214).

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1. Mục đích | ➖ | | bối cảnh: Delta là đại lý hải quan, khai thuê toàn quốc, khai tập trung tại Hà Nội, Hải Phòng, TP.HCM. ⚠ `service-delivery` OQ-17 ghi "không có chi nhánh Hải Phòng"; sơ đồ 1 ghi kho dữ liệu "VT" — có thể là Vận tải Delta (MST 0201280131, mã tỉnh Hải Phòng); đã thành `service-delivery` OQ-45 |
| 2.1. Viết tắt | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` H2 | Ecus Delta (dữ liệu riêng ở HN, HP, HCM), Ecus KH, EcusAuto |
| 2.2. Khách hàng của Delta | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` H2, OQ-46 | 137 khách khai thuê (đã ghi `docs/_shared/project-profile.md`); nhóm 1 khai trên Ecus Delta, nhóm 2 khai trên Ecus của khách |
| 2.3. Phạm vi kết nối API | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` H1 | tờ khai xuất, nhập, sửa AMA; không gồm nguyên phụ liệu, thanh khoản, kiểm tra sau thông quan |
| 3. Yêu cầu | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` H1 | màn khai tờ khai nháp trên phần mềm Delta, đính kèm Hợp đồng, Invoice, Packing List |
| 3.1. Nhóm khách hàng 1 | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` H2 (a), H3, H4, OQ-45 | đẩy nháp + chứng từ sang Ecus Delta; danh mục VNACCS/VCIS; nhận về số tiếp nhận chứng từ, trạng thái (đã truyền, phân luồng, thông báo thuế, thông quan), số + ngày tờ khai, mã vạch, đồng bộ sau khai chính thức; sơ đồ 1 đã chép chữ |
| 3.1 (dữ liệu nhận về bổ sung chứng từ JobID) | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` A10 | số tờ khai, ngày, phân luồng, mã vạch, chứng từ đính kèm vào bộ chứng từ JobID; tờ khai khách tự khai vẫn quét QR (`shipment-coordination` A2) |
| 3.2. Nhóm khách hàng 2 | ✅ | `docs/service-delivery/brainstorms/service-delivery.md` H2 (b), (c), H5, OQ-46 | Lựa chọn 1 EcusAuto trên máy chủ khách tự đẩy về Ecus Delta; Lựa chọn 2 xuất XML, nhân viên Delta đưa lên tay qua Ultraview (không nhận dữ liệu về); sơ đồ 2 đã chép chữ |
| 4. Liên hệ | ➖ | | đầu mối phía Delta (Nguyễn Việt Cường), không phải yêu cầu |
