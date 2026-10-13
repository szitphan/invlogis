---
type: srs-flows
feature: cross-process-flow
updated: 2026-10-12
---

# Liên quy trình — Flows

## Flow: Gửi bản ghi → cập nhật cây quy trình
__Trigger__: Người tạo bản ghi gửi, thu hồi hoặc xoá một bản ghi thuộc bảng liên quy trình
__Related UC__: [[docs/cross-process-flow/usecases/uc-tao-nghiep-vu-tiep-theo.md|uc-tao-nghiep-vu-tiep-theo]] · [[docs/cross-process-flow/usecases/uc-cap-nhat-quy-trinh-theo-ban-ghi.md|uc-cap-nhat-quy-trinh-theo-ban-ghi]]
__Related FR__: FR-cross-process-flow-001, -002, -003, -004, -012, -013, -014, -020 · BR-cross-process-flow-011, -012

```mermaid
sequenceDiagram
    actor U as Người tạo bản ghi
    participant NV as Nghiệp vụ (module)
    participant LQT as Liên quy trình
    participant M as Màn đang mở

    U->>NV: Bấm nút tạo bước tiếp theo
    NV->>LQT: Hỏi dữ liệu mang từ bản ghi trước
    LQT-->>NV: Dữ liệu điền sẵn
    NV-->>U: Form tạo mới đã điền sẵn
    U->>NV: Gửi bản ghi
    NV->>LQT: Hỏi cây có nhận bước mới từ bản ghi nguồn không
    alt Bản ghi nguồn vừa bị thu hồi (thu hồi đến trước)
        LQT-->>NV: Từ chối thêm bước
        NV-->>U: Popup E-cross-process-flow-003, nút Giữ bản nháp hoặc Xoá bản nháp
    else Bước khai 1 bản ghi đã có bản ghi đang chờ phê duyệt hoặc đã xong
        LQT-->>NV: Từ chối thêm bước
        NV-->>U: Popup E-cross-process-flow-001, giữ bản nháp
    else Bước nhận được (hợp lệ, khai nhiều bản ghi, hoặc bản cũ Đã thu hồi/từ chối)
        LQT-->>NV: Nhận bước
        Note over NV,LQT: Ghi nhận gửi và thêm bước cùng thành công hoặc cùng không. Lỗi thì bản ghi giữ nháp
        NV->>LQT: Ghi nhận bản ghi gửi thành công kèm bản ghi nguồn
        opt Chưa có quy trình
            LQT->>LQT: Tạo quy trình, sinh mã QT-[CN]-[YY]-[XXXX]
        end
        opt Bước 1 bản ghi đang có bản ghi Đã thu hồi/từ chối
            LQT->>LQT: Bản ghi cũ thành Đã thay thế, bản mới là bản ghi hiện hành
        end
        LQT->>LQT: Thêm bước nối về bản ghi nguồn, Đang triển khai, hiện mã yêu cầu
        LQT->>LQT: Tính lại trạng thái quy trình
        LQT-->>NV: Đã cập nhật cây
        NV-->>U: Màn chi tiết bản ghi mới, ghim Ở đây
        LQT-)M: Báo quy trình vừa có cập nhật (GR-27)
    end

    U->>NV: Thu hồi hoặc xoá bản ghi
    NV->>LQT: Hỏi bản ghi đã có bước con chưa
    alt Đã có bước con
        LQT-->>NV: Không cho phép
        NV-->>U: Popup E-cross-process-flow-002, nêu tối đa 2 bước con kèm mã
    else Chưa có bước con
        LQT-->>NV: Cho phép
        NV->>LQT: Báo bản ghi đã thu hồi hoặc đã xoá
        LQT->>LQT: Đổi trạng thái bước (xoá nhánh phát sinh thì Đã huỷ), tính lại quy trình
        LQT-)M: Báo quy trình vừa có cập nhật (GR-27)
    end

    NV->>LQT: Bản ghi được duyệt
    LQT->>LQT: Thẻ bước đổi từ mã yêu cầu sang mã bản ghi, tính lại trạng thái
```

