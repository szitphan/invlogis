# Sổ đối chiếu: Vehicle Intelligent Service — VIS (SRC-06)

> Nguồn: `sop/vis-du-lieu-van-hanh-xe/vis-du-lieu-van-hanh-xe.md`
> Bản: 08/10/2026 (nhận 2026-10-11)

| Mục | Kết quả | Ở đâu | Ghi chú |
|---|---|---|---|
| I. Đặt vấn đề | ➖ | | giới thiệu tài liệu |
| 2.1 Kiến trúc hệ thống | ➖ | | kiến trúc kỹ thuật (EUP webhook, Map API), việc của SRS/dev |
| 2.2.1 Thời gian xe sẽ đến (ETA) | ⬜ | | chưa rà |
| 2.2.2 Thời gian xe đã đến (Geofencing) | ✅ | `docs/transport-dispatch/brainstorms/transport-dispatch.md` E7, Mục 5.1 bước 6 | |
| 2.2.3 Thời gian xe di chuyển dưới 5 km/h (Traffic jam) | ✅ | `docs/transport-dispatch/brainstorms/transport-dispatch.md` E7 | |
| 2.2.4 Thời gian nổ máy không di chuyển (Idling) | ⬜ | | chưa rà |
| 2.2.5 Dầu diesel tồn và bất thường nhiên liệu | ⬜ | | chưa rà |
| 2.2.6 Giám sát lộ trình, ghi nhận tránh trạm vé | ✅ | `docs/transport-dispatch/brainstorms/transport-dispatch.md` E7, F8 | |
| 2.2.7 Tổng số km xe đã di chuyển | ⬜ | | chưa rà |
| 3.1 Hệ thống quản lý tự động vé cầu đường | ⬜ | | F8 có một phần; master account, trích nợ tự động, bảng kê tránh trạm, đối soát hoá đơn cuối kỳ chưa rà |
| 3.2 Dầu hao phí do tắc đường | ⬜ | | chưa rà |
| 3.3 Dầu hao phí khi chọn container rỗng (Geofence) | ⬜ | | km tìm vỏ, dầu bù — chưa có |
| 3.4 Dầu hao phí do nổ máy ngủ | ⬜ | | chưa có |
| 3.5 Giám sát dầu tồn, báo cáo hút dầu bất thường | ⬜ | | chưa có |
| 3.6 Đối soát lượng dầu thực đổ | ⬜ | | F6 có một phần |
