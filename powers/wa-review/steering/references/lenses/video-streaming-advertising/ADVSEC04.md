# ADVSEC04 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC04-BP01 Implement secure data collaboration with least privileged access and privacy controls

## Implementation guidance

Raw data that is used in collaboration with SSPs, DSPs, and
third-party systems need to be carefully shared to verify
consumer privacy and data protection. Consider using AWS
Clean Rooms, which enables more secure data collaboration
without potentially exposing raw data and allows different
parties to review and analyze data while maintaining strict
privacy controls. With AWS Clean Rooms, you can create a
more secure data clean room in minutes and collaborate with
other companies to generate unique insights about
advertising campaigns, investment decisions, and research
and development. AWS Clean Rooms automatically encrypts
service metadata at rest without requiring additional
configurations. AWS Clean Rooms allows for you to have
granular control on the type of information you may want to
share.

Use IAM to provide least privileged access to approved
parties with AWS Clean Rooms. Use IAM policies to define
which users and roles can access which data, analyses, and
collaborations. This allows for the precise control of how
data is created, modified, and queried within AWS Clean
Rooms.

### Key AWS services

- AWS Clean Rooms
- AWS IAM

### Resources

- [Solutions for Advertising and Marketing](https://aws.amazon.com/solutions/advertising-marketing/)
- [AWS Clean Rooms proof of concept scoping part 1: media measurement](https://aws.amazon.com/blogs/big-data/aws-clean-rooms-proof-of-concept-scoping-part-1-media-measurement/)
- [How AWS Clean Rooms works with IAM](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security_iam_service-with-iam.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec04-bp01.html*

---
