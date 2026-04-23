# network-algorithmics-14-14-quick-fair-queueing-qfq (chunk 000001)

# Network Algorithmics — 14.14 Quick fair queueing (QFQ) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 446
- Slice: from `14.14 Quick fair queueing (QFQ)` up to next detected section heading

---

14.14 Quick fair queueing (QFQ)
Recall from Section 14.11 that the WF2 Q scheduling algorithm can closely approximate the GPS
scheduler with the smallest possible T-WFI (the maximum amount by which the real finish time of
any packet under a certain policy can either lead or lag behind that under GPS, as defined in Sec-
tion 14.11) of O(L). It does so with time complexity O(log n) using the sophisticated data structures
described in Section 14.12 (for tracking GPS clock and sorting GPS virtual finish times) and Sec-
tion 14.13 (for checking eligibility). In this section, we describe a scheduling algorithm called QFQ
(Quick Fair Queueing) that can achieve nearly the same T-WFI as WF2 Q, yet has a time complexity of
only O(1).
