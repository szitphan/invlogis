---
type: brainstorm
feature: cross-process-flow
status: draft
updated: 2026-10-12
links:
  - docs-input/srs-cu/lg-srs-export.md
  - docs-input/srs-cu/srs-mobile/srs-mobile.md
  - docs-input/ui-common/web/web-common-rules.md
  - docs-input/ui-common/app/app-common-rules.md
  - design/ui-common/screen-patterns.md
  - design/ui-common/conventions.md
  - design/_lab/lab-progress.html
  - design/_lab/refs/notes.md
  - docs/_shared/project-profile.md
---

# Liên quy trình — xem toàn bộ quy trình nghiệp vụ dạng cây

## 1. Idea Seed

Liên quy trình (CMP-09) — tính năng dùng chung: từ 1 bản ghi nghiệp vụ xem được cả quy trình liên nghiệp vụ dạng cây (bước chính, nhánh phát sinh, ngã rẽ chưa chốt, liên module, công nợ), web popup + mobile sheet. Đi lại từ đầu để cover đủ case. Bổ sung: 1 màn danh sách để quản lý các quy trình lớn và trạng thái của chúng.

## 2. Context

Từ màn chi tiết của bất kỳ bản ghi nào thuộc một liên quy trình, người dùng thấy dòng quy trình đầu màn, mở ra sơ đồ cây toàn bộ các bước và nhánh phát sinh, chọn một bước để xem trạng thái + lịch sử rồi mở màn hình chi tiết của bước đó. Cùng tính năng này hiện nút tạo nghiệp vụ tiếp theo khi bản ghi đạt điều kiện, và một màn danh sách để theo dõi mọi quy trình đang chạy.

**Vấn đề đang giải:**
- Thanh tiến trình tuyến tính của SRS cũ (UC00.00.02 web, UC00.01.02 mobile) không vẽ được nhánh lồng nhau (Bồi thường TH3 sinh từ Nhập kho dư TH2) và nhiều phiếu cùng loại (2 phiếu Xuất kho của 1 lệnh sửa chữa).
- SRS cũ phải đặt ngoại lệ "nhánh phát sinh xếp liền sau Xuất kho" vì Lệnh sửa chữa và Xuất kho xảy ra đồng thời.
- Mã CMP-09 đang bị dùng cho 4 nghĩa khác nhau (quy trình nhiều nghiệp vụ, vòng đời 1 bản ghi, form nhiều bước, checklist).

**Vì sao làm lúc này:** chuẩn hoá trước khi viết SRS mới cho Xưởng và Điều phối, để mọi nghiệp vụ khai báo liên quy trình cùng một kiểu.

**Phạm vi luồng:** áp dụng nhiều module. Đã có bảng phát sinh: Xưởng (9 luồng), Cây dầu (Nhập dầu), Liên module (4 luồng) theo UC00.00.02. Điều vận (Cung cấp dịch vụ tổng quát → Điều phối → Lệnh vận tải → Thanh toán chi/thu) là liên quy trình nhưng chưa chốt với khách — bổ sung bảng khi chốt.

**Cách viết tài liệu (phương án C — 2 lớp):**
- Lớp nghiệp vụ: feature dùng chung `cross-process-flow` chứa use case chung + business rule (lưu nguồn, phát sinh, trạng thái, quyền xem, mã QT).
- Lớp hiển thị: CMP-09 "Liên quy trình" giữ quy tắc vẽ R1–R17 của lab.
- Mỗi nghiệp vụ khai 1 **bảng liên quy trình** (bước · tạo từ · trigger · trường hợp phát sinh · điều kiện · cho xoá?) — chính là cột "Trường hợp phát sinh" của SRS cũ, viết lại cho người dùng đọc.
- Tham chiếu ngành: SAP "Document flow" (cây chứng từ trước/sau, mỗi nút có loại, số, người tạo, ngày, trạng thái, mở được chứng từ) và SAP Fiori Process Flow (luồng chứng từ rẽ nhánh, bước dự kiến vẽ nét đứt).

