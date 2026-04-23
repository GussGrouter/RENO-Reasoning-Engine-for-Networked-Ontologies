# Systems Performance — CPU workload characterization (6.5.3) (PDF 231–285 + 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5.3** — characterize **applied load** (averages, user/kernel mix, syscall and switch rates, interrupts) plus advanced checklist framing

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-workload-characterization-6-5-3.md` (spans **pdftotext** pages **231–285** and **286–320**; join marker in file)
- Chunks:
  - `processed/code/systems-performance-cpu-workload-characterization-6-5-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Workload characterization targets inputs**, not delivered latency—mixing the two without qualification creates **false tuning targets** ([[resource-analysis-vs-workload-analysis]], [[measurement-validity]]).
- (measurement) **Load-average semantics differ by OS**—the same number can mean **CPU-only demand** vs **mixed runnable pressure**; treat labels as **portability hazards** ([[measurement-validity]], [[counters-statistics-metrics]]).
- (diagnosis) **Rate metrics couple cause and effect** (e.g., faster CPUs finish sooner → **higher syscall/sec** for identical logical work)—interpret deltas only with a **fixed workload model** ([[scientific-method]], [[throughput-latency-metrics]]).

## Application validation

- **“Syscalls doubled” after hardware refresh**: check **wall time per unit of work** before blaming regressions—the rate can rise because **work completes faster**, not because the app became syscall-heavier.

## Decision clarity

- **Decision**: choose **normalize rates per business transaction** over **raw syscall/sec alerts** when comparing **different CPU speeds or container limits** on the same codebase.

## Concepts reused / refined / created

- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (abstraction): [[scientific-method]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[measurement-validity]]
  - [[counters-statistics-metrics]]
  - [[scientific-method]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-use-method-cpu-checklist-6-5-2]]
  - [[systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4]]
