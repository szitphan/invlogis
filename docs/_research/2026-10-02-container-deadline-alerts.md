---
type: research
keyword: "cảnh báo mốc SI/CY/DEM/DET"
status: draft
updated: 2026-10-02
links:
  - docs-input/Giao_nhan_container_2.md
  - docs-input/Quy_trinh_dieu_phoi.md
  - docs-input/Quy_trinh_cung_cap_dich_vu_tong_quat.md
---

# Cảnh báo mốc SI / CY / DEM / DET

> **Khuyến nghị: NÊN LÀM — có điều chỉnh, theo 2 bước.** CS và điều vận cần biết sớm lô nào sắp trễ mốc để kịp xử lý trước khi phát sinh phí, nhưng hiện chưa có số liệu thiệt hại thật — nên đo trước bằng bảng kế hoạch đang có, rồi mới đưa cảnh báo vào phần mềm.

***

## Tóm tắt

SOP giao nhận container coi trễ mốc là nguồn phát sinh chi phí thường xuyên nhất (rớt tàu, phí lưu container, phí sửa vận đơn) và đã quy định sẵn cách cảnh báo, nhưng việc rà vẫn làm tay và chưa ai đo thiệt hại thực tế. Ba phần mềm vận tải trong nước được xem không công khai tính năng cảnh báo bốn mốc này — cảnh báo của họ dừng ở GPS, lộ trình, hạn giấy tờ xe. Hai sản phẩm quốc tế làm tốt việc này (Dockflow, BuyCo) nhưng phục vụ forwarder và chủ hàng, không gắn mốc với lệnh vận tải và xe. Khuyến nghị: bổ sung cột vào bảng kế hoạch để đo trong một thời gian, đồng thời giữ chỗ bốn mốc trong thiết kế dữ liệu mảng điều phối; đưa cảnh báo vào phần mềm khi số liệu xác nhận.

***

## 1. CS và điều vận cần gì

CS và điều vận cần:

1) **Biết sớm lô/container nào sắp trễ mốc** — đủ sớm để điều xe, báo khách và hãng tàu bằng văn bản, hoặc xin gia hạn trước khi bị tính phí.
2) **Biết ai đang xử lý và đã xử lý tới đâu** — để không lô nào bị bỏ sót giữa các ca, các người.
3) **Có căn cứ quy trách nhiệm khi đã trễ** — ghi được nguyên nhân thuộc khách, thuộc Delta hay thuộc bên thứ ba để quyết bên nào trả phí.

Bốn mốc theo SOP:

| Mốc | Nghĩa | Cảnh báo trước | Nếu trễ |
|---|---|---|---|
| SI | Hạn Delta cung cấp số container và số chì cho khách, theo Booking Note | 24 giờ | Phí sửa hoặc phát hành vận đơn muộn, có thể chuyển chuyến |
| CY (cut-off) | Hạn hạ container hàng xuất về cảng, đối chiếu bằng giờ trên Phiếu EIR hạ hàng | 12 giờ | Rớt tàu, phí lưu bãi, phí đổi Booking Note |
| DEM | Hạn lưu container hàng nhập miễn phí tại cảng, tính từ khi tàu cập, ghi trên Lệnh giao hàng | 2 ngày | Phí lưu container hàng |
| DET | Số ngày miễn phí giữ container ngoài cảng, tính từ giờ EIR nhận container đến khi trả vỏ đúng nơi hãng chỉ định | 2 ngày | Phí lưu container |

**Vì sao đáng làm:** Mỗi lần trễ là một khoản phí thật, và theo SOP đây là loại phí phát sinh thường xuyên nhất. Việc rà hàng ngày bằng tay phụ thuộc trí nhớ và sự chú ý của từng người; trễ một mốc CY là mất cả chuyến tàu. Quy định ghi nguyên nhân theo 3 nhóm cũng chỉ có tác dụng khi được ghi đều đặn.

