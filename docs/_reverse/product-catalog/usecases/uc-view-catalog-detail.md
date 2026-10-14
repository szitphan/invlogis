# UC-view-catalog-detail — Xem thông tin bản ghi danh mục

## a. Introduction

Mở màn Thông tin của một bản ghi từ danh sách; ở trạng thái Đã huỷ / Đã từ chối còn cho Xoá yêu cầu và Tạo mới yêu cầu. Mã UC gốc: UC03.01.02 (DVKT), UC03.03.02 (PTVT), UC03.04.02 (CCDC), UC03.05.02 (Lốp), UC03.06.02 (Ắc quy). ✅ [SRS Web tr.293, 329, 365, 399, 432 — Xem thông tin (5 danh mục)]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.293 — UC03.01.02 Xem thông tin Dịch vụ kỹ thuật]
- Đối tượng: bản ghi danh mục, Lịch sử hoạt động ✅ [SRS Web tr.297 — UC03.01.02]

## c. Pre-conditions

- Người dùng đã đăng nhập vào hệ thống ✅ [SRS Web tr.293 — UC03.01.02]
- Người dùng được phân quyền vào chức năng Xem của danh mục ✅ [SRS Web tr.293 — UC03.01.02]

## d. Expected result

- Hiển thị thông tin chi tiết của bản ghi ✅ [SRS Web tr.293 — UC03.01.02]

## e. Activity diagram

Xem flows.md — Flow: Xem thông tin danh mục; hành động Xoá / Tạo mới yêu cầu xem flows.md — Flow: Xoá yêu cầu và Tạo mới yêu cầu từ bản đã huỷ hoặc đã từ chối.

Main Success Scenario:
1. Hệ thống hiển thị màn Danh sách ✅ [SRS Web tr.293 — hình lưu đồ UC03.01.02]
2. Người dùng chọn 1 bản ghi trong danh sách ✅ [SRS Web tr.293 — hình lưu đồ UC03.01.02]
3. Hệ thống hiển thị màn Thông tin: tên, mã (nếu có), các trường của danh mục, Trạng thái, Ghi chú (ẩn nếu không có) ✅ [SRS Web tr.294–295 — UC03.01.02]

Extensions:
- 3a. Trạng thái Chờ phê duyệt, người dùng có quyền: có nút Huỷ đề xuất / Phê duyệt / Từ chối ✅ [SRS Web tr.297, 307 — UC03.01.02, UC03.01.03]
- 3b. Trạng thái Đã huỷ hoặc Đã từ chối: nút "…" cho Xoá yêu cầu (popup Xác nhận xoá; Xoá thì toast "Xoá yêu cầu thành công" và về Danh sách; Huỷ thì quay lại Thông tin) và Tạo mới yêu cầu (mở màn Tạo mới với dữ liệu cũ, cập nhật bản ghi cũ, đưa về Chờ phê duyệt) ✅ [SRS Web tr.296–297 — UC03.01.02; SRS Web tr.311–312 — UC03.01.04]
- 3c. Trạng thái Đã phê duyệt: không có hành động nào thêm, ẩn icon "…" ✅ [SRS Web tr.321 — UC03.01.05; SRS Web tr.297 — UC03.01.02]
- 3d. Người dùng nhấn Lịch sử hoạt động: popup Lịch sử hoạt động ✅ [SRS Web tr.297 — UC03.01.02]
- 3e. Người dùng nhấn icon đóng: quay về Danh sách ✅ [SRS Web tr.297 — UC03.01.02]

## f. Screens

- Thông tin dịch vụ kỹ thuật / phụ tùng vật tư / công cụ dụng cụ / lốp / ắc quy (4 biến thể theo trạng thái); popup Xác nhận xoá; popup Lịch sử hoạt động (spec.md Mục 10)

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|------|----|----|-------|-------|
| 1, 2 | FR-product-catalog-005 | — | — | SRS Web tr.293 — hình lưu đồ UC03.01.02 |
| 3 | FR-product-catalog-006 | BR-product-catalog-011, BR-product-catalog-028 | — | SRS Web tr.294–295 — UC03.01.02 |
| 3a | FR-product-catalog-008 | BR-product-catalog-027 | — | SRS Web tr.297, 307 — UC03.01.02, UC03.01.03 |
| 3b | FR-product-catalog-007, FR-product-catalog-018, FR-product-catalog-019 | BR-product-catalog-018, BR-product-catalog-019 | — | SRS Web tr.296–297 — UC03.01.02 |
| 3c | FR-product-catalog-022 | — | — | SRS Web tr.321 — UC03.01.05 |
| 3d | FR-product-catalog-021 | — | — | SRS Web tr.297 — UC03.01.02 |

## h. Open Questions

OQ-3, OQ-4, OQ-10, OQ-16 (xem gaps.md)
