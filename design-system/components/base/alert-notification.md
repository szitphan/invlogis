---
type: design-component
status: stale
status_prev: draft
updated: 2026-11-02
links:
  - design-system/architecture.md
  - design-system/foundations/README.md
  - design-system/tokens.json
  - design-system/components/_work/alert-notification/page.json
  - design/ui-common/screen-patterns.md
  - _workspace/decisions.md
---

# Alert · Notification

> Base · phiên bản 0.1.0 · Nháp · người phụ trách @szitphan · Figma: Section `Alerts & notifications` (6862:203175) trang DS · Base
> components — `Notification` 6862:202736 · `Alert` 6862:203147 · `_Notification icon` 6862:202535 · khối Mobile 6862:203176 ·
> Demo 6862:204019 · DEC-286, DEC-287 · trang duyệt https://claude.ai/artifact/5wf1mywkCacs675SaLoVFZ

Hai component cùng họ và một phần con: **Notification** (toast, tạm thời, nổi trên màn) và **Alert** (bền, nằm trong
luồng nội dung). Nhóm A (DEC-279): cùng cấu tạo trên web và app, không có trục Platform; cỡ, lề, chữ đọc từ mode
Platform của khung chứa. Vị trí toast là quy định cấp màn (CMP-01). Notification Center (chuông + danh sách, CMP-02)
là component Application riêng, không thuộc md này. Banner sự cố toàn trang: chưa dựng (DEC-286).

## Web

> Khối Web đặt mode Platform = Web; mọi số là giá trị mode Web.

### Tổng quan

- **Notification** — phản hồi sau hành động, tự ẩn (CMP-01). 7 Type:
  - **Success / Info / Warning / Error** — trạng thái kết quả; Error không tự ẩn, có Thử lại.
  - **Icon** — sự kiện về một đối tượng (xe vào cổng, chứng từ đã ký): icon nội dung, tông trung tính.
  - **Avatar** — việc do người khác làm (tài xế nhận lệnh, gửi ảnh).
  - **Progress** — tải lên / xuất / nhập: thanh %, dòng phụ (dung lượng, số dòng, thời gian còn lại), nút Huỷ; không
    tự ẩn khi đang chạy. Xong → đổi sang Success có nút Tải xuống; lỗi → Error có Thử lại.
- **Alert** — thông tin cần ở lại trên màn tới khi xử lý xong: "Danh sách vừa có cập nhật." + Tải lại (GR-27), lỗi khối
  có Thử lại, thiếu chứng từ. 4 Tone, nền nhạt theo tone (DEC-287); đóng được chỉ khi tin chỉ để biết. GR-27 dùng Tone Info.

### Cấu tạo

| Phần | Token | Giá trị (Web) |
|---|---|---|
| Notification · khung | nền `color/bg/primary_alt`, viền `shadow/xl-border`, bóng `shadow/xl`, bo 12 (`radius/xl`), lề `space/lg` | rộng `width/xs` 384, lề 12, khoảng cách 12 |
| `_Notification icon` | vòng `radius/full`, nền `color/status/*-bg` (Neutral: `color/bg/secondary`), icon `color/status/*-icon` (Neutral: `color/fg/tertiary`) | 32, viền ngoài 4 (nền nhạt 45%), icon 20 |
| Avatar (Type Avatar) | `Avatar` Size 32, chấm trạng thái | 32 |
| Tiêu đề | `color/text/primary`, `type/heading` (14/20 nét 600) | xuống dòng, không cắt — viết ngắn |
| Mô tả | `color/text/tertiary`, `type/hint` | 12/18, tối đa 2 dòng |
| Hành động | `Button` Hierarchy Link Gray, Size SM; nút đầu chữ đậm; khoảng giữa 2 nút `space/lg` | 12; vùng bấm ≥ 24 (`touch/min`) |
| Nút đóng | `Close button` Size SM | 28 |
| Thanh giờ (Has Timer) | màu `color/status/*-icon`, cao 4 | chạy theo thời gian tự ẩn: 3 giây, có nút ≥ 10 giây (CMP-01) |
| Thanh tiến độ (Progress) | nền `color/bg/secondary`, phần chạy `color/fg/info/primary`, `radius/full` | cao 6, % 12/18 `color/text/tertiary` |
| Alert · khung | nền `color/status/*-bg`, viền `color/status/*-border-subtle`, bo 10 (`radius/lg`), lề `space/lg` (DEC-287) | khoảng cách 12 |
| Alert · tiêu đề / mô tả | `color/text/primary` `type/heading` · `color/text/primary` `type/caption` | xuống dòng, không cắt |
| Alert · nút | nút đầu `Button` Secondary Size MD; nút thứ hai Link Gray, chữ `color/text/primary` (xám mặc định chỉ đạt 4,1–4,3:1 trên nền nhạt) | 32 (app 44) |

