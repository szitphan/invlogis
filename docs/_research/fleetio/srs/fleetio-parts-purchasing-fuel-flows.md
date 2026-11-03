---
type: research
feature: fleetio-parts-purchasing-fuel
updated: 2026-11-03
---

# Phụ tùng, mua hàng, nhiên liệu — Flows

Mã lỗi viết tắt, đầy đủ có tiền tố `E-fleetio-parts-purchasing-fuel-`. Mã case dẫn về SRS Mục 6A. Mô tả Fleetio đang làm gì, không phải yêu cầu đã chốt.

## Flow 1: Mua và nhận hàng (`Chạy` nhánh có quyền, `Docs` nhánh chờ duyệt)

```mermaid
sequenceDiagram
    actor U as Người lập đơn
    actor A as Người duyệt
    participant P as Đơn mua
    participant K as Kho
    participant L as Sổ kho
    U->>P: Chọn một nhà cung cấp có Parts, một kho
    alt Chưa chọn đủ
        P-->>U: E-001 Select a Vendor and Part Location first
    else Chọn đủ
        U->>P: Thêm dòng, thấy tồn tại kho của đơn
    end
    alt Dòng trùng
        P-->>U: E-011 Part is duplicated, không tạo đơn
    else Lưu được
        P-->>U: Draft, chưa Edit thì chưa tính vào Pending PO Qty
    end
    opt Sửa Draft rồi lưu
        U->>P: Đổi kho, nhà cung cấp, số, xoá dòng
        P->>K: E-032 Số vào Pending dù chưa duyệt
    end
    alt Có quyền duyệt
        U->>P: Approve hoặc Save and Approve, một cú bấm
    else Không có quyền, theo tài liệu
        U->>P: Submit for Approval
        A->>P: Approve hoặc Reject
    end
    P-->>U: Approved, ghi Approved By, đơn chưa Edit thì Pending PO Qty vẫn 0
    opt Sửa lại sau khi duyệt
        U->>P: Save as Draft, chỉ có trong form Edit
        P-->>U: Về Draft, mất dòng Approved By
    end
    U->>P: Mark as Purchased
    P->>K: Đơn chưa Edit bắt đầu tính Pending PO Qty
    opt Mua nhầm
        U->>P: Unmark as Purchased
        P-->>U: Về Approved, không hỏi, E-026 Pending không giảm
    end
    opt Sửa đơn đã mua
        U->>P: Sửa số, giá, kho và nhà cung cấp đã khoá
        P->>K: Pending theo số đặt mới, không cảnh báo
    end
    U->>P: Receive số lượng, chọn nơi đến
    alt Gõ số âm
        P-->>U: E-014 Thành nhận dương, không báo
    else Gõ vượt số đặt
        P-->>U: E-013 Không chặn, tiền vẫn theo số đặt
    end
    P->>K: Tăng tồn
    K->>L: Ghi số trước, số sau, chứng từ
    alt Mọi dòng đạt số đặt
        P-->>U: Received Full, hiện Close, Make Adjustment
    else Còn dòng thiếu
        P-->>U: Received Partial, lần sau gợi ý số còn lại
    end
```

Nhánh: D1 đến D11, D22 đến D33 ở SRS Mục 6A. Nhánh Submit for Approval lượt 3 vẫn không chạy được (D32). Tổng đơn tính theo số đặt, thuế tính trên phần sau giảm, không gồm phí (D6). Ô Shipping sai 100 lần: E-012.

## Flow 2: Nhận hàng vào lệnh (`Chạy`)

```mermaid
flowchart TD
    A["Hộp Receive: chọn nơi đến"] --> B{"Nơi đến"}
    B -->|"Inventory"| C["Tăng tồn, sổ loại Purchase Order"]
    B -->|"Existing work order"| D["Báo sẽ nhập kho trước rồi thêm vào lệnh"]
    B -->|"New work order"| E["Báo hàng ở lại kho nếu không lưu lệnh"]
    D --> F["Sổ cộng số nhận, mở form lệnh với ghi chú From PO"]
    E --> F
    F --> G{"Lưu form lệnh"}
    G -->|"Lưu"| H["Sổ trừ số nhận, dòng phụ tùng vào lệnh"]
    G -->|"Huỷ form"| I["Hàng ở lại kho, đơn đã đổi trạng thái, không có lệnh"]
    C --> Z["Đơn: Partial hoặc Full"]
    H --> Z
    I --> Z
    Z --> KetThuc["Kết thúc"]
```

