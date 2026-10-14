---
type: reverse-srs-flows
feature: product-catalog
updated: 2026-10-15
---

# Danh mục hàng hoá và dịch vụ kỹ thuật (`product-catalog`) — Flows tái lập (reverse)

## Flow: Xem danh sách danh mục

> Nguồn: SRS Web tr.288 — hình lưu đồ UC03.01.01 Xem danh mục Dịch vụ kỹ thuật; cùng khuôn ở SRS Web tr.325 — hình lưu đồ UC03.03.01; SRS Web tr.361 — hình lưu đồ UC03.04.01; SRS Web tr.394 — hình lưu đồ UC03.05.01; SRS Web tr.427 — hình lưu đồ UC03.06.01. Áp cho cả 5 danh mục (Dịch vụ kỹ thuật, Phụ tùng vật tư, Công cụ dụng cụ, Lốp, Ắc quy), chỉ khác tên sub-tab. ✅

### Sequence — Xem danh sách danh mục
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    ND->>HT: Mở Dashboards
    HT-->>ND: Hiển thị màn Dashboards
    ND->>HT: Chọn tab Danh mục ở thanh điều hướng
    ND->>HT: Chọn sub-tab của danh mục
    HT-->>ND: Hiển thị màn Danh sách danh mục
```

### Activity — Xem danh sách danh mục
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hiển thị màn Dashboards"]
    B --> C["Người dùng chọn tab Danh mục ở Navigation bar"]
    C --> D["Người dùng chọn sub-tab của danh mục"]
    D --> E["Hiển thị màn Danh sách danh mục"]
    E --> F(["Kết thúc"])
```

## Flow: Xem thông tin danh mục

> Nguồn: SRS Web tr.293 — hình lưu đồ UC03.01.02 Xem thông tin Dịch vụ kỹ thuật; cùng khuôn ở SRS Web tr.329 — hình lưu đồ UC03.03.02; SRS Web tr.365 — hình lưu đồ UC03.04.02; SRS Web tr.399 — hình lưu đồ UC03.05.02; SRS Web tr.432 — hình lưu đồ UC03.06.02. ✅

### Sequence — Xem thông tin danh mục
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    HT-->>ND: Hiển thị màn Danh sách
    ND->>HT: Chọn 1 bản ghi trong danh sách
    HT-->>ND: Hiển thị màn Thông tin
```

### Activity — Xem thông tin danh mục
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hiển thị màn Danh sách"]
    B --> C["Người dùng chọn 1 bản ghi trong danh sách"]
    C --> D["Hiển thị màn Thông tin"]
    D --> E(["Kết thúc"])
```

## Flow: Tạo đề xuất tạo mới

> Nguồn: SRS Web tr.298 — hình lưu đồ UC03.01.03 Tạo đề xuất tạo mới Dịch vụ kỹ thuật; cùng khuôn ở SRS Web tr.334 — hình lưu đồ UC03.03.03; SRS Web tr.370 — hình lưu đồ UC03.04.03; SRS Web tr.405 — hình lưu đồ UC03.05.03; SRS Web tr.437 — hình lưu đồ UC03.06.03. Lưu đồ ghi bước "Hiển thị popup Tạo mới", mô tả chữ ghi "màn hình Tạo mới", ảnh cho thấy panel trượt bên phải (SRS Web tr.299 — ảnh UC03.01.03). Lưu đồ chỉ vẽ nhánh hợp lệ; nhánh lỗi in-line và gửi thông báo lấy từ mô tả chữ (SRS Web tr.302–303 — UC03.01.03). ✅ cho bước trong lưu đồ, 🔵 cho vị trí bước thông báo.

### Sequence — Tạo đề xuất tạo mới
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    participant TB as Thông báo
    HT-->>ND: Hiển thị màn Danh sách
    ND->>HT: Nhấn nút Tạo mới
    HT-->>ND: Hiển thị form Tạo mới
    ND->>HT: Nhập thông tin và xác nhận
    HT->>HT: Kiểm tra validate
    alt Có trường không hợp lệ
        HT-->>ND: Lỗi in-line dưới trường không hợp lệ
    else Hợp lệ
        HT->>HT: Lưu bản ghi Chờ phê duyệt
        HT-->>ND: Toast thành công
        HT->>HT: Tạo bản ghi Lịch sử hoạt động
        HT->>TB: Gửi thông báo cho người có quyền phê duyệt (🔵)
        HT-->>ND: Chuyển sang màn Thông tin (xem)
    end
