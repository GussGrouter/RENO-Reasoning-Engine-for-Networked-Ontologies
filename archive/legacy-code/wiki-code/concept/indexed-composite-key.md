# Indexed composite key

- Tag: structure

## Definition

An **indexed composite key** represents a pair (or tuple) key by first mapping each component to a compact index, then using the composed indices as the lookup key for associated state.

## Scope note

This avoids dense \(N \times M\) tables when only a sparse set of pairs is active, while still enabling fast lookup.

## Relation

- A way to reuse existing single-key lookup machinery to implement multi-key lookup.
- An instance of exploiting a finite universe of indices for fast lookup (related to the “finite universe” theme in [[network-algorithmics-3-3-3-speeding-up-routines]]).

## Links

- Source: [[network-algorithmics-4-4-ethernet-monitor-bridge-hardware]]
- Related concepts:
  - [[network-algorithmics]]
