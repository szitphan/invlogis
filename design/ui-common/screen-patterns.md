---
type: shared-screen-patterns
status: draft
updated: 2026-10-04
links:
  - design/design.md
  - design/components.md
  - design/ui-common/conventions.md
  - docs-input/ui-common/web/web-common-rules.md
  - docs-input/ui-common/app/app-common-rules.md
---

# UI Common Components (CMP)

Component dùng chung toàn hệ thống, web và app. UC/màn gọi theo mã: `Xem CMP-xx — {tên}`, rồi chỉ điền phần
**UC phải khai báo** của CMP đó. Màn app gọi cùng mã; chỗ app khác web ghi ở khối **Mobile** trong từng
mục, kèm phần UC phải khai báo riêng nếu có. Quy tắc nhập liệu, định dạng, bảng ở [[design/ui-common/conventions.md|Quy tắc chung (GR)]].

Màu, cỡ, khoảng cách, câu chữ lấy theo `design/design.md` (Content & Formatting › Copy động). File này
không chứa wording cố định; chỗ nào có câu mẫu là trỏ về design.md.

| Mã | Tên | Dùng khi | Nguồn gốc |
|---|---|---|---|
| CMP-01 | Toast Notification | Phản hồi sau hành động (thành công, lỗi hệ thống, cảnh báo, thông tin) | SC-01 · app 2.12, 2.17 |
| CMP-02 | In-app Notification | Hành động nghiệp vụ cần báo cho người liên quan trong luồng | SC-02 · MSC-01 |
| CMP-03 | Confirm Dialog / Confirm Popup | Trước hành động quan trọng hoặc không hoàn tác được | SC-03 · MSC-02, app 2.13, 2.18 |
| CMP-04 | Pagination / Tải thêm | Cuối mọi màn danh sách | SC-04 · app 2.15 |
| CMP-05 | Filter Drawer (Bộ lọc nâng cao) | Lọc nâng cao trên màn danh sách | SC-05 + 2.20 · MSC-03 |
| CMP-06 | Column Customizer | Bật/tắt, sắp thứ tự cột bảng danh sách — chỉ web | SC-06 |
| CMP-07 | Action Matrix / Action Sheet | Hành động trên từng bản ghi của danh sách | SC-07 · MSC-04 |
| CMP-08 | Activity Log | Lịch sử hành động trên màn chi tiết/drawer | SC-08 · MSC-05 |
| CMP-09 | Stepper | Luồng nghiệp vụ nhiều bước liên tiếp | SC-09 · MSC-06 |
| CMP-10 | File Upload | Đính kèm chứng từ, tài liệu | SC-10 · MSC-07 |
| CMP-11 | Sidebar Menu / Bottom Navigation | Điều hướng chính giữa module/feature | SC-13 · MSC-08 |
| CMP-12 | Success Bottom Sheet | Chỉ app: sau hành động quan trọng, buộc người dùng chọn bước tiếp theo | MSC-11 |

Nguồn app: `docs-input/ui-common/app/app-common-rules.md`. Mã MSC theo mục lục và tiêu đề Phần 1 của
tài liệu đó; Phần 2 của tài liệu gọi lệch số (vd "MSC-03" cho Confirm) — đã map theo nội dung.
MSC-09 Empty State và MSC-10 Skeleton Loader là quy tắc trạng thái, nằm ở GR-12 (khối Mobile).

Mỗi CMP có dòng **Figma**: component trong thư viện Astryx (tên set theo `design/figma-library-keys.json`)
hoặc component dự án (mục *Components - innvie logis* của design.md), node mẫu trong file Figma dự án
`FifpyOMpZk9OP8qyNzbRVJ`, và ảnh cache `design/ui-common/images/cmp-NN.png` (chụp qua Figma MCP). Dòng
**design.md** liệt kê mục design.md chứa chi tiết (tách bằng `;`) — `_scripts/ui-common-expand.py` đọc
dòng này để chép nguyên văn vào Phụ lục A của SRS.

**Việc còn mở (2026-10-01):** CMP-07 cần dựng component dự án Action Matrix · CMP-09 Stepper nghiệp vụ
cần component riêng · CMP-10 File Upload và CMP-11 Sidebar bản thư viện chưa đạt yêu cầu. Bốn mục này
đang tạm dùng component Astryx, chưa có ảnh.
CMP-05 Bộ lọc nâng cao và CMP-06 Tuỳ chỉnh cột: đã có node nhưng ảnh chụp UI chưa đủ rõ (chip co chữ,
popover tách khỏi ngữ cảnh) — cần chọn/dựng khung chụp riêng rồi gắn lại ảnh.

