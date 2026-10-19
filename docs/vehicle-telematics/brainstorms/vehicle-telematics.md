---
type: brainstorm
feature: vehicle-telematics
status: draft
status_changed: 2026-10-18
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-15
links:
  - docs-input/sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md
  - docs-input/tich-hop/vis-sim-cong-tac-chuan-bi/vis-sim-cong-tac-chuan-bi.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_shared/project-profile.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_product/tenant-parameters.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Dữ liệu vận hành xe — kết nối GPS, vé đường bộ và phát hiện sự việc

## 1. Idea Seed

"feed SRC-06 và brainstorm (vẫn đi từ đầu full round) và đưa đề xuất, ngoài ra bạn phải check phần phương tiện hiện tại đang có gì (module xưởng có bàn giao thu hồi định mức phương tiện) bên danh mục có quản lý thông tin phương tiện"

Mô tả đã chốt: phần mềm tự đọc dữ liệu GPS, cảm biến dầu của từng xe và giao dịch vé VETC, đổi thành sự việc có ý nghĩa (đã đến nơi, kẹt xe, nổ máy ngủ, qua trạm hay tránh trạm, đổ dầu, hút dầu, số km), gắn đúng Lệnh và đúng xe, để duyệt Lệnh, tính bù dầu, đối soát vé và dầu mà không ai phải nhập tay.

## 2. Context

**Vấn đề hiện tại (đã xác nhận):**

| Mã | Vấn đề |
|---|---|
| a | Kế toán đối soát hoá đơn VETC tổng bằng tay cuối tháng |
| b | Bù dầu kẹt xe dựa vào lời lái xe kể |
| c | Hút dầu, đổ thiếu phát hiện muộn hoặc không phát hiện |
| d | Lái xe tránh trạm mà không ai biết |

**Vì sao lúc này:** Delta đang chuẩn bị làm việc với EUP, VETC và Vietcombank cho VIS (bản Công tác chuẩn bị 11/10/2026). Toàn bộ VIS vào giai đoạn 1, go-live 30/03/2027.

**Phạm vi feature này.** VIS được lồng vào các feature đã có; feature này chỉ giữ phần dùng chung chưa có chỗ (DEC-100):
- Kết nối với nhà cung cấp GPS, cảm biến dầu (EUP), đơn vị thu phí (VETC), dịch vụ bản đồ.
- Phát hiện sự việc từ dữ liệu xe theo bộ ngưỡng của từng khách.
- Danh mục trạm thu phí dùng chung mọi khách (DEC-101).
- Vòng đời "sự việc cần xử lý" mà các feature khác dùng chung.

| Phần của VIS | Feature nhận |
|---|---|
| ETA, đã đến, kẹt xe, qua và tránh trạm, khớp vé, bù dầu kẹt xe, tìm vỏ, dự toán vé, nổ máy ngủ trong Lệnh | `transport-dispatch` Nhóm I |
| Km, dầu tồn trên hồ sơ xe; thẻ ETC, mã GPS; bàn giao, thu hồi; hút dầu; xe chạy ngoài Lệnh; nổ máy ngủ ngoài Lệnh; báo cáo theo xe, lái xe | `vehicle-management` |
| Định mức l/giờ; mức "Đầu kéo không" cho dầu tìm vỏ; chạy định mức lấy km, dầu từ GPS | `fuel-allowance` (chưa có thư mục) |
| Đối soát dầu thực đổ với phiếu cấp dầu; xác nhận đầy bình ở dGas4, dGas5; dầu chờ nhận nhận qua dGas3 | `fuel-issuing` (chưa có thư mục, BL-152) |
| Lịch nhắc bảo dưỡng theo km GPS | `reminders` (chưa có thư mục) |
| Kiểm phát sinh VETC cuối kỳ, vé mồ côi | `invoice-management` (brainstorm SIM đang chạy) |

**Ngoài phạm vi:** tài khoản mẹ VETC và Vietcombank tự nạp tiền (cài ở ngân hàng, ngoài phần mềm); xe thuê ngoài, xe nhà thầu (DEC-102); điều xe tự động (P2, `transport-dispatch` F9).

**Nguồn:** Vehicle Intelligent Service — VIS (08/10/2026); SIM & VIS — Công tác chuẩn bị (11/10/2026) mục 2.2, 3.3, 3.4; SRS LG v2.0 Feature 04.01 Phương tiện và Barem, sensor iGAS; SRS mobile Epic 06 Phiếu cấp dầu; phỏng vấn 14–15/10/2026.

**Nhãn:** [SOP to-be] = VIS đã yêu cầu · [SOP+] = VIS có nêu, đề xuất làm thêm · [Mới] = VIS chưa có. Nhãn tầng theo `docs/_product/saas-core-vs-tenant.md`.

## 3. User Types (preliminary)

