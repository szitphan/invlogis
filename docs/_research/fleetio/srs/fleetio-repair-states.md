---
type: research
feature: fleetio-repair
updated: 2026-11-03
---

# Sửa chữa — States

Ô "Không có" nghĩa là đã quan sát và không xảy ra, trừ khi có ghi "chưa thử". Mức theo bản ghi chạy 03/11/2026.

## Sự cố

Fleetio lưu ba giá trị: Open, Resolved, Closed. **Overdue là giá trị tính**, không phải trạng thái lưu: đọc từ hạn và đồng hồ hiện tại, không có sự kiện chuyển. Sơ đồ vẽ tách Resolved theo nguồn vì ba nguồn có cách mở lại khác nhau; Fleetio chỉ hiện một chữ Resolved. "Đã gắn lệnh" cũng là điều kiện trên Open, không phải giá trị trạng thái.

```mermaid
stateDiagram-v2
    [*] --> Open: Lưu sự cố
    Open --> Overdue: Ngày qua hạn hoặc đồng hồ vượt hạn, tự tính
    Overdue --> Open: Đổi hạn sang tương lai, tự tính
    Open --> ResolvedNote: Resolve with Note
    Open --> ResolvedEntry: Lưu Service Entry
    Open --> ResolvedWO: Lệnh chứa nó hoàn thành
    Open --> Closed: Close
    Overdue --> ResolvedNote: Resolve with Note
    Overdue --> ResolvedEntry: Lưu Service Entry
    Overdue --> ResolvedWO: Lệnh chứa nó hoàn thành
    Overdue --> Closed: Close
    ResolvedNote --> Open: Reopen
    ResolvedEntry --> Open: Reopen
    ResolvedWO --> Open: Mở lại lệnh
    Closed --> Open: Reopen
    Open --> [*]: Delete, chưa thử
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Open | Close | Closed | Note tuỳ chọn | Closed Details; ghi chú thành Comment; mất Edit, Resolve; Timeline không ghi | "Close Issue", "Describe why you're closing the issue." | `Chạy` |
| Open | Resolve with Note | Resolved bằng ghi chú | Note bắt buộc, nút khoá khi trống | Resolution Details; Time to Resolve; mất Edit | "Describe what work was performed to resolve the issue.", "Issue #35 was resolved." | `Chạy` |
| Open | Add to Service Entry rồi lưu entry | Resolved bằng entry | Entry đủ Odometer, Completion Date; chưa lưu thì vẫn Open | Resolved Meter Entry; Timeline ghi | "1 Issue will be added", "Issue Resolved by service entry" | `Chạy` |
| Open | Draft Work Order | Giữ Open | AI bật | Banner nền; xem đối tượng Bản nháp AI | "Drafting service for this issue" | `Chạy` |
| Open | Add to Work Order hoặc tick ở form lệnh | Giữ Open, thành đã gắn lệnh | Sự cố chưa ở lệnh nào; lưu lệnh | Khoá ba lối; Timeline "added this issue to a work order" | "Issue already added to a Work Order. Remove it from all Work Orders to add it to another." | `Chạy` |
| Open | Get Service at Shop | Giữ Open | Cần bật Shop Network, không bật | Hộp giới thiệu | "Streamline your outsourced maintenance with Shop Network" | `Xem` |
| Open | Edit, View Record History | Giữ Open | Không có | Đổi hạn thì tính lại Overdue | Không có | `Chạy` |
| Open | Delete | Không rõ | Không có | Chưa thử | Không rõ | `Xem` |
| Open | Tự tính | Overdue | Ngày hiện tại qua Due Date, hoặc đồng hồ lớn hơn Due Odometer; đúng bằng thì không | Hiện ở Issue Status, tab Overdue; không có sự kiện | "Considered overdue after this date", "Considered overdue above this value" | `Chạy` |
| Overdue | Mọi hành động của Open | Như Open | Y hệt Open, vẫn thuộc `state_scope=opened` | Như Open | Như Open | `Chạy` |
| Overdue | Đổi hạn sang tương lai | Open | Tự tính khi lưu | Không có sự kiện, không có nút | Không có | `Chạy` |
| Open, đã gắn lệnh | Add to Service Entry, Add to Work Order, Resolve with Note | Không đổi được | Mục xám có khoá, phải gỡ khỏi lệnh trước | Không có | "Issue already added to a Work Order. Remove it from all Work Orders to add it to another." | `Chạy` |
| Open, đã gắn lệnh | Edit, Draft Work Order, Get Service at Shop | Giữ Open | Mục vẫn dùng được. Close chưa thử | Chưa thử Draft trên sự cố đã gắn | Không có | `Chạy` |
| Open, đã gắn lệnh | Bỏ tick ở form lệnh rồi lưu | Open, tự do | Lệnh chưa Completed | Timeline xoá dòng "added this issue" | "No issues to show." | `Chạy` |
| Open, đã gắn lệnh | Lệnh Completed | Resolved bằng lệnh | Lệnh đủ điều kiện | Xem đối tượng Lệnh | "Issue Resolved by work order" | `Chạy` |
| Resolved bằng ghi chú | Reopen | Open | Không điều kiện, có hộp xác nhận | Mất Resolution Details; Comment giữ | "Are you sure you want to reopen the selected issue(s)?" | `Chạy` |
| Resolved bằng ghi chú | View Record History | Giữ nguyên | Không có | Không có Edit | Không có | `Chạy` |
| Resolved bằng entry | Reopen | Open | Không điều kiện, nút **không** khoá | Entry còn, mất liên kết, "No issues to show"; Timeline vẫn giữ dòng cũ, không ghi mở lại | "Successfully reopened Issue." | `Chạy` |
| Resolved bằng entry | Bỏ tick trong entry | Open | Theo tài liệu hãng | Chưa thử | Không rõ | `Docs` |
| Resolved bằng lệnh | Reopen | Không đổi được | Nút khoá, phải mở lại lệnh | Không có | "Reopen work order #104 to reopen this issue." | `Chạy` |
| Resolved bằng lệnh | Mở lại lệnh | Open | Lệnh về Open hoặc Pending | Mất Resolution Details, xoá dòng "Issue Resolved by work order", giữ "added this issue" | "Changing this completed Work Order to an incomplete Status..." | `Chạy` |
| Closed | Reopen | Open | Không điều kiện, có hộp xác nhận | Closed Details mất, Comment còn; Timeline chỉ có "opened this issue" | "Are you sure you want to reopen the selected issue(s)?" | `Chạy` |
| Closed | View Record History | Giữ nguyên | Không có | Không có Edit, Resolve | Không có | `Chạy` |

**Mở lại đều không để vết**, ở cả ba nguồn. Từ phiếu kiểm tra, lỗi tái diễn sau khi Resolved sinh sự cố mới, không mở lại sự cố cũ (`Chạy` nhóm Nhắc).

## Lệnh sửa

Danh mục có 3 trạng thái mặc định; mỗi trạng thái thuộc loại Incomplete hoặc Completed. Khách thêm được là `Docs`, chưa thử.

```mermaid
stateDiagram-v2
    [*] --> Open: Tạo lệnh
    Open --> Pending: Đổi trạng thái, không hỏi
    Pending --> Open: Đổi trạng thái, không hỏi
    Open --> Completed: Đủ điều kiện
    Pending --> Completed: Đủ điều kiện, không cần qua Open
    Completed --> Open: Xác nhận, xoá Service Entry
    Completed --> Pending: Xác nhận, xoá Service Entry
    Open --> [*]: Delete, chưa thử
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Open | Lưu lệnh có dòng phụ tùng chọn kho | Giữ Open | Không chặn khi vượt tồn | Tồn trừ ngay, sổ nguồn số lệnh | "This will make an inventory adjustment" | `Chạy` |
| Open | Đổi Pending | Pending | Không điều kiện, không hỏi | Không có | "Work Order was successfully updated" | `Chạy` |
| Open | Đổi Completed, thiếu ngày | Giữ Open | Started At trống | Không có | "Please edit and fix the following errors: Started At can't be blank" | `Chạy` |
| Open | Đổi Completed, thiếu đồng hồ | Giữ Open | Require a Meter Reading bật | Không có | "Starting Meter Entry can't be blank (per your account settings)" | `Chạy` |
| Open | Đổi Completed, đủ điều kiện | Completed | Started At, đồng hồ theo cài đặt | Xem dòng Completed | "Work Order was successfully updated" | `Chạy` |
| Open | Edit, Rerun Assessment, Print, Make a Copy, View Record History | Giữ Open | Không có | Sửa dòng ghi bù kho; lệnh đổi sau đánh giá hiện Rerun available | "Rerun available." | `Chạy` |
| Open | Email PDF, Delete | Không rõ | Chưa thử; Delete báo xoá vĩnh viễn | Chưa biết có hoàn kho không | "All data will be lost forever." | `Xem` |
| Open, có contact mẫu trên xe thường | Sửa, đổi trạng thái | Giữ Open, lệnh kẹt | Tạo qua được, về sau luôn lỗi | Không xoá được dòng công ở lần thử | "Contact is a sample, and cannot be used with non sample vehicles" | `Chạy` |
| Pending | Như Open | Open, Completed | Như Open, không phải quay qua Open | Như Open | "Work Order was successfully updated" | `Chạy` |
| Completed | Edit | Không đổi được | Nút khoá | Không có | Không có | `Chạy` |
| Completed | Đổi Open hoặc Pending | Open hoặc Pending | Hộp "Update Status", Confirm | Xoá entry, sự cố về Open; đồng hồ GIỮ; tồn GIỮ; khôi phục archive chạy nền, vài giây trang vẫn Completed | "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items. Are you sure you wish to continue?" | `Chạy` |
| Completed | Run Assessment, Print, View Record History | Giữ Completed | Không có | Không có | Không có | `Chạy` |
| Open, đã từng Completed | Đổi Completed lần nữa | Completed | Dữ liệu cũ còn, không hỏi lại | Entry mới số khác; Resolved Date, Time to Resolve như lần đầu; thêm dòng đồng hồ trùng nguồn entry | "Issue Resolved by work order" | `Chạy` |