**Việc còn mở — Mobile (2026-10-04):** bố cục mobile chưa có chuẩn trong design.md (KG-03, spec M chưa
có node Figma; khung nền `Device / Frame` 393×852 (iPhone 14 Pro) có từ 06/10/2026) → mọi khối Mobile và CMP-12 chưa có
node, chưa có ảnh. CMP-11 Mobile: chốt Bottom Navigation 4 tab + nút Quét giữa là điều hướng của M1
(06/10/2026), dựng thành component dự án. CMP-05 Mobile cao tối đa 85% chưa có biến thể BottomSheet tương ứng (Capped 62% / Tall 92%).

---

## CMP-01 — Toast Notification

Thông báo ngắn góc trên phải, tự ẩn sau 3 giây, không chặn thao tác.

![CMP-01](images/cmp-01.png)
_Ảnh: Toast "Đã lưu thay đổi." — node [5080:2503](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5080-2503), xuất PNG 2x._

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Toast thành công | Toast | ReadOnly | • Sau khi hành động hoàn tất<br>• Câu: mẫu "Đã {hành động}" theo design.md › Copy động › Toast; thêm `[Hoàn tác]` nếu đảo ngược được |
| 2 | Toast lỗi | Toast | ReadOnly | • Chỉ cho lỗi kỹ thuật/hệ thống (GR-15 Loại 3) — `E-common-008..010`<br>• Lỗi của trường → inline; lỗi nghiệp vụ server → Popup Error (GR-15) |
| 3 | Toast cảnh báo | Toast | ReadOnly | • Cảnh báo không chặn hành động |
| 4 | Toast thông tin | Toast | ReadOnly | • Hướng dẫn hoặc trạng thái trung gian |

- **Figma:** Astryx `Toast` · node: [172:56853](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=172-56853)
- **design.md:** Copy động
- **UC phải khai báo:** hành động nào có toast thành công + động từ dùng trong câu; hành động có `[Hoàn tác]` không.

### Mobile

- Cùng 4 loại và câu chữ như web. Toast lỗi nền error cho lỗi không gắn với trường nào (lỗi server,
  lỗi mạng — `E-common-008`, `E-common-009`).
- Vị trí và thời gian hiện trên màn app: chưa có chuẩn trong design.md.
- **Figma:** chưa gắn.

## CMP-02 — In-app Notification

Icon chuông trên header, badge chưa đọc, panel danh sách thông báo. Spec đầy đủ: design.md ›
*Notification Center (theo SC-02)*.

![CMP-02](images/cmp-02.png)
_Ảnh: Panel Desktop — node [5144:2204](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5144-2204), xuất PNG 2x._

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Icon chuông | Button | Click | • Mở panel thông báo |
| 2 | Badge chưa đọc | Badge | ReadOnly | • Số chưa đọc, tối đa `9+`, ẩn khi 0, cập nhật realtime |
| 3 | Tiêu đề panel | Label | ReadOnly | • "Thông báo" + số chưa đọc |
| 4 | Đánh dấu đã đọc | Button | Click | • Ghost/link; toàn bộ về Đã đọc, badge về 0; ẩn khi không còn chưa đọc |
| 5 | Một thông báo | Item | Click | • Module nguồn · nội dung · thời gian (GR-03 dạng Relative)<br>• Chưa đọc / đã đọc phân biệt bằng nền + chấm<br>• Click → Đã đọc, badge −1, mở chi tiết bản ghi |

Mẫu nội dung chung: `[Tên module] · [Tên feature] — [Định danh] vừa được/bị [hành động] bởi [Người thực hiện]`.
Định danh: có mã → mã bản ghi; chưa có mã (trước phê duyệt, GR-11) → "một [tên feature]".

Hành động mặc định:

| Hành động | Động từ | Người nhận |
|---|---|---|
| Tạo mới (submit) | vừa được tạo | Người có quyền phê duyệt |
| Phê duyệt | vừa được phê duyệt | Người tạo |
| Từ chối | vừa bị từ chối | Người tạo |
| Thu hồi | vừa bị thu hồi | Người có quyền phê duyệt |

