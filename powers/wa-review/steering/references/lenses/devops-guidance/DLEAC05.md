**Saga**: Development lifecycle
**Capability**: DL.EAC — Everything as code

---

# [DL.EAC.5] Integrate technical and operational documentation into the development lifecycle

**Category:** RECOMMENDED

Integrating documentation and code involves creating,
maintaining, and publishing documentation using the same tools
and processes used for application development. With this
approach, changes to systems should be immediately reflected
in documentation, reducing the risk of discrepancies between
system behavior and documentation. By making documentation
part of the development lifecycle, it becomes a living
document that evolves with the system over time.

Documentation should be stored in a versioned source code repository and written in a
machine-readable markup language, such as Markdown. The documentation can be made directly
accessible through the repository or through knowledge sharing tools capable of rendering
the markup language, like Git-based wikis, static site generators, or directly in
developers' integrated development environments (IDEs).

Code should include clear, insightful comments and commit
messages should be structured using a machine-readable
specification, such
as [Conventional
Commits](https://www.conventionalcommits.org/en/v1.0.0/). This information can be used as a source to
generate detailed documentation and change logs using tools
specific to the programming language and platforms being used.
Many of these tools can create API references, class diagrams,
or other technical documents from inline comments in your
source code, ensuring the documentation is always in line with
the most recent changes. Automate this process by adding a
stage to the deployment pipeline to generate documentation
with every change to a main, releasable branch.

This approach is not only limited to documenting code, but also can be used to store
operational documentation like incident response procedures, disaster recovery plans,
training material, and onboarding processes. While some aspects of these documents still
likely require manual effort to create, the benefits of incorporating these documents into
the development lifecycle include enforced reviews of changes, ability to write tests to
suggest updating documentation when changes are significant or made to important
components, and versioning the documents for auditability.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL12-BP01 Use
playbooks to investigate failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_playbook_resiliency.html)
- [Write
the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)
- [One
AWS team's move to docs as code](https://www.youtube.com/watch?v=Cxuo3udElcE)
- [AWS Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks)
- [Using
code as documentation to save time and share
context](https://github.com/readme/guides/code-as-documentation)
- [DocFx](https://dotnet.github.io/docfx/)
- [How
to build an automated C# code documentation generator
using AWS DevOps](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-build-an-automated-c-code-documentation-generator-using-aws-devops/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.5-integrate-technical-and-operational-documentation-into-the-development-lifecycle.html*
