# Soát location-1 (section 7261:348951, 17 màn)

| Màn | Kết quả | Đã sửa gì | Còn lệch gì |
|---|---|---|---|
| 1.2 fleet-map-nearby-list-2-vehicles | Đã sửa | Chip Địa điểm sáng (Hierarchy Primary); thêm toast "Hoàn tất: Đang tính toán..." góc phải dưới | Tên địa điểm tròn đọc là TEST-Cang-Cat-Lai theo spec (ảnh mờ, có thể đọc thành "TEST-XE-01-Lai") |
| 1.3 fleet-map-vehicle-panel | Đã sửa | Thêm 2 toast xếp chồng như ảnh | Thẻ "Thông tin" cuối panel ảnh bị cắt, giữ |
| 1.4 vehicle-nearby-places | Đã sửa | Chip Địa điểm sáng; thêm toast | Ảnh thumbnail địa điểm là ô xám (không có ảnh vệ tinh) |
| 1.5 nearby-hover-dashed | Đã sửa | Chip Địa điểm sáng; thêm toast | Marker xe vẽ chấm xanh, ảnh có biểu tượng xe |
| 1.6 fleet-map-legend | Đã sửa | Chip sáng; ẩn vùng đa giác + marker + nhãn TEST-Bai-Xe (ảnh không thấy); ẩn nhãn vòng tròn; dời/phóng vòng tròn về vị trí ảnh; thêm toast | Nội dung chú giải khớp; không đối chiếu từng đường phố |
| 1.7 fleet-map-options | Đã sửa | Chip sáng; ẩn Bai-Xe và nhãn vòng tròn; dời vòng tròn | Không còn |
| 1.8 fleet-map-satellite | Đã sửa | như 1.7 | Nền vệ tinh vẽ xám đơn giản (theo quy ước) |
| 1.9 fleet-map-grayscale | Đã sửa | như 1.7 | Không còn |
| 1.10 fleet-map-labels-polygon | Đã sửa | Chip Địa điểm sáng | Không còn |
| 1.11 zoomed-out-no-cluster | Đã sửa | Chip Địa điểm sáng | Không còn |
| 2.2 place-new-form | Đã sửa | Banner gợi ý: ẩn tiêu đề tự thêm và nút đóng (ảnh chỉ có 1 dòng, không có X) | Panel nút công cụ bản đồ chưa chỉnh (đã biết); thiếu liên kết "← Địa điểm" trên tiêu đề |
| 2.3 place-new-polygon | Đã sửa | Như 2.2; thêm pin thứ nhất nằm trên đa giác (trước bị đa giác che, ảnh có 2 pin) | Như 2.2 |
| 2.4 places-list-data | Khớp | — | Thiếu mũi tên sắp xếp cột Tên, nút trang trước/sau (chrome nhỏ) |
| 2.5 place-detail-circle | Đã sửa | Thêm toast "Đã tạo địa điểm thành công" | Thiếu liên kết "← Địa điểm" |
| 2.6 place-detail-with-entries | Khớp | — | — |
| 2.7 place-location-entries | Đã sửa | Thêm toast | — |
| 2.8 place-geofence-alert-policy | Khớp | — | Nút đóng viết "Đóng" thay biểu tượng X (chấp nhận) |

Ghi chú: xoá node bị chặn quyền, nên "bỏ" phần tử thừa bằng visible:false (khôi phục được). Menu Sidebar đang bị agent khác sửa nên không soát.
