# R4b: review đề xuất điểm chạm sản phẩm (Mốc 3.5)

Phạm vi: `design/brand/_drafts/m3/product/` (README, touchpoints.md, mọi PNG trong `previews/`, HTML, email). Không sửa file nào ngoài file này.

## Kết quả

PASS 11 · FAIL 0 · PARTIAL 1 · N/A 0

| # | Tiêu chí | Kết quả | Bằng chứng (file · dòng xác nhận) |
|---|---|---|---|
| 1 | Accent trong UI sản phẩm là `#262626`; gradient/cobalt chỉ ở điểm chạm | PASS | `_build.py` `:root{--accent:#262626}`; nút "Đăng nhập" nền `#262626` (15,13:1 trên trắng) ở `login-web-*.html`; gradient chỉ ở panel đăng nhập và header mobile (điểm chạm). Focus ring `rgba(38,38,38,.18)`. |
| 2 | Splash A giữ DEC-037; B ghi rõ là đề xuất | PASS | `splash-mobile-a.html`: "Được phát triển bởi" 13px + logo innvie 26px, khớp `design/design.md` § Splash web (dòng 1492). Nhãn "PHIÊN BẢN A · GIỮ NGUYÊN DEC-037" và "B · ĐỀ XUẤT (CHỜ FOUNDER DUYỆT)" trên PNG. |
| 3 | Đăng nhập tenant: logo khách chỉ ở ô logo, không đổi màu UI | PASS | `login-web-tenant-*.html`: ô "M" (#0F6B5C) và tên khách chỉ ở đầu form; nút, input, link vẫn `#262626`/`#171717`. Panel tenant hiện "Vận hành trên" + logo Invlogis, đúng DEC đề xuất Y trong touchpoints.md. |
| 4 | Icon app là phương án B, kích thước home-screen hợp lý | PASS | `assets/app-icon-1024.png` SHA-256 trùng `design/brand/invlogis/logo/app-icon-1024.png` (f41fb1bb…). Mock 60/40/29/20 pt, 90 px touch icon, Android adaptive 432 px vùng an toàn 66 dp. |
| 5 | Favicon đúng file đã duyệt, đọc được sáng/tối | PASS | `assets/favicon.svg` trùng SHA-256 với `logo/favicon.svg` (926936d2…). `browser-tab.png` cho thấy tab sáng và tối; ký hiệu không khung đọc được cả hai nền. Lưu ý 16 px nhỏ, xem Nice to have. |
| 6 | Email: bảng, inline, 600 px, dấu đúng, không web font, logo `<img>` | PASS (kèm lưu ý) | `email/*.html`: `role="presentation"`, `width="600"`, `style` inline, không `@import`/`<link>`, font stack `-apple-system,'Segoe UI',Roboto…`. Logo `<img src="../assets/email/logo-reverse.png">` là đường dẫn tương đối, chưa phải URL công khai (touchpoints đã nêu). |
| 7 | Tương phản: chữ thường ≥4,5:1, chữ lớn ≥3:1, gồm chữ trắng trên gradient | PASS | Xem bảng tương phản bên dưới. |
| 8 | Vùng an toàn, cỡ tối thiểu, đúng biến thể theo nền | PASS | Cỡ tối thiểu theo `logo/logo-spec.md` Mục 2 (logo chữ màn hình ≥20 px, lockup "by innvie" ≥48 px, lockup có khẩu hiệu ≥64 px): login desktop 52 px, mobile 28–40 px, splash B 72 px, email 150×43 px. Biến thể: reverse trên chàm/gradient, `invlogis-by-innvie` màu trên trắng (splash B), logo-reverse PNG trên header email. Vùng an toàn thấy được trong panel đăng nhập (padding 56–64 px). |
| 9 | Không có "Delta", không stock photo, khách mẫu trung tính | PASS | `grep -ri delta design/brand/_drafts/m3/product/` không có kết quả. Khách mẫu "Công ty Vận tải Mẫu", người dùng "An Nguyễn"/"binh.tran@congtymau.vn". Nền là file `assets/bg-n*.jpg` (nền lụa thương hiệu, không phải ảnh stock). Chưa mở từng file JPG để xác nhận nguồn. |
| 10 | Dấu tiếng Việt đúng trong mọi PNG | PASS | Đã xem: "Vận hành trên", "Được phát triển bởi", "Công ty Vận tải Mẫu", "Đăng nhập một lần (SSO)", "Mã xác thực", "Chấp nhận lời mời", "Đặt lại mật khẩu", "Lệnh vận tải", "Giới thiệu", "Phiên bản A/B". Không lỗi dấu. |
| 11 | touchpoints.md đủ điểm chạm, có hiện tại/đề xuất/cần quyết, liệt kê file sẽ đổi; không đổi file sản phẩm | PASS | `touchpoints.md` có 10 dòng điểm chạm với đủ 5 cột. Git (`git status --short design/design.md design/design-tokens.css prototype/ docs/`): `design/design.md`, `design/design-tokens.css`, `prototype/` không thay đổi. Trong `docs/` có thay đổi có sẵn từ đầu phiên, không do bản nháp này: `M docs/_shared/project-profile.md`, `?? docs/_product/prd.md`, `?? docs/exports/`, `?? docs/cross-process-flow/cross-process-flow-preview.html`. |
| 12 | README giải thích cách dựng lại | PARTIAL | `README.md` có lệnh `python3 _build.py && python3 _contact.py`, nhưng không ghi: (a) `render.py` cần Google Chrome đường dẫn cố định `/Applications/Google Chrome.app/...` (macOS), (b) cần Pillow, (c) `previews/` và HTML sinh ra, không sửa tay. |

## Bảng tương phản (`design/brand/_drafts/_tools/contrast.py` và lấy mẫu nền từ PNG)

| Cặp | Tỉ lệ | Ngưỡng | Kết quả |
|---|---|---|---|
| `#171717` trên `#FFFFFF` (chữ chính) | 17,4:1 | 4,5 | đạt |
| `#737373` trên `#FFFFFF` (chữ phụ, footer email) | 4,74:1 | 4,5 | đạt |
| `#FFFFFF` trên `#262626` (nút) | 15,13:1 | 4,5 | đạt |
| `#262626` trên `#FFFFFF` (link, nhãn nút ghost) | 15,13:1 | 4,5 | đạt |
| `#FFFFFF` trên `#0E1442` (header email) | 17,54:1 | 4,5 | đạt |
| `#FFFFFF` trên `#0F6B5C` (ô "M" mẫu) | 6,41:1 | 3 (chữ lớn) | đạt |
| `#9AA0A6` trên `#35363A` (tab không chọn, nền tối) | 4,57:1 | 4,5 | đạt, sát ngưỡng |
| `#A3B0FF` trên `#0E1442` (periwinkle) | 8,53:1 | 4,5 | đạt |
| Chữ trắng trên gradient, panel đăng nhập desktop (lấy mẫu nền, không tính chữ) | ≥11:1 | 4,5 | đạt |
| Chữ trắng trên gradient, mobile có lớp phủ 42% (lấy mẫu nền) | ≥7:1 | 4,5 | đạt |

Ghi chú: một lần lấy mẫu đầu bị lẫn pixel chữ trắng nên cho kết quả sai (1–3:1). Đã lấy lại bằng cách loại pixel sáng, và các bảng trên là kết quả sau khi sửa phép đo. Không có cặp nào trượt.

## Must fix (xếp theo mức ưu tiên)

1. **README thiếu điều kiện dựng lại (tiêu chí 12).** Thêm vào README: cần Google Chrome (`render.py` đang trỏ tới `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, chỉ chạy trên macOS), cần Pillow, `previews/` và HTML sinh ra từ `_build.py`, không sửa tay.
2. **Logo email là đường dẫn tương đối (tiêu chí 6).** `email/*.html` dùng `../assets/email/logo-reverse.png`. Trước khi giao dev hoặc gửi thật, thay bằng URL công khai tuyệt đối (touchpoints đã nêu việc này; cần chốt là điều kiện phát hành).

## Nice to have

- `app-icon-in-context.png`: nhãn app (Lịch, Ghi chú, Bản đồ…) màu trắng trên nền lavender nhạt, độ tương phản thấp. Đây là mock hệ điều hành nên không phải lỗi sản phẩm, nhưng có thể đổi nền mẫu tối hơn để mock không gây hiểu lầm.
- `browser-tab.png`: nhãn "16 ×4" trên sheet dễ hiểu nhầm là kích thước; nên ghi "16 px (phóng 4×)".
- `logo-motion.html` gốc vẫn lỗi thiếu `--k` (đã ghi trong README); bản trong thư mục này đã gán. Nên sửa file gốc khi có cơ hội.
- Ảnh nền `assets/bg-n*.jpg`: nên ghi nguồn (file gốc trong `design/brand/invlogis/backgrounds/`) vào README để chứng minh không phải ảnh stock.
- Splash B: nếu dùng lockup 72 px thì nên thử một bản 48 px để so sánh độ cân đối với khách có logo lớn.
