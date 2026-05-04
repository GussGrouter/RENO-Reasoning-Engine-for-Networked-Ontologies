# network-algorithmics-13-14-the-queue-proportional-sampling-strategy (chunk 000001)

# Network Algorithmics — 13.14 The queue-proportional sampling strategy (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 383
- Slice: from `13.14 The queue-proportional sampling strategy` up to next detected section heading

---

13.14 The queue-proportional sampling strategy
In SERENA, the way a (typically partial) starter matching A (t) is derived from the arrival graph A(t)
can be viewed as a proposing process: each input port i “proposes” to an output port j , if and only
if the edge (i, j ) belongs to A(t), by sending the output port j a message containing the length of the
corresponding VOQ; an output port, upon receiving proposals from one or more input ports, accepts the
one whose corresponding VOQ is the longest. As explained earlier, this starter matching A (t), which
is typically partial, is then populated into a full matching R(t), and it is finally refined into the final
matching S(t) via merging with S(t − 1).
    This A(t)-generated proposing strategy is quite sensible because, at each input port, an output port
is always proposed with a probability proportional to the packet arrival rate of the corresponding VOQ.
However, this proposing strategy has a subtle shortcoming: it is oblivious to the current lengths of N
VOQs at each input port, so not enough attention is devoted to reducing the lengths of longest VOQs.
For example, a VOQ with many packets but without recent arrivals, which could happen under bursty
traffic, will mostly be denied service until it has new arrivals.
    In Gong et al. (2017) researchers proposed a data structure that allows the switch to constantly
maintain a keen “situational awareness” of the lengths of its N 2 VOQs. This data structure supports, in
constant (i.e., O(1)) time, an operation called queue-proportional sampling that generates an excellent
starter matching. It was shown in Gong et al. (2017) that SERENA, when using the QPS-generated
starter matching instead (called QPS-SERENA), has better delay performances than when using the
A(t)-generated starter matching. In addition, just like SERENA, QPS-SERENA can also attain 100%
throughput under all traffic patterns.
    Furthermore, scheduling algorithms that start from “scratch” (i.e., an empty matching), such as iS-
LIP, may also benefit significantly from QPS by instead starting from a QPS-generated starter matching.
It was shown in Gong et al. (2017) that iSLIP, when using a QPS-generated starter matching instead
(called QPS-iSLIP), attains higher throughputs and better delay performances than iSLIP under various
traffic patterns.
    The QPS proposing strategy, at any input port, is extremely simple to state: the input port proposes
to an output port with a probability proportional to the length of the corresponding VOQ. QPS’s name
comes from the fact that the output port proposed to by any input port is sampled, out of all N output
ports, using the queue-proportional distribution at the input port.
    We will shortly describe a data structure and algorithm that can perform a QPS operation (at an input
port) in O(1) time. The constant time complexity of the QPS operation may be surprising to readers
since even to “read” the lengths of all N VOQs at an input port takes O(N ) time. However, a short
explanation of this “paradox” is that the QPS operation really only needs to track the small number of
changes in the lengths of these N VOQs, caused by packet arrivals to and departures from the input port
during a time slot. This is exactly what the QPS data structure does: gain constant situational awareness
via learning incrementally (P12a) over time rather than in one shot.

13.15 QPS implementation               357
