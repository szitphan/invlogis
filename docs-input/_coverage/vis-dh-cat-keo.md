# Sổ đối chiếu: Giải pháp D&H — Tự động hóa Lệnh vận tải phụ cho mô hình cắt kéo container (SRC-28)

> Nguồn: `sop/vis-dh-cat-keo/vis-dh-cat-keo.md`
> Bản: 15/10/2026 (nhận 2026-10-15)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1. Đặt vấn đề | ➡ transport-dispatch | | luồng cắt kéo: lượt đi Lệnh X để mooc X tại nhà máy, lượt về kéo mooc Y theo Lệnh phụ của Lệnh Y; 4 trạng thái mooc (0 Sẵn sàng, 1 Đang trên đường, 2 Chờ kéo về, 3 Đang kéo về Cảng); trả lời một phần OQ-45 (hàng quay cắt); "một số khách hàng" dùng → hợp làm gói bật theo khách |
| 2. Nguyên lý kích hoạt biến cố ghép cặp cắt kéo (Hook event) | ➡ transport-dispatch | | ghép cặp trong Geofence nhà máy khách (danh mục), cùng 3 ngưỡng PUR (≤10 m, ≥5 km/h, >3 phút) |
| 3. Quy trình xử lý dữ liệu | ➡ transport-dispatch | | "1 hành động – 3 kết quả": chốt km lượt đi Lệnh X + cờ mooc X "Chờ kéo về"; tìm Lệnh gốc Y qua mooc có cờ; tự tạo Lệnh vận tải phụ trong Lệnh Y, gán cứng Đầu kéo A ⇒ Mooc Y ⇒ Container Y |
| 4. Hạch toán nhiên liệu phát sinh | ➡ transport-dispatch | | hàng/rỗng lấy từ Lệnh gốc; cung đường quy định để tính cầu đường, dầu, chi phí khác; km + nhiên liệu hạch toán riêng dưới Lệnh phụ, quản lý duyệt trên màn đối soát; tách khỏi luồng đi tìm vỏ J01; phần cấp dầu liên quan fuel-issuing |
| 5. Hiệu quả quản trị | ➖ | | nêu lợi ích, không có yêu cầu mới |
