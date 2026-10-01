---
type: shared-definitions
status: draft
updated: 2026-10-01
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_shared/system-overview.md
---

# Definitions

Thuật ngữ nghiệp vụ dùng chung toàn dự án. Nguồn: tài liệu SRS LG (`docs-input/srs-cu/lg-srs-export.md`).
Tổ chức dữ liệu Công ty → Chi nhánh → Cơ sở xem [[docs/_shared/system-overview.md|System Overview]] › Tổ chức dữ liệu.

## Glossary

### Chi nhánh
Đơn vị vận hành độc lập về dữ liệu: cùng bộ chức năng nhưng dữ liệu tách hẳn. Người ở chi nhánh A không thấy dữ liệu chi nhánh B dù cùng quyền.
**Appears in:** mọi module
**Aliases:** —

### Cơ sở
Đơn vị vật lý trực thuộc 1 chi nhánh, chỉ có ở module tổ chức theo cơ sở (Xưởng, Cây dầu). Dữ liệu quản lý riêng theo từng cơ sở. Module nào chia cơ sở là cố định theo nghiệp vụ, không cấu hình.
**Appears in:** Xưởng, Cây dầu, Home
**Aliases:** —

### Ngoài cơ sở
Cơ sở đặc biệt hệ thống tạo sẵn cho mỗi chi nhánh, gán tự động cho nghiệp vụ phát sinh ngoài mọi cơ sở nội bộ (vd cấp dầu tại cây dầu mua ngoài của đối tác, hoá đơn lẻ). Không tạo/sửa/xoá được; cần phân quyền riêng mới thấy.
**Appears in:** Cây dầu (Cấp dầu, Thanh toán trả sau)
**Aliases:** —

### Tất cả cơ sở
Chế độ xem tổng hợp mọi cơ sở trong chi nhánh mà người dùng được phân quyền (gồm cả "Ngoài cơ sở"). Danh sách có thêm cột Cơ sở; Tạo mới ở chế độ này phải chọn 1 cơ sở trước.
**Appears in:** Xưởng, Cây dầu
**Aliases:** view tổng hợp

### Xưởng
Cơ sở sửa chữa của Delta (xưởng nhà). Phân biệt với **xưởng ngoài** — xưởng của nhà cung cấp HHDV mà Delta thuê sửa.
**Appears in:** Sửa chữa, Báo giá, Kho, Hàng tồn xưởng
**Aliases:** xưởng nhà, xưởng Delta (= Xưởng); xưởng đối tác của Delta (= xưởng ngoài)

### Cây dầu
Điểm cấp nhiên liệu. **Cây dầu nội bộ** là cây dầu của Delta, được quản lý như 1 cơ sở (có sensor đo mức dầu, barem, dung tích, ngưỡng). Cây dầu mua ngoài của đối tác thì nghiệp vụ gắn vào "Ngoài cơ sở".
**Appears in:** Cây dầu (Mua dầu, Nhập dầu, Cấp dầu, Dashboard), Danh mục
**Aliases:** —

### HHDV (Hàng hoá dịch vụ)
Gọi chung hàng hoá và dịch vụ Delta mua vào hoặc bán ra. Xuất hiện trong tên Đơn mua HHDV, Nhà cung cấp HHDV, Thanh toán bán HHDV.
**Appears in:** Mua hàng, Thanh toán, Danh mục
**Aliases:** hàng hoá dịch vụ

### PTVT (Phụ tùng vật tư)
Danh mục phụ tùng và vật tư dùng cho sửa chữa phương tiện, tách riêng với Lốp và Ắc quy. Trong báo giá "PTVT còn lại" là phụ tùng không thuộc Lốp/Ắc quy.
**Appears in:** Danh mục, Báo giá, Kho, Sửa chữa
**Aliases:** phụ tùng vật tư

### CCDC (Công cụ dụng cụ)
Danh mục công cụ, dụng cụ của xưởng; xuất kho riêng bằng mục đích "Xuất CCDC".
**Appears in:** Danh mục, Kho, Thanh lý
**Aliases:** công cụ dụng cụ