**Tách nghĩa CMP-09 (đã chốt 11/10):** quy trình nhiều nghiệp vụ → CMP-09 Liên quy trình · vòng đời 1 bản ghi → nhãn trạng thái + Lịch sử (CMP-08) · form nhiều bước → CMP mới "Form theo bước" · danh sách việc phải làm → CMP mới "Checklist".

## 3. User Types (preliminary)

Tất cả là **Nhân viên nội bộ Delta** (theo Actor Registry), phân theo vai nghiệp vụ; làm được gì theo phân quyền. Admin cấp quyền menu Quy trình theo module; Hệ thống tự tạo quy trình, sinh mã, tính trạng thái.

| User Type | Pain Point | Primary Need |
|---|---|---|
| Kế toán thanh toán | Không biết các bước trước (xuất kho, chốt lệnh) đã xong chưa khi đối soát | Thấy ngay các bước trước và trạng thái trước khi thanh toán |
| Quản lý xưởng | Một lệnh sửa chữa sinh nhiều phiếu, khó biết phiếu nào đang kẹt | Thấy mọi phiếu sinh từ lệnh và bước đang chờ |
| Thủ kho | Khó tìm phiếu nhập kho dư / bồi thường sinh từ lệnh nào | Tra từ một mã ra cả quy trình |
| Người duyệt (các cấp) | Duyệt mà không rõ yêu cầu sinh từ đâu, vì sao | Xem ngữ cảnh: bước trước, lý do phát sinh |
| Lái xe | Không biết xe mình đang sửa tới đâu | Xem tiến độ trên Delta Super App |
| Điều phối | (Luồng Điều vận chưa chốt) theo dõi Lệnh vận tải tới thanh toán | Xem tiến độ liên nghiệp vụ |

Nhân viên đối tác cây dầu **không** dùng liên quy trình.

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---|---|---|---|---|
| Kế toán thanh toán | Kiểm các bước trước đã xong trước khi thanh toán | Cuối tháng | Cao | Sai thì thanh toán sai/thiếu |
| Quản lý xưởng | Xem lệnh sửa chữa đã sinh phiếu gì, bước nào đang kẹt | Hằng ngày | Cao | Chậm thì xe nằm xưởng lâu |
| Thủ kho | Tìm nhánh nhập kho dư / bồi thường của một lệnh | Khi có vấn đề | Trung | Lệch tồn kho |
| Người duyệt | Xem ngữ cảnh trước khi duyệt | Thỉnh thoảng | Trung | Duyệt sai |
| Lái xe | Xem tiến độ sửa xe của mình | Thường xuyên | Thấp | Ít ảnh hưởng nghiệp vụ |
| Điều phối | Theo dõi luồng Điều vận | Thường xuyên | Cao | Luồng chưa chốt |

## 4. Capabilities Breakdown

### P0 — must have
- **Dòng quy trình trên màn chi tiết** (web: đầu màn · mobile: thẻ quy trình): tên luồng, thanh tiến độ, "Xong x/y bước · n nhánh phát sinh", "Bước trước: …" hoặc "Phát sinh từ: …".
- **Sơ đồ cây** (web popup · mobile sheet) theo quy tắc vẽ R1–R17: bước chính, nhánh phát sinh (nhãn góc thẻ), ngã rẽ chưa chốt, bước liên module, bước công nợ, nhiều bước trước nối vào 1 bước, zoom/kéo/vừa khung.
- **Panel chi tiết bước**: đầu panel (tên, mã, trạng thái, nhãn Đang ở đây / Phát sinh / module), Lịch sử hoạt động (5 dòng mới nhất), nút "Mở màn hình chi tiết" ghim đáy panel.
- **Quyền xem theo bước**: thấy mọi bước của cây; bước không có quyền thì ẩn lịch sử + nút.
- **Nút tạo nghiệp vụ tiếp theo** (UC00.00.03) ở vùng hành động đầu trang, đọc cùng bảng liên quy trình.
- **Đối tượng Quy trình**: mã `QT-[Mã chi nhánh]-[XXXX]`, trạng thái tự tính (Đang triển khai · Đã dừng · Đã hoàn thành).
- **Màn danh sách Quy trình** (web, menu "Quy trình" mỗi module): cột, bộ lọc, tìm theo mã bất kỳ bản ghi trong cây, bấm dòng mở sơ đồ.
- **Bảng liên quy trình** mỗi nghiệp vụ khai báo: bước · tạo từ · trigger · trường hợp phát sinh · điều kiện · 1 hay nhiều bản ghi · cho thu hồi/xoá khi đã có bước con? · cho xoá? — câu chữ viết cho người dùng đọc.