```

### Activity — Tạo đề xuất tạo mới
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B["Hiển thị màn Danh sách"]
    B --> C["Người dùng nhấn Tạo mới"]
    C --> D["Hiển thị form Tạo mới"]
    D --> E["Người dùng nhập thông tin và xác nhận"]
    E --> F{"Kiểm tra validate"}
    F -->|Không hợp lệ| G["Lỗi in-line dưới trường không hợp lệ"]
    G --> D
    F -->|Hợp lệ| H["Toast thành công và lưu bản ghi Chờ phê duyệt"]
    H --> I["Tạo bản ghi Lịch sử hoạt động"]
    I --> J["Gửi thông báo cho người có quyền phê duyệt (🔵)"]
    J --> K["Chuyển sang màn Thông tin (xem)"]
    K --> L(["Kết thúc"])
```

## Flow: Huỷ bỏ khi đang tạo đề xuất

> Nguồn: SRS Web tr.303–304 — UC03.01.03 Tạo đề xuất tạo mới Dịch vụ kỹ thuật (nút Huỷ và icon đóng; mô tả chữ, không có hình lưu đồ riêng); cùng khuôn ở SRS Web tr.339–340 — UC03.03.03; SRS Web tr.374–375 — UC03.04.03; SRS Web tr.410 — UC03.05.03; SRS Web tr.442 — UC03.06.03. ✅

### Sequence — Huỷ bỏ khi đang tạo đề xuất
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    ND->>HT: Nhấn Huỷ hoặc icon đóng ở form Tạo mới
    HT-->>ND: Hộp thoại xác nhận huỷ tạo mới
    alt Xác nhận
        HT-->>ND: Không tạo bản ghi và về màn Danh sách
    else Hủy
        HT-->>ND: Quay lại form Tạo mới với dữ liệu đã nhập
    end
```

### Activity — Huỷ bỏ khi đang tạo đề xuất
```mermaid
flowchart TD
    A(["Bắt đầu: đang ở form Tạo mới"]) --> B["Nhấn Huỷ hoặc icon đóng"]
    B --> C["Hiển thị hộp thoại xác nhận huỷ tạo mới"]
    C --> D{"Người dùng chọn"}
    D -->|Xác nhận| E["Không tạo bản ghi và về màn Danh sách"]
    D -->|Hủy| F["Quay lại form Tạo mới với dữ liệu đã nhập"]
    E --> G(["Kết thúc"])
    F --> G
```

## Flow: Huỷ đề xuất cấp mới

> Nguồn: SRS Web tr.308 — hình lưu đồ UC03.01.04 Huỷ đề xuất cấp mới Dịch vụ kỹ thuật; cùng khuôn ở SRS Web tr.344 — hình lưu đồ UC03.03.04; SRS Web tr.378 — hình lưu đồ UC03.04.04; SRS Web tr.413 — hình lưu đồ UC03.05.04; SRS Web tr.444 — hình lưu đồ UC03.06.04. Lưu đồ không vẽ nhánh Huỷ bỏ và bước gửi thông báo; hai bước này lấy từ mô tả chữ (SRS Web tr.310–311 — UC03.01.04). ✅ cho bước trong lưu đồ, 🔵 cho vị trí bước thông báo.

### Sequence — Huỷ đề xuất cấp mới
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    participant TB as Thông báo
    HT-->>ND: Hiển thị màn Thông tin hoặc Danh sách
    ND->>HT: Nhấn Huỷ đề xuất
    HT-->>ND: Popup Xác nhận huỷ
    alt Huỷ bỏ
        HT-->>ND: Đóng popup và giữ Chờ phê duyệt
    else Xác nhận
        HT->>HT: Lưu trạng thái Đã huỷ
        HT-->>ND: Toast thành công
        HT->>HT: Tạo bản ghi Lịch sử hoạt động
        HT->>TB: Gửi thông báo cho người có quyền phê duyệt (🔵)
        HT-->>ND: Chuyển sang màn Thông tin (xem)
    end
```

