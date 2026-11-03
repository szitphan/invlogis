---
type: research
feature: fleetio-parts-purchasing-fuel
updated: 2026-11-03
---

# Phụ tùng, mua hàng, nhiên liệu — States

Nhãn mức: `Chạy` đã thao tác · `Xem` thấy, không thao tác · `Docs` tài liệu hãng · `Suy` suy ra. "Chưa ghi" là nhật ký chạy không ghi câu chữ hoặc kết quả cho ô đó. Mã case dẫn về SRS Mục 6A.

## 1. Đơn mua

```mermaid
stateDiagram-v2
    [*] --> Draft: Save as Draft
    [*] --> Approved: Save and Approve
    Draft --> PendingApproval: Submit for Approval, theo tài liệu
    Draft --> Approved: Approve
    Approved --> Draft: Save as Draft
    PendingApproval --> Approved: Duyệt, theo tài liệu
    PendingApproval --> Rejected: Từ chối, theo tài liệu
    Approved --> Purchased: Mark as Purchased
    Purchased --> Approved: Unmark as Purchased
    Purchased --> ReceivedPartial: Nhận một phần
    Purchased --> ReceivedFull: Nhận đủ
    ReceivedPartial --> ReceivedFull: Nhận nốt
    ReceivedFull --> ReceivedPartial: Make Adjustment giảm
    ReceivedPartial --> Closed: Close khi nhận thiếu
    ReceivedFull --> Closed: Close
    ReceivedFull --> ReceivedFull: Sửa tăng số đặt, vẫn Full
    Closed --> Closed: Make Adjustment giảm, vẫn Closed
    Rejected --> [*]: Gửi lại chưa biết
    Closed --> [*]
```

Sơ đồ không vẽ Delete và Make a Copy vì có ở nhiều trạng thái, xem cuối bảng. Không có trạng thái hay nút huỷ riêng; thoát đơn chỉ có Close (từ Partial, Full) hoặc Delete. Closed không có nút mở lại, nhưng Make Adjustment vẫn đổi số nhận và tồn (D18). Trạng thái cố định, trang cấu hình không có nút thêm (`Xem`).

Pending PO Qty theo trạng thái, đo trên PO #4, `Chạy`:

| Bước trên PO #4 | Trạng thái sau bước | Pending PT-A | Current Qty PT-A | Case |
|---|---|---|---|---|
| Copy, lưu nháp, đặt 12 | Draft | 0 | 121 | D22 |
| Duyệt | Approved | 0 | 121 | D23 |
| Mark as Purchased | Purchased | 12 | 121 | D24 |
| Sửa số đặt thành 15 | Purchased | 15 | 121 | D25 |
| Unmark as Purchased | Approved | 15, không giảm | Chưa ghi | D27 |
| Save as Draft | Draft | 15, không giảm | Chưa ghi | D28 |
| Approve, Mark as Purchased lại | Purchased | 15, không nhân đôi | Chưa ghi | D29 |

PO #4 chưa Edit trước Purchased nên Draft, Approved tính 0; đơn đã qua Purchased rồi lùi lại thì giữ số đã vào. Cách tính sau khi lùi là `Suy`, chỉ đo ở PO #4 (OQ-25).

Đơn Draft đã Edit, đo trên PO #5, chưa từng Approve, `Chạy`:

| Thời điểm | Pending KHO-01 | Pending KHO-02 | Case |
|---|---|---|---|
| Trước khi có PO #5 | 15, của PO #4 Purchased | 0 | D40 |
| PO #5 Draft đã Edit, số 15, tải lại trang | 15 | 15 | D40 |
| PO #5 Draft Edit, số 7 | 15 | 7 | D41 |

