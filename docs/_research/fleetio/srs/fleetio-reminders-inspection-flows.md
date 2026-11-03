---
type: research
feature: fleetio-reminders-inspection
updated: 2026-11-03
---

# Nhắc và kiểm tra — Flows

Mã lỗi đầy đủ có tiền tố `E-fleetio-reminders-inspection-`. Luồng đảo ngược ghi cạnh từng flow; "không có" nghĩa là đã tìm và không thấy.

## Flow 1: Tạo nhắc bảo dưỡng (`Chạy`)

```mermaid
flowchart TD
    A["Mở form, chọn xe và đầu việc"] --> B["Hiện lần gần nhất hoặc Never logged"]
    B --> C{"Có chu kỳ?"}
    C -->|"Không"| E8["E-008 Thiếu chu kỳ"]
    E8 -.->|"Nhập lại"| C
    C -->|"Có"| D{"Ngưỡng nhỏ hơn chu kỳ?"}
    D -->|"Không"| E9["E-009, E-010 Ngưỡng quá cao"]
    E9 -.->|"Giảm ngưỡng"| D
    D -->|"Có"| F{"Đặt tay mốc?"}
    F -->|"Có"| G["Mốc = hôm nay + chu kỳ, đồng hồ hiện tại + chu kỳ"]
    F -->|"Không, có lịch sử"| H["Mốc từ lần làm gần nhất"]
    F -->|"Không, chưa có lịch sử"| I["Km bội số từ 0, thời gian từ hôm nay"]
    G --> J["Lưu, tính trạng thái theo trục xấu nhất"]
    H --> J
    I --> J
    J --> K{"Mốc so với hiện tại"}
    K -->|"Còn xa"| L["Upcoming"]
    K -->|"Trong ngưỡng"| M["Due Soon"]
    K -->|"Đã qua"| N["Overdue ngay"]
    L --> End["Kết thúc"]
    M --> End["Kết thúc"]
    N --> End["Kết thúc"]
```

**Nhánh đảo ngược:** sửa chu kỳ tính lại ngay, không ghi lịch sử; xoá chưa bấm.

## Flow 2: Số đồng hồ đổi, nhắc đổi trạng thái (`Chạy`)

```mermaid
sequenceDiagram
    actor U as Người dùng
    participant N as Nguồn số km
    participant M as Sổ đồng hồ
    participant R as Nhắc
    participant T as Thông báo
    U->>N: Lưu lệnh, phiếu dầu, phiếu kiểm hoặc nhập tay
    N->>M: Ghi số km
    alt Trái lịch sử theo thời điểm
        M-->>U: E-013 must be less than ... or marked as void
    else Hợp lệ
        M->>R: Tính lại ngay, không chờ job
        alt Còn lớn hơn ngưỡng
            R->>R: Giữ Upcoming
        else Còn nhỏ hơn hoặc bằng ngưỡng
            R->>R: Chuyển Due Soon
            R->>T: Fleetio gửi lúc 7 giờ sáng (Xem)
        else Lớn hơn hoặc bằng mốc
            R->>R: Chuyển Overdue
            R->>T: Gửi, lặp lại mỗi tuần (Xem)
        end
    end
    opt Nhập sai số
        U->>M: Void số đồng hồ, không hỏi lý do
        M->>R: Tính lại, trạng thái lùi ngay
    end
```

**Nhánh lỗi:** lệch múi giờ thiết bị và tài khoản làm số đúng bị E-013 (`Chạy`).

## Flow 3: Tạm hoãn và huỷ hoãn (`Chạy`)

```mermaid
flowchart TD
    A["Nhắc Overdue, menu chọn Snooze"] --> B["Hộp ngày giờ, mặc định cộng 7 ngày"]
    B --> C{"Ngày đã qua?"}
    C -->|"Có"| D["Báo thành công, vẫn Overdue"]
    C -->|"Không"| E["Snoozed, Next Due xám"]
    E --> F{"Điều gì xảy ra trước"}
    F -->|"Đồng hồ tăng"| G["Số quá hạn đổi, vẫn Snoozed"]
    G --> F
    F -->|"Hết hạn"| H["Về trạng thái thường, dưới 2 phút"]
    F -->|"Remove Snooze"| I["Về ngay, không hỏi"]
    F -->|"Hoàn thành"| J["Xoá hoãn, tính kỳ mới, vẫn Late nếu quá"]
    D --> End["Kết thúc"]
    H --> End["Kết thúc"]
    I --> End["Kết thúc"]
    J --> End["Kết thúc"]
```

**Không có:** ô lý do, mức chọn sẵn, cảnh báo ngày đã qua. Hoãn từ Upcoming, Due Soon chưa bấm.

