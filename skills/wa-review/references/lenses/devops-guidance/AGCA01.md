**Saga**: Automated governance
**Capability**: AG.CA — Continuous auditing

---

# [AG.CA.1] Establish comprehensive audit trails

**Category:** FOUNDATIONAL

Comprehensive audit trails involve capturing, recording, and
storing every action taken across your environment. This
provides a log of evidence that can offer insights for
security and audit teams, aiding in identifying suspicious
activities, evidencing non-compliance, and uncovering the root
cause of issues.

Effective DevOps processes are able to streamline both
software delivery and the audit process. Automated governance,
quality assurance, development lifecycle, and observability
capabilities provide a significant amount of data about the
processes that are being followed by your organization, and
the absence of data indicates those that are not. This data
can form a comprehensive audit trail, as steps such as
committing code and doing peer reviews can be traced back to
specific actors, actions, and timestamps.

Use tools for logging and tracking events should be enforced,
along with access controls to maintain the integrity and
confidentiality of audit data. Centralize evidence from these
tools in a secure, accessible location for easy retrieval
during audits. Consider using tools capable of automatically
pulling data from resource APIs to collect and organize
evidence rather than waiting for data to be pushed to it. It's
important that this data remains secure and accessible only to
auditors. There must be controls in place to prevent deletion,
overwriting, or tampering with the evidence in any way.
Regular audits of your audit systems and processes should also
be undertaken to ensure their effectiveness.

Recognize that while developers aren't auditors, they play a
significant role in the compliance process. Provide training
and resources to ensure that everyone on the team understands
the concept of compliance as it relates to each systems
specific industry.

**Related information:**

- [What
Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Automate
Cloud Audits - AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [Cloud
Audit Academy](https://aws.amazon.com/compliance/auditor-learning-path/)
- [Compliance
and Auditing with AWS](https://aws.amazon.com/cloudops/compliance-and-auditing/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc)
- [Verifiable
Controls Evidence Store](https://aws.amazon.com/solutions/implementations/verifiable-controls-evidence-store/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.ca.1-establish-comprehensive-audit-trails.html*
