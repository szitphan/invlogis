# Catalog ví dụ shadcnuikit.com (trích 06/11, dùng dựng lại bằng foundation bộ thử)

> Trích bằng script (class Tailwind, đã lọc dark:/aria-/focus:). Mỗi ví dụ dựng lại trên trang chọn biến thể
> **bằng token bộ thử** (user 06/11: lấy mẫu web về thì bắt buộc áp foundation của mình).
> Token web chung: input/select nền `bg-input/50` (#e5e5e5 50% ≈ #f2f2f2), không viền, rounded-3xl 19.2;
> checkbox/radio nền `bg-input/90` không viền, checked bg-primary; card lựa chọn `rounded-md border p-4 shadow-xs`;
> badge rounded-3xl h-5 px-2 text-xs. Quy đổi: radius → token (nút 8, ô nhập pill, card 14, tag pill, checkbox 4).

## Button (27) — đã dựng ở `components-r1.src.html` (key `button-web-01..27`)

## Input (25) — /components/input (không có tên mẫu, đặt theo label)
1 Cơ bản (placeholder Email) · 2 Có nhãn · 3 Nhãn + chữ trợ giúp (xs muted, mt-2) · 4 Lỗi (viền đỏ + ring, chữ đỏ xs "Email is invalid")
5 Hợp lệ (viền green-600, nền trắng, dòng check-circle xanh "Username is available") · 6 Icon tìm trái + chữ "12 results" phải (input-group)
7 Tiền tố chữ "https://" + nút icon-xs info tròn phải · 8 Hậu tố chữ ".com" · 9 Hậu tố là select nhỏ ".com ▾" trong ô
10 Tiền tố "$" + hậu tố "USD" · 11 Nút copy icon-xs (rounded-xl) cuối ô · 12 Đếm ký tự còn lại dưới ô ("12 characters left")
13 Mật khẩu ẩn/hiện (icon eye phải, w-9) · 14 Nhãn nổi (label nằm giữa ô, animate lên) · 15 Giới hạn ký tự trong ô phải "0/50"
16 Nút xoá X trong ô · 17 OTP 4 ô 36×36 viền liền nhau (rounded-md hai đầu) · 18 Số điện thoại: ô chọn quốc gia (icon + ▾) dính ô nhập
19 Thẻ thanh toán: ô số thẻ (icon card) trên, MM/YY + CVC dưới, dính nhau · 20 Mật khẩu + thanh độ mạnh h-1 + danh sách 4 điều kiện (icon x)
21 Mask "AB12 CDE" · 22 Timestamp "00:00:00" · 23 Khoảng From–To hai ô dính · 24 Ô nhập + danh sách tag dưới (badge outline h-7, nút x)
25 Tag nằm trong ô (input-group h-auto p-1, badge h-7 + input)

## Select (15) — /components/select (trigger: bg-input/50 rounded-3xl px-3 h-9 gap-1.5 chevron-down)
1 Default (w-full) · 2 Auto width (w-fit) · 3 Placeholder · 4 Icon trái (clock, ps-9) · 5 Chữ trợ giúp dưới · 6 Lỗi (ring đỏ + chữ đỏ)
7 Nhóm tuỳ chọn (menu có group label) · 8 Nhãn đè viền (label xs nền trắng nằm trên mép) · 9 Trạng thái có chấm màu (● Completed)
10 Icon tuỳ chọn + dấu ✓ phải · 11 Mô tả 2 dòng + dấu ✓ phải · 12 Avatar · 13 Avatar 2 dòng (tên + @handle, h-auto)
14 Combobox có ô tìm (trigger outline: viền border-input, nền trắng, rounded-4xl, chữ placeholder muted) · 15 Combobox tìm + nút (đã chọn "Shadcn UI Kit")

## Checkbox (13) — /components/checkbox (ô 16, rounded 5px, nền input/90 không viền; checked nền primary + check)
1 Đồng ý điều khoản (label có link gạch chân) · 2 Màu riêng (đổi --primary) · 3 Todo đơn · 4 Todo "fancy" ô tròn + gạch ngang chữ khi chọn
5 Nhóm ngang (gap-4) · 6 Nhóm dọc (gap-3) · 7 Nhãn + nhãn phụ "(Sublabel)" + mô tả xs · 8 Chọn thì mở ô nhập chi tiết (expansion)
9 Thẻ: viền rounded-md p-4 shadow-xs, ô check bên phải (order-1) · 10 Thẻ có avatar 32 + nhãn/mô tả, check phải
11 Thẻ lựa chọn thông báo (rounded-lg border p-3, hover accent/50): Email / Push · 12 Chọn tất cả + con thụt 24 (Read/Write/Delete)
13 Danh sách viền chia dòng (icon + nhãn trái, check phải): Mobile/Desktop/Cloud

## Radio Group (15) — /components/radio-group (nút 16 tròn, nền input/90; checked nền primary + chấm 8 trắng)
1 Dọc (Monthly/Quarterly/Yearly) · 2 Ngang (Email/SMS/Push) · 3 Phương thức thanh toán · 4 Nhãn + nhãn phụ + mô tả
5 Chọn thì mở ô nhập (Home delivery → địa chỉ) · 6 Lọc đánh giá sao + số đếm · 7 Chọn màu (chấm 24 màu, legend)
8 Thẻ gói (viền rounded-md p-4, radio 20, giá phải) · 9 Thẻ ô vuông 3 cột icon + chữ (radio ẩn) · 10 Lưới 3 cột "2 CPU…16 CPU" (1 ô tắt)
11 Thẻ vùng nhỏ flex-wrap · 12 Danh sách gói dính nhau (-space-y-px, badge "Popular") · 13 Đánh giá 5 sao (radio ẩn)
14 Thẻ dọc căn giữa icon + tiêu đề + mô tả, radio dưới · 15 Thẻ gói chi tiết (badge giá, mô tả, danh sách •)

## Switch (10) — /components/switch (track default h-5 w-11, sm h-4 w-7, border-2, tắt nền input/90, bật primary; thumb trắng shadow-sm tròn)
1 Airplane Mode (nhãn phải) · 2 Màu riêng · 3 Vuông (track rounded-sm) · 4 Kiểu M2 (track mảnh h-3 w-9, thumb to hơn)
5 Chữ trạng thái "On/Off" cạnh nút · 6 Icon mặt trời/mặt trăng hai bên · 7–8 Nhãn/icon nằm trong track (h-full, w-auto)
9 Chữ ON/OFF trong track chữ nhật rounded-md · 10 Thẻ: nhãn + nhãn phụ + mô tả, switch phải

## Badge → Tag (17) — /components/badge (h-5 rounded-3xl px-2 text-xs font-medium; default nền primary, outline viền border)
1 Badge · 2 Có icon (zap) · 3 Số tròn "6" (primary/80) · 4 Liên kết "Go to Website" · 5 "Chat 73" (nhãn + số)
6 Outline + check "Completed" · 7 Outline "Pending" (chấm màu) · 8 Outline "Build Error" (chấm đỏ) · 9 Có nút x "Close"
10 Nhóm tag nền muted rounded-md có x (React, Tailwind, Shadcn) · 11 Tag người có avatar + x · 12 Tăng/giảm % (nền green-50/red-50, mũi tên)
13 Chấm số "3" · 14–17 Pill thông báo lớn h-9/h-10 rounded-full nền muted: "12+ New Updates" (bell), + mũi tên ↗, "AI Assistant Discover More →", "50+ Blocks Added View Changes"

## Tooltip (8) — /components/tooltip (nền foreground #0a0a0a, chữ trắng 12, px-3 py-1.5, rounded-lg 11.2, có mũi tên, max-w-xs)
1 Hover cơ bản · 2 Có tiêu đề + mô tả · 3 Stats (số liệu trong tooltip) · 4 Bốn hướng Left/Top/Bottom/Right · 5 Trigger icon info
6 Xem trước sản phẩm (ảnh + chữ) · 7 Không mũi tên · 8 Light (nền trắng viền)
