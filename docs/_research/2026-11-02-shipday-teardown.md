---
type: research
keyword: "phân tích tính năng phần mềm điều phối giao hàng Shipday"
status: draft
updated: 2026-11-02
links:
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Phân tích tính năng Shipday Dispatch

> **Khuyến nghị: NÊN THAM KHẢO — chọn lọc.** Đáng học bộ tự gán đơn có phương án dự phòng, nhật ký gán đơn, cách cấu hình lương tài xế và cách giới hạn tính năng theo gói. Không chép mô hình dữ liệu: Shipday làm cho giao đồ ăn chặng ngắn, một đơn một điểm lấy một điểm giao, còn Lệnh vận tải của Invlogis có tổ hợp xe, mốc cảng và đối soát chi phí.

***

## Tóm tắt

Shipday là phần mềm SaaS cho doanh nghiệp nhỏ tự giao hàng (nhà hàng, tạp hoá, chuyển phát nội thành). Lõi là 4 màn: Điều phối, Đơn, Tài xế, Bản đồ. Xung quanh là tự gán đơn, tối ưu tuyến, trả lương tài xế, trang theo dõi cho khách, báo cáo, cổng merchant, 52 tích hợp và lớp AI bán thêm.

**Nhãn độ chắc chắn dùng trong tài liệu:**

| Nhãn | Nghĩa |
|---|---|
| **Thấy trực tiếp** | Thấy trên màn hình tài khoản thật, kể cả phần mờ sau lớp khoá gói |
| **Trong code** | Đọc được trong JS hoặc file chữ giao diện, chưa thấy chạy |
| **Suy ra** | Kết luận rút từ các dữ kiện trên, chưa kiểm chứng |
| **Chưa biết** | Không có dữ liệu để trả lời |

Không ghi nhãn trong bảng nghĩa là **Thấy trực tiếp**.

## Nguồn phân tích

| Mục | Giá trị |
|---|---|
| Sản phẩm | Shipday Dispatch, bản web |
| Ngày xem | 2026-11-02 |
| Tài khoản | Tài khoản của người phân tích, gói Starter, không có dữ liệu thật |
| Cách làm | Đi qua giao diện; đọc JS và file chữ tiếng Anh công khai (75 file, 9,1 MB); không gọi API trực tiếp |
| Dữ liệu thử | 1 đơn `TEST-001` đi tới Delivered; đơn này còn nằm trong tài khoản vì đơn đã giao không còn nút xoá |

File JS và dữ liệu thô không lưu trong repo.

### Độ phủ

| Mức | Nội dung |
|---|---|
| Đã chạy thật trên web | Tạo đơn, gán tài xế, sẵn sàng lấy, đánh dấu đã giao, trang theo dõi, form đánh giá, nhật ký gán, báo cáo sau khi có đơn |
| Chỉ thấy phần mờ (khoá theo gói) | Reviews, Analytics, Heatmap, báo cáo Extended và Customers, Branding, luật gán đơn, nhiều người dùng, Merchant |
| Chỉ có trong code | Chi tiết luật gán, tạo tuyến, AI, Marketing, đối tác giao ngoài |
| Chưa thấy | App tài xế, app quản lý, tối ưu tuyến chạy thật, giao qua đối tác ngoài, đơn thất bại đi đến cuối, đơn Scheduled |

## 1. Luồng nghiệp vụ

### Luồng đã chạy

```
Tạo đơn (tay / CSV / API / form / tích hợp)
   → Unassigned (hiện ở Điều phối, Đơn, Bản đồ)
   → Gán tài xế → Waiting (có link theo dõi)
   → [App tài xế: nhận, lấy hàng, đi giao — chưa thấy]
   → Delivered → Completed → khách đánh giá → vào báo cáo
```

### Trạng thái đơn

| Mã trong code | Chữ hiển thị | Thấy khi chạy |
|---|---|---|
| `NOT_ASSIGNED` | Unassigned | Có |
| `PRE_ASSIGNED` | Pre-assigned | Không |
| `BROADCASTED` | Broadcasted | Không |
| `NOT_ACCEPTED` | Waiting | Có |
| `NOT_STARTED_YET` | Not started | Không |
| `STARTED` | Started | Không |
| `PICKED_UP` | Picked Up | Không |
| `READY_TO_DELIVER` | On the Way | Không |
| `ALREADY_DELIVERED` | Delivered | Có |
| `INCOMPLETE` | Incomplete | Không |
| `FAILED_DELIVERY` | Failed | Không (chỉ mở hộp thoại) |
| `CANCELLED` | Cancelled | Không |

