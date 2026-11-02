# UC-cancel-partner-request — Huỷ đề xuất cấp mới nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng

## a. Introduction

Người dùng huỷ đề xuất đang Chờ phê duyệt, bản ghi sang Đã huỷ. Mã UC gốc: UC03.07.04, UC03.08.04, UC03.09.04. Một khuôn cho cả ba. ✅ [SRS Web tr.488 — UC03.07.04 Huỷ đề xuất cấp mới nhà cung cấp HHDV; SRS Web tr.528 — UC03.08.04 Huỷ đề xuất cấp mới khách hàng DK05; SRS Web tr.565 — UC03.09.04 Huỷ đề xuất cấp mới xe của khách hàng]

## b. Actors & Objects

Người dùng phần mềm xưởng (có quyền Huỷ đề xuất tạo mới); người có quyền phê duyệt (nhận thông báo). ✅ [SRS Web tr.488 — UC03.07.04; SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động]

## c. Pre-conditions

- Được phân quyền Huỷ đề xuất tạo mới của danh mục. ✅ [SRS Web tr.488 — UC03.07.04]
- Trạng thái bản ghi là Chờ phê duyệt. ✅ [SRS Web tr.488 — UC03.07.04]
- Đường vào: nút Huỷ đề xuất ở cột Hành động màn Danh sách hoặc ở màn Thông tin (Xem). ✅ [SRS Web tr.488 — UC03.07.04]

## d. Expected result

Trạng thái đổi từ Chờ phê duyệt sang Đã huỷ; toast thành công; tắt popup Xác nhận huỷ; hiển thị màn Thông tin với 2 hành động Xoá yêu cầu, Tạo mới yêu cầu. ✅ [SRS Web tr.488 — UC03.07.04; SRS Web tr.490 — UC03.07.04]

## e. Activity diagram

Xem flows.md — Flow: Huỷ đề xuất tạo mới.

Main Success Scenario:
1. Hệ thống hiển thị màn Thông tin hoặc màn Danh sách. ✅ [SRS Web tr.489 — hình lưu đồ UC03.07.04]
2. Người dùng nhấn Huỷ đề xuất. ✅ [SRS Web tr.489 — hình lưu đồ UC03.07.04]
3. Hệ thống hiển thị popup Xác nhận huỷ ("Huỷ đề xuất tạo mới?" ... "Bạn có chắc chắn muốn huỷ đề xuất này không?"). ✅ [SRS Web tr.489 — hình lưu đồ và hình mockup UC03.07.04]
4. Người dùng nhấn Xác nhận. ✅ [SRS Web tr.489 — hình lưu đồ UC03.07.04]
5. Hệ thống báo toast và lưu trạng thái mới Đã huỷ. ✅ [SRS Web tr.490 — UC03.07.04]
6. Hệ thống gửi thông báo tới người có quyền phê duyệt (nội dung "... đã bị huỷ."). ✅ [SRS Web tr.490 — UC03.07.04]
7. Hệ thống ghi Lịch sử hoạt động "Đã huỷ yêu cầu cấp mới". ✅ [SRS Web tr.490 — UC03.07.04]
8. Hệ thống chuyển sang màn Thông tin (view mode, Đã huỷ). ✅ [SRS Web tr.489 — hình lưu đồ UC03.07.04]

Extensions:
- 4a. Người dùng nhấn Huỷ bỏ: đóng popup, trạng thái giữ Chờ phê duyệt, về màn Thông tin. ✅ [SRS Web tr.491 — UC03.07.04]
- 4b. Có người đã phê duyệt/từ chối cùng lúc: ưu tiên Huỷ đề xuất (người kia nhận popup lỗi, xem uc-approve-reject-partner-request). ✅ [SRS Web tr.496 — UC03.07.05]
- 2a. Người dùng không có quyền hoặc bản ghi đã không còn Chờ phê duyệt: không có nút Huỷ đề xuất. 🔵 [SRS Web tr.488 — UC03.07.04]

## f. Screens

Danh sách (cột Hành động); Thông tin (Chờ phê duyệt, Đã huỷ); popup Xác nhận huỷ.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–3 | FR-business-partners-023 | BR-business-partners-003 | — | SRS Web tr.488 — UC03.07.04; SRS Web tr.489 — UC03.07.04 |
| 4–8 | FR-business-partners-024, FR-business-partners-033, FR-business-partners-036, FR-business-partners-037 | BR-business-partners-002, BR-business-partners-032 | — | SRS Web tr.490 — UC03.07.04; SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động |
| 4a | FR-business-partners-025 | BR-business-partners-034 | — | SRS Web tr.491 — UC03.07.04 |
| 4b | FR-business-partners-029 | BR-business-partners-006 | E-business-partners-008, E-business-partners-009 | SRS Web tr.496 — UC03.07.05 |

## h. Open Questions

OQ-11, OQ-15 (xem gaps.md).
