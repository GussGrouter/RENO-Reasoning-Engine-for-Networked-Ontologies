# Systems Performance — CPU binding risks (5.2.7 tail) + performance mantras (5.2.8) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.7 (binding caveats) + Section 5.2.8 (pointer to Performance Mantras)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-binding-risks-and-performance-mantras-5-2-7-8.md`
- Chunks:
  - `processed/code/systems-performance-cpu-binding-risks-and-performance-mantras-5-2-7-8-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Hard CPU pins** can fight device IRQ affinity, other pins, or **unknown colocation**—on shared hosts, “I own these CPUs” assumptions create **scheduler hotspots** while siblings stay idle ([[known-unknowns-framework]] hazard).
- (abstraction) **Drift**: topology and tenancy change over years; stale pins can **hurt** locality (e.g., spanning sockets) once hardware maps move.
- (heuristic) **Mantras recap**: ordered intervention ladder (eliminate, repeat, reduce, defer, hide, parallelize, cheapen) anchors application tuning to the same prioritization as Chapter 2 ([[performance-mantras]]).

## Application validation

- **Shared fleet / containers**: if an app sets explicit CPU affinity without coordinating with the scheduler pool, validate under multi-tenant load that it is not colliding with other pinned workloads on the same physical cores.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (heuristic): [[performance-mantras]]
- Reused (abstraction): [[process-abstraction]]
- Reused (mechanism): [[context-switching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[known-unknowns-framework]]
  - [[throughput-latency-metrics]]
  - [[performance-mantras]]
  - [[process-abstraction]]
  - [[context-switching]]
  - [[systems-performance]]
