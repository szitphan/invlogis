---
type: brainstorm
feature: account-access
status: draft
status_changed: 2026-11-06
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-06
links:
  - docs/account-access/brainstorms/account-access.md
  - docs/account-access/srs/account-access-spec.md
  - docs/_product/tenant-parameters.md
  - docs/employee-records/brainstorms/employee-records.md
  - docs/access-control/brainstorms/access-control.md
  - docs-input/srs-cu/lg-srs-export.md
  - docs-input/sop/apas-thanh-toan-doi-soat/apas-thanh-toan-doi-soat.md
---

# Đăng nhập bằng Google và khoá truy cập khi nghỉ việc

## 1. Idea Seed

login bằng SSO (google)

## 2. Context

Sản phẩm đang chuyển thành SaaS bán cho nhiều doanh nghiệp, và phần lớn doanh nghiệp đã dùng một bộ tài khoản công ty (Google Workspace hoặc Microsoft 365). Delta, khách đầu tiên, mua **200 tài khoản Google Workspace Business Starter** cho nhân viên (tài liệu APAS, mục chi phí phần mềm), nên đăng nhập bằng tài khoản Google công ty giúp nhân viên bớt một mật khẩu phải nhớ và giúp khách quản lý truy cập ở một nơi.

Ý này mở lại quyết định "không làm SSO" ngày 15/10 (ISS-13). Đăng nhập Google chạy **song song** với mật khẩu, vì ở Delta có người có tài khoản Google, có người không (phần lớn lái xe không có email). Bật hay tắt tuỳ từng khách. Bản đầu chỉ làm Google; Microsoft để sau (G15).

Khi đã nối với tài khoản Google của khách, một yêu cầu đi kèm là **khoá hết truy cập khi nhân viên nghỉ việc**: duyệt đơn nghỉ việc thì tài khoản phần mềm bị vô hiệu hoá ngay, và tài khoản Google công ty bị tạm ngưng nếu khách bật. Khoá khi nghỉ việc chỉ áp cho tài khoản cá nhân của nhân viên; tài khoản Admin dùng chung và tài khoản đối tác cây dầu không nằm trong luồng này. Hai bên không đồng bộ danh sách người dùng với nhau; hệ thống chỉ so khớp lúc đăng nhập và chỉ gửi lệnh tạm ngưng khi có người nghỉ.

Mỗi khách có một app riêng trên kho ứng dụng, nên app không cần bước nhập mã công ty.

Feature liên quan: `account-access` (luồng đăng nhập chung, Mục 5.1 của [[docs/account-access/brainstorms/account-access.md|brainstorm đăng nhập]]), `employee-records` (hồ sơ nhân viên, đơn nghỉ việc), `access-control` (tài khoản, vô hiệu hoá, quyền), `cross-process-flow` (luồng Offboarding), `activity-log`, `notifications`.

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| Nhân viên nội bộ dùng web | Thêm một mật khẩu phải nhớ, quên thì chờ IT đặt lại | Vào phần mềm bằng tài khoản Google công ty đang dùng hằng ngày |
| Lái xe, nhân viên hiện trường dùng app | Ít đăng nhập nên hay quên mật khẩu | Một nút đăng nhập, không gõ mật khẩu trên điện thoại |
| Admin của khách | Phải cấp và thu hồi tài khoản ở nhiều nơi | Bật tính năng, khai tên miền, cấp quyền một lần |
| Người duyệt đơn nghỉ việc | Nhân viên đã nghỉ vẫn vào được phần mềm và email công ty | Duyệt nghỉ là khoá xong mọi truy cập |
| IT của khách | Không biết ai vừa nghỉ để khoá tài khoản Google | Được báo ngay khi hệ thống chưa khoá được |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| Nhân viên nội bộ dùng web | Đăng nhập bằng Google | mỗi ngày | cao | Không vào được thì ngừng việc cả ngày |
| Lái xe, nhân viên hiện trường | Đăng nhập bằng Google trên app | hiếm (app giữ phiên) | cao | Lúc cần đăng nhập thường là lúc đang nhận việc |
| Admin của khách | Bật tính năng, khai tên miền, cấp quyền Google | hiếm (lúc khởi tạo khách) | trung | Khai sai tên miền thì cả công ty bị từ chối |
| Người duyệt đơn nghỉ việc | Duyệt đơn, xem kết quả khoá | mỗi tuần | cao | Duyệt nhầm thì nhân viên mất ngay quyền vào phần mềm và email |
| IT của khách | Khoá tay hoặc mở khoá tài khoản Google | hiếm | cao | Chậm khoá thì người đã nghỉ còn đọc được email công ty |

Quy mô: Delta khoảng **200 người dùng** có tài khoản Google (tương đương số tài khoản đã mua).

## 4. Capabilities Breakdown

Nhãn nguồn: `[Mới]` là chức năng SRS cũ chưa có. Mỗi dòng ghi feature sẽ đặc tả khi khác `account-access`.

### P0 — must have

