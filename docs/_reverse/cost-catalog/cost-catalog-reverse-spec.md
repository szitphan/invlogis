---
type: reverse-srs
feature: cost-catalog
status: draft
updated: 2026-10-20
confidence_summary: "✅99 🔵3 🟡15"
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs/_product/srs-v2-change-log.md
---

# Khoản mục chi phí cấp 1–3 (`cost-catalog`) — SRS tái lập (reverse)

> Trạng thái: `draft` (tái lập, chưa duyệt). Nhãn: ✅ chắc chắn · 🔵 suy đoán · 🟡 cần xác nhận.

## 0. Truy vết nguồn & độ tin cậy

- **Module:** Danh mục › Tài chính (gắn tạm theo DEC-079, chốt ở PRD).
- **Nguồn:** Tài liệu SRS - ERP Delta 3.0 (Web) (bản 30/9/2026) — chi tiết ở [`reverse-sources.md`](./reverse-sources.md).
- **Câu hỏi mở / khác biệt:** xem [`reverse-gaps.md`](./reverse-gaps.md).
- **Độ tin cậy:** ✅ 99 · 🔵 3 · 🟡 15 (đếm trên các dòng bảng).
- **Trạng thái:** tái lập từ SRS cũ, **CHƯA duyệt**. ✅ nghĩa là "SRS cũ ghi rõ", không có nghĩa "hệ thống đang chạy đúng như thế".

| Phần | Nguồn đã đọc |
|---|---|
| Chi phí cấp 1, cấp 2, cấp 3 | SRS Web tr.283–284, tr.578–679 |

### 0.3 Khác biệt với thay đổi đã chốt

| Điểm | SRS cũ nói | Thay đổi nói | Đề xuất |
|---|---|---|---|
| Danh mục chi phí có gắn địa điểm không | Danh mục phân cấp 1–2–3, không gắn địa điểm nào. ✅ [SRS Web tr.581–584, 614–617, 648–651 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3] | Loại phí có cách hạch toán theo địa điểm. `Thay đổi CHG-20 (loại phí hạch toán theo địa điểm)` — ✅ SOP đường sắt | `/cr` |
| Cách hạch toán của loại phí | Không có thuộc tính cách hạch toán trong form tạo cấp 1, 2, 3. ✅ [SRS Web tr.592–593, 626–627, 658–661 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3] | Bốn cách hạch toán: thu nhập chịu thuế của lái xe · chi hộ · trả hộ · chi phí vận hành. `Thay đổi CHG-20 (loại phí hạch toán theo địa điểm)` — ✅ SOP đường sắt | `/cr` |
| Định mức theo loại phí và địa điểm | Không có định mức trong danh mục chi phí. ✅ [SRS Web tr.648–651 — UC03.12.01 Xem danh mục chi phí cấp 3] | Định mức tự điền theo loại phí và địa điểm, ví dụ depot đường sắt 150.000 đ Nam Khánh, 160.000 đ Phú Lợi. `Thay đổi CHG-20 (loại phí hạch toán theo địa điểm)` — ✅ SOP đường sắt | `/cr` |
| Ai chọn loại phí | SRS cũ chỉ có tác nhân "Người dùng phần mềm xưởng", không có lái xe. ✅ [SRS Web tr.581 — UC03.10.01 Xem danh mục chi phí cấp 1] | Lái xe chỉ chọn loại phí, cách hạch toán và định mức do bảng quyết định. `Thay đổi CHG-20 (loại phí hạch toán theo địa điểm)` — ✅ SOP đường sắt | `/cr` |
| Chỗ gắn bảng mới | Chi phí cấp 3 chỉ có tên, tên tiếng Anh, ghi nhận qua PO, tên dịch vụ, liên quan phương tiện, thuộc cấp 2, ghi chú. ✅ [SRS Web tr.658–661 — UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 3] | Thêm bảng "loại phí × địa điểm → cách hạch toán, định mức" nối vào chi phí cấp 3. `Thay đổi CHG-20 (loại phí hạch toán theo địa điểm)` — ✅ SOP đường sắt | `/cr` |
| Tuyến ngoài đường sắt | SRS cũ không phân biệt tuyến. ✅ [SRS Web tr.581 — UC03.10.01 Xem danh mục chi phí cấp 1] | Chờ Delta gửi bảng cho các tuyến ngoài đường sắt. `Thay đổi CHG-20 (loại phí hạch toán theo địa điểm)` — ⏳ tuyến khác (OQ-31) | `/gap` |

## 1. Scope

Phần này tái lập đặc tả hiện trạng của **danh mục khoản mục chi phí ba cấp** (chi phí cấp 1, cấp 2, cấp 3) trong phân hệ Danh mục của phần mềm xưởng (PMX), đường dẫn Dashboards > Tab Danh mục > Sub-tab Chi phí cấp 1 / cấp 2 / cấp 3 ✅ [SRS Web tr.581, 614, 648 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3]. Ba cấp tạo thành cây cha-con: chi phí cấp 2 thuộc một chi phí cấp 1, chi phí cấp 3 thuộc một chi phí cấp 2 ✅ [SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 2, 3].

Mỗi cấp dùng chung một khuôn năm use case: xem danh sách, xem thông tin, tạo đề xuất tạo mới, huỷ đề xuất, phê duyệt/từ chối đề xuất ✅ [SRS Web tr.578–679 — Feature 03.10, 03.11, 03.12]. Bản ghi mới không có hiệu lực ngay: tạo ra ở trạng thái Chờ phê duyệt và chỉ thành khoản mục đã phê duyệt (được cấp mã) sau khi có người phê duyệt ✅ [SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục; tr.609, 643, 677 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3]. Vì vậy FR và use case được viết một lần cho cả khuôn, kèm bảng "Khác biệt theo cấp" (Mục 3).

Điểm khác biệt chính giữa các cấp: cấp 2 có thêm cấp cha (cấp 1); cấp 3 có thêm cấp cha (cấp 2), cờ ghi nhận chi phí qua luồng PO, tên dịch vụ và cờ dịch vụ liên quan tới phương tiện ✅ [SRS Web tr.626–627, 658–660 — UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 2, 3].

Các thay đổi đã chốt đụng tới phần này (CHG-20: cách hạch toán theo địa điểm, định mức) được ghi ở Mục 0.3, không gộp vào FR vì SRS cũ chưa có.

Ngoài phạm vi:
- Chức năng chung Export, Import, Bộ lọc, Tuỳ chỉnh cột, phân trang, popup Lịch sử hoạt động (nguồn chỉ trỏ "xem Common Rules") ✅ [SRS Web tr.582–584 — UC03.10.01 Xem danh mục chi phí cấp 1].
- Luồng đơn mua hàng hoá dịch vụ (PO) dùng chi phí cấp 3 — nguồn ghi "(Xử lý sau)" ✅ [SRS Web tr.659–660 — UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 3].
- Phân quyền chi tiết theo từng chức năng (nguồn chỉ nêu điều kiện "được phân quyền").
- Sửa, ngừng dùng, xoá khoản mục đã phê duyệt: nguồn không có (xem `gaps.md`).

## 2. Actors & Stakeholders

| Actor | Loại (người/hệ thống/ngoài) | Mục tiêu | Trong scope? | Nguồn | Nhãn |
|---|---|---|---|---|---|
| Người dùng phần mềm xưởng | người | Xem, tạo đề xuất, huỷ đề xuất, phê duyệt/từ chối khoản mục chi phí, theo quyền được cấp | Có | SRS Web tr.581, 585, 591, 598, 603 — UC03.10.01 đến UC03.10.05 (mục Tác nhân) | ✅ |
| Người dùng có quyền phê duyệt/từ chối yêu cầu cấp mới | người (vai trò theo phân quyền) | Nhận thông báo khi có yêu cầu mới/bị huỷ; phê duyệt hoặc từ chối | Có | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 (cột Đối tượng nhận thông báo) | ✅ |
| Người dùng đã tạo yêu cầu cấp mới | người | Nhận thông báo yêu cầu đã được phê duyệt hoặc bị từ chối | Có | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 (cột Đối tượng nhận thông báo) | ✅ |
| Hệ thống PMX | hệ thống | Kiểm tra dữ liệu, lưu bản ghi, sinh mã, gửi thông báo, ghi lịch sử hoạt động | Có | SRS Web tr.591, 594 — UC03.10.03 Tạo đề xuất tạo mới chi phí cấp 1 (lưu đồ hoạt động, nút Tạo mới) | ✅ |
| Lái xe | người | Chọn loại phí khi khai báo chi phí (do thay đổi CHG-20) | Không (chỉ có trong thay đổi, SRS cũ không có) | Thay đổi CHG-20 (loại phí hạch toán theo địa điểm) | 🟡 |

