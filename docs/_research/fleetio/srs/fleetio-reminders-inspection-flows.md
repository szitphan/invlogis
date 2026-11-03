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

**Nhánh đảo ngược:** sửa chu kỳ tính lại ngay, không hiện ở tab History nhưng có ở Record History; đặt tay hạn cũ không bị chặn, Overdue ngay; xoá chưa bấm.

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
    A["Nhắc Overdue hoặc Upcoming, menu chọn Snooze"] --> B["Hộp ngày giờ, mặc định cộng 7 ngày"]
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

**Không có:** ô lý do, mức chọn sẵn, cảnh báo ngày đã qua. Hoãn từ Due Soon chưa bấm trực tiếp. Mỗi lần hoãn, bỏ hoãn ghi Record History.

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

**Nhánh đảo ngược:** lệnh đã Completed khoá Edit; mở lại xem nhóm Sửa chữa. Draft Work Order xem Flow 11.

## Flow 5: Đóng nhắc bằng phiếu dịch vụ (`Chạy`)

```mermaid
flowchart TD
    A{"Đi từ đâu"}
    A -->|"Resolve, Add to service history"| B["Hộp Log completed service"]
    A -->|"New Service Entry, gõ đầu việc"| C["Form hiện Last Completed, Next Due"]
    B --> D{"Cách nhập"}
    D -->|"Smart uploads, mặc định"| E["Đọc hoá đơn dưới 30 giây, Review, gộp dòng thành đầu việc hệ thống"]
    E --> E0{"Có đầu việc của nhắc?"}
    E0 -->|"Có, tự thêm tay"| G
    E0 -->|"Không"| E00["Lưu phiếu, nhắc KHÔNG đóng"]
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
    E00 --> End["Kết thúc"]
    K --> End["Kết thúc"]
    L --> End["Kết thúc"]
```

**Nhánh đảo ngược:** Discard bỏ kết quả đọc. "Add to Service Entry" chỉ đổ vào form, phải Save lần nữa. Xem thêm khối Assessment sau lưu: FR-049.

## Flow 6: Áp và sửa bộ lịch (`Chạy`, phần nhân đôi là `Docs`)

```mermaid
flowchart TD
    A0{"Tạo bộ từ đâu"}
    A0 -->|"Mẫu hệ thống"| A1["Hiện số nhắc sẽ tạo, đồng hồ Miles cố định"]
    A0 -->|"Trống"| A["Tạo bộ, chọn đồng hồ chính, có thể bật đồng hồ phụ"]
    A1 --> B
    A --> B["Thêm lịch trên Time, Primary, Secondary, Set First Service"]
    B --> C["Add Vehicles, chỉ xe cùng đơn vị"]
    C --> C1{"Điều kiện theo thuộc tính"}
    C1 -->|"Current Operator"| E25["E-025, lọc được, không lưu thành Rule"]
    E25 -.->|"Đổi thuộc tính"| C1
    C1 -->|"Không khớp xe"| E26["E-026, nút lưu khoá"]
    E26 -.->|"Đổi điều kiện"| C1
    C1 -->|"Khớp xe"| D["Bảng Conflicting, Duplicate, New Interval"]
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

**Nhánh đảo ngược:** không có hoàn tác khi áp bộ (`Docs`). Gỡ xe chỉ có Delete, chưa bấm (OQ-12). Ô Rule khoá khi còn Sample Data (E-029) nên xe mới tự vào chưa chạy (OQ-21); lần gán chỉ là gán một lần theo kết quả lọc. Sau khi gán, đầu việc của bộ xám ở form nhắc lẻ của xe.

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
    G --> J["Sửa tay Due Date sang kỳ mới, Contact hoặc Vehicle và Type khoá"]
    H --> J
    J --> K["Status Upcoming, Record History ghi đổi hạn, không có kỳ, không có chứng từ"]
    C --> End["Kết thúc"]
    I --> End["Kết thúc"]
    K --> End["Kết thúc"]
```

**Không có:** Resolve, tab History, tải giấy tờ mới. **Nhánh đảo ngược:** sửa ngày lại lần nữa; lịch sử đổi xem ở Record History.

## Flow 8: Dựng và gán biểu mẫu (`Chạy`)

