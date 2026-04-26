# Network Algorithmics — 14.11 Worst-case fair weighed fair queueing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 435
- Slice: from `14.11 Worst-case fair weighed fair queueing` up to next detected section heading

---

14.11 Worst-case fair weighed fair queueing
In this section we describe another scheduling policy called worst-case fair WFQ or WF2 Q in
short (Bennett and Zhang, 1996b). WF2 Q is a modification of WFQ to improve its fairness. We have
just shown that, under WFQ, any packet cannot finish service much later than it would under GPS.
However, the former could lead the latter by a considerable amount. Due to this potential large lead in
the short-term, there can be significant unfairness in serving different flows, as we will show using an
example taken from the WF2 Q paper (Bennett and Zhang, 1996b).
    In this example there are 11 flows denoted as F 1, F 2, ..., F 11. Among them flows F 1, F 2, ..., F 10
each has weight 1, and flow F 11 has weight 10. With this weight assignment, flows F 1, F 2, ..., F 10 get
50% of the link rate, and flow F 11 gets the other 50%. Flows F 1, F 2, ..., F 10 each has a packet arrival
at (real) time 0, whereas flow F 11 has 10 packet arrivals at (real) times 0, 0.1, 0.2, ..., 0.9, respectively.
All packets have the same length of 1 bit and the service rate of the link is 1 bit per second. The GPS
graph of this packet arrival instance is shown in Fig. 14.18.
    Under WFQ the service order of the packets will be p11,1 , p11,2 , . . . , p11,10 , p1,1 , p2,1 , . . . , p10,1 .
In other words, under WFQ, F 11 gets all its 10 packets served before all other 10 flows have their 10
packets. Although this is consistent with the intended 50/50 rate allocation, the manner this allocation
is made sounds very unfair: F11 gets the entirety of its 50% allocation before all the other 10 flows get
any. Another way to look at this unfairness is that the packet p11,10 has a real finish time of 20 under
GPS but a real finish time of 10 under WFQ, so the former leads the latter by 10.
    This lead time can grow as O(nL), where n (n = 11 here) is the total number of flows and L (L = 1
here) is the maximum packet length, since for any n, we can create a packet arrival instance like that
shown in Fig. 14.18, in which one flow (like F 11 here) get 50% bandwidth and the other n − 1 flows
(like F 1, F 2, . . ., F 10 here) share the remaining 50% equally. For a certain scheduling policy, the
maximum amount by which the real finish time of any packet under the policy can either lead or lag
behind that under GPS is called T-WFI (Bennett and Zhang, 1996b) of the policy, where T stands for
(real finish) time and WFI stands for weighted fair index. Using this definition, we can say that the
T-WFI of WFQ is O(nL).
    As WFQ is already a close approximation to GPS, readers might wonder if we can design a much
fairer packet scheduling policy than WFQ at all. Quite surprisingly, the answer is yes, and the solution is
WF2 Q. It was shown in Bennett and Zhang (1996b) that WF2 Q has the smallest (best) possible T-WFI
of O(L) (that does not grow with n). The WF2 Q policy can be succinctly stated as follows.

          14.12 The data structure and algorithm for efficient GPS clock tracking                         409




FIGURE 14.18
A motivating example for WF2 Q.


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