Phân quyền theo chức năng, không cố định vai trò. Luồng ghi theo vai trò nghiệp vụ.

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Quản lý phương tiện | Biết hút dầu, xe chạy sai mục đích khi đã muộn | Cảnh báo tức thời có bằng chứng, xử lý một chỗ |
| Người duyệt Lệnh, điều vận | Không có số liệu thật để duyệt bù dầu, vé | Số liệu GPS và vé đã gắn sẵn trên Lệnh |
| Kế toán | Đối soát vé VETC bằng tay | Vé tự khớp, chỉ xử lý phần phát sinh |
| Quản lý cây dầu | Không biết cây dầu bơm thiếu | Cảnh báo lệch dầu thực đổ |
| Lái xe | Bị trừ tiền mà không thấy căn cứ | Xem được số liệu của chính mình |
| Admin khách | Mỗi khách một nhà cung cấp GPS, một chính sách | Khai nhà cung cấp, đặt ngưỡng không cần sửa phần mềm |
| Đội sản phẩm | Khách mới phải tự vẽ hàng trăm trạm | Duy trì một danh mục trạm dùng chung |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Quản lý phương tiện | Xử lý cảnh báo hút dầu, xe chạy ngoài Lệnh | Khi có | cao | Mất dầu, dùng xe sai mục đích |
| Quản lý phương tiện | Xem nổ máy ngủ, tiêu hao theo lái xe | Mỗi tháng | trung | Hao phí dầu kéo dài |
| Quản lý cây dầu | Xử lý lệch dầu thực đổ | Mỗi ngày | cao | Cây dầu bơm thiếu, gian lận |
| Admin khách | Khai nhà cung cấp, đặt ngưỡng | Hiếm | trung | Ngưỡng sai thì cảnh báo sai |
| Đội sản phẩm | Thêm trạm, cập nhật biểu phí | Hiếm | trung | Trạm thiếu thì báo tránh trạm sai |

## 4. Capabilities Breakdown

### P0 — must have

**Nhóm K — kết nối**
- K1 [SOP to-be] [Lõi] Nhận dữ liệu xe từ nhà cung cấp GPS: vị trí, tốc độ, máy nổ hay tắt, mức dầu, km. Nhà cung cấp gửi sự việc khi trạng thái xe đổi; phần mềm chỉ chủ động đọc khi xe tắt máy, mỗi `P-chu-ky-doc-dau-tat-may` (Delta: 30 phút; VIS mục 2.2 ghi 30–60 phút). EUP là nhà cung cấp đầu tiên.
- K2 [SOP to-be] [Lõi] Nhận giao dịch trừ tiền theo xe từ đơn vị thu phí (VETC đầu tiên): giao dịch gửi về khi trừ tiền nếu đơn vị đó hỗ trợ, và tra cứu theo xe trong một khung giờ.
- K3 [SOP to-be] [Lõi] Dịch vụ bản đồ tính cung đường, quãng đường, ETA; có dữ liệu tắc đường thì dùng thêm cho kẹt cứng (S4). Nhà cung cấp chờ khách (OQ-1).
- K4 [SOP+] [Lõi] [Cấu hình] Mỗi khách khai nhà cung cấp GPS, tài khoản thu phí, dịch vụ bản đồ của mình. Feature khác chỉ nhận sự việc đã xử lý, không biết nhà cung cấp là ai, nên đổi nhà cung cấp không phải sửa các feature đó.

**Nhóm S — phát hiện sự việc**
- S1 [SOP to-be] [Lõi] Đã đến: xe vào vùng của địa điểm giao nhận (cảng, bãi, kho của Lệnh) thì ghi giờ đến thật.
- S2 [SOP to-be] [Lõi] [Cấu hình] Kẹt xe: máy nổ, xe nhích dưới `P-van-toc-ket-xe` (Delta: 5 km/h), liên tục quá `P-thoi-gian-ket-xe` (Delta: 10 phút); kết thúc khi xe chạy lại từ ngưỡng đó trở lên.
- S3 [SOP to-be] [Lõi] [Cấu hình] Nổ máy ngủ: máy nổ, xe đứng yên hẳn, quá `P-thoi-gian-no-may-ngu` (Delta: 10 phút); kết thúc khi xe chạy. Trong Lệnh thì gắn vào Lệnh, ngoài Lệnh thì gắn lái xe đang giữ xe theo lịch sử bàn giao.
- S4 [SOP+] [Lõi] [Cấu hình] Kẹt cứng: khoảng đứng yên hẳn được tính là kẹt xe khi có ít nhất một dấu hiệu: (a) nằm giữa hai đoạn kẹt xe cách nhau không quá `P-khoang-dung-giua-ket-xe` (chưa chốt); (b) lái xe báo vấn đề giữa chặng trên app (tai nạn, tắc đường, đường cấm); (c) dịch vụ bản đồ báo tắc đường hoặc sự cố tại vị trí đó. Không có dấu hiệu nào thì là nổ máy ngủ. Trạm dừng nghỉ, cây xăng không xét kẹt cứng. Chờ khách (OQ-53 ở `transport-dispatch`).
- S5 [SOP to-be] [Lõi] Qua trạm: xe vào vùng đa giác của trạm trong danh mục (cách vẽ vùng và xét đoạn nối hai điểm GPS: `transport-dispatch` E9, E10).
- S6 [SOP to-be] [Gói: Giám sát nhiên liệu] [Cấu hình] Đổ dầu: dầu trong bình tăng liên tục quá `P-nguong-do-dau` (Delta: 20 lít trong 10 phút, dùng chung ngưỡng với EUP), xe đứng yên; ghi giờ, toạ độ, dầu trước, số lít vào bình. Đối soát với phiếu ở `fuel-issuing`.
- S7 [SOP to-be] [Gói: Giám sát nhiên liệu] [Cấu hình] Hút dầu: dầu giảm quá `P-nguong-hut-dau` (Delta: 5 lít trong dưới 3 phút, dùng chung ngưỡng với EUP); ghi giờ, toạ độ, dầu trước và sau. Tự bỏ qua khi xe có lệnh sửa chữa đang mở tại xưởng hoặc số đo tụt rồi trở lại ngay. EUP đủ dữ liệu thì dùng thẳng của EUP (OQ-2).
- S8 [Mới] [Lõi] [Cấu hình] Xe chạy ngoài Lệnh: xe không có Lệnh đang chạy mà di chuyển quá `P-nguong-chay-ngoai-lenh` (chưa chốt). Trường hợp miễn chờ khách (OQ-3 ở `vehicle-management`).
- S9 [SOP to-be] [Lõi] Km theo GPS và dầu tồn gần nhất của từng xe, ghi về hồ sơ xe ở `vehicle-management`.
- S10 [Mới] [Lõi] [Cấu hình] Nhắc lái xe tắt máy trên app khi nổ máy ngủ, theo `P-nhac-tat-may` (chờ khách, OQ-5). Hoãn được nếu trễ go-live (review r17).

