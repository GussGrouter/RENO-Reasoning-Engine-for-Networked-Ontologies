# Monotone bucket queue

- Tag: structure

## Definition

A **monotone bucket queue** maintains items in buckets keyed by nondecreasing integer priorities, allowing `extract-min` by advancing a cursor forward through buckets without ever moving backward.

## Scope note

This structure is useful when priorities are small integers and the algorithm guarantees a monotonicity property (the next minimum is never below the current cursor).

## Relation

- Used to speed up shortest-path computations with bounded integer edge weights (e.g., Dial’s algorithm for Dijkstra variants).
- A “finite universe” technique aligned with integer/bucket methods (see the P14 theme in [[network-algorithmics-3-3-3-speeding-up-routines]]).

## Links

- Source: [[network-algorithmics-4-3-dijkstra-route-computation]]
- Related concepts:
  - [[network-algorithmics]]

