# Brainstorm điều phối: ghi chép phỏng vấn (cập nhật 2026-10-02)

Nguồn: 3 SOP trong `docs-input/`, cộng 4 báo cáo `/discover` trong `docs/_research/2026-10-02-*.md`. Chưa ghi file vào vault. Feature slug dự kiến `dispatch-coordination`.

## Cách làm đã chốt
- Phỏng vấn **Deep**, đủ 7 phần, hỏi từng phần một. Không đi đường tắt dù tài liệu đã có.
- Mỗi câu hỏi ghi "Theo SOP" và/hoặc "Đề xuất" để user quyết định.
- SOP là **to-be của khách**, không phải as-is. Gắn nhãn [SOP to-be] / [SOP+] / [Mới]. Chỉ [SOP+] và [Mới] được tính là USP.
- Khách sẽ gửi thêm tài liệu, đọc rồi bổ sung vào nghiệp vụ và giải pháp.
- @author = `@szitphan` (đã xác nhận).
- Go-live 30/3/2027, nhưng không nặng về timeline. Tập trung vào giải pháp và USP.

## Phần 1 — Tổng quan (ĐÃ CHỐT)
- Tính năng: **dữ liệu liền mạch, liên kết** đi từ JobID sang Yêu cầu vận tải sang Lệnh vận tải và chiều ngược lại. Chuỗi này **gồm cả Quy trình cung cấp dịch vụ tổng quát** (mình đã hiểu thiếu phần này, user sửa). Mỗi việc làm phải kéo theo đủ chi phí.
- Pain (cả 5 đều đúng):
  - (a) nhập lại nhiều lần;
  - (b) giao việc qua điện thoại/Zalo, không truy được ai đang giữ việc;
  - (c) không thấy trước mốc SI/CY/DEM/DET nên bị phạt;
  - (d) chứng từ giấy về chậm nên chốt lệnh và tính chi phí chậm;
  - (e) chi phí chưa được hạch toán rõ ràng, đầy đủ.
- Phạm vi:
  - Gồm Điều phối 6 luồng, tạo và duyệt JobID (có AI01), ghi nhận chi phí/doanh thu lên JobID và Lệnh.
  - Bảng kê, công nợ, MISA: Điều phối chỉ đảm bảo dữ liệu đủ và đúng JobID, phần màn hình để feature riêng (mình đề xuất, user chưa phản đối).
  - Ý nào còn thiếu thì ghi thành câu hỏi mở, khách bổ sung sau.

## Điểm rút từ QTCCDV (đã đọc đủ 4.2–4.6, 5.1–5.5, phụ lục)
- **AI01** đọc chứng từ định danh. Người tạo xác nhận lại, chỗ sửa dùng làm dữ liệu huấn luyện. Trường hợp chọn thủ công phải thống kê lại.
- **Phạm vi dịch vụ và nhu cầu mua ngoài** khai khi tạo JobID, chỉ được đổi tại **một bước**.
- **Duyệt JobID** theo nợ quá hạn và hạn mức tín dụng. Trước khi giai đoạn 1 xong thì người tạo tự duyệt.
- **Kê khai tờ khai và QR**, sau đó phân luồng 3 hướng: Điều phối / Mua ngoài / Ghi nhận doanh thu.
- **Chi phí định mức hiện trường** tự áp lên JobID khi phân công.
- **Chi phí không hóa đơn** gắn vào Lệnh hoặc JobID. Hệ thống tự lập quyết định công tác hằng tháng.
- **"Lỗi phải có hệ quả":** có Lệnh nâng/hạ mà thiếu chi phí thì không cho lập bảng kê.
- **Trạng thái "Hoàn thành dịch vụ"** là lúc ghi nhận doanh thu/chi phí vào kỳ.
- Mục 5.3–5.5:
  - Chi phí mua ngoài khai theo JobID, có điều kiện trả trước/trả sau.
  - Chi phí trả hộ gắn mã JobID và nhóm phí.
  - Khi khách từ chối trả hộ do lỗi nhân viên: tăng chi phí trên JobID, có thể phát sinh bồi thường nội bộ.
  - JobID chia sẻ giữa chi nhánh thì đưa vào báo cáo giao dịch nội bộ, nên cần ghi chi nhánh nào làm phần việc nào.

## Phần 2 — Người dùng và quyền truy cập (ĐANG DỞ)
- Câu 1, vai trò: tạm thời gồm CS, nhân viên hiện trường, lái xe, điều vận, cán bộ quản lý, trợ lý AI, đại diện khách hàng, kế toán.
  - Hệ thống **phân quyền theo chức năng**, không cố định vai trò. Gọi là "quyền lái xe", "quyền hiện trường"…
  - Khi tạo dữ liệu nhóm quyền sẽ bổ sung các vai trò này.
  - **Lưu ý:** actor trong luồng và diagram vẫn ghi theo vai trò nghiệp vụ. Không để việc phân quyền làm thay đổi actor.
  - Cần bổ sung thêm 2 điểm: Điều vận cũng đưa chứng từ để tạo JobID; cán bộ quản lý duyệt thông tin viết hóa đơn bất thường.
- Câu 2, super app:
  - Dùng chung cho **nhân viên Delta nội bộ và nhân viên đối tác/khách hàng**.
  - Tạm thời làm cả web và mobile, sau này bỏ bên nào nếu không dùng.
- Câu 3 — phạm vi xem (CHỐT 2026-10-05): mặc định chỉ thấy JobID của chi nhánh mình. Xem chi nhánh khác do **feature Phân quyền** quyết, Điều phối không tự định nghĩa → brainstorm chỉ ghi "phạm vi dữ liệu theo Phân quyền". → OQ-16.
- Câu 4 — vào việc (CHỐT, user sửa): **MỌI vai trò đều có màn "Việc của tôi"** (+ thông báo đẩy mở thẳng việc; CS/ĐV thấy kèm cảnh báo mốc). Ngoài ra mỗi feature có màn danh sách riêng.
- Câu 5 — quy mô: CHƯA RÕ → OQ-17 hỏi khách; bổ sung thêm OQ quy mô sau.
- **Phần 2 ĐÃ XONG.**
- SRS mobile ĐÃ NHẬN (2026-10-05, SRC-23 `docs-input/srs-cu/srs-mobile/`). User chốt: là feature cũ đang phát triển (tài khoản/sửa chữa/sự cố/lịch nhắc/cấp dầu), KHÔNG feed brainstorm, để sau `/reverse-doc` (BL-033). Phần 2 câu 3–5 hỏi thẳng user, không chờ SRS. Tên app thống nhất: Delta Super App.

