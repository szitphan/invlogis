---
type: reverse-srs-flows
feature: account-access
updated: 2026-10-15
---

# Đăng nhập và tài khoản cá nhân (`account-access`) — Flows tái lập (reverse)

## Flow: Đăng nhập

> Nguồn: SRS Web tr.248 — UC01.01 Đăng nhập (lưu đồ bằng chữ); SRS Web tr.253 — UC01.01 Đăng nhập; SRS Web tr.257 — UC01.01 Đăng nhập; SRS Mobile tr.43 — UC01.01.01 Đăng nhập; SRS Mobile tr.44 — UC01.01.01 Đăng nhập. Ngưỡng khoá khác nhau giữa Web (5) và Mobile (10) (xem Conflict); sơ đồ ghi "ngưỡng" chung. Phần chọn tổ chức xem flow riêng.

### Sequence — Đăng nhập
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    ND->>HT: Mở hệ thống (Web) / mở app (Mobile)
    Note over HT: Mobile: Splash 3 giây, Onboarding nếu lần đầu
    alt Có phiên hợp lệ
        HT-->>ND: Bỏ qua đăng nhập, kiểm tra tổ chức
    else Chưa có phiên
        HT-->>ND: Hiện màn Đăng nhập
        ND->>HT: Nhập tên tài khoản + mật khẩu, bấm Đăng nhập
        alt Có trường trống (Web)
            HT-->>ND: Lỗi inline từng ô, không gọi xác thực (E-account-access-020)
        else Đủ thông tin
            HT->>HT: Xác thực tên tài khoản và mật khẩu
            alt Lỗi máy chủ hoặc mất mạng (Web)
                HT-->>ND: Toast lỗi (E-account-access-007 / E-account-access-008)
            else Sai thông tin
                HT-->>ND: Lỗi còn [N] lần thử, xoá mật khẩu (E-account-access-001)
            else Tài khoản bị khoá hoặc vô hiệu hoá
                HT-->>ND: Lỗi liên hệ Admin (E-account-access-002 / E-account-access-003)
            else Không có quyền truy cập
                HT-->>ND: Lỗi không có quyền (E-account-access-004 / E-account-access-005)
            else Đúng và dùng mật khẩu mặc định
                HT-->>ND: Chuyển sang Tạo mật khẩu mới
            else Đúng
                HT->>HT: Xác định loại tài khoản và số chi nhánh
                HT-->>ND: Vào Module Menu / Home hoặc hiện chọn tổ chức
            end
        end
    end
```

### Activity — Đăng nhập
```mermaid
flowchart TD
    A(["Mở hệ thống / mở app"]) --> M{"Mobile?"}
    M -->|"Có"| S["Splash 3 giây"]
    S --> P1{"Có phiên hợp lệ?"}
    M -->|"Không (Web)"| P1
    P1 -->|"Có"| ORG["Kiểm tra tổ chức"]
    P1 -->|"Không"| ONB{"Mobile lần đầu?"}
    ONB -->|"Có"| ONB2["Onboarding, bấm Đăng nhập"]
    ONB -->|"Không"| L["Màn Đăng nhập"]
    ONB2 --> L
    L --> IN["Nhập tên tài khoản + mật khẩu, bấm Đăng nhập"]
    IN --> V{"Có trường trống? (Web)"}
    V -->|"Có"| VE["Lỗi inline từng ô, không gọi API"]
    VE --> L
    V -->|"Không"| AUTH["Hệ thống xác thực"]
    AUTH --> R{"Kết quả"}
    R -->|"Lỗi 5xx hoặc mất mạng (Web)"| TE["Toast lỗi"]
    TE --> L
    R -->|"Sai thông tin"| WR["Lỗi còn N lần thử, xoá mật khẩu"]
    WR --> LK{"Vượt ngưỡng sai? (Web 5 / Mobile 10)"}
    LK -->|"Có"| LOCK["Khoá tài khoản"]
    LK -->|"Không"| L
    R -->|"Tài khoản khoá hoặc vô hiệu hoá"| LOCK2["Lỗi liên hệ Admin"]
    R -->|"Không có quyền truy cập"| NP["Lỗi không có quyền"]
    R -->|"Đúng + mật khẩu mặc định"| NEWPW["Chuyển sang Tạo mật khẩu mới"]
    R -->|"Đúng"| TYPE{"Loại tài khoản (Mobile)"}
    TYPE -->|"Nội bộ hoặc Web"| ORG
    TYPE -->|"Đối tác (Cây dầu)"| HP["Vào Home Partner Portal"]
    ORG --> CNT{"Số chi nhánh/tổ chức"}
    CNT -->|"1 chi nhánh"| HOME["Vào Module Menu / Home nội bộ"]
    CNT -->|"2 trở lên"| SEL["Chọn tổ chức (flow riêng)"]
    LOCK --> KetThuc(["Kết thúc"])
    LOCK2 --> KetThuc
    NP --> KetThuc
    NEWPW --> KetThuc
    HP --> KetThuc
    HOME --> KetThuc
    SEL --> KetThuc
