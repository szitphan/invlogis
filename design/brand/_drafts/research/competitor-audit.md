---
type: brand-research
status: draft
updated: 2026-10-14
links:
  - design/brand/brand-brief.md
---

# Việc 1.1 — Đối thủ, xu hướng nhận diện AI, bản đồ màu xanh, nghĩa "innvie"

> Tra cứu ngày 14/10/2026. Mức tin cậy ghi cạnh dữ kiện: **[V]** đọc thẳng từ nguồn gốc (HTML, CSS, meta, ảnh OG, file logo của chính trang thương hiệu; từ điển) · **[T]** nguồn thứ ba hoặc tóm tắt tìm kiếm, chưa đọc toàn văn · **[N]** nhận định của người khảo sát. Màu "CSS" là mã có trong CSS trang chủ, KHÔNG phải brand guideline; màu "logo/ảnh" là fill SVG hoặc lấy mẫu điểm ảnh.

## 0. Tóm tắt và giới hạn

**5 phát hiện chính**
1. Khoảng trống thông điệp lớn nhất: chữ trên 5 trang chủ Việt Nam (Logivan, Ahamove, Vietmap, ECUS, GHN) nhắc "eDO / EIR / booking / ePort / phiếu cân / bãi / depot" đúng 0 lần; chỉ GHN nói AI bằng chữ, nói chung chung [V].
2. Toàn cầu đã chiếm cú pháp "AI-powered…" (Flexport, project44, Samsara) → mở bằng kết quả, để AI làm lý do [V].
3. Xanh dương: mảng hue 206–217° ("xanh công nghệ") đông nhất. Ba vùng chưa mẫu nào dùng làm màu thương hiệu: cobalt ngả tím hue 234–240°, navy mực ngả chàm, xanh khói bạc màu (Mục C).
4. Đại trà cần tránh: gradient tím→xanh mượt + vòng rỗng tâm toả tia; nền đen + quầng sáng + lưới; ảnh stock phủ xanh. Còn tươi: gradient có hạt + vệt hướng, nền giấy ấm, chữ display mảnh + nhãn mono (Mục B).
5. "innvie": nghĩa "khánh thành / đưa vào sử dụng" đã xác minh ở 3 từ điển; nghĩa "cống hiến" chỉ xác minh gián tiếp (Mục D).

**Giới hạn đã biết**
- Không truy cập được: smartlog.com.vn (kết nối bị từ chối) → Smartlog, đối thủ container gần nhất, CHƯA audit; openai.com và creativereview.co.uk trả 403; creativebloq.com chỉ trả tiêu đề.
- Lalamove: chưa lấy được file logo/ảnh. ECUS, Vietmap, GHN: chỉ xem logo + banner; CargoWise: chỉ xem logo; không xem toàn trang.
- Không đọc ảnh tham chiếu của founder (theo yêu cầu); chi tiết "icon kính mờ nổi" chỉ đối chiếu qua CSS elevenlabs.io.
- "Đối thủ nói / không nói gì" chỉ ở mức chữ trang chủ, chưa phải toàn website.
- Cách làm: curl đọc HTML/CSS/OG/logo trang chính thức, WebSearch/WebFetch, API công khai ordbokene.no; khoảng 40 lượt; không dùng API trả phí, không tạo ảnh.

## A. Đối thủ / benchmark (12 thương hiệu)

### A1. Việt Nam (5)

