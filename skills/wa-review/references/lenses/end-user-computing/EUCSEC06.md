# EUCSEC06 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC06-BP01 Rely on a centralized authentication system that satisfies security requirements for your EUC environment

Evaluate your organization's security policies to determine the
requirements that authentication systems need to provide for end
users accessing EUC services.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Use authentication providers
configured for best practices**: Consider the
following regarding authentication of users accessing AWS
EUC services using Microsoft Active Directory or an
authentication provider:

Use a strong password policy.
- Use multi-factor authentication (MFA) to provide
additional protection to end users in your
environment. For Amazon WorkSpaces and WorkSpaces Applications
environments integrated with a SAML IdP, enable MFA in
the IdP. For Amazon WorkSpaces Personal where a SAML
IdP is not in use, implement a RADIUS server to
provide the MFA capability.
- Consider adding password expiration policy to require
users to change their passwords regularly.
- When using a SAML identity provider (IdP), consider
enabling advanced features like geo-restrictions and
conditional access.
- Using a corporate managed (and HR linked) identity
provider improves security by automatically
propagating role and permission changes to the EUC
environment. It also promotes the best practice of
managing access based on user lifecycle.

- **Users should be authenticated and
authorized to access EUC services**: Use an
authentication system, such as a SAML 2.0 IdP or Microsoft
Active Directory, to authenticate users prior to them
accessing an AWS EUC service. Verifying authenticating or
authorization checks that only entitled users can access
the applications and data accessible from Amazon WorkSpaces and WorkSpaces Applications instances.
- **Manage user entitlements using
groups where possible**: Use groups within Active
Directory or your authentication provider instead of
granting access to individual users. This approach
simplifies the administration process and helps you
perform access reviews and updates more efficiently.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec06-bp01.html*

---
