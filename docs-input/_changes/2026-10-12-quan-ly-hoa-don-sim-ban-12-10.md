# Thay đổi: SOLUTIONS FOR INVOICE MANAGEMENT (SIM)

> Bản cũ: nhận 2026-10-11 (`SIM_Oct 11 2026.pdf`, 19 trang) · Bản mới: nhận 2026-10-12 (`SIM_Oct 12 2026.pdf`, 16 trang) · Tài liệu: [quan-ly-hoa-don-sim.md](../sop/quan-ly-hoa-don-sim/quan-ly-hoa-don-sim.md)

## Tóm tắt nghiệp vụ

- **Đổi tên trợ lý AI.** Trợ lý tạo JobID từ chứng từ (bản cũ là AI02, mục 2.3) nay là **AI01**, mục 2.2. Mục 2.2 cũ "Quản lý hóa đơn đầu vào (AI01)" bị bỏ. Việc xử lý hóa đơn đầu vào nay thuộc **Phân hệ IIP** (Incoming Invoice Processing), mục 3.3, không còn gọi là trợ lý AI.
  - ⚠ Phần đầu 2.1 và bảng 2.1.1 vẫn ghi "Trợ lý AI01 đối chiếu chéo, định danh hóa đơn / AI01 đối soát hóa đơn". Hai chỗ này sót từ bản cũ, mâu thuẫn với nghĩa AI01 mới (tạo JobID).
  - ⚠ Tài liệu "SIM & VIS – Công tác chuẩn bị" (SRC-24, 11/10) cũng gọi AI01 là bộ đọc hóa đơn.
- **Nơi giữ giao dịch ngân hàng chờ đối chiếu** đổi từ "bộ nhớ đệm cache của AI01" thành **Cơ sở dữ liệu tạm thời (Staging Database/Table)**. Sơ đồ sổ phụ 2.1.2 cũng đổi theo.
- **Hóa đơn đầu vào chia 2 luồng theo cách nhân viên đã chi tiền** (mục 3.3.4, Bước 4):
  - **Chi qua API Banking:** khớp với giao dịch thì hóa đơn đóng, khóa không dùng lại và gắn lên JobID. Hệ thống tự ghi giảm "Dư nợ tạm ứng 2" của nhân viên trên MISA AMIS.
  - **Chi bằng tiền mặt hoặc thẻ cá nhân** (mới): không tìm thấy giao dịch đối ứng thì hóa đơn vào danh mục **Hóa đơn vô chủ**. Cán bộ quản lý duyệt bước 1, Kế toán tổng hợp duyệt bước 2. Duyệt xong, hệ thống tự tạo **Phiếu chi** trên AMIS và chuyển sang **Quy trình 5.8** (Quản lý quỹ & thanh toán) để **hoàn tiền vào tài khoản của nhân viên** đã tải hóa đơn.
- **Nghĩa của "Hóa đơn vô chủ" đổi** (mục 3.3.5 mới).
  - Bản cũ: hóa đơn trả hộ không khớp vì đối tác gộp hoặc tách hóa đơn. Xử lý bằng cách ghi giảm Dư nợ tạm ứng 2 của người làm Yêu cầu thanh toán, chỉ thêm 1 bước duyệt của Kế toán tổng hợp.
  - Bản mới: chủ yếu là chi tiêu cá nhân cần hoàn tiền (vẫn gồm "lỗi đối chiếu gộp"). Duyệt 2 bước, rồi hoàn tiền.
  - ⚠ Cần hỏi khách: hóa đơn vô chủ do lỗi gộp/tách mà thực ra đã chi qua ngân hàng thì có đi luồng hoàn tiền không. Theo bản mới, có nguy cơ hoàn tiền cho khoản đã chi bằng tiền công ty. Bản mới chỉ có "gợi ý đối chiếu" cho kế toán soi chéo.
- **Mới: khớp nhiều–một và một–nhiều**, do khách giao cho BA phát triển tiếp:
  - **N-1** (nhiều UNC, 1 hóa đơn): Kế toán viên tick chọn nhiều giao dịch "Chờ đối soát" để gộp với 1 hóa đơn, tổng tiền phải bằng đúng tiền hóa đơn.
  - **1-N** (1 UNC, nhiều hóa đơn): giao dịch chuyển sang trạng thái "Khớp một phần (Số tiền còn lại: …)" và nằm trong danh sách đối soát đến khi đủ tiền.
- **Kiểm trùng hóa đơn mở rộng:** từ chối cả hóa đơn **đang chờ duyệt thanh toán ở hồ sơ khác**, không chỉ hóa đơn đã có trong lịch sử. Khóa trùng vẫn là Mã số thuế người bán + Ký hiệu + Số hóa đơn.
- **Hóa đơn PDF/ảnh** gọi Google Document AI **hoặc Cloud Vision API**. Bản cũ chỉ ghi Document AI.
- **Bỏ một số ý của bản cũ:**
  - Tự hoàn thành Phân loại bước 2 (chi phí trả hộ theo JobID) khi khớp.
  - Lấy Số JobID bằng Regex từ nội dung Yêu cầu thanh toán.
  - Gom hóa đơn từ Cục thuế hoặc email forward qua Misa (bản mới chỉ ghi "gom tự động từ Misa meInvoice").
  - Hai trạng thái "Chưa làm thanh toán / Đã làm thanh toán" của danh mục hóa đơn.
- **Phê duyệt Yêu cầu thanh toán (3.1.3, Bước 3):** bỏ dòng nói rõ 2 nhánh "Phê duyệt → Bước 4 / Từ chối → trả về Bước 1". Ngưỡng QR còn hiệu lực ≥ 3 phút giữ nguyên. ⚠ Nhánh từ chối vẫn cần có trong luồng, chỉ là tài liệu không ghi nữa.
- **Phụ lục 5.2 bỏ Techcombank.** Chỉ còn MB Bank, TP Bank, Vietcombank (chờ báo giá), khớp với thân bài. Câu hỏi về Techcombank trong BL-048 coi như đã có đáp án.
- **Mục lục đã khớp thân bài.** Câu hỏi "mục lục lệch thân bài" trong BL-048 không còn cần hỏi.
- **Công tác chuẩn bị (2.3)** chỉ còn nói tới AI01: Google Cloud, bộ xử lý, khóa truy cập, hạn mức gọi API.

## Đổi số mục

| Mục cũ (11/10) | Mục mới (12/10) |
|---|---|
| 2.2 Quản lý hóa đơn đầu vào (AI01) | bỏ, nội dung chuyển vào 3.3 (Phân hệ IIP) |
| 2.3 Tạo JobID nghiệp vụ (AI02), 2.3.1–2.3.4 | 2.2 Tạo JobID nghiệp vụ (AI01), 2.2.1–2.2.4 |
| 2.4 Công tác chuẩn bị, 2.4.1 | 2.3 Công tác chuẩn bị, 2.3.1 |
| 3.3.1 Sơ đồ kiến trúc hệ thống | 3.3.2 Sơ đồ kiến trúc hệ thống (vẽ lại) |
| 3.3.2 Sơ đồ luồng dữ liệu (sơ đồ 10 bước) | 3.3.3 Sơ đồ luồng dữ liệu (4 bước dạng chữ, không còn hình) |
| 3.3.3.1–3.3.3.5 Quy trình nghiệp vụ | 3.3.4 Quy trình nghiệp vụ & Logic xử lý chi tiết (Bước 1–4) |
| 3.3.4 Các trường hợp đặc biệt | 3.3.5 Hóa đơn vô chủ |
| — | 3.3.1 Nguyên lý vận hành (mới) |
| 5.2 dòng 3 Techcombank, dòng 4 Vietcombank | dòng 3 Vietcombank |

## Tài liệu đang dùng nguồn này

- `docs/service-delivery/brainstorms/service-delivery.md`: chỉ trích ở `links`. Rà phần tạo JobID (nay là AI01, mục 2.2) và chặn tạo JobID khi nợ xấu (2.1.2).
- `docs/transport-dispatch/brainstorms/transport-dispatch.md`: chỉ trích ở `links`. Rà phần lái xe tải hóa đơn hoặc chi tiền mặt, vì hóa đơn của luồng đó nay vào Hóa đơn vô chủ và đi luồng hoàn tiền.
- `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md`: OQ-17 (7.000 hóa đơn trả hộ/tháng, không đổi) và OQ-32 (UNC qua API, không đổi). BL-048 có thể bỏ câu hỏi Techcombank và mục lục, thêm câu hỏi về nghĩa AI01 và hóa đơn vô chủ.
- `docs/_shared/logistics-primer.html`: trích chung, ít bị ảnh hưởng.

## Chi tiết

## Tổng quan thay đổi

