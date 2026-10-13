---
type: product-strategy
status: draft
status_changed: 2026-10-14
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-12
links:
  - docs/_shared/project-profile.md
  - docs/_shared/system-overview.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs/service-delivery/brainstorms/service-delivery.md
  - docs/shipment-coordination/brainstorms/shipment-coordination.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
  - docs/cross-process-flow/srs/cross-process-flow-spec.md
  - docs/meetings/2026-10-09-client-dispatch-field-issues.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs/_product/srs-v2-change-log.md
---

# Lõi SaaS và phần riêng Delta — phân loại quy tắc để bán cho khách khác

## 1. Bài toán

Hệ thống đang làm theo hợp đồng outsource cho Delta. Định hướng mới: phát triển thành **sản phẩm SaaS logistics** bán cho nhiều doanh nghiệp, Delta là khách hàng đầu tiên. Rủi ro lớn nhất là quy tắc riêng của Delta bị viết cứng vào phần mềm. Khi bán cho khách thứ hai, mỗi điểm cứng đó thành một trong ba thứ: sửa code riêng cho từng khách, tách nhánh code, hoặc từ chối bán.

Tài liệu này phân mọi quy tắc nghiệp vụ hiện có (SRS v2.0, brainstorm Điều phối, Liên quy trình, quyết định họp 09/10 và 10/10) thành 4 tầng, kèm cách làm để Delta vẫn được đúng như yêu cầu mà lõi sản phẩm không bị khoá vào Delta.

## 2. Bốn tầng

| Tầng | Định nghĩa | Ai quyết | Cách làm trong phần mềm | Ví dụ |
|---|---|---|---|---|
| **Lõi** | Đúng với mọi doanh nghiệp vận tải, giao nhận ở Việt Nam | Đội sản phẩm | Viết cứng trong sản phẩm, có test, mọi khách dùng chung | Kiểm số container theo ISO 6346; Lệnh vận tải có tổ hợp đầu kéo – mooc – container; app chạy khi mất sóng |
| **Cấu hình** | Cùng quy tắc, mỗi khách khác con số, danh sách hoặc tên gọi | Khách (admin của khách) | Tham số theo khách, có giá trị mặc định của sản phẩm; danh mục; mẫu quy trình | Ngưỡng 5.000.000 đ; ca trực 17h30–8h; danh sách lý do "Chuyển việc"; kỳ chốt ngày 25 |
| **Gói mở rộng** | Đúng với một nhóm khách (có xưởng riêng, có cây dầu riêng, chạy CBT, đường sắt, hàng lạnh) | Đội sản phẩm thiết kế; khách mua gói nào bật gói đó | Module bật/tắt theo hợp đồng, có điểm nối chuẩn với lõi | Xưởng sửa chữa; Cây dầu và đối tác cây dầu; Nhật ký nhiệt hàng lạnh; Đường sắt |
| **Riêng Delta** | Chỉ Delta cần, khách khác gần như chắc không dùng | Delta | Dữ liệu cấu hình của Delta, kết nối riêng (adapter), hoặc dịch vụ tuỳ chỉnh tính phí riêng. **Không sửa lõi** | Mã khách hàng "DK05"; tên phiếu dGas1–dGas5; truck sheet riêng kho Pan Hải An; tài khoản VETC tự nạp qua Vietcombank |

Nguyên tắc gác cổng: một yêu cầu của Delta chỉ vào **Lõi** khi trả lời "có" cả 3 câu ở Mục 6. Không chắc thì để **Cấu hình**, vì Cấu hình đổi lên Lõi dễ hơn rút từ Lõi xuống.

## 3. Phân loại quy tắc hiện có

Cột "Nếu viết cứng" ghi điều sẽ chặn bán cho khách khác.