## Câu hỏi mở
- OQ-1: Chưa có tài liệu Quy trình điều vận (QTĐV).
- OQ-2: Thiếu file `Giao_nhan_hang_hoa_Sep18_2026.md`.
- OQ-3: Phụ lục Bảng thông tin JobID và Định mức chi phí còn trống.
- OQ-4: Phân chia lợi nhuận nội bộ chưa chốt.
- OQ-5: Phụ lục bảng kê doanh thu/chi phí còn trống.
- OQ-6: Chưa có cách xử lý bồi thường nội bộ khi khách từ chối trả hộ.
- OQ-7: Quy trình 5.10 (Quản lý quỹ và thanh toán) chưa phát triển.
- OQ-16: JobID có được chia sẻ hoặc đẩy (chuyển giao) sang chi nhánh khác không, cơ chế ra sao? (QTCCDV 5.5 đã nhắc JobID chia sẻ giữa chi nhánh → báo cáo giao dịch nội bộ, nhưng chưa rõ thao tác chia sẻ/đẩy.)
- OQ-18: Quản lý vỏ container swap (vỏ Delta/khách, sửa chữa vỏ) có thuộc phạm vi Điều phối không? (= OQ-14 cũ, user chốt để OQ)
- OQ-19 (hỏi khách): Khách có cung cấp số booking/tàu/chuyến (xuất) hoặc free time DEM/DET (nhập) ngay khi đặt xe, trước khi có Booking Note/Lệnh giao hàng không? SOP chỉ nói mốc lấy từ Booking Note (SI/CY) và Lệnh giao hàng/Thỏa thuận mượn cont (DEM/DET) — GNHH dòng 404–408.
- OQ-20: Người ký biên bản giao hàng phía khách là ai (thủ kho/bảo vệ/đại diện)? Có khách bắt buộc đóng dấu không? Lý do hỏi: quyết cách ký điện tử (ký trên máy lái xe + ghi tên vs OTP về SĐT người ký) và biên bản điện tử có thay được giấy không. Mẫu `chung-tu-mau/bien-ban-bat-thuong-hang-nhap.pdf` là biên bản bất thường của kho ALSC (hàng air), không phải biên bản Delta–khách → không trả lời được.
- OQ-21: Top cảng/depot Delta làm nhiều nhất? Lý do: ưu tiên cảng nào cho danh sách việc ePort theo cảng + xin kênh dữ liệu 2–3 cảng đầu.
- OQ-17 (hỏi khách): quy mô — JobID/ngày, số lái xe, nhân viên hiện trường, CS, điều vận theo chi nhánh (HN/HP/HCM/Lạng Sơn). Sẽ bổ sung OQ quy mô sau.
- OQ-22 (hỏi khách): Mẫu QR tờ khai hải quan thật — QR chứa những trường nào? (A2: lưu ảnh QR + thông tin bóc từ QR.)
- OQ-23 (hỏi kế toán/MISA): Gói MISA của Delta có lấy được hoá đơn ĐẦU VÀO không, có đủ 100% không? Hoá đơn trả hộ ghi MST của ai? (A9 — SOP chỉ mô tả MISA chiều phát hành, QTCCDV:1132-1152.)
- OQ-24 (hỏi khách): QR trên Lệnh giao vỏ điện tử (SRC-12, mẫu CNTRHUB…) chứa gì, bãi nào phát hành? Mới có 1 mẫu. (A6.)
- OQ-25 (hỏi khách duyệt): Danh sách lý do bắt buộc khi CS bấm "Chuyển cho hiện trường" (B2): Bãi yêu cầu có xe mới chọn vỏ · Ngoài giờ làm việc · ePort lỗi/không thao tác được · Khác (bắt ghi chú). Khách duyệt/thêm/bớt.
- OQ-26 (hỏi khách): Ca trực ngoài giờ — SOP (sop-dieu-phoi.md:417-421) chỉ định nghĩa: CBQL phân công NV hiện trường trực 17h30–8h theo ngày + người trực có quyền như CBQL để tự giao việc. CHƯA định nghĩa: xếp lịch trực theo vòng hay từng ngày; ngày không có người trực thì sao (cảnh báo ai?); việc người trực đang làm dở lúc 8h sáng chuyển cho ai; có trực cuối tuần/lễ không; một chi nhánh 1 hay nhiều người trực. (B3b)
- OQ-27 (hỏi khách xác nhận): Gộp giao việc làm Lệnh hạ vỏ rỗng theo **vận đơn + nơi hạ** (mỗi container vẫn 1 Lệnh hạ) có đúng thực tế không? Có trường hợp cùng vận đơn, cùng nơi hạ nhưng phải giao cho người khác nhau không? (B4)
- OQ-28 (hỏi khách): Ai bấm xác nhận "đã nhận tiền hoàn" cho khoản tiền nâng vỏ chờ hoàn 7 ngày (GNHH:462): người làm Lệnh nâng vỏ (tiền về TK của họ) hay kế toán? Quá hạn chưa về thì báo ai? (B5)
- OQ-29 (hỏi khách): Khi điều vận xác nhận khoản chi ngoài định mức với khách (E1), lưu bằng chứng khách đồng ý bằng cách nào? Phương án gợi ý: (1) đại diện khách bấm đồng ý trên Delta Super App; (2) đính kèm ảnh chụp tin nhắn/email khách đồng ý; (3) gửi link xác nhận qua email/tin nhắn để khách bấm; (4) chỉ ghi chú "đã gọi khách" + giờ gọi. Khách có chấp nhận (1)/(3) không, hay chỉ làm được (2)/(4)?
- OQ-30 (hỏi khách/kế toán): Rail (E3) — chuyến chưa có đơn giá trong phụ lục HĐ: giá xác định lần đầu được (a) lưu vào bảng giá dùng cho các chuyến sau (ghi ngày hiệu lực, chờ ký phụ lục), hay (b) chỉ dùng cho đúng chuyến đó tới khi có phụ lục mới? User nghĩ có cả 2 trường hợp → cần khách xác nhận khi nào áp (a), khi nào (b), ai quyết.
- OQ-31 (hỏi kế toán): Bảng "loại phí × địa điểm (ga/depot) → cách hạch toán" (E5): Thu nhập chịu thuế lái xe (trả kỳ lương) / Chi hộ (thu lại khách) / Trả hộ / Chi phí vận hành (module Vận tải). Nguồn hiện có GNHH:956, 978-982 (rail); các tuyến/loại hàng khác chưa có.
- OQ-32 (hỏi khách): Chi hộ Ratraco 5 bước (E4) — bước 5 "thủ quỹ chuyển tiền trả lái xe" (GNHH:984-987) giữ thủ công hay đi qua luồng chuyển khoản tự động (API Banking SRC-07, mục tiêu bỏ quỹ tiền mặt)?
- OQ-33 (hỏi khách): Phí lưu xe 72h + phí máy phát chiều thu CBT (E8, GNHH:789-793, 734) — khách xác nhận có muốn phần mềm tự tính đề xuất doanh thu không; đơn giá lưu xe / máy phát lấy theo HĐ khách nào; đơn vị tính (giờ / ngày / ca); giờ bắt đầu lấy từ geofence hay ảnh định vị check-in.
- OQ-34 (hỏi khách): Quá mốc vì kẹt xe/sự cố đường (container): SOP chỉ có 3 nhóm nguyên nhân (khách giao chậm / Delta điều xe chậm-xe hỏng / bên thứ ba) — sop-ban-do-kien-thuc.md:188. Có thêm nhóm thứ 4 "khách quan (kẹt xe, sự cố đường)" như hàng air không? Đổi cách quy trách nhiệm phí. (E7 câu 2 — hiện chốt phương án (a): chỉ gắn dữ liệu kẹt xe GPS làm bằng chứng.)
- Còn lại từ trước:
  - dòng "Cái này không cần" (bảng DEM/DET theo hãng);
  - hóa đơn lái xe trả hộ mang MST của ai;
  - khách có chấp nhận ký điện tử không.