```

## Flow: Chọn tổ chức/chi nhánh sau đăng nhập

> Nguồn: SRS Web tr.254 — UC01.01 Đăng nhập (Modal Chọn tổ chức); SRS Web tr.255 — UC01.01 Đăng nhập; SRS Web tr.256 — UC01.01 Đăng nhập; SRS Web tr.257 — UC01.01 Đăng nhập; SRS Mobile tr.49 — UC01.01.01 Đăng nhập; SRS Mobile tr.50 — UC01.01.01 Đăng nhập; SRS Mobile tr.51 — UC01.01.01 Đăng nhập. Chỉ tài khoản nội bộ.

### Sequence — Chọn tổ chức/chi nhánh
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    HT-->>ND: Hiện Modal (Web) / Bottom Sheet (Mobile) Chọn tổ chức
    Note over HT,ND: Không đóng được bằng click nền hoặc kéo xuống
    opt Muốn tìm chi nhánh
        ND->>HT: Gõ vào ô tìm kiếm
        HT-->>ND: Lọc gần đúng theo thời gian thực
    end
    alt Không có kết quả tìm
        HT-->>ND: Không tìm thấy chi nhánh phù hợp (E-account-access-009)
    end
    alt Bấm Huỷ (hoặc ✕ trên Web)
        ND->>HT: Huỷ
        HT-->>ND: Đăng xuất, về màn Đăng nhập
    else Chọn công ty mẹ hoặc 1 chi nhánh
        ND->>HT: Chọn option rồi bấm Chọn / Xác nhận
        HT-->>ND: Vào Module Menu / Home của phạm vi đã chọn
        Note over HT: Mobile lưu lựa chọn cho lần sau (🟡 Web không nói)
    end
```

### Activity — Chọn tổ chức/chi nhánh
```mermaid
flowchart TD
    A(["Đăng nhập đúng, có 2 chi nhánh trở lên hoặc 2 tổ chức"]) --> B["Hiện Modal / Bottom Sheet Chọn tổ chức"]
    B --> C{"Tài khoản có quyền toàn bộ tổ chức?"}
    C -->|"Có"| D["Hiện option công ty mẹ + dòng HOẶC CHỌN CHI NHÁNH CỤ THỂ"]
    C -->|"Không"| E["Chỉ hiện danh sách chi nhánh"]
    D --> F["Người dùng chọn 1 option hoặc tìm kiếm"]
    E --> F
    F --> G{"Hành động"}
    G -->|"Tìm kiếm không có kết quả"| H["Hiện: Không tìm thấy chi nhánh phù hợp"]
    H --> F
    G -->|"Huỷ hoặc ✕"| I["Đăng xuất, về màn Đăng nhập"]
    G -->|"Chọn 1 option"| J["Nút Chọn / Xác nhận được bật"]
    J --> K["Bấm Chọn / Xác nhận"]
    K --> L["Vào Module Menu / Home của phạm vi đã chọn"]
    I --> KetThuc(["Kết thúc"])
    L --> KetThuc
```

