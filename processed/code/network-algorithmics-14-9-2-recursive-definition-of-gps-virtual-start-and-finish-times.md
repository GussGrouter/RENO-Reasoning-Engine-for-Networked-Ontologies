# Network Algorithmics — 14.9.2 Recursive definition of GPS virtual start and finish times (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 429
- Slice: from `14.9.2 Recursive definition of GPS virtual start and finish times` up to next detected section heading

---

14.9.2 Recursive definition of GPS virtual start and finish times
Although GPS cannot be used directly as a realistic scheduler as explained earlier, some concepts as-
sociated with GPS are important in specifying, reasoning about, and implementing realistic schedulers,
such as WFQ, WF2 Q (Bennett and Zhang, 1996a), and WFQ+ (Bennett and Zhang, 1997). One such
concept is the GPS virtual finish time of a packet pi,k , defined as the virtual time when this packet
finishes service under GPS and denoted as fi,k . For example, in Fig. 14.16 the GPS virtual finish time
of packet p3,2 is 4 (bits). Similarly, the GPS virtual start time of a packet pi,k is defined as the virtual
time at which the packet starts to receive service under GPS and denoted as si,k . For example, the GPS
virtual start time of p3,2 is 3. In general, the virtual start and the virtual finish times of any packet can
be computed from the following simple recursive formulae:

                                         si,k = max{fi,k−1 , V (ai,k )},                                 (14.1)
                                                       li,k
                                         fi,k = si,k +      .                                            (14.2)
                                                        φi
Here, V (ai,k ) is the virtual time that corresponds to ai,k , the real arrival time of pi,k . For example, when
packet p3,2 arrives at time a3,2 = 3, the corresponding virtual time V (3) = 13 because there are three
backlogged flows sharing GPS service during the real time interval [0, 1], and each receives 13 bits of
service. As stated in (14.1), the virtual start time of the packet pi,k is defined as the larger of fi,k−1 , the
virtual finish time of its previous packet pi,k−1 , and V (ai,k ). This is because, per GPS policy, a packet
pi,k cannot start receiving service under GPS until pi,k−1 , the previous packet in the same flow, finishes

                                                     14.9 Generalized processor sharing               403



service under GPS. Since in each GPS round flow Fi receives φi bits of service, the GPS virtual finish
        l
time is φi,ki bits later than the GPS virtual start time, which is precisely Formula (14.2). Formulae (14.1)
and (14.2) imply the following fact.
Fact 1. The virtual start and the virtual finish times of a packet are finalized as soon as the packet
arrives. In particular, they neither depend on nor change with, future packet arrivals.
    For example, when packet p3,3 arrives at real time 4 (seconds), its virtual start time s3,3 and virtual
finish time f3,3 , are known to be 4 (bits) and 10, respectively, and they remain unchanged even if a new
flow were to arrive to share the link bandwidth with the three existing flows shortly after real time 4
(say at real time 5). Since the x-axis corresponds to virtual times in a GPS graph, another way to state
this constancy of virtual start and finish times is that the start and the end positions of existing packets
(rectangles) in a GPS graph do not change with future packet arrivals.
    In contrast, the expected real finish time of a packet could change with future packet arrivals; this
fact was mentioned in Section 14.7.1 in the Parochial Parcel Service example. For this reason, it is not
not known for certain until the “finish” event actually happens. For example, at time 0+ , the expected
real finish time of packet p1,1 is 15 because, at the moment, the packet queue contains only three packets
p1,1 , p2,1 , and p3,1 whose lengths are 7, 5, and 3 bits, respectively, and it would take the GPS scheduler
15 seconds to finish serving p1,1 , the longest among the three. However, at time 3+ , its expected real
finish time becomes 18 due to the arrival of p1,2 , p2,2 , and p3,2 at real time 3, and becomes 21 due
to the arrival of p3,3 at real time 4. Furthermore, we do not know for certain that the real finish time
of p1,1 is indeed 21 until its virtual finish time 7 (known for certain since real time 0+ ) has passed at
real time 21. More generally, the real time corresponding to any future virtual time is not known for
certain until the (real and virtual) time occurs. This fact makes the task of tracking the GPS clock much
trickier, as will be shown in Section 14.9.4.
    As shown in Formula (14.1), when a packet pi,k arrives at real time ai,k , we need to obtain the corre-
sponding virtual time V (ai,k ). In other words, we need to compute the virtual time whose corresponding
real time is equal to ai,k .
    This virtual-to-real mapping is mathematically well-defined, or in other words does not suffer from
the “not finalized until the time has come” issue described earlier because here this mapping is per-
formed after this packet has already arrived (at time ai,k ). However, the computation involved in this
mapping, which is the bulk of the aforementioned GPS clock tracking task, is no easy matter, as we
elaborate in Section 14.9.4.
    Although this computation seems straightforward in Fig. 14.16, it is not when the scheduling in-
stance is less “friendly”. In the next section we will present a packet scheduling instance that is not
really larger than that in Fig. 14.16, but is a bit more contrived. Even in this fairly simple instance, GPS
clock tracking becomes more complex.
