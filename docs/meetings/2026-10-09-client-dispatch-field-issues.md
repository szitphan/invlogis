---
type: meeting
status: processed
updated: 2026-10-09
links:
  - docs/dispatch-coordination/brainstorms/dispatch-coordination.md
  - _workspace/backlog.md
---

# Gặp khách — các vấn đề điều phối vận tải thực tế

> Ngày: 2026-10-09 | Bên khách: chị Trang và đội điều vận Delta | Bản tổng hợp dưới đây đã gửi khách ngày 2026-10-09.

## Bản tổng hợp đã gửi khách

**1. Thay đổi và phát sinh khi xe đang chạy**

- Hiện lái xe báo thay đổi qua kênh bên ngoài, không qua hệ thống, nên hành trình thực tế khác kế hoạch mà hệ thống không ghi nhận được. Hệ thống sẽ cho lái xe báo trực tiếp ngay giữa chặng khi có vấn đề hoặc khi lệch kế hoạch.
- Các thay đổi cần ghi nhận: cung đường, thời gian giao hàng, đi công suất, khách muốn đi cao tốc, sự cố trên đường về, khách báo thiếu hàng, khách huỷ vì hàng chưa sẵn sàng, đổi điểm giao. Mỗi thay đổi kéo theo xử lý phía sau như chi phí, nhiên liệu, chứng từ.
- Khi đổi cung đường, chi phí phát sinh do công ty chịu và lượng dầu cấp được điều chỉnh theo.
- Mong muốn: Mọi thay đổi so với kế hoạch và mọi vấn đề phát sinh đều đến được điều vận và quản lý.

**2. Mooc**

- Trường hợp hiếm phải bỏ mooc giữa đường: điều xe khác ra kéo tiếp.
- Mooc trong lệnh vận tải được phép khác mooc đang móc trên xe. Khi đổi mooc, việc ghép hàng và xe cũng thay đổi theo.

**3. Nhiên liệu**

- Khi triển khai lệnh vận tải, việc cấp dầu gắn với định mức phương tiện. Dầu cấp vượt định mức vẫn đi luồng cấp dầu hiện có.
- Dầu mua ngoài theo hoá đơn lẻ: tính lượng dầu dư để làm căn cứ cấp bù (hiện tại đang không lưu lượng dầu dư cho trường hợp mua ngoài và hoá đơn lẻ)

**4. Dữ liệu và chứng từ**

- Dữ liệu từ Vietmap và VETC đang lệch nhau về toạ độ và chi phí, cần thống nhất nguồn chuẩn -> VETC.
- Mỗi lệnh có hạn chuẩn bị giấy tờ riêng.
- In hoá đơn trả hộ hàng loạt ra PDF.

**5. Hướng phát triển**

- Cơ chế điều phối lệnh có hỗ trợ AI, tương tự ứng dụng gọi xe đẩy chuyến cho tài xế: hệ thống đề xuất xe phù hợp, điều vận chốt.

**6. Câu hỏi**

- "Hàng quay cắt" trong thực tế là tình huống nào? Khi đó xe và hàng được xử lý ra sao?
- Tạm ứng dầu cho xe chạy CBT: đợt trước mình có trao đổi có nói sẽ bỏ phần xử lý bên ngoài. Hệ thống có cần làm luồng tạm ứng dầu cho xe CBT này nữa không?

## Quyết định

| # | Quyết định | Người đề xuất | Ghi vào |
|---|---|---|---|
| 1 | Lái xe báo thay đổi, vấn đề giữa chặng trên app; điều vận và quản lý đều nhận | chị Trang | Brainstorm F1, F2 |
| 2 | Đổi cung đường: chi phí công ty chịu, điều chỉnh lượng dầu cấp | Khách | Brainstorm F3 |
| 3 | Mooc trên Lệnh được khác mooc đang móc trên xe; bỏ mooc giữa đường thì điều xe khác | Khách | Brainstorm F4, F5 |
| 4 | Cấp dầu trên Lệnh gắn định mức phương tiện; vượt định mức đi phiếu dGas 4 | Khách | Brainstorm F6 |
| 5 | Dầu mua ngoài theo hoá đơn lẻ: lưu lượng dư làm căn cứ cấp bù | chị Trang | Brainstorm F6 |
| 6 | Hạn chuẩn bị giấy tờ đặt theo từng Lệnh | Khách | Brainstorm F7 |
| 7 | VETC là nguồn chuẩn toạ độ và chi phí đường bộ | Khách | Brainstorm F8 |
| 8 | Điều phối có AI: phần mềm đề xuất xe, điều vận chốt (P2) | Khách | Brainstorm F9 |

## Việc cần làm

| Việc | Ai | Theo dõi |
|---|---|---|
| Nhận khách trả lời 2 câu hỏi (hàng quay cắt, tạm ứng dầu CBT) | @szitphan | BL-036 · OQ-45, OQ-46 |
| Gắn cấp dầu, định mức, cấp bù vào SRS Lệnh vận tải | @szitphan | BL-037 |
| Ghi VETC là nguồn chuẩn trong SRS | @szitphan | BL-038 |
| In hoá đơn trả hộ hàng loạt ra PDF (feature Thanh toán trả hộ) | @szitphan | BL-039 |
