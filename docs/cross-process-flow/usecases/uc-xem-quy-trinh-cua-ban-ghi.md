# Use Case: Xem quy trình của một bản ghi

> Scope: Liên quy trình (dùng chung mọi module) · Level: sea

## Primary Actor

Người theo dõi quy trình (Nhân viên nội bộ Delta, Website hoặc Delta Super App). Lái xe dùng cùng use case trên Delta Super App, quyền xem theo FR-cross-process-flow-009.

## Stakeholders & Interests

| Stakeholder | Interest |
|-------------|----------|
| Kế toán thanh toán | Biết các bước trước (xuất kho, chốt lệnh, công nợ) đã xong chưa trước khi thanh toán |
| Quản lý xưởng | Thấy bước đang kẹt của một lệnh sửa chữa mà không mở từng phiếu |

## Trigger

Người dùng mở màn chi tiết của một bản ghi nghiệp vụ.

## Preconditions

- Người dùng đã đăng nhập và có quyền xem bản ghi đang mở.

## Guarantees

- **Minimal Guarantee:** Màn chi tiết bản ghi vẫn dùng được kể cả khi không tải được quy trình; không hiện lịch sử hay nút mở của bước người dùng không có quyền xem.
- **Success Guarantee:** Người dùng thấy toàn bộ cây quy trình với trạng thái mới nhất của từng bước, và đã đến được màn chi tiết (hoặc bảng công nợ) của bước mình chọn.

## Main Success Scenario

1. Người dùng mở màn chi tiết bản ghi.
2. Hệ thống hiện dòng quy trình (web: đầu màn · mobile: thẻ quy trình): tên luồng, thanh tiến độ, "Xong x/y bước · n nhánh phát sinh", "Bước trước: …" hoặc "Phát sinh từ: …" (FR-cross-process-flow-005). Đang tải: skeleton (web cao bằng dòng thật · app thẻ có shimmer).
3. Người dùng bấm dòng quy trình.
4. Hệ thống mở sơ đồ (web: popup · mobile: sheet), vừa khung, chọn sẵn bước "Ở đây"; web mở panel của bước đó, app chỉ đánh dấu bước, không tự mở sheet bước (FR-cross-process-flow-006, -007).
5. Người dùng thu phóng (web: zoom, nút vừa khung · app: chụm hai ngón), kéo và chọn một bước khác.
6. Hệ thống hiện panel bước: đầu panel (tên, mã, trạng thái, nhãn), 5 dòng lịch sử hoạt động mới nhất và nút "Mở màn hình chi tiết" (FR-cross-process-flow-008). Mã là mã yêu cầu khi bản ghi chưa được duyệt, mã bản ghi khi đã duyệt (BR-cross-process-flow-012). Xem CMP-09 — Cross Process Flow (Liên quy trình), Xem CMP-08 — Activity Log.
7. Người dùng bấm "Mở màn hình chi tiết".
8. Hệ thống mở màn chi tiết bản ghi của bước (web: cùng tab, đóng popup · mobile: đẩy màn mới) (FR-cross-process-flow-010).

## Extensions

**2a. Bản ghi không thuộc quy trình, hoặc là luồng độc lập chưa có nhánh:**
- 2a1. Hệ thống không hiện dòng quy trình. Use case kết thúc.

**2b. Không tải được dòng quy trình:**
- 2b1. Hệ thống hiện "Không tải được quy trình." + Thử lại; màn chi tiết vẫn dùng bình thường.
- 2b2. Người dùng bấm Thử lại → quay lại bước 2.

**4a. Lỗi tải sơ đồ hoặc mất mạng:**
- 4a1. Hệ thống hiện "Không tải được sơ đồ." kèm câu E-common-008 (lỗi hệ thống) hoặc E-common-009 (mất mạng) và nút Thử lại trong popup/sheet (Override GR-15).
- 4a2. Người dùng bấm Thử lại → quay lại bước 4.

