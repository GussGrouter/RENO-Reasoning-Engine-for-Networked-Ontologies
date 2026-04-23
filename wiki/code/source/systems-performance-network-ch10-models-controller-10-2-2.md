# Systems Performance — Ch.10 §10.2.2 Controller (NIC) (model) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **939–956**; file rebuilt 2026-04-20)
- Scope: controller as a distinct resource boundary

## Processed artifacts

- `processed/code/systems-performance-network-ch10-models-controller-10-2-2.md`

## Extracted ideas

- Separate “network is slow” into **port/link constraints** vs **controller constraints**; controllers do work and can bottleneck under high packet rates ([[resource-vs-implementation-bottleneck]], [[utilization-and-saturation]]).

## Decision clarity

**Decision:** choose **controller-focused investigation** over “blame the network path” when **host-side utilization/saturation** indicates the endpoint is the limiting resource ([[use-method]], [[utilization-and-saturation]]).

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[use-method]], [[utilization-and-saturation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[use-method]], [[utilization-and-saturation]], [[systems-performance]]

