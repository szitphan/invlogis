# Use Case: Tạo nghiệp vụ tiếp theo từ một bản ghi

> Scope: Liên quy trình (dùng chung mọi module) · Level: sea

## Primary Actor

Người tạo bản ghi (Nhân viên nội bộ Delta, Website; Delta Super App ở nghiệp vụ có màn trên app — cột "Có trên app" của bảng liên quy trình, BR-cross-process-flow-007).

## Trigger

Người tạo bản ghi bấm nút tạo bước tiếp theo (vd "Tạo phiếu xuất kho") ở vùng hành động đầu màn chi tiết của bản ghi trước.

## Preconditions

- Bản ghi trước đã đạt hành động trigger theo bảng liên quy trình của nghiệp vụ (vd Phê duyệt báo giá, Chốt lệnh sửa chữa).
- Người tạo bản ghi có quyền tạo bản ghi của bước tiếp theo (D6).

## Guarantees

- **Minimal Guarantee:** Không có bước mới nào trên cây khi bản ghi chưa gửi thành công; bản nháp không bị tự xoá khi gửi bị chặn.
- **Success Guarantee:** Bản ghi mới ở trạng thái gửi thành công, cây có thêm Bước ở trạng thái Đang triển khai nối về bản ghi trước, trạng thái Quy trình được tính lại.

## Main Success Scenario

1. Hệ thống hiện nút tạo bước tiếp theo ở vùng hành động đầu trang khi bản ghi trước đạt trigger và người xem có quyền tạo (FR-cross-process-flow-012).
2. Người tạo bản ghi bấm nút.
3. Hệ thống mở form tạo mới của nghiệp vụ tiếp theo, đã điền sẵn thông tin mang từ bản ghi trước (theo bảng liên quy trình của nghiệp vụ).
4. Người tạo bản ghi bổ sung thông tin và gửi.
5. Hệ thống ghi nhận bản ghi mới và thêm Bước vào cây nối về bản ghi trước — cùng thành công hoặc cùng không — rồi tính lại trạng thái Quy trình (FR-cross-process-flow-003; chi tiết ở uc-cap-nhat-quy-trinh-theo-ban-ghi).
6. Hệ thống đưa người tạo vào màn chi tiết bản ghi mới; dòng quy trình gắn "Ở đây" cho bước mới. Thông báo thành công theo toast của nghiệp vụ được tạo.

## Extensions

**1a. Bản ghi trước chưa đạt trigger, hoặc người xem không có quyền tạo:**
- 1a1. Hệ thống không hiện nút. Use case kết thúc.

**4a. Người tạo bản ghi lưu nháp thay vì gửi:**
- 4a1. Hệ thống lưu nháp riêng tư; cây không thay đổi. Use case kết thúc với Minimal Guarantee.

**5a. Bước khai "1 bản ghi" đã có bản ghi khác đang chờ phê duyệt hoặc đã xong (có người tạo trước):**
- 5a1. Hệ thống chặn bằng E-cross-process-flow-001 — câu "đang chờ phê duyệt" hoặc "đã hoàn thành với [mã]" (web: popup GR-15 Loại 2 · app: sheet lỗi Loại 2), giữ nguyên form và bản nháp. Hai người cùng gửi thì chỉ người gửi trước được nhận.
- 5a2. Người tạo đóng popup; tải lại màn bản ghi trước thì nút ẩn theo điều kiện của nghiệp vụ. Use case kết thúc với Minimal Guarantee.

**5b. Bước khai "nhiều bản ghi" (vd Xuất kho) đã có bản ghi khác:**
- 5b1. Hệ thống không chặn; bản ghi mới thành bước anh em cùng tên, phân biệt bằng mã (BR-cross-process-flow-008). Tiếp bước 6.

**5c. Bước khai "1 bản ghi" đang có bản ghi Đã thu hồi/từ chối:**
- 5c1. Hệ thống không chặn; bản ghi mới thay thế bản cũ, bản cũ mang nhãn Đã thay thế (BR-cross-process-flow-011). Tiếp bước 6.

**5d. Bản ghi trước vừa bị thu hồi trong lúc gửi:**
- 5d1. Thu hồi thắng: hệ thống chặn bằng popup E-cross-process-flow-003 (web: GR-15 Loại 2 · app: sheet lỗi Loại 2), bản ghi không được ghi nhận gửi.
- 5d2. Người tạo bấm Giữ bản nháp (nút chính) → đóng popup, bản nháp giữ lại; hoặc bấm Xoá bản nháp → xác nhận Xem CMP-03 rồi xoá. Use case kết thúc với Minimal Guarantee.

**5e. Gửi thất bại do lỗi hệ thống, mất mạng, hoặc cây không nhận bước:**
- 5e1. Bản ghi không được ghi nhận gửi; hệ thống hiện toast E-common-008 / E-common-009, giữ nguyên form. Quay lại bước 4.

## Related Requirements

FR-cross-process-flow-003, FR-cross-process-flow-012, FR-cross-process-flow-013 · BR-cross-process-flow-001, BR-cross-process-flow-007, BR-cross-process-flow-008, BR-cross-process-flow-011 · E-cross-process-flow-001, -003 — [[docs/cross-process-flow/srs/cross-process-flow-spec.md|SRS spec]]