**Nhóm T — danh mục trạm thu phí dùng chung**
- T1 [SOP+] [Lõi] Danh mục trạm thu phí dùng chung mọi khách, đội sản phẩm duy trì: tên, toạ độ, vùng đa giác theo từng chiều, giá vé theo loại xe, ngày hiệu lực (DEC-101). Khách mới dùng được ngay; khách chỉ khai trạm riêng nếu thiếu. Nguồn ban đầu: hỏi VETC (OQ-3).
- T2 [Mới] [Lõi] Giao dịch thu phí ở trạm chưa có trong danh mục: ghi tiền theo giao dịch, đánh dấu "Trạm chưa có trong danh mục", báo đội duy trì bổ sung. Chờ khách (OQ-7).

**Nhóm X — sự việc cần xử lý**
- X1 [SOP+] [Lõi] [Cấu hình] Hút dầu, xe chạy ngoài Lệnh, lệch dầu thực đổ là "sự việc cần xử lý": Mới → Vi phạm, Hợp lệ (bắt lý do) hoặc Lỗi thiết bị. Quá `P-han-xu-ly-su-viec` (chưa chốt) chưa xử lý thì nhắc người xử lý, báo trưởng bộ phận. Mở lại được khi kỳ chưa chốt, kèm lý do.
- X2 [Mới] [Lõi] Hai người cùng xử lý một sự việc: người lưu sau thấy ai đã xử lý, không ghi đè. Hoãn được nếu trễ go-live (review r17).

**Nhóm G — dữ liệu thiếu, sai**
- G1 [SOP+] [Lõi] Dữ liệu GPS về muộn (xe mất sóng rồi có lại) được xử lý theo giờ thật của dữ liệu, không theo giờ nhận.
- G2 [SOP+] [Lõi] [Cấu hình] Một xe báo lỗi thiết bị quá `P-so-lan-loi-cam-bien` lần trong kỳ (chưa chốt) thì báo quản lý phương tiện kiểm tra thiết bị. Hoãn được nếu trễ go-live (review r17).
- G3 [Mới] [Lõi] Thẻ ETC gắn nhầm xe: giao dịch thu phí của xe A ở trạm X trong khi GPS xe A lúc đó ở nơi khác thì không ghi vào Lệnh, cảnh báo "nghi gắn nhầm thẻ ETC". Chờ khách (OQ-7). Hoãn được nếu trễ go-live (review r17).
- G4 [Mới] [Lõi] Trừ trùng: hai giao dịch cùng xe, cùng trạm, cách nhau vài phút thì ghi một lượt, lượt còn lại đánh dấu "nghi trừ trùng" để kế toán khiếu nại. Chờ khách (OQ-7). Hoãn được nếu trễ go-live (review r17).
- G5 [SOP+] [Lõi] [Cấu hình] Dữ liệu GPS thô giữ `P-thoi-gian-giu-gps` (chưa chốt) để tra ngược cuối kỳ, quá hạn thì xoá. Hoãn được nếu trễ go-live (review r17).

**Nhóm R — kỳ và báo cáo**
- R1 [SOP+] [Lõi] Kỳ báo cáo là tháng, khớp kỳ chốt dầu; xem thêm theo khoảng ngày tuỳ ý. Sự việc kéo qua nửa đêm, qua tháng tính theo giờ bắt đầu; số liệu của Lệnh tính theo ngày duyệt Lệnh (chờ khách, OQ-9).

