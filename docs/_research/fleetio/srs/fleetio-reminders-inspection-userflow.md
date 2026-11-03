---
type: research
feature: fleetio-reminders-inspection
primary_device: desktop
stage: flow-approved
updated: 2026-11-03
---

# Nhắc và kiểm tra — User flow

`stage` ghi theo lựa chọn của user: tự chốt, xem ở bản cuối (02/11/2026).

## 1. Sơ đồ tổng

```mermaid
flowchart TD
    menu["Menu bên"]
    a["1.1 Nhắc bảo dưỡng"]
    b["1.4 Thêm nhắc bảo dưỡng"]
    sn["1.8 Hộp tạm hoãn"]
    d["1.5 Chi tiết nhắc"]
    d2["1.6 Chi tiết nhắc sau khi hoàn thành"]
    c["1.7 Danh sách nhắc kèm tuân thủ"]
    res["1.9 Hộp giải quyết nhắc"]
    pv["1.10 Gán xe vào bộ lịch"]
    rn["1.11 Thêm nhắc gia hạn"]
    se["Sửa chữa · Service Entry"]
    wo["Sửa chữa · Lệnh sửa chữa"]
    p["1.2 Form bộ lịch bảo dưỡng"]
    r["1.3 Nhắc gia hạn"]
    f["2.1 Biểu mẫu kiểm tra"]
    i["2.2 Sửa mục"]
    v["2.15 Xe và lịch của biểu mẫu"]
    wf["2.14 Thêm workflow"]
    l["2.5 Lịch kiểm tra"]
    n["2.6 Form làm phiếu"]
    ax["2.7 Phiếu thiếu cấu hình trục"]
    rm["2.8 Phiếu lốp bắt nhận xét"]
    ts["2.9 Phiếu lốp không đạt, tổng"]
    td["2.10 Phiếu lốp không đạt, từng vị trí"]
    loc["2.11 Phiếu có bản đồ vị trí"]
    pre["2.12 Phiếu đủ mục, vị trí giả lập"]
    na["2.13 Mục lỗi cần xử lý"]
    e7["E-007 Không có vị trí, chỉ cảnh báo"]
    q{"Hợp lệ?"}
    e15["E-001 E-002 E-003 Thiếu ghi chú hoặc giá trị"]
    e4["E-004 Thiếu cấu hình trục"]
    e17["E-017 Biểu mẫu chưa gán xe"]
    e5["E-005 Chưa tick ô không có lỗi"]
    e6["E-006 Không nộp được biểu mẫu kiểm tra"]
    t["2.3 Phiếu kiểm tra"]
    g["2.4 Mục lỗi"]
    ack["Đã ghi nhận"]
    z["Xong"]
    menu -->|"Nhắc bảo dưỡng"| a
    menu -->|"Bộ lịch bảo dưỡng"| p
    menu -->|"Gia hạn"| r
    menu -->|"Biểu mẫu"| f
    menu -->|"Lịch"| l
    a -->|"Thêm nhắc bảo dưỡng"| b
    b -.->|"Lưu"| a
    a -->|"Chọn nhắc"| d
    a -->|"Lọc theo xe"| c
    c -.->|"Bỏ lọc"| a
    d -->|"Tạm hoãn"| sn
    sn -.->|"Hết hạn hoặc Remove Snooze"| d
    d -->|"Resolve"| res
    a -->|"Resolve trên dòng"| res
    res -->|"Thêm vào lệnh sửa chữa"| wo
    res -->|"Ghi lịch sử dịch vụ"| se
    wo -->|"Lệnh Completed"| d2
    se -->|"Lưu"| d2
    d2 -.->|"Kỳ mới"| a
    p -->|"Lưu"| pv
    pv -->|"Lưu"| z
    r -->|"Thêm gia hạn"| rn
    rn -.->|"Lưu"| r
    r -->|"Kết thúc"| z
    f -->|"Sửa mục"| i
    i -.->|"Lưu"| f
    f -->|"Workflow"| wf
    wf -.->|"Lưu"| f
    f -->|"Xe và lịch"| v
    v -->|"Lưu"| l
    l -->|"Bắt đầu kiểm tra"| n
    n -->|"Biểu mẫu chưa gán"| e17
    e17 -.->|"Gán xe"| v
    n -->|"Xe chưa khai trục"| ax
    ax -.->|"Khai trục, Done"| n
    n -->|"Gai dưới mức, thiếu nhận xét"| rm
    rm -.->|"Thêm nhận xét"| n
    n -->|"Trình duyệt không cấp vị trí"| e7
    e7 -.->|"Làm tiếp"| n
    n -->|"Nộp"| q
    q -->|"Đạt"| t
    q -->|"Thiếu ghi chú, giá trị"| e15
    q -->|"Thiếu trục"| e4
    q -->|"Chưa tick"| e5
    e15 -->|"Thông báo"| e6
    e4 -->|"Thông báo"| e6
    e5 -->|"Thông báo"| e6
    e6 -.->|"Sửa lại"| n
    q -->|"Phiếu lốp không đạt"| ts
    q -->|"Có vị trí"| loc
    q -->|"Đủ mục, vị trí giả lập"| pre
    ts -->|"Mở rộng"| td
    td -->|"Sự cố tự sinh"| g
    loc -->|"Kết thúc"| z
    pre -->|"Kết thúc"| z
    t -->|"Mục không đạt, workflow bật"| g
    t -->|"Mục không đạt, workflow tắt"| na
    t -->|"Không có lỗi"| z
    g -->|"Tạo sự cố, lệnh"| wo
    na -->|"Ghi nhận"| ack
    na -->|"Create Issue"| g
    ack -->|"Kết thúc"| z
```

