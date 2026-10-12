---
type: shared-screen-patterns
status: draft
updated: 2026-10-12
links:
  - design/design.md
  - design/components.md
  - design/ui-common/conventions.md
  - docs-input/ui-common/web/web-common-rules.md
  - docs-input/ui-common/app/app-common-rules.md
  - docs/cross-process-flow/brainstorms/cross-process-flow.md
  - design/_lab/lab-progress.html
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
| CMP-09 | Cross Process Flow (Liên quy trình) | Bản ghi thuộc một quy trình nhiều nghiệp vụ — xem cả quy trình dạng cây từ màn chi tiết | SC-09 · MSC-06 · lab-progress (12/10/2026) |
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

**Việc còn mở (2026-10-01):** CMP-07 cần dựng component dự án Action Matrix · CMP-09 Cross Process Flow
cần component dự án dạng cây · CMP-10 File Upload và CMP-11 Sidebar bản thư viện chưa đạt yêu cầu. Bốn mục này
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

Bottom sheet xác nhận (kéo lên từ đáy màn), cùng bộ hành động bắt buộc và cùng câu chữ như web.
Mẫu: `design/_lab/lab-confirm.html` phương án B (chốt 09/10/2026).

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 0 | Tay nắm | — | — | • Thanh ngang trên đỉnh sheet; vuốt xuống = Huỷ, trừ các trường hợp ở hàng 8 |
| 1 | Icon hành động | Icon | ReadOnly | • Tông theo loại: phá huỷ / xác nhận / cảnh báo (design.md › Ánh xạ trạng thái nghiệp vụ); luôn đi kèm tiêu đề, không chỉ dựa vào màu |
| 2 | Tiêu đề | Label | ReadOnly | • Căn giữa, chữ đậm |
| 3 | Nội dung | Label | ReadOnly | • Như web; tên/mã bản ghi in đậm |
| 4 | Trường lý do | Chip + Text area | Select + Text | • Chỉ khi hành động cần lý do (vd Từ chối): chip lý do nhanh + ô ghi thêm; danh sách chip và bắt buộc hay không do UC khai |
| 5 | Nút xác nhận | Button | Click | • Full width, đứng trên; phá huỷ dùng biến thể destructive<br>• Loading khi đang gửi |
| 6 | Nút huỷ | Button | Click | • Full width, ghost, đứng dưới<br>• Huỷ form (GR-13): đảo vai — "Tiếp tục chỉnh sửa" là nút chính, "Bỏ thay đổi" là nút chữ đỏ |
| 7 | Nền mờ | — | — | • Chạm ngoài = Huỷ |
| 8 | Khoá đóng | — | — | • **Không** đóng bằng chạm ngoài / vuốt xuống với hành động không hoàn tác được (Xoá) và với popup chặn GR-26 |

**Biến thể Vuốt để xác nhận** — cho hành động quan trọng cần chắc chắn người dùng cố ý (mẫu: `lab-confirm.html`
phương án E). Cùng sheet trên, thay nút xác nhận (hàng 5) bằng thanh vuốt "Vuốt để [động từ]": kéo hết thanh
mới gửi, thả giữa chừng thì trượt về; phá huỷ dùng tông destructive. Thêm nút đóng (X) góc phải; nút huỷ giữ ở dưới.
Trình đọc màn hình / bàn phím: thanh vuốt kích hoạt được bằng Enter/Space.
- **UC phải khai báo thêm:** hành động nào dùng biến thể vuốt. Không khai → dùng sheet nút bấm thường.

- Thêm trường hợp chỉ app có — **Chuyển site** (chạm bản ghi thuộc site khác): "Chuyển sang [Tên site]?" ·
  "Trang sẽ tải lại theo site mới." → `[Chuyển site] [Huỷ]`. Câu gốc app 2.18: "Bạn đang chuyển sang
  [Tên site]. Trang sẽ được tải lại theo site mới."
- Back / vuốt back khi form có dữ liệu chưa lưu: GR-13 (Mobile).
- **Figma:** chưa có node Figma cho sheet xác nhận — chưa có chuẩn trong design.md (mẫu ở lab, chờ vẽ lại).

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

## CMP-09 — Cross Process Flow (Liên quy trình)

