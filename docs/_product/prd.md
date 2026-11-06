---
type: prd-product
status: stale
status_prev: draft
updated: 2026-10-20
links:
  - docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md
  - docs/_shared/project-profile.md
  - docs/_shared/system-overview.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_product/tenant-parameters.md
  - docs/_product/srs-v2-change-log.md
  - docs/_product/legacy-issues.md
  - docs/_reverse/account-access/account-access-reverse-spec.md
  - docs/_reverse/product-catalog/product-catalog-reverse-spec.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/cross-process-flow/brainstorms/cross-process-flow.md
---

# Invlogis — Product Requirements Document (project-level)

## 1. One-line Pitch

Nền tảng vận hành cho doanh nghiệp vận tải và logistics ở Việt Nam: các module điều phối vận tải (kèm công nợ, hoá đơn), phương tiện, bảo dưỡng sửa chữa, dầu, nhân sự dùng chung một dữ liệu, để mỗi lô hàng và mỗi đầu xe được theo từ chứng từ khách tới chi phí, doanh thu, công nợ mà không nhập lại.

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
  * Nhiều module chung một dữ liệu (điều phối vận tải kèm công nợ, phương tiện, bảo dưỡng sửa chữa, dầu): mỗi đầu xe và mỗi lô hàng có giá thành thật, điều phần mềm chỉ làm điều vận hoặc chỉ làm kế toán không có.
  * Cấu hình theo khách không sửa code: tham số, tên gọi, danh mục, bật/tắt gói.
  * App chạy khi mất sóng, hợp với lái xe ở cảng và trên đường.
  * Đã chạy thật ở quy mô Delta (~110.000 lô/năm) — có khách tham chiếu khi bán.
* __Khoảng trống đã biết:__ v1 cung cấp dữ liệu chi phí, doanh thu đúng JobID và cây quy trình; màn xem lãi lỗ theo lô, theo đầu xe cho lãnh đạo chưa có feature (OQ-3). Đây là khoảng trống lớn nhất giữa giá trị cốt lõi và phạm vi hiện tại.

## 5. Goals & Non-Goals

__Mục tiêu (in-scope):__
* Phân hệ Điều phối vận tải chạy thật tại Delta: JobID từ chứng từ khách → điều phối việc cảng, bãi → Lệnh vận tải → chi phí về đúng JobID.
* Các module đã có trong SRS v2.0 chạy trên cùng dữ liệu: Nền tảng, Quản trị và cấu hình, Danh mục cấp doanh nghiệp (trừ miền Hàng hoá, DEC-084), Quản lý phương tiện thuộc lõi; Bảo dưỡng sửa chữa, Quản lý dầu, Nhân sự đóng gói thành gói bán thêm (DEC-079).
* Lõi sản phẩm không chứa quy tắc riêng Delta: mọi con số, danh sách, bật/tắt đi qua tham số theo khách.

__Ngoài phạm vi (non-goals / out-of-scope):__
* Không làm phần mềm kế toán đầy đủ: có ghi nhận chi phí, doanh thu, công nợ theo chứng từ và xuất dữ liệu; sinh bút toán và đẩy một chiều sang phần mềm kế toán của khách qua lớp kết nối thay được (`accounting-integration`, DEC-344); không làm sổ cái, báo cáo thuế.
* Không kết nối máy với ePort cảng; phần mềm hỗ trợ danh sách việc ePort và lưu kết quả.
* Không làm sàn ghép hàng, ghép xe cho bên ngoài; không làm app cho chủ hàng tự đặt dịch vụ. Việc khách của doanh nghiệp tự theo dõi lô hàng chưa chốt (OQ-14).
* Không sửa lõi riêng cho một khách; yêu cầu riêng đi qua cấu hình, gói hoặc kết nối riêng.

## 6. Capability Themes

| Theme | Mô tả | Features thuộc theme |
|---|---|---|
| Nền tảng (Lõi) | Đăng nhập, thao tác chung, liên quy trình, trợ giúp, thư viện nội dung, kho tài liệu | `account-access`, `common-workspace`, `cross-process-flow`, `help-center`, `content-management`, `document` |
| Quản trị và cấu hình (Lõi) | Tài khoản, nhóm quyền, phân quyền theo chi nhánh, cơ sở | `access-control` |
| Danh mục cấp doanh nghiệp (Lõi; Hàng hoá bật theo Gói Bảo dưỡng đội xe) | Danh mục dùng chung đặt trên các chi nhánh, có trang quản lý và cấu hình riêng, chia miền Tổ chức (kho thuộc xưởng) · Hàng hoá · Phương tiện · Đối tác · Nhân sự · Tài chính. Miền Phương tiện, Nhân sự chưa có feature riêng | `organization`, `product-catalog`, `business-partners`, `cost-catalog` |
| Điều phối vận tải (Lõi) | Từ chứng từ khách tới Lệnh vận tải hoàn tất, chi phí về đúng JobID. Công nợ, hoá đơn tạm đặt ở module này (OQ-6) | `service-delivery`, `shipment-coordination`, `transport-dispatch` |
| Quản lý phương tiện (Lõi; định mức nhiên liệu bật theo Gói Nhiên liệu) | Hồ sơ phương tiện, bàn giao, thu hồi, định mức nhiên liệu — dữ liệu nối điều vận với xưởng và dầu | `vehicle-management`, `fuel-allowance` |
| Bảo dưỡng sửa chữa (Gói Bảo dưỡng đội xe) | Sự cố, chẩn đoán và báo giá, sửa chữa, lịch nhắc, mua hàng, kho phụ tùng, thanh toán, báo cáo xưởng | `incident-report`, `repair-quotation`, `repair-order`, `reminders`, `purchasing`, `stock-movement`, `inventory-count`, `workshop-payment`, `service-sales-payment`, `workshop-reports` |
| Quản lý dầu (Gói Nhiên liệu) | Cây dầu, mua nhập dầu, cấp dầu, thanh toán dầu | `fuel-stations`, `fuel-purchase`, `fuel-issuing`, `fuel-payment` |
| Nhân sự (Gói Nhân sự) | Hồ sơ nhân viên, cấp mới, cho nghỉ | `employee-records` |

Cấu trúc module theo DEC-079; tầng của module Danh mục theo DEC-084.

Gói gắn kèm bên trong feature lõi (bật theo khách): Đa chi nhánh (giao dịch nội bộ trong `service-delivery`), Tài chính (kết nối ngân hàng cho thanh toán trả hộ), Đường sắt, CBT, Hàng lạnh (trong `transport-dispatch`). Có Gói Nhân sự; định mức nhiên liệu thuộc Gói Nhiên liệu (DEC-085).

## 7. Feature Map

### Luồng người dùng tổng quan

__Hành trình Điều phối vận tải (CS, hiện trường, điều vận, lái xe, kế toán):__
1) Người dùng đăng nhập, vào đúng chi nhánh theo quyền → `account-access`, `access-control`
2) CS mở JobID từ chứng từ khách, AI đọc và điền sẵn, khách hàng lấy từ danh mục đối tác → `service-delivery`, `business-partners`
3) CS và hiện trường làm việc cảng, bãi theo luồng hàng trên app, sinh yêu cầu vận tải → `shipment-coordination`
4) Điều vận lập Lệnh vận tải trên xe của đội; lái xe chạy Lệnh, chụp chứng từ, ghi chi phí → `transport-dispatch`, `vehicle-management`
5) Chi phí, doanh thu về đúng JobID và đúng khoản mục chi phí, sẵn cho bảng kê và thanh toán → `service-delivery`, `cost-catalog`
6) Ai cũng xem được cả chuỗi quy trình từ một bản ghi bất kỳ → `cross-process-flow`

__Hành trình Bảo dưỡng sửa chữa – Quản lý dầu (quản lý phương tiện, xưởng, cây dầu):__
1) Phương tiện được bàn giao cho lái xe → `vehicle-management`
2) Lái xe báo sự cố; xưởng chẩn đoán, báo giá rồi lập lệnh sửa chữa → `incident-report`, `repair-quotation`, `repair-order`
3) Xưởng mua hàng hoá dịch vụ, nhập và xuất kho phụ tùng → `purchasing`, `stock-movement`
4) Thanh toán nhà cung cấp → `workshop-payment`
5) Cây dầu cấp dầu cho xe theo định mức → `fuel-allowance`, `fuel-issuing`
6) Quản lý xem báo cáo xưởng và dashboard cây dầu → `workshop-reports`, `fuel-stations`

