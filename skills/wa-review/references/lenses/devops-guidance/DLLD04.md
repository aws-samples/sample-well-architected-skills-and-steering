**Saga**: Development lifecycle
**Capability**: DL.LD — Local development

---

# [DL.LD.4] Enforce security checks before commit

**Category:** FOUNDATIONAL

Pre-commit hooks can be an effective tool for maintaining security best practices.
These hooks can help in the early detection of potential security risks, such as exposed
sensitive data or publishing code to untrusted repositories. At a minimum, use pre-commit
hooks to identify hidden secrets, like passwords and access keys, before code is published
to a shared repository. When discovering secrets, the code push should fail
immediately—effectively preventing a security incident from occurring.

Select security tools compatible with your chosen programming languages and customize
them to uphold your specific governance and compliance requirements. It is best to integrate
these security tools into pre-commit hooks, integrated development environments (IDEs), and
continuous integration pipelines so that changes are continuously checked before code is
committed into a shared repository.

**Related information:**

- [Security
in every stage of CI/CD pipeline: Pre-commit hooks](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#pre-commit-hooks)
- [Security
scans - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security-scans.html)
- [Pre-commit](https://pre-commit.com/)
- [Husky](https://typicode.github.io/husky/)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [GitGuardian](https://docs.gitguardian.com/ggshield-docs/integrations/git-hooks/pre-commit)
- [AWS-IA
opinionated pre-commit hooks](https://github.com/aws-ia/pre-commit-configs)
- [Blog: Extend
your pre-commit hooks with AWS CloudFormation Guard](https://aws.amazon.com/blogs/security/extend-your-pre-commit-hooks-with-aws-cloudformation-guard/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.4-enforce-security-checks-before-commit.html*
