# Tra cứu 39 tên phương tiện (SRS cũ LG) — đặc điểm nhận dạng để tinh chỉnh ảnh

Nguồn danh mục: `docs-input/srs-cu/lg-srs-export.md:5519-5583`. Tra ngày 09/10/2026.
Mức chắc: ✅ có nguồn tra được · 🟡 suy từ hiểu biết chung về dòng xe, chưa có nguồn · ❓ chưa rõ, cần hỏi khách.

## Khách đã trả lời (09/10/2026, qua user)

| Câu hỏi | Trả lời |
|---|---|
| "Giàn" là gì | Số trục bánh. Mooc 2 giàn = 2 trục, có thể là mooc **xương hoặc sàn** |
| Xe tải AC820 | Thaco Auman ~8,2 tấn ✅ |
| Xe tải TMT | Có 2 tải trọng: **7 tấn và 8 tấn** |
| "Olin 250" | Thaco Ollin 250 ✅ |
| Container thường | Đội có **20ft, 40ft, 45ft** |
| Container lạnh | Hiện chỉ có **45ft** |
| Đầu kéo Maxxforce | Đầu kéo Mỹ đầu dài — nhóm này gồm **Maxxforce và Cascadia** |
| Mooc 45ft | Đội **không dùng cổ cò** — mooc 45ft xương thẳng, 3 trục |
| Máy phát HP / BN, Trạm bơm dầu | Chưa trả lời |

## Ảnh thực tế đội xe (user gửi 09/10) — `refs/fleet/`, dùng làm tham chiếu dáng xe khi sinh ảnh

| File | Xe | Nhận dạng |
|---|---|---|
| n31-toyota-25t.png | Xe nâng Toyota 2.5T | Thân cam-đỏ, nắp + đối trọng xám đậm, khung bảo vệ hở (không cabin), cột 3 tầng đen, giá tựa + bộ chỉnh càng, lốp đặc xám, đèn xoay cam |
| n30-isuzu-qkr210.png | Isuzu QKR 210 | Cabin trắng hẹp, cản đen, thùng nhôm bạc |
| n29-ollin-700.png | Thaco Ollin 700 | Cabin trắng, dải tối trên kính, cánh gió nóc, lưới mạ crôm, thùng nhôm xám |
| n27-chenglong-m3.png | Chenglong M3 | Cabin bạc có cánh gió, lưới tổ ong đen, 2 trục, thùng trắng dài nhiều cửa hông |
| n26-auman-c240.png | Foton Auman C240 | Cabin trắng, lưới lưới thép đục lỗ hình chữ V (cùng dáng cabin Auman AC990) |
| n25-dongfeng-b180.png | Dongfeng (tạm hiểu là B180 — chờ xác nhận) | Cabin trắng, mảng lưới xám đậm |

Thùng xe trong đội chủ yếu là thùng kín nhôm màu bạc/trắng.

## Phát hiện cần xử lý ngay

| Mã | Tên SRS | Vấn đề | Ảnh hiện tại |
|---|---|---|---|
| 32 | Xe nâng Komatsu FB15RL-15 1.5T | Là **xe nâng điện đứng lái tầm với (reach truck)**, dài ~2 m, cột 3 tầng, càng dịch ngang ✅ | Sai — đang là xe nâng đối trọng ngồi lái |
| 31 | Xe nâng Toyota 2.5T | Dòng phổ biến Toyota 8FD25: xe nâng **đối trọng diesel**, khung bảo vệ hở (thường không cabin), màu cam Toyota ✅ | Lệch — đang có cabin kín màu vàng |
| 06 | Đầu kéo Maxxforce | MaxxForce là **động cơ** của International (Navistar); "đầu kéo Maxxforce" ở VN là đầu kéo Mỹ International ProStar — **đầu dài (mũi xe)**, không phải cabin lật 🟡 | Đầu kéo đại diện hiện là cabin lật |
| 10, 11 | Xe tải AC990, AC820 | AC990 = **Thaco Auman AC990 9 tấn**, cabin lật Foton Auman có giường ✅. AC820 nhiều khả năng cùng dòng Auman ~8,2 tấn ❓ | — |

## Bảng đầy đủ