D14 chạy nhánh lệnh có sẵn đến lưu lệnh; D15 chạy nhánh lệnh mới đến huỷ form. Lưu lệnh mới chưa được nhật ký ghi riêng. `Docs`: chỉ với Static Pricing; phương pháp khác chưa thử (OQ-11).

## Flow 3: Trả hàng và đóng đơn (`Chạy`)

```mermaid
flowchart TD
    A["Đơn đã nhận"] --> B{"Trạng thái"}
    B -->|"Partial"| C{"Còn chờ hàng"}
    B -->|"Full"| D{"Có trả hàng"}
    C -->|"Có"| E["Receive tiếp, gợi ý số còn lại"]
    C -->|"Không"| F["Close, hộp xác nhận, không ghi lý do"]
    E --> B
    D -->|"Có"| G["Make Adjustment: nhập số âm"]
    D -->|"Không"| H["Close tay vì tự đóng đang tắt"]
    G --> I{"Số âm quá số đã nhận"}
    I -->|"Có"| J["E-015 Cắt về số đã nhận, không báo"]
    I -->|"Không"| K["Giữ nguyên số nhập"]
    J --> L["Sổ ghi giảm, tồn có thể âm, về Partial, Received in Full By vẫn còn"]
    K --> L
    L --> B
    F --> M["Closed, không có nút mở lại"]
    H --> M
    M --> N{"Thao tác sau khi đóng"}
    N -->|"Sửa đơn giá"| O["E-025 Edit đổi đơn giá, tổng tính lại"]
    N -->|"Make Adjustment"| Q["E-027 Tick dòng, nhập số âm: số nhận và tồn giảm, sổ ghi Received, vẫn Closed"]
    N -->|"Không"| P["Kết thúc"]
    O --> P
    Q --> P
    P --> KetThuc["Kết thúc"]
```

Partial không có Make Adjustment. Receive gõ số âm thành nhận dương (E-014), nên đó không phải đường trả hàng. Make Adjustment từ Closed: -1 làm Qty Received 110 xuống 109, đơn vẫn Closed, không hỏi lý do (D18). Không có huỷ đơn; lùi về Draft trước khi Purchased, hoặc Delete (chưa bấm, OQ-10).

## Flow 4: Xuất phụ tùng cho lệnh, sửa, xoá, hoàn thành (`Chạy`)

```mermaid
sequenceDiagram
    actor T as Nhân viên xưởng
    participant W as Lệnh sửa
    participant K as Kho
    participant L as Sổ kho
    T->>W: Tìm phụ tùng, thấy tồn từng kho
    alt Chọn None
        T->>W: None, No Inventory Adjustment
        W-->>T: Không đổi tồn
    else Chọn kho
        T->>W: Chọn kho, số lượng, đầu việc
        W-->>T: This will make an inventory adjustment
        T->>W: Lưu lệnh
        W->>K: Trừ tồn ngay, kể cả lệnh Open
        K->>L: Ghi biến động theo số lệnh
    end
    opt Xuất quá tồn
        K-->>T: E-003 Không báo, tồn âm, nhãn Out of Stock
    end
    opt Sửa số lượng dòng
        T->>W: 5 thành 3
        W->>L: Sổ cộng 2
    end
    opt Xoá dòng
        T->>W: Xác nhận xoá vĩnh viễn dòng
        W->>K: Cộng lại đủ số
        K->>L: Ghi cộng
    end
    T->>W: Open sang Completed
    alt Thiếu Started At, Start Odometer
        W-->>T: E-009 Please edit and fix the following errors
    else Đủ
        W-->>T: Sinh Service Entry, Edit khoá, sổ không có dòng mới
    end
    opt Mở lại lệnh
        T->>W: Completed sang Open
        W-->>T: Khôi phục phần lưu trữ, sổ không đổi, mất liên kết Service Entry
    end
```

Lệch tiền 100 lần ở trang chi tiết lệnh, Service Entry: E-005; hộp Add Part thì đúng. Xoá cả lệnh chưa chạy (OQ-9). Đổi vị trí dòng sang None chưa thử (OQ-12).

## Flow 5: Khai kho và phụ tùng (`Chạy`)

