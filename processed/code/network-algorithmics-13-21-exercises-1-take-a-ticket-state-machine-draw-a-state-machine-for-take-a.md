# Network Algorithmics — 13.21 Exercises 1. Take-a-Ticket State Machine: Draw a state machine for take-a-ticket. Describe the state machine (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 406
- Slice: from `13.21 Exercises 1. Take-a-Ticket State Machine: Draw a state machine for take-a-ticket. Describe the state machine` up to next detected section heading

---

13.21 Exercises
1. Take-a-Ticket State Machine: Draw a state machine for take-a-ticket. Describe the state machine
   using pseudocode, with a state machine for each sender and each receiver. Extend the state machine
   to handle hunt groups.
2. Knockout Implementation: There are dependencies between the knockout trees. The simplest im-
   plementation passes all the losers from the Position j − 1 tree to the Position j tree. This would take
   k log N gate delays because each tree takes log N gate delays. Find a way to pipeline this process
   such that Tree j begins to work on each batch of losers as they are determined by Tree j − 1, as
   opposed to waiting for all losers to be determined. Draw your implementation using 2-by-2 concen-
   trators as your building block and estimate the worst-case delay in concentrator delays.

380      Chapter 13 Switching



3. PIM unfairness: In the knockout example using just one tree can lead to unfairness; a collection of
   locally fair decisions can lead to global unfairness. Surprisingly, PIM can also lead to some form of
   unfairness (but not to persistent starvation). Consider a 2-by-2 switch, where input 1 has unlimited
   traffic to outputs 1 and 2, and input 2 has unlimited traffic to output 1.
   • Show that, on average, input 1 will get two grants from outputs 2 and 1 for half the cell slots and
     one grant (for output 2 only) for the remaining cell slots. What fraction of output 2’s link should
     input 1 receive?
   • Infer, based on the preceding fraction of output 1’s bandwidth, what input 1 receives on average
     versus input 2. Is this fair?
4. Motivating the iSLIP Pointer Increment Rule: The following is one unfairness scenario if point-
   ers in iSLIP are incremented incorrectly. For example, suppose in Fig. 13.10 that input port A always
   has traffic to output ports 1, 2, and 3, whose grant pointers are initialized to A. Suppose also that
   input ports B and C also always have traffic to 2. Thus initially A, B, and C all grant to 1, which
   chooses A. In the second iteration since input port 2 has traffic to B, 2 and B are matched.
   • Suppose B increments its grant pointer to 3 based on this second iteration match. Between which
     port pairs can traffic be continually starved if this scenario persists?
   • How does iSLIP prevent this scenario?
5. Clos Proof Revisited: The Clos proof is based on a reduction that looks and is simple. However,
   until you try a few twists that do not work, you may not appreciate its simplicity. In our reduction
   each iteration routed n pairs, one per input stage, using just one middle switch. Suppose instead that
   any set of middle switches is used that had free input and output links. Show, by counterexample,
   why the reduction does not work.
6. Benes Switch Load-Balancing Proof: In the Benes switch the chapter argued that any link one
   hop from the output cannot be overloaded, assuming perfect load balancing at the first stage. It is
   helpful to work out with some simple cases to provide intuition before turning, if needed, to the
   proof provided in Turner (1997).
   • Repeat the same proof for links one hop away from the network, but this time for a two-copy
     network. Does the proof change for a three-copy network?
   • Repeat all the proofs for links two hops away. Do you see a pattern that can now be stated
     algebraically (Turner, 1997)?
7. Avici TSR and 3D Grid Layout: It seems a good bet that layout and packaging will be increasingly
   important as switches scale up in speeds. Extend the layout drawing in Fig. 13.22 for a 1D torus to
   a 2D and a 3D torus. Then, read Dally (2002) to learn how the Avici TSR packages its 3D mesh in
   a box.
8. Switching Using iSLIP: As shown in Fig. 13.23, the switch is the same as shown in Fig. 13.8.
   However, the inputs and the starting values of accept–grant pointers are different. You need to show
   intermediate steps like in Figs. 13.8 and 13.9.
   • Please draw a cell transmission timing chart like Fig. 13.10.
   • Please write down the values of grant and accept pointers after the transmission of all these cells.

                                                                       13.21 Exercises         381




FIGURE 13.23
Switching using iSLIP.




FIGURE 13.24
R(t).


9. Switching Using SERENA: Assume an 8 × 8 crossbar is being scheduled. At a time slot t, the new
   random matching R(t) (derived from the arrival graph) and the matching S(t − 1) used during the
   previous time slot, including the weight of each edge in both matchings, are shown in Figs. 13.24
   and 13.25 respectively. Please draw or specify the matching S(t) that results from MERGING R(t)
   with S(t − 1).

382         Chapter 13 Switching




FIGURE 13.25
S(t − 1).

                                                                                                   CHAPTER


Scheduling packets
                                                                                            14
                                                                           A schedule defends from chaos and whim.
                                                                                                    —Annie Dillard



From arranging vacations to making appointments, we are constantly scheduling activities. A busy
router is no exception. Routers must schedule the handling of routing updates, management queries,
and, of course, data packets. Data packets must be scheduled in real time by the forwarding proces-
sors within each line card. This chapter concentrates on the efficient scheduling of data packets, while
allowing certain classes of data packets to receive different services from other classes.
    Returning to our picture of a router (Fig. 14.1), recall that packets enter on input links and are
