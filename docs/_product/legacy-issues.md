---
type: issue-register
status: draft
updated: 2026-10-15
links:
  - docs/_product/prd.md
  - docs/_product/srs-v2-change-log.md
  - docs/_shared/definitions.md
---

# Sổ vấn đề hệ thống cũ — cần giải quyết khi cải tiến

> Nguồn: đội ghi nhận ngày 15/10/2026 khi lên kế hoạch reverse SRS cũ (Tài liệu SRS - ERP Delta 3.0 Web + Mobile).
> Mỗi vấn đề phải có quyết định trong brainstorm của feature được gắn. `*` = mọi feature có màn hình.

| Mã | Vấn đề | Module | Feature | Xử lý ở | Trạng thái |
|---|---|---|---|---|---|
| ISS-01 | Chia module theo miền chuẩn (fleet, hrm, crm, inventory, organization, finance…), không dồn mọi thứ vào "danh mục". Danh mục dùng chung đưa lên cấp doanh nghiệp (trên chi nhánh), có trang riêng để quản lý và cấu hình | Cấp sản phẩm | (cấp sản phẩm) | PRD Feature Map + object-map | ⬜ |
| ISS-02 | Tổ chức lại danh mục hàng hoá: sản phẩm (thông tin hàng hoá, thiết bị), fitment (sản phẩm lắp được cho loại phương tiện, tên phương tiện nào), nhóm sản phẩm dạng cây | Danh mục › Hàng hoá | `product-catalog`, `vehicle-management` | brainstorm | ⬜ |
| ISS-03 | Phương tiện đang gộp cả thiết bị không phải xe (máy phát điện, rơ mooc…) — cần tách loại tài sản | Quản lý phương tiện | `vehicle-management` | brainstorm | ⬜ |
| ISS-04 | Danh mục không ngừng dùng hay xoá được (khách tạo sai phải nhờ đội xoá); cân nhắc luồng cập nhật danh mục | Danh mục | `product-catalog`, `partners`, `cost-catalog`, `organization`, `common-workspace` | brainstorm (khuôn chung ở `common-workspace`) | ⬜ |
| ISS-05 | Chứng từ nghiệp vụ chưa có điểm kết thúc rõ. Vd: chẩn đoán → lệnh sửa chữa → xuất kho, làm sai từ chẩn đoán thì không kết thúc được. Cần: đóng lệnh sửa chữa thì phát sinh nhập kho trả lại; chẩn đoán huỷ được để không tạo lại lệnh sửa chữa từ nó | Bảo dưỡng sửa chữa | `repair-quotation`, `repair-order`, `stock-movement`, `common-workspace` | brainstorm (khuôn vòng đời chứng từ ở `common-workspace`) | ⬜ |
| ISS-06 | Chưa có cách cập nhật lệnh sửa chữa đã chốt (liên quan ghi chép đối ứng) | Bảo dưỡng sửa chữa | `repair-order`, `stock-movement`, `workshop-payment` | brainstorm | ⬜ |
| ISS-07 | Thống nhất thuật ngữ dev–BA. Vd: một yêu cầu có 2 loại BusinessDocument (chứng từ nghiệp vụ) và ChangeRequest (yêu cầu thay đổi danh mục) — BA tài liệu hoá | Cấp dự án | (cấp dự án), `common-workspace` | `docs/_shared/definitions.md` | ⬜ |
| ISS-08 | Nhật ký thay đổi (audit trail) cho hàng tồn kho, tồn xưởng | Bảo dưỡng sửa chữa | `inventory-count`, `stock-movement` | brainstorm | ⬜ |
| ISS-09 | Thanh lý rác thải chưa cho tick chọn để đưa thẳng vào thanh lý | Bảo dưỡng sửa chữa | `inventory-count` | brainstorm | ⬜ |
| ISS-10 | Ký điện tử (biên bản bàn giao, thu hồi và chứng từ cần ký) | Quản lý phương tiện, Nền tảng | `vehicle-management`, `common-workspace` | brainstorm | ⬜ |
| ISS-11 | Lái xe xem và kiểm tra thông tin trên app để tiến hành bàn giao, thu hồi | Quản lý phương tiện | `vehicle-management` | brainstorm | ⬜ |
| ISS-12 | Báo cáo đang làm cố định — cần lọc, cấu hình được | Bảo dưỡng sửa chữa, Quản lý dầu, Nền tảng | `workshop-reports`, `fuel-stations`, `common-workspace` | brainstorm | ⬜ |
| ISS-13 | Đăng nhập bằng SSO thay cách đăng nhập hiện tại | Nền tảng | `account-access` | brainstorm | ⬜ |
| ISS-14 | Giao diện làm lại theo design system mới | Mọi module | `*` | `/figma-screen` | ⬜ |
| ISS-15 | Onboarding trực tiếp hoặc hướng dẫn sử dụng gắn với từng chức năng (trừ feature đơn giản) | Mọi module, Nền tảng | `*`, `help-center` | brainstorm (đánh dấu feature đơn giản) + `/userguide` | ⬜ |
