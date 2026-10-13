# Use Case: Tra cứu quy trình trên danh sách

> Scope: Liên quy trình — màn danh sách Quy trình (Website) · Level: sea

## Primary Actor

Người theo dõi quy trình (Nhân viên nội bộ Delta, Website).

## Trigger

Người dùng vào menu {Module} › Quy trình.

## Preconditions

- Người dùng có quyền xem menu Quy trình của module (Admin cấp theo FR-cross-process-flow-019).

## Guarantees

- **Minimal Guarantee:** Danh sách chỉ hiện quy trình thuộc module + chi nhánh người dùng được phân quyền dữ liệu; lỗi tải không làm mất bộ lọc đang chọn.
- **Success Guarantee:** Người dùng tìm ra quy trình cần theo dõi và mở được sơ đồ của nó (hoặc xuất được đúng danh sách đang thấy).

## Main Success Scenario

1. Hệ thống hiện danh sách Quy trình của module, chỉ gồm quy trình thuộc chi nhánh người dùng được phân quyền dữ liệu, 10 cột, sắp theo Cập nhật lần cuối mới nhất; cột Bước đang chờ hiện bước chờ lâu nhất + "+n bước khác" (FR-cross-process-flow-015). Đang tải: skeleton theo 10 cột (GR-12). Luồng liên module hiện ở cả 2 module.
2. Người dùng gõ mã của bất kỳ bản ghi nào trong cây (mã yêu cầu, mã bản ghi, hoặc mã quy trình) vào ô tìm.
3. Hệ thống tìm khi ô có từ 3 ký tự, mã chứa chuỗi đã gõ ở bất kỳ vị trí nào, không phân biệt hoa thường, sau khi ngừng gõ 0,3 giây (FR-cross-process-flow-016). Theo GR-09.
4. Người dùng lọc thêm theo Luồng, Trạng thái, Chi nhánh, khoảng ngày Cập nhật lần cuối (FR-cross-process-flow-017). Xem CMP-05 — Filter Drawer.
5. Hệ thống hiện kết quả sau lọc.
6. Người dùng bấm một dòng.
7. Hệ thống mở popup sơ đồ ngay trên danh sách, chưa chọn bước nào (FR-cross-process-flow-018). Từ đây tiếp như uc-xem-quy-trinh-cua-ban-ghi bước 5–8.

## Extensions

**1a. Chưa có quy trình nào:**
- 1a1. Hệ thống hiện "Chưa có quy trình nào. Quy trình tự tạo khi có bản ghi đầu tiên được gửi." (Theo GR-12, không có nút Tạo mới). Use case kết thúc.

**1b. Lỗi tải danh sách:**
- 1b1. Hệ thống thay vùng bảng bằng khối "Không tải được danh sách." + Thử lại, giữ thanh công cụ và bộ lọc (Override GR-15). Người dùng bấm Thử lại → quay lại bước 1.

**1c. Người dùng mở thẳng đường dẫn danh sách khi không có quyền menu Quy trình:**
- 1c1. Vùng nội dung hiện câu E-common-011 + nút Về trang chủ (FR-cross-process-flow-019). Use case kết thúc.

**3a. Ô tìm dưới 3 ký tự:**
- 3a1. Hệ thống chưa tìm, không báo lỗi. Quay lại bước 2.

**5a. Không có kết quả:**
- 5a1. Có từ khoá: hệ thống hiện "Không tìm thấy quy trình chứa mã "[mã]"." + Xoá bộ lọc. Ô tìm trống: "Không có quy trình phù hợp với bộ lọc." + Xoá bộ lọc (FR-cross-process-flow-017).
- 5a2. Người dùng bấm Xoá bộ lọc → quay lại bước 1.

**5b. Thông tin đang hiện trên danh sách đổi trong khi đang mở:**
- 5b1. Hệ thống hiện banner Theo GR-27 "Danh sách vừa có cập nhật." + Tải lại; tải lại giữ bộ lọc (FR-cross-process-flow-020). Tiếp bước 5.

**5c. Người dùng muốn xuất danh sách:**
- 5c1. Người dùng bấm Xuất, chọn PDF hoặc Excel; hệ thống xuất đúng tập dữ liệu đang thấy (sau tìm, lọc, sắp, gồm mọi trang) và các cột đang hiện, theo quy định xuất danh sách chung (FR-cross-process-flow-022, Theo GR-19). Use case kết thúc.

**6a. Người dùng bấm ô Phương tiện / khách hàng:**
- 6a1. Hệ thống mở màn chi tiết Phương tiện hoặc Xe của khách hàng (FR-cross-process-flow-018). Use case kết thúc.

## Related Requirements

FR-cross-process-flow-015 → 020, FR-cross-process-flow-022 · BR-cross-process-flow-002 (cột Bước đang chờ), BR-cross-process-flow-012 (tìm theo mã yêu cầu) · NFR-cross-process-flow-009 — [[docs/cross-process-flow/srs/cross-process-flow-spec.md|SRS spec]]