| Thương hiệu · URL | Định vị / khẩu hiệu (nguyên văn) | Màu chủ đạo (mã · nguồn) | Kiểu logo | Hình ảnh | Giọng văn | AI? |
|---|---|---|---|---|---|---|
| **Logivan** · https://logivan.com | "LOGIVAN - Digitising and optimising freight transportation in Vietnam"; "Vietnam's Leading Digital Freight Network Since 2017" | Cyan `#5ae1e6` + than `#2a2a2a` (logo JPG) · web nhấn `#f0523d`, `#00b2ff` (CSS) | Ký hiệu + chữ: tam giác/mũi tên hướng phải kèm vạch tốc độ cyan; chữ serif hoa "LOGIVAN / LOGISTICS GROUP" | Bản đồ xám + tuyến cam (ảnh OG), mẫu Squarespace | Trang trọng, tiếng Anh, nhấn bền vững ("Driving Sustainability") | Không (0 lần) |
| **Ahamove** · https://ahamove.com | "Ahamove - Chuyên gia giao hàng"; "Ahamove là chuyên gia giao hàng của riêng bạn"; "Luôn chuyển động cùng bạn, dù bạn là ai" | Navy `#0d4073` + cam `#ff7f32` (logo SVG) · theme-color `#142246` | Ký hiệu + chữ: chữ "A" cam có vạch tốc độ và hai chấm như mắt; chữ "Ahamove" đậm, bo tròn | Cam rực, ảnh dựng đời thường, chữ thư pháp (chiến dịch "Chuyển nhà", ảnh OG) | Thân thiện, "bạn", hứa trải nghiệm ("thời gian, chi phí, an tâm") | Không |
| **Vietmap** · https://vietmap.vn | "VIETMAP JSC - Công Ty Cổ Phần Ứng Dụng Bản Đồ Việt"; "…thiết bị GPS dẫn đường, camera hành trình, phần mềm theo dõi và quản lý xe, các giải pháp ứng dụng bản đồ số và hệ thống thông tin địa lý (GIS)…" | Xanh `#2a5dff` (logo PNG, CSS) · theme-color `#f02b2b` (đỏ) | Chỉ chữ: "VIETMAP" nghiêng, đậm, có chân, xanh, kèm ® | Ảnh sản phẩm trên nền xám, chữ xanh lớn (banner dashcam), mẫu cửa hàng | Bán hàng, liệt kê sản phẩm ("Cảnh báo thông minh") | Không (nói "thông minh") |
| **ECUS (ThaisonSoft)** · https://ecus.vn | "PHẦN MỀM HẢI QUAN ĐIỆN TỬ ECUS"; "Phần mềm được nhiều doanh nghiệp xuất nhập khẩu sử dụng nhất tại Việt Nam"; slogan trong logo "Tin cậy - Tận Tình - Chuyên nghiệp" | Xanh `#004b98` + cam `#f8811f` (logo SVG) · banner xanh `#026cbc` (lấy mẫu ảnh) | Chỉ chữ: "ECUS" nghiêng, đậm, vệt tốc độ xanh–cam, slogan bên dưới | Ảnh cảng + hộp phần mềm trên nền xanh; ảnh văn phòng thật | Trang trọng, chữ HOA, khẳng định "nhiều nhất" | Chữ: không. Ảnh banner có nhãn "AI" nhỏ (thấy trong ảnh, chưa kiểm) |
| **GHN (Giao Hàng Nhanh)** · https://ghn.vn | "Giao Hàng Nhanh: Giao Siêu Nhanh, Giá Siêu Tốt"; "GIẢI PHÁP LOGISTICS MAY ĐO CHO TỪNG NGÀNH HÀNG"; logo kèm "YOUR LOADS. OUR ROADS." | Banner cam `#f06b00` / `#fb5500` (lấy mẫu ảnh) · logo đen `#000000` + ngọc `#00a19a` (PNG) | Chỉ chữ: "GHN" khối đậm, chữ G có mũi tên cắt màu ngọc | Cam gradient + minh hoạ isometric (xe, người, bản đồ điện thoại) | Hô khẩu hiệu, lặp "Siêu", hứa nhanh + rẻ | **Có**: "Ứng dụng công nghệ AI sâu vào vận hành và quản lý đảm bảo giao-nhận đơn hàng nhanh, thông minh và tiết kiệm hơn." |

### A2. Đông Nam Á (3)

| Thương hiệu · URL | Định vị / khẩu hiệu (nguyên văn) | Màu chủ đạo (mã · nguồn) | Kiểu logo | Hình ảnh | Giọng văn | AI? |
|---|---|---|---|---|---|---|
| **Haulio** (Singapore) · https://www.haulio.io | "The Future of Haulage is Here."; "Haulio is Southeast Asia's fastest-growing container haulage platform, with the greater vision of connecting global trade to local first-mile transportation across ASEAN." | Đỏ `#d42229` (logo PNG; CSS `#d22127`) · phụ chàm `#4e35df` (CSS) | Chỉ chữ: "HAULIO" hoa, đậm, chữ H có khấc | Ảnh chụp từ trên cao bãi xe container, màu bão hoà (ảnh OG) | Tầm nhìn khu vực: "Join the Digital Revolution of Container Trucking" | Không (0 lần) |
| **Kargo Technologies** (Indonesia) · https://www.kargo.tech | "Kargo - Sewa Truk Online \| Logistics \| Indonesia"; "Layanan Logistik Fullfilment Bantu Bisnis Anda"; sản phẩm "Kargo Nexus: Transport Management System" | Xanh `#1473b8` + da trời `#4cbce5` (logo PNG) · CSS `#028eff`, `#0a83e4`, đỏ `#d41317` | Ký hiệu + chữ: chữ K có tia chớp (hai sắc xanh) + "KARGO" hoa | Ảnh stock phủ xanh (máy bay, xe đầu kéo, cảng) + nút xanh/chàm (ảnh OG) | Dịch vụ, hứa "Delivering Beyond Expectations"; ESG xe điện | Không (0 lần) |
| **Lalamove** · https://www.lalamove.com | "Same Day Delivery & Courier丨Van & Truck Hire Services"; "Lalamove is the fastest way to deliver anything in your city… connects you with thousands of drivers in 1 click." | Cam `#f16622` (CSS, chưa có file logo) | Chưa xác minh (không tải được file logo) | Chưa xác minh (trang không có ảnh OG) | Thực dụng, "1 click", so tốc độ | Không (0 lần) |

### A3. Toàn cầu (4)