**Bằng chứng nhu cầu:**
* SOP Giao nhận container (Mục 4) nêu rõ DEM/DET là nguồn phát sinh chi phí thường xuyên nhất và quy định ngưỡng cảnh báo cho cả bốn mốc.
* Chưa có số liệu thật: không có thống kê số lần rớt tàu, số tiền phí DEM/DET hay phí sửa vận đơn mỗi tháng. Mức độ thiệt hại hiện là nhận định của người viết SOP, chưa được đo.

**Phục vụ ai:** CS (ghi mốc khi nhận Booking Note, Lệnh giao hàng), điều vận (rà và cảnh báo hằng ngày, điều xe), quản lý (xem lô quá hạn và nguyên nhân).

***

## 2. Đối thủ làm thế nào

| | **Delta (dự kiến)** | XLogis | LogisViet | Smartlog | Dockflow | BuyCo |
|---|---|---|---|---|---|---|
| **Có cảnh báo bốn mốc?** | Chưa có — đang làm tay theo SOP | Không thấy | Không thấy | Không thấy | Có | Có |
| **Lấy mốc từ đâu** | CS ghi tay từ Booking Note, Lệnh giao hàng | Không rõ | Không rõ | Không rõ | Dữ liệu hãng tàu, vị trí tàu, dữ liệu cảng; ngày hết hạn tính theo quy tắc từng hãng, cảng, hợp đồng | Dữ liệu booking và điều khoản hợp đồng với hãng tàu |
| **Cách cảnh báo** | Ngưỡng cố định 24 giờ / 12 giờ / 2 ngày, báo bằng văn bản | Chỉ cảnh báo tiêu hao nhiên liệu | Cảnh báo GPS, giao thông, hạn đăng kiểm và giấy tờ xe | Cảnh báo lộ trình, điểm dừng lạ, qua SMS và email | Người dùng tự chọn báo trước bao lâu, hiện luôn ngày hết hạn miễn phí | Ba mức: bình thường / sắp tới hạn / đang phát sinh phí |
| **Ghi nguyên nhân, quy trách nhiệm** | Có quy định 3 nhóm nguyên nhân, ghi tay | Không thấy | Không thấy | Không thấy | Không — chỉ theo dõi thời gian, không tính tiền phí | Có — gom bằng chứng theo từng mốc, lọc theo bên chịu trách nhiệm, đối chiếu hoá đơn hãng tàu |
| **Hợp với Delta?** | — | Cùng thị trường nhưng không phủ việc này | Cùng mô hình xe đầu kéo nhưng không phủ việc này | Thiên về chủ hàng | Hướng forwarder, chưa rõ có phủ cảng Việt Nam | Hướng chủ hàng quy mô lớn |
| **Chỗ Delta khai thác được** | — | Gắn mốc với lệnh vận tải | Gắn mốc với lệnh vận tải | Gắn mốc với lệnh vận tải | Góc nhìn nhà vận tải, quy trách nhiệm | Thêm nhóm nguyên nhân "do nhà vận tải" |
| *Giá* | *Nội bộ* | *Không công khai* | *Không rõ* | *Không công khai* | *Không công khai* | *Thuê bao, từ khoảng 500 USD/tháng* |

*Độ tin cậy: thông tin về Dockflow và BuyCo lấy từ trang sản phẩm chính thức, chắc chắn có nguồn. Kết luận "không thấy" ở ba phần mềm trong nước chỉ dựa trên trang giới thiệu công khai — có thể họ làm theo yêu cầu riêng mà không công bố, cần hỏi trực tiếp nếu muốn chắc. Giá BuyCo lấy từ trang đánh giá phần mềm, chưa đối chiếu trang giá gốc.*

**Mấy điểm chung rút ra:**
* Phần mềm vận tải trong nước dừng ở cảnh báo xe (GPS, lộ trình, giấy tờ), chưa thấy ai cảnh báo mốc của cảng và hãng tàu.
* Sản phẩm làm tốt việc này tính ngày hết hạn từ **bộ quy tắc theo hãng, cảng, hợp đồng**, không bắt người dùng nhập tay từng lô.
* Không ai trong số đã xem nhìn từ phía nhà vận tải, nơi lệnh vận tải, xe và lái xe quyết định có kịp CY hay trả vỏ đúng hạn hay không.