Ngoài 2 hành trình chính (back-office, quản trị): `common-workspace`, `help-center` dùng xuyên suốt; `organization`, `product-catalog` là danh mục cấp doanh nghiệp, khai báo trước khi các module dùng; `reminders`, `inventory-count`, `service-sales-payment`, `fuel-purchase`, `fuel-payment`, `employee-records` là việc hậu cần định kỳ của xưởng, cây dầu, nhân sự.

### Bảng Feature Map

| # | Tính năng | Slug | Theme | Persona | Ưu tiên (MoSCoW) | Phụ thuộc | Chi tiết hóa |
|---|---|---|---|---|---|---|---|
| 1 | Đăng nhập và quản lý tài khoản cá nhân | `account-access` | Nền tảng | Mọi người dùng | Must | — | ⬜ chưa (có bộ reverse) |
| 2 | Dùng màn Home và thao tác chung trên danh sách | `common-workspace` | Nền tảng | Mọi người dùng | Must | `access-control` | ⬜ chưa |
| 3 | Xem quy trình liên nghiệp vụ dạng cây | `cross-process-flow` | Nền tảng | Mọi người dùng | Must | `access-control`; mềm: mỗi module đăng ký quy trình của mình | ✅ đã chi tiết (1 brainstorm, đang stale) |
| 4 | Tra cứu câu hỏi thường gặp và hướng dẫn sử dụng | `help-center` | Nền tảng | Mọi người dùng | Must (làm ở P1, sau phần P0 của `task-assignment`, `in-app-guidance`) | `account-access` | ✅ đã brainstorm |
| 5 | Quản lý tài khoản, nhóm quyền và phân quyền | `access-control` | Quản trị và cấu hình | Admin | Must | `account-access`, `organization` | ⬜ chưa |
| 6 | Quản lý xưởng, cơ cấu tổ chức và phân vùng dữ liệu theo chi nhánh | `organization` | Danh mục › Tổ chức | Admin | Must | `account-access` | ⬜ chưa |
| 7 | Quản lý danh mục hàng hoá và dịch vụ kỹ thuật | `product-catalog` | Danh mục › Hàng hoá | Nhân viên xưởng | Should | `access-control` | ✅ đã chi tiết (1 brainstorm) |
| 8 | Quản lý nhà cung cấp, khách hàng và xe của khách hàng | `business-partners` | Danh mục › Đối tác | Nhân viên xưởng, CS, Kế toán | Must | `access-control` | ⬜ chưa |
| 9 | Quản lý khoản mục chi phí cấp 1–3 | `cost-catalog` | Danh mục › Tài chính | Admin, Kế toán | Must | `access-control` | ⬜ chưa |
| 10 | Mở hồ sơ dịch vụ (JobID) từ chứng từ khách | `service-delivery` | Điều phối vận tải | CS, Kế toán | Must | `access-control`, `business-partners`, `cost-catalog` | ✅ đã chi tiết (1 brainstorm) |
| 11 | Điều phối việc cảng, bãi theo luồng hàng | `shipment-coordination` | Điều phối vận tải | CS, Hiện trường | Must | `service-delivery`, `access-control`, `cost-catalog`, `fund-payments`, `location-catalog` | ✅ đã chi tiết (1 brainstorm) |
| 12 | Lập và chạy Lệnh vận tải | `transport-dispatch` | Điều phối vận tải | Điều vận, Lái xe | Must | `shipment-coordination`, `vehicle-management`, `cost-catalog`; mềm (khi bật Gói Nhiên liệu): `fuel-allowance` | ✅ đã chi tiết (1 brainstorm) |
| 13 | Quản lý phương tiện, bàn giao và thu hồi | `vehicle-management` | Quản lý phương tiện | Quản lý phương tiện, Lái xe | Must | `access-control` | ⬜ chưa |
| 14 | Đặt định mức khoán nhiên liệu phương tiện | `fuel-allowance` | Quản lý phương tiện | Quản lý phương tiện | Should | `vehicle-management` | ⬜ chưa |
| 15 | Báo cáo sự cố phương tiện | `incident-report` | Bảo dưỡng sửa chữa | Lái xe, Nhân viên xưởng | Should | `vehicle-management` | ⬜ chưa |
| 16 | Chẩn đoán và báo giá sửa chữa, bán phụ tùng | `repair-quotation` | Bảo dưỡng sửa chữa | Nhân viên xưởng | Should | `product-catalog`, `business-partners`, `vehicle-management`; mềm: `incident-report` | ⬜ chưa |
| 17 | Lập và theo dõi lệnh sửa chữa | `repair-order` | Bảo dưỡng sửa chữa | Nhân viên xưởng | Should | `vehicle-management`, `stock-movement`, `repair-quotation`, `cost-catalog`; mềm: `incident-report` | ⬜ chưa |
| 18 | Đặt và nhận lịch nhắc bảo dưỡng và giấy tờ | `reminders` | Bảo dưỡng sửa chữa | Nhân viên xưởng, Quản lý phương tiện | Should | `access-control`, `vehicle-management` | ⬜ chưa |
| 19 | Mua hàng hoá dịch vụ | `purchasing` | Bảo dưỡng sửa chữa | Nhân viên xưởng | Should | `product-catalog`, `business-partners`, `cost-catalog` | ⬜ chưa |
| 20 | Nhập và xuất kho phụ tùng | `stock-movement` | Bảo dưỡng sửa chữa | Nhân viên kho xưởng | Should | `purchasing` | ⬜ chưa |
| 21 | Kiểm kê tồn kho, tồn xưởng, thanh lý rác thải | `inventory-count` | Bảo dưỡng sửa chữa | Nhân viên kho xưởng | Should | `stock-movement` | ⬜ chưa |
| 22 | Thanh toán mua hàng và bồi thường | `workshop-payment` | Bảo dưỡng sửa chữa | Kế toán, Nhân viên xưởng | Should | `purchasing`, `cost-catalog` | ⬜ chưa |
| 23 | Thu tiền bán hàng hoá dịch vụ | `service-sales-payment` | Bảo dưỡng sửa chữa | Kế toán | Should | `business-partners`, `stock-movement`, `repair-quotation`, `repair-order` | ⬜ chưa |
| 24 | Xem báo cáo và dashboard xưởng | `workshop-reports` | Bảo dưỡng sửa chữa | Lãnh đạo, Quản lý xưởng | Should | `repair-order`, `purchasing`, `stock-movement`, `inventory-count`, `workshop-payment` | ⬜ chưa |
| 25 | Quản lý cây dầu và xem dashboard cây dầu | `fuel-stations` | Quản lý dầu | Quản lý cây dầu | Should | `access-control` | ⬜ chưa |
| 26 | Lập kế hoạch mua và nhập dầu | `fuel-purchase` | Quản lý dầu | Nhân viên cây dầu | Should | `fuel-stations`, `business-partners` | ⬜ chưa |
| 27 | Cấp dầu cho phương tiện | `fuel-issuing` | Quản lý dầu | Nhân viên cây dầu, Nhân viên đối tác cây dầu | Should | `fuel-allowance`, `fuel-stations`, `cost-catalog` | ⬜ chưa |
| 28 | Thanh toán trả sau cây dầu | `fuel-payment` | Quản lý dầu | Kế toán | Should | `fuel-issuing`, `business-partners`, `cost-catalog` | ⬜ chưa |
| 29 | Cấp mới và cho nghỉ nhân viên | `employee-records` | Nhân sự | Nhân sự | Should | `access-control` | ⬜ chưa |
| 30 | Soạn, chia sẻ tài liệu nội bộ của công ty theo cây, đẩy sang Help Center | `content-management` | Nền tảng | Admin khách, mọi người dùng | Should | `access-control`, `help-center` | ⬜ chưa |
| 31 | Gom và lưu tài liệu, ảnh của mọi nghiệp vụ | `document` | Nền tảng | Mọi người dùng | Should | `access-control`, `file-attachments` | ⬜ chưa |

Thứ tự dựng nền: `account-access` → `organization` → `access-control` → các danh mục → các module nghiệp vụ (khác thứ tự module trong bảng).