```mermaid
flowchart TD
    A["Tạo biểu mẫu"] --> B{"Nguồn"}
    B -->|"Trống"| C["Thêm mục từ thanh phải"]
    B -->|"Mẫu hệ thống"| D["Sửa mục có sẵn"]
    B -->|"PDF hoặc ảnh, Beta"| E["Hộp Processing khoá form"]
    E --> E1{"Kết quả"}
    E1 -->|"Khoảng 4 phút chưa xong"| E27["E-027 Taking longer than usual"]
    E27 -.->|"Restart Processing"| E
    E27 -->|"Đóng, xác nhận Discard"| A
    E1 -->|"Dưới 30 giây, Review, số, ô chọn, đồng hồ, ảnh thành Free Text"| D
    C --> F0{"Nhãn hợp lệ?"}
    F0 -->|"Mục kho thiếu nhãn"| E23["E-023"]
    E23 -.->|"Nhập nhãn"| C
    F0 -->|"Có"| F["Lưu, có workflow mặc định"]
    D --> F
    F --> G{"Phạm vi xe"}
    G -->|"Mọi xe"| H{"Đặt lịch"}
    G -->|"Theo thuộc tính"| H
    G -->|"Xe cụ thể"| H
    H -->|"Có"| I["Upcoming rồi Due Soon (Chạy), quá hạn (Suy)"]
    H -->|"Không"| J["Schedule Off, không vào Inspection Schedules, làm khi cần"]
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
    L->>F: Start Inspection, chọn biểu mẫu
    F-->>L: Chỉ có ô Vehicle, Save Inspection khoá
    L->>F: Chọn xe
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
        S-->>L: E-001, E-002, E-003, E-005, E-013, E-015, E-020, E-022, kèm E-006
    else Hợp lệ
        S->>G: Lưu một cặp toạ độ, sinh Location Entry
        S->>S: Gắn Job đang gán, ghi đồng hồ, đọc lốp
        S->>W: Chạy theo mục
        S-->>L: Inspection form submitted
    end
```

**Nhánh đảo ngược:** phiếu đã nộp không sửa, chỉ Delete (chưa bấm). **Không có:** nháp, phát hiện toạ độ giả, Location Exception trên web. Ảnh trên phiếu xem Flow 13, workflow khi nộp xem Flow 14, vị trí xem Flow 15.

## Flow 10: Xử lý mục lỗi (`Chạy`)

```mermaid
flowchart TD
    A["Mục Fail khi nộp"] --> B{"Workflow bật?"}
    B -->|"Không"| C["Needs Action"]
    C --> D{"Chọn"}
    D -->|"Acknowledge, ghi chú tuỳ chọn"| E["Acknowledged, cuối"]
    D -->|"Create Issue, một cú bấm"| F["Sự cố"]
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
    M --> N{"Reopen?"}
    N -->|"Có, không hỏi lý do"| O["Sự cố Open, Resolution Details biến mất, Timeline không thêm dòng"]
    O -->|"Dòng lỗi về Open Issue"| F
    N -->|"Không"| End["Kết thúc"]
    E --> End["Kết thúc"]
```

**Không có:** đạt lại tự đóng sự cố; câu hỏi xác nhận lại trên web; đường quay lại từ Acknowledged; lý do khi Reopen. Reopen có vào Record History của sự cố không: chưa mở (OQ-18).

## Flow 11: Bản nháp lệnh bằng AI (`Chạy` đến Discard; Add to là `Xem`)

```mermaid
sequenceDiagram
    actor Q as Quản lý
    participant R as Nhắc
    participant A as Xử lý AI
    participant D as Bản nháp
    participant W as Lệnh sửa chữa
    Q->>R: Resolve, Draft Work Order
    alt Nhắc Upcoming
        R-->>Q: E-030 xám, icon khoá, khoá theo trạng thái
    else Nhắc Due Soon hoặc Overdue
        R->>A: Gom hồ sơ toàn xe
        A-->>Q: Toast Drafting service, chạy nền
        A->>D: Xong dưới 2 phút
        D-->>Q: Dải Work Order drafted trên nhắc của cùng xe
        Q->>D: Review draft
        D-->>Q: Nhóm Resolves và Due for maintenance, tick sẵn hết, Est. Subtotal
        alt Discard
            Q->>D: Discard, không sinh lệnh
        else Add to, chưa bấm
            Q->>W: Lệnh đang mở hoặc lệnh mới
            W-->>Q: Tự điền Repair Priority Class, Issue Date, WO Status
        end
    end
```

**Nhánh đảo ngược:** Discard là bỏ hết; bỏ tick từng dòng có "Clear all" trên hộp. Thêm việc Upcoming vào lệnh rồi hoàn thành sẽ mất phần còn lại của chu kỳ (`Suy`).

## Flow 12: Ghi tuân thủ từng lần (`Chạy`)

