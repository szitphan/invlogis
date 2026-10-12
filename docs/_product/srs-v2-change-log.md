---
type: change-log
status: draft
updated: 2026-10-12
jira_key:
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs-input/srs-cu/srs-mobile/srs-mobile.md
  - design/design.md
  - design/ui-common/conventions.md
  - design/ui-common/screen-patterns.md
  - docs/_shared/definitions.md
  - docs/_shared/operating-environment.md
  - docs/cross-process-flow/brainstorms/cross-process-flow.md
  - docs/cross-process-flow/srs/cross-process-flow-spec.md
  - docs/dispatch-coordination/brainstorms/dispatch-coordination.md
  - docs/meetings/2026-10-09-client-dispatch-field-issues.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs/meetings/decks/2026-10-06-oq-object-map-deck.md
---

# Thay đổi so với SRS v2.0 (LG) — story Jira

## Thông tin story

| Trường | Giá trị |
|---|---|
| Loại | Story |
| Tiêu đề | Cập nhật đặc tả và backlog theo các thay đổi so với SRS v2.0 (LG), chốt tới 12/10/2026 |
| Nhãn | `srs-baseline`, `change-log` |
| Ưu tiên đề xuất | High — phần nào dev đã làm theo SRS v2.0 mà nằm trong danh sách dưới thì phải sửa |
| Người lập | @szitphan |

## Story

Là đội phát triển ERP Delta, tôi cần danh sách đủ các điểm đã đổi so với SRS v2.0 (LG), kèm phương án xử lý, để không xây theo bản cũ ở chỗ đã đổi và biết chỗ nào còn chờ khách chốt.

## Bối cảnh

- SRS v2.0 (LG, gồm bản web `lg-srs-export.md` và bản mobile `srs-mobile.md`) là bản gốc đang dùng. Bản này phủ Xưởng, Kho, Mua hàng, Thanh toán, Cây dầu, Quản trị, Nhân sự, Phương tiện và quy tắc giao diện chung. **Không có phân hệ điều phối vận tải.**
- Từ 29/09 đến 12/10/2026 có 5 nguồn thay đổi: chuẩn hoá quy tắc giao diện chung; làm lại Liên quy trình; phỏng vấn Điều phối theo SOP mới của Delta; 2 buổi trao đổi với khách (09/10 với đội điều vận, 10/10 trả lời bộ câu hỏi vòng 1); 2 tài liệu khách cập nhật (Dữ liệu vận hành xe 08/10, Quản lý hoá đơn SIM 11/10).
- Trạng thái mỗi thay đổi:
  - ✅ **Đã chốt** — khách hoặc đội đã quyết định, có ngày. Dev làm theo được.
  - 🟡 **Đề xuất của đội** — có hướng, chờ khách xác nhận. Dev chưa làm.
  - ⏳ **Chờ khách** — thiếu tài liệu hoặc câu trả lời. Dev chưa làm.

## Tóm tắt

| Nhóm | Số dòng | Chốt hết | Có phần đề xuất | Có phần chờ khách |
|---|---|---|---|---|
| 1. Chung toàn hệ thống (tên app, ngôn ngữ, định dạng, quy tắc giao diện) | 12 | 11 | 1 | 0 |
| 2. Liên quy trình (thay UC00.00.02, UC00.00.03, UC00.01.02) | 4 | 4 | 0 | 0 |
| 3. Phân hệ có trong SRS v2.0 bị Điều phối chạm tới | 8 | 3 | 1 | 4 |
| 4. Phân hệ mới: Điều phối vận tải | 9 | 4 | 0 | 5 |
| 5. Câu hỏi đang chờ khách, có thể làm đổi SRS v2.0 | 2 | 0 | 0 | 2 |

Chi tiết từng dòng ở các mục dưới. Cột "Phương án xử lý" ghi việc của BA (tài liệu) và của dev (phần mềm).

## 1. Thay đổi chung toàn hệ thống