**Hạng mục triển khai (không phải tính năng):** dựng quy trình cho **toàn bộ** dữ liệu cũ (cả quy trình đã hoàn thành, để kế toán đối soát) từ chứng từ nguồn đã ghi trên mỗi phiếu.

### P1 — should have
- **Báo dữ liệu đã cũ**: banner "Quy trình vừa có cập nhật." + [Tải lại] trên popup/sheet/danh sách (đề xuất thành quy tắc chung GR-27).

### P2 — nice to have
- Bảng phát sinh luồng Điều vận (khi chốt với khách).
- Lịch sử hoạt động trình bày theo lab (câu theo hành động riêng của nghiệp vụ) thay bộ câu hiện hành.

## 5. Core Flows (Happy Path)

### 5.1 F1 — Xem dòng quy trình

1. Người dùng mở màn chi tiết một bản ghi.
2. Hệ thống kiểm bản ghi có thuộc một quy trình không (D1). Không thuộc → không hiện gì.
3. Thuộc → web hiện dòng quy trình đầu màn, mobile hiện thẻ quy trình: tên luồng · thanh tiến độ theo trạng thái · "Xong 5/8 bước · 3 nhánh phát sinh" · "Bước trước: Chẩn đoán BG-0140" (bước chính) hoặc "Phát sinh từ: Sửa chữa LSC-0930" (nhánh phát sinh).

### 5.2 F2 + F3 — Mở sơ đồ, xem một bước, mở màn hình chi tiết

1. Người dùng bấm dòng quy trình (hoặc một dòng ở màn danh sách).
2. Hệ thống mở sơ đồ: web popup, mobile sheet. Mở từ màn chi tiết: mặc định chọn bước "Ở đây". Mở từ danh sách: không chọn bước nào (panel đóng). Phóng vừa khung.
3. Người dùng zoom, kéo, chọn một bước.
4. Hệ thống hiện panel theo D2–D5.
5. Người dùng bấm "Mở màn hình chi tiết" → web: mở cùng tab, đóng popup (Back trình duyệt về màn cũ, popup không mở lại) · mobile: đẩy sang màn chi tiết mới (Back về màn trước, sheet đã đóng).

```
 Màn danh sách Quy trình (web)          Màn chi tiết bản ghi (web / mobile)
 ┌──────────────────────────┐           ┌──────────────────────────────┐
 │ Lọc · tìm theo mã bất kỳ │           │ D1: thuộc quy trình?          │
 └────────────┬─────────────┘           └───────┬──────────────┬───────┘
              │ bấm dòng                    Có  │              │ Không
              │                                 ▼              ▼
              │                     ┌──────────────────┐   (không hiện)
              │                     │ Dòng quy trình    │
              │                     │ "Xong x/y · n nhánh" │
              │                     └────────┬─────────┘
              │                              │ bấm
              ▼                              ▼
     ┌─────────────────────────────────────────────────┐
     │ Sơ đồ (web popup / mobile sheet)                 │
     │ từ chi tiết: chọn sẵn bước "Ở đây"               │
     │ từ danh sách: chưa chọn bước nào                 │
     └───────────────────────┬─────────────────────────┘
                             │ chọn 1 bước
                             ▼
          ┌──────────── D5: ngã rẽ? ────────────┐
          │ Có                                   │ Không
          ▼                                      ▼
   Liệt kê hướng có thể đi           ┌── D2: có bản ghi? ──┐
                                     │ Không               │ Có
                                     ▼                     ▼
                           "Chưa có hoạt động"   ┌─ D3: có quyền xem? ─┐
                                                 │ Không               │ Có
                                                 ▼                     ▼
                                      "Bạn không có quyền   Lịch sử hoạt động
                                       xem thông tin này…"  ┌─ D4: công nợ? ─┐
                                                            │ Có             │ Không
                                                            ▼                ▼
                                                   Mở bảng công nợ   Mở màn hình chi tiết
                                                   (lọc theo NCC)    (web: cùng tab, đóng popup
                                                                      mobile: đẩy màn mới)
```

