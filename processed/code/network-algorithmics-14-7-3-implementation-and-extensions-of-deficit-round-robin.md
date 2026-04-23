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


link. For example, a transatlantic link may be shared by two organizations in proportion to the amount
each pays for the link. Consider two organizations, A and B, who respectively pay 70% and 30% of the
cost of a link and so wish to have assured bandwidth shares in that ratio. However, within organization
A there are two main traffic types: Web users and others. Organization A wishes to limit Web traffic to
get only 40% of A’s share of the traffic when other traffic from A is present. Similarly, B wishes video
traffic to take no more than 50% of the total traffic when other traffic from B is present (Fig. 14.13).
    Suppose at a given instant organization A’s traffic is only Web traffic and organization B has both
video and other traffic. Then A’s Web traffic should get all of A’s share of the bandwidth (say, 0.7 Mbps
of a 1-Mbps link); B’s video traffic should get 50% of the remaining share, which is 0.15 Mbps. If other
traffic for A comes on the scene, then the share of A’s Web traffic should fall to 0.7 × 0.4 = 0.28 Mbps.
CBQ is easy to implement using a hierarchical DRR scheduler for each node in the CBQ tree. For
example, we would use a DRR scheduler to divide traffic between A and B. When A’s queue gets
visited, we run the DRR scheduler for A’s traffic, which then visits the Web queue and the other traffic
queue and serves them in proportion to their quanta.

Deficit round-robin plus priority
A simple idea implemented by Cisco Systems (and called Modified DRR, or MDRR) is to combine
DRR with priority to allow minimal delay for voice over IP. The idea, depicted in Fig. 14.14, allows up
to eight flow queues for a router. A packet is placed in a queue based on bits in the IP TOS fields called
the IP precedence bits. However, queue 1 is a special queue typically reserved for voice over IP. There
are two modes: in the first mode queue 1 is given strict priority over the other queues. Thus in the figure
we would serve all three of queue 1’s packets before alternating between queues 2 and 3. On the other
hand, in alternating priority mode queue 1 visits alternate with visits to a DRR scan of the remaining
queues. Thus in this mode we would first serve queue 1, then queue 2, then queue 1, then queue 3, etc.