### Activity — Huỷ đề xuất cấp mới
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B{"Vào từ đâu"}
    B -->|"Từ màn Thông tin"| C["Hiển thị màn Thông tin"]
    B -->|"Từ màn Danh sách"| D["Hiển thị màn Danh sách"]
    C --> E["Người dùng nhấn Huỷ đề xuất"]
    D --> E
    E --> F["Hiển thị popup Xác nhận huỷ"]
    F --> G{"Người dùng chọn"}
    G -->|Huỷ bỏ| H["Đóng popup và giữ Chờ phê duyệt"]
    G -->|Xác nhận| I["Toast thành công và lưu trạng thái Đã huỷ"]
    I --> J["Tạo bản ghi Lịch sử hoạt động"]
    J --> K["Gửi thông báo cho người có quyền phê duyệt (🔵)"]
    K --> L["Chuyển sang màn Thông tin (xem)"]
    H --> M(["Kết thúc"])
    L --> M
```

## Flow: Phê duyệt / Từ chối đề xuất cấp mới

> Nguồn: SRS Web tr.314 — hình lưu đồ UC03.01.05 Phê duyệt/Từ chối đề xuất cấp mới Dịch vụ kỹ thuật; cùng khuôn ở SRS Web tr.350 — hình lưu đồ UC03.03.05; SRS Web tr.383 — hình lưu đồ UC03.04.05; SRS Web tr.418 — hình lưu đồ UC03.05.05; SRS Web tr.450 — hình lưu đồ UC03.06.05. Lưu đồ không vẽ nhánh bỏ xác nhận (nút Huỷ bỏ hoặc Huỷ), nhánh xung đột đồng thời, nhập lý do, sinh mã, gửi thông báo; các bước này lấy từ mô tả chữ (SRS Web tr.316–320 — UC03.01.05). ✅ cho bước trong lưu đồ, 🔵 cho vị trí bước thông báo và sinh mã.

### Sequence — Phê duyệt / Từ chối đề xuất cấp mới
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    participant TB as Thông báo
    HT-->>ND: Hiển thị màn Thông tin hoặc Danh sách
    alt Chọn Phê duyệt
        ND->>HT: Nhấn Phê duyệt
        HT-->>ND: Popup Xác nhận phê duyệt
        alt Huỷ
            ND->>HT: Nhấn Huỷ trong popup
            HT-->>ND: Đóng popup và giữ Chờ phê duyệt
        else Phê duyệt
            ND->>HT: Nhấn Phê duyệt trong popup
            alt Đề xuất vừa bị huỷ
                HT-->>ND: Popup Lỗi với nút Tải lại trang
            else Còn Chờ phê duyệt
                HT->>HT: Lưu trạng thái Đã phê duyệt và sinh mã
                HT-->>ND: Toast thành công
                HT->>HT: Tạo bản ghi Lịch sử hoạt động
                HT->>TB: Gửi thông báo cho người đã tạo yêu cầu (🔵)
                HT-->>ND: Chuyển sang màn Thông tin (xem)
            end
        end
    else Chọn Từ chối
        ND->>HT: Nhấn Từ chối
        HT-->>ND: Popup Xác nhận từ chối với Lý do từ chối
        alt Huỷ bỏ
            ND->>HT: Nhấn Huỷ bỏ trong popup
            HT-->>ND: Đóng popup và giữ Chờ phê duyệt
        else Từ chối
            ND->>HT: Nhập lý do (tuỳ chọn) và nhấn Từ chối
            alt Đề xuất vừa bị huỷ
                HT-->>ND: Popup Lỗi với nút Tải lại trang
            else Còn Chờ phê duyệt
                HT->>HT: Lưu trạng thái Đã từ chối
                HT-->>ND: Toast thành công
                HT->>HT: Tạo bản ghi Lịch sử hoạt động
                HT->>TB: Gửi thông báo cho người đã tạo yêu cầu (🔵)
                HT-->>ND: Chuyển sang màn Thông tin (xem)
            end
        end
    end
```