Ưu tiên tính cho bản thí điểm Điều phối vận tải với Delta. Should của Bảo dưỡng sửa chữa, Quản lý dầu, Nhân sự là gói bán thêm Delta bật sẵn, chưa có mốc trong 6 tháng đầu; thứ tự giữa các gói chốt cùng OQ-4.

Chưa có trong Feature Map (chưa có SRS): xem lãi lỗ theo lô cho lãnh đạo (OQ-3); bảng kê, công nợ, thanh toán trả hộ của Điều phối — hoá đơn đã tạm đặt trong `service-delivery` (DEC-079), tách feature riêng hay không chốt ở OQ-6; cấu hình theo khách và khởi tạo khách mới — điều kiện để bán SaaS, phải chốt trước mốc 12 tháng (OQ-7); hồ sơ lái xe dùng chung (OQ-11); báo giá, hợp đồng với khách để module Sales sau này (DEC-086); quản lý danh mục cảng, bãi, điểm chụp ảnh và loại phí theo địa điểm mà brainstorm Điều phối dùng (OQ-17). North Star Mục 8 phụ thuộc nhóm OQ-6.

### 7.1 Đăng nhập và quản lý tài khoản cá nhân — `account-access`

Người dùng đăng nhập vào web và app, khôi phục hoặc đổi mật khẩu, xem thông tin cá nhân. Đây là cửa vào chung của mọi module; được cấp nhiều chi nhánh thì chọn chi nhánh trước khi vào Home.

__Phục vụ job:__ Feature nền — hỗ trợ mọi nhóm người dùng ở Mục 3.

__Phạm vi v1:__ Đăng nhập, quên mật khẩu, đăng xuất, đổi mật khẩu, tạo mật khẩu mới, xem thông tin cá nhân (UC01.01–01.06).
__Phạm vi thêm:__ đăng nhập bằng Google song song mật khẩu, bật theo khách; tự khoá tài khoản Google khi nhân viên nghỉ việc (DEC-405).
__Chưa làm:__ đăng nhập Microsoft.

__Luồng chính:__
1) Người dùng nhập tài khoản, mật khẩu.
2) Được cấp nhiều chi nhánh thì chọn chi nhánh.
3) Vào màn Home theo quyền.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ khi nhiều khách SaaS dùng chung cửa đăng nhập] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd số yêu cầu hỗ trợ quên mật khẩu mỗi tháng]
__OQ riêng:__ OQ-9

### 7.2 Dùng màn Home và thao tác chung trên danh sách — `common-workspace`

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

### 7.3 Xem quy trình liên nghiệp vụ dạng cây — `cross-process-flow`

Từ bất kỳ bản ghi nào thuộc một quy trình nhiều nghiệp vụ, người dùng mở được sơ đồ cây toàn bộ bước chính, nhánh phát sinh, liên module, công nợ; chọn một bước để xem trạng thái và mở màn chi tiết. Thay thanh tiến trình tuyến tính của SRS cũ vốn không vẽ được nhánh lồng nhau. Kèm màn danh sách theo dõi mọi quy trình đang chạy.

__Phục vụ job:__ Lãnh đạo, CS, điều vận — biết một việc đang ở đâu trong cả chuỗi mà không phải hỏi.

__Phạm vi v1:__ Theo brainstorm `cross-process-flow` (đã có SRS và màn Figma): cây quy trình web và mobile, tạo nghiệp vụ tiếp theo, danh sách quy trình.
__Chưa làm:__ Bảng phát sinh của Điều phối vận tải — bổ sung khi chốt quy trình với khách. Bản thí điểm chỉ cần 3 feature điều phối đăng ký quy trình.

__Luồng chính:__
1) Người dùng mở chi tiết một bản ghi.
2) Mở dòng quy trình, xem cây các bước.
3) Chọn một bước, xem trạng thái, mở màn chi tiết bước đó.

__Rủi ro chính:__ Mỗi module khai báo quy trình một kiểu, cây hiển thị không nhất quán · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chốt chỉ số khi rà lại brainstorm `cross-process-flow`, vd số cuộc gọi hỏi tình trạng việc giảm]
__OQ riêng:__ —

### 7.4 Tra cứu câu hỏi thường gặp và hướng dẫn sử dụng — `help-center`

Người dùng tự tra câu hỏi thường gặp và hướng dẫn sử dụng ngay trong sản phẩm. Với SaaS nhiều khách, đây là cách giảm tải hỗ trợ khi khách mới bắt đầu dùng.

__Phục vụ job:__ Feature nền — hỗ trợ mọi người dùng tự học cách dùng.

__Phạm vi v1:__ trang web tài liệu công khai và cần đăng nhập, bài gắn cứng với từng chức năng; FAQ, PDF riêng của khách trong phần mềm (UC09.01–09.02), giữ như chức năng cũ; bài của công ty đẩy từ `content-management` (DEC-405, DEC-406). Chi tiết: [[docs/help-center/brainstorms/help-center.md|Brainstorm Help Center]].
__Chưa làm:__ màn soạn bài trong sản phẩm; khách tự sửa bài dùng chung. Bài dùng chung mọi khách do innvie soạn; khách tự tải FAQ, PDF riêng.

__Luồng chính:__
1) Người dùng mở trợ giúp.
2) Tìm câu hỏi hoặc hướng dẫn.
3) Đọc và làm theo.

__Rủi ro chính:__ bài viết cũ hơn giao diện; tự làm trang kéo dài · __Đo thành công:__ số câu hỏi đội innvie nhận theo từng module, đếm từ 4 tuần trước khi bật đợt 1; chưa đặt chỉ tiêu

### 7.5 Quản lý tài khoản, nhóm quyền và phân quyền — `access-control`

Admin của khách tạo tài khoản, lập nhóm quyền và gán quyền chức năng theo nền tảng, phạm vi chi nhánh, cơ sở. Quyền theo chức năng chứ không theo vai trò cố định, để mỗi khách tự ghép quyền đúng chức danh của mình. Không có quyền thì không thấy tính năng; nút không có quyền thì ẩn.

__Phục vụ job:__ Feature nền — hỗ trợ Admin của khách; mọi job ở Mục 3 dựa vào phân quyền đúng.

__Phạm vi v1:__ Quản lý tài khoản, nhóm quyền, thay đổi phân quyền chức năng (UC13.01–13.02, UC02.02.01); phạm vi Công ty → Chi nhánh → Cơ sở lấy từ cơ cấu khai ở `organization`. Cơ chế quyền có thời hạn gắn bản ghi hoặc ca trực là lõi, thuộc feature này; `shipment-coordination` chỉ dùng cơ chế. Tài khoản chỉ được tạo ở đây; `employee-records` gọi sang.
__Phạm vi thêm:__ gỡ tài khoản Google đã gắn; vô hiệu hoá tay kèm tạm ngưng Google; quyền cài đặt đăng nhập Google, Thử khoá lại, IT đã khoá tay (xem 7.1, DEC-405).

__Luồng chính:__
1) Admin tạo nhóm quyền, chọn quyền chức năng theo nền tảng.
2) Admin tạo tài khoản, gán nhóm quyền và phạm vi chi nhánh, cơ sở.
3) Người dùng đăng nhập chỉ thấy tính năng và dữ liệu trong phạm vi được cấp.

__Rủi ro chính:__ Cấp sai phạm vi làm người chi nhánh này thấy dữ liệu chi nhánh khác · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd thời gian Admin của khách mới tự thiết lập xong phân quyền]
__OQ riêng:__ OQ-9

### 7.6 Quản lý xưởng, cơ cấu tổ chức và phân vùng dữ liệu theo chi nhánh — `organization`

Admin của khách khai báo cơ cấu Công ty → Chi nhánh → Cơ sở và danh sách xưởng; kho thuộc xưởng (DEC-079). Cơ cấu này là khung phân vùng dữ liệu: bản ghi thuộc chi nhánh, cơ sở nào thì chỉ người có phạm vi đó thấy. Là danh mục cấp doanh nghiệp, đặt trên các chi nhánh, có trang quản lý riêng. Cơ cấu tổ chức thuộc lõi; danh sách xưởng và kho bật theo Gói Bảo dưỡng đội xe.

__Phục vụ job:__ Feature nền — hỗ trợ Admin của khách; phân quyền theo chi nhánh ở `access-control` và mọi module dựa vào cơ cấu này.

