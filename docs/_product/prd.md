---
type: prd-product
status: draft
updated: 2026-10-13
links:
  - docs/_shared/project-profile.md
  - docs/_shared/system-overview.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_product/tenant-parameters.md
  - docs/_product/srs-v2-change-log.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/cross-process-flow/brainstorms/cross-process-flow.md
---

# Invlogis — Product Requirements Document (project-level)

## 1. One-line Pitch

Nền tảng vận hành cho doanh nghiệp vận tải và logistics ở Việt Nam: các module điều vận, xưởng, dầu, công nợ – thanh toán – hoá đơn, nhân sự dùng chung một dữ liệu, để mỗi lô hàng và mỗi đầu xe được theo từ chứng từ khách tới chi phí, doanh thu, công nợ mà không nhập lại.

## 2. Problem & Why Now

Doanh nghiệp giao nhận, vận tải container vận hành bằng Excel, Zalo và giấy tờ. Dữ liệu một lô hàng nằm rải ở nhiều người, nhiều file; chi phí dọc đường về chậm theo chứng từ giấy. Lãnh đạo không biết lô nào lãi, lô nào lỗ, việc nào sắp trễ mốc cho tới khi đã muộn.

* __Vấn đề cốt lõi:__ (a) nhập lại cùng một dữ liệu nhiều lần; (b) giao việc hiện trường qua Zalo, không tra lại được; (c) quá mốc thời gian bị phạt lưu container, lưu vỏ; (d) chứng từ giấy về chậm; (e) chi phí chưa được hạch toán rõ ràng, đầy đủ. Năm vấn đề này Delta đã xác nhận.
* __Ai đang đau:__ Lãnh đạo doanh nghiệp — người chịu kết quả lãi lỗ nhưng phải gọi hỏi từng người để biết tình hình.
* __Giải pháp thay thế hiện tại:__ Excel, Zalo, giấy tờ.
* __Why now:__ Đã có khách hàng đầu tiên chạy thật (Delta, ~110.000 lô hàng/năm, tăng 2 con số mỗi năm); AI đọc chứng từ đã đủ dùng để bỏ khâu nhập tay; công ty chuyển hướng từ làm outsource sang bán sản phẩm (từ 2026-10-12). Cần xác nhận thêm tín hiệu thị trường (OQ-2).

## 3. Target Users

Khách hàng mua sản phẩm: doanh nghiệp giao nhận và vận tải container ở Việt Nam, có đội xe riêng, nhiều chi nhánh, khoảng 10.000–200.000 lô hàng/năm. Delta là khách hàng đầu tiên.

| Nhóm người dùng | Vai trò (primary/secondary) | Job-to-be-done | Bối cảnh sử dụng |
|---|---|---|---|
| Lãnh đạo | Primary (người mua, đau nhất) | Biết lô nào lãi, lỗ, tiền đang kẹt ở đâu, việc nào sắp trễ mốc, không phải gọi hỏi từng người | Xem trên điện thoại hoặc máy tính, đầu và cuối ngày |
| CS | Primary | Mở hồ sơ dịch vụ từ chứng từ khách một lần, theo tới khi giao xong | Web cả ngày, áp lực mốc cảng và hạn lưu container |
| Điều vận | Primary | Xếp xe, xếp lái đúng mốc, biết ngay khi có sự cố | Web cả ngày, áp lực mốc cảng |
| Hiện trường, lái xe | Primary | Nhận việc, làm việc, chụp chứng từ, ghi chi phí ngay tại chỗ, không cần giấy và Zalo | App ngoài đường, ở cảng, bãi; có lúc mất sóng |
| Kế toán | Primary | Có chi phí, doanh thu đủ và đúng theo từng lô để làm bảng kê, công nợ, hoá đơn | Web, theo kỳ chốt |
| Quản lý phương tiện, quản lý xưởng, quản lý cây dầu | Secondary | Biết xe nào sẵn sàng; chi phí sửa chữa, nhiên liệu theo đầu xe | Web |
| Nhân viên xưởng, nhân viên kho xưởng, nhân viên cây dầu, nhân viên đối tác cây dầu, nhân sự | Secondary (theo gói) | Làm nghiệp vụ xưởng, kho, cấp dầu, hồ sơ nhân viên trên cùng dữ liệu phương tiện | Web; app cho cấp dầu |
| Admin của khách | Secondary | Quản lý tài khoản, quyền, danh mục của doanh nghiệp mình | Web |

*Ai KHÔNG phải người dùng: sàn ghép xe tải lẻ, hãng tàu, cảng; chủ hàng không tự đặt dịch vụ trên sản phẩm.*

## 4. Value Proposition & Differentiator

* __Giá trị cốt lõi (1 câu):__ Lãnh đạo thấy lãi lỗ và rủi ro trễ mốc của từng lô hàng gần như ngay khi việc xảy ra, vì mọi dữ liệu chỉ nhập một lần ngay tại nơi phát sinh.
* __Vì sao chọn mình thay vì giải pháp cũ:__
  * Bớt nhập lại: chứng từ khách được AI đọc thẳng vào hồ sơ dịch vụ, dữ liệu chảy tiếp sang điều phối, lệnh vận tải, thanh toán.
  * Giao việc và bằng chứng trên app thay Zalo: ai nhận việc gì, làm tới đâu, ảnh chứng từ ở đâu đều tra lại được.
  * Chi phí, doanh thu tự gắn đúng lô hàng: kế toán không chờ giấy về rồi gom tay.
* __Lợi thế khác biệt:__
  * Làm riêng cho thực tế cảng Việt Nam: 6 mẫu quy trình FCL, LCL/CFS, air × xuất, nhập; danh mục cảng, bãi Việt Nam có thuộc tính ePort dùng chung mọi khách; AI đọc chứng từ Việt Nam (Booking Note, eDO, EIR, phiếu cân, tờ khai có QR).
  * Nhiều module chung một dữ liệu (điều vận, xưởng, dầu, công nợ): mỗi đầu xe và mỗi lô hàng có giá thành thật, điều phần mềm chỉ làm điều vận hoặc chỉ làm kế toán không có.
  * Cấu hình theo khách không sửa code: tham số, tên gọi, danh mục, bật/tắt gói.
  * App chạy khi mất sóng, hợp với lái xe ở cảng và trên đường.
  * Đã chạy thật ở quy mô Delta (~110.000 lô/năm) — có khách tham chiếu khi bán.
* __Khoảng trống đã biết:__ v1 cung cấp dữ liệu chi phí, doanh thu đúng JobID và cây quy trình; màn xem lãi lỗ theo lô, theo đầu xe cho lãnh đạo chưa có feature (OQ-3). Đây là khoảng trống lớn nhất giữa giá trị cốt lõi và phạm vi hiện tại.

## 5. Goals & Non-Goals

