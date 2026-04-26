# Factor analysis (capacity planning)

- Tag: heuristic

## Definition

**Factor analysis (capacity planning)** reduces the number of performance tests needed when many configuration factors exist by starting from a maximum configuration, varying factors one at a time, attributing performance drops and cost savings, then selecting a low-cost configuration that still meets requirements and retesting it.

## Relation

- Role: method (a decision procedure for selecting price/performance configurations under many knobs).
- Helps avoid combinatorial explosion and acknowledges interaction risk by requiring retest (see [[cross-component-interactions]]).
- Fits [[model-classify-intervene]] by turning “which factors matter?” into measured effect sizes before intervention selection.

## Links

- Source: [[systems-performance-factor-analysis-2-7-2]]
- Source: [[systems-performance-disks-ch9-architecture-hdd-throughput-9-4-1a]]
- Source: [[systems-performance-disks-ch9-methodology-scaling-9-5-10]]
- Related concepts:
  - [[cross-component-interactions]]
  - [[model-classify-intervene]]

