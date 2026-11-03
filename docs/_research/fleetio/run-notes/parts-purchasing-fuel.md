# Chạy thử phụ tùng, kho, đơn mua, nhiên liệu, nhà cung cấp

Chạy 03/11/2026 trên tài khoản dùng thử, người dùng duy nhất Bảo Tín (có quyền duyệt). Cài đặt đang là Static Pricing, tắt tự đóng đơn, bật Track Inventory mặc định, bán kính cảnh báo dầu 2 miles; chỉ đọc, không đổi.

Mức: Chạy = tự thao tác thấy kết quả · Xem = thấy trên giao diện, không thao tác · Docs = theo SRS cũ từ tài liệu hãng · Không chạy = nêu lý do.

## Dữ liệu TEST đã tạo
- Xe TEST-KHO-01 (5891233), dung tích bình 60. Không tạo được TEST-KHO-02, xem case K1.
- Kho TEST-KHO-02 (TEST-KHO-01 có sẵn). NCC: TEST-KHO-NCC-01 (Parts, 14999735), -02 (Parts + Fuel, 14999737), -DAU (Fuel, 14999738).
- Phụ tùng TEST-KHO-PT-A (9424431), TEST-KHO-PT-B (9424568). PO #2 (Closed), #3 (Received, Full). WO #102 (Open, còn dòng PT-B số lượng 3). 14 phiếu dầu TEST-KHO-F1 đến F14 trên xe TEST-KHO-01.
- Có một xác nhận xoá: dòng PT-A trong WO #102, hộp "Are you sure you want to permanently delete this line item?". Không xoá lệnh (K21).

## Tồn kho theo kho — Chạy
Các bước đã làm: tạo phụ tùng bật 2 kho, chỉnh tăng giảm, chuyển kho, xuất cho lệnh, nhập từ đơn, sửa hàng loạt; đọc sổ kho sau mỗi bước.
Kết quả thấy được: mỗi kho một thẻ gồm Current Qty, Reorder Point, Pending PO Qty, WO Current Qty; 4 nút chỉnh, chuyển, đặt mua, menu (Edit, View History). Sổ kho có loại Initial, Manual, Transfer, Purchase Order, Work Order, Bulk Update.

### Ma trận trạng thái tồn (theo từng kho)
| Trạng thái | Điều kiện đo được | Nút khác biệt | Sang trạng thái | Câu chữ | Mức |
|---|---|---|---|---|---|
| Không nhãn | Tồn > điểm đặt lại (6 và 6,5 với điểm 5) | Đủ nút | Low Stock khi tồn <= điểm; Out of Stock khi <= 0 | — | Chạy |
| Low Stock | 0 < tồn <= điểm (3 và đúng bằng 5 với điểm 5) | Đủ nút, số màu cam | Không nhãn khi vượt điểm; Out khi <= 0 | "Low Stock" | Chạy |
| Out of Stock | Tồn <= 0 (0 và -10) | Nút chuyển kho khoá | Low Stock khi 0 + 5; không nhãn khi vượt điểm | "Out of Stock" | Chạy |
| Điểm đặt lại = 0 | Lưu được dù tài liệu nói phải > 0; tồn 9,5 không nhãn | Đủ nút | Chưa thử về 0 với điểm 0 | "Part was successfully updated" | Chạy |

### Bảng case kho
| # | Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|---|
| K1 | Thêm xe | Thanh "5 of 5" trên Vehicles | Save Vehicle quay mãi, không báo lỗi, xe không được tạo; lần trước đó tạo được. Suy: giới hạn 5 xe | — |
| K2 | Trùng tên kho | TEST-KHO-01 lần 2 | "has already been taken", "Part Location could not be created" | — |
| K3 | Chỉnh giảm quá tồn | 10, chỉnh -20, lý do Lost | Lưu được, tồn -10, không cảnh báo | part-adjust-dialog |
| K4 | Chỉnh bằng số mới | Gõ New Quantity 0 | Adjust Quantity tự thành 10; hai ô liên động | — |
| K5 | Số lẻ | +0,5 | Tồn 6,5, chấp nhận | — |
| K6 | Lý do | Bắt buộc, Save khoá khi trống | 11 lý do: Broken, Checked Inventory, Expired, Found, Lost, Miscellaneous, Received, Sold, Stolen, Transferred, Used | — |
| K7 | Chuyển quá tồn | Có 6,5, chuyển 100, nút Save vẫn mở | "Parts transfer was successful."; chỉ chuyển 6,5, sổ ghi -6,5 và +6,5, không báo đã cắt số | part-transfer-dialog |
| K8 | Chuyển khi tồn 0 | Tồn <= 0 | Nút chuyển khoá | — |
| K9 | Danh sách kho đích | 2 kho | Chỉ hiện kho còn lại kèm tồn | — |
| K10 | Trừ kho khi lưu lệnh | PT-B 5 cái, WO Open | -5 ngay lúc lưu | — |
| K11 | Sửa số lượng dòng | 5 thành 3 | Sổ +2, loại Work Order #102 | — |
| K12 | Xuất quá tồn | PT-A 20, kho 9,5 | Không cảnh báo ở hộp Add Part, tồn -10,5. Hộp chỉ ghi "This will make an inventory adjustment" | — |
| K13 | Không trừ kho | Part Location | Có lựa chọn "None (No Inventory Adjustment)" | — |
| K14 | Hoàn thành lệnh | Open sang Completed | Sổ không có dòng mới; sinh Service Entry #57857777; Edit khoá. Cần Started At và Start Odometer: "Please edit and fix the following errors: Started At can't be blank", "Start Odometer can't be blank (per your account settings)" | — |
| K15 | Mở lại lệnh | Completed sang Open | "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items."; sổ không đổi; liên kết Service Entry biến mất | — |
| K16 | Xoá dòng sau khi mở lại | Xoá PT-A 20 | Sổ +20, tồn về 9,5 | — |
| K17 | Giá khi nhập nhiều giá | Static: danh mục 100.000, đơn 90.000 | Unit Cost phụ tùng giữ 100.000; Total Inventory Value 13.750.000 = 131,5 x 100.000 + 2 x 300.000. FIFO, LIFO, Average không thử vì không đổi cài đặt | — |
| K18 | Phụ tùng không có giá | PT-B | Giá trị tồn tính 0. Giá gõ lúc tạo không được lưu, chưa rõ vì sao | — |
| K19 | Bulk Manage | Tab theo kho; sửa ô là tự lưu | "All changes saved"; -1 thành 8, sổ loại Bulk Update +9, không hỏi lý do | parts-bulk-manage |
| K20 | Tắt kho khi có đơn | Gạt Active ở Bulk | Không tắt: "This part can't be deactivated because it's used in one or more purchase orders at this location." | — |
| K21 | Xoá cả lệnh | Hộp "All data will be lost forever." | Không chạy: đã huỷ ở hộp xác nhận vì là xoá vĩnh viễn. Xoá lệnh có hoàn kho không vẫn chưa biết | — |
| K22 | Nhiều nhà cung cấp | Thêm NCC-02 giá 110.000 trong Purchase History | Lưu được, trang phụ tùng vẽ biểu đồ giá 90.000 đến 110.000; đơn tự thêm dòng lịch sử | — |
| K23 | Thay thế, tương thích xe | Form phụ tùng | Không thấy trường nào; chỉ có Replaced Parts trong bảo hành ở lệnh. Mức Xem, chưa tìm ở nơi khác | — |