| Thương hiệu · URL | Định vị / khẩu hiệu (nguyên văn) | Màu chủ đạo (mã · nguồn) | Kiểu logo | Hình ảnh | Giọng văn | AI? |
|---|---|---|---|---|---|---|
| **Flexport** · https://www.flexport.com | "AI-powered logistics for the real world"; "Ship smarter with Flexport's AI-powered freight forwarding platform…" | Navy `#052439` (CSS) / `#052338` (ảnh OG) + trắng · phụ chàm `#344d9b`, `#223369`, `#7d8ce4` (CSS) | Chỉ chữ: "flexport" chữ thường, rất đậm | Nền navy phẳng, wordmark trắng, ít ảnh (ảnh OG) | Tự tin, nói kết quả ("Better on-time-in-full performance") | **Có**, là tiêu đề: "AI that spots problems before they happen"; "AI Customs Classification" |
| **project44** · https://www.project44.com | "Decision Intelligence Platform"; "Your Supply Chain at Work"; "Introducing Movement: The AI-powered Decision Intelligence Platform for the modern supply chain." | Xanh `#0072e9` (logo SVG, mask-icon) · cyan `#00bbff` (CSS) · nền đen (ảnh OG) | Chữ + chấm: "project44" chữ thường hẹp, số "44" trắng trong vòng tròn xanh | Nền đen, lưới xanh mảnh, khối thuỷ tinh 3D (ảnh OG) | Kỹ thuật, nhiều thuật ngữ ("Orchestration") | **Có**, nặng: "AI Orchestration", "Agentic Workflow Manager", "no-code platform for deploying AI agents…" |
| **Samsara** · https://www.samsara.com | "Samsara \| The Connected Operations Platform"; "Operator grade. Proven in the field." | Vàng hổ phách `#feae0f` (`--sm-color-brand-500`) + than `#1c1917`; xanh chỉ là thang phụ (`#2a75d4`) | Ký hiệu + chữ: đầu cú + "SAMSARA" hoa, rộng, đậm (ảnh OG) | Vàng–đen phẳng có hạt, thực địa, cứng cáp (ảnh OG) | Câu ngắn, giọng người vận hành: "Operator grade isn't a promise. It's a practice." | **Có**: "AI dash cams", "AI that acts", "Samsara MCP" |
| **CargoWise (WiseTech)** · https://www.cargowise.com | "Centralize global logistics operations on a single platform solution, CargoWise."; "All modes. All borders. One platform." | Chàm điện `#371ee1` (logo SVG) · phụ cyan `#73d7f4`, `#ccdcff` (CSS) | Ký hiệu + chữ: cụm vạch ngang xếp lệch (như dòng chứng từ) + "cargowise" chữ thường tròn | Chưa xem ảnh trang; nền trắng, một sắc chàm (suy từ CSS) | Bao quát, công thức ba chấm, nêu số ("over 17,000 organizations") | Ít: chỉ qua tin e2open ("AI-powered approach to transportation management") |

### A4. Nguồn file (màu, logo, ảnh) và ghi chú

- Logivan: logo https://images.squarespace-cdn.com/content/v1/644e1ca0b2ee8b5623e2934b/bce356eb-e37b-489c-ac9b-cc2402240b22/Logo+Grey+with+Turquoise+Highlight+Background+White+%281%29.jpg · OG http://static1.squarespace.com/static/644e1ca0b2ee8b5623e2934b/t/645235633502c4348e55e584/1723365759696/control+tower+north+1.png
- Ahamove: logo https://ahamove.com/static/icons/Logo.svg · OG https://cdn-cms.ahamove.com/KV_banner_web_copy_90f80c2656.png · theme-color, mask-icon `#ff7500` trong HTML https://ahamove.com
- Vietmap: logo https://bizweb.dktcdn.net/100/415/690/themes/804206/assets/logo.png · banner https://bizweb.dktcdn.net/100/415/690/themes/804206/assets/slider_1.jpg
- ECUS: logo https://ecus.vn/Content/images/ECUS/Logo_Header.svg · banner https://ecus.vn/FileUpload/images/Slide/1b861bf3-d24d-4a43-b6a5-807bb8b58a8c.jpg
- GHN: logo https://cdn.hstatic.net/files/200000472237/file/logo_set_ngang.png · banner https://cdn.hstatic.net/files/200000472237/file/headbanner_1600x686-01.jpg
- Haulio: logo https://haulio.io/wp-content/uploads/2023/01/Haulio_Logo_Red.png · OG https://www.haulio.io/wp-content/uploads/2020/05/FreightTrucksTA_GettyImages-83661454_2.jpg
- Kargo: logo https://static.wixstatic.com/media/b8ae15_8fbe22c55ca6487eb481cd9794413b90~mv2.png · OG https://static.wixstatic.com/media/c937f3_e0e10f155c2d443db775b7e635f8f58d~mv2.jpg
- Flexport: OG https://cdn.sanity.io/images/ynj1yl20/development/1bab2957162734f28a7d3b723d4eb6a63300ed20-726x396.png · logo là `<symbol id="flexport-logo">` nhúng trong https://www.flexport.com
- project44: logo https://cdn-iladlmn.nitrocdn.com/qcimIvFNvroAeWBmCEUImqHGnxBfwdwN/assets/images/source/rev-c00774b/www.project44.com/wp-content/uploads/2024/01/logo.svg · OG https://www.project44.com/wp-content/uploads/2024/05/Frame-8.png
- Samsara: OG https://images.ctfassets.net/bx9krvy0u3sx/7cxFtCvfGbzKg8s56mzITz/b98e6bd658d8e998d50ee7277daee538/Meta-Image_Homeapge-v2.png · biến CSS trong https://www.samsara.com
- CargoWise: logo https://www.cargowise.com/media/zfpirzxd/cargowise-logo.svg · CSS trong https://www.cargowise.com
- Smartlog (chưa audit): sản phẩm SMT, SWM, STX, COS; ký với CMA CGM Vietnam 1/2020 [T] https://en.vietstock.vn/2021/06/smartlog-transforms-vietnam8217s-logistics-business-development-38-447531.htm. Cần kiểm tay website trước khi chốt định vị.
- ECUS (hải quan) và Vietmap (định vị xe) là phần mềm kề cận, không phải TMS/điều vận; GHN, Ahamove, Lalamove thiên về giao hàng hơn là phần mềm cho doanh nghiệp vận tải container.