| Mã | Tên SRS | Thực tế là | Đặc điểm nhận dạng (đưa vào câu lệnh) | Mức chắc |
|---|---|---|---|---|
| 00 | Phương tiện chưa xác định | — | Giữ hình giữ chỗ | — |
| 01 | Mooc 20ft | Sơ mi rơ moóc xương 20ft | Ngắn ~6,4 m, 1–2 trục, 4 chốt khoá | 🟡 |
| 02 | Mooc 40ft 2 giàn | Rơ moóc xương 40ft, 2 trục | "Giàn" = trục bánh ❓; dài ~12,4 m | 🟡 |
| 03 | Mooc 40ft 3 giàn | Rơ moóc xương 40ft 3 trục, 12 khoá (Thaco) | 3 trục, 12 chốt khoá (chở 2×20 hoặc 1×40) | ✅ |
| 04 | Mooc 45ft | Rơ moóc xương 45ft 3 trục (đội không dùng cổ cò) | Dầm thẳng, dài ~13,9 m | ✅ khách |
| 05 | Đầu kéo Maz | MAZ (Belarus), cabin lật | Mặt nạ lưới ngang, logo bò rừng; hay sơn xanh dương/đỏ | 🟡 |
| 06 | Đầu kéo Maxxforce | International ProStar (Mỹ) | Đầu dài, mũi khí động, cabin giường | 🟡 |
| 07 | Đầu kéo Hino 700 | Hino 700 (Nhật), cabin lật 6x4 | Đã đúng ở ảnh hiện tại | 🟡 |
| 08 | Đầu kéo Cascadia | Freightliner Cascadia (Mỹ) | Đầu dài, mũi tròn, đèn vuốt | 🟡 |
| 09 | Đầu kéo Chenglong H7 385PS | Dongfeng Chenglong H7, 385 mã lực | Cabin lật nóc cao, 6x4 | ✅ |
| 10 | Xe tải AC990 | Thaco Auman AC990, 9 tấn | Cabin lật có giường, thùng dài | ✅ |
| 11 | Xe tải AC820 | Có thể Thaco Auman ~8,2 tấn | Như AC990, nhỏ hơn | ❓ |
| 12 | Xe tải TMT | Cửu Long TMT (Việt Nam) | Chưa rõ dòng/tải trọng | ❓ |
| 13 | Xe tải Ollin 700A | Thaco Ollin (Foton) ~7 tấn | Cabin lật vuông, thùng kín | 🟡 |
| 14 | Xe tải Isuzu NQR75L | Isuzu N-series 5,5 tấn, khung dài | Đã đúng kiểu ảnh xe tải hiện tại | ✅ |
| 15 | Xe tải Ollin 450 | Thaco Ollin ~4,5 tấn | Cabin lật nhỏ hơn Ollin 700 | 🟡 |
| 16 | Xe Isuzu NQR66P | Isuzu N-series đời cũ | Cabin lật vuông | 🟡 |
| 17 | Xe Hyundai HD72 | Hyundai Mighty ~3,5 tấn | Cabin lật mặt tròn | ✅ |
| 18 | Xe Olin 250 | Có thể Thaco Ollin 250 (2,5 tấn) — SRS viết "Olin" | Xe tải nhẹ | ❓ |
| 19 | Xe Kia Frontier K165 | Thaco Kia K165, 2,4 tấn, thùng kín 3,5 m | Xe tải nhẹ cabin lật | ✅ |
| 20 | Xe Isuzu QKR 55H | Isuzu QKR tải nhẹ | Cabin lật nhỏ | 🟡 |
| 21 | Xe Kia Frontier 140 | Thaco Kia K140 ~1,4 tấn | Tải nhẹ | 🟡 |
| 22 | Xe Kia K2700 | Thaco Kia K2700 ~1,25 tấn | Tải nhẹ | 🟡 |
| 23 | Xe Isuzu NLR55 | Isuzu NLR tải nhẹ ~1,4 tấn | Cabin lật nhỏ | 🟡 |
| 24 | Xe tải Kia K3000 | Thaco Kia K3000 ~1,4 tấn | Tải nhẹ | 🟡 |
| 25 | Xe tải Dongfeng B180 | Dongfeng (Hoàng Huy) B180 ~9 tấn | Bản 2024: đèn mới, có cánh gió nóc | ✅ |
| 26 | Xe tải Auman C240 | Thaco Auman C240, 3 trục | Xe tải nặng 3 trục | 🟡 |
| 27 | Xe tải Chenglong M3 - 2024 | Chenglong M3 tải trung | 2 trục | 🟡 |
| 28 | Xe tải Chenglong H5 - 2024 | Chenglong H5 tải nặng | 3–4 trục | 🟡 |
| 29 | Xe tải Ollin 700 | Thaco Ollin ~7 tấn | Như 13 | 🟡 |
| 30 | Xe tải Isuzu QKR 210 | Isuzu QKR tải nhẹ ~1,9 tấn | Như 20 | 🟡 |
| 31 | Xe nâng Toyota 2.5T | Toyota 8FD25 diesel | Đối trọng, khung hở, cam Toyota | ✅ |
| 32 | Xe nâng Komatsu FB15RL-15 1.5T | Reach truck điện đứng lái | Thân ngắn, chỗ đứng lái bên hông, cột cao, càng vươn | ✅ |
| 33 | Container thường | Container khô | SRS không ghi 20ft hay 40ft | ❓ |
| 34 | Container lạnh | Container lạnh (reefer) | SRS không ghi 20ft hay 40ft | ❓ |
| 35 | Máy phát điện 25 KVA | Máy phát vỏ cách âm cỡ nhỏ | ~1,8 m | 🟡 |
| 36 | Máy phát điện 44 KVA (HP) | "HP" là hãng/đơn vị nào? | — | ❓ |
| 37 | Máy phát điện 45 KVA (BN) | "BN" là hãng/đơn vị nào? | — | ❓ |
| 38 | Trạm bơm dầu | Cột bơm cố định hay bồn + bơm di động? | — | ❓ |

