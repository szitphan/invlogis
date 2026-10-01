---
type: research
keyword: "kết nối ePort tự động"
status: draft
updated: 2026-10-02
links:
  - docs-input/Giao_nhan_container_2.md
  - docs-input/Quy_trinh_dieu_phoi.md
  - docs-input/Danh_muc_dia_diem_va_hang_tau.md
  - docs-input/doc.md
  - docs/_research/2026-10-02-container-deadline-alerts.md
  - docs/_research/2026-10-02-electronic-delivery-record.md
---

# Kết nối ePort tự động

> **Khuyến nghị: KHÔNG LÀM kết nối ePort lúc này — chỉ làm 2 việc thử nhỏ.** Không cảng nào công bố kênh kết nối cho đơn vị vận tải, còn cách cho máy đăng nhập hộ thì rủi ro lớn; giờ thật cho cảnh báo mốc và công nợ nên lấy từ App Lái xe và đọc ảnh EIR, cách này phủ được cả nơi không có ePort.

***

## Tóm tắt

CS hiện đăng nhập từng ePort của từng cảng, depot để làm lệnh, thanh toán phí và tải Phiếu EIR; nơi không có ePort thì lái xe và hiện trường làm tại chỗ. Ở Việt Nam mỗi nhóm cảng vận hành ePort riêng, chỉ mở qua web và app có đăng nhập; không cảng nào được xem công bố kênh kết nối cho phần mềm của đơn vị vận tải, và xu hướng là cảng bắt đơn vị vận tải dùng app của cảng. Dữ liệu theo dõi container quốc tế có thể bổ sung trạng thái và lịch tàu nhưng độ phủ Việt Nam còn hạn chế và không phủ depot. Khuyến nghị: không làm lệnh tự động, chưa kết nối EIR; thử dữ liệu theo dõi container với 10 container thật và xin kênh chính thức từ vài cảng làm nhiều nhất.

***

## 1. CS và điều vận cần gì

1) **CS bớt thao tác trên từng ePort** — làm lệnh nâng, hạ, thanh toán phí nâng hạ, tải EIR trên nhiều cổng khác nhau cho từng lô, từng container.
2) **Điều vận biết container đã sẵn sàng hay đã ra cổng** — để điều xe đúng lúc, không để xe chờ hay đến khi container chưa dỡ.
3) **Có giờ thật cho cảnh báo mốc và công nợ** — giờ EIR nhận container là mốc bắt đầu tính DET; giờ EIR hạ hàng là căn cứ kịp CY.

**Vì sao đáng làm:** Có ePort hay không quyết định ai làm lệnh và quy trình đi nhánh nào; mỗi cổng một giao diện, một tài khoản. Phần việc này lặp lại cho mọi lô hàng và là đầu vào của cảnh báo mốc, biên bản, công nợ.

**Bằng chứng nhu cầu:**
* SOP Giao nhận container (Mục 2) và SOP điều phối mô tả CS thao tác trên ePort cho từng lệnh, từng container; nơi không có ePort thì lái xe tự làm và chụp ảnh EIR.
* Danh mục địa điểm: 36 cảng (25 có ePort; Hải Phòng 15/17), 88 depot (chỉ 14 có ePort), kho CFS và kho hàng không không nơi nào có ePort.
* Chưa có số liệu số lượt làm việc theo cảng hay thời gian CS bỏ ra cho các thao tác này.

**Phục vụ ai:** CS (làm lệnh, thanh toán), điều vận (điều xe), lái xe và hiện trường (nơi không có ePort), kế toán (chứng từ phí).

***

## 2. Đối thủ làm thế nào