Thứ tự các trạng thái giữa Waiting và Delivered là **Suy ra** từ tên và thứ tự trong file chữ.

### Hành vi quan sát được đáng chú ý

| Tình huống | Kết quả |
|---|---|
| Đơn chưa gán | Không có link theo dõi; có link ngay khi gán, chưa cần tài xế nhận |
| Gán cho tài xế Offline | Được phép, khi tắt cài đặt "chỉ gán tài xế online" |
| Bật Ready for pick-up | Trạng thái vẫn Waiting, trang theo dõi không đổi |
| Đánh dấu đã giao lúc đơn còn Waiting | Đóng ngay, **không có hộp xác nhận** |
| Sau khi đóng đơn như trên | Tài xế bị xoá khỏi đơn (Not assigned), lương ngày ghi 0 chuyến, nhưng cột giờ lấy hàng ở tab Completed vẫn hiện giờ yêu cầu |
| Đánh dấu thất bại | Hộp xác nhận có 1 ô ghi chú tự do, không có danh sách lý do |
| Đơn đã Delivered | Chỉ còn tải PDF và in, không sửa, không xoá |
| Tài xế không phản hồi trong 10 phút (mặc định) | Theo mô tả cài đặt: đơn quay lại màn Điều phối. Chưa kiểm chứng |

**Điểm yếu nên tránh:** đóng đơn tay không xác nhận, làm mất dấu tài xế và để lại dữ liệu thời gian không nhất quán.

## 2. Tính năng theo module

### 2.1 Điều phối (Dispatch)

- Bố cục 2 khối: trái là tài xế kèm đơn đang giữ, phải là New Orders.
- Thẻ đơn hiện mã, tiền, điểm lấy, điểm giao, giờ; nút **Assign**, sau khi gán đổi thành nhãn "Waiting for {tài xế}" và nút **Unassign**.
- Hộp Assign Order liệt kê tài xế, trạng thái, loại xe, số đơn đang giữ. Bấm một lần là gán.
- Có gán trước (Pre-assign) và gán lại (Reassign) — **Trong code**.

### 2.2 Đơn (Orders)

| Thành phần | Chi tiết |
|---|---|
| Tab | Current · Scheduled · Completed · Incomplete · History |
| Cột Current | Mã, khách, điểm lấy, tiền, khoảng cách, giờ đặt, giờ yêu cầu lấy, giờ yêu cầu giao, Ready for pick-up, tài xế, trạng thái, tracking |
| Cột Completed | Thêm giờ bắt đầu, giờ lấy, giờ giao thật, đánh giá |
| Tạo đơn | Form tay, nhập CSV, API, form đặt đơn, tích hợp |
| Trường bắt buộc | Mã đơn; tên, điện thoại, địa chỉ, giờ điểm lấy; tên, điện thoại, địa chỉ, ngày giờ điểm giao |
| Trường tuỳ chọn | Email khách, đơn catering, dòng hàng (tên, giá, số lượng), thuế %, phí giao, tip, giảm giá, ghi chú giao, thanh toán (Cash, Credit Card) |
| Tiện ích form | Tự tính tổng, tìm lại địa chỉ và khách cũ, gợi ý địa chỉ Google, chỉnh ghim vị trí |
| Thao tác dòng | Reassign, Details, Edit, Print order, Print label, Cancel order |
| Thao tác chi tiết | Mark as Delivered, Edit, Download PDF, Print, Mark as Failed, Delete |
| Chi tiết đơn | Tab Details (người nhận, hàng, tiền, mốc giờ, thanh toán, POD, Proof of Pickup) và tab **Assignment history** |
| Hành động khác | Thao tác hàng loạt, tạo đơn hoàn (`createReturnOrder`) — **Trong code** |

**Nhật ký gán đơn** mỗi dòng ghi: loại (In-house driver), tài xế, người gán, thời gian.

### 2.3 Tự gán đơn (Automatic Assignment)

Mở Settings › Dispatch settings › Auto-assign. Form chia 4 phần.

