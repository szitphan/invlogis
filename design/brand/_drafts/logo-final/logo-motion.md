---
type: brand-logo
status: draft
updated: 2026-10-14
links:
  - design/brand/_drafts/logo-final/logo-motion.html
---

# Logo động (splash)

File `logo-motion.html` chỉ dùng CSS, logo nhúng sẵn dạng SVG nét, không cần thư viện. Nút "Chạy lại" chỉ để xem thử.

**Ý tưởng:** dải lụa kéo lên thành thân chữ i, phần đầu dải gập lên thành chấm, sau đó tên hiện ra.

| # | Phần | Bắt đầu | Thời lượng | Chuyển động | Đường cong |
|---|---|---|---|---|---|
| 1 | Thân i | 0 ms | 700 ms | Dài ra từ chân lên: `scaleY 0 → 1`, gốc ở cạnh đáy | `cubic-bezier(.22,1,.36,1)`, ra nhanh rồi chậm dần như lụa căng |
| 2 | Chấm i (nếp gấp) | 450 ms | 700 ms | Lật quanh cạnh đáy: `scaleY −1 → 1`. Lúc đầu mảnh lụa úp xuống, sau đó gập lên vị trí. Độ mờ 0 → 1 trong 25% đầu. | `cubic-bezier(.65,0,.35,1)`, vào chậm, giữa nhanh, ra chậm |
| 3 | n v l o g i s | 900 ms, mỗi chữ trễ thêm 70 ms | 550 ms mỗi chữ | Hiện dần và trượt từ trái sang 60 đơn vị (≈ 6% em) | `cubic-bezier(.16,1,.3,1)` |

**Tổng thời gian:** khoảng 1,9 giây (chữ s bắt đầu ở 1.320 ms và xong ở 1.870 ms), dưới giới hạn 2,5 giây. Nên giữ logo tĩnh thêm 300–500 ms rồi mới chuyển màn.

**Giảm chuyển động:** khi người dùng bật `prefers-reduced-motion: reduce`, không chạy bước nào ở trên. Cả logo chỉ hiện dần trong 200 ms.

**Đã kiểm:** dừng ở 250 / 600 / 900 / 1.300 / 2.000 ms (dùng Web Animations, chụp bằng Chrome headless). Thứ tự hiện là: thân, chấm gập, tên. Khung cuối trùng với `invlogis-primary.svg`.

**Khi lên app:** splash nền tối thì thay SVG bên trong bằng `invlogis-reverse.svg`, vẫn giữ `class="ii"` / `data-part` cho chữ i và `class="lt"` cho các chữ còn lại. Trên mobile gốc (Lottie/Rive), dựng lại theo đúng bảng thời gian trên.
