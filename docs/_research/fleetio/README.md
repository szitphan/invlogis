---
type: research
keyword: "Fleetio: mục lục tham khảo theo feature Invlogis"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_research/fleetio/fleetio-repair.md
  - docs/_research/fleetio/fleetio-reminders-inspection.md
  - docs/_research/fleetio/fleetio-vehicle.md
  - docs/_research/fleetio/fleetio-tires.md
  - docs/_research/fleetio/fleetio-location-dispatch.md
  - docs/_research/fleetio/fleetio-parts-purchasing-fuel.md
  - docs/_research/fleetio/fleetio-saas-platform.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
---

# Fleetio: tham khảo cho đợt cải tiến và tính năng mới

Bộ tài liệu này trả lời câu hỏi: **mỗi feature của Invlogis nên lấy case nào của Fleetio làm tham khảo.** Mỗi file viết theo khuôn brainstorm 12 mục, có luồng và giải pháp. Đây là đầu vào để cân nhắc, chưa phải yêu cầu đã chốt, và chưa đối chiếu với Delta.

Màn trên Figma: 169 màn (40 bộ đầu, 129 sau đợt chạy thật), file `[innvie] invlogis v0.3.4`, trang `Research · Fleetio`, mỗi màn có ảnh gốc Fleetio ngay dưới. Nhãn tiếng Việt, vẽ bằng DS v2 theo ảnh chụp, không phải thiết kế đã duyệt của Invlogis. Userflow 7 nhóm cũng ở trang này. Chưa vẽ 10 màn không có ảnh gốc (hộp ghi "chưa có ảnh riêng" trong userflow). 13 màn thuộc 2 nhóm chỉ vẽ một lần.

Danh sách chức năng và mức đã đi: [fleetio-function-list.md](fleetio-function-list.md), ghi chú chạy thật: [run-notes/](run-notes/).

## Hai lớp tài liệu

> Phát hiện của 4 reviewer, phần đã sửa và phần còn mở: [[docs/_research/fleetio/srs/fleetio-srs-review-findings.md|Phát hiện review]].

| Lớp | Dùng khi | Ở đâu |
|---|---|---|
| Brainstorm | Đọc nhanh ý tưởng, đề xuất, mức tham khảo | `fleetio-*.md` trong thư mục này |
| SRS chi tiết | Cần FR, BR, câu báo lỗi, ERD, luồng, trạng thái, use case, ảnh màn thật | [srs/](srs/) |

