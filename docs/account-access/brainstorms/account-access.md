---
type: brainstorm
feature: account-access
status: in-review
status_changed: 2026-10-20
status_reason: "kéo sang In Review trên dashboard 15/10"
updated: 2026-10-15
links:
  - docs/_product/prd.md
  - docs/_product/legacy-issues.md
  - docs/_product/tenant-parameters.md
  - docs/_reverse/account-access/account-access-reverse-spec.md
  - docs/_reverse/account-access/reverse-gaps.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs-input/srs-cu/srs-mobile/srs-mobile.md
  - design/ui-common/conventions.md
---

# Đăng nhập và tài khoản cá nhân

## 1. Idea Seed

Đăng nhập và quản lý tài khoản cá nhân (`account-access`, PRD mục 7.1): người dùng đăng nhập vào web và app, khôi phục hoặc đổi mật khẩu, xem thông tin cá nhân; được cấp nhiều chi nhánh thì chọn chi nhánh trước khi vào Home. Làm lại từ hiện trạng SRS cũ (SRS Web 30/9/2026, SRS Mobile 5/10/2026): mỗi chức năng hiện có được quyết Giữ, Cải tiến hoặc Bỏ.

## 2. Context

Đây là cửa vào chung của mọi module, cả web (nhân viên văn phòng, quản lý) và app (lái xe, hiện trường, đối tác cây dầu). Hệ thống cũ có đủ đăng nhập, quên mật khẩu, đổi mật khẩu, hồ sơ, nhưng Web và Mobile lệch nhau ở nhiều điểm (ngưỡng khoá 5 và 10 lần, link và OTP, ghi nhớ đăng nhập, xác nhận đăng xuất) và còn các điểm gắn chặt với Delta: mật khẩu mặc định chung, đồng bộ mật khẩu giữa ERP Delta và PMX, email IT Delta viết cứng.

Sản phẩm chuyển sang SaaS nhiều khách, nên mọi con số (ngưỡng khoá, hạn mã, chính sách mật khẩu, thời gian phiên) và nơi liên hệ hỗ trợ trở thành tham số theo khách. Đăng nhập bằng Google song song mật khẩu, bật theo khách, xem [[docs/account-access/brainstorms/google-sso.md|brainstorm đăng nhập Google]] (DEC-405). Đây là feature đơn giản, không cần hướng dẫn sử dụng gắn theo chức năng (ISS-15).

Feature liên quan: `access-control` (Admin tạo tài khoản, cấp phạm vi chi nhánh, vô hiệu hoá, mở khoá, đặt lại mật khẩu), `organization` (cơ cấu Công ty → Chi nhánh → Cơ sở dùng ở bước chọn chi nhánh), `employee-records` (hồ sơ nhân viên hiện ở màn thông tin cá nhân), `common-workspace` (màn Home sau đăng nhập), `fuel-stations` (thông tin cây dầu của tài khoản đối tác).

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Nhân viên văn phòng, quản lý (web) | Phải chọn lại chi nhánh mỗi lần vào; muốn sang chi nhánh khác phải đăng xuất | Vào nhanh đúng chi nhánh, đổi chi nhánh không mất việc đang dở |
| Lái xe, hiện trường (app) | Không có email công ty nên không tự lấy lại mật khẩu được; bị khoá thì đứng việc tới khi có người mở | Ít phải đăng nhập lại; bị khoá thì tự mở được sau một thời gian |
| Nhân viên đối tác cây dầu (app) | Màn tài khoản chỉ có đăng xuất, không đổi được mật khẩu | Dùng đủ chức năng mật khẩu như nhân viên |
| Bộ phận IT hoặc Admin của khách | Nhận yêu cầu đặt lại mật khẩu qua email, không biết ai đã xử lý | Có đủ thông tin để đặt lại mật khẩu đúng người |
| Nhân sự | Tạo nhân viên mới xong phải nhờ người khác cấp tài khoản | Tài khoản được tạo từ hồ sơ nhân viên (`employee-records` gọi sang `access-control`) và tự gửi mật khẩu tạm |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Nhân viên văn phòng | Đăng nhập web | mỗi ngày | cao | Chậm hoặc lỗi thì cả ngày làm việc trễ |
| Người phụ trách nhiều chi nhánh | Chọn chi nhánh khi vào | mỗi lần đăng nhập | cao | Chọn nhầm thì làm việc trên dữ liệu chi nhánh khác |
| Người phụ trách nhiều chi nhánh | Đổi chi nhánh trong phiên | vài lần mỗi tuần | trung | |
| Lái xe, hiện trường | Đăng nhập app | hiếm (phiên được giữ) | cao | Không vào được app thì không nhận việc, không chụp chứng từ |
| Mọi người dùng | Quên mật khẩu, đổi mật khẩu | vài lần mỗi năm | trung | |
| Mọi người dùng | Xem thông tin cá nhân, đổi ngôn ngữ | hiếm | thấp | |
| Bộ phận IT hoặc Admin | Đặt lại mật khẩu theo yêu cầu | theo yêu cầu | trung | Người dùng chờ, không làm việc được |

## 4. Capabilities Breakdown

Nhãn nguồn: `[SOP+]` là chức năng có trong SRS cũ (kèm quyết định Giữ hoặc Cải tiến), `[Mới]` là chức năng SRS cũ chưa có.

