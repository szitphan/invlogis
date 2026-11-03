---
type: research
feature: fleetio-tires
primary_device: desktop
stage: flow-approved
updated: 2026-11-03
---

# Quản lý lốp — User flow

`stage` ghi theo lựa chọn của user: tự chốt, xem ở bản cuối (03/11/2026).

## 1. Sơ đồ tổng

```mermaid
flowchart TD
    root["Menu bên, Vehicles"]
    menu["Trang xe, tab Tire Management"]
    a["1.1 Chưa khai trục"]
    b["1.2 Trình hướng dẫn"]
    c["1.3 Chọn Axle Type"]
    d["1.4 Đường I know my axle configuration"]
    e["1.5 Danh sách cấu hình"]
    f["1.6 Sơ đồ đầu kéo 6x4"]
    g["1.7 Sơ đồ mooc 3 trục"]
    h["2.1 Lắp lốp"]
    i["2.2 Sơ đồ đã có lốp"]
    j["2.3 Sửa lốp"]
    k["2.4 Mooc 12 lốp, Spare"]
    l["3.1 Đảo lốp"]
    m["3.2 Kết quả đảo, Undo"]
    n["3.3 Lỗi thiếu tên mẫu"]
    o["4.1 Tháo lốp"]
    p["5.1 Đọc lốp, trống"]
    q["5.2 Đọc lốp, có dữ liệu"]
    r["5.3 Lọc Warning"]
    s["5.4 Biên mức gai"]
    t["5.5 Lịch sử lốp"]
    e1["E-002 Edit khoá khi còn lốp"]
    e2["E-006 Ô đã có lốp bị xám"]
    e3["E-003 Nút đảo tắt khi chưa khép kín"]
    side["Danh sách Tire Readings"]
    KetThuc["Xong"]
    root -->|"Vehicle List, mở xe"| menu
    root -->|"Tire Readings"| side
    menu -->|"Xe chưa khai trục"| a
    a -->|"Set up axle configuration"| b
    b -->|"Vehicle, chọn số vị trí"| c
    b -->|"I know my axle configuration"| d
    d -->|"Mở ô chọn"| e
    c -->|"Lưu đầu kéo"| f
    e -->|"Lưu đầu kéo"| f
    b -->|"Trailer, lưu"| g
    e -->|"Lưu mooc"| g
    f -->|"Sửa cấu hình khi có lốp"| e1
    e1 -.->|"Tháo hết"| o
    f -->|"Bấm ô cộng, Add"| h
    g -->|"Bấm ô cộng, Add"| h
    h -->|"Chọn ô đã có lốp"| e2
    e2 -.->|"Chọn ô khác"| h
    h -->|"Lưu đầu kéo"| i
    h -->|"Lưu mooc"| k
    i -->|"Bấm lốp"| j
    k -->|"Bấm lốp"| j
    j -.->|"Lưu"| i
    i -->|"Rotate Tires"| l
    k -->|"Rotate Tires"| l
    l -->|"Chưa khép kín"| e3
    e3 -.->|"Ghép thêm"| l
    l -->|"Tick lưu mẫu, trống tên"| n
    n -.->|"Nhập tên"| l
    l -->|"Đảo"| m
    m -.->|"Undo Rotation"| l
    m -.->|"Close"| i
    i -->|"Remove, Remove All"| o
    j -->|"Remove"| o
    o -.->|"Xác nhận"| i
    i -->|"Tab Tire Activity"| t
    side -->|"Chưa có lốp"| p
    side -->|"Có lốp"| q
    q -->|"Lọc Tread Depth Health"| r
    q -->|"Xem theo mức"| s
    p -->|"Kết thúc"| KetThuc
    r -->|"Kết thúc"| KetThuc
    s -->|"Kết thúc"| KetThuc
    t -->|"Kết thúc"| KetThuc
```

Trên Figma: frame `Userflow · Fleetio · Quản lý lốp`. Đường liền là luồng thường, nét đứt là quay lại. Đọc lốp qua phiếu kiểm đi qua nhóm Nhắc, kiểm tra, xem Mục "Màn liên quan".

## 2. Màn

| # | Màn | Slug | Trạng thái | Ảnh |
|---|---|---|---|---|
| 1.1 | Lốp, chưa khai trục | tire-management-empty | Trống | Có |
| 1.2 | Trình hướng dẫn cấu hình trục | axle-setup-step1 | 3 khối gập | Có |
| 1.3 | Chọn Axle Type | axle-setup-axle-type | Đang chọn | Có |
| 1.4 | Đường đã biết cấu hình | axle-setup-known | Đang chọn | Có |
| 1.5 | Danh sách cấu hình trục | axle-config-options | Ô chọn mở | Có |
| 1.6 | Sơ đồ đầu kéo 6x4 | tire-management-6x4 | Ô trống | Có |
| 1.7 | Sơ đồ mooc 3 trục | tire-management-trailer | Ô trống | Có |
| 2.1 | Lắp lốp | tire-install | Form | Có |
| 2.2 | Sơ đồ đã có lốp | tire-management-installed | Có dữ liệu | Có |
| 2.3 | Sửa lốp | tire-edit | Form | Có |
| 2.4 | Mooc đủ 12 lốp và Spare | tire-management-trailer-12-spare | Có dữ liệu, đủ 3 mức | Có |
| 3.1 | Đảo lốp | tire-rotate | Mẫu Standard 6x4 | Có |
| 3.2 | Kết quả đảo | tire-rotate-result-undo | Thành công, có Undo | Có |
| 3.3 | Đảo lốp, thiếu tên mẫu | tire-rotate-name-required | Lỗi | Có |
| 4.1 | Tháo lốp | tire-remove | Hộp xác nhận | Có |
| 5.1 | Đọc lốp | tire-readings | Trống | Có |
| 5.2 | Đọc lốp có dữ liệu | tire-readings-data | Có dữ liệu | Có |
| 5.3 | Đọc lốp lọc Warning | tire-readings-filter-warning | Đã lọc | Có |
| 5.4 | Đọc lốp, biên mức gai | tire-readings-boundary | Có dữ liệu | Có |
| 5.5 | Lịch sử lốp | tire-activity | Có dữ liệu | Có |

## Màn liên quan

Có ảnh, không đánh số trong nhóm này vì không mang tiền tố `tire-`, `axle-`: `inspection-tire-axle-error`, `inspection-tire-remark-required`, `inspection-tire-fail-summary`, `inspection-tire-fail-detail`, `part-tire-category-fields`. Mô tả ở [[docs/_research/fleetio/srs/fleetio-tires-screens.md|Màn hình]].

Lượt 3 không có ảnh mới của nhóm Lốp, nên Mục 1, 2 không thêm màn. Settings › Tire Management Settings chỉ đọc, chưa chụp. Mooc nối hai xe có ảnh ở màn 1.7 nhóm Phương tiện: `trailer-linked-two-vehicles`.