| Nhóm | Spec | Mô hình | Màn thật |
|---|---|---|---|
| Sửa chữa | [Spec](srs/fleetio-repair-spec.md) | [ERD](srs/fleetio-repair-erd.md) · [Flows](srs/fleetio-repair-flows.md) · [States](srs/fleetio-repair-states.md) · [Use case](srs/fleetio-repair-usecases.md) · [User flow](srs/fleetio-repair-userflow.md) | [Màn](srs/fleetio-repair-screens.md) |
| Nhắc, kiểm tra | [Spec](srs/fleetio-reminders-inspection-spec.md) | [ERD](srs/fleetio-reminders-inspection-erd.md) · [Flows](srs/fleetio-reminders-inspection-flows.md) · [States](srs/fleetio-reminders-inspection-states.md) · [Use case](srs/fleetio-reminders-inspection-usecases.md) · [User flow](srs/fleetio-reminders-inspection-userflow.md) | [Màn](srs/fleetio-reminders-inspection-screens.md) |
| Kho, mua, nhiên liệu | [Spec](srs/fleetio-parts-purchasing-fuel-spec.md) | [ERD](srs/fleetio-parts-purchasing-fuel-erd.md) · [Flows](srs/fleetio-parts-purchasing-fuel-flows.md) · [States](srs/fleetio-parts-purchasing-fuel-states.md) · [Use case](srs/fleetio-parts-purchasing-fuel-usecases.md) · [User flow](srs/fleetio-parts-purchasing-fuel-userflow.md) | [Màn](srs/fleetio-parts-purchasing-fuel-screens.md) |
| Phương tiện | [Spec](srs/fleetio-vehicle-spec.md) | [ERD](srs/fleetio-vehicle-erd.md) · [Flows](srs/fleetio-vehicle-flows.md) · [States](srs/fleetio-vehicle-states.md) · [Use case](srs/fleetio-vehicle-usecases.md) · [User flow](srs/fleetio-vehicle-userflow.md) | [Màn](srs/fleetio-vehicle-screens.md) |
| Quản lý lốp | [Spec](srs/fleetio-tires-spec.md) | [ERD](srs/fleetio-tires-erd.md) · [Flows](srs/fleetio-tires-flows.md) · [States](srs/fleetio-tires-states.md) · [Use case](srs/fleetio-tires-usecases.md) · [User flow](srs/fleetio-tires-userflow.md) | [Màn](srs/fleetio-tires-screens.md) |
| Nền tảng SaaS | [Spec](srs/fleetio-saas-platform-spec.md) | [ERD](srs/fleetio-saas-platform-erd.md) · [Flows](srs/fleetio-saas-platform-flows.md) · [States](srs/fleetio-saas-platform-states.md) · [Use case](srs/fleetio-saas-platform-usecases.md) · [User flow](srs/fleetio-saas-platform-userflow.md) | [Màn](srs/fleetio-saas-platform-screens.md) |
| Bản đồ, gán việc | [Spec](srs/fleetio-location-dispatch-spec.md) | [ERD](srs/fleetio-location-dispatch-erd.md) · [Flows](srs/fleetio-location-dispatch-flows.md) · [States](srs/fleetio-location-dispatch-states.md) · [Use case](srs/fleetio-location-dispatch-usecases.md) · [User flow](srs/fleetio-location-dispatch-userflow.md) | [Màn](srs/fleetio-location-dispatch-screens.md) |

Mỗi FR có cột bằng chứng và cột đề xuất cho Invlogis. Phần SRS viết theo khuôn `/srs`, khác ở ba điểm: `type: research` để không lẫn vào số liệu SRS của dự án; use case gộp một file mỗi nhóm; màn hình là ảnh chụp thật thay cho Figma.

## Feature Invlogis nên tham khảo gì