| Mã | Chỗ trong SRS v2.0 | SRS v2.0 ghi | Thay đổi | Phương án xử lý | Trạng thái | Nguồn |
|---|---|---|---|---|---|---|
| CHG-01 | Toàn bộ bản mobile; Partner Portal | "App Lái xe" cho nhân viên Delta; Partner Portal riêng cho nhân viên đối tác cây dầu | Đổi tên thành **Delta Super App**. Partner Portal gộp vào app, chỉ còn bản mobile. Ai thấy chức năng nào theo phân quyền | Dev: 1 app, 1 cửa đăng nhập, trang chủ theo loại tài khoản (giữ logic UC00.01.01 và UC00.01.03); bỏ portal web đối tác. BA: tài liệu mới dùng tên mới | ✅ 05/10 | `docs/_shared/definitions.md` › Delta Super App |
| CHG-02 | UC02.03.01 Thay đổi ngôn ngữ | Việt, Anh, Nhật | Chỉ Tiếng Việt (mặc định) và Tiếng Anh | Dev bỏ Tiếng Nhật khỏi danh sách và bộ dịch. BA sửa UC02.03.01 | ✅ 01/10 | `docs/_shared/operating-environment.md` |
| CHG-03 | Quy tắc web 2.4, 2.5 (số, tiền) | Chuẩn vi-VN: dấu chấm ngăn nghìn, dấu phẩy thập phân | Dấu phẩy ngăn nghìn, dấu chấm thập phân: `1,234,567` · `12.5` · `12.5%` · `100,000 đ`. Không dùng định dạng mặc định của trình duyệt | Dev sửa hàm định dạng dùng chung (web + app), kiểm lại file export | ✅ 29/09 | `design/design.md` › Số và tiền tệ |
| CHG-04 | Quy tắc app 2.2 (ô nhập dài) | Tối đa 4000 ký tự | Tối đa 1000 như web; bộ đếm chỉ hiện khi còn ≤ 200 ký tự | Dev sửa giới hạn ô nhập dài trên app | ✅ 04/10 | `design/ui-common/conventions.md` › GR-01 |
| CHG-05 | Quy tắc app 2.10 (trường không có thông tin) | Hiện `--` | Hiện `-` như web | Dev sửa ký tự rỗng trên app | ✅ 04/10 | conventions › GR-10 |
| CHG-06 | MSC-01 thông báo trong app | Số chưa đọc tối đa `99+` | Tối đa `9+` như web | Dev sửa nhãn số trên biểu tượng thông báo | ✅ 04/10 | `design/ui-common/screen-patterns.md` › CMP-02 |
| CHG-07 | MSC-05 Lịch sử hoạt động (app) | Mở màn riêng | Mở dạng tấm trượt từ đáy (bottom sheet), giữ màn chi tiết phía sau | Dev đổi cách mở lịch sử trên app | ✅ 29/09, 04/10 | screen-patterns › CMP-08 |
| CHG-08 | SC-08 Lịch sử hoạt động (web) | Chỉ ghi ngày | Ghi `dd/MM/yyyy hh:mm`; dòng "Hiện tại" chỉ ghi trạng thái + thời gian chờ, không ghi tên người duyệt | Dev sửa định dạng thời gian và dòng "Hiện tại" | ✅ 29/09 | design.md › Activity Log |
| CHG-09 | SC-04 Phân trang | Nhãn "50 bản ghi trên 1 trang"; trang hiện tại màu xanh lá | (a) Màu trang hiện tại theo màu nhấn của theme. (b) Đổi lọc/tìm/sắp xếp thì về trang 1; mở chi tiết rồi quay lại thì giữ trang, bộ lọc, vị trí cuộn; đang chuyển trang thì giữ bảng, hiện khung chờ. (c) Mobile tải thêm khi cuộn. (d) Nhãn tổng đổi thành "Hiển thị 1–50 / 128" | Dev làm (a)–(c). (d) chưa làm tới khi khách đồng ý | ✅ 01/10 (a–c) · 🟡 (d) | design.md › Phân trang danh sách; BL-054 |
| CHG-10 | Câu chữ thông báo (web + app) | "Vui lòng nhập thông tin này!" và các câu "Vui lòng…" | Ngôi "bạn", câu ngắn, không "Vui lòng". Bộ câu chuẩn dùng chung mã `E-common-001…` | Dev thay chuỗi theo bảng E-common, dùng chung khoá dịch cho web và app | ✅ | conventions › bảng E-common |
| CHG-11 | Quy tắc chung web và app | Nằm rải ở 2 tài liệu; số hiệu lệch nhau (vd bản app gọi "MSC-03" cho hộp xác nhận) | Gộp thành 1 bộ mã: **GR-01…GR-27** (quy tắc), **CMP-01…CMP-12** (thành phần dùng chung), **E-common** (lỗi chung). Thêm mới: GR-27 Dữ liệu đã cũ (banner + nút Tải lại), CMP-12 Tấm thông báo thành công (app) | Dev đối chiếu thư viện thành phần với CMP; đặc tả mới chỉ gọi theo mã | ✅ 12/10 | screen-patterns, conventions |
| CHG-12 | Khung giao diện | Chưa quy định | Khung trang dự án và mốc màn hình (12/10); thanh điều hướng đáy app chỉ hiện biểu tượng (06/10); luôn hiện thanh trạng thái và vạch Home (06/10) | Dev áp theo design.md | ✅ | design.md › Layout, Bottom Navigation, Responsive |