## 3. Functional Requirements (FR)

> Mỗi FR áp cho cả ba cấp trừ khi cột Description ghi rõ. Chi tiết khác nhau theo cấp ở bảng "Khác biệt theo cấp" bên dưới.

| ID | Title | Description | Priority | Verify by | Nguồn | Nhãn |
|---|---|---|---|---|---|---|
| FR-cost-catalog-001 | Mở danh sách khoản mục chi phí theo cấp | Người dùng đăng nhập, được phân quyền Xem của Danh mục - Chi phí cấp N, đi Dashboards > chọn tab Danh mục ở thanh điều hướng > chọn sub-tab Chi phí cấp N; hệ thống hiển thị màn hình Danh sách chi phí cấp N. Điều kiện sau: danh sách hiển thị thành công. | — | demo | SRS Web tr.581, 614, 648 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3; hình lưu đồ UC03.10.01, UC03.11.01, UC03.12.01 | ✅ |
| FR-cost-catalog-002 | Công cụ trên danh sách: tìm, nhóm, lọc, xuất, nhập, tuỳ chỉnh, phân trang | Thanh tìm kiếm tìm gần đúng trên toàn bộ bảng, trừ cột Trạng thái. Nút Nhóm cho nhóm theo các cột cho phép (khác theo cấp). Bộ lọc (sidebar) lọc theo các cột cho phép (khác theo cấp), chi tiết theo Common Rules. Nút Export, Import, Tuỳ chỉnh theo Common Rules (Tuỳ chỉnh liệt kê các trường hiển thị được, khác theo cấp). Chọn số bản ghi mỗi trang và số trang theo Common Rules. | — | demo | SRS Web tr.582–584, 615–617, 649–651 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-003 | Cột hiển thị trong danh sách | Danh sách hiển thị cột Mã CP (điều kiện có mã: xem BR-cost-catalog-015), Tên chi phí cấp N, Tên tiếng Anh, Trạng thái (xem Lưu đồ trạng thái) và cột Hành động (các hành động người dùng được phân quyền theo trạng thái). Cấp 2 thêm cột Chi phí cấp 1; cấp 3 thêm Ghi nhận PO, Tên dịch vụ, Liên quan tới phương tiện, Chi phí cấp 2. | — | demo | SRS Web tr.583, 616–617, 650–651 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-004 | Nút Tạo mới trên danh sách | Nút Tạo mới dẫn tới màn hình Tạo mới chi phí cấp N và thực hiện chức năng Tạo đề xuất tạo mới chi phí cấp N. | — | demo | SRS Web tr.583, 616, 650 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-005 | Xem thông tin chi tiết khoản mục | Từ Danh sách chi phí cấp N, nhấn vào một bản ghi mở màn hình Thông tin chi phí cấp N (hiển thị dạng khung trượt bên phải). Hiển thị: tên chi phí, mã chi phí (nếu có), trạng thái, tên tiếng Anh, ghi chú (nếu không có ghi chú thì không hiển thị), các trường riêng của cấp (Khác biệt theo cấp). Khi đã phê duyệt, ảnh hiển thị thêm dòng "ID:" dưới tên. Có biểu tượng đóng để quay lại danh sách. | — | demo | SRS Web tr.585–590, 618–624, 652–656 — UC03.10.02, UC03.11.02, UC03.12.02 Xem thông tin chi phí cấp 1, 2, 3; hình mockup tr.610, 644, 678 | ✅ |
| FR-cost-catalog-006 | Tab danh sách cấp con trong màn chi tiết | Màn chi tiết cấp 1 có 2 tab: Thông tin chung (mặc định) và Chi phí cấp 2; màn chi tiết cấp 2 có 2 tab: Thông tin chung và Chi phí cấp 3. Tab cấp con hiển thị danh sách các chi phí cấp dưới ở trạng thái phê duyệt thuộc khoản mục đang xem, có tìm kiếm gần đúng, nhóm, lọc, Export, phân trang; chọn một dòng để mở chi tiết khoản mục con. Tab cấp con có thêm cột Hành động với biểu tượng "…" (mô tả viết theo "chi phí cấp 1/2 đó"); vì tab chỉ liệt kê bản ghi đã phê duyệt nên biểu tượng này luôn rơi vào "các trạng thái còn lại: ẩn" 🔵. Cấp 3 không có tab cấp con. | — | demo | SRS Web tr.587–590, 620–624 — UC03.10.02, UC03.11.02 Xem thông tin chi phí cấp 1, 2; SRS Web tr.653–654 — UC03.12.02 Xem thông tin chi phí cấp 3 | ✅ |
| FR-cost-catalog-007 | Mở tắt lên cấp cha | Ở chi tiết cấp 2 và cấp 3, trường "Thuộc chi phí cấp 1/2" là hyperlink; khi hover có giao diện để người dùng mở tắt sang xem chi tiết khoản mục cha. | — | demo | SRS Web tr.620, 654 — UC03.11.02, UC03.12.02 Xem thông tin chi phí cấp 2, 3 | ✅ |
| FR-cost-catalog-008 | Mở popup Lịch sử hoạt động | Nút Lịch sử hoạt động trên màn chi tiết mở popup Lịch sử hoạt động của khoản mục (nội dung theo bảng Thông báo & Lịch sử hoạt động). | — | demo | SRS Web tr.590, 624, 656 — UC03.10.02, UC03.11.02, UC03.12.02 Xem thông tin chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-009 | Form tạo đề xuất tạo mới | Người dùng được phân quyền Tạo đề xuất tạo mới của chi phí cấp N mở form Tạo mới chi phí cấp N từ nút Tạo mới ở danh sách. Trường: Tên chi phí cấp N (bắt buộc, nhập ngắn), Tên tiếng Anh (nhập ngắn), Ghi chú (nhập dài), cùng các trường riêng của cấp (Khác biệt theo cấp). Nút Tạo mới, nút Huỷ và biểu tượng đóng. Lưu đồ ảnh gọi là "popup Tạo mới", bảng mô tả gọi là "Màn hình Tạo mới"; ảnh mockup là khung trượt bên phải (Conflict ở gaps.md). | — | demo | SRS Web tr.591–596, 625–630, 657–664 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-010 | Kiểm tra dữ liệu và tạo bản ghi Chờ phê duyệt | Khi nhấn Tạo mới, hệ thống kiểm tra các trường. Hợp lệ: hiển thị toast "Đề xuất tạo mới thành công", tạo 1 bản ghi chi phí cấp N trạng thái Chờ phê duyệt, hiển thị màn chi tiết với 3 hành động (theo phân quyền): Huỷ đề xuất, Phê duyệt, Từ chối. Không hợp lệ: thông báo lỗi in-line dưới trường không hợp lệ. | — | test | SRS Web tr.594–595, 628–629, 662–663 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-011 | Thông báo và lịch sử khi tạo đề xuất | Sau khi tạo thành công, hệ thống gửi thông báo tới người dùng có quyền phê duyệt/từ chối với nội dung "Chi phí cấp N - Yêu cầu cấp mới / Yêu cầu cấp mới chi phí cấp N [Tên chi phí] đang chờ phê duyệt." (nhấn thông báo dẫn tới màn Thông tin chi phí cấp N) và lưu 1 bản ghi Lịch sử hoạt động "[Tên tài khoản thực hiện hành động] hh:mm dd/mm/yyyy Đã tạo yêu cầu cấp mới". | — | test | SRS Web tr.579–580, 594, 612–613, 628, 646–647, 662 — Thông báo & Lịch sử hoạt động; UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| FR-cost-catalog-012 | Huỷ thao tác tạo mới | Nút Huỷ và biểu tượng đóng ở form Tạo mới hiển thị hộp thoại xác nhận trước khi huỷ. Xác nhận: không tạo bản ghi nào và quay về Danh sách chi phí cấp N. Huỷ (nút trong hộp thoại): quay về form Tạo mới với dữ liệu đã nhập/chọn. | — | demo | SRS Web tr.595–596, 629–630, 663–664 — UC03.10.03, UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-013 | Huỷ đề xuất tạo mới | Từ cột hành động của danh sách hoặc từ màn chi tiết, người dùng được phân quyền Huỷ đề xuất, khi bản ghi ở Chờ phê duyệt, chọn Huỷ đề xuất; hệ thống hiện popup "Huỷ đề xuất tạo mới?" . Xác nhận: trạng thái Chờ phê duyệt → Đã huỷ, toast "Huỷ đề xuất tạo chi phí cấp N thành công", đóng popup và hiển thị màn chi tiết với 2 hành động Xoá yêu cầu và Tạo mới yêu cầu. Huỷ bỏ: giữ Chờ phê duyệt, về màn chi tiết. | — | test | SRS Web tr.598–602, 632–636, 666–670 — UC03.10.04, UC03.11.04, UC03.12.04 Huỷ đề xuất cấp mới chi phí cấp 1, 2, 3; hình mockup tr.599, 633, 667 | ✅ |
| FR-cost-catalog-014 | Thông báo và lịch sử khi huỷ đề xuất | Sau khi huỷ, gửi thông báo tới người dùng có quyền phê duyệt "Chi phí cấp N - Yêu cầu cấp mới / Yêu cầu cấp mới chi phí cấp N [Tên chi phí] đã bị huỷ." và lưu lịch sử "[Tên tài khoản thực hiện hành động] hh:mm dd/mm/yyyy Đã huỷ yêu cầu cấp mới". | — | test | SRS Web tr.580, 600, 613, 634, 647, 668 — Thông báo & Lịch sử hoạt động; UC03.10.04, UC03.11.04, UC03.12.04 | ✅ |
| FR-cost-catalog-015 | Phê duyệt đề xuất | Người dùng được phân quyền Phê duyệt/Từ chối, bản ghi ở Chờ phê duyệt, chọn Phê duyệt ở cột hành động hoặc màn chi tiết; popup "Phê duyệt đề xuất tạo mới?" . Xác nhận Phê duyệt: Chờ phê duyệt → Đã phê duyệt, toast "Phê duyệt đề xuất tạo chi phí cấp N thành công", đóng popup và hiển thị màn chi tiết, sinh mã chi phí mới (BR-cost-catalog-014), gửi thông báo cho người đã tạo yêu cầu, ghi lịch sử. Huỷ (nút trong popup): giữ Chờ phê duyệt. Ở trạng thái Đã phê duyệt không có hành động thêm. | — | test | SRS Web tr.603–610, 637–644, 671–679 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-016 | Từ chối đề xuất | Chọn Từ chối: popup "Từ chối đề xuất tạo mới?" có ô nhập Lý do từ chối (nhập ngắn; có bắt buộc hay không: xem BR-cost-catalog-011). Xác nhận Từ chối: Chờ phê duyệt → Đã từ chối, toast "Từ chối đề xuất tạo chi phí cấp N thành công", đóng popup, hiển thị màn chi tiết với 2 hành động Xoá yêu cầu và Tạo mới yêu cầu, gửi thông báo cho người đã tạo yêu cầu, lưu lịch sử kèm "Lý do: [Lý do người dùng nhập]". Huỷ bỏ (nút trong popup): giữ Chờ phê duyệt. | — | test | SRS Web tr.604–607, 638–641, 672–675 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3 | ✅ |
| FR-cost-catalog-017 | Thông báo và lịch sử khi phê duyệt/từ chối | Phê duyệt: thông báo cho người đã tạo "Chi phí cấp N - Yêu cầu cấp mới / Yêu cầu cấp mới chi phí cấp N [Tên chi phí] đã được phê duyệt." + lịch sử "[Tên tài khoản thực hiện hành động] hh:mm dd/mm/yyyy Đã phê duyệt yêu cầu cấp mới". Từ chối: thông báo cho người đã tạo "Chi phí cấp N - Yêu cầu cấp mới / Yêu cầu cấp mới chi phí cấp N [Tên chi phí] đã bị từ chối." + lịch sử "[Tên tài khoản thực hiện hành động] hh:mm dd/mm/yyyy Đã từ chối yêu cầu cấp mới / Lý do: [Lý do người dùng nhập khi thực hiện hành động]". Nhấn thông báo dẫn tới màn Thông tin chi phí cấp N. | — | test | SRS Web tr.580, 606, 609, 613, 640, 643, 647, 674, 677–678 — Thông báo & Lịch sử hoạt động; UC03.10.05, UC03.11.05, UC03.12.05 | ✅ |
| FR-cost-catalog-018 | Xử lý hành động xảy ra cùng lúc | Khi Huỷ đề xuất và Phê duyệt/Từ chối xảy ra cùng thời điểm, ưu tiên Huỷ đề xuất. Nếu người phê duyệt đang ở màn Thông tin và bấm Phê duyệt/Từ chối sau khi người khác vừa huỷ, hệ thống hiện popup lỗi; bấm nút Tải lại trang để nạp lại trạng thái/thông tin mới nhất. | — | test | SRS Web tr.606, 609, 640, 643, 674, 677 — UC03.10.05, UC03.11.05, UC03.12.05 Phê duyệt/Từ chối đề xuất cấp mới chi phí cấp 1, 2, 3; hình mockup tr.606, 609 | ✅ |
| FR-cost-catalog-019 | Xoá yêu cầu đã huỷ/đã từ chối | Ở trạng thái Đã huỷ hoặc Đã từ chối, biểu tượng "…" (ở cột hành động hoặc đầu màn chi tiết) có hành động Xoá yêu cầu. Chọn: popup "Xoá yêu cầu?"; Xoá: hệ thống xoá yêu cầu, toast "Xoá yêu cầu thành công", đóng mọi popup, về Danh sách chi phí cấp N; Huỷ: về màn Thông tin chi phí cấp N. Ở màn Thông tin (khung chi tiết), khi ở các trạng thái còn lại (Chờ phê duyệt, Đã phê duyệt) ẩn biểu tượng "…" ✅. Ở Danh sách, ảnh hiện "…" ở mọi dòng kể cả Chờ phê duyệt; hành động hiện theo trạng thái và phân quyền, nguồn không nói dòng Chờ phê duyệt/Đã phê duyệt hiện gì sau "…" 🟡 (xem Gap). | — | test | SRS Web tr.589–590, 601–602, 607–608, 623–624, 635–636, 641–642, 655–656, 669–670, 675–676 — UC03.10.02, UC03.10.04, UC03.10.05 (và cấp 2, 3) | ✅ |
| FR-cost-catalog-020 | Tạo lại yêu cầu từ yêu cầu đã huỷ/đã từ chối | Chọn Tạo mới yêu cầu ở "…": hiển thị màn Tạo mới yêu cầu cấp mới, các trường lấy từ yêu cầu hiện tại; không sinh bản ghi mới mà cập nhật thông tin chỉnh sửa và đưa trạng thái về Chờ phê duyệt. Trường nào sửa được, người tạo, lịch sử, thông báo: nguồn không nói (OQ-13). | — | test | SRS Web tr.589–590, 602, 608, 623–624, 636, 642, 655–656, 670, 676 — UC03.10.02, UC03.10.04, UC03.10.05 (và cấp 2, 3) | ✅ |
| FR-cost-catalog-021 | Trạng thái và hành động cho phép | Bốn trạng thái: Chờ phê duyệt (hành động: Phê duyệt, Từ chối, Huỷ), Đã huỷ (Xoá yêu cầu, Tạo mới yêu cầu), Đã từ chối (Xoá yêu cầu, Tạo mới yêu cầu), Đã phê duyệt (không có hành động). Nút hiển thị theo phân quyền người dùng và trạng thái. | — | demo | SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục; tr.590, 624, 656 — UC03.10.02, UC03.11.02, UC03.12.02 (nút Huỷ đề xuất/Phê duyệt/Từ chối) | ✅ |
| FR-cost-catalog-022 | Chọn cấp cha khi tạo (cấp 2, cấp 3) | Cấp 2: trường "Thuộc chi phí cấp 1" (bắt buộc, danh sách thả, chọn 1 giá trị) lấy từ danh mục chi phí cấp 1 đã phê duyệt. Cấp 3: trường "Thuộc chi phí cấp 2" (bắt buộc, danh sách thả, chọn 1 giá trị) lấy từ danh mục chi phí cấp 2 đã phê duyệt. | — | test | SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 2, 3 | ✅ |
| FR-cost-catalog-023 | Khai báo ghi nhận qua PO (cấp 3) | Radio "Ghi nhận chi phí qua PO" (bắt buộc, mặc định Không, giá trị Có/Không, chọn 1). Chọn Có: hiện trường "Tên dịch vụ" (bắt buộc, nhập ngắn) để chọn tại luồng tạo đơn mua hàng hoá dịch vụ (xử lý sau). | — | test | SRS Web tr.659 — UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 3 | ✅ |
| FR-cost-catalog-024 | Khai báo dịch vụ liên quan phương tiện (cấp 3) | Radio "Dịch vụ liên quan tới phương tiện" (bắt buộc, Có/Không, chọn 1), chỉ hiển thị khi chọn Có ghi nhận chi phí qua PO. Chi phí PO liên quan phương tiện thì luồng tạo PO ghi nhận thông tin phương tiện và tính chi phí cho phương tiện đó (xử lý sau). | — | test | SRS Web tr.660 — UC03.12.03 Tạo đề xuất tạo mới chi phí cấp 3 | ✅ |

