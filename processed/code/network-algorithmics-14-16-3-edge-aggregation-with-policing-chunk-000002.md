# network-algorithmics-14-16-3-edge-aggregation-with-policing (chunk 000002)

worked our way upward from schemes, such as RED, that provide congestion feedback to schemes that
provide QoS guarantees in terms of bandwidth and delay. We also studied how to scale the QoS state
to core routers using aggregation techniques such as DiffServ.
    A real router will often have to choose various combinations of these individual schemes. Many
routers today offer RED, Approximate Fair Dropping (AFD), token bucket policing, and multiple
queues and DRR. However, the major point is that all these schemes, with the exception of the schemes
that provide delay bounds, can be implemented efficiently.
    Even schemes that provide excellent delay bounds can be implemented fairly efficiently. For exam-
ple, we have shown that both WFQ and WF2 Q can provide excellent delay bounds with only O(log N )
time complexity (per packet), using a sophisticated shape data structure described in Section 14.12.
Furthermore, Quick Fair Queueing (QFQ) described in Section 14.14 can provide similar delay bounds
with O(1) time complexity. A number of combination schemes can also be implemented efficiently
using the principles we have outlined. The exercises explore some of these combinations.
    To make this chapter self-contained, we devoted a great deal of the discussion to explanations of top-
ics, such as congestion control and resource reservation, that are really peripheral to the main business
of this book. What we really care about is the use of our principles to attack scheduling bottlenecks.
Lest that be forgotten, we remind you as always, of the summary, in Table 14.1 of the techniques used
in this chapter and the corresponding principles.

14.18 Exercises
1. Consider what happens if there are large variations in the reserved bandwidths of flows, for example,
   F 1 with a rate of 1000 and F 2, . . . , F n with a rate of 1. Assuming that all flows have the same
   minimum packet size, show that flow F 1 can be locked out for a long period.
2. Consider the simple idea of sending one packet for each queue with an enabled quantum for each
   round in DRR. In other words, we interleave the packets sent in various queues during a DRR round
   rather than finishing a quantum’s worth for every flow. Describe how to implement this efficiently.
3. Work out the details of implementing a hierarchical DRR scheme.
4. Suppose an implementation wishes to combine DRR with token bucket shaping also on the queues.
   How can the implementation ensure that it skips empty queues (a DRR scan should not visit a queue
   that has no token bucket credits)?
5. Describe how to efficiently combine DRR with multiple levels of priority. In other words, there are
   several levels of priority; within each level of priority, the algorithm runs DRR.
6. Suppose that the required bandwidths of flows vary by an order of magnitude in DRR. What fairness
   problems can result? Suggest a simple fix that provides better short-term fairness without requiring
   sorting.
7. We consider a packet scheduling scenario in which there are three flows (denoted as F 1, F 2, and
   F 3) with equal weights. The j th packet of Fi is denoted pi,j . Its arrival time and length (in bits)
   are denoted as ai,j and li,j , respectively. Let a1,1 = a2,1 = a3,1 = 0. Let a1,2 = a2,2 = a3,2 = 1
   and a1,3 = a3,3 = 2. Let l1,1 = 2, l1,2 = 3, l1,3 = 6, l2,1 = 6, l2,2 = 3, l3,1 = 3, l3,2 = 1, and l3,3 = 6.
   Suppose the service rate of the link is 1 bit per second. Then
 (a) What is the GPS finish time of each packet?

428      Chapter 14 Scheduling packets
