---
type: research
feature: fleetio-parts-purchasing-fuel
primary_device: desktop
stage: flow-approved
updated: 2026-11-03
---

# Phụ tùng, mua hàng, nhiên liệu — User flow

`stage` ghi theo lựa chọn của user: tự chốt, xem ở bản cuối (02/11/2026).

## 1. Sơ đồ tổng

```mermaid
flowchart TD
    menu["Menu bên"]
    a["Danh sách đơn mua, chưa chụp"]
    b["2.3 Form đơn mua"]
    e1["E-001 Chọn nhà cung cấp và vị trí kho trước"]
    e2["E-002 Không có quyền ở vị trí kho nào"]
    e11["E-011 Dòng trùng"]
    c["Form thêm nhà cung cấp, chưa chụp"]
    d["2.1 Đơn mua"]
    rej["Đã từ chối"]
    e6["2.4 Hộp nhận hàng"]
    rwo["2.5 Hộp nhận vào lệnh có sẵn"]
    q{"Nhận đủ?"}
    pe["2.6 Sửa đơn đã nhận một phần"]
    ma["2.7 Hộp điều chỉnh số nhận"]
    pc["2.8 Đơn đã đóng khi nhận thiếu"]
    cls["Đã đóng"]
    wo["Sửa chữa · Lệnh sửa chữa"]
    v["2.2 Nhà cung cấp"]
    g["Danh sách phụ tùng, chưa chụp"]
    h["1.1 Phụ tùng"]
    i["1.2 Hoạt động kho"]
    adj["1.3 Hộp điều chỉnh tồn"]
    trf["1.4 Hộp chuyển kho"]
    i2["1.5 Sổ kho đủ loại"]
    bulk["1.6 Cập nhật phụ tùng hàng loạt"]
    e3["E-003 Tồn âm, không báo"]
    e8["E-008 Chuyển quá tồn bị cắt"]
    e10["E-010 Không tắt được kho khi có đơn"]
    j["3.2 Lịch sử dầu"]
    j2["3.3 Lịch sử dầu có cảnh báo dung tích"]
    k["Form phiếu dầu"]
    e19["3.4 E-019 Lỗi lùi ngày, số đồng hồ cao"]
    l["3.1 Phiếu dầu"]
    e4["E-004 Xe km, lít nhưng hiện mpg"]
    pah["2.9 Hộp điều chỉnh từ đơn đã đóng"]
    prh["2.10 Lịch sử bản ghi đơn"]
    pep["2.11 Sửa đơn đã mua"]
    ppdf["2.12 PDF đơn mua"]
    fs["2.13 Tìm xưởng"]
    ws["1.7 PDF phiếu kiểm kê"]
    jf["3.5 Lọc dầu theo loại cảnh báo"]
    z["Xong"]
    menu -->|"Đơn mua"| a
    menu -->|"Nhà cung cấp"| v
    menu -->|"Phụ tùng"| g
    menu -->|"Lịch sử dầu"| j
    a -->|"Thêm đơn mua"| b
    b -->|"Thêm dòng, chưa chọn đủ"| e1
    e1 -.->|"Chọn đủ"| b
    b -->|"Không có quyền kho"| e2
    e2 -->|"Xin quyền"| z
    b -->|"Dòng trùng"| e11
    e11 -.->|"Gộp dòng"| b
    b -->|"Tạo mới trong ô Nhà cung cấp"| c
    c -.->|"Lưu"| b
    b -->|"Lưu"| d
    d -->|"Từ chối"| rej
    rej -->|"Gửi lại chưa chạy"| z
    d -->|"Duyệt, đánh dấu đã mua, nhận hàng"| e6
    e6 -->|"Lưu"| q
    q -.->|"Một phần"| d
    q -->|"Đủ"| cls
    e6 -->|"Nhận vào lệnh đang có"| rwo
    rwo -->|"Mở form lệnh"| wo
    d -->|"Sửa khi đã nhận một phần"| pe
    pe -.->|"Lưu"| d
    cls -->|"Điều chỉnh số nhận"| ma
    ma -.->|"Giảm, về một phần"| d
    d -->|"Đóng khi nhận thiếu"| pc
    pc -->|"Điều chỉnh từ đơn đã đóng"| pah
    cls -->|"Điều chỉnh từ đơn đã đóng"| pah
    pah -.->|"Lưu, vẫn đã đóng"| cls
    d -->|"Lịch sử bản ghi"| prh
    prh -.->|"Đóng hộp"| d
    d -->|"Sửa khi đã mua"| pep
    pep -.->|"Lưu"| d
    d -->|"In"| ppdf
    ppdf -->|"Kết thúc"| z
    d -->|"Sao chép"| b
    v -->|"Tìm xưởng"| fs
    fs -.->|"Huỷ"| v
    bulk -->|"In phiếu kiểm kê"| ws
    ws -->|"Kết thúc"| z
    j -->|"Lọc theo loại cảnh báo"| jf
    jf -->|"Mở dòng"| l
    pc -->|"Kết thúc"| z
    cls -->|"Đóng"| z
    v -->|"Kết thúc"| z
    g -->|"Mở dòng"| h
    g -->|"Cập nhật hàng loạt"| bulk
    bulk -->|"Sửa số, tự lưu"| i2
    bulk -->|"Tắt kho khi có đơn"| e10
    e10 -.->|"Giữ nguyên"| bulk
    h -->|"Hoạt động"| i
    h -->|"Điều chỉnh"| adj
    h -->|"Chuyển kho"| trf
    adj -->|"Lưu"| i2
    trf -->|"Lưu"| i2
    trf -->|"Số lớn hơn tồn"| e8
    e8 -->|"Đọc sổ"| i2
    i2 -->|"Kết thúc"| z
    i -->|"Xuất quá tồn"| e3
    e3 -->|"Nhận thêm"| z
    i -->|"Kết thúc"| z
    j -->|"Thêm phiếu dầu"| k
    j -->|"Mở dòng"| l
    j -->|"Xem cảnh báo"| j2
    j2 -->|"Mở dòng"| l
    k -->|"Lưu"| l
    k -->|"Lùi ngày, số cao"| e19
    e19 -.->|"Sửa số hoặc Void"| k
    l -->|"Xem tiêu hao"| e4
    e4 -->|"Kết thúc"| z
    l -->|"Kết thúc"| z
```