| | **Delta (hiện tại)** | ePort Tân Cảng (SNP) | ePort Cảng Hải Phòng | ePort HICT | Gemadept SmartPort | CETA, LogisViet | Terminal49 | Vizion |
|---|---|---|---|---|---|---|---|---|
| **Là gì** | CS làm tay trên từng ePort | Cổng của nhóm Tân Cảng: Cát Lái, Hiệp Phước, Cái Mép, HICT | Cổng của Cảng Hải Phòng, gắn cổng tự động ở Tân Vũ | Cổng của HICT, cổng tự động 100% | Cổng của Nam Đình Vũ, Nam Hải ICD | Phần mềm vận tải trong nước | Dữ liệu theo dõi container quốc tế | Dữ liệu sự kiện từ hãng tàu |
| **Lấy được gì** | — | Làm lệnh, thanh toán, eDO, tra EIR | eDO, đăng ký dịch vụ, thanh toán, EIR điện tử, lịch sử chuyến xe | Tra container, tàu, thanh toán, mẫu EIR | Tra cứu container theo cảng | — | Tàu đến, dỡ, sẵn sàng lấy, ngày hết miễn phí | Sự kiện hãng tàu |
| **Kết nối cho đơn vị vận tải** | — | Không thấy — chỉ web, app đăng nhập | Không thấy — web và app tài xế | Không thấy — web và app tài xế | Không rõ | Không công bố nối ePort | Có, qua gói trả phí | Có |
| **Phủ địa bàn Delta** | — | HCM, Cái Mép, Lạch Huyện | Hải Phòng | Lạch Huyện | Hải Phòng | — | 15 terminal Hải Phòng, Cát Lái và vài cảng HCM; dữ liệu ghi "hạn chế"; không có depot | Chưa xác nhận cảng Việt Nam |
| *Chi phí* | *Công CS* | *Phí dịch vụ cảng* | *Phí dịch vụ cảng* | *Phí dịch vụ cảng* | *Phí dịch vụ cảng* | *LogisViet 350.000 đ/xe/tháng; CETA không công khai* | *Có gói miễn phí 10 container; gói có kết nối không công khai giá* | *Từ khoảng 119 USD/tháng* |

*Độ tin cậy: thông tin về các ePort lấy từ trang chính thức của cảng và báo ngành — chắc chắn có nguồn về chức năng, nhưng kết luận "không có kênh cho đơn vị vận tải" chỉ là "không thấy công bố", có thể có kênh ký đối tác riêng; cần hỏi trực tiếp từng cảng. Độ phủ Việt Nam của Terminal49 và Vizion là suy đoán từ trang giới thiệu, chưa thử với dữ liệu thật.*

**Mấy điểm chung rút ra:**
* Mỗi nhóm cảng một ePort riêng, chưa thấy cổng gộp nhiều cảng cho đơn vị vận tải, cũng chưa thấy hệ thống lệnh giao hàng điện tử dùng chung cho nhiều hãng tàu.
* Cảng đang kéo đơn vị vận tải vào app của cảng (đăng ký xe, tài xế, mã thẻ) — ePort đang trở thành nơi giữ giờ qua cổng thật.
* Kết nối có tiền lệ theo chiều hãng tàu (hãng tàu với cảng, hãng tàu với phần mềm vận tải), không theo chiều cảng cho đơn vị vận tải.

***

## 3. Nếu làm thì lưu ý gì

**Cách làm đề xuất:** Không kết nối máy với máy ở giai đoạn này. Gom việc và giấy tờ cho CS trong phần mềm; lấy giờ thật từ App Lái xe và đọc ảnh EIR; thử dữ liệu theo dõi container ở quy mô nhỏ.

| Phần | Tự động được hôm nay? | Kết luận |
|---|---|---|
| Trạng thái container, lịch tàu | Một phần, qua dữ liệu hãng tàu và dịch vụ theo dõi container | Thử 10 container thật ở Hải Phòng bằng gói miễn phí, so với file theo dõi của hãng tàu; chưa dùng làm mốc DEM/DET khi chưa xác nhận độ khớp |
| EIR, giờ ra/vào cổng | Không — chỉ có qua ePort đăng nhập; phần lớn depot và kho CFS không có ePort | Chưa kết nối; lái xe chụp EIR trên App và máy đọc ảnh là nguồn chính; đo số lượt theo cảng rồi xin kênh chính thức ở 2–3 cảng làm nhiều nhất |
| Làm lệnh tự động | Không có kênh — chỉ có cách cho máy đăng nhập hộ | Không làm; phần mềm chỉ hỗ trợ CS điền sẵn dữ liệu, xem danh sách việc theo cảng, lưu lệnh và EIR vào Lệnh vận tải |

