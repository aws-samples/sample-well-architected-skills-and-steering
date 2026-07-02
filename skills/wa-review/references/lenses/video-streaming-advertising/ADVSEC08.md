# ADVSEC08 — Brand safety

**Pillar**: Security  
**Best Practices**: 2

---

# ADVSEC08-BP01 Create guardrails and controls to maintain brand safety and content moderation within your workload

Brand reputation protection can block brand association with
inappropriate or otherwise harmful content. Having guardrails
can maintain customer trust and potential business
relationships while avoiding reputational damage and negative
publicity.

## Implementation guidance

Consider implementing Amazon SageMaker AI, with the
custom model development capability of SageMaker AI, you can
build, train, and deploy custom machine learning models.
Designing a guardrail for brand safety could allow you to
develop a model that could detect inappropriate imagery in
advertisements, classify text within content for sentiment and
safety, and predict the likelihood of an ad placement being
brand appropriate. With the real time inference capability of
SageMaker AI, you can deploy your models deemed brand safe for
real time content analysis, allowing for quick decision making
for your solution.

Additionally, consider using AWS Config, to
assess, audit, and evaluate resource configurations within
your AWS environment. Config can track changes to underlying
resources with your advertising solution to verify that
security settings and access controls remain
compliance-aligned for brand safety.

## Key AWS services

- AWS Config
- Amazon SageMaker AI

## Resources

- [Examples and More Information: Use Your Own Algorithm or Model](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-notebooks.html)
- [Compliance](https://docs.aws.amazon.com/config/latest/APIReference/API_Compliance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp01.html*

---

# ADVSEC08-BP02 Look for opportunities to block ad fraud and enhance transparency in your advertising solution

DSP’s need to verify their advertisers and agencies are
purchasing legitimate advertising inventory across potentially
multiple exchanges in real time. Consider implementing an
ads.txt file, designed by IAB tech labs, is designed to enable
additional transparency within the advertising solution by
allowing DSPs to review legitimate companies authorized to
market their advertisement inventory.

## Implementation guidance

Adding an `ads.txt` file
lets ad publishers declare which services can market their ad
space. Retailers can verify incoming advertisement inventory
against the list to verify authenticity. This aids in fraud
prevention by blocking domain spoofing threats by bad actors
impersonating legitimate publishers. The file also aids in
protecting DSP’s budgets and campaigns performance. Ads.txt
may also aid in compliance by meeting certain criteria large
advertisers require within their best practices.

Consider
using Amazon S3 to host your `ads.txt` file for highly available
and simple access. Amazon S3 allows for version control and
accessible updates to the file if needed. Lastly, within Amazon S3,
you can block object version deletion using S3 object lock.
This defined retention period can be used as an extra layer of
data protection.

## Key AWS services

- Amazon S3

## Resources

- [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp02.html*

---