## Câu hỏi cho khách (ban đầu — câu 4, 5 còn mở) (Nguồn khách: tài liệu SRS hệ thống LG — bảng "Tên phương tiện - Mã phương tiện - Loại phương tiện", màn Tạo mới DVKT)

1. "Giàn" trong "Mooc 40ft 2 giàn / 3 giàn" là số trục bánh?
2. Xe tải AC820 là dòng nào (Thaco Auman ~8,2 tấn?); Xe tải TMT là dòng/tải trọng nào; "Olin 250" có phải Thaco Ollin 250?
3. Container thường / lạnh của đội là 20ft, 40ft hay cả hai?
4. Máy phát 44 KVA (HP) và 45 KVA (BN): HP, BN nghĩa là gì?
5. Trạm bơm dầu là cột bơm cố định ở bãi hay bồn + bơm di động?
6. Đầu kéo Maxxforce có phải đầu kéo Mỹ International (đầu dài)?

## Nguồn

- Komatsu FB15RL-15 (reach, 1,5 t, 2.005 × 1.095 × 2.245 mm): https://biglemon.kenkey.jp/en/item/157787
- Toyota 62-8FD25 diesel 2,5 t: https://www.plantandequipment.com/equipment-items/2025-toyota-62-8fd25
- Thaco Auman AC990 9T: https://hanoma.vn/ban-xe-tai-thaco-auman-ac990-9t-chassis-15539.pro
- Thaco SMRM 45ft cổ cò 3 trục: https://thacoindustries.com/wp-content/uploads/2024/08/SMRM-San-3-truc-10-khoa-45.pdf
- Thaco SMRM 40ft 3 trục 12 khoá: https://thacoindustries.com/wp-content/uploads/2025/03/Leaflet-San-3-truc-12-khoa-40-Q345.pdf
- International ProStar + MaxxForce: https://www.worktruckonline.com/products/maxxforce-13-0l-with-scr
- Chenglong H7: https://fleet.ie/?p=6617
- Dongfeng B180 2024: https://www.kolesa.ru/news/dongfeng-s180-novaia-era-v-segmente-srednetonnaznyx-gruzovikov
- Kia Frontier K165 thùng kín: https://bonbanh.com/oto/kia-frontier-k165-thung-kin
- Hyundai HD72: https://www.truckdeal.com.ph/trucks/hyundai/hd/72-cargo
- Isuzu NQR75 (Isuzu Việt Nam): https://isuzu-vietnam.com/xetai/n-series/isuzu-truck-nqr75he5a-chassis/
