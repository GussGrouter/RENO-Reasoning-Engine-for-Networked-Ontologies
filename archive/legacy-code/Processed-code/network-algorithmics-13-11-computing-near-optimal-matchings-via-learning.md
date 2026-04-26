# Network Algorithmics — 13.11 Computing near-optimal matchings via learning (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 379
- Slice: from `13.11 Computing near-optimal matchings via learning` up to next detected section heading

---

13.11 Computing near-optimal matchings via learning
Recall from Section 13.8 that a heavy matching, such as maximum weighted matching (MWM), is
generally a good matching in terms of throughput and delay performances. In most bipartite match-
ing algorithms for switching, such as PIM and iSLIP described earlier, the computation of the crossbar
schedule (matching) for each time slot is done from scratch, or in other words, oblivious of earlier com-
putations. This might sound computationally wasteful (P1). For example, a heavy matching computed
in the previous time slot typically remains heavy in the current time slot since, in the previous time slot,
there can be at most N departures, but possibly close to N arrivals under a heavy load. Intuitively, if
we can somehow learn the heavy edges from the matching used in the previous time slot, we may be
able to compute a new heavy matching incrementally (P12a) with a much lower time complexity than
to compute it from scratch. Indeed we can do just that with a family of adaptive algorithms that we will
describe in the next few sections.
    Besides the bipartite matching used in the previous time slot, there are other things an adaptive al-
gorithm can learn from earlier computations to help compute a good new matching faster. For example,
an intelligent adaptive algorithm can develop and maintain “situational awareness” of the weights of all
N 2 edges (VOQs) gradually over many past time slots, which can help the algorithm make quick, yet
wise, matching decisions, as will be shown in Section 13.14. In the next few sections we assume there
is an equal number N of input ports and output ports and that an edge is allowed to have weight 0 (i.e.,
with the corresponding VOQ being empty). Under both assumptions, a maximum matching (defined
in Section 13.8) always contains N edges and is necessarily a full matching. Hence, we use the term
full matching instead throughout this section to avoid any confusion.

                                    13.13 SERENA: an improved adaptive algorithm                  353
