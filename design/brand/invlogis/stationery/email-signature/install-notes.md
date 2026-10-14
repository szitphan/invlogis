# Cài chữ ký email

1. Đưa `logo-by-innvie-email.png` (480 px, nền trắng) lên host có HTTPS tại `https://[chờ: domain]/brand/email/logo-by-innvie-email.png`. Ảnh nhúng base64 bị Gmail chặn, nên phải là URL tuyệt đối.
2. Thay `[chờ: ...]` trong `signature-vi.html` / `signature-en.html` (tên, chức danh, điện thoại, email, domain, địa chỉ). Khi domain chưa có, xem bản PNG `*-preview.png` (đã dùng ảnh nội bộ).
3. **Gmail:** mở file HTML trong trình duyệt, Ctrl/Cmd+A, Ctrl/Cmd+C, dán vào Cài đặt, Chữ ký. Gmail không nhận dán HTML thô, phải dán bản đã hiển thị. Ảnh phải là URL, không phải ảnh kéo thả.
4. **Outlook (Windows, bản Microsoft 365):** Tệp, Tuỳ chọn, Thư, Chữ ký, dán bản đã hiển thị. Outlook cổ điển dùng engine Word nên bỏ qua `max-width`; vì vậy bảng đã đặt `width="600"` cứng.
5. Chỉ dùng phông hệ thống (Arial) vì client email không tải web font. Màu theo bảng: mực `#0E1442`, cobalt `#2F43DB`, xám chàm `#4A5380` (6,97:1 trên trắng).
6. Logo dùng lockup "by innvie" rộng 150 px (cao khoảng 56 px, đạt cỡ tối thiểu 48 px); không kéo méo, không đổi `width`/`height` độc lập.
