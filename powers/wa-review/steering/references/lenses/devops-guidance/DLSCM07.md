**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.7] Standardize vulnerability disclosure processes

**Category:** RECOMMENDED

A standard vulnerability disclosure policy helps ensure consistent reporting and
handling of potential vulnerabilities, which in turn enhances the security of the software
development lifecycle. Implementing standardized vulnerability disclosure practices is
recommended for optimizing DevOps, as it promotes security, helps manage risk effectively,
and encourages the responsible reporting and handling of discovered vulnerabilities.

A method for implementation is provided in RFC 9116, *A File Format to Aid
in Security Vulnerability Disclosure* (Foudil, Shafranovich, & Nightwatch
Cybersecurity, 2022). This guidance provides a standardized process for vulnerability
disclosure using a machine readable `security.txt` file, which contains contact
details and the vulnerability disclosure policy. This file is to be placed in
the `/.well-known/` path of  a domain name or IP address to enable security
researchers to find the right information to report vulnerabilities they discover easily.

**Related information:**

- [RFC
9116 - A File Format to Aid in Security Vulnerability
Disclosure](https://www.rfc-editor.org/rfc/rfc9116)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.7-standardize-vulnerability-disclosure-processes.html*
