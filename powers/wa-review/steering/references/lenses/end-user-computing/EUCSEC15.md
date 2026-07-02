# EUCSEC15 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC15-BP01 Encourage users to store data on long-term storage services

Educate users to avoid storing critical data directly on EUC
systems without also saving that data to an approved, long-term
storage solution that is regularly backed up. This practice
verifies that data remains visible, accessible, and protected
against loss in the event of an EUC instance failure or
lifecycle event such as termination or rebuild.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Verify that EUC services are not used for long-term data
storage. EUC services such as Amazon WorkSpaces and Amazon
WorkSpaces Applications are optimized for application delivery and user
productivity, rather than as primary long-term data storage
solutions. Amazon WorkSpaces Applications streaming instances are
non-persistent, meaning data stored locally during a session
is lost when the instance is recycled or terminated. Amazon WorkSpaces provides persistent root and user volumes, which
are well-suited for user profiles, application settings, and
day-to-day productivity tasks. However, for storing critical
or long-term data, organizations should use dedicated storage
services that offer centralized management, data durability,
and backup capabilities.

To reduce the risk of data loss, encourage users to save
important data to approved, persistent storage services that
align with the organization's data protection and recovery
requirements. Recommended options include Amazon FSx for Windows File Server, which integrates with WorkSpaces to
provide durable, backed-up home directories, as well as Amazon S3 or other enterprise-grade cloud storage services. Implement
clear governance policies and user education to verify that
data is consistently stored in systems designed for long-term
retention and resilience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec15-bp01.html*

---
