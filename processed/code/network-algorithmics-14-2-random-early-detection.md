# Network Algorithmics — 14.2 Random early detection (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 413
- Slice: from `14.2 Random early detection` up to next detected section heading

---

14.2 Random early detection
RED is a packet-scheduling algorithm implemented in most modern routers, even at the highest speeds,
that has become a de facto standard. In a nutshell a RED router monitors the average output-queue
length; when this goes beyond a threshold, it randomly drops arriving packets with a certain probability,
even though there may be space to buffer the packet. The dropped packet acts as a signal to the source
to slow down early, preventing a large number of dropped packets later.
    To understand RED, we must review the Internet-congestion-control algorithm. The top of Fig. 14.2
shows a network connecting source S and destination D. Imagine the network had links with a capacity
of 1 Mbps and that a file transfer can occur at 1 Mbps. Now suppose the middle link is replaced by
a faster, 10-Mbps link. Surely it can’t make things worse, can it? Well, in the old days of the Internet
it did. Packets arrived at a 10-Mbps rate at the second router, which could only forward packets at
1 Mbps; this caused a flood of dropped packets, which led to slow retransmissions. This resulted in a
very low throughput for the file transfer.
    Fortunately, the dominant Internet transport protocol, TCP, added a mechanism called TCP conges-
tion control, which is depicted in Fig. 14.2. The source maintains a window of size W , which is the
number of packets the source will send without an acknowledgment. Controlling window size controls
the source rate because the source is limited to a rate of W packets in a trip delay to the destination. As
shown in Fig. 14.2, a TCP source starts W at 1. Assuming no dropped packets, the source increases its

                                                                         14.2 Random early detection                     387




FIGURE 14.2
An illustration of TCP congestion control as a prelude to RED.


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


    The implementation of RED is more complex than it seems. First, we need to calculate the output-
queue size using a weighted average with weight w. Assuming that each arriving packet uses the queue
size it sees as a sample, the average queue length is calculated by adding (1 − w) times the old average
queue size to w times the new sample. In other words, if w is small, even if the sample is large, it
only increases the average queue size by a small amount. The average queue size changes slowly as
a result and needs a large number of samples to change value appreciably. This is done deliberately
to detect congestion on the order of round-trip delays (100 milliseconds) rather than instantaneous
congestion that can come and go. However, we can avoid unnecessary generality (P7) by allowing the
w to be only a reciprocal of a power of 2; a typical value is 1/512. There is a small loss in tunability
compared to allowing arbitrary values of w. However, the implementation is more efficient because the
multiplications reduce to easy bit shifting.
    However, there’s further complexity to contend with. The drop probability is calculated using the
function shown in Fig. 14.4. When the average queue size is below a minimum threshold, the drop
probability is zero; it then increases linearly to a maximum drop probability at the maximum threshold;
beyond this all packets are dropped. Once again, we can remove unnecessary generality (P7) and use
appropriate values, such as MaxThreshold being twice MinThreshold and MaxP a power of 2. Then the
interpolation can be done with two shifts and a subtract.
    But wait, there’s more. The version of RED so far is likely to drop more than one packet in a burst
of closely spaced packets for a source. To make this less likely and fast retransmit more likely to work,
the probability calculated earlier is scaled by a function that depends on the number of packets queued
(see Peterson and Davy, 2000 for a pithy explanation) since the last drop. This makes the probability
increase with the number of nondropped packets, making closely spaced drops less likely.
    But wait, there’s even more. There is also the possibility of adding different thresholds for different
types of traffic; for example, bursty traffic may need a larger minimum threshold. Cisco has introduced
weighted RED, where the thresholds can vary depending on the TOS bits in the IP header. Finally, there
is the thorny problem of generating a random number at a router. This can be done by grabbing bits
from some seemingly random register on the router; a possible example is the low-order bits of a clock
that runs faster than packet arrivals. The net result is that RED, which seems easy, takes some care in
practice, especially at gigabit speeds. Nevertheless, RED is quite feasible and is almost a requirement
for routers being built today.

                                                         14.3 Approximate fair dropping            389




FIGURE 14.4
Calculating drop probabilities using RED thresholds.
