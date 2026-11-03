---
type: research
feature: fleetio-location-dispatch
updated: 2026-11-03
---

# Bản đồ, gán việc — Use cases

## Use cases

| UC | Tên | Actor | FR | Màn | Lỗi | OQ |
|---|---|---|---|---|---|---|
| UC-view-map | Xem đội xe | Fleet Manager | 001–009, 013, 030, 031, 035, 036 | 1.1–1.11, 1.13, 1.14 | E-001, E-002, E-014, E-015, E-016 | OQ-1, OQ-2, OQ-5, OQ-6, OQ-7, OQ-16 đã trả lời |
| UC-quick-add | Tạo bản ghi từ bản đồ | Fleet Manager | 006, 029 | 1.3 | — | — |
| UC-manage-place | Khai địa điểm, vùng | Administrator | 010, 025, 026 | 2.1–2.7 | E-010 | OQ-10 |
| UC-alert-policy | Đặt cảnh báo vùng | Administrator | 027 | 2.8 | — | OQ-12 |
| UC-job | Gán xe vào việc | Fleet Manager | 012, 014–021 | 3.1–3.9 | E-003–E-009 | OQ-13 |
| UC-job-auto | Tự gán theo vùng | Hệ thống | 011, 022 | 3.10, 3.11 | — | OQ-8, OQ-9 |
| UC-geofence-automation | Tự động hoá theo sự kiện vùng | Administrator | 011, 028 | 4.1–4.4 | E-011 | OQ-8, OQ-11 |
| UC-location-inspection | Ghi vị trí qua phiếu kiểm | Người kiểm tra xe | 004, 023, 024, 032, 033, 037 | 5.1, 5.2 | E-012 | OQ-3, OQ-4, OQ-13, OQ-17 |
| UC-location-fuel | Vị trí từ phiếu dầu, phiếu dịch vụ | Người nhập phiếu | 004, 034, 038 | 1.3, 1.12 | E-013, E-018, E-019 | OQ-3, OQ-19 |
| UC-location-history | Xem lịch sử vị trí xe | Fleet Manager | 013 | 1.12 | E-017 | OQ-18 |

Số FR, lỗi viết tắt, đầy đủ có tiền tố `fleetio-location-dispatch`.

## UC-view-map — Xem đội xe

`Chạy (vị trí giả lập)`; tìm, lọc, "Update list" lượt 3 là `Chạy`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở Fleet Map | Hiện "Map initializing..."; mở theo IP, không tự thu về xe |
| 2 | Tìm ở ô Locate, bật lớp, lọc, kéo hoặc zoom | Vẽ lớp, cập nhật Nearby sắp theo Distance, có tuổi vị trí |
| 3 | Bấm marker hoặc dòng | Không popup; panel trái đổi sang xe, marker gắn nhãn tên |
| 4 | Xem Overview, Nearby | Last Known Location có Status, Last Updated, Where, Source |
| 5 | Show Places, rê chuột dòng Place | Khoảng cách; đường nét đứt; marker xe đổi tạm thành marker Place |
| 6 | Map Options, Map Legend | Đổi nền, nhãn, lưu theo người dùng; chú giải độ tươi |

**Nhánh:** 2a Không có kết quả: E-fleetio-location-dispatch-001. 3a Xe chưa có vị trí, trên trang xe: E-fleetio-location-dispatch-002. 2b Enter ở ô tìm chọn dòng đầu, có thể nhầm nhà cung cấp: E-fleetio-location-dispatch-014. 2c Tải lại khi đang lọc, bộ lọc mất: E-fleetio-location-dispatch-015. 2d Bỏ tick "Update list when map moves" rồi kéo tay, danh sách đứng yên: E-fleetio-location-dispatch-016; chọn từ ô tìm vẫn cập nhật, tick lại là áp ngay. 2e Zoom xa: không gom cụm, marker đè nhau. 3b Xe trùng tâm Place: marker xe bị che, phải chọn từ danh sách. 6a Street View: có Pegman, không vào được. 6b Set Label Options: chọn 1 trong 5 trường làm nhãn marker xe, trường trống thì về Vehicle Name, giữ sau tải lại. 6c Use Current Map Center: dòng mở đầu đổi sang tên vùng đang xem; Reset to Default trả lại. 2f Bật tắt lớp: tắt Vehicles mất tab và marker, tắt hết ra E-fleetio-location-dispatch-001; tải lại về mặc định.

## UC-quick-add — Tạo bản ghi từ bản đồ

`Chạy (vị trí giả lập)` với Add Issue, còn lại `Xem`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Chọn xe, bấm Add | Hiện 11 mục |
| 2 | Chọn Add Issue | Form New Issue điền sẵn xe |
| 3 | Lưu | Về trang sự cố, rời bản đồ |

## UC-manage-place — Khai địa điểm, vùng

`Chạy`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Nhập tên, toạ độ | Address tự điền theo địa chỉ ngược, bản đồ tự chuyển |
| 2 | Chọn hoặc gõ bán kính | Vòng tròn đổi ngay |
| 2b | Hoặc vẽ đa giác | Toạ độ thành tâm, Address đổi, Radius khoá với giá trị tự tính |
| 3 | Save Place | "Place was successfully created"; dùng cho lọc, sự kiện, cảnh báo, việc |

**Nhánh:** 1a Bấm nhầm bản đồ: pin, Address, toạ độ đổi. 2c Đa giác 2 đỉnh: không bị chặn. 3a Rời form có thay đổi: E-fleetio-location-dispatch-010. 3b Sửa về sau: "Place was successfully updated".

