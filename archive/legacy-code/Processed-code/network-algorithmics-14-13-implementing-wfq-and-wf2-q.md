# Network Algorithmics — 14.13 Implementing WFQ and WF2 Q (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 445
- Slice: from `14.13 Implementing WFQ and WF2 Q` up to next detected section heading

---

14.13 Implementing WFQ and WF2 Q
It was shown in Valente (2004) that the shape data structure alone is sufficient for implementing WFQ.
However, WF2 Q is even harder to implement than WFQ because, in addition to tracking the GPS clock
and sorting the GPS virtual finish times, its implementation has to somehow maintain the set of eligible
packets. It was shown in Valente (2004) that another augmented data structure and algorithm, proposed
in Stoica and Abdel-Wahab (1995) for implementing a different scheduling policy called Earliest Eli-
gible Virtual Deadline First (EEVDF), can be used to carry out each WF2 Q operation, namely to find
the (next) eligible packet that has the lowest GPS virtual finish time, in O(log n) time in the worst case.
The WF2 Q implementation proposed in Valente (2004) contains both a shape data structure and an
EEVDF data structure. Each arriving packet is first processed by the shape data structure to obtain its
virtual start and finish times as described above, and then inserted into the EEVDF data structure for

                                                       14.14 Quick fair queueing (QFQ)              419



EEVDF scheduling; the virtual start and finish times of this packet are regarded as the eligible time and
the deadline respectively, for EEVDF scheduling. We summarize this data structure and algorithm into
an exercise problem in Section 14.18.
