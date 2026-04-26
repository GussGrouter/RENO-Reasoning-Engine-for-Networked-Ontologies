# Systems Performance — Ch.10 §10.6.15 other tools — Table 10.7 (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3835–3838**; file rebuilt 2026-04-20)
- Scope: **navigation map**, not a new concept per row

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-other-tools-table-10-7-crossrefs-10-6-15a.md`

## Extracted ideas

- The table’s value is **coverage planning**: pick the smallest tool that answers the hypothesis (drops vs latency vs connect path vs qdisc) instead of defaulting to packet capture ([[streetlight-anti-method]], [[drill-down-analysis]]).
- Many entries are **BPF-specialized lenses** on the same recurring primitives: **socket queues**, **sk_buff lifetimes**, **device/qdisc latency**—symptoms like drops/retransmits remain **queueing consequences** until localized ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **a targeted BPF tool from the book’s map** over **Wireshark diving** when your question matches a single failure mode (e.g., **sk_buff drops with stacks**) ([[extended-bpf]]).

## Application validation

- **Intermittent drops:** prefer **skbdrop-style stack attribution** over hours of pcaps when you need “which kernel path dropped buffers” ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[streetlight-anti-method]], [[drill-down-analysis]], [[queueing-theory]], [[extended-bpf]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[streetlight-anti-method]], [[drill-down-analysis]], [[queueing-theory]], [[extended-bpf]], [[systems-performance]]