### Biến thể

- `Notification`: Type = Success · Info · Warning · Error · Icon · Avatar · Progress (7).
- `Alert`: Tone = Success · Info · Warning · Error × Actions = None · Inline · Stacked (12). Inline: nút căn phải cùng hàng
  (một nút, chỉ web). Stacked: từ 2 nút trở lên — và mọi alert có nút trên app — nút xuống dưới chữ (thẳng lề chữ).
- `_Notification icon`: Tone = Success · Info · Warning · Error · Neutral (5); phần con, không dùng riêng.

### Trạng thái

Không có trạng thái tương tác riêng — trạng thái nằm ở `Button`, `Close button` lồng bên trong. Vòng đời toast:
hiện → (rê chuột / focus; app: chạm giữ, trình đọc màn hình bật — dừng đếm giờ) → tự ẩn / đóng. Không có nút: 3 giây; có nút hành
động: tối thiểu 10 giây; Error, Progress: không tự ẩn (CMP-01, DEC-287). Tối đa 3 toast chồng, mới nhất ở dưới cùng (gần góc neo).

### Kích thước

Một cỡ. Toast rộng `width/xs` 384 trên web (DEC-324); Alert rộng theo cột nội dung.

### Nên và không nên

- Nên: một câu nói việc đã xảy ra (mẫu "Đã {hành động}", design.md › Copy động › Toast); thêm Hoàn tác khi đảo ngược được.
- Nên: lỗi của trường báo tại trường; lỗi nghiệp vụ server dùng Popup Error (GR-15) — không dùng toast.
- Không: dùng toast cho thông tin người dùng phải đọc lại (dùng Alert); lỗi toast tự ẩn mất nút Thử lại.
- Không: chỉ dùng màu để báo loại tin — luôn có icon và chữ.

### Trợ năng — chấm theo WCAG 2.2

- 1.4.3: tiêu đề 17,7:1, mô tả `text/tertiary` trên nền trắng ≥ 4,5:1 (foundations Mục 3.4).
- 1.4.11: Alert tách nền bằng nền nhạt theo tone + viền nhạt; loại tin báo bằng icon (≥ 3:1) và chữ, không dựa vào viền. Icon trạng
  thái ≥ 3:1 trên nền vòng.
- 2.5.8: nút đóng 28, link hành động có vùng bấm vô hình 24.
- 4.1.3: toast đọc bằng vùng thông báo lịch sự (`role="status"`), Error dùng `role="alert"`; không lấy focus.
- 2.2.1: toast có hành động hiện tối thiểu 10 giây; dừng đếm khi rê chuột / focus, trên app khi chạm giữ hoặc TalkBack/VoiceOver bật;
  Hoàn tác làm lại được ở chỗ khác (DEC-287).
- 4.1.2 nút đóng: tên đọc "Đóng thông báo: {tiêu đề}"; Esc đóng toast / Alert đang có focus; đóng xong focus về phần tử trước đó.
- 1.1.1 / 1.4.1: icon tone đọc kèm nhãn ẩn trước tiêu đề ("Thành công:", "Thông tin:", "Cảnh báo:", "Lỗi:"); icon Type Icon / Avatar là
  trang trí (ẩn với trình đọc màn hình).
- Progress: thanh dùng `role="progressbar"` + `aria-valuenow`, `aria-valuetext` ("64%, còn khoảng 20 giây"); không đọc từng bước %;
  xong báo bằng status, lỗi bằng alert; nút Huỷ có tên "Huỷ tải lên {tên tệp}".