Kết luận lượt 3 "chỉ tính từ Purchased" chỉ đúng với đơn chưa Edit. Thao tác nào kích hoạt chưa tách riêng, Approved đã Edit chưa đo (OQ-13). Nhật ký suy bước lưu Edit ghi Pending không xét trạng thái, nhưng Edit tăng số đặt ở Full không cộng Pending (D37), nên suy luận này chưa đứng vững.

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Mới | Save as Draft | Draft | Đã chọn nhà cung cấp, kho; 0 dòng vẫn lưu được | Có số đơn tự tăng; chưa Edit thì không tính vào Pending PO Qty (D22) | "Purchase Order was successfully created" (D21) | `Chạy` |
| Mới | Save & Approve | Approved | Có quyền duyệt; có dòng | Lưu và ghi Approved By | Chưa ghi | `Chạy` |
| Mới | Lưu khi trùng dòng | Không tạo | Hai dòng cùng phụ tùng (D4) | Chặn | "Part TEST-KHO-PT-A is duplicated", "Purchase Order could not be created" | `Chạy` |
| Draft | Sửa, lưu | Draft | Nhà cung cấp, kho mở; có Add Line Item, nút xoá dòng, "Save as Draft", "Save & Approve" (D30). Đổi kho, nhà cung cấp không xoá dòng, không hỏi lại; xoá dòng không có hộp xác nhận (D38) | Không đổi trạng thái; số đặt vào Pending của kho trên đơn, theo số mới mỗi lần lưu (D40, D41, E-032) | "Purchase Order was successfully updated" | `Chạy` |
| Draft | Approve | Approved | Khoá khi 0 dòng; dòng số lượng 0 vẫn duyệt được (D5); duyệt đơn của mình được, một cú bấm, không hộp xác nhận (D17) | Ghi Approved By; đơn chưa Edit thì Pending PO Qty vẫn 0 (D23); lượt đầu ghi 12 ở PO #2, đơn có lần sửa trước đó (`Suy`, OQ-13) | "Purchase Order #2 approved" | `Chạy` |
| Draft | Save & Approve | Approved | Có quyền duyệt | Lưu sửa và duyệt | Chưa ghi | `Chạy` |
| Draft | Submit for Approval | Pending Approval | Người không có quyền duyệt; người có quyền không thấy nút. Lượt 3 không chạy được (D32) | Chờ người duyệt | Không thấy nút | `Docs` |
| Pending Approval | Duyệt | Approved | Người có quyền | Ghi người duyệt | Có tab lọc, chưa ghi câu | `Docs` |
| Pending Approval | Từ chối | Rejected | Người có quyền | Chưa biết | Có tab lọc, chưa ghi câu | `Docs` |
| Rejected | Gửi lại | Chưa biết | Tài khoản một người không tới được, OQ-8 | Chưa biết | Có tab lọc, chưa ghi câu | `Docs` |
| Approved | Mark as Purchased | Purchased | Một cú bấm | Đơn chưa Edit: Pending PO Qty bắt đầu tính, 0 thành 12 (D24) | "marked as purchased" | `Chạy` |
| Approved | Edit | Approved | Đủ trường, thêm bớt dòng được; có "Save as Draft", "Save & Approve" | Lưu không đổi trạng thái | Chưa ghi | `Chạy` |
| Approved | Save as Draft | Draft | Chỉ trong form Edit, menu không có mục này (D33) | Mất dòng Approved By; Pending không giảm nếu đã qua Purchased (D28) | "Purchase Order was successfully updated" | `Chạy` |
| Approved | Save & Approve | Approved | Trong form Edit | Lưu, giữ trạng thái | Chưa ghi | `Chạy` |
| Purchased | Receive một phần | Received, Partial | Chọn nơi đến | Tồn tăng theo số nhận (D8) | "was successfully received" | `Chạy` |
| Purchased | Receive đủ | Received, Full | Mọi dòng đạt số đặt; nhận vào lệnh mới rồi huỷ form cũng vậy (D15) | Tồn tăng, hàng ở lại kho nếu huỷ form | "Your received parts will remain in inventory even if you don't save this work order." | `Chạy` |
| Purchased | Unmark as Purchased | Approved | Một cú bấm, không hỏi | Pending PO Qty không giảm: PT-A vẫn 15, PT-B vẫn 5 sau khi tải lại (D27, E-026); Purchase Date, Purchased By vẫn còn (D35) | "Purchase Order #4 unmarked as purchased" | `Chạy` |
| Purchased | Edit | Purchased | Khoá nhà cung cấp, kho; không có Add Line Item, nút xoá dòng; sửa được Label, số, giá, Description, Discount, Shipping, Tax (D26) | Không cảnh báo đã gửi nhà cung cấp; số đặt 12 thành 15 thì Pending thành 15 (D25) | Chưa ghi | `Chạy` |
| Received, Partial | Receive tiếp, còn thiếu | Received, Partial | Lần sau gợi ý số còn lại (D8); vượt ở một dòng mà dòng khác 0 vẫn Partial (D10) | Tồn tăng từng lần; nhận vượt không chặn (D9) | "was successfully received" | `Chạy` |
| Received, Partial | Receive đủ | Received, Full | Mọi dòng đạt số đặt | Ghi Received in Full By | "was successfully received" | `Chạy` |
| Received, Partial | Receive gõ số âm | Không lùi | Gõ -5 (D11) | Thành nhận +5, mất dấu âm, không báo | "was successfully received" | `Chạy` |
| Received, Partial | Close | Closed | Hộp xác nhận; đóng được khi còn thiếu, không ghi lý do (D13) | Ghi Closed By; dòng PT-B giữ 0 trên 5 | "Are you sure you want to close the selected purchase order?", "was successfully closed" | `Chạy` |
| Received, Partial | Edit | Received, Partial | Khoá nhà cung cấp, kho, không thêm bớt dòng; sửa số và giá được | Tổng tính lại | "was successfully updated" | `Chạy` |
| Received, Partial | Make Adjustment | Không có | Không có nút ở trạng thái này | Không có | Không có | `Chạy` |
| Received, Full | Close | Closed | Tự đóng tắt nên cần Close tay | Ghi Closed By | "was successfully closed" | `Chạy` |
| Received, Full | Make Adjustment giảm | Received, Partial | Số âm tới số đã nhận; -6 trên 5 cắt còn -5, không báo (D12) | Sổ -5, tồn 2 thành -3; "Received in Full By" vẫn còn | "Negative values are allowed up to the quantity received on this order.", "was successfully adjusted" | `Chạy` |
| Received, Full | Edit, tăng số đặt | Received, Full | Khoá nhà cung cấp, kho; không thêm bớt dòng; ô số, giá mở; nút "Save Purchase Order" (D31). Đặt 15, nhận 12 (D36) | Trạng thái không tính lại; tổng tính lại; menu không có Receive dù thiếu 3; không cộng Pending, không đổi Unit Cost phụ tùng (D37, E-033) | "Purchase Order was successfully updated" | `Chạy` |
| Closed | Edit | Closed | Vẫn đổi được đơn giá dưới Static Pricing | Tổng 1.429.400 thành 1.312.760 | "was successfully updated" | `Chạy` |
| Closed | Make Adjustment giảm | Closed | Tick dòng, nhập số âm tới số đã nhận; nút mờ tới khi tick; không mở lại, không hỏi lý do (D18) | Qty Received 110 xuống 109; sổ "Received: -1.0"; tồn giảm (E-027) | "Check the box to make an Adjustment. Negative values are allowed up to the quantity received on this order.", "Purchase Order #2 was successfully adjusted" | `Chạy` |
| Closed | Mở lại | Không có | Không có nút | Không có | Không có | `Chạy` |
| Draft, Approved, Purchased, Received, Closed | Make a Copy | Form đơn mới | Mở form điền sẵn (D16, D21) | Giữ giá đơn cũ, số đơn tăng; không chép số đã nhận; lưu ra Draft | "Purchase Order was successfully created" | `Chạy` từ Closed; thấy trong menu Approved, Purchased (D33); các trạng thái khác `Xem` |
| Draft, Approved, Purchased, Received, Closed | Delete | Chưa biết | Không bấm, OQ-10 | Chưa biết | Chưa ghi | `Xem` |
| Draft | Print, View Record History | Draft | Có nút | Không đổi trạng thái | Chưa ghi | `Xem` |
| Approved | Print | Approved | PO #4 sau Unmark (D34, D35) | Tab mới, `purchase_order_4.pdf`; vẫn in Purchase Date, Purchased By; tiền kiểu US | "Preparing your PDF..." | `Chạy` |
| Approved, Purchased | Print, View Record History | Không đổi | Có trong menu (D33) | Không đổi trạng thái | Chưa ghi | `Xem`, trừ Print ở dòng trên |
| Closed | View Record History | Closed | PO #2 (D19) | Hộp liệt kê chuyển trạng thái, đổi tiền; phần ảnh đọc được không có dòng số nhận (D20) | "State changed from Received Partial to Closed" | `Chạy` |

