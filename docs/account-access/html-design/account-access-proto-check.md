---
type: proto-check
feature: account-access
status: draft
updated: 2026-10-16
links:
  - docs/account-access/html-design/account-access-prototype.html
  - docs/account-access/srs/account-access-userflow.md
---

# Sổ đối chiếu prototype ↔ Figma — account-access

> Sinh bởi `/figma-proto-check account-access --after` (Flow 1–3 web, 29 cặp màn, đo 16/10/2026). Trang duyệt: https://claude.ai/artifact/6YQUy7KD2GkjDTQUwRVtRW
> Bảng 1 = quyết định theo nguyên nhân (1 dòng gộp nhiều dòng máy). Bảng 2 = khoá máy → dòng gộp; `proto-figma-diff.py --ledger` đọc cả hai: dòng `Theo DS` / `Giữ Figma` / `Bỏ qua` không báo lại, dòng `Theo prototype` mà Figma vẫn lệch thì báo lại.

## 1. Quyết định

| Khoá | Màn | Phần tử | Thuộc tính | Prototype | Figma/DS | Sửa ở | Quyết định | Ngày | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| `c01` | 1.3 · 2.1 · 3.2 — 22 chỗ | Dấu * của ô bắt buộc mất màu đỏ | Màu dấu * | Đỏ #a50c25 | Đen #171717 (đang gửi: xám #a3a3a3) | Component XDSFieldLabel (Astryx · Library) | Theo prototype | 2026-10-16 | Dấu đỏ giúp nhận ra ô bắt buộc; prototype đã duyệt dùng đỏ. (bạn chọn; 22 dòng máy) |
| `c02` | 1.3 «Quên mật khẩu» (6 state) · 2.1 «Quay về đăng nhập» (2 state) | Link mất gạch chân và nhạt hơn | Gạch chân · độ đậm · màu | Có gạch chân · 500 · #171717 | Không gạch · 400 · #262626 | Component Link (innvie · Components) | Theo prototype | 2026-10-16 | Không gạch chân thì chữ link trông như chữ thường. (bạn chọn; 28 dòng máy) |
| `c03` | 1.3 «Ghi nhớ đăng nhập» (6 state) | Ô checkbox to hơn và bo tròn | Kích thước · bo góc | 16×16 · 0 (trình duyệt tự bo 3) | 22×22 · bo 6 | Component Checkbox / CheckboxInput (innvie · Components) | Theo prototype | 2026-10-16 | Nhỏ hơn nhưng giữ tròn (bạn chọn; 16 dòng máy) |
| `c04` | 1.3 (6 state) | Chữ cạnh checkbox đậm hơn | Độ đậm | 400 | 500 | Component Checkbox / CheckboxListItem (innvie · Components) | Theo prototype | 2026-10-16 |  (theo gợi ý; 7 dòng máy) |
| `c05` | 1.5 (4 state, mỗi thẻ 1 nút) | Nút radio to hơn | Kích thước | 16×16 | 22×22 | Component Radio / RadioListItem (innvie · Components) | Theo prototype | 2026-10-16 | Cùng nguyên nhân với checkbox c03. (bạn chọn; 6 dòng máy) |
| `c06` | 1.3 · 2.1 · 3.2 — 5 câu lỗi | Chữ báo lỗi dưới ô đổi màu và giãn dòng | Màu · line-height | #a50c25 · 16 | #89001a · 20 | Component TextInput (innvie · Components) | Giữ Figma | 2026-10-16 | Hai mã đỏ khác nhau trên cùng màn: dấu * dùng #a50c25. (bạn chọn; 10 dòng máy) |
| `c07` | 1.3 · 1.5 · 3.2 | Chữ gõ trong ô cao dòng 20 thay vì tự nhiên | Line-height | 16.8 (normal) | 20 | Component TextInput (innvie · Components) | Bỏ qua | 2026-10-16 | Chữ một dòng, nhìn không thấy khác. (theo gợi ý; 18 dòng máy) |
| `c08` | 2.1 Hết thời gian · 3.3 Kiểm tra email | Tiêu đề thông báo nhỏ hơn, sát câu dưới | Cỡ / line-height · tiêu đề → câu | 24/32 · 18 | 20/28 · 8 | Component Thông báo trạng thái (innvie · Components) | Theo prototype | 2026-10-16 | Prototype dùng cùng cỡ tiêu đề 24 cho mọi màn đăng nhập. (theo gợi ý; 12 dòng máy) |
| `c09` | 3.1 (2 thẻ) | Thẻ điều hướng nhạt hơn, chữ tiêu đề mảnh hơn | Độ đậm tiêu đề · viền · tiêu đề → mô tả | 600 · 1px #d4d4d4 · 5 | 500 · 1px #00000014 · 2 | Component Thẻ điều hướng (innvie · Components) | Theo prototype | 2026-10-16 | Mô tả «Khi không có…» bị xuống 2 dòng vì thẻ Figma hẹp hơn (xem m01). (theo gợi ý; 10 dòng máy) |
| `c10` | 1.5 (4 state) | Thẻ chọn chi nhánh: nền trắng, viền nhạt, chữ sát nhau | Nền · viền · tiêu đề → mô tả · cao | Không nền · 1px #d4d4d4 · 5 · 63 | #ffffff · 1px #00000014 · 2 · 68 | Component Thẻ chọn (innvie · Components) | Theo prototype | 2026-10-16 | Thẻ đang chọn: prototype viền 1px #262626, Figma 2px. (theo gợi ý; 39 dòng máy) |
| `c11` | 1.5 (4 state) | Hộp «Chọn chi nhánh» hẹp hơn, có thêm 2 đường kẻ | Rộng · màu tiêu đề · lề trong · đường kẻ | 480 · #171717 · 20/23 · 0 | 400 · #1c2b33 · 17/16 · 2 | Component Dialog (Astryx · Library) | Theo prototype | 2026-10-16 | Màu tiêu đề #1c2b33 là màu riêng của Astryx, lệch mọi tiêu đề khác. (theo gợi ý; 26 dòng máy) |
| `s01` | 1.3 · 2.1 · 3.1 · 3.2 · 3.3 · 3.5 | Khung trắng của form: lề trong rộng hơn, viền nhạt hơn | Lề trong trái/trên · viền | 21/25 (3.2: 21/24 · 3.3: 27/97) · 1px #d4d4d4 | 33/33 (3.2: 33/39 · 3.3: 34/105) · 1px #00000014 | Màn — khung form của mọi màn đăng nhập | Theo prototype | 2026-10-16 | Đây là nguyên nhân gốc: lề rộng hơn làm mọi khoảng cách ngang bên trong đổi theo (vd «Ghi nhớ» → «Quên mật khẩu» 108 → 76). (theo gợi ý; 86 dòng máy) |
| `s02` | 1.3 (8 state, kể cả nền sau 1.5) | Tiêu đề trang nhỏ hơn | Cỡ / line-height | 24/32 | 20/28 | Màn — chữ tiêu đề «Đăng nhập» | Theo prototype | 2026-10-16 | 2.1, 3.1, 3.2 trên Figma vẫn 24; chỉ 1.3 bị 20. (theo gợi ý; 10 dòng máy) |
| `s03` | 1.3 (6 state) | Nhịp dọc của form đăng nhập giãn ra | Khoảng cách dọc | Ô → ô 23 · Mật khẩu → Ghi nhớ 23 · Quên mật khẩu → nút 25 | 26 · 32 · 32 | Màn — 1.3 | Theo prototype | 2026-10-16 |  (theo gợi ý; 26 dòng máy) |
| `s04` | 1.3 (6 state) | Dòng «Chưa có tài khoản?» canh giữa | Canh lề | Trái | Giữa | Màn — 1.3 | Theo prototype | 2026-10-16 | Prototype canh trái thẳng với các ô. (theo gợi ý; 6 dòng máy) |
| `s05` | 3.1 · 3.2 (6 state) | Nút «Quay lại» rộng hơn, xa tiêu đề hơn | Rộng · Quay lại → tiêu đề | 94 · 20 | 102 · 26 | Màn — 3.1, 3.2 | Theo prototype | 2026-10-16 |  (theo gợi ý; 12 dòng máy) |
| `s06` | 3.3 (3 state) | Khối «Chưa nhận được email?» đổi bố cục | Nền · nút · chữ | Hộp nền #f1f1f1 bo 12 · 2 nút xếp dọc rộng hết khối · «Gửi lại link» nền trắng có viền · «Liên hệ IT» gạch chân · tiêu đề khối 600 · câu hướng dẫn #525252 | Không nền · 2 nút cùng hàng 163px · «Gửi lại link» nền xám · «Liên hệ IT» không gạch · 500 · #737373 · thêm đường kẻ trên «Quay về đăng nhập» | Màn — 3.3 (+ Component Button cho 2 nút) | Theo prototype | 2026-10-16 | Dòng «Tài khoản: an.nguyen» + «Nhập lại tên tài khoản» là phần bạn đã chốt 16/10, giữ nguyên (d04). Hàng này chỉ nói về bố cục khối bên dưới. (theo gợi ý; 56 dòng máy) |
| `s07` | 1.3 · 2.1 Submitting | Đang gửi: Figma làm mờ nhãn ô | Màu nhãn khi đang gửi | Giữ nguyên #171717 | #a3a3a3 (như ô bị khoá) | Màn — state Submitting | Theo prototype | 2026-10-16 | Figma thêm hành vi khoá ô khi đang gửi; prototype chỉ đổi nút. Chọn Giữ Figma nếu muốn khoá ô. (theo gợi ý; 10 dòng máy) |
| `s08` | 1.5 (3 state) — ~40 dòng máy báo «Figma có» | Nền sau hộp chọn chi nhánh vẽ đủ form | Nền sau lớp mờ | Khung xương: tiêu đề + 2 thanh xám | Form đăng nhập đầy đủ | Màn — 1.5 | Theo prototype | 2026-10-16 | Nằm sau lớp phủ tối, không ảnh hưởng nhìn hộp chọn. (bạn chọn; 50 dòng máy) |
| `s09` | 2.1 (4 state) | Nhịp dọc nhỏ ở form tạo mật khẩu | Khoảng cách dọc | Gợi ý → ô sau 44 · ô cuối → nút 29 | 40 · 32 | Màn — 2.1 | Bỏ qua | 2026-10-16 | Lệch 3–4px. (theo gợi ý; 13 dòng máy) |
| `m01` | 3.5 | Vòng biểu tượng đồng hồ đổi sang đỏ | Nền vòng icon (so bằng mắt) | Xám trung tính | Đỏ nhạt | Màn — 3.5 | Bỏ qua | 2026-10-16 | Prototype dùng vòng đỏ cho lỗi (2.1 hết hạn) và xám cho thông báo; link hết hạn là thông báo. (bạn chọn; 1 dòng máy) |
| `d01` | 2.1 · 3.2 | Nút chính đổi chữ | Chữ nút | «Xác nhận» | «Đặt mật khẩu» (2.1) · «Gửi link đặt lại» (3.2) | Màn | Giữ Figma | 2026-10-16 | Đã chốt trên Figma 16/10. (theo gợi ý; 15 dòng máy) |
| `d02` | 2.1 (5 state) — kéo theo tiêu đề → ô 18 → 66 | 2.1 thêm câu dẫn mật khẩu tạm | Phần tử | Không có | «Mật khẩu tạm chỉ dùng một lần. Hãy đặt mật khẩu của riêng bạn.» | Màn | Giữ Figma | 2026-10-16 | Đã chốt 16/10. (theo gợi ý; 14 dòng máy) |
| `d03` | 3.2 (5 state) — kéo theo nhãn → ô 12 → 30 | 3.2 thêm gợi ý dưới nhãn | Phần tử | Không có | «Tên bạn dùng để đăng nhập.» | Màn | Giữ Figma | 2026-10-16 | Đã chốt 16/10. (theo gợi ý; 9 dòng máy) |
| `d04` | 3.3 (3 state) | 3.3 thêm dòng tài khoản + link nhập lại | Phần tử | Không có | «Tài khoản: an.nguyen» · «Nhập lại tên tài khoản» | Màn | Giữ Figma | 2026-10-16 | Đã chốt 16/10. (theo gợi ý; 3 dòng máy) |
| `d05` | 1.3 Tenant not found · 1.4 · 2.1 Temp expired | Màn thông báo có thêm tiêu đề | Phần tử | Chỉ có câu báo | «Không tìm thấy doanh nghiệp» · «Không dùng được Web» · «Mật khẩu tạm hết hạn» | Màn | Giữ Figma | 2026-10-16 | Đã chốt 16/10. (theo gợi ý; 12 dòng máy) |
| `d06` | 3.5 | 3.5 thêm tiêu đề «Link đã hết hạn» và nút «Quay về đăng nhập» | Phần tử | Không có | Tiêu đề + đường kẻ + «Quay về đăng nhập» | Màn | Giữ Figma | 2026-10-16 | Bạn đã chốt nút «Quay về đăng nhập». Riêng tiêu đề là mình tự thêm theo mẫu bạn chọn ở 1.4, CHƯA hỏi bạn. Chọn Theo prototype nếu muốn bỏ tiêu đề. (theo gợi ý; 4 dòng máy) |
| `d07` | 1.5 · 2.1 Confirm leave | Đổi chữ nút huỷ | Chữ nút | «Huỷ» | 1.5: «Quay về đăng nhập» · 2.1 hộp xác nhận: «Bỏ thay đổi» | Màn | Giữ Figma | 2026-10-16 | Đã chốt 16/10. (theo gợi ý; 5 dòng máy) |
| `d08` | 1.3 Password created | «Đã đặt mật khẩu mới» dùng banner thành công | Kiểu banner | Banner thông tin | Banner thành công | Màn | Giữ Figma | 2026-10-16 | Đã chốt 16/10. (theo gợi ý; 11 dòng máy) |
| `x01` | 3.2 | 3.2 có state «Gửi lại sau 42 giây» mà prototype không có | State | Không có: đang chờ thì đi thẳng sang 3.3 | Nút xám «Gửi lại sau 42 giây» | Màn — 3.2 Cooldown | Giữ Figma | 2026-10-16 | Theo prototype = xoá frame này và nối thẳng 3.2 → 3.3 khi đang chờ. (theo gợi ý; 3 dòng máy) |
| `n01` | 1.3 · 2.1 · 3.2 Network error, 1.3 Session expired | Toast lỗi: mất icon bên trái, thêm nút đóng | Icon · nút đóng · cao · lề trái chữ | Icon cảnh báo bên trái · không nút đóng · cao 44 · chữ cách mép 44 | Không icon · nút X bên phải · cao 56 · chữ cách mép 13 | Component Toast (innvie · Components) | Theo prototype | 2026-10-16 | Icon giúp nhận ra đây là lỗi. Nút X thì tuỳ: toast tự tắt sau vài giây. (theo gợi ý; 15 dòng máy) |
| `n02` | 1.3 Session expired | Toast «Phiên đã hết hạn» thành toast lỗi đỏ | Nền · icon · canh lề | Nền tối (toast thông báo) · icon dấu tích · chữ canh giữa | Nền đỏ #aa071e (toast lỗi) · không icon · canh trái | Component Toast | Theo prototype | 2026-10-16 | Hết phiên là thông báo, không phải lỗi người dùng gây ra. Prototype dùng toast thường. (theo gợi ý; 3 dòng máy) |
| `n03` | 1.3 · 2.1 · 3.2 Network error, 1.3 Session expired | Toast hiện ở góc trên phải thay vì giữa đáy màn | Vị trí | Giữa, sát đáy màn | Góc trên bên phải | Màn — các state có toast | Theo prototype | 2026-10-16 | Chọn Giữ Figma nếu quy ước chung của dự án là toast góc trên phải; khi đó cần ghi vào design.md. (theo gợi ý; 4 dòng máy) |
| `n04` | 1.5 Search, No search results | Ô tìm chi nhánh: icon kính lúp to và đậm hơn | Icon kính lúp: cỡ · màu | 14×14 · xám #737373 | 16×16 · đen #171717 | Component TextInput (innvie · Components) | Theo prototype | 2026-10-16 | Icon gợi ý trong ô nên nhạt hơn chữ gõ. (theo gợi ý; 6 dòng máy) |
| `n05` | 1.5 No search results | «Không có chi nhánh phù hợp» đậm và đen hơn | Độ đậm · màu chữ · màu icon | 400 · #737373 · icon xám | 500 · #171717 · icon đen | Component EmptyState | Theo prototype | 2026-10-16 | Trạng thái rỗng là thông tin phụ, prototype để xám. (theo gợi ý; 4 dòng máy) |
| `n06` | 1.5 Search, No search results | Hộp chọn chi nhánh mất bóng đổ | Bóng đổ | 0 4 6 0 #0000001a | Không có | Component Dialog (Astryx · Library) | Theo prototype | 2026-10-16 | Máy chỉ bắt được ở 2 state; các state khác bóng nằm ở lớp ngoài nên không ghép được — sửa ở component thì đủ cả. (theo gợi ý; 2 dòng máy) |
| `n07` | 2.1 Confirm leave | Hộp «Huỷ bản ghi?»: 2 nút xếp dọc | Xếp nút | Cùng hàng (Huỷ · Tiếp tục chỉnh sửa) | Xếp dọc | Component AlertDialog | Theo prototype | 2026-10-16 | Màn web rộng, prototype xếp nút cùng hàng như các hộp xác nhận khác. (theo gợi ý; 1 dòng máy) |
| `n08` | 2.1 Field error | Lỗi mật khẩu: Figma bỏ dòng gợi ý chính sách | Gợi ý dưới ô khi có lỗi | Vẫn hiện «Ít nhất 8 ký tự…» dưới câu lỗi | Chỉ còn câu lỗi | Màn — 2.1 Field error | Giữ Figma | 2026-10-16 | Câu lỗi đã nói đủ chính sách, hiện thêm gợi ý là lặp chữ. (theo gợi ý; 1 dòng máy) |
| `n10` | 1.3 Tenant not found | Sai đường dẫn khách: icon cấm thay icon cảnh báo | Icon | circle-alert (cảnh báo) | ban (cấm) | Component Thông báo trạng thái | Giữ Figma | 2026-10-16 | Icon cấm đang dùng cho 1.4 «không được dùng kênh này»; sai đường dẫn không phải bị cấm. (bạn chọn; 2 dòng máy) |
| `n11` | 3.5 | 3.5: hai nút sát nhau hơn | «Gửi lại link» → «Liên hệ IT» | 31 | 20 | Màn — 3.5 | Theo prototype | 2026-10-16 |  (theo gợi ý; 1 dòng máy) |
| `n12` | 3.3 Cooldown | Nút «Gửi lại sau 42 giây» mất icon | Icon trên nút khi đang chờ | Giữ icon refresh-cw | Không icon | Component Button | Theo prototype | 2026-10-16 | Giữ icon để nút không đổi hình khi hết thời gian chờ. (theo gợi ý; 1 dòng máy) |
| `d09` | 1.3 · 2.1 · 3.2 Submitting | Nút đang gửi chỉ hiện spinner, ẩn chữ | Nhãn khi đang gửi | Spinner + «Đang đăng nhập…» / «Đang lưu…» / «Đang gửi…» | Chỉ spinner | Component Button (Loading) | Giữ Figma | 2026-10-16 | Đã chốt 16/10: nút Loading giữ spinner theo DS. (theo gợi ý; 6 dòng máy) |
| `n13` | 1.3 · 2.1 — mọi ô mật khẩu | Icon con mắt trong ô mật khẩu đen và to hơn | Màu · kích thước | Xám #737373 · 20×20 | Đen #171717 · vùng bấm 28×28 (cỡ hình vẽ bên trong cần soi bằng mắt) | Component Ô mật khẩu (innvie · Components) | Theo prototype | 2026-10-16 | Icon phụ trong ô nên nhạt hơn chữ gõ, như icon kính lúp ở n04. (theo gợi ý; 32 dòng máy) |
| `n14` | 1.3 · 2.1 · 3.2 khi có lỗi | Ô có lỗi: Figma thêm icon cảnh báo trong ô | Icon trong ô khi lỗi | Không có (chỉ viền đỏ + câu lỗi) | Có icon cảnh báo ở mép phải ô | Component TextInput (innvie · Components) | Giữ Figma | 2026-10-16 | Icon giúp người không phân biệt màu vẫn thấy ô lỗi. Chọn Theo prototype nếu muốn giữ ô gọn như bản đã duyệt. (theo gợi ý; 4 dòng máy) |
| `x02` | — | 1.5 Switch branch — nền Home | — | — | — | — | Bỏ qua | 2026-10-16 | Home trên Figma còn là màn giữ chỗ; đo lại khi vẽ Home (BL-173) (119 dòng máy) |

