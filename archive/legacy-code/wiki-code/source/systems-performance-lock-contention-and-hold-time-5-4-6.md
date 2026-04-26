# Systems Performance — lock contention vs hold time (5.4.6) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.6 Lock Analysis (contention vs excessive hold time framing; excludes vendor tool catalog)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-lock-contention-and-hold-time-5-4-6.md`
- Chunks:
  - `processed/code/systems-performance-lock-contention-and-hold-time-5-4-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Contention** answers “is parallelism being lost *now*?”; **hold time** answers “will critical sections become serialization points *as load grows*?”—different interventions and owners ([[resource-vs-implementation-bottleneck]]).
- (measurement) **Spin lock** contention often appears in **CPU profiles**; **adaptive mutex** paths may split between brief spinning and sleeping—CPU sampling alone can understate blocked time ([[sampling-based-profiling]], [[drill-down-analysis]]).

## Application validation

- **Moderate CPU but growing p99 under concurrency**: profile hot locks, then check whether holders routinely block on I/O or nested locks—shortening the critical section may beat switching to a “fancier” mutex.

## Decision clarity

- **Decision**: choose **shortening critical sections / reducing nested blocking** over **tuning lock implementation constants** when hold-time growth explains future contention under parallel load.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[sampling-based-profiling]]
  - [[drill-down-analysis]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
  - [[systems-performance-static-performance-tuning-application-checklist-5-4-7]]