**Lưu ý:**
* **Thông tin cần lưu:** cảng, depot có ePort hay không và kênh nào; lệnh và EIR gắn với Lệnh vận tải; nguồn của từng mốc giờ (EIR, dữ liệu hãng tàu, lái xe nhập) để không trộn lẫn.
* **Rủi ro vận hành:** tài khoản ePort gắn với thanh toán tiền thật — bị khoá là cả công ty ngừng làm lệnh ở cảng đó; cảng đổi quy trình, giao diện thường xuyên (Tân Vũ bắt buộc cổng tự động từ 5/2023, HICT từ 6/2025).
* **Phụ thuộc:** App Lái xe, việc đọc ảnh chứng từ, Lệnh vận tải của mảng điều phối; sự đồng ý của từng cảng nếu muốn kết nối chính thức.
* **Chi phí dữ liệu:** dịch vụ theo dõi container tính theo gói năm; chỉ mua sau khi thử với dữ liệu thật.

**Đừng mắc mấy lỗi này:**
* Cho máy đăng nhập hộ ePort để làm lệnh — dễ bị khoá tài khoản (Tân Cảng đã cảnh báo đăng nhập từ vị trí lạ), có thể vi phạm điều khoản chưa đọc, và hỏng mỗi khi cảng đổi giao diện.
* Lưu mật khẩu ePort của CS trong hệ thống nội bộ — lộ là lộ tài khoản có quyền thanh toán.
* Tin chữ "có phủ" của dịch vụ quốc tế — có tên terminal không có nghĩa có giờ ra cổng; phải thử với lô thật.
* Trộn sự kiện của hãng tàu với giờ trên EIR — hai nguồn khác nhau, trộn sẽ làm sai mốc DEM/DET.

***

## 4. Nên làm không

**Mức độ ưu tiên (xếp thô để so với tính năng khác):** Giá trị cao (bớt thao tác lặp cho CS, có giờ thật cho mốc và công nợ), công sức L nếu làm đủ kết nối và S cho 2 việc thử, độ tin cậy nhận định thấp (chưa biết cảng có cho kết nối, chưa có số lượt theo cảng). Phần kết nối xếp nhóm thấp; 2 việc thử làm ngay được.

**Kết luận: KHÔNG LÀM kết nối ePort lúc này — chỉ làm 2 việc thử nhỏ.**

Nhu cầu là có thật, nhưng con đường kết nối chưa tồn tại: không cảng nào công bố kênh cho đơn vị vận tải, việc làm lệnh tự động chỉ có thể làm bằng cách cho máy đăng nhập hộ — rủi ro lớn hơn lợi ích khi chưa biết số lượt theo cảng. Phần giá trị thật (giờ thật cho cảnh báo mốc, công nợ) lấy được bằng App Lái xe và đọc ảnh EIR, và cách này phủ cả 74 depot và các kho không có ePort. Hai việc nên làm ngay vì rẻ: thử dữ liệu theo dõi container với 10 container thật, và đo số lượt theo cảng để xin kênh chính thức ở 2–3 cảng làm nhiều nhất.

**Các góc nhìn đã cân nhắc:** Ba góc nhìn ủng hộ, phản đối và khả thi đều đồng ý không cho máy đăng nhập hộ để làm lệnh, chỉ thử hẹp phần trạng thái container với lô thật trước khi mua dịch vụ, và lấy EIR do lái xe chụp làm nguồn chính cho giờ thật. Góc nhìn ủng hộ thấy giá trị lớn ở việc gom các ePort rời rạc về một chỗ — ý này được giữ ở mức gom việc và giấy tờ cho CS, không ở mức kết nối máy. Góc nhìn phản đối nhấn mạnh chưa có số lượt theo cảng, nên bước đầu tiên là đo.

***

## 5. Bước tiếp theo

**Các phần đề xuất làm (mỗi phần đủ gọn để brainstorm riêng):**

1) **Hỗ trợ CS làm việc trên ePort** — danh sách việc cần làm theo cảng, điền sẵn dữ liệu từ lô hàng, lưu lệnh và EIR về Lệnh vận tải; có thể gộp vào brainstorm mảng điều phối.
2) **Kết nối dữ liệu theo dõi container** — để bản sau, chỉ làm khi thử 10 container đạt yêu cầu.

**Việc cần làm:**
* [ ] Thống kê số lượt làm việc theo cảng, depot trong vài tháng gần nhất.
* [ ] Thử gói miễn phí của dịch vụ theo dõi container với 10 container thật ở Hải Phòng; so với file theo dõi của hãng tàu.
* [ ] Liên hệ 2–3 cảng làm nhiều nhất hỏi có kênh dữ liệu cho đơn vị vận tải không (giờ cổng, EIR).
* [ ] Đọc điều khoản sử dụng ePort của các cảng chính trước khi tính chuyện tự động hoá.

