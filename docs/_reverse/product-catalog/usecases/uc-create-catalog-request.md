# UC-create-catalog-request — Tạo đề xuất tạo mới bản ghi danh mục

## a. Introduction

Người dùng đề xuất tạo mới một bản ghi danh mục; hệ thống kiểm tra, tạo bản ghi ở Chờ phê duyệt, thông báo cho người duyệt và ghi lịch sử. Mã UC gốc: UC03.01.03 (DVKT), UC03.03.03 (PTVT), UC03.04.03 (CCDC), UC03.05.03 (Lốp), UC03.06.03 (Ắc quy). Trường của từng danh mục ở spec.md Mục 3 bảng Khác biệt. ✅ [SRS Web tr.298, 334, 370, 404, 437 — Tạo đề xuất tạo mới (5 danh mục)]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.298 — UC03.01.03 Tạo đề xuất tạo mới Dịch vụ kỹ thuật]
- Đối tượng: bản ghi danh mục mới, Thông báo, Lịch sử hoạt động ✅ [SRS Web tr.302 — UC03.01.03]

## c. Pre-conditions

- Người dùng đã đăng nhập vào hệ thống ✅ [SRS Web tr.298 — UC03.01.03]
- Người dùng được phân quyền vào chức năng Tạo đề xuất tạo mới của danh mục ✅ [SRS Web tr.298 — UC03.01.03]

## d. Expected result

- Hệ thống tạo 1 bản ghi ở trạng thái Chờ phê duyệt ✅ [SRS Web tr.298 — UC03.01.03]
- Hiển thị toast message tạo thành công ✅ [SRS Web tr.298 — UC03.01.03]
- Hiển thị màn Thông tin (Xem) của bản ghi ✅ [SRS Web tr.298 — UC03.01.03]

## e. Activity diagram

Xem flows.md — Flow: Tạo đề xuất tạo mới (và Flow: Huỷ bỏ khi đang tạo đề xuất).

Main Success Scenario:
1. Hệ thống hiển thị màn Danh sách ✅ [SRS Web tr.298 — hình lưu đồ UC03.01.03]
2. Người dùng nhấn Tạo mới ✅ [SRS Web tr.298 — hình lưu đồ UC03.01.03]
3. Hệ thống hiển thị form Tạo mới (panel trượt bên phải trên ảnh; lưu đồ gọi "popup", mô tả gọi "màn hình") ✅ [SRS Web tr.298–299 — UC03.01.03 và ảnh tr.299]
4. Người dùng nhập các thông tin và xác nhận bằng nút Tạo mới ✅ [SRS Web tr.298, 302 — UC03.01.03]
5. Hệ thống kiểm tra validate ✅ [SRS Web tr.298 — hình lưu đồ UC03.01.03]
6. Hệ thống báo toast và lưu bản ghi mới ở Chờ phê duyệt ✅ [SRS Web tr.302 — UC03.01.03]
7. Hệ thống gửi thông báo cho người dùng có quyền phê duyệt ✅ [SRS Web tr.302 — UC03.01.03]
8. Hệ thống lưu 1 bản ghi Lịch sử hoạt động "Đã tạo yêu cầu cấp mới" ✅ [SRS Web tr.302 — UC03.01.03]
9. Hệ thống chuyển sang màn Thông tin (xem) với 3 hành động tuỳ phân quyền (Huỷ đề xuất, Phê duyệt, Từ chối) ✅ [SRS Web tr.302 — UC03.01.03]

Extensions:
- 5a. Tên trùng: báo lỗi in-line “Tên này đã bị trùng.” ✅ [SRS Web tr.299 — UC03.01.03]
- 5b. Trường khác không hợp lệ: thông báo lỗi in-line dưới trường ✅ [SRS Web tr.303 — UC03.01.03]
- 4a. Người dùng nhấn Huỷ hoặc icon đóng: hộp thoại "Huỷ tạo mới?" (nút "Huỷ" / "Xác nhận", chữ ở FR-product-catalog-024); Xác nhận thì không tạo bản ghi và về Danh sách, Hủy thì quay lại form với dữ liệu đã nhập ✅ [SRS Web tr.303–304 — UC03.01.03]
- 4b. Chọn Loại phương tiện trước rồi mới chọn Mã phương tiện - Tên phương tiện trong danh sách thuộc loại đó (DVKT, PTVT, Lốp, Ắc quy) ✅ [SRS Web tr.300 — UC03.01.03]

## f. Screens

- Tạo mới DVKT / PTVT / CCDC / lốp / ắc quy; hộp thoại xác nhận huỷ tạo mới; màn Thông tin (Chờ phê duyệt) (spec.md Mục 10)

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|------|----|----|-------|-------|
| 1, 2 | FR-product-catalog-004 | — | — | SRS Web tr.291, 298 — UC03.01.01, UC03.01.03 |
| 3, 4 | FR-product-catalog-009 | BR-product-catalog-002 đến BR-product-catalog-010, BR-product-catalog-032 | — | SRS Web tr.299–301 — UC03.01.03 |
| 5, 5a, 5b | FR-product-catalog-010 | BR-product-catalog-001, BR-product-catalog-002, BR-product-catalog-031 | E-product-catalog-001, E-product-catalog-002, E-product-catalog-005 | SRS Web tr.299, 302–303 — UC03.01.03 |
| 6, 7, 8, 9 | FR-product-catalog-010, FR-product-catalog-020, FR-product-catalog-021 | BR-product-catalog-012, BR-product-catalog-021 | — | SRS Web tr.302 — UC03.01.03 |
| 4a | FR-product-catalog-011 | BR-product-catalog-020, BR-product-catalog-030 | — | SRS Web tr.303–304 — UC03.01.03 |

## h. Open Questions

OQ-1, OQ-5, OQ-7, OQ-9, OQ-13, OQ-15, OQ-20, OQ-22, OQ-24, OQ-25, OQ-26 (xem gaps.md)