looked up using the address lookup component. Address lookup provides an output-link number, and
the packet is switched to the output link by the switching system. Once the packet arrives at the output
port, the packet could be placed in a FIFO (first in, first out) queue. If congestion occurs and the output
link buffers fill up, packets arriving at the tail of the queue are dropped. Many routers use such a default
output-link scheduling mechanism, often referred to as FIFO with tail-drop.
    However, there are certainly other options. First, we could place packets in multiple queues based
on packet headers and schedule these output queues according to some scheduling policy. There are
several policies, such as priority and round-robin, that can schedule packets in a different order than
FIFO. Second, even if we had a single queue, we need not always drop from the tail when buffers
overflow; we can, surprisingly, even drop a packet when the packet buffer is not full.
    Packet scheduling can be used to provide (to a flow of packets) so-called quality of service (QoS)
guarantees on measures such as delay and bandwidth. We will see that QoS requires packet schedul-
ing together with some form of reservations at routers. We will only briefly sketch some reservation
schemes, such as those underlying RSVP (Boyle, 1997) and DiffServ (Blake et al., 1998), and we refer
the reader to the specifications for more details. This is because the other parts of the QoS picture,
such as handling reservations, can be handled out-of-band at a slower rate by a control processor in
the router. Since this book concentrates on implementation bottlenecks, this chapter focuses on packet
scheduling.
    We will briefly examine the motivation for some popular scheduling choices. More importantly, we
will use our principles to look for efficient implementations. Since packet scheduling is done in the
real-time path, as is switching and lookup, it is crucial that scheduling decisions can be made in the
minimum interpacket times because links scale to OC-768 (40-gigabit) speeds and higher.
    This chapter is organized as follows. Section 14.1 presents the motivation for providing QoS guar-
antees. Section 14.2 describes random early detection (RED) schemes, which are better suited to TCP
congestion control than tail-drop. Section 14.3 describes a fair queueing technique called Approximate
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00021-X
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                            383

384       Chapter 14 Scheduling packets




FIGURE 14.1
Router model: This chapter concentrates on the third bottleneck, B3, scheduling of data packets.


Fair Dropping (AFD) that has a similarly low time complexity as RED, yet a similarly good QoS guar-
antee as Deficit Round Robin. Section 14.4 offers a simple scheme to limit the bandwidth and burstiness
of a flow, and Section 14.5 describes a basic priority scheme. Section 14.6 provides a brief introduction
to reservation protocols. Section 14.7 presents simple techniques to apportion the available link band-
width among competing flows. The section also briefly describes how the accompanying reservations
for flow bandwidths can be made. Section 14.8 provides an introduction to how one can provide good
delay guarantees for a flow at the cost of sorting packet deadlines in real time.
    Sections 14.9 through Section 14.14 begin a technical description of how to ensure both delay
bounds and fairness, culminating in Quick Fair Queuing that is implemented in the Linux kernel. These
sections can be skipped by more practical readers who may want to skip to Section 14.14. Section 14.9
introduces generalized processor sharing (GPS), the fairest possible scheduling policy. Although the
GPS policy is not practically implementable, a key component of it called GPS clock tracking is. This
implementation is described in Section 14.12. GPS clock tracking lies at the heart of implementing
weighted fair queueing (WFQ) and worst-case fair weighted-fair queueing (WF2 Q), two practically
implementable packet scheduling policies that are almost as fair as GPS. They are described in Sec-
tion 14.10 and Section 14.11, respectively. Section 14.14 describes Quick Fair Queuing (QFQ), a packet
scheduling algorithm that provides a QoS guarantee similar to WF2 Q, yet has an implementation com-
plexity comparable to DRR.
    Finally, Section 14.15 describes two research proposals towards making packet scheduling pro-
grammable in switches and routers: PIFO in Section 14.15.1 and UPS in Section 14.15.2. Section 14.16
describe several scalable schedulers that are able to schedule a large number of flows with little or no
state.
    The packet-scheduling techniques described in this chapter (and the corresponding principles in-
volved) are summarized in Table 14.1.

                                                             14.1 Motivation for quality of service                     385




  Quick reference guide
  The most important scheduling algorithms that an Internet router must implement are RED (Section 14.2), token buckets
  (Section 14.4), priority queueing (Section 14.5), deficit round-robin (DRR) (Section 14.7.3), and DiffServ (for DiffServ,
  consult only the relevant portion of Section 14.16). Other interconnect devices, such as SAN switches and gateways, are
  not required to implement RED; however, implementing some form of QoS, such as DRR or token buckets, in such devices
  is also a good idea. Cisco routers also implement Approximate Fair Dropping (Section 14.3) as a cheaper alternative to
  DRR. Finally, Quick Fair Queuing (QFQ), described in Section 14.14, provides comparable implementation complexity
  to DRR but has much better delay bounds; it was incorporated into the Linux kernel.




              Table 14.1 Summary of packet-scheduling techniques used in this chapter
              and the corresponding principles.
              Number                     Principle                           Scheduling technique
              P7          Use power of two parameters                 RED
              P3          Use policing, not shaping                   Token bucket policing
              P3          Focus on bandwidth only                     DRR
              P12         Maintain list of active queues
              P7          Use large enough quanta
              P3a         Aggregate by hashing flows                  SFQ
              P3c         Shift work to edge routers                  DiffServ
              P10         Incrementally compute interest vector
              P10         Pass class in TOS field                     Core stateless
              P2b         clean up lazily                             GPS clock tracking using shape data
                                                                      structure
              P15         use augmented data structure
              P3b         schedule among groups using DRR             QFQ
              P14         use bucket sorting, bitmaps
              P4c         use built-in instruction