Xem cả quy trình nhiều nghiệp vụ dạng cây từ màn chi tiết của bất kỳ bản ghi nào trong quy trình: bước
chính, nhánh phát sinh, ngã rẽ chưa chốt, bước thuộc module khác, bước công nợ. Phần nghiệp vụ (lưu
nguồn, trạng thái bước và quy trình, mã quy trình, quyền xem) ở feature
[[docs/cross-process-flow/brainstorms/cross-process-flow.md|cross-process-flow]]; mục này giữ phần hiển thị.
Chỉ dùng cho quy trình nhiều nghiệp vụ. Vòng đời của 1 bản ghi dùng nhãn trạng thái + CMP-08, không dùng CMP-09.

| # | Items | Control type | Data type | Description |
|---|---|---|---|---|
| 1 | Dòng quy trình | Row | Click | • Web: đầu màn chi tiết · Mobile: thẻ quy trình<br>• Tên luồng · thanh tiến độ · "Xong x/y bước · n nhánh phát sinh" · "Bước trước: …" (bước chính) hoặc "Phát sinh từ: …" (nhánh phát sinh)<br>• Bản ghi không thuộc quy trình, hoặc luồng độc lập chưa có nhánh → không hiện (R11)<br>• Tải lỗi → "Không tải được quy trình." + Thử lại; màn chi tiết vẫn dùng bình thường |
| 2 | Sơ đồ | Popup (web) · Sheet (mobile) | Click | • Mở từ màn chi tiết: chọn sẵn bước "Ở đây" · mở từ danh sách Quy trình: chưa chọn bước nào<br>• Mặc định vừa khung; zoom 40–250%, kéo, nút vừa khung<br>• Card tóm tắt góc trên trái: thanh tiến độ + số bước theo trạng thái<br>• Đang tải: "Đang tải sơ đồ…" · lỗi: E-common-008 / E-common-009 + Thử lại · dữ liệu đổi: Theo GR-27 |
| 3 | Thẻ bước | Card | Click | • Icon nghiệp vụ · tên bước · mã chứng từ (`N/A` khi chưa tạo) · trạng thái của bản ghi (R7)<br>• Nhãn Phát sinh góc trên trái (R16) · ghim "Ở đây" góc trên phải (R10) · nhãn module khi khác module đang mở (R9)<br>• Bước chính chưa tới: viền đứt + "Chưa tạo" (R5)<br>• Chọn → viền màu + mở panel (#6) |
| 4 | Đường nối | Line | ReadOnly | • Nét liền: đã tạo · nét đứt: chưa tạo · vệt sáng chạy theo chiều đi khi bước đích Đang triển khai, tắt khi người dùng bật giảm chuyển động (R15)<br>• Trên đường chỉ có nhãn điều kiện của bước chính, 1 dòng, viết cho người dùng đọc (R16, R17)<br>• Nhiều bước trước cùng vào 1 bước: mỗi đường 1 cửa vào, chip "Điều kiện x/y" trên đường nguồn (R1) |
| 5 | Nút ngã rẽ | Card | Click | • "Chưa xác định …" khi bước sau phụ thuộc lựa chọn chưa có; panel liệt kê các hướng có thể đi (R6) |
| 6 | Panel chi tiết bước | Panel (web) · Sheet (mobile) | — | • Web: rộng 300px, nổi đè cột phải; nội dung dài thì cuộn<br>• Đầu panel: tên, mã, trạng thái, nhãn Ở đây / Phát sinh / module; nhánh phát sinh có thêm lý do phát sinh (không ghi mã TH)<br>• Lịch sử hoạt động: 5 dòng mới nhất, Theo CMP-08 + link "Xem tất cả" mở màn chi tiết<br>• Bước chưa tạo: "Chưa có hoạt động. Bước này chưa được tạo."<br>• Không có quyền xem bước: ẩn lịch sử + nút, hiện E-common-011 tại chỗ. Override GR-26: hiện trong panel thay vì popup chặn — lý do: chỉ 1 bước không xem được, không chặn cả màn |
| 7 | Nút mở | Button | Click | • "Mở màn hình chi tiết", ghim đáy panel. Web: mở cùng tab, đóng popup (Back trình duyệt về màn cũ, popup không mở lại) · Mobile: đẩy màn mới<br>• Bước công nợ: "Mở bảng công nợ", lọc theo nhà cung cấp + khoảng thời gian của bảng công nợ (R8)<br>• Bản ghi vừa bị thu quyền: popup chặn E-common-011 theo GR-26 |

**Quy tắc vẽ:**

| Mã | Quy tắc |
|---|---|
| R1 | Vẽ theo nguồn, không theo thứ tự thời gian: mỗi bước nối về đúng bản ghi tạo ra nó. Bước cần nhiều bước trước cùng xong thì nối từ tất cả các bước đó về 1 nút. Nhánh không bắt buộc chỉ nối vào bước sau khi bước sau thật sự chờ nhánh đó. |
| R2 | Nhánh phát sinh có nhãn Phát sinh trên thẻ, viền liền như bước khác. Lý do phát sinh chỉ ghi ở panel; kiểu đường không dùng để báo phát sinh. |
| R3 | Nhánh phát sinh sinh tiếp bước khác thì nối vào chính nhánh đó (vd Nhập kho dư → Bồi thường). |
| R4 | Mỗi bản ghi là 1 bước, không gộp. Nhiều phiếu cùng loại cùng nguồn là các bước anh em cùng tên, phân biệt bằng mã; không ghi "lần 1, lần 2". |
| R5 | Nhánh phát sinh chỉ hiện khi điều kiện đã xảy ra. Bước chính chưa tới vẫn hiện, ghi "Chưa tạo". |
| R6 | Bước sau phụ thuộc lựa chọn chưa có → 1 nút ngã rẽ "Chưa xác định …". |
| R7 | Thẻ ghi trạng thái của bản ghi, màu theo nhóm: xong · đang chờ/đang làm · từ chối · chưa tạo, luôn kèm icon (✓ · đồng hồ · ▶ · ✕ · vòng đứt). 4 trạng thái bước chỉ quyết định icon và màu đường nối. Bước bị từ chối không làm mất nhánh con đã có. |
| R8 | Bước thanh toán trả sau ghi "Công nợ [Tên nhà cung cấp]", mở bảng công nợ đã lọc. |
| R9 | Bước thuộc module khác gắn nhãn module (vd Cây dầu). |
| R10 | Bước của màn đang mở có ghim "Ở đây"; đường từ gốc tới bước đó tô đậm. Viền màu chỉ dành cho bước đang chọn. |
| R11 | Luồng độc lập chưa có nhánh thì không hiện dòng quy trình; có nhánh đầu tiên thì bản ghi gốc là nút đầu cây. |
| R12 | Dòng tóm tắt: "Xong x/y bước · n nhánh phát sinh". |
| R13 | Nút tạo nghiệp vụ tiếp theo đặt ở vùng hành động đầu trang, không đặt trên sơ đồ. |
| R14 | Dàn sơ đồ: cột = bậc (bước đứng sau bước trước xa nhất của nó); bước chính giữ hàng bước trước, nhánh xuống hàng trống kế tiếp; đường chỉ vuông góc, không cắt qua thẻ; nhãn ở giữa đường. |
| R15 | Đường nối vào bước Đang triển khai là nét liền có vệt sáng chạy; nét đứt chỉ cho bước chưa tạo. |
| R16 | Nhãn Phát sinh gắn cố định góc trên trái thẻ, đối xứng ghim "Ở đây" góc trên phải; không đặt nhãn trên đường. |
| R17 | Khe giữa 2 cột = nhãn dài nhất trên đường + 16px mỗi bên, tối thiểu 64px; khe giữa 2 hàng 32px. Nhãn điều kiện 1 dòng, mục tiêu ≤40 ký tự, không cắt chữ; góc rẽ cách bước trước 16px. Cây trên 20 bước vẫn vẽ, mặc định vừa khung. |

- **Figma:** chưa có — Astryx `Stepper` chỉ vẽ được dạng thẳng, cần dựng component dự án dạng cây · node: chưa gắn · ảnh: chưa gắn. Mẫu tương tác: `design/_lab/lab-progress.html`.
- **design.md:** —
- **UC phải khai báo:** bảng liên quy trình của nghiệp vụ (bước · tạo từ · trigger · trường hợp phát sinh · điều kiện · 1 hay nhiều bản ghi · cho thu hồi/xoá khi đã có bước con · cho xoá), câu chữ viết cho người dùng đọc; tên luồng; tên bước + icon nghiệp vụ; màn chi tiết đích của mỗi bước.

### Mobile

- Thẻ quy trình trên màn chi tiết: tên quy trình là chính, dòng tóm tắt là phụ.
- Sheet: card tóm tắt như web + cây rẽ nhánh dọc, thẻ cùng dạng web; vuốt ngang khi cây rộng hơn màn.
- Panel bước: không nền màu, pill trạng thái có viền, nhãn đặt bên phải.
- "Mở màn hình chi tiết" đẩy màn mới; Back về màn trước, sheet đã đóng.
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