### 3.1 Tổ chức, phân quyền, mã bản ghi

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| Dữ liệu theo Công ty → Chi nhánh → Cơ sở | Lõi (cấu trúc) + Cấu hình (số cấp, tên cấp) | Cây tổ chức nhiều cấp; khách đặt tên cấp | Khách 1 công ty 1 kho phải khai giả chi nhánh/cơ sở |
| Phân quyền theo chức năng + phạm vi dữ liệu | Lõi | — | — |
| Bộ 5 vai trò mẫu | Cấu hình | Mẫu vai trò khởi tạo, khách sửa được | Vai trò không khớp chức danh khách |
| Quyền gắn với việc (người được giao việc có quyền thanh toán của JobID đó) và quyền theo ca trực có bàn giao | Lõi (cơ chế) | Cơ chế "quyền có thời hạn, gắn bản ghi hoặc ca" | — |
| Ca trực 17h30–8h, cán bộ quản lý hiện trường giao lịch | Cấu hình | Giờ ca, ai được giao lịch | Khách làm 3 ca hoặc 24/7 không dùng được |
| Mã bản ghi có mã chi nhánh (`QT-[Mã chi nhánh]-[YY]-[XXXX]`) | Cấu hình | Mẫu sinh mã theo khách (`P-mau-ma-quy-trinh`) | Khách đã có quy ước mã riêng (thường gặp khi chuyển từ phần mềm cũ) |
| JobID / giao việc trái tuyến thì tự ghi nhận giao dịch nội bộ, tự hạch toán | Gói mở rộng "Đa chi nhánh, hạch toán nội bộ" | Bật khi khách có nhiều chi nhánh hạch toán riêng | Khách 1 pháp nhân, 1 chi nhánh bị sinh bút toán thừa |
| Chia lợi nhuận liên chi nhánh 50/50 theo lãi gộp | Cấu hình (trong gói trên) | Công thức chia: tỷ lệ %, cơ sở chia (lãi gộp, doanh thu), thời điểm hạch toán | Mỗi khách một chính sách chia; viết cứng là sai với mọi khách khác |

### 3.2 Hồ sơ dịch vụ (JobID), Yêu cầu vận tải, Lệnh vận tải

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| Chuỗi JobID → YCVT → Lệnh vận tải | Lõi | Khái niệm chuẩn ngành: hồ sơ dịch vụ (job file) → yêu cầu vận tải → lệnh vận tải | — |
| Tên "JobID", "YCVT", "CS", "Điều vận" | Cấu hình | Từ điển thuật ngữ theo khách (chỉ đổi nhãn hiển thị, không đổi dữ liệu) | Khách gọi "Booking", "Shipment", "Lô hàng" thấy phần mềm lạ |
| Loại JobID J01–J07 | Cấu hình | Danh mục loại hồ sơ, mỗi loại trỏ tới mẫu quy trình | Khách không có J07 (CBT) hoặc thêm loại mới phải sửa code |
| Trạng thái JobID, Lệnh vận tải | Lõi (khung trạng thái) + Cấu hình (tên hiển thị, trạng thái con) | Khung trạng thái cố định để báo cáo và tích hợp chạy được; khách đổi nhãn, thêm trạng thái con | Khách thêm bước duyệt riêng phải sửa máy trạng thái |
| JobID dừng khi nợ quá hạn, vượt hạn mức; chặn khi nợ xấu theo sổ phụ ngân hàng | Lõi (cơ chế chặn công nợ) + Cấu hình (điều kiện, ngưỡng, có cho duyệt ngoại lệ không) + kết nối (nguồn công nợ) | Nguồn công nợ là kết nối thay được (kế toán, ngân hàng) | Khách không dùng sổ phụ ngân hàng không có dữ liệu để chặn |
| 1 YCVT cho mỗi container; YCVT khai số xe, trừ dần khi lập Lệnh | Lõi | — | — |
| AI đọc chứng từ (Booking Note, eDO, EIR, phiếu cân, tờ khai + QR), người tạo duyệt, chỗ sửa lưu lại | Lõi (chứng từ chuẩn ngành Việt Nam) + Cấu hình (mẫu chứng từ riêng của khách) | Thư viện mẫu chứng từ dùng chung; mỗi khách thêm mẫu riêng. **Dữ liệu sửa của khách nào chỉ dùng cho khách đó**, trừ khi hợp đồng cho phép | Mô hình AI học từ dữ liệu Delta rồi dùng cho khách khác mà chưa có thoả thuận |
| Thời gian AI trả kết quả (P95 ≤ 10 giây, nền ≤ 60 giây) | Lõi | Cam kết chất lượng chung của sản phẩm | — |
| Gán trước DK05 + báo giá/hợp đồng + loại JobID rồi mới tải chứng từ | Lõi (quy trình) + Riêng Delta (tên DK05) | "Khách hàng" là đối tượng lõi; "DK05" chỉ là mã của Delta | Màn hình ghi "DK05" với khách khác |

