---
type: research
keyword: "phân tích ngược app Green SM (Xanh SM)"
status: draft
updated: 2026-11-02
links: []
---

# Phân tích ngược app Green SM (Xanh SM)

> **Khuyến nghị: NÊN THAM KHẢO — chọn lọc.** Đáng học cách tách trạng thái đơn và trạng thái từng điểm, cách chia mảng thành mini app, và cách ghi rõ ai huỷ đơn. Không dùng tài liệu này làm căn cứ về thuật toán điều phối hay giá, vì phần đó không có trong dữ liệu đã đọc.

***

## Tóm tắt

Green SM là app lai: vỏ Kotlin cho đặt xe và giao hàng, các mini app Flutter cho food, xe tuyến, hỗ trợ và an toàn. Phân tích đọc được danh sách màn, enum trạng thái, chữ tiếng Việt và SDK từ bản Android 5.13.0. Thuật toán ghép tài, bán kính tìm và công thức giá chưa biết, nhiều khả năng nằm ở máy chủ. Quy tắc chuyển trạng thái trong tài liệu này là suy ra, chưa đọc code vì chưa decompile.

**Nhãn độ chắc chắn dùng trong tài liệu:**

| Nhãn | Nghĩa |
|---|---|
| **Thấy trực tiếp** | Đọc được nguyên văn trong gói: enum, tên class, tên màn, chữ trong app |
| **Suy ra** | Kết luận rút từ các dữ kiện trên, chưa kiểm chứng bằng code hay chạy thật |
| **Chưa biết** | Không có dữ liệu để trả lời |

## Nguồn phân tích

| Mục | Giá trị |
|---|---|
| App | Green SM: Electric Mobility (`com.gsm.customer`) |
| Nhà phát hành trên App Store | GSM GREEN AND SMART MOBILITY JOINT STOCK COMPANY |
| Phiên bản | 5.13.0, version code 599 (Android) |
| Ngày tải | 2026-11-02 |
| Nguồn | APKPure, gói XAPK, không phải Google Play |
| SHA-256 XAPK | `7a8543532d0fbbbe9c8dd83f7bb6f170e599076d9c1490a53e94f42cd6d48b3f` |
| SHA-256 APK chính | `821719b7b4e3affbd765dae25c5051cfc88d94c9a731d5de1bf2626e1ca3f580` |
| Cách làm | Chỉ đọc tĩnh: không chạy app, không gọi máy chủ, không trích khoá API, chưa decompile |

File gói và dữ liệu thô không lưu trong repo. Muốn phân tích lại thì phải tải lại, và APKPure có thể đã lên bản mới.

## 1. Luồng đặt xe và điều phối

### Thứ tự màn

**Suy ra** từ tên màn trong `ride_nav_graph`. File điều hướng chỉ xác nhận các màn tồn tại, chưa xác nhận thứ tự.

`RideHome` → `SelectAddress` / `SetOnMap` → `TripService` (chọn dịch vụ) → `TripAddons` → `ConfirmPickup` → `TripDetail` (theo dõi chuyến) → `CancelBooking` hoặc `HistoryDetailTrip`

### Trạng thái đơn và điểm dừng

**Thấy trực tiếp** trong enum:

| Enum | Giá trị |
|---|---|
| `OrderStatus` | `SCHEDULING`, `FINDING`, `ASSIGNED`, `IN_PROCESS`, `COMPLETED`, `CANCELLED`, `EXPIRED`, `RETURNING`, `WAITING_FOR_PAYMENT`, `PENDING_FOR_CONFIRMATION`, `FREE_TRIAL` |
| `OrderSubStatus` | `DISPATCHING`, `COMPLETING`, `RETURNING` |
| `PointStatus` (từng điểm) | `CREATED`, `ARRIVING`, `NEARED`, `ARRIVED`, `COMPLETED`, `FAILED` |
| `PointType` | `PICK_UP`, `DROP_OFF`, `RETURN`, `ROUND_TRIP`, `OVER_CHARGE`, `END_TRIP` |
| `CancelBy` | `CUSTOMER`, `DRIVER`, `MERCHANT`, `PARTNER`, `ADMIN`, `SYSTEM` |

