---
type: srs-userflow
feature: cross-process-flow
updated: 2026-10-12
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-10-12
flow_hash: "33e60cca"
---

# Liên quy trình — User Flow

> Nguồn chia flow DUY NHẤT cho feature này. `/wireframe-ascii` và `/wireframe-html` đọc file này để biết flow nào gồm những màn nào — KHÔNG tự chia flow riêng.

Thiết bị theo kênh: Người theo dõi quy trình và Người tạo bản ghi dùng web desktop 1920; Lái xe dùng Delta Super App, khung mobile 393. Cột "Thiết bị" ở Mục 3 là nguồn bề rộng khung cho từng flow. Màn chi tiết bản ghi mẫu: Lệnh sửa chữa LSC-0930 (luồng Sửa chữa xe khách hàng). Mọi nghiệp vụ khác hiện dòng quy trình cùng cách.

## 1. User Flow (tổng)

> Phủ happy / error / edge cases. `[n]` = số màn hình đối chiếu Mục 2. Node không đánh số là màn của feature khác hoặc thông báo/popup dùng chung.

### Flow: xem-quy-trinh

```mermaid
flowchart TD
    n1["[1] Màn chi tiết bản ghi<br/>có dòng quy trình"]
    d1{"D1: Bản ghi thuộc quy trình?"}
    x0["Màn chi tiết không có dòng quy trình"]
    dl{"Tải dòng quy trình được?"}
    n2["[2] Dòng quy trình tải lỗi<br/>Không tải được quy trình + Thử lại"]
    n4["[4] Sơ đồ đang tải"]
    dt{"Tải sơ đồ được?"}
    n5["[5] Sơ đồ lỗi<br/>Không tải được sơ đồ + E-common-008 hoặc 009 + Thử lại"]
    n3["[3] Popup sơ đồ<br/>chọn sẵn bước Ở đây, panel mở"]
    pick{"Bước được chọn là gì?"}
    n6["[6] Panel bước chưa tạo"]
    n7["[7] Panel ngã rẽ<br/>các hướng có thể đi"]
    n8["[8] Panel không có quyền<br/>E-common-011 tại chỗ, giữ lý do phát sinh"]
    n9["[9] Panel công nợ<br/>Công nợ tên NCC"]
    n10["[10] Sơ đồ có banner<br/>Quy trình vừa có cập nhật"]
    n30["[30] Dòng quy trình đang tải<br/>skeleton"]
    n31["[31] Panel bước có bản ghi trước<br/>+n bản ghi trước, khối Bản ghi trước đó"]
    n32["[32] Panel, lịch sử tải lỗi<br/>Không tải được lịch sử + Thử lại"]
    gone{"Bản ghi còn không?"}
    n34["[34] Popup E-cross-process-flow-004<br/>bản ghi đã bị xoá"]
    perm{"Còn quyền xem bản ghi?"}
    n33["[33] Popup không có quyền mở<br/>E-common-011 + Đóng"]
    xd["Màn chi tiết bản ghi của bước<br/>ngoài feature"]
    xc["Bảng công nợ đã lọc theo NCC<br/>SRS Thanh toán"]

    n1 --> d1
    d1 -->|"Không"| x0
    d1 -->|"Có"| n30
    n30 --> dl
    dl -->|"Không"| n2
    n2 -.->|"Thử lại"| dl
    dl -->|"Có, bấm dòng quy trình"| n4
    n4 --> dt
    dt -->|"Không"| n5
    n5 -.->|"Thử lại"| n4
    dt -->|"Có"| n3
    n3 -->|"Chọn bước khác"| pick
    pick -->|"Có bản ghi, có quyền"| n3
    pick -->|"Chưa có bản ghi"| n6
    pick -->|"Ngã rẽ chưa chốt"| n7
    pick -->|"Không có quyền"| n8
    pick -->|"Công nợ trả sau"| n9
    pick -->|"Có bản ghi Đã thay thế"| n31
    n31 -.->|"Chọn bước khác"| n3
    n3 -->|"Lịch sử tải lỗi"| n32
    n32 -.->|"Thử lại"| n3
    n6 -.->|"Chọn bước khác"| n3
    n7 -.->|"Chọn bước khác"| n3
    n8 -.->|"Chọn bước khác"| n3
    n9 -->|"Mở bảng công nợ"| xc
    n3 -->|"Thông tin đang hiện đổi ở nơi khác"| n10
    n10 -.->|"Tải lại, giữ bước đang chọn"| n3
    n3 -->|"Mở màn hình chi tiết"| gone
    gone -->|"Đã bị xoá"| n34
    n34 -.->|"Tải lại sơ đồ"| n4
    n34 -.->|"Đóng"| n3
    gone -->|"Còn"| perm
    perm -->|"Có"| xd
    perm -->|"Không"| n33
    n33 -.->|"Đóng, ở lại sơ đồ"| n3
    xd -.->|"Back trình duyệt, popup không mở lại"| n1
    n3 -.->|"Đóng popup"| n1

    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
    class n1,n3,n4,n30,xd happy
    class n2,n5,n32,n33,n34 error
    class x0,n6,n7,n8,n9,n10,n31,xc edge
```