## Việc cần làm tiếp
1. (Xong) SRS mobile đã intake — không dùng cho brainstorm.
2. Hỏi nốt câu 3–5 của Phần 2 trực tiếp user.
3. **GATE trước Phần 3:** 4 báo cáo `/discover` mới là **bản nháp, user CHƯA đọc lại và CHƯA quyết**. Phải lấy quyết định của user cho từng chủ đề (làm / không làm / điều chỉnh) trước. Chưa có quyết định thì KHÔNG chạy Phần 3. Không được coi kết luận trong báo cáo là quyết định.
   - 4 chủ đề cần quyết:
     - container-deadline-alerts (cảnh báo mốc);
     - electronic-delivery-record (biên bản giao hàng điện tử);
     - eport-integration (kết nối ePort);
     - field-document-reading (đọc chứng từ hiện trường).
   - Khi đã có quyết định: rà lại A1–A9, B1–B6, C theo nhãn [SOP to-be]/[SOP+]/[Mới], rồi bổ sung nhóm đề xuất về chi phí cho pain (e).
4. Phần 4–7 theo SKILL brainstorm, rồi quality gate, L1, Write `docs/dispatch-coordination/brainstorms/<slug>.md`.

## Đề xuất cũ (phiên 01/10), chưa gắn nhãn, cần rà lại ở Phần 3
- A, giảm nhập liệu:
  - AI đọc Booking Note/eDO, điền SI/CY/DEM/DET;
  - quét barcode/QR tờ khai thay cho OCR;
  - check-digit ISO 6346 cho số container;
  - chụp EIR để tự điền (giờ ra EIR nhận hàng là mốc tính DET);
  - kéo tracking từ ePort;
  - quét QR lệnh giao vỏ;
  - biên bản giao hàng điện tử ký trên app, chặn "Rời điểm" khi chưa ghi bất thường;
  - AI đọc phiếu cân để ra VGM, AI đọc hóa đơn lái xe.
- B, quy trình:
  - phân luồng theo cặp cảng × hãng tàu (danh mục có cột "Có xe chọn vỏ") và thuộc tính "ePort nhưng thanh lý offline";
  - nút "Chuyển cho hiện trường" thay cho "từ chối";
  - gợi ý người nhận việc, tự phân ca trực;
  - gộp giao việc Lệnh hạ;
  - theo dõi khoản chờ hoàn 7 ngày;
  - cảnh báo mốc có soạn sẵn email, chia 3 nhóm nguyên nhân.
- C, thiết bị: phiên trước đề xuất "mỗi vai trò một app". **Đã bỏ**, thay bằng super app.

## Nạp SOP Giao nhận hàng hóa 18/9/2026 (2026-10-02) — impact & gap
Nguồn: `docs-input/sop/giao-nhan-hang-hoa/giao-nhan-hang-hoa.md` (đã đọc I–III; Đính kèm 01–05 trùng nguồn có sẵn). OQ-2 ĐÓNG.
SOP Điều phối tự tham chiếu file này ("Giao nhận hàng hóa tại cảng/bãi"). 6 luồng ĐP = FCL/LCL/air × X/N. CBT (J07) + rail (J08–J11) đi thẳng YCVT → Lệnh (bỏ qua ĐP) → rơi vào QTĐV chưa có (OQ-1); GNHH tạm là nguồn duy nhất.
- Phạm vi: +CBT (sầu riêng Thái/VN, TQ–CPC, Bắc–Nam đối ứng), +đường sắt Ratraco (Đông Anh/Yên Viên, Trảng Bom/Sóng Thần). CHỜ user quyết: CBT/rail vào brainstorm ở mức Lệnh?
- Pain mới: (a) CBT đổi pháp nhân thanh toán → âm/dương, hủy JobID/Lệnh làm lại [SOP to-be: DK05 mẹ-con, J07 chọn bên xuất HĐ sau Lệnh]; (b) Zalo khắp nơi: nhóm chứng từ, "Lái xe CBT_Delta", chat trưởng ga, nhiệt độ 3–4 lần/ngày; (c) mốc mới: cut-off CFS (sớm 1–2 ngày so CY), cut-off air 4–6 giờ, free time lưu kho CFS/air, lưu xe 72h CBT (chiều THU), máy phát 24h tại TQ; rail không mốc; rớt chuyến air 4 nhóm nguyên nhân (+khách quan); (d) mã vạch gốc air phải về CS→khách (căn cứ thanh toán), tally, phiếu cân, biên bản biến thể theo loại hàng; (e) ngưỡng 5tr, CBT có/không HĐ, chi ngoài định mức phải duyệt TRƯỚC, rail: depot 150k/160k ghi Lệnh=thu nhập chịu thuế lái xe, tài 2/bốc xếp → lương, chi hộ Ratraco 5 bước (LX→ĐV bảng kê→CS→CBQL duyệt→thủ quỹ), doanh thu rail 2 kỳ (25 + cuối tháng), đơn giá theo phụ lục HĐ (thiếu hỏi anh Vũ).
- Actor mới: kho CFS, co-loader, đại lý/NVOCC, kho hàng không, HQ giám sát kho, đối tác Lào/TQ/Thái, vựa sầu riêng, đơn vị khai thuê HQ cửa khẩu, Ratraco (khách) + phòng giao nhận/trưởng ga, xe nâng, thủ quỹ (nội bộ mới), tài 2, Trasas(?).
- Câu 3/5 Phần 2 có dữ liệu một phần: điểm hoạt động HN/HP/HCM/Lạng Sơn (trucking hub); HCM rail ~16 xe (Bình Thung 5 + Trảng Bom 11).
- Ứng viên đề xuất mới: checklist ảnh định vị bắt buộc theo loại hàng/mốc [SOP+]; nhật ký nhiệt độ + lệnh chỉnh nhiệt có xác nhận [SOP+]; xin chi ngoài định mức trước khi chi [SOP+]; đồng hồ lưu xe 72h tự tính phí [SOP+]; chặn lập Lệnh khi hàng chưa sẵn sàng/kiện chưa về đủ [SOP+]; đối chiếu tên kho D/O vs Lệnh [SOP+]; gợi ý ghép LCL/air [SOP+]; rail: nhập kế hoạch n-1 → Lệnh hàng loạt, cổng trưởng ga/Ratraco, shipment list + bảng kê 2 kỳ tự sinh [SOP+]; bảng giá phụ lục tự áp, thiếu giá thì cờ [SOP+]; gợi ý hàng đối ứng [Mới]; theo dõi chứng từ gốc (mã vạch) [SOP+].
- OQ mới: OQ-8 4 quy trình chờ Trasas + Trasas là ai; OQ-9 định danh JobID rail (SOP tự nêu); OQ-10 thuế khoản chi hộ Ratraco không HĐ đầu vào; OQ-11 lệch BC quản trị vs thuế (CBT) cần kế toán xác nhận; OQ-12 CBT/rail thuộc QTĐV chưa có; OQ-13 ai nhập đơn giá rail khi thiếu phụ lục; OQ-14 quản lý vỏ container swap (Delta/khách, sửa chữa) có thuộc phạm vi; OQ-15 địa chỉ 4 ga trống. DEM/DET: dòng "không cần" đã bỏ → nghiêng giữ bảng, cần xác nhận.
- Discover: mốc → mở rộng đa loại hàng + chiều thu; biên bản → template theo 5 loại hàng (+ký người nhận TQ); ePort → chỉ container, tỷ trọng giảm; đọc chứng từ → +D/O (tên kho), giấy báo hàng đến (split), mã vạch, phiếu cân, tally, tờ khai CBT, bảng điện reefer.

