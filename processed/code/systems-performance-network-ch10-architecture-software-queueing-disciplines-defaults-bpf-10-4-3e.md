# Systems Performance — Ch.10 §10.4.3 Software (queueing disciplines: defaults + bufferbloat trade)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Linux has an optional **qdisc layer** for traffic scheduling/shaping/filtering (tc).
- Most of the section is a catalog; the decision-relevant point is that defaults differ:
  - kernel default: **pfifo_fast**
  - systemd may set: **fq_codel** to reduce bufferbloat (with slightly higher complexity)
- BPF can attach at ingress/egress for classification/actions, expanding what can be done at this layer.

