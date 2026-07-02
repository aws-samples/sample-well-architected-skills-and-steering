**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.2] Keep feature branches short-lived

**Category:** FOUNDATIONAL

In version control systems, feature branches provide a structured way to develop new
functions or address defects. These branches are carved out with the intent of eventually
merging changes into the main code base for release. Traditional branching methods, such as
GitFlow, lean towards creating long-lived feature branches which can introduce challenges
including complex merges and divergent code bases. Modern branching strategies, including
[GitHub
flow](https://docs.github.com/en/get-started/quickstart/github-flow) and [trunk-based
development](https://trunkbaseddevelopment.com/), emphasize the significance of keeping feature branches short-lived to
avoid these challenges. We recommend trunk-based development paired with a pull request
workflow utilizing [short-lived feature
branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/) as the most effective branching strategy when practicing DevOps.

The core benefit of short-lived feature branches is the
promotion of continuous integration. By frequently integrating
code changes into the main releasable branch of the
repository, teams discover integration problems early on. This
approach prevents last-minute chaos when merging code bases
leading to software that can be reliably released at any time.
We recommend merging into the main releasable branch at least
once per day.

Smaller teams might prefer committing directly to the trunk of
the releasable branch. Larger teams or those working on
complex software might lean towards a Pull-Request workflow
that uses short-lived branches. Regardless of the branching
strategy you choose to use, the principle remains: branches
should be transient, preferably representing a single
contributor's work. To enforce this, put a process in place to
remove branches that are already merged and prevent long-lived
branches by actively deleting branches that surpass a specific
retention period.

**Related information:**

- [Trunk-based
Development: Short-Lived Feature Branches](https://trunkbaseddevelopment.com/short-lived-feature-branches)
- [GitHub
flow](https://guides.github.com/introduction/flow/)
- [A
successful Git branching model: Note of reflection](https://nvie.com/posts/a-successful-git-branching-model/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.2-keep-feature-branches-short-lived.html*
