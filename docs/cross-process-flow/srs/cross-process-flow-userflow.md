---
type: srs-userflow
feature: cross-process-flow
updated: 2026-10-13
primary_device: desktop
stage: flow-approved
flow_approved_at: 2026-10-12
flow_hash: "26cca05b"
---

# Liên quy trình — User Flow

> Nguồn chia flow DUY NHẤT cho feature này. `/wireframe-ascii` và `/wireframe-html` đọc file này để biết flow nào gồm những màn nào — KHÔNG tự chia flow riêng.

Thiết bị theo kênh: Người theo dõi quy trình và Người tạo bản ghi dùng web desktop 1920; Lái xe dùng Delta Super App, khung mobile 393. Cột "Thiết bị" ở Mục 3 là nguồn bề rộng khung cho từng flow. Màn chi tiết bản ghi mẫu: Lệnh sửa chữa LSC-0930 (luồng Sửa chữa xe khách hàng). Mọi nghiệp vụ khác hiện dòng quy trình cùng cách.

## 1. User Flow (tổng)

> Phủ happy / error / edge cases. `[n]` = số màn hình đối chiếu Mục 2; `[n] · Trạng thái` = trạng thái của màn đó (frame Figma 4 phần). Node không đánh số là màn của feature khác hoặc thông báo/popup dùng chung.

### Flow: view-process

```mermaid
flowchart TD
    n1["[1.1] Màn chi tiết bản ghi<br/>có dòng quy trình"]
    d1{"D1: Bản ghi thuộc quy trình?"}
    x0["Màn chi tiết không có dòng quy trình"]
    dl{"Tải dòng quy trình được?"}
    n2["[1.1] · Load error Dòng quy trình tải lỗi<br/>Không tải được quy trình + Thử lại"]
    n4["[1.2] · Loading Sơ đồ đang tải"]
    dt{"Tải sơ đồ được?"}
    n5["[1.2] · Load error Sơ đồ lỗi<br/>Không tải được sơ đồ + E-common-008 hoặc 009 + Thử lại"]
    n3["[1.2] Popup sơ đồ<br/>chọn sẵn bước Ở đây, panel mở"]
    pick{"Bước được chọn là gì?"}
    n6["[1.3] Panel bước chưa tạo"]
    n7["[1.4] Panel ngã rẽ<br/>các hướng có thể đi"]
    n8["[1.5] Panel không có quyền<br/>E-common-011 tại chỗ, giữ lý do phát sinh"]
    n9["[1.6] Panel công nợ<br/>Công nợ tên NCC"]
    n10["[1.2] · Update banner Sơ đồ có banner<br/>Quy trình vừa có cập nhật"]
    n30["[1.1] · Loading Dòng quy trình đang tải<br/>skeleton"]
    n31["[1.7] Panel bước có bản ghi trước<br/>+n bản ghi trước, khối Bản ghi trước đó"]
    n32["[1.2] · History load error Panel, lịch sử tải lỗi<br/>Không tải được lịch sử + Thử lại"]
    gone{"Bản ghi còn không?"}
    n34["[1.9] Popup E-cross-process-flow-004<br/>bản ghi đã bị xoá"]
    perm{"Còn quyền xem bản ghi?"}
    n33["[1.8] Popup không có quyền mở<br/>E-common-011 + Đóng"]
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

### Flow: search-process

```mermaid
flowchart TD
    m0["Menu Module - Quy trình"]
    dq{"Có quyền menu Quy trình?"}
    t38["[2.1] · No permission Trang không có quyền<br/>E-common-011 + Về trang chủ"]
    t35["[2.1] · Loading Danh sách đang tải<br/>skeleton 10 cột"]
    t11["[2.1] Danh sách Quy trình<br/>chỉ chi nhánh được phân quyền"]
    dr{"Có quy trình nào?"}
    t12["[2.1] · Empty Danh sách rỗng"]
    t36["[2.1] · Load error Danh sách tải lỗi<br/>khối lỗi + Thử lại, giữ bộ lọc"]
    ds{"Ô tìm từ 3 ký tự?"}
    dk{"Có kết quả?"}
    t13["[2.1] · No search results Tìm không ra + Xoá bộ lọc"]
    t37["[2.1] · No filter results Lọc không ra kết quả<br/>ô tìm trống + Xoá bộ lọc"]
    t14["[2.1] · Update banner Danh sách có banner<br/>Danh sách vừa có cập nhật"]
    t15["[2.2] Popup sơ đồ trên danh sách<br/>chưa chọn bước nào"]
    tp["Chọn bước, panel như flow view-process [1.2] đến [1.6]"]
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

