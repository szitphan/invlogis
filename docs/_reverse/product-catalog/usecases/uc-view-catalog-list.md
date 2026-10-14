# UC-view-catalog-list — Xem danh sách danh mục (Dịch vụ kỹ thuật, Phụ tùng vật tư, Công cụ dụng cụ, Lốp, Ắc quy)

## a. Introduction

Mở màn Danh sách của một trong 5 danh mục, tìm kiếm, nhóm, lọc, xuất/nhập, tuỳ chỉnh cột và đi tới Tạo mới hoặc Thông tin. Mã UC gốc: UC03.01.01 (DVKT), UC03.03.01 (PTVT), UC03.04.01 (CCDC), UC03.05.01 (Lốp), UC03.06.01 (Ắc quy). Viết một lần cho cả khuôn, khác biệt từng danh mục ở spec.md Mục 3 bảng "Khác biệt theo danh mục". ✅ [SRS Web tr.288, 325, 361, 394, 427 — Xem danh mục (5 danh mục)]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.288 — UC03.01.01 Xem danh mục Dịch vụ kỹ thuật]
- Đối tượng: bản ghi danh mục (DVKT / PTVT / CCDC / Lốp / Ắc quy), Trạng thái ✅ [SRS Web tr.291 — UC03.01.01]

## c. Pre-conditions

- Người dùng đã đăng nhập vào hệ thống ✅ [SRS Web tr.288 — UC03.01.01]
- Người dùng được phân quyền vào chức năng Xem của danh mục tương ứng ✅ [SRS Web tr.288 — UC03.01.01]

## d. Expected result

- Hệ thống hiển thị danh sách của danh mục thành công ✅ [SRS Web tr.288 — UC03.01.01; SRS Web tr.325 — UC03.03.01]

## e. Activity diagram

Xem flows.md — Flow: Xem danh sách danh mục.

Main Success Scenario:
1. Hiển thị màn Dashboards ✅ [SRS Web tr.288 — hình lưu đồ UC03.01.01]
2. Người dùng chọn tab Danh mục ở Navigation bar ✅ [SRS Web tr.288 — hình lưu đồ UC03.01.01]
3. Người dùng chọn sub-tab của danh mục ✅ [SRS Web tr.288 — hình lưu đồ UC03.01.01]
4. Hệ thống hiển thị màn Danh sách ✅ [SRS Web tr.288 — hình lưu đồ UC03.01.01]

Extensions:
- 4a. Người dùng nhập thanh tìm kiếm: tìm gần đúng trên toàn bộ bảng ✅ [SRS Web tr.289 — UC03.01.01]
- 4b. Người dùng dùng Nhóm hoặc Bộ lọc theo các cột của danh mục ✅ [SRS Web tr.289–290 — UC03.01.01]
- 4c. Người dùng dùng Export, Import, Tuỳ chỉnh (chi tiết ở Common Rules) ✅ [SRS Web tr.290 — UC03.01.01]
- 4d. Người dùng nhấn Tạo mới: chuyển sang UC Tạo đề xuất tạo mới ✅ [SRS Web tr.291 — UC03.01.01]
- 4e. Người dùng nhấn một hành động ở cột Hành động: chuyển sang UC Huỷ đề xuất hoặc UC Phê duyệt/Từ chối ✅ [SRS Web tr.291 — UC03.01.01; SRS Web tr.308 — UC03.01.04]
- 4f. Người dùng nhấn vào 1 bản ghi: chuyển sang UC Xem thông tin ✅ [SRS Web tr.293 — UC03.01.02]

## f. Screens

- Danh sách dịch vụ kỹ thuật / phụ tùng vật tư / công cụ dụng cụ / lốp / ắc quy (spec.md Mục 10)

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|------|----|----|-------|-------|
| 1 đến 4 | FR-product-catalog-001 | BR-product-catalog-027 | — | SRS Web tr.288 — hình lưu đồ UC03.01.01 |
| 4a, 4b | FR-product-catalog-002 | BR-product-catalog-029 | — | SRS Web tr.289–290 — UC03.01.01 |
| 4c | FR-product-catalog-003 | — | — | SRS Web tr.290 — UC03.01.01 |
| 4 (cột, phân trang) | FR-product-catalog-004 | BR-product-catalog-012, BR-product-catalog-027 | — | SRS Web tr.291–292 — UC03.01.01 |
| 4d | FR-product-catalog-004, FR-product-catalog-009 | — | — | SRS Web tr.291 — UC03.01.01 |

## h. Open Questions

OQ-11, OQ-12, OQ-17, OQ-18 (xem gaps.md)