## Flow: Quên mật khẩu — Liên hệ IT

> Nguồn: SRS Web tr.259 — hình lưu đồ UC01.02 Quên mật khẩu; SRS Web tr.260 — UC01.02 Quên mật khẩu; SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Mobile tr.53 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.55 — UC01.01.02 Quên mật khẩu. Bước "IT reset" suy từ câu "ERP call API cho PMX để update mật khẩu mới mà IT đã reset" (🟡).

### Sequence — Quên mật khẩu, Liên hệ IT
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    actor IT as IT Delta
    participant PMX as PMX
    ND->>HT: Bấm Quên mật khẩu ở màn Đăng nhập
    HT-->>ND: Hiện lựa chọn cách lấy lại mật khẩu
    ND->>HT: Chọn Liên hệ IT
    HT-->>ND: Hiện màn Nhập tên tài khoản
    ND->>HT: Nhập tên tài khoản, bấm Xác nhận
    alt Tên tài khoản sai
        HT-->>ND: Tên tài khoản không chính xác (E-account-access-010)
    else Tài khoản không ở trạng thái Đang hoạt động
        HT-->>ND: Không cho đổi mật khẩu (câu lỗi không có trong nguồn 🟡)
    else Gửi quá nhanh (dưới 1 phút)
        HT-->>ND: Popup lỗi 1 lần mỗi phút (E-account-access-011)
    else Hợp lệ
        HT->>IT: Email Yêu cầu hỗ trợ đặt lại mật khẩu tài khoản Delta
        HT-->>ND: Màn Gửi tài khoản thành công
        ND->>HT: Bấm Quay về đăng nhập
        Note over IT,PMX: IT reset, ERP gọi API cập nhật mật khẩu sang PMX, trạng thái Cấp mới (🟡)
    end
```

### Activity — Quên mật khẩu, Liên hệ IT
```mermaid
flowchart TD
    A(["Bắt đầu: màn Đăng nhập"]) --> B["Bấm Quên mật khẩu"]
    B --> C["Hiện popup Chọn cách lấy lại mật khẩu"]
    C --> D["Bấm Liên hệ IT"]
    D --> E["Màn Nhập tên tài khoản"]
    E --> F["Nhập tên tài khoản, bấm Xác nhận"]
    F --> G{"Tên tài khoản đúng?"}
    G -->|"Không"| H["Lỗi: Tên tài khoản không chính xác"]
    G -->|"Có"| GA{"Tài khoản Đang hoạt động?"}
    GA -->|"Không"| GB["Không cho đổi mật khẩu (câu lỗi không có trong nguồn 🟡)"]
    H --> E
    GA -->|"Có"| I{"Đã gửi trong vòng 1 phút?"}
    I -->|"Có"| J["Popup lỗi tối đa 1 lần mỗi phút"]
    J --> E
    I -->|"Không"| K["Gửi email tới IT Delta"]
    K --> L["Màn Gửi tài khoản thành công"]
    L --> M["Quay về đăng nhập"]
    K --> N["IT reset, ERP cập nhật mật khẩu sang PMX, trạng thái Cấp mới (🟡)"]
    M --> KetThuc(["Kết thúc"])
    N --> KetThuc
