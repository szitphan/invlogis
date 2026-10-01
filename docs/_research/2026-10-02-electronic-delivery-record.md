---
type: research
keyword: "biên bản giao hàng điện tử"
status: draft
updated: 2026-10-02
links:
  - docs-input/sop/sop-giao-nhan-container.md
  - docs-input/sop/sop-dieu-phoi.md
  - docs-input/sop/sop-ban-do-kien-thuc.md
  - docs/_research/2026-10-02-container-deadline-alerts.md
---

# Biên bản giao hàng điện tử

> **Khuyến nghị: NÊN LÀM — có điều chỉnh, tách 2 phần.** Phần đem lại giá trị lớn nhất — biên bản có cấu trúc để đối chiếu công nợ và bắt buộc ghi bất thường trước khi rời điểm — không phụ thuộc việc khách có chịu ký điện tử; làm phần này cùng mảng điều phối, còn khách ký điện tử thì chạy thử với khách đã đồng ý.

***

## Tóm tắt

Hiện lái xe lập biên bản giấy 2 bản, ký với khách rồi chụp ảnh gửi nhóm Zalo; SOP điều phối mới chuyển sang chụp ảnh và tải lên Lệnh vận tải qua App. Biên bản là căn cứ đối chiếu công nợ và quy trách nhiệm khi có bất thường, nhưng ảnh chụp tờ giấy không cho dữ liệu có cấu trúc và không có gì bảo đảm lái xe đã ghi bất thường trước khi rời điểm. Ký trên máy lái xe kèm ảnh, giờ và vị trí đã là cách làm phổ biến ở các phần mềm được xem; nhưng không ai công bố biên bản theo đúng mục container trong SOP (số chì, tình trạng chì), chặn hoàn tất khi chưa ghi bất thường, hay lối thoát khi khách từ chối ký điện tử. Khuyến nghị: làm phần ghi nhận giao hàng có cấu trúc trên App Lái xe trước, chạy thử phần khách ký điện tử sau.

***

## 1. Lái xe, điều vận và kế toán cần gì

1) **Lái xe ghi nhận giao nhận đầy đủ trước khi rời điểm** — nhất là bất thường (chì không nguyên vẹn, hàng thiếu, đổ vỡ, ướt, sai chủng loại), vì rời đi rồi thì Delta chịu toàn bộ trách nhiệm.
2) **Điều vận biết ngay việc giao đã xong và có bất thường hay không** — để xử lý với khách và hãng tàu trong ngày.
3) **Kế toán có biên bản đối chiếu được ngay** — theo số container, số chì, số lượng, không phải chờ bản giấy về hay dò ảnh trong nhóm Zalo.

**Vì sao đáng làm:** Biên bản giao hàng vừa là căn cứ thu hồi công nợ, vừa là căn cứ quy trách nhiệm giữa Delta, khách và hãng tàu. Hiện mọi thứ dựa vào việc lái xe nhớ ghi đủ và nhớ chụp gửi; khi sót, Delta là bên chịu thiệt.

**Bằng chứng nhu cầu:**
* SOP Giao nhận container (Mục 3, Mục 5) và SOP điều phối quy định chặt: ghi bất thường và chụp ảnh trước khi rời điểm, không ký khi chưa ghi nhận, chụp gửi ngay không chờ về công ty.
* Chưa có số liệu về biên bản thất lạc, tranh chấp do không ghi bất thường hay đối chiếu công nợ chậm.
* Chưa biết khách có chấp nhận biên bản điện tử thay bản giấy không — đây là rủi ro chính của phần khách ký.

**Phục vụ ai:** lái xe (người lập biên bản), điều vận (nhận biên bản, xử lý bất thường), kế toán (đối chiếu công nợ), khách (người ký nhận).

***

## 2. Đối thủ làm thế nào