### 5.3 F4 — Tạo nghiệp vụ tiếp theo

1. Bản ghi đạt hành động trigger (vd Phê duyệt báo giá, Chốt lệnh sửa chữa) và người xem có quyền tạo (D6).
2. Hệ thống hiện nút ở vùng hành động đầu trang (vd "Tạo phiếu xuất kho"), không đặt trên sơ đồ.
3. Người dùng bấm → form tạo mới đã điền sẵn thông tin mang từ bản ghi trước (theo bảng UC00.00.03).
4. Lưu nháp → chưa hiện trên cây (nháp riêng tư).
5. Gửi thành công → vào màn chi tiết bản ghi mới; cây có thêm bước mới gắn "Ở đây", nối từ bản ghi trước; trạng thái quy trình tính lại.

### 5.4 F5 — Bước công nợ trả sau

1. Luồng trả sau: mỗi cây có bước Thanh toán **của riêng nó**, trỏ tới bảng công nợ (nhóm đơn) của nhà cung cấp, ghi "Công nợ {Tên NCC}".
2. Cây chỉ hiển thị trạng thái bảng công nợ và link. Quy tắc bảng công nợ hoàn thành khi nào, có nhận thêm đơn sau khi trả đủ không — thuộc SRS Thanh toán (theo SRS cũ: chốt lần đầu → Đang triển khai; thanh toán toàn bộ → Đã hoàn thành).
3. Kế toán chọn bước → panel có nút "Mở bảng công nợ" (lọc theo NCC, khoảng thời gian bảng công nợ).

### 5.5 F6 — Màn danh sách Quy trình (web)

1. Người dùng vào menu {Module} › Quy trình (theo phân quyền). Luồng liên module hiện ở cả 2 module.
2. Hệ thống hiện danh sách, mặc định sắp theo cập nhật mới nhất.
3. Người dùng lọc (luồng, trạng thái, chi nhánh, khoảng ngày cập nhật lần cuối) hoặc gõ ≥3 ký tự của mã bất kỳ bản ghi trong cây.
4. Bấm một dòng → mở popup sơ đồ ngay trên danh sách (dùng lại F2/F3), chưa chọn bước nào.

| Cột | Nội dung |
|---|---|
| Mã quy trình | `QT-[Mã chi nhánh]-[XXXX]` |
| Luồng | vd "Sửa chữa xe khách hàng" |
| Bản ghi gốc | tên bước + mã |
| Phương tiện / khách hàng | theo luồng; bấm mở màn chi tiết phương tiện / xe của khách hàng |
| Tiến độ | thanh màu + "Xong 5/8 bước" |
| Nhánh phát sinh | số nhánh |
| Bước đang chờ | tên bước + trạng thái + chờ bao lâu |
| Trạng thái | Đang triển khai · Đã dừng · Đã hoàn thành |
| Chi nhánh | |
| Cập nhật lần cuối | |

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| D1 | F1 | Bản ghi đang mở thuộc một quy trình? | Hiện dòng quy trình | Không hiện gì (luồng độc lập chưa phát sinh) |
| D2 | F3 | Bước được chọn đã có bản ghi? | Panel có lịch sử + nút | "Chưa có hoạt động. Bước này chưa được tạo." |
| D3 | F3 | Người xem có quyền xem bản ghi của bước? | Như D2 YES | Ẩn lịch sử + nút, hiện câu E-common-011 tại chỗ. Override GR-26: hiện trong panel thay vì popup chặn — lý do: chỉ 1 bước không xem được, không chặn cả màn |
| D4 | F3, F5 | Bước là công nợ trả sau? | Nút "Mở bảng công nợ" | Nút "Mở màn hình chi tiết" |
| D5 | F3 | Bước là ngã rẽ chưa chốt? | Panel liệt kê các hướng có thể đi | Đi tiếp D2 |
| D6 | F4 | Bản ghi đạt trigger theo bảng liên quy trình **và** người xem có quyền tạo? | Hiện nút tạo bước tiếp theo | Không hiện |
| D7 | F6 | Ô tìm có ≥3 ký tự? | Tìm (khớp một phần mã, không phân biệt hoa thường) | Chưa tìm, không báo lỗi |

