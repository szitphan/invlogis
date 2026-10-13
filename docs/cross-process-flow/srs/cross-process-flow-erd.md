---
type: srs-erd
feature: cross-process-flow
updated: 2026-10-12
---

# Liên quy trình — Entity Relationship Diagram

> Scope: Quy trình, Bước quy trình và các đối tượng nó trỏ tới. Bản ghi nghiệp vụ của từng module (Báo giá, Lệnh sửa chữa, Phiếu xuất kho…) chi tiết ở SRS module đó.

## Diagram

```mermaid
erDiagram
    ChiNhanh ||--o{ QuyTrinh : "có"
    PhuongTien |o--o{ QuyTrinh : "có"
    XeKhachHang |o--o{ QuyTrinh : "có"
    QuyTrinh ||--|{ BuocQuyTrinh : "gồm"
    BuocQuyTrinh ||--o{ LienKetBuoc : "là bước trước"
    BuocQuyTrinh ||--o{ LienKetBuoc : "là bước sau"
    BuocQuyTrinh |o--o{ BanGhiNghiepVu : "ứng với"
    BangCongNo |o--o{ BuocQuyTrinh : "được trỏ tới"

    QuyTrinh {
        string ma_quy_trinh PK "QT-[Mã chi nhánh]-[YY]-[XXXX], dữ liệu cũ QT-[Mã chi nhánh]-LG-[XXXX], sinh khi bản ghi gốc gửi thành công"
        string luong "vd Sửa chữa xe khách hàng"
        string trang_thai "Đang triển khai | Đã dừng | Đã hoàn thành"
        string chi_nhanh_id FK "chi nhánh lúc tạo, không đổi"
        string phuong_tien_id FK "theo luồng, có thể trống"
        string xe_khach_hang_id FK "theo luồng, có thể trống"
        datetime cap_nhat_lan_cuoi "lọc + sắp danh sách"
    }
    BuocQuyTrinh {
        string id PK
        string quy_trinh_id FK
        string bang_cong_no_id FK "chỉ bước thanh toán trả sau"
        string ten_buoc
        string loai_buoc "bước chính | nhánh phát sinh | ngã rẽ chưa chốt | công nợ"
        string module "nhãn module khi khác module đang mở"
        string trang_thai "Chưa triển khai | Đang triển khai | Đã hoàn thành | Đã thu hồi/từ chối | Đã huỷ (chỉ nhánh phát sinh)"
        string truong_hop_phat_sinh "câu cho người dùng đọc, giá trị lúc phát sinh"
        string truong_hop_phat_sinh_en "nhãn tiếng Anh"
        string cac_huong_co_the_di "chỉ ngã rẽ"
    }
    LienKetBuoc {
        string buoc_quy_trinh_truoc_id FK
        string buoc_quy_trinh_sau_id FK
        string nhan_dieu_kien "1 dòng, tối đa 40 ký tự (bắt buộc)"
        string nhan_dieu_kien_en "nhãn tiếng Anh"
    }
    BanGhiNghiepVu {
        string id PK
        string buoc_quy_trinh_id FK "trống khi còn là bản nháp"
        string ma_yeu_cau "sinh khi gửi, giữ nguyên khi sửa rồi gửi lại"
        string ma_ban_ghi "sinh khi được duyệt, trống trước đó"
        string loai "Báo cáo sự cố, Báo giá, Lệnh sửa chữa, Phiếu xuất kho..."
        string trang_thai
        boolean da_thay_the "true khi bước 1 bản ghi đã nhận bản ghi mới thay"
    }
    BangCongNo {
        string id PK
        string nha_cung_cap
        date tu_ngay
        date den_ngay
        string trang_thai
    }
    ChiNhanh {
        string ma_chi_nhanh PK
    }
    PhuongTien {
        string id PK
    }
    XeKhachHang {
        string id PK
    }
```

## Entity Reference

| Entity | Purpose | Key attributes |
|--------|---------|----------------|
| QuyTrinh | Quy trình — chuỗi nghiệp vụ bắt đầu từ một bản ghi gốc, trạng thái do hệ thống tự tính | Mã quy trình (BR-cross-process-flow-004) · Luồng · Trạng thái · Chi nhánh · Cập nhật lần cuối |
| BuocQuyTrinh | Bước quy trình — một nút trên cây, ứng với tối đa 1 bản ghi hiện hành; bước "1 bản ghi" có thể kèm các bản ghi Đã thay thế | Tên bước · Loại bước · Module · Trạng thái · Trường hợp phát sinh |
| LienKetBuoc | Đường nối bước trước → bước sau; 1 bước có thể có nhiều bước trước (R1) | Bước trước · Bước sau · Nhãn điều kiện |
| BanGhiNghiepVu | Đại diện cho 14 loại bản ghi của các module (object map Mục 2) | Mã yêu cầu · Mã bản ghi · Loại · Trạng thái · Đã thay thế |
| BangCongNo | Bảng công nợ (nhóm đơn) của nhà cung cấp — thuộc SRS Thanh toán | Nhà cung cấp · Khoảng thời gian · Trạng thái |
| ChiNhanh, PhuongTien, XeKhachHang | Đối tượng cấp dự án (object map dự án) | — |

## Notes & Assumptions

- Object map ghi "Bước quy trình phát sinh Bước quy trình 1–n". ERD tách thành `LienKetBuoc` vì một bước có thể cần nhiều bước trước cùng xong (R1).
- Mỗi bản ghi thuộc đúng 1 cây (BR-cross-process-flow-001): `BanGhiNghiepVu` ứng với tối đa 1 `BuocQuyTrinh` (bản nháp chưa ứng với bước nào).
- Một `BuocQuyTrinh` có nhiều `BanGhiNghiepVu` chỉ khi bước khai "1 bản ghi" nhận bản ghi thay thế (BR-cross-process-flow-011): đúng 1 bản ghi hiện hành (`da_thay_the` = false), còn lại Đã thay thế. Bước "nhiều bản ghi" không dùng cách này — mỗi bản ghi là 1 bước anh em (BR-cross-process-flow-008).
- Mã trên thẻ bước: `ma_ban_ghi` nếu đã có, không thì `ma_yeu_cau` (BR-cross-process-flow-012). Ô tìm tìm cả hai.
- Nhãn tiếng Anh lấy từ bảng liên quy trình của nghiệp vụ (BR-cross-process-flow-007).
- Bản ghi gốc của quy trình là bước không có `LienKetBuoc` nào trỏ vào.
- Tiến độ, số nhánh phát sinh và Bước đang chờ tính từ các bước, không lưu riêng; không tính bước Đã huỷ và bản ghi Đã thay thế.