| | **Delta (dự kiến)** | Abivin | CETA | LogisViet | Draymate | Detrack |
|---|---|---|---|---|---|---|
| **Có biên bản điện tử?** | Chưa — giấy và ảnh chụp | Có | Có, mô tả sơ lược | Có | Một phần — chỉ chữ ký | Có |
| **Khách xác nhận thế nào** | Ký giấy | Ký trên màn hình, mã OTP, vùng địa lý | Ký, quét QR trên đơn | Ký kèm ảnh | Ký trên máy lái xe | Ký trên máy lái xe, có thể bắt buộc tên người nhận |
| **Mục riêng cho container, chì** | Có trong mẫu giấy theo SOP | Không thấy | Có nêu số chì, container | Ảnh container và ảnh chì | Chưa | Không |
| **Ghi bất thường** | Quy định nhưng chưa có công cụ | Không rõ | Không rõ | Không rõ | Chưa có ảnh hàng hỏng | Tối đa 10 ảnh, quản trị bắt buộc được ảnh và trường thông tin, phải đúng bước mới hoàn tất |
| **Dùng khi mất sóng** | — | Có | Có | Có | Không rõ | Có |
| **Thời gian, vị trí** | Ghi tay | Tự gắn giờ và vị trí | Có vị trí | Có vị trí | Đang làm | Tự gắn giờ và vị trí |
| **Chỗ Delta khai thác được** | — | Mục container, chì | Chặn hoàn tất khi thiếu bất thường | Chặn hoàn tất khi thiếu bất thường | Bất thường, mất sóng | Mục container, chì, nối công nợ |
| *Giá* | *Nội bộ* | *Không công khai* | *Không công khai* | *Không công khai* | *App miễn phí kèm phần mềm điều vận* | *29–39 USD/lái xe/tháng* |

*Độ tin cậy: Detrack và Draymate lấy từ trang sản phẩm và trang giá chính thức, chắc chắn có nguồn. Abivin, CETA, LogisViet chủ yếu từ trang giới thiệu dạng liệt kê tính năng — chưa xem trực tiếp màn hình nên chưa rõ tính năng nào là bắt buộc hay tuỳ chọn. Không đối thủ nào công bố cách nối biên bản với công nợ hay cách xử lý khi khách từ chối ký điện tử.*

**Mấy điểm chung rút ra:**
* Ký trên máy lái xe kèm ảnh là mặc định; OTP và mã QR là lớp thêm.
* Sản phẩm làm kỹ nhất cho quản trị chọn mục nào bắt buộc và khoá hoàn tất theo bước — đúng cơ chế cần để thi hành nguyên tắc "ghi bất thường trước khi rời điểm".
* Phần mềm giao hàng nói chung không có mục dành cho container và chì; phần mềm vận tải container trong nước có ảnh chì nhưng không công bố cách bắt buộc ghi bất thường.

**Về giá trị pháp lý** (tham khảo, chưa phải ý kiến luật sư): theo các bài tóm tắt Luật Giao dịch điện tử số 20/2023/QH15 (hiệu lực từ 1/7/2024), chữ ký điện tử thông thường như vẽ trên màn hình hay mã OTP không bị phủ nhận giá trị chỉ vì ở dạng điện tử, nhưng không tự động ngang chữ ký tay; chữ ký số mới có giá trị tương đương. Các bên được thoả thuận loại chữ ký điện tử dùng với nhau — nên ghi điều khoản chấp nhận biên bản điện tử vào hợp đồng hoặc phụ lục với khách. Chưa đọc được văn bản gốc nên số điều luật cần kiểm lại.

***

## 3. Nếu làm thì lưu ý gì

**Cách làm đề xuất:** Làm phần ghi nhận giao hàng có cấu trúc trên App Lái xe cùng lúc với Lệnh vận tải; phần khách ký điện tử chạy thử sau với nhóm khách đã đồng ý.

**Lưu ý:**
* **Thông tin cần lưu:** các mục theo mẫu biên bản SOP (ngày giờ, địa điểm, khách, số container, số chì, tình trạng chì, biển số, lái xe, số lượng và tình trạng hàng); có hay không bất thường kèm mô tả và ảnh; ảnh biên bản giấy đã ký; chữ ký và tên người ký phía khách (phần B); giờ, vị trí ghi nhận; lý do khi khách không ký điện tử; trạng thái đã đồng bộ hay chưa.
* **Rủi ro trải nghiệm:** bắt quá nhiều thao tác tại điểm giao làm lái xe mất thời gian hoặc nhập qua loa; kho, nhà máy hay mất sóng; người ký phía khách thường là thủ kho hoặc bảo vệ nên mã OTP gửi điện thoại có thể không hợp.
* **Phụ thuộc:** Lệnh vận tải của mảng điều phối (để tự điền số container, chì, biển số, lái xe); App Lái xe đang có; điều khoản hợp đồng với khách (cho phần B).
* **Chi phí duy trì:** lưu trữ ảnh lâu dài; cập nhật mẫu biên bản khi SOP đổi.

