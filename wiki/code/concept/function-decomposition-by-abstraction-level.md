# Function decomposition by abstraction level

- Tag: heuristic

## Definition

A function “does one thing” when its steps are **one level of abstraction below** the function’s stated name, and the function avoids mixing multiple abstraction levels.

## Design rules

- Prefer small functions to keep intent readable and enable descriptive naming.
- Avoid deep nesting and multi-level abstraction mixing inside a single function.
- A practical test for “more than one thing”: you can extract a helper whose name is not merely a restatement of the implementation.

## Relation

- Complements [[abstraction-design-principles]] by applying abstraction boundaries at the function level.
- Can be in tension with [[deep-modules]] if “small” is applied at module boundaries in a way that increases interface surface area.

## Links

- Source: [[clean-code-small-functions-do-one-thing]]
- Related concepts:
  - [[abstraction-design-principles]]
  - [[deep-modules]]
- Related insights:
  - [[local-clarity-vs-interface-complexity]]

