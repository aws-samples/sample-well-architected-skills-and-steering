# Security

**Pillar**: Security  
**Questions**: 9

---

# MIDASEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 6

---

# MIDASEC01-BP01 Create a security Shared Responsibility Model

Define and document a customized Shared Responsibility Model (SRM) that explicitly
separates the security responsibilities between cloud environment, IT, and OT stakeholders.
This provides clarity when managing security across cloud, edge, and on-premises industrial
assets.

**Desired outcome:** Manufacturing stakeholders understand
their distinct responsibilities in securing the infrastructure, data, and workloads across the
IT/OT boundary.

**Benefits of establishing this best practice:** Reduces
ambiguity during audits and incidents, strengthens collaboration across IT/OT, and supports
secure innovation by clarifying boundaries of responsibility.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use the AWS Shared Responsibility Model as a foundation, then extend it to cover the
specific roles and responsibilities across your IT and OT teams.

### Implementation steps

- Review the AWS Shared Responsibility Model and corresponding manufacturing
standards (for example, IEC 62443).
- Identify and document key security ownership across cloud, edge, and on-premises
systems.
- Collaborate with IT, OT, and third-party vendors to define shared controls and
data ownership boundaries.
- Incorporate the SRM into onboarding and compliance training for manufacturing
teams.

## Resources

**Related documents:**

[Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

[AWS Security Foundations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/security-foundations.html)

[Amazon
IoT](https://aws.amazon.com/iot/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp01.html*

---

# MIDASEC01-BP02 Standardize security baseline and implement role-based access controls

Establish a standardized security configuration across accounts and workloads using AWS Organizations, AWS IAM, and control policies. Implement role-based access controls (RBAC) to
limit access based on job function and responsibility, especially across IT and OT
environments.

**Desired outcome:**Establish consistent security controls
across industrial cloud workloads that help protect both IT systems (MES, ERP) and OT systems
(PLCs, SCADA), reducing exposure to unauthorized access and privilege escalation that could
impact manufacturing operations.

**Benefits of establishing this best practice:**Enables
centralized governance across IT and OT environments, improves auditability of manufacturing
system access, and minimizes risk of misconfigurations through role-based controls aligned
with production requirements.

**Level of risk exposed if this best practice is not
established:** High

## Implementation steps

- Define roles and responsibilities across IT and OT personas (for example,
automation engineers, data scientists, or vendors).
- Create and assign IAM roles and policies aligned to job responsibilities.
- Use AWS IAM Identity Center for central identity management and federated access.
- Apply SCPs to enforce service-level restrictions at the organizational unit (OU)
level.

## Resources

**Related documents:**

- [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp02.html*

---

# MIDASEC01-BP03 Secure machine-to-machine and human-to-machine access

Help protect communication between devices and systems in industrial settings by securing
machine-to-machine (M2M) and human-to-machine (H2M) access using authentication,
authorization, and encryption methods tailored to industrial protocols and devices.

**Desired outcome:** Avoid unauthorized access to industrial
devices and trace actions across automation systems.

**Benefits of establishing this best practice:** Reduces the
scope of impact, improves system integrity, and provides operational visibility for audit and
compliance.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use X.509 certificates for M2M identity, IoT policies for access control, and managed
bastion solutions like AWS Systems Manager Session Manager for H2M.

### Implementation steps

- Provision devices with unique X.509 certificates using AWS IoT Core.
- Define and enforce AWS IoT policies for device communication.
- Use AWS Systems Manager Session Manager for secure remote access to edge and OT
assets.
- Monitor access using AWS CloudTrail and AWS IoT Device Defender.

## Resources

**Related documents:**

[Iot Security Best Practices](https://docs.aws.amazon.com/iot/latest/developerguide/iot-security-best-practices.html)

[Session Manager Userguide](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp03.html*

---

# MIDASEC01-BP04 Automate monitoring and reporting with cloud-ready compliance tools

Automate the collection, evaluation, and reporting of compliance evidence using AWS Cloud
tools. Tailor configurations to meet industry-specific regulatory requirements such as NIST,
CMMC, or ISO and IEC standards for manufacturing.

**Desired outcome:** Ongoing compliance posture monitoring and
reduced manual effort in security and audit processes.

**Benefits of establishing this best practice:** Improves audit
readiness, reduces cost and error in manual compliance efforts, and verifies continuous
governance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish manufacturing compliance baselines by documenting the required controls for
industrial systems and mapping them to technical implementations.

Then, implement automated monitoring that evaluates industrial system configurations,
tracks security control changes, and validates compliance with manufacturing standards.

Use AWS Config, Security Hub CSPM, and Audit Manager, configured specifically for
manufacturing environments, to continuously monitor both IT and OT systems while maintaining
required compliance evidence.

### Implementation steps

- Enable AWS Config across all Regions and accounts.
- Use AWS Security Hub CSPM to aggregate security findings.
- Map controls in AWS Audit Manager to your industry framework.
- Schedule automated compliance report generation and alerting.

## Resources

**Related documents:**

- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html)
- [What is AWS Security Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [What is AWS Audit Manager?](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp04.html*

---

# MIDASEC01-BP05 Implement incident response playbooks

Develop and test incident response playbooks for common OT/IT scenarios such as device
compromise, unauthorized access, and data exfiltration. Verify your cross-functional
coordination and readiness to minimize downtime and safety risks.

**Desired outcome:** Manufacturing organizations respond to
incidents swiftly with predefined procedures, minimizing production disruption.

**Benefits of establishing this best practice:** Improves MTTD
and MTTR, reduces risk of safety events, and improves regulatory and audit outcomes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS Systems Manager, AWS Lambda, and Amazon EventBridge to automate containment and
response. Simulate scenarios to validate readiness.

### Implementation steps

- Identify critical incident types and build corresponding playbooks.
- Use AWS Systems Manager Automation to orchestrate predefined remediation.
- Run chaos experiments using AWS Fault Injection Service to test response
efficacy.
- Train IT and OT teams on roles and escalation procedures.

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp05.html*

---

# MIDASEC01-BP06 Establish a communication protocol between IT and OT systems

Define secure communication and data exchange methods between IT and OT environments. Use
edge services to control and monitor flows across the boundary and verify that only authorized
systems interact.

**Desired outcome:** Reduced risk of unintended system access
and data leakage between IT and OT, while enabling secure data-driven operations.

**Benefits of establishing this best practice:** Promotes
security-by-design, improves clarity in responsibility demarcation, and supports long-term
scalability and digital transformation.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish secure communication patterns between IT and OT networks by defining allowed
protocols, data flows, and security controls.

Implement edge processing capabilities to manage data exchange, using protocol gateways
for format translation and security enforcement.

Monitor all cross-boundary communications and implement automated alerts for
unauthorized access attempts. This can be achieved using AWS IoT Greengrass and AWS IoT SiteWise for edge management, but the key is maintaining clear security boundaries while
enabling necessary operational data flows.

### Implementation steps

- Use AWS IoT Greengrass to manage and secure data ingestion at the edge.
- Define and monitor edge-to-cloud traffic patterns.
- Use VPC endpoints and private connectivity where needed for isolation.
- Document IT and OT interfaces, protocols, and access policies.

## Resources

**Related documents:**

- [What is AWS IoT Greengrass?](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-aws-iot-greengrass.html)
- [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iotsitewise/latest/userguide/what-is-sitewise.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp06.html*

---

# MIDASEC02 — Identity and access management

**Pillar**: Security  
**Best Practices**: 4

---

# MIDASEC02-BP01 Enforce least privilege and security policies to control system access

Minimize access rights for users and systems by enforcing least privilege principles.
This reduces the risk of lateral movement and privilege escalation in manufacturing
environments.

**Desired outcome:** Users and systems can only access
resources necessary for their roles, reducing exposure to unauthorized activities.

**Benefits of establishing this best practice:** Limits the
scope of security incidents and enhances overall control over sensitive manufacturing
resources.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Map access requirements for different production roles and critical system
interactions. Implement IAM policies and SCPs aligned with manufacturing functions,
enforcing clear boundaries between IT/OT systems. Monitor access patterns using AWS IAM Access Analyzer to continually align with operational needs.

### Implementation steps

- Conduct role analysis across IT/OT to define minimum required privileges.
- Apply IAM permission boundaries and SCPs at account and organizational unit
levels.
- Use IAM Access Analyzer to detect overly permissive roles.
- Implement regular audits to verify adherence to least privilege policies.

## Resources

**Related documents:**

- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp01.html*

---

# MIDASEC02-BP02 Enable multi-factor authentication (MFA) and token authorization (TA)

Strengthen identity verification by enforcing MFA for human users and implementing
token-based authorization for machines and services.

**Desired outcome:** Stronger authentication for both human
users and industrial systems accessing AWS resources.

**Benefits of establishing this best practice:** Reduces risks
associated with credential theft and replay attacks across IT/OT boundaries.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Enable MFA across all accounts, and integrate token services for secure, time-bound
access.

### Implementation steps

- Require MFA for all AWS accounts and IAM users using virtual or hardware devices.
- Implement SSO with MFA enforcement using AWS IAM Identity Center.
- Use temporary credentials and tokens through AWS Security Token Service for
federated and service access.
- Enable and monitor MFA usage compliance with AWS Config rules.

## Resources

- [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [What is AWS Identity and Access Management Access Analyzer?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Welcome to the AWS Security Token Service API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp02.html*

---

# MIDASEC02-BP03 Use centralized access management tools

Consolidate identity and access management using centralized tools to streamline
permission handling and improve visibility across multi-site operations.

**Desired outcome:** Reduced access complexity and improved
governance across distributed industrial environments.

**Benefits of establishing this best practice:** Simplifies
identity lifecycle management, supports consistent policy application, and enables centralized
logging.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Adopt AWS IAM Identity Center or integrate with external identity providers to unify
access controls.

### Implementation steps

- Set up IAM Identity Center or integrate AWS accounts with your identity provider
(for example, Active Directory).
- Configure fine-grained access permissions mapped to business roles.
- Enable centralized access logging and reporting.
- Regularly update identity mappings to reflect org structure changes.

## Resources

- [What is AWS IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp03.html*

---

# MIDASEC02-BP04 Develop a mechanism for regular review of IAM roles and policies

Establish processes to regularly review IAM roles and permissions to help prevent
privilege creep and maintain access integrity over time.

**Desired outcome:** Stale or over-permissive access is
detected and remediated proactively.

**Benefits of establishing this best practice:** Improves
compliance posture, reduces operational risk, and enforces clean access policies aligned to
least privilege.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use tools like IAM Access Analyzer, AWS Config, and custom automation to audit and
report access configuration regularly.

### Implementation steps

- Establish a schedule for IAM access reviews.
- Use AWS IAM Access Analyzer to identify unused or overly broad permissions.
- Log and track review outcomes for auditing purposes.
- Automate revocation or modification of unneeded permissions using AWS Lambda or
AWS Systems Manager.

## Resources

- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)
- [iam-user-policy-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-policy-check.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp04.html*

---

# MIDASEC03 — Detection

**Pillar**: Security  
**Best Practices**: 5

---

# MIDASEC03-BP01 Integrate and enforce privacy by design principles

Apply privacy-by-design principles in the architecture of manufacturing data environments
to help you comply with privacy regulations from the outset. This includes minimizing data
collection, embedding access controls, and anonymizing personal data.

**Desired outcome:** Data privacy is protected from the start
of the system design, reducing regulatory risks and improving trust with stakeholders.

**Benefits of establishing this best practice:** Aligns with
data protection regulations like GDPR or CCPA, reduces risk of breaches, and supports ethical
data use.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Design architectures with data minimization, separation, encryption, and auditability
as core principles.

### Implementation steps

- Identify personal and sensitive data processed within the manufacturing system.
- Limit collection and retention to only required fields and durations.
- Implement anonymization or pseudonymization where applicable.
- Embed access controls and audit logs from the start.

## Resources

- [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)
- [Privacy by Design on AWS](https://docs.aws.amazon.com/whitepapers/latest/privacy-by-design-on-aws/privacy-by-design-on-aws.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp01.html*

---

# MIDASEC03-BP02 Implement industrial data classifications and protection policies

Define classification tiers for industrial data (for example, public, internal,
confidential, and restricted), and apply policies to control access, visibility, and
protection levels accordingly.

**Desired outcome:** Manufacturing data is systematically
classified and protected based on its criticality and sensitivity.

**Benefits of establishing this best practice:** Reduces risk
of data leakage, safeguards sensitive data, and supports scalable governance models.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS tools like Amazon Macie and AWS IAM policies to tag, monitor, and restrict
access to classified data.

### Implementation steps

- Define classification categories based on business needs and risk.
- Tag data assets using AWS resource tags or AWS AWS Glue Data Catalog.
- Use Amazon Macie to identify and monitor sensitive data types.
- Enforce access controls and monitoring based on classification tags.

## Resources

- [What is Amazon Macie?](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [Populating the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp02.html*

---

# MIDASEC03-BP03 Identify source data and set data classifications

Discover and classify data at the source (for example, sensors, PLCs, MES, and ERP
systems) to apply appropriate controls from ingestion onward.

**Desired outcome:** Data is classified and governed from the
moment it enters the system, helping prevent downstream risk exposure.

**Benefits of establishing this best practice:** Improves
control over high-risk data, simplifies pipeline security, and enhances lineage tracking and
compliance auditing.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Build data ingestion pipelines with tagging and classification integrated into the
ingestion and cataloging layers.

### Implementation steps

- Identify all upstream data sources contributing to the system.
- Use edge and gateway services to apply initial metadata or tags.
- Ingest data into AWS using services like Amazon Kinesis, AWS IoT Core, or AWS IoT SiteWise with classification.
- Catalog and tag datasets in AWS Glue or AWS Lake Formation.

## Resources

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp03.html*

---

# MIDASEC03-BP04 Implement industrial encryption policies

Apply encryption policies across all layers of the manufacturing data system, including
at rest, in transit, and optionally during processing, to help protect sensitive operational
and proprietary information.

**Desired outcome:** Data remains encrypted end-to-end,
providing confidentiality and integrity and helping with regulatory alignment.

**Benefits of establishing this best practice:** Reduces impact
of data breaches, supports regulatory compliance, and builds trust with partners and
customers.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS KMS for key management and enforce encryption using S3 bucket policies, VPC
security, and service-level configurations.

### Implementation steps

- Enable default encryption on all data stores (for example, Amazon S3, Amazon RDS,
Amazon Redshift, and Amazon DynamoDB).
- Use TLS 1.2+ for all data in transit.
- Create customer-managed keys (CMKs) using AWS KMS for sensitive workloads.
- Regularly rotate keys and audit access with AWS CloudTrail.

## Resources

- [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp04.html*

---

# MIDASEC03-BP05 Implement data retention policies for each data class

Define and enforce data retention rules based on classification and regulatory
requirements to reduce storage costs and minimize compliance risks.

**Desired outcome:** Only required data is retained, improving
cost efficiency and reducing exposure of legacy data.

**Benefits of establishing this best practice:** Helps prevent
unnecessary storage costs, reduce audit complexity, and support lifecycle compliance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use Amazon S3 lifecycle policies, AWS Glue table TTLs, and tagging strategies to
automate enforcement of retention policies.

### Implementation steps

- Define data retention durations based on classification and compliance needs.
- Apply tags and metadata to datasets to identify lifecycle requirements.
- Use S3 lifecycle rules or Glue jobs to delete or archive data.
- Regularly review and update retention policies based on changing regulations.

## Resources

- [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp05.html*

---

# MIDASEC04 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC04-BP01 Segment OT networks from IT systems

Establish clear segmentation between OT networks and IT systems to limit the scope of
impact and reduce risk of lateral movement between environments.

**Desired outcome:** OT systems are logically and physically
isolated from IT networks while enabling secure data flows.

**Benefits of establishing this best practice:** Reduces
propagation of malware, minimizes risk of compromise of safety-critical systems, and supports
compliance with industrial cybersecurity frameworks.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Implement logical segmentation using VPCs, subnets, routing controls, and edge
gateways. Verify that minimal and controlled data flows between domains.

### Implementation steps

- Design separate network segments for IT and OT environments using VPCs and
subnets.
- Deploy gateway services like AWS IoT Greengrass or AWS Transit Gateway to manage
traffic between zones.
- Apply network ACLs and security groups to limit access paths.
- Log and monitor all cross-boundary traffic using VPC Flow Logs and AWS Network Firewall.

## Resources

- [Secure data ingestion from OT to IT using AWS IoT SiteWise and AWS IoT Greengrass](https://aws.amazon.com/blogs/iot/secure-data-ingestion-from-ot-to-it-using-aws-iot-sitewise-and-iot-greengrass/)
- [Security in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec04-bp01.html*

---

# MIDASEC04-BP02 Use firewalls, perimeter networks, and dedicated network zones

Implement perimeter defenses such as firewalls, perimeter networks and dedicated network
zones to manage and secure traffic flows between cloud, IT, and OT systems.

**Desired outcome:** Traffic is filtered and restricted at each
trust boundary to enforce zero trust and layered defense.

**Benefits of establishing this best practice:** Helps improve
network security posture, prevent direct exposure of OT systems, and support layered
defense-in-depth architecture.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Deploy AWS Network Firewall, private subnets, and multi-tier perimeter network
architectures to filter and control inbound and outbound traffic.

### Implementation steps

- Deploy AWS Network Firewall or third-party appliances in VPCs.
- Create perimeter networks between public internet and sensitive workloads using
public and private subnet models.
- Enforce rule groups that restrict IPs, ports, and protocols.
- Continuously monitor and update firewall rules and network configurations.

## Resources

- [What is AWS Network Firewall?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
- [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://aws.amazon.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec04-bp02.html*

---

# MIDASEC05 — Data protection

**Pillar**: Security  
**Best Practices**: 3

---

# MIDASEC05-BP01 Define access permissions

Establish clear and granular access permissions to control who can access industrial
data, based on job roles and operational responsibilities.

**Desired outcome:** Only authorized personnel can access
specific data resources, reducing the risk of data leakage or misuse.

**Benefits of establishing this best practice:** Supports
principle of least privilege, improves accountability, and reduces insider threats.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use IAM policies and resource tagging strategies to enforce fine-grained permissions
aligned to user roles.

### Implementation steps

- Inventory data assets and define roles for access control.
- Apply IAM roles and permissions based on job functions.
- Use resource tags to apply conditional access policies.
- Review and refine permissions regularly using AWS IAM Access Analyzer.

## Resources

- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp01.html*

---

# MIDASEC05-BP02 Build user identity solutions

Deploy centralized identity systems that integrate with existing directories and cloud
resources to manage user authentication and authorization efficiently.

**Desired outcome:** Consistent and secure identity management
across all industrial and cloud systems.

**Benefits of establishing this best practice:** Improves user
lifecycle management, simplifies access governance, and enhances login security with MFA and
federation.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement AWS IAM Identity Center or integrate third-party identity providers with AWS.

### Implementation steps

- Deploy IAM Identity Center for central identity control.
- Enable federation with existing AD or SAML-based systems.
- Set up MFA for all privileged roles and access points.
- Log all authentication events using AWS CloudTrail.

## Resources

- [AWS Identity and Access Management Access Analyzer](https://aws.amazon.com/iam/identity-center/)
- [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp02.html*

---

# MIDASEC05-BP03 Implement data authorization models

Design and implement scalable data authorization frameworks using attribute-based or
role-based access control (ABAC or RBAC) models.

**Desired outcome:** Users are granted access to data based on
roles, attributes, or context, supporting scalable and secure access decisions.

**Benefits of establishing this best practice:** Improves
flexibility in data sharing, reduces over-permissions, and enhances compliance controls.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Define authorization attributes based on manufacturing context (like job function,
facility, equipment type, or product line). Implement access controls using AWS Lake Formation for data-level permissions, AWS IAM conditions for resource access, and custom
logic for specialized manufacturing scenarios.

Regularly review access patterns to verify alignment with production needs while
maintaining security boundaries between IT and OT systems.

### Implementation steps

- Define business roles and relevant attributes (for example, plant location or
department).
- Implement policies in Lake Formation or Amazon S3 bucket policies using
conditions.
- Monitor access patterns and refine authorization models over time.
- Log and audit access for compliance reporting.

## Resources

- [What Is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp03.html*

---

# MIDASEC06 — Data protection

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC06-BP01 Use secure data exchange protocols

Use secure and standardized protocols for sharing industrial data internally and
externally, helping protect integrity and confidentiality.

**Desired outcome:** Data is transmitted securely across
different systems and organizations without unauthorized interception or tampering.

**Benefits of establishing this best practice:** Helps prevent
data breaches, supports secure collaboration, and aligns with industry data exchange
standards.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use MQTT over TLS, HTTPS, or OPC-UA with encryption and certificate-based
authentication.

### Implementation steps

- Configure IoT and gateway devices to communicate over secure protocols.
- Enforce TLS 1.2 or higher for all data-in-transit.
- Implement endpoint authentication using certificates or tokens.
- Monitor traffic for anomalies using AWS IoT Device Defender.

## Resources

- [AWS IoT Core protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)
- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp01.html*

---

# MIDASEC06-BP02 Establish clear data ownership and sharing agreements

Define clear ownership responsibilities and data sharing rules to guide access and usage
across internal teams and partner organizations.

**Desired outcome:** Data is shared responsibly, with clarity
around who controls, accesses, and governs its lifecycle.

**Benefits of establishing this best practice:** Improves
accountability, supports regulatory compliance, and fosters trusted partnerships in the
industrial environment.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Document data ownership roles and access conditions as part of your data governance
framework and reinforce with access controls.

### Implementation steps

- Identify and document data owners across all domains.
- Define acceptable use policies and access controls for each dataset.
- Use AWS Lake Formation and IAM policies to enforce agreements.
- Review agreements regularly to align with evolving compliance needs.

## Resources

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp02.html*

---

# MIDASEC07 — Incident response

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC07-BP01 Deploy continuous monitoring tools

Implement continuous monitoring of your industrial systems to detect and respond to
threats in real time. Monitoring should span cloud, edge, and on-premises systems across both
IT and OT environments.

**Desired outcome:** Security teams can detect anomalies and
threats early, reducing the impact of potential breaches.

**Benefits of establishing this best practice:** Enables
real-time visibility, faster incident response, and proactive threat mitigation.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS monitoring tools such as Amazon CloudWatch, AWS IoT Device Defender, and AWS Config to gather and analyze telemetry.

### Implementation steps

- Enable Amazon CloudWatch metrics and logs for all AWS workloads.
- Deploy AWS IoT Device Defender to monitor device behavior and audit
configurations.
- Use AWS Config to track configuration changes across resources.
- Integrate alerts with AWS SNS or AWS Security Hub CSPM for real-time response.

## Resources

- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html)
- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp01.html*

---

# MIDASEC07-BP02 Implement SIEM systems

Aggregate and analyze logs from industrial and cloud systems using a security information
and event management (SIEM) system to help detect and respond to threats efficiently.

**Desired outcome:** Centralized visibility across hybrid
environments enables faster detection of coordinated threats or unusual activities.

**Benefits of establishing this best practice:** Improves
threat correlation, reduces alert fatigue, and strengthens compliance with audit trails.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use Amazon Security Lake or integrate with third-party SIEM tools such as Splunk or IBM
QRadar for advanced analytics and incident workflows.

### Implementation steps

- Set up Amazon Security Lake to collect and normalize logs from AWS and industrial
sources.
- Integrate with a SIEM system for event correlation and alerting.
- Define detection rules and dashboards tailored to OT and ICS environments.
- Automate incident response workflows with runbooks or SOAR integrations.

## Resources

- [Amazon Security Lake](https://aws.amazon.com/security-lake/)
- [AWS SIEM Partners](https://aws.amazon.com/partners/siem/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp02.html*

---

# MIDASEC08 — Application security

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC08-BP01 Align security controls with industry standards

Implement security controls across industrial workloads, and map those controls to
recognized industry standards such as NIST 800-82, ISO/IEC 27001, and IEC 62443.

**Desired outcome:** Security implementations are auditable,
and your organization improves its compliance with applicable industrial regulations.

**Benefits of establishing this best practice:** Streamlines
audit processes, standardizes your security practices, and demonstrates due diligence in
regulated industries.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS Audit Manager and AWS Control Tower to align cloud configurations with
industry-standard security frameworks.

### Implementation steps

- Identify regulatory and industry-specific frameworks applicable to your
workloads.
- Map AWS services and controls to required standards using AWS Audit Manager
frameworks.
- Continuously monitor control adherence using AWS Config and Security Hub CSPM.
- Integrate compliance requirements into the CI/CD process for industrial apps.

## Resources

- [What is AWS Audit Manager?](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)
- [Security standards and controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec08-bp01.html*

---

# MIDASEC08-BP02 Conduct regular security awareness programs

Develop training and awareness programs for industrial application teams to reinforce
best practices, policy understanding, and threat awareness.

**Desired outcome:** Engineering and operations staff are
informed about evolving security threats and policies, reducing the risk of human error.

**Benefits of establishing this best practice:** Improves
organizational security culture, reduces social engineering risks, and increases policy
adherence.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Deliver targeted training sessions and simulate threat scenarios relevant to OT and
industrial environments.

### Implementation steps

- Identify key roles that need training (for example, developers, operators, and
integrators).
- Use AWS learning resources or third-party courses tailored to industrial
security.
- Conduct quarterly refresher sessions and phishing simulations.
- Track and report training completion and outcomes to leadership.

## Resources

- [AWS Security Fundamentals (Digital)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13441/aws-security-fundamentals)
- [NICE Framework Resource Center](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec08-bp02.html*

---

# MIDASEC09 — Application security

**Pillar**: Security  
**Best Practices**: 3

---

# MIDASEC09-BP01 Apply secure coding practices for applications and data integrations

Implement secure coding guidelines across industrial application development and
integration pipelines to help prevent common vulnerabilities.

**Desired outcome:** Software and data interfaces in industrial
systems are resilient against common attack vectors.

**Benefits of establishing this best practice:** Reduces
injection attacks and vulnerabilities in custom code and enables secure interoperability.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Adopt secure coding checklists (like OWASP), enforce static code analysis, and secure
APIs during development.

### Implementation steps

- Incorporate security requirements into software specifications.
- Use tools like Amazon CodeGuru Reviewer and SonarQube in pipelines.
- Secure APIs with authorization, throttling, and validation.
- Review and test all data transformations and payloads for tampering risks.

## Resources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [What is Amazon CodeGuru Reviewer?](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/what-is-codeguru-reviewer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp01.html*

---

# MIDASEC09-BP02 Perform regular vulnerability scans and penetration tests

Identify and mitigate vulnerabilities in applications and environments by conducting
recurring scans and authorized penetration testing.

**Desired outcome:** Exposed vulnerabilities are proactively
identified and mitigated before exploitation.

**Benefits of establishing this best practice:** Enhances
visibility into system weaknesses and builds resilience against external and internal threats.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use Amazon Inspector and integrate third-party scanning tools for deep and layered
assessments.

### Implementation steps

- Schedule recurring scans using Amazon Inspector across EC2 and container
workloads.
- Perform black-box and white-box pen tests with third-party experts.
- Integrate findings with AWS Security Hub CSPM for centralized visibility.
- Remediate critical vulnerabilities through prioritized CI/CD updates.

## Resources

- [Getting started with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting-started.html)
- [Penetration Testing](https://aws.amazon.com/security/penetration-testing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp02.html*

---

# MIDASEC09-BP03 Automate patch management for ICS and connected data infrastructure

Patch known vulnerabilities in a timely manner across industrial control systems (ICS),
gateways, and cloud services by automating patch management processes.

**Desired outcome:** Patches are deployed consistently and
timely, minimizing exposure to known exploits.

**Benefits of establishing this best practice:** Reduces manual
overhead, enhances system stability, and supports compliance with vulnerability remediation
SLAs.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use AWS Systems Manager Patch Manager for cloud-side automation and coordinate closely
with OT vendors for ICS-specific patch cycles.

### Implementation steps

- Inventory all patchable assets across OT and IT systems.
- Use AWS Systems Manager Patch Manager to automate patching for EC2 and managed
nodes.
- Align maintenance windows with production downtime cycles.
- Monitor patch compliance using AWS Config and AWS Systems Manager reports.

## Resources

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
- [Patch Orchestration with AWS Systems Manager](https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
