---
type: decision-log
status: draft
updated: 2026-10-13
links:
  - .claude/rules/decision-log.md
  - _workspace/interviews/dispatch-coordination-interview.md
  - docs/meetings/2026-10-10-oq-dispatch-coordination.md
  - docs/_product/srs-v2-change-log.md
  - design/design.md
  - design/_lab/refs/notes.md
---
# Sổ quyết định

> Mỗi dòng một quyết định đã chốt, kèm **lý do** và **phương án đã bỏ**. Doc trích bằng mã: `(DEC-012)`.
> Quyết định bị thay không xoá, đổi Trạng thái thành `thay bởi DEC-xxx`. Lý do không tìm thấy khi điền
> ngược ghi **⚠ chưa ghi lý do**, chờ người chốt bổ sung. Quy tắc: `.claude/rules/decision-log.md`.
>
> Điền ngược 2026-10-13 từ các chỗ "(chốt dd/mm)" trong `docs/`, `design/`, backlog và quy ước làm việc.
> Quyết định nghiệp vụ trong phỏng vấn và quyết định của khách KHÔNG chép lại ở đây — xem mục cuối.

## 1. Sản phẩm và phạm vi

| Mã | Ngày | Quyết định | Lý do | Phương án đã bỏ | Ai chốt | Nguồn / ghi ở | Trạng thái |
|---|---|---|---|---|---|---|---|
| DEC-001 | 2026-10-01 | Ngôn ngữ giao diện chỉ Tiếng Việt (mặc định) và Tiếng Anh | ⚠ chưa ghi lý do | Giữ Tiếng Nhật như UC02.03.01 | @szitphan | `docs/_shared/operating-environment.md` · CHG-02 | hiệu lực |
| DEC-002 | 2026-10-05 | CBT và đường sắt vào brainstorm ở mức Lệnh + chi phí | Chưa có Quy trình điều vận (OQ-1, OQ-12), lấy tạm GNHH 3.4–3.5 | — | @szitphan | `docs/meetings/decks/2026-10-06-oq-dispatch-coordination-deck.md` | thay bởi quyết định khách 10/10 (OQ-12): CBT, đường sắt không qua Điều phối · CHG-26 |
| DEC-003 | 2026-10-12 | Sản phẩm chuyển thành SaaS logistics bán nhiều khách, Delta là khách #1; mọi quy tắc mang nhãn tầng, con số đi qua mã `P-…` | Muốn bán sản phẩm thay vì chỉ làm outsource; quy tắc riêng Delta viết cứng vào lõi sẽ chặn bán cho khách khác | Tiếp tục làm hệ thống riêng cho Delta | @szitphan (lãnh đạo công ty) | `docs/_product/saas-core-vs-tenant.md` · `.claude/rules/saas-layer.md` | hiệu lực (còn kiểm quyền khai thác, BL-056) |
| DEC-004 | 2026-10-12 | VETC là nguồn chuẩn toạ độ và chi phí khi lệch Vietmap — tầng Lõi | ⚠ chưa ghi lý do | Vietmap làm nguồn chuẩn | @szitphan | `docs/_product/saas-core-vs-tenant.md` Mục 3.7 | hiệu lực |
| DEC-005 | 2026-10-12 | Delta Super App không có màn Bảng công nợ; sheet công nợ chỉ hiện trạng thái, không có nút mở | ⚠ chưa ghi lý do | Thêm màn Bảng công nợ trên app | @szitphan | `docs/cross-process-flow/srs/cross-process-flow-userflow.md` OQ-2 | hiệu lực |
| DEC-006 | 2026-10-12 | Mã quy trình `QT-[Mã chi nhánh]-[YY]-[XXXX]`, đánh lại theo năm; là tham số `P-mau-ma-quy-trinh` | Mẫu mã khác nhau theo khách nên đi qua tham số (SaaS, DEC-003) | ⚠ chưa ghi | @szitphan | `docs/_product/tenant-parameters.md` · cross-process-flow OQ-10 | hiệu lực |
| DEC-007 | 2026-10-12 | GR-11: yêu cầu có mã yêu cầu, duyệt xong mới có mã bản ghi | ⚠ chưa ghi lý do | ⚠ chưa ghi | @szitphan | `design/ui-common/conventions.md` GR-11 · cross-process-flow OQ-9 · BL-063 | hiệu lực |
| DEC-008 | 2026-10-12 | Chưa thêm CMP Checklist và Form theo bước vào component chung | Đợi có feature thứ 2 dùng mới đáng tách thành component chung | Thêm ngay từ brainstorm Liên quy trình | @szitphan | BL-052 | hiệu lực |
| DEC-009 | 2026-10-12 | Vẽ đủ 4 userflow Figma Liên quy trình trước khi khách trả lời OQ-3…OQ-31, không gắn link màn | ⚠ chưa ghi lý do (chấp nhận rủi ro: OQ đổi luồng thì sửa từng frame) | Chờ khách trả lời OQ rồi mới vẽ | @szitphan | BL-058 | hiệu lực |
| DEC-010 | 2026-10-12 | SRC-04 (`sop-ban-do-kien-thuc.md`) là bản BA tự viết → ➖, không lập sổ đối chiếu | Tránh đếm trùng với SRC-01…03 (nguồn gốc của khách) | Lập sổ đối chiếu như nguồn khách | @szitphan | BL-071 · `docs-input/README.md` | hiệu lực |
| DEC-011 | 2026-10-11 | Tách nghĩa CMP-09: quy trình nhiều nghiệp vụ → CMP-09 Liên quy trình · vòng đời 1 bản ghi → nhãn trạng thái + Lịch sử (CMP-08) · form nhiều bước → CMP "Form theo bước" · việc phải làm → CMP "Checklist" | CMP-09 đang bị dùng cho 4 nghĩa khác nhau, wireframe gọi sai nghĩa (BL-053) | Giữ CMP-09 bao cả 4 nghĩa | @szitphan | `docs/cross-process-flow/brainstorms/cross-process-flow.md` Mục 2 | hiệu lực |