### P1 — should have

Chưa phân mức: mọi phần đã chốt đều vào giai đoạn 1.

### P2 — nice to have

- Điều xe tự động dùng dữ liệu xe: `transport-dispatch` F9.

## 5. Core Flows (Happy Path)

### 5.1 Nhận dữ liệu và phát hiện sự việc

1. Nhà cung cấp GPS gửi dữ liệu của một thiết bị.
2. Phần mềm tìm xe đang gắn thiết bị đó (lịch sử gắn thiết bị ở `vehicle-management`).
3. Phần mềm tìm Lệnh đang chạy của xe; không có thì tìm lái xe đang giữ xe theo lịch sử bàn giao.
4. Áp ngưỡng của khách, ra sự việc (S1–S9).
5. Gửi sự việc cho feature nhận: trên Lệnh → `transport-dispatch`; theo xe → `vehicle-management`; đổ dầu → `fuel-issuing`.

```
 NHÀ CUNG CẤP GPS        PHẦN MỀM (vehicle-telematics)              FEATURE NHẬN
 Dữ liệu thiết bị ─────► Tìm xe theo thiết bị
                         Tìm Lệnh đang chạy, hoặc lái xe đang giữ xe
                         Áp ngưỡng của khách
                         ◇ Ra sự việc nào?
                         ├─ Đến nơi, kẹt xe, qua trạm, nổ máy ngủ trong Lệnh ──► Lệnh vận tải
                         ├─ Hút dầu, chạy ngoài Lệnh, nổ máy ngủ ngoài Lệnh ──► Quản lý phương tiện
                         ├─ Đổ dầu ──────────────────────────────────────────► Cấp dầu
                         └─ Km, dầu tồn ──────────────────────────────────────► Hồ sơ xe
 ĐƠN VỊ THU PHÍ
 Giao dịch trừ tiền ───► Tìm xe theo thẻ ETC ─► khớp lượt qua trạm của Lệnh ──► Lệnh vận tải
```

### 5.2 Phân loại máy nổ mà xe chậm hoặc đứng

1. Máy nổ, quá 10 phút, xe nhích dưới 5 km/h: kẹt xe.
2. Máy nổ, quá 10 phút, xe đứng yên hẳn: xét kẹt cứng (S4).
3. Có dấu hiệu kẹt cứng: kẹt xe. Không có: nổ máy ngủ.
4. Kẹt xe trong Lệnh: cộng đề xuất bù dầu trên Lệnh. Nổ máy ngủ: gắn Lệnh hoặc lái xe đang giữ xe, không bù.

```
 ◇ Máy nổ, quá 10 phút?
 └─ Có ─► ◇ Xe nhích dưới 5 km/h?
          ├─ Có ─► Kẹt xe ─► trong Lệnh: cộng đề xuất bù dầu
          └─ Không, đứng yên hẳn ─► ◇ Kẹt cứng: (a) giữa 2 đoạn kẹt · (b) lái xe báo · (c) bản đồ báo tắc?
                                    ├─ Có ─► Kẹt xe
                                    └─ Không ─► Nổ máy ngủ (gắn Lệnh hoặc lái xe đang giữ xe)
```

### 5.3 Xử lý sự việc cần xử lý

1. Phần mềm tạo sự việc (hút dầu, chạy ngoài Lệnh, lệch dầu thực đổ), gửi cảnh báo cho người xử lý theo chi nhánh khai thác xe.
2. Người xử lý mở sự việc từ thông báo, xem bằng chứng (giờ, vị trí trên bản đồ, số liệu).
3. Người xử lý chọn Vi phạm, Hợp lệ (bắt lý do) hoặc Lỗi thiết bị.
4. Vi phạm gắn lái xe đang giữ xe lúc xảy ra, vào báo cáo cuối kỳ.

### 5.4 Duy trì danh mục trạm thu phí

1. Đội sản phẩm thêm trạm: tên, toạ độ, vùng đa giác từng chiều, giá theo loại xe, ngày hiệu lực.
2. Biểu phí đổi: thêm giá mới với ngày hiệu lực mới, giữ giá cũ cho dữ liệu cũ.
3. Có giao dịch ở trạm lạ (T2): đội sản phẩm nhận báo, bổ sung trạm.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| D1 | 5.2 | Máy nổ quá 10 phút, xe nhích dưới 5 km/h | Kẹt xe | Sang D2 |
| D2 | 5.2 | Xe đứng yên hẳn có dấu hiệu kẹt cứng | Kẹt xe | Nổ máy ngủ |
| D3 | 5.1 | Xe có Lệnh đang chạy | Gắn sự việc vào Lệnh | Gắn lái xe đang giữ xe |
| D4 | S7 | Xe có lệnh sửa chữa mở, hoặc số đo trở lại ngay | Bỏ qua | Cảnh báo hút dầu |
| D5 | S8 | Xe không có Lệnh mà di chuyển, không thuộc trường hợp miễn | Cảnh báo | Bỏ qua |
| D6 | T2 | Trạm của giao dịch có trong danh mục | Khớp bình thường | Đánh dấu trạm chưa có, báo đội duy trì |
| D7 | G3 | GPS xe ở trạm lúc có giao dịch | Khớp bình thường | Nghi gắn nhầm thẻ ETC |

