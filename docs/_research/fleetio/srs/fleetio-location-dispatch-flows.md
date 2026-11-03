---
type: research
feature: fleetio-location-dispatch
updated: 2026-11-03
---

# Bản đồ, gán việc — Flows

Mã lỗi viết tắt, đầy đủ có tiền tố `E-fleetio-location-dispatch-`.

## Flow 1: Xem đội xe (`Chạy (vị trí giả lập)`, gọi dữ liệu theo khung là `Chạy`)

```mermaid
sequenceDiagram
    actor U as Người dùng
    participant M as Bản đồ
    participant A as Dịch vụ vị trí
    participant N as Danh sách Nearby
    participant P as Panel trái
    U->>M: Mở bản đồ
    M->>A: Lấy điểm mở theo IP
    A-->>M: Tâm bản đồ, không thu về xe
    M->>A: Lấy vị trí theo khung nhìn
    alt Khung không có xe
        A-->>N: Rỗng
        N-->>U: E-001 No results found in this area
        U->>M: Tìm ở ô Locate, kéo hoặc đổi lọc
        M->>A: Gọi lại theo khung mới
    else Khung có xe
        A-->>M: Vị trí gần nhất, độ tươi
        M->>N: Danh sách sắp Distance, có tuổi vị trí
    end
    U->>M: Bấm marker hoặc dòng
    M->>P: Đổi panel sang xe, không có popup
    P-->>U: Overview, Last Known Location, Source
    U->>P: Mở Nearby, Show Places
    P-->>U: Dòng Place có khoảng cách
    U->>P: Rê chuột dòng Place
    P->>M: Vẽ nét đứt, marker xe đổi thành marker Place
    U->>P: Rời chuột
    P->>M: Trả marker xe (Suy)
```

Bỏ tích "Update list when map moves": chưa thấy khác biệt rõ, chưa thử kéo tay (OQ-6). Map Options lưu theo người dùng, đổi lại được.

## Flow 2: Khai địa điểm, vùng (`Chạy`)

```mermaid
flowchart TD
    A["Add Place"] --> B["Gõ tên, toạ độ"]
    B --> C["Address tự điền, bản đồ tự chuyển"]
    C --> D{"Loại vùng"}
    D -->|"Tròn"| E["Chọn bán kính hoặc gõ số"]
    D -->|"Đa giác"| F["Bấm đỉnh, bấm lại đỉnh đầu"]
    E --> G["Vòng tròn đổi ngay"]
    F --> H["Toạ độ thành tâm, Address đổi, Radius khoá"]
    G --> I{"Thao tác tiếp"}
    H --> I
    I -->|"Bấm nhầm bản đồ"| J["Pin, Address, toạ độ đổi, Name giữ"]
    J --> B
    I -->|"Rời form"| K["E-010 Leave site, tab kẹt"]
    K --> Z["Kết thúc"]
    I -->|"Save Place"| L["Place was successfully created"]
    L --> M["Trang chi tiết"]
    M --> N{"Sửa"}
    N -->|"Edit"| B
    N -->|"Không"| Z
```

Đa giác 2 đỉnh: form không chặn, chưa thử lưu (OQ-10). Bỏ đa giác để quay về vòng tròn: chưa thử.

## Flow 3: Vị trí từ phiếu kiểm web (`Chạy`; toạ độ giả là `Chạy (vị trí giả lập)`)

```mermaid
sequenceDiagram
    actor K as Người kiểm tra
    participant W as Web app
    participant T as Trình duyệt
    participant S as Máy chủ
    participant G as Dịch vụ địa chỉ
    W->>T: Đọc vị trí 1 lần lúc khởi động app
    alt Có quyền định vị
        T-->>W: Toạ độ, giữ lại
    else Không có quyền (Suy)
        T-->>W: Không có toạ độ
    end
    K->>W: Mở form, điền, Submit
    Note over K,W: Form không báo đang gửi vị trí
    alt Đồng hồ sai theo lịch sử
        W-->>K: E-012
        K->>W: Sửa số, Submit lại
    end
    W->>S: Phiếu kèm toạ độ cấp phiếu, nếu có
    alt Có toạ độ
        S->>S: Lưu đúng toạ độ, không kiểm hợp lệ
        S->>S: Tạo Location Entry, gắn initial_place
        S-->>K: Phiếu có bản đồ nhỏ, Source Fleetio Web App
        S->>G: Tra địa chỉ ngược
        G-->>S: Địa chỉ, sau khoảng 1 phút
    else Không có toạ độ
        S-->>K: Phiếu không có vị trí
    end
```

