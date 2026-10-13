# Tích hợp hệ thống VIS & SIM — Công tác chuẩn bị

> Nguồn: [`SIM & VIS_Công tác chuẩn bị_Oct 11 2026.docx`](source/vis-sim-cong-tac-chuan-bi.docx) (Word) · Nhận: 2026-10-12 · Chuyển sang Markdown bằng `/intake`.
> Thông tin trang: chân trang "SIM & VIS_Công tác chuẩn bị_Octpber 11, 2026 — Trang: 1/16" (giữ nguyên như bản gốc).

*Hà Nội, ngày 11 tháng 10 năm 2026*


## I. TỔNG QUAN

### 1.1. Dự án bao gồm hai phân hệ chính

- Vehicle Intelligent Service (VIS): Hệ thống xử lý dữ liệu vận hành đội xe thời gian thực (Event-driven) dựa trên các điều kiện logic cứng về tọa độ, vận tốc và thời gian.
- Solutions for Invoice Management (SIM): Trục tích hợp tự động hóa luồng thanh toán API Banking, kết nối Open API MISA và đối soát hóa đơn.

### 1.2. Định vị vai trò kỹ thuật

- 95% Hệ thống là code quy tắc truyền thống: Toàn bộ luồng tiền ngân hàng, lệnh chi, đối soát ma trận dữ liệu, quản lý Geofence, và xử lý dữ liệu GPS hoàn toàn sử dụng lập trình backend truyền thống để đảm bảo tính chính xác tuyệt đối (100% Deterministic).
- 5% Hệ thống ứng dụng AI bổ trợ: AI không đóng vai trò cốt lõi hay ra quyết định điều hành. AI chỉ được sử dụng như một công cụ phụ trợ (OCR Engine) ở khâu đầu vào của giải pháp SIM. Cụ thể, khi tài xế hoặc nhân viên hiện trường chụp ảnh/upload hóa đơn dạng tệp PDF/ảnh, mô hình AI OCR được gọi để quét và chuyển đổi hình ảnh thành chuỗi văn bản (Text) tại mục "Ghi chú/Nội dung". Ngay sau khi thông tin được văn bản hóa, code truyền thống (Regex/Query) lập tức tiếp quản để xử lý logic. Đối với tệp hóa đơn gốc XML nhận từ Misa Gateway, hệ thống dùng bộ phân tích cú pháp XML Parser truyền thống để đọc dữ liệu chính xác 100%, hoàn toàn không dùng đến AI.

## II. KHỐI LƯỢNG CÔNG VIỆC PHÁT TRIỂN

Mục này ước tính khối lượng công việc để định hướng cho việc chuẩn bị nhân sự thực hiện. Triển khai các kết nối ngoại vi, đặc biệt với ngân hàng thì nhân sự phải có chuyên môn phù hợp ở trình độ cao. Nếu có rủi ro an ninh thì họ sẽ từ bỏ việc triển khai cổng kết nối với Delta ngay lập tức vì một khách hàng cỡ Delta là quá nhỏ so với bất kỳ ngân hàng nào.

### 2.1. Trục nền tảng trung tâm & API gateway

- Kiến trúc xử lý: Thiết kế trục tích hợp Integration Hub và Gateway trung tâm sử dụng kiến trúc Message Queue để nhận và điều phối dữ liệu bất đồng bộ.
- Bảo mật Core Banking: Triển khai các chuẩn bảo mật lập trình bắt buộc gồm giao thức đường truyền mTLS (Mutual TLS), mã hóa dữ liệu đầu cuối bằng thuật toán AES-256, và cấu hình chữ ký số phần cứng RSA để kết nối trực tiếp với cổng ngân hàng.
- Cơ chế Hàng đợi: Viết code quản lý hàng đợi ký số (Signing Queue) và cơ chế tự động thử lại (Retry Mechanism) với cấu hình lũy tiến để xử lý rủi ro nghẽn mạng từ Cục Thuế.

### 2.2. Phân hệ VIS - Quản lý đội xe

- Delta MIS Service Worker: Lập trình tiến trình ngầm tiếp nhận sự kiện webhook từ EUP Server để cập nhật liên tục tọa độ, tốc độ, mức dầu thực tế.
- Logic xử lý biến cố vận hành (Rule-based):
  - *Kẹt xe (Traffic Jam):* Cài đặt điều kiện cứng: Nếu Vận tốc < 5 km/h + Trạng thái máy mở (Engine ON) duy trì liên tục > 10 phút => Tự động tính tổng thời gian và gọi bảng Định mức để đề xuất số lít dầu bù.
  - *Nổ máy ngủ (Idling Time):* Cài đặt điều kiện cứng: Nếu Vận tốc = 0 km/h + Trạng thái máy mở duy trì liên tục > 10 phút => Ghi nhận thời gian vô ích và tính số dầu hao phí.
