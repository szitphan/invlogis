# Quy chuẩn ảnh phương tiện — 2 mặt cắt, 1 hướng, 1 góc, 1 khung

Lập 09/10/2026 theo yêu cầu user. Áp cho mọi ảnh trong `assets/vehicles/b-ai/`. Chưa gọi API.

## 1. Hai mặt cắt bắt buộc cho mỗi phương tiện

| Mặt cắt | Tên file | Định nghĩa | Dùng ở |
|---|---|---|---|
| **Q — 3/4 trước** | `{mã}-q.png` | Đầu xe quay **phải**. Camera lệch ~35° khỏi trục hông về phía đầu xe: mặt trước chiếm ~1/3, hông ~2/3. Cao ~1,3 m (dưới kính lái, nhìn xuống 5–7°). Ống kính tele ~100 mm, ít méo phối cảnh. Chuẩn theo ảnh mẫu `refs/angle-q34-user.png` | Chi tiết, thẻ, ảnh thu nhỏ, chọn loại |
| **S — ngang vuông góc** | `{mã}-s.png` | Camera vuông góc với hông xe, ngang tâm bánh (0–2°). Đầu xe quay **phải**, **không** thấy mặt trước / mặt sau, bánh là hình tròn | Tổ hợp kéo, so sánh kích thước, dòng tóm tắt, danh sách ngang |
| Từ trên (giữ nguyên) | `{mã}-top.png` | Nhìn thẳng từ trên, đầu xe hướng **lên** | Marker bản đồ |

**Đảo trái/phải:** chỉ có 1 bản gốc quay phải; cần quay trái thì lật bằng CSS (`transform: scaleX(-1)`). Chữ/logo trên đầu xe sẽ bị ngược — chấp nhận ở cỡ UI.

**"Đầu" của vật không phải xe** (quay sang phải): mooc = đầu chốt kéo / chân chống · container thường = đầu cửa · container lạnh = đầu cụm máy lạnh · máy phát = đầu bảng điều khiển · cột bơm = mặt có màn số và vòi.

## 2. Khung chuẩn (máy làm sau khi tách nền — không phụ thuộc AI)

| Mặt cắt | Khổ | Vật lấp tối đa | Đường đáy (đế bánh) |
|---|---|---|---|
| Q | 1600 × 1000 | 90% rộng hoặc 82% cao | 94% chiều cao |
| S | 1800 × 720 | 92% rộng hoặc 80% cao | 93% chiều cao |

Mọi ảnh cùng khổ, cùng lề, cùng đường đáy → đặt cạnh nhau trên UI thẳng hàng. Vật căn giữa ngang. Nền trong suốt, không bóng.

## 3. Cách đảm bảo đồng nhất khi sinh

1. Mỗi lượt gửi Gemini **2 ảnh**: ảnh 1 = **chuẩn góc chụp** (Q: ảnh mẫu của user; S: ảnh ngang được duyệt ở bước pilot) · ảnh 2 = **ảnh thật đội xe** (nếu có) để lấy dáng xe.
2. Câu lệnh mặt cắt cố định (`CUT_VIEW` trong `gen_ai.py`), chỉ thay phần mô tả xe.
3. **Pilot trước:** 2 xe × 2 mặt cắt (Isuzu tải trung + Cascadia) ≈ 0,55 USD → user duyệt → lấy ảnh S đã duyệt làm chuẩn góc ngang cho cả bộ → chạy hàng loạt.
4. Sau khi sinh: soát hướng (đầu xe phải), soát góc bằng mắt, đặt khung chuẩn, tự kiểm trang.

## 4. Đánh giá bộ ảnh hiện tại theo quy chuẩn

- Toàn bộ 38 ảnh hiện tại sinh theo câu lệnh cũ ("3/4 từ bên phải", không chuẩn góc, không chuẩn khung) → **góc lệch nhau** (vd MAZ, Maxxforce gần chính diện; máy phát, cột bơm gần chính diện; container nghiêng nhiều) và **chưa có mặt cắt S** cho xe đơn.
- Tổ hợp: 4 ảnh đã gần mặt ngang (1×20, 2×20, 1×40, 45ft lạnh), ảnh "rỗng" đang là 3/4 → không đồng nhất.
- Ảnh từ trên (marker): đạt, giữ.
- ⇒ Đề xuất **sinh lại toàn bộ theo quy chuẩn** thay vì vá từng ảnh — vá sẽ không bao giờ đồng nhất.