### Bảng vòng đời danh mục

| Danh mục | Tạo | Sửa | Ngừng dùng | Xoá | Nguồn | Nhãn |
|---|---|---|---|---|---|---|
| Chi phí cấp 1 | có — đề xuất tạo mới, phê duyệt mới có hiệu lực (UC03.10.03, UC03.10.05) | không có trong nguồn (chỉ có "tạo lại yêu cầu" cho yêu cầu đã huỷ/từ chối, không sửa bản ghi đã duyệt) | không có trong nguồn | có — chỉ "Xoá yêu cầu" cho bản ghi Đã huỷ/Đã từ chối; không xoá bản ghi đã phê duyệt | SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục; tr.589–590, 591–610 — UC03.10.02, UC03.10.03, UC03.10.05 | ✅ |
| Chi phí cấp 2 | có — như cấp 1 (UC03.11.03, UC03.11.05) | không có trong nguồn | không có trong nguồn | có — chỉ "Xoá yêu cầu" Đã huỷ/Đã từ chối | SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục; tr.623–624, 625–644 — UC03.11.02, UC03.11.03, UC03.11.05 | ✅ |
| Chi phí cấp 3 | có — như cấp 1 (UC03.12.03, UC03.12.05) | không có trong nguồn | không có trong nguồn | có — chỉ "Xoá yêu cầu" Đã huỷ/Đã từ chối | SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục; tr.655–656, 657–678 — UC03.12.02, UC03.12.03, UC03.12.05 | ✅ |

