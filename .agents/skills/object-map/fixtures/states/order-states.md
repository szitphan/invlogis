## State: Đơn hàng

```mermaid
stateDiagram-v2
    state "Chờ xác nhận" as ChoXacNhan
    state "Đã xác nhận" as DaXacNhan
    state "Đã huỷ" as DaHuy
    [*] --> ChoXacNhan
    ChoXacNhan --> DaXacNhan
    ChoXacNhan --> DaHuy
```