```mermaid
flowchart TD
    A["Settings: tạo kho"] --> B{"Tên kho trùng"}
    B -->|"Có"| C["E-006 has already been taken"]
    B -->|"Không"| D["Kho vào danh mục"]
    C --> A
    D --> E["Tạo phụ tùng: mã, đơn giá"]
    E --> F{"Giá lưu được"}
    F -->|"Có"| G["Bật phụ tùng tại kho"]
    F -->|"Không, gặp ở PT-B"| H["E-024 Giá trị tồn tính 0, phải sửa phụ tùng"]
    H --> G
    G --> I{"Có quyền kho"}
    I -->|"Không"| J["E-002 You do not have access to any Part Locations"]
    I -->|"Có"| K["Nhập tồn đầu, sổ loại Initial, hiện thẻ tồn"]
    J --> L["Cấp quyền, chưa rõ nguyên nhân"]
    L --> G
    K --> KetThuc["Kết thúc"]
```

Thẻ tồn hiện Current Qty, Reorder Point, Pending PO Qty, WO Current Qty. Điểm đặt lại lưu được 0 dù tài liệu nói phải lớn hơn 0 (S4). Tắt khi có đơn bị chặn: E-010.

## Flow 6: Chỉnh tồn và chuyển kho (`Chạy`)

```mermaid
flowchart TD
    A["Thẻ tồn"] --> B{"Thao tác"}
    B -->|"Chỉnh"| C["Hộp chỉnh: Adjust Quantity và New Quantity liên động"]
    B -->|"Chuyển"| D{"Tồn trên 0"}
    C --> E{"Có lý do"}
    E -->|"Không"| F["Save khoá"]
    F --> C
    E -->|"Có"| G{"Giảm quá tồn"}
    G -->|"Có"| H["E-007 Lưu được, tồn âm, không cảnh báo"]
    G -->|"Không"| I["Lưu, chấp nhận số lẻ"]
    H --> J["Sổ loại Manual, cập nhật nhãn"]
    I --> J
    D -->|"Không"| K["Nút chuyển khoá"]
    D -->|"Có"| L["Hộp chuyển: chỉ hiện kho còn lại kèm tồn"]
    L --> M{"Số chuyển lớn hơn tồn"}
    M -->|"Có"| N["E-008 Vẫn báo thành công, chỉ chuyển phần có"]
    M -->|"Không"| O["Chuyển đúng số"]
    N --> P["Sổ loại Transfer: trừ kho nguồn, cộng kho đích"]
    O --> P
    J --> KetThuc["Kết thúc"]
    K --> KetThuc["Kết thúc"]
    P --> KetThuc["Kết thúc"]
```

Nhánh chuyển đúng số là `Suy` từ sổ kho; nhật ký chỉ ghi lần chuyển quá tồn (K7). Đảo ngược: chỉnh tay ngược lại hoặc chuyển ngược, đều ghi dòng sổ mới, không có nút hoàn tác.

## Flow 7: Kiểm kê hàng loạt (`Chạy`)

```mermaid
flowchart TD
    A["Bulk Manage Parts: tab theo kho"] --> B{"Sửa ô nào"}
    B -->|"Current Qty"| C["Tự lưu, All changes saved, sổ loại Bulk Update, không hỏi lý do"]
    B -->|"Active"| D{"Có đơn tại kho"}
    B -->|"Aisle, Row, Bin, Track Inventory"| E["Thấy cột, nhật ký chỉ ghi sửa số và Active"]
    B -->|"Không sửa, in phiếu"| H["Print Worksheet: E-029 tự tải PDF, 3 bản giống hệt"]
    D -->|"Có"| F["E-010 Không tắt"]
    D -->|"Không"| G["Chưa thử"]
    H --> I["Kiểm đếm tay, ghi ô New Qty"]
    I --> C
    C --> KetThuc["Kết thúc"]
    E --> KetThuc["Kết thúc"]
    F --> KetThuc["Kết thúc"]
    G --> KetThuc["Kết thúc"]
```

Print Worksheet `Chạy`: toast "Complete: Bulk Manage Parts Worksheet", không mở tab, PDF in theo kho đang chọn (K27, K28). Từ phiếu giấy về ô Current Qty là `Suy` theo công dụng ô New Qty, chưa thao tác. Sửa số về 0 với điểm đặt lại 0: Out of Stock (S5).

## Flow 8: Phiếu dầu và cảnh báo (`Chạy` phần phiếu và Capacity Alert, `Docs` Vendor Location Alert)

