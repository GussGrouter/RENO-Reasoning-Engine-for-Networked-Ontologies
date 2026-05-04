# network-algorithmics-14-2-random-early-detection (chunk 000003)

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
