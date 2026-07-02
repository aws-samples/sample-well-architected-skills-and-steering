**Saga**: Development lifecycle
**Capability**: DL.CR — Code review

---

# [DL.CR.8] Designate code owners for expert review

**Category:** OPTIONAL

A code owners process assigns a designated owner, usually the
person or team with the most knowledge or expertise, to each
part of the code base. In a DevOps environment, this helps
ensure that there is an expert reviewer available for specific
or complex parts of the system at all times.

To implement a code owners process, determine who the code owners should be based on
expertise and distribute the ownership equally amongst the team to avoid bottlenecks. You
can use features in version control systems that automatically assign code owners to
review code changes in their area of expertise. One example of this would be to use a
`CODEOWNERS` file stored along with the code in the repository. This file
defines individuals or teams that are responsible for code in a repository.

While this practice is optional and not beneficial for all organizations, it can be
particularly useful for larger teams or those with complex, distributed systems as it
provides an additional layer of control and can prevent potential issues from going
unnoticed if all reviewers are not equally experienced with a specific or complex part of
the code base.

**Related information:**

- [About
code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.8-designate-code-owners-for-expert-review.html*
