# network-algorithmics-14-9-2-recursive-definition-of-gps-virtual-start-and-finish-times (chunk 000002)

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
