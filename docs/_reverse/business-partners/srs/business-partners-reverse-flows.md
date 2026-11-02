---
type: reverse-srs-flows
feature: business-partners
updated: 2026-10-20
---

# Đối tác: nhà cung cấp, khách hàng, xe của khách (`business-partners`) — Flows tái lập (reverse)

## Flow: Xem danh sách danh mục đối tác

> Nguồn: SRS Web tr.461 — hình lưu đồ UC03.07.01 Xem danh mục nhà cung cấp HHDV; SRS Web tr.505 — hình lưu đồ UC03.08.01 Xem danh mục khách hàng DK05. Dùng chung cho Nhà cung cấp HHDV và Khách hàng DK05; Xe có thêm đường vào (xem flow riêng). Các thao tác tìm, nhóm, lọc, Export, Import, Tuỳ chỉnh, phân trang (🟡) chỉ có trong bảng mô tả màn hình, không có trong lưu đồ.

### Sequence — Xem danh sách danh mục đối tác
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    ND->>HT: Mở Dashboards
    HT-->>ND: Hiển thị màn hình Dashboards
    ND->>HT: Chọn tab Danh mục ở Navigation bar
    ND->>HT: Chọn sub-tab danh mục
    HT-->>ND: Hiển thị màn hình Danh sách của danh mục
    ND->>HT: Tìm kiếm, nhóm, lọc, phân trang (🟡)
    HT-->>ND: Cập nhật bảng (🟡)
```

### Activity — Xem danh sách danh mục đối tác
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hệ thống hiển thị Dashboards"]
    B --> C["Người dùng chọn tab Danh mục ở Navigation bar"]
    C --> D["Người dùng chọn sub-tab Nhà cung cấp HHDV hoặc Khách hàng DK05"]
    D --> E["Hệ thống hiển thị Danh sách danh mục"]
    E --> F["Tìm kiếm, nhóm, lọc, phân trang (🟡)"]
    F --> G(["Kết thúc"])
```

## Flow: Xem danh sách xe của khách hàng

> Nguồn: SRS Web tr.545 — hình lưu đồ UC03.09.01 Xem danh mục xe của khách hàng; SRS Web tr.549 — hình lưu đồ UC03.09.02 Xem thông tin xe của khách hàng. Lưu đồ có một cổng "?" chia hai đường vào, không ghi điều kiện của cổng; nhãn điều kiện dưới đây suy từ phần "Đường dẫn" của bảng thông tin chung (🔵).

### Sequence — Xem danh sách xe của khách hàng
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    alt Từ Danh mục (🔵)
        HT-->>ND: Hiển thị màn hình Dashboards
        ND->>HT: Chọn tab Danh mục
        ND->>HT: Chọn sub-tab Xe khách hàng
    else Từ Thông tin khách hàng DK05 (🔵)
        HT-->>ND: Hiển thị màn hình Thông tin khách hàng DK05
        ND->>HT: Chọn tab Xe của khách hàng (🔵)
    end
    HT-->>ND: Hiển thị màn hình Danh sách xe khách hàng
```

### Activity — Xem danh sách xe của khách hàng
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> Q{"Đường vào (🔵)"}
    Q -->|"Từ Danh mục"| B["Hệ thống hiển thị Dashboards"]
    B --> C["Người dùng chọn tab Danh mục ở Navigation bar"]
    C --> D["Người dùng chọn sub-tab Xe khách hàng"]
    Q -->|"Từ Thông tin khách hàng DK05"| E["Hệ thống hiển thị Thông tin khách hàng DK05"]
    E --> D
    D --> F["Hệ thống hiển thị Danh sách xe khách hàng"]
    F --> G(["Kết thúc"])
```

## Flow: Xem chi tiết bản ghi danh mục

> Nguồn: SRS Web tr.467 — hình lưu đồ UC03.07.02 Xem thông tin nhà cung cấp HHDV; SRS Web tr.510 — hình lưu đồ UC03.08.02 Xem thông tin khách hàng DK05; SRS Web tr.549 — hình lưu đồ UC03.09.02 Xem thông tin xe của khách hàng. Dùng chung ba danh mục; Xe có cổng "?" hai đường vào (SRS Web tr.549 — hình lưu đồ UC03.09.02). Các nút hành động trên màn chi tiết (🟡 theo mô tả bảng) chỉ có trong bảng, không có trong lưu đồ.

### Sequence — Xem chi tiết bản ghi danh mục
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    alt Danh sách từ Danh mục (cả ba danh mục)
        HT-->>ND: Hiển thị màn hình Danh sách
    else Xe: danh sách từ Thông tin khách hàng DK05
        HT-->>ND: Hiển thị Danh sách xe khách hàng trong Thông tin khách hàng DK05
    end
    ND->>HT: Chọn 1 bản ghi trong danh sách
    HT-->>ND: Hiển thị màn hình Thông tin (trạng thái và hành động theo quyền)
    ND->>HT: Nhấn Lịch sử hoạt động (🟡)
    HT-->>ND: Hiển thị popup Lịch sử hoạt động (🟡)