Phiếu dầu, phiếu dịch vụ trên web không có ô vị trí nên không có đường này (`Chạy`). API `POST /vehicles/:id/location_entries` và thiết bị là nguồn khác (`Docs`).

## Flow 4: Sự kiện vùng và hệ quả (`Chạy (vị trí giả lập)`, bước so sánh là `Suy`)

```mermaid
flowchart TD
    A["Location Entry mới"] --> B{"So với vùng các Place"}
    B -->|"Không đổi quan hệ"| C["Chỉ cập nhật vị trí"]
    B -->|"Mới vào"| D["Entered"]
    B -->|"Mới ra"| H["Exited"]
    B -->|"Từ A sang B"| X["Exited A và Entered B"]
    D --> E{"Việc gắn Place bật tự động"}
    H --> R{"Có lượt Geofence đang chạy"}
    X --> E
    X --> R
    E -->|"Có"| F["Thêm lượt, Added = Geofence, chip"]
    E -->|"Không"| Y{"Có Automation khớp"}
    R -->|"Có"| L["Lượt có End, xe về Unassigned"]
    R -->|"Không"| Y
    F --> Y
    L --> Y
    Y -->|"Có"| Q["Chạy hành động trên xe"]
    Y -->|"Không"| Z["Kết thúc"]
    Q --> Z
    C --> Z
```

Phiếu làm xe ra vùng vẫn mang `job_assignment` của việc đó, vì phiếu ghi lại việc đang gán lúc nộp. Xe đang có việc khác, xe đã trong vùng khi bật ô, chống nhiễu mép vùng: chưa kiểm (OQ-8, OQ-9). Không có màn xem lại sự kiện.

## Flow 5: Tạo việc (`Chạy`)

```mermaid
flowchart TD
    A["Jobs"] --> B{"Đã có việc"}
    B -->|"Chưa"| C["Nút giữa màn trống"]
    B -->|"Rồi"| D["Nút góc phải"]
    C --> E["Form Add Job"]
    D --> E
    E --> F{"Đủ Job Number, Job Name"}
    F -->|"Thiếu"| G["E-003 can't be blank"]
    G --> E
    F -->|"Đủ"| H["Job created successfully, Active"]
    H --> I["Start Date/Time tự lấy, thêm cột"]
    I --> Z["Kết thúc"]
```

## Flow 6: Gán tay và kết thúc, kể cả đảo ngược (`Chạy`)

```mermaid
flowchart TD
    A["Tích xe trong cột"] --> B{"Xe đang có việc"}
    B -->|"Không"| C["Actions, Assign"]
    B -->|"Có"| D["E-009 Assign mờ, chỉ còn Unassign"]
    C --> E["Chọn Job, Start Date/Time"]
    E --> F{"Giờ hợp lệ"}
    F -->|"Tương lai"| G["E-004 cannot be in the future"]
    G --> E
    F -->|"Chồng khoảng cũ"| H["E-005 overlaps with historical Assignment"]
    H --> E
    F -->|"Hợp lệ"| I["Lượt Active, On job đếm giờ"]
    I --> J{"Thao tác tiếp"}
    D --> K["Hộp Unassign from Job"]
    J -->|"Unassign"| K
    J -->|"Edit"| L["Chỉ sửa Start Date/Time"]
    L --> I
    K --> M{"Đã bấm vào ô giờ"}
    M -->|"Chưa"| N["E-006 Băng đỏ không rõ lỗi"]
    N --> K
    M -->|"Rồi"| O["Lượt có End, xe về Unassigned"]
    O --> P{"Đảo ngược"}
    P -->|"Gán lại"| A
    P -->|"Không"| Z["Kết thúc"]
```

