---
type: brand-kit
status: approved
updated: 2026-10-14
links:
  - design/brand/brand-brief.md
  - design/brand/guideline/brand-guideline.html
---

# Bộ nhận diện Invlogis × innvie · v1.0 (Mốc 2)

Hướng A · Lụa (DEC-072), chữ v gradient phương án 1 (DEC-073), founder duyệt Mốc 2 (DEC-074).
Quy chuẩn đầy đủ: `../guideline/brand-guideline.html` (bản in: `brand-guideline.pdf`, A4 ngang).

File Figma: https://www.figma.com/design/KPpfeOJ4m0JI33rBnhon3o ([innvie] Invlogis Brand, team innvie): 6 trang Cover · Logo · Color · Type · Gradients · Applications; logo là component vector, bộ biến "Brand" (Light/Dark, 43 biến), 15 kiểu chữ (Mốc 4, DEC-078).

## Có gì

| Thư mục / file | Nội dung |
|---|---|
| `logo/` | Logo chính, nền tối, đơn sắc đen/trắng, xếp dọc, kèm khẩu hiệu Việt/Anh, lockup "by innvie", ký hiệu i (màu/tối/đơn sắc), logo innvie. Favicon SVG + PNG 16/32/48, icon app iOS 1024 + 180, Android adaptive 432 (phương án B). Logo động `logo-motion.html`. Quy định dùng: `logo/logo-spec.md` |
| `backgrounds/` | 9 nền gradient lụa × 5 cỡ (`bg-{mã}_{cỡ}.jpg`, JPG q90), thẻ chứng từ trên nền (`doc-hero-*`), khung thiết bị (`device-*`), trang xem thử `gradients.html`, số đo tương phản `_contrast.json` |
| `fonts/` | Lexend, Be Vietnam Pro, JetBrains Mono (giấy phép OFL) |
| `brand.yml` | Màu, logo, font cho `/deck` (cùng định dạng `../innvie/brand.yml`) |
| `brand-tokens.css` / `.json` | Token thương hiệu tiền tố `--brand-` cho tài liệu và web marketing. Không thay token sản phẩm `design/design-tokens.css` |
| `deck/` | Mốc 3 (DEC-075). Deck chào hàng 16 slide `invlogis-sales-deck.{html,pptx,pdf}`, bộ mẫu slide `invlogis-template.pptx` (10 layout; slide deck gắn layout, chữ nằm trong placeholder), ảnh xem trước. PPTX cần cài font trong `deck/assets/fonts/` |
| `web/` | Mốc 3. Landing page tiếng Việt `index.html` + tiếng Anh `en/index.html`, tự chứa assets, ảnh OG 1200×630. Trước khi đăng: `grep -c "\[chờ" web/index.html web/en/index.html` phải ra 0 |
| `stationery/` | Mốc 3. Danh thiếp 90×55 mm (PDF in, tràn lề 3 mm), giấy tiêu đề, mẫu báo giá, mẫu hợp đồng (DOCX + PDF, có bản `-arial`), chữ ký email Việt/Anh, phong bì DL. Pháp nhân ký: innvie. Hợp đồng là khung, cần luật sư duyệt |
| `marketing/` | Mốc 3. Tài liệu 1 trang A4 Việt/Anh, 6 bài đăng, 3 story, ảnh bìa LinkedIn/Facebook/YouTube-X, bộ ra mắt (hero web, đầu email, bài đăng, story đếm ngược, phông sự kiện 3000×2000). Mẫu HTML sửa chữ được + PNG/PDF |
| `product/` | Mốc 3. Đề xuất điểm chạm sản phẩm: đăng nhập (thường + khách thuê), splash A giữ DEC-037 (B là phương án đã bỏ), icon, favicon, 3 email hệ thống, màn tải, giới thiệu. Bảng việc cần sửa trong sản phẩm: `product/touchpoints.md` |

Mã nền: `n1-chamdem`, `n2-cobalt`, `n3-chamtim`, `n4-periwinkle`, `n5-giay-lua`, `n6-muc-cobalt` (dùng hằng ngày) · `r1-tim-hong`, `r2-lam-tim`, `r3-nang` (rực, chỉ dùng cho ra mắt). Cỡ: 1920x1080, 1080x1350, 1080x1080, 1500x500, 2560x1440. Luật đặt chữ trên nền: quy chuẩn mục Gradient.

## Dựng lại

Thư mục này chỉ chứa thành phẩm. Script dựng nằm trong `../_drafts/`; sửa và dựng ở đó, xong chép thành phẩm sang đây.

| Phần | Nguồn | Lệnh |
|---|---|---|
| Logo, favicon | `_drafts/logo-final/_src/build.py` | `python3 _src/build.py` (trong `_drafts/logo-final/`) |
| Icon app | `_drafts/logo-final/_src/icons.py` | xem `logo/logo-spec.md` Mục 7 |
| Nền, thẻ, khung | `_drafts/visuals/generate.py` | `python3 generate.py` → PNG; đổi sang JPG q90 khi chép sang `backgrounds/` |
| Deck, web, văn phòng phẩm, điểm chạm | `_drafts/m3/{deck,web,marketing,stationery,product}/` | script dựng trong từng thư mục (`build.py`, `_build.py`, `_src/`); dựng xong chép sang đây, bỏ file `.py` |
| Quy chuẩn | `_drafts/system/brand-guideline.html` | sửa đường dẫn `../logo-final/` → `../invlogis/logo/`; PDF: `python3 _drafts/_tools/render.py guideline/brand-guideline.html guideline/brand-guideline.pdf` |

Cần PNG không nén cho in khổ lớn: chạy lại `generate.py`, không phóng to file JPG.