### Khác biệt theo cấp

| Mục con | Khác ở đâu (trường, quy tắc, câu chữ, quyền) | Nguồn | Nhãn |
|---|---|---|---|
| Danh sách — nhóm, lọc | Cấp 1: nhóm/lọc theo Trạng thái. Cấp 2: nhóm/lọc theo Chi phí cấp 1, Trạng thái. Cấp 3: nhóm/lọc theo Chi phí cấp 2, Ghi nhận PO, Dịch vụ liên quan tới phương tiện, Trạng thái. | SRS Web tr.582, 615, 649–650 — UC03.10.01, UC03.11.01, UC03.12.01 Xem danh mục chi phí cấp 1, 2, 3 | ✅ |
| Danh sách — trường trong Tuỳ chỉnh | Cấp 1: Mã CP, Tên chi phí cấp 1, Tên tiếng Anh, Trạng thái. Cấp 2: thêm Chi phí cấp 1. Cấp 3: Mã CP, Tên chi phí cấp 3, Tên tiếng Anh, Ghi nhận PO, Tên dịch vụ, Dịch vụ liên quan tới phương tiện, Chi phí cấp 2, Trạng thái. | SRS Web tr.583, 616, 650 — UC03.10.01, UC03.11.01, UC03.12.01 | ✅ |
| Danh sách — cột | Cấp 1: Mã CP, Tên chi phí cấp 1, Tên tiếng Anh, Trạng thái, Hành động. Cấp 2: thêm cột Chi phí cấp 1 (cấp cha). Cấp 3: thêm Ghi nhận PO, Tên dịch vụ, Liên quan tới phương tiện, Chi phí cấp 2 (cấp cha). Ảnh danh sách cấp 3 chỉ thấy Ghi nhận PO trong các cột mới. | SRS Web tr.583, 616–617, 650–651 — UC03.10.01, UC03.11.01, UC03.12.01; hình mockup tr.649 | ✅ |
| Chi tiết — trường riêng | Cấp 1: Tên tiếng Anh, Ghi chú. Cấp 2: thêm "Thuộc chi phí cấp 1" (hyperlink). Cấp 3: thêm Ghi nhận PO, Tên dịch vụ (khi được ghi nhận qua PO), Liên quan đến phương tiện, "Thuộc chi phí cấp 2" (hyperlink), Trạng thái. | SRS Web tr.587, 620, 653–654 — UC03.10.02, UC03.11.02, UC03.12.02 | ✅ |
| Chi tiết — tab con | Cấp 1: tab "Chi phí cấp 2" (cột Mã chi phí, Tên chi phí cấp 2; nhóm/lọc theo Trạng thái). Cấp 2: tab "Chi phí cấp 3" (nhóm/lọc theo Ghi nhận PO, Dịch vụ liên quan tới phương tiện, Trạng thái; ảnh thấy cột Mã CP, Tên chi phí cấp 3). Cấp 3: không có tab. | SRS Web tr.588, 621–622, 653 — UC03.10.02, UC03.11.02, UC03.12.02 | ✅ |
| Form tạo — trường | Cấp 1: Tên cấp 1*, Tên tiếng Anh, Ghi chú. Cấp 2: Tên cấp 2*, Tên tiếng Anh, Thuộc chi phí cấp 1*, Ghi chú. Cấp 3: Tên cấp 3*, Tên tiếng Anh, Ghi nhận chi phí qua PO*, Tên dịch vụ* (khi Có), Dịch vụ liên quan tới phương tiện* (khi Có), Thuộc chi phí cấp 2*, Ghi chú. | SRS Web tr.592–593, 626–627, 658–661 — UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| Validate tên | Cả ba cấp: tên bắt buộc và phải unique, lỗi "Tên chi phí này đã bị trùng." (phạm vi unique chưa nói, OQ-1). | SRS Web tr.592, 626, 658 — UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| Quan hệ cha-con | Cấp 1: không có cha. Cấp 2: thuộc đúng 1 cấp 1 đã phê duyệt. Cấp 3: thuộc đúng 1 cấp 2 đã phê duyệt. Cấp cha chọn lúc tạo; nguồn không có sửa cấp cha sau đó. | SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 | ✅ |
| Mã chi phí sinh khi phê duyệt | Cấp 1: định dạng aa (01–99). Cấp 2: xxaa (xx = mã cấp 1 cha; aa 01–99). Cấp 3: xxaabbb (xx = mã cấp 1; aa = mã cấp 2; bbb 001–999 tăng dần khi xx và aa trùng nhau). | SRS Web tr.609, 643, 677 — UC03.10.05, UC03.11.05, UC03.12.05 | ✅ |
| Câu chữ toast/thông báo | Chỉ khác số cấp trong câu (cấp 1/2/3). Không khác cấu trúc. | SRS Web tr.600, 606, 609, 634, 640, 643, 668, 674, 677 — UC03.10.04, UC03.10.05 (và cấp 2, 3) | ✅ |
| Quyền | Mỗi cấp có quyền riêng: Xem; Tạo đề xuất tạo mới; Huỷ đề xuất tạo mới; Phê duyệt/Từ chối đề xuất tạo mới của Danh mục - Chi phí cấp N. Không nêu khác biệt thêm giữa các cấp. | SRS Web tr.581, 585, 591, 598, 603 — điều kiện trước UC03.10.01 đến UC03.10.05 (và cấp 2, 3) | ✅ |
| Thông báo & Lịch sử hoạt động | Không khác ngoài tên cấp trong câu chữ; cả ba cấp có 4 dòng giống nhau (tạo, huỷ, phê duyệt, từ chối). | SRS Web tr.579–580, 612–613, 646–647 — Thông báo & Lịch sử hoạt động Chi phí cấp 1, 2, 3 | ✅ |
| Lưu đồ hoạt động xem chi tiết | Cấp 1: vào từ Danh sách chi phí cấp 1. Cấp 2 và cấp 3: vào từ danh sách cùng cấp hoặc từ tab cấp con trong chi tiết cấp cha (Danh mục\Danh sách chi phí cấp N hoặc Thông tin chi phí cấp N-1\Danh sách cấp N). | SRS Web tr.585, 618, 652 — hình lưu đồ UC03.10.02, UC03.11.02, UC03.12.02 | ✅ |

