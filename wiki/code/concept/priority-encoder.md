# Priority encoder

- Tag: mechanism

## Definition

A **priority encoder** selects the highest-priority active input from a set (e.g., the first set bit in a bitmap under a fixed priority order).

## Scope note

This shows up across hardware and software as a reusable mechanism: “pick the first eligible item” under a priority ordering.

## Relation

- Used to implement fast selection/scheduling decisions when eligibility is represented as a bitset.
- Related to [[network-algorithmics]] as an example of mapping a networking problem to a standard hardware function.

## Links

- Source:
  - [[network-algorithmics-2-2-1-combinatorial-logic]]
  - [[network-algorithmics-2-2-2-timing-and-power]]
- Related concepts:
  - [[network-algorithmics]]

