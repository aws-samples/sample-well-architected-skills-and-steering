**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.4] Grant access only to trusted repositories

**Category:** FOUNDATIONAL

To maintain the security, integrity, and quality of your software, restrict the usage
of untrusted source code and artifact repositories. Untrusted repositories present risks,
including potentially introducing vulnerabilities into your software and leaking sensitive
code or information. As a safer alternative, only use trusted repositories that offer
secure, vetted libraries, and dependencies.

Implement policies that control where developers can publish
code, to prevent accidental exposure or internal threats. This
should apply to both artifact and source code repositories
across the organization. Protect against internal threat
actors or inadvertently sharing code to public or untrusted
git repositories by limiting the allowed repositories that
developers can publish code to. Hosting your own repositories
might be advantageous depending on your needs, enabling
complete control over available code. Methods such as
pre-commit hooks for git repositories can be used to enforce
these rules effectively.

By enforcing usage of trusted repositories, you ensure that
only secure, vetted code components and artifacts are used,
enhancing software lifecycle stability and security. It also
minimizes the risk of sensitive information being leaked into
untrusted repositories.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.4-grant-access-only-to-trusted-repositories.html*
