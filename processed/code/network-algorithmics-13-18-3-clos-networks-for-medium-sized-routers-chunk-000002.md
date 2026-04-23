# network-algorithmics-13-18-3-clos-networks-for-medium-sized-routers (chunk 000002)

Clos networks in telephony
Clos’s insight was to see that, if k ≥ 2n − 1, then the resulting Clos network could indeed√simulate a
crossbar (i.e., is nonblocking), while still reducing the number of crosspoints to be 5.6N N instead
of N 2 . This can be big savings for large N . Of course, to achieve this crosspoint reduction, the Clos
network has increased latency by two extra stages of switching delay, but that is often acceptable.
    The proof of Clos’s theorem is easy to see from Fig. 13.17. If a hitherto-idle input i wishes to be
connected to an idle output o, then consider the first-stage switch S that I is connected to. There can be
at most n − 1 other inputs in S that are busy (S is an n-by-k switch). These n − 1 busy input links of S
can be connected to at most n − 1 middle-stage switches.
    Similarly, focusing on output o, consider the last-stage switch T that o is connected to. Then, T
can have at most n − 1 other outputs that are busy, and each of these outputs can be connected via
at most n − 1 middle-stage switches. Since both S and T are connected to k middle-stage switches,
if k ≥ 2n − 1, then it is always possible to find a middle-stage switch M that has a free input link to
connect to S and a free output link to connect to T . Since S and T are assumed to be crossbars or
otherwise nonblocking switches, it is always possible to connect i to the corresponding input link to M
and to connect the corresponding output link of M to√    o.
    If k = 2n − 1 and n is set to its optimal value of N/2, √ then the number of crosspoints (summed
across all smaller switches in Fig. 13.16) becomes 5.6N N. For example, for N = 512, this reduces
the number of crosspoints from 4.2 million for a crossbar to 516,096 for a three-stage Clos switch.
Larger telephone switches, such as the No. 1. ESS, which can handle 65,000 inputs, use an eight-stage
switch for further reductions in crosspoint size.

Reducing the size of the middle stage
On the other hand, for networking using VLSI switches, what is important is the total number of
switches and the number of links interconnecting switches. Recall that the largest possible switches
are fabricated in VLSI and that their cost is a constant, regardless of their crosspoint size. Juniper
Networks, for example, uses a Clos network to form effectively a 256-by-256 multichassis router by
connecting sixteen 16×16 T-series routers in the first stage.
    Using a standard Clos network for a fully populated multichassis router would require 16 routers
in the first stage, 16 in the third stage, and k = 2 ∗ 16 − 1 = 31 switches in the middle stage. Clearly,
Juniper can (and does) reduce the cost of this configuration by setting k = n. Thus the Juniper multi-
chassis router requires only 16 switches in the middle stage. This is exactly the construction of a large
                        √                                     √     √
m × m switch using 3 m small switches, each of the size m × m that we mentioned earlier.

368       Chapter 13 Switching

FIGURE 13.17
Proof that a Clos network with k = 2n − 1 is nonblocking.
