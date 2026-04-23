# Random change anti-method

- Tag: heuristic

## Definition

The **random change anti-method** tries to improve performance by guessing a change, applying it, and checking whether a chosen metric improves—repeating until performance “gets better.”

## Failure mode

It is time-consuming and can leave behind changes that are not understood, are fragile, or later become unnecessary as the environment changes.

## Relation

- Over-emphasizes experimentation without sufficient diagnosis (see [[observability-vs-experimentation]]).
- Risks interacting changes and unclear causality (see [[cross-component-interactions]]).
- Can be a way of working around bottlenecks without identifying whether the limit is resource- or implementation-driven (see [[resource-vs-implementation-bottleneck]]).

## Links

- Source: [[systems-performance-random-change-anti-method-2-5-2]]
- Related concepts:
  - [[observability-vs-experimentation]]
  - [[cross-component-interactions]]
  - [[resource-vs-implementation-bottleneck]]

