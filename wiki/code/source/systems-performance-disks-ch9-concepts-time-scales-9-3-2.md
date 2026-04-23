# Systems Performance — Ch.9 §9.3.2 Time scales + Table 9.1 (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.3.2** — orders of magnitude; **Table 9.1** summarized; enterprise vs cloud heuristics; **bimodal average** warning

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-concepts-time-scales-9-3-2.md`
- Chunks: `systems-performance-disks-ch9-concepts-time-scales-9-3-2-chunk-000001.md`

## Extracted ideas

- **Same device** returns **multiple latency populations** (cache hit vs miss)—**average** collapses modes (**multimodal** + **representation** validity).
- **Environment-specific** “bad I/O” thresholds—treat author’s ms cutoffs as **hypotheses**, not constants.

## Application validation

Dashboard **mean disk latency** flat while users feel stalls: inspect **histogram/heatmap**—means sit **between modes** or **hide tail**.

## Decision clarity

**Decision:** choose **distribution visualization** over **mean disk latency** when **service time histograms show separated peaks** (hit vs backend path).

## Concepts reused / refined / created

- Reused: [[multimodal-latency-distribution]], [[metric-visualization]], [[measurement-validity]], [[throughput-latency-metrics]], [[micro-benchmarking]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[multimodal-latency-distribution]], [[metric-visualization]], [[measurement-validity]], [[throughput-latency-metrics]], [[micro-benchmarking]], [[systems-performance]]