### 6.2 Scenario Matrix

| Máy | Tốc độ | Trong Lệnh | Dấu hiệu kẹt cứng | Kết quả |
|---|---|---|---|---|
| Nổ, quá 10 phút | Trên 0, dưới 5 km/h | Có | — | Kẹt xe, đề xuất bù dầu |
| Nổ, quá 10 phút | Trên 0, dưới 5 km/h | Không | — | Kẹt xe, không có Lệnh để bù, chỉ ghi nhận |
| Nổ, quá 10 phút | 0 | Có | Có | Kẹt xe, đề xuất bù dầu |
| Nổ, quá 10 phút | 0 | Có | Không | Nổ máy ngủ, gắn Lệnh, không bù |
| Nổ, quá 10 phút | 0 | Không | — | Nổ máy ngủ, gắn lái xe đang giữ xe |
| Tắt | — | — | — | Không ghi; đọc mức dầu theo chu kỳ tắt máy |

### 6.3 State Transitions

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Sự việc cần xử lý | — | Mới | Phần mềm phát hiện, gửi cảnh báo | — |
| Sự việc cần xử lý | Mới | Vi phạm · Hợp lệ · Lỗi thiết bị | Người xử lý chọn; Hợp lệ bắt lý do | Mở lại được khi kỳ chưa chốt, kèm lý do |
| Sự việc cần xử lý | Mới | Quá hạn | Quá `P-han-xu-ly-su-viec`: nhắc người xử lý, báo trưởng bộ phận | Có, khi người xử lý chọn kết quả |
| Trạm thu phí (danh mục) | Đang dùng | Ngừng dùng | Đội sản phẩm ngừng trạm | Có |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Xe mất tín hiệu giữa đường | Dữ liệu tới lúc mất | Dữ liệu về muộn xử lý theo giờ thật (G1); trên Lệnh xử lý như `transport-dispatch` 6.4 | — |
| Cả Lệnh không có dữ liệu (thiết bị hỏng) | Lệnh không có sự việc GPS | Lệnh ghi "Không có dữ liệu GPS"; báo quản lý phương tiện kiểm tra thiết bị | — |
| Đơn vị thu phí lỗi, chậm | Lượt qua trạm chưa khớp | Tra lại theo `transport-dispatch` I6 | — |
| Dịch vụ bản đồ lỗi | ETA gốc | ETA = quãng còn lại ÷ vận tốc trung bình tuyến, ghi "ETA ước tính" | — |
| Cảm biến dầu nhiễu | Số đo tụt rồi trở lại | Không báo hút dầu; lặp lại thì G2 | — |
| Hai người cùng xử lý một sự việc | Kết quả của người lưu trước | Người sau thấy ai đã xử lý (X2) | — |

### 6.5 Other Edge Cases

- Xe chưa gắn GPS: Lệnh chạy như hiện có, lái xe bấm đến nơi kèm ảnh định vị, không có kẹt xe và bù dầu tự động, vé theo giao dịch thu phí. Xe có GPS mà không có cảm biến dầu: không có cảnh báo hút dầu, đổ dầu; phiếu đầy bình chọn tay. Chờ khách (OQ-6).
- Xe thuê ngoài, xe nhà thầu: không quản lý (DEC-102).
- Lệnh không hết chạy: xác định bằng GPS (xe vào vùng điểm cuối); chỉ khi GPS hỏng mới nhắc lái xe và điều vận sau `P-qua-gio-ket-thuc-lenh` (chưa chốt) quá giờ kết thúc dự kiến.
- Đổi thiết bị, đổi thẻ ETC giữa kỳ: dữ liệu cũ vẫn gắn đúng xe theo lịch sử gắn thiết bị, thẻ (`vehicle-management` H3).

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Vùng trạm thu phí | Đa giác khép kín, ít nhất 3 đỉnh, các cạnh không cắt nhau; mỗi trạm ít nhất 1 vùng, mỗi chiều đường 1 vùng |
| Giá vé theo loại xe | Số không âm, đơn vị đồng, có ngày hiệu lực |
| Lý do (Hợp lệ, mở lại sự việc) | Bắt buộc, tối đa 1000 ký tự |
| Làm tròn hiển thị | Lít và km 1 chữ số thập phân; phút làm tròn xuống |

### 7.2 Limits & Quotas (exact values)

