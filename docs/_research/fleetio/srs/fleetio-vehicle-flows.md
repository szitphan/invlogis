---
type: research
feature: fleetio-vehicle
updated: 2026-11-03
---

# Phương tiện — Flows

Mã lỗi viết tắt `E-0NN` là `E-fleetio-vehicle-0NN`. Mức ghi ở tiêu đề từng luồng. Luồng lốp: [[docs/_research/fleetio/srs/fleetio-tires-flows.md|Flows Lốp]].

## Flow 1: Gán xe (`Chạy`)

```mermaid
sequenceDiagram
    actor M as Quản lý phương tiện
    participant F as Form gán xe
    participant A as Lần gán
    participant V as Trang xe
    M->>F: Chọn xe, người lái, hoặc bấm ô trống trên lịch
    alt Liên hệ không phải Operator
        F-->>M: E-012, không có trong ô chọn
    else Enter khi tên chưa có
        F-->>M: E-003, mở Add Contact
    else Đủ xe và người
        F-->>M: Hiện Starting Odometer, Ending Odometer
        M->>F: Thời gian, số km, ghi chú
        alt Chồng khoảng khác của cùng xe
            F-->>M: E-001, không lưu, không đóng lần cũ
        else Không chồng, kể cả người đang giữ xe khác
            F->>A: Lưu lần gán
            A->>V: Cập nhật người lái hiện tại khi đang trong khoảng
            V-->>M: Hiện tên ở đầu trang, thanh trên lịch
        end
    end
```

Nhánh đảo ngược: Delete trên menu thanh (`Xem`, chưa bấm). Múi giờ: E-017.

## Flow 2: Đổi người lái giữa chừng (`Chạy`)

Fleetio không có hành động riêng. Có hai đường.

```mermaid
flowchart TD
    A["Cần đổi người lái"] --> B{"Phân công đã bắt đầu chưa"}
    B -->|"Chưa, Future"| C["Edit, đổi Operator, xe khoá"]
    C --> D["Lưu đè, mất dấu người cũ trên trang chi tiết"]
    B -->|"Rồi"| E["Tự nhập End cho phân công cũ, Suy"]
    E --> F["Tạo phân công mới cho người mới"]
    F --> G{"Khoảng có chồng không"}
    G -->|"Có"| H["E-001, quay lại sửa ngày"]
    H --> F
    G -->|"Không"| I["Xong, có hai bản ghi"]
    D --> J["Kết thúc"]
    I --> J
```

Sửa phân công đã qua chưa thử.

## Flow 3: Ghi số đồng hồ (`Chạy`; Out of Sequence là `Docs`)

```mermaid
flowchart TD
    A["Số mới từ lệnh, dầu, kiểm tra, tay, thiết bị"] --> V{"Tick Void"}
    V -->|"Có"| MV["Lưu, Manually Voided, không đổi đồng hồ"]
    V -->|"Không"| B{"Lệch thứ tự so với ngày trước, ngày sau"}
    B -->|"Có, nguồn có người sửa"| R["Từ chối ở trường: E-004, E-005, E-008"]
    R --> R2{"Người dùng chọn"}
    R2 -->|"Sửa số"| A
    R2 -->|"Tick Void"| MV
    B -->|"Có, nguồn thiết bị, Docs"| OS["Tự Void: Out of Sequence, E-019"]
    B -->|"Không"| C{"Vượt mức tối đa một ngày"}
    C -->|"Có"| AV["Lưu, Auto-Voided: Exceeds Max. Daily Usage, E-006"]
    AV --> CS["Dòng gốc gắn Conflict Source, E-007"]
    C -->|"Không"| D{"Lớn hơn số hiện tại"}
    D -->|"Có"| G["Thành số hiện tại, tính lại nhắc, chi phí trên km"]
    D -->|"Không, cùng ngày"| H["Lưu như số cũ, không báo, E-002"]
    OS --> CS
    CS --> K["Kết thúc, xem Flow 4 nếu cần sửa"]
    MV --> K
    G --> K
    H --> K
```

## Flow 4: Sửa số sai, nhánh đảo ngược (`Chạy` phần Unvoid; `Docs` phần Void gốc)

```mermaid
flowchart TD
    A["Mở sổ đồng hồ, thấy cờ đỏ hoặc Auto-Voided"] --> B{"Số bị Void có đúng không"}
    B -->|"Đúng, xe thật chạy vậy"| C["Unvoid this Entry, Confirm, không hỏi lý do"]
    C --> D["Đồng hồ lên số đó, cờ Conflict Source tự mất"]
    B -->|"Sai"| E["Giữ Void, nhập lại số đúng"]
    B -->|"Dòng gốc mới là sai, Docs"| F["Void dòng gốc, bỏ Void từng dòng sau"]
    D --> G{"Unvoid nhầm"}
    G -->|"Có"| H["Số thật sau đó bị E-015, phải Void lại, Suy"]
    G -->|"Không"| I["Kết thúc"]
    E --> I
    F --> I
    H --> I
```