**Suy ra**, luồng chính của đơn:

`SCHEDULING` (nếu đặt trước) → `FINDING` → `ASSIGNED` → `IN_PROCESS` → `COMPLETED`

### Các điểm đáng tham khảo

| Điểm | Dữ kiện thấy trực tiếp | Suy ra |
|---|---|---|
| Hai tầng trạng thái | `OrderStatus` và `PointStatus` là hai enum riêng | "Tài xế đang đến / sắp đến / đã đến" nhiều khả năng là trạng thái của điểm, không phải của đơn |
| Không có tài xế | Chuỗi `order-status-user-title-cancelled-expired` = "Không tìm thấy tài xế" | `EXPIRED` có vẻ là nhánh này |
| Tài xế huỷ | `driver_cancel_first_time` = "…Xanh đang tìm tài xế mới gần bạn"; `driver_cancel_trip` = "…vui lòng đặt lại chuyến mới" | Có thể app tự điều phối lại một lần |
| Mua ưu tiên | `RideInstantBookingType` gồm `NORMAL`, `SUBSCRIPTION`, `SUPER`; chữ "Ưu tiên thường", "Ưu tiên VIP", "Đảm bảo ghép tài nhanh 100%" | Khách trả thêm để được tìm xe nhanh hơn |
| Điều phối đồ ăn | `FoodDispatchType` gồm `AUTO`, `DRIVER_FIRST`, `MERCHANT_FIRST` | Có nhiều chiến lược gọi tài xế và quán |
| Đổi điểm đón | `ChangePickupInfoStatus` gồm `PROCESSING`, `SUCCESS`, `FAILED`, `UNKNOWN`; chữ "Tài xế đã đến rồi, bạn không thể đổi điểm đón!" | Đổi điểm đón có quy trình xử lý riêng và bị từ chối khi tài xế đã đến |
| Ghép chuyến | `RideShareStage` gồm `DEFAULT`, `DROPOFF_CO_RIDER_BEFORE_ME`, `PICKUP_CO_RIDER_AFTER_ME` | App báo khách biết đang đón hoặc trả khách đi cùng |
| Khứ hồi | `RoundTripStatus` gồm `OUTBOUND`, `WAITING`, `RETURN_IN_PROGRESS`, `RETURN_CANCELLED`, `COMPLETED`; chữ "Phí chờ" | Khứ hồi có trạng thái riêng và tính phí chờ |
| Vị trí tài xế | Class `DriverLocationSse…`; trạng thái `HEALTHY`, `STALE_NO_EVENTS_YET`, `STALE_NO_RECENT_EVENTS` | Dùng SSE (máy chủ đẩy dữ liệu liên tục) và có theo dõi mất tín hiệu |

### Cần kiểm chứng

App có `EDriverMovingType` (`FAKE`, `REAL`), `DriverFakeMarkerInfo` và `mirroredFakeDriver`. **Chưa biết** đây là hiệu ứng làm mượt xe trên bản đồ, chế độ thử hay thứ khác. Không kết luận gì từ riêng các tên này.

## 2. Danh sách tính năng

**Thấy trực tiếp** qua class và chữ trong gói. Có trong gói không có nghĩa là đang mở cho mọi người dùng.

