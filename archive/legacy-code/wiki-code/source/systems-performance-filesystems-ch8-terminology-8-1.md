# Systems Performance — Chapter 8 terminology placeholder (§8.1) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.1** — glossary-style entries (**omitted** in processed extract); cross-references retained

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-terminology-8-1.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-terminology-8-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Logical vs physical I/O** vocabulary sets up **measurement plane discipline**—avoid counting one while reasoning about the other ([[measurement-validity]]).

## Application validation

- **Incident doc cites “disk IOPS”:** verify whether the symptom came from **logical FS ops** or **background flush**—rename metrics to the **plane you measured**.

## Decision clarity

- **Decision:** choose **explicit logical vs physical wording in runbooks** over **generic “I/O”** when **multiple teams interpret the same dashboard differently**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-intro-outline-8]]
