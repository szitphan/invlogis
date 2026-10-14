# Mốc 3.5: nhận diện tại điểm chạm sản phẩm (bản nháp)

Đề xuất chờ founder duyệt. Không sửa `design/design.md`, `design-tokens.css`, prototype, Figma. Nguồn: logo và nền ở `design/brand/invlogis/` (bản sao trong `assets/`). Người dùng mẫu: "Công ty Vận tải Mẫu" (không dùng tên khách thật).

| # | Sản phẩm | HTML | PNG |
|---|---|---|---|
| 1 | Đăng nhập web (mặc định, khách; desktop 1440x900, mobile 390x844) | `login-web-{default,tenant}-{desktop,mobile}.html` | `previews/` cùng tên |
| 2 | Splash A (giữ DEC-037) và B (đề xuất) | `splash-mobile-a.html`, `-b.html` | `previews/` |
| 3 | Icon app iOS/Android | `app-icon-in-context.html` | `previews/` |
| 4 | Favicon tab sáng/tối | `browser-tab.html` | `previews/` |
| 5 | Email: mời, OTP, đặt lại MK | `email/*.html` (bảng, style inline, 600px) | `previews/email-*.png` |
| 6 | Màn tải (+5 khung chuyển động), Giới thiệu | `loading-screen.html`, `loading-motion-frames.html`, `about-screen.html` | `previews/` |
| 7 | Bảng điểm chạm | `touchpoints.md` | |
| 8 | Tổng hợp | | `previews/contact-sheet.png` |

Dựng lại: `python3 _build.py && python3 _contact.py`.

## Kiểm tra
- Chữ trắng trên panel gradient: desktop tối thiểu 6,1:1; mobile có lớp phủ mực 42% (không phủ thì 3,7 đến 4,3:1, trượt) nên đạt khoảng 7,5:1. Chữ phụ `#737373` trên trắng 4,74:1; nút than chì 15,1:1.
- Ngôn ngữ tiếng Việt có dấu đầy đủ.

## Lưu ý
- `design/brand/invlogis/logo/logo-motion.html` có lỗi: biến `--k` (độ trễ từng chữ) không được gán nên animation của chữ bị bỏ, chỉ chữ i chạy. Bản trong thư mục này đã gán `--k` theo thứ tự. Chưa sửa file gốc.
- Hiển thị dùng Inter nếu máy có, nếu không dùng Be Vietnam Pro; Cal Sans không đóng gói. Ảnh mockup khác font so với sản phẩm thật.
- Logo email dùng PNG (`assets/email/`), khi phát hành cần URL công khai.
- Logo khách "M" chỉ là mẫu minh hoạ.

## Dựng lại (yêu cầu)
- macOS có Google Chrome tại `/Applications/Google Chrome.app` (`_tools/render.py` dùng đường dẫn này) và Python có Pillow.
- HTML trong `email/`, các trang HTML và `previews/` đều do máy sinh. Sửa `_build.py` rồi chạy lại, không sửa tay file đầu ra.
- Email: logo trỏ `https://[chờ: tên miền]/brand/email/logo-reverse.png` (chỗ giữ chỗ, chờ tên miền). Bản PNG cục bộ giữ ở `assets/email/`; ảnh xem thử dùng bản cục bộ.
