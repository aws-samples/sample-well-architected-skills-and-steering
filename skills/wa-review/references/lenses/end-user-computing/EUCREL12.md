# EUCREL12 — Failure management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL12-BP01 Develop an EUC-specific incident response plan that improves reliability in your environment

When developing incident response plans for Amazon WorkSpaces
and WorkSpaces Applications, it's important to address their unique
characteristics such as the session-based nature of AppStream
2.0 and the persistent data in WorkSpaces. Plans should include
strategies for handling issues with scaling, session failures,
and network dependencies like VPCs or AWS Direct Connect. Active
Directory integration is crucial for both services, so steps for
troubleshooting authentication failures or AD synchronization
must be detailed. The plan should also account for
Region-specific outages, using cross-Region backups or failover
mechanisms for user data and application availability.

Additionally, document user connectivity issues and regular
backups to provide seamless recovery and data protection. Verify
that the incident response plans are comprehensive, covering
procedures for responding to various types of incidents or
events specific to WorkSpaces and WorkSpaces Applications. Collaborate
with key stakeholders in the process to gather insights into
potential scenarios and verify alignment with organizational
goals. Regularly review and refine these plans to incorporate
lessons learned and evolving requirements, maintaining their
effectiveness and relevance over time.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

When developing incident response plans for Amazon WorkSpaces
and WorkSpaces Applications, customize them to suit the specific
features and challenges posed by these cloud services. Verify
that these plans are thorough, encompassing procedures for
addressing various incidents or situations specific to
WorkSpaces and WorkSpaces Applications.

Collaborate with key stakeholders to gather valuable insights
and align plans with organizational objectives. Document
comprehensive procedures, clearly define roles and
responsibilities, establish effective communication channels,
prioritize incidents based on severity, and set response
timelines.

Regularly review and update these plans to incorporate lessons
learned and evolving requirements, improving their ongoing
effectiveness and relevance. This structured and inclusive
approach fosters readiness to respond swiftly and effectively,
bolstering overall system reliability and resilience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel12-bp01.html*

---
