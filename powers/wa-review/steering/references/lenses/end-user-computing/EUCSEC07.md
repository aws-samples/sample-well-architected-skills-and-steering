# EUCSEC07 — Detection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC07-BP01 Monitor user access to EUC instances and aggregate logs in central location

Record events generated when users access systems to a central
system to log attempted and successful user authentication, as
well as access to applications. Prior to implementation,
consider that the use of a central system for security events
may be subject to local regulation and legal framework.

Events logged in the central system should include the following
data attributes:

- Timestamps
- User ID
- IP address
- Outcome of access attempt (success or failure)

Additional attributes or metadata may be required for compliance
reasons. Evaluate any applicable regulatory and organizational
security policy requirements to determine the complete set of
attributes to record.

For completeness, consider all possible sources of events,
including:

- Service-emitted events and logs (for example, Amazon WorkSpaces EventBridge events and WorkSpaces Applications usage
reports)
- Data plane logs collected through agents installed onto
Amazon WorkSpaces or WorkSpaces Applications instances

For Windows instances, use events recorded in the Windows
security log alongside a log management system to collect and
aggregate data from various sources, such as other text-based
logs, network devices, and security applications. This
integration provides a deeper insight into potential security
issues so that your organization can address them.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use agents on Amazon WorkSpaces Applications and Amazon WorkSpaces
instances to aggregate security logs. If instance security
logs need to be captured from WorkSpaces Applications instances, then
event forwarding agents such as Amazon CloudWatch, Amazon Kinesis Agent for Windows, or Telegraf can be used to forward
relevant events into the central security logging system.

For WorkSpaces, these agents can be pre-installed into a
WorkSpaces custom bundle to make sure a logging capability is
available before users attempt to access WorkSpaces. For
WorkSpaces Applications, these agents need to be installed into the
Image Builder for On-Demand and Always-On fleets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec07-bp01.html*

---