Thay đồng hồ: Bulk Meter Management Void toàn bộ số của xe (`Docs`, chưa chạy).

## Flow 5: Tạo xe và mooc (`Chạy`)

```mermaid
flowchart TD
    A["New Vehicle"] --> B{"Còn hạn mức xe"}
    B -->|"Không"| E9["E-009, nút khoá, dừng"]
    B -->|"Có"| C["Nhập 6 phần, chọn Type"]
    C --> D{"Đủ trường bắt buộc"}
    D -->|"Thiếu"| E10["E-010, quay lại form"]
    E10 --> C
    D -->|"Đủ"| F{"Type là Trailer"}
    F -->|"Có"| G["Xe mooc riêng, đồng hồ trống thành 0 km"]
    F -->|"Không"| H["Xe thường, trang xe có khối rỗng"]
    G --> Z["Kết thúc"]
    H --> Z
    E9 --> Z
```

## Flow 6: Liên kết đầu kéo và mooc (`Chạy`)

```mermaid
sequenceDiagram
    actor M as Quản lý phương tiện
    participant D as Đầu kéo
    participant T as Mooc
    M->>D: Sửa xe, thêm mooc vào Linked Vehicles
    D-->>M: Linked Assets hiện mooc
    T-->>M: Linked Assets hiện đầu kéo
    Note over D,T: Không gộp lốp, không truyền km, không có ngày
    opt Đổi mooc
        M->>D: Xoá chip
        T-->>M: There are no linked Assets for this Vehicle
        M->>T: Gắn lại từ phía mooc hoặc đầu kéo khác
    end
```

Một mooc gắn nhiều đầu kéo: không chạy (OQ-16).

## Flow 7: Chi phí và chi phí trên km (`Chạy`)

```mermaid
flowchart TD
    A["Add Expense Entry"] --> B{"Frequency"}
    B -->|"Single Expense"| C["Lưu một dòng"]
    B -->|"Recurring Expense"| D{"Đã gõ Start Date thật"}
    D -->|"Chưa, chỉ chữ xám"| E["E-011, quay lại nhập"]
    E --> D
    D -->|"Rồi"| F["Xử lý nền, sinh dòng từng kỳ trong Future"]
    F --> G["Có thể cần tải lại trang"]
    C --> H["Cost of Ownership tính dòng đã đến ngày"]
    G --> H
    H --> I["Cost Per Meter bằng tổng chia km đã chạy trong kỳ"]
    I --> J["Kết thúc"]
```

Xoá, sửa dòng định kỳ: chưa thử.

## Flow 8: Bảo hành và cơ hội trên lệnh (`Chạy`; claim chưa thử)

```mermaid
flowchart TD
    A["Add Warranty"] --> B["Chọn xe, mỗi xe Start Date, Start Meter"]
    B --> C{"Coverage Type"}
    C -->|"Standard templates"| T{"Có mẫu"}
    T -->|"Không"| U["E-016 No options, chọn lại"]
    U --> C
    T -->|"Có, chưa chạy"| D["Coverage theo mẫu"]
    C -->|"Standard, Extended"| D2["Nhập thời hạn, quãng đường"]
    D --> E["Gắn mã bảo dưỡng"]
    D2 --> E
    E --> F["Tự tính End Date, End Meter, Active"]
    F --> G["Mở lệnh trên xe đó"]
    G --> H{"Service Task cùng mã"}
    H -->|"Không, kể cả có phụ tùng cùng loại"| I["No vehicle warranty opportunities to show"]
    H -->|"Có"| J["Warranty Opportunities, View Active Coverage"]
    I --> K["Kết thúc"]
    J --> K
```

E-014: Start Meter nhập 1000 hiện 1 km.

## Flow 9: Đổi trạng thái, Archive (`Xem`)

```mermaid
flowchart TD
    A["Trang xe"] --> B{"Việc cần làm"}
    B -->|"Đổi trạng thái"| C{"Có quyền update_status"}
    C -->|"Có"| D["Đổi tự do, có lịch sử"]
    C -->|"Không"| E["Không thao tác được, Suy"]
    B -->|"Lưu trữ"| F{"Có quyền archive_delete"}
    F -->|"Có"| G["Archive, sang tab Archived, chưa chạy"]
    F -->|"Không, như Operator"| E
    D --> H["Kết thúc"]
    E --> H
    G --> H
```

Automation đổi trạng thái theo sự cố, lệnh: `Xem` mẫu, xem nhóm Nền tảng.

## Flow 10: Phân tích thay xe (`Chạy` đọc)

```mermaid
flowchart TD
    A["Vehicles, Replacement Analysis"] --> B["Hiện tham số mặc định, không chọn xe"]
    B --> C["Vẽ chi phí trên km theo tuổi xe"]
    C --> D["Mốc Optimal Replacement, Estimated Replacement"]
    D --> E{"Đổi tham số"}
    E -->|"Có, chưa thử"| F["Docs: vẽ lại, chưa biết có lưu không"]
    E -->|"Không"| G["Kết thúc"]
    F --> G
```
