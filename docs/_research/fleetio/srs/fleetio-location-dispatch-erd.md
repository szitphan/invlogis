---
type: research
feature: fleetio-location-dispatch
updated: 2026-11-03
---

# Bản đồ, gán việc — ERD nghiệp vụ

Suy ra từ form, màn hình, dữ liệu phiếu quan sát được và tài liệu hãng, không phải sơ đồ cơ sở dữ liệu thật.

```mermaid
erDiagram
    VEHICLE ||--o{ LOCATION_ENTRY : "có vị trí"
    INSPECTION_SUBMISSION ||--o| LOCATION_ENTRY : "sinh ra"
    FUEL_ENTRY ||--o| LOCATION_ENTRY : "sinh ra khi có nhà cung cấp"
    VENDOR ||--o{ FUEL_ENTRY : "bán dầu"
    VEHICLE ||--o{ FUEL_ENTRY : "đổ dầu"
    SERVICE_ENTRY ||--o| LOCATION_ENTRY : "sinh ra khi có nhà cung cấp"
    VENDOR ||--o{ SERVICE_ENTRY : "làm dịch vụ"
    VEHICLE ||--o{ SERVICE_ENTRY : "được làm dịch vụ"
    VEHICLE ||--o{ INSPECTION_SUBMISSION : "được kiểm"
    INSPECTION_SUBMISSION ||--o{ INSPECTION_ITEM : "gồm mục"
    JOB_ASSIGNMENT ||--o{ INSPECTION_SUBMISSION : "gắn lúc nộp"
    PLACE ||--o{ LOCATION_ENTRY : "chứa lần ghi"
    PLACE ||--o{ GEOFENCE_EVENT : "vào ra"
    VEHICLE ||--o{ GEOFENCE_EVENT : "tạo"
    LOCATION_ENTRY ||--o{ GEOFENCE_EVENT : "kích hoạt"
    PLACE ||--o{ GEOFENCE_ALERT_POLICY : "có cảnh báo"
    GEOFENCE_EVENT }o--o{ AUTOMATION : "kích hoạt"
    PLACE ||--o{ JOB : "diễn ra tại"
    JOB ||--o{ JOB_ASSIGNMENT : "gồm"
    VEHICLE ||--o{ JOB_ASSIGNMENT : "tham gia"

    VEHICLE {
        string id PK
        string ten
        string trang_thai
        string current_job
    }
    LOCATION_ENTRY {
        string id PK
        string vehicle_id FK
        string submission_id FK
        string fuel_entry_id FK
        string service_entry_id FK
        string initial_place FK
        datetime thoi_diem
        number vi_do
        number kinh_do
        string dia_chi "rỗng khoảng 1 phút đầu với phiếu kiểm"
        string entry_type "Fuel Entry, Service Entry hoặc Inspection"
        string contact
    }
    FUEL_ENTRY {
        string id PK
        string vehicle_id FK
        string vendor_id FK "để trống thì không sinh vị trí"
        datetime ngay
        number dong_ho
    }
    SERVICE_ENTRY {
        string id PK
        string vehicle_id FK
        string vendor_id FK "chỉ nhà cung cấp phân loại Service"
        datetime ngay_hoan_thanh
    }
    VENDOR {
        string id PK
        string ten
        string dia_chi "giữ chuỗi đã nhập, quy ra điểm cho lần ghi, không có độ tin cậy"
        string phan_loai "Service mới chọn được ở phiếu dịch vụ"
    }
    INSPECTION_ITEM {
        string id PK
        string submission_id FK
        number latitude "chỉ có từ Fleetio Go"
        number longitude "chỉ có từ Fleetio Go"
    }
    INSPECTION_SUBMISSION {
        string id PK
        string vehicle_id FK
        string job_assignment FK "việc đang gán lúc nộp"
        number submitted_latitude
        number submitted_longitude
        number starting_latitude "rỗng cả trên web và Fleetio Go"
        boolean location_exception "luôn false trên web"
        boolean are_items_too_close "thấy trên phiếu Fleetio Go"
        number items_completed_too_far_away_count "thấy trên phiếu Fleetio Go"
        string submission_source
        string submitted_from
    }
    PLACE {
        string id PK
        string ten
        string mo_ta
        string dia_chi
        number vi_do
        number kinh_do
        number ban_kinh "đa giác thì tự tính"
        string loai_vung "tròn hoặc đa giác"
        string vung_ve
    }
    GEOFENCE_EVENT {
        string id PK
        string place_id FK
        string vehicle_id FK
        string location_entry_id FK
        string loai "Entered hoặc Exited"
        datetime thoi_diem
    }
    GEOFENCE_ALERT_POLICY {
        string id PK
        string place_id FK
        string trigger
        string nguoi_nhan
        boolean enabled
        boolean receive_as_summary
    }
    AUTOMATION {
        string id PK
        string record_type
        string trigger_type
        string dieu_kien
        string hanh_dong
        boolean bat
        number total_runs
    }
    JOB {
        string id PK
        string place_id FK
        string so
        string ten
        string trang_thai
        boolean auto_tracking
        datetime bat_dau
        datetime ket_thuc
    }
    JOB_ASSIGNMENT {
        string id PK
        string job_id FK
        string vehicle_id FK
        datetime bat_dau
        datetime ket_thuc
        number thoi_gian_tren_viec
        string added "Manual hoặc Geofence"
    }
```

## Mức bằng chứng

| Thành phần | Mức |
|---|---|
| JOB, JOB_ASSIGNMENT, các cột hiện trên màn | `Chạy` |
| JOB_ASSIGNMENT.added = Geofence, INSPECTION_SUBMISSION.job_assignment | `Chạy (vị trí giả lập)` |
| LOCATION_ENTRY, `initial_place`, `location_exception`, `submitted_latitude`, `submitted_longitude` | `Chạy (vị trí giả lập)` |
| FUEL_ENTRY, VENDOR, LOCATION_ENTRY.entry_type, liên kết phiếu dầu với lần ghi | `Chạy`; quan hệ qua khoá ngoại là `Suy` từ Source trên panel |
| VENDOR.phan_loai | `Chạy`, chỉ thấy tác dụng ở form Service Entry |
| SERVICE_ENTRY, Location Entry loại Service Entry | `Chạy`; quan hệ qua khoá ngoại là `Suy` từ dòng cùng giờ phiếu |
| INSPECTION_ITEM.latitude, longitude, `submitted_from`, `are_items_too_close`, `items_completed_too_far_away_count` | `Chạy (Fleetio Go)` |
| PLACE, loại vùng | `Chạy` |
| GEOFENCE_EVENT.loai, trigger Created | `Chạy (vị trí giả lập)` |
| GEOFENCE_EVENT là bản ghi riêng, liên kết với LOCATION_ENTRY | `Suy`: có Record Type nhưng không có màn xem |
| GEOFENCE_ALERT_POLICY | `Xem`, chưa lưu |
| AUTOMATION nhiều-nhiều với GEOFENCE_EVENT | `Suy` từ số lần chạy |
| Khoá chính, khoá ngoại | `Suy`, thêm để đọc quan hệ |
| Lớp đồng hồ, Issue, Equipment | Ngoài sơ đồ; Equipment có API tương tự (`Docs`) |
