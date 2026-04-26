# Systems Performance — XFS positioning (§8.4.5) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.5** — **XFS** (**feature bullet catalog omitted** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fs-types-xfs-8-4-5c.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fs-types-xfs-8-4-5c-chunk-000001.md`

## Extracted ideas (with classification)

- (evidence anecdote) **Same org, different FS roles** (example workload vs root): treats FS choice as **component-local default** validated by workload—not a universal ranking.

## Application validation

- Use **service-specific qualification** (benchmark/trace on *that* object mix and journal placement), not distro defaults alone, when copying “Netflix uses XFS for Cassandra”–style anecdotes.

## Concepts reused / refined / created

- Reused: [[resource-analysis-vs-workload-analysis]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[resource-analysis-vs-workload-analysis]], [[measurement-validity]], [[micro-benchmarking]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-types-ext-8-4-5b]], [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]]
