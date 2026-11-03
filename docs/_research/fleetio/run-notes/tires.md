# Ghi chú chạy thử: Lốp (đi cạn, nối tiếp vehicle.md)

> Chạy 03/11/2026 trên tài khoản dùng thử. Xe dùng: `TEST-XE-LOP` (5890753, Semi Truck), `TEST-MOOC-LOP` (5890758, Trailer).
> Không tạo được xe thứ 3 trở đi: tài khoản đã chạm trần, nút Save Vehicle khoá, "You've reached the maximum number of records allowed on your account." Vì vậy không có `TEST-LOP-DAUKEO-2`, `TEST-LOP-MOOC-2`, `TEST-LOP-XECON`. Case giữa 2 đầu kéo, 2 mooc, xe con mới: suy từ cơ chế, ghi rõ từng dòng.
> Mức: **Chạy** = tự thao tác và thấy kết quả. **Suy luận** = rút từ số liệu, chưa tách riêng để chứng minh. **Docs** = help.fleetio.com. **Không chạy** = nêu lý do.

## 1. Kết luận nhanh

- Fleetio **không có đối tượng "quả lốp"**. Lốp là dữ liệu của **một vị trí trên một xe**. Vì thế không có trạng thái trong kho, không có chuyển lốp sang xe khác, không truy được 1 lốp qua nhiều xe.
- Trạng thái thật chỉ có 3: vị trí trống, có lốp, Spare. "Đã tháo" chỉ còn là dòng lịch sử.
- Mooc là 1 Vehicle độc lập: đồng hồ riêng, lốp riêng. Liên kết với đầu kéo chỉ là đường dẫn, không truyền số km.

## 2. Ma trận trạng thái

| Trạng thái | Hành động làm được | Sang trạng thái | Điều kiện | Hiệu ứng | Câu chữ nguyên văn | Mức |
|---|---|---|---|---|---|---|
| Xe chưa khai trục | Set up, chọn trong phiếu kiểm | Có trục, chưa lốp | Không | Phiếu kiểm hỏi trục; khai trong phiếu thì tự sinh lốp | "Set up this vehicle's axle configuration to begin managing tires." | Chạy (vehicle.md) |
| Vị trí trống | Bấm ô + (điền sẵn vị trí), Add, chip trục | Đang lắp | Vị trí đang trống | Dòng Activity `Installed` | "4 tires were installed on this vehicle." | Chạy |
| Vị trí trống | Copy details to... | Đang lắp | Chọn ô trống làm đích | **Tạo lốp mới**, `Installed`, ngày lắp là hôm nay, gai trống | "Details copied to 2 tire positions." | Chạy |
| Vị trí trống | "Install Tires" trong phiếu kiểm | Đang lắp | Xe thiếu lốp khi mở phiếu | Tạo lốp trống, không hỏi gì thêm | "This vehicle is missing 2 tires at these positions." | Chạy |
| Vị trí trống | Làm đích khi đảo | Đang lắp | Ô trống cũng có dòng New Position | Lốp chuyển sang ô này | "Successfully Rotated 2 tires" | Chạy |
| Đang lắp | Sửa gai, áp suất trên dòng hoặc hộp Edit | Giữ nguyên | Không | Dòng đọc mới, Method Manual | "Tire updated successfully." | Chạy |
| Đang lắp | Sửa Tire Meter, Model, Factory, Min, Life, TIN | Giữ nguyên | Không | Không có dòng Activity riêng cho TIN, Min | Hộp "Edit Left Outer (1LO)" | Chạy |
| Đang lắp | Đọc qua phiếu kiểm | Giữ nguyên | Xe được gán biểu mẫu có Tire Readings | Ghi về Tire Readings, Method `Inspection #...` | | Chạy |
| Đang lắp | Đảo | Vị trí khác | Sơ đồ đảo khép kín, cùng xe | Gai, áp suất, số km theo lốp | "Rotate Tires" | Chạy |
| Đang lắp | Undo Rotation | Vị trí cũ | Chỉ ở màn kết quả ngay sau đảo | Lốp về chỗ cũ, Activity **không còn dấu vết** lần đảo | "Undo Rotation" | Chạy |
| Đang lắp | Remove, Remove All | Trống | Không hỏi lý do, không chọn đích | Dòng `Removal` | "Are you sure you would like to permanently remove tires from this asset?" | Chạy |
| Đang lắp | Lắp đè | Bị chặn | Ô đã có lốp bị xám trong Position, chip trục đầy biến mất | Save vẫn tắt | | Chạy |
| Spare | Add, chọn "Spare Tire" | Spare | Chưa có Spare | Activity `Spare Stowed`, Axle Type `N/A`; đầu mục "6 + Spare" | "1 spare tire was installed on this vehicle." | Chạy |
| Spare | Sửa, đọc tay | Giữ nguyên | Không | Không có ô trên sơ đồ, chỉ có dòng ở Installed Tires | | Chạy |
| Spare | Đảo | **Không làm được** | Spare không có dòng trong Rotate, không có trong New Position | | | Chạy |
| Spare | Vào phiếu kiểm | **Không có** | Phiếu 12 vị trí, không có Spare | | | Chạy |
| Đã tháo | Xem Tire Activity | | Không còn dòng ở Tire Readings | Không có nút lắp lại, không có kho | | Chạy |
| Đã tháo | Lắp lại | Là 1 lần lắp mới | Gõ lại TIN bằng tay | Không nối với lịch sử cũ; km về 0 nếu không nhập tay | | Chạy |

