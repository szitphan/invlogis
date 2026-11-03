---
type: research
feature: fleetio-saas-platform
updated: 2026-11-03
---

# Nền tảng SaaS — Flows

## Flow 1: Kiểm quyền hai lớp (`Suy` từ `Docs`, cấu hình `Xem`, chưa kiểm hiệu lực thật)

Bước đảo ngược: đổi Role hoặc Record Set của người dùng; Record Type của Record Set không đổi được, phải tạo mới (E-fleetio-saas-platform-008).

```mermaid
flowchart TD
    A["Người dùng thao tác"] --> B{"Role cho phép hành động?"}
    B -->|"Không"| C["E-fleetio-saas-platform-001 Không có quyền"]
    B -->|"Có"| D{"Record Set có bản ghi này?"}
    D -->|"Không"| E["Không thấy hoặc không chọn được"]
    D -->|"Có, chỉ View"| F["Chỉ xem"]
    D -->|"Có, Manage"| G["Thực hiện"]
    C --> Z["Kết thúc"]
    E --> Z
    F --> Z
    G --> Z
```

## Flow 2: Tự động hoá (`Chạy` Issue, Add Comment, Update Field, Create Record)

```mermaid
sequenceDiagram
    actor A as Admin
    participant B as Trình dựng
    participant E as Hệ thống
    participant R as Bản ghi
    A->>B: Add Automation hoặc Browse Templates
    A->>B: Chọn loại bản ghi và kiểu sự kiện
    A->>B: Thêm điều kiện tuỳ chọn, thêm hành động
    A->>B: Save, lưu ở trạng thái tắt
    A->>B: Gạt bật, xác nhận
    B->>E: Sinh phiên bản v.1
    R->>E: Sự kiện xảy ra
    E->>E: Kiểm điều kiện
    alt Đạt
        E->>R: Update Field, Add Comment, Create Record
        E->>E: Ghi lượt chạy SUCCESS, trong vòng 6 giây
        R-->>E: Nếu giá trị đổi, sinh sự kiện Update, kiểm lại
    else Không đạt
        E->>E: Bỏ qua, không đếm lượt
    end
```

## Flow 3: Khách mới (`Chạy` một phần)

```mermaid
flowchart TD
    A["Đăng ký"] --> B["Có dữ liệu mẫu nhãn Sample, không tính hạn mức"]
    B --> C["Onboarding Tasks trên trang đầu, 7 đường dẫn"]
    C --> D["Làm từng việc, khung Learn hướng dẫn"]
    D --> E{"Đã sẵn sàng?"}
    E -->|"Chưa"| D
    E -->|"Rồi"| F["Disable Sample Data"]
    F --> G["Kết thúc"]
```

## Flow 4: Tạo và bật automation từ mẫu, có nhánh lỗi và đảo ngược (`Chạy`)

```mermaid
flowchart TD
    A["Browse Templates"] --> B["Apply mẫu, mở trình dựng, chưa lưu"]
    B --> C{"Mẫu đủ giá trị?"}
    C -->|"Thiếu"| D["E-fleetio-saas-platform-009 Missing Value hoặc để trống"]
    D --> E["Chọn giá trị"]
    E --> F
    C -->|"Đủ"| F{"Có trigger và hành động?"}
    F -->|"Chưa"| G["Save mờ"]
    G --> E
    F -->|"Có"| H{"Bấm Save hay rời trang?"}
    H -->|"Rời trang"| I["Không để lại bản rác"]
    H -->|"Save"| J["Disabled, chưa chạy"]
    J --> K{"Bật?"}
    K -->|"Chưa"| L["Sự kiện không tạo lượt chạy"]
    K -->|"Gạt, xác nhận"| M["Enabled, sinh v.1"]
    M --> N{"Dừng thế nào?"}
    N -->|"Gạt tắt, xác nhận"| J
    N -->|"Archive"| O["Archived, tắt ngay, chỉ đọc"]
    O --> P{"Restore?"}
    P -->|"Có"| J
    P -->|"Sửa khi chưa Restore"| Q["E-fleetio-saas-platform-005 Chỉ đọc"]
    I --> Z["Kết thúc"]
    L --> Z
    Q --> Z
```