### 6.2 Scenario Matrix — ai thấy gì

| Người xem | Bước trong cây | Thấy trên sơ đồ | Panel |
|---|---|---|---|
| Nhân viên nội bộ có quyền xem bước | Bất kỳ | Tên, mã, trạng thái | Đủ: lịch sử + "Mở màn hình chi tiết" |
| Nhân viên nội bộ không có quyền xem bước | Bất kỳ | Tên, mã, trạng thái | Đầu panel + trạng thái + E-common-011 |
| Lái xe | Đơn mua HHDV · Lệnh sửa chữa · Báo cáo sự cố | Tên, mã, trạng thái | Đủ |
| Lái xe | Bước khác | Tên, mã, trạng thái | Như "không có quyền" |
| Nhân viên đối tác cây dầu | — | Không có dòng quy trình | — |

### 6.3 State Transitions

**Bước** (theo UC00.00.02):

```
Bước: Chưa triển khai → Đang triển khai → Đã hoàn thành
                              ↕
                     Đã thu hồi/từ chối → (xoá) → Chưa triển khai
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|---|---|---|---|---|
| Bước | Chưa triển khai | Đang triển khai | Gửi thành công (nháp không tính) | — |
| Bước | Đang triển khai | Đã hoàn thành | Phê duyệt nếu là hành động cuối, hoặc hoàn tất theo UC riêng | Không |
| Bước | Đang triển khai | Đã thu hồi/từ chối | Thu hồi hoặc từ chối | Có |
| Bước | Đã thu hồi/từ chối | Đang triển khai | Sửa rồi gửi lại, giữ nguyên mã | — |
| Bước | Đã thu hồi/từ chối | Chưa triển khai | Xoá bản ghi (chỉ nghiệp vụ cho xoá), mã về N/A; nhánh phát sinh vẫn hiện "Chưa tạo" nét đứt | — |
| Bước công nợ | Chưa triển khai | Đang triển khai | Chốt công nợ lần đầu | — |
| Bước công nợ | Đang triển khai | Đã hoàn thành | Thanh toán toàn bộ bảng công nợ | Không |

**Quy trình** (tự tính, không ai sửa tay):

```
(tạo) → Đang triển khai ⇄ Đã dừng
              ↓
        Đã hoàn thành (kết thúc)
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|---|---|---|---|---|
| Quy trình | (chưa có) | Đang triển khai | Bản ghi gốc gửi thành công; luồng độc lập: nhánh phát sinh đầu tiên gửi thành công. Sinh mã QT ngay lúc này | — |
| Quy trình | Đang triển khai | Đã dừng | Một **bước chính** bị từ chối/thu hồi chưa gửi lại | Có |
| Quy trình | Đã dừng | Đang triển khai | Bước chính đó được gửi lại | — |
| Quy trình | Đang triển khai | Đã hoàn thành | Mọi bước chính và nhánh phát sinh đã xong | Không — chưa luồng nào phát sinh nhánh sau khi xong |

Nhánh phát sinh bị từ chối **không** làm quy trình Đã dừng; cột "Bước đang chờ" hiện nhánh đó kèm trạng thái.

