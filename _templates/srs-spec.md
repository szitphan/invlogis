---
type: srs
feature: {{feature}}
status: draft
updated: {{date}}
links: {{links}}
---

# {{feature}} — Software Requirements Specification‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

## 1. Scope‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

{{scope}}

## 2. Actors & Stakeholders‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| Actor | Loại (người/hệ thống/ngoài) | Mục tiêu | Trong scope? |
|-------|-----------------------------|----------|--------------|
| {{actor}} | người/hệ thống/ngoài | {{goal}} | Có/Không |

## 3. Functional Requirements (FR)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| ID | Title | Description | Priority | Tầng | Verify by | Source |
|----|-------|-------------|----------|------|-----------|--------|
| FR-{{feature}}-001 | {{title}} | {{desc}} | P0/P1/P2 | {{layer}} | demo/test/kiểm tra/phân tích | PRD Mục 4 |

## 4. Non-Functional Requirements (NFR)‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍

| ID | Category | Requirement | Priority | Acceptance |
|----|----------|-------------|----------|------------|
| NFR-{{feature}}-001 | performance | {{req}} | P0/P1/P2 | {{accept}} |

## 5. Business Rules

| ID | Rule | Tầng | Trigger | Implements FR | Source |
|----|------|------|---------|---------------|--------|
| BR-{{feature}}-001 | {{rule}} | {{layer}} | {{trigger}} | FR-{{feature}}-NNN | BRD Mục X / PRD Mục X |

## 6. Error Matrix

| Error ID | Title | Trigger | Severity | Related FR | Screen state | Recovery |
|----------|-------|---------|----------|------------|--------------|----------|
| E-{{feature}}-001 | {{title}} | {{trigger}} | critical/major/minor | FR-{{feature}}-NNN | {{screen-state}} | {{recovery}} |

## 7. Success Criteria

| ID | Outcome nghiệp vụ | Đo bằng | Mốc đạt |‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍
|----|-------------------|---------|---------|
| SC-{{feature}}-01 | {{outcome}} | {{measurement}} | {{target}} |

## 8. Data Entities (tóm tắt — chi tiết ở erd.md)

{{entities}}

## 9. Flows (tóm tắt — chi tiết ở flows.md)

{{flows_summary}}

## 10. Screens (tóm tắt — chi tiết ở ascii-wireframe/)

{{screens_summary}}

### Cấu hình UI Common Rules & Components

| Mã (CMP/GR) | Áp ở màn | Phần UC khai báo / Override + lý do |
|---|---|---|
| {{cmp_gr_code}} | {{screens}} | {{declared_or_override}} |

E-common dùng: {{e_common_used}}

## 11. Constraints, Dependencies & Assumptions

**Constraints (ràng buộc áp đặt — có source/owner):**

| Ràng buộc | Source / Owner |
|-----------|----------------|
| {{constraint}} | {{source_owner}} |

**Dependencies (deliverable do bên khác sở hữu):**

| Phụ thuộc | Owner | Blocks nếu chưa sẵn |
|-----------|-------|---------------------|
| {{dependency}} | {{owner}} | {{blocks}} |

**Assumptions (tin là đúng — nêu hệ quả nếu sai):**

| Giả định | Invalidate {X} nếu sai |
|----------|------------------------|
| {{assumption}} | {{invalidated}} |

## 12. Open Questions

* [ ] {{open_question_1}}‍​‌​​​‌‌​‌‌‌​​‌‌​​‌​​‌‌‌​‌‌‌‌​​‌‌​​‌​​​​​‌‌​‌‌​‌‌‌‌‌‌​‌​‌‌​‌​‌‌‌‌‌​‌‌‌​‌​​‌​​​​​‌‌​​​‌​‌​​‌​‌‌​‌​​​‌‌​​‌‌​‌‌​​​‌‌‌‌‌​‌​‌​‌​​​‌‌​‌‍


## Phụ lục A — UI Common Rules & Components áp dụng

<!-- ui-common:begin -->
<!-- ui-common:end -->


<!-- wm:60d5580055f5e6dd44329f2c02b7fe5a -->
<sub>Tài liệu thuộc bộ AI4BA BA-Kit — bản quyền hoangphan.blog</sub>
