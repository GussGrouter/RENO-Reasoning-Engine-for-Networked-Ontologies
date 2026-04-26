# network-algorithmics-14-9-3-another-packet-arrival-scenario (chunk 000002)

More precisely, consider a packet scheduling scenario in which there are three flows, namely F 1,
F 2, and F 3, with weights 1, 1, and 2, respectively. They share a link again with service rate of r = 1
bit per second. The terms pi,j , ai,j and li,j are similarly defined as before. The packet arrival instance
consists of p1,1 with a1,1 = 0 and l1,1 = 20, p2,1 with a2,1 = 11 and l2,1 = 10, p3,1 with a3,1 = 23 and
l2,1 = 10, and finally p2,2 with a2,2 = 39 and l2,2 = 10.
    The GPS graph of this instance is shown in Fig. 14.17. The GPS virtual start and finish times of
the first packet p1,1 are straightforward to compute: s1,1 = 0 and f1,1 = 20. Those of later packets need
some reasoning. For the second packet p2,1 , its virtual start time s2,1 is 11 since F 1, being the only
active flow during the real time interval [0, 11], gets 11 bits of service in the meantime. Its virtual finish
time f2,1 is s2,1 + l2,1 /φ2 = 21. When packet p3,1 arrives at t = 23, the corresponding virtual time
V (23) is 17 because F 1 and F 2 are both active during the real time interval [11, 23], and each receives
6 bits of service under GPS. Hence, s3,1 = 17, and since F3 has weight 2 (so the height of packet p3,1
is twice as large as other packets), f3,1 = s3,1 + l3,1 /φ3 = 17 + 10/2 = 22.
    With this example explained, we are now ready to specify the evolution of the virtual time exactly.
Let ti , i = 0, 1, 2, · · · , be the ith real time when a past (i.e., earlier than the current time t) event hap-
pened that resulted in a change to the set of backlogged flows; note that we emphasize the word “past”
here since, at any real time t = η, the image of the function V (t) is finalized only for the real time in-
terval [0, η]. There are two types of such events. The first type is when a previously unbacklogged flow
becomes backlogged due to a new packet arrival (from this flow). For example, such an event happens
when packet p3,1 arrives in Fig. 14.17.
    In Fig. 14.16, however, the arrival of packet p1,2 at real time 3 does not cause such an event since
packets p1,1 and p1,2 are “back-to-back” (i.e., there is no gap in between) in the GPS graph and the
total weight of the backlogged flows remains unchanged. The second type of event is when a previously
backlogged flow becomes unbacklogged. For example, in Fig. 14.17 such an event happens when packet
p1,1 finishes service under GPS at real time 35.
    With this definition of ti , it is clear that t0 < t1 < t2 < · · · . The GPS virtual time V (t), as a function
of real time t, is calculated as (14.3) and (14.4) as follows.

V (t0 ) = 0,                                                      (14.3)

14.9 Generalized processor sharing               405

τ
                                V (ti−1 + τ ) = V (ti−1 ) +                    ,                     (14.4)
                                                               j ∈B(ti−1 ) φj
                                       0 ≤ τ ≤ ti − ti−1 ,   i = 1, 2, 3, · · ·