Tháo xong lốp đi đâu: **không đi đâu cả**. Muốn dùng lại phải lắp mới.

## 3. Bảng case

### Cấu hình trục

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Vai trò trên mooc | Menu trục mooc | Dead, Lifted, Trailer, Other | Chạy |
| Vai trò trên xe | Menu trục xe | Steer, Drive, Dead, Lifted, Tag, Pusher, Other | Chạy |
| Đổi vai trò khi chưa lốp | Trailer → Lifted | "Trailer Axle 1 updated successfully", còn sau khi tải lại | Chạy |
| Đổi vai trò khi có lốp | Drive → Tag, Edit trục đang khoá | Đổi được, không có dòng Activity | Chạy |
| Vai trò có đổi số cầu kéo không | Trục sau thành Tag | Dòng phụ vẫn "4 wheel positions, 2 driven (rear)". Nhãn chữ, không phải dữ liệu tính toán | Chạy |
| Vai trò ghi vào lịch sử | Lắp lốp trên trục Tag | Axle Type của dòng là `Tag` | Chạy |
| Đổi cấu hình khi có lốp | | Edit khoá (tooltip ở vehicle.md) | Chạy |
| Tháo hết rồi đổi | Remove All 9 lốp | Edit mở lại, đổi 6x4 → 4x2 RWD (Dually) được; Activity giữ nguyên | Chạy |
| Đổi cấu hình làm mất vai trò | Tri-Axle có Lifted → Multi → Tri-Axle | Trục về "Trailer" | Chạy |
| Multi-Axle | Trên mooc | Hiện thêm "Number of Axles *" từ 2 đến 10. Tiêu đề "4 Axle" | Chạy |
| Loại xe và cấu hình có ràng buộc không | Semi Truck, ô Edit lọc "Axle" | Vẫn liệt kê 7 cấu hình mooc. Chưa lưu thử | Một phần |
| Số vị trí | Tri-Axle: "6 wheel positions", 12 ô. 6x4: "6 wheel positions, 4 driven", 10 ô | "Wheel position" đếm đầu trục, lốp kép vẫn tính 1 | Chạy |
| Lốp đơn, kép theo từng trục | | Không chỉnh được, đi theo cấu hình có sẵn | Chạy |
| 4x2 kép | 4x2 RWD (Dually) | Trước 2, sau 4 (Vị trí LO, LI, RI, RO), đúng đầu kéo 4x2 | Chạy |
| 12x, 8x4, 10x | | Không chạy, chỉ thấy trong danh sách | Không chạy |

