---
type: srs-erd
feature: account-access
updated: 2026-10-15
---

# Đăng nhập và tài khoản cá nhân — Entity Relationship Diagram

> Scope: tài khoản và các đối tượng phục vụ đăng nhập, đặt lại mật khẩu. KHACH, CHI_NHANH, HO_SO_NHAN_VIEN, CAY_DAU thuộc feature khác (`organization`, `employee-records`, `fuel-stations`), chỉ vẽ để thấy quan hệ.

## Diagram

```mermaid
erDiagram
    KHACH ||--o{ TAI_KHOAN : "có"
    TAI_KHOAN ||--o{ MAT_KHAU_TAM : "được cấp"
    TAI_KHOAN ||--o{ PHIEN : "mở"
    TAI_KHOAN ||--o{ YEU_CAU_DAT_LAI : "nhận"
    TAI_KHOAN ||--o| CHI_NHANH_GAN_NHAT : "nhớ"
    TAI_KHOAN ||--o{ LICH_SU_HOAT_DONG : "ghi"
    CHI_NHANH ||--o{ CHI_NHANH_GAN_NHAT : "được chọn"
    CHI_NHANH ||--o{ PHIEN : "đang dùng"
    HO_SO_NHAN_VIEN |o--o| TAI_KHOAN : "gắn với"
    CAY_DAU |o--o{ TAI_KHOAN : "đối tác"
    KHACH ||--o{ DEM_SAI_THEO_TEN : "đếm"

    KHACH {
        string ten_khach "tham chiếu"
        string duong_dan_dang_nhap
    }
    CHI_NHANH {
        string ten_chi_nhanh "tham chiếu organization"
        string tinh_thanh
    }
    HO_SO_NHAN_VIEN {
        string ma_nhan_vien "tham chiếu employee-records"
    }
    CAY_DAU {
        string ma_doi_tac "tham chiếu fuel-stations"
    }
    TAI_KHOAN {
        string ten_tai_khoan
        string email
        string so_dien_thoai
        string loai
        string trang_thai
        string quyen_kenh
        string ngon_ngu
        string anh_dai_dien
        int so_lan_sai_lien_tiep
        datetime het_khoa_luc
    }
    MAT_KHAU_TAM {
        datetime cap_luc
        datetime het_han_luc
        string nguoi_cap
        boolean con_hieu_luc
    }
    PHIEN {
        string kenh
        string thiet_bi
        boolean ghi_nho
        datetime thao_tac_cuoi
        datetime het_han_luc
        string trang_thai
    }
    YEU_CAU_DAT_LAI {
        string ten_da_nhap
        string loai
        datetime gui_luc
        datetime het_han_luc
        int so_lan_nhap_sai
        boolean da_dung
        string ket_qua_gui
    }
    CHI_NHANH_GAN_NHAT {
        boolean la_cong_ty_me
        datetime chon_luc
    }
    DEM_SAI_THEO_TEN {
        string ten_da_nhap
        int so_lan_sai_lien_tiep
        datetime het_khoa_luc
    }
    LICH_SU_HOAT_DONG {
        datetime luc
        string hanh_dong
        string doi_tuong
    }
```

## Ghi chú

| Thực thể | Ghi chú nghiệp vụ |
|---|---|
| TAI_KHOAN | `loai`: nội bộ / đối tác. `trang_thai`: Chờ kích hoạt, Đang hoạt động, Tạm khoá, Vô hiệu hoá (xem states.md). Tên tài khoản và email duy nhất trong một KHACH (BR-account-access-001). |
| MAT_KHAU_TAM | Chỉ bản mới nhất còn hiệu lực (BR-account-access-005). Không lưu mật khẩu dạng xem được (NFR-account-access-005). |
| PHIEN | `kenh`: web / app. Kết thúc theo BR-account-access-012 và FR-account-access-013, 014, 016. |
| YEU_CAU_DAT_LAI | `loai`: link / mã OTP / Liên hệ IT. Ghi cả khi tên đã nhập không tồn tại (để đếm giới hạn, BR-account-access-010); khi đó không gắn TAI_KHOAN. |
| DEM_SAI_THEO_TEN | Bộ đếm sai cho tên đã nhập không tồn tại, để báo và "khoá" giống tên có thật (BR-account-access-003, 022). |
| LICH_SU_HOAT_DONG | Lưu không giới hạn (OQ-7); người dùng xem 90 ngày gần nhất (NFR-account-access-007). |