Mọi con số dưới đây chờ khách xác nhận hoặc cho số (OQ-4).

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| `P-van-toc-ket-xe` | Delta: 5 km/h | — | Dưới mức này, máy nổ: xét kẹt xe |
| `P-thoi-gian-ket-xe` | Delta: 10 phút | liên tục | Ghi kẹt xe |
| `P-thoi-gian-no-may-ngu` | Delta: 10 phút | liên tục | Ghi nổ máy ngủ |
| `P-khoang-dung-giua-ket-xe` | chưa chốt | giữa 2 đoạn kẹt | Đứng yên vẫn tính kẹt xe |
| `P-chu-ky-doc-dau-tat-may` | Delta: 30 phút | khi tắt máy | Đọc mức dầu |
| `P-nguong-hut-dau` | Delta: 5 lít trong dưới 3 phút | — | Nghi hút dầu |
| `P-nguong-do-dau` | Delta: 20 lít trong 10 phút | xe đứng yên | Ghi sự kiện đổ dầu |
| `P-nguong-chay-ngoai-lenh` | chưa chốt | quãng hoặc thời gian | Cảnh báo xe chạy ngoài Lệnh |
| `P-han-xu-ly-su-viec` | chưa chốt | từ lúc tạo | Nhắc, báo trưởng bộ phận |
| `P-so-lan-loi-cam-bien` | chưa chốt | mỗi kỳ | Báo kiểm tra thiết bị |
| `P-thoi-gian-giu-gps` | chưa chốt | — | Xoá dữ liệu GPS thô |
| `P-qua-gio-ket-thuc-lenh` | chưa chốt | sau giờ kết thúc dự kiến, khi GPS hỏng | Nhắc lái xe, điều vận |
| `P-nhac-tat-may` | chờ khách | — | Bật thì nhắc lái xe tắt máy |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Vùng trạm sai | "Vùng trạm cần ít nhất 3 điểm, các cạnh không cắt nhau." | E-? |
| Bỏ trống lý do | "Nhập lý do." | E-common-001 |
| Xử lý sự việc đã có người xử lý | Popup: "Sự việc đã được [tên] xử lý lúc [hh:mm]." | E-? |
| Lỗi kết nối nhà cung cấp | Dùng câu chung | E-common-008 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Ghi kết quả sự việc | "Đã ghi kết quả: [Vi phạm · Hợp lệ · Lỗi thiết bị]" |
| Lưu trạm | "Đã lưu trạm [tên trạm]" |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Hút dầu (quản lý phương tiện) | **Nghi hút dầu: xe [biển số]** · "Dầu giảm [x] lít trong [y] phút lúc [hh:mm] tại [địa điểm]. Lái xe đang giữ xe: [tên]." |
| Xe chạy ngoài Lệnh | **Xe [biển số] chạy ngoài Lệnh** · "Đã đi [x] km từ [hh:mm], chưa có Lệnh nào đang chạy." |
| Sự việc quá hạn | **Sự việc quá hạn xử lý** · "[Loại sự việc] của xe [biển số] quá hạn [n] ngày." |
| Nhắc tắt máy (nếu bật) | **Xe đang nổ máy đứng yên** · "Đã [x] phút. Tắt máy nếu chưa chạy." |
| Nhãn | "ETA ước tính" · "Không có dữ liệu GPS" · "Không đủ dữ liệu" · "Trạm chưa có trong danh mục" · "Nghi gắn nhầm thẻ ETC" · "Nghi trừ trùng" |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

| Dịch vụ | Dùng để | Thay được bằng |
|---|---|---|
| EUP (GPS, cảm biến dầu) | Vị trí, tốc độ, máy, mức dầu, km; sự kiện đổ, hút dầu | Vietmap, Bình Anh, Adsun… |
| VETC | Giao dịch trừ tiền theo xe; hoá đơn tổng cuối kỳ; có thể cả danh mục trạm | Đơn vị thu phí khác |
| Dịch vụ bản đồ | Cung đường, quãng đường, ETA, tình trạng giao thông | Google, Vietmap… (OQ-1) |
| iGAS | Số lít thực bơm ở cây dầu nội bộ | Đã có ở module dầu |

- **Cần tức thời:** ETA và giờ đến, cảnh báo quá mốc, hút dầu, xe chạy ngoài Lệnh, "Bình chưa đầy" trong phiên bơm, vé khớp khi đơn vị thu phí gửi về.
- **Chậm vài phút được:** đề xuất bù dầu, ghép phiếu với sự kiện đổ dầu, cảnh báo lệch dầu thực đổ.
- **Chạy nền:** đọc mức dầu khi tắt máy; tra lại giao dịch thu phí sau `P-quet-lai-vetc`; mỗi ngày nhắc sự việc quá hạn; xoá dữ liệu GPS thô quá hạn; lập báo cáo cuối kỳ.
- **Thông báo:** trong web và app; không SMS, không email.

## 8. Assumptions