```

## Flow: Quên mật khẩu — Reset bằng email (Web, gửi link)

> Nguồn: SRS Web tr.259 — hình lưu đồ UC01.02 Quên mật khẩu; SRS Web tr.263 — UC01.02 Quên mật khẩu; SRS Web tr.264 — UC01.02 Quên mật khẩu; SRS Web tr.265 — UC01.02 Quên mật khẩu. Bước người dùng bấm link rồi vào Tạo mật khẩu mới suy từ UC01.05 TH3 (🔵).

### Sequence — Reset bằng email (link)
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    participant EM as Email
    ND->>HT: Quên mật khẩu rồi chọn Reset mật khẩu
    HT-->>ND: Màn Nhập tên tài khoản
    ND->>HT: Nhập tên tài khoản, bấm Xác nhận
    alt Tên tài khoản sai
        HT-->>ND: Tên tài khoản không chính xác (E-account-access-010)
    else Tài khoản không ở trạng thái Đang hoạt động
        HT-->>ND: Không cho đổi mật khẩu (câu lỗi không có trong nguồn 🟡)
    else Gửi quá nhanh
        HT-->>ND: Popup lỗi 1 lần mỗi phút (E-account-access-011)
    else Hợp lệ
        HT->>EM: Gửi email kèm đường link đổi mật khẩu
        HT-->>ND: Màn Kiểm tra hòm thư
        ND->>HT: Bấm Quay về đăng nhập
        EM-->>ND: Email Yêu cầu reset mật khẩu cho tài khoản Delta
        ND->>HT: Bấm link trong email (🔵)
        HT-->>ND: Màn Tạo mật khẩu mới (TH3)
    end
```

### Activity — Reset bằng email (link)
```mermaid
flowchart TD
    A(["Bắt đầu: màn Đăng nhập"]) --> B["Bấm Quên mật khẩu rồi Reset mật khẩu"]
    B --> C["Màn Nhập tên tài khoản"]
    C --> D["Nhập tên tài khoản, bấm Xác nhận"]
    D --> E{"Tên tài khoản đúng?"}
    E -->|"Không"| F["Lỗi: Tên tài khoản không chính xác"]
    E -->|"Có"| EA{"Tài khoản Đang hoạt động?"}
    EA -->|"Không"| EB["Không cho đổi mật khẩu (câu lỗi không có trong nguồn 🟡)"]
    F --> C
    EA -->|"Có"| G{"Đã gửi trong vòng 1 phút?"}
    G -->|"Có"| H["Popup lỗi tối đa 1 lần mỗi phút"]
    H --> C
    G -->|"Không"| I["Gửi email reset tới email của tài khoản"]
    I --> J["Màn Kiểm tra hòm thư"]
    J --> K["Bấm Quay về đăng nhập"]
    I --> L["Người dùng mở email, bấm link (🔵)"]
    L --> M["Màn Tạo mật khẩu mới"]
    K --> KetThuc(["Kết thúc"])
    M --> KetThuc
```

## Flow: Quên mật khẩu — Reset bằng email (Mobile, mã OTP)

> Nguồn: SRS Mobile tr.52 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.55 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.56 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.57 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.58 — UC01.01.02 Quên mật khẩu; SRS Mobile tr.59 — UC01.01.02 Quên mật khẩu. Mục "Lưu đồ hoạt động" của UC này không có hình trong bản nguồn nên flow dựng từ bảng mô tả màn (🔵).

### Sequence — Reset bằng email (OTP)
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    participant EM as Email
    ND->>HT: Quên mật khẩu rồi chọn Reset mật khẩu
    HT-->>ND: Màn Nhập tên tài khoản
    ND->>HT: Nhập tên tài khoản, bấm Xác nhận
    alt Tên tài khoản sai
        HT-->>ND: Tên tài khoản không chính xác (E-account-access-010)
    else Tài khoản không ở trạng thái Đang hoạt động
        HT-->>ND: Không cho đổi mật khẩu (câu lỗi không có trong nguồn 🟡)
    else Gửi quá nhanh
        HT-->>ND: Popup lỗi 1 lần mỗi phút (E-account-access-011)
    else Hợp lệ
        HT->>EM: Gửi email OTP 6 ký tự, hiệu lực 5 phút
        HT-->>ND: Màn Nhập OTP, nút Gửi lại mã khoá đếm ngược
        ND->>HT: Nhập đủ 6 chữ số
        alt OTP đúng
            HT-->>ND: Màn Tạo mật khẩu mới
        else OTP sai hoặc hết hạn
            HT-->>ND: Popup OTP không hợp lệ hoặc hết hạn (E-account-access-013)
        else Sai 5 lần
            HT-->>ND: Popup đã nhập sai 5 lần, gửi lại mã (E-account-access-012)
        end
        opt Sau 5 phút nút Gửi lại mã bật
            ND->>HT: Bấm Gửi lại mã
            HT->>EM: Email OTP mới, reply email OTP cũ
        end
    end