## 2. Tồn theo từng kho

Tồn là nhãn tính từ số lượng, không phải trạng thái lưu; mỗi kho một nhãn. Ngưỡng: tồn từ 0 trở xuống là Out of Stock; trên 0 và từ điểm đặt lại trở xuống là Low Stock; còn lại không nhãn. Điểm đặt lại 0 thì không có Low Stock: tồn 0 là Out of Stock, tồn 0,5 không nhãn (S5, S6). Danh sách Parts tô đỏ Total Quantity khi một kho hết, dù tổng còn nhiều (S9).

```mermaid
stateDiagram-v2
    [*] --> KhongNhan: Bật tại kho, nhập tồn đầu
    KhongNhan --> LowStock: Tồn xuống tới điểm đặt lại
    LowStock --> KhongNhan: Tồn vượt điểm đặt lại
    LowStock --> OutOfStock: Tồn từ 0 trở xuống
    KhongNhan --> OutOfStock: Giảm hoặc xuất quá tồn
    OutOfStock --> LowStock: Tăng, chưa vượt điểm đặt lại
    OutOfStock --> KhongNhan: Tăng, vượt điểm đặt lại
    KhongNhan --> [*]: Tắt tại kho khi không vướng đơn, lệnh
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Không nhãn | Chỉnh tăng | Không nhãn | +0,5 trên 6, điểm 5 (K5); lý do bắt buộc (K6) | Tồn 6,5, sổ Manual | Chưa ghi | `Chạy` |
| Không nhãn | Chỉnh giảm, còn trên 0 | Low Stock | Tồn từ điểm trở xuống | Số màu cam, đủ nút | "Low Stock" | `Chạy` |
| Không nhãn | Chỉnh giảm quá tồn | Out of Stock | 10, chỉnh -20, lý do Lost (K3) | Tồn -10, không cảnh báo | "Out of Stock" | `Chạy` |
| Không nhãn | Chuyển quá tồn | Out of Stock ở kho nguồn | Có 6,5, chuyển 100, Save vẫn mở (K7) | Chỉ chuyển 6,5, sổ -6,5 và +6,5, không báo đã cắt | "Parts transfer was successful." | `Chạy` |
| Không nhãn | Xuất cho lệnh, vượt tồn | Out of Stock | PT-A 20, kho 9,5 (K12) | Trừ ngay khi lưu, tồn -10,5, không cảnh báo | "This will make an inventory adjustment" | `Chạy` |
| Không nhãn | Xuất cho lệnh, trong tồn | Theo số còn lại | PT-B 5 cái, WO Open (K10) | -5 ngay lúc lưu | "This will make an inventory adjustment" | `Chạy` |
| Không nhãn | Đặt mua | Không đổi | Nút trên thẻ tồn | Tạo đơn mua cho phụ tùng; chưa ghi lần bấm | Chưa ghi | `Xem` |
| Không nhãn | Menu Edit | Không nhãn | Điểm đặt lại lưu được 0 dù tài liệu nói phải lớn hơn 0, tồn 9,5 (S4, S7) | Không nhãn | "Part was successfully updated" | `Chạy` |
| Không nhãn | Sửa ở Bulk về 0, điểm đặt lại 0 | Out of Stock | 9,5 thành 0 (S5); không hỏi lý do (S8) | Ô đếm Out of Stock 1, Low Stock 0; sổ "Adjustment: 9.5 → 0.0", chứng từ Bulk Update | "Out of Stock" | `Chạy` |
| Không nhãn | Menu View History | Không đổi | Nút trong menu | Mở sổ kho | Chưa ghi | `Xem` |
| Không nhãn | Tắt tại kho | Tắt | Không vướng đơn ở mọi trạng thái, lệnh chưa xong | Chưa thử nhánh thành công | "A location cannot be disabled if the part is used on any incomplete Work Orders, or on Purchase Orders in any status." | `Xem` |
| Không nhãn | Tắt tại kho ở Bulk | Không tắt | Có đơn tại kho (K20) | Giữ nguyên | "This part can't be deactivated because it's used in one or more purchase orders at this location." | `Chạy` |
| Low Stock | Tăng vượt điểm | Không nhãn | Tồn vượt điểm đặt lại | Bỏ nhãn | Không có nhãn | `Chạy` |
| Low Stock | Giảm tới 0 hoặc quá tồn | Out of Stock | Make Adjustment: tồn 2 thành -3 (D12) | Sổ ghi; không cảnh báo | "Out of Stock" | `Chạy` |
| Low Stock | Chuyển, chỉnh, đặt mua | Theo số còn lại | Đủ nút | Như không nhãn | "Low Stock" | `Chạy` |
| Out of Stock | Chuyển kho | Không đổi | Tồn từ 0 trở xuống (K8) | Nút khoá | "Out of Stock" | `Chạy` |
| Out of Stock | Chỉnh bằng số mới | Out of Stock | Từ -10 gõ New Quantity 0, Adjust Quantity tự thành 10 (K4) | Tồn 0 | "Out of Stock" | `Chạy` |
| Out of Stock | Tăng, chưa vượt điểm | Low Stock | 0 cộng 5, điểm 5 | Số màu cam | "Low Stock" | `Chạy` |
| Out of Stock | Tăng, vượt điểm | Không nhãn | Bulk -1 thành 8, sổ Bulk Update +9, không hỏi lý do (K19); xoá dòng lệnh +20, về 9,5 (K16) | Bỏ nhãn | "All changes saved" ở Bulk | `Chạy` |
| Out of Stock | Nhận hàng | Theo số sau | -2 nhận 6 về 4 (C1) | Sổ Purchase Order | "was successfully received" | `Chạy` |
| Out of Stock | Sửa ở Bulk lên 0,5, điểm đặt lại 0 | Không nhãn | 0 thành 0,5 (S6) | Không qua Low Stock | Không có nhãn | `Chạy` |
| Mọi nhãn | Make Adjustment từ Closed | Theo số sau | PT-A -1 ở PO #2 (D18) | Tồn KHO-01 còn 121, sổ "Received: -1.0" | "was successfully adjusted" | `Chạy` |
| Mọi nhãn | Tồn xuống ngưỡng, gửi email | Chưa biết | Không gửi email theo ràng buộc (S10) | Theo tài liệu gửi email | Chưa ghi | `Docs` |

## 3. Phụ tùng tại kho

Bật, tắt theo từng cặp phụ tùng, kho; xem cột Active? ở Bulk.

```mermaid
stateDiagram-v2
    [*] --> ChuaBat: Có phụ tùng và kho
    ChuaBat --> DangBat: Bật, nhập tồn đầu
    DangBat --> DangBat: Tắt bị chặn khi có đơn
    DangBat --> DaTat: Tắt khi không vướng
    DaTat --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Chưa bật | Bật qua Manage | Đang bật | Có kho | Hiện thẻ tồn, sổ loại Initial | Chưa ghi | `Chạy` |
