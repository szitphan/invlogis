# UC-approve-reject-catalog-request — Phê duyệt / Từ chối đề xuất cấp mới

## a. Introduction

Phê duyệt hoặc từ chối một đề xuất tạo mới đang ở Chờ phê duyệt. Phê duyệt sinh mã cho bản ghi. Mã UC gốc: UC03.01.05 (DVKT), UC03.03.05 (PTVT), UC03.04.05 (CCDC), UC03.05.05 (Lốp), UC03.06.05 (Ắc quy). Nguồn ghi tên UC "Phê duyệt/từ chối yêu cầu tạo mới …". ✅ [SRS Web tr.313, 349, 382, 417, 449 — Phê duyệt/Từ chối đề xuất cấp mới (5 danh mục)]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng (có quyền Phê duyệt/Từ chối) ✅ [SRS Web tr.313 — UC03.01.05 Phê duyệt/Từ chối đề xuất cấp mới Dịch vụ kỹ thuật]
- Đối tượng: bản ghi danh mục (Chờ phê duyệt), Thông báo, Lịch sử hoạt động ✅ [SRS Web tr.316, 319 — UC03.01.05]

## c. Pre-conditions

- Người dùng được phân quyền vào chức năng Phê duyệt/Từ chối đề xuất tạo mới của danh mục ✅ [SRS Web tr.313 — UC03.01.05]
- Bản ghi ở trạng thái Chờ phê duyệt ✅ [SRS Web tr.313 — UC03.01.05]

## d. Expected result

- Trạng thái bản ghi từ Chờ phê duyệt → Đã phê duyệt hoặc Đã từ chối ✅ [SRS Web tr.313 — UC03.01.05]
- Hiển thị toast message thành công ✅ [SRS Web tr.313 — UC03.01.05]
- Tắt popup Xác nhận và hiển thị màn Thông tin ✅ [SRS Web tr.313 — UC03.01.05]

## e. Activity diagram

Xem flows.md — Flow: Phê duyệt / Từ chối đề xuất cấp mới.

Main Success Scenario (Phê duyệt):
1. Người dùng ở màn Thông tin hoặc màn Danh sách ✅ [SRS Web tr.314 — hình lưu đồ UC03.01.05]
2. Người dùng nhấn Phê duyệt ✅ [SRS Web tr.314 — hình lưu đồ UC03.01.05]
3. Hệ thống hiển thị popup Xác nhận phê duyệt ✅ [SRS Web tr.314 — hình lưu đồ UC03.01.05]
4. Người dùng nhấn Phê duyệt trong popup ✅ [SRS Web tr.314 — hình lưu đồ UC03.01.05]
5. Hệ thống đổi trạng thái sang Đã phê duyệt, báo toast “Phê duyệt đề xuất tạo … thành công” ✅ [SRS Web tr.319 — UC03.01.05]
6. Hệ thống hiển thị màn Thông tin ✅ [SRS Web tr.319 — UC03.01.05]
7. Hệ thống gửi thông báo cho người dùng đã tạo yêu cầu: "… đã được phê duyệt." ✅ [SRS Web tr.319 — UC03.01.05]
8. Hệ thống sinh mã mới theo quy tắc của danh mục ✅ [SRS Web tr.319–320 — UC03.01.05]
9. Hệ thống lưu Lịch sử hoạt động "Đã phê duyệt yêu cầu cấp mới" ✅ [SRS Web tr.320 — UC03.01.05]