__Phạm vi v1:__ Danh mục xưởng (UC03.02); cơ cấu tổ chức, phân vùng dữ liệu theo chi nhánh, cơ sở (mục "Cơ cấu tổ chức, phân vùng dữ liệu và quản lý feature theo Chi nhánh/Cơ sở" của SRS v2.0, chưa làm).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: chi nhánh tách hoặc nhập thì dữ liệu cũ thuộc về đâu]. Ngừng dùng, xoá mục danh mục (ISS-04) chốt ở brainstorm.

__Luồng chính:__
1) Admin khai báo công ty, chi nhánh, cơ sở.
2) Admin khai báo xưởng và kho thuộc xưởng.
3) Admin gán phạm vi cho tài khoản ở `access-control`; bản ghi mới tự gắn chi nhánh, cơ sở.

__Rủi ro chính:__ Khai sai cơ cấu làm dữ liệu chi nhánh này lộ sang chi nhánh khác · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd thời gian khởi tạo cơ cấu cho khách mới]
__OQ riêng:__ OQ-7, OQ-9

### 7.7 Quản lý danh mục hàng hoá và dịch vụ kỹ thuật — `product-catalog`

Danh mục hàng hoá và dịch vụ kỹ thuật dùng chung cấp doanh nghiệp: dịch vụ kỹ thuật, phụ tùng vật tư, công cụ dụng cụ, lốp, ắc quy. Mỗi mục tạo mới qua đề xuất và phê duyệt để danh mục sạch. Miền này bật theo Gói Bảo dưỡng đội xe (DEC-084).

__Phục vụ job:__ Nhân viên xưởng — làm nghiệp vụ trên danh mục chuẩn.

__Phạm vi v1:__ UC03.01, UC03.03–03.06 (xem, đề xuất tạo mới, thu hồi, phê duyệt/từ chối).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: danh mục mẫu dùng chung cho khách SaaS mới có không]. Tổ chức lại sản phẩm, lắp được cho loại xe nào, nhóm dạng cây (ISS-02) và ngừng dùng, xoá mục danh mục (ISS-04) chốt ở brainstorm.

__Luồng chính:__
1) Nhân viên xưởng đề xuất tạo mới mục danh mục.
2) Người có quyền phê duyệt hoặc từ chối.
3) Mục được dùng trong báo giá, mua hàng, kho, sửa chữa.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.8 Quản lý nhà cung cấp, khách hàng và xe của khách hàng — `business-partners`

Danh mục đối tác dùng chung cấp doanh nghiệp: nhà cung cấp hàng hoá dịch vụ, khách hàng và xe của khách hàng. Xưởng và Điều phối vận tải dùng chung một danh mục khách hàng thay vì mỗi module giữ một bản. Tên hiển thị của danh mục khách hàng theo từ điển thuật ngữ của từng khách. Xe của khách hàng chỉ xưởng dùng nên bật theo Gói Bảo dưỡng đội xe.

__Phục vụ job:__ Nhân viên xưởng, CS, Kế toán — mua, bán, mở JobID đúng đối tác.

__Phạm vi v1:__ UC03.07–03.09.
__Chưa làm:__ Báo giá, hợp đồng với khách để module Sales sau này (DEC-086). Bên xuất hoá đơn khác khách đặt dịch vụ (CHG-21) và ngừng dùng, xoá đối tác (ISS-04) chốt ở brainstorm.

__Luồng chính:__
1) Nhân viên đề xuất tạo nhà cung cấp, khách hàng hoặc xe khách hàng.
2) Người có quyền phê duyệt.
3) Đối tác được dùng trong JobID, mua hàng, bán hàng hoá dịch vụ.

__Rủi ro chính:__ Cùng một khách hàng bị tạo hai lần khi Xưởng và Điều phối cùng đề xuất · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.9 Quản lý khoản mục chi phí cấp 1–3 — `cost-catalog`

Danh mục khoản mục chi phí 3 cấp dùng chung cấp doanh nghiệp. Chi phí của Lệnh vận tải, JobID, xưởng, cây dầu đều gắn vào khoản mục này, để kế toán gom chi phí theo lô, theo đầu xe mà không phải đối chiếu tay. Mỗi khoản mục tạo mới qua đề xuất và phê duyệt.

__Phục vụ job:__ Kế toán — chi phí đủ, đúng theo từng lô; Lãnh đạo — xem chi phí theo khoản mục (dữ liệu nền cho báo cáo lãi lỗ, OQ-3).

__Phạm vi v1:__ UC03.10–03.12 (chi phí cấp 1, cấp 2, cấp 3).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: loại phí có cách hạch toán theo địa điểm (CHG-20) vào v1 hay để sau]. Ngừng dùng, xoá khoản mục (ISS-04) chốt ở brainstorm.

__Luồng chính:__
1) Kế toán đề xuất khoản mục chi phí mới.
2) Người có quyền phê duyệt hoặc từ chối.
3) Khoản mục được dùng khi ghi chi phí ở điều phối, xưởng, cây dầu.

__Rủi ro chính:__ Mỗi chi nhánh đặt khoản mục một kiểu, không gom được chi phí toàn doanh nghiệp · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.10 Mở hồ sơ dịch vụ (JobID) từ chứng từ khách — `service-delivery`

JobID là xương sống mọi dịch vụ (hải quan, vận tải, thủ tục chuyên ngành, giá trị gia tăng). CS tạo JobID một lần từ chứng từ khách, AI đọc chứng từ điền sẵn, người tạo duyệt. Mọi việc làm sau đó ở Điều phối và Điều vận đều kéo chi phí, doanh thu về đúng JobID, để khi dịch vụ xong thì bảng kê, công nợ và hạch toán nội bộ đã sẵn sàng.

__Phục vụ job:__ CS — mở hồ sơ một lần; Kế toán — chi phí, doanh thu đủ theo lô; Lãnh đạo — có dữ liệu chi phí, doanh thu theo lô làm nền cho báo cáo lãi lỗ (OQ-3).

__Phạm vi v1:__ Theo brainstorm `service-delivery`: tạo, duyệt JobID từ chứng từ; chi phí trên JobID (tạm ứng theo ngưỡng, yêu cầu thanh toán); hoá đơn điện tử, hoá đơn trả hộ; giao dịch nội bộ liên chi nhánh (gói Đa chi nhánh).
__Chưa làm:__ Duyệt thanh toán, QR, uỷ nhiệm chi, kết nối ngân hàng (thuộc feature "Thanh toán trả hộ", chưa có trong Feature Map — OQ-6). Báo giá, hợp đồng với khách để module Sales sau này (DEC-086); danh mục khách hàng thuộc `business-partners`.

__Luồng chính:__
1) CS chọn khách hàng (từ `business-partners`) và loại JobID.
2) CS tải chứng từ khách, AI đọc và điền sẵn.
3) CS duyệt, JobID được tạo.
4) Điều phối, Điều vận làm việc; chi phí, doanh thu về JobID.
5) Dịch vụ hoàn thành, JobID sẵn cho bảng kê và công nợ.

__Rủi ro chính:__ AI đọc chứng từ sai nhiều, CS vẫn phải sửa tay · __Đo thành công:__ % JobID tạo từ AI đọc chứng từ không nhập tay (mục tiêu ≥ 70% sau 6 tháng)
__OQ riêng:__ OQ-6, OQ-16

### 7.11 Điều phối việc cảng, bãi theo luồng hàng — `shipment-coordination`

Dữ liệu đi liền từ JobID sang yêu cầu vận tải, không nhập lại. CS kê khai một lần, phần mềm phân luồng theo loại hàng và thuộc tính cảng, bãi: CS tự làm trên ePort, giao việc cho hiện trường, hoặc sinh yêu cầu vận tải ngay. Việc hiện trường được giao, nhận, chụp chứng từ trên app; mỗi việc kéo theo chi phí định mức và quyền thanh toán đúng người, đúng JobID.

__Phục vụ job:__ CS, Hiện trường — giao và làm việc cảng, bãi trên app thay Zalo; Lãnh đạo — biết việc nào sắp trễ mốc.