## Flow 4: Đóng nhắc bằng lệnh sửa chữa (`Chạy`)

```mermaid
sequenceDiagram
    actor Q as Quản lý
    participant R as Nhắc
    participant W as Lệnh sửa chữa
    participant S as Service Entry
    participant C as Tuân thủ
    Q->>R: Resolve, Add to Work Order
    R-->>Q: Hộp mọi nhắc của xe, tick thêm
    Q->>W: Lệnh mới hoặc có sẵn
    W-->>R: Dải added to Work Order, trạng thái KHÔNG đổi
    Q->>W: Đặt Completed
    alt Thiếu Started At
        W-->>Q: E-011
    else Thiếu đồng hồ theo cài đặt tài khoản
        W-->>Q: E-012
    else Đồng hồ trái lịch sử
        W-->>Q: E-013
    else Đủ
        W->>S: Sinh Service Entry, khoá Edit lệnh
        S->>R: Kỳ mới từ ngày và số của lần làm
        R->>C: Ghi On-Time hoặc Late, tính ngầm
    end
```

**Nhánh đảo ngược:** lệnh đã Completed khoá Edit; mở lại xem nhóm Sửa chữa. Draft Work Order xám, bấm không phản hồi.

## Flow 5: Đóng nhắc bằng phiếu dịch vụ (`Chạy`)

```mermaid
flowchart TD
    A{"Đi từ đâu"}
    A -->|"Resolve, Add to service history"| B["Hộp Log completed service"]
    A -->|"New Service Entry, gõ đầu việc"| C["Form hiện Last Completed, Next Due"]
    B --> D{"Cách nhập"}
    D -->|"Smart uploads, mặc định"| E["Quét hoá đơn, chưa chạy"]
    D -->|"Nhập tay"| F["Chọn phiếu mới hoặc có sẵn"]
    F --> G["Form Service Entry"]
    C --> G
    G --> H{"Hợp lệ?"}
    H -->|"Thiếu Completion Date"| E14["E-014"]
    H -->|"Đồng hồ trái lịch sử"| E13["E-013"]
    E14 -.->|"Nhập"| G
    E13 -.->|"Sửa số"| G
    H -->|"Đủ"| I["Đầu việc khớp là nhận, tính kỳ mới"]
    I --> J{"Trễ trên trục nào không"}
    J -->|"Có"| K["Late, có thể Due Soon ngay"]
    J -->|"Không"| L["On-Time"]
    E --> End["Kết thúc"]
    K --> End["Kết thúc"]
    L --> End["Kết thúc"]
```

## Flow 6: Áp và sửa bộ lịch (`Chạy`, phần nhân đôi là `Docs`)

```mermaid
flowchart TD
    A["Tạo bộ, chọn đồng hồ chính"] --> B["Thêm lịch, Set First Service"]
    B --> C["Add Vehicles, chỉ xe cùng đơn vị"]
    C --> D["Bảng Conflicting, Duplicate, New Interval"]
    D --> E["Lưu, xử lý ngầm khoảng 1 phút"]
    E --> F{"Đã có nhắc cùng đầu việc"}
    F -->|"Không"| G["Tạo nhắc mới"]
    F -->|"Nhắc thêm tay"| H["Thay lịch, giữ mã, không hỏi"]
    F -->|"Nhắc từ bộ khác"| I["Nhân đôi (Docs)"]
    G --> J["Trạng thái tính lại"]
    H --> J
    I --> J
    J --> K{"Sửa lịch trên bộ?"}
    K -->|"Có"| L["Xử lý ngầm, nhắc đổi trạng thái, không hỏi"]
    K -->|"Không"| M["Giữ"]
    L --> N{"Gỡ xe khỏi bộ?"}
    M --> N
    N -->|"Xác nhận"| O["Xoá nhắc từ bộ, chưa bấm"]
    N -->|"Không"| P["Tiếp tục theo bộ"]
    O --> End["Kết thúc"]
    P --> End["Kết thúc"]
```

**Nhánh đảo ngược:** không có hoàn tác khi áp bộ (`Docs`).

## Flow 7: Gia hạn giấy tờ (`Chạy`)

```mermaid
flowchart TD
    A["Tạo gia hạn, chọn xe hoặc liên hệ"] --> B{"Xe đã có loại này?"}
    B -->|"Có"| C["Dòng xám, không chọn được"]
    B -->|"Không"| D["Ngày đến hạn, ngưỡng, Watcher"]
    D --> E["Lưu, về danh sách"]
    E --> F{"So ngày"}
    F -->|"Trong ngưỡng"| G["Due Soon"]
    F -->|"Đã qua"| H["Overdue"]
    F -->|"Còn xa"| I["Chưa đến ngưỡng"]
    G --> J["Sửa tay Due Date sang kỳ mới"]
    H --> J
    J --> K["Kỳ cũ không lưu, không có chứng từ"]
    C --> End["Kết thúc"]
    I --> End["Kết thúc"]
    K --> End["Kết thúc"]
```