Main Success Scenario (Từ chối):
1. Người dùng ở màn Thông tin hoặc màn Danh sách ✅ [SRS Web tr.314 — hình lưu đồ UC03.01.05]
2. Người dùng nhấn Từ chối ✅ [SRS Web tr.314 — hình lưu đồ UC03.01.05]
3. Hệ thống hiển thị popup Xác nhận từ chối với trường Lý do từ chối (không bắt buộc) ✅ [SRS Web tr.314–315 — UC03.01.05]
4. Người dùng nhập lý do (tuỳ chọn) và nhấn Từ chối ✅ [SRS Web tr.315–316 — UC03.01.05]
5. Hệ thống đổi trạng thái sang Đã từ chối, báo toast “Từ chối đề xuất tạo … thành công” (ảnh DVKT ghi “Từ chối tạo mới dịch vụ kỹ thuật thành công!”, OQ-23) ✅ [SRS Web tr.316 — UC03.01.05]
6. Hệ thống hiển thị màn Thông tin với 2 hoạt động: Xoá yêu cầu, Tạo mới yêu cầu ✅ [SRS Web tr.316 — UC03.01.05]
7. Hệ thống gửi thông báo cho người dùng đã tạo yêu cầu: "… đã bị từ chối." ✅ [SRS Web tr.316 — UC03.01.05]
8. Hệ thống lưu Lịch sử hoạt động "Đã từ chối yêu cầu cấp mới" kèm "Lý do: [lý do người dùng nhập]" ✅ [SRS Web tr.316 — UC03.01.05]

Extensions:
- 4a. Người dùng nhấn Huỷ bỏ (popup từ chối) hoặc Huỷ (popup phê duyệt trên ảnh; bảng ghi Huỷ bỏ) ở popup: trạng thái giữ nguyên Chờ phê duyệt; đóng popup và về màn Thông tin ✅ [SRS Web tr.317, 320 — UC03.01.05]
- 4b. Người khác vừa huỷ đề xuất trước (hoặc huỷ và duyệt cùng lúc): ưu tiên Huỷ; hệ thống hiển thị popup lỗi (tiêu đề “Lỗi!”, nội dung “Đề xuất tạo mới này đã bị huỷ. Vui lòng tải lại trang để cập nhật.”, nút “Tải lại trang”, chữ trên ảnh giống ở 5 danh mục) ✅ [SRS Web tr.316, 319 — UC03.01.05]
- 6a. Ở trạng thái Đã từ chối: Xoá yêu cầu / Tạo mới yêu cầu ✅ [SRS Web tr.317–318 — UC03.01.05]
- 6b. Ở trạng thái Đã phê duyệt: không có hành động nào thêm ✅ [SRS Web tr.321 — UC03.01.05]

## f. Screens

- Popup Xác nhận phê duyệt; popup Xác nhận từ chối; popup lỗi Tải lại trang; màn Thông tin các trạng thái Đã từ chối, Đã phê duyệt (spec.md Mục 10)

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|------|----|----|-------|-------|
| Phê duyệt 1 đến 4 | FR-product-catalog-008, FR-product-catalog-014 | BR-product-catalog-014, BR-product-catalog-027 | — | SRS Web tr.314, 318 — UC03.01.05 |
| Phê duyệt 5 đến 7, 9 | FR-product-catalog-014, FR-product-catalog-020, FR-product-catalog-021 | BR-product-catalog-014, BR-product-catalog-021 | — | SRS Web tr.319–320 — UC03.01.05 |
| Phê duyệt 8 | FR-product-catalog-015 | BR-product-catalog-022 đến BR-product-catalog-026 | — | SRS Web tr.319–320 — UC03.01.05 |
| Từ chối 1 đến 4 | FR-product-catalog-008, FR-product-catalog-013 | BR-product-catalog-014, BR-product-catalog-015 | — | SRS Web tr.314–316 — UC03.01.05 |
| Từ chối 5 đến 8 | FR-product-catalog-013, FR-product-catalog-020, FR-product-catalog-021 | BR-product-catalog-014, BR-product-catalog-021 | — | SRS Web tr.316 — UC03.01.05 |
| 4a | FR-product-catalog-016 | BR-product-catalog-016 | — | SRS Web tr.317, 320 — UC03.01.05 |
| 4b | FR-product-catalog-017 | BR-product-catalog-017 | E-product-catalog-003, E-product-catalog-004 | SRS Web tr.316, 319 — UC03.01.05 |
| 6a, 6b | FR-product-catalog-018, FR-product-catalog-019, FR-product-catalog-022 | BR-product-catalog-018, BR-product-catalog-019 | — | SRS Web tr.317–318, 321 — UC03.01.05 |

## h. Open Questions

OQ-3, OQ-5, OQ-6, OQ-7, OQ-8, OQ-14, OQ-19, OQ-23 (xem gaps.md)
