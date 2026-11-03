---
type: research
feature: fleetio-tires
updated: 2026-11-03
---

# Quản lý lốp — Flows

## Flow 1: Khai cấu hình trục (`Chạy`)

```mermaid
flowchart TD
    A["Mở tab Tire Management"] --> B{"Xe đã khai trục"}
    B -->|"Chưa"| C{"Biết cấu hình"}
    C -->|"Không"| D["Asset Type"]
    D -->|"Vehicle"| E["Wheel Positions 4, 6, 8, 10"]
    E --> F["Axle Type"]
    D -->|"Trailer"| G["Chọn 1 trong 7 cấu hình mooc"]
    C -->|"Có"| H["Danh sách 27 cấu hình"]
    F --> I["Lưu"]
    G --> I
    H --> I
    I --> J["Sơ đồ, mọi ô trống"]
    B -->|"Rồi"| K{"Xe có lốp"}
    K -->|"Có"| L["E-002 Edit khoá"]
    L -->|"Remove All"| M["Edit mở lại, lịch sử giữ nguyên"]
    M --> H
    K -->|"Không"| H
    J --> KetThuc["Kết thúc"]
```

Đổi cấu hình làm vai trò trục đã đặt về mặc định. Đổi vai trò trục làm được cả khi khoá, không có dòng lịch sử.

## Flow 2: Lắp lốp (`Chạy`)

```mermaid
flowchart TD
    A["Bấm ô cộng hoặc Add"] --> B["Chọn vị trí, chip trục, chip All"]
    B --> C{"Ô đã có lốp"}
    C -->|"Có"| D["E-006 Ô xám, Save tắt"]
    D --> B
    C -->|"Không"| E{"Chọn Tire Model"}
    E -->|"Danh mục rỗng"| F["E-013 No options"]
    F -->|"Tạo Part category lốp"| E
    E -->|"Có mẫu"| G["Factory, Min, Life tự điền, khoá"]
    E -->|"Bỏ qua"| H["Nhập tay hoặc để trống"]
    G --> I["Lưu"]
    H --> I
    I --> J["Mỗi vị trí một dòng Installed, cùng mã lốp, không kiểm trùng"]
    J --> K["Không trừ kho, không vào chi phí"]
    K --> KetThuc["Kết thúc"]
```

Đường đảo ngược: tháo (Flow 5). Lắp nhầm vị trí có thể sửa bằng đảo (Flow 4), `Suy`.

## Flow 3: Chép thông số (`Chạy`)

```mermaid
flowchart TD
    A["Menu dòng lốp, Copy details to"] --> B["Tick trường cần chép"]
    B --> C{"Trường gai, áp suất"}
    C -->|"Có"| D["E-008 Không chép được"]
    D --> B
    C -->|"Không"| E["Chọn đích"]
    E --> F{"Đích trống"}
    F -->|"Có"| G["Tạo lốp mới, Installed, gai trống"]
    F -->|"Không"| H["Sửa đích, không có dòng lịch sử"]
    H --> I{"Chỉ tick mã lốp"}
    I -->|"Có"| J["E-009 Factory, Life của đích bị xoá trắng"]
    I -->|"Không"| K["Trường đã tick đổi"]
    G --> KetThuc["Kết thúc"]
    J --> KetThuc
    K --> KetThuc
```

Không có đường hoàn tác.

## Flow 4: Đảo lốp (`Chạy`)

```mermaid
flowchart TD
    A["Menu Rotate Tires"] --> B{"Rotation Pattern"}
    B -->|"Mooc"| C["E-014 No options"]
    B -->|"Chọn mẫu chuẩn"| D["Điền sẵn New Position, kể cả ô trống"]
    B -->|"Tự ghép"| E["Chọn New Position từng dòng"]
    C --> E
    D --> F{"Sơ đồ khép kín"}
    E --> F
    F -->|"Chưa"| G["E-003 Nút tắt"]
    G --> E
    F -->|"Rồi"| H{"Tick lưu mẫu"}
    H -->|"Trống tên"| I["E-004 Không đảo"]
    I --> H
    H -->|"Không tick, hoặc có tên"| J["Đảo: gai, áp suất, số km theo lốp"]
    J --> K["Màn kết quả, mỗi lốp một dòng Tire Rotation"]
    K -->|"Undo Rotation"| L["Về chỗ cũ, E-010 lịch sử sạch"]
    L --> E
    K -->|"Close"| M["Mất Undo"]
    M --> KetThuc["Kết thúc"]
```

