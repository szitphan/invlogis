---
type: brainstorm
feature: vehicle-management
status: draft
status_changed: 2026-10-18
status_reason: "đã review upstream, không cần sửa"
updated: 2026-10-15
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs-input/srs-cu/srs-mobile/srs-mobile.md
  - docs-input/sop/vis-giam-sat-doi-xe/vis-giam-sat-doi-xe.md
  - docs/_shared/project-profile.md
  - docs/_product/prd.md
  - docs/_product/saas-core-vs-tenant.md
  - docs/_product/tenant-parameters.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
  - docs/transport-dispatch/brainstorms/transport-dispatch.md
---

# Quản lý phương tiện — hồ sơ xe, bàn giao, thu hồi và dữ liệu vận hành theo xe

## 1. Idea Seed

"feed SRC-06 và brainstorm (vẫn đi từ đầu full round) và đưa đề xuất, ngoài ra bạn phải check phần phương tiện hiện tại đang có gì (module xưởng có bàn giao thu hồi định mức phương tiện) bên danh mục có quản lý thông tin phương tiện"

Phần VIS gắn theo từng xe (km, dầu tồn, hút dầu, xe chạy ngoài Lệnh, nổ máy ngủ ngoài Lệnh, báo cáo theo xe và lái xe) được lồng vào Quản lý phương tiện, trên nền hồ sơ xe, bàn giao, thu hồi đã có ở SRS v2.0.

## 2. Context

**Phần phương tiện đang có (SRS LG v2.0, Module 5 Danh mục › Feature 04.01 Phương tiện, trang 2014–2430).** Đường vào "Dashboards › Quản lý tài sản › Phương tiện", người dùng là "người dùng phần mềm xưởng".

| Mảng | Đang có | Nguồn |
|---|---|---|
| Hồ sơ xe | Danh sách, chi tiết 6 tab; sửa hồ sơ qua duyệt; lịch sử thay đổi | UC04.00.01–07 |
| Trạng thái xe | Lái xe giữ: Đang hoạt động · Đang sửa chữa · Đang tạm giữ. Công ty giữ: Sẵn sàng hoạt động · Đang sửa chữa | trang 2015 |
| Ô chờ dữ liệu ngoài | "Số vận hành hiện tại (km/giờ) lấy theo API bên thứ 3"; thẻ "Dầu diesel tồn" chưa chốt nguồn | UC04.00.02 |
| Bàn giao, thu hồi | Yêu cầu → duyệt → ký biên bản; nhập tay "KMs bàn giao", "Mô tả nhiên liệu" bằng chữ; ảnh xe, tình trạng | UC04.01.01–10 |
| Liên quy trình dầu | Phiếu đổ đầy bình (dGas4) xong → bàn giao; phiếu chốt dầu (dGas5) xong → thu hồi, chạy định mức | Bảng liên quy trình |
| Định mức nhiên liệu | Kế hoạch chạy định mức → tiêu hao thực tế → định mức khoán 8 mức tải (l/km) | UC04.01.11–21 → `fuel-allowance` |
| Lịch nhắc | Theo thời gian và theo km, giờ máy | Tab Lịch nhắc → `reminders` |

**Vấn đề feature này xử lý thêm (đã xác nhận):** (c) hút dầu, đổ thiếu phát hiện muộn hoặc không phát hiện. Đề xuất thêm: km và dầu trên biên bản bàn giao hiện nhập tay, dễ tranh cãi.

**Phạm vi:**
- Gồm: hồ sơ xe, trạng thái xe, bàn giao, thu hồi; dữ liệu vận hành theo xe từ `vehicle-telematics` (km, dầu tồn, hút dầu, xe chạy ngoài Lệnh, nổ máy ngủ ngoài Lệnh); báo cáo theo xe, lái xe.
- Không gồm: định mức nhiên liệu (`fuel-allowance`); lịch nhắc (`reminders`); sửa chữa (`repair-order`); phiếu cấp dầu (`fuel-issuing`); xe thuê ngoài, xe nhà thầu (DEC-102).
- Phần ghi theo SRS v2.0 chưa phỏng vấn lại; rà khi đối chiếu SRS cũ (BL-146).

