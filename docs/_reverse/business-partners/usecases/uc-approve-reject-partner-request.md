# UC-approve-reject-partner-request — Phê duyệt / Từ chối đề xuất cấp mới nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng

## a. Introduction

Người có quyền phê duyệt hoặc từ chối đề xuất đang Chờ phê duyệt. Mã UC gốc: UC03.07.05, UC03.08.05, UC03.09.05. Một khuôn cho cả ba; sinh mã chỉ NCC và KH. ✅ [SRS Web tr.493 — UC03.07.05 Phê duyệt/Từ chối đề xuất cấp mới nhà cung cấp HHDV; SRS Web tr.533 — UC03.08.05 Phê duyệt/Từ chối đề xuất cấp mới khách hàng DK05; SRS Web tr.570 — UC03.09.05 Phê duyệt/Từ chối đề xuất cấp mới xe của khách hàng]

## b. Actors & Objects

Người dùng phần mềm xưởng (có quyền Phê duyệt/Từ chối đề xuất tạo mới); người đã tạo yêu cầu (nhận thông báo). ✅ [SRS Web tr.493 — UC03.07.05; SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động]

## c. Pre-conditions

- Được phân quyền Phê duyệt/Từ chối đề xuất tạo mới của danh mục. ✅ [SRS Web tr.493 — UC03.07.05]
- Trạng thái bản ghi là Chờ phê duyệt. ✅ [SRS Web tr.493 — UC03.07.05]
- Đường vào: nút Phê duyệt/Từ chối ở cột Hành động màn Danh sách hoặc ở màn Thông tin (Xem). ✅ [SRS Web tr.493 — UC03.07.05]

## d. Expected result

Trạng thái đổi từ Chờ phê duyệt sang Đã phê duyệt hoặc Đã từ chối; toast thành công; tắt popup xác nhận; hiển thị màn Thông tin. ✅ [SRS Web tr.493 — UC03.07.05]

## e. Activity diagram

Xem flows.md — Flow: Phê duyệt hoặc Từ chối đề xuất.

Main Success Scenario (Phê duyệt):
1. Hệ thống hiển thị màn Thông tin hoặc Danh sách. ✅ [SRS Web tr.494 — hình lưu đồ UC03.07.05]
2. Người dùng nhấn Phê duyệt. ✅ [SRS Web tr.494 — hình lưu đồ UC03.07.05]
3. Hệ thống hiển thị popup Xác nhận phê duyệt ("Phê duyệt đề xuất tạo mới?" ... "Bạn có muốn phê duyệt đề xuất tạo mới này?"). ✅ [SRS Web tr.498 — hình mockup UC03.07.05]
4. Người dùng nhấn Phê duyệt trong popup. ✅ [SRS Web tr.494 — hình lưu đồ UC03.07.05]
5. Hệ thống báo toast và lưu trạng thái Đã phê duyệt. ✅ [SRS Web tr.499 — UC03.07.05]
6. Hệ thống sinh mã mới (NCC aabbb; KH DK05xxxxx; Xe: nguồn không ghi). ✅ [SRS Web tr.499 — UC03.07.05; SRS Web tr.539 — UC03.08.05]
7. Hệ thống gửi thông báo "... đã được phê duyệt." tới người đã tạo. ✅ [SRS Web tr.499 — UC03.07.05]
8. Hệ thống ghi Lịch sử hoạt động "Đã phê duyệt yêu cầu cấp mới". ✅ [SRS Web tr.500 — UC03.07.05]
9. Hệ thống hiển thị màn Thông tin (Đã phê duyệt, không hành động thêm). ✅ [SRS Web tr.501 — UC03.07.05]

Extensions:
- 2a. Từ chối: người dùng nhấn Từ chối, popup "Từ chối đề xuất tạo mới?" có ô lý do (không bắt buộc), nhấn Từ chối; trạng thái Đã từ chối; toast; thông báo "... đã bị từ chối." tới người đã tạo; Lịch sử hoạt động "Đã từ chối yêu cầu cấp mới" kèm "Lý do: ..."; màn Thông tin hiển thị Xoá yêu cầu, Tạo mới yêu cầu. ✅ [SRS Web tr.495 — UC03.07.05; SRS Web tr.496 — UC03.07.05; SRS Web tr.494 — hình mockup UC03.07.05]
- 4a. Người dùng nhấn Huỷ bỏ (hoặc Huỷ): đóng popup, trạng thái giữ Chờ phê duyệt, về màn Thông tin. ✅ [SRS Web tr.497 — UC03.07.05; SRS Web tr.500 — UC03.07.05]
- 4b. Người khác vừa huỷ đề xuất trước: ưu tiên Huỷ đề xuất; hệ thống hiển thị popup lỗi "Lỗi!" "Đề xuất tạo mới này đã bị huỷ. Vui lòng tải lại trang để cập nhật." nút "Tải lại trang". ✅ [SRS Web tr.496 — UC03.07.05; SRS Web tr.496 — hình mockup UC03.07.05]
- 4c. Phê duyệt khi người khác vừa phê duyệt/từ chối: nguồn không nói. <!-- TBD --> (OQ-15)

## f. Screens

Thông tin (Chờ phê duyệt, Đã từ chối, Đã phê duyệt); popup Xác nhận phê duyệt; popup Xác nhận từ chối; popup Lỗi tải lại trang.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–5, 9 | FR-business-partners-026 | BR-business-partners-002, BR-business-partners-004 | — | SRS Web tr.499 — UC03.07.05; SRS Web tr.539 — UC03.08.05; SRS Web tr.576 — UC03.09.05 |
| 6 | FR-business-partners-038, FR-business-partners-039 | BR-business-partners-008, BR-business-partners-024, BR-business-partners-025 | — | SRS Web tr.499 — UC03.07.05; SRS Web tr.500 — UC03.07.05; SRS Web tr.539 — UC03.08.05 |
| 7, 8 | FR-business-partners-034, FR-business-partners-036, FR-business-partners-037 | BR-business-partners-032 | — | SRS Web tr.499 — UC03.07.05; SRS Web tr.500 — UC03.07.05 |
| 2a | FR-business-partners-027, FR-business-partners-035 | BR-business-partners-007 | — | SRS Web tr.495 — UC03.07.05; SRS Web tr.496 — UC03.07.05 |
| 4a | FR-business-partners-028 | BR-business-partners-034 | — | SRS Web tr.497 — UC03.07.05; SRS Web tr.500 — UC03.07.05 |
| 4b | FR-business-partners-029 | BR-business-partners-006 | E-business-partners-008, E-business-partners-009 | SRS Web tr.496 — UC03.07.05; SRS Web tr.499 — UC03.07.05 |

## h. Open Questions

OQ-7, OQ-8, OQ-11, OQ-14, OQ-15 (xem gaps.md).
