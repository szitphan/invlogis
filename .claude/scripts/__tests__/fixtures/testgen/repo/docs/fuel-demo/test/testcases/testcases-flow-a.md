# Test cases — flow-a

---
**STT:** 01
**Category:** Luồng C
**Sub-Category:** Duyệt
**Checklist:** CHK-fuel-demo-001 — Duyệt phiếu hiện toast thành công
**Ref:** FR-fuel-demo-R001
**Priority:** 1
**Title:** Duyệt phiếu cấp dầu cây ngoài
**Description:** Duyệt trên web.
**Auto:** Yes
**Target:** web
**Role:** approver
**Data:** phieu-cho-duyet
**Preconditions:** ROLE: approver
DATA: phieu-cho-duyet

**Step:** 1
**Action:** Truy cập /fuel/dispensings
**Expected:** Hiển thị "Phiếu cấp dầu" và "Chờ duyệt"
**Test Data:** —

**Step:** 2
**Action:** Chọn "Cây ngoài A" trong "Cây cấp dầu"
**Expected:** —
**Test Data:** —

**Step:** 3
**Action:** Chọn ngày "Từ ngày"
**Expected:** —
**Test Data:** 01/10/2026

**Step:** 4
**Action:** Nhập field "Ghi chú"
**Expected:** —
**Test Data:** Duyệt QA

**Step:** 5
**Action:** Bấm nút "Duyệt" trong dòng chứa "PCD-0001"
**Expected:** —
**Test Data:** —

**Step:** 6
**Action:** Xác nhận hộp thoại "Đồng ý"
**Expected:** Toast hiện "Duyệt thành công"
**Test Data:** —
---
**STT:** 02
**Category:** Luồng A
**Sub-Category:** Tạo phiếu
**Checklist:** CHK-fuel-demo-002 — Tạo phiếu dGas1 trả 201
**Ref:** FR-fuel-demo-R002, AC:FU-FD-AC-002
**Priority:** 1
**Title:** Tạo phiếu dGas1 qua API rồi giả lập bơm
**Description:** API xương sống.
**Auto:** Yes
**Target:** api
**Role:** requester-mobile
**Data:** xe-noi-bo
**Preconditions:** ROLE: requester-mobile

**Step:** 1
**Action:** POST /api/fuel-management/v1/fuel-dispensings
**Expected:** HTTP 201
body.data.status = "draft"
lưu data.id → fuelDispensingId
**Test Data:** {"type": "dGas1", "vehicleId": {{data_xe_noi_bo}}}

**Step:** 2
**Action:** POST /api/fuel-management/v1/fuel-dispensings/{{fuelDispensingId}}/dispensing-authorizations
**Expected:** HTTP 2xx; lưu data.authorizationCode → authorizationCode
**Test Data:** {}

**Step:** 3
**Action:** Giả lập bơm pumped {{authorizationCode}} 48.5 lít
**Expected:** HTTP 200
**Test Data:** —

**Step:** 4
**Action:** [vai: approver] GET /api/fuel-management/v1/fuel-dispensings/{{fuelDispensingId}}
**Expected:** HTTP 200; data.status = "completed"
**Test Data:** —
---
**STT:** 03
**Category:** Luồng A
**Sub-Category:** Danh sách
**Checklist:** CHK-fuel-demo-003 — Danh sách hiện tiêu đề cũ
**Ref:** —
**Priority:** 2
**Title:** Danh sách phiếu
**Description:** x
**Auto:** Yes
**Preconditions:** —

**Step:** 1
**Action:** Truy cập /fuel/list
**Expected:** Hiển thị "Danh sách phiếu cấp dầu"
**Test Data:** —
---
**STT:** 04
**Category:** Luồng A
**Sub-Category:** Tra cứu
**Checklist:** CHK-fuel-demo-004 — Tra cứu thủ công
**Ref:** FR-fuel-demo-R004
**Priority:** 2
**Title:** Tra cứu
**Description:** x
**Auto:** No
**Preconditions:** Có phiếu đã duyệt (dựng: tạo + duyệt; nguồn: FR-fuel-demo-R004)

**Step:** 1
**Action:** Truy cập /fuel/search
**Expected:** Hiển thị "Kết quả"
**Test Data:** —
---
**STT:** 05
**Category:** Luồng A
**Sub-Category:** App
**Checklist:** CHK-fuel-demo-005 — Lấy mã iGAS trên app
**Ref:** FR-fuel-demo-R005
**Priority:** 2
**Title:** Lấy mã iGAS
**Description:** x
**Auto:** Yes
**Target:** mob
**Role:** requester-mobile
**Preconditions:** ROLE: requester-mobile

**Step:** 1
**Action:** Bấm "Lấy mã Igas"
**Expected:** Hiện "Mã iGAS"
**Test Data:** —
---
**STT:** 06
**Category:** Luồng A
**Sub-Category:** Phân quyền
**Checklist:** CHK-fuel-demo-006 — Tạo phiếu sai kênh bị chặn
**Ref:** FR-fuel-demo-R006
**Priority:** 2
**Title:** Web token không tạo được phiếu
**Description:** x
**Auto:** Yes
**Target:** api
**Role:** approver
**Preconditions:** —

**Step:** 1
**Action:** POST /api/fuel-management/v1/fuel-dispensings
**Expected:** HTTP 403
errorCode = "AuthZ.PermissionMissing"
**Test Data:** {"type": "dGas1"}
---
**STT:** 07
**Category:** Luồng A
**Sub-Category:** API chưa map
**Checklist:** CHK-fuel-demo-007 — API chưa map
**Ref:** —
**Priority:** 3
**Title:** API grammar sai
**Description:** x
**Auto:** Yes
**Target:** api
**Role:** approver
**Preconditions:** —

**Step:** 1
**Action:** Gọi API tạo phiếu
**Expected:** Thành công
**Test Data:** —
---
**STT:** 08
**Category:** Luồng C
**Sub-Category:** Đăng nhập
**Checklist:** CHK-fuel-demo-008 — Nhập mật khẩu qua ENV
**Ref:** —
**Priority:** 3
**Title:** Mật khẩu lấy từ ENV
**Description:** x
**Auto:** Yes
**Target:** web
**Preconditions:** —

**Step:** 1
**Action:** Nhập field "Mật khẩu"
**Expected:** —
**Test Data:** ENV: QA_DEMO_SECRET

**Step:** 2
**Action:** Bấm nút "Đăng nhập"
**Expected:** Không hiển thị "Sai mật khẩu"
**Test Data:** —
