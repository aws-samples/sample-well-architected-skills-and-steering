**Pillar**: Cost Optimization

# FSICOST05: How do you track anomalies in your ongoing costs for AWS services?

Understanding your organization's costs and drivers is critical for managing your cost
and usage effectively, and identifying cost-reduction opportunities. Accurate cost and usage
monitoring allows you to make more informed decisions about where to allocate resources
within your organization.

## FSICOST05-BP01 Be aware of anomalies and periodically review your architecture

Anomalies can drive up cost. Set up AWS Cost Anomaly Detection to detect and alert
on anomalous spend patterns in your deployed AWS services. Cost Anomaly Detection
automatically determines thresholds each day by adjusting for organic growth and seasonal
trends (like usage increases from Sunday to Monday or increased spend at the beginning of
the month) through machine learning models. Financial systems usually integrate with
several other third-party systems, and Cost Anomaly Detection can integrate with these
systems as well.

Extend Cost Anomaly Detection with custom metrics such as `token_in`,
`token_out`, and `embedding_ops`, and route alerts to product or
data owners when cost spikes correspond to new prompt deployments, unexpected
retrieval-augmented generation (RAG) expansion, or fine-tuning jobs running out of
schedule. Combine these alerts with CloudWatch dashboards to correlate generative AI usage
trends with cost anomalies in near real-time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost05.html*
