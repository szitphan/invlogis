# UC-approve-reject-cost-proposal — Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3

## a. Introduction

Phê duyệt hoặc từ chối đề xuất tạo mới khoản mục đang Chờ phê duyệt; phê duyệt sinh mã chi phí. Mã UC gốc: UC03.10.05, UC03.11.05, UC03.12.05. Nhóm cùng khuôn, viết một lần. ✅ [SRS Web tr.603, 637, 671 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng (có quyền Phê duyệt/Từ chối) ✅ [SRS Web tr.603 — UC03.10.05]
- Đối tượng: Chi phí cấp N, người đã tạo yêu cầu (nhận thông báo), Lịch sử hoạt động ✅

## c. Pre-conditions

- Được phân quyền Phê duyệt/Từ chối đề xuất tạo mới của Danh mục - Chi phí cấp N ✅
- Bản ghi ở Chờ phê duyệt ✅ [SRS Web tr.603, 637, 671]
- Đường dẫn: nút Phê duyệt/Từ chối ở cột Hành động của danh sách, hoặc màn Thông tin (xem) ✅

## d. Expected result

- Trạng thái Chờ phê duyệt → Đã phê duyệt hoặc Đã từ chối ✅
- Toast thành công; tắt popup, hiển thị màn Thông tin chi phí cấp N ✅ [SRS Web tr.603, 637, 671]

## e. Activity diagram

Xem flows.md — Flow: Phê duyệt hoặc từ chối đề xuất tạo mới

Main Success Scenario (phê duyệt):
1. Người dùng bấm Phê duyệt; popup "Phê duyệt đề xuất tạo mới?" — "Bạn có muốn phê duyệt đề xuất tạo mới này?" ✅ [SRS Web tr.608 — hình mockup]
2. Người dùng bấm Phê duyệt trong popup ✅
3. Hệ thống đổi trạng thái sang Đã phê duyệt, toast "Phê duyệt đề xuất tạo chi phí cấp N thành công" ✅ [SRS Web tr.609]
4. Hệ thống sinh mã chi phí (cấp 1: aa; cấp 2: xxaa; cấp 3: xxaabbb) ✅
5. Gửi thông báo "[Tên chi phí] đã được phê duyệt." tới người đã tạo yêu cầu; lưu lịch sử "Đã phê duyệt yêu cầu cấp mới" ✅
6. Hiển thị màn Thông tin chi phí cấp N (Đã phê duyệt, không thêm hành động) ✅ [SRS Web tr.610]

Main Success Scenario (từ chối):
1. Người dùng bấm Từ chối; popup "Từ chối đề xuất tạo mới?" — "Bạn có chắc chắn muốn từ chối duyệt tạo mới này? Vui lòng nhập lý do từ chối." với ô "Nhập lý do từ chối tạo mới..." ✅ [SRS Web tr.604 — hình mockup]
2. Người dùng nhập lý do và bấm Từ chối; bảng trường ghi không bắt buộc nhưng ảnh nhắc "Vui lòng nhập lý do" 🟡 [SRS Web tr.605; hình mockup tr.604]
3. Hệ thống đổi trạng thái sang Đã từ chối, toast "Từ chối đề xuất tạo chi phí cấp N thành công" ✅ [SRS Web tr.606]
4. Gửi thông báo "[Tên chi phí] đã bị từ chối." tới người đã tạo; lưu lịch sử "Đã từ chối yêu cầu cấp mới / Lý do: …" ✅
5. Hiển thị màn Thông tin chi phí cấp N với Xoá yêu cầu, Tạo mới yêu cầu ✅ [SRS Web tr.606–607]

Extensions:
- 2a. Bấm Huỷ/Huỷ bỏ trong popup: giữ Chờ phê duyệt, về màn Thông tin ✅ [SRS Web tr.607, 610]
- 3a. Người khác vừa huỷ đề xuất trước: popup lỗi "Lỗi! Đề xuất tạo mới này đã bị huỷ. Vui lòng tải lại trang để cập nhật." nút Tải lại trang; ưu tiên hành động Huỷ ✅ [SRS Web tr.606, 609 — mô tả và hình mockup]

## f. Screens

Popup Phê duyệt; popup Từ chối (có ô lý do); popup lỗi; Thông tin chi phí cấp N (Đã từ chối / Đã phê duyệt).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| Phê duyệt 1–6 | FR-cost-catalog-015, FR-cost-catalog-017 | BR-cost-catalog-009, BR-cost-catalog-012, BR-cost-catalog-013, BR-cost-catalog-014, BR-cost-catalog-020 | — | SRS Web tr.608–610 — UC03.10.05 |
| Từ chối 1–5 | FR-cost-catalog-016, FR-cost-catalog-017 | BR-cost-catalog-011, BR-cost-catalog-012, BR-cost-catalog-020 | — | SRS Web tr.604–607 — UC03.10.05 |
| 3a | FR-cost-catalog-018 | BR-cost-catalog-018 | E-cost-catalog-002 | SRS Web tr.606, 609 — UC03.10.05 |

## h. Open Questions

OQ-2 (tự phê duyệt), OQ-5 (giới hạn mã), OQ-12 (xung đột khác), OQ-14 (lý do bắt buộc)