```

### Activity — Xem chi tiết bản ghi danh mục
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> Q0{"Đường vào danh sách (Xe có hai đường)"}
    Q0 -->|"Từ Danh mục"| B["Hệ thống hiển thị màn hình Danh sách"]
    Q0 -->|"Xe: từ Thông tin khách hàng DK05"| B2["Hệ thống hiển thị Danh sách xe khách hàng của khách hàng"]
    B2 --> C
    B --> C["Người dùng chọn 1 bản ghi trong danh sách"]
    C --> D["Hệ thống hiển thị màn hình Thông tin"]
    D --> E{"Trạng thái bản ghi (🟡)"}
    E -->|"Chờ phê duyệt"| F["Hiển thị nút Huỷ đề xuất, Phê duyệt, Từ chối theo quyền (🟡)"]
    E -->|"Đã huỷ hoặc Đã từ chối"| G["Hiển thị menu ba chấm: Xoá yêu cầu, Tạo mới yêu cầu (🟡)"]
    E -->|"Đã phê duyệt"| H["Không có hành động thêm (🟡)"]
    F --> I(["Kết thúc"])
    G --> I
    H --> I
```

## Flow: Tạo đề xuất tạo mới

> Nguồn: SRS Web tr.474 — hình lưu đồ UC03.07.03 Tạo đề xuất tạo mới nhà cung cấp HHDV; SRS Web tr.517 — hình lưu đồ UC03.08.03 Tạo đề xuất tạo mới khách hàng DK05; SRS Web tr.554 — hình lưu đồ UC03.09.03 Tạo đề xuất tạo mới xe của khách hàng. Lưu đồ chỉ có nhánh hợp lệ; nhánh không hợp lệ và nhánh Huỷ lấy từ bảng mô tả màn hình (🟡 cho nhãn nhánh suy ra). Popup xác nhận Huỷ tạo mới: SRS Web tr.485 — hình mockup UC03.07.03.

### Sequence — Tạo đề xuất tạo mới
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    participant NG as Người có quyền phê duyệt
    HT-->>ND: Hiển thị màn hình Danh sách
    ND->>HT: Nhấn nút Tạo mới
    HT-->>ND: Hiển thị form Tạo mới
    ND->>HT: Nhập các thông tin và nhấn Tạo mới
    HT->>HT: Kiểm tra validate
    alt Hợp lệ
        HT-->>ND: Toast "Đề xuất tạo mới thành công"
        HT->>HT: Tạo bản ghi trạng thái Chờ phê duyệt
        HT->>NG: Gửi thông báo đang chờ phê duyệt
        HT->>HT: Tạo dòng Lịch sử hoạt động "Đã tạo yêu cầu cấp mới"
        HT-->>ND: Hiển thị màn hình Thông tin (view mode)
    else Không hợp lệ
        HT-->>ND: Thông báo lỗi in-line dưới trường không hợp lệ
    end
    opt Nhấn Huỷ hoặc icon X (🟡)
        ND->>HT: Nhấn Huỷ
        HT-->>ND: Popup "Huỷ tạo mới?"
        alt Xác nhận
            HT-->>ND: Về màn hình Danh sách, không tạo bản ghi
        else Huỷ
            HT-->>ND: Về form Tạo mới với dữ liệu đã nhập
        end
    end
```

### Activity — Tạo đề xuất tạo mới
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hệ thống hiển thị Danh sách"]
    B --> C["Người dùng nhấn nút Tạo mới"]
    C --> D["Hệ thống hiển thị form Tạo mới"]
    D --> E["Người dùng nhập thông tin và nhấn Tạo mới"]
    E --> F{"Kiểm tra validate"}
    F -->|"Hợp lệ"| G["Báo toast Đề xuất tạo mới thành công và lưu bản ghi Chờ phê duyệt"]
    G --> H["Gửi thông báo tới người có quyền phê duyệt"]
    H --> I["Tạo bản ghi Lịch sử hoạt động mới"]
    I --> J["Chuyển sang màn hình Thông tin (view mode)"]
    J --> K(["Kết thúc"])
    F -->|"Không hợp lệ (🟡)"| L["Hiển thị lỗi in-line dưới trường không hợp lệ"]
    L --> D
    D --> M["Người dùng nhấn Huỷ hoặc icon X (🟡)"]
    M --> N["Hệ thống hiển thị popup Huỷ tạo mới"]
    N -->|"Xác nhận"| O["Không tạo bản ghi và về Danh sách"]
    O --> K
    N -->|"Huỷ"| D
```