__Phạm vi v1:__ Theo brainstorm `shipment-coordination`: 6 luồng hàng, phân luồng theo thuộc tính cảng/bãi (danh mục ở `location-catalog`), danh mục lô hàng, AI đọc Booking Note/eDO/EIR/phiếu cân, quét QR tờ khai, giao việc và chuyển việc, gợi ý người nhận việc, ca trực, chọn vỏ và chốt số container thực nhận, việc phát sinh có duyệt, thu hoá đơn GTGT, định mức khi giao việc.
__Chưa làm:__ Kết nối máy với ePort.

__Luồng chính:__
1) JobID được duyệt, CS kê khai việc cảng, bãi.
2) Phần mềm phân luồng theo loại hàng và thuộc tính cảng, bãi.
3) Việc hiện trường được giao, người nhận làm và chụp chứng từ trên app.
4) Sinh yêu cầu vận tải đủ dữ liệu cho Điều vận.

__Rủi ro chính:__ Hiện trường vẫn nhận việc qua Zalo, không dùng app · __Đo thành công:__ % việc hiện trường giao và nhận trên app (mục tiêu ≥ 90% sau 6 tháng)
__OQ riêng:__ —

### 7.12 Lập và chạy Lệnh vận tải — `transport-dispatch`

Điều vận nhận yêu cầu vận tải đủ dữ liệu, lập Lệnh trên một màn theo dõi xếp xe; lái xe chạy Lệnh trên app: chụp ảnh tại điểm, ghi chi phí, lập biên bản giao hàng, báo vấn đề giữa chặng. Lệnh lưu cả kế hoạch và thực tế; quá mốc thì cảnh báo, leo thang. Lệnh duyệt xong thì chi phí đã nằm đúng JobID.

__Phục vụ job:__ Điều vận — xếp xe đúng mốc, biết ngay sự cố; Lái xe — làm việc và ghi chi phí tại chỗ; Lãnh đạo — rủi ro trễ mốc.

__Phạm vi v1:__ Theo brainstorm `transport-dispatch`: Lệnh theo FCL, LCL, CFS, air; ảnh định vị tại các điểm bắt buộc (danh sách điểm cấu hình theo loại hàng); biên bản giao hàng điện tử chạy khi mất sóng; cảnh báo quá mốc; chi phí dọc đường; báo vấn đề giữa chặng; cấp dầu trên Lệnh gắn định mức phương tiện, chỉ có khi bật Gói Nhiên liệu (DEC-085). Gói Đường sắt, CBT, Hàng lạnh bật theo khách.
__Chưa làm:__ Điều phối Lệnh có AI đề xuất xe (P2); gợi ý hàng chiều về cho CBT. Cấp dầu ngoài Lệnh và bù dầu thuộc `fuel-issuing`.

__Luồng chính:__
1) Điều vận nhận yêu cầu vận tải, lập Lệnh, chọn xe và lái xe.
2) Lái xe nhận Lệnh trên app, chạy tới từng điểm, chụp ảnh.
3) Lái xe ghi chi phí, lập biên bản giao hàng.
4) Có vấn đề thì báo giữa chặng; quá mốc thì cảnh báo.
5) Điều vận duyệt Lệnh, chi phí về JobID.

__Rủi ro chính:__ Lái xe vẫn gửi ảnh và chi phí qua Zalo · __Đo thành công:__ % Lệnh hoàn thành có đủ ảnh và biên bản giao hàng (mục tiêu ≥ 95% sau 6 tháng)
__OQ riêng:__ OQ-5

### 7.13 Quản lý phương tiện, bàn giao và thu hồi — `vehicle-management`

Hồ sơ phương tiện của doanh nghiệp (đầu kéo, xe tải, mooc), cập nhật thông tin chung, bàn giao và thu hồi phương tiện cho lái xe. Đây là dữ liệu nối Điều vận (xe chạy Lệnh) với Xưởng (sửa chữa) và Cây dầu (định mức, cấp dầu), để mỗi đầu xe có giá thành thật.

__Phục vụ job:__ Điều vận — biết xe nào sẵn sàng; Lãnh đạo — chi phí theo đầu xe (dữ liệu nền cho báo cáo lãi lỗ, OQ-3).

__Phạm vi v1:__ Danh sách, chi tiết, cập nhật phương tiện, hàng hoá và thiết bị, duyệt cập nhật, lịch sử thay đổi (UC04.00.01–04, UC04.00.06–07); bàn giao, thu hồi (UC04.01.01–10).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: xe thuê ngoài, xe nhà thầu có quản lý ở đây không]. Trước khi viết SRS Điều phối phải tách "phương tiện" khỏi "thiết bị" (container, máy phát) — SRS v2.0 đang coi container là phương tiện (OQ-12). Hồ sơ lái xe tối thiểu dùng chung chưa có chỗ sở hữu (OQ-11).

__Luồng chính:__
1) Quản lý tạo hoặc cập nhật hồ sơ phương tiện.
2) Bàn giao phương tiện cho lái xe.
3) Thu hồi khi đổi người hoặc đưa xe vào xưởng.

__Rủi ro chính:__ Hồ sơ phương tiện lệch thực tế làm sai xếp xe và định mức · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd % phương tiện có người phụ trách đúng thực tế]
__OQ riêng:__ OQ-9, OQ-11, OQ-12

### 7.14 Đặt định mức khoán nhiên liệu phương tiện — `fuel-allowance`

Đặt và duyệt định mức khoán nhiên liệu cho từng phương tiện. Định mức là căn cứ cấp dầu và cấp dầu trên Lệnh vận tải.

__Phục vụ job:__ Quản lý phương tiện, Lãnh đạo — kiểm soát chi phí nhiên liệu.

__Phạm vi v1:__ Cập nhật định mức nhiên liệu (UC04.00.05); định mức nhiên liệu, mức tiêu hao thực tế, định mức khoán (UC04.01.11–21).
__Chưa làm:__ TBD [NEEDS CLARIFICATION: định mức theo cung đường thay vì theo xe có cần không]. Định mức nhiên liệu thuộc Gói Nhiên liệu (DEC-085).

__Luồng chính:__
1) Quản lý đề xuất định mức cho phương tiện.
2) Người có quyền phê duyệt.
3) Định mức được dùng khi cấp dầu.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.15 Báo cáo sự cố phương tiện — `incident-report`

Lái xe hoặc nhân viên báo sự cố phương tiện, xưởng tiếp nhận rồi chuyển sang chẩn đoán, báo giá khi cần.

__Phục vụ job:__ Lái xe — báo sự cố nhanh; Nhân viên xưởng — tiếp nhận đủ thông tin.

__Phạm vi v1:__ UC05.07.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: nối với báo vấn đề giữa chặng của Lệnh vận tải thế nào]

__Luồng chính:__
1) Lái xe báo sự cố kèm ảnh.
2) Xưởng tiếp nhận, đánh giá.
3) Chuyển sang chẩn đoán, báo giá nếu cần.

__Rủi ro chính:__ Sự cố báo ở Lệnh vận tải không sang được xưởng · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.16 Chẩn đoán và báo giá sửa chữa, bán phụ tùng — `repair-quotation`

Xưởng chẩn đoán xe rồi lập báo giá cho 3 trường hợp: sửa xe của doanh nghiệp, sửa xe của khách hàng, bán phụ tùng. Báo giá sửa xe của doanh nghiệp đi qua phê duyệt nội bộ; báo giá cho khách hàng chờ người đại diện khách xác nhận. Báo giá được duyệt là nguồn cho lệnh sửa chữa và thu tiền bán hàng hoá dịch vụ.

__Phục vụ job:__ Nhân viên xưởng — chốt hạng mục và giá trước khi sửa; Kế toán — có căn cứ thu tiền.

__Phạm vi v1:__ Feature 05.02 Báo giá hàng hoá dịch vụ của SRS v2.0.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phần nào để sau]. Huỷ chẩn đoán để không sinh lại lệnh sửa chữa (ISS-05) chốt ở brainstorm.

__Luồng chính:__
1) Xe vào xưởng (từ báo cáo sự cố hoặc khách mang tới), nhân viên chẩn đoán.
2) Lập báo giá dịch vụ kỹ thuật, phụ tùng.
3) Phê duyệt nội bộ hoặc khách hàng xác nhận.
4) Báo giá được duyệt chuyển sang lệnh sửa chữa hoặc xuất bán phụ tùng.

