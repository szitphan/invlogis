---
type: research
keyword: "đọc chứng từ hiện trường bằng ảnh chụp"
status: draft
updated: 2026-10-02
links:
  - docs-input/Giao_nhan_container_2.md
  - docs-input/Quy_trinh_dieu_phoi.md
  - docs-input/Quy_trinh_cung_cap_dich_vu_tong_quat.md
  - docs/_research/2026-10-02-container-deadline-alerts.md
  - docs/_research/2026-10-02-eport-integration.md
  - docs/_research/2026-10-02-electronic-delivery-record.md
---

# Đọc chứng từ hiện trường bằng ảnh chụp

> **Khuyến nghị: NÊN LÀM — có điều chỉnh, quyết riêng từng loại chứng từ.** Phiếu EIR là nguồn giờ thật duy nhất cho mốc DET sau khi không kết nối ePort, nên làm trước — nhưng thử với ảnh thật của lái xe trước khi chọn nhà cung cấp; hoá đơn điện tử lấy qua MISA thay vì đọc ảnh; phiếu cân và phiếu thu giấy chưa đọc tự động.

***

## Tóm tắt

SOP đã chọn cách "AI đọc, người xác nhận, thống kê lần phải sửa" cho chứng từ định danh lô hàng, số container lúc chọn vỏ và số tờ khai; chủ đề này là mở rộng cách đó sang chứng từ lái xe chụp ở hiện trường: Phiếu EIR, phiếu cân, hoá đơn và phiếu thu. Các dịch vụ đọc chứng từ trong nước và quốc tế được xem không có mẫu sẵn cho EIR hay phiếu cân cảng Việt Nam, và độ chính xác họ công bố đều là tự công bố. Mô hình AI đa năng rẻ nhưng có thể đọc ra chữ không có thật khi ảnh mờ — đúng ở các ô quan trọng nhất là giờ và trọng lượng. Hoá đơn điện tử thì không cần đọc ảnh: MISA tự lấy được từ cổng thuế, với điều kiện hoá đơn xuất cho Delta. Khuyến nghị: thử đọc EIR với vài trăm ảnh thật, lấy hoá đơn điện tử qua MISA, hoãn phiếu cân, phiếu thu giấy nhập tay có hỗ trợ.

***

## 1. Lái xe, CS và kế toán cần gì

1) **Lái xe chụp là xong** — không phải nhập lại giờ, số container, số tiền trên điện thoại ở hiện trường.
2) **Điều vận và cảnh báo mốc có giờ EIR thật** — giờ trên Phiếu EIR nhận container hàng nhập là mốc bắt đầu tính DET; giờ trên EIR hạ hàng là căn cứ kịp CY.
3) **CS có trọng lượng đúng để kê VGM** — trọng lượng trên phiếu cân là căn cứ lập VGM trước khi làm lệnh hạ hàng.
4) **Kế toán có số tiền đúng để thanh toán và trả lại cho lái xe** — từ hoá đơn, phiếu thu lái xe nộp về.

**Vì sao đáng làm:** Lái xe đã phải chụp và tải các chứng từ này lên Lệnh vận tải theo SOP, nhưng ảnh chỉ là ảnh — mọi bước sau vẫn cần người gõ lại số. Với quyết định không kết nối ePort ở thời điểm này, ảnh EIR do lái xe chụp là nguồn giờ thật cho cả cảng có ePort lẫn 74 depot và các kho không có ePort.

**Bằng chứng nhu cầu:**
* SOP Giao nhận container và SOP điều phối yêu cầu chụp và tải EIR, VGM, phiếu xuất kho, hoá đơn lên Lệnh vận tải; các bước kê VGM, thanh toán, theo dõi mốc dùng lại số liệu từ đó.
* SOP Cung cấp dịch vụ tổng quát đã chọn trợ lý AI đọc chứng từ định danh để tạo JobID, có bước người xác nhận và thống kê lần làm tay.
* Chưa có số liệu khối lượng EIR, phiếu cân, hoá đơn mỗi tháng hay thời gian nhập liệu hiện nay.

**Phục vụ ai:** lái xe (chụp), điều vận (xác nhận giờ EIR, theo dõi mốc), CS (kê VGM), kế toán (thanh toán chi phí lái xe trả hộ).

***

## 2. Đối thủ làm thế nào