### Flow: tra-cuu-quy-trinh

```mermaid
flowchart TD
    m0["Menu Module - Quy trình"]
    dq{"Có quyền menu Quy trình?"}
    t38["[38] Trang không có quyền<br/>E-common-011 + Về trang chủ"]
    t35["[35] Danh sách đang tải<br/>skeleton 10 cột"]
    t11["[11] Danh sách Quy trình<br/>chỉ chi nhánh được phân quyền"]
    dr{"Có quy trình nào?"}
    t12["[12] Danh sách rỗng"]
    t36["[36] Danh sách tải lỗi<br/>khối lỗi + Thử lại, giữ bộ lọc"]
    ds{"Ô tìm từ 3 ký tự?"}
    dk{"Có kết quả?"}
    t13["[13] Tìm không ra + Xoá bộ lọc"]
    t37["[37] Lọc không ra kết quả<br/>ô tìm trống + Xoá bộ lọc"]
    t14["[14] Danh sách có banner<br/>Danh sách vừa có cập nhật"]
    t15["[15] Popup sơ đồ trên danh sách<br/>chưa chọn bước nào"]
    tp["Chọn bước, panel như flow xem-quy-trinh [3] đến [9]"]
    tv["Màn chi tiết Phương tiện hoặc Xe của khách hàng<br/>ngoài feature"]
    tx["File PDF hoặc Excel<br/>đúng dữ liệu và cột đang thấy"]

    m0 --> dq
    dq -->|"Không, mở thẳng đường dẫn"| t38
    dq -->|"Có"| t35
    t35 --> dr
    dr -->|"Có"| t11
    dr -->|"Chưa có"| t12
    dr -->|"Tải lỗi"| t36
    t36 -.->|"Thử lại"| t35
    t11 -->|"Gõ mã"| ds
    ds -->|"Dưới 3 ký tự, chưa tìm"| t11
    ds -->|"Đủ"| dk
    t11 -->|"Lọc"| dk
    dk -->|"Có"| t11
    dk -->|"Không, có từ khoá"| t13
    dk -->|"Không, ô tìm trống"| t37
    t13 -.->|"Xoá bộ lọc"| t11
    t37 -.->|"Xoá bộ lọc"| t11
    t11 -->|"Thông tin đang hiện đổi ở nơi khác"| t14
    t14 -.->|"Tải lại, giữ bộ lọc"| t11
    t11 -->|"Bấm dòng"| t15
    t15 -->|"Chọn bước"| tp
    t15 -.->|"Đóng popup"| t11
    t11 -->|"Bấm ô Phương tiện"| tv
    t11 -->|"Xuất"| tx

    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
    class m0,t35,t11,t15,tp,tx happy
    class t36,t38 error
    class t12,t13,t14,t37,tv edge
```

### Flow: tao-nghiep-vu-tiep-theo

```mermaid
flowchart TD
    c1["[1] Màn chi tiết bản ghi<br/>dùng chung với xem-quy-trinh"]
    d6{"D6: Đạt trigger và có quyền tạo?"}
    cn["Không hiện nút tạo"]
    cf["Form tạo mới đã điền sẵn<br/>của nghiệp vụ tiếp theo, ngoài feature"]
    cs{"Kết quả gửi"}
    c16["[16] Màn chi tiết bản ghi mới<br/>cây có bước mới, ghim Ở đây"]
    c17["[17] Popup E-cross-process-flow-001<br/>bước đã có yêu cầu khác hoặc đã hoàn thành"]
    c39["[39] Popup E-cross-process-flow-003<br/>bản ghi nguồn vừa bị thu hồi"]
    cdel["Bản nháp đã xoá"]
    ct["Toast E-common-008 hoặc 009, giữ form"]
    cd["Lưu nháp, cây không đổi"]
    ch{"Bản ghi đã có bước con?"}
    c18["[18] Popup E-cross-process-flow-002<br/>không thể thu hồi hoặc xoá"]
    co["Thu hồi hoặc xoá thành công<br/>theo nghiệp vụ, cây cập nhật"]

    c1 --> d6
    d6 -->|"Không"| cn
    d6 -->|"Có, bấm nút Tạo phiếu"| cf
    cf -->|"Gửi"| cs
    cf -->|"Lưu nháp"| cd
    cs -->|"Thành công, bước 1 bản ghi còn trống hoặc bản cũ bị từ chối, thu hồi"| c16
    cs -->|"Thành công, bước nhiều bản ghi thành bước anh em"| c16
    cs -->|"Bước 1 bản ghi đã có yêu cầu đang chờ hoặc đã xong"| c17
    cs -->|"Bản ghi nguồn vừa bị thu hồi"| c39
    cs -->|"Lỗi hệ thống, mất mạng hoặc cây không nhận bước"| ct
    c17 -.->|"Đóng, giữ bản nháp"| cf
    c39 -.->|"Giữ bản nháp"| cf
    c39 -->|"Xoá bản nháp, xác nhận CMP-03"| cdel
    ct -.->|"Gửi lại"| cf
    c1 -->|"Thu hồi hoặc Xoá"| ch
    ch -->|"Có"| c18
    ch -->|"Không"| co
    c18 -.->|"Đóng"| c1

    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
    class c1,cf,c16,co happy
    class c17,c39,ct,c18 error
    class cn,cd,cdel edge
```