### 3.3 Luồng giao nhận

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| 6 luồng FCL, LCL/CFS, air × xuất, nhập | Lõi, dưới dạng **mẫu quy trình** | Sản phẩm phát hành sẵn 6 mẫu theo thông lệ cảng Việt Nam; khách bật mẫu mình dùng, chỉnh bước tuỳ chọn | Khách chỉ làm FCL vẫn phải đi qua bước của air |
| Phân luồng theo 3 thuộc tính cảng/bãi (có ePort, có xe mới chọn được vỏ, thanh lý tờ khai online hay tại bãi) | Lõi (logic) + **dữ liệu chung** | Danh mục cảng/bãi Việt Nam do sản phẩm duy trì, dùng chung mọi khách; khách sửa đè được | Mỗi khách tự nhập lại danh mục cảng — mất một lợi thế bán hàng |
| Nút "Chuyển việc", 2 lý do (Hết giờ làm việc · Khác) | Lõi (nút) + Cấu hình (danh sách lý do) | — | Khách cần thêm lý do phải sửa code |
| Gợi ý 2–3 người nhận việc (gần cảng, số việc đang ôm, trong ca) | Lõi + Cấu hình (tiêu chí và trọng số) | — | — |
| Gộp giao việc Lệnh hạ vỏ theo vận đơn + nơi hạ, chỉ khi JobID có 1 container | Cấu hình | Quy tắc gộp bật/tắt, điều kiện số container | Khách gộp theo cách khác |
| Biên bản giao hàng điện tử + giấy; tự email cho CS và khách khi lái xe xác nhận | Lõi + Cấu hình (mẫu biên bản theo loại hàng, người nhận email) | — | — |
| Truck sheet bắt buộc riêng với kho Pan Hải An | Cấu hình | Danh mục "chứng từ bắt buộc theo kho/cảng" | Tên kho cụ thể nằm trong code |
| Không kết nối ePort, chỉ lưu lệnh và EIR | Lõi (hiện tại) | Để chỗ cho kết nối ePort sau này như một kết nối thay được | — |
| Không quản lý vỏ container ở giai đoạn 1; chi phí sửa container ghi trên Lệnh | Riêng Delta (quyết định phạm vi) | Lõi nên có chỗ cắm gói "Quản lý vỏ container" về sau; không thiết kế dữ liệu theo giả định "không bao giờ có vỏ" | Khách sở hữu vỏ (SOC) không có chỗ quản lý |