| Phần | Nội dung |
|---|---|
| Driver assignment | Cách chọn tài xế, khoảng cách tới điểm lấy, số đơn tối đa mỗi tài xế |
| Dispatch timing | Gửi ngay hoặc khi sẵn sàng; thời gian chờ trước khi chuyển phương án dự phòng |
| Fallback behavior | Khi không có ai nhận: giữ trong hàng đợi, hoặc đẩy sang đối tác ngoài |
| Driver selection rules | Luật tuỳ chỉnh, khoá theo gói |

**Cách chọn tài xế:** ít đơn nhất · gần điểm lấy nhất · cùng khu vực · gom đơn cùng hướng (mức Thấp, Vừa, Cao) · broadcast cho tài xế gần nhất · broadcast tất cả · round robin.

**Giao ngoài (Trong code, chỉ ở Mỹ):** chọn theo giá thấp nhất, lấy hàng nhanh nhất hoặc ưu tiên; gửi ngay, sau 5–40 phút, hoặc khi sẵn sàng; dự phòng là giữ, đổi nhà cung cấp, hoặc về tài xế nhà. Có đối tác địa phương và mời công ty giao hàng địa phương.

**Luật tuỳ chỉnh (Trong code):** điều kiện theo giá trị đơn, khoảng cách, số món, tip, tổng phụ, giờ, ngày, loại thanh toán, món, loại đơn; toán tử lớn hơn, nhỏ hơn, bằng, trước, sau, trong khoảng, có chứa, không chứa; kết quả là gửi về nhóm đích. Có luật mặc định khi không luật nào khớp.

Có nhật ký tự gán riêng `/auto-dispatch-log/...` — **Trong code**.

### 2.4 Tuyến (Routes)

Bật tuyến bị khoá ở gói Starter, toàn bộ phần dưới là **Trong code**, trừ màn cài đặt.

| Thành phần | Chi tiết |
|---|---|
| Cài đặt | Một hoặc nhiều điểm lấy; thời gian mỗi điểm dừng; tuyến khép kín về điểm lấy; khung giờ giao và mức cứng (10 phút–12 giờ); thời gian chờ tối đa của tài xế; ép đi đúng thứ tự |
| Tạo tuyến | Chọn đơn trên bản đồ hoặc khoanh vùng, nhập số tuyến, chọn điểm xuất phát, xác nhận |
| Quản lý | Tối ưu lại, đổi thứ tự, in, tải về, thêm hoặc bỏ đơn, tài xế tự tối ưu lại trên app |
| Luật chặn | Đơn đã gán không vào tuyến; đơn khác điểm lấy không vào tuyến; số tuyến không ít hơn số điểm lấy; xoá đơn trong tuyến có cảnh báo; bỏ gán đơn đã lấy có cảnh báo |

### 2.5 Bản đồ (Map)

- Panel bật tắt được: Drivers, Orders, Routes; bản đồ bên phải.
- Lọc: ngày, buổi, trạng thái đơn, tài xế đã gán hay chưa, loại xe, điểm đánh giá tài xế.
- Trong code còn có: lọc khách VIP, khách mới, danh sách đen; lọc theo hạn giao (quá hạn, 0–30 phút, 30–60 phút, 1–2 giờ); lọc đơn trong tuyến.
- Bấm thẻ đơn mở popup: thông tin đơn, Assign driver, View details, sửa vị trí; khi đã gán thì hiện tài xế kèm menu thao tác.
- Lớp hiển thị (Trong code): giao thông trực tiếp, vùng giao hàng, tên cửa hàng, mã đơn, tên khách, giờ, ảnh và loại xe tài xế.
- Trạng thái tài xế (Trong code): Not connected, On delivery, Available.
- Heatmap có so sánh kỳ trước, khoá theo gói.

### 2.6 Tài xế và trả lương

**Danh sách:** tên, đánh giá, điện thoại, email, loại xe, hồ sơ lương, trạng thái. Tạo tài xế cần tên, điện thoại, email, mật khẩu tạm, ghi chú.

**Tuyển tài xế (Trong code):** hồ sơ đăng ký qua QR, có tài liệu; duyệt hoặc từ chối.

**Cài đặt app tài xế:**