```

### Activity — Reset bằng email (OTP)
```mermaid
flowchart TD
    A(["Bắt đầu: màn Đăng nhập"]) --> B["Quên mật khẩu rồi Reset mật khẩu"]
    B --> C["Màn Nhập tên tài khoản"]
    C --> D["Nhập tên tài khoản, bấm Xác nhận"]
    D --> E{"Tên tài khoản đúng?"}
    E -->|"Không"| F["Lỗi: Tên tài khoản không chính xác"]
    E -->|"Có"| EA{"Tài khoản Đang hoạt động?"}
    EA -->|"Không"| EB["Không cho đổi mật khẩu (câu lỗi không có trong nguồn 🟡)"]
    F --> C
    EA -->|"Có"| G{"Đã gửi trong vòng 1 phút?"}
    G -->|"Có"| H["Popup lỗi tối đa 1 lần mỗi phút"]
    H --> C
    G -->|"Không"| I["Gửi email OTP, mở màn Nhập OTP"]
    I --> J["Nhập 6 chữ số OTP"]
    J --> K{"OTP hợp lệ?"}
    K -->|"Đúng"| L["Màn Tạo mật khẩu mới"]
    K -->|"Sai hoặc hết hạn"| M["Popup OTP không hợp lệ hoặc hết hạn"]
    M --> N{"Đã sai 5 lần?"}
    N -->|"Có"| O["Popup sai 5 lần, gửi lại mã OTP mới"]
    N -->|"Không"| J
    O --> P{"Hết 5 phút, nút Gửi lại mã bật?"}
    P -->|"Có"| Q["Bấm Gửi lại mã, email OTP mới"]
    Q --> J
    P -->|"Chưa"| R["Chờ đếm ngược hoặc bấm Back về Đăng nhập (🟡)"]
    L --> KetThuc(["Kết thúc"])
    R --> KetThuc
```

## Flow: Đăng xuất

> Nguồn: SRS Web tr.267 — hình lưu đồ UC01.03 Đăng xuất; SRS Web tr.268 — UC01.03 Đăng xuất; SRS Mobile tr.60 — hình lưu đồ UC01.01.03 Đăng xuất; SRS Mobile tr.61 — UC01.01.03 Đăng xuất; SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu (đường vào riêng của tài khoản cây dầu: tab Tài khoản, không qua dropdown Avatar).

### Sequence — Đăng xuất
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    alt Web hoặc Mobile nội bộ
        ND->>HT: Bấm icon Avatar
        HT-->>ND: Hiện dropdown Tài khoản
        ND->>HT: Chọn Đăng xuất
        HT->>HT: Đăng xuất tài khoản
    else Tài khoản cây dầu (Mobile)
        ND->>HT: Ở màn Tài khoản bấm nút Đăng xuất
        HT-->>ND: Hộp xác nhận Bạn có chắc muốn đăng xuất
        alt Bấm Ở lại
            ND->>HT: Ở lại
            HT-->>ND: Quay lại màn Tài khoản
        else Bấm Đăng xuất
            ND->>HT: Đăng xuất
            HT->>HT: Đăng xuất tài khoản
        end
    end
    HT-->>ND: Hiện màn Đăng nhập
```

### Activity — Đăng xuất
```mermaid
flowchart TD
    A(["Bắt đầu: đã đăng nhập"]) --> Q{"Loại tài khoản và đường vào"}
    Q -->|"Web hoặc Mobile nội bộ"| B["Bấm icon Avatar"]
    B --> C["Hiện dropdown Tài khoản"]
    C --> D["Chọn Đăng xuất"]
    D --> I["Thực hiện đăng xuất tài khoản"]
    Q -->|"Tài khoản cây dầu (Mobile)"| E["Ở màn Tài khoản bấm nút Đăng xuất"]
    E --> F["Hộp xác nhận: Bạn có chắc muốn đăng xuất?"]
    F --> G{"Chọn"}
    G -->|"Ở lại"| H["Quay lại màn Tài khoản"]
    G -->|"Đăng xuất"| I
    I --> J["Hiện màn Đăng nhập"]
    H --> KetThuc(["Kết thúc"])
    J --> KetThuc
```

