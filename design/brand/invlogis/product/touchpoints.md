# Điểm chạm sản phẩm: hiện tại và đề xuất (Mốc 3, bản nháp)

Chỉ đề xuất, chưa đổi file sản phẩm. Màu nhấn giao diện giữ than chì `#262626` (DEC-041, DEC-042, DEC-066). Gradient và cobalt chỉ ở mặt điểm chạm (panel thương hiệu, icon, header email).

| Điểm chạm | Hiện tại | Đề xuất | Cần founder quyết (Y/N) | File sẽ đổi sau trong sản phẩm (chỉ liệt kê) |
|---|---|---|---|---|
| Đăng nhập web (desktop) | Mẫu P6: thẻ giữa nền body hoặc split form và ảnh, logo khách ở ô logo | Split: panel gradient lụa (logo reverse + "Khai mở cách vận hành mới.") và form sản phẩm, nút than chì | **Y** (chọn split + dùng gradient ở panel) | `design/design.md` mục P6; `design/ui-common/screen-patterns.md`; Figma 2749:3026 và các biến thể; `prototype/src/**/login*` |
| Đăng nhập khi có khách (tenant) | Ô logo khách (`P-logo`, `P-mau-logo`) | Logo khách đúng ô P-logo trên form; panel ghi "Vận hành trên" + logo Invlogis nhỏ. Cơ chế tenant không đổi | **Y** (chấp nhận Invlogis hiện ở panel khi có khách) | như trên; `docs/_product/tenant-parameters.md` (chỉ nếu thêm tham số ẩn/hiện dòng "Vận hành trên") |
| Đăng nhập mobile | Chưa có chuẩn M riêng (Known Gap) | Header gradient (có lớp phủ tối 42% để chữ đạt 4,5:1) + tờ trắng bo 24px | **Y** | `design/design.md` (thêm mẫu M); Figma |
| Splash mobile/web | Logo khách giữa, chân: "Được phát triển bởi" + logo innvie 26px (DEC-037) | **A:** giữ nguyên. **B (đề xuất):** chân ghi "Vận hành trên" + lockup `invlogis by innvie` cao 72px | **Y/N cho DEC-037: thay "Được phát triển bởi innvie" bằng lockup "Invlogis by innvie"?** Nếu N, giữ A | `design/design.md` § Splash web; Figma 5562:103807..103825 và 5521:94959; artifact "Splash screen web"; `prototype/src/**/splash*` |
| Icon app iOS/Android | Chưa có icon thương hiệu mới | Phương án B: `app-icon-1024.png`; Android adaptive nền + lớp trước 432 | **Y** (xác nhận B làm icon phát hành) | cấu hình app mobile (asset catalog, `mipmap-*`), `prototype/public/` apple-touch-icon |
| Favicon tab | Chưa có / mặc định | `favicon.svg` + PNG 16/32/48, đọc được trên nền sáng và tối | N | `prototype/src/app/` (icon), `<link rel="icon">` |
| Email giao dịch (mời, OTP, đặt lại MK) | Chưa có mẫu | Bảng 600px, header chàm đêm + logo reverse (PNG), thân trung tính, nút than chì | **Y** (nội dung và tên người gửi); ảnh logo đang trỏ URL giữ chỗ `https://[chờ: tên miền]/brand/email/logo-reverse.png`, cần tên miền và tải PNG từ `assets/email/` lên | dịch vụ gửi mail (template), 3 file ở `email/` |
| Màn tải | Splash không thanh tải; chuyển trang dùng `Skeleton` | Dùng chuyển động logo (dải lụa kéo lên, chấm gập, chữ hiện dần); bản tĩnh khi `prefers-reduced-motion` | Y | `design/design.md` § Splash web (chuyển động); `design/brand/invlogis/logo/logo-motion.html` (**lỗi: thiếu `--k` nên chữ không chạy, xem README**) |
| Màn Giới thiệu | Chưa có | Lockup `invlogis by innvie`, phiên bản, liên kết pháp lý, "Invlogis là sản phẩm của innvie" | **Y** (có đặt innvie ở đây, độc lập với DEC-037) | màn Cài đặt mới trong sản phẩm |
| Chữ và màu trong UI | Inter / Cal Sans, than chì | Không đổi | N | không có |

## Câu hỏi DEC-037 (nêu rõ)

DEC-037 chốt splash ghi "Được phát triển bởi innvie" với logo innvie. Bản B đổi thành "Vận hành trên Invlogis by innvie". Lý do đề xuất: sản phẩm mang tên Invlogis nên chân splash nên đọc ra tên sản phẩm; innvie vẫn xuất hiện. Đánh đổi: lockup lớn hơn (72px) cạnh logo khách; khách có thể thấy tên thương hiệu thứ hai. DEC-037 chưa ghi lý do nên cần founder quyết, không đổi nếu chưa duyệt.