| Nhóm | Tuỳ chọn |
|---|---|
| Phân việc | Chỉ gán tài xế online; tự nhận đơn, không có từ chối; thời gian phản hồi (mặc định 10 phút) |
| Hiển thị | Giá hàng; thu nhập trước khi nhận đơn; lộ điện thoại tài xế cho khách; lộ tên và điện thoại khách cho tài xế |
| Kiểm soát | Kiểm hàng khi lấy; bắt POD ảnh; bắt ảnh khi lấy; quét giấy tờ; tài xế tự tối ưu tuyến; geofence điểm lấy và giao |

**Lương:** 1 cấu hình mặc định và các hồ sơ riêng gán theo tài xế hoặc nhóm, có bảng ước tính thu nhập trên đơn mẫu.

| Luật lương | Cách tính |
|---|---|
| Fixed pay per delivery | Cố định mỗi chuyến |
| Order value percentage | % giá trị đơn |
| Distance-based pay | Theo khoảng cách |
| Hourly online pay | Theo giờ online |
| Pass-through earnings | Chuyển phí giao và tip cho tài xế |

**Thưởng:** theo chuyến hoặc theo giờ, có ngày bắt đầu và kết thúc, bật tắt được.

**Lương ngày:** số chuyến, lương cơ bản, tip, thu nhập ca, điều chỉnh tay, số phải trả.

### 2.7 Trang theo dõi và thông báo cho khách

| Thành phần | Chi tiết |
|---|---|
| Trang theo dõi | Trang web riêng, không cần đăng nhập: thanh 5 bước, câu trạng thái, giờ giao yêu cầu, chi tiết đơn |
| Sau khi giao | Chuyển thành form đánh giá sao riêng cho đơn và cho tài xế |
| Kênh gửi | Email; WhatsApp và SMS theo gói |
| Thời điểm gửi | Chọn được, mặc định khi tài xế nhận đơn |
| Tuỳ chọn khác | Khách sửa ghi chú giao qua link; báo trễ tự động; biên nhận kèm POD sau khi giao |

Có lỗi hiển thị nhỏ: đơn không còn tài xế thì form đánh giá ghi tên tài xế là "Not".

### 2.8 Báo cáo

| Báo cáo | Nội dung thấy được | Gói |
|---|---|---|
| Sales | Theo nguồn đơn: số đơn, tổng tiền, giá trị trung bình; tab theo khoảng cách | Mở |
| Drivers | Giờ online, hiệu suất, lương | Mở |
| Performance | Biểu đồ phân bố thời gian và % đúng giờ; bảng theo ngày: số chuyến, thời gian hứa, % đúng giờ, % lấy trong 20 phút, % giao trong 40 phút | Mở |
| Third party | Số chuyến, phí, tip, chi phí đối tác, phí quản lý, thời gian hoàn tất | Mở |
| Refund | Thời gian yêu cầu, trạng thái, lý do, số tiền, thời gian xử lý | Mở |
| Extended | Theo đơn, theo điểm lấy, đơn đã xoá. Trong code có đủ mốc giờ, người gán, độ trễ, POD | Business AI |
| Analytics | Xu hướng theo thời gian, chia theo nhân sự | Business AI |
| Heatmap | Đơn, doanh thu, khách theo khu vực, so sánh kỳ | Business AI |
| Customers | Doanh thu, chi tiêu trung bình, đánh giá theo khách | Business AI Lite |
| Connect | Hoạt động qua Shipday Connect | Chưa mở |

### 2.9 Merchant và form đặt đơn (Shipday Connect)

- **Online order forms:** form có tính tiền, form chuyển phát ngắn và chi tiết, form nhà hàng; mỗi form có link, QR, chia sẻ.
- **Merchant portal:** tab Settings, Manage Merchants (đã kết nối, danh bạ), Payments; bán năng lực giao cho cửa hàng khác. Cấu hình lịch nhận đơn, vùng phục vụ, phí cơ bản, khoảng cách đã gồm, luật giá riêng theo merchant, tip tối thiểu.
- **Invoicing:** kết nối Stripe, tạo hoá đơn có dòng hàng, tệp đính kèm, xem trước, theo dõi trạng thái.

### 2.10 Tích hợp và API