| Loại | Số mục | Mục |
|---|---|---|
| Thêm mới | 3 | 3.3.1. Nguyên lý vận hành; 3.3.4. Quy trình nghiệp vụ & Logic xử lý chi tiết; 3.3.5. Hóa đơn vô chủ |
| Bỏ | 10 | 2.2. Quản lý hóa đơn đầu vào (AI01); 2.2.3. Các trường hợp đặc biệt; 3.3.1. Sơ đồ kiến trúc hệ thống (System architecture); 3.3.2. Sơ đồ luồng dữ liệu (Data flow); 3.3.3.1. Định danh giao dịch qua luồng API Banking; 3.3.3.2. Thu thập hóa đơn tự động qua Misa API Gateway; 3.3.3.3. Trợ lý AI01 thực hiện quét & đọc và trích xuất thông tin hóa đơn; 3.3.3.4. Đối chiếu chéo (AI01 cross-matching) để mapping; 3.3.3.5. Kiểm soát hóa đơn trùng & Gửi thông báo; 3.3.4. Các trường hợp đặc biệt (Exceptional case) |
| Sửa | 26 | SOLUTIONS FOR INVOICE MANAGEMENT (SIM); MỤC LỤC; 2.1. Luồng thanh toán tự động qua API Banking; 2.1.2. Luồng số hóa Sổ phụ ngân hàng để quản lý công nợ; 2.1.3. Quy trình thanh toán qua API Banking; 3.3.3. Sơ đồ luồng dữ liệu; 2.2.3. Quy trình nghiệp vụ; Bước 1: Tiếp nhận và Trích xuất thông tin hóa đơn (Parsing & OCR Engine); Bước 2: Đối chiếu chéo tự động (Rule-based Cross-Matching) để định danh; Bước 3: Kiểm soát trùng lặp lịch sử; Bước 4: Điều phối trạng thái danh mục và Xử lý thanh toán phân nhánh; 2.2. Tạo JobID nghiệp vụ (AI01); 2.2.1. Kiến trúc tích hợp Google Document AI; 2.2.2. Quy trình xử lý kỹ thuật qua API; 2.2.4. Luồng tạo JobID thủ công; 2.3. Công tác chuẩn bị; 2.3.1. Các công việc cần chuẩn bị; 3.3.2. Sơ đồ kiến trúc hệ thống; Bước 3: Phê duyệt Yêu cầu thanh toán; Mã QR động hết hạn bị động; 3.2. Phát hành và điều chỉnh hóa đơn tự động (Misa meInvoice); 3.2.1.3. Quy trình phù hợp với Delta; 3.2.2. Sơ đồ kiến trúc luồng dữ liệu (Data Flow); Thay thế / Điều chỉnh hóa đơn đã phát hành; 3.3. Thu thập & định danh hóa đơn đầu vào và làm thanh toán tự động (IIP); 5.2. Chi phí thực hiện kết nối API Banking |
| Giữ nguyên | 24 | |

## Con số thay đổi

| Chỉ có ở bản cũ | Chỉ có ở bản mới |
|---|---|
| 0004-01 | 0004-02 |
| 0005-10 | 0005-08 |
| 0007-12 | 0007-05 |
| 0010-00 | 0011-02 |
| 0013-15 | 0012-08 |
| 0015-00 | 12 |
| 0015-02 | 16 |
| 11 | 2.2.4 |
| 19 | 3.3.5 |
| 2.3.2 | 5.8 |
| 2.3.3 |  |
| 2.3.4 |  |
| 2.4 |  |
| 2.4.1 |  |
| 3.3.3.1 |  |
| 3.3.3.2 |  |
| 3.3.3.3 |  |
| 3.3.3.4 |  |
| 3.3.3.5 |  |
| 6,000 |  |
| 70 |  |
| 8 |  |
| 9 |  |

## Mục thêm mới

### 3.3.1. Nguyên lý vận hành

+ Bản chất nghiệp vụ thanh toán & thu thập hóa đơn của Delta là thực hiện chi tiền trước cho đối tác (phí trả hộ, local charges, vé cầu đường...) qua luồng API Banking hoặc nhân viên chủ động ứng trước tiền cá nhân tại hiện trường. Hóa đơn điện tử sẽ được thu thập về sau. Vì vậy, nhiệm vụ của **Phân hệ IIP** (Incoming Invoice Processing) là hoạt động như một cấu phần xử lý dữ liệu bất đồng bộ để tiếp nhận hóa đơn từ các nguồn, trích xuất dữ liệu, kiểm tra trùng lặp và điều phối luồng thanh toán & hoàn ứng dựa trên phương thức chi ban đầu của nhân viên.

### 3.3.4. Quy trình nghiệp vụ & Logic xử lý chi tiết

+ Hệ thống phân tách luồng xử lý theo định dạng đầu vào để tối ưu hóa chi phí vận hành.

### 3.3.5. Hóa đơn vô chủ

