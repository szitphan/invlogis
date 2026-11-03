---
type: research
feature: fleetio-saas-platform
primary_device: desktop
stage: flow-approved
updated: 2026-11-03
---

# Nền tảng SaaS — User flow

`stage` ghi theo lựa chọn của user: tự chốt, xem ở bản cuối (02/11/2026). Các màn số 2.2 trở đi và 3.2 trở đi thêm sau lượt chạy 03/11/2026, chưa qua duyệt.

## 1. Sơ đồ tổng

```mermaid
flowchart TD
    s["Đăng nhập"]
    a["1.1 Trang đầu"]
    b["Danh sách đã lọc"]
    c["Chi tiết bản ghi"]
    e2["E-002 Không có kết quả để hiện"]
    d["2.1 Báo cáo"]
    d2["2.2 Báo cáo Sự cố"]
    d3["2.3 Hỏi dữ liệu"]
    d4["2.4 Hộp chia sẻ báo cáo"]
    d5["2.5 Báo cáo đã chia sẻ"]
    e10["E-010 Lối thu hồi trong hộp không tác dụng"]
    e12["E-012 Số sai không báo lỗi"]
    e13["E-013 Link công khai sinh ngay"]
    e["Cài đặt"]
    e1["E-001 Bạn không có quyền thực hiện thao tác này"]
    f["4.1 Cài đặt bảo dưỡng"]
    g["4.2 Tập bản ghi"]
    g3["4.3 Điều kiện tập bản ghi"]
    h["3.3 Danh sách tự động hoá"]
    i["3.1 Trình dựng tự động hoá"]
    t["3.2 Thư viện mẫu tự động hoá"]
    k["3.4 Chi tiết tự động hoá"]
    r["3.5 Lịch sử lượt chạy"]
    q["3.6 Kết quả một lượt chạy"]
    q2["3.7 Lượt chạy tự kích hoạt"]
    m["3.8 Tự động hoá đã lưu trữ"]
    n["3.9 Comment do tự động hoá tạo"]
    l1["5.1 Liên hệ không truy cập"]
    l2["5.2 Menu thao tác xe"]
    l3["5.3 Danh sách thu hồi hãng"]
    l4["5.4 Đặt xe dùng chung"]
    l5["5.5 Kho tài liệu"]
    e3["E-003 Hết hạn mức xe"]
    e6["E-006 Liên hệ chưa là Operator"]
    z["Xong"]
    s -->|"Đăng nhập"| a
    a -->|"Bấm số trên thẻ"| b
    b -->|"Mở dòng"| c
    b -->|"Không có dữ liệu"| e2
    e2 -.->|"Bỏ lọc"| b
    c -->|"Kết thúc"| z
    a -->|"Báo cáo"| d
    d -->|"Mở báo cáo"| d2
    d2 -->|"Chia sẻ"| e13
    e13 -->|"Hiện hộp"| d4
    d4 -->|"Bấm lối trong hộp"| e10
    e10 -->|"Vào đúng lối"| d5
    d4 -->|"Đóng"| z
    d5 -->|"Thu hồi"| z
    d2 -->|"Kết thúc"| z
    d -->|"Kết thúc"| z
    a -->|"Hỏi dữ liệu"| d3
    d3 -->|"Số lệch dữ liệu thật"| e12
    e12 -->|"Đối chiếu tay"| c
    d3 -->|"Kết thúc"| z
    a -->|"Cài đặt"| e
    e -->|"Cài đặt bảo dưỡng"| f
    e -->|"Tập bản ghi"| g
    g -->|"Thêm tập bản ghi"| g3
    g3 -.->|"Huỷ"| g
    e -->|"Tự động hoá"| h
    f -->|"Lưu"| z
    g -->|"Kết thúc"| z
    h -->|"Thêm tự động hoá"| i
    h -->|"Duyệt mẫu"| t
    t -->|"Áp dụng"| i
    i -.->|"Lưu"| k
    h -->|"Mở dòng"| k
    k -->|"Lịch sử lượt chạy"| r
    r -->|"Mở lượt"| q
    r -->|"Lượt do tự động hoá gây ra"| q2
    q -.->|"Quay lại"| r
    q2 -.->|"Quay lại"| r
    q -->|"Mở bản ghi"| n
    n -->|"Kết thúc"| z
    k -->|"Lưu trữ"| m
    m -.->|"Khôi phục"| k
    h -->|"Kết thúc"| z
    e -->|"Không đủ quyền"| e1
    e1 -->|"Xin quyền"| z
    a -->|"Liên hệ"| l1
    l1 -->|"Gán xe khi chưa là Operator"| e6
    e6 -.->|"Tick Operator"| l1
    l1 -->|"Kết thúc"| z
    a -->|"Xe"| l2
    l2 -->|"Thêm xe khi hết hạn mức"| e3
    e3 -->|"Dừng"| z
    l2 -->|"Kết thúc"| z
    a -->|"Thu hồi hãng"| l3
    l3 -->|"Kết thúc"| z
    a -->|"Đặt xe"| l4
    l4 -->|"Kết thúc"| z
    a -->|"Tài liệu"| l5
    l5 -->|"Kết thúc"| z
```