## Flow 5: Một sự kiện đi qua automation (`Chạy`)

```mermaid
flowchart TD
    A["Issue được tạo hoặc sửa"] --> B{"Automation đang bật?"}
    B -->|"Tắt"| C["Không lượt chạy, không chạy bù khi bật sau"]
    B -->|"Bật"| D{"Khớp điều kiện? Không phân biệt hoa thường"}
    D -->|"Không"| E["Total Runs không đổi"]
    D -->|"Có"| F["Chạy hành động, mọi automation khớp đều chạy"]
    F --> G{"Hành động xong?"}
    G -->|"Có"| H["Lượt SUCCESS"]
    G -->|"Lỗi, chưa tái hiện"| I["E-fleetio-saas-platform-011 Failed Runs"]
    H --> J{"Bản ghi có đổi và trigger gồm Updated?"}
    J -->|"Có"| A
    J -->|"Không đổi nữa"| K["Dừng"]
    C --> Z["Kết thúc"]
    E --> Z
    I --> Z
    K --> Z
```

Vòng lặp giữa hai automation lật giá trị chưa chạy (OQ-5). Lượt do automation gây ra vẫn ghi "Triggered By" là người tạo Issue; lượt chỉ thêm comment ghi "Records: No records changed".

## Flow 6: Sự cố sinh lệnh sửa (`Chạy` đến khi WO Open)

```mermaid
sequenceDiagram
    actor U as Người dùng
    participant I as Issue
    participant E as Automation
    participant W as Work Order
    U->>I: Tạo Issue khớp điều kiện
    I->>E: Sự kiện Created
    E->>W: Create Record, Status Open
    W-->>I: Resolved Issues trỏ về Issue
    Note over E,W: Hành động chỉ cho Open, Pending, không có Completed
    U->>W: Hoàn tất lệnh, xem nhóm Sửa chữa
    W-->>I: Giải quyết Issue, theo câu trên màn
```

## Flow 7: Tạo xe khi có hạn mức (`Chạy` nhánh chặn)

```mermaid
flowchart TD
    A["Mở New Vehicle"] --> B["Nhập form, bấm Save"]
    B --> C{"Có Vehicle Name?"}
    C -->|"Không"| D["E-fleetio-saas-platform-004 can't be blank, toast"]
    D --> E{"Còn hạn mức?"}
    C -->|"Có"| E
    E -->|"Hết, 5 of 5"| F["E-fleetio-saas-platform-003 Your plan is limited to 5 vehicles"]
    E -->|"Còn, chưa chạy"| G["Lưu xe, chưa kiểm"]
    F --> H{"Xử lý?"}
    H -->|"Explore Plans"| I["Nâng gói, không làm"]
    H -->|"Add Multiple hoặc nhập tệp"| J["Không thử vì là lách hạn mức"]
    G --> Z["Kết thúc"]
    I --> Z
    J --> Z
```

## Flow 8: Liên hệ thành người dùng (`Chạy` No Access, `Xem` Enable Access)

```mermaid
flowchart TD
    A["Add Contact"] --> B["Nhập First Name, tick phân loại"]
    B --> C["Lưu, không cần email, trùng tên vẫn lưu"]
    C --> D{"Cần gán xe?"}
    D -->|"Có, chưa tick Operator"| E["E-fleetio-saas-platform-006 Phải có Operator"]
    E --> F["Tick Operator"]
    F --> G["Gán được, chưa chạy"]
    D -->|"Không"| H{"Cần đăng nhập?"}
    G --> H
    H -->|"Không"| I["No Access, không nhận thông báo"]
    H -->|"Có"| J["Enable Access to Fleetio, chọn Role, Record Set, không mời người"]
    I --> Z["Kết thúc"]
    J --> Z
```

## Flow 9: Chia sẻ báo cáo (`Chạy`)