### P0 — must have

- A1 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Đăng nhập bằng tên tài khoản hoặc email, như nhau trên web và app. Đăng nhập bằng số điện thoại là tuỳ chọn theo khách `P-dang-nhap-bang-sdt` (Delta: tắt).
- A2 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Đếm lần nhập sai chung cho web và app; sai liên tiếp `P-so-lan-sai-mat-khau` (Delta: 5) lần thì tài khoản chuyển sang Tạm khoá; về 0 khi đăng nhập đúng. Mỗi lần sai báo số lần thử còn lại; tên tài khoản không tồn tại cũng được đếm và báo y như vậy để không lộ tài khoản có thật.
- A3 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Tạm khoá tự mở sau `P-thoi-gian-tam-khoa` (Delta: 30 phút); đặt lại mật khẩu thành công cũng mở khoá; Admin mở tay ở `access-control`.
- A4 [SOP+] [Lõi] **Giữ** — Chặn đăng nhập khi tài khoản bị khoá hoặc vô hiệu hoá, chưa được cấp chi nhánh nào, hoặc không có quyền vào web/app; mỗi trường hợp một câu báo riêng.
- A5 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Tài khoản mới và tài khoản được đặt lại mật khẩu nhận mật khẩu tạm riêng: có email thì hệ thống tự gửi (dù tài khoản tạo từ Admin hay từ hồ sơ nhân viên); không có email thì người tạo hoặc người đặt lại thấy mật khẩu tạm trên màn đúng một lần và tự gửi cho người dùng ngoài phần mềm; hết hạn sau `P-han-mat-khau-tam` (Delta: 72 giờ); đăng nhập bằng mật khẩu tạm thì phải tạo mật khẩu mới trước khi vào. Sai mật khẩu tạm đủ số lần thì Tạm khoá như thường; hai lần đặt lại liên tiếp thì chỉ mật khẩu tạm mới nhất còn hiệu lực. Bỏ mật khẩu mặc định chung.
- A6 [SOP+] [Lõi] **Cải tiến** — Chọn chi nhánh sau đăng nhập: 1 chi nhánh thì vào thẳng; từ 2 chi nhánh hiện cửa sổ chọn: chọn công ty mẹ (khi có quyền toàn tổ chức) hoặc đúng một chi nhánh, tìm theo tên chi nhánh hoặc tỉnh thành, sắp theo lần dùng gần nhất, nút Chọn khoá tới khi chọn; lần đăng nhập sau tự vào chi nhánh lần trước nếu còn quyền (cả web và app); bấm Huỷ ở cửa sổ chọn là đăng xuất. Cơ sở chọn ở màn Home (`common-workspace`), không ở bước này.
- A8 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Phiên đăng nhập web: không chọn "Ghi nhớ đăng nhập" thì hết khi đóng trình duyệt hoặc sau `P-het-phien-khong-thao-tac` (Delta: 8 giờ) không thao tác; có chọn thì giữ `P-thoi-han-ghi-nho` (Delta: 30 ngày). App không có ô ghi nhớ, luôn giữ phiên tới khi đăng xuất hoặc không mở app quá `P-thoi-han-ghi-nho` (Delta: 30 ngày).
- A11 [Mới] [Lõi] — Mỗi khách một đường dẫn đăng nhập riêng; tên tài khoản và email chỉ cần duy nhất trong một khách; màn đăng nhập lấy tham số theo khách của đường dẫn.
- A10 [SOP+] [Lõi] **Giữ** — Ô mật khẩu ẩn ký tự, có biểu tượng hiện/ẩn; nút Đăng nhập, Xác nhận khoá và hiện vòng chờ khi đang gửi để không bấm lặp.
- A9 [SOP+] [Lõi] **Giữ** — Có phiên hợp lệ thì bỏ qua màn đăng nhập; phiên hết hạn đưa về màn đăng nhập kèm thông báo; lỗi hệ thống và mất mạng báo toast. Áp cho cả web và app.
- B1 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Quên mật khẩu, tự đặt lại qua email: web gửi link, app gửi mã OTP. Dùng được với tài khoản Đang hoạt động, Tạm khoá hoặc Chờ kích hoạt có email đăng ký (Vô hiệu hoá thì không gửi); câu báo sau khi gửi giống nhau dù tài khoản có tồn tại hay không. Gửi lại sau `P-cho-gui-lai-ma` (Delta: 60 giây), tối đa `P-so-lan-gui-ma-moi-gio` (Delta: 5) lần mỗi giờ, đếm theo tên đã nhập dù tài khoản có tồn tại hay không. Email gửi lại là thư trả lời của email trước để không rải nhiều thư trong hộp thư. Link web có hạn `P-han-link-dat-lai` (Delta: 30 phút), dùng một lần.
- B2 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Mã OTP 6 chữ số (cố định trong sản phẩm), hiệu lực `P-han-ma-otp` (Delta: 5 phút), nhập sai tối đa `P-so-lan-sai-otp` (Delta: 5) lần thì phải gửi mã mới.
- B3 [SOP+] [Lõi] [Cấu hình] **Giữ** — Quên mật khẩu, liên hệ hỗ trợ: người dùng nhập tên tài khoản, hệ thống gửi email yêu cầu đặt lại mật khẩu tới địa chỉ hỗ trợ của khách `P-email-ho-tro-mat-khau` (Delta: it@delta.com.vn). Người nhận đặt lại mật khẩu ở `access-control`, tài khoản về Chờ kích hoạt và mọi phiên đang mở kết thúc. Gửi email lỗi thì báo người dùng "Chưa gửi được yêu cầu. Thử lại sau.", không tự gửi lại; người dùng gửi lại theo cùng giới hạn của B1. Địa chỉ hỗ trợ là thông tin bắt buộc khi khởi tạo khách.
- B4 [SOP+] [Lõi] [Cấu hình] **Giữ** — Đổi mật khẩu: mật khẩu cũ, mật khẩu mới, nhập lại; theo chính sách `P-chinh-sach-mat-khau` (Delta: ít nhất 8 ký tự gồm chữ thường, chữ hoa, số, ký tự đặc biệt); không trùng mật khẩu hiện tại.
- B5 [Mới] [Lõi] — Đổi hoặc đặt lại mật khẩu thành công thì đăng xuất mọi thiết bị khác của tài khoản.
- B6 [SOP+] [Lõi] **Giữ** — Tạo mật khẩu mới (sau mật khẩu tạm hoặc link/OTP đặt lại) xong thì về màn đăng nhập.
- C1 [SOP+] [Lõi] **Giữ** — Đăng xuất từ menu ảnh đại diện, hỏi xác nhận trên cả web và app, như nhau cho mọi loại tài khoản.

