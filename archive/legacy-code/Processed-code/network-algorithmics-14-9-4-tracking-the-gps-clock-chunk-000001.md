# network-algorithmics-14-9-4-tracking-the-gps-clock (chunk 000001)

# Network Algorithmics — 14.9.4 Tracking the GPS clock (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 432
- Slice: from `14.9.4 Tracking the GPS clock` up to next detected section heading

---

14.9.4 Tracking the GPS clock
When p2,2 arrives at real time t = 39, we need to compute the corresponding virtual time V (39). In
Fig. 14.17 we “show” that this virtual time is “after” f2,1 = 21, but “before” f3,1 = 22. In practice,
such “before-and-after” relationships have to be determined before the value of V (39) can. One way to
compute such “before-or-after” relationships is to proactively compute and maintain the expected real
finish time of the last packet in each backlogged flow, as illustrated by the following example.
Example. In Fig. 14.17 at real time t = 23+ , the expected real finish times corresponding to the virtual
finish times f1,1 = 20, f2,1 = 21, and f3,1 = 22 are V −1 (20) = 23 + (20 − 17) ∗ 4 = 35, V −1 (21) =
35 + (21 − 20) ∗ 3 = 38, and V −1 (22)   = 38 + (22 − 21) ∗ 2 = 40, respectively. Note the multiplica-
tive terms 4, 3, and 2 are the values of j ∈B(ti−1 ) φj (the total weight of the backlogged flows) during
the intervals [17, 20], [20, 21], and [21, 22], respectively. As a2,2 = 39 is between V −1 (21) = 38 and
V −1 (22) = 40, we know that V (39) = 21 + (39 − 38)/2 = 21.5 (since V −1 (21) = 38 and the total
weight during real time interval [38, 39] is 2).
    This example also highlights an important fact mentioned earlier. That is, the tracking of the GPS
clock consists of two intertwined types of tasks. The first is to evaluate V −1 (ν) (i.e., to compute the
real time given a virtual time) and the second to evaluate V (t) (i.e., to compute the virtual time given a
past real time). Each type is dependent on the other. For example, in the instance shown in Fig. 14.17,
to evaluate V (39), we need to evaluate V −1 (21). But to obtain this virtual finish time 21 (of packet
p2,1 ), we need to evaluate V(11) = 11 (when packet p2,1 arrives at real time t = 11).
    Due to this interdependence, although only the GPS virtual finish times (of packets) are used in
the policy statements of WFQ and WF2 Q, as will be shown in Sections 14.10 and 14.11, respectively,
perhaps ironically the key difficulty in implementing both policies comes from a dilemma that arises in
computing the expected future real time (assuming no new flow would arrive before this future time)
corresponding to a future virtual (finish) time, as will be explained next.
    While both types of GPS clock tracking tasks can be accomplished by proactively computing and
maintaining the expected real finish times as shown in the previous example, the cost of doing so
however is a very high worst-case computational complexity of O(n) per packet. This is because, if
(the first packet of) a new flow arrives, all precomputed real finish times will change and need to be
recomputed, and there can be O(n) of them. Indeed, proactively computing the real finish times was
suggested in Parekh and Gallager (1993) as the algorithm for tracking the GPS clock as an integral part
of the WFQ algorithm. Most later papers cited (Parekh and Gallager, 1993) for the perceived complexity
of O(n) per packet for performing WFQ.

406      Chapter 14 Scheduling packets