| | **Delta (dự kiến)** | FPT.AI Read | VNPT SmartReader | MISA (hoá đơn đầu vào) | Klippa | Mô hình AI đa năng |
|---|---|---|---|---|---|---|
| **Đọc được gì** | Đã chọn đọc chứng từ định danh, số container, số tờ khai | Chứng từ xuất nhập khẩu, hoá đơn, biên lai | Hoá đơn, phiếu xuất, mẫu hành chính; có chữ viết tay | Chỉ hoá đơn điện tử — lấy dữ liệu gốc, không đọc ảnh | Hơn 50 loại chứng từ logistics: vận đơn, phiếu giao hàng | Mọi loại giấy theo yêu cầu |
| **Có mẫu EIR, phiếu cân cảng Việt Nam** | — | Không thấy | Không thấy | Không áp dụng | Không thấy | Không có sẵn — tự mô tả |
| **Ảnh chụp điện thoại** | — | Nhận ảnh chụp | Không nói rõ | Không áp dụng | Có bộ công cụ chụp trên điện thoại | Ổn khi ảnh rõ; có thể đọc ra chữ không có thật khi ảnh mờ, xoay, nhỏ |
| **Người xác nhận** | Có trong SOP | Không rõ | Có điểm tin cậy từng ô, cảnh báo ô kém | Có bước xử lý hoá đơn đầu vào | Có người kiểm tra | Tự xây |
| **Độ chính xác** | — | 90–95% (tự công bố) | Đến 99,9% (tự công bố) | Dữ liệu gốc của cơ quan thuế | Đến 99% (tự công bố) | Không công bố — phải tự đo |
| *Giá* | — | *Có gói thử; giá liên hệ* | *Có dùng thử; giá liên hệ* | *Không rõ phí gói hoá đơn đầu vào* | *Thuê bao năm; giá liên hệ* | *Theo lượng dùng — ước tính vài USD cho 1.000 ảnh, chỉ tính phần ảnh* |

*Độ tin cậy: cơ chế lấy hoá đơn đầu vào của MISA và cảnh báo về ảnh mờ của mô hình AI đa năng lấy từ tài liệu chính thức, chắc chắn có nguồn. Các con số độ chính xác của nhà cung cấp là tự công bố, không nói đo trên loại ảnh nào — chưa áp được cho ảnh điện thoại ở hiện trường hay giấy in nhiệt phai. Chi phí mô hình đa năng là ước tính từ bảng giá công khai, chưa tính phần trả kết quả.*

**Mấy điểm chung rút ra:**
* Không ai có sẵn mẫu đọc EIR hay phiếu cân cảng Việt Nam — dù chọn dịch vụ nào, Delta cũng phải tự đo trên ảnh thật.
* Cách làm chung của sản phẩm tốt: đọc ra từng ô, hiện ảnh cạnh ô, đánh dấu ô kém tin cậy để người chỉ cần soi ô đó.
* Với hoá đơn điện tử, dữ liệu gốc từ cơ quan thuế tốt hơn mọi cách đọc ảnh.

***

## 3. Nếu làm thì lưu ý gì

**Cách làm đề xuất:** Quyết riêng từng loại chứng từ, dùng chung một cơ chế "AI đọc, người xác nhận, thống kê lần phải sửa" như SOP đã chọn. Thử trước, chọn nhà cung cấp sau.

| Loại | Kết luận | Cách làm |
|---|---|---|
| Phiếu EIR | Làm, ưu tiên số 1, thử trước | Đọc giờ, số container, số chì; số container tự kiểm bằng chữ số kiểm tra theo chuẩn ISO 6346; lái xe hoặc điều vận xác nhận giờ với ảnh bên cạnh |
| Phiếu cân | Hoãn | Tạm vẫn chụp và nhập tay; xem lại sau khi có kết quả thử EIR |
| Hoá đơn điện tử | Không đọc ảnh | Lấy dữ liệu gốc qua MISA từ cổng thuế; ảnh chỉ để đối chiếu |
| Phiếu thu giấy | Chưa tự động | Chụp ảnh, nhập tay với ảnh hiện bên cạnh |