```mermaid
flowchart TD
    A["Chọn xe, ngày, số đồng hồ, số lít, đơn giá"] --> B{"Số đồng hồ và ngày"}
    B -->|"Lùi ngày, số cao"| C["E-019 must be less than 1,000 or marked as void"]
    B -->|"Lùi cùng ngày"| D["E-016 Lưu được, không báo, phiếu sau không tính lại"]
    B -->|"Lùi ngày, số thấp"| E["Lưu được, không đổi phiếu sau"]
    B -->|"Tiến bình thường"| F{"Cờ trên phiếu"}
    C --> A
    D --> F
    E --> F
    F -->|"Void, trống số"| G["E-018 can't be blank"]
    F -->|"Void, có số"| H["Số gạch ngang, đồng hồ xe không đổi, không Usage"]
    F -->|"Partial"| I["Không tiêu hao, số lít cộng sang phiếu đầy kế tiếp"]
    F -->|"Reset usage"| J["Không usage, phiếu sau Usage N/A nhưng vẫn có tiêu hao"]
    F -->|"Personal hoặc không cờ"| K{"Có phiếu trước"}
    G --> A
    K -->|"Không"| L["Usage N/A, không tiêu hao"]
    K -->|"Có"| M["Quãng đường, tiêu hao, chi phí trên km, E-004 hiện mpg"]
    H --> N{"Đã khai dung tích và số lít lớn hơn"}
    I --> N
    J --> N
    L --> N
    M --> N
    N -->|"Có"| O["Capacity Alert, E-017 sửa phiếu không gỡ"]
    N -->|"Không"| P{"Có tích hợp định vị và thẻ"}
    O --> P
    P -->|"Có, theo tài liệu"| Q["Vendor Location Alert nếu xa hơn bán kính"]
    P -->|"Không"| R["Cộng vào chi phí xe và thẻ tổng, kể cả Void, Personal, E-028; đẩy nhắc bảo dưỡng"]
    Q --> R
    R --> S{"Có chọn nhà cung cấp"}
    S -->|"Có"| T["Tạo vị trí xe tại địa chỉ nhà cung cấp, form không báo"]
    S -->|"Không"| KetThuc["Kết thúc"]
    T --> KetThuc
```

Đường đảo ngược: sửa phiếu đổi số lít nhưng không gỡ cảnh báo (E-017, F19); hiệu ứng lên tiêu hao của phiếu sau chỉ đo ở F8. Void không phải đường huỷ: phiếu vẫn cộng vào thẻ tổng (F22). Báo cáo dầu lệch tiền: E-020, kể cả khi lọc (T9, T10); trang chi tiết xe đúng (T6). Tạo vị trí đo một lần (F25); chi tiết ở nhóm Vị trí. Số 0 lít vẫn lưu được (F11). Có áp số lít, dung tích ở phiếu Void không thì chưa thử, sơ đồ vẽ theo đường chung.

## Flow 9: Khai nhà cung cấp (`Chạy`, Find Shops ở Flow 12)

```mermaid
flowchart TD
    A["Tạo từ danh sách hoặc từ ô chọn"] --> B["Form: tên điền sẵn, phân loại theo ngữ cảnh"]
    B --> C{"Thiếu Tên, Address, City, State, Zip, Country"}
    C -->|"Có"| D["E-021 can't be blank"]
    C -->|"Không"| E{"Nhấn Enter ở ô Country"}
    D --> B
    E -->|"Có"| F["E-022 Vừa chọn vừa lưu form"]
    E -->|"Không"| G["Lưu bằng nút"]
    F --> H["Nhà cung cấp được tạo"]
    G --> H
    H --> I{"Phân loại"}
    I -->|"Parts"| J["Chọn được ở đơn mua, tab Purchase Orders"]
    I -->|"Fuel"| K["Chọn được ở phiếu dầu, tab Fuel Entries, phiếu có bản đồ"]
    I -->|"Không chọn"| L["Không hiện ở đơn mua, phiếu dầu theo quy tắc phân loại"]
    J --> KetThuc["Kết thúc"]
    K --> KetThuc["Kết thúc"]
    L --> KetThuc["Kết thúc"]
```

Nhánh không phân loại là `Suy` từ D1 và F-NCC. Nhánh trùng tên nhà cung cấp không có trong nhật ký.

## Flow 10: Số đang về khi đơn tiến và lùi (`Chạy`, chỉ đo trên PO #4)

```mermaid
flowchart TD
    A["Đơn Draft, Pending PO Qty 0"] --> A1{"Sửa rồi lưu"}
    A1 -->|"Có"| A2["E-032 Pending bằng số đặt dù chưa duyệt, theo số mới mỗi lần lưu"]
    A2 --> A1
    A1 -->|"Không"| B["Approve: Approved, Pending vẫn 0"]
    B --> C["Mark as Purchased: Pending bằng số đặt"]
    C --> D{"Thao tác tiếp"}
    D -->|"Sửa số đặt"| E["Pending theo số mới, không cảnh báo"]
    E --> D
    D -->|"Unmark as Purchased"| F["Về Approved, E-026 Pending không giảm"]
    D -->|"Receive"| G["Nhận hàng, xem Flow 1"]
    F --> H{"Đi tiếp từ Approved"}
    H -->|"Mark as Purchased lại"| I["Purchased, Pending không nhân đôi"]
    H -->|"Vào Edit, Save as Draft"| J["Về Draft, mất Approved By, Pending không giảm"]
    J --> K["Approve, Mark as Purchased lại"]
    K --> I
    I --> D
    G --> KetThuc["Kết thúc"]
```

