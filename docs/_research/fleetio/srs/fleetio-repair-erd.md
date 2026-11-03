---
type: research
feature: fleetio-repair
updated: 2026-11-03
---

# Sửa chữa — ERD nghiệp vụ

Suy ra từ form, cột danh sách, kết quả chạy và tài liệu hãng; không phải sơ đồ cơ sở dữ liệu thật của Fleetio. Thuộc tính ghi ở mức nghiệp vụ.

```mermaid
erDiagram
    VEHICLE ||--o{ ISSUE : "co"
    VEHICLE ||--o{ WORK_ORDER : "co"
    VEHICLE ||--o{ SERVICE_ENTRY : "co"
    VEHICLE ||--o{ FAULT : "phat sinh"
    VEHICLE ||--o{ WARRANTY : "duoc bao hanh"
    VEHICLE ||--o{ METER_ENTRY : "co so dong ho"
    WORK_ORDER ||--o{ WO_LINE : "gom"
    WORK_ORDER ||--o| SERVICE_ENTRY : "sinh ra"
    WORK_ORDER |o--o{ ISSUE : "giai quyet"
    SERVICE_ENTRY |o--o{ ISSUE : "giai quyet"
    WO_LINE }o--o{ ISSUE : "lien ket"
    WO_LINE }o--|| SERVICE_TASK : "la"
    WO_LINE ||--o{ LABOR_LINE : "co cong"
    WO_LINE ||--o{ PART_LINE : "co phu tung"
    CONTACT ||--o{ LABOR_LINE : "lam"
    CONTACT ||--o{ WORK_ORDER : "nhan viec"
    WO_STATUS ||--o{ WORK_ORDER : "phan loai"
    PART_LINE ||--o{ INVENTORY_ACTIVITY : "ghi so kho"
    WORK_ORDER ||--o{ METER_ENTRY : "ghi"
    SERVICE_ENTRY ||--o{ METER_ENTRY : "ghi"
    FAULT }o--o| ISSUE : "gom vao"
    WORK_ORDER ||--o| ASSESSMENT : "duoc danh gia"
    SERVICE_ENTRY ||--o| ASSESSMENT : "duoc danh gia"
    ISSUE ||--o| AI_DRAFT : "tao nhap"
    AI_DRAFT ||--o| WORK_ORDER : "tao thanh"
    WARRANTY ||--o{ WARRANTY_CODE : "khop theo"
    WARRANTY ||--o{ WARRANTY_COMPONENT : "chia pham vi"
    WO_LINE }o--o{ WARRANTY : "co hoi"
    LABOR_LINE ||--o| TIME_ENTRY : "tao"
    WORK_ORDER ||--o{ RECORD_HISTORY : "ghi thay doi"
    FAULT_RULE ||--o{ FAULT : "ap cho"
    WATCHER }o--|| WORK_ORDER : "theo doi"
    WATCHER }o--|| ISSUE : "theo doi"
    WARRANTY_TEMPLATE ||--o{ TEMPLATE_COVERAGE : "gom"
    TEMPLATE_COVERAGE ||--o{ WARRANTY : "sinh ra"

    VEHICLE {
        string ten
        string loai
        number so_km_hien_tai
    }
    LABOR_LINE {
        string ky_thuat_vien
        number gio
        money don_gia
    }
    PART_LINE {
        string phu_tung
        string kho
        number so_luong
        money don_gia
    }
    AI_DRAFT {
        string ly_do
        string trang_thai
        string tu_dien
    }
    ISSUE {
        number so
        string tom_tat
        string mo_ta
        string uu_tien
        string trang_thai
        string nguon
        datetime ngay_bao
        date han
        number han_so_km
        string nguon_giai_quyet
        datetime ngay_giai_quyet
        string ghi_chu_giai_quyet
        datetime ngay_dong
        string ghi_chu_dong
    }
    WORK_ORDER {
        number so
        string phan_loai_uu_tien
        datetime ngay_lap
        datetime bat_dau_du_kien
        datetime bat_dau_thuc_te
        datetime hoan_thanh_du_kien
        datetime hoan_thanh_thuc_te
        number so_km_dau
        number so_km_cuoi
        boolean dung_so_dau
        string hoa_don
        string so_don_mua
        number markup_cong
        number markup_phu_tung
        money tin_dung_bao_hanh
        number giam_gia
        number thue
        money tong
    }
    WO_LINE {
        money cong
        money phu_tung
        string ly_do_sua
        string nhom_he_thong
        string ghi_chu
        string trieu_chung
        string nguyen_nhan
        string khac_phuc
        string tinh_trang
    }
    SERVICE_ENTRY {
        number so
        datetime hoan_thanh
        number so_km
        money tong
        string tham_chieu
    }
    SERVICE_TASK {
        string ten
        string nhom_mac_dinh
        number gio_cong_du_kien
        string trang_thai
    }
    FAULT {
        string ma
        boolean nghiem_trong
        string mo_ta
        datetime lan_cuoi
        string trang_thai
    }
    WARRANTY {
        string ten
        string loai
        date bat_dau
        number thoi_han
        date ket_thuc
        number km_bat_dau
        number km_ket_thuc
        string ma_phan_loai
        string ma_hop_dong
        string trang_thai
    }
    ASSESSMENT {
        string ket_luan
        string tom_tat
        datetime luc_chay
    }
    METER_ENTRY {
        number gia_tri
        datetime thoi_diem
        string nguon
    }
    INVENTORY_ACTIVITY {
        number dieu_chinh
        number truoc
        number sau
        string nguon
    }
    CONTACT {
        string ten
        string nhom
        money don_gia_cong
    }
    WO_STATUS {
        string ten
        string mo_ta
        string mau
        string loai
        boolean mac_dinh
    }
    WARRANTY_TEMPLATE {
        string ten
        string don_vi_dong_ho
        string nguon
    }
    TEMPLATE_COVERAGE {
        string ten
        string loai
        number thoi_han
        number khoang_cach
        string ma_phan_loai
    }
    WARRANTY_CODE {
        string ma_he_thong
        string ma_assembly
    }
    WARRANTY_COMPONENT {
        string ten
        string mo_ta
    }
    TIME_ENTRY {
        datetime bat_dau
        datetime ket_thuc
    }
    RECORD_HISTORY {
        datetime thoi_diem
        string nguoi_doi
        string noi_dung_doi
    }
    FAULT_RULE {
        string ma
        string ten
        string mo_ta
        string xu_ly_uu_tien
    }
    WATCHER {
        string nguoi_dung
    }
```