**Nguồn:** SRS LG v2.0 Feature 04.01 Phương tiện; SRS mobile Epic 06 Phiếu cấp dầu; Vehicle Intelligent Service — VIS (08/10/2026); phỏng vấn 14–15/10/2026.

**Nhãn:** [SRS v2.0] = đã có trong SRS cũ · [SOP to-be] = VIS đã yêu cầu · [SOP+] = có nêu, đề xuất làm thêm · [Mới] = chưa có trong tài liệu khách.

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Quản lý phương tiện | Biết hút dầu, xe chạy sai mục đích khi đã muộn; km, dầu trên biên bản nhập tay | Cảnh báo tức thời; số liệu GPS tự điền |
| Lái xe | Tranh cãi lượng dầu lúc nhận, trả xe | Biên bản có số liệu khách quan; xem được số liệu của mình |
| Người duyệt bàn giao, thu hồi | Duyệt dựa trên số nhập tay | Số liệu từ GPS, phiếu dầu đã xong |
| Kế toán, bộ phận lương | Không có căn cứ trừ, thưởng | Báo cáo theo lái xe theo kỳ |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Quản lý phương tiện | Xử lý cảnh báo hút dầu, xe chạy ngoài Lệnh | Khi có | cao | Mất dầu, dùng xe sai mục đích |
| Quản lý phương tiện | Xem nổ máy ngủ, tiêu hao theo lái xe | Mỗi tháng | trung | Hao phí dầu kéo dài |
| Quản lý phương tiện | Bàn giao, thu hồi xe | Vài lần mỗi tuần | trung | Gán sai người giữ xe thì gán sai trách nhiệm |

## 4. Capabilities Breakdown

### P0 — must have

**Nhóm H — hồ sơ xe**
- H1 [SRS v2.0] [Lõi] Hồ sơ xe 6 tab: Thông tin chung · Hàng hoá và thiết bị · Bàn giao, thu hồi · Sửa chữa · Định mức · Lịch nhắc. Sửa hồ sơ qua duyệt, có lịch sử thay đổi. Tab Sửa chữa, Định mức, Lịch nhắc chỉ hiện khi khách bật gói tương ứng.
- H2 [SRS v2.0] [Lõi] Trạng thái xe theo người giữ: lái xe giữ (Đang hoạt động · Đang sửa chữa · Đang tạm giữ), công ty giữ (Sẵn sàng hoạt động · Đang sửa chữa).
- H3 [Mới] [Lõi] Số thẻ ETC và mã thiết bị GPS trên hồ sơ xe, có lịch sử gắn và ngày hiệu lực, không trùng giữa các xe đang hoạt động. Dùng để ghép giao dịch thu phí và dữ liệu GPS với đúng xe.
- H4 [SOP to-be] [Lõi] Km hiện tại lấy từ GPS, điền vào ô "Số vận hành hiện tại" đang chờ dữ liệu ngoài. Lịch nhắc theo km ở `reminders` đọc số này.
- H5 [SOP to-be] [Gói: Giám sát nhiên liệu] Dầu tồn hiện tại lấy từ cảm biến, điền vào thẻ "Dầu diesel tồn"; chỉ xe có cảm biến.
- H6 [Mới] [Lõi] Khối "Vận hành" trên hồ sơ xe: km, dầu tồn, sự việc gần nhất (đổ dầu, hút dầu, chạy ngoài Lệnh, nổ máy ngủ), mở thẳng tới sự việc. Hoãn được nếu trễ go-live (review r17).

