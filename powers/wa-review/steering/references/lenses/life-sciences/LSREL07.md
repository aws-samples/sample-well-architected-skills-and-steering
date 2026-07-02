# LSREL07 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 4

---

# LSREL07-BP01 Implement system-wide data checksums and transfer validation

Incorporate integrity verification at every transfer and
transformation stage. Use cryptographic checksums (like SHA-256 or
MD5) or ETags to validate files when moved into or across the cloud.
Use managed services like AWS DataSync or Amazon S3 replication that
perform integrity checks automatically. For domain-specific use
cases (like genomics and imaging), add plausibility checks to detect
biologically inconsistent results that may indicate processing
corruption.

**Desired outcome:** Data fidelity is
preserved during ingestion, transfer, and transformation, with
verifiable proof that data has not been altered.

**Common anti-patterns:**

- Moving data without checksum or hash verification.
- Relying solely on application logs to detect corruption.
- Using manual copy processes without automated validation.

**Benefits of establishing this best
practice:**

- Reduces risk of silent corruption during high-volume genomic or
imaging transfers.
- Increases trust in research outputs by deriving results
validated input data.
- Provides auditors and regulators with evidence of data integrity
safeguards.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Integrate checksums and validation at every stage where data is
moved or transformed. Cryptographic checksums (such as SHA-256) or
S3 ETags provide automated validation during transfers into cloud
storage. Managed services like AWS DataSync, S3 Replication, and
S3 Transfer Acceleration perform integrity checks by default,
reducing operational burden. For scientific pipelines, augment
checksum validation with domain-specific checks, such as detecting
biologically implausible variants in genomic data or corrupt
slices in imaging data.

### Implementation steps

- Data should be ingested into Amazon S3 where ETag-based
validation confirms file integrity.
- Use AWS DataSync for on-premises to cloud transfers,
verifying that validation occurs automatically.
- Configure S3 Replication with replication metrics enabled to
verify data consistency across buckets.
- For sensitive research workloads, embed integrity checks
directly into processing pipelines (for example, validating
SHA-256 digests before and after transformation).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp01.html*

---

# LSREL07-BP02 Build idempotent and reproducible processing pipelines

Design processing systems that produce consistent results regardless
of retries or partial failures. Incorporate unique identifiers,
transaction logs, and state tracking to verify that retries don't
duplicate or corrupt data. In research and clinical analysis,
reproducibility of results under repeated execution is a cornerstone
of scientific and regulatory assurance.

**Desired outcome:** Processing
pipelines can be retried without causing duplication or corruption,
maintaining reproducibility of results under repeated execution.

**Common anti-patterns:**

- Designing pipelines that overwrite intermediate results without
safeguards.
- Using non-unique identifiers for jobs, leading to duplication of
processed data.
- Failing to persist state, making retries non-deterministic.

**Benefits of establishing this best
practice:**

- Maintains scientific reproducibility by producing consistent
outputs from the same inputs.
- Reduces wasted compute cycles by allowing safe retries after
transient errors.
- Increases confidence in regulatory submissions where
reproducibility is scrutinized.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Idempotency should be a foundational principle in workflow design.
Each job execution must generate unique identifiers tied to input
datasets and persist transaction logs or checkpoints. State
tracking should record which inputs have been successfully
processed, enabling retries without duplication. For long-running
genomic analysis, idempotency verifies that a failed job can be
retried without corrupting downstream results.

### Implementation steps

- Processing pipelines should use AWS Step Functions or AWS Batch to track execution state and verify that retries are
idempotent.
- Use Amazon DynamoDB or Amazon RDS to persist transaction
logs and job state.
- Store intermediate artifacts in Amazon S3 with unique
identifiers as S3 prefixes (for example, prefixing with
dataset UUIDs) to maintain reproducibility.
- Implement retry policies with exponential backoff in AWS Step Functions, so transient failures don't result in
duplicate or corrupted processing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp02.html*

---

# LSREL07-BP03 Use staged validation and data quarantine mechanisms

Introduce controlled validation stages where data is quarantined
before being processed further. Apply automated rules for schema
conformity, metadata completeness, and domain-specific plausibility
(for example, genomic variants outside biological ranges). Only data
that passes validation and adherence data standards (such as CDISC
or FHIR) proceeds. Isolate data that fails for human review, with
full audit trails to support regulatory adherence.

**Desired outcome:** Only data that
meets predefined quality and plausibility criteria enters production
pipelines, while problematic data is isolated for review.

**Common anti-patterns:**

- Directly processing incoming data without validation.
- Overlooking schema, metadata, or biological plausibility checks.
- Mixing invalid data with production datasets, causing downstream
corruption.

**Benefits of establishing this best
practice:**

- Stops invalid datasets from contaminating results.
- Accelerates regulatory reviews by providing traceable validation
evidence.
- Improves scientific trust by verifying that only high-quality
data enters analysis.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data pipelines should incorporate a quarantine stage where
incoming data is validated before processing. Automated rules must
check for schema adherence, metadata completeness, and
instrument-specific error patterns. Apply domain-specific rules,
such as filtering out biologically implausible values in clinical
data. Flag and isolate quarantined data, with human review
workflows for resolution.

### Implementation steps

- Ingest new datasets into a quarantine Amazon S3 bucket with
tagging enabled to indicate that data is pending validation.
- Use AWS Glue or AWS Lambda to validate schema, metadata, and
plausibility.
- Store failed validation results in Amazon DynamoDB or
OpenSearch for investigation, and configure notifications
through Amazon SNS to alert data stewards.
- Only validated data should be transitioned into production
pipelines using S3 lifecycle policies or Step Functions
orchestration.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp03.html*

---

# LSREL07-BP04 Track data lineage with lifecycle metadata

Assign metadata tags (for example, raw,
filtered, processed, and
analyzed) at each lifecycle stage, so data state
is visible. This enables reproducibility, auditing, and debugging
when results need to be traced back to raw inputs. Use catalogs and
governance tools to track lineage across storage and processing
layers.

**Desired outcome:** Data state is
transparent across ingestion, processing, and analysis, with lineage
records supporting reproducibility and audits.

**Common anti-patterns:**

- Failing to label datasets by processing stage.
- Storing derived data without linkage to raw inputs.
- Using inconsistent or unstructured metadata practices.

**Benefits of establishing this best
practice:**

- Enables reproducibility by tracing results back to raw data.
- Simplifies compliance-related audits by showing how data was
transformed.
- Reduces troubleshooting time by quickly identifying the source
of anomalies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Every dataset should be tagged with lifecycle metadata reflecting
its stage: raw, filtered,
processed, or analyzed.
Lineage metadata should include transformation steps, software
versions, and parameter settings. These lineage records must be
centralized in a catalog or metadata repository to provide
transparency across the workload.

### Implementation steps

- Store datasets in Amazon S3 with metadata tags to reflect
their lifecycle stage.
- Use AWS AWS Glue Data Catalog to maintain a centralized record
of lineage and transformations.
- Capture transformation metadata during pipeline execution
using AWS Step Functions or AWS Lambda and store results in
Amazon DynamoDB or Amazon OpenSearch Service.
- Include metadata in evidence packages for GxP-regulated
workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp04.html*

---