## 2. Liên quy trình — thay UC00.00.02, UC00.00.03 (web) và UC00.01.02 (mobile)

| Mã | Chỗ trong SRS v2.0 | SRS v2.0 ghi | Thay đổi | Phương án xử lý | Trạng thái | Nguồn |
|---|---|---|---|---|---|---|
| CHG-13 | UC00.00.02, UC00.01.02 Thanh tiến trình | Thanh ngang tuyến tính; phải đặt ngoại lệ "nhánh phát sinh xếp liền sau Xuất kho". Không vẽ được nhánh lồng nhau (Bồi thường sinh từ Nhập kho dư) và nhiều phiếu cùng loại (2 phiếu Xuất kho của 1 lệnh sửa chữa) | **Sơ đồ cây**: web mở cửa sổ nổi, app mở tấm trượt. Có bước chính, nhánh phát sinh, ngã rẽ chưa chốt, bước của module khác, bước công nợ. Chọn 1 bước → khung chi tiết (trạng thái, 5 dòng lịch sử mới nhất, nút "Mở màn hình chi tiết"). Thấy mọi bước, bước không có quyền thì ẩn lịch sử và nút | Dev: mỗi bản ghi lưu bản ghi nguồn tạo ra nó; vẽ theo nguồn, không theo thời gian (quy tắc vẽ R1–R17 của CMP-09); làm lại thành phần thanh tiến trình. BA: chuyển SRS cross-process-flow sang in-review | ✅ 11–12/10 | `docs/cross-process-flow/srs/cross-process-flow-spec.md` |
| CHG-14 | — (mới) | — | Đối tượng **Quy trình**: mã `QT-[Mã chi nhánh]-[XXXX]`, trạng thái tự tính (Đang triển khai · Đã dừng · Đã hoàn thành). Màn danh sách Quy trình ở menu mỗi module; tìm theo mã của bất kỳ bản ghi nào trong cây (từ 3 ký tự) | Dev: thực thể mới, sinh mã, việc tự tính trạng thái; Admin cấp quyền menu Quy trình theo module | ✅ 12/10 | như trên |
| CHG-15 | UC00.00.03 Tạo nghiệp vụ tiếp theo | Điều kiện viết kỹ thuật ("Lệnh SC có SL hỏng > 0"), mã TH1/TH2 hiện trên giao diện | Giữ logic. Nút đặt ở vùng hành động đầu trang. Điều kiện và nguồn tạo viết bằng lời nghiệp vụ ("Có 1 phụ tùng hỏng khi sửa", "Tạo từ lệnh sửa chữa LSC-0930"); không hiện mã TH. Thêm 2 chặn: gửi cho bước đã có yêu cầu khác chờ duyệt (E-cross-process-flow-001); thu hồi/xoá bản ghi đã sinh bước con (E-cross-process-flow-002) | Dev: câu hiển thị đọc từ bảng liên quy trình của mỗi nghiệp vụ; thêm 2 chặn. BA: mỗi SRS nghiệp vụ mới phải có bảng liên quy trình | ✅ 12/10 | như trên |
| CHG-16 | CMP-09 (thành phần chung) | 1 mã dùng cho 4 nghĩa (quy trình nhiều nghiệp vụ, vòng đời 1 bản ghi, form nhiều bước, danh sách việc) | Tách: CMP-09 chỉ còn Liên quy trình · vòng đời 1 bản ghi dùng nhãn trạng thái + Lịch sử (CMP-08) · thêm "Form theo bước" và "Checklist" (để sau) | BA sửa 3 wireframe Điều phối đang gọi CMP-09 sai nghĩa (BL-053); 2 thành phần mới chờ feature thứ 2 dùng (BL-052) | ✅ 11/10 | cross-process-flow brainstorm Mục 2 |

