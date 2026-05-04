# Systems Performance — Ch.9 §9.5.7–§9.5.9 Cache, controls, micro-benchmark (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.5.7–§9.5.9**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-cache-resource-microbench-9-5-7-9.md`

## Extracted ideas

- **Cache tuning** spans **stack**; **I/O caps** masquerade as hardware; **raw microbench** needs **honest axes** and **skepticism of sector-0 shortcuts** ([[cache-tuning]], [[caching]], [[micro-benchmarking]], [[measurement-validity]]).

## Decision clarity

**Decision:** choose **multi-offset + block-device path microbench** over **single-offset hero numbers** when **procurement** must predict **random read tails**.

## Concepts reused / refined / created

- Reused: [[cache-tuning]], [[caching]], [[micro-benchmarking]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cache-tuning]], [[caching]], [[micro-benchmarking]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