**Nhóm B — bàn giao, thu hồi**
- B1 [SRS v2.0] [Lõi] Yêu cầu bàn giao hoặc thu hồi → duyệt → ký biên bản. Bàn giao cho lái xe hoặc giữa chi nhánh; ảnh xe, tình trạng hoạt động.
- B2 [SRS v2.0] [Gói: Nhiên liệu] Bàn giao đi cùng phiếu đổ đầy bình (Delta: dGas4), thu hồi đi cùng phiếu chốt dầu (Delta: dGas5). Làm phiếu trước hay biên bản trước đều được; biên bản chỉ ký xong khi phiếu đi kèm đã xong. Chờ khách xác nhận loại phiếu (OQ-1).
- B3 [SOP+] [Gói: Nhiên liệu] Phần dầu trên biên bản lấy từ phiếu đã xong: số lít thực bơm, "Đã đầy (theo cảm biến)". Người ký chỉ xem lại, không nhập. Thay ô "Mô tả nhiên liệu" ghi bằng chữ.
- B4 [Mới] [Lõi] [Cấu hình] Km trên biên bản: xe có GPS thì lấy từ GPS lúc ký, không sửa tay. Lúc ký mà GPS không có dữ liệu thì lấy lần đọc gần nhất, ghi kèm giờ đọc (OQ-2). Xe không có GPS: `P-cho-nhap-km-tay` (Delta: tắt) bật thì cho nhập tay, bắt ghi lý do (review r15). Thay ô "KMs bàn giao" nhập tay.
- B5 [Mới] [Gói: Nhiên liệu] [Cấu hình] Dầu chờ nhận của lái xe còn tồn khi thu hồi xe hoặc lái xe nghỉ việc: `P-dau-cho-nhan-vao-thuong` (Delta: bật) bật thì vào thưởng lương lái xe. Việc chốt dầu thuộc phiếu chốt dầu ở `fuel-issuing`; feature này chỉ nêu điều kiện ký biên bản thu hồi (review r16).

**Nhóm V — vận hành theo xe**
- V1 [SOP to-be] [Gói: Giám sát nhiên liệu] Nhận và xử lý cảnh báo hút dầu bất thường (phát hiện ở `vehicle-telematics` S7): xác nhận vi phạm, hợp lệ hoặc lỗi thiết bị; vi phạm gắn lái xe đang giữ xe.
- V2 [Mới] [Lõi] [Cấu hình] Nhận và xử lý cảnh báo xe chạy ngoài Lệnh (`vehicle-telematics` S8). Vé thu phí phát sinh trong khoảng đó gắn vào sự việc, không thành vé mồ côi cuối kỳ. Trường hợp miễn cảnh báo chờ khách (OQ-3).
- V3 [SOP to-be] [Lõi] Nổ máy ngủ ngoài Lệnh gắn lái xe đang giữ xe theo lịch sử bàn giao.
- V4 [SOP to-be] [Lõi] Báo cáo cuối kỳ theo xe, lái xe, chi nhánh, toàn đội: km theo GPS; nổ máy ngủ (số phút; số lít hao phí khi bật Gói Nhiên liệu).
- V5 [SOP to-be] [Gói: Giám sát nhiên liệu] Báo cáo cuối kỳ: dầu tiêu hao, mức tiêu hao bình quân (l/100 km) so với định mức; dầu bị hút, có bản đồ vị trí.

### P1 — should have

Chưa phân mức: mọi phần đã chốt đều vào giai đoạn 1.

### P2 — nice to have

—

## 5. Core Flows (Happy Path)

### 5.1 Bàn giao xe cho lái xe

1. Quản lý phương tiện lập yêu cầu bàn giao (xe đang Sẵn sàng hoạt động), người có quyền duyệt.
2. Phiếu đổ đầy bình đi kèm được lập, bơm tại cây dầu nội bộ; cảm biến xác nhận đã đầy (`fuel-issuing`). Có thể làm phiếu trước biên bản.
3. Ký biên bản: km tự điền từ GPS; phần dầu lấy từ phiếu đã xong; ảnh xe, tình trạng.
4. Phiếu chưa xong thì chưa ký xong biên bản.
5. Ký xong: xe sang Đang hoạt động, lái xe thành người giữ xe; từ lúc này sự việc ngoài Lệnh gắn lái xe này.

### 5.2 Thu hồi xe

1. Lập yêu cầu thu hồi (xe Đang hoạt động hoặc Đang sửa chữa), duyệt.
2. Phiếu chốt dầu đi kèm, bơm đầy tại cây dầu nội bộ, cảm biến xác nhận đầy.
3. Dầu chờ nhận còn tồn của lái xe được chốt trên phiếu chốt dầu, đưa vào thưởng lương lái xe.
4. Ký biên bản: km từ GPS, dầu từ phiếu. Xe về Sẵn sàng hoạt động.