__Mục tiêu (in-scope):__
* Phân hệ Điều phối vận tải chạy thật tại Delta: JobID từ chứng từ khách → điều phối việc cảng, bãi → Lệnh vận tải → chi phí về đúng JobID.
* Các module đã có trong SRS v2.0 chạy trên cùng dữ liệu: Phương tiện và Quản trị thuộc lõi; Xưởng, Cây dầu, Nhân sự đóng gói thành gói bán thêm.
* Lõi sản phẩm không chứa quy tắc riêng Delta: mọi con số, danh sách, bật/tắt đi qua tham số theo khách.

__Ngoài phạm vi (non-goals / out-of-scope):__
* Không làm phần mềm kế toán đầy đủ: có ghi nhận chi phí, doanh thu, công nợ theo chứng từ và xuất dữ liệu; không làm sổ cái, bút toán, báo cáo thuế. Cách chuyển dữ liệu sang phần mềm kế toán của khách chưa chốt (OQ-6).
* Không kết nối máy với ePort cảng; phần mềm hỗ trợ danh sách việc ePort và lưu kết quả.
* Không làm sàn ghép hàng, ghép xe cho bên ngoài; không làm app cho chủ hàng tự đặt dịch vụ. Việc khách của doanh nghiệp tự theo dõi lô hàng chưa chốt (OQ-14).
* Không sửa lõi riêng cho một khách; yêu cầu riêng đi qua cấu hình, gói hoặc kết nối riêng.

## 6. Capability Themes

| Theme | Mô tả | Features thuộc theme |
|---|---|---|
| Nền dùng chung (Lõi) | Tài khoản, phân quyền, thao tác chung, liên quy trình, nhắc việc, trợ giúp | `account-access`, `access-control`, `common-workspace`, `cross-process-flow`, `reminders`, `help-center` |
| Điều phối vận tải (Lõi) | Từ chứng từ khách tới Lệnh vận tải hoàn tất, chi phí về đúng JobID | `service-delivery`, `shipment-coordination`, `transport-dispatch` |
| Phương tiện (Lõi) | Hồ sơ phương tiện, bàn giao, thu hồi — dữ liệu nối điều vận với xưởng và dầu | `vehicle-management` |
| Xưởng (Gói Bảo dưỡng đội xe) | Danh mục kỹ thuật, mua hàng, kho phụ tùng, sửa chữa, thanh toán, báo cáo xưởng | `workshop-catalog`, `workshop-partners`, `purchasing`, `stock-movement`, `inventory-count`, `repair-order`, `incident-report`, `workshop-payment`, `service-sales-payment`, `workshop-reports` |
| Cây dầu (Gói Nhiên liệu) | Định mức nhiên liệu, mua nhập dầu, cấp dầu, thanh toán cây dầu | `fuel-allowance`, `fuel-purchase`, `fuel-issuing`, `fuel-payment`, `fuel-stations` |
| Nhân sự (Gói Nhân sự) | Hồ sơ nhân viên, cấp mới, cho nghỉ | `employee-records` |

Gói gắn kèm bên trong feature lõi (bật theo khách): Đa chi nhánh (giao dịch nội bộ trong `service-delivery`), Tài chính (kết nối ngân hàng cho thanh toán trả hộ), Đường sắt, CBT, Hàng lạnh (trong `transport-dispatch`). Danh sách gói đang lệch với `saas-core-vs-tenant.md` (chưa có gói Nhân sự; tầng của định mức nhiên liệu) — OQ-13.

## 7. Feature Map

### Luồng người dùng tổng quan

__Hành trình Điều phối vận tải (CS, hiện trường, điều vận, lái xe, kế toán):__
1) Người dùng đăng nhập, vào đúng chi nhánh theo quyền → `account-access`, `access-control`
2) CS mở JobID từ chứng từ khách, AI đọc và điền sẵn → `service-delivery`
3) CS và hiện trường làm việc cảng, bãi theo luồng hàng trên app, sinh yêu cầu vận tải → `shipment-coordination`
4) Điều vận lập Lệnh vận tải trên xe của đội; lái xe chạy Lệnh, chụp chứng từ, ghi chi phí → `transport-dispatch`, `vehicle-management`
5) Chi phí, doanh thu về đúng JobID, sẵn cho bảng kê và thanh toán → `service-delivery`
6) Ai cũng xem được cả chuỗi quy trình từ một bản ghi bất kỳ → `cross-process-flow`

__Hành trình Xưởng – Dầu (quản lý phương tiện, xưởng, cây dầu):__
1) Phương tiện được bàn giao cho lái xe → `vehicle-management`
2) Lái xe báo sự cố; xưởng lập lệnh sửa chữa → `incident-report`, `repair-order`
3) Xưởng mua hàng hoá dịch vụ, nhập và xuất kho phụ tùng → `purchasing`, `stock-movement`
4) Thanh toán nhà cung cấp → `workshop-payment`
5) Cây dầu cấp dầu cho xe theo định mức → `fuel-allowance`, `fuel-issuing`
6) Quản lý xem báo cáo xưởng và dashboard cây dầu → `workshop-reports`, `fuel-stations`

Ngoài 2 hành trình chính (back-office, quản trị): `common-workspace`, `reminders`, `help-center` dùng xuyên suốt; `workshop-catalog`, `workshop-partners`, `inventory-count`, `service-sales-payment`, `fuel-purchase`, `fuel-payment`, `employee-records` là việc hậu cần định kỳ của xưởng, cây dầu, nhân sự.

### Bảng Feature Map