- **Figma:** component dự án `Notification Center` · node: [5142:2017](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5142-2017)
- **design.md:** Notification Center
- **UC phải khai báo:** hành động nào phát thông báo; người nhận; nội dung theo hành động (dùng bảng mặc định hay động từ riêng); định danh (tên feature, mã bản ghi); màn đích khi click.

### Mobile

- Chuông nằm ở tab Thông báo của Bottom Navigation (CMP-11). Badge tối đa `9+`, chỉ đếm việc cần xử lý
  như web (tài liệu app ghi `99+` — đã chốt `9+`, 2026-10-04).
- Chạm tab → **màn riêng** "Thông báo", nút ← quay lại (design.md › Notification Center, Platform = Mobile).
- Chạm một thông báo → Đã đọc, badge −1, mở thẳng màn chi tiết bản ghi qua deep link (GR-24).
- **Figma:** `Notification Center / Panel` Platform = Mobile · node mẫu: chưa gắn.

## CMP-03 — Confirm Dialog

Modal xác nhận trước hành động quan trọng hoặc không hoàn tác được. Bắt buộc với: Xoá, Thu hồi, Phê
duyệt, Từ chối, Huỷ form khi có dữ liệu chưa lưu (GR-13). Tiêu đề, nội dung, nhãn nút theo design.md ›
Copy động › *Hộp xác nhận*.

![CMP-03](images/cmp-03.png)
_Ảnh: Destructive, Default — node [5046:66967](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5046-66967), xuất PNG 2x._

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tiêu đề | Label | ReadOnly | • Câu hỏi nêu hành động + đối tượng |
| 2 | Nội dung | Label | ReadOnly | • Nêu bản ghi bị tác động (ưu tiên tên, không có thì mã, không có cả hai thì bỏ) + hệ quả |
| 3 | Trường lý do | Text area | Text | • Chỉ khi hành động cần lý do (vd Từ chối); bắt buộc hay không do UC quy định |
| 4 | Nút xác nhận | Button | Click | • Nhãn = động từ hành động; hành động phá huỷ dùng biến thể destructive<br>• Loading khi đang gửi |
| 5 | Nút huỷ | Button | Click | • Đóng dialog, không thay đổi dữ liệu |

- **Figma:** Astryx `AlertDialog` (có trường lý do → `Dialog` [2266:9922](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=2266-9922)) · node: [5046:66987](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5046-66987)
- **design.md:** Copy động
- **UC phải khai báo:** hành động nào cần xác nhận; tên feature + trường định danh hiển thị; có trường lý do không, bắt buộc không; hệ quả nêu trong nội dung (vd "trở về Bản nháp").

### Mobile

Confirm Popup giữa màn, cùng bộ hành động bắt buộc và cùng câu chữ như web.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Icon hành động | Icon | ReadOnly | • Tông theo loại: phá huỷ / xác nhận / cảnh báo (design.md › Ánh xạ trạng thái nghiệp vụ); luôn đi kèm tiêu đề, không chỉ dựa vào màu |
| 2 | Tiêu đề | Label | ReadOnly | • Căn giữa, chữ đậm |
| 3 | Nội dung | Label | ReadOnly | • Như web; tên/mã bản ghi in đậm |
| 4 | Nút xác nhận | Button | Click | • Full width; phá huỷ dùng biến thể destructive |
| 5 | Nút huỷ | Button | Click | • Full width, outlined/ghost |
| 6 | Nền mờ | — | — | • Chạm ngoài = Huỷ; **không** đóng với hành động không hoàn tác được (Xoá) và với popup chặn GR-26 |

- Thêm trường hợp chỉ app có — **Chuyển site** (chạm bản ghi thuộc site khác): "Chuyển sang [Tên site]?" ·
  "Trang sẽ tải lại theo site mới." → `[Chuyển site] [Huỷ]`. Câu gốc app 2.18: "Bạn đang chuyển sang
  [Tên site]. Trang sẽ được tải lại theo site mới."
- Back / vuốt back khi form có dữ liệu chưa lưu: GR-13 (Mobile).
- **Figma:** chưa gắn (Astryx `AlertDialog` trên khung 390 — chưa có chuẩn trong design.md).

## CMP-04 — Pagination

Thanh phân trang cuối mọi màn danh sách. Spec: design.md › *Phân trang danh sách (theo SC-04)*.