| Quan hệ | Bằng chứng |
|---|---|
| Lệnh sinh một Service Entry | `Chạy` #99 và 57837459; #104 và 57857945. Mở lại thì entry bị xoá, hoàn thành lại sinh entry mới: một lệnh có một entry tại một thời điểm, nhiều entry theo thời gian nhưng entry cũ không còn |
| Sửa so với bản trước: một sự cố thuộc một lệnh | `Chạy` dòng đã ở lệnh khác có ổ khoá, tooltip yêu cầu gỡ. Bản trước vẽ nhiều nhiều. Tooltip viết "all Work Orders", cột cũng là số nhiều, nhưng lượt 3 đã thử: Draft Work Order xám trên #45; nháp của sự cố khác gợi ý #45 thì #45 vẫn chỉ ở #107 (OQ-14 đã trả lời) |
| Một Service Entry giải quyết nhiều sự cố; Reopen, bỏ tick tháo liên kết | `Chạy` hộp chọn nhiều, #37 tháo liên kết, #52 gắn vào entry có sẵn rồi bỏ tick. `Suy` một sự cố chỉ ở một entry |
| Dòng việc liên kết sự cố | `Chạy` #45 và dòng TEST-SUA-DV-A, cột Linked Line Items |
| Nhiều mã lỗi vào một sự cố | `Xem` Issue #13, #14, #15 nhận nhiều mã |
| Trường Triệu chứng, Nguyên nhân, Khắc phục | `Chạy` #107 là ba ô chữ theo từng đầu việc khớp bảo hành, không có bản ghi claim, không nối Warranty Credits. `Docs` phần bắt buộc khi bật cấu hình. `trieu_chung` theo cặp dòng việc và bảo hành hay chỉ theo dòng: `Suy`, chưa thử hai bảo hành cùng khớp một dòng |
| Tình trạng dòng việc | `Docs`; `Chạy` #107 web không có ô đánh dấu, nên thuộc tính `tinh_trang` chưa kiểm chứng |
| Bảo hành khớp dòng việc theo mã | `Chạy` #107, #110: khớp đúng từng mức `ma_he_thong`, `ma_assembly`; phần Component của mã bị bỏ. Quan hệ tính khi mở form hoặc lưu lệnh, không phải bản ghi riêng: `Suy` |
| Thành phần bảo hành | `Xem` hộp Add Component, mở rồi huỷ |
| Tổng lệnh, markup, credit, giảm giá, thuế | `Chạy` #107. Mỗi ô đổi được giữa phần trăm và số tiền; `number` ở sơ đồ chỉ để gọn |
| Time Entry từ dòng công | `Chạy` tick Set Labor Time Entry; bản ghi Time Entry ở đâu ngoài dòng: chưa xem |
| Record History trên lệnh | `Chạy` #107 cột Date, Changes By, Changes Made; `Suy` là một bản ghi cho mỗi dòng đổi |
| Luật mã lỗi | `Xem` hộp Add Fault Rule, 11 dòng; quan hệ với Fault là khớp chính xác Code |
| Người theo dõi | `Chạy` #110, sự cố; xe cũng có Watch nhưng không vẽ trên sơ đồ để gọn. Chỉ user, không phải liên hệ: `Chạy` #106 |
| Dòng phụ tùng ghi sổ kho | `Chạy` Inventory Activity ghi trước, sau, nguồn số lệnh. Tồn, kho chi tiết ở [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-erd.md|Kho, mua]] |
| Dòng đồng hồ có nguồn lệnh, entry | `Chạy` nguồn "Work Order #104", "Service Entry #57858956" |
| Contact có đơn giá công | `Chạy` TEST-SUA-KTV |
| Trạng thái lệnh thuộc danh mục có loại | `Chạy` thêm 2 trạng thái; loại chỉ Incomplete, Completed, khoá đổi khi đã có lệnh dùng |
| Mẫu bảo hành gồm coverage, sinh bảo hành riêng và vẫn liên kết | `Chạy` mẫu TEST: áp về quá khứ làm đổi End Date của bảo hành đã sinh. Mẫu OEM cùng cấu trúc là `Suy`; `nguon` phân biệt riêng, OEM theo nhóm trên ô chọn |
| Một Assessment trên một lệnh hay entry | `Chạy` khối trên lệnh, entry. Lịch sử các lần chạy lại: `Suy` chỉ giữ lần mới nhất |
| Overdue không có thuộc tính lưu | `Chạy` giá trị tính từ `han`, `han_so_km`, đồng hồ của xe |
| Đầu kéo, mooc là hai Vehicle, không có bản ghi tổ hợp trên lệnh | `Chạy` nhóm Lốp về Vehicle; `Suy` về lệnh |
