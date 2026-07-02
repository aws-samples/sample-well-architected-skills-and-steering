# MLSEC01 — Business goal identification

**Pillar**: Security  
**Best Practices**: 1

---

# MLSEC01-BP01 Validate ML data permissions, privacy, software, and license terms

Machine learning implementations require careful consideration of
data permissions, privacy, and software licensing to adhere to
organizational and legal requirements. Validating these elements
throughout the ML lifecycle builds trusted ML systems that respect
data rights while delivering business value.

**Desired outcome:** Establish a
robust governance process that verifies that ML data usage and
software implementations meets your organization's requirements.
Maintain clear documentation of data permissions, approved software
packages, and license adherence. Operate ML implementations within a
framework that respects data subject rights, follows privacy
regulations, and avoids legal complications related to software
licensing.

**Common anti-patterns:**

- Assuming data collected for one purpose can automatically be
used for ML training without additional consent.
- Installing ML libraries and packages without reviewing their
license terms or data collection practices.
- Failing to document data permissions and consent mechanisms for
adherence verification.
- Ignoring the need for a process to handle withdrawn consent from
data subjects.
- Using third-party ML models without understanding their privacy
implications or license restrictions.

**Benefits of establishing this best
practice:**

- Reduces legal and regulatory risks related to data privacy and
software licensing.
- Enhances trust from data subjects and stakeholders through
ethical data handling.
- Avoids unexpected limitations on business plans due to
restrictive license terms.
- Improves documentation for audits and regulatory requirements.
- Streamlines deployment through pre-validated software and
container solutions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

ML libraries and packages handle various aspects of the machine
learning lifecycle, from data processing and model development to
training and hosting. Each component may come with specific
license terms, privacy considerations, and data handling
requirements. Validating these elements verifies your
organization's ML initiatives adhere to regulatory requirements
and don't introduce unexpected limitations.

When implementing ML systems, verify that data being used has
proper permissions for ML applications specifically. This often
means going beyond general data collection consent to verify
explicit permission for ML usage. For example, if you collected
customer data for service delivery, you may need additional
consent to use that data for training ML models.

Understanding license implications is critical for software
components. Some open-source ML libraries may have restrictions
that could affect your ability to commercialize models trained
with them. Similarly, third-party models or APIs might include
terms that grant the provider certain rights to your data or
restrict how you can deploy solutions.

Privacy considerations extend beyond initial data collection to
the entire ML lifecycle. Establish mechanisms to handle data
subject requests, including the right to withdraw consent or be
forgotten. Your ML implementation should respect these requests
without compromising the entire system.

### Implementation steps

- **Attain data permissions for
ML**. Verify whether your intended data can be used
for machine learning specifically. Document the legitimate
business purpose for using the data, and determine whether
you need additional consent from data owners or subjects.
Implement a process to handle data subjects who withdraw
their consent, including the ability to remove their data
from training sets or models when required. Maintain
comprehensive documentation of data permissions for
compliance-aligned purposes and potential audits.
- **Create a software license
inventory**. Develop and maintain an inventory of
ML libraries, packages, and dependencies used in your ML
pipeline. For each component, document the license type, key
terms, restrictions, and implications for your business
model. Use tools like
[AWS License Manager](https://aws.amazon.com/license-manager/) to track and manage software licenses
across your ML environments, improving adherence to
licensing agreements and optimizing license usage.
- **Bootstrap instances with lifecycle
management policies**. Create lifecycle
configurations with references to your approved package
repositories and scripts to install required packages. This
improves consistency across development environments and
avoids the introduction of unauthorized packages. Implement
[Amazon SageMaker AI Lifecycle Configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations.html) to automate the
setup of development environments with pre-approved software
packages and configurations.
- **Evaluate package integrations that
require external lookup services**. Based on your
data privacy requirements, opt out of data collection
features when necessary. Minimize data exposure by
establishing trusted relationships with service providers
and understanding their data handling practices. Evaluate
privacy policies and license terms for ML packages that
might collect telemetry or other data. For sensitive
implementations, consider creating private mirrors of
required packages to maintain control over external
connections.
- **Use prebuilt containers**.
Start with pre-packaged and verified containers to quickly
provide support for commonly used dependencies while
improving license adherence.
[AWS Deep Learning Containers](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html) contain several deep
learning framework libraries and tools including TensorFlow,
PyTorch, and Apache MXNet with pre-validated license terms.
These containers maintain consistency while reducing the
risk of introducing unauthorized or incompatible packages.
- **Establish a privacy-preserving ML
workflow**. Implement data minimization principles
by using only the data necessary for your ML tasks. Apply
anonymization or pseudonymization techniques to sensitive
data before using it for training. Consider using
privacy-preserving ML techniques such as differential
privacy or federated learning for highly sensitive
applications. Document your privacy-preserving measures for
compliance-aligned purposes and to build trust with
stakeholders.
- **Monitor for license and privacy
adherence**. Implement continuous monitoring of
your ML environments to detect potential license violations
or privacy issues. Create automated checks for package
versions and license changes during CI/CD processes.
Regularly audit data access patterns to verify that they
comply with documented permissions and privacy requirements.
Establish a process for addressing issues when they arise.
- **Consider synthetic data for training
and testing**. Create synthetic datasets that
preserve the statistical properties of real data while
avoiding privacy concerns.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides capabilities for generating
synthetic data for training and testing ML models when using
real data presents privacy or licensing challenges. Document
the use of synthetic data in your ML pipelines to
demonstrate privacy-preserving practices.

## Resources

**Related documents:**

- [Protecting
compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html)
- [What
is AWS Deep Learning Containers?](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html)
- [AWS License Manager](https://aws.amazon.com/license-manager/)
- [Lifecycle
configurations within Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations.html)
- [Data
Privacy in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/data-privacy.html)
- [Best
practices for endpoint security and health with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practice-endpoint-security.html)
- [Private
package installation in Amazon SageMaker AI running in
internet-free mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/)
- [Machine
Learning Best Practices in Financial Services](https://aws.amazon.com/blogs/machine-learning/machine-learning-best-practices-in-financial-services/)

**Related videos:**

- [Machine
Learning Best Practices in Financial Services](https://youtu.be/HlSEUvApDZE?t=578)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec01-bp01.html*

---
