---
**STT:** 01
**Category:** Luồng A
**Sub-Category:** Lấy mã iGAS
**Checklist:** CHK-fuel-demo-001 — Verify lấy mã iGAS rồi giả lập bơm [đáp án: code FU-FD-AC-002]
**Ref:** FR-fuel-demo-R001, AC:FU-FD-AC-002
**Priority:** 1
**Title:** Verify lấy mã iGAS và giả lập bơm tại cây nội bộ
**Description:** Luồng A.
**Auto:** Yes
**Target:** mob
**Role:** requester-mobile
**Data:** phieu-dgas1
**Preconditions:** ROLE: requester-mobile

**Step:** 1
**Action:** Mở app
**Expected:** Hiện "Trang chủ"
**Test Data:** —

**Step:** 2
**Action:** Bấm "Cấp dầu"
**Expected:** Hiện "Lấy mã Igas"
**Test Data:** —

**Step:** 3
**Action:** Bấm "Lấy mã Igas"
**Expected:** Không hiện "Lỗi"
**Test Data:** —

**Step:** 4
**Action:** Giả lập bơm
Chờ "Đã bơm xong" hiện
**Expected:** Hiện "Đã bơm xong"
**Test Data:** —
---
**STT:** 02
**Category:** Luồng A
**Sub-Category:** Nhập liệu
**Checklist:** CHK-fuel-demo-002 — Verify nhập số lít
**Ref:** FR-fuel-demo-R002
**Priority:** 2
**Title:** Verify nhập số lít
**Description:** x
**Auto:** Yes
**Target:** mob
**Preconditions:** —

**Step:** 1
**Action:** Đăng nhập vai approver
**Expected:** Hiện "Trang chủ"
**Test Data:** —

**Step:** 2
**Action:** Nhập "ENV: QA_LITERS" vào "Số lít"
**Expected:** Hiện "Số lít hợp lệ"
**Test Data:** —
---
**STT:** 03
**Category:** Luồng A
**Sub-Category:** Lạ
**Checklist:** CHK-fuel-demo-003 — Bước lạ
**Ref:** FR-fuel-demo-R003
**Priority:** 2
**Title:** Bước lạ
**Description:** x
**Auto:** Yes
**Target:** mob
**Preconditions:** —

**Step:** 1
**Action:** Lắc điện thoại ba lần
**Expected:** Hiện "X"
**Test Data:** —
---
**STT:** 04
**Category:** Web
**Sub-Category:** web
**Checklist:** CHK-fuel-demo-004 — Web
**Ref:** FR-fuel-demo-R004
**Priority:** 2
**Title:** Web
**Description:** x
**Auto:** Yes
**Target:** web
**Preconditions:** —

**Step:** 1
**Action:** Bấm "Duyệt"
**Expected:** Hiện "OK"
**Test Data:** —
---
**STT:** 05
**Category:** Luồng A
**Sub-Category:** manual
**Checklist:** CHK-fuel-demo-005 — Thủ công
**Ref:** FR-fuel-demo-R005
**Priority:** 3
**Title:** Thủ công
**Description:** x
**Auto:** No
**Target:** mob
**Preconditions:** —

**Step:** 1
**Action:** Bấm "A"
**Expected:** Hiện "B"
**Test Data:** —
---
