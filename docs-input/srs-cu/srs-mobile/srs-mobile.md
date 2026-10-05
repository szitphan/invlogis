# Tài liệu SRS - ERP Delta 3.0 (Mobile)

> Nguồn: [`ndlxd-export.pdf`](source/srs-mobile.pdf) (PDF) · Nhận: 2026-10-05 · Chuyển sang Markdown bằng `/intake`.
> Tên ứng dụng: thống nhất gọi **Delta Super App** (chốt 2026-10-05). Bản gốc còn gọi "ứng dụng Lái xe Delta" / "app Lái xe" ở 46 chỗ — giữ nguyên chữ gốc bên dưới.

<!-- Trang 1 -->

## Mục lục

- [v1.0] Quy tắc chung xử lý giao diện (Common rules)
- [v2.0] Quy tắc chung xử lý giao diện trên Application (Application common rules & shared components)
- UC00.01.01 - Xem trang chủ - Tài khoản nội bộ
- UC00.01.03 - Xem trang chủ - Tài khoản cây dầu
- UC00.01.02 - Xem thanh tiến trình liên quy trình
- Epic 01 - Quản lý tài khoản
   - UC01.01.01 - Đăng nhập
   - UC01.01.02 - Quên mật khẩu
   - UC01.01.03 - Đăng xuất
   - UC01.01.04 - Đổi mật khẩu
   - UC01.01.05 - Tạo mật khẩu mới
   - UC01.01.06 - Xem thông tin cá nhân - Tài khoản nội bộ
   - UC01.01.07 - Xem thông tin tài khoản - Tài khoản cây dầu
- Epic 02 - Đơn mua dịch vụ sửa chữa ngoài
   - 02 - Thông báo & Lịch sử hoạt động
   - 02 - Lưu đồ trạng thái cho đơn mua HHDV
   - UC02.01.01 - Xem danh sách đơn mua DVSC ngoài
   - UC02.01.02 - Xem thông tin chi tiết đơn mua dịch vụ ngoài
   - UC02.01.03 - Nghiệm thu/Từ chối nghiệm thu dịch vụ sửa chữa ngoài
- Epic 03 - Lệnh sửa chữa
   - 03 - Thông báo & Lịch sử hoạt động
   - 03 - Lưu đồ trạng thái cho lệnh sửa chữa
   - UC03.01.01 - Xem danh sách lệnh sửa chữa
   - UC03.01.02 - Xem thông tin chi tiết lệnh sửa chữa
   - UC03.01.03 - Nghiệm thu/Từ chối nghiệm thu lệnh sửa chữa nội bộ
- Epic 04 - Báo cáo sự cố & Thanh toán chi phí lái xe
   - 04 - Thông báo & Lịch sử hoạt động
   - 04 - Lưu đồ trạng thái cho báo cáo sự cố
   - UC04.01.01 - Xem danh sách báo cáo sự cố
   - UC04.01.02 - Xem chi tiết báo cáo sự cố
   - UC04.01.03 - Tạo báo cáo sự cố
   - UC04.01.04 - Thu hồi báo cáo sự cố
- Epic 05 - Lịch nhắc
   - UC05.01.01 - Xem lịch nhắc
- Epic 06 - Phiếu cấp dầu
   - 06.00 - Lưu đồ trạng thái của phiếu cấp dầu
   - 06.00 - Thông báo & Lịch sử hoạt động
   - UC06.00.01 - Xem danh sách phiếu cấp dầu
   - UC06.00.02 - Xem chi tiết phiếu cấp dầu
   - UC06.00.03 - Tạo mới phiếu dGas1 (Cấp dầu quản lý)
   - UC06.00.04 - Tạo mới phiếu dGas2 (Cấp dầu xưởng)
   - UC06.00.05 - Tạo mới phiếu dGas3 (Cấp dầu vận tải)
   - UC06.00.06 - Tạo mới phiếu dGas4 (Đổ đầy bình)
   - UC06.00.07 - Tạo mới phiếu dGas5 (Chốt dầu)
   - UC06.00.08 - Tạo mới phiếu cấp bù dầu
   - UC06.00.09 - Phê duyệt/Từ chối phiếu cấp dầu (tất cả vòng)
   - UC06.00.10 - Nhận mã Igas & bơm dầu - Cây nội bộ
   - UC06.00.11 - Ghi nhận bơm dầu - Cây mua ngoài & Mua hoá đơn lẻ
   - UC06.00.12 - Xuất hoá đơn - Cây mua ngoài & Mua hoá đơn lẻ
   - UC06.00.13 - Chốt phiếu - Cây mua ngoài

<!-- Trang 2 -->

<!-- Trang 3 -->

![](images/ndlxd-export.pdf-0003-00.png)

Tài liệu SRS - ERP Delta 3.0 (Mobile)

![](images/ndlxd-export.pdf-0003-02.png)

<!-- Trang 4 -->

|1|||||
|---|---|---|---|---|
|||Loại control|Item|Ràng buộc trên Mobile|
||1|Button|Validate dữ liệu|Validate khi người dùng nhấn nút. Hiển thị lỗi bằng toast|
|||||hoặc popup message (ngay dưới input) tùy theo context.|
||2|Textbox|Validate dữ liệu|Validate khi người dùng rời khỏi input field (blur) hoặc sau<br>khi nhấn Submit. Lỗi hiển thị ngay dưới field.|
||3||Max length|Không cho nhập quá max length.<br>Nếu dán (paste), hệ thống tự động cắt theo max length.<br>Short textbox: ≤255 ký tự<br>Long textbox: ≤4000 ký tự|
||4||Bắt buộc nhập<br>(Required)|Label có dấu * đỏ hoặc placeholder có dấu hiệu bắt<br>buộc.<br>Nếu bỏ trống, hiển thị lỗi: "Vui lòng nhập thông tin này!"<br>ngay dưới input.|
||5||Ràng buộc<br>format dữ liệu|Áp dụng theo quy định SRS hoặc mặc định từng loại dữ<br>liệu: số, tiền, thời gian, email, v.v.|
||6|Combobox|Nhập dữ liệu|Hỗ trợ single/multi select tùy loại.<br>Có chức năng search với dữ liệu từ API.<br>Hỗ trợ input + gợi ý gần đúng.|
||7|Format ngày<br>tháng|Kiểu nhập liệu|Có thể nhập hoặc chọn từ date picker (dùng native<br>date/time picker).|
||8||Format hiển thị<br>ngày|Không có giờ: dd/mm/yyyy<br>Có giờ: dd/mm/yyyy hh:mm|
||9|Format số tiền|Đơn vị tiền tệ|Combobox chọn đơn vị tiền tệ.<br>Mặc định là VND.<br>Danh sách đơn vị từ DB.|
||1||ề|ố<br>ề<br>ế|
||1<br>0||Format nhập tiền|Nhập số tiền + đơn vị + tỉ giá (nếu không phải VND).|

## [v1.0] Quy tắc chung xử lý giao diện (Common rules)

### 1. Các thành phần chung

![Trang 4 — ảnh xem trước để đối chiếu hình vẽ](images/page-04.png)

<!-- Trang 5 -->

Tự động định dạng hàng nghìn bằng dấu phẩy.

Ví dụ: 50 USD → 50 USD 25,000 VND

|1<br>1|Format số|Format nhập|Chỉ cho phép nhập số và dấu . (dấu thập phân).<br>Tự động phân cách hàng nghìn bằng dấu phẩy.|
|---|---|---|---|
|1<br>2||Format hiển thị<br>số|Hàng nghìn: dấu ,<br>Thập phân: dấu .|
|1<br>3|Email|Format|Kiểm tra đúng format (phải có @ ).<br>Lỗi: “Email không đúng định dạng.”|
|1<br>4|SĐT|Format nhập|Chỉ cho phép số.<br>Bắt đầu bằng 0 hoặc 84 , tối đa 11 ký tự.<br>Format: 0xxx xxx xxx hoặc 84 xxx xxx xxx<br>Sai: “SĐT không đúng định dạng.”|
|1<br>5|Popup<br>Message|Thông báo|Thành công: Popup màu xanh.<br>Thất bại: Popup màu đỏ.<br>Cảnh báo: Màu cam/vàng.<br>Nội dung theo đặc tả.|
|1<br>6|Thanh tìm<br>kiếm|Tìm kiếm|Nhập và nhấn "Tìm" hoặc "Enter" trên bàn phím.<br>Cho phép tìm gần đúng trong toàn bộ bảng.|
|1<br>7|Tên màn hình|Vị trí|Tên hiển thị ở đầu màn hình, cùng với icon quay lại hoặc<br>icon menu tùy theo thiết kế.|

### 2. Thông báo

![Trang 5 — ảnh xem trước để đối chiếu hình vẽ](images/page-05.png)

<!-- Trang 6 -->

![](images/ndlxd-export.pdf-0006-00.png)

Nhấn vào icon quả chuông ở màn Trang chủ hoặc tab Thông báo trên Navigation bar để mở

ra danh sách thông báo.

Có 2 trường hợp:

Không có thông báo mới: Không hiển thị badge

|Có ≥ 1 thông báo chưa đọc: Hiển thị|badge đỏ|với số lượng thông báo chưa đọc (tối đa hiển|
|---|---|---|

thị “9+”)

Nội dung 1 thông báo bao gồm:

Tên epic/module

Nội dung thông báo

Thời gian thông báo:

Nếu thông báo của ngày hôm nay:

hiển thị dưới dạng hh:mm (nếu cách thời điểm hiện tại > 5 phút)

hiển thị “Bây giờ” (nếu cách thời điểm hiện tại <= 5 phút)

Nếu thông báo của ngày hôm qua trở về trước: hiển thị dưới dạng 1 ngày trước, 2 ngày

trước,…

Các thông báo chưa đọc được hiển thị với màu nền xanh. Nhấn vào dòng thông báo đó để

chuyển sang trạng thái “Đã đọc” & điều hướng đến màn xem chi tiết của đối tượng được thông

báo (sẽ được đĩnh nghĩa chi tiết ở từng usecase)

<!-- Trang 7 -->

→ Reload lại số lượng ở badge trên icon thông báo (-1)

Các thông báo đã đọc được hiển thị với màu nền trắng.

Nhấn Đọc tất cả để chuyển tất cả các thông báo sang trạng thái Đã đọc + reload lại số lượng ở

badge trên icon thông báo (về 0).

### 3. Lịch sử hoạt động

![](images/ndlxd-export.pdf-0007-04.png)

Cho phép người dùng xem lại được lịch sử hoạt động của người dùng đối với các bản ghi trên hệ

thống.

Mỗi bản ghi hoạt động sẽ bao gồm các thông tin sau:

Tên tài khoản thực hiện hành động

Thời gian người dùng thực hiện hành động

Tên hành động người dùng thực hiện

### 4. Thanh điều hướng

![](images/ndlxd-export.pdf-0007-11.png)

Thanh điều hướng bao gồm:

<!-- Trang 8 -->

Trang chủ

Lịch nhắc

Thông báo

Tải khoản

### 5. Danh sách

![](images/ndlxd-export.pdf-0008-05.png)

|Loại control|Item|Ràng buộc|
|---|---|---|
|Trình bày danh sách|Card/List Item|Mỗi bản ghi hiển thị dưới<br>dạng card.<br>Sắp xếp dọc theo chiều<br>cuộn (vertical scroll).|
|Căn lề dữ liệu|Căn lề trong card|Title căn lề trái<br>Nội dung căn lể phải|
|Trạng thái|Hiển thị trạng thái theo màu|Trạng thái hiển thị rõ ràng<br>bằng màu sắc.<br>Trạng thái đặt bên phải<br>hàng đầu tiên của card.|

<!-- Trang 9 -->

|Tìm kiếm|Box tìm kiếm|Thanh tìm kiếm nằm trên<br>cùng danh sách.<br>Hỗ trợ tìm kiếm gần đúng.<br>Kích hoạt sau khi nhấn<br>“Tìm” hoặc “Enter” trên bàn<br>phím mobile.|
|---|---|---|
|Phân trang|Infinity Load|Trên mobile, ưu tiên infinity<br>scroll (cuộn để tải thêm).<br>Mỗi lần tải thêm khoảng 10<br>bản ghi.|
|Hiển thị mặc định|Số bản ghi ban đầu|Mặc định hiển thị 10 bản ghi<br>đầu tiên.|

5.1. Lọc

![](images/ndlxd-export.pdf-0009-02.png)

Ở mỗi màn danh sách, hệ thống hiển thị icon Filter để người dùng có thể filter.

Hệ thống hiển thị 1 popup hiển thị các trường cho phép filter.

Cho phép người dùng lọc các giá trị của các cột trong bảng (Các cột được phép lọc sẽ được

quy định rõ trong từng Usecase).

Khi đang thực hiện lọc thì button Bộ lọc phía bên trên của bảng hiện số lượng cột đang filter.

Các loại filter:

<!-- Trang 10 -->

Chọn giá trị: Người dùng có thể chọn giá trị để filter data.

![](images/ndlxd-export.pdf-0010-01.png)

Date time range picker: Người dùng có thể chọn ngày bắt đầu - ngày kết thúc để filter data

theo thời gian.

![](images/ndlxd-export.pdf-0010-03.png)

Slider: Cho phép người dùng nhập hoặc kéo giá trị trong khoảng min-max.

![](images/ndlxd-export.pdf-0010-05.png)

Hiển thị các tab là các cột (được phép lọc) theo thứ tự từ trên xuống dưới là thứ tự cột từ trái qua

phải của bảng (kể cả các cột đã ẩn).

Trong mỗi tab, hiển thị các giá trị của cột đó & 1 giá trị “Không có” cho các dữ liệu null.

Nhấn chọn 1 hoặc nhiều giá trị để áp dụng bộ lọc cho cột đó hoặc chọn “Xoá tất cả” để bỏ lọc.

### 6. Lịch nhắc

<!-- Trang 11 -->

## [v2.0] Quy tắc chung xử lý giao diện trên Application (Application common rules & shared components)

### PHẦN 1 — SHARED COMPONENTS

Các component dùng chung toàn hệ thống. Các UC chỉ cần gọi theo mã: (Xem MSC-XX — Tên

component).

|Mã|Tên|Dùng khi|
|---|---|---|
|MSC-01|In-app Notification|Mọi hành động nghiệp vụ cần gửi thông báo đến người liên<br>quan trong luồng|
|MSC-02|Confirm Bottom<br>Sheet|Trước hành động quan trọng hoặc không thể hoàn tác|
|MSC-03|Filter Bottom Sheet|Bộ lọc nâng cao cho màn hình danh sách|
|MSC-04|Action Sheet|Danh sách hành động tuỳ chọn từ 1 item|
|MSC-05|Activity Log|Icon 🕐 trên màn hình chi tiết|
|MSC-06|Stepper Header|Màn hình có luồng nghiệp vụ nhiều bước|
|MSC-07|File Upload|Khi upload file lên hệ thống|
|MSC-08|Bottom Navigation|Điều hướng chính giữa các module|
|MSC-09|Empty State|Màn hình danh sách hoặc section không có dữ liệu|
|MSC-10|Skeleton Loader|Khi đang tải dữ liệu|

#### MSC-01 — In-app Notification

![Trang 11 — ảnh xem trước để đối chiếu hình vẽ](images/page-11.png)

<!-- Trang 12 -->

![](images/ndlxd-export.pdf-0012-00.png)

Notification hiển thị trong notification center của app.

**Badge số đếm trên icon chuông.**

|Thành phần|Control|Mô tả|
|---|---|---|
|Badge đếm|Badge|Số thông báo chưa đọc trên icon chuông.|
|Thông báo chưa<br>đọc|—|Nền xanh nhạt.|
|Thông báo đã đọc|—|Nền trắng.|
|Click vào thông<br>báo|—|Chuyển trạng thái → Đã đọc + badge −1 + navigate đến màn<br>chi tiết bản ghi liên quan.|

Pattern nội dung thông báo: (Xem SC-02 Website common rules — Pattern

thông báo chung)

#### MSC-02 — Confirm Popup

<!-- Trang 13 -->

![](images/ndlxd-export.pdf-0013-00.png)

![](images/ndlxd-export.pdf-0013-01.png)

![](images/ndlxd-export.pdf-0013-02.png)

![](images/ndlxd-export.pdf-0013-03.png)

![](images/ndlxd-export.pdf-0013-04.png)

Popup xác nhận trước khi thực hiện hành động quan trọng hoặc không thể hoàn tác.

|Thành phần|Control|Mô tả|
|---|---|---|

<!-- Trang 14 -->

|Icon hành động|Icon|Icon đại diện hành động, nền màu theo loại (đỏ =<br>destructive · xanh lá = xác nhận · vàng = cảnh báo).|
|---|---|---|
|Tiêu đề|Label|Font bold, căn giữa.<br>VD: "Thu hồi bản ghi?"|
|Nội dung mô tả|Label|Mô tả hậu quả hành động.<br>Có thể highlight tên bản ghi bằng bold.|
|Button chính|Button|Full width, màu theo loại hành động.<br>Destructive: đỏ.<br>Xác nhận: xanh lá.|
|Button phụ|Button|Full width, outlined/text.<br>VD: "Huỷ bỏ".|
|Backdrop|—|Nền tối mờ phía sau.<br>Tap ra ngoài = đóng (tương đương button Huỷ), trừ các hành<br>động không thể hoàn tác.|

Các hành động bắt buộc dùng MSC-03: Xoá · Thu hồi · Phê duyệt · Từ chối · Huỷ form (khi có

dữ liệu chưa lưu).

|Action|Tiêu đề|Nội dung|
|---|---|---|
|Xoá|Xoá [tên<br>feature]?|Bạn đang xoá [tên feature] [tên/mã]. Hành động này không<br>thể hoàn tác.|
|Thu hồi|Thu hồi yêu<br>cầu?|Bạn đang thu hồi [tên feature] [tên/mã]. Yêu cầu sẽ trở về<br>trạng thái Bản nháp.|
|Phê duyệt|Xác nhận phê<br>duyệt?|Bạn đang phê duyệt [tên feature] [tên/mã].|
|Từ chối|Từ chối yêu<br>cầu?|Bạn đang từ chối [tên feature] [tên/mã].|
|Huỷ form|Huỷ bản ghi?|Bạn có dữ liệu chưa được lưu. Nếu rời khỏi trang, toàn bộ<br>thông tin sẽ bị mất.|

![Trang 14 — ảnh xem trước để đối chiếu hình vẽ](images/page-14.png)

<!-- Trang 15 -->

#### MSC-03 — Filter Bottom Sheet

![](images/ndlxd-export.pdf-0015-01.png)

**Bottom Sheet bộ lọc nâng cao.**

|Thành phần|Control|Mô tả|
|---|---|---|
|Trigger|Button|Button Bộ lọc trên toolbar màn hình danh sách.<br>Badge số lượng filter đang active.|
|Bottom Sheet|—|Slide up từ dưới.<br>Chiều cao tối đa 85% màn hình.<br>Có thể scroll nội dung bên trong.|
|Header|Label|Tiêu đề "Bộ lọc" + button Đặt lại (text, xanh lá) góc phải.|
|Các trường lọc|—|Tuỳ từng UC.<br>Dạng: Select · DatePicker · Checkbox list.|
|Button Áp dụng|Button|Full width, filled xanh lá, sticky bottom.<br>Click → đóng sheet + áp dụng bộ lọc.|

<!-- Trang 16 -->

|Active filters|Badge|Hiển thị chips bộ lọc đang active ngay dưới search bar màn<br>hình danh sách.<br>Tap vào chip → xoá filter đó.|
|---|---|---|

#### MSC-04 — Action Sheet

![](images/ndlxd-export.pdf-0016-02.png)

**Bottom Sheet danh sách action từ 1 item. Tương ứng với Action Matrix (SC-07) trên web.**

|Thành phần|Control|Mô tả|
|---|---|---|
|Trigger|—|Long press vào item hoặc tap icon ⋯ trên item.|
|Bottom Sheet|—|Slide up.<br>Danh sách action dạng list.|
|Action item|Button|Mỗi action 1 dòng: Icon trái + Label.<br>Destructive action: màu đỏ, luôn ở cuối danh sách.|
|Button Huỷ|Button|Full width, phân cách với danh sách action. Label "Huỷ".|
|Backdrop|—|Tap ra ngoài = đóng.|

<!-- Trang 17 -->

#### MSC-05 — Activity Log

![](images/ndlxd-export.pdf-0017-01.png)

|Thành phần|Control|Mô tả|
|---|---|---|
|Trigger|Icon /<br>Button|Icon 🕐 trên header màn hình chi tiết.|
|Hiển thị|—|Hiển thị màn hình riêng.|
|Nội dung|—|Timeline dọc.<br>Mỗi mốc: Avatar + Tên + Ngày + Icon hành động + Nội dung.<br>Sắp xếp mới nhất lên trên.|

#### MSC-06 — Stepper Header

![](images/ndlxd-export.pdf-0017-04.png)

Header thanh tiến trình cho màn hình có luồng nghiệp vụ nhiều bước.

Xem thêm ở của website.

UC00.00.02

<!-- Trang 18 -->

|Thành phần|Control|Mô tả|
|---|---|---|
|Vị trí|—|Header cố định phía trên màn hình, dưới navigation bar.|
|Step indicator|—|Dạng icon.<br>Step hiện tại: màu xanh lá, bold.<br>Step đã qua: icon ✓ xanh lá.<br>Step chưa đến: xám.|
|Tên bước|Label|Hiển thị dưới step indicator.|
|Navigation|—|Tap trực tiếp vào step để chuyển.|

#### MSC-07 — File Upload

![](images/ndlxd-export.pdf-0018-02.png)

|Thành phần|Control|Mô tả|
|---|---|---|
|Trigger|Button|Vùng tap.|
|Nguồn file|—|Mở bottom sheet chọn nguồn:<br>Thư viện ảnh · Chụp ảnh · Files (file manager).|
|File đang upload|Card|Icon loại file + Tên file + Progress bar + Nút huỷ.|
|File upload thành<br>công|Card|Icon loại file + Tên file + Icon ✓ xanh lá + Icon xoá 🗑️.|
|File upload thất bại|Card|Icon loại file + Tên file + Icon ✕ đỏ + Icon thử lại 🔄 +<br>Icon xoá 🗑️.|

<!-- Trang 19 -->

|Định dạng cho<br>phép|Label|Hiển thị dưới vùng upload.<br>Định nghĩa theo từng UC.|
|---|---|---|
|Dung lượng tối đa|Label|Hiển thị dưới vùng upload.|

#### MSC-08 — Bottom Navigation

![](images/ndlxd-export.pdf-0019-02.png)

**Thanh điều hướng chính cố định phía dưới màn hình.**

|Thành phần|Control|Mô tả|
|---|---|---|
|Vị trí|—|Sticky bottom, phía trên safe area (iPhone notch).|
|Tab items|—|4 tab. Mỗi tab: Icon + Label ngắn.<br>Trang chủ<br>Lịch nhắc<br>Thông báo<br>Tài khoản|
|Tab active|—|Icon + Label màu xanh lá.|
|Tab inactive|—|Icon + Label màu xám.|
|Badge|Badge|Số đếm thông báo trên tab tương ứng. Tối đa hiển thị "99+".|

#### MSC-09 — Empty State

![](images/ndlxd-export.pdf-0019-06.png)

<!-- Trang 20 -->

|Thành phần|Control|Mô tả|
|---|---|---|
|Illustration|Image|Ảnh minh hoạ căn giữa.|
|Tiêu đề|Label|Font bold, căn giữa. VD: "Chưa có dữ liệu".|
|Mô tả|Label|Text phụ xám, căn giữa.<br>Hướng dẫn hoặc giải thích.|
|CTA button|Button|Tuỳ UC. VD: "+ Tạo mới".<br>Chỉ hiển thị nếu user có quyền tạo.|

#### MSC-10 — Skeleton Loader

|Thành phần|Control|Mô tả|
|---|---|---|
|Trigger|—|Hiển thị khi màn hình đang tải dữ liệu lần đầu.|
|Layout|—|Skeleton có hình dạng gần giống layout thực tế của màn<br>hình.<br>Shimmer animation từ trái sang phải.|
|Thay thế|—|Sau khi load xong → skeleton fade out, dữ liệu thực fade in.|

#### MSC-11 — Popcon Thành công (Success Bottom Sheet)

![Trang 20 — ảnh xem trước để đối chiếu hình vẽ](images/page-20.png)

<!-- Trang 21 -->

![](images/ndlxd-export.pdf-0021-00.png)

Bottom Sheet chặn toàn bộ flow, yêu cầu người dùng hiện tại chủ động chọn bước tiếp theo sau

khi hoàn tất một hành động quan trọng.

|Thành phần|Control|Mô tả|
|---|---|---|
|Backdrop|—|Nền tối mờ.<br>Tap không đóng được — bắt buộc chọn button.|
|Container|Bottom Sheet|Slide-up 300ms ease-out.<br>Bo góc trên 20px. C<br>ao tự động, tối đa 85% màn hình.|
|Handle bar|—|40×4px, căn giữa.<br>Swipe down không đóng (khác Bottom Sheet thông<br>thường).|
|Icon|Icon|Tròn nền xanh lá đậm 64px, checkmark + document trắng<br>bên trong.|
|Tiêu đề|Label|Bold 18px, căn giữa.<br>Định nghĩa theo UC.|

<!-- Trang 22 -->

|Mô tả|Label|Regular 14px, xám, căn giữa, tối đa 2 dòng.<br>Định nghĩa theo UC.|
|---|---|---|
|Card tóm tắt|Card|Nền #F5F5F5 , border-radius 12px.<br>Các dòng key–value: label xám trái + giá trị semi-bold phải,<br>divider 1px giữa các dòng.<br>Số dòng và nội dung định nghĩa theo UC.|
|Button chính|Button|Full-width, filled xanh lá đậm.<br>Label + navigation định nghĩa theo UC.|
|Button phụ|Button|Full-width, outlined xám nhạt.<br>Label + navigation định nghĩa theo UC.<br>Back gesture (Android/iOS) xử lý như tap button phụ.|

Cách dùng trong UC: Ghi (Xem MSC-11) và khai báo thêm: nội dung card tóm tắt +

label/navigation của 2 button.

### PHẦN 2 — QUY TẮC CHUNG GIAO DIỆN

#### 2.1 Button

|Quy tắc|Mô tả|
|---|---|
|Validate khi tap|Validate toàn bộ trường bắt buộc khi user tap button Submit / Lưu / Tạo<br>mới.|
|Hiển thị lỗi|Lỗi hiển thị inline ngay dưới trường tương ứng.<br>Scroll đến lỗi đầu tiên nếu cần.|
|Loading state|Button hiển thị spinner + disable trong khi đang xử lý request.<br>Tránh double-tap.|
|Full width|Button chính (CTA) trong form hoặc Bottom Sheet luôn full width.|
|Destructive|Button xoá/huỷ màu đỏ. Không dùng làm CTA chính.<br>Luôn là button phụ hoặc ở vị trí thứ yếu.|

![Trang 22 — ảnh xem trước để đối chiếu hình vẽ](images/page-22.png)

<!-- Trang 23 -->

#### 2.2 Input / Textbox

|Quy tắc|Mô tả|
|---|---|
|Validate On Blur|Validate và hiển thị lỗi ngay dưới field sau khi user blur (rời khỏi field).|
|Validate On Submit|Validate toàn bộ khi tap Submit.<br>Scroll đến field lỗi đầu tiên.|
|Max length — Short|≤ 255 ký tự.<br>Không cho nhập quá.<br>Nếu paste: tự động cắt theo max length.|
|Max length — Long|≤ 4000 ký tự.<br>Counter "X/4000" hiển thị khi còn ≤ 200 ký tự.|
|Keyboard type|Tự động mở đúng loại keyboard:<br>Text · Number · Email · Phone · Decimal.|
|Clear button|Hiển thị icon ✕ trong field khi có nội dung.<br>Tap → xoá toàn bộ.|

#### 2.3 Select / Dropdown

|Quy tắc|Mô tả|
|---|---|
|Hiển thị|Mở Bottom Sheet thay vì dropdown xuống như web.|
|Tìm kiếm|Bottom Sheet có ô tìm kiếm nếu danh sách > 10 item.|
|Single select|Radio button bên phải mỗi item.<br>Tap → chọn ngay, đóng Bottom Sheet.|
|Multi select|Checkbox bên phải mỗi item.<br>Button Xong sticky bottom để xác nhận.|

![Trang 23 — ảnh xem trước để đối chiếu hình vẽ](images/page-23.png)

<!-- Trang 24 -->

|User select|Avatar + Tên (bold) + Mã · Chức vụ (dòng 2, xám).<br>Filled: Avatar nhỏ + Mã - Tên trong field.<br>(Xem Common Rules 2.2 Web)|
|---|---|

#### 2.4 Format số tiền

(Dùng chung với Web — Xem Common Rules 2.4 Website)

|Loại|Quy tắc|Ví dụ|
|---|---|---|
|Phân tách hàng nghìn|Tự động thêm dấu , khi nhập|100,000|
|Hiển thị VND|100,000 đ hoặc 100,000<br>VND tuỳ context|—|
|Làm tròn VND|Không có thập phân.<br>Round Up|123,456.10 → 123,457|
|Làm tròn số học|2 chữ số thập phân, Round Half<br>Up|12.345 → 12.35|

#### 2.5 Format số

(Dùng chung với Web — Xem Common Rules 2.5 Website)

#### 2.6 Format ngày giờ

|Quy tắc|Mô tả|
|---|---|
|Không có giờ|dd/mm/yyyy|
|Có giờ|dd/mm/yyyy HH:mm|
|DatePicker|Mở native date picker của OS hoặc custom wheel picker tuỳ<br>context.|
|Validate|"Hãy nhập ngày tháng theo định dạng: dd/mm/yyyy"|

![Trang 24 — ảnh xem trước để đối chiếu hình vẽ](images/page-24.png)

<!-- Trang 25 -->

#### 2.7 Input Email

|Quy tắc|Mô tả|
|---|---|
|Keyboard type|Tự động mở keyboard email.|
|Format hợp lệ|Phải có @ .<br>VD: example@mail.com .|
|Lỗi|"Email không đúng định dạng."|

#### 2.8 Input Số điện thoại

|Quy tắc|Mô tả|
|---|---|
|Keyboard type|Tự động mở keyboard số (numpad).|
|Ký tự cho phép|Chỉ số.<br>Chặn ký tự khác.|
|Đầu số|0 hoặc 84 .<br>Tối đa 11 ký tự.|
|Format|0xxx xxx xxx hoặc 84 xxx xxx xxx .|
|Lỗi|"SĐT không đúng định dạng."|

#### 2.9 Tìm kiếm

|Quy tắc|Mô tả|
|---|---|
|Kiểu tìm kiếm|Gần đúng (fuzzy) trong toàn bộ dữ liệu danh sách.|
|Kích hoạt|Realtime debounce 300ms sau khi ngừng nhập.|
|Không tìm kiếm được|Các trường fix cứng (trạng thái, phân loại...) → dùng bộ lọc (MSC-<br>05).<br>Các trường không tìm kiếm được định nghĩa trong từng UC.|

![Trang 25 — ảnh xem trước để đối chiếu hình vẽ](images/page-25.png)

<!-- Trang 26 -->

|Empty state khi search|(MSC-10) Tiêu đề: "Không tìm thấy kết quả".<br>Subtext: "Thử tìm với từ khoá khác."|
|---|---|

#### 2.10 Trường không có thông tin

|Loại trường|Hiển thị|
|---|---|
|Ghi chú|Ẩn hoàn toàn nếu không có giá trị.|
|ID / Mã|Hiển thị "N/A" .|
|Các trường còn lại|Hiển thị "--" .|

#### 2.11 Generate ID / Mã bản ghi

(Dùng chung với Web — Xem Common Rules 2.11 Website)

#### 2.12 Xử lý lỗi

BE vs FE check trả lỗi

|Loại lỗi|Hiển thị|
|---|---|
|Lỗi inline|Ngay dưới field tương ứng. Text đỏ + icon ⚠️.<br>Tự ẩn khi user sửa field.|
|Lỗi toast|(MSC-01)<br>Nền đỏ.<br>Dùng cho lỗi không gắn với field cụ thể (VD: lỗi server, lỗi network).|
|Lỗi màn hình|Màn hình lỗi riêng khi không load được dữ liệu:<br>(MSC-10) illustration + mô tả lỗi + button Thử lại.|

#### 2.13 Unsaved Changes

|Quy tắc|Mô tả|
|---|---|

![Trang 26 — ảnh xem trước để đối chiếu hình vẽ](images/page-26.png)

<!-- Trang 27 -->

|Trigger|User tap Back hoặc swipe back khi đang có dữ liệu chưa lưu trong<br>form.|
|---|---|
|Hiển thị|(MSC-03): "Bạn có chắc muốn thoát? Dữ liệu đã nhập sẽ bị mất." +<br>Button Thoát (đỏ) + Button Ở lại (outlined).|
|Không trigger|Khi form chưa có bất kỳ thay đổi nào so với dữ liệu ban đầu.|

#### 2.14 Pull to Refresh

|Quy tắc|Mô tả|
|---|---|
|Trigger|Kéo xuống từ đầu màn hình khi scroll position = 0.|
|Áp dụng|Tất cả màn hình danh sách và màn hình chi tiết.|
|Kết quả|Reload dữ liệu, reset về đầu danh sách.|

#### 2.15 Scroll behavior

|Quy tắc|Mô tả|
|---|---|
|Infinite scroll|Tự động load thêm 20 item khi scroll đến 80% cuối danh sách.<br>Spinner nhỏ ở cuối khi đang tải thêm.<br>Label "Đã hiển thị tất cả kết quả" khi hết dữ liệu.|
|Scroll to top|Tap vào title bar / header → scroll về đầu danh sách.|
|Sticky section header|Section header trong danh sách nhóm dính lại khi scroll qua.|

#### 2.16 Navigation

|Quy tắc|Mô tả|
|---|---|
|Back|Tap nút Back hoặc swipe từ trái sang phải (iOS) / gesture back<br>(Android) → về màn hình trước.|
|Deep link|App hỗ trợ deep link để navigate thẳng vào màn chi tiết từ thông báo<br>(MSC-02).|

![Trang 27 — ảnh xem trước để đối chiếu hình vẽ](images/page-27.png)

<!-- Trang 28 -->

|Bottom Sheet / Modal|Swipe down hoặc tap backdrop → đóng.<br>Ngoại lệ: Bottom Sheet bắt buộc không đóng khi tap backdrop (Xem<br>MSC-03).|
|---|---|

#### 2.17 Trạng thái kết nối mạng

BE vs FE check trả thế nào

![](images/ndlxd-export.pdf-0028-05.png)

|Trạng thái|Hiển thị|
|---|---|
|Mất kết nối|Banner xám phía trên màn hình: "Không có kết nối internet".<br>Sticky cho đến khi kết nối lại.|
|Kết nối lại|Banner xanh lá: "Đã kết nối lại".<br>Tự ẩn sau 2 giây.<br>Tự động retry request đang pending.|
|Request thất bại do<br>mạng|(MSC-01) đỏ: "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."|

#### 2.18 Popup messages đặc biệt

![](images/ndlxd-export.pdf-0028-08.png)

<!-- Trang 29 -->

![](images/ndlxd-export.pdf-0029-00.png)

![](images/ndlxd-export.pdf-0029-01.png)

**Các Bottom Sheet bắt buộc dùng (MSC-03) với backdrop không dismiss.**

|Loại|Trigger|Nội dung|Button|
|---|---|---|---|
|Token hết hạn|Session hết hạn|"Phiên đăng nhập hết<br>hạn. Vui lòng đăng<br>nhập lại để tiếp tục."|Đăng nhập lại (bắt buộc)|
|Không có quyền|Navigate đến màn<br>không có quyền|"Bạn không có quyền<br>xem thông tin này. Vui<br>lòng liên hệ quản trị<br>viên."|Quay lại|
|Phân quyền thay<br>đổi|Flag session được<br>set|"Tài khoản của bạn vừa<br>được thay đổi phân<br>quyền. Vui lòng tải lại<br>để áp dụng thay đổi<br>mới."|Tải lại ngay (bắt buộc)|
|Xác nhận chuyển<br>site|Tap vào item thuộc<br>site khác|"Bạn đang chuyển sang<br>[Tên site]. Trang sẽ<br>được tải lại theo site<br>mới."|Huỷ bỏ + Chuyển site|

<!-- Trang 30 -->

![](images/ndlxd-export.pdf-0030-00.png)

<!-- Trang 31 -->

## UC00.01.01 - Xem trang chủ - Tài khoản nội bộ

#### 1. Thông tin chung

|Mã UC - Tên UC|UC00.01.01 - Xem trang chủ - Tài khoản nội bộ|
|---|---|
|Tác nhân|Người dùng ứng dụng Delta Super App|
|Đường dẫn|Màn hình Đăng nhập >> Màn hình Trang chủ<br>Chọn tới mục Trang chủ trên Navigation bar >> Màn hình Trang<br>chủ|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hệ thống hiển thị màn hình Trang chủ thành công.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình:

##### 3.1 Màn hình Đăng nhập

![](images/ndlxd-export.pdf-0031-06.png)

<!-- Trang 32 -->

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Thông báo|Icon|||Mở tới màn hình Thông báo<br>của app Lái xe||
|2|Báo cáo sự<br>cố|Card|||Mở tới màn hình Danh sách<br>báo cáo sự cố của app Lái xe||
|3|Sửa chữa<br>xe|Card|||Mở tới màn hình Danh sách<br>lệnh sửa chữa của app Lái xe||
|4|Dịch vụ sửa<br>xe ngoài|Card|||Mở tới màn hình Danh sách<br>đơn mua dịch vụ SC ngoài<br>của app Lái xe||

1 Thông báo Icon Mở tới màn hình Thông báo

![Trang 32 — ảnh xem trước để đối chiếu hình vẽ](images/page-32.png)

<!-- Trang 33 -->

## UC00.01.03 - Xem trang chủ - Tài khoản cây dầu

#### 1. Thông tin chung

|Mã UC|UC00.01.03|
|---|---|
|Tên UC|Trang chủ — Tài khoản Cây dầu|
|Tác nhân|Nhân viên cây dầu mua ngoài đã đăng nhập (loại tài khoản = Cây dầu)|
|Đường dẫn|Bottom Navigation → Tab Trang chủ (tab đầu tiên)|
|Điều kiện trước|Đã đăng nhập. Loại tài khoản = Cây dầu.|
|Điều kiện sau|Hiển thị dashboard tổng quan + danh sách phiếu cấp dầu hôm nay của<br>cây.|

Thiết kế đa loại tài khoản: Màn Trang chủ được render theo loại tài khoản. Tài

khoản loại Cây dầu hiển thị layout này. Các loại tài khoản khác (VD: HĐ lẻ, Đối

tác vận tải...) sẽ có layout Trang chủ riêng biệt — định nghĩa trong UC tương

ứng.

#### 2. Lưu đồ hoạt động

1. Người dùng mở app → navigate đến tab Trang chủ.

2. Hệ thống load dữ liệu: tổng phiếu hôm nay + danh sách phiếu.

3. Skeleton loader trong khi tải (App Common — MSC-10).

4. Người dùng có thể:

Tap avatar góc trên trái → navigate UC-PP.02 (Tài khoản).

Tap icon chuông → navigate màn Thông báo.

Tap card phiếu "Chờ bơm" → mở màn chi tiết + Button "Bơm ngay" (UC06.00.11).

Tap "Bơm ngay ›" trực tiếp → shortcut mở Bottom Sheet Ghi nhận bơm dầu (UC06.00.11).

Tap card phiếu "Hoàn thành" → tap "Xem chi tiết ›" → màn chi tiết phiếu.

Pull-to-refresh để tải lại (App Common 2.14).

#### 3. Mô tả màn hình

![Trang 33 — ảnh xem trước để đối chiếu hình vẽ](images/page-33.png)

<!-- Trang 34 -->

##### 3.1 Màn hình Trang chủ

![](images/ndlxd-export.pdf-0034-01.png)

Hiển thị tất cả các phiếu, sắp xếp theo thứ tự thời gian tạo gần nhất → lâu nhất,

||Tên thành<br>phần|Control|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Header|—|—|—|—|Nền xanh lá đậm (màu<br>brand).<br>Không có navigation bar<br>tiêu đề.|—|

<!-- Trang 35 -->

|2|Avatar cây<br>dầu|Image/<br>Button|—|—|—|Góc trên trái.<br>Hình tròn, ảnh đại diện<br>cây dầu.<br>Tap → UC01.01.07 Xem<br>thông tin tài khoản.|—|
|---|---|---|---|---|---|---|---|
|3|Greeting|Label|Text|—|—|Dòng trên: "Xin chào<br>👋," — font regular,<br>trắng nhỏ.<br>Dòng dưới: Tên cây dầu<br>— font bold, trắng lớn.<br>VD: "Petrolimex Đường<br>Láng".|—|
|4|Icon<br>chuông|Icon/Bu<br>tton|—|—|—|Góc trên phải.<br>Badge đỏ số nếu có<br>thông báo chưa đọc.<br>Tap → màn Thông báo.|—|
|5|Card Tổng<br>phiếu hôm<br>nay|Card|—|—|—|Nền trắng, bo góc 16px,<br>shadow nhẹ.<br>Nằm đè lên header<br>(overlap ~50%).<br>Xem cấu trúc chi tiết<br>STT 6–9.|—|
|6|Label tổng|Label|Text|—|—|"Tổng phiếu hôm nay"<br>— font regular, xám nhỏ.|—|
|7|Số phiếu|Label|Number|—|—|Format: X/Y — X = chờ<br>xử lý (trạng thái Chờ<br>bơm) trong hôm nay, Y =<br>tổng các phiếu có trạng<br>thái Hoàn thành trong<br>hôm nay).|—|

![Trang 35 — ảnh xem trước để đối chiếu hình vẽ](images/page-35.png)

<!-- Trang 36 -->

|||||||Font bold 28px, đen.||
|---|---|---|---|---|---|---|---|
|8|Progress<br>bar|—|—|—|—|Thanh ngang 2 màu:<br>xanh lá = đã hoàn thành<br>(60%), xanh nhạt = chờ<br>xử lý (40%).|—|
|9|Label<br>progress|Label|Text|—|—|Trái: "X% chờ xử lý"<br>(xám).<br>Phải: "Y% hoàn thành"<br>(xám).|—|
|1<br>0|Icon<br>illustration|Image|—|—|—|Góc phải card:<br>illustration nhỏ màu xanh<br>nhạt (icon phiếu/danh<br>sách).|—|
|1<br>1|Label<br>"Danh sách<br>cấp dầu"|Label|Text|—|—|Font bold 18px, đen.<br>Padding trên cùng của<br>list section.|—|
|1<br>2|Danh sách<br>card phiếu|List|—|—|—|Infinite scroll.<br>Pull-to-refresh.<br>MSC-10 Skeleton khi<br>loading.<br>Empty state khi không<br>có phiếu hôm nay:<br>"Chưa có phiếu cấp dầu<br>nào hôm nay."<br>Xem cấu trúc card theo<br>trạng thái bên dưới.|—|

##### 3.2 Cấu trúc card chung

Mỗi card phiếu có 2 vùng:

![Trang 36 — ảnh xem trước để đối chiếu hình vẽ](images/page-36.png)

<!-- Trang 37 -->

Vùng trên: Icon loại dGas (44px vuông bo góc) + Mã phiếu (bold) + Dot trạng thái + Nhãn

trạng thái (góc phải) + Tên lái xe • Biển số xe (xám nhỏ).

Vùng dưới (divider ngăn cách): Ngày + CTA (nếu có). Một số trạng thái thêm 2 card THỰC

BƠM / THÀNH TIỀN ở giữa.

##### 3.3 Card theo từng trạng thái

![](images/ndlxd-export.pdf-0037-03.png)

|Trạng thái|Dot|Nhãn|Card data|Ngày|CTA|
|---|---|---|---|---|---|
|waiting|Xanh<br>dương|Chờ bơm|Không có|"Phát hành:<br>dd/mm/yyyy"<br>Lấy theo ngày tạo<br>phiếu dầu|"Bơm ngay ›"<br>(xanh lá bold)|
|po_expir<br>ed|Đỏ|Hết hạn|Không có|"Phát hành:<br>dd/mm/yyyy"<br>Lấy theo ngày tạo<br>phiếu dầu|Không có CTA|
|fuel_don<br>e|Cam/vàng|Đã bơm|✅ THỰC BƠM +<br>THÀNH TIỀN|"Hoàn thành:<br>dd/mm/yyyy"<br>Lấy theo ngày ghi<br>nhận bơm dầu|"Xuất hóa<br>đơn ›" (xanh<br>lá bold)|
|invoice_<br>done|Tím|Đã xuất<br>HĐ|✅ THỰC BƠM +<br>THÀNH TIỀN|"Hoàn thành:<br>dd/mm/yyyy"<br>Lấy theo ngày ghi<br>nhận bơm dầu|"Chốt phiếu<br>›" (xanh lá<br>bold)|

<!-- Trang 38 -->

|done|Xanh lá|Đã hoàn<br>thành|✅ THỰC BƠM +<br>THÀNH TIỀN|"Hoàn thành:<br>dd/mm/yyyy"<br>Lấy theo ngày ghi<br>nhận bơm dầu|Không có CTA|
|---|---|---|---|---|---|

Card data THỰC BƠM / THÀNH TIỀN (hiển thị ở trạng thái fuel_done , invoice_done ,

done ):

2 card nằm ngang, nền xám nhạt, bo góc nhẹ.

THỰC BƠM: Label chữ hoa xám + giá trị "X,XXX L" (bold, đen).

THÀNH TIỀN: Label chữ hoa xám + giá trị "X,XXX,XXX đ" (bold, xanh lá).

<!-- Trang 39 -->

## UC00.01.02 - Xem thanh tiến trình liên quy trình

**Mô tả chung thanh tiến trình**

![](images/ndlxd-export.pdf-0039-02.png)

Thanh tiến trình bao gồm:

Bước (tên + ID đi kèm)

Thanh nối

Tên feature/nghiệp vụ

Thanh tiến trình (mobile) hiển thị no data như sau:

![](images/ndlxd-export.pdf-0039-08.png)

Hiển thị hint text để miêu tả nếu chưa hiển thị luôn thanh tiến trình.

||Control|Loại|Giá trị mặc<br>định|Mô tả|
|---|---|---|---|---|
|1|Bước/step|Icon +<br>Label||Icon: Icon tương ứng với từng feature<br>(fixed theo UI)<br>Tên: hiển thị tên của bước/step tương ứng<br>theo từng feature (tên feature - tên step)<br>Các bước/thứ tự bước của từng quy trình lớn<br>sẽ được mô tả ở<br>.<br>Bước: thể hiện trạng thái theo UI được mô<br>tả ở<br>.<br>ID: Hiển thị lên thanh tiến trình khi<br>feature/bản ghi đó sinh ra ID, tuỳ thuộc<br>vào từng feature/bản ghi đó sinh ra ID khi<br>nào.<br>Chưa có: để là “ID: N/A”<br>Đã có ID: để là “ID: xxxxx”<br>dưới<br>dưới|

|Icon|: Icon tương ứng với từng feature|
|---|---|

<!-- Trang 40 -->

||||Cho phép ấn vào để mở màn hình chi tiết của<br>feature đó (nếu bản ghi của feature đó đã<br>được tạo)<br>Do app Lái xe đang chỉ có thể hiển thị các<br>bản ghi của feature Đơn mua HHDV, Lệnh<br>sửa chữa, Báo cáo sự cố nên chỉ những step<br>này mới mở được màn chi tiết, còn lại khi ấn<br>vào sẽ không hiển thị thông tin, chỉ báo<br>message: “Bạn không có quyền xem thông<br>tin này.”|Cho phép ấn vào để mở màn hình chi tiết của|
|---|---|---|---|---|
|2|Thanh nối|Line|Là thanh nối giữa các step với nhau, thể hiện<br>trạng thái theo UI được mô tả ở<br>.<br>dưới||
|3|Tên<br>feature/nghiệp vụ<br>của popup|Label|Là tên feature/nghiệp vụ đang hiển thị của<br>popup.<br>Hiển thị tên của feature/nghiệp vụ.<br>Đơn mua HHDV → Mua HHDV<br>Báo giá chuẩn đoán → Báo giá (nếu bên<br>SC = khách hàng hoặc loại báo giá = bán<br>phụ tùng), Chuẩn đoán (nếu bên SC =<br>Delta)<br>Lệnh sửa chữa → Sửa chữa<br>Xuất kho → Xuất kho<br>Nhập kho → Nhập kho<br>Đề nghị bồi thường → Bồi thường<br>Thanh toán bán HHDV trả trước → Thanh<br>toán<br>Thanh toán bán HHDV trả sau → Thanh<br>toán||

|bản ghi của feature|Đơn mua HHDV, Lệnh|
|---|---|

|sửa chữa, Báo cáo sự cố|nên chỉ những step|
|---|---|

|message: “|Bạn không có quyền xem thông|
|---|---|

2 Thanh nối Line Là thanh nối giữa các step với nhau, thể hiện

![Trang 40 — ảnh xem trước để đối chiếu hình vẽ](images/page-40.png)

<!-- Trang 41 -->

Thanh toán chi phí trả trước → Thanh toán
Thanh toán chi phí trả sau → Thanh toán
Báo cáo sự cố → Sự cố

**Các step theo từng quy trình**

Lấy theo tài liệu của website.

UC00.00.02

Lưu ý: các step/feature bị phát sinh xảy ra liền kề sau step/feature gây phát sinh trên thanh tiến

trình, trừ feature Lệnh sửa chữa - xuất kho (do 2 feature này xảy ra đồng thời) nên các feature

phát sinh sẽ xảy ra phía sau feautre xuất kho.

**Trạng thái của step trên thanh tiến trình**

Bước trên thanh tiến trình nói chung sẽ có 4 trạng thái như sau:

|Trạng thái|Thanh nối|Bước|Trigger|
|---|---|---|---|
|Chưa triển khai:<br>Nghiệp vụ chưa<br>được, chưa tới<br>bước triển khai.|||Trạng thái mặc định ban đầu của nghiệp<br>vụ/feature<br>Hiển thị khi nghiệp vụ/feature chưa được tạo<br>mới.|
|Đang triển khai:<br>Nghiệp vụ đang<br>được triển khai.|||Hiển thị khi bắt đầu tạo mới nghiệp vụ/feature|
|Đã thu hồi/từ chối:<br>Nghiệp vụ bị thu<br>hồi hoặc bị từ chối<br>thực hiện.|||Hiển thị khi thu hồi/từ chối nghiệp vụ/feature|
|Đã hoàn thành:<br>Nghiệp vụ được<br>hoàn tất hoặc được<br>phê duyệt (nếu phê<br>duyệt là hành động<br>cuối của nghiệp vụ)|||Hiển thị khi hoàn thành (kết thúc toàn bộ luồng)<br>của nghiệp vụ/feature|

![](images/ndlxd-export.pdf-0041-00.png)

<!-- Trang 42 -->

## Epic 01 - Quản lý tài khoản

![](images/ndlxd-export.pdf-0042-01.png)

<!-- Trang 43 -->

### UC01.01.01 - Đăng nhập

#### 1. Thông tin chung

|Mã UC - Tên UC|UC01.01.01 - Đăng nhập|
|---|---|
|Tác nhân|Người dùng ứng dụng Delta Super App/Delta Partner Portal (mọi role)|
|Đường dẫn|Khởi động ứng dụng → Màn Splash → Onboarding (lần đầu) → Màn<br>Đăng nhập|
|Điều kiện trước|Người dùng đã được cấp tài khoản.<br>Trạng thái tài khoản: Đang hoạt động/Hoạt động.<br>Tài khoản có quyền truy cập ứng dụng.|
|Điều kiện sau|Tài khoản nội bộ:<br>Đăng nhập thành công + chọn tổ chức/chi nhánh (nếu có ≥2) →<br>navigate Home nội bộ.<br>Nếu dùng mật khẩu mặc định → navigate Tạo mật khẩu mới<br>(UC01.01.05).<br>Tài khoản đối tác:<br>Đăng nhập thành công → navigate thẳng Home theo loại tài khoản,<br>không qua màn chọn tổ chức.|

#### 2. Lưu đồ hoạt động

1. Người dùng khởi động app → Màn Splash hiển thị 3 giây (hoặc cho đến khi tài nguyên tải

xong) → tự động chuyển tiếp.

2. Kiểm tra session:

Có session hợp lệ → bỏ qua Onboarding + Đăng nhập → kiểm tra tổ chức (bước 6).

Không có session → chuyển sang bước 3.

3. Màn Onboarding (chỉ hiển thị lần đầu cài app hoặc sau khi xoá dữ liệu): Giới thiệu ngắn gọn

về ứng dụng. Button "Đăng nhập" → navigate màn Đăng nhập.

4. Người dùng nhập Tên tài khoản và Mật khẩu → tap "Đăng nhập".

5. Hệ thống xác thực:

![Trang 43 — ảnh xem trước để đối chiếu hình vẽ](images/page-43.png)

<!-- Trang 44 -->

Sai thông tin: Hiển thị inline error. Trừ 1 lần thử. Thông báo: "Tên tài khoản hoặc mật khẩu

không đúng. Bạn còn [X] lần thử."

Sai ≥ 10 lần: Khoá tài khoản → thông báo lỗi: "Tài khoản đã bị khoá. Vui lòng liên hệ Admin

để được hỗ trợ." Không thể đăng nhập tiếp.

Đúng + mật khẩu mặc định: Navigate màn Tạo mật khẩu mới (UC01.01.05).

Đúng + mật khẩu đã thay đổi: Chuyển sang bước 6.

6. Hệ thống xác định loại tài khoản vừa đăng nhập:

Nhánh A — Tài khoản nội bộ:

Hệ thống kiểm tra số tổ chức/chi nhánh có quyền truy cập:

= 1 chi nhánh: Tự động chọn → navigate Home nội bộ. Bỏ qua bước 7.

≥ 2 chi nhánh hoặc ≥ 2 tổ chức: Hiển thị Bottom Sheet Chọn tổ chức (bước 7).

Nhánh B — Tài khoản đối tác:

Không hiển thị màn Chọn tổ chức. Hệ thống tự động xác định loại tài khoản đối tác →

navigate thẳng vào màn Home tương ứng.

Hiện tại hỗ trợ loại: Cây dầu → Home Partner Portal (UC-PP.01).

Các loại đối tác khác sẽ được bổ sung theo từng UC tương ứng.

7. (Chỉ Nhánh A — ≥2 tổ chức/chi nhánh)

Người dùng chọn tổ chức hoặc chi nhánh → tap "Xác nhận" → navigate Home nội bộ.

Tap "Huỷ" → đăng xuất, quay về màn Đăng nhập.

#### 3. Mô tả màn hình

##### 3.1. Màn hình Splash

<!-- Trang 45 -->

![](images/ndlxd-export.pdf-0045-00.png)

Hệ thống hiển thị màn hình Splash khi người dùng truy cập vào ứng dụng

Thời gian hiển thị: 3 giây (hoặc cho đến khi các tài nguyên chính được tải xong). Sau đó, hệ

thống chuyển sang màn hình Onboarding.

Không có hành động tương tác từ người dùng.

##### 3.2. Màn hình Onboarding

![](images/ndlxd-export.pdf-0045-05.png)

<!-- Trang 46 -->

**Màn hình Onboarding:**

Hiển thị nội dung giới thiệu ngắn gọn về ứng dụng.

Có nút CTA Đăng nhập: Khi người dùng nhấn vào, hệ thống chuyển sang màn hình đăng

nhập.

##### 3.3. Màn hình Đăng nhập

![](images/ndlxd-export.pdf-0046-04.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tên tài<br>khoản|Textb<br>ox<br>(short<br>)|||Cho phép người dùng nhập<br>tên tài khoản để đăng nhập<br>vào hệ thống.|Tên tài khoản phải<br>tồn tại trong danh<br>sách tài khoản đang<br>hoạt động của ứng<br>dụng lái xe Delta.|

<!-- Trang 47 -->

|2|Mật khẩu|Textb<br>ox<br>(short<br>)||Cho phép người dùng nhập<br>mật khẩu của tài khoản đó.|Mật khẩu phải<br>khớp với tên tài<br>khoản đã nhập.<br>Không được phép<br>nhập sai mật khẩu<br>quá 10 lần.<br>=> Nếu sai quá 10<br>lần, hệ thống lock tài<br>khoản. Nếu người<br>dùng đăng nhập lại<br>tài khoản bị lock,<br>thông báo lỗi: “Tài<br>khoản này đã bị<br>khoá.”|
|---|---|---|---|---|---|
|3|Eye icon|Icon|Enable<br>button và<br>ẩn<br>passwor<br>ds|Cho phép người dùng bật/tắt<br>hiển thị mật khẩu.<br>Khi người dùng nhấn vào eye<br>icon, mật khẩu sẽ hiển thị dưới<br>dạng văn bản (plain text)<br>Khi nhấn lại vào eye icon, mật<br>khẩu sẽ được ẩn trở lại.||
|4|Ghi nhớ<br>đăng nhập|Chec<br>kbox|Enable|Cho phép người dùng chọn để<br>hệ thống ghi nhớ đăng nhập.<br>Khi checked: session không<br>hết hạn khi đóng app.<br>Khi unchecked: session hết<br>hạn khi đóng app.||
|5|Quên mật<br>khẩu|Butto<br>n|Enable|Cho phép người dùng yêu cầu<br>khôi phục mật khẩu nếu quên.<br>Khi nhấn vào button, người<br>dùng sẽ được chuyển đến<br>popup Quên mật khẩu, thực<br>hiện UC Quên mật khẩu||

![Trang 47 — ảnh xem trước để đối chiếu hình vẽ](images/page-47.png)

<!-- Trang 48 -->

|6|Đăng nhập|Butto<br>n|Enable|Cho phép người dùng gửi<br>thông tin tài khoản và mật<br>khẩu để đăng nhập.|Hệ thống phải kiểm<br>tra tính hợp lệ của<br>tên tài khoản và mật<br>khẩu trước khi đăng<br>nhập.<br>Nếu thông tin<br>đăng nhập sai, hệ<br>thống phải thông<br>báo lỗi và yêu cầu<br>người dùng thử<br>lại: "Tên tài khoản<br>hoặc mật khẩu<br>không đúng. Bạn<br>chỉ còn [?] lần<br>thử".<br>Nếu thông tin<br>đăng nhập đúng:<br>cho phép người<br>dùng vào trang<br>chủ (nếu tài<br>khoản không<br>dùng mật khẩu<br>mặc định) hoặc<br>vào trang Tạo<br>mật khẩu mới,<br>thực hiện UC<br>nếu<br>tài khoản đang<br>dùng tài khoản<br>mặc định.<br>Nếu tài khoản<br>không có quyền<br>Tạo<br>mật khẩu mới|
|---|---|---|---|---|---|

![Trang 48 — ảnh xem trước để đối chiếu hình vẽ](images/page-48.png)

<!-- Trang 49 -->

truy cập vào ứng
dụng Delta, hiển
thị thông báo lỗi:

![](images/ndlxd-export.pdf-0049-00.png)

##### 3.4 Bottom Sheet Chọn tổ chức

![](images/ndlxd-export.pdf-0049-02.png)

Slide-up từ dưới, duration 300ms, bo góc trên 20px.

Chiều cao tự động, tối đa 85% màn hình.

Swipe down không đóng được — bắt buộc chọn trước khi vào app.

|Tên thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá<br>trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|Handle bar|—|—|—|—|40×4px, căn giữa trên cùng.|—|

![](images/ndlxd-export.pdf-0049-04.png)

<!-- Trang 50 -->

||||||Swipe down không đóng.||
|---|---|---|---|---|---|---|
|Tiêu đề|Label|Text|—|—|"Chọn tổ chức".<br>Font bold 18px, căn giữa.|—|
|Card Tổ<br>chức|Radio<br>Card|—|Khôn<br>g|—|Chỉ hiển thị nếu tài khoản có<br>quyền truy cập toàn tổ chức.<br>Icon vuông bo góc xanh nhạt<br>(grid icon) + Tên tổ chức (bold)<br>+ "X chi nhánh" (xám nhỏ).<br>Selected: border xanh lá + nền<br>xanh rất nhạt.|—|
|Separator|Label|Text|—|—|"HOẶC CHỌN CHI NHÁNH CỤ<br>THỂ" — chữ hoa, xám nhỏ, căn<br>trái.<br>Chỉ hiện khi có cả option tổ<br>chức lẫn danh sách chi nhánh.|—|
|Ô tìm kiếm|Input|Text|Khôn<br>g|—|Icon kính lúp trái.<br>Placeholder "Tìm kiếm".<br>Fuzzy search realtime theo tên<br>chi nhánh.|—|
|Danh sách<br>chi nhánh|Radio<br>List|—|Khôn<br>g|—|Danh sách dọc, scroll nếu nhiều.<br>Hiển thị theo thứ tự truy cập gần<br>nhất → xa nhất (thêm thứ tự A-Z<br>nếu cần)<br>Mỗi card: Avatar chữ tắt 2 ký tự<br>(nền xanh nhạt, bo góc) + Tên<br>chi nhánh (bold) + Icon 📍 +<br>Tên tỉnh (xám nhỏ).<br>Tap card → selected.<br>Selected: border xanh lá + nền<br>xanh rất nhạt.|—|

![](images/ndlxd-export.pdf-0050-01.png)

<!-- Trang 51 -->

|Empty state<br>tìm kiếm|Label|—|—|—|"Không tìm thấy chi nhánh phù<br>hợp."<br>(MSC-09)|—|
|---|---|---|---|---|---|---|
|Button Huỷ|Butto<br>n|—|—|—|~40% width, secondary<br>outlined.<br>Tap → đăng xuất, quay về màn<br>Đăng nhập.|—|
|Button Xác<br>nhận|Butto<br>n|—|—|Disabl<br>ed|~60% width, primary xanh lá.<br>Disabled cho đến khi chọn ≥1<br>option.<br>Tap → navigate Home của tổ<br>chức/chi nhánh đã chọn.<br>Session lưu lựa chọn — lần sau<br>tự động bỏ qua màn này nếu<br>vẫn còn quyền.|(Disabled<br>nếu chưa<br>chọn)|

**Ghi chú:**

Tap "Huỷ" = đăng xuất hoàn toàn — không thể vào app nếu chưa chọn.

Session lưu lựa chọn: lần đăng nhập tiếp theo nếu vẫn còn quyền → tự động

bỏ qua Bottom Sheet này.

Bottom Sheet này chỉ áp dụng cho Tài khoản nội bộ. Tài khoản đối tác

không qua bước này.

![Trang 51 — ảnh xem trước để đối chiếu hình vẽ](images/page-51.png)

<!-- Trang 52 -->

### UC01.01.02 - Quên mật khẩu

#### 1. Thông tin chung

|Mã UC - Tên UC|UC01.01.02 - Quên mật khẩu|
|---|---|
|Tác nhân|Người dùng ứng dụng lái xe Delta|
|Đường dẫn|Màn hình Đăng nhập > Chọn Quên mật khẩu|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng lái xe Delta|
|Điều kiện sau|Nếu người dùng chọn Liên hệ IT, thông báo reset mật khẩu được<br>gửi tới bộ phận IT phần mềm ERP Delta và hiển thị màn hình Gửi tài<br>khoản thành công<br>Nếu người dùng chọn Reset mật khẩu bằng email, gửi OTP qua<br>email công ty của người dùng và hiển thị màn hình Kiểm tra hòm<br>thư|

#### 2. Lưu đồ hoạt động:

#### 3. Mô tả màn hình:

##### 3.1. Màn hình Chọn cách lấy lại mật khẩu

![](images/ndlxd-export.pdf-0052-06.png)

<!-- Trang 53 -->

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Liên hệ IT|Butto<br>n||Enable|Cho phép người dùng liên hệ<br>với bộ phận IT để được hỗ trợ<br>khôi phục mật khẩu.<br>Khi nhấn vào button, hệ thống<br>sẽ chuyển hướng người dùng<br>đến màn hình Nhập tên tài<br>khoản - Liên hệ IT.<br>ERP call API cho PMX để<br>update mật khẩu mới mà IT<br>đã reset >> Khi đó, trạng thái<br>tài khoản chuyển sang: Cấp<br>mới||
|2|Reset mật<br>khẩu|Butto<br>n||Enable|Cho phép người dùng yêu cầu<br>reset lại mật khẩu thông qua<br>hệ thống tự động.<br>Khi nhấn vào button, hệ thống<br>sẽ chuyển hướng người dùng<br>đến màn hình Nhập tên tài<br>khoản - Reset bằng email.||

##### 3.2. Màn hình Nhập tên tài khoản

![Trang 53 — ảnh xem trước để đối chiếu hình vẽ](images/page-53.png)

<!-- Trang 54 -->

![](images/ndlxd-export.pdf-0054-00.png)

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tên tài<br>khoản|Textb<br>ox<br>(short<br>)|Có||Cho phép người dùng nhập<br>tên tài khoản để khôi phục<br>hoặc reset mật khẩu.|Hệ thống kiểm tra<br>tài khoản được nhập<br>với các tài khoản<br>đang có sau khi<br>người dùng ấn<br>button Kết thúc<br>nhập<br>Nếu tên tài khoản<br>nhập đúng, hệ<br>thống hiển thị Họ<br>và tên và Tên tài<br>khoản tương ứng<br>Nếu tên tài khoản<br>sai, hệ thống hiển<br>thị thông báo lỗi:|

<!-- Trang 55 -->

||||||"Tên tài khoản<br>không chính xác."|
|---|---|---|---|---|---|
|2|Tài khoản|Label|No data|Hiển thị họ và tên & tên tài<br>khoản tương ứng nếu người<br>dùng nhập đúng tên tài khoản.<br>Hiển thị giao diện no data:|Chỉ tài khoản có<br>trạng thái tài<br>khoản là Đang<br>hoạt động thì mới<br>được đổi mật<br>khẩu.<br>Nếu tên tài khoản<br>sai, hệ thống hiển<br>thị thông báo lỗi:<br>"Tên tài khoản<br>không chính xác."|
|3|Xác nhận|Butto<br>n|Enable|Cho phép người dùng xác<br>nhận và chuyển tiếp đến bước<br>tiếp theo nếu nhập đúng tài<br>khoản:<br>Liên hệ IT: hiển thị màn<br>hình thông báo Gửi tài<br>khoản thành công và gửi<br>email tự động tới email IT<br>Delta:<br>Tiêu đề email: Yêu cầu hỗ trợ<br>đặt lại mật khẩu tài khoản<br>Delta<br>Nội dung email:<br>Xin chào đội IT,<br>Hệ thống vừa ghi nhận một<br>yêu cầu đặt lại mật khẩu từ<br>người dùng. Dưới đây là thông<br>tin chi tiết:<br>Tên tài khoản: [Tên tài<br>khoản]|Chỉ cho phép người<br>dùng gửi email quên<br>mật khẩu 1 lần mỗi<br>phút.<br>Nếu vi phạm, khi<br>người dùng ấn<br>button Xác nhận và<br>báo popup message<br>lỗi như sau:|

![Trang 55 — ảnh xem trước để đối chiếu hình vẽ](images/page-55.png)

<!-- Trang 56 -->

Tên người dùng: [Tên người
dùng]
Thời gian yêu cầu: [Thời
gian gửi yêu cầu]
Vui lòng kiểm tra và hỗ trợ đặt
lại mật khẩu theo quy trình.
Nếu cần thêm thông tin, vui
lòng liên hệ bộ phận hỗ trợ.
Trân trọng,
Đội ngũ hỗ trợ Delta.
Reset mật khẩu bằng email:
Hiển thị màn hình Nhập
OTP
Hệ thống sẽ tự động tạo
& gửi một email với OTP
để người dùng nhập. Nội
dung email gửi từ hệ
thống như sau:
Tiêu đề email:
Yêu cầu reset mật khẩu cho
tài khoản Delta
Nội dung email:
Chào bạn,
Chúng tôi nhận được yêu
cầu reset mật khẩu cho tài
khoản của bạn.
Mã OTP của bạn là: [Mã
OTP]
(Có hiệu lực trong 5 phút)
Nếu bạn không yêu cầu
thay đổi mật khẩu này, vui
lòng bỏ qua email này.
Trân trọng,
Đội ngũ hỗ trợ Delta.

|Mã OTP của bạn là: [|[Mã|
|---|---|

![](images/ndlxd-export.pdf-0056-05.png)

<!-- Trang 57 -->

Mã OTP được định nghĩa
như sau:
OTP có độ dài 6 ký tự,
được sinh ngẫu nhiên.
Thời hạn OTP: 5 phút.

##### 3.3. Màn hình Gửi tài khoản thành công

![](images/ndlxd-export.pdf-0057-00.png)

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Quay lại|Butto<br>n||Enable|Cho phép người dùng nhập<br>quay trở về màn hình Đăng<br>nhập||

##### 3.3. Màn hình Nhập OTP

![](images/ndlxd-export.pdf-0057-03.png)

![](images/ndlxd-export.pdf-0057-05.png)

<!-- Trang 58 -->

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Nhập OTP|Numb<br>erbox|Có||Cho phép người dùng nhập<br>mã OTP được gửi về qua<br>email.<br>Bao gồm 6 ô numberbox<br>tương ứng với OTP 6 chữ số.<br>Mỗi numberbox chỉ được nhập<br>1 chữ số.<br>→ Sau khi người dùng nhập<br>đủ 6 chữ số, hệ thống tự động<br>check validation của dãy số<br>với OTP được gửi.<br>Nếu thành công, chuyển sang<br>màn hình Tạo mật khẩu mới,<br>thực hiện UC Tạo mật khẩu<br>mới|Giới hạn số lần<br>nhập OTP sai (tối<br>đa 5 lần)<br>→ Hệ thống báo<br>popup message<br>“Bạn đã nhập sai mã<br>OTP 5 lần. Vui lòng<br>gửi lại mã OTP mới.”<br>OTP không hợp lệ<br>hoặc hết hạn.<br>→ Hệ thống báo<br>popup message<br>“OTP không hợp lệ<br>hoặc hết hạn. Vui<br>lòng thử lại.”|
|2|Gửi lại mã<br>[x]|Butto<br>n||Disable|Cho phép người dùng gửi lại<br>mã OTP qua email<br>Hệ thống sẽ tự động tạo & gửi<br>một email với OTP để người<br>dùng nhập. Nội dung email gửi<br>từ hệ thống như sau:<br>Tiêu đề email:<br>Yêu cầu reset mật khẩu cho<br>tài khoản Delta<br>Nội dung email:<br>Chào bạn,<br>Chúng tôi nhận được yêu cầu<br>reset mật khẩu cho tài khoản<br>của bạn.||

![Trang 58 — ảnh xem trước để đối chiếu hình vẽ](images/page-58.png)

<!-- Trang 59 -->

||||Mã OTP của bạn là: [Mã OTP]<br>(Có hiệu lực trong 5 phút)<br>Nếu bạn không yêu cầu thay<br>đổi mật khẩu này, vui lòng bỏ<br>qua email này.<br>Trân trọng,<br>Đội ngũ hỗ trợ Delta.<br>Mã OTP được định nghĩa như<br>sau:<br>OTP có độ dài 6 ký tự, được<br>sinh ngẫu nhiên.<br>Thời hạn OTP: 5 phút.<br>Email được gửi phải là email<br>reply email OTP cũ, tránh<br>spam email công ty.<br>Enable button lên sau thời<br>gian expire OTP (5ph), thể<br>hiện số giây đếm ngược còn<br>lại trên UI button.|
|---|---|---|---|
|3|Back|Butto<br>n|Cho phép người dùng nhập<br>quay trở về màn hình Đăng<br>nhập|

|Mã OTP của bạn là: [|[Mã OTP]|
|---|---|

![](images/ndlxd-export.pdf-0059-01.png)

<!-- Trang 60 -->

### UC01.01.03 - Đăng xuất

#### 1. Thông tin chung

|Mã UC - Tên UC|UC01.01.03 - Đăng xuất|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe Delta|
|Đường dẫn|Chọn icon Avatar (góc trên bên phải màn hình) > Button Đăng xuất|
|Điều kiện trước|Người dùng đã đăng nhập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Tài khoản đã đăng xuất khỏi ứng dụng Lái xe Delta<br>Hiển thị màn hình Đăng nhập|

#### 2. Lưu đồ quy trình

![](images/ndlxd-export.pdf-0060-04.png)

#### 3. Mô tả màn hình

##### 3.1 Màn hình Đăng xuất

<!-- Trang 61 -->

![](images/ndlxd-export.pdf-0061-00.png)

Người dụng chọn icon Avatar (góc trên bên phải màn hình) để hiển thị dropdown:

![](images/ndlxd-export.pdf-0061-02.png)

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Đăng xuất|Butto<br>n|||Cho phép người dùng đăng<br>xuất khỏi hệ thống.<br>Khi nhấn vào button Đăng<br>xuất, hệ thống sẽ đăng xuất<br>người dùng khỏi hệ thống và<br>chuyển hướng người dùng về<br>màn hình Đăng nhập.||

<!-- Trang 62 -->

### UC01.01.04 - Đổi mật khẩu

#### 1. Thông tin chung

|Mã UC - Tên UC|UC01.01.04 - Đổi mật khẩu|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe Delta|
|Đường dẫn|Màn hình Thông tin cá nhân > Button Đổi mật khẩu|
|Điều kiện trước|Người dùng đã đăng nhập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Người dùng cập nhật được mật khẩu mới cho tài khoản của mình<br>Hiển thị popup message Thành công<br>Hiển thị trở lại màn hình Thông tin tài khoản|

#### 2. Lưu đồ hoạt động

![](images/ndlxd-export.pdf-0062-04.png)

#### 3. Mô tả màn hình

<!-- Trang 63 -->

![](images/ndlxd-export.pdf-0063-00.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tài khoản|Label|||Hiển thị Họ và tên & Tên tài<br>khoản của người dùng hiện<br>tại.||
|2|Mật khẩu cũ|Textb<br>ox<br>(short<br>)|Có||Cho phép người dùng nhập<br>mật khẩu cũ để xác nhận<br>quyền truy cập.|Mật khẩu cũ phải<br>được nhập chính<br>xác để xác nhận<br>quyền thay đổi mật<br>khẩu.<br>=> Thông báo lỗi:<br>"Mật khẩu cũ không<br>chính xác."|
|3|Eye icon|Icon||Enable +<br>ẩn/mã<br>hoá pass|Cho phép người dùng bật/tắt<br>hiển thị mật khẩu cũ.||

1 Tài khoản Label Hiển thị Họ và tên & Tên tài

<!-- Trang 64 -->

||||||Khi người dùng nhấn vào eye<br>icon, mật khẩu sẽ hiển thị dưới<br>dạng văn bản (plain text)<br>Khi nhấn lại vào eye icon, mật<br>khẩu sẽ được ẩn trở lại.||
|---|---|---|---|---|---|---|
|4|Mật khẩu<br>mới|Textb<br>ox<br>(short<br>)|Có||Cho phép người dùng nhập<br>mật khẩu mới.|Mật khẩu mới phải<br>có ít nhất 8 ký tự,<br>bao gồm chữ cái,<br>số, chữ cái viết<br>hoa và ký tự đặc<br>biệt.<br>=> Thông báo lỗi:<br>“Mật khẩu phải có ít<br>nhất 8 ký tự, bao<br>gồm chữ cái, số,<br>chữ cái viết hoa và<br>ký tự đặc biệt.”<br>Mật khẩu mới<br>không được trùng<br>với mật khẩu hiện<br>tại.<br>=> Thông báo lỗi:<br>“Mật khẩu trùng với<br>mật khẩu cũ”|
|5|Xác nhận<br>mật khẩu<br>mới|Textb<br>ox<br>(short<br>)|Có||Cho phép người dùng nhập lại<br>mật khẩu mới để xác nhận.|Mật khẩu xác<br>nhận phải trùng<br>với mật khẩu mới.<br>=> Thông báo lỗi:<br>"Mật khẩu xác nhận<br>không khớp."|
|6|Xác nhận|Butto<br>n||Enable|Cho phép người dùng xác<br>nhận thay đổi mật khẩu.<br>Khi nhấn vào button Xác nhận,<br>hệ thống sẽ kiểm tra tính hợp||

![Trang 64 — ảnh xem trước để đối chiếu hình vẽ](images/page-64.png)

<!-- Trang 65 -->

lệ của các trường thông tin
(mật khẩu cũ, mật khẩu mới
và xác nhận mật khẩu mới).
Nếu thành công, thực hiện
cập nhật mật khẩu mới cho
tài khoản này & hiển thị
popup message Đổi mật
khẩu thành công & tắt
popup Đổi mật khẩu
(Cập nhật mật khẩu mới cả
qua hệ thống ERP Delta)
Nếu có lỗi, hệ thống sẽ hiển
thị thông báo lỗi cụ thể nêu
trên.

![](images/ndlxd-export.pdf-0065-00.png)

![](images/ndlxd-export.pdf-0065-02.png)

<!-- Trang 66 -->

### UC01.01.05 - Tạo mật khẩu mới

#### 1. Thông tin chung

|Mã UC - Tên UC|UC01.01.05 - Tạo mật khẩu mới|
|---|---|
|Tác nhân|Người dùng ứng dụng lái xe Delta|
|Đường dẫn|TH1: Màn hình Đăng nhập (đăng nhập lần đầu tiên) > Màn hình Tạo<br>mật khẩu mới<br>TH2: Màn hình Đăng nhập (sau khi IT ERP Delta reset thành mật<br>khẩu mặc định) > Màn hình Tạo mật khẩu mới<br>TH3: Link đường dẫn reset mật khẩu ở email (đi từ luồng<br>- Reset mật khẩu bằng email) > Màn hình Tạo mật khẩu mới<br>Quên mật<br>khẩu|
|Điều kiện trước|TH1 & TH2: Tài khoản người dùng đang dùng mật khẩu mặc định<br>TH3: Email tài khoản nhận được link reset mật khẩu đã gửi từ luồng<br>- Reset mật khẩu bằng email<br>Quên mật khẩu|
|Điều kiện sau|Người dùng cập nhật được mật khẩu mới cho tài khoản của mình<br>Hiển thị popup message thành công<br>Hiển thị màn hình Đăng nhập, cho phép người dùng đăng nhập với<br>mật khẩu mới|

#### 2. Lưu đồ hoạt động

![Trang 66 — ảnh xem trước để đối chiếu hình vẽ](images/page-66.png)

<!-- Trang 67 -->

![](images/ndlxd-export.pdf-0067-00.png)

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tạo mật khẩu mới

![](images/ndlxd-export.pdf-0067-03.png)

<!-- Trang 68 -->

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tài khoản|Label|||Hiển thị họ và tên & tên tài<br>khoản tương ứng sau khi nhập<br>đúng tên tài khoản.||
|2|Mật khẩu<br>mới|Textb<br>ox<br>(short<br>)|Có||Cho phép người dùng nhập<br>mật khẩu mới.|Mật khẩu mới phải<br>có ít nhất 8 ký tự,<br>bao gồm chữ cái,<br>số, chữ cái viết<br>hoa và ký tự đặc<br>biệt.<br>→ Thông báo lỗi:<br>“Mật khẩu phải có ít<br>nhất 8 ký tự, bao<br>gồm chữ cái, số,<br>chữ cái viết hoa và<br>ký tự đặc biệt.”<br>Mật khẩu mới<br>không được trùng<br>với mật khẩu mặc<br>định.<br>→ Thông báo lỗi:<br>“Mật khẩu trùng với<br>mật khẩu mặc định”|
|3|Eye icon|Icon||Enable +<br>ẩn/mã<br>hoá pass|Cho phép người dùng bật/tắt<br>hiển thị mật khẩu cũ.<br>Khi người dùng nhấn vào eye<br>icon, mật khẩu sẽ hiển thị dưới<br>dạng văn bản (plain text)<br>Khi nhấn lại vào eye icon, mật<br>khẩu sẽ được ẩn trở lại.||

1 Tài khoản Label Hiển thị họ và tên & tên tài

![Trang 68 — ảnh xem trước để đối chiếu hình vẽ](images/page-68.png)

<!-- Trang 69 -->

|4|Nhập lại mật<br>khẩu mới|Textb<br>ox<br>(short<br>)|Có||Cho phép người dùng nhập lại<br>mật khẩu mới để xác nhận.|Mật khẩu xác nhận<br>phải trùng với mật<br>khẩu mới.<br>→ Thông báo lỗi:<br>"Mật khẩu xác nhận<br>không khớp."|
|---|---|---|---|---|---|---|
|5|Đổi mật<br>khẩu|Butto<br>n|||Cho phép người dùng xác<br>nhận thay đổi mật khẩu.|Sau khi nhấn, hệ<br>thống sẽ kiểm tra<br>tính hợp lệ của mật<br>khẩu,<br>Nếu thành công,<br>hiển thị toast<br>message "Đổi mật<br>khẩu thành công"<br>và tự động đăng<br>nhập người dùng<br>vào trang chủ<br>Delta.<br>Nếu thất bại, hiển<br>thị thông báo lỗi<br>“Đã có lỗi xảy ra,<br>vui lòng thử lại.”|
|6|Xác nhận|Butto<br>n||Enable|Cho phép người dùng xác<br>nhận tạo mật khẩu mới.<br>Khi nhấn vào button Xác nhận,<br>hệ thống sẽ kiểm tra tính hợp<br>lệ của các trường thông tin<br>(mật khẩu cũ, mật khẩu mới<br>và xác nhận mật khẩu mới).<br>Nếu thành công, thực hiện<br>cập nhật mật khẩu mới cho<br>tài khoản này & hiển thị<br>toast message Đổi mật<br>khẩu thành công & hiển thị<br>màn hình Đăng nhập, thực||

![Trang 69 — ảnh xem trước để đối chiếu hình vẽ](images/page-69.png)

<!-- Trang 70 -->

hiện chức năng UC
(Cập nhật mật khẩu mới cả
qua hệ thống ERP Delta)
Nếu có lỗi, hệ thống sẽ hiển
thị thông báo lỗi cụ thể nêu
trên.
Đăng
nhập

![](images/ndlxd-export.pdf-0070-00.png)

![](images/ndlxd-export.pdf-0070-02.png)

<!-- Trang 71 -->

### UC01.01.06 - Xem thông tin cá nhân - Tài khoản nội bộ

#### 1. Thông tin chung

|Mã UC - Tên UC|UC01.01.06 - Xem thông tin cá nhân - Tài khoản nội bộ|
|---|---|
|Tác nhân|Người dùng ứng dụng Delta Super App|
|Đường dẫn|Màn hình bất kỳ > icon Avatar > Màn hình Thông tin tài khoản<br>Màn hình bất kỳ > Icon Tài khoản trên Navigation Bar|
|Điều kiện trước|Người dùng đã đăng nhập vào ứng dụng lái xe Delta|
|Điều kiện sau|Người dùng xem được thông tin tài khoản của mình đang đăng nhập|

#### 2. Lưu đồ hoạt động

![](images/ndlxd-export.pdf-0071-04.png)

#### 3. Mô tả màn hình

##### 3.1. Màn hình Xem thông tin tài khoản

<!-- Trang 72 -->

![](images/ndlxd-export.pdf-0072-00.png)

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Họ và tên &<br>Tên tài<br>khoản|Label|||Hiển thị thông tin Họ và tên<br>của người dùng đang đăng<br>nhập.||
|2|Trạng thái|Label|||Hiển thị trạng thái tài khoản||
|3|ID nhân<br>viên|Label|||Hiển thị ID nhân viên||
|4|Chức vụ|Label|||Hiển thị Chức vụ, để trống nếu<br>không có.||

2 Trạng thái Label Hiển thị trạng thái tài khoản

Label Hiển thị ID nhân viên

4 Chức vụ Label Hiển thị Chức vụ, để trống nếu

<!-- Trang 73 -->

|5|Phòng ban|Label|Hiển thị tên Phòng ban, để<br>trống nếu không có.|
|---|---|---|---|
|6|Xưởng|Label|Hiển thị tên Xưởng, để trống<br>nếu không có.|
|7|Ngày sinh|Label|Hiển thị Ngày sinh, để trống<br>nếu không có.|
|8|Giới tính|Label|Hiển thị Giới tính, để trống nếu<br>không có.|
|9|Email|Label|Hiển thị Email, để trống nếu<br>không có.|
|1<br>0|Số điện<br>thoại|Label|Hiển thị SĐT, để trống nếu<br>không có.|
|1<br>1|Mã số thuế|Label|Hiển thị MST, để trống nếu<br>không có.|
|1<br>2|Địa chỉ|Label|Hiển thị Địa chỉ, để trống nếu<br>không có.|
|1<br>3|Ghi chú|Label|Hiển thị Ghi chú, để trống nếu<br>không có.|
|1<br>4|Hành động|Butto<br>n|Chọn để hiển thị các hoạt<br>động người dùng có thể làm<br>đối với tài khoản:<br>Đổi mật khẩu<br>=> Chọn để mở popup Đổi<br>mật khẩu, thực hiện UC<br>Lịch sử hoạt động: Cho<br>phép người dùng xem được<br>lịch sử hoạt động của nhân<br>viên<br>-> Chọn để hiển thị popup<br>Lịch sử hoạt động của<br>Đổi<br>mật khẩu|

5 Phòng ban Label Hiển thị tên Phòng ban, để

6 Xưởng Label Hiển thị tên Xưởng, để trống

7 Ngày sinh Label Hiển thị Ngày sinh, để trống

8 Giới tính Label Hiển thị Giới tính, để trống nếu

9 Email Label Hiển thị Email, để trống nếu

1 Mã số thuế Label Hiển thị MST, để trống nếu

1 2 Địa chỉ Label Hiển thị Địa chỉ, để trống nếu

1 3 Ghi chú Label Hiển thị Ghi chú, để trống nếu

![](images/ndlxd-export.pdf-0073-01.png)

<!-- Trang 74 -->

nhân viên đó
Đăng xuất: Thực hiện UC
Đăng xuất

![](images/ndlxd-export.pdf-0074-00.png)

<!-- Trang 75 -->

### UC01.01.07 - Xem thông tin tài khoản - Tài khoản cây dầu

#### 1. Thông tin chung

|Mã UC|UC01.01.07|
|---|---|
|Tên UC|Xem thông tin tài khoản — Cây dầu|
|Tác nhân|Nhân viên cây dầu mua ngoài đã đăng nhập|
|Đường dẫn|App Delta Partner Portal: Bottom Navigation → Tab Tài khoản (tab<br>cuối) hoặc tap Avatar trên Trang chủ|
|Điều kiện trước|Đã đăng nhập. Loại tài khoản = Cây dầu.|
|Điều kiện sau|Hiển thị thông tin đầy đủ của cây dầu.<br>Đăng xuất nếu người dùng chọn.|

Tham chiếu: Nội dung màn này tương đương UC12.04.05 (Xem chi tiết cây

dầu mua ngoài) trên web/ERP, nhưng render trên app Portal theo góc nhìn của

chính cây dầu đó (chỉ xem thông tin của mình, không có action phê duyệt/từ

chối).

#### 2. Lưu đồ hoạt động

1. Người dùng tap Tab Tài khoản hoặc Avatar trên Trang chủ.

2. Hệ thống load thông tin tài khoản cây dầu. Skeleton loader khi tải.

3. Người dùng xem thông tin (read-only). Không có action chỉnh sửa trực tiếp trên màn này.

4. Người dùng tap "Đăng xuất" → MSC-02 Confirm → Đăng xuất, redirect về màn đăng nhập.

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tài khoản

![Trang 75 — ảnh xem trước để đối chiếu hình vẽ](images/page-75.png)

<!-- Trang 76 -->

![](images/ndlxd-export.pdf-0076-00.png)

|Tên thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|Avatar cây<br>dầu|Image|—|—|—|Hình tròn lớn (~80px), căn giữa.<br>Ảnh đại diện cây dầu.<br>Không có ảnh → fallback icon<br>no data.|—|
|Tên cây dầu|Label|Text|—|—|Font bold 20px, căn giữa.<br>VD: "Petrolimex Đường Láng".|—|
|Mã đối tác|Label|Text|—|—|"Mã đối tác: XXXXXXXX" —<br>font regular, xám, căn giữa.|—|

Section: Thông tin cây dầu

<!-- Trang 77 -->

![](images/ndlxd-export.pdf-0077-00.png)

|Thuộc nhà<br>cung cấp<br>HHDV|Card|—|—|—|Label nhỏ xám "Thuộc nhà<br>cung cấp HHDV". Card: Avatar<br>chữ cái (nền màu theo tên) +<br>Tên NCC (bold) + Mã NCC · Mô<br>tả ngắn (xám nhỏ).<br>(Xem UC12.04.05 STT 11)|—|
|---|---|---|---|---|---|---|
|Người đại<br>diện|Card|—|—|—|Label nhỏ xám "Người đại diện".<br>Card: Avatar chữ cái (nền xanh<br>lá) + Tên người đại diện (bold)<br>+ Mã NV · Chức vụ (xám nhỏ).<br>(Xem UC12.04.05 STT 13)|—|
|Địa chỉ|Label|Text|—|—|Label nhỏ xám "Địa chỉ".<br>Giá trị: địa chỉ đầy đủ (bold,<br>đen).|—|
|Ghi chú|Textar<br>ea|Text|—|—|Label nhỏ xám "Ghi chú". Giá trị<br>trong box nền xám nhạt, font<br>italic.<br>Ẩn hoàn toàn nếu không có<br>giá trị(App Common 2.10).|—|

**Section: Hạn mức**

![](images/ndlxd-export.pdf-0077-03.png)

<!-- Trang 78 -->

Icon chart tròn + label "Hạn mức".

Dữ liệu theo tháng hiện tại, reset đầu tháng mới.

(Xem UC12.04.05 STT 15–19)

|Đã cấp|Label|Numb<br>er|—|—|Dot cam + label "Đã cấp" (trái).<br>Giá trị: X,XXX,XXX L (font lớn,<br>cam).|—|
|---|---|---|---|---|---|---|
|Còn lại|Label|Numb<br>er|—|—|Dot xanh lá + label "Còn lại"<br>(phải).<br>Giá trị: X,XXX,XXX L (font lớn,<br>xanh lá).|—|
|Progress<br>bar hạn<br>mức|—|—|—|—|Thanh ngang 2 màu: cam = đã<br>cấp, xanh = còn lại.<br>Bên dưới: "X% tổng hạn mức"<br>(cam, trái) + "Y%" (xanh, phải).<br>(Xem UC12.04.05 STT 19)|—|
|Loại hợp<br>đồng|Label|Text|—|—|Label nhỏ xám "Loại hợp đồng"<br>(trái) + giá trị "Đặt cọc" / "Tín<br>chấp" (bold, phải).|—|
|Số tiền đặt<br>cọc|Label|Numb<br>er|Hidden|—|Chỉ hiển thị khi Loại hợp đồng<br>= "Đặt cọc".<br>Label "Số tiền đặt cọc" (trái) +<br>giá trị "X,XXX,XXX đ" (bold,<br>phải).|—|

Section: Hợp đồng

Icon tài liệu + label "Hợp đồng".

(Xem UC12.04.05 STT 20–22)

![Trang 78 — ảnh xem trước để đối chiếu hình vẽ](images/page-78.png)

<!-- Trang 79 -->

||||||Ẩn hoàn toàn khi Tín chấp (App<br>Common 2.10).||
|---|---|---|---|---|---|---|
|Button<br>Đăng xuất|Button|—|—|—|Full-width, text màu đỏ nhạt,<br>icon [→ ra ngoài bên trái.<br>Không có border/background.<br>Tap → MSC-02 Confirm: "Bạn<br>có chắc muốn đăng xuất?" →<br>Button "Ở lại" + Button "Đăng<br>xuất" (đỏ) → Đăng xuất,<br>redirect về màn đăng nhập.|—|
|Bottom<br>Navigation|—|—|—|—|3 tab: Trang chủ · Thông báo ·<br>Tài khoản (active).|—|

Ghi chú màn hình: Màn này chỉ đọc — không có action chỉnh sửa. Mọi thay

đổi thông tin cây dầu phải thực hiện qua CBQL trên Delta ERP (UC12.04.06).

Hạn mức hiển thị theo tháng hiện tại và tự động reset về 0 vào đầu tháng mới.

![Trang 79 — ảnh xem trước để đối chiếu hình vẽ](images/page-79.png)

<!-- Trang 80 -->

## Epic 02 - Đơn mua dịch vụ sửa chữa ngoài

![](images/ndlxd-export.pdf-0080-01.png)

<!-- Trang 81 -->

### 02 - Thông báo & Lịch sử hoạt động

Danh sách các thông báo và lịch sử hoạt động (chức năng xem thêm ở ) của

Common rules

phần Mua hàng hoá dịch vụ như sau:

|Đối<br>tượ|Hệ<br>thống|Thời điểm|Nội dung thông báo|Đối tượng nhận<br>thông báo|Nội dung lịch sử<br>hoạt động|
|---|---|---|---|---|---|
|ng|trigge<br>r|||||
|Tạo<br>mới|PM<br>Xưởng|Sau khi người<br>dùng tạo thành<br>công yêu cầu<br>tạo.|PO - Mua HHDV<br>Yêu cầu mua HHDV<br>- [Loại đơn] đang<br>chờ phê duyệt.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng có<br>quyền phê<br>duyệt/từ chối<br>yêu cầu tạo mới<br>lần 1.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã tạo yêu cầu tạo<br>mới|
||PM<br>Xưởng|Sau khi người<br>dùng huỷ thành<br>công yêu cầu<br>tạo.|PO - Mua HHDV<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã bị<br>huỷ.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng có<br>quyền phê<br>duyệt/từ chối<br>yêu cầu tạo mới<br>lần 1.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã huỷ yêu cầu tạo<br>mới|
||PM<br>Xưởng|Sau khi người<br>dùng phê duyệt<br>lần 1 thành công<br>yêu cầu tạo.|PO - Mua HHDV<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã được<br>phê duyệt lần 1.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã phê duyệt yêu<br>cầu tạo mới lần 1|
||PM<br>Xưởng|Sau khi người<br>dùng từchối|PO - Mua HHDV|Hệ thống PM<br>Xưởng:|[Tên tài khoản thực<br>hiện hành động]|
||ưởg|dù g từc ố<br>thành công yêu||ưởg|ệ<br>à<br>độg]<br>hh:mm dd/mm/yyyy|

![Trang 81 — ảnh xem trước để đối chiếu hình vẽ](images/page-81.png)

<!-- Trang 82 -->

||cầu tạo ở lần<br>phê duyệt 1.|Yêu cầu mua HHDV<br>- [Loại đơn] đã bị từ<br>chối ở lần phê duyệt<br>1.|Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới và người<br>dùng có quyền<br>phê duyệt/từ<br>chối yêu cầu tạo<br>mới lần 2.|Đã từ chối yêu cầu<br>tạo mới ở lần phê<br>duyệt 1.<br>Lý do: [Lý do người<br>dùng nhập khi thực<br>hiện hành động]|
|---|---|---|---|---|
|PM<br>Xưởng|Sau khi người<br>dùng phê duyệt<br>lần 2 thành<br>công yêu cầu<br>tạo.|PO - Mua HHDV<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã được<br>phê duyệt lần 2.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới/phê duyệt<br>lần 1.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã phê duyệt yêu<br>cầu tạo mới lần 2|
|PM<br>Xưởng|Sau khi người<br>dùng từ chối<br>thành công<br>yêu cầu tạo ở<br>lần phê duyệt<br>2.<br>Loại đơn<br>không phải là<br>đơn mua dịch<br>vụ SC ngoài<br>hay đơn mua<br>dịch vụ SC<br>PT hỏng ở<br>xưởng ngoài.|PO - Mua HHDV<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã bị từ<br>chối ở lần phê duyệt<br>2.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới/phê duyệt<br>lần 1.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã từ chối yêu cầu<br>tạo mới ở lần phê<br>duyệt 2.<br>Lý do: [Lý do người<br>dùng nhập khi thực<br>hiện hành động]|
|PM<br>Xưởng|Sau khi người<br>dùng từ chối<br>thành công<br>yêu cầu tạo ở<br>lần phê duyệt<br>2.|PO - Mua HHDV<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã bị từ<br>chối ở lần phê duyệt<br>2.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo||

|Hệ thống|PM|
|---|---|

|-|[Loại đơn]|đã bị từ|
|---|---|---|

![](images/ndlxd-export.pdf-0082-00.png)

<!-- Trang 83 -->

|||Loại đơn là<br>đơn mua dịch<br>vụ SC ngoài<br>hay đơn mua<br>dịch vụ SC<br>PT hỏng ở<br>xưởng ngoài.||mới/phê duyệt<br>lần 1.<br>Hệ thống App<br>Lái xe:<br>Hiển thị đối với<br>người dùng là lái<br>xe của phương<br>tiện được chọn<br>tới.||
|---|---|---|---|---|---|
|Ngh<br>iệm<br>thu|App<br>Lái xe|Sau khi người<br>dùng từ app Lái<br>xe nghiệm thu<br>thành công lệnh<br>sửa chữa.|PO - Nghiệm thu<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã được<br>nghiệm thu thành<br>công.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới/phê duyệt<br>lần 1 và lần 2.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã nghiệm thu|
||APP<br>Lái xe|Sau khi người<br>dùng từ app Lái<br>xe từ chối<br>nghiệm thu<br>thành công lệnh<br>sửa chữa.|PO - Nghiệm thu<br>Yêu cầu mua HHDV<br>- [Loại đơn] đã bị từ<br>chối nghiệm thu.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới/phê duyệt<br>lần 1 và lần 2.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã từ chối nghiệm<br>thu<br>Lý do: [Lý do người<br>dùng nhập khi thực<br>hiện hành động]|

|Loại đơn|là|
|---|---|

**Các loại đơn HHDV bao gồm:**

Mua hàng hoá

Mua dịch vụ

Mua dịch vụ có phương tiện

Mua dịch vụ sửa chữa xe ngoài

Mua dịch vụ sửa phụ tùng hỏng ở xưởng ngoài

Điều hướng sau khi nhấn vào thông báo: Dẫn đến màn hình Thông tin đơn mua HHDV

![Trang 83 — ảnh xem trước để đối chiếu hình vẽ](images/page-83.png)

<!-- Trang 84 -->

### 02 - Lưu đồ trạng thái cho đơn mua HHDV

![](images/ndlxd-export.pdf-0084-01.png)

|Trạng thái|Hệ<br>thốn<br>g<br>trigg<br>er|Thời điểm (Trigger)|Hành động ở PM<br>Xưởng (chưa tính<br>phân quyền)|Hành động ở APP<br>Lái xe (chưa tính<br>phân quyền)|
|---|---|---|---|---|
|Chờ phê<br>duyệt|PM<br>Xưởn<br>g|Sau khi người dùng tạo yêu<br>cầu tạo mới|Phê duyệt yêu cầu<br>tạo mới ở lần phê<br>duyệt 1<br>Từ chối yêu cầu<br>tạo mới ở lần phê<br>duyệt 1<br>Huỷ yêu cầu tạo<br>mới||
|Đã huỷ|PM<br>Xưởn<br>g|Sau khi người dùng huỷ<br>yêu cầu tạo mới|Xoá yêu cầu<br>Tạo mới yêu cầu||
|Đã từ chối|PM<br>Xưởn<br>g|Sau khi người dùng từ chối<br>yêu cầu tạo mới ở lần phê<br>duyệt 1,2|Xoá yêu cầu<br>Tạo mới yêu cầu||

<!-- Trang 85 -->

|Đã phê duyệt<br>- lần 1|PM<br>Xưởn<br>g|Sau khi người dùng phê<br>duyệt yêu cầu tạo mới ở<br>lần phê duyệt 1|Phê duyệt yêu cầu<br>tạo mới ở lần phê<br>duyệt 2<br>Từ chối yêu cầu<br>tạo mới ở lần phê<br>duyệt 2<br>Huỷ yêu cầu tạo<br>mới||
|---|---|---|---|---|
|Đã phê duyệt<br>- lần 2|PM<br>Xưởn<br>g|Sau khi người dùng phê<br>duyệt yêu cầu tạo mới ở<br>lần phê duyệt 2<br>Trường hợp loại đơn<br>không phải là đơn mua<br>DVSC ngoài hoặc sửa<br>chữa PT hỏng ở xưởng<br>ngoài|Tạo phiếu nhập<br>kho<br>Tạo phiếu đề nghị<br>thanh toán||
|Chờ nghiệm<br>thu|PM<br>Xưởn<br>g|Sau khi người dùng phê<br>duyệt yêu cầu tạo mới ở<br>lần phê duyệt 2<br>Trường hợp loại đơn là<br>đơn mua DVSC ngoài<br>hoặc sửa chữa PT hỏng<br>ở xưởng ngoài|Tạo phiếu nhập<br>kho<br>Tạo phiếu đề nghị<br>thanh toán<br>Hai nghiệp vụ trên sẽ<br>xử lý sau ở giai đoạn<br>tiếp theo.|Nghiệm thu<br>Từ chối nghiệm<br>thu|
|Đã nghiệm<br>thu|APP<br>Lái xe|Sau khi người dùng<br>nghiệm thu đơn mua<br>HHDV.|||
|Từ chối<br>nghiệm thu|APP<br>Lái xe|Sau khi người dùng từ chối<br>nghiệm thu đơn mua<br>HHDV.|Tạo mới yêu cầu||

|Sau khi người dùng|phê|
|---|---|

|nghiệm thu|đơn mua|
|---|---|

|Sau khi người dùng|từ chối|
|---|---|

|nghiệm thu|đơn mua|
|---|---|

![Trang 85 — ảnh xem trước để đối chiếu hình vẽ](images/page-85.png)

<!-- Trang 86 -->

### UC02.01.01 - Xem danh sách đơn mua DVSC ngoài

#### 1. Thông tin chung

|Mã UC - Tên UC|UC02.01.01 - Xem lịch sử mua hàng hoá dịch vụ|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe|
|Đường dẫn|Màn hình Trang chủ >> chọn card Dịch vụ sửa chữa ngoài|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hệ thống hiển thị lịch sử mua dịch vụ thành công.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1. Màn hình Lịch sử mua dịch vụ sửa chữa ngoài

![](images/ndlxd-export.pdf-0086-06.png)

<!-- Trang 87 -->

Hiển thị đơn mua hàng theo các điều kiện sau:

Là đơn mua hàng loại mua DVSC ngoài

PT mua dịch vụ là PT của người dùng hiện tại

Trạng thái Chờ nghiệm thu thì mới hiển thị, sau đó nếu có từ chối thì vẫn keep hiện bản ghi

đấy

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Thanh tìm<br>kiếm|Searc<br>h box|||Cho phép tìm kiếm gần đúng<br>các dữ liệu trong toàn bộ bảng<br>(trừ trạng thái)||
|2|Bộ lọc|Sideb<br>ar|||Xem mô tả phần<br>Cho phép lọc các cột sau:<br>Thời gian tạo đơn<br>Thời gian đặt hàng<br>Loại đơn dịch vụ (SC xe, SC<br>phụ tùng hỏng)<br>Nhà cung cấp<br>Người phụ trách<br>Trạng thái<br>Common<br>Rules||
|3|Thời gian<br>tạo đơn|Label|||Hiển thị thời gian tạo đơn mua<br>HHDV||
|4|Mã đơn<br>hàng|Label|||Hiển thị mã đơn hàng (chỉ có<br>khi ở trạng thái đã phê duyệt 2<br>lần)||
|5|Người phụ<br>trách|Label|||Hiển thị người phụ trách của<br>đơn mua dịch vụ||
|6|Tổng GTTT|Colu<br>mn|||Hiển thị tổng giá trị thanh toán<br>của đơn mua HHDV||

![Trang 87 — ảnh xem trước để đối chiếu hình vẽ](images/page-87.png)

<!-- Trang 88 -->

|7|Trạng thái|Colu<br>mn|Hiển thị trạng thái hiện tại của<br>bản ghi (xem thêm ở<br>)<br>Lưu đồ<br>trạng thái|
|---|---|---|---|

![](images/ndlxd-export.pdf-0088-01.png)

<!-- Trang 89 -->

### UC02.01.02 - Xem thông tin chi tiết đơn mua dịch vụ ngoài

#### 1. Thông tin chung

|Mã UC - Tên UC|UC02.01.02 - Xem thông tin chi tiết đơn mua dịch vụ ngoài|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe Delta|
|Đường dẫn|Màn hình Danh sách đơn mua dịch vụ ngoài > Nhấn vào 1 bản ghi trong<br>bảng: Hiển thị màn hình thông tin đơn mua dịch vụ|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hiển thị thông tin chi tiết đơn mua dịch vụ ngoài thành công.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Thông tin đơn mua HHDV

![Trang 89 — ảnh xem trước để đối chiếu hình vẽ](images/page-89.png)

<!-- Trang 90 -->

![Trang 90 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0090-00.png)


<!-- Trang 91 -->

![Trang 91 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0091-00.png)


<!-- Trang 92 -->

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Collapse/Ex<br>pand|Icon||Collapse<br>d.|Cho phép người dùng đóng<br>mở xem thanh tiến trình của<br>nghiệp vụ<br>Trạng thái expanded:<br>Trạng thái collpased:||
|2|Thanh tiến<br>trình|Proce<br>ss bar|||Hiển thị trạng thái hiện tại của<br>quy trình.<br>Các trạng thái của tiến trình đã<br>được định nghĩa trong<br>.<br>Hiển thị tiến trình theo<br>trường hợp Mua dịch vụ<br>sửa chữa ngoài - Có báo<br>cáo sự cố từ lái xe:<br>Có 4 bước nghiệp vụ:<br>Báo cáo SC<br>Chuẩn đoán<br>Mua HHDV<br>Thanh toán<br>Common Rules||

Icon Collapse

![Trang 92 — ảnh xem trước để đối chiếu hình vẽ](images/page-92.png)

<!-- Trang 93 -->

||||Hiển thị tiến trình theo<br>trường hợp Mua dịch vụ<br>sửa chữa ngoài - Không có<br>báo cáo sự cố từ lái xe:<br>Có 3 bước nghiệp vụ:<br>Chuẩn đoán<br>Mua HHDV<br>Thanh toán<br>All steps disable trừ Báo cáo<br>SC và Mua HHDV để cho<br>phép người dùng ấn vào để<br>xem thông tin bản ghi chi tiết.<br>State của từng step phải được<br>lưu dưới BE để cập nhật đúng<br>trạng thái của từng step.<br>Thanh tiến trình trên chỉ mô tả<br>tiến trình ban đầu, có thể thay<br>đổi tùy theo trường hợp thực<br>tế, chi tiết sẽ được mô tả thêm<br>ở tài liệu tổng hợp các trường<br>hợp thanh tiến trình.|
|---|---|---|---|
|3|Tab|Tab|Hiển thị tab:<br>Thông tin<br>Chi tiết SC|
|4|Thông tin|||
|5|[TT] Thông tin chung|||
|6|Mã đơn<br>hàng|Label|Hiển thị mã đơn HHDV (nếu<br>có)|
|7|Trạng thái|Label|Hiển thị trạng thái hiện tại của<br>đơn mua HHDV|

![](images/ndlxd-export.pdf-0093-02.png)

3 Tab Tab Hiển thị tab:

7 Trạng thái Label Hiển thị trạng thái hiện tại của

![](images/ndlxd-export.pdf-0093-04.png)

![](images/ndlxd-export.pdf-0093-09.png)

<!-- Trang 94 -->

|8|Phân luồng|Label|Hiển thị phân luồng theo từng<br>trường hợp:<br>Sửa chữa xe<br>Sửa chữa phụ tùng|
|---|---|---|---|
|9|Nhà cung<br>cấp|Hyper<br>link|Hiển thị nhà cung cấp HHDV<br>của đơn mua hàng.|
|1<br>0|Số điện<br>thoại|Label|Hiển thị số điện thoại của nhà<br>cung cấp HHDV|
|1<br>1|Địa chỉ|Label|Hiển thị địa chỉ của nhà cung<br>cấp HHDV|
|1<br>2|Phương<br>thức thanh<br>toán|Label|Hiển thị phương thức thanh<br>toán của đơn mua hàng|
|1<br>3|Biển số xe|Label|Hiển thị tên phương tiện sử<br>dụng dịch vụ|
|1<br>4|[TT] Thông tin khác|||
|1<br>5|Tên tài<br>khoản - Tên<br>người phụ<br>trách||Hiển thị tên tài khoản - tên<br>phụ trách của đơn mua HHDV|
|1<br>6|Thời gian<br>sửa chữa||Hiển thị thời gian sửa chữa|
|1<br>7|Ghi chú|Text|Hiển thị ghi chú của đơn mua<br>HHDV|
|1<br>8|Chi tiết đơn|||
|1<br>9|Tab|Tab|Hiển thị tab:<br>Hàng hoá<br>Dịch vụ<br>Hiển thị tổng số item trong<br>từng tab.|

8 Phân luồng Label Hiển thị phân luồng theo từng

1 Địa chỉ Label Hiển thị địa chỉ của nhà cung

1 3 Biển số xe Label Hiển thị tên phương tiện sử

7 Ghi chú Text Hiển thị ghi chú của đơn mua

9 Tab Tab Hiển thị tab:

![](images/ndlxd-export.pdf-0094-01.png)

![](images/ndlxd-export.pdf-0094-02.png)

![](images/ndlxd-export.pdf-0094-03.png)

<!-- Trang 95 -->

|2<br>0|[CTĐ] Chi tiết hàng hoá: Hiển thị chi tiết danh sách hàng hoá mua từ nhà cung cấp HHDV||||
|---|---|---|---|---|
|2<br>1|Expand/Coll<br>apse|Icon|Expande<br>d|Cho phép người dùng mở<br>rông/thu gọn thông tin của<br>card hàng hoá<br>Collapsed:<br>Expanded:|
|2<br>2|Hàng hoá|Card||Hiển thị mã - tên hàng hoá<br>của hàng hoá|
|2<br>3|Icon hàng<br>hoá|Icon||Sử dụng icon để hiển thị theo<br>từng loại hàng hoá như sau:<br>: Công cụ dụng cụ<br>: Phụ tùng vật tư<br>: Lốp<br>: Ắc quy|
|2<br>4|Số lượng|Colu<br>mn|Expande<br>d|Hiển thị số lượng của hàng<br>hoá|
|2<br>5|Thành tiền|Colu<br>mn|Expande<br>d|Hiển thị tổng giá của hàng hoá|
|2<br>6|[CTĐ] Chi tiết dịch vụ: Hiển thị chi tiết danh sách dịch vụ từ nhà cung cấp HHDV||||

![](images/ndlxd-export.pdf-0095-00.png)

Icon Expande

2 2 Hàng hoá Card Hiển thị mã - tên hàng hoá

<!-- Trang 96 -->

![](images/ndlxd-export.pdf-0096-00.png)

|2<br>7|Expand/Coll<br>apse|Icon|Expande<br>d|Cho phép người dùng mở<br>rông/thu gọn thông tin của<br>card hàng hoá<br>Collapsed:<br>Expanded:|
|---|---|---|---|---|
|2<br>8|Dịch vụ|Colu<br>mn||Hiển thị mã dịch vụ của dịch<br>vụ|
|2<br>9|Icon dịch<br>vụ|Icon||Sử dụng icon sau:|
|3<br>0|Số lượng|Colu<br>mn|Expande<br>d|Hiển thị số lượng của dịch vụ|
|3<br>1|Thành tiền|Colu<br>mn|Expande<br>d|Hiển thị tổng giá của dịch vụ|
|3<br>2|Tổng cộng||||
|3<br>3|Expand/Coll<br>apse||Collapse<br>d|Cho phép người dùng mở rộng<br>xem thêm các thông tin về giá<br>tiền tổng.<br>Collapsed:<br>Expanded:|

Icon Expande

Icon Sử dụng icon sau:

<!-- Trang 97 -->

|3<br>4|Tổng giá trị<br>đơn hàng<br>trước thuế||Collapse<br>d|Hiển thị tổng giá trị đơn hàng<br>trước thuế|
|---|---|---|---|---|
|3<br>5|Tiền thuế||Collapse<br>d|Hiển thị tiền thuế của đơn<br>hàng|
|3<br>6|Tổng giá trị<br>đơn hàng<br>sau thuế||Collapse<br>d|Hiển thị tổng giá trị đơn hàng<br>sau thuế|
|3<br>7|Chiết khấu||Collapse<br>d|Hiển thị chiết khấu của đơn<br>hàng|
|3<br>8|Tổng giá trị<br>thanh toán|||Hiển thị tổng giá trị thanh toán<br>của đơn hàng|
|3<br>9|Nghiệm/Từ<br>chối|Butto<br>n|Enable|Cho phép người dùng được<br>phân quyền thực hiện hành<br>động tương ứng.<br>Hiển thị tương ứng theo phân<br>quyền người dùng và trạng<br>thái của đối tượng (xem thêm<br>ở Lưu đồ trạng thái)<br>Người dùng chọn tới hành<br>động để thực hiện UC:<br>Nghiệm thu/từ chối nghiệm<br>thu đơn mua dịch vụ|

3 5 Tiền thuế Collapse

3 7 Chiết khấu Collapse

![Trang 97 — ảnh xem trước để đối chiếu hình vẽ](images/page-97.png)

<!-- Trang 98 -->

|4<br>0|Lịch sử hoạt<br>động|Butto<br>n|Enable|Chọn để hiển thị popup Lịch<br>sử hoạt động, xem thêm ở<br>Thông báo & Lịch sử hoạt<br>động|
|---|---|---|---|---|
|4<br>1||Icon|Enable|Click icon để đóng màn hình,<br>quay lại màn hình Lịch sử đơn<br>mua HHDV|

![](images/ndlxd-export.pdf-0098-01.png)

##### 3.5 Màn hình Thông tin hàng hoá/dịch vụ

![](images/ndlxd-export.pdf-0098-03.png)

||Control|Loại|Trư<br>ờng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tên hàng<br>hoá/dịch vụ|Label|||Hiển thị tên hàng hoá hoặc<br>dịch vụ thêm vào||

<!-- Trang 99 -->

||||Hàng hoá hay dịch vụ tuỳ theo<br>loại đơn mua hàng|
|---|---|---|---|
|2|Mã hàng<br>hoá/dịch vụ|Label|Hiển thị mã hàng hoá hoặc<br>dịch vụ thêm vào<br>Hàng hoá hay dịch vụ tuỳ theo<br>loại đơn mua hàng|
|3|Số lượng|Label|Hiển thị số lượng|
|4|Đơn giá|Label|Hiển thị đơn giá|
|5|Đơn vị tiền<br>tệ|Label|Hiển thị đơn vị tiền tệ|
|6|Tỷ giá|Label|Hiển thị tỷ giá|
|7|Tương<br>đương|Label|Hiển thị tương đương|
|8|Chiết khấu|Label|Hiển thị chiết khấu|
|9|Giá trị chiết<br>khấu|Label|Hiển thị giá trị chiết khấu|
|1<br>0|Giá sau<br>chiết khấu|Label|Hiển thị giá sau chiết khấu|
|1<br>1|Thuế suất|Label|Hiển thị thuế suất|
|1<br>2|Giá trị thuế|Label|Hiển thị giá trị thuế|
|1<br>3|Thành tiền<br>sau thuế|Label|Hiển thị thành tiền sau thuế|
|1<br>4|Tổng giá trị<br>đơn hàng|Label|Hiển thị tổng giá trị đơn hàng|
|1<br>5|Thông tin danh mục của hàng hoá/dịch vụ:<br>Hiển thị thông tin danh mục theo loại hàng hoá/dịch vụ như sau:<br>Hàng hoá<br>Công cụ dụng cụ<br>Loại công cụ dụng cụ|||

3 Số lượng Label Hiển thị số lượng

4 Đơn giá Label Hiển thị đơn giá

Label Hiển thị đơn vị tiền tệ

6 Tỷ giá Label Hiển thị tỷ giá

Label Hiển thị tương đương

8 Chiết khấu Label Hiển thị chiết khấu

1 1 Thuế suất Label Hiển thị thuế suất

1 2 Giá trị thuế Label Hiển thị giá trị thuế

![](images/ndlxd-export.pdf-0099-03.png)

<!-- Trang 100 -->

Đơn vị tính

Phụ tùng vật tư/Lốp/Ắc quy

Loại phương tiện

Mã PT - Tên PT

Hệ thống tổng thành

Đơn vị tính

Dịch vụ:

Dịch vụ kỹ thuật

Loại phương tiện

Mã PT - Tên PT

Hệ thống tổng thành

Đơn vị tính

![](images/ndlxd-export.pdf-0100-00.png)

<!-- Trang 101 -->

### UC02.01.03 - Nghiệm thu/Từ chối nghiệm thu dịch vụ sửa chữa ngoài

#### 1. Thông tin chung

|Mã UC - Tên UC|UC02.01.03 - Nghiệm thu/Từ chối nghiệm thu dịch vụ sửa chữa ngoài|
|---|---|
|Tác nhân|Người dùng ứng dựng lái xe|
|Đường dẫn|Màn hình Thông tin đơn mua dịch vụ (xem): chọn button Nghiệm thu/Từ<br>chối|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta<br>Trạng thái bản ghi là Chờ nghiệm thu|
|Điều kiện sau|Trạng thái của bản ghi thay đổi từ Chờ nghiệm thu → Đã nghiệm thu/Từ<br>chối nghiệm thu<br>Tắt popup Xác nhận nghiệm thu/từ chối và hiển thị màn hình Thông tin<br>đơn mua dịch vụ|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Xác nhận từ chối nghiệm thu

![](images/ndlxd-export.pdf-0101-06.png)

<!-- Trang 102 -->

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Lý do từ<br>chối|Textb<br>ox<br>(Short<br>)|Khô<br>ng||Cho phép người dùng nhập lý<br>do từ chối đơn mua dịch vụ.||
|2|Xác nhận|Butto<br>n||Enable|Cho phép người dùng xác<br>nhận từ chối đơn mua dịch vụ.<br>Sau khi xác nhận,<br>Trạng thái của bản ghi thay<br>đổi từ Chờ nghiệm thu →<br>Đã từ chối<br>Trạng thái của tiến trình<br>chuyển từ Đang triển khai<br>→ Đã hủy/từ chối<br>Gửi thông báo tới người<br>dùng đã tạo/phê duyệt đơn<br>mua dịch vụ này với nội<br>dung:<br>PO - Mua HHDV<br>Đơn mua HHDV - [Loại đơn]<br>đã bị từ chối nghiệm thu.<br>Lưu 1 bản ghi hoạt động mới<br>ở Lịch sử hoạt động:<br>[Tên tài khoản thực hiện hành<br>động] hh:mm dd/mm/yyyy<br>Đã từ chối nghiệm thu.||

![Trang 102 — ảnh xem trước để đối chiếu hình vẽ](images/page-102.png)

<!-- Trang 103 -->

|||||Lý do: [Lý do người dùng<br>nhập]|
|---|---|---|---|---|
|3|Huỷ bỏ|Butto<br>n|Enable|Cho phép người dùng huỷ bỏ<br>việc xác nhận từ chối đơn mua<br>dịch vụ.<br>Sau khi huỷ bỏ,<br>Trạng thái bản ghi giữ<br>nguyên: Chờ nghiệm thu<br>Đóng popup và trở về màn<br>hình Thông tin đơn mua<br>dịch vụ.|

##### 3.2 Màn hình Thông tin đơn mua dịch vụ (Xem) - Trạng thái Từ chối nghiệm thu

![](images/ndlxd-export.pdf-0103-00.png)

Các trường thông tin đã được mô tả ở UC ở đây không có thêm hành

Xem thông tin chi tiết

động ở trạng thái Từ chối nghiệm thu (xem đầy đủ các hành động theo từng trạng thái ở

Lưu đồ

trạng thái

).

##### 3.3 Màn hình Xác nhận nghiệm thu

![](images/ndlxd-export.pdf-0103-02.png)

<!-- Trang 104 -->

![](images/ndlxd-export.pdf-0104-00.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Xác nhận|Butto<br>n||Enable|Cho phép người dùng xác<br>nhận nghiệm thu cấp mới.<br>Sau khi xác nhận,<br>Trạng thái của bản ghi thay<br>đổi từ Chờ nghiệm thu →<br>Đã nghiệm thu<br>Trạng thái của tiến trình<br>chuyển từ Đang triển khai<br>→ Đã hoàn thành<br>Đóng popup Xác nhận<br>nghiệm thu và hiển thị màn<br>hình Thông tin đơn mua<br>dịch vụ.<br>Gửi thông báo tới người<br>dùng đã tạo/phê duyệt đơn<br>mua dịch vụ này với nội<br>dung:<br>PO - Mua HHDV<br>Đơn mua HHDV - [Loại đơn]<br>đã được nghiệm thu.||

<!-- Trang 105 -->

|||||Lưu 1 bản ghi hoạt động mới<br>ở Lịch sử hoạt động:<br>[Tên tài khoản thực hiện hành<br>động] hh:mm dd/mm/yyyy<br>Đã nghiệm thu.|
|---|---|---|---|---|
|2|Huỷ|Butto<br>n|Enable|Cho phép người dùng huỷ bỏ<br>việc xác nhận nghiệm thu đơn<br>mua dịch vụ.<br>Sau khi huỷ bỏ,<br>Trạng thái bản ghi giữ<br>nguyên: Chờ nghiệm thu<br>Đóng popup và trở về màn<br>hình Thông tin đơn mua<br>dịch vụ|

##### 3.4 Màn hình Thông tin đơn mua dịch vụ (Xem) - Trạng thái Đã nghiệm thu

![](images/ndlxd-export.pdf-0105-00.png)

Các trường thông tin đã được mô tả ở UC ở đây không có thêm hành

Xem thông tin chi tiết

động ở trạng thái Đã nghiệm thu (xem đầy đủ các hành động theo từng trạng thái ở

Lưu đồ

trạng thái

).

![](images/ndlxd-export.pdf-0105-02.png)

<!-- Trang 106 -->

## Epic 03 - Lệnh sửa chữa

![](images/ndlxd-export.pdf-0106-01.png)

<!-- Trang 107 -->

### 03 - Thông báo & Lịch sử hoạt động

Danh sách các thông báo và lịch sử hoạt động (chức năng xem thêm ở ) của

Common rules

phần Lệnh sửa chữa như sau:

|Đối<br>tượ|Hệ<br>thống|Thời điểm/<br>Điều kiện|Nội dung thông báo|Đối tượng nhận<br>thông báo|Nội dung lịch sử<br>hoạt động|
|---|---|---|---|---|---|
|ng|trigge<br>r|||||
|Tạo<br>mới|PM<br>Xưởng|Sau khi<br>người<br>dùng tạo<br>thành<br>công lệnh<br>sửa chữa.<br>Loại lệnh<br>SC = sửa<br>chữa<br>xe/thay<br>lốp/thay<br>ắc quy|Lệnh sửa chữa - Tạo<br>mới<br>Lệnh sửa chữa đối với<br>xe [Biển số xe] được<br>bắt đầu triển khai.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng có<br>quyền chốt lệnh<br>sửa chữa và lái xe<br>của phương tiện<br>Delta được đưa<br>vào sửa chữa<br>(trên app Lái xe)|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã tạo lệnh sửa chữa|
||PM<br>Xưởng|Sau khi<br>người<br>dùng tạo<br>thành<br>công lệnh<br>sửa chữa.<br>Loại lệnh<br>SC = phục<br>hồi phụ<br>tùng hỏng|Lệnh sửa chữa - Tạo<br>mới<br>Lệnh sửa chữa -<br>Phục hồi phụ tùng<br>hỏng được bắt đầu<br>triển khai.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng có<br>quyền chốt lệnh<br>sửa chữa.||
|Chốt<br>lệnh|PM<br>Xưởng|Sau khi<br>người<br>dùng chốt|Lệnh sửa chữa -<br>Chốt lệnh<br>Lệnh sửa chữa đối với|Hệ thống PM<br>Xưởng:<br>Hiển thịđối với|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy|
|||thành|Lệnh sửa chữa đối với<br>xe [Biển số xe] đã|Hiển thị đối với<br>người dùng tạo||

|Hệ thống|PM|
|---|---|

|Hệ thống|PM|
|---|---|

|Hệ thống|PM|
|---|---|

![Trang 107 — ảnh xem trước để đối chiếu hình vẽ](images/page-107.png)

<!-- Trang 108 -->

||công lệnh<br>sửa chữa.<br>Loại lệnh<br>SC = sửa<br>chữa<br>xe/thay<br>lốp/thay<br>ắc quy|được chốt lệnh và sẵn<br>sàng nghiệm thu.|chốt lệnh sửa<br>chữa và lái xe của<br>phương tiện Delta<br>được đưa vào<br>sửa chữa (trên<br>app Lái xe)|Đã chốt lệnh sửa<br>chữa|
|---|---|---|---|---|
|PM<br>Xưởng|Sau khi<br>người<br>dùng cập<br>nhật chốt<br>thành<br>công lệnh<br>sửa chữa.<br>Loại lệnh<br>SC = sửa<br>chữa<br>xe/thay<br>lốp/thay<br>ắc quy|Lệnh sửa chữa -<br>Chốt lệnh<br>Lệnh sửa chữa đối với<br>xe [Biển số xe] đã<br>được cập nhật chốt<br>lệnh và sẵn sàng<br>nghiệm thu.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng tạo<br>lệnh sửa chữa.<br>Hệ thống APP Lái<br>xe:<br>Hiển thị đối với<br>người dùng lái xe<br>của phương tiện<br>Delta được đưa<br>vào sửa chữa.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã cập nhật chốt lệnh<br>sửa chữa|
|PM<br>Xưởng|Sau khi<br>người<br>dùng chốt<br>thành<br>công lệnh<br>sửa chữa.<br>Loại lệnh<br>SC = phục<br>hồi phụ<br>tùng hỏng|Lệnh sửa chữa -<br>Chốt lệnh<br>Lệnh sửa chữa -<br>Phục hồi phụ tùng<br>hỏng đã được chốt<br>lệnh.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng tạo<br>chốt lệnh sửa<br>chữa|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã chốt lệnh sửa<br>chữa|
|PM<br>Xưởng|Sau khi<br>người<br>dùng cập<br>nhật chốt|Lệnh sửa chữa -<br>Chốt lệnh<br>Lệnh sửa chữa -<br>Phục hồi phụ tùng|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng tạo|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy|

|Hệ thống|APP Lái|
|---|---|

![](images/ndlxd-export.pdf-0108-00.png)

<!-- Trang 109 -->

|||thành<br>công lệnh<br>sửa chữa.<br>Loại lệnh<br>SC = phục<br>hồi phụ<br>tùng hỏng|hỏng đã được cập<br>nhật chốt lệnh.|chốt lệnh sửa<br>chữa|Đã cập nhật chốt lệnh<br>sửa chữa|
|---|---|---|---|---|---|
|Nghi<br>ệm<br>thu|App<br>Lái xe|Sau khi<br>người dùng<br>từ app Lái xe<br>nghiệm thu<br>thành công<br>lệnh sửa<br>chữa.|Lệnh sửa chữa -<br>Nghiệm thu<br>Lệnh sửa chữa đối với<br>xe [Biển số xe] đã<br>được nghiệm thu<br>thành công.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng tạo<br>chốt lệnh sửa<br>chữa và người có<br>quyền chốt lệnh<br>sửa chữa.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã nghiệm thu lệnh<br>sửa chữa|
||App<br>Lái xe|Sau khi<br>người dùng<br>từ app Lái xe<br>từ chối<br>nghiệm thu<br>thành công<br>lệnh sửa<br>chữa.|Lệnh sửa chữa -<br>Nghiệm thu<br>Lệnh sửa chữa đối với<br>xe [Biển số xe] đã bị<br>từ chối nghiệm thu.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng tạo<br>chốt lệnh sửa<br>chữa và người có<br>quyền chốt lệnh<br>sửa chữa.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã từ chối nghiệm<br>thu lệnh sửa chữa<br>Lý do: [Lý do người<br>dùng nhập khi thực<br>hiện hành động]|

|Hệ thống|PM|
|---|---|

|Hệ thống|PM|
|---|---|

**Các loại lệnh sửa chữa bao gồm:**

Sửa chữa xe Delta/khách hàng

Thay lốp xe Delta/khách hàng

Thay ắc quy xe Delta/khách hàng

Phục hồi phụ tùng hỏng

Điều hướng sau khi nhấn vào thông báo: Dẫn đến màn hình Thông tin lệnh SC

![Trang 109 — ảnh xem trước để đối chiếu hình vẽ](images/page-109.png)

<!-- Trang 110 -->

### 03 - Lưu đồ trạng thái cho lệnh sửa chữa

![](images/ndlxd-export.pdf-0110-01.png)

|Trạng thái|Hệ<br>thống<br>trigger|Thời điểm (Trigger)|Hành động ở PM Xưởng<br>(chưa tính phân quyền)|Hành động ở APP<br>Lái xe|
|---|---|---|---|---|
|Đang sửa<br>chữa|PM<br>Xưởng|Sau khi người dùng<br>hoàn thành tạo lệnh<br>sửa chữa.|Xuất kho (đối với<br>trường hợp sửa chữa<br>xe/thay lốp/thay ắc<br>quy)<br>Chốt lệnh||
|Đã chốt<br>lệnh|PM<br>Xưởng|Sau khi người dùng<br>chốt lệnh sửa chữa.|Cập nhật chốt lệnh|Nghiệm thu<br>Từ chối nghiệm<br>thu|
|Đã nghiệm<br>thu|APP Lái<br>xe|Sau khi người dùng<br>(từ app Lái xe)<br>nghiệm thu lệnh sửa<br>chữa.|Thanh toán (đối với<br>trường hợp trả trước)<br>Nhập kho (nếu có phát<br>sinh khối lượng dư<br>không sử dụng)||
|Từ chối<br>nghiệm thu|APP Lái<br>xe|Sau khi người dùng<br>(từ app Lái xe) từ chối<br>nghiệm thu lệnh sửa<br>chữa.|Cập nhật chốt lệnh||

<!-- Trang 111 -->

![](images/ndlxd-export.pdf-0111-00.png)

<!-- Trang 112 -->

### UC03.01.01 - Xem danh sách lệnh sửa chữa

#### 1. Thông tin chung

|Mã UC - Tên UC|UC03.01.01 - Xem lịch sử sửa chữa|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe|
|Đường dẫn|Màn hình Trang chủ >> chọn card Sửa chữa xe|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hệ thống hiển thị lịch sử sửa chữa thành công.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1. Màn hình Lịch sử sửa chữa

![Trang 112 — ảnh xem trước để đối chiếu hình vẽ](images/page-112.png)

<!-- Trang 113 -->

![](images/ndlxd-export.pdf-0113-00.png)

**Hiển thị lệnh sửa chữa theo các điều kiện sau:**

Là lệnh sửa chữa mà khách hàng = Delta

Phương tiện được sửa chữa là phương tiện của người dùng hiện tại

Trạng thái Đã chốt lệnh SC thì mới hiển thị, sau đó nếu có từ chối thì vẫn keep hiện bản ghi

đấy

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Thanh tìm<br>kiếm|Searc<br>h box|||Cho phép tìm kiếm gần đúng<br>các dữ liệu trong toàn bộ bảng<br>(trừ trạng thái)||
|2|Bộ lọc|Sideb<br>ar|||Xem mô tả phần Common<br>Rules.||

<!-- Trang 114 -->

||||Cho phép lọc các cột sau:<br>Thời gian tạo<br>Người phụ trách<br>Trạng thái|
|---|---|---|---|
|3|Thời gian<br>tạo|Colu<br>mn|Hiển thị thời gian tạo lệnh sửa<br>chữa|
|4|Mã lệnh|Colu<br>mn|Hiển thị mã lệnh sửa chữa|
|5|Người phụ<br>trách|Colu<br>mn|Hiển thị người phụ trách của<br>lệnh sửa chữa|
|6|Trạng thái|Colu<br>mn|Hiển thị trạng thái hiện tại của<br>bản ghi (xem thêm ở<br>)<br>Lưu đồ<br>trạng thái|

![](images/ndlxd-export.pdf-0114-01.png)

<!-- Trang 115 -->

### UC03.01.02 - Xem thông tin chi tiết lệnh sửa chữa

#### 1. Thông tin chung

|Mã UC - Tên UC|UC05.06.02 - Xem thông tin lệnh sửa chữa|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe Delta|
|Đường dẫn|Màn hình Danh sách lệnh sửa chữa > Nhấn vào 1 bản ghi trong bảng:<br>Hiển thị màn hình thông tin lệnh sửa chữa|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hiển thị thông tin chi tiết lệnh sửa chữa thành công.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Thông tin Lệnh sửa chữa

![](images/ndlxd-export.pdf-0115-06.png)

<!-- Trang 116 -->

![Trang 116 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0116-00.png)


<!-- Trang 117 -->

![](images/ndlxd-export.pdf-0117-00.png)

**Thông tin Lệnh sửa chữa bao gồm:**

Thông tin chung

Thông tin phương tiện

Chi tiết hàng hoá/dịch vụ

Thông tin khác

Tổng cộng

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Collapse/Ex<br>pand|Icon||Collapse<br>d.|Cho phép người dùng đóng<br>mở xem thanh tiến trình của<br>nghiệp vụ<br>Trạng thái expanded:<br>Trạng thái collpased:||

Icon Collapse

<!-- Trang 118 -->

|2|Thanh tiến<br>trình|Proce<br>ss bar|Hiển thị trạng thái hiện tại của<br>quy trình.<br>Các trạng thái của tiến trình<br>đã được định nghĩa trong<br>.<br>Hiển thị tiến trình theo từng<br>trường hợp:<br>Hiển thị tiến trình theo<br>trường hợp Không có báo<br>cáo sự cố:<br>Có 3 bước nghiệp vụ:<br>Chuẩn đoán<br>Sửa chữa<br>Xuất kho<br>Hiển thị tiến trình theo<br>trường hợp Có báo cáo sự<br>cố:<br>Có 4 bước nghiệp vụ:<br>Báo cáo sự cố<br>Chuẩn đoán<br>Sửa chữa<br>Xuất kho<br>All steps disable trừ Báo cáo<br>SC và Lệnh SC để cho phép<br>người dùng ấn vào để xem<br>thông tin bản ghi chi tiết.<br>Common Rules|
|---|---|---|---|

![Trang 118 — ảnh xem trước để đối chiếu hình vẽ](images/page-118.png)

<!-- Trang 119 -->

|||||State của từng step phải được<br>lưu dưới BE để cập nhật đúng<br>trạng thái của từng step.<br>Thanh tiến trình trên chỉ mô tả<br>tiến trình ban đầu, có thể thay<br>đổi tùy theo trường hợp thực<br>tế, chi tiết sẽ được mô tả thêm<br>ở tài liệu tổng hợp các trường<br>hợp thanh tiến trình.|
|---|---|---|---|---|
|3|Tab|Tab|Chung|Chia tab:<br>Chung<br>Chi tiết SC|
|4|[Chung] Thông tin chung||||
|5|Trạng thái|Label||Hiển thị trạng thái hiện tại của<br>lệnh sửa chữa|
|6|Mã sửa<br>chữa|Label||Hiển thị mã lệnh sửa chữa|
|7|Phân luồng|Label||Hiển thị trường hợp phân<br>luồng hiện tại của Lệnh sửa<br>chữa, bao gồm:<br>Sửa xe<br>Thay lốp<br>Thay ắc quy<br>→ Tuỳ thuộc vào trường hợp<br>người dùng chọn khi tạo Lệnh<br>sửa chữa.|
|8|Biển số xe|Hyper<br>link||Hiển thị biển số xe của<br>phương tiện sử dụng dịch vụ.|
|9|Số kms|Label||Hiển thị số kms hiện tại của xe<br>khi đưa vào sửa chữa|
|1<br>0|Mô tả sự cố|Label||Hiển thị mô tả sự cố theo báo<br>cáo sự cố/yêu cầu sửa chữa|

3 Tab Tab Chung Chia tab:

5 Trạng thái Label Hiển thị trạng thái hiện tại của

7 Phân luồng Label Hiển thị trường hợp phân

9 Số kms Label Hiển thị số kms hiện tại của xe

1 0 Mô tả sự cố Label Hiển thị mô tả sự cố theo báo

![](images/ndlxd-export.pdf-0119-01.png)

![](images/ndlxd-export.pdf-0119-02.png)

<!-- Trang 120 -->

|||||từ app Lái xe.|
|---|---|---|---|---|
|1<br>1|[Chung] Thông tin khác||||
|1<br>2|Người phụ<br>trách|||Hiển thị mã NV - tên người<br>phụ trách của Lệnh sửa chữa|
|1<br>3|Thời gian<br>sửa chữa|||Hiển thị thời gian sửa chữa|
|1<br>4|Ghi chú|Text||Hiển thị ghi chú của Lệnh sửa<br>chữa|
|1<br>5|Chi tiết sửa chữa: Bao gồm 2 tab: Hàng hoá, dịch vụ.||||
|1<br>6|Tab|Tab||Hiển thị tab đang được hiển thị<br>tương ứng<br>Hàng hoá<br>Dịch vụ<br>Thể hiện số lượng hàng<br>hoá/dịch vụ/số lần xuất kho ở<br>cuối tên tab.<br>Ví dụ: Phụ tùng vật tư (3)|
|1<br>7|[CTSC] Chi tiết hàng hoá: Hiển thị chi tiết danh sách hàng hoá tổng hợp sau khi chốt lệnh<br>sửa chữa mà cung cấp/sửa chữa cho phương tiện.||||
|1<br>8|Sub-tab|Tab|Thay ra|Hiển thị tab của hàng hoá<br>Thay ra<br>Lắp vào|
|1<br>9|Xem sơ đồ<br>lốp|Butto<br>n||Hiển thị màn hình Sơ đồ lốp<br>của phương tiện (sơ đồ hiện<br>tại - sau khi đã chốt lệnh SC)<br>Chỉ trong trường hợp loại sửa<br>chữa = thay lốp.|
|2<br>0|[CTSC] [HH] Thay ra: Hiển thị danh sách các hàng hoá được thay ra khỏi phương tiện Delta.||||

1 4 Ghi chú Text Hiển thị ghi chú của Lệnh sửa

1 6 Tab Tab Hiển thị tab đang được hiển thị

![](images/ndlxd-export.pdf-0120-03.png)

![](images/ndlxd-export.pdf-0120-04.png)

![](images/ndlxd-export.pdf-0120-06.png)

<!-- Trang 121 -->

**UI mỗi bản ghi:**

![](images/ndlxd-export.pdf-0121-01.png)

|2<br>1|Phụ tùng<br>vật tự/lốp/<br>ắc quy|Colu<br>mn||Hiển thị mã-tên hàng hoá của<br>hàng hoá được ghi nhận thay<br>ra khỏi phương tiện khi chốt<br>lệnh SC|
|---|---|---|---|---|
|2<br>2|ĐVT|Colu<br>mn||Hiển thị đơn vị tính của hàng<br>hoá được ghi nhận thay ra<br>khỏi phương tiện khi chốt lệnh<br>SC|
|2<br>3|Số lượng|Colu<br>mn||Hiển thị số lượng của hàng<br>hoá được ghi nhận thay ra<br>khỏi phương tiện khi chốt lệnh<br>SC|
|2<br>4|Collapse/Ex<br>pand|Icon|Collapse<br>d|Cho phép người dùng ẩn hiện<br>các thông tin serial của hàng<br>hoá|
|2<br>5|Serial|Colu<br>mn||Hiển thị serial của từng sản<br>phẩm|
|2<br>6|Nhà sản<br>xuất|Colu<br>mn||Hiển thị nhà sản xuất của từng<br>sản phẩm|
|2<br>7|Lưu ý|Colu<br>mn||Hiển thị lưu ý của từng sản<br>phẩm|
|2<br>8|[CTSC] [HH] Lắp vào: Hiển thị danh sách các hàng hoá được lắp vào phương tiện.<br>Hàng hoá sẽ được tổng hợp từ số lượng sử dụng (=số lượng xuất - số lượng thừa - số lượng<br>hỏng) của hàng xuất kho + số lượng sử dụng của hàng xuất từ xưởng.<br>UI mỗi bản ghi:||||

Icon Collapse

![](images/ndlxd-export.pdf-0121-03.png)

<!-- Trang 122 -->

![](images/ndlxd-export.pdf-0122-02.png)

|2<br>9|Phụ tùng<br>vật tư/lốp/<br>ắc quy|Label||Hiển thị mã-tên hàng hoá của<br>hàng hoá|
|---|---|---|---|---|
|3<br>0|ĐVT|Label||Hiển thị đơn vị tính của hàng<br>hoá|
|3<br>1|Số lượng|Label||Hiển thị tổng số lượng lắp vào<br>của hàng hoá|
|3<br>2|Thành tiền|Label||Hiển thị thành tiền của hàng<br>hoá.<br>Lấy theo giá trị = số lượng *<br>đơn giá của hàng hoá đó.|
|3<br>3|Collapse/Ex<br>pand|Icon|Collapse<br>d|Cho phép người dùng ẩn hiện<br>các thông tin của hàng hóa<br>(Đơn vị tính/số lượng)|
|3<br>4|Chi tiết dịch vụ: Hiển thị chi tiết danh sách dịch vụ mà xưởng hiện tại cung cấp cho lệnh sửa<br>chữa.||||
|3<br>5|Dịch vụ|Colu<br>mn||Hiển thị mã-tên dịch vụ của<br>dịch vụ|
|3<br>6|Số lượng|Colu<br>mn||Hiển thị số lượng của dịch vụ|
|3<br>7|Thành tiền|Colu<br>mn||Hiển thị tổng giá của dịch vụ|
|3<br>8|Tổng cộng||||

3 0 ĐVT Label Hiển thị đơn vị tính của hàng

3 1 Số lượng Label Hiển thị tổng số lượng lắp vào

2 Thành tiền Label Hiển thị thành tiền của hàng

Icon Collapse

![](images/ndlxd-export.pdf-0122-06.png)

<!-- Trang 123 -->

|3<br>9|Tổng giá trị<br>sửa chữa|||Hiển thị tổng giá trị sửa chữa<br>của Lệnh sửa chữa<br>Lấy giá trị bằng = tổng thành<br>tiền của các hàng hoá lắp vào<br>từ kho và danh mục xưởng +<br>tổng thành tiền của dịch vụ.|
|---|---|---|---|---|
|4<br>0|Từ<br>chối/Nghiệ<br>m thu|Butto<br>n|Enable|Cho phép người dùng được<br>phân quyền thực hiện hành<br>động tương ứng.<br>Hiển thị tương ứng theo phân<br>quyền người dùng và trạng<br>thái của đối tượng (xem thêm<br>ở<br>Người dùng chọn tới hành<br>động để thực hiện 1 trong các<br>UC:<br>Lưu đồ trạng thái của Danh<br>mục)<br>Nghiệm thu/từ chối nghiệm<br>thu lệnh sửa chữa|
|4<br>1|Lịch sử hoạt<br>động|Butto<br>n|Enable|Chọn để hiển thị popup Lịch<br>sử hoạt động, xem thêm ở<br>Thông báo & Lịch sử hoạt<br>động|
|4<br>2||Icon|Enable|Click icon để đóng màn hình,<br>quay lại màn hình Lịch sử sửa<br>chữa|

##### 3.2 Màn hình Sơ đồ lốp

![](images/ndlxd-export.pdf-0123-01.png)

<!-- Trang 124 -->

![](images/ndlxd-export.pdf-0124-00.png)

Cho phép người dùng ấn vào từng lốp để xem thông tin chi tiết của quả lốp đó.

![](images/ndlxd-export.pdf-0124-02.png)

<!-- Trang 125 -->

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1||Icon|||Cho phép người dùng xem<br>chú thích cho sơ đồ lốp.<br>Hệ thống hiển thị popup Chú<br>thích||
|2||Icon||Enable|Click icon để đóng màn hình,<br>quay lại màn hình Thông tin<br>sửa chữa||
|3|Thông tin serial<br>→ Lấy các thông tin trên từ lệnh sửa chữa lốp mới nhất (nếu có) hoặc thông tin của PT (cập<br>nhật).||||||
|4|Icon lốp|Icon|||Hiển thị icon theo lốp được<br>chọn||
|5|Serial lốp|Label|||Hiển thị serial của lốp tương<br>ứng được chọn||
|6|Lốp|Label|||Hiển thị tên - mã lốp tương<br>ứng được chọn||
|7|Vị trí|Label|||Hiển thị vị trí lốp trên sơ đồ lốp<br>của phương tiện||
|8|Ngày lắp lên<br>phương tiện|Label|||Hiển thị ngày lắp lốp lên PT -<br>lấy theo ngày chốt lệnh SC||

1 Icon Cho phép người dùng xem

![](images/ndlxd-export.pdf-0125-00.png)

4 Icon lốp Icon Hiển thị icon theo lốp được

5 Serial lốp Label Hiển thị serial của lốp tương

6 Lốp Label Hiển thị tên - mã lốp tương

7 Vị trí Label Hiển thị vị trí lốp trên sơ đồ lốp

<!-- Trang 126 -->

|9|Vị trí tráo<br>đổi|Label|Hiển thị vị trí trao đổi trước đó<br>của lốp<br>Hiện trường này nếu tráo đổi<br>vị trí|
|---|---|---|---|

##### 3.3 Màn hình Chú thích

![](images/ndlxd-export.pdf-0126-01.png)

##### 3.4 Màn hình Serial

![](images/ndlxd-export.pdf-0126-03.png)

<!-- Trang 127 -->

![](images/ndlxd-export.pdf-0127-00.png)

**Hiển thị mỗi bản ghi serial thành 1 card con.**

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tên popup||||Hiển thị tên popup theo tên<br>hàng hóa được chọn xem<br>serial con<br>Format:<br>Mã - tên hàng hóa||
|2|Serial|Colu<br>mn|||Hiển thị serial của từng sản<br>phẩm||
|3|Nhà sản<br>xuất|Colu<br>mn|||Hiển thị nhà sản xuất của từng<br>sản phẩm||
|4|Lưu ý|Colu<br>mn|||Hiển thị lưu ý của từng sản<br>phẩm||

1 Tên popup Hiển thị tên popup theo tên

<!-- Trang 128 -->

### UC03.01.03 - Nghiệm thu/Từ chối nghiệm thu lệnh sửa chữa nội bộ

#### 1. Thông tin chung

|Mã UC - Tên UC|UC03.01.03 - Nghiệm thu/Từ chối nghiệm thu lệnh sửa chữa nội bộ|
|---|---|
|Tác nhân|Người dùng ứng dụng lái xe|
|Đường dẫn|Màn hình Thông tin lệnh sửa chữa nội bộ (xem): chọn button Nghiệm<br>thu/Từ chối|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta<br>Trạng thái bản ghi là Chờ nghiệm thu|
|Điều kiện sau|Trạng thái của bản ghi thay đổi từ Chờ nghiệm thu → Đã nghiệm thu/Từ<br>chối nghiệm thu<br>Tắt popup Xác nhận nghiệm thu/từ chối và hiển thị màn hình Thông tin<br>lệnh sửa chữa nội bộ|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Xác nhận từ chối nghiệm thu

![Trang 128 — ảnh xem trước để đối chiếu hình vẽ](images/page-128.png)

<!-- Trang 129 -->

![](images/ndlxd-export.pdf-0129-00.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Lý do từ<br>chối|Textb<br>ox<br>(Short<br>)|Khô<br>ng||Cho phép người dùng nhập lý<br>do từ chối lệnh sửa chữa nội<br>bộ.||
|2|Từ chối|Butto<br>n||Enable|Cho phép người dùng xác<br>nhận từ chối lệnh sửa chữa nội<br>bộ.<br>Sau khi xác nhận,<br>Trạng thái của bản ghi thay<br>đổi từ Chờ nghiệm thu →<br>Đã từ chối<br>Trạng thái của tiến trình<br>chuyển từ Đang triển khai<br>→ Đã huỷ/từ chối||

<!-- Trang 130 -->

![](images/ndlxd-export.pdf-0130-00.png)

|||||Gửi thông báo tới người<br>dùng đã tạo/chốt lệnh sửa<br>chữa nội bộ này với nội<br>dung:<br>Lệnh sửa chữa - Nghiệm thu<br>Lệnh sửa chữa đối với xe<br>[Biển số xe] đã bị từ chối<br>nghiệm thu.<br>Lưu 1 bản ghi hoạt động mới<br>ở Lịch sử hoạt động:<br>[Tên tài khoản thực hiện hành<br>động] hh:mm dd/mm/yyyy<br>Đã từ chối nghiệm thu.<br>Lý do: [Lý do người dùng<br>nhập]|
|---|---|---|---|---|
|3|Huỷ bỏ|Butto<br>n|Enable|Cho phép người dùng huỷ bỏ<br>việc xác nhận từ chối lệnh sửa<br>chữa nội bộ.<br>Sau khi huỷ bỏ,<br>Trạng thái bản ghi giữ<br>nguyên: Chờ nghiệm thu<br>Đóng popup và trở về màn<br>hình Thông tin lệnh sửa<br>chữa nội bộ.|

##### 3.2 Màn hình Thông tin lệnh sửa chữa nội bộ (Xem) - Trạng thái Từ chối nghiệm thu

![](images/ndlxd-export.pdf-0130-02.png)

<!-- Trang 131 -->

![](images/ndlxd-export.pdf-0131-00.png)

Các trường thông tin đã được mô tả ở UC ở đây không có thêm hành

Xem thông tin chi tiết

động ở trạng thái Từ chối nghiệm thu (xem đầy đủ các hành động theo từng trạng thái ở

Lưu đồ

trạng thái

).

##### 3.3 Màn hình Xác nhận nghiệm thu

![](images/ndlxd-export.pdf-0131-03.png)

<!-- Trang 132 -->

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Xác nhận|Butto<br>n||Enable|Cho phép người dùng xác<br>nhận nghiệm thu cấp mới.<br>Sau khi xác nhận,<br>Trạng thái của bản ghi thay<br>đổi từ Chờ nghiệm thu →<br>Đã nghiệm thu<br>Trạng thái của tiến trình<br>chuyển từ Đang triển khai<br>→ Đã hoàn thành<br>Đóng popup Xác nhận<br>nghiệm thu và hiển thị màn<br>hình Thông tin lệnh sửa<br>chữa nội bộ.<br>Gửi thông báo tới người<br>dùng đã tạo/chốt lệnh sửa<br>chữa nội bộ này với nội<br>dung:<br>Lệnh sửa chữa - Nghiệm thu<br>Lệnh sửa chữa đối với xe<br>[Biển số xe] đã được nghiệm<br>thu thành công.<br>Lưu 1 bản ghi hoạt động mới<br>ở Lịch sử hoạt động:<br>[Tên tài khoản thực hiện hành<br>động] hh:mm dd/mm/yyyy<br>Đã nghiệm thu.||

![Trang 132 — ảnh xem trước để đối chiếu hình vẽ](images/page-132.png)

<!-- Trang 133 -->

|2|Huỷ bỏ|Butto<br>n|Enable|Cho phép người dùng huỷ bỏ<br>việc xác nhận nghiệm thu lệnh<br>sửa chữa nội bộ.<br>Sau khi huỷ bỏ,<br>Trạng thái bản ghi giữ<br>nguyên: Chờ nghiệm thu<br>Đóng popup và trở về màn<br>hình Thông tin lệnh sửa<br>chữa nội bộ|
|---|---|---|---|---|

##### 3.4 Màn hình Thông tin lệnh sửa chữa nội bộ (Xem) - Trạng thái Đã nghiệm thu

![](images/ndlxd-export.pdf-0133-00.png)

Các trường thông tin đã được mô tả ở UC ở đây không có thêm hành

Xem thông tin chi tiết

động ở trạng thái Đã nghiệm thu (xem đầy đủ các hành động theo từng trạng thái ở

Lưu đồ

trạng thái

).

![](images/ndlxd-export.pdf-0133-02.png)

<!-- Trang 134 -->

## Epic 04 - Báo cáo sự cố & Thanh toán chi phí lái xe

![](images/ndlxd-export.pdf-0134-01.png)

<!-- Trang 135 -->

### 04 - Thông báo & Lịch sử hoạt động

Danh sách các thông báo và lịch sử hoạt động (chức năng xem thêm ở ) của

Common rules

phần Báo cáo sự cố như sau:

|Đối<br>tượ|Hệ<br>thống|Thời điểm/Điều<br>kiện|Nội dung thông báo|Đối tượng nhận<br>thông báo|Nội dung lịch sử<br>hoạt động|
|---|---|---|---|---|---|
|ng|trigge<br>r|||||
|Tạo<br>mới|App<br>Lái xe|Sau khi người<br>dùng tạo thành<br>công bản ghi.|Báo cáo sự cố<br>Báo cáo sự cố cho<br>phương tiện [Biển số<br>xe] đang chờ phê<br>duyệt.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng có<br>quyền xác<br>nhận/chuẩn<br>đoán/từ chối<br>bản ghi.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã tạo mới báo cáo<br>sự cố.|
||App<br>Lái xe|Sau khi người<br>dùng thu hồi<br>thành công bản<br>ghi.|Báo cáo sự cố<br>Báo cáo sự cố cho<br>phương tiện [Biển số<br>xe] đã bị thu hồi.|Hệ thống PM<br>Xưởng:<br>Hiển thị đối với<br>người dùng có<br>quyền xác<br>nhận/chuẩn<br>đoán/từ chối<br>bản ghi.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã thu hồi báo cáo<br>sự cố.|
||PM<br>Xưởn<br>g|Sau khi người<br>dùng xác nhận<br>thành công<br>bản ghi.<br>Báo cáo sự cố<br>có cách giải<br>quyết = lái xe|Báo cáo sự cố<br>Báo cáo sự cố cho<br>phương tiện [Biển số<br>xe] đã bị từ chối.|Hệ thống App<br>Lái xe:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã xác nhận báo<br>cáo sự cố.|
||PM|Sau khi người|Báo cáo sựcố|Hệthống App|[Tên tài khoản thực|
||Xưởn|Sau<br>gườ<br>dùng từ chối|áo cáo sựcố|ệt ốg<br>pp<br>Lái xe:|[ ê<br>tà<br>oả<br>t ực<br>hiện hành động]|

![Trang 135 — ảnh xem trước để đối chiếu hình vẽ](images/page-135.png)

<!-- Trang 136 -->

||g|thành công yêu<br>cầu tạo.|Báo cáo sự cố cho<br>phương tiện [Biển số<br>xe] đã được xác<br>nhận.|Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới.|hh:mm dd/mm/yyyy<br>Đã từ chối báo cáo<br>sự cố.<br>Lý do: [Lý do người<br>dùng nhập khi thực<br>hiện hành động]|
|---|---|---|---|---|---|
|Chu<br>ẩn<br>đoá<br>n|PM<br>Xưởn<br>g|Sau khi người<br>dùng phê<br>duyệt thành<br>công bản ghi<br>báo giá tương<br>ứng.<br>Báo cáo sự cố<br>có cách giải<br>quyết = xưởng|Báo cáo sự cố<br>Báo cáo sự cố cho<br>phương tiện [Biển số<br>xe] đã được chuẩn<br>đoán.|Hệ thống App<br>Lái xe:<br>Hiển thị đối với<br>người dùng đã<br>tạo yêu cầu tạo<br>mới.|[Tên tài khoản thực<br>hiện hành động]<br>hh:mm dd/mm/yyyy<br>Đã chuẩn đoán sự<br>cố.|

**Điều hướng sau khi nhấn vào thông báo: Dẫn đến màn hình Thông tin báo cáo sự cố.**

![Trang 136 — ảnh xem trước để đối chiếu hình vẽ](images/page-136.png)

<!-- Trang 137 -->

### 04 - Lưu đồ trạng thái cho báo cáo sự cố

![](images/ndlxd-export.pdf-0137-01.png)

|Trạng thái|Nơi<br>xuất<br>phát<br>hành<br>động|Thời điểm (Trigger)|Hành động ở PM<br>Xưởng (chưa tính<br>phân quyền)|Hành động ở APP Lái<br>xe|
|---|---|---|---|---|
|Đang chờ xử<br>lý|App Lái<br>xe|Sau khi người dùng<br>hoàn thành tạo mới<br>báo cáo sự cố.|Xác nhận (PMX)<br>nếu cách giải quyết<br>= lái xe<br>Chuẩn đoán (PMX)<br>nếu cách giải quyết<br>= xưởng<br>Từ chối (PMX)|Thu hồi (ALX)|
|Đang xử lý|PM<br>Xưởng|Sau khi người dùng<br>hoàn thành tạo mới<br>báo giá chuẩn đoán.|||
|Đã thu hồi|App Lái<br>xe|Sau khi người dùng<br>thu hồi báo cáo sự<br>cố.||Tạo lại (ALX)<br>Xoá (ALX)|

<!-- Trang 138 -->

|Đã chuẩn<br>đoán|PM<br>Xưởng|Sau khi người dùng<br>phê duyệt báo giá<br>tương ứng với báo<br>cáo sự cố.||
|---|---|---|---|
|Đã xác nhận|PM<br>Xưởng|Sau khi người dùng<br>xác nhận báo cáo<br>sự cố.||
|Đã từ chối|PM<br>Xưởng|Sau khi người dùng<br>từ chối báo cáo sự<br>cố.|Tạo lại (ALX)<br>Xoá (ALX)|

![Trang 138 — ảnh xem trước để đối chiếu hình vẽ](images/page-138.png)

<!-- Trang 139 -->

### UC04.01.01 - Xem danh sách báo cáo sự cố

#### 1. Thông tin chung

|Mã UC - Tên UC|UC05.07.01 - Xem danh sách báo cáo sự cố|
|---|---|
|Tác nhân|Người dùng app Lái xe|
|Đường dẫn|Dashboards > Tab Báo cáo sự cố|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hệ thống hiển thị lịch sử báo cáo sự cố thành công.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1. Màn hình Lịch sử báo cáo sự cố

![Trang 139 — ảnh xem trước để đối chiếu hình vẽ](images/page-139.png)

<!-- Trang 140 -->

![](images/ndlxd-export.pdf-0140-00.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Thanh tìm<br>kiếm|Searc<br>h box|||Cho phép tìm kiếm gần đúng<br>các dữ liệu trong toàn bộ bảng<br>(trừ trạng thái)||
|2|Bộ lọc|Sideb<br>ar|||Xem mô tả phần<br>Cho phép lọc các cột sau:<br>Thời gian phát hiện sự cố<br>Hệ thống tổng thành<br>Phân loại chi phí<br>Cách giải quyết<br>Common<br>Rules||

<!-- Trang 141 -->

||||Số tiền<br>Sửa tại<br>Địa điểm SC<br>Trạng thái||
|---|---|---|---|---|
|3|Thời gian<br>phát hiện<br>sự cố|Label|Hiển thị thời gian phát hiện sự<br>cố||
|4|Mã báo cáo<br>sự cố|Label|Hiển thị mã báo cáo sự cố||
|5|Cách giải<br>quyết|Label|Hiển thị cách giải quyết||
|6|Số tiền|Label|Hiển thị số tiền||
|7|Trạng thái|Label|Hiển thị trạng thái hiện tại của<br>bản ghi (xem thêm ở<br>)<br>Lưu đồ<br>trạng thái||
|8|Tạo mới|Butto<br>n|Cho phép người dụng tạo 1<br>báo cáo sự cố mới gửi về<br>PMX.<br>Hệ thống thực hiện UC<br>.<br>Tạo<br>mới báo cáo sự cố|Validate xe không có<br>ID xe hoặc có ID xe<br>nhưng không lấy<br>được biển số xe thì<br>hệ thống báo lỗi:|

Label Hiển thị cách giải quyết

6 Số tiền Label Hiển thị số tiền

7 Trạng thái Label Hiển thị trạng thái hiện tại của

![](images/ndlxd-export.pdf-0141-01.png)

<!-- Trang 142 -->

### UC04.01.02 - Xem chi tiết báo cáo sự cố

#### 1. Thông tin chung

|Mã UC - Tên UC|UC04.01.02 - Xem chi tiết báo cáo sự cố|
|---|---|
|Tác nhân|Người dùng phần mềm xưởng|
|Đường dẫn|Màn hình Lịch sử báo cáo sự cố > Nhấn vào 1 bản ghi trong bảng: Hiển<br>thị màn hình thông tin báo cáo sự cố|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hiển thị thông tin chi tiết báo cáo sự cố.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Thông tin báo cáo sự cố

![Trang 142 — ảnh xem trước để đối chiếu hình vẽ](images/page-142.png)

<!-- Trang 143 -->

![Trang 143 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0143-00.png)


<!-- Trang 144 -->

![](images/ndlxd-export.pdf-0144-00.png)

Thông tin báo cáo sự cố bao gồm:

Thông tin sự cố

Giải quyết sự cố

Thông tin khác

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Collapse/Ex<br>pand|Icon||Collapse<br>d.|Cho phép người dùng đóng<br>mở xem thanh tiến trình của<br>nghiệp vụ<br>Trạng thái expanded:<br>Trạng thái collpased:||

Icon Collapse

<!-- Trang 145 -->

|2|Thanh tiến<br>trình|Proce<br>ss bar|Hiển thị trạng thái hiện tại của<br>quy trình.<br>Các trạng thái của tiến trình<br>đã được định nghĩa trong<br>.<br>Hiển thị tiến trình theo từng<br>trường hợp:<br>Hiển thị tiến trình theo<br>trường hợp Cách giải quyết<br>= Xưởng:<br>Có 3 bước nghiệp vụ (ban<br>đầu):<br>Báo sự cố<br>Báo giá chuẩn đoán<br>N/A<br>Trường hợp Cách giải quyết<br>= Lái xe không hiển thị<br>thanh tiến trình.<br>All steps disable trừ Báo cáo<br>SC và Mua HHDV để cho<br>phép người dùng ấn vào để<br>xem thông tin bản ghi chi tiết.<br>State của từng step phải được<br>lưu dưới BE để cập nhật đúng<br>trạng thái của từng step.<br>Thanh tiến trình trên chỉ mô tả<br>tiến trình ban đầu, có thể thay<br>đổi tùy theo trường hợp thực<br>tế, chi tiết sẽ được mô tả thêm<br>Common Rules|
|---|---|---|---|

![Trang 145 — ảnh xem trước để đối chiếu hình vẽ](images/page-145.png)

<!-- Trang 146 -->

||||ở tài liệu tổng hợp các trường<br>hợp thanh tiến trình.|
|---|---|---|---|
|3|Thông tin sự cố|||
|4|Trạng thái|Label|Hiển thị trạng thái hiện tại của<br>báo cáo sự cố|
|5|Mã sự cố|Label|Hiển thị mã báo cáo sự cố<br>(nếu có)|
|6|Biển số xe|Label|Hiển thị tên phương tiện báo<br>cáo sự cố|
|7|Hoạt động<br>thực hiện|Label|Hiển thị tên hoạt động nhắc<br>lịch tương ứng được làm đầu<br>vào để tạo báo cáo sự cố.<br>Chỉ hiển thị khi tạo báo cáo<br>sự cố từ 1 lịch nhắc.|
|8|Hệ thống<br>tồng thành|Label|Hiển thị hệ thống tổng thành<br>được chọn khi tạo báo cáo sự<br>cố.|
|9|Mô tả sự cố|Label|Hiển thị mô tả sự cố được điền<br>khi tạo báo cáo sự cố.|
|1<br>0|Vị trí hiện<br>tại|Label|Hiển thị vị trí hiện tại khi tạo<br>báo cáo sự cố.|
|1<br>1|Hình ảnh sự<br>cố và<br>chứng từ<br>thanh toán|Imag<br>e|Hiển thị các hình ảnh và<br>chứng từ sự cố tại thời điểm<br>bàn giao ở dạng preview.<br>Cho phép người dùng điều<br>hướng trước sau bằng cách<br>scroll ngang.<br>Hiển thị ảnh 1 dòng, nếu nhiều<br>hơn 3 bản ghi thì cho scroll<br>ngang.|

4 Trạng thái Label Hiển thị trạng thái hiện tại của

5 Mã sự cố Label Hiển thị mã báo cáo sự cố

6 Biển số xe Label Hiển thị tên phương tiện báo

9 Mô tả sự cố Label Hiển thị mô tả sự cố được điền

![](images/ndlxd-export.pdf-0146-01.png)

![](images/ndlxd-export.pdf-0146-02.png)

<!-- Trang 147 -->

||||Cho phép người dùng ấn vào<br>ảnh hoặc ấn vào icon Phóng<br>to để xem ảnh lớn hơn.|
|---|---|---|---|
|1<br>2|Giải quyết sự cố:<br>Nếu cách giải quyết = lái xe, hiển thị UI như sau:<br>Nếu cách giải quyết = xưởng, hiển thị UI no data ban đầu:<br>Khi ở trạng thái Đã chuẩn đoán, hiển thị UI như sau:|||
|1<br>3|Cách giải<br>quyết|Label|Hiển thị cách giải quyết lái xe<br>chọn khi tạo báo cáo sự cố<br>Giá trị:<br>Lái xe<br>Xưởng|
|1<br>4|Sửa tại|Label|Hiển thị nơi sửa chung được<br>quyết định sau khi xưởng<br>chuẩn đoán (hoàn thành báo<br>giá).<br>Giá trị:<br>Xưởng Delta<br>Xưởng đối tác|

![](images/ndlxd-export.pdf-0147-00.png)

4 Sửa tại Label Hiển thị nơi sửa chung được

<!-- Trang 148 -->

||||Hiển thị khi ở trạng thái Đã<br>chuẩn đoán và cách giải<br>quyết = xưởng.|
|---|---|---|---|
|1<br>5|Địa điểm<br>sửa chữa|Label|Hiển thị địa điểm sửa chữa<br>cho phương tiện báo cáo sự<br>cố.<br>Hiển thị tên nhà cung cấp<br>HHDV nếu sửa tại = xưởng đối<br>tác.<br>Hiển thị tên xưởng Delta được<br>chọn nếu sửa tại xưởng Delta.<br>Hiển thị khi ở trạng thái Đã<br>chuẩn đoán và cách giải<br>quyết = xưởng.|
|1<br>6|Số tiền|Label|Hiển thị số tiền của báo cáo<br>sự cố.<br>Hiển thị nếu cách giải quyết =<br>lái xe.|
|1<br>7|Phân loại<br>chi phí|Label|Hiển thị phân loại chi phí được<br>chọn khi tạo báo cáo sự cố.<br>Hiển thị nếu cách giải quyết =<br>lái xe.|
|1<br>8|Thông tin khác|||
|1<br>9|Lái xe|Label|Hiển thị tên lái xe|
|2<br>0|Thời gian<br>phát hiện<br>sự cố|Label|Hiển thị thời gian phát hiện sự<br>cố của báo cáo sự cố.|
|2<br>1|Ghi chú|Label|Hiển thị ghi chú của báo cáo<br>sự cố.<br>Nếu không có thì không hiển<br>thị lên giao diện.|

6 Số tiền Label Hiển thị số tiền của báo cáo

1 9 Lái xe Label Hiển thị tên lái xe

1 Ghi chú Label Hiển thị ghi chú của báo cáo

![](images/ndlxd-export.pdf-0148-01.png)

![](images/ndlxd-export.pdf-0148-02.png)

<!-- Trang 149 -->

|2<br>2|Thu hồi|Butto<br>n|Enable|Cho phép người dùng được<br>phân quyền thực hiện hành<br>động tương ứng.<br>Hiển thị tương ứng theo phân<br>quyền người dùng và trạng<br>thái của đối tượng (xem thêm<br>ở<br>Người dùng chọn tới hành<br>động để thực hiện 1 trong các<br>UC:<br>Lưu đồ trạng thái của Danh<br>mục)<br>Thu hồi báo cáo sự cố|
|---|---|---|---|---|
|2<br>3|Lịch sử hoạt<br>động|Butto<br>n|Enable|Chọn để hiển thị popup Lịch<br>sử hoạt động, xem thêm ở<br>Thông báo & Lịch sử hoạt<br>động|
|2<br>4|Đóng|Icon|Enable|Click icon để đóng màn hình,<br>quay lại màn hình Lịch sử báo<br>cáo sự cố|

![](images/ndlxd-export.pdf-0149-01.png)

<!-- Trang 150 -->

### UC04.01.03 - Tạo báo cáo sự cố

#### 1. Thông tin chung

|Mã UC - Tên UC|UC04.01.03 - Tạo báo cáo sự cố|
|---|---|
|Tác nhân|Người dùng ứng dụng dành cho lái xe Delta|
|Đường dẫn|Màn hình Danh sách báo cáo sự cố > Button Tạo mới > Màn hình Tạo<br>mới báo cáo sự cố<br>Chọn tới button Tạo báo cáo sự cố của lịch nhắc > Màn hình Tạo mới<br>báo cáo sự cố|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Hệ thống tạo 1 bản ghi với trạng thái Đang chờ xử lý<br>Hiển thị popup message tạo thành công<br>Hiển thị màn hình Thông tin báo cáo sự cố (Xem)|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tạo mới báo cáo sự cố

![Trang 150 — ảnh xem trước để đối chiếu hình vẽ](images/page-150.png)

<!-- Trang 151 -->

![Trang 151 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0151-00.png)


<!-- Trang 152 -->

![](images/ndlxd-export.pdf-0152-00.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Biển số xe|Label|||Hiển thị biển số của lái<br>xe/người hiện tại đang đăng<br>nhập.||
|2|Hệ thống<br>tổng thành<br>xe|Dropd<br>own<br>list|Có||Cho phép chọn hệ thống tổng<br>thành xe trong danh sách có<br>sẵn.||

1 Biển số xe Label Hiển thị biển số của lái

<!-- Trang 153 -->

|||||Danh sách gồm:<br>0 - Không xác định.<br>1 - Động cơ – làm mát<br>2 - Hệ thống truyền lực.<br>3 - Hệ thống gầm.<br>4 - Hệ thống điện.<br>5 - Hệ thống cung cấp<br>nhiên liệu – khí nạp.<br>6 - Hệ thống phụ và cabin<br>Chỉ cho phép chọn 1 giá trị.||
|---|---|---|---|---|---|
|3|Mô tả sự cố|Long<br>textb<br>ox|Có|Cho phép người dùng nhập<br>mô tả sự cố.||
|4|Hình ảnh và<br>chứng từ<br>thanh toán|Imag<br>e<br>Uploa<br>d|Có|Cho phép người chụp hình<br>ảnh và chứng từ thanh toán<br>lên (real-time).<br>File upload cho phép: file ảnh<br>đuôi .JPG / .JPEG/ .PNG<br>Hiển thị ban đầu (no data):<br>Sau khi có file đã được<br>upload, phần mềm hiển thêm<br>thị giao diện:<br>Người dùng có thể chọn icon<br>X để loại bỏ file đã upload.<br>Hình ảnh chụp realtime phải<br>hiển thị thông tin:|Dung lượng tối đa<br>được upload:<br>250MB.<br>→ Nếu vi phạm, hệ<br>thống hiển thị<br>message lỗi: “Dung<br>lượng các file tải lên<br>không quá 250MB.”<br>ngay sau khi file<br>được upload<br>Các định dạng<br>cho phép: .JPG /<br>.JPEG/ .PNG<br>→ Nếu người dùng<br>upload các định<br>dạng không đúng<br>quy định lên, hệ<br>thống không ghi<br>nhận file upload và<br>báo lỗi: “File upload|

![Trang 153 — ảnh xem trước để đối chiếu hình vẽ](images/page-153.png)

<!-- Trang 154 -->

||||||Thời gian tại thời điểm chụp<br>Format: dd/mm/yyyy<br>hh:mm<br>Địa điểm chụp|lên không đúng định<br>dạng.”|
|---|---|---|---|---|---|---|
|5|Ghi chú|Textb<br>ox<br>(Long<br>)|||Cho phép người dùng nhập<br>ghi chú.||
|6|Thời gian<br>phát hiện<br>sự cố|Label|||Hiển thị thời gian hiện tại khi<br>tạo báo cáo sự cố (lấy thời<br>gian ấn button Tạo)<br>Format hiển thị: dd/mm/yyyy<br>hh:mm||
|7|Vị trí hiện<br>tại|Label|||Hiển thị địa chỉ hiện tại của lái<br>xe.<br>Lấy vị trí hiện tại GPS của<br>người dùng và dùng service<br>bên thứ 3 để trả về địa chỉ<br>(reverse geocoding).||
|8|Cách giải<br>quyết|Dropd<br>own<br>list|Có||Cho phép người dùng chọn<br>cách giải quyết cho sự cố.<br>Danh sách giá trị:<br>Xưởng: xưởng hướng dẫn<br>giải quyết<br>Lái xe: lái xe tự giải quyết<br>Chỉ cho phép chọn 1.<br>→ ảnh hưởng tới luồng tiếp<br>theo sau khi tạo.||
|9|Số tiền|Numb<br>erbox|Có|Hidden|Cho phép người dùng nhập số<br>tiền khắc phục sự cố.<br>Nhập tiền, số dương.|Số tiền nhập <= 2<br>triệu đồng.<br>→ Nếu vi phạm, hệ<br>thống báo lỗi inline:|

![Trang 154 — ảnh xem trước để đối chiếu hình vẽ](images/page-154.png)

<!-- Trang 155 -->

||||||Chỉ hiển thị khi cách giải<br>quyết = lái xe.|“Số tiền >= 2 triệu<br>phải ghi nhận qua<br>đơn mua dịch vụ<br>ngoài của xưởng.”|
|---|---|---|---|---|---|---|
|1<br>0|Phân loại<br>chi phí|Dropd<br>own<br>list|Có|Hidden|Cho phép người dùng chọn tới<br>phân loại chi phí của sự cố<br>được báo.<br>Danh sách giá trị bao gồm:<br>Rửa xe<br>Bơm mỡ<br>Sửa xe<br>Thay thế phụ tùng<br>Chi phí khác<br>Chỉ cho phép chọn 1<br>Chỉ hiển thị khi cách giải<br>quyết = lái xe.||
|1<br>1|Tạo mới|Butto<br>n||Enable|Cho phép người dùng hoàn tất<br>việc tạo yêu cầu tạo mới 1 bản<br>ghi báo cáo sự cố.<br>Hệ thống thực hiện kiểm tra<br>validate các trường thông tin<br>tạo mới.<br>Nếu tất cả hợp lệ:<br>Hiển thị màn hình Xem<br>chi tiết báo cáo sự cố với<br>hành động (tuỳ theo phân<br>quyền):<br>Thu hồi<br>Tạo 1 bản ghi báo cáo sự<br>cố với trạng thái Đang<br>chờ xử lý<br>Gửi thông báo tới người<br>dùng có quyền xác<br>nhận/chuẩn đoán báo||

![Trang 155 — ảnh xem trước để đối chiếu hình vẽ](images/page-155.png)

<!-- Trang 156 -->

cáo sự cố ở PM Xưởng
với nội dung:
Báo cáo sự cố
Báo cáo sự cố cho
phương tiện [Biển số xe]
đang chờ phê duyệt.
Lưu 1 bản ghi hoạt động
mới ở Lịch sử hoạt động:
[Tên tài khoản thực hiện
hành động] hh:mm
dd/mm/yyyy
Đã tạo mới báo cáo sự
cố.
Generate ID mới cho
phiếu báo cáo sự cố với
quy tắc như sau:
Format: [Biển
số]/BCSC[xx]
[ddmmyyyy]
Biển số: lấy biển số
phương tiện báo cáo
sự cố
xx: Mã báo cáo sự
cố chạy từ 01 đến
99, đánh số thứ tự
tăng dần nếu mà có
cùng [Biển số] và
ddmmyyyy
ddmmyyyy: lấy ngày
báo cáo sự cố của
phương tiện
Nếu có trường không hợp
lệ, thông báo lỗi (in-line
error msg) dưới trường
không hợp lệ đó.

![](images/ndlxd-export.pdf-0156-00.png)

![](images/ndlxd-export.pdf-0156-02.png)

<!-- Trang 157 -->

|1<br>2|Huỷ|Butto<br>n|Enable|Cho phép người dùng huỷ bỏ<br>tạo mới báo cáo sự cố<br>Hệ thống hiển thị hộp thoại<br>xác nhận huỷ tạo mới báo cáo<br>sự cố trước khi huỷ.<br>Xác nhận: không tạo ra bản<br>ghi mới nào & trở về màn<br>hình Danh sách báo cáo sự<br>cố<br>Hủy: trở về màn Tạo mới<br>báo cáo sự cố với các dữ<br>liệu đã chọn/nhập.|
|---|---|---|---|---|
|1<br>3||Icon||Cho phép người dùng huỷ bỏ<br>tạo mới báo cáo sự cố<br>Hệ thống hiển thị hộp thoại<br>xác nhận huỷ tạo mới báo cáo<br>sự cố trước khi huỷ.<br>Xác nhận: không tạo ra bản<br>ghi mới nào & trở về màn<br>hình Danh sách báo cáo sự<br>cố<br>Hủy: trở về màn Tạo mới<br>báo cáo sự cố với các dữ<br>liệu đã chọn/nhập.|

![](images/ndlxd-export.pdf-0157-01.png)

1 3 Icon Cho phép người dùng huỷ bỏ

<!-- Trang 158 -->

##### 3.1 Màn hình Thông tin báo cáo sự cố (xem) - Trạng thái Đang chờ xử lý

![](images/ndlxd-export.pdf-0158-01.png)

<!-- Trang 159 -->

![](images/ndlxd-export.pdf-0159-00.png)

Các trường thông tin đã được mô tả ở UC , ở đây chỉ mô tả

Xem thông tin chi tiết báo cáo sự cố

thêm các hành động (xem đầy đủ các hành động theo từng trạng thái ở Lưu đồ trạng thái):

Button Thu hồi: Click vào để hiển thị popup Xác nhận thu hồi, thực hiện UC

Thu hồi báo cáo

sự cố

<!-- Trang 160 -->

### UC04.01.04 - Thu hồi báo cáo sự cố

#### 1. Thông tin chung

|Mã UC - Tên UC|UC04.01.04 - Thu hồi báo cáo sự cố|
|---|---|
|Tác nhân|Người dùng ứng dụng dành cho lái xe Delta|
|Đường dẫn|Màn hình Thông tin báo cáo sự cố(xem): chọn button Thu hồi|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta|
|Điều kiện sau|Trạng thái của bản ghi thay đổi từ Đang chờ xử lý → Đã thu hồi<br>Hiển thị popup message thành công<br>Tắt popup Thu hồi và hiển thị màn hình Thông tin báo cáo sự cố|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình

##### 3.1 Màn hình Thu hồi báo cáo sự cố

![](images/ndlxd-export.pdf-0160-06.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Xác nhận|Butto||Enable|Cho phép người dùng xác||
|||n|||nhận thu hồi báo cáo sự cố.||

<!-- Trang 161 -->

|||||Sau khi xác nhận,<br>Trạng thái của bản ghi thay<br>đổi từ Đang chờ xử lý → Đã<br>thu hồi<br>Trạng thái của tiến trình<br>chuyển từ Đang triển khai<br>→ Đã hủy/từ chối<br>Đóng popup Xác nhận Thu<br>hồi và hiển thị màn hình<br>Thông tin báo cáo sự cố.<br>Gửi thông báo tới người<br>dùng đã tạo báo cáo sự cố<br>này ở app Lái xe với nội<br>dung:<br>Báo cáo sự cố<br>Báo cáo sự cố của bạn đã bị<br>thu hồi.<br>Lưu 1 bản ghi hoạt động mới<br>ở Lịch sử hoạt động:<br>[Tên tài khoản thực hiện hành<br>động] hh:mm dd/mm/yyyy<br>Đã thu hồi báo cáo sự cố<br>Lý do: [Lý do người dùng<br>nhập]|
|---|---|---|---|---|
|2|Huỷ bỏ|Butto<br>n|Enable|Cho phép người dùng huỷ bỏ<br>việc xác nhận thu hồi báo cáo<br>sự cố.<br>Sau khi huỷ bỏ,<br>Trạng thái bản ghi giữ<br>nguyên: Đang chờ xử lý|

![](images/ndlxd-export.pdf-0161-01.png)

<!-- Trang 162 -->

Đóng popup và trở về màn
hình Thông tin báo cáo sự
cố.

##### 3.2 Màn hình Thông tin báo cáo sự cố (Xem) - Trạng thái Đã thu hồi

![](images/ndlxd-export.pdf-0162-00.png)

Các trường thông tin đã được mô tả ở UC báo cáo sự cố, ở đây chỉ mô tả

Xem thông tin chi tiết

thêm các hành động (xem đầy đủ các hành động theo từng trạng thái ở ):

Lưu đồ trạng thái

Xoá: Cho phép người dùng xoá bản ghi đã bị thu hồi.

Chọn Xoá: Hệ thống hiển thị popup Xác nhận

![](images/ndlxd-export.pdf-0162-02.png)

![](images/ndlxd-export.pdf-0162-04.png)

<!-- Trang 163 -->

![](images/ndlxd-export.pdf-0163-00.png)

Xác nhận:

Hệ thống xoá bản ghi tương ứng

Đóng tất cả popup và trở về màn hình Lịch sử báo cáo sự cố

Huỷ: Quay trở về màn hình Thông tin báo cáo sự cố

Tạo lại: Cho phép người dùng cập nhật lại bản ghi từ thông tin đã bị thu hồi.

Chọn Tạo lại: Hệ thống hiển thị màn hình Tạo mới báo cáo sự cố, thực hiện UC Tạo mới báo

cáo sự cố với các trường lấy thông tin từ yêu cầu hiện tại (đã bị thu hồi) nhưng không sinh ra

bản ghi mới mà cập nhật thông tin chỉnh sửa và trạng thái (từ Đã thu hồi về Đang chờ xử lý)

<!-- Trang 164 -->

## Epic 05 - Lịch nhắc

![](images/ndlxd-export.pdf-0164-01.png)

<!-- Trang 165 -->

### UC05.01.01 - Xem lịch nhắc

#### 1. Thông tin chung

|Mã UC - Tên UC|UC05.01.01 - Xem lịch nhắc|
|---|---|
|Tác nhân|Người dùng ứng dụng Lái xe Delta|
|Đường dẫn|Chọn tới mục Lịch nhắc trên Navigation bar >> Màn hình Lịch nhắc|
|Điều kiện trước|Người dùng đã được cấp tài khoản trên ứng dụng Lái xe Delta<br>Trạng thái tài khoản là: Đang hoạt động<br>Tài khoản có quyền truy cập vào ứng dụng Lái xe Delta<br>Lịch nhắc đã được tạo và cho phép thông báo tới lái xe ở hệ thống<br>PM Xưởng|
|Điều kiện sau|Hệ thống hiển thị màn hình Lịch nhắc thành công.<br>Hệ thống hiển thị đầy đủ các lịch nhắc tới hạn.|

#### 2. Lưu đồ hoạt động

#### 3. Mô tả màn hình:

##### 3.1 Màn hình Lịch nhắc

Hệ thống báo lịch nhắc cho người dùng qua thông báo và qua danh sách nhắc lịch:

Thông báo nhắc lịch:

Hôm nay bạn có [x] lịch nhắc mới và [y] lịch nhắc chưa thực hiện.

Trong đó,

x = số lượng lịch nhắc bắt đầu báo từ hôm nay

y = tổng số lịch nhắc còn lại chưa thực hiện (không tính hôm nay)

![Trang 165 — ảnh xem trước để đối chiếu hình vẽ](images/page-165.png)

<!-- Trang 166 -->

![Trang 166 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0166-00.png)


<!-- Trang 167 -->

![](images/ndlxd-export.pdf-0167-00.png)

||Control|Loại|Trườ<br>ng<br>bắt<br>buộ<br>c|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tab||||Hiển thị tab thông tin:<br>Chưa thực hiện<br>Đã thực hiện<br>Hiển thị UI tổng số lượng bản<br>ghi lịch nhắc ở tab Chưa thực||

1 Tab Hiển thị tab thông tin:

<!-- Trang 168 -->

||||hiện cạnh tên tab như sau:|
|---|---|---|---|
|2|Collapse/Ex<br>pand|Expande<br>d|Cho phép người dùng mở ra/<br>đóng lại các lịch nhắc theo<br>từng loại.|
|3|Phân loại||Hiển thị lịch nhắc theo các<br>phân loại:<br>Theo thời gian:<br>Theo vận hành:<br>Theo hạn thời gian:|
|4|Chưa thực hiện: Hiển thị các bản ghi lịch nhắc đến hạn nhắc lịch (từ [lần cuối thực hiện +<br>khoảng nhắc lịch - dung sai] đến khi được ghi nhận hoàn thành qua lệnh sửa chữa) mà chưa<br>được thực hiện.<br>Bản ghi nhắc lịch theo thời gian:<br>Bản ghi nhắc lịch theo vận hành (kms/giờ):<br>Bản ghi nhắc lịch theo hạn thời gian:|||
|5|Đã thực hiện: Hiển thị các bản ghi lịch nhắc đã thực hiện và chưa đến hạn nhắc lịch.<br>UI bản ghi:|||

3 Phân loại Hiển thị lịch nhắc theo các

![](images/ndlxd-export.pdf-0168-00.png)

<!-- Trang 169 -->

|6|Icon nhắc<br>lịch||Hiển thị icon nhắc lịch theo<br>tình trạng lịch nhắc:<br>Đến thời gian nhắc lịch<br>nhưng chưa tới điều kiện<br>thực hiện:<br>Quá điều kiện thực hiện:|
|---|---|---|---|
|7|Nội dung<br>nhắc lịch|Label|Hiển thị tên hoạt động nhắc<br>lịch.|
|8|Lần cuối<br>thực hiện|Label|Hiển thị thời gian lần cuối thực<br>hiện hoạt động của phương<br>tiện.<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo thời gian.|
|9|Ngày cần<br>thực hiện|Label|Hiển thị thời gian cần thực<br>hiện hoạt động của phương<br>tiện.<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo thời gian.|
|1<br>0|Số kms cuối<br>thực hiện|Label|Hiển thị số kms cuối phương<br>tiện thực hiện hoạt động.<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo vận hành và<br>phương tiện chạy vận hành<br>theo kms.|
|1<br>1|Số kms cần<br>thực hiện|Label|Hiển thị số kms cần thực hiện<br>hoạt động của phương tiện.<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo vận hành và|

![Trang 169 — ảnh xem trước để đối chiếu hình vẽ](images/page-169.png)

<!-- Trang 170 -->

||||phương tiện chạy vận hành<br>theo kms.|
|---|---|---|---|
|1<br>2|Số kms hiện<br>tại|Label|Hiển thị số giờ hiện tại của<br>phương tiện<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo vận hành và<br>phương tiện chạy vận hành<br>theo giờ.|
|1<br>3|Số giờ cuối<br>thực hiện|Label|Hiển thị số giờ cuối phương<br>tiện thực hiện hoạt động.<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo vận hành và<br>phương tiện chạy vận hành<br>theo giờ.|
|1<br>4|Số giờ cần<br>thực hiện|Label|Hiển thị số giờ cần thực hiện<br>hoạt động của phương tiện.<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo vận hành và<br>phương tiện chạy vận hành<br>theo giờ.|
|1<br>5|Số giờ hiện<br>tại|Label|Hiển thị số giờ hiện tại của<br>phương tiện<br>Hiển thị đối với các bản ghi<br>nhắc lịch theo vận hành và<br>phương tiện chạy vận hành<br>theo giờ.|
|1<br>6|Ngày hết<br>hạn|Label|Hiển thị ngày hết hạn của hoạt<br>động nhắc lịch.|

![](images/ndlxd-export.pdf-0170-01.png)

<!-- Trang 171 -->

## Epic 06 - Phiếu cấp dầu

![](images/ndlxd-export.pdf-0171-01.png)

<!-- Trang 172 -->

### 06.00 - Lưu đồ trạng thái của phiếu cấp dầu

**1. Danh sách trạng thái**

|Trạng thái|Mã|Mô tả|Hành động|
|---|---|---|---|
|Trạng thái|Mã|Mô tả|Hành động<br>(chưa tính<br>phân|
||||phân<br>quyền)|
|Bản nháp|draft|Đã lưu, chưa gửi|Tạo mới|
|Chờ phê duyệt|pending|Chờ CBQL duyệt (vòng 1 — tạo<br>phiếu)|Phê duyệt<br>Từ chối<br>Thu hồi|
|Hoàn thành|done|Toàn bộ luồng hoàn tất theo từng<br>phương thức như sau:<br>Cây dầu nội bộ: Bơm xong, Igas<br>trả dữ liệu thực bơm về<br>Cây dầu mua ngoài: Đối tác chốt<br>phiếu dầu<br>Hoá đơn lẻ: Phê duyệt hoá đơn||
|Từ chối|rejected|Người dùng từ chối ở bất kỳ vòng<br>duyệt nào|Tạo lại|
|Đã thu hồi|recalled|Người tạo tự thu hồi khi đang<br>pending|Tạo lại|
|Chờ nhận mã|approved_waitin<br>g|Đã duyệt / không cần duyệt — lái xe<br>chưa tap nhận mã Igas|Cấp mã<br>Igas|
|Đã cấp Igas|igas_active|Mã Igas đã sinh, đang trong phiên<br>bơm (TTL 5 phút)||

Trạng thái chung

Trạng thái theo phương thức 1: Đổ tại cây dầu nội bộ

![Trang 172 — ảnh xem trước để đối chiếu hình vẽ](images/page-172.png)

<!-- Trang 173 -->

|Igas hết hạn|igas_expired|Mã Igas quá 5 phút chưa bơm|Cấp lại mã<br>Igas|
|---|---|---|---|
|Chờ bơm|waiting|Phiếu gửi đến cây mua ngoài, hiệu<br>lực 24h, chờ nhân viên cây xử lý cho<br>lái xe|Ghi nhận<br>bơm dầu|
|Hết hạn|po_expired|Phiếu quá 24h chưa xác nhận bơm|Tạo lại|
|Đã bơm|fuel_done|Hoàn thành ghi nhận bơm dầu, chờ<br>xuất HĐ cho lái xe|Cập nhật<br>bơm dầu<br>Xuất hoá<br>đơn|
|Đã xuất HĐ|invoice_done|Đã xuất hoá đơn, chờ chốt phiếu để<br>đóng|Cập nhật<br>hoá đơn<br>Chốt<br>phiếu|
|Chờ mua HĐ lẻ|purchase_pendin<br>g|CBQL đã duyệt vòng 1, lái xe đang đi<br>mua|Ghi nhận<br>bơm dầu|
|Chờ duyệt bơm|purchase_fuel_pe<br>nding|Lái xe đã ghi nhận bơm xong, chờ<br>CBQL duyệt vòng 2|Phê duyệt<br>Từ chối|
|Chờ xuất HĐ|purchase_invoici<br>ng|CBQL đã duyệt vòng 2, lái xe chờ lấy<br>/ upload HĐ|Xuất hoá<br>đơn|
|Chờ duyệt HĐ|purchase_invoice<br>_pending|Lái xe đã upload HĐ, chờ CBQL<br>duyệt vòng 3|Phê duyệt<br>Từ chối|

Trạng thái theo phương thức 2: Đổ tại cây dầu mua ngoài

**Trạng thái theo phương thức 3: Mua dầu hoá đơn lẻ**

#### 2. Lưu đồ trạng thái

##### 2.1 Luồng Cây nội bộ

1 ┌───────┐ Submit 2 │ draft │──────────────────────────────────────────────┐ 3 └───────┘ │ 4 ▼ 5 ┌──────────────────┐

![Trang 173 — ảnh xem trước để đối chiếu hình vẽ](images/page-173.png)

<!-- Trang 174 -->

![](images/ndlxd-export.pdf-0174-00.png)

![](images/ndlxd-export.pdf-0174-01.png)

![](images/ndlxd-export.pdf-0174-03.png)

6 │ Approval Check │ 7 └────────┬─────────┘ 8 ┌───────────────┴──────────────┐ 9 TH1/TH3 TH2 10 (không cần duyệt) (cần CBQL duyệt) 11 │ │ 12 ▼ ▼ 13 ┌─────────────────┐ ┌──────────────┐ 14 │ approved_waiting │ │ pending │ 15 └────────┬────────┘ └──────┬───────┘ 16 │ Từ chối│ │Phê duyệt 17 │ ▼ │ 18 │ rejected │ 19 │ ▼ 20 │ ┌─────────────────┐ 21 │◄───────────────────│ approved_waiting│ 22 │ (CBQL phê duyệt)└─────────────────┘ 23 │ 24 Lái xe tap "Nhận mã Igas" 25 │ 26 ▼ 27 ┌──────────────┐ 28 │ igas_active │──── Hết 5 phút ──► igas_expired 29 └──────┬───────┘ │ 30 │ Xin lại mã 31 Igas callback │ 32 (bơm xong) ▼ 33 │ igas_active (mới) 34 ▼ 35 ┌──────┐ 36 │ done │ 37 └──────┘ 38

##### 2.2 Luồng Cây mua ngoài

1 ┌───────┐ 2 │ draft │── Submit ──► Approval Check 3 └───────┘ │ 4 ┌──────────────┴──────────────┐ 5 TH4 TH2 6 (không cần duyệt) (cần CBQL duyệt) 7 │ Từ chối ──► rejected 8 ▼ │ Phê duyệt 9 ┌─────────────┐◄───────────────────────┘ 10 │ waiting │──── Hết 24h ──► po_expired ──── Tạo lại ──► back về trạng thái chờ duyệt 11 └──────┬──────┘ 12 │ Nhân viên cây: Ghi nhận bơm dầu + nhập số lít 13 │ (qua Partner Portal) 14 ▼ 15 ┌────────────┐ 16 │ fuel_done │ 17 └─────┬──────┘ 18 │ Nhân viên cây: Xuất hoá đơn + upload HĐ 19 │ (qua Partner Portal) 20 ▼ 21 ┌──────────────┐ 22 │ invoice_done │ 23 └──────┬───────┘ 24 │ Nhân viên cây: Chốt phiếu 25 │ (qua Partner Portal) 26 ▼ 27 ┌──────┐ 28 │ done │ (terminal) 29 └──────┘

<!-- Trang 175 -->

30

##### 2.3 Luồng Hóa đơn lẻ (3 vòng phê duyệt)

![](images/ndlxd-export.pdf-0175-02.png)

1 ┌───────┐ 2 │ draft │── Submit (TH5 — luôn qua pending) 3 └───────┘ │ 4 Từ chối ──► rejected · Thu hồi ──► recalled 5 │ Phê duyệt vòng 1 6 ▼ 7 ┌──────────────────┐ 8 │ purchase_pending │ Lái xe đến Petrolimex mua 9 └────────┬──────────┘ 10 │ Lái xe: Ghi nhận bơm dầu + nhập số lít 11 ▼ 12 ┌──────────────────────┐ 13 │ purchase_fuel_pending│ Chờ CBQL duyệt vòng 2 14 └──────────┬────────────┘ 15 Từ chối ──► rejected 16 │ Phê duyệt vòng 2 17 ▼ 18 ┌──────────────────────┐ 19 │ purchase_invoicing │ Lái xe lấy + upload HĐ 20 └──────────┬────────────┘ 21 │ Lái xe: Xuất hoá đơn (upload ảnh HĐ) 22 ▼ 23 ┌──────────────────────────┐ 24 │ purchase_invoice_pending │ Chờ CBQL duyệt vòng 3 25 └──────────┬───────────────┘ 26 Từ chối ──► rejected 27 │ Phê duyệt vòng 3 28 ▼ 29 ┌──────┐ 30 │ done │ (terminal) 31 └──────┘ 32

Ghi chú: Trạng thái terminal done , rejected , recalled — không chuyển tiếp. Chỉ có thể

"Tạo lại" → phiếu gốc back về trạng thái chờ duyệt trước đó chứ không phải tạo lại từ đầu.

<!-- Trang 176 -->

|0||||||
|---|---|---|---|---|---|
|||Sự kiện|Notify<br>gửi đi|Nội dung thông báo|Activity Log|
||||(MSC-<br>01/SC-|||
||||03)|||
||1|Luồng chung||||
||2|Tạo mới (Submit)<br>— Không cần phê<br>duyệt (TH1/TH3 —<br>cây nội bộ)|—||[Tên] đã tạo phiếu - không<br>cần phê duyệt.|
||3|Tạo mới (Submit)<br>— Không cần phê<br>duyệt (TH4 — cây<br>mua ngoài)|Partner<br>Portal|Cấp dầu<br>Có phiếu mới [mã] cấp [X<br>lít/đầy bình] cho<br>phương tiện [Biển số<br>xe] .|[Tên] đã tạo phiếu - không<br>cần phê duyệt.|
||4|Submit — Cần<br>phê duyệt<br>(TH2/TH5)|Người<br>có<br>quyền<br>phê<br>duyệt|Cây dầu · Cấp dầu<br>Một phiếu mới [loại<br>dGas] xin cấp [X lít/<br>đầy bình] vừa được tạo<br>bởi [tên_lx] .|[Tên] đã tạo phiếu - có yêu<br>cầu phê duyệt.|
||5|Phê duyệt v1 —<br>nội bộ|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được phê duyệt<br>bởi<br>[tên_người_phê_duyệt] .|[Tên] đã phê duyệt.|
||6|Phê duyệt v1 —<br>mua ngoài|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được phê duyệt<br>bởi<br>[tên_người_phê_duyệt] .|[Tên] đã phê duyệt.|

### 06.00 - Thông báo & Lịch sử hoạt động

— [Tên] đã tạo phiếu - không

![Trang 176 — ảnh xem trước để đối chiếu hình vẽ](images/page-176.png)

<!-- Trang 177 -->

|7||NV cây<br>dầu<br>(Portal)|Cấp dầu<br>Có phiếu mới [mã] cấp [X<br>lít/đầy bình] cho<br>phương tiện [Biển số<br>xe] .||
|---|---|---|---|---|
|8|Phê duyệt v1 —<br>HĐ lẻ|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được phê duyệt<br>bởi<br>[tên_người_phê_duyệt] .|[Tên] đã phê duyệt.|
|9|Từ chối (mọi<br>vòng)|Người<br>tạo|Chưa có mã:<br>Cây dầu · Cấp dầu<br>Phiếu cấp dầu vừa bị từ chối<br>bởi<br>[tên_người_từ_chối] .<br>Đã có mã:<br>Cây dầu · Cấp dầu<br>[mã] vừa bị từ chối bởi<br>[tên_người_từ_chối] .|[Tên] đã từ chối.<br>Lý do: [Lý do]|
|1<br>0|Thu hồi|Người<br>có<br>quyền<br>phê<br>duyệt|Cây dầu · Cấp dầu<br>Phiếu cấp dầu vừa bị thu hồi<br>bởi<br>[tên_người_thu_hồi] .|[Tên] đã thu hồi.|
|1<br>1|Luồng cây dầu nội bộ||||
|1<br>2|Nhận mã Igas|—||[Tên] đã nhận mã Igas.|
|1<br>3|Igas callback bơm<br>xong|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được hoàn thành<br>bơm dầu.|[Tên] đã hoàn thành bơm.|
|1<br>4|Igas hết hạn|Người<br>tạo|Cây dầu · Cấp dầu|Mã Igas hết hạn — Chưa bơm<br>Actor = hệ thống|

7 NV cây

2 Nhận mã Igas — [Tên] đã nhận mã Igas.

![Trang 177 — ảnh xem trước để đối chiếu hình vẽ](images/page-177.png)

<!-- Trang 178 -->

||||[mã] vừa bị hết hạn mã<br>Igas.||
|---|---|---|---|---|
|1<br>5|Cấp lại mã Igas|—||[Tên] đã nhận lại mã Igas.|
|1<br>6|Luồng cây dầu mua ngoài||||
|1<br>7|Phiếu cấp dầu hết<br>hạn 24h|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa bị hết hạn.|Phiếu hết hạn - Chưa ghi nhận<br>bơm.<br>Actor = hệ thống|
|1<br>8|NV cây ghi nhận<br>bơm|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được ghi nhận<br>bơm bởi [tên_cây_dầu] .|[tên_cây] đã (cập nhật) ghi<br>nhận bơm xong.<br>Ghi chú: Nếu có cập nhật thì<br>thêm text cập nhật vào.|
|1<br>9|NV cây xuất HĐ|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được xuất hoá<br>đơn bởi [tên_cây_dầu] .|[tên_cây] đã (cập nhật)<br>xuất hoá đơn.<br>Ghi chú: Nếu có cập nhật thì<br>thêm text cập nhật vào.|
|2<br>0|NV cây chốt phiếu|Người<br>tạo +<br>Người<br>phê<br>duyệt.|Cây dầu · Cấp dầu<br>[mã] vừa được chốt bởi<br>[tên_cây_dầu] .|[tên_cây] đã chốt phiếu.|
|2<br>1|Luồng mua hoá đơn lẻ||||
|2<br>2|Lái xe ghi nhận<br>bơm HĐ lẻ|Người<br>có<br>quyền<br>phê<br>duyệt<br>ghi nhận<br>bơm|Cây dầu · Cấp dầu<br>[mã] vừa được ghi nhận<br>bơm bởi [tên] .|[tên] đã ghi nhận bơm<br>xong.|

5 Cấp lại mã Igas — [Tên] đã nhận lại mã Igas.

![Trang 178 — ảnh xem trước để đối chiếu hình vẽ](images/page-178.png)

<!-- Trang 179 -->

|2<br>3|Phê duyệt v2 HĐ<br>lẻ|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được xác nhận<br>bơm bởi [tên] .|[tên] đã xác nhận bơm dầu.|
|---|---|---|---|---|
|2<br>4|Lái xe upload HĐ|Người<br>có<br>quyền<br>phê<br>duyệt<br>ghi nhận<br>hoá đơn|Cây dầu · Cấp dầu<br>[mã] vừa được xuất hoá<br>đơn bởi [tên] .|[tên] đã upload hoá đơn.|
|2<br>5|Phê duyệt v3 HĐ<br>lẻ|Người<br>tạo|Cây dầu · Cấp dầu<br>[mã] vừa được phê duyệt<br>hoá đơn bởi [tên] .|[tên] đã phê duyệt hoá<br>đơn.|
|2<br>6|Trường hợp đặc biệt: Loại dGas 5||||
|2<br>7|Submit dGas5|Người<br>có<br>quyền<br>phê<br>duyệt|Cây dầu · Cấp dầu<br>Phiếu chốt dầu tháng [kỳ]<br>cho phương tiện [Biển số<br>xe] vừa được tạo bởi<br>[tên_lx]|[tên] đã tạo phiếu chốt dầu<br>kỳ.|

![Trang 179 — ảnh xem trước để đối chiếu hình vẽ](images/page-179.png)

<!-- Trang 180 -->

### UC06.00.01 - Xem danh sách phiếu cấp dầu

#### 1. Thông tin chung

|Mã UC|UC06.00.01|
|---|---|
|Tên UC|Xem danh sách phiếu cấp dầu|
|Tác nhân|Lái xe, Nhân viên, Quản lý — đã đăng nhập và có quyền xem module Cấp dầu|
|Đường dẫn|Bottom Navigation → Tab Trang chủ → Cấp dầu / hoặc Deep link từ thông báo|
|Điều kiện trước|Người dùng đã đăng nhập.<br>Có quyền truy cập tính năng Cấp dầu.|
|Điều kiện sau|Danh sách phiếu cấp dầu hiển thị theo bộ lọc/tìm kiếm hiện tại.|

#### 2. Lưu đồ hoạt động

1. Người dùng vào màn Danh sách phiếu cấp dầu.

2. Hệ thống load danh sách phiếu cấp dầu thuộc về user (lái xe thấy phiếu của mình; quản lý/TP điều vận thấy tất cả phiếu trong phạm vi quyền).

Sắp xếp mặc định: thời gian tạo giảm dần.

3. Người dùng có thể:

Tìm kiếm theo mã phiếu (debounce 300ms).

Tap icon Filter (MSC-03) → Bottom sheet lọc theo: Loại dGas, Trạng thái, Khoảng thời gian, Lượng dầu.

Scroll để load thêm (infinite scroll hoặc pagination).

Tap card bất kỳ → điều hướng đến UC06.00.02 (Xem chi tiết).

Tap Button "Tạo mới" → mở Bottom sheet chọn loại phiếu (UC06.00.03–07).

Làm mới: kéo xuống (pull-to-refresh) → reload danh sách (Xem 2.14 App Common).

Load thêm: scroll xuống đến 80% cuối danh sách → tự động load thêm 20 phiếu (Xem 2.15 App Common).

4. Hệ thống cập nhật danh sách khi user quay lại từ màn chi tiết hoặc sau khi tạo mới.

#### 3. Mô tả màn hình

##### 3.1 Màn hình Danh sách phiếu cấp dầu

![](images/ndlxd-export.pdf-0180-17.png)

Danh sách dạng card (không phải table), phù hợp mobile. Mỗi card đại diện 1 phiếu cấp dầu.

<!-- Trang 181 -->

||Tên thành phần|Control|Loại|Bắt buộc|Giá trị mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Header|Label|Text|—|—|"Danh sách phiếu cấp dầu".<br>Button back (←) bên trái điều hướng về màn<br>trước.|—|
|2|Ô tìm kiếm|Input|Text|Không|—|Placeholder "Tìm kiếm…".<br>Tìm theo mã phiếu, thời gian, số lít, mã dGas.<br>Realtime debounce 300ms.<br>Icon ✕ xoá nội dung khi đang có text.|—|
|3|Icon Filter|Icon/Butto<br>n|—|Không|—|Góc phải ô search.<br>Tap → mở Bottom sheet Bộ lọc (MSC-03).<br>Badge số đỏ nếu đang có filter active.|—|
|4|Bottom sheet Bộ<br>lọc|Modal|—|Không|—|Trượt lên từ dưới.<br>Các mục lọc: Loại dGas (multi-select:<br>dGas1/2/3/4/5/Cấp bù); Trạng thái (multi-select);<br>Khoảng thời gian (DatePicker từ–đến), Lượng dầu<br>(from-to)<br>Button "Xoá bộ lọc" + "Áp dụng".|—|
|5|Danh sách card|List|—|—|—|Pull-to-refresh.<br>Empty state khi không có phiếu: icon + "Chưa có<br>phiếu cấp dầu nào."<br>Infinite scroll — load 20 item mỗi lần, spinner nhỏ<br>ở cuối khi tải thêm, label "Đã hiển thị tất cả kết<br>quả" khi hết (Xem 2.15 App Common).<br>Khi đang load lần đầu: Skeleton Loader (Xem<br>MSC-10).|—|
|6|Card phiếu|Card|—|—|—|Tap → UC06.00.02.<br>Xem chi tiết cấu trúc card bên dưới (STT 7–14).|—|
|7|Mã phiếu|Label|Text|—|—|In đậm, góc trên trái.|—|
|8|Ngày tạo|Label|DateTime|—|—|Góc dưới trái.<br>Format: DD/MM/YYYY.|—|
|9|Icon loại dGas|Icon|—|—|—|Hình vuông bo góc, kích thước 40px.<br>Màu nền + icon theo loại dGas (fixed theo UI)<br>Nằm góc trên trái card.||
|1<br>0|Loại dGas (text)|Label|Text|—|—|Nằm dưới mã phiếu, font nhỏ hơn, màu xám. VD:<br>"dGas 1", "dGas 2", "Cấp bù".||
|1<br>1|Badge trạng thái|Badge|—|—|—|Nằm góc phải, hàng trên (cùng hàng với mã<br>phiếu).<br>Dạng: ● [Tên trạng thái] . Màu dot theo<br>trạng thái (xem Bảng trạng thái).|—|
|1<br>2|Ngày tạo|Label|DateTime|—|—|Nằm dưới cùng card, bên trái. Format:<br>dd/mm/yyyy .||
|1<br>3|Số lít|Label|Number/Te<br>xt|—|—|Nằm dưới cùng card, bên phải.||

![Trang 181 — ảnh xem trước để đối chiếu hình vẽ](images/page-181.png)

<!-- Trang 182 -->

|||||||Hiển thị theo logic (xem Bảng hiển thị số lít bên<br>dưới).||
|---|---|---|---|---|---|---|---|
|1<br>4|Empty State|MSC-09|—|—|—|(Xem MSC-09 — Empty State).<br>Tiêu đề: "Chưa có phiếu cấp dầu nào."<br>Subtext: "Tạo phiếu mới để bắt đầu."<br>CTA button "Tạo mới" chỉ hiển thị nếu user có<br>quyền tạo.||
|1<br>5|Button Tạo mới|Button|—|—|—|Full-width, sticky bottom (phía trên safe area).<br>Màu xanh lá đậm (Primary).<br>Label "Tạo mới".<br>Tap → mở Bottom Sheet chọn loại phiếu (3.2).<br>Luôn hiển thị kể cả khi danh sách rỗng (nếu user<br>có quyền tạo).|—|

Ghi chú màn hình: Khi danh sách đang load (lần đầu hoặc sau filter): hiển thị skeleton loading cho 5 card đầu. Khi load

thêm (scroll xuống): spinner nhỏ ở dưới cùng list.

Bảng hiển thị số lít trên card (góc dưới phải)

|Case|Điều kiện|Hiển thị|Ghi chú|
|---|---|---|---|
|A|Chưa bơm (mọi trạng thái pending/approved)|X L — font thường|Chỉ hiện số lít xin cấp|
|A'|dGas4/5 chưa bơm|Đổ đầy bình — font thường|Không có số lít cụ thể|
|B|Đã bơm, thực nhận = xin cấp|X L — font xanh lá|Số thực nhận|
|C|Đã bơm, thực nhận ≠ xin cấp|X L / Y L — thực nhận<br>(xanh) / xin cấp (xám)|X = thực nhận, Y = xin cấp|

##### 3.2 Bottom sheet chọn loại phiếu

![](images/ndlxd-export.pdf-0182-05.png)

Trigger: tap Button "Tạo mới".

Slide-up animation từ dưới, duration 300ms.

<!-- Trang 183 -->

**Hiển thị danh sách này theo chức vụ:**

Quản lý: dGas 1, dGas 4

Lái xe: dGas 3, dGas 5

Kỹ thuật xưởng, Quản lý xưởng: dGas 2

||Tên thành phần|Control|Loại|Bắt buộc|Giá trị mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Tiêu đề|Label|Text|—|—|"Tạo phiếu cấp dầu".<br>Handle bar nhỏ ở trên cùng (swipe down để<br>đóng).|—|
|2|Nhóm "CẤP DẦU<br>THƯỜNG"|Group<br>Label|—|—|—|Section header xám, chữ hoa.|—|
|3|Option dGas1|Radio Card|—|Không|—|Icon ⚙ vàng + "Cấp dầu quản lý".<br>Tap → chọn loại.|—|
|4|Option dGas2|Radio Card|—|Không|—|Icon 🔧 hồng + "Cấp dầu xưởng”<br>Tap → chọn loại.|—|
|5|Option dGas3|Radio Card|—|Không|—|Icon 🚛 xanh + "Cấp dầu vận tải".<br>Nếu có lượng dầu tích lũy chờ nhận: hiển thị chip<br>vàng "X L chờ nhận" bên phải.<br>Lượng dầu tích luỹ = lượng dầu từ lệnh VC đã<br>hoàn thành nhưng chưa nhận dầu.<br>BE check API và trường dữ liệu lệnh VC mà Delta<br>ERP trả về|—|
|6|Nhóm "CẤP DẦU<br>ĐẦY BÌNH"|Group<br>Label|—|—|—|Section header xám.|—|
|7|Option dGas4|Radio Card|—|Không|—|Icon 🔋 xanh lam + "Đổ đầy bình".|—|
|8|Option dGas5|Radio Card|—|Không|—|Icon 📅 xanh lá + "Chốt dầu" + chip "Kỳ<br>[tháng/năm]" hiển thị kỳ chốt hiện tại (kỳ chưa<br>được chốt)|—|
|9|Nhóm "CẤP BÙ"|Group<br>Label|—|—|—|Section header xám.|—|
|1<br>0|Option Cấp bù|Radio Card|—|Không|—|Icon ⛽ đỏ + "Cấp bù dầu".<br>Nếu có phiếu cấp dầu chưa đổ hết: chip đỏ "X<br>phiếu".|—|
|1<br>1|Button Huỷ|Button|—|—|—|Secondary.<br>Đóng bottom sheet.|—|
|1<br>2|Button Tiếp tục|Button|—|—|Disabled|Disabled cho đến khi chọn 1 loại.<br>Active (xanh) sau khi chọn.<br>Tap → navigate đến màn tạo tương ứng với pre-<br>check điều kiện (xem Lưu đồ bên dưới).|—|

Logic pre-check khi tap "Tiếp tục":

||Loại chọn|Pre-check|Kết quả nếu pass|Kết quả nếu fail|
|---|---|---|---|---|
|1|dGas1|Kiểm tra định mức tháng còn lại > 0|Navigate UC06.00.03|Popup cảnh báo "Đã hết định mức<br>tháng"|

![Trang 183 — ảnh xem trước để đối chiếu hình vẽ](images/page-183.png)

<!-- Trang 184 -->

|2|dGas2|Kiểm tra có lệnh SC active không|Navigate UC06.00.04|Popup "Không có lệnh sửa chữa nào"|
|---|---|---|---|---|
|3|dGas3|(1) Kiểm tra có lệnh VC tích lũy chưa cấp<br>không ·<br>(2) Kiểm tra chốt dầu tháng trước đã hoàn<br>thành chưa|Navigate UC06.00.05|(1) Bottom Sheet "Không có lệnh vận<br>chuyển nào tích lũy" ·<br>(2) Modal "Không thể tạo phiếu mới —<br>chưa hoàn thành chốt dầu tháng trước"|
|4|dGas4|Không có pre-check|Navigate UC06.00.06|—|
|5|dGas5|Kiểm tra 3 điều kiện chốt tháng + chốt dầu<br>tháng trước chưa hoàn thành|Navigate UC06.00.07 (qua<br>modal kiểm tra điều kiện)|Modal điều kiện chốt thất bại|
|6|Cấp bù|Kiểm tra có phiếu gốc thiếu dầu không|Navigate UC06.00.08 (Tạo<br>phiếu Cấp bù)|Popup "Không có phiếu nào cần cấp bù"|

Ghi chú màn hình: Popup này không đóng khi tap backdrop sau khi đã chọn loại — tránh mất lựa chọn khi vô tình chạm.

Swipe down vẫn đóng được. Nếu user chưa chọn loại nào, tap backdrop = đóng bình thường.

##### 3.3 Message các loại

3.3.1 Popup cảnh báo "Đã hết định mức tháng"

![](images/ndlxd-export.pdf-0184-04.png)

3.3.2 Popup "Không có lệnh sửa chữa nào"

![](images/ndlxd-export.pdf-0184-06.png)

3.3.3 Popup "Không có lệnh vận chuyển nào tích lũy"

![](images/ndlxd-export.pdf-0184-08.png)

3.3.4 Bottom sheet "Không thể tạo phiếu mới — chưa hoàn thành chốt dầu tháng trước"

![](images/ndlxd-export.pdf-0184-10.png)

<!-- Trang 185 -->

Deadline = 5 ngày đầu tháng được chốt dầu, số ngày còn lại = deadline - ngày hôm nay +1.

Button Chốt dầu dGas 5 → navigate UC06.00.07.

3.3.5 Popup "Không có phiếu nào cần cấp bù"

![](images/ndlxd-export.pdf-0185-02.png)

<!-- Trang 186 -->

### UC06.00.02 - Xem chi tiết phiếu cấp dầu

#### 1. Thông tin chung

|Mã UC|UC06.00.02|
|---|---|
|Tên UC|Xem chi tiết phiếu cấp dầu|
|Tác nhân|Lái xe · Nhân viên · CBQL — có quyền xem phiếu|
|Đường dẫn|UC06.00.01 Danh sách → Tap card bất kỳ|
|Điều kiện trước|Đã đăng nhập.<br>Phiếu tồn tại.<br>Người dùng có quyền xem.|
|Điều kiện sau|Hiển thị thông tin phiếu theo trạng thái.<br>Actions thực hiện được theo quyền.|

#### 2. Lưu đồ hoạt động

1. Người dùng tap card phiếu từ danh sách → navigate màn chi tiết (slide-in từ phải, 300ms).

2. Hệ thống load và hiển thị theo trạng thái phiếu + quyền người dùng.

3. Người dùng xem thông tin, thực hiện action phù hợp (xem Action Matrix Mục 4).

4. Tap icon "..." góc phải header → Xem lịch sử hoạt động (MSC-05) - chỉ áp dụng cho nội bộ,

không áp dụng cho Delta Partner Portal.

5. Tap Back → về danh sách.

**3. Cấu trúc màn hình**

##### 3.1 Header (cố định)

![](images/ndlxd-export.pdf-0186-11.png)

|Thành phần|Mô tả|
|---|---|

<!-- Trang 187 -->

|Button Back (←)|Navigate về danh sách.|
|---|---|
|Tiêu đề|"Phiếu cấp dầu".|
|Badge loại|dGas1 / dGas2 / ... / Cấp bù — màu theo loại (fixed theo UI, consistent).|
|Separator "\|"|Ký tự phân cách.|
|Mã phiếu|PCD-[Mã chi nhánh]-[2 số] (theo<br>).<br>Chỉ hiển thị sau khi phiếu được phê duyệt.<br>Trước phê duyệt: ẩn.<br>UC00.00.07|
|Dot trạng thái|● [Nhãn trạng thái] — màu theo state.|
|Button "..."|Góc phải.<br>Tap → "Xem lịch sử hoạt động".|

##### 3.2 Tab (theo phương thức)

![](images/ndlxd-export.pdf-0187-02.png)

|Phương thức nhận<br>dầu|Tabs hiển thị|
|---|---|
|Cây dầu nội bộ|Không có tab — chỉ hiển thị màn Chung dạng scroll|
|Cây dầu mua ngoài|Chung \| Bơm dầu \| Hóa đơn|
|Hóa đơn lẻ|Chung \| Bơm dầu \| Hóa đơn|

Tab mặc định khi mở: Chung (trừ khi navigate từ action "Xem thông tin chi tiết" sau ghi nhận

bơm/xuất HĐ → active tab tương ứng).

#### 4. Action Matrix — Button actions theo trạng thái và quyền

Dựa theo lưu đồ trạng thái và các UCs để thể hiện actions. Đối với các hành động cập

nhật/chỉnh sửa, đưa vào icon …

#### 5. Mô tả Hero card theo trạng thái

<!-- Trang 188 -->

![](images/ndlxd-export.pdf-0188-00.png)

![](images/ndlxd-export.pdf-0188-01.png)

Dạng thực nhận của dGas 5

![](images/ndlxd-export.pdf-0188-03.png)

Dạng thực nhận của nội bộ (hình trước) và mua ngoài/hoá đơn lẻ (hình sau)

Hero card là component nổi bật đầu trang, hiển thị metric chính và thay đổi nội dung theo trạng

thái.

|Trạng thái|Nền|Nội dung hero card|
|---|---|---|
|draft /<br>pending /<br>approved_wa|Màu loại dGas|Icon loại + Tên + Mô tả ngắn · "SỐ DẦU XIN CẤP: X L"|

<!-- Trang 189 -->

|iting /<br>waiting /<br>purchase_pe<br>nding /<br>purchase_fu<br>el_pending /<br>purchase_in<br>voicing /<br>purchase_in<br>voice_pendi<br>ng / recalle<br>d / rejected|||
|---|---|---|
|igas_active|Màu loại dGas|Icon loại + Tên + Mô tả · "SỐ DẦU XIN CẤP: X L"|
|igas_expire<br>d|Màu loại dGas<br>(mờ hơn)|Icon loại + Tên + Mô tả · "SỐ DẦU XIN CẤP: X L"|
|fuel_done /<br>invoice_don<br>e|Màu loại dGas|Icon loại + Tên + Mô tả · "THỰC NHẬN: X L" · BẮT ĐẦU<br>HH:mm · KẾT THÚC HH:mm · THỜI LƯỢNG X phút (badge)|
|po_expired|Màu loại dGas<br>(mờ hơn)|Icon loại + Tên · "SỐ DẦU XIN CẤP: X L"|
|done (cây nội<br>bộ / mua ngoài)|Màu loại dGas|Icon loại + Tên · "THỰC NHẬN: X L" · Progress bar (% thực<br>nhận / xin cấp) · BẮT ĐẦU · KẾT THÚC · THỜI LƯỢNG|
|done (dGas5<br>— thừa)|Xanh lá đậm|"DẦU THỪA: X L" (trái) · "Thưởng lương tháng: +X đ" (phải) ·<br>Badge kỳ tháng<br>Giá trị thường = Số lít dầu thừa * đơn giá dầu hiện tại trước<br>thuế<br>Số lít dầu thừa = tổng số lít dầu chưa bơm ở các phiếu cấp<br>dầu còn dư.|
|done (dGas5<br>— thiếu)|Đỏ tối|"DẦU THIẾU: X L" · "Phạt lương tháng: −X đ"<br>Giá trị thường = số lít dầu thiếu * đơn giá dầu hiện tại sau<br>thuế|

![Trang 189 — ảnh xem trước để đối chiếu hình vẽ](images/page-189.png)

<!-- Trang 190 -->

|done (dGas5<br>— hòa)|Xám tối|"DẦU THỪA/THIẾU: 0 L" · "Điều chỉnh lương: 0 đ"|
|---|---|---|

#### 6. Mô tả Tab Chung — theo trạng thái

##### 6.1 Banner cảnh báo (xuất hiện trên đầu tab Chung, trên hero card)

|Trạng thái|Banner|
|---|---|
|po_expired|🔴 Nền đỏ nhạt · "Phiên đã hết hiệu lực. Phiếu này đã phát hành<br>quá 24 giờ mà chưa được thực hiện. Phiếu không còn hiệu lực –<br>vui lòng tạo phiếu mới để tiếp tục nhận dầu." + Badge đỏ nhỏ<br>"Hết hạn lúc HH:mm dd/mm/yyyy".|
|igas_expired|(không dùng banner — dùng Card Hết hiệu lực trong nội dung)|

##### 6.2 Components theo phương thức + trạng thái

**Cây nội bộ:**

|Trạng thái|Components hiển thị trên Tab Chung|
|---|---|
|approved_waiti<br>ng|Section Phương thức nhận dầu (read-only)<br>Section Thông tin khác<br>Button "Cấp mã Igas"|
|igas_active|Card Mã Igas hiện tại (STT 3.2 UC10)<br>Section Phương thức nhận dầu<br>Section Thông tin khác|

![Trang 190 — ảnh xem trước để đối chiếu hình vẽ](images/page-190.png)

<!-- Trang 191 -->

|igas_expired|Card Tiền phạt + Mã hết hạn (STT 3.3 UC10)<br>Section Phương thức nhận dầu<br>Section Thông tin khác<br>Checkbox + Button "Cấp lại mã Igas"|
|---|---|
|igas_active<br>(lần 2+)|Card Mã Igas mới<br>Card Tiền phạt (persistent bên dưới)<br>Các sections còn lại|
|done|Hero card THỰC NHẬN<br>Card Tiền phạt (nếu có, persistent)<br>Section Phương thức<br>Section Thông tin khác|

**Cây mua ngoài + HĐ lẻ (Tab Chung):**

|Trạng thái|Tab Chung hiển thị|
|---|---|
|pending /<br>approved_waiting /<br>waiting|Section Phương thức nhận dầu<br>Section Thông tin khác|
|po_expired|Banner đỏ (hết hạn)<br>Section Phương thức<br>Section Thông tin khác<br>Button "Tạo lại"|
|fuel_done → done|Section Phương thức<br>Section Thông tin khác (tab Bơm dầu + Hóa đơn chứa chi tiết)|

##### 6.3 Section Phương thức nhận dầu (Tab Chung — read-only)

![Trang 191 — ảnh xem trước để đối chiếu hình vẽ](images/page-191.png)

<!-- Trang 192 -->

![](images/ndlxd-export.pdf-0192-00.png)

![](images/ndlxd-export.pdf-0192-01.png)

![](images/ndlxd-export.pdf-0192-02.png)

|Thành phần|Mô tả|
|---|---|
|Label loại phương thức|"Cây dầu nội bộ" / "Cây dầu mua ngoài" / "Hóa đơn lẻ".<br>Kèm link "Xem quy trình ›".|
|Card cây dầu|Tên cây (bold) + Badge "Cây dầu gốc" ⭐ (nếu có) + 📍 X km + ⏱ X<br>phút + ⛽ X L tồn (nội bộ) / Đủ hạn mức (mua ngoài).<br>Button "Xem đường đi ›" → Google Maps.|

##### 6.4 Section Thông tin khác (Tab Chung — read-only)

![](images/ndlxd-export.pdf-0192-05.png)

|Thành phần|Mô tả|
|---|---|
|Người yêu cầu|Card: Avatar + Tên + Mã NV + Chức vụ.|
|Ngày yêu cầu|dd/mm/yyyy|

<!-- Trang 193 -->

|Ghi chú|Giá trị đã nhập.<br>Ẩn hoàn toàn nếu trống (App Common 2.10).|
|---|---|

**Thêm với loại phiếu đặc thù:**

![](images/ndlxd-export.pdf-0193-04.png)

![](images/ndlxd-export.pdf-0193-05.png)

![](images/ndlxd-export.pdf-0193-06.png)

<!-- Trang 194 -->

![](images/ndlxd-export.pdf-0194-00.png)

![](images/ndlxd-export.pdf-0194-01.png)

|Loại|Thêm vào Section Thông tin yêu cầu|
|---|---|
|dGas2|Section "Lệnh sửa chữa": Mã lệnh SC + card Kỹ thuật viên.|
|dGas3|Section "Lệnh vận chuyển": Danh sách mã lệnh VC + ngày + số lít từng lệnh.|
|dGas4|Mục đích + Card thông tin xe (biển số + loại xe + tên xe).|
|dGas5|Section "Tính toán dầu chốt tháng": card xe + dung tích bình + tiêu thụ ước<br>tính + danh sách phiếu trong tháng + tổng lượng dầu.|
|Cấp bù|Section "Phiếu gốc": mã phiếu gốc + ngày + Số lít xin cấp / Đã bơm thực tế /<br>Còn lại (vàng đậm).|

##### 6.5 Section Hướng dẫn thực hiện

Giao diện fixed theo UI.

Content trên giao diện như sau:

<!-- Trang 195 -->

**1. Chuẩn bị bơm dầu**

1. Đối chiếu thông tin phiếu cấp với lái xe và biển số xe.

2. Bơm đúng số lít theo phiếu — không được bơm thừa hoặc thiếu. Trong trường hợp dầu đã đầy

bình, có thể kết thúc bơm.

3. Chụp ảnh màn hình máy bơm cây dầu để làm bằng chứng.

**2. Ghi nhận bơm dầu**

1. Mở phiếu trên app, tap Bơm ngay/Ghi nhận bơm dầu.

2. Nhập số lít thực tế đã bơm và thời gian bắt đầu — kết thúc.

3. Upload ảnh màn hình máy bơm đã chụp.

4. Tap Ghi nhận bơm dầu để xác nhận.

**3. Xuất hoá đơn**

1. Tap Xuất hóa đơn trên phiếu đã ghi nhận bơm xong.

2. Chọn số hoá đơn từ danh sách hoặc nhập thủ công nếu chưa có.

3. Upload file hoá đơn (PDF hoặc ảnh chụp).

4. Tap Hoàn thành để gửi hoá đơn cho hệ thống.

**4. Chốt phiếu**

1. Kiểm tra lại thông tin bơm dầu và hoá đơn đã chính xác chưa.

2. Tap "Chốt phiếu" để đóng phiếu và hoàn tất giao dịch.

3. Xác nhận trong hộp thoại — sau khi chốt không thể chỉnh sửa.

#### 7. Tab Bơm dầu

![](images/ndlxd-export.pdf-0195-19.png)

Chỉ có ở phiếu cây mua ngoài + HĐ lẻ.

<!-- Trang 196 -->

|Trạng thái|Nội dung Tab Bơm dầu|
|---|---|
|waiting / pending /<br>purchase_pending /<br>purchase_fuel_pendin<br>g /<br>purchase_invoicing /<br>purchase_invoice_pend<br>ing (chưa ghi nhận)|MSC-09 Empty state: illustration + "Chưa có thông tin bơm dầu"<br>+ "Phiếu cấp dầu chưa được ghi nhận bơm dầu." + Button "Ghi<br>nhận bơm dầu" (nếu user có quyền)|
|fuel_done /<br>invoice_done / done|Hero card THỰC NHẬN<br>Section Thông tin bơm dầu: Badge "Đã bơm xong" (xanh, right-<br>align) + Thời gian bơm + Đơn giá + THÀNH TIỀN (xanh lá, bold)<br>Section Hình ảnh bơm dầu: lưới thumbnail ảnh đã chụp<br>Button "Xuất hoá đơn" (nếu chưa xuất)<br>Button "Cập nhật bơm dầu" (nếu chưa xuất HĐ) trong icon …|

#### 8. Tab Hóa đơn

![](images/ndlxd-export.pdf-0196-02.png)

Chỉ có ở phiếu cây mua ngoài + HĐ lẻ.

|Trạng thái|Nội dung Tab Hóa đơn|
|---|---|
|fuel_done (chưa xuất HĐ)|MSC-09 Empty state: illustration + "Chưa có thông tin hóa đơn"<br>+ "Tạo hóa đơn để ghi nhận giao dịch!"|

<!-- Trang 197 -->

Button "Xuất hóa đơn"

|invoice_done /<br>purchase_invoice_pend<br>ing / done|Section Thông tin hóa đơn: Số hóa đơn + Ký hiệu hóa đơn + Mã<br>tra cứu<br>LINK TRUY CẬP HĐDT: URL rút gọn + icon Copy<br>Button "Mở cổng tra cứu" (full-width, primary, icon external-link<br>→ mở browser)<br>Section Hóa đơn: Danh sách file (icon PDF/JPG + tên file + kích<br>thước). Tap → xem full.<br>Button "Cập nhật hoá đơn" (chỉ khi chưa qua vòng duyệt tiếp<br>theo)|
|---|---|

#### 9. Action - Thu hồi phiếu

Không có màn hình riêng — xử lý inline trên màn chi tiết.

1. Người tạo tap "Thu hồi" (chỉ hiển thị khi pending ).

2. MSC-02 Confirm cho hành động thu hồi.

3. Xác nhận → Phiếu → recalled → refresh màn.

4. Button "Tạo lại" hiện → reset phiếu về pending (không tạo mới, giữ dữ liệu).

#### 10. Action - Tạo lại

Áp dụng với rejected / recalled / po_expired .

|Thành phần|Mô tả|
|---|---|
|Button "Tạo lại"|Full-width, primary xanh lá.|
|Hành động|Không tạo phiếu mới — reset phiếu hiện tại về pending , giữ nguyên toàn<br>bộ dữ liệu và lịch sử Activity Log.|
|Activity Log|Ghi thêm entry: [Tên] đã tạo lại — Phiếu reset về trạng thái Chờ phê duyệt.|

Đặc biệt với po_expired : Tạo lại từ PO hết hạn cũng reset về pending

(nếu TH2) hoặc thẳng waiting (nếu TH4) — không qua màn tạo mới từ đầu.

![Trang 197 — ảnh xem trước để đối chiếu hình vẽ](images/page-197.png)

<!-- Trang 198 -->

### UC06.00.03 - Tạo mới phiếu dGas1 (Cấp dầu quản lý)

#### 1. Thông tin chung

|Mã UC|UC06.00.03|
|---|---|
|Tên UC|Tạo mới phiếu cấp dầu dGas1 — Cấp dầu quản lý|
|Tác nhân|Quản lý|
|Đường dẫn|UC06.00.01 Danh sách → Button "Tạo mới" → Chọn dGas1 → Tiếp tục|
|Điều kiện trước|Người dùng đã đăng nhập.<br>Người dùng có chức vụ quản lý.<br>Có định mức tháng (đối với nhân viên hoặc đối với phương tiện) còn lại ><br>0.|
|Điều kiện sau|Lưu nháp: phiếu trạng thái draft , chỉ người tạo thấy.<br>Submit: phiếu trạng thái pending / approved_waiting / waiting ,<br>gửi in-app notification (MSC-01) đến người có quyền phê duyệt, lưu lịch<br>sử hoạt động.|

#### 2. Lưu đồ hoạt động

1. Người dùng chọn dGas1 và tap "Tiếp tục" từ bottom sheet chọn loại.

2. Hệ thống navigate đến màn Tạo phiếu dGas1. Header hiển thị Badge "dGas1".

3. Người dùng chọn Mục đích cấp dầu:

Nhánh A — "Sử dụng xe công ty": Hệ thống kiểm tra xe của nhân viên → hiển thị thẻ Định

mức theo nhân viên hoặc Định mức theo phương tiện.

Nhánh B — "Sử dụng cho hoạt động công ty": Hiển thị dropdown chọn Hoạt động (Chạy

máy phát điện / Xe nâng / Vận hành xe cứu hộ / Hoạt động khác → cho nhập mục đích tự

do).

Nhánh C — "Nhận xe mới mua": Hiển thị info message "Xe mới mua cần bổ sung thông tin

danh mục để xin cấp dầu." + trường chọn Biển số xe.

Nhánh D — "Mục đích khác": Hiển thị Input nhập mục đích tự do.

4. Người dùng nhập Số lít yêu cầu. Tap vào ô → bàn phím số + Quick-fill Chips xuất hiện.

![Trang 198 — ảnh xem trước để đối chiếu hình vẽ](images/page-198.png)

<!-- Trang 199 -->

5. Người dùng chọn Phương thức nhận dầu. Mặc định tự chọn cây gốc của nhân viên.

6. Người dùng xem/chỉnh Thông tin khác (nhân viên nhận dầu, ngày, ghi chú).

7. Footer bar cập nhật realtime: "Số lít: X L | Nơi nhận dầu: [Tên cây]".

8. Người dùng chọn hành động cuối:

Nhánh "Lưu nháp":

Không validate bắt buộc.

Lưu phiếu trạng thái draft .

Không có UI feedback — navigate về màn danh sách.

Nhánh "Tạo mới":

Validate toàn bộ trường bắt buộc. Nếu lỗi: scroll đến trường lỗi đầu tiên, hiển thị error

inline/popup.

Nếu hợp lệ:

Tạo mới bản ghi.

Hệ thống xác định luồng phê duyệt theo Bảng Approval Matrix (Mục 5), sau đó:

Không cần phê duyệt (TH1/TH3 — cây nội bộ): Tạo phiếu → approved_waiting

→ không gửi notify → hiển thị MSC-11 Popcon thành công.

Không cần phê duyệt (TH4 — cây mua ngoài): Tạo phiếu → waiting → MSC-01

notify NV cây dầu qua Partner Portal → hiển thị MSC-11 Popcon thành công.

Cần phê duyệt (TH2/TH5): Tạo phiếu → pending → MSC-01 notify người có

quyền phê duyệt → hiển thị MSC-11 Popcon thành công.

Lưu lịch sử hoạt động mới.

9. Người dùng tap Back khi form đang có dữ liệu chưa lưu → Common 2.13 Unsaved Changes

(xem Ghi chú màn hình).

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tạo phiếu dGas1

<!-- Trang 200 -->

![](images/ndlxd-export.pdf-0200-00.png)

||Tên thành<br>phần|Cont<br>rol|Loại|Bắt<br>buộc|Giá<br>trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Header|Label|Text|—|—|"Tạo phiếu cấp dầu" +<br>Badge "dGas1" (vàng) góc<br>phải.|—|

<!-- Trang 201 -->

|||||||Button back (←).||
|---|---|---|---|---|---|---|---|
|2|Section Thông tin yêu cầu|||||||
|3|Mục đích<br>cấp dầu|Selec<br>t|List|Có|—|Placeholder "Chọn mục<br>đích".<br>Các giá trị: Sử dụng xe công<br>ty / Sử dụng cho hoạt động<br>công ty / Nhận xe mới mua /<br>Mục đích khác.<br>Khi thay đổi mục đích: các<br>trường phụ thuộc (STT 4–8)<br>reset + re-render. Validate<br>on blur + on submit.|"Vui lòng<br>chọn mục đích<br>cấp dầu."|
|4|Hoạt động<br>công ty|Selec<br>t|List|Hidd<br>en|—|Chỉ hiển thị khi Mục đích =<br>"Sử dụng cho hoạt động<br>công ty".<br>Giá trị: Chạy máy phát điện<br>văn phòng / Xe nâng / Vận<br>hành xe cứu hộ / Hoạt động<br>khác.|"Vui lòng<br>chọn hoạt<br>động công<br>ty."|
|5|Mô tả hoạt<br>động|Input|Text|Hidd<br>en|—|Chỉ hiển thị khi Hoạt động =<br>"Hoạt động khác".<br>Nhập tự do.<br>Max 200 ký tự.<br>Placeholder "Mô tả hoạt<br>động…"|"Vui lòng<br>nhập mô tả<br>hoạt động."|
|6|Biển số xe|Selec<br>t|List|Hidd<br>en|—|Chỉ hiển thị khi Mục đích =<br>"Nhận xe mới mua".<br>Dropdown tìm kiếm biển số.|"Vui lòng<br>chọn biển số<br>xe."|

![](images/ndlxd-export.pdf-0201-03.png)

<!-- Trang 202 -->

|||||||Lấy danh sách toàn bộ<br>phương tiện của chi nhánh.||
|---|---|---|---|---|---|---|---|
|7|Info<br>message xe<br>mới|Bann<br>er|—|Hidd<br>en|—|Chỉ hiển thị khi Mục đích =<br>"Nhận xe mới mua".<br>Nội dung: "Xe mới mua cần<br>bổ sung thông tin danh mục<br>để xin cấp dầu." Màu xanh<br>dương nhạt.|—|
|8|Thẻ Định<br>mức|Card|—|Hidd<br>en|—|Chỉ hiển thị khi Mục đích =<br>"Sử dụng xe công ty".<br>Xem 2 biến thể bên dưới<br>(STT 9 / 10).<br>Hệ thống check theo nhân<br>viên để xem áp định mức<br>theo cái nào.<br>Nếu nhân viên có định mức<br>→ sử dụng định mức của<br>nhân viên.<br>Nếu có định mức của<br>phương tiện → sử dụng của<br>phương tiện.<br>→ Hiển thị định mức (UI)<br>theo đối tượng|—|
|9|Thẻ Định<br>mức theo<br>nhân viên|Card|—|—|—|Header "Định mức theo<br>nhân viên".<br>Card nhỏ: Avatar (chữ tắt,<br>nền xanh nếu không có) +<br>Tên + Mã NV + Chức vụ.<br>Phần "ĐỊNH MỨC THÁNG":<br>[X L đã dùng] ←progress|—|

![Trang 202 — ảnh xem trước để đối chiếu hình vẽ](images/page-202.png)

<!-- Trang 203 -->

|||||||bar→ [Y L còn lại].<br>Bên dưới bar: "X% đã dùng"<br>(xanh) + "Y% còn lại" (xám).||
|---|---|---|---|---|---|---|---|
|1<br>0|Thẻ Định<br>mức theo<br>phương tiện|Card|—|—|—|Header "Định mức theo<br>phương tiện". Card nhỏ:<br>Icon xe + Biển số + Loại xe.<br>Phần "ĐỊNH MỨC THÁNG":<br>tương tự 9.|—|
|1<br>1|Section Số lượng|||||||
|1<br>2|Số lít yêu<br>cầu|Input|Num<br>ber|Có|0|Suffix "L".<br>Tap → bàn phím số +<br>(Mục 3.4).<br>BIZ = định mức tháng còn<br>lại của nhân viên.<br>Quick-<br>fill Chips|"Vui lòng<br>nhập số lít<br>yêu cầu." ·<br>"Số lít phải<br>lớn hơn 0."<br>Warn vượt định<br>mức: "Vượt<br>định mức<br>tháng còn lại<br>(X lít)."|
|1<br>3|Section Phương thức nhận dầu:|||||||

![](images/ndlxd-export.pdf-0203-00.png)

![](images/ndlxd-export.pdf-0203-01.png)

<!-- Trang 204 -->

![](images/ndlxd-export.pdf-0204-00.png)

Icon bơm + label "Phương thức nhận dầu". Radio group 3 option xếp dọc.

Mặc định tự chọn option có cây gốc của nhân viên.

|1<br>4|Option A —<br>Cây dầu nội<br>bộ|Radio<br>Card|—|—|Chọn<br>nếu<br>cây<br>gốc<br>là nội<br>bộ|Card có border xanh khi<br>selected.<br>Gồm: Radio + "Cây dầu nội<br>bộ" (bold) + mô tả "Tự đổ<br>qua mã Igas" + Badge "Ưu<br>tiên 1" (xanh lá) nếu cây<br>gốc là nội bộ, "Ưu tiên 2"<br>nếu không + Link "Xem quy<br>trình ›" mở Bottom Sheet<br>mô tả quy trình (xem thêm ở<br>3.2).<br>Khi selected → hiện sub-<br>section chọn cây (STT 15).|—|
|---|---|---|---|---|---|---|---|

![](images/ndlxd-export.pdf-0204-02.png)

![](images/ndlxd-export.pdf-0204-04.png)

<!-- Trang 205 -->

|1<br>5|Sub-section<br>chọn cây<br>nội bộ|Radio<br>List|—|—|—|Header xám nhỏ: "CHỌN<br>CÂY DẦU NỘI BỘ".<br>Hiển thị khi Option A được<br>chọn, slide-down animation.<br>Mỗi card cây: Tên cây +<br>Badge "Cây dầu gốc" (nếu<br>là cây gốc của xe) + X km +<br>X phút + X L tồn + Button<br>"Xem đường đi ›" (link<br>Google Maps chỉ đường từ<br>vị trí hiện tại).<br>Giá trị tồn kho của cây dầu<br>nội bộ lấy theo giá trị<br>available = giá trị tồn kho<br>actual - số dầu chưa bơm ở<br>các phiếu cấp dầu đã phê<br>duyệt - lượng dầu vận hành<br>tối thiểu<br>Dùng API bên thứ 3(GG<br>Maps/Vietmap) để lấy<br>khoảng cách quãng đưỡng<br>và thời gian ước tính di<br>chuyển từ vị trí hiện tại đến<br>cây dầu đích.<br>Cây tồn kho < số lít yêu cầu:<br>disabled + warning inline<br>màu vàng "⚠ Tồn kho<br>không đủ."||
|---|---|---|---|---|---|---|---|
|1<br>6|Option B —<br>Cây dầu<br>mua ngoài|Radio<br>Card|—|—|Chọn<br>nếu<br>cây<br>gốc<br>là|Badge "Ưu tiên 1" (xanh lá)<br>nếu cây gốc là mua ngoài,<br>"Ưu tiên 2" nếu không.<br>Mô tả: "Giao phiếu cho nhân<br>viên cây dầu ngoài đổ dầu".|—|

![Trang 205 — ảnh xem trước để đối chiếu hình vẽ](images/page-205.png)

<!-- Trang 206 -->

||||||mua<br>ngoài|Khi selected → hiện banner<br>cảnh báo vàng "TP điều vận<br>cần phê duyệt phiếu trước.<br>Thời gian chờ từ 10–30<br>phút." + sub-section chọn<br>cây mua ngoài (STT 17).|
|---|---|---|---|---|---|---|
|1<br>7|Sub-section<br>chọn cây<br>mua ngoài|Radio<br>List|—|—|—|Header xám nhỏ: "CHỌN<br>CÂY DẦU MUA NGOÀI".<br>Tương tự 15 nhưng thay ⛽<br>tồn kho bằng ⛽ "Đủ hạn<br>mức" hoặc "Thiếu X L"<br>(theo hạn mức danh mục<br>cây dầu mua ngoài, lấy<br>realtime giá trị này = hạn<br>mức cấp dầu còn lại - số<br>dầu xin cấp ).<br>Cây hạn mức không đủ:<br>disabled + "⚠ Hạn mức<br>không đủ."|
|1<br>8|Option C —<br>Hóa đơn lẻ|Radio<br>Card|—|—|—|Badge "Ưu tiên 3" (hồng).<br>Mô tả: "Tự đổ bên ngoài và<br>lấy hoá đơn về". Khi|

![](images/ndlxd-export.pdf-0206-01.png)

<!-- Trang 207 -->

|||||||selected → hiện banner<br>vàng "Chỉ được dùng trong<br>giờ hành chính và khi cây<br>nội bộ + cây ngoài đều<br>không khả dụng. Giám đốc<br>phê duyệt trước khi bơm." +<br>sub-section "CHỈ ĐƯỢC<br>MUA TẠI PETROLIMEX" +<br>Button "Tìm Petrolimex gần<br>đây ›" (link Google Maps).|
|---|---|---|---|---|---|---|
|1<br>9|Yêu cầu vị<br>trí|Syste<br>m|—|—|—|Nếu thiết bị chưa cấp quyền<br>vị trí: hiện Bottom Sheet yêu<br>cầu "Cho phép truy cập vị<br>trí để tính khoảng cách cây<br>dầu gần nhất."<br>Button "Cho phép" / "Bỏ<br>qua".<br>Nếu bỏ qua thì phần khoảng<br>cách, thời gian sẽ hiện no<br>data “-”.<br>Nếu tap "Xem đường đi" /<br>"Tìm Petrolimex" mà chưa<br>cài Google Maps: dialog<br>"Cần cài Google Maps để<br>xem đường đi. Tải về?" →<br>link App Store/CH Play.|
|2<br>0|Section Thông tin khác||||||

![](images/ndlxd-export.pdf-0207-01.png)

<!-- Trang 208 -->

|2<br>1|Nhân viên<br>nhận dầu|Card|—|Khôn<br>g|Ngườ<br>i<br>đang<br>đăng<br>nhập|Card nhỏ: Avatar + Tên +<br>Mã NV + Chức vụ.<br>Read-only, không chỉnh sửa.|—|
|---|---|---|---|---|---|---|---|
|2<br>2|Ngày yêu<br>cầu|Label|Date<br>Time|—|Thời<br>điểm<br>hiện<br>tại|Format: DD/MM/YYYY<br>HH:mm.<br>Read-only.|—|
|2<br>3|Ghi chú|Texta<br>rea|Text|Khôn<br>g|—|Placeholder "Nhập thông tin<br>ghi chú".|—|
|2<br>4|Footer Bar|Label|—|—|—|Cố định bottom (trên<br>button).<br>2 cột: "Số lít: X L" "Nơi nhận<br>dầu: [Tên cây]".<br>Cập nhật realtime.<br>Hiện "-" khi chưa điền.||
|2<br>5|Button Lưu<br>nháp|Butto<br>n|—|—|—|Secondary.<br>Xử lý theo bước 8 - Nhánh<br>Lưu nháp (Lưu đồ hoạt<br>động)|—|
|2<br>6|Button Tạo<br>mới|Butto<br>n|—|—|—|Primary "Tạo mới →".<br>Validate toàn bộ.<br>Nếu hợp lệ → xử lý theo<br>bước 8 - Nhánh Tạo mới<br>(Lưu đồ hoạt động)<br>Lịch sử hoạt động, thông<br>báo chi tiết xem ở tài liệu<br>tổng hợp<br>.<br>Thông báo và lịch<br>sử hoạt động của phiếu cấp<br>dầu|—|

![Trang 208 — ảnh xem trước để đối chiếu hình vẽ](images/page-208.png)

<!-- Trang 209 -->

Nếu lỗi → scroll đến trường
lỗi đầu tiên.

**Ghi chú màn hình:**

Khi người dùng tap Back khi form đang có dữ liệu chưa lưu → hiển thị

Confirm Dialog (MSC-02)

Khi Mục đích thay đổi: các trường phụ thuộc reset về giá trị mặc định. Thẻ

Định mức (STT 8) xuất hiện với slide-down animation nếu Mục đích = "Sử

dụng xe công ty".

##### 3.2 Xem quy trình

![](images/ndlxd-export.pdf-0209-01.png)

Cần bổ sung content cho 3 loại phương thức

##### 3.3 Màn hình Popcon

![](images/ndlxd-export.pdf-0209-02.png)

![](images/ndlxd-export.pdf-0209-07.png)

<!-- Trang 210 -->

![](images/ndlxd-export.pdf-0210-00.png)

Xem thêm .

MSC-11

||Tên thành<br>phần|Cont<br>rol|Loại|Bắt<br>buộc|Giá<br>trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Title<br>popcon|Text|Label|—|—|“Yêu cầu đã gửi”||
|2|Mô tả<br>popcon|Text|Label|—|—|Nếu có luồng phê duyệt<br>phía sau:<br>“Yêu cầu cấp dầu dGas 1 đã<br>được tạo mới và chờ phê<br>duyệt.”||
|3|Các trường<br>quan trọng|Text|Label|—|—|Loại phiếu: dGas 1<br>Phân loại: Chi phí sửa chữa||

<!-- Trang 211 -->

|||||||Phương thức nhận dầu: Lấy<br>phương thức được chọn<br>Số lít dầu: Lấy số lít dầu xin<br>cấp|
|---|---|---|---|---|---|---|
|4|Button Về<br>trang chủ|Butto<br>n|—|—|—|Navigate về trang chủ (màn<br>menu chính).|
|5|Button Xem<br>thông tin<br>chi tiết|Butto<br>n|—|—|—|Navigate về màn xem chi<br>tiết của phiếu cấp dầu hiện<br>tại.|

##### 3.4 Quick-fill Chips (Gợi ý số lít)

![](images/ndlxd-export.pdf-0211-01.png)

**Hiển thị phía trên bàn phím số khi user tap vào ô nhập số lít.**

||Thành phần|Control|Mô tả|
|---|---|---|---|
|1|Chip BIZ|Badge/Button|Màu xanh lá đậm. Label: "Theo [nguồn]" (VD: "Theo lệnh VC",<br>"Theo định mức").<br>Luôn xuất hiện đầu tiên nếu BIZ > 0.<br>Tap → điền giá trị BIZ vào ô input.|
|2|Chip LAST|Badge/Button|Màu xám. Label: "Lần trước".|

![](images/ndlxd-export.pdf-0211-03.png)

<!-- Trang 212 -->

Chỉ hiển thị nếu LAST > 0 và LAST ≠ BIZ.

|3|Chip ROUND|Badge/Button|Màu xám nhạt. Label: giá trị số (bội số 50 gần BIZ nhất).<br>Tối đa 2–3 chip ROUND để tổng ≤ 4 chips.|
|---|---|---|---|
|4|Button Xong|Button|Text xanh, right-aligned.<br>Đóng bàn phím.|
|5|Empty state|—|Ẩn toàn bộ chips nếu BIZ chưa có (chưa chọn xe/lệnh).<br>Hiển thị placeholder "0" trong ô input.|

Thuật toán sinh chips: BIZ → LAST → ROUND (bội số 50, sắp xếp gần BIZ nhất trước) → tổng

≤ 4 chips. Chips render lại mỗi khi context thay đổi (đổi xe, đổi lệnh VC/SC, đổi mục đích).

#### 4. Approval Matrix — Logic phê duyệt theo cây dầu gốc

Cây dầu gốc được cấu hình trong hồ sơ nhân viên (Danh mục nhân viên trên Delta ERP). Khi

user submit phiếu, hệ thống tự động xác định có cần phê duyệt hay không dựa theo bảng sau:

||Cây dầu gốc của lái<br>xe|Phương thức nhận<br>dầu chọn|Cần phê duyệt?|Trạng thái sau<br>submit|
|---|---|---|---|---|
|1|Cây dầu nội bộ|Cây dầu nội bộ|Không|approved_waitin<br>g|
|2|Cây dầu nội bộ|Cây dầu mua ngoài|Có — CBQL phê<br>duyệt|pending|
|3|Cây dầu mua ngoài|Cây dầu nội bộ|Không|approved_waitin<br>g|
|4|Cây dầu mua ngoài|Cây dầu mua ngoài|Không|waiting|
|5|Bất kỳ|Hóa đơn lẻ|Có — CBQL phê<br>duyệt|pending|

![Trang 212 — ảnh xem trước để đối chiếu hình vẽ](images/page-212.png)

<!-- Trang 213 -->

### UC06.00.04 - Tạo mới phiếu dGas2 (Cấp dầu xưởng)

#### 1. Thông tin chung

|Mã UC|UC06.00.04|
|---|---|
|Tên UC|Tạo mới phiếu cấp dầu dGas2 — Cấp dầu xưởng (theo lệnh sửa|
|Tác nhân|Kỹ thuật xưởng, quản lý xưởng,…|
|Đường dẫn|UC06.00.01 Danh sách → Button "Tạo mới" → Chọn dGas2 → Tiếp<br>tục|
|Điều kiện trước|Người dùng đã đăng nhập.<br>Có ≥1 lệnh sửa chữa (SC) trạng thái Đang sửa chữa .|
|Điều kiện sau|Lưu nháp: draft .<br>Submit: approved_waiting (TH1/TH3 — cây nội bộ, không cần<br>duyệt) hoặc pending (TH2 — cần CBQL duyệt), gửi thông báo và<br>lưu lịch sử hoạt động (nếu có)|

chữa)

#### 2. Lưu đồ hoạt động

1. Người dùng chọn dGas2 → tap "Tiếp tục" từ Bottom Sheet chọn loại.

2. Hệ thống navigate đến màn Tạo phiếu dGas2. Badge "dGas2" hiển thị trên header.

3. Người dùng chọn Lệnh sửa chữa — Bottom Sheet tìm kiếm mã lệnh. Hệ thống auto-fill Kỹ

thuật viên từ lệnh đã chọn.

4. Người dùng nhập Số lít yêu cầu. Tap vào ô → bàn phím số + Quick-fill Chips. Validate on blur.

5. Phương thức nhận dầu: Fixed = Cây dầu nội bộ. Không có radio chọn loại khác.

6. Người dùng điền Ghi chú (tuỳ chọn) → chọn Lưu nháp hoặc Tạo mới.

7. Khi tap "Tạo mới": Validate → hệ thống xác định luồng theo Approval Matrix:

TH1/TH3 (cây nội bộ, không cần duyệt): approved_waiting → không gửi notify →

MSC-11 Popcon thành công.

TH2 (cần duyệt): pending → MSC-01 notify người có quyền PD → MSC-11 Popcon thành

công.

![Trang 213 — ảnh xem trước để đối chiếu hình vẽ](images/page-213.png)

<!-- Trang 214 -->

Lưu lịch sử hoạt động mới.

8. Tap Back khi có dữ liệu chưa lưu → MSC-02 Unsaved Changes

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tạo phiếu dGas2

![](images/ndlxd-export.pdf-0214-04.png)

|Tên<br>thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|

<!-- Trang 215 -->

|1|Header|Label|Text|—|—|"Tạo phiếu cấp dầu" + Badge<br>"dGas2"|—|
|---|---|---|---|---|---|---|---|
|2|Stepper|Banne<br>r|—|—|—|Xanh dương nhạt.<br>Hiển thị nodata: "Chọn Lệnh sửa<br>chữa để xem tiến trình nghiệp<br>vụ."<br>Xem thêm ở<br>Loading chạy skeleton loading<br>Sau đó hiển thị:<br>Lấy đúng trường hợp này (Liên<br>module, luồng sửa chữa dùng<br>dầu) được định nghĩa trong<br>.<br>MSC-06<br>tài<br>liệu chung|—|
|3|Section: Lệnh sửa chữa|||||||
|4|Info liên<br>kết|Banne<br>r|—|—|—|Nội dung: "Phiếu dGas2 phải liên<br>kết với Lệnh sửa chữa. Chi phí<br>hạch toán vào CP sửa chữa xe."<br>Màu xanh dương nhạt.|—|
|5|Chọn<br>lệnh sửa<br>chữa|Select|List|Có|—|Placeholder "Tìm mã lệnh".<br>Lấy danh sách lệnh SC đang sửa<br>chữa của chi nhánh.<br>Dropdown tìm kiếm theo mã lệnh<br>SC.|"Vui<br>lòng<br>chọn<br>lệnh sửa<br>chữa."|

![](images/ndlxd-export.pdf-0215-00.png)

<!-- Trang 216 -->

![](images/ndlxd-export.pdf-0216-00.png)

|||||||Hiển thị:<br>Icon thể hiển loại SC: SC<br>PTVT, thay lốp, thay ắc quy<br>Mã lệnh SC<br>Biển kiểm soát - Kỹ thuật viên<br>Chỉ show lệnh SC đang active<br>(Đang sửa chữa)<br>Sau khi chọn:<br>Hiển thị rút gọn: Icon loại - Mã<br>lệnh||
|---|---|---|---|---|---|---|---|
|6|Kỹ thuật<br>viên|Label|Text|—|—|Auto-fill sau khi chọn lệnh SC.<br>Dạng Label read-only, hiển thị tên<br>KTV của lệnh SC.<br>Không hiển thị nếu chưa chọn|—|
|7|Section: Số lượng|||||||
|8|Số lít yêu<br>cầu|Input|Numb<br>er|Có|0|Quick-fill Chips.<br>Follow theo 3.4<br>Không có BIZ.<br>UC06.00.03|"Vui<br>lòng<br>nhập số|

<!-- Trang 217 -->

||||||||lít yêu<br>cầu."<br>"Số lít<br>phải lớn<br>hơn 0."|
|---|---|---|---|---|---|---|---|
|9|Section: Phương thức nhận dầu<br>Chỉ hiển thị Cây dầu nội bộ link với xưởng tương ứng với lệnh SC (bắt buộc, không radio<br>chọn).<br>Hiển thị tên cây + lít tồn.<br>Link "Xem quy trình >" → mở Bottom Sheet mô tả quy trình.|||||||
|1<br>0|Cây dầu<br>nội bộ<br>(fixed)|Card|—|—|Cây<br>dầu<br>gốc<br>của xe|Tên cây + ⛽ X L tồn.<br>Read-only.|—|
|1<br>1|Section: Thông tin khác<br>Nhân viên yêu cầu + Ngày yêu cầu + Ghi chú (tương tự UC06.00.03 STT 21–23).|||||||
|1<br>2|Footer|||||||
|1<br>3|Footer<br>Bar|Label|—|—|—|"Số lượng: X L \| Nơi nhận dầu:<br>[Tên cây]".||

![](images/ndlxd-export.pdf-0217-00.png)

![](images/ndlxd-export.pdf-0217-01.png)

![](images/ndlxd-export.pdf-0217-02.png)

<!-- Trang 218 -->

|1<br>4|Button<br>Lưu nháp|Button|—|—|—|Secondary.<br>Không validate bắt buộc.<br>Lưu phiếu trạng thái draft .<br>Không có UI feedback —<br>navigate về màn danh sách.|—|
|---|---|---|---|---|---|---|---|
|1<br>5|Button<br>Tạo mới|Button|—|—|—|Primary "Tạo mới →".<br>Validate toàn bộ.<br>Nếu hợp lệ → xử lý theo bước 7 -<br>Nhánh Tạo mới (Lưu đồ hoạt<br>động)<br>Lịch sử hoạt động, thông báo chi<br>tiết xem ở tài liệu tổng hợp<br>.<br>Nếu lỗi → scroll đến trường lỗi<br>đầu tiên.<br>Thông<br>báo và lịch sử hoạt động của<br>phiếu cấp dầu||

##### 3.2 Màn hình Popcon

Giống Popcon chỉ khác:

mục 3.3 UC06.00.03

Thay mã dGas 1 → dGas 2

Thay phân loại là chi phí sửa chữa

![Trang 218 — ảnh xem trước để đối chiếu hình vẽ](images/page-218.png)

<!-- Trang 219 -->

### UC06.00.05 - Tạo mới phiếu dGas3 (Cấp dầu vận tải)

#### 1. Thông tin chung

|Mã UC|UC06.00.05|
|---|---|
|Tên UC|Tạo mới phiếu cấp dầu dGas3 — Cấp dầu vận tải (theo lệnh VC tích lũy)|
|Tác nhân|Lái xe|
|Đường dẫn|UC06.00.01 Danh sách → Button "Tạo mới" → Chọn dGas3 → Tiếp tục|
|Điều kiện trước|Đã đăng nhập.<br>Có ≥1 lệnh vận chuyển (VC) đã hoàn thành chưa xin cấp dầu.<br>Tháng trước đã hoàn thành chốt dầu (pre-check tại<br>).<br>UC06.00.01|
|Điều kiện sau|Lưu nháp: draft .<br>Submit:<br>Tạo bản ghi mới trạng thái approved_waiting (TH1/TH3),<br>waiting (TH4), hoặc pending (TH2/TH5).<br>Thông báo<br>Lưu lịch sử hoạt động<br>Hiển thị popcon|

#### 2. Lưu đồ hoạt động

1. Người dùng chọn dGas3 → tap "Tiếp tục" (đã qua pre-check chốt dầu tháng trước tại

UC06.00.01).

2. Hệ thống load danh sách lệnh VC đã hoàn thành chưa xin cấp dầu của lái xe → hiển thị

section "Dầu tích lũy từ hệ thống".

3. Số lít cấp = tổng lít theo tất cả lệnh VC — read-only, lái xe không nhập tuỳ ý.

4. Người dùng chọn Phương thức nhận dầu — Radio group 3 option (STT 8a/b/c).

5. Người dùng điền Ghi chú (tuỳ chọn) → chọn Lưu nháp hoặc Tạo mới.

6. Khi tap "Tạo mới": Validate → hệ thống xác định luồng theo Approval Matrix:

a. TH1/TH3 (cây nội bộ, không cần duyệt): approved_waiting → không gửi notify →

MSC-11 Popcon.

![Trang 219 — ảnh xem trước để đối chiếu hình vẽ](images/page-219.png)

<!-- Trang 220 -->

b. TH4 (cây mua ngoài, không cần duyệt): waiting → MSC-01 notify NV cây (Partner

Portal) → MSC-11 Popcon.

c. TH2/TH5 (cần duyệt): pending → MSC-01 notify người có quyền PD → MSC-11 Popcon.

d. Tất cả các trường hợp đều lưu lịch sử hoạt động mới.

7. Tap Back khi có dữ liệu → MSC-02 Unsaved Changes.

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tạo phiếu dGas3

<!-- Trang 221 -->

![Trang 221 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0221-00.png)


<!-- Trang 222 -->

||Tên<br>thành<br>phần|Con<br>trol|Loại|Bắt<br>buộ<br>c|Giá<br>trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Header|Labe<br>l|Text|—|—|"Tạo phiếu cấp dầu" + Badge "dGas3"|—|
|2|Section: Dầu tích lũy từ hệ thống|||||||
|3|Info<br>banner|Bann<br>er|—|—|—|"Số liệu lấy tự động từ Lệnh vận<br>chuyển. Không thể chỉnh sửa."<br>Màu xanh dương nhạt.|—|
|4|Danh<br>sách lệnh<br>VC|List<br>Card|—|—|—|Mỗi card: Mã lệnh VC + Ngày hoàn<br>thành + ⛽ Số lít theo lệnh.<br>Không tương tác — chỉ xem.|—|
|5|Card<br>tổng dầu|Card|—|—|—|Nền tím/xanh đậm. "Tổng dầu được<br>cấp · X Lệnh vận chuyển: Y lít".<br>Font lớn, màu trắng.<br>Đếm số lượng lệnh vận chuyển chưa<br>cấp dầu.|—|
|6|Section: Số lượng|||||||

![](images/ndlxd-export.pdf-0222-00.png)

<!-- Trang 223 -->

|7|Số lít cấp|Inpu<br>t|Num<br>ber|—|Tổng<br>lệnh<br>VC|Read-only (disabled).<br>Giá trị = tổng lít theo các lệnh VC.<br>Suffix "L".<br>Info phụ: "Lượng dầu bơm cố định<br>theo lệnh vận chuyển."|—|
|---|---|---|---|---|---|---|---|
|8|Section: Phương thức nhận dầu|||||||
|9|Option A<br>— Cây<br>dầu nội<br>bộ|Radi<br>o<br>Card|—|—|Chọ<br>n<br>nếu<br>cây<br>gốc<br>nội<br>bộ|Badge Ưu tiên 1/2 + sub-section cây<br>nội bộ khi selected.<br>(Chi tiết xem<br>STT 14-15)<br>UC06.00.03||
|1<br>0|Option B<br>— Cây<br>dầu mua<br>ngoài|Radi<br>o<br>Card|—|—|Chọ<br>n<br>nếu<br>cây<br>gốc<br>mua|Badge Ưu tiên 1/2 + banner cảnh báo<br>chờ duyệt + sub-section cây mua<br>ngoài.<br>(Chi tiết xem<br>STT 16-17)<br>UC06.00.03||

![Trang 223 — ảnh xem trước để đối chiếu hình vẽ](images/page-223.png)

<!-- Trang 224 -->

||||||ngoà<br>i|||
|---|---|---|---|---|---|---|---|
|1<br>1|Option C<br>— Hóa<br>đơn lẻ|Radi<br>o<br>Card|—|—|—|Badge Ưu tiên 3 + banner điều kiện +<br>link Petrolimex.<br>(Chi tiết xem<br>STT 18)<br>UC06.00.03||
|1<br>2|Section: Thông tin khác|||||||
|1<br>3|Footer:|||||||
|1<br>4|Footer<br>Bar|Labe<br>l|—|—|—|"Số lượng: Y L|Nơi nhận<br>dầu: [Tên<br>cây]".|
|1<br>5|Button<br>Lưu nháp|Butt<br>on|—|—|—|Không validate bắt buộc.<br>Lưu phiếu trạng thái draft .<br>Không có UI feedback — navigate về<br>màn danh sách.|—|
|1<br>6|Button<br>Tạo mới|Butt<br>on|—|—|—|Primary "Tạo mới →".<br>Validate toàn bộ.<br>Nếu hợp lệ → xử lý theo bước 6 -<br>Nhánh Tạo mới (Lưu đồ hoạt động)|—|

![](images/ndlxd-export.pdf-0224-00.png)

<!-- Trang 225 -->

Lịch sử hoạt động, thông báo chi tiết
xem ở tài liệu tổng hợp
.
Nếu lỗi → scroll đến trường lỗi đầu
tiên.
Thông báo và
lịch sử hoạt động của phiếu cấp dầu

Ghi chú màn hình: Nếu không có lệnh VC nào tích lũy: hiển thị empty state

trong section "Dầu tích lũy" — icon + "Không có lệnh vận chuyển nào chờ cấp

dầu." Button "Tạo mới" bị disabled. Người dùng chỉ có thể Lưu nháp hoặc Huỷ.

##### 3.2 Màn hình Popcon

Giống Popcon chỉ khác:

mục 3.3 UC06.00.03

Thay mã dGas 1 → dGas 3

Thay phân loại là chi phí hàng bán

![](images/ndlxd-export.pdf-0225-00.png)

![](images/ndlxd-export.pdf-0225-02.png)

<!-- Trang 226 -->

### UC06.00.06 - Tạo mới phiếu dGas4 (Đổ đầy bình)

#### 1. Thông tin chung

|Mã UC|UC06.00.06|
|---|---|
|Tên UC|Tạo mới phiếu cấp dầu dGas4 — Đổ đầy bình|
|Tác nhân|Quản lý|
|Đường dẫn|UC06.00.01 Danh sách → Button "Tạo mới" → Chọn dGas4 → Tiếp tục|
|Điều kiện trước|Người dùng đã đăng nhập.<br>Có quyền tạo phiếu.|
|Điều kiện sau|Lưu nháp: draft .<br>Submit: pending + popcon + thông báo + lịch sử hoạt động.|

#### 2. Lưu đồ hoạt động

1. Người dùng chọn dGas4 → tap "Tiếp tục" (không có pre-check).

2. Màn tạo hiển thị Stepper.

3. Người dùng chọn Mục đích và Biển số xe (cả hai bắt buộc).

4. Số lượng: read-only "–" — không nhập trước, ghi nhận thực tế sau khi bơm.

5. Phương thức nhận dầu: Chọn Cây dầu nội bộ (dầu hoạch toán vào hàng tồn kho).

6. Người dùng điền Ghi chú → Lưu nháp hoặc Tạo mới.

7. Submit → pending → MSC-01 notify người có quyền PD → MSC-11 Popcon → lưu lịch sử

hoạt động mới.

8. Tap Back khi có dữ liệu → MSC-02 Unsaved Changes.

#### 3. Mô tả màn hình

##### 3.1 Màn hình Tạo phiếu dGas4

![Trang 226 — ảnh xem trước để đối chiếu hình vẽ](images/page-226.png)

<!-- Trang 227 -->

![](images/ndlxd-export.pdf-0227-00.png)

||Tên<br>thành<br>phần|Cont<br>rol|Loại|Bắt<br>buộ<br>c|Giá<br>trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Header|Labe<br>l|Text|—|—|"Tạo phiếu cấp dầu" + Badge<br>"dGas4" (tím).|—|

<!-- Trang 228 -->

|2|Stepper|Step<br>per|—|—|—|Hiển thị nodata: "Chọn mục<br>đích để xem tiến trình nghiệp<br>vụ."<br>Xem thêm ở<br>Loading chạy skeleton loading<br>Sau đó hiển thị:<br>Lấy đúng trường hợp này (Liên<br>module, luồng sửa chữa dùng<br>dầu) được định nghĩa trong<br>.<br>MSC-06<br>tài<br>liệu chung|—|
|---|---|---|---|---|---|---|---|
|3|Info<br>banner|Bann<br>er|—|—|—|"Dầu hoạch toán vào hàng tồn<br>kho. Bắt buộc nhận tại cây dầu<br>nội bộ."<br>Màu xanh dương nhạt.|—|
|4|Section: Thông tin yêu cầu|||||||
|5|Mục đích|Sele<br>ct|List|Có|—|Placeholder "Chọn mục đích".<br>Các giá trị:<br>Đổ đầy bình lần đầu<br>Bàn giao phương tiện<br>Chạy định mức<br>→ Hiển thị thanh tiến trình theo<br>mục đích được chọn|"Vui lòng chọn<br>mục đích."|

![](images/ndlxd-export.pdf-0228-01.png)

<!-- Trang 229 -->

|||||||Khi thay đổi mục đích: reload<br>lại thanh tiến trình.||
|---|---|---|---|---|---|---|---|
|6|Biển số<br>xe|Sele<br>ct|List|Có|—|Dropdown tìm kiếm biển số xe.<br>Hiển thị tất cả các phương tiện<br>(khai thác) của chi nhánh.|"Vui lòng chọn<br>biển số xe."|
|7|Section: Số lượng|||||||
|8|Số lượng|Labe<br>l|Num<br>ber|—|—|Read-only "–".<br>Không nhập được.<br>Info phụ: "Bơm đến khi đầy<br>bình rồi ghi nhận số lít bơm<br>vào. Hệ thống ghi số theo số<br>thực tế."|—|
|9|Section: Phương thức nhận dầu<br>Chỉ hiển thị Cây dầu nội bộ (không có radio).|||||||
|1<br>0|Cây dầu<br>nội bộ<br>(fixed)|Card|—|—|Cây<br>gốc|Tên cây + ⛽ lít tồn.<br>Read-only.<br>"Xem quy trình >".|—|
|1<br>1|Section: Thông tin khác|||||||

![](images/ndlxd-export.pdf-0229-00.png)

<!-- Trang 230 -->

Nhân viên yêu cầu + Ngày yêu cầu + Ghi chú.

|1<br>2|Footer:|||||||
|---|---|---|---|---|---|---|---|
|1<br>3|Footer<br>Bar|Labe<br>l|—|—|—|"Nơi nhận dầu: [Tên cây]".<br>(Không hiển thị số lít vì chưa<br>có.)|—|
|1<br>4|Button<br>Lưu nháp|Butto<br>n|—|—|—|Không validate bắt buộc.<br>Lưu phiếu trạng thái draft .<br>Không có UI feedback —<br>navigate về màn danh sách.|—|
|1<br>5|Button<br>Tạo mới|Butto<br>n|—|—|—|Primary "Tạo mới →".<br>Validate toàn bộ.<br>Nếu hợp lệ → xử lý theo bước 7<br>- Nhánh Tạo mới (Lưu đồ hoạt<br>động)<br>Lịch sử hoạt động, thông báo<br>chi tiết xem ở tài liệu tổng hợp<br>.<br>Nếu lỗi → scroll đến trường lỗi<br>đầu tiên.<br>Thông báo và lịch sử hoạt động<br>của phiếu cấp dầu|—|

##### 3.2 Màn hình Popcon

Giống Popcon chỉ khác:

mục 3.3 UC06.00.03

Thay mã dGas 1 → dGas 4

Thay phân loại là chi phí tồn kho

Thay số lít dầu là đổ đầy bình

![Trang 230 — ảnh xem trước để đối chiếu hình vẽ](images/page-230.png)

<!-- Trang 231 -->

### UC06.00.07 - Tạo mới phiếu dGas5 (Chốt dầu)

#### 1. Thông tin chung

|Mã UC|UC06.00.07|
|---|---|
|Tên UC|Tạo mới phiếu cấp dầu dGas5 — Chốt dầu|
|Tác nhân|Lái xe, Quản lý|
|Đường dẫn|UC06.00.01 Danh sách → Button "Tạo mới" → Chọn dGas5 → Tiếp tục|
|Điều kiện trước|Đã đăng nhập.<br>Đủ 3 điều kiện chốt:<br>(1) Tất cả lệnh VC đã chốt,<br>(2) Lái xe đã hoàn thành bơm dầu theo mã dGas 3 cho tất cả lệnh VC,<br>(3) Tổng dầu ≥ ngưỡng tối thiểu (đầu kéo ≥100L, xe tải thùng ≥25L) —<br>ngoại lệ: Loại 2 (Thu hồi) và Loại 3 (Chạy định mức) bỏ qua điều kiện<br>3.|
|Điều kiện sau|Lưu nháp: draft .<br>Submit: approved_waiting (dGas5 luôn cần phê duyệt), lưu lịch sử<br>hoạt động<br>Sau phê duyệt: kết quả thưởng/phạt ghi vào lương tháng sau.|

#### 2. Lưu đồ hoạt động

1. Người dùng chọn dGas5 → tap "Tiếp tục".

2. Hệ thống kiểm tra 3 điều kiện chốt → hiển thị Modal kiểm tra điều kiện:

Không đủ điều kiện: Modal thất bại (3.1) → Button "Đã hiểu" → đóng, không thể tạo.

Đủ điều kiện: Modal thành công (3.2) → Button "Tiếp tục" → Modal xác nhận tình trạng

bình (3.3).

3. Người dùng chọn tình trạng bình → tap "Tiếp tục":

"Đã đầy bình": Navigate màn tạo dGas5 phiên bản A — không cần bơm thêm (3.4).

"Chưa đầy bình": Navigate màn tạo dGas5 phiên bản B — cần bơm thêm để đầy bình

(3.5).

![Trang 231 — ảnh xem trước để đối chiếu hình vẽ](images/page-231.png)

<!-- Trang 232 -->

4. Người dùng xem summary chốt tháng, điền Ghi chú → Lưu nháp hoặc Tạo mới.

5. Submit:

Tạo mới bản ghi approved_waiting → không gửi notify → hiển thị MSC-11 Popcon

thành công.

Lưu lịch sử hoạt động mới.

6. Người dùng tap Back khi form đang có dữ liệu chưa lưu → Common 2.13 Unsaved Changes.

#### 3. Mô tả màn hình

##### 3.0 Modal Lý do chốt dầu

![](images/ndlxd-export.pdf-0232-07.png)

Xuất hiện ngay sau khi người dùng tap "Tiếp tục" từ Bottom Sheet chọn loại phiếu.

Xác định loại chốt trước khi kiểm tra điều kiện.

||Tên thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Mô tả|Validate|
|---|---|---|---|---|---|---|
|1|Tiêu đề|Label|Text|—|"Lý do chốt dầu". Center-align.|—|
|2|Option Chốt<br>cuối tháng|Radio<br>Card|—|Có|Icon 📅 + "Chốt cuối tháng" + "Ghi<br>nhận tổng dầu tháng [MM/YYYY]".<br>Chỉ active trong 5 ngày làm việc<br>đầu tháng n+1.|—|

<!-- Trang 233 -->

||||||Ngoài thời gian: hiển thị nhưng<br>disabled + badge xám "Chưa đến kỳ<br>chốt".||
|---|---|---|---|---|---|---|
|3|Option Thu<br>hồi phương<br>tiện|Radio<br>Card|—|Có|Icon 🚗 + "Thu hồi phương tiện" +<br>"Xe thu hồi lại từ lái xe".<br>Active bất kỳ lúc nào.|—|
|4|Option<br>Chuyển<br>nghiệp vụ|Radio<br>Card|—|Có|Icon 🔄 + "Chạy định mức" + "Xe<br>chuẩn bị chạy định mức".<br>Active bất kỳ lúc nào.|—|
|5|Button Huỷ|Butto<br>n|—|—|Secondary.<br>Đóng modal.|—|
|6|Button Tiếp<br>tục|Butto<br>n|—|—|Primary.<br>Disabled cho đến khi chọn.<br>Tap → kiểm tra điều kiện theo loại<br>đã chọn.|"Vui lòng<br>chọn lý do<br>chốt<br>dầu."|

##### 3.1 Modal Điều kiện chốt — Thất bại

![](images/ndlxd-export.pdf-0233-02.png)

Xử lý các điều kiện chốt dầu như sau:

<!-- Trang 234 -->

(1) Tất cả lệnh VC đã chốt → yêu cầu ERP trả API có list trạng thái hoàn thành.

(2) Lái xe đã hoàn thành bơm dầu theo mã dGas 3 cho tất cả lệnh VC → kiểm tra còn lệnh VC

nào chưa được cấp dầu dGas 3 không và các phiếu cấp dầu dGas 3 đã hoàn thành chưa.

(3) Tổng lượng dầu đủ ngưỡng chốt (đầu kéo ≥100L, xe tải thùng ≥25L, các loại phương tiện

khác không cần hiển thị điều kiện này)

Note cho test: Ở đây cần test các case sau:

Skip chốt dầu theo tháng này do không đủ điều kiện ngưỡng chốt → tháng sau chốt đủ cả 2

(list phiếu cần hiển đủ), khi đó chốt dầu là tháng hiện tại, không phải tháng trước đó (chưa

được chốt).

Do k đạt điều kiện tháng này nên skip chốt dầu, nên vẫn phải được tạo mới bình thường phiếu

cấp dầu loại khác (rule thường là validate k cho tạo mới)

Nếu tháng trước đủ điều kiện ngưỡng mà không chốt thì validate không cho tạo mới phiếu.

|Tên thành<br>phần|Cont<br>rol|Loại|Bắt<br>buộc|Giá<br>trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|Tiêu đề|Label|Text|—|—|"Điều kiện chốt dầu".<br>Center-align.|—|
|Dòng điều<br>kiện 1|Row|—|—|—|Icon + "Tất cả lệnh VC đã chốt" +<br>Badge xanh/đỏ nhạt "X chờ".<br>Thể hiện số lượng lệnh chưa được<br>chốt.<br>✅ = xanh, ❌ = đỏ.|—|
|Dòng điều<br>kiện 2|Row|—|—|—|Icon + "Lái xe đã hoàn thành bơm<br>dầu theo mã dGas 3 cho tất cả lệnh<br>VC " + Badge số.<br>Thể hiện số lượng lệnh không thoả<br>mãn.|—|
|Dòng điều<br>kiện 3|Row|—|—|—|Icon + "Tổng lượng dầu đủ ngưỡng<br>chốt" + Badge số.|—|

![Trang 234 — ảnh xem trước để đối chiếu hình vẽ](images/page-234.png)

<!-- Trang 235 -->

||||||Chỉ hiển thị với Loại 1 (Chốt cuối<br>tháng).<br>Loại 2/3: ẩn dòng này.<br>Nếu fail: badge đỏ "Còn thiếu Z L"||
|---|---|---|---|---|---|---|
|Banner kết<br>quả|Bann<br>er|—|—|—|Nền đỏ nhạt, border đỏ:<br>"❌ Không đủ điều kiện tạo phiếu<br>chốt tháng [M/YYYY]."|—|
|Button Đã<br>hiểu|Butto<br>n|—|—|—|Primary.<br>Đóng modal.<br>Người dùng không thể tiếp tục tạo<br>dGas5.|—|

##### 3.2 Modal Điều kiện chốt — Đủ điều kiện

![](images/ndlxd-export.pdf-0235-02.png)

|Tên thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|(Tương tự<br>3.1)|—|—|—|—|Tất cả 3 dòng điều kiện đều ✅.|—|

<!-- Trang 236 -->

|Banner kết<br>quả|Banne<br>r|—|—|—|Nền xanh nhạt: "✅ Đủ điều kiện<br>tạo phiếu chốt tháng [M/YYYY]."|—|
|---|---|---|---|---|---|---|
|Button Huỷ|Button|—|—|—|Secondary.<br>Đóng modal, không tạo phiếu.|—|
|Button Tiếp<br>tục|Button|—|—|—|Primary.<br>Mở Modal 3.3.|—|

##### 3.3 Modal Xác nhận tình trạng bình dầu

![](images/ndlxd-export.pdf-0236-02.png)

|Tên thành<br>phần|Contro<br>l|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|Tiêu đề|Label|Text|—|—|"Xác nhận tình trạng bình<br>dầu".|—|
|Info|Banner|—|—|—|Xanh dương nhạt: "Kiểm tra<br>bình dầu xe trước khi xác<br>nhận.|—|

<!-- Trang 237 -->

||||||Hệ thống sẽ tính thưởng/phạt<br>dựa trên lựa chọn này."||
|---|---|---|---|---|---|---|
|Option Đã<br>đầy bình|Radio<br>Card|Boolea<br>n|Có|—|Icon + "Đã đầy bình" + mô tả<br>"Không cần bơm thêm – chốt<br>ngay".<br>Khi chọn: border xanh, nền<br>xanh nhạt.|—|
|Option<br>Chưa đầy<br>bình|Radio<br>Card|Boolea<br>n|Có|—|Icon ⛽ xám + "Chưa đầy<br>bình" + mô tả "Cần xử lý thêm<br>sau khi chốt".<br>Khi chọn: border xanh, nền<br>xanh nhạt.|—|
|Button Huỷ|Button|—|—|—|Secondary.<br>Đóng modal.|—|
|Button Tiếp<br>tục|Button|—|—|Disable<br>d|Enabled sau khi chọn 1 option.<br>Tap với "Đã đầy bình" →<br>navigate màn 3.4.<br>Tap với "Chưa đầy bình" →<br>navigate màn 3.5.|"Vui<br>lòng<br>chọn<br>tình<br>trạng<br>bình<br>dầu."|

##### 3.4 Màn hình Tạo phiếu dGas5 (Đã đầy bình)

![Trang 237 — ảnh xem trước để đối chiếu hình vẽ](images/page-237.png)

<!-- Trang 238 -->

![](images/ndlxd-export.pdf-0238-00.png)

Không cần bơm thêm — không có section Số lượng và Phương thức nhận

dầu. Card tổng lượng dầu hiển thị nền xanh lá.

||Tên thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|Header|Label|Text|—|—|"Chốt dầu tháng" + Badge<br>"dGas5" (cam).|—|
|2|Stepper|Bann<br>er|—|—|—|Xanh dương nhạt.<br>Xem thêm ở<br>Sau đó hiển thị:<br>MSC-06|—|

<!-- Trang 239 -->

![](images/ndlxd-export.pdf-0239-00.png)

|||||||Lấy đúng trường hợp này (Liên<br>module, luồng chạy định mức +<br>thu hồi phương tiện) được định<br>nghĩa trong<br>.<br>tài liệu chung||
|---|---|---|---|---|---|---|---|
|3|Section: Phân loại chốt dầu|||||||
|4|Mục đích<br>chốt dầu|Label|—|—|—|Hiển thị mục đích chốt dầu chọn<br>từ modal 3.0<br>Chốt dầu tháng<br>Thu hồi phương tiện<br>Chạy định mức<br>Read-only||
|5|Section: Tính toán dầu chốt tháng|||||||
|6|Card xe|Card|—|—|—|Icon xe + Biển số + Loại PT +<br>Mã PT<br>(VD: Đầu kéo container • Xe<br>ChengLong).|—|

![](images/ndlxd-export.pdf-0239-01.png)

![](images/ndlxd-export.pdf-0239-02.png)

![](images/ndlxd-export.pdf-0239-04.png)

<!-- Trang 240 -->

|7|Header<br>danh sách<br>cấp dầu|Label|—|—|—|"DANH SÁCH CẤP DẦU TRONG<br>THÁNG" — chữ hoa xám nhỏ.|—|
|---|---|---|---|---|---|---|---|
|8|Danh sách<br>phiếu cấp<br>dầu trong<br>tháng|List<br>Card|—|—|—|Lấy danh sách các phiếu cấp<br>dầu chưa được chốt dầu trong<br>tháng trước.<br>Nếu tháng trước đó chưa chốt<br>dầu (do chưa đủ ngưỡng dầu) thì<br>tính thêm các phiếu của tháng<br>trước nữa)<br>Mỗi card: Mã phiếu + Icon loại<br>dGas + Ngày + Số lít (giá trị thực<br>nhận).<br>Read-only, chỉ xem.|—|
|9|Card tổng<br>lượng dầu|Card|—|—|—|Nền xanh lá đậm, text trắng.<br>"Tổng lượng dầu · X phiếu cấp<br>dầu: Y lít".<br>Font lớn.|—|
|1<br>0|Section: Thông tin khác|||||||

![](images/ndlxd-export.pdf-0240-03.png)

<!-- Trang 241 -->

**Nhân viên yêu cầu + Ngày yêu cầu + Ghi chú.**

|1<br>1|Button Lưu<br>nháp|Butto<br>n|—|—|—|Secondary.<br>Lưu phiếu trạng thái draft .<br>Không có UI feedback —<br>navigate về màn danh sách.|—|
|---|---|---|---|---|---|---|---|
|1<br>2|Button Tạo<br>mới|Butto<br>n|—|—|—|Primary "Tạo mới →".<br>Validate toàn bộ.<br>Nếu hợp lệ → xử lý theo bước 5<br>(Lưu đồ hoạt động)<br>Lịch sử hoạt động, thông báo chi<br>tiết xem ở tài liệu tổng hợp<br>.<br>Nếu lỗi → scroll đến trường lỗi<br>đầu tiên.<br>Thông báo và lịch sử hoạt động<br>của phiếu cấp dầu|—|

##### 3.5 Màn hình Tạo dGas5 — Chưa đầy bình

![Trang 241 — ảnh xem trước để đối chiếu hình vẽ](images/page-241.png)

<!-- Trang 242 -->

![Trang 242 — ảnh mockup màn hình (toàn trang)](images/ndlxd-export.pdf-0242-00.png)


<!-- Trang 243 -->

Cần bơm thêm để đầy bình — có thêm section Số lượng (đổ thêm) và Phương

thức nhận dầu (bắt buộc cây nội bộ). Card tổng lượng dầu hiển thị nền đỏ

(cảnh báo thiếu).

||Tên<br>thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|---|
|1|(Giống<br>3.4 STT<br>1–7)|—|—|—|—|—|—|
|2|Danh<br>sách<br>phiếu<br>trong<br>tháng|List<br>Card|—|—|—|Tương tự 3.4 STT 8.|—|
|3|Card<br>tổng<br>lượng<br>dầu|Card|—|—|—|Nền đỏ đậm, text trắng.<br>Icon ⛽ + "Tổng lượng dầu · X<br>phiếu cấp dầu: Y lít". Màu đỏ báo<br>hiệu chưa đủ.|—|
|4|Section: Số lượng|||||||

![](images/ndlxd-export.pdf-0243-02.png)

<!-- Trang 244 -->

|5|Số lít cấp|Label|Numb<br>er|—|—|Read-only "–".<br>Không nhập được.<br>Info phụ xám: "Bơm đến khi đầy<br>bình rồi ghi nhận số lít bơm vào.<br>Hệ thống ghi số theo số thực tế."|—|
|---|---|---|---|---|---|---|---|
|6|Section: Phương thức nhận dầu<br>Icon bơm + label "Phương thức nhận dầu".<br>Bắt buộc cây nội bộ (không cho chọn mua ngoài hay HĐ lẻ để chốt).<br>Dấu * màu đỏ bên cạnh label.|||||||
|7|Sub-<br>section<br>chọn cây<br>nội bộ|Radio<br>List|—|Có|Cây<br>dầu<br>gốc|Tương tự<br>STT 15: Tên<br>cây + Badge "Cây dầu gốc" ⭐ +<br>📍 km + ⏱ phút + ⛽ hạn mức +<br>"Xem đường đi ›".<br>Cây hạn mức không đủ: disabled<br>+ "⚠ Tồn kho không đủ."<br>Hyperlink Xem quy trình mở boom<br>sheet xem quy trình (xem thêm ở<br>).<br>UC06.00.03<br>3.2 UC06.00.03|"Vui<br>lòng<br>chọn cây<br>dầu nội<br>bộ."|
|8|(Section Thông tin khác, Buttons — giống 3.4 STT 7–13)|||||||
|9|Footer<br>Bar|Label|—|—|—|"Số lượng: 3,200 L \| Nơi nhận dầu:<br>[Tên cây]".<br>"--" khi chưa chọn cây.|—|

![](images/ndlxd-export.pdf-0244-00.png)

<!-- Trang 245 -->

Cập nhật realtime.

##### 3.6 Màn hình Popcon

![](images/ndlxd-export.pdf-0245-02.png)

Giống Popcon chỉ khác:

mục 3.3 UC06.00.03

Thay mã dGas 1 → dGas 5

Thay trường phân loại = kết quả chốt (giá trị = thừa/thiếu · X lít)

Bỏ các trường số lít dầu, phương thức nhận dầu

<!-- Trang 246 -->

### UC06.00.08 - Tạo mới phiếu cấp bù dầu

#### 1. Thông tin chung

|Mã UC|UC06.00.08|
|---|---|
|Tên UC|Tạo mới phiếu Cấp bù dầu|
|Tác nhân|Lái xe, quản lý,…|
|Đường dẫn|UC06.00.01 Danh sách → Button "Tạo mới" → Chọn Cấp bù → Tiếp<br>tục|
|Điều kiện trước|Đã đăng nhập.<br>Có ≥1 phiếu cấp dầu cây nội bộ ở trạng thái done với số lít thực nhận<br>< số lít xin cấp (còn dư chưa bơm > 0).|
|Điều kiện sau|Lưu nháp: draft .<br>Submit: approved_waiting (TH1/TH3), waiting (TH4), hoặc<br>pending (TH2/TH5) — theo Approval Matrix, gửi in-app notification<br>(MSC-01) đến người có quyền phê duyệt, lưu lịch sử hoạt động.|

#### 2. Lưu đồ hoạt động

1. Người dùng chọn Cấp bù → tap "Tiếp tục" từ Bottom Sheet chọn loại.

Nếu không có phiếu nào đủ điều kiện: Bottom Sheet thông báo "Không có phiếu nào cần

cấp bù." → không navigate.

2. Hệ thống mở Bottom Sheet Chọn phiếu (3.1) — danh sách tất cả phiếu cây nội bộ done còn

dư dầu.

3. Người dùng chọn một hoặc nhiều phiếu (multi-select). Counter cập nhật realtime "Đã chọn

X/Y phiếu".

4. Tap "Tiếp tục" → navigate màn Tạo phiếu Cấp bù (3.2).

5. Hệ thống auto-fill:

Section Phiếu gốc: danh sách phiếu đã chọn + card Tổng dầu còn dư.

Số lít nhận = tổng dầu còn dư từ tất cả phiếu đã chọn — read-only.

6. Người dùng chọn Phương thức nhận dầu (chỉ Cây nội bộ hoặc HĐ lẻ).

7. Người dùng điền Ghi chú → Lưu nháp hoặc Tạo mới.

![Trang 246 — ảnh xem trước để đối chiếu hình vẽ](images/page-246.png)

<!-- Trang 247 -->

8. Submit → Validate hợp lệ:

Tạo mới bản ghi.

Hệ thống xác định luồng phê duyệt theo Bảng Approval Matrix (Mục 5), sau đó:

Không cần phê duyệt (TH1/TH3 — cây nội bộ): Tạo phiếu → approved_waiting →

không gửi notify → hiển thị MSC-11 Popcon thành công.

Không cần phê duyệt (TH4 — cây mua ngoài): Tạo phiếu → waiting → MSC-01

notify NV cây dầu qua Partner Portal → hiển thị MSC-11 Popcon thành công.

Cần phê duyệt (TH2/TH5): Tạo phiếu → pending → MSC-01 notify người có quyền

phê duyệt → hiển thị MSC-11 Popcon thành công.

Lưu lịch sử hoạt động mới.

9. Tap Back khi có dữ liệu → MSC-02 Unsaved Changes.

#### 3. Mô tả màn hình

##### 3.1 Bottom Sheet — Chọn phiếu

![](images/ndlxd-export.pdf-0247-10.png)

Slide-up từ dưới.

Swipe down → đóng (chưa có dữ liệu nên không trigger Unsaved Changes).

|Tên thành<br>phần|Contr<br>ol|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|

<!-- Trang 248 -->

|Handle bar<br>+ Tiêu đề|Label|Text|—|—|"Chọn phiếu".|—|
|---|---|---|---|---|---|---|
|Counter|Label|Text|—|—|Góc phải: "Đã chọn X/Y phiếu".<br>Cập nhật realtime khi chọn/bỏ<br>chọn.|—|
|Danh sách<br>phiếu|List<br>Card|—|—|—|Multi-select.<br>Mỗi card: Icon loại dGas (vuông<br>bo góc, màu theo loại) + Mã<br>phiếu (bold) + Badge loại dGas<br>(nhỏ, xám) + Ngày (hàng dưới<br>trái) + Số lít còn dư (hàng dưới<br>phải).<br>Selected: border xanh + nền<br>xanh rất nhạt.<br>Sắp xếp: mới nhất lên trên.<br>Chỉ hiển thị phiếu cây nội bộ<br>done có dư > 0.|—|
|Empty state|MSC-<br>09|—|—|—|Nếu không có phiếu nào đủ điều<br>kiện: illustration + "Không có<br>phiếu nào có thể cấp bù."|—|
|Button Tiếp<br>tục|Button|—|Có|Disabl<br>ed|Full-width, primary xanh lá.<br>Disabled khi chưa chọn phiếu<br>nào.<br>Active sau khi chọn ≥1 phiếu.|"Vui<br>lòng<br>chọn ít<br>nhất 1<br>phiếu."|

##### 3.2 Màn hình Tạo phiếu Cấp bù

![Trang 248 — ảnh xem trước để đối chiếu hình vẽ](images/page-248.png)

<!-- Trang 249 -->

![](images/ndlxd-export.pdf-0249-00.png)

|Tên<br>thành<br>phần|Con<br>trol|Loại|Bắt<br>buộ<br>c|Giá<br>trị<br>mặc<br>địn<br>h|Mô tả|Validate|
|---|---|---|---|---|---|---|

![](images/ndlxd-export.pdf-0249-02.png)

<!-- Trang 250 -->

|1|Navigatio<br>n bar|Lab<br>el|Text|—|—|"Tạo phiếu cấp dầu" + Badge<br>"Cấp bù" (cam).<br>Button back (←).|—|
|---|---|---|---|---|---|---|---|
|2|Section: Phiếu gốc chưa nhận hết<br>Icon danh sách + label "Phiếu gốc chưa nhận hết" + Badge xám nhỏ "[X] phiếu"<br>(right-align, số phiếu đã chọn).|||||||
|3|Danh<br>sách<br>phiếu gốc|List<br>Car<br>d|—|—|—|Read-only.<br>Mỗi card: Icon loại dGas + Mã<br>phiếu (bold) + Badge loại<br>dGas + Ngày (hàng dưới trái)<br>+ Số lít còn dư (hàng dưới<br>phải).<br>Không tương tác.|—|
|4|Card<br>Tổng dầu<br>còn dư|Car<br>d|—|—|—|Nền cam đậm, text trắng.<br>Icon ⛽ + "Tổng dầu còn dư"<br>+ "[X] Phiếu cấp dầu: Y lít".<br>Font lớn.|—|
|5|Section: Số lượng|||||||

![](images/ndlxd-export.pdf-0250-00.png)

<!-- Trang 251 -->

|6|Số lít<br>nhận|Lab<br>el|Num<br>ber|—|Tổn<br>g dư<br>từ<br>phiế<br>u<br>gốc|Read-only (disabled, nền<br>xám).<br>Giá trị = tổng dầu còn dư từ<br>tất cả phiếu đã chọn.<br>Suffix "L".<br>Info phụ xám: "Lượng dầu<br>bơm cố định theo số dầu còn<br>lại chưa bơm từ phiếu cấp dầu<br>cũ."|—|
|---|---|---|---|---|---|---|---|
|7|Section: Phương thức nhận dầu<br>Icon bơm + label. Chỉ hiển thị 2 option (không có cây mua ngoài).|||||||
|8|Option A<br>— Cây<br>dầu nội<br>bộ|Radi<br>o<br>Car<br>d|—|—|Chọ<br>n<br>nếu<br>cây<br>gốc<br>nội<br>bộ|Badge Ưu tiên 1/2 + sub-<br>section cây nội bộ khi<br>selected.<br>(Chi tiết xem<br>STT<br>14-15)<br>UC06.00.03||
|9|Option B<br>— Cây|Radi<br>o|—|—|Chọ<br>n|Badge Ưu tiên 1/2 + banner<br>cảnh báo chờ duyệt + sub-||

![Trang 251 — ảnh xem trước để đối chiếu hình vẽ](images/page-251.png)

<!-- Trang 252 -->

||dầu mua<br>ngoài|Car<br>d|||nếu<br>cây<br>gốc<br>mua<br>ngo<br>ài|section cây mua ngoài.<br>(Chi tiết xem<br>STT<br>16-17)<br>UC06.00.03||
|---|---|---|---|---|---|---|---|
|1<br>0|Option C<br>— Hóa<br>đơn lẻ|Radi<br>o<br>Car<br>d|—|—|—|Badge Ưu tiên 3 + banner điều<br>kiện + link Petrolimex.<br>(Chi tiết xem<br>STT<br>18)<br>UC06.00.03||
|1<br>1|Section: Thông tin khác<br>Tương tự các màn khác.|||||||
|1<br>2|Footer|||||||
|1<br>3|Footer<br>Bar|Lab<br>el|—|—|—|"Số lượng: X L \| Nơi nhận dầu:<br>[Tên cây]".<br>"--" khi chưa chọn cây. Cập<br>nhật realtime.|—|
|1<br>4|Button<br>Lưu nháp|Butt<br>on|—|—|—|Trái ~40%,<br>secondary/outlined.<br>Không validate.<br>Lưu draft .<br>Navigate về danh sách.|—|
|1<br>5|Button<br>Tạo mới|Butt<br>on|—|—|—|Phải ~60%, primary xanh lá.<br>"Tạo mới →".<br>Loading + disabled khi đang<br>xử lý.<br>Nếu hợp lệ → xử lý theo bước<br>8 (Lưu đồ hoạt động)|—|

![](images/ndlxd-export.pdf-0252-01.png)

<!-- Trang 253 -->

Lịch sử hoạt động, thông báo
chi tiết xem ở tài liệu tổng hợp
.
Nếu lỗi → scroll đến trường lỗi
đầu tiên.
Thông báo và lịch sử hoạt
động của phiếu cấp dầu

![](images/ndlxd-export.pdf-0253-00.png)

![](images/ndlxd-export.pdf-0253-02.png)

<!-- Trang 254 -->

### UC06.00.09 - Phê duyệt/Từ chối phiếu cấp dầu (tất cả vòng)

#### 1. Thông tin chung

|Mã UC|UC06.00.09|
|---|---|
|Tên UC|Phê duyệt / Từ chối phiếu cấp dầu (vòng 1, 2, 3)|
|Tác nhân|CBQL / Trưởng phòng điều vận — Người có quyền phê duyệt|
|Đường dẫn|UC06.00.02 Màn chi tiết phiếu → Button "Phê duyệt" hoặc "Từ chối"<br>UC06.00.01 Danh sách phiếu → Long press 1 bản ghi → "Phê duyệt" hoặc<br>"Từ chối"|
|Điều kiện trước|Phiếu đang ở trạng thái<br>pending / purchase_fuel_pending / purchase_invoice_pending<br>(bất kỳ vòng).<br>Người dùng có quyền phê duyệt tương ứng vòng đó.|
|Điều kiện sau|Phê duyệt: Phiếu chuyển trạng thái theo bảng Approval Matrix, gửi notify<br>cho người liên quan, lưu lịch sử hoạt động mới.<br>Từ chối: Phiếu → rejected , notify người tạo kèm lý do.|

#### 2. Lưu đồ hoạt động

Nhánh Phê duyệt:

1. Người có quyền duyệt tap Button Phê duyệt trên màn chi tiết phiếu hoặc màn danh sách.

2. Hệ thống hiển thị Confirm Dialog (MSC-02): "Xác nhận phê duyệt?"

3. Người dùng xác nhận → Hệ thống cập nhật trạng thái theo phương thức nhận dầu:

Vòng 1: Tạo mới ( pending )

Cây dầu nội bộ → approved_waiting (chờ lái xe bấm Bắt đầu bơm).

Cây dầu mua ngoài → waiting (PO được phát hành đến cây đối tác, hiệu lực 24h).

Hóa đơn lẻ → purchase_pending (lái xe đi mua tại Petrolimex, hiệu lực 24h).

Vòng 2: Phê duyệt ghi nhận bơm dầu - Mua dầu hoá đơn lẻ ( purchase_fuel_pending )

→ purchase_invoicing

![Trang 254 — ảnh xem trước để đối chiếu hình vẽ](images/page-254.png)

<!-- Trang 255 -->

Vòng 3: Phê duyệt ghi nhận hoá đơn - Mua dầu hoá đơn lẻ

( purchase_invoice_pending ) → done

4. Notification đến người tạo phiếu (nếu có) + lưu lịch sử hoạt động mới + refresh màn chi

tiết/danh sách

Nhánh Từ chối:

1. Người có quyền duyệt tap Button Từ chối.

2. Hệ thống hiển thị Confirm Dialog (SC-02) có thêm Input lý do (bắt buộc nhập).

3. Người dùng nhập lý do → Xác nhận → Trạng thái phiếu → rejected .

4. Notification đến người tạo kèm lý do từ chối + lưu lịch sử hoạt động.

#### 3. Mô tả màn hình

Không có màn hình riêng. Giao diện xử lý qua Confirm Dialog (MSC-02) trên

màn UC06.00.02 hoặc màn UC06.00.01.

<!-- Trang 256 -->

### UC06.00.10 - Nhận mã Igas & bơm dầu - Cây nội bộ

#### 1. Thông tin chung

|Mã UC|UC06.00.10|
|---|---|
|Tên UC|Nhận mã Igas & bơm dầu — Cây dầu nội bộ|
|Tác nhân|Lái xe / Nhân viên — người tạo phiếu|
|Đường dẫn|UC06.00.02 Màn chi tiết phiếu (trạng thái approved_waiting ) →<br>Button "Cấp mã Igas"|
|Điều kiện trước|Phiếu đang ở trạng thái approved_waiting .<br>Người dùng là người tạo phiếu.<br>Có kết nối mạng.|
|Điều kiện sau|Phiếu → igas_active .<br>Mã Igas 6 ký tự được sinh, TTL 5 phút bắt đầu đếm.<br>Sau khi bơm xong: Igas callback → phiếu → done .<br>Nếu hết hạn: phiếu → igas_expired , phát sinh tiền phạt.|

#### 2. Lưu đồ hoạt động

1. Người dùng ở màn chi tiết phiếu trạng thái approved_waiting → tap "Cấp mã Igas".

2. Button loading + disabled. Hệ thống gọi Igas API sinh mã 6 ký tự (retry tối đa 3 lần):

Thành công: Phiếu → igas_active → hiển thị Card Mã Igas (3.2) trên màn chi tiết.

Lỗi sau 3 retry: Banner lỗi đỏ: "Không thể kết nối Igas. Vui lòng thử lại."

3. Người dùng dùng mã Igas tại trụ bơm cây nội bộ.

4. Igas callback bơm xong → Phiếu → done :

Card Mã Igas ẩn đi.

Hero card cập nhật sang dạng "Đã hoàn thành" (STT 3.5).

Nếu từng có mã hết hạn: Card Tiền phạt vẫn giữ nguyên.

5. Nhánh hết hạn: TTL 5 phút hết → Phiếu → igas_expired :

Card Mã Igas (và card Tiền phạt) chuyển sang Card Hết hiệu lực (3.3).

Hệ thống tính tiền phạt và cộng vào tổng.

![Trang 256 — ảnh xem trước để đối chiếu hình vẽ](images/page-256.png)

<!-- Trang 257 -->

6. Nhánh cấp lại: Người dùng tích checkbox xác nhận → tap "Cấp lại mã Igas":

Hệ thống sinh mã mới, TTL reset 5 phút → Phiếu → igas_active .

Card Mã Igas mới xuất hiện.

Card Tiền phạt giữ nguyên bên dưới (persistent).

Lặp lại từ bước 3.

#### 3. Mô tả màn hình

##### 3.1 Màn chi tiết — Trạng thái approved_waiting

Màn chi tiết tab Chung (mặc định). Không có tab Bơm dầu / Hóa đơn (cây nội bộ không dùng

tab).

||Tên thành phần|Control|Mô tả|
|---|---|---|---|
|1|Hero card|Card|Nền + Icon + Tên mã dGas + tên loại cấp dầu → tuỳ<br>thuộc theo mã dGas<br>Hiển thị: "SỐ DẦU XIN CẤP: X L". Chưa có thông tin<br>bơm.|
|2|Section Phương thức<br>nhận dầu|Section|Cây dầu nội bộ + tên cây + khoảng cách + lít tồn +<br>button "Xem đường đi".<br>Read-only.|
|3|Section Thông tin<br>khác|Section|Người yêu cầu + Ngày yêu cầu + Ghi chú.<br>Read-only.|
|4|Button Cấp mã Igas|Button|Full-width, primary xanh lá.<br>Loading spinner khi đang gọi API.|

##### 3.2 Card Mã Igas hiện tại ( igas_active )

![](images/ndlxd-export.pdf-0257-10.png)

<!-- Trang 258 -->

Card xuất hiện inline trên màn chi tiết, phía trên section Phương thức nhận dầu. Viền xanh lá,

nền xanh rất nhạt.

||Tên thành phần|Control|Mô tả|
|---|---|---|---|
|1|Header|Label|"MÃ IGAS HIỆN TẠI" — chữ hoa, xanh lá, font nhỏ.|
|2|Hướng dẫn|Label|"Nhập mã này vào bảng điều khiển trụ bơm."<br>Xám nhỏ.|
|3|Mã Igas|Label|Font mono 36px, bold, xanh lá đậm.<br>Format: IGS-XXXXX.<br>Tap → copy.|
|4|Countdown|Label|Format MM:SS.<br>Màu xám.<br>Về 0 → chuyển sang Card Hết hiệu lực (3.3) (yêu cầu có<br>transition từ card 3.2 → 3.3, có thể dùng skeleton loading)|
|5|Progress bar|—|Giảm dần theo TTL.<br>Màu đổi theo ngưỡng như countdown.|
|6|Info phụ|Label|"X L • [Tên cây] • Bơm một lần duy nhất." Xám nhỏ, căn giữa.<br>Lấy giá trị số dầu xin cấp và tên cây dầu nội bộ chọn đổ dầu.|

Ghi chú màn hình: Màn Mã Igas giữ nguyên khi user navigate away (về home,

lock màn hình...) — khi quay lại sẽ tiếp tục đếm ngược từ thời gian còn lại.

Countdown chạy bằng server-side TTL, không dùng local timer đơn thuần để

tránh sai lệch khi thiết bị sleep.

##### 3.3 Card Mã Igas hết hiệu lực ( igas_expired )

![Trang 258 — ảnh xem trước để đối chiếu hình vẽ](images/page-258.png)

<!-- Trang 259 -->

![](images/ndlxd-export.pdf-0259-00.png)

**Thay thế Card 3.2 khi TTL hết.**

**Viền đỏ, nền đỏ rất nhạt.**

||Tên thành phần|Control|Mô tả|
|---|---|---|---|
|1|Header|Label|"MÃ IGAS HẾT HIỆU LỰC!" — chữ hoa, đỏ, font nhỏ.|
|2|Label phạt|Label|"TIỀN PHẠT PHÁT SINH" — xám nhỏ, căn giữa.|
|3|Tổng tiền phạt|Label|Tổng cộng tất cả mã đã hết hạn.<br>Font 28px, bold, đỏ.<br>VD: 1,000,000đ.|
|4|Ghi chú|Label|"Trừ vào tháng lương tiếp theo."<br>Xám nhỏ.|
|5|Danh sách mã<br>hết hạn|List|Mỗi row: Mã IGS-XXXXX (trái) + "Cấp HH:mm • Hết<br>HH:mm" (xám nhỏ) + Badge đỏ "Hết hạn: −Xđ" (phải).|
|6|Checkbox xác<br>nhận|Checkbox|Bắt buộc tích trước khi cấp lại.<br>Label: "Tôi xác nhận chưa đổ dầu đúng thời hạn và đồng ý<br>bị trừ 500,000 đ vào lương tháng tiếp theo."|

<!-- Trang 260 -->

|7|Button Cấp lại<br>mã Igas|Button|Full-width, primary xanh lá.<br>Disabled cho đến khi tích checkbox.<br>Active → loading khi gọi API.<br>Xử lý theo lưu đồ hoạt động (Bước 6)|
|---|---|---|---|

##### 3.4 Card Tiền phạt (persistent)

![](images/ndlxd-export.pdf-0260-00.png)

Sau khi cấp lại mã ( igas_active lần 2 trở đi): Card Hết hiệu lực đổi thành Card Tiền phạt —

không có header "HẾT HIỆU LỰC", không có checkbox + button.

Chỉ còn: tổng tiền phạt + danh sách mã đã hết hạn.

Viền đỏ, nền đỏ rất nhạt.

Card này tồn tại vĩnh viễn kể cả sau khi bơm xong ( done ).

##### 3.5 Hero card sau khi bơm xong ( done — có phạt hoặc không)

![](images/ndlxd-export.pdf-0260-02.png)

||Thành phần|Mô tả|
|---|---|---|
|1|Header|"THỰC NHẬN" — chữ hoa, trắng nhỏ.|
|2|Số lít thực nhận|Font lớn, trắng bold.<br>VD: 135,000 L.|

![](images/ndlxd-export.pdf-0260-08.png)

<!-- Trang 261 -->

|3|Sub-label|"trên tổng [X] L xin cấp" — trắng nhỏ.|
|---|---|---|
|4|Progress bar|% thực nhận / xin cấp.<br>Màu trắng / xanh nhạt.<br>Label % bên phải.|
|5|BẮT ĐẦU|HH:mm bắt đầu của phiên bơm.<br>Yêu cầu API Igas trả về giá trị này.|
|6|KẾT THÚC|HH:mm kết thúc của phiên bơm.<br>Yêu cầu API Igas trả về giá trị này.|
|7|THỜI LƯỢNG|X phút. Badge trắng nhạt.|

![Trang 261 — ảnh xem trước để đối chiếu hình vẽ](images/page-261.png)

<!-- Trang 262 -->

### UC06.00.11 - Ghi nhận bơm dầu - Cây mua ngoài & Mua hoá đơn lẻ

#### 1. Thông tin chung

|Mã UC|UC06.00.11|
|---|---|
|Tên UC|Ghi nhận bơm dầu — Cây dầu mua ngoài|
|Tác nhân|(A) Nhân viên cây dầu mua ngoài — Delta Partner Portal<br>(B) Lái xe / NV — Delta ERP (HĐ lẻ)|
|Đường dẫn|(A) Partner Portal → Chi tiết đơn trạng thái waiting → Button "Ghi<br>nhận bơm dầu"<br>(A) Partner Portal → Chi tiết đơn trạng thái fuel_done → … →<br>"Ghi nhận bơm dầu"<br>(B) ERP → UC06.00.02 Chi tiết phiếu trạng thái<br>purchase_pending → Button "Ghi nhận bơm dầu"<br>(B) ERP → UC06.00.01 → Long press bản ghi trạng thái<br>purchase_pending → Button "Ghi nhận bơm dầu"|
|Điều kiện trước|(A) Đơn trạng thái waiting .<br>(A) Partner Portal → Chi tiết đơn trạng thái fuel_done → … →<br>"Ghi nhận bơm dầu"<br>(B) Phiếu trạng thái purchase_pending .<br>Người dùng có quyền tương ứng.|
|Điều kiện sau|(A) Đơn → fuel_done .<br>(B) Phiếu → purchase_fuel_pending .<br>Hero card + Tab Bơm dầu cập nhật thông tin bơm.<br>MSC-11 Popcon thành công.<br>Lưu lịch sử hoạt động mới|

#### 2. Lưu đồ hoạt động

![Trang 262 — ảnh xem trước để đối chiếu hình vẽ](images/page-262.png)

<!-- Trang 263 -->

1. Người dùng tap "Ghi nhận bơm dầu" (từ tab Bơm dầu — button trên màn chi tiết đơn Portal/

action trong icon …/sau khi Long press thẻ bản ghi ở màn danh sách).

2. Hệ thống mở Bottom Sheet Ghi nhận bơm dầu (3.1).

3. Người dùng nhập: số lượng thực bơm + thời gian bắt đầu + kết thúc + chụp ảnh máy bơm.

4. Hệ thống tự tính thành tiền = số lít × đơn giá hiện tại (lấy realtime từ API).

5. Tap "Ghi nhận bơm dầu" → Validate → MSC-02 Confirm.

6. Xác nhận → Hệ thống lưu:

(A) Đơn Portal → fuel_done . ERP sync.

(B) Phiếu ERP → purchase_fuel_pending . Notify người có quyền phê duyệt

7. Hệ thống lưu lịch sử hoạt động mới.

8. Hiển thị MSC-11 Popcon "Đã ghi nhận bơm dầu!" (3.2).

9. Người dùng tap "Xem thông tin chi tiết" → màn chi tiết, tab Bơm dầu cập nhật (3.3).

#### 3. Mô tả màn hình

##### 3.1 Bottom Sheet — Ghi nhận bơm dầu

![](images/ndlxd-export.pdf-0263-13.png)

Slide-up, duration 300ms. Swipe down khi đã có dữ liệu → MSC-02 Unsaved Changes.

<!-- Trang 264 -->

|Tên thành<br>phần|Control|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|
|Handle bar<br>+ Tiêu đề|Label|Text|—|—|"Ghi nhận bơm dầu".|—|
|Số lượng<br>thực bơm|Input|Number|Có|—|Placeholder "0". Suffix "L".<br>Hint xám: "Số lượng thực<br>bơm không vượt quá [X] L."<br>(X = số lít xin cấp).<br>Validate on blur + submit.|"Vui<br>lòng<br>nhập số<br>lượng<br>thực<br>bơm." ·<br>"Số<br>lượng<br>phải lớn<br>hơn 0." ·<br>"Số<br>lượng<br>không<br>được<br>vượt quá<br>[X] L."|
|Bắt đầu|DateTi<br>mePick<br>er|DateTi<br>me|Có|—|2 cột ngang hàng:<br>Bắt đầu (trái) + Kết thúc<br>(phải).<br>Format hh/mm .<br>Tap → DateTimePicker với<br>chọn giờ phút.|"Vui<br>lòng<br>chọn<br>thời<br>gian bắt<br>đầu."|
|Kết thúc|DateTi<br>mePick<br>er|DateTi<br>me|Có|—|Cùng hàng với Bắt đầu.<br>Phải ≥ Bắt đầu.|"Vui<br>lòng<br>chọn<br>thời<br>gian kết<br>thúc." ·<br>"Thời|

![Trang 264 — ảnh xem trước để đối chiếu hình vẽ](images/page-264.png)

<!-- Trang 265 -->

|||||||gian kết<br>thúc<br>phải sau<br>thời<br>gian bắt<br>đầu."|
|---|---|---|---|---|---|---|
|Đơn giá|Label|Number|—|Auto từ<br>API|Read-only.<br>Tự động lấy đơn giá dầu<br>hiện tại từ hệ thống.<br>Label nhỏ "ĐƠN GIÁ" bên<br>trái.|—|
|Thành tiền|Label|Number|—|Tính tự<br>động|Read-only.<br>= Số lượng × Đơn giá.<br>Cập nhật realtime khi số<br>lượng thay đổi.<br>Label "THÀNH TIỀN" màu<br>xanh lá.|—|
|Hình ảnh<br>máy bơm|Camera|—|Không|—|Chỉ cho phép chụp trực<br>tiếp (không chọn từ thư<br>viện).<br>Button "Chụp ảnh".<br>Tối đa 3 ảnh.<br>Thumbnail 80×80px sau khi<br>chụp.<br>Tap thumbnail → xem full.<br>Tap X → xoá.|—|
|Button Ghi<br>nhận bơm<br>dầu|Button|—|—|—|Full-width, primary xanh lá.<br>Loading + disabled khi đang<br>xử lý.|—|

##### 3.2 MSC-11 Popcon — Đã lưu ghi nhận bơm

![Trang 265 — ảnh xem trước để đối chiếu hình vẽ](images/page-265.png)

<!-- Trang 266 -->

(Xem MSC-11 — Popcon Thành công)

![](images/ndlxd-export.pdf-0266-01.png)

**Card tóm tắt:**

|Label|Giá trị|
|---|---|
|Thời gian|[dd/mm/yyyy HH:mm]|
|Số lượng thực bơm|[X] L · Khớp (xanh) / Thiếu [Y] L (đỏ) / Thừa<br>[Y] L (cam) so với xin cấp|
|Thành tiền|[X,XXX,XXX] đ|

Buttons: "Về trang chủ" (chính) · "Xem thông tin chi tiết" (phụ)

##### 3.3 Tab Bơm dầu — Sau khi ghi nhận

<!-- Trang 267 -->

![](images/ndlxd-export.pdf-0267-00.png)

**Tab Bơm dầu active.**

Hero card cập nhật (xem STT 3.5) nhưng không có sub-label và progress bar

UC06.00.10

(STT3-4).

|Tên thành phần|Control|Mô tả|
|---|---|---|
|Hero card|Card|Đổi sang THỰC NHẬN + BẮT ĐẦU / KẾT THÚC / THỜI<br>LƯỢNG (= Kết thúc − Bắt đầu, tính bằng phút).|
|Section Thông tin<br>bơm dầu|Section|Header + Badge "Đã bơm xong" (xanh lá, right-align).|
|Thời gian bơm|Label|HH:mm − HH:mm.|
|Đơn giá|Label|X,XXX đ.|
|Thành tiền|Label|X,XXX,XXX đ.<br>Font xanh lá, bold.<br>Label "THÀNH TIỀN".|
|Section Hình ảnh<br>bơm dầu|Section|Lưới thumbnail ảnh đã chụp.<br>Tap → xem full-screen.|

<!-- Trang 268 -->

|Button Xuất hóa<br>đơn|Button|Full-width, primary.<br>Chuyển sang tab Hóa đơn + mở Bottom Sheet xuất HĐ<br>(UC06.00.12/15).|
|---|---|---|
|Icon …|Button|Action: Cập nhật bơm dầu.<br>Chỉ hiện khi chưa xuất HĐ.<br>Mở lại Bottom Sheet 3.1 với dữ liệu pre-fill để sửa.|

Ghi chú: Ghi nhận bơm có thể cập nhật nếu chưa xuất HĐ. Mỗi lần cập nhật: ERP / Portal sync

lại, Activity Log ghi thêm entry "Cập nhật thông tin bơm".

<!-- Trang 269 -->

### UC06.00.12 - Xuất hoá đơn - Cây mua ngoài & Mua hoá đơn lẻ

#### 1. Thông tin chung

|Mã UC|UC06.00.12|
|---|---|
|Tên UC|Xuất hoá đơn|
|Tác nhân|(A) Nhân viên cây dầu mua ngoài — Delta Partner Portal<br>(B) Lái xe / NV — Delta ERP (HĐ lẻ)|
|Đường dẫn|(A) Partner Portal → Chi tiết đơn trạng thái fuel_done → Button<br>"Xuất hóa đơn"<br>(A) Partner Portal → Danh sách đơn → Long press đơn trạng thái<br>fuel_done → "Xuất hóa đơn"<br>(B) ERP → UC06.00.02 Chi tiết phiếu trạng thái<br>purchase_invoicing → Button "Xuất hóa đơn"|
|Điều kiện trước|(A) Đơn trạng thái fuel_done .<br>(B) Phiếu trạng thái purchase_invoicing .|
|Điều kiện sau|(A) Đơn → invoice_done .<br>(B) Phiếu → purchase_invoice_pending .<br>Tab Hóa đơn cập nhật.<br>MSC-11 Popcon.<br>Lưu lịch sử hoạt động mới.|

#### 2. Lưu đồ hoạt động

1. Người dùng tap "Xuất hóa đơn" từ tab Bơm dầu (sau ghi nhận) hoặc tab Hóa đơn (empty

state).

2. Hệ thống mở Bottom Sheet Xuất hóa đơn (3.1).

3. Người dùng chọn Số hóa đơn từ dropdown (BE pull từ email Petrolimex về):

Nhánh A — Chọn từ danh sách: Ký hiệu + Mã giao dịch PLX tự động điền. Upload ảnh HĐ

nếu muốn.

![Trang 269 — ảnh xem trước để đối chiếu hình vẽ](images/page-269.png)

<!-- Trang 270 -->

Nhánh B — Nhập thủ công: Người dùng gõ số HĐ khác → nhập thủ công Ký hiệu + Mã

PLX + upload ảnh/file HĐ bắt buộc.

4. Tap "Hoàn thành" → Validate → MSC-02 Confirm.

5. Xác nhận:

(A) Đơn Portal → invoice_done . ERP sync.

(B) Phiếu ERP → purchase_invoice_pending . Notify CBQL.

6. MSC-11 Popcon "Đã xuất hóa đơn!" (3.2) và lưu lịch sử hoạt động mới.

7. Tap "Xem thông tin chi tiết" → màn chi tiết, tab Hóa đơn cập nhật (3.3).

#### 3. Mô tả màn hình

##### 3.1 Bottom Sheet — Xuất hóa đơn

![](images/ndlxd-export.pdf-0270-09.png)

Slide-up, duration 300ms. Swipe down khi đã nhập dữ liệu → MSC-02 Unsaved Changes.

|Tên thành<br>phần|Contro<br>l|Loại|Bắt<br>buộc|Giá trị<br>mặc<br>định|Mô tả|Validate|
|---|---|---|---|---|---|---|

<!-- Trang 271 -->

|1|Handle bar<br>+ Tiêu đề|Label|Text|—|—|"Xuất hóa đơn".|—|
|---|---|---|---|---|---|---|---|
|2|Số hóa đơn|Select|List|Có|—|Tap → Dropdown danh sách<br>HĐ BE đã pull từ email<br>Petrolimex về.<br>Mỗi item: Số HĐ + Ngày.<br>Người dùng có thể gõ để lọc.<br>Nếu không có trong list: gõ<br>số khác + Enter/Xong →<br>chuyển sang nhập thủ công<br>(hiện STT 4, 5).<br>Hint: "Số thứ tự trên tờ HĐ".<br>Validate on blur.|"Vui<br>lòng<br>chọn<br>hoặc<br>nhập số<br>hóa<br>đơn."|
|3|Ký hiệu hóa<br>đơn|Input|Text|Có|Auto-<br>fill nếu<br>chọn<br>từ list|Placeholder "HĐ12345".<br>Auto-fill khi chọn từ<br>dropdown.<br>Editable nếu nhập thủ công.|"Vui<br>lòng<br>nhập ký<br>hiệu hóa<br>đơn."|
|4|Mã giao<br>dịch PLX|Input|Text|Có|Auto-<br>fill nếu<br>chọn<br>từ list|Placeholder "123-123-RFG".<br>Auto-fill khi chọn từ<br>dropdown.<br>Editable nếu nhập thủ công.|"Vui<br>lòng<br>nhập mã<br>giao<br>dịch<br>PLX."|
|5|Hóa đơn<br>(file)|Upload|—|Không<br>(auto) /<br>Có (thủ<br>công)|—|Action Sheet khi tap vào<br>vùng upload: Mở camera /<br>Chọn ảnh từ thư viện / Tải<br>file.|"Vui<br>lòng<br>upload<br>ít nhất<br>1 file<br>hoá<br>đơn."<br>(chỉ khi|

![Trang 271 — ảnh xem trước để đối chiếu hình vẽ](images/page-271.png)

<!-- Trang 272 -->

![](images/ndlxd-export.pdf-0272-00.png)

|||||||Định dạng: DPF, XML, JPG,<br>PNG.<br>Tối đa 10MB.<br>Preview thumbnail sau khi<br>chọn.<br>Tap X → xoá.<br>Bắt buộc nếu nhập thủ<br>công.|nhập thủ<br>công)|
|---|---|---|---|---|---|---|---|
|6|Button<br>Hoàn thành|Button|—|—|—|Full-width, primary xanh lá.<br>Loading + disabled khi đang<br>xử lý.|—|

Action Sheet upload (STT 5):

|Option|Mô tả|
|---|---|
|Mở camera|Chụp ảnh trực tiếp|
|Chọn ảnh từ thư viện|Mở thư viện ảnh|
|Tải file|Mở file picker (DPF, XML, JPG, PNG)|
|Hủy|Đóng Action Sheet|

<!-- Trang 273 -->

##### 3.2 MSC-11 Popcon — Đã xuất hóa đơn

(Xem MSC-11 — Popcon Thành công)

![](images/ndlxd-export.pdf-0273-02.png)

**Card tóm tắt:**

|Label|Giá trị|
|---|---|
|Số hóa đơn|[Số HĐ]|
|Ký hiệu|[Ký hiệu HĐ]|

Buttons: "Về trang chủ" (chính) · "Xem thông tin chi tiết" (phụ)

##### 3.3 Tab Hóa đơn — Sau khi xuất

<!-- Trang 274 -->

![](images/ndlxd-export.pdf-0274-01.png)

||Tên thành phần|Control|Mô tả|
|---|---|---|---|
|1|Hero card|Card|Giữ nguyên trạng thái THỰC NHẬN với BẮT ĐẦU / KẾT<br>THÚC / THỜI LƯỢNG.|
|2|Section Thông tin hóa đơn|||
|3|Số hóa đơn|Label|Giá trị số HĐ.|
|4|Ký hiệu hóa đơn|Label|Ký hiệu.|
|5|Mã tra cứu|Label|Mã tra cứu hệ thống (do BE sinh).|
|6|Link HĐDT|Label +<br>Button|Label: "LINK TRUY CẬP HĐDT".<br>URL rút gọn hiển thị.<br>Button Copy icon bên phải.<br>Button "Mở cổng tra cứu" (full-width, primary xanh, icon<br>external link) → mở browser đến link HĐDT của nhà cung<br>cấp HHDV/cây dầu mua ngoài.|
|7|Section Hóa đơn<br>Danh sách file đã upload: icon PDF/JPG + tên file + kích thước.|||

<!-- Trang 275 -->

Tap → xem full file.

|8|Icon …|Button|Action: Cập nhật hoá đơn<br>Chỉ hiện khi chưa chốt / chưa qua vòng duyệt tiếp theo.<br>Mở lại Bottom Sheet 3.1 với dữ liệu pre-fill.|
|---|---|---|---|

Ghi chú màn hình: Tab Hóa đơn empty state: illustration + "Chưa có thông tin

hóa đơn" + "Tạo hóa đơn để ghi nhận giao dịch!" + Button "Xuất hóa đơn". Tab

Bơm dầu tương tự: "Chưa có thông tin bơm dầu" + "Phiếu cấp dầu chưa được

ghi nhận bơm dầu." + Button "Ghi nhận bơm dầu".

<!-- Trang 276 -->

### UC06.00.13 - Chốt phiếu - Cây mua ngoài

#### 1. Thông tin chung

Mã UC UC06.00.13

|Mã UC|UC06.00.13|
|---|---|
|Tên UC|Chốt phiếu — Cây dầu mua ngoài|
|Tác nhân|Nhân viên cây dầu mua ngoài (Delta Partner Portal)|
|Đường dẫn|Partner Portal → Danh sách đơn hàng → Tap đơn trạng thái<br>invoice_done → Button "Chốt phiếu"|
|Điều kiện trước|Đơn hàng trạng thái invoice_done .<br>Đã ghi nhận bơm + đã xuất HĐ.|
|Điều kiện sau|Đơn → done .<br>MSC-01 notify người tạo + CBQL.|

#### 2. Lưu đồ hoạt động

1. Nhân viên cây vào màn chi tiết đơn trạng thái invoice_done .

2. Kiểm tra lại thông tin bơm + HĐ. Nếu cần sửa → tap "Cập nhật hoá đơn" (UC06.00.12) trước.

3. Tap Button "Chốt phiếu".

4. MSC-02 Confirm Popup (nội dung cảnh báo không hoàn tác).

5. Tap "Xác nhận" → Đơn → done . ERP sync realtime.

6. Notify người tạo + CBQL.

7. Lưu lịch sử hoạt động mới

8. Màn chi tiết đơn: hiển thị trạng thái "Hoàn thành". Tất cả button action ẩn.

#### 3. Mô tả màn hình

Không có màn hình riêng — xử lý qua MSC-02 trên màn chi tiết đơn (Partner

Portal).

**MSC-02 Confirm:**

![Trang 276 — ảnh xem trước để đối chiếu hình vẽ](images/page-276.png)

<!-- Trang 277 -->

|Thành phần|Nội dung|
|---|---|
|Tiêu đề|"Xác nhận chốt phiếu?"|
|Nội dung|"Bạn đang chốt phiếu [mã]. Sau khi chốt, phiếu sẽ hoàn tất và<br>không thể chỉnh sửa thêm."|
|Button "Ở lại"|Secondary.|
|Button "Xác nhận"|Primary xanh lá.|

Ghi chú: done là trạng thái terminal. Nhân viên cây không thể thực hiện thêm

bất kỳ action nào sau khi chốt. Mọi sai sót sau chốt cần xử lý qua CBQL trên

ERP.