__Rủi ro chính:__ Sửa xong chi phí vượt báo giá, khách không chịu trả phần vượt · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd % lệnh sửa chữa có chi phí khớp báo giá]
__OQ riêng:__ OQ-9

### 7.17 Lập và theo dõi lệnh sửa chữa — `repair-order`

Xưởng lập lệnh sửa chữa cho phương tiện, ghi dịch vụ kỹ thuật và phụ tùng dùng, theo dõi tới khi xe ra xưởng. Chi phí sửa chữa gắn vào phương tiện.

__Phục vụ job:__ Nhân viên xưởng — sửa đúng, đủ; Lãnh đạo — chi phí theo đầu xe (dữ liệu nền cho báo cáo lãi lỗ, OQ-3).

__Phạm vi v1:__ UC05.06, gồm nghiệm thu sửa chữa trên app.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: lịch bảo dưỡng định kỳ theo km có trong v1 không]. Đóng lệnh sinh nhập kho trả lại (ISS-05), cập nhật lệnh đã chốt (ISS-06) chốt ở brainstorm.

__Luồng chính:__
1) Báo giá sửa chữa được duyệt, hoặc xe vào bảo dưỡng định kỳ.
2) Lập lệnh sửa chữa, xuất kho phụ tùng.
3) Hoàn thành, bàn giao lại xe.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số, vd thời gian xe nằm xưởng]
__OQ riêng:__ OQ-9

### 7.18 Đặt và nhận lịch nhắc bảo dưỡng và giấy tờ — `reminders`

Đặt lịch nhắc cho việc định kỳ hoặc có hạn của đội xe, như bảo dưỡng, hạn giấy tờ, và nhận nhắc trên web, app. Lịch nhắc tạo mới hoặc cập nhật đi qua phê duyệt. Đặt trong Bảo dưỡng sửa chữa (DEC-083).

__Phục vụ job:__ Nhân viên xưởng, Quản lý phương tiện — không bỏ sót bảo dưỡng, hạn giấy tờ của xe.

__Phạm vi v1:__ Epic 08 Lịch nhắc của SRS v2.0, có phê duyệt tạo mới và cập nhật.
__Chưa làm:__ Cảnh báo mốc container, quá mốc — thuộc `shipment-coordination` và `transport-dispatch`; feature này chỉ nhắc do người dùng tự đặt.

__Luồng chính:__
1) Người dùng tạo lịch nhắc, chọn thời điểm.
2) Người có quyền phê duyệt.
3) Đến hạn, hệ thống nhắc.
4) Người dùng xử lý và đóng nhắc.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.19 Mua hàng hoá dịch vụ — `purchasing`

Xưởng mua hàng hoá dịch vụ (phụ tùng, dịch vụ sửa chữa ngoài) từ nhà cung cấp, có phê duyệt; dịch vụ sửa chữa ngoài được nghiệm thu trên app. Giao dịch mua là nguồn cho nhập kho và thanh toán.

__Phục vụ job:__ Nhân viên xưởng — mua đúng hàng, đúng giá; Kế toán — có chứng từ để thanh toán.

__Phạm vi v1:__ UC05.01. Báo giá bán của xưởng (Feature 05.02) thuộc `repair-quotation`.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: mua hàng cho điều vận, văn phòng có dùng chung feature này không]

__Luồng chính:__
1) Nhân viên lập đơn mua hàng hoá dịch vụ.
2) Người có quyền phê duyệt.
3) Hàng về nhập kho; dịch vụ ngoài được nghiệm thu trên app.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.20 Nhập và xuất kho phụ tùng — `stock-movement`

Nhập kho hàng mua về, xuất kho cho sửa chữa hoặc bán. Mỗi phiếu gắn với nghiệp vụ nguồn để theo được trong cây liên quy trình.

__Phục vụ job:__ Nhân viên kho xưởng — tồn kho đúng; Lãnh đạo — chi phí sửa chữa theo đầu xe (dữ liệu nền cho báo cáo lãi lỗ, OQ-3).

__Phạm vi v1:__ UC05.03–05.04.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: nhiều kho trong một xưởng có cần không]. Nhập kho trả lại khi đóng lệnh sửa chữa (ISS-05), nhật ký thay đổi tồn (ISS-08) chốt ở brainstorm.

__Luồng chính:__
1) Hàng mua về, lập phiếu nhập kho.
2) Lệnh sửa chữa cần phụ tùng, lập phiếu xuất kho (phiếu tham chiếu lệnh sửa chữa, feature này không phụ thuộc ngược `repair-order`).
3) Tồn kho cập nhật.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.21 Kiểm kê tồn kho, tồn xưởng, thanh lý rác thải — `inventory-count`

Kiểm kê định kỳ hàng tồn kho và hàng tồn xưởng, xử lý chênh lệch, thanh lý rác thải. Giữ số tồn trên phần mềm khớp thực tế.

__Phục vụ job:__ Nhân viên kho xưởng — số tồn khớp thực tế.

__Phạm vi v1:__ UC04.02–04.04.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]. Feature gồm 3 đối tượng (tồn kho, tồn xưởng, rác thải), giữ chung một feature (OQ-15, DEC-087).

__Luồng chính:__
1) Lập đợt kiểm kê.
2) Ghi số thực tế, xem chênh lệch.
3) Duyệt điều chỉnh; thanh lý rác thải nếu có.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.22 Thanh toán mua hàng và bồi thường — `workshop-payment`

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

### 7.23 Thu tiền bán hàng hoá dịch vụ — `service-sales-payment`

Xưởng bán hàng hoá dịch vụ cho khách hàng (sửa xe khách, bán phụ tùng) và thu tiền theo trả trước hoặc trả sau.

__Phục vụ job:__ Kế toán — thu đủ tiền dịch vụ xưởng.

__Phạm vi v1:__ UC06.04.
__Chưa làm:__ TBD [NEEDS CLARIFICATION: phạm vi cần làm sau]

__Luồng chính:__
1) Báo giá sửa xe khách hoặc bán phụ tùng được xác nhận, xuất bán cho khách.
2) Lập yêu cầu thanh toán.
3) Ghi nhận thu tiền.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.24 Xem báo cáo và dashboard xưởng — `workshop-reports`

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

### 7.26 Lập kế hoạch mua và nhập dầu — `fuel-purchase`

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

### 7.27 Cấp dầu cho phương tiện — `fuel-issuing`

Cấp dầu cho phương tiện tại cây dầu nội bộ hoặc cây dầu đối tác. Nhân viên đối tác cây dầu dùng app để xem phiếu, ghi nhận bơm, xuất hoá đơn, chốt phiếu.

__Phục vụ job:__ Nhân viên cây dầu, Nhân viên đối tác cây dầu — cấp đúng định mức; Lãnh đạo — chi phí nhiên liệu theo xe (dữ liệu nền cho báo cáo lãi lỗ, OQ-3).

__Phạm vi v1:__ UC12.03; app cho nhân viên đối tác cây dầu.
__Chưa làm:__ Cấp dầu trên Lệnh vận tải nằm ở `transport-dispatch`; feature này giữ cấp dầu ngoài Lệnh, bù dầu, cây dầu đối tác.

__Luồng chính:__
1) Lập phiếu cấp dầu theo định mức.
2) Nhân viên cây dầu bơm và ghi nhận.
3) Chốt phiếu, xuất hoá đơn.

__Rủi ro chính:__ TBD [NEEDS CLARIFICATION: rủi ro nghiệp vụ chính] · __Đo thành công:__ TBD [NEEDS CLARIFICATION: chọn chỉ số đo]
__OQ riêng:__ OQ-9

### 7.28 Thanh toán trả sau cây dầu — `fuel-payment`

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

### 7.29 Cấp mới và cho nghỉ nhân viên — `employee-records`

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

__Mục tiêu 3 / 6 / 12 tháng:__ 3 tháng — Delta chạy thật phân hệ Điều phối vận tải tại 1 chi nhánh thí điểm (cần OQ-4, OQ-5, OQ-12, SRS Điều phối và 6 feature Must chưa chi tiết hoá: `account-access`, `organization`, `access-control`, `business-partners`, `cost-catalog`, `vehicle-management`) · 6 tháng — toàn bộ chi nhánh Delta dùng, ≥ 90% việc giao nhận trên app, Zalo chỉ còn ngoại lệ có ghi nhận · 12 tháng — có khách SaaS thứ hai đang dùng mà không sửa lõi (cần OQ-7, OQ-8).

