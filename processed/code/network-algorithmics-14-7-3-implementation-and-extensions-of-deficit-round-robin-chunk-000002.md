# network-algorithmics-14-7-3-implementation-and-extensions-of-deficit-round-robin (chunk 000002)

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