- Mọi đầu kéo Delta đã gắn GPS EUP; xe có cảm biến dầu là một phần đội xe (số lượng chờ khách, OQ-8).
- Mọi xe đã dán thẻ VETC thuộc tài khoản mẹ Delta VT hoặc Delta HCM.
- EUP và VETC cung cấp dữ liệu theo xe, theo thời gian qua kết nối máy.
- Lịch sử bàn giao, thu hồi phản ánh đúng ai đang giữ xe.
- Định mức theo tải (l/km) đã có cho từng xe; định mức l/giờ sẽ được bổ sung.
- Danh mục trạm thu phí dựng được từ nguồn công khai hoặc từ VETC.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| EUP không gửi sự kiện tức thời hoặc không dùng chung ngưỡng cảm biến | thỉnh thoảng | Cảnh báo trễ, kẹt xe tính sai, bù dầu sai | Chốt sớm với EUP (Công tác chuẩn bị mục 3.3); có phương án đọc định kỳ |
| VETC không cho tra giao dịch theo xe, hoặc không gửi tức thời | thỉnh thoảng | Tránh trạm phát hiện muộn, đối soát dồn cuối kỳ | Theo công văn VETC 02/09/2026; thiết kế chạy được cả hai cách |
| Lái xe phản đối khi bị ghi nổ máy ngủ, tránh trạm, hút dầu | thường | Tranh chấp, mất lái xe | Công bố quy chế trước khi bật; lái xe xem được số liệu của mình; người duyệt chấp nhận được kèm lý do; tháng đầu chỉ ghi nhận, chưa tính tiền |
| Cảm biến dầu lệch, nhiễu | thỉnh thoảng | Kết luận sai vi phạm, tranh chấp với cây dầu, lái xe | Dung sai theo khách; kết quả "Lỗi thiết bị"; báo hiệu chỉnh khi lệch lặp lại |
| Vùng trạm vẽ sai, thiếu | thỉnh thoảng | Báo tránh trạm sai, lái xe bị tính oan | Giao dịch thu phí là nguồn chuẩn khi có; danh mục do đội sản phẩm duy trì; theo dõi tỉ lệ "GPS không bắt được trạm" |
| Tính tiền vào lương từ dữ liệu GPS khi quy chế lao động chưa cho phép | hiếm | Tranh chấp lao động | Khách xác nhận quy chế trước khi bật tính tiền |

## 10. Success Criteria (preliminary)

Mục tiêu con số chốt ở BRD.

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| a | % giao dịch VETC tự khớp vào Lệnh không cần người; số giờ kế toán đối soát hoá đơn VETC mỗi tháng | ? |
| b | % lít bù dầu có bằng chứng GPS; độ lệch giữa số đề xuất và số được duyệt | ? |
| c | Thời gian từ lúc hút dầu tới lúc quản lý nhận cảnh báo; % phiếu cấp dầu khớp cảm biến | ? |
| d | Số trạm tránh trên 100 Lệnh, theo tháng | ? |
| Hao phí | Lít nổ máy ngủ trên mỗi xe mỗi tháng | ? |

## 11. Open Questions