### Lắp

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Nhiều lốp một lần | Chip "Axle 1" | Tạo 4 lốp cùng thông số, cùng TIN | Chạy |
| Thiếu TIN, gai, áp suất | Để trống | Lưu được. Sơ đồ hiện "–/32"", dòng "Unknown Tire" | Chạy |
| TIN trùng | Cùng xe, sang vị trí khác | Không cảnh báo | Chạy |
| Số thập phân | Gai 12.5, áp 95.5 | Activity giữ đúng 12.5; ô nhập hiện làm tròn 13; 4.5 trên sơ đồ hiện 5/32"; 79.9 PSI hiện 79PSI ở bảng | Chạy |
| Tire Model "No options" | Danh mục lấy từ **Part thuộc Category lốp** | Tạo Part `TEST-LOP-MODEL-01` category Tires thì xuất hiện ngay | Chạy |
| Chọn Tire Model | Model có Factory 20, Min 6, Life 120.000 | 3 ô tự điền và **khoá** (biểu tượng ổ khoá) | Chạy |
| Không có chi phí | Form lắp | Không có ô tiền. Part giá 3.000.000 ₫, "There is no Inventory Activity for this part"; Total Costs của xe tháng này 1.500.000 ₫ nên chắc chắn không cộng giá lốp | Chạy |
| Ngày lắp quá khứ | 10/20, 10/24 | Lưu được | Chạy |
| Tire Meter at Installation | Nhập 12.000 | Hiện "12,000 kilometers" | Chạy |
| Minimum để trống | Trục 3 mooc | Bảng lại hiện 4/32"; LO trên đầu kéo để trống thì trống; lắp từ phiếu thì trống. **Chưa rõ quy luật** | Chạy, chưa giải thích được |
| Copy details: trường | | Không chép được gai và áp suất: "For data accuracy, current tread depth and pressure cannot be copied." Ô rỗng thì khoá tick | Chạy |
| Copy details: lỗi dữ liệu | Chỉ tick TIN, chép sang 1LI và 1LO | TIN đổi, **Factory 16 và Life 100.000 của đích bị xoá trắng**. Lặp lại 2 lần đều vậy. Chỉ tick Factory thì TIN đích không đổi | Chạy |
| Copy details: lịch sử | Đích đã có lốp | Không có dòng Activity | Chạy |

### Đảo

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Mẫu trên mooc | Rotation Pattern | "No options". Settings có 8 mẫu chuẩn, không mẫu nào cho mooc | Chạy |
| Mẫu trên 6x4 | "Standard 6x4" | Điền sẵn 10 dòng, kể cả ô trống LF | Chạy |
| Đảo khi có ô trống | LF trống, Standard 6x4 | RF sang LF, RF thành trống. "Successfully Rotated 10 tires" (đếm cả ô trống) | Chạy |
| Tự do, chưa khép kín | Chỉ 1LO → 3LO | Nút Rotate Tires tắt | Chạy |
| Tự do, khép kín | Thêm 3LO → 1LO | Nút bật, hiện "Save as a Custom Rotation Pattern" | Chạy |
| Tick lưu mẫu, bỏ trống tên | | "Could not rotate tires.", "can't be blank" | Chạy |
| Undo | Ngay sau đảo | Lốp về chỗ cũ, quay lại form đảo, mapping còn nguyên. Activity sạch | Chạy |
| Undo sau khi đóng | Bấm Close | Không còn nút | Chạy |
| Đảo sang xe khác | | New Position chỉ có vị trí của xe đó | Chạy |
| Lưu mẫu tuỳ biến | | Không lưu: mẫu nằm trong Settings, quy định Settings chỉ đọc. Form Settings cho chọn cả nhóm mooc | Không chạy |

### Đọc

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Biên, Min 4 | 3.9, 4.0 | Low (đỏ) | Chạy |
| | 4.5, 5, 6.0 | Warning (vàng) | Chạy |
| | 6.1, 6.9, 7, 8 | Normal | Chạy |
| Biên, Min 8 | 9, 10 | Warning | Chạy |
| | 10.5, 11, 12 | Normal | Chạy |
| **Quy tắc** | | **Low: gai ≤ Min. Warning: Min < gai ≤ Min + 2. Normal: còn lại** | Suy luận từ 2 mức Min |
| Không có Min | TEST-XE-01 | 3/32" vẫn Low, 10/32" Normal. Ngưỡng mặc định chưa xác định | Chạy |
| Đổi Min | 5 → Min 8 | Mức tính lại theo Min mới | Chạy |
| Áp suất | 60 PSI | Không có mức theo lốp, chỉ phiếu kiểm mới có | Chạy |
| Đơn vị | Xe đặt Metric | Vẫn /32 in và PSI. Không thấy chỗ đổi mm, bar | Chạy |
| Đọc lùi ngày | | Không có ô ngày ở đọc trên dòng và hộp Edit | Chạy |
| Đọc nhiều lốp | | Trên màn lốp không có. Copy details không chép gai, áp suất. Cách duy nhất: phiếu kiểm | Chạy |
| Import | Docs có mẫu import lốp | Không chạy | Docs |
| Tự động | "Automated tire pressure readings" khoá, chỉ 4x2 hoặc 4x4 có telematics; docs nói Geotab | Không dùng được cho đầu kéo 6x4 | Chạy (đọc) + Docs |