## Flow: Đổi mật khẩu

> Nguồn: SRS Web tr.269 — hình lưu đồ UC01.04 Đổi mật khẩu; SRS Web tr.270 — UC01.04 Đổi mật khẩu; SRS Web tr.271 — UC01.04 Đổi mật khẩu; SRS Web tr.272 — UC01.04 Đổi mật khẩu; SRS Mobile tr.62 — hình lưu đồ UC01.01.04 Đổi mật khẩu; SRS Mobile tr.63 — UC01.01.04 Đổi mật khẩu; SRS Mobile tr.64 — UC01.01.04 Đổi mật khẩu; SRS Mobile tr.65 — UC01.01.04 Đổi mật khẩu.

### Sequence — Đổi mật khẩu
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    participant ERP as ERP Delta
    ND->>HT: Từ Thông tin cá nhân bấm Đổi mật khẩu (nút trên màn hoặc trong Hành động, xem Conflict)
    HT-->>ND: Hiện popup Đổi mật khẩu
    ND->>HT: Nhập mật khẩu cũ, mật khẩu mới, xác nhận, bấm Xác nhận
    HT->>HT: Kiểm tra hợp lệ ba ô
    alt Có lỗi
        HT-->>ND: Lỗi cụ thể (E-account-access-014 đến E-account-access-017)
    else Hợp lệ
        HT->>ERP: Cập nhật mật khẩu mới
        HT-->>ND: Toast/popup Đổi mật khẩu thành công, tắt popup
        HT-->>ND: Quay lại màn Thông tin tài khoản
    end
```

### Activity — Đổi mật khẩu
```mermaid
flowchart TD
    A(["Bắt đầu: màn Thông tin cá nhân"]) --> B["Bấm Đổi mật khẩu (nút trên màn hoặc trong Hành động / menu)"]
    B --> C["Hiện popup Đổi mật khẩu"]
    C --> D["Nhập mật khẩu cũ, mật khẩu mới, xác nhận mật khẩu mới"]
    D --> E["Bấm Xác nhận"]
    E --> F{"Kiểm tra hợp lệ 3 ô"}
    F -->|"Có lỗi (thứ tự kiểm tra 🟡)"| G["Lỗi cụ thể: mật khẩu cũ sai, mật khẩu mới yếu hoặc trùng mật khẩu cũ, xác nhận không khớp"]
    G --> C
    F -->|"Hợp lệ"| N["Cập nhật mật khẩu qua ERP Delta"]
    N --> O["Thông báo Đổi mật khẩu thành công, tắt popup"]
    O --> P["Hiện lại màn Thông tin tài khoản"]
    P --> KetThuc(["Kết thúc"])
