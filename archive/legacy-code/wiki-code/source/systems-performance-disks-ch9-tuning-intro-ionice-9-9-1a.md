# Systems Performance — Ch.9 §9.9 Tuning (intro + §9.9.1 ionice)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.9** framing + **`ionice`** subsection opening

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-tuning-intro-ionice-9-9-1a.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Storage tuning** completes **§9.5 methodology** loops—prefer **proving unnecessary work removed** before ** sysctl surgery** ([[model-classify-intervene]], [[static-performance-tuning]]).
- **`ionice RT` vs neighbors:** disk **priority starvation** is a **cross-tier fairness** failure mode — parallel to CPU RT hazards ([[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **`ionice idle`** over **RT disk class** for **offline backups** when **latency-sensitive OLTP shares the same spindles/array**.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[model-classify-intervene]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[model-classify-intervene]], [[cross-component-interactions]], [[systems-performance]]