- Quản lý trạm vé (Polygon Geofence): Sử dụng các thuật toán hình học máy tính thuần túy để vẽ và xác định xe đi vào vùng đa giác bao trọn trạm vé nhằm triệt tiêu lỗi bắt hụt sự kiện.
- Thuật toán đối soát chéo (Matrix Matching): Lập trình module so khớp dữ liệu GPS và API giao dịch trừ tiền từ VETC nhằm tự động phân loại xe "Đã qua" hoặc lái xe "Tránh trạm vé / Sai lộ trình".
- Kiểm soát nhiên liệu: Viết code nhận diện biến động thể tích bình dầu theo quy tắc sụt giảm đột ngột (giảm quá 5 lít trong dưới 3 phút => Hút dầu bất thường) hoặc tăng liên tục (tăng trên 20 lít trong 10 phút => Sự kiện Đổ dầu) để đối soát chéo với Phiếu cấp dầu điện tử.
- Quy trình JobID J01 (Tìm vỏ container rỗng): Viết logic tự động tính số kms phát sinh bằng cách lấy Tổng hành trình thực tế trừ đi Lộ trình chuẩn của Lệnh vận tải, áp định mức tải trọng 0 kg để tính số dầu cấp bù.

### 2.3. Phân hệ SIM - Quản lý hóa đơn & Tài chính (95% code, 5% AI bổ trợ)

- Engine Quét & Đọc Hóa Đơn (AI01):
  - *Mảnh ghép AI (5%):* Tích hợp một thư viện/mô hình học máy PDF OCR Engine để quét hình ảnh/văn bản của file PDF/ảnh do nhân viên upload thủ công, thực hiện nhiệm vụ duy nhất là nhận diện chữ viết tại mục "Ghi chú/Nội dung".
  - *Mảnh ghép Code truyền thống (95%):* Phát triển bộ XML Parser để đọc trực tiếp thẻ dữ liệu có cấu trúc từ Misa API Gateway (độ chính xác tuyệt đối 100%). Viết thuật toán so khớp cấu trúc (Cross-matching 1-1) để tự động ghép hóa đơn với giao dịch ngân hàng theo các hàm điều kiện bằng tiền, tên nhà cung cấp và sai số ngày lập ± 3 ngày.
- Trục Tích hợp Kết nối Ngân hàng (API Banking): Lập trình luồng Outbound đẩy lệnh lập Ủy nhiệm chi sang hệ thống 3 ngân hàng (MB, TPBank & Vietcombank) và luồng Inbound Webhook tiếp nhận Sổ phụ điện tử/biến động số dư thời gian thực.
- Tích hợp Open API MISA meInvoice & AMIS: Lập trình luồng tự động đẩy dữ liệu sang cổng MISA meInvoice để ký số từ xa (Cloud HSM) và luồng đồng bộ ngược (Reverse Sync API) tự động hạch toán, tạo chứng từ chi tiền trên MISA AMIS khi có thông báo trích tiền thành công từ Bank.
- Giao diện ứng dụng: Xây dựng hệ thống màn hình Web/App để nhân viên, lái xe tải ảnh QR (tĩnh/động), hiển thị danh mục quản lý hóa đơn theo trạng thái và xử lý phân hệ "Hóa đơn vô chủ".

## III. LÀM VIỆC VỚI ĐỐI TÁC

Để chuẩn bị tốt nhất cho đội ngũ lập trình phát triển hai bộ giải pháp SIM (Quản lý hóa đơn) và VIS (Số hóa dữ liệu vận hành đội xe), Delta cần làm việc với 4 nhóm đối tác để thống nhất về tài liệu API, môi trường thử nghiệm (Sandbox), tiêu chuẩn bảo mật và cơ chế đồng bộ dữ liệu. Mục này liệt kê các công việc cần thực hiện với từng đối tác:

### 3.1. Ngân hàng (MB, VCB, TPBank)