```

## Flow: Tạo mật khẩu mới

> Nguồn: SRS Web tr.273 — UC01.05 Tạo mật khẩu mới; SRS Web tr.274 — hình lưu đồ UC01.05 Tạo mật khẩu mới; SRS Web tr.275 — UC01.05 Tạo mật khẩu mới; SRS Web tr.276 — UC01.05 Tạo mật khẩu mới; SRS Web tr.277 — UC01.05 Tạo mật khẩu mới; SRS Mobile tr.66 — UC01.01.05 Tạo mật khẩu mới; SRS Mobile tr.67 — hình lưu đồ UC01.01.05 Tạo mật khẩu mới; SRS Mobile tr.68-70 — UC01.01.05 Tạo mật khẩu mới. Kết thúc: lưu đồ và điều kiện sau nói về màn Đăng nhập (✅), nút "Đổi mật khẩu" nói tự đăng nhập (🟡, xem Conflict).

### Sequence — Tạo mật khẩu mới
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    participant PMX as ERP và PMX
    alt TH1 hoặc TH2 đăng nhập bằng mật khẩu mặc định
        ND->>HT: Đăng nhập bằng mật khẩu mặc định
        HT->>HT: Kiểm tra hợp lệ tài khoản
    else TH3 từ link hoặc luồng Reset bằng email
        ND->>HT: Mở màn Tạo mật khẩu mới từ email
    end
    HT-->>ND: Hiện màn Tạo mật khẩu mới
    ND->>HT: Nhập mật khẩu mới, nhập lại, xác nhận
    HT->>HT: Kiểm tra hợp lệ
    alt Có lỗi kiểm tra
        HT-->>ND: Lỗi cụ thể (E-account-access-015, E-account-access-017, E-account-access-018)
    else Cập nhật không thành công
        HT-->>ND: Đã có lỗi xảy ra, vui lòng thử lại (E-account-access-019)
    else Thành công
        HT->>PMX: Cập nhật mật khẩu
        HT-->>ND: Toast Đổi mật khẩu thành công
        HT-->>ND: Hiện màn Đăng nhập (🟡 hoặc tự vào trang chủ)
    end
```

### Activity — Tạo mật khẩu mới
```mermaid
flowchart TD
    A(["Bắt đầu"]) --> Q{"Đường vào"}
    Q -->|"TH1/TH2: đăng nhập bằng mật khẩu mặc định"| B["Hiện màn Đăng nhập, đăng nhập mật khẩu mặc định"]
    B --> C["Kiểm tra hợp lệ"]
    C --> D["Hiện màn Tạo mật khẩu mới"]
    Q -->|"TH3: link hoặc luồng Reset bằng email"| D
    D --> E["Nhập mật khẩu mới + nhập lại, bấm Xác nhận"]
    E --> F{"Kiểm tra hợp lệ"}
    F -->|"Có lỗi (thứ tự kiểm tra 🟡)"| G["Lỗi cụ thể: mật khẩu yếu, trùng mật khẩu mặc định hoặc xác nhận không khớp"]
    G --> D
    F -->|"Hợp lệ"| L["Update mật khẩu (ERP + PMX)"]
    L --> M{"Cập nhật thành công?"}
    M -->|"Không"| N["Lỗi: Đã có lỗi xảy ra, vui lòng thử lại"]
    N --> D
    M -->|"Có"| O["Toast Đổi mật khẩu thành công"]
    O --> P["Hiện màn Đăng nhập (🟡 hoặc tự đăng nhập)"]
    P --> KetThuc(["Kết thúc"])
```

## Flow: Xem thông tin cá nhân

> Nguồn: SRS Web tr.278 — hình lưu đồ UC01.06 Xem thông tin cá nhân; SRS Web tr.279 — UC01.06 Xem thông tin cá nhân; SRS Web tr.280 — UC01.06 Xem thông tin cá nhân; SRS Web tr.281 — UC01.06 Xem thông tin cá nhân; SRS Mobile tr.71 — hình lưu đồ UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ; SRS Mobile tr.72-74 — UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ. Nhánh menu Mobile đọc từ ảnh màn Thông tin tài khoản (SRS Mobile tr.72 — hình UC01.01.06 Xem thông tin cá nhân - Tài khoản nội bộ).

### Sequence — Xem thông tin cá nhân
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    ND->>HT: Bấm icon Avatar rồi Thông tin tài khoản (Mobile còn icon Tài khoản trên Navigation Bar)
    HT-->>ND: Hiện màn Thông tin tài khoản chỉ đọc
    opt Bấm Lịch sử hoạt động
        ND->>HT: Lịch sử hoạt động
        HT-->>ND: Popup Lịch sử hoạt động của nhân viên
    end
    opt Bấm Hành động
        ND->>HT: Hành động
        HT-->>ND: Đổi mật khẩu (popup) hoặc Đăng xuất (Mobile)
    end