### Flow: create-next-step

```mermaid
flowchart TD
    c1["[1.1] Màn chi tiết bản ghi<br/>dùng chung với view-process"]
    d6{"D6: Đạt trigger và có quyền tạo?"}
    cn["Không hiện nút tạo"]
    cf["Form tạo mới đã điền sẵn<br/>của nghiệp vụ tiếp theo, ngoài feature"]
    cs{"Kết quả gửi"}
    c16["[3.1] Màn chi tiết bản ghi mới<br/>cây có bước mới, ghim Ở đây"]
    c17["[3.2] Popup E-cross-process-flow-001<br/>bước đã có yêu cầu khác hoặc đã hoàn thành"]
    c39["[3.3] Popup E-cross-process-flow-003<br/>bản ghi nguồn vừa bị thu hồi"]
    cdel["Bản nháp đã xoá"]
    ct["Toast E-common-008 hoặc 009, giữ form"]
    cd["Lưu nháp, cây không đổi"]
    ch{"Bản ghi đã có bước con?"}
    c18["[3.4] Popup E-cross-process-flow-002<br/>không thể thu hồi hoặc xoá"]
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

### Flow: view-process-mobile

```mermaid
flowchart TD
    a19["[1.1] Màn chi tiết trên app<br/>có thẻ quy trình"]
    ad1{"Bản ghi thuộc quy trình?"}
    ax0["Không có thẻ quy trình"]
    a40["[1.1] · Loading Thẻ quy trình đang tải<br/>skeleton shimmer"]
    adl{"Tải thẻ được?"}
    a20["[1.1] · Load error Thẻ quy trình tải lỗi + Thử lại"]
    a22["[1.2] · Loading Sheet sơ đồ đang tải"]
    adt{"Tải sơ đồ được?"}
    a23["[1.2] · Load error Sheet sơ đồ lỗi<br/>Không tải được sơ đồ + E-common-008 hoặc 009 + Thử lại"]
    a21["[1.2] Sheet sơ đồ<br/>cây dọc, đánh dấu Ở đây, không tự mở sheet bước"]
    a24["[1.2] · Update banner Sheet sơ đồ có banner<br/>Quy trình vừa có cập nhật"]
    apick{"Bước được chọn là gì?"}
    a25["[4.1] Sheet bước<br/>lịch sử + Mở màn hình chi tiết khi app có màn"]
    a26["[1.3] Sheet bước chưa tạo"]
    a27["[1.4] Sheet ngã rẽ"]
    a28["[1.6] Sheet công nợ<br/>chỉ trạng thái, không có nút mở"]
    a29["[1.5] Sheet bước không có quyền<br/>E-common-011, giữ lý do phát sinh"]
    agone{"Bản ghi còn không?"}
    ae4["Sheet lỗi E-cross-process-flow-004<br/>nội dung như [1.9]"]
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