## 9. Constraints

* __Ngân sách / timeline / team:__ Ngân sách, đội làm TBD (OQ-4). Chưa có business case và giá bán gói; phần cost-benefit để `/brd` làm. Lộ trình của Delta (Phần mềm Delta 3.0, 16/10/2026, mục II và 3.3): giai đoạn 1 từ 01/9/2026 đến 31/3/2027 làm phần quản trị cơ bản (vận tải, hải quan, thủ tục chuyên ngành, dịch vụ giá trị gia tăng); giai đoạn 2 từ 01/4 đến 31/12/2027 làm các phân hệ còn lại; giai đoạn 3 chuyển sang nền AI Agent làm việc qua MCP. Xưởng đã xong, đang hiệu chỉnh và go live; dầu go live 15/10/2026; kế toán quỹ và thanh toán go live trên Delta 2.0 trước 31/12/2026.
* __Ràng buộc tích hợp (chỉ tên hệ thống):__ Hoá đơn điện tử MISA; ngân hàng Vietcombank (QR, uỷ nhiệm chi); VETC (phí đường bộ); Vietmap và GPS xe (EUP); kế hoạch nhà ga Ratraco (qua file). Mỗi kết nối là kết nối đầu tiên, thay được theo khách.
* __Ràng buộc pháp lý / vùng / compliance:__ Hoá đơn GTGT điện tử theo quy định Việt Nam. Dữ liệu từng khách tách riêng; dữ liệu sửa của AI đọc chứng từ chỉ dùng cho chính khách đó, trừ khi hợp đồng cho phép. Quyền sở hữu sản phẩm đồng sở hữu với Delta; còn làm rõ quyền khai thác thương mại riêng của mỗi bên (OQ-8). Giao diện tiếng Việt và tiếng Anh.

### 9.1 Yêu cầu chung về AI và dữ liệu

Áp cho mọi feature. Nguồn: Phần mềm Delta 3.0 — Thiết kế kiến trúc và lộ trình (16/10/2026), mục 2.2.3, IV, VI, VII.

* __Bảo mật nhiều tầng:__ dữ liệu được kiểm ngay khi vào hệ thống; AI chỉ làm được những gì người dùng thật đứng sau nó được phép; phân quyền tới từng dòng dữ liệu (theo chi nhánh, đội xe, luồng AI).
* __AI nằm trong quy trình:__ AI chạy như một bước của quy trình, kích hoạt theo thao tác trên phần mềm; không chép dữ liệu ra công cụ AI bên ngoài. Sẵn sàng cho khách kiểm toán bảo mật dữ liệu.
* __Đo chi phí AI:__ đo được số lượt gọi và token AI theo từng quy trình nghiệp vụ và theo từng khách.
* __Phân loại dữ liệu 4 cấp:__ pháp lý (mã hoá, lưu biệt lập); quản trị, tài chính (P/L Jobsheet, công nợ, hợp đồng, bảng lương — chỉ người được phân quyền); vận hành; công cộng. Ngoại lệ: tệp, bình luận và lịch sử hiện cho mọi người xem được bản ghi, gồm giấy tờ nhân viên (04/11, chờ Delta xác nhận).
* __Lưu trữ:__ lưu tập trung trên hệ thống, không lưu ra ngoài. Chứng từ kế toán, thuế, hải quan giữ theo `P-thoi-gian-luu-chung-tu` (Delta: 10 năm); log hệ thống và log gọi AI giữ theo `P-thoi-gian-luu-log` (Delta: 6 tháng).
* __Chặn AI chạy vòng lặp:__ một tác vụ AI vượt `P-gioi-han-luot-goi-ai` (Delta: 10 lượt gọi) hoặc `P-gioi-han-thoi-gian-tac-vu-ai` (Delta: 3 phút) thì ngắt, báo email hoặc Telegram, khoá luồng AI đó và chuyển thành việc "Task lỗi cần xử lý bằng tay" cho nhân viên.

## 10. Risks & Assumptions

| Rủi ro / Giả định | Loại (value/usability/feasibility/viability) | Tầm quan trọng | Evidence | Khả năng | Hậu quả | Cách phòng |
|---|---|---|---|---|---|---|
| Quy tắc riêng Delta bị viết cứng vào lõi | viability | Cao | Tín hiệu gián tiếp | Thường | Không bán được cho khách thứ hai nếu không sửa code | Gắn nhãn tầng cho mọi quy tắc, con số đi qua bảng tham số theo khách, kiểm bằng lint trước khi duyệt tài liệu |
| Doanh nghiệp vận tải khác có quy trình đủ giống Delta để dùng chung lõi (giả định rủi ro nhất) | value | Cao | Giả định | Thỉnh thoảng | Lõi phải làm lại, mất lợi thế "đã chạy thật" | Phỏng vấn 2–3 doanh nghiệp cùng ngành trước khi chốt lõi |
| Lái xe và hiện trường chịu dùng app thay Zalo | usability | Cao | Tín hiệu gián tiếp | Thỉnh thoảng | Dữ liệu dọc đường thiếu, chi phí không về đúng JobID | App chạy khi mất sóng, ít bước, thiếu ảnh thì chặn bước tiếp; quản lý theo dõi tỷ lệ dùng app |
| AI đọc chứng từ đủ đúng để bỏ nhập tay | feasibility | Vừa | Tín hiệu gián tiếp | Thỉnh thoảng | CS vẫn sửa tay nhiều, vấn đề nhập lại không giảm | Người tạo luôn duyệt kết quả, lưu chỗ sửa, đo tỷ lệ phải sửa |
| Quyền khai thác thương mại sản phẩm đồng sở hữu với Delta chưa rõ | viability | Cao | Tín hiệu gián tiếp | Thỉnh thoảng | Không bán được cho khách thứ hai đúng mốc 12 tháng | Chốt điều khoản khai thác và bảo mật SOP, dữ liệu Delta trước khi chào bán (OQ-8) |
| Delta chưa gửi Quy trình điều vận | feasibility | Cao | Dữ liệu trực tiếp | Thường | Trạng thái Lệnh, luồng CBT, đường sắt sai; trễ mốc thí điểm 3 tháng | Bám OQ-5; viết SRS Điều phối theo đề xuất hiện có, đánh dấu phần chờ khách |
| Cấu hình theo khách và khởi tạo khách mới chưa thành feature, trong khi mọi feature lõi dựa vào nó để không viết cứng quy tắc Delta | viability | Cao | Tín hiệu gián tiếp | Thường | Không có khách SaaS thứ hai đúng mốc 12 tháng mà không sửa lõi | Chốt OQ-7 và đưa vào Feature Map trước khi chi tiết hoá các feature lõi còn lại |
| Mô hình "container là phương tiện" của SRS v2.0 bị kế thừa | feasibility | Cao | Dữ liệu trực tiếp | Thường | Tổ hợp đầu kéo – mooc – container khó làm, khó bán khách khác | Tách phương tiện và thiết bị trước khi viết SRS Điều phối (OQ-12) |

## 11. Open Questions