### P1 — should have

- A7 [SOP+] [Lõi] **Cải tiến** — Đổi chi nhánh ngay trong ứng dụng, không cần đăng xuất; đang có dữ liệu chưa lưu thì hỏi xác nhận rời trang theo mẫu chung.
- C2 [SOP+] [Lõi] **Cải tiến** — Tài khoản đối tác (v1: loại Cây dầu) vào thẳng Home của đối tác, không qua chọn chi nhánh, dùng đủ quên, đổi, tạo mật khẩu như tài khoản nội bộ; Admin của khách đặt lại mật khẩu cho tài khoản đối tác ở `access-control`.
- C3 [SOP+] [Gói: Nhiên liệu] **Giữ** — Màn Tài khoản cây dầu trên app (chỉ đọc): tên cây dầu, mã đối tác, nhà cung cấp, người đại diện, hạn mức lít của tháng hiện tại (đã cấp, còn lại, về 0 đầu tháng), loại hợp đồng Đặt cọc hoặc Tín chấp, số tiền đặt cọc khi Đặt cọc, mục Hợp đồng ẩn khi Tín chấp, ghi chú; kèm đổi mật khẩu, ngôn ngữ, đăng xuất. Sửa thông tin cây dầu thuộc `fuel-stations`.
- D1 [SOP+] [Lõi] **Cải tiến** — Thông tin cá nhân chỉ đọc, lấy từ hồ sơ ở `employee-records` (trường hiển thị do feature đó quyết); riêng ảnh đại diện người dùng tự đổi được.
- D2 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Lịch sử hoạt động: thao tác của chính người dùng trong `P-so-ngay-lich-su-hoat-dong` (Delta: 90 ngày) gần nhất.
- D3 [SOP+] [Lõi] [Cấu hình] **Cải tiến** — Đổi ngôn ngữ giao diện trên cả web và app, lưu theo tài khoản; danh sách `P-ngon-ngu-giao-dien` (Delta: Tiếng Việt, Tiếng Anh). Bỏ tiếng Nhật.
- D4 [SOP+] [Lõi] **Giữ** — App: màn Splash khi mở, Onboarding giới thiệu lần đầu cài.
- D5 [SOP+] [Lõi] [Cấu hình] **Giữ** — Màn đăng nhập có dòng hướng dẫn cho người chưa có tài khoản, nội dung `P-huong-dan-cap-tai-khoan` (Delta: như mặc định sản phẩm).

### P2 — nice to have

- E1 [Mới] [Lõi] — Nhật ký bảo mật (đăng nhập đúng và sai, khoá, mở khoá, đổi mật khẩu, kèm thiết bị). Không làm ở v1; khi làm, màn xem thuộc `access-control`.

### Bỏ hoặc chuyển

| Chức năng SRS cũ | Quyết định | Lý do |
|---|---|---|
| Đồng bộ mật khẩu giữa ERP Delta và PMX (SRS Web tr.260, 272, 274) | Bỏ | Sản phẩm mới là một hệ thống, một tài khoản |
| Mật khẩu mặc định chung (SRS Web tr.248, 273) | Bỏ, thay bằng A5 | Ai biết tên tài khoản là vào được tới khi chủ đổi |
| Hiện họ tên sau khi nhập tên tài khoản ở Quên mật khẩu; câu "Tên tài khoản không chính xác." (SRS Web tr.262) | Bỏ | Để lộ tài khoản và họ tên nhân viên |
| Ô "Ghi nhớ đăng nhập" trên app (SRS Mobile tr.47) | Bỏ, thay bằng A8 | App luôn giữ phiên |
| Lỗi riêng từng ô trên app: "Tài khoản không hợp lệ", "Mật khẩu không đúng" (SRS Mobile tr.48) | Bỏ, dùng một câu chung | Lỗi riêng ô tên tài khoản để lộ tài khoản có tồn tại |
| Gửi lại OTP chỉ khi mã cũ hết hạn (SRS Mobile tr.58) | Đổi thành chờ 60 giây | Email đến chậm thì người dùng phải chờ đủ 5 phút |
| Tiếng Nhật trong danh sách ngôn ngữ (SRS Web tr.162) | Bỏ | PRD chỉ cam kết tiếng Việt và tiếng Anh |
## 5. Core Flows (Happy Path)

