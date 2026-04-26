# Model → classify → intervene (for performance work)

## Synthesis

Combine:

- a **work model** (e.g., [[protocol-state-machine-model]]) to enumerate where time is spent and what events drive work,
- a **bottleneck classification** ([[resource-vs-implementation-bottleneck]]) to decide whether the constraint is resources or design,
- an **implementation method set** ([[network-algorithmics]]) when the bottleneck is implementation-driven.

Result: a stable workflow that reduces premature optimization and misapplied fixes.

## Why it matters

Naive performance work often fails because it:

- optimizes without a clear model of *what work exists* and *what triggers it*
- treats all slowdowns as the same kind of constraint
- jumps to a favorite technique instead of selecting an intervention that matches the constraint

## Failure modes

- **Model-free tuning**: changes knobs without identifying the dominant work path.
- **Measurement bias**: tool choice/overhead can distort which work path appears dominant, leading to the wrong model.
- **Wrong remedy**: adds resources when the bottleneck is design-driven, or rewrites design when resources are the hard limit.
- **Local-only focus**: optimizes a component that is not on the critical path.

## Boundary

This workflow may not apply (or may need extension) when:

- the bottleneck is not primarily performance (e.g., correctness, safety, compliance constraints dominate)
- constraints are externally fixed (e.g., hard protocol/ABI requirements) such that meaningful intervention is unavailable

## Links

- Concepts:
  - [[protocol-state-machine-model]]
  - [[resource-vs-implementation-bottleneck]]
  - [[network-algorithmics]]