## Flow: Huỷ đề xuất tạo mới

> Nguồn: SRS Web tr.489 — hình lưu đồ UC03.07.04 Huỷ đề xuất cấp mới nhà cung cấp HHDV; SRS Web tr.528 — hình lưu đồ UC03.08.04 Huỷ đề xuất cấp mới khách hàng DK05; SRS Web tr.565 — hình lưu đồ UC03.09.04 Huỷ đề xuất cấp mới xe của khách hàng. Cổng "?" đầu lưu đồ chia hai đường vào (màn Thông tin hoặc màn Danh sách). Nhánh Huỷ bỏ lấy từ bảng mô tả (🟡).

### Sequence — Huỷ đề xuất tạo mới
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    participant NG as Người có quyền phê duyệt
    alt Từ màn hình Thông tin
        HT-->>ND: Hiển thị màn hình Thông tin
    else Từ màn hình Danh sách
        HT-->>ND: Hiển thị màn hình Danh sách
    end
    ND->>HT: Nhấn Huỷ đề xuất
    HT-->>ND: Popup "Huỷ đề xuất tạo mới?"
    alt Xác nhận
        ND->>HT: Nhấn Xác nhận
        HT->>HT: Đổi trạng thái Chờ phê duyệt sang Đã huỷ
        HT-->>ND: Toast huỷ thành công
        HT->>NG: Gửi thông báo đã bị huỷ
        HT->>HT: Tạo dòng Lịch sử hoạt động "Đã huỷ yêu cầu cấp mới"
        HT-->>ND: Hiển thị màn hình Thông tin (Xoá yêu cầu, Tạo mới yêu cầu)
    else Huỷ bỏ (🟡)
        ND->>HT: Nhấn Huỷ bỏ
        HT-->>ND: Đóng popup, trạng thái giữ Chờ phê duyệt
    end
```

### Activity — Huỷ đề xuất tạo mới
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> Q{"Đang ở màn hình nào"}
    Q -->|"Thông tin"| B["Hệ thống hiển thị Thông tin"]
    Q -->|"Danh sách"| C["Hệ thống hiển thị Danh sách"]
    B --> D["Người dùng nhấn Huỷ đề xuất"]
    C --> D
    D --> E["Hệ thống hiển thị popup Xác nhận huỷ"]
    E -->|"Xác nhận"| F["Báo toast và lưu trạng thái mới Đã huỷ"]
    F --> G["Gửi thông báo tới người có quyền phê duyệt"]
    G --> H["Tạo bản ghi Lịch sử hoạt động mới"]
    H --> I["Chuyển sang màn hình Thông tin (view mode)"]
    I --> J(["Kết thúc"])
    E -->|"Huỷ bỏ (🟡)"| K["Đóng popup, giữ Chờ phê duyệt"]
    K --> J
```

## Flow: Phê duyệt hoặc Từ chối đề xuất

> Nguồn: SRS Web tr.494 — hình lưu đồ UC03.07.05 Phê duyệt/Từ chối đề xuất cấp mới nhà cung cấp HHDV; SRS Web tr.534 — hình lưu đồ UC03.08.05 Phê duyệt/Từ chối đề xuất cấp mới khách hàng DK05; SRS Web tr.571 — hình lưu đồ UC03.09.05 Phê duyệt/Từ chối đề xuất cấp mới xe của khách hàng. Sinh mã (NCC aabbb, KH DK05xxxxx) lấy từ bảng mô tả (🟡 vị trí bước trong dòng thời gian). Nhánh xung đột và Huỷ bỏ lấy từ bảng mô tả (🟡).

### Sequence — Phê duyệt hoặc Từ chối đề xuất
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    participant NT as Người tạo yêu cầu
    alt Từ màn hình Thông tin
        HT-->>ND: Hiển thị màn hình Thông tin
    else Từ màn hình Danh sách
        HT-->>ND: Hiển thị màn hình Danh sách
    end
    alt Phê duyệt
        ND->>HT: Nhấn Phê duyệt
        HT-->>ND: Popup "Phê duyệt đề xuất tạo mới?"
        ND->>HT: Nhấn Phê duyệt trong popup
        HT->>HT: Đổi trạng thái sang Đã phê duyệt và sinh mã (NCC, KH) (🟡)
        HT-->>ND: Toast phê duyệt thành công
        HT->>NT: Gửi thông báo đã được phê duyệt
    else Từ chối
        ND->>HT: Nhấn Từ chối
        HT-->>ND: Popup "Từ chối đề xuất tạo mới?" có ô lý do
        ND->>HT: Nhập lý do (không bắt buộc) và nhấn Từ chối
        HT->>HT: Đổi trạng thái sang Đã từ chối
        HT-->>ND: Toast từ chối thành công
        HT->>NT: Gửi thông báo đã bị từ chối
    end
    HT->>HT: Tạo dòng Lịch sử hoạt động mới
    HT-->>ND: Hiển thị màn hình Thông tin (view mode)
    opt Người khác vừa huỷ trước (🟡)
        HT-->>ND: Popup "Lỗi!" Tải lại trang
    end
