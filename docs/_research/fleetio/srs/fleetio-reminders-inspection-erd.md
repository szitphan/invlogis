---
type: research
feature: fleetio-reminders-inspection
updated: 2026-11-03
---

# Nhắc và kiểm tra — ERD nghiệp vụ

Suy ra từ form, kết quả chạy và tài liệu hãng, không phải sơ đồ cơ sở dữ liệu thật.

```mermaid
erDiagram
    VEHICLE ||--o{ SERVICE_REMINDER : "có"
    VEHICLE ||--o{ RENEWAL_REMINDER : "có"
    CONTACT ||--o{ RENEWAL_REMINDER : "có"
    VEHICLE ||--o{ METER_ENTRY : "ghi"
    SERVICE_TASK ||--o{ SERVICE_REMINDER : "được nhắc"
    SERVICE_PROGRAM ||--o{ PROGRAM_SCHEDULE : "gồm"
    PROGRAM_SCHEDULE }o--o{ SERVICE_TASK : "cho đầu việc"
    PROGRAM_SCHEDULE ||--o{ SERVICE_REMINDER : "sinh ra"
    SERVICE_PROGRAM ||--o{ PROGRAM_VEHICLE : "gán"
    VEHICLE ||--o{ PROGRAM_VEHICLE : "được gán"
    SERVICE_REMINDER ||--o{ COMPLIANCE_RECORD : "ghi từng lần"
    SERVICE_ENTRY ||--o{ COMPLIANCE_RECORD : "hoàn thành"
    WORK_ORDER ||--o| SERVICE_ENTRY : "sinh khi Completed"
    WORK_ORDER }o--o{ SERVICE_REMINDER : "đang xử lý"
    RENEWAL_TYPE ||--o{ RENEWAL_REMINDER : "phân loại"
    INSPECTION_FORM ||--o{ FORM_VERSION : "có phiên bản"
    FORM_VERSION ||--o{ INSPECTION_ITEM : "gồm"
    INSPECTION_FORM ||--o{ WORKFLOW : "có"
    INSPECTION_FORM ||--o{ SCHEDULE_RULE : "gán theo"
    SCHEDULE_RULE }o--o{ VEHICLE : "áp cho"
    FORM_VERSION ||--o{ SUBMISSION : "được nộp"
    VEHICLE ||--o{ SUBMISSION : "được kiểm"
    JOB ||--o{ SUBMISSION : "gắn lúc nộp"
    SUBMISSION ||--o| LOCATION_ENTRY : "sinh"
    SUBMISSION ||--o| METER_ENTRY : "ghi"
    SUBMISSION ||--o{ SUBMITTED_ITEM : "gồm"
    INSPECTION_ITEM ||--o{ SUBMITTED_ITEM : "trả lời"
    SUBMITTED_ITEM ||--o| ITEM_FAILURE : "khi lỗi"
    ISSUE ||--o{ ITEM_FAILURE : "gộp nhiều lần lỗi"
    SUBMITTED_ITEM ||--o{ TIRE_READING : "đọc lốp"
    VEHICLE ||--o{ WORK_ORDER_DRAFT : "có nháp"
    WORK_ORDER_DRAFT ||--o| WORK_ORDER : "thêm vào"
    SERVICE_REMINDER ||--o{ RECORD_HISTORY_ENTRY : "ghi thay đổi"
    RENEWAL_REMINDER ||--o{ RECORD_HISTORY_ENTRY : "ghi thay đổi"
    SERVICE_REMINDER ||--o| SERVICE_OCCURRENCE : "kỳ hiện tại"
    SERVICE_PROGRAM ||--o{ PROGRAM_RULE : "giữ đồng bộ"
    SUBMITTED_ITEM }o--o| PART_LOCATION : "lấy phụ tùng từ"
    SUBMITTED_ITEM ||--o{ INVENTORY_ADJUSTMENT : "trừ kho"
    PART_LOCATION ||--o{ INVENTORY_ADJUSTMENT : "tại"
    SERVICE_ENTRY ||--o| SERVICE_ASSESSMENT : "được đánh giá"
    SERVICE_REMINDER ||--o{ OUTSOURCED_ASSIGNMENT : "giao ngoài"

    VEHICLE {
        string ten
        number so_km_hien_tai
        string don_vi_dong_ho
        number so_km_ngay
        boolean tu_tinh_so_km_ngay
    }
    CONTACT {
        string ten
        boolean la_operator
    }
    JOB {
        string ten
    }
    SERVICE_TASK {
        string ten
    }
    ISSUE {
        number so
        string trang_thai
        string uu_tien
        string nguon
    }
    METER_ENTRY {
        number so
        datetime thoi_diem
        string void_status
    }
    LOCATION_ENTRY {
        string dia_chi
        string dia_diem_ban_dau
    }
    TIRE_READING {
        string vi_tri
        number do_gai
        number ap_suat
        string phuong_thuc
    }
    WORK_ORDER {
        number so
        string trang_thai
    }
    SERVICE_ENTRY {
        number so
        date ngay_hoan_thanh
        number so_dong_ho
    }
    SERVICE_REMINDER {
        number chu_ky_thoi_gian
        number chu_ky_so_km
        number nguong_thoi_gian
        number nguong_so_km
        date moc_ngay
        number moc_so_km
        boolean dat_tay_moc
        string trang_thai
        date hoan_den
        boolean thong_bao
        string nguoi_duoc_giao
        number moc_sap_den_han_km
        date ngay_du_bao
    }
    SERVICE_OCCURRENCE {
        number so
    }
    WORK_ORDER_DRAFT {
        string tom_tat_ai
        number so_viec
        number tam_tinh
        string trang_thai
    }
    RECORD_HISTORY_ENTRY {
        datetime thoi_diem
        string nguoi_doi
        string truong
        string gia_tri_truoc
        string gia_tri_sau
    }
    PROGRAM_RULE {
        string thuoc_tinh
        string gia_tri
    }
    PART_LOCATION {
        string ten
    }
    INVENTORY_ADJUSTMENT {
        datetime thoi_diem
        string loai
        string ly_do
        number so_luong
        number ton_truoc
        number ton_sau
        string nguoi_lam
    }
    SERVICE_ASSESSMENT {
        string ket_qua
        string tieu_de
        string nhan_xet
        number so_nguon
    }
    OUTSOURCED_ASSIGNMENT {
        string nguoi_nhan
        string thoi_gian
        string cach_bao
    }
    COMPLIANCE_RECORD {
        date moc_ngay
        number moc_so_km
        date ngay_lam
        number so_km_lam
        string ket_qua
        string chenh_lech
    }
    SERVICE_PROGRAM {
        string ten
        string dong_ho_chinh
        string dong_ho_phu
        string mau
        string hanh_vi_lich
    }
    PROGRAM_SCHEDULE {
        number chu_ky_thoi_gian
        number chu_ky_so_km
        number chu_ky_dong_ho_phu
        number nguong_thoi_gian
        number nguong_so_km
        number nguong_dong_ho_phu
        number lan_dau_thoi_gian
        number lan_dau_so_km
    }
    PROGRAM_VEHICLE {
        string cach_gan
    }
    RENEWAL_TYPE {
        string ten
        string ap_cho
    }
    RENEWAL_REMINDER {
        date den_han
        number nguong_bao_truoc
        string trang_thai
        boolean thong_bao
    }
    INSPECTION_FORM {
        string ten
        string mau_sac
        boolean theo_doi_vi_tri
        boolean cam_anh_co_san
    }
    FORM_VERSION {
        number phien_ban
    }
    INSPECTION_ITEM {
        string nhan
        string loai
        boolean bat_buoc
        string nhan_dat
        string nhan_khong_dat
        boolean cho_na
        boolean bat_ghi_chu_khi_dat
        boolean bat_ghi_chu_khi_loi
        number toi_thieu
        number toi_da
    }
    WORKFLOW {
        string trigger
        string pham_vi_muc
        string hanh_dong
        boolean bat
    }
    SCHEDULE_RULE {
        string pham_vi
        string tan_suat
        date bat_dau_tre
        boolean nhac_nguoi_lai
        string them_qua
        string form_status
    }
    SUBMISSION {
        datetime bat_dau
        datetime nop_luc
        number thoi_luong_giay
        string nguon
        string vi_do_kinh_do
        boolean ngoai_le_vi_tri
        boolean muc_qua_gan_nhau
        number so_muc_qua_xa
    }
    SUBMITTED_ITEM {
        string ket_qua
        string ghi_chu
        string vi_do_kinh_do_muc
        string phu_tung_da_dung
    }
    ITEM_FAILURE {
        string trang_thai
        string ghi_chu_ghi_nhan
    }
```

