# network-algorithmics-14-14-2-how-qfq-improves-upon-frr (chunk 000001)

# Network Algorithmics — 14.14.2 How QFQ improves upon FRR (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 447
- Slice: from `14.14.2 How QFQ improves upon FRR` up to next detected section heading

---

14.14.2 How QFQ improves upon FRR
QFQ improves upon FRR by reducing its technically O(1) (actually O(G log G)) time complexity to
true O(1), or in other words getting rid of its dependence on G, through three modifications. The first
modification is that it makes use of an approximate virtual time function V (t) proposed in what was
called WF2 Q+ (Bennett and Zhang, 1996a). WF2 Q+ is pretty much the same algorithm as WF2 Q except
that its V (t) only approximately tracks the GPS clock (whereas that of WF2 Q does so exactly). This
approximation, combined with the third modification to be described shortly, allows the WF2 Q+ clock
to be tracked with true O(1) (independent of both n and G) time complexity. The tradeoff (P3b) is that
its fairness guarantee, as measured by T-WFI, is slightly worse than that of WF2 Q.
     The second modification is that it assigns a flow Fk to a group based not only on its weight φk ,
but also on its maximum packet size Lk . More precisely, it assigns a flow Fk to flow group i, where
i = log2 (Lk /φk ) (with base C = 2). It was shown in Checconi et al. (2013) that the use of WF2 Q+
clock with this modification leads to the following nice property of QFQ that is key to its true O(1)
time complexity: The difference between the WF2 Q+ virtual finish times of the HOL packets of any
two flows in the system is bounded by a small universal constant δ, no matter what the traffic arrival
pattern is. A weaker version of this property is called the Globally Bounded Timestamp (GBT) property
in Bennett and Zhang (1996a).
     The third modification is that for the purpose of sorting (the WF2 Q+ virtual finish times of HOL
packets), in each group i, the WF2 Q+ virtual finish times are rounded to the multiples of a certain
unit value σi . For each group index i, the value of σi is defined to be 2i (bits). With this σi -integral
rounding, the rounded WF2 Q+ virtual finish time of any HOL packet can only take a small number
of possible values thanks to the GBT property described above. Hence the sorting of rounded WF2 Q+
virtual finish times (to decide which flow shall have its HOL packet transmitted) within any group
can be done in O(1) time using bucket sorting (P14). In the rest of this section, we drop the qualifier
“rounded WF2 Q+” with the understanding that all virtual finish and start times referred to below has
this qualifier.
     For any flow Fk that belongs to a group i ∗ , its maximum normalized packet length Lk /φk is less than
2σi ∗ as a result of how we assign flows to groups as described above. This property in turn guarantees
that the virtual finish time of any packet is no later than its virtual start time by more than 2σi . For
each group i, define s (i) to be the earliest virtual start time among all flows (their HOL packets) in

14.14 Quick fair queueing (QFQ)                421