![CMP-04](images/cmp-04.png)
_Ảnh: Pages, md — node [2347:57791](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=2347-57791), xuất PNG 2x._

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Số bản ghi/trang | Dropdown | Select | • 25 / 50 / 100, mặc định 50 |
| 2 | Nhãn tổng | Label | ReadOnly | • Cập nhật theo bộ lọc hiện tại |
| 3 | Số trang | Button | Click | • Trang đầu, hiện tại ±1, `…`, trang cuối; trang hiện tại nổi bật |
| 4 | Trước / Sau | Button | Click | • Vô hiệu ở trang đầu/cuối |

- **Figma:** Astryx `Pagination` · node: [2347:58586](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=2347-58586)
- **design.md:** Phân trang danh sách
- **UC phải khai báo:** chỉ khi khác mặc định (vd số bản ghi/trang khác 50). Khi nhóm dữ liệu, phân trang theo nhóm (GR-17).

### Mobile

- Không dùng số trang. Cuộn tới 80% cuối danh sách thì tự tải thêm 20 mục, spinner nhỏ ở cuối khi đang
  tải, hết dữ liệu hiện "Đã hiển thị tất cả kết quả". Chi tiết: GR-23.
- **UC phải khai báo:** chỉ khi khác 20 mục/lần.

## CMP-05 — Filter Drawer (Bộ lọc nâng cao)

Bộ lọc nâng cao màn danh sách. Spec + phương án đã chốt: design.md › *Bộ lọc nâng cao (theo SC-05 +
2.20)*. Lọc theo từng cột trên header bảng: GR-20.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Tiêu đề | Label | ReadOnly | • "Bộ lọc" + số điều kiện đang áp dụng |
| 2 | Trường lọc | Dropdown / DatePicker / Textbox | Select / Date / Number | • Thứ tự theo thứ tự cột của bảng (kể cả cột ẩn)<br>• Kiểu: chọn đơn, chọn nhiều (có giá trị "Không có" cho dữ liệu rỗng), khoảng ngày, khoảng số |
| 3 | Xoá bộ lọc | Button | Click | • Ghost; đưa mọi trường về rỗng |
| 4 | Áp dụng | Button | Click | • Primary; đóng, áp dụng, tải lại danh sách |
| 5 | Badge trên nút Bộ lọc | Badge | ReadOnly | • Số điều kiện đang áp dụng; ẩn khi không có |

- **Figma:** component dự án `Bộ lọc nâng cao` (PowerSearch + `.Value Editor`) · node: [5176:9303](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5176-9303) · **ảnh: chưa gắn — xử lý sau:** ảnh chụp UI chưa đủ rõ
- **design.md:** Bộ lọc nâng cao
- **UC phải khai báo:** danh sách trường lọc + kiểu lọc mỗi trường; giá trị mặc định; phụ thuộc giữa các trường (nếu có); trường không lọc được.

### Mobile

- Nút **Bộ lọc** trên thanh công cụ màn danh sách, badge số điều kiện đang áp dụng.
- Mở `BottomSheet` trượt từ đáy, cao tối đa 85% màn, cuộn được bên trong (85% chưa có biến thể — tạm
  Height = Tall). Header "Bộ lọc" + nút xoá mọi điều kiện ở góc phải.
- Trường lọc dạng chọn (Select), ngày (DatePicker), danh sách checkbox. Nút **Áp dụng** full width cố
  định đáy → đóng sheet, áp dụng, tải lại danh sách.
- Chip điều kiện hiện dưới ô tìm, cuộn ngang; × trên chip → xoá điều kiện đó (design.md › Bộ lọc nâng cao, phần Mobile).
- **Figma:** `Bộ lọc nâng cao` bản Mobile · node mẫu: chưa gắn.

## CMP-06 — Column Customizer (Tuỳ chỉnh cột)

Bật/tắt và sắp thứ tự cột, lưu theo từng người dùng. Spec: design.md › *Tuỳ chỉnh cột (theo SC-06)*.
**Chỉ web** — app không có bảng nhiều cột (danh sách dạng List).

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Danh sách cột | Checkbox | Check | • Mọi cột theo thứ tự bảng (kể cả cột ẩn); tick để hiện/ẩn; kéo thả để đổi thứ tự |
| 2 | Cột khoá | Checkbox | ReadOnly | • Không ẩn được, checkbox vô hiệu + icon khoá |
| 3 | Đặt lại mặc định | Button | Click | • Về cấu hình cột mặc định của màn |
| 4 | Áp dụng | Button | Click | • Bảng cập nhật ngay |

