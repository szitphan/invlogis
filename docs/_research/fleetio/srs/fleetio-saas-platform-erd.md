---
type: research
feature: fleetio-saas-platform
updated: 2026-11-03
---

# Nền tảng SaaS — ERD nghiệp vụ

Suy ra từ giao diện và tài liệu hãng, không phải sơ đồ cơ sở dữ liệu thật.

```mermaid
erDiagram
    ACCOUNT ||--o{ CONTACT : "có"
    CONTACT ||--o| USER : "có đăng nhập"
    ROLE ||--o{ USER : "gán cho"
    RECORD_SET }o--o{ USER : "gán cho"
    ACCOUNT ||--o{ ROLE : "định nghĩa"
    ROLE ||--o{ ROLE_PERMISSION : "theo module"
    ACCOUNT ||--o{ RECORD_SET : "định nghĩa"
    USER ||--o{ SAVED_VIEW : "tạo"
    ACCOUNT ||--o{ AUTOMATION : "có"
    AUTOMATION ||--o{ AUTOMATION_VERSION : "sinh khi bật"
    AUTOMATION ||--o{ AUTOMATION_RUN : "chạy"
    AUTOMATION_VERSION ||--o{ AUTOMATION_RUN : "được ghi ở"
    AUTOMATION_TEMPLATE ||--o{ AUTOMATION : "điền sẵn"
    ACCOUNT ||--o{ DASHBOARD : "có"
    ACCOUNT ||--o{ CUSTOM_FIELD : "khai"
    ACCOUNT ||--o{ CUSTOM_RECORD_TYPE : "khai"
    ACCOUNT ||--o{ WEBHOOK : "đăng ký"
    ACCOUNT ||--o{ ACCOUNT_SETTING : "cấu hình"
    ACCOUNT ||--o{ PLAN_LIMIT : "giới hạn"
    ACCOUNT ||--o{ GROUP_NODE : "có"
    GROUP_NODE ||--o{ GROUP_NODE : "cha con"
    GROUP_NODE ||--o{ CONTACT : "chứa"
    ACCOUNT ||--o{ REPORT_VIEW : "lưu"
    USER ||--o{ REPORT_VIEW : "tạo"
    REPORT_VIEW ||--o{ REPORT_SHARE_LINK : "chia sẻ"
    USER ||--o{ AI_CONVERSATION : "lưu"
    ACCOUNT ||--o{ RECALL : "có"
    ACCOUNT ||--o{ MOTOR_POOL : "có"
    MOTOR_POOL ||--o{ RESERVATION : "nhận"
    CONTACT ||--o{ RESERVATION : "đặt"
    ACCOUNT ||--o{ DOCUMENT : "lưu"

    ACCOUNT {
        string ten
        string tien_te
        string mui_gio
        string dinh_dang_ngay
        string don_vi_do
        string goi
        string goi_doi_tuong
    }
    PLAN_LIMIT {
        string loai
        number da_dung
        number gioi_han
    }
    CONTACT {
        string ten
        string email
        string phan_loai
        boolean la_operator
        boolean la_employee
        boolean la_technician
    }
    USER {
        string trang_thai
        string loai
        number so_lan_dang_nhap
    }
    GROUP_NODE {
        string ten
        string nhom_cha
    }
    ROLE {
        string ten
        string mo_ta
        boolean khoa
    }
    ROLE_PERMISSION {
        string module
        string muc
        string quyen_con
    }
    RECORD_SET {
        string ten
        string doi_tuong
        string quyen_quan_ly
        string quyen_xem
        string dieu_kien
        boolean khoa
    }
    SAVED_VIEW {
        string ten
        string man
        string bo_loc
        string cot
        boolean dung_chung
    }
    AUTOMATION {
        string ten
        string loai_ban_ghi
        string kieu_su_kien
        string dieu_kien
        string hanh_dong
        boolean bat
        number phien_ban
        datetime enabled_at
        datetime disabled_at
        boolean luu_tru
        string email_bao_loi
    }
    AUTOMATION_VERSION {
        number so
        datetime luc_sinh
    }
    AUTOMATION_RUN {
        datetime luc_chay
        string ket_qua
        string ban_ghi_kich_hoat
        string triggered_by
        string log
    }
    AUTOMATION_TEMPLATE {
        string ten
        string loai_ban_ghi
        number so_dieu_kien
        number so_hanh_dong
    }
    DASHBOARD {
        string ten
        string khoi
    }
    CUSTOM_FIELD {
        string nhan
        string kieu
        string loai_ban_ghi
    }
    CUSTOM_RECORD_TYPE {
        string ten
        string truong
        string lien_ket
    }
    WEBHOOK {
        string dia_chi
        string su_kien
        string trang_thai
    }
    ACCOUNT_SETTING {
        string nhom
        string khoa
        string gia_tri
    }
    REPORT_VIEW {
        string ten
        string nhom
        string bo_loc
        string cot
    }
    REPORT_SHARE_LINK {
        string trang_thai
        datetime het_han
    }
    AI_CONVERSATION {
        string cau_hoi
        string cau_tra_loi
        string data_model
    }
    RECALL {
        date issued_at
        string trang_thai
        string so_chien_dich_hang
        string so_chien_dich_nhtsa
    }
    MOTOR_POOL {
        string ten
    }
    RESERVATION {
        string so
        string loai_xe
        datetime nhan_xe
        datetime tra_xe
        string trang_thai
    }
    DOCUMENT {
        string ten_tep
        number kich_thuoc
        string vi_tri
        string tu_xoa
        string gan_voi
        string nhan
    }
```

**Ghi chú nghiệp vụ:**

- Contact là bảng gốc; User là Contact được bật truy cập (`Chạy` phần No Access). Lái xe, thợ, kế toán chung một hồ sơ, phân vai bằng tick.
- Automation sinh phiên bản khi bật (`Chạy` v.1); chưa thấy v.2.
- Group gán cho cả xe và liên hệ; xe thuộc nhóm Phương tiện nên không vẽ lại ở đây (`Xem`).
- Report Share Link không lưu trong sơ đồ giá trị đường dẫn vì tài liệu này không ghi link đã chia sẻ.
- Quan hệ Reservation với xe và Recall với xe, Issue thuộc nhóm khác, chưa chạy.
