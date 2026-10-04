---
type: brainstorm
feature: {{feature}}
status: draft
updated: {{date}}
links: {{links}}
---

# {{title}}‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## 1. Idea Seed‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

{{seed}}

## 2. Context‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

{{context}}

## 3. User Types (preliminary)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| User Type | Pain Point | Primary Need |
|-----------|-----------|--------------|
| {{user_type}} | {{pain}} | {{need}} |

### 3.1 Tác vụ chính

| Vai trò | Tác vụ | Tần suất | Mức quan trọng | Ghi chú |
|---------|--------|----------|----------------|---------|
| {{user_type}} | {{task}} | {{mỗi ca / mỗi ngày / mỗi tuần / hiếm}} | {{cao / trung / thấp}} | {{hậu quả khi làm sai/chậm}} |

## 4. Capabilities Breakdown‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

### P0 — must have
{{p0_capabilities}}

### P1 — should have
{{p1_capabilities}}

### P2 — nice to have
{{p2_capabilities}}

## 5. Core Flows (Happy Path)

### 5.1 {{flow_1_name}}

1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

```
{{ascii_flow_1}}
```

### 5.2 {{flow_2_name}}

1. ...

```
{{ascii_flow_2}}
```

## 6. System Behavior Deep Dive

### 6.1 Decision Points

| ID | Flow | Khi nào | YES (nhánh đồng ý) | NO (nhánh từ chối) |
|---|---|---|---|---|
| D1 | {{flow_name}} | {{condition}} | {{yes_action}} | {{no_action}} |

### 6.2 Scenario Matrix (nếu `has_multi_role` / ≥2 input states)

| From State | To State | Rule | Action | Result |
|------------|----------|------|--------|--------|
| {{scenario_row}} | | | | |

### 6.3 State Transitions (nếu `has_state_machine`)

```
{{entity}}: {{state_a}} → {{state_b}} → {{state_c}}
                      ↘ {{state_d}} (alternative)
```

| Entity | Từ | Sang | Trigger | Quay lại được? |
|--------|------|----|---------|-------------|
| {{entity}} | {{from}} | {{to}} | {{trigger}} | có/không |

### 6.4 Interrupted Transactions (nếu `has_external_redirect` / `has_async_flow`)

| Tình huống | Hệ thống còn lại gì | Resume | Cleanup |
|---|---|---|---|
| Browser/app đóng giữa flow | {{state}} | {{resume}} | {{cleanup}} |
| External service fail/timeout | {{state}} | {{resume}} | {{cleanup}} |
| Link/token hết hạn | {{state}} | {{resume}} | {{cleanup}} |
| 2 device cùng action | {{state}} | {{resume}} | {{cleanup}} |
| Flow mới khi flow cũ còn pending | {{state}} | {{resume}} | {{cleanup}} |

### 6.5 Other Edge Cases

{{edge_cases}}

## 7. Validation, Limits & Wording‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

### 7.1 Validation rules

| Field | Rule |
|---|---|
| {{field}} | {{validation_rule}} |

### 7.2 Limits & Quotas (exact values)

| Tham số | Giá trị | Window | Behavior khi vượt |
|---|---|---|---|
| {{limit_name}} | {{value}} | {{window}} | {{action}} |

### 7.3 Wording samples (exact strings)

#### Error messages

| Tình huống | Wording | Code |
|---|---|---|
| {{error_case}} | "{{exact_string}}" | E-? |

#### Success messages

| Tình huống | Wording |
|---|---|
| {{success_case}} | "{{exact_string}}" |

#### Info / neutral messages

| Tình huống | Wording |
|---|---|
| {{info_case}} | "{{exact_string}}" |

## 8. Assumptions

{{assumptions}}

## 9. Risks

| Rủi ro | Khả năng | Hậu quả nghiệp vụ | Cách phòng |
|--------|----------|-------------------|-----------|
| {{risk}} | thường / thỉnh thoảng / hiếm | {{impact_business}} | {{mitigation}} |

## 10. Success Criteria (preliminary)

{{success_criteria}}

## 11. Open Questions

- [ ] OQ-1: {{open_question_1}}
- [ ] OQ-2: {{open_question_2}}
- [ ] OQ-3: {{open_question_3}}

## 12. Next Steps

Sau brainstorm này (sau khi BA approve):
- `/urd {{feature}}` — capture user perspective
- `/brd {{feature}}` — business case
- `/prd {{feature}}` — product scope‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
