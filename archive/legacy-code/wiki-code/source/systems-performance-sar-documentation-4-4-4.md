# Systems Performance — sar metric semantics / documentation (4.4.4) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.4.4 (man-page semantics, SNMP cross-names, pointers to later chapters)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-sar-documentation-4-4-4.md`
- Chunks:
  - `processed/code/systems-performance-sar-documentation-4-4-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Semantic mapping matters**: counters only become decisions after you know the *definition* (rate vs level, inclusion rules, error handling). SNMP names in brackets are hooks to **fleet-wide schema alignment**—the same abstract problem as correlating vendor metrics across services.
- (diagnosis) Primary documentation plus later chapter deep-dives are the antidote to **metric name intuition**—treating a label as obvious is a known failure mode tied to [[known-unknowns-framework]].

## Concepts reused / refined / created

- Reused (measurement): [[counters-statistics-metrics]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (measurement): [[baseline-statistics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[known-unknowns-framework]]
  - [[baseline-statistics]]
  - [[systems-performance]]