***

## 3. Nếu làm thì lưu ý gì

**Cách làm đề xuất:** Đo trước bằng bảng kế hoạch đang dùng; trong lúc đó giữ chỗ bốn mốc trong thiết kế mảng điều phối. Khi đưa vào phần mềm, làm phần theo dõi và xử lý cảnh báo trước; việc tự lấy mốc từ chứng từ hoặc kết nối ePort để sau.

**Lưu ý:**
* **Thông tin cần lưu:** bốn mốc của từng lô/container kèm nguồn chứng từ và người xác nhận; trạng thái của mốc (đã xác nhận / chờ xác minh); người phụ trách xử lý; trạng thái xử lý cảnh báo; nhóm nguyên nhân khi quá hạn; lịch sử sửa mốc.
* **Rủi ro trải nghiệm:** mốc ghi sai thì mọi cảnh báo sau đều sai, cảnh báo sai nhiều sẽ làm điều vận mất niềm tin và bỏ qua cả cảnh báo đúng. Bắt CS nhập đủ bốn mốc ngay khi tạo lô là không thực tế — mốc DEM/DET có thể chưa có lúc nhận Booking Note.
* **Phụ thuộc:** gắn với lệnh vận tải của mảng điều phối; mốc DET cần giờ trên Phiếu EIR nhận container thật (liên quan chủ đề chụp và đọc chứng từ, kết nối ePort).
* **Chi phí dữ liệu:** nếu cần bảng ngày miễn phí DEM/DET theo hãng tàu thì phải có người duy trì khi hãng đổi chính sách.

**Đừng mắc mấy lỗi này:**
* Nhầm cảnh báo xe (GPS, giấy tờ) với cảnh báo mốc cảng — như các phần mềm trong nước hiện có: người dùng tưởng "đã có cảnh báo" nhưng không bắt được đúng mốc gây phí.
* Hứa tính chính xác số tiền phí khi chưa có biểu phí từng hãng — Dockflow cũng tránh việc này, chỉ theo dõi thời gian.
* Cảnh báo mà không có người nhận, không có bước "đã xử lý" và không leo thang — cảnh báo sẽ thành tiếng ồn.
* Dùng một quy tắc cứng cho mọi hãng tàu trong khi ngày miễn phí khác nhau theo hãng và hợp đồng.

***

## 4. Nên làm không

**Mức độ ưu tiên (xếp thô để so với tính năng khác):** Giá trị cao (đánh vào loại phí phát sinh thường xuyên nhất theo SOP), công sức M, độ tin cậy nhận định thấp đến vừa (chưa có số liệu thiệt hại). Xếp nhóm vừa; nâng lên khi có số liệu.

**Kết luận: NÊN LÀM — có điều chỉnh, theo 2 bước.**

Nhu cầu biết sớm lô sắp trễ mốc là có thật trên quy trình, và chưa phần mềm vận tải trong nước nào được xem làm việc này, nên đây là phần Delta tự làm được giá trị riêng: gắn mốc với lệnh vận tải và quy trách nhiệm theo 3 nhóm nguyên nhân. Nhưng mức thiệt hại hiện chỉ là nhận định, và chất lượng mốc nhập tay là rủi ro lớn nhất. Vì vậy:

* **Bước 0 — làm ngay, chưa cần phần mềm:** thêm vào bảng kế hoạch hiện có các cột người phụ trách, nguồn chứng từ của mốc, trạng thái xử lý, nhóm nguyên nhân khi quá hạn; đồng thời lấy thống kê hoá đơn DEM/DET và phí sửa vận đơn của hãng tàu trong vài tháng gần nhất từ kế toán.
* **Bước 1 — đưa vào phần mềm khi số liệu xác nhận:** làm phần theo dõi và xử lý cảnh báo trong mảng điều phối. Thiết kế dữ liệu mảng điều phối giữ chỗ cho bốn mốc ngay từ bây giờ.

