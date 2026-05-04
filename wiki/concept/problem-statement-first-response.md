---
id: problem-statement-first-response
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Problem statement first response"
---

# Problem statement first response

## Definition

A short, structured opening to incident or performance triage that produces a *written problem statement* before any deeper instrumentation work. The statement answers a small set of discovery questions, typically:

1. What is the symptom, and how is it observed?
2. Has it changed — when did it start, and what changed near that time?
3. Who or what is affected, and what is the blast radius?
4. Is the symptom expressed as latency, throughput, errors, or saturation, and against what baseline?
5. Where in the stack does the symptom appear, and where does it explicitly not appear?
6. What is the environment — versions, topology, recent rollouts, neighbours?

The output is a single paragraph or short bullet list that anchors the rest of the investigation. Often the statement on its own resolves the question without needing further data; just as often it reveals that the original ticket was misframed.

## Use when

- An incident or performance ticket arrives with a vague description ("it's slow", "it's broken", "the cluster is bad").
- The fastest responder is about to log in and start running commands without a written hypothesis.
- Multiple team members are converging on the same incident and need a shared frame.
- A previous investigation stalled and you suspect the team has been answering the wrong question.
- You have remote-only or expensive access and want to bound the work before paying for the context switch.

## Do not use when

- The incident is already over and the data window is closing fast; capture raw evidence first, then write the problem statement against it.
- The system is on fire and revert is the obvious move; execute the rollback, then write the post-action statement.
- The investigation is open-ended performance work rather than incident-driven; a problem statement over-constrains exploratory benchmarking.
- You only have one of the six answers and no realistic way to get more; do not pretend the statement is complete — mark the gaps as known-unknowns.

## Related concepts

- [[use-method]] — typically runs *after* the problem statement, scoped by it.
- [[resource-analysis-vs-workload-analysis]] — the problem statement usually picks the lens.
- [[load-versus-architecture]] — the statement often resolves which class of ceiling is in play.
- [[performance-anti-methods]] — what you fall into when you skip the statement: streetlight, random-change, blame-someone-else.
- [[workload-characterization-input-model]] — supplies the data behind questions 3 and 4 (who is affected, what does the load look like).
- *scientific-method-and-diagnosis-cycle* (deferred) — extends problem-statement-first-response into a hypothesis-test loop.

## Source support

- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.5 introduces the problem-statement method and the discovery questions, and contrasts it with the streetlight, random-change, and blame-someone-else anti-methods.