```
 QUẢN LÝ PHƯƠNG TIỆN       PHẦN MỀM                         CÂY DẦU NỘI BỘ
 Lập yêu cầu ────────────► Chờ duyệt ─► Đã duyệt
                           Phiếu đi kèm: bàn giao = đổ đầy bình · thu hồi = chốt dầu
                           (phiếu trước hay biên bản trước đều được)
                                                     ◄──── Bơm, iGAS ghi số lít,
                                                           cảm biến xác nhận đầy
 Ký biên bản ────────────► ◇ Phiếu đi kèm đã xong?
                           ├─ Không ─► Chưa ký xong, chỉ ra phiếu còn thiếu
                           └─ Có ─► Km từ GPS (không có thì lần đọc gần nhất + giờ)
                                    Dầu từ phiếu (chỉ xem)
                                    Thu hồi: chốt dầu chờ nhận ─► thưởng lương lái xe
                                    ─► Bàn giao: Đang hoạt động · Thu hồi: Sẵn sàng hoạt động
```

### 5.3 Hút dầu bất thường

1. `vehicle-telematics` phát hiện dầu giảm quá ngưỡng, đã loại trừ xe đang sửa chữa và số đo nhiễu.
2. Quản lý phương tiện chi nhánh khai thác xe nhận cảnh báo ngay.
3. Mở sự việc: giờ, vị trí trên bản đồ, dầu trước và sau, lái xe đang giữ xe.
4. Chọn Vi phạm, Hợp lệ (bắt lý do) hoặc Lỗi thiết bị.
5. Cuối kỳ: báo cáo dầu bị hút theo xe, lái xe, có bản đồ vị trí.

### 5.4 Xe chạy ngoài Lệnh

1. `vehicle-telematics` thấy xe không có Lệnh đang chạy mà di chuyển quá ngưỡng, không thuộc trường hợp miễn.
2. Quản lý phương tiện nhận cảnh báo kèm vị trí, quãng đã đi, lái xe đang giữ xe.
3. Xử lý: Hợp lệ kèm lý do, hoặc Vi phạm.
4. Vé thu phí trong khoảng đó gắn vào sự việc.

### 5.5 Xem vận hành của xe

1. Mở hồ sơ xe: khối Vận hành có km, dầu tồn, sự việc gần nhất.
2. Mở báo cáo cuối kỳ: chọn tháng hoặc khoảng ngày, xem theo xe, lái xe, chi nhánh.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| D1 | 5.1, 5.2 | Phiếu dầu đi kèm đã xong | Ký xong biên bản | Chưa ký xong, chỉ ra phiếu còn thiếu |
| D2 | 5.1, 5.2 | GPS có dữ liệu lúc ký | Km lúc ký | Km lần đọc gần nhất, ghi giờ đọc |
| D3 | 5.2 | Lái xe còn dầu chờ nhận | Chốt trên phiếu chốt dầu, vào thưởng lương | Bỏ qua |
| D4 | 5.3 | Xe có lệnh sửa chữa mở, hoặc số đo trở lại ngay | Bỏ qua | Cảnh báo hút dầu |
| D5 | 5.4 | Thuộc trường hợp miễn cảnh báo | Bỏ qua | Cảnh báo xe chạy ngoài Lệnh |

### 6.2 Scenario Matrix

| Việc | Thứ tự | Phiếu đi kèm | Kết quả |
|---|---|---|---|
| Bàn giao | Phiếu trước | Đã xong | Ký biên bản bình thường |
| Bàn giao | Biên bản trước | Chưa lập | Biên bản ở trạng thái đã duyệt, chờ phiếu; ký xong khi phiếu xong |
| Bàn giao | Biên bản trước | Đang bơm | Chờ phiếu xong |
| Thu hồi | Phiếu trước | Đã xong | Ký biên bản; dầu chờ nhận chốt trên phiếu |
| Thu hồi | Biên bản trước | Chưa xong | Chờ phiếu xong |
| Bàn giao, thu hồi | — | Xe không có cảm biến | Phiếu chọn đầy bình bằng tay như hiện nay |

### 6.3 State Transitions

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Xe | Sẵn sàng hoạt động | Đang hoạt động | Ký xong biên bản bàn giao cho lái xe | Có, qua thu hồi |
| Xe | Đang hoạt động | Sẵn sàng hoạt động | Ký xong biên bản thu hồi | Có, qua bàn giao |
| Xe | Đang hoạt động · Sẵn sàng hoạt động | Đang sửa chữa | Xe gắn vào lệnh sửa chữa đang triển khai | Có, khi lệnh sửa chữa xong |
| Xe | Đang hoạt động | Đang tạm giữ | Khoá xe | Có |
| Bàn giao, thu hồi | Chờ phê duyệt | Đã phê duyệt · Đã từ chối · Đã huỷ | Duyệt, từ chối, huỷ (SRS v2.0) | Từ chối, huỷ: tạo lại |
| Bàn giao, thu hồi | Đã phê duyệt | Đã hoàn thành | Ký biên bản, phiếu đi kèm đã xong | Không |