Spare không tham gia. New Position chỉ có vị trí của xe đó, không đảo được sang xe khác. Lưu mẫu thật: `Không chạy`; mẫu nằm ở Settings › Tire Management Settings, cấp tài khoản (`Xem`, FR-fleetio-tires-031).

## Flow 5: Tháo, thay lốp (`Chạy`)

```mermaid
flowchart TD
    A["Remove, hoặc Remove All"] --> B["Chọn lốp, Select All"]
    B --> C{"Xác nhận tháo vĩnh viễn"}
    C -->|"Huỷ"| D["Giữ nguyên"]
    C -->|"Đồng ý"| E["Ô về nút cộng, dòng Removal"]
    E --> F["Mất khỏi Tire Readings, không hỏi lý do, không có đích"]
    F --> G{"Thay lốp mới"}
    G -->|"Có"| H["Lắp mới theo Flow 2, không nối lệnh, không trừ kho"]
    G -->|"Không"| I["Ô trống"]
    F --> J{"Xe hết lốp"}
    J -->|"Có"| K["Edit cấu hình trục mở lại"]
    J -->|"Không"| I
    D --> KetThuc["Kết thúc"]
    H --> KetThuc
    I --> KetThuc
    K --> KetThuc
```

Không có đường đảo ngược: muốn dùng lại lốp đã tháo phải gõ lại mã, km về 0 nếu không nhập tay, lịch sử không nối. Nhánh huỷ ở hộp xác nhận là `Suy`, không thử và không ghi câu chữ nút.

## Flow 6: Đọc trực tiếp (`Chạy`)

```mermaid
flowchart TD
    A["Sửa gai, áp suất trên dòng hoặc hộp Edit"] --> B["Rời ô, lưu ngay"]
    B --> C["Dòng đọc Manual, ngày là hôm nay"]
    C --> D{"So với Min của lốp"}
    D -->|"Gai từ Min trở xuống"| E["Low đỏ"]
    D -->|"Đến Min + 2"| F["Warning vàng"]
    D -->|"Cao hơn"| G["Normal"]
    E --> H["Không sự cố, không thông báo"]
    F --> H
    G --> H
    H --> KetThuc["Kết thúc"]
```

Áp suất không có mức theo lốp. Sửa nhầm thì sửa lại, số cũ còn ở lịch sử.

## Flow 7: Đọc qua phiếu kiểm (`Chạy`)

```mermaid
sequenceDiagram
    actor D as Lái xe
    participant F as Phiếu kiểm
    participant T as Lốp
    participant I as Sự cố
    D->>F: Chọn biểu mẫu, xe
    alt Xe chưa được gán biểu mẫu
        F-->>D: E-007 No inspection forms exist yet
    else Xe chưa khai trục
        D->>F: Save
        F-->>D: E-001 hộp More info needed
        D->>F: Chọn cấu hình, Done
        F->>T: Sinh lốp mọi vị trí
    else Xe thiếu lốp
        F-->>D: Install Missing Tires
        D->>F: Install Tires
        F->>T: Tạo lốp trống
    else Đủ
        F-->>D: Sinh ô Tread Depth, Pressure
    end
    D->>F: Nhập từng vị trí, không có Spare
    opt Có ô không đạt và thiếu nhận xét
        F-->>D: E-005 must contain a remark on failure
        D->>F: Nhập nhận xét, ảnh
    end
    D->>F: Nộp
    F->>T: Ghi đọc, Method Inspection
    alt Fail và biểu mẫu có workflow tạo sự cố
        F->>I: Tạo một sự cố, High, vị trí nằm trong chữ
        I-->>D: Issue trên phiếu
    else Pass, hoặc không có workflow
        F-->>D: Nộp xong
    end
```

Cùng số đọc có thể Pass ở phiếu nhưng Low ở lốp vì hai mức tối thiểu tách rời. Mô tả sự cố có thể thiếu lỗi (E-011). Fail lần 2 gộp vào sự cố cũ: `Không chạy`.

## Flow 8: Số km lốp theo đồng hồ (`Chạy`, quy tắc `Suy`)

```mermaid
flowchart TD
    A["Có số đồng hồ mới của chính xe chứa lốp"] --> B{"Có số trước ngày lắp"}
    B -->|"Có"| C["Số km lốp bằng số mới nhất trừ số mốc"]
    B -->|"Không"| D["E-012 Đứng ở gạch ngang, Edit và Rotate hiện 0"]
    D -->|"Nhập Tire Meter tay"| E["Có số km lốp"]
    C --> F["Tính lại khi đồng hồ đổi"]
    F --> KetThuc["Kết thúc"]
    E --> KetThuc
```

