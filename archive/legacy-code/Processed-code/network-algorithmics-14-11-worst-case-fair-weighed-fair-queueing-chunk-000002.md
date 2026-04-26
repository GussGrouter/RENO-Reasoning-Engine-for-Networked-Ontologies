# network-algorithmics-14-11-worst-case-fair-weighed-fair-queueing (chunk 000002)

Among all eligible packets currently in the queue, pick the one with the earliest GPS virtual finish
time to serve next.
    WF2 Q is only slightly different than WFQ in that “who is next” is picked only from those that are
eligible in the packet queue. At any time t, a packet is said to be eligible if and only if it should have
started service under GPS at t. Using the same packet arrival instance, we now show that WF2 Q policy
results in a much fairer service schedule given the packet arrival instance shown in Fig. 14.18.
    At time 0, packet p11,1 is the first to receive service under WF2 Q because it is eligible at time 0
(since its GPS start time is 0). The real time becomes 1 when p11,1 finishes service. However, unlike
in the schedule under WFQ, packet p11,2 cannot receive service next because, at this moment (real
time 1), the corresponding virtual time is only 0.05, but the GPS virtual start time of p11,2 is 0.1 (so it
is not eligible yet). Hence, p1,1 is serviced next (assuming flow ID is used for tiebreaking).
    When p1,1 finishes service at real time 2, p11,2 becomes eligible because the corresponding virtual
time is 0.1, and is hence serviced next. By this reasoning, the service order for the rest of the packets is
p2,1 , p11,3 , p3,1 , ..., p11,10 , p10,1 . In other words, the service alternates between F 11 and the other 10
flows. This schedule is much fairer because it can be shown (e.g., in Bennett and Zhang (1996b)) that,
for any packet, its real finish time under WFQ neither lags behind nor leads that under GPS by more
than L/r, the amount of time needed to service a maximum size packet.
