---
type: reverse-srs-flows
feature: cost-catalog
updated: 2026-10-20
---

# Khoản mục chi phí cấp 1–3 (`cost-catalog`) — Flows tái lập (reverse)

## Flow: Xem danh sách khoản mục chi phí (cấp 1, 2, 3)

> Nguồn: SRS Web tr.581, 614, 648 — hình lưu đồ UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3. Cả ba cấp cùng một lưu đồ, chỉ khác tên sub-tab.

### Sequence — Xem danh sách khoản mục chi phí

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    ND->>HT: Mở Dashboards
    HT-->>ND: Hiển thị màn hình Dashboards
    ND->>HT: Chọn tab Danh mục ở thanh điều hướng
    ND->>HT: Chọn sub-tab Chi phí cấp N
    HT-->>ND: Hiển thị màn hình Danh sách chi phí cấp N
```

### Activity — Xem danh sách khoản mục chi phí

```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hiển thị màn hình Dashboards"]
    B --> C["Người dùng chọn tab Danh mục"]
    C --> D["Người dùng chọn sub-tab Chi phí cấp N"]
    D --> E["Hiển thị Danh sách chi phí cấp N"]
    E --> F(["Kết thúc"])
```

## Flow: Xem thông tin khoản mục chi phí

> Nguồn: SRS Web tr.585, 618, 652 — hình lưu đồ UC03.10.02, UC03.11.02, UC03.12.02 Xem thông tin chi phí cấp 1, 2, 3. Cấp 2 và cấp 3 còn vào được từ tab cấp con trong chi tiết cấp cha.

### Sequence — Xem thông tin khoản mục chi phí

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    HT-->>ND: Hiển thị Danh sách chi phí cấp N
    ND->>HT: Chọn 1 bản ghi trong danh sách
    HT-->>ND: Hiển thị màn hình Thông tin chi phí cấp N
    opt Cấp 1 và cấp 2 có tab cấp con
        ND->>HT: Chọn tab Chi phí cấp N+1
        HT-->>ND: Danh sách khoản mục con đã phê duyệt
        ND->>HT: Chọn 1 khoản mục con
        HT-->>ND: Thông tin chi phí cấp N+1
    end
```

### Activity — Xem thông tin khoản mục chi phí

```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B{"Từ đâu"}
    B -->|Danh sách cùng cấp| C["Hiển thị Danh mục Danh sách chi phí cấp N"]
    B -->|Tab cấp con của cấp cha| D["Hiển thị Thông tin chi phí cấp N-1 và danh sách cấp N"]
    C --> E["Người dùng chọn 1 bản ghi"]
    D --> E
    E --> F["Hiển thị Thông tin chi phí cấp N"]
    F --> G(["Kết thúc"])
```

## Flow: Tạo đề xuất tạo mới khoản mục chi phí

> Nguồn: SRS Web tr.591–597, 625–631, 657–665 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3; hình lưu đồ tr.591, 625, 657. Nhánh dữ liệu không hợp lệ lấy từ mô tả chữ (lưu đồ chỉ vẽ nhánh hợp lệ).

### Sequence — Tạo đề xuất tạo mới khoản mục chi phí

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    participant QD as Người có quyền phê duyệt
    HT-->>ND: Hiển thị Danh sách chi phí cấp N
    ND->>HT: Bấm Tạo mới
    HT-->>ND: Hiển thị form Tạo mới chi phí cấp N (lưu đồ ghi popup)
    ND->>HT: Nhập thông tin và bấm Tạo mới
    HT->>HT: Kiểm tra validate
    alt Có trường không hợp lệ
        HT-->>ND: Lỗi in-line dưới trường, ví dụ Tên chi phí này đã bị trùng.
    else Hợp lệ
        HT-->>ND: Toast Đề xuất tạo mới thành công
        HT->>HT: Tạo bản ghi trạng thái Chờ phê duyệt
        HT->>QD: Thông báo đang chờ phê duyệt
        HT->>HT: Lưu Lịch sử hoạt động Đã tạo yêu cầu cấp mới
        HT-->>ND: Màn Thông tin chi phí cấp N với Huỷ đề xuất, Phê duyệt, Từ chối
    end
