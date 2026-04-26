# Systems Performance — Ch.10 §10.3.1 Networks and routing (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **999–1036**; file rebuilt 2026-04-20)
- Scope: topology and shared components as performance constraints

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-networks-and-routing-10-3-1.md`

## Extracted ideas

- Treat the path as **shared infrastructure**; contention can appear outside the app and still dominate latency ([[cross-component-interactions]]).
- Routing introduces a natural **queueing** story (shared routers/links); backlog can propagate delay across unrelated flows ([[queueing-theory]]).

## Application validation

If one service-to-service call degrades only during another team’s bulk transfer window, suspect **shared path contention** before changing application code.

## Decision clarity

**Decision:** choose **path/contestion hypotheses** over “optimize endpoint CPU” when multiple flows share routers/links and degradation correlates with other traffic ([[queueing-theory]], [[cross-component-interactions]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]