| # | Tính năng | Slug | Theme | Persona | Ưu tiên (MoSCoW) | Phụ thuộc | Chi tiết hóa |
|---|---|---|---|---|---|---|---|
| 1 | Đăng nhập và quản lý tài khoản cá nhân | `account-access` | Nền dùng chung | Mọi người dùng | Must | — | ⬜ chưa |
| 2 | Quản lý tài khoản, nhóm quyền và phân quyền | `access-control` | Nền dùng chung | Admin | Must | `account-access` | ⬜ chưa |
| 3 | Dùng màn Home và thao tác chung trên danh sách | `common-workspace` | Nền dùng chung | Mọi người dùng | Must | `access-control` | ⬜ chưa |
| 4 | Xem quy trình liên nghiệp vụ dạng cây | `cross-process-flow` | Nền dùng chung | Mọi người dùng | Must | `access-control`; mềm: mỗi module đăng ký quy trình của mình | ✅ đã chi tiết (1 brainstorm, đang stale) |
| 5 | Đặt và nhận lịch nhắc | `reminders` | Nền dùng chung | Mọi người dùng | Should | `access-control` | ⬜ chưa |
| 6 | Tra cứu câu hỏi thường gặp và hướng dẫn sử dụng | `help-center` | Nền dùng chung | Mọi người dùng | Could | `account-access` | ⬜ chưa |
| 7 | Mở hồ sơ dịch vụ (JobID) từ chứng từ khách | `service-delivery` | Điều phối vận tải | CS, Kế toán | Must | `access-control` | ✅ đã chi tiết (1 brainstorm) |
| 8 | Điều phối việc cảng, bãi theo luồng hàng | `shipment-coordination` | Điều phối vận tải | CS, Hiện trường | Must | `service-delivery`, `access-control` | ✅ đã chi tiết (1 brainstorm) |
| 9 | Lập và chạy Lệnh vận tải | `transport-dispatch` | Điều phối vận tải | Điều vận, Lái xe | Must | `shipment-coordination`, `vehicle-management` | ✅ đã chi tiết (1 brainstorm) |
| 10 | Quản lý phương tiện, bàn giao và thu hồi | `vehicle-management` | Phương tiện | Quản lý phương tiện, Lái xe | Must | `access-control` | ⬜ chưa |
| 11 | Quản lý danh mục kỹ thuật xưởng | `workshop-catalog` | Xưởng | Nhân viên xưởng | Should | `access-control` | ⬜ chưa |
| 12 | Quản lý nhà cung cấp, khách hàng và xe của khách hàng | `workshop-partners` | Xưởng | Nhân viên xưởng | Should | `access-control` | ⬜ chưa |
| 13 | Mua và báo giá hàng hoá dịch vụ | `purchasing` | Xưởng | Nhân viên xưởng | Should | `workshop-catalog`, `workshop-partners` | ⬜ chưa |
| 14 | Nhập và xuất kho phụ tùng | `stock-movement` | Xưởng | Nhân viên kho xưởng | Should | `purchasing` | ⬜ chưa |
| 15 | Kiểm kê tồn kho, tồn xưởng, thanh lý rác thải | `inventory-count` | Xưởng | Nhân viên kho xưởng | Should | `stock-movement` | ⬜ chưa |
| 16 | Lập và theo dõi lệnh sửa chữa | `repair-order` | Xưởng | Nhân viên xưởng | Should | `vehicle-management`, `stock-movement`; mềm: `incident-report` | ⬜ chưa |
| 17 | Báo cáo sự cố phương tiện | `incident-report` | Xưởng | Lái xe, Nhân viên xưởng | Should | `vehicle-management` | ⬜ chưa |
| 18 | Thanh toán mua hàng và bồi thường | `workshop-payment` | Xưởng | Kế toán, Nhân viên xưởng | Should | `purchasing` | ⬜ chưa |
| 19 | Thu tiền bán hàng hoá dịch vụ | `service-sales-payment` | Xưởng | Kế toán | Should | `workshop-partners`, `stock-movement`, `repair-order` | ⬜ chưa |
| 20 | Xem báo cáo và dashboard xưởng | `workshop-reports` | Xưởng | Lãnh đạo, Quản lý xưởng | Should | `repair-order`, `purchasing`, `stock-movement`, `inventory-count`, `workshop-payment` | ⬜ chưa |
| 21 | Đặt định mức khoán nhiên liệu phương tiện | `fuel-allowance` | Cây dầu | Quản lý phương tiện | Should | `vehicle-management` | ⬜ chưa |
| 22 | Lập kế hoạch mua và nhập dầu | `fuel-purchase` | Cây dầu | Nhân viên cây dầu | Should | `fuel-stations` | ⬜ chưa |
| 23 | Cấp dầu cho phương tiện | `fuel-issuing` | Cây dầu | Nhân viên cây dầu, Nhân viên đối tác cây dầu | Should | `fuel-allowance`, `fuel-stations` | ⬜ chưa |
| 24 | Thanh toán trả sau cây dầu | `fuel-payment` | Cây dầu | Kế toán | Should | `fuel-issuing` | ⬜ chưa |
| 25 | Quản lý cây dầu và xem dashboard cây dầu | `fuel-stations` | Cây dầu | Quản lý cây dầu | Should | `access-control` | ⬜ chưa |
| 26 | Cấp mới và cho nghỉ nhân viên | `employee-records` | Nhân sự | Nhân sự | Should | `access-control` | ⬜ chưa |

Ưu tiên tính cho bản thí điểm Điều phối vận tải với Delta. Should của Xưởng, Cây dầu, Nhân sự là gói bán thêm Delta bật sẵn, chưa có mốc trong 6 tháng đầu; thứ tự giữa các gói chốt cùng OQ-4.

Chưa có trong Feature Map (chưa có SRS): xem lãi lỗ theo lô cho lãnh đạo (OQ-3); bảng kê, công nợ, hoá đơn điện tử, thanh toán trả hộ của Điều phối (OQ-6); cấu hình theo khách và khởi tạo khách mới — điều kiện để bán SaaS, phải chốt trước mốc 12 tháng (OQ-7); danh mục khách hàng, báo giá, hợp đồng và hồ sơ lái xe dùng chung (OQ-11). North Star Mục 8 phụ thuộc nhóm OQ-6.

### 7.1 Đăng nhập và quản lý tài khoản cá nhân — `account-access`

Người dùng đăng nhập vào web và app, khôi phục hoặc đổi mật khẩu, xem thông tin cá nhân. Đây là cửa vào chung của mọi module; được cấp nhiều chi nhánh thì chọn chi nhánh trước khi vào Home.

__Phục vụ job:__ Feature nền — hỗ trợ mọi nhóm người dùng ở Mục 3.

__Phạm vi v1:__ Đăng nhập, quên mật khẩu, đăng xuất, đổi mật khẩu, tạo mật khẩu mới, xem thông tin cá nhân (UC01.01–01.06).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: có cần đăng nhập một lần (SSO) với hệ thống của khách SaaS không]

__Luồng chính:__
1) Người dùng nhập tài khoản, mật khẩu.
2) Được cấp nhiều chi nhánh thì chọn chi nhánh.
3) Vào màn Home theo quyền.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ khi nhiều khách SaaS dùng chung cửa đăng nhập] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd số yêu cầu hỗ trợ quên mật khẩu mỗi tháng]
__OQ riêng:__ OQ-9

### 7.2 Quản lý tài khoản, nhóm quyền và phân quyền — `access-control`

Admin của khách tạo tài khoản, lập nhóm quyền và gán quyền chức năng theo nền tảng, phạm vi chi nhánh, cơ sở. Quyền theo chức năng chứ không theo vai trò cố định, để mỗi khách tự ghép quyền đúng chức danh của mình. Không có quyền thì không thấy tính năng; nút không có quyền thì ẩn.

__Phục vụ job:__ Feature nền — hỗ trợ Admin của khách; mọi job ở Mục 3 dựa vào phân quyền đúng.

__Phạm vi v1:__ Quản lý tài khoản, nhóm quyền, thay đổi phân quyền chức năng (UC13.01–13.02, UC02.02.01); phạm vi Công ty → Chi nhánh → Cơ sở. Cơ chế quyền có thời hạn gắn bản ghi hoặc ca trực là lõi, thuộc feature này; `shipment-coordination` chỉ dùng cơ chế. Tài khoản chỉ được tạo ở đây; `employee-records` gọi sang.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: có cần đăng nhập bằng tài khoản của hệ thống khách (SSO) không]

__Luồng chính:__
1) Admin tạo nhóm quyền, chọn quyền chức năng theo nền tảng.
2) Admin tạo tài khoản, gán nhóm quyền và phạm vi chi nhánh, cơ sở.
3) Người dùng đăng nhập chỉ thấy tính năng và dữ liệu trong phạm vi được cấp.

