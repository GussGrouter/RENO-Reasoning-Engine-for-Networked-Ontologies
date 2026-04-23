# network-algorithmics-14-9-3-another-packet-arrival-scenario (chunk 000001)

# Network Algorithmics — 14.9.3 Another packet arrival scenario (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 430
- Slice: from `14.9.3 Another packet arrival scenario` up to next detected section heading

---

14.9.3 Another packet arrival scenario
The following scenario was used in the aforementioned work that presented an algorithm for tracking
the GPS clock at a worst-case computational complexity of O(log n). It is different from the previous
simple scenario in two important aspects. First, all flows do not have the same weight. Second, whereas
the packets in the same flow are “back-to-back” and leave no “gaps” in the GPS graph of the previous
instance, there is a hole in this scenario. Now, when a new flow arrives at real time t, determining the
corresponding virtual time V (t) is no longer straightforward.

404       Chapter 14 Scheduling packets

FIGURE 14.17
GPS graph of a more complicated instance.