| Feature Invlogis | Trạng thái | Case Fleetio đáng tham khảo | Mức | Ở đâu |
|---|---|---|---|---|
| `incident-report` | Chưa chi tiết | Mọi nguồn lỗi về một Sự cố; 5 cách xử lý; ưu tiên AI | Cao | [Sửa chữa](fleetio-repair.md) R1, R9, R16 |
| `repair-order` | Chưa chi tiết | Đóng lệnh kéo theo dây chuyền; khoá sửa; tách công, phụ tùng | Cao | [Sửa chữa](fleetio-repair.md) R2–R6, R11 |
| `repair-quotation` | Chưa chi tiết | Fleetio không có bước riêng; chỉ markup, tổng hợp chi phí | Thấp | [Sửa chữa](fleetio-repair.md) R12 |
| `reminders` | Chưa chi tiết | Nhắc hai trục; trạng thái tự đổi; xem trước lịch; bộ lịch; giấy tờ | Cao | [Nhắc, kiểm tra](fleetio-reminders-inspection.md) N1–N6, N12 |
| Kiểm tra xe (đề xuất mới, `vehicle-inspection`) | Chưa có | Biểu mẫu tự dựng; lỗi thành sự cố; chống kiểm khống | Cao, chờ hỏi Delta | [Nhắc, kiểm tra](fleetio-reminders-inspection.md) N7–N11, N14–N16 |
| `vehicle-management` | Đã có brainstorm | Trang xe trung tâm; bàn giao có số km; không gán trùng; sơ đồ trục, lắp, đảo, tháo lốp (lốp không phải đối tượng độc lập) | Trung | [Phương tiện](fleetio-vehicle.md) V1–V5, V11 · [Lốp](fleetio-tires.md) |
| `vehicle-telematics` | Đã có brainstorm | Sổ số km có nguồn; bản đồ cạnh danh sách; mã lỗi | Trung | [Phương tiện](fleetio-vehicle.md) V4, V5 · [Bản đồ](fleetio-location-dispatch.md) B1–B3 · [Sửa chữa](fleetio-repair.md) R19 |
| `transport-dispatch` | Đã có brainstorm | Chỉ lịch tài nguyên; **không** lấy Jobs | Thấp | [Phương tiện](fleetio-vehicle.md) V6 |
| `location-catalog` | Đã có thư mục | Bán kính vùng địa lý | Thấp | [Bản đồ](fleetio-location-dispatch.md) B4 |
| `purchasing` | Chưa chi tiết | Một nút chính mỗi bước; nhận một phần; 3 nơi đến; tự duyệt theo ngưỡng | Cao | [Kho, mua](fleetio-parts-purchasing-fuel.md) K1–K3, K8 |
| `stock-movement`, `inventory-count` | Chưa chi tiết | Thẻ tồn theo kho; sổ kho có số trước, số sau | Cao | [Kho, mua](fleetio-parts-purchasing-fuel.md) K4–K7, K10 |
| `business-partners` | Có bộ reverse | Phân loại quyết định nơi xuất hiện; tạo nhanh trong ô chọn | Trung | [Kho, mua](fleetio-parts-purchasing-fuel.md) K11, K12 |
| `product-catalog` | Đã có brainstorm | Định mức giờ công, phụ tùng theo đầu việc | Trung | [Sửa chữa](fleetio-repair.md) R21 |
| `fuel-issuing`, `fuel-allowance` | Chưa chi tiết | Cờ đổ một phần; tính tiêu hao ngay; cảnh báo vị trí, dung tích | Trung | [Kho, mua](fleetio-parts-purchasing-fuel.md) K13–K16 |
| `access-control`, `organization` | Chưa chi tiết | Quyền hai lớp Role và Record Set | Cao | [Nền tảng](fleetio-saas-platform.md) P1 |
| `common-workspace` | Chưa chi tiết | Trang đầu Needs Attention; danh sách chuẩn; theo dõi, bình luận | Cao | [Nền tảng](fleetio-saas-platform.md) P4, P5, P9 |
| OQ-7: cấu hình, khởi tạo khách | Chưa là feature | Luật bật tắt có giải thích; thiết lập chung; dữ liệu mẫu | Cao | [Nền tảng](fleetio-saas-platform.md) P2, P3, P6 |
| `workshop-reports` | Chưa chi tiết | Danh mục 49 báo cáo, 13 nhóm để chọn | Trung | [Nền tảng](fleetio-saas-platform.md) P11 |
| `help-center` | Chưa chi tiết | Khung Learn trên từng trang | Trung | [Nền tảng](fleetio-saas-platform.md) P6 |

## Nên làm trước

Đề xuất của mình khi xét theo PRD, vì Gói Bảo dưỡng đội xe chưa có mốc trong 6 tháng đầu:

1. **Có ích ngay cho bản thí điểm:** quyền hai lớp (P1), luật cấu hình theo khách (P2, P3), danh sách chuẩn và trang đầu (P4, P5). Không phụ thuộc gói nào.
2. **Hỏi Delta sớm:** có quy trình kiểm tra xe không. Câu trả lời quyết định có thêm feature mới.
3. **Để đến lượt gói:** toàn bộ phần sửa chữa, nhắc bảo dưỡng, kho, mua hàng.

## Không nên học

| Điểm | Vì sao | Ở đâu |
|---|---|---|
| Cho tồn kho âm không cảnh báo | Lệch sổ kho | [Kho, mua](fleetio-parts-purchasing-fuel.md) Mục 6.5 |
| Lệch tiền 100 lần ở chi tiết lệnh và Service Entry với tiền Việt; hộp thêm phụ tùng lưu đúng | Sai số tiền nghiêm trọng | [Sửa chữa](fleetio-repair.md) Mục 6.5 |
| Mức tiêu hao hiện mpg dù xe dùng km và lít | Sai đơn vị | [Kho, mua](fleetio-parts-purchasing-fuel.md) Mục 6.5 |
| Hoàn thành lệnh có lúc ghi trùng số đồng hồ, không phải lần nào cũng vậy | Rác dữ liệu | [Phương tiện](fleetio-vehicle.md) Mục 6.5, [Sửa chữa](fleetio-repair.md) Mục 6.5 |
| Nhãn nút zoom bị đảo | Lỗi trợ năng | [Bản đồ](fleetio-location-dispatch.md) Mục 6.5 |
| Lưu form trống chỉ báo "not authorized" | Không chỉ trường thiếu | [Sửa chữa](fleetio-repair.md) Mục 6.5 |
| Jobs làm mẫu điều vận; bắt buộc mã bưu chính | Không hợp ngành, không hợp Việt Nam | [Bản đồ](fleetio-location-dispatch.md), [Kho, mua](fleetio-parts-purchasing-fuel.md) Mục 7.1 |

