**Saga**: Development lifecycle
**Capability**: DL.CR — Code review

---

# [DL.CR.6] Initiate code reviews using pull requests

**Category:** RECOMMENDED

[Pull
requests](https://docs.aws.amazon.com/codecommit/latest/userguide/pull-requests.html) are a method of integrating changes from one
branch of a repository into another. They can be used to
propose, review, and integrate changes from a feature branch
into the main releasable branch. Modern branching strategies,
including
[GitHub
flow](https://docs.github.com/en/get-started/quickstart/github-flow) and
[trunk-based
development](https://trunkbaseddevelopment.com/continuous-review/), support this workflow to initiate code
review.

A pull request workflow is recommended for organizations and teams which have
enhanced code review requirements. This workflow could include requiring multiple peer
reviewers, or enforcing that reviews must take place before code is integrated into the
main releasable branch. We recommend adopting trunk-based development paired with a pull
request workflow utilizing [short-lived
feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/). This method uses feature branches solely to trigger code
review processes through a pull request workflow. These short-lived feature branches
should not be used as a source for code deployments.

There should be clearly defined steps to standardize creating,
reviewing, and merging pull requests. Store these guidelines
in a shared, easily accessible location to ensure all team
members understand the process. The guidelines should include:

- **Useful descriptions and titles:** The pull request
descriptions should guide the reviewer through the changes, grouping related files and
concepts. A well-crafted title gives a high-level summary of the changes, providing
the reviewer with the necessary context.
- **Descriptive commit messages:** Each commit message
should clearly communicate what changed and why. This can make auto-generated pull
requests more useful, provide a bullet-point summary of the changes, and aid reviewers
who read the commits along with the diff.
- **Inline comments:** Leaving comments on the pull request
can guide the reviewer through the changes. These comments can provide the reviewer
with the necessary context, such as files that were simply re-indented or files where
the main bulk of changes occurred.
- **Visual cues:** For user interface (UI) changes,
consider including screenshots, GIFs, or videos. Visual representations can make it
easier for reviewers to understand the changes.

Pull request workflows are recommended, but not strictly
required for DevOps adoption. Some organizations and smaller
teams may choose to strictly follow trunk-based development
practices and commit
changes [directly
to the main releasable branch](https://trunkbaseddevelopment.com/committing-straight-to-the-trunk/). In this workflow, code
reviews are performed
through [pair
programming]( https://www.agilealliance.org/glossary/pair-programming) or initiated through custom post-commit
processes. Choose the right method for performing code review
based on your organization requirements and individual team
preferences.

**Related information:**

- [Reviewing
a pull request - Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-review.html)
- [Team
Collaboration with Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/team-collaboration-with-amazon-codecatalyst/)
- [Code
review](https://en.wikipedia.org/wiki/Code_review)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.6-initiate-code-reviews-using-pull-requests.html*