__Rủi ro chính:__ Cấp sai phạm vi làm người chi nhánh này thấy dữ liệu chi nhánh khác · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd thời gian Admin của khách mới tự thiết lập xong phân quyền]
__OQ riêng:__ OQ-9

### 7.3 Dùng màn Home và thao tác chung trên danh sách — `common-workspace`

Các thao tác dùng chung mọi module: màn Home chọn phạm vi, lưu nháp bản ghi, xuất chi tiết, xuất danh sách, xuất báo cáo, nhập dữ liệu, thao tác hàng loạt, định dạng mã bản ghi. Làm một lần, mọi module dùng lại, để giao diện và cách làm nhất quán.

__Phục vụ job:__ Feature nền — giúp mọi nhóm người dùng làm nhanh hơn trên danh sách lớn.

__Phạm vi v1:__ UC00.00.01, UC00.00.04–00.00.11 theo SRS v2.0 và quy tắc giao diện chung đã chuẩn hoá.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: thông báo trong app có thuộc feature này không]

__Luồng chính:__
1) Người dùng vào Home, chọn module, cơ sở.
2) Lọc, chọn nhiều bản ghi trên danh sách.
3) Thực hiện thao tác hàng loạt hoặc xuất dữ liệu.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ khi nhập dữ liệu hàng loạt sai] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.4 Xem quy trình liên nghiệp vụ dạng cây — `cross-process-flow`

Từ bất kỳ bản ghi nào thuộc một quy trình nhiều nghiệp vụ, người dùng mở được sơ đồ cây toàn bộ bước chính, nhánh phát sinh, liên module, công nợ; chọn một bước để xem trạng thái và mở màn chi tiết. Thay thanh tiến trình tuyến tính của SRS cũ vốn không vẽ được nhánh lồng nhau. Kèm màn danh sách theo dõi mọi quy trình đang chạy.

__Phục vụ job:__ Lãnh đạo, CS, điều vận — biết một việc đang ở đâu trong cả chuỗi mà không phải hỏi.

__Phạm vi v1:__ Theo brainstorm `cross-process-flow` (đã có SRS và màn Figma): cây quy trình web và mobile, tạo nghiệp vụ tiếp theo, danh sách quy trình.
__Chưa làm:__ Bảng phát sinh của Điều phối vận tải — bổ sung khi chốt quy trình với khách. Bản thí điểm chỉ cần 3 feature điều phối đăng ký quy trình.

__Luồng chính:__
1) Người dùng mở chi tiết một bản ghi.
2) Mở dòng quy trình, xem cây các bước.
3) Chọn một bước, xem trạng thái, mở màn chi tiết bước đó.

__Rủi ro chính:__ Mỗi module khai báo quy trình một kiểu, cây hiển thị không nhất quán · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd số cuộc gọi hỏi tình trạng việc giảm]
__OQ riêng:__ —

### 7.5 Đặt và nhận lịch nhắc — `reminders`

Người dùng đặt lịch nhắc cho việc định kỳ hoặc việc có hạn và nhận nhắc trên web, app. Giúp không bỏ sót việc đến hạn khi chưa có luồng tự động.

__Phục vụ job:__ Mọi nhóm người dùng — không bỏ sót việc đến hạn.

__Phạm vi v1:__ Lịch nhắc theo UC08.04.
__Chưa làm:__ Cảnh báo mốc container, quá mốc — thuộc `shipment-coordination` và `transport-dispatch`; feature này chỉ nhắc do người dùng tự đặt.

__Luồng chính:__
1) Người dùng tạo lịch nhắc, chọn thời điểm.
2) Đến hạn, hệ thống nhắc.
3) Người dùng xử lý và đóng nhắc.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.6 Tra cứu câu hỏi thường gặp và hướng dẫn sử dụng — `help-center`

Người dùng tự tra câu hỏi thường gặp và hướng dẫn sử dụng ngay trong sản phẩm. Với SaaS nhiều khách, đây là cách giảm tải hỗ trợ khi khách mới bắt đầu dùng.

__Phục vụ job:__ Feature nền — hỗ trợ mọi người dùng tự học cách dùng.

__Phạm vi v1:__ FAQs và hướng dẫn sử dụng (UC09.01–09.02).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: nội dung hướng dẫn dùng chung mọi khách hay mỗi khách tự soạn]

__Luồng chính:__
1) Người dùng mở trợ giúp.
2) Tìm câu hỏi hoặc hướng dẫn.
3) Đọc và làm theo.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd số yêu cầu hỗ trợ trên mỗi khách]
__OQ riêng:__ OQ-9

### 7.7 Mở hồ sơ dịch vụ (JobID) từ chứng từ khách — `service-delivery`

JobID là xương sống mọi dịch vụ (hải quan, vận tải, thủ tục chuyên ngành, giá trị gia tăng). CS tạo JobID một lần từ chứng từ khách, AI đọc chứng từ điền sẵn, người tạo duyệt. Mọi việc làm sau đó ở Điều phối và Điều vận đều kéo chi phí, doanh thu về đúng JobID, để khi dịch vụ xong thì bảng kê, công nợ và hạch toán nội bộ đã sẵn sàng.

__Phục vụ job:__ CS — mở hồ sơ một lần; Kế toán — chi phí, doanh thu đủ theo lô; Lãnh đạo — có dữ liệu chi phí, doanh thu theo lô làm nền cho báo cáo lãi lỗ (OQ-3).

__Phạm vi v1:__ Theo brainstorm `service-delivery`: tạo, duyệt JobID từ chứng từ; chi phí trên JobID (tạm ứng theo ngưỡng, yêu cầu thanh toán); hoá đơn điện tử, hoá đơn trả hộ; giao dịch nội bộ liên chi nhánh (gói Đa chi nhánh).
__Chưa làm:__ Duyệt thanh toán, QR, uỷ nhiệm chi, kết nối ngân hàng (thuộc feature "Thanh toán trả hộ", chưa có trong Feature Map — OQ-6). Danh mục khách hàng, báo giá, hợp đồng mà bước 1 cần chưa có feature sở hữu (OQ-11). Feature đang lớn hơn cỡ một brainstorm, có thể tách (OQ-15).

__Luồng chính:__
1) CS chọn khách hàng, báo giá/hợp đồng, loại JobID.
2) CS tải chứng từ khách, AI đọc và điền sẵn.
3) CS duyệt, JobID được tạo.
4) Điều phối, Điều vận làm việc; chi phí, doanh thu về JobID.
5) Dịch vụ hoàn thành, JobID sẵn cho bảng kê và công nợ.

__Rủi ro chính:__ AI đọc chứng từ sai nhiều, CS vẫn phải sửa tay · __Đo thành công:__ % JobID tạo từ AI đọc chứng từ không nhập tay (mục tiêu ≥ 70% sau 6 tháng)
__OQ riêng:__ OQ-6, OQ-11, OQ-15