## 5. Khối lượng

| Nhóm | Số đối tượng | Mặt cắt | Ảnh |
|---|---|---|---|
| Loại đại diện t01–t09 | 9 | Q + S | 18 |
| Ảnh theo tên n01, n03, n04, n05, n06, n08, n09, n12, n25, n26, n27, n29 | 12 | Q + S | 24 |
| Ảnh nhóm g-truck-s, g-truck-l, g-truck-l3, g-mooc-san | 4 | Q + S | 8 |
| Tổ hợp rỗng, 1×20, 2×20, 1×40, 45ft lạnh | 5 | S | 5 |
| **Tổng** | | | **55 ảnh ≈ 7,5 USD** (Pro, 1 phương án) |

Pilot 4 ảnh nằm trong 55 (không tốn thêm).

## 6. Cần user chốt trước khi gọi API

1. Góc 3/4 ~35° như ảnh mẫu — đúng ý chưa?
2. **Khoảng cách / cỡ:** (a) mỗi xe lấp khung như bảng Mục 2 (đẹp đều trên UI, mất tương quan kích thước) hay (b) giữ **tỉ lệ thật** giữa các xe (xe nâng nhỏ, tổ hợp dài) cho một số màn so sánh?
3. Tổ hợp: chỉ mặt S + từ trên, hay thêm Q?
4. Đảo trái/phải bằng CSS (logo ngược chữ) — chấp nhận?
5. Duyệt chạy **pilot 4 ảnh ≈ 0,55 USD** trước.

## 7. Lệnh (chỉ chạy sau khi user duyệt)

```
# pilot
python3 design/_lab/vehicles-src/gen_ai.py t03 n08 --cut both --model gemini-3-pro-image-preview
# hàng loạt (sau khi thêm ảnh S pilot vào ANGLE_REF["s"])
python3 design/_lab/vehicles-src/gen_ai.py t01 t02 t04 t05 t06 t07 t08 t09 n01 n03 n04 n05 n06 n09 n12 n25 n26 n27 n29 g-truck-s g-truck-l g-truck-l3 g-mooc-san --cut both --model gemini-3-pro-image-preview
python3 design/_lab/vehicles-src/gen_ai.py combo-0 combo combo-2 combo-40 combo-45 --cut s --model gemini-3-pro-image-preview
```
Soát trước bằng `--dry-run` (in câu lệnh, ảnh mẫu, chi phí — không gọi API).

## 8. Đối chiếu danh sách xe tải với ảnh trên mạng (09/10/2026)

Cách làm: ảnh đại diện trang đại lý/rao vặt (bonbanh, chotot, truckdeal…) đặt cạnh ảnh đang gán; ảnh mạng chỉ để soát, không lưu vào dự án.

| Mã · tên | Ảnh đang gán | Kết quả | Đề xuất |
|---|---|---|---|
| 19 Kia K165 · 21 Kia K140 · 22 Kia K2700 · 24 Kia K3000 | g-truck-s (dáng Isuzu QKR) | **Sai** — Thaco Kia Frontier: cabin hẹp, mặt trước bo tròn, đèn tròn, lưới Kia, thùng ngắn | Ảnh nhóm mới **g-kia** |
| 18 Ollin 250 | g-truck-s (Isuzu) | **Sai hãng** — thuộc họ Thaco Ollin (Foton) | Gán n29 (Ollin) |
| 13 Ollin 700A · 15 Ollin 450 · 29 Ollin 700 | n29 | Đúng họ Ollin (cabin Foton, lưới mạ) | Giữ |
| 14 NQR75L · 16 NQR66P | t03 (Isuzu N) | Đúng dáng Isuzu N-series | Giữ |
| 20 QKR 55H · 23 NLR55 · 30 QKR 210 | g-truck-s | Đúng họ Isuzu tải nhẹ | Giữ |
| 17 Hyundai HD72 | t03 (Isuzu) | **Sai hãng** — Hyundai Mighty, cabin mặt tròn khác Isuzu (không tải được ảnh trang, theo hiểu biết dòng xe) | Ảnh riêng **n17** |
| 10 AC990 · 11 AC820 | g-truck-l | **Sai dáng** — đã có ảnh thật AC990 (refs/fleet/n10-auman-ac990.png): cabin Auman đời cũ, cánh gió cao, lưới ngang đen | Sinh lại g-truck-l theo ảnh thật |
| 28 Chenglong H5 | g-truck-l3 | Gần đúng (Chenglong 3 chân, cabin lớn) | Giữ |
| 12 TMT · 25 B180 · 26 C240 · 27 M3 | ảnh riêng theo ảnh thật | Đúng | Giữ |