### DVKT (Dịch vụ kỹ thuật)
Danh mục dịch vụ sửa chữa/kỹ thuật được chuẩn hoá (có mã riêng theo loại phương tiện), dùng khi lập báo giá và lệnh sửa chữa.
**Appears in:** Danh mục, Báo giá, Sửa chữa
**Aliases:** dịch vụ kỹ thuật

### Chi phí cấp 1 / Chi phí cấp 2
Danh mục phân loại chi phí 2 tầng: chi phí cấp 2 thuộc 1 chi phí cấp 1.
**Appears in:** Danh mục, Thanh toán
**Aliases:** —

### Phụ tùng hỏng
Phụ tùng thay ra từ phương tiện, đưa vào xưởng để phục hồi. Phục hồi thành công thì nhập kho lại; thất bại thì chuyển sang rác thải chờ thanh lý.
**Appears in:** Sửa chữa, Kho, Thanh lý
**Aliases:** PT hỏng (tránh — "PT" trùng với phương tiện)

### Nhà cung cấp HHDV
Đơn vị bán hàng hoá/dịch vụ cho Delta, gồm cả xưởng ngoài. Có phương thức thanh toán trả trước hoặc trả sau.
**Appears in:** Danh mục, Mua hàng, Thanh toán
**Aliases:** NCC

### Khách hàng DK05
Khách hàng đã đăng ký trong danh mục (pháp nhân hoặc cá nhân, có MST/CCCD), mua phụ tùng hoặc dịch vụ sửa chữa của Delta; có phương thức thanh toán trả trước hoặc trả sau. Phân biệt với **khách hàng lẻ** — không có trong danh mục, luôn thanh toán trả trước.
**Appears in:** Danh mục, Báo giá, Sửa chữa, Thanh toán
**Aliases:** —

### Phương tiện
Xe của Delta (đầu kéo, xe tải, sơ mi-rơ mooc…) hoặc xe của khách hàng mang tới sửa. Hiển thị dạng "[Mã PT] - [Tên PT]".
**Appears in:** Quản lý phương tiện, Sửa chữa, Báo cáo sự cố, Cấp dầu
**Aliases:** PT, xe (viết "PT" chỉ dùng cho phương tiện, không dùng cho phụ tùng)

### Phân luồng
Trường hợp nghiệp vụ của 1 chứng từ, quyết định các bước và trường hiển thị. Vd báo giá: Sửa xe / Bán phụ tùng; lệnh sửa chữa: Sửa chữa xe / Phục hồi phụ tùng hỏng; đơn mua HHDV: Mua hàng hoá / Mua dịch vụ / Mua dịch vụ có phương tiện / Mua dịch vụ sửa chữa ngoài / Mua dịch vụ sửa chữa phụ tùng hỏng ở xưởng ngoài.
**Appears in:** Báo giá, Sửa chữa, Mua hàng, Thanh toán
**Aliases:** luồng, trường hợp

### Báo cáo sự cố
Báo hỏng hóc phương tiện do lái xe gửi từ App Lái xe; xưởng xác nhận hoặc từ chối, rồi lập báo giá chẩn đoán.
**Appears in:** Sửa chữa
**Aliases:** yêu cầu sửa chữa (từ lái xe)

### Báo giá
Chứng từ báo chi phí sửa chữa/bán phụ tùng trước khi làm. **Báo giá chẩn đoán** là báo giá lập sau khi xác nhận báo cáo sự cố, xác định nơi sửa (xưởng nhà / xưởng ngoài).
**Appears in:** Sửa chữa, Mua hàng, Thanh toán
**Aliases:** —

### Lệnh sửa chữa
Chứng từ thực hiện sửa chữa sau khi báo giá được duyệt. Loại: sửa chữa xe Delta/khách hàng, thay lốp, thay ắc quy, phục hồi phụ tùng hỏng. **Chốt lệnh** = ghi nhận số lượng thực dùng/hỏng/thừa và giờ công khi kết thúc.
**Appears in:** Sửa chữa, Kho, Thanh toán, Bồi thường
**Aliases:** lệnh SC

### Đơn mua HHDV
Đơn đặt mua hàng hoá/dịch vụ từ nhà cung cấp HHDV, duyệt 2 lần.
**Appears in:** Mua hàng, Thanh toán
**Aliases:** PO, đơn mua