## 4. Non-Functional Requirements (NFR)

| ID | Category | Requirement | Priority | Acceptance | Nguồn | Nhãn |
|---|---|---|---|---|---|---|
| NFR-cost-catalog-001 | usability | Thanh tìm kiếm tìm gần đúng trên toàn bộ bảng (danh sách chính trừ cột Trạng thái; tab cấp con không nêu ngoại lệ). | — | Nhập một phần tên vẫn ra kết quả | SRS Web tr.582, 588, 621 — UC03.10.01, UC03.10.02, UC03.11.02 | ✅ |
| NFR-cost-catalog-002 | usability | Mọi thời điểm ghi trong Lịch sử hoạt động theo định dạng hh:mm dd/mm/yyyy kèm tên tài khoản thực hiện. | — | Kiểm tra dòng lịch sử | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 | ✅ |
| NFR-cost-catalog-003 | usability | Danh sách phân trang với lựa chọn số bản ghi mỗi trang; ảnh mặc định 50 bản ghi/trang. | — | Chọn được số bản ghi | SRS Web tr.584, 617, 651 — UC03.10.01, UC03.11.01, UC03.12.01; hình mockup tr.582 | 🟡 |
| NFR-cost-catalog-004 | consistency | Mọi hành động đổi trạng thái đều có popup xác nhận, toast kết quả và quay về màn chi tiết/danh sách theo đặc tả. | — | Kiểm từng hành động | SRS Web tr.599–601, 604–609, 633–635, 638–643, 667–669, 672–677 — UC03.10.04, UC03.10.05 (và cấp 2, 3) | ✅ |
| NFR-cost-catalog-005 | data-consistency | Trường hợp xung đột thao tác, ưu tiên Huỷ đề xuất và buộc người dùng tải lại trang để lấy trạng thái mới. | — | Mô phỏng 2 người dùng cùng lúc | SRS Web tr.606, 609, 640, 643, 674, 677 — UC03.10.05, UC03.11.05, UC03.12.05 | ✅ |

## 5. Business Rules