| OQ | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-1 | Delta đang dùng dịch vụ bản đồ nào (Google, Delta Map API, Vietmap)? Có dữ liệu tắc đường, biển báo không? Đề xuất chọn bên có nhiều dữ liệu hơn vì đây là đầu vào điều chỉnh cung đường thực tế. | Vehicle Intelligent Service — VIS (08/10/2026), mục 2.1 Kiến trúc hệ thống, mục 2.2.1 Thời gian xe sẽ đến (ETA) | Chưa hỏi Delta |
| OQ-2 | EUP có gửi sự kiện ngay khi trạng thái xe đổi không, bao nhiêu giây một lần khi xe chạy? EUP có đủ dữ liệu cảnh báo hút dầu để dùng thẳng không? Ngưỡng cảm biến (5 lít trong 3 phút, 20 lít trong 10 phút) đã thống nhất với EUP chưa? | VIS (08/10/2026), mục 2.2 Quy trình xử lý chi tiết, mục 3.5; SIM & VIS — Công tác chuẩn bị (11/10/2026), mục 3.3 Giám sát hành trình EUP | Chưa hỏi Delta |
| OQ-3 | VETC có cung cấp danh mục trạm thu phí (toạ độ, giá theo loại xe) không? Đề xuất làm danh mục dùng chung, đội sản phẩm duy trì. | VIS (08/10/2026), mục 2.2.6 Giám sát lộ trình và ghi nhận tránh trạm vé | Chưa hỏi Delta |
| OQ-4 | Xác nhận các ngưỡng đã ghi (đọc dầu 30 phút khi tắt máy — mục 2.2 ghi 30–60 phút; nổ máy ngủ 10 phút; hút dầu 5 lít trong 3 phút; đổ dầu 20 lít trong 10 phút) và cho số các ngưỡng còn trống: ngưỡng chạy ngoài Lệnh, hạn xử lý sự việc, số lần lỗi thiết bị, thời gian giữ dữ liệu GPS, quá giờ kết thúc Lệnh khi GPS hỏng. | VIS (08/10/2026), mục 2.2, 2.2.4, 3.5, 3.6 | Chưa hỏi Delta |
| OQ-5 | Có muốn nhắc lái xe tắt máy trên app khi nổ máy đứng yên quá 10 phút không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-6 | Xe chưa gắn GPS, xe có GPS mà không có cảm biến dầu: xử lý như Mục 6.5 được không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-7 | Giao dịch ở trạm chưa có trong danh mục, thẻ ETC gắn nhầm xe, VETC trừ trùng: xử lý như T2, G3, G4 được không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-8 | Quy mô: số xe gắn GPS, số xe có cảm biến dầu, số trạm hay đi qua, số giao dịch VETC mỗi tháng, số người mỗi vai (quản lý phương tiện, kế toán, quản lý cây dầu). | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-9 | Sự việc kéo qua nửa đêm, qua tháng tính vào kỳ theo giờ bắt đầu; số liệu của Lệnh vào kỳ theo ngày duyệt: đúng ý khách không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-10 | Khách xem các rủi ro ở Mục 9 và cho ý kiến, nhất là: quy chế nội bộ đã cho phép tính tiền vào lương từ dữ liệu GPS (tránh trạm, nổ máy ngủ, hút dầu) chưa; lái xe sẽ được xem số liệu của mình thế nào. | VIS (08/10/2026), mục 3.1.1 Sơ đồ kiến trúc và luồng dữ liệu (vé tránh trạm trả vào lương lái xe) | Chưa hỏi Delta |
| OQ-11 | Mục lục VIS không có mục 3.6 Quy trình đối soát lượng dầu thực đổ, thân tài liệu có. Mục này có thuộc phạm vi không? | VIS (08/10/2026), mục lục và mục 3.6 | Chưa hỏi Delta |
| OQ-12 | Định mức dầu khi nổ máy không chạy (l/giờ) đã có chưa, ai đặt? Dùng chung một con số cho kẹt xe và nổ máy ngủ được không? (Chuyển `fuel-allowance` khi lập feature.) | VIS (08/10/2026), mục 3.2 bước 3, mục 3.4 bước 3 | Chưa hỏi Delta |
| OQ-13 | Ghép sự kiện đổ dầu với phiếu cấp dầu trong khung giờ bao lâu? Dung sai lít thực đổ, dung sai coi là đầy bình, thời gian chờ cảm biến ổn định là bao nhiêu? (Chuyển `fuel-issuing`.) | VIS (08/10/2026), mục 3.6 bước 3 | Chưa hỏi Delta |
| OQ-14 | dGas4, dGas5 ở cây dầu nội bộ dừng bơm do vòi tự ngắt, có thể lệch với cảm biến. Đề xuất: lấy số iGAS làm căn cứ, chờ cảm biến ổn định, chưa đầy thì nhắc bơm bồi một lần, vẫn chưa đầy thì chốt theo số iGAS và ghi số lít thiếu. Khách đồng ý không? (Chuyển `fuel-issuing`.) | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-15 | Xe tắt máy, phần mềm chỉ đọc mức dầu mỗi 30 phút nên ngưỡng "giảm 5 lít trong dưới 3 phút" không kiểm được: hút dầu lúc xe đậu bãi tắt máy sẽ lọt, đổ dầu lúc tắt máy không ra sự kiện. EUP có gửi sự kiện dầu khi xe tắt máy không? Nếu không: đề xuất so hai lần đọc liền nhau, giảm quá ngưỡng là nghi hút dầu, tăng quá ngưỡng là đổ dầu (ngưỡng chờ khách cho số). | VIS (08/10/2026), mục 2.2, mục 3.5 Bước 1, mục 3.6 Bước 1 | Chưa hỏi Delta (review r1: hỏi khách) |

### Review vòng 1 — chưa trả lời

Câu review của PO và senior BA trên trang phỏng vấn VIS (https://claude.ai/artifact/GRtqWJ6Zwc7a3P4MuBoNhr, nhóm Phần 8). Ghi vào repo trước khi trả lời (anh chốt 15/10); trả lời xong thì áp vào mục được nêu.

| # | Vấn đề | Đề xuất của reviewer | Áp vào |
|---|---|---|---|
| r6 | Lệch dầu thực đổ: lỗi của ai | Xem đề xuất trên trang | S6 · `fuel-issuing` |
| r10 | Thiết bị chưa khai; cả đội mất dữ liệu | Xem đề xuất trên trang | K1, G1–G2, Mục 6.5 |
| r11 | Trạm đổi giữa chừng; giá vé theo tổ hợp xe; trả tiền mặt tại trạm | Xem đề xuất trên trang | T1 · I7, I10 |
| r12 | Một gói hay hai gói nhiên liệu | Tách "Giám sát nhiên liệu" (cảm biến) và "Nhiên liệu" (cây dầu, định mức, phiếu) | Nhãn gói toàn bộ · `saas-core-vs-tenant.md` |
| r13 | Có thêm vấn đề (e) "không kiểm soát được hao phí" không | Thêm (e): nổ máy ngủ, nhắc tắt máy, dự toán vé, chỉ số lít nổ máy ngủ/xe/tháng | Mục 1, Mục 10 |

## 12. Next Steps

- Hỏi Delta các câu ở Mục 11 cùng câu mở VIS ở `transport-dispatch` (OQ-49–57) và `vehicle-management`.
- Thêm "Gói Giám sát nhiên liệu" vào danh sách gói ở `saas-core-vs-tenant.md` và PRD sản phẩm; thêm `vehicle-telematics` vào Feature Map (`/prd`).
- `/srs vehicle-telematics` sau khi khách trả lời OQ-1, OQ-2, OQ-4.
