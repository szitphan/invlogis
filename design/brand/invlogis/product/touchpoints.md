# Điểm chạm sản phẩm: hiện tại và đề xuất (Mốc 3, bản nháp)

Chỉ đề xuất, chưa đổi file sản phẩm. Màu nhấn giao diện giữ than chì `#262626` (DEC-041, DEC-042, DEC-066). Gradient và cobalt chỉ ở mặt điểm chạm (panel thương hiệu, icon, header email).

| Điểm chạm | Hiện tại | Đề xuất | Cần founder quyết (Y/N) | File sẽ đổi sau trong sản phẩm (chỉ liệt kê) |
|---|---|---|---|---|
| Đăng nhập web (desktop) | Mẫu P6: thẻ giữa nền body hoặc split form và ảnh, logo khách ở ô logo | Split: panel gradient lụa (logo reverse + "Khai mở cách vận hành mới.") và form sản phẩm, nút than chì | **Y** (chọn split + dùng gradient ở panel) | `design/design.md` mục P6; `design/ui-common/screen-patterns.md`; Figma 2749:3026 và các biến thể; `prototype/src/**/login*` |
| Đăng nhập khi có khách (tenant) | Ô logo khách (`P-logo`, `P-mau-logo`) | Logo khách đặt thẳng trên form, cao 40; chân ghi "Được phát triển bởi innvie" cao 20, tắt được theo khách. Không dùng "Vận hành trên" | Đã chốt DEC-326 | như trên; `docs/_product/tenant-parameters.md` (`P-hien-phat-trien-boi`); `login-web-tenant-*.html` còn chữ cũ |
| Đăng nhập mobile | Chưa có chuẩn M riêng (Known Gap) | Header gradient (có lớp phủ tối 42% để chữ đạt 4,5:1) + tờ trắng bo 24px | **Y** | `design/design.md` (thêm mẫu M); Figma |
| Splash mobile/web | Logo khách giữa, chân: "Được phát triển bởi" + logo innvie 26px (DEC-037) | Logo khách ngang cao 64, theo chế độ, khách chưa có bản nền tối thì giữ nền trắng; chân "Được phát triển bởi innvie" cao 20, tắt được theo khách | Đã chốt DEC-326 | `design/design.md` § Splash web; `splash-mobile-b.html` còn chữ cũ; Figma 5562:103807..103825 và 5521:94959; artifact "Splash screen web"; `prototype/src/**/splash*` |
| Icon app iOS/Android | Chưa có icon thương hiệu mới | Theo khách ngay từ đầu (`P-icon-app`, DEC-326). Bộ Invlogis: phương án B `app-icon-1024.png`; Android adaptive nền + lớp trước 432. Kéo theo nhu cầu mỗi khách một bản app, chờ xác nhận ở `saas-core-vs-tenant.md` Mục 7 việc 3 | Đã chốt theo khách; một bản hay nhiều bản app chờ xác nhận | cấu hình app mobile (asset catalog, `mipmap-*`), `prototype/public/` apple-touch-icon |
| Favicon tab | Chưa có / mặc định | Theo khách ngay từ đầu (`P-favicon`, DEC-326). Bộ Invlogis: `favicon.svg` + PNG 16/32/48, đọc được trên nền sáng và tối | Đã chốt DEC-326 | `prototype/src/app/` (icon), `<link rel="icon">` |
| Email giao dịch (mời, OTP, đặt lại MK) | Chưa có mẫu | Bảng 600px, **logo khách** (`P-logo`, DEC-326; ảnh PNG xuất từ tệp khách, nền tối dùng `P-logo-nen-toi`), thân trung tính, nút than chì. Mẫu trong `email/` đang là logo reverse Invlogis trên header chàm đêm, chỉ đúng khi chưa có khách; nền header khi có logo khách chưa quyết | **Y** (nội dung, tên người gửi, nền header); ảnh logo đang trỏ URL giữ chỗ `https://[chờ: tên miền]/brand/email/logo-reverse.png`, cần tên miền và tải PNG từ `assets/email/` lên | dịch vụ gửi mail (template), 3 file ở `email/` |
| Màn tải | Splash không thanh tải; chuyển trang dùng `Skeleton` | Dùng chuyển động logo (dải lụa kéo lên, chấm gập, chữ hiện dần); bản tĩnh khi `prefers-reduced-motion` | Y | `design/design.md` § Splash web (chuyển động); `design/brand/invlogis/logo/logo-motion.html` (**lỗi: thiếu `--k` nên chữ không chạy, xem README**) |
| Màn Giới thiệu | Chưa có | Lockup `invlogis by innvie`, phiên bản, liên kết pháp lý, "Invlogis là sản phẩm của innvie" | **Y** (có đặt innvie ở đây, độc lập với DEC-037) | màn Cài đặt mới trong sản phẩm |
| Chữ và màu trong UI | Inter / Cal Sans, than chì | Không đổi | N | không có |

## Chân màn khi có logo khách (DEC-326)

Giữ tinh thần DEC-037: chân đăng nhập, splash ghi "Được phát triển bởi innvie", cao 20. Không dùng "Vận hành trên" và lockup 72px. Tắt được theo khách qua `P-hien-phat-trien-boi`, mặc định bật, Delta chưa chốt. innvie vẫn ở màn Giới thiệu và giấy tờ.
