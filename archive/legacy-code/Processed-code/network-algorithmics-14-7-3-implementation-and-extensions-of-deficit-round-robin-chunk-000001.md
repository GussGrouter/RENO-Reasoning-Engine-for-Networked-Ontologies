# network-algorithmics-14-7-3-implementation-and-extensions-of-deficit-round-robin (chunk 000001)

# Network Algorithmics — 14.7.3 Implementation and extensions of deficit round-robin (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 424
- Slice: from `14.7.3 Implementation and extensions of deficit round-robin` up to next detected section heading

---

14.7.3 Implementation and extensions of deficit round-robin
As described, DRR (Deficit Round Robin) has one major implementation problem. The algorithm may
visit a number of queues that have no packets to send. This would be very wasteful if the number of
possible queues is much larger than the number of active queues. However, there is a simple way to
avoid idle skipping of inactive queues by adding redundant state for speed (P12).
    More precisely, the algorithm maintains an auxiliary queue, ActiveList, which is a list of indices
of queues that contain at least one packet. In the example F 1, which was at the head of ActiveList,
is removed from ActiveList after its last packet is serviced. If F 1’s packet queue were nonempty, the
algorithm would place F 1 at the tail of ActiveList and keep track of any unused deficit. Notice that this
prevents a flow from getting quantum added to its account while the flow is idle.
    Note that DRR shares bandwidth among flows in proportion to quantum sizes. For example, sup-
pose there are three flows, F 1, F 2, and F 3, with respective quantum sizes 2, 2, and 3, which have

398       Chapter 14 Scheduling packets

FIGURE 14.12
Deficit round-robin (2): after sending out a packet of size 200, F 1’s queue had 300 bytes of its quantum left. It could
not use it in the current round, since the next packet in the queue is 750 bytes. Therefore the amount 300 will carry
over to the next round when it can send packets of size totaling 300 (deficit from previous round) + 500 (quantum).

reservations. Then, if all three are active, F 2 should get a fraction 2 + 22 + 3 = 2/7 of the output-link
bandwidth. If, for example, F 3 is idle, then F 2 is guaranteed the fraction 2 +2 2 = 1/2 of the output-link
bandwidth. In all cases a flow is guaranteed a minimum bandwidth, measured over the period that the
flow is active, that is proportional to the ratio of its quantum size to the sum of the quantum sizes of all
reservations.
    How efficient is the algorithm? The cost to dequeue a packet is a constant number of instructions,
as long as each flow’s quantum is greater than a maximum-size packet. This ensures that a packet is
sent every time a queue is visited. For example, if the quantum size of a flow is 1, the algorithm would
have to visit a queue 100 times to send a packet of size 100. Thus if the maximum packet size is 1500
and flow F 1 is to receive twice the bandwidth as flow F 2, we may arrange for the quantum of F 1 to be
3000 and the quantum of F 2 to be 1500. Once again, in terms of our principles, we note that avoiding
the generality (P7) of arbitrary quantum settings allows a more efficient implementation.

Extensions of deficit round-robin
We now consider two extensions of DRR: hierarchical DRR and DRR with a single priority queue.

Hierarchical deficit round-robin
An interesting model for bandwidth sharing is introduced in the so-called class-based queuing (CBQ)
scheme (Floyd and Jacobson, 1995). The idea is to specify a hierarchy of users that can share an output

14.8 Schedulers that provide delay guarantees              399

FIGURE 14.13
Example of a class-based queuing specification for bandwidth sharing.
