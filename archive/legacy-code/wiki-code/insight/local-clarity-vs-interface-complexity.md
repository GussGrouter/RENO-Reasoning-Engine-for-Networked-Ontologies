# Local clarity vs interface complexity

## Synthesis

Design has two coupled goals:

- **Local clarity**: keep implementation readable via decomposition (e.g., small functions; consistent abstraction level).
- **Interface simplicity**: keep the *public surface* small/simple so users don’t inherit internal complexity.

The tradeoff boundary: decomposition is beneficial when it **reduces cognitive load without increasing the interface that other modules must learn**.

## Boundary rule (practical)

- Prefer decomposition **inside** a module (private helpers) when it improves readability.
- Be cautious promoting decomposition to **new public interfaces**: it can convert hidden implementation complexity into system-wide interface complexity (shallower modules).

## Links

- Concepts:
  - [[abstraction-design-principles]]
  - [[deep-modules]]
  - [[function-decomposition-by-abstraction-level]]