Sự việc hút dầu, chạy ngoài Lệnh dùng vòng đời "sự việc cần xử lý" ở `vehicle-telematics` Mục 6.3.

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| GPS không có dữ liệu lúc ký | Lần đọc gần nhất | Dùng km lần đọc gần nhất, ghi giờ đọc (OQ-2) | — |
| Phiếu đi kèm bị từ chối hoặc hết hạn | Biên bản đã duyệt, chưa ký | Tạo lại phiếu theo luồng phiếu cấp dầu; ký sau | — |
| Đổi thiết bị GPS, thẻ ETC giữa kỳ | Lịch sử gắn cũ | Dữ liệu cũ vẫn gắn xe cũ theo ngày hiệu lực | — |

### 6.5 Other Edge Cases

- Xe chưa gắn GPS: biên bản lấy km theo cách OQ-2 hoặc theo câu trả lời của khách (`vehicle-telematics` OQ-6).
- Thu hồi khi lái xe nghỉ việc: như thu hồi thường, dầu chờ nhận chốt vào thưởng lương (B5).
- Bàn giao giữa chi nhánh: không đổi người giữ là lái xe; sự việc ngoài Lệnh gắn chi nhánh nhận.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Số thẻ ETC | Không trùng với xe đang hoạt động khác; đổi thẻ ghi ngày hiệu lực |
| Mã thiết bị GPS | Không trùng với xe đang hoạt động khác; đổi thiết bị ghi ngày hiệu lực |
| Km trên biên bản | Chỉ lấy từ GPS, không sửa tay |
| Lý do (Hợp lệ) | Bắt buộc, tối đa 1000 ký tự |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| `P-nguong-chay-ngoai-lenh` | chưa chốt | quãng hoặc thời gian | Cảnh báo xe chạy ngoài Lệnh |
| `P-han-xu-ly-su-viec` | chưa chốt | từ lúc tạo sự việc | Nhắc, báo trưởng bộ phận |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Thẻ ETC đang gắn xe khác | Popup: "Thẻ ETC [số thẻ] đang gắn với xe [biển số]. Gỡ thẻ khỏi xe đó trước." | E-? |
| Thiết bị GPS đang gắn xe khác | Popup: "Thiết bị GPS [mã] đang gắn với xe [biển số]. Gỡ thiết bị khỏi xe đó trước." | E-? |
| Ký biên bản khi phiếu đi kèm chưa xong | Popup: **Chưa ký được biên bản** · "Phiếu [loại phiếu] [mã] chưa xong. Hoàn thành phiếu rồi ký biên bản." | E-? |
| Bỏ trống lý do | "Nhập lý do." | E-common-001 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Gắn thẻ ETC | "Đã gắn thẻ ETC cho xe [biển số]" |
| Gắn thiết bị GPS | "Đã gắn thiết bị GPS cho xe [biển số]" |
| Ghi kết quả sự việc | "Đã ghi kết quả: [Vi phạm · Hợp lệ · Lỗi thiết bị]" |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Km lấy từ lần đọc gần nhất | "Km lấy từ GPS lúc [hh:mm dd/mm/yyyy]." |
| Thông báo hút dầu, chạy ngoài Lệnh | Theo `vehicle-telematics` Mục 7.3 |

### 7.4 Bối cảnh hệ thống (mức nghiệp vụ)

- Nhận từ `vehicle-telematics`: km, dầu tồn, sự việc theo xe. Nhận từ phiếu cấp dầu (`fuel-issuing`): số lít, xác nhận đầy bình.
- Gửi cho `reminders`: km hiện tại. Gửi cho bộ phận lương: báo cáo theo lái xe, dầu chờ nhận đã chốt.
- Tức thời: cảnh báo hút dầu, xe chạy ngoài Lệnh. Theo kỳ: báo cáo.

