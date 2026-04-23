# Incremental computation

- Tag: mechanism

## Definition

**Incremental computation** updates a result using the previous result plus a small delta, instead of recomputing from scratch.

## Scope note

This is useful when inputs evolve gradually and full recomputation is expensive.

## Relation

- A way to “exploit state” to gain speed; can trade complexity/state maintenance for lower per-update cost.
- Often pairs with [[shift-computation-in-time]] when updates can be amortized or deferred.

## Links

- Source: [[network-algorithmics-3-3-3-speeding-up-routines]]
- Related concepts:
  - [[shift-computation-in-time]]