- G1 [Mới] [Lõi] [Cấu hình] — Nút "Đăng nhập bằng Google" trên màn đăng nhập web và app, chạy song song với đăng nhập mật khẩu. Hiện khi khách bật `P-dang-nhap-google` (Delta: bật). Bản đầu chỉ có Google.
- G2 [Mới] [Lõi] [Cấu hình] — Chỉ nhận tài khoản Google do công ty cấp. Đủ cả 4 điều kiện mới cho vào: (1) Google xác nhận đây là tài khoản thuộc một tổ chức Google Workspace, không phải Gmail cá nhân; (2) tên miền của tổ chức đó nằm trong `P-ten-mien-dang-nhap-google` (Delta: `delta.com.vn`); (3) Google xác nhận email đã được xác minh và email trùng email của tài khoản trong hệ thống; (4) tài khoản là nhân viên nội bộ gắn với hồ sơ nhân viên. Không suy công ty từ đuôi email.
- G3 [Mới] [Lõi] — Không tự tạo tài khoản khi đăng nhập Google. Email đúng công ty mà chưa có tài khoản thì từ chối, hướng dẫn liên hệ quản trị viên. Khách mới chưa có dữ liệu nhân viên thì Admin của khách tạo các tài khoản đầu tiên.
- G4 [Mới] [Lõi] — Chỉ tài khoản nhân viên nội bộ dùng được đăng nhập Google. Admin (tài khoản dùng chung) và tài khoản đối tác cây dầu không gắn với tài khoản Google, vẫn đăng nhập bằng mật khẩu.
- G5 [Mới] [Lõi] — Lần đầu đăng nhập Google thành công, hệ thống gắn tài khoản Google đó (theo mã định danh Google cấp, không theo email) vào tài khoản phần mềm. Các lần sau so theo tài khoản Google đã gắn. Một tài khoản Google khác dù cùng email (email bị xoá rồi tạo lại) thì bị từ chối; Admin gỡ tài khoản Google đã gắn ở `access-control` để người dùng gắn lại.
- G6 [Mới] [Lõi] — Qua đủ 4 điều kiện thì đi chung luồng kiểm trạng thái, quyền vào web/app, chọn chi nhánh như đăng nhập mật khẩu (A4, A6 của brainstorm đăng nhập). Tài khoản Chờ kích hoạt đăng nhập Google thành công thì chuyển Đang hoạt động, mật khẩu tạm hết hiệu lực. Tài khoản Tạm khoá do nhập sai mật khẩu vẫn vào được bằng Google; đăng nhập Google thành công thì mở Tạm khoá và đưa số lần sai mật khẩu về 0, như đăng nhập mật khẩu đúng. Quy tắc Tạm khoá chặn đăng nhập (BR-account-access-022) chỉ áp cho đăng nhập mật khẩu. Vô hiệu hoá thì chặn.
- G7 [Mới] [Lõi] — Ghi lịch sử hoạt động: đăng nhập thành công kèm cách đăng nhập (mật khẩu hay Google), bị từ chối đăng nhập Google kèm lý do, gắn và gỡ tài khoản Google. Không gửi email thông báo đăng nhập.
- G8 [Mới] [Lõi] — Tài khoản chưa tự tạo mật khẩu (mật khẩu tạm đã hết hiệu lực vì vào bằng Google) bấm Đổi mật khẩu thì báo chưa có mật khẩu, hướng dẫn dùng Quên mật khẩu để tạo.
- G9 [Mới] [Gói: Nhân sự] — Offboarding: duyệt đơn nghỉ việc thì nhân viên chuyển Đã nghỉ việc và tài khoản chuyển **Vô hiệu hoá ngay**: mọi phiên web và app kết thúc ở lần thao tác hoặc lần kết nối kế tiếp (FR-account-access-016), chặn đăng nhập mật khẩu, Google và Quên mật khẩu, ghi lịch sử. Không có tham số tắt. Đơn đang chờ duyệt hoặc bị từ chối thì tài khoản giữ nguyên. Đặc tả ở `employee-records` và `access-control`.
- G10 [Mới] [Lõi] [Cấu hình] — Tự tạm ngưng tài khoản Google công ty khi nhân viên nghỉ việc, bật theo khách `P-tu-khoa-google-khi-nghi-viec` (Delta: bật). Chỉ tạm ngưng, không bao giờ xoá. Khoá theo tài khoản Google đã gắn; chưa gắn mà email hồ sơ thuộc tên miền công ty thì khoá theo email đó; không có tài khoản Google nào thì bỏ qua phần khoá Google, không gửi email. Khoá lỗi thì báo IT qua `P-email-it-khoa-tai-khoan` (Delta: it@delta.com.vn) và hồ sơ nhân viên có nút "Thử khoá lại"; hệ thống không tự thử lại. Khách tắt tự khoá thì hệ thống chỉ gửi email báo IT khoá tay.
- G11 [Mới] [Lõi] — Khách không dùng Gói Nhân sự: Admin vô hiệu hoá tài khoản bằng tay ở `access-control`; nếu khách bật `P-tu-khoa-google-khi-nghi-viec` thì thao tác này cũng tạm ngưng tài khoản Google, cùng cách báo lỗi như G10.
- G12 [Mới] [Lõi] — Nhân viên quay lại làm: hồ sơ còn Đã nghỉ việc thì không kích hoạt lại tài khoản được; HR chuyển hồ sơ về đang làm rồi Admin mới kích hoạt lại. Kích hoạt lại thì tài khoản về Chờ kích hoạt kèm mật khẩu tạm mới; đăng nhập Google đưa về Đang hoạt động. Trạng thái khoá Google trên hồ sơ về Chưa khoá. Hệ thống không tự mở khoá Google, IT tự mở trên Google. Cùng tài khoản Google cũ thì đăng nhập lại được, không cần gắn lại. Khách không có Gói Nhân sự thì Admin kích hoạt lại trực tiếp.
- G13 [Mới] [Lõi] — Màn cài đặt của Admin khách: bật/tắt đăng nhập Google, khai danh sách tên miền, cấp quyền cho hệ thống tạm ngưng tài khoản Google, bật/tắt tự khoá. Đổi cài đặt được ghi lịch sử.
- G14 [Mới] [Lõi] — Mỗi khách một app trên kho ứng dụng, nên app bỏ bước nhập mã công ty; app biết khách từ chính bản app. Sửa tài liệu đăng nhập theo BL-160.