### 7.8 Điều phối việc cảng, bãi theo luồng hàng — `shipment-coordination`

Dữ liệu đi liền từ JobID sang yêu cầu vận tải, không nhập lại. CS kê khai một lần, phần mềm phân luồng theo loại hàng và thuộc tính cảng, bãi: CS tự làm trên ePort, giao việc cho hiện trường, hoặc sinh yêu cầu vận tải ngay. Việc hiện trường được giao, nhận, chụp chứng từ trên app; mỗi việc kéo theo chi phí định mức và quyền thanh toán đúng người, đúng JobID.

__Phục vụ job:__ CS, Hiện trường — giao và làm việc cảng, bãi trên app thay Zalo; Lãnh đạo — biết việc nào sắp trễ mốc.

__Phạm vi v1:__ Theo brainstorm `shipment-coordination`: 6 luồng hàng, danh mục cảng/bãi 3 thuộc tính, AI đọc Booking Note/eDO/EIR/phiếu cân, quét QR tờ khai, giao việc và chuyển việc, gợi ý người nhận việc, ca trực.
__Chưa làm:__ Kết nối máy với ePort.

__Luồng chính:__
1) JobID được duyệt, CS kê khai việc cảng, bãi.
2) Phần mềm phân luồng theo loại hàng và thuộc tính cảng, bãi.
3) Việc hiện trường được giao, người nhận làm và chụp chứng từ trên app.
4) Sinh yêu cầu vận tải đủ dữ liệu cho Điều vận.

__Rủi ro chính:__ Hiện trường vẫn nhận việc qua Zalo, không dùng app · __Đo thành công:__ % việc hiện trường giao và nhận trên app (mục tiêu ≥ 90% sau 6 tháng)
__OQ riêng:__ OQ-15

### 7.9 Lập và chạy Lệnh vận tải — `transport-dispatch`

Điều vận nhận yêu cầu vận tải đủ dữ liệu, lập Lệnh trên một màn theo dõi xếp xe; lái xe chạy Lệnh trên app: chụp ảnh tại điểm, ghi chi phí, lập biên bản giao hàng, báo vấn đề giữa chặng. Lệnh lưu cả kế hoạch và thực tế; quá mốc thì cảnh báo, leo thang. Lệnh duyệt xong thì chi phí đã nằm đúng JobID.

__Phục vụ job:__ Điều vận — xếp xe đúng mốc, biết ngay sự cố; Lái xe — làm việc và ghi chi phí tại chỗ; Lãnh đạo — rủi ro trễ mốc.

__Phạm vi v1:__ Theo brainstorm `transport-dispatch`: Lệnh theo FCL, LCL, CFS, air; ảnh định vị tại các điểm bắt buộc (danh sách điểm cấu hình theo loại hàng); biên bản giao hàng điện tử chạy khi mất sóng; cảnh báo quá mốc; chi phí dọc đường; báo vấn đề giữa chặng; cấp dầu trên Lệnh gắn định mức phương tiện. Gói Đường sắt, CBT, Hàng lạnh bật theo khách.
__Chưa làm:__ Điều phối Lệnh có AI đề xuất xe (P2); gợi ý hàng chiều về cho CBT. Cấp dầu ngoài Lệnh và bù dầu thuộc `fuel-issuing`.

__Luồng chính:__
1) Điều vận nhận yêu cầu vận tải, lập Lệnh, chọn xe và lái xe.
2) Lái xe nhận Lệnh trên app, chạy tới từng điểm, chụp ảnh.
3) Lái xe ghi chi phí, lập biên bản giao hàng.
4) Có vấn đề thì báo giữa chặng; quá mốc thì cảnh báo.
5) Điều vận duyệt Lệnh, chi phí về JobID.

__Rủi ro chính:__ Lái xe vẫn gửi ảnh và chi phí qua Zalo · __Đo thành công:__ % Lệnh hoàn thành có đủ ảnh và biên bản giao hàng (mục tiêu ≥ 95% sau 6 tháng)
__OQ riêng:__ OQ-5, OQ-15

### 7.10 Quản lý phương tiện, bàn giao và thu hồi — `vehicle-management`

Hồ sơ phương tiện của doanh nghiệp (đầu kéo, xe tải, mooc), cập nhật thông tin chung, bàn giao và thu hồi phương tiện cho lái xe. Đây là dữ liệu nối Điều vận (xe chạy Lệnh) với Xưởng (sửa chữa) và Cây dầu (định mức, cấp dầu), để mỗi đầu xe có giá thành thật.

__Phục vụ job:__ Điều vận — biết xe nào sẵn sàng; Lãnh đạo — chi phí theo đầu xe.

__Phạm vi v1:__ Danh sách, chi tiết, cập nhật phương tiện, hàng hoá và thiết bị, duyệt cập nhật, lịch sử thay đổi (UC04.00.01–04, UC04.00.06–07); bàn giao, thu hồi (UC04.01.01–10).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: xe thuê ngoài, xe nhà thầu có quản lý ở đây không]. Trước khi viết SRS Điều phối phải tách "phương tiện" khỏi "thiết bị" (container, máy phát) — SRS v2.0 đang coi container là phương tiện (OQ-12). Hồ sơ lái xe tối thiểu dùng chung chưa có chỗ sở hữu (OQ-11).

__Luồng chính:__
1) Quản lý tạo hoặc cập nhật hồ sơ phương tiện.
2) Bàn giao phương tiện cho lái xe.
3) Thu hồi khi đổi người hoặc đưa xe vào xưởng.

__Rủi ro chính:__ Hồ sơ phương tiện lệch thực tế làm sai xếp xe và định mức · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd % phương tiện có người phụ trách đúng thực tế]
__OQ riêng:__ OQ-9, OQ-11, OQ-12

### 7.11 Quản lý danh mục kỹ thuật xưởng — `workshop-catalog`

Danh mục dùng cho nghiệp vụ xưởng: dịch vụ kỹ thuật, phụ tùng vật tư, công cụ dụng cụ, lốp, ắc quy, chi phí cấp 1–3, danh sách xưởng. Mỗi mục tạo mới qua đề xuất và phê duyệt để danh mục sạch.

__Phục vụ job:__ Nhân viên xưởng — làm nghiệp vụ trên danh mục chuẩn.

__Phạm vi v1:__ UC03.01–03.06, UC03.10–03.12 (xem, đề xuất tạo mới, thu hồi, phê duyệt/từ chối).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: danh mục mẫu dùng chung cho khách SaaS mới có không]

__Luồng chính:__
1) Nhân viên xưởng đề xuất tạo mới mục danh mục.
2) Người có quyền phê duyệt hoặc từ chối.
3) Mục được dùng trong mua hàng, kho, sửa chữa.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.12 Quản lý nhà cung cấp, khách hàng và xe của khách hàng — `workshop-partners`

Danh mục đối tác của xưởng: nhà cung cấp hàng hoá dịch vụ, khách hàng mua dịch vụ xưởng và xe của khách hàng. Tên hiển thị của danh mục khách hàng theo từ điển thuật ngữ của từng khách.

