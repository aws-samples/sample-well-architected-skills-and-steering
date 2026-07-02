# EUCPERF07 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# EUCPERF07-BP01 Conduct realistic end-to-end testing aligned with organizational objectives

When planning to conduct testing, consider how your users interact with the EUC service
and on an everyday basis. Create tests that align with the primary use of the service
initially and expand to edge cases over time or in response to incidents to verify that they
do not arise in future iterations of the service.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Conduct tests that align with the expected use of the service. Work backwards from
organizational objectives to conduct realistic tests. For example, consider any use case
where remote users process invoices in an accounting application. Key metrics may include
the number of invoices that each user processes per hour and their accuracy. A realistic
test would include experienced application users processing actual invoices, using
representative client devices under typical network conditions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf07-bp01.html*

---
