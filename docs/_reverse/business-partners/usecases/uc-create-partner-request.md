# UC-create-partner-request — Tạo đề xuất tạo mới nhà cung cấp HHDV / khách hàng DK05 / xe của khách hàng

## a. Introduction

Người dùng nhập form và gửi đề xuất tạo mới; bản ghi vào ở trạng thái Chờ phê duyệt. Mã UC gốc: UC03.07.03, UC03.08.03, UC03.09.03. Một khuôn cho cả ba; trường riêng từng danh mục xem spec bảng Khác biệt. ✅ [SRS Web tr.474 — UC03.07.03 Tạo đề xuất tạo mới nhà cung cấp HHDV; SRS Web tr.517 — UC03.08.03 Tạo đề xuất tạo mới khách hàng DK05; SRS Web tr.554 — UC03.09.03 Tạo đề xuất tạo mới xe của khách hàng]

## b. Actors & Objects

Người dùng phần mềm xưởng (có quyền Tạo đề xuất tạo mới của danh mục); hệ thống PMX; người có quyền phê duyệt (nhận thông báo). ✅ [SRS Web tr.474 — UC03.07.03; SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động]

## c. Pre-conditions

Đã đăng nhập; được phân quyền Tạo đề xuất tạo mới của danh mục. ✅ [SRS Web tr.474 — UC03.07.03]

## d. Expected result

Hệ thống tạo 1 bản ghi ở trạng thái Chờ phê duyệt; hiển thị toast "Đề xuất tạo mới thành công"; hiển thị màn Thông tin (Xem) với 3 hành động tuỳ phân quyền (Huỷ đề xuất, Phê duyệt, Từ chối); gửi thông báo và ghi Lịch sử hoạt động. ✅ [SRS Web tr.474 — UC03.07.03; SRS Web tr.484 — UC03.07.03]

## e. Activity diagram

Xem flows.md — Flow: Tạo đề xuất tạo mới.

Main Success Scenario:
1. Hệ thống hiển thị màn Danh sách. ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03]
2. Người dùng nhấn nút Tạo mới. ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03]
3. Hệ thống hiển thị form Tạo mới. ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03]
4. Người dùng nhập thông tin và nhấn Tạo mới. ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03]
5. Hệ thống kiểm tra validate: tất cả hợp lệ. ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03; SRS Web tr.484 — UC03.07.03]
6. Hệ thống báo toast, lưu bản ghi Chờ phê duyệt. ✅ [SRS Web tr.484 — UC03.07.03]
7. Hệ thống gửi thông báo tới người có quyền phê duyệt. ✅ [SRS Web tr.484 — UC03.07.03]
8. Hệ thống tạo dòng Lịch sử hoạt động "Đã tạo yêu cầu cấp mới". ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03; SRS Web tr.485 — UC03.07.03]
9. Hệ thống chuyển sang màn Thông tin (view mode). ✅ [SRS Web tr.474 — hình lưu đồ UC03.07.03]

Extensions:
- 5a. Có trường không hợp lệ: lỗi in-line dưới trường (trùng tên/biển số, quá độ dài, file quá dung lượng/sai định dạng...), không tạo bản ghi. ✅ [SRS Web tr.485 — UC03.07.03; SRS Web tr.475 — UC03.07.03; SRS Web tr.481 — UC03.07.03]
- 4a. Người dùng nhấn Huỷ hoặc icon X: popup "Huỷ tạo mới?"; Xác nhận thì không tạo bản ghi, về Danh sách; Huỷ thì về form giữ dữ liệu. ✅ [SRS Web tr.485 — UC03.07.03; SRS Web tr.486 — UC03.07.03]
- 4b. NCC chọn Thanh toán trả sau: hiện thêm 3 trường bắt buộc. ✅ [SRS Web tr.482 — UC03.07.03]
- 4c. KH chọn Loại khách hàng: hiện CCCD/CMT (cá nhân) hoặc Người đại diện (doanh nghiệp). ✅ [SRS Web tr.522 — UC03.08.03; SRS Web tr.523 — UC03.08.03]
- 4d. Xe chọn Loại phương tiện: danh sách Mã phương tiện - Tên phương tiện lọc theo loại. ✅ [SRS Web tr.556 — UC03.09.03]
- 2a. Từ menu "…" Tạo mới yêu cầu: form nhận dữ liệu từ yêu cầu đã huỷ/từ chối (uc-delete-or-recreate-closed-request). ✅ [SRS Web tr.492 — UC03.07.04]

## f. Screens

Tạo mới nhà cung cấp HHDV; Tạo mới khách hàng DK05; Tạo mới xe của khách hàng; popup Huỷ tạo mới; màn Thông tin (Chờ phê duyệt).

## g. Related FR

| Bước | FR | BR | Error | Nguồn |
|---|---|---|---|---|
| 2–5 | FR-business-partners-019 | BR-business-partners-009..016, BR-business-partners-026..029, BR-business-partners-037, BR-business-partners-038 | E-business-partners-001..007 | SRS Web tr.475 — UC03.07.03; SRS Web tr.518 — UC03.08.03; SRS Web tr.556 — UC03.09.03 |
| 5a | FR-business-partners-021 | — | E-business-partners-010 | SRS Web tr.485 — UC03.07.03 |
| 6–9 | FR-business-partners-020, FR-business-partners-032, FR-business-partners-036, FR-business-partners-037 | BR-business-partners-001, BR-business-partners-032 | — | SRS Web tr.484 — UC03.07.03; SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động |
| 4a | FR-business-partners-022 | BR-business-partners-033 | — | SRS Web tr.485 — UC03.07.03; SRS Web tr.486 — UC03.07.03 |
| 4b | FR-business-partners-041 | BR-business-partners-018..021 | — | SRS Web tr.482 — UC03.07.03; SRS Web tr.483 — UC03.07.03 |
| 4 chứng từ | FR-business-partners-042 | BR-business-partners-017 | E-business-partners-006, E-business-partners-007 | SRS Web tr.481 — UC03.07.03 |
| 4c | FR-business-partners-043 | BR-business-partners-026 | — | SRS Web tr.522 — UC03.08.03 |
| 4d | FR-business-partners-044 | BR-business-partners-027, BR-business-partners-028 | — | SRS Web tr.555 — UC03.09.03; SRS Web tr.556 — UC03.09.03 |

## h. Open Questions

OQ-4, OQ-5, OQ-6, OQ-9, OQ-13 (xem gaps.md).
