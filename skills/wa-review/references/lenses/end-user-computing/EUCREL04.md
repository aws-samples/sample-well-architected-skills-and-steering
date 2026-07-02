# EUCREL04 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL04-BP01 Establish data integrity with replication and backup strategies

Implement data replication and backup strategies to safeguard user data and
configurations. Use automated backup solutions such as Amazon WorkSpaces Automated
Snapshots to create regular backups of WorkSpaces volumes. Store data backups securely and
verify that you can promptly restore backups in the event of data loss or
corruption.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

To fortify resilience and safeguard data within Amazon WorkSpaces environments, adopt a comprehensive approach to
data replication and backup strategies. Use automated
solutions to regularly capture backups of user data. Store
backups are stored securely, and check that you can readily
access them for prompt restoration in the event of data loss
or corruption.

Additionally, establish a backup retention policy to determine
how long backups are retained, and verify your compliance with
regulatory requirements. Regularly test the effectiveness of
your backup and restoration processes and identify any
potential areas for improvement proactively. By implementing
robust data protection practices, you can strengthen the
resilience of your WorkSpaces infrastructure and protect
valuable user data and configurations, supporting operational
continuity and reducing the risk of data loss.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel04-bp01.html*

---