Luồng nghiệp vụ kho: khai kho ở Settings → bật phụ tùng tại kho, nhập tồn đầu (ghi Initial) → nhập qua đơn hoặc chỉnh tay có lý do → xuất khi lưu dòng lệnh (trừ ngay, không chờ hoàn thành) → sửa hoặc xoá dòng thì sổ ghi bù → Bulk để kiểm kê.

## Đơn mua — Chạy, trừ nhánh duyệt
Các bước đã làm: PO #2 đi hết Draft, Approved, về Draft, Approved, Purchased, Partial, Full, về Partial, Closed. PO #3 copy, duyệt, Purchased, Unmark, Purchased, nhận vào lệnh mới.

### Ma trận trạng thái đơn
| Trạng thái | Hành động làm được | Sang | Điều kiện, người | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Draft | Sửa mọi thứ, Approve, Save & Approve, Print, Make a Copy, View Record History, Delete | Approved | Approve khoá khi 0 dòng; lưu 0 dòng được | Không tính Pending khi chưa duyệt: chưa đo riêng | "Purchase Order #2 approved" | Chạy |
| Pending Approval | — | — | Một người dùng có quyền duyệt không thấy Submit for Approval | — | Tab lọc có | Docs, không chạy được |
| Rejected | — | — | Như trên; gửi lại sau từ chối vẫn chưa biết | — | Tab lọc có | Docs, không chạy được |
| Approved | Mark as Purchased, Edit (đủ trường), Save as Draft, Save & Approve, Copy, Delete | Purchased, Draft | Save as Draft lùi về Draft, mất dòng Approved By | Pending PO Qty = 12 | "marked as purchased" | Chạy |
| Purchased | Receive, Unmark as Purchased, Edit, Copy, Delete | Partial, Full, Approved | Một cú bấm, không hỏi | Pending vẫn 12 | "unmarked as purchased" | Chạy |
| Received, Partial | Receive, Close, Edit (khoá NCC, kho, không thêm bớt dòng; sửa số và giá được), Copy, Delete | Full, Closed | Không có Make Adjustment | Tồn tăng từng lần | "was successfully received" | Chạy |
| Received, Full | Close, Make Adjustment, Edit, Copy, Delete | Closed, Partial | Lùi về Partial khi điều chỉnh giảm | Tự đóng tắt nên cần Close tay | "was successfully adjusted" | Chạy |
| Closed | Make Adjustment, Edit, Copy, Delete | Không có nút mở lại | Edit vẫn đổi được đơn giá, tổng tính lại | 1.429.400 thành 1.312.760 | "was successfully closed", "was successfully updated" | Chạy |

Không có trạng thái hay nút huỷ riêng; thoát đơn chỉ có Close (từ Partial, Full) hoặc Delete. Delete không bấm.

