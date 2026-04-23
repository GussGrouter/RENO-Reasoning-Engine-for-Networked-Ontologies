# Deep modules

- Tag: structure

## Definition

A **deep module** provides powerful functionality behind a **simple interface**, hiding most internal complexity from users.

## Design model

- Benefit: the module’s functionality.
- Cost: the module’s interface complexity, i.e., the complexity it imposes on the rest of the system.
- Objective: maximize benefit while minimizing cost; larger interfaces are not automatically better.

## Relation

Deep modules are a concrete target for designing good **abstractions**: they achieve abstraction by hiding internal complexity behind an interface.

## Links

- Source: [[ousterhout-deep-modules-p38-42]]
- Related concepts:
  - [[abstraction-design-principles]]
  - [[function-decomposition-by-abstraction-level]]
- Related insights:
  - [[local-clarity-vs-interface-complexity]]
