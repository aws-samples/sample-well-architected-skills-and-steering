---
name: ai-wafr
description: Run a Well-Architected review through the AI-WAFR kernel — a deterministic, offline binary that records an evidence ledger, verifies findings against a pinned framework contract, keeps agent proposals separate from human decisions, and produces a hash-chained, verifiable review bundle plus an explorable localhost report. The evidence-verified counterpart to aws-well-architected-framework-review.
not_for: a fast prompt-only review with no binary (use aws-well-architected-framework-review), learning WA concepts or diagrams (use wa-builder), migration readiness (use migration-readiness), enforcement controls (use wa-guardrails)
version: 0.1.0
tags: [skill, well-architected, review, evidence, verification, kernel]
---

# AI-WAFR — kernel-backed Well-Architected review

This skill does **not** perform the review in the prompt. It drives the **AI-WAFR reference
protocol kernel** — a small, offline binary that owns the review state machine, an evidence
ledger, a pinned framework contract, and artifact verification. Your job is to facilitate and
gather evidence; the kernel holds deterministic state and provenance; the **human owns every
decision**. The result is a verifiable review bundle in which each claim traces to a quoted
source or a named human's attestation.

> Use this skill when the review must be **evidence-backed, auditable, or governance-grade**.
> For a fast, prompt-only read, use `aws-well-architected-framework-review` instead — the two
> are complementary, and you can run both and compare.

## Step 1: Ensure the kernel is present

Check for the binary:

```bash
command -v ai-wafr && ai-wafr --version
```

If it is missing, install it — and **never run an unverified binary**:

- **Today (build from source):** clone the AI-WAFR package, `cargo build --release`, and put the
  resulting `ai-wafr` on `PATH` (e.g. copy `target/release/ai-wafr` to `~/.local/bin`).
- **Once signed releases are published:** download the artifact for your OS/architecture and
  verify it against the published `SHA256SUMS` before putting it on `PATH`.

The kernel needs no AWS account, no network, and no model SDK to run.

## Step 2: Hand off to the kernel — do not improvise the review

```bash
ai-wafr bootstrap --workspace .        # add --json if your host prefers a structured handshake
```

`bootstrap` returns a **pinned operating procedure**: the framework identity and pack digest,
the mandatory rules, the exact next commands, and the first question to ask the user. **Follow
it verbatim.** This skill deliberately carries no risk logic and no framework rules of its own —
every rule comes from the kernel's bootstrap output, so the review is identical in every host.

> The bundled pack is reference-derived from the public AWS Well-Architected Framework and is
> `unverified`. You MUST NOT describe any result as an HRI or MRI — the kernel enforces this.

## Step 3: Facilitate; never decide

Drive the state machine the bootstrap names. A typical flow:

1. Confirm the **workload name and repository scope** with the human, then `ai-wafr start`.
2. Gather evidence:
   - `ai-wafr scan` — the offline, deterministic detector pass (repository-observable practices).
   - `ai-wafr register-source` / `add-evidence` / `import-evidence` — documents and facts, each
     recorded with an **exact locator and verbatim quote**.
3. `ai-wafr propose` — record your feedback as **non-authoritative** candidate input. It never
   becomes workload truth.
4. The human reviewer records an **independent** `ai-wafr evaluate` *before* your proposal is
   revealed, then explicitly keeps or revises it.
5. `ai-wafr adjudicate` / `assess` — the human-owned canonical decision.

Rules the kernel will hold you to: record facts with exact locators; use `unknown` when evidence
is absent, inaccessible, stale, or out of scope; **never** turn a missing file into
`not_implemented`; keep agent feedback out of the canonical decision.

## Step 4: Verify before presenting

```bash
ai-wafr verify --review-dir <review-dir>
```

This recomputes the policy outcomes, the hash-chained event log, and artifact integrity. Present
results only after it passes. Optionally, verify persisted event signatures against a receiver
keyring: `ai-wafr verify --review-dir <dir> --trust-root <keyring.json>`.

## Step 5: Open the reviewer workspace

```bash
ai-wafr serve --review-dir <review-dir>
```

A loopback-only, explorable report and control pane — the human's surface for exploring evidence,
recording evaluations, and adjudicating. This is the primary experience; the CLI is the protocol
underneath it.

## Why this and not `aws-well-architected-framework-review`?

| | `aws-well-architected-framework-review` (prompt-layer) | `ai-wafr` (kernel-backed) |
|---|---|---|
| Findings | Produced by the model, directly and fast | Recorded in an evidence ledger, verified against a pinned contract |
| Agent opinion | Is the review | Kept structurally separate from the human's decision |
| Output | A report | A hash-chained, re-verifiable bundle + explorable workspace |
| Best when | You want a fast read | The review must be auditable or governance-grade |
| Needs | Just the agent | The `ai-wafr` binary (offline) |
