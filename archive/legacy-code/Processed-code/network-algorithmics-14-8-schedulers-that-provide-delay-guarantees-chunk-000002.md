# network-algorithmics-14-8-schedulers-that-provide-delay-guarantees (chunk 000002)

manner: the (scheduling) policy statement of WFQ contains references to the GPS virtual finish times
of packets, and hence its implementation requires tracking of GPS clock;. Both concepts will be defined
in Section 14.9.4.
     For decades it was widely believed that GPS clock tracking operation required a prohibitively high
computational complexity of O(n) per packet (Parekh and Gallager, 1993; Bennett and Zhang, 1996a;
Stiliadis and Varma, 1996b,a; Bennett and Zhang, 1997; Chao and Guo, 2001), where n is the num-
ber of concurrent flows. For this reason, WFQ was always been considered impractical; consequently,
several WFQ approximation schemes (e.g., Zhang, 1991; Bennett and Zhang, 1996a, 1997; Cobb et
al., 1996; Stiliadis and Varma, 1996b; Suri et al., 1997) have been proposed to reduce this complex-
ity to O(log n) per packet, all at a cost of GPS tracking errors. However, it is now known that the
worst-case computational complexity of GPS tracking can indeed be bounded by O(log n) per packet
using an augmented data structure proposed in Valente (2004). With this, the complexity of WFQ can
also be bounded by O(log n) per packet, making WFQ arguably as computationally efficient as WFQ
approximation schemes.
     The next sections (Sections 14.9 through Section 14.14) begin a more rigorous explanation of why
providing delay bounds together with fairness is challenging. While it is hard to appreciate the in-
novation behind Quick Fair Queuing (Section 14.14) without these preliminaries, implementors less
interested in the theoretical foundations may wish to skip to Section 14.14.
