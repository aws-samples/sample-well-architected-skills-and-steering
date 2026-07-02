**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.1] Use a version control system with appropriate access management

**Category:** FOUNDATIONAL

Version control systems enable tracking and managing of
changes to code over time. They allow multiple developers to
work on a project concurrently, provide a history of changes,
and make it possible to revert to a previous version if
necessary. Version control systems play a role in maintaining
the integrity of software components, as they provide an
auditable trail of all modifications made to the code base,
authorizes users as they access the code base, and help to
ensure that changes to the code base can be reverted or rolled
back.

Implement access management policies on the version control
systems which supports a culture of code sharing and
collaboration amongst teams in your organization. Having a mix
of both open and private repositories allows for a balance
between promoting code reuse and collaboration, and
safeguarding sensitive information. For open repositories,
developers can share code freely to encourage collaboration
and learning, while confidential projects or sensitive parts
of the code base can use private repositories.

Consider implementing role-based access control (RBAC) in your
version control system. Using RBAC, you can restrict write
(commit) access to specific roles or individuals and can
protect the main code base from inadvertent or inappropriate
alterations. This also allows granting broad,
organization-wide read access to open repositories, while
reserving the ability to limit access to sensitive or
confidential private repositories.

**Related information:**

- [What
Is Repo?](https://aws.amazon.com/what-is/repo/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.1-use-a-version-control-system-with-appropriate-access-management.html*
