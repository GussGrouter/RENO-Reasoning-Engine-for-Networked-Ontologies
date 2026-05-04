# Code theory — summary

Scope: programming, systems, architecture, cryptography, tooling.

## Entry point

This page is the domain-level overview. Write new material by promoting from:

`summary → concept → insight → source`

- Book spine (Network Algorithmics sources): [[network-algorithmics-toc]]

## Hierarchy (where to put pages)

- Concept pages (expected): `../concept/`
- Insight pages (expected): `../insight/`
- Source pages (expected): `../source/`

## Key concept areas (placeholders)

- Summaries (this domain):
  - [[systems-performance]]

- Concepts (this domain):
  - [[network-algorithmics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[protocol-state-machine-model]]
  - [[throughput-latency-metrics]]
  - [[counters-statistics-metrics]]
  - [[sampling-based-profiling]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[observability-vs-experimentation]]
  - [[utilization-and-saturation]]
  - [[scalability-knee-point]]
  - [[caching]]
  - [[known-unknowns-framework]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[streetlight-anti-method]]
  - [[random-change-anti-method]]
  - [[problem-statement-method]]
  - [[scientific-method]]
  - [[diagnosis-cycle]]
  - [[use-method]]
  - [[red-method]]
  - [[drill-down-analysis]]
  - [[latency-analysis]]
  - [[event-tracing]]
  - [[baseline-statistics]]
  - [[static-performance-tuning]]
  - [[cache-tuning]]
  - [[micro-benchmarking]]
  - [[performance-mantras]]
  - [[amdahls-law-of-scalability]]
  - [[universal-scalability-law]]
  - [[queueing-theory]]
  - [[resource-limits-method]]
  - [[factor-analysis-capacity-planning]]
  - [[quantifying-performance-gains]]
  - [[latency-percentiles]]
  - [[coefficient-of-variation]]
  - [[geometric-mean]]
  - [[harmonic-mean]]
  - [[multimodal-latency-distribution]]
  - [[latency-outliers]]
  - [[time-series-monitoring]]
  - [[workload-seasonality]]
- [[centralized-monitoring-architecture]]
- [[metric-visualization]]
- [[latency-heatmap]]
- [[timeline-waterfall-chart]]
- [[multivariate-metric-surface-plot]]
- [[extended-bpf]]
- [[kernel-architecture-models]]
- [[time-space-tradeoff]]
  - [[priority-encoder]]
  - [[memory-technology-tradeoff]]
  - [[longest-prefix-match]]
  - [[fast-path-slow-path]]
  - [[process-abstraction]]
  - [[context-switching]]
  - [[virtual-memory-abstraction]]
  - [[demand-paging]]
  - [[system-call]]
  - [[kernel-user-boundary]]
  - [[ternary-cam]]
  - [[exploit-degrees-of-freedom]]
  - [[bounded-recent-history-buffer]]
  - [[shift-computation-in-time]]
  - [[relax-system-requirements]]
  - [[performance-hints]]
  - [[optimize-expected-case]]
  - [[incremental-computation]]
  - [[cross-component-interactions]]
  - [[handle-as-index]]
  - [[eligibility-list]]
  - [[monotone-bucket-queue]]
  - [[indexed-composite-key]]
  - [[abstraction-design-principles]]
  - [[deep-modules]]
  - [[function-decomposition-by-abstraction-level]]

## Potential insights (placeholders)

- Insights (this domain):
  - [[model-classify-intervene]]
  - [[local-clarity-vs-interface-complexity]]

## Future sources (placeholders)

- Sources (this domain):
  - [[network-algorithmics-1-1-1-endnode-bottlenecks-endnodes-are-the-endpoints-of-the-network-they-inclu]]
  - [[network-algorithmics-1-1-2-router-bottlenecks-though-we-concentrate-on-internet-routers-almost-all]]
  - [[network-algorithmics-1-1-the-problem-network-bottlenecks]]
  - [[network-algorithmics-1-2-1-warm-up-example-scenting-an-evil-packet]]
  - [[network-algorithmics-1-2-2-strawman-solution-the-check-of-overall-length-is-straightforward-to-impl]]
  - [[network-algorithmics-1-2-3-thinking-algorithmically]]
  - [[network-algorithmics-1-2-4-refining-the-algorithm-exploiting-hardware]]
  - [[network-algorithmics-1-2-5-cleaning-up-we-have-postponed-one-thorny-issue-to-this-point-the-termina]]
  - [[network-algorithmics-1-2-6-characteristics-of-network-algorithmics]]
  - [[network-algorithmics-1-2-the-techniques-network-algorithmics]]
  - [[network-algorithmics-1-3-exercise-1-implementing-chi-square-the-chi-square-statistic-can-be-used]]
  - [[network-algorithmics-10-1-challenge-1-ethernet-under-fire]]
  - [[network-algorithmics-10-2-challenge-2-wire-speed-forwarding]]
  - [[network-algorithmics-10-3-2-using-hardware-parallelism]]
  - [[network-algorithmics-10-3-3-the-d-left-approach-now-we-introduce-d-left-the-state-of-art-solution-br]]
  - [[network-algorithmics-10-3-challenge-3-scaling-lookups-to-higher-speeds]]
  - [[network-algorithmics-10-4-summary-this-chapter-on-exact-match-lookups-is-written-as-a-story-the-st]]
  - [[network-algorithmics-10-5-exercise-1-arp-caches-another-example-of-an-exact-match-lookup-is-furnis]]
  - [[network-algorithmics-11-1-1-prefix-notation-internet-prefixes-are-defined-using-bits-and-not-alphanu]]
  - [[network-algorithmics-11-1-2-why-variable-length-prefixes]]
  - [[network-algorithmics-11-1-3-lookup-model-recall-the-router-model-of-chapter-2-a-packet-arrives-on-an]]
  - [[network-algorithmics-11-1-introduction-to-prefix-lookups]]
  - [[network-algorithmics-11-10-binary-search-on-ranges-with-initial-lookup-table]]
  - [[network-algorithmics-11-11-binary-search-on-prefix-lengths]]
  - [[network-algorithmics-11-12-1-using-bloom-filters-to-compress-prefix-bitmaps]]
  - [[network-algorithmics-11-12-2-sail-uncompressed-bitmaps-up-to-a-pivot-level]]
  - [[network-algorithmics-11-12-linear-search-on-prefix-lengths-with-hardware-assist]]
  - [[network-algorithmics-11-13-1-frame-based-compaction]]
  - [[network-algorithmics-11-13-memory-allocation-in-compressed-schemes]]
  - [[network-algorithmics-11-14-fixed-function-lookup-chip-models]]
  - (see full list in `wiki/meta/index.md` — 334 total Network Algorithmics source pages)

## Indexes

Use `../indexes/` only when you need domain-level cross-links (avoid early over-creation).