## Bối cảnh nạp từ 4 báo cáo /discover (2026-10-05) — VẪN LÀ NHÁP, CHƯA PHẢI QUYẾT ĐỊNH
- Mốc SI/CY/DEM/DET: nghiêng "làm, 2 bước" (Bước 0 thêm cột vào bảng kế hoạch + xin kế toán số liệu phí; Bước 1 theo dõi + xử lý cảnh báo trong phần mềm). Điểm khác biệt: gắn mốc với Lệnh vận tải + 3 nhóm nguyên nhân (đối thủ VN không làm; Dockflow/BuyCo hướng forwarder/chủ hàng). Mốc theo loại lô (xuất SI/CY, nhập DEM/DET); DET hệ thống tự tính từ giờ EIR; mốc "dự kiến"/"đã xác nhận". Giữ chỗ 4 mốc trong dữ liệu ngay.
- Biên bản điện tử: nghiêng "làm, tách A/B". A = ghi nhận giao hàng có cấu trúc trên Super App, tự điền từ Lệnh, bắt buộc có/không bất thường + ảnh chì/hàng trước khi hoàn tất, kèm ảnh biên bản giấy, chạy khi mất sóng. B = khách ký trên máy lái xe, chạy thử với khách đồng ý, lối thoát khi khách từ chối.
- ePort: nghiêng "không kết nối lúc này". 36 cảng (25 có ePort), 88 depot (14 có), CFS/kho air không có. Không cho máy đăng nhập hộ. Làm: hỗ trợ CS danh sách việc theo cảng + lưu lệnh/EIR về Lệnh; thử tracking 10 container HP; đo lượt theo cảng. (Chưa đọc SRC-11 eport-qr-thanh-toan.)
- Đọc chứng từ: nghiêng "làm, quyết theo loại". EIR ưu tiên 1 (giờ/số cont/số chì, check-digit ISO 6346, người xác nhận); phiếu cân hoãn; hoá đơn điện tử lấy qua MISA không đọc ảnh; phiếu thu giấy nhập tay có ảnh bên cạnh.
- 4 báo cáo viết trước khi nạp SOP GNHH 18/9 → chưa phủ CFS/air/CBT/rail (xem mục SOP 18/9 ở trên).


## Phần 3 — GATE ĐÃ MỞ (2026-10-05): user quyết cả 4 báo cáo = LÀM NGAY, đồng ý mọi đề xuất điều chỉnh
- Mốc: đưa theo dõi + xử lý cảnh báo vào phạm vi ngay (không đo trước); +mốc CFS cut-off, air cut-off, free time kho, lưu xe 72h CBT. Leo thang → **trưởng điều vận**. Bảng free time DEM/DET theo hãng tàu: GIỮ (bản 18/9 bỏ ghi chú "Cái này không cần", giữ yêu cầu — GNHH dòng 418; bản cũ commit 8f48584 `sop-giao-nhan-container.md:204`).
- Biên bản: làm A + B (B chạy thử), mẫu theo 5 loại hàng.
- ePort: không kết nối; hỗ trợ CS danh sách việc theo cảng, lưu lệnh/EIR về Lệnh.
- Đọc chứng từ: EIR ưu tiên 1 + D/O (tên kho), mã vạch air, tally; phiếu cân hoãn; HĐ điện tử qua MISA. **Ai chụp người đó xác nhận** (lái xe/hiện trường), không đẩy cho ĐV.
- Câu 8: CBT + rail Ratraco VÀO brainstorm ở mức Lệnh + chi phí.

