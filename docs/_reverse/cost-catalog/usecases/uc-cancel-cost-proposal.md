# UC-cancel-cost-proposal — Huỷ đề xuất cấp mới chi phí cấp 1, 2, 3

## a. Introduction

Huỷ đề xuất tạo mới khoản mục đang Chờ phê duyệt. Mã UC gốc: UC03.10.04, UC03.11.04, UC03.12.04. Nhóm cùng khuôn, viết một lần. ✅ [SRS Web tr.598, 632, 666 — UC03.10.04, UC03.11.04, UC03.12.04 Huỷ đề xuất cấp mới chi phí cấp 1, 2, 3]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.598 — UC03.10.04]
- Đối tượng: Chi phí cấp N (trạng thái), Thông báo, Lịch sử hoạt động ✅

## c. Pre-conditions

- Được phân quyền Huỷ đề xuất tạo mới của chi phí cấp N ✅
- Bản ghi ở trạng thái Chờ phê duyệt ✅ [SRS Web tr.598, 632, 666]
- Đường dẫn: nút Huỷ đề xuất ở cột Hành động của danh sách, hoặc trong màn Thông tin (xem) ✅

## d. Expected result

- Trạng thái Chờ phê duyệt → Đã huỷ ✅
- Toast "Huỷ đề xuất tạo chi phí cấp N thành công" ✅
- Tắt popup Xác nhận huỷ, hiển thị màn Thông tin chi phí cấp N với 2 hành động Xoá yêu cầu, Tạo mới yêu cầu ✅ [SRS Web tr.598, 600]

## e. Activity diagram

Xem flows.md — Flow: Huỷ đề xuất tạo mới

Main Success Scenario:
1. Hiển thị màn Thông tin hoặc Danh sách chi phí cấp N ✅ [SRS Web tr.598 — hình lưu đồ UC03.10.04]
2. Người dùng bấm Huỷ đề xuất; hệ thống hiện popup "Huỷ đề xuất tạo mới?" — "Bạn có chắc chắn muốn huỷ đề xuất này không?" ✅ [SRS Web tr.599 — hình mockup]
3. Người dùng bấm Xác nhận ✅
4. Hệ thống đổi trạng thái sang Đã huỷ và hiển thị toast ✅
5. Hệ thống gửi thông báo "[Tên chi phí] đã bị huỷ." tới người có quyền phê duyệt ✅ [SRS Web tr.600, 580]
6. Hệ thống lưu Lịch sử hoạt động "Đã huỷ yêu cầu cấp mới" ✅
7. Hệ thống hiển thị màn Thông tin chi phí cấp N (xem) ✅

Extensions:
- 3a. Bấm Huỷ bỏ: giữ Chờ phê duyệt, đóng popup, về màn Thông tin ✅ [SRS Web tr.601]
- 4a. Người phê duyệt đang ở màn Thông tin bấm Phê duyệt/Từ chối sau khi người khác huỷ: popup lỗi (xem UC phê duyệt/từ chối) ✅ [SRS Web tr.606, 609]

## f. Screens

Popup Huỷ đề xuất tạo mới; Thông tin chi phí cấp N (Đã huỷ).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–4 | FR-cost-catalog-013 | BR-cost-catalog-009, BR-cost-catalog-012, BR-cost-catalog-013 | — | SRS Web tr.598–601 — UC03.10.04 |
| 5–6 | FR-cost-catalog-014 | BR-cost-catalog-019, BR-cost-catalog-024 | — | SRS Web tr.600 — UC03.10.04 |

## h. Open Questions

OQ-11 (người tạo có được báo khi người khác huỷ)