## 3. Phân hệ có trong SRS v2.0 bị Điều phối chạm tới

| Mã | Chỗ trong SRS v2.0 | SRS v2.0 ghi | Thay đổi | Phương án xử lý | Trạng thái | Nguồn |
|---|---|---|---|---|---|---|
| CHG-17 | Phương tiện (Feature 04.01) | Mooc, đầu kéo, container DC/Reefer là từng phương tiện riêng; chưa có khái niệm ghép chúng trên một chuyến | Lệnh vận tải ghi **tổ hợp đầu kéo – mooc – container**. Mooc trên Lệnh được khác mooc đang móc trên xe; đổi mooc thì ghép hàng – xe đổi theo. Bỏ mooc giữa đường (hiếm): điều xe khác ra kéo tiếp | Không sửa hồ sơ phương tiện; thêm quan hệ "tổ hợp theo Lệnh". BA đưa bảng quy tắc mooc × cấu hình, 4 trạng thái vị trí container, 13 trường hợp và 7 câu hỏi khách của `design/_lab/lab-combo.html` vào brainstorm | ✅ 09/10 (yêu cầu) · ⏳ chi tiết | Họp 09/10 mục 2; BL-050 |
| CHG-18 | Cấp dầu (mobile Epic 06: dGas3 cấp dầu vận tải, dGas4 đổ đầy bình, UC06.00.08 cấp bù, UC06.00.11 mua hoá đơn lẻ) | Phiếu cấp dầu không gắn chuyến; dầu mua ngoài theo hoá đơn lẻ không lưu lượng dư | Cấp dầu gắn **Lệnh vận tải** và định mức phương tiện; vượt định mức vẫn đi phiếu dGas4. Đổi cung đường thì điều chỉnh lượng dầu cấp, chi phí công ty chịu. Dầu mua ngoài theo hoá đơn lẻ: **lưu lượng dầu dư** làm căn cứ tạo phiếu cấp bù | Dev: thêm liên kết phiếu cấp dầu – Lệnh; thêm trường lượng dư ở UC06.00.11 và đọc nó ở UC06.00.08. BA ghi vào SRS Lệnh vận tải | ✅ 09/10 | Họp 09/10 mục 1, 3; BL-037 |
| CHG-19 | Báo cáo sự cố (mobile Epic 04, web 05.07) | Lái xe báo hỏng hóc phương tiện, xưởng xác nhận rồi lập báo giá | Thêm **báo thay đổi và vấn đề giữa chặng** trên Lệnh: cung đường, giờ giao, đi công suất, khách muốn đi cao tốc, sự cố đường về, khách báo thiếu hàng, khách huỷ vì hàng chưa sẵn sàng, đổi điểm giao. Điều vận và quản lý đều nhận. Lệnh lưu cả kế hoạch và thực tế | Đề xuất tách 2 luồng vì khác người xử lý: báo vấn đề trên Lệnh (điều vận) và báo cáo sự cố phương tiện (xưởng). Hỏng xe giữa chặng thì từ Lệnh mở báo cáo sự cố cũ | ✅ 09/10 (yêu cầu) · 🟡 cách tách | Họp 09/10 mục 1 |
| CHG-20 | Danh mục chi phí cấp 1, 2, 3 (03.10–03.12) | Danh mục phân cấp, không gắn địa điểm, không có cách hạch toán | Loại phí có **cách hạch toán theo địa điểm** (thu nhập chịu thuế của lái xe · chi hộ · trả hộ · chi phí vận hành) và định mức tự điền (vd depot đường sắt 150.000 đ Nam Khánh, 160.000 đ Phú Lợi). Lái xe chỉ chọn loại phí | Thêm bảng "loại phí × địa điểm → cách hạch toán, định mức" nối vào chi phí cấp 3. Chờ Delta gửi bảng cho các tuyến ngoài đường sắt | ✅ SOP (đường sắt) · ⏳ tuyến khác (OQ-31) | Brainstorm Điều phối E5 |
| CHG-21 | Khách hàng DK05 (03.08) | Một khách hàng trên một giao dịch | Trên JobID, **bên xuất hoá đơn có thể khác khách đặt dịch vụ**; đổi được tới trước khi xuất hoá đơn, không phải huỷ Lệnh. Bên thứ ba chưa có mã thì tạo việc "Đăng ký bên thanh toán" kèm thoả thuận ba bên. Delta chấp nhận lệch về hình thức, báo cáo quản trị theo thực tế giao dịch | Dev thêm trường bên xuất hoá đơn trên JobID. Chờ khách trả lời ai duyệt mã DK05 cấp 2 | ✅ 10/10 (OQ-11) · ⏳ OQ-36 | Brainstorm D10; họp 10/10 câu 23 |
| CHG-22 | Thanh toán (Epic 06) | Thanh toán theo đơn mua, công nợ nhà cung cấp; không gắn chuyến | Nút **tạo Yêu cầu thanh toán trên Lệnh/JobID**, chi phí gắn đúng Lệnh/JobID. JobID chưa kê khai đủ thì khoá thanh toán (E-dispatch-007). Khoản trên 5.000.000 đ tạo việc cho CS phụ trách + kế toán; dưới thì tạm ứng. Phần duyệt, QR, UNC, API ngân hàng, in hoá đơn trả hộ hàng loạt ra PDF thuộc feature mới **Thanh toán trả hộ** | Dev thêm điểm vào thanh toán từ Lệnh/JobID. BA mở brainstorm Thanh toán trả hộ (BL-042, BL-039) | ✅ SOP to-be | Brainstorm E2, E6; họp 09/10 mục 4 |
| CHG-23 | Phân quyền (13.02 nhóm quyền, 02.02 phân quyền, bảng 5 vai trò mẫu) | Nhóm quyền theo chức năng + phạm vi chi nhánh/cơ sở; quyền cố định theo tài khoản | Thêm **quyền gắn với việc và theo ca**: (a) người được giao việc hiện trường được cấp quyền thanh toán của đúng JobID đó, chuyển việc thì quyền đi theo; (b) ca trực ngoài giờ 17h30–8h: cán bộ quản lý hiện trường giao, người trực tự giao việc trong ca, hết ca thu quyền, có bàn giao việc đầu và cuối ca; (c) mặc định chỉ thấy JobID chi nhánh mình | Dev: thêm loại quyền có thời hạn và gắn bản ghi, cạnh nhóm quyền tĩnh. Chờ khách trả lời chi tiết lịch trực | ✅ 10/10 (OQ-26 phương án A) · ⏳ chi tiết lịch | Brainstorm B2, B3b; họp 10/10 câu 9 |
| CHG-24 | Kế toán, báo cáo nội bộ | Không có giao dịch giữa chi nhánh | Tạo JobID trái tuyến hoặc giao việc trái tuyến thì phần mềm **tự ghi nhận giao dịch nội bộ và tự hạch toán**. Chia lợi nhuận theo tỷ lệ lãi gộp 50/50, sau khi chốt bảng kê công nợ phải thu, phải trả | Dev: nhận diện trái tuyến theo chi nhánh của JobID và người làm; sinh bút toán nội bộ sau khi chốt bảng kê. BA viết thành BR trong SRS Điều phối | ✅ 10/10 (OQ-16, OQ-4) | Họp 10/10 câu 1, 2 |

