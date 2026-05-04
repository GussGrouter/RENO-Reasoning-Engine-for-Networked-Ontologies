---
id: performance-anti-methods
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Performance anti-methods"
---

# Performance anti-methods

## Definition

A bundle of three named patterns that produce *plausible-looking* performance work without producing *valid* performance answers. They are warnings, not techniques:

- **Streetlight method** — investigate only with familiar tools, on the parts of the system those tools illuminate. The bug is wherever the light is, regardless of where it actually is.
- **Random-change method** — change a setting, measure, change another, measure, repeat — without a hypothesis. The loop terminates when something looks better, not when something is *understood*; later regressions are unsurprising.
- **Blame-someone-else method** — pre-commit to a hypothesis (it's the network, it's DNS, it's the database) and ship the ticket without data. Recognise by absence of screenshots and absence of falsifiable predictions.

The **tools method** — start from a fixed tool checklist — is a related but milder failure: it is bounded by the tools' coverage and silently ignores unknown unknowns where no tool yet exists.

These patterns are reusable warnings for code review, incident triage, post-mortem audit, and self-check.

## Use when

- Reviewing an incident report or post-mortem — pattern-match against the three anti-methods before accepting the conclusion.
- Onboarding — explicitly call out which pattern a new responder is sliding into during their first incidents.
- Code or architecture review where a performance fix is proposed but the diagnostic chain is not shown — ask which method produced the fix.
- Negotiating with a team that "already investigated" — request the data that would falsify their hypothesis. The absence of such data is the streetlight or blame pattern in disguise.
- Self-check during your own debugging sessions, especially under time pressure.

## Do not use when

- The incident is over and a clearly correct change is queued — anti-method labelling slows recovery without changing the fix; defer the methodological lesson to post-mortem.
- The change is provably correct on its own merits and the methodology is irrelevant — do not litigate process when the artefact stands.
- For trivial changes (typo, missing semicolon) — there is no methodology to evaluate.
- As a rhetorical weapon. The point is to redirect the investigation, not to score points; misuse turns the concept into a fourth anti-method.

## Related concepts

- [[problem-statement-first-response]] — the anti-methods are typically what a responder defaults to when no problem statement was written first.
- [[use-method]] — USE is structurally resistant to streetlight (resource-first, not tool-first); contrast.
- [[resource-analysis-vs-workload-analysis]] — blame-someone-else is often a refusal to switch lens.
- [[red-method-service-health]] — RED's per-service triplet bounds the streetlight pattern at service boundaries.
- [[scheduler-policy-shapes-latency]] — random-change of preemption modes or cgroup quotas, without a problem statement, is the canonical random-change pattern at the OS-policy layer.

## Source support

- [[systems-performance-ch2-methodologies-continuation-p76-90]] — § 2.5 introduces the streetlight, random-change, and blame-someone-else anti-methods alongside the tools method, and explicitly contrasts them with problem-statement-first hygiene.