### 5.1 Đăng nhập và chọn chi nhánh

1. Người dùng mở web, hoặc mở app (Splash; lần đầu cài thì qua Onboarding).
2. Hệ thống kiểm tra phiên: còn phiên thì sang bước 6.
3. Người dùng nhập tên tài khoản (hoặc email) và mật khẩu, bấm Đăng nhập. Web có thể chọn Ghi nhớ đăng nhập.
4. Hệ thống kiểm tra tài khoản, mật khẩu, trạng thái, quyền vào web hoặc app.
5. Đúng và đang dùng mật khẩu tạm → sang 5.2. Đúng và Đang hoạt động → tiếp.
6. Tài khoản đối tác → vào Home đối tác. Tài khoản nội bộ 1 chi nhánh → vào Home chi nhánh đó. Đã có chi nhánh lần trước còn quyền → vào thẳng chi nhánh đó. Từ 2 chi nhánh và chưa có lựa chọn → cửa sổ chọn.
7. Người dùng bấm Chọn → vào Home của chi nhánh hoặc công ty mẹ đã chọn.

```
 Mở web/app ──► Còn phiên? ──có──────────────────────────┐
                  │không                                 │
                  ▼                                      ▼
          Nhập tài khoản + mật khẩu            Loại tài khoản?
                  │                         ┌──────┼───────────┐
                  ▼                     đối tác  nội bộ 1 CN  nội bộ ≥2 CN
          Kiểm tra (DP-1–4) ──sai──► báo lỗi, │       │            │
                  │đúng           trừ lần thử▼       ▼            ▼
          Mật khẩu tạm? ──có──► 5.2   Home đối tác  Home CN   Chọn chi nhánh
                  │không                                         │Huỷ → đăng xuất
                  └────────────► Loại tài khoản?                 ▼
                                                             Home CN đã chọn
```

### 5.2 Kích hoạt bằng mật khẩu tạm

1. Admin tạo tài khoản hoặc đặt lại mật khẩu ở `access-control`; hệ thống gửi mật khẩu tạm tới email của tài khoản.
2. Người dùng đăng nhập bằng mật khẩu tạm (trước khi hết hạn).
3. Hệ thống mở màn Tạo mật khẩu mới.
4. Người dùng nhập mật khẩu mới và nhập lại, bấm Xác nhận.
5. Hệ thống kiểm tra theo chính sách, lưu, chuyển tài khoản sang Đang hoạt động, báo thành công, về màn đăng nhập.
6. Người dùng đăng nhập bằng mật khẩu mới (theo 5.1).

### 5.3 Quên mật khẩu — tự đặt lại

1. Ở màn đăng nhập, người dùng bấm Quên mật khẩu, chọn "Đặt lại qua email".
2. Người dùng nhập tên tài khoản, bấm Xác nhận.
3. Hệ thống: tài khoản tồn tại, Đang hoạt động hoặc Tạm khoá, có email → gửi email (web: link; app: mã OTP). Mọi trường hợp đều hiện cùng một màn "Kiểm tra email".
4. Web: người dùng mở link → màn Tạo mật khẩu mới. App: người dùng nhập mã OTP 6 số; mã đúng → màn Tạo mật khẩu mới.
5. Người dùng đặt mật khẩu mới; hệ thống lưu, mở khoá nếu đang Tạm khoá, đăng xuất các thiết bị khác, về màn đăng nhập.

```
 Quên mật khẩu ─► Đặt lại qua email ─► Nhập tên tài khoản ─► Xác nhận
                                                               │
                         ┌──── có tài khoản + email? ──────────┤
                         │có                                   │không
                         ▼                                     ▼
              Gửi link (web) / OTP (app)              (không gửi gì)
                         └──────────────┬──────────────────────┘
                                        ▼
                         Màn "Kiểm tra email" (giống nhau)
                                        │
            web: mở link ───────────────┼──────── app: nhập OTP ──sai──► còn lượt? ─hết─► gửi mã mới
                                        ▼                         │đúng
                               Tạo mật khẩu mới ◄─────────────────┘
                                        ▼
                     Lưu · mở khoá · đăng xuất thiết bị khác · về đăng nhập
```

### 5.4 Quên mật khẩu — liên hệ hỗ trợ

1. Ở màn Quên mật khẩu, người dùng chọn "Liên hệ IT" (dùng khi không có email hoặc không nhận được email).
2. Người dùng nhập tên tài khoản, bấm Xác nhận.
3. Hệ thống gửi email tới địa chỉ hỗ trợ của khách: tên tài khoản, họ tên, thời gian yêu cầu (chỉ gửi khi tài khoản tồn tại); người dùng luôn thấy cùng một màn "Đã gửi yêu cầu".
4. Người nhận đặt lại mật khẩu ở `access-control`; người dùng nhận mật khẩu tạm (qua email, hoặc người đặt lại gửi ngoài phần mềm khi không có email) và đi tiếp theo 5.2.
5. Gửi email tới bộ phận hỗ trợ lỗi → người dùng thấy "Chưa gửi được yêu cầu. Thử lại sau."