### Flow: xem-quy-trinh-mobile

```mermaid
flowchart TD
    a19["[19] Màn chi tiết trên app<br/>có thẻ quy trình"]
    ad1{"Bản ghi thuộc quy trình?"}
    ax0["Không có thẻ quy trình"]
    a40["[40] Thẻ quy trình đang tải<br/>skeleton shimmer"]
    adl{"Tải thẻ được?"}
    a20["[20] Thẻ quy trình tải lỗi + Thử lại"]
    a22["[22] Sheet sơ đồ đang tải"]
    adt{"Tải sơ đồ được?"}
    a23["[23] Sheet sơ đồ lỗi<br/>Không tải được sơ đồ + E-common-008 hoặc 009 + Thử lại"]
    a21["[21] Sheet sơ đồ<br/>cây dọc, đánh dấu Ở đây, không tự mở sheet bước"]
    a24["[24] Sheet sơ đồ có banner<br/>Quy trình vừa có cập nhật"]
    apick{"Bước được chọn là gì?"}
    a25["[25] Sheet bước<br/>lịch sử + Mở màn hình chi tiết khi app có màn"]
    a26["[26] Sheet bước chưa tạo"]
    a27["[27] Sheet ngã rẽ"]
    a28["[28] Sheet công nợ<br/>chỉ trạng thái, không có nút mở"]
    a29["[29] Sheet bước không có quyền<br/>E-common-011, giữ lý do phát sinh"]
    agone{"Bản ghi còn không?"}
    ae4["Sheet lỗi E-cross-process-flow-004<br/>nội dung như [34]"]
    aperm{"Còn quyền xem bản ghi?"}
    agr["Popup chặn E-common-011 theo GR-26"]
    axd["Màn chi tiết bản ghi trên app<br/>ngoài feature"]

    a19 --> ad1
    ad1 -->|"Không"| ax0
    ad1 -->|"Có"| a40
    a40 --> adl
    adl -->|"Không"| a20
    a20 -.->|"Thử lại"| adl
    adl -->|"Có, chạm thẻ"| a22
    a22 --> adt
    adt -->|"Không"| a23
    a23 -.->|"Thử lại"| a22
    adt -->|"Có"| a21
    a21 -->|"Thông tin đang hiện đổi ở nơi khác"| a24
    a24 -.->|"Tải lại, giữ bước đang chọn"| a21
    a21 -->|"Chạm bước"| apick
    apick -->|"Có bản ghi, có quyền"| a25
    apick -->|"Chưa có bản ghi"| a26
    apick -->|"Ngã rẽ chưa chốt"| a27
    apick -->|"Công nợ trả sau"| a28
    apick -->|"Không có quyền"| a29
    a26 -.->|"Đóng sheet bước"| a21
    a27 -.->|"Đóng sheet bước"| a21
    a28 -.->|"Đóng sheet bước"| a21
    a29 -.->|"Đóng sheet bước"| a21
    a25 -.->|"Đóng sheet bước"| a21
    a25 -->|"Mở màn hình chi tiết"| agone
    agone -->|"Đã bị xoá"| ae4
    ae4 -.->|"Tải lại sơ đồ"| a22
    agone -->|"Còn"| aperm
    aperm -->|"Có"| axd
    aperm -->|"Không"| agr
    agr -.->|"Quay lại"| a21
    axd -.->|"Back, sheet đã đóng"| a19
    a21 -.->|"Vuốt xuống đóng sheet"| a19

    classDef happy fill:#d4edda,stroke:#28a745
    classDef error fill:#f8d7da,stroke:#dc3545
    classDef edge fill:#fff3cd,stroke:#ffc107
    class a19,a40,a21,a22,a25,axd happy
    class a20,a23,agr,ae4 error
    class ax0,a24,a26,a27,a28,a29 edge
```

## 2. Danh sách màn hình

