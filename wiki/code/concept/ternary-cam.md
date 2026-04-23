# Ternary CAM

- Tag: structure

## Definition

A **ternary content-addressable memory (ternary CAM)** stores patterns over \(\{0,1,*\}\) and, given a key, returns a matching entry by comparing against many stored patterns in parallel.

## Scope note

This is a hardware lookup structure; it is useful when the matching relation is “pattern with wildcards matches key” and lookup latency must be very low.

## Relation

- Can implement routing/forwarding lookups that require [[longest-prefix-match]] when entries are ordered to prefer more specific matches.
- Fits into [[network-algorithmics]] as an example of mapping an algorithmic rule to a hardware primitive with distinct update costs.

## Links

- Source: [[network-algorithmics-3-1-ternary-cam-update]]
- Related concepts:
  - [[longest-prefix-match]]
  - [[network-algorithmics]]