## 2. Design system và giao diện

| Mã | Ngày | Quyết định | Lý do | Phương án đã bỏ | Ai chốt | Nguồn / ghi ở | Trạng thái |
|---|---|---|---|---|---|---|---|
| DEC-012 | 2026-09-29 | Lỗi mạng ở Thông báo: `EmptyState` giữa panel + nút Thử lại, giữ tab | Giữ tab để người dùng vẫn chuyển được | Banner lỗi | @szitphan | `design/design.md` § Notification Center · cross-process-flow-spec | hiệu lực |
| DEC-013 | 2026-10-01 | Phân trang: trang hiện tại dùng trạng thái chọn sẵn của `Pagination` (`{colors.accent}`), không xanh lá như SC-04 | Theme Neutral không dùng màu brand cho điều hướng | Xanh lá theo SC-04 | @szitphan | `design/design.md` § Pagination | hiệu lực |
| DEC-014 | 2026-10-01 | Đổi bộ lọc, tìm, sắp xếp hoặc số dòng/trang → về trang 1 | ⚠ chưa ghi lý do (SC-04 không nói, KG-17) | — | @szitphan | `design/design.md` § Pagination | hiệu lực |
| DEC-015 | 2026-10-01 | Tuỳ chỉnh cột không có panel: ẩn/ghim/sắp xếp trên tiêu đề cột, kéo tiêu đề để đổi thứ tự, không có nút "Áp dụng" | Người dùng thấy kết quả ngay trên bảng | Panel tuỳ chỉnh cột theo SC-06 gốc | @szitphan | `design/design.md` § Table | hiệu lực |
| DEC-016 | 2026-10-01 | Giá trị rỗng trong bảng: Ghi chú để trống · ID/Mã `N/A` · cột khác `-` | Theo `web-common-rules.md` 2.10 | ⚠ chưa ghi | @szitphan | `design/design.md` § Data display | hiệu lực |
| DEC-017 | 2026-10-01 | Chấp nhận Timer hiện `12m 05s` trên giao diện tiếng Việt | Code không dịch h/m/s (gắn cứng trong `Timer.tsx`); cần trung tính thì dùng Format = Clock | Sửa component để dịch đơn vị | @szitphan | `design/design.md` § Timer | hiệu lực |
| DEC-018 | 2026-10-04 | Mobile dùng chung quy tắc web: giá trị rỗng `-` (không `--`), textarea tối đa 1000 (không 4000), badge thông báo tối đa `9+` (không `99+`) | Một quy tắc cho cả web và app; tài liệu app cũ lệch web | Giữ số của tài liệu app | @szitphan | `design/ui-common/conventions.md` · `design/ui-common/screen-patterns.md` | hiệu lực |
| DEC-019 | 2026-10-04 | Lịch sử hoạt động trên mobile mở `BottomSheet`, không phải màn riêng | ⚠ chưa ghi lý do (chỉ ghi "theo design.md") | Màn riêng theo MSC-05 | @szitphan | `design/ui-common/screen-patterns.md` CMP-08 | hiệu lực |
| DEC-020 | 2026-10-06 | Khung mobile M1 dùng Bottom Navigation, không hamburger/`MobileNav` | ⚠ chưa ghi lý do | Hamburger + `MobileNav` | @szitphan | `design/design.md` § Mẫu M1 | hiệu lực |
| DEC-021 | 2026-10-06 | Tab Bottom Navigation chỉ icon, ẩn chữ (chữ giữ làm nhãn truy cập) | ⚠ chưa ghi lý do (chỉ ghi "sau khi so với bản icon + nhãn") | Icon + nhãn | @szitphan | `design/design.md` § Bottom Navigation | hiệu lực |
| DEC-022 | 2026-10-06 | Khung Figma mobile luôn hiện Status bar và Home indicator | ⚠ chưa ghi lý do | Ẩn theo màn | @szitphan | `design/design.md` § Device Frame | hiệu lực |
| DEC-023 | 2026-10-09 | Xác nhận trên mobile dùng bottom sheet, phương án B của `lab-confirm.html` | ⚠ chưa ghi lý do | Các phương án khác trong lab | @szitphan | `design/ui-common/screen-patterns.md` · `design/_lab/lab-confirm.html` | hiệu lực |
| DEC-024 | 2026-10-09 | Ảnh xe góc 3/4 ~35° như ảnh mẫu | Khớp ảnh mẫu | ⚠ chưa ghi | @szitphan | `design/_lab/refs/vehicle-shot-spec.md` Mục 9 | hiệu lực |
| DEC-025 | 2026-10-12 | Khung trang dự án theo số đo đã chốt ở lab, thắng số mẫu Astryx | Kết quả so Lab ↔ DS (notes.md dòng 07–09) | Số đo mẫu Astryx | @szitphan | `design/design.md` § Layout · `design/_lab/refs/notes.md` | hiệu lực |
| DEC-026 | 2026-10-12 | Mã nghiệp vụ dùng `{typography.code-sm}` 12/16, không bao giờ cắt | Đồng nhất mã ở thẻ, dòng, panel; mã cắt thì không tra được | — | @szitphan | `design/design.md` § Typography | hiệu lực |
| DEC-027 | 2026-10-12 | Ngoại lệ viết hoa: nhãn nhóm menu và tên cột đầu bảng | Đây là nhãn phân vùng, không phải chữ đọc liền; giữ như bản trước. Chấp nhận nhãn nhóm menu #8F8F8F chỉ đạt 3.23:1 | Bỏ viết hoa theo Typography › Principles | @szitphan | `design/design.md` § Typography · notes.md | hiệu lực |
| DEC-028 | 2026-10-12 | Tên cột đầu bảng Inter 12/16 đậm 500, màu `text-secondary` | Giảm nổi bật so với dữ liệu (vòng 3) | Đậm hơn ở vòng 1–2 | @szitphan | `design/design.md` § Typography | hiệu lực |
| DEC-029 | 2026-10-12 | Chip trạng thái theo lab: 7 sắc, icon 14 thay chấm, mọi chip là instance `Chip trạng thái` | ⚠ chưa ghi lý do (chỉ ghi "theo lab") | Chip của thư viện Astryx | @szitphan | `design/design.md` § Ánh xạ trạng thái nghiệp vụ | hiệu lực |
| DEC-030 | 2026-10-12 | Chip trạng thái chế độ tối = phương án B (biến `Status Chip/*` mode Neutral Dark) | ⚠ chưa ghi lý do | Phương án A | @szitphan | `design/_lab/refs/notes.md` | hiệu lực |
| DEC-031 | 2026-10-12 | Quy chuẩn icon: Lucide, nét theo cỡ (1.8/24), cỡ 16/14, bảng icon theo hành động | ⚠ chưa ghi lý do (theo lab `.ic`) | Nét 1.333 của thư viện Figma | @szitphan | `design/design.md` § Iconography | hiệu lực |
| DEC-032 | 2026-10-12 | Bo góc nút: web 10px, mobile tròn hẳn; nút chính mobile cao 40 | ⚠ chưa ghi lý do (theo lab) | Cùng bo góc cho cả 2 nền tảng | @szitphan | `design/design.md` § Button | hiệu lực |
| DEC-033 | 2026-10-12 | Thanh công cụ PowerSearch: tìm + chip trong 1 ô; bỏ nút Sắp xếp | ⚠ chưa ghi lý do | — | @szitphan | `design/_lab/refs/notes.md` "Áp quyết định vào lab" | thay bởi DEC-034 |
| DEC-034 | 2026-10-12 | Thanh công cụ 2 hàng: hàng 1 ô tìm + Bộ lọc + Tuỳ chỉnh cột + Nhóm, hàng 2 chip điều kiện | Nhóm điều khiển luôn đứng yên dù có bao nhiêu chip; chip dài không đẩy nút xuống dòng | PowerSearch 1 ô (DEC-033) | @szitphan | `design/design.md` § Toolbar | hiệu lực |
| DEC-035 | 2026-10-12 | Bỏ nhãn "50 bản ghi trên 1 trang" ở phân trang | Ô chọn "50 / trang" đã nói đúng thông tin; tổng sau lọc đã có ở thanh công cụ | Giữ nhãn theo SC-04 | @szitphan | `design/design.md` § Pagination | hiệu lực |
| DEC-036 | 2026-10-12 | Nút Tuỳ chỉnh cột = Button Ghost icon + chữ, ở hàng 1 sau Bộ lọc | Tham khảo column picker của Jira | ⚠ chưa ghi | @szitphan | `design/design.md` § Table | hiệu lực |
| DEC-037 | 2026-10-12 | Splash web: logo khách giữa, innvie ở chân | ⚠ chưa ghi lý do | ⚠ chưa ghi | @szitphan | `design/design.md` § Splash web | hiệu lực |
| DEC-038 | 2026-10-12 | Breakpoint dùng nguyên `DEFAULT_WIDTH_BREAKPOINTS` của Astryx | Không tự đặt mốc riêng, dùng mốc sẵn của thư viện | Mốc riêng của dự án | @szitphan | `design/design.md` § Breakpoints | hiệu lực |
| DEC-039 | 2026-10-12 | Màn 768–1279: menu tự thu gọn 64px (cột icon), bấm thì bung 240 đè lên nội dung | ⚠ chưa ghi lý do | ⚠ chưa ghi | @szitphan | `design/_lab/refs/notes.md` | hiệu lực |
| DEC-040 | 2026-10-12 | Dòng lịch sử CMP-08 theo kiểu lab: icon tròn theo hành động + đường nối dọc | ⚠ chưa ghi lý do | `Activity Log / Entry` gốc | @szitphan | BL-075 · `design/design.md` | hiệu lực |
| DEC-041 | 2026-10-12 | Thương hiệu theo khách chỉ thay ô logo (`P-logo`, `P-mau-logo`); bộ màu và component giữ trung tính | SaaS (DEC-003): một design system cho mọi khách | Đổi màu nhấn theo khách | @szitphan | `design/design.md` § Thương hiệu theo khách · `docs/_product/saas-core-vs-tenant.md` 3.8 | hiệu lực |
| DEC-042 | 2026-10-13 | Giữ màu nhấn than chì `#262626`, chưa đổi sang màu khách | Màu Delta #1B7B46 gần trùng chữ chip "Đã duyệt" (#1B7542, chênh sáng 1.08) → xanh lá lẫn nghĩa "đã duyệt"; chàm/xanh dương trùng chip Đang thực hiện/Đã giao; than chì 15.1:1, không đụng chip | Navy, xanh đá, chàm, xanh dương, màu Delta, màu Innvie (7 ứng viên) | @szitphan | `design/_lab/refs/notes.md` § Màu nhấn · BL-080 | hiệu lực (giữ DEC-041) |
| DEC-043 | 2026-10-13 | Màu ô logo Delta (`P-mau-logo`) = #1B7B46 | ⚠ chưa ghi lý do | Mặc định #262626 | @szitphan | `docs/_product/tenant-parameters.md` | hiệu lực |

