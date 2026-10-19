# Sổ đối chiếu: Giải pháp PUR — Tự động ghép/tách cặp giữa mooc và đầu kéo/số container (SRC-29)

> Nguồn: `sop/vis-pur-ghep-tach-mooc/vis-pur-ghep-tach-mooc.md`
> Bản: 14/10/2026 (nhận 2026-10-15)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| 1. Vấn đề | ➡ transport-dispatch | | mooc hoán đổi liên tục giữa đầu kéo, nhập tay biển số mooc lên Lệnh không khả thi; truy vết lái xe khi mooc mất giấy tờ/bị phạt nguội; GPS mooc không cần hợp chuẩn + webhook EUP |
| 2. Nguyên lý kích hoạt biến cố ghép cặp (pairing event) | ➡ transport-dispatch | | 3 điều kiện đồng thời: cách ≤10 m, cùng ≥5 km/h, tích lũy >3 phút — ngưỡng thành tham số theo khách (mã P) |
| 3. Nguyên lý kích hoạt biến cố tách cặp (unpairing event) | ➡ transport-dispatch | | |
| 3.1. Biến cố tách cặp giữa Mooc và Đầu kéo (Trailer Unpairing) | ➡ transport-dispatch | | luồng chuẩn = ghép cặp với đầu kéo mới; mooc mồ côi = GPS mooc offline + đầu kéo cũ ≥5 km/h + xa >100 m (phân biệt tắt máy ngủ); liên quan F4, F5 |
| 3.2. Biến cố tách cặp giữa mooc và số container (Container Unpairing) | ➡ transport-dispatch | | gán mooc vào Lệnh mới thì tự giải phóng container của Lệnh cũ gần nhất; mooc mồ côi 2 điều kiện (offline + đầu kéo cũ đi ra ngoài 100 m) |
| 4. Quy trình gán dữ liệu tự động theo Lệnh vận tải | ➡ transport-dispatch | | quét Lệnh đang chạy của đầu kéo, rẽ nhánh Lệnh có/chưa có số container (sơ đồ) |
| 5. Quy trình áp dụng cho Lệnh vận tải có số container | ➡ transport-dispatch | | hàng nhập FCL, trả hàng đường sắt, CBT luôn có số container khi lập Lệnh; khóa khớp Đầu kéo ⇔ Mooc ⇔ Container |
| 6. Quy trình áp dụng cho Lệnh vận tải chưa có số container | ➡ transport-dispatch | | Bước 1–3: tự điền mooc vào Lệnh, ghi nhận lộ trình "đi tìm vỏ" (bãi phụ chỉ tính khi đỗ trong Geofence >10 phút), số container nhập từ App lái xe hoặc điều vận rồi gán cứng |
| Bước 4: Hạch toán nhiên liệu phát sinh thực tế | ➡ fuel-issuing | | km tìm vỏ + dầu bù theo định mức tải 0 kg, "Đề nghị cấp bù dầu do chọn container rỗng ở nhiều bãi" trên Lệnh, danh sách bãi đã qua, duyệt 2 bước điều vận + CBQL; PRD 7.12 xếp bù dầu vào fuel-issuing — phần hiển thị/duyệt trên Lệnh chốt ranh giới với transport-dispatch khi chia feature; ⚠ cách tính km (từ vào Geofence bãi chọn vỏ đến lúc nhập số container) lệch SRC-06 mục 3.3 (tổng km bãi gốc → nơi đóng hàng trừ km cung chuẩn) |
| (đoạn cuối, không số mục) Giá trị quản trị của vòng đời ghép/tách cặp | ➡ vehicle-management | | báo cáo vòng quay khai thác mooc (mooc đã ghép qua đầu kéo nào, chở container nào theo thời gian) cho khấu hao, lịch bảo dưỡng; dữ liệu thời gian sử dụng phương tiện đến từng phút |
