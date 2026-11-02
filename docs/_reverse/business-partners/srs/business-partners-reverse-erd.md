---
type: reverse-srs-erd
feature: business-partners
updated: 2026-10-20
---

# Đối tác: nhà cung cấp, khách hàng, xe của khách (`business-partners`) — ERD tái lập (reverse)

```mermaid
erDiagram
    NHA_CUNG_CAP_HHDV ||--o{ CHUNG_TU_NCC : "đính kèm"
    NHA_CUNG_CAP_HHDV }o--|| CHI_NHANH_DELTA : "ký hợp đồng với"
    NHA_CUNG_CAP_HHDV }o--o| NGAN_HANG : "mở tài khoản tại"
    KHACH_HANG_DK05 }o--o| NGAN_HANG : "mở tài khoản tại"
    KHACH_HANG_DK05 ||--o{ XE_KHACH_HANG : "sở hữu"
    XE_KHACH_HANG }o--|| LOAI_PHUONG_TIEN : "thuộc loại"
    LOAI_PHUONG_TIEN ||--o{ MA_PHUONG_TIEN : "gồm"
    XE_KHACH_HANG }o--|| MA_PHUONG_TIEN : "có mã"
    YEU_CAU_CAP_MOI ||--o{ LICH_SU_HOAT_DONG : "ghi lịch sử"
    YEU_CAU_CAP_MOI ||--o{ THONG_BAO : "sinh thông báo"
    NGUOI_DUNG ||--o{ YEU_CAU_CAP_MOI : "tạo"
    NGUOI_DUNG ||--o{ LICH_SU_HOAT_DONG : "thực hiện"
    NGUOI_DUNG ||--o{ THONG_BAO : "nhận"

    NHA_CUNG_CAP_HHDV {
        chuoi ma_ncc "dạng aabbb, chỉ có sau khi phê duyệt"
        chuoi ten_ncc "duy nhất"
        chuoi ten_day_du "tối đa 255 ký tự"
        chuoi ten_viet_tat "tối đa 100 ký tự"
        chuoi loai_ncc "Cá nhân hoặc Doanh nghiệp"
        chuoi nguoi_lien_he "tên người liên hệ"
        chuoi dia_chi_dai_dien "địa chỉ đại diện"
        chuoi email "email"
        chuoi so_dien_thoai "số điện thoại"
        chuoi so_tai_khoan "số tài khoản ngân hàng"
        chuoi ten_tai_khoan "chữ in hoa không dấu"
        chuoi phuong_thuc_thanh_toan "trả trước hoặc trả sau"
        boolean hoa_don_tai_chinh "có hoặc không"
        chuoi san_pham_dich_vu_mua_vao "sản phẩm dịch vụ mua vào"
        chuoi thoi_diem_tinh_han_thanh_toan "chỉ khi trả sau"
        so so_ngay_thanh_toan "chỉ khi trả sau, số dương"
        chuoi ngay_chot_cong_no "1-31 hoặc Cuối tháng, chỉ khi trả sau"
        so so_ngay_giao_hang "mặc định 5, cố định"
        chuoi link_hoa_don_dien_tu "URL cổng tra cứu hoá đơn điện tử"
        chuoi ghi_chu "ghi chú"
        chuoi anh_dai_dien "ảnh đại diện"
        chuoi trang_thai "theo lưu đồ trạng thái chung"
    }

    KHACH_HANG_DK05 {
        chuoi ma_kh "dạng DK05xxxxx, chỉ có sau khi phê duyệt"
        chuoi ten_khach_hang "duy nhất"
        chuoi dia_chi "địa chỉ"
        chuoi email "email"
        chuoi so_dien_thoai "số điện thoại"
        chuoi nguoi_lien_he "tên người liên hệ"
        chuoi so_tai_khoan "số tài khoản ngân hàng"
        chuoi ten_tai_khoan "chữ in hoa không dấu"
        chuoi loai_khach_hang "Cá nhân hoặc Doanh nghiệp (Pháp nhân)"
        chuoi cccd_cmt "chỉ khi cá nhân"
        chuoi ma_so_thue "chỉ số"
        chuoi nguoi_dai_dien "chỉ khi doanh nghiệp"
        chuoi phuong_thuc_thanh_toan "trả trước hoặc trả sau"
        chuoi san_pham_dich_vu_ban_ra "sản phẩm dịch vụ bán ra"
        chuoi ghi_chu "ghi chú"
        chuoi trang_thai "theo lưu đồ trạng thái chung"
    }

    XE_KHACH_HANG {
        chuoi bien_so_xe "duy nhất"
        chuoi lai_xe "tên lái xe"
        so nam_san_xuat "không quá năm nay"
        chuoi nha_san_xuat "nhà sản xuất"
        chuoi ghi_chu "ghi chú"
        chuoi trang_thai "theo lưu đồ trạng thái chung"
    }

    LOAI_PHUONG_TIEN {
        chuoi ten_loai "8 giá trị trong dropdown"
    }

    MA_PHUONG_TIEN {
        chuoi ma_loai "00 đến 38"
        chuoi ten_phuong_tien "tên phương tiện"
    }

    CHI_NHANH_DELTA {
        chuoi ten_chi_nhanh "6 giá trị"
        chuoi ma_viet_tat "HN, VT, BN, SG"
    }

    NGAN_HANG {
        chuoi ten_ngan_hang "33 giá trị"
    }

    CHUNG_TU_NCC {
        chuoi ten_file "JPG, PNG, PDF"
    }

    YEU_CAU_CAP_MOI {
        chuoi loai_danh_muc "NCC, KH hoặc Xe"
        chuoi trang_thai "Chờ phê duyệt, Đã phê duyệt, Đã từ chối, Đã huỷ"
        chuoi ly_do_tu_choi "không bắt buộc"
    }

    LICH_SU_HOAT_DONG {
        chuoi tai_khoan "tên tài khoản thực hiện"
        chuoi thoi_gian "hh:mm dd/mm/yyyy"
        chuoi noi_dung "đã tạo, đã huỷ, đã phê duyệt, đã từ chối"
        chuoi ly_do "chỉ khi từ chối"
    }

    THONG_BAO {
        chuoi tieu_de "ví dụ Nhà cung cấp HHDV - Yêu cầu cấp mới"
        chuoi noi_dung "đang chờ phê duyệt, đã bị huỷ, đã được phê duyệt, đã bị từ chối"
    }

    NGUOI_DUNG {
        chuoi tai_khoan "tài khoản người dùng"
    }
```

