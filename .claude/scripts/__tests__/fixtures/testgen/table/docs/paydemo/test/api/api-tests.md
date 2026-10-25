# API tests — paydemo

<!-- TC:START -->
| TC | Method | Path | Auth | Body | HTTP | Assert | Kết quả | Lần chạy |
|----|--------|------|------|------|------|--------|---------|----------|
| TC-01 | POST | /auth/login | public | {"email":"a"} | 200 | data.ok=true | — | — |
| TC-02 | GET | /orders | session | — | 200 | — | — | — |
| TC-03 | POST | /orders | session | {"x":1} | | — | — | — |
<!-- TC:END -->

## Lịch sử chạy
