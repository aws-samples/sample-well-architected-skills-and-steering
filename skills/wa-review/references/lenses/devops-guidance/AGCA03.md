**Saga**: Automated governance
**Capability**: AG.CA — Continuous auditing

---

# [AG.CA.3] Implement systematic exception tracking and review processes

**Category:** FOUNDATIONAL

DevOps environments are dynamic, characterized by rapid changes and updates. During
this rapid development cycle, temporary exceptions might need to be made, for instance,
granting greater permissions to a user for a specific task, or turning off a governance
control for a system update. While necessary, these exceptions can lead to unexpected issues
if not properly managed, and therefore, need to be tracked and revisited.

Implement a process for tracking exceptions, documenting each exception made and help
ensure these exceptions are revisited over time. This documentation should take place in a
centralized, searchable, and secure location. Critical details such as the reasoning behind
the exception, when it was made, who approved it, the business use case, and the anticipated
duration should be included. Clear roles and responsibilities should be assigned for the
creation, review, and retirement of exceptions to help ensure accountability.

To prevent exceptions from being lingering for vast amounts of time, implement
automated alerts for active exceptions that exceed their expected time frame. These alerts
serve as reminders to revisit and address these exceptions.

A regular review process of all exceptions should also be
scheduled. Depending on the associated risk, these reviews
could be conducted on a weekly, monthly, or quarterly basis.
These reviews will derive the continued necessity of each
exception, which could be investigated to become an approved
feature, and investigate any unexpected behavior that may have
arisen as a result of the exception. Once an exception is no
longer necessary, it should be retired and documentation
should be updated.

**Related information:**

- [Amazon's
approach to high-availability deployment: Dealing with the
real world](https://youtu.be/bCgD2bX1LI4?t=1349)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.ca.3-implement-systematic-exception-tracking-and-review-processes.html*