## Entity Reference

| Entity | Mô tả nghiệp vụ | Thuộc tính chính | Nguồn | Nhãn |
|---|---|---|---|---|
| NHA_CUNG_CAP_HHDV | Nhà cung cấp hàng hoá dịch vụ; Danh mục | Mã NCC (aabbb, sau phê duyệt), tên (duy nhất), tên đầy đủ, tên viết tắt, loại, liên hệ, ngân hàng, phương thức thanh toán, hoá đơn tài chính, 3 trường trả sau, số ngày giao hàng, link HĐĐT, trạng thái | SRS Web tr.468 — UC03.07.02 Xem thông tin nhà cung cấp HHDV; SRS Web tr.475 — UC03.07.03 Tạo đề xuất tạo mới nhà cung cấp HHDV | ✅ |
| KHACH_HANG_DK05 | Khách hàng; Danh mục | Mã DK05xxxxx (sau phê duyệt), tên (duy nhất), loại, MST, CCCD/CMT (cá nhân), người đại diện (doanh nghiệp), ngân hàng, phương thức thanh toán, sản phẩm bán ra, trạng thái | SRS Web tr.512 — UC03.08.02; SRS Web tr.518 — UC03.08.03 | ✅ |
| XE_KHACH_HANG | Xe thuộc khách hàng; Danh mục | Biển số (duy nhất), lái xe, loại và mã phương tiện, năm sản xuất, nhà sản xuất, trạng thái | SRS Web tr.550 — UC03.09.02 Xem thông tin xe của khách hàng; SRS Web tr.556 — UC03.09.03 | ✅ |
| YEU_CAU_CAP_MOI | Yêu cầu thay đổi (ChangeRequest): đề xuất tạo mới bản ghi danh mục; có thể trùng với chính bản ghi danh mục (OQ-1) | Loại danh mục, trạng thái, lý do từ chối | SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục; SRS Web tr.495 — UC03.07.05 | 🟡 |
| LICH_SU_HOAT_DONG | Nhật ký thao tác; Khác | Tài khoản, thời gian, nội dung, lý do | SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động | ✅ |
| THONG_BAO | Thông báo trong ứng dụng; Khác | Tiêu đề, nội dung, đích điều hướng | SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động | ✅ |
| CHUNG_TU_NCC | Tệp chứng từ của nhà cung cấp; Khác | Tên file, tải xuống, xoá | SRS Web tr.481 — UC03.07.03 | ✅ |
| LOAI_PHUONG_TIEN, MA_PHUONG_TIEN | Danh mục loại và mã/tên phương tiện | 8 loại; 39 dòng mã 00 đến 38 | SRS Web tr.556 — UC03.09.03; SRS Web tr.560 — UC03.09.03 | ✅ |
| CHI_NHANH_DELTA | Danh sách chi nhánh Delta ký hợp đồng; mã viết tắt cho 4 chi nhánh | Tên chi nhánh, HN/VT/BN/SG | SRS Web tr.480 — UC03.07.03; SRS Web tr.499 — UC03.07.05 | 🟡 |
| NGAN_HANG | Danh sách ngân hàng chọn | 33 ngân hàng | SRS Web tr.478 — UC03.07.03 | ✅ |
| NGUOI_DUNG | Người thực hiện hành động, người tạo yêu cầu, người nhận thông báo | Tài khoản | SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động | 🔵 |

