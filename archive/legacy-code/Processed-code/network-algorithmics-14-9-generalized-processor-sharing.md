# Network Algorithmics — 14.9 Generalized processor sharing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 428
- Slice: from `14.9 Generalized processor sharing` up to next detected section heading

---

14.9 Generalized processor sharing
The perfect service discipline to provide delay and fairness guarantees is GPS (Keshav et al., 1990;
Parekh and Gallager, 1993), which we earlier described as the “simulated bit-by-bit round-robin” al-
gorithm. In a GPS scheduler all backlogged flows are served simultaneously in a weighted fashion as
follows. In a link of rate r served by a GPS scheduler each flow Fi is assigned
                                                                               a weight φi . Each back-
logged flow Fi at every moment t is served simultaneously at rate ri = rφi /( j ∈B(t) φj ), where B(t)
is the set of flows that are backlogged at time t.
