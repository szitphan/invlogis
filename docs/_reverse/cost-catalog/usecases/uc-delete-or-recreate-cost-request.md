# UC-delete-or-recreate-cost-request — Xoá yêu cầu / Tạo mới yêu cầu từ bản đã huỷ hoặc đã từ chối

## a. Introduction

Hai hành động ở trạng thái Đã huỷ / Đã từ chối: Xoá yêu cầu và Tạo mới yêu cầu (tạo lại từ dữ liệu cũ). Nguồn không có mã UC riêng; mô tả nằm trong màn "Thông tin chi phí cấp N — Đã huỷ" của UC03.10.04, UC03.11.04, UC03.12.04, mục Đã từ chối của UC03.10.05, UC03.11.05, UC03.12.05 và cột Hành động của UC03.10.02, UC03.11.02, UC03.12.02. Nhóm cùng khuôn cho ba cấp. 🔵 (suy ra là 1 use case từ nhiều chỗ mô tả; nội dung từng bước ✅) [SRS Web tr.589–590, 601–602, 607–608, 623–624, 635–636, 641–642, 655–656, 669–670, 675–676]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng 🔵 (quyền thực hiện không nêu riêng; OQ-7)
- Đối tượng: Chi phí cấp N (trạng thái Đã huỷ hoặc Đã từ chối)

## c. Pre-conditions

- Bản ghi ở Đã huỷ hoặc Đã từ chối ✅ [SRS Web tr.589, 284 — Lưu đồ trạng thái chung]
- Người dùng ở màn Thông tin chi phí cấp N, hoặc cột Hành động của danh sách ✅

## d. Expected result

- Xoá yêu cầu: toast "Xoá yêu cầu thành công", đóng mọi popup, về Danh sách chi phí cấp N ✅ [SRS Web tr.589, 601]
- Tạo mới yêu cầu: bản ghi được cập nhật thông tin chỉnh sửa và đưa về Chờ phê duyệt, không sinh bản ghi mới ✅ [SRS Web tr.602, 608]

## e. Activity diagram

Xem flows.md — Flow: Xoá yêu cầu và tạo lại yêu cầu từ bản đã huỷ hoặc đã từ chối

Main Success Scenario (Xoá yêu cầu):
1. Người dùng chọn "…" > Xoá yêu cầu ✅
2. Hệ thống hiện popup "Xoá yêu cầu?" — "Bạn có chắc chắn muốn xoá yêu cầu này không?" ✅ [SRS Web tr.589 — hình mockup]
3. Người dùng bấm Xoá; hệ thống xoá yêu cầu, toast "Xoá yêu cầu thành công", về Danh sách ✅

Main Success Scenario (Tạo mới yêu cầu):
1. Người dùng chọn "…" > Tạo mới yêu cầu ✅
2. Hệ thống hiển thị màn Tạo mới yêu cầu cấp mới với các trường lấy từ yêu cầu hiện tại ✅ [SRS Web tr.589–590]
3. Người dùng chỉnh sửa và xác nhận theo UC Tạo đề xuất; hệ thống cập nhật bản ghi và đặt trạng thái Chờ phê duyệt ✅ [SRS Web tr.602, 608]; trường nào sửa được: nguồn không nói

Extensions:
- 3a (Xoá). Bấm Huỷ trong popup: về màn Thông tin chi phí cấp N ✅ [SRS Web tr.589, 601]
- 1a. Ở màn Thông tin: trạng thái Chờ phê duyệt hoặc Đã phê duyệt ẩn biểu tượng "…" ✅ [SRS Web tr.590; hình mockup tr.596, 610]. Ở Danh sách: ảnh hiện "…" mọi dòng, nguồn không nói ẩn theo trạng thái 🟡 [SRS Web tr.582]

## f. Screens

Thông tin chi phí cấp N (Đã huỷ / Đã từ chối); popup Xoá yêu cầu; Tạo mới yêu cầu.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| Xoá 1–3 | FR-cost-catalog-019 | BR-cost-catalog-022 | — | SRS Web tr.589–590, 601 — UC03.10.02, UC03.10.04 |
| Tạo lại 1–3 | FR-cost-catalog-020 | BR-cost-catalog-022, BR-cost-catalog-023 | — | SRS Web tr.589–590, 602, 608 — UC03.10.02, UC03.10.04, UC03.10.05 |

## h. Open Questions

OQ-4 (xoá hẳn hay ẩn), OQ-13 (tạo lại sửa gì, lịch sử, thông báo)