**Lưu ý:**
* **Thông tin cần lưu:** ảnh gốc đủ nét; giá trị máy đọc và giá trị người xác nhận của từng ô; ai xác nhận, lúc nào; ô nào bị sửa (để thống kê); với hoá đơn: khớp hoá đơn điện tử với khoản lái xe đã trả.
* **Rủi ro trải nghiệm:** nếu phải sửa nhiều, bước xác nhận còn chậm hơn nhập tay; ảnh bị nén khi tải lên làm khó đọc.
* **Phụ thuộc:** App Lái xe (chụp đủ nét, giữ độ phân giải); Lệnh vận tải; MISA và tài khoản cổng thuế của Delta; cảnh báo mốc (nơi dùng giờ EIR đã xác nhận).
* **Chi phí vận hành:** theo số ảnh mỗi tháng — chưa tính được vì chưa có khối lượng.

**Đừng mắc mấy lỗi này:**
* Tin số độ chính xác 95–99,9% của nhà cung cấp — không nói đo trên ảnh điện thoại hay giấy in nhiệt phai.
* Để máy tự điền giờ EIR hoặc trọng lượng không qua người xác nhận — sai một số là sai mốc DET hoặc sai VGM, và không có cách kiểm chéo tự động như số container.
* Coi mọi hoá đơn đều lấy được qua MISA — hoá đơn có thể xuất cho chủ hàng chứ không phải Delta, có thể thiếu khi mất kết nối cổng thuế, và phiếu thu giấy không bao giờ đi đường này.
* Ký hợp đồng nhà cung cấp trước khi thử với ảnh thật.

***

## 4. Nên làm không

**Mức độ ưu tiên (xếp thô để so với tính năng khác):** Giá trị cao cho EIR (nguồn giờ thật cho cảnh báo mốc, thay cho kết nối ePort), công sức M, độ tin cậy nhận định vừa đến thấp (chưa đo trên ảnh thật, chưa có khối lượng). Phần thử EIR xếp nhóm cao vì chủ đề cảnh báo mốc và chủ đề ePort đều dựa vào nó.

**Kết luận: NÊN LÀM — có điều chỉnh, quyết riêng từng loại chứng từ.**

Nhu cầu "chụp là xong" là có thật trên quy trình và đã được SOP chọn hướng cho chứng từ định danh. Với Phiếu EIR, giá trị cao nhất vì đây là nguồn giờ thật duy nhất còn lại cho mốc DET; nhưng chưa ai đọc sẵn được EIR cảng Việt Nam và mô hình AI có thể đọc sai đúng ô giờ, nên phải thử với ảnh thật và bắt buộc người xác nhận. Hoá đơn điện tử đi đường MISA rẻ và chính xác hơn đọc ảnh, chỉ cần xác minh hoá đơn xuất cho Delta. Phiếu cân và phiếu thu giấy rủi ro cao hơn lợi ích ở thời điểm này. Tất cả nhận định về độ chính xác vẫn là suy đoán đến khi có kết quả thử.

**Các góc nhìn đã cân nhắc:** Ba góc nhìn ủng hộ, phản đối và khả thi đều đồng ý ưu tiên EIR và thử với ảnh thật trước khi chọn nhà cung cấp, bắt buộc người xác nhận giờ và trọng lượng, lấy hoá đơn điện tử qua MISA, chưa đọc tự động phiếu thu giấy. Riêng phiếu cân, góc nhìn phản đối muốn bỏ, hai góc nhìn kia muốn làm sau — kết luận là hoãn và xem lại sau khi thử EIR. Góc nhìn phản đối cũng lưu ý nếu tỷ lệ phải sửa cao thì đọc tự động không nhanh hơn nhập tay, nên ngưỡng quyết định đặt theo số đo thật.

***

## 5. Bước tiếp theo

**Các phần đề xuất làm (mỗi phần đủ gọn để brainstorm riêng):**

1) **Đọc Phiếu EIR trên App Lái xe** — chụp đủ nét; đọc giờ, số container, số chì; tự kiểm số container; người xác nhận có ảnh bên cạnh; thống kê lần phải sửa; giờ đã xác nhận đưa vào cảnh báo mốc.
2) **Hoá đơn và phiếu thu lái xe** — hoá đơn điện tử lấy qua MISA và tự khớp với khoản lái xe đã trả; phiếu thu giấy chụp rồi nhập tay có hỗ trợ.
3) **Đọc phiếu cân** — để bản sau, xem lại khi có kết quả thử EIR.