__Phục vụ job:__ Nhân viên xưởng, Kế toán — mua, bán đúng đối tác.

__Phạm vi v1:__ UC03.07–03.09.
__Chưa làm:__ Danh mục khách hàng có thể thuộc lõi, dùng chung với Điều phối vận tải; feature này khi đó chỉ giữ xe của khách hàng và quy trình duyệt của xưởng (OQ-11).

__Luồng chính:__
1) Nhân viên đề xuất tạo nhà cung cấp, khách hàng hoặc xe khách hàng.
2) Người có quyền phê duyệt.
3) Đối tác được dùng trong mua hàng, bán hàng hoá dịch vụ.

__Rủi ro chính:__ Danh mục khách hàng trùng giữa Xưởng và Điều phối vận tải · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9, OQ-11

### 7.13 Mua và báo giá hàng hoá dịch vụ — `purchasing`

Xưởng lấy báo giá và mua hàng hoá dịch vụ (phụ tùng, dịch vụ ngoài) từ nhà cung cấp, có phê duyệt. Giao dịch mua là nguồn cho nhập kho và thanh toán.

__Phục vụ job:__ Nhân viên xưởng — mua đúng hàng, đúng giá; Kế toán — có chứng từ để thanh toán.

__Phạm vi v1:__ UC05.01–05.02.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: mua hàng cho điều vận, văn phòng có dùng chung feature này không]

__Luồng chính:__
1) Nhân viên lập yêu cầu báo giá.
2) Chọn báo giá, lập đơn mua.
3) Phê duyệt, hàng về nhập kho.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.14 Nhập và xuất kho phụ tùng — `stock-movement`

Nhập kho hàng mua về, xuất kho cho sửa chữa hoặc bán. Mỗi phiếu gắn với nghiệp vụ nguồn để theo được trong cây liên quy trình.

__Phục vụ job:__ Nhân viên kho xưởng — tồn kho đúng; Lãnh đạo — chi phí sửa chữa theo đầu xe.

__Phạm vi v1:__ UC05.03–05.04.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: nhiều kho trong một xưởng có cần không]

__Luồng chính:__
1) Hàng mua về, lập phiếu nhập kho.
2) Lệnh sửa chữa cần phụ tùng, lập phiếu xuất kho (phiếu tham chiếu lệnh sửa chữa, feature này không phụ thuộc ngược `repair-order`).
3) Tồn kho cập nhật.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.15 Kiểm kê tồn kho, tồn xưởng, thanh lý rác thải — `inventory-count`

Kiểm kê định kỳ hàng tồn kho và hàng tồn xưởng, xử lý chênh lệch, thanh lý rác thải. Giữ số tồn trên phần mềm khớp thực tế.

__Phục vụ job:__ Nhân viên kho xưởng — số tồn khớp thực tế.

__Phạm vi v1:__ UC04.02–04.04.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]. Feature gồm 3 đối tượng (tồn kho, tồn xưởng, rác thải), có thể tách thanh lý rác thải riêng (OQ-15).

__Luồng chính:__
1) Lập đợt kiểm kê.
2) Ghi số thực tế, xem chênh lệch.
3) Duyệt điều chỉnh; thanh lý rác thải nếu có.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9, OQ-15

### 7.16 Lập và theo dõi lệnh sửa chữa — `repair-order`

Xưởng lập lệnh sửa chữa cho phương tiện, ghi dịch vụ kỹ thuật và phụ tùng dùng, theo dõi tới khi xe ra xưởng. Chi phí sửa chữa gắn vào phương tiện.

__Phục vụ job:__ Nhân viên xưởng — sửa đúng, đủ; Lãnh đạo — chi phí theo đầu xe.

__Phạm vi v1:__ UC05.06.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: lịch bảo dưỡng định kỳ theo km có trong v1 không]

__Luồng chính:__
1) Xe vào xưởng (từ báo cáo sự cố hoặc định kỳ).
2) Lập lệnh sửa chữa, xuất kho phụ tùng.
3) Hoàn thành, bàn giao lại xe.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd thời gian xe nằm xưởng]
__OQ riêng:__ OQ-9

### 7.17 Báo cáo sự cố phương tiện — `incident-report`

Lái xe hoặc nhân viên báo sự cố phương tiện, xưởng tiếp nhận và chuyển thành lệnh sửa chữa khi cần.

__Phục vụ job:__ Lái xe — báo sự cố nhanh; Nhân viên xưởng — tiếp nhận đủ thông tin.

__Phạm vi v1:__ UC05.07.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: nối với báo vấn đề giữa chặng của Lệnh vận tải thế nào]

__Luồng chính:__
1) Lái xe báo sự cố kèm ảnh.
2) Xưởng tiếp nhận, đánh giá.
3) Tạo lệnh sửa chữa nếu cần.

__Rủi ro chính:__ Sự cố báo ở Lệnh vận tải không sang được xưởng · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.18 Thanh toán mua hàng và bồi thường — `workshop-payment`

Thanh toán cho nhà cung cấp theo trả trước hoặc trả sau, theo dõi công nợ phải trả, xử lý đề nghị bồi thường thiệt hại.

__Phục vụ job:__ Kế toán — trả đúng, đủ, đúng hạn.

__Phạm vi v1:__ UC06.01–06.03.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: dùng chung luồng thanh toán với Điều phối vận tải hay tách]

__Luồng chính:__
1) Đơn mua đủ điều kiện, lập đề nghị thanh toán.
2) Phê duyệt.
3) Ghi nhận thanh toán, cập nhật công nợ.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.19 Thu tiền bán hàng hoá dịch vụ — `service-sales-payment`

Xưởng bán hàng hoá dịch vụ cho khách hàng (sửa xe khách, bán phụ tùng) và thu tiền theo trả trước hoặc trả sau.

__Phục vụ job:__ Kế toán — thu đủ tiền dịch vụ xưởng.

__Phạm vi v1:__ UC06.04.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]

__Luồng chính:__
1) Xuất bán hàng hoá dịch vụ cho khách.
2) Lập yêu cầu thanh toán.
3) Ghi nhận thu tiền.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.20 Xem báo cáo và dashboard xưởng — `workshop-reports`

Báo cáo và dashboard tổng hợp nghiệp vụ xưởng: chi phí sửa chữa, tồn kho, mua hàng, thanh toán. Cho quản lý xưởng và lãnh đạo thấy tình hình mà không gom tay.

__Phục vụ job:__ Lãnh đạo — biết chi phí xưởng theo đầu xe, theo kỳ.

__Phạm vi v1:__ Epic 10 Báo cáo, Epic 11 Dashboards của SRS v2.0.
__Chưa làm:__ Lãi lỗ theo lô hàng toàn doanh nghiệp (OQ-3).

__Luồng chính:__
1) Quản lý mở dashboard xưởng.
2) Lọc theo kỳ, cơ sở.
3) Xuất báo cáo.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-3, OQ-9