## Flow: Mở sơ đồ và xem một bước
__Trigger__: Người theo dõi quy trình bấm dòng quy trình trên màn chi tiết, hoặc bấm một dòng ở danh sách Quy trình
__Related UC__: [[docs/cross-process-flow/usecases/uc-xem-quy-trinh-cua-ban-ghi.md|uc-xem-quy-trinh-cua-ban-ghi]] · [[docs/cross-process-flow/usecases/uc-tra-cuu-quy-trinh.md|uc-tra-cuu-quy-trinh]]
__Related FR__: FR-cross-process-flow-006 → 011, FR-cross-process-flow-020

```mermaid
flowchart TD
    start(["Bấm dòng quy trình hoặc dòng danh sách"]) --> load["Tải sơ đồ"]
    load --> ok{"Tải được?"}
    ok -->|"Không"| err["Popup Không tải được sơ đồ: E-common-008 hoặc E-common-009 + Thử lại"]
    err -->|"Thử lại"| load
    ok -->|"Có"| from{"Mở từ đâu?"}
    from -->|"Màn chi tiết"| here["Chọn sẵn bước Ở đây"]
    from -->|"Danh sách"| none["Chưa chọn bước nào"]
    none --> pick["Người dùng chọn một bước"]
    here --> chan{"Kênh?"}
    chan -->|"Web"| d5
    chan -->|"App: chỉ đánh dấu bước"| pick
    pick --> d5{"D5: Ngã rẽ chưa chốt?"}
    d5 -->|"Có"| fork["Panel liệt kê các hướng có thể đi"]
    d5 -->|"Không"| d2{"D2: Bước đã có bản ghi?"}
    d2 -->|"Không"| empty["Panel: Chưa có hoạt động"]
    d2 -->|"Có"| d3{"D3: Có quyền xem?"}
    d3 -->|"Không"| noperm["Panel: E-common-011 tại chỗ, ẩn lịch sử và nút, giữ lý do phát sinh"]
    d3 -->|"Có"| hist["Panel: lịch sử 5 dòng mới nhất + khối Bản ghi trước đó nếu có"]
    hist --> d4{"D4: Bước công nợ trả sau?"}
    d4 -->|"Có, web"| debt["Mở bảng công nợ đã lọc theo NCC"]
    d4 -->|"Có, app"| debtapp["Sheet chỉ hiện trạng thái, không có nút mở"]
    d4 -->|"Không"| open["Mở màn hình chi tiết"]
    open --> gone{"Bản ghi còn không?"}
    gone -->|"Đã bị xoá"| e4["Popup E-cross-process-flow-004"]
    e4 -->|"Tải lại sơ đồ"| load
    gone -->|"Còn"| perm{"Vẫn còn quyền?"}
    perm -->|"Không"| block["Web: popup Loại 2 E-common-011 + Đóng · App: popup chặn GR-26"]
    perm -->|"Có"| done(["Màn chi tiết bản ghi của bước"])
    debtapp --> pick
    debt --> done2(["Bảng công nợ"])
    fork --> pick
    empty --> pick
    noperm --> pick
    block --> pick
```

Trong khi sơ đồ đang mở, thông tin đang hiện trên sơ đồ đổi ở nơi khác thì hiện banner Theo GR-27 + Tải lại; tải lại giữ bước đang chọn nếu còn. Thay đổi không làm đổi thông tin đang hiện thì không báo (FR-cross-process-flow-020).

Không vẽ trong sơ đồ, theo spec: đang tải sơ đồ hiện "Đang tải sơ đồ…" (FR-cross-process-flow-006) · khối lịch sử có đang tải (skeleton 5 dòng), lỗi ("Không tải được lịch sử." + Thử lại, đầu panel và nút mở vẫn dùng được), rỗng (FR-cross-process-flow-008) · trên app, nút mở chỉ có khi app có màn chi tiết của loại bản ghi đó (FR-cross-process-flow-009).

## Notes

- Mã lỗi theo Error Matrix trong [[docs/cross-process-flow/srs/cross-process-flow-spec.md|SRS spec]] Mục 6.
- "Liên quy trình" trong sequence là phần dùng chung của hệ thống. "Nghiệp vụ (module)" là phần của từng nghiệp vụ (Xưởng, Kho, Thanh toán…).
