---
type: research
keyword: "Fleetio: bản đồ đội xe, địa điểm, vùng địa lý, gán xe vào việc"
status: draft
status_changed: 2026-11-03
status_reason: "đã review upstream, không cần sửa"
updated: 2026-11-03
links:
  - docs/_product/prd.md
  - docs/vehicle-telematics/brainstorms/vehicle-telematics.md
  - docs/_research/2026-11-02-fleetio-app-teardown.md
  - docs/_research/fleetio/run-notes/location-dispatch.md
---

# Giải pháp tham khảo: Bản đồ, địa điểm, vùng địa lý và gán việc

> Khuyến nghị: **Tham khảo bố cục bản đồ, mô hình độ tươi vị trí và cách lấy vị trí từ hoạt động.** Không dùng Jobs làm mẫu điều vận. Đã thấy marker thật bằng vị trí giả lập; marker của Fleetio báo độ tươi dữ liệu, không báo xe chạy hay dừng, nên BL-382 chỉ học được một phần. Phiếu dựa vào toạ độ trình duyệt không chống được kiểm khống trên web. Phiếu dầu, phiếu dịch vụ có nhà cung cấp tạo vị trí xe từ địa chỉ khai mà không báo, địa chỉ sai có thể đẩy xe sang nước khác: đáng học cách lấy vị trí không cần thiết bị, nhưng phải ghi rõ đây là vị trí khai và kiểm địa chỉ.

## 1. Idea Seed

Một bản đồ gom xe, địa điểm, nhà cung cấp và xưởng, cạnh danh sách gần vị trí đang xem. Vị trí xe đến từ thiết bị hoặc từ chính hoạt động trên app: phiếu kiểm mang vị trí trình duyệt hay điện thoại, phiếu dầu, phiếu dịch vụ mang địa chỉ nhà cung cấp. Mỗi lần có vị trí mới, hệ thống đối chiếu với vùng của các địa điểm: sinh sự kiện vào, ra vùng; sự kiện này tự gán, tự kết thúc gán xe vào việc và kích hoạt Automation.

## 2. Context