### Bảng case đơn
| # | Case | Kết quả thật | Ảnh |
|---|---|---|---|
| D1 | Chọn NCC | Chỉ hiện NCC có Parts; NCC-DAU (Fuel) không có | — |
| D2 | Tìm phụ tùng | Hiện tồn tại kho của đơn; PT-B không bật ở KHO-02 thì xám, có khoá | — |
| D3 | Một đơn nhiều kho | Không được: Part Location một giá trị cho cả đơn, khoá sau khi nhận | — |
| D4 | Dòng trùng | "Part TEST-KHO-PT-A is duplicated", "Purchase Order could not be created" | — |
| D5 | Dòng số lượng 0 | Duyệt được, không chặn | — |
| D6 | Thuế, phí, giảm | 1.250.000, giảm 10% -125.000, Shipping 20.000, thuế 8% 90.000, tổng 1.235.000: thuế tính trên sau giảm, không gồm phí | — |
| D7 | Lỗi ô Shipping | Gõ 20000 thành 2.000.000; gõ 200 mới ra 20.000. Ô Unit Cost của dòng thì đúng | — |
| D8 | Nhận thiếu | 5/12: Partial, lần sau gợi ý 7 | po-receive-dialog |
| D9 | Nhận vượt | Gõ 100 thành 105/12, sau đó 110/12: không chặn, không cảnh báo; tồn tăng đủ; tiền đơn vẫn theo số đặt | — |
| D10 | Vượt ở một dòng, dòng khác 0 | Vẫn Partial | — |
| D11 | Trả hàng ở Receive | Gõ -5 thành nhận +5, mất dấu âm, không báo | — |
| D12 | Trả hàng bằng Make Adjustment | "Negative values are allowed up to the quantity received on this order."; -6 trên 5 nhận được cắt còn -5, không báo; sổ -5, tồn 2 thành -3, về Partial; "Received in Full By" vẫn còn | po-make-adjustment |
| D13 | Đóng khi nhận thiếu | "Are you sure you want to close the selected purchase order?"; đóng được, PT-B 0/5, không ghi lý do | po-closed-partial |
| D14 | Nhận vào lệnh có sẵn | "These parts will be received to your inventory before being added to the selected work order."; mở form lệnh với dòng ghi chú "From PO #2"; sổ +5 trước, -5 khi lưu lệnh | po-receive-existing-wo |
| D15 | Nhận vào lệnh mới, huỷ form | "Your received parts will remain in inventory even if you don't save this work order."; hàng ở lại kho, đơn thành Full, không có lệnh | — |
| D16 | Copy | Mở form mới điền sẵn, giữ giá đơn cũ, số tăng lên #3 | — |
| D17 | Duyệt đơn của mình | Được, một cú bấm, không hộp xác nhận. Không kiểm được tách người vì tài khoản 1 người, không mời người ngoài | — |

Luồng nghiệp vụ đơn: lập đơn cho 1 NCC + 1 kho → duyệt → Mark as Purchased → nhận một hoặc nhiều lần vào kho hoặc lệnh → Make Adjustment nếu trả → Close.

## Dầu — Chạy
Các bước đã làm: 14 phiếu trên TEST-KHO-01 (bình 60), đọc từng phiếu và Fuel History.

### Bảng case dầu
| # | Case | Điều kiện | Kết quả thật | Ảnh |
|---|---|---|---|---|
| F1 | Phiếu đầu | 2.000 km, 50 lít, 20.000 ₫ | Usage "N/A", không tiêu hao; tổng 1.000.000 | — |
| F2 | Đầy tiếp | 500 km, 40 lít | 29,40 mpg (US) = 12,5 km/lít đúng, nhưng xe km, lít vẫn hiện mpg | — |
| F3, F4 | Không đầy rồi đầy | 2.700 (10 lít, partial), 3.000 (20 lít) | F3 không có tiêu hao; F4 39,20 mpg = 500 km / 30 lít: cộng dồn phiếu partial. Đúng | — |
| F5, F6 | Bỏ lần | 3.500 Reset usage, 3.800 | F5 không usage; F6 Usage "N/A" nhưng vẫn có 35,28 mpg = 300 km / 20 lít | — |
| F7 | Personal | 10 lít | Tính tiêu hao bình thường; vẫn cộng vào Cost of Ownership | — |
| F8 | Số đồng hồ lùi cùng ngày | 2.900 khi đã có 4.000 | Lưu được, không báo; lấy phiếu trước theo số đồng hồ (2.700), Usage 200. F4 vẫn hiện 300 | — |
| F9 | Vượt bình | 100 lít, bình 60 | Có cảnh báo: icon Alerts, Capacity Exception Volume "100 liters". Khác SRS FR-022 | fuel-history-capacity-alert |
| F9b | Sửa phiếu vượt | 100 thành 50 lít | Cảnh báo không mất, cột vẫn 100 | — |
| F13, F14 | Biên bình | 60 lít; 60,5 lít | Bằng bình không cảnh báo; 60,5 có cảnh báo | — |
| F1b | Chưa khai dung tích | 50 lít | Không kiểm | — |
| F11 | 0 lít | 4.800 km | Lưu được, tổng 0 ₫ | — |
| F10 | Void | Tick Void, trống số | "can't be blank"; ghi 50.000 thì lưu, số gạch ngang, đồng hồ xe vẫn 4.800, không Usage | — |
| F12 | Lùi ngày, số cao | 20/10, 9.000 km | "must be less than 1,000 or marked as void" | fuel-entry-odometer-backdate-error |
| F12b | Lùi ngày, số thấp | 20/10, 900 km | Lưu được, không đổi phiếu sau | — |
| — | NCC trên phiếu | Chọn | Chỉ NCC có Fuel: NCC-02, NCC-DAU; NCC-01 không có. Phiếu có NCC-DAU hiện bản đồ, phiếu không NCC ghi "Location is unknown or not available" | — |
| — | Bộ lọc | Date, Vehicle, Vehicle Group, Vendor, Filters | Mở bộ lọc theo xe, có Add Filter, Add Filter Group; chỉ thử lọc xe | — |
| — | Thẻ dầu | Fuel Card trên phiếu | Ô "No"; cài đặt WEX chỉ đọc; không có màn gán thẻ thử được. Không tích hợp | — |
| — | Vendor Location Alert | Cần định vị và thẻ | Không chạy: cần tích hợp | — |
| — | Charging History | — | Điều phối viên bỏ khỏi phạm vi, không xem | — |