### 7.21 Đặt định mức khoán nhiên liệu phương tiện — `fuel-allowance`

Đặt và duyệt định mức khoán nhiên liệu cho từng phương tiện. Định mức là căn cứ cấp dầu và cấp dầu trên Lệnh vận tải.

__Phục vụ job:__ Quản lý phương tiện, Lãnh đạo — kiểm soát chi phí nhiên liệu.

__Phạm vi v1:__ Cập nhật định mức nhiên liệu (UC04.00.05); định mức nhiên liệu, mức tiêu hao thực tế, định mức khoán (UC04.01.11–21).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: định mức theo cung đường thay vì theo xe có cần không]. `saas-core-vs-tenant.md` xếp định mức nhiên liệu theo phương tiện vào lõi; PRD đang để ở Gói Nhiên liệu (OQ-13).

__Luồng chính:__
1) Quản lý đề xuất định mức cho phương tiện.
2) Người có quyền phê duyệt.
3) Định mức được dùng khi cấp dầu.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9, OQ-13

### 7.22 Lập kế hoạch mua và nhập dầu — `fuel-purchase`

Cây dầu nội bộ lập kế hoạch mua dầu và nhập dầu vào bồn. Giữ số dầu tồn khớp thực tế.

__Phục vụ job:__ Nhân viên cây dầu — đủ dầu để cấp.

__Phạm vi v1:__ UC12.01–12.02.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]

__Luồng chính:__
1) Lập kế hoạch mua dầu.
2) Phê duyệt.
3) Nhập dầu vào cây dầu.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.23 Cấp dầu cho phương tiện — `fuel-issuing`

Cấp dầu cho phương tiện tại cây dầu nội bộ hoặc cây dầu đối tác. Nhân viên đối tác cây dầu dùng app để xem phiếu, ghi nhận bơm, xuất hoá đơn, chốt phiếu.

__Phục vụ job:__ Nhân viên cây dầu, Nhân viên đối tác cây dầu — cấp đúng định mức; Lãnh đạo — chi phí nhiên liệu theo xe.

__Phạm vi v1:__ UC12.03; app cho nhân viên đối tác cây dầu.
__Chưa làm:__ Cấp dầu trên Lệnh vận tải nằm ở `transport-dispatch`; feature này giữ cấp dầu ngoài Lệnh, bù dầu, cây dầu đối tác.

__Luồng chính:__
1) Lập phiếu cấp dầu theo định mức.
2) Nhân viên cây dầu bơm và ghi nhận.
3) Chốt phiếu, xuất hoá đơn.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.24 Thanh toán trả sau cây dầu — `fuel-payment`

Tổng hợp và thanh toán trả sau cho cây dầu đối tác theo kỳ.

__Phục vụ job:__ Kế toán — trả đúng cho đối tác cây dầu.

__Phạm vi v1:__ UC12.05.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]

__Luồng chính:__
1) Tổng hợp phiếu cấp dầu trong kỳ.
2) Đối chiếu với đối tác.
3) Thanh toán.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.25 Quản lý cây dầu và xem dashboard cây dầu — `fuel-stations`

Danh mục cây dầu nội bộ và cây dầu mua ngoài; dashboard tổng hợp mọi cây dầu.

__Phục vụ job:__ Quản lý cây dầu, Lãnh đạo — thấy tình hình nhiên liệu toàn doanh nghiệp.

__Phạm vi v1:__ UC12.00, UC12.04 (cây dầu nội bộ, cây dầu mua ngoài).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]

__Luồng chính:__
1) Tạo cây dầu nội bộ hoặc mua ngoài.
2) Theo dõi tồn, cấp, mua trên dashboard.
3) Lọc theo cây dầu, kỳ.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.26 Cấp mới và cho nghỉ nhân viên — `employee-records`

Đề xuất cấp mới nhân viên và yêu cầu xin nghỉ, có phê duyệt; hồ sơ nhân viên nối với tài khoản và phân quyền.

__Phục vụ job:__ Nhân sự — quản lý hồ sơ nhân viên; Admin — tài khoản theo đúng nhân viên.

__Phạm vi v1:__ UC02.01.01–02.01.08.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: chấm công, lương có thuộc gói Nhân sự không]

__Luồng chính:__
1) Đề xuất cấp mới nhân viên.
2) Phê duyệt, tạo hồ sơ; tài khoản tạo qua `access-control`.
3) Khi nghỉ: tạo yêu cầu, phê duyệt.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

## 8. Success Metrics

| Vai trò | Chỉ số | Baseline | Target | Mốc thời gian |
|---|---|---|---|---|
| North Star | % JobID hoàn thành có mọi Lệnh vận tải đã duyệt và không còn chi phí chờ chứng từ, trong 3 ngày kể từ khi giao hàng xong (theo biên bản giao hàng) | TBD [NEEDS CLARIFICATION: baseline lấy từ đâu] | ≥ 80% | 6 tháng |
| Input | % JobID tạo từ AI đọc chứng từ, không nhập tay | TBD [NEEDS CLARIFICATION: baseline lấy từ đâu] | ≥ 70% | 6 tháng |
| Input | % việc hiện trường giao và nhận trên app | TBD [NEEDS CLARIFICATION: baseline lấy từ đâu] | ≥ 90% | 6 tháng |
| Input | % Lệnh vận tải hoàn thành có đủ ảnh và biên bản giao hàng | TBD [NEEDS CLARIFICATION: baseline lấy từ đâu] | ≥ 95% | 6 tháng |
| Kết quả kinh doanh | Số khách SaaS đang dùng | 1 (Delta) | 2 | 12 tháng |
| Guardrail | Tiền phạt quá mốc (lưu container, lưu vỏ) mỗi tháng | TBD [NEEDS CLARIFICATION: số phạt hiện tại của Delta] | Không tăng | liên tục |
| Guardrail | % chi phí phải sửa lại sau khi duyệt Lệnh | TBD [NEEDS CLARIFICATION: baseline lấy từ đâu] | Không tăng | liên tục |
| Guardrail | % trường AI đọc chứng từ phải sửa tay | TBD [NEEDS CLARIFICATION: đo từ lần chạy thật đầu tiên] | Không tăng | liên tục |
| Guardrail | Số Lệnh, biên bản bị mất khi app chạy lúc mất sóng | 0 | 0 | liên tục |

__Mục tiêu 3 / 6 / 12 tháng:__ 3 tháng — Delta chạy thật phân hệ Điều phối vận tải tại 1 chi nhánh thí điểm (cần OQ-4, OQ-5, OQ-12 và SRS Điều phối) · 6 tháng — toàn bộ chi nhánh Delta dùng, ≥ 90% việc giao nhận trên app, Zalo chỉ còn ngoại lệ có ghi nhận · 12 tháng — có khách SaaS thứ hai đang dùng mà không sửa lõi (cần OQ-7, OQ-8).

## 9. Constraints

