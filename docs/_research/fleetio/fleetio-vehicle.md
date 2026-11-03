---
type: research
keyword: "Fleetio: hồ sơ xe, mooc, gán xe, số đồng hồ, chi phí, bảo hành, phân tích thay xe"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/vehicle-management/brainstorms/vehicle-management.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/vehicle.md
  - docs/_research/fleetio/run-notes/platform.md
  - docs/_research/fleetio/fleetio-tires.md
---

# Giải pháp tham khảo: Hồ sơ và vòng đời phương tiện

> Khuyến nghị: **Tham khảo chọn lọc** cho `vehicle-management`. Fleetio đơn giản hơn nhu cầu Delta ở tổ hợp đầu kéo, mooc, container; mooc chỉ là một xe riêng có đường dẫn sang đầu kéo, một mooc nối được nhiều xe mà không biết đang kéo bởi đầu nào. Nên học cách gom thông tin, sổ số đồng hồ có luật chặn và tự Void, Void hàng loạt giữ lịch sử khi thay đồng hồ, hộp Archive báo trước hiệu ứng, cơ hội bảo hành theo mã trên lệnh. Không nên học cách đổi người lái đè lên phân công, việc không xét trùng theo người, trạng thái xe không ràng buộc gì, và lỗi Archive bị từ chối vẫn ngắt liên kết.

## 1. Idea Seed

Hồ sơ xe là trung tâm: một trang thấy đủ tình trạng, lịch sử và tạo được mọi bản ghi liên quan. Việc gán xe hiển thị dạng lịch, không cho trùng theo xe. Số đồng hồ có sổ riêng, biết từng số đến từ đâu, chặn số lệch thứ tự ngày và tự Void số quá cao; chi phí trên km tính từ chính sổ đó.

## 2. Context

