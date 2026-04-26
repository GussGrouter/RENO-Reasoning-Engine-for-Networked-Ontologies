# Systems Performance — scientific method (2.5.6) (PDF pages 82–92)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.6 Scientific Method (hypothesis-driven tests; observational vs experimental)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-scientific-method-2-5-6.md`
- Chunks:
  - `processed/code/systems-performance-scientific-method-2-5-6-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) The scientific method frames performance work as hypothesis-driven investigation: question → hypothesis → prediction → test → analysis.
- (diagnosis) Tests can be observational (measure and rule in/out components) or experimental (change a factor and measure impact); reverse experimental changes when they fail to avoid compounding factors.
- (diagnosis) Negative tests (deliberately worsening performance) can be used to learn system behavior and guide drill-down.

## Concepts reused / refined / created

- Created (abstraction): [[scientific-method]]
- Reused (measurement): [[observability-vs-experimentation]] (observational vs experimental tests).
- Reused (diagnosis): [[cross-component-interactions]] (avoid changing multiple factors at once; reverse failed changes).
- Reused (mechanism): [[caching]] (cache-size examples motivate observational vs experimental testing).

## Links

- Concepts:
  - [[scientific-method]]
  - [[observability-vs-experimentation]]
  - [[cross-component-interactions]]
  - [[caching]]