## Nạp SRC-05/06/07 (2026-10-05)
- SRC-06 Dữ liệu vận hành xe 30/9 (bản mới của SRC-05 EUP & Điều vận 19/9): GPS + sensor dầu EUP qua webhook → Delta MIS. Mục tiêu: điều xe tự động, **cập nhật Lệnh tự động**, **duyệt Lệnh tự động theo tiến trình xe**. 7 chức năng: ETA (Google Maps chỉ gọi khi bắt đầu Lệnh/kẹt/sai lộ trình/≤30' cho tuyến >300km), **geofence "đã đến" ghi lên Lệnh**, kẹt xe (<5km/h >10') → bù dầu định mức, idling (0km/h nổ máy >10') × định mức lít/giờ theo loại xe, hút dầu (vd giảm >5L/<3'), đối soát dầu thực đổ vs phiếu cấp dầu (vd tăng >20L/10'), trạm vé polygon + đối soát VETC → "Đã qua"/"Tránh trạm vé", km GPS vs km Lệnh.
  → Liên quan Điều phối: ETA/geofence = giờ thật cho cảnh báo mốc + tự chuyển trạng thái Lệnh (giảm thao tác LX) [SOP+]; vé cầu đường/bù dầu = chi phí tự ghi lên Lệnh (pain e). Phần dầu/hút dầu thuộc feature Cấp dầu/xưởng (SRS mobile Epic 06) → chỉ tham chiếu.
- SRC-07 Hóa đơn trả hộ 1/10: **~7.000 hoá đơn trả hộ/tháng** (local charges, facility, nâng hạ, lưu kho CFS/air, vệ sinh, lưu bãi). Yêu cầu thanh toán tạo từ JobID (CS/HT) hoặc **từ Lệnh (lái xe)** → chi phí từ Lệnh chuyển lên JobID; QR động/tĩnh hoặc chọn người nhận từ danh mục (cảng bãi/đại lý/hãng tàu/kho air/CFS); QL duyệt theo phân quyền; QR còn <3' → trả lại tạo mã mới; UNC qua API MB/VCB/TPBank, chủ TK duyệt OTP trên app ngân hàng; định tuyến pháp nhân Delta HN/HCM/HP; nội dung CK tự điền JobID + vận đơn/booking + tên phí + khách; mapping mã FT ↔ JobID. HĐ GTGT: phần mềm giao CS/HT **gần lái xe nhất** theo luồng phân công Lệnh thu thập & upload. Hạn mức đồng chủ TK: QL nghiệp vụ 50tr/ngày, 15tr/lệnh; QL hiện trường 30tr/ngày, 10tr/lệnh. Mục tiêu: bỏ quỹ tiền mặt tạm ứng.
  → Liên quan Điều phối: trả hộ phát sinh tại hiện trường gắn Lệnh/JobID (pain e, d); quy tắc "giao việc cho người gần lái xe nhất" dùng cho phân công. MST trên hoá đơn trả hộ vẫn CHƯA trả lời (tài liệu chỉ nói "HĐ GTGT nếu có").
- 7.000 HĐ trả hộ/tháng là số quy mô đầu tiên (gợi ý cho OQ-17).

## Phần 3 — vòng rà đề xuất (2026-10-05, đang dở)
Đã gửi bảng A1–A9, B1–B6 (B3 tách a/b), E1–E8 (chi phí pain e), D1–D9 (từ GNHH 18/9) + câu sót Phần 2 (tác vụ chính/tần suất/hậu quả → bảng 3.1).
User trả lời nhóm A:
- A1 OK [SOP+]. A4 OK. A5 OK. A7 OK.
- A2: lưu CẢ ảnh QR lẫn thông tin tờ khai bóc từ QR. → cần mẫu QR tờ khai thật để biết QR chứa trường nào (OQ-22).
- A3: user hỏi để làm gì → đã giải thích (khoá nối Lệnh–EIR–mốc DEM/DET–phí nâng hạ; bắt sai gõ/AI đọc sai ngay). Chờ quyết.
- A6: user hỏi SRC-12 → mẫu Lệnh giao vỏ điện tử mã CNTRHUB…, có QR + Booking/SizeType/Container. Chỉ 1 mẫu, chưa biết QR chứa gì + bãi nào phát hành. Chờ quyết.
- A8: user hỏi vì sao hoãn → lý do báo cáo: không có mẫu đọc phiếu cân VN, sai trọng lượng = sai VGM, không kiểm chéo tự động được, chưa có khối lượng/tháng. Đề xuất phương án giữa. Chờ quyết.
- A9: user yêu cầu kiểm MISA có lấy đúng 100% hoá đơn không → SOP chỉ mô tả MISA meInvoice chiều PHÁT HÀNH (QTCCDV:1132-1152); chiều lấy hoá đơn ĐẦU VÀO không có trong SOP. Không đảm bảo 100% → OQ-23 cho kế toán/MISA.
- 2026-10-06 user chốt tiếp nhóm A:
  - A2 OK (lưu ảnh QR + thông tin tờ khai bóc từ QR; OQ-22 mẫu QR).
  - A3 OK — check-digit ISO 6346 cho số container.
  - A6 OK — quét QR Lệnh giao vỏ (mức nhẹ; SRC-12 chỉ 1 mẫu, ghi OQ nội dung QR/bãi phát hành).
  - A8 LÀM LUÔN (không hoãn) — AI đọc phiếu cân ra VGM nhưng BẮT BUỘC người xác nhận (ai chụp người đó xác nhận) trước khi lưu.
  - A9 OK — MISA nguồn chính; không khớp → chụp + nhập tay, cờ "chưa khớp HĐĐT"; OQ-23 kế toán.
  - → NHÓM A ĐÃ CHỐT HẾT. Còn B, E, D + câu sót Phần 2.
  - Bảng E/D gốc chỉ nằm trong chat phiên 05/10 → dựng lại từ ghi chú nguồn phiên 06/10.
- 2026-10-06 rà lại căn cứ nhóm B (user xin mô tả chi tiết):
  - B1 căn cứ: sop-dieu-phoi.md:1480-1484 (SOP tự hỏi "phân biệt cảng bãi có thuộc tính này trên danh mục thế nào???") + danh-muc-dia-diem-hang-tau.md:50 (cột "Có xe chọn vỏ", "ePort").
  - B2 căn cứ: sop-dieu-phoi.md:787 (TH2) + :815 (TH5) — CS "từ chối" = chuyển JobID sang 5.1.2.3.
  - B3b SỬA NHÃN [Mới] → [SOP to-be]: sop-dieu-phoi.md:417-421 đã yêu cầu CBQL phân công NV hiện trường trực 17h30–8h theo ngày + quyền như CBQL để tự giao việc. Phần "tự xếp lịch" mới là [SOP+].
  - B5 SỬA CĂN CỨ: GNHH:462 (từ chối vỏ → hoàn tiền nâng sau 7 ngày về TK người làm Lệnh); sop-ban-do-kien-thuc.md:233 (chưa có giải pháp ghi nhận). Không phải QTCCDV.
  - B6: SOP có 3 nhóm nguyên nhân ghi tay; leo thang đã chốt 05/10 (trưởng điều vận); phần còn quyết = soạn sẵn văn bản báo khách/hãng tàu + bắt buộc chọn nguyên nhân khi quá hạn (research deadline:115).
- 2026-10-06 user chốt nhóm B (đợt 1):
  - B1 LÀM — thêm thuộc tính "Thanh lý tờ khai: online / tại bãi" vào danh mục cảng/bãi; phần mềm phân luồng theo 3 thuộc tính (ePort, có xe chọn vỏ, cách thanh lý). Ai cập nhật danh mục: **người có quyền (theo Phân quyền chức năng)**, không gán cứng vai trò.
  - B2 LÀM — đổi nút "Từ chối" → "Chuyển cho hiện trường", **bắt buộc chọn lý do**; quyền thanh toán tự chuyển sang hiện trường. Không tính USP.
  - Còn chờ: B3a, B3b, B4, B5, B6.
- 2026-10-06 user chốt nhóm B (đợt 2) → NHÓM B CHỐT HẾT:
  - B3a LÀM — gợi ý 2–3 người nhận việc (gần cảng/bãi, số việc đang ôm, trong ca trực), quản lý vẫn bấm chọn; dùng chung quy tắc "gần lái xe nhất" với SRC-07.
  - B3b LÀM phần SOP [SOP to-be] (phân công trực theo ngày + quyền tự giao việc trong ca, hết ca thu quyền). Phần SOP chưa định nghĩa → OQ-26.
  - B4 LÀM — gộp giao việc Lệnh hạ vỏ theo **vận đơn + nơi hạ**, mỗi container vẫn 1 Lệnh hạ; theo dõi "đã làm x/n". Khách xác nhận → OQ-27.
  - B5 LÀM — khoản chờ hoàn gắn Lệnh/JobID, hạn 7 ngày, cảnh báo quá hạn; phí đổi vỏ ghi chi phí phát sinh của Lệnh. Ai bấm "đã nhận tiền hoàn" → OQ-28.
  - B6 LÀM cả 3 điểm: bắt chọn nhóm nguyên nhân khi quá hạn (+ nhóm "do nhà vận tải" theo discover), văn bản soạn sẵn báo khách/hãng tàu, mỗi cảnh báo có người phụ trách + trạng thái "đã xử lý". Kênh gửi: **email**, hoặc **copy nội dung**, hoặc **xuất file** để gửi qua các kênh tin nhắn.
  - Còn lại Phần 3: nhóm E, nhóm D (trình bày chi tiết như B), câu sót Phần 2.
- 2026-10-06: đã viết trang đọc hiểu nghiệp vụ `docs/_shared/logistics-primer.html` cho user (không phải output brainstorm).
- 2026-10-06 rà căn cứ nhóm E trước khi trình chi tiết — SỬA NHÃN:
  - E1 [SOP+]→[SOP to-be]: SOP đã bắt xin trước chi ngoài định mức (GNHH:778, 823, 852 — CBT). Phần [SOP+] = làm trên app + gắn Lệnh + chặn hoàn nếu chưa duyệt + mở rộng cho mọi loại hàng.
  - E2 viết lại: ngưỡng 5tr là quy tắc CÁCH TRẢ (tiền mặt tạm ứng <5tr / chuyển khoản >5tr; HT >5tr báo CS) — GNHH:495, 586, 680; không phải ngưỡng duyệt. CBT chia chi phí có/không hoá đơn (GNHH:704-716).
  - E3 [SOP+]: rail nhập giá theo phụ lục HĐ, thiếu hỏi anh Vũ (GNHH:1000).
  - E4 [SOP to-be]: 5 bước chi hộ Ratraco (GNHH:968-987).
  - E5 [SOP to-be] quy tắc + [SOP+] tự phân loại: depot 150k Nam Khánh/160k Phú Lợi = thu nhập chịu thuế LX, trả kỳ lương (GNHH:956); tài 2/bốc xếp → thu nhập chịu thuế LX (GNHH:976-980); chi hộ Ratraco không HĐ đầu vào (GNHH:999).
  - E6 [SOP to-be]: SRC-07 hoa-don-tra-ho:29-39, 55-89.
  - E7 [SOP+]→[SOP to-be]: SRC-06 đã mô tả vé trạm (VETC đối soát), kẹt xe bù dầu, idling (du-lieu-van-hanh-xe:70-110). Chi phí vận hành (dầu/ETC/lưu ca) thuộc module vận tải (GNHH:972) → Điều phối chỉ tham chiếu.
  - E8 [SOP+]: 72h lưu xe miễn phí đóng hàng + 72h tại cửa khẩu TQ, máy phát 24h (GNHH:789-793; Thái: 734). Cảnh báo 72h đã chốt 05/10 → E8 chỉ thêm tự tính phí lưu xe chiều thu.
- 2026-10-06 user chốt nhóm E (đợt 1):
  - E1 LÀM, áp cho MỌI loại hàng (không chỉ CBT). Hiện tại KHÔNG cần cấp quản lý duyệt thêm theo mức tiền — điều vận duyệt là đủ. Cách lưu bằng chứng khách đồng ý → OQ-29.
  - E2 LÀM — phần mềm tự đề xuất cách trả theo ngưỡng 5tr (<5tr tạm ứng; >5tr tạo việc cho CS phụ trách + kế toán), bắt chọn có/không hoá đơn. Lưu ý phụ thuộc E6 (nếu bỏ quỹ tiền mặt thì ngưỡng có thể đổi).
  - Còn chờ: E3–E8.
- 2026-10-06 user chốt nhóm E (đợt 2):
  - E3 LÀM — bảng giá phụ lục HĐ rail trong danh mục, Lệnh rail tự áp giá; thiếu giá → cờ "Chưa có đơn giá" + việc "Xác định giá" cho người có quyền; còn cờ thì chặn chốt kỳ (25 / cuối tháng). Giá xác định lần đầu lưu cho lần sau hay chỉ dùng 1 chuyến: có cả 2 trường hợp → OQ-30.
  - E4 LÀM — lái xe ghi khoản chi hộ Ratraco/cân xe ngay trên Lệnh (loại phí, số tiền, ảnh); phần mềm tự gom bảng kê chi phí cho điều vận xác nhận; tự gắn nhãn "chi hộ — phải thu lại" để lên bảng kê doanh thu Ratraco; cân xe chọn "khách trả trực tiếp"/"Delta trả". Bước 5 thủ công hay chuyển khoản tự động → OQ-32.
  - E5 LÀM — danh mục loại phí có thuộc tính cách hạch toán theo địa điểm, lái xe chỉ chọn loại phí, phần mềm tự xếp + tự điền định mức (150k Nam Khánh/160k Phú Lợi). Bảng quy tắc → OQ-31 (user nói OQ-30 nhưng số đó đã dùng cho E3).
  - E7 câu 1 OK — Điều phối chỉ HIỆN trên Lệnh (giờ đến thật, vé trạm, cờ tránh trạm, thời gian kẹt xe); ghi nhận/duyệt/bù dầu thuộc module Vận tải/Cấp dầu. Câu 2 CHỐT (a): dữ liệu kẹt xe GPS gắn làm bằng chứng vào cảnh báo quá mốc (B6) để thương lượng, KHÔNG đổi 3 nhóm nguyên nhân SOP. Phương án thêm nhóm "khách quan" → OQ-34.
  - E8 LÀM có điều kiện khách xác nhận — đồng hồ lưu xe từ giờ đến tới khởi hành, quá 72h tự đề xuất dòng doanh thu trên JobID, CS xác nhận; máy phát tương tự. Xác nhận + đơn giá/đơn vị → OQ-33.
  - E6 CHỐT TÁCH: Điều phối giữ nút tạo Yêu cầu thanh toán trên Lệnh/JobID, gắn chi phí đúng Lệnh/JobID, việc "Thu HĐ GTGT" cho người gần lái xe nhất (chung quy tắc B3a), hiện trạng thái thanh toán. Feature riêng "Thanh toán trả hộ" (SRC-07): duyệt hạn mức, QR, UNC/API Banking, OTP chủ TK, đối soát mã FT, định tuyến pháp nhân.
  - → NHÓM E CHỐT HẾT. Còn nhóm D + câu sót Phần 2.
- 2026-10-07 user chốt nhóm D (đợt 1) — bản D dựng lại 06/10 từ GNHH, D1–D10:
  - D1 LÀM — danh sách điểm chụp ảnh định vị bắt buộc theo loại hàng, thiếu ảnh thì CHẶN bước tiếp; trưởng điều vận duy trì danh sách.
  - D2 LÀM, rút gọn — yêu cầu chỉnh nhiệt vẫn nhắn qua kênh ngoài; trên app lái xe chỉ ghi nhận đã chỉnh + lý do (KHÔNG có object "Yêu cầu chỉnh nhiệt" do điều vận tạo). Nhật ký nhiệt: chu kỳ nhắc mặc định theo loại hàng, chỉnh được trên từng Lệnh. Khách nhận qua xuất file. (Chờ xác nhận: ghi nhận chỉnh nhiệt có bắt ảnh không — SOP :757 yêu cầu ảnh bằng chứng.)
  - D3 HOÃN QUYẾT — để lại sau (CFS chặn/cảnh báo; lô tách chuyến nhiều Lệnh/JobID hay 1 Lệnh nhiều lượt).
  - D4 CHƯA CHỐT — user: Lệnh tạo liền mạch lấy dữ liệu từ trước (D/O) nên không lệch? → đang làm rõ các trường hợp lệch còn lại.
  - D5 LÀM NGAY giai đoạn này — gợi ý ghép LCL/air (cùng kho/kho gần, cut-off, CBM/tải xe), điều vận chọn. Phụ thuộc dữ liệu tải xe + khoảng cách kho.
  - D6 LÀM — nhập kế hoạch Ratraco n-1 → Lệnh hàng loạt; mẫu kế hoạch Ratraco → OQ-35; trưởng ga chỉ NHẬN FILE (không tài khoản).
  - D7 ĐỒNG Ý phạm vi — Điều phối chỉ đảm bảo Lệnh rail đủ dữ liệu + tự vào đúng kỳ (25 / cuối tháng); màn shipment list/bảng kê là feature riêng.
  - D8 LÀM NGAY giai đoạn này [Mới] — gợi ý hàng chiều về cho xe CBT. Phụ thuộc dữ liệu YCVT nội địa trên phần mềm.
  - D9, D10 chưa trả lời.
- OQ-35 (hỏi khách): Kế hoạch ngày Ratraco gửi n-1 (D6, GNHH:870-874) có mẫu cố định không? Xin 1 mẫu thật để thiết kế nhập file/dán bảng.
- 2026-10-07 user chốt nhóm D (đợt 2) — THAY các mục tương ứng ở đợt 1:
  - D1 GIỮ như đợt 1 (chặn; trưởng điều vận duy trì).
  - D2 SỬA — nhật ký nhiệt dùng MỘT chu kỳ nhắc mặc định chung (không chia theo loại hàng), chỉnh được trên từng Lệnh; khách nhận qua file xuất. Còn chờ: giá trị mặc định; phần ghi nhận chỉnh nhiệt có giữ bản rút gọn đợt 1 + có bắt ảnh không.
  - D3 CHỐT (thay "hoãn") — kho CFS chưa sẵn sàng chỉ CẢNH BÁO; air chưa đủ kiện vẫn chặn tới khi CS chọn; lô tách chuyến = NHIỀU LỆNH dưới 1 JobID.
  - D4 CHỐT — nơi nhận trên Lệnh phải trùng tên kho trên D/O, không có trường hợp lệch được giữ. Chờ xác nhận cách hiểu: nơi nhận lấy thẳng từ D/O, không nhập tay; D/O đổi kho thì Lệnh cập nhật theo.
  - D5 LÀM NGAY (khẳng định lại).
  - D6, D7, D8 khẳng định lại như đợt 1 (D6 OQ-35 + trưởng ga chỉ nhận file; D7 chỉ lo dữ liệu Lệnh; D8 làm ngay).
  - D9 CHỐT — đánh dấu "cần chuyển mã vạch gốc" trên TỪNG JobID (không đặt ở danh mục khách DK05).
  - D10 CHỐT theo đề xuất — đổi bên xuất hoá đơn trên JobID được tới TRƯỚC KHI XUẤT HOÁ ĐƠN, không đụng Lệnh; bên thứ ba chưa có mã → việc "Đăng ký bên thanh toán" kèm thoả thuận ba bên. Người duyệt mã DK05 cấp 2 → OQ-36.
- OQ-36 (hỏi khách): Ai duyệt mã khách DK05 cấp 2 khi CBT đổi pháp nhân thanh toán sang bên mới (D10, GNHH:697-700)?
- 2026-10-07 user chốt nốt nhóm D:
  - D2 CHỐT — chu kỳ nhắc nhật ký nhiệt MAP THEO LOẠI HÀNG (mặc định theo loại hàng, chỉnh được trên Lệnh — thay ý "1 chu kỳ chung" đợt 2); khách nhận qua file xuất. Chỉnh nhiệt giữ bản rút gọn (yêu cầu nhắn kênh ngoài, lái xe ghi "đã chỉnh" + lý do), KHÔNG bắt ảnh → OQ-37.
  - D4 CHỐT — nơi nhận trên Lệnh lấy thẳng từ D/O, không nhập tay → không lệch; D/O đổi kho thì Lệnh cập nhật theo, xe đã giao thì báo điều vận.
  - → NHÓM D CHỐT HẾT. Phần 3 vòng rà đề xuất A/B/D/E xong. Còn câu sót Phần 2 (bảng 3.1).
- OQ-37 (hỏi khách): Khi lái xe chỉnh nhiệt theo yêu cầu khách/đại lý TQ, có bắt buộc chụp ảnh làm bằng chứng không? SOP GNHH:757 ghi "mọi yêu cầu chỉnh phải có hình ảnh làm bằng chứng" — đề xuất hiện tại chỉ ghi "đã chỉnh" + lý do.

## Phần 2 — câu sót bảng 3.1 (CHỐT 2026-10-07)
- Bảng tác vụ chính / tần suất / hậu quả theo 8 vai trò (bản em đề xuất trong chat 07/10) — user: tạm OK, chưa sửa.
  - CS: tạo JobID từ chứng từ; xử lý air chưa đủ kiện (D3); xác nhận doanh thu phát sinh (E8); giao chứng từ gốc (D9) · nhiều lần/ngày · sai → đi nhầm kho, thiếu doanh thu.
  - Điều vận: tạo Lệnh, xếp xe/lái xe; Lệnh rail hàng loạt (D6); ghép LCL (D5); duyệt chi ngoài định mức (E1); cảnh báo quá mốc · liên tục trong ca · sai → trễ cut-off, chạy rỗng, chi phí mất kiểm soát.
  - Lái xe: nhận Lệnh; ảnh điểm bắt buộc (D1); nhật ký nhiệt (D2); chi hộ (E4); chuyển bước · nhiều lần/chuyến · sai → thiếu bằng chứng tranh chấp.
  - Hiện trường: nhận việc gợi ý (B3a); phiếu cân → VGM (A8); mã vạch gốc (D9); thu HĐ GTGT · vài lần/ngày · sai → lỡ tàu, mất chứng từ.
  - Cán bộ quản lý: duyệt HĐ bất thường; xem cảnh báo · vài lần/ngày. Kế toán: nhận chi phí gắn Lệnh/JobID; trả >5tr (E2) · hằng ngày, dồn kỳ chốt.
  - Đại diện khách: theo dõi lô, nhận file xuất · thỉnh thoảng. Trợ lý AI: đọc chứng từ, gợi ý · tự động.
- Tần suất: CHƯA đo được → ghi định tính (như trên), không ghi số.
- Tác vụ phải nhanh nhất (ưu tiên tối ưu màn — dùng cho userflow Mục 3.6):
  - Lái xe: chụp ảnh, nhận Lệnh, thao tác nhanh trên Lệnh.
  - CS: theo dõi và xử lý các nghiệp vụ trong JobID.
  - Điều vận: màn theo dõi xếp xe + dữ liệu liên quan để ra quyết định.
  - Cán bộ quản lý: Việc của tôi (duyệt).
  - Nhân viên hiện trường: chụp.
- → PHẦN 2 XONG HẲN. Tiếp: Phần 3 luồng chính.

## Phần 3 — Luồng chính (2026-10-07)
- Xương sống 9 bước 0–8 (bản chat 07/10): user OK. 6 luồng phụ: user OK, yêu cầu đọc kỹ SOP — đã đọc đủ 5.1–5.6 sop-dieu-phoi.md, SỬA 2 điểm:
  - Bước 4 → YCVT CHỈ ĐÚNG với FCL. LCL xuất / air xuất / CFS nhập / air nhập: phần mềm tạo YCVT NGAY khi cán bộ quản lý giao việc (sop-dieu-phoi:1085-1095, 1257-1265, 1666-1670, 1798-1803); việc hiện trường (Phiếu nhập kho / Phiếu cân / Phiếu xuất kho) chạy SONG SONG với Lệnh. Nhập CFS/air: giao nhận 3 bên kho–hiện trường–lái xe gần như đồng thời (:1690, :1830).
  - FCL nhập (5.4, :1335-1429): bước 2 CS kê khai (giờ nhận cont tại cảng, hạn trả vỏ, bãi hạ vỏ, thông báo hãng tàu, tờ khai + số + QR) — CHƯA kê khai thì KHÔNG ai thanh toán được cho JobID (:1379); rồi CS trả hãng tàu lấy eDO, ghi hạn eDO + hạn trả vỏ, phí gia hạn, cược vỏ (:1381-1386). Phân luồng 2 TH (không phải 6): cảng có ePort → CS đổi eDO lấy Lệnh nâng hàng đủ mọi container trên vận đơn → tự thành YCVT, bỏ qua bước 3–4 (CS được từ chối → giao việc); không ePort → giao hiện trường lấy Lệnh nâng. Lái xe chụp EIR khi nhận cont + biên bản giao hàng. Lệnh hạ vỏ: ePort → CS làm (EIR + lệnh giao hàng + email nơi hạ vỏ); không ePort → lái xe tự làm.
  - Chung nhóm hàng lẻ/air: số kiện/CBM/kg (air: kích thước → chargeable weight, phần mềm tự tính CBM) từ tally/phiếu cân THAY số Booking Note trên JobID để tính cước (:1110-1120, :1290-1300). Xuất: lái xe chụp phiếu xuất kho của khách + thùng xe niêm phong nếu khách yêu cầu.
- Câu 3 thông báo khách theo mốc → OQ-38.
- OQ-38 (hỏi khách): Khách có cần nhận thông báo (email/Zalo/SMS) ở mốc nào không — xe đã đến kho/cảng, đã nhận hàng, đã giao xong, quá mốc? Hiện chỉ có "Việc của tôi" + thông báo đẩy nội bộ + khách nhận file xuất.
- OQ-39 (hỏi khách): Cảng có ePort nhưng hiện trường vẫn phải xuống thanh lý tờ khai offline (SOP Điều phối 5.4.2.2, :1395-1396, SOP tự ghi "???") — cảng nào? Đánh dấu thuộc tính này trên danh mục cảng/bãi thế nào?
- OQ-40 (hỏi khách): SOP 5.4.2.4 (:1409) ghi "Sau khi nhân viên CS upload đủ Lệnh nâng hàng" trong bước của nhân viên hiện trường — là hiện trường upload (lỗi chép) hay CS phải upload lại?
- 4e sơ đồ luồng chính v1 (chat 07/10): user OK thứ tự + người làm. JobID không đạt điều kiện nợ quá hạn/hạn mức → DỪNG HẲN, chờ khách thanh toán (không có duyệt ngoại lệ). OQ-40 tạm hiểu: hiện trường upload, vẫn hỏi khách xác nhận.
- User muốn doc có CẢ 2 loại: sơ đồ tổng + sơ đồ con từng luồng (FCL X/N, LCL X, air X/N, CFS N, CBT, rail). Đang trình v2.