**Feature Invlogis liên quan:** `vehicle-telematics`, `location-catalog`, `transport-dispatch` (#12), BL-382 (marker Phương tiện).

**Nguồn và bằng chứng:** xem trực tiếp ngày 2026-11-02, chạy thật ngày 2026-11-03 trên tài khoản dùng thử bằng dữ liệu TEST ([[docs/_research/fleetio/run-notes/location-dispatch.md|ghi chú chạy thử]]). Tài khoản không có thiết bị định vị; kết quả về marker và sự kiện vùng phần lớn dùng vị trí giả lập gửi qua phiếu kiểm tra web, chưa kiểm với thiết bị thật. Vị trí từ phiếu dầu, phiếu dịch vụ có nhà cung cấp là dữ liệu chạy thật. Fleetio Go mới kiểm một phiếu không vi phạm. Lượt 3, lượt 4 đọc bản đồ qua DOM, không lưu ảnh có vị trí hoặc địa chỉ thật.

| Nhãn | Nghĩa |
|---|---|
| `Chạy` | Đã thao tác và thấy kết quả, không phụ thuộc vị trí giả lập |
| `Chạy (vị trí giả lập)` | Đã thao tác, dữ liệu vị trí là giả lập |
| `Chạy (Fleetio Go)` | Phiếu nộp thật trên app, chỉ đọc kết quả của chính phiếu |
| `Xem` | Thấy trên giao diện, chưa thao tác hết |
| `Docs` | Tài liệu công khai của hãng |
| `Suy` | Suy ra, chưa kiểm chứng |
| `GĐ` | Giả định |

## 3. User Types (preliminary)

| User Type | Pain Point | Primary Need |
|---|---|---|
| Điều vận | Không thấy xe đang ở đâu, dữ liệu còn tươi không | Bản đồ cùng danh sách, biết tuổi vị trí, lọc nhanh |
| Quản lý phương tiện | Xe hỏng, không biết xưởng gần nhất | Thấy xe và xưởng trên một bản đồ, tạo sự cố ngay từ xe |
| Admin của khách | Phải khai báo địa điểm | Tạo địa điểm, vùng tròn hoặc đa giác đơn giản |
| Quản lý công trường, dự án | Không biết xe nào đang ở việc nào, bao lâu | Gán xe vào việc, tự tính thời gian theo vùng |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Điều vận | Xem vị trí, độ tươi vị trí xe | Liên tục | Cao | Marker không báo chạy hay dừng |
| Quản lý phương tiện | Tìm xưởng, cây dầu gần xe; tạo sự cố từ bản đồ | Mỗi ngày | Trung | Quick Add rời khỏi bản đồ sau khi lưu |
| Admin của khách | Khai báo địa điểm, vùng | Hiếm | Trung | Bấm nhầm bản đồ làm đổi địa chỉ, toạ độ |
| Quản lý công trường | Gán, kết thúc gán, hoàn thành việc | Mỗi ngày | Thấp với vận tải | Hoàn thành không hỏi lại dù còn xe đang gán |
| Admin của khách | Tạo Automation, cảnh báo vùng | Hiếm | Trung | Sự kiện vùng không có màn xem lại |

## 4. Capabilities Breakdown

Phần "Đề xuất" là gợi ý cho Invlogis, chưa phải yêu cầu đã chốt.

### P0 — must have

- B1 [Mới] [Lõi] **Bản đồ cạnh danh sách, sắp theo khoảng cách**, dòng ghi tên xe, người lái, tuổi vị trí ("3m ago"). `Chạy (vị trí giả lập)`. Mốc tính khoảng cách là tâm bản đồ: `Suy`. Đề xuất cho `vehicle-telematics`.
- B2 [Mới] [Lõi] **Lớp bật tắt:** Xe, Địa điểm, Nhà cung cấp; tài liệu hãng có thêm Xưởng. Bật Nhà cung cấp thêm marker và tab ở danh sách, tắt Xe mất marker và cả tab, tải lại trang về mặc định: `Chạy`. Không có nút Xưởng riêng, chú giải có 5 loại, phần Xưởng giữ `Docs`. Trong panel xe, Places và Vendors mặc định ẩn, có nút Show: `Chạy (vị trí giả lập)`.
- B16 [Mới] [Lõi] **Tìm và lọc trên bản đồ:** ô tìm gộp nhà cung cấp, xe, địa điểm; 8 bộ lọc xe và 1 bộ lọc nhà cung cấp, huy hiệu số bộ lọc. `Chạy`. Đề xuất: lấy, nhưng tên khớp đúng lên đầu và giữ bộ lọc khi tải lại; Fleetio xếp nhà cung cấp trước và mất lọc khi tải lại.
- B3 [Mới] [Lõi] **Tải dữ liệu theo khung nhìn.** `Chạy`, API `map/last_live_location_values` nhận `current_bounds`.
- B10 [Mới] [Lõi] [Cấu hình] **Marker theo độ tươi dữ liệu:** Active, Idle, Stale. Fleetio: 30 phút, 1 giờ. `Chạy (vị trí giả lập)`. Con số là tham số mới, chưa có mã. Đề xuất: tách độ tươi khỏi trạng thái chạy, dừng để tránh hiểu nhầm.
- B11 [Mới] [Lõi] **Bấm xe không mở popup mà đổi panel trái sang xe đó**, có Overview, Nearby và nút Add. `Chạy (vị trí giả lập)`. Đề xuất cho `vehicle-telematics`: giữ bản đồ thấy được khi xem chi tiết.

### P1 — should have

- B4 [Mới] [Cấu hình] **Địa điểm có vùng tròn hoặc đa giác**, nhập toạ độ thì tự điền địa chỉ. Fleetio: bán kính gợi ý 100, 200, 500, 1000 m, gõ số khác được. `Chạy`. Đề xuất cho `location-catalog`, Invlogis vẫn cần thêm cảng, bãi, loại phí; danh sách bán kính là tham số mới, chưa có mã.
- B5 [Mới] [Lõi] **Khối Vị trí gần nhất trên panel xe:** Status, Last Updated, Where, Source trỏ về phiếu đã sinh vị trí. `Chạy (vị trí giả lập)`.
- B6 [Mới] [Lõi] **Lấy vị trí từ phiếu kiểm tra** khi không có thiết bị. Trên web, phiếu kiểm gửi vị trí trình duyệt: `Chạy`. Phiếu dầu và phiếu dịch vụ trên web **không có ô vị trí**: `Chạy`. Fleet Map thể hiện kết quả: `Chạy (vị trí giả lập)`. Fleetio Go ghi toạ độ từng mục: `Chạy (Fleetio Go)`.
- B17 [Mới] [Lõi] **Vị trí từ phiếu dầu, phiếu dịch vụ có nhà cung cấp:** chọn nhà cung cấp là sinh vị trí xe từ địa chỉ đó, cùng giờ phiếu, xe lên bản đồ. Không cần thiết bị. `Chạy`. Đề xuất: cân nhắc làm dự phòng khi mất GPS, ghi rõ "vị trí khai", báo trên form và kiểm địa chỉ quy đổi.
- B18 [Mới] [Lõi] **Lịch sử vị trí trên trang xe:** danh sách có icon loại, bản đồ cạnh bên, lọc theo ngày và 3 loại nguồn. `Chạy`. Đề xuất cho `vehicle-telematics`, thêm loại GPS.
- B7 [Mới] [Cấu hình] **Sự kiện vào, ra vùng là trigger Automation:** điều kiện loại sự kiện, Place, xe, nhóm xe; hành động Update Field, Add Comment, Send Email. Add Comment: `Chạy (vị trí giả lập)`. Update Field, Send Email: `Xem`. Đề xuất đối chiếu `vehicle-telematics`.
- B12 [Mới] [Cấu hình] **Cảnh báo vùng:** trong hoặc ngoài vùng, cho xe hoặc Contact, gửi email từng lần hoặc tổng hợp ngày. `Xem`, chưa lưu vì hành động duy nhất là gửi email.
- B13 [Mới] [Lõi] **Quick Add từ panel xe:** 11 loại bản ghi, xe điền sẵn. Add Issue: `Chạy (vị trí giả lập)`. 10 mục còn lại: `Xem`. Đề xuất: lưu xong quay lại bản đồ, Fleetio chuyển sang trang sự cố.

### P2 — nice to have

- B8 [Mới] [Cấu hình] **Gán xe vào việc bằng bảng cột:** cột Unassigned và mỗi việc một cột, thẻ xe đếm thời gian, lịch sử có nguồn Manual hoặc Geofence. Gán tay: `Chạy`. Tự gán: `Chạy (vị trí giả lập)`. Chỉ hợp khách công trình, không phải vận tải container.
- B9 [Mới] [Cấu hình] **Bộ chú giải bản đồ, nhãn tên, lớp nền Satellite, Grayscale, lưu theo người dùng.** `Chạy (vị trí giả lập)`. Nhãn marker xe chọn 1 trong 5 trường (tên, VIN, loại xe, biển số, năm hãng dòng), trường trống thì về tên xe, lưu theo người dùng: `Chạy`. Đề xuất: Invlogis cân nhắc mặc định biển số.
- B14 [Mới] [Lõi] **Đường nét đứt từ xe tới địa điểm khi rê chuột dòng Nearby**, kèm khoảng cách. `Chạy (vị trí giả lập)`.
- B15 [Mới] [Cấu hình] **API đẩy vị trí từ hệ thống ngoài**, có Bulk API. `Docs`, chưa gọi thử. Đề xuất đọc khi thiết kế lớp kết nối GPS.

## 5. Core Flows (Happy Path)

### 5.1 Xem đội xe trên bản đồ

`Chạy (vị trí giả lập)`.

1. Mở bản đồ: tâm mở theo IP của máy (`/web_api/ip_geo_location`), không tự thu về xe. Khung không có xe thì hiện "No results found in this area".
2. Tìm xe ở ô Locate, hoặc kéo, zoom tới vùng có xe. Danh sách hiện xe, người lái, tuổi vị trí.
3. Bấm marker hoặc dòng: không có popup, panel trái đổi sang xe, marker gắn nhãn tên.
4. Xem Overview, Nearby; bật Places, rê chuột để thấy đường nối; bấm Add để Quick Add.

```
Mở map ─> Tâm theo IP ─> Lấy bounds ─> Vẽ lớp + Danh sách gần nhất ─> Chọn xe ─> Panel trái
                            ▲                     │                       ├─> Nearby ─> rê chuột: nét đứt
                            └── kéo, zoom ────────┘                       └─> Add ─> form điền sẵn xe
```

### 5.2 Vị trí từ hoạt động

```
Thiết bị GPS ──────────────────────(Docs)──┐
API location_entries ──────────────(Docs)──┤
Phiếu kiểm tra, web ───────────────(Chạy)──┼─> Location Entry ─> Vị trí gần nhất ─> Bản đồ
Phiếu dầu có nhà cung cấp ─────────(Chạy)──┤
Phiếu dịch vụ có nhà cung cấp Service ─(Chạy)──┘
Phiếu dầu không có nhà cung cấp: không sinh vị trí (Suy)
```

Trên web, app đọc vị trí trình duyệt một lần lúc khởi động app rồi giữ giá trị đó; form không báo gì khi gửi. Địa chỉ ngược có sau khoảng 1 phút. Phiếu dầu, phiếu dịch vụ không có ô vị trí; vị trí lấy từ địa chỉ nhà cung cấp, form cũng không báo. Xe hiện như đang ở đó dù chỉ là địa chỉ khai. Địa chỉ giả vẫn được quy ra một điểm, có thể ở nước khác, không báo độ tin cậy.

### 5.3 Sự kiện vùng và hệ quả

`Chạy (vị trí giả lập)`; việc so với lần trước là `Suy` từ kết quả.

```
Location Entry mới ─> So với các vùng ─┬─ Từ ngoài vào ─> Entered ─┬─> Việc bật tự động: thêm lượt gán, Added = Geofence
                                       │                           └─> Automation Geofence Event chạy
                                       └─ Từ trong ra ──> Exited ──┬─> Lượt gán tự kết thúc, xe về Unassigned
                                                                   └─> Automation Geofence Event chạy
```

Một lần ghi từ vùng A sang vùng B làm Automation chạy 2 lần: `Chạy (vị trí giả lập)`; 2 lần đó ứng với ra A và vào B là `Suy`.

### 5.4 Việc và lượt gán

`Chạy`.

```
Add Job ─> Việc Active ─> Tick xe, Actions, Assign ─> Lượt gán Active ─┬─> Unassign ─> lượt có End, xe về Unassigned
                                                                       └─> Complete Job ─> mọi lượt tự kết thúc, việc Completed
```

Chi tiết mọi nhánh: [[docs/_research/fleetio/srs/fleetio-location-dispatch-flows.md|Flows]], [[docs/_research/fleetio/srs/fleetio-location-dispatch-states.md|States]].

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES | NO | Mức |
|---|---|---|---|---|---|
| D1 | 5.1 | Bật "Update list when map moves" | Danh sách theo khung nhìn | Kéo tay: danh sách giữ nguyên, kể cả khi bản đồ đã thấy marker. Chọn từ ô tìm: danh sách vẫn đổi. Tick lại: áp ngay | `Chạy` |
| D2 | 5.2 | Nhà cung cấp GPS hỗ trợ gần thời gian thực | Cập nhật liên tục | Chỉ hiện các lần ghi đã có | `Docs` |
| D3 | 5.2 | Trình duyệt cho phép định vị lúc khởi động app | Phiếu mang vị trí, sinh Location Entry | Phiếu không có vị trí (#125988723, nguyên nhân chưa rõ) | `Chạy`, nhánh NO là `Suy` |
| D4 | 5.3 | Vị trí mới đổi quan hệ với vùng | Sinh Entered hoặc Exited | Không có sự kiện | `Suy` từ `Chạy (vị trí giả lập)` |
| D5 | 5.3 | Việc gắn Place có ô tự động bật | Tự thêm, tự kết thúc lượt gán | Không gán | `Chạy (vị trí giả lập)` |
| D6 | 5.4 | Xe đang có việc | Assign mờ, chỉ còn Unassign | Assign được | `Chạy` |
| D7 | 5.4 | Giờ gán trùng khoảng cũ của xe | Báo lỗi trùng, không lưu | Tạo lượt gán | `Chạy` |
| D8 | 5.4 | Complete khi còn xe đang gán | Tự kết thúc lượt cùng End, không hỏi | Chỉ đóng việc (`Suy`) | `Chạy` |
| D9 | 5.2 | Phiếu dầu có chọn nhà cung cấp | Sinh Location Entry Fuel Entry tại địa chỉ nhà cung cấp, không báo | Không sinh vị trí (`Suy`) | `Chạy` |
| D10 | 5.2 | Nhà cung cấp có phân loại Service trên form phiếu dịch vụ | Chọn được; lưu là sinh Location Entry Service Entry, không báo | Chỉ hiện `Create "TEST"` | `Chạy` |
| D13 | 5.1 | Tải lại trang sau khi đổi lớp | Lớp về mặc định: Xe bật, Địa điểm, Nhà cung cấp tắt | Giữ trong phiên | `Chạy` |
| D11 | 5.1 | Enter ngay ở ô tìm | Chọn dòng đầu, có thể nhầm nhà cung cấp | Đi xuống chọn đúng dòng | `Chạy` |
| D12 | 5.1 | Tải lại trang khi đang lọc | Bộ lọc mất, về toàn bộ kết quả; Map Options vẫn giữ | Bộ lọc còn trong phiên | `Chạy` |

### 6.3 Trạng thái

| Đối tượng | Trạng thái | Ghi chú |
|---|---|---|
| Việc | Active, Completed | Chưa thấy đường mở lại |
| Lượt gán | Active, đã kết thúc | Cột End Date hiện "Active" khi đang gán |
| Độ tươi vị trí xe | Không có vị trí, Active, Idle, Stale | Tính theo thời gian, không phải trạng thái lưu (`Suy`) |
| Địa điểm, sự kiện vùng | Không có trạng thái | Sự kiện vùng chỉ có loại Entered, Exited |
| Ô "Update list when map moves" | Đã tick, bỏ tick | Trạng thái giao diện |
| Bộ lọc bản đồ | Không lọc, đang lọc | Mất khi tải lại trang |

### 6.5 Other Edge Cases

- **Nút zoom:** nút "+" có `aria-label` "Zoom Out", nút "−" có "Zoom In". Hành vi đúng theo hình vẽ, chỉ nhãn trợ năng sai. Lỗi này cần tránh. `Chạy`
- **Vùng không có xe:** "No results found in this area. Try updating your filter criteria or moving the map to re-do your search." Bản đồ không tự thu về xe nên người dùng mới dễ gặp màn này dù có xe.
- **Gom cụm marker:** zoom xa hết với 2 xe và 2 Place không gom, marker đè nhau: `Chạy (vị trí giả lập)`. Lượt 3 đếm thêm 15 nhà cung cấp và 4 xe, vẫn không có marker dạng số: `Chạy`. **Chưa biết ngưỡng ở số lớn hơn.**
- **Vị trí khai giống vị trí thật:** xe có vị trí từ phiếu dầu hiện như đang ở cây dầu, chỉ phân biệt qua Source và loại. Địa chỉ nhà cung cấp giả vẫn quy được ra một điểm ở nước khác, không báo độ tin cậy, trang nhà cung cấp vẫn ghi đúng chuỗi đã nhập; khai sai địa chỉ làm xe nhảy đi mà không cảnh báo. `Chạy`
- **Form nhà cung cấp:** Enter ở ô Country lưu luôn, bỏ qua Classification. `Chạy`
- **Ô tìm bản đồ:** gõ tên xe rồi Enter chọn nhầm nhà cung cấp vì khớp mờ và nhà cung cấp đứng đầu; phải đi xuống 4 dòng mới tới xe. Xe chưa có vị trí vẫn nằm trong kết quả. `Chạy`
- **Mất bộ lọc:** tải lại trang là mất bộ lọc, trong khi Map Options được giữ. `Chạy`
- **Danh sách lệch bản đồ:** bỏ tick "Update list when map moves" rồi kéo tay, danh sách vẫn "0 results" dù bản đồ thấy marker. `Chạy`
- **Phiếu dịch vụ:** form chỉ cho chọn nhà cung cấp phân loại Service; có nhà cung cấp đúng phân loại thì sinh vị trí như phiếu dầu. `Chạy`
- **Marker bị che:** xe trùng tâm Place thì tâm Place che marker xe. `Chạy (vị trí giả lập)`
- **Độ tươi không nhất quán:** trang xe có lúc ghi "Idle" khi vị trí mới 25 giây, bản đồ vẫn "Active". Chưa rõ lý do. `Chạy (vị trí giả lập)`
- **Không chống toạ độ giả:** máy chủ tin toạ độ trình duyệt gửi. Phiếu cách nhau đến khoảng 1.100 km vẫn `location_exception` = false, kể cả khi biểu mẫu bật Location Exception Tracking. `Chạy (vị trí giả lập)`
- **Location Exception:** trên web gói tin chỉ có một cặp toạ độ cấp phiếu, mục kiểm không có toạ độ, nên không tạo được cờ. Fleetio Go có ghi toạ độ từng mục (#126102722, 21/21 mục, lệch tối đa 37 m, cờ vẫn false), phiếu có 2 chỉ báo mục quá gần và số mục quá xa, `starting_latitude` vẫn rỗng: `Chạy (Fleetio Go)`. Chưa có ca dương nên chưa biết ngưỡng.
- **Sự kiện vùng không xem lại được:** không có màn danh sách, không có cột ở Location Entries của Place. Chỉ thấy gián tiếp qua lịch sử việc, Automation và `location_entry.initial_place`.
- **Log Automation không đáng tin:** Run Result ghi "No records changed" dù comment đã thêm; log có bước `ActionSet` trạng thái `DNF` với lý do "Automation Trigger has no action set". Run Result cũng không ghi loại sự kiện hay Place.
- **Bấm bản đồ trong form địa điểm:** đặt lại pin, Address và toạ độ đổi theo, Name giữ nguyên. Form mở với bản đồ chưa đúng nơi nên dễ bấm nhầm. Đổi toạ độ còn để lại một pin đỏ ở điểm cũ.
- **Đa giác:** Radius bị khoá với giá trị tự tính, trang chi tiết vẫn ghi Geofence Radius như vùng tròn. Đa giác 2 đỉnh vẫn được form chấp nhận, chưa thử lưu.
- **Kéo thả thẻ xe:** không hoạt động ở mức quan sát qua công cụ.
- **Unassign:** ô giờ chỉ có chữ mờ chứ chưa có giá trị; bấm ngay thì băng đỏ không nói lỗi gì.
- **Múi giờ:** giờ hiển thị theo giờ máy dù cài đặt người dùng khác, có banner cảnh báo lệch.
- **Gần thời gian thực** theo tài liệu hãng chỉ áp cho Samsara, Geotab, Motive, Verizon, Caterpillar. Chưa rõ về các nhà cung cấp ở Việt Nam.

### 6.6 Điểm đáng học và điểm yếu

| Loại | Điểm | Đề xuất cho Invlogis (chưa chốt) |
|---|---|---|
| Đáng học | Panel trái thay popup, bản đồ vẫn thấy được | Dùng cho bản đồ phương tiện |
| Đáng học | Source của vị trí trỏ về bản ghi sinh ra nó | Dòng vị trí luôn ghi nguồn |
| Đáng học | Tuổi vị trí ngay trên dòng danh sách | Điều vận biết dữ liệu còn tươi không |
| Đáng học | Lượt gán ghi nguồn Manual hoặc Geofence, chip trên thẻ xe | Mẫu hay cho mọi dữ liệu tự sinh |
| Đáng học | Phiếu ghi việc đang gán tại thời điểm nộp, rồi mới xử lý vùng | Bản ghi giữ đúng bối cảnh lúc phát sinh |
| Đáng học | Cấm gán giờ tương lai, cấm chồng khoảng | Nguyên tắc lịch sử phản ánh việc thật |
| Đáng học | Phiếu dầu, phiếu dịch vụ tự cho vị trí xe, không cần thiết bị | Dự phòng khi mất GPS, ghi rõ nguồn |
| Đáng học | Nhãn marker chọn trường, trống thì về tên xe | Áp cho marker phương tiện |
| Đáng học | Lịch sử vị trí có loại nguồn, lọc được | Thêm loại GPS, phiếu dầu, phiếu kiểm |
| Đáng học | Fleetio Go ghi toạ độ từng mục kiểm | Dữ liệu đúng mức để phát hiện kiểm khống |
| Đáng học | Tuỳ chọn bản đồ lưu theo người dùng | Áp cho cả bộ lọc hay dùng |
| Điểm yếu | Marker chỉ báo độ tươi, không báo chạy, dừng | Invlogis có GPS EUP nên tách hai thông tin |
| Điểm yếu | Máy chủ tin toạ độ, không so giữa các phiếu | Nếu dùng vị trí để chống khống: kiểm hợp lý giữa các lần ghi |
| Điểm yếu | Đọc vị trí lúc khởi động app, không phải lúc nộp, không báo người dùng | Đọc lúc nộp, báo rõ đang ghi vị trí |
| Điểm yếu | Sự kiện vùng không có màn xem lại | Cần nhật ký vào, ra vùng |
| Điểm yếu | Sự kiện vào và ra dùng chung trigger, dễ chạy trùng nếu thiếu điều kiện loại | Tách hoặc buộc chọn loại sự kiện |
| Điểm yếu | Hoàn thành việc không hỏi dù còn xe | Báo số xe sẽ bị kết thúc |
| Điểm yếu | Lỗi Unassign không có câu chữ, kéo thả không có | Điền sẵn giờ hiện tại |
| Điểm yếu | Phiếu dầu, phiếu dịch vụ tạo vị trí không báo, xe hiện như đang ở địa chỉ khai | Tách "vị trí khai" khỏi vị trí đo được, báo trên form |
| Điểm yếu | Địa chỉ quy ra điểm không có độ tin cậy, có thể sang nước khác | Cho xác nhận điểm trên bản đồ khi khai nhà cung cấp, không lấy điểm kém tin cậy làm vị trí xe |
| Điểm yếu | Lớp bản đồ không giữ qua tải lại | Lưu theo người dùng như Map Options |
| Điểm yếu | Enter ở một ô giữa form lưu luôn nhà cung cấp | Enter không gửi form có phần chưa điền |
| Điểm yếu | Ô tìm khớp mờ, nhà cung cấp đứng trước xe | Tên khớp đúng lên đầu, Enter không chọn nhầm |
| Điểm yếu | Bộ lọc mất khi tải lại | Giữ bộ lọc qua tải lại |
| Điểm yếu | Bỏ tick làm danh sách lệch bản đồ, không có dấu hiệu | Báo danh sách đang theo khung cũ, có nút cập nhật |
| Điểm yếu | Marker không gom ở mức đã đo, đè nhau khi xa | Đội xe lớn cần gom cụm |

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule | Bằng chứng |
|---|---|---|
| Địa điểm | Bắt buộc tên, địa chỉ, vĩ độ, kinh độ, bán kính | `Xem` |
| Bán kính | Chọn sẵn hoặc gõ số; đa giác thì khoá, tự tính | `Chạy` |
| Đa giác | Không chặn 2 đỉnh trên form | `Chạy`, chưa thử lưu |
| Job Number, Job Name | Bắt buộc | `Chạy` |
| Start Date/Time lượt gán | Hiện tại hoặc quá khứ, không chồng khoảng cũ | `Chạy` |
| End Date/Time | Sau giờ bắt đầu, không ở tương lai | `Chạy` |
| Alert Policy | Bắt buộc Which Vehicles, Recipients; chỉ người dùng có email | `Xem` |
| Nhà cung cấp trên phiếu dịch vụ | Chỉ chọn được nhà cung cấp phân loại Service | `Chạy` |
| Địa chỉ nhà cung cấp | Không kiểm, địa chỉ giả vẫn quy ra điểm | `Chạy` |

### 7.2 Limits

| Giới hạn | Giá trị | Bằng chứng |
|---|---|---|
| Độ tươi Active | Fleetio: trong 30 phút | `Chạy (vị trí giả lập)`, chú giải |
| Độ tươi Idle | Fleetio: trong 1 giờ | `Chạy (vị trí giả lập)`, chú giải |
| Độ tươi Stale | Fleetio: quá 1 giờ | `Chạy (vị trí giả lập)`, chú giải |
| Bán kính gợi ý | Fleetio: 100, 200, 500, 1000 m | `Chạy` |
| Địa chỉ ngược của Location Entry | Khoảng 1 phút, đo một lần | `Chạy (vị trí giả lập)` |
| Lịch sử vị trí | Fleetio: 30 dòng mỗi trang | `Chạy` |
| Gom cụm | Fleetio: chưa gom ở 15 nhà cung cấp, 4 xe; chưa biết ngưỡng | `Chạy` |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording |
|---|---|
| Bỏ trống số việc | "can't be blank" |
| Gán giờ tương lai | "cannot be in the future" |
| Gán trùng khoảng | "active Assignment overlaps with historical Assignment" |
| Complete, End trước giờ bắt đầu | "must be after active assignment start date/time" |
| Complete, End ở tương lai | "End date cannot be in the future" |
| Xe chưa có lịch sử vị trí | "No results found." |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Xe chưa có vị trí | "No current location information available for this Vehicle" |
| Người nhận cảnh báo | "Only users with an email address will be available for selection." |
| Đang khởi tạo | "Map initializing..." |
| Gợi ý vẽ vùng | "You can draw a geofence directly on the map by clicking the circle or polygon icon." |
| Quy tắc gán | "Job assignments can only be created for the current or past date/time. Since they're meant to reflect real activity, future-dated assignments aren't supported at present." |
| Quy tắc kết thúc gán | "When unassigning an asset from a job, the end time of the assignment must be set to the current time or a past date/time." |
| Ô tự động | "Automatically assign and unassign assets when entering or leaving the selected Place's geofence boundary." |
| Nhãn marker xe | "Select field to display for Vehicle map marker labels. Falls back to Vehicle Name if selected field value is empty/blank." |
| Kết quả tìm | "10 results available for search term TEST" |
| Đổi vị trí mở đầu | "Map Preferences Updated" |
| Tổng hợp cảnh báo | "By default, alerts are sent when detected. Enable this setting to receive a daily summary of the previous day's activity for the configured policy rules." |

#### Success messages

| Tình huống | Wording |
|---|---|
| Địa điểm | "Place was successfully created", "Place was successfully updated" |
| Việc | "Job created successfully", "Job completed successfully" |
| Lượt gán | "Job assignments created successfully", "Vehicles successfully unassigned from Jobs" |

## 8. Assumptions

- `GĐ` Invlogis dùng dữ liệu GPS từ EUP theo brainstorm `vehicle-telematics`, không phụ thuộc mô hình tích hợp của Fleetio.
- `GĐ` Hành vi sự kiện vùng với vị trí giả lập qua phiếu giống với vị trí từ thiết bị. Chưa kiểm vì không có thiết bị.

## 9. Risks

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| Lấy Jobs làm mẫu khiến đơn giản hoá Lệnh vận tải | Cao | Không dùng; giữ brainstorm `transport-dispatch` |
| Chi phí bản đồ tăng theo số lần gọi | Trung | Giãn cách khi kéo, tải theo khung nhìn |
| Dùng toạ độ phiếu làm bằng chứng có mặt trong khi toạ độ giả được | Cao | Không coi là bằng chứng nếu không có kiểm tra thêm |
| Ghi vị trí thật của người dùng mà không báo | Cao | Chờ pháp chế (OQ-3 trong SRS); đề xuất báo rõ khi ghi |
| Kết luận sự kiện vùng dựa trên vị trí giả lập | Trung | Kiểm lại với thiết bị trước khi trích làm yêu cầu |
| Coi vị trí từ phiếu dầu, phiếu dịch vụ là vị trí xe thật; địa chỉ khai sai làm xe nhảy sang nơi không liên quan mà không cảnh báo | Cao | Tách vị trí khai khỏi vị trí đo được, kiểm địa chỉ nếu lấy cơ chế này |

## 10. Success Criteria (preliminary)

- Điều vận tìm được xe cần xem trong vài thao tác.
- Điều vận biết vị trí đang thấy cũ bao lâu ngay trên danh sách.

## 11. Open Questions

| ID | Câu hỏi | Nguồn khách |
|---|---|---|
| OQ-1 | [x] Có tài khoản Fleetio nào có thiết bị định vị để xem marker thật không? Không cần nữa cho phần giao diện: đã thấy marker bằng vị trí giả lập qua phiếu kiểm tra. Hành vi với thiết bị thật vẫn chưa kiểm | Câu hỏi nội bộ |
| OQ-2 | [ ] Fleetio Go có ghi vị trí từng mục kiểm, có tạo Location Exception không? Một phần: có ghi vị trí từng mục; chưa có ca dương | Câu hỏi nội bộ |
| OQ-3 | [ ] Gom cụm marker khi nhiều xe? Tới 15 nhà cung cấp, 4 xe chưa thấy gom; chưa biết ngưỡng ở số lớn hơn | Câu hỏi nội bộ |
| OQ-4 | [x] Phiếu dịch vụ có nhà cung cấp có sinh vị trí như phiếu dầu không? Có, cùng cơ chế, form không báo | Câu hỏi nội bộ |
| OQ-5 | [x] Địa chỉ nhà cung cấp giả được quy ra một điểm bằng cách nào? Vẫn ra một điểm, ở nước khác, không báo độ tin cậy; dịch vụ quy đổi không nhìn thấy được | Câu hỏi nội bộ |
| OQ-6 | [ ] Địa chỉ hoàn toàn không quy được thì phiếu có sinh vị trí không; sửa địa chỉ có đổi các lần ghi cũ không? | Câu hỏi nội bộ |

Danh sách đầy đủ: [[docs/_research/fleetio/srs/fleetio-location-dispatch-spec.md|SRS]] Mục 12.

## 12. Next Steps

- BL-382: dùng được chú giải 3 mức độ tươi và marker nhỏ làm đầu vào; trạng thái chạy, dừng cần nguồn khác.
- Đối chiếu ý B1, B11 với thiết kế bản đồ Điều vận khi đến lượt.
- Thử ca dương trên Fleetio Go nếu cần ngưỡng Location Exception; thử với nhiều xe nếu cần kết luận gom cụm (gói thử đã đủ 5 xe, phải có tài khoản khác).
- Quyết định có lấy vị trí từ phiếu dầu làm dự phòng khi đến lượt `vehicle-telematics`.
