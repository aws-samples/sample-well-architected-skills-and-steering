# EUCREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL01-BP01 Add redundancy and remove single points of failure in your environment

The principle of assuming that failures will occur represents a
paradigm shift in the approach to designing Amazon WorkSpaces
and WorkSpaces Applications environments. By adopting this mindset,
organizations can prioritize resilience and develop strategies
that minimize the impact of failures, thereby reducing downtime
and mitigating potential business disruptions.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

When designing an Amazon WorkSpaces or WorkSpaces Applications
environment, the approach should prioritize resilience and
minimize the impact of failures by assuming that failures will
occur and implementing robust strategies.

Implement redundancy at every layer of your architecture. This
includes network paths, storage, and virtual desktops. Use
multiple instances of Amazon WorkSpaces or WorkSpaces Applications so
that if one fails, others can take over seamlessly. For
WorkSpaces Applications, use automatic scaling to match the number of
running instances to user demand, keeping performance
consistent even during usage spikes.

Regularly test your failure recovery procedures. Use AWS tools
such as AWS Fault Injection Service to simulate different
failure scenarios and validate your recovery strategies.

Implement robust data backup and disaster recovery plans.
Regularly back up user data and configurations, and verify
that you have a tested recovery plan in place to restore
operations quickly in case of a failure.

Set up comprehensive monitoring using Amazon CloudWatch to
keep track of the performance and health of your WorkSpaces
and WorkSpaces Applications environments. Create alarms and automated
responses to detect and remediate detected issues promptly.

Continuously review and improve your architecture and
operational procedures. Learn from historical incidents and
update your strategies to help prevent future occurrences.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel01-bp01.html*

---
