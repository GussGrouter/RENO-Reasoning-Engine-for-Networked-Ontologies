# network-algorithmics-13-21-exercises-1-take-a-ticket-state-machine-draw-a-state-machine-for-take-a (chunk 000003)

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