Bản vẽ trên Figma: trang `Research · Fleetio`, frame `7214:221572`, vẽ theo bản 02/11/2026, chưa có các màn thêm ngày 03/11/2026. Đường liền là luồng thường, nét đứt là quay lại.

## 2. Màn hình

| # | Màn | Slug | Trạng thái | Ảnh |
|---|---|---|---|---|
| 1.1 | Chi tiết phụ tùng | part-detail | Có tồn | Có |
| 1.2 | Sổ kho | inventory-activity | 3 dòng | Có |
| 2.3 | Form đơn mua | po-new | Trống | Có |
| 2.1 | Chi tiết đơn | po-detail | Received, Full | Có |
| 2.2 | Danh sách nhà cung cấp | vendors | Có dữ liệu | Có |
| 3.1 | Chi tiết phiếu dầu | fuel-entry | Có tiêu hao | Có |
| 3.2 | Danh sách dầu | fuel-list | Có dữ liệu | Có |
| 1.3 | Hộp điều chỉnh tồn | part-adjust-dialog | Có số | Có |
| 1.4 | Hộp chuyển kho | part-transfer-dialog | Có số | Có |
| 1.5 | Sổ kho đủ loại biến động | inventory-activity-adjust-transfer | Nhiều loại | Có |
| 1.6 | Cập nhật phụ tùng hàng loạt | parts-bulk-manage | Tab theo kho | Có |
| 2.4 | Hộp nhận hàng | po-receive-dialog | Nhận một phần | Có |
| 2.5 | Hộp nhận vào lệnh có sẵn | po-receive-existing-wo | Chọn lệnh | Có |
| 2.6 | Sửa đơn đã nhận một phần | po-edit-received-partial | Khoá nhà cung cấp, kho | Có |
| 2.7 | Hộp điều chỉnh số nhận | po-make-adjustment | Có số âm | Có |
| 2.8 | Đơn đã đóng khi nhận thiếu | po-closed-partial | Closed, thiếu | Có |
| 3.3 | Lịch sử dầu có cảnh báo dung tích | fuel-history-capacity-alert | Có cảnh báo | Có |
| 3.4 | Lỗi lùi ngày, số đồng hồ cao | fuel-entry-odometer-backdate-error | Lỗi | Có |
| 2.9 | Hộp điều chỉnh từ đơn đã đóng | po-adjust-closed | Closed, chưa tick | Có |
| 2.10 | Lịch sử bản ghi đơn | po-record-history | Có dữ liệu | Có |
| 2.11 | Sửa đơn đã mua | po-edit-purchased | Purchased, khoá nhà cung cấp, kho | Có |
| 2.12 | PDF đơn mua | po-print-pdf | Approved sau khi bỏ đã mua | Có, đã che dòng địa chỉ |
| 3.5 | Lọc dầu theo loại cảnh báo | fuel-filter-alert-type | Lọc Fuel Capacity Alert | Có |
| 2.13 | Tìm xưởng | vendors-find-shops | Có kết quả | Không, không lưu vì có địa chỉ thật |
| 1.7 | PDF phiếu kiểm kê | parts-worksheet-pdf | Theo kho đang chọn | Không, không lưu vì có địa chỉ tài khoản |

