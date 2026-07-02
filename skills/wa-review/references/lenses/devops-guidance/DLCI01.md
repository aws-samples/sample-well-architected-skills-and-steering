**Saga**: Development lifecycle
**Capability**: DL.CI — Continuous integration

---

# [DL.CI.1] Integrate code changes regularly and frequently

**Category:** FOUNDATIONAL

Working in small batches, characterized by regular, small changes to a code base,
enhances software delivery performance. It reduces the time to receive feedback on changes,
which is required to enable continuous integration. This way of working is an improvement
over traditional phased development approaches, which often leads to delayed feedback due to
large batches of work. By making smaller, more frequent changes, teams can uncover and fix
bugs earlier in the development lifecycle, simplifying the process of updating, testing, and
releasing software.

Features should be broken down into independent work units
that align with the agile
[INVEST](https://www.agilealliance.org/glossary/invest/)
checklist. Splitting features into small increments of value,
ramping up the frequency of deployment, and practicing Test
Driven Development (TDD) all contribute to ensuring small
batch sizes. Developers should strive to integrate multiple
small, releasable changes to the code base at least once per
day. Techniques like
[dark
launching](https://martinfowler.com/bliki/DarkLaunching.html), [branch
by abstraction](https://trunkbaseddevelopment.com/branch-by-abstraction/), and
[feature
flags](https://aws.amazon.com/systems-manager/features/appconfig/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc#Feature_flags) allow incomplete features to be integrated in a
reversible way without impacting end users.

Working in small batches requires discipline and commitment,
but leads to improvements in speed, security, collaboration,
and code base consistency. In mature teams, developers commit
changes multiple times per day and merge code frequently to
prevent accumulating large changes. These teams yield better
collaboration and success in maintaining an up-to-date,
releasable version of the code base.

**Related information:**

- [What
is continuous integration and continuous
delivery/deployment?](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/what-is-continuous-integration-and-continuous-deliverydeployment.html)
- [What
does INVEST Stand For?](https://www.agilealliance.org/glossary/invest/)
- [Testing
software and systems at Amazon: Continuous Integration and
Deployment](https://youtu.be/o1sc3cK9bMU?t=1313)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.1-integrate-code-changes-regularly-and-frequently.html*
