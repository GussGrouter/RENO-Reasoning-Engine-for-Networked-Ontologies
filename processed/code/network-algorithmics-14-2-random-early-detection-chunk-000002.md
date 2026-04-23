# network-algorithmics-14-2-random-early-detection (chunk 000002)

window size exponentially, doubling every round-trip delay until W reaches a threshold. After this, the
source increases W linearly.
    If there is a single dropped packet (this can be inferred from a number of acknowledgments with
the same number), the “gap” is repaired by retransmitting only the dropped packet; this is called fast
retransmit. In this special case the source detects some congestion and reduces its window size to half
the original size (Fig. 14.2) and then starts trying to increase again. If several packets are lost, the only
way for the source to recover is by having a slow, 200 milliseconds timer expire. In this case the source
infers more drastic congestion and restarts the window size at 1, as shown in Fig. 14.2.
    For example, with tail-drop routers, the example network shown at the top of Fig. 14.2 will probably
have the source ramp up until it drops some packets and then return to a window size of 1 and start again.
Despite this oscillation, the average throughput of the source is quite good because the retransmissions
rarely occur as compared to the example without congestion control. However, wouldn’t it be nicer if
the source could drop to half the maximum at each cycle (instead of 1) and avoid expensive timeouts
(200 msec) completely? The use of a RED router makes this more likely.
    The main idea in a RED (Floyd and Jacobson, 1993) router (Fig. 14.3) is to have the router detect
congestion early, before all its buffers are exhausted, and to warn the source. The simplest scheme,
called the DECbit scheme (Ramakrishnan and Jain, 1990), would have the router send a “congestion
experienced” bit to the source when its average queue size goes beyond a threshold. Since there is
no room for such a bit in current IPv4 headers, RED routers simply drop a packet with some small
probability. This makes it more likely that a flow causing congestion will drop just a single packet,
which can be recovered by the more efficient fast retransmit instead of a drastic timeout.1

1 But, what of sources that do not use TCP and use UDP? Since the majority of traffic is TCP, RED is still useful; the RED drops
also motivate UDP applications to add TCP-like congestion, a subject of active research. A more potent question is whether RED
helps small packet flows, such as Web traffic, which account for a large percentage of Internet traffic.

388       Chapter 14 Scheduling packets

FIGURE 14.3
RED is an early warning system that operates implicitly by packet dropping instead of explicitly by sending a bit as
in the DECbit scheme.
