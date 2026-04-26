# network-algorithmics-14-15-2-universal-packet-scheduler (chunk 000002)

Suppose we now use another set of packet scheduling algorithms {Aα } on these routers, and the
resulting schedule given the same packet arrival instance is {(path(p), i(p), o (p))|p ∈ P } where o (p)
is the departure time of p under {Aα }. In Mittal et al. (2015), {Aα } is said to replay {Aα } if o (p) ≤ o(p)
for all p ∈ P . A universal packet scheduler is one that, when used by all routers, can be “manipulated”
to replay any viable schedule, defined as one that can be produced by a certain {Aα }. Here, information
used to “manipulate” a universal packet scheduler is limited to header values commonly used for packet
scheduling such as a priority value or a timestamp. For example, a packet p is not allowed to have a
“full route schedule” in the header that specifies the departure deadlines of p from every hop along
path(p).
    The following theoretical results were shown in Mittal et al. (2015). First, under some mild and
commonsense assumptions, no universal packet scheduler can exist in general. Second, if for every
packet p ∈ P there are at most two congestion points along its path, then it is possible to manipulate
the Least Slack Time First (LSTF) algorithm (Leung, 1989) into a universal packet scheduler, where the
manipulation is to assign the appropriate slack (in the schedule) value in its packet header at the ingress
point. A congestion point is a node (router) where a packet has to wait for its turn to be transmitted.
Third, if there can be at most one congestion point along the path of every packet, then the simple
priority scheduling algorithm can also be manipulated into a universal packet scheduler, where the
manipulation is to assign each packet p an appropriate priority value. Finally, if there can be three more
congestion points along the path of a packet, then again no universal packet scheduler can exist. The
second and the third results can be useful in practice, since in both data center and wide-area networks,
typically there can be at most two congestion points along each path: the ingress router and the egress
router.