### 5.5 Đổi mật khẩu

1. Người dùng mở Thông tin cá nhân → Đổi mật khẩu.
2. Nhập mật khẩu cũ, mật khẩu mới, nhập lại; bấm Xác nhận.
3. Hệ thống kiểm tra, lưu, đăng xuất các thiết bị khác, báo thành công, đóng cửa sổ, ở lại màn Thông tin cá nhân.

### 5.6 Đổi chi nhánh trong phiên

1. Người dùng có từ 2 chi nhánh bấm tên chi nhánh đang dùng trên thanh đầu trang.
2. Hệ thống mở cửa sổ chọn chi nhánh (như bước 6 của 5.1).
3. Người dùng chọn chi nhánh khác → hệ thống tải lại Home của chi nhánh đó và nhớ lựa chọn cho lần sau.

### 5.7 Đăng xuất

1. Người dùng mở menu ảnh đại diện (web) hoặc tab Tài khoản (app), bấm Đăng xuất.
2. Hệ thống hỏi xác nhận; người dùng bấm Đăng xuất.
3. Hệ thống kết thúc phiên trên thiết bị này, về màn đăng nhập.

### 5.8 Thông tin cá nhân, lịch sử, ngôn ngữ

1. Người dùng mở menu ảnh đại diện → Thông tin tài khoản (web) hoặc tab Tài khoản (app).
2. Xem thông tin chỉ đọc; đổi ảnh đại diện nếu muốn.
3. Mở Lịch sử hoạt động để xem thao tác của mình trong `P-so-ngay-lich-su-hoat-dong`.
4. Đổi ngôn ngữ: chọn trong danh sách → giao diện tải lại theo ngôn ngữ mới, áp cho mọi thiết bị của tài khoản.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| DP-1 | 5.1 | Tên tài khoản (hoặc email) và mật khẩu khớp? | Kiểm tra trạng thái (DP-2) | Trừ 1 lần thử, báo còn n lần; hết lượt → Tạm khoá |
| DP-2 | 5.1 | Tài khoản Đang hoạt động hoặc Chờ kích hoạt? | Kiểm tra quyền (DP-3) | Báo bị khoá (Tạm khoá: kèm thời gian mở) hoặc vô hiệu hoá |
| DP-3 | 5.1 | Có quyền vào kênh đang dùng (web hoặc app)? | Kiểm tra chi nhánh (DP-4) | Màn lỗi không có quyền, nút Quay về đăng nhập |
| DP-4 | 5.1 | Tài khoản nội bộ có ít nhất 1 chi nhánh? | 1 CN vào thẳng, ≥2 CN mở cửa sổ chọn | Báo chưa được cấp chi nhánh |
| DP-5 | 5.1 | Đăng nhập bằng mật khẩu tạm còn hạn? | Màn Tạo mật khẩu mới | Mật khẩu tạm hết hạn: báo liên hệ hỗ trợ |
| DP-6 | 5.1 | Lựa chọn chi nhánh lần trước còn quyền? | Vào thẳng chi nhánh đó | Mở cửa sổ chọn |
| DP-7 | 5.3 | Tài khoản có email và không bị vô hiệu hoá? | Gửi link hoặc OTP | Không gửi; vẫn hiện màn "Kiểm tra email" |
| DP-8 | 5.3 | Đã quá `P-cho-gui-lai-ma` từ lần gửi trước và chưa vượt số lần mỗi giờ? | Gửi | Báo chờ hoặc đã vượt giới hạn |
| DP-9 | 5.3 | Mã OTP đúng và còn hạn? | Màn Tạo mật khẩu mới | Báo sai; sai đủ 5 lần thì phải gửi mã mới |
| DP-10 | 5.3 | Link đặt lại còn hạn và chưa dùng? | Màn Tạo mật khẩu mới | Màn báo link hết hạn, nút Gửi lại |
| DP-11 | 5.2, 5.3, 5.5 | Mật khẩu mới đúng chính sách, khớp ô nhập lại, khác mật khẩu hiện tại? | Lưu | Báo lỗi tại ô |
| DP-12 | 5.5 | Mật khẩu cũ đúng? | Kiểm tra DP-11 | Báo mật khẩu cũ không đúng |

### 6.2 Scenario Matrix

| From State | To State | Rule | Action | Result |
|------------|----------|------|--------|--------|
| Nội bộ, 1 chi nhánh | Home | Đăng nhập đúng | Vào thẳng | Không hiện cửa sổ chọn |
| Nội bộ, ≥2 chi nhánh | Home CN đã chọn | Đăng nhập đúng | Chọn chi nhánh | Nhớ lựa chọn |
| Nội bộ, quyền toàn công ty | Home công ty mẹ | Có quyền toàn tổ chức | Chọn "Công ty mẹ" | Thấy dữ liệu mọi chi nhánh theo quyền |
| Nội bộ, 0 chi nhánh | Màn đăng nhập | Chưa được cấp | — | Báo chưa được cấp chi nhánh |
| Đối tác Cây dầu | Home đối tác | Đăng nhập đúng | — | Không qua chọn chi nhánh |
| Có email | Kiểm tra email | Quên mật khẩu | Đặt lại qua email | Nhận link hoặc OTP |
| Không có email | Đã gửi yêu cầu | Quên mật khẩu | Liên hệ IT | Chờ mật khẩu tạm |