### 3.4 Hiện trường, lái xe

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| Điểm chụp ảnh định vị bắt buộc, thiếu thì chặn bước | Lõi (cơ chế) + Cấu hình (danh sách điểm theo loại hàng) | — | — |
| App chạy khi mất sóng, giờ và vị trí theo lúc chụp | Lõi | — | — |
| Báo thay đổi, vấn đề giữa chặng; Lệnh lưu kế hoạch và thực tế | Lõi + Cấu hình (danh sách loại thay đổi) | — | — |
| Nhật ký nhiệt độ hàng lạnh, chu kỳ nhắc theo loại hàng | Gói "Hàng lạnh" + Cấu hình (chu kỳ) | — | Khách không chạy hàng lạnh thấy màn thừa |
| Theo dõi mã vạch gốc hàng air | Gói "Hàng không" (hoặc Lõi nếu đa số khách làm air) | — | — |
| Tổ hợp đầu kéo – mooc – container theo Lệnh; đổi mooc, bỏ mooc giữa đường | Lõi | — | — |
| Danh sách loại phương tiện gồm cả container DC/Reefer, máy phát, trạm bơm dầu | Cấu hình, **sửa mô hình** | Tách "phương tiện" khỏi "thiết bị" (container, máy phát) trong lõi; danh sách loại là cấu hình | Mô hình "container là một phương tiện" của SRS v2.0 khó bán cho khách khác và làm rối tổ hợp đầu kéo – mooc – container |

### 3.5 Chi phí, thanh toán, hạch toán

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| Chi phí gắn đúng Lệnh, JobID; duyệt Lệnh thì chi phí lên JobID | Lõi | — | — |
| Ngưỡng 5.000.000 đ: dưới thì tạm ứng, trên thì tạo việc cho CS + kế toán | Cấu hình | Ngưỡng và cách xử lý mỗi bậc | Mỗi khách một quy chế tài chính |
| Loại phí × địa điểm → cách hạch toán (thu nhập chịu thuế lái xe, chi hộ, trả hộ, chi phí vận hành) | Lõi (cơ chế + 4 nhóm hạch toán theo thuế Việt Nam) + Cấu hình (bảng loại phí, địa điểm) | — | — |
| Định mức depot 150.000 đ Nam Khánh, 160.000 đ Phú Lợi | Riêng Delta (dữ liệu) | Nhập vào bảng định mức của Delta | Con số trong code |
| Phí lưu ca xe quá 72 giờ | Cấu hình | Số giờ miễn phí, đơn giá, nguồn giờ (GPS hay ảnh) | — |
| Delta **bỏ** luồng xin duyệt chi ngoài định mức trên app | Cấu hình (tắt với Delta) | **Giữ trong sản phẩm, tắt mặc định với Delta.** Khách khác thường cần luồng này | Xoá hẳn thì phải làm lại khi bán khách thứ hai |
| Delta **bỏ** theo dõi tiền hoàn nâng vỏ 7 ngày | Cấu hình (tắt với Delta) | Như trên | Như trên |
| Đơn giá đường sắt CS nhập tay (giai đoạn 1), lấy từ báo giá Sales (giai đoạn 2) | Gói "Đường sắt" + Lõi (bảng giá theo hợp đồng) | Bảng giá theo hợp đồng là lõi; nguồn giá (tay hay Sales) là cấu hình | — |
| Bên xuất hoá đơn khác khách đặt dịch vụ | Lõi | — | — |
| Thanh toán trả hộ, QR, UNC, API ngân hàng | Gói "Tài chính" + kết nối | Kết nối ngân hàng thay được; Vietcombank là kết nối đầu tiên | Chỉ chạy với khách dùng Vietcombank |

