# EUCSEC11 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC11-BP01 Perform vulnerability scanning on EUC instances

The frequent release of patches for vulnerabilities in operating
systems and applications means that you should patch them on a
frequent basis to address potential risks.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Perform frequent vulnerability
scanning and patch instances accordingly:**
Software patching is critical for the security and
performance of compute resources. Frequent patching is a
best practice in the security pillar of the
Well-Architected Framework.
- **Regularly patch Amazon AppStream
2.0 images:** As part of the AWS Shared
Responsibility Model, customers are responsible for
patching and securing their WorkSpaces Applications images. When an
image is built and deployed, there are five categories of
software that require patching in your WorkSpaces Applications
image:

- **Applications and
dependencies:** Customers are responsible for
patching the applications and dependencies in images.
- **Operating system:**
Customers are responsible for installing and maintaining
updates for Linux and Windows.
- **Software components:**
These are drivers, agents, and other software required for
WorkSpaces Applications operation (for example, the Amazon CloudWatch agent). WorkSpaces Applications periodically releases new
base images that contain new agents and drivers. Customers
can recreate their images using the latest base image to
bring the software components to the latest baseline.
- **WorkSpaces Applications agent**:
Customers can choose to consistently use the latest agent
version in the Image Assistant. With this option,
streaming instances that are launched from the image
automatically use the latest version of the agent.
- **Clients**: Where the
Amazon WorkSpaces Applications client is in use, this should also be
updated upon the release of each new version.

- **Regularly patch Amazon WorkSpaces
Personal instances:** Amazon WorkSpaces Personal
instances need to be scanned for vulnerabilities and
patched regularly post-deployment. Use configuration
management tools or patch management tools to satisfy the
requirement for ongoing assessment and deployment of
patches. The Amazon WorkSpaces client should also be
updated upon the release of a new version.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec11-bp01.html*

---