| ID | Rule | Trigger | Implements FR | Nguồn | Nhãn |
|---|---|---|---|---|---|
| BR-cost-catalog-001 | Khoản mục chi phí có 3 cấp; cấp 2 thuộc cấp 1, cấp 3 thuộc cấp 2. | Tạo cấp 2, cấp 3 | FR-cost-catalog-022 | SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 | ✅ |
| BR-cost-catalog-002 | Mọi bản ghi mới tạo ra có trạng thái Chờ phê duyệt; chưa có hiệu lực cho tới khi được phê duyệt. | Nhấn Tạo mới hợp lệ | FR-cost-catalog-010 | SRS Web tr.284, 591 — Lưu đồ trạng thái chung cho danh mục; UC03.10.03 Điều kiện sau | ✅ |
| BR-cost-catalog-003 | Tên chi phí (mỗi cấp) bắt buộc và phải unique; trùng → lỗi "Tên chi phí này đã bị trùng." | Nhấn Tạo mới | FR-cost-catalog-010 | SRS Web tr.592, 626, 658 — UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| BR-cost-catalog-004 | Tên tiếng Anh và Ghi chú không bắt buộc. | Nhập form | FR-cost-catalog-009 | SRS Web tr.592–593, 626–627, 658–661 — UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| BR-cost-catalog-005 | Cấp cha khi tạo cấp 2 chỉ lấy từ chi phí cấp 1 ở trạng thái Đã phê duyệt; chọn 1 giá trị. | Mở form tạo cấp 2 | FR-cost-catalog-022 | SRS Web tr.627 — UC03.11.03 | ✅ |
| BR-cost-catalog-006 | Cấp cha khi tạo cấp 3 chỉ lấy từ chi phí cấp 2 ở trạng thái Đã phê duyệt; chọn 1 giá trị. | Mở form tạo cấp 3 | FR-cost-catalog-022 | SRS Web tr.660 — UC03.12.03 | ✅ |
| BR-cost-catalog-007 | Cấp 3: "Ghi nhận chi phí qua PO" bắt buộc, mặc định Không; Tên dịch vụ chỉ hiện và bắt buộc khi chọn Có. | Chọn radio PO | FR-cost-catalog-023 | SRS Web tr.659 — UC03.12.03 | ✅ |
| BR-cost-catalog-008 | Cấp 3: "Dịch vụ liên quan tới phương tiện" bắt buộc, chỉ hiện khi chọn Có ghi nhận qua PO; giá trị Có/Không, chọn 1. | Chọn Có ở PO | FR-cost-catalog-024 | SRS Web tr.660 — UC03.12.03 | ✅ |
| BR-cost-catalog-009 | Chỉ khi ở trạng thái Chờ phê duyệt mới được Huỷ đề xuất, Phê duyệt, Từ chối. | Chọn hành động | FR-cost-catalog-013, FR-cost-catalog-015, FR-cost-catalog-016 | SRS Web tr.284, 598, 603 — Lưu đồ trạng thái chung; điều kiện trước UC03.10.04, UC03.10.05 | ✅ |
| BR-cost-catalog-010 | Chỉ người được phân quyền chức năng tương ứng (Xem, Tạo đề xuất, Huỷ đề xuất, Phê duyệt/Từ chối) mới thực hiện hoặc thấy nút. | Mở màn / chọn hành động | FR-cost-catalog-021 | SRS Web tr.581, 585, 591, 598, 603 — điều kiện trước UC03.10.01 đến UC03.10.05 (và cấp 2, 3) | ✅ |
| BR-cost-catalog-011 | Lý do từ chối: bảng trường ghi Bắt buộc = Không; nếu nhập thì ghi vào Lịch sử hoạt động. Ảnh popup lại ghi "Vui lòng nhập lý do từ chối." (Conflict ở gaps.md). | Từ chối | FR-cost-catalog-016 | SRS Web tr.605–606, 639–640, 673–674 — UC03.10.05, UC03.11.05, UC03.12.05; hình mockup tr.604, 638, 672 | 🟡 |
| BR-cost-catalog-012 | Huỷ đề xuất chuyển Chờ phê duyệt → Đã huỷ; Từ chối chuyển → Đã từ chối; Phê duyệt chuyển → Đã phê duyệt. | Xác nhận trong popup | FR-cost-catalog-013, FR-cost-catalog-015, FR-cost-catalog-016 | SRS Web tr.284, 600, 606, 609 — Lưu đồ trạng thái chung; UC03.10.04, UC03.10.05 | ✅ |
| BR-cost-catalog-013 | Nút Huỷ bỏ/Huỷ trong popup xác nhận giữ nguyên trạng thái Chờ phê duyệt và quay về màn chi tiết. | Bấm Huỷ bỏ/Huỷ | FR-cost-catalog-013, FR-cost-catalog-015, FR-cost-catalog-016 | SRS Web tr.601, 607, 610 — UC03.10.04, UC03.10.05 | ✅ |
| BR-cost-catalog-014 | Mã chi phí chỉ sinh khi phê duyệt: cấp 1 = aa (01–99, tăng dần); cấp 2 = xxaa (xx mã cấp 1 cha; aa 01–99 tăng dần); cấp 3 = xxaabbb (xx mã cấp 1; aa mã cấp 2; bbb 001–999 tăng dần khi xx và aa trùng nhau). | Phê duyệt | FR-cost-catalog-015 | SRS Web tr.609, 643, 677 — UC03.10.05, UC03.11.05, UC03.12.05 | ✅ |
| BR-cost-catalog-015 | Theo mô tả: cột Mã CP trong danh sách chỉ có khi ở trạng thái phê duyệt; Mã chi phí ở chi tiết hiển thị "nếu có". Ảnh danh sách lại hiện mã ở dòng Chờ phê duyệt (Conflict ở gaps.md). | Xem danh sách/chi tiết | FR-cost-catalog-003, FR-cost-catalog-005 | SRS Web tr.583, 587 — UC03.10.01, UC03.10.02; hình mockup tr.582 | 🟡 |
| BR-cost-catalog-016 | Tab cấp con trong chi tiết chỉ liệt kê các khoản mục con ở trạng thái đã phê duyệt. | Mở tab cấp con | FR-cost-catalog-006 | SRS Web tr.588, 621 — UC03.10.02, UC03.11.02 | ✅ |
| BR-cost-catalog-017 | Ghi chú rỗng thì không hiển thị trên màn chi tiết. | Xem chi tiết | FR-cost-catalog-005 | SRS Web tr.587, 620, 654 — UC03.10.02, UC03.11.02, UC03.12.02 | ✅ |
| BR-cost-catalog-018 | Khi Huỷ và Phê duyệt/Từ chối xảy ra cùng lúc: ưu tiên Huỷ. | Xung đột đồng thời | FR-cost-catalog-018 | SRS Web tr.606, 609 — UC03.10.05 | ✅ |
| BR-cost-catalog-019 | Thông báo tạo mới và thông báo huỷ chỉ hiển thị cho người có quyền phê duyệt/từ chối. | Sau khi tạo / huỷ | FR-cost-catalog-011, FR-cost-catalog-014 | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 | ✅ |
| BR-cost-catalog-020 | Thông báo phê duyệt và thông báo từ chối chỉ hiển thị cho người đã tạo yêu cầu cấp mới. | Sau khi phê duyệt / từ chối | FR-cost-catalog-017 | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 | ✅ |
| BR-cost-catalog-021 | Nhấn thông báo dẫn tới màn Thông tin chi phí cấp N tương ứng. | Nhấn thông báo | FR-cost-catalog-011, FR-cost-catalog-014, FR-cost-catalog-017 | SRS Web tr.580, 613, 647 — Thông báo & Lịch sử hoạt động | ✅ |
| BR-cost-catalog-022 | Ở Đã huỷ / Đã từ chối: được Xoá yêu cầu hoặc Tạo mới yêu cầu (bảng trạng thái chung). Màn Thông tin (khung chi tiết): biểu tượng "…" chỉ hiện ở Đã huỷ/Đã từ chối, các trạng thái còn lại ẩn. Danh sách: ảnh hiện "…" ở mọi dòng, nguồn không nói ẩn theo trạng thái. | Xem chi tiết | FR-cost-catalog-019, FR-cost-catalog-020, FR-cost-catalog-021 | SRS Web tr.284, 589–590 — Lưu đồ trạng thái chung; UC03.10.02; hình mockup tr.582, 596, 601, 610 | ✅ |
| BR-cost-catalog-023 | Tạo lại yêu cầu từ bản ghi đã huỷ/từ chối cập nhật chính bản ghi đó (không sinh bản ghi mới) và đưa về Chờ phê duyệt. | Chọn Tạo mới yêu cầu | FR-cost-catalog-020 | SRS Web tr.602, 608, 636, 642, 670, 676 — UC03.10.04, UC03.10.05 (và cấp 2, 3) | ✅ |
| BR-cost-catalog-024 | Mỗi hành động đổi trạng thái đều ghi 1 bản ghi Lịch sử hoạt động: "[Tên tài khoản thực hiện hành động] hh:mm dd/mm/yyyy" + một trong "Đã tạo yêu cầu cấp mới" / "Đã huỷ yêu cầu cấp mới" / "Đã phê duyệt yêu cầu cấp mới" / "Đã từ chối yêu cầu cấp mới" (từ chối kèm "Lý do: [Lý do người dùng nhập khi thực hiện hành động]"). | Sau mỗi hành động | FR-cost-catalog-011, FR-cost-catalog-014, FR-cost-catalog-017 | SRS Web tr.580, 594, 600, 606, 609 — Thông báo & Lịch sử hoạt động; UC03.10.03 đến UC03.10.05 | ✅ |
| BR-cost-catalog-025 | Nút Huỷ và biểu tượng đóng ở form Tạo mới đều hỏi xác nhận; Xác nhận bỏ toàn bộ dữ liệu đã nhập, không tạo bản ghi. | Đóng form tạo | FR-cost-catalog-012 | SRS Web tr.595–596, 629–630, 663–664 — UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| BR-cost-catalog-026 | Cấp 3 gắn với luồng PO: chi phí ghi nhận qua PO thì người dùng chọn dịch vụ này ở luồng tạo đơn mua hàng hoá dịch vụ (xử lý sau); liên quan phương tiện thì luồng PO ghi nhận phương tiện và tính chi phí cho phương tiện. | Tạo PO (ngoài phạm vi) | FR-cost-catalog-023, FR-cost-catalog-024 | SRS Web tr.659–660 — UC03.12.03 | 🟡 |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery | Nguồn | Nhãn |
|---|---|---|---|---|---|---|---|---|
| E-cost-catalog-001 | Tên chi phí trùng | Tên chi phí đã tồn tại khi nhấn Tạo mới | minor | FR-cost-catalog-010 | Form Tạo mới (lỗi in-line dưới trường tên) | Đổi tên. Câu chữ: "Tên chi phí này đã bị trùng." | SRS Web tr.592, 626, 658 — UC03.10.03, UC03.11.03, UC03.12.03 | ✅ |
| E-cost-catalog-002 | Đề xuất đã bị huỷ khi duyệt/từ chối | Người phê duyệt bấm Phê duyệt/Từ chối sau khi người khác vừa huỷ | major | FR-cost-catalog-018 | Popup lỗi | Nút "Tải lại trang". Câu chữ ảnh: "Lỗi! Đề xuất tạo mới này đã bị huỷ. Vui lòng tải lại trang để cập nhật." | SRS Web tr.606, 609 — UC03.10.05 (ảnh popup lỗi); mô tả bảng nói "popup thông báo lỗi" | ✅ |
| E-cost-catalog-003 | Thiếu tên chi phí | Để trống Tên chi phí (trường bắt buộc) | minor | FR-cost-catalog-010 | Form Tạo mới | Nhập tên. Câu chữ lỗi không có trong nguồn | SRS Web tr.592, 626, 658 — UC03.10.03, UC03.11.03, UC03.12.03 (trường bắt buộc); tr.595 — in-line error msg | 🟡 |
| E-cost-catalog-004 | Thiếu cấp cha | Không chọn "Thuộc chi phí cấp 1/2" (cấp 2, 3) | minor | FR-cost-catalog-022 | Form Tạo mới | Chọn cấp cha. Câu chữ lỗi không có trong nguồn | SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 (trường bắt buộc) | 🟡 |
| E-cost-catalog-005 | Thiếu dữ liệu PO (cấp 3) | Ghi nhận PO = Có nhưng để trống Tên dịch vụ hoặc Dịch vụ liên quan tới phương tiện | minor | FR-cost-catalog-023, FR-cost-catalog-024 | Form Tạo mới cấp 3 | Nhập đủ. Câu chữ lỗi không có trong nguồn | SRS Web tr.659–660 — UC03.12.03 | 🟡 |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt | Nguồn | Nhãn |
|---|---|---|---|---|---|
| SC-cost-catalog-01 | Người dùng được phân quyền mở được danh sách và chi tiết khoản mục ở mỗi cấp | Kiểm tra theo điều kiện sau UC xem | Danh sách/chi tiết hiển thị thành công | SRS Web tr.581, 585, 614, 618, 648, 652 — UC03.10.01, UC03.10.02 (và cấp 2, 3) | ✅ |
| SC-cost-catalog-02 | Tạo đề xuất cho ra 1 bản ghi Chờ phê duyệt, có toast, thông báo, lịch sử | Kiểm tra sau khi tạo | Đủ 3 kết quả | SRS Web tr.591, 625, 657 — UC03.10.03, UC03.11.03, UC03.12.03 (Điều kiện sau) | ✅ |
| SC-cost-catalog-03 | Huỷ đề xuất chuyển bản ghi sang Đã huỷ | Kiểm tra trạng thái | Chờ phê duyệt → Đã huỷ | SRS Web tr.598, 632, 666 — UC03.10.04, UC03.11.04, UC03.12.04 (Điều kiện sau) | ✅ |
| SC-cost-catalog-04 | Phê duyệt/Từ chối chuyển bản ghi sang Đã phê duyệt/Đã từ chối | Kiểm tra trạng thái | Chuyển đúng, có toast | SRS Web tr.603, 637, 671 — UC03.10.05, UC03.11.05, UC03.12.05 (Điều kiện sau) | ✅ |
| SC-cost-catalog-05 | Khoản mục đã phê duyệt được cấp mã đúng định dạng của cấp | Kiểm tra mã | aa / xxaa / xxaabbb | SRS Web tr.609, 643, 677 — UC03.10.05, UC03.11.05, UC03.12.05 | ✅ |