| Nhóm | Nội dung |
|---|---|
| Di chuyển | Taxi, thuê theo giờ (RideHour), sân bay, GreenNow, đặt trước, đặt hộ, khứ hồi, ghép chuyến, liên tỉnh |
| Giao nhận | Express (khai báo, theo dõi, đổi điểm giao, bảo hiểm, COD) và Food |
| Xe tuyến (mini app) | VinBus, xe đưa đón học sinh (có Face ID), Shuttle |
| Tài khoản | Gia đình, doanh nghiệp, xác minh sinh viên, eKYC, VNeID, chế độ đơn giản |
| Tiền và ưu đãi | Ví, thẻ doanh nghiệp, thẻ quà tặng, gói hội viên, hạng thành viên, VPoint, giới thiệu bạn bè, nợ cước, hoá đơn |
| An toàn và hỗ trợ | Trung tâm an toàn, SOS, RideCheck, Camera S2S, trung tâm hỗ trợ |
| Khác | Tìm kiếm toàn app, khám phá, hướng dẫn địa phương, đóng góp bản đồ, Live Activity |

App có 32 đồ thị điều hướng, 9.518 chuỗi tiếng Việt và 13 file ngôn ngữ (12 file đầy đủ, `ch.json` chỉ có 489 chuỗi).

## 3. Công nghệ và SDK

**Thấy trực tiếp** qua class và thư viện native, trừ các chỗ ghi chú trong bảng.

| Mảng | Thành phần |
|---|---|
| Kiến trúc | App lai: vỏ Kotlin (có Jetpack Compose) cho đặt xe và giao hàng, mini app Flutter cho food, bus, hỗ trợ, an toàn. Mini app nằm sẵn trong gói. Toàn bộ có 62.888 class |
| Bản đồ | SDK riêng `net.gsm.maps`, lớp `dmp` với provider Google, GSM, Huawei, cùng MapLibre và 2GIS. Thư viện 2GIS là file lớn nhất, 67 MB |
| Mạng | Retrofit, OkHttp, Moshi; Dio cho phần Flutter. Có gRPC, chưa rõ do app hay SDK khác dùng |
| Gọi điện trong app | Infobip WebRTC, PJSIP, CiCare |
| eKYC | FPT FCI, VinBigData (khuôn mặt), ML Kit, TensorFlow Lite |
| Đo lường | AppsFlyer, CleverTap, Snowplow, Firebase |
| Khác | Google Pay, HMS cho máy Huawei, SQLCipher, vài thư viện native tên ngẫu nhiên (có thể là lớp bảo vệ, chưa xác nhận) |

## 4. Gợi ý cho Delta Super App

Đây là ý kiến của người phân tích, chưa phải quyết định hay yêu cầu.

- **Tách trạng thái đơn và trạng thái điểm:** rất hợp với vận tải nhiều điểm.
- **Dùng mini app cho từng mảng:** hợp với hướng super app nhiều bên.
- **Lưu `CancelBy`, tách `EXPIRED` khỏi `CANCELLED`:** báo cáo sẽ rõ nguyên nhân hơn.
- **Cẩn thận với chữ "tenant":** ở Green SM nó có vẻ là quốc gia hoặc thị trường (chuỗi `multitenant_*`, màn chọn quốc gia), không phải khách SaaS như Invlogis, nên đừng lấy nguyên mô hình.

## Giới hạn

| Hạng mục | Tình trạng |
|---|---|
| Thuật toán ghép tài, bán kính, công thức giá | Chưa biết, không thấy trong dữ liệu đã đọc |
| Quy tắc chuyển trạng thái | Suy ra, chưa đọc code; vị trí của `RETURNING`, `FREE_TRIAL`, `PENDING_FOR_CONFIRMATION` chưa rõ |
| Giao diện thật và bản iOS | Chưa xem, bản iOS có thể khác Android |
| Nguồn gói | Tải từ APKPure, không phải Google Play. Chứng chỉ khai báo là "Android / Google Inc." từ 2023-03-19, hợp với kiểu ký qua Play App Signing, nhưng chữ ký chưa được xác thực |
| Sử dụng | Chỉ nên dùng để tham khảo thiết kế. Nếu dùng cho mục đích thương mại, cần xem lại điều khoản của Green SM |
