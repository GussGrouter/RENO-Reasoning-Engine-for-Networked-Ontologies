# Systems Performance — USE method applied to CPUs (6.5.2) (PDF 231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5.2** — CPU USE checklist (utilization semantics under quotas, saturation via run-queue / load, ECC/offline errors)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-use-method-cpu-checklist-6-5-2.md`
- Chunks:
  - `processed/code/systems-performance-cpu-use-method-cpu-checklist-6-5-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Errors first**: correctable error escalation can **offline CPUs**—treat “CPU missing” as a capacity event, not a scheduling mystery ([[use-method]], [[utilization-and-saturation]]).
- (measurement) **Utilization under quotas** must be read against **both** physical busy% and **limit consumption**—cloud saturation can appear as **throttling** while sockets look idle ([[use-method]], [[cross-component-interactions]]).
- (diagnosis) **Saturation signals** often arrive as **system-wide aggregates** (e.g., load averages)—pair with **per-CPU utilization** to separate **imbalance** from uniform overload ([[utilization-and-saturation]], [[measurement-validity]]).

## Application validation

- **K8s CPU throttling**: node `%idle` healthy but SLO bad → classify as **saturation vs limit** using **quota-shaped runnable delay**, not only host utilization.

## Decision clarity

- **Decision**: choose **quota headroom / burst allowance** over **node pool expansion** when **runnable delay** tracks **policy limits** before **physical utilization** saturates.

## Concepts reused / refined / created

- Reused (heuristic): [[use-method]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[use-method]]
  - [[utilization-and-saturation]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-methodology-cookbook-and-tools-method-6-5-intro-6-5-1]]
  - [[systems-performance-cpu-workload-characterization-6-5-3]]