### 6.4 Interrupted Transactions

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Đang mở popup/sheet/danh sách thì một bước đổi trạng thái | Dữ liệu trên màn đã cũ | Banner "Quy trình vừa có cập nhật." + [Tải lại]; tải lại giữ bước đang chọn nếu còn | — |
| Mất mạng / lỗi khi tải sơ đồ | Khung popup | Toast E-common-009 / E-common-008 + nút "Thử lại" trong popup | — |
| 2 người cùng gửi bản ghi cho 1 bước **"1 bản ghi"** | Người đầu chiếm bước (bước Đang triển khai, bản ghi chờ phê duyệt) | Người sau bị chặn E-cross-process-flow-001; bản nháp giữ lại để gửi sau. Bước "nhiều bản ghi" (Xuất kho) không chặn — thành bước anh em | Không tự xoá nháp |
| Nút tạo tiếp theo đã hiện nhưng bước tiếp đã có người tạo | Nút còn trên màn | Bấm vẫn mở form (nháp riêng tư); gửi thì bị chặn E-cross-process-flow-001. Tải lại màn thì nút ẩn theo điều kiện UC00.00.03 (vd nút Xuất kho chỉ hiện khi các phiếu trước đã phê duyệt) | — |
| Bấm "Mở màn hình chi tiết" mà bản ghi vừa bị thu quyền | Popup đang mở | Popup chặn E-common-011 như quy tắc chung | — |
| Tải dòng quy trình đầu màn chi tiết lỗi | Màn chi tiết vẫn hiện bình thường | Dòng quy trình hiện "Không tải được quy trình." + [Thử lại] | — |

### 6.5 Other Edge Cases

- **Mỗi bản ghi chỉ thuộc 1 cây** — không có ngoại lệ. Bước Thanh toán trả sau là bước riêng của mỗi cây, chỉ trỏ tới bảng công nợ.
- **Nhiều phiếu cùng loại cùng nguồn** (2 phiếu Xuất kho) là các bước anh em, phân biệt bằng mã, không ghi "lần 1/lần 2".
- **Thanh toán không chờ Bồi thường / Nhập kho dư** — không vẽ đường nối từ 2 nhánh đó sang Thanh toán.
- **Cây quá 20 bước**: vẫn vẽ, mặc định vừa khung, zoom/kéo để xem.
- **Nhãn điều kiện dài**: khe cột nới theo nhãn (R17); câu viết lại mục tiêu ≤40 ký tự.
- **Bước thuộc module người xem không có quyền**: vẫn thấy bước, panel theo D3.
- **Bản ghi chuyển chi nhánh**: mã QT giữ theo chi nhánh lúc tạo.
- **Dữ liệu cũ**: dựng lại từ liên kết nguồn đã ghi trên mỗi phiếu; chỉ quy trình chưa hoàn thành.
- **Bước xoá được hay không** tuỳ nghiệp vụ (vd Bồi thường không cho xoá) — khai ở bảng liên quy trình.
- **Bản ghi đã sinh bước con** (vd Lệnh sửa chữa đã có Xuất kho): người tạo không thu hồi/xoá được — chặn bằng E-cross-process-flow-002. Nghiệp vụ muốn khác thì khai ở bảng liên quy trình.
- **Quy trình kẹt**: nhánh phát sinh "Chưa tạo" vẫn tính là chưa xong; không có đóng thủ công. Quy trình nằm ở danh sách với Bước đang chờ = nhánh đó tới khi được tạo lại.
- **Lái xe** mở được chứng từ theo phân quyền; hiện giới hạn bởi 3 màn chi tiết có trên app (Đơn mua HHDV, Lệnh sửa chữa, Báo cáo sự cố) — app thêm màn thì tự mở rộng.

## 7. Validation, Limits & Wording

### 7.1 Validation rules