* [ ] OQ-1: Tên thương mại của sản phẩm SaaS là gì? ("Invlogis" là tên dự án, dùng tạm.)
* [ ] OQ-2: Ngoài Delta, có tín hiệu thị trường nào khác cho "why now" (khách khác đã hỏi, quy định cảng điện tử, ePort)? Có đối thủ SaaS logistics Việt Nam nào cần theo dõi?
* [ ] OQ-3: Xem lãi lỗ và rủi ro theo lô hàng cho lãnh đạo — job chính của người đau nhất nhưng chưa có trong SRS. Thành feature riêng khi nào?
* [ ] OQ-4: Ngân sách, mốc go-live Điều phối vận tải với Delta, quy mô đội làm?
* [ ] OQ-5: Delta chưa gửi Quy trình điều vận — trạng thái Lệnh, luồng CBT, đường sắt đang là đề xuất.
* [ ] OQ-6: Bảng kê, shipment list, công nợ phải thu/phải trả, kết nối MISA, thanh toán trả hộ (QR, uỷ nhiệm chi, ngân hàng), xuất dữ liệu sang phần mềm kế toán của khách: tách thành feature nào, thuộc theme nào, chạy mốc nào? Dùng chung với thanh toán Xưởng không? Kết nối MISA đã có hướng: `accounting-integration` (DEC-344); phần còn lại vẫn mở.
* [ ] OQ-7: Cấu hình theo khách (tham số, thuật ngữ, bật/tắt gói) và khởi tạo khách mới — điều kiện để bán SaaS nhưng chưa có trong SRS. Thành feature khi nào?
* [ ] OQ-8: Quyền khai thác thương mại riêng của mỗi bên với sản phẩm đồng sở hữu; SOP và dữ liệu Delta có phải bảo mật không (BL-056).
* [ ] OQ-9: Rủi ro chính, chỉ số đo thành công và phần "chưa làm" của các feature chưa có brainstorm (nền, phương tiện, Xưởng, Cây dầu, Nhân sự) — bổ sung khi chạy `/brainstorm` từng feature.
* [ ] OQ-10: Baseline các chỉ số Mục 8 (tiền phạt quá mốc mỗi tháng, tỷ lệ lô đủ chi phí hiện nay) lấy từ đâu?
* [ ] OQ-11: Hồ sơ lái xe tối thiểu dùng chung chưa có feature sở hữu — đưa vào `employee-records`, `vehicle-management` hay feature riêng? Đã chốt một phần: danh mục khách hàng về `business-partners` cấp doanh nghiệp (DEC-079); báo giá, hợp đồng với khách (bước 1 của `service-delivery`) để module Sales sau này (DEC-086).
* [ ] OQ-12: Tách "phương tiện" khỏi "thiết bị" (container, máy phát) ở SRS v2.0 trước khi viết SRS Điều phối — ai làm, khi nào?
* [x] OQ-13: Danh sách gói bán chốt thế nào cho khớp `saas-core-vs-tenant.md` — có gói Nhân sự không (hay Nhân sự thuộc lõi)? Định mức nhiên liệu theo phương tiện thuộc lõi hay Gói Nhiên liệu? Resolved: có Gói Nhân sự; định mức nhiên liệu thuộc Gói Nhiên liệu (DEC-085).
* [ ] OQ-14: Khách của doanh nghiệp (đại diện chủ hàng) có được xem tình trạng lô hàng của mình không, hay ngoài phạm vi?
* [x] OQ-15: `service-delivery`, `shipment-coordination`, `transport-dispatch`, `inventory-count` đang lớn hơn cỡ một brainstorm — có tách không (vd chi phí JobID, danh mục cảng/bãi, gói Đường sắt/CBT/Hàng lạnh, thanh lý rác thải)? Resolved: không tách. (DEC-087)
* [ ] OQ-16: Chưa có module Sales (DEC-086), JobID v1 lấy giá bán, doanh thu từ đâu (nhập tay, bảng giá theo khách)? Phần mềm Delta 3.0 (16/10/2026) mục 3.1.5 xếp phân hệ Sales (hợp đồng, báo giá, hoa hồng sales và sales fund, hoa hồng khách, thu hồi công nợ) vào giai đoạn 2.
* [ ] OQ-17: Danh mục cảng, bãi, điểm chụp ảnh và loại phí, định mức theo địa điểm mà brainstorm `shipment-coordination`, `transport-dispatch` dùng thuộc feature nào? Loại phí có trùng khoản mục chi phí của `cost-catalog` không? Đã chốt một phần: danh mục địa điểm và định mức theo địa điểm thuộc `location-catalog` (DEC-249). Điểm chụp ảnh, loại phí còn mở.
* [ ] OQ-18: Thông báo trong app (nhắc, cảnh báo quá mốc, chờ duyệt) do feature nào sở hữu — `common-workspace` hay feature riêng?
* [ ] OQ-19: Tiền thuê xe nội bộ tính theo "Tổng Kms thực chạy chéo × Định mức cấu hình theo dòng xe" hay theo khấu hao và số ngày chạy chéo? — Nguồn khách: Phân hệ APAS (25/10/2026), mục 3.6.3 Quy trình đối lưu chi phí và quyết toán nội bộ cuối kỳ, mục 3.4.1 Luồng xử lý chi phí cho thuê phương tiện định kỳ hàng tháng, mục 3.6.4 Lõi hạch toán thuê phương tiện tự động đối lưu khấu hao; Phân hệ FIAM (25/10/2026), mục 4.7.1 Luồng xử lý chi phí cho thuê phương tiện định kỳ hàng tháng — Nguồn nội bộ: `docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md:940`, `:727`, `:970`; `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md:803`
* [ ] OQ-20: Công thức ghi "Mức trích khấu hao tháng × Tổng số ngày lịch của tháng hiện hành ÷ Tổng số ngày chạy chéo thực tế" khiến xe chạy chéo càng ít ngày thì tiền thuê càng cao. Có phải ý là khấu hao tháng ÷ ngày lịch × ngày chạy chéo không? — Nguồn khách: Phân hệ APAS (25/10/2026), mục 3.4.1 Luồng xử lý chi phí cho thuê phương tiện định kỳ hàng tháng; Phân hệ FIAM (25/10/2026), mục 4.7.1 Luồng xử lý chi phí cho thuê phương tiện định kỳ hàng tháng — Nguồn nội bộ: `docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md:727`; `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md:803`
* [ ] OQ-21: Phí thuê xe nội bộ ở chi nhánh sử dụng xe ghi vào TK 632 hay TK 6274? — Nguồn khách: Phân hệ APAS (25/10/2026), mục 3.4.1 Luồng xử lý chi phí cho thuê phương tiện định kỳ hàng tháng, mục 3.6.4 Lõi hạch toán thuê phương tiện tự động đối lưu khấu hao — Nguồn nội bộ: `docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md:735`, `:980`
* [ ] OQ-22: Lốp, ắc quy, đại tu lớn khi xe chạy chéo treo TK 242 ở chi nhánh sở hữu hay chi nhánh sử dụng xe? Mục 2.1.1 e (Tình huống 2) và dòng 15 (đại tu) ghi chi nhánh sở hữu; mục 2.1.5 và dòng 10 ghi chi nhánh sử dụng. — Nguồn khách: Phân hệ FIAM (25/10/2026), mục 2.1.1 e Quy trình kết chuyển chi phí khi chốt Lệnh sửa chữa, mục 2.1.5 Quy chế quản trị tài chính đối với phương tiện điều động chéo chi nhánh, mục 4.4 Ma trận định tuyến hạch toán tự động dòng 10 và 15 — Nguồn nội bộ: `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md:271`, `:404`, `:714`, `:720`
* [ ] OQ-23: Bảo hiểm xe chạy chéo, tại chi nhánh sở hữu ghi Có TK 331 hay Có TK 242? — Nguồn khách: Phân hệ FIAM (25/10/2026), mục 4.4 Ma trận định tuyến hạch toán tự động dòng 20, mục 4.8 Cơ chế ủy quyền chi hộ, Chặng 2 — Nguồn nội bộ: `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md:725`, `:872`
* [ ] OQ-24: Delta có 3 bồn dầu nội bộ (Hải Phòng, Bắc Ninh, Hải Dương) hay bồn tại 4 văn phòng chi nhánh (HP, BN, HD, BD)? — Nguồn khách: Phân hệ FIAM (25/10/2026), mục 1.2 Danh mục hệ thống tài khoản kế toán, tiểu khoản 1522; mục 2.2.1 Các nguyên tắc quản lý và hạch toán — Nguồn nội bộ: `docs-input/sop/fiam-ke-toan-quan-tri/fiam-ke-toan-quan-tri.md:102`, `:442`
* [ ] OQ-25: FIAM, APAS, VIS khớp với 6 phân hệ của Delta 3.0 thế nào? Delta 3.0 không có 3 tên này, nhưng Kiến trúc đa pháp nhân lại dùng chúng. — Nguồn khách: Phần mềm Delta 3.0 (16/10/2026), mục 3.1 Phân hệ và chức năng; Kiến trúc tầng dữ liệu đa pháp nhân (26/10/2026), đoạn Tầng Quản trị Nội bộ — Nguồn nội bộ: `docs-input/sop/delta-3-0-master-plan/delta-3-0-master-plan.md:153`; `docs-input/sop/kien-truc-du-lieu-da-phap-nhan/kien-truc-du-lieu-da-phap-nhan.md:9`