```mermaid
flowchart TD
    A["Mở Issues Report"] --> B["Bấm Share"]
    B --> C["E-fleetio-saas-platform-013 Link công khai sinh ngay, hạn 7 ngày"]
    C --> D{"Muốn thu hồi?"}
    D -->|"Không"| E["Ai có link xem được dữ liệu đến khi hết hạn"]
    D -->|"Bấm lối trong hộp"| F["E-fleetio-saas-platform-010 Không tác dụng, bấm lại 404, link vẫn sống"]
    F --> G["Reports, Shared, Unshare"]
    D -->|"Vào Reports, Shared"| G
    G --> H{"Xác nhận Are you sure?"}
    H -->|"Không"| E
    H -->|"Có"| I["Shared về 0, mở lại không còn báo cáo"]
    E --> Z["Kết thúc"]
    I --> Z
```

Đề xuất Invlogis: nhánh thay thế là mở hộp không có link, bấm tạo mới có, nói rõ phạm vi, ghi nhật ký (NFR-fleetio-saas-platform-010).

## Flow 10: Xuất và in báo cáo (`Xem` nút, chưa bấm)

```mermaid
flowchart TD
    A["Mở báo cáo"] --> B["Filters, Columns"]
    B --> C{"Có dữ liệu?"}
    C -->|"Không"| D["E-fleetio-saas-platform-002 Không có dữ liệu"]
    D --> B
    C -->|"Có"| E{"Chọn thao tác"}
    E -->|"Export CSV"| F["Export Visible Columns hoặc Export All Columns"]
    E -->|"Print"| G["In"]
    E -->|"Save"| H["Vào Saved, chưa đọc"]
    F --> Z["Kết thúc"]
    G --> Z
    H --> Z
```

## Flow 11: Hỏi dữ liệu bằng lời (`Chạy` 2 câu)

```mermaid
sequenceDiagram
    actor U as Người dùng
    participant A as AI Data Analyst
    participant K as Kho phân tích
    participant X as Trang xe
    U->>A: Hỏi bằng lời
    A->>K: Truy vấn, nguồn dữ liệu là suy luận
    K-->>A: Số liệu, không ghi thời điểm
    A-->>U: Trả lời sau khoảng 40 đến 50 giây
    Note over U,A: E-fleetio-saas-platform-012 Số sai không báo lỗi
    opt Người dùng muốn kiểm
        U->>A: Show work
        U->>X: Đối chiếu tay
        X-->>U: Số thật khác, 7 so với 2, 2.999 so với 1.700
    end
```

## Flow 12: Từ trang đầu tới việc cần xử lý (`Chạy`)

```mermaid
flowchart TD
    A["Trang đầu"] --> B{"Thẻ có số?"}
    B -->|"Có"| C["Bấm số"]
    B -->|"ROs Needing Approval rỗng"| D["Không có đích"]
    C --> E["Danh sách đã lọc theo đường dẫn của thẻ"]
    E --> F{"Có dòng?"}
    F -->|"Không"| G["E-fleetio-saas-platform-002 Không có dữ liệu"]
    F -->|"Có"| H["Mở bản ghi"]
    D --> Z["Kết thúc"]
    G --> Z
    H --> Z
```

## Flow 13: Bật luật theo khách (`Xem`, không Save)

```mermaid
flowchart TD
    A["Mở trang Settings"] --> B["Đọc câu mô tả dưới ô"]
    B --> C{"Điều kiện tiên quyết đủ?"}
    C -->|"Thiếu, Require Group"| D["E-fleetio-saas-platform-007 Gán nhóm cho đủ"]
    D --> A
    C -->|"Đủ"| E["Tick, loại trừ theo loại xe nếu có, Save"]
    E --> F["Chỉ áp cho bản ghi về sau"]
    F --> G{"Đổi ý?"}
    G -->|"Có"| H["Bỏ tick, bản ghi đã làm giữ nguyên, Suy"]
    G -->|"Không"| Z["Kết thúc"]
    H --> Z
```