**Việc cần làm:**
* [ ] Gom vài trăm ảnh Phiếu EIR thật từ lái xe (cả cảng có ePort, depot, giấy in nhiệt) để thử.
* [ ] Thử 1 dịch vụ đọc chứng từ trong nước và 1 mô hình AI đa năng trên cùng bộ ảnh; đo tỷ lệ đúng của giờ, số container, số chì và tỷ lệ người phải sửa.
* [ ] Hỏi kế toán: hoá đơn lái xe trả hộ tại cảng xuất cho mã số thuế của Delta hay của chủ hàng; gói hoá đơn đầu vào của MISA có tính phí không.
* [ ] Đếm khối lượng EIR, phiếu cân, hoá đơn, phiếu thu mỗi tháng.

**Câu hỏi còn mở:**
* [ ] Hoá đơn lái xe trả hộ tại cảng xuất cho mã số thuế nào?
* [ ] Mỗi tháng có khoảng bao nhiêu Phiếu EIR, phiếu cân, hoá đơn, phiếu thu?
* [ ] Tỷ lệ phải sửa tối đa bao nhiêu thì việc đọc tự động còn đáng làm?
* [ ] Ai xác nhận giờ EIR — lái xe ngay khi chụp hay điều vận khi rà?

***

## Nguồn

1) SOP Giao nhận container, Mục 1, 3, 6 — `docs-input/Giao_nhan_container_2.md` — 2026-08-21
2) SOP Điều phối, node AI đọc số container và số tờ khai — `docs-input/Quy_trinh_dieu_phoi.md`
3) SOP Cung cấp dịch vụ tổng quát, trợ lý AI đọc chứng từ định danh — `docs-input/Quy_trinh_cung_cap_dich_vu_tong_quat.md`
4) FPT.AI — Số hoá bộ chứng từ xuất nhập khẩu — [https://fpt.ai/vi/bai-viet/so-hoa-bo-chung-tu-xuat-nhap-khau-voi-fptai-reader/](https://fpt.ai/vi/bai-viet/so-hoa-bo-chung-tu-xuat-nhap-khau-voi-fptai-reader/) — 2026-10-02
5) FPT.AI — Hướng dẫn Reader — [https://docs.fpt.ai/docs/vi/vision/documentation/reader-guide/](https://docs.fpt.ai/docs/vi/vision/documentation/reader-guide/) — 2026-10-02
6) VNPT SmartReader — [https://vnptai.io/ldp/smartreader/vi](https://vnptai.io/ldp/smartreader/vi) — 2026-10-02
7) MISA — Đồng bộ hoá đơn đầu vào từ cơ quan thuế — [https://helpact.misa.vn/kb/dong-bo-hoa-don-dau-vao-tu-co-quan-thue/](https://helpact.misa.vn/kb/dong-bo-hoa-don-dau-vao-tu-co-quan-thue/) — 2026-10-02
8) MISA — Khi đồng bộ hoá đơn đầu vào không đủ — [https://helpact.misa.vn/kb/lam-the-nao-khi-dong-bo-hoa-don-dau-vao-tu-co-quan-thue-ve-phan-mem-khong-du/](https://helpact.misa.vn/kb/lam-the-nao-khi-dong-bo-hoa-don-dau-vao-tu-co-quan-thue-ve-phan-mem-khong-du/) — 2026-10-02
9) Klippa — Đọc chứng từ logistics — [https://www.klippa.com/en/ocr/logistics-documents/](https://www.klippa.com/en/ocr/logistics-documents/) — 2026-10-02
10) Klippa — Chụp chứng từ trên điện thoại — [https://www.klippa.com/en/dochorizon/mobile-scanning/](https://www.klippa.com/en/dochorizon/mobile-scanning/) — 2026-10-02
11) Anthropic — Đọc ảnh bằng Claude — [https://platform.claude.com/docs/en/build-with-claude/vision](https://platform.claude.com/docs/en/build-with-claude/vision) — 2026-10-02
12) Google — Bảng giá Gemini API — [https://ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) — 2026-10-02
13) Chuẩn ISO 6346 về mã container — [https://en.wikipedia.org/wiki/ISO_6346](https://en.wikipedia.org/wiki/ISO_6346) — 2026-10-02
