# Network Algorithmics — 14.8 Schedulers that provide delay guarantees (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 426
- Slice: from `14.8 Schedulers that provide delay guarantees` up to next detected section heading

---

14.8 Schedulers that provide delay guarantees
So far, we have considered only schedulers that provide bandwidth guarantees across multiple queues.
Our only exception is MDRR, which is an ad hoc solution. We now consider providing delay bounds.
The situation is analogous to a number of chefs sharing an oven, as shown in Fig. 14.15. The frozen-
food chef (analogous to, say, FTP traffic) cares more about throughput and less about delay; the regular

400      Chapter 14 Scheduling packets




FIGURE 14.14
Cisco’s MDRR scheme.




FIGURE 14.15
Three types of chefs sharing an oven, among whom only the fast-food chef needs bounded delay.


chef (analogous to, say, SSH traffic) cares about delay, but for the fast-food chef (analogous to voice or
real-time video traffic) a small delay is critical for business.
    In practice, most routers implement some form of throughput sharing using algorithms such as
DRR. However, almost no commercial router implements schedulers that guarantee delay bounds. The
result is that real-time video (e.g., for remote surgery) may not work well at all times. This may be
unacceptable for commercial use. One answer to this problem is to have heavily underutilized links
and to employ ad hoc schemes like MDRR. This may work if bandwidth becomes plentiful. However,
traffic does go up to compensate for increased bandwidth; witness the spurt in traffic due to Netflix, for
instance.
    In theory, the simulated bit-by-bit round-robin algorithm (Demers et al., 1989) that we have already
mentioned guarantees isolation and delay bounds. Thus it was used as the basis for the IntServ proposal
as a scheduler that could integrate video, voice, and data. However, bit-by-bit round-robin, also called
generalized processor sharing and to be described next in detail, is unrealistic because it would require
(relatively) expensive context switching after each bit of service.
    WFQ, also called packetized generalized processor sharing (PGPS) in Parekh and Gallager (1993)
and to be described in Section 14.10, provides a close approximation to GPS. WFQ does not have the
issue of expensive context switching and is hence realistic since its scheduling is packet-by-packet, not
bit-by-bit. However, as will be shown in Section 14.10, WFQ depends subtly on GPS in the following

                                                       14.9 Generalized processor sharing                401



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