### Đồng hồ, số km lốp

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Không bỏ đồng hồ được | Primary Meter | Chỉ Miles, Kilometers, Hours | Chạy |
| Mooc không có số đồng hồ nào lúc lắp | Lắp 10/20 và 10/24, sau đó nhập 1.000 (10/25), 3.000, 3.500 | Tire Meter vẫn "—", hộp Edit và Rotate hiện 0 | Chạy |
| Mooc có số trước ngày lắp | Lắp 11/03, có 1.000 ngày 10/25, 3.000 cùng ngày 11/03, nhập tiếp 3.500 | Tire Meter **2.500** = 3.500 − 1.000. Số cùng ngày lắp không làm mốc | Chạy, quy tắc là suy luận |
| Tính lại liên tục | TEST-XE-01 | 100 → 800 → 799 km khi đồng hồ đổi | Chạy |
| Đầu kéo tăng km | TEST-XE-LOP lên 20.500 | Mooc giữ nguyên 3.500 | Chạy |

### Liên kết

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Hai chiều | Liên kết từ đầu kéo | Mooc cũng có "Linked Assets" › TEST-XE-LOP | Chạy |
| Gỡ | Xoá chip ở đầu kéo | Mooc: "There are no linked Assets for this Vehicle"; lốp 12 + Spare, đồng hồ không đổi | Chạy |
| Gắn lại từ phía mooc | | Đầu kéo hiện lại mooc | Chạy |
| Đổi mooc | | Tức là gỡ rồi gắn. Không có lịch sử ghép, không có ngày | Suy luận |
| 1 mooc gắn nhiều đầu kéo | Ô chọn nhiều | Không chạy: xe còn lại của nhóm khác | Không chạy |

### Đổi lốp giữa các xe

| Case | Kết quả | Mức |
|---|---|---|
| Đầu kéo ↔ mooc, 2 đầu kéo, 2 mooc | Không có thao tác. Remove bên A, lắp mới bên B, gõ lại TIN, gai, áp suất, km. Hai lịch sử không nối | Cơ chế Chạy trên 1 xe; giữa 2 xe là suy luận |
| Cùng xe, không qua đảo | Remove rồi lắp, TIN `TEST-TIN-A2` dùng lại, không báo gì | Chạy |

### Phiếu kiểm

| Case | Điều kiện | Kết quả thật | Mức |
|---|---|---|---|
| Xe không thấy biểu mẫu | Mooc chưa gán form | "No inspection forms exist yet" dù tài khoản có form. Câu chữ gây hiểu nhầm | Chạy |
| Mục Tire Readings | Khi tạo form | Tick Tread Depth, Pressure; Minimum, Maximum cho từng cái; bắt ảnh hoặc nhận xét khi Pass, Fail | Chạy |
| Mooc có đủ cấu hình, thiếu lốp | Tri-Axle, thiếu 2 | Hộp "Install Missing Tires" kèm danh sách, nút Install Tires, "2 tires were successfully installed" | Chạy |
| Thứ tự ô | 12 vị trí | Đi vòng: bên trái từ trước ra sau, rồi bên phải từ sau ra trước | Chạy |
| Biên Pass, Fail | Min 5, áp 80 đến 120 | 5 Pass, 4.9 Fail; 80 Pass, 79.9 Fail; 120 Pass, 120.1 Fail. Biên tính là đạt | Chạy |
| Kết quả từng vị trí | Mở rộng mục | Từng dòng dấu tích hoặc X; dòng tổng 1 chữ "Fail" | Chạy |
| Ghi về lốp | | Có. Method "Inspection #126055120" | Chạy |
| Hai mức tối thiểu | 1LO gai 5, form Min 5, lốp Min 8 | Phiếu Pass, Tire Readings Low | Chạy |
| Fail tạo sự cố | | Issue #41 "[Inspection] Tire Readings", High, 1 sự cố cho nhiều lốp | Chạy |
| Sự cố gắn vị trí nào | | **Chỉ trong chữ mô tả**, không có trường vị trí: "Left Inner (1LI) Pressure and Tread Depth" và "Left Inner (2LI) Tread Depth" | Chạy |
| Mô tả thiếu lỗi | 2LI áp 120.1 có X ở phiếu | Mô tả sự cố không nhắc áp suất 2LI | Chạy |
| Fail lần 2 | | "Added to Issue #41 (1 time reported)" gợi ý gộp, chưa nộp lần 2 | Không chạy |