## 3. Cách làm việc

| Mã | Ngày | Quyết định | Lý do | Phương án đã bỏ | Ai chốt | Nguồn / ghi ở | Trạng thái |
|---|---|---|---|---|---|---|---|
| DEC-044 | 2026-10-02 | SOP Delta là thiết kế to-be của khách; gắn nhãn ý tưởng [SOP to-be] / [SOP+] / [Mới], chỉ [SOP+] và [Mới] tính là USP | Ý đã có trong SOP là yêu cầu của khách, không được nhận là ý của đội | Coi SOP là as-is | @szitphan | memory · nhãn trong brainstorm Mục 4 | hiệu lực |
| DEC-045 | 2026-10-06 | `/brainstorm` phỏng vấn Deep, hỏi từng phần, mỗi câu có "Theo SOP" + "Đề xuất" để user tự quyết | Xây hiểu biết nghiệp vụ cùng lúc phỏng vấn; user muốn tự xác nhận hoặc lật từng điểm | Targeted / Shallow khi tài liệu đã có | @szitphan | `_workspace/interviews/dispatch-coordination-interview.md` | hiệu lực |
| DEC-046 | 2026-10-09 | Gọi API tạo ảnh trả phí phải trình kế hoạch + chi phí, `--dry-run` trước, chạy 1 lô cuối | Chạy sửa nhiều lần tốn tiền, dự án đã chạm trần chi Google | Chạy thử từng ảnh | @szitphan | memory · `design/_lab/refs/vehicle-shot-spec.md` | hiệu lực |
| DEC-047 | 2026-10-11 | Thiết kế UI đi từ khung chung (vùng trang, tab, hành động, tỉ lệ khối) trước, chi tiết từng màn sau | Cần xương sống để các màn sau xoay quanh; nghiệp vụ chưa rõ thì chưa vẽ chi tiết | Vẽ từng màn theo ca | @szitphan | memory · `design/_lab/lab-web-layout.html` | hiệu lực |
| DEC-048 | 2026-10-12 | Duyệt L2 bằng bảng Trước → Sau tiếng Việt, không unified diff | User xem unified diff "chả hiểu gì" | Unified diff (`approval-gate.md` mặc định) | @szitphan | memory | hiệu lực |
| DEC-049 | 2026-10-12 | Finding của reviewer đụng phần nhìn đã duyệt → hỏi trước, không tự sửa | Chuẩn chung không tự thắng bản đã chốt; user muốn tự quyết ngoại lệ (12/10 phải trả về bản trước) | Tự áp finding | @szitphan | memory | hiệu lực |
| DEC-050 | 2026-10-13 | Việc chung trên `main`; phần dispatch sau checkpoint ở `draft/dispatch-downstream`, chuyển qua `merge --squash`, không push draft | Main giữ phần đã xong và chia sẻ; merge thường từng làm sai và phải revert | Merge draft → main | @szitphan | memory | hiệu lực |
| DEC-051 | 2026-10-13 | Ghi quyết định vào sổ này kèm lý do và phương án đã bỏ | Quyết định đang rải ~46 chỗ "(chốt dd/mm)", nhiều chỗ không có lý do, không tra ngược được | Ghi rải trong từng doc | @szitphan | `.claude/rules/decision-log.md` | hiệu lực |
| DEC-052 | 2026-10-13 | Sửa trên Figma thì đồng bộ ngược về tài liệu bằng skill riêng `/figma-sync`; mọi skill đụng Figma (`/figma-screen`, `/figma-userflow`, `/figma-component`) tự gọi ở cuối | Figma không báo cho repo khi có người sửa, nên bảng 5 cột và userflow lệch dần; `/figma-screen` đã dài và giữ ranh giới chỉ ghi link | Thêm chế độ `--sync` vào `/figma-screen` | @szitphan | `.claude/rules/screen-source.md` Mục 5 | hiệu lực |
| DEC-053 | 2026-10-13 | Flow đã lên Figma: bảng 5 cột chuyển sang `screens/{flow}.md`, bỏ file HTML/ASCII wireframe của flow đó; SRS nhúng ảnh Figma + bảng (Phụ lục B, máy sinh) | Hình đã là Figma, giữ HTML song song thành 2 nguồn; .md sửa được từng row và nhúng được vào SRS | Giữ HTML làm nơi chứa bảng | @szitphan | `.claude/rules/screen-source.md` Mục 2, 8 | hiệu lực |
| DEC-054 | 2026-10-13 | "Done" một flow Figma = user trả lời done khi `/figma-sync` hỏi, hoặc đổi task backlog "Chốt giao diện Figma" sang ✅ (dashboard đổi được trạng thái: BL-089) | User muốn chốt từ backlog/dashboard, không bắt buộc qua chat | Gắn với `status: approved` của wireframe index qua `/status` | @szitphan | `.claude/rules/screen-source.md` Mục 6 | hiệu lực |
| DEC-069 | 2026-10-13 | Điều phối agent: việc độc lập chạy song song, mỗi việc có reviewer riêng, chọn model theo việc (Haiku kiểm checklist; Sonnet nghiên cứu, dựng, review; Opus chiến lược và logo cuối; không dùng Fable) | Founder: "làm song song, có reviewer và chọn model phù hợp cho từng task nhé tránh lãng phí" | Một model cho mọi việc | @szitphan | memory agent-orchestration | hiệu lực |
| DEC-070 | 2026-10-13 | Reviewer bộ thương hiệu chỉ dùng agent Claude, không lấy ý kiến Codex/Gemini | ⚠ chưa ghi lý do | Codex/Gemini ở 2 mốc lớn · mọi mốc | @szitphan | `design/brand/brand-brief.md` Mục 9 | hiệu lực |
| DEC-071 | 2026-10-13 | Người duyệt bộ thương hiệu: chỉ founder | ⚠ chưa ghi lý do | Founder + ban lãnh đạo · hỏi thêm Delta | @szitphan | `design/brand/brand-brief.md` Mục 9 | hiệu lực |