**Feature Invlogis liên quan:** `vehicle-management` (#13, brainstorm đã có nhóm mooc, sơ đồ lốp, hút dầu), `vehicle-telematics` (số km từ GPS, sự việc cần xử lý), `transport-dispatch` (#12), `cost-catalog` (#9).

**Nguồn và bằng chứng:** chạy thật ngày 02/11/2026 trên `TEST-XE-01`; chạy tiếp ngày 03/11/2026 trên `TEST-XE-LOP` (Semi Truck, đồng hồ đầu 5.000 km) và `TEST-MOOC-LOP` (Trailer); lượt 3 cùng ngày thêm `TEST-DAUKEO-2` và đọc kết quả phiếu Fleetio Go có sẵn. Nhãn: `Chạy`, `Xem`, `Docs`, `Suy`, `GĐ`. Lốp sâu tách sang [[docs/_research/fleetio/fleetio-tires.md|Lốp]].

**Giới hạn của lượt chạy:** tài khoản dùng thử chỉ có 5 xe, đang 5 of 5. Lượt 3 đã chạy trạng thái thật, Archive, Restore, trùng tên xe. Lượt 5 đã tạo Motor Pool, mẫu bảo hành. Chưa chạy: đặt xe Motor Pool, dán nhiều dòng vượt hạn mức, gán nhóm thật, nguồn GPS.

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Quản lý phương tiện | Thông tin xe nằm ở nhiều nơi | Một trang tổng cho mỗi xe |
| Điều vận | Không biết xe đang giao cho ai | Lịch gán rõ ràng, không trùng |
| Kế toán | Khó tính chi phí trên km | Số km tin cậy, chi phí theo xe |
| Lãnh đạo | Không biết lúc nào nên thay xe | Số liệu vòng đời |
| Kỹ thuật xưởng | Sửa miễn phí mà vẫn trả tiền vì quên còn bảo hành | Thấy cơ hội bảo hành ngay trên lệnh |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Quản lý phương tiện | Tra cứu, cập nhật hồ sơ xe | Mỗi ngày | Cao | |
| Quản lý phương tiện | Bàn giao, thu hồi xe | Mỗi tuần | Cao | Sai người chịu trách nhiệm |
| Quản lý phương tiện | Sửa số đồng hồ sai | Mỗi tuần | Cao | Ảnh hưởng nhắc bảo dưỡng, chi phí/km |
| Điều vận | Xem xe rảnh | Mỗi ca | Cao | |
| Kế toán | Ghi chi phí định kỳ, xem chi phí/km | Mỗi tháng | Trung | |
| Kỹ thuật xưởng | Kiểm tra bảo hành khi mở lệnh | Mỗi lệnh | Trung | |
| Lãnh đạo | Xem phân tích thay xe | Hiếm | Thấp | |

## 4. Capabilities Breakdown

### P0 — must have

- V1 [Mới] [Lõi] **Trang xe trung tâm:** đầu trang có số đồng hồ, trạng thái, nhóm, người lái; khoảng 20 tab lịch sử; nút Add tạo 13 loại bản ghi với xe điền sẵn. Fleetio: `Chạy`. Áp vào `vehicle-management`.
- V2 [Mới] [Lõi] **Không cho gán xe trùng thời gian theo xe.** Fleetio: `Chạy`, báo lỗi ở cả ngày bắt đầu và kết thúc, không tự đóng phân công cũ, không xét trùng theo người. Áp vào `vehicle-management`.
- V3 [Mới] [Lõi] **Bàn giao kèm số km đầu, số km cuối.** Fleetio: `Chạy`, ô hiện khi chọn đủ xe và người, gợi ý số hiện tại; trang chi tiết có Distance. Hợp với biên bản bàn giao đang có câu hỏi `vehicle-management` OQ-2.
- V4 [Mới] [Lõi] **Sổ số đồng hồ có cột Nguồn**, liên kết về lệnh, lịch sử, phiếu dầu. Fleetio: `Chạy`.
- V5 [Mới] [Lõi] **Bỏ số sai (Void), kể cả tự động.** Fleetio: `Chạy` tự Void khi vượt mức một ngày (Fleetio: đúng 4.828 km vẫn nhận, thêm 1 km thì Void), tự Void lý do Out of Sequence với phiếu Fleetio Go (một ca), Void tay khi nhập, Void hàng loạt, Unvoid. Invlogis nên thêm bắt buộc lý do, Fleetio không hỏi.
- V16 [Mới] [Lõi] **Chặn số đồng hồ lệch thứ tự ngày.** Fleetio: `Chạy`, từ chối ngay ở trường với cả Meter Entry và Fuel Entry, cho lối thoát bằng tick Void.
- V17 [Mới] [Lõi] **Chi phí sở hữu và chi phí/km trên trang xe.** Fleetio: `Chạy`, chọn mốc thời gian, tách nhiên liệu, dịch vụ, khác; mẫu số là km đã chạy trong kỳ.

### P1 — should have

- V6 [Mới] [Lõi] **Lịch tài nguyên:** mỗi xe một hàng, xem ngày hoặc tuần, lịch tháng bên cạnh, thanh cam là tương lai, xanh là đang chạy, bấm ô trống tạo nhanh. Fleetio: `Chạy`. Có thể dùng làm mẫu hiển thị cho `transport-dispatch`, nhưng phải thêm tổ hợp đầu kéo, mooc.
- V7 [Mới] [Cấu hình] **Form xe chia 6 phần:** Chi tiết, Bảo dưỡng, Vòng đời, Tài chính, Thông số, Cài đặt; chỉ vài trường bắt buộc. Fleetio: `Chạy`.
- V8 [Mới] [Lõi] **Liên kết phương tiện (Linked Vehicles).** Fleetio: `Chạy`, hai chiều, gỡ được từ hai phía, không ngày, không lịch sử, không truyền km, không gộp lốp. Một mooc nối được nhiều xe, không kiểm loại xe, không biết đang kéo bởi đầu nào. Điểm khởi đầu đơn giản cho đầu kéo và mooc, nhưng không đủ cho nghiệp vụ ghép tách.
- V9 [Mới] [Cấu hình] **Đồng hồ phụ** theo giờ chạy. Fleetio: `Chạy`, chuỗi số riêng, phiếu chỉ có số phụ vẫn lưu được. Hợp với máy phát điện, xe nâng.
- V10 [Mới] [Cấu hình] **Tạo nhiều xe một lần** (Add Multiple Vehicles). Fleetio: `Chạy` 1 dòng lỗi, 1 dòng hợp lệ: dán tối đa 200 dòng, tự giải mã VIN, chạy nền; lỗi chỉ báo qua email. Hợp khi khởi tạo khách mới.
- V11 [Mới] [Gói: Bảo dưỡng đội xe] **Chỉ số đo lốp:** Fleetio: `Chạy`, xem [[docs/_research/fleetio/fleetio-tires.md|Lốp]]. Ghép vào sơ đồ lốp sẵn có.
- V12 [Mới] [Cấu hình] **Chi phí khác theo xe:** một lần hoặc định kỳ, 17 loại có sẵn, định kỳ sinh sẵn từng kỳ. Fleetio: `Chạy`. Invlogis vẫn lấy `cost-catalog` làm gốc.
- V18 [Mới] [Gói: Bảo dưỡng đội xe] **Cơ hội bảo hành trên lệnh sửa:** gắn mã bảo dưỡng vào bảo hành, Service Task cùng mã hiện gợi ý ngay trên lệnh. Fleetio: `Chạy`, khớp theo mã việc, không theo phụ tùng. Tính End Date, End Meter tự động.
- V19 [Mới] [Lõi] **Tách quyền cấp xe:** đổi trạng thái, gán xe, xem tài chính, lưu trữ là quyền con riêng. Fleetio: `Chạy` đọc màn Role.
- V20 [Mới] [Cấu hình] **Hạn mức xe theo gói, xe mẫu không tính.** Fleetio: `Chạy`, nút Add có khoá, câu cảnh báo tiền ngay tại quyền Create. Invlogis: tham số mới, chưa có mã.
- V23 [Mới] [Lõi] **Void hàng loạt để thay đồng hồ, giữ lịch sử số cũ.** Fleetio: `Chạy`, phải gõ VOID, Void toàn bộ thì xe về 0 km, nhận số mới bất kỳ. Không có bước khai báo thay đồng hồ, không lưu lý do. Số GPS là `Docs`.
- V24 [Mới] [Lõi] **Lưu trữ xe, có báo trước hiệu ứng.** Fleetio: `Chạy`, ngắt liên kết, đóng phân công đang chạy, xoá phân công tương lai; chặn khi còn lệnh mở. Restore không trả lại những gì đã mất.
- V25 [Mới] [Lõi] **Tên xe, số khung không trùng.** Fleetio: `Chạy`, trùng VIN xét cả xe mẫu, tên của xe đã lưu trữ không tính trùng (mới thấy không báo lỗi, chưa lưu).
- V26 [Mới] [Lõi] **Đính tài liệu dùng chung vào xe.** Fleetio: `Chạy`, chọn từ kho tài liệu chung, thẻ mang nhãn "Shared", tách khỏi tệp riêng của xe. Hợp giấy tờ áp cho nhiều xe.

### P2 — nice to have

- V13 [Mới] [Gói: Bảo dưỡng đội xe] **Phân tích thay xe:** chi phí trên km theo tuổi xe, từ giả định nhập tay. Fleetio: `Chạy` đọc: chỉ là máy tính chung, không theo xe, không đọc dữ liệu thật. Nếu làm, Invlogis nên đọc số thật từng xe. Cần vài năm dữ liệu.
- V14 [Mới] [Cấu hình] **Tùy biến bố cục trang xe.** Fleetio: `Chạy` ẩn hiện thẻ cá nhân, Restore defaults; layout tài khoản (Customize Layout) `Xem`; kéo đổi thứ tự chưa thử.
- V15 [Mới] [Cấu hình] **Giải mã số khung** (VIN Decode) để điền thông số. Fleetio: `Chạy`, có bảng so sánh, dòng khác biệt không tick sẵn, chỉ ghi vào xe khi lưu form. Dữ liệu chủ yếu phù hợp thị trường Mỹ, cần kiểm tra với xe tại Việt Nam.
- V21 [Mới] [Gói: Bảo dưỡng đội xe] **Recall theo hãng:** nhập tự động theo năm, hãng, đời từ nguồn NHTSA. Fleetio: `Xem`. Nguồn không áp được cho xe Việt Nam (`Suy`).
- V22 [Mới] [Gói: Bảo dưỡng đội xe] **Đặt xe chung (Motor Pool):** Fleetio: `Chạy` phần tạo pool, kiểm tra form đặt xe; chưa tạo được đặt xe vì người đặt phải vừa có đăng nhập vừa là Operator. Đặt theo loại xe, không theo xe cụ thể.
- V27 [Mới] [Cấu hình] **Mẫu bảo hành riêng của khách.** Fleetio: `Chạy`, một mẫu nhiều coverage, áp sinh nhiều bảo hành, sửa mẫu chọn áp tương lai hay cả quá khứ. Thư viện OEM 14 mẫu xe con, không có đầu kéo.

### 4.1 Giải pháp đáng học

| Giải pháp | Vì sao hay | Bằng chứng |
|---|---|---|
| Lối thoát "or marked as void" ngay trong câu lỗi | Không chặn cứng; số lạ vẫn ghi được mà không làm hỏng số hiện tại | `Chạy` |
| Cờ Conflict Source kèm popup số dòng, chênh lệch | Chỉ đúng dòng gốc cần sửa thay vì để người dùng tự dò | `Chạy` |
| Popup vượt ngưỡng ghi rõ Last Meter Entry, Daily Usage, Max, Exceeds By | Người dùng hiểu vì sao, sửa được | `Chạy` |
| Dòng Void không bao giờ là số hiện tại | Một luật giữ sạch nhắc bảo dưỡng và mọi tính toán sau | `Chạy` |
| Bấm ô trống trên lịch, xe và ngày điền sẵn | Điều vận tạo nhanh, ít nhầm | `Chạy` |
| Cơ hội bảo hành hiện cả khi trống, kèm số active, expiring soon | Người mở lệnh luôn thấy, không phải nhớ đi tra | `Chạy` |
| Một bảng Contact, tick Operator | Lái xe, thợ, kế toán chung hồ sơ | `Chạy` |
| Require Meter + Excluded Vehicle Types | Mẫu cho loại xe không đồng hồ như mooc | `Xem` |
| Sửa mẫu có lựa chọn tương lai hay cả quá khứ, báo số xe bị ảnh hưởng | Áp được cho mẫu giá thuê, định mức, chính sách của Invlogis | `Chạy` |
| Đặt xe theo loại xe, không theo xe cụ thể | Hợp khi người đặt chỉ cần "1 đầu kéo", điều độ mới gán xe (gán xe chưa chạy) | `Chạy` phần form |
| Void hàng loạt phải gõ VOID, số cũ vẫn còn trong sổ | Thay đồng hồ đầu kéo mà không xoá lịch sử, khó bấm nhầm | `Chạy` |
| Hộp Archive nói trước sẽ đóng, xoá những gì | Người dùng biết hậu quả trước khi bấm | `Chạy` |
| Dòng Void đánh dấu lý do, popup nêu số đang xung đột, chênh bao nhiêu | Biết ngay vì sao phiếu từ app không làm số hiện tại | `Chạy` |
| Giải mã VIN qua bảng so sánh, không tự ghi đè dòng khác biệt | Dữ liệu ngoài không đè mất loại xe đã chọn | `Chạy` |
| Status Updates ghi ai đổi, từ đâu sang đâu, kể cả "Fleetio Automation" | Truy được lý do xe đổi trạng thái lúc nào, bởi ai | `Chạy` |

### 4.2 Điểm yếu, không nên học

| Điểm yếu | Hệ quả | Đề xuất Invlogis | Bằng chứng |
|---|---|---|---|
| Đổi người lái đè lên phân công, mất người cũ trên trang | Không biết ai giữ xe trước đó | Hành động "bàn giao": tự đóng lần cũ, mở lần mới, có km | `Chạy` |
| Một người giữ nhiều xe không cảnh báo | Lịch sai không ai biết | Cảnh báo theo người, khách bật hay tắt: tham số mới, chưa có mã | `Chạy` |
| Unvoid không hỏi lý do, không kiểm lại ngưỡng | Một thao tác đẩy đồng hồ lên 20.000, số thật sau đó bị từ chối, chi phí/km sai | Bắt buộc lý do, xác nhận lại khi vượt ngưỡng | `Chạy`, `Suy` |
| Số nhỏ hơn cùng ngày lưu im lặng | Rác trong sổ | Cảnh báo, không chặn | `Chạy` |
| Số so sánh trong lỗi không phải số hiện tại; hộp nhập hiện số cũ | Người dùng không hiểu vì sao bị từ chối | Luôn nêu số, ngày đang so | `Chạy` |
| Ngày chữ xám giống đã điền | Lưu xong mới báo trống | Điền thật hoặc để trống hẳn | `Chạy` |
| Mooc không có đồng hồ vẫn bắt Primary Meter | Mooc thường đứng yên ở 0 km | Cho loại xe không đồng hồ; lấy km mooc từ chuyến đi | `Chạy`, `Suy` |
| Liên kết không ngày, không lịch sử | Không biết mooc đi cùng đầu kéo nào lúc nào | Giữ tổ hợp có thời gian trong `transport-dispatch` | `Chạy` |
| Replacement Analysis không theo xe, số mặc định kiểu đô la dù đơn vị ₫ | Không trả lời được "xe này nên thay chưa" | Đọc số thật từng xe | `Chạy` |
| Dòng định kỳ đúng hôm nay ở tab Future, nhưng đã tính vào chi phí | Hai nơi nói khác nhau | Một định nghĩa "đã phát sinh" | `Chạy` |
| Archive bị từ chối vẫn ngắt liên kết, 2/2 lần, không có dòng lịch sử | Mất quan hệ ghép đầu kéo, mooc mà không ai biết | Thao tác phải trọn vẹn hoặc không có gì | `Chạy` |
| Trạng thái xe không ràng buộc gì | Xe Sold, Out of Service vẫn gán tài xế, mở lệnh, nhập đồng hồ | Luật chặn theo trạng thái, xem OQ-7 | `Chạy` |
| Mooc nối nhiều xe không có ngày hiệu lực | Không biết đang kéo bởi đầu nào, không đủ ghép theo chuyến | Giữ tổ hợp có thời gian trong `transport-dispatch` | `Chạy` |
| Lỗi tạo hàng loạt chỉ gửi email | Màn hình không nói dòng nào sai | Báo ngay trên màn từng dòng | `Chạy` |
| Restore khoá khi đầy gói, Void khoá khi chọn lẫn, Decode khoá với VIN ngắn, đều không có lý do | Người dùng không biết phải làm gì | Luôn nêu lý do khoá | `Chạy` |
| Restore không trả lại liên kết, phân công; bấm là chạy, không báo | Tưởng khôi phục đủ | Báo trước phần không trả lại được | `Chạy` |
| Thay đồng hồ không có bước khai báo, không lưu lý do | Sau này không phân biệt được thay đồng hồ với số sai | Hành động thay đồng hồ riêng, xem OQ-8 | `Chạy` |
| Một lỗi nhóm mẫu làm cả form không lưu, dấu đỏ ở mục khác mục đang đứng | Tưởng đổi trạng thái không có tác dụng | Nêu lỗi ngay chỗ đang đứng | `Chạy` |
| Liên hệ không phải Operator chỉ hiện dòng "Create" trong ô gán | Dễ tạo trùng liên hệ | Hiện liên hệ đó kèm lý do không gán được | `Chạy` |
| Tab bộ lịch của xe chỉ có nút tạo mới, không gán được bộ lịch sẵn có | Phải rời xe để gán | Cho gán bộ lịch có sẵn ngay trên xe | `Chạy` |
| Áp mẫu về quá khứ ghi đè phần sửa riêng từng xe, chỉ có câu cảnh báo | Mất phần đã sửa tay | So sánh trước sau khi áp | `Chạy`, ghi đè `Xem` |
| Thư viện mẫu OEM thuần xe con Mỹ, không lọc theo Make | Vô dụng với đầu kéo, mooc Việt Nam | Mẫu riêng theo khách | `Chạy` |
| Người lái không đăng nhập không đặt được, cũng không được đặt hộ | Lái xe thường không có tài khoản, điều độ không đặt thay được | Cho điều độ đặt hộ | `Chạy` |
| Motor Pool bắt buộc Groups | Tài khoản không dùng nhóm xe không tạo được pool | Không bắt buộc nhóm | `Chạy` |
| Automation lật lại thao tác tay sau khoảng 1 giây, không báo | Người sửa tưởng đã đổi được | Báo khi luật ghi đè thao tác tay | `Chạy`, nhóm Nền tảng |

### 4.3 Đề xuất Invlogis từ lượt 3

Đề xuất để cân nhắc, chưa chốt với Delta.

| Đề xuất | Dựa trên | Tầng đề xuất |
|---|---|---|
| Hành động "thay đồng hồ": chốt số cũ, số đầu mới, lý do; giữ lịch sử, tính chi phí/km nối hai đoạn | Fleetio chỉ có Void hàng loạt | [Lõi] |
| Luật chặn theo trạng thái xe: xe đã bán, ngừng hoạt động không gán tài xế, không mở lệnh; khách bật hay tắt: tham số mới, chưa có mã | Fleetio không chặn gì | [Lõi] [Cấu hình] |
| Lưu trữ xe là thao tác trọn vẹn: bị từ chối thì không đổi gì; ghi lịch sử mọi thứ bị ngắt, đóng, xoá; khôi phục nêu rõ phần không trả lại | Lỗi E-fleetio-vehicle-022 | [Lõi] |
| Số từ thiết bị, app lệch thứ tự: lưu rồi tự Void kèm số xung đột; nhập tay: chặn ngay. Giữ hai đường như Fleetio, cả hai đều có việc để người xử lý | Ca Out of Sequence | [Lõi] |
| Ghép mooc theo tổ hợp có thời gian, không dùng liên kết không ngày | Mooc nối 2 xe không có ngày hiệu lực | [Lõi] |
| Tạo nhiều xe: kiểm trùng ở bước xem lại, báo lỗi trên màn, không qua email | Lỗi E-fleetio-vehicle-025 | [Cấu hình] |

## 5. Core Flows (Happy Path)

### 5.1 Tạo xe

1. Nhập tên, chọn loại, trạng thái, sở hữu; đơn vị số đo lấy theo tài khoản.
2. Lưu, sang trang xe; các khối hiện trạng thái rỗng và nút thêm.

```
Form xe ─> Trang xe ─> Add: lệnh, dầu, sự cố, số km, nhắc, gán xe...
```

### 5.2 Gán xe cho lái xe

1. Chọn xe, người lái, hoặc bấm ô trống trên lịch. Ô chọn chỉ hiện liên hệ có phân loại Operator; chưa có thì tạo ngay trong ô.
2. Chọn đủ xe và người thì hiện ô số km; nhập thời gian và số km đầu.
3. Hệ thống kiểm trùng theo xe. Lưu xong đầu trang xe hiện tên người lái.

```
Chọn xe ─> Chọn người ─> Thời gian, số km ─┬─ Trùng trên xe: báo lỗi, không lưu
                                           └─ Hợp lệ: cập nhật người lái hiện tại
                                              (người đang giữ xe khác vẫn hợp lệ)
```

### 5.3 Ghi số đồng hồ

1. Số đến từ lệnh sửa, phiếu dầu, phiếu kiểm tra, nhập tay, thiết bị.
2. Hệ thống kiểm thứ tự ngày, rồi mức tối đa một ngày.
3. Số lớn nhất không bị Void là số hiện tại; nhắc bảo dưỡng, chi phí/km tính lại.

```
Nguồn số km ─> Kiểm thứ tự ngày ─┬─ Lệch: từ chối, trừ khi tick Void
                                 └─ Đúng ─> Kiểm mức một ngày ─┬─ Vượt: lưu + tự Void + cờ dòng gốc
                                                               └─ Đạt ─> Số hiện tại của xe
                                                                         ├─> Nhắc bảo dưỡng
                                                                         ├─> Mức tiêu hao
                                                                         └─> Chi phí trên km
```

### 5.4 Mooc và đầu kéo

1. Tạo mooc là một xe loại Trailer, có đồng hồ riêng.
2. Khai trục mooc ở chính xe mooc (xem [[docs/_research/fleetio/fleetio-tires.md|Lốp]]).
3. Thêm mooc vào Linked Vehicles của đầu kéo; hai xe hiện đường dẫn sang nhau, không gì khác đổi.

```
Tạo mooc ─> Khai trục mooc ─> Linked Vehicles ─> Linked Assets ở cả hai xe
```

Một mooc nối thêm được xe khác, kể cả xe Car, không cảnh báo (`Chạy`).

### 5.5 Chi phí và chi phí/km

1. Tạo chi phí đơn lẻ hoặc định kỳ; định kỳ xử lý nền và sinh sẵn từng kỳ.
2. Cost of Ownership tính phần đã đến ngày, chia cho km đã chạy trong kỳ.

### 5.6 Bảo hành

1. Chọn nhiều xe, mỗi xe một ngày và số km bắt đầu; chọn loại coverage.
2. Nhập thời hạn, quãng đường, gắn mã bảo dưỡng; hệ thống tính End Date, End Meter.
3. Lệnh có Service Task cùng mã thì hiện Warranty Opportunities.

```
Bảo hành + mã ─> Lệnh sửa + Service Task cùng mã ─> View Active Coverage
```

### 5.7 Thay đồng hồ

1. Meter History lọc theo xe, tick các dòng chưa Void, Actions, Void, gõ VOID.
2. Void hết thì xe về 0 km; nhập số mới bất kỳ.

```
Tick dòng ─> Actions, Void ─> Gõ VOID ─> Xe 0 km ─> Nhập số mới
```

### 5.8 Lưu trữ, khôi phục xe

1. Đóng hết lệnh, More Actions, Archive, đọc hộp báo trước, xác nhận.
2. Liên kết mất, phân công đang chạy đóng, phân công tương lai bị xoá, xe sang tab Archived, trạng thái giữ nguyên.
3. Restore là chạy ngay; liên kết, phân công đã mất phải làm lại.

```
Đóng lệnh ─> Archive ─> Xác nhận ─┬─ Còn lệnh: từ chối, liên kết vẫn mất (lỗi)
                                  └─ Hết lệnh: sang tab Archived ─> Restore khi gói còn chỗ
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO |
|---|---|---|---|---|
| D1 | 5.2 | Thời gian chồng lần gán khác của cùng xe | Chặn | Lưu |
| D2 | 5.2 | Không nhập ngày bắt đầu | Hiểu là gán từ trước đến nay | Theo ngày nhập |
| D3 | 5.3 | Số nhỏ hơn số hiện tại, cùng ngày | Lưu thành số cũ, không báo | Xét D4 |
| D4 | 5.3 | Số lệch thứ tự so với ngày trước, ngày sau | Từ chối, trừ khi tick Void | Xét D5 |
| D5 | 5.3 | Vượt mức tối đa một ngày | Lưu + tự Void + cờ dòng gốc | Lên số hiện tại |
| D6 | 5.6 | Service Task cùng mã với coverage | Hiện cơ hội bảo hành | "No vehicle warranty opportunities to show." |
| D7 | 5.3 | Số lệch thứ tự đến từ nhập tay trên web | Từ chối ở trường | Phiếu Fleetio Go: lưu, tự Void Out of Sequence (một ca) |
| D8 | 5.7 | Danh sách chọn lẫn dòng đã Void và chưa Void | Void, Unvoid khoá | Mở Void, đòi gõ VOID |
| D9 | 5.8 | Xe còn lệnh chưa xong | Từ chối, liên kết vẫn mất | Archive |
| D10 | 5.8 | Gói đã đầy khi Restore | Nút khoá, không giải thích | Restore ngay, không hỏi |

### 6.2 Scenario Matrix

| From State | To State | Rule | Action | Result | Bằng chứng |
|---|---|---|---|---|---|
| Số hiện tại 1.010 km | Nhập 900 km cùng ngày | Không chặn | Lưu | Xếp là "110 km ago", số hiện tại giữ nguyên | `Chạy` |
| Số hiện tại 1.010 km | Nhập 1.600 km | Hợp lệ | Lưu | Số hiện tại 1.600, nhắc đổi trạng thái | `Chạy` |
| Số hiện tại 5.500 km | Nhập 5.300 km cùng ngày | Không chặn | Lưu | "200 km ago", số hiện tại giữ nguyên | `Chạy` |
| Số hôm nay 5.000 km | Nhập 5.800 km ngày 01/11 | Lệch ngày | Từ chối | "must be less than 5,000 or marked as void" | `Chạy` |
| Số hiện tại 5.500 km | Nhập 5.400 km ngày 04/11 | Lệch ngày | Từ chối | "must be greater than 5,500 or marked as void" | `Chạy` |
| Số hiện tại 5.500 km | Nhập 20.000 km hôm nay | Vượt mức | Lưu, tự Void | Auto-Voided, dòng 5.500 thành Conflict Source | `Chạy` |
| Dòng 20.000 Auto-Voided | Unvoid | Không kiểm lại | Confirm | Đồng hồ 20.000, cờ mất | `Chạy` |
| Có phân công 05–07/11 | Tạo phân công không End từ 04/11 | Trùng xe | Từ chối | "can't overlap existing assignments" | `Chạy` |
| Người đang giữ xe A, không End | Gán thêm xe B | Không xét theo người | Lưu | Cùng lúc giữ 2 xe | `Chạy` |
| Từ 100 km | Nhập 4.928 km (+4.828) | Đúng bằng mức | Lưu | Số hiện tại 4.928 | `Chạy` |
| Đang 4.928 km | Nhập 9.757 km (+4.829) | Vượt mức 1 km | Lưu, tự Void | Dòng 4.928 thành Conflict Source | `Chạy` |
| Mọi số chưa Void | Void hàng loạt | Gõ VOID | Void | Xe 0 km, "No meter history"; 100 km nhận ngay | `Chạy` |
| Dòng đã Unvoid, từng tự Void | Void lại | Nhớ lý do cũ | Void | Về Auto-Voided, không thành Manually Voided | `Chạy` |
| Xe Active | Out of Service, Sold, In Shop, Sold, Inactive | Không có luật | Đổi | Lưu cả, không hỏi lý do | `Chạy` |
| Xe Sold | Tạo lệnh, nhập đồng hồ | Không ràng buộc | Lưu | Xe vẫn Sold khi mở, đóng lệnh | `Chạy` |
| Xe có lệnh Open, có mooc | Archive | Chặn | Từ chối | Xe không Archive nhưng mất liên kết mooc ở hai phía | `Chạy` |
| Xe không còn lệnh, có phân công | Archive | Thành công | Lưu trữ | Phân công đang chạy đóng, tương lai xoá hẳn, Status giữ nguyên | `Chạy` |
| Xe Archived, gói còn chỗ | Restore | Không hỏi | Khôi phục | Giữ đồng hồ, trục; không trả lại liên kết, phân công | `Chạy` |
| Xe Archived, gói đầy | Restore | Nút khoá | Không có gì | Không có câu giải thích | `Chạy` |
| Mooc nối xe A | Nối thêm xe B (Car) | Không kiểm | Lưu | Hiện cả hai, không ngày hiệu lực | `Chạy` |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Gõ tên chưa có trong ô chọn | Ô chọn mở hộp tạo mới, điền sẵn tên | Lưu xong quay lại form | Huỷ thì quay lại form gốc |
| Chi phí định kỳ đang xử lý nền | Thông báo "Processing: Recurring expense save" | Tải lại trang nếu chưa thấy | Không cần |
| Form New Fuel Entry bỏ dở | Hộp "Leave site?" kẹt, không có phiếu nào được lưu | Không lưu | Không có dữ liệu thừa |
| Thoát form xe đã giải mã VIN, chưa Save Vehicle | Tab kẹt hộp rời trang, xe chưa đổi | Mở tab mới, làm lại | Không có dữ liệu thừa |
| Archive bị từ chối vì còn lệnh | Xe không Archive nhưng mất liên kết; phân công tương lai còn | Đóng lệnh, làm lại | Nối lại liên kết bằng tay |
| Add Multiple có dòng lỗi | Không tạo xe dòng đó, email gửi người đăng nhập | Sửa, dán lại | Nội dung email chưa kiểm |
| Một lỗi trường trong form xe | Cả form bị từ chối, mọi thay đổi khác không lưu | Bỏ trường lỗi, lưu lại | Không có dữ liệu thừa |

### 6.5 Other Edge Cases

- **Số nhỏ hơn cùng ngày không báo gì:** Fleetio không cảnh báo khi nhập 900 km trong khi xe đã 1.010 km (`Chạy`). Khác ngày thì bị từ chối. Invlogis nên cảnh báo vì GPS có thể mất tín hiệu, đồng hồ có thể thay.
- **Tạo liên hệ từ ô chọn dễ nhập nhầm:** gõ tên chưa có rồi Enter là mở form tạo mới; đã gặp đúng lỗi này khi chạy thử. Nên yêu cầu chọn rõ "Tạo mới".
- **Ngưỡng tự Void của Fleetio:** Fleetio: 4.828 km một ngày (`Chạy`, nhập 20.000 khi đang 5.500, vượt 9.672 km). Fleetio: 3.000 dặm, 24 giờ (`Docs`). Biên: đúng 4.828 km nhận, 4.829 km tự Void (`Chạy`). Lý do Exceeds Max. Daily Usage đã thấy; Out of Sequence đã thấy thật từ phiếu Fleetio Go (`Chạy`, một ca), nhập tay trên web không ra lý do này; telematics, API chưa thử. Icon lạ ở số 3.100 km chính là dấu đã Void.
- **Số so sánh trong lỗi lùi ngày:** số trong câu lỗi là dòng đầu của ngày sau, không phải số hiện tại (`Chạy`).
- **Một số sai lan sang chi phí:** Cost Per Meter chia cho km đã chạy, nên một lần Unvoid nhầm làm sai chi phí/km (`Suy` từ phép tính 3.500.000 / 15.000).
- **Start Meter bảo hành nhập 1000 hiện 1 km** (`Chạy`): lượt 5 thấy ô chỉ giữ ký tự đầu vì mất tiêu điểm, 2365 thành 2 km, không cảnh báo lệch đồng hồ xe; có thể do gõ tự động nhanh, chưa thử tay.
- **"No options" ở Coverage Template:** do chưa có mẫu đúng điều kiện, không phải do thiếu Make; lọc theo đơn vị đồng hồ là `Suy` (`Chạy`).
- **Múi giờ phân công:** trường ngày gửi đi theo múi giờ thiết bị trong khi tài khoản đặt múi giờ khác (`Chạy`). Dòng đồng hồ của phiếu app cũng ghi lệch ngày so với giờ Việt Nam (`Suy`).
- **Đóng lệnh để Archive:** đóng đòi Started At, số đồng hồ; Start Odometer 4.928 bị "must be less than 100 or marked as void", nhập 90 thì qua. Đóng lệnh tự sinh Service Entry, không đổi trạng thái xe (`Chạy`).
- **Xe Archived:** vẫn xem được đồng hồ, cấu hình trục; Edit trục khoá; Status vẫn hiện Active hoặc Inactive (`Chạy`).
- **Record History có lỗ hổng:** ghi đổi loại, ngày ngừng, Archived At; không ghi ngắt liên kết, đổi đồng hồ (`Chạy`).
- **Out-of-Service Date, Odometer chỉ là trường chữ:** không đổi Status, không tạo dòng đồng hồ (`Chạy`).
- **Menu Add đổi theo nhiên liệu:** xe Gasoline ẩn Add Charging Entry (`Chạy`).
- **Add Multiple giải mã VIN khác hộp tay:** Tire Type có, MSRP vẫn 0, trong khi hộp tay ra $26,360.00 (`Chạy`).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Xe | Bắt buộc tên, loại, trạng thái, sở hữu, đồng hồ chính, đơn vị nhiên liệu, đơn vị đo; tên, VIN không trùng; xe thật không dùng nhóm mẫu | `Chạy` |
| Giải mã VIN | Mở khi đủ 17 ký tự; `ABC123` thì khoá | `Chạy` |
| Void hàng loạt | Chỉ dòng chưa Void; gõ đúng VOID | `Chạy` |
| Archive | Không còn lệnh chưa xong; Motor Pool theo câu trong hộp, ca có đặt chỗ chưa chạy | `Chạy`, `Xem` |
| Gán xe | Bắt buộc xe, người lái; không trùng thời gian **tính theo xe, không tính theo người** | `Chạy` |
| Số đồng hồ | Theo thứ tự ngày, trừ khi tick Void; cùng ngày không ràng buộc | `Chạy` |
| Chi phí | Bắt buộc xe, loại, số tiền, ngày; định kỳ cần Start Date | `Chạy` |
| Bảo hành | Bắt buộc Start Date; Coverage Distance có Unlimited | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Số xe gói dùng thử | Fleetio: 5, xe Sample không tính | Theo gói | "Your plan is limited to 5 vehicles"; nút khoá | 
| Mức dùng một ngày | Fleetio: 4.828 km, đúng bằng vẫn nhận | Một ngày | Lưu + tự Void |
| Dán Add Multiple | Fleetio: tối đa 200 xe | Mỗi lần | Vượt chưa thử |
| Đơn vị số đồng hồ chính | Miles, Kilometers, Hours | Theo xe | Không bỏ được |
| Loại xe, loại chi phí | Fleetio: 25, 17 | Theo khách | Khách thêm được ở Settings (`Xem`) |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Trùng thời gian | "can't overlap existing assignments" | E-fleetio-vehicle-001 |
| Lưu lỗi | "Vehicle Assignment could not be created" | E-fleetio-vehicle-001 |
| Lùi ngày, số cao | "must be less than 5,000 or marked as void" | E-fleetio-vehicle-004 |
| Ngày mới, số thấp | "must be greater than 5,500 or marked as void" | E-fleetio-vehicle-005 |
| Hết hạn mức | "Your plan is limited to 5 vehicles" | E-fleetio-vehicle-009 |
| Không phải Operator | "Contact must have operator classification to be assigned to vehicles" | E-fleetio-vehicle-012 |
| Tự Void lệch thứ tự | "Automatically voided because it is out of sequence and ahead of the conflicting meter by 601 kilometers" | E-fleetio-vehicle-019 |
| Archive còn lệnh | "Vehicle could not be archived." | E-fleetio-vehicle-021 |
| Trùng tên, VIN | "has already been taken" | E-fleetio-vehicle-024 |
| Add Multiple lỗi | "Process warning: Add Multiple Vehicles", "Please check your email for detailed information about records that failed to create." | E-fleetio-vehicle-025 |
| Nhóm mẫu | "Selected group is a sample, and cannot be used with non-sample records." | E-fleetio-vehicle-028 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Tạo xe | "Vehicle was successfully created" |
| Thêm số đồng hồ | "Meter Entry was successfully created" |
| Tự Void | "Meter Entry was successfully created. However, it was automatically voided because it exceeds maximum possible for day" |
| Unvoid | "Successfully unvoided Meter Entry" |
| Tạo bảo hành | "Warranties have been successfully created" |
| Sửa phân công | "Vehicle Assignment was successfully updated" |
| Đổi trạng thái xe | "Vehicle was successfully updated" |
| Void hàng loạt | "Successfully voided Meter Entries" |
| Restore | "Record successfully restored!" |
| Liên kết | "Linked Assets have been updated" |
| Giải mã VIN | "We've successfully decoded your VIN and have downloaded the vehicle specifications." |

## 8. Assumptions

- Số km chính của Delta lấy từ GPS, nhập tay chỉ để bù.
- Mô hình `Linked Vehicles` không đủ thay nghiệp vụ ghép tách mooc đã có trong `transport-dispatch`: `Chạy` xác nhận chỉ là đường dẫn hai chiều, không ngày, không truyền km, không gộp lốp.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Trang xe 20 tab quá nặng cho mobile | Trung | Mobile chỉ hiện khối cần xử lý |
| Nhiều nguồn số km mâu thuẫn | Cao | Quy định nguồn ưu tiên, giữ dấu vết từng nguồn |
| Chép form Mỹ làm thừa trường | Trung | Chọn trường theo thực tế xe tại Việt Nam |
| Số km sai lan sang chi phí/km, nhắc bảo dưỡng | Cao | Lý do bắt buộc khi Unvoid, kiểm lại ngưỡng |
| Học theo Fleetio mà bỏ lịch sử người giữ xe | Cao | Bàn giao là hành động riêng, có lịch sử |
| Chép thao tác lưu trữ mà không làm trọn vẹn | Cao | Bị từ chối thì không đổi gì, xem Mục 4.3 |
| Chép liên kết không ngày cho đầu kéo, mooc | Cao | Dùng tổ hợp có thời gian |

## 10. Success Criteria (preliminary)

- Mọi thông tin cần xử lý của một xe xem được trong một trang.
- Đề xuất Invlogis: không có xe gán trùng thời gian, cảnh báo khi một người giữ nhiều xe. Fleetio chỉ chặn vế theo xe.
- Mỗi số km truy được về nguồn.
- Chi phí/km không bị một dòng số sai làm lệch.

## 11. Open Questions

| ID | Câu hỏi | Trạng thái | Nguồn khách |
|---|---|---|---|
| OQ-1 | Delta có cho một xe nhiều người lái theo ca không? | Mở. Sự thật Fleetio: được, miễn các khoảng không chồng nhau trên xe; không xét theo người | Chưa có trong tài liệu khách gửi |
| OQ-2 | Số km lệch giữa GPS và đồng hồ thì lấy số nào? | Mở | Chưa có trong tài liệu khách gửi |
| OQ-3 | Delta có cần đo gai lốp định kỳ không, hay chỉ quản lý vị trí lốp? | Mở. Sự thật Fleetio ở `fleetio-tires` | File sơ đồ lốp của Delta |
| OQ-4 | Lãnh đạo có cần phân tích thay xe không? | Mở. Sự thật Fleetio: chỉ là máy tính chung, không theo xe | Chưa có trong tài liệu khách gửi |
| OQ-5 | Delta có chặn một người giữ nhiều xe cùng lúc không? | Mở, mới | Chưa có trong tài liệu khách gửi |
| OQ-6 | Delta có cần bảo hành theo mã việc trên lệnh không? Hiện mã bảo dưỡng của Delta dùng gì? | Mở, mới | Chưa có trong tài liệu khách gửi |
| OQ-7 | Delta có chặn gán tài xế, mở lệnh, nhập đồng hồ khi xe đã bán, ngừng hoạt động không? | Mở, mới. Sự thật Fleetio: không chặn gì | Chưa có trong tài liệu khách gửi |
| OQ-8 | Khi thay đồng hồ, Delta có cần khai báo riêng kèm lý do, số chốt không? | Mở, mới. Sự thật Fleetio: không có bước này | Chưa có trong tài liệu khách gửi |

## 12. Next Steps

- Đối chiếu Mục 4 với `docs/vehicle-management/brainstorms/vehicle-management.md`, chỉ đưa vào ý chưa có.
- Lịch tài nguyên: nếu ổn, đưa vào phần giao diện Điều vận.
- Khi có liên hệ vừa đăng nhập vừa là Operator: đóng Lệnh đang mở, tạo đặt xe, chạy Motor Pool chặn Archive (SRS OQ-11). Khi có chỗ xe trống: dán nhiều dòng (SRS OQ-19). Lượt 4 chưa làm được vì gói đầy, Add Multiple khoá từ menu.
