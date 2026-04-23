# Network Algorithmics — 14.10 Weighted fair queueing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 434
- Slice: from `14.10 Weighted fair queueing` up to next detected section heading

---

14.10 Weighted fair queueing
In this section and the next we distinguish a packet-scheduling policy from a packet-scheduling al-
gorithm, just as we distinguish policy from the mechanism in the OSs literature. This distinction will
become clearer once we show how succinctly the WFQ policy can be stated and how hard it is to do
the same for the WFQ algorithm.
    We now describe WFQ (Parekh and Gallager, 1993), the aforementioned packet-by-packet work-
conserving scheduling policy that closely approximates the GPS policy. To state the WFQ policy, it
suffices to specify the service order of packets during a busy period because, for all work-conserving
scheduling policies, their busy periods are identical (and hence not ambiguous) given any packet arrival
instance. Also due to the work-conserving nature of WFQ, it suffices to specify which packet should
be chosen for transmission next, when the current packet finishes transmission, since idling (between
serving two consecutive packets) is not allowed in a work-conserving policy. With the concept of GPS
virtual finish time defined, the WFQ policy on “who is (to be serviced) next” can be succinctly stated
as follows:
Among all packets currently in the queue, pick the one with the earliest GPS virtual finish time
to serve next.
    We highlight a subtle property of the WFQ policy. The policy remains the same if we replace the
term “virtual finish time” with “expected real finish time” (when the “who is next” decision has to be
made) in its statement. This is because it is not hard to show that, for any pair of real times τ1 ≤ τ2 ,
their corresponding virtual times satisfy V (τ1 ) ≤ V (τ2 ): thus, sorting based on virtual finish times is
the same as sorting based on real finish times. However, the policy statement after this replacement
is bad from an implementation point of view. This is because (as explained earlier) the real time that
corresponds to a future virtual time v is not finalized until v arrives. In contrast, the virtual finish time
of a packet is determined as soon as the packet arrives and will not change afterward, as stated in Fact 1
in Section 14.9.2.
    To illustrate how WFQ policy works and to give readers intuition on how it should be implemented,
we use WFQ to schedule the packet arrival instance shown in Fig. 14.16. It is not hard to check that the
resulting service order is p3,1 , p3,2 , p2,2 , p1,1 , p1,2 , p2,2 , and p3,3 .
    WFQ is considered a close approximation to GPS: it has been proven (e.g., in Parekh and Gallager,
1993) that, given any packet arrival instance, the real finish time of each packet under WFQ schedul-
ing, minus that under GPS scheduling, is upper-bounded by the amount of time it takes to service a

408       Chapter 14 Scheduling packets



maximum-size packet at the full link rate r. For example, in the packet arrival instance, it is not hard to
verify that, for each of the seven packets, this difference is always upper-bounded by 7/1 = 7, where 7
is the maximum packet size and r = 1 is the link rate.
    Next, we briefly discuss the WFQ algorithm, the implementation of the WFQ policy. The WFQ
algorithm consists of two parts. The first part is the tracking of GPS clock, through which the GPS
virtual finish time of each packet can be determined. The second part is to have the GPS virtual finish
times of all packets currently in queue stored in a balanced priority queue data structure such as a heap,
so that “who is next” can be determined by making an ExtractMin() method call, which has O(log n)
time complexity per call (packet). Since the second part is straightforward, we only describe how to
implement the first part, GPS clock tracking, in detail in Section 14.12.