Bản vẽ trên Figma: trang `Research · Fleetio`, frame `7214:221413`, chưa có các màn thêm ở đợt 03/11/2026. Đường liền là luồng thường, nét đứt là quay lại.

## 2. Màn hình

| # | Màn | Slug | Trạng thái | Ảnh |
|---|---|---|---|---|
| 1.1 | Danh sách nhắc | reminders-list | Có dữ liệu | Có |
| 1.4 | Form nhắc | reminder-new | Trống | Có |
| 1.2 | Form bộ lịch | program-new | Trống | Có |
| 1.3 | Danh sách gia hạn | renewals-list | Có dữ liệu | Có |
| 2.1 | Chi tiết biểu mẫu | inspection-form | Có mục | Có |
| 2.2 | Dựng mục | inspection-items-edit | Sửa | Có |
| 2.3 | Trang phiếu | inspection-submission | Có mục lỗi | Có |
| 2.4 | Item Failures | item-failures | Một dòng | Có |
| 2.5 | Lịch kiểm tra | inspection-schedules | Một dòng | Có |
| 1.5 | Chi tiết nhắc | reminder-detail-overdue | Quá hạn | Không |
| 1.6 | Chi tiết nhắc sau khi hoàn thành | reminder-after-work-order | Có lịch sử | Có |
| 1.7 | Danh sách nhắc kèm tuân thủ | reminder-list-compliance | Lọc một xe | Có |
| 1.8 | Hộp tạm hoãn | reminder-snooze | Mở | Không |
| 1.9 | Hộp giải quyết nhắc | reminder-resolve | Thêm vào lệnh, ghi lịch sử | Không |
| 1.10 | Gán xe vào bộ lịch | program-vehicles-add | Có đối chiếu | Không |
| 1.11 | Thêm nhắc gia hạn | renewal-new | Trống | Không |
| 2.6 | Form làm phiếu | inspection-submit-form | Có lỗi từng mục | Không |
| 2.7 | Phiếu thiếu cấu hình trục | inspection-tire-axle-error | Lỗi | Có |
| 2.8 | Phiếu lốp bắt nhận xét | inspection-tire-remark-required | Lỗi | Có |
| 2.9 | Phiếu lốp không đạt, tổng | inspection-tire-fail-summary | Có mục lỗi | Có |
| 2.10 | Phiếu lốp không đạt, từng vị trí | inspection-tire-fail-detail | Mở rộng | Có |
| 2.11 | Phiếu có bản đồ vị trí | inspection-submission-location | Có vị trí | Có |
| 2.12 | Phiếu đủ mục, vị trí giả lập | inspection-pretrip-simulated | Có vị trí | Có |
| 2.13 | Mục lỗi cần xử lý | item-failure-needs-action | Một dòng | Có |
| 2.14 | Thêm workflow | inspection-workflow-add | Trống | Không |
| 2.15 | Xe và lịch của biểu mẫu | inspection-form-vehicles | Một dòng | Không |

Màn ghi "Không" ở cột Ảnh: có mô tả trong ghi chú chạy nhưng không có ảnh lưu lại.

## 3. Flow theo tác vụ

| Flow | Happy path | Nhánh lỗi, ngoại lệ |
|---|---|---|
| Nhắc | 1.1 → 1.4 → 1.5 → 1.9 → lệnh → 1.6 → 1.1 | E-fleetio-reminders-inspection-008, 009, 010; tạm hoãn 1.8; E-fleetio-reminders-inspection-011 đến 014 |
| Tuân thủ | 1.1 → 1.7 | Recalculate xám khi chưa có lịch sử |
| Bộ lịch | 1.2 → 1.10 → xử lý ngầm | Nhắc tay trùng bị thay; gỡ xe chưa bấm |
| Gia hạn | 1.3 → 1.11 → 1.3 | Loại đã có hiện xám; gia hạn là sửa tay |
| Biểu mẫu | 2.1 → 2.2 → 2.14 → 2.15 → 2.5 | E-fleetio-reminders-inspection-017 |
| Kiểm tra | 2.5 → 2.6 → 2.3 hoặc 2.11, 2.12 | E-fleetio-reminders-inspection-001 đến 007, 013, 015, 019; lốp 2.7, 2.8 |
| Lốp | 2.6 → 2.9 → 2.10 → sự cố | Spare không có trong phiếu |
| Lỗi | 2.3 → 2.4 → sự cố → lệnh | Workflow tắt 2.13, ghi nhận không sửa; lỗi lặp gộp; E-fleetio-reminders-inspection-018 |
