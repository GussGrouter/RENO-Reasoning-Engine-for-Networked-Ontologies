# Systems Performance — User allocator selection (§7.6.3) (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.6.3** — **LD_PRELOAD** / runtime **allocator substitution** pattern

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-tuning-allocators-7-6-3.md`
- Chunks: `processed/code/systems-performance-memory-tuning-allocators-7-6-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Allocator “upgrades” need production-shaped contention + fragmentation**—**micro-bench ranking inverts** under real parallelism ([[micro-benchmarking]], [[measurement-validity]]).
- (scope) **LD_PRELOAD changes global libc behavior for the process**—validate **compatibility** (JIT, profiler hooks, `jemalloc`/`tcmalloc` assumptions) ([[cross-component-interactions]]).

## Application validation

- **Swap `malloc` at startup script:** enforce **canary workload** + **OOM guardrails**—wrong allocator can **inflate RSS** or **fragment** worse than glibc for your allocation pattern.

## Decision clarity

- **Decision:** choose **controlled A/B on representative prod drivers** over **developer laptop malloc benchmarks** when **allocator choice is justified by tail latency under parallel load**, not peak throughput alone.

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- Related sources: [[systems-performance-memory-tuning-numa-bind-7-6-4]]
