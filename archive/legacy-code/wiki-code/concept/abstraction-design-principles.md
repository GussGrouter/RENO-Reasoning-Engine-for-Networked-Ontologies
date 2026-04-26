# Abstraction design principles

- Tag: heuristic

## Definition

An **abstraction** is a simplified view of an entity that omits **unimportant details**.

## Design rules

- Omitting unimportant details is beneficial: the more truly unimportant details are omitted, the simpler the abstraction becomes for its users.
- An abstraction can fail in two ways:
  - it includes details that are not really important, increasing cognitive load
  - it omits details that really are important, creating obscurity (a **false abstraction**)
- The key is to understand what is important, and minimize the amount of important information exposed in the abstraction.

## Relation

Abstraction quality constrains what other work can safely assume about an interface (e.g., which implementation details are intentionally hidden vs which are still required knowledge).

Deep modules are a concrete way to achieve high-quality abstractions by maximizing functionality behind a simple interface.

## Links

- Source: [[ousterhout-abstractions-p35-39]]
- Source: [[systems-performance-kernels-unix-3-3-1]]
- Source: [[systems-performance-compiled-languages-performance-5-3-1]]
- Related concepts:
  - [[deep-modules]]
  - [[function-decomposition-by-abstraction-level]]
- Related insights:
  - [[local-clarity-vs-interface-complexity]]