## 4. Thương hiệu

| Mã | Ngày | Quyết định | Lý do | Phương án đã bỏ | Ai chốt | Nguồn / ghi ở | Trạng thái |
|---|---|---|---|---|---|---|---|
| DEC-055 | 2026-10-13 | Invlogis là thương hiệu chính cho mọi truyền thông; innvie chỉ là pháp nhân, xuất hiện như chữ ký nhỏ ("by innvie"); hai logo chung một hệ, Invlogis đứng trước | Công ty chỉ còn bán Invlogis (DEC-003), truyền thông dồn cho sản phẩm; tên Invlogis = innvie + logistics nên chung hệ | innvie là thương hiệu mẹ ngang hàng · tách hệ · chỉ Invlogis lộ diện | @szitphan | `design/brand/brand-brief.md` Mục 2 | hiệu lực |
| DEC-056 | 2026-10-13 | Giữ tên innvie và Invlogis | Không mất công đổi tên, đăng ký lại, báo khách (phương án đề xuất founder chọn) | Đặt tên mới cho sản phẩm · đặt lại cả hai | @szitphan | `design/brand/brand-brief.md` Mục 2 | hiệu lực |
| DEC-057 | 2026-10-13 | Làm lại toàn bộ logo và nhận diện; chỉ giữ họ màu xanh dương, bỏ ký hiệu ô vuông pixel và kiểu chữ cũ | Logo cũ trông như công ty outsource, chung chung khó nhớ, không hợp khách logistics; đánh dấu bước chuyển sang bán sản phẩm; founder muốn nhận diện theo tầm nhìn của mình | Giữ logo, mở rộng hệ · làm mới nhẹ | @szitphan | `design/brand/brand-brief.md` Mục 7 | hiệu lực |
| DEC-058 | 2026-10-13 | Thị trường thương hiệu: Việt Nam trước, khu vực sau; tên, logo, khẩu hiệu phải ổn bằng tiếng Anh, tài liệu song ngữ | Tầm nhìn dài hạn: Invlogis thành chuẩn ngành logistics khu vực | Chỉ Việt Nam như PRD · quốc tế ngay từ đầu | @szitphan | `design/brand/brand-brief.md` Mục 1 | hiệu lực |
| DEC-059 | 2026-10-13 | Câu chuyện chào bán chính: AI đọc chứng từ Việt Nam; AI là điểm mạnh, nói kết quả trước; không hứa màn lãi lỗ theo lô | Màn lãi lỗ theo lô chưa có feature (PRD OQ-3); nói kết quả trước an toàn hơn với lãnh đạo ngại rủi ro | Thấy lãi lỗ từng lô · làm riêng cho cảng Việt · một dữ liệu giá thành thật · AI là trung tâm | @szitphan | `design/brand/brand-brief.md` Mục 5 | hiệu lực |
| DEC-060 | 2026-10-13 | Tài liệu chào bán không nêu tên Delta; ghi "một doanh nghiệp vận tải container khoảng 110.000 lô/năm" tới khi Delta đồng ý | Chưa kiểm Delta có cho dùng tên, dữ liệu không (BL-056) | Nêu tên Delta · không nhắc khách nào | @szitphan | `design/brand/brand-brief.md` Mục 5 · BL-108 | hiệu lực |
| DEC-061 | 2026-10-13 | Tính cách thương hiệu: chuyên gia điềm tĩnh + kỹ sư tiên phong; khách gặp lần đầu thấy ấn tượng, hào hứng | Khớp giá trị Minh bạch, Đáng tin cậy, Đổi mới và tầm nhìn AI agent | Người đồng hành trong nghề · người chỉ huy quyết đoán | @szitphan | `design/brand/brand-brief.md` Mục 6 | hiệu lực |
| DEC-062 | 2026-10-13 | Xưng hô "chúng tôi – bạn" cho web, mạng xã hội, deck; hợp đồng, báo giá dùng giọng trang trọng | ⚠ chưa ghi lý do | Chúng tôi – Anh/Chị · Invlogis – Quý khách | @szitphan | `design/brand/brand-brief.md` Mục 6 | hiệu lực |
| DEC-063 | 2026-10-14 | Gu nhận diện theo Instagram ElevenLabs: gradient lụa, chữ mảnh thoáng, chi tiết giao diện tinh tế; học gu, không sao chép | Founder thấy style này "nhìn hiện tại lại có gu" | Ảnh người kiểu điện ảnh | @szitphan | `design/brand/brand-brief.md` Mục 7 | hiệu lực |
| DEC-064 | 2026-10-14 | Màu: xanh dương chủ đạo cho logo, tài liệu; banner, ảnh chiến dịch dùng gradient rực nhiều sắc | Giữ họ xanh (DEC-057) mà vẫn có gu gradient rực | Gradient chỉ trong họ xanh · thử cả hai ở mốc đầu | @szitphan | `design/brand/brand-brief.md` Mục 7 | hiệu lực |
| DEC-065 | 2026-10-14 | Ảnh chính: gradient trừu tượng + chứng từ, và sản phẩm trên thiết bị; tránh sáo rỗng ngành, xanh công nghệ đại trà, ảnh stock, phong cách cứng nhắc | Kể đúng câu chuyện AI đọc chứng từ; dựng bằng code được nên rẻ | Ảnh người trong nghề kiểu điện ảnh | @szitphan | `design/brand/brand-brief.md` Mục 7 | hiệu lực |
| DEC-066 | 2026-10-13 | Nhận diện mới chỉ vào điểm chạm sản phẩm (logo, đăng nhập, splash, icon app, email); màu nhấn giao diện giữ than chì | Giữ DEC-041, DEC-042: màu thương hiệu dễ trùng nghĩa chip trạng thái; không phải làm lại Figma | Đổi màu nhấn giao diện theo thương hiệu · quyết sau khi có nhận diện | @szitphan | `design/brand/brand-brief.md` Mục 9 | hiệu lực |
| DEC-067 | 2026-10-13 | Ảnh AI trả phí cho bộ thương hiệu chỉ dùng cho mockup, minh hoạ, 1 lô sau khi duyệt giá; logo vẽ vector bằng code | Theo DEC-046; logo vector không tốn phí | Không dùng ảnh AI · dùng cả cho ý tưởng logo | @szitphan | `design/brand/brand-brief.md` Mục 9 | hiệu lực |
| DEC-068 | 2026-10-13 | Phạm vi bàn giao: nền tảng, bộ chào bán + ra mắt, bộ nội bộ, điểm chạm sản phẩm; định dạng file nguồn + trang xem, Figma, PDF + PPTX; hạn khoảng 13/11/2026 | Phục vụ chào bán Invlogis, chuẩn hoá nội bộ, ra mắt sản phẩm (founder chọn đủ cả) | Bớt món · hạn 2 tuần · không gấp | @szitphan | `design/brand/brand-brief.md` Mục 10 | hiệu lực |
| DEC-072 | 2026-10-14 | Mốc 1 thương hiệu: chọn hướng A · Lụa, làm lại chữ "v" trong logo; khẩu hiệu chính "Khai mở cách vận hành mới." / "Open a new way to operate."; câu chuyện tên innvie giữ cả hai nghĩa tiếng Na Uy: cống hiến (dedicate) và khánh thành; logo viết chữ thường, trong câu viết "Invlogis", "innvie" | Founder chọn sau khi xem trang so sánh 3 hướng; chữ v của bản A "xấu quá" | Hướng C làm nền theo khuyến nghị reviewer (34/45) · hướng B · khẩu hiệu "Chứng từ vào. Hồ sơ sẵn." | @szitphan | `design/brand/_drafts/m1/index.html` · `design/brand/_drafts/review/r2-identity-review.md` | hiệu lực |
| DEC-073 | 2026-10-14 | Mốc 2 thương hiệu: chữ v trong logo dùng phương án 1 · Gradient nhẹ (nền sáng mực chàm → cobalt, nền tối trắng → periwinkle `#A3B0FF`, bản đơn sắc v một màu) | ⚠ chưa ghi lý do | Phương án 3 · Nguyên bản (agent + reviewer đề xuất, 4,5/5) · phương án 2 · Nếp gấp | @szitphan | `design/brand/_drafts/logo-final/v-options.md` · `logo-spec.md` | hiệu lực |
| DEC-074 | 2026-10-14 | Duyệt Mốc 2 thương hiệu: icon app phương án B · Lụa vắt ra ngoài; duyệt bộ logo, bộ màu chữ + trang quy chuẩn, nền gradient lụa + hoạ tiết chứng từ; bàn giao bản chính ở `design/brand/invlogis/` + `design/brand/guideline/`, nền dạng JPG q90 | ⚠ chưa ghi lý do | Icon A · Giấy · icon C · Nền lụa | @szitphan | trang duyệt https://claude.ai/artifact/HzYd3A9hqXm4jXX14WJa45 · `design/brand/invlogis/README.md` | hiệu lực |

## Sổ quyết định khác (không chép lại)

| Loại | Ở đâu | Ghi gì |
|---|---|---|
| Quyết định của khách (trả lời OQ) | `docs/meetings/*.md` mục "Quyết định" | Mã OQ, phương án, quyết định của khách, ghi chú — vd họp 10/10: 15 quyết định |
| Quyết định nghiệp vụ khi phỏng vấn | `_workspace/interviews/{feature}-interview.md` | "user chốt nhóm A/B/D/E" theo ngày, kể cả lần đổi ý |
| Điểm đổi so với SRS v2.0 (LG) | `docs/_product/srs-v2-change-log.md` | CHG-xx, trạng thái ✅/🟡/⏳, nguồn |
| Thay đổi sau baseline đã duyệt | `docs/cr/CR-{id}.md` (chưa có CR nào) | Lý do, ảnh hưởng 6 chiều, Decision log |
| Lịch sử sửa file | `_workspace/changelog.md` | Ai sửa file nào ngày nào — không ghi lý do |