### Liên hệ sang

| Việc | Kết quả | Mức |
|---|---|---|
| Lệnh sửa chữa có đầu việc lốp | Form Work Order không có trường lốp. Dòng công việc, phụ tùng là loại chung. Lốp không đổi khi đóng lệnh là suy luận, chưa thêm phụ tùng lốp vào lệnh | Một phần |
| Phụ tùng lốp từ kho | Lắp bằng Tire Model không sinh Inventory Activity, không trừ kho | Chạy |
| Nhắc theo độ mòn | Không thấy ở Tire Management; docs không nói tới. Form nhắc lịch thuộc nhóm khác | Một phần |
| Chi phí | Không vào chi phí xe | Chạy |
| Báo cáo | Standard Reports chỉ có "Tire Activity Report"; thêm màn Tire Readings | Chạy |
| Cảnh báo dưới mức | Đọc trên màn lốp chỉ đổi màu, không sự cố, không thông báo (vehicle.md). Chỉ phiếu kiểm ra sự cố | Chạy |

## 4. Luồng nghiệp vụ

1. Quản trị: tạo xe → khai trục (mooc: chọn Trailer) → tuỳ chọn tạo Part category lốp làm Tire Model.
2. Kỹ thuật: lắp theo ô hoặc chip trục, nhập TIN, gai, áp suất, Min. Có thể bỏ qua hết trừ vị trí và ngày.
3. Đọc định kỳ: lái xe làm phiếu kiểm hoặc kỹ thuật sửa trực tiếp.
   - Phiếu Fail → Issue tự động → xử lý như sự cố thường.
   - Sửa trực tiếp dưới mức → chỉ đổi màu.
4. Đảo: chọn mẫu hoặc tự ghép khép kín → xong → Undo ngay được, đóng rồi thì thôi.
5. Thay lốp: Remove → lắp mới. Không nối với Work Order, không trừ kho, không có chi phí, không lý do.
6. Đổi mooc: sửa Linked Vehicles. Lốp và đồng hồ đứng yên.

## 5. Giải pháp đáng học, điểm yếu

Đáng học:
- Lắp theo chip trục và ô + điền sẵn vị trí: lắp cả xe rất nhanh, hợp đầu kéo 10 lốp, mooc 12 lốp.
- Ba mức gai có công thức đơn giản, Min theo lốp hoặc theo model.
- Đảo là sơ đồ khép kín, cho ô trống tham gia, có Undo tức thì.
- Phiếu kiểm tự sinh ô theo cấu hình trục, phát hiện thiếu lốp ngay trong phiếu.
- Vai trò trục tách khỏi hình dạng trục.

Điểm yếu, gắn logistics:
- Không có định danh lốp: lốp đắp, đảo giữa mooc, trả về kho đều mất dấu. TIN dùng chung và trùng thoải mái.
- Mooc đi theo đầu kéo mà km lốp không theo: nhập đồng hồ tay cho từng mooc, hoặc số km sai. Có thể im lặng "—" nếu chưa có số trước ngày lắp.
- Không có lý do tháo, đích đến, phế thải, chi phí, kho.
- Spare nằm ngoài đảo và ngoài phiếu.
- Copy details xoá trắng Factory, Life của đích; Undo xoá dấu vết.
- Sự cố lốp không có trường vị trí nên không thống kê được theo vị trí.

## 6. So với sơ đồ lốp của Delta

Nguồn: `design-system/components/application/tyre-layout.md`, `design-system/foundations/vehicle.md` mục 3, `design/_lab/tyre-mapping.html`, SRS cũ UC03.05 và UC05.06.05 (`docs-input/srs-cu/lg-srs-export.md`), `docs-input/srs-cu/srs-mobile/srs-mobile.md`, `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md`. Không tìm thấy file xlsx sơ đồ lốp gốc trong `docs-input`, chỉ có bản dựng lại ở lab.