⇒ Thêm 2 đối tượng vào Mục 5: g-kia, n17 (× 2 mặt cắt = 4 ảnh ≈ 0,55 USD) → tổng 59 ảnh ≈ 8,1 USD. Đổi gán 18 → n29. AC990/AC820 chờ ảnh thật.

## 9. User đã chốt (09/10/2026)

1. Góc 3/4 ~35° như ảnh mẫu — đúng.
2. **Giữ tỉ lệ thật** giữa các xe → ảnh lưu cắt sát; kích thước thật (m) ở `vehicles-src/sizes.json`; trang hiển thị theo 1 tỉ lệ px/m chung (Q: bề ngang ≈ dài × 0,82 + rộng 2,5 m × 0,57).
3. Tổ hợp: **cả mặt ngang và 3/4**.
4. Lật trái/phải bằng CSS — được.
5. Pilot — duyệt. **Lần chạy pilot 09/10 bị 429 (chạm giới hạn chi tiêu tháng), chưa tốn phí.**
6. Sau loạt cuối: gom thành **1 trang HTML bản chốt**, bỏ các bản nháp cũ.

Khối lượng cập nhật: 27 đối tượng × 2 mặt cắt (thêm g-kia, n17) + 5 tổ hợp × 2 = **64 ảnh ≈ 8,8 USD** (gồm 4 ảnh pilot).

## 10. Tổ hợp kéo = ma trận mooc × hàng, máy ghép (đề xuất 09/10/2026, chờ duyệt)

User góp ý: thiếu tổ hợp với mooc khác (vd 40ft 3 giàn); ảnh "Mooc 40ft rỗng" cũ là góc 3/4, không phải mặt ngang.

- **18 tổ hợp hợp lệ** (xem ma trận trong `vehicle-mapping.html`): mooc 20ft × {rỗng, 1×20} · mooc 40ft 2 giàn / 40ft 3 giàn / sàn 40ft × {rỗng, 1×20, 2×20, 1×40} · mooc 45ft × {rỗng, 1×40, 1×45 thường, 1×45 lạnh}.
- **Mặt ngang + nhìn từ trên: máy ghép** từ ảnh từng phần cùng tỉ lệ thật (chốt kéo đặt lên mâm kéo, container khoá trên mooc) — 0 USD cho mỗi tổ hợp, ghép được với **bất kỳ đầu kéo nào** trong 5 đầu kéo.
- Phần cần sinh AI thêm: container **40ft thường** và **45ft thường** (Q + S = 4 ảnh); **ảnh nhìn từ trên** của 5 mooc, 4 container, 4 đầu kéo chưa có (13 ảnh).
- Tổng AI mới: 27 đối tượng × 2 mặt cắt (54) + 4 + 13 = **71 ảnh ≈ 9,7 USD**; bỏ 10 ảnh tổ hợp AI trong kế hoạch cũ.
- **Mặt 3/4 của tổ hợp**: máy không ghép đúng phối cảnh được → chờ user chọn (a) sinh AI cho vài tổ hợp hay dùng nhất, (b) ghép gần đúng, (c) dùng 3/4 của đầu kéo + nhãn tổ hợp.
- Màu container mặc định khi ghép: 20ft đỏ gỉ, 40ft xanh dương, 45ft thường xám, 45ft lạnh trắng.

## 11. User chốt tổ hợp (09/10/2026)

1. **Máy ghép** mặt ngang + nhìn từ trên cho 18 tổ hợp — đồng ý.
2. **Mặt 3/4 của tổ hợp** = ảnh 3/4 của đầu kéo + **nhãn tổ hợp** (vd "Mooc 40ft 3 giàn · 2 × 20ft") — không sinh AI cho tổ hợp.
3. **Container toàn trắng** (khô 20/40/45ft và lạnh 45ft). Để thấy rõ 2 container: khe hở ~0,3 m (tỉ lệ thật) + khung đầu và 4 góc thép xám đậm ở mỗi container + vách gân ngắt ở chỗ nối; ảnh từ trên: 2 nóc tách bằng vạch. Khô = vách gân dọc; lạnh = vách phẳng + cụm máy lạnh ở đầu.

