# Systems Performance — PMC register budget and cross-vendor portability (6.4.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — PMC tail: **finite counter registers per thread/core**, counter width, pointer back to Chapter 4 vendor/architectural sets (Table 6.5 omitted as vendor event catalog)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Hardware multiplexing ceiling**: only **a handful** of counters are physically present—wide investigations require **rotating event groups** or accepting blind spots ([[counters-statistics-metrics]], [[instrumentation-overhead-and-perturbation]]).
- (abstraction) **Counter width matters for long runs** (wrap / sampling error)—treat read discipline as part of **measurement validity**, not housekeeping ([[measurement-validity]]).
- (measurement) **Vendor families diverge**—portable practice is to anchor on **documented architectural subsets** and cross-check with **independent instruments** when SKU changes ([[scientific-method]], [[counters-statistics-metrics]]).

## Application validation

- **24h production profile**: if counters rotate every minute, **tail events** can be statistically invisible—budget **fixed counters** to SLO-critical ratios.

## Decision clarity

- **Decision**: choose **fewer, stable architectural counters** over **maximal event fan-out** when evidence must survive **SKU upgrades and fleet heterogeneity**.

## Concepts reused / refined / created

- Reused (structure): [[counters-statistics-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[scientific-method]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[measurement-validity]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[scientific-method]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-pmc-hardware-counter-programming-model-6-4-1]]
  - [[systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1]]
  - [[systems-performance-pmc-fundamentals-4-3-9]]