### 3.6 Nhiên liệu, xưởng

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| Định mức nhiên liệu theo phương tiện; cấp dầu gắn Lệnh; vượt định mức đi phiếu riêng | Lõi (khách có đội xe riêng) | — | — |
| Tên phiếu dGas1–dGas5 (cấp quản lý, cấp xưởng, cấp vận tải, đổ đầy bình, chốt dầu) | Riêng Delta (tên) + Cấu hình (loại phiếu) | Lõi có "phiếu cấp nhiên liệu" với loại phiếu do khách khai | Khách khác không hiểu "dGas4" |
| Cây dầu nội bộ, cây dầu mua ngoài, nhân viên đối tác cây dầu dùng app | Gói "Nhiên liệu" | Chỉ bán cho khách có cây dầu riêng hoặc ký đối tác cây dầu | Khách đổ dầu ngoài hoàn toàn thấy cả module thừa |
| Lưu lượng dầu dư khi mua ngoài theo hoá đơn lẻ để cấp bù | Gói "Nhiên liệu" | — | — |
| Xưởng: lệnh sửa chữa, báo giá, kho phụ tùng, kiểm kê, rác thải | Gói "Bảo dưỡng đội xe" | Bán riêng hoặc kèm; nối với lõi qua phương tiện và chi phí | Khách thuê sửa ngoài hoàn toàn vẫn phải cài xưởng |
| Mã "Khách hàng DK05", duyệt "DK05 cấp 2" | Riêng Delta (tên) + Cấu hình (cấp duyệt khách hàng) | — | — |

### 3.7 Kết nối bên ngoài

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| GPS và cảm biến dầu EUP | Kết nối thay được | Lõi định nghĩa "nhà cung cấp GPS"; EUP là kết nối đầu tiên | Khách dùng Vietmap, Bình Anh, Adsun… không dùng được |
| VETC là nguồn chuẩn toạ độ và chi phí khi lệch Vietmap | Lõi (chốt 2026-10-12) | VETC là nguồn chuẩn cho mọi khách | — |
| Vé đường bộ 3 loại; vé tránh trạm trả vào lương lái xe | Lõi (phân loại vé) + Riêng Delta (chính sách lương) | Lõi chỉ phân loại và chuyển dữ liệu; chính sách lương là cấu hình hoặc nằm ngoài sản phẩm | Lương là chính sách nội bộ, khác mỗi khách |
| Tài khoản VETC tự nạp qua Vietcombank (dưới 15/5 triệu thì nạp lên 150/50 triệu) | Riêng Delta | Cấu hình ngưỡng nạp + kết nối ngân hàng của khách | — |
| MISA lấy hoá đơn điện tử | Kết nối thay được | Lõi định nghĩa "nhà cung cấp hoá đơn điện tử, phần mềm kế toán"; MISA là kết nối đầu tiên | Khách dùng FAST, Bravo, Viettel… không dùng được |
| Kế hoạch Ratraco ngày n-1 | Gói "Đường sắt" | Nhập kế hoạch theo mẫu file; mẫu Ratraco là mẫu đầu tiên | — |
| Google Maps cung đường, giờ đến dự kiến | Kết nối thay được | — | — |

### 3.8 Giao diện, thương hiệu

| Quy tắc (theo Delta) | Tầng | Cách tổng quát hoá | Nếu viết cứng |
|---|---|---|---|
| Tên app "Delta Super App", logo Delta | Cấu hình (gắn nhãn theo khách) | Một app chung chọn khách khi đăng nhập, hoặc mỗi khách một bản build mang tên riêng — cần quyết định (Mục 7) | Khách khác không chấp nhận app mang tên Delta |
| Quy tắc giao diện GR, CMP, E-common; design system không gắn thương hiệu | Lõi + Cấu hình (logo, màu ô logo) | Thương hiệu khách chỉ thay ô logo (`P-logo`, `P-mau-logo`); bộ màu và component giữ trung tính, không đổi theo khách (chốt 12/10/2026) | — |
| Tiếng Việt, Tiếng Anh | Lõi | — | — |
| Câu chữ ngôi "bạn", không "Vui lòng" | Lõi | — | — |

## 4. Mười điểm dễ chặn bán nhất

Xếp theo mức khó gỡ nếu đã viết cứng:

