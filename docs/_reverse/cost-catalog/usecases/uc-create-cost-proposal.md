# UC-create-cost-proposal — Tạo đề xuất tạo mới chi phí cấp 1, 2, 3

## a. Introduction

Tạo đề xuất tạo mới một khoản mục chi phí; bản ghi tạo ra ở trạng thái Chờ phê duyệt. Mã UC gốc: UC03.10.03, UC03.11.03, UC03.12.03. Nhóm cùng khuôn, viết một lần. ✅ [SRS Web tr.591, 625, 657 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3]

## b. Actors & Objects

- Tác nhân: Người dùng phần mềm xưởng ✅ [SRS Web tr.591 — UC03.10.03]
- Đối tượng: Chi phí cấp N, chi phí cấp cha (cấp 2, 3), Thông báo, Lịch sử hoạt động ✅

## c. Pre-conditions

- Đăng nhập; được phân quyền Tạo đề xuất tạo mới của chi phí cấp N ✅ [SRS Web tr.591, 625, 657]
- Đường dẫn: Danh sách chi phí cấp N > Tạo mới > Màn hình Tạo mới ✅
- Cấp 2: có ít nhất 1 chi phí cấp 1 Đã phê duyệt để chọn; cấp 3: ít nhất 1 cấp 2 Đã phê duyệt 🔵 [SRS Web tr.627, 660]

## d. Expected result

- Hệ thống tạo 1 bản ghi trạng thái Chờ phê duyệt ✅
- Toast "Đề xuất tạo mới thành công" ✅
- Hiển thị màn Thông tin chi phí cấp N (xem) với 3 hành động theo phân quyền: Huỷ đề xuất, Phê duyệt, Từ chối ✅ [SRS Web tr.591, 594, 628, 662]

## e. Activity diagram

Xem flows.md — Flow: Tạo đề xuất tạo mới khoản mục chi phí

Main Success Scenario:
1. Hiển thị Danh sách chi phí cấp N ✅ [SRS Web tr.591 — hình lưu đồ UC03.10.03]
2. Người dùng bấm Tạo mới; hệ thống hiển thị popup/form Tạo mới chi phí cấp N ✅
3. Người dùng nhập tên (bắt buộc), tên tiếng Anh, ghi chú; cấp 2: chọn Thuộc chi phí cấp 1 (bắt buộc); cấp 3: chọn Ghi nhận qua PO, Tên dịch vụ, Dịch vụ liên quan phương tiện, Thuộc chi phí cấp 2 ✅ [SRS Web tr.592–593, 626–627, 658–661]
4. Người dùng bấm Tạo mới; hệ thống kiểm tra validate ✅
5. Hợp lệ: toast, lưu bản ghi Chờ phê duyệt ✅
6. Hệ thống tạo bản ghi Lịch sử hoạt động "Đã tạo yêu cầu cấp mới" ✅
7. Hệ thống gửi thông báo "đang chờ phê duyệt" tới người có quyền phê duyệt ✅ [SRS Web tr.594, 580]
8. Hệ thống chuyển sang màn Thông tin chi phí cấp N chế độ xem ✅

Extensions:
- 4a. Trường không hợp lệ: lỗi in-line dưới trường ✅ [SRS Web tr.595]
- 4b. Tên trùng: "Tên chi phí này đã bị trùng." ✅ [SRS Web tr.592, 626, 658]
- 3a. Cấp 3 chọn Không ở "Ghi nhận chi phí qua PO" (mặc định): ẩn Tên dịch vụ và Dịch vụ liên quan phương tiện ✅ [SRS Web tr.659–660]
- 2a. Bấm Huỷ hoặc biểu tượng đóng: hộp thoại "Huỷ tạo mới?"; Xác nhận: không tạo bản ghi, về danh sách; Huỷ: quay lại form với dữ liệu đã nhập ✅ [SRS Web tr.595–596, 629–630, 663–664]

## f. Screens

Tạo mới chi phí cấp 1, 2, 3; popup Huỷ tạo mới; Thông tin chi phí cấp N (Chờ phê duyệt).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 2–3 | FR-cost-catalog-004, FR-cost-catalog-009, FR-cost-catalog-022, FR-cost-catalog-023, FR-cost-catalog-024 | BR-cost-catalog-001, BR-cost-catalog-004 đến BR-cost-catalog-008 | E-cost-catalog-003, E-cost-catalog-004, E-cost-catalog-005 | SRS Web tr.592–596 — UC03.10.03 |
| 4–5 | FR-cost-catalog-010 | BR-cost-catalog-002, BR-cost-catalog-003 | E-cost-catalog-001 | SRS Web tr.594–595 — UC03.10.03 |
| 6–7 | FR-cost-catalog-011 | BR-cost-catalog-019, BR-cost-catalog-024 | — | SRS Web tr.594 — UC03.10.03 |
| 2a | FR-cost-catalog-012 | BR-cost-catalog-025 | — | SRS Web tr.595–596 — UC03.10.03 |

## h. Open Questions

OQ-1 (phạm vi unique), OQ-9 (tên dịch vụ), OQ-10 (giá trị liên quan phương tiện khi PO = Không)