| Chưa bật | Chọn trên đơn mua | Không chọn được | Kho của đơn chưa bật phụ tùng (D2) | Dòng xám, có khoá | Chưa ghi | `Chạy` |
| Đang bật | Tắt ở Bulk | Đang bật | Có đơn tại kho (K20) | Gạt không có tác dụng | "This part can't be deactivated because it's used in one or more purchase orders at this location." | `Chạy` |
| Đang bật | Tắt khi không vướng | Đã tắt | Không có đơn, lệnh chưa xong | Chưa thử | Chưa ghi | `Xem` |
| Đã tắt | Bật lại | Chưa biết | Chưa thử | Chưa biết | Chưa ghi | Không chạy |

Mức cả phụ tùng: menu có "Archive", mờ với PT-A, lý do chưa rõ (K26, OQ-23, `Xem`). Archive, Restore phụ tùng chưa chạy nên không vẽ.

## 4. Dòng phụ tùng trên lệnh

Dòng không có trường trạng thái riêng; hành vi đi theo trạng thái lệnh. Trạng thái lệnh đầy đủ ở nhóm Sửa chữa, ở đây chỉ ghi tác động lên kho.

```mermaid
stateDiagram-v2
    [*] --> TrenLenhMo: Lưu dòng, trừ kho
    TrenLenhMo --> TrenLenhMo: Sửa số, sổ ghi bù
    TrenLenhMo --> TrenLenhXong: Lệnh sang Completed
    TrenLenhXong --> TrenLenhMo: Lệnh mở lại
    TrenLenhMo --> [*]: Xoá dòng, sổ cộng lại
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Mới | Thêm từ kho | Trên lệnh Open | Chọn kho, số lượng | Trừ ngay, sổ Work Order (K10); không chặn vượt tồn (K12) | "This will make an inventory adjustment" | `Chạy` |
| Mới | Thêm với None | Trên lệnh Open | "None (No Inventory Adjustment)" (K13) | Không đổi tồn | Chưa ghi | `Chạy` |
| Mới | Nhận từ đơn | Trên lệnh Open | Nhận vào lệnh có sẵn (D14) | Sổ +5, rồi -5 khi lưu lệnh; ghi chú "From PO #2" | "These parts will be received to your inventory before being added to the selected work order." | `Chạy` |
| Trên lệnh Open | Sửa số lượng | Trên lệnh Open | 5 thành 3 (K11) | Sổ +2, loại Work Order #102 | Chưa ghi | `Chạy` |
| Trên lệnh Open | Xoá dòng | Hết dòng | Sau hộp xác nhận (K16) | Sổ +20, tồn về 9,5 | "Are you sure you want to permanently delete this line item?" | `Chạy` |
| Trên lệnh Open | Đổi vị trí sang None | Chưa biết | Chưa thử, OQ-12 | Chưa biết | Chưa ghi | Không chạy |
| Trên lệnh Open | Lệnh sang Completed | Trên lệnh Completed | Có Started At, Start Odometer theo cài đặt (K14) | Sổ không có dòng mới; sinh Service Entry; Edit khoá | "Please edit and fix the following errors: Started At can't be blank", "Start Odometer can't be blank (per your account settings)" | `Chạy` |
| Trên lệnh Completed | Lệnh mở lại | Trên lệnh Open | Đổi trạng thái (K15) | Sổ không đổi; liên kết Service Entry biến mất | "Changing this completed Work Order to an incomplete Status will automatically restore any archived parts, part locations, and contacts associated with line items." | `Chạy` |
| Trên lệnh Open | Xoá cả lệnh | Chưa biết | Đã huỷ ở hộp xác nhận (K21), OQ-9 | Chưa biết có hoàn kho không | "All data will be lost forever." | Không chạy |

## 5. Phiếu dầu

Phiếu dầu không có vòng đời trạng thái: không có Draft, duyệt hay đóng. Khác biệt nằm ở cờ trên phiếu và cảnh báo. Sơ đồ chỉ vẽ cảnh báo dung tích vì đây là thứ duy nhất đổi theo sự kiện.

```mermaid
stateDiagram-v2
    [*] --> KhongCanhBao: Số lít không vượt hoặc chưa khai dung tích
    [*] --> CoCanhBao: Số lít lớn hơn dung tích
    CoCanhBao --> CoCanhBao: Sửa số lít nhỏ lại, không gỡ
    KhongCanhBao --> [*]
    CoCanhBao --> [*]