1. **AI học từ dữ liệu Delta** rồi dùng chung cho khách khác — vướng hợp đồng và bảo vệ dữ liệu, không phải lỗi kỹ thuật. Tách dữ liệu học theo khách ngay từ đầu.
2. **Container là một loại phương tiện** (SRS v2.0) — sai mô hình, càng làm Điều phối càng khó gỡ. Nên sửa trước khi viết SRS Điều phối.
3. **Hạch toán nội bộ liên chi nhánh và công thức chia 50/50** — dễ lọt vào lõi vì nằm sâu trong luồng chi phí.
4. **Chặn công nợ dựa vào sổ phụ ngân hàng** — phụ thuộc nguồn dữ liệu Delta có.
5. **Kết nối viết thẳng cho EUP, MISA, VETC, Vietcombank** thay vì qua lớp kết nối chung.
6. **Tên gọi Delta trong dữ liệu và giao diện**: DK05, dGas1–5, J01–J07, "Delta Super App".
7. **Con số chính sách**: 5 triệu, 72 giờ, 17h30–8h, ngày 25, 7 ngày, định mức depot.
8. **Tính năng Delta từ chối bị xoá khỏi thiết kế** (duyệt chi ngoài định mức, theo dõi tiền hoàn) — khách khác sẽ hỏi.
9. **Một chuỗi trạng thái cố định** không cho khách thêm bước duyệt.
10. **Danh mục cảng, kho Delta trộn với danh mục dùng chung** — mất cơ hội làm dữ liệu cảng Việt Nam dùng chung cho mọi khách.

## 5. Phương án kết hợp

**Một bộ code, Delta là khách số 1.** Không tách nhánh code riêng cho Delta. Mọi khác biệt của Delta đi qua 6 cơ chế dưới đây.

| Cơ chế | Dùng cho tầng | Phần mềm cần có | Ví dụ với Delta |
|---|---|---|---|
| Tham số theo khách (có mặc định) | Cấu hình | Màn cài đặt của admin khách; mỗi tham số có giá trị mặc định của sản phẩm | Ngưỡng 5 triệu; 72 giờ; ca trực; kỳ chốt |
| Danh mục theo khách + danh mục dùng chung | Cấu hình | Danh mục 2 lớp: lớp sản phẩm (cảng Việt Nam, loại chứng từ) và lớp khách sửa đè | Danh mục cảng/bãi; loại phí × địa điểm |
| Mẫu quy trình | Lõi, Cấu hình | Sản phẩm phát hành mẫu; khách bật/tắt bước tuỳ chọn, đổi nhãn; khung trạng thái lõi giữ nguyên | 6 luồng FCL/LCL/air |
| Bật/tắt tính năng và gói | Gói mở rộng, Cấu hình | Cờ tính năng theo khách, gắn với gói hợp đồng | Tắt duyệt chi ngoài định mức với Delta; bật gói Nhiên liệu, Xưởng |
| Từ điển thuật ngữ | Cấu hình | Đổi nhãn hiển thị theo khách | JobID, YCVT, DK05, dGas |
| Lớp kết nối | Kết nối | Giao diện chuẩn cho GPS, vé đường bộ, hoá đơn điện tử, kế toán, ngân hàng; mỗi nhà cung cấp là một bộ nối | EUP, VETC, MISA, Vietcombank |

Phần không đi được qua 6 cơ chế trên → làm **dịch vụ tuỳ chỉnh** cho Delta: tách thành bộ nối hoặc báo cáo riêng, tính phí riêng, không đụng lõi.

## 6. Quy tắc gác cổng khi nhận yêu cầu mới

Mỗi yêu cầu mới (của Delta hay khách sau) trả lời 3 câu trước khi đưa vào SRS:

1. Có ít nhất 2 doanh nghiệp cùng ngành cần đúng quy tắc này không (đối thủ có làm, hoặc đã gặp ở khách khác)?
2. Có thể viết quy tắc mà không có con số, tên riêng, tên đối tác của khách không?
3. Nếu khách khác muốn ngược lại, có tắt hoặc đổi được mà không sửa code không?

