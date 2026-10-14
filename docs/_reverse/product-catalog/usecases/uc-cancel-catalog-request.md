# UC-cancel-catalog-request — Huỷ đề xuất cấp mới

## a. Introduction

Huỷ một đề xuất tạo mới đang ở Chờ phê duyệt; bản ghi chuyển sang Đã huỷ. Mã UC gốc: UC03.01.04 (DVKT), UC03.03.04 (PTVT), UC03.04.04 (CCDC), UC03.05.04 (Lốp), UC03.06.04 (Ắc quy). ✅ [SRS Web tr.308, 344, 377, 412, 444 — Huỷ đề xuất cấp mới (5 danh mục)]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.308 — UC03.01.04 Huỷ đề xuất cấp mới Dịch vụ kỹ thuật]
- Đối tượng: bản ghi danh mục (Chờ phê duyệt), Thông báo, Lịch sử hoạt động ✅ [SRS Web tr.310 — UC03.01.04]

## c. Pre-conditions

- Người dùng được phân quyền vào chức năng Huỷ đề xuất tạo mới của danh mục ✅ [SRS Web tr.308 — UC03.01.04]
- Bản ghi ở trạng thái Chờ phê duyệt (DVKT và PTVT ghi "trạng thái xưởng") ✅ [SRS Web tr.308 — UC03.01.04; SRS Web tr.344 — UC03.03.04]

## d. Expected result

- Trạng thái bản ghi từ Chờ phê duyệt → Đã huỷ ✅ [SRS Web tr.308 — UC03.01.04]
- Hiển thị toast message thành công ✅ [SRS Web tr.308 — UC03.01.04]
- Tắt popup Xác nhận huỷ và hiển thị màn Thông tin ✅ [SRS Web tr.308 — UC03.01.04]

## e. Activity diagram

Xem flows.md — Flow: Huỷ đề xuất cấp mới.

Main Success Scenario:
1. Người dùng ở màn Thông tin hoặc màn Danh sách ✅ [SRS Web tr.308 — hình lưu đồ UC03.01.04]
2. Người dùng nhấn Huỷ đề xuất (ở cột Hành động hoặc ở màn Thông tin) ✅ [SRS Web tr.308 — UC03.01.04]
3. Hệ thống hiển thị popup "Huỷ đề xuất tạo mới?" (nút "Huỷ bỏ" / "Xác nhận", chữ ở FR-product-catalog-024) ✅ [SRS Web tr.308 — hình lưu đồ UC03.01.04; ảnh tr.309]
4. Người dùng nhấn Xác nhận ✅ [SRS Web tr.310 — UC03.01.04]
5. Hệ thống đổi trạng thái sang Đã huỷ, báo toast “Huỷ đề xuất tạo … thành công” (câu chữ theo danh mục; ảnh DVKT ghi “Huỷ đề xuất tạo mới thành công!”, OQ-23) ✅ [SRS Web tr.310 — UC03.01.04]
6. Hệ thống hiển thị màn Thông tin với 2 hành động: Xoá yêu cầu, Tạo mới yêu cầu ✅ [SRS Web tr.310 — UC03.01.04]
7. Hệ thống gửi thông báo cho người dùng có quyền phê duyệt: "… đã bị huỷ." ✅ [SRS Web tr.310 — UC03.01.04]
8. Hệ thống lưu Lịch sử hoạt động "Đã huỷ yêu cầu cấp mới" ✅ [SRS Web tr.310 — UC03.01.04]

Extensions:
- 4a. Người dùng nhấn Huỷ bỏ: trạng thái giữ nguyên Chờ phê duyệt; đóng popup và về màn Thông tin ✅ [SRS Web tr.311 — UC03.01.04]
- 4b. Tham chiếu: khi Phê duyệt/Từ chối xảy ra cùng lúc thì ưu tiên Huỷ đề xuất; popup lỗi xuất hiện ở phía người duyệt và được mô tả ở UC Phê duyệt/Từ chối, UC này không có thông báo lỗi nào 🔵 [SRS Web tr.316 — UC03.01.05; SRS Web tr.310–311 — UC03.01.04]
- 6a. Ở trạng thái Đã huỷ: Xoá yêu cầu / Tạo mới yêu cầu (xem UC-view-catalog-detail 3b) ✅ [SRS Web tr.311–312 — UC03.01.04]

## f. Screens

- Popup Xác nhận huỷ yêu cầu; màn Thông tin trạng thái Đã huỷ (spec.md Mục 10)

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|------|----|----|-------|-------|
| 1, 2 | FR-product-catalog-008 | BR-product-catalog-013, BR-product-catalog-027 | — | SRS Web tr.308 — UC03.01.04 |
| 3, 4 | FR-product-catalog-012 | BR-product-catalog-013 | — | SRS Web tr.310 — UC03.01.04 |
| 5 đến 8 | FR-product-catalog-012, FR-product-catalog-020, FR-product-catalog-021 | BR-product-catalog-021 | — | SRS Web tr.310 — UC03.01.04 |
| 4a | FR-product-catalog-016 | BR-product-catalog-016 | — | SRS Web tr.311 — UC03.01.04 |
| 4b (tham chiếu) | FR-product-catalog-017 | BR-product-catalog-017 | — (xem UC Phê duyệt/Từ chối) | SRS Web tr.316 — UC03.01.05 |
| 6a | FR-product-catalog-018, FR-product-catalog-019 | BR-product-catalog-018, BR-product-catalog-019 | — | SRS Web tr.311–312 — UC03.01.04 |

## h. Open Questions

OQ-2, OQ-3, OQ-16, OQ-23 (xem gaps.md)