**Câu hỏi còn mở:**
* [ ] Delta làm nhiều nhất ở những cảng, depot nào?
* [ ] Cảng nào sẵn sàng cấp kênh dữ liệu cho đơn vị vận tải?
* [ ] Ai đứng ra liên hệ cảng?
* [ ] ePort ở các cảng Hải Phòng do nhà cung cấp nào vận hành — có dùng chung không?

***

## Nguồn

1) SOP Giao nhận container, Mục 1–2 — `docs-input/Giao_nhan_container_2.md` — 2026-08-21
2) Danh mục cảng, bãi, kho và hãng tàu — `docs-input/Danh_muc_dia_diem_va_hang_tau.md` — 2026-09-15
3) IRTech — Giải pháp cảng điện tử ePort — [https://irtech.com.vn/giai-phap-cang-dien-tu-eport/](https://irtech.com.vn/giai-phap-cang-dien-tu-eport/) — 2026-10-02
4) Thanh Niên — Tân Cảng Sài Gòn ra mắt ứng dụng SNP ePort — [https://thanhnien.vn/tan-cang-sai-gon-ra-mat-ung-dung-di-dong-snp-eport-1851488821.htm](https://thanhnien.vn/tan-cang-sai-gon-ra-mat-ung-dung-di-dong-snp-eport-1851488821.htm) — 2026-10-02
5) Logistics.gov.vn — Tân Cảng Sài Gòn hoàn thiện ePort cho Cái Mép, Hiệp Phước, Lạch Huyện — [https://logistics.gov.vn/dich-vu-logistics/dich-vu-khac/tan-cang-sai-gon-se-hoan-thien-eport-cho-cac-cang-cai-mep-hiep-phuoc-va-lach-huyen-hict](https://logistics.gov.vn/dich-vu-logistics/dich-vu-khac/tan-cang-sai-gon-se-hoan-thien-eport-cho-cac-cang-cai-mep-hiep-phuoc-va-lach-huyen-hict) — 2026-10-02
6) ePort Cảng Hải Phòng — [https://haiphongport.com.vn/vi/ep/eport](https://haiphongport.com.vn/vi/ep/eport) — 2026-10-02
7) Cảng vụ Hải Phòng — Cảng Hải Phòng triển khai Smart Gate — [https://cangvuhaiphong.gov.vn/cang-hai-phong-trien-khai-he-thong-giao-nhan-cong-tu-dong-smart-gate/](https://cangvuhaiphong.gov.vn/cang-hai-phong-trien-khai-he-thong-giao-nhan-cong-tu-dong-smart-gate/) — 2026-10-02
8) ePort HICT — [https://eport.hict.net.vn/](https://eport.hict.net.vn/) — 2026-10-02
9) Gemadept SmartPort — [https://smartport.gemadept.com.vn/](https://smartport.gemadept.com.vn/) — 2026-10-02
10) ePort Tân Cảng — tra cứu EIR — [https://eport.saigonnewport.com.vn/Eir](https://eport.saigonnewport.com.vn/Eir) — 2026-10-02
11) CETA — API trong ngành logistics — [https://ceta.vn/api-trong-nganh-logistics-tang-tinh-ket-noi-va-tu-dong-hoa-chuoi-van-hanh/](https://ceta.vn/api-trong-nganh-logistics-tang-tinh-ket-noi-va-tu-dong-hoa-chuoi-van-hanh/) — 2026-10-02
12) LogisViet — [https://www.logisviet.com/](https://www.logisviet.com/) — 2026-10-02
13) Terminal49 — Hải Phòng — [https://terminal49.com/ports/vnhph-haiphong/](https://terminal49.com/ports/vnhph-haiphong/) — 2026-10-02
14) Terminal49 — Bảng giá — [https://terminal49.com/pricing](https://terminal49.com/pricing) — 2026-10-02
15) Vizion — Các gói dịch vụ — [https://docs.vizionapi.com/docs/plans](https://docs.vizionapi.com/docs/plans) — 2026-10-02
16) Vizion — Kết nối cảng và terminal — [https://www.vizionapi.com/container-tracking/port-terminal-connections](https://www.vizionapi.com/container-tracking/port-terminal-connections) — 2026-10-02