```

### Activity — Tạo đề xuất tạo mới khoản mục chi phí

```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hiển thị Danh sách chi phí cấp N"]
    B --> C["Bấm nút Tạo mới"]
    C --> D["Hiển thị form Tạo mới chi phí cấp N"]
    D --> E["Nhập thông tin và xác nhận"]
    E --> F{"Kiểm tra validate"}
    F -->|"Không hợp lệ"| G["Báo lỗi in-line dưới trường"]
    G --> D
    F -->|"Hợp lệ"| H["Toast và lưu bản ghi Chờ phê duyệt"]
    H --> I["Gửi thông báo cho người có quyền phê duyệt"]
    I --> J["Tạo bản ghi Lịch sử hoạt động"]
    J --> K["Chuyển sang màn Thông tin chi phí cấp N chế độ xem"]
    K --> L(["Kết thúc"])
    D --> M["Bấm Huỷ hoặc đóng"]
    M --> N{"Xác nhận huỷ tạo mới"}
    N -->|"Xác nhận"| O["Không tạo bản ghi và về Danh sách"]
    N -->|"Huỷ"| D
    O --> L
```

## Flow: Huỷ đề xuất tạo mới

> Nguồn: SRS Web tr.598–602, 632–636, 666–670 — UC03.10.04, UC03.11.04, UC03.12.04 Huỷ đề xuất cấp mới chi phí cấp 1, 2, 3; hình lưu đồ tr.598, 632, 666.

### Sequence — Huỷ đề xuất tạo mới

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    participant QD as Người có quyền phê duyệt
    HT-->>ND: Màn Thông tin hoặc Danh sách chi phí cấp N
    ND->>HT: Bấm Huỷ đề xuất
    HT-->>ND: Popup Huỷ đề xuất tạo mới?
    alt Huỷ bỏ
        ND->>HT: Bấm Huỷ bỏ
        HT-->>ND: Giữ Chờ phê duyệt và về màn Thông tin
    else Xác nhận
        ND->>HT: Bấm Xác nhận
        HT->>HT: Đổi trạng thái Chờ phê duyệt sang Đã huỷ
        HT-->>ND: Toast Huỷ đề xuất tạo chi phí cấp N thành công
        HT->>QD: Thông báo yêu cầu đã bị huỷ
        HT->>HT: Lưu Lịch sử hoạt động Đã huỷ yêu cầu cấp mới
        HT-->>ND: Màn Thông tin với Xoá yêu cầu và Tạo mới yêu cầu
    end
```

### Activity — Huỷ đề xuất tạo mới

```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B{"Đang ở màn nào"}
    B -->|Màn Thông tin chi phí cấp N| C["Bấm Huỷ đề xuất"]
    B -->|Danh sách chi phí cấp N| C
    C --> D["Popup Xác nhận huỷ"]
    D --> E{"Người dùng chọn"}
    E -->|"Huỷ bỏ"| F["Giữ trạng thái Chờ phê duyệt và về màn Thông tin"]
    E -->|"Xác nhận"| G["Toast và lưu trạng thái Đã huỷ"]
    G --> H["Gửi thông báo cho người có quyền phê duyệt"]
    H --> I["Tạo bản ghi Lịch sử hoạt động"]
    I --> J["Chuyển sang màn Thông tin chi phí cấp N chế độ xem"]
    J --> K(["Kết thúc"])
    F --> K
```

## Flow: Phê duyệt hoặc từ chối đề xuất tạo mới

> Nguồn: SRS Web tr.603–610, 637–644, 671–679 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3; hình lưu đồ tr.604, 638, 672. Bước sinh mã, thông báo và xử lý xung đột lấy từ mô tả chữ và ảnh popup lỗi (lưu đồ ảnh không vẽ).

### Sequence — Phê duyệt hoặc từ chối đề xuất tạo mới

```mermaid
sequenceDiagram
    actor ND as Người phê duyệt
    participant HT as Hệ thống PMX
    participant NT as Người đã tạo yêu cầu
    HT-->>ND: Màn Thông tin hoặc Danh sách chi phí cấp N
    alt Phê duyệt
        ND->>HT: Bấm Phê duyệt
        HT-->>ND: Popup Phê duyệt đề xuất tạo mới?
        ND->>HT: Bấm Phê duyệt
        alt Đề xuất đã bị người khác huỷ trước
            HT-->>ND: Popup Lỗi và nút Tải lại trang
        else Còn Chờ phê duyệt
            HT->>HT: Chờ phê duyệt sang Đã phê duyệt và sinh mã chi phí
            HT-->>ND: Toast Phê duyệt đề xuất tạo chi phí cấp N thành công
            HT->>NT: Thông báo đã được phê duyệt
            HT->>HT: Lưu Lịch sử hoạt động Đã phê duyệt yêu cầu cấp mới
        end
    else Từ chối
        ND->>HT: Bấm Từ chối
        HT-->>ND: Popup Từ chối đề xuất tạo mới? và ô lý do
        ND->>HT: Nhập lý do không bắt buộc và bấm Từ chối
        alt Đề xuất đã bị người khác huỷ trước
            HT-->>ND: Popup Lỗi và nút Tải lại trang
        else Còn Chờ phê duyệt
            HT->>HT: Chờ phê duyệt sang Đã từ chối
            HT-->>ND: Toast Từ chối đề xuất tạo chi phí cấp N thành công
            HT->>NT: Thông báo đã bị từ chối
            HT->>HT: Lưu Lịch sử hoạt động kèm lý do
        end
    end
    HT-->>ND: Màn Thông tin chi phí cấp N chế độ xem
```