**Không có:** Resolve, History, tải giấy tờ mới.

## Flow 8: Dựng và gán biểu mẫu (`Chạy`)

```mermaid
flowchart TD
    A["Tạo biểu mẫu"] --> B{"Nguồn"}
    B -->|"Trống"| C["Thêm mục từ thanh phải"]
    B -->|"Mẫu hệ thống"| D["Sửa mục có sẵn"]
    B -->|"PDF hoặc ảnh, Beta"| E["AI chuyển thành mục (Xem)"]
    C --> F["Lưu, có workflow mặc định"]
    D --> F
    E --> F
    F --> G{"Phạm vi xe"}
    G -->|"Mọi xe"| H{"Đặt lịch"}
    G -->|"Theo thuộc tính"| H
    G -->|"Xe cụ thể"| H
    H -->|"Có"| I["Theo dõi đến hạn, quá hạn (Suy)"]
    H -->|"Không"| J["Làm khi cần, không quá hạn (Docs)"]
    I --> K["Xử lý ngầm hơn 1 phút, E-017 trong lúc chờ"]
    J --> K
    K --> L{"Sửa biểu mẫu sau khi có phiếu?"}
    L -->|"Có"| M["Phiếu cũ giữ nhãn cũ, Past Version"]
    L -->|"Không"| N["Dùng tiếp"]
    M --> End["Kết thúc"]
    N --> End["Kết thúc"]
```

## Flow 9: Làm và nộp phiếu (`Chạy`; vị trí `Chạy (vị trí giả lập)`)

```mermaid
sequenceDiagram
    actor L as Lái xe
    participant F as Biểu mẫu
    participant S as Phiếu
    participant G as Vị trí
    participant W as Workflow
    L->>F: Chọn biểu mẫu và xe
    alt Chưa gán xe
        F-->>L: E-017 danh sách rỗng
    else Có quyền vị trí
        G-->>F: Toạ độ lấy lúc khởi động app
    else Không có quyền
        F-->>L: E-007 cảnh báo, vẫn làm được
    end
    L->>S: Trả lời mục
    opt Mục lốp, xe chưa khai trục
        S-->>L: E-004 hộp More info needed
        L->>S: Chọn trục, Done, tự sinh lốp
    end
    opt Rời trang
        S-->>L: E-019 Leave site, phiếu mất
    end
    L->>S: Save Inspection
    alt Thiếu dữ liệu
        S-->>L: E-001, E-002, E-003, E-005, E-013, E-015, kèm E-006
    else Hợp lệ
        S->>G: Lưu một cặp toạ độ, sinh Location Entry
        S->>S: Gắn Job đang gán, ghi đồng hồ, đọc lốp
        S->>W: Chạy theo mục
        S-->>L: Inspection form submitted
    end
```

**Nhánh đảo ngược:** phiếu đã nộp không sửa, chỉ Delete (chưa bấm). **Không có:** nháp, phát hiện toạ độ giả, Location Exception trên web.

## Flow 10: Xử lý mục lỗi (`Chạy`; Create Issue, Reopen là `Xem`)

```mermaid
flowchart TD
    A["Mục Fail khi nộp"] --> B{"Workflow bật?"}
    B -->|"Không"| C["Needs Action"]
    C --> D{"Chọn"}
    D -->|"Acknowledge, ghi chú tuỳ chọn"| E["Acknowledged, cuối"]
    D -->|"Create Issue, chưa bấm"| F["Sự cố"]
    B -->|"Có"| G{"Sự cố của mục còn mở?"}
    G -->|"Có"| H["Gộp, thêm mốc thời gian, thêm dòng"]
    G -->|"Không, đã Resolved"| I["Sự cố MỚI, không mở lại"]
    G -->|"Chưa từng lỗi"| F
    H --> F
    I --> F
    F --> J{"Giải quyết"}
    J -->|"Thêm vào lệnh"| K["Status WO, lệnh xử lý"]
    J -->|"Resolve with Note"| L{"Có Note?"}
    L -->|"Không"| E18["E-018"]
    E18 -.->|"Nhập"| L
    L -->|"Có"| M["Resolved in Issue"]
    K --> M
    M --> N["Reopen, chưa bấm"]
    E --> End["Kết thúc"]
    N --> End["Kết thúc"]
```

**Không có:** đạt lại tự đóng sự cố; câu hỏi xác nhận lại trên web; đường quay lại từ Acknowledged.