Trạng thái lệnh không tác động lên nhắc khi Open; Completed mới tính lại nhắc (`Chạy` nhóm Nhắc, lệnh #101). Mở lại với nhắc: chưa kiểm.

## Service Entry

**Không có trường trạng thái.** Bản ghi chỉ có hai nguồn với quyền khác nhau, và có thể biến mất. Sơ đồ vẽ để thấy vòng đời, các tên dưới đây không xuất hiện trên giao diện.

```mermaid
stateDiagram-v2
    [*] --> Tay: Lưu entry tạo tay hoặc từ sự cố
    [*] --> TuLenh: Lệnh hoàn thành
    Tay --> Tay: Edit
    TuLenh --> DaXoa: Mở lại lệnh
    DaXoa --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Tạo tay, từ sự cố | Edit | Giữ nguyên | Lưu lại không đổi gì vẫn thành công | Không có | Không có | `Chạy` |
| Tạo tay, từ sự cố | Sự cố được Reopen | Giữ nguyên | Không có | Mất liên kết sự cố | "No issues to show" | `Chạy` |
| Tạo tay, từ sự cố | Xoá | Không rõ | Chưa thử; không tự xoá | Chưa biết | Không rõ | Không chạy |
| Từ lệnh | Edit | Không đổi được | Nút khoá | Không có | Không có | `Chạy` |
| Từ lệnh | Run Assessment | Giữ nguyên | Không tự chạy, khác lệnh | Có kết luận | "Run Assessment" | `Chạy` |
| Từ lệnh | Mở lại lệnh | Đã xoá | Xác nhận ở lệnh | URL ra Not Found; hoàn thành lại sinh entry số khác | "the record may have been deleted" | `Chạy` |

## Mã lỗi

```mermaid
stateDiagram-v2
    [*] --> Open: Thiết bị gửi mã
    Open --> Pending: Đã gắn sự cố
    Pending --> Resolved: Sự cố giải quyết
    Open --> Ignored: Bỏ qua
    Open --> Resolved: Giải quyết
    Resolved --> [*]
    Ignored --> [*]
```

Chuyển trạng thái mã lỗi là `Suy` từ các tab và cột Issue trên danh sách mẫu; xe TEST không có thiết bị, không chạy hành động trên dữ liệu Sample.

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Open | Create Issue | Pending | Suy từ cột Issue | Không rõ | "Create Issue" | `Xem`, chuyển là `Suy` |
| Open | Ignore | Ignored | Suy từ tab | Không rõ | "Ignore" | `Xem`, chuyển là `Suy` |
| Open | View Fault Rule | Giữ nguyên | Không có | Không rõ | "View Fault Rule" | `Xem` |
| Pending | Sự cố giải quyết | Resolved | Suy | Không rõ | Không rõ | `Suy` |
| Resolved | Không rõ | Không rõ | Không thao tác | Không rõ | Không rõ | `Xem` |
| Ignored | Không rõ | Không rõ | Không thao tác | Không rõ | Không rõ | `Xem` |

## Bản nháp AI

```mermaid
stateDiagram-v2
    [*] --> Drafting: Chọn Draft Work Order
    Drafting --> Ready: AI xong, có thông báo
    Ready --> Created: Create new Work Order
    Ready --> AddedToOpen: Add to Work Order đang mở, chưa bấm
    Ready --> Discarded: Discard
    Created --> [*]
    AddedToOpen --> [*]
    Discarded --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Drafting | Chờ, rời trang | Ready | Khoảng 40 giây | Banner đổi chữ, chạy nền | "Drafting service for this issue", "Gathering vehicle details", "Reviewing this issue" | `Chạy` |
| Ready | Review draft | Giữ Ready | Không có | Mở hộp; cảnh báo lệnh mở; gom sự cố cùng xe | "Review Work Order draft", "A Work Order is already open for this vehicle" | `Chạy` |
| Ready | Bỏ tick việc | Giữ Ready | Không có | Số đếm đổi, nút "Select all" | "1/2 Service Tasks" | `Chạy` |
| Ready | Create new Work Order | Created | Có ít nhất một việc: `Suy` | Lệnh mới; sự cố được tick vào lệnh; sự cố bỏ tick không vào; phân loại ưu tiên vẫn trống dù hộp hứa | "Created from an AI draft from Issue #46" | `Chạy` |
| Ready | Add to Work Order đang mở | Đã thêm | Xe đang có lệnh mở | Chưa bấm | "Add to Work Order #104" | `Xem` |
| Ready | Discard | Discarded | Không hỏi lại | Mất ngay, không ghi Timeline | "Discard" | `Chạy` |
| Created | Không có | Kết thúc | Không có | Timeline "added this issue to a work order from an AI draft" | "Work Order successfully created" | `Chạy` |
| Discarded | Không có | Kết thúc | Có thể soạn lại: chưa thử | Không có | Không có | `Chạy` |

## Đánh giá AI

Không phải trường trạng thái riêng; là khối trên lệnh, entry.

```mermaid
stateDiagram-v2
    [*] --> ChuaDu: Thiếu đầu việc hoặc chi phí
    ChuaDu --> DangChay: Đủ điều kiện, tự chạy trên lệnh
    DangChay --> CoKetLuan: Xong
    CoKetLuan --> LoiThoi: Lệnh đổi sau đánh giá
    LoiThoi --> DangChay: Rerun Assessment
    CoKetLuan --> DangChay: Rerun Assessment
    CoKetLuan --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Chưa đủ | Thêm đầu việc, chi phí | Đang chạy | Lệnh có đầu việc và tiền | Tự chạy | "Add a service task to run an assessment.", "Add line item costs to run an assessment.", "Add a line item to run an assessment." | `Chạy` |
| Đang chạy | Chờ | Có kết luận | Không có | Đổi chữ tiến độ | "Reviewing this service", "Checking labor rates and times", "Reviewing parts and pricing" | `Chạy` |
| Có kết luận | Rerun Assessment | Đang chạy | Không có | Kết luận Acceptable hoặc Needs Review, số nguồn | "Auto-assessed 3 minutes ago", "Was this helpful?" | `Chạy` |
| Lỗi thời | Rerun Assessment | Đang chạy | Lệnh đổi sau đánh giá | Không có | "Rerun available." | `Chạy` |

## Đầu việc

```mermaid
stateDiagram-v2
    [*] --> Active: Lưu đầu việc
    Active --> Archived: Archive, có xác nhận
    Archived --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Active | Archive | Archived | Hộp xác nhận | Bản ghi liên quan cập nhật nền; không dùng được nữa | "Archiving a record does not remove it from Fleetio, but it will no longer be usable." | `Chạy` |
| Active | Update Service Tasks, Import, Export | Giữ Active | Không có | Chưa thử | Không có | `Xem` |
| Archived | Khôi phục | Không rõ | Chưa thử | Chưa biết | Không rõ | Không chạy |

## Bảo hành

Thấy Status "Active" trên danh sách; khối trên lệnh đếm active, expiring soon, total. Chưa đợi được hết hạn, nên sơ đồ phần sau Active là `Suy`.

```mermaid
stateDiagram-v2
    [*] --> Active: Lưu, tự tính End Date, End Meter
    Active --> ExpiringSoon: Sắp đến hạn, chưa thấy
    ExpiringSoon --> Expired: Hết hạn, chưa thấy
    Expired --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Active | Lệnh có đầu việc khớp mã | Giữ Active | Mã phân loại trùng | Hiện cơ hội trên lệnh | "Warranty Opportunities (1)", "View Active Coverage" | `Chạy` |
| Expiring soon | Không rõ | Không rõ | Ngưỡng chưa biết | Đếm ở khối | "expiring soon" | `Xem` nhãn |
| Expired | Không rõ | Không rõ | Chưa đợi được | Không rõ | Không rõ | `Suy` |

## Đối tượng không có trạng thái thật

- **Dòng việc:** tình trạng từng dòng và luật bắt buộc xong hết là `Docs`, chưa kiểm vì không đổi Settings.
- **Dòng phụ tùng, tồn:** dòng không có trạng thái, chỉ có sửa, xoá. Tồn theo kho có Low Stock, Out of Stock: xem [[docs/_research/fleetio/srs/fleetio-parts-purchasing-fuel-states.md|Kho, mua]].
- **Dòng đồng hồ:** không có trạng thái, không bị đảo khi mở lại lệnh.