| Yêu cầu Delta | Fleetio | Đáp ứng |
|---|---|---|
| `tractor-6x4` 10 + 1 | 6x4 + Spare | Có, Chạy |
| `tractor-4x2` 6 + 1 | 4x2 RWD (Dually) + Spare | Có, Chạy (Spare chưa thử riêng trên cấu hình này) |
| `trailer-2ax` 8 + 1, `trailer-3ax` 12 + 1 | Tandem, Tri-Axle 4 lốp mỗi trục + Spare | 3 giàn Chạy, 2 giàn theo danh sách |
| `truck-4x2`, `truck-6x4` | Cùng cấu hình trên | Có |
| `truck-6x2` 8 + 1 (2 dí 1 cầu) | 6x2 có trong danh sách, chưa xem hình | Chưa kiểm |
| `truck-8x4` 12 + 1, `truck-5ax` 16 + 1 | 8x4, 10x có trong danh sách, chưa xem hình | Chưa kiểm |
| `forklift-diesel` 4 | 4x2 thường | Có về số lốp, theo danh sách |
| `forklift-elec` 3 lốp | Không có cấu hình 3 lốp | Không |
| Container, máy phát: không lốp | Xe để chưa khai trục | Được, nhưng không có loại riêng |
| Tổ hợp đầu kéo + mooc + container | Chỉ Linked Vehicles, không vẽ chung | Không |
| Số thứ tự vị trí theo file, bên lái, bên phụ | Mã 2LO, 2RI. Không đổi tên, không đánh số | Không |
| Warning (đến hạn km, ngày, mòn) | Chỉ theo gai. Life Expectancy không tạo cảnh báo nào trong các case đã chạy | Một phần |
| Error (hỏng, cần thay) | Không có trạng thái hỏng trên vị trí | Không |
| Serial từng lốp, Tháo ra, Lắp vào, Đổi vị trí, Thay thế theo lệnh sửa chữa | TIN không duy nhất, tách khỏi Work Order | Không |
| Ngày lắp lấy theo ngày chốt lệnh | Nhập tay | Không |
| Chốt lệnh cập nhật tồn kho, tồn xưởng, rác thải | Không trừ kho, không có đích tháo | Không |
| Thẻ phân bổ `LOP_BiểnSố_Series`, metadata series + vị trí + km lúc lắp (FIAM G-LOP) | Không chi phí, không thẻ | Không |
| Chặn tạo lệnh sửa chữa khi sơ đồ lốp trống (FIAM) | Không chặn, chỉ nhắc trong phiếu kiểm | Không |
| Danh mục lốp có đề xuất, phê duyệt (UC03.05.03, .05) | Part không qua duyệt | Không |

## 7. Trả lời câu hỏi mở

- OQ-4 nhóm Phương tiện: phần còn thiếu ở vehicle.md đã có (biên gai, Undo, Copy, Spare, lốp mooc, nguồn Tire Model).
- Mục "Chưa làm" của vehicle.md: đã xong trừ lưu mẫu đảo tuỳ biến và Coverage Template.

## 8. Màn mới

- tire-rotate-name-required — images/tire-rotate-name-required.jpg — form đảo, "Could not rotate tires." Phần "can't be blank" nằm cuối form, ảnh chỉ có đầu form.
- tire-readings-boundary — images/tire-readings-boundary.jpg — bảng đọc với 3.9, 4.0, 4.5, 5, 6.9, 7, 8.
- inspection-tire-fail-summary — images/inspection-tire-fail-summary.jpg — Submission, dòng Tire Readings Fail, Issue #41.
- inspection-tire-fail-detail — images/inspection-tire-fail-detail.jpg — từng vị trí đạt, không đạt.
- part-tire-category-fields — images/part-tire-category-fields.jpg — Part category Tires, khối Tire Size.
- tire-management-trailer-12-spare — images/tire-management-trailer-12-spare.jpg — mooc đủ 12 ô, "12 + Spare", đủ màu Low, Warning, Normal.

Ảnh có tên "Bảo Tín" ở thanh bên, không có email.

## 9. Dữ liệu TEST đã tạo, đã đổi