## Phạm vi đã chọn

User chọn 37 mục ở [trang chọn](https://claude.ai/artifact/PaGiyyqCVUkyqs99sjAbvd). Không mở: Advanced Analytics, Custom Records, Tools. Recalls và Motor Pool ban đầu không viết, đợt chạy thật có đọc giao diện và ghi mức `Xem`.

## Mức bằng chứng theo nhóm

Mức từng chức năng ở [danh sách chức năng](fleetio-function-list.md) và cột Mức trong từng Spec. Dưới đây là phần chưa chạy trọn và lý do.

| Nhóm | Chưa chạy trọn | Vì sao |
|---|---|---|
| Sửa chữa | Đưa ra xưởng ngoài, Get Service at Shop | Shop Network chuyển sang Fleetio Pay, Access Denied; web không có bấm giờ công; đầu kéo, mooc là `Suy` vì nhóm này chỉ chạy xe Car |
| Nhắc, kiểm tra | Ca Location Exception bật thật, lịch Overdue, Skipped, chụp webcam, lưu Rule | Chưa có ca dương trên Fleetio Go, cần chờ qua ngày, chưa cấp camera, Rule khoá khi còn Sample Data |
| Phương tiện | Đặt xe Motor Pool, Archive khi có đặt chỗ | Không có liên hệ vừa đăng nhập vừa là Operator; Archive và trạng thái xe khác đã chạy ở lượt 3 |
| Lốp | Lưu mẫu đảo tuỳ biến, đọc áp suất tự động, import lốp | Một phần hoặc chỉ có tài liệu hãng; không có thao tác chuyển lốp giữa xe |
| Bản đồ, gán việc | Marker và sự kiện vùng chỉ chạy bằng `Chạy (vị trí giả lập)`, lưu Geofence Alert Policy | Không có thiết bị GPS; không lưu vì có gửi email |
| Kho, mua, nhiên liệu | Pending, Rejected của đơn, FIFO, LIFO, Average, Invite nhà cung cấp | Cần người thứ hai; đổi cách tính giá là một chiều, chờ quyết; không mời người ngoài |
| Nền tảng | Tích hợp, phần lớn Settings | Không kết nối, Settings chỉ đọc |

## Chưa làm

- **App Fleetio Go:** user đã nộp 1 phiếu (#126102722), mới kiểm dữ liệu phiếu và số đồng hồ; chưa đi hết app.
- **Lượt 3, 4, 5 (03/11):** function list 327 dòng: 216 chạy trọn, 67 một phần, 38 chỉ xem, 2 tài liệu, 4 ngoài phạm vi; mẫu số tăng do thêm FR mới nên không so trực tiếp với 275 dòng cũ. Tổng FR 336, BR 350, E 199. Đã rà ảnh lượt 3 và lượt 4: 46 ảnh mới có trong bảng màn, agent mở từng ảnh, không thấy bản đồ vị trí thật, địa chỉ thật, email, token; ảnh còn tên hiển thị tài khoản thử. 13 ảnh lượt 5 cũng đã rà.
- **Figma lượt 3-4:** 46 màn có ảnh đã vẽ ở 4 section mới (y từ 79900), chưa nối flow, chưa kiểm a11y, chưa soát kiểu 171 frame. 13 màn lượt 5 chưa vẽ.
- **Cài đặt:** Forecast đã tắt lại, Inventory Valuation vẫn Static (đổi là một chiều, chờ quyết). Shop Network không bật được: chuyển sang Fleetio Pay, Access Denied. Đặt xe Motor Pool chưa tạo được vì không có liên hệ vừa đăng nhập vừa là Operator.
- **Người dùng thứ hai:** chưa có, nên chưa đi nhánh chờ duyệt, phân quyền bằng tài khoản thật.
- **Tools, Custom Records, Advanced Analytics:** không mở theo lựa chọn của user.
- **Figma:** 10 màn không có ảnh gốc chưa vẽ. Nối được 126/218 đường, phần còn lại thiếu control trên màn, hệ thống tự chuyển hoặc là nhánh phụ ([kiểm độc lập](run-notes/_flow/verify-report.md), [báo cáo nối flow](run-notes/_flow/flow-report.md)). Chưa bấm thử Present. Toàn bộ 171 frame đã so với ảnh gốc: 59 khớp ngay, 112 đã sửa, chỗ còn lệch ở [run-notes/_audit/](run-notes/_audit/). Hàng Responsive chưa soát.
- **Đối chiếu nghiệp vụ:** gate máy chỉ kiểm nhãn, mã tham số, cú pháp sơ đồ. Đúng tầng, đúng nghiệp vụ chưa có người soát. Bảng màn mới viết theo ghi chú chạy, chưa đối chiếu từng ảnh.

## Dữ liệu TEST trên tài khoản Fleetio

Mọi bản ghi có tiền tố `TEST`; danh sách theo nhóm ở cuối từng file [run-notes/](run-notes/). Có thể dọn hoặc để hết hạn cùng bản dùng thử. Không gửi lời mời, không có email người ngoài, không đụng thanh toán.

Cần biết:

- Hạn mức 5 xe của gói thử đã đầy: `TEST-XE-01`, `TEST-MOOC-LOP`, `TEST-SUA-01`, `TEST-KHO-01`, `TEST-DAUKEO-2`. `TEST-XE-LOP` đã Archive, Restore bị khoá khi gói đầy; 2 phân công tương lai của xe này đã mất theo lần Archive.
- Một số phiếu kiểm tra mang vị trí thật của máy chạy trình duyệt. Ảnh có bản đồ các phiếu này đã được che.
- Có thao tác tháo 1 lốp TEST, Archive 1 automation TEST; mở lại lệnh làm mất Service Entry TEST đã sinh.
- Share báo cáo từng sinh link công khai khoảng 5 phút, đã thu hồi.
- Trial Tools đã Disable theo yêu cầu user, chờ huỷ tới 16/11. Chưa rõ ai bật.
- Biểu mẫu #680174 còn workflow đổi xe sang In Shop: nộp lại sẽ đổi trạng thái TEST-XE-01.

## Nguồn công khai đã đọc

- [Custom Records](https://help.fleetio.com/en_US/custom-records) · [Custom Fields](https://help.fleetio.com/en_US/custom-fields-overview) · [Record Sets](https://help.fleetio.com/en_US/record-sets)
- [Tools Overview](https://help.fleetio.com/en_US/tools-overview) · [Reminders for Tools](https://help.fleetio.com/en_US/reminders-for-tools)
- [Fleet Map Overview](https://help.fleetio.com/en_US/fleet-map-overview) · [Fuel Entry Overview](https://help.fleetio.com/en_US/fuel-entry-overview) · [Reduce fuel theft with alerts](https://www.fleetio.com/blog/reduce-fuel-theft-with-alerts) · [Vendor Location Alert](https://updates.fleetio.com/fuel-location-exception-updates-1WUzrG)

Đọc toàn văn thêm: Work Order Statuses, Maintenance Settings, Issues Overview, Service Tasks vs Issues, Purchase Orders Overview, Inventory Overview, Meter Entry Conflicts, Inspections Workflows, Location Exceptions, Fleet Map Overview. Các trang còn lại đọc qua kết quả tìm kiếm. Bản đồ module đầy đủ: [phân tích ban đầu](../2026-11-02-fleetio-app-teardown.md).