## B. Xu hướng nhận diện thương hiệu AI 2025–2026

### B1. Sáu mẫu

| Thương hiệu · URL | Mã hình ảnh nhận ra được | Trạng thái |
|---|---|---|
| **ElevenLabs** · https://elevenlabs.io | Nền trắng ấm `#fdfcfc` / `#f5f3f1`; chữ Waldenburg nhẹ + Inter + Geist Mono; gradient có hạt và vệt chuyển động; viền mảnh bo tròn; nhãn ngoặc `[whispers]` [V]. Đã có trang tổng hợp "design system ElevenLabs" cho người khác dùng lại, vd https://www.shadcn.io/design/elevenlabs [T] | Tươi, nhưng bắt đầu bị sao chép |
| **Anthropic** · https://www.anthropic.com | Nền kem `#faf9f5` / `#f0eee6`, mực ấm `#141413`, nhấn cam đất `#d97757` / `#c6613f`; font tự thiết kế "Anthropic Sans / Serif / Mono"; wordmark hoa "ANTHROP\C" (ảnh OG) [V] | Tươi so với xanh–tím; nền giấy ấm đang thành "phe" mới [N] |
| **Perplexity** · https://www.perplexity.ai | Nền xanh ngọc tối `#12343b` (ảnh OG), ký hiệu nét mảnh dạng tia/asterisk, tagline "Where Knowledge Begins" ngọc `#32b8c6`; theme-color `#FCFCF9` / `#100E12` [V] | Ký hiệu tia/asterisk thuộc họ đại trà [N] |
| **Linear · Vercel** · https://linear.app · https://vercel.com | Đen gần tuyệt đối (`#08090a` / `#000`), ký hiệu trắng có quầng sáng (vòng sọc, tam giác), Geist; Vercel có họ chữ pixel "Geist Pixel" [V] | Đại trà: "đen + glow" [N] |
| **Runway** · https://runway.com | Nền `#0C0C0C`, ảnh sương nhiếp ảnh teal–xám, chữ serif "timesNow" + "abcNormal" [V] | Tươi: ảnh sương + serif |
| **OpenAI** · https://openai.com/brand (403 khi tải) | 2/2025: font riêng OpenAI Sans ("balances geometric precision with approachable, rounded characters"), hoa "blossom" chỉ dành cho nghiên cứu [T] https://www.maginative.com/article/openai-unveils-new-visual-identity/. Palette xám–xanh, ảnh phong cảnh + hoa văn Sora [T] https://www.creativereview.co.uk/openai-brand-refresh/ | Hướng "ít logo, nhiều chữ riêng, ấm hơn" |

### B2. Mã đã thành đại trà (nên tránh)

- Gradient "tím→xanh" hoặc "ngọc→magenta", vòng tròn rỗng tâm có tia/chấm toả ra: bài ngày 20/7/2026 nói bảng màu này "close to an industry-standard palette", lý do "everyone runs the same calculation" và công cụ tạo logo AI quay về mẫu chung [T] https://braindetox.kr/en/posts/ai_logo_design_convergence_2026.html. Creative Bloq cùng đề tài nhưng không đọc được nội dung [T] https://creativebloq.com/design/logos-icons/why-do-all-ai-company-logos-look-the-same.
- Ký hiệu tia/asterisk/spark: thấy ở Perplexity (ảnh OG) [V]; mức phổ biến là [N].
- Nền đen + quầng sáng + lưới + khối thuỷ tinh 3D: project44 (lưới xanh + khối thuỷ tinh), Vercel (tam giác phát sáng), Linear (đen chuyển sắc) [V ảnh OG]; "đại trà" là [N].
- Ảnh stock phủ xanh của ngành (xe đầu kéo, máy bay, cảng): Kargo, Haulio, ECUS [V ảnh OG/banner] — trùng danh sách sáo rỗng ngành trong brief.
- Từ vựng: "AI-powered", "agents" đã lên tiêu đề (Flexport, project44, Samsara; Linear "teams and agents"; Vercel "Agentic Infrastructure"; ElevenLabs "Voice Agents") [V] → "AI agent" để ở phần tầm nhìn (đúng brief), đừng làm khẩu hiệu.

### B3. Mã còn tươi

- Gradient có hạt + vệt hướng + vài sắc ấm, mỗi sản phẩm một "thế giới màu" (ElevenLabs) thay cho gradient mượt tím–xanh [V].
- Nền giấy ấm (`#fdfcfc`, `#faf9f5`, `#FCFCF9`) + mực gần đen + một nhấn: Anthropic, ElevenLabs, Perplexity (theme-color) [V]. Chưa thấy thương hiệu logistics nào trong 12 mẫu dùng.
- Chữ display mảnh hoặc serif + nhãn mono: ElevenLabs Waldenburg 300 + Geist Mono; Anthropic Serif; Runway timesNow [V].
- Giao diện sản phẩm làm hình chính, kèm nhãn vi mô có chức năng thật (`[whispers]`) thay cho ảnh stock [V].
- Samsara bỏ xanh sang vàng hổ phách `#feae0f` [V] → xanh trong logistics đã đông; Invlogis giữ xanh theo brief nên khác biệt phải đến từ sắc độ và chất liệu, không từ đổi hẳn màu [N].

### B4. ElevenLabs — mổ xẻ để học gu (nguồn [V]: https://elevenlabs.io và CSS/ảnh của trang)

