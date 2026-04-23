# Systems Performance — PMCs as programmable hardware counters (6.4.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — **Hardware Counters (PMCs)** through event-select / mask / ring / threshold semantics (vendor event tables treated as reference material, not concepts)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-pmc-hardware-counter-programming-model-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-pmc-hardware-counter-programming-model-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **PMCs are registers that count microarchitectural events**—they bridge “what happened on-chip” to **rates and ratios** (IPC, MPKI, stall classes) when you pick events that match your claim ([[counters-statistics-metrics]], [[measurement-validity]]).
- (mechanism) **Programming model is selective**: event **type + subtype mask + privilege ring + thresholding** determines what increments—misconfiguration yields **valid counts for the wrong question** ([[measurement-validity]]).
- (diagnosis) **Counters are SKU-specific**: the portable decision is to treat manuals as **capability contracts** and plan **fallback event sets** when portable profiling breaks ([[counters-statistics-metrics]], [[scientific-method]]).

## Application validation

- **“L2 misses look zero” on a new CPU**: verify **UMASK / architectural vs non-architectural** naming—then triangulate with **top-down** or **sampling** rather than trusting one counter.

## Decision clarity

- **Decision**: choose **multi-event ratio panels (IPC + memory + front-end)** over **single hot counter** when diagnosing **CPU stalls** under unclear microarchitecture.

## Concepts reused / refined / created

- Reused (structure): [[counters-statistics-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[scientific-method]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[measurement-validity]]
  - [[scientific-method]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-interconnect-scalability-memory-system-6-4-1]]
  - [[systems-performance-cpu-pmc-register-budget-and-sku-variance-6-4-1]]
  - [[systems-performance-pmc-fundamentals-4-3-9]]