## Quan hệ

| Từ | Đến | Bản số | Ý nghĩa | Nguồn | Nhãn |
|---|---|---|---|---|---|
| KHACH_HANG_DK05 | XE_KHACH_HANG | 1-n | Khách hàng sở hữu nhiều xe; mỗi xe có một khách hàng sở hữu (bắt buộc) | SRS Web tr.512 — UC03.08.02; SRS Web tr.555 — UC03.09.03 | ✅ |
| NHA_CUNG_CAP_HHDV | CHI_NHANH_DELTA | n-1 | NCC ký hợp đồng với một chi nhánh Delta (bắt buộc) | SRS Web tr.480 — UC03.07.03 | ✅ |
| NHA_CUNG_CAP_HHDV | CHUNG_TU_NCC | 1-n | NCC đính kèm chứng từ (bắt buộc ít nhất một, số lượng tối đa nguồn không nói) | SRS Web tr.481 — UC03.07.03 | 🟡 |
| NHA_CUNG_CAP_HHDV, KHACH_HANG_DK05 | NGAN_HANG | n-0..1 | Chọn một ngân hàng trong danh sách (không bắt buộc) | SRS Web tr.478 — UC03.07.03; SRS Web tr.520 — UC03.08.03 | ✅ |
| XE_KHACH_HANG | LOAI_PHUONG_TIEN, MA_PHUONG_TIEN | n-1 | Mỗi xe chọn một loại và một mã/tên thuộc loại đó | SRS Web tr.556 — UC03.09.03 | ✅ |
| LOAI_PHUONG_TIEN | MA_PHUONG_TIEN | 1-n | Mã phương tiện lọc theo loại | SRS Web tr.556 — UC03.09.03; SRS Web tr.560 — UC03.09.03 | ✅ |
| YEU_CAU_CAP_MOI | LICH_SU_HOAT_DONG | 1-n | Mỗi hành động tạo/huỷ/phê duyệt/từ chối ghi một dòng | SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động | ✅ |
| YEU_CAU_CAP_MOI | THONG_BAO | 1-n | Mỗi hành động sinh thông báo tới nhóm người dùng tương ứng | SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động | ✅ |
| NGUOI_DUNG | YEU_CAU_CAP_MOI | 1-n | Người tạo yêu cầu; nhận thông báo khi phê duyệt/từ chối | SRS Web tr.460 — 03.07 Thông báo & Lịch sử hoạt động | ✅ |

## Notes

- Nguồn không ghi bảng nào đối chiếu giữa yêu cầu cấp mới và bản ghi danh mục (OQ-1); ERD vẽ YEU_CAU_CAP_MOI riêng để thể hiện vòng đời đề xuất, trạng thái cũng được gắn trên từng danh mục vì nguồn ghi "bản ghi" có trạng thái.
- Các danh sách chọn (ngân hàng, chi nhánh, loại, phương thức thanh toán) nguồn không nói được quản lý ở đâu nên mô hình hoá là danh sách cố định; phương thức thanh toán, loại NCC/KH, thời điểm tính hạn chỉ là giá trị trong bảng thuộc tính.
- Không đưa ra tên cột kỹ thuật thật; mọi thuộc tính lấy từ tên trường nghiệp vụ trên màn hình.