## 8. Data Entities (tóm tắt — chi tiết ở `srs/cost-catalog-reverse-erd.md`)

| Đối tượng | Loại | Mô tả | Nguồn | Nhãn |
|---|---|---|---|---|
| Chi phí cấp 1 | Danh mục | Khoản mục chi phí gốc: tên, tên tiếng Anh, ghi chú, mã (aa), trạng thái | SRS Web tr.587, 609 — UC03.10.02, UC03.10.05 | ✅ |
| Chi phí cấp 2 | Danh mục | Khoản mục con của cấp 1: thêm cấp cha (cấp 1), mã (xxaa) | SRS Web tr.620, 643 — UC03.11.02, UC03.11.05 | ✅ |
| Chi phí cấp 3 | Danh mục | Khoản mục con của cấp 2: thêm cấp cha, ghi nhận qua PO, tên dịch vụ, liên quan phương tiện, mã (xxaabbb) | SRS Web tr.653–654, 677 — UC03.12.02, UC03.12.05 | ✅ |
| Đề xuất tạo mới khoản mục (Yêu cầu cấp mới) | Yêu cầu thay đổi (ChangeRequest) | Đề xuất tạo mới 1 khoản mục, qua phê duyệt/từ chối/huỷ mới có hiệu lực. Nguồn không tách thành bản ghi riêng: chính bản ghi khoản mục mang trạng thái Chờ phê duyệt/Đã huỷ/Đã từ chối (UC03.10.03 Điều kiện sau: "tạo 1 bản ghi với trạng thái Chờ phê duyệt"; tr.602, 608: tạo lại không sinh bản ghi mới). Phân loại ChangeRequest là cách xếp, chưa có xác nhận | SRS Web tr.284, 591, 602, 608, 625, 657 — Lưu đồ trạng thái chung; UC03.10.03 (Điều kiện sau) | 🟡 |
| Thông báo | Khác (thông báo cho người dùng) | Thông báo 4 loại: đang chờ phê duyệt, đã bị huỷ, đã được phê duyệt, đã bị từ chối | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 | ✅ |
| Lịch sử hoạt động | Khác (nhật ký thao tác) | Dòng: tài khoản + giờ ngày + hành động (+ lý do từ chối) | SRS Web tr.580 — Thông báo & Lịch sử hoạt động Chi phí cấp 1 | ✅ |
| Đơn mua hàng hoá dịch vụ (PO) | Chứng từ nghiệp vụ (BusinessDocument) | Chứng từ ngoài phần này, nơi chọn dịch vụ của chi phí cấp 3 (xử lý sau) | SRS Web tr.659 — UC03.12.03 | 🟡 |
| Phương tiện | Danh mục | Danh mục ngoài phần này; chi phí cấp 3 "liên quan phương tiện" dẫn tới việc ghi nhận phương tiện ở PO | SRS Web tr.660 — UC03.12.03 | 🟡 |
| Bảng loại phí × địa điểm → cách hạch toán, định mức | Danh mục | Bảng mới do CHG-20, chưa có trong SRS cũ | Thay đổi CHG-20 (loại phí hạch toán theo địa điểm) | 🟡 |

Chi tiết ở `erd.md`.

## 9. Flows (tóm tắt — chi tiết ở `srs/cost-catalog-reverse-flows.md`)

- **Xem danh sách khoản mục chi phí (cấp 1, 2, 3)** — Dashboards > Danh mục > sub-tab > danh sách ✅ [SRS Web tr.581, 614, 648 — hình lưu đồ UC03.10.01, UC03.11.01, UC03.12.01].
- **Xem thông tin khoản mục chi phí** — chọn 1 bản ghi (từ danh sách hoặc tab cấp con) > màn thông tin ✅ [SRS Web tr.585, 618, 652 — hình lưu đồ UC03.10.02, UC03.11.02, UC03.12.02].
- **Tạo đề xuất tạo mới** — mở form > nhập > kiểm tra > toast + lưu > thông báo + lịch sử > màn chi tiết ✅ [SRS Web tr.591, 625, 657 — hình lưu đồ UC03.10.03, UC03.11.03, UC03.12.03].
- **Huỷ đề xuất** — Huỷ đề xuất > popup xác nhận > toast + lưu trạng thái + lịch sử + thông báo ✅ [SRS Web tr.598, 632, 666 — hình lưu đồ UC03.10.04, UC03.11.04, UC03.12.04].
- **Phê duyệt / Từ chối đề xuất** — chọn Phê duyệt hoặc Từ chối > popup > toast + lưu + lịch sử + thông báo (+ sinh mã nếu duyệt, + xử lý xung đột) ✅ [SRS Web tr.604, 638, 672 — hình lưu đồ UC03.10.05, UC03.11.05, UC03.12.05].
- **Xoá yêu cầu / Tạo lại yêu cầu từ bản đã huỷ/từ chối** — theo mô tả chữ, không có lưu đồ riêng ✅ [SRS Web tr.589–590, 601–602, 607–608 — UC03.10.02, UC03.10.04, UC03.10.05].

## 10. Screens