**5a. Trong khi sơ đồ đang mở, thông tin đang hiện trên sơ đồ đổi ở nơi khác:**
- 5a1. Hệ thống hiện banner Theo GR-27 "Quy trình vừa có cập nhật." + Tải lại (FR-cross-process-flow-020).
- 5a2. Người dùng bấm Tải lại → hệ thống tải lại cây, giữ bước đang chọn nếu còn → tiếp bước 5.

**6a. Bước là ngã rẽ chưa chốt:**
- 6a1. Panel ghi "Chưa xác định …" và liệt kê các hướng có thể đi; không có nút mở. Quay lại bước 5.

**6b. Bước chưa có bản ghi:**
- 6b1. Panel ghi "Chưa có hoạt động. Bước này chưa được tạo."; không có nút mở. Quay lại bước 5.

**6c. Người dùng không có quyền xem bản ghi của bước:**
- 6c1. Panel chỉ hiện đầu panel (tên, mã, trạng thái, lý do phát sinh nếu có), ẩn lịch sử và nút, hiện câu E-common-011 tại chỗ (Override GR-26). Quyền tính theo phân quyền xem của nghiệp vụ ứng với bước đó, như nhau cho mọi người dùng kể cả Lái xe (FR-cross-process-flow-009). Quay lại bước 5.

**6d. Bước là thanh toán trả sau:**
- 6d1. Panel ghi "Công nợ {Tên NCC}", nút "Mở bảng công nợ" thay cho "Mở màn hình chi tiết".
- 6d2. Người dùng bấm → hệ thống mở bảng công nợ đã lọc theo nhà cung cấp và khoảng thời gian của bảng công nợ (FR-cross-process-flow-011). Use case kết thúc.
- 6d3. Trên app: sheet bước chỉ hiện trạng thái, không có nút mở — Delta Super App không có màn Bảng công nợ (userflow OQ-2). Use case kết thúc.

**6e. Không tải được lịch sử:**
- 6e1. Khối lịch sử hiện "Không tải được lịch sử." + Thử lại; đầu panel và nút mở vẫn dùng được (FR-cross-process-flow-008). Lịch sử rỗng: "Chưa có hoạt động."

**6f. Bước có bản ghi Đã thay thế:**
- 6f1. Thẻ bước hiện bản ghi hiện hành kèm "+n bản ghi trước"; panel thêm khối "Bản ghi trước đó", mỗi bản ghi 1 dòng: mã · Đã thay thế · ngày bị từ chối/thu hồi · Mở (theo quyền) (FR-cross-process-flow-008, BR-cross-process-flow-011). Tiếp bước 7.

**6g. Trên app, loại bản ghi của bước không có màn chi tiết trên app:**
- 6g1. Sheet bước không có nút mở (FR-cross-process-flow-009). Quay lại bước 5.

**8a. Bản ghi vừa bị thu quyền xem:**
- 8a1. Web: hệ thống hiện popup Loại 2 (GR-15) câu E-common-011 + Đóng · app: popup chặn E-common-011 Theo GR-26; người dùng ở lại sơ đồ. Quay lại bước 5.

**8b. Bản ghi đã bị xoá trong lúc sơ đồ đang mở:**
- 8b1. Hệ thống hiện popup E-cross-process-flow-004 + Tải lại sơ đồ (FR-cross-process-flow-010).
- 8b2. Người dùng bấm Tải lại sơ đồ → cây tải lại theo trạng thái mới (bước chính thành "Chưa tạo", nhánh phát sinh thành Đã huỷ). Quay lại bước 5.

## Related Requirements

FR-cross-process-flow-005 → 011, FR-cross-process-flow-020, FR-cross-process-flow-021 · BR-cross-process-flow-005, BR-cross-process-flow-006, BR-cross-process-flow-009, BR-cross-process-flow-011, BR-cross-process-flow-012 · E-cross-process-flow-004 · NFR-cross-process-flow-001, -002, -004, -005 — [[docs/cross-process-flow/srs/cross-process-flow-spec.md|SRS spec]]
