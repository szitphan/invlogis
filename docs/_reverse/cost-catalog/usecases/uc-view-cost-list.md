# UC-view-cost-list — Xem danh mục chi phí cấp 1, 2, 3

## a. Introduction

Xem danh sách khoản mục chi phí của từng cấp từ sub-tab Chi phí cấp N trong tab Danh mục. Mã UC gốc: UC03.10.01 (cấp 1), UC03.11.01 (cấp 2), UC03.12.01 (cấp 3). Nhóm cùng khuôn, viết một lần; khác biệt theo cấp ở `spec.md` Mục 3. ✅ [SRS Web tr.581, 614, 648 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.581 — UC03.10.01]
- Đối tượng: Chi phí cấp N (danh sách), Trạng thái ✅ [SRS Web tr.583 — UC03.10.01]

## c. Pre-conditions

- Người dùng đã đăng nhập ✅
- Người dùng được phân quyền Xem của Danh mục - Chi phí cấp N ✅ [SRS Web tr.581, 614, 648 — UC03.10.01, UC03.11.01, UC03.12.01]

## d. Expected result

Hệ thống hiển thị danh sách chi phí cấp N thành công ✅ [SRS Web tr.581, 614, 648 — UC03.10.01, UC03.11.01, UC03.12.01]

## e. Activity diagram

Xem flows.md — Flow: Xem danh sách khoản mục chi phí (cấp 1, 2, 3)

Main Success Scenario:
1. Người dùng vào Dashboards; hệ thống hiển thị màn Dashboards ✅ [SRS Web tr.581 — hình lưu đồ UC03.10.01]
2. Người dùng chọn tab Danh mục ở thanh điều hướng ✅ [SRS Web tr.581 — hình lưu đồ UC03.10.01]
3. Người dùng chọn sub-tab Chi phí cấp N ✅
4. Hệ thống hiển thị Danh sách chi phí cấp N ✅
5. Người dùng dùng thanh tìm kiếm (tìm gần đúng, trừ cột Trạng thái), nhóm, lọc, Export, Import, Tuỳ chỉnh, đổi số bản ghi/trang, chọn trang ✅ [SRS Web tr.582–584 — UC03.10.01]

Extensions:
- 5a. Nhấn Tạo mới: dẫn tới form Tạo mới chi phí cấp N (UC tạo đề xuất) ✅ [SRS Web tr.583 — UC03.10.01]
- 5b. Nhấn một dòng: mở Thông tin chi phí cấp N (UC xem thông tin) ✅ [SRS Web tr.585 — UC03.10.02]
- 5c. Cột Hành động: hiện hành động theo trạng thái và phân quyền (Phê duyệt, Từ chối, Huỷ đề xuất, Xoá yêu cầu, Tạo mới yêu cầu) ✅ [SRS Web tr.583 — UC03.10.01; tr.589 — UC03.10.02]
- 5d. Chức năng Export, Import, Bộ lọc, Tuỳ chỉnh: nguồn chỉ trỏ Common Rules 🟡 [SRS Web tr.582–583 — UC03.10.01]

## f. Screens

Danh sách chi phí cấp 1; Danh sách chi phí cấp 2; Danh sách chi phí cấp 3 (xem spec Mục 10).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–4 | FR-cost-catalog-001 | BR-cost-catalog-010 | — | SRS Web tr.581 — UC03.10.01 |
| 5 | FR-cost-catalog-002, FR-cost-catalog-003, FR-cost-catalog-004 | BR-cost-catalog-015, BR-cost-catalog-021 | — | SRS Web tr.582–584 — UC03.10.01 |

## h. Open Questions

OQ-6 (Import), OQ-7 (phân quyền)
