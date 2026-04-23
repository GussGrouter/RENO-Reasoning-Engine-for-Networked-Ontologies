# Protocol state machine model

- Tag: abstraction

## Definition

A protocol can be modeled as **a state machine per participating node**, plus **interfaces** and **message formats**, where transitions are driven by:

- interface calls
- received messages
- timer events

## Scope note

This model is useful for reasoning about **protocol implementations** and the recurring work they perform (e.g., per-message/packet processing and state management).

Observability signals (counters/events) provide the measurements needed to map observed timings and state-related work onto this model.

## Relation

An example of an “implementation model” used in [[network-algorithmics]] to make performance-relevant work explicit.

## Links

- Source: [[network-algorithmics-abstract-protocol-model-p45-47]]
- Related concepts:
  - [[network-algorithmics]]
- Related insights:
  - [[model-classify-intervene]]