## 4. Phân hệ mới: Điều phối vận tải (JobID → Yêu cầu vận tải → Lệnh vận tải)

Không có trong SRS v2.0, phải đặc tả mới toàn bộ. Nội dung đầy đủ ở brainstorm Điều phối; bảng dưới chỉ ghi phạm vi và các điểm đã đổi sau bản brainstorm 07/10.

| Mã | Phần | Nội dung | Phương án xử lý | Trạng thái | Nguồn |
|---|---|---|---|---|---|
| CHG-25 | Đối tượng và trạng thái | **JobID**: Chờ duyệt → (Dừng – chờ khách thanh toán) → Chờ xử lý → Đã tạo YCVT → Đã thực hiện Lệnh vận tải → Hoàn thành dịch vụ. **YCVT**: hiện "đã lập x/n Lệnh". **Lệnh vận tải**: Đã lập → Đã giao lái xe → Lái xe đã nhận → Đang thực hiện → Lái xe đã chốt → Đã duyệt, kèm Huỷ, lái xe từ chối, duyệt trả lại. Thêm **Cảnh báo mốc** và **Chứng từ gốc phải chuyển** | BA vẽ `/state` khi viết SRS | ✅ 07/10 | Brainstorm Mục 6.3 |
| CHG-26 | Phạm vi luồng | 6 luồng FCL, LCL/CFS, air × xuất, nhập đi qua Điều phối. **Đổi 10/10:** CBT và đường sắt không đi qua Điều phối (không giao nhận tại cảng, CBT thuê ngoài toàn bộ); mỗi loại JobID có giao diện riêng, kéo theo YCVT và Lệnh riêng | BA tách D6–D8, E3, E4, E8 (CBT, đường sắt) khỏi phạm vi Điều phối, chờ quy trình điều vận | ✅ 10/10 · ⏳ luồng CBT, đường sắt (OQ-1) | Họp 10/10 câu 3 |
| CHG-27 | Tạo JobID có AI đọc chứng từ | Bản SIM 11/10 bổ sung: người tạo gán trước khách DK05 + báo giá/hợp đồng + loại JobID rồi mới tải chứng từ; AI ra JobID nháp, người tạo rà, sửa, duyệt mới phát hành; trường độ tin cậy thấp để trống; chỗ người sửa lưu lại để cải tiến; 1–3 trang dưới 5MB trả ngay (P95 ≤ 10 giây), lớn hơn chạy nền (P95 ≤ 60 giây); chặn xử lý lặp theo loại JobID + DK05 + tệp; JobID không có chứng từ thì tạo tay. Chặn tạo JobID khi nợ xấu theo cảnh báo từ sổ phụ ngân hàng | BA đưa vào brainstorm bước 0 và DP-01 | ⏳ chưa vào brainstorm | BL-047 |
| CHG-28 | Giảm nhập liệu (A1–A9) | AI đọc Booking Note, eDO, EIR, phiếu cân ra VGM; quét QR tờ khai; kiểm số container theo ISO 6346; danh sách việc ePort theo cảng (không kết nối máy); hoá đơn điện tử lấy qua MISA, không khớp thì gắn cờ | BA viết FR. MISA chờ OQ-23 | ✅ 07/10 · ⏳ MISA | Brainstorm A1–A9 |
| CHG-29 | Quy trình (B1–B6) | **Đổi 10/10:** nút "Chuyển cho hiện trường" đổi tên **"Chuyển việc"**, chỉ 2 lý do (Hết giờ làm việc · Khác, tự ghi), bắt buộc lý do · gộp giao việc Lệnh hạ vỏ rỗng theo vận đơn + nơi hạ **chỉ khi JobID có 1 container** (nhiều container làm từng cái) · **bỏ theo dõi tiền hoàn nâng vỏ** (đã nằm trong dư nợ tạm ứng của nhân viên) · cảnh báo quá mốc **không thêm nhóm nguyên nhân** "khách quan" (kẹt xe xử lý ngoài phần mềm) | BA sửa brainstorm B2, B4, B5, B6 rồi mới viết SRS | ✅ 10/10 · chưa vào brainstorm | Họp 10/10 câu 8, 10, 13, 15; BL-040 |
| CHG-30 | Giao nhận (D1–D10) | Điểm chụp ảnh bắt buộc theo loại hàng; nhật ký nhiệt hàng lạnh; chặn giao xe khi air chưa đủ kiện; nơi nhận lấy từ D/O; gợi ý ghép hàng lẻ; theo dõi mã vạch gốc. **Đổi 10/10:** biên bản giao hàng làm **cả ký điện tử và giấy**; khi lái xe xác nhận biên bản khách đã ký thì phần mềm **tự gửi email biên bản cho CS và khách** | BA thêm FR gửi email biên bản | ✅ 10/10 · ⏳ ai ký phía khách, khách nào bắt đóng dấu (OQ-20) | Họp 10/10 câu 12 |
| CHG-31 | Chi phí (E1–E8) | **Đổi 10/10:** **bỏ luồng xin duyệt chi ngoài định mức trên app** (khách đồng ý ngoài phần mềm, rồi ghi nhận và chi ở quy trình cung cấp dịch vụ hoặc thanh toán không hoá đơn) · đơn giá đường sắt giai đoạn 1 CS nhập tay, giai đoạn 2 lấy từ báo giá phân hệ Sales · phí lưu ca xe ghi lên Lệnh, phí máy phát làm sau · chi phí sửa chữa container ghi trên Lệnh (giai đoạn 1 không quản lý vỏ container). **Đổi 08/10 (VIS):** vé đường bộ chia 3 loại (qua trạm ghi vào Lệnh · tránh trạm trả vào lương lái xe · vé không khớp chuyến chuyển kế toán); VETC là nguồn chuẩn toạ độ và chi phí khi lệch Vietmap | BA bỏ E1 khỏi brainstorm và lỗi E-dispatch-008; ghi VETC vào SRS; quyết định tài khoản VETC tự nạp thuộc Điều phối hay feature riêng | ✅ 09/10, 10/10 · ⏳ chi tiết VIS | Họp 10/10 câu 5, 14, 16, 18; BL-038, BL-044 |
| CHG-32 | Thay đổi giữa chặng, nhiên liệu (F1–F8) | Báo thay đổi giữa chặng; đổi cung đường; mooc khác xe; cấp dầu theo Lệnh; hạn chuẩn bị giấy tờ theo từng Lệnh; VETC nguồn chuẩn. Ảnh hưởng phân hệ cũ ghi ở CHG-17, 18, 19 | BA viết FR | ✅ 09/10 | Họp 09/10 |
| CHG-33 | Hướng phát triển (P2) | Điều phối Lệnh có AI kiểu ứng dụng gọi xe: phần mềm đề xuất xe, điều vận chốt | Không làm giai đoạn này | ✅ 09/10 (P2) | Brainstorm F9 |

