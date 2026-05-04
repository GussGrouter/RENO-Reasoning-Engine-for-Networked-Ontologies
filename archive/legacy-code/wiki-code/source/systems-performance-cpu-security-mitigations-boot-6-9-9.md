# Systems Performance — CPU security mitigations vs performance (6.9.9) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.9.9** — optional **kernel boot mitigations** (Spectre/Meltdown class) that trade **security for throughput/latency**

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-security-mitigations-boot-6-9-9.md`
- Chunks:
  - `processed/code/systems-performance-cpu-security-mitigations-boot-6-9-9-chunk-000001.md`

## Extracted ideas (with classification)

- (decision) **Mitigation toggles are a product/architecture boundary**, not a tuning knob—default is “keep mitigations on”; any exception needs an explicit **threat model** owner, not perf alone ([[scientific-method]], [[measurement-validity]]).
- (measurement) **Cross-environment CPU regressions** after kernel upgrades often mix **real workload change** with **mitigation defaults**—treat “before/after” as a **scope/semantics** problem before optimizing code ([[measurement-validity]], [[static-performance-tuning]]).
- (measurement) **Perturbation class reminder**: turning mitigations off in a lab changes **more than MHz**—it changes **exploitability assumptions**, so lab numbers are not a representation of production safety or even production time ([[measurement-validity]]).

## Application validation

- **Fleet-wide kernel bump looks “CPU heavier”**: first classify whether **mitigation set / boot cmdline** matches between baseline and candidate; only then profile for **application hot spots**.

## Decision clarity

- **Decision**: choose **documented security posture + apples-to-apples kernel configs** over **mitigation-off micro-benchmark wins** when the decision affects **production exposure** or **cross-team performance contracts**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[scientific-method]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[scientific-method]]
  - [[static-performance-tuning]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-kpti-meltdown-3-4-3]]
  - [[systems-performance-cpu-tuning-governors-affinity-cgroups-6-9-4-8]]