### P1 — should have

- (không có)

### P2 — nice to have

- G15 [Mới] [Lõi] [Cấu hình] — Đăng nhập bằng Microsoft cho khách dùng Microsoft 365, cùng 4 điều kiện và cùng luồng như Google.

### Bỏ hoặc chuyển

| Chức năng | Quyết định | Lý do |
|---|---|---|
| Đăng nhập Google thay hẳn mật khẩu | Bỏ | Có nhân viên không có tài khoản Google, chặn mật khẩu thì họ không vào được |
| Đồng bộ danh sách người dùng giữa Google và hệ thống | Bỏ | Chưa thấy giải quyết thêm vấn đề gì, để hai bên độc lập cho đơn giản |
| Tự tạo tài khoản khi đăng nhập Google lần đầu | Bỏ, thay bằng G3 | Tài khoản phải gắn với hồ sơ nhân viên và do khách cấp |
| Nhận cả Gmail cá nhân | Bỏ, thay bằng G2 | Chỉ tài khoản công ty cấp mới thu hồi được khi nghỉ việc |
| Xoá tài khoản Google khi nghỉ việc | Bỏ, thay bằng tạm ngưng (G10) | Xoá thì mất dữ liệu và không quay lại được nếu duyệt nhầm |
| Tự mở khoá Google khi nhân viên quay lại | Bỏ, thay bằng G12 | Tài khoản Google do IT của khách quản lý |

### Chuyển sang feature khác

| Việc | Feature |
|---|---|
| Duyệt đơn nghỉ việc kích hoạt Offboarding (G9); popup xác nhận và toast kết quả khoá | `employee-records` |
| Trạng thái khoá Google trên hồ sơ nhân viên, nút "Thử khoá lại" và "IT đã khoá tay"; khoá nút kích hoạt lại khi hồ sơ còn Đã nghỉ việc | `employee-records` |
| Cho phép email trùng với hồ sơ đã nghỉ việc, để người mới dùng lại email cũ | `employee-records` |
| Cảnh báo khi nhập email không thuộc tên miền công ty vào hồ sơ | `employee-records` |
| Bỏ bắt buộc email trong hồ sơ nhân viên (phần lớn lái xe không có email) | `employee-records` |
| Gỡ tài khoản Google đã gắn; vô hiệu hoá tay cũng tạm ngưng Google (G11) | `access-control` |
| 3 quyền mới: cài đặt đăng nhập Google, gỡ tài khoản Google đã gắn, "Thử khoá lại" và "IT đã khoá tay" | `access-control` |
| Luồng Offboarding | `cross-process-flow` |

## 5. Core Flows (Happy Path)

### 5.1 Đăng nhập bằng Google

1. Người dùng bấm "Đăng nhập bằng Google" trên màn đăng nhập (web) hoặc màn mở đầu (app).
2. Google hiện màn chọn tài khoản; người dùng chọn tài khoản công ty và xác nhận trên Google.
3. Hệ thống kiểm 4 điều kiện của G2, rồi kiểm tài khoản Google đã gắn (G5).
4. Đạt: đi tiếp luồng kiểm trạng thái, quyền vào web/app, chọn chi nhánh như đăng nhập mật khẩu.
5. Vào màn Home; lịch sử ghi "Đăng nhập bằng Google".

```
┌──────────────────────────┐
│ Bấm "Đăng nhập bằng       │
│ Google"                  │
└────────────┬─────────────┘
             ▼
┌──────────────────────────┐   Huỷ trên Google
│ Google: chọn tài khoản    ├──────────────────► Về màn đăng nhập, không báo lỗi
└────────────┬─────────────┘
             │ Google lỗi / mất mạng ─────────► "Chưa kết nối được Google…"
             │ IT khách chặn ứng dụng (D1b) ──► "Công ty của bạn chưa cho phép…"
             ▼
      ◇ D1 Tài khoản tổ chức,       KHÔNG
        đúng tên miền khách? ─────────────────► "Chỉ dùng được tài khoản Google do {tên công ty} cấp."
             │ CÓ
             ▼
      ◇ D2 Có tài khoản cùng        KHÔNG
        email trong khách? ───────────────────► "Email {email} chưa có tài khoản…"
             │ CÓ
             ▼
      ◇ D3 Là nhân viên nội bộ?     KHÔNG
             ├────────────────────────────────► "Tài khoản này không dùng được đăng nhập Google…"
             │ CÓ
             ▼
      ◇ D4 Đã gắn tài khoản Google? ── CHƯA ──► Gắn tài khoản Google này (5.2)
             │ RỒI                                   │
             ▼                                       │
      ◇ D5 Trùng tài khoản đã gắn?  KHÔNG            │
             ├────────────────────────────────► "Tài khoản Google này không khớp…"
             │ CÓ                                    │
             ▼◄──────────────────────────────────────┘
┌──────────────────────────────────────────────┐
│ Luồng chung: trạng thái (D6), quyền web/app, │
│ chọn chi nhánh — như đăng nhập mật khẩu       │
└────────────┬─────────────────────────────────┘
             ▼
        Màn Home + ghi lịch sử
```

### 5.2 Lần đầu gắn tài khoản Google

1. Người dùng đăng nhập Google lần đầu, đạt D1–D3.
2. Hệ thống gắn tài khoản Google vào tài khoản phần mềm, ghi lịch sử "Gắn tài khoản Google".
3. Tài khoản đang Chờ kích hoạt thì chuyển Đang hoạt động, mật khẩu tạm hết hiệu lực.
4. Đi tiếp luồng chung như 5.1 bước 4.