## 8. Assumptions

- Phần SRS v2.0 (hồ sơ, trạng thái, bàn giao, thu hồi) vẫn đúng với cách Delta làm; chưa phỏng vấn lại.
- Lịch sử bàn giao, thu hồi phản ánh đúng ai đang giữ xe.
- Bàn giao, thu hồi làm ở chi nhánh có cây dầu nội bộ, nên phiếu đổ đầy bình, chốt dầu bơm qua iGAS.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Lịch sử bàn giao không cập nhật kịp | thỉnh thoảng | Sự việc ngoài Lệnh gắn sai lái xe, tranh chấp | Biên bản ký xong mới đổi người giữ; báo cáo hiện người giữ theo từng ngày |
| Lái xe phản đối khi bị ghi hút dầu, nổ máy ngủ | thường | Tranh chấp, mất lái xe | Lái xe xem được số liệu của mình; Hợp lệ kèm lý do; quy chế công bố trước |
| Bắt phiếu đi kèm mới ký được biên bản làm chậm giao xe | thỉnh thoảng | Xe nằm chờ, trễ Lệnh | Cho làm phiếu trước hoặc biên bản trước; hỏi khách (OQ-1) |

## 10. Success Criteria (preliminary)

| Vấn đề | Tiêu chí | Mục tiêu |
|---|---|---|
| c | Thời gian từ lúc hút dầu tới lúc quản lý nhận cảnh báo | ? |
| Bàn giao | % biên bản bàn giao, thu hồi có km từ GPS và dầu từ phiếu, không nhập tay | ? |
| Hao phí | Lít nổ máy ngủ trên mỗi xe mỗi tháng | ? |

## 11. Open Questions

| OQ | Câu hỏi | Nguồn khách | Trả lời |
|---|---|---|---|
| OQ-1 | Bàn giao xe đi cùng phiếu đổ đầy bình (dGas4), thu hồi đi cùng phiếu chốt dầu (dGas5): đúng không? Cho làm phiếu trước hay biên bản trước đều được, biên bản chỉ ký xong khi phiếu xong: có làm chậm giao xe không? | SRS LG v2.0, bảng liên quy trình (Bàn giao phương tiện, Thu hồi phương tiện) | Chưa hỏi Delta |
| OQ-2 | Lúc ký biên bản bàn giao, thu hồi mà GPS không có dữ liệu: lấy km lần đọc gần nhất, ghi kèm giờ đọc được không? | Chưa có trong tài liệu khách gửi | Chưa hỏi Delta |
| OQ-3 | Xe chạy ngoài Lệnh: những trường hợp nào không cảnh báo (Lệnh đã nhận, xe đang tới điểm đầu; về bãi sau Lệnh; đi đổ dầu có phiếu đang mở; đi xưởng có lệnh sửa chữa đang mở; đang bàn giao giữa chi nhánh)? Đi bao xa hoặc bao lâu thì cảnh báo? | VIS (08/10/2026), mục 3.1.3 Bước 4 (chạy xe ngoài lịch trình, việc riêng) | Chưa hỏi Delta |

### Review vòng 1 — chưa trả lời

Câu review của PO và senior BA trên trang phỏng vấn VIS (https://claude.ai/artifact/GRtqWJ6Zwc7a3P4MuBoNhr, nhóm Phần 8). Ghi vào repo trước khi trả lời (anh chốt 15/10); trả lời xong thì áp vào mục được nêu.

| # | Vấn đề | Đề xuất của reviewer | Áp vào |
|---|---|---|---|
| r5 | Lái xe được báo, được xem, được khiếu nại | Lái xe thấy sự việc gắn mình trên app, khiếu nại trong hạn | Nhóm I · `vehicle-management` V1–V3 |
| r8 | Thu hồi xe khi còn Lệnh chưa duyệt; thiết bị lỗi lúc bơm đầy | Xem đề xuất trên trang | B2–B5 |

## 12. Next Steps

- Đối chiếu phần SRS v2.0 với SRS cũ (BL-146) rồi phỏng vấn lại phần hồ sơ, bàn giao, thu hồi.
- Hỏi Delta Mục 11 cùng lượt với `vehicle-telematics` và `transport-dispatch`.
- `/srs vehicle-management` sau khi chốt OQ-1, OQ-3.