`FORM_VERSION` đã có bằng chứng hành vi (phiếu cũ mang "Past Version", `Chạy`); cách lưu phiên bản là `Suy`. Vị trí từng mục: trên web gói tin chỉ có một cặp toạ độ cấp phiếu (`Chạy (vị trí giả lập)`); phiếu Fleetio Go có cặp `latitude`, `longitude` riêng cho 21/21 mục cùng hai chỉ báo `are_items_too_close`, `items_completed_too_far_away_count` (`Chạy (Fleetio Go)`). `moc_sap_den_han_km`, `SERVICE_OCCURRENCE` lộ từ Record History ("Due Soon Meter Value", "Current Service Occurrence"), `Chạy`. `RECORD_HISTORY_ENTRY` có bản ghi thật; cấu trúc là `Suy`. `WORK_ORDER_DRAFT`, `PROGRAM_RULE`, `PART_LOCATION` đặt tên theo màn; quan hệ của `WORK_ORDER_DRAFT` với `WORK_ORDER` chưa chạy, `PROGRAM_RULE` chưa lưu được vì còn Sample Data (`Suy`). `INVENTORY_ADJUSTMENT` có bản ghi thật ở Inventory Activity (`Chạy`). `SERVICE_ASSESSMENT` thấy trên phiếu (`Chạy`). `OUTSOURCED_ASSIGNMENT` dừng ở Confirm, chưa tạo (`Suy`). `so_km_ngay`, `tu_tinh_so_km_ngay` thấy trên form Vehicle (`Chạy`); `ngay_du_bao` có thể tính khi đọc, không lưu (`Suy`). Cờ Forecasting ở cấp tài khoản, không vẽ. `COMPLIANCE_RECORD`, `ITEM_FAILURE`, `PROGRAM_SCHEDULE`, `PROGRAM_VEHICLE` là tên đặt để mô tả, suy từ màn hình (`Suy`). Một `ISSUE` gom nhiều `ITEM_FAILURE` khi lỗi lặp lúc sự cố còn mở (`Chạy`).