### 5.3 Offboarding — khoá truy cập khi nghỉ việc

1. Người duyệt mở đơn nghỉ việc ở `employee-records`, bấm Duyệt (thường đúng ngày nghỉ thực tế).
2. Popup xác nhận nêu rõ những gì sẽ bị khoá; người duyệt xác nhận.
3. Nhân viên chuyển Đã nghỉ việc; tài khoản chuyển Vô hiệu hoá; mọi phiên web và app kết thúc ở lần thao tác hoặc lần kết nối kế tiếp.
4. Nhân viên có tài khoản Google và khách bật tự khoá: hệ thống gửi lệnh tạm ngưng tài khoản Google tới Google. Không có tài khoản Google thì dừng ở bước 3.
5. Kết quả hiện toast cho người duyệt và ghi trên hồ sơ nhân viên; khoá lỗi hoặc khách tắt tự khoá thì gửi email báo IT.

```
┌───────────────────┐   ┌────────────────────┐   ┌──────────────────────────┐
│ Người duyệt bấm    ├──►│ Popup xác nhận      ├──►│ Nhân viên: Đã nghỉ việc   │
│ Duyệt đơn nghỉ     │   │ (Huỷ → giữ nguyên)  │   │ Tài khoản: Vô hiệu hoá    │
└───────────────────┘   └────────────────────┘   │ Kết thúc mọi phiên        │
                                                  └────────────┬─────────────┘
                                                               ▼
                                          ◇ D7a Có tài khoản Google? ── KHÔNG ──► Hồ sơ: Không có tài khoản Google
                                                               │ CÓ
                                                               ▼
                                          ◇ D7 Khách bật tự khoá Google?
                                       KHÔNG │                     │ CÓ
                                             ▼                     ▼
                              ┌────────────────────┐   ┌──────────────────────┐
                              │ Email IT: khoá tay  │   │ Gửi lệnh tạm ngưng    │
                              │ Toast "…Đã báo IT   │   │ tới Google            │
                              │ khoá Google."       │   └──────────┬───────────┘
                              └────────────────────┘              ▼
                                                     ◇ D8 Google khoá thành công?
                                                   CÓ │                    │ KHÔNG
                                                      ▼                    ▼
                                   ┌──────────────────────┐  ┌──────────────────────────┐
                                   │ Hồ sơ: Đã khoá Google │  │ Hồ sơ: Khoá lỗi           │
                                   │ Toast "…Đã khoá tài   │  │ Email IT + nút "Thử khoá  │
                                   │ khoản phần mềm và     │  │ lại"; Toast "…Chưa khoá   │
                                   │ Google."              │  │ được Google, đã báo IT."  │
                                   └──────────────────────┘  └──────────────────────────┘
```

### 5.4 Nhân viên quay lại làm

1. HR chuyển hồ sơ từ Đã nghỉ việc về đang làm ở `employee-records`; trước bước này nút kích hoạt lại bị khoá.
2. Admin kích hoạt lại tài khoản phần mềm ở `access-control`; tài khoản về Chờ kích hoạt kèm mật khẩu tạm mới, trạng thái khoá Google về Chưa khoá.
3. IT mở khoá tài khoản Google trên Google.
4. Nhân viên đăng nhập Google như thường; cùng tài khoản Google cũ nên không cần gắn lại.

### 5.5 Admin cài đặt đăng nhập Google

1. Admin khách mở cài đặt đăng nhập, khai tên miền công ty (Delta: `delta.com.vn`).
2. Bật đăng nhập Google; nút hiện ngay trên màn đăng nhập của khách.
3. Muốn tự khoá khi nghỉ việc: Admin bấm cấp quyền, IT của khách (quản trị Google Workspace) đồng ý trên Google; cấp thành công thì mới bật được tự khoá.
4. Mỗi lần đổi cài đặt được ghi lịch sử.

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| D1 | 5.1 | Tài khoản Google thuộc tổ chức Workspace và tên miền nằm trong `P-ten-mien-dang-nhap-google`? | Kiểm D2 | Từ chối, câu "Chỉ dùng được tài khoản Google do {tên công ty} cấp." |
| D1b | 5.1 | IT của khách cho phép ứng dụng trên Google Workspace? | Kiểm D1 | Từ chối, câu "Công ty của bạn chưa cho phép…" |
| D2 | 5.1 | Email đã xác minh và có tài khoản cùng email trong khách? | Kiểm D3 | Từ chối, câu "Email {email} chưa có tài khoản…" |
| D3 | 5.1 | Tài khoản là nhân viên nội bộ gắn hồ sơ nhân viên? | Kiểm D4 | Từ chối, hướng dẫn đăng nhập bằng mật khẩu |
| D4 | 5.1 | Tài khoản đã gắn tài khoản Google? | Kiểm D5 | Gắn tài khoản Google này (5.2) |
| D5 | 5.1 | Tài khoản Google đang dùng trùng tài khoản đã gắn? | Luồng chung | Từ chối, liên hệ quản trị viên gỡ gắn |
| D6 | 5.1 | Trạng thái tài khoản cho phép đăng nhập Google? (6.2) | Kiểm quyền, chi nhánh | Vô hiệu hoá: câu E-account-access-003 |
| D7a | 5.3 | Nhân viên có tài khoản Google (đã gắn, hoặc email hồ sơ thuộc `P-ten-mien-dang-nhap-google`)? | Kiểm D7 | Bỏ qua khoá Google, không email; hồ sơ ghi Không có tài khoản Google |
| D7 | 5.3 | Khách bật `P-tu-khoa-google-khi-nghi-viec`? | Gửi lệnh tạm ngưng | Email IT khoá tay; hồ sơ ghi Chờ IT khoá tay |
| D8 | 5.3 | Google tạm ngưng thành công? | Hồ sơ ghi Đã khoá Google | Hồ sơ ghi Khoá lỗi, email IT, nút "Thử khoá lại" |
| D9 | 5.5 | Bật đăng nhập Google mà danh sách tên miền có ít nhất 1 tên miền? | Lưu | Không cho lưu, báo cần khai tên miền |
| D10 | 5.5 | Bật tự khoá mà quyền Google đã cấp thành công? | Lưu | Không cho bật, hướng dẫn cấp quyền trước |
| D11 | 5.4 | Hồ sơ nhân viên còn Đã nghỉ việc (khách có Gói Nhân sự)? | Khoá nút kích hoạt lại | Admin kích hoạt lại |