### Activity — Phê duyệt / Từ chối đề xuất cấp mới
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> B{"Vào từ đâu"}
    B -->|"Từ màn Thông tin"| C["Hiển thị màn Thông tin"]
    B -->|"Từ màn Danh sách"| D["Hiển thị màn Danh sách"]
    C --> E{"Người dùng chọn"}
    D --> E
    E -->|Phê duyệt| F["Hiển thị popup Xác nhận phê duyệt"]
    E -->|Từ chối| G["Hiển thị popup Xác nhận từ chối"]
    F --> F1{"Nhấn Phê duyệt hay Huỷ"}
    G --> G1{"Nhấn Từ chối hay Huỷ bỏ"}
    F1 -->|Huỷ bỏ| Z["Đóng popup và giữ Chờ phê duyệt"]
    G1 -->|Huỷ bỏ| Z
    F1 -->|Phê duyệt| X{"Đề xuất đã bị huỷ trước đó"}
    G1 -->|Từ chối| X
    X -->|Có| Y["Popup lỗi với nút Tải lại trang"]
    X -->|Không| H["Toast thành công và lưu trạng thái mới"]
    H --> I["Tạo bản ghi Lịch sử hoạt động"]
    I --> J["Gửi thông báo cho người đã tạo yêu cầu (🔵)"]
    J --> K["Chuyển sang màn Thông tin (xem)"]
    Z --> M(["Kết thúc"])
    Y --> M
    K --> M
```

## Flow: Xoá yêu cầu và Tạo mới yêu cầu từ bản đã huỷ hoặc đã từ chối

> Nguồn: SRS Web tr.296–297 — UC03.01.02 Xem thông tin Dịch vụ kỹ thuật; SRS Web tr.311–312 — UC03.01.04 Huỷ đề xuất cấp mới Dịch vụ kỹ thuật; SRS Web tr.317–318 — UC03.01.05 Phê duyệt/Từ chối đề xuất cấp mới Dịch vụ kỹ thuật; cùng khuôn ở 4 danh mục còn lại (PTVT tr.332, 347–348, 353–354; CCDC tr.368, 380–381, 386–387; Lốp tr.402, 415–416, 420–421; Ắc quy tr.435, 447–448, 453–454). Nguồn mô tả bằng chữ, không có hình lưu đồ riêng. ✅ cho bước Xoá; 🔵 cho kết quả "Tạo mới yêu cầu" ở trạng thái Đã từ chối (OQ-3).

### Sequence — Xoá yêu cầu và Tạo mới yêu cầu
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống PMX
    HT-->>ND: Màn Thông tin ở trạng thái Đã huỷ hoặc Đã từ chối
    ND->>HT: Chọn icon ba chấm
    alt Xoá yêu cầu
        HT-->>ND: Popup Xác nhận xoá
        alt Xoá
            HT->>HT: Xoá yêu cầu đã chọn
            HT-->>ND: Toast Xoá yêu cầu thành công và về màn Danh sách
        else Huỷ
            HT-->>ND: Quay về màn Thông tin
        end
    else Tạo mới yêu cầu
        HT-->>ND: Màn Tạo mới yêu cầu với thông tin lấy từ yêu cầu hiện tại
        ND->>HT: Chỉnh sửa và xác nhận
        HT->>HT: Cập nhật bản ghi và đưa về Chờ phê duyệt (🔵)
    end
```

### Activity — Xoá yêu cầu và Tạo mới yêu cầu
```mermaid
flowchart TD
    A(["Bắt đầu: màn Thông tin ở Đã huỷ hoặc Đã từ chối"]) --> B["Người dùng chọn icon ba chấm"]
    B --> C{"Hành động"}
    C -->|Xoá yêu cầu| D["Hiển thị popup Xác nhận xoá"]
    D --> E{"Người dùng chọn"}
    E -->|Xoá| F["Xoá yêu cầu và toast Xoá yêu cầu thành công"]
    F --> G["Đóng popup và về màn Danh sách"]
    E -->|Huỷ| H["Quay về màn Thông tin"]
    C -->|Tạo mới yêu cầu| I["Hiển thị màn Tạo mới yêu cầu với dữ liệu cũ"]
    I --> J["Người dùng chỉnh sửa và xác nhận"]
    J --> K["Cập nhật bản ghi, không sinh bản ghi mới, trạng thái về Chờ phê duyệt (🔵)"]
    G --> L(["Kết thúc"])
    H --> L
    K --> L
```