## UC-alert-policy — Đặt cảnh báo vùng

`Xem`, chưa lưu vì hành động duy nhất là gửi email.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Alert Policy trên Place | Mở form |
| 2 | Chọn Trigger, xe hoặc nhóm, người nhận, nội dung | Recipients chỉ gồm người dùng có email |
| 3 | Lưu (chưa thử) | Gửi khi phát hiện, hoặc tổng hợp hằng ngày |

## UC-job — Gán xe vào việc

`Chạy`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Add Job, nhập số, tên, Place | Việc Active, có cột, Start Date/Time tự lấy |
| 2 | Tích xe, Actions, Assign, chọn giờ | Lượt Active, Added = Manual, thẻ xe đếm giờ |
| 3 | Actions, Unassign, chọn giờ | Lượt có End, xe về Unassigned |
| 4 | Menu cột, Complete, chọn giờ | Việc Completed, lượt còn chạy tự kết thúc |
| 5 | Xem Job Assignment History | Time on Job, nguồn Added |

**Nhánh:** 1a Thiếu trường: E-003. 2a Giờ tương lai: E-004. 2b Chồng khoảng cũ: E-005. 2c Xe đang có việc: E-009. 2d Kéo thả: không hoạt động. 3a Chưa bấm ô giờ: E-006. 4a Giờ trước bắt đầu: E-007. 4b Giờ tương lai: E-008.

## UC-job-auto — Tự gán theo vùng

`Chạy (vị trí giả lập)`.

| Bước | Tác nhân | Hệ thống |
|---|---|---|
| 1 | Admin bật ô tự động trên việc có Place | Auto-Tracking bật |
| 2 | Xe có lần ghi trong vùng | Lượt mới Added = Geofence, chip trên thẻ, "Current Job" đổi |
| 3 | Xe có lần ghi ngoài vùng | Lượt có End Date, Time on Job, xe về Unassigned; phiếu vừa nộp vẫn mang việc đó |

## UC-geofence-automation — Tự động hoá theo sự kiện vùng

`Chạy (vị trí giả lập)`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Automation mới, Record Type Geofence Event | Trigger Type chỉ có Created |
| 2 | Chọn điều kiện, hành động, bật | Lưu |
| 3 | Xe đi từ vùng A sang B | Chạy 2 lần, thêm 2 comment |
| 4 | Xem Run History, Run Result | Total Runs, Successful; log có thể mâu thuẫn: E-011 |
| 5 | Tắt | "Automation disabled" |

## UC-location-inspection — Ghi vị trí qua phiếu kiểm

`Chạy`, phần toạ độ giả là `Chạy (vị trí giả lập)`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở web, trình duyệt đã cho định vị | Đọc vị trí 1 lần lúc khởi động app, không báo gì |
| 2 | Nộp phiếu kiểm tra | Gửi toạ độ cấp phiếu; máy chủ lưu đúng, không kiểm |
| 3 | Xem phiếu, bản đồ | Bản đồ nhỏ, xe lên marker, Source trỏ về phiếu; địa chỉ có sau khoảng 1 phút |

**Nhánh:** 1a Trình duyệt chưa cho định vị: phiếu không có vị trí (`Suy`). 2a Đồng hồ sai theo lịch sử: E-012. 2b Biểu mẫu bật Location Exception: vẫn false trên web. 2c Phiếu dầu, dịch vụ trên web: không có ô vị trí; có nhà cung cấp thì xem UC-location-fuel. 2d Nộp trên Fleetio Go: mỗi mục có toạ độ riêng, ca không vi phạm cờ vẫn false (`Chạy (Fleetio Go)`).

## UC-location-fuel — Vị trí từ phiếu dầu, phiếu dịch vụ

`Chạy`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Mở form phiếu dầu hoặc phiếu dịch vụ, điền, chọn nhà cung cấp | Form không có ô vị trí, không báo gì |
| 2 | Lưu | Sinh Location Entry loại Fuel Entry hoặc Service Entry tại vị trí quy từ địa chỉ nhà cung cấp, cùng giờ phiếu |
| 3 | Mở Fleet Map, panel xe, Location History | Xe lên marker như đang ở địa chỉ khai; Source "Fuel Entry #..."; có dòng theo loại |

**Nhánh:** 1a Phiếu dầu không chọn nhà cung cấp: không sinh vị trí (`Suy`). 1b Phiếu dịch vụ: chỉ chọn được nhà cung cấp phân loại Service, E-fleetio-location-dispatch-013. 1c Tạo nhà cung cấp mới, Enter ở ô Country lưu luôn: E-fleetio-location-dispatch-018. 2a Địa chỉ giả: quy ra điểm ở nước khác, không báo độ tin cậy: E-fleetio-location-dispatch-019. 2b Địa chỉ không quy được: chưa thử (OQ-19).

## UC-location-history — Xem lịch sử vị trí xe

`Chạy`.

| Bước | Người dùng | Hệ thống |
|---|---|---|
| 1 | Trang xe, More, Location History | Danh sách trái có icon loại, ngày, địa chỉ; bản đồ phải; Newest First |
| 2 | Lọc Location Entry Date, Location Entry Type, tìm | Lọc theo Fuel Entry, Service Entry, Inspection |
| 3 | Sang trang | Fleetio: 30 dòng mỗi trang |

**Nhánh:** 1a Xe chưa có vị trí: E-fleetio-location-dispatch-017.