### 6.2 Scenario Matrix

Trạng thái tài khoản × cách đăng nhập:

| Trạng thái tài khoản | Đăng nhập mật khẩu | Đăng nhập Google | Ghi chú |
|---|---|---|---|
| Chờ kích hoạt | Mật khẩu tạm, phải tạo mật khẩu mới | Vào được dù mật khẩu tạm còn hạn hay đã hết hạn; chuyển Đang hoạt động, mật khẩu tạm hết hiệu lực | G6 |
| Đang hoạt động | Vào được | Vào được | — |
| Tạm khoá (sai mật khẩu) | Chặn tới khi tự mở sau `P-thoi-gian-tam-khoa` (Delta: 30 phút) | Vào được, mở Tạm khoá, số lần sai về 0 | Tạm khoá chỉ chặn mật khẩu (G6) |
| Vô hiệu hoá (Admin hoặc nghỉ việc) | Chặn | Chặn | E-account-access-003 |

Loại tài khoản × đăng nhập Google:

| Loại tài khoản | Đăng nhập Google |
|---|---|
| Nhân viên nội bộ có email công ty | Dùng được |
| Nhân viên nội bộ chưa có email hoặc email cá nhân | Không, dùng mật khẩu |
| Admin (tài khoản dùng chung) | Không |
| Nhân viên đối tác cây dầu | Không |

Trạng thái đơn nghỉ việc × tài khoản:

| Đơn nghỉ việc | Tài khoản phần mềm | Tài khoản Google |
|---|---|---|
| Chờ duyệt | Giữ nguyên | Giữ nguyên |
| Bị từ chối | Giữ nguyên | Giữ nguyên |
| Đã duyệt, không có tài khoản Google | Vô hiệu hoá ngay | Không áp dụng |
| Đã duyệt, khách bật tự khoá | Vô hiệu hoá ngay | Tạm ngưng (lỗi thì báo IT) |
| Đã duyệt, khách tắt tự khoá | Vô hiệu hoá ngay | Giữ nguyên, email IT khoá tay |

### 6.3 State Transitions

Trạng thái tài khoản dùng chung với brainstorm đăng nhập (Mục 6.3); đăng nhập Google thêm 1 chuyển và Offboarding thêm 1 nguồn vào Vô hiệu hoá:

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Tài khoản | Chờ kích hoạt | Đang hoạt động | Đăng nhập Google thành công lần đầu | có, Admin đặt lại mật khẩu |
| Tài khoản | Đang hoạt động, Tạm khoá, Chờ kích hoạt | Vô hiệu hoá | Duyệt đơn nghỉ việc, hoặc Admin vô hiệu hoá tay | có, Admin kích hoạt lại |

Trạng thái khoá Google trên hồ sơ nhân viên:

