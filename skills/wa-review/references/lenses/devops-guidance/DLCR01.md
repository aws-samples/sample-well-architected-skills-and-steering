**Saga**: Development lifecycle
**Capability**: DL.CR — Code review

---

# [DL.CR.1] Standardize coding practices

**Category:** FOUNDATIONAL

Coding standards promote uniformity and consistency across the organization.
Individual teams can also extend this standard to adopt specific practices that align with
the team's preferences. Having standards not only helps ensure consistency across
distributed teams, but can also make code reviews more efficient, support knowledge sharing,
and lead to faster issue resolution.

Identify or develop coding standards that align with the primary programming
languages used across the organization. This does not mean that other languages cannot be
used, but does lead to a structured approach to development for new teams and new employees.
The coding standards are meant to facilitate error detection, improve code readability,
simplify maintenance, and enhance the overall efficiency of builders, not prevent
innovation.

These standards can be codified into linters and code quality tools to improve
developer experience. This approach provides fast feedback to developers and evaluate their
adherence to the standards automatically. Hold training sessions for developers on these
standards, store them in centralized knowledge sharing spaces, and create mechanisms to
gather feedback to continuously improve the standard over time. We recommend getting started
by adopting industry-specific standards, such as the [Secure Coding
Guidelines for Java SE](https://www.oracle.com/java/technologies/javase/seccodeguide.html), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for Git,
or the [PEP8](https://pypi.org/project/pep8/) styling guide for Python.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.1-standardize-coding-practices.html*
