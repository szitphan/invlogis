# UC-view-partner-list — Xem danh mục (danh sách) nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng

## a. Introduction

Hiển thị danh sách bản ghi của một trong ba danh mục, kèm tìm kiếm, nhóm, lọc, Export, Import, Tuỳ chỉnh, Tạo mới, phân trang. Mã UC gốc: UC03.07.01 (Nhà cung cấp HHDV), UC03.08.01 (Khách hàng DK05), UC03.09.01 (Xe của khách hàng). Một khuôn cho cả ba. ✅ [SRS Web tr.461 — UC03.07.01 Xem danh mục nhà cung cấp HHDV; SRS Web tr.505 — UC03.08.01 Xem danh mục khách hàng DK05; SRS Web tr.545 — UC03.09.01 Xem danh mục xe của khách hàng]

## b. Actors & Objects

- Actor chính: Người dùng phần mềm xưởng (có quyền Xem của danh mục). ✅ [SRS Web tr.461 — UC03.07.01]
- Đối tượng: Nhà cung cấp HHDV, Khách hàng DK05, Xe của khách hàng. ✅ [SRS Web tr.461 — UC03.07.01; SRS Web tr.505 — UC03.08.01; SRS Web tr.545 — UC03.09.01]
- Đường dẫn: Dashboards > Tab Danh mục > Sub-tab (NCC, KH, Xe). Xe: còn qua Thông tin khách hàng DK05 > Tab Xe của khách hàng. ✅ [SRS Web tr.545 — UC03.09.01]

## c. Pre-conditions

- Người dùng đã đăng nhập. ✅ [SRS Web tr.461 — UC03.07.01]
- Người dùng được phân quyền chức năng Xem của danh mục tương ứng. ✅ [SRS Web tr.461 — UC03.07.01]
- Xe, đường vào từ chi tiết khách hàng: thêm quyền Xem của Thông tin xe khách hàng DK05. ✅ [SRS Web tr.545 — UC03.09.01]

## d. Expected result

Hệ thống hiển thị thành công danh sách của danh mục. ✅ [SRS Web tr.461 — UC03.07.01; SRS Web tr.505 — UC03.08.01; SRS Web tr.545 — UC03.09.01]

## e. Activity diagram

Xem flows.md — Flow: Xem danh sách danh mục đối tác; Flow: Xem danh sách xe của khách hàng.

Main Success Scenario:
1. Hệ thống hiển thị Dashboards. ✅ [SRS Web tr.461 — hình lưu đồ UC03.07.01]
2. Người dùng chọn tab Danh mục ở Navigation bar. ✅ [SRS Web tr.461 — hình lưu đồ UC03.07.01]
3. Người dùng chọn sub-tab danh mục. ✅ [SRS Web tr.461 — hình lưu đồ UC03.07.01]
4. Hệ thống hiển thị màn Danh sách. ✅ [SRS Web tr.461 — hình lưu đồ UC03.07.01]
5. Người dùng tìm kiếm gần đúng, nhóm, lọc, Tuỳ chỉnh cột, đổi số bản ghi/trang, chuyển trang. 🟡 [SRS Web tr.462 — UC03.07.01]

Extensions:
- 2a. Xe: người dùng đang ở Thông tin khách hàng DK05, chọn tab Xe của khách hàng thay cho bước 2–3. 🔵 [SRS Web tr.545 — hình lưu đồ UC03.09.01 Xem danh mục xe của khách hàng]
- 5a. Nhấn Tạo mới: chuyển sang UC Tạo đề xuất (uc-create-partner-request). ✅ [SRS Web tr.464 — UC03.07.01]
- 5b. Nhấn một bản ghi: chuyển sang uc-view-partner-detail. ✅ [SRS Web tr.467 — UC03.07.02]
- 5c. Nhấn Huỷ đề xuất/Phê duyệt/Từ chối ở cột Hành động: chuyển sang uc-cancel-partner-request hoặc uc-approve-reject-partner-request. ✅ [SRS Web tr.488 — UC03.07.04; SRS Web tr.493 — UC03.07.05]
- 5d. Export, Import: theo Common Rules (ngoài lát). 🟡 [SRS Web tr.463 — UC03.07.01]

## f. Screens

Danh sách nhà cung cấp HHDV; Danh sách khách hàng DK05; Danh sách xe của khách hàng (xem spec Mục 10).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–4 | FR-business-partners-001 | BR-business-partners-008 | — | SRS Web tr.461 — UC03.07.01; SRS Web tr.505 — UC03.08.01; SRS Web tr.545 — UC03.09.01 |
| 5 tìm/nhóm/lọc/Tuỳ chỉnh | FR-business-partners-002, FR-business-partners-003, FR-business-partners-004, FR-business-partners-007 | — | — | SRS Web tr.462 — UC03.07.01; SRS Web tr.463 — UC03.07.01; SRS Web tr.464 — UC03.07.01 |
| 5 Export/Import | FR-business-partners-005, FR-business-partners-006 | — | — | SRS Web tr.463 — UC03.07.01 |
| Cột, trạng thái, Hành động | FR-business-partners-008, FR-business-partners-009 | BR-business-partners-005 | — | SRS Web tr.465 — UC03.07.01; SRS Web tr.466 — UC03.07.01 |
| Phân trang, Tạo mới | FR-business-partners-010, FR-business-partners-011 | — | — | SRS Web tr.466 — UC03.07.01; SRS Web tr.464 — UC03.07.01 |

## h. Open Questions

OQ-10, OQ-12 (xem gaps.md).
