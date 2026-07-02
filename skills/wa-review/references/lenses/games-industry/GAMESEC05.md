# GAMESEC05 — Detection

**Pillar**: Security  
**Best Practices**: 2

---

# GAMESEC05-BP01 Implement a comprehensive data collection strategy to monitor player behavior

To maintain a positive player experience, implement a
comprehensive data collection and analysis strategy. Capturing,
storing, and analyzing relevant data provides insights into how
players interact with your game's features and with each other.
This data-driven approach can guide decision-making, enhance
player engagement and retention, optimize monetization strategies,
and ultimately improve the overall player experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement data collection systems to capture and log relevant
player actions, such as gameplay sessions, progress, achievements,
purchases, interactions with game elements, and social activities.
Collect server-side data like server load, network traffic, and
error logs to monitor the technical performance and identify
potential issues. Gather player feedback through surveys, forums,
support tickets, and social media channels to understand their
experiences and preferences.

When storing your game data, establish a centralized data
warehouse or data lake to store and organize the collected data
and implement pipelines for data cleaning, transformation, and
aggregation to prepare the data for efficient analysis.

After storing the data, analyze it to gain insights such as player
retention and churn, monetization strategies, and feature usage
through data visualization tools.

### Implementation steps

- Capture and log player actions, server-side metrics, and
feedback to monitor interactions and technical performance.
- Use a centralized data warehouse like Amazon Redshift or S3
data lake to store, clean, transform, and organize game data
for analysis.
- Analyze collected data with visualization tools, like Amazon Quicksight, to gain insights into player retention,
monetization, and feature usage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec05-bp01.html*

---

# GAMESEC05-BP02 Collect, store, and analyze player usage logs to detect inappropriate behavior

Instrument your game to collect logs to understand how players use
the features of your game and how they interact with other players.
You can then block unauthorized activities that can degrade the
player experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Send structured log events to
the [Game
Analytics Pipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/), by using a logging solution such as
[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) or
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), or through a solution from an AWS
Partner such
as [Datadog](https://www.datadoghq.com/),
[Sumo Logic](https://www.sumologic.com/),
[New Relic](https://newrelic.com/),
[Honeycomb.io](https://www.honeycomb.io/),
or [Splunk](https://www.splunk.com/).
Structure these player usage logs so that they can be used to
detect when specific actions by players need to be investigated.

After you have captured the data, consider implementing tools to
detect inappropriate usage behavior. For example, if your game has
social features such as in-game player messaging, voice chat, or
online forums, save logs from these player engagements in a format
that can be analyzed for moderation purposes.

Configure your game's voice chat feature to export recordings to
Amazon S3 and
use [Amazon Transcribe](https://aws.amazon.com/transcribe) to convert the audio speech to text format which
can be stored for processing. Alternatively, you can perform
real-time streaming transcription by integrating your game backend
voice chat service directly with the Transcribe API
to [transcribe
streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html) in real time. Moderation teams can manually
review the content, and once the content is in a standard format,
you can also use AWS AI/ML services to perform moderation
automatically.
[Amazon Comprehend](https://aws.amazon.com/comprehend/) can be used to perform natural language
processing (NLP) to uncover information from the unstructured
text, which can classify and organize the conversations into
relevant topics and identify inappropriate behavior such as
profanity.

### Implementation steps

- Collect, store, and analyze player usage logs.
- Use AWS services for artificial intelligence and machine
learning to more efficiently review and gain insights into
your player usage logs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamsec05-bp02.html*

---
