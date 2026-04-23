# Systems Performance — Ch.10 §10.7 Experimentation intro (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: when to **inject traffic** to falsify “is the network path the limiter?”

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-intro-probes-vs-observability-10-7.md`

## Extracted ideas

- Experiments answer **end-to-end capacity / reachability** questions that passive counters may leave ambiguous—especially “is the problem **between** these two hosts?” ([[observability-vs-experimentation]], [[micro-benchmarking]] as a controlled probe mindset).
- Probes still obey **queueing**: injected ICMP/TCP test packets compete in the same queues as production—interpret delays/drops as **shared-path consequences** unless isolated ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **controlled cross-host probes** over **deeper app profiling** when the open question is whether **baseline path health / throughput** can explain the symptom ([[observability-vs-experimentation]]).

## Application validation

- **“Only bad from AZ-B to AZ-C”:** run a small matrix of probes/microbench between AZ pairs before rewriting service code ([[cross-component-interactions]]).

## Concepts reused / refined / created

- Reused: [[observability-vs-experimentation]], [[micro-benchmarking]], [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[observability-vs-experimentation]], [[micro-benchmarking]], [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
