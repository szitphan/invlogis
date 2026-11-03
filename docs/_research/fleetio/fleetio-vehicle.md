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

> Khuyến nghị: **Tham khảo chọn lọc** cho `vehicle-management`. Fleetio đơn giản hơn nhu cầu Delta ở tổ hợp đầu kéo, mooc, container; mooc chỉ là một xe riêng có đường dẫn sang đầu kéo. Nên học cách gom thông tin, sổ số đồng hồ có luật chặn và tự Void, cơ hội bảo hành theo mã trên lệnh. Không nên học cách đổi người lái đè lên phân công và việc không xét trùng theo người.

## 1. Idea Seed

Hồ sơ xe là trung tâm: một trang thấy đủ tình trạng, lịch sử và tạo được mọi bản ghi liên quan. Việc gán xe hiển thị dạng lịch, không cho trùng theo xe. Số đồng hồ có sổ riêng, biết từng số đến từ đâu, chặn số lệch thứ tự ngày và tự Void số quá cao; chi phí trên km tính từ chính sổ đó.

## 2. Context

**Feature Invlogis liên quan:** `vehicle-management` (#13, brainstorm đã có nhóm mooc, sơ đồ lốp, hút dầu), `vehicle-telematics` (số km từ GPS, sự việc cần xử lý), `transport-dispatch` (#12), `cost-catalog` (#9).

**Nguồn và bằng chứng:** chạy thật ngày 02/11/2026 trên `TEST-XE-01`; chạy tiếp ngày 03/11/2026 trên `TEST-XE-LOP` (Semi Truck, đồng hồ đầu 5.000 km) và `TEST-MOOC-LOP` (Trailer). Nhãn: `Chạy`, `Xem`, `Docs`, `Suy`, `GĐ`. Lốp sâu tách sang [[docs/_research/fleetio/fleetio-tires.md|Lốp]].

**Giới hạn của lượt chạy:** tài khoản dùng thử chỉ có 5 xe, đã hết, nên trạng thái thật, Archive, trùng tên xe, Motor Pool chưa chạy.

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
- V5 [Mới] [Lõi] **Bỏ số sai (Void), kể cả tự động.** Fleetio: `Chạy` tự Void khi vượt mức một ngày (Fleetio: 4.828 km), Void tay khi nhập, Unvoid. Invlogis nên thêm bắt buộc lý do, Fleetio không hỏi.
- V16 [Mới] [Lõi] **Chặn số đồng hồ lệch thứ tự ngày.** Fleetio: `Chạy`, từ chối ngay ở trường với cả Meter Entry và Fuel Entry, cho lối thoát bằng tick Void.
- V17 [Mới] [Lõi] **Chi phí sở hữu và chi phí/km trên trang xe.** Fleetio: `Chạy`, chọn mốc thời gian, tách nhiên liệu, dịch vụ, khác; mẫu số là km đã chạy trong kỳ.

### P1 — should have

- V6 [Mới] [Lõi] **Lịch tài nguyên:** mỗi xe một hàng, xem ngày hoặc tuần, lịch tháng bên cạnh, thanh cam là tương lai, xanh là đang chạy, bấm ô trống tạo nhanh. Fleetio: `Chạy`. Có thể dùng làm mẫu hiển thị cho `transport-dispatch`, nhưng phải thêm tổ hợp đầu kéo, mooc.
- V7 [Mới] [Cấu hình] **Form xe chia 6 phần:** Chi tiết, Bảo dưỡng, Vòng đời, Tài chính, Thông số, Cài đặt; chỉ vài trường bắt buộc. Fleetio: `Chạy`.
- V8 [Mới] [Lõi] **Liên kết phương tiện (Linked Vehicles).** Fleetio: `Chạy`, hai chiều, gỡ được từ hai phía, không ngày, không lịch sử, không truyền km, không gộp lốp. Điểm khởi đầu đơn giản cho đầu kéo và mooc, nhưng không đủ cho nghiệp vụ ghép tách.
- V9 [Mới] [Cấu hình] **Đồng hồ phụ** theo giờ chạy. Fleetio: `Xem`. Hợp với máy phát điện, xe nâng.
- V10 [Mới] [Cấu hình] **Tạo nhiều xe một lần** (Add Multiple Vehicles). Fleetio: `Xem` nút. Hợp khi khởi tạo khách mới.
- V11 [Mới] [Gói: Bảo dưỡng đội xe] **Chỉ số đo lốp:** Fleetio: `Chạy`, xem [[docs/_research/fleetio/fleetio-tires.md|Lốp]]. Ghép vào sơ đồ lốp sẵn có.
- V12 [Mới] [Cấu hình] **Chi phí khác theo xe:** một lần hoặc định kỳ, 17 loại có sẵn, định kỳ sinh sẵn từng kỳ. Fleetio: `Chạy`. Invlogis vẫn lấy `cost-catalog` làm gốc.
- V18 [Mới] [Gói: Bảo dưỡng đội xe] **Cơ hội bảo hành trên lệnh sửa:** gắn mã bảo dưỡng vào bảo hành, Service Task cùng mã hiện gợi ý ngay trên lệnh. Fleetio: `Chạy`, khớp theo mã việc, không theo phụ tùng. Tính End Date, End Meter tự động.
- V19 [Mới] [Lõi] **Tách quyền cấp xe:** đổi trạng thái, gán xe, xem tài chính, lưu trữ là quyền con riêng. Fleetio: `Chạy` đọc màn Role.
- V20 [Mới] [Cấu hình] **Hạn mức xe theo gói, xe mẫu không tính.** Fleetio: `Chạy`, nút Add có khoá, câu cảnh báo tiền ngay tại quyền Create. Invlogis: tham số mới, chưa có mã.

### P2 — nice to have

- V13 [Mới] [Gói: Bảo dưỡng đội xe] **Phân tích thay xe:** chi phí trên km theo tuổi xe, từ giả định nhập tay. Fleetio: `Chạy` đọc: chỉ là máy tính chung, không theo xe, không đọc dữ liệu thật. Nếu làm, Invlogis nên đọc số thật từng xe. Cần vài năm dữ liệu.
- V14 [Mới] [Cấu hình] **Tùy biến bố cục trường** trên trang xe (Customize Layout). Fleetio: `Xem` nút.
- V15 [Mới] [Cấu hình] **Giải mã số khung** (VIN Decode) để điền thông số. Fleetio: `Xem` nút. Dữ liệu chủ yếu phù hợp thị trường Mỹ, cần kiểm tra với xe tại Việt Nam.
- V21 [Mới] [Gói: Bảo dưỡng đội xe] **Recall theo hãng:** nhập tự động theo năm, hãng, đời từ nguồn NHTSA. Fleetio: `Xem`. Nguồn không áp được cho xe Việt Nam (`Suy`).
- V22 [Mới] [Gói: Bảo dưỡng đội xe] **Đặt xe chung (Motor Pool):** Fleetio: `Xem`, chưa chạy.

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

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Gõ tên chưa có trong ô chọn | Ô chọn mở hộp tạo mới, điền sẵn tên | Lưu xong quay lại form | Huỷ thì quay lại form gốc |
| Chi phí định kỳ đang xử lý nền | Thông báo "Processing: Recurring expense save" | Tải lại trang nếu chưa thấy | Không cần |
| Form New Fuel Entry bỏ dở | Hộp "Leave site?" kẹt, không có phiếu nào được lưu | Không lưu | Không có dữ liệu thừa |

### 6.5 Other Edge Cases

- **Số nhỏ hơn cùng ngày không báo gì:** Fleetio không cảnh báo khi nhập 900 km trong khi xe đã 1.010 km (`Chạy`). Khác ngày thì bị từ chối. Invlogis nên cảnh báo vì GPS có thể mất tín hiệu, đồng hồ có thể thay.
- **Tạo liên hệ từ ô chọn dễ nhập nhầm:** gõ tên chưa có rồi Enter là mở form tạo mới; đã gặp đúng lỗi này khi chạy thử. Nên yêu cầu chọn rõ "Tạo mới".
- **Ngưỡng tự Void của Fleetio:** Fleetio: 4.828 km một ngày (`Chạy`, nhập 20.000 khi đang 5.500, vượt 9.672 km). Fleetio: 3.000 dặm, 24 giờ (`Docs`). Lý do Exceeds Max. Daily Usage đã thấy; Out of Sequence không tái hiện được trên web, có thể chỉ từ telematics, API (chưa kiểm chứng).
- **Số so sánh trong lỗi lùi ngày:** số trong câu lỗi là dòng đầu của ngày sau, không phải số hiện tại (`Chạy`).
- **Một số sai lan sang chi phí:** Cost Per Meter chia cho km đã chạy, nên một lần Unvoid nhầm làm sai chi phí/km (`Suy` từ phép tính 3.500.000 / 15.000).
- **Start Meter bảo hành nhập 1000 hiện 1 km** (`Chạy`), chưa rõ do ô nhập hay định dạng.
- **Múi giờ phân công:** trường ngày gửi đi theo múi giờ thiết bị trong khi tài khoản đặt múi giờ khác (`Chạy`).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Xe | Bắt buộc tên, loại, trạng thái, sở hữu, đồng hồ chính, đơn vị nhiên liệu, đơn vị đo | `Chạy` |
| Gán xe | Bắt buộc xe, người lái; không trùng thời gian **tính theo xe, không tính theo người** | `Chạy` |
| Số đồng hồ | Theo thứ tự ngày, trừ khi tick Void; cùng ngày không ràng buộc | `Chạy` |
| Chi phí | Bắt buộc xe, loại, số tiền, ngày; định kỳ cần Start Date | `Chạy` |
| Bảo hành | Bắt buộc Start Date; Coverage Distance có Unlimited | `Chạy` |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Số xe gói dùng thử | Fleetio: 5, xe Sample không tính | Theo gói | "Your plan is limited to 5 vehicles"; nút khoá | 
| Mức dùng một ngày | Fleetio: 4.828 km | Một ngày | Lưu + tự Void |
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

#### Success messages

| Tình huống | Wording |
|---|---|
| Tạo xe | "Vehicle was successfully created" |
| Thêm số đồng hồ | "Meter Entry was successfully created" |
| Tự Void | "Meter Entry was successfully created. However, it was automatically voided because it exceeds maximum possible for day" |
| Unvoid | "Successfully unvoided Meter Entry" |
| Tạo bảo hành | "Warranties have been successfully created" |
| Sửa phân công | "Vehicle Assignment was successfully updated" |

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

## 12. Next Steps

- Đối chiếu Mục 4 với `docs/vehicle-management/brainstorms/vehicle-management.md`, chỉ đưa vào ý chưa có.
- Lịch tài nguyên: nếu ổn, đưa vào phần giao diện Điều vận.
- Khi có chỗ xe trống: chạy đổi trạng thái thật, Archive và Restore, Motor Pool (SRS OQ-11).