```

### Activity — Phê duyệt hoặc Từ chối đề xuất
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> Q{"Đang ở màn hình nào"}
    Q -->|"Thông tin"| B["Hệ thống hiển thị Thông tin"]
    Q -->|"Danh sách"| C["Hệ thống hiển thị Danh sách"]
    B --> D{"Chọn hành động"}
    C --> D
    D -->|"Phê duyệt"| E["Hệ thống hiển thị popup Xác nhận phê duyệt"]
    D -->|"Từ chối"| F["Hệ thống hiển thị popup Xác nhận từ chối"]
    E -->|"Phê duyệt"| G{"Đề xuất vừa bị huỷ (🟡)"}
    F -->|"Từ chối"| G
    E -->|"Huỷ bỏ (🟡)"| H["Đóng popup, giữ Chờ phê duyệt"]
    F -->|"Huỷ bỏ (🟡)"| H
    G -->|"Có"| I["Popup Lỗi: tải lại trang để cập nhật"]
    G -->|"Không"| J["Báo toast và lưu trạng thái mới, sinh mã nếu là NCC hoặc KH (🟡)"]
    J --> K["Gửi thông báo tới người đã tạo yêu cầu"]
    K --> L["Tạo bản ghi Lịch sử hoạt động mới"]
    L --> M["Chuyển sang màn hình Thông tin (view mode)"]
    M --> N(["Kết thúc"])
    H --> N
    I --> N
```

## Flow: Xoá yêu cầu hoặc Tạo mới yêu cầu từ yêu cầu đã huỷ hoặc đã từ chối

> Nguồn: SRS Web tr.472 — UC03.07.02 Xem thông tin nhà cung cấp HHDV (mục "…"); SRS Web tr.492 — UC03.07.04 Huỷ đề xuất cấp mới nhà cung cấp HHDV; SRS Web tr.497 — UC03.07.05; SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục. Không có lưu đồ riêng; vẽ từ mô tả bảng (🔵). Xe: Tạo mới yêu cầu cập nhật cùng bản ghi (SRS Web tr.569 — UC03.09.04 Huỷ đề xuất cấp mới xe của khách hàng); NCC, KH nguồn không nói (🟡).

### Sequence — Xoá yêu cầu hoặc Tạo mới yêu cầu
```mermaid
sequenceDiagram
    participant ND as Người dùng
    participant HT as Hệ thống PMX
    HT-->>ND: Màn hình Thông tin ở trạng thái Đã huỷ hoặc Đã từ chối
    ND->>HT: Nhấn icon ba chấm
    alt Xoá yêu cầu
        ND->>HT: Chọn Xoá yêu cầu
        HT-->>ND: Popup "Xoá yêu cầu?"
        alt Xoá
            ND->>HT: Nhấn Xoá
            HT->>HT: Xoá yêu cầu được chọn
            HT-->>ND: Toast "Xoá yêu cầu thành công" và về Danh sách
        else Huỷ
            HT-->>ND: Về màn hình Thông tin
        end
    else Tạo mới yêu cầu
        ND->>HT: Chọn Tạo mới yêu cầu
        HT-->>ND: Màn hình Tạo mới yêu cầu cấp mới với dữ liệu từ yêu cầu hiện tại
        Note over ND,HT: Tiếp tục theo Flow Tạo đề xuất tạo mới
    end
```

### Activity — Xoá yêu cầu hoặc Tạo mới yêu cầu
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Màn hình Thông tin ở trạng thái Đã huỷ hoặc Đã từ chối"]
    B --> C["Người dùng nhấn icon ba chấm"]
    C --> D{"Chọn hành động"}
    D -->|"Xoá yêu cầu"| E["Hệ thống hiển thị popup Xác nhận xoá"]
    E -->|"Xoá"| F["Xoá yêu cầu và báo toast Xoá yêu cầu thành công"]
    F --> G["Đóng popup và về Danh sách"]
    G --> H(["Kết thúc"])
    E -->|"Huỷ"| I["Quay về màn hình Thông tin"]
    I --> H
    D -->|"Tạo mới yêu cầu"| J["Hiển thị màn hình Tạo mới với dữ liệu yêu cầu cũ"]
    J --> K["Thực hiện Tạo đề xuất tạo mới (Xe: cập nhật cùng bản ghi, NCC và KH: 🟡)"]
    K --> H
```