- 52 tích hợp: Ecommerce 7, POS 22, Online Ordering 33, Email 2 (một tích hợp có thể thuộc nhiều nhóm). Ví dụ Toast, Square, Uber Eats, Shopify, WooCommerce.
- Có API Credentials, webhook (Trong code), tài liệu API.
- Dịch vụ tách theo miền: API chính, báo cáo, phân tích, thanh toán.

### 2.11 AI và Marketing

| Tính năng | Nội dung | Nguồn |
|---|---|---|
| Shipday AI | Trợ lý chat trong app: đơn trễ, vị trí tài xế, tối ưu tuyến, tìm POD | Thấy trong trang, chưa dùng |
| Live Customer Support | Agent trả lời khách về đơn đang giao, chuyển người khi không xử lý được, nạp quy định và chính sách hoàn tiền | Trong code |
| AI Marketing Manager | SMS tự động theo nhóm: khách mới, quay lại, khách lớn, khách lâu không mua, đánh giá xấu, thời tiết, gần cửa hàng | Trong code |
| AI Receptionist, Voice agent | Nhận cuộc gọi, báo cáo cuộc gọi | Trong code |
| Hồ sơ khách | VIP, ghi chú, ghi chú giao hàng, món mua nhiều, chi tiêu | Trong code |
| Marketing | Chiến dịch SMS, in tờ rơi, QR, coupon | Trong code, menu không hiện ở tài khoản này |

### 2.12 Tài khoản, phân quyền, gói giá

- Nhiều tài khoản điều phối, chuyển nhanh giữa các tài khoản; mời người dùng theo vai trò (khoá gói).
- 20 ngôn ngữ, không có tiếng Việt; giao diện sáng, tối. Đơn vị mile hoặc km, chọn được tiền tệ và múi giờ.
- Mua gói và bán thêm rải khắp app: nút Upgrade cạnh tính năng khoá, chương trình giới thiệu.

| Gói | Giá từ (trả năm) | Giới hạn | Đặc trưng |
|---|---|---|---|
| Starter | Đang dùng | 300 đơn/tháng, 10 tài xế, 1 điều phối | Tự gán cơ bản |
| Professional | $39/tháng | 300 đơn, thêm $0,10/đơn; 5 nhân sự | Tuyến, tự gán, WhatsApp |
| Branded Elite | $79/tháng | 300 đơn, thêm $0,20/đơn; 15 nhân sự | Thương hiệu riêng, app riêng |
| Business AI Lite | $159/tháng | 750 đơn, thêm $0,20/đơn | Marketing, thu hút khách |
| Business AI | $319/tháng | 1.500 đơn, thêm $0,25/đơn; không giới hạn nhân sự | Geofence, phân tích nâng cao |

## 3. Đối chiếu với Invlogis

Đối chiếu theo mã trong [[docs/transport-dispatch/brainstorms/transport-dispatch.md|brainstorm Lệnh vận tải]]. Những dòng "chưa thấy" dựa trên tìm từ khoá, chưa phải kết luận feature thiếu.

| Tính năng Shipday | Invlogis | Đánh giá |
|---|---|---|
| Màn Điều phối 2 khối | Màn theo dõi xếp xe | Đã có. Tham khảo cách gán một lần bấm |
| Gán thủ công kèm số đơn đang giữ | Xếp xe, lái xe | Đã có. Thêm "số Lệnh đang giữ" nếu chưa có |
| Tự gán theo luật | F9: AI đề xuất, điều vận chốt | **Nên thêm một phần:** mượn phần tiêu chí, nhưng giữ người chốt |
| Phương án dự phòng khi không ai nhận | Chưa thấy | **Nên thêm** |
| Nhật ký gán đơn | Chưa thấy theo từ khoá | **Nên thêm** |
| Thời gian phản hồi của tài xế | Chưa thấy | **Nên xem xét** |
| Gom đơn cùng hướng | D5, D8 | Đã có, Invlogis sâu hơn (CBM, cut-off) |
| POD ảnh, ảnh khi lấy | D1, A7 | Đã có, Invlogis chặt hơn |
| Geofence | I2, E9 | Đã có, Invlogis sâu hơn |
| Báo trễ | B6, I1, I2 | Đã có, Invlogis sâu hơn |
| Trang theo dõi không cần đăng nhập cho khách | Chưa thấy | **Nên xem xét** cho khách hàng của doanh nghiệp vận tải |
| Đánh giá sau giao | Chưa thấy | Chọn lọc: có thể cho khách doanh nghiệp, không cần 2 mức sao |
| Luật lương có ước tính thu nhập | Có nhắc ở `transport-dispatch`, `vehicle-management`, `vehicle-telematics` | **Cần đối chiếu** thêm |
| Thưởng có thời hạn | Chưa thấy | Nên xem xét |
| Báo cáo % đúng giờ theo mốc | I12, B6 | Tham khảo biểu đồ phân bố |
| Cổng merchant bán năng lực giao | Chưa thấy | Không ưu tiên: khác mô hình |
| Đối tác giao ngoài, chọn theo giá | Chưa thấy | Xem xét riêng cho xe thuê ngoài, chưa làm ngay |
| Tối ưu tuyến nhiều điểm | Chưa thấy | Không phù hợp với container; có thể cho hàng lẻ |
| Tip, món ăn, catering, broadcast | — | **Không phù hợp** |
| AI receptionist, SMS marketing | — | Không phù hợp |