## 5. Câu hỏi đang chờ khách, có thể làm đổi SRS v2.0

| Mã | Phân hệ | Câu hỏi | Nếu khách chọn khác SRS v2.0 | Theo dõi |
|---|---|---|---|---|
| CHG-34 | Phân quyền, Nhân sự, Xưởng, Cây dầu | 9 câu gửi 06/10: bộ 5 vai trò mẫu có dùng được không; ai duyệt thêm nhân viên và nghỉ việc; mỗi nhân viên một tài khoản dùng chung web và app; một lệnh sửa chữa xuất phụ tùng nhiều lần; báo giá chọn sửa xưởng ngoài có tự tạo đơn mua không; ai ghi nhận khách đồng ý báo giá; biên bản bàn giao, thu hồi xe ký giấy hay trên app; nhà cung cấp dầu dùng chung danh sách nhà cung cấp không; phiếu nhập dầu có thu hồi, huỷ được không | Sửa UC tương ứng trong SRS v2.0 (5/9 câu SRS v2.0 đã có hướng, khách chỉ cần xác nhận) | Deck `2026-10-06-oq-object-map-deck` |
| CHG-35 | Điều phối | 12 câu còn mở sau vòng 1 (quy mô theo chi nhánh, số booking khi đặt xe, phí lưu ca xe, MISA, bảng loại phí, mẫu QR, quy trình điều vận…) và 2 câu ngày 09/10 (hàng quay cắt, tạm ứng dầu xe CBT) | Ảnh hưởng CHG-18, 20, 26, 28, 31 | BL-036, BL-041 |

