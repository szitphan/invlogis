# UC-view-cost-detail — Xem thông tin chi phí cấp 1, 2, 3

## a. Introduction

Xem thông tin chi tiết một khoản mục chi phí. Mã UC gốc: UC03.10.02, UC03.11.02, UC03.12.02. Nhóm cùng khuôn, viết một lần. ✅ [SRS Web tr.585, 618, 652 — UC03.10.02, UC03.11.02, UC03.12.02 Xem thông tin chi phí cấp 1, 2, 3]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.585 — UC03.10.02]
- Đối tượng: Chi phí cấp N, danh sách chi phí cấp N+1 (tab con), Lịch sử hoạt động ✅

## c. Pre-conditions

- Đăng nhập; được phân quyền Xem của Danh mục - Chi phí cấp N ✅ [SRS Web tr.585, 618, 652]
- Đường dẫn: từ Danh sách chi phí cấp N nhấn một bản ghi ✅

## d. Expected result

Hiển thị thông tin chi tiết của chi phí cấp N ✅ [SRS Web tr.585, 618, 652 — UC03.10.02, UC03.11.02, UC03.12.02]

## e. Activity diagram

Xem flows.md — Flow: Xem thông tin khoản mục chi phí

Main Success Scenario:
1. Hệ thống hiển thị Danh sách chi phí cấp N ✅ [SRS Web tr.585 — hình lưu đồ UC03.10.02]
2. Người dùng chọn 1 bản ghi ✅
3. Hệ thống hiển thị màn Thông tin chi phí cấp N: tên, mã (nếu có), trạng thái, tên tiếng Anh, thuộc cấp cha (cấp 2, 3), ghi chú (ẩn nếu rỗng), các trường PO (cấp 3) ✅ [SRS Web tr.587, 620, 653–654]
4. Với cấp 1, 2: tab Chi phí cấp N+1 liệt kê khoản mục con đã phê duyệt, có tìm, nhóm, lọc, Export, phân trang ✅ [SRS Web tr.588, 621–622]

Extensions:
- 2a. Cấp 2, 3 mở từ tab con trong chi tiết cấp cha (lưu đồ cấp 2, 3) ✅ [SRS Web tr.618, 652 — hình lưu đồ]
- 3a. Trạng thái Chờ phê duyệt: nút Phê duyệt, Từ chối, Huỷ đề xuất (theo quyền) ✅ [SRS Web tr.597, 631, 665]
- 3b. Trạng thái Đã huỷ / Đã từ chối: biểu tượng "…" với Xoá yêu cầu, Tạo mới yêu cầu ✅ [SRS Web tr.589–590, 623–624, 655–656]
- 3c. Trạng thái Đã phê duyệt: không thêm hành động; ảnh hiện dòng ID ✅ [SRS Web tr.610, 644, 678]
- 3d. Nhấn hyperlink "Thuộc chi phí cấp 1/2": mở tắt sang chi tiết khoản mục cha ✅ [SRS Web tr.620, 654]
- 3e. Nhấn Lịch sử hoạt động: popup lịch sử ✅ [SRS Web tr.590, 624, 656]
- 3f. Nhấn biểu tượng đóng: về Danh sách chi phí cấp N ✅ [SRS Web tr.590, 624, 656]

## f. Screens

Thông tin chi phí cấp 1; Thông tin chi phí cấp 2; Thông tin chi phí cấp 3; popup Lịch sử hoạt động.

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 1–3 | FR-cost-catalog-005 | BR-cost-catalog-015, BR-cost-catalog-017 | — | SRS Web tr.585–587 — UC03.10.02 |
| 4 | FR-cost-catalog-006 | BR-cost-catalog-016 | — | SRS Web tr.588 — UC03.10.02 |
| 3d | FR-cost-catalog-007 | — | — | SRS Web tr.620 — UC03.11.02 |
| 3e | FR-cost-catalog-008 | BR-cost-catalog-024 | — | SRS Web tr.590 — UC03.10.02 |
| 3a–3c | FR-cost-catalog-021 | BR-cost-catalog-022 | — | SRS Web tr.284, 589–590 |

## h. Open Questions

Không có