- **Figma:** component dự án `Tuỳ chỉnh cột` · node: [5177:7634](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5177-7634) · **ảnh: chưa gắn — xử lý sau:** ảnh chụp UI chưa đủ rõ
- **design.md:** Tuỳ chỉnh cột
- **UC phải khai báo:** danh sách cột + thứ tự mặc định; cột nào hiện mặc định; cột khoá.

## CMP-07 — Action Matrix (hành động trên hàng)

Cột hành động cuối mỗi hàng danh sách. Quy tắc bảng: design.md › *Quy tắc bảng danh sách*.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Icon hành động hiện sẵn | Button | Click | • Tối đa 2 icon; chỉ hiện hành động khả dụng theo trạng thái + quyền (không hiện rồi vô hiệu) |
| 2 | Menu ⋯ | Button | Click | • Gom hành động phụ; hành động phá huỷ (Xoá, Huỷ) luôn nằm trong ⋯; chỉ có 1 hành động phụ thì hiện thẳng, không dùng ⋯ |
| 3 | Vùng thông tin hàng | Link | Click | • Click → màn chi tiết; click vùng hành động không mở chi tiết |

- **Figma:** tạm Astryx `MoreMenu` + `Button` (Ghost Icon Only) · node: [198:12758](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=198-12758) · **chưa chuẩn — xử lý sau:** cần dựng component dự án Action Matrix · ảnh: chưa gắn
- **design.md:** Quy tắc bảng danh sách
- **UC phải khai báo:** ma trận **trạng thái × quyền → hành động**; 2 hành động hiện sẵn; hành động nào cần CMP-03.

### Mobile — Action Sheet

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Mở | — | — | • Nhấn giữ bản ghi hoặc chạm icon ⋯ trên bản ghi |
| 2 | Danh sách hành động | Button | Click | • `BottomSheet` trượt từ đáy; mỗi dòng icon trái + nhãn<br>• Chỉ hiện hành động khả dụng theo trạng thái + quyền (như web)<br>• Hành động phá huỷ tông error, luôn ở cuối danh sách → CMP-03 |
| 3 | Huỷ | Button | Click | • Full width, tách riêng khỏi danh sách; nhãn "Huỷ" |
| 4 | Nền mờ | — | — | • Chạm ngoài = đóng |

- **Figma:** Astryx `BottomSheet` + `BottomSheet / .Content · Hành động` (design.md › BottomSheet) · node mẫu: chưa gắn.
- **UC phải khai báo:** cùng ma trận trạng thái × quyền như web; app không có "2 hành động hiện sẵn".

## CMP-08 — Activity Log

Lịch sử thay đổi trạng thái/hành động trên bản ghi, mở từ icon đồng hồ góc trên phải màn chi tiết.
Spec: design.md › *Activity Log (theo SC-08)*.

![CMP-08](images/cmp-08.png)
_Ảnh: Panel Desktop — node [5162:3528](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5162-3528), xuất PNG 2x._

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Icon mở | Button | Click | • Mở panel lịch sử |
| 2 | Một mốc | Item | ReadOnly | • Avatar · tên tài khoản · ngày (GR-03) · icon · nội dung hành động<br>• Dòng "Lý do: …" chỉ khi hành động có lý do (vd Từ chối) |
| 3 | Sắp xếp | — | — | • Mới nhất trên cùng |

Hành động mặc định: Tạo mới (`+`, "Đã tạo mới [tên feature]") · Phê duyệt (`✓`, "Đã phê duyệt tạo mới [tên feature]") ·
Từ chối (`✕`, "Đã từ chối phê duyệt [tên feature]") · Thu hồi ("Đã huỷ tạo mới [tên feature]").

- **Figma:** component dự án `Activity Log` · node: [5160:3295](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5160-3295)
- **design.md:** Activity Log
- **UC phải khai báo:** tên feature dùng trong câu; hành động ghi log ngoài 4 hành động mặc định + icon/nội dung.

### Mobile