- Thống nhất chuẩn bảo mật nghiêm ngặt: Yêu cầu ngân hàng cung cấp tài liệu kết nối sử dụng giao thức mã hóa đường truyền mTLS (Mutual TLS). Phối hợp cấu hình thuật toán mã hóa đầu cuối AES-256 và bàn giao chữ ký số RSA.
- Đăng ký gói API trọn gói cho đa pháp nhân: Đặt hàng giải pháp API Banking dùng chung hệ thống quản trị nhưng quản lý đồng thời cả 3 tài khoản hoạt động độc lập của Delta HN, Delta HCM và Delta Hải Phòng.
- Thống nhất cấu trúc dữ liệu lệnh chi và sổ phụ:
- Cung cấp mẫu biểu và các thông tin định danh lệnh chuyển tiền theo yêu cầu của ngân hàng.
- Yêu cầu ngân hàng cung cấp định dạng Sổ phụ điện tử cố định để lập trình tính năng tự động đối soát công nợ.
- Cấu hình Webhook và mã tham chiếu đối chiếu:
- Yêu cầu ngân hàng cung cấp Inbound Webhook để tự động bắn tín hiệu biến động số dư theo thời gian thực về Delta API Gateway.
- Thiết kế cơ chế lưu vết để đối chiếu song song giữa Mã giao dịch tham chiếu (Mã FT...) của ngân hàng với JobID phục vụ hạch toán tự động.
- Đàm phán chi phí kết nối: Làm việc riêng với Vietcombank để nhận báo cáo giá chi phí kết nối API. Đăng ký cơ chế trích nợ tự động Auto-topup trên hệ thống Vietcombank Corporate Internet Banking.

### 3.2. MISA (meInvoice, AMIS, eSign Cloud)

- Kết nối cổng Open API phát hành hóa đơn: Tiếp cận tài liệu Open API của MISA meInvoice để Delta MIS truyền dữ liệu xuất/điều chỉnh hóa đơn tự động.
- Tích hợp giải pháp ký số từ xa: Đăng ký và kết nối gói doanh nghiệp qua API của MISA eSign Cloud để ký số hóa đơn tự động 100% không cần con người can thiệp.
- Cấu hình Webhook gom hóa đơn đầu vào: Thiết lập cơ chế webhook hoặc scheduler pull định kỳ từ Misa API Gateway để tự động đẩy gói dữ liệu chứa file XML gốc và bản PDF hóa đơn đầu vào về hệ thống.
- Phát triển luồng đồng bộ ngược (Reverse sync API): Phối hợp kết nối API đối ứng sang MISA AMIS. Đảm bảo khi Delta MIS thanh toán thành công, hệ thống sẽ tự động tạo chứng từ chi, khớp hóa đơn đầu vào và ghi nhận mã FT ngân hàng vào trường số chứng từ gốc trên AMIS.

### 3.3. Giám sát hành trình EUP

- Xây dựng kiến trúc hướng sự kiện (Event-driven): Yêu cầu EUP hỗ trợ và cung cấp tài liệu cơ chế Webhook để ghi nhận liên tục trạng thái thay đổi của xe (tọa độ, vận tốc, trạng thái máy hoạt động).
- Thống nhất tần suất quét dữ liệu (Polling): Thiết lập cơ chế cho phép Delta MIS chủ động quét với tần suất thấp (30-60 phút/lần) khi xe tắt máy nhằm kiểm tra lượng dầu tồn.
- Dùng chung cấu hình ngưỡng sensor dầu: Làm việc chặt chẽ với EUP để đồng bộ cấu hình cài đặt sensor nhằm phát hiện bất thường. Cụ thể:
- Ngưỡng cảnh báo hút dầu trái phép: Giảm quá 5 lít trong dưới 3 phút.
- Ngưỡng ghi nhận sự kiện đổ dầu: Tăng liên tục trên 20 lít trong vòng 10 phút khi xe dừng hoạt động.

### 3.4. Thu phí tự động VETC

- Cấu hình tài khoản doanh nghiệp tập trung: Đăng ký cấu trúc quản lý chi phí "Một tài khoản mẹ (Master Account) - Nhiều tài khoản con" cho đội xe thuộc Delta VT và Delta HCM.
- Kết nối API đối soát trạm vé: Đề nghị VETC cung cấp tài liệu VETC API để Delta MIS tự động gọi và thu thập danh sách giao dịch trừ tiền phát sinh của phương tiện.
- Định nghĩa khung thời gian đối soát: Lập trình luồng dữ liệu gọi API VETC ngay tại thời điểm xe kích hoạt Geofence điểm đích (kết thúc Lệnh vận tải) nhằm đối soát chéo dữ liệu GPS thực tế với dữ liệu trừ tiền.