| Kết quả | Xếp tầng |
|---|---|
| Có cả 3 | Lõi |
| Có câu 1, 3 nhưng có con số hoặc tên riêng | Lõi + Cấu hình (tách con số ra tham số) |
| Chỉ đúng một nhóm khách | Gói mở rộng |
| Không câu nào | Riêng Delta |

**Ghi vào tài liệu:** thêm nhãn tầng `[Lõi]` / `[Cấu hình]` / `[Gói: tên gói]` / `[Riêng Delta]` cạnh nhãn nguồn `[SOP to-be]` / `[SOP+]` / `[Mới]` đang dùng trong brainstorm; SRS mới thêm cột "Tầng" ở bảng FR và BR. Như vậy khi review, ai cũng thấy ngay quy tắc nào khoá vào Delta.

Con số chính sách không viết thẳng vào quy tắc mà gọi qua mã `P-…` trong [[docs/_product/tenant-parameters|bảng tham số tenant]]. Cách gắn nhãn, gate và lint: `.claude/rules/saas-layer.md`, kiểm bằng `python3 _scripts/saas-layer-lint.py <file>`.

## 7. Việc cần quyết trước khi viết SRS mới

| # | Việc | Ai quyết | Vì sao gấp |
|---|---|---|---|
| 1 | **Quyền khai thác phần mềm đồng sở hữu** — hợp đồng outsource quy định phần mềm thuộc cả hai bên (xác nhận 2026-10-12). Còn phải kiểm 3 điều khoản: (a) mỗi bên có được tự bán, cấp quyền cho khách khác mà không cần Delta đồng ý không, có phải chia doanh thu không; (b) có điều khoản độc quyền hoặc không cạnh tranh trong ngành logistics không; (c) SOP, quy trình, dữ liệu Delta cung cấp có là thông tin bảo mật không — nếu có, sản phẩm chỉ dùng lại phần mềm, không mang theo nội dung riêng của Delta | Lãnh đạo, pháp chế | Đồng sở hữu chưa chắc đã cho phép một bên tự khai thác thương mại; (c) quyết định phần nào ở tầng "Riêng Delta" phải tách hẳn khỏi sản phẩm |
| 2 | Dữ liệu Delta (chứng từ, chỗ AI sửa, danh mục) có được dùng để cải thiện sản phẩm chung không | Lãnh đạo + Delta | Ảnh hưởng thiết kế AI đọc chứng từ (CHG-27) |
| 3 | Một app chung có chọn khách, hay mỗi khách một bản app mang tên riêng | Đội sản phẩm | Ảnh hưởng đăng nhập, phân phối app, tên "Delta Super App" |
| 4 | Sửa mô hình "container là phương tiện" trước khi viết SRS Điều phối | BA + kỹ thuật | Rẻ nhất nếu sửa bây giờ |
| 5 | Danh sách gói bán (Xưởng, Nhiên liệu, Hàng lạnh, Đường sắt, CBT, Tài chính, Đa chi nhánh) | Đội sản phẩm | Quyết định chỗ nối giữa lõi và gói |

## 8. Bước tiếp theo đề xuất

1. Chốt việc 1 (3 điều khoản a–c) và việc 2 ở Mục 7 (không phải việc của BA, nhưng chặn việc bán cho khách khác). Trong lúc chờ, vẫn làm được bước 2–4 vì tách lõi và cấu hình có lợi cho cả Delta.
2. Gắn nhãn tầng cho các dòng trong brainstorm Điều phối và các dòng ✅ của danh sách thay đổi so với SRS v2.0, trước khi viết SRS Điều phối.
3. Tách các con số chính sách ra danh sách tham số chung (một bảng duy nhất cho toàn sản phẩm, ghi giá trị mặc định và giá trị của Delta).
4. Thiết kế lớp kết nối cho GPS, vé đường bộ, hoá đơn điện tử, ngân hàng trước khi dev viết kết nối EUP, VETC, MISA.
5. Khi có khách tiềm năng thứ hai, chạy lại Mục 3 với quy trình của họ để kiểm phân loại.
