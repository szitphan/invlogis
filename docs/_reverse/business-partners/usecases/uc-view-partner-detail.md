# UC-view-partner-detail — Xem thông tin nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng

## a. Introduction

Hiển thị chi tiết một bản ghi và các hành động tuỳ trạng thái, quyền. Mã UC gốc: UC03.07.02, UC03.08.02, UC03.09.02. Một khuôn cho cả ba. ✅ [SRS Web tr.467 — UC03.07.02 Xem thông tin nhà cung cấp HHDV; SRS Web tr.510 — UC03.08.02 Xem thông tin khách hàng DK05; SRS Web tr.549 — UC03.09.02 Xem thông tin xe của khách hàng]

## b. Actors & Objects

Người dùng phần mềm xưởng; đối tượng: nhà cung cấp HHDV, khách hàng DK05 (kèm tab Xe khách hàng), xe của khách hàng. ✅ [SRS Web tr.467 — UC03.07.02; SRS Web tr.510 — UC03.08.02; SRS Web tr.549 — UC03.09.02]

## c. Pre-conditions

- Đã đăng nhập; được phân quyền Xem của danh mục. ✅ [SRS Web tr.467 — UC03.07.02]
- Đã đứng ở màn Danh sách và nhấn một bản ghi. ✅ [SRS Web tr.467 — UC03.07.02]

## d. Expected result

Hiển thị thông tin chi tiết của bản ghi. ✅ [SRS Web tr.467 — UC03.07.02]

## e. Activity diagram

Xem flows.md — Flow: Xem chi tiết bản ghi danh mục.

Main Success Scenario:
1. Hệ thống hiển thị màn Danh sách. ✅ [SRS Web tr.467 — hình lưu đồ UC03.07.02]
2. Người dùng chọn 1 bản ghi trong danh sách. ✅ [SRS Web tr.467 — hình lưu đồ UC03.07.02]
3. Hệ thống hiển thị màn Thông tin (tên, trạng thái, mã nếu có, các trường; Ghi chú ẩn khi trống). ✅ [SRS Web tr.468 — UC03.07.02; SRS Web tr.469 — UC03.07.02]

Extensions:
- 1a. Xe: có hai đường vào màn Danh sách (từ Danh mục > Danh sách xe khách hàng, hoặc từ Thông tin khách hàng DK05 > Danh sách xe khách hàng) rồi chọn 1 bản ghi. ✅ [SRS Web tr.549 — hình lưu đồ UC03.09.02 Xem thông tin xe của khách hàng]
- 3a. Trạng thái Chờ phê duyệt: hiển thị nút Huỷ đề xuất, Phê duyệt, Từ chối theo quyền; nhấn nút thực hiện UC Huỷ đề xuất hoặc Phê duyệt/Từ chối. ✅ [SRS Web tr.473 — UC03.07.02; SRS Web tr.487 — UC03.07.03]
- 3b. Trạng thái Đã huỷ/Đã từ chối: menu "…" có Xoá yêu cầu, Tạo mới yêu cầu (uc-delete-or-recreate-closed-request). ✅ [SRS Web tr.472 — UC03.07.02]
- 3c. Trạng thái Đã phê duyệt: không hành động thêm; ẩn icon "…". ✅ [SRS Web tr.473 — UC03.07.02; SRS Web tr.501 — UC03.07.05]
- 3d. Nhấn Lịch sử hoạt động: mở popup Lịch sử hoạt động. ✅ [SRS Web tr.473 — UC03.07.02]
- 3e. Nhấn icon đóng: quay về Danh sách. ✅ [SRS Web tr.473 — UC03.07.02]
- 3f. Khách hàng DK05: chuyển sang tab Xe khách hàng (tìm, lọc, Export, chọn xe, phân trang). ✅ [SRS Web tr.512 — UC03.08.02; SRS Web tr.515 — UC03.08.02]
- 3g. NCC trả sau: hiển thị thêm Thời điểm tính thời hạn thanh toán, Số ngày thanh toán, Ngày chốt tính công nợ. ✅ [SRS Web tr.470 — UC03.07.02]

## f. Screens

Thông tin nhà cung cấp HHDV; Thông tin khách hàng DK05 (2 tab); Thông tin xe của khách hàng; popup Lịch sử hoạt động.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–3 | FR-business-partners-012, FR-business-partners-013 | BR-business-partners-031 | — | SRS Web tr.467 — UC03.07.02; SRS Web tr.510 — UC03.08.02; SRS Web tr.549 — UC03.09.02 |
| 3a–3c | FR-business-partners-014, FR-business-partners-015 | BR-business-partners-005 | — | SRS Web tr.472 — UC03.07.02; SRS Web tr.473 — UC03.07.02 |
| 3d, 3e | FR-business-partners-016, FR-business-partners-017 | — | — | SRS Web tr.473 — UC03.07.02 |
| 3f | FR-business-partners-018 | — | — | SRS Web tr.512 — UC03.08.02; SRS Web tr.516 — UC03.08.02 |
| 3g | FR-business-partners-041, FR-business-partners-045 | BR-business-partners-018, BR-business-partners-022, BR-business-partners-023 | — | SRS Web tr.470 — UC03.07.02; SRS Web tr.471 — UC03.07.02 |

## h. Open Questions

OQ-9, OQ-13 (xem gaps.md).
