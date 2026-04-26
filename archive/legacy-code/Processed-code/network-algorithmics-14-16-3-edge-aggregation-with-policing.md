# Network Algorithmics — 14.16.3 Edge aggregation with policing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 453
- Slice: from `14.16.3 Edge aggregation with policing` up to next detected section heading

---

14.16.3 Edge aggregation with policing
Using edge aggregation, two flows (say, F 1 and F 2) that have reserved bandwidth (say, B1 and B2 ,
respectively) could be aggregated into a class that has nominally reserved some bandwidth, which is
B ≥ B1 + B2 for all flows in the class. Consider Fig. 14.24. Suppose F 1 decides to oversubscribe and to
send at a rate greater than B. The edge router ER in Fig. 14.24 may currently have sufficient bandwidth
to allow all packets of flow F 1 and F 2 through. Unfortunately, when this aggregated class reaches the
backbone (core) router CR, suppose the core router is limited in bandwidth and must drop packets.
Ideally, CR should only drop oversubscribed flows like F 1 and let all of F 2’s packets through.
    How, though, can CR tell which flows are oversubscribed? It could do so by keeping state for all
flows passing through, but that would defeat scaling. A clever idea, called core-stateless fair queuing
(Stoica et al., 1998), makes the observation that the edge router ER has sufficient information to distin-
guish the oversubscribed flows. Thus ER can, using Principle P10, pass information in packet headers
to CR.
    How, though, should CR handle oversubscribed flows? Dropping all such marked packets may be
too severe. If there is enough bandwidth for some oversubscribed flows, it seems reasonable for CR to
drop in proportion to the degree a flow is oversubscribed. Thus ER should pass a value in the packet
header of a flow that is proportional to the degree a flow is oversubscribed. To implement this idea, CR
can drop randomly (P3a), with a drop probability that is proportional to the degree of oversubscription.
While this has some error probability, it is close enough. Most importantly, random dropping can be
implemented without CR keeping any state per flow. In effect, CR is implementing RED, but with the
drop probability computed based on a packet header field set by an edge router.
    While core-stateless is a nice idea, we note that unlike SFQ (which can be implemented in isola-
tion without cooperation between routers) and DiffServ (which has mustered sufficient support for its
standardized use of the TOS field), core-stateless fair queuing is, as of now, only a research proposal
(Stoica et al., 1998).



14.17 Summary
In this chapter we attacked another major implementation bottleneck for a router: scheduling data pack-
ets to reduce the effects of congestion and to provide fairness and QoS guarantees to certain flows. We

                                                                               14.18 Exercises           427



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



  (b) What is the service order of these packets under WFQ?
  (c) What is the service order of these packets under WF2 Q?
  (d) What is the service order of these packets under DRR when the quantum size is 3 bits?
 8. Reuse distance (Bennett and Kruskal, 1975) is a heavily studied concept in computer architecture
    and programming languages. Given a sequence of memory references (addresses accessed during
    the execution of a computer program), the reuse distance of a memory reference (say, to memory
    address a) is the number of distinct memory references that have happened between the previous ref-
    erence to a and this reference. For example, suppose the list of memory references is a, b, c, b, c, a.
    Then the reuse distance between the two consecutive references to a is 2, since only two distinct
    addresses, namely b and c, are referenced in between. Please design and implement in C++/C an
    augmented data structure that, given as input a long list of memory references (by a program), al-
    lows a companion algorithm to compute, for each memory access, its reuse distance in O(log N )
    time, where N is the number of distinct addresses in the list. (Hint: This augmented data structure
    subsumes one for implementing dynamic order statistics, which is the sole topic of Section 14.1
    in Cormen et al. (2009). Reading and understanding that section will make this problem much eas-
    ier to tackle.)
 9. As mentioned in Section 14.13, an augmented data structure and algorithm was proposed in Stoica
    and Abdel-Wahab (1995) for implementing the Earliest Eligible Virtual Deadline First (EEVDF)
    scheduling policy, in a computationally efficient manner. The EEVDF policy is used to schedule
    tasks in a system for service. Each task has a virtual deadline, that like a virtual time, is determined
    when this task arrives (to the system), and its value does not change thereafter. Each task also has a
    virtual eligible time te (that is also determined when the task arrives) in the sense when the current
    virtual time is at least te this task is eligible for service. The EEVDF policy is that, whenever the
    server becomes idle (right after finishing serving the current task), the scheduler needs to pick,
    among the eligible tasks (as determined by their eligible times), the one with the earliest virtual
    deadline for service. Now, please design an augmented data structure that can carry out the following
    three operations (and hence implements the EEVDF policy), all in O(log n) time, where n is the
    number of tasks in the system.
    • Insertion. When a new task arrives with a virtual eligible time and a virtual deadline, this method
      is called to insert the task into the data structure.
    • Searching. This method, with the current virtual time as its argument, is called when the sched-
      uler selects the next task for service. This method shall return, among the eligible tasks, the one
      with the earliest virtual deadline.
    • Deletion. This method is called to delete a task after the server finishes serving the task.
    Note in both insertion and deletion, rebalancing the base data structure (and correspondingly re-
    pairing the invariants of the augmented data structure) is necessary for guaranteeing O(log n) time
    complexity in the worse case. The design of this augmented data structure is much simpler than that
    of the shape data structure, so please refrain from reading Stoica and Abdel-Wahab (1995) while
    working on this problem.
