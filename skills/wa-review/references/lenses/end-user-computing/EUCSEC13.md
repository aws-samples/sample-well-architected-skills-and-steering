# EUCSEC13 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC13-BP01 Align your compliance of data storage with policies and regulatory requirements

The storage of data accessible by users and applications on end
user systems should align with and comply with the data
residency requirements for the data and the organization.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Data should be stored and accessed in compliance with the
in-scope policies and regulatory requirements. The location of
data and the applications accessing data should align with the
compliance framework and requirements for the respective
organization. To achieve this, consider your AWS Region for
compliance against the data sovereignty requirements for the
application and data. Additionally, consider data permissions
to verify compliance and enforce least privilege access. Keep
latency between end user devices and the data they need to
access in consideration when choosing the location of the EUC
environment but also adhere to data residency requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec13-bp01.html*

---
