# Relax system requirements

- Tag: heuristic

## Definition

To **relax system requirements** is to weaken a subsystem’s specification (or correctness/precision/guarantee) to make an implementation feasible or faster, while compensating elsewhere in the system.

## Scope note

This includes trading certainty or accuracy for time, and shifting work to another component (“shift computation in space”).

## Relation

- Often a deliberate way to change where costs are paid in the system, relating to [[resource-vs-implementation-bottleneck]].
- Can pair naturally with [[shift-computation-in-time]] when strict requirements force expensive worst-case work.

## Links

- Source: [[network-algorithmics-3-3-1-systems-principles]]
- Related concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[shift-computation-in-time]]