### Activity — Phê duyệt hoặc từ chối đề xuất tạo mới

```mermaid
flowchart TD
    A(["Bắt đầu"]) --> C{"Chọn hành động"}
    C -->|Phê duyệt| D["Popup Xác nhận phê duyệt"]
    C -->|Từ chối| E["Popup Xác nhận từ chối với ô lý do"]
    D --> F{"Bản ghi còn Chờ phê duyệt"}
    E --> F
    F -->|"Đã bị huỷ trước"| G["Popup Lỗi và Tải lại trang"]
    F -->|"Còn Chờ phê duyệt"| H{"Hành động"}
    H -->|Phê duyệt| I["Toast, lưu Đã phê duyệt, sinh mã chi phí"]
    H -->|Từ chối| J["Toast, lưu Đã từ chối kèm lý do"]
    I --> K["Gửi thông báo cho người đã tạo"]
    J --> K
    K --> L["Tạo bản ghi Lịch sử hoạt động"]
    L --> M["Chuyển sang màn Thông tin chi phí cấp N chế độ xem"]
    M --> N(["Kết thúc"])
    G --> N
```

## Flow: Xoá yêu cầu và tạo lại yêu cầu từ bản đã huỷ hoặc đã từ chối

> Nguồn: SRS Web tr.589–590, 601–602, 607–608, 623–624, 635–636, 641–642, 655–656, 669–670, 675–676 — UC03.10.02, UC03.10.04, UC03.10.05 (và cấp 2, 3). Không có lưu đồ riêng; theo mô tả chữ và ảnh popup Xoá yêu cầu. Bước tạo lại cập nhật cùng bản ghi theo mô tả chữ.

### Sequence — Xoá yêu cầu và tạo lại yêu cầu

```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    HT-->>ND: Màn Thông tin chi phí cấp N trạng thái Đã huỷ hoặc Đã từ chối
    ND->>HT: Bấm biểu tượng ba chấm
    alt Chọn Xoá yêu cầu
        HT-->>ND: Popup Xoá yêu cầu?
        alt Xoá
            ND->>HT: Bấm Xoá
            HT->>HT: Xoá yêu cầu được chọn
            HT-->>ND: Toast Xoá yêu cầu thành công và về Danh sách
        else Huỷ
            ND->>HT: Bấm Huỷ
            HT-->>ND: Về màn Thông tin chi phí cấp N
        end
    else Chọn Tạo mới yêu cầu
        HT-->>ND: Màn Tạo mới yêu cầu với dữ liệu từ yêu cầu hiện tại
        ND->>HT: Chỉnh sửa và xác nhận
        Note over HT: Cập nhật cùng bản ghi và đưa về Chờ phê duyệt
        HT-->>ND: Màn Thông tin chi phí cấp N
    end
```

### Activity — Xoá yêu cầu và tạo lại yêu cầu

```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Màn Thông tin chi phí cấp N trạng thái Đã huỷ hoặc Đã từ chối"]
    B --> C["Bấm biểu tượng ba chấm"]
    C --> D{"Chọn hành động"}
    D -->|Xoá yêu cầu| E["Popup Xoá yêu cầu?"]
    E --> F{"Người dùng chọn"}
    F -->|Xoá| G["Xoá yêu cầu, toast và về Danh sách chi phí cấp N"]
    F -->|Huỷ| H["Về màn Thông tin chi phí cấp N"]
    D -->|Tạo mới yêu cầu| I["Hiển thị màn Tạo mới yêu cầu với dữ liệu hiện tại"]
    I --> J["Cập nhật bản ghi và đưa về Chờ phê duyệt"]
    G --> K(["Kết thúc"])
    H --> K
    J --> K
```
