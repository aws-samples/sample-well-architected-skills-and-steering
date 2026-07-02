**Saga**: Development lifecycle
**Capability**: DL.CR — Code review

---

# [DL.CR.2] Perform peer review for code changes

**Category:** FOUNDATIONAL

A peer review process for code changes is a strategy for
ensuring code quality and shared responsibility. To support
separation of duties in a DevOps environment, every change
should be reviewed and approved by at least one other person
before merging. Once approved, a pipeline with sufficient
access will deploy the change.

Most version control systems support protection rules
enforcing certain workflows, like requiring at least one peer
review, before merging into designated branches. Use these
rules to enforce this workflow and provide assurance that all
code changes adhere to this mandatory review process.

Incorporating [pair
programming](https://www.agilealliance.org/glossary/pair-programming/), where two programmers collaboratively work side-by-side or through
screen sharing, is method of peer review. By integrating this approach, reviews can be
integrated into the development lifecycle earlier—while the code is being written, reducing
the time taken to identify and fix issues. This accelerates review timelines, reduces the
introduction of bugs or issues, promotes knowledge sharing, and creates a culture
of quality and continuous improvement.

Some companies require multiple reviewers, or require more
proof than just pair-programming to adhere to compliance
requirements. Pick a code review process that works for your
organization, and enforce it through policies, processes, and
technology.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP04 Manual code
reviews](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_manual_code_reviews.html)
- [Team
Collaboration with Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/team-collaboration-with-amazon-codecatalyst/)
- [Code
review](https://en.wikipedia.org/wiki/Code_review)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.2-perform-peer-review-for-code-changes.html*