**Chữ và nền**
- Nền trắng ấm `#fdfcfc` (mã nhiều nhất), `#f5f3f1`; mực đen; không dùng trắng lạnh.
- H1 "Bringing technology to life" dùng Waldenburg trọng lượng 300, letter-spacing −0.02em (`.tw-type-6xl`); token heading: 36px / dòng 105% / −0.03em; body Inter 400, tracking +0.01em; nhãn Geist Mono; tiêu đề `text-balance`. Token display dùng Waldenburg FH 700 (đậm); heading chính vẫn 300.
**Gradient (phần "lụa" founder thích)**
- Hai họ. (a) Mesh gradient có hạt: https://eleven-public-cdn.elevenlabs.io/marketing_website/_next/static/media/purpleblue.7b1b4a1a.webp (chàm→đỏ→tím), .../green.9f6a4e17.webp (ôliu→lục). (b) Vệt chuyển động mờ như lụa: https://eleven-public-cdn.elevenlabs.io/payloadcms/31vqrnjmkll-Creatives-BG.webp (san hô/cam), .../tvqokiltm5q-Agents-BG.webp (xanh than→chàm), .../em4cn4nlbxm-v4-cover.png (cam–lục–đen).
- Hạt (noise) là lớp riêng: file `noise.png/avif` và các tham chiếu `noise` + `mix-blend-mode` trong CSS. Hạt làm gradient có "chất liệu", khác gradient mượt của họ AI xanh–tím.
- Màu nóng–dịu, bão hoà vừa (san hô, đào, ôliu, periwinkle), không neon. Mỗi sản phẩm một thế giới màu: Creative = cam/vàng; Agents = lục→xanh da trời; Voice = periwinkle→đào; v4 = cam–lục–đen.
- Gradient làm chất liệu của chữ: "V4" tô bằng chính gradient (https://eleven-public-cdn.elevenlabs.io/payloadcms/s74wyvms6k-v4-banner-icon.png).
**Khung, đường kẻ, chi tiết giao diện**
- Khung "V4": viền trắng dày dạng viên thuốc quanh chữ trên nền gradient (v4-cover.png). Trong markup trang chủ, `rounded-full` ~218 lần, `rounded-3xl` ~38 lần.
- Viền cực mảnh: `border-black/5` ~24 lần; đường kẻ dọc trái/phải (`border-l`, `border-r`) ~24 lần mỗi loại, tạo cột; banner có góc khuyết kiểu tab, nét 0,5px đen 10%.
- Kính mờ có thật: `backdrop-filter` 13 lần trong CSS (khớp "icon kính mờ nổi"; chưa đối chiếu ảnh của founder).
- Ảnh bìa tĩnh (https://elevenlabs.io/cover.png): nền kem + hoa văn lưới sóng nét mảnh + wordmark "IIElevenLabs" (hai vạch dọc + chữ đậm); không ảnh người.
- Nhãn ngoặc `[whispers]` (chữ xám) và `[laughs]` nằm trong mock giao diện của trang; đây là nội dung sản phẩm (có vẻ là thẻ điều khiển giọng đọc [N]), không phải trang trí thuần tuý. Nút đen dạng viên thuốc, không màu CTA bão hoà [T] https://www.shadcn.io/design/elevenlabs.

**Học gu, không sao chép (cho Invlogis)**
- Giữ cơ chế "hạt + vệt hướng + 2–3 sắc" nhưng neo xanh; hướng vệt gắn với ý riêng (vệt quét ngang như tia đọc chứng từ), sắc ấm chỉ là ánh.
- Giữ viền 0,5px 5–10% đen và góc khuyết; đổi hình khung: góc gấp tờ giấy hoặc cắt vát, không dùng viên thuốc có chữ phiên bản.
- Giữ nhãn mono nhỏ nhưng nội dung là nhãn chứng từ Việt: `[eDO · đã đọc]`, `[Booking Note · khớp]`. ElevenLabs gắn nhãn vào giọng nói; Invlogis gắn nhãn vào chứng từ — đó là chỗ để nhìn vào nhận ra Invlogis. Font nhãn phải qua kiểm dấu tiếng Việt (việc 1.3).
- Bỏ: hai vạch dọc "II", Waldenburg, hoa văn lưới sóng, bảng cam–lục–đen của v4, nền kem + chữ đen làm bố cục y hệt.

## C. Bản đồ màu xanh

### C1. Mảng xanh đối thủ đang chiếm (hue° · S% · L%, tính từ mã đã xác minh)

| Nhóm | Mã đã xác minh (nguồn) | Ai chiếm |
|---|---|---|
| Azure "xanh công nghệ" 206–217°, S 90–100, L 37–58 | `#0072e9` 211°·100·46 (logo SVG project44) · `#028eff` / `#0a83e4` 207° (CSS Kargo) · `#2b7fff` / `#0a59d2` 216° (CSS ElevenLabs) · `#0070f3` 212° (CSS Vercel) · `#026cbc` 206°·98·37 (banner ECUS) · `#007bff` 211° (mặc định Bootstrap trong CSS GHN, ECUS, Vietmap, CargoWise) | Đông nhất: project44, Kargo, ECUS (banner), ElevenLabs/Vercel (UI); `#007bff` chỉ là mã mặc định có trong CSS, chưa chắc hiển thị |
| Navy 204–214°, L 12–30 | `#052439` 204°·84·12 (CSS Flexport) · `#0c2648` 214° (Samsara, thang phụ) · `#0d4073` 210°·80·25 (logo Ahamove) · `#004b98` 210°·100·30 (logo ECUS) · `#0d3458` (ảnh OG Kargo) | Flexport, Ahamove, ECUS, Samsara (phụ) |
| Royal blue 226°, L 58 | `#2a5dff` 226°·100·58 (logo + CSS Vietmap) | Vietmap (VN) |
| Chàm / indigo 247–249° | `#371ee1` 248°·76·50 (logo SVG CargoWise) · `#4e35df` 249° (CSS Haulio, phụ) · `#4f39f6` 247° (CSS Vercel) · + gradient tím→xanh của "AI logos" (Mục B2) | CargoWise (logistics), cả họ logo AI |
| Cyan / da trời 182–198° | `#00bbff` 196° (CSS project44, phụ) · `#00b2ff` 198° (CSS Logivan) · `#5ae1e6` (logo Logivan) · `#4cbce5` (logo Kargo) · `#55cdff` (CSS Linear) · `#73d7f4` 193° (CSS CargoWise) | Dùng làm nhấn: project44, Logivan, Kargo, CargoWise |
| Xanh ngọc tối ~177–190° | `#12343b` (ảnh OG Perplexity) · `#00a19a` (logo GHN) · `#32b8c6` (CSS Perplexity) | Perplexity, GHN |
| Đối cực (không xanh) | cam `#f16622` Lalamove · `#f06b00` GHN · `#ff7f32` Ahamove, `#f8811f` ECUS · đỏ `#d42229` Haulio · vàng `#feae0f` Samsara | Cặp "navy + cam phẳng" đã có ở Ahamove và ECUS |

### C2. Ba vùng Invlogis có thể sở hữu (mã là mốc minh hoạ, việc 1.3–1.5 chốt)

| Vùng | Thông số · mốc | Vì sao sở hữu được | Hợp hướng | Lưu ý |
|---|---|---|---|---|
| **1. Cobalt ngả tím** | hue 234–240°, S 78–88%, L 38–48% · `#1729cf`, `#1a23d1`, đậm `#0f14b3` | Khoảng 230–244° ở S≥70, L 35–60 không có mã thương hiệu nào trong 18 mẫu đã khảo sát; láng giềng gần nhất: Vietmap 226° (sáng hơn), mã UI `#0447ff` / `#1d4ed8` 224° (CSS ElevenLabs, Perplexity), CargoWise 248°. Đủ "điện" cho tiên phong, sang tím/cam được mà không thành gradient tím–xanh mượt | C, A | Cách CargoWise ≥ 8–10° (đừng vượt 244°); đừng sáng lên L58 (dính Vietmap) |
| **2. Navy mực ngả chàm** | hue 228–238°, S 45–55%, L 10–20% · `#0f1433`, `#19204d` | Navy hiện có nghiêng lục/dương (204–214°); navy ngả chàm gần như trống (gần nhất là theme-color Ahamove `#142246`, 223°, chưa dùng ở logo). Cho chữ, tài liệu, nền tối mà không giống "đen + glow" của Linear/Vercel | B, tài liệu | Phải đi cùng nền trắng ấm, nếu không thành "navy doanh nghiệp cũ" (Flexport, ECUS) |
| **3. Xanh khói / thép** | hue 210–218°, S 25–40%, L 45–86% · `#d0dae7`, `#a2b5cd`, `#4b6d9b` | Không mẫu nào dùng xanh bạc màu làm màu thương hiệu (chỉ thấy làm nền ảnh: Agents-BG của ElevenLabs, sương Runway). Hợp "chuyên gia điềm tĩnh", ghép tốt với nền ấm và đào/san hô làm ánh | A (nền lụa), mọi tài liệu | Đứng một mình khó nhận diện; luôn đi cùng vùng 1 hoặc 2 |

- Tránh làm màu chủ đạo: azure 205–218° (đông, mặc định Bootstrap/Wix `#116dff` 217°), royal 226° L58 (Vietmap), chàm ≥ 246° (CargoWise, gradient AI).
- Cặp "xanh + cam phẳng" làm logo đã bị Ahamove và ECUS dùng; giữ logo một sắc xanh, sắc ấm chỉ nằm trong gradient chiến dịch.

## D. Nghĩa tiếng Na Uy của "innvie"

**Kết luận: ĐÃ XÁC MINH [V] từ Bokmålsordboka, Nynorskordboka, NAOB.** *innvie* là động từ, từ nguyên "etter tysk *einweihen*" (ordbokene.no).

| Nguồn | Nghĩa (nguyên văn → dịch) | Ví dụ trong từ điển |
|---|---|---|
| Bokmålsordboka https://ordbokene.no/bm/26789/innvie (bài cập nhật 6/11/2023) | 1. "vie, hellige" → thánh hoá, phong chức · 2. "markere ved seremoni el. fest at noe er ferdig og skal tas i bruk" → làm lễ/tiệc đánh dấu một thứ đã xong, bắt đầu đưa vào sử dụng (khánh thành) · 3. "gjøre delaktig i" / "fortelle om" → cho ai tham dự, cho biết | "han ble innviet til prest"; "innvie en ny skole"; "lørdag skal vi innvie vår nye leilighet med en skikkelig fest"; "jeg innviet ham i planene" |
| Nynorskordboka https://ordbokene.no/nn/34451/innvie | 1. "vie, vigsle" · 2. "høgtideleg opne for å ta i bruk (bygning eller idrettsplass)" → long trọng mở để đưa vào sử dụng · 3. "gje nokon del i noko som elles ikkje er vanleg kjent" / "fortelje om" | "innvie ei kyrkje"; "innvie ein prest til biskop"; "innvie det nye samfunnshuset"; "eg innvigde henne i løyndomen" |
| NAOB https://naob.no/ordbok/innvie | 1 "vie, gjøre hellig" · 2 "markere ved høytidelig, festlig seremoni e.l. at f.eks. en bygning skal tas i bruk" · 3 "ved høytidelig seremoni hellige (en person) til en (religiøs) gjerning" · 4 (tôn giáo) "gjøre delaktig (i et mysterium…)" · 5 nghĩa bóng "gjøre delaktig (i en viten som ikke er alminnelig, i noe som ellers holdes hemmelig)" · 5.1 tính từ *innviet* "som vet noe som ellers holdes hemmelig eller som er lite kjent" | "imorgen skal asylet indvies" (Ibsen 1881); "innvie noen i en hemmelighet, i en plan"; "frimurerspråk for innvidde" (Borgen 1955) |
| *vie* https://ordbokene.no/bm/68226/vie | "bruke mye tid og krefter på noe" → dành nhiều thời gian, sức lực cho việc gì (nghĩa "cống hiến"); cũng "gjøre hellig ved bestemte seremonier" (tham chiếu tới *hellige*, *innvie*) | "vie livet sitt til vitenskapen" |
| *innvielse* (danh từ) https://ordbokene.no/bm/26790/innvielse | "det å innvie eller bli innviet" → lễ khánh thành / lễ nhập môn | "innvielse av misjonærer"; "vi skal feire innvielsen av det nye huset" |
| Wiktionary [T] https://en.wiktionary.org/wiki/innvie | "to consecrate"; "to dedicate, inaugurate" | — |

**Đối chiếu hai nghĩa trong brief**
- **"Khánh thành / khai mở / đưa vào sử dụng": CÓ**, cả ba từ điển (nghĩa 2). Từ điển viết "ta i bruk" (đưa vào sử dụng) và "høgtideleg opne" (long trọng mở) → "khánh thành", "đưa vào sử dụng" đúng sát; "khai mở" gần nghĩa. Dùng được cho dịp ra mắt; danh từ *innvielse* = lễ khánh thành/ra mắt.
- **"Cống hiến (dedicate)": chỉ xác minh gián tiếp.** Mục *innvie* không có nghĩa "dành trọn thời gian, sức lực cho một việc" (NAOB không liệt kê "vie seg til"). Gần nhất: "hiến/thánh hoá một người cho một sứ mệnh" (NAOB 3, Bokmål 1) và Wiktionary dịch "to dedicate". Nghĩa "cống hiến" đời thường thuộc *vie (seg) til* ("vie livet sitt til vitenskapen"). Đề nghị ghi "nghĩa suy rộng của hiến dâng" và nhờ người bản ngữ Na Uy kiểm trước khi in.
- Nghĩa thêm hợp "hiểu nghề": "đưa ai vào cuộc, cho biết điều ít người biết" (*innvie noen i en plan*); *innviet* = người trong cuộc. Lưu ý *innviet* cũng là từ của hội kín ("frimurerspråk for innvidde") → tránh cảm giác "hội kín".

## E. Khoảng trống thông điệp

### E1. Đối thủ đang lặp lại (nguyên văn, nguồn: trang chủ ở cột URL Mục A)

| Chủ đề lặp | Ai nói |
|---|---|
| Nhanh + rẻ | GHN "Giao Siêu Nhanh, Giá Siêu Tốt" · Lalamove "the fastest way to deliver anything in your city" · Ahamove "Luôn chuyển động cùng bạn" |
| "Nhiều nhất / hàng đầu / nhanh nhất" | ECUS "được nhiều doanh nghiệp xuất nhập khẩu sử dụng nhất tại Việt Nam" · Logivan "Vietnam's Leading Digital Freight Network Since 2017" · Haulio "Southeast Asia's fastest-growing container haulage platform" |
| Tin cậy / chuyên gia | ECUS "Tin cậy - Tận Tình - Chuyên nghiệp" · Ahamove "chuyên gia giao hàng" |
| Một nền tảng cho tất cả | CargoWise "All modes. All borders. One platform." · Flexport "Unify shipments, orders, and inventory in one AI-powered platform" · Samsara "Connected Operations Platform" |
| AI-powered / agents (toàn cầu) | Flexport "AI-powered logistics for the real world" · project44 "no-code platform for deploying AI agents" · Samsara "AI that acts" |
| Xanh / bền vững | Logivan "Pioneering Green Logistics" · Kargo "Net Zero Emission dengan Truk Listrik" |
| Con số khách | CargoWise "over 17,000 organizations" · Samsara "20,000+ operations" |

### E2. Chưa ai nói (trong 12 mẫu, mức chữ trang chủ)

- Tên chứng từ cụ thể: 0/5 trang Việt Nam nhắc eDO, EIR, booking, ePort, phiếu cân, bãi, depot. Toàn cầu nói "customs", "documents" ở mức tính năng ("Centralized document management" — project44; "AI Customs Classification" — Flexport).
- AI đọc chứng từ rồi điền vào hồ sơ: không ai nói như vậy. Flexport phân loại hải quan bằng AI; project44 triển khai "AI agents" cho workflow; GHN nói AI chung chung gắn với nhanh/rẻ.
- Bằng chứng "hiểu cảng Việt" bằng tên riêng: không ai. Công thức gần nhất là Kargo ở Indonesia ("Merekrut profesional dari Silicon Valley… dengan pendekatan lokal"), tức "chuẩn quốc tế + bản địa" đã có tiền lệ ở khu vực.
- Từ "thông minh" đang đứng thay chỗ của AI ở Việt Nam (GHN "nhanh, thông minh và tiết kiệm hơn"; Vietmap "Cảnh báo thông minh") → nói "AI đọc" phải kèm hành động cụ thể (đọc Booking Note, điền hồ sơ), nếu không bị nghe như "thông minh" chung chung [N].
- Dữ liệu nhập một lần, đi xuyên điều vận–xưởng–dầu–công nợ; app chạy khi mất sóng; cấu hình theo khách không sửa code: không thấy ở trang nào. Màn lãi lỗ theo lô: không ai nói, và Invlogis cũng chưa có feature (PRD OQ-3) → KHÔNG hứa.

### E3. Đối chiếu với lời hứa và câu chuyện của brief

- "Hiểu thực tế cảng Việt" là khoảng trống thật nhưng "hiểu" là tính từ ai cũng tự nhận (ECUS "chuyên nghiệp", Kargo "pendekatan lokal"). Chỉ thắng khi gọi tên: Booking Note, eDO, EIR, phiếu cân, tờ khai có QR, ePort.
- "AI đọc chứng từ Việt Nam" gần như bỏ trống ở Việt Nam, nhưng cú pháp "AI-powered…" đã bị toàn cầu chiếm → nói kết quả trước ("bớt nhập lại"), trình diễn bằng hình (chứng từ → hồ sơ).
- Giá trị "Đáng tin cậy": từ "Tin cậy" đã nằm trong slogan logo ECUS → cần bằng chứng số ẩn danh ("một doanh nghiệp vận tải container khoảng 110.000 lô/năm") thay vì tính từ.
- Cẩn trọng "one platform" (CargoWise, Flexport) khi nói "nhiều module chung một dữ liệu": nêu cụ thể "mỗi lô, mỗi đầu xe có giá thành thật".

## F. Kết luận cho Invlogis

**Cho chiến lược (việc 1.2)**
1. **Nên** gọi tên chứng từ và cảng Việt (Booking Note, eDO, EIR, phiếu cân, tờ khai có QR, ePort) ngay trang đầu và trong câu định vị; đây là khoảng trống rõ nhất (E2).
2. **Nên** mở bằng kết quả, AI là lý do; **tránh** "AI-powered…" làm câu mở và ba trục đã đông: nhanh+rẻ, "nhiều nhất/hàng đầu", "tin cậy/chuyên nghiệp" thuần tính từ. "Đáng tin cậy" cần số ẩn danh; không nêu tên khách.
3. **Nên** dùng nghĩa innvie đã xác minh: "khánh thành, đưa vào sử dụng" cho dịp ra mắt, "đưa vào cuộc" cho "hiểu nghề"; **tránh** viết "innvie = cống hiến" như nghĩa chính (chỉ là nghĩa suy rộng); nhờ người Na Uy kiểm trước khi in.

**Cho hình ảnh (việc 1.3–1.5)**
4. **Tránh**: gradient tím→xanh mượt, vòng rỗng tâm toả tia, nền đen + quầng sáng + lưới/khối thuỷ tinh, ảnh stock phủ xanh; ký hiệu tia chớp, mũi tên, vệt tốc độ (Kargo, Logivan, ECUS, Ahamove); azure 205–218°; logo "xanh + cam phẳng"; chữ nghiêng có vệt tốc độ.
5. **Nên** chọn màu chủ đạo từ vùng 1 (cobalt ngả tím) hoặc vùng 2 (navy mực), dùng vùng 3 (xanh khói) làm nền; gợi ý: A = vùng 3 + 1, B = vùng 2 + 1 (vệt quét), C = vùng 1 + gradient rực; luôn đi với nền trắng ấm.
6. **Nên** học gu ElevenLabs theo cơ chế: gradient có hạt + vệt hướng neo xanh, viền 0,5px, góc khuyết, nhãn mono nhỏ là nhãn chứng từ Việt. **Tránh** "II", viên thuốc "V4", Waldenburg, hoa văn lưới sóng, họ chữ pixel (Vercel đang dùng; brief đã bỏ pixel).
7. **Nên** thử 16px và đơn sắc ngay từ phác thảo; hướng B cảnh giác trùng ký hiệu vạch ngang xếp lệch của CargoWise và icon "tài liệu"; hướng A cảnh giác mềm quá; hướng C cảnh giác chữ "v" thành dấu tick và giống logo ngân hàng.

## G. Việc cần người kiểm tiếp

- Kiểm tay website Smartlog (không truy cập được từ môi trường khảo sát), bổ sung 1 dòng vào Mục A.
- Nhờ người bản ngữ Na Uy xác nhận cách đọc "innvie" khi làm tên riêng và sắc thái "cống hiến" trước khi đưa vào tài liệu in.
- Lấy logo/ảnh Lalamove; xem toàn trang ECUS, GHN, CargoWise nếu cần định vị hình ảnh sâu hơn.
- Đối chiếu ảnh tham chiếu của founder với Mục B4 (kính mờ, nhãn ngoặc) khi bắt đầu việc 1.3.