**Đừng mắc mấy lỗi này:**
* Chỉ lưu ảnh chụp tờ giấy — không đối chiếu công nợ theo số container, số chì được; đây chính là chỗ vướng của cách gửi Zalo hiện nay.
* Có biên bản điện tử nhưng không bắt buộc bước ghi bất thường — lái xe sẽ bỏ qua, trong khi SOP coi đây là điểm quyết định trách nhiệm.
* Thiết kế chỉ cho luồng ký điện tử — khách từ chối là lái xe kẹt tại điểm giao. Phải có lối thoát ký giấy, chụp ảnh và ghi lý do.
* Tin chữ "chống sửa" của nhà cung cấp mà không có cơ chế rõ — tự định nghĩa: khoá sau khi ký, sửa thì ghi lịch sử.

***

## 4. Nên làm không

**Mức độ ưu tiên (xếp thô để so với tính năng khác):** Giá trị vừa đến cao (đánh vào căn cứ công nợ và quy trách nhiệm), công sức M, có thể lên L vì phải chạy được khi mất sóng, độ tin cậy nhận định vừa (chưa có số liệu, chưa biết khách chấp nhận). Xếp nhóm vừa đến cao; phụ thuộc thiết kế Lệnh vận tải.

**Kết luận: NÊN LÀM — có điều chỉnh, tách 2 phần.**

Nhu cầu ghi nhận giao nhận và bất thường đúng lúc là yêu cầu cứng của SOP, và các phần mềm được xem chưa ai công bố đúng phần Delta cần: mục container và chì, bắt buộc ghi bất thường, lối thoát khi khách không ký. Điểm mấu chốt là phần giá trị lớn nhất không phụ thuộc vào việc khách có chấp nhận chữ ký điện tử — nên làm ngay được, còn phần khách ký thì chạy thử:

* **Phần A — làm cùng mảng điều phối:** ghi nhận giao hàng có cấu trúc trên App Lái xe, tự điền từ Lệnh vận tải, bắt buộc chọn có/không bất thường và chụp ảnh chì, hàng trước khi được hoàn tất, đính kèm ảnh biên bản giấy đã ký, dùng được khi mất sóng.
* **Phần B — chạy thử với khách đã đồng ý:** khách ký trên máy lái xe, khoá biên bản sau khi ký; đo tỷ lệ ký và từ chối; chỉ bỏ hẳn giấy khi đã có điều khoản trong hợp đồng.

Nhu cầu vẫn dựa trên SOP chứ chưa đo bằng số liệu thiệt hại.

**Các góc nhìn đã cân nhắc:** Ba góc nhìn ủng hộ, phản đối và khả thi đều đồng ý không bỏ giấy ngay, phải có lối thoát khi khách từ chối ký, và chỉ chạy thử ký điện tử với khách đã đồng ý. Góc nhìn phản đối muốn làm trước chỉ luồng chụp ảnh biên bản giấy vì chưa có số liệu biện minh cho công sức lớn hơn; góc nhìn khả thi lưu ý phần mất sóng có thể đẩy công sức lên mức lớn. Kết luận gộp: phần A đã bao gồm luồng chụp ảnh giấy, chỉ thêm dữ liệu có cấu trúc và bước bắt buộc ghi bất thường — hai thứ SOP thực sự cần — nên không tách thành bước riêng.

***

## 5. Bước tiếp theo

**Các phần đề xuất làm (mỗi phần đủ gọn để brainstorm riêng):**

1) **Ghi nhận giao hàng trên App Lái xe** — mục theo mẫu biên bản SOP, tự điền từ Lệnh vận tải, bắt buộc ghi bất thường và ảnh trước khi hoàn tất, đính kèm ảnh biên bản giấy, dùng được khi mất sóng; điều vận thấy ngay khi lái xe hoàn tất hoặc báo bất thường.
2) **Khách ký điện tử (chạy thử)** — khách ký trên máy lái xe, khoá sau khi ký, ghi lý do khi khách từ chối, gửi bản PDF cho khách.