### 6.3 State Transitions

```
Tài khoản: Chờ kích hoạt ──đặt mật khẩu mới──► Đang hoạt động ──sai đủ lần──► Tạm khoá
                ▲                                  ▲   │                          │
                │ Admin đặt lại mật khẩu           │   └──── Admin vô hiệu hoá ──► Vô hiệu hoá
                └──────────────────────────────────┴── hết thời gian khoá / đặt lại mật khẩu / Admin mở
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Tài khoản | (chưa có) | Chờ kích hoạt | Admin tạo tài khoản (`access-control`) | — |
| Tài khoản | Chờ kích hoạt | Đang hoạt động | Người dùng tạo mật khẩu mới | có (Admin đặt lại mật khẩu) |
| Tài khoản | Đang hoạt động | Chờ kích hoạt | Admin đặt lại mật khẩu | có |
| Tài khoản | Đang hoạt động | Tạm khoá | Sai mật khẩu đủ `P-so-lan-sai-mat-khau` lần liên tiếp | có |
| Tài khoản | Tạm khoá | Chờ kích hoạt | Admin đặt lại mật khẩu | có |
| Tài khoản | Chờ kích hoạt | Tạm khoá | Sai mật khẩu tạm đủ `P-so-lan-sai-mat-khau` lần | có |
| Tài khoản | Tạm khoá | Đang hoạt động | Hết `P-thoi-gian-tam-khoa`; hoặc đặt lại mật khẩu qua email; hoặc Admin mở | có |
| Tài khoản | mọi trạng thái | Vô hiệu hoá | Admin vô hiệu hoá (`access-control`) | có (Admin kích hoạt lại) |
| Tài khoản | Vô hiệu hoá | Chờ kích hoạt | Admin kích hoạt lại, hệ thống cấp mật khẩu tạm mới | có |
| Phiên | Đang dùng | Kết thúc | Đăng xuất, hết hạn, đổi mật khẩu (thiết bị khác), Admin đặt lại mật khẩu (mọi thiết bị), tài khoản bị vô hiệu hoá | không |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Đóng app khi đang ở màn nhập OTP | Mã đã gửi còn hiệu lực tới hết hạn | Mở lại Quên mật khẩu, gửi mã mới (theo giới hạn) | Mã hết hạn tự vô hiệu |
| Email không tới | Yêu cầu đã ghi | Gửi lại sau `P-cho-gui-lai-ma`, hoặc chọn Liên hệ IT | — |
| Link hoặc mã hết hạn | Không đổi gì | Gửi lại | — |
| Hai thiết bị cùng đặt lại mật khẩu | Mỗi lần gửi mới làm mã hoặc link cũ hết hiệu lực | Dùng mã hoặc link mới nhất | Mã, link cũ vô hiệu |
| Mất mạng khi bấm Đăng nhập | Không gửi gì | Báo mất kết nối, thử lại | — |
| Chọn chi nhánh rồi đóng trình duyệt trước khi bấm Chọn | Phiên chưa có chi nhánh | Lần vào sau hiện lại cửa sổ chọn | — |

### 6.5 Other Edge Cases

- Đang dùng mà quyền chi nhánh bị thu hồi hoặc tài khoản bị vô hiệu hoá: phiên kết thúc ở lần thao tác kế tiếp, báo theo `E-common-012` hoặc câu bị vô hiệu hoá.
- Đổi mật khẩu trên web khi app đang mở: app bị đăng xuất ở lần thao tác kế tiếp, báo phiên hết hạn (`E-common-010`).
- Mật khẩu tạm hết hạn mà chưa kích hoạt: đăng nhập báo hết hạn; người dùng chọn Quên mật khẩu (nếu có email) hoặc Liên hệ IT.
- Tạm khoá rồi tự mở sau `P-thoi-gian-tam-khoa`: bộ đếm về 0.
- Chọn "Công ty mẹ" chỉ hiện khi tài khoản có quyền toàn tổ chức; tìm chi nhánh không có kết quả thì hiện trạng thái rỗng.
- Bấm Huỷ ở cửa sổ chọn chi nhánh: đăng xuất và xoá phiên ghi nhớ, tránh vòng lặp đăng nhập.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Tên tài khoản (đăng nhập) | Bắt buộc. Nhận tên tài khoản hoặc email; số điện thoại khi bật `P-dang-nhap-bang-sdt` |
| Mật khẩu (đăng nhập) | Bắt buộc. Chỉ so khớp, không kiểm chính sách |
| Mật khẩu mới | Bắt buộc. Theo `P-chinh-sach-mat-khau`; khác mật khẩu hiện tại |
| Nhập lại mật khẩu mới | Bắt buộc. Trùng mật khẩu mới |
| Mật khẩu cũ (đổi mật khẩu) | Bắt buộc. Trùng mật khẩu hiện tại |
| Tên tài khoản (quên mật khẩu) | Bắt buộc. Không báo tài khoản có tồn tại hay không |
| Mã OTP | 6 chữ số; đủ 6 số thì tự kiểm tra |
| Ảnh đại diện | Ảnh JPG hoặc PNG, tối đa 5 MB (nhỏ hơn mức chung 250 MB vì chỉ là ảnh đại diện) |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| `P-so-lan-sai-mat-khau` | Delta: 5 lần | liên tiếp, chung web và app | Tạm khoá |
| `P-thoi-gian-tam-khoa` | Delta: 30 phút | từ lúc khoá | Tự mở, bộ đếm về 0 |
| `P-han-mat-khau-tam` | Delta: 72 giờ | từ lúc gửi | Mật khẩu tạm hết hiệu lực |
| `P-han-ma-otp` | Delta: 5 phút | từ lúc gửi | Mã hết hiệu lực |
| `P-so-lan-sai-otp` | Delta: 5 lần | mỗi mã | Phải gửi mã mới |
| `P-cho-gui-lai-ma` | Delta: 60 giây | giữa 2 lần gửi link, OTP hoặc yêu cầu hỗ trợ | Nút Gửi lại khoá, đếm ngược |
| `P-so-lan-gui-ma-moi-gio` | Delta: 5 lần | 60 phút, mỗi tài khoản | Báo đã gửi quá nhiều lần |
| `P-han-link-dat-lai` | Delta: 30 phút | từ lúc gửi | Màn link hết hạn |
| `P-het-phien-khong-thao-tac` | Delta: 8 giờ | web, không ghi nhớ | Hết phiên |
| `P-thoi-han-ghi-nho` | Delta: 30 ngày | web có ghi nhớ; app không mở | Hết phiên |
| `P-so-ngay-lich-su-hoat-dong` | Delta: 90 ngày | — | Không hiện cũ hơn |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Bỏ trống tên tài khoản hoặc mật khẩu | "Nhập Tên tài khoản." / "Nhập Mật khẩu." | E-common-001 |
| Sai tên tài khoản hoặc mật khẩu | "Tên tài khoản hoặc mật khẩu không đúng. Còn {n} lần thử." | E-? |
| Vừa bị tạm khoá hoặc đăng nhập khi đang tạm khoá | "Tài khoản tạm khoá do nhập sai nhiều lần. Thử lại sau {hh:mm}, đặt lại mật khẩu hoặc liên hệ IT." | E-? |
| Tài khoản bị vô hiệu hoá | "Tài khoản đã bị vô hiệu hoá. Liên hệ quản trị viên." | E-? |
| Chưa được cấp chi nhánh | "Tài khoản chưa được cấp chi nhánh nào. Liên hệ quản trị viên." | E-? |
| Không có quyền vào web hoặc app | "Tài khoản này không được dùng {Web/ứng dụng}. Liên hệ quản trị viên." | E-? |
| Mật khẩu tạm hết hạn | "Mật khẩu tạm đã hết hạn. Đặt lại mật khẩu hoặc liên hệ IT." | E-? |
| Mật khẩu cũ sai | "Mật khẩu cũ không đúng." | E-? |
| Mật khẩu mới không đúng chính sách | "Mật khẩu cần ít nhất 8 ký tự, có chữ thường, chữ hoa, số và ký tự đặc biệt." (theo `P-chinh-sach-mat-khau`) | E-? |
| Mật khẩu mới trùng mật khẩu hiện tại | "Mật khẩu mới phải khác mật khẩu đang dùng." | E-? |
| Nhập lại không khớp | "Mật khẩu nhập lại không khớp." | E-? |
| OTP sai | "Mã không đúng. Còn {n} lần nhập." | E-? |
| OTP sai đủ lần hoặc hết hạn | "Mã đã hết hiệu lực. Gửi mã mới để tiếp tục." | E-? |
| Link đặt lại hết hạn hoặc đã dùng | "Link đặt lại mật khẩu đã hết hạn. Gửi lại link mới." | E-? |
| Gửi quá nhiều lần trong 1 giờ | "Bạn đã gửi quá nhiều yêu cầu. Thử lại sau {hh:mm}." | E-? |
| Gửi yêu cầu Liên hệ IT lỗi | "Chưa gửi được yêu cầu. Thử lại sau." | E-? |
| Lỗi hệ thống | "Đã xảy ra lỗi. Thử lại sau." | E-common-008 |
| Mất mạng | "Mất kết nối. Kiểm tra mạng và thử lại." | E-common-009 |
| Phiên hết hạn | "Phiên làm việc đã hết hạn. Đăng nhập lại." | E-common-010 |
| Quyền vừa thay đổi | "Quyền của tài khoản vừa thay đổi. Tải lại để áp dụng." | E-common-012 |
| Không tìm thấy chi nhánh | "Không có chi nhánh phù hợp." | — |

#### Success messages

| Tình huống | Wording |
|---|---|
| Tạo mật khẩu mới xong | "Đã đặt mật khẩu mới. Đăng nhập lại bằng mật khẩu này." |
| Đổi mật khẩu xong | "Đã đổi mật khẩu. Các thiết bị khác đã được đăng xuất." |
| Đổi ngôn ngữ | "Đã đổi ngôn ngữ." |
| Đổi ảnh đại diện | "Đã cập nhật ảnh đại diện." |

#### Email

| Email | Tiêu đề | Nội dung chính |
|---|---|---|
| Mật khẩu tạm | "Mật khẩu tạm cho tài khoản {tên sản phẩm}" | Tên tài khoản, mật khẩu tạm, hạn dùng, đường vào web và app, nhắc phải đặt mật khẩu mới ở lần đăng nhập đầu |
| Link đặt lại (web) | "Đặt lại mật khẩu tài khoản {tên sản phẩm}" | Link đặt lại, hạn dùng; "Nếu bạn không yêu cầu, bỏ qua email này." |
| Mã OTP (app) | "Mã đặt lại mật khẩu: {mã}" | Mã 6 số, hạn {phút} phút; "Nếu bạn không yêu cầu, bỏ qua email này." |
| Yêu cầu Liên hệ IT (gửi bộ phận hỗ trợ) | "Yêu cầu đặt lại mật khẩu: {tên tài khoản}" | Tên tài khoản, họ tên, chi nhánh, thời gian yêu cầu, kênh gửi (web hoặc app) |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Sau khi gửi đặt lại qua email (web) | Tiêu đề "Kiểm tra email" · "Nếu tài khoản có email đăng ký, link đặt lại mật khẩu đã được gửi tới email đó. Không nhận được email? Chọn Liên hệ IT." |
| Sau khi gửi đặt lại qua email (app) | Tiêu đề "Nhập mã xác thực" · "Nếu tài khoản có email đăng ký, mã 6 số đã được gửi tới email đó. Mã có hiệu lực {phút} phút." (theo `P-han-ma-otp`) |
| Sau khi gửi Liên hệ IT | Tiêu đề "Đã gửi yêu cầu" · "Bộ phận hỗ trợ sẽ đặt lại mật khẩu và gửi mật khẩu tạm cho bạn." |
| Nút gửi lại đang chờ | "Gửi lại sau {s} giây" |
| Hỏi xác nhận đăng xuất | Tiêu đề "Đăng xuất?" · "Bạn sẽ cần đăng nhập lại để tiếp tục." · `[Đăng xuất] [Ở lại]` |
| Cửa sổ chọn chi nhánh | Tiêu đề "Chọn chi nhánh" · ngăn cách "Hoặc chọn chi nhánh cụ thể" |
| Người chưa có tài khoản | Nội dung theo `P-huong-dan-cap-tai-khoan` |

## 8. Assumptions

- Web và app dùng chung một bộ tài khoản, mật khẩu, trạng thái và bộ đếm sai.
- Admin của khách (hoặc bộ phận IT nhận email hỗ trợ) có quyền đặt lại mật khẩu ở `access-control`.
- Mật khẩu tạm gửi qua email; tài khoản không có email nhận mật khẩu tạm từ người tạo hoặc người đặt lại, gửi ngoài phần mềm.
- Phần lớn lái xe không có email công ty, nên với họ Liên hệ IT là đường lấy lại mật khẩu chính.
- Thông tin hồ sơ ở màn cá nhân lấy từ `employee-records`, feature này không sửa.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Người không có email (lái xe, hiện trường) quên mật khẩu phải chờ bộ phận IT, nhất là ngoài giờ | thường | Lái xe không nhận được Lệnh, chậm chuyến | Liên hệ IT gửi email ngay kèm đủ thông tin; app giữ phiên 30 ngày để ít phải đăng nhập lại |
| Nhiều lái xe dùng chung một tài khoản trên một điện thoại | thỉnh thoảng | Không biết ai làm gì trên Lệnh, chứng từ | Quy định mỗi người một tài khoản |

## 10. Success Criteria (preliminary)

- Ít nhất 80% yêu cầu quên mật khẩu của người có email tự xong, không cần bộ phận IT.
- Dưới 2 yêu cầu Liên hệ IT trên 100 người dùng mỗi tháng.
- Theo dõi số lần tạm khoá mỗi tuần để chỉnh `P-so-lan-sai-mat-khau` và `P-thoi-gian-tam-khoa`.
- Vào Home dưới 3 giây khi đã có phiên.

## 11. Open Questions

- [x] OQ-1: Link đặt lại mật khẩu trên web có hạn bao lâu, dùng một lần hay nhiều lần? — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (30/9/2026), UC01.02 Quên mật khẩu, trang 264 — Resolved 15/10 (qua /srs): 30 phút.
- [x] OQ-2: Địa chỉ email nhận yêu cầu Liên hệ IT của Delta là gì? — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Web) (30/9/2026), UC01.02 Quên mật khẩu, trang 263 — Resolved 15/10 (qua /srs): it@delta.com.vn.
- [x] OQ-3: Dòng hướng dẫn người chưa có tài khoản của Delta ghi nơi liên hệ nào? — Nguồn khách: Tài liệu SRS - ERP Delta 3.0 (Mobile) (5/10/2026), UC01.01.01 Đăng nhập, trang 46 — Resolved 15/10 (qua /srs): dùng câu mặc định sản phẩm "Chưa có tài khoản? Liên hệ quản trị viên.".

## 12. Next Steps

- `/srs account-access`
- `/user-flow account-access`
- `/figma-screen account-access`
