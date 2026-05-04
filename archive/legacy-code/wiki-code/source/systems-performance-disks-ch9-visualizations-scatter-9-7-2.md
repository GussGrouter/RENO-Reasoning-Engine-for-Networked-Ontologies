# Systems Performance — Ch.9 §9.7.2 Latency scatter plots

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.7.2**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-visualizations-scatter-9-7-2.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Scatter** makes **rare ms-scale** events **visible**; **story arc** example links **cached writes** → **later read stalls** (**[[cross-component-interactions]]**, **[[queueing-theory]]** intuition).

## Decision clarity

**Decision:** choose **event scatter** over **rolled-up line averages** when debugging **long-tail SLO breaches** that **vanish in hourly means**.

## Concepts reused / refined / created

- Reused: [[latency-outliers]], [[metric-visualization]], [[cross-component-interactions]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-outliers]], [[metric-visualization]], [[cross-component-interactions]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