| Field | Rule |
|---|---|
| Ô tìm theo mã (danh sách) | Từ 3 ký tự mới tìm; khớp một phần mã; không phân biệt hoa thường; ngừng gõ 0,3 giây thì chạy |
| Bộ lọc danh sách | Luồng · Trạng thái · Chi nhánh · Khoảng ngày theo Cập nhật lần cuối (theo quy tắc bộ lọc chung) |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| Số bước mỗi cây (mức thiết kế) | 20 | — | Vẫn vẽ; vừa khung + zoom/kéo |
| Zoom sơ đồ | 40–250% | — | Dừng ở giới hạn |
| Panel chi tiết (web) | rộng 300px, nổi bên phải | — | Nội dung dài thì cuộn, nút ghim đáy |
| Lịch sử hoạt động trong panel | 5 dòng mới nhất | — | Link "Xem tất cả" mở màn chi tiết |
| Nhãn điều kiện trên đường | 1 dòng, mục tiêu ≤40 ký tự | — | Không cắt chữ; khe cột nới (R17) |
| Khe giữa 2 cột | nhãn dài nhất + 16px mỗi bên, tối thiểu 64px | — | — |
| Khe giữa 2 hàng | 32px | — | — |
| Tìm theo mã | ≥3 ký tự, trễ 0,3 giây | — | Dưới 3 ký tự: chưa tìm |

**Quy tắc câu chữ cho người dùng đọc** (bảng liên quy trình mỗi nghiệp vụ): viết bằng lời nghiệp vụ, không ký hiệu so sánh, không mã TH trên giao diện; "sửa chữa" viết đầy đủ, HHDV được viết tắt; số liệu lấy giá trị lúc phát sinh.

| Chỗ | SRS cũ | Trên giao diện |
|---|---|---|
| Điều kiện TH1 | Lệnh SC có SL hỏng > 0 | "Có 1 phụ tùng hỏng khi sửa" |
| Điều kiện TH2 | Lệnh SC có SL thừa > 0 | "Còn dư 5 phụ tùng sau khi sửa" |
| Điều kiện TH3 | Nhập kho có SL nhập < SL chốt nhập | "Nhập kho thiếu 2 so với số cần nhập" |
| Trigger | Ấn button Xuất kho | "Tạo từ lệnh sửa chữa LSC-0930" |
| Trigger | Chốt lệnh SC | "Phát sinh khi chốt lệnh sửa chữa" |
| Ngã rẽ | N/A, tooltip "Chưa xác định." | "Chưa xác định nơi sửa" |
| Điều kiện thanh toán | Khách DK05, PTTT = trả trước | "Khách hàng DK05 trả trước" |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| Gửi bản ghi cho một bước đã có yêu cầu khác đang chờ phê duyệt (Popup, GR-15 Loại 2) | "Bước [Tên bước] đã có yêu cầu khác đang chờ phê duyệt. Chờ yêu cầu đó được xử lý rồi gửi lại." | E-cross-process-flow-001 |
| Thu hồi/xoá bản ghi đã sinh bước con (Popup, GR-15 Loại 2) | "Không thể thu hồi vì đã có [Tên bước] tạo từ bản ghi này." (xoá: "Không thể xoá vì…") | E-cross-process-flow-002 |
| Lỗi tải sơ đồ / danh sách | (câu chung) | E-common-008 |
| Mất mạng khi mở sơ đồ | (câu chung) | E-common-009 |
| Bước không có quyền xem (hiện tại chỗ trong panel) | (câu chung) | E-common-011 |

#### Success messages

| Tình huống | Wording |
|---|---|
| Tạo nghiệp vụ tiếp theo thành công | Theo toast của nghiệp vụ được tạo (không có câu riêng) |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| Dòng quy trình — tóm tắt | "Xong 5/8 bước · 3 nhánh phát sinh" |
| Dòng quy trình — bước chính | "Bước trước: Chẩn đoán BG-0140" |
| Dòng quy trình — nhánh phát sinh | "Phát sinh từ: Sửa chữa LSC-0930" |
| Panel — bước chưa tạo | "Chưa có hoạt động. Bước này chưa được tạo." |
| Panel — ngã rẽ | "Chưa xác định nơi sửa. Chốt khi phê duyệt báo giá." |
| Panel — công nợ | "Công nợ Gara Minh Phát" + nút "Mở bảng công nợ" |
| Panel — nút chính | "Mở màn hình chi tiết" |
| Danh sách rỗng | "Chưa có quy trình nào. Quy trình tự tạo khi có bản ghi đầu tiên được gửi." |
| Tìm không ra | "Không tìm thấy quy trình chứa mã "BT-0031"." + nút "Xoá bộ lọc" |
| Đang tải sơ đồ | "Đang tải sơ đồ…" |
| Dòng quy trình tải lỗi | "Không tải được quy trình." + [Thử lại] |
| Dữ liệu đã cũ (sơ đồ) | "Quy trình vừa có cập nhật." + [Tải lại] |
| Dữ liệu đã cũ (danh sách) | "Danh sách vừa có cập nhật." + [Tải lại] |