## Phương án chạy story

1. **Giữ SRS v2.0 làm bản gốc**, không sửa file gốc. Mọi thay đổi ✅ đi vào SRS mới theo từng feature (hoặc UC cập nhật), có dẫn nguồn.
2. **Dev chỉ làm dòng ✅.** Dòng 🟡 và ⏳ gom vào bộ câu hỏi gửi khách; khách chốt thì cập nhật trạng thái trong file này và báo dev.
3. Thứ tự: nhóm 1 (chung, ảnh hưởng mọi màn) → nhóm 2 (Liên quy trình, nền cho Xưởng và Điều phối) → nhóm 3 (phân hệ cũ bị chạm) → nhóm 4 (Điều phối, sau khi brainstorm cập nhật xong).

**Việc con đề xuất:**

| # | Việc | Người làm | Dòng liên quan |
|---|---|---|---|
| 1 | Áp thay đổi giao diện chung trên web và app | Dev | CHG-01 → CHG-12 |
| 2 | Chuyển SRS Liên quy trình sang in-review; dựng thành phần sơ đồ cây và đối tượng Quy trình | BA, Dev | CHG-13 → CHG-16 |
| 3 | Cập nhật brainstorm Điều phối theo họp 10/10, VIS 08/10, SIM 11/10, tổ hợp mooc | BA | CHG-17, 26 → 31 (BL-040, BL-044, BL-047, BL-050) |
| 4 | Viết SRS Điều phối | BA | CHG-24 → CHG-33 |
| 5 | Viết lại các UC SRS v2.0 bị chạm: Phương tiện, Cấp dầu, Báo cáo sự cố, Danh mục chi phí, Khách hàng DK05, Thanh toán, Phân quyền | BA | CHG-17 → CHG-23 |
| 6 | Gửi khách bộ câu hỏi cho các dòng 🟡, ⏳ | BA | CHG-09, 19, 20, 21, 23, 34, 35 |

