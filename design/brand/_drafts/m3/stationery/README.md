# Văn phòng phẩm Invlogis (Mốc 3, nhiệm vụ 3.4)

Bản nháp trong `_drafts/m3/stationery/`. Chưa chuyển sang `design/brand/` (chờ founder duyệt mốc). Mọi thông tin pháp nhân là chỗ trống `[chờ: ...]`, tô nền đào nhạt, KHÔNG bịa.

## Danh sách file
| Thư mục | File | Ghi chú |
|---|---|---|
| `business-card/` | `business-card-print.pdf` | 2 trang (trước, sau), trang 112×77 mm: cắt 90×55 mm, tràn lề 3 mm, dấu cắt ngoài vùng tràn lề |
| | `business-card-front.png`, `-back.png` | xem trước 1020×624 px (cỡ cắt) |
| | `card.print.html`, `card.preview.html` | nguồn sửa tay, mở bằng Chrome |
| `letterhead/` | `letterhead.docx`, `letterhead.pdf` | A4, header logo + thông tin, footer pháp nhân + số trang |
| `email-signature/` | `signature-vi.html`, `signature-en.html`, `logo-by-innvie-email.png`, `*-preview.png`, `install-notes.md` | bảng, style inline, rộng 600 |
| `quotation/` | `bao-gia-template.docx` (+ `.pdf`) | báo giá trang trọng, VI chính, nhãn EN phụ |
| `contract/` | `hop-dong-template.docx` (+ `.pdf`) | khung hợp đồng 9 điều; mọi thân điều khoản gắn `[Cần luật sư duyệt]` |
| `envelope/` | `envelope-dl.pdf`, `envelope-dl-preview.png` | DL 220×110 mm |
| `previews/` | `contact-sheet.png` | |
| `assets/` | logo SVG+PNG, phông, nền | bản sao từ `design/brand/invlogis/` |
| `_src/` | `build_print.py`, `build_docs.py`, `build_content.py`, `build_extra.py` (email, phong bì, TrimBox/BleedBox), `build_sheet.py`, `doc.css` | dựng lại toàn bộ (thứ tự: print, content, extra, sheet) |

Mỗi `.docx` có bản `-arial.docx` dùng Arial khi máy chưa cài phông.

## Thông số in
- Danh thiếp: 90×55 mm, tràn lề 3 mm, dấu cắt đen 0,1 mm; giấy đề xuất 350 gsm mịn. Nền mặt trước là ảnh nền chàm đêm (`bg-n1`, 1920×1080); ảnh nền 1920×1080 phủ 96 mm tương đương khoảng 500 dpi, dải gradient ít chi tiết nên đủ. Màu trong PDF là RGB, nhà in cần chuyển CMYK và so thử màu cobalt `#2F43DB`.
- Logo trên danh thiếp: lockup "by innvie" rộng 41 mm (cao ~15 mm, quy chuẩn tối thiểu 12 mm), chừa trống hơn 1x mọi phía.
- Giấy tiêu đề: A4, lề trái/phải 22 mm, logo cao 13 mm. In offset hoặc laser đều được, không có nền tràn lề.
- Phong bì DL: cắt 220×110 mm, tràn lề 3 mm (trang 226×116 mm, TrimBox/BleedBox đã đặt, chưa có dấu cắt); dải gradient 3 mm sát mép phải kéo tràn lề.
- Vùng an toàn logo (`logo-spec.md` Mục 2, 1 x ≈ 0,52 chiều cao phần chữ logo; lockup "by innvie" cao 13 mm có phần chữ ~10 mm nên 1 x ≈ 5 mm): kẻ tiêu đề giấy tờ cách logo 6 mm, địa chỉ phong bì cách logo ≥ 8 mm, email chừa 22 px dưới logo và 12 px (0,5 x) bên trái.
- Màu chỉ lấy từ `brand-tokens.css`: nền placeholder = peach `#FFD3C0`, đường kẻ = periwinkle nhạt `#C4CDFF`.
- Ghi chú dùng: thân giấy tiêu đề viết Be Vietnam Pro 10,5 pt, giãn dòng 1,35, căn đều hai bên.
- Chữ tối thiểu in: 7 pt (danh thiếp, kể cả nhãn T/E/W), 7,5 pt (chân trang); tương phản chữ xám chàm/giấy 6,97:1, chữ mực/nền vàng placeholder 15,7:1, trắng/chàm đêm 18,5:1 (`contrast.py`).

## Cách sửa
- DOCX: mở bằng Word, sửa header/footer (nhấp đúp vùng đầu trang). Phông: Be Vietnam Pro (thân), Lexend (tiêu đề); file phông trong `assets/fonts/` (OFL). Thiếu phông thì dùng bản `-arial`.
- Điền placeholder: tìm `[chờ`. Chỗ nền đào là phải thay trước khi dùng; xoá nền đào sau khi thay.
- Dựng lại PDF/DOCX: `python3 _src/build_content.py` (tài liệu), `python3 _src/build_print.py` (danh thiếp). Lưu ý: PDF xem trước của DOCX được dựng từ bản HTML sinh đôi, không phải do Word xuất; bố cục có thể lệch nhẹ so với Word. Không có LibreOffice/Word trong môi trường dựng nên chưa kiểm DOCX trực tiếp; số trang trong PDF xem trước chưa hiện, trong DOCX có "Trang X / Y".

## Kiểm
- Dấu tiếng Việt: Be Vietnam Pro 400 đủ glyph (`vn_glyphs.py`); các bản xem trước hiển thị đúng.
- Logo: đúng bản (lockup trên nền sáng; reverse trên nền tối), không kéo méo.

## Câu hỏi mở
1. Tên pháp nhân đầy đủ, địa chỉ, MST, số điện thoại, domain (OQ chung với BL thương hiệu).
2. innvie là pháp nhân bán hàng/ký hợp đồng, hay một pháp nhân khác? Hiện lockup "by innvie" đặt trên mọi giấy tờ; không làm danh thiếp riêng cho innvie vì brief coi innvie chỉ là chữ ký (Mục 2). Cần bản riêng thì báo.
3. Báo giá/hợp đồng: có cần bảng đa tiền tệ, VAT theo dòng khác nhau, phụ lục SLA mẫu không?
4. Danh thiếp: có thêm QR, LinkedIn, mặt sau song ngữ không? Hiện chỉ T/E/W/địa chỉ.
5. Luật sư duyệt toàn bộ điều khoản hợp đồng và điều khoản thương mại báo giá trước khi dùng.
6. Khẩu hiệu trên danh thiếp/chữ ký: dùng "Khai mở cách vận hành mới." (VI) và "Open a new way to operate." (EN) theo DEC-072; founder xác nhận có đặt khẩu hiệu trên văn phòng phẩm không.