* __Ngân sách / timeline / team:__ TBD (OQ-4). Chưa có business case và giá bán gói; phần cost-benefit để `/brd` làm.
* __Ràng buộc tích hợp (chỉ tên hệ thống):__ Hoá đơn điện tử MISA; ngân hàng Vietcombank (QR, uỷ nhiệm chi); VETC (phí đường bộ); Vietmap và GPS xe (EUP); kế hoạch nhà ga Ratraco (qua file). Mỗi kết nối là kết nối đầu tiên, thay được theo khách.
* __Ràng buộc pháp lý / vùng / compliance:__ Hoá đơn GTGT điện tử theo quy định Việt Nam. Dữ liệu từng khách tách riêng; dữ liệu sửa của AI đọc chứng từ chỉ dùng cho chính khách đó, trừ khi hợp đồng cho phép. Quyền sở hữu sản phẩm đồng sở hữu với Delta; còn làm rõ quyền khai thác thương mại riêng của mỗi bên (OQ-8). Giao diện tiếng Việt và tiếng Anh.

## 10. Risks & Assumptions

| Rủi ro / Giả định | Loại (value/usability/feasibility/viability) | Tầm quan trọng | Evidence | Khả năng | Hậu quả | Cách phòng |
|---|---|---|---|---|---|---|
| Quy tắc riêng Delta bị viết cứng vào lõi | viability | Cao | Tín hiệu gián tiếp | Thường | Không bán được cho khách thứ hai nếu không sửa code | Gắn nhãn tầng cho mọi quy tắc, con số đi qua bảng tham số theo khách, kiểm bằng lint trước khi duyệt tài liệu |
| Doanh nghiệp vận tải khác có quy trình đủ giống Delta để dùng chung lõi (giả định rủi ro nhất) | value | Cao | Giả định | Thỉnh thoảng | Lõi phải làm lại, mất lợi thế "đã chạy thật" | Phỏng vấn 2–3 doanh nghiệp cùng ngành trước khi chốt lõi |
| Lái xe và hiện trường chịu dùng app thay Zalo | usability | Cao | Tín hiệu gián tiếp | Thỉnh thoảng | Dữ liệu dọc đường thiếu, chi phí không về đúng JobID | App chạy khi mất sóng, ít bước, thiếu ảnh thì chặn bước tiếp; quản lý theo dõi tỷ lệ dùng app |
| AI đọc chứng từ đủ đúng để bỏ nhập tay | feasibility | Vừa | Tín hiệu gián tiếp | Thỉnh thoảng | CS vẫn sửa tay nhiều, vấn đề nhập lại không giảm | Người tạo luôn duyệt kết quả, lưu chỗ sửa, đo tỷ lệ phải sửa |
| Quyền khai thác thương mại sản phẩm đồng sở hữu với Delta chưa rõ | viability | Cao | Tín hiệu gián tiếp | Thỉnh thoảng | Không bán được cho khách thứ hai đúng mốc 12 tháng | Chốt điều khoản khai thác và bảo mật SOP, dữ liệu Delta trước khi chào bán (OQ-8) |
| Delta chưa gửi Quy trình điều vận | feasibility | Cao | Dữ liệu trực tiếp | Thường | Trạng thái Lệnh, luồng CBT, đường sắt sai; trễ mốc thí điểm 3 tháng | Bám OQ-5; viết SRS Điều phối theo đề xuất hiện có, đánh dấu phần chờ khách |
| Mô hình "container là phương tiện" của SRS v2.0 bị kế thừa | feasibility | Cao | Dữ liệu trực tiếp | Thường | Tổ hợp đầu kéo – mooc – container khó làm, khó bán khách khác | Tách phương tiện và thiết bị trước khi viết SRS Điều phối (OQ-12) |

## 11. Open Questions

* [ ] OQ-1: Tên thương mại của sản phẩm SaaS là gì? ("Invlogis" là tên dự án, dùng tạm.)
* [ ] OQ-2: Ngoài Delta, có tín hiệu thị trường nào khác cho "why now" (khách khác đã hỏi, quy định cảng điện tử, ePort)? Có đối thủ SaaS logistics Việt Nam nào cần theo dõi?
* [ ] OQ-3: Xem lãi lỗ và rủi ro theo lô hàng cho lãnh đạo — job chính của người đau nhất nhưng chưa có trong SRS. Thành feature riêng khi nào?
* [ ] OQ-4: Ngân sách, mốc go-live Điều phối vận tải với Delta, quy mô đội làm?
* [ ] OQ-5: Delta chưa gửi Quy trình điều vận — trạng thái Lệnh, luồng CBT, đường sắt đang là đề xuất.
* [ ] OQ-6: Bảng kê, shipment list, công nợ phải thu/phải trả, kết nối MISA, thanh toán trả hộ (QR, uỷ nhiệm chi, ngân hàng), xuất dữ liệu sang phần mềm kế toán của khách: tách thành feature nào, thuộc theme nào, chạy mốc nào? Dùng chung với thanh toán Xưởng không?
* [ ] OQ-7: Cấu hình theo khách (tham số, thuật ngữ, bật/tắt gói) và khởi tạo khách mới — điều kiện để bán SaaS nhưng chưa có trong SRS. Thành feature khi nào?
* [ ] OQ-8: Quyền khai thác thương mại riêng của mỗi bên với sản phẩm đồng sở hữu; SOP và dữ liệu Delta có phải bảo mật không (BL-056).
* [ ] OQ-9: Rủi ro chính, chỉ số đo thành công và phần "chưa làm" của các feature chưa có brainstorm (nền, phương tiện, Xưởng, Cây dầu, Nhân sự) — bổ sung khi chạy `/brainstorm` từng feature.
* [ ] OQ-10: Baseline các chỉ số Mục 8 (tiền phạt quá mốc mỗi tháng, tỷ lệ lô đủ chi phí hiện nay) lấy từ đâu?
* [ ] OQ-11: Danh mục khách hàng, báo giá, hợp đồng (bước 1 của `service-delivery`) và hồ sơ lái xe tối thiểu chưa có feature sở hữu. Đưa vào lõi dùng chung Điều phối và Xưởng, hay thành feature danh mục riêng?
* [ ] OQ-12: Tách "phương tiện" khỏi "thiết bị" (container, máy phát) ở SRS v2.0 trước khi viết SRS Điều phối — ai làm, khi nào?
* [ ] OQ-13: Danh sách gói bán chốt thế nào cho khớp `saas-core-vs-tenant.md` — có gói Nhân sự không (hay Nhân sự thuộc lõi)? Định mức nhiên liệu theo phương tiện thuộc lõi hay Gói Nhiên liệu?
* [ ] OQ-14: Khách của doanh nghiệp (đại diện chủ hàng) có được xem tình trạng lô hàng của mình không, hay ngoài phạm vi?
* [ ] OQ-15: `service-delivery`, `shipment-coordination`, `transport-dispatch`, `inventory-count` đang lớn hơn cỡ một brainstorm — có tách không (vd chi phí JobID, danh mục cảng/bãi, gói Đường sắt/CBT/Hàng lạnh, thanh lý rác thải)?
