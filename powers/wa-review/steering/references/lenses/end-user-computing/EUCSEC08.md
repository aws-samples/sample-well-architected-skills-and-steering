# EUCSEC08 — Detection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC08-BP01 Install endpoint protection software on instances to detect unexpected behavior

Endpoint protection software can provide the capability to
detect anomalous behavior on end user computing services.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Configure security software for
Amazon WorkSpaces Applications:** If you choose to install
security software (for example, anti-virus or behavioral
anomaly detection) on your image, we recommend that you do
not enable automatic updates for the software. Otherwise,
the software may attempt to update itself with the latest
definition or configuration files or other updates during
user sessions, which can affect performance. In addition,
updates made to the software will not persist beyond the
current user session. To verify that your fleet instances
have the latest updates, we recommend that you do either
of the following:

Update your image builder and create a new image on a
regular basis (for example, by using the Image
Assistant CLI operations).
- Use security software that delegates scanning,
detection, or other operations to an continuously
updated external server.
- For more detail, see
[Administer
Your Amazon WorkSpaces Applications Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#windows-update-antivirus-software-av) and

[Best
Practices for Deploying Amazon WorkSpaces Applications](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/security-1.html).

- **Configure security software for Amazon WorkSpaces:** Security software can adversely affect the operation of Amazon WorkSpaces if it is not configured to consider the requirements of the service. For details on the configuration elements that are required to be considered as exclusions for anti-malware scanning, see [Required configuration and service components for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/required-service-components.html).

The configuration of endpoint security software should verify that the status of the agents deployed on Amazon WorkSpaces is centralized to provide a consolidated view of the status of the deployed Amazon WorkSpaces.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec08-bp01.html*

---
