# Clean Code — small functions & “do one thing” (excerpt)

## Source

- Title: *Clean Code: A Handbook of Agile Software Craftsmanship* (Robert C. Martin)
- Raw: `raw/code/pdf/Clean Code.pdf`
- Batch scope: Chapter 3 excerpt covering “Small!” and “Do One Thing” (function size + decomposition by abstraction level)

## Processed artifacts

- Converted slice: `processed/code/clean-code-functions-small-do-one-thing.md`
- Chunks:
  - `processed/code/clean-code-functions-small-do-one-thing-chunk-000001.md`
  - `processed/code/clean-code-functions-small-do-one-thing-chunk-000002.md`

## Classified ideas (axis)

- Design/abstraction reasoning: function decomposition as a boundary between abstraction levels; “one thing” defined as steps one level below the function name.

## Comparison (no merging)

- Compared to [[abstraction-design-principles]]: emphasizes cognitive load reduction via decomposition and abstraction-level consistency inside functions.
- Compared to [[deep-modules]]: may create tension if “small” is treated as a universal rule at module boundaries; can be compatible when applied internally without expanding interfaces.

## Promoted concepts (from this batch)

- [[function-decomposition-by-abstraction-level]]
  - Evidence: “one thing” definition via one-level-below function name; warning about mixing abstraction levels; preference for small functions.

## Links

- Concepts:
  - [[function-decomposition-by-abstraction-level]]
- Related concepts:
  - [[abstraction-design-principles]]
  - [[deep-modules]]
- Related insights:
  - [[local-clarity-vs-interface-complexity]]