```

| Trạng thái | Hành động | Sang | Điều kiện | Hiệu ứng | Câu chữ | Mức |
|---|---|---|---|---|---|---|
| Phiếu đầu | Lưu | Phiếu thường | Chưa có phiếu trước (F1) | Tổng tiền; không tiêu hao | Usage "N/A" | `Chạy` |
| Phiếu thường | Lưu | Phiếu thường | Có phiếu trước (F2) | Tiêu hao theo mpg dù xe km, lít | "mpg (US)" | `Chạy` |
| Cờ Partial | Lưu | Phiếu Partial | Đổ không đầy (F3) | Không tiêu hao; số lít cộng sang phiếu đầy kế tiếp (F4) | Chưa ghi | `Chạy` |
| Cờ Reset usage | Lưu | Phiếu Reset | Bỏ lần ghi (F5) | Không usage; phiếu sau Usage "N/A" nhưng vẫn tính tiêu hao (F6) | Usage "N/A" | `Chạy` |
| Cờ Personal | Lưu | Phiếu Personal | Dùng riêng (F7) | Tính tiêu hao bình thường, vẫn vào Cost of Ownership | Chưa ghi | `Chạy` |
| Cờ Void | Lưu, trống số | Không lưu | Tick Void, trống số (F10) | Chặn | "can't be blank" | `Chạy` |
| Cờ Void | Lưu, có số | Phiếu Void | Ghi 50.000 (F10) | Số gạch ngang, đồng hồ xe không đổi, không Usage; vẫn vào chi phí xe, vẫn cộng Total Volume, Total Fuel Cost (F22, E-028). Void không phải huỷ phiếu | Chưa ghi | `Chạy` |
| Không cảnh báo | Lưu số lít bằng dung tích | Không cảnh báo | 60 lít, bình 60 (F13) | Không cảnh báo | Không có | `Chạy` |
| Không cảnh báo | Lưu khi chưa khai dung tích | Không cảnh báo | 50 lít (F1b) | Không kiểm | Không có | `Chạy` |
| Có cảnh báo | Lưu số lít lớn hơn dung tích | Có cảnh báo | 100 lít (F9), 60,5 lít (F14), bình 60 | Icon Alerts, Capacity Exception Volume | "100 liters" | `Chạy` |
| Có cảnh báo | Sửa số lít nhỏ lại | Có cảnh báo | 100 thành 50 (F9b) | Cảnh báo không mất, cột vẫn 100; lọc Fuel Capacity Alert vẫn ra phiếu 50 lít (F19) | "100 liters" | `Chạy` |
| Mọi phiếu | Vendor Location Alert | Chưa biết | Cần định vị và thẻ (F-VLA, F23), OQ-14 | Theo tài liệu gắn cảnh báo; chỉ thấy tên loại ở bộ lọc | Location Exception Distance | `Docs` |
| Mọi phiếu | Missing GPS Location Alert | Chưa biết | Chỉ thấy tên ở bộ lọc (F18), OQ-26 | Chưa biết | "Missing GPS Location Alert" | `Xem` |
| Mọi phiếu | Lưu, có chọn nhà cung cấp | Không đổi cờ | Form không có ô vị trí (F25) | Tạo dòng "Fuel Entry" trong Location History, xe lên Fleet Map, form không báo | Không có | `Chạy` |

## 6. Nhà cung cấp

Nhà cung cấp không có vòng đời trạng thái đã chạy nên không vẽ sơ đồ. Phân loại Parts, Fuel, Service, Vehicle quyết định nơi được chọn (N2), không phải trạng thái. Tab Archived, cột Archived At có trên danh sách (N9, `Xem`), lưu trữ và khôi phục chưa thử. "Network Status: Invite" thấy, không bấm vì mời người ngoài (N11); giá trị khác của trường này chưa biết (OQ-15). Rating là số, hiện "Rating not available" ở cả 20 nhà cung cấp, không phải trạng thái (N10, N13, N14). Sạc ngoài phạm vi theo yêu cầu user.