| [#] | Slug | Màn hình | Mục đích | Thuộc flow |
|-----|------|----------|----------|------------|
| 1 | ban-ghi-dong-quy-trinh | Màn chi tiết bản ghi có dòng quy trình | Dòng quy trình đầu màn (tên luồng, tiến độ, "Xong x/y bước · n nhánh phát sinh", Bước trước / Phát sinh từ) + nút tạo tiếp theo + Thu hồi/Xoá ở vùng hành động | xem-quy-trinh |
| 2 | ban-ghi-dong-quy-trinh-loi | Dòng quy trình tải lỗi | "Không tải được quy trình." + Thử lại, màn chi tiết vẫn dùng được | xem-quy-trinh |
| 3 | so-do-o-day | Popup sơ đồ — chọn sẵn Ở đây | Cây quy trình vừa khung, panel bước Ở đây mở (lịch sử 5 dòng + Mở màn hình chi tiết) | xem-quy-trinh |
| 4 | so-do-dang-tai | Popup sơ đồ đang tải | "Đang tải sơ đồ…" | xem-quy-trinh |
| 5 | so-do-loi | Popup sơ đồ lỗi | "Không tải được sơ đồ." + câu E-common-008 / E-common-009 + Thử lại, tại chỗ thay toast | xem-quy-trinh |
| 6 | panel-buoc-chua-tao | Panel bước chưa tạo | "Chưa có hoạt động. Bước này chưa được tạo." | xem-quy-trinh |
| 7 | panel-nga-re | Panel ngã rẽ | "Chưa xác định …" + các hướng có thể đi | xem-quy-trinh |
| 8 | panel-khong-quyen | Panel không có quyền | Đầu panel (kể cả lý do phát sinh) + E-common-011 tại chỗ | xem-quy-trinh |
| 9 | panel-cong-no | Panel công nợ | "Công nợ {Tên NCC}" + Mở bảng công nợ | xem-quy-trinh |
| 10 | so-do-du-lieu-cu | Popup sơ đồ có banner cập nhật | "Quy trình vừa có cập nhật." + Tải lại | xem-quy-trinh |
| 11 | danh-sach-quy-trinh | Danh sách Quy trình | 10 cột, chỉ chi nhánh được phân quyền; tìm theo mã quy trình / mã yêu cầu / mã bản ghi, lọc, xuất, tuỳ chỉnh cột | tra-cuu-quy-trinh |
| 12 | danh-sach-rong | Danh sách rỗng | "Chưa có quy trình nào. Quy trình tự tạo khi có bản ghi đầu tiên được gửi." | tra-cuu-quy-trinh |
| 13 | danh-sach-tim-khong-ra | Tìm không ra | "Không tìm thấy quy trình chứa mã "[mã]"." + Xoá bộ lọc | tra-cuu-quy-trinh |
| 14 | danh-sach-du-lieu-cu | Danh sách có banner cập nhật | "Danh sách vừa có cập nhật." + Tải lại, giữ bộ lọc | tra-cuu-quy-trinh |
| 15 | so-do-tu-danh-sach | Popup sơ đồ trên danh sách | Cây quy trình, chưa chọn bước nào, panel đóng | tra-cuu-quy-trinh |
| 16 | ban-ghi-moi-o-day | Màn chi tiết bản ghi mới | Sau khi gửi thành công: dòng quy trình có bước mới, ghim Ở đây | tao-nghiep-vu-tiep-theo |
| 17 | popup-buoc-da-co-yeu-cau | Popup E-cross-process-flow-001 | Chặn gửi trùng bước "1 bản ghi" (đang chờ / đã hoàn thành), giữ bản nháp | tao-nghiep-vu-tiep-theo |
| 18 | popup-da-co-buoc-con | Popup E-cross-process-flow-002 | Chặn thu hồi/xoá bản ghi đã sinh bước con, nêu tối đa 2 bước + "và n bước khác" | tao-nghiep-vu-tiep-theo |
| 19 | m-the-quy-trinh | App — màn chi tiết có thẻ quy trình | Thẻ quy trình: tên luồng là chính, dòng tóm tắt là phụ | xem-quy-trinh-mobile |
| 20 | m-the-quy-trinh-loi | App — thẻ quy trình tải lỗi | "Không tải được quy trình." + Thử lại | xem-quy-trinh-mobile |
| 21 | m-sheet-so-do | App — sheet sơ đồ | Card tóm tắt + cây rẽ nhánh dọc, vuốt ngang khi cây rộng | xem-quy-trinh-mobile |
| 22 | m-sheet-so-do-dang-tai | App — sheet sơ đồ đang tải | "Đang tải sơ đồ…" | xem-quy-trinh-mobile |
| 23 | m-sheet-so-do-loi | App — sheet sơ đồ lỗi | E-common-008 / E-common-009 + Thử lại | xem-quy-trinh-mobile |
| 24 | m-sheet-so-do-du-lieu-cu | App — sheet sơ đồ có banner | "Quy trình vừa có cập nhật." + Tải lại | xem-quy-trinh-mobile |
| 25 | m-sheet-buoc | App — sheet bước | Đầu sheet + lịch sử 5 dòng + Mở màn hình chi tiết | xem-quy-trinh-mobile |
| 26 | m-sheet-buoc-chua-tao | App — sheet bước chưa tạo | "Chưa có hoạt động. Bước này chưa được tạo." | xem-quy-trinh-mobile |
| 27 | m-sheet-nga-re | App — sheet ngã rẽ | "Chưa xác định …" + các hướng có thể đi | xem-quy-trinh-mobile |
| 28 | m-sheet-cong-no | App — sheet công nợ | "Công nợ {Tên NCC}" + trạng thái, không có nút mở (app không có Bảng công nợ) | xem-quy-trinh-mobile |
| 29 | m-sheet-buoc-khong-quyen | App — sheet bước không có quyền | E-common-011 tại chỗ, giữ lý do phát sinh; quyền theo nghiệp vụ của bước | xem-quy-trinh-mobile |
| 30 | ban-ghi-dong-quy-trinh-dang-tai | Dòng quy trình đang tải | Skeleton cao bằng dòng thật, không đẩy bố cục | xem-quy-trinh |
| 31 | panel-ban-ghi-truoc | Panel bước có bản ghi trước | Thẻ "+n bản ghi trước"; panel thêm khối "Bản ghi trước đó" (mã · Đã thay thế · ngày · Mở) | xem-quy-trinh |
| 32 | panel-lich-su-loi | Panel — lịch sử tải lỗi | "Không tải được lịch sử." + Thử lại trong khối; đầu panel, nút mở vẫn dùng được | xem-quy-trinh |
| 33 | popup-khong-quyen-mo | Popup không có quyền mở bản ghi | Web: popup Loại 2 câu E-common-011 + Đóng, ở lại sơ đồ | xem-quy-trinh |
| 34 | popup-ban-ghi-da-xoa | Popup E-cross-process-flow-004 | "Bản ghi [mã] đã bị xoá." + Tải lại sơ đồ / Đóng | xem-quy-trinh |
| 35 | danh-sach-dang-tai | Danh sách đang tải | Skeleton theo 10 cột | tra-cuu-quy-trinh |
| 36 | danh-sach-loi | Danh sách tải lỗi | Khối "Không tải được danh sách." + Thử lại thay vùng bảng, giữ thanh công cụ và bộ lọc | tra-cuu-quy-trinh |
| 37 | danh-sach-loc-khong-ra | Lọc không ra kết quả | Ô tìm trống: "Không có quy trình phù hợp với bộ lọc." + Xoá bộ lọc | tra-cuu-quy-trinh |
| 38 | danh-sach-khong-quyen | Trang không có quyền | Mở thẳng đường dẫn khi không có quyền menu: E-common-011 + Về trang chủ | tra-cuu-quy-trinh |
| 39 | popup-ban-ghi-nguon-thu-hoi | Popup E-cross-process-flow-003 | Bản ghi nguồn vừa bị thu hồi lúc gửi: Giữ bản nháp (chính) / Xoá bản nháp (phụ, CMP-03) | tao-nghiep-vu-tiep-theo |
| 40 | m-the-quy-trinh-dang-tai | App — thẻ quy trình đang tải | Skeleton theo hình thẻ, có shimmer | xem-quy-trinh-mobile |

## 3. Danh sách flow

| Flow-slug | Tên flow | Thiết bị | Màn hình gồm | Cases phủ |
|-----------|----------|----------|--------------|-----------|
| xem-quy-trinh | Xem quy trình từ màn chi tiết | desktop 1920 | ban-ghi-dong-quy-trinh-dang-tai → ban-ghi-dong-quy-trinh → so-do-dang-tai → so-do-o-day → panel-buoc-chua-tao / panel-nga-re / panel-khong-quyen / panel-cong-no / panel-ban-ghi-truoc; ban-ghi-dong-quy-trinh-loi, so-do-loi, so-do-du-lieu-cu, panel-lich-su-loi, popup-khong-quyen-mo, popup-ban-ghi-da-xoa | happy (mở sơ đồ, mở chi tiết), error (dòng / sơ đồ / lịch sử tải lỗi, không còn quyền mở, bản ghi đã xoá), edge (không thuộc quy trình, chưa tạo, ngã rẽ, không quyền, công nợ, bản ghi thay thế, nhánh Đã huỷ, dữ liệu cũ) |
| tra-cuu-quy-trinh | Tra cứu danh sách Quy trình | desktop 1920 | danh-sach-dang-tai → danh-sach-quy-trinh → so-do-tu-danh-sach; danh-sach-rong, danh-sach-tim-khong-ra, danh-sach-loc-khong-ra, danh-sach-du-lieu-cu, danh-sach-loi, danh-sach-khong-quyen | happy (tìm, lọc, mở sơ đồ, xuất), error (tải lỗi, không có quyền), edge (rỗng, dưới 3 ký tự, tìm không ra, lọc không ra, dữ liệu cũ, mở Phương tiện) |
| tao-nghiep-vu-tiep-theo | Tạo nghiệp vụ tiếp theo, chặn thu hồi/xoá | desktop 1920 | (từ ban-ghi-dong-quy-trinh) → ban-ghi-moi-o-day; popup-buoc-da-co-yeu-cau, popup-ban-ghi-nguon-thu-hoi, popup-da-co-buoc-con | happy (gửi thành công, bước anh em, bản ghi thay thế), error (E-001, E-003, lỗi mạng, E-002), edge (không đạt D6, lưu nháp, xoá bản nháp) |
| xem-quy-trinh-mobile | Xem quy trình trên Delta Super App | mobile 393 | m-the-quy-trinh-dang-tai → m-the-quy-trinh → m-sheet-so-do-dang-tai → m-sheet-so-do → m-sheet-buoc / m-sheet-buoc-chua-tao / m-sheet-nga-re / m-sheet-cong-no / m-sheet-buoc-khong-quyen; m-the-quy-trinh-loi, m-sheet-so-do-loi, m-sheet-so-do-du-lieu-cu | như xem-quy-trinh; nút mở chỉ có khi app có màn chi tiết của loại bản ghi; lỗi E-001 / E-003 / E-004 dạng sheet lỗi Loại 2 cùng nội dung [17] / [39] / [34] |

Màn dùng chung: `ban-ghi-dong-quy-trinh` là điểm bắt đầu của cả `xem-quy-trinh` và `tao-nghiep-vu-tiep-theo` (vẽ 1 lần ở flow xem). Panel [6]–[9], [31], [32] và popup [33], [34] dùng cho cả popup mở từ màn chi tiết [3] và mở từ danh sách [15] (vẽ 1 lần ở flow xem).

## 3.5. Chuyển màn (transitions)

| Từ màn [#] | Đến màn [#] | Trigger | Điều kiện |
|-----------|------------|---------|-----------|
| Màn chi tiết [1] | (không dòng quy trình) [1] | Mở màn | Bản ghi không thuộc quy trình, hoặc luồng độc lập chưa có nhánh (D1) |
| Màn chi tiết [1] | Dòng quy trình đang tải [30] | Mở màn | Bản ghi thuộc quy trình |
| Dòng quy trình đang tải [30] | Màn chi tiết [1] | Tải xong | Tải được |
| Dòng quy trình đang tải [30] | Dòng quy trình tải lỗi [2] | Tải xong | Tải dòng quy trình lỗi |
| Dòng quy trình tải lỗi [2] | Màn chi tiết [1] | Bấm Thử lại | Tải được |
| Màn chi tiết [1] | Sơ đồ đang tải [4] | Bấm dòng quy trình | — |
| Sơ đồ đang tải [4] | Popup sơ đồ Ở đây [3] | Tải xong | Tải được |
| Sơ đồ đang tải [4] | Sơ đồ lỗi [5] | Tải xong | Lỗi hệ thống hoặc mất mạng |
| Sơ đồ lỗi [5] | Sơ đồ đang tải [4] | Bấm Thử lại | — |
| Popup sơ đồ Ở đây [3] | Popup sơ đồ Ở đây [3] | Chọn bước | Bước có bản ghi, có quyền (panel đổi theo bước) |
| Popup sơ đồ Ở đây [3] | Panel bước chưa tạo [6] | Chọn bước | Bước chưa có bản ghi (D2) |
| Popup sơ đồ Ở đây [3] | Panel ngã rẽ [7] | Chọn bước | Ngã rẽ chưa chốt (D5) |
| Popup sơ đồ Ở đây [3] | Panel không có quyền [8] | Chọn bước | Không có quyền xem bản ghi (D3) |
| Popup sơ đồ Ở đây [3] | Panel công nợ [9] | Chọn bước | Bước thanh toán trả sau (D4) |
| Popup sơ đồ Ở đây [3] | Panel bước có bản ghi trước [31] | Chọn bước | Bước "1 bản ghi" có bản ghi Đã thay thế |
| Popup sơ đồ Ở đây [3] | Panel, lịch sử tải lỗi [32] | Tải lịch sử | Lỗi khi tải khối lịch sử |
| Panel, lịch sử tải lỗi [32] | Popup sơ đồ Ở đây [3] | Bấm Thử lại | Tải được |
| Panel [6] / [7] / [8] / [31] | Popup sơ đồ Ở đây [3] | Chọn bước khác | — |
| Panel công nợ [9] | (Bảng công nợ — SRS Thanh toán) | Bấm Mở bảng công nợ | Lọc theo NCC + khoảng thời gian bảng công nợ |
| Popup sơ đồ Ở đây [3] | Sơ đồ có banner [10] | Bước đổi ở nơi khác | Popup đang mở |
| Sơ đồ có banner [10] | Popup sơ đồ Ở đây [3] | Bấm Tải lại | Giữ bước đang chọn nếu còn |
| Popup sơ đồ Ở đây [3] | (Màn chi tiết bản ghi của bước — ngoài feature) | Bấm Mở màn hình chi tiết | Còn quyền; mở cùng tab, đóng popup |
| Popup sơ đồ Ở đây [3] | Popup không có quyền mở [33] | Bấm Mở màn hình chi tiết | Bản ghi vừa bị thu quyền |
| Popup không có quyền mở [33] | Popup sơ đồ Ở đây [3] | Bấm Đóng | — |
| Popup sơ đồ Ở đây [3] | Popup E-004 [34] | Bấm Mở màn hình chi tiết | Bản ghi đã bị xoá trong lúc sơ đồ đang mở |
| Popup E-004 [34] | Sơ đồ đang tải [4] | Bấm Tải lại sơ đồ | — |
| Popup E-004 [34] | Popup sơ đồ Ở đây [3] | Bấm Đóng | Sơ đồ giữ nguyên |
| (Màn chi tiết của bước) | Màn chi tiết [1] | Back trình duyệt | Popup không mở lại |
| Popup sơ đồ Ở đây [3] | Màn chi tiết [1] | Đóng popup | — |
| (Đường dẫn danh sách) | Trang không có quyền [38] | Mở thẳng đường dẫn | Không có quyền menu Quy trình |
| (Menu Module › Quy trình) | Danh sách đang tải [35] | Vào menu | Có quyền |
| Danh sách đang tải [35] | Danh sách [11] | Tải xong | Có quy trình |
| Danh sách đang tải [35] | Danh sách rỗng [12] | Tải xong | Chưa có quy trình nào |
| Danh sách đang tải [35] | Danh sách tải lỗi [36] | Tải xong | Tải lỗi |
| Danh sách tải lỗi [36] | Danh sách đang tải [35] | Bấm Thử lại | Giữ ô tìm và bộ lọc |
| Danh sách [11] | Danh sách [11] | Gõ mã | Dưới 3 ký tự: chưa tìm; từ 3 ký tự: có kết quả |
| Danh sách [11] | Tìm không ra [13] | Gõ mã / lọc | Không có kết quả, ô tìm có từ khoá |
| Danh sách [11] | Lọc không ra kết quả [37] | Lọc | Không có kết quả, ô tìm trống |
| Lọc không ra kết quả [37] | Danh sách [11] | Bấm Xoá bộ lọc | — |
| Tìm không ra [13] | Danh sách [11] | Bấm Xoá bộ lọc | — |
| Danh sách [11] | Danh sách có banner [14] | Có thay đổi ở nơi khác | Thông tin đang hiện trên danh sách đổi |
| Danh sách có banner [14] | Danh sách [11] | Bấm Tải lại | Giữ bộ lọc |
| Danh sách [11] | Popup sơ đồ trên danh sách [15] | Bấm dòng | — |
| Popup sơ đồ trên danh sách [15] | Panel [6] / [7] / [8] / [9] / [31] hoặc panel có bản ghi | Chọn bước | Theo D5 / D2 / D3 / D4, bản ghi thay thế |
| Popup sơ đồ trên danh sách [15] | Danh sách [11] | Đóng popup | — |
| Danh sách [11] | (Màn chi tiết Phương tiện / Xe của khách hàng) | Bấm ô Phương tiện / khách hàng | — |
| Danh sách [11] | (File PDF / Excel) | Bấm Xuất | Đúng dữ liệu và cột đang thấy (FR-cross-process-flow-022) |
| Màn chi tiết [1] | (Form tạo mới của nghiệp vụ tiếp theo) | Bấm nút Tạo … | Đạt trigger + có quyền tạo (D6); không đạt thì không có nút |
| (Form tạo mới) | Màn chi tiết bản ghi mới [16] | Gửi | Thành công (bước 1 bản ghi còn trống, bản cũ Đã thu hồi/từ chối → bản mới thay thế, hoặc bước nhiều bản ghi → bước anh em) |
| (Form tạo mới) | Popup E-001 [17] | Gửi | Bước 1 bản ghi đã có yêu cầu đang chờ hoặc đã hoàn thành; hai người cùng gửi thì người sau |
| Popup E-001 [17] | (Form tạo mới) | Đóng | Giữ bản nháp |
| (Form tạo mới) | Popup E-003 [39] | Gửi | Bản ghi nguồn vừa bị thu hồi (thu hồi đến trước) |
| Popup E-003 [39] | (Form tạo mới) | Bấm Giữ bản nháp | — |
| Popup E-003 [39] | (Bản nháp đã xoá) | Bấm Xoá bản nháp | Xác nhận theo CMP-03 |
| (Form tạo mới) | (Toast E-common-008 / 009) | Gửi | Lỗi hệ thống, mất mạng hoặc cây không nhận bước, giữ form |
| (Form tạo mới) | (Màn của nghiệp vụ) | Lưu nháp | Cây không đổi |
| Màn chi tiết [1] | Popup E-002 [18] | Bấm Thu hồi / Xoá | Đã có bước con |
| Popup E-002 [18] | Màn chi tiết [1] | Đóng | Bản ghi giữ nguyên |
| Màn chi tiết app [19] | (không thẻ quy trình) [19] | Mở màn | Không thuộc quy trình |
| Màn chi tiết app [19] | Thẻ đang tải [40] | Mở màn | Bản ghi thuộc quy trình |
| Thẻ đang tải [40] | Màn chi tiết app [19] | Tải xong | Tải được |
| Thẻ đang tải [40] | Thẻ tải lỗi [20] | Tải xong | Tải thẻ lỗi |
| Thẻ tải lỗi [20] | Màn chi tiết app [19] | Chạm Thử lại | Tải được |
| Màn chi tiết app [19] | Sheet đang tải [22] | Chạm thẻ quy trình | — |
| Sheet đang tải [22] | Sheet sơ đồ [21] | Tải xong | Tải được |
| Sheet đang tải [22] | Sheet lỗi [23] | Tải xong | Lỗi hệ thống hoặc mất mạng |
| Sheet lỗi [23] | Sheet đang tải [22] | Chạm Thử lại | — |
| Sheet sơ đồ [21] | Sheet có banner [24] | Có thay đổi ở nơi khác | Thông tin đang hiện trên sheet đổi |
| Sheet có banner [24] | Sheet sơ đồ [21] | Chạm Tải lại | Giữ bước đang chọn |
| Sheet sơ đồ [21] | Sheet bước [25] | Chạm bước | Có bản ghi, có quyền; nút mở chỉ có khi app có màn chi tiết của loại bản ghi |
| Sheet sơ đồ [21] | Sheet bước chưa tạo [26] | Chạm bước | Chưa có bản ghi |
| Sheet sơ đồ [21] | Sheet ngã rẽ [27] | Chạm bước | Ngã rẽ chưa chốt |
| Sheet sơ đồ [21] | Sheet công nợ [28] | Chạm bước | Bước thanh toán trả sau |
| Sheet sơ đồ [21] | Sheet không có quyền [29] | Chạm bước | Không có quyền xem theo nghiệp vụ của bước |
| Sheet bước [25] – [29] | Sheet sơ đồ [21] | Đóng sheet bước | — |
| Sheet bước [25] | (Màn chi tiết bản ghi trên app) | Chạm Mở màn hình chi tiết | Còn quyền; đẩy màn mới |
| Sheet bước [25] | (Popup chặn E-common-011, GR-26) | Chạm Mở màn hình chi tiết | Bản ghi vừa bị thu quyền |
| Sheet bước [25] | (Sheet lỗi E-004) | Chạm Mở màn hình chi tiết | Bản ghi đã bị xoá; Tải lại sơ đồ → [22] |
| (Màn chi tiết bản ghi trên app) | Màn chi tiết app [19] | Back | Sheet đã đóng |
| Sheet sơ đồ [21] | Màn chi tiết app [19] | Vuốt xuống đóng sheet | — |

## 3.6. Tác vụ chính

| Tác vụ | Vai trò | Tần suất | Mức quan trọng | Đường đi | Số bước | Thành công khi |
|--------|---------|----------|----------------|----------|---------|----------------|
| Kiểm các bước trước đã xong trước khi thanh toán | Kế toán thanh toán | cuối tháng | cao | [1] → [4] → [3] → chọn bước | 2 | ≤3 bước, không mở từng phiếu |
| Xem lệnh sửa chữa đã sinh phiếu gì, bước nào kẹt | Quản lý xưởng | hằng ngày | cao | [11] gõ mã → bấm dòng → [15] | 2 | ≤2 bước (SC-cross-process-flow-02) |
| Tìm nhánh nhập kho dư / bồi thường của một lệnh | Thủ kho | khi có vấn đề | trung | [11] gõ mã → bấm dòng → [15] → chọn bước → Mở màn hình chi tiết | 4 | ≤4 bước |
| Xem ngữ cảnh trước khi duyệt | Người duyệt | thỉnh thoảng | trung | [1] → [4] → [3] → chọn bước trước | 2 | ≤3 bước |
| Xem tiến độ sửa xe của mình | Lái xe | thường xuyên | thấp | [19] chạm thẻ → [22] → [21] | 1 | ≤2 bước |
| Tạo nghiệp vụ tiếp theo | Người tạo bản ghi | hằng ngày | cao | [1] bấm nút → form (ngoài feature) gửi → [16] | 2 + phần nhập của nghiệp vụ | không phải gõ lại dữ liệu đã có ở bản ghi trước |

## 4. Open Questions

- [ ] OQ-1: Bảng phát sinh luồng Điều vận (Cung cấp dịch vụ tổng quát → Điều phối → Lệnh vận tải → Thanh toán chi/thu) — chờ chốt với khách; tác vụ của Điều phối chưa đưa vào Mục 3.6. — Nguồn khách: chưa có trong tài liệu khách gửi
- [x] OQ-2: Delta Super App có màn Bảng công nợ không? — Không. Sheet công nợ [28] chỉ hiện trạng thái, không có nút mở. (chốt 2026-10-12)