- Icon đồng hồ trên header màn chi tiết (nút LG trong vùng chạm 44).
- Mở `BottomSheet` (design.md › Activity Log, Platform = Mobile). Khác MSC-05 (tài liệu app ghi "màn
  riêng") — đã chốt theo design.md, 2026-10-04.
- Timeline dọc, mới nhất trên cùng, nội dung mốc như web.
- **Figma:** `Activity Log / Panel` Platform = Mobile (khung [5160:3295](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5160-3295)).

## CMP-09 — Stepper

Thanh tiến trình đầu màn cho luồng nghiệp vụ nhiều bước liên tiếp.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Bước | Label | Click | • Trạng thái: đã xong / hiện tại / chưa tới<br>• Click bước đã xong → chuyển sang màn nghiệp vụ của bước đó (nếu có quyền) |

- **Figma:** tạm Astryx `Stepper` + `Stepper / Step` · node: [5045:66913](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5045-66913) · **chưa chuẩn — xử lý sau:** Stepper nghiệp vụ phức tạp hơn bản thư viện, cần dựng component dự án · ảnh: chưa gắn
- **design.md:** —
- **UC phải khai báo:** danh sách bước + thứ tự; điều kiện hoàn thành mỗi bước; bước nào được click quay lại.

### Mobile

- Thanh bước cố định đầu màn, ngay dưới thanh điều hướng. Bước hiện tại nổi bật + chữ đậm · bước đã qua
  icon ✓ · bước chưa tới màu nhạt — luôn có icon/chữ, không chỉ dựa vào màu. Tên bước dưới icon.
- Chạm bước để chuyển, cùng điều kiện như web.
- **Figma:** chưa gắn.

## CMP-10 — File Upload

Đính kèm chứng từ, tài liệu.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Vùng upload | Browse Button | File | • Viền đứt + icon + hướng dẫn; hỗ trợ kéo thả |
| 2 | Nút chọn file | Button | Click | • Outlined; mở hộp chọn file |
| 3 | Định dạng cho phép | Label | ReadOnly | • Mặc định JPG, PNG, PDF |
| 4 | Dung lượng tối đa | Label | ReadOnly | • Mặc định 250MB |
| 5 | Thẻ file | Card | Click | • Đang tải: icon loại + tên + dung lượng + đang tải<br>• Thành công/thất bại: thêm icon kết quả + Xoá<br>• Màn xem: icon loại + tên (click xem/tải) |
| 6 | Giới hạn số file | — | — | • 1 file: tải xong ẩn vùng upload, xoá file thì hiện lại<br>• Nhiều file: giữ vùng upload, thẻ file xếp bên dưới |
| 7 | Lỗi định dạng | Label | ReadOnly | • Inline ngay khi chọn file, file không được ghi nhận — `E-common-006` |
| 8 | Lỗi dung lượng | Label | ReadOnly | • Inline ngay khi chọn file, file không được ghi nhận — `E-common-007` |

- **Figma:** tạm Astryx `FileInput` · node: [2577:20886](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=2577-20886) · **chưa chuẩn — xử lý sau:** chưa đạt yêu cầu CMP-10 (thẻ file, trạng thái tải, giới hạn số file) · ảnh: chưa gắn
- **design.md:** —
- **UC phải khai báo:** định dạng bổ sung; dung lượng nếu khác 250MB; 1 hay nhiều file (tối đa bao nhiêu); bắt buộc không.

### Mobile

- Chạm vùng upload → `BottomSheet` chọn nguồn: **Thư viện ảnh** · **Chụp ảnh** · **Files**. Không có kéo thả.
- Thẻ file: đang tải có thanh tiến độ + nút huỷ · thành công icon ✓ + xoá · thất bại icon ✕ + **Thử lại** + xoá.
- Định dạng, dung lượng, lỗi (`E-common-006`, `E-common-007`) như web; hiện dưới vùng upload.
- **Figma:** chưa gắn.

## CMP-11 — Sidebar Menu

Menu cố định bên trái, điểm truy cập chính tới module/feature.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Logo | Link | Click | • Về danh sách module |
| 2 | Thu gọn | Button | Click | • Chỉ còn icon, hover hiện tooltip tên; trạng thái lưu theo người dùng |
| 3 | Mục cấp 1 (module) | Button | Click | • Tên + icon; có submenu thì mũi tên mở/đóng; module chứa trang hiện tại tự mở |
| 4 | Mục cấp 2 | Link | Click | • Thụt lề dưới module cha; điều hướng tới màn |
| 5 | Trạng thái active | — | — | • Chỉ 1 mục active, nổi bật + vạch dọc trái |
| 6 | Footer: tên module | Label | ReadOnly | • Module hiện tại |
| 7 | Footer: tên cơ sở | Dropdown | Select | • Ẩn khi module không chia cơ sở<br>• 1 cơ sở: chỉ hiện tên, không mở được<br>• Nhiều cơ sở: chọn để chuyển sang cơ sở khác |

Cấu trúc menu theo phân quyền role: người dùng chỉ thấy module được phép.

- **Figma:** tạm Astryx `Navigation / SideNav` trong `AppShell` · node: [2401:17634](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=2401-17634) · **chưa chuẩn — xử lý sau:** chưa đạt yêu cầu CMP-11 (footer module/cơ sở, menu theo role) · ảnh: chưa gắn
- **design.md:** —
- **UC phải khai báo:** vị trí mục menu của feature (module cha, cấp); role nào thấy; module có chia cơ sở không.

### Mobile — Bottom Navigation

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Thanh điều hướng | — | — | • Thanh nổi cố định đáy, phía trên vùng an toàn của máy<br>• Chỉ hiện ở 4 màn gốc; màn con ẩn thanh, đáy dành cho hành động chính của màn |
| 2 | Tab | Button | Click | • 4 tab chỉ icon (không hiện chữ), nhãn truy cập: Trang chủ · Lịch nhắc · Thông báo · Tài khoản |
| 3 | Tab đang chọn | — | — | • Khối nền đồng tâm với thanh + icon đậm; tab khác icon nhạt<br>• Chạm lại → cuộn về đầu |
| 4 | Badge | Badge | ReadOnly | • Trên tab Thông báo, tối đa `9+` (theo CMP-02) |
| 5 | Nút Quét | Button | Click | • Tròn, giữa thanh, nhô lên trên mép; chỉ icon, nhãn truy cập "Quét mã QR"<br>• Mở màn quét bằng camera |

- Là điều hướng của mẫu M1 (design.md › Bottom Navigation, chốt 06/10/2026). Astryx chưa có component
  này → component dự án.
- **Figma:** component dự án `Bottom Navigation` · node mẫu: [5381:3341](https://www.figma.com/design/FifpyOMpZk9OP8qyNzbRVJ/-innvie--invlogis-v0.3?node-id=5381-3341) · ảnh: chưa gắn
- **design.md:** Bottom Navigation
- **UC phải khai báo:** feature mở từ tab nào / màn nào; quét xong đi tới màn nào.

## CMP-12 — Success Bottom Sheet

Chỉ app. Sheet chặn toàn bộ luồng sau khi hoàn tất một hành động quan trọng, buộc người dùng chủ động
chọn bước tiếp theo.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Nền mờ | — | — | • Chạm ngoài **không** đóng |
| 2 | Khung sheet | Bottom Sheet | — | • Trượt lên từ đáy, cao theo nội dung, tối đa 85% màn<br>• Thanh kéo có nhưng vuốt xuống **không** đóng (khác bottom sheet thường) |
| 3 | Icon | Icon | ReadOnly | • Tròn tông success, dấu ✓ |
| 4 | Tiêu đề | Label | ReadOnly | • Căn giữa, chữ đậm |
| 5 | Mô tả | Label | ReadOnly | • Căn giữa, chữ phụ, tối đa 2 dòng |
| 6 | Thẻ tóm tắt | Card | ReadOnly | • Các dòng nhãn (trái) – giá trị (phải, đậm vừa), đường kẻ giữa các dòng |
| 7 | Nút chính | Button | Click | • Full width, primary |
| 8 | Nút phụ | Button | Click | • Full width, secondary; Back của hệ điều hành = chạm nút phụ |

- Màu, cỡ, bo góc, chuyển động lấy theo token design.md (tài liệu app ghi số cứng: nền `#F5F5F5`, bo 20px,
  icon 64px, tiêu đề 18px, trượt 300ms — không dùng).
- **Figma:** Astryx `BottomSheet` · node mẫu: chưa gắn — chưa có chuẩn trong design.md.
- **design.md:** —
- **UC phải khai báo:** tiêu đề + mô tả; các dòng của thẻ tóm tắt; nhãn + màn đích của 2 nút.