## 8. Assumptions

- Lịch sử hoạt động trong panel tạm lấy lịch sử của bản ghi (bộ câu hiện hành của CMP-08); sau này cập nhật tài liệu theo cách trình bày của lab.
- Mỗi phiếu trên hệ thống LG đã ghi chứng từ nguồn của nó — đủ để dựng lại toàn bộ quy trình cho dữ liệu cũ.
- R4 (mỗi phiếu là 1 bước), R9 (nhãn module), R11 (luồng độc lập), R12 (dòng tóm tắt) do BA xác nhận, không chờ Delta.
- Điều kiện phát sinh lưu giá trị lúc xảy ra; sửa bản ghi nguồn sau đó không đổi nhãn trên cây.
- Liên quy trình không tự gửi thông báo; thông báo đi theo từng nghiệp vụ (CMP-02).
- Hiện không có lệnh sửa chữa nào sinh từ 5 phiếu xuất kho trở lên.

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|---|---|---|---|
| Luồng Điều vận chưa chốt với khách | Thường | Mô hình phải sửa khi chốt, trễ SRS Điều phối | Giữ mô hình chung: thêm luồng là thêm bảng liên quy trình, không đổi cách vẽ |
| Một nghiệp vụ quên khai bảng liên quy trình | Thỉnh thoảng | Cây thiếu nhánh, người dùng tin nhầm "đã xong" | Mỗi SRS nghiệp vụ bắt buộc có bảng; khi rà thiếu sót đối chiếu bảng SRS cũ |
| Dựng lại dữ liệu cũ sai | Hiếm | Kế toán đối soát sai cuối tháng, mất niềm tin vào tính năng | Đối chiếu mẫu theo từng luồng trước khi lên |

## 10. Success Criteria (preliminary)

- 100% luồng trong bảng phát sinh SRS cũ (Xưởng, Cây dầu, Liên module) có bảng liên quy trình viết theo quy tắc câu chữ mới.
- Từ một mã bất kỳ, người dùng tìm ra quy trình chứa nó trong ≤2 thao tác (gõ mã → bấm dòng).
- Quản lý xưởng thấy bước đang kẹt của một lệnh sửa chữa mà không phải mở từng phiếu.
- Tỉ lệ bản ghi tạo qua nút "tạo nghiệp vụ tiếp theo" so với tạo tay (đo sau khi lên).
- Số lần quản lý xưởng phải mở từng phiếu để tìm bước kẹt (đo trước và sau).
- Chỉ số chính thức chốt ở URD/BRD.

## 11. Open Questions

- [ ] OQ-1: Bảng phát sinh luồng Điều vận (Cung cấp dịch vụ tổng quát → Điều phối → Lệnh vận tải → Thanh toán chi/thu) — chờ chốt với khách, không chặn feature. — Nguồn khách: chưa có trong tài liệu khách gửi
- [x] OQ-2: Thanh toán có chờ Bồi thường / Nhập kho dư? — Không.
- [x] OQ-3: Xác nhận R4/R9/R11/R12 — BA tự xác nhận.
- [x] OQ-4: Checklist / Form theo bước có cần mã CMP mới? — Có.
- [x] OQ-5: Mỗi phiếu có ghi chứng từ nguồn để dựng dữ liệu cũ? — Có.
- [x] OQ-6: Bước thanh toán trả sau hoàn thành khi nào? — Theo bảng công nợ (nhóm đơn); quy tắc chi tiết thuộc SRS Thanh toán.

## 12. Next Steps

- `/srs cross-process-flow`
- `/object-map cross-process-flow`