**Các góc nhìn đã cân nhắc:** Ba góc nhìn ủng hộ, phản đối và khả thi đều đồng ý nên làm, không bắt buộc nhập đủ bốn mốc khi tạo lô mà cho phép trạng thái "chờ xác minh", và chưa làm việc đọc chứng từ tự động, kết nối ePort hay tính tiền phí. Điểm còn lệch là làm ngay hay đo trước: sau một vòng phản biện, hai trên ba góc nhìn chọn đo trước vì chưa có số liệu và lo dữ liệu nhập tay sai. Kết luận theo hướng đo trước, nhưng không coi là việc tách rời: bảng kế hoạch đã có sẵn nên chỉ tốn công thêm cột, còn mảng điều phối đang được thiết kế nên giữ chỗ bốn mốc gần như không tốn thêm.

***

## 5. Bước tiếp theo

**Các phần đề xuất làm (mỗi phần đủ gọn để brainstorm riêng):**

1) **Theo dõi bốn mốc theo lô** — gắn với lệnh vận tải; đếm ngược và ba mức trạng thái (bình thường / sắp tới hạn / đã quá hạn) theo ngưỡng cấu hình được; mốc "chờ xác minh" kèm nguồn chứng từ; lịch sử sửa mốc.
2) **Xử lý cảnh báo** — giao người phụ trách; leo thang khi quá ngưỡng mà chưa có hành động; bắt buộc chọn nhóm nguyên nhân khi quá hạn; soạn sẵn văn bản báo khách và hãng tàu.

**Việc cần làm:**
* [ ] Thêm cột người phụ trách, nguồn chứng từ, trạng thái xử lý, nhóm nguyên nhân vào bảng kế hoạch đang dùng.
* [ ] Nhờ kế toán thống kê hoá đơn DEM/DET và phí sửa vận đơn của hãng tàu trong vài tháng gần nhất.
* [ ] Khi brainstorm mảng điều phối, giữ chỗ bốn mốc trong dữ liệu lô và lệnh vận tải.
* [ ] Khi có số liệu, chạy `/brainstorm` cho hai phần đề xuất ở trên.

**Câu hỏi còn mở:**
* [ ] SOP có dòng "Cái này không cần" ngay sau yêu cầu lập bảng ngày miễn phí DEM/DET theo hãng tàu — là bỏ yêu cầu này, hay ghi chú còn sót từ bản nháp?
* [ ] Khi cảnh báo leo thang thì báo cho ai (trưởng điều vận, quản lý CS)?
* [ ] Đo bằng bảng kế hoạch trong bao lâu thì đủ để quyết định đưa vào phần mềm?

***

## Nguồn

1) SOP Giao nhận container, Mục 4 — `docs-input/Giao_nhan_container_2.md` — 2026-08-21
2) Dockflow — Demurrage tracking — [https://dockflow.com/platform/demurrage-tracking/](https://dockflow.com/platform/demurrage-tracking/) — 2026-10-02
3) BuyCo — Detention and Demurrage — [https://buyco.co/container-shipping-solutions/demurrage-and-detention/](https://buyco.co/container-shipping-solutions/demurrage-and-detention/) — 2026-10-02
4) BuyCo — Best D&D management software — [https://buyco.co/blog/productivity/best-detention-demurrage-management-software/](https://buyco.co/blog/productivity/best-detention-demurrage-management-software/) — 2026-10-02
5) LogisViet — Tính năng — [https://logisviet.com/tinh-nang.html](https://logisviet.com/tinh-nang.html) — 2026-10-02
6) XLogis — [https://xlogis.vn/](https://xlogis.vn/) — 2026-10-02
7) FBS — XMan Logistics — [https://fbs.com.vn/san-pham/phan-mem-quan-ly-van-tai-xman-logistics-2](https://fbs.com.vn/san-pham/phan-mem-quan-ly-van-tai-xman-logistics-2) — 2026-10-02
8) Smartlog — Track & Trace — [https://gosmartlog.com/track-trace/](https://gosmartlog.com/track-trace/) — 2026-10-02
9) BuyCo trên Capterra (giá) — [https://www.capterra.com/p/179235/BUYCO/](https://www.capterra.com/p/179235/BUYCO/) — 2026-10-02
