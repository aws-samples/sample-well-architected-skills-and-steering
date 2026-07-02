# EUCOPS07 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS07-BP01 Formalize the mandatory creation and maintenance of all EUC service-related documentation

Maintain a library of documentation related to the business requirements, architectural
design, service delivery, and support of your EUC deployment.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Create deployment and operations guides and keep them updated over time verify that
all processes used to install, administer, update, and maintain the AWS EUC environment
are captured. This documentation provides an effective method of communicating how the
environment should be managed to new administration or support staff and external
partners, when required.

As iterative operational testing takes place, use lessons learned from failover and
DR testing to evolve the deployment and operations guides and capture relevant changes
that were needed in order to successfully complete testing.

While this documentation does not provide an exhaustive list of all aspects of a
deployment that should be captured, gather as much detail of the end to end service
configuration and the subsequent management processes as possible.

For each of the following topics, if a manual installation was performed, capture the
specifics of how and why you configured each setting. If the deployment was automated,
document the methods used (like AWS CloudFormation or Terraform), and call out the specifics of how
and why each configuration decision was made.

**Infrastructure build**

How were the landing zone and your WorkSpaces or WorkSpaces Applications environments created, which
options were configured for each service, and why? CloudFormation templates can be used to
reliably and repeatably build the baseline infrastructure and the rationale behind the
CloudFormation template creation. Deployment and rollback processes can be captured and
documented.

**Active Directory or RADIUS integration**

Your Active Directory and RADIUS deployment and maintenance should be part of a
separate operations guide chapter. For WorkSpaces and WorkSpaces Applications, capture the specifics of
how you integrated Active Directory and RADIUS for the respective service. For WorkSpaces,
document which directory integration method was used, and capture the manual steps used to
deploy or details of the CloudFormation templates used to automate this process.

**SAML 2.0 or certificate-based authentication**

How was your SAML 2.0 IdP configured with respect to integration with Amazon WorkSpaces or
WorkSpaces Applications? Which SAML attributes were used to drive AppStream application
entitlements?

How will you monitor and manage the certificates used to build a chain of trust
between AWS IAM and your SAML provider?

For certificate-based authentication, capture the installation choices taken and the
integration points with Microsoft Certificate Services.

How will you manage certificates and expiry for integration between CBA and Microsoft
Certificate Services?

**Image management**

Document the process followed to create each of your custom images. Which updates and
hotfixes were applied, which applications were installed, how were they configured, and
which registry or file system changes were required?

How were your applications installed and deployed (for example, did you use local
images, App-V, MSIX, AppVolumes, network share, or third party isolation products?).

For WorkSpaces Applications, did you use session scripts? Document the scripts deployed and
what each script does.

For WorkSpaces BYOL deployments, document the process followed to extract your Windows 10
or 11 images, sanitize them, and import into Amazon WorkSpaces.

How should image updates be managed, which version control and naming conventions
will be applied, and how will you roll back to a known good configuration if required?

**Client deployment**

Which clients are required to access Workspaces or WorkSpaces Applications (for example,
Windows, macOS, or web), which user groups require each client type, and how should it be
installed? How will clients be updated?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops07-bp01.html*

---