- **Danh sách chi phí cấp 1** — xem, tìm, nhóm, lọc, Export, Import, Tuỳ chỉnh, Tạo mới, phân trang — cột Mã CP, Tên chi phí cấp 1, Tên tiếng Anh, Trạng thái, Hành động (…) — thấy thêm hàng lọc theo cột (mã, tên, tên tiếng Anh, trạng thái) trên ảnh — nhóm/lọc: Trạng thái; Export, Import, Tuỳ chỉnh theo Common Rules; không phải báo cáo, bộ lọc cố định theo cột cho phép, cột hiển thị chọn được qua Tuỳ chỉnh ✅ [SRS Web tr.581–584 — UC03.10.01; hình mockup tr.582].
- **Danh sách chi phí cấp 2** — như trên, thêm cột Chi phí cấp 1; nhóm/lọc: Chi phí cấp 1, Trạng thái ✅ [SRS Web tr.614–617 — UC03.11.01; hình mockup tr.615].
- **Danh sách chi phí cấp 3** — như trên, thêm cột Ghi nhận PO, Tên dịch vụ, Liên quan tới phương tiện, Chi phí cấp 2; nhóm/lọc: Chi phí cấp 2, Ghi nhận PO, Dịch vụ liên quan tới phương tiện, Trạng thái ✅ [SRS Web tr.648–651 — UC03.12.01; hình mockup tr.649].
- **Thông tin chi phí cấp 1** — khung trượt phải: tiêu đề, tên, trạng thái, nút Phê duyệt/Từ chối/Huỷ đề xuất (khi Chờ phê duyệt), nút "…" (Đã huỷ/Đã từ chối), tab Thông tin chung / Chi phí cấp 2, nút Lịch sử hoạt động (nút tròn dưới phải trên ảnh), biểu tượng đóng ✅ [SRS Web tr.585–590 — UC03.10.02; hình mockup tr.586, 596, 601, 607, 610].
- **Thông tin chi phí cấp 2** — như trên, thêm "Thuộc chi phí cấp 1" (hyperlink); tab Thông tin chung / Chi phí cấp 3 ✅ [SRS Web tr.618–624 — UC03.11.02; hình mockup tr.619, 630, 635, 641, 644].
- **Thông tin chi phí cấp 3** — như trên, không có tab; thêm Ghi nhận chi phí qua PO, Tên dịch vụ, Dịch vụ liên quan tới phương tiện, "Thuộc chi phí cấp 2" ✅ [SRS Web tr.652–656 — UC03.12.02; hình mockup tr.653, 664, 669, 675, 678].
- **Tạo mới chi phí cấp 1** — khung trượt phải: Tên chi phí cấp 1*, Tên tiếng Anh, Ghi chú; nút Huỷ, Tạo mới, biểu tượng đóng ✅ [SRS Web tr.591–597 — UC03.10.03; hình mockup tr.592].
- **Tạo mới chi phí cấp 2** — Tên cấp 2*, Tên tiếng Anh, Thuộc chi phí cấp 1*, Ghi chú ✅ [SRS Web tr.625–631 — UC03.11.03; hình mockup tr.626].
- **Tạo mới chi phí cấp 3** — Tên cấp 3*, Tên tiếng Anh, Ghi nhận chi phí qua PO*, Tên dịch vụ*, Dịch vụ có liên quan tới phương tiện không?, Thuộc chi phí cấp 2*, Ghi chú ✅ [SRS Web tr.657–665 — UC03.12.03; hình mockup tr.658].
- **Popup "Huỷ tạo mới?"** — "Bạn có chắc chắn muốn huỷ quá trình tạo mới này không? Tất cả thông tin đã nhập sẽ bị mất."; nút Huỷ, Xác nhận ✅ [SRS Web tr.595–596 — UC03.10.03; hình mockup tr.595, 596, 629, 630, 663, 664].
- **Popup "Huỷ đề xuất tạo mới?"** — "Bạn có chắc chắn muốn huỷ đề xuất này không?"; nút Huỷ bỏ, Xác nhận ✅ [SRS Web tr.599–601 — UC03.10.04; hình mockup tr.599, 633, 667].
- **Popup "Từ chối đề xuất tạo mới?"** — "Bạn có chắc chắn muốn từ chối duyệt tạo mới này? Vui lòng nhập lý do từ chối."; ô "Nhập lý do từ chối tạo mới..."; nút Huỷ bỏ, Từ chối ✅ [SRS Web tr.604–607 — UC03.10.05; hình mockup tr.604, 638, 672].
- **Popup "Phê duyệt đề xuất tạo mới?"** — "Bạn có muốn phê duyệt đề xuất tạo mới này?"; nút Huỷ, Phê duyệt ✅ [SRS Web tr.608–610 — UC03.10.05; hình mockup tr.608, 642, 676].
- **Popup "Xoá yêu cầu?"** — "Bạn có chắc chắn muốn xoá yêu cầu này không?"; nút Huỷ, Xoá ✅ [SRS Web tr.589, 601, 607 — UC03.10.02, UC03.10.04, UC03.10.05; hình mockup tr.589, 602, 608].
- **Popup lỗi "Lỗi!"** — "Đề xuất tạo mới này đã bị huỷ. Vui lòng tải lại trang để cập nhật."; nút Tải lại trang ✅ [SRS Web tr.606, 609 — UC03.10.05; hình mockup tr.606, 609].
- **Popup Lịch sử hoạt động** — theo bảng Thông báo & Lịch sử hoạt động; không có ảnh riêng trong lát 🟡 [SRS Web tr.590 — UC03.10.02].
- **Thông báo** — 4 loại thông báo (tạo, huỷ, phê duyệt, từ chối), nhấn dẫn tới Thông tin chi phí cấp N ✅ [SRS Web tr.579–580, 612–613, 646–647 — Thông báo & Lịch sử hoạt động].

Báo cáo / dashboard: phần này không có báo cáo hay dashboard; danh sách chỉ có Export/Import theo Common Rules (xem Gap trong `gaps.md`).

## 11. Constraints, Dependencies & Assumptions

__Constraints (ràng buộc áp đặt):__

| Ràng buộc | Source / Owner | Nguồn | Nhãn |
|---|---|---|---|
| Danh mục dùng một lưu đồ trạng thái chung cho mọi danh mục (Chờ phê duyệt, Đã huỷ, Đã từ chối, Đã phê duyệt) | SRS Web (Epic 03 - Danh mục) | SRS Web tr.284 — Lưu đồ trạng thái chung cho danh mục | ✅ |
| Cây 3 cấp: cấp 3 → cấp 2 → cấp 1 | SRS Web | SRS Web tr.627, 660 — UC03.11.03, UC03.12.03 | ✅ |
| Định dạng mã bị giới hạn: cấp 1 tối đa 99, cấp 2 tối đa 99 trong mỗi cấp 1, cấp 3 tối đa 999 trong mỗi cặp cấp 1-cấp 2 | SRS Web | SRS Web tr.609, 643, 677 — UC03.10.05, UC03.11.05, UC03.12.05 | 🔵 |

__Dependencies (deliverable do bên khác sở hữu):__

| Phụ thuộc | Owner | Blocks nếu chưa sẵn | Nguồn | Nhãn |
|---|---|---|---|---|
| Common Rules (Export, Import, Bộ lọc, Tuỳ chỉnh, phân trang, Lịch sử hoạt động) | SRS Web (phần Common Rules) | Chức năng danh sách và popup lịch sử | SRS Web tr.582–584 — UC03.10.01 | ✅ |
| Luồng đơn mua hàng hoá dịch vụ (PO) | Phần PO (xử lý sau) | Cấp 3 gắn "ghi nhận qua PO" chưa dùng được | SRS Web tr.659–660 — UC03.12.03 | 🟡 |
| Danh mục phương tiện | Phần Phương tiện | Cấp 3 "liên quan phương tiện" | SRS Web tr.660 — UC03.12.03 | 🟡 |
| Phân quyền người dùng (Xem, Tạo đề xuất, Huỷ đề xuất, Phê duyệt/Từ chối theo từng cấp) | Quản trị hệ thống | Mọi UC của phần này | SRS Web tr.581, 585, 591, 598, 603 — điều kiện trước UC03.10.01 đến UC03.10.05 | ✅ |

__Assumptions (tin là đúng — nêu hệ quả nếu sai):__

| Giả định | Invalidate {X} nếu sai | Nguồn | Nhãn |
|---|---|---|---|
| Màn hình cấp 1, 2, 3 theo cùng khuôn nên chỗ UC cấp 1 nhắc "cấp 2" là chép nhầm | Bảng Khác biệt theo cấp | SRS Web tr.585, 601–602 — UC03.10.02, UC03.10.04 | 🔵 |

## 12. Open Questions

> Danh sách đầy đủ OQ + Gap ở [`reverse-gaps.md`](./reverse-gaps.md). Dưới đây chỉ trích các OQ chặn tiến độ.

- [ ] OQ-1: Tên chi phí phải unique trong phạm vi nào (toàn cấp, trong cùng cấp cha, có tính bản ghi Đã huỷ/Đã từ chối không)?
- [ ] OQ-2: Người tạo đề xuất có được tự phê duyệt đề xuất của mình không?
- [ ] OQ-3: Khoản mục đã phê duyệt có được sửa, ngừng dùng hoặc xoá không (SRS cũ không có UC)?
- [ ] OQ-4: "Xoá yêu cầu" xoá hẳn hay ẩn; lịch sử hoạt động có còn không?
- [ ] OQ-5: Mã chi phí vượt giới hạn (cấp 1 quá 99, cấp 2 quá 99, cấp 3 quá 999) xử lý thế nào?
- [ ] OQ-6: Import danh mục có phải qua phê duyệt không, quy tắc kiểm tra trùng thế nào?
- [ ] OQ-7: Ma trận phân quyền chi tiết cho từng cấp và từng hành động?
- [ ] OQ-8: CHG-20 — các tuyến ngoài đường sắt, bảng loại phí × địa điểm → cách hạch toán, định mức (OQ-31)?