Bản vẽ trên Figma: trang `Research · Fleetio`, frame `7214:221842`, chưa có các màn thêm sau 03/11/2026. Đường liền là luồng thường, nét đứt là quay lại.

## 2. Màn hình

| # | Màn | Slug | Trạng thái | Ảnh |
|---|---|---|---|---|
| 1.1 | Trang đầu | dashboard | Có dữ liệu | Có |
| 2.1 | Báo cáo chuẩn | reports | Có dữ liệu | Có |
| 3.1 | Trình dựng tự động hoá | automation-builder | Mới | Có |
| 4.1 | Maintenance Settings | maintenance-settings | Mặc định | Có |
| 4.2 | Record Sets | record-sets | Mặc định | Có |
| 2.2 | Báo cáo Sự cố | report-issues | Có dữ liệu | Có |
| 2.3 | Hỏi dữ liệu | ai-analyst-issues | Có dữ liệu | Có |
| 2.4 | Hộp chia sẻ báo cáo | report-share-dialog | Có link | Không có ảnh |
| 2.5 | Báo cáo đã chia sẻ | reports-shared | Có dữ liệu, Empty | Không có ảnh |
| 3.2 | Thư viện mẫu tự động hoá | automation-templates | Có dữ liệu | Có |
| 3.3 | Danh sách tự động hoá | automation-list-data | Có dữ liệu | Có |
| 3.4 | Chi tiết tự động hoá | automation-detail | Có dữ liệu | Có |
| 3.5 | Lịch sử lượt chạy | automation-run-history | Có dữ liệu | Có |
| 3.6 | Kết quả một lượt chạy | automation-run-result | Có dữ liệu | Có |
| 3.7 | Lượt chạy tự kích hoạt | automation-self-trigger-runs | Có dữ liệu | Có |
| 3.8 | Tự động hoá đã lưu trữ | automation-archived | Chỉ đọc | Có |
| 3.9 | Comment do tự động hoá tạo | automation-comment-result | Có dữ liệu | Có |
| 4.3 | Điều kiện tập bản ghi | record-set-conditions | Mới | Có |
| 5.1 | Liên hệ không truy cập | contact-no-access | Có dữ liệu | Có |
| 5.2 | Menu thao tác xe | vehicle-more-actions | Mở menu | Có |
| 5.3 | Danh sách thu hồi hãng | recalls-list | Có dữ liệu | Có |
| 5.4 | Đặt xe dùng chung | motor-pool-reservations | Empty | Có |
| 5.5 | Kho tài liệu | documents-empty | Empty | Có |