+ Danh mục "Hóa đơn vô chủ" được dùng để quản lý toàn bộ các hóa đơn thuộc **Trường hợp 2** (nhân viên không thanh toán qua luồng API Banking hoặc các lỗi đối chiếu gộp.
+ 1. **Hỗ trợ gợi ý đối chiếu:** Hệ thống tự động quét và hiển thị thông tin định danh hóa đơn kèm theo danh sách các giao dịch API Banking có số tiền tương đương hoặc phát sinh từ cùng một nhân viên trong thời gian gần nhất để kế toán kiểm tra chéo (đề phòng nhân viên quên không nhập JobID khi chuyển khoản).
+ 2. **Quy trình phê duyệt hoàn tiền:** Khi Kế toán tổng hợp xác nhận hóa đơn hoàn toàn là chi phí nhân viên tự chi tiền cá nhân, bước duyệt này sẽ là chốt chặn cuối cùng kích hoạt lệnh chuyển khoản hoàn trả tiền và gán hóa đơn vào đúng JobID nghiệp vụ để tập hợp chi phí.


## Mục bị bỏ

### 2.2. Quản lý hóa đơn đầu vào (AI01)

- Để giải quyết triệt để tình trạng thanh toán trùng lặp, giảm workload nhập liệu thủ công và quản trị dòng tiền chặt chẽ, Delta phát triển trợ lý AI01 nằm trong giải pháp SIM. Để tối ưu hóa chi phí phát triển và vận hành hệ thống, AI01 sử dụng Google Document AI làm dịch vụ xử lý ảnh đầu vào và hoạt động như một phân hệ xử lý bất đồng bộ, hội tụ dữ liệu hóa đơn đầu vào từ hai nguồn:
- - Nguồn tự động (Misa API Gateway): Nhận file XML gốc và PDF từ Cục thuế.
- - Nguồn thủ công (Upload từ Web/App): Do nhân viên hiện trường/lái xe chụp ảnh hoặc tải lên tệp PDF.
- Hệ thống gọi dịch vụ của Google để văn bản hóa dữ liệu thô, sau đó dùng code truyền thống để đối chiếu chéo 1-1 với giao dịch ngân hàng để định danh chủ thể, kiểm soát trùng lặp và phân phối vào danh mục chờ thanh toán hoặc tự động thanh toán.
- Bản chất nghiệp vụ: Toàn bộ các khoản chi (phí trả hộ, phí local charges, vé cầu đường...) và các khoản chi phí khác đều được Delta thực hiện thanh toán trước cho đối tác thông qua luồng API Banking hoặc các phương thức thanh toán khác. Hóa đơn điện tử sẽ được thu thập về hệ thống AI01 sau đó. Vì vậy, nhiệm vụ cốt lõi của AI01 là tiếp nhận hóa đơn, trích xuất dữ liệu, đối chiếu chéo 1- 1 với giao dịch ngân hàng đã chi để tự động định danh (gán JobID/Nhân viên) và đóng trạng thái công nợ ngay lập tức.

### 2.2.3. Các trường hợp đặc biệt

- Nếu luồng API Banking không tìm thấy giao dịch phù hợp (do đối tác xuất hóa đơn gộp nhiều UNC hoặc nhân viên gom nhiều hóa đơn cho một UNC), AI01 chuyển tiếp xử lý theo quy tắc an toàn:
- 1. Chuyển toàn bộ các hóa đơn này sang danh mục "Hóa đơn vô chủ" để cách ly và xử lý thủ công.
- 2. Tại màn hình "Hóa đơn vô chủ", hệ thống hiển thị thông tin định danh của hóa đơn kèm theo danh sách các giao dịch API Banking có số tiền tương đương hoặc phát sinh từ cùng một nhân viên trong thời gian gần nhất để kế toán đối chiếu.
- 3. Áp dụng bước duyệt bổ sung của _Kế toán tổng hợp_ để kiểm tra hai lần trước khi gán hóa đơn vào JobID nghiệp vụ và ghi giảm Dư nợ tạm ứng 2.
- Chi tiết lưu đồ quy trình thực hiện - Xem Quy trình nghiệp vụ.

### 3.3.1. Sơ đồ kiến trúc hệ thống (System architecture)

- Mô hình kiến trúc phân tách thành các tầng xử lý bất đồng bộ, đảm bảo tính hội tụ dữ liệu tại hệ thống lõi Delta MIS.
- ![Sơ đồ kiến trúc hệ thống thu thập hóa đơn đầu vào](images/SIM_Oct_11_2026.pdf-0015-00.png)
- Chữ trong sơ đồ (theo thứ tự đọc):
- - Cục thuế / Email — Đối tác xuất hóa đơn — Misa meInvoice — Hóa đơn đầu vào
- - API Banking — Nhận tiền trên tài khoản ngân hàng — Core Banking
- - Upload hóa đơn PDF thủ công — Các trường hợp ngoại lệ, bất thường
- - Delta API Gate — Misa API, bank webhook & PDF upload — Thanh toán hóa đơn trả hộ — Delta MIS
- - Stoarge & Application layer — JobID / Employee — Giao diện quản lý hóa đơn
- - AI01 — XML parser & OCR engine — Đối chiếu hóa đơn — Giao dịch ngân hàng — Integration & message queue

### 3.3.2. Sơ đồ luồng dữ liệu (Data flow)

- ![Sơ đồ luồng dữ liệu thu thập & định danh hóa đơn đầu vào](images/SIM_Oct_11_2026.pdf-0015-02.png)
- Chữ trong sơ đồ (theo thứ tự đọc):
- - Nhân viên / Đối tác — Misa / Ngân hàng — Delta API Gate — Trợ lý AI01 — Delta database
- - 1. Nhân viên quét QR / Thanh toán
- - 2. Biến động số dư (Mã nhân viên & JobID
- - 3. Cache giao dịch
- - 4. Đối tác xuất hóa đơn điện tử
- - 5. Thông tin hóa đơn (file XML, PDF)
- - 6. Đưa hóa đơn vào queue
- - 7. Quét & parsing => Bóc tách thông tin định danh.
- - 8. Đối chiếu chéo => Khớp hóa đơn với mã UNC.
- - 9. Kiểm tra hóa đơn trùng => Từ chối
- - 10. Gán mã nhân viên & JobID => Đưa vào danh mục hóa đơn chờ thanh toán

### 3.3.3.1. Định danh giao dịch qua luồng API Banking

- - Nhân viên thực hiện thanh toán chi phí/trả hộ bằng cách quét mã QR (tĩnh/động) hoặc chuyển khoản thông tin tài khoản đối tác.
- - Hệ thống Core Banking của ngân hàng đối tác bắn tín hiệu biến động số dư bằng cơ chế webhook về Delta API Gateway.
- - Delta API Gateway phân tích nội dung chuyển khoản và Yêu cầu thanh toán đã được phê duyệt để lấy thông tin định danh giao dịch bao gồm:
- - ✓ Mã nhân viên: Xác định từ tài khoản người dùng tạo Yêu cầu thanh toán.
- - ✓ Đối với luồng quét mã QR động, hệ thống sử dụng cơ chế mapping số tham chiếu FT nhận từ Webhook ngân hàng với dữ liệu Cache để truy vết ngược lại Mã nhân viên và Số JobID tương ứng.
- - ✓ Số JobID: Sử dụng cấu trúc Regex để trích xuất JobID nghiệp vụ trong nội dung Yêu cầu thanh toán.
- - ✓ Số tiền thực chi, Ngày giờ giao dịch, Mã số tài khoản đối tác.
- - Thông tin giao dịch quan luồng API bbanking được đưa vào bộ nhớ đệm (cache) của Trợ lý AI01 để chờ đối chiếu với hóa đơn.

### 3.3.3.2. Thu thập hóa đơn tự động qua Misa API Gateway

- - Misa meInvoice tự động quét và gom toàn bộ hóa đơn điện tử do đối tác xuất cho mã số thuế của Delta (từ Cục thuế) hoặc nhận qua hộp thư email forward.
- - Sử dụng cơ chế webhook hoặc scheduler pull định kỳ, Misa API Gateway đẩy toàn bộ gói dữ liệu chứa file XML gốc và bản thể hiện PDF của hóa đơn về Delta API Gateway.

### 3.3.3.3. Trợ lý AI01 thực hiện quét & đọc và trích xuất thông tin hóa đơn

- Trợ lý AI01 tiếp nhận tệp tin từ hàng đợi (message queue) và tiến hành xử lý bất đồng bộ:
- - XML Parsing _(Hóa đơn nhận qua luồng Misa API Gateway)_: Đọc trực tiếp thẻ cấu trúc tệp XML để trích xuất thông tin định danh pháp lý hóa đơn với độ chính xác 100%: _Mã số thuế người bán, Ký hiệu hóa đơn, Số hóa đơn, Ngày lập, Tổng tiền trước thuế, Tiền thuế, Tổng tiền thanh toán_.
- - PDF OCR Engine _(Hóa đơn nhận từ nhân viên nghiệp vụ upload thủ công)_: Thực hiện quét hình ảnh/văn bản của file PDF để bóc tách thông tin bổ sung tại mục "Ghi chú/Nội dung" nhằm tìm kiếm các từ khóa đặc biệt (nếu có).

### 3.3.3.4. Đối chiếu chéo (AI01 cross-matching) để mapping

- Trợ lý AI01 thực hiện thuật toán so khớp (matching) giữa dữ liệu trích xuất từ hóa đơn đầu vào (do nhân viên Delta upload & nhận từ Misa API gatewway) với dữ liệu giao dịch thu về từ luồng API Banking:
- - Điều kiện khớp cấu trúc (Khớp 1-1):
- - $$\text{Hóa đơn} \equiv \text{Giao dịch Banking} \iff \begin{cases} \text{Tổng tiền thanh toán (HĐ)} = \text{Số tiền thực chi (Bank)} \\ \text{Mã số thuế/Tên NCC (HĐ)} \approx \text{Thông tin tài khoản nhận (Bank)} \\ \text{Ngày lập (HĐ)} \in [\text{Ngày giao dịch (Bank)} \pm 3 \text{ ngày}] \end{cases}$$
- - Xử lý kết quả khớp:
- - ✓ Khi tìm thấy giao dịch Banking tương ứng, Trợ lý AI01 tự động kế thừa thông tin Mã nhân viên và Mã JobID từ giao dịch đó để định danh cho hóa đơn.
- - ✓ Hệ thống tự động hoàn thành Phân loại bước 2 (Chi phí trả hộ theo JobID) mà không cần nhân viên phải upload file hay chọn tay trên phần mềm.

### 3.3.3.5. Kiểm soát hóa đơn trùng & Gửi thông báo

- Sau khi đã định danh được hóa đơn, AI01 chuyển tiếp thông tin sang chức năng quản lý để thực hiện rà soát:
- - Hệ thống so sánh thông tin định danh pháp lý (_Mã số thuế người bán + Ký hiệu + Số hóa đơn_) với danh mục cơ sở dữ liệu hóa đơn đã tồn tại hoặc đang trong tiến trình chờ duyệt thanh toán.
- - ✓ Nếu TRÙNG LẶP: Delta MIS từ chối và đưa hóa đơn vào _Danh mục hóa đơn từ chối thanh toán_. Delta MIS kiểm tra trùng cho cả hai nguồn hóa đơn thu thập. Đối với nguồn upload thủ công, Delta MIS từ chối trực tiếp tại màn hình của AI01.
- - ✓ Nếu KHÔNG TRÙNG LẶP: Chuyển hóa đơn vào danh mục hóa đơn chờ thanh toán.
- - Trạng thái hóa đơn trong danh mục quản lý:
- - ✓ Chưa làm thanh toán: Delta MIS thực hiện thanh toán tự động thay nhân viên.
- - Nếu hóa đơn nhận được từ một thanh toán trên Quy trình nợ hóa đơn qua luồng API Banking: Thực hiện quy trình thanh toán trả hóa đơn để (1) đưa hóa đơn lên JobID nghiệp vụ và (2) ghi giảm dư nợ tạm ứng 2 của nhân viên nghiệp vụ thực hiện thanh toán nợ hóa đơn.
- - Nếu hóa đơn do nhân viên nghiệp vụ upload thủ công: Đưa vào danh mục hóa đơn chờ thanh toán trên mã nhân viên thực hiện việc upload thủ công.
- - ✓ Đã làm thanh toán: Khi nhân viên chuyển duyệt thanh toán hoặc Delta MIS làm thanh toán tự động, hóa đơn chuyển trạng thái đóng, ẩn khỏi danh sách sẵn sàng và khóa tính năng sử dụng lại để triệt tiêu hoàn toàn rủi ro chi trả nhiều lần.

### 3.3.4. Các trường hợp đặc biệt (Exceptional case)

- Trong trường hợp luồng API Banking không tìm thấy giao dịch phù hợp (Ví dụ đối tác xuất một hóa đơn gộp cho nhiều Ủy nhiệm chi của Delta hoặc nhân viên nghiệp vụ nhận nhiều hóa đơn cho một UNC), Delta MIS sẽ xử lý theo quy trình sau:
- 1. Chuyển các hóa đơn này sang danh mục “Hóa đơn vô chủ” để xử lý thủ công.
- 2. Trên danh mục “Hóa đơn vô chủ”, Delta MIS hiển thị thông tin định danh của hóa đơn kèm danh sách các giao dịch từ API Banking có số tiền tương đương hoặc phát sinh từ cùng một nhân viên trong khoảng thời gian gần nhất.
- 3. Các hóa đơn nằm trong danh mục “Hóa đơn vô chủ” chắc chắn là những hóa đơn trả hộ. Vì vậy, hóa đơn vô chủ sẽ được thanh toán theo Quy trình thanh toán trả hóa đơn với một bước duyệt bổ sung của Kế toán tổng hợp nhằm kiểm tra hai lần hóa đơn trước khi đưa vào JobID nghiệp vụ và ghi giảm Dư nợ tạm ứng 2 của người làm Yêu cầu thanh toán trả hóa đơn này.


## Mục bị sửa

### SOLUTIONS FOR INVOICE MANAGEMENT (SIM)

```diff
-> Thông tin trang: CÔNG TY CỔ PHẦN QUỐC TẾ DELTA · chân trang "SIM_Octpber 10, 2026 — Trang: N/19"
-![Logo Delta International](images/SIM_Oct_11_2026.pdf-0001-00.png)
+> Thông tin trang: CÔNG TY CỔ PHẦN QUỐC TẾ DELTA · chân trang "SIM_October 12, 2026 — Trang: N/16"
+![Logo Delta International](images/SIM_Oct_12_2026.pdf-0001-00.png)
-**Hà Nội, ngày 11 tháng 10 năm 2026**
+**Hà Nội, ngày 12 tháng 10 năm 2026**
```

### MỤC LỤC

```diff
-- **2.1. Quản lý hóa đơn đầu vào (AI01)**
-- **2.2. Tạo JobID nghiệp vụ (AI02)**
-- **2.3. Luồng thanh toán tự động qua API Banking** — _(số trang in trong mục lục: "Error! Bookmark not defined.")_
-- **2.4. Công tác chuẩn bị**
+- **2.1. Luồng thanh toán tự động qua API Banking**
+- **2.2. Tạo JobID nghiệp vụ (AI01)**
+- **2.3. Công tác chuẩn bị**
-- **3.3. Thu thập & định danh hóa đơn đầu vào và làm thanh toán tự động**
-- _3.3.1. Sơ đồ kiến trúc hệ thống (System architecture)_
-- _3.3.2. Sơ đồ luồng dữ liệu (Data flow)_
-- _3.3.3. Quy trình nghiệp vụ_
-- _3.3.4. Các trường hợp đặc biệt (Exceptional case)_
+- **3.3. Thu thập & định danh hóa đơn đầu vào và làm thanh toán tự động (IIP)**
+- _3.3.1. Nguyên lý vận hành_
+- _3.3.2. Sơ đồ kiến trúc hệ thống_
+- _3.3.3. Sơ đồ luồng dữ liệu_
+- _3.3.4. Quy trình nghiệp vụ & Logic xử lý chi tiết_
+- _3.3.5. Hóa đơn vô chủ_
```

### 2.1. Luồng thanh toán tự động qua API Banking

```diff
-Hiện tại, việc quản lý dòng tiền và đối soát công nợ tại Delta đang gặp các nút thắt lớn (1) Kế toán phải lập lệnh thanh toán chi phí trả hộ và chi phí nhà cung cấp bằng tay trên ngân hàng điện tử (2) Việc quản lý công nợ phải thu và phảu trả làm hoàn toàn bằng phương pháp thủ công, dễ gây sai sót và chậm trễ. Vì vậy, phân hệ API Banking được phát triển nhằm tích hợp trực tiếp luồng tiền từ các tài khoản ngân hàng (MB Bank, Vietcombank, TPBank) vào Hệ thống SIM, làm cơ sở dữ liệu thời gian thực để Trợ lý AI01 đối chiếu chéo, định danh hóa đơn và tự động hóa quy trình đóng/mở công nợ.
+Hiện tại, việc quản lý dòng tiền và đối soát công nợ tại Delta đang gặp các nút thắt lớn (1) Kế toán phải lập lệnh thanh toán chi phí trả hộ và chi phí nhà cung cấp bằng tay trên ngân hàng điện tử (2) Việc quản lý công nợ phải thu và phải trả làm hoàn toàn bằng phương pháp thủ công, dễ gây sai sót và chậm trễ. Vì vậy, phân hệ API Banking được phát triển nhằm tích hợp trực tiếp luồng tiền từ các tài khoản ngân hàng (MB Bank, Vietcombank, TPBank) vào Hệ thống SIM, làm cơ sở dữ liệu thời gian thực để Trợ lý AI01 đối chiếu chéo, định danh hóa đơn và tự động hóa quy trình đóng/mở công nợ.
```

### 2.1.2. Luồng số hóa Sổ phụ ngân hàng để quản lý công nợ

```diff
-![Sơ đồ luồng số hóa Sổ phụ ngân hàng](images/SIM_Oct_11_2026.pdf-0004-01.png)
+![Sơ đồ luồng số hóa Sổ phụ ngân hàng](images/SIM_Oct_12_2026.pdf-0004-02.png)
-- Ngân hàng đối tác — Cung cấp biến động số dư qua webhook — Delta API Gateway
-- Bộ nhớ đệm Cache AI01 — Xác định mã DK05, số hóa đơn và Bảng kê nợ phải thu
+- Ngân hàng đối tác — Cung cấp biến động số dư qua webhook — Delta API Gate
+- Staging Database — Xác định mã DK05, số hóa đơn và Bảng kê nợ phải thu
```

### 2.1.3. Quy trình thanh toán qua API Banking

```diff
-- Bước 1 (Yêu cầu thanh toán): Nhân viên lập Yêu cầu thanh toán trên Delta MIS từ JobID nghiệp vụ hoặc Lệnh vận tải. Bắt buộc phải chọn tài khoản đích từ danh mục đối tác đã chuẩn hóa hoặc quét mã QR động hoặc tĩnh để loại bỏ lỗi nhập liệu nhầm.
-- Bước 2 (Ghi chép đối ứng): Delta MIS tự động trích xuất dữ liệu, kiểm tra tính hợp lệ của mã QR (đảm bảo thời gian hiệu lực ≥ 3 phút) và tự động tạo nội dung chuyển tiền chứa: Mã nhân viên - Số JobID - Số vận đơn/Booking - Tên chi phí - Tên khách hàng.
-- ✓ <mark>Nếu sử dụng mã QR động thì không được chèn vào nội dung chuyển tiền trên UNC mà phải mapping số tham chiếu FT của UNC với Yêu cầu thanh toán.</mark>
-- Bước 3 (Định tuyến & Lập UNC): Hệ thống tự động xác định pháp nhân chi trả (Delta HN, Delta HCM, Delta Vận tải) để chọn tài khoản nguồn tương ứng và đẩy lệnh chi qua Transfer API sang ngân hàng.
-- Bước 4 (Phê duyệt tối cao): Chủ tài khoản hoặc Đồng chủ tài khoản kiểm tra thông tin và thực hiện duyệt OTP trên môi trường App/Web doanh nghiệp của Ngân hàng (MBBank Biz, VCB DigiBiz, TPBank Biz).
-- Bước 5 (Đồng bộ & Lưu vết): Sau khi ngân hàng trừ tiền thành công, Webhook của ngân hàng bắn dữ liệu về Delta MIS. Hệ thống lưu vết mã giao dịch tham chiếu (Mã FT...) vào cache để phục vụ Trợ lý AI01 đối chiếu với hóa đơn đầu vào sẽ thu thập về sau.
+- **Bước 1 - Yêu cầu thanh toán:** Nhân viên lập Yêu cầu thanh toán trên Delta MIS từ JobID nghiệp vụ hoặc Lệnh vận tải. Bắt buộc phải chọn tài khoản đích từ danh mục đối tác đã chuẩn hóa hoặc quét mã QR động hoặc tĩnh để loại bỏ lỗi nhập liệu nhầm.
+- **Bước 2 - Ghi chép đối ứng:** Delta MIS tự động trích xuất dữ liệu, kiểm tra tính hợp lệ của mã QR (đảm bảo thời gian hiệu lực ≥ 3 phút) và tự động tạo nội dung chuyển tiền chứa: Mã nhân viên - Số JobID - Số vận đơn/Booking - Tên chi phí - Tên khách hàng.
+- ✓ Nếu sử dụng mã QR động thì không được chèn vào nội dung chuyển tiền trên UNC mà phải mapping số tham chiếu FT của UNC với Yêu cầu thanh toán.
+- **Bước 3 - Định tuyến & Lập UNC:** Hệ thống tự động xác định pháp nhân chi trả (Delta HN, Delta HCM, Delta Vận tải) để chọn tài khoản nguồn tương ứng và đẩy lệnh chi qua Transfer API sang ngân hàng.
+- **Bước 4 - Phê duyệt tối cao:** Chủ tài khoản hoặc Đồng chủ tài khoản kiểm tra thông tin và thực hiện duyệt OTP trên môi trường App/Web doanh nghiệp của Ngân hàng (MBBank Biz, VCB DigiBiz, TPBank Biz).
+- **Bước 5 - Đồng bộ & Lưu vết:** Sau khi ngân hàng trừ tiền thành công, Webhook của ngân hàng bắn dữ liệu về Delta MIS. Hệ thống lưu vết mã giao dịch tham chiếu trên UNC (Mã FT) vào Cơ sở dữ liệu tạm thời (Staging Database/Table) để phục vụ Phân hệ IIP đối chiếu với hóa đơn đầu vào sẽ thu thập về sau.
```

### 3.3.3. Sơ đồ luồng dữ liệu _(trước: 2.2.1. Sơ đồ luồng dữ liệu)_

```diff
-![Sơ đồ luồng dữ liệu AI01](images/SIM_Oct_11_2026.pdf-0005-10.png)
-Chữ trong sơ đồ (theo thứ tự đọc):
-- Misa API Gate — Nhận file XML & Parsing
-- End-users: Nhân viên & Lái xe — Upload thủ công PDF
-- Delta API Gate — Nhận file ảnh & PDF — Google Document AI
-- AI01 — Kiểm tra trùng lặp — Danh mục hóa đơn từ chối
-- API Banking — Thông tin UNC — Đối chiếu chéo 1-1
-- Khớp mã => Gán JobID & user — Danh mục hóa đơn chờ thanh toán
-- Lệnh mã => Hóa đơn vô chủ — Danh mục hóa đơn vô chủ
+- **Bước 1 - Ghi nhận chi phí**
+- ✓ Nhân viên quét QR/chuyển khoản từ tài khoản công ty. Core Banking bắn webhook biến động số dư về Delta API Gateway.
+- ✓ Nhân viên dùng tiền mặt/thẻ cá nhân trả trước tại hiện trường. Không có dữ liệu qua luồng API Banking.
+- **Bước 2 - Thu thập hóa đơn:** Hóa đơn được gom tự động từ Misa meInvoice hoặc do nhân viên upload thủ công lên hệ thống.
+- **Bước 3 - Đưa vào hàng đợi:** Toàn bộ dữ liệu được đẩy vào Message Queue của Phân hệ IIP.
+- **Bước 4 - Xử lý tại Phân hệ IIP:** Hệ thống thực hiện Parsing/OCR => Đối chiếu chéo (Cross-matching) => Kiểm tra trùng lặp => Phân phối luồng thanh toán phù hợp.
```

### 2.2.3. Quy trình nghiệp vụ _(trước: 3.3.3. Quy trình nghiệp vụ)_

```diff
+- Bước 1 (Tiền xử lý): Nhân viên CS/Điều vận gán trước các thông tin bối cảnh kinh doanh bắt buộc gồm: Mã khách hàng (DK05), Số báo giá hoặc hợp đồng để kiểm soát dòng doanh thu dịch vụ, chọn loại JobID và thực hiện upload bộ chứng từ định danh lên hệ thống.
+- Bước 2 (Phân luồng gọi dịch vụ): Hệ thống kiểm tra dung lượng và số trang tệp tin để tự động điều phối lệnh gọi sang Google Document AI:
+- ✓ _Tài liệu nhỏ (1-3 trang, < 5MB):_ Chạy chế độ đồng bộ (Interactive Mode), nhân viên chờ kết quả hiển thị trực tiếp trên màn hình, cam kết thời gian phản hồi chỉ số P95 ≤ 10 giây.
+- ✓ _Tài liệu lớn (> 3 trang hoặc > 5MB):_ Chạy chế độ bất đồng bộ (Async Mode), hệ thống trả ngay trạng thái tiếp nhận queued trong ≤ 1 giây, tiến trình chạy nền hoàn tất xử lý chỉ số P95 ≤ 60 giây.
+- Bước 3 (Kiểm soát trùng lặp): Trước khi hiển thị dữ liệu ra giao diện, hệ thống thực thi thuật toán kiểm tra tính bất biến (Idempotency) dựa trên quy tắc khóa: jobType + dk05 + fileHash để loại bỏ hoàn toàn các yêu cầu xử lý rác hoặc click lặp từ người dùng.
+- Bước 4 (Nhân viên xác thực & Duyệt chính thức): Dữ liệu hợp lệ được đổ vào bản ghi JobID Draft (Nháp).
+- ✓ Áp dụng nghiêm ngặt nguyên tắc Fail-safe (An toàn hệ thống): AI không tự ý suy đoán bừa bãi. Các trường dữ liệu có độ tin cậy thấp hoặc không thể bóc tách sẽ hiển thị giá trị null (để trống).
+- ✓ Nhân viên CS/Điều vận thực hiện rà soát trực quan, bổ sung các trường thông tin còn thiếu, hiệu chỉnh dữ liệu sai lệch (nếu có) và nhấn nút xác nhận duyệt để phát hành JobID chính thức.
+- ✓ Hệ thống tự động ghi nhận dữ liệu chênh lệch (diff) giữa giá trị AI đề xuất ban đầu và giá trị con người sửa đổi, lưu trữ độc lập để phục vụ công tác tái huấn luyện offline nhằm tối ưu hóa bộ luật Regex.
```

### Bước 1: Tiếp nhận và Trích xuất thông tin hóa đơn (Parsing & OCR Engine) _(trước: Bước 1: Tiếp nhận và Trích xuất thông tin hóa đơn (Parsing & Google API))_

```diff
-Khi tệp tin hóa đơn đi vào hàng đợi (Message Queue), Trợ lý AI01 tiến hành xử lý bất đồng bộ:
-- Đối với hóa đơn XML (Nguồn Misa Gateway): Hệ thống chạy bộ phân tích cú pháp XML Parser truyền thống của Delta để đọc trực tiếp các thẻ cấu trúc dữ liệu, đảm bảo chính xác tuyệt đối 100%. Hoàn toàn không gọi sang dịch vụ của Google để tiết kiệm chi phí API.
-- Đối với hóa đơn PDF/Ảnh (Nguồn upload thủ công): Delta MIS đóng gói tệp tin và thực hiện một lệnh gọi API bảo mật (HTTPS REST API) sang Google Document AI.
-- ✓ Dịch vụ của Google thực hiện quét bề mặt ảnh, số hóa và trả về chuỗi văn bản (Text) có cấu trúc dạng JSON.
-- ✓ Hệ thống Delta tiếp nhận kết quả JSON từ Google, sử dụng code truyền thống (Regex/Query) để bóc tách thông tin tại mục _"Ghi chú/Nội dung"_, số hóa tiền và thông tin người bán.
+- Đối với hóa đơn XML (nhận tự động từ Misa meInvoice): Hệ thống sử dụng bộ phân tích XML Parser truyền thống để đọc trực tiếp các thẻ cấu trúc dữ liệu. Độ chính xác đạt 100% và không gọi sang dịch vụ của Google, giúp tiết kiệm chi phí API. Các trường bóc tách: _Mã số thuế người bán, Ký hiệu hóa đơn, Số hóa đơn, Ngày lập, Tổng tiền trước thuế, Tiền thuế, Tổng tiền thanh toán_.
+- Đối với hóa đơn PDF/Ảnh (nguồn upload thủ công từ nhân viên nghiệp vụ & lái xe): Delta MIS đóng gói tệp tin và thực hiện lệnh gọi HTTPS REST API sang Google Document AI / Cloud Vision API. Dịch vụ của Google số hóa văn bản thô dưới dạng JSON. Hệ thống Delta sử dụng code truyền thống (Regex/Query) để bóc tách thông tin tại mục _"Ghi chú/Nội dung"_, số hóa số tiền và thông tin người bán.
```

### Bước 2: Đối chiếu chéo tự động (Rule-based Cross-Matching) để định danh _(trước: Bước 2: Đối chiếu chéo tự động (AI01 Cross-Matching) để định danh)_

```diff
-Ngay sau khi dữ liệu hóa đơn được cấu trúc hóa, hệ thống tiến hành so khớp với dữ liệu giao dịch thu về từ luồng API Banking (đang lưu trữ tại bộ nhớ đệm cache của AI01).
-- Điều kiện khớp cấu trúc (Khớp 1-1):
-- $$\text{Hóa đơn} \equiv \text{Giao dịch Banking} \iff \begin{cases} \text{Tổng tiền thanh toán (HĐ)} = \text{Số tiền thực chi (Bank)} \\ \text{Mã số thuế/Tên NCC (HĐ)} \approx \text{Thông tin tài khoản nhận (Bank)} \\ \text{Ngày lập (HĐ)} \in [\text{Ngày giao dịch (Bank)} \pm 3 \text{ ngày}] \end{cases}$$
-- Xử lý kết quả khớp: Hệ thống tự động kế thừa Mã nhân viên và Mã JobID từ giao dịch ngân hàng để định danh cho hóa đơn. Hoàn thành tự động Phân loại bước 2 (Chi phí trả hộ theo JobID) mà không cần con người can thiệp.
+Ngay sau khi dữ liệu hóa đơn được cấu trúc hóa, hệ thống tiến hành so khớp với dữ liệu giao dịch thu về từ luồng API Banking đang lưu trữ tại cơ sở dữ liệu tạm thời (Staging Database/Table) để phục vụ Phân hệ IIP đối chiếu.
+**Điều kiện khớp cấu trúc (Khớp 1-1):**
+Hệ thống sẽ tự động xác định tờ hóa đơn và giao dịch ngân hàng là trùng khớp tuyệt đối (khớp 1-1) khi và chỉ khi thỏa mãn đồng thời cả 3 tiêu chí sau:
+- **Khớp số tiền:** Tổng số tiền trên hóa đơn phải bằng chính xác số tiền thực tế đã chi qua ngân hàng.
+- **Khớp đối tác:** Mã số thuế hoặc Tên nhà cung cấp trên hóa đơn phải trùng (hoặc gần đúng) với thông tin tài khoản nhận tiền của ngân hàng.
+- **Khớp thời gian:** Ngày lập hóa đơn và Ngày giao dịch ngân hàng không được lệch nhau quá 3 ngày.
+Trong quá trình BA, phát triển giải pháp để giải quyết các trường hợp (1) 1-N trong đó một UNC được đối tác tách thành nhiều hóa đơn và (2) N-1 trong đó nhiều UNC được đối tác gộp thành một hóa đơn, dựa trên các quy tắc sau:
+- **Quy tắc xử lý luồng gộp N-1 (Nhiều giao dịch ngân hàng - 1 Hóa đơn):** Hệ thống tại màn hình đối soát cho phép Kế toán viên tick chọn thủ công nhiều giao dịch (Mã FT) đang ở trạng thái "Chờ đối soát" trên Staging Table để liên kết gộp với 01 hóa đơn đầu vào. Điều kiện khớp: Σ Số tiền của N giao dịch = Tổng tiền thanh toán trên hóa đơn.
+- **Quy tắc xử lý luồng tách 1-N (1 Giao dịch ngân hàng - Nhiều Hóa đơn):** Khi một giao dịch ngân hàng có giá trị lớn hơn hóa đơn đầu vào thu thập về, hệ thống cho phép khớp một phần và chuyển trạng thái giao dịch ngân hàng đó thành "Khớp một phần (Số tiền còn lại: [Số tiền])". Giao dịch ngân hàng này sẽ tiếp tục nằm trong danh sách đối soát cho đến khi tổng giá trị các hóa đơn đầu vào liên kết bằng chính xác số tiền thực chi trên lệnh gộp.
```

### Bước 3: Kiểm soát trùng lặp lịch sử

```diff
-Ngay khi nhận được dữ liệu cấu trúc của hóa đơn từ bộ phân tích XML Parser hoặc nhận từ Google API, hệ thống sử dụng thông tin định danh hóa đơn gồm: Mã số thuế người bán + Ký hiệu + Số hóa đơn để truy vấn đối chiếu với toàn bộ cơ sở dữ liệu lịch sử (Database):
-- Trường hợp TRÙNG LẶP: Nếu các thông tin định danh hóa đơn này đã tồn tại trong cơ sở dữ liệu của các kỳ trước hoặc các giao dịch đã hoàn tất đóng:
-- ✓ Hệ thống lập tức từ chối và tự động đẩy hóa đơn này vào _Danh mục hóa đơn từ chối thanh toán_.
-- ✓ Nếu là nguồn upload thủ công, hệ thống hiển thị cảnh báo lỗi trực tiếp trên màn hình của người dùng.
-- Trường hợp KHÔNG TRÙNG LẶP: Hóa đơn được xác nhận là hợp lệ về mặt lịch sử và được chuyển tiếp sang Bước 4 để điều phối trạng thái vận hành thời gian thực.
+Hệ thống sử dụng bộ ba thông tin định danh pháp lý: **Mã số thuế người bán + Ký hiệu + Số hóa đơn** để truy vấn đối chiếu với toàn bộ cơ sở dữ liệu lịch sử (Database).
+- Trường hợp TRÙNG LẶP: Nếu hóa đơn đã tồn tại trong lịch sử hoặc đang trong tiến trình chờ duyệt thanh toán khác, hệ thống lập tức từ chối và đẩy vào _Danh mục hóa đơn từ chối thanh toán_. Nếu là nguồn upload thủ công, hệ thống hiển thị cảnh báo lỗi trực tiếp trên màn hình của người dùng.
+- Trường hợp KHÔNG TRÙNG LẶP: Hóa đơn hợp lệ về mặt lịch sử, chuyển tiếp sang Bước 4.
```

### Bước 4: Điều phối trạng thái danh mục và Xử lý thanh toán phân nhánh _(trước: Bước 4: Điều phối trạng thái danh mục và Kiểm soát va chạm thanh toán)_

```diff
-Hệ thống sử dụng các quy tắc lập trình truyền thống (Rule-based Core Logic) để giám sát và điều khiển trạng thái của hóa đơn theo thời gian thực, ngăn chặn tuyệt đối tình trạng một hóa đơn bị sử dụng nhiều lần tại cùng một thời điểm:
-- Trạng thái Chưa làm thanh toán.
-- ✓ Hệ thống đưa hóa đơn vào _Danh mục hóa đơn chờ thanh toán_.
-- ✓ Đối với Quy trình thanh toán nợ hóa đơn: Hệ thống tự động đưa hóa đơn lên JobID nghiệp vụ tương ứng và tự động ghi giảm _"Dư nợ tạm ứng 2"_ của nhân viên.
-- Trạng thái Đã / Đang làm thanh toán
-Ngay khi hóa đơn được gán vào một Yêu cầu thanh toán đang nằm trong luồng xử lý (bao gồm: _Đang chờ duyệt nội bộ, Đã duyệt nội bộ hoặc Đã thanh toán thành công_), hệ thống sẽ:
-- ✓ Lập tức chuyển hóa đơn này vào _Danh mục hóa đơn từ chối thanh toán_.
-- ✓ Nếu xuất hiện một luồng dữ liệu khác cố tình sử dụng lại tờ hóa đơn này tại thời điểm đó (Ví dụ: một nhân viên khác upload thủ công trùng tệp PDF lên), hệ thống sẽ kích hoạt lệnh chặn, đẩy luồng trùng lặp này vào _Danh mục hóa đơn từ chối thanh toán_.
-- ✓ Tự động gửi thông báo cảnh báo trực tiếp đến tài khoản của người đã upload thủ công để thông báo về việc hóa đơn đã bị trùng hoặc đang trong tiến trình xử lý thanh toán khác.
-- **Đồng bộ ngược kế toán.**
-Kích hoạt Background Job gọi API sang MISA AMIS để tự động lập chứng từ chi tiền, khớp nối hóa đơn đầu vào này với chứng từ và chuyển trạng thái công nợ thành "Đã thanh toán".
+Hệ thống sử dụng các quy tắc lập trình để giám sát và tự động xử lý thanh toán đóng công nợ theo phương thức chi ban đầu của nhân viên. Chi tiết như bảng sau:
+| Phân loại luồng chi | Logic xử lý nghiệp vụ | Hành động kế toán trên Delta MIS & MISA AMIS |
+|---|---|---|
+| **Trường hợp 1:** Nhân viên thanh toán qua luồng API Banking | - Hệ thống so khớp thành công hóa đơn với giao dịch ngân hàng theo điều kiện tại Bước 2.<br>- Tự động gán Mã nhân viên và Số JobID nghiệp vụ cho hóa đơn từ giao dịch gốc. | **Tự động làm thanh toán giảm nợ:**<br>- Hệ thống tự động chuyển hóa đơn sang trạng thái đóng, khóa tính năng sử dụng lại và đưa lên JobID.<br>- Delta MIS gọi Background Job API sang MISA AMIS tự động **ghi giảm "Dư nợ tạm ứng 2"** của nhân viên đã thực hiện giao dịch chi tiền trước đó. |
+| **Trường hợp 2:** Nhân viên KHÔNG thanh toán qua luồng API Banking _(Chi tiền mặt/thẻ cá nhân)_ | Hệ thống không tìm thấy giao dịch đối ứng phù hợp trên cổng API Banking.<br>Hệ thống tự động đưa hóa đơn này vào danh mục **"Hóa đơn vô chủ"** kèm mã nhân viên thực hiện upload thủ công để cách ly và xử lý an toàn. | **Tự động làm thanh toán hoàn trả tiền:**<br>- Tại màn hình "Hóa đơn vô chủ", Cán bộ quản lý duyệt bước một và Kế toán tổng hợp duyệt bước 2 để kiểm tra thông tin định danh của hóa đơn 2 lần.<br>- Ngay khi kế toán bấm duyệt, Delta MIS gọi API sang MISA AMIS **tự động tạo Phiếu chi** và gửi đến Quy trình 5.8 thuộc bộ quy trình Quản lý quỹ & thanh toán để **hoàn trả** số tiền tương ứng trị giá hóa đơn trực tiếp vào tài khoản của nhân viên upload hóa đơn. |
```

### 2.2. Tạo JobID nghiệp vụ (AI01) _(trước: 2.3. Tạo JobID nghiệp vụ (AI02))_

```diff
-Giải pháp đọc chứng từ định danh của lô hàng để lấy các thông tin định danh và tạo JobID cho lô hàng trên phần mềm Delta gọi tắt la Trợ lý AI02. Giải pháp này có mục tiêu giảm công việc nhập liệu thủ công và tối ưu hóa chi phí vận hành, Trợ lý AI02 sử dụng hạ tầng Google Document AI (bộ xử lý Document OCR) phối hợp với bộ lọc lập trình nội bộ. Mô hình vận hành quy định rõ: AI02 chỉ đóng vai trò trích xuất và khởi tạo bản ghi JobID Draft (Nháp), nhân viên nghiệp vụ (CS/Điều vận) bắt buộc phải thực hiện bước kiểm tra, xác thực nội dung và chủ động nhấn nút duyệt để phát hành JobID chính thức.
+Giải pháp đọc chứng từ định danh của lô hàng để lấy các thông tin định danh và tạo JobID cho lô hàng trên phần mềm Delta gọi tắt là Trợ lý AI01. Giải pháp này có mục tiêu giảm công việc nhập liệu thủ công và tối ưu hóa chi phí vận hành, Trợ lý AI01 sử dụng hạ tầng Google Document AI (bộ xử lý Document OCR) phối hợp với bộ lọc lập trình nội bộ. Mô hình vận hành quy định rõ: AI01 chỉ đóng vai trò trích xuất và khởi tạo bản ghi JobID Draft (Nháp), nhân viên nghiệp vụ (CS/Điều vận) bắt buộc phải thực hiện bước kiểm tra, xác thực nội dung và chủ động nhấn nút duyệt để phát hành JobID chính thức.
```

### 2.2.1. Kiến trúc tích hợp Google Document AI _(trước: 2.3.1. Kiến trúc tích hợp Google Document AI)_

```diff
-![Kiến trúc tích hợp Google Document AI cho AI02](images/SIM_Oct_11_2026.pdf-0007-12.png)
+![Kiến trúc tích hợp Google Document AI cho AI01](images/SIM_Oct_12_2026.pdf-0005-08.png)
-- End-users: CS / Điều vận — Tải chứng từ định danh — Chọn DK05, Hợp đồng / Báo giá & Mã JobID
-- Hàng đợi xử lý Async — AI02 — Delta API Gate
-- Delta API Gate — HTTPS Rest API / mTLS — Google Document AI — Trả chuỗi Json văn bản
-- Bản ghi JobID nháp — Nhân viên CS / Điều vận kiểm tra, xác thực trên Delta MIS
-- Tạo JobID thủ công — Nhân viên CS / Điều vận xác nhận trên Delta MIS — Delta MIS — End-users: CS / Điều vận
+- End-users: CS / Điều vận — Tải chứng từ định danh, Chọn DK05, Hợp đồng / Báo giá & Mã JobID — AI01
+- AI01 — Hàng đợi xử lý Async — Delta API Gate — HTTPS Rest API / mTLS, Trả chuỗi Json văn bản — Google Document AI
+- AI01 — Bản ghi JobID nháp, Nhân viên CS / Điều vận kiểm tra, xác thực trên Delta MIS — Delta MIS
+- End-users: CS / Điều vận — Tạo JobID thủ công, Nhân viên CS / Điều vận xác nhận trên Delta MIS — Delta MIS
```

### 2.2.2. Quy trình xử lý kỹ thuật qua API _(trước: 2.3.2. Quy trình xử lý kỹ thuật qua API)_

```diff
```

### 2.2.4. Luồng tạo JobID thủ công _(trước: 2.3.4. Luồng tạo JobID thủ công)_

```diff
```

### 2.3. Công tác chuẩn bị _(trước: 2.4. Công tác chuẩn bị)_

```diff
```

### 2.3.1. Các công việc cần chuẩn bị _(trước: 2.4.1. Các công việc cần chuẩn bị)_

```diff
-Để chuẩn bị cho đối tác outsourcing tích hợp Trợ lý AI01 và AI02, cần thực hiện các bước sau:
+Để chuẩn bị cho đối tác outsourcing tích hợp Trợ lý AI01, cần thực hiện các bước sau:
-4. Tối ưu hóa & Quản trị chi phí: Thiết lập hạn mức gọi API (Quota limits) theo ngày cho Trợ lý AI01 và AI02 nhằm kiểm soát chi phí trả theo lượng sử dụng (Pay-as-you-go) của Google, tránh rủi ro bùng nổ chi phí khi nhân viên upload tệp tin rác hoặc tệp trùng lặp.
+4. Tối ưu hóa & Quản trị chi phí: Thiết lập hạn mức gọi API (Quota limits) theo ngày cho Trợ lý AI01 nhằm kiểm soát chi phí trả theo lượng sử dụng (Pay-as-you-go) của Google, tránh rủi ro bùng nổ chi phí khi nhân viên upload tệp tin rác hoặc tệp trùng lặp.
```

### 3.3.2. Sơ đồ kiến trúc hệ thống _(trước: 3.1.1. Sơ đồ kiến trúc hệ thống)_

```diff
-![Sơ đồ kiến trúc hệ thống thanh toán bằng mã QR](images/SIM_Oct_11_2026.pdf-0010-00.png)
+![Sơ đồ kiến trúc hệ thống Phân hệ IIP](images/SIM_Oct_12_2026.pdf-0012-08.png)
-- End-users: Nhân viên nghiệp vụ — App / Web — Tạo Yêu cầu thanh toán rồi quét mã QR động hoặc nhập thông tin tài khoản của đối tác
-- Delta MIS — Phê duyệt yêu cầu thanh toán nội bộ — Kiểm tra JobID, xác định & mapping tài khoản, hạch toán & đối soát tự động
-- Ngân hàng số: MBBank Biz, VCB DigiBiz & TPBank Biz — Duyệt OTP — Xác thực-Trừ tiền
-- Delta API gate — Khởi tạo giao dịch / Truy vấn trạng thái / Webhook nhận Ủy nhiệm chi — Chữ ký số / Bảo mật — API Gateway MB, VCB & TPBank — Tài khoản ngân hàng của Delta
-- Ứng dụng giải mã QR ngoại vi — Phân tích ảnh & trả về text theo cấu trúc
+- Cục thuế / Email đối tác — Misa meInvoice gateway (Hóa đơn XML/PDF) — Delta API Gate, Message queue
+- API Banking Webhook — Delta API Gate, Message queue
+- Nhân viên / Lái xe, Giao diện App/Web — Upload ảnh & PDF thủ công qua App/Web — Delta API Gate, Message queue
+- Delta API Gate — Phân hệ IIP — XML parser & Google OCR engine
+- Phân hệ IIP — Delta MIS - Storage & Application layer
+- Delta MIS — Thanh toán qua API Banking — **Ghi giảm** Dư nợ tạm ứng 2 — Misa AMIS
+- Delta MIS — Không thanh toán qua API Banking — **Tạo Phiếu chi** Thanh toán tiền — Misa AMIS
```

### Bước 3: Phê duyệt Yêu cầu thanh toán

```diff
-- ✓ Nếu thời gian hiệu lực còn lại của mã QR ngắn hơn 3 phút thì Delta MIS chuyển trả Yêu cầu thanh toán lại Bước 1 cho nhân viên nghiệp vụ hoặc lái xe kèm yêu cầu tạo mã QR động mới để thực hiện thanh toán lại.
-- ✓ Nếu thời gian hiệu lực của mã QR bằng hoặc dài hơn 3 phút thì Delta MIS chuyển Yêu cầu thanh toán cho cán bộ quản lý phê duyệt Yêu cầu thanh toán theo phân quyền.
-- Phê duyệt: Delta MIS kích hoạt luồng xử lý dữ liệu tiếp theo ở Bước 4.
-- Từ chối: Chuyển trả Yêu cầu thanh toán lại cho nhân viên nghiệp vụ ở Bước 1.
+- ✓ Nếu thời gian hiệu lực còn lại của mã QR ngắn hơn 3 phút, Delta MIS sẽ chặn và chuyển trả Yêu cầu thanh toán lại Bước 1 để nhân viên nghiệp vụ hoặc lái xe chủ động tạo mã QR động mới nhằm đảm bảo an toàn cho luồng API Banking.
+- ✓ Nếu thời gian hiệu lực của mã QR từ 3 phút trở lên (đủ thời gian tối thiểu để hệ thống trích xuất thông tin và thực hiện thanh toán qua API Banking), Delta MIS chuyển Yêu cầu thanh toán cho cán bộ quản lý phê duyệt theo phân quyền.
```

### Mã QR động hết hạn bị động

```diff
-- Bước 2: Liên lạc với đối tác, cung cấp Ủy nhiệm chi của khoản thanh toán và yêu cầu thực hiện hạch toán thủ công để tiếp tục giải quyết công việc. Thực hiện việc này theo quy trình hướng dẫn của từng đối tác.
+- Bước 2: Liên lạc với đối tác tạo mã QR động (thường là cảng, bãi, kho hàng), cung cấp Ủy nhiệm chi của khoản thanh toán và yêu cầu thực hiện hạch toán thủ công để tiếp tục giải quyết công việc. Thực hiện việc này theo quy trình hướng dẫn của từng đối tác.
```

### 3.2. Phát hành và điều chỉnh hóa đơn tự động (Misa meInvoice)

```diff
-Trong quá trình phát triển qy trình nghiệp vụ để xây dựng Module Nghiệp vụ, Delta cần phát triển một giải pháp phát hành và điều chỉnh hóa đơn điện tử đơn giản để tích hợp vào Quy trình 5.2 (Quy trình cung cấp dịch vụ tổng quát). Tài liệu này (1) trình bày các vấn đề liên quan đến việc phát hành hóa đơn điện từ mới và (2) điều chỉnh hóa đơn điện tử đã phát hành và tìm giải pháp thực hiện hai công việc này để tích hợp vào Quy trình 5.2.
+Trong quá trình phát triển quy trình nghiệp vụ để xây dựng Module Nghiệp vụ, Delta cần phát triển một giải pháp phát hành và điều chỉnh hóa đơn điện tử đơn giản để tích hợp vào Quy trình 5.2 (Quy trình cung cấp dịch vụ tổng quát). Tài liệu này (1) trình bày các vấn đề liên quan đến việc phát hành hóa đơn điện tử mới và (2) điều chỉnh hóa đơn điện tử đã phát hành và tìm giải pháp thực hiện hai công việc này để tích hợp vào Quy trình 5.2.
```

### 3.2.1.3. Quy trình phù hợp với Delta

```diff
-Giải pháp phát hành và điều chỉnh hóa đơn tự động để tích hợp vào quy trình nghiệp vụ của Delta là kết nối trực tiếp qua cổng Open API của MISA meInvoice trong đó Delta MIS đóng vai trò điều phối (cung cấp dữ liệu, duyệt phát hành và nhận hóa đơn với mã của cơ quan thuế), phần mềm kế toán MISA đóng vai trò lưu trữ hóa đơn và dịch vụ MISA meInvoice đóng vai trò là cổng phát hành hóa đơn điện tử trực tiếp với Cục thuế.
+Giải pháp phát hành và điều chỉnh hóa đơn tự động để tích hợp vào quy trình nghiệp vụ của Delta là kết nối trực tiếp qua cổng Open API của MISA meInvoice trong đó Delta MIS đóng vai trò điều phối (cung cấp dữ liệu, duyệt phát hành và nhận hóa đơn với mã của cơ quan thuế), phần mềm kế toán MISA đóng vai trò lưu trữ hóa đơn và dịch vụ [MISA meInvoice](https://www.meinvoice.vn/) đóng vai trò là cổng phát hành hóa đơn điện tử trực tiếp với Cục thuế.
```

### 3.2.2. Sơ đồ kiến trúc luồng dữ liệu (Data Flow)

```diff
-Sơ đò kiến trúc mô hình phát hành và điều chỉnh hóa đơn tự động, kết nối giữa Delta MIS, MISA meInvoice và MISA AMIS, sử dụng giải pháp chữ ký số từ xa MISA eSign (Gói Doanh nghiệp kết nối API) để đạt mức độ tự động hóa cao nhất (100% không con người can thiệp).
-![Sơ đồ luồng dữ liệu phát hành/điều chỉnh hóa đơn qua MISA meInvoice](images/SIM_Oct_11_2026.pdf-0013-15.png)
+Sơ đồ kiến trúc mô hình phát hành và điều chỉnh hóa đơn tự động, kết nối giữa Delta MIS, MISA meInvoice và MISA AMIS, sử dụng giải pháp chữ ký số từ xa MISA eSign (Gói Doanh nghiệp kết nối API) để đạt mức độ tự động hóa cao nhất (100% không con người can thiệp).
+![Sơ đồ luồng dữ liệu phát hành/điều chỉnh hóa đơn qua MISA meInvoice](images/SIM_Oct_12_2026.pdf-0011-02.png)
-- Misa meInvoice — eSign & Cấp mã hóa đơn — Cục thuế — Trả kết quả (mã thuế, pdf, xml)
+- Misa meInvoice — eSign & Cấp mã hóa đơn, Trả kết quả (mã thuế, pdf, xml) — Cục thuế
```

### Thay thế / Điều chỉnh hóa đơn đã phát hành

```diff
-1. Khởi tạo yêu cầu. Nhân viên khởi tạo yêu cầu từ hóa đơn bị sai và chọn “Điều chỉnh” hoặc “Thay thế”, nhập lý do và chọn Bảng kê doanh thu dịch vụ hoặc Doanh thu trả hộ mới. Hệ thống tự động thu thập dữ liệu và gọi API tạo hóa đơn của MISA meInvoice.
+1. Khởi tạo yêu cầu. Nhân viên khởi tạo yêu cầu từ hóa đơn bị sai và chọn "Điều chỉnh" hoặc "Thay thế", nhập lý do và chọn Bảng kê doanh thu dịch vụ hoặc Doanh thu trả hộ mới. Hệ thống tự động thu thập dữ liệu và gọi API tạo hóa đơn của MISA meInvoice.
-3. Misa meInvoice trả kết quả, bao gồm mã cơ quan thuế, link PDF và link XML cập nhật trạng thái hóa đơn gốc thành “Bị thay thế” hoặc “Bị điều chỉnh”.
+3. Misa meInvoice trả kết quả, bao gồm mã cơ quan thuế, link PDF và link XML cập nhật trạng thái hóa đơn gốc thành "Bị thay thế" hoặc "Bị điều chỉnh".
```

### 3.3. Thu thập & định danh hóa đơn đầu vào và làm thanh toán tự động (IIP) _(trước: 3.3. Thu thập & định danh hóa đơn đầu vào và làm thanh toán tự động)_

```diff
-Mục này này mô tả giải pháp tự động hóa toàn diện luồng xử lý hóa đơn đầu vào của Delta nhằm loại bỏ hoàn toàn việc nhập tay thông tin định danh và phân loại thủ công hóa đơn đầu vào. Quy trình sử dụng API Banking để ghi nhận thông tin định danh giao dịch (Người thực hiện Yêu cầu thanh toán, JobID), kết hợp Misa API Gateway để thu thập hóa đơn tập trung và chuyển giao dữ liệu cho Trợ lý AI01 đối chiếu chéo, kiểm soát trùng lặp và tự động đưa hóa đơn vào danh mục quản lý.
-- Tự động làm thanh toán cho các hóa đơn được phân loại nhóm phí là chi phí trả hộ hoặc doanh thu trả hộ theo Quy trình thanh toán trả hóa đơn.
-- Tự động ghi giảm “Dư nợ tạm ứng 2” của nhân viên tương ứng với hóa đơn trả hộ làm thanh toán.
+Tài liệu này mô tả giải pháp tự động hóa toàn diện luồng xử lý hóa đơn đầu vào của Delta, loại bỏ hoàn toàn việc nhập liệu thủ công, chọn phân loại chi phí, và rà soát hóa đơn bằng tay. Giải pháp này có các mục tiêu sau:
+- Định danh tự động: Sử dụng dữ liệu API Banking kết hợp dữ liệu hóa đơn để tự động gán Mã nhân viên và Số JobID nghiệp vụ cho hóa đơn.
+- Triệt tiêu rủi ro trùng lặp: Loại bỏ 100% rủi ro chi trả nhiều lần hoặc thanh toán âm thông qua thuật toán kiểm soát trùng lặp lịch sử và va chạm thời gian thực.
+- Quyết toán & Hoàn trả tự động: Phân tách luồng xử lý để tự động ghi giảm dư nợ tạm ứng cho nhân viên chi qua bank công ty, hoặc thực hiện lệnh chi hoàn trả tiền túi cho nhân viên chi bằng tiền mặt/thẻ cá nhân.
```

### 5.2. Chi phí thực hiện kết nối API Banking

```diff
-| 1 | MB Bank | Miễn phí | 7 triệu/tài khoản nếu không đạt trị giá thanh toán phí trả hộ 3 tỷ/tháng cho cả 3 tài khoản. | 3,000,000 | Trong MB: 1,000 đồng / giao dịch. Ngoài MB (1) 1,500 đồng / giao dịch < 500 triệu (2) 0,025%*Giá trị giao dịch, phí tối đa 300,000 đồng / giao dịch> =500 triệu. | Không yêu cầu cam kết nhưng đề nghị Delta hỗ trợ mỗi tháng một thời điểm duy trì mức 10-15 tỷ. | 3 tỷ đồng cho 3 tài khoản thì được miễn phí phí duy trì hàng tháng. |
+| 1 | MB Bank | Miễn phí | 7 triệu/tài khoản nếu không đạt trị giá thanh toán phí trả hộ 3 tỷ/tháng cho cả 3 tài khoản. | 3,000,000 | Trong MB: 1,000 đồng / giao dịch. Ngoài MB (1) 1,500 đồng / giao dịch < 500 triệu (2) 0,025%*Giá trị giao dịch, phí tối đa 300,000 đồng / giao dịch > = 500 triệu. | Không yêu cầu cam kết nhưng đề nghị Delta hỗ trợ mỗi tháng một thời điểm duy trì mức 10-15 tỷ. | 3 tỷ đồng cho 3 tài khoản thì được miễn phí phí duy trì hàng tháng. |
-| 3 | Techcombank | 70 triệu | 5 triệu / tháng / tài khoản nếu ít hơn 500 giao dịch trả hộ / tháng. | Không chào phí | Trong TCB: Miễn phí. Ngoài TCB: 6,000 đồng / giao dịch. | Không yêu cầu cam kết. | 500 giao dịch chi hộ / tài khoản / tháng. |
-| 4 | Vietcombank _(Đồng ý cung cấp API Banking, chờ báo giá chi phí)_ | | | | | | |
+| 3 | Vietcombank _(Đồng ý cung cấp API Banking, chờ báo giá chi phí)_ | | | | | | |
```

