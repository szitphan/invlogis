# Landing page Invlogis (việc 3.2, Mốc 3)

Bản nháp, tĩnh, tự đủ (không request ngoài). Token từ `design/brand/invlogis/brand-tokens.css`.

## Cấu trúc
```
index.html          Việt
en/index.html       English
assets/             site.css, site.js, brand-tokens.css, fonts/ (Lexend, Be Vietnam Pro, JetBrains Mono),
                    logo/ (logo, favicon, apple-touch), bg/ (n6, n3, r1), og-image-vi.png, og-image-en.png
previews/           {vi,en}-{desktop-1440,mobile-390}.png (toàn trang, đã tắt chuyển động -> demo ở trạng thái cuối)
```
Hai trang sinh từ cùng một khung; sửa chữ thì sửa cả hai file.

## Xem thử
`cd design/brand/_drafts/m3/web && python3 -m http.server 8080` rồi mở `http://localhost:8080/` (mở thẳng file cũng chạy).

## Ghi chú thiết kế
- Hero nền `n6`, dải vision/AI nền `n3`; dải ra mắt trên cùng dùng `r1` (chỉ dải ra mắt, gỡ sau ra mắt).
- Chữ trắng chỉ ở vùng tối của nền (`_contrast.json`: n6 11,5:1, n3 7,2:1); không có chữ trên vùng 56–70%. Chip kính tối cho chữ nhỏ.
- Sáng/tối theo `prefers-color-scheme`; logo đổi cặp primary/reverse. Hero, vision, thẻ AI luôn tối.
- Demo "AI đọc chứng từ": CSS/JS, chạy khi cuộn tới, lặp; `prefers-reduced-motion` hoặc tắt JS thì hiện sẵn trạng thái cuối. Một trường cố ý gắn `[kiểm lại]` để thể hiện minh bạch. Dữ liệu là mẫu minh hoạ, không phải chứng từ thật.
- Demo có nút "Tạm dừng minh hoạ" (WCAG 2.2.2), tự dừng sau 3 vòng và có "Phát lại"; giảm chuyển động thì hiện trạng thái cuối, không có nút.
- Form chỉ front-end (`preventDefault`, hiện lời cảm ơn), chưa gửi đi đâu.
- Khách ẩn danh: "một doanh nghiệp vận tải container, khoảng 110.000 lô/năm" (DEC-060).

## Copy deck
| | VI | EN |
|---|---|---|
| H1 | Khai mở cách vận hành mới. | Open a new way to operate. |
| Subline | Invlogis đọc chứng từ Việt Nam — Booking Note, eDO, EIR, phiếu cân — vào thẳng hồ sơ lô hàng. Bạn kiểm tra, bấm lưu; dữ liệu đi tiếp sang điều vận, xưởng, dầu và công nợ. | Invlogis reads Vietnamese shipping documents — Booking Notes, eDOs, EIRs, weigh slips — straight into the shipment file. You review and save; the data carries on into dispatch, workshop, fuel and receivables. |
| Vấn đề | Mỗi lô hàng đi qua nhiều tờ giấy — và nhiều lần gõ lại. (thẻ: DEM, DET, giấy về chậm, Excel/Zalo) | Every shipment passes through many papers — and gets re-typed many times. |
| Cách hoạt động | Ba bước, một dữ liệu. (Chứng từ vào · AI đọc · Bạn duyệt, dữ liệu đi tiếp) | Three steps, one set of data. (Document in · AI reads · You review, data moves on) |
| Nền tảng | Một nền tảng, nhiều module chung một dữ liệu. | One platform, many modules, one set of data. |
| Giá trị | Chúng tôi làm việc theo ba điều. Minh bạch · Đáng tin cậy · Đổi mới | We work by three things. Transparent · Reliable · Innovative |
| Bằng chứng | Đã chạy thật, ở quy mô thật. ~110.000 lô hàng mỗi năm | Already running, at real scale. ~110,000 shipments a year |
| Tầm nhìn | Từ vận hành bằng kinh nghiệm sang vận hành bằng dữ liệu và AI agent. | From running on experience to running on data and AI agents. |
| Liên hệ | Xem Invlogis đọc chính chứng từ của bạn. | See Invlogis read your own documents. |
| CTA | Đặt lịch demo | Book a demo |

## Chỗ còn trống (`[chờ: …]`)
Ngày ra mắt · thời lượng demo · địa chỉ, MST, email, tên pháp nhân innvie · khách đồng ý nêu tên (BL-056) · số đo tỷ lệ trường AI phải sửa tay · lộ trình màn lãi lỗ theo lô · tên miền (og:url, canonical, URL tuyệt đối của og:image).

## Vòng sửa R4a
Sửa: href `##`, aria-label nav, mục Vấn đề viết lại theo docs, Giá trị một ngôn ngữ, placeholder ngắn (ghi chú nội bộ chuyển thành comment HTML), nút tạm dừng, eyebrow nêu đối tượng, "Khoảng 110.000", dòng "Phù hợp với", ngày mẫu 12/10/2026, thẻ Điều vận có viền nhấn.
Chưa làm: liên kết chính sách quyền riêng tư, thông báo lỗi từng ô, gộp Giá trị + Bằng chứng cho trang mobile ngắn hơn.
Kiểm trước khi đăng: `grep -c "\[chờ" index.html en/index.html` phải = 0.

Nguồn mục Vấn đề (chỉ dùng cái docs xác nhận): `docs/_product/prd.md` Mục 2 (lưu container, lưu vỏ, giấy về chậm, Excel/Zalo); `docs/cross-process-flow` (DEM = hàng nhập nằm cảng quá hạn miễn phí; DET = từ giờ trên EIR tới trả vỏ đúng nơi hãng chỉ định); ePort: PRD Mục 5 (không kết nối máy, chỉ danh sách việc + kết quả).

## Câu hỏi mở
1. Khẩu hiệu làm H1 (DEC-072) hay dùng "Chứng từ vào. Hồ sơ sẵn." làm H1, khẩu hiệu xuống dải phụ?
2. Có giữ dải ra mắt r1 ở đầu trang, hay chỉ bật từ ngày ra mắt?
3. Tên module "Dầu", "Xưởng" có nên nói là "gói bán thêm" ngay trên trang không?
4. Chưa xác nhận với khách, nên chỉ nói trung tính: cách tính DEM/DET theo từng hãng tàu; thẻ "Phí lưu container" dùng đúng chữ docs (DEM) nhưng chưa có số tiền; ePort chỉ nhắc ở thẻ Điều vận (giữ danh sách việc + kết quả), không nói thao tác cụ thể ở Cát Lái/Hải Phòng. Ai kiểm thuật ngữ với khách trước khi đăng?
5. Form gửi về đâu (email, CRM)? Cần chính sách quyền riêng tư.
6. Số ~110.000 lô/năm: được phép dùng công khai chưa?