```

### Activity — Xem thông tin cá nhân
```mermaid
flowchart TD
    A(["Bắt đầu: màn bất kỳ"]) --> B["Bấm icon Avatar rồi chọn Thông tin tài khoản"]
    B --> C["Hiện màn Thông tin tài khoản"]
    C --> D{"Người dùng chọn"}
    D -->|"Chỉ xem"| KetThuc(["Kết thúc"])
    D -->|"Lịch sử hoạt động"| E["Popup Lịch sử hoạt động của nhân viên"]
    D -->|"Hành động: Đổi mật khẩu"| F["Popup Đổi mật khẩu (flow riêng)"]
    D -->|"Hành động: Đăng xuất (Mobile)"| G["UC Đăng xuất (flow riêng)"]
    E --> KetThuc
    F --> KetThuc
    G --> KetThuc
```

## Flow: Xem thông tin tài khoản cây dầu (Mobile)

> Nguồn: SRS Mobile tr.75 — UC01.01.07 Xem thông tin tài khoản cây dầu (lưu đồ bằng chữ); SRS Mobile tr.76-79 — UC01.01.07 Xem thông tin tài khoản cây dầu.

### Sequence — Xem thông tin tài khoản cây dầu
```mermaid
sequenceDiagram
    actor ND as Nhân viên cây dầu
    participant HT as Hệ thống
    ND->>HT: Tap tab Tài khoản hoặc Avatar trên Trang chủ
    HT-->>ND: Tải thông tin (skeleton loader), hiện màn chỉ đọc
    ND->>HT: Xem thông tin, hạn mức, hợp đồng
    opt Đăng xuất
        ND->>HT: Tap Đăng xuất
        HT-->>ND: Hộp xác nhận Bạn có chắc muốn đăng xuất
        ND->>HT: Bấm Đăng xuất
        HT-->>ND: Về màn đăng nhập
    end
```

### Activity — Xem thông tin tài khoản cây dầu
```mermaid
flowchart TD
    A(["Bắt đầu: Home Partner Portal"]) --> B["Tap tab Tài khoản hoặc Avatar"]
    B --> C["Tải thông tin, hiện skeleton loader"]
    C --> D["Hiện thông tin cây dầu, hạn mức, hợp đồng (chỉ đọc)"]
    D --> E{"Người dùng chọn"}
    E -->|"Chỉ xem"| KetThuc(["Kết thúc"])
    E -->|"Tap Đăng xuất"| F["Hộp xác nhận Bạn có chắc muốn đăng xuất?"]
    F -->|"Ở lại"| D
    F -->|"Đăng xuất"| G["Đăng xuất, redirect về màn đăng nhập"]
    G --> KetThuc
```

## Flow: Đổi ngôn ngữ (Web)

> Nguồn: SRS Web tr.160 — hình lưu đồ UC02.03.01 Thay đổi ngôn ngữ; SRS Web tr.161 — UC02.03.01 Thay đổi ngôn ngữ; SRS Web tr.162 — UC02.03.01 Thay đổi ngôn ngữ.

### Sequence — Đổi ngôn ngữ
```mermaid
sequenceDiagram
    actor ND as Người dùng
    participant HT as Hệ thống
    ND->>HT: Bấm icon Avatar
    HT-->>ND: Dropdown Tài khoản
    ND->>HT: Chọn Ngôn ngữ
    HT-->>ND: Danh sách Tiếng Anh, Tiếng Việt, Tiếng Nhật
    ND->>HT: Chọn 1 ngôn ngữ
    HT-->>ND: Tải lại giao diện theo ngôn ngữ mới + toast thành công
```

### Activity — Đổi ngôn ngữ
```mermaid
flowchart TD
    A(["Bắt đầu: màn bất kỳ"]) --> B["Bấm icon Avatar"]
    B --> C["Hiện dropdown Tài khoản"]
    C --> D["Chọn Ngôn ngữ"]
    D --> E["Chọn 1 ngôn ngữ: Anh, Việt hoặc Nhật"]
    E --> F["Hiển thị giao diện với ngôn ngữ được chọn, toast thành công"]
    F --> KetThuc(["Kết thúc"])
```