## 4. Đề xuất cho Invlogis (chờ duyệt)

Chỉ là đề xuất, chưa đưa vào tài liệu feature nào. Nhãn tầng theo `.claude/rules/saas-layer.md`; con số cụ thể sẽ cần mã `P-…` khi đưa vào brainstorm.

| # | Đề xuất | Tầng | Lý do |
|---|---|---|---|
| 1 | Đề xuất xe theo tiêu chí mà khách tự chọn và xếp thứ tự, điều vận chốt | `[Lõi] [Cấu hình]` | Mở rộng F9, mỗi khách có tiêu chí riêng |
| 2 | Quy tắc khi lái xe chưa nhận Lệnh quá thời gian: nhắc, trả về điều vận, hoặc đổi xe | `[Lõi] [Cấu hình]` | Tránh Lệnh treo |
| 3 | Lịch sử xếp xe trên từng Lệnh: ai xếp, xếp cho ai, đổi lúc nào, lý do | `[Lõi]` | Rõ trách nhiệm khi trễ mốc |
| 4 | Link theo dõi cho khách, không cần đăng nhập, ẩn chi phí, có hạn dùng | `[Lõi] [Cấu hình]` | Giảm cuộc gọi hỏi CS |
| 5 | Bộ công thức lương có màn ước tính trước khi lưu | `[Gói: Nhân sự] [Cấu hình]` | Dễ cấu hình, bán được cho nhiều khách |
| 6 | Mẫu khoá tính năng: vẫn hiện phần mờ kèm tên gói cần nâng | `[Lõi]` | Tham khảo cho bán gói SaaS |

**Bài học để tránh:**

- Đóng Lệnh tay phải xác nhận và ghi lý do, không được làm mất lái xe và dữ liệu đã có.
- Không để giờ yêu cầu lẫn vào cột giờ thực tế.
- Lý do thất bại nên chọn từ danh mục, để còn báo cáo được.
- Không để link theo dõi lộ dữ liệu; cần kiểm tra bảo mật riêng trước khi làm.

## 5. Công nghệ

| Hạng mục | Quan sát |
|---|---|
| Giao diện | jQuery, DataTables, controller viết tay, route dạng `#...`, gói JS tĩnh |
| Bản đồ, thanh toán | Google Maps, Stripe |
| Cập nhật dữ liệu | Polling 10 giây đến 3 phút; không thấy WebSocket trong các file đã tải (**Suy ra**) |
| Đăng nhập | JWT (Trong code) |

## Giới hạn

- Chỉ dựa trên một đơn thử, không có tải thật; hành vi khi nhiều đơn hoặc nhiều tài xế là **Chưa biết**.
- App tài xế và app quản lý **Chưa biết**. Phần mô tả tài xế lấy từ cài đặt trên web.
- Tính năng khoá gói và phần "Trong code" có thể đã bị ẩn hoặc chưa hoàn thiện. Giá và giới hạn gói ghi theo ngày xem; giới hạn lấy một phần từ file chữ và có thể khác theo thị trường.
- Không kiểm thử bảo mật và không kết luận về an toàn dữ liệu của Shipday.
- Phần đối chiếu mới soi với brainstorm `transport-dispatch` và tìm từ khoá ở vài feature khác, chưa đối chiếu toàn bộ sản phẩm.
