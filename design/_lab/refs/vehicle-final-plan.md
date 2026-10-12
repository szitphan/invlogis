# Bản kế hoạch sinh ảnh cuối — chạy 1 lần sau khi duyệt

Lập 09/10/2026. Chưa gọi API. Soát câu lệnh: `python3 design/_lab/vehicles-src/gen_ai.py <tên...> --model gemini-3-pro-image-preview --dry-run`.
Nguồn quyết định: `refs/vehicle-refs.md` (tra cứu + trả lời khách) và ảnh thực tế đội xe `refs/fleet/`.

## 1. Ảnh sẽ sinh mới (21 ảnh, model Pro)

| Ảnh | Nội dung | Tham chiếu ảnh thật |
|---|---|---|
| t04 | Xe nâng Toyota 2.5T — thân cam-đỏ, khung bảo vệ hở, cột 3 tầng, bộ chỉnh càng, lốp đặc | n31-toyota-25t |
| t04-top | Như t04, nhìn từ trên (marker) | — |
| t05 | Komatsu FB15RL-15 — xe nâng điện đứng lái tầm với (reach), thân xanh coban | — |
| t07 | Container lạnh **45ft** | — |
| n01 | Mooc xương 20ft, 2 trục | — |
| n03 | Mooc xương 40ft, 3 trục, 12 chốt | — |
| n04 | Mooc xương **45ft thẳng** (không cổ cò), 3 trục | — |
| n05 | Đầu kéo MAZ — cabin lật xanh | — |
| n08 | Đầu kéo Mỹ đầu dài — dùng cho **Maxxforce và Cascadia** | — |
| n09 | Đầu kéo Chenglong H7 — cabin nóc cao xám bạc | n09-chenglong-h7-crop (cắt từ nền ảnh xe nâng) |
| g-truck-s | Xe tải nhẹ — dáng Isuzu QKR 210, thùng nhôm bạc | n30-isuzu-qkr210 |
| n29 | Thaco Ollin 700 | n29-ollin-700 |
| n27 | Chenglong M3 — thùng dài nhiều cửa hông | n27-chenglong-m3 |
| n26 | Foton Auman C240 — 3 trục | n26-auman-c240 |
| n25 | Dongfeng (B180) | n25-dongfeng-b180 |
| g-truck-l | Tải nặng 2 trục dáng Auman (AC990, AC820, TMT) | n26-auman-c240 (lấy dáng cabin) |
| g-truck-l3 | Tải nặng 3 trục (Chenglong H5) | — |
| combo | Tổ hợp: mooc 40ft chở 1 × 20ft **thường** | — |
| combo-top | Như combo, nhìn từ trên | — |
| combo-45 | Tổ hợp: mooc 45ft thẳng chở 1 × 45ft **lạnh** | — |
| combo-45-top | Như combo-45, nhìn từ trên | — |

Chi phí: 21 × ≈0,137 USD ≈ **2,9 USD** (1 phương án/ảnh) · ≈ 5,8 USD nếu 2 phương án/ảnh để chọn mà không cần chạy lại.

## 2. Giữ ảnh hiện có (không sinh lại)

t01 (mooc 40ft 2 trục) · t02 (Hino 700) · t03 (Isuzu NQR — tải trung) · t06 (container thường 20ft) · t08 (máy phát) · t09 (cột bơm) · combo-0 / combo-2 / combo-40 (+ -top) · t02-top · t03-top.

## 3. Tên SRS → ảnh dùng

| Mã | Tên | Ảnh |
|---|---|---|
| 00 | Chưa xác định | hình vẽ giữ chỗ |
| 01 · 02 · 03 · 04 | Mooc 20ft · 40ft 2 giàn · 40ft 3 giàn · 45ft | n01 · t01 · n03 · n04 |
| 05 · 06 · 07 · 08 · 09 | Maz · Maxxforce · Hino 700 · Cascadia · Chenglong H7 | n05 · n08 · t02 · n08 · n09 |
| 10 · 11 · 12 | AC990 · AC820 · TMT | g-truck-l |
| 13 · 15 · 29 | Ollin 700A · Ollin 450 · Ollin 700 | n29 |
| 14 · 16 · 17 | Isuzu NQR75L · NQR66P · Hyundai HD72 | t03 |
| 18–24, 30 | Ollin 250, Kia K165/140/K2700/K3000, Isuzu QKR 55H/NLR55/QKR 210 | g-truck-s |
| 25 · 26 · 27 · 28 | Dongfeng B180 · Auman C240 · Chenglong M3 · Chenglong H5 | n25 · n26 · n27 · g-truck-l3 |
| 31 · 32 | Toyota 2.5T · Komatsu FB15RL-15 | t04 · t05 |
| 33 · 34 | Container thường · Container lạnh | t06 · t07 |
| 35–37 · 38 | Máy phát · Trạm bơm dầu | t08 · t09 |

## 4. Cần chốt trước khi chạy

1. Ảnh thứ 6 (Dongfeng cabin trắng) có phải **Dongfeng B180** (mã 25)?
2. Mooc 2 giàn: giữ ảnh mooc **xương** hiện có, hay cần thêm ảnh mooc **sàn**?
3. Máy phát (HP/BN) và trạm bơm dầu: giữ ảnh hiện tại?
4. TMT 7–8 tấn dùng chung dáng Auman — đồng ý, hay gửi ảnh TMT thật?
5. Ollin 450 / 700A dùng chung ảnh Ollin 700 — đồng ý?
6. Màu thật của đầu kéo MAZ (đang để xanh), Maxxforce/Cascadia (trắng), Hino 700 (trắng) — nếu có ảnh đội xe thì gửi thêm (cả AC990, Chenglong H5).
7. 1 hay 2 phương án mỗi ảnh; nâng giới hạn chi tiêu tháng của dự án Google ≥ 3 USD (1 phương án) hoặc ≥ 6 USD (2 phương án).

## 5. Lệnh chạy (sau khi chốt)

```
python3 design/_lab/vehicles-src/gen_ai.py t04 t04-top t05 t07 n01 n03 n04 n05 n08 n09 g-truck-s n29 n27 n26 n25 g-truck-l g-truck-l3 combo combo-top combo-45 combo-45-top --model gemini-3-pro-image-preview
```
Thêm `--tries 2` nếu chọn 2 phương án. Sau khi chạy: soát hướng xe (ảnh từ trên đầu xe hướng lên, ảnh ngang đầu xe quay phải), xoay/lật nếu cần, `--rekey`, tự kiểm trang lab.

## 6. Kết quả chạy (09/10/2026)

- Đã chạy 23 ảnh theo kế hoạch + 5 ảnh bù có ảnh thật (MAZ, Maxxforce = n06 riêng, Cascadia = n08, Toyota khung hở, máy phát Shindaiwa 25 kVA) = 28 lượt Pro ≈ 3,8 USD.
- Chỉnh sau khi sinh (không gọi lại API): lật 4 ảnh quay trái, xoay 3 ảnh nhìn từ trên; bỏ đèn studio lọt khung (n03); ngưỡng tách nền tự theo độ xanh của nền (sửa MAZ bị khoét).
- Quyết định khi chạy: cabin đầu kéo / xe tải sơn trắng trung lập, giữ dáng + lưới + logo hãng; xe nâng, container, máy phát giữ màu thật.
- Bộ chốt: 38 ảnh trong `assets/vehicles/b-ai/` (không tính bản -flash/-pro so sánh và ảnh thu nhỏ -th/-xs).