### Định mức nhiên liệu
Mức tiêu hao nhiên liệu khoán cho từng phương tiện, phân loại theo tải trọng hàng hoá hoặc không theo tải trọng; có yêu cầu định mức cần phê duyệt và cập nhật mức tiêu hao thực tế.
**Appears in:** Quản lý phương tiện
**Aliases:** định mức NL, khoán định mức

### Barem (dầu)
Bảng quy đổi chiều cao mức dầu trong bồn sang lượng dầu (lít) của 1 cây dầu nội bộ, upload dạng file khi tạo cây dầu.
**Appears in:** Cây dầu
**Aliases:** —

### Kế hoạch mua dầu / Phiếu nhập dầu / Phiếu cấp dầu
Chuỗi nghiệp vụ dầu: lập kế hoạch mua → đơn mua dầu → nhập dầu vào cây dầu (từ nhà cung cấp hoặc phương tiện) → cấp dầu cho phương tiện. Phiếu cấp dầu tại cây dầu đối tác do nhân viên đối tác ghi nhận trên Portal.
**Appears in:** Cây dầu, Thanh toán trả sau
**Aliases:** —

### Thanh toán trả trước / trả sau
Hai phương thức thanh toán với nhà cung cấp hoặc khách hàng. **Trả trước**: lập đề nghị thanh toán cho từng đơn. **Trả sau**: gom vào **bảng công nợ** theo tháng rồi **chốt công nợ** (chốt được nhiều lần) và ghi nhận thanh toán.
**Appears in:** Thanh toán, Mua hàng, Cây dầu
**Aliases:** TT trả trước / TT trả sau

### GTTT (Giá trị thanh toán)
Tổng tiền phải thanh toán của 1 chứng từ, sau chiết khấu.
**Appears in:** Thanh toán, Mua hàng
**Aliases:** giá trị thanh toán

### Bồi thường thiệt hại
Đề nghị bồi thường khi có thất thoát: trả tiền chưa nhận đủ HHDV, chuyển kho chênh lệch số lượng, làm hỏng/mất phụ tùng trong lệnh sửa chữa.
**Appears in:** Thanh toán, Kho, Sửa chữa
**Aliases:** bồi thường

### Đề xuất cấp mới
Yêu cầu tạo bản ghi danh mục mới (DVKT, PTVT, CCDC, lốp, ắc quy, nhà cung cấp, khách hàng DK05, chi phí…). Bản ghi chỉ chính thức và có mã sau khi được phê duyệt.
**Appears in:** Danh mục, Cây dầu nội bộ
**Aliases:** yêu cầu cấp mới, đề xuất tạo mới

### Thu hồi
Người tạo rút lại yêu cầu đang chờ phê duyệt. Nếu thu hồi và phê duyệt xảy ra cùng lúc, hệ thống ưu tiên thu hồi.
**Appears in:** mọi luồng có phê duyệt
**Aliases:** huỷ đề xuất, huỷ yêu cầu (tránh dùng) — mọi luồng gọi thống nhất là "Thu hồi"

## Actor Registry

| Canonical | Loại | Aliases (tránh dùng) | Mô tả ngắn |
|---|---|---|---|
| Nhân viên nội bộ Delta | primary | Người dùng phần mềm xưởng, người dùng PM Xưởng, người tạo, người phê duyệt | Nhân viên Delta; thấy và làm gì tuỳ phân quyền |
| Lái xe | primary | ALX, người dùng app Lái xe | Nhân viên nội bộ Delta dùng App Lái xe (Mobile); làm được gì tuỳ phân quyền (vd báo cáo sự cố, nghiệm thu, nhận/trả phương tiện) |
| Admin | primary | Quản trị viên | Toàn quyền, quản lý tài khoản và phân quyền |
| Nhân viên đối tác cây dầu | secondary | đối tác, nhân viên cây dầu đối tác | Dùng Portal ghi nhận bơm dầu, xuất hoá đơn, chốt phiếu cấp dầu |
| Hệ thống | system | Backend, Server, BE | Xử lý nghiệp vụ phía sau, sinh mã, gửi thông báo |
| Sensor iGAS | external | Igas, IGAS | Thiết bị đo mức dầu tại cây dầu nội bộ |
| Delta ERP | external | ERP | Phần mềm ERP tích hợp |