### Lỗi tiền trên VND (đã lặp lại)
| Nơi | Giá trị đúng | Hiện |
|---|---|---|
| Chi tiết WO, dòng PT-B | 50.000 (form sửa) | 5.000.000 |
| Chi tiết WO, tổng; Service Entry | 2.550.000 | 255.000.000 |
| Fuel History, Total Fuel Cost | 8.010.000 cộng theo dòng | 80.100 |
| Fuel, Cost per km | 1.600 | 16 ₫ |
| Fuel History, Avg. Cost | Suy khoảng 75.700 ₫/gallon | 757 ₫ |
Trang chi tiết xe đúng: Fuel & Energy Costs 7.610.000, 1.770 ₫/km, tính cả Personal, Void; không tính phiếu 20/10 vì thẻ "This Month".
Lưu ý: ở hộp Add Part gõ 120000 thì form ra đúng; lệch xuất hiện ở trang chi tiết, Service Entry theo con số sai. Bấm lưu form không đổi gì thì số trên chi tiết không tăng thêm, nhưng trang vẫn đứng ở form nên chưa chắc lần lưu đó đã chạy.

Luồng nghiệp vụ dầu: chọn xe → ngày, số đồng hồ → số lít, đơn giá → loại dầu, NCC, tham chiếu → cờ Personal, Partial, Reset → lưu → hệ thống tính tiêu hao, chi phí km, so với lần trước, gắn Capacity Alert → cộng vào chi phí xe.

## Nhà cung cấp — Chạy, Tìm xưởng không mở
Tên, Address, City, State, Zip, Country đều bắt buộc: "can't be blank". Phân loại không bắt buộc, quyết định nơi được chọn (D1, F). Tab Overview, Fuel Entries, Purchase Orders; NCC-DAU chỉ Fuel thì không có tab Purchase Orders, NCC-02 có cả hai. Tab đơn của NCC-01 liệt kê #3 và #2. Trang có "Network Status: Invite": không bấm. "Find Shops" có nút Add Vendors: thấy, không mở. Enter trong ô Country vừa chọn vừa lưu form luôn, ba lần đều vậy. Bất ngờ này dễ tạo bản ghi sớm.

## Màn mới
- part-adjust-dialog: images/part-adjust-dialog.jpg: Location (khoá), Adjust Quantity, New Quantity, Reason, Comment.
- part-transfer-dialog: images/part-transfer-dialog.jpg: Current Location, Current Quantity, Quantity to Transfer, New Location.
- inventory-activity-adjust-transfer: images/inventory-activity-adjust-transfer.jpg: sổ kho đủ loại.
- po-receive-dialog, po-receive-existing-wo: Item, Total Received, Total Ordered, Receive; nơi đến Inventory, Existing work order, New work order.
- po-edit-received-partial: NCC, kho khoá; không có Add Line Item.
- po-make-adjustment: Item, Total Received, Total Ordered, Adjustment.
- po-closed-partial: Closed By, Received in Full By còn dấu.
- parts-bulk-manage: tab theo kho; Aisle, Row, Bin, Active?, Track Inventory, Current Qty, Last Quantity Update, Print Worksheet.
- fuel-history-capacity-alert: Alerts, Capacity Exception Volume, Location Exception Distance.
- fuel-entry-odometer-backdate-error: lỗi số đồng hồ.

## Trả lời câu hỏi mở
- parts-purchasing-fuel OQ-6: Không có nút huỷ sau Approved, chỉ Delete hoặc lùi Draft. Đóng được khi nhận thiếu. Nhận vượt được. Trả hàng qua Make Adjustment, ở Full và Closed. Gửi lại đơn Rejected: chưa trả lời được, tài khoản 1 người.
- OQ-7: Xoá dòng hoàn kho (K16). Xoá lệnh: chưa thử.
- FR-022 sai: nhập tay có Capacity Alert khi đã khai dung tích. BR-007 sai với thực tế: điểm đặt lại 0 lưu được. BR-006: dưới Static Pricing Closed vẫn sửa được giá.
- Đơn giá nhận thẳng vào lệnh (FR-013): chạy được dưới Static; phương pháp khác chưa thử.

## Giải pháp đáng học, điểm yếu
- Học: thẻ tồn 4 số theo từng kho cho xưởng biết hàng đang về và đã xuất cho lệnh. Hợp với nhiều bãi đầu kéo, mooc.
- Học: sổ kho ghi số trước, số sau, chứng từ cho mọi biến động, kể cả sửa và xoá dòng lệnh. Dễ đối soát khi kiểm kê.
- Học: nhận thẳng vào lệnh đi qua kho hai bước; hàng không mất khi huỷ form. Hợp phụ tùng đặt riêng cho xe nằm xưởng.
- Học: gộp phiếu không đầy khi tính tiêu hao, Reset khi thiếu phiếu. Hợp đầu kéo đổ nhiều cây dầu dọc đường.
- Học: Capacity Alert chỉ cần dung tích bình, không cần tích hợp; với đầu kéo cần khai đúng tổng bình.
- Yếu: tồn âm, chuyển kho, nhận vượt, trả quá số đều không chặn, có chỗ còn cắt số hoặc mất dấu âm mà vẫn báo thành công. Với Invlogis phải báo rõ.
- Yếu: tiền VND lệch 100 lần ở chi tiết lệnh, Service Entry, báo cáo dầu; làm sai chi phí sửa chữa theo xe.
- Yếu: đơn Closed vẫn sửa được giá, không mở lại, không có lý do đóng thiếu; cảnh báo dầu không xoá khi sửa phiếu; số đồng hồ lùi cùng ngày không chặn.