10. Prove that the WF2 Q packet scheduling policy is work-conserving.
11. Construct a counterexample to show that the WF2 Q packet scheduling policy is not PIFO-
    compatible.

                                                                                                CHAPTER


Routers as distributed systems
                                                                                        15
                                                                           Come now and let us reason together.
                                                                                     —Isaiah 1:18, The Bible



Distributed systems are clearly evil things. They are subject to a lack of synchrony, a lack of assurance,
and a lack of trust. Thus in a distributed system, the time to receive messages can vary widely; messages
can be lost and servers can crash, and when a message does arrive, it could even contain a virus. In
Lamport’s well-known words a distributed system is “one in which the failure of a computer you didn’t
even know existed can render your own computer unusable.”
    Of course, the main reason to use a distributed system is that people are distributed. It would perhaps
be unreasonable to pack every computer on the Internet into an efficiency apartment in upper Manhat-
tan. But a router? Behind the gleaming metallic cage and the flashing lights, surely there lies an orderly
world of synchrony, assurance, and trust.
    On the contrary, this chapter argues that, as routers (recall routers include general interconnect
devices such as also switches and gateways) get faster, the delay between router components increases
in importance when compared to message-transmission times. The delay across links connecting router
components can also vary significantly. Finally, availability requirements make it infeasible to deal
with component failures by crashing the entire router. With the exception of trust, trust arguably exists
between router components, a router is a distributed system. Thus within a router, it makes sense to use
techniques developed to design reliable distributed systems.
    To support this thesis, this chapter considers four sample phenomena that commonly occur
within most high-performance interconnect devices, flow control, striping across links, striping across
DRAMs, and asynchronous data structure updates. In each case the desire for performance leads to
intuitively plausible schemes. However, the combination of failure and asynchrony can lead to subtle
interactions.
    Thus a second thesis of this chapter is that the use of distributed algorithms within routers requires
careful analysis to ensure reliable operation. While this is trite advice for protocol designers (who
ignore it anyway), it may be slightly more novel in the context of a router’s internal microcosm.
    The chapter is organized as follows. Section 15.1 motivates the need for flow control on long chip-
to-chip links and describes solutions that are simpler than, say, transmission control protocol’s (TCP)
window flow control. Section 15.2 motivates the need for internal striping across links and fabrics to
gain throughput and presents solutions that restore packet ordering after striping. Section 15.3 moti-
vates the need for further internal striping across DRAMs at high packet rates. Section 15.4 details the
difficulties of performing asynchronous updates on data structures that run concurrently with search
operations.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00022-1
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                         429

430       Chapter 15 Routers as distributed systems



               Table 15.1 Principles used in the various distributed systems techniques
               (for use within a router) discussed in this chapter.
               Number                        Principle                                       Used in
               P1     Avoid waste caused by partitioned buffers                       Internal flow control
               P13    Exploit degrees of freedom by decoupling logical from           Internal striping
                      physical reception
               P5c    Make fast buffers out of banks of DRAM with a DRAM              Distributed Memory
                      cache
               P3     Relax binary search requirements to allow duplicate             Binary search update
                      key values


    The techniques described in this chapter (and the corresponding principles invoked) are summarized
in Table 15.1.
    In all four examples in this chapter the focus is not merely on performance but also on the use of
design and reasoning techniques from distributed algorithms to produce solutions that gain performance
without sacrificing reliability. The techniques used to gain reliability include periodic synchronization
of key invariants and centralizing asynchronous computation to avoid race conditions. Counterexamples
are also given to show how easily the desire to gain performance can lead, without care, to obscure
failure modes that are hard to debug.
    The sample of internal distributed algorithms presented in this chapter is necessarily incomplete.
An important omission is the use of failure detectors to detect and swap out failed boards, switching
fabrics, and power supplies.

   Quick reference guide
   It is important for an implementor to learn how to make link flow control reliable, as described in Section 15.1.2. Im-
   plementors are increasingly turning to striping within networking devices. Solutions for link striping are described in
   Section 15.2. Solutions for striping across DRAMs while maintaining guarantees are described in Section 15.3.