```
Chưa khoá ──(duyệt nghỉ, có TK Google, khách bật tự khoá)──► Đang khoá ──► Đã khoá
    │                                                            └──────► Khoá lỗi ──(Thử khoá lại)──► Đang khoá
    │                                                                        └──(IT đã khoá tay)──► Đã khoá
    ├──(duyệt nghỉ, khách tắt tự khoá)──► Chờ IT khoá tay ──(IT đã khoá tay)──► Đã khoá
    └──(duyệt nghỉ, không có TK Google)──► Không có tài khoản Google
Mọi trạng thái ──(Admin kích hoạt lại tài khoản)──► Chưa khoá
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| Khoá Google | Chưa khoá | Đang khoá | Duyệt nghỉ hoặc vô hiệu hoá tay; có tài khoản Google; khách bật tự khoá | không |
| Khoá Google | Chưa khoá | Chờ IT khoá tay | Duyệt nghỉ hoặc vô hiệu hoá tay; khách tắt tự khoá | có, IT đã khoá tay |
| Khoá Google | Chưa khoá | Không có tài khoản Google | Duyệt nghỉ hoặc vô hiệu hoá tay; không có tài khoản Google | — |
| Khoá Google | Đang khoá | Đã khoá | Google xác nhận tạm ngưng | — |
| Khoá Google | Đang khoá | Khoá lỗi | Google từ chối hoặc không phản hồi | có, "Thử khoá lại" |
| Khoá Google | Khoá lỗi | Đang khoá | Bấm "Thử khoá lại" | — |
| Khoá Google | Khoá lỗi, Chờ IT khoá tay | Đã khoá | Người có quyền bấm "IT đã khoá tay" | — |
| Khoá Google | Mọi trạng thái | Chưa khoá | Admin kích hoạt lại tài khoản; nút "Thử khoá lại" ẩn | — |

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Đóng trình duyệt hoặc app giữa màn Google | Chưa có phiên, chưa ghi gì | Bấm lại "Đăng nhập bằng Google" | Không có |
| Bấm Huỷ trên màn Google | Chưa có phiên | Về màn đăng nhập, không báo lỗi | Không có |
| Google lỗi hoặc mất mạng khi đăng nhập | Chưa có phiên | Thử lại hoặc đăng nhập bằng mật khẩu | Không có |
| IT của khách chặn ứng dụng trên Google Workspace | Chưa có phiên | Liên hệ quản trị viên | Không có |
| Google không phản hồi khi tạm ngưng | Tài khoản phần mềm đã Vô hiệu hoá; khoá Google ở Khoá lỗi | IT khoá tay hoặc bấm "Thử khoá lại" | Email IT |
| Khách tắt `P-dang-nhap-google` khi người dùng đang trong phiên | Phiên giữ tới khi hết hạn hoặc đăng xuất | Lần sau đăng nhập bằng mật khẩu | Nút Google ẩn ngay |
| Hai người cùng duyệt một đơn nghỉ việc | Chỉ lần duyệt đầu có hiệu lực | Người sau thấy đơn đã duyệt | Chỉ gửi một lệnh tạm ngưng |

### 6.5 Other Edge Cases

- Lần bị từ chối đăng nhập Google không tính vào bộ đếm `P-so-lan-sai-mat-khau`; mỗi lần từ chối chỉ ghi lịch sử kèm lý do.
- Ghi nhớ đăng nhập trên web và giữ phiên trên app áp như đăng nhập mật khẩu (A8 của brainstorm đăng nhập).
- Đăng xuất khỏi phần mềm không đăng xuất khỏi Google.
- App đang mất mạng khi tài khoản bị vô hiệu hoá: người dùng còn xem được dữ liệu đã lưu trên máy (GR-25) tới khi app có mạng lại; lúc đó phiên kết thúc.
- Email bị xoá rồi tạo lại giống hệt là một tài khoản Google mới (mã định danh khác), nên bị từ chối ở D5 tới khi Admin gỡ gắn.
- Người mới được cấp lại email của người đã nghỉ: cần tài khoản phần mềm riêng gắn hồ sơ riêng; hồ sơ được trùng email với hồ sơ đã nghỉ việc (`employee-records`).
- Tài khoản chỉ dùng Google vẫn dùng được Quên mật khẩu để tạo mật khẩu, nếu có email đăng ký.
- Khách đổi danh sách tên miền: tài khoản đã gắn mà tên miền bị bỏ thì bị từ chối ở D1 từ lần đăng nhập sau.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Danh sách tên miền | Bắt buộc ít nhất 1 khi bật đăng nhập Google; mỗi dòng đúng dạng tên miền, không có `@`, không trùng |
| Bật đăng nhập Google | Chỉ lưu được khi có ít nhất 1 tên miền |
| Bật tự khoá Google | Chỉ bật được khi quyền Google đã cấp thành công |
| Email tài khoản dùng đăng nhập Google | Trùng email Google trả về (không phân biệt hoa thường), đã được Google xác minh |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Bật đăng nhập Google | `P-dang-nhap-google` (Delta: bật) | theo khách | Tắt thì ẩn nút, phiên đang mở giữ nguyên |
| Tên miền được nhận | `P-ten-mien-dang-nhap-google` (Delta: `delta.com.vn`) | theo khách | Ngoài danh sách thì từ chối ở D1 |
| Tự khoá Google khi nghỉ việc | `P-tu-khoa-google-khi-nghi-viec` (Delta: bật) | theo khách | Tắt thì chỉ email IT |
| Email IT nhận báo khoá | `P-email-it-khoa-tai-khoan` (Delta: it@delta.com.vn) | theo khách | Trống thì dùng địa chỉ hỗ trợ mật khẩu |
| Số lần thử đăng nhập Google | Không giới hạn trong hệ thống | — | Google tự chặn dò mật khẩu phía Google |
| Tự thử lại khi khoá Google lỗi | Không tự thử lại | — | Báo IT ngay, có nút "Thử khoá lại" |

### 7.3 Wording samples (exact strings)

Nhãn nút: "Đăng nhập bằng Google".

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Gmail cá nhân, hoặc tài khoản Google của công ty khác | "Chỉ dùng được tài khoản Google do {tên công ty} cấp." | E-account-access-019 |
| Đúng công ty, chưa có tài khoản | "Email {email} chưa có tài khoản trong hệ thống. Liên hệ quản trị viên để được cấp." | E-account-access-020 |
| Email trùng tài khoản Admin hoặc đối tác cây dầu | "Tài khoản này không dùng được đăng nhập Google. Đăng nhập bằng mật khẩu." | E-account-access-021 |
| Khác tài khoản Google đã gắn | "Tài khoản Google này không khớp với tài khoản đã gắn. Liên hệ quản trị viên." | E-account-access-022 |
| Google lỗi | "Chưa kết nối được Google. Thử lại hoặc đăng nhập bằng mật khẩu." | E-account-access-023 |
| IT của khách chặn ứng dụng trên Google Workspace | "Công ty của bạn chưa cho phép đăng nhập Google vào ứng dụng này. Liên hệ quản trị viên." | E-account-access-024 |
| Tài khoản chưa có mật khẩu bấm Đổi mật khẩu | "Tài khoản của bạn chưa có mật khẩu. Dùng Quên mật khẩu để tạo." | E-account-access-025 |
| Bật đăng nhập Google khi chưa khai tên miền (D9) | "Thêm ít nhất một tên miền công ty để bật đăng nhập Google." | E-account-access-026 |
| Bật tự khoá khi chưa cấp quyền Google (D10) | "Cấp quyền Google trước khi bật tự khoá." | E-account-access-027 |
| Cấp quyền Google không thành công | "Chưa cấp được quyền. Người cấp phải là quản trị viên Google Workspace của công ty." | E-account-access-028 |
| "Thử khoá lại" vẫn lỗi | "Chưa khoá được tài khoản Google. Đã báo IT." | E-account-access-029 |
| Vô hiệu hoá | Dùng lại câu hiện có | E-account-access-003 |
| Chưa được cấp chi nhánh | Dùng lại câu hiện có | E-account-access-004 |
| Không có quyền vào web hoặc app | Dùng lại câu hiện có | E-account-access-005 |
| Mất mạng | Dùng lại câu hiện có | E-common-009 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Duyệt nghỉ, khoá được cả hai | "Đã duyệt nghỉ việc. Đã khoá tài khoản phần mềm và Google." |
| Duyệt nghỉ, khoá Google lỗi | "Đã duyệt nghỉ việc và khoá tài khoản phần mềm. Chưa khoá được Google, đã báo IT." |
| Duyệt nghỉ, khách tắt tự khoá | "Đã duyệt nghỉ việc và khoá tài khoản phần mềm. Đã báo IT khoá Google." |
| "Thử khoá lại" thành công | "Đã khoá tài khoản Google." |
| Cấp quyền Google thành công | "Đã cấp quyền. Bạn có thể bật tự khoá Google khi nghỉ việc." |
| Gỡ tài khoản Google đã gắn | "Đã gỡ tài khoản Google. Người dùng gắn lại ở lần đăng nhập Google kế tiếp." |

#### Confirm messages

| Tình huống | Wording |
|---|---|
| Popup duyệt nghỉ, khách bật tự khoá | "Tài khoản phần mềm và tài khoản Google {email} của {họ tên} sẽ bị khoá ngay." |
| Popup duyệt nghỉ, khách tắt tự khoá | "Tài khoản phần mềm của {họ tên} sẽ bị khoá ngay." |
| Popup gỡ tài khoản Google đã gắn | "Gỡ tài khoản Google {email} khỏi tài khoản của {họ tên}? Người dùng sẽ gắn lại ở lần đăng nhập Google kế tiếp." |

#### Email gửi IT

Gửi tới `P-email-it-khoa-tai-khoan` (Delta: it@delta.com.vn).

> **Tiêu đề:** Khoá tài khoản Google của {họ tên}
> **Nội dung:** {họ tên} ({email}) đã nghỉ việc từ {ngày giờ duyệt}. Tài khoản phần mềm đã khoá. {Hệ thống chưa khoá được tài khoản Google | Khách chưa bật tự khoá}, cần IT khoá trên Google.

### 7.4 Bối cảnh hệ thống

Thông tin nghiệp vụ cần lưu thêm:

| Ở đâu | Thông tin | Khi nào ghi |
|---|---|---|
| Tài khoản | Tài khoản Google đã gắn (mã Google cấp), ngày gắn | Lần đầu đăng nhập Google thành công |
| Tài khoản | Đã tự tạo mật khẩu hay chưa | Để chặn Đổi mật khẩu (G8) |
| Hồ sơ nhân viên | Trạng thái khoá Google và thời điểm (6.3) | Khi duyệt nghỉ, vô hiệu hoá tay, thử khoá lại, kích hoạt lại |
| Cấu hình khách | 4 tham số `P-dang-nhap-google`, `P-ten-mien-dang-nhap-google`, `P-tu-khoa-google-khi-nghi-viec`, `P-email-it-khoa-tai-khoan`; quyền Google đã cấp hay chưa | Khi Admin cài đặt |

Dùng chung:

| Nhóm | Feature chung | Feature này cần | Trạng thái |
|---|---|---|---|
| Liên quy trình | `cross-process-flow` | Luồng **Offboarding**: đơn nghỉ việc (`employee-records`) → duyệt → tài khoản Vô hiệu hoá (`access-control`) → tạm ngưng Google; bước sau: email IT; nhân viên quay lại thì HR cập nhật hồ sơ, Admin kích hoạt lại, IT mở khoá Google | đề xuất |
| Thông báo | `notifications` | Email IT (`P-email-it-khoa-tai-khoan`) khi khoá Google lỗi, khi khách tắt tự khoá; toast kết quả cho người duyệt. Email IT đi kênh email riêng, không qua chuông trong app vì IT có thể không dùng phần mềm | đề xuất |
| Lịch sử hoạt động | `activity-log` | Đăng nhập kèm cách đăng nhập; từ chối đăng nhập Google kèm lý do; gắn, gỡ tài khoản Google; tự vô hiệu hoá do nghỉ việc; khoá Google thành công, lỗi, thử khoá lại, IT đã khoá tay; đổi 4 tham số. Ai xem: Admin và người có quyền xem lịch sử tài khoản | đề xuất |
| Quyền | `access-control` | Cài đặt đăng nhập Google (Admin khách); gỡ tài khoản Google đã gắn (Admin, người quản lý tài khoản); "Thử khoá lại" và "IT đã khoá tay" (người duyệt nghỉ việc, Admin) | đề xuất |
| Danh mục | `employee-records` | Chỉ đọc email và trạng thái nghỉ việc của hồ sơ nhân viên | đề xuất |
| Ảnh/tài liệu, Bình luận, Thao tác chung | — | Không dùng: không có tệp, không có bản ghi cần trao đổi, không lưu nháp, nhập, xuất | — |

## 8. Assumptions

- Ba giả định về Google và IT Delta dưới đây được kiểm bằng tài khoản Google thật của Delta khi làm; tài liệu coi là đúng tới lúc đó.
- Google trả về thông tin tổ chức Workspace, email đã xác minh và mã định danh không dùng lại cho mọi tài khoản Workspace, kể cả gói Business Starter của Delta.
- Google cho phần mềm tạm ngưng và mở lại tài khoản người dùng khi quản trị viên Workspace của khách cấp quyền.
- IT Delta là người quản trị Google Workspace của Delta và đồng ý cấp quyền tạm ngưng cho hệ thống.
- HR duyệt đơn nghỉ việc đúng ngày nhân viên nghỉ thực tế, nên khoá ngay khi duyệt là đúng thời điểm.
- Mỗi khách có một app riêng trên App Store và Google Play.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| Apple từ chối duyệt app riêng cho từng khách, vì app chỉ dành cho nhân viên một công ty mà phát hành công khai | thỉnh thoảng | Chậm ra mắt app cho khách mới | Kiểm hướng dẫn duyệt của Apple trước khi làm app khách thứ hai; chuẩn bị tài khoản thử cho người duyệt |
| Mỗi khách một app nên mỗi lần phát hành phải làm nhiều bản | thường | Tốn công vận hành, khách nhận bản mới chậm hơn | Đưa vào kế hoạch phát hành |
| IT của khách không cấp quyền tạm ngưng tài khoản Google | thỉnh thoảng | Không tự khoá được, quay về IT khoá tay | Tham số tắt tự khoá; hệ thống vẫn email IT |
| Duyệt nhầm đơn nghỉ việc | hiếm | Nhân viên mất ngay quyền vào phần mềm và email công ty | Popup ghi rõ tên và email; Admin kích hoạt lại, IT mở khoá Google |
| Gói Business Starter của Delta xử lý khác tài liệu Google (khoá, chặn ứng dụng) | hiếm | Chức năng chạy sai với khách đầu tiên | Thử bằng tài khoản Delta thật khi làm |
| Hồ sơ nhân viên ghi email cá nhân hoặc email cũ | thường | Bấm đăng nhập Google bị từ chối, sinh yêu cầu hỗ trợ | Cảnh báo khi nhập email ngoài tên miền công ty (`employee-records`) |
| Tạm ngưng tài khoản Google làm người nghỉ mất email và dữ liệu công việc chưa bàn giao | thỉnh thoảng | Tranh chấp với người lao động, mất dữ liệu cần bàn giao | Chỉ tạm ngưng, không xoá; IT tự bàn giao dữ liệu trên Google trước khi xoá hẳn |
| Google đổi cách tích hợp hoặc chính sách | hiếm | Đăng nhập Google hoặc tự khoá ngừng chạy với mọi khách | Đăng nhập mật khẩu luôn còn; tự khoá lỗi thì báo IT |
| Người đã nghỉ biết mật khẩu tài khoản Admin dùng chung | thỉnh thoảng | Người đã nghỉ vẫn vào được phần mềm, trái lời hứa "khoá hết khi nghỉ" | Ghi rõ luồng khoá không áp cho tài khoản dùng chung; khuyến nghị khách đổi mật khẩu Admin khi người biết mật khẩu nghỉ |

## 10. Success Criteria (preliminary)

Mốc so sánh lấy ở tháng trước khi bật tại Delta; số liệu lấy từ lịch sử hoạt động của hệ thống và hộp thư IT Delta.

- Sau 1 tháng chạy ở Delta, ít nhất 60% lượt đăng nhập web và 40% lượt đăng nhập app của nhân viên có tài khoản Google là đăng nhập bằng Google.
- Yêu cầu "Quên mật khẩu, liên hệ IT" của Delta giảm ít nhất 50% so với tháng mốc.
- 100% nhân viên được duyệt nghỉ việc có tài khoản ở trạng thái Vô hiệu hoá trong vòng 1 phút sau khi duyệt.
- Ít nhất 95% lệnh tự khoá Google thành công ngay lần đầu; 100% trường hợp khoá lỗi có email tới IT.

## 11. Open Questions

| # | Câu hỏi | Trả lời | Nguồn khách |
|---|---|---|---|
| OQ-1 | Delta có bao nhiêu nhân viên dùng đăng nhập Google? | ✅ Khoảng 200, bằng số tài khoản Google đã mua | Tài liệu APAS thanh toán, đối soát, mục chi phí phần mềm |
| OQ-2 | Khách mới chưa có dữ liệu nhân viên thì ai tạo tài khoản đầu tiên? | ✅ Admin của khách tạo các tài khoản tiếp theo | chưa có trong tài liệu khách gửi |
| OQ-3 | Hồ sơ nhân viên có còn bắt buộc email không, khi phần lớn lái xe không có email? | ✅ Bỏ bắt buộc, chuyển `employee-records` | SRS LG v2.0, UC02.01 Hồ sơ nhân viên |
| OQ-4 | App của từng khách phát hành công khai hay nội bộ? | ✅ Công khai trên kho ứng dụng | chưa có trong tài liệu khách gửi |

## 12. Next Steps

- `/srs account-access` — thêm FR, BR, mã lỗi cho đăng nhập Google; bỏ mã công ty trên app theo BL-160.
- `/brainstorm employee-records` — Offboarding, trạng thái khoá Google, email không bắt buộc.
- `/brainstorm access-control` — gỡ tài khoản Google, vô hiệu hoá tay kèm khoá Google, 3 quyền mới.