## 2. Khoá máy

| Khoá | Dòng | Màn | Phần tử | Thuộc tính |
|---|---|---|---|---|
| `k-cd8183fc` | c01 | 1.3 · web | Tên tài khoản — dấu * | Màu |
| `k-80a96581` | c01 | 1.3 · web | Mật khẩu — dấu * | Màu |
| `k-e413a0e5` | c04 | 1.3 · web | Ghi nhớ đăng nhập | Độ đậm |
| `k-6bbcd9ba` | c02 | 1.3 · web | Quên mật khẩu | Độ đậm |
| `k-2a051517` | c02 | 1.3 · web | Quên mật khẩu | Màu chữ |
| `k-838b80e3` | c02 | 1.3 · web | Quên mật khẩu | Gạch chân |
| `k-9f95636e` | s01 | 1.3 · web | Khung «Đăng nhập» +9 chữ | Cao |
| `k-bbe96e7d` | s01 | 1.3 · web | Khung «Đăng nhập» +9 chữ | Viền |
| `k-a6550de0` | s01 | 1.3 · web | Khung «Đăng nhập» +9 chữ | Lề trong trái |
| `k-8b6a32bd` | s01 | 1.3 · web | Khung «Đăng nhập» +9 chữ | Lề trong trên |
| `k-5b3cbff9` | s03 | 1.3 · web | «Tên tài khoản hoặc em…» → «Mật khẩu» | Khoảng cách dọc |
| `k-a59ec510` | s03 | 1.3 · web | «Mật khẩu» → «Ghi nhớ đăng nhập» | Khoảng cách dọc |
| `k-8f4aa283` | s03 | 1.3 · web | «Ghi nhớ đăng nhập» → «Quên mật khẩu» | Khoảng cách ngang |
| `k-39d6f994` | s03 | 1.3 · web | «Quên mật khẩu» → «Đăng nhập» | Khoảng cách dọc |
| `k-063b503e` | s04 | 1.3 · web | Chưa có tài khoản? Liên hệ quản trị viê… | Canh lề |
| `k-f7bd9316` | c03 | 1.3 · web | Checkbox #1 | Kích thước |
| `k-838b2028` | c03 | 1.3 · web | Checkbox #1 | Bo góc |
| `k-a77a42df` | n13 | 1.3 · web | Icon eye cạnh «Mật khẩu» | Kích thước |
| `k-7c2986f5` | n13 | 1.3 · web | Icon eye cạnh «Mật khẩu» | Màu |
| `k-67112c85` | s02 | 1.3 · web · Field error | Đăng nhập | Cỡ chữ |
| `k-29e54201` | s02 | 1.3 · web · Field error | Đăng nhập | Line-height |
| `k-158b2a2a` | c01 | 1.3 · web · Field error | Tên tài khoản — dấu * | Màu |
| `k-b3109fcf` | c07 | 1.3 · web · Field error | an.nguyen | Line-height |
| `k-731e2e14` | c01 | 1.3 · web · Field error | Mật khẩu — dấu * | Màu |
| `k-3de26864` | c06 | 1.3 · web · Field error | Tên tài khoản hoặc mật khẩu không đúng.… | Line-height |
| `k-0c1908d3` | c06 | 1.3 · web · Field error | Tên tài khoản hoặc mật khẩu không đúng.… | Màu chữ |
| `k-023d6f3a` | c04 | 1.3 · web · Field error | Ghi nhớ đăng nhập | Độ đậm |
| `k-3550aa84` | c02 | 1.3 · web · Field error | Quên mật khẩu | Độ đậm |
| `k-4ab1d0ed` | c02 | 1.3 · web · Field error | Quên mật khẩu | Màu chữ |
| `k-40f8c421` | c02 | 1.3 · web · Field error | Quên mật khẩu | Gạch chân |
| `k-3a83138d` | s01 | 1.3 · web · Field error | Khung «Đăng nhập» +10 chữ | Cao |
| `k-b1630179` | s01 | 1.3 · web · Field error | Khung «Đăng nhập» +10 chữ | Viền |
| `k-82f29b04` | s01 | 1.3 · web · Field error | Khung «Đăng nhập» +10 chữ | Lề trong trái |
| `k-bff9a2c4` | s01 | 1.3 · web · Field error | Khung «Đăng nhập» +10 chữ | Lề trong trên |
| `k-f97ac6ae` | s03 | 1.3 · web · Field error | «an.nguyen» → «Mật khẩu» | Khoảng cách dọc |
| `k-bf379aee` | s03 | 1.3 · web · Field error | «Mật khẩu» → «Tên tài khoản hoặc mậ…» | Khoảng cách dọc |
| `k-d2fa1e79` | s03 | 1.3 · web · Field error | «Tên tài khoản hoặc mậ…» → «Ghi nhớ đăng nhập» | Khoảng cách dọc |
| `k-bd117fc3` | s03 | 1.3 · web · Field error | «Ghi nhớ đăng nhập» → «Quên mật khẩu» | Khoảng cách ngang |
| `k-f275abe8` | s03 | 1.3 · web · Field error | «Quên mật khẩu» → «Đăng nhập» | Khoảng cách dọc |
| `k-35f78246` | s04 | 1.3 · web · Field error | Chưa có tài khoản? Liên hệ quản trị viê… | Canh lề |
| `k-8d31ebf3` | c03 | 1.3 · web · Field error | Checkbox #1 | Kích thước |
| `k-4dc38939` | c03 | 1.3 · web · Field error | Checkbox #1 | Bo góc |
| `k-46f2203c` | n14 | 1.3 · web · Field error | Icon Icon | Phần tử |
| `k-e3f884e5` | n13 | 1.3 · web · Field error | Icon eye cạnh «Mật khẩu» | Kích thước |
| `k-6c824c9d` | n13 | 1.3 · web · Field error | Icon eye cạnh «Mật khẩu» | Màu |
| `k-645e7c71` | d09 | 1.3 · web · Submitting | Đang đăng nhập… | Phần tử |
| `k-5de4814d` | s02 | 1.3 · web · Submitting | Đăng nhập | Cỡ chữ |
| `k-78d69cfb` | s02 | 1.3 · web · Submitting | Đăng nhập | Line-height |
| `k-581bf457` | s07 | 1.3 · web · Submitting | Tên tài khoản | Màu chữ |
| `k-6569ffb0` | s07 | 1.3 · web · Submitting | Tên tài khoản — dấu * | Màu |
| `k-35052019` | c07 | 1.3 · web · Submitting | an.nguyen | Line-height |
| `k-a46e1dcf` | s07 | 1.3 · web · Submitting | Mật khẩu | Màu chữ |
| `k-f2b67731` | s07 | 1.3 · web · Submitting | Mật khẩu — dấu * | Màu |
| `k-8a66d708` | c07 | 1.3 · web · Submitting | •••••••••• | Line-height |
| `k-2098d668` | c04 | 1.3 · web · Submitting | Ghi nhớ đăng nhập | Độ đậm |
| `k-361e60c5` | c04 | 1.3 · web · Submitting | Ghi nhớ đăng nhập | Màu chữ |
| `k-7a0c0217` | c02 | 1.3 · web · Submitting | Quên mật khẩu | Độ đậm |
| `k-404a08b7` | c02 | 1.3 · web · Submitting | Quên mật khẩu | Màu chữ |
| `k-d3c3343e` | c02 | 1.3 · web · Submitting | Quên mật khẩu | Gạch chân |
| `k-3bb2b480` | s01 | 1.3 · web · Submitting | Khung «Đăng nhập» +8 chữ | Cao |
| `k-718d1218` | s01 | 1.3 · web · Submitting | Khung «Đăng nhập» +8 chữ | Viền |
| `k-06306955` | s01 | 1.3 · web · Submitting | Khung «Đăng nhập» +8 chữ | Lề trong trái |
| `k-51835211` | s01 | 1.3 · web · Submitting | Khung «Đăng nhập» +8 chữ | Lề trong trên |
| `k-dd0e87b7` | s03 | 1.3 · web · Submitting | «an.nguyen» → «Mật khẩu» | Khoảng cách dọc |
| `k-b9e3c055` | s03 | 1.3 · web · Submitting | «••••••••••» → «Ghi nhớ đăng nhập» | Khoảng cách dọc |
| `k-9bcb010f` | s03 | 1.3 · web · Submitting | «Ghi nhớ đăng nhập» → «Quên mật khẩu» | Khoảng cách ngang |
| `k-b58483c1` | s03 | 1.3 · web · Submitting | «Quên mật khẩu» → «Chưa có tài khoản? Li…» | Khoảng cách dọc |
| `k-2824887a` | s04 | 1.3 · web · Submitting | Chưa có tài khoản? Liên hệ quản trị viê… | Canh lề |
| `k-b4847978` | c03 | 1.3 · web · Submitting | Checkbox #1 | Kích thước |
| `k-b7e874de` | c03 | 1.3 · web · Submitting | Checkbox #1 | Bo góc |
| `k-db86774d` | d09 | 1.3 · web · Submitting | Icon loader cạnh «Chưa có tài khoản? Liên…» | Kích thước |
| `k-ebca173b` | n13 | 1.3 · web · Submitting | Icon eye cạnh «••••••••••» | Kích thước |
| `k-c70bedc9` | n13 | 1.3 · web · Submitting | Icon eye cạnh «••••••••••» | Màu |
| `k-3cbd4638` | s02 | 1.3 · web · Network error | Đăng nhập | Cỡ chữ |
| `k-35bfec59` | s02 | 1.3 · web · Network error | Đăng nhập | Line-height |
| `k-518ff7c4` | c01 | 1.3 · web · Network error | Tên tài khoản — dấu * | Màu |
| `k-17a10fe4` | c07 | 1.3 · web · Network error | an.nguyen | Line-height |
| `k-98a32ae2` | c01 | 1.3 · web · Network error | Mật khẩu — dấu * | Màu |
| `k-352277b3` | c07 | 1.3 · web · Network error | •••••••••• | Line-height |
| `k-2d202ae4` | c04 | 1.3 · web · Network error | Ghi nhớ đăng nhập | Độ đậm |
| `k-06b8bf8a` | c02 | 1.3 · web · Network error | Quên mật khẩu | Độ đậm |
| `k-31f0b85b` | c02 | 1.3 · web · Network error | Quên mật khẩu | Màu chữ |
| `k-2355a55c` | c02 | 1.3 · web · Network error | Quên mật khẩu | Gạch chân |
| `k-10363c68` | s01 | 1.3 · web · Network error | Khung «Đăng nhập» +9 chữ | Cao |
| `k-86c74073` | s01 | 1.3 · web · Network error | Khung «Đăng nhập» +9 chữ | Viền |
| `k-3314c64c` | s01 | 1.3 · web · Network error | Khung «Đăng nhập» +9 chữ | Lề trong trái |
| `k-f951d974` | s01 | 1.3 · web · Network error | Khung «Đăng nhập» +9 chữ | Lề trong trên |
| `k-b2cd420d` | n01 | 1.3 · web · Network error | Khung «Mất kết nối. Kiểm tra mạng …» | Cao |
| `k-8cffb060` | n01 | 1.3 · web · Network error | Khung «Mất kết nối. Kiểm tra mạng …» | Lề trong trái |
| `k-00532171` | s03 | 1.3 · web · Network error | «an.nguyen» → «Mật khẩu» | Khoảng cách dọc |
| `k-77415fa4` | s03 | 1.3 · web · Network error | «••••••••••» → «Ghi nhớ đăng nhập» | Khoảng cách dọc |
| `k-5f190e1b` | s03 | 1.3 · web · Network error | «Ghi nhớ đăng nhập» → «Quên mật khẩu» | Khoảng cách ngang |
| `k-243c5b16` | s03 | 1.3 · web · Network error | «Quên mật khẩu» → «Đăng nhập» | Khoảng cách dọc |
| `k-817eb63f` | n03 | 1.3 · web · Network error | «Chưa có tài khoản? Li…» → «Mất kết nối. Kiểm tra…» | Khoảng cách dọc |
| `k-9e4097ee` | s04 | 1.3 · web · Network error | Chưa có tài khoản? Liên hệ quản trị viê… | Canh lề |
| `k-c1a122d0` | c03 | 1.3 · web · Network error | Checkbox #1 | Kích thước |
| `k-c50d4644` | c03 | 1.3 · web · Network error | Checkbox #1 | Bo góc |
| `k-a30deb3c` | n01 | 1.3 · web · Network error | Icon circle-alert cạnh «Mất kết nối. Kiểm tra m…» | Phần tử |
| `k-cd6f037d` | n01 | 1.3 · web · Network error | Icon icon/x | Phần tử |
| `k-f63db9f2` | n13 | 1.3 · web · Network error | Icon eye cạnh «••••••••••» | Kích thước |
| `k-cecc053a` | n13 | 1.3 · web · Network error | Icon eye cạnh «••••••••••» | Màu |
| `k-265355ec` | s02 | 1.3 · web · Session expired | Đăng nhập | Cỡ chữ |
| `k-9d6e7745` | s02 | 1.3 · web · Session expired | Đăng nhập | Line-height |
| `k-2d0a2d2a` | c01 | 1.3 · web · Session expired | Tên tài khoản — dấu * | Màu |
| `k-d2d47e20` | c01 | 1.3 · web · Session expired | Mật khẩu — dấu * | Màu |
| `k-8078be6e` | c04 | 1.3 · web · Session expired | Ghi nhớ đăng nhập | Độ đậm |
| `k-6d80016f` | c02 | 1.3 · web · Session expired | Quên mật khẩu | Độ đậm |
| `k-25a3c724` | c02 | 1.3 · web · Session expired | Quên mật khẩu | Màu chữ |
| `k-9b6d8cf0` | c02 | 1.3 · web · Session expired | Quên mật khẩu | Gạch chân |
| `k-8e59598c` | s01 | 1.3 · web · Session expired | Khung «Đăng nhập» +9 chữ | Cao |
| `k-e95c6071` | s01 | 1.3 · web · Session expired | Khung «Đăng nhập» +9 chữ | Viền |
| `k-280504ea` | s01 | 1.3 · web · Session expired | Khung «Đăng nhập» +9 chữ | Lề trong trái |
| `k-5da81172` | s01 | 1.3 · web · Session expired | Khung «Đăng nhập» +9 chữ | Lề trong trên |
| `k-2d271265` | n01 | 1.3 · web · Session expired | Khung «Phiên làm việc đã hết hạn. …» | Cao |
| `k-aec1e63e` | n02 | 1.3 · web · Session expired | Khung «Phiên làm việc đã hết hạn. …» | Nền |
| `k-53e7b498` | n01 | 1.3 · web · Session expired | Khung «Phiên làm việc đã hết hạn. …» | Lề trong trái |
| `k-d58d6ca5` | s03 | 1.3 · web · Session expired | «Tên tài khoản hoặc em…» → «Mật khẩu» | Khoảng cách dọc |
| `k-040bcc51` | s03 | 1.3 · web · Session expired | «Mật khẩu» → «Ghi nhớ đăng nhập» | Khoảng cách dọc |
| `k-e5d9ad8a` | s03 | 1.3 · web · Session expired | «Ghi nhớ đăng nhập» → «Quên mật khẩu» | Khoảng cách ngang |
| `k-1d2b50f8` | s03 | 1.3 · web · Session expired | «Quên mật khẩu» → «Đăng nhập» | Khoảng cách dọc |
| `k-39466028` | n03 | 1.3 · web · Session expired | «Chưa có tài khoản? Li…» → «Phiên làm việc đã hết…» | Khoảng cách dọc |
| `k-847cc4c4` | s04 | 1.3 · web · Session expired | Chưa có tài khoản? Liên hệ quản trị viê… | Canh lề |
| `k-afbe9159` | n02 | 1.3 · web · Session expired | Phiên làm việc đã hết hạn. Đăng nhập lạ… | Canh lề |
| `k-dc28df49` | c03 | 1.3 · web · Session expired | Checkbox #1 | Kích thước |
| `k-a2c6cb18` | c03 | 1.3 · web · Session expired | Checkbox #1 | Bo góc |
| `k-872c3e86` | n02 | 1.3 · web · Session expired | Icon circle-check cạnh «Phiên làm việc đã hết h…» | Phần tử |
| `k-a1cba46d` | n01 | 1.3 · web · Session expired | Icon icon/x | Phần tử |
| `k-f17f3ce6` | n13 | 1.3 · web · Session expired | Icon eye cạnh «Mật khẩu» | Kích thước |
| `k-359cc3b6` | n13 | 1.3 · web · Session expired | Icon eye cạnh «Mật khẩu» | Màu |
| `k-7bd57228` | d08 | 1.3 · web · Password created | Đã đặt mật khẩu mới. Đăng nhập lại bằng… | Độ đậm |
| `k-20e35440` | d08 | 1.3 · web · Password created | Đã đặt mật khẩu mới. Đăng nhập lại bằng… | Màu chữ |
| `k-f083bdd6` | s02 | 1.3 · web · Password created | Đăng nhập | Cỡ chữ |
| `k-cad40a7b` | s02 | 1.3 · web · Password created | Đăng nhập | Line-height |
| `k-f7754935` | c01 | 1.3 · web · Password created | Tên tài khoản — dấu * | Màu |
| `k-ad82f4fa` | c01 | 1.3 · web · Password created | Mật khẩu — dấu * | Màu |
| `k-cc08b35e` | c04 | 1.3 · web · Password created | Ghi nhớ đăng nhập | Độ đậm |
| `k-84d40d91` | c02 | 1.3 · web · Password created | Quên mật khẩu | Độ đậm |
| `k-c89d1829` | c02 | 1.3 · web · Password created | Quên mật khẩu | Màu chữ |
| `k-95fb7691` | c02 | 1.3 · web · Password created | Quên mật khẩu | Gạch chân |
| `k-ffdb6061` | d08 | 1.3 · web · Password created | Khung «Đã đặt mật khẩu mới. Đăng n…» +10 chữ | Cao |
| `k-7589f55b` | d08 | 1.3 · web · Password created | Khung «Đã đặt mật khẩu mới. Đăng n…» +10 chữ | Viền |
| `k-25df25b7` | d08 | 1.3 · web · Password created | Khung «Đã đặt mật khẩu mới. Đăng n…» +10 chữ | Lề trong trái |
| `k-b4f4a5f2` | d08 | 1.3 · web · Password created | Khung «Đã đặt mật khẩu mới. Đăng n…» +10 chữ | Lề trong trên |
| `k-897495d5` | d08 | 1.3 · web · Password created | Khung «Đã đặt mật khẩu mới. Đăng n…» | Nền |
| `k-31af06d1` | d08 | 1.3 · web · Password created | Khung «Đã đặt mật khẩu mới. Đăng n…» | Lề trong trái |
| `k-8d4bd248` | d08 | 1.3 · web · Password created | «Đã đặt mật khẩu mới. …» → «Đăng nhập» | Khoảng cách dọc |
| `k-fd99eb1c` | s03 | 1.3 · web · Password created | «Nhập thông tin tài kh…» → «Tên tài khoản» | Khoảng cách dọc |
| `k-c9ae01d1` | s03 | 1.3 · web · Password created | «Tên tài khoản hoặc em…» → «Mật khẩu» | Khoảng cách dọc |
| `k-9edc494c` | s03 | 1.3 · web · Password created | «Mật khẩu» → «Ghi nhớ đăng nhập» | Khoảng cách dọc |
| `k-b2e222cb` | s03 | 1.3 · web · Password created | «Ghi nhớ đăng nhập» → «Quên mật khẩu» | Khoảng cách ngang |
| `k-3b6d8014` | s03 | 1.3 · web · Password created | «Quên mật khẩu» → «Đăng nhập» | Khoảng cách dọc |
| `k-9536834d` | s04 | 1.3 · web · Password created | Chưa có tài khoản? Liên hệ quản trị viê… | Canh lề |
| `k-2467995f` | c03 | 1.3 · web · Password created | Checkbox #1 | Kích thước |
| `k-a30a5047` | c03 | 1.3 · web · Password created | Checkbox #1 | Bo góc |
| `k-2db511de` | d08 | 1.3 · web · Password created | Icon info cạnh «Đã đặt mật khẩu mới. Đă…» | Kích thước |
| `k-a2475772` | d08 | 1.3 · web · Password created | Icon info cạnh «Đã đặt mật khẩu mới. Đă…» | Màu |
| `k-6901360b` | n13 | 1.3 · web · Password created | Icon eye cạnh «Mật khẩu» | Kích thước |
| `k-75517641` | n13 | 1.3 · web · Password created | Icon eye cạnh «Mật khẩu» | Màu |
| `k-bc09ee72` | d05 | 1.3 · web · Tenant not found | Không tìm thấy doanh nghiệp. Kiểm tra l… | Phần tử |
| `k-5d80e367` | d05 | 1.3 · web · Tenant not found | Không tìm thấy doanh nghiệp | Phần tử |
| `k-97c795ae` | d05 | 1.3 · web · Tenant not found | Kiểm tra lại đường dẫn hoặc liên hệ quả… | Phần tử |
| `k-f552a29c` | n10 | 1.3 · web · Tenant not found | Icon circle-alert | Phần tử |
| `k-eaecc263` | n10 | 1.3 · web · Tenant not found | Icon icon/ban | Phần tử |
| `k-ed6eb56c` | d05 | 1.3 · web · Tenant not found | Ảnh/logo | Số lượng |
| `k-3cc29d2b` | d05 | 1.4 · web | Không dùng được Web | Phần tử |
| `k-2d6469c9` | s01 | 1.4 · web | Khung «Tài khoản này không được dù…» +1 chữ | Cao |
| `k-3d57026d` | s01 | 1.4 · web | Khung «Tài khoản này không được dù…» +1 chữ | Viền |
| `k-262180be` | s01 | 1.4 · web | Khung «Tài khoản này không được dù…» +1 chữ | Lề trong trái |
| `k-0c3dd7db` | s01 | 1.4 · web | Khung «Tài khoản này không được dù…» +1 chữ | Lề trong trên |
| `k-608a0e7d` | d07 | 1.5 · web | Huỷ | Phần tử |
| `k-6dd1c8ed` | s08 | 1.5 · web | Nhập thông tin tài khoản để tiếp tục. | Phần tử |
| `k-f9d5c21a` | s08 | 1.5 · web | Tên tài khoản * | Phần tử |
| `k-5bb8858d` | s08 | 1.5 · web | Tên tài khoản hoặc email | Phần tử |
| `k-ee079b97` | s08 | 1.5 · web | Mật khẩu * | Phần tử |
| `k-b1c2db8e` | s08 | 1.5 · web | Mật khẩu | Phần tử |
| `k-a5c50844` | s08 | 1.5 · web | Ghi nhớ đăng nhập | Phần tử |
| `k-a6dffe27` | s08 | 1.5 · web | Quên mật khẩu | Phần tử |
| `k-2cbf7ad3` | s08 | 1.5 · web | Đăng nhập | Phần tử |
| `k-0ce3048f` | s08 | 1.5 · web | Chưa có tài khoản? Liên hệ quản trị viê… | Phần tử |
| `k-c1f0053c` | s08 | 1.5 · web | Quay về đăng nhập | Phần tử |
| `k-44f6c927` | c11 | 1.5 · web | Chọn chi nhánh | Màu chữ |
| `k-5b868b6e` | s08 | 1.5 · web | Đăng nhập | Cỡ chữ |
| `k-8db08b5b` | s08 | 1.5 · web | Đăng nhập | Line-height |
| `k-c3d95cb8` | c11 | 1.5 · web | Khung «Chọn chi nhánh» +11 chữ | Rộng |
| `k-f1027894` | c11 | 1.5 · web | Khung «Chọn chi nhánh» +11 chữ | Cao |
| `k-12eb4df4` | c11 | 1.5 · web | Khung «Chọn chi nhánh» +11 chữ | Lề trong trái |
| `k-fc133c26` | c11 | 1.5 · web | Khung «Chọn chi nhánh» +11 chữ | Lề trong trên |
| `k-23efe24f` | c10 | 1.5 · web | Khung «Delta Hà Nội» | Rộng |
| `k-6b47b1c6` | s08 | 1.5 · web | Khung «Delta Hà Nội» | Cao |
| `k-e8c78fe7` | s08 | 1.5 · web | Khung «Delta Hà Nội» | Bo góc |
| `k-7c2f4a39` | s08 | 1.5 · web | Khung «Delta Hà Nội» | Nền |
| `k-2340d690` | s08 | 1.5 · web | Khung «Delta Hà Nội» | Viền |
| `k-a87449c0` | s08 | 1.5 · web | Khung «Delta Hà Nội» | Lề trong trái |
| `k-04e8521b` | c10 | 1.5 · web | Khung «Delta Hải Phòng» +1 chữ | Rộng |
| `k-a67aa40e` | c10 | 1.5 · web | Khung «Delta Hải Phòng» +1 chữ | Cao |
| `k-3fd36fa7` | c10 | 1.5 · web | Khung «Delta Hải Phòng» +1 chữ | Nền |
| `k-5e046f17` | c10 | 1.5 · web | Khung «Delta Hải Phòng» +1 chữ | Viền |
| `k-09c34fdb` | c10 | 1.5 · web | Khung «Delta Hải Phòng» +1 chữ | Lề trong trái |
| `k-84ccada1` | c10 | 1.5 · web | Khung «Delta Hà Nội» +1 chữ | Rộng |
| `k-129b1ac7` | c10 | 1.5 · web | Khung «Delta Hà Nội» +1 chữ | Cao |
| `k-1563cdd1` | c10 | 1.5 · web | Khung «Delta Hà Nội» +1 chữ | Nền |
| `k-38c91468` | c10 | 1.5 · web | Khung «Delta Hà Nội» +1 chữ | Viền |
| `k-ade112e5` | c10 | 1.5 · web | Khung «Delta Hà Nội» +1 chữ | Lề trong trái |
| `k-703018fe` | c10 | 1.5 · web | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Rộng |
| `k-9ebbe6bf` | c10 | 1.5 · web | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Cao |
| `k-052c7744` | c10 | 1.5 · web | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Nền |
| `k-e6781d4a` | c10 | 1.5 · web | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Viền |
| `k-03cf3f3d` | c10 | 1.5 · web | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Lề trong trái |
| `k-b0754494` | c11 | 1.5 · web | «Chọn chi nhánh» → «Công ty mẹ — Delta Qu…» | Khoảng cách dọc |
| `k-db8bccff` | c10 | 1.5 · web | «Công ty mẹ — Delta Qu…» → «Toàn bộ 3 chi nhánh» | Khoảng cách dọc |
| `k-bbe8e103` | c10 | 1.5 · web | «Toàn bộ 3 chi nhánh» → «Hoặc chọn chi nhánh c…» | Khoảng cách dọc |
| `k-d71de420` | c10 | 1.5 · web | «Hoặc chọn chi nhánh c…» → «Đăng nhập» | Khoảng cách dọc |
| `k-1f017a77` | c10 | 1.5 · web | «Đăng nhập» → «Delta Hải Phòng» | Xếp hàng |
| `k-f5b2078c` | c10 | 1.5 · web | «Delta Hải Phòng» → «Hải Phòng» | Khoảng cách dọc |
| `k-8f31ff10` | c10 | 1.5 · web | «Delta Hà Nội» → «Hà Nội» | Khoảng cách dọc |
| `k-a2c63d16` | c10 | 1.5 · web | «Delta TP. Hồ Chí Minh» → «TP. Hồ Chí Minh» | Khoảng cách dọc |
| `k-b373167d` | c10 | 1.5 · web | «TP. Hồ Chí Minh» → «Chọn» | Khoảng cách dọc |
| `k-dbfe7d19` | c05 | 1.5 · web | Checkbox #1 | Kích thước |
| `k-67d1a4e6` | c05 | 1.5 · web | Checkbox #1 | Bo góc |
| `k-4b998a94` | c05 | 1.5 · web | Checkbox #2 | Kích thước |
| `k-95e310a4` | c05 | 1.5 · web | Checkbox #2 | Bo góc |
| `k-79ca6a61` | c05 | 1.5 · web | Checkbox #3 | Kích thước |
| `k-0f53f1da` | c05 | 1.5 · web | Checkbox #3 | Bo góc |
| `k-c46965a8` | c03 | 1.5 · web | Checkbox #4 | Kích thước |
| `k-45d107f1` | c03 | 1.5 · web | Checkbox #4 | Bo góc |
| `k-715ada54` | c11 | 1.5 · web | Đường kẻ ngang | Số lượng |
| `k-af0cf08f` | s08 | 1.5 · web | Icon Button | Phần tử |
| `k-0f4d1537` | c11 | 1.5 · web | Icon search cạnh «Chọn chi nhánh» | Kích thước |
| `k-17a81959` | c10 | 1.5 · web · Search | Delta Hải Phòng | Phần tử |
| `k-315cc7ea` | c10 | 1.5 · web · Search | Hải Phòng | Phần tử |
| `k-e1349cfb` | d07 | 1.5 · web · Search | Huỷ | Phần tử |
| `k-af42abe8` | s08 | 1.5 · web · Search | Nhập thông tin tài khoản để tiếp tục. | Phần tử |
| `k-8bafa5e4` | s08 | 1.5 · web · Search | Tên tài khoản * | Phần tử |
| `k-e1f7417a` | s08 | 1.5 · web · Search | Tên tài khoản hoặc email | Phần tử |
| `k-3148a516` | s08 | 1.5 · web · Search | Mật khẩu * | Phần tử |
| `k-b9d6d918` | s08 | 1.5 · web · Search | Mật khẩu | Phần tử |
| `k-d9e25adc` | s08 | 1.5 · web · Search | Ghi nhớ đăng nhập | Phần tử |
| `k-ff3c91c2` | s08 | 1.5 · web · Search | Quên mật khẩu | Phần tử |
| `k-1b25e787` | s08 | 1.5 · web · Search | Đăng nhập | Phần tử |
| `k-8dcb523b` | s08 | 1.5 · web · Search | Chưa có tài khoản? Liên hệ quản trị viê… | Phần tử |
| `k-59bb70bf` | s08 | 1.5 · web · Search | Quay về đăng nhập | Phần tử |
| `k-882819d5` | c11 | 1.5 · web · Search | Chọn chi nhánh | Màu chữ |
| `k-5ed2c315` | c07 | 1.5 · web · Search | hà | Line-height |
| `k-16f80561` | s08 | 1.5 · web · Search | Đăng nhập | Cỡ chữ |
| `k-1a05ab06` | s08 | 1.5 · web · Search | Đăng nhập | Line-height |
| `k-57ebb95e` | c11 | 1.5 · web · Search | Khung «Chọn chi nhánh» +5 chữ | Rộng |
| `k-5a92faca` | c11 | 1.5 · web · Search | Khung «Chọn chi nhánh» +5 chữ | Cao |
| `k-97ebfa22` | c11 | 1.5 · web · Search | Khung «Chọn chi nhánh» +5 chữ | Viền |
| `k-2b938a00` | n06 | 1.5 · web · Search | Khung «Chọn chi nhánh» +5 chữ | Bóng đổ |
| `k-6bb92137` | c11 | 1.5 · web · Search | Khung «Chọn chi nhánh» +5 chữ | Lề trong trái |
| `k-30dd496a` | c11 | 1.5 · web · Search | Khung «Chọn chi nhánh» +5 chữ | Lề trong trên |
| `k-af83d73e` | c10 | 1.5 · web · Search | Khung «Hà Nội» | Rộng |
| `k-bcde9b76` | c10 | 1.5 · web · Search | Khung «Hà Nội» | Bo góc |
| `k-94171abe` | c10 | 1.5 · web · Search | Khung «Hà Nội» | Nền |
| `k-417e5e10` | c10 | 1.5 · web · Search | Khung «Hà Nội» | Lề trong trái |
| `k-d113cd04` | n04 | 1.5 · web · Search | Ô nhập «hà» | Rộng |
| `k-b33d24bb` | c10 | 1.5 · web · Search | Khung «Delta Hà Nội» +1 chữ | Rộng |
| `k-1861dfed` | c10 | 1.5 · web · Search | Khung «Delta Hà Nội» +1 chữ | Cao |
| `k-7cdedd3d` | c10 | 1.5 · web · Search | Khung «Delta Hà Nội» +1 chữ | Nền |
| `k-b9e436c4` | c10 | 1.5 · web · Search | Khung «Delta Hà Nội» +1 chữ | Viền |
| `k-99d6b8da` | c11 | 1.5 · web · Search | «Chọn chi nhánh» → «hà» | Khoảng cách dọc |
| `k-187ca6c3` | s08 | 1.5 · web · Search | «hà» → «Đăng nhập» | Khoảng cách dọc |
| `k-6cb0cdbf` | c10 | 1.5 · web · Search | «Đăng nhập» → «Delta Hà Nội» | Khoảng cách dọc |
| `k-90362524` | c10 | 1.5 · web · Search | «Delta Hà Nội» → «Hà Nội» | Khoảng cách dọc |
| `k-203b8001` | c10 | 1.5 · web · Search | «Hà Nội» → «Chọn» | Khoảng cách dọc |
| `k-85a38ee5` | c03 | 1.5 · web · Search | Checkbox #1 | Kích thước |
| `k-2f765cd7` | c03 | 1.5 · web · Search | Checkbox #1 | Bo góc |
| `k-209ed668` | c11 | 1.5 · web · Search | Đường kẻ ngang | Số lượng |
| `k-1a6bcd43` | c11 | 1.5 · web · Search | Icon x cạnh «Chọn chi nhánh» | Phần tử |
| `k-3a8c4861` | c10 | 1.5 · web · Search | Icon map-pin cạnh «Delta Hà Nội» | Phần tử |
| `k-eae8884e` | s08 | 1.5 · web · Search | Icon Button | Phần tử |
| `k-eae8884e` | s08 | 1.5 · web · Search | Icon Button | Phần tử |
| `k-f6944a4f` | s08 | 1.5 · web · Search | Icon Radio / RadioListItem | Phần tử |
| `k-e125c7b5` | n04 | 1.5 · web · Search | Icon search cạnh «hà» | Kích thước |
| `k-ce1eeb5d` | n04 | 1.5 · web · Search | Icon search cạnh «hà» | Màu |
| `k-9d7c751c` | c10 | 1.5 · web · Search | Icon map-pin cạnh «Đăng nhập» | Màu |
| `k-180bdafa` | d07 | 1.5 · web · No search results | Huỷ | Phần tử |
| `k-51dcc35f` | s08 | 1.5 · web · No search results | Nhập thông tin tài khoản để tiếp tục. | Phần tử |
| `k-d211c786` | s08 | 1.5 · web · No search results | Tên tài khoản * | Phần tử |
| `k-2175736d` | s08 | 1.5 · web · No search results | Tên tài khoản hoặc email | Phần tử |
| `k-0284ae38` | s08 | 1.5 · web · No search results | Mật khẩu * | Phần tử |
| `k-791abe8f` | s08 | 1.5 · web · No search results | Mật khẩu | Phần tử |
| `k-f3c2284b` | s08 | 1.5 · web · No search results | Ghi nhớ đăng nhập | Phần tử |
| `k-a853694a` | s08 | 1.5 · web · No search results | Quên mật khẩu | Phần tử |
| `k-b96cdc68` | s08 | 1.5 · web · No search results | Đăng nhập | Phần tử |
| `k-3e04af67` | s08 | 1.5 · web · No search results | Chưa có tài khoản? Liên hệ quản trị viê… | Phần tử |
| `k-eb160ef9` | s08 | 1.5 · web · No search results | Quay về đăng nhập | Phần tử |
| `k-c3bd9230` | c11 | 1.5 · web · No search results | Chọn chi nhánh | Màu chữ |
| `k-b6962c00` | c07 | 1.5 · web · No search results | Đà Nẵng | Line-height |
| `k-2e523cc8` | s08 | 1.5 · web · No search results | Đăng nhập | Cỡ chữ |
| `k-914c5be9` | s08 | 1.5 · web · No search results | Đăng nhập | Line-height |
| `k-facaadfb` | n05 | 1.5 · web · No search results | Không có chi nhánh phù hợp. | Độ đậm |
| `k-1a591435` | n05 | 1.5 · web · No search results | Không có chi nhánh phù hợp. | Màu chữ |
| `k-fc4cd181` | c11 | 1.5 · web · No search results | Khung «Chọn chi nhánh» +4 chữ | Rộng |
| `k-6c8ae559` | c11 | 1.5 · web · No search results | Khung «Chọn chi nhánh» +4 chữ | Cao |
| `k-f91b686e` | c11 | 1.5 · web · No search results | Khung «Chọn chi nhánh» +4 chữ | Viền |
| `k-32b139c0` | n06 | 1.5 · web · No search results | Khung «Chọn chi nhánh» +4 chữ | Bóng đổ |
| `k-c6d46571` | c11 | 1.5 · web · No search results | Khung «Chọn chi nhánh» +4 chữ | Lề trong trái |
| `k-664dcee1` | c11 | 1.5 · web · No search results | Khung «Chọn chi nhánh» +4 chữ | Lề trong trên |
| `k-90072b48` | n04 | 1.5 · web · No search results | Ô nhập «Đà Nẵng» | Rộng |
| `k-6789a9f1` | c11 | 1.5 · web · No search results | «Chọn chi nhánh» → «Đà Nẵng» | Khoảng cách dọc |
| `k-6bd8622d` | s08 | 1.5 · web · No search results | «Đà Nẵng» → «Đăng nhập» | Khoảng cách dọc |
| `k-d08761c3` | s08 | 1.5 · web · No search results | «Đăng nhập» → «Không có chi nhánh ph…» | Khoảng cách dọc |
| `k-4b072a16` | n05 | 1.5 · web · No search results | «Không có chi nhánh ph…» → «Chọn» | Khoảng cách dọc |
| `k-42244581` | c11 | 1.5 · web · No search results | Đường kẻ ngang | Số lượng |
| `k-6bae38ee` | c11 | 1.5 · web · No search results | Icon x cạnh «Chọn chi nhánh» | Phần tử |
| `k-da857a57` | s08 | 1.5 · web · No search results | Icon Button | Phần tử |
| `k-da857a57` | s08 | 1.5 · web · No search results | Icon Button | Phần tử |
| `k-99427a46` | n04 | 1.5 · web · No search results | Icon search cạnh «Đà Nẵng» | Kích thước |
| `k-41902fd7` | n04 | 1.5 · web · No search results | Icon search cạnh «Đà Nẵng» | Màu |
| `k-9db5d44e` | n05 | 1.5 · web · No search results | Icon search cạnh «Không có chi nhánh phù …» | Màu |
| `k-f0f9c80d` | x02 | 1.5 · web · Switch branch | Điều hành vận tải | Phần tử |
| `k-6d1e0480` | x02 | 1.5 · web · Switch branch | Trang chủ | Phần tử |
| `k-4913ee5d` | x02 | 1.5 · web · Switch branch | Vận hành | Phần tử |
| `k-ae9c137a` | x02 | 1.5 · web · Switch branch | Lệnh vận tải | Phần tử |
| `k-b969457b` | x02 | 1.5 · web · Switch branch | Điều phối | Phần tử |
| `k-6d1e0480` | x02 | 1.5 · web · Switch branch | Trang chủ | Phần tử |
| `k-40b9bf58` | x02 | 1.5 · web · Switch branch | Nội dung Trang chủ thuộc tính năng Khôn… | Phần tử |
| `k-df8b7909` | x02 | 1.5 · web · Switch branch | D | Phần tử |
| `k-a45d9043` | x02 | 1.5 · web · Switch branch | Delta | Phần tử |
| `k-c1d3b5a2` | x02 | 1.5 · web · Switch branch | Tổng quan | Phần tử |
| `k-3f329651` | x02 | 1.5 · web · Switch branch | Việc của tôi | Phần tử |
| `k-eb598be6` | x02 | 1.5 · web · Switch branch | 4 | Phần tử |
| `k-8314d1b8` | x02 | 1.5 · web · Switch branch | SỬA CHỮA | Phần tử |
| `k-0ca40a89` | x02 | 1.5 · web · Switch branch | Lệnh sửa chữa | Phần tử |
| `k-3a3ecf42` | x02 | 1.5 · web · Switch branch | Báo giá | Phần tử |
| `k-e1015dc0` | x02 | 1.5 · web · Switch branch | Phiếu xuất kho | Phần tử |
| `k-ab8455fa` | x02 | 1.5 · web · Switch branch | Bồi thường | Phần tử |
| `k-7f9078d9` | x02 | 1.5 · web · Switch branch | THEO DÕI | Phần tử |
| `k-3058600c` | x02 | 1.5 · web · Switch branch | Quy trình | Phần tử |
| `k-cd76022a` | x02 | 1.5 · web · Switch branch | Báo cáo | Phần tử |
| `k-b15d1baf` | x02 | 1.5 · web · Switch branch | Xưởng | Phần tử |
| `k-323aeb53` | x02 | 1.5 · web · Switch branch | Cơ sở Hải Phòng | Phần tử |
| `k-c1d3b5a2` | x02 | 1.5 · web · Switch branch | Tổng quan | Phần tử |
| `k-cc16b174` | x02 | 1.5 · web · Switch branch | Home chi nhánh | Phần tử |
| `k-9ea75197` | x02 | 1.5 · web · Switch branch | Màn giữ chỗ để nối prototype. | Phần tử |
| `k-aa9fb08d` | x02 | 1.5 · web · Switch branch | Đang dùng | Phần tử |
| `k-e21ef12a` | x02 | 1.5 · web · Switch branch | Trang chủ | Cỡ chữ |
| `k-6e89200f` | x02 | 1.5 · web · Switch branch | Trang chủ | Độ đậm |
| `k-db20a3d1` | x02 | 1.5 · web · Switch branch | Trang chủ | Màu chữ |
| `k-18f0227a` | x02 | 1.5 · web · Switch branch | Nguyễn Văn An | Độ đậm |
| `k-561e2e82` | x02 | 1.5 · web · Switch branch | NA | Cỡ chữ |
| `k-0591362e` | x02 | 1.5 · web · Switch branch | NA | Độ đậm |
| `k-e21ef12a` | x02 | 1.5 · web · Switch branch | Trang chủ | Cỡ chữ |
| `k-d77307e1` | x02 | 1.5 · web · Switch branch | Trang chủ | Line-height |
| `k-db20a3d1` | x02 | 1.5 · web · Switch branch | Trang chủ | Màu chữ |
| `k-c6819a82` | x02 | 1.5 · web · Switch branch | Trang chủ | Font |
| `k-70ebe023` | x02 | 1.5 · web · Switch branch | Chọn chi nhánh | Màu chữ |
| `k-e3cd66bc` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» +16 chữ | Rộng |
| `k-72795caf` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» +16 chữ | Cao |
| `k-3bddb92b` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» +16 chữ | Nền |
| `k-79222d8e` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» +16 chữ | Lề trong trái |
| `k-2d8c9f67` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» +3 chữ | Rộng |
| `k-de96e488` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» +3 chữ | Lề trong trái |
| `k-addf4054` | x02 | 1.5 · web · Switch branch | Nút «Delta Hải Phòng» | Rộng |
| `k-be14269f` | x02 | 1.5 · web · Switch branch | Nút «Nguyễn Văn An» | Rộng |
| `k-0c343433` | x02 | 1.5 · web · Switch branch | Nút «Nguyễn Văn An» | Cao |
| `k-9599f3e6` | x02 | 1.5 · web · Switch branch | Khung «NA» | Rộng |
| `k-6bf3f57f` | x02 | 1.5 · web · Switch branch | Khung «NA» | Cao |
| `k-210a5724` | x02 | 1.5 · web · Switch branch | Khung «NA» | Bo góc |
| `k-d8495fe9` | x02 | 1.5 · web · Switch branch | Khung «NA» | Lề trong trái |
| `k-b14e9360` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» | Cao |
| `k-cc6c4f04` | x02 | 1.5 · web · Switch branch | Khung «Trang chủ» | Nền |
| `k-392023e4` | x02 | 1.5 · web · Switch branch | Khung «Delta Hải Phòng» +1 chữ | Rộng |
| `k-4c532cb1` | x02 | 1.5 · web · Switch branch | Khung «Delta Hải Phòng» +1 chữ | Cao |
| `k-2af33b70` | x02 | 1.5 · web · Switch branch | Khung «Delta Hải Phòng» +1 chữ | Nền |
| `k-c72e63bd` | x02 | 1.5 · web · Switch branch | Khung «Delta Hải Phòng» +1 chữ | Viền |
| `k-503c9cde` | x02 | 1.5 · web · Switch branch | Khung «Chọn chi nhánh» +11 chữ | Rộng |
| `k-47c0bff9` | x02 | 1.5 · web · Switch branch | Khung «Chọn chi nhánh» +11 chữ | Cao |
| `k-b68a0527` | x02 | 1.5 · web · Switch branch | Khung «Chọn chi nhánh» +11 chữ | Lề trong trái |
| `k-53cff25a` | x02 | 1.5 · web · Switch branch | Khung «Chọn chi nhánh» +11 chữ | Lề trong trên |
| `k-830c88a5` | x02 | 1.5 · web · Switch branch | Khung «Công ty mẹ — Delta Quốc tế» +1 chữ | Rộng |
| `k-f1b6e88b` | x02 | 1.5 · web · Switch branch | Khung «Công ty mẹ — Delta Quốc tế» +1 chữ | Cao |
| `k-6331e2f9` | x02 | 1.5 · web · Switch branch | Khung «Công ty mẹ — Delta Quốc tế» +1 chữ | Nền |
| `k-acdffbaa` | x02 | 1.5 · web · Switch branch | Khung «Công ty mẹ — Delta Quốc tế» +1 chữ | Viền |
| `k-f59f2416` | x02 | 1.5 · web · Switch branch | Khung «Công ty mẹ — Delta Quốc tế» +1 chữ | Lề trong trái |
| `k-6809e77a` | x02 | 1.5 · web · Switch branch | Khung «Delta Hà Nội» +1 chữ | Rộng |
| `k-a540b154` | x02 | 1.5 · web · Switch branch | Khung «Delta Hà Nội» +1 chữ | Cao |
| `k-3f5bd123` | x02 | 1.5 · web · Switch branch | Khung «Delta Hà Nội» +1 chữ | Nền |
| `k-54c0d45d` | x02 | 1.5 · web · Switch branch | Khung «Delta Hà Nội» +1 chữ | Viền |
| `k-8cd1ab01` | x02 | 1.5 · web · Switch branch | Khung «Delta Hà Nội» +1 chữ | Lề trong trái |
| `k-9b81ec71` | x02 | 1.5 · web · Switch branch | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Rộng |
| `k-0d2179cd` | x02 | 1.5 · web · Switch branch | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Cao |
| `k-74e7213c` | x02 | 1.5 · web · Switch branch | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Nền |
| `k-2051353f` | x02 | 1.5 · web · Switch branch | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Viền |
| `k-eae1bc05` | x02 | 1.5 · web · Switch branch | Khung «Delta TP. Hồ Chí Minh» +1 chữ | Lề trong trái |
| `k-679bd69b` | x02 | 1.5 · web · Switch branch | «NA» → «Trang chủ» | Khoảng cách dọc |
| `k-f38a73a6` | x02 | 1.5 · web · Switch branch | «Trang chủ» → «Chọn chi nhánh» | Khoảng cách dọc |
| `k-2a89d055` | x02 | 1.5 · web · Switch branch | «Chọn chi nhánh» → «Công ty mẹ — Delta Qu…» | Khoảng cách dọc |
| `k-77599ea5` | x02 | 1.5 · web · Switch branch | «Công ty mẹ — Delta Qu…» → «Toàn bộ 3 chi nhánh» | Khoảng cách dọc |
| `k-2439ef5d` | x02 | 1.5 · web · Switch branch | «Toàn bộ 3 chi nhánh» → «Hoặc chọn chi nhánh c…» | Khoảng cách dọc |
| `k-b7334fe4` | x02 | 1.5 · web · Switch branch | «Delta Hải Phòng» → «Hải Phòng» | Khoảng cách dọc |
| `k-8bb9073a` | x02 | 1.5 · web · Switch branch | «Delta Hà Nội» → «Hà Nội» | Khoảng cách dọc |
| `k-57a6b35b` | x02 | 1.5 · web · Switch branch | «Delta TP. Hồ Chí Minh» → «TP. Hồ Chí Minh» | Khoảng cách dọc |
| `k-5ad08b99` | x02 | 1.5 · web · Switch branch | «TP. Hồ Chí Minh» → «Huỷ» | Khoảng cách dọc |
| `k-b2a4ef50` | x02 | 1.5 · web · Switch branch | «Huỷ» → «Chọn» | Khoảng cách ngang |
| `k-dcea85b3` | x02 | 1.5 · web · Switch branch | Hoặc chọn chi nhánh cụ thể | Canh lề |
| `k-fa37ef17` | x02 | 1.5 · web · Switch branch | Checkbox #1 | Kích thước |
| `k-f57da841` | x02 | 1.5 · web · Switch branch | Checkbox #1 | Bo góc |
| `k-cad7d8d8` | x02 | 1.5 · web · Switch branch | Checkbox #2 | Kích thước |
| `k-2f7dea88` | x02 | 1.5 · web · Switch branch | Checkbox #2 | Bo góc |
| `k-f9f0467b` | x02 | 1.5 · web · Switch branch | Checkbox #3 | Kích thước |
| `k-f39d84fd` | x02 | 1.5 · web · Switch branch | Checkbox #3 | Bo góc |
| `k-cdfe80ed` | x02 | 1.5 · web · Switch branch | Đường kẻ ngang | Số lượng |
| `k-dc771dbb` | x02 | 1.5 · web · Switch branch | Icon house cạnh «Trang chủ» | Phần tử |
| `k-0332d326` | x02 | 1.5 · web · Switch branch | Icon clipboard-list cạnh «Trang chủ» | Phần tử |
| `k-f724ae98` | x02 | 1.5 · web · Switch branch | Icon truck cạnh «Trang chủ» | Phần tử |
| `k-56d13663` | x02 | 1.5 · web · Switch branch | Icon search cạnh «Chọn chi nhánh» | Phần tử |
| `k-f0adb719` | x02 | 1.5 · web · Switch branch | Icon icon/layout-dashboard | Phần tử |
| `k-3517fc45` | x02 | 1.5 · web · Switch branch | Icon icon/inbox | Phần tử |
| `k-1a28b0fc` | x02 | 1.5 · web · Switch branch | Icon icon/wrench | Phần tử |
| `k-8dd819a1` | x02 | 1.5 · web · Switch branch | Icon icon/file-text | Phần tử |
| `k-56c458c4` | x02 | 1.5 · web · Switch branch | Icon icon/package | Phần tử |
| `k-c034fa60` | x02 | 1.5 · web · Switch branch | Icon icon/shield | Phần tử |
| `k-9ae8a887` | x02 | 1.5 · web · Switch branch | Icon icon/git-branch | Phần tử |
| `k-fa6f5422` | x02 | 1.5 · web · Switch branch | Icon icon/chart-column | Phần tử |
| `k-1a28b0fc` | x02 | 1.5 · web · Switch branch | Icon icon/wrench | Phần tử |
| `k-19f60b56` | x02 | 1.5 · web · Switch branch | Icon icon/map-pin | Phần tử |
| `k-e02de15c` | x02 | 1.5 · web · Switch branch | Icon icon/chevron-down | Phần tử |
| `k-07feab05` | x02 | 1.5 · web · Switch branch | Icon icon/chevron-right | Phần tử |
| `k-a7dc3037` | x02 | 1.5 · web · Switch branch | Icon Icon | Phần tử |
| `k-dfaba06c` | x02 | 1.5 · web · Switch branch | Icon Radio / RadioListItem | Phần tử |
| `k-f72ce50f` | x02 | 1.5 · web · Switch branch | Icon map-pin cạnh «Delta Hải Phòng» | Kích thước |
| `k-8547386a` | x02 | 1.5 · web · Switch branch | Icon map-pin cạnh «Delta Hải Phòng» | Màu |
| `k-66c88394` | x02 | 1.5 · web · Switch branch | Icon panel-left cạnh «Trang chủ» | Kích thước |
| `k-8c6ae416` | x02 | 1.5 · web · Switch branch | Icon search cạnh «Delta Hải Phòng» | Kích thước |
| `k-72bb46fe` | x02 | 1.5 · web · Switch branch | Icon bell cạnh «NA» | Kích thước |
| `k-aef3d5b7` | x02 | 1.5 · web · Switch branch | Icon house cạnh «Chọn chi nhánh» | Kích thước |
| `k-bc307469` | x02 | 1.5 · web · Switch branch | Icon house cạnh «Chọn chi nhánh» | Màu |
| `k-4fef87b1` | x02 | 1.5 · web · Switch branch | Ảnh/logo | Số lượng |
| `k-33977150` | d01 | 2.1 · web | Xác nhận | Phần tử |
| `k-61f453e6` | d02 | 2.1 · web | Mật khẩu tạm chỉ dùng một lần. Hãy đặt … | Phần tử |
| `k-de27505d` | d01 | 2.1 · web | Đặt mật khẩu | Phần tử |
| `k-c18a20be` | c01 | 2.1 · web | Mật khẩu mới — dấu * | Màu |
| `k-d7d28db5` | c01 | 2.1 · web | Nhập lại mật khẩu mới — dấu * | Màu |
| `k-185f11d6` | d02 | 2.1 · web | Khung «Tạo mật khẩu mới» +6 chữ | Cao |
| `k-3e479765` | s01 | 2.1 · web | Khung «Tạo mật khẩu mới» +6 chữ | Viền |
| `k-54528495` | s01 | 2.1 · web | Khung «Tạo mật khẩu mới» +6 chữ | Lề trong trái |
| `k-5f871dc9` | s01 | 2.1 · web | Khung «Tạo mật khẩu mới» +6 chữ | Lề trong trên |
| `k-5278d65b` | d02 | 2.1 · web | «Tạo mật khẩu mới» → «Mật khẩu mới» | Khoảng cách dọc |
| `k-9d355951` | s09 | 2.1 · web | «Nhập lại mật khẩu mới» → «Huỷ» | Khoảng cách dọc |
| `k-e26324a8` | n13 | 2.1 · web | Icon eye cạnh «Mật khẩu mới» | Kích thước |
| `k-07c8458b` | n13 | 2.1 · web | Icon eye cạnh «Mật khẩu mới» | Màu |
| `k-715a2543` | n13 | 2.1 · web | Icon eye cạnh «Nhập lại mật khẩu mới» | Kích thước |
| `k-7af16e27` | n13 | 2.1 · web | Icon eye cạnh «Nhập lại mật khẩu mới» | Màu |
| `k-27402fc0` | d09 | 2.1 · web · Submitting | Đang lưu… | Phần tử |
| `k-55dfcede` | d02 | 2.1 · web · Submitting | Mật khẩu tạm chỉ dùng một lần. Hãy đặt … | Phần tử |
| `k-2f06abeb` | s07 | 2.1 · web · Submitting | Mật khẩu mới | Màu chữ |
| `k-73cb249f` | s07 | 2.1 · web · Submitting | Mật khẩu mới — dấu * | Màu |
| `k-9f9c608f` | c07 | 2.1 · web · Submitting | ••••••••••• | Line-height |
| `k-c9644c43` | s07 | 2.1 · web · Submitting | Nhập lại mật khẩu mới | Màu chữ |
| `k-d4b72b11` | s07 | 2.1 · web · Submitting | Nhập lại mật khẩu mới — dấu * | Màu |
| `k-9f9c608f` | c07 | 2.1 · web · Submitting | ••••••••••• | Line-height |
| `k-7b8358b5` | d02 | 2.1 · web · Submitting | Khung «Tạo mật khẩu mới» +6 chữ | Cao |
| `k-e3d2787a` | s01 | 2.1 · web · Submitting | Khung «Tạo mật khẩu mới» +6 chữ | Viền |
| `k-6fc07d56` | s01 | 2.1 · web · Submitting | Khung «Tạo mật khẩu mới» +6 chữ | Lề trong trái |
| `k-098f79e1` | s01 | 2.1 · web · Submitting | Khung «Tạo mật khẩu mới» +6 chữ | Lề trong trên |
| `k-d517a2c6` | d02 | 2.1 · web · Submitting | «Tạo mật khẩu mới» → «Mật khẩu mới» | Khoảng cách dọc |
| `k-e0f24fe4` | s09 | 2.1 · web · Submitting | «•••••••••••» → «Huỷ» | Khoảng cách dọc |
| `k-56d1e4b4` | d09 | 2.1 · web · Submitting | Icon loader cạnh «Huỷ» | Kích thước |
| `k-f6df3aaf` | n13 | 2.1 · web · Submitting | Icon eye cạnh «•••••••••••» | Kích thước |
| `k-1eeb15be` | n13 | 2.1 · web · Submitting | Icon eye cạnh «•••••••••••» | Màu |
| `k-f6df3aaf` | n13 | 2.1 · web · Submitting | Icon eye cạnh «•••••••••••» | Kích thước |
| `k-1eeb15be` | n13 | 2.1 · web · Submitting | Icon eye cạnh «•••••••••••» | Màu |
| `k-5b794387` | n08 | 2.1 · web · Field error | Ít nhất 8 ký tự, có chữ thường, chữ hoa… | Phần tử |
| `k-b3f1a64a` | d01 | 2.1 · web · Field error | Xác nhận | Phần tử |
| `k-4e203abc` | d02 | 2.1 · web · Field error | Mật khẩu tạm chỉ dùng một lần. Hãy đặt … | Phần tử |
| `k-936c2ff9` | d01 | 2.1 · web · Field error | Đặt mật khẩu | Phần tử |
| `k-7fa49ce4` | c01 | 2.1 · web · Field error | Mật khẩu mới — dấu * | Màu |
| `k-0e62652f` | c07 | 2.1 · web · Field error | •••• | Line-height |
| `k-92185d32` | c06 | 2.1 · web · Field error | Mật khẩu cần ít nhất 8 ký tự, có chữ th… | Line-height |
| `k-009730d8` | c06 | 2.1 · web · Field error | Mật khẩu cần ít nhất 8 ký tự, có chữ th… | Màu chữ |
| `k-b60935ea` | c01 | 2.1 · web · Field error | Nhập lại mật khẩu mới — dấu * | Màu |
| `k-cd43f9aa` | c07 | 2.1 · web · Field error | ••••• | Line-height |
| `k-50d4ef1b` | c06 | 2.1 · web · Field error | Mật khẩu nhập lại không khớp. | Line-height |
| `k-139fe440` | c06 | 2.1 · web · Field error | Mật khẩu nhập lại không khớp. | Màu chữ |
| `k-1444cfaf` | d02 | 2.1 · web · Field error | Khung «Tạo mật khẩu mới» +7 chữ | Cao |
| `k-f398dcf0` | s01 | 2.1 · web · Field error | Khung «Tạo mật khẩu mới» +7 chữ | Viền |
| `k-c68cbfb7` | s01 | 2.1 · web · Field error | Khung «Tạo mật khẩu mới» +7 chữ | Lề trong trái |
| `k-9ff1d526` | s01 | 2.1 · web · Field error | Khung «Tạo mật khẩu mới» +7 chữ | Lề trong trên |
| `k-f5203434` | d02 | 2.1 · web · Field error | «Tạo mật khẩu mới» → «Mật khẩu mới» | Khoảng cách dọc |
| `k-48e0ea92` | c06 | 2.1 · web · Field error | «••••» → «Mật khẩu cần ít nhất …» | Khoảng cách dọc |
| `k-9a9cefc6` | s09 | 2.1 · web · Field error | «Mật khẩu cần ít nhất …» → «Nhập lại mật khẩu mới» | Khoảng cách dọc |
| `k-8ac9cf1a` | s09 | 2.1 · web · Field error | «•••••» → «Mật khẩu nhập lại khô…» | Khoảng cách dọc |
| `k-20c56e54` | s09 | 2.1 · web · Field error | «Mật khẩu nhập lại khô…» → «Huỷ» | Khoảng cách dọc |
| `k-26e02d82` | n14 | 2.1 · web · Field error | Icon Icon | Phần tử |
| `k-26e02d82` | n14 | 2.1 · web · Field error | Icon Icon | Phần tử |
| `k-0e2ac80a` | n13 | 2.1 · web · Field error | Icon eye cạnh «••••» | Kích thước |
| `k-c3cfc768` | n13 | 2.1 · web · Field error | Icon eye cạnh «••••» | Màu |
| `k-f7d9099a` | n13 | 2.1 · web · Field error | Icon eye cạnh «•••••» | Kích thước |
| `k-648cf186` | n13 | 2.1 · web · Field error | Icon eye cạnh «•••••» | Màu |
| `k-e7db3880` | d01 | 2.1 · web · Network error | Xác nhận | Phần tử |
| `k-77a2f04a` | d02 | 2.1 · web · Network error | Mật khẩu tạm chỉ dùng một lần. Hãy đặt … | Phần tử |
| `k-cf75f95a` | d01 | 2.1 · web · Network error | Đặt mật khẩu | Phần tử |
| `k-720f0a91` | c01 | 2.1 · web · Network error | Mật khẩu mới — dấu * | Màu |
| `k-7f478d18` | c07 | 2.1 · web · Network error | ••••••••••• | Line-height |
| `k-cc090a87` | c01 | 2.1 · web · Network error | Nhập lại mật khẩu mới — dấu * | Màu |
| `k-7f478d18` | c07 | 2.1 · web · Network error | ••••••••••• | Line-height |
| `k-dc695fde` | d02 | 2.1 · web · Network error | Khung «Tạo mật khẩu mới» +6 chữ | Cao |
| `k-2d3ccefb` | s01 | 2.1 · web · Network error | Khung «Tạo mật khẩu mới» +6 chữ | Viền |
| `k-cc23d6e6` | s01 | 2.1 · web · Network error | Khung «Tạo mật khẩu mới» +6 chữ | Lề trong trái |
| `k-6668eab2` | s01 | 2.1 · web · Network error | Khung «Tạo mật khẩu mới» +6 chữ | Lề trong trên |
| `k-c6673780` | n01 | 2.1 · web · Network error | Khung «Mất kết nối. Kiểm tra mạng …» | Cao |
| `k-a21208a0` | n01 | 2.1 · web · Network error | Khung «Mất kết nối. Kiểm tra mạng …» | Lề trong trái |
| `k-8926ebe0` | d02 | 2.1 · web · Network error | «Tạo mật khẩu mới» → «Mật khẩu mới» | Khoảng cách dọc |
| `k-9139ec39` | s09 | 2.1 · web · Network error | «•••••••••••» → «Huỷ» | Khoảng cách dọc |
| `k-23ca7129` | n03 | 2.1 · web · Network error | «Huỷ» → «Mất kết nối. Kiểm tra…» | Khoảng cách dọc |
| `k-f6f9cd3c` | n01 | 2.1 · web · Network error | Icon circle-alert cạnh «Mất kết nối. Kiểm tra m…» | Phần tử |
| `k-c40577ff` | n01 | 2.1 · web · Network error | Icon icon/x | Phần tử |
| `k-ff4d3b9c` | n13 | 2.1 · web · Network error | Icon eye cạnh «•••••••••••» | Kích thước |
| `k-d5d502f1` | n13 | 2.1 · web · Network error | Icon eye cạnh «•••••••••••» | Màu |
| `k-ff4d3b9c` | n13 | 2.1 · web · Network error | Icon eye cạnh «•••••••••••» | Kích thước |
| `k-d5d502f1` | n13 | 2.1 · web · Network error | Icon eye cạnh «•••••••••••» | Màu |
| `k-2fbddf6d` | d05 | 2.1 · web · Temp expired | Mật khẩu tạm hết hạn | Phần tử |
| `k-851b21e1` | c02 | 2.1 · web · Temp expired | Quay về đăng nhập | Độ đậm |
| `k-8e3e2ebd` | c02 | 2.1 · web · Temp expired | Quay về đăng nhập | Màu chữ |
| `k-353f40c2` | d05 | 2.1 · web · Temp expired | Quên mật khẩu | Màu chữ |
| `k-4b7734e3` | d05 | 2.1 · web · Temp expired | Quên mật khẩu | Gạch chân |
| `k-e94feb4b` | s01 | 2.1 · web · Temp expired | Khung «Mật khẩu tạm đã hết hạn. Đặ…» +2 chữ | Cao |
| `k-a197682a` | s01 | 2.1 · web · Temp expired | Khung «Mật khẩu tạm đã hết hạn. Đặ…» +2 chữ | Viền |
| `k-277c5395` | s01 | 2.1 · web · Temp expired | Khung «Mật khẩu tạm đã hết hạn. Đặ…» +2 chữ | Lề trong trái |
| `k-a760d82a` | s01 | 2.1 · web · Temp expired | Khung «Mật khẩu tạm đã hết hạn. Đặ…» +2 chữ | Lề trong trên |
| `k-f951873d` | d05 | 2.1 · web · Temp expired | Nút «Quay về đăng nhập» | Cao |
| `k-dfc1c10d` | c02 | 2.1 · web · Temp expired | Nút «Quay về đăng nhập» | Bo góc |
| `k-5eab690a` | c02 | 2.1 · web · Temp expired | Nút «Quay về đăng nhập» | Nền |
| `k-8cb0512a` | d05 | 2.1 · web · Temp expired | Link «Quên mật khẩu» | Cao |
| `k-58cb66b6` | d05 | 2.1 · web · Temp expired | Link «Quên mật khẩu» | Bo góc |
| `k-14c78559` | d05 | 2.1 · web · Temp expired | Link «Quên mật khẩu» | Nền |
| `k-da5eef27` | s09 | 2.1 · web · Temp expired | «Mật khẩu tạm đã hết h…» → «Quay về đăng nhập» | Khoảng cách dọc |
| `k-d197e9ad` | s09 | 2.1 · web · Temp expired | «Quay về đăng nhập» → «Quên mật khẩu» | Khoảng cách dọc |
| `k-b6702f7d` | c08 | 2.1 · web · Window expired | Hết thời gian | Cỡ chữ |
| `k-35581002` | c08 | 2.1 · web · Window expired | Hết thời gian | Line-height |
| `k-46e76f62` | c02 | 2.1 · web · Window expired | Quay về đăng nhập | Độ đậm |
| `k-b5540178` | c02 | 2.1 · web · Window expired | Quay về đăng nhập | Màu chữ |
| `k-9c08dad9` | c02 | 2.1 · web · Window expired | Quay về đăng nhập | Gạch chân |
| `k-f9a9de65` | s01 | 2.1 · web · Window expired | Khung «Hết thời gian» +3 chữ | Cao |
| `k-6d1da7d6` | s01 | 2.1 · web · Window expired | Khung «Hết thời gian» +3 chữ | Viền |
| `k-5c45e84d` | s01 | 2.1 · web · Window expired | Khung «Hết thời gian» +3 chữ | Lề trong trái |
| `k-52eacdb2` | s01 | 2.1 · web · Window expired | Khung «Hết thời gian» +3 chữ | Lề trong trên |
| `k-99db06bd` | c08 | 2.1 · web · Window expired | «Hết thời gian» → «Đã quá thời gian đặt …» | Khoảng cách dọc |
| `k-c97d6c08` | d07 | 2.1 · web · Confirm leave | Huỷ | Phần tử |
| `k-e7f4ed6c` | d01 | 2.1 · web · Confirm leave | Xác nhận | Phần tử |
| `k-2dfad786` | d02 | 2.1 · web · Confirm leave | Mật khẩu tạm chỉ dùng một lần. Hãy đặt … | Phần tử |
| `k-7f29680f` | d01 | 2.1 · web · Confirm leave | Đặt mật khẩu | Phần tử |
| `k-fb227ebf` | d07 | 2.1 · web · Confirm leave | Bỏ thay đổi | Phần tử |
| `k-85778e53` | c01 | 2.1 · web · Confirm leave | Mật khẩu mới — dấu * | Màu |
| `k-a40a2937` | c07 | 2.1 · web · Confirm leave | ••••••••••• | Line-height |
| `k-dc80a7a4` | c01 | 2.1 · web · Confirm leave | Nhập lại mật khẩu mới — dấu * | Màu |
| `k-7d073aaa` | c07 | 2.1 · web · Confirm leave | ••• | Line-height |
| `k-f1b200f3` | d02 | 2.1 · web · Confirm leave | Khung «Tạo mật khẩu mới» +9 chữ | Cao |
| `k-0458aadb` | s01 | 2.1 · web · Confirm leave | Khung «Tạo mật khẩu mới» +9 chữ | Viền |
| `k-3ee70a04` | s01 | 2.1 · web · Confirm leave | Khung «Tạo mật khẩu mới» +9 chữ | Lề trong trái |
| `k-15703a3a` | s01 | 2.1 · web · Confirm leave | Khung «Tạo mật khẩu mới» +9 chữ | Lề trong trên |
| `k-2bd8db2c` | s09 | 2.1 · web · Confirm leave | «Tạo mật khẩu mới» → «Huỷ bản ghi?» | Khoảng cách dọc |
| `k-88e46e5e` | s09 | 2.1 · web · Confirm leave | «Huỷ bản ghi?» → «Mật khẩu mới» | Khoảng cách dọc |
| `k-047a6733` | s09 | 2.1 · web · Confirm leave | «Mật khẩu mới» → «Bạn có dữ liệu chưa đ…» | Khoảng cách dọc |
| `k-37d7838f` | s09 | 2.1 · web · Confirm leave | «Ít nhất 8 ký tự, có c…» → «Huỷ» | Khoảng cách dọc |
| `k-d9d4ee0a` | n07 | 2.1 · web · Confirm leave | «Huỷ» → «Tiếp tục chỉnh sửa» | Xếp hàng |
| `k-0030cdb4` | s09 | 2.1 · web · Confirm leave | «Tiếp tục chỉnh sửa» → «Nhập lại mật khẩu mới» | Khoảng cách dọc |
| `k-fafe0599` | n13 | 2.1 · web · Confirm leave | Icon eye cạnh «Bạn có dữ liệu chưa đượ…» | Kích thước |
| `k-5c38ed70` | n13 | 2.1 · web · Confirm leave | Icon eye cạnh «Bạn có dữ liệu chưa đượ…» | Màu |
| `k-c28767fe` | n13 | 2.1 · web · Confirm leave | Icon eye cạnh «•••» | Kích thước |
| `k-ac5d49b9` | n13 | 2.1 · web · Confirm leave | Icon eye cạnh «•••» | Màu |
| `k-50a7ada6` | c09 | 3.1 · web | Đặt lại qua email | Độ đậm |
| `k-4703c1d5` | c09 | 3.1 · web | Liên hệ IT | Độ đậm |
| `k-65b2885e` | s01 | 3.1 · web | Khung «Quay lại» +5 chữ | Cao |
| `k-9c6bcf71` | s01 | 3.1 · web | Khung «Quay lại» +5 chữ | Viền |
| `k-157472f9` | s01 | 3.1 · web | Khung «Quay lại» +5 chữ | Lề trong trái |
| `k-b5402301` | s01 | 3.1 · web | Khung «Quay lại» +5 chữ | Lề trong trên |
| `k-61a17cec` | s05 | 3.1 · web | Nút «Quay lại» | Rộng |
| `k-70d5672f` | c09 | 3.1 · web | Nút «Đặt lại qua email» | Viền |
| `k-88f8f86e` | c09 | 3.1 · web | Nút «Liên hệ IT» | Cao |
| `k-86b23c96` | c09 | 3.1 · web | Nút «Liên hệ IT» | Viền |
| `k-acdd1b23` | s05 | 3.1 · web | «Quay lại» → «Quên mật khẩu» | Khoảng cách dọc |
| `k-b29f27dd` | c09 | 3.1 · web | «Đặt lại qua email» → «Nhận link qua email» | Khoảng cách dọc |
| `k-8dd262ae` | c09 | 3.1 · web | «Liên hệ IT» → «Khi không có hoặc khô…» | Khoảng cách dọc |
| `k-0a122225` | c09 | 3.1 · web | Khi không có hoặc không nhận được email | Canh lề |
| `k-5b67addf` | c09 | 3.1 · web | Icon mail cạnh «Nhận link qua email» | Kích thước |
| `k-b876f05d` | c09 | 3.1 · web | Icon headset cạnh «Khi không có hoặc không…» | Kích thước |
| `k-202adc6a` | d01 | 3.2 · web | Xác nhận | Phần tử |
| `k-31279628` | d03 | 3.2 · web | Tên bạn dùng để đăng nhập. | Phần tử |
| `k-16be3a6d` | d01 | 3.2 · web | Gửi link đặt lại | Phần tử |
| `k-cf2df573` | c01 | 3.2 · web | Tên tài khoản — dấu * | Màu |
| `k-ba0c60ef` | s01 | 3.2 · web | Khung «Quay lại» +3 chữ | Cao |
| `k-5f41d584` | s01 | 3.2 · web | Khung «Quay lại» +3 chữ | Viền |
| `k-c28a5eb5` | s01 | 3.2 · web | Khung «Quay lại» +3 chữ | Lề trong trái |
| `k-6b1adba1` | s01 | 3.2 · web | Khung «Quay lại» +3 chữ | Lề trong trên |
| `k-808abbe3` | s05 | 3.2 · web | Nút «Quay lại» | Rộng |
| `k-1872a0df` | s05 | 3.2 · web | «Quay lại» → «Đặt lại mật khẩu» | Khoảng cách dọc |
| `k-dabcf0c2` | d03 | 3.2 · web | «Tên tài khoản» → «Tên tài khoản» | Khoảng cách dọc |
| `k-2d65dffe` | d09 | 3.2 · web · Submitting | Đang gửi… | Phần tử |
| `k-003de3df` | d03 | 3.2 · web · Submitting | Tên bạn dùng để đăng nhập. | Phần tử |
| `k-6ea99edf` | s07 | 3.2 · web · Submitting | Tên tài khoản | Màu chữ |
| `k-b3768f4b` | s07 | 3.2 · web · Submitting | Tên tài khoản — dấu * | Màu |
| `k-4dba6c70` | c07 | 3.2 · web · Submitting | an.nguyen | Line-height |
| `k-34022d88` | s01 | 3.2 · web · Submitting | Khung «Quay lại» +3 chữ | Cao |
| `k-01cd4bd6` | s01 | 3.2 · web · Submitting | Khung «Quay lại» +3 chữ | Viền |
| `k-9437bd27` | s01 | 3.2 · web · Submitting | Khung «Quay lại» +3 chữ | Lề trong trái |
| `k-d4122423` | s01 | 3.2 · web · Submitting | Khung «Quay lại» +3 chữ | Lề trong trên |
| `k-b79ac171` | s05 | 3.2 · web · Submitting | Nút «Quay lại» | Rộng |
| `k-f523c136` | s05 | 3.2 · web · Submitting | «Quay lại» → «Đặt lại mật khẩu» | Khoảng cách dọc |
| `k-ec886607` | d03 | 3.2 · web · Submitting | «Tên tài khoản» → «an.nguyen» | Khoảng cách dọc |
| `k-82ad2e3e` | d09 | 3.2 · web · Submitting | Icon loader cạnh «an.nguyen» | Kích thước |
| `k-df489768` | x01 | 3.2 · web · Cooldown | Tên tài khoản | Phần tử |
| `k-f6d4e9bf` | d01 | 3.2 · web · Cooldown | Xác nhận | Phần tử |
| `k-636faa82` | d03 | 3.2 · web · Cooldown | Tên bạn dùng để đăng nhập. | Phần tử |
| `k-327a48bd` | x01 | 3.2 · web · Cooldown | an.nguyen | Phần tử |
| `k-9939c52d` | x01 | 3.2 · web · Cooldown | Gửi lại sau 42 giây | Phần tử |
| `k-14899b04` | c01 | 3.2 · web · Cooldown | Tên tài khoản — dấu * | Màu |
| `k-b7d1d0ca` | s01 | 3.2 · web · Cooldown | Khung «Quay lại» +2 chữ | Cao |
| `k-e87675cc` | s01 | 3.2 · web · Cooldown | Khung «Quay lại» +2 chữ | Viền |
| `k-ecc336c7` | s01 | 3.2 · web · Cooldown | Khung «Quay lại» +2 chữ | Lề trong trái |
| `k-9927f218` | s01 | 3.2 · web · Cooldown | Khung «Quay lại» +2 chữ | Lề trong trên |
| `k-ecc6b282` | s05 | 3.2 · web · Cooldown | Nút «Quay lại» | Rộng |
| `k-919737af` | s05 | 3.2 · web · Cooldown | «Quay lại» → «Đặt lại mật khẩu» | Khoảng cách dọc |
| `k-0e9fa484` | d01 | 3.2 · web · Rate limited | Xác nhận | Phần tử |
| `k-853eb30a` | d03 | 3.2 · web · Rate limited | Tên bạn dùng để đăng nhập. | Phần tử |
| `k-23b8c8d5` | d01 | 3.2 · web · Rate limited | Gửi link đặt lại | Phần tử |
| `k-78c76c74` | c01 | 3.2 · web · Rate limited | Tên tài khoản — dấu * | Màu |
| `k-142b6d89` | c07 | 3.2 · web · Rate limited | an.nguyen | Line-height |
| `k-0c9bc72f` | c06 | 3.2 · web · Rate limited | Bạn đã gửi quá nhiều yêu cầu. Thử lại s… | Line-height |
| `k-70280d54` | c06 | 3.2 · web · Rate limited | Bạn đã gửi quá nhiều yêu cầu. Thử lại s… | Màu chữ |
| `k-6782a616` | s01 | 3.2 · web · Rate limited | Khung «Quay lại» +4 chữ | Cao |
| `k-d4bcbc49` | s01 | 3.2 · web · Rate limited | Khung «Quay lại» +4 chữ | Viền |
| `k-633b6bca` | s01 | 3.2 · web · Rate limited | Khung «Quay lại» +4 chữ | Lề trong trái |
| `k-350fe6a4` | s01 | 3.2 · web · Rate limited | Khung «Quay lại» +4 chữ | Lề trong trên |
| `k-69161192` | s05 | 3.2 · web · Rate limited | Nút «Quay lại» | Rộng |
| `k-9b69fc5d` | s05 | 3.2 · web · Rate limited | «Quay lại» → «Đặt lại mật khẩu» | Khoảng cách dọc |
| `k-779645be` | d03 | 3.2 · web · Rate limited | «Tên tài khoản» → «an.nguyen» | Khoảng cách dọc |
| `k-995d842b` | c06 | 3.2 · web · Rate limited | «an.nguyen» → «Bạn đã gửi quá nhiều …» | Khoảng cách dọc |
| `k-64f8dd63` | n14 | 3.2 · web · Rate limited | Icon Icon | Phần tử |
| `k-1567f927` | d01 | 3.2 · web · Network error | Xác nhận | Phần tử |
| `k-692ff83b` | d03 | 3.2 · web · Network error | Tên bạn dùng để đăng nhập. | Phần tử |
| `k-e82b463b` | d01 | 3.2 · web · Network error | Gửi link đặt lại | Phần tử |
| `k-eef94f8c` | c01 | 3.2 · web · Network error | Tên tài khoản — dấu * | Màu |
| `k-3c46094a` | c07 | 3.2 · web · Network error | an.nguyen | Line-height |
| `k-47098152` | s01 | 3.2 · web · Network error | Khung «Quay lại» +3 chữ | Cao |
| `k-a5172e45` | s01 | 3.2 · web · Network error | Khung «Quay lại» +3 chữ | Viền |
| `k-db04af8b` | s01 | 3.2 · web · Network error | Khung «Quay lại» +3 chữ | Lề trong trái |
| `k-49280efd` | s01 | 3.2 · web · Network error | Khung «Quay lại» +3 chữ | Lề trong trên |
| `k-80a5ce61` | s05 | 3.2 · web · Network error | Nút «Quay lại» | Rộng |
| `k-3294dca0` | n01 | 3.2 · web · Network error | Khung «Mất kết nối. Kiểm tra mạng …» | Cao |
| `k-ef1be3d1` | n01 | 3.2 · web · Network error | Khung «Mất kết nối. Kiểm tra mạng …» | Lề trong trái |
| `k-2d0c2a63` | s05 | 3.2 · web · Network error | «Quay lại» → «Đặt lại mật khẩu» | Khoảng cách dọc |
| `k-5d43b535` | d03 | 3.2 · web · Network error | «Tên tài khoản» → «an.nguyen» | Khoảng cách dọc |
| `k-63e4f708` | n03 | 3.2 · web · Network error | «an.nguyen» → «Mất kết nối. Kiểm tra…» | Khoảng cách dọc |
| `k-5a3f5bea` | n01 | 3.2 · web · Network error | Icon circle-alert cạnh «Mất kết nối. Kiểm tra m…» | Phần tử |
| `k-cf17b923` | n01 | 3.2 · web · Network error | Icon icon/x | Phần tử |
| `k-c8bfa23f` | d04 | 3.3 · web | Tài khoản: an.nguyen | Phần tử |
| `k-6794b09c` | c02 | 3.3 · web | Nhập lại tên tài khoản | Phần tử |
| `k-640ef74b` | c08 | 3.3 · web | Kiểm tra email | Cỡ chữ |
| `k-04deac5e` | c08 | 3.3 · web | Kiểm tra email | Line-height |
| `k-8ed2b2e8` | s06 | 3.3 · web | Chưa nhận được email? | Độ đậm |
| `k-a6c865ed` | s06 | 3.3 · web | Kiểm tra cả mục Thư rác, rồi thử gửi lạ… | Line-height |
| `k-b5a62b20` | s06 | 3.3 · web | Kiểm tra cả mục Thư rác, rồi thử gửi lạ… | Màu chữ |
| `k-18515c78` | s06 | 3.3 · web | Liên hệ IT | Gạch chân |
| `k-3c10c750` | s01 | 3.3 · web | Khung «Kiểm tra email» +6 chữ | Cao |
| `k-0508f9ac` | s01 | 3.3 · web | Khung «Kiểm tra email» +6 chữ | Viền |
| `k-0b12342b` | s01 | 3.3 · web | Khung «Kiểm tra email» +6 chữ | Lề trong trái |
| `k-973a5fd7` | s01 | 3.3 · web | Khung «Kiểm tra email» +6 chữ | Lề trong trên |
| `k-059b1917` | s06 | 3.3 · web | Khung «Chưa nhận được email?» +3 chữ | Cao |
| `k-63f1ad8a` | s06 | 3.3 · web | Khung «Chưa nhận được email?» +3 chữ | Bo góc |
| `k-f4bd57fa` | s06 | 3.3 · web | Khung «Chưa nhận được email?» +3 chữ | Nền |
| `k-e768556d` | s06 | 3.3 · web | Khung «Chưa nhận được email?» +3 chữ | Lề trong trái |
| `k-6f6cc825` | s06 | 3.3 · web | Khung «Chưa nhận được email?» +3 chữ | Lề trong trên |
| `k-4cfdc329` | s06 | 3.3 · web | Nút «Gửi lại link» | Rộng |
| `k-c6f88c11` | s06 | 3.3 · web | Nút «Gửi lại link» | Nền |
| `k-38a98a53` | s06 | 3.3 · web | Nút «Liên hệ IT» | Rộng |
| `k-49f5f98c` | c08 | 3.3 · web | «Kiểm tra email» → «Nếu tài khoản có emai…» | Khoảng cách dọc |
| `k-e7af0c45` | s06 | 3.3 · web | «Nếu tài khoản có emai…» → «Chưa nhận được email?» | Khoảng cách dọc |
| `k-c6044579` | s06 | 3.3 · web | «Chưa nhận được email?» → «Kiểm tra cả mục Thư r…» | Khoảng cách dọc |
| `k-72db5093` | s06 | 3.3 · web | «Kiểm tra cả mục Thư r…» → «Gửi lại link» | Khoảng cách dọc |
| `k-b25e0c01` | s06 | 3.3 · web | «Gửi lại link» → «Liên hệ IT» | Xếp hàng |
| `k-51da0c06` | s06 | 3.3 · web | «Liên hệ IT» → «Quay về đăng nhập» | Khoảng cách dọc |
| `k-dc4d8d28` | s06 | 3.3 · web | Đường kẻ ngang | Số lượng |
| `k-2db10f94` | d04 | 3.3 · web · Cooldown | Tài khoản: an.nguyen | Phần tử |
| `k-f0b91975` | c02 | 3.3 · web · Cooldown | Nhập lại tên tài khoản | Phần tử |
| `k-9358ff3f` | c08 | 3.3 · web · Cooldown | Kiểm tra email | Cỡ chữ |
| `k-981ec34b` | c08 | 3.3 · web · Cooldown | Kiểm tra email | Line-height |
| `k-7aa57de4` | s06 | 3.3 · web · Cooldown | Chưa nhận được email? | Độ đậm |
| `k-d716ab3d` | s06 | 3.3 · web · Cooldown | Kiểm tra cả mục Thư rác, rồi thử gửi lạ… | Line-height |
| `k-37180f6a` | s06 | 3.3 · web · Cooldown | Kiểm tra cả mục Thư rác, rồi thử gửi lạ… | Màu chữ |
| `k-8b148702` | s06 | 3.3 · web · Cooldown | Liên hệ IT | Gạch chân |
| `k-211ecb6e` | s01 | 3.3 · web · Cooldown | Khung «Kiểm tra email» +6 chữ | Cao |
| `k-99565388` | s01 | 3.3 · web · Cooldown | Khung «Kiểm tra email» +6 chữ | Viền |
| `k-d5a6852b` | s01 | 3.3 · web · Cooldown | Khung «Kiểm tra email» +6 chữ | Lề trong trái |
| `k-4100f0a8` | s01 | 3.3 · web · Cooldown | Khung «Kiểm tra email» +6 chữ | Lề trong trên |
| `k-1639fa12` | s06 | 3.3 · web · Cooldown | Khung «Chưa nhận được email?» +3 chữ | Cao |
| `k-dc4cc291` | s06 | 3.3 · web · Cooldown | Khung «Chưa nhận được email?» +3 chữ | Bo góc |
| `k-35694f4a` | s06 | 3.3 · web · Cooldown | Khung «Chưa nhận được email?» +3 chữ | Nền |
| `k-ea43175d` | s06 | 3.3 · web · Cooldown | Khung «Chưa nhận được email?» +3 chữ | Lề trong trái |
| `k-ba61f8a3` | s06 | 3.3 · web · Cooldown | Khung «Chưa nhận được email?» +3 chữ | Lề trong trên |
| `k-d5f165f3` | s06 | 3.3 · web · Cooldown | Nút «Gửi lại sau 42 giây» | Rộng |
| `k-b046ce2f` | s06 | 3.3 · web · Cooldown | Nút «Gửi lại sau 42 giây» | Nền |
| `k-13ef708a` | s06 | 3.3 · web · Cooldown | Nút «Liên hệ IT» | Rộng |
| `k-7f840f3f` | c08 | 3.3 · web · Cooldown | «Kiểm tra email» → «Nếu tài khoản có emai…» | Khoảng cách dọc |
| `k-7681afb3` | s06 | 3.3 · web · Cooldown | «Nếu tài khoản có emai…» → «Chưa nhận được email?» | Khoảng cách dọc |
| `k-293c4901` | s06 | 3.3 · web · Cooldown | «Chưa nhận được email?» → «Kiểm tra cả mục Thư r…» | Khoảng cách dọc |
| `k-976cf9be` | s06 | 3.3 · web · Cooldown | «Kiểm tra cả mục Thư r…» → «Gửi lại sau 42 giây» | Khoảng cách dọc |
| `k-1ed4439f` | s06 | 3.3 · web · Cooldown | «Gửi lại sau 42 giây» → «Liên hệ IT» | Xếp hàng |
| `k-3c87ac54` | s06 | 3.3 · web · Cooldown | «Liên hệ IT» → «Quay về đăng nhập» | Khoảng cách dọc |
| `k-abf1f37f` | s06 | 3.3 · web · Cooldown | Gửi lại sau 42 giây | Canh lề |
| `k-6658700f` | s06 | 3.3 · web · Cooldown | Đường kẻ ngang | Số lượng |
| `k-e918e5ea` | n12 | 3.3 · web · Cooldown | Icon refresh-cw cạnh «Gửi lại sau 42 giây» | Phần tử |
| `k-dbf15ab9` | d04 | 3.3 · web · Rate limited | Tài khoản: an.nguyen | Phần tử |
| `k-0fb5d1b7` | c02 | 3.3 · web · Rate limited | Nhập lại tên tài khoản | Phần tử |
| `k-b3fa91e4` | c08 | 3.3 · web · Rate limited | Kiểm tra email | Cỡ chữ |
| `k-264daa6a` | c08 | 3.3 · web · Rate limited | Kiểm tra email | Line-height |
| `k-32ab4cc1` | s06 | 3.3 · web · Rate limited | Chưa nhận được email? | Độ đậm |
| `k-e92aba66` | s06 | 3.3 · web · Rate limited | Kiểm tra cả mục Thư rác, rồi thử gửi lạ… | Line-height |
| `k-c03d8c40` | s06 | 3.3 · web · Rate limited | Kiểm tra cả mục Thư rác, rồi thử gửi lạ… | Màu chữ |
| `k-c02a72af` | s06 | 3.3 · web · Rate limited | Liên hệ IT | Gạch chân |
| `k-7fffbcf5` | s06 | 3.3 · web · Rate limited | Bạn đã gửi quá nhiều yêu cầu. Thử lại s… | Line-height |
| `k-de17e5a6` | s01 | 3.3 · web · Rate limited | Khung «Kiểm tra email» +7 chữ | Cao |
| `k-aab67874` | s01 | 3.3 · web · Rate limited | Khung «Kiểm tra email» +7 chữ | Viền |
| `k-7a3c007d` | s01 | 3.3 · web · Rate limited | Khung «Kiểm tra email» +7 chữ | Lề trong trái |
| `k-50a30aa7` | s01 | 3.3 · web · Rate limited | Khung «Kiểm tra email» +7 chữ | Lề trong trên |
| `k-831752f0` | s06 | 3.3 · web · Rate limited | Khung «Chưa nhận được email?» +4 chữ | Cao |
| `k-00c0dbd7` | s06 | 3.3 · web · Rate limited | Khung «Chưa nhận được email?» +4 chữ | Bo góc |
| `k-257f780a` | s06 | 3.3 · web · Rate limited | Khung «Chưa nhận được email?» +4 chữ | Nền |
| `k-368c63fc` | s06 | 3.3 · web · Rate limited | Khung «Chưa nhận được email?» +4 chữ | Lề trong trái |
| `k-2a423337` | s06 | 3.3 · web · Rate limited | Khung «Chưa nhận được email?» +4 chữ | Lề trong trên |
| `k-65faef64` | s06 | 3.3 · web · Rate limited | Nút «Gửi lại link» | Rộng |
| `k-6c11e14e` | s06 | 3.3 · web · Rate limited | Nút «Gửi lại link» | Nền |
| `k-4a24f658` | s06 | 3.3 · web · Rate limited | Nút «Liên hệ IT» | Rộng |
| `k-ea276df8` | c08 | 3.3 · web · Rate limited | «Kiểm tra email» → «Nếu tài khoản có emai…» | Khoảng cách dọc |
| `k-0aec2fa7` | s06 | 3.3 · web · Rate limited | «Nếu tài khoản có emai…» → «Chưa nhận được email?» | Khoảng cách dọc |
| `k-3b2620ee` | s06 | 3.3 · web · Rate limited | «Chưa nhận được email?» → «Kiểm tra cả mục Thư r…» | Khoảng cách dọc |
| `k-1e59b4c9` | s06 | 3.3 · web · Rate limited | «Kiểm tra cả mục Thư r…» → «Gửi lại link» | Khoảng cách dọc |
| `k-430563c8` | s06 | 3.3 · web · Rate limited | «Gửi lại link» → «Liên hệ IT» | Xếp hàng |
| `k-02e5d5f9` | s06 | 3.3 · web · Rate limited | «Bạn đã gửi quá nhiều …» → «Quay về đăng nhập» | Khoảng cách dọc |
| `k-7e304946` | s06 | 3.3 · web · Rate limited | Đường kẻ ngang | Số lượng |
| `k-d4b4041e` | d06 | 3.5 · web | Link đã hết hạn | Phần tử |
| `k-355d6a4c` | d06 | 3.5 · web | Quay về đăng nhập | Phần tử |
| `k-7c6dfc9a` | s01 | 3.5 · web | Khung «Link đặt lại mật khẩu đã hế…» +2 chữ | Cao |
| `k-149027a7` | s01 | 3.5 · web | Khung «Link đặt lại mật khẩu đã hế…» +2 chữ | Viền |
| `k-ef9af889` | s01 | 3.5 · web | Khung «Link đặt lại mật khẩu đã hế…» +2 chữ | Lề trong trên |
| `k-f7c22507` | n11 | 3.5 · web | «Gửi lại link» → «Liên hệ IT» | Khoảng cách dọc |
| `k-c6cf49c3` | d06 | 3.5 · web | Đường kẻ ngang | Số lượng |
| `k-68013269` | d06 | 3.5 · web | Icon icon/arrow-left | Phần tử |
| `k-232620ee` | m01 | 3.5 · web | Icon clock cạnh «Link đặt lại mật khẩu đ…» | Màu |
