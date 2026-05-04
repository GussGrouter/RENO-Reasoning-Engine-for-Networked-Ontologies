# Systems Performance — tuning efforts (2.3.4) (PDF pages 64–71)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.4 Tuning Efforts (where to tune vs where to observe)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-tuning-efforts-2-3-4.md`
- Chunks:
  - `processed/code/systems-performance-tuning-efforts-2-3-4-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) The largest performance wins are often found closest to where work is performed (frequently application logic), but observation may be easiest and most informative at lower layers (OS-level signals).
- (diagnosis) Lower-layer tuning may yield smaller end-to-end wins because higher-layer work (“tax”) has already been paid.
- (measurement) OS-level observability can reveal application-level issues in some cases more easily than application-only observability.

## Concepts reused / refined / created

- Reused (diagnosis): [[cross-component-interactions]] (layering effects: local changes do not map linearly to end-to-end wins).
- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (distinguishing “too much load” vs inefficient work at a layer).

## Links

- Concepts:
  - [[systems-performance]]
  - [[cross-component-interactions]]
  - [[resource-vs-implementation-bottleneck]]