## Tiêu chí hoàn thành

- [ ] Mỗi dòng ✅ đã có trong SRS mới hoặc UC cập nhật, ghi nguồn về mã CHG.
- [ ] Mỗi dòng 🟡, ⏳ đã nằm trong câu hỏi mở của tài liệu feature hoặc bộ câu hỏi gửi khách.
- [ ] Dev đánh dấu UC nào của SRS v2.0 không còn hiệu lực (ít nhất UC00.00.02, UC00.01.02, UC02.03.01).
- [ ] Story có link tới các ticket dev của từng việc con.
- [ ] File này cập nhật trạng thái mỗi khi khách chốt thêm.

## Không đổi

Các phần sau của SRS v2.0 giữ nguyên, trừ chỗ đã ghi ở trên: Đăng nhập và tài khoản cá nhân; danh mục Xưởng (dịch vụ kỹ thuật, phụ tùng, công cụ, lốp, ắc quy, nhà cung cấp, xe của khách hàng); hàng tồn kho, tồn xưởng, kiểm kê, rác thải; mua hàng, báo giá, nhập kho, xuất kho, lệnh sửa chữa; bồi thường, thanh toán bán hàng hoá dịch vụ; báo cáo; mua dầu, nhập dầu, cây dầu mua ngoài; quản trị tài khoản, nhóm quyền; nhân sự; bàn giao, thu hồi phương tiện, định mức nhiên liệu.