## Chưa làm
Pending Approval, Rejected; xoá lệnh; Delete đơn; FIFO, LIFO, Average; đổi vị trí dòng lệnh sang None; Pending khi Draft; Vendor Location Alert; Find Shops; TEST-KHO-02 xe. Tác nghiệp thực hiện song song khi nhóm tab bị đóng 3 lần; zoom trang đổi 75% do tab khác.

# Lượt 3 (03/11)

Gói xe đã 5/5, không tạo xe mới. Dùng lại kho, NCC, phụ tùng TEST-KHO có sẵn. Không đụng TEST-SUA-01.

## Make Adjustment từ đơn Closed — Chạy
Các bước đã làm: PO #2 (Closed) mở menu, "Make Adjustment", tick TEST-KHO-PT-A, nhập -1, bấm "Make Adjustment".
Kết quả thấy được: "Purchase Order #2 was successfully adjusted". Qty Received 110 xuống 109. Trạng thái **vẫn Closed** (khác từ Full: về Partial). Sổ kho phụ tùng ghi "Received: -1.0", chứng từ Purchase Order #2. Tồn TEST-KHO-01 còn 121.
Bất ngờ: đơn đã đóng vẫn đổi được số nhận và tồn kho mà không mở lại đơn, không hỏi lý do. Hộp thoại: "Check the box to make an Adjustment. Negative values are allowed up to the quantity received on this order."
Màn mới: po-adjust-closed — ảnh images/po-adjust-closed.jpg — bảng Item, Total Received, Total Ordered, Adjustment; ô tick từng dòng; nút Close, Make Adjustment (mờ tới khi tick).
Trả lời câu hỏi mở: FR-028 phần "từ Closed" đã chạy.

## Lịch sử bản ghi đơn — Chạy
Các bước đã làm: PO #2, menu, "View Record History".
Kết quả thấy được: hộp "Record History", ô "Select Date Range", cột Date, Changes By, Changes Made. Ghi từng chuyển trạng thái ("State changed from Received Partial to Closed", "Received Full to Received Partial", "Approved to Draft") và đổi tiền ("Tax 1 changed from ... to ...", "Discount", "Subtotal", "Total Amount").
Màn mới: po-record-history — ảnh images/po-record-history.jpg.

## Make a Copy — Chạy (chức năng chưa có trong function list)
Các bước đã làm: PO #2 Closed, menu, "Make a Copy", "Save as Draft".
Kết quả thấy được: form "New Purchase Order" số 4, chép NCC, kho, 2 dòng, số đặt 12 và 5, giá, chiết khấu. Không chép số đã nhận. Lưu: "Purchase Order was successfully created", PO #4 Draft. Có ở cả Closed và Purchased.

## Pending PO Qty theo trạng thái — Chạy
Các bước đã làm: PO #4 của TEST-KHO-PT-A kho TEST-KHO-01, đọc thẻ tồn sau mỗi bước.
| Trạng thái PO #4 | Pending PO Qty | Current Qty |
|---|---|---|
| Draft (12) | 0 | 121 |
| Approved (12) | 0 | 121 |
| Purchased (12) | 12 | 121 |
| Purchased, sửa số đặt thành 15 | 15 | 121 |
Trả lời câu hỏi mở: parts-purchasing-fuel OQ-13: Draft và cả Approved không tính; chỉ tính từ Purchased.

## Sửa đơn ở Purchased — Chạy
Các bước đã làm: PO #4 Purchased, Edit, đổi số PT-A 12 thành 15, "Save Purchase Order".
Kết quả thấy được: Vendor và Part Location bị khoá (xám). Không có "Add Line Item", không có nút xoá dòng. Sửa được Label, số, giá, Description, Discount, Shipping, Tax. Lưu được, không cảnh báo đã gửi nhà cung cấp.
Menu ở Purchased: "Receive", "Unmark as Purchased", "Print", "Make a Copy", "View Record History", "Delete".
Màn mới: po-edit-purchased — ảnh images/po-edit-purchased.jpg.
Dữ liệu TEST đã tạo: PO #4 (TEST-KHO-NCC-01, kho TEST-KHO-01).

## Lùi trạng thái đơn: Unmark as Purchased — Chạy
Các bước đã làm: PO #4 Purchased, menu, "Unmark as Purchased". Mở lại thẻ tồn PT-A và PT-B.
Kết quả thấy được: "Purchase Order #4 unmarked as purchased", đơn về Approved. **Pending PO Qty của PT-A vẫn 15, PT-B vẫn 5** sau khi tải lại trang, dù đơn không còn Purchased.
Bất ngờ: số hàng đang về bị thừa sau khi lùi trạng thái (ngược quy tắc Approved = 0 đo ở trên).
Đi tiếp: Edit ở Approved, "Save as Draft": "Purchase Order was successfully updated", về Draft, dòng Approved By mất. Pending vẫn 15. Approve rồi "Mark as Purchased" lại: Pending vẫn 15, không nhân đôi. Suy (chưa kiểm được công thức): số đã từng vào Pending không bị trừ khi lùi trạng thái; chỉ đo được ở PO #4.
Trạng thái cuối PO #4: Purchased, số đặt 15 và 5, chưa nhận.

