---
type: shared-environment
status: draft
updated: 2026-10-01
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_shared/system-overview.md
  - docs/design.md
---

# Operating Environment

Môi trường vận hành chung: nền tảng, người dùng, ngôn ngữ và bộ yêu cầu phi chức năng nền mà mọi
feature kế thừa. Nguồn: tài liệu SRS LG (`docs-input/srs-cu/lg-srs-export.md` — NFR mục 6, UC02.03.01).

## Target Platforms

| Kênh | Hỗ trợ | Ghi chú |
|---|---|---|
| Website | Trình duyệt **Chrome**; hệ điều hành Windows, macOS, Linux | Kênh chính. Màn mẫu thiết kế cho desktop 1920×1080 (design.md › Breakpoints) |
| Ứng dụng di động | **iOS** và **Android** | Dùng cho một số nghiệp vụ theo quyền nền tảng Mobile (vd Đơn mua HHDV, Lịch nhắc) |
| Portal đối tác | Website | Riêng cho nhân viên đối tác cây dầu — nghiệp vụ Cấp dầu |

- Tích hợp với phần mềm ERP khác: **Delta ERP**.

## Target Users

- Primary: nhân viên nội bộ Delta — quyền tuỳ theo phân quyền (xem [[docs/_shared/system-overview.md|System Overview]] › Actors).
- Admin: full quyền.
- Secondary: nhân viên đối tác cây dầu (Portal).

## Regions & Languages

- Vận hành tại Việt Nam, dữ liệu tách theo chi nhánh (vd Chi nhánh Hà Nội, Chi nhánh TP.HCM).
- UI languages: **Tiếng Việt (mặc định)**, Tiếng Anh. Đổi ngôn ngữ: Avatar › Ngôn ngữ (UC02.03.01), chọn 1, giao diện tải lại theo ngôn ngữ mới + toast thành công.
- Ghi chú: UC02.03.01 trong nguồn còn liệt kê Tiếng Nhật — đã chốt chỉ Việt + Anh (2026-10-01), UC02.03.01 cần cập nhật theo.

## NFR nền (áp mọi feature)

Feature kế thừa bảng này; `/srs` chỉ ghi NFR **khác** hoặc **chặt hơn** baseline.

| Nhóm | Yêu cầu |
|---|---|
| Hiệu năng | Yêu cầu cơ bản xử lý trong **1 giây**; yêu cầu phức tạp trong **5 giây**. Tối thiểu **200** người dùng đồng thời không giảm hiệu năng |
| Mở rộng | Mở rộng tới **500** người dùng không ảnh hưởng hiệu năng; tăng tài nguyên (CPU, RAM, bộ nhớ) linh hoạt theo nhu cầu |
| Tài nguyên | Dùng CPU, RAM, đĩa hiệu quả; có giám sát tài nguyên theo thời gian thực |
| Bảo mật | Bắt buộc xác thực trước khi truy cập; dữ liệu nhạy cảm mã hoá khi lưu và khi truyền; phân quyền chi tiết theo vai trò |
| Khả dụng | Uptime tối thiểu **99.9%**; sao lưu định kỳ để phục hồi dữ liệu; tự phát hiện sự cố |
| Bảo trì | Kiến trúc dễ mở rộng, bảo trì; triển khai tính năng mới không gián đoạn dịch vụ |
| Khả năng sử dụng | Giao diện dễ dùng, dễ điều hướng; có tài liệu hướng dẫn cho người dùng và quản trị viên |
| Ứng dụng di động | Giao diện tối ưu cho cảm ứng; chạy mượt trên máy cấu hình trung bình; tiết kiệm pin; hỗ trợ **push notification** |
