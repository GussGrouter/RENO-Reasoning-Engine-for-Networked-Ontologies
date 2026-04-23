# Amdahl's law of scalability

- Tag: abstraction

## Definition

**Amdahl's law of scalability** models relative capacity \(C(N)\) when scaling a system by \(N\), accounting for serial components that cannot be parallelized:

\[
C(N) = \\frac{N}{1 + \\alpha (N - 1)}
\]

where \(\\alpha\) (0..1) captures the degree of seriality (contention for a serial component).

## Relation

- Role: framework (a simple scalability model for contention/serial work).
- Used with measured scaling data (often from [[micro-benchmarking]]) to estimate \(\\alpha\) and compare model vs reality.
- Supports [[model-classify-intervene]] by classifying “non-scaling” behavior as serial/contended work before interventions.

## Links

- Source: [[systems-performance-amdahls-law-of-scalability-2-6-3]]
- Source: [[systems-performance-algorithm-complexity-scaling-5-1-4]]
- Related concepts:
  - [[micro-benchmarking]]
  - [[scalability-knee-point]]
  - [[model-classify-intervene]]