```mermaid
flowchart TD
    A["Service Entry hoặc lệnh Completed có đúng đầu việc"] --> B{"Trễ từ 10% chu kỳ trở lên trên trục nào?"}
    B -->|"Không, sớm hoặc đúng"| C["On-Time, chữ ahead"]
    B -->|"Trễ dưới 10%, 9 ngày trên 92, 99 km trên 1.000"| D["On-Time, chữ behind vẫn đỏ"]
    B -->|"Từ 10%, 10 ngày trên 92, 100 km trên 1.000"| E["Late"]
    C --> F["Thêm dòng Due, Completed, Compliance"]
    D --> F
    E --> F
    F --> G["Thẻ nhắc: số lần đúng hạn trên số lần làm"]
    G --> H["Trung bình danh sách khớp theo lần, một điểm đo"]
    H --> I["Kỳ sau tính từ lần làm, kể cả ghi lùi ngày"]
    I --> End["Kết thúc"]
```

**Nhánh đảo ngược:** Void số đồng hồ làm trạng thái lùi; xoá Service Entry chưa thử.

## Flow 13: Ảnh trên phiếu (`Chạy`; chụp webcam thật chưa chạy)

```mermaid
flowchart TD
    S{"Loại ảnh trên phiếu"}
    S -->|"Mục Photo"| A["Bấm Pick File"]
    S -->|"Ảnh xác minh đồng hồ"| M["Dòng Meter Entry Photo Verification"]
    A --> B{"Prevent Use of Stored Photos"}
    B -->|"Bật"| C{"Có camera?"}
    C -->|"Không"| E21["E-021 Webcam Disabled"]
    E21 --> X["Mục bắt buộc: không nộp được phiếu"]
    C -->|"Có, chưa chạy"| D["Chụp"]
    B -->|"Tắt"| F["Pick File, Or drop file here"]
    F --> G{"Ảnh đã tải xong?"}
    G -->|"Chưa, bấm nộp"| E22["E-022 is required"]
    E22 -.->|"Chờ File uploaded, bấm lại"| G
    G -->|"Rồi"| H["Mục Photo đạt"]
    D --> H
    M --> N["Luôn chỉ webcam, không theo cờ trên"]
    N --> O{"Có ảnh?"}
    O -->|"Không, kể cả tick Void"| E20["E-020 must attach an odometer image"]
    E20 -.->|"Admin tắt Require Photo Verification"| P["Dòng ảnh biến mất"]
    O -->|"Có, chưa chạy"| Q["Mục đồng hồ đạt"]
    P --> Q
    H --> End["Kết thúc"]
    Q --> End["Kết thúc"]
    X --> End["Kết thúc"]
```

**Nhánh đảo ngược:** đổi cờ trên biểu mẫu áp ngay cho lần làm phiếu sau; không có đường bỏ qua cho từng phiếu.

## Flow 14: Workflow khi nộp phiếu (`Chạy` cho form submitted, trigger đạt, lỗi, mục lỗi tạo sự cố)

```mermaid
flowchart TD
    A["Nộp phiếu"] --> B{"Workflow bật trên biểu mẫu"}
    B -->|"If an item passes, đổi trạng thái"| P1["Xe sang Inactive ngay chỉ vì mục đạt, không hỏi"]
    B -->|"If an item fails từng mục, đổi trạng thái"| P2["Xe sang Out of Service"]
    P1 --> F
    P2 --> E
    B -->|"If form is submitted, đổi trạng thái"| C["Xe sang In Shop ngay, không hỏi, kể cả có mục Fail"]
    B -->|"ANY Failed tạo sự cố"| D{"Có mục lỗi?"}
    D -->|"Có"| E["Mỗi mục lỗi sinh một sự cố, hoặc gắn lại sự cố đang mở"]
    D -->|"Không"| F["Lưu phiếu"]
    B -->|"Không có workflow xử lý lỗi"| G{"Có mục lỗi?"}
    G -->|"Có"| H["Fail kèm Acknowledge, Create Issue"]
    G -->|"Không"| F
    C --> I{"Có mục lỗi?"}
    I -->|"Có"| H
    I -->|"Không"| F
    C --> J["Đổi lại tay bằng Edit Vehicle"]
    E --> End["Kết thúc"]
    F --> End["Kết thúc"]
    H --> End["Kết thúc"]
    J --> End["Kết thúc"]
```

**Nhánh đảo ngược:** workflow không tự đổi trạng thái xe về; phải sửa tay, bằng Edit Vehicle hoặc ô trạng thái đầu trang (`Chạy`). Chưa chạy Send an email, Assign user (OQ-15). Không có action tạo lệnh. Trạng thái xe không chặn làm phiếu.

## Flow 15: Vị trí và Location Exception (`Chạy (vị trí giả lập)` trên web; `Chạy (Fleetio Go)` một ca)