Bảng số đo ở States Mục 1. Nhánh sửa Draft đo trên PO #5 (D40, D41); từ đó đi tiếp Approve chưa đo, sơ đồ không vẽ. Sửa tăng số đặt ở Full không cộng Pending, đơn vẫn Full (D36, D37, E-033). Nhánh Mark as Purchased lại ngay từ Approved không đo riêng, chỉ đo đường qua Draft (D29). Công thức khi lùi là `Suy` (OQ-25).

## Flow 11: Sao chép, in, xem lịch sử đơn (`Chạy`)

```mermaid
flowchart TD
    A["Menu đơn"] --> B{"Chọn mục"}
    B -->|"Make a Copy"| C["Form New Purchase Order, số mới, chép nhà cung cấp, kho, dòng, số đặt, giá, chiết khấu, không chép số nhận"]
    B -->|"Print"| D["Tab mới Preparing your PDF, ra PDF một trang, tiền kiểu US"]
    B -->|"View Record History"| E["Hộp Record History, lọc theo khoảng ngày"]
    C --> F{"Lưu form"}
    F -->|"Save as Draft"| G["Đơn mới Draft, chưa Edit nên Pending vẫn 0"]
    F -->|"Không lưu"| H["Không tạo đơn, chưa thử"]
    D --> KetThuc["Kết thúc"]
    E --> KetThuc
    G --> KetThuc
    H --> KetThuc
```

Save & Approve trên form copy chưa thử. Copy từ đơn đã sửa lấy số đặt, giá đã sửa (D39). Báo cáo đơn mua cộng cả Draft vào Total Amount: E-034. Đơn Approved sau Unmark vẫn in Purchase Date, Purchased By (D35). Record History: phần ảnh đọc được chỉ có trạng thái và tiền (D20, OQ-22).

## Flow 12: Tìm xưởng (`Chạy` tới bước tick, Add Vendor không bấm)

```mermaid
flowchart TD
    A["Vendors, Find Shops"] --> B["Gõ địa chỉ, thành phố hoặc mã bưu chính, chọn Shop type, Let's Go"]
    B --> C["Danh sách cửa hàng và bản đồ, All Results"]
    C --> D{"Tick cửa hàng"}
    D -->|"Có"| E["SELECTED, Clear selection, ghim đỏ, khoảng cách, nút Add Vendor"]
    D -->|"Không"| F["Huỷ, không tạo gì"]
    E --> G{"Bấm Add Vendor"}
    G -->|"Có, chưa thử"| H["Tạo nhà cung cấp, kết quả chưa biết"]
    G -->|"Huỷ"| F
    H --> KetThuc["Kết thúc"]
    F --> KetThuc
```

Không bấm Add Vendor vì sẽ tạo nhà cung cấp trùng tên doanh nghiệp thật (N8). Network Status: Invite không bấm (N11).

## Flow 13: Lọc phiếu dầu (`Chạy`)

```mermaid
flowchart TD
    A["Fuel History, Date 30 ngày khoá"] --> B{"Cách lọc"}
    B -->|"Ô Vendor"| C["Chọn nhiều, mọi nhà cung cấp, áp vào danh sách"]
    B -->|"Filters, Add Filter"| D["Chọn trường và điều kiện"]
    D --> E{"Bấm Apply"}
    E -->|"Có"| F["Danh sách và thẻ tổng tính lại, E-020 tiền lệch 100 lần"]
    E -->|"Chưa"| D
    C --> F
    F --> G{"Xoá một điều kiện"}
    G -->|"Có"| H["Áp ngay, không cần Apply"]
    G -->|"Không"| KetThuc["Kết thúc"]
    H --> KetThuc
```

Đã lọc Vendor (1 phiếu), Fuel Capacity Alert (2 phiếu), Personal (1 phiếu), theo xe (F16, F19, F20, F22). Nhóm OR thứ 4 chưa thử; Fleetio: tối đa 3 theo câu trên panel. Trường thẻ có ở bộ lọc nhưng không có dữ liệu thẻ để lọc (F24).