Đã cập nhật câu lệnh: t06 (20ft trắng), thêm c40, c45 (trắng) + kích thước trong `sizes.json`. Khối lượng AI giữ 71 ảnh ≈ 9,7 USD (Mục 10). Máy ghép (`vehicles-src/compose.py`) sẽ viết khi đã có ảnh từng phần.

## 12. Duyệt sơ đồ lốp (09/10/2026, file góp ý của người duyệt)

- Xác nhận đúng: 34/38 dòng đã map. Sửa: **05 MAZ = 4x2 (kiểu 2)** · **10 AC990 = 3 trục 2 dí 1 cầu (kiểu 5)**, tách khỏi AC820 (vẫn 2 trục) · **28 Chenglong H5 = 4 trục 2 dí 2 cầu (kiểu 6)** · **38 Trạm bơm = trụ bơm + téc chứa + container 20ft bảo vệ**, không lốp.
- Ảnh phải sinh lại theo đó: n05 (MAZ 4x2), **n10 (AC990 3 trục — mới)**, **n28 (H5 4 trục — mới, thay g-truck-l3)**, t09 (trạm bơm trong container 20ft).
- Khối lượng loạt chính cập nhật: 28 đối tượng × Q+S (56) + 13 ảnh từ trên = **69 ảnh ≈ 9,5 USD**.
- Kiểu 7 (5 trục, 17 lốp) vẫn chưa có xe nào → hỏi khách giữ hay bỏ.

## 13. Kết quả loạt chính (09/10/2026)

- Đã sinh: 56/56 ảnh Q+S + 3/13 ảnh từ trên (n01, t01, n03) ≈ 8,1 USD. 10 ảnh từ trên còn lại bị 429 (chạm giới hạn chi tiêu) — chưa tốn phí.
- Lật 6 ảnh quay ngược (không gọi API): t05-q, n12-q, n17-q, n28-q, t01-s, g-truck-l-s.
- **Lỗi của Claude:** lệnh thay mô tả t06 khớp nhầm vào FRONT_OF → t06 vẫn đỏ, mất định nghĩa "đầu" của t07/t08/t09. Đã sửa (`gen_ai.py` FRONT_OF + SUBJECT).
- Sai nội dung, cần sinh bù (10 ảnh): t06-q/-s (cont 20ft phải trắng) · t07-q/-s (cont lạnh bị gắn lên xe/mooc → phải đứng riêng) · n10-q/-s (AC990 ra 4 trục → phải 3: 2 lái + 1 tải) · n26-s (C240 ra 4 trục → 3: 1 lái + 2 tải) · t08-s (máy phát có bánh → đặt trên đế) · t09-q (ra xe tải chở téc → container trạm bơm) · g-truck-s-q (lọt phông studio).
- Cộng 10 ảnh từ trên còn thiếu: n04, g-mooc-san, t06, t07, c40, c45, n05, n06, n08, n09.
- **Đợt bù: 20 ảnh ≈ 2,7 USD.** Lệnh:
  `gen_ai.py t06 t07 n10 --cut both` · `gen_ai.py t08 n26 --cut s` · `gen_ai.py t09 g-truck-s --cut q` · `gen_ai.py n04-top g-mooc-san-top t06-top t07-top c40-top c45-top n05-top n06-top n08-top n09-top` (tất cả `--model gemini-3-pro-image-preview`).

## 14. Bản chốt (09/10/2026)

