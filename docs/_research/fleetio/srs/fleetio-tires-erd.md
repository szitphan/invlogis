---
type: research
feature: fleetio-tires
updated: 2026-11-03
---

# Quản lý lốp — ERD nghiệp vụ

Suy ra từ form, tên trường và kết quả chạy thật, không phải sơ đồ cơ sở dữ liệu thật. Điểm chính: **TIRE là một vị trí trên một xe**, mã lốp (TIN) chỉ là một trường chữ không duy nhất.

```mermaid
erDiagram
    VEHICLE ||--o| AXLE_CONFIG : "khai"
    AXLE_CONFIG ||--|{ AXLE : "gom"
    VEHICLE ||--o{ TIRE : "chua"
    AXLE ||--o{ TIRE : "dat tai"
    TIRE_MODEL ||--o{ TIRE : "mau cua"
    TIRE ||--o{ TIRE_ACTIVITY : "lich su"
    VEHICLE ||--o{ METER_ENTRY : "dong ho"
    VEHICLE ||--o{ VEHICLE_LINK : "lien ket"
    VEHICLE ||--o{ INSPECTION_SUBMISSION : "duoc kiem"
    INSPECTION_SUBMISSION ||--o{ TIRE_ACTIVITY : "ghi doc"
    INSPECTION_SUBMISSION ||--o{ ISSUE : "tao"
    AXLE_CONFIG ||--o{ ROTATION_PATTERN : "ap mau"
    VEHICLE {
        string ten PK
        string loai
        string don_vi_dong_ho "bat buoc, ke ca mooc"
    }
    AXLE_CONFIG {
        string ma PK "1 trong 27 dong"
        string vehicle_id FK
        string nhom "xe hoac mooc"
        number so_truc "Multi-Axle tu 2 den 10"
    }
    AXLE {
        string ma PK
        string config_id FK
        string vai_tro "Steer, Drive, Trailer"
    }
    TIRE {
        string ma PK "sinh theo vi tri"
        string vehicle_id FK
        string axle_id FK
        string model_id FK
        string vi_tri "LF, 2LO, Spare"
        date ngay_lap
        number km_luc_lap
        number gai_hien_tai
        number ap_hien_tai
        number gai_toi_thieu
        number gai_ban_dau
        number tuoi_tho
        string tin "khong duy nhat"
    }
    TIRE_MODEL {
        string part_id PK "Part category lop"
        number gai_ban_dau
        number gai_toi_thieu
        number tuoi_tho
    }
    TIRE_ACTIVITY {
        string ma PK
        string tire_id FK
        string submission_id FK
        string loai "Installed, Rotation, Reading, Removal, Spare Stowed"
        string cach "Manual, Inspection, Telematics, API, Import"
        date ngay_ghi
        string vi_tri
        string vai_tro_truc
    }
    ROTATION_PATTERN {
        string ten PK "cap tai khoan, o Settings"
        string config_id FK
        string nhom "Standard co khoa, hoac tuy bien"
        date ngay_tao
    }
    METER_ENTRY {
        string ma PK
        string vehicle_id FK
        number gia_tri
        date ngay
    }
    VEHICLE_LINK {
        string ma PK
        string vehicle_id FK
        string linked_vehicle_id FK
    }
    INSPECTION_SUBMISSION {
        string ma PK
        string vehicle_id FK
        string ket_qua
    }
    ISSUE {
        string ma PK
        string submission_id FK
        string mo_ta "vi tri chi nam trong chu"
        string uu_tien
    }
```

Tire Readings là góc nhìn của TIRE ở lần đọc mới nhất, không phải bảng riêng (`Suy`). Lốp đã tháo mất khỏi Tire Readings, còn dòng TIRE_ACTIVITY (`Chạy`). Không thấy quan hệ TIRE với Work Order, kho hay chi phí (`Chạy`, với Work Order là `Chạy một phần`). `VEHICLE_LINK` là nhiều-nhiều: một mooc nối được nhiều xe, không có ngày hiệu lực (`Chạy`). `ROTATION_PATTERN` thuộc cấp tài khoản; một mẫu áp cho nhiều cấu hình, vd Standard 6x4 cho 6x2 / 6x4 / 6x6 (`Xem`), nên cột `config_id` đang vẽ là giản lược. Xe Archived giữ `AXLE_CONFIG` (`Chạy`).

## Đề xuất Invlogis: mô hình quả lốp

> Phần này **không phải Fleetio**, chưa chốt với Delta (DX-01 đến DX-05, DX-07, DX-08).

```mermaid
erDiagram
    TIRE_UNIT ||--o{ FITMENT : "cac lan lap"
    VEHICLE ||--o{ FITMENT : "chua"
    TYRE_POSITION ||--o{ FITMENT : "tai"
    TYRE_LAYOUT ||--|{ TYRE_POSITION : "gom"
    VEHICLE }o--|| TYRE_LAYOUT : "dung so do"
    REPAIR_ORDER ||--o{ FITMENT : "chot"
    COMBO ||--o{ TRANSPORT_ORDER : "gan lenh"
    VEHICLE ||--o{ COMBO : "dau keo hoac mooc"
    TRANSPORT_ORDER ||--o{ FITMENT_KM : "cong km"
    FITMENT ||--o{ FITMENT_KM : "tich luy"
    TIRE_UNIT ||--o{ TIRE_READING : "doc"
    TIRE_UNIT {
        string serial PK "duy nhat"
        string mau_lop
        string trang_thai "Trong kho, Dang lap, Du phong, Ton xuong, Rac thai"
    }
    FITMENT {
        string ma PK
        string tire_unit_id FK "serial"
        string vehicle_id FK
        string position_id FK
        string repair_order_id FK
        date tu_ngay
        date den_ngay
        string ly_do_thao
    }
    VEHICLE {
        string ma PK
        string layout_id FK
    }
    TYRE_LAYOUT {
        string ma PK "tractor-6x4, trailer-3ax"
    }
    TYRE_POSITION {
        string ma PK
        string layout_id FK
        number so_thu_tu
        string ben "ben lai, ben phu"
    }
    REPAIR_ORDER {
        string ma PK
        date ngay_chot
    }
    COMBO {
        string ma PK
        string vehicle_id FK "dau keo"
        string mooc_vehicle_id FK "0 hoac 1"
    }
    TRANSPORT_ORDER {
        string ma PK
        string combo_id FK
        number km
    }
    FITMENT_KM {
        string fitment_id FK
        string order_id FK
        number km
    }
    TIRE_READING {
        string ma PK
        string tire_unit_id FK "serial"
        number gai
        number ap_suat
        date ngay_doc
    }
```

Container không có lốp nên không xuất hiện trong mô hình lốp, dù thuộc tổ hợp.