Ví dụ `Chạy`: lắp 03/11, có 1.000 ngày 25/10, 3.000 cùng ngày 03/11, nhập 3.500 thì số km lốp là 2.500. Đầu kéo tăng km thì mooc không đổi.

## Flow 9: Gắn lốp theo đầu kéo và theo mooc (`Chạy`)

```mermaid
flowchart TD
    A["Tạo xe"] --> B{"Loại"}
    B -->|"Đầu kéo"| C["Cấu hình xe: 6x4, 4x2 RWD Dually"]
    B -->|"Mooc"| D["Cấu hình mooc: Tandem, Tri-Axle"]
    C --> E["Lắp lốp đầu kéo, vai trò Steer, Drive"]
    D --> F["Lắp lốp mooc, vai trò Trailer, không có mẫu đảo"]
    E --> G["Số km lốp theo đồng hồ đầu kéo"]
    F --> H["Số km lốp theo đồng hồ mooc, nhập tay"]
    G --> I["Liên kết Linked Vehicles, chỉ là đường dẫn"]
    H --> I
    I -->|"Gỡ hoặc đổi mooc"| J["Lốp, đồng hồ không đổi, không có lịch sử ghép"]
    J --> I
    I -->|"Nối thêm xe thứ hai vào mooc"| N["Lưu được, không kiểm loại xe, không ngày hiệu lực"]
    N --> I
    I -->|"Archive xe, kể cả bị từ chối"| R["Mất liên kết, cấu hình trục còn, Edit trục khoá khi đã Archive"]
    R --> KetThuc["Kết thúc"]
    I --> KetThuc
```

## Flow 10: Đổi lốp giữa hai xe (cơ chế `Chạy`, giữa hai xe `Suy`)

```mermaid
flowchart TD
    A["Muốn chuyển lốp từ xe A sang xe B"] --> B["Không có thao tác chuyển"]
    B --> C["Remove ở xe A, dòng Removal"]
    C --> D["Lắp mới ở xe B, gõ lại mã, gai, áp suất, số km"]
    D --> E["Hai lịch sử không nối, không theo được một lốp"]
    E --> KetThuc["Kết thúc"]
```

## Flow 11: Mẫu đảo, đọc tự động, Import ở cấp tài khoản (`Xem`, không bấm)

```mermaid
flowchart TD
    A["Settings, Tire Management Settings"] --> B{"Việc cần làm"}
    B -->|"Mẫu đảo"| C["Tire Rotation Patterns, 8 mẫu Standard có khoá"]
    C --> D["Add Tire Rotation Pattern, không chạy"]
    B -->|"Áp suất tự động"| E["General, công tắc đang tắt, có khoá"]
    E --> F{"Xe 4x2, 4x4 có telematics"}
    F -->|"Có"| G["Theo câu chữ, cập nhật hằng ngày, chưa bật"]
    F -->|"Không, như 6x4"| H["Không áp dụng"]
    B -->|"Import lốp"| I["Không thấy lối vào ở Settings, Vehicle List, Tire Readings"]
    D --> KetThuc["Kết thúc"]
    G --> KetThuc
    H --> KetThuc
    I --> KetThuc
```

## Đề xuất Invlogis: đổi lốp và km theo tổ hợp

> Phần này **không phải Fleetio**, chưa chốt với Delta (DX-02, DX-03).

```mermaid
flowchart TD
    A["Lệnh vận tải gắn một tổ hợp"] --> B["Km đầu kéo trong thời gian Lệnh"]
    B --> C["Cộng vào đoạn lắp của lốp đầu kéo"]
    B --> D{"Tổ hợp có mooc"}
    D -->|"Có"| E["Cộng vào đoạn lắp của lốp mooc đó"]
    D -->|"Không"| F["Mooc đứng bãi, không tăng km"]
    C --> G["Lệnh sửa chữa chuyển lốp"]
    E --> G
    G --> H{"Đích"}
    H -->|"Xe khác hoặc vị trí khác"| I["Đóng đoạn cũ, mở đoạn mới, km cộng dồn"]
    H -->|"Tồn xưởng hoặc kho"| J["Đóng đoạn, cập nhật tồn"]
    H -->|"Rác thải"| K["Đóng đoạn, cập nhật rác thải, xử lý phân bổ"]
    F --> KetThuc["Kết thúc"]
    I --> KetThuc
    J --> KetThuc
    K --> KetThuc
```