Kéo thả thẻ xe không hoạt động. Không có chuyển thẳng xe sang việc khác. Đảo ngược việc kết thúc chỉ bằng cách tạo lượt mới, giờ không chồng lượt cũ; Delete lượt chưa thử.

## Flow 7: Hoàn thành việc (`Chạy`)

```mermaid
flowchart TD
    A["Menu cột, Complete"] --> B["Hộp Complete Job, End Date/Time"]
    B --> C{"Giờ hợp lệ"}
    C -->|"Trước giờ bắt đầu lượt"| D["E-007 must be after active assignment"]
    D --> B
    C -->|"Tương lai"| E["E-008 End date cannot be in the future"]
    E --> B
    C -->|"Hợp lệ"| F["Job completed successfully"]
    F --> G["Xe đang gán tự kết thúc, không hỏi"]
    G --> H["Việc sang tab Completed"]
    H --> Z["Kết thúc"]
```

Mở lại việc đã hoàn thành: chưa thấy đường (OQ-13).

## Flow 8: Automation theo sự kiện vùng (`Chạy (vị trí giả lập)`)

```mermaid
sequenceDiagram
    actor A as Admin
    participant B as Automation
    participant S as Sự kiện vùng
    participant X as Xe
    A->>B: Record Type Geofence Event, Trigger Created
    A->>B: Điều kiện Vehicle, hành động Add Comment, bật
    S->>B: Sự kiện của xe, 2 lần khi đi từ vùng A sang B
    B->>X: Thêm comment của Fleetio Automation
    B-->>A: Total Runs 2, Successful 2
    alt Xem Run Result
        B-->>A: E-011 No records changed, bước ActionSet DNF
        A->>X: Xem xe để biết kết quả thật
    end
    A->>B: Tắt
    B-->>A: Automation disabled
```

Không có điều kiện Geofence Event Type thì chạy cả vào lẫn ra (`Suy`). Update Field, Send Email chưa chạy.

## Flow 9: Cảnh báo vùng (`Xem`, chưa lưu)

```mermaid
flowchart TD
    A["Trang Place, Add Alert Policy"] --> B["Chọn Trigger trong hoặc ngoài vùng"]
    B --> C["Which Vehicles, Recipients, Email Message"]
    C --> D{"Thao tác"}
    D -->|"Cancel"| Z["Kết thúc"]
    D -->|"Lưu, chưa thử"| E{"Receive as Summary"}
    E -->|"Bật"| F["Tổng hợp hằng ngày của ngày trước"]
    E -->|"Tắt"| G["Gửi khi phát hiện"]
    F --> Z
    G --> Z
```

Hai nhánh lưu lấy từ câu chữ trên form, chưa chạy (OQ-12).

## Flow 10: Quick Add từ bản đồ (`Chạy (vị trí giả lập)` với Add Issue, còn lại `Xem`)

```mermaid
flowchart TD
    A["Panel xe"] --> B["Nút Add, 11 mục"]
    B --> C{"Chọn"}
    C -->|"Add Issue"| D["Form New Issue điền sẵn xe"]
    C -->|"10 mục khác, chưa mở"| E["Chưa biết"]
    D --> F["Lưu, về trang sự cố"]
    F --> G["Rời bản đồ, phải quay lại Fleet Map"]
    E --> Z["Kết thúc"]
    G --> Z
```

## Flow 11: Location Exception trên web (`Chạy (vị trí giả lập)`, nguyên nhân là `Suy`)

```mermaid
flowchart TD
    A["Biểu mẫu Location Exception Tracking: Enabled"] --> B["Nộp phiếu trên web"]
    B --> C{"Có toạ độ từng mục"}
    C -->|"Không, chỉ 1 cặp cấp phiếu"| D["location_exception = false"]
    C -->|"Có, Fleetio Go, chưa kiểm"| E["Chưa biết"]
    D --> F["Không so với phiếu trước, kể cả lệch rất xa"]
    F --> Z["Kết thúc"]
    E --> Z
```
