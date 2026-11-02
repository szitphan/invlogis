# UC-delete-or-recreate-closed-request — Xoá yêu cầu / Tạo mới yêu cầu từ yêu cầu đã huỷ hoặc đã từ chối

## a. Introduction

Hai hành động ở menu "…" khi bản ghi ở trạng thái Đã huỷ/Đã từ chối: Xoá yêu cầu và Tạo mới yêu cầu (tạo lại từ thông tin cũ). Không có mã UC riêng: mô tả nằm trong UC03.07.02/04/05, UC03.08.02/04/05, UC03.09.02/04/05 (nguồn đặt dưới các mục "Màn hình Thông tin (Xem) — Trạng thái Đã huỷ/Đã từ chối"). Một khuôn cho cả ba. Việc tách thành một use case riêng là suy luận của người viết (🔵); từng bước dưới đây ✅ [SRS Web tr.472 — UC03.07.02 Xem thông tin nhà cung cấp HHDV; SRS Web tr.491 — UC03.07.04 Huỷ đề xuất cấp mới nhà cung cấp HHDV; SRS Web tr.497 — UC03.07.05 Phê duyệt/Từ chối đề xuất cấp mới nhà cung cấp HHDV]

## b. Actors & Objects

Người dùng phần mềm xưởng; quyền cụ thể cho Xoá yêu cầu/Tạo mới yêu cầu nguồn không nêu. 🟡 [SRS Web tr.472 — UC03.07.02]

## c. Pre-conditions

Bản ghi ở trạng thái Đã huỷ hoặc Đã từ chối; người dùng ở màn Thông tin. ✅ [SRS Web tr.472 — UC03.07.02]

## d. Expected result

- Xoá yêu cầu: yêu cầu bị xoá, toast "Xoá yêu cầu thành công", đóng mọi popup, về màn Danh sách. ✅ [SRS Web tr.472 — UC03.07.02; SRS Web tr.492 — UC03.07.04]
- Tạo mới yêu cầu: hiển thị form Tạo mới với dữ liệu từ yêu cầu hiện tại; Xe: cập nhật cùng bản ghi, trạng thái về Chờ phê duyệt. ✅ [SRS Web tr.492 — UC03.07.04; SRS Web tr.569 — UC03.09.04 Huỷ đề xuất cấp mới xe của khách hàng]

## e. Activity diagram

Xem flows.md — Flow: Xoá yêu cầu hoặc Tạo mới yêu cầu từ yêu cầu đã huỷ hoặc đã từ chối.

Main Success Scenario (Xoá yêu cầu):
1. Người dùng nhấn icon "…" và chọn Xoá yêu cầu. ✅ [SRS Web tr.472 — UC03.07.02]
2. Hệ thống hiển thị popup Xác nhận xoá ("Xoá yêu cầu?" ... "Bạn có chắc chắn muốn xoá yêu cầu này không?", nút Huỷ/Xoá). ✅ [SRS Web tr.472 — hình mockup UC03.07.02]
3. Người dùng nhấn Xoá; hệ thống xoá yêu cầu, báo toast, đóng popup, về Danh sách. ✅ [SRS Web tr.472 — UC03.07.02]

Extensions:
- 3a. Người dùng nhấn Huỷ: quay về màn Thông tin. ✅ [SRS Web tr.472 — UC03.07.02]
- 1a. Chọn Tạo mới yêu cầu: hệ thống hiển thị màn Tạo mới yêu cầu cấp mới, thực hiện UC Tạo đề xuất (uc-create-partner-request) với trường lấy thông tin từ yêu cầu hiện tại. ✅ [SRS Web tr.473 — UC03.07.02; SRS Web tr.492 — UC03.07.04]
- 1b. Xe: Tạo mới yêu cầu không sinh bản ghi mới mà cập nhật thông tin chỉnh sửa và trạng thái về Chờ phê duyệt. ✅ [SRS Web tr.569 — UC03.09.04; SRS Web tr.575 — UC03.09.05]
- 1c. NCC, KH: nguồn không nói bản ghi mới hay cập nhật. 🟡 [SRS Web tr.492 — UC03.07.04; SRS Web tr.532 — UC03.08.04]

## f. Screens

Thông tin (Đã huỷ, Đã từ chối) có menu "…"; popup Xác nhận xoá; form Tạo mới.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–3 | FR-business-partners-015, FR-business-partners-030 | BR-business-partners-005, BR-business-partners-035 | — | SRS Web tr.472 — UC03.07.02; SRS Web tr.492 — UC03.07.04 |
| 1a, 1b, 1c | FR-business-partners-031 | BR-business-partners-030 | — | SRS Web tr.473 — UC03.07.02; SRS Web tr.569 — UC03.09.04 |

## h. Open Questions

OQ-3, OQ-4 (xem gaps.md).
