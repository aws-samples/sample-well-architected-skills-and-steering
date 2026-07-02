# GAMESEC02 — Ongoing security

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC02-BP01 Use ready to deploy templates for standard security practices

Ready-to-deploy templates provide a proactive and agile way to assess your security posture
in the cloud. Pre-configured templates evaluate your cloud security and implement necessary
changes promptly. The templates encompass a wide range of best practices across various
technologies and widely accepted security frameworks. Using templates can assist game studios to
maintain consistent infrastructure configurations, especially as they may scale and add
additional AWS accounts to support new workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

By using AWS services and implementing ready-to-deploy templates, game developers can
proactively assess and strengthen their cloud security posture, safeguarding their
intellectual property, protecting player data, and fostering a secure gaming landscape through
regular security assessments and continuous monitoring to promptly identify and address
potential vulnerabilities.

**Customer example**

AnyCompany Games faced a significant challenge when preparing to launch their next title
in the European industry. They realized that their existing data handling practices didn't
meet GDPR requirements. They turned to AWS Security Hub CSPM and AWS Config and its ready-to-deploy
templates for a solution. The team implemented the GDPR-specific conformance pack in AWS Config,
which automatically assessed their existing infrastructure against GDPR standards. This
initial scan revealed several critical gaps, such as improper data retention policies and
inadequate access controls on where player data was stored. Using the template's predefined
rules, AnyCompany Games rapidly implemented the necessary changes. Moreover, the ongoing
automated compliance checks provided by the template allowed the small team to maintain GDPR
compliance effortlessly, even as they continued to update and expand the game.

### Implementation steps

- Use templates for standard security practices, such as managed rules and
conformance packs in AWS Config and standards in AWS Security Hub CSPM.
- Review the details of the [Security Hub CSPM standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) to
determine which ones align most with the security needs of your game studio.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec02-bp01.html*

---