- 2.4.11: toast không được che phần tử đang có focus — khi toast hiện, vùng cuộn thêm lề dưới bằng chiều cao toast.
- Vùng bấm vô hình (24 web / 44 app) không vẽ trên Figma; code đặt bằng lề đệm quanh nút, được tràn ra ngoài chữ nhưng không tràn
  khỏi mép toast.

### Thuộc tính

Notification: `Title`, `Description` (Type Progress: dòng phụ — dung lượng, số dòng, thời gian còn lại), `Has Description`,
`Has Actions`, `Has Action 2`, `Has Timer`, `Percent` (Type Progress). Nhãn nút sửa ở instance lồng `Action` / `Action 2` (đã đưa
ra panel); đổi icon (Type Icon) hoặc chữ viết tắt (Type Avatar) ở instance lồng `Lead`. Nhãn mặc định: Error "Thử lại",
Progress "Huỷ"; nút đầu là hành động chính (chữ `color/text/primary`).
Alert: `Title`, `Description`, `Has Description`, `Has Close`, `Has Action 2`; nhãn nút ở instance lồng `Action` / `Action 2`.

### Thành phần lồng

`Button` (Link Gray SM; Secondary MD), `Close button` SM, `Avatar` 32, `_Notification icon`, icon Lucide.

### Được dùng trong

CMP-01 Toast (mọi feature) · GR-27 banner cập nhật (cross-process-flow: search-process, view-process) · lỗi khối có
Thử lại (cross-process-flow view-process #1).

### Token

Số đo theo mode ở bảng Cấu tạo; màu ở Phần máy.

### Kiểm máy

28/10: layout_audit 0 lỗi (chấm trạng thái avatar tràn khung — cố ý) · kiểm tên DEC-264 0 lỗi · a11y_audit component 0 lỗi; demo:
`text/tertiary` trên `bg/secondary` 4,35:1 (token chung, đã biết), nút đóng 28 (có vùng bấm vô hình). 3 agent review: 28 điểm — 19 sửa
thẳng, 9 user quyết Sửa (DEC-287).

### Chuyển động

Toast vào `duration/medium` + `easing/standard`, trượt 8 + mờ dần; ra `duration/fast` + `easing/exit`, chỉ mờ; thanh giờ linear, không qua đường cong. Luật chung: `foundations/motion.md` (DEC-333).

## Mobile

> Khối Mobile đặt mode Platform = Mobile.

### Tổng quan

Như Web. Toast rộng theo màn trừ lề 16 (361 trên khung 393), đặt **dưới, ngay trên thanh tab** (D8); màn không có
thanh tab: trên vùng nút chân màn.

### Cấu tạo

Như Web; khác: Alert có nút luôn dùng `Actions=Stacked` (Inline bóp chữ còn 3–4 từ một dòng ở 361); vùng bấm của nút đóng và link hành động 44 (`touch/min` Mobile), hai link cách nhau 24 (`space/3xl`); nút Alert
Size MD = 44; chữ theo mode Mobile (`type/caption` 13).

### Biến thể · Trạng thái · Kích thước · Nên và không nên · Thuộc tính · Thành phần lồng · Token

Như Web.

### Trợ năng — chấm theo WCAG 2.2

2.5.8 nâng lên 44 theo DEC-138; còn lại như Web.

### Được dùng trong

CMP-01 › Mobile (app tài xế) · cross-process-flow sheet sơ đồ (banner cập nhật dưới header sheet).

### Kiểm máy

Chưa chạy.

## Đối chiếu Astryx

- Toast Astryx nền đảo (tối), 360px, loại default/error → đổi sang nền trắng + icon màu (D1), có Icon, Avatar, Progress.
- Banner Astryx nền nhạt → Alert nền nhạt theo tone + viền nhạt (DEC-287; trước đó trắng + viền đậm ở DEC-286).
- Vị trí toast web: Astryx/CMP-01 góc trên phải → dưới phải (D4).

## Phần máy (chung Web và Mobile)

<!-- auto:begin -->
<!-- auto:end -->
