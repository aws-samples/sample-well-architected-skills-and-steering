# GAMESEC09 — Automate security

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC09-BP01 Integrate tooling and automation to reduce the mean time of security reviews

To identify security vulnerabilities, organizations can use a variety of different tools
and services like Static Application Security Testing (SAST) and Dynamic Application Security
Testing (DAST). SAST is a way to review the source code and determine security vulnerability.
DAST is a black box way of testing your code which tests your applications without looking at
the source code.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Another tool that organizations can use is Software Composition Analysis (SCA), which
assesses the security of your third-party or open source dependencies. For a more manual
approach, secure code reviews can be implemented throughout the pipeline.

**Customer example**

AnyCompany Games uses SAST tools to automatically flag potential security flaws during
the development process. They also use DAST tools to simulate threats against running game
builds to validate that security controls are working as intended. Additionally, AnyCompany
Games integrates dependency scanning tools into their development process to automatically
identify known vulnerabilities in third-party libraries and game engines.

### Implementation steps

- Use Amazon CodeGuru as a SAST tool.
- Use open-source tools like OWASP Dependency Check, SonarQube, or OWASPZap.

### Resources

- [Security for Developers](https://catalog.us-east-1.prod.workshops.aws/workshops/66275888-6bab-4872-8c6e-ed2fe132a362/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec09-bp01.html*

---