## Sửa đơn ở Draft và Received Full — Xem form, không lưu
Draft: Vendor, Part Location mở; có "Add Line Item", nút xoá dòng; có "Save as Draft", "Save & Approve". Received Full (PO #3): Vendor, Part Location khoá; không thêm bớt dòng; ô số và giá mở; nút "Save Purchase Order". Không lưu.
Trả lời FR-030: đã đi đủ Draft, Approved, Purchased, Full; Partial, Closed có từ lượt trước.

## Pending Approval, Rejected — Không chạy được: cần người thứ hai không có quyền duyệt, mà mời người ngoài bị cấm. Giữ OQ-8, OQ-20.
Menu ở Approved: "Mark as Purchased", "Print", "Make a Copy", "View Record History", "Delete". Không có mục lùi về Draft trong menu; Edit ở Approved có "Save as Draft" và "Save & Approve", đủ trường, thêm bớt dòng được.

## In đơn — Chạy
Các bước đã làm: PO #4 Approved, menu, "Print".
Kết quả thấy được: mở tab mới "Preparing your PDF...", ra `purchase_order_4.pdf`, 1 trang: Number, Status, Vendor, Part Location, Created Date, Created By, Approval Date, Approved By, Purchase Date, Purchased By, Closed Date, Closed By; dòng hàng; Subtotal, Discount, Shipping, Tax, Total; Description. Đầu trang in tên và địa chỉ tài khoản.
Bất ngờ: PO Approved sau Unmark vẫn in Purchase Date và Purchased By (dữ liệu không bị xoá khi lùi). Số tiền in kiểu US (₫1,575,200) khác dạng trên web (1.575.200 ₫).
Màn mới: po-print-pdf — ảnh images/po-print-pdf.jpg (đã che dòng địa chỉ tài khoản).

## Biên tồn khi điểm đặt lại bằng 0 — Chạy
Các bước đã làm: PT-A kho TEST-KHO-02 (Reorder Point 0), sửa tồn ở Bulk Manage: 9,5 thành 0, rồi 0,5, rồi trả về 9,5.
| Tồn | Điểm đặt lại | Nhãn thẻ kho | Ô đếm danh sách |
|---|---|---|---|
| 0 | 0 | "Out of Stock" | Out of Stock 1, Low Stock 0 |
| 0,5 | 0 | Không nhãn | — |
| 9,5 | 0 | Không nhãn | — |
Sổ kho ghi "Adjustment: 9.5 → 0.0", chứng từ Bulk Update, không hỏi lý do. Danh sách Parts tô đỏ số Total Quantity 121 của PT-A khi một kho hết hàng, dù tổng còn nhiều.
Trả lời câu hỏi mở: parts-purchasing-fuel OQ-17: Out of Stock thắng, Low Stock không hiện. Email cảnh báo tồn thấp: không chạy, không gửi email theo ràng buộc; giữ Docs.

## Danh mục phụ tùng: thay thế, tương thích — Chạy phần form
Các bước đã làm: mở form New Part (không lưu), đọc cột danh sách Parts, menu trang phụ tùng.
Kết quả thấy được: form có Part Number, Description, Photo, Document, Category, Manufacturer, Manufacturer Part #, UPC, Unit Cost, Measurement Unit, Warranty, Locations, Purchase History. Không có trường thay thế hay tương thích xe. Danh sách có cột "Linked Service Tasks": nơi duy nhất nối phụ tùng với việc khác. Menu phụ tùng: "Update Quantity", "Archive" (mờ với PT-A), "View Record History".
Trả lời câu hỏi mở: OQ-19: không có trong form, danh sách, menu phụ tùng. Chưa rà trang Linked Service Tasks.

## Print Worksheet — Chạy
Các bước đã làm: Bulk Manage Parts, "Print Worksheet", 1 cú bấm.
Kết quả thấy được: toast "Complete: Bulk Manage Parts Worksheet", "Click here if download doesn't start". Không mở tab; **tự tải PDF về máy**, 3 bản giống hệt `bulk_manage_parts_2026_11_03*.pdf` (39 KB) trong Downloads.
Bất ngờ: một cú bấm ra 3 file. Không xoá, để user tự xử lý.

PDF 1 trang: tên, địa chỉ tài khoản, rồi Part, Category, Manufacturer, Aisle, Row, Bin, Current Qty kèm mốc ("Yesterday", "Today"), ô trống New Qty để kiểm đếm tay. In theo kho đang chọn. Ảnh không lưu vì có địa chỉ tài khoản.

## Tính giá tồn FIFO, LIFO, Average — Không chạy được: đổi Cài đặt cấp tài khoản, bị cấm. Giữ OQ-11.

## Bộ lọc phiếu dầu — Chạy
Các bước đã làm: Fuel History, lọc Vendor, mở Filters, Add Filter, chọn Fuel Alert Type, xoá điều kiện, lọc Personal, lọc theo xe.
Kết quả thấy được:
- Mặc định Date 30 ngày gần nhất, là điều kiện có biểu tượng khoá trong panel. Panel: "You can create up to 3 "OR" filter types. To add more filters, use "AND" within the filter builder."
- Vendor chọn nhiều, liệt kê **mọi** NCC kể cả NCC không có phân loại Fuel (khác form phiếu chỉ cho NCC Fuel). Lọc TEST-KHO-NCC-DAU: 1 phiếu, thẻ tổng tính lại.
- Trường lọc: Date, Fuel Alert Type, Fuel Transaction, Fuel Type, Partial, Personal, Reference, Reset, Transaction Card Number, Transaction Driver ID, Transaction Driver Name, Transaction Vehicle ID, Vendor, Void Status; 24 trường Vehicle; 6 trường Vendor.
- **Fuel Alert Type có đúng 3 giá trị: "Vendor Location Alert", "Fuel Capacity Alert", "Missing GPS Location Alert".** Lọc Fuel Capacity Alert ra 2 phiếu 60,5 lít và 50 lít (phiếu 50 lít là phiếu sửa từ 100, xác nhận F9b cảnh báo không mất).
- Personal: đúng 1 phiếu 10 lít. Xoá một điều kiện thì danh sách áp ngay; thêm điều kiện phải bấm Apply.
Màn mới: fuel-filter-alert-type — ảnh images/fuel-filter-alert-type.jpg.

## Cờ Void, Personal trong thẻ tổng — Chạy
Các bước đã làm: lọc xe TEST-KHO-01, cộng tay 14 phiếu rồi so với thẻ tổng.
Kết quả thấy được: tổng tay 400,5 lít = 105,80 gallons, khớp "Total Volume" 105.80. Phiếu Void 20 lít, số đồng hồ gạch ngang, **vẫn được cộng vào Total Volume và Total Fuel Cost**; bỏ Void chỉ còn 100,5 gallons. Phiếu Personal cũng cộng. Tổng tiền hiện 80.100 ₫ trong khi cộng tay là 8.010.000 ₫: lỗi lệch 100 lần trên VND, lại ở thẻ tổng này.
Bất ngờ: Void không loại khỏi thống kê, nên không dùng được làm "huỷ phiếu" mà chỉ là "bỏ qua đồng hồ".

## Cảnh báo sai vị trí trên phiếu dầu — Không chạy được: cần tích hợp thẻ, định vị. Chỉ thấy tên loại ở bộ lọc. Giữ OQ-14.

## Nhà cung cấp: Find Shops, Network Status — Một phần
Các bước đã làm: Vendors, "Find Shops", gõ thành phố công khai (Atlanta, không phải vị trí thật), "Let's Go", tick 1 dòng để xem, không bấm thêm. Đọc form Edit Vendor, không lưu.
Kết quả thấy được: mở hộp "Select service shops and easily save them to your vendors list", ô "Enter address, city or ZIP/postal code", ô "Shop type". Kết quả khoảng 30 cửa hàng thật kèm bản đồ, chữ "All Results"; tick thì hiện "SELECTED", "Clear selection", ghim đổi đỏ, nhãn khoảng cách, có nút "Add Vendor". Không bấm Add Vendor vì sẽ tạo NCC trùng tên doanh nghiệp thật không tiền tố TEST; đã huỷ. Ảnh không lưu vì có địa chỉ thật.
Danh sách Vendors có cột Rating, Labels, Archived At; tab Charging, Fuel, Parts, Service, Vehicle, Archived. Trang chi tiết có thêm "Tools Vendor". Cột Rating mọi NCC TEST hiện "...", rê chuột: "Rating not available". Form Edit Vendor không thấy chỗ nhập điểm ở phần đọc được; suy ra điểm không do người dùng nhập, nguồn chưa rõ.
"Network Status: Invite": không bấm vì mời người ngoài. Giữ một nửa OQ-15.

## Thẻ dầu trên phiếu — Xem
Không có màn gán thẻ không cần tích hợp. Bộ lọc có Transaction Card Number, Transaction Driver ID, Transaction Driver Name, Transaction Vehicle ID: dữ liệu thẻ gắn ở mức phiếu. Không kết nối WEX (cấm tích hợp).

## Phiếu dầu tạo vị trí xe — Chạy (phát hiện sửa FR-004 nhóm Vị trí; chi tiết ở location-dispatch.md Lượt 3)
Dữ liệu TEST đã tạo: Fuel Entry #229944275 trên TEST-DAUKEO-2 (100 km, 5 lít, 20.000 ₫, TEST-KHO-NCC-02).

## Trả lời câu hỏi mở Lượt 3
OQ-13 xong, OQ-17 xong, OQ-19 xong phần form. OQ-15 xong phần Find Shops, còn Invite. OQ-8, OQ-11, OQ-14, OQ-20: vẫn mở, lý do ở trên.

## Giải pháp đáng học, điểm yếu Lượt 3
- Học: Record History ghi cả chuyển trạng thái lẫn đổi tiền từng lần, không cần log riêng cho đối soát đơn mua.
- Học: Worksheet kiểm kê in theo từng kho, có ô New Qty trống; hợp kiểm đếm tay ở bãi.
- Học: Make a Copy đơn giúp lặp đơn định kỳ phụ tùng đầu kéo, mooc.
- Yếu: Pending PO Qty không giảm khi lùi Purchased, nên số hàng đang về sai, dẫn tới quyết định đặt hàng sai.
- Yếu: đơn Closed vẫn đổi số nhận và tồn kho, không có lý do, không mở lại.
- Yếu: Void vẫn cộng vào tổng lít, tổng tiền của Fuel History; với đối soát dầu đầu kéo là sai số âm thầm.
- Yếu: Print Worksheet 1 cú bấm tải 3 file; PO và PDF đổi định dạng tiền so với web.

# Lượt 4 (03/11)

Vẫn không đổi Cài đặt, không gửi email, không có người thứ hai. Dùng lại kho, NCC, phụ tùng TEST-KHO.

## Sửa đơn Received Full có lưu thật — Chạy (FR-030)
Các bước đã làm: PO #3 (Full, đặt 12, nhận 12), Edit, đổi số đặt PT-A 12 thành 15, đơn giá 90.000 thành 95.000, "Save Purchase Order".
Kết quả thấy được: "Purchase Order was successfully updated". Đặt 15, nhận 12, **trạng thái vẫn "Received, Full"**, Total 1.069.760 thành 1.405.100 ₫. Menu vẫn: "Close", "Make Adjustment", "Print", "Make a Copy", "View Record History", "Delete"; không hiện "Receive" dù còn thiếu 3.
Thẻ PT-A: Current Qty 121 giữ nguyên, Pending PO Qty 15 giữ nguyên (đó là của PO #4), Unit Cost phụ tùng 100.000 giữ nguyên.
Bất ngờ: tăng số đặt trên đơn Full không đưa đơn về Partial, cũng không cộng Pending. Tức trạng thái không tính lại từ số đặt, số nhận khi sửa; đơn "đủ hàng" đang thiếu 3 mà không báo.

## Sửa đơn Draft có lưu thật — Chạy (FR-030)
Các bước đã làm: PO #3 › "Make a Copy" › "Save as Draft" ra PO #5. Edit #5: đổi Part Location TEST-KHO-01 thành TEST-KHO-02, xoá dòng PT-B, đổi Vendor sang TEST-NCC-01, "Save as Draft".
Kết quả thấy được: "Purchase Order was successfully updated". #5 Draft, kho TEST-KHO-02, NCC TEST-NCC-01, 1 dòng. Đổi kho, đổi NCC đều không xoá dòng, không hỏi lại; xoá dòng không có hộp xác nhận. Copy lấy số đặt, giá đã sửa của #3 (15; 95.000), không lấy số nhận.
Dữ liệu TEST đã tạo: PO #5 (Draft).
Thêm: PO #3 đã trả về 12 và 90.000 sau khi đo, Total về 1.069.760 ₫.

## Pending PO Qty ở Draft sau khi Edit — Chạy (sửa kết luận OQ-13 lượt 3)
Các bước đã làm: PO #5 (Draft, chưa từng Approve) đổi sang TEST-KHO-02, số 15; đọc thẻ PT-A; sửa số thành 7, Save as Draft; đọc lại.
| Thời điểm | TEST-KHO-01 Pending | TEST-KHO-02 Pending |
|---|---|---|
| Trước khi có #5 | 15 (của #4 Purchased) | 0 |
| #5 Draft đã Edit, số 15, tải lại trang | 15 | **15** |
| #5 Draft Edit, số 7 | 15 | **7** |
Kết luận chỉnh: lượt 3 đo #4 Draft mới tạo chưa Edit thì Pending 0. Thực tế: đơn Draft **một khi đã Edit và lưu** thì số vào Pending dù chưa duyệt. Quy tắc "chỉ tính từ Purchased" chỉ đúng cho đơn chưa Edit. Có thể cùng gốc với lỗi Pending không giảm khi Unmark: bước lưu Edit ghi Pending, không xét trạng thái (suy, không xem được mã).
Hiệu ứng thật: 7 cái ở TEST-KHO-02 là số ảo trên đơn nháp; nhóm khác đọc thẻ PT-A sẽ thấy. Không xoá #5.

## Nguồn điểm Rating nhà cung cấp — Một phần (FR-015)
Các bước đã làm: Vendors, Filters, Add Filter đọc danh sách; chọn Rating, không Apply. Find Shops gõ Atlanta, bấm ghim bản đồ, đóng, không thêm. Rê chuột cột Rating trên NCC Sample.
Kết quả thấy được: Trường lọc Vendor gồm "Archived", "Archived at", "Classification", "Contact Email", "Contact Name", "Contact Phone", "Labels", "Minority Owned (MBE)", "Network Status", "Phone", "Preferred", "Rating", "State/Province/Region", "Watcher", "Website", "Women Owned (MBE)". Chọn Rating ra "Vendor Rating", "is equal to", ô "Search number": điểm là số. 20 NCC, cả Sample lẫn TEST, đều hiện "..." và tooltip "Rating not available". Thẻ cửa hàng Find Shops và bóng ghim chỉ có tên, địa chỉ hoặc loại, khoảng cách, dấu xanh; không có điểm.
Trả lời: chưa thấy nơi nhập hoặc nơi sinh điểm trên form, danh sách, Find Shops. Nguồn vẫn chưa rõ. Có thể cần Shop Network (bị chặn vì Enable Shop Network là đổi Cài đặt); đây là suy đoán. Lọc Rating không Apply.

## Không chạy được (lượt 4)
- FR-010 Pending Approval, Rejected: cần người thứ hai. Mới thấy thêm: automation có Update Status "Approved", "Rejected" nhưng hãng bắt điều kiện Pending Approval (platform.md Lượt 4).
- FR-008 FIFO, LIFO, Average: đổi Cài đặt. FR-007 email tồn thấp: gửi email. FR-035 Invite: mời người ngoài.

## Trả lời câu hỏi mở Lượt 4
OQ-13 sửa: Draft chưa Edit: 0; Draft đã Edit và lưu: số vào Pending. OQ-15: Invite vẫn mở. Rating (FR-015): vẫn chưa rõ nguồn.

## Giải pháp đáng học, điểm yếu Lượt 4
- Yếu: Pending PO Qty tính cả đơn nháp đã sửa. Quyết định đặt hàng đọc Pending sẽ thừa hàng ảo; Invlogis nên tính từ trạng thái, không ghi lúc lưu form.
- Yếu: đơn Full không tính lại trạng thái khi tăng số đặt: đơn báo đủ hàng dù đang thiếu.
- Học: đổi kho và NCC trên Draft không xoá dòng hàng, đỡ nhập lại.
- Dữ liệu cuối: PO #5 Draft số 6, kho TEST-KHO-02, NCC TEST-NCC-01. PO #3 đã trả số cũ. Pending PT-A ở KHO-02 lần đọc cuối là 7, trước khi sửa về 6; chưa đọc lại.
