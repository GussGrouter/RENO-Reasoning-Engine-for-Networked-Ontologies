# Systems Performance — Ch.9 §9.5.5 Latency analysis (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.5.5** stack correlation + layer inflation

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-latency-analysis-9-5-5.md`

## Extracted ideas

- **Correlate latency by layer** before blaming disks; **FS metadata/locks** can dominate while **block stack looks idle** ([[latency-analysis]], [[throughput-latency-metrics]]).

## Decision clarity

**Decision:** choose **FS+VFS+block timestamps on the same requests** over **disk-only biolatency** when **app wait >> disk completion** for outliers.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[drill-down-analysis]], [[throughput-latency-metrics]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[drill-down-analysis]], [[throughput-latency-metrics]], [[measurement-validity]], [[systems-performance]]
