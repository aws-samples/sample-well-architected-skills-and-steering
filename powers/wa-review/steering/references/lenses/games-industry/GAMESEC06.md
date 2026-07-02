# GAMESEC06 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 3

---

# GAMESEC06-BP01 Use tools for detecting and responding to threats to your infrastructure

To continuously monitor for malicious activities and unauthorized
behaviors within your AWS environment, consider
using [Amazon GuardDuty](https://aws.amazon.com/guardduty/). GuardDuty identifies threats by monitoring
account behavior, network activity, and data access patterns
within your environment. It analyzes events across multiple data
sources, such as CloudTrail event logs, Amazon VPC Flow Logs, and
DNS logs for potential threats. By integrating with Amazon CloudWatch Events and Lambda, GuardDuty alerts can be
automatically forwarded to relevant security teams for further
analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) provides a comprehensive view of your security
state in AWS and check your environment against security industry
standards and best practices. Security Hub CSPM collects security data
from across AWS accounts, services, and supported third-party
partner products and analyzes your security trends and identify
the highest priority security issues.
The [Amazon GuardDuty](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html)
[integration
with Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html) enables you to send findings from
GuardDuty to Security Hub CSPM. Security Hub CSPM can then include those
findings in its analysis of your security posture.

It's common for bad actors to employ bots to take over accounts
and cheat in
games. [WAF
Bot Control](https://aws.amazon.com/waf/features/bot-control/) gives you visibility and control over common
and pervasive bot traffic that can consume excess resources, skew
metrics, cause downtime, or perform other undesired activities.

Ransomware is malicious code designed to gain unauthorized access
to systems and datasets and encrypt that data to block access by
legitimate players. After ransomware has locked players out of
their systems and encrypted their sensitive data, cyber criminals
demand a ransom before providing a decryption key to unlock the
data. Organizations can be completely shut down by a malicious
event, incurring significant costs and loss of business
productivity. Refer
to [Securing
your AWS Cloud environment from ransomware](https://d1.awsstatic.com/WWPS/pdf/AWSPS_ransomware_ebook_Apr-2020.pdf) for best
practices that you can apply to strengthen your ability to fight
ransomware before, during, and after an incident takes place.

Your game may provide players with the ability to contact player
support agents through a call center such
as [Amazon
Connect](https://aws.amazon.com/connect/) or chat bots using Amazon Lex. Amazon Connect
provides support
for [monitoring
live and](https://docs.aws.amazon.com/connect/latest/adminguide/monitoring-amazon-connect.html)
[recorded
conversations](https://docs.aws.amazon.com/connect/latest/adminguide/monitoring-amazon-connect.html). To analyze interactions between players and
player support chat bots built with Amazon Lex, you can store the
[conversation
logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-cw.html) from these interactions in Amazon CloudWatch Logs
which can be exported to Amazon S3 and analyzed as described
previously.

Finally, conduct penetration testing exercises as part of your
infrastructure protection strategy. Whether you are performing
these assessments in-house or through an AWS Partner, adhere to
the
[AWS customer support policies for penetration testing](https://aws.amazon.com/security/penetration-testing/).

### Implementation steps

- Use Amazon GuardDuty to monitor account behavior, network
activity, and data access patterns for threats, and
integrate with Security Hub CSPM for a unified security view.
- Implement AWS WAF Bot Control to help detect and mitigate
bot traffic that can harm resources and player experiences.
- Conduct penetration testing exercises regularly, adhering to
AWS customer support policies, to assess and strengthen your
security posture.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec06-bp01.html*

---

# GAMESEC06-BP02 Use artificial intelligence and machine learning tools to automate aspects of your infrastructure protection strategy

[Amazon
Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/) uses machine learning to automatically
detect and diagnose anomalies in your business and operational
data and monitors the metrics that are most important to your
businesses with greater speed and accuracy. The service also makes
it straightforward to diagnose the root cause of anomalies, such
as a sudden dip in revenue, logins, transactions, or retention. It
does not require game developers to have ML experience to set up
and can connect to popular data sources including Amazon S3,
Amazon CloudWatch, Amazon RDS, Amazon Redshift, as well as many
SaaS applications. For example, you
can [integrate
Amazon Lookout for Metrics with the Game Analytics
Pipeline](https://aws.amazon.com/blogs/gametech/detect-game-anomalies-amazon-lookout-for-metrics-game-analytics-pipeline/) and other data sources to begin analyzing behavior
to detect anomalies.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Alternatively, you may choose to build, train, and host a custom
machine learning model using
[Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker/) to address use cases such as content
moderation, toxicity detection, cheat detection, fraud detection,
and more.

**Customer example**

AnyCompany Games uses Amazon Lookout for Metrics to automatically
detect unusual patterns in server performance, player login
attempts, or transaction volumes that could indicate threats from
bad actors. Additionally, they have used Amazon SageMaker AI to
develop custom machine learning models that continually analyze
network traffic patterns and player behavior to help identify
coordinated threats, such as bot networks that are attempting to
exploit their virtual economy.

This automated approach allows their security team to focus on
investigating and responding to genuine threats rather than
manually monitoring thousands of metrics, while making sure that
emerging threat patterns are detected and addressed before they
can significantly impact game availability or player safety.

### Implementation steps

- Use Amazon Lookout for Metrics to help automatically detect
and diagnose anomalies in key business and operational data
- Integrate Amazon Lookout for Metrics with data sources like
the Game Analytics Pipeline, Amazon S3, or CloudWatch to
monitor metrics such as revenue, logins, and retention.
- Use Amazon SageMaker AI to build, train, and host custom
machine learning models for advanced use cases like cheat
detection, fraud prevention, and content moderation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec06-bp02.html*

---

# GAMESEC06-BP03 Use insights from system-level logs to continuously improve your infrastructure protection strategy

Capture and store system-level logs from relevant services, such
as [S3
server access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html),
[CloudFront
access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html), and
[ALB
access](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)
[logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html).
These logs can be stored in an S3 bucket in your account and are
useful for associating your player usage information from within
the game with system-level information including connection
details such as IP addresses, request headers, and relevant
request manipulation and filtering that you may have configured
within your game backend. You can send these logs to the same
logging solutions mentioned earlier, and you can
[analyze
them using SQL queries with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html) without requiring
the logs to be moved out of Amazon S3.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Access
Analyzer for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-analyzer.html) is a feature that monitors your bucket
access policies, making sure that the policies provide only the
intended access to your Amazon S3 resources. Access Analyzer for
S3 evaluates your bucket access policies and allows you to
discover and swiftly remediate buckets with potentially unintended
access.

### Implementation steps

- Use AWS services for threat detection and incident response
to automate aspects of your infrastructure protection
strategy.
- Gain insights into your infrastructure protection through
system-level logs and AWS services for artificial
intelligence and machine learning.

## Data protection

When developing and architecting your game, consider what type of
data your studio is gathering and how you have decided to approach
protecting it. Topics to explore within this aspect of security
include:

- How you have chosen to identify and classify your data
- How you are protecting data at rest
- How you are protecting data in transit

There are no data protection best practices specific to the Games
Lens. Refer to the Well-Architected Framework whitepaper for best
practices
in [data
protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) for security.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec06-bp03.html*

---