- `TEST-MOOC-LOP`: 12 lốp + Spare, TIN `TEST-LOP-M1`, `M2`, `M3`, `NOMIN`, `SPARE`. Đồng hồ 1.000, 3.000, 3.500. Trang lốp lúc cuối hiện 3.502 km, tôi không nhập số này; chưa kiểm nguồn.
- `TEST-XE-LOP`: **đã Remove All 9 lốp** (thao tác "tháo" trên dữ liệu nhóm, cần để mở khoá cấu hình), đổi 6x4 → 4x2 RWD (Dually), trục sau thành Tag, còn 2 lốp LO (`TEST-TIN-A2`) và LI (`TEST-LOP-MODEL`). Đồng hồ thêm 20.500. Liên kết mooc đã gỡ rồi gắn lại.
- Biểu mẫu `TEST-LOP kiem lop` (679194), gán 2 xe trên. Phiếu #126055120, Issue #41.
- Part `TEST-LOP-MODEL-01` (9425062), giá 3.000.000 ₫, category Tires.

## 10. Chưa làm

- Xe thứ 3 trở đi (trần tài khoản): đổi lốp thật giữa 2 xe khác nhau, xe con mới, 1 mooc gắn 2 đầu kéo.
- Xem hình 6x2, 8x4, 10x, 12x. Fail phiếu lần 2. Thêm phụ tùng lốp vào Work Order. Lưu mẫu đảo tuỳ biến. Quy luật Minimum tự hiện 4/32".

# Lượt 3 (03/11)

## Lưu mẫu đảo tuỳ biến — Không chạy được (mẫu là danh mục dùng chung trong Settings, brief cấm tạo và không được xoá)
Các bước đã làm: Đọc Settings › Tire Management Settings, không bấm gì.
Kết quả thấy được: Khối "Tire Rotation Patterns" có "Add Tire Rotation Pattern", cột Name, Type, Created, Axle Configuration. 8 mẫu đọc được đều Type Standard, có icon khoá: Forward Cross, Front To Rear, Rearward Cross, Side-to-Side, X-Pattern (4x2 / 4x4); Classic Dually, Side-to-Side Dually (4x2 / 4x4 Dually); Standard 6x4 (6x2 / 6x4 / 6x6). Xác nhận mẫu thuộc cấp tài khoản.
Trả lời câu hỏi mở nào: OQ-7 nhóm Lốp: Một phần, nơi lưu đã rõ; việc lưu thật chưa chạy.

## Đọc áp suất tự động — Không chạy được (cài đặt tài khoản, cần telematics, brief cấm cả hai)
Các bước đã làm: Đọc Settings › Tire Management Settings › General.
Kết quả thấy được: Công tắc "Automated tire pressure readings" đang tắt, có icon khoá: "When enabled, Fleetio will automatically update tire pressure readings for all 4x2 or 4x4 vehicles with compatible telematics installed. Readings will update daily." Điều kiện 4x2, 4x4 đúng như lượt trước, không dùng được cho đầu kéo 6x4. Tên hãng Geotab vẫn chỉ từ tài liệu.

## Import lốp — Không chạy được (không tìm thấy lối vào)
Các bước đã làm: Xem trang Tire Readings, menu "…" của Vehicle List, tìm "import" trong Settings. Chỉ đọc, không bấm Import nào.
Kết quả thấy được: Tire Readings không có menu "…". Menu Vehicle List có Add Multiple Vehicles (khoá khi đầy gói), Import Vehicles, Import Meter Entries, Add GPS / Telematics Integration, Export Data; không có Import lốp. Settings tìm "import": "No results for: 'import'". Vẫn giữ mức Docs. Chưa loại trừ lối vào ở nơi chưa mở.

## Bổ sung từ nhóm xe
1 mooc nối 2 xe: chạy được (`vehicle.md`, mục Lượt 3). Xác nhận mooc nối với cả xe Car, không kiểm loại xe. Xe Archived vẫn giữ cấu hình trục, Edit trục khoá. Đổi lốp thật giữa 2 xe: lượt này không chạy.

# Lượt 4 (03/11)

## Lưu mẫu đảo tuỳ biến (FR-tires-016) — Không chạy được
Chặn: mẫu lưu nằm trong Settings, user chưa mở phần đổi Cài đặt. Không thử lại.

## Đọc áp suất tự động (FR-tires-029) — Không chạy được
Chặn: công tắc Settings khoá, cần telematics, brief cấm tích hợp. Không thử lại.
