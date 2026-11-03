# Soát nhóm parts (section 7271:387349, 11 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.3 part-adjust-dialog | Đã sửa | Thêm toast "Hoàn tất" góc phải dưới (ảnh có 1) | Nền phụ tùng chỉ đúng cấu trúc (đã biết) |
| 1.4 part-transfer-dialog | Đã sửa | Thêm 2 toast | Không |
| 1.5 inventory-activity-adjust-transfer | Đã sửa | Thêm 2 toast | Cột Người điều chỉnh, Ghi chú nằm ngoài khung ảnh, đang để "—" (giữ) |
| 1.6 parts-bulk-manage | Đã sửa | Thêm 2 toast (đồng bộ xe với Bộ lịch bảo dưỡng; khôi phục dữ liệu Lệnh sửa chữa #102) | Không |
| 2.4 po-receive-dialog | Đã sửa | Thêm 1 toast | Trạng thái đơn "Đã mua" là suy (đã biết) |
| 2.5 po-receive-existing-wo | Đã sửa | Thêm 2 toast | Trạng thái đơn "Đã mua" là suy (đã biết) |
| 2.6 po-edit-received-partial | Đã sửa | Thêm 2 toast; thêm badge số dòng "2" cạnh "Dòng hàng"; thêm ô nhập Phí vận chuyển "20000" cạnh 20.000 ₫ | Cột Thành tiền, Tạm tính, Chiết khấu, Thuế để "—" (ảnh bị toast che, ngoài khung) |
| 2.7 po-make-adjustment | Đã sửa | Thêm 1 toast | Không |
| 2.8 po-closed-partial | Đã sửa | Thêm 2 toast (tính toán tuân thủ; "Đơn mua #2 đã được đóng thành công"); thêm nút "Thêm" (…) trước "Sửa" | Dòng "Tạo 7 phút trước" dưới cùng nằm ngoài khung ảnh, giữ; nút avatar người phụ trách chưa vẽ; "Đơn mua #2" trong toast in đậm, ảnh là màu xanh |
| 3.3 fuel-history-capacity-alert | Đã sửa | Thêm nút "Thêm" cạnh Thêm Phiếu dầu; thêm icon cảnh báo bên trái Thể tích dòng 4.500 km | Icon cắt-vòng ở ô Số đồng hồ dòng 1 (50.000 km gạch) chưa vẽ; chip "Learn" bỏ theo quy ước; 2 dòng cuối bỏ (đã biết) |
| 3.4 fuel-entry-odometer-backdate-error | Khớp | Không | Hậu tố đơn vị "km" ở Số đồng hồ và "lít" ở Số lít chưa vẽ; link "Learn More" cuối mô tả Cờ chưa vẽ |

Giá trị, ngày giờ (am/pm sang 24h), nhãn, trạng thái, badge, checkbox/radio, dòng bảng đã đối chiếu đúng ảnh ở cả 11 màn. Radio/checkbox không lệch. Lỗi lặp lại: thiếu toast (10/11 màn).
Toast dựng bằng frame tuyệt đối góc phải dưới (460px, thanh xanh trái, icon circle-check, chữ type/label), tên layer "Thông báo hoàn tất". Không đụng Sidebar, Header, Menu bổ sung. Chưa chạy layoutAudit.