| [#] | Slug | Màn hình | Mục đích | Trạng thái | Thiết bị | Thuộc flow |
|-----|------|----------|----------|------------|----------|------------|
| 1.1 | record-detail | Màn chi tiết bản ghi có dòng quy trình | Web: dòng quy trình đầu màn (tên luồng, tiến độ, "Xong x/y bước · n nhánh phát sinh", Bước trước / Phát sinh từ) + nút tạo tiếp theo + Thu hồi/Xoá ở vùng hành động. App: thẻ quy trình, tên luồng là chính, dòng tóm tắt là phụ | Loading (skeleton cao bằng dòng thật; app: theo hình thẻ, có shimmer) · Load error ("Không tải được quy trình." + Thử lại, màn chi tiết vẫn dùng được) | web, mob | view-process, view-process-mobile, create-next-step |
| 1.2 | process-diagram | Sơ đồ quy trình — chọn sẵn Ở đây | Web: popup cây quy trình vừa khung, panel bước Ở đây mở (lịch sử 5 dòng + Mở màn hình chi tiết). App: sheet card tóm tắt + cây rẽ nhánh dọc, vuốt ngang khi cây rộng, không tự mở sheet bước | Loading ("Đang tải sơ đồ…") · Load error ("Không tải được sơ đồ." + E-common-008 / E-common-009 + Thử lại, tại chỗ thay toast) · Update banner ("Quy trình vừa có cập nhật." + Tải lại) · History load error (web: "Không tải được lịch sử." + Thử lại trong khối; đầu panel, nút mở vẫn dùng được) | web, mob | view-process, view-process-mobile |
| 1.3 | step-not-created | Bước chưa tạo | "Chưa có hoạt động. Bước này chưa được tạo." (web: panel; app: sheet) | — | web, mob | view-process, view-process-mobile |
| 1.4 | branch-point | Ngã rẽ | "Chưa xác định …" + các hướng có thể đi | — | web, mob | view-process, view-process-mobile |
| 1.5 | step-no-permission | Bước không có quyền | Đầu panel/sheet (kể cả lý do phát sinh) + E-common-011 tại chỗ; quyền theo nghiệp vụ của bước | — | web, mob | view-process, view-process-mobile |
| 1.6 | debt-step | Bước công nợ | "Công nợ {Tên NCC}". Web: + Mở bảng công nợ. App: chỉ trạng thái, không có nút mở (app không có Bảng công nợ) | — | web, mob | view-process, view-process-mobile |
| 1.7 | step-previous-records | Bước có bản ghi trước | Thẻ "+n bản ghi trước"; panel thêm khối "Bản ghi trước đó" (mã · Đã thay thế · ngày · Mở) | — | web | view-process |
| 1.8 | open-denied | Popup không có quyền mở bản ghi | Popup Loại 2 câu E-common-011 + Đóng, ở lại sơ đồ | — | web | view-process |
| 1.9 | record-deleted | Popup E-cross-process-flow-004 | "Bản ghi [mã] đã bị xoá." + Tải lại sơ đồ / Đóng | — | web | view-process |
| 2.1 | process-list | Danh sách Quy trình | 10 cột, chỉ chi nhánh được phân quyền; tìm theo mã quy trình / mã yêu cầu / mã bản ghi, lọc, xuất, tuỳ chỉnh cột | Loading (skeleton theo 10 cột) · Load error (khối "Không tải được danh sách." + Thử lại thay vùng bảng, giữ thanh công cụ và bộ lọc) · Empty ("Chưa có quy trình nào. Quy trình tự tạo khi có bản ghi đầu tiên được gửi.") · No search results ("Không tìm thấy quy trình chứa mã "[mã]"." + Xoá bộ lọc) · No filter results (ô tìm trống: "Không có quy trình phù hợp với bộ lọc." + Xoá bộ lọc) · Update banner ("Danh sách vừa có cập nhật." + Tải lại, giữ bộ lọc) · No permission (mở thẳng đường dẫn khi không có quyền menu: E-common-011 + Về trang chủ) | web | search-process |
| 2.2 | list-process-diagram | Popup sơ đồ trên danh sách | Cây quy trình, chưa chọn bước nào, panel đóng | — | web | search-process |
| 3.1 | new-record-detail | Màn chi tiết bản ghi mới | Sau khi gửi thành công: dòng quy trình có bước mới, ghim Ở đây | — | web | create-next-step |
| 3.2 | step-already-requested | Popup E-cross-process-flow-001 | Chặn gửi trùng bước "1 bản ghi" (đang chờ / đã hoàn thành), giữ bản nháp | — | web | create-next-step |
| 3.3 | source-revoked | Popup E-cross-process-flow-003 | Bản ghi nguồn vừa bị thu hồi lúc gửi: Giữ bản nháp (chính) / Xoá bản nháp (phụ, CMP-03) | — | web | create-next-step |
| 3.4 | has-child-step | Popup E-cross-process-flow-002 | Chặn thu hồi/xoá bản ghi đã sinh bước con, nêu tối đa 2 bước + "và n bước khác" | — | web | create-next-step |
| 4.1 | step-sheet | App — sheet bước | Đầu sheet + lịch sử 5 dòng + Mở màn hình chi tiết | — | mob | view-process-mobile |

## 3. Danh sách flow

| Flow-slug | Tên flow | Thiết bị | Màn hình gồm | Cases phủ |
|-----------|----------|----------|--------------|-----------|
| view-process | Xem quy trình từ màn chi tiết | desktop 1920 | record-detail → process-diagram → step-not-created / branch-point / step-no-permission / debt-step / step-previous-records; open-denied, record-deleted | happy (mở sơ đồ, mở chi tiết), error (dòng / sơ đồ / lịch sử tải lỗi, không còn quyền mở, bản ghi đã xoá), edge (không thuộc quy trình, chưa tạo, ngã rẽ, không quyền, công nợ, bản ghi thay thế, nhánh Đã huỷ, dữ liệu cũ) |
| search-process | Tra cứu danh sách Quy trình | desktop 1920 | process-list → list-process-diagram | happy (tìm, lọc, mở sơ đồ, xuất), error (tải lỗi, không có quyền), edge (rỗng, dưới 3 ký tự, tìm không ra, lọc không ra, dữ liệu cũ, mở Phương tiện) |
| create-next-step | Tạo nghiệp vụ tiếp theo, chặn thu hồi/xoá | desktop 1920 | (từ record-detail) → new-record-detail; step-already-requested, source-revoked, has-child-step | happy (gửi thành công, bước anh em, bản ghi thay thế), error (E-001, E-003, lỗi mạng, E-002), edge (không đạt D6, lưu nháp, xoá bản nháp) |
| view-process-mobile | Xem quy trình trên Delta Super App | mobile 393 | record-detail → process-diagram → step-sheet / step-not-created / branch-point / debt-step / step-no-permission | như view-process; nút mở chỉ có khi app có màn chi tiết của loại bản ghi; lỗi E-001 / E-003 / E-004 dạng sheet lỗi Loại 2 cùng nội dung [3.2] / [3.3] / [1.9] |

Màn dùng chung: `record-detail` là điểm bắt đầu của `view-process`, `create-next-step` (web) và `view-process-mobile` (mob). Bước [1.3]–[1.7] và popup [1.8], [1.9] dùng cho cả sơ đồ mở từ màn chi tiết [1.2] và mở từ danh sách [2.2] (vẽ 1 lần ở flow view-process). Trạng thái không có số riêng (cột Trạng thái) là frame `{screenId} · {slug} · {Trạng thái}` dưới màn gốc.

## 3.5. Chuyển màn (transitions)

| Từ màn [#] | Đến màn [#] | Trigger | Điều kiện |
|-----------|------------|---------|-----------|
| Màn chi tiết [1.1] | (không dòng quy trình) [1.1] | Mở màn | Bản ghi không thuộc quy trình, hoặc luồng độc lập chưa có nhánh (D1) |
| Màn chi tiết [1.1] | Dòng quy trình đang tải [1.1] · Loading | Mở màn | Bản ghi thuộc quy trình |
| Dòng quy trình đang tải [1.1] · Loading | Màn chi tiết [1.1] | Tải xong | Tải được |
| Dòng quy trình đang tải [1.1] · Loading | Dòng quy trình tải lỗi [1.1] · Load error | Tải xong | Tải dòng quy trình lỗi |
| Dòng quy trình tải lỗi [1.1] · Load error | Màn chi tiết [1.1] | Bấm Thử lại | Tải được |
| Màn chi tiết [1.1] | Sơ đồ đang tải [1.2] · Loading | Bấm dòng quy trình | — |
| Sơ đồ đang tải [1.2] · Loading | Popup sơ đồ Ở đây [1.2] | Tải xong | Tải được |
| Sơ đồ đang tải [1.2] · Loading | Sơ đồ lỗi [1.2] · Load error | Tải xong | Lỗi hệ thống hoặc mất mạng |
| Sơ đồ lỗi [1.2] · Load error | Sơ đồ đang tải [1.2] · Loading | Bấm Thử lại | — |
| Popup sơ đồ Ở đây [1.2] | Popup sơ đồ Ở đây [1.2] | Chọn bước | Bước có bản ghi, có quyền (panel đổi theo bước) |
| Popup sơ đồ Ở đây [1.2] | Panel bước chưa tạo [1.3] | Chọn bước | Bước chưa có bản ghi (D2) |
| Popup sơ đồ Ở đây [1.2] | Panel ngã rẽ [1.4] | Chọn bước | Ngã rẽ chưa chốt (D5) |
| Popup sơ đồ Ở đây [1.2] | Panel không có quyền [1.5] | Chọn bước | Không có quyền xem bản ghi (D3) |
| Popup sơ đồ Ở đây [1.2] | Panel công nợ [1.6] | Chọn bước | Bước thanh toán trả sau (D4) |
| Popup sơ đồ Ở đây [1.2] | Panel bước có bản ghi trước [1.7] | Chọn bước | Bước "1 bản ghi" có bản ghi Đã thay thế |
| Popup sơ đồ Ở đây [1.2] | Panel, lịch sử tải lỗi [1.2] · History load error | Tải lịch sử | Lỗi khi tải khối lịch sử |
| Panel, lịch sử tải lỗi [1.2] · History load error | Popup sơ đồ Ở đây [1.2] | Bấm Thử lại | Tải được |
| Panel [1.3] / [1.4] / [1.5] / [1.7] | Popup sơ đồ Ở đây [1.2] | Chọn bước khác | — |
| Panel công nợ [1.6] | (Bảng công nợ — SRS Thanh toán) | Bấm Mở bảng công nợ | Lọc theo NCC + khoảng thời gian bảng công nợ |
| Popup sơ đồ Ở đây [1.2] | Sơ đồ có banner [1.2] · Update banner | Bước đổi ở nơi khác | Popup đang mở |
| Sơ đồ có banner [1.2] · Update banner | Popup sơ đồ Ở đây [1.2] | Bấm Tải lại | Giữ bước đang chọn nếu còn |
| Popup sơ đồ Ở đây [1.2] | (Màn chi tiết bản ghi của bước — ngoài feature) | Bấm Mở màn hình chi tiết | Còn quyền; mở cùng tab, đóng popup |
| Popup sơ đồ Ở đây [1.2] | Popup không có quyền mở [1.8] | Bấm Mở màn hình chi tiết | Bản ghi vừa bị thu quyền |
| Popup không có quyền mở [1.8] | Popup sơ đồ Ở đây [1.2] | Bấm Đóng | — |
| Popup sơ đồ Ở đây [1.2] | Popup E-004 [1.9] | Bấm Mở màn hình chi tiết | Bản ghi đã bị xoá trong lúc sơ đồ đang mở |
| Popup E-004 [1.9] | Sơ đồ đang tải [1.2] · Loading | Bấm Tải lại sơ đồ | — |
| Popup E-004 [1.9] | Popup sơ đồ Ở đây [1.2] | Bấm Đóng | Sơ đồ giữ nguyên |
| (Màn chi tiết của bước) | Màn chi tiết [1.1] | Back trình duyệt | Popup không mở lại |
| Popup sơ đồ Ở đây [1.2] | Màn chi tiết [1.1] | Đóng popup | — |
| (Đường dẫn danh sách) | Trang không có quyền [2.1] · No permission | Mở thẳng đường dẫn | Không có quyền menu Quy trình |
| (Menu Module › Quy trình) | Danh sách đang tải [2.1] · Loading | Vào menu | Có quyền |
| Danh sách đang tải [2.1] · Loading | Danh sách [2.1] | Tải xong | Có quy trình |
| Danh sách đang tải [2.1] · Loading | Danh sách rỗng [2.1] · Empty | Tải xong | Chưa có quy trình nào |
| Danh sách đang tải [2.1] · Loading | Danh sách tải lỗi [2.1] · Load error | Tải xong | Tải lỗi |
| Danh sách tải lỗi [2.1] · Load error | Danh sách đang tải [2.1] · Loading | Bấm Thử lại | Giữ ô tìm và bộ lọc |
| Danh sách [2.1] | Danh sách [2.1] | Gõ mã | Dưới 3 ký tự: chưa tìm; từ 3 ký tự: có kết quả |
| Danh sách [2.1] | Tìm không ra [2.1] · No search results | Gõ mã / lọc | Không có kết quả, ô tìm có từ khoá |
| Danh sách [2.1] | Lọc không ra kết quả [2.1] · No filter results | Lọc | Không có kết quả, ô tìm trống |
| Lọc không ra kết quả [2.1] · No filter results | Danh sách [2.1] | Bấm Xoá bộ lọc | — |
| Tìm không ra [2.1] · No search results | Danh sách [2.1] | Bấm Xoá bộ lọc | — |
| Danh sách [2.1] | Danh sách có banner [2.1] · Update banner | Có thay đổi ở nơi khác | Thông tin đang hiện trên danh sách đổi |
| Danh sách có banner [2.1] · Update banner | Danh sách [2.1] | Bấm Tải lại | Giữ bộ lọc |
| Danh sách [2.1] | Popup sơ đồ trên danh sách [2.2] | Bấm dòng | — |
| Popup sơ đồ trên danh sách [2.2] | Panel [1.3] / [1.4] / [1.5] / [1.6] / [1.7] hoặc panel có bản ghi | Chọn bước | Theo D5 / D2 / D3 / D4, bản ghi thay thế |
| Popup sơ đồ trên danh sách [2.2] | Danh sách [2.1] | Đóng popup | — |
| Danh sách [2.1] | (Màn chi tiết Phương tiện / Xe của khách hàng) | Bấm ô Phương tiện / khách hàng | — |
| Danh sách [2.1] | (File PDF / Excel) | Bấm Xuất | Đúng dữ liệu và cột đang thấy (FR-cross-process-flow-022) |
| Màn chi tiết [1.1] | (Form tạo mới của nghiệp vụ tiếp theo) | Bấm nút Tạo … | Đạt trigger + có quyền tạo (D6); không đạt thì không có nút |
| (Form tạo mới) | Màn chi tiết bản ghi mới [3.1] | Gửi | Thành công (bước 1 bản ghi còn trống, bản cũ Đã thu hồi/từ chối → bản mới thay thế, hoặc bước nhiều bản ghi → bước anh em) |
| (Form tạo mới) | Popup E-001 [3.2] | Gửi | Bước 1 bản ghi đã có yêu cầu đang chờ hoặc đã hoàn thành; hai người cùng gửi thì người sau |
| Popup E-001 [3.2] | (Form tạo mới) | Đóng | Giữ bản nháp |
| (Form tạo mới) | Popup E-003 [3.3] | Gửi | Bản ghi nguồn vừa bị thu hồi (thu hồi đến trước) |
| Popup E-003 [3.3] | (Form tạo mới) | Bấm Giữ bản nháp | — |
| Popup E-003 [3.3] | (Bản nháp đã xoá) | Bấm Xoá bản nháp | Xác nhận theo CMP-03 |
| (Form tạo mới) | (Toast E-common-008 / 009) | Gửi | Lỗi hệ thống, mất mạng hoặc cây không nhận bước, giữ form |
| (Form tạo mới) | (Màn của nghiệp vụ) | Lưu nháp | Cây không đổi |
| Màn chi tiết [1.1] | Popup E-002 [3.4] | Bấm Thu hồi / Xoá | Đã có bước con |
| Popup E-002 [3.4] | Màn chi tiết [1.1] | Đóng | Bản ghi giữ nguyên |
| Màn chi tiết app [1.1] | (không thẻ quy trình) [1.1] | Mở màn | Không thuộc quy trình |
| Màn chi tiết app [1.1] | Thẻ đang tải [1.1] · Loading | Mở màn | Bản ghi thuộc quy trình |
| Thẻ đang tải [1.1] · Loading | Màn chi tiết app [1.1] | Tải xong | Tải được |
| Thẻ đang tải [1.1] · Loading | Thẻ tải lỗi [1.1] · Load error | Tải xong | Tải thẻ lỗi |
| Thẻ tải lỗi [1.1] · Load error | Màn chi tiết app [1.1] | Chạm Thử lại | Tải được |
| Màn chi tiết app [1.1] | Sheet đang tải [1.2] · Loading | Chạm thẻ quy trình | — |
| Sheet đang tải [1.2] · Loading | Sheet sơ đồ [1.2] | Tải xong | Tải được |
| Sheet đang tải [1.2] · Loading | Sheet lỗi [1.2] · Load error | Tải xong | Lỗi hệ thống hoặc mất mạng |
| Sheet lỗi [1.2] · Load error | Sheet đang tải [1.2] · Loading | Chạm Thử lại | — |
| Sheet sơ đồ [1.2] | Sheet có banner [1.2] · Update banner | Có thay đổi ở nơi khác | Thông tin đang hiện trên sheet đổi |
| Sheet có banner [1.2] · Update banner | Sheet sơ đồ [1.2] | Chạm Tải lại | Giữ bước đang chọn |
| Sheet sơ đồ [1.2] | Sheet bước [4.1] | Chạm bước | Có bản ghi, có quyền; nút mở chỉ có khi app có màn chi tiết của loại bản ghi |
| Sheet sơ đồ [1.2] | Sheet bước chưa tạo [1.3] | Chạm bước | Chưa có bản ghi |
| Sheet sơ đồ [1.2] | Sheet ngã rẽ [1.4] | Chạm bước | Ngã rẽ chưa chốt |
| Sheet sơ đồ [1.2] | Sheet công nợ [1.6] | Chạm bước | Bước thanh toán trả sau |
| Sheet sơ đồ [1.2] | Sheet không có quyền [1.5] | Chạm bước | Không có quyền xem theo nghiệp vụ của bước |
| Sheet bước [4.1], [1.3] – [1.6] | Sheet sơ đồ [1.2] | Đóng sheet bước | — |
| Sheet bước [4.1] | (Màn chi tiết bản ghi trên app) | Chạm Mở màn hình chi tiết | Còn quyền; đẩy màn mới |
| Sheet bước [4.1] | (Popup chặn E-common-011, GR-26) | Chạm Mở màn hình chi tiết | Bản ghi vừa bị thu quyền |
| Sheet bước [4.1] | (Sheet lỗi E-004) | Chạm Mở màn hình chi tiết | Bản ghi đã bị xoá; Tải lại sơ đồ → [1.2] · Loading |
| (Màn chi tiết bản ghi trên app) | Màn chi tiết app [1.1] | Back | Sheet đã đóng |
| Sheet sơ đồ [1.2] | Màn chi tiết app [1.1] | Vuốt xuống đóng sheet | — |

## 3.6. Tác vụ chính

| Tác vụ | Vai trò | Tần suất | Mức quan trọng | Đường đi | Số bước | Thành công khi |
|--------|---------|----------|----------------|----------|---------|----------------|
| Kiểm các bước trước đã xong trước khi thanh toán | Kế toán thanh toán | cuối tháng | cao | [1.1] → [1.2] · Loading → [1.2] → chọn bước | 2 | ≤3 bước, không mở từng phiếu |
| Xem lệnh sửa chữa đã sinh phiếu gì, bước nào kẹt | Quản lý xưởng | hằng ngày | cao | [2.1] gõ mã → bấm dòng → [2.2] | 2 | ≤2 bước (SC-cross-process-flow-02) |
| Tìm nhánh nhập kho dư / bồi thường của một lệnh | Thủ kho | khi có vấn đề | trung | [2.1] gõ mã → bấm dòng → [2.2] → chọn bước → Mở màn hình chi tiết | 4 | ≤4 bước |
| Xem ngữ cảnh trước khi duyệt | Người duyệt | thỉnh thoảng | trung | [1.1] → [1.2] · Loading → [1.2] → chọn bước trước | 2 | ≤3 bước |
| Xem tiến độ sửa xe của mình | Lái xe | thường xuyên | thấp | [1.1] chạm thẻ → [1.2] · Loading → [1.2] | 1 | ≤2 bước |
| Tạo nghiệp vụ tiếp theo | Người tạo bản ghi | hằng ngày | cao | [1.1] bấm nút → form (ngoài feature) gửi → [3.1] | 2 + phần nhập của nghiệp vụ | không phải gõ lại dữ liệu đã có ở bản ghi trước |

## 4. Open Questions

- [ ] OQ-1: Bảng phát sinh luồng Điều vận (Cung cấp dịch vụ tổng quát → Điều phối → Lệnh vận tải → Thanh toán chi/thu) — chờ chốt với khách; tác vụ của Điều phối chưa đưa vào Mục 3.6. — Nguồn khách: chưa có trong tài liệu khách gửi
- [x] OQ-2: Delta Super App có màn Bảng công nợ không? — Không. Sheet công nợ [1.6] chỉ hiện trạng thái, không có nút mở. (chốt 2026-10-12)