## 3. Flow theo tác vụ

| Flow | Happy path | Nhánh lỗi, ngoại lệ |
|---|---|---|
| Mua | Danh sách → form → 2.1 → hộp nhận 2.4 → Close | E-fleetio-parts-purchasing-fuel-001; E-fleetio-parts-purchasing-fuel-011; E-fleetio-parts-purchasing-fuel-012; từ chối |
| Sửa khi đã mua, lùi | 2.1 → 2.11 → 2.1; Unmark về Approved | E-fleetio-parts-purchasing-fuel-026; sửa Draft: E-fleetio-parts-purchasing-fuel-032; sửa Full: E-fleetio-parts-purchasing-fuel-033 |
| Sao chép, in, lịch sử | 2.1 → form đơn mới; 2.1 → 2.12; 2.1 → 2.10 | E-fleetio-parts-purchasing-fuel-030 |
| Tìm xưởng | 2.2 → 2.13 | Add Vendor không bấm |
| Nhận vào lệnh | 2.1 → 2.5 → form lệnh | Huỷ form: hàng ở lại kho; E-fleetio-parts-purchasing-fuel-013; E-fleetio-parts-purchasing-fuel-014 |
| Trả, đóng | 2.1 → 2.7 → 2.1 → 2.8; đã đóng → 2.9 | E-fleetio-parts-purchasing-fuel-015; E-fleetio-parts-purchasing-fuel-025; E-fleetio-parts-purchasing-fuel-027 |
| Sửa sau nhận | 2.1 → 2.6 → 2.1 | Nhà cung cấp, kho khoá; không thêm bớt dòng |
| Tồn | 1.1 → 1.2 | E-fleetio-parts-purchasing-fuel-002 |
| Chỉnh, chuyển | 1.1 → 1.3 hoặc 1.4 → 1.5 | E-fleetio-parts-purchasing-fuel-007; E-fleetio-parts-purchasing-fuel-008 |
| Kiểm kê | Danh sách → 1.6 → 1.5; 1.6 → 1.7 | E-fleetio-parts-purchasing-fuel-010; E-fleetio-parts-purchasing-fuel-029 |
| Dầu | 3.2 → form → 3.1 → 3.3 | E-fleetio-parts-purchasing-fuel-004; E-fleetio-parts-purchasing-fuel-016; E-fleetio-parts-purchasing-fuel-017; E-fleetio-parts-purchasing-fuel-018; E-fleetio-parts-purchasing-fuel-019 tại 3.4; E-fleetio-parts-purchasing-fuel-020 |
| Đối soát dầu | 3.2 → 3.5 → 3.1 | E-fleetio-parts-purchasing-fuel-020; E-fleetio-parts-purchasing-fuel-028 |
