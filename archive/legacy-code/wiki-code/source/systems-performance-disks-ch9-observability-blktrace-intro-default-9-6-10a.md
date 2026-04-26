# Systems Performance — Ch.9 §9.6.10 blktrace (intro + default trace)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.10** (part **a** of **c**—pipeline + default output)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-blktrace-intro-default-9-6-10a.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **blktrace family** gives **fine-grained block narrative**—expect **many lines per I/O**; pair with **aggregation** (`btt`) or **filters** before drawing conclusions ([[event-tracing]], [[instrumentation-overhead-and-perturbation]] **perturbation**).

## Decision clarity

**Decision:** choose **filtered `btrace`** over **raw full trace** when you already know **which action letter** (e.g. issue-only) matches your hypothesis.

## Concepts reused / refined / created

- Reused: [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[systems-performance]]