```mermaid
flowchart TD
    A{"Nộp từ đâu"}
    A -->|"Web"| B["Một cặp toạ độ cấp phiếu, lấy lúc khởi động app"]
    A -->|"Fleetio Go"| C["Toạ độ riêng từng mục"]
    B --> D["Mục không có toạ độ, không so giữa các phiếu"]
    D --> E["location_exception false, kể cả lệch khoảng 1.100 km giữa các phiếu"]
    C --> F{"So với ngưỡng (Docs)"}
    F -->|"Lệch tối đa 37 m, ca đã chạy"| G["are_items_too_close false, số mục quá xa 0, location_exception false"]
    F -->|"Vượt ngưỡng, chưa có ca dương"| H["Gắn Location Exception (Docs)"]
    E --> End["Kết thúc"]
    G --> End["Kết thúc"]
    H --> End["Kết thúc"]
```

**Không có:** phát hiện toạ độ giả trên web. Tắt định vị trên app chưa thử (OQ-7).

## Flow 16: Giao dịch vụ thuê ngoài (`Chạy` đến Confirm)

```mermaid
sequenceDiagram
    actor Q as Quản lý
    participant R as Nhắc
    participant A as Hộp Assign outsourced service
    participant N as Thông báo
    Q->>R: Resolve, Find a shop
    R-->>A: Service Details, có nhắc đang mở, Assign all
    Q->>A: Chọn Assign to
    alt Liên hệ không có đăng nhập
        A-->>Q: E-031 No results
    else Người dùng
        A-->>Q: Notification Methods, Email, Text Message tick sẵn
    end
    opt Bấm ASAP
        A-->>Q: Continue khoá, không gọi máy chủ (OQ-26)
    end
    Q->>A: Continue
    A-->>Q: Suggest Shop tích xanh, không hiện cửa hàng, sang Confirm
    Q->>A: Assign, chưa bấm
    A->>N: Gửi email, SMS thật (Suy)
```

**Nhánh đảo ngược:** Back ở Confirm, hoặc đóng hộp, không sinh gì (`Chạy`).

## Flow 17: Trừ kho từ phiếu (`Chạy`)

```mermaid
flowchart TD
    A["Mục Inventory Adjustment, chọn Part Location"] --> B["Ô Parts, chỉ phụ tùng ở kho đó kèm tồn"]
    A --> C{"Bỏ trống?"}
    C -->|"Có"| D["Phiếu ghi No parts used"]
    C -->|"Không"| B
    B --> E["Số lượng, mặc định 1"]
    E --> F["Nộp phiếu"]
    F --> G["Trừ ngay, không duyệt, Reason trống"]
    G --> H["Inventory Activity ghi số phiếu, tồn trước, tồn sau"]
    H --> I["Phiếu hiện kho và số dòng, không phải số lượng"]
    D --> End["Kết thúc"]
    I --> End["Kết thúc"]
```

**Nhánh đảo ngược:** phiếu không sửa được; hoàn kho qua Adjust Inventory tay là `Suy`, chưa thử.

## Flow 18: Bật và đọc dự báo (`Chạy`; usage tự tính thật, đồng hồ phụ, thông báo chưa đo)

```mermaid
flowchart TD
    A["Bấm Enable Forecasting trên danh sách"] --> B["Chỉ sang Service Reminder Settings"]
    B --> C["Tích Forecasting, Save Settings, không hỏi"]
    C --> D{"Số km ngày của xe"}
    D -->|"Bằng 0, E-032"| E["Forecast not available, nhắc có thời gian về ngày lịch, nhắc chỉ km giữ số"]
    D -->|"Lớn hơn 0"| F["Số còn lại chia số km ngày ra ngày dự báo"]
    F --> G{"Ngày dự báo trong ngưỡng thời gian?"}
    G -->|"Có, 14 ngày"| H["Due Soon, kể cả còn trên ngưỡng km"]
    G -->|"Không, 15,2 ngày"| I["Upcoming"]
    H --> J["Popover Next Due, Meter Forecast bày phép tính"]
    I --> J
    E --> K["Group Week, Month: nhắc không dự báo vào This Week"]
    J --> K
    K --> L{"Tắt Forecasting?"}
    L -->|"Có"| M["Về nguyên trạng ngay, menu Group còn None, Vehicle"]
    L -->|"Không"| End["Kết thúc"]
    M --> End["Kết thúc"]
```

**Nhánh đảo ngược:** tắt ô Forecasting; xe tick lại tự tính thì đọc lại mới về số tự tính. **Chưa giải thích:** OQ-28 đến OQ-31.