**Việc cần làm:**
* [ ] Khi brainstorm mảng điều phối, đưa phần 1 vào phạm vi App Lái xe gắn với Lệnh vận tải.
* [ ] Hỏi một vài khách thường xuyên xem có chấp nhận biên bản điện tử không, và ai là người ký phía khách.
* [ ] Nhờ pháp chế hoặc luật sư xem điều khoản chấp nhận biên bản điện tử trong hợp đồng.

**Câu hỏi còn mở:**
* [ ] Khách nào sẵn sàng thử biên bản điện tử?
* [ ] Có cần luật sư xem điều khoản hợp đồng trước khi chạy thử không?
* [ ] Người ký phía khách thường là thủ kho, bảo vệ hay đại diện có thẩm quyền?
* [ ] Bản giấy có bắt buộc đóng dấu với một số khách không?

***

## Nguồn

1) SOP Giao nhận container, Mục 3 và Mục 5 — `docs-input/sop/sop-giao-nhan-container.md` — 2026-08-21
2) SOP Điều phối, các bước chụp ảnh và tải biên bản lên Lệnh vận tải — `docs-input/sop/sop-dieu-phoi.md`
3) Abivin — Bằng chứng giao hàng điện tử — [https://www.abivin.com/vi/blog/it-truyen-thong-7/bang-chung-giao-hang-dien-tu-epod-la-gi-1745](https://www.abivin.com/vi/blog/it-truyen-thong-7/bang-chung-giao-hang-dien-tu-epod-la-gi-1745) — 2026-10-02
4) Abivin vRoute — [https://www.abivin.com/vroute](https://www.abivin.com/vroute) — 2026-10-02
5) CETA — Danh sách chức năng — [https://help.ceta.vn/kb/uncategorized/danh-sach-chuc-nang-giai-phap-ceta/](https://help.ceta.vn/kb/uncategorized/danh-sach-chuc-nang-giai-phap-ceta/) — 2026-10-02
6) CETA — Hướng dẫn app tài xế — [https://help.ceta.vn/kb/huong-dan-nghiep-vu-tai-xe/mobile-nghiep-vu-tai-xe/](https://help.ceta.vn/kb/huong-dan-nghiep-vu-tai-xe/mobile-nghiep-vu-tai-xe/) — 2026-10-02
7) LogisViet — Tính năng — [https://logisviet.com/tinh-nang.html](https://logisviet.com/tinh-nang.html) — 2026-10-02
8) Draymate — Driver mobile apps — [https://draymate.com/drayage-software-driver-mobile-apps](https://draymate.com/drayage-software-driver-mobile-apps) — 2026-10-02
9) Detrack — Electronic proof of delivery — [https://www.detrack.com/electronic-proof-of-delivery/](https://www.detrack.com/electronic-proof-of-delivery/) — 2026-10-02
10) Detrack — Bảng giá — [https://www.detrack.com/pricing/](https://www.detrack.com/pricing/) — 2026-10-02
11) Bộ Khoa học và Công nghệ — Chữ ký điện tử theo luật cũ và mới — [https://mst.gov.vn/hoi-dap/viec-ca-nhan-su-dung-chu-ky-dien-tu-theo-luat-cu-va-luat-moi-14818.htm](https://mst.gov.vn/hoi-dap/viec-ca-nhan-su-dung-chu-ky-dien-tu-theo-luat-cu-va-luat-moi-14818.htm) — 2026-10-02
12) Luật sư Việt Nam — Giá trị pháp lý của chữ ký điện tử — [https://lsvn.vn/gia-tri-phap-ly-cua-chu-ky-dien-tu-duoc-quy-dinh-the-nao-1697702148-a136561.html](https://lsvn.vn/gia-tri-phap-ly-cua-chu-ky-dien-tu-duoc-quy-dinh-the-nao-1697702148-a136561.html) — 2026-10-02
13) Trung tâm Chứng thực điện tử quốc gia — Luật Giao dịch điện tử có hiệu lực từ 1/7/2024 — [https://ceca.gov.vn/luat-giao-dich-dien-tu-co-hieu-luc-tu-1-7-2024-co-hoi-de-chuyen-doi-so-viet-nam-but-pha/](https://ceca.gov.vn/luat-giao-dich-dien-tu-co-hieu-luc-tu-1-7-2024-co-hoi-de-chuyen-doi-so-viet-nam-but-pha/) — 2026-10-02