- Đợt bù chạy xong (20 ảnh; 8 ảnh đầu bị 429 rồi chạy lại thành công). Xoay 3 ảnh từ trên (n05, n06, n08). Mọi ảnh -q/-s/-top cắt SÁT mép (không viền) để ghép đúng kích thước.
- `vehicles-src/compose.py` ghép 18 tổ hợp với Hino → `assets/vehicles/b-ai/cb-{mooc}-{hàng}-t02-{s|top}.png`; sàn mooc đo theo hàng phủ > 50% chiều dài (bỏ qua vách chắn mooc sàn).
- Trang bản chốt: `vehicles-final.html` (danh mục 39 tên Q+S + sơ đồ lốp, dàn tỉ lệ thật, ma trận 18 tổ hợp ghép trong trình duyệt với ô chọn 5 đầu kéo, nút lật trái). Bản gửi: `vehicles-final-share.html`. Dựng lại: `python3 design/_lab/vehicles-src/build_final.py [--share]`.
- Còn sai: **n10 AC990** vẫn ra 4 trục (cần 3: 2 lái + 1 tải) ở cả 2 mặt cắt; **n26-s C240** ra 2 trục (cần 3). Mooc 3 trục ở ảnh từ trên chỉ 2 trục (chấp nhận ở cỡ marker).
- 09/10 sửa nốt bằng chế độ chỉnh ảnh (`gen_ai.py --edit`, lệnh trong EDITS, bản gốc lưu `raw/{tag}-before-edit.png`): n10-q, n10-s → 3 trục (2 lái + 1 tải); n26-s → 3 trục (1 lái + 2 tải). Đã dựng lại bản chốt + bản gửi. **Bộ ảnh đã đủ và đúng theo duyệt.**

## 15. Sửa M3 / container ngang / thử tổ hợp Flash (09/10/2026)
- n27 (M3) q,s: chỉnh thùng thành 6 cánh nhôm phẳng theo ảnh thật (Pro, `--edit`).
- t06-s, c45-s, t07-s: chỉnh về mặt ngang thật, mẫu góc = c40-s (Pro, `--edit` + EDIT_REF). Đạt.
- 18 tổ hợp AI nguyên khối bằng **Flash** (17 ảnh trước khi hết credit, lỗi 402 "prepayment credits depleted"): **không đạt** — Flash vẽ xe tải thân liền chở container trên sát-xi, không có đầu kéo + sơ mi rơ mooc tách rời. Đã chuyển sang `assets/vehicles/_rejected-flash-combos/`, trang bản chốt vẫn dùng tổ hợp máy ghép.
- Đề xuất: sinh lại tổ hợp bằng **Pro** (18 ảnh ngang ≈ 2,5 USD) sau khi nạp credit; mô tả đã có trong `gen_ai.py` (SUBJECT cb-*).

## 16. Dọn kho (09/10/2026)
- Tổ hợp kéo **tạm gác** theo user: bỏ mục tổ hợp khỏi trang bản chốt, bỏ compose.py, SUBJECT cb-*, ảnh combo/cb-*.
- Đã dời ra ngoài dự án (kho tạm phiên): lab-vehicles.html/.js (SVG nháp), vehicle-mapping.html, ảnh không theo quy chuẩn (t0X.png, n*.png, -flash, -pro, -th, -xs, combo*), raw tương ứng, ảnh tổ hợp Flash bị loại.
- Còn lại: `assets/vehicles/b-ai/` 77 ảnh (-q/-s/-top), `vehicles-src/` (gen_ai, vehlib, build_final, build_share, final-template, sizes.json, raw 77, usage.log). Trang: `vehicles-final(.html|-share.html)`, `tyre-mapping(.html|-share.html)` (đã chuyển sang ảnh -q, gán đúng tên theo duyệt).
- Việc sau: đưa mục 1 (danh mục 39 tên) + mục 2 (dàn tỉ lệ thật) lên Figma; tổ hợp kéo làm lại sau (Pro, khi có credit).

## 17. Đưa lên Figma (09/10/2026)
- File "[innvie] invlogis v0.3", trang 🧪 Sandbox: frame `5464:95538` "Phương tiện — Danh mục 39 tên (SRS)" và `5464:95849` "Phương tiện — Dàn xe tỉ lệ thật" (40 px/m).
- Cách làm: reqwise dựng bố cục với 108 ô `img:{key}` → Figma MCP chính thức `upload_assets` (nodeIds, scaleMode FIT) + POST multipart ảnh từ `assets/vehicles/figma-import/` (≤900 px).
- Lưu ý: ảnh container 40ft/45ft mặt ngang có tỉ lệ cao/dài lớn hơn thật (c40-s ≈ 3,9 m cao, c45-s ≈ 5,9 m) nên ở dàn tỉ lệ thật trông quá cao → cần chỉnh lại ảnh (Pro --edit) khi có credit.
